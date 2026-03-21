#!/usr/bin/env python3
"""Benchmark — Phase D1: Defect-Sector Admissibility.

57 checks across 10 sections.
"""

import math
import sys
import json

from grut.defect_admissibility import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, MU_DEFAULT, LAMBDA_DEFAULT,
    N_FIELD_CANDIDATES, COMPONENT_B_TARGET_EXPONENT, DELTA_CORE,
    # Assumptions / nonclaims
    DEFECT_ASSUMPTIONS, DEFECT_NONCLAIMS,
    # Functions
    compute_defect_admissibility,
    defect_admissibility_result_to_dict,
    DefectAdmissibilityParams,
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


def close(label: str, a: float, b: float, tol: float = 1e-6) -> None:
    check(label, abs(a - b) < tol)


def rel_close(label: str, a: float, b: float, tol: float = 1e-4) -> None:
    denom = abs(b) if abs(b) > 1e-30 else 1.0
    check(label, abs(a - b) / denom < tol)


# ================================================================
print("=" * 60)
print("Benchmark — Phase D1: Defect-Sector Admissibility")
print("=" * 60)

result = compute_defect_admissibility()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

close("ETA_TARGET = 1/sqrt(8*pi)", ETA_TARGET, 1.0 / math.sqrt(8.0 * math.pi))
close("ETA_TARGET^2 = COMP_B_COEFF", ETA_TARGET ** 2, COMP_B_COEFF)
close("LAMBDA_DEFAULT = mu^2/eta^2", LAMBDA_DEFAULT, MU_DEFAULT ** 2 / ETA_TARGET ** 2)
close("COMP_B_COEFF = 1/(8*pi)", COMP_B_COEFF, 1.0 / (8.0 * math.pi))
check("N_FIELD_CANDIDATES = 3", N_FIELD_CANDIDATES == 3)

# ================================================================
print("\n--- Section 2: Field Content Assessment (6 checks) ---")
# ================================================================

fc = result.field_content
check("Field content exists", fc is not None)
check("3 candidates", fc.n_candidates == 3)
check("Real scalar: no monopole", not fc.candidates[0].supports_monopole)
check("Complex scalar: no monopole", not fc.candidates[1].supports_monopole)
check("O(3) triplet: supports monopole", fc.candidates[2].supports_monopole)
check("Selected: O3_triplet", fc.selected_name == "O3_triplet")

# ================================================================
print("\n--- Section 3: SSB Potential (5 checks) ---")
# ================================================================

p = result.potential
check("Potential exists", p is not None)
close("eta = mu/sqrt(lambda)", p.eta, p.mu / math.sqrt(p.lam))
rel_close("eta^2 matches COMP_B_COEFF", p.eta_squared, COMP_B_COEFF)
check("Vacuum manifold is S^2", "S^2" in p.vacuum_manifold)

# V(eta) = -mu^4/(4*lambda)
expected_V = -p.mu ** 4 / (4.0 * p.lam)
close("V at minimum", p.potential_at_minimum, expected_V)

# ================================================================
print("\n--- Section 4: Hedgehog Ansatz (5 checks) ---")
# ================================================================

a = result.ansatz
check("Ansatz exists", a is not None)
check("3 components", a.n_components == 3)
check("BC f(0)=0", a.boundary_conditions["f(0)"] == 0.0)
check("BC f(inf)=1", a.boundary_conditions["f(infinity)"] == 1.0)
check("Gradient squared formula present", "f'" in a.gradient_squared)

# ================================================================
print("\n--- Section 5: ODE Structure (6 checks) ---")
# ================================================================

o = result.ode
check("ODE exists", o is not None)
check("ODE formula contains f''", "f''" in o.ode_formula)
check("Coefficient of f': 2/r", o.coefficient_f_prime == "2/r")
check("Coefficient of f: -2/r^2", o.coefficient_f == "-2/r^2")
check("BC origin = 0", o.bc_origin == 0.0)
check("BC infinity = 1", o.bc_infinity == 1.0)

# ================================================================
print("\n--- Section 6: Energy Decomposition (6 checks) ---")
# ================================================================

e = result.energy
check("Energy exists", e is not None)

# At large r, angular gradient should dominate
check("Angular fraction > 0.99 at large r", e.angular_fraction_at_large_r > 0.99)

# Tail exponent should be close to -2.0
check("Tail exponent close to -2.0", abs(e.tail_exponent - (-2.0)) < 0.05)

# All three terms should be non-negative
import numpy as np
check("Radial kinetic >= 0", np.all(e.radial_kinetic >= 0))
check("Angular gradient >= 0", np.all(e.angular_gradient >= 0))
check("Potential >= 0", np.all(e.potential_term >= 0))

# ================================================================
print("\n--- Section 7: Asymptotic Tail (7 checks) ---")
# ================================================================

t = result.tail_proof
check("Tail proof exists", t is not None)
check("Shape compatible", t.shape_compatible)
check("Coefficient match (eta^2 = 1/(8*pi))", t.coefficient_match)
check("Fitted exponent within 0.05 of -2.0", t.exponent_deviation < 0.05)
check("Ratio test passes", t.ratio_match)
rel_close("Surviving coefficient = eta^2", t.surviving_coefficient, ETA_TARGET ** 2)
rel_close("Target coefficient = 1/(8*pi)", t.target_coefficient, COMP_B_COEFF)

# ================================================================
print("\n--- Section 8: Compatibility Inventory (6 checks) ---")
# ================================================================

ci = result.compatibility
check("Inventory exists", ci is not None)
check("6 questions", ci.n_questions == 6)
check("4 high severity", ci.n_high_severity == 4)
check("2 medium severity", ci.n_medium_severity == 2)

# Check scalar-memory relation question exists
scalar_q = [q for q in ci.questions if q.category == "scalar_memory_relation"]
check("Scalar-memory relation question present", len(scalar_q) == 1)

# All deferred to Phase D2
check("All deferred to Phase D2",
      all(q.deferred_to == "Phase D2" for q in ci.questions))

# ================================================================
print("\n--- Section 9: Classification (6 checks) ---")
# ================================================================

cl = result.classification
check("Classification exists", cl is not None)
check("Classification string exact",
      cl.classification == "provisional_candidate_extension_formulated")
check("Phase status = formulated", cl.phase_status == "formulated")
check("Shape compatible", cl.shape_compatible)
check("Phase lock has defect_sector_D1", "defect_sector_D1" in cl.phase_lock_update)
check("Result valid", result.valid)

# ================================================================
print("\n--- Section 10: Nonclaims & Serialization (5 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = defect_admissibility_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)
check("Serialization has classification",
      d.get("classification", {}).get("classification") ==
      "provisional_candidate_extension_formulated")
check("Serialization has tail_proof",
      "tail_proof" in d and d["tail_proof"]["shape_compatible"])

# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Selected field: O(3) triplet (pi_2(S^2) = Z)")
print(f"eta = {p.eta:.6f}, eta^2 = {p.eta_squared:.6f}")
print(f"Tail exponent: {t.fitted_exponent:.6f} (target: -2.0)")
print(f"Shape compatible: {t.shape_compatible}")
print(f"Coefficient match: {t.coefficient_match}")
print(f"Compatibility questions: {ci.n_questions} ({ci.n_high_severity} high)")
print(f"ODE max residual: {o.max_residual:.3e} (analytic profile approximation)")

if _failed > 0:
    sys.exit(1)
