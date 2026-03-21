#!/usr/bin/env python3
"""Benchmark — Phase D4: Embedded Triplet Unification Dynamics.

55 checks across 10 sections.
"""

import math
import sys
import json

from grut.unification_dynamics import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    XI_CONFORMAL, XI_DEFAULT, XI_SCAN_VALUES,
    MU0_SQUARED_DEFAULT, KRETSCHNER_COEFF,
    N_CURVATURE_INVARIANTS, N_LAGRANGIAN_TERMS, N_MODE_SECTORS,
    # Assumptions / nonclaims
    DYNAMICS_ASSUMPTIONS, DYNAMICS_NONCLAIMS,
    # Dataclasses
    UnificationDynamicsParams,
    # Functions
    construct_lagrangian,
    apply_embedding_ansatz,
    decompose_modes,
    derive_radial_mode_equation,
    assess_component_A_recovery,
    assess_component_B_preservation,
    assess_trigger_regime,
    inventory_artifacts,
    classify_dynamics,
    compute_unification_dynamics,
    unification_dynamics_result_to_dict,
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
print("Benchmark — Phase D4: Embedded Triplet Unification Dynamics")
print("=" * 60)

result = compute_unification_dynamics()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

check("N_LAGRANGIAN_TERMS = 4", N_LAGRANGIAN_TERMS == 4)
check("N_MODE_SECTORS = 4", N_MODE_SECTORS == 4)
check("N_CURVATURE_INVARIANTS = 3", N_CURVATURE_INVARIANTS == 3)
check("ETA_SQUARED = 1/(8*pi)",
      abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10)
check("MU0_SQUARED_DEFAULT < 0 (broken phase)",
      MU0_SQUARED_DEFAULT < 0)


# ================================================================
print("\n--- Section 2: Lagrangian Construction (5 checks) ---")
# ================================================================

lag = result.lagrangian
check("Lagrangian exists", lag is not None)
check("4 Lagrangian terms", lag.n_terms == 4)
check("Broken phase", lag.broken_phase)
check("VEV matches eta^2",
      abs(lag.vev_squared - ETA_SQUARED) < 0.01)
check("Effective mass formula present",
      "m_eff" in lag.effective_mass_formula)


# ================================================================
print("\n--- Section 3: Embedding Ansatz (5 checks) ---")
# ================================================================

ans = result.ansatz
check("Ansatz exists", ans is not None)
check("Hedgehog formula", "eta" in ans.ansatz_formula and "f(r)" in ans.ansatz_formula)
check("Radial mode formula", "eta" in ans.radial_mode_formula)
check("f(0) = 0", ans.boundary_f_origin == 0.0)
check("f(inf) = 1", ans.boundary_f_infty == 1.0)


# ================================================================
print("\n--- Section 4: Mode Decomposition (6 checks) ---")
# ================================================================

dec = result.decomposition
check("Decomposition exists", dec is not None)
check("BVP converged", dec.bvp_converged)
check("4 sectors", dec.n_sectors == 4)
check("Radial kinetic sector present",
      any(s.name == "radial_kinetic" for s in dec.sectors))
check("Angular gradient sector present",
      any(s.name == "angular_gradient" for s in dec.sectors))
check("Potential decays steeply (exponent < -5)",
      dec.potential_exponent < -5.0)


# ================================================================
print("\n--- Section 5: Radial Mode Equation (6 checks) ---")
# ================================================================

req = result.radial_equation
check("Radial equation exists", req is not None)
check("EOM formula present", len(req.eom_formula) > 10)
check("Scalar-memory formula present", len(req.scalar_memory_formula) > 10)
check("Radial is static", req.radial_is_static)
check("Scalar-memory is dynamic", req.scalar_memory_is_dynamic)
check("EOM has curvature coupling", req.eom_has_curvature_coupling)


# ================================================================
print("\n--- Section 6: Component A Recovery (6 checks) ---")
# ================================================================

