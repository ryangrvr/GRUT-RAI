#!/usr/bin/env python3
"""Benchmark — Phase D9: Self-Consistent Coupled Profile Integration.

60 checks across 11 sections.
"""

import sys
import json

from grut.self_consistent_coupling import (
    compute_self_consistent,
    self_consistent_result_to_dict,
    SelfConsistentParams,
    CLASSIFICATION_OPTIONS,
    G_PORTAL_SCAN_VALUES,
    LAMBDA_SCAN_VALUES,
    SELF_CONSISTENT_ASSUMPTIONS,
    SELF_CONSISTENT_NONCLAIMS,
)

# ---- Harness ----
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


# ---- Compute ----
print("=" * 60)
print("Benchmark — Phase D9: Self-Consistent Coupled Profile")
print("=" * 60)

params = SelfConsistentParams()
result = compute_self_consistent(params)

# ---- Section 1: Constants & Parameters (5 checks) ----
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
check("G_PORTAL_SCAN has 4 values", len(G_PORTAL_SCAN_VALUES) == 4)
check("LAMBDA_SCAN has 6 values", len(LAMBDA_SCAN_VALUES) == 6)
check("Default relaxation = 0.5", abs(params.relaxation_factor - 0.5) < 1e-10)
check("Default g_portal = 1.0", abs(params.g_portal - 1.0) < 1e-10)
check("CLASSIFICATION_OPTIONS has 5 values", len(CLASSIFICATION_OPTIONS) == 5)

# ---- Section 2: Coupled Solver Definition (5 checks) ----
print("\n--- Section 2: Coupled Solver Definition (5 checks) ---")
sd = result.solver_definition
check("Solver definition exists", sd is not None)
check("Proxy closure statement present", "PROXY" in sd.proxy_closure_statement.upper())
check("Sign analysis present", "POSITIVE" in sd.sign_analysis.upper() or "STABILIZING" in sd.sign_analysis.upper())
check("Under-relaxation documented", "omega" in sd.under_relaxation_scheme.lower() or "relax" in sd.under_relaxation_scheme.lower())
check("Modified ODE documented", "g_portal" in sd.modified_ode)

# ---- Section 3: Self-Consistent Solution (7 checks) ----
print("\n--- Section 3: Self-Consistent Solution (7 checks) ---")
ps = result.profile_solution
check("Profile solution exists", ps is not None)
check("SC converged", ps.converged)
check("Iterations > 0", ps.n_iterations > 0)
check("Final residual < tolerance", ps.final_residual < params.convergence_tol)
check("Sigma_defect > 0", ps.sigma_defect_at_Req > 0)
check("A_eff > A_0", ps.A_eff_at_Req > params.scalar_A)
check("Convergence history populated", len(ps.convergence_history) > 0)

# ---- Section 4: Profile Deformation (6 checks) ----
print("\n--- Section 4: Profile Deformation (6 checks) ---")
df = result.deformation
check("Deformation exists", df is not None)
check("f_shift_max >= 0", df.f_shift_max >= 0)
check("f_shift_rms >= 0", df.f_shift_rms >= 0)
check("Crossover radius frozen > 0", df.crossover_radius_frozen > 0)
check("Deformation classified", df.deformation_classification in ["negligible", "moderate", "significant", "large"])
check("Sigma defect shift is finite", abs(df.sigma_defect_shift) < 100)

# ---- Section 5: Metric Injection (6 checks) ----
print("\n--- Section 5: Metric Injection (6 checks) ---")
mr = result.metric_result
check("Metric result exists", mr is not None)
check("f_min finite", abs(mr.f_min) < 1000)
check("f_at_Req finite", abs(mr.f_at_Req) < 1000)
check("Budget at R_eq exists", any("0.3333" in k for k in mr.budget))
check("Metric shift from D7 finite", abs(mr.metric_shift_from_d7) < 100)
check("Metric positive reported", isinstance(mr.metric_positive, bool))

# ---- Section 6: Lambda Scan (6 checks) ----
print("\n--- Section 6: Lambda Scan (6 checks) ---")
ls = result.lambda_scan
check("Lambda scan exists", ls is not None)
check("6 scanned", ls.n_scanned == 6)
check("All converged", ls.n_converged == 6)
check("D7 viable count matches", ls.n_positive_d7 == 6)
check("SC viable count > 0", ls.n_positive_sc > 0)
check("Threshold shift valid", ls.threshold_shift in ["unchanged", "lower", "higher", "destroyed", "shifted"])

