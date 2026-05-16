"""
R Target Inversion (Gate 2b).

PURPOSE
-------
Given the target R = 1.15470 (canonical) or R = 1.15428 (V4.3-stated), what
matrix change is minimally required to hit it?

This script does NOT freely tune all matrix entries. Instead, it tests
CONSTRAINED variations:
  • Vary only M11 (Euler diagonal) — find required M11
  • Vary only off-diagonal scale — find required loop-suppression factor
  • Vary only RG-time scaling — find required t multiplier
  • Vary only one row/column — find which sector is culprit
  • Global L2-penalized deformation — find minimal Frobenius norm change

RESULT
------
For each constraint mode, outputs the minimal change and what it implies for
the physics (missing physics vs tuning).
"""
from __future__ import annotations

import math
from typing import Dict, Any

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar, minimize

from grut.derivation.euler.v4_matrix_resolution import (
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)
from grut.derivation.euler.v5_loop_suppressed_matrix import build_v5_matrix

# Target values
R_CANONICAL = math.sqrt(4.0 / 3.0)  # 1.15470...
R_V43_STATED = 1.15428


def evolve_euler_channel(M: np.ndarray, t_scale: float = 1.0) -> tuple[float, float]:
    """Evolve Euler channel with optional time scaling."""
    C0 = np.zeros(9)
    C0[1] = R_BARE_PLANCK
    C_hubble = expm(M * T_PLANCK_TO_HUBBLE * t_scale) @ C0
    R = float(C_hubble[1])
    beta_eff = math.log(R / R_BARE_PLANCK) / (T_PLANCK_TO_HUBBLE * t_scale) if R > 0 else float("nan")
    return R, beta_eff


def inversion_vary_m11(target_r: float = R_CANONICAL) -> Dict[str, Any]:
    """
    Inversion mode: vary only M11 (Euler diagonal).

    Find M11 such that exp(M*t) acting on Euler initial condition gives R ≈ target_r.
    """
    M_base = build_v5_matrix(lambda_euler=0.92)

    def objective_m11(m11_value):
        M = M_base.copy()
        M[1, 1] = m11_value
        R, _ = evolve_euler_channel(M)
        return (R - target_r) ** 2

    result = minimize_scalar(objective_m11, bounds=(0.05, 0.20), method="bounded")
    m11_optimal = result.x
    R_achieved, beta_achieved = evolve_euler_channel(M_base.copy())
    M_opt = M_base.copy()
    M_opt[1, 1] = m11_optimal
    R_opt, beta_opt = evolve_euler_channel(M_opt)

    return {
        "constraint": "vary_only_m11",
        "m11_required": m11_optimal,
        "m11_structural": M_base[1, 1],
        "delta_m11": m11_optimal - M_base[1, 1],
        "delta_m11_percent": (m11_optimal - M_base[1, 1]) / M_base[1, 1] * 100.0,
        "r_achieved": R_opt,
        "r_target": target_r,
        "error_percent": abs(R_opt - target_r) / target_r * 100.0,
        "beta_eff_achieved": beta_opt,
    }


def inversion_vary_offdiag_scale(target_r: float = R_CANONICAL) -> Dict[str, Any]:
    """
    Inversion mode: vary only off-diagonal scale κ multiplier.

    All off-diagonals are scaled by κ_scale. Find κ_scale such that R ≈ target_r.
    """
    M_base = build_matrix_raw = build_v5_matrix(lambda_euler=0.92)

    def objective_kappa(kappa_scale):
        M = M_base.copy()
        # Re-scale all off-diagonals by the factor kappa_scale (which modifies κ)
        for i in range(9):
            for j in range(9):
                if i != j:
                    # Current off-diagonal = original * κ
                    # We want to rescale it: M[i,j] *= (kappa_scale / κ_current)
                    # But simpler: apply the scale directly
                    # Actually, we need to work from the raw V4 matrix
                    pass
        # For simplicity, rebuild with scaled κ
        from grut.derivation.euler.v4_matrix_resolution import build_matrix
        M_raw = build_matrix(lambda_euler=0.92)
        M = np.diag(np.diag(M_raw))  # Only diagonals
        # Add scaled off-diagonals
        for i in range(9):
            for j in range(9):
                if i != j:
                    M[i, j] = M_raw[i, j] * kappa_scale
        R, _ = evolve_euler_channel(M)
        return (R - target_r) ** 2

    result = minimize_scalar(objective_kappa, bounds=(0.001, 0.1), method="bounded")
    kappa_optimal = result.x

    return {
        "constraint": "vary_only_offdiag_scale",
        "kappa_required": kappa_optimal,
        "kappa_structural": 1.0 / (16.0 * math.pi ** 2),
        "ratio": kappa_optimal / (1.0 / (16.0 * math.pi ** 2)),
        "r_target": target_r,
        "beta_achieved": None,  # Would need recompute
        "interpretation": f"Off-diagonals need to be scaled by {kappa_optimal/((1.0/(16*math.pi**2))):.2f}× relative to loop suppression",
    }


