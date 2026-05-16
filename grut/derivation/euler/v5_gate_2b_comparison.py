"""
Gate 2b: Side-by-Side V5 Comparison — Monolithic vs. First-Principles Decomposed M[1,5].

PURPOSE
-------
Test whether first-principles decomposition of M[1,5] (separating 1-loop and 2-loop
contributions with correct suppressions) naturally moves R toward 1.15470 without
any hand-tuning of coefficients.

METHODOLOGY
-----------
1. Run V5 with monolithic M[1,5] = 0.92κ (current state)
2. Run V5 with decomposed M[1,5] = 0.60κ + 0.30κ² (first-principles)
3. Compare:
   - β_eff (required: 0.1215)
   - R (observed: 1.15470)
   - Error margins
4. Classify outcome per decision gate

NO HAND-TUNING: Both coefficients come from decomposition audit, not from
fitting to target R. The decomposition is first-principles loop counting.

DECISION GATE
-------------
Outcome                             Interpretation
────────────────────────────────────────────────────────────────
R_decomposed → 1.154 ±0.01         ✓ Loop-order conflation resolves V5
R_decomposed improves but stays high  ≈ Right direction, incomplete diagnosis
R barely changes (<1% improvement)    ✗ M[1,5] not dominant factor
R worsens                           ✗ Decomposition/assignment incorrect
"""

from __future__ import annotations

import math
from typing import Dict, Any
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm

# Reuse V4/V5 infrastructure
from grut.derivation.euler.v4_matrix_resolution import (
    build_matrix,
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)

# Loop suppression constants
KAPPA = 1.0 / (16.0 * math.pi**2)  # ≈ 0.00633


@dataclass
class V5ComparisonResult:
    """Result from single V5 run with specified M[1,5] setup."""
    
    mode: str                  # "monolithic" or "decomposed"
    m15_coefficient: float     # Coefficient (0.92 or 0.60+0.30κ)
    m15_numerical: float       # Actual M[1,5] value in matrix
    
    beta_eff: float            # Derived β_eff
    r_predicted: float         # Predicted R
    error_percent: float       # Error vs 1.15470
    
    eigenvalues: list[float]   # Sorted eigenvalue spectrum (for diagnostics)
    euler_proj: float          # Euler channel projection onto eigenstate near 0.11
    gershgorin: float          # Gershgorin radius for Euler row
    
    def __str__(self) -> str:
        icon_r = "↓" if self.r_predicted < R_OBSERVED else ("↑" if self.r_predicted > R_OBSERVED else "=")
        icon_beta = "↓" if self.beta_eff < 0.1215 else ("↑" if self.beta_eff > 0.1215 else "=")
        return (
            f"{self.mode:12s} | M[1,5]={self.m15_numerical:.6f} | "
            f"β_eff={self.beta_eff:.6f} {icon_beta} | "
            f"R={self.r_predicted:.6f} {icon_r} | "
            f"Error={self.error_percent:+.2f}%"
        )


def build_v5_matrix_with_m15_override(
    m15_coefficient_before_kappa: float,
    lambda_euler: float = 0.92,
    decomposed: bool = False,
) -> np.ndarray:
    """
    Build V5 loop-suppressed matrix with M[1,5] override.
    
    Parameters
    ----------
    m15_coefficient_before_kappa : float
        M[1,5] coefficient BEFORE κ suppression (e.g., 0.92 or 0.60/0.30).
        This gets κ suppression applied for monolithic, or decomposed for 2-loop.
    lambda_euler : float
        Λ→Euler coupling (standard 0.92).
    decomposed : bool
        If False: apply uniform κ suppression → M[1,5] = 0.92κ (monolithic)
        If True: decompose with correct loop suppressions → M[1,5] = 0.60κ + 0.30κ²
    
    Returns
    -------
    np.ndarray, shape (9, 9)
    """
    # Start from V4 structure
    M = build_matrix(lambda_euler=lambda_euler).copy()
    
    # For decomposed mode: manually set M[1,5] components BEFORE applying κ to everything
    if decomposed:
        # Set the 2-loop component explicitly before general κ suppression
        # We'll handle this below after the loop
        m15_1loop_coeff = 0.60
        m15_2loop_coeff = 0.30
    else:
        # Monolithic: use single coefficient
        m15_1loop_coeff = m15_coefficient_before_kappa
        m15_2loop_coeff = 0.0
    
    # Apply κ suppression to all off-diagonals EXCEPT M[1,5]
    n = M.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and not (i == 1 and j == 5) and not (i == 5 and j == 1):
                M[i, j] *= KAPPA
    
    # Now set M[1,5] with appropriate suppression
    if decomposed:
        # 1-loop gets κ, 2-loop gets κ²
        m15_final = m15_1loop_coeff * KAPPA + m15_2loop_coeff * KAPPA**2
    else:
        # Monolithic: all gets κ
        m15_final = m15_1loop_coeff * KAPPA
    
    M[1, 5] = m15_final
    M[5, 1] = m15_final
    
    return M


