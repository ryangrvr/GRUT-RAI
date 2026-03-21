#!/usr/bin/env python3
"""Benchmark — Phase D7: Cross-Coupling Dynamics and Back-Reaction Test.

60 checks across 11 sections.
"""

import math
import sys
import json

from grut.cross_coupling_dynamics import (
    # Constants
    ALPHA_BR_SCAN, BETA_XR_SCAN, LAMBDA_SCAN_VALUES,
    N_INTERACTION_CHANNELS, UNIT_BENCHMARK,
    MASS_COEFF, RHO_EQ_COEFF, R_EQ, R_EXT, M_EXT, ETA_SQUARED,
    # Assumptions / nonclaims
    CROSS_COUPLING_ASSUMPTIONS, CROSS_COUPLING_NONCLAIMS,
    # Dataclasses
    CrossCouplingParams,
    # Functions
    define_coupled_model,
    compute_coupled_sectors,
    assess_back_reaction,
    inject_coupled_metric,
    scan_coupling_strength,
    scan_lambda_coupled,
    classify_cross_coupling,
    compute_cross_coupling,
    cross_coupling_result_to_dict,
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
print("Benchmark — Phase D7: Cross-Coupling Dynamics")
print("=" * 60)

result = compute_cross_coupling()

# ================================================================
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
# ================================================================

check("N_INTERACTION_CHANNELS = 2", N_INTERACTION_CHANNELS == 2)
check("ALPHA_BR_SCAN has 5 values", len(ALPHA_BR_SCAN) == 5)
check("BETA_XR_SCAN has 5 values", len(BETA_XR_SCAN) == 5)
check("UNIT_BENCHMARK = (1,1)", UNIT_BENCHMARK == (1.0, 1.0))
check("MASS_COEFF matches pi/3",
      abs(MASS_COEFF - math.pi / 3.0) < 1e-10)


# ================================================================
print("\n--- Section 2: Model Definition (5 checks) ---")
# ================================================================

md = result.model_definition
check("Model definition exists", md is not None)
check("Two channels", md.n_channels == 2)
check("D6 recovery condition mentions alpha=0",
      "0" in md.d6_recovery_condition)
check("Unit benchmark = (1,1)", md.unit_benchmark == (1.0, 1.0))
check("Channel names correct",
      md.channels[0].name == "gravitational_back_reaction" and
      md.channels[1].name == "source_amplification")


# ================================================================
print("\n--- Section 3: Coupled Sectors (7 checks) ---")
# ================================================================

cs = result.coupled_sectors
check("Coupled sectors exist", cs is not None)
check("Sigma_defect > 0", cs.sigma_defect_at_Req > 0)
check("A_eff > A_0 at unit benchmark",
      cs.A_eff_at_Req > result.params.scalar_A)
check("Sigma_macro_coupled > D6 at unit benchmark",
      cs.sigma_macro_coupled_at_Req > cs.sigma_macro_d6_at_Req)
check("Sigma total positive", float(cs.sigma_total[0]) > 0)
check("BVP converged", cs.bvp_converged)
check("Grid has 400 points", len(cs.r_grid) == 400)


# ================================================================
print("\n--- Section 4: Back-Reaction Assessment (6 checks) ---")
# ================================================================

br = result.back_reaction
check("Back-reaction exists", br is not None)
check("Delta increase > 0 at alpha=1", br.delta_increase_at_Req > 0)
check("Amplification factor > 1 at beta=1", br.amplification_factor > 1.0)
check("Net classification is valid string",
      br.net_classification in ["constructive", "destructive", "neutral"])
check("Sigma_macro increase > 0 at beta=1",
      br.sigma_macro_increase_at_Req > 0)
check("Net metric shift finite", math.isfinite(br.net_metric_shift_at_Req))


# ================================================================
print("\n--- Section 5: Metric Injection (6 checks) ---")
# ================================================================

mi = result.metric_injection
check("Metric injection exists", mi is not None)
check("f_min finite", math.isfinite(mi.f_min))
check("f(R_eq) finite", math.isfinite(mi.f_at_Req))
check("Budget at R_eq exists", f"r={R_EQ:.4f}" in mi.budget)
check("Metric shift reported", math.isfinite(mi.metric_shift))
check("D6 reference positive", mi.f_d6_at_Req > 0)


# ================================================================
print("\n--- Section 6: Coupling Strength Scan (7 checks) ---")
# ================================================================

sc = result.coupling_scan
check("Coupling scan exists", sc is not None)
check("25 entries (5x5)", sc.n_scanned == 25)
check("D6 limit (0,0) exists", any(
    abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10
    for e in sc.entries))
check("Unit benchmark reported", sc.unit_benchmark_entry is not None)
check("Unit benchmark f_min finite",
      math.isfinite(sc.unit_benchmark_f_min))
check("At least one positive config", sc.n_positive >= 1)
check("Pure amplification (0,1) exists", sc.pure_amplification is not None)


# ================================================================
print("\n--- Section 7: Lambda Scan (6 checks) ---")
# ================================================================

ls = result.lambda_scan
check("Lambda scan exists", ls is not None)
check("6 scanned", ls.n_scanned == 6)
check("All converged", ls.n_converged == 6)
check("D6 positive >= 4 (matching D6)", ls.n_positive_d6 >= 4)
check("Coupled positive > 0", ls.n_positive_coupled > 0)
check("Best lambda in scan values",
      ls.best_lambda_coupled in LAMBDA_SCAN_VALUES)


# ================================================================
print("\n--- Section 8: Classification (6 checks) ---")
# ================================================================

cl = result.classification
check("Classification exists", cl is not None)
check("Classification is valid string",
      cl.classification in [
          "fully_coupled_viable",
          "viability_window_shifted_but_survives",
          "partially_viable_under_coupling",
          "destroyed_by_back_reaction",
          "unresolved_coupled_artifacts",
      ])
check("Phase lock has D7", "cross_coupling_D7" in cl.phase_lock_update)
check("D6 pessimistic is bool", isinstance(cl.d6_additive_pessimistic, bool))
check("Viable windows are lists",
      isinstance(cl.viable_lambda_window_coupled, list))
check("Threshold shift valid",
      cl.threshold_shift in ["unchanged", "lower", "higher", "shifted", "destroyed"])


# ================================================================
print("\n--- Section 9: D6 Recovery (4 checks) ---")
# ================================================================

# Find (0,0) entry
d6_entry = None
for e in sc.entries:
    if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
        d6_entry = e
        break
check("D6 (0,0) entry found", d6_entry is not None)
if d6_entry:
    check("D6 (0,0) metric positive", d6_entry.metric_positive)
    check("Pure BR (1,0) f_min <= D6",
          sc.pure_backreaction.f_min <= d6_entry.f_min + 0.01
          if sc.pure_backreaction else False)
    check("Pure amp (0,1) f_min >= D6",
          sc.pure_amplification.f_min >= d6_entry.f_min - 0.01
          if sc.pure_amplification else False)
else:
    check("D6 (0,0) metric positive", False)
    check("Pure BR (1,0) <= D6", False)
    check("Pure amp (0,1) >= D6", False)


# ================================================================
print("\n--- Section 10: Nonclaims & Serialization (3 checks) ---")
# ================================================================

check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)

