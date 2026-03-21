#!/usr/bin/env python3
"""Benchmark — Phase D5: Source-Coupled Defect Dynamics.

60 checks across 11 sections.
"""

import math
import sys
import json

from grut.source_coupled_defect import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    GAMMA_DEFAULT, GAMMA_SCAN_VALUES, SOURCE_AMPLITUDE,
    COMP_A_TARGET, N_COUPLING_TYPES, KRETSCHNER_COEFF, MASS_COEFF,
    # Assumptions / nonclaims
    SOURCE_COUPLED_ASSUMPTIONS, SOURCE_COUPLED_NONCLAIMS,
    # Dataclasses
    SourceCoupledDefectParams, NormalizationMap,
    # Functions
    build_normalization_map,
    define_source_couplings,
    construct_sourced_lagrangian,
    derive_sourced_radial_ode,
    solve_sourced_bvp,
    extract_sourced_energy,
    assess_component_A_recovery,
    assess_component_B_preservation,
    scan_gamma,
    inventory_pathologies,
    classify_source_coupled,
    compute_source_coupled_defect,
    source_coupled_defect_result_to_dict,
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
print("Benchmark — Phase D5: Source-Coupled Defect Dynamics")
print("=" * 60)

result = compute_source_coupled_defect()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

check("N_COUPLING_TYPES = 2", N_COUPLING_TYPES == 2)
check("GAMMA_DEFAULT = 1.0", GAMMA_DEFAULT == 1.0)
check("SOURCE_AMPLITUDE = M_EXT", SOURCE_AMPLITUDE == M_EXT)
check("COMP_A_TARGET > 1.0", COMP_A_TARGET > 1.0)
check("ETA_SQUARED = 1/(8*pi)",
      abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10)


# ================================================================
print("\n--- Section 2: Normalization Map (6 checks) ---")
# ================================================================

nm = result.normalization
check("Normalization map exists", nm is not None)
check("r_star = 1.0 (r_s units)", nm.r_star == 1.0)
check("X_star = 0.5 (M_ext/r_s^2)", abs(nm.X_star - 0.5) < 1e-10)
check("eta_value matches ETA_TARGET",
      abs(nm.eta_value - ETA_TARGET) < 1e-10)
check("Source nondim formula is 1/r_tilde^2",
      "1/r_tilde^2" in nm.source_nondim_formula)
check("Nondim map has Lambda_bar",
      "Lambda_bar" in nm.nondim_map)


# ================================================================
print("\n--- Section 3: Source-Coupling Choices (5 checks) ---")
# ================================================================

couplings = result.couplings
check("Couplings list exists", couplings is not None)
check("Two couplings defined", len(couplings) == 2)
check("Quadratic coupling first", couplings[0].coupling_type == "quadratic")
check("Quadratic preserves O(3)", couplings[0].symmetry_preserved)
check("Linear breaks symmetry", not couplings[1].symmetry_preserved)


# ================================================================
print("\n--- Section 4: Sourced Lagrangian (5 checks) ---")
# ================================================================

lag = result.lagrangian
check("Lagrangian exists", lag is not None)
check("4 Lagrangian terms", lag.n_terms == 4)
check("Coupling type = quadratic", lag.coupling_type == "quadratic")
check("Source formula contains M/r^2",
      "/r^2" in lag.source_formula)
check("Has source coupling term",
      any(t.name == "source_coupling" for t in lag.terms))


# ================================================================
print("\n--- Section 5: Sourced Radial ODE (6 checks) ---")
# ================================================================

req = result.radial_equation
check("Radial equation exists", req is not None)
check("Source sign is -1 (derived)", req.source_term_sign == "-1")
check("Sign derivation mentions Euler-Lagrange",
      "Euler" in req.sign_derivation or "EL" in req.sign_derivation
      or "L_int" in req.sign_derivation)
check("Full ODE contains gamma", "gamma" in req.full_ode)
check("Unsourced ODE matches D4",
      "lam*eta^2*f*(f^2-1)" in req.unsourced_ode)
check("Source term formula is non-empty",
      len(req.source_term_formula) > 5)


# ================================================================
print("\n--- Section 6: BVP Convergence (5 checks) ---")
# ================================================================

bvp = result.baseline_bvp
check("BVP result exists", bvp is not None)
check("BVP converged", bvp.converged)
check("f(r_max) ~ 1.0", abs(bvp.f_at_rmax - 1.0) < 0.05)
check("f_max <= 1.05 (no overshoot)", bvp.f_max <= 1.05)
check("Max residual finite", math.isfinite(bvp.max_residual))