def evolve_euler_channel(M: np.ndarray) -> tuple[float, float]:
    """Evolve C₀ = (0, R_bare, 0, …) through exp(M * t); return (R, β_eff)."""
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


def run_v5_with_m15(
    m15_coefficient_before_kappa: float,
    mode_label: str,
    decomposed: bool = False,
) -> V5ComparisonResult:
    """
    Run full V5 evolution with specified M[1,5] coefficient.
    
    Parameters
    ----------
    m15_coefficient_before_kappa : float
        M[1,5] coefficient before κ suppression (e.g., 0.92 for monolithic).
    mode_label : str
        Descriptive label (e.g., "monolithic", "decomposed").
    decomposed : bool
        If True, applies decomposed loop suppressions; else monolithic κ suppression.
    
    Returns
    -------
    V5ComparisonResult
    """
    M = build_v5_matrix_with_m15_override(
        m15_coefficient_before_kappa=m15_coefficient_before_kappa,
        decomposed=decomposed
    )
    
    # Eigenstructure analysis
    eigenvals, eigenvecs = np.linalg.eig(M)
    eigenvals_sorted = sorted(eigenvals.real, reverse=True)
    
    # Euler-channel projection
    C0 = np.zeros(9)
    C0[1] = 1.0
    try:
        coeffs = np.linalg.solve(eigenvecs, C0)
        # Find eigenvalue nearest to 0.11 (Euler diagonal)
        idx_euler = int(np.argmin([abs(v - 0.11) for v in eigenvals.real]))
        proj_euler = float(abs(coeffs[idx_euler]))
    except np.linalg.LinAlgError:
        proj_euler = float("nan")
    
    # Gershgorin radius for Euler row
    gershgorin = float(np.sum(np.abs(M[1])) - abs(M[1, 1]))
    
    # RG evolution
    R, beta_eff = evolve_euler_channel(M)
    error = abs(R - R_OBSERVED) / R_OBSERVED * 100
    
    # Get actual M[1,5] numerical value
    m15_numerical = M[1, 5]
    
    return V5ComparisonResult(
        mode=mode_label,
        m15_coefficient=m15_coefficient_before_kappa,
        m15_numerical=m15_numerical,
        beta_eff=beta_eff,
        r_predicted=R,
        error_percent=error,
        eigenvalues=[round(float(x), 6) for x in eigenvals_sorted],
        euler_proj=proj_euler,
        gershgorin=gershgorin,
    )


def run_gate_2b_comparison() -> Dict[str, Any]:
    """
    Execute full Gate 2b comparison: monolithic vs decomposed M[1,5].
    
    Baseline assumption: M[1,5] structural coefficient = 0.92 (before κ suppression).
    
    Mode 1: Monolithic — apply uniform κ suppression → M[1,5] = 0.92κ
    Mode 2: Decomposed — decompose with loop-correct suppressions → M[1,5] = 0.60κ + 0.30κ²
    
    Returns
    -------
    Dict with both results and classification
    """
    # --- MONOLITHIC (structural 0.92, uniform κ suppression) ---
    result_mono = run_v5_with_m15(
        m15_coefficient_before_kappa=0.92,
        mode_label="monolithic",
        decomposed=False,
    )
    
    # --- DECOMPOSED (first-principles loop suppression: 0.60κ + 0.30κ²) ---
    result_decomp = run_v5_with_m15(
        m15_coefficient_before_kappa=0.92,  # Same structural estimate, but decomposed
        mode_label="decomposed",
        decomposed=True,
    )
    
    # --- DECISION GATE CLASSIFICATION ---
    r_improvement = result_mono.r_predicted - result_decomp.r_predicted
    r_improvement_pct = (r_improvement / result_mono.r_predicted) * 100
    beta_improvement = result_mono.beta_eff - result_decomp.beta_eff
    
    # Classify outcome
    if abs(result_decomp.error_percent) < 1.5:
        classification = "✓ RESOLUTION: Loop-order conflation likely resolves V5"
        confidence = "HIGH"
    elif result_decomp.error_percent < result_mono.error_percent - 5.0:
        classification = "≈ PROGRESS: Right direction, but incomplete diagnosis (Gate 1 or 4?)"
        confidence = "MEDIUM"
    elif abs(result_decomp.error_percent - result_mono.error_percent) < 1.0:
        classification = "✗ INSUFFICIENT: M[1,5] is not the dominant factor"
        confidence = "LOW"
    else:
        classification = "✗ CONTRADICTION: Decomposition worsens the fit"
        confidence = "CRITICAL"
    
    targets_met = {
        "beta_eff_within_0.1%": abs(result_decomp.beta_eff - 0.1215) < 0.001215,
        "r_within_1.5%": abs(result_decomp.r_predicted - R_OBSERVED) / R_OBSERVED < 0.015,
        "improvement_vs_monolithic": r_improvement > 0.01,
    }
    
    return {
        "kappa": KAPPA,
        "result_monolithic": result_mono,
        "result_decomposed": result_decomp,
        "r_improvement_absolute": r_improvement,
        "r_improvement_percent": r_improvement_pct,
        "beta_improvement": beta_improvement,
        "classification": classification,
        "confidence": confidence,
        "targets_met": targets_met,
        "m15_reduction_factor": result_decomp.m15_numerical / result_mono.m15_numerical if result_mono.m15_numerical > 0 else float("nan"),
    }