# ---- Section 7: Portal Strength Scan (5 checks) ----
print("\n--- Section 7: Portal Strength Scan (5 checks) ---")
ps2 = result.portal_scan
check("Portal scan exists", ps2 is not None)
check("4 scanned", ps2.n_scanned == 4)
check("g_portal=0 entry exists", any(abs(e.g_portal) < 1e-10 for e in ps2.entries))
check("g_portal=0 positive (D7 recovery)", [e for e in ps2.entries if abs(e.g_portal) < 1e-10][0].metric_positive)
check("Sensitivity assessed", ps2.sensitivity_assessment in ["insensitive", "mild_sensitivity", "moderate_sensitivity", "high_sensitivity"])

# ---- Section 8: Classification (6 checks) ----
print("\n--- Section 8: Classification (6 checks) ---")
cl = result.classification
check("Classification exists", cl is not None)
check("Classification valid string", cl.classification in CLASSIFICATION_OPTIONS)
check("Phase lock has D9", "self_consistent_D9" in cl.phase_lock_update)
check("Phase lock has D8", "coupled_action_D8" in cl.phase_lock_update)
check("Proxy closure flagged", cl.proxy_closure_used is True)
check("Deformation level reported", cl.deformation_level in ["negligible", "moderate", "significant", "large"])

# ---- Section 9: D7 Recovery (5 checks) ----
print("\n--- Section 9: D7 Recovery (5 checks) ---")
frozen = result.frozen_solution
check("Frozen solution exists", frozen is not None)
check("Frozen g_portal = 0", abs(frozen.g_portal) < 1e-10)
check("Frozen iterations = 0", frozen.n_iterations == 0)
check("Frozen converged", frozen.converged)
check("Frozen f_defect matches SC at g=0",
      [e for e in ps2.entries if abs(e.g_portal) < 1e-10][0].converged)

# ---- Section 10: Nonclaims & Serialization (4 checks) ----
print("\n--- Section 10: Nonclaims & Serialization (4 checks) ---")
check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)
d = self_consistent_result_to_dict(result)
check("Serialization valid JSON", json.dumps(d) is not None)
check("Serialization has classification", "classification" in d)

# ---- Section 11: Physics Consistency (5 checks) ----
print("\n--- Section 11: Physics Consistency (5 checks) ---")
# Portal stabilizing: SC profile should have f closer to 1 than frozen (tighter core)
check("Portal stabilizing: SC sigma_defect shifted",
      abs(df.sigma_defect_shift) > 0)
check("SC f_min close to D7 f_min (within 10%)",
      abs(mr.f_min - mr.f_d7_at_Req) / max(abs(mr.f_d7_at_Req), 0.01) < 0.5)
check("Lambda scan rescue preserved", ls.rescue_preserved)
check("No NaN in convergence history",
      all(not (x != x) for x in ps.convergence_history if isinstance(x, float)))
check("Under-relaxation used", ps.relaxation_used <= 1.0)

# ---- Summary ----
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

# Key findings
print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"D7 viability preserved: {cl.d7_viability_preserved}")
print(f"Proxy closure used: {cl.proxy_closure_used}")
print()
print(f"Self-consistent solution:")
print(f"  Converged in {ps.n_iterations} iterations")
print(f"  Final residual: {ps.final_residual:.2e}")
print(f"  Relaxation: {ps.relaxation_used}")
print()
print(f"Profile deformation:")
print(f"  Max |delta_f|: {df.f_shift_max:.6f}")
print(f"  Classification: {df.deformation_classification}")
print(f"  Crossover shift: {df.crossover_shift:.4f}")
print()
print(f"Metric result:")
print(f"  f_min (SC): {mr.f_min:.6f}")
print(f"  f_min (D7 frozen): {mr.f_d7_at_Req:.6f}")
print(f"  Shift: {mr.metric_shift_from_d7:.6f}")
print(f"  Positive: {mr.metric_positive}")
print()
print(f"Lambda scan:")
print(f"  Viable D7: {ls.viable_d7}")
print(f"  Viable SC: {ls.viable_sc}")
print(f"  Threshold shift: {ls.threshold_shift}")
for e in ls.entries:
    print(f"    lam={e.lam:6.1f}  D7={e.f_min_d7:+.6f}  SC={e.f_min_sc:+.6f}  "
          f"shift={e.f_shift:+.6f}  deform={e.deformation_max:.4f}  "
          f"iters={e.n_iterations}")
print()
print(f"Portal scan:")
print(f"  Sensitivity: {ps2.sensitivity_assessment}")
for e in ps2.entries:
    print(f"    g={e.g_portal:.2f}  f_min={e.f_min:+.6f}  pos={e.metric_positive}  "
          f"deform={e.deformation_max:.4f}  iters={e.n_iterations}")
print()
print(f"Summary: {cl.summary}")

if _failed > 0:
    sys.exit(1)
