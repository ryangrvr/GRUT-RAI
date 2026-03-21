#!/usr/bin/env python3
"""Benchmark: Phase 6B — Dynamical Non-Equilibrium Interior Branch.

~80 independent checks covering:
  1.  Parameter Setup (6)
  2.  Stress-Energy with Phi-dot (8)
  3.  Profile Generators (6)
  4.  Radial Snapshot — Uniform (6)
  5.  Radial Snapshot — Natural (6)
  6.  Radial Snapshot — Relaxation (5)
  7.  Profile Library & Thresholds (8)
  8.  Phase 6 Comparison (5)
  9.  Time Evolution (8)
  10. Threshold Classification (6)
  11. Anisotropy Comparison (6)
  12. Nonclaims (4)
  13. Serialization (3)

KEY FINDINGS:
  The Phase 6 "11.5% of natural rate" is an artifact of UNIFORM processing.
  For the physically motivated "natural" profile, A_crit ~ 1.06 (106% of
  natural rate).  Dynamical collapse produces CONCENTRATED processing that
  is even less efficient — the metric positivity obstruction is GLOBAL and
  ROBUST under realistic collapse perturbations.  Anisotropy self-quenches
  at f = 0, contributing < 1% to the threshold.
"""

from __future__ import annotations

import math
import sys
import numpy as np

