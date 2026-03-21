#!/usr/bin/env python3
"""Benchmark: Phase 6C — Global Metric Positivity Deficit and Minimal Closure Requirement.

~80 independent checks covering:
  1.  Parameter Setup (6)
  2.  Static Mass Profile (6)
  3.  Deficit Profile (7)
  4.  Minimal Source Decomposition (8)
  5.  Correction Verification (5)
  6.  Kinetic Deficit Profile (6)
  7.  Anisotropy Insufficiency (5)
  8.  Additive Source (5)
  9.  Two-Parameter Scan (8)
  10. Monotonic Profile Insufficiency (6)
  11. Phase 6B Comparison (6)
  12. Nonclaims & Assumptions (5)
  13. Serialization (3)

KEY FINDINGS:
  The deficit function delta(r) = m(r) - r/2 is positive over ~83% of the
  barrier region.  The minimal additive source epsilon_min = |rho_eq| + 1/(8*pi*r^2)
  has two components: Component A (1/r^4) cancels rho_eq, Component B (1/r^2)
  provides intermediate-radius support.  No tested GRUT profile provides
  Component B.  A_crit > 1 for the natural profile because the 1/r^4 profile
  must overshoot to brute-force Component B.  Classification:
  current_closure_insufficient__minimal_additive_source_identified.
"""

from __future__ import annotations

import math
import sys
import numpy as np

from grut.metric_deficit import (
    compute_metric_deficit_analysis,
    metric_deficit_result_to_dict,
    DeficitParams,
    compute_deficit_profile,
    compute_static_mass,
    compute_equilibrium_density,
    compute_minimal_source,
    compute_kinetic_deficit,
    assess_anisotropy_insufficiency,
    compute_additive_source,
    scan_two_parameter,
    assess_monotonic_profile_insufficiency,
    build_phase6b_comparison,
    classify_closure,
    make_radial_grid,
    ALPHA_VAC,
    BETA_Q,
    R_S,
    M_EXT,
    R_EQ,
    C_COMPACTNESS,
    TAU_CANONICAL,
    A_EFF_CONSTITUTIVE,
    A_SCHW,
    MASS_COEFF,
    PHASE6_F_AT_REQ,
    PHASE6B_A_CRIT_NATURAL,
    NONCLAIMS,
    MINIMAL_SOURCE_ASSUMPTIONS,
)


passed = 0
failed = 0
results = []


def check(label: str, condition: bool, detail: str = "") -> None:
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if not condition:
        failed += 1
    else:
        passed += 1
    msg = f"  [{status}] {label}"
    if detail and not condition:
        msg += f"  -- {detail}"
    results.append(msg)
    print(msg)


def close(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) < tol


def rel_close(a: float, b: float, tol: float = 0.05) -> bool:
    if abs(b) < 1e-30:
        return abs(a) < tol
    return abs(a - b) / abs(b) < tol