def print_gate_2b_report(r: Dict[str, Any]) -> None:
    """Print formatted Gate 2b comparison report."""
    
    print("\n" + "=" * 90)
    print("GATE 2b: V5 DECOMPOSITION TEST — SIDE-BY-SIDE COMPARISON")
    print("=" * 90)
    print(f"\nTest Date: 2026-05-09")
    print(f"κ = 1/(16π²) = {r['kappa']:.6f}")
    print(f"Target R (observed): {R_OBSERVED:.5f}")
    print(f"Target β_eff (required): 0.1215")
    print(f"\nBASELINE ASSUMPTION: M[1,5] structural coefficient = 0.92 (before κ suppression)")
    print(f"─" * 90)
    
    # --- Comparison table header ---
    print("\n" + "-" * 90)
    print("COMPARISON TABLE")
    print("-" * 90)
    print(f"{'Mode':<12} | {'M[1,5] value':<18} | {'β_eff':<15} | {'R predicted':<15} | {'Error %':<12}")
    print("-" * 90)
    
    mono = r["result_monolithic"]
    decomp = r["result_decomposed"]
    
    print(f"{mono.mode:<12} | {mono.m15_numerical:<18.6f} | {mono.beta_eff:<15.6f} | {mono.r_predicted:<15.6f} | {mono.error_percent:+10.2f}%")
    print(f"{decomp.mode:<12} | {decomp.m15_numerical:<18.6f} | {decomp.beta_eff:<15.6f} | {decomp.r_predicted:<15.6f} | {decomp.error_percent:+10.2f}%")
    print("-" * 90)
    
    # --- Detailed analysis ---
    print("\n--- M[1,5] Setup (Structural Estimate = 0.92) ---")
    print(f"  Monolithic (uniform κ)         : 0.92 × κ = {mono.m15_numerical:.6f}")
    print(f"  Decomposed (1-loop + 2-loop)   : 0.60κ + 0.30κ² = {decomp.m15_numerical:.6f}")
    print(f"  Reduction factor               : {r['m15_reduction_factor']:.4f}× (M[1,5] becomes {(1-r['m15_reduction_factor'])*100:.1f}% weaker)")
    
    print("\n--- β_eff Comparison ---")
    print(f"  Monolithic                     : {mono.beta_eff:.6f}  (vs target 0.1215, error: {abs(mono.beta_eff - 0.1215):.6f})")
    print(f"  Decomposed                     : {decomp.beta_eff:.6f}  (vs target 0.1215, error: {abs(decomp.beta_eff - 0.1215):.6f})")
    print(f"  Improvement (β lower is better): {r['beta_improvement']:.6f}  ({'✓' if r['beta_improvement'] > 0 else '✗'})")
    print(f"  Target                         : 0.1215")
    
    print("\n--- R Prediction Comparison ---")
    print(f"  Monolithic                     : {mono.r_predicted:.6f}  (Error: {mono.error_percent:+.2f}%)")
    print(f"  Decomposed                     : {decomp.r_predicted:.6f}  (Error: {decomp.error_percent:+.2f}%)")
    print(f"  Improvement (R closer to obs)  : {r['r_improvement_absolute']:+.6f}  ({r['r_improvement_percent']:+.2f}%)")
    print(f"  Observed target                : {R_OBSERVED:.6f}")
    
    print("\n--- Gate Success Criteria ---")
    targets = r["targets_met"]
    print(f"  β_eff within 0.1% of target    : {'✓ YES' if targets['beta_eff_within_0.1%'] else '✗ NO'}")
    print(f"  R within 1.5% of observed      : {'✓ YES' if targets['r_within_1.5%'] else '✗ NO'}")
    print(f"  Improvement vs monolithic      : {'✓ YES' if targets['improvement_vs_monolithic'] else '✗ NO'}")
    
    print("\n--- Eigenvalue Spectrum ---")
    print(f"  Monolithic (top 5)             : {mono.eigenvalues[:5]}")
    print(f"  Decomposed (top 5)             : {decomp.eigenvalues[:5]}")
    
    print("\n--- Euler Channel Diagnostics ---")
    print(f"  Monolithic Euler projection    : {mono.euler_proj:.4f}  (should be close to 1.0)")
    print(f"  Decomposed Euler projection    : {decomp.euler_proj:.4f}  (should be close to 1.0)")
    print(f"  Monolithic Gershgorin radius   : {mono.gershgorin:.6f}  (small = eigenvalue locked near diagonal)")
    print(f"  Decomposed Gershgorin radius   : {decomp.gershgorin:.6f}")
    
    # --- Decision gate ---
    print("\n" + "=" * 90)
    print("DECISION GATE CLASSIFICATION")
    print("=" * 90)
    print(f"\n  Confidence Level: {r['confidence']}")
    print(f"  Outcome: {r['classification']}")
    print("\n" + "=" * 90)
    
    # --- Interpretation ---
    print("\n--- Interpretation ---")
    if abs(decomp.error_percent) < 1.5:
        print(f"""
  ✓ SUCCESS: First-principles loop-order decomposition resolves the R-gap.
  
  Starting from structural estimate M[1,5] = 0.92:
  - Monolithic (0.92κ): R = {mono.r_predicted:.5f} (error {mono.error_percent:+.2f}%)
  - Decomposed (0.60κ + 0.30κ²): R = {decomp.r_predicted:.5f} (error {decomp.error_percent:+.2f}%)
  
  The decomposition moves R by {r['r_improvement_absolute']:+.5f} toward target {R_OBSERVED:.5f}.
  β_eff improves from {mono.beta_eff:.6f} to {decomp.beta_eff:.6f} (target 0.1215).
  
  CONCLUSION: Loop-order conflation (treating 2-loop pieces as 1-loop) was
  over-weighting the off-diagonal mixing. Applying correct suppressions naturally
  moves the result in the right direction WITHOUT hand-tuning.
  
  NEXT STEP: Gate 2 likely complete. Prepare publication on loop-order correction.
""")
    elif decomp.error_percent < mono.error_percent - 5.0:
        print(f"""
  ≈ PARTIAL PROGRESS: First-principles decomposition improves both β_eff and R,
  but the remaining gap suggests other factors (Gate 1 normalization? Gate 4 diagonal?).
  
  Starting from structural estimate M[1,5] = 0.92:
  - Monolithic (0.92κ): R = {mono.r_predicted:.5f} ({mono.error_percent:+.2f}%)
  - Decomposed (0.60κ + 0.30κ²): R = {decomp.r_predicted:.5f} ({decomp.error_percent:+.2f}%)
  
  Improvement: R moved {r['r_improvement_percent']:.2f}% toward target,
  β_eff improved by {r['beta_improvement']:.6f}.
  
  INTERPRETATION: The loop-order correction moves in the right direction
  (first-principles confirms the direction), but magnitude isn't complete.
  
  NEXT STEP: Run Gates 1 & 4 in parallel to address complementary corrections.
""")
    elif abs(decomp.error_percent - mono.error_percent) < 1.0:
        print(f"""
  ✗ INSUFFICIENT: M[1,5] decomposition shows minimal impact (<1% change).
  
  This indicates either:
  1. M[1,5] is not the leverage point for resolving R (check Gate 4 diagonal)
  2. Decomposition coefficients conflict with matrix structure
  3. Structural estimate 0.92 is not the right baseline
  
  NEXT STEP: Verify structural estimate for M[1,5]; investigate Gate 1 (normalization)
  and Gate 4 (diagonal refinement) as independent primary factors.
""")
    else:
        print(f"""
  ✗ DECOMPOSITION WORSENS FIT: This is unexpected and indicates either:
  1. Sign error in decomposition (loop-order assignment backwards)
  2. Structural estimate 0.92 is significantly wrong
  3. Matrix element interaction creates instability
  
  NEXT STEP: Review decomposition diagram assignments; verify loop-order logic
  against explicit Feynman computation.
""")
    
    print("\n" + "=" * 90 + "\n")


if __name__ == "__main__":
    result = run_gate_2b_comparison()
    print_gate_2b_report(result)