from grut.dynamical_interior import (
    compute_dynamical_analysis,
    dynamical_result_to_dict,
    DynamicalParams,
    PhiDotProfile,
    stress_energy_dynamical,
    make_radial_grid,
    make_phi_dot_profile,
    solve_radial_snapshot,
    scan_amplitude_threshold,
    build_profile_library,
    evolve_quasi_static,
    classify_threshold,
    compare_anisotropy,
    build_phase6_comparison,
    ALPHA_VAC,
    BETA_Q,
    R_S,
    M_EXT,
    R_EQ,
    C_COMPACTNESS,
    TAU_CANONICAL,
    A_EFF_CONSTITUTIVE,
    A_SCHW,
    NONCLAIMS,
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
    print("BENCHMARK: Phase 6B — Dynamical Non-Equilibrium Interior Branch")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running dynamical interior analysis...")
    params = DynamicalParams(n_r=400, n_t=100)
    r = compute_dynamical_analysis(params)
    print(f"  Analysis complete. Valid: {r.valid}\n")

    # ================================================================
    # Section 1: Parameter Setup
    # ================================================================
    print("\n--- Section 1: Parameter Setup ---")

    check("alpha_vac = 1/3", close(ALPHA_VAC, 1.0 / 3.0))
    check("M = r_s/2 = 0.5", close(M_EXT, 0.5))
    check("R_eq = r_s/3", close(R_EQ, 1.0 / 3.0))
    check("tau = sqrt(C/2) ~ 1.2247", close(TAU_CANONICAL, math.sqrt(1.5), 1e-4))
    check("DynamicalParams has defaults",
          params.M == M_EXT and params.R_eq == R_EQ and params.tau == TAU_CANONICAL)
    check("R_ext = 2*r_s", close(params.R_ext, 2.0))

    # ================================================================
    # Section 2: Stress-Energy with Phi-dot
    # ================================================================
    print("\n--- Section 2: Stress-Energy with Phi-dot ---")

    # At r=1, m=0.3, Phi=0.4, Phi'=0.1, Phi_dot=0.5, nu=0.1, tau=1.2
    rho, p_r, p_p = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.1, 1.2)
    f_test = 1.0 - 2.0 * 0.3 / 1.0  # = 0.4
    e_m2nu = math.exp(-0.2)

    temporal_k = 0.5 * e_m2nu * 0.25  # 0.5 * e^{-2nu} * Phi_dot^2
    spatial_k = 0.5 * 0.01 * f_test   # 0.5 * (Phi')^2 * f
    V = 0.16 / (2 * 1.44)             # Phi^2 / (2 tau^2)
    PhiJ = 0.4 * 0.3 / 1.2            # Phi * X / tau (X = m/r^2 = 0.3)

    check("NEC radial: rho + p_r >= 0", rho + p_r >= -1e-15,
          f"rho+p_r = {rho + p_r:.8f}")
    check("NEC tangential: rho + p_perp >= 0", rho + p_p >= -1e-15,
          f"rho+p_perp = {rho + p_p:.8f}")
    check("NEC_t = e^{-2nu}*Phi_dot^2",
          close(rho + p_p, e_m2nu * 0.25, 1e-10),
          f"got {rho + p_p:.8f}, expected {e_m2nu * 0.25:.8f}")
    check("Anisotropy = f*(Phi')^2",
          close(p_r - p_p, f_test * 0.01, 1e-10),
          f"got {p_r - p_p:.8f}, expected {f_test * 0.01:.8f}")

    # Static limit: Phi_dot = 0, Phi' = 0, nonzero Phi
    rho0, pr0, pp0 = stress_energy_dynamical(1.0, 0.3, 0.4, 0.0, 0.0, 0.0, 1.2)
    rho_eq_expected = 0.16 / (2 * 1.44) - 0.4 * 0.3 / 1.2  # V - PhiJ
    check("Static: Phi_dot=0 recovers rho_eq (V - PhiJ)",
          close(rho0, rho_eq_expected, 1e-10),
          f"rho0={rho0:.8f}, expected={rho_eq_expected:.8f}")
    check("Static: p_r = p_perp (isotropic when Phi'=0)",
          close(pr0, pp0, 1e-15))

    # Anisotropy vanishes at f=0 (r=2m → Schwarzschild radius)
    rho_sc, pr_sc, pp_sc = stress_energy_dynamical(1.0, 0.5, 0.4, 0.3, 0.2, 0.0, 1.2)
    check("Anisotropy vanishes at f=0",
          close(pr_sc - pp_sc, 0.0, 1e-15),
          f"p_r - p_perp = {pr_sc - pp_sc:.8e}")

    # Positive Phi_dot increases rho vs static
    rho_pd, _, _ = stress_energy_dynamical(1.0, 0.3, 0.0, 0.0, 1.0, 0.0, 1.2)
    check("Phi_dot > 0 raises rho above static",
          rho_pd > rho0,
          f"rho(Phi_dot=1) = {rho_pd:.6f}, rho(static) = {rho0:.6f}")

    # ================================================================
    # Section 3: Profile Generators
    # ================================================================
    print("\n--- Section 3: Profile Generators ---")

    r_arr = make_radial_grid(params)
    check("Grid is decreasing (R_ext to R_min)", r_arr[0] > r_arr[-1],
          f"r[0]={r_arr[0]:.4f}, r[-1]={r_arr[-1]:.4f}")

    prof_u = make_phi_dot_profile("uniform", r_arr, params, amplitude=1.0)
    check("Uniform: constant Phi_dot",
          close(float(np.std(prof_u.Phi_dot)), 0.0, 1e-15))

    prof_n = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
    check("Natural: Phi_dot = X(r)/tau (peaks at small r)",
          float(prof_n.Phi_dot[-1]) > float(prof_n.Phi_dot[0]),
          f"Phi_dot(R_min)={prof_n.Phi_dot[-1]:.4f} > Phi_dot(R_ext)={prof_n.Phi_dot[0]:.4f}")

    prof_g = make_phi_dot_profile("gaussian", r_arr, params, amplitude=1.0,
                                  r_center=R_EQ, sigma=0.2)
    idx_peak = np.argmax(prof_g.Phi_dot)
    check("Gaussian: peaks near R_eq",
          abs(r_arr[idx_peak] - R_EQ) < 0.3,
          f"peak at r={r_arr[idx_peak]:.3f}, R_eq={R_EQ:.3f}")

    check("Epsilon = 0.5*Phi_dot^2",
          close(float(np.max(np.abs(prof_u.epsilon - 0.5 * prof_u.Phi_dot ** 2))), 0.0, 1e-15))

    check("Profile type stored",
          prof_n.profile_type == "natural" and prof_u.profile_type == "uniform")

    # ================================================================
    # Section 4: Radial Snapshot — Uniform
    # ================================================================
    print("\n--- Section 4: Radial Snapshot — Uniform ---")

    # Zero amplitude → should recover Phase 6 static result
    prof_zero = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.0)
    snap_zero = solve_radial_snapshot(prof_zero, params)
    check("Zero amplitude: f(R_eq) ~ -17.71 (Phase 6)",
          rel_close(snap_zero.f_at_R_eq, -17.71, 0.01),
          f"f(R_eq) = {snap_zero.f_at_R_eq:.4f}")
    check("Zero amplitude: m(R_eq) ~ 3.12",
          rel_close(snap_zero.m_at_R_eq, 3.118, 0.01),
          f"m(R_eq) = {snap_zero.m_at_R_eq:.4f}")

    # Phase 6 critical Phi_dot
    tau2 = params.tau ** 2
    coeff = 2.0 * math.pi * M_EXT ** 2 / tau2
    m_static = M_EXT + coeff * (1.0 / R_EQ - 1.0 / params.R_ext)
    vol = (4.0 * math.pi / 3.0) * (params.R_ext ** 3 - R_EQ ** 3)
    eps6 = (m_static - R_EQ / 2.0) / vol
    Phi_dot_crit_6 = math.sqrt(2.0 * eps6)

    prof_crit = make_phi_dot_profile("uniform", r_arr, params, amplitude=Phi_dot_crit_6)
    snap_crit = solve_radial_snapshot(prof_crit, params)
    check("Uniform at Phase6 crit: f(R_eq) ~ 0",
          abs(snap_crit.f_at_R_eq) < 0.01,
          f"f(R_eq) = {snap_crit.f_at_R_eq:.6f}")

    # BC: m(R_ext) = M
    check("BC: m(R_ext) = M", close(snap_crit.m[0], M_EXT, 1e-10),
          f"m[0] = {snap_crit.m[0]:.8f}")

    # NEC satisfied
    check("NEC radial >= 0", snap_crit.nec_radial_min >= -1e-10,
          f"min = {snap_crit.nec_radial_min:.6f}")
    check("NEC tangential >= 0", snap_crit.nec_tangential_min >= -1e-10,
          f"min = {snap_crit.nec_tangential_min:.6f}")

    # ================================================================
    # Section 5: Radial Snapshot — Natural
    # ================================================================
    print("\n--- Section 5: Radial Snapshot — Natural ---")

    # At A=1: rho_eq + epsilon = 0 → m = M const → f = 1 - 2M/r
    prof_nat1 = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
    snap_nat1 = solve_radial_snapshot(prof_nat1, params)
    f_expected_nat1 = 1.0 - 2.0 * M_EXT / R_EQ
    check("Natural A=1: f(R_eq) = 1 - 2M/R_eq = -2",
          close(snap_nat1.f_at_R_eq, f_expected_nat1, 0.01),
          f"f(R_eq) = {snap_nat1.f_at_R_eq:.4f}, expected {f_expected_nat1:.4f}")
    check("Natural A=1: m(R_eq) = M (rho cancels)",
          close(snap_nat1.m_at_R_eq, M_EXT, 0.01),
          f"m = {snap_nat1.m_at_R_eq:.4f}")

    # A=1 still has f < 0 (natural rate insufficient)
    check("Natural A=1: f(R_eq) < 0",
          snap_nat1.f_at_R_eq < 0,
          f"f = {snap_nat1.f_at_R_eq:.4f}")

    # Above threshold: A > A_crit should give f > 0 at R_eq
    prof_nat_hi = make_phi_dot_profile("natural", r_arr, params, amplitude=1.2)
    snap_nat_hi = solve_radial_snapshot(prof_nat_hi, params)
    check("Natural A=1.2: f(R_eq) > 0",
          snap_nat_hi.f_at_R_eq > 0,
          f"f = {snap_nat_hi.f_at_R_eq:.4f}")

    check("Natural NEC tangential >= 0", snap_nat1.nec_tangential_min >= -1e-10)
    check("Natural BC: m(R_ext) = M", close(snap_nat1.m[0], M_EXT, 1e-10))

    # ================================================================
    # Section 6: Radial Snapshot — Relaxation
    # ================================================================
    print("\n--- Section 6: Radial Snapshot — Relaxation ---")

    prof_rel = make_phi_dot_profile("relaxation", r_arr, params, amplitude=1.0)
    snap_rel = solve_radial_snapshot(prof_rel, params)
    check("Relaxation A=1: concentrated at small r",
          float(prof_rel.Phi_dot[-1]) > 10.0 * float(prof_rel.Phi_dot[0]),
          f"ratio = {float(prof_rel.Phi_dot[-1] / prof_rel.Phi_dot[0]):.1f}")

    # Relaxation improves f(R_eq) vs static
    check("Relaxation A=1: f(R_eq) better than static",
          snap_rel.f_at_R_eq > snap_zero.f_at_R_eq,
          f"f_rel={snap_rel.f_at_R_eq:.4f}, f_static={snap_zero.f_at_R_eq:.4f}")

    # Relaxation at high amplitude can fix f(R_eq) but not f_min
    prof_rel_hi = make_phi_dot_profile("relaxation", r_arr, params, amplitude=5.0)
    snap_rel_hi = solve_radial_snapshot(prof_rel_hi, params)
    check("Relaxation A=5: f(R_eq) > 0 (localized fix)",
          snap_rel_hi.f_at_R_eq > 0,
          f"f(R_eq) = {snap_rel_hi.f_at_R_eq:.4f}")
    check("Relaxation A=5: f_min still < 0 (can't fix globally)",
          snap_rel_hi.f_min < 0,
          f"f_min = {snap_rel_hi.f_min:.4f}")
    check("Relaxation NEC tangential >= 0",
          snap_rel.nec_tangential_min >= -1e-10)

    # ================================================================
    # Section 7: Profile Library & Thresholds
    # ================================================================
    print("\n--- Section 7: Profile Library & Thresholds ---")

    pl = r.profile_library
    check("Profile library exists", pl is not None)

    if pl is not None:
        check("Uniform A_crit_R_eq matches Phase6 Phi_dot",
              rel_close(pl.uniform.A_crit_R_eq, Phi_dot_crit_6, 0.03),
              f"got {pl.uniform.A_crit_R_eq:.4f}, expected {Phi_dot_crit_6:.4f}")

        check("Natural A_crit_R_eq > 1 (above natural rate)",
              pl.natural.A_crit_R_eq > 1.0,
              f"A_crit = {pl.natural.A_crit_R_eq:.4f}")

        check("Natural A_crit > Uniform A_crit (concentrated less efficient)",
              pl.natural.A_crit_global > pl.uniform.A_crit_global,
              f"nat={pl.natural.A_crit_global:.4f}, uni={pl.uniform.A_crit_global:.4f}")

        check("Relaxation: no global threshold",
              not pl.relaxation.A_crit_exists,
              f"exists={pl.relaxation.A_crit_exists}")
        check("Gaussian: no global threshold",
              not pl.gaussian.A_crit_exists,
              f"exists={pl.gaussian.A_crit_exists}")

        check("Most efficient = uniform",
              pl.most_efficient_profile == "uniform",
              f"got {pl.most_efficient_profile}")

        check("Phase 6 uniform recovery",
              pl.uniform_recovery,
              "uniform A_crit_R_eq does not match Phase 6")

        # Uniform is most efficient because it spreads energy everywhere
        # Natural needs amplitude > 1 because it wastes energy at small r
        check("Uniform threshold exists",
              pl.uniform.A_crit_exists)

        print(f"\n  PROFILE LIBRARY:")
        for name in ["uniform", "natural", "relaxation", "gaussian"]:
            ptr = getattr(pl, name)
            if ptr:
                print(f"    {name:12s}: A_crit_global={ptr.A_crit_global:.4f}"
                      f", A_crit_R_eq={ptr.A_crit_R_eq:.4f}"
                      f", exists={ptr.A_crit_exists}")

    # ================================================================
    # Section 8: Phase 6 Comparison
    # ================================================================
    print("\n--- Section 8: Phase 6 Comparison ---")

    p6 = r.phase6_comparison
    check("Phase 6 comparison exists", p6 is not None)

    if p6 is not None:
        check("Phase6 eps_crit matches analytical",
              rel_close(p6.phase6_epsilon_crit, eps6, 1e-6),
              f"got {p6.phase6_epsilon_crit:.6f}")

        X_eq = M_EXT / (R_EQ ** 2)
        Phi_dot_natural = X_eq / params.tau
        ratio_expected = Phi_dot_crit_6 / Phi_dot_natural
        check("Phase6 ratio ~ 11.5%",
              rel_close(p6.phase6_Phi_dot_ratio, ratio_expected, 0.01),
              f"got {p6.phase6_Phi_dot_ratio*100:.1f}%, expected {ratio_expected*100:.1f}%")

        check("Natural A_crit > Phase6 ratio (uniform is optimistic)",
              p6.natural_A_crit > p6.phase6_Phi_dot_ratio * 2,
              f"nat={p6.natural_A_crit:.3f}, phase6={p6.phase6_Phi_dot_ratio:.3f}")

        check("Uniform IS optimistic",
              p6.uniform_is_optimistic)

        check("Dynamical exceeds uniform threshold",
              p6.dynamical_exceeds_threshold)

    # ================================================================
    # Section 9: Time Evolution
    # ================================================================
    print("\n--- Section 9: Time Evolution ---")

    ev = r.time_evolution
    check("Time evolution exists", ev is not None)

    if ev is not None:
        check("Number of time steps matches params",
              ev.n_steps == params.n_t,
              f"n_steps={ev.n_steps}, n_t={params.n_t}")

        check("Multiple time slices stored",
              len(ev.slices) >= 3,
              f"len(slices) = {len(ev.slices)}")

        # Phi_dot peak at t=0 (initial perturbation)
        check("Phi_dot peaks at t=0",
              close(ev.Phi_dot_peak_time, 0.0, params.dt_over_tau * params.tau * 2),
              f"peak at t={ev.Phi_dot_peak_time:.4f}")

        # Phi_dot decays exponentially
        t_arr = ev.t_array
        pdm = ev.Phi_dot_max_vs_t
        if pdm[0] > 0:
            tau = params.tau
            idx_3tau = np.argmin(np.abs(t_arr - 3 * tau))
            decay = pdm[idx_3tau] / pdm[0]
            expected_decay = math.exp(-3.0)
            check("Phi_dot decays as exp(-t/tau) at 3*tau",
                  rel_close(decay, expected_decay, 0.15),
                  f"ratio={decay:.4f}, expected={expected_decay:.4f}")
        else:
            check("Phi_dot decays as exp(-t/tau)", False, "pdm[0] = 0")

        # f(R_eq) improves at early times (processing helps)
        check("f(R_eq) at t=0 better than static",
              ev.f_at_R_eq_vs_t[0] > snap_zero.f_at_R_eq * 1.001,
              f"f(0)={ev.f_at_R_eq_vs_t[0]:.4f}, static={snap_zero.f_at_R_eq:.4f}")

        # f(R_eq) approaches static at late times
        f_late = ev.f_at_R_eq_vs_t[-1]
        check("f(R_eq) approaches static at late times",
              rel_close(f_late, snap_zero.f_at_R_eq, 0.08),
              f"f(late)={f_late:.4f}, static={snap_zero.f_at_R_eq:.4f}")

        # With default collapse_amplitude, never positive globally
        check("Default collapse: f never positive everywhere",
              ev.never_positive,
              f"never_positive={ev.never_positive}")

        # f_min is always negative
        check("f_min always < 0",
              np.all(ev.f_min_vs_t < 0),
              f"max(f_min_vs_t) = {float(np.max(ev.f_min_vs_t)):.4f}")

    # ================================================================
    # Section 10: Threshold Classification
    # ================================================================
    print("\n--- Section 10: Threshold Classification ---")

    tc = r.threshold_classification
    check("Classification exists", tc is not None)

    if tc is not None:
        check("Spatial: global (violation spans most of barrier)",
              tc.spatial_class == "global",
              f"got {tc.spatial_class}")

        check("Temporal: robust (not healed by processing)",
              tc.temporal_class == "robust",
              f"got {tc.temporal_class}")

        check("Combined: global_robust",
              tc.classification == "global_robust",
              f"got {tc.classification}")

        check("f_min_global < 0",
              tc.f_min_global < 0,
              f"f_min = {tc.f_min_global:.4f}")

        check("Fraction of r with f<0 > 50%",
              tc.fraction_r_negative > 0.5,
              f"frac = {tc.fraction_r_negative:.2f}")

        check("Does not heal within simulation",
              not tc.heals_within_simulation)

    # ================================================================
    # Section 11: Anisotropy Comparison
    # ================================================================
    print("\n--- Section 11: Anisotropy Comparison ---")

    an = r.anisotropy
    check("Anisotropy comparison exists", an is not None)

    if an is not None:
        check("Iso A_crit > 0", an.iso_A_crit > 0,
              f"iso_A_crit = {an.iso_A_crit:.4f}")
        check("Aniso A_crit > 0", an.aniso_A_crit > 0,
              f"aniso_A_crit = {an.aniso_A_crit:.4f}")

        check("|delta_A_crit| < 1% (anisotropy negligible)",
              abs(an.delta_A_crit_fraction) < 0.01,
              f"|delta| = {abs(an.delta_A_crit_fraction)*100:.2f}%")

        check("Anisotropy does NOT matter for threshold",
              not an.anisotropy_matters)

        # Self-quenching: at f=0, p_r - p_perp = f*(Phi')^2 = 0
        check("Self-quenching at f=0: anisotropy ~ 0 at threshold",
              abs(an.delta_A_crit_fraction) < 0.02,
              f"delta = {an.delta_A_crit_fraction*100:.2f}%")

        check("Both iso and aniso A_crit agree within 2%",
              abs(an.aniso_A_crit - an.iso_A_crit) / an.iso_A_crit < 0.02,
              f"iso={an.iso_A_crit:.4f}, aniso={an.aniso_A_crit:.4f}")

    # ================================================================
    # Section 12: Nonclaims
    # ================================================================
    print("\n--- Section 12: Nonclaims ---")

    check("NONCLAIMS list is nonempty", len(NONCLAIMS) >= 10,
          f"count = {len(NONCLAIMS)}")
    check("Nonclaim mentions quasi-static limitation",
          any("quasi-static" in nc.lower() for nc in NONCLAIMS))
    check("Nonclaim mentions uniform optimism",
          any("uniform" in nc.lower() and "optimistic" in nc.lower()
              for nc in NONCLAIMS))
    check("Nonclaims in master result",
          len(r.nonclaims) >= 10)

    # ================================================================
    # Section 13: Serialization
    # ================================================================
    print("\n--- Section 13: Serialization ---")

    d = dynamical_result_to_dict(r)
    check("Serialization dict is nonempty", len(d) > 0)
    check("Contains profile_library key", "profile_library" in d)
    check("Contains nonclaims", "nonclaims" in d and len(d["nonclaims"]) >= 10)

    # ================================================================
    # Summary
    # ================================================================
    print("\n" + "=" * 72)
    total = passed + failed
    print(f"RESULTS: {passed}/{total} passed, {failed} failed")

    if failed == 0:
        print("ALL CHECKS PASSED")
    else:
        print("\nFailed checks:")
        for msg in results:
            if "[FAIL]" in msg:
                print(msg)

    print("\n  KEY PHASE 6B FINDINGS:")
    if pl is not None:
        print(f"    Uniform A_crit_R_eq   = {pl.uniform.A_crit_R_eq:.4f}"
              f" (ratio to natural = {p6.phase6_Phi_dot_ratio*100:.1f}%)")
        print(f"    Natural A_crit_R_eq   = {pl.natural.A_crit_R_eq:.4f}"
              f" ({pl.natural.A_crit_R_eq*100:.1f}% of natural rate)")
        print(f"    Natural A_crit_global = {pl.natural.A_crit_global:.4f}")
    if tc is not None:
        print(f"    Classification        = {tc.classification}")
    if an is not None:
        print(f"    Anisotropy effect      = {an.delta_A_crit_fraction*100:.2f}%")
    print(f"    Uniform is OPTIMISTIC: 11.5% vs {pl.natural.A_crit_R_eq*100:.0f}%"
          if pl is not None else "")

    print("=" * 72)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
