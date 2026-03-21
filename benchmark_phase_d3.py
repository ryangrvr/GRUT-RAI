#!/usr/bin/env python3
"""Benchmark — Phase D3: Scalar/Triplet Unification.

57 checks across 10 sections.
"""

import math
import sys
import json

from grut.scalar_triplet_unification import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, LAMBDA_DEFAULT,
    N_RELATION_TYPES, N_TRIGGER_TYPES, N_MINIMAL_COUPLINGS,
    # Assumptions / nonclaims
    UNIFICATION_ASSUMPTIONS, UNIFICATION_NONCLAIMS,
    # Dataclasses
    ScalarTripletParams,
    # Functions
    define_relation_types,
    assess_relation_types,
    build_relation_taxonomy,
    define_trigger_types,
    assess_trigger_types,
    build_trigger_taxonomy,
    check_canon_preservation,
    define_minimal_couplings,
    rank_candidates,
    classify_unification,
    compute_scalar_triplet_unification,
    scalar_triplet_unification_result_to_dict,
)

# ---- harness ----
_passed = 0
_failed = 0


def check(label: str, condition: bool) -> None:
    global _passed, _failed
    if condition:
        _passed += 1
        print(f"  [PASS] {label}")
    else:
        _failed += 1
        print(f"  [FAIL] {label}")


# ================================================================
print("=" * 60)
print("Benchmark — Phase D3: Scalar/Triplet Unification")
print("=" * 60)

result = compute_scalar_triplet_unification()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

check("N_RELATION_TYPES = 4", N_RELATION_TYPES == 4)
check("N_TRIGGER_TYPES = 5", N_TRIGGER_TYPES == 5)
check("N_MINIMAL_COUPLINGS = 5", N_MINIMAL_COUPLINGS == 5)
check("ETA_TARGET = 1/sqrt(8*pi)",
      abs(ETA_TARGET - 1.0 / math.sqrt(8.0 * math.pi)) < 1e-10)
check("COMP_B_COEFF = 1/(8*pi)",
      abs(COMP_B_COEFF - 1.0 / (8.0 * math.pi)) < 1e-10)


# ================================================================
print("\n--- Section 2: Relation-Type Taxonomy (6 checks) ---")
# ================================================================

rt = result.relation_taxonomy
check("Relation taxonomy exists", rt is not None)
check("4 relation types", rt.n_types == 4)

# Check all four types present
names = [s.short_name for s in rt.specs]
check("Embedding type present", "embedding" in names)
check("Companion type present", "companion" in names)
check("Emergent type present", "emergent" in names)
check("Replacement type present", "replacement" in names)


# ================================================================
print("\n--- Section 3: Relation-Type Assessments (6 checks) ---")
# ================================================================

# All assessments should have scores in [0, 1]
check("All relation scores in range",
      all(0 <= a.overall_score <= 1 for a in rt.assessments))

# Embedding should score highest (canon preservation is the hardest filter)
embedding_a = [a for a in rt.assessments if a.type_id == 1][0]
companion_a = [a for a in rt.assessments if a.type_id == 2][0]
replacement_a = [a for a in rt.assessments if a.type_id == 4][0]

check("Embedding scores higher than replacement",
      embedding_a.overall_score > replacement_a.overall_score)

# Embedding and companion should preserve both components
check("Embedding preserves Component A", embedding_a.preserves_comp_A)
check("Embedding preserves Component B", embedding_a.preserves_comp_B)
check("Companion preserves Component A", companion_a.preserves_comp_A)

# Each assessment should have a verdict
check("All assessments have verdict",
      all(len(a.verdict) > 0 for a in rt.assessments))


# ================================================================
print("\n--- Section 4: Trigger-Type Taxonomy (6 checks) ---")
# ================================================================

tt = result.trigger_taxonomy
check("Trigger taxonomy exists", tt is not None)
check("5 trigger types", tt.n_types == 5)

# Check all five types present
trig_names = [s.short_name for s in tt.specs]
check("Explicit trigger present", "explicit" in trig_names)
check("Curvature trigger present", "curvature" in trig_names)
check("Source-density trigger present", "source_density" in trig_names)
check("Lag/processing trigger present", "lag_processing" in trig_names)


# ================================================================
print("\n--- Section 5: Trigger-Type Assessments (6 checks) ---")
# ================================================================

# All trigger assessments should be coherent
check("All triggers mathematically coherent",
      all(a.coherent for a in tt.assessments))

# Check GRUT-nativeness
curvature_t = [a for a in tt.assessments if a.trigger_id == 2][0]
explicit_t = [a for a in tt.assessments if a.trigger_id == 1][0]
lag_t = [a for a in tt.assessments if a.trigger_id == 4][0]

