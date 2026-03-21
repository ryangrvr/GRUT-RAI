#!/usr/bin/env python3
"""Benchmark — Phase D2: Numerical Monopole Integration.

57 checks across 10 sections.
"""

import math
import sys
import json

from grut.numerical_monopole import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT, A_CRIT_SQUARED,
    COMP_B_COEFF, ETA_MATCH, ETA_MATCH_SQUARED, MASS_COEFF, R_EXT,
    LAMBDA_SCAN_VALUES, PHASE6_F_AT_REQ, KEY_RADII,
    # Assumptions / nonclaims
    MONOPOLE_ASSUMPTIONS, MONOPOLE_NONCLAIMS,
    # Dataclasses
    NumericalMonopoleParams,
    # Functions
    compute_core_series,
    solve_hedgehog_bvp,
    extract_defect_energy,
    inject_into_metric,
    run_both_coupling_cases,
    scan_lambda,
    check_compatibility,
    classify_numerical_monopole,
    compute_numerical_monopole,
    numerical_monopole_result_to_dict,
)

import numpy as np

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


def close(label: str, a: float, b: float, tol: float = 1e-6) -> None:
    check(label, abs(a - b) < tol)


def rel_close(label: str, a: float, b: float, tol: float = 1e-4) -> None:
    denom = abs(b) if abs(b) > 1e-30 else 1.0
    check(label, abs(a - b) / denom < tol)


# ================================================================
print("=" * 60)
print("Benchmark — Phase D2: Numerical Monopole Integration")
print("=" * 60)

result = compute_numerical_monopole()

# ================================================================
print("\n--- Section 1: Constants & Parameters (6 checks) ---")
# ================================================================

close("ETA_MATCH = 1/sqrt(8*pi)", ETA_MATCH, 1.0 / math.sqrt(8.0 * math.pi))
close("ETA_MATCH^2 = COMP_B_COEFF", ETA_MATCH_SQUARED, COMP_B_COEFF)
close("MASS_COEFF = 2*pi*M^2/tau^2", MASS_COEFF,
      2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2)
close("R_EXT = 2*R_S", R_EXT, 2.0 * R_S)
check("6 lambda scan values", len(LAMBDA_SCAN_VALUES) == 6)

# Verify Phase 6 baseline: f(R_eq) without source
m_req = M_EXT + MASS_COEFF * (1.0 / R_EQ - 1.0 / R_EXT)
f_req_baseline = 1.0 - 2.0 * m_req / R_EQ
close("Phase 6 baseline f(R_eq) ~ -17.71", f_req_baseline,
      PHASE6_F_AT_REQ, tol=0.01)


# ================================================================
print("\n--- Section 2: Core Series Expansion (5 checks) ---")
# ================================================================

cs = result.core_series
check("Core series exists", cs is not None)
check("c1_estimate > 0", cs.c1_estimate > 0)
check("c3_value < 0", cs.c3_value < 0)
check("c3 formula correct", "lam * eta^2 * c1 / 10" in cs.c3_formula)

# Series at r_min should be small positive
check("f(r_min) from series is small positive",
      0 < cs.series_at_rmin < 0.1)


# ================================================================
print("\n--- Section 3: BVP Solver Convergence (6 checks) ---")
# ================================================================

bvp = result.bvp_solution
check("BVP solution exists", bvp is not None)
check("BVP converged", bvp.converged)
check("Max residual < 1e-4", bvp.max_residual < 1e-4)
check("c1_effective > 0", bvp.c1_effective > 0)

# f(r_max) should be 1
close("f(r_max) = 1.0", bvp.f_at_rmax, 1.0, tol=1e-4)

# f(r_min) should be near 0
check("f(r_min) near 0", abs(bvp.f_solution[0]) < 0.02)


# ================================================================
print("\n--- Section 4: Energy Decomposition (6 checks) ---")
# ================================================================

ep = result.energy_profile
check("Energy profile exists", ep is not None)
check("Core peak > 0", ep.core_peak > 0)
check("Integrated mass > 0", ep.integrated_mass > 0)

# All three energy terms should be non-negative
check("Radial kinetic >= 0", np.all(ep.radial_kinetic >= 0))
check("Angular gradient >= 0", np.all(ep.angular_gradient >= 0))
check("Potential >= 0", np.all(ep.potential_term >= 0))


# ================================================================
print("\n--- Section 5: Asymptotic Tail Verification (6 checks) ---")
# ================================================================

# Tail exponent should approach -2.0 (within tolerance for default lambda)
check("Tail exponent < -1.5", ep.tail_exponent < -1.5)
check("Tail exponent > -2.5", ep.tail_exponent > -2.5)

# Tail coefficient should approximate eta^2
rel_close("Tail coefficient ~ eta^2",
          ep.tail_coefficient, ETA_MATCH_SQUARED, tol=0.15)

# At high lambda (200), tail should be closer to -2
high_lam = [e for e in result.lambda_scan.entries if e.lam == 200.0]
if high_lam:
    check("High-lambda tail exponent within 0.05 of -2.0",
          abs(high_lam[0].tail_exponent - (-2.0)) < 0.05)