def inversion_vary_rg_time(target_r: float = R_CANONICAL) -> Dict[str, Any]:
    """
    Inversion mode: vary only RG-time scaling.

    Find t_scale such that exp(M * t_scale * T_PLANCK_TO_HUBBLE) gives R ≈ target_r.
    """
    M = build_v5_matrix(lambda_euler=0.92)

    def objective_time(t_scale):
        R, _ = evolve_euler_channel(M, t_scale=t_scale)
        return (R - target_r) ** 2

    result = minimize_scalar(objective_time, bounds=(0.5, 2.0), method="bounded")
    t_scale_optimal = result.x
    R_opt, beta_opt = evolve_euler_channel(M, t_scale=t_scale_optimal)

    return {
        "constraint": "vary_only_rg_time",
        "t_scale_required": t_scale_optimal,
        "t_scale_structural": 1.0,
        "delta_t_scale_percent": (t_scale_optimal - 1.0) / 1.0 * 100.0,
        "t_planck_hubble_scaled": T_PLANCK_TO_HUBBLE * t_scale_optimal,
        "r_achieved": R_opt,
        "r_target": target_r,
        "error_percent": abs(R_opt - target_r) / target_r * 100.0,
        "beta_eff_achieved": beta_opt,
    }


def inversion_vary_euler_row(target_r: float = R_CANONICAL) -> Dict[str, Any]:
    """
    Inversion mode: vary only row/column 1 (Euler).

    Find how much to scale M[1,:] and M[:,1] to hit target R.
    """
    M_base = build_v5_matrix(lambda_euler=0.92)

    def objective_euler_row(scale):
        M = M_base.copy()
        M[1, :] *= scale
        M[:, 1] *= scale
        M[1, 1] /= scale  # Undo double-scaling on diagonal
        R, _ = evolve_euler_channel(M)
        return (R - target_r) ** 2

    result = minimize_scalar(objective_euler_row, bounds=(0.5, 2.0), method="bounded")
    scale_optimal = result.x
    M_opt = M_base.copy()
    M_opt[1, :] *= scale_optimal
    M_opt[:, 1] *= scale_optimal
    M_opt[1, 1] /= scale_optimal
    R_opt, beta_opt = evolve_euler_channel(M_opt)

    return {
        "constraint": "vary_only_euler_row_column",
        "euler_couplings_scale_factor": scale_optimal,
        "r_achieved": R_opt,
        "r_target": target_r,
        "error_percent": abs(R_opt - target_r) / target_r * 100.0,
        "interpretation": f"Euler row/column couplings need to be {scale_optimal:.2f}× their current values",
    }


def run_target_inversion(target_r: float = R_CANONICAL) -> Dict[str, Any]:
    """Run all constrained inversion modes."""
    return {
        "target_r": target_r,
        "mode_vary_m11": inversion_vary_m11(target_r),
        "mode_vary_offdiag_scale": inversion_vary_offdiag_scale(target_r),
        "mode_vary_rg_time": inversion_vary_rg_time(target_r),
        "mode_vary_euler_row": inversion_vary_euler_row(target_r),
    }


def print_inversion_report(r: Dict[str, Any]) -> None:
    print("\n" + "=" * 80)
    print("R TARGET INVERSION (Gate 2b)")
    print(f"Target R = {r['target_r']:.5f}")
    print("=" * 80)

    print(f"\n--- Mode 1: Vary Only M11 (Euler Diagonal) ---")
    m1 = r["mode_vary_m11"]
    print(f"  Required M11        : {m1['m11_required']:.6f}")
    print(f"  Structural M11      : {m1['m11_structural']:.6f}")
    print(f"  Δ                   : {m1['delta_m11']:+.6f} ({m1['delta_m11_percent']:+.2f}%)")
    print(f"  R achieved          : {m1['r_achieved']:.6f} (error: {m1['error_percent']:.3f}%)")
    print(f"  β_eff achieved      : {m1['beta_eff_achieved']:.6f}")

    print(f"\n--- Mode 2: Vary Off-Diagonal Scale Factor ---")
    m2 = r["mode_vary_offdiag_scale"]
    print(f"  {m2['interpretation']}")
    print(f"  κ_structural        : {m2['kappa_structural']:.8f}")
    print(f"  κ_required          : {m2['kappa_required']:.8f}")
    print(f"  Ratio               : {m2['ratio']:.4f}×")

    print(f"\n--- Mode 3: Vary Only RG-Time Scale ---")
    m3 = r["mode_vary_rg_time"]
    print(f"  Required t_scale    : {m3['t_scale_required']:.4f}")
    print(f"  Δ t_scale           : {m3['delta_t_scale_percent']:+.2f}%")
    print(f"  t × T_PLANCK_HUBBLE : {m3['t_planck_hubble_scaled']:.2f}")
    print(f"  R achieved          : {m3['r_achieved']:.6f} (error: {m3['error_percent']:.3f}%)")
    print(f"  β_eff achieved      : {m3['beta_eff_achieved']:.6f}")

    print(f"\n--- Mode 4: Vary Only Euler Row/Column Couplings ---")
    m4 = r["mode_vary_euler_row"]
    print(f"  {m4['interpretation']}")
    print(f"  R achieved          : {m4['r_achieved']:.6f} (error: {m4['error_percent']:.3f}%)")

    print(f"\n--- Summary ---")
    print(f"  If the problem is in M11 alone, it needs to be {m1['m11_required']:.6f}")
    print(f"  If the problem is in loop suppression, κ needs {m2['ratio']:.2f}× enhancement")
    print(f"  If the problem is in RG time, t needs {m3['t_scale_required']:.2f}× scaling")
    print(f"  If the problem is in Euler coupling, it needs {m4['euler_couplings_scale_factor']:.2f}× strength")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    result = run_target_inversion(target_r=R_CANONICAL)
    print_inversion_report(result)
