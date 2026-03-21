#!/usr/bin/env python3
"""
Phase D10 — Trigger Selection Closure: Benchmark (60 checks).

Validates all levels of the trigger selection analysis:
candidates, regime tests, action compatibility, self-consistency
compatibility, scoring, ranking, classification, and serialization.
"""

import json
import math
import sys

from grut.trigger_selection import (
    # Constants
    N_TRIGGER_CANDIDATES,
    SCORE_CRITERIA,
    CONTRAST_THRESHOLD,
    TRIGGER_CLASSIFICATION_OPTIONS,
    TRIGGER_SELECTION_ASSUMPTIONS,
    TRIGGER_SELECTION_NONCLAIMS,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    R_EXT,
    KRETSCHNER_COEFF,
    ETA_TARGET,
    LAMBDA_DEFAULT,
    XI_DEFAULT,
    # Dataclasses
    TriggerSelectionParams,
    TriggerSelectionResult,
    # Functions
    compute_trigger_selection,
    trigger_selection_result_to_dict,
)

# ================================================================
# Benchmark infrastructure
# ================================================================

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
# Run the computation once
# ================================================================

params = TriggerSelectionParams()
result = compute_trigger_selection(params)

# ================================================================
# Section 1: Constants & Parameters (5 checks)
# ================================================================

print("\n=== Section 1: Constants & Parameters ===")
check("N_TRIGGER_CANDIDATES == 4", N_TRIGGER_CANDIDATES == 4)
check("SCORE_CRITERIA == 5", SCORE_CRITERIA == 5)
check("CONTRAST_THRESHOLD == 100.0", CONTRAST_THRESHOLD == 100.0)
check("R_EQ == 1/3", abs(R_EQ - 1.0/3.0) < 1e-10)
check("KRETSCHNER_COEFF == 12.0", abs(KRETSCHNER_COEFF - 12.0) < 1e-10)

# ================================================================
# Section 2: Trigger Candidate Definitions (5 checks)
# ================================================================

print("\n=== Section 2: Trigger Candidate Definitions ===")
check("result valid", result.valid)
check("4 candidates defined", len(result.candidates) == N_TRIGGER_CANDIDATES)
names = [c.name for c in result.candidates]
check("ricci_scalar in candidates", "ricci_scalar" in names)
check("kretschmann_sqrt in candidates", "kretschmann_sqrt" in names)
check("weyl_sqrt in candidates", "weyl_sqrt" in names)

# ================================================================
# Section 3: Vacuum Strong-Field Tests (6 checks)
# ================================================================

print("\n=== Section 3: Vacuum Strong-Field Tests ===")
rt_by_name = {r.candidate_name: r for r in result.regime_tests}

check("ricci_scalar vacuum_active = False",
      rt_by_name["ricci_scalar"].vacuum_active is False)
check("kretschmann_sqrt vacuum_active = True",
      rt_by_name["kretschmann_sqrt"].vacuum_active is True)
check("weyl_sqrt vacuum_active = True",
      rt_by_name["weyl_sqrt"].vacuum_active is True)
check("ricci_squared_sqrt vacuum_active = False",
      rt_by_name["ricci_squared_sqrt"].vacuum_active is False)

# Kretschmann value at R_eq: sqrt(48)*0.5/(1/3)^3 = sqrt(48)*0.5*27
kretsch_expected = math.sqrt(48.0) * M_EXT / (R_EQ**3)
check("kretschmann value at R_eq correct",
      abs(rt_by_name["kretschmann_sqrt"].value_at_Req - kretsch_expected) < 1e-6)
check("kretschmann contrast > 100",
      rt_by_name["kretschmann_sqrt"].contrast_ratio > CONTRAST_THRESHOLD)

# ================================================================
# Section 4: Weak-Field Suppression Tests (6 checks)
# ================================================================

print("\n=== Section 4: Weak-Field Suppression Tests ===")
check("kretschmann weak_field_suppressed = True",
      rt_by_name["kretschmann_sqrt"].weak_field_suppressed is True)
check("weyl_sqrt weak_field_suppressed = True",
      rt_by_name["weyl_sqrt"].weak_field_suppressed is True)
check("kretschmann regime_correct = True",
      rt_by_name["kretschmann_sqrt"].regime_correct is True)
check("weyl regime_correct = True",
      rt_by_name["weyl_sqrt"].regime_correct is True)
check("ricci_scalar regime_correct = False",
      rt_by_name["ricci_scalar"].regime_correct is False)
check("ricci_squared regime_correct = False",
      rt_by_name["ricci_squared_sqrt"].regime_correct is False)

# ================================================================
# Section 5: D8 Action Compatibility (6 checks)
# ================================================================

print("\n=== Section 5: D8 Action Compatibility ===")
ac_by_name = {a.candidate_name: a for a in result.action_compatibility}

check("kretschmann naturally_compatible",
      ac_by_name["kretschmann_sqrt"].compatibility_level == "naturally_compatible")
check("weyl naturally_compatible",
      ac_by_name["weyl_sqrt"].compatibility_level == "naturally_compatible")
check("ricci_scalar naturally_compatible",
      ac_by_name["ricci_scalar"].compatibility_level == "naturally_compatible")
check("ricci_squared compatible_with_assumptions",
      ac_by_name["ricci_squared_sqrt"].compatibility_level == "compatible_with_assumptions")
check("kretschmann natural_in_action = True",
      ac_by_name["kretschmann_sqrt"].natural_in_action is True)
check("ricci_squared natural_in_action = False",
      ac_by_name["ricci_squared_sqrt"].natural_in_action is False)

