"""
Gate 2b CORRECTED: V5 Decomposition Test with Live Baseline.

PURPOSE
-------
After baseline reconciliation, we know:
- Live V5 uses M[1,5] = 0.08κ (not 0.92κ as referenced in audit)
- M[1,5] IS the highest-leverage entry (sensitivity = 8.066)
- Decomposition target is correct, but baseline was wrong

This corrected Gate 2b answers: If we decompose the ACTUAL M[1,5] = 0.08κ
with first-principles loop suppressions, does it help resolve R?

METHODOLOGY
-----------
Assume the audit's percentage split applies proportionally:
- Audit found: 0.60κ (1-loop) + 0.30κ² (2-loop) from a 0.92 baseline
- This is 65% 1-loop (0.60/0.92) and 35% 2-loop (0.30/0.92)
- Apply same percentages to live baseline 0.08:
  * 1-loop: 0.08 × 0.65 ≈ 0.052
  * 2-loop: 0.08 × 0.35 ≈ 0.028
- With correct suppressions: 0.052κ + 0.028κ²

IMPORTANT: This is a theoretical decomposition. The audit estimates may not
apply directly to the smaller 0.08 baseline. But this shows the principle:
"If M[1,5] actually decomposes with correct loop orders, does it help?"
"""

from __future__ import annotations

import math
from typing import Dict, Any
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm

from grut.derivation.euler.v4_matrix_resolution import (
    build_matrix,
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)

KAPPA = 1.0 / (16.0 * math.pi**2)


@dataclass
class V5CorrectedResult:
    """Result from corrected Gate 2b test."""
    
    mode: str                  # "baseline" or "decomposed"
    m15_final: float          # Actual M[1,5] in matrix
    m15_pre_kappa: float      # Pre-κ coefficient
    
    beta_eff: float
    r_predicted: float
    error_percent: float
    
    eigenvalues: list[float]
    sensitivity_m15: float
    
    def __str__(self) -> str:
        return (
            f"{self.mode:12s} | M[1,5]={self.m15_final:.6f} | "
            f"β_eff={self.beta_eff:.6f} | R={self.r_predicted:.6f} | "
            f"Error={self.error_percent:+.2f}%"
        )


def build_v5_with_m15_override(
    m15_final: float,
    lambda_euler: float = 0.92,
) -> np.ndarray:
    """
    Build V5 matrix with explicit M[1,5] override.
    
    All other entries remain at their live values.
    """
    M = build_matrix(lambda_euler=lambda_euler).copy()
    
    # Apply κ suppression to all off-diagonals EXCEPT M[1,5]
    n = M.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and not (i == 1 and j == 5) and not (i == 5 and j == 1):
                M[i, j] *= KAPPA
    
    # Set M[1,5] to exact override value
    M[1, 5] = m15_final
    M[5, 1] = m15_final
    
    return M


def evolve_euler_channel(M: np.ndarray) -> tuple[float, float]:
    """Evolve C₀ and return (R, β_eff)."""
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


def compute_m15_sensitivity(M: np.ndarray, eps: float = 1e-6) -> float:
    """Compute dβ_eff/dM[1,5] via finite differences."""
    _, beta_base = evolve_euler_channel(M)
    
    M_pert = M.copy()
    M_pert[1, 5] += eps
    M_pert[5, 1] += eps
    
    _, beta_pert = evolve_euler_channel(M_pert)
    return (beta_pert - beta_base) / eps


