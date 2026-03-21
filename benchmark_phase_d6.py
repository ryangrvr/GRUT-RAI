#!/usr/bin/env python3
"""Benchmark — Phase D6: Companion Architecture and Dual-Sector Metric Integration.

60 checks across 11 sections.
"""

import math
import sys
import json

from grut.companion_architecture import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    MASS_COEFF, RHO_EQ_COEFF, R_EXT, KRETSCHNER_COEFF,
    XI_DEFAULT, N_SECTORS, N_CROSS_TERMS,
    LAMBDA_SCAN_VALUES,
    # Assumptions / nonclaims
    COMPANION_ASSUMPTIONS, COMPANION_NONCLAIMS,
    # Dataclasses
    CompanionParams,
    # Functions
    define_architecture,
    verify_trigger_regime,
    construct_macro_sector,
    construct_defect_sector,
    decompose_dual_sector,
    analyze_sector_dominance,
    inject_companion_metric,
    scan_lambda_companion,
    inventory_cross_terms,
    classify_companion,
    compute_companion_architecture,
    companion_architecture_result_to_dict,
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
print("Benchmark — Phase D6: Companion Architecture")
print("=" * 60)

result = compute_companion_architecture()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

check("N_SECTORS = 2", N_SECTORS == 2)
check("N_CROSS_TERMS = 4", N_CROSS_TERMS == 4)
check("A_CRIT = 1.062", A_CRIT == 1.062)
check("XI_DEFAULT = 1.0", XI_DEFAULT == 1.0)
check("ETA_SQUARED = 1/(8*pi)",
      abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10)


# ================================================================
print("\n--- Section 2: Architecture Definition (5 checks) ---")
# ================================================================

arch = result.architecture
check("Architecture exists", arch is not None)
check("Two sectors", arch.n_sectors == 2)
check("Additive combination rule", "additive" in arch.combination_rule.lower())
check("Cross-terms inventoried", "inventoried" in arch.cross_term_treatment)
check("Macro sector described", len(arch.macro_description) > 20)


# ================================================================
print("\n--- Section 3: Trigger Regime (7 checks) ---")
# ================================================================

tr = result.trigger_regime
check("Trigger regime exists", tr is not None)
check("sqrt(K) at R_eq > 0", tr.sqrt_K_at_Req > 0)
check("sqrt(K) at R_ext > 0", tr.sqrt_K_at_Rext > 0)
check("Core >> exterior (ratio > 10)",
      tr.core_to_exterior_ratio > 10)
check("K_crit positive", tr.K_crit > 0)
check("Activation radius positive", tr.activation_radius > 0)
check("Active at R_eq", tr.active_at_Req)


# ================================================================
print("\n--- Section 4: Macro Sector (6 checks) ---")
# ================================================================

mb = result.macro_baseline
mc = result.macro_critical
check("Macro baseline exists", mb is not None)
check("Macro critical exists", mc is not None)
check("Baseline label is A1", mb.label == "baseline_A1")
check("Critical label is Acrit", mc.label == "critical_Acrit")
check("Sigma_macro(R_eq) baseline > 0", mb.sigma_at_Req > 0)
check("Sigma_macro(R_eq) critical > baseline",
      mc.sigma_at_Req > mb.sigma_at_Req)


# ================================================================
print("\n--- Section 5: Defect Sector (6 checks) ---")
# ================================================================

ds = result.defect_sector
check("Defect sector exists", ds is not None)
check("BVP converged", ds.bvp_converged)
check("Sigma_defect(R_eq) > 0", ds.sigma_at_Req > 0)
check("Tail exponent negative", ds.tail_exponent < 0)
check("Tail coefficient positive", ds.tail_coefficient > 0)
check("Interior grid length = 400", len(ds.r_interior) == 400)


# ================================================================
print("\n--- Section 6: Dual-Sector Decomposition (6 checks) ---")
# ================================================================

d_a1 = result.decomposition_A1
d_ac = result.decomposition_Acrit
check("Decomposition A=1 exists", d_a1 is not None)
check("Decomposition A_crit exists", d_ac is not None)
check("A=1 epsilon ratio mean > 0", d_a1.epsilon_ratio_mean > 0)
check("A_crit epsilon ratio > A=1 ratio",
      d_ac.epsilon_ratio_mean >= d_a1.epsilon_ratio_mean)
check("Sigma_total(R_eq) A=1 > 0",
      float(d_a1.sigma_total[0]) > 0)
check("Sigma_total(R_eq) A_crit > A=1",
      float(d_ac.sigma_total[0]) >= float(d_a1.sigma_total[0]))


# ================================================================
print("\n--- Section 7: Sector Dominance (5 checks) ---")
# ================================================================

dom = result.dominance
check("Dominance result exists", dom is not None)
check("Crossover radius > R_eq", dom.crossover_radius > R_EQ)
check("Crossover radius < R_ext + epsilon",
      dom.crossover_radius < R_EXT + 1.0)
