"""
M[1,5] Required Coefficient Scan.

PURPOSE
-------
Diagnostic sweep: What M[1,5] coefficient is required to achieve target R values?

This is NOT a fit or a derived result. It is a diagnostic target that
identifies what first-principles diagram decomposition must achieve.

The live V5 baseline uses M[1,5] = 0.08κ and produces R ≈ 1.32 (14% error).
We need to identify the coefficient x such that M[1,5] = x*κ produces R ≈ 1.154.

This script scans M[1,5] = x*κ over a dense range and locates the required x value.

IMPORTANT
---------
- This is a diagnostic tool, not a physics derivation.
- The next step is deriving x from explicit Euler↔gauge diagrams.
- Do not promote this coefficient as "derived from first principles."
- Use language: "coefficient required by RG flow to hit target R"
"""

from __future__ import annotations

import math
from typing import Dict, Any, Tuple

import numpy as np
from scipy.linalg import expm
from scipy.interpolate import interp1d

# Import live V5 infrastructure
from grut.derivation.euler.v4_matrix_resolution import (
    build_matrix,
    R_BARE_PLANCK,
    R_OBSERVED,
    T_PLANCK_TO_HUBBLE,
)

KAPPA = 1.0 / (16.0 * math.pi**2)

# Target R values
R_TARGET_TREE = math.sqrt(4.0 / 3.0)  # ≈ 1.154700538
R_TARGET_LOOP = 1.15428


def build_v5_with_m15_coefficient(
    m15_coefficient: float,
    lambda_euler: float = 0.92,
) -> np.ndarray:
    """
    Build V5 matrix with M[1,5] = m15_coefficient * κ.
    
    All other entries remain at their live values.
    All diagonals unchanged.
    All other off-diagonals get standard κ suppression.
    """
    M = build_matrix(lambda_euler=lambda_euler).copy()
    
    # Apply κ suppression to all off-diagonals EXCEPT M[1,5]
    n = M.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and not (i == 1 and j == 5) and not (i == 5 and j == 1):
                M[i, j] *= KAPPA
    
    # Set M[1,5] to specified coefficient
    m15_value = m15_coefficient * KAPPA
    M[1, 5] = m15_value
    M[5, 1] = m15_value
    
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


def scan_m15_coefficient(
    x_min: float = 0.045,
    x_max: float = 0.085,
    num_points: int = 100,
) -> Dict[str, Any]:
    """
    Scan M[1,5] = x*κ over range [x_min, x_max].
    
    Returns dictionary with results and diagnostic targets.
    """
    
    # Dense sweep
    x_values = np.linspace(x_min, x_max, num_points)
    results = {
        "x_coefficients": [],
        "m15_values": [],
        "r_values": [],
        "beta_eff_values": [],
        "r_error_tree": [],  # error vs R_tree
        "r_error_loop": [],  # error vs R_loop
        "beta_error": [],    # error vs 0.1215
    }
    
    for x in x_values:
        M = build_v5_with_m15_coefficient(m15_coefficient=x)
        R, beta_eff = evolve_euler_channel(M)
        
        m15_value = x * KAPPA
        error_tree = abs(R - R_TARGET_TREE) / R_TARGET_TREE * 100
        error_loop = abs(R - R_TARGET_LOOP) / R_TARGET_LOOP * 100
        error_beta = abs(beta_eff - 0.1215) / 0.1215 * 100
        
        results["x_coefficients"].append(x)
        results["m15_values"].append(m15_value)
        results["r_values"].append(R)
        results["beta_eff_values"].append(beta_eff)
        results["r_error_tree"].append(error_tree)
        results["r_error_loop"].append(error_loop)
        results["beta_error"].append(error_beta)
    
    # Convert to arrays for easier manipulation
    for key in results:
        results[key] = np.array(results[key])
    
    # Find best x for each target R
    idx_best_tree = int(np.argmin(results["r_error_tree"]))
    idx_best_loop = int(np.argmin(results["r_error_loop"]))
    idx_best_beta = int(np.argmin(results["beta_error"]))
    
    # Known reference points
    idx_baseline = int(np.argmin(np.abs(results["x_coefficients"] - 0.08)))
    idx_decomposed = int(np.argmin(np.abs(results["x_coefficients"] - 0.052)))
    
    return {
        "x_values": results["x_coefficients"],
        "r_values": np.array(results["r_values"]),
        "beta_eff_values": np.array(results["beta_eff_values"]),
        "r_error_tree": np.array(results["r_error_tree"]),
        "r_error_loop": np.array(results["r_error_loop"]),
        "beta_error": np.array(results["beta_error"]),
        # Best fit indices
        "idx_best_tree": idx_best_tree,
        "idx_best_loop": idx_best_loop,
        "idx_best_beta": idx_best_beta,
        "idx_baseline": idx_baseline,
        "idx_decomposed": idx_decomposed,
        # Reference data
        "kappa": KAPPA,
        "r_target_tree": R_TARGET_TREE,
        "r_target_loop": R_TARGET_LOOP,
        "beta_target": 0.1215,
    }