def run_corrected_gate_2b() -> Dict[str, Any]:
    """
    Execute corrected Gate 2b: decompose M[1,5] from 0.08κ with loop-correct suppressions.
    
    Baseline (mode="baseline"): M[1,5] = 0.08κ (current live state)
    Decomposed (mode="decomposed"): M[1,5] = 0.052κ + 0.028κ² (proportional decomposition)
    """
    
    # --- BASELINE (current live M[1,5] = 0.08κ) ---
    m15_baseline = 0.08 * KAPPA
    M_baseline = build_v5_with_m15_override(m15_final=m15_baseline)
    
    eigenvals_base, _ = np.linalg.eig(M_baseline)
    eigenvals_base_sorted = sorted(eigenvals_base.real, reverse=True)
    
    R_base, beta_base = evolve_euler_channel(M_baseline)
    error_base = abs(R_base - R_OBSERVED) / R_OBSERVED * 100
    sens_base = compute_m15_sensitivity(M_baseline)
    
    result_baseline = V5CorrectedResult(
        mode="baseline (0.08κ)",
        m15_final=m15_baseline,
        m15_pre_kappa=0.08,
        beta_eff=beta_base,
        r_predicted=R_base,
        error_percent=error_base,
        eigenvalues=[round(float(x), 6) for x in eigenvals_base_sorted],
        sensitivity_m15=sens_base,
    )
    
    # --- DECOMPOSED (first-principles loop suppressions on 0.08 baseline) ---
    # Proportional to audit: 65% 1-loop, 35% 2-loop
    m15_1loop_coeff = 0.08 * 0.65  # ≈ 0.052
    m15_2loop_coeff = 0.08 * 0.35  # ≈ 0.028
    m15_decomposed = m15_1loop_coeff * KAPPA + m15_2loop_coeff * KAPPA**2
    
    M_decomp = build_v5_with_m15_override(m15_final=m15_decomposed)
    
    eigenvals_decomp, _ = np.linalg.eig(M_decomp)
    eigenvals_decomp_sorted = sorted(eigenvals_decomp.real, reverse=True)
    
    R_decomp, beta_decomp = evolve_euler_channel(M_decomp)
    error_decomp = abs(R_decomp - R_OBSERVED) / R_OBSERVED * 100
    sens_decomp = compute_m15_sensitivity(M_decomp)
    
    result_decomp = V5CorrectedResult(
        mode="decomposed (0.052κ+0.028κ²)",
        m15_final=m15_decomposed,
        m15_pre_kappa=0.08,  # Still based on 0.08 structural estimate
        beta_eff=beta_decomp,
        r_predicted=R_decomp,
        error_percent=error_decomp,
        eigenvalues=[round(float(x), 6) for x in eigenvals_decomp_sorted],
        sensitivity_m15=sens_decomp,
    )
    
    # --- DECISION GATE ---
    r_improvement = R_base - R_decomp
    r_improvement_pct = (r_improvement / R_base) * 100 if R_base != 0 else 0
    beta_improvement = beta_base - beta_decomp
    
    # Classification
    if abs(result_decomp.error_percent) < 2.0:
        classification = "✓ SIGNIFICANT: Decomposition moves R toward target"
        confidence = "HIGH"
    elif result_decomp.error_percent < result_baseline.error_percent - 1.0:
        classification = "≈ MINOR: Decomposition improves slightly, but incomplete"
        confidence = "MEDIUM"
    elif abs(result_decomp.error_percent - result_baseline.error_percent) < 0.5:
        classification = "✗ NEGLIGIBLE: Decomposition has minimal impact"
        confidence = "LOW"
    else:
        classification = "✗ WRONG: Decomposition worsens the fit"
        confidence = "CRITICAL"
    
    return {
        "kappa": KAPPA,
        "result_baseline": result_baseline,
        "result_decomposed": result_decomp,
        "r_improvement_absolute": r_improvement,
        "r_improvement_percent": r_improvement_pct,
        "beta_improvement": beta_improvement,
        "classification": classification,
        "confidence": confidence,
        "m15_reduction_factor": m15_decomposed / m15_baseline if m15_baseline > 0 else float("nan"),
        "note": "Decomposition coefficients are PROPORTIONAL ESTIMATES based on audit. Not independently verified.",
    }


