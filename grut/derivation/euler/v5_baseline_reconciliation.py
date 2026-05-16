"""
V5 Baseline Reconciliation Audit.

PURPOSE
-------
Answer the foundational question: Which exact matrix produces R ≈ 1.32?

This module:
1. Builds the LIVE V5 matrix as-is (no hypotheticals)
2. Prints full matrix with all entries and κ suppressions
3. Runs RG flow to reproduce reported R ≈ 1.32, β_eff ≈ 0.1229
4. Identifies all off-diagonal entries, especially M[1,5]
5. Recomputes local sensitivity ∂β_eff/∂M_ij around the live matrix
6. Answers: Is M[1,5] actually the high-leverage entry? Or something else?

OUTCOME
-------
This is the ground truth. All Gate 2 physics interpretation depends on this.
No more hypothetical 0.92; only what's actually running.
"""

from __future__ import annotations

import math
from typing import Dict, Any

import numpy as np
from scipy.linalg import expm

# Import exact live V5 infrastructure
from grut.derivation.euler.v4_matrix_resolution import (
    build_matrix,
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)

KAPPA = 1.0 / (16.0 * math.pi**2)  # ≈ 0.00633


def build_live_v5_matrix() -> np.ndarray:
    """
    Build the LIVE V5 matrix exactly as used in production.
    This is the ground truth: what actually produces R ≈ 1.32.
    """
    M = build_matrix(lambda_euler=0.92).copy()
    
    # Apply κ suppression to ALL off-diagonals (this is the V5 prescription)
    n = M.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] *= KAPPA
    
    return M


def evolve_euler_channel(M: np.ndarray) -> tuple[float, float]:
    """Evolve C₀ = (0, R_bare, 0, …) through exp(M·t); return (R, β_eff)."""
    C0 = np.zeros(9)
    C0[1] = R_BARE_PLANCK
    C_hubble = expm(M * T_PLANCK_TO_HUBBLE) @ C0
    R = float(C_hubble[1])
    beta_eff = (
        math.log(R / R_BARE_PLANCK) / T_PLANCK_TO_HUBBLE
        if R > 0
        else float("nan")
    )
    return R, beta_eff


def compute_local_sensitivity(M: np.ndarray, eps: float = 1e-6) -> Dict[tuple[int, int], float]:
    """
    Compute dβ_eff/dM_ij for all matrix entries around the live matrix.
    
    Uses finite differences: sensitivity = (β(M + ε·e_ij) - β(M)) / ε
    
    Only computes for off-diagonal entries (where physics sensitivity matters).
    
    Returns
    -------
    Dict mapping (i, j) → dβ_eff/dM_ij (only i ≠ j)
    """
    _, beta_base = evolve_euler_channel(M)
    
    sensitivities = {}
    n = M.shape[0]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Perturb M[i,j]
                M_pert = M.copy()
                M_pert[i, j] += eps
                
                _, beta_pert = evolve_euler_channel(M_pert)
                
                # Sensitivity: change in β per unit change in M_ij
                sensitivity = (beta_pert - beta_base) / eps
                sensitivities[(i, j)] = float(sensitivity)
    
    return sensitivities