d = cross_coupling_result_to_dict(result)
json_str = json.dumps(d, indent=2, default=str)
check("Serialization valid JSON", len(json_str) > 100)


# ================================================================
print("\n--- Section 11: Physics Consistency (5 checks) ---")
# ================================================================

# Pure BR (1,0) should eliminate defect benefit → essentially macro only
if sc.pure_backreaction:
    check("Pure BR (1,0) f_min negative (defect cancelled)",
          sc.pure_backreaction.f_min < 0)
else:
    check("Pure BR (1,0) f_min negative", False)

# A_eff at R_ext should approach A_0 (sigma_defect -> 0)
A_eff_end = float(cs.A_eff[-1])
check("A_eff approaches A_0 at R_ext",
      abs(A_eff_end - result.params.scalar_A) < 0.1)

# At beta=0 sigma_macro should match analytic D6
d6_zero = None
for e in sc.entries:
    if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
        d6_zero = e
        break
check("D6 (0,0) f_min close to D6 benchmark",
      d6_zero is not None and abs(d6_zero.f_min - 0.498) < 0.05)

# No NaN in profiles
check("No NaN in f_coupled",
      all(math.isfinite(float(x)) for x in mi.f_coupled))

# Combined formula reduces correctly at (0,0)
check("D6 entry classification is neutral (no shift at zero coupling)",
      d6_zero.net_classification == "neutral" if d6_zero else False)


# ================================================================
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"D6 additive was pessimistic: {cl.d6_additive_pessimistic}")
print(f"Threshold shift: {cl.threshold_shift}")

print(f"\nBack-reaction at unit benchmark (1,1):")
print(f"  A_eff(R_eq) = {br.A_eff_at_Req:.4f}")
print(f"  Amplification factor = {br.amplification_factor:.4f}")
print(f"  Delta increase = {br.delta_increase_at_Req:.6f}")
print(f"  Sigma macro increase = {br.sigma_macro_increase_at_Req:.6f}")
print(f"  Net shift = {br.net_metric_shift_at_Req:.6f}")
print(f"  Classification: {br.net_classification}")

print(f"\nThree named slices:")
if sc.pure_backreaction:
    print(f"  (1,0) pure BR: f_min={sc.pure_backreaction.f_min:.6f}")
if sc.pure_amplification:
    print(f"  (0,1) pure amp: f_min={sc.pure_amplification.f_min:.6f}")
print(f"  (1,1) unit benchmark: f_min={sc.unit_benchmark_f_min:.6f}")

print(f"\nLambda scan:")
print(f"  Viable D6: {ls.viable_lambda_d6}")
print(f"  Viable coupled: {ls.viable_lambda_coupled}")
for e in ls.entries:
    print(f"    lam={e.lam:6.1f}  D6={e.f_min_d6:+.6f}  coupled={e.f_min_coupled:+.6f}  "
          f"shift={e.f_shift:+.6f}  {e.net_classification}")

print(f"\nSummary: {cl.summary}")

if _failed > 0:
    sys.exit(1)