# ================================================================
# Section 6: D9 Self-Consistent Compatibility (5 checks)
# ================================================================

print("\n=== Section 6: D9 Self-Consistent Compatibility ===")
sc_by_name = {s.candidate_name: s for s in result.sc_compatibility}

check("kretschmann stabilizing",
      sc_by_name["kretschmann_sqrt"].effect_on_iteration == "stabilizing")
check("weyl stabilizing",
      sc_by_name["weyl_sqrt"].effect_on_iteration == "stabilizing")
check("ricci_scalar neutral",
      sc_by_name["ricci_scalar"].effect_on_iteration == "neutral")
check("ricci_squared neutral",
      sc_by_name["ricci_squared_sqrt"].effect_on_iteration == "neutral")
check("all candidates d9_compatible",
      all(s.d9_compatible for s in result.sc_compatibility))

# ================================================================
# Section 7: Trigger Assessments & Scoring (6 checks)
# ================================================================

print("\n=== Section 7: Trigger Assessments & Scoring ===")
check("4 assessments", len(result.assessments) == N_TRIGGER_CANDIDATES)

a_by_name = {a.candidate.name: a for a in result.assessments}
check("kretschmann score = 5",
      a_by_name["kretschmann_sqrt"].total_score == 5)
check("weyl score = 5",
      a_by_name["weyl_sqrt"].total_score == 5)
check("ricci_scalar score = 2",
      a_by_name["ricci_scalar"].total_score == 2)
check("ricci_squared score = 1",
      a_by_name["ricci_squared_sqrt"].total_score == 1)
check("all scores have 5 criteria",
      all(len(a.score_breakdown) == SCORE_CRITERIA for a in result.assessments))

# ================================================================
# Section 8: Ranking & Closure Logic (6 checks)
# ================================================================

print("\n=== Section 8: Ranking & Closure Logic ===")
ranking = result.ranking
check("top_score = 5", ranking.top_score == 5)
check("runner_up_score = 5", ranking.runner_up_score == 5)
check("family has 2 members", len(ranking.family_members) == 2)
check("kretschmann in family", "kretschmann_sqrt" in ranking.family_members)
check("weyl in family", "weyl_sqrt" in ranking.family_members)
check("vacuum degeneracy note mentions distinct",
      "distinct" in ranking.vacuum_degeneracy_note.lower())

# ================================================================
# Section 9: Classification (6 checks)
# ================================================================

print("\n=== Section 9: Classification ===")
cl = result.classification
check("classification is valid option",
      cl.classification in TRIGGER_CLASSIFICATION_OPTIONS)
check("classification = best_supported",
      cl.classification == "kretschmann_family_trigger_best_supported_within_tested_framework")
check("phase_status = ASSESSED", cl.phase_status == "ASSESSED")
check("trigger_family has 2 members", len(cl.trigger_family) == 2)
check("proxy_caveat conditional = True",
      cl.proxy_caveat.trigger_closure_conditional is True)
check("phase_lock_update contains D10",
      "D10" in cl.phase_lock_update)

# ================================================================
# Section 10: Nonclaims & Serialization (4 checks)
# ================================================================

print("\n=== Section 10: Nonclaims & Serialization ===")
check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

d = trigger_selection_result_to_dict(result)
check("serializable to dict", isinstance(d, dict))

try:
    json_str = json.dumps(d)
    check("JSON-serializable", True)
except (TypeError, ValueError):
    check("JSON-serializable", False)

# ================================================================
# Section 11: Physics & Cross-Phase Consistency (5 checks)
# ================================================================

print("\n=== Section 11: Physics & Cross-Phase Consistency ===")

# Kretschmann and Weyl give identical values in vacuum
check("kretschmann == weyl at R_eq (vacuum)",
      abs(rt_by_name["kretschmann_sqrt"].value_at_Req
          - rt_by_name["weyl_sqrt"].value_at_Req) < 1e-10)

# Kretschmann contrast ratio = (R_ext/R_eq)^3 = 6^3 = 216
check("contrast ratio = 216.0",
      abs(rt_by_name["kretschmann_sqrt"].contrast_ratio - 216.0) < 1e-6)

# Ricci-family candidates all fail vacuum test
ricci_family = [a for a in result.assessments
                if a.candidate.invariant_type == "ricci_family"]
check("all ricci-family fail vacuum test",
      all(not a.regime_test.vacuum_active for a in ricci_family))

# Tidal-family candidates all pass vacuum test
tidal_family = [a for a in result.assessments
                if a.candidate.invariant_type == "tidal_family"]
check("all tidal-family pass vacuum test",
      all(a.regime_test.vacuum_active for a in tidal_family))

# D4 score ordering preserved: kretschmann > ricci_squared > ricci_scalar
d4_k = a_by_name["kretschmann_sqrt"].candidate.d4_score
d4_rs = a_by_name["ricci_scalar"].candidate.d4_score
d4_r2 = a_by_name["ricci_squared_sqrt"].candidate.d4_score
check("D4 score ordering preserved (K > R2 > R)",
      d4_k > d4_r2 > d4_rs)

# ================================================================
# Summary
# ================================================================

print("\n" + "=" * 60)
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"Trigger family: {cl.trigger_family}")
print(f"Top score: {ranking.top_score}/{SCORE_CRITERIA}")
print(f"Proxy caveat: conditional={cl.proxy_caveat.trigger_closure_conditional}")
print(f"Phase lock: {cl.phase_lock_update}")
print("=" * 60)
print(f"\nTotal: {_passed} passed, {_failed} failed out of {_passed + _failed}")

if _failed > 0:
    sys.exit(1)
