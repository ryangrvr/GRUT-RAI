"""
V5 Sensitivity Audit (Gate 2).

PURPOSE
-------
The loop-suppressed V5 matrix gives β_eff ≈ 0.1229, but the required target is
0.1215. The question is: which matrix element(s) are responsible for the
overshoot?

This script computes the sensitivity ∂β_eff / ∂M_ij for every diagonal and
off-diagonal entry in the 9×9 matrix, ranks them by absolute sensitivity,
and identifies which entries dominate the flow and cause the overshoot.

APPROACH
--------
Numerical finite-difference sensitivity:
  ∂β_eff / ∂M_ij ≈ [β_eff(M_ij + ε) - β_eff(M_ij - ε)] / (2ε)

For each matrix entry, perturb by ±δ and recompute the RG flow.

RESULT
------
A ranked table of matrix elements by |∂β_eff / ∂M_ij|, showing which elements
have the strongest effect on the final β_eff value. This localizes whether the
overshoot comes from:
  • the Euler diagonal M11 (if dβ/dM11 is largest),
  • off-diagonal loop suppression (if cross-coupling sensitivities dominate),
  • RG-time projection effects (if the issue is not local but flow-geometric),
  • or a combination.
"""
from __future__ import annotations

import math
from typing import Dict, Any

import numpy as np
from scipy.linalg import expm

from grut.derivation.euler.v4_matrix_resolution import (
    build_matrix,
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)
from grut.derivation.euler.v5_loop_suppressed_matrix import (
    build_v5_matrix,
)

# Loop-suppression constant
KAPPA = 1.0 / (16.0 * math.pi ** 2)


def evolve_euler_channel_v5(M: np.ndarray) -> tuple[float, float]:
    """Evolve C₀ = (0, R_bare, 0, …) through exp(M*t); return (R, β_eff)."""
    C0 = np.zeros(9)
    C0[1] = R_BARE_PLANCK
    C_hubble = expm(M * T_PLANCK_TO_HUBBLE) @ C0
    R = float(C_hubble[1])
    beta_eff = math.log(R / R_BARE_PLANCK) / T_PLANCK_TO_HUBBLE if R > 0 else float("nan")
    return R, beta_eff


def compute_sensitivity(lambda_euler: float = 0.92, delta: float = 0.001) -> Dict[str, Any]:
    """
    Compute ∂β_eff / ∂M_ij for all 9×9 matrix entries.

    Parameters
    ----------
    lambda_euler : float
        Λ→Euler coupling.
    delta : float
        Perturbation magnitude for finite-difference.

    Returns
    -------
    Dict with sensitivity for each matrix element and ranked table.
    """
    # Baseline
    M_base = build_v5_matrix(lambda_euler=lambda_euler)
    _, beta_base = evolve_euler_channel_v5(M_base)

    sensitivities = []

    for i in range(9):
        for j in range(9):
            # Perturb +delta
            M_plus = M_base.copy()
            M_plus[i, j] += delta
            _, beta_plus = evolve_euler_channel_v5(M_plus)

            # Perturb -delta
            M_minus = M_base.copy()
            M_minus[i, j] -= delta
            _, beta_minus = evolve_euler_channel_v5(M_minus)

            # Central difference
            d_beta_d_mij = (beta_plus - beta_minus) / (2.0 * delta)

            sensitivities.append({
                "i": i,
                "j": j,
                "M_ij_base": float(M_base[i, j]),
                "d_beta_d_mij": d_beta_d_mij,
                "abs_sensitivity": abs(d_beta_d_mij),
                "type": "diagonal" if i == j else "off-diagonal",
                "label": f"M[{i},{j}]",
            })

    # Sort by absolute sensitivity (largest first)
    sensitivities_sorted = sorted(sensitivities, key=lambda x: x["abs_sensitivity"], reverse=True)

    # Contribution: how much does this element contribute to total overshoot?
    # (rough estimate: sensitivity × current value)
    overshoot = beta_base - 0.1215  # positive = exceeds target
    contributions = []
    for s in sensitivities_sorted[:20]:  # Top 20 entries
        contrib = s["d_beta_d_mij"] * s["M_ij_base"]
        contributions.append({
            "label": s["label"],
            "sensitivity": s["d_beta_d_mij"],
            "base_value": s["M_ij_base"],
            "contribution_to_beta": contrib,
        })

    return {
        "lambda_euler": lambda_euler,
        "beta_base": beta_base,
        "beta_target": 0.1215,
        "overshoot": overshoot,
        "all_sensitivities": sensitivities,
        "sensitivities_sorted_by_magnitude": sensitivities_sorted,
        "top_20_contributions": contributions,
    }