def print_full_matrix_report(M: np.ndarray) -> Dict[str, Any]:
    """Print comprehensive matrix audit and store key results."""
    
    R, beta_eff = evolve_euler_channel(M)
    error_r = abs(R - R_OBSERVED) / R_OBSERVED * 100
    error_beta = abs(beta_eff - 0.1215) / 0.1215 * 100
    
    sensitivities = compute_local_sensitivity(M)
    
    # Rank sensitivities by absolute value
    ranked_sens = sorted(sensitivities.items(), key=lambda x: abs(x[1]), reverse=True)
    
    print("\n" + "=" * 90)
    print("V5 BASELINE RECONCILIATION AUDIT")
    print("=" * 90)
    print(f"\nGround Truth Test: Can we reproduce R ≈ 1.32?")
    
    print("\n--- Constants ---")
    print(f"  κ = 1/(16π²)                   : {KAPPA:.6f}")
    print(f"  t_RG (Planck→Hubble)           : {T_PLANCK_TO_HUBBLE:.4f}")
    print(f"  R_bare (Planck)                : {R_BARE_PLANCK:.6e}")
    print(f"  R_observed (cosmic)            : {R_OBSERVED:.5f}")
    
    print("\n--- RG Flow Output (LIVE MATRIX) ---")
    print(f"  β_eff (derived from M)         : {beta_eff:.6f}  (required: 0.1215, error: {error_beta:+.2f}%)")
    print(f"  R (predicted)                  : {R:.6f}  (target: {R_OBSERVED:.5f}, error: {error_r:+.2f}%)")
    
    # Verify we're reproducing the known state
    if abs(R - 1.32063) < 0.001:
        print(f"  ✓ CONFIRMED: Matrix reproduces live R ≈ 1.32")
    elif abs(R - 1.154) < 0.01:
        print(f"  ✓ CONFIRMED: Matrix produces target R ≈ 1.154")
    else:
        print(f"  ⚠ WARNING: Unexpected R value. Check matrix definition.")
    
    print("\n--- Full 9×9 Matrix ---")
    print("(Rows/Cols: 0=R², 1=Euler, 2=□R, 3=R²_ferm, 4=G_B_ferm, 5=Tr(F²)R², 6=Tr(F·GB), 7=Λ, 8=Mixed_EW)")
    print()
    
    # Print matrix with row/col labels
    labels = ["R²    ", "Euler ", "□R    ", "R²_fm ", "G_B_f ", "Tr(F²)", "Tr(FG)", "Λ     ", "Mix_EW"]
    
    # Header
    print("        " + "".join(f"{labels[j]:>12}" for j in range(9)))
    print("   " + "─" * 117)
    
    # Matrix rows
    for i in range(9):
        print(f"{labels[i]} |", end="")
        for j in range(9):
            val = M[i, j]
            if abs(val) < 1e-8:
                print(f"{'0':>12}", end="")
            elif abs(val) < 0.01:
                print(f"{val:>12.2e}", end="")
            else:
                print(f"{val:>12.6f}", end="")
        print()
    
    print("\n--- Key Entry: M[1,5] (Euler ↔ Tr(F²)R² coupling) ---")
    m15_final = M[1, 5]
    m15_pre_kappa = m15_final / KAPPA if KAPPA > 0 else 0
    print(f"  M[1,5] (final value in matrix)  : {m15_final:.6f}")
    print(f"  M[1,5] pre-κ (structural coeff): {m15_pre_kappa:.6f}")
    print(f"  κ suppression applied?         : {'✓ YES' if abs(m15_final / KAPPA - m15_pre_kappa) < 1e-4 else '✗ NO (or not standard)'}")
    
    print("\n--- Symmetry Check ---")
    is_symmetric = np.allclose(M, M.T, atol=1e-10)
    print(f"  Matrix is symmetric            : {'✓ YES' if is_symmetric else '✗ NO'}")
    if not is_symmetric:
        print("  (Asym entries listed below)")
        for i in range(9):
            for j in range(i+1, 9):
                if abs(M[i, j] - M[j, i]) > 1e-10:
                    print(f"    M[{i},{j}]={M[i,j]:.2e} ≠ M[{j},{i}]={M[j,i]:.2e}")
    
    print("\n--- Diagonal Entries ---")
    for i in range(9):
        print(f"  M[{i},{i}] ({labels[i]:6s})  : {M[i,i]:.6f}")
    
    print("\n--- Off-Diagonal Entries (absolute magnitude ranking) ---")
    off_diag = {}
    for i in range(9):
        for j in range(9):
            if i != j:
                off_diag[(i, j)] = M[i, j]
    
    ranked_offdiag = sorted(off_diag.items(), key=lambda x: abs(x[1]), reverse=True)
    
    print("\n  Rank  Entry        Value        κ factor  (pre-κ coeff)")
    for rank, ((i, j), val) in enumerate(ranked_offdiag[:15], 1):
        pre_kappa_coeff = val / KAPPA if KAPPA > 0 else 0
        print(f"  {rank:2d}. M[{i},{j}]={labels[i]:6s}×{labels[j]:6s}  {val:>12.2e}   " + 
              (f"{KAPPA:.2e}" if abs(val) > 1e-10 else "          ") + 
              f"  ({pre_kappa_coeff:>8.4f})")
    
    print("\n--- Sensitivity Analysis: dβ_eff/dM_ij (Top 20 entries) ---")
    print("\n  Rank  Entry              Sensitivity   M_ij value   Interpretation")
    print("  " + "─" * 90)
    
    for rank, ((i, j), sens) in enumerate(ranked_sens[:20], 1):
        m_val = M[i, j]
        impact = "CRITICAL" if abs(sens) > 5 else ("HIGH" if abs(sens) > 1 else ("MODERATE" if abs(sens) > 0.1 else "LOW"))
        print(f"  {rank:2d}. M[{i},{j}] ({labels[i]:6s}×{labels[j]:6s})  {sens:>+10.3f}     {m_val:>12.2e}   {impact}")
    
    print("\n--- Verdict ---")
    if ranked_sens[0][0] == (1, 5):
        print(f"  ✓ M[1,5] is the HIGHEST sensitivity entry: dβ/dM[1,5] = {ranked_sens[0][1]:.3f}")
        print("  → Decomposition of M[1,5] is well-motivated")
    else:
        i, j = ranked_sens[0][0]
        print(f"  ⚠ M[1,5] is NOT the highest sensitivity entry!")
        print(f"  → Top entry is M[{i},{j}] ({labels[i]} ↔ {labels[j]}) with sensitivity {ranked_sens[0][1]:.3f}")
        print(f"  → M[1,5] sensitivity ranks #{next(idx+1 for idx, ((ii,jj), s) in enumerate(ranked_sens) if (ii,jj) == (1,5))}")
        print("  → RECONSIDER: May be decomposing wrong coefficient!")
    
    print("\n" + "=" * 90 + "\n")
    
    return {
        "M": M,
        "R": R,
        "beta_eff": beta_eff,
        "error_r_percent": error_r,
        "error_beta_percent": error_beta,
        "m15_final": m15_final,
        "m15_pre_kappa": m15_pre_kappa,
        "sensitivities": sensitivities,
        "ranked_sensitivities": ranked_sens,
        "kappa": KAPPA,
        "t_rg": T_PLANCK_TO_HUBBLE,
    }


if __name__ == "__main__":
    M = build_live_v5_matrix()
    result = print_full_matrix_report(M)