check("Macro dominates at R_eq", dom.macro_dominates_inner)
check("Ratio at R_eq > 1 (macro dominant)", dom.ratio_at_Req > 1.0)


# ================================================================
print("\n--- Section 8: Metric Injection (6 checks) ---")
# ================================================================

m_a1 = result.metric_A1
m_ac = result.metric_Acrit
check("Metric A=1 exists", m_a1 is not None)
check("Metric A_crit exists", m_ac is not None)
check("f_min A=1 is finite", math.isfinite(m_a1.f_min))
check("f_min A_crit >= f_min A=1",
      m_ac.f_min >= m_a1.f_min - 1e-10)
check("Budget at R_eq exists", f"r={R_EQ:.4f}" in m_a1.budget)
check("Budget has delta field",
      "delta" in m_a1.budget.get(f"r={R_EQ:.4f}", {}))


# ================================================================
print("\n--- Section 9: Lambda Scan (6 checks) ---")
# ================================================================

ls = result.lambda_scan
check("Lambda scan exists", ls is not None)
check("6 values scanned", ls.n_scanned == 6)
check("All converged", ls.n_converged == 6)
check("A_crit positive count >= A=1 positive count",
      ls.n_positive_Acrit >= ls.n_positive_A1)
check("Best lambda A=1 in scan values",
      ls.best_lambda_A1 in LAMBDA_SCAN_VALUES)
check("Best lambda A_crit in scan values",
      ls.best_lambda_Acrit in LAMBDA_SCAN_VALUES)


# ================================================================
print("\n--- Section 10: Cross-Terms & Classification (5 checks) ---")
# ================================================================

ct = result.cross_terms
check("Cross-term inventory exists", ct is not None)
check("4 cross-terms documented", ct.n_cross_terms == 4)
check("Additive approx not fully justified",
      not ct.additive_approximation_justified)

cl = result.classification
check("Classification exists", cl is not None)
check("Phase lock has D6",
      "companion_D6" in cl.phase_lock_update)


# ================================================================
print("\n--- Section 11: Nonclaims & Serialization (3 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

# Serialization
d = companion_architecture_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization produces valid JSON", len(json_str) > 100)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")

print(f"\nTrigger regime:")
print(f"  sqrt(K) at R_eq: {tr.sqrt_K_at_Req:.4f}")
print(f"  sqrt(K) at R_ext: {tr.sqrt_K_at_Rext:.4f}")
print(f"  Core/exterior ratio: {tr.core_to_exterior_ratio:.1f}x")
print(f"  K_crit: {tr.K_crit:.4f}")
print(f"  Activation radius: {tr.activation_radius:.4f}")
print(f"  Active at R_eq: {tr.active_at_Req}")

print(f"\nMacro baseline (A=1):")
print(f"  Sigma_macro(R_eq) = {mb.sigma_at_Req:.6f}")
print(f"Macro critical (A=A_crit):")
print(f"  Sigma_macro(R_eq) = {mc.sigma_at_Req:.6f}")
print(f"Defect:")
print(f"  Sigma_defect(R_eq) = {ds.sigma_at_Req:.6f}")

print(f"\nMetric (default lambda):")
print(f"  A=1:     f_min = {m_a1.f_min:.6f}, positive = {m_a1.metric_positive}")
print(f"  A=A_crit: f_min = {m_ac.f_min:.6f}, positive = {m_ac.metric_positive}")

print(f"\nDominance:")
print(f"  Crossover radius: {dom.crossover_radius:.4f}")
print(f"  Macro/defect at R_eq: {dom.ratio_at_Req:.4f}")

print(f"\nLambda scan:")
print(f"  A=1: {ls.n_positive_A1} positive, best fmin = {ls.best_fmin_A1:.6f} at lam = {ls.best_lambda_A1}")
print(f"  A_crit: {ls.n_positive_Acrit} positive, best fmin = {ls.best_fmin_Acrit:.6f} at lam = {ls.best_lambda_Acrit}")
for e in ls.entries:
    print(f"    lam={e.lam:6.1f}  fmin_A1={e.f_min_A1:+.6f}  pos_A1={e.metric_positive_A1}  "
          f"fmin_Ac={e.f_min_Acrit:+.6f}  pos_Ac={e.metric_positive_Acrit}  "
          f"defect_frac_A1={e.sigma_defect_fraction_A1:.4f}")

print(f"\nCross-terms: {ct.n_cross_terms} documented")
print(f"  Main: {ct.main_approximation[:80]}...")
print(f"\nViable lambda window A=1: {cl.viable_lambda_window_A1}")
print(f"Viable lambda window A_crit: {cl.viable_lambda_window_Acrit}")
print(f"\nSummary: {cl.summary}")

if _failed > 0:
    sys.exit(1)