check("Curvature trigger is GRUT-native", curvature_t.grut_native)
check("Explicit trigger is NOT GRUT-native", not explicit_t.grut_native)
check("Lag trigger is GRUT-native", lag_t.grut_native)

# Curvature should score higher than explicit
check("Curvature scores higher than explicit",
      curvature_t.score > explicit_t.score)

# All should preserve canon
check("All triggers preserve canon",
      all(a.preserves_canon for a in tt.assessments))


# ================================================================
print("\n--- Section 6: Canon Preservation (6 checks) ---")
# ================================================================

cc = result.canon_checks
check("Canon checks exist", cc is not None)
check("4 canon checks (one per relation type)", len(cc) == 4)

# Embedding and companion should pass all
emb_cc = [c for c in cc if c.relation_type_id == 1][0]
comp_cc = [c for c in cc if c.relation_type_id == 2][0]
emerg_cc = [c for c in cc if c.relation_type_id == 3][0]
repl_cc = [c for c in cc if c.relation_type_id == 4][0]

check("Embedding passes all canon checks", emb_cc.all_pass)
check("Companion passes all canon checks", comp_cc.all_pass)
check("Emergent fails canon checks (undemonstrated)", not emerg_cc.all_pass)
check("Replacement fails canon checks (disrupts locked)", not repl_cc.all_pass)


# ================================================================
print("\n--- Section 7: Minimal Couplings (5 checks) ---")
# ================================================================

mc = result.minimal_couplings
check("Minimal couplings exist", mc is not None)
check("5 coupling candidates", len(mc) == 5)

# Check coupling diversity
rel_ids = set(c.relation_type_id for c in mc)
check("Couplings span multiple relation types", len(rel_ids) >= 2)

# First coupling should be embedding identification (0 new params)
check("Embedding identification has 0 new params", mc[0].n_new_params == 0)

# All should have descriptions
check("All couplings have descriptions",
      all(len(c.description) > 10 for c in mc))


# ================================================================
print("\n--- Section 8: Candidate Ranking (6 checks) ---")
# ================================================================

rk = result.ranking
check("Ranking exists", rk is not None)
check("At least 5 candidates ranked", rk.n_candidates >= 5)

# Ranking should be sorted by score descending
scores = [r.combined_score for r in rk.ranked]
check("Ranking is sorted by score descending",
      all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1)))

# Top-ranked should pass canon
check("Top-ranked passes canon", rk.ranked[0].canon_passes)

# Scores should be in reasonable range
check("All scores in [0, 1]",
      all(0 <= s <= 1 for s in scores))

# Top score should be > 0.5 (should have a clear leading candidate)
check("Top score > 0.5", rk.top_score > 0.5)


# ================================================================
print("\n--- Section 9: Classification (6 checks) ---")
# ================================================================

cl = result.classification
check("Classification exists", cl is not None)
check("Classification string is non-empty", len(cl.classification) > 0)
check("Phase status is non-empty", len(cl.phase_status) > 0)
check("Summary is non-empty", len(cl.summary) > 10)

# Phase lock update should include unification_D3
check("Phase lock has unification_D3",
      "unification_D3" in cl.phase_lock_update)

# Result valid
check("Result valid", result.valid)


# ================================================================
print("\n--- Section 10: Nonclaims & Serialization (5 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = scalar_triplet_unification_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)
check("Serialization has classification",
      "classification" in d and len(d["classification"]["classification"]) > 0)
check("Serialization has ranking",
      "ranking" in d and d["ranking"]["n_candidates"] >= 5)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"Top-ranked architecture: {cl.top_relation}")
print(f"Top-ranked trigger: {cl.top_trigger}")
print(f"Top combined score: {cl.top_score:.4f}")
print(f"Canon-passing candidates: "
      f"{sum(1 for r in rk.ranked if r.canon_passes)}/{rk.n_candidates}")

print("\nRelation-type scores:")
for a in rt.assessments:
    print(f"  {a.type_id}. {a.name[:45]:45s} = {a.overall_score:.4f} ({a.verdict})")

print("\nTrigger-type scores:")
for a in tt.assessments:
    print(f"  {a.trigger_id}. {a.name[:45]:45s} = {a.score:.2f} ({a.verdict})")

print("\nTop 5 ranked architectures:")
for r in rk.ranked[:5]:
    print(f"  #{r.rank} {r.notes:45s} score={r.combined_score:.4f} canon={r.canon_passes}")

if _failed > 0:
    sys.exit(1)