def print_sensitivity_report(r: Dict[str, Any]) -> None:
    print("\n" + "=" * 80)
    print("V5 SENSITIVITY AUDIT (Gate 2)")
    print(f"λ_Euler = {r['lambda_euler']}")
    print("=" * 80)

    print(f"\n--- Baseline ---")
    print(f"  β_eff (V5)     : {r['beta_base']:.6f}")
    print(f"  Target         : {r['beta_target']:.6f}")
    print(f"  Overshoot      : {r['overshoot']:.6f} ({r['overshoot']/r['beta_target']*100:.2f}%)")

    print(f"\n--- Top 20 Matrix Elements by |∂β_eff/∂M_ij| ---")
    print(f"{'Rank':>4} {'Element':>8} {'Type':>12} {'Base Value':>12} {'∂β/∂M_ij':>12}")
    print("-" * 60)
    for idx, s in enumerate(r["sensitivities_sorted_by_magnitude"][:20]):
        print(
            f"{idx+1:4d} {s['label']:>8} {s['type']:>12} "
            f"{s['M_ij_base']:>12.6f} {s['d_beta_d_mij']:>12.6f}"
        )

    print(f"\n--- Contribution Analysis (top 20) ---")
    print(f"  Element    │  Sensitivity  │  Base Value  │  Contribution (Δβ per element)")
    print(f"  ───────────┼───────────────┼──────────────┼─────────────────────────────────")
    total_contribution = 0.0
    for item in r["top_20_contributions"]:
        print(
            f"  {item['label']:>8}   │  {item['sensitivity']:>11.6f}  │  {item['base_value']:>10.6f}  │  {item['contribution_to_beta']:>+.6f}"
        )
        total_contribution += item["contribution_to_beta"]

    print(f"\n--- Diagnostic Interpretation ---")
    top_elem = r["sensitivities_sorted_by_magnitude"][0]
    if top_elem["type"] == "diagonal":
        print(f"  Largest sensitivity is {top_elem['label']} (diagonal, M[{top_elem['i']},{top_elem['j']}]).")
        if top_elem["i"] == 1:
            print(f"  → This is the Euler diagonal M11. The overshoot may be driven by M11 itself.")
        else:
            print(f"  → This is NOT the Euler diagonal. The overshoot is driven by diagonal entry {top_elem['i']}.")
    else:
        print(f"  Largest sensitivity is {top_elem['label']} (off-diagonal).")
        print(f"  → The overshoot is driven by off-diagonal mixing, not diagonal values.")

    # Check if off-diagonals dominate
    diag_sensitivities = [s for s in r["sensitivities_sorted_by_magnitude"] if s["type"] == "diagonal"]
    offdiag_sensitivities = [s for s in r["sensitivities_sorted_by_magnitude"] if s["type"] == "off-diagonal"]

    if diag_sensitivities and offdiag_sensitivities:
        max_diag = diag_sensitivities[0]["abs_sensitivity"]
        max_offdiag = offdiag_sensitivities[0]["abs_sensitivity"]
        if max_offdiag > max_diag * 2:
            print(f"\n  Off-diagonal dominance: largest off-diag sensitivity ({max_offdiag:.6f})")
            print(f"  is > 2× largest diag sensitivity ({max_diag:.6f}).")
            print(f"  → Loop-suppression may be insufficient; check κ = {1.0/(16*math.pi**2):.6f}.")
        elif max_diag > max_offdiag * 2:
            print(f"\n  Diagonal dominance: largest diag sensitivity ({max_diag:.6f})")
            print(f"  is > 2× largest off-diag sensitivity ({max_offdiag:.6f}).")
            print(f"  → Problem is in the diagonal entries (Seeley-DeWitt coefficients).")
        else:
            print(f"\n  Mixed: diag and off-diag sensitivities are comparable.")
            print(f"  → Problem likely spans both diagonal structure and mixing.")

    print("=" * 80 + "\n")


if __name__ == "__main__":
    result = compute_sensitivity(lambda_euler=0.92, delta=0.001)
    print_sensitivity_report(result)