def print_m15_scan_report(results: Dict[str, Any]) -> None:
    """Print formatted scan report."""
    
    print("\n" + "=" * 100)
    print("M[1,5] REQUIRED COEFFICIENT SCAN")
    print("=" * 100)
    print(f"\nDiagnostic Objective: Identify M[1,5] = x*κ required to achieve target R")
    print(f"κ = 1/(16π²) = {results['kappa']:.6f}")
    print(f"Target R (tree):  {results['r_target_tree']:.8f}")
    print(f"Target R (loop):  {results['r_target_loop']:.8f}")
    print(f"Target β_eff:     0.1215")
    
    # Key reference points
    x_baseline = results["x_values"][results["idx_baseline"]]
    r_baseline = results["r_values"][results["idx_baseline"]]
    beta_baseline = results["beta_eff_values"][results["idx_baseline"]]
    
    x_decomposed = results["x_values"][results["idx_decomposed"]]
    r_decomposed = results["r_values"][results["idx_decomposed"]]
    beta_decomposed = results["beta_eff_values"][results["idx_decomposed"]]
    
    x_best_tree = results["x_values"][results["idx_best_tree"]]
    r_best_tree = results["r_values"][results["idx_best_tree"]]
    beta_best_tree = results["beta_eff_values"][results["idx_best_tree"]]
    err_best_tree = results["r_error_tree"][results["idx_best_tree"]]
    
    x_best_loop = results["x_values"][results["idx_best_loop"]]
    r_best_loop = results["r_values"][results["idx_best_loop"]]
    beta_best_loop = results["beta_eff_values"][results["idx_best_loop"]]
    err_best_loop = results["r_error_loop"][results["idx_best_loop"]]
    
    print("\n" + "-" * 100)
    print("REFERENCE POINTS")
    print("-" * 100)
    print(f"{'Label':<30} {'x (coeff)':<15} {'M[1,5] value':<18} {'R':<12} {'β_eff':<12} {'Error % R':<12}")
    print("-" * 100)
    
    print(f"{'Live baseline (current)':<30} {x_baseline:<15.6f} {x_baseline*results['kappa']:<18.6e} {r_baseline:<12.6f} {beta_baseline:<12.6f} {abs(r_baseline-results['r_target_tree'])/results['r_target_tree']*100:>+10.2f}%")
    print(f"{'Proportional decomposed':<30} {x_decomposed:<15.6f} {x_decomposed*results['kappa']:<18.6e} {r_decomposed:<12.6f} {beta_decomposed:<12.6f} {abs(r_decomposed-results['r_target_tree'])/results['r_target_tree']*100:>+10.2f}%")
    
    print("\n" + "-" * 100)
    print("DIAGNOSTIC TARGETS")
    print("-" * 100)
    print(f"{'Label':<30} {'x (coeff)':<15} {'M[1,5] value':<18} {'R':<12} {'β_eff':<12} {'Error %':<12}")
    print("-" * 100)
    
    print(f"{'Required for R_tree':<30} {x_best_tree:<15.6f} {x_best_tree*results['kappa']:<18.6e} {r_best_tree:<12.6f} {beta_best_tree:<12.6f} {err_best_tree:>+10.3f}%")
    print(f"{'Required for R_loop':<30} {x_best_loop:<15.6f} {x_best_loop*results['kappa']:<18.6e} {r_best_loop:<12.6f} {beta_best_loop:<12.6f} {err_best_loop:>+10.3f}%")
    
    print("\n" + "-" * 100)
    print("INTERPRETATION")
    print("-" * 100)
    print(f"""
  Live baseline uses x = 0.08, producing R = {r_baseline:.6f} (error {abs(r_baseline-results['r_target_tree'])/results['r_target_tree']*100:+.2f}%)
  Proportional decomposition suggests x ≈ 0.052, producing R = {r_decomposed:.6f} (under-corrected)
  
  RG flow analysis shows:
  - To reach R_tree = {results['r_target_tree']:.6f}, required x ≈ {x_best_tree:.4f} (error {err_best_tree:.3f}%)
  - To reach R_loop = {results['r_target_loop']:.6f}, required x ≈ {x_best_loop:.4f}
  
  This required x lies {"BETWEEN decomposed and baseline" if x_decomposed < x_best_tree < x_baseline else ("ABOVE baseline" if x_best_tree > x_baseline else "BELOW decomposed")}.
  
  NEXT STEP: Derive this x from first-principles Euler↔gauge diagram decomposition.
  Do not promote this x as "fitted" or "derived" until independent diagram calculation confirms it.
""")
    
    print("\n" + "-" * 100)
    print("FULL SCAN TABLE (selected points)")
    print("-" * 100)
    print(f"{'x (coeff)':<12} {'R':<12} {'β_eff':<12} {'Error vs R_tree %':<18} {'Error vs β_eff %':<18}")
    print("-" * 100)
    
    # Print every 5th point for readability
    for i in range(0, len(results["x_values"]), max(1, len(results["x_values"]) // 20)):
        x = results["x_values"][i]
        r = results["r_values"][i]
        beta = results["beta_eff_values"][i]
        err_r = results["r_error_tree"][i]
        err_beta = results["beta_error"][i]
        marker = " ← baseline" if abs(x - 0.08) < 0.001 else (" ← decomposed" if abs(x - 0.052) < 0.001 else (" ← best_tree" if i == results["idx_best_tree"] else ""))
        print(f"{x:<12.6f} {r:<12.6f} {beta:<12.6f} {err_r:>+16.3f}% {err_beta:>+16.3f}%{marker}")
    
    print("\n" + "=" * 100 + "\n")


if __name__ == "__main__":
    results = scan_m15_coefficient(x_min=0.045, x_max=0.085, num_points=100)
    print_m15_scan_report(results)