def print_corrected_report(r: Dict[str, Any]) -> None:
    """Print corrected Gate 2b report."""
    
    print("\n" + "=" * 90)
    print("GATE 2b CORRECTED: V5 DECOMPOSITION WITH LIVE BASELINE")
    print("=" * 90)
    print(f"\nTest Date: 2026-05-09")
    print(f"κ = 1/(16π²) = {r['kappa']:.6f}")
    print(f"Target R (observed): {R_OBSERVED:.5f}")
    print(f"Target β_eff (required): 0.1215")
    print(f"\nBASELINE CORRECTION: M[1,5] in live matrix is 0.08κ (NOT 0.92κ)")
    print(f"Audit's 0.92 referred to M[1,7] (Euler-Lambda), not M[1,5]")
    print(f"─" * 90)
    
    print("\n" + "-" * 90)
    print("COMPARISON TABLE")
    print("-" * 90)
    print(f"{'Mode':<25} | {'M[1,5]':<18} | {'β_eff':<12} | {'R':<10} | {'Error %':<10}")
    print("-" * 90)
    
    base = r["result_baseline"]
    decomp = r["result_decomposed"]
    
    print(f"{base.mode:<25} | {base.m15_final:<18.6f} | {base.beta_eff:<12.6f} | {base.r_predicted:<10.6f} | {base.error_percent:>+8.2f}%")
    print(f"{decomp.mode:<25} | {decomp.m15_final:<18.6f} | {decomp.beta_eff:<12.6f} | {decomp.r_predicted:<10.6f} | {decomp.error_percent:>+8.2f}%")
    print("-" * 90)
    
    print("\n--- M[1,5] Setup (Live Baseline = 0.08κ) ---")
    print(f"  Baseline (current)             : 0.08κ = {base.m15_final:.6f}")
    print(f"  Decomposed (first-principles)  : 0.052κ + 0.028κ² = {decomp.m15_final:.6f}")
    print(f"  Reduction factor               : {r['m15_reduction_factor']:.4f}× (M[1,5] becomes {(1-r['m15_reduction_factor'])*100:.1f}% weaker)")
    
    print("\n--- β_eff Comparison ---")
    print(f"  Baseline                       : {base.beta_eff:.6f}  (vs target 0.1215, error: {abs(base.beta_eff - 0.1215):+.6f})")
    print(f"  Decomposed                     : {decomp.beta_eff:.6f}  (vs target 0.1215, error: {abs(decomp.beta_eff - 0.1215):+.6f})")
    print(f"  Improvement (smaller is better): {r['beta_improvement']:+.6f}")
    
    print("\n--- R Prediction Comparison ---")
    print(f"  Baseline                       : {base.r_predicted:.6f}  (Error: {base.error_percent:+.2f}%)")
    print(f"  Decomposed                     : {decomp.r_predicted:.6f}  (Error: {decomp.error_percent:+.2f}%)")
    print(f"  Improvement (R closer to obs)  : {r['r_improvement_absolute']:+.6f}  ({r['r_improvement_percent']:+.2f}%)")
    print(f"  Observed target                : {R_OBSERVED:.6f}")
    
    print("\n--- Sensitivity at Both States ---")
    print(f"  Baseline dβ/dM[1,5]            : {base.sensitivity_m15:.4f}  (CRITICAL)")
    print(f"  Decomposed dβ/dM[1,5]          : {decomp.sensitivity_m15:.4f}")
    
    print("\n--- Top 5 Eigenvalues ---")
    print(f"  Baseline                       : {base.eigenvalues[:5]}")
    print(f"  Decomposed                     : {decomp.eigenvalues[:5]}")
    
    # Decision gate
    print("\n" + "=" * 90)
    print("DECISION GATE CLASSIFICATION")
    print("=" * 90)
    print(f"\n  Confidence: {r['confidence']}")
    print(f"  Outcome: {r['classification']}")
    print("\n" + "=" * 90)
    
    # Interpretation
    print("\n--- Interpretation ---")
    if "SIGNIFICANT" in r["classification"]:
        print(f"""
  ✓ Loop-order decomposition of live M[1,5] produces meaningful R shift.
  
  Live baseline (0.08κ) produces R = {base.r_predicted:.5f} ({base.error_percent:+.2f}%)
  Decomposed (0.052κ + 0.028κ²) produces R = {decomp.r_predicted:.5f} ({decomp.error_percent:+.2f}%)
  
  Decomposition reduces M[1,5] by {(1-r['m15_reduction_factor'])*100:.1f}%, moving R closer to target.
  
  This suggests: Loop-order conflation is contributing to the live overshoot.
  
  NEXT STEP: Verify decomposition coefficients independently via Feynman diagrams.
""")
    elif "MINOR" in r["classification"]:
        print(f"""
  ≈ Decomposition shows slight improvement, but magnitude is small.
  
  Live baseline (0.08κ) produces R = {base.r_predicted:.5f} ({base.error_percent:+.2f}%)
  Decomposed (0.052κ + 0.028κ²) produces R = {decomp.r_predicted:.5f} ({decomp.error_percent:+.2f}%)
  
  Improvement: {r['r_improvement_percent']:+.2f}% (subtle).
  
  This suggests: M[1,5] contributes to the problem, but other entries may be more important.
  
  NEXT STEP: Re-examine full sensitivity ranking; other entries may deserve attention first.
""")
    elif "NEGLIGIBLE" in r["classification"]:
        print(f"""
  ✗ Decomposition has negligible impact on R.
  
  This suggests: Either (a) decomposition coefficients are wrong for 0.08κ baseline,
  or (b) M[1,5] is not actually responsible for the current overshoot.
  
  NEXT STEP: Investigate other high-sensitivity entries (M[1,6], M[1,3], etc.).
""")
    else:
        print(f"""
  ✗ Decomposition worsens the fit.
  
  This indicates a fundamental error in decomposition direction or coefficient estimates.
  
  NEXT STEP: Re-examine loop-order assignment and verify against Feynman diagrams.
""")
    
    print(f"\n⚠ NOTE: {r['note']}")
    print("\n" + "=" * 90 + "\n")


if __name__ == "__main__":
    result = run_corrected_gate_2b()
    print_corrected_report(result)
