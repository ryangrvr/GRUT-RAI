#!/usr/bin/env python3
"""Benchmark — Source-Law Program I (Loophole 5: X != M/r^2).

57 checks across 10 sections.  Validates all numerical results from
grut/source_law_program.py against analytically known targets.
"""

import math
import sys

from grut.source_law_program import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    RHO_EQ_COEFF, EPSILON_RC_COEFF, COMP_B_COEFF, PHI_GOLDEN,
    N_SOURCE_FAMILIES, COMPONENT_B_TARGET_EXPONENT, LOCKED_EXPONENT,
    DIAGNOSTIC_B_COEFF,
    # Assumptions / nonclaims
    SOURCE_LAW_ASSUMPTIONS, SOURCE_LAW_NONCLAIMS,
    # Functions
    compute_source_law_assessment,
    source_law_result_to_dict,
    SourceLawParams,
)

import json

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
print("Benchmark — Source-Law Program I (Loophole 5)")
print("=" * 60)

# Run the full assessment
result = compute_source_law_assessment()

# ================================================================
print("\n--- Section 1: Setup & Constants (5 checks) ---")
# ================================================================

close("ALPHA_VAC = 1/3", ALPHA_VAC, 1.0 / 3.0)
close("M_EXT = 0.5", M_EXT, 0.5)
close("TAU_CANONICAL ~ 1.2247", TAU_CANONICAL, math.sqrt(1.5), tol=1e-4)
close("COMP_B_COEFF = 1/(8*pi)", COMP_B_COEFF, 1.0 / (8.0 * math.pi))
check("N_SOURCE_FAMILIES = 5", N_SOURCE_FAMILIES == 5)

# ================================================================
print("\n--- Section 2: Target Definition (5 checks) ---")
# ================================================================

t = result.target
check("Target exists", t is not None)
close("Target epsilon exponent = -2.0", t.target_epsilon_exponent, -2.0)
close("Required source exponent = -1.0", t.required_source_exponent, -1.0)
close("Standard source exponent = -2.0", t.standard_source_exponent, -2.0)
close("Standard epsilon exponent = -4.0", t.standard_epsilon_exponent, -4.0)

# ================================================================
print("\n--- Section 3: Diagnostic Toy Probe (7 checks) ---")
# ================================================================

dp = result.diagnostic_probe
check("Diagnostic probe exists", dp is not None)
close("B value = 0.1", dp.B_value, DIAGNOSTIC_B_COEFF)

# Component A coefficient: (A^2/(2*tau^2)) * M^2
expected_A = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * M_EXT ** 2
rel_close("Component A coefficient", dp.component_A_coeff, expected_A)

# Component B coefficient: (A^2/(2*tau^2)) * B^2
expected_B = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * DIAGNOSTIC_B_COEFF ** 2
rel_close("Component B coefficient from probe", dp.component_B_coeff, expected_B)

# Cross-term coefficient: (A^2/(2*tau^2)) * 2*M*B
expected_cross = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * 2.0 * M_EXT * DIAGNOSTIC_B_COEFF
rel_close("Cross-term coefficient", dp.cross_term_coeff, expected_cross)

check("Inner exponent closer to -4 than -2",
      abs(dp.fitted_exponent_inner - (-4.0)) < abs(dp.fitted_exponent_inner - (-2.0)))
check("Probe confirms mechanism", dp.probe_confirms_mechanism)

# ================================================================
print("\n--- Section 4: Family 1 — Local Algebraic (6 checks) ---")
# ================================================================

f1 = result.taxonomy.shape_results[0]
check("Family 1 is local_algebraic", f1.family_name == "local_algebraic")

# p=1 should give exponent -4.0
sub = f1.sub_exponents
close("p=1.0 epsilon exponent = -4.0", sub["p=1.00_epsilon"], -4.0, tol=0.01)

# p=0.5 should give exponent -2.0 (target)
close("p=0.50 epsilon exponent = -2.0", sub["p=0.50_epsilon"], -2.0, tol=0.01)

# p=0.75 should give exponent -3.0
close("p=0.75 epsilon exponent = -3.0", sub["p=0.75_epsilon"], -3.0, tol=0.01)

# p=0.25 should give exponent -1.0
close("p=0.25 epsilon exponent = -1.0", sub["p=0.25_epsilon"], -1.0, tol=0.01)

# Best power should be p=0.5
check("Best algebraic power = 0.5", f1.algebraic_power_used == 0.5)

# ================================================================
print("\n--- Section 5: Family 2 — Gradient/Derivative (5 checks) ---")
# ================================================================

f2 = result.taxonomy.shape_results[1]
check("Family 2 is gradient_derivative", f2.family_name == "gradient_derivative")
check("Family 2 cannot produce 1/r", not f2.can_produce_1_over_r)

# Derivative exponents
sub2 = f2.sub_exponents
close("d/dr exponent = -3.0", sub2["d/dr_exponent"], -3.0, tol=0.01)
close("d^2/dr^2 exponent = -4.0", sub2["d2/dr2_exponent"], -4.0, tol=0.01)