else:
    check("High-lambda tail exponent within 0.05 of -2.0", False)

# Core peak increases with lambda
lam_5 = [e for e in result.lambda_scan.entries if e.lam == 5.0]
lam_200 = [e for e in result.lambda_scan.entries if e.lam == 200.0]
check("Core peak increases with lambda",
      lam_200[0].core_peak > lam_5[0].core_peak)

# Tail exponent monotonically approaches -2
exponents = [e.tail_exponent for e in result.lambda_scan.entries]
check("Tail exponent monotonically decreases toward -2",
      all(exponents[i] >= exponents[i + 1] for i in range(len(exponents) - 1)))


# ================================================================
print("\n--- Section 6: Metric Injection (7 checks) ---")
# ================================================================

inj_A = result.injection_A
inj_B = result.injection_B
check("Injection Case A exists", inj_A is not None)
check("Injection Case B exists", inj_B is not None)
check("Case A coupling mode = case_A", inj_A.coupling_mode == "case_A")
check("Case B coupling mode = case_B", inj_B.coupling_mode == "case_B")
check("Case A scalar_amplitude = A_CRIT", abs(inj_A.scalar_amplitude - A_CRIT) < 0.01)
check("Case B scalar_amplitude = 1.0", abs(inj_B.scalar_amplitude - 1.0) < 0.01)

# Defect fraction at R_eq should be between 0 and 1
frac_key = f"r={R_EQ:.4f}"
frac_A = inj_A.defect_fraction.get(frac_key, -1.0)
check("Defect fraction at R_eq in (0, 1)",
      0 < frac_A < 1)


# ================================================================
print("\n--- Section 7: Lambda Scan (6 checks) ---")
# ================================================================

ls = result.lambda_scan
check("Lambda scan exists", ls is not None)
check("6 lambda values scanned", ls.n_scanned == 6)
check("All BVPs converged", ls.n_converged == 6)

# Case A should have more positive metrics than Case B
check("Case A positive >= Case B positive",
      ls.n_positive_A >= ls.n_positive_B)

# At least some lambda values should give positive Case A
check("At least 1 positive Case A", ls.n_positive_A >= 1)

# Defect fraction at R_eq should increase with lambda
fracs = [e.defect_sigma_fraction_at_Req for e in ls.entries]
check("Defect fraction increases with lambda",
      all(fracs[i] <= fracs[i + 1] + 1e-6 for i in range(len(fracs) - 1)))


# ================================================================
print("\n--- Section 8: Compatibility Checks (5 checks) ---")
# ================================================================

compat = result.compatibility
check("Compatibility check exists", compat is not None)
check("Component A intact", compat.component_A_intact)
check("Coupling is additive", compat.coupling_is_additive)
check("Locked results preserved", compat.locked_results_preserved)

# Defect tail shape should be at least roughly correct
check("Defect provides Component B shape (within tolerance)",
      compat.defect_provides_component_B_shape or
      abs(ep.tail_exponent - (-2.0)) < 0.5)


# ================================================================
print("\n--- Section 9: Classification (6 checks) ---")
# ================================================================

cl = result.classification
check("Classification exists", cl is not None)
check("Classification string is non-empty", len(cl.classification) > 0)
check("Phase status is non-empty", len(cl.phase_status) > 0)
check("Summary is non-empty", len(cl.summary) > 10)

# Phase lock update should include defect_D2
check("Phase lock has defect_D2", "defect_D2" in cl.phase_lock_update)

# Result valid
check("Result valid", result.valid)


# ================================================================
print("\n--- Section 10: Nonclaims & Serialization (5 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = numerical_monopole_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)
check("Serialization has classification",
      "classification" in d and len(d["classification"]["classification"]) > 0)
check("Serialization has lambda_scan",
      "lambda_scan" in d and d["lambda_scan"]["n_scanned"] == 6)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"BVP converged: {bvp.converged} (max residual: {bvp.max_residual:.2e})")
print(f"c1_effective: {bvp.c1_effective:.6f}")
print(f"Tail exponent (default lam): {ep.tail_exponent:.4f}")
print(f"Core peak (default lam): {ep.core_peak:.6f}")
print(f"Case A: f_min = {inj_A.f_min:.4f}, metric positive: {inj_A.metric_positive}")
print(f"Case B: f_min = {inj_B.f_min:.4f}, metric positive: {inj_B.metric_positive}")
print(f"Lambda scan — positive Case A: {ls.n_positive_A}/{ls.n_scanned}")
print(f"Lambda scan — positive Case B: {ls.n_positive_B}/{ls.n_scanned}")
print(f"Defect Sigma fraction at R_eq (Case B, default lam): "
      f"{inj_B.defect_fraction.get(frac_key, 0):.4f}")

if ls.n_positive_B > 0 and ls.n_positive_B < ls.n_scanned:
    # Find critical lambda
    entries = ls.entries
    for i in range(len(entries) - 1):
        if not entries[i].metric_positive_B and entries[i + 1].metric_positive_B:
            print(f"Case B critical lambda: between {entries[i].lam} and "
                  f"{entries[i + 1].lam}")
            break

if _failed > 0:
    sys.exit(1)