# ================================================================
print("\n--- Section 7: Component A Recovery (6 checks) ---")
# ================================================================

ca = result.comp_a_result
check("Component A assessment exists", ca is not None)
check("Shape exponent target = -4.0", ca.shape_exponent_target == -4.0)
check("Shape exponent measured < 0", ca.shape_exponent_measured < 0)
check("Coefficient ratio > 0", ca.coeff_ratio > 0)
check("Coefficient ratio << 1 (insufficient)",
      ca.coeff_ratio < 0.1)
check("Classification is source_coupling_insufficient or partial",
      "insufficient" in ca.classification or "partial" in ca.classification)


# ================================================================
print("\n--- Section 8: Component B Preservation (6 checks) ---")
# ================================================================

cb = result.comp_b_result
check("Component B assessment exists", cb is not None)
check("Exponent target = -2.0", cb.exponent_target == -2.0)
check("Exponent measured < 0", cb.exponent_measured < 0)
check("No overshoot at baseline", not cb.f_overshoot)
check("Oscillation free", cb.oscillation_free)
check("Classification contains 'preserved'",
      "preserved" in cb.classification)


# ================================================================
print("\n--- Section 9: Gamma Scan (6 checks) ---")
# ================================================================

gs = result.gamma_scan
check("Gamma scan exists", gs is not None)
check("9 values scanned", gs.n_scanned == 9)
check("All converged", gs.n_converged == 9)
check("gamma=0 is first entry", gs.entries[0].gamma == 0.0)
check("Baseline ratio matches D4 (~0.0035)",
      abs(gs.entries[0].comp_A_ratio - 0.0035) < 0.002)
check("Best ratio > baseline",
      gs.best_ratio >= gs.entries[0].comp_A_ratio)


# ================================================================
print("\n--- Section 10: Pathology Inventory & Classification (5 checks) ---")
# ================================================================

pi = result.pathology_inventory
check("Pathology inventory exists", pi is not None)
check("No critical pathologies", pi.n_critical == 0)
check("At least one documented pathology", pi.n_pathologies >= 1)

cl = result.classification
check("Classification exists", cl is not None)
check("Phase lock has D5",
      "source_coupled_D5" in cl.phase_lock_update)


# ================================================================
print("\n--- Section 11: Nonclaims & Serialization (5 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = source_coupled_defect_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)
check("Serialization has normalization", "normalization" in d)
check("Serialization has classification",
      "classification" in d and len(d["classification"]["classification"]) > 0)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")

print(f"\nNormalization:")
print(f"  r_unit: {nm.r_unit}")
print(f"  X_star: {nm.X_star}")
print(f"  Source nondim: {nm.source_nondim_formula}")

print(f"\nSource term sign: {req.source_term_sign} (derived from EL)")

print(f"\nComponent A (three-part test):")
print(f"  Shape: {'PASS' if ca.shape_match else 'FAIL'} "
      f"(exponent {ca.shape_exponent_measured:.2f}, target {ca.shape_exponent_target})")
print(f"  Coefficient: {'PASS' if ca.coeff_match else 'FAIL'} "
      f"(ratio {ca.coeff_ratio:.4f})")
print(f"  Mechanism: {ca.mechanism}")

print(f"\nComponent B: {cb.classification}")
print(f"  Exponent: {cb.exponent_measured:.3f} (target {cb.exponent_target})")
print(f"  Coefficient: {cb.coefficient_measured:.6f} (target {cb.coefficient_target:.6f})")
print(f"  Monotonic: {cb.monotonic}, Oscillation-free: {cb.oscillation_free}")

print(f"\nGamma scan:")
print(f"  Best gamma: {gs.best_gamma}")
print(f"  Best ratio: {gs.best_ratio:.4f} (D4 baseline ~0.0035)")
print(f"  Viable window: {gs.viable_window}")
for e in gs.entries:
    print(f"    gamma={e.gamma:6.1f}  ratio={e.comp_A_ratio:.4f}  "
          f"B_pres={e.comp_B_preserved}")

print(f"\nPathologies: {pi.n_pathologies} total "
      f"(critical={pi.n_critical}, moderate={pi.n_moderate}, minor={pi.n_minor})")

if _failed > 0:
    sys.exit(1)