# Epsilon exponent should be steeper than -2.0
check("Family 2 epsilon steeper than -2.0", f2.epsilon_exponent < -2.0)

# ================================================================
print("\n--- Section 6: Family 3 — Cumulative/Integral (6 checks) ---")
# ================================================================

f3 = result.taxonomy.shape_results[2]
check("Family 3 is cumulative_integral", f3.family_name == "cumulative_integral")
check("Family 3 cannot produce pure 1/r", not f3.can_produce_1_over_r)

# Integral contains 1/r contribution
sub3 = f3.sub_exponents
check("1/r coefficient > 0", sub3["one_over_r_coeff"] > 0)
check("Constant offset > 0", sub3["constant_offset"] > 0)

# Constant offset should dominate at large r => exponent shallower than -2
check("Epsilon exponent shallower than -2 (contaminated)",
      f3.epsilon_exponent > -2.0)

# The constant offset is lambda * M / r_min
params = result.params
expected_const = params.integral_lambda * params.M / params.integral_r_min
rel_close("Constant offset value", sub3["constant_offset"], expected_const)

# ================================================================
print("\n--- Section 7: Family 4 — Defect/Topological (6 checks) ---")
# ================================================================

f4 = result.taxonomy.shape_results[3]
check("Family 4 is defect_topological", f4.family_name == "defect_topological")
check("Family 4 CAN produce 1/r", f4.can_produce_1_over_r)

# Pure Q/r epsilon exponent should be -2.0
sub4 = f4.sub_exponents
close("Pure Q/r epsilon exponent = -2.0",
      sub4["Q_only_epsilon_exponent"], -2.0, tol=0.01)

# Component B coefficient from Q
Q = params.defect_Q
prefactor = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2)
expected_comp_B_Q = prefactor * Q ** 2
rel_close("Component B coeff from Q",
          sub4["comp_B_from_Q"], expected_comp_B_Q)

# Full profile is mixed (not pure 1/r^2)
check("Full epsilon exponent between -4 and -2",
      -4.0 < f4.epsilon_exponent < -2.0)

# Full source exponent between -2 and -1
check("Full source exponent between -2 and -1",
      -2.0 < f4.source_exponent < -1.0)

# ================================================================
print("\n--- Section 8: Family 5 — Processing-Invariant (5 checks) ---")
# ================================================================

f5 = result.taxonomy.shape_results[4]
check("Family 5 is processing_lag_invariant",
      f5.family_name == "processing_lag_invariant")
check("Family 5 cannot produce 1/r", not f5.can_produce_1_over_r)

# At equilibrium, collapses to Family 1 with p=1
close("Family 5 source exponent = -2.0 (standard)",
      f5.source_exponent, -2.0, tol=0.01)
close("Family 5 epsilon exponent = -4.0 (standard)",
      f5.epsilon_exponent, -4.0, tol=0.01)
close("Family 5 deviation = 2.0",
      f5.deviation_from_target, 2.0, tol=0.01)

# ================================================================
print("\n--- Section 9: Candidate Ranking & GRUT-Nativeness (6 checks) ---")
# ================================================================

rk = result.ranking
check("Ranking exists", rk is not None)
check("Top candidate is local_algebraic",
      rk.top_candidate_name == "local_algebraic")
check("No GRUT-native viable", not rk.any_grut_native_viable)

nat = result.nativeness
check("Nativeness exists", nat is not None)
check("0 GRUT-native viable", nat.n_grut_native_viable == 0)
check("n_non_native_viable = 2 (algebraic + defect)",
      nat.n_non_native_viable == 2)

# ================================================================
print("\n--- Section 10: Final Classification & Nonclaims (6 checks) ---")
# ================================================================

cl = result.classification
check("Classification exists", cl is not None)
check("Loophole 5 status = partially_viable",
      cl.loophole_5_status == "partially_viable")
check("Classification string correct",
      cl.classification ==
      "source_law_loophole_5_partially_viable__no_grut_native_mechanism")
check("2 viable families", cl.n_viable_families == 2)

# Nonclaims and assumptions
check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = source_law_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)

# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Loophole 5 status: {cl.loophole_5_status}")
print(f"Viable families: {cl.viable_family_names}")
print(f"GRUT-native viable: {cl.n_grut_native}")
print(f"Top candidate: {rk.top_candidate_name}")
print(f"Diagnostic probe confirms mechanism: {dp.probe_confirms_mechanism}")
print(f"Family 1 (p=0.5) epsilon exponent: {sub['p=0.50_epsilon']:.4f}")
print(f"Family 4 (Q/r only) epsilon exponent: {sub4['Q_only_epsilon_exponent']:.4f}")
print(f"Family 2 (gradient): CLOSED (all derivatives steepen profile)")
print(f"Family 3 (integral): contaminated by constant offset")
print(f"Family 5 (processing): collapses to Family 1 at equilibrium")

if _failed > 0:
    sys.exit(1)
