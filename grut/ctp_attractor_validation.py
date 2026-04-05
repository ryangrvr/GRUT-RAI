"""
Book XXI Delta (Validation) — Strange Attractor Verification
=============================================================

Three tests required before claiming SRB measure:
  1. True boundedness (10x longer integration; no secular drift)
  2. Attractor geometry (Kaplan-Yorke dimension; Poincare section)
  3. Numerical robustness (timestep invariance; Gram-Schmidt frequency invariance)

Plus structural stability: does the attractor persist across lambda values?

Uses the g_p = 0 system (pure CTP doubling + hedgehog):
  Phi_+'' + (2/r)Phi_+' + (1/tau^2)Phi_+ - X(r)/tau^2 = 0
  Phi_-'' + (2/r)Phi_-' - (1/tau^2)Phi_- = 0
  f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0

6D system: (Phi_+, Phi_+', Phi_-, Phi_-', f, f')
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

ETA = 1.0 / math.sqrt(8.0 * math.pi)
TAU_SQ = 1.5
M_EXT = 0.5
N_DIM = 6


def F(r, y, lam):
    """6D ODE at g_p = 0."""
    Pp, dPp, Pm, dPm, fv, dfv = y
    rs = max(r, 1e-10)
    r2 = rs * rs
    X_r = M_EXT / r2
    return np.array([
        dPp,
        (-2.0/rs)*dPp + (1.0/TAU_SQ)*Pp - X_r/TAU_SQ,
        dPm,
        (-2.0/rs)*dPm - (1.0/TAU_SQ)*Pm,
        dfv,
        (-2.0/rs)*dfv + (2.0/r2)*fv + lam*ETA**2*fv*(fv**2 - 1.0),
    ])


def J_analytical(r, y, lam):
    """Analytical 6x6 Jacobian at g_p = 0."""
    Pp, dPp, Pm, dPm, fv, dfv = y
    rs = max(r, 1e-10)
    r2 = rs * rs
    J = np.zeros((N_DIM, N_DIM))
    J[0, 1] = 1.0
    J[1, 0] = 1.0/TAU_SQ
    J[1, 1] = -2.0/rs
    J[2, 3] = 1.0
    J[3, 2] = -1.0/TAU_SQ
    J[3, 3] = -2.0/rs
    J[4, 5] = 1.0
    J[5, 4] = 2.0/r2 + lam*ETA**2*(3.0*fv**2 - 1.0)
    J[5, 5] = -2.0/rs
    return J


def rk4(r, y, dr, lam):
    k1 = dr * F(r, y, lam)
    k2 = dr * F(r + dr/2, y + k1/2, lam)
    k3 = dr * F(r + dr/2, y + k2/2, lam)
    k4 = dr * F(r + dr, y + k3, lam)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0


def initial_state(lam, r0=0.5, pm_init=0.01):
    delta = 1.0 / math.sqrt(max(lam * ETA**2, 0.01))
    f0 = r0 / math.sqrt(r0**2 + delta**2)
    df0 = delta**2 / (r0**2 + delta**2)**1.5
    return np.array([M_EXT/r0**2, -2*M_EXT/r0**3, pm_init, 0.0, f0, df0])


def benettin(lam, dr, r_start, r_end, renorm_int, pm_init=0.01):
    """Benettin with analytical Jacobian. Returns (spectrum, bounded, norms, le_history)."""
    n_steps = int((r_end - r_start) / dr)
    y = initial_state(lam, r_start, pm_init)
    Q = np.eye(N_DIM)
    lyap_sum = np.zeros(N_DIM)
    total_L = 0.0
    norms = []
    le_history = []
    r = r_start

    for step in range(n_steps):
        norm = np.linalg.norm(y)
        if norm > 1e12:
            return None, False, norms, le_history
        if step % 200 == 0:
            norms.append((r, norm))

        y = rk4(r, y, dr, lam)
        Jac = J_analytical(r, y, lam)
        Q = Q + dr * (Jac @ Q)
        r += dr
        total_L += dr

        if (step + 1) % renorm_int == 0:
            Q_o, R = np.linalg.qr(Q)
            for i in range(N_DIM):
                d = abs(R[i, i])
                if d > 1e-30:
                    lyap_sum[i] += math.log(d)
            Q = Q_o
            if total_L > 0:
                le_history.append(sorted(lyap_sum / total_L, reverse=True))

    if total_L > 0:
        Q_o, R = np.linalg.qr(Q)
        for i in range(N_DIM):
            d = abs(R[i, i])
            if d > 1e-30:
                lyap_sum[i] += math.log(d)

    spectrum = sorted(lyap_sum / total_L, reverse=True) if total_L > 0 else [0]*N_DIM
    return spectrum, True, norms, le_history


if __name__ == "__main__":
    print("=" * 80)
    print("  STRANGE ATTRACTOR VALIDATION — g_p = 0 (pure CTP + hedgehog)")
    print("=" * 80)

    # ================================================================
    # TEST 1: TRUE BOUNDEDNESS (10x longer integration)
    # ================================================================
    print("\n" + "=" * 80)
    print("  TEST 1: TRUE BOUNDEDNESS")
    print("  Integration to r = 150 (10x baseline of r = 15)")
    print("=" * 80)

    lam_test = 0.1
    sp, bounded, norms, hist = benettin(lam_test, dr=0.001, r_start=0.5, r_end=150.0,
                                         renorm_int=50, pm_init=0.01)
    if bounded and sp:
        print("  Bounded: YES")
        print("  Spectrum: [{}]".format(", ".join("{:.4f}".format(x) for x in sp)))
        print("  Sum LE: {:.4f}".format(sum(sp)))
        # Check secular drift in norms
        if len(norms) > 10:
            early = [n for r, n in norms if r < 20]
            late = [n for r, n in norms if r > 130]
            if early and late:
                print("  ||y|| early (r<20):  mean={:.2e}, max={:.2e}".format(
                    np.mean(early), np.max(early)))
                print("  ||y|| late (r>130):  mean={:.2e}, max={:.2e}".format(
                    np.mean(late), np.max(late)))
                drift = np.mean(late) / max(np.mean(early), 1e-30)
                print("  Drift ratio (late/early): {:.2f}".format(drift))
                if drift < 10:
                    print("  ==> NO SECULAR DRIFT (ratio < 10)")
                else:
                    print("  ==> SECULAR DRIFT DETECTED (ratio >= 10)")
        # LE convergence
        if hist:
            n = len(hist)
            checkpoints = [n//4, n//2, 3*n//4, n-1]
            print("  LE1 convergence:")
            for idx in checkpoints:
                if idx < n:
                    print("    step {}: LE1 = {:.4f}".format(idx, hist[idx][0]))
    else:
        print("  Bounded: NO (diverged)")

    # ================================================================
    # TEST 2: ATTRACTOR GEOMETRY (Kaplan-Yorke dimension)
    # ================================================================
    print("\n" + "=" * 80)
    print("  TEST 2: ATTRACTOR GEOMETRY (Kaplan-Yorke dimension)")
    print("=" * 80)

    if bounded and sp:
        # Kaplan-Yorke: D_KY = j + sum(LE_1..j) / |LE_{j+1}|
        # where j = largest integer such that sum(LE_1..j) >= 0
        sorted_les = sorted(sp, reverse=True)
        cumsum = 0
        j_ky = 0
        for i, le in enumerate(sorted_les):
            cumsum += le
            if cumsum >= 0:
                j_ky = i + 1
            else:
                break

        if j_ky > 0 and j_ky < len(sorted_les):
            partial_sum = sum(sorted_les[:j_ky])
            D_KY = j_ky + partial_sum / abs(sorted_les[j_ky])
        else:
            D_KY = float(len(sorted_les))

        print("  Lyapunov spectrum: {}".format(
            ", ".join("{:.4f}".format(x) for x in sorted_les)))
        print("  j (positive cumsum): {}".format(j_ky))
        print("  Kaplan-Yorke dimension: {:.4f}".format(D_KY))
        if D_KY != int(D_KY):
            print("  ==> FRACTIONAL (strange attractor signature)")
        else:
            print("  ==> INTEGER (not strange attractor)")
    else:
        print("  SKIPPED (trajectory not bounded)")

    # ================================================================
    # TEST 3: NUMERICAL ROBUSTNESS
    # ================================================================
    print("\n" + "=" * 80)
    print("  TEST 3: NUMERICAL ROBUSTNESS")
    print("  Timestep refinement: dr = 0.002, 0.001, 0.0005")
    print("  Renorm interval: 25, 50, 100")
    print("=" * 80)

    for dr_test in [0.002, 0.001, 0.0005]:
        for ri in [25, 50, 100]:
            sp_t, bnd, _, _ = benettin(lam_test, dr=dr_test, r_start=0.5, r_end=50.0,
                                        renorm_int=ri, pm_init=0.01)
            if bnd and sp_t:
                print("  dr={:.4f}, renorm={:3d}: LE1={:.4f}, LE2={:.4f}, sum={:.4f}".format(
                    dr_test, ri, sp_t[0], sp_t[1], sum(sp_t)))
            else:
                print("  dr={:.4f}, renorm={:3d}: DIVERGED".format(dr_test, ri))

    # ================================================================
    # TEST 4: STRUCTURAL STABILITY (lambda scan)
    # ================================================================
    print("\n" + "=" * 80)
    print("  TEST 4: STRUCTURAL STABILITY")
    print("  Lambda scan at g_p = 0: does the attractor persist?")
    print("=" * 80)

    print("  {:>8s} {:>8s} {:>8s} {:>8s} {:>10s} {:>8s} {:>10s}".format(
        "lambda", "LE1", "LE2", "LE3", "SumLE", "D_KY", "Bounded"))
    print("  " + "-" * 70)

    for lam_scan in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0]:
        sp_s, bnd_s, _, _ = benettin(lam_scan, dr=0.001, r_start=0.5, r_end=50.0,
                                      renorm_int=50, pm_init=0.01)
        if bnd_s and sp_s:
            sorted_s = sorted(sp_s, reverse=True)
            cs = 0
            j = 0
            for i, le in enumerate(sorted_s):
                cs += le
                if cs >= 0:
                    j = i + 1
                else:
                    break
            if j > 0 and j < len(sorted_s):
                dky = j + sum(sorted_s[:j]) / abs(sorted_s[j])
            else:
                dky = float(len(sorted_s))
            print("  {:8.2f} {:8.4f} {:8.4f} {:8.4f} {:10.4f} {:8.4f} {:>10s}".format(
                lam_scan, sorted_s[0], sorted_s[1], sorted_s[2],
                sum(sorted_s), dky, "YES"))
        else:
            print("  {:8.2f} {:>8s} {:>8s} {:>8s} {:>10s} {:>8s} {:>10s}".format(
                lam_scan, "—", "—", "—", "—", "—", "DIVERGED"))

    print("\n" + "=" * 80)
    print("  VALIDATION COMPLETE")
    print("=" * 80)