ca = result.comp_a_assessment
check("Component A assessment exists", ca is not None)
check("Shape exponent target = -4.0", ca.shape_exponent_target == -4.0)
check("Shape exponent measured < 0", ca.shape_exponent_measured < 0)
check("Mechanisms not identical (honest)",
      not ca.mechanisms_identical)
check("Classification is non-empty", len(ca.classification) > 0)
check("All three pass is False (mechanism differs)",
      not ca.all_three_pass)


# ================================================================
print("\n--- Section 7: Component B Preservation (5 checks) ---")
# ================================================================

cb = result.comp_b_assessment
check("Component B assessment exists", cb is not None)
check("Angular tail target = -2.0",
      cb.angular_tail_exponent_target == -2.0)
check("Angular tail exponent < 0", cb.angular_tail_exponent_measured < 0)
check("Angular match (within tolerance)", cb.angular_match)
check("Classification is preserved or preserved_with_corrections",
      cb.classification in ("preserved", "preserved_with_corrections"))


# ================================================================
print("\n--- Section 8: Trigger Regime (6 checks) ---")
# ================================================================

tr = result.trigger_assessment
check("Trigger assessment exists", tr is not None)
check("3 invariants assessed", tr.n_invariants == 3)
check("Top-ranked is non-empty", len(tr.top_ranked_name) > 0)
check("Top-ranked score > 0.5", tr.top_ranked_score > 0.5)
# Kretschner should rank highest (nonzero in vacuum = robust)
check("Kretschner in invariants",
      any(inv.name == "kretschner_sqrt" for inv in tr.invariants))
check("Classification is non-empty", len(tr.classification) > 0)


# ================================================================
print("\n--- Section 9: Artifact Inventory & Classification (6 checks) ---")
# ================================================================

ai = result.artifact_inventory
check("Artifact inventory exists", ai is not None)
check("At least 5 artifacts", ai.n_artifacts >= 5)
check("At least 1 major artifact", ai.n_major >= 1)
check("All artifacts have descriptions",
      all(len(a.description) > 10 for a in ai.artifacts))

cl = result.classification
check("Classification exists", cl is not None)
check("Phase lock has D4",
      "unification_D4" in cl.phase_lock_update)


# ================================================================
print("\n--- Section 10: Nonclaims & Serialization (5 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = unification_dynamics_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)
check("Serialization has classification",
      "classification" in d and len(d["classification"]["classification"]) > 0)
check("Serialization has trigger",
      "trigger" in d and d["trigger"]["n_invariants"] == 3)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")

print(f"\nComponent A (three-part test):")
print(f"  Shape: {'PASS' if ca.shape_match else 'FAIL'} "
      f"(exponent {ca.shape_exponent_measured:.2f}, target {ca.shape_exponent_target})")
print(f"  Coefficient: {'PASS' if ca.coeff_match else 'FAIL'} "
      f"(ratio {ca.coeff_ratio:.4f})")
print(f"  Interpretation: {'SAME' if ca.mechanisms_identical else 'DIFFERENT'} "
      f"mechanisms")

print(f"\nComponent B: {cb.classification}")
print(f"  Angular exponent: {cb.angular_tail_exponent_measured:.3f} "
      f"(target {cb.angular_tail_exponent_target})")

print(f"\nTrigger regime: {tr.classification}")
print(f"  Top invariant: {tr.top_ranked_name} (score {tr.top_ranked_score:.2f})")
for inv in tr.invariants:
    print(f"    {inv.name}: score={inv.score:.2f}, "
          f"ssb={inv.ssb_achieved}, vacuum={inv.nonzero_in_vacuum}")

print(f"\nArtifacts: {ai.n_artifacts} total "
      f"(major={ai.n_major}, moderate={ai.n_moderate}, minor={ai.n_minor})")

if _failed > 0:
    sys.exit(1)