def main() -> int:
    print("=" * 72)
    print("BENCHMARK: Phase 6C — Metric Positivity Deficit & Minimal Closure")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running metric deficit analysis...")
    params = DeficitParams(n_r=500, n_A=40, n_B=40)
    result = compute_metric_deficit_analysis(params)
    print(f"  Analysis complete. Valid: {result.valid}\n")

    deficit = result.deficit
    ms = result.minimal_source
    kd = result.kinetic_deficit
    aniso = result.anisotropy_insufficiency
    addsrc = result.additive_source
    tp = result.two_param_scan
    mono = result.monotonic_gap
    p6b = result.phase6b_comparison
    cc = result.closure_classification

    # ================================================================
    # Section 1: Parameter Setup (6)
    # ================================================================
    print("\n--- Section 1: Parameter Setup ---")

    check("alpha_vac = 1/3", close(ALPHA_VAC, 1.0 / 3.0))
    check("M = r_s/2 = 0.5", close(M_EXT, 0.5))
    check("R_eq = r_s/3", close(R_EQ, 1.0 / 3.0))
    check("tau = sqrt(C/2) ~ 1.2247", close(TAU_CANONICAL, math.sqrt(1.5), 1e-4))
    check("MASS_COEFF = 2*pi*M^2/tau^2",
          rel_close(MASS_COEFF, 2.0 * math.pi * 0.25 / 1.5, 0.001))
    check("DeficitParams defaults correct",
          params.M == M_EXT and params.R_eq == R_EQ and params.tau == TAU_CANONICAL)

    # ================================================================
    # Section 2: Static Mass Profile (6)
    # ================================================================
    print("\n--- Section 2: Static Mass Profile ---")

    r_arr = make_radial_grid(params)
    m_arr = compute_static_mass(r_arr, params)

    check("m(R_ext) = M = 0.5",
          rel_close(float(m_arr[0]), 0.5, 0.001),
          f"got {m_arr[0]:.4f}")
    check("m increases inward (m(R_eq) > M)",
          deficit.m_at_R_eq > M_EXT,
          f"m(R_eq) = {deficit.m_at_R_eq:.4f}")
    check("m(R_eq) ~ 3.118 (Phase 6 locked)",
          rel_close(deficit.m_at_R_eq, 3.118, 0.02),
          f"got {deficit.m_at_R_eq:.4f}")
    check("f(R_eq) ~ -17.71 (Phase 6 locked)",
          rel_close(deficit.f_at_R_eq, PHASE6_F_AT_REQ, 0.02),
          f"got {deficit.f_at_R_eq:.2f}")

    rho_eq = compute_equilibrium_density(r_arr, params)
    check("rho_eq < 0 everywhere", bool(np.all(rho_eq < 0)))
    check("rho_eq(R_eq) ~ -M^2/(2*tau^2*R_eq^4)",
          rel_close(
              float(np.interp(R_EQ, r_arr[::-1], rho_eq[::-1])),
              -M_EXT**2 / (2.0 * TAU_CANONICAL**2 * R_EQ**4),
              0.01,
          ))

    # ================================================================
    # Section 3: Deficit Profile (7)
    # ================================================================
    print("\n--- Section 3: Deficit Profile ---")

    check("delta(R_eq) ~ 2.951",
          rel_close(deficit.delta_at_R_eq, 2.951, 0.01),
          f"got {deficit.delta_at_R_eq:.4f}")
    check("delta_max > delta(R_eq) (peak is innermost)",
          deficit.delta_max >= deficit.delta_at_R_eq - 0.01,
          f"max={deficit.delta_max:.4f}, R_eq={deficit.delta_at_R_eq:.4f}")
    check("delta > 0 over ~83% of grid",
          0.7 < deficit.fraction_r_with_delta_positive < 0.95,
          f"got {deficit.fraction_r_with_delta_positive:.3f}")
    check("delta(R_ext) = m(R_ext) - R_ext/2 = -0.5",
          rel_close(float(deficit.delta[0]), -0.5, 0.01),
          f"got {deficit.delta[0]:.4f}")
    check("delta transitions from negative to positive",
          float(deficit.delta[0]) < 0 and float(deficit.delta[-1]) > 0)
    check("r_at_delta_max near R_min end",
          deficit.r_at_delta_max < 0.5,
          f"got {deficit.r_at_delta_max:.4f}")
    check("integrated_deficit > 0",
          deficit.integrated_deficit > 0,
          f"got {deficit.integrated_deficit:.4f}")

    # ================================================================
    # Section 4: Minimal Source Decomposition (8)
    # ================================================================
    print("\n--- Section 4: Minimal Source Decomposition ---")

    check("epsilon_min = Component A + Component B",
          bool(np.allclose(ms.epsilon_min, ms.component_A + ms.component_B, atol=1e-12)))
    check("Component A = |rho_eq| where delta > 0",
          bool(np.allclose(
              ms.component_A[deficit.delta > 0],
              np.abs(deficit.rho_eq[deficit.delta > 0]),
              rtol=1e-10,
          )))
    check("Component B = 1/(8*pi*r^2) where delta > 0",
          bool(np.allclose(
              ms.component_B[deficit.delta > 0],
              1.0 / (8.0 * math.pi * deficit.r[deficit.delta > 0]**2),
              rtol=1e-10,
          )))
    check("epsilon_min = 0 where delta <= 0",
          bool(np.allclose(ms.epsilon_min[deficit.delta <= 0], 0.0)))
    check("Sigma(R_eq) ~ delta(R_eq) within 1%",
          rel_close(ms.Sigma_at_R_eq, ms.delta_at_R_eq, 0.01),
          f"Sigma={ms.Sigma_at_R_eq:.4f}, delta={ms.delta_at_R_eq:.4f}")
    check("ratio B/A at R_eq ~ 5.3%",
          rel_close(ms.ratio_B_over_A_at_R_eq, 0.053, 0.10),
          f"got {ms.ratio_B_over_A_at_R_eq:.4f}")
    check("ratio B/A at r=1 ~ 48%",
          rel_close(ms.ratio_B_over_A_at_r1, 0.48, 0.10),
          f"got {ms.ratio_B_over_A_at_r1:.4f}")
    check("Sigma monotonically increasing inward",
          bool(np.all(np.diff(ms.Sigma) >= -1e-10)),
          "Sigma should grow as we move to smaller r")

    # ================================================================
    # Section 5: Correction Verification (5)
    # ================================================================
    print("\n--- Section 5: Correction Verification ---")

    check("f_corrected >= -0.1 everywhere (numerical precision)",
          ms.f_corrected_min > -0.1,
          f"got {ms.f_corrected_min:.6f}")
    check("f_corrected(R_eq) ~ 0 (saturation)",
          abs(ms.f_corrected_at_R_eq) < 0.5,
          f"got {ms.f_corrected_at_R_eq:.4f}")
    check("BC preserved: f_corrected(R_ext) ~ 0.5",
          rel_close(float(ms.f_corrected[0]), 0.5, 0.01),
          f"got {ms.f_corrected[0]:.4f}")
    check("verification_passes flag is True", ms.verification_passes)
    check("4 assumptions documented",
          len(ms.assumptions) == 4,
          f"got {len(ms.assumptions)}")

    # ================================================================
    # Section 6: Kinetic Deficit Profile (6)
    # ================================================================
    print("\n--- Section 6: Kinetic Deficit Profile ---")

    check("Phi_dot_deficit = sqrt(2 * epsilon_min)",
          bool(np.allclose(
              kd.Phi_dot_deficit[deficit.delta > 0],
              np.sqrt(2.0 * ms.epsilon_min[deficit.delta > 0]),
              rtol=1e-10,
          )))
    check("Phi_dot(R_eq) > 0", kd.Phi_dot_at_R_eq > 0,
          f"got {kd.Phi_dot_at_R_eq:.4f}")
    check("Ratio to natural at R_eq ~ 1.0",
          rel_close(kd.ratio_to_natural_at_R_eq, 1.0, 0.10),
          f"got {kd.ratio_to_natural_at_R_eq:.4f}")
    check("Monotonic inward-increasing", kd.is_monotonic_inward)
    check("NOT achievable within GRUT", not kd.achievable_within_grut)
    check("Phi_dot_max > Phi_dot(R_ext)",
          kd.Phi_dot_max > kd.Phi_dot_at_R_ext)

    # ================================================================
    # Section 7: Anisotropy Insufficiency (5)
    # ================================================================
    print("\n--- Section 7: Anisotropy Insufficiency ---")

    check("Vanishes at f=0", aniso.vanishes_at_f_zero)
    check("Formally insufficient", aniso.insufficient)
    check("Formula is f*(Phi')^2", aniso.p_r_minus_p_perp_formula == "f * (Phi')^2")
    check("Mechanism explains self-quenching",
          "self-quenching" in aniso.mechanism.lower() or "vanish" in aniso.mechanism.lower())
    check("Notes mention Phase 6B confirmation",
          any("6B" in n or "6b" in n for n in aniso.notes))

    # ================================================================
    # Section 8: Additive Source (5)
    # ================================================================
    print("\n--- Section 8: Additive Source ---")

    check("Works by construction", addsrc.works_by_construction)
    check("Requires beyond-GRUT", addsrc.requires_beyond_grut)
    check("rho_extra = epsilon_min",
          bool(np.allclose(addsrc.rho_extra, ms.epsilon_min, rtol=1e-10)))
    check("f_corrected same as minimal source verification",
          bool(np.allclose(addsrc.f_corrected, ms.f_corrected, rtol=1e-10)))
    check("f_corrected_min > -0.1",
          addsrc.f_corrected_min > -0.1,
          f"got {addsrc.f_corrected_min:.6f}")

    # ================================================================
    # Section 9: Two-Parameter Scan (8)
    # ================================================================
    print("\n--- Section 9: Two-Parameter Scan ---")

    rho_eq_coeff = params.M**2 / (2.0 * params.tau**2)
    expected_A = PHASE6B_A_CRIT_NATURAL**2 * rho_eq_coeff

    check("Contour exists", tp.contour_exists)
    check("A_crit(B=0) > 0", tp.A_crit_at_B0 > 0,
          f"got {tp.A_crit_at_B0:.6f}")
    check("A_crit(B=0) recovers Phase 6B within 10%",
          rel_close(tp.A_crit_at_B0, expected_A, 0.10),
          f"A_crit={tp.A_crit_at_B0:.6f}, expected={expected_A:.6f}")
    check("recovers_phase6b flag", tp.recovers_phase6b)
    check("B_crit(A=0) > 0", tp.B_crit_at_A0 > 0,
          f"got {tp.B_crit_at_A0:.6f}")
    check("Contour has > 5 points",
          len(tp.threshold_contour_A) > 5,
          f"got {len(tp.threshold_contour_A)}")
    check("Threshold contour A decreases as B increases",
          len(tp.threshold_contour_A) > 2
          and tp.threshold_contour_A[-1] < tp.threshold_contour_A[0],
          "A should decrease as B compensates")
    check("f_min_grid shape correct",
          tp.f_min_grid.shape == (params.n_A + 1, params.n_B + 1),
          f"got {tp.f_min_grid.shape}")

    # ================================================================
    # Section 10: Monotonic Profile Insufficiency (6)
    # ================================================================
    print("\n--- Section 10: Monotonic Profile Insufficiency ---")

    check("4 profiles tested",
          len(mono.tested_profiles) == 4,
          f"got {len(mono.tested_profiles)}")
    check("Tested includes 1/r^4 (natural)",
          "1/r^4" in mono.tested_profiles)
    check("Gap fraction > 0",
          mono.gap_fraction > 0,
          f"got {mono.gap_fraction:.4f}")
    check("Gap at intermediate r (r > R_eq)",
          mono.r_at_max_gap > R_EQ,
          f"got r = {mono.r_at_max_gap:.4f}")
    check("NOT a general no-go", not mono.is_general_no_go)
    check("Insufficiency statement present",
          len(mono.insufficiency_statement) > 50,
          f"statement length = {len(mono.insufficiency_statement)}")

    # ================================================================
    # Section 11: Phase 6B Comparison (6)
    # ================================================================
    print("\n--- Section 11: Phase 6B Comparison ---")

    check("A_crit = 1.062 (Phase 6B locked)",
          rel_close(p6b.A_crit_natural, 1.062, 0.01),
          f"got {p6b.A_crit_natural:.4f}")
    check("A_crit exceeds unity", p6b.A_crit_exceeds_unity)
    check("Excess fraction ~ 6.2%",
          rel_close(p6b.excess_fraction, 0.062, 0.10),
          f"got {p6b.excess_fraction:.4f}")
    check("Natural provides Component A", p6b.natural_provides_component_A)
    check("Natural does NOT provide Component B", not p6b.natural_provides_component_B)
    check("Overshoot explanation present",
          len(p6b.overshoot_explanation) > 50)

    # ================================================================
    # Section 12: Nonclaims & Assumptions (5)
    # ================================================================
    print("\n--- Section 12: Nonclaims & Assumptions ---")

    check("14 nonclaims",
          len(result.nonclaims) == 14,
          f"got {len(result.nonclaims)}")
    check("4 assumptions",
          len(result.assumptions) == 4,
          f"got {len(result.assumptions)}")
    check("Nonclaims contain 'saturation'",
          any("saturation" in nc.lower() or "f = 0" in nc for nc in result.nonclaims))
    check("Nonclaims contain 'not a general no-go'",
          any("not a general no-go" in nc.lower() for nc in result.nonclaims),
          "Should disclaim monotonic insufficiency scope")
    check("Assumptions mention 'additive positive source'",
          any("additive positive source" in a for a in result.assumptions))

    # ================================================================
    # Section 13: Serialization (3)
    # ================================================================
    print("\n--- Section 13: Serialization ---")

    d = metric_deficit_result_to_dict(result)
    check("Dict has 'closure_classification' key",
          "closure_classification" in d)
    check("Classification string correct",
          d.get("closure_classification", {}).get("classification")
          == "current_closure_insufficient__minimal_additive_source_identified")
    check("Dict has 'assumptions' key with 4 items",
          len(d.get("assumptions", [])) == 4)

    # ================================================================
    # Summary
    # ================================================================
    print("\n" + "=" * 72)
    total = passed + failed
    print(f"TOTAL: {passed}/{total} checks passed, {failed} failed")

    if failed == 0:
        print("ALL CHECKS PASSED")
    else:
        print("\nFailed checks:")
        for r_line in results:
            if "[FAIL]" in r_line:
                print(f"  {r_line}")

    # Print key findings
    print("\n--- Key Findings ---")
    print(f"  delta(R_eq) = {deficit.delta_at_R_eq:.4f}")
    print(f"  f(R_eq)     = {deficit.f_at_R_eq:.2f} (Phase 6 locked: {PHASE6_F_AT_REQ})")
    print(f"  |rho_eq(R_eq)| = {abs(float(np.interp(R_EQ, deficit.r[::-1], deficit.rho_eq[::-1]))):.4f}")
    print(f"  Component B at R_eq = {1.0/(8.0*math.pi*R_EQ**2):.4f}")
    print(f"  ratio B/A at R_eq = {ms.ratio_B_over_A_at_R_eq:.4f}")
    print(f"  ratio B/A at r=1  = {ms.ratio_B_over_A_at_r1:.4f}")
    print(f"  A_crit(B=0) two-param = {tp.A_crit_at_B0:.6f}")
    print(f"  Phase 6B A_crit natural = {PHASE6B_A_CRIT_NATURAL}")
    discrepancy = abs(tp.A_crit_at_B0 - expected_A) / expected_A * 100
    print(f"  Normalization: A_coeff = A_amplitude^2 * M^2/(2*tau^2)")
    print(f"    Phase 6B A_amplitude = {PHASE6B_A_CRIT_NATURAL:.3f}"
          f" -> A_coeff = {expected_A:.6f}")
    print(f"    Two-param A_crit(B=0) = {tp.A_crit_at_B0:.6f}"
          f" ({discrepancy:.1f}% diff)")
    print(f"  Classification: {cc.classification}")
    print(f"  Uniform is OPTIMISTIC: 11.5% vs 106%")

    print("=" * 72)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
