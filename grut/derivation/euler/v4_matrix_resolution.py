"""
V4 Matrix Resolution: Independent derivation of R from the 9×9 RG mixing matrix.

PURPOSE
-------
V4.3 hardcodes beta_eff = -0.1215 (back-solved from R_obs = 1.154) and does not
derive it from the 9×9 matrix eigenstructure.  This module performs the correct
computation:

  1. Construct M (the 9×9 RG beta-function matrix) from V4.3 specifications.
  2. Verify internal consistency: trace(M) must equal sum of eigenvalues.
  3. Evolve the ODE  dC/d(ln M_P/μ) = M · C  from M_P to H⁻¹.
  4. Extract the Euler-channel prediction R = C_Euler(H⁻¹)  WITHOUT using
     R_obs = 1.154 as input.
  5. Sweep λ_Euler ∈ [0.80, 1.00] to determine sensitivity.

RESULT (Correction #32, May 2026)
----------------------------------
The structural estimate matrix gives R_matrix ≈ 10⁸⁹ (CIRCULAR verdict).
Root cause: dominant eigenvalue +2.28 captures 32% of the Euler channel's
initial projection and amplifies it over 96.74 log-steps.  The eigenvalue
nearest to the required β_eff = 0.1215 is 0.1247 (3% off), but the Euler
channel projects onto it with only |coeff| = 0.049.

Run as a script:  python v4_matrix_resolution.py
Returns a structured dict (also printed) with:
  - matrix_trace          : sum of diagonal entries
  - eigenvalue_sum        : sum of computed eigenvalues (must equal trace)
  - v43_eigenvalue_sum    : sum of V4.3-stated eigenvalues (1.831)
  - consistency_ok        : bool
  - R_predicted           : Euler channel prediction without observational input
  - R_observed            : 1.154 (for comparison)
  - error_percent         : |R_predicted - 1.154| / 1.154 * 100
  - beta_eff_derived      : ln(amplification) / t, derived from matrix
  - beta_eff_calibrated   : -0.1215 (V4.3 back-solved value)
  - provenance            : "independent" or "circular" or "inconsistent"

OPEN QUESTION #20 — PROOF STRATEGY
------------------------------------
The 0.1247 eigenvalue is within 3% of the required 0.1215. Whether this is a
structural signal or numerical coincidence is decided by implementing the actual
2-loop tensor calculus on the curved S⁴ background (not flat-space dimensional
regularization approximations).  The proof proceeds in three steps:

Step A — First-principles matrix entries from S⁴ 2-loop beta functions
  Replace the structural estimates in build_matrix() with M_ij computed from
  the heat-kernel / Seeley-DeWitt anomaly coefficients on S⁴ for each operator
  pair (i, j).  These are known at 1-loop for individual operators; the 2-loop
  off-diagonal mixing requires the full curved-background tensor contraction:

    M_ij = (1/16π²) × <O_i | δβ_j/δg_μν | O_j>|_{S⁴, W²=0}

  where δβ/δg is the functional derivative of the RG beta function with respect
  to the background metric, evaluated on the S⁴ saddle (Weyl² = 0).

Step B — S⁴ geometry zeroes non-topological off-diagonals
  On S⁴, Weyl² = 0 by construction.  Any operator mixing that requires a Weyl²
  insertion (e.g. Weyl-sector → Euler-sector coupling) must vanish identically.
  This is the key geometric constraint:

    M[Weyl-type, Euler] |_{W²=0}  =  0

  In the structural estimate matrix, these entries are set to 0.025 (midpoint
  of "0.01-0.04" range) — a non-zero value that couples the Euler channel to
  the dominant +2.28 Weyl-sector eigenvector.  If the S⁴ geometry forces these
  to zero, the Euler channel's projection onto the dominant mode collapses:

    |coeff on λ=2.28|  →  < 0.01   (from current 0.322)

Step C — Eigenvalue refinement and verdict
  With the Weyl-sector off-diagonals zeroed, the Euler channel evolves almost
  entirely on the topological sub-block of M.  If the first-principles diagonal
  and remaining off-diagonal entries of that sub-block produce an eigenvalue
  within ≤ 1% of 0.1215, the result is:

    R_predicted (first-principles) ≈ 1.154   [INDEPENDENT verdict]

  and the 0.28% agreement of V4.3 is confirmed as structurally correct — the
  calibrated β_eff matched what the geometry would have given.

  If the topological sub-block eigenvalue deviates > 5% from 0.1215, the
  framework has a genuine structural gap and V4's agreement with observation
  was coincidental.

Implementation guide
  - Seeley-DeWitt coefficient a₂ for each operator on S⁴: well-tabulated in
    Christensen & Duff (1979), Barvinsky & Vilkovisky (1985).
  - Off-diagonal mixing at 2-loop: requires the techniques of
    Jack & Osborn (1990), Osborn (2003) applied to S⁴ curved background.
  - The `grut/hard_theory/s4_ctp_solver/` directory and the AJ propagator
    (`grut/derivation/tji/allen_jacobson.py`) provide the S⁴ geometric
    machinery already in the codebase.
  - Test criterion: provenance == "independent" AND error_percent < 1.0%
"""

from __future__ import annotations
import math
from typing import Dict, Any

import numpy as np
from scipy.linalg import expm  # matrix exponential


# ---------------------------------------------------------------------------
# Operator index legend
# ---------------------------------------------------------------------------
# 0: R²              pure gravity scalar
# 1: Euler/G_B       topological Gauss-Bonnet  ← hierarchy-defining
# 2: □R              conformal box operator
# 3: R²_quark        fermionic sector scalar
# 4: G_B_ferm        fermionic topological
# 5: Tr(F²)·R²       gauge-scalar mixing
# 6: Tr(F·G_B)       gauge-topological mixing
# 7: Λ               cosmological constant  ← universal coupling hub
# 8: Mixed_EW        electroweak-gravity coupling

# V4.3-stated eigenvalues (Step 2 of Phase 3)
V43_EIGENVALUES = [2.325, 0.260, 0.204, 0.162, 0.120, 0.099, 0.052, 0.011, -1.402]

# V3 Euler barepoint at Planck scale
R_BARE_PLANCK = 9.07e-6

# Observed cosmological R
R_OBSERVED = 1.154

# Scale span: ln(M_P / H⁻¹) = 42 × ln(10)
T_PLANCK_TO_HUBBLE = 42.0 * math.log(10)   # = 96.74

# V4.3 back-solved effective beta
BETA_EFF_V43 = -0.1215


def build_matrix(lambda_euler: float = 0.92) -> np.ndarray:
    """
    Construct the 9×9 RG beta-function matrix M from V4.3 specifications.

    Convention: dC/d(ln M_P/μ) = M · C
    Positive diagonal → operator grows as RG runs to lower μ (IR direction).

    Parameters
    ----------
    lambda_euler : float
        Λ→Euler coupling strength (default 0.92 as in V4.3).

    Returns
    -------
    np.ndarray, shape (9, 9), symmetric
    """
    # ---- Diagonal (self-coupling β functions, from V4.3 table) ----
    diag = [0.15, 0.11, 0.08, 0.18, 0.14, 0.22, 0.19, 0.09, 0.16]
    M = np.diag(diag, k=0).astype(float)

    # ---- Λ off-diagonal couplings (symmetric) ----
    # Specified: R²↔Λ=0.73, Euler↔Λ=λ_euler, □R↔Λ=0.45,
    #            R²_ferm↔Λ=0.61, G_B_ferm↔Λ=0.58, Tr(F²)·R²↔Λ=0.84
    # Estimated for unspecified entries: Tr(F·G_B)↔Λ=0.70, Mixed_EW↔Λ=0.65
    lambda_couplings = {
        0: 0.73,            # R²      ↔ Λ (specified)
        1: lambda_euler,    # Euler   ↔ Λ (key coupling; varied in sweep)
        2: 0.45,            # □R      ↔ Λ (specified)
        3: 0.61,            # R²_ferm ↔ Λ (specified)
        4: 0.58,            # G_B_ferm↔ Λ (specified)
        5: 0.84,            # Tr(F²)  ↔ Λ (specified)
        6: 0.70,            # Tr(F·GB)↔ Λ (estimated midpoint)
        # 7: Λ itself — diagonal only
        8: 0.65,            # Mixed_EW↔ Λ (estimated midpoint)
    }
    for i, c in lambda_couplings.items():
        M[7, i] = c
        M[i, 7] = c

    # ---- Pure gravity off-diagonal (R²↔Euler, R²↔□R, Euler↔□R) ----
    # V4.3: "0.01–0.04"; use midpoint 0.025
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        M[i, j] = M[j, i] = 0.025

    # ---- Fermion ↔ Fermion ----
    M[3, 4] = M[4, 3] = 0.05

    # ---- Gauge ↔ Gauge ----
    M[5, 6] = M[6, 5] = 0.08

    # ---- Gauge ↔ Gravity (cross-sector) ----
    # V4.3: "0.07–0.09"; use midpoint 0.08
    for grav in [0, 1, 2]:
        for gauge in [5, 6]:
            M[grav, gauge] = M[gauge, grav] = 0.08

    # ---- Fermion ↔ Gauge cross-sector ----
    for ferm in [3, 4]:
        for gauge in [5, 6]:
            M[ferm, gauge] = M[gauge, ferm] = 0.05

    # ---- Fermion ↔ Gravity ----
    for grav in [0, 1, 2]:
        for ferm in [3, 4]:
            if M[grav, ferm] == 0.0:
                M[grav, ferm] = M[ferm, grav] = 0.03  # mild cross-sector

    # ---- Mixed_EW ↔ all remaining zeros ----
    for i in range(8):
        if M[8, i] == 0.0:
            M[8, i] = M[i, 8] = 0.04  # mild EW coupling

    return M


def build_matrix_s4_geometry_constrained(lambda_euler: float = 0.92) -> np.ndarray:
    """
    Gate B test: apply the S⁴ Weyl² = 0 geometric constraint to build_matrix().

    On S⁴, the Weyl tensor vanishes identically (W² = 0).  Any mixing matrix
    element M[i, j] that requires a Weyl² insertion to couple operator i to
    operator j must vanish.  This affects specifically:

    - Weyl-sector (R², □R) ↔ Euler (topological)
      R² and □R have non-trivial Weyl² components; on S⁴ their coupling to the
      purely topological Euler sector via Weyl-mediated diagrams is zero.
      Retained coupling: only the purely scalar (trace) channel, which on S⁴
      is suppressed to the Ricci-scalar level.  Conservative residual: 0.005.

    - Gauge ↔ Euler cross-sector
      Tr(F²)·R² and Tr(F·G_B) couple to Euler via a Weyl² graviton insertion
      in 2-loop diagrams.  On S⁴ this insertion vanishes.  Conservative
      residual: 0.005 (from direct Ricci coupling, not Weyl-mediated).

    - Mixed_EW ↔ Euler
      Same argument: EW-gravity mixing via Weyl insertion → zero on S⁴.
      Conservative residual: 0.005.

    Entries NOT zeroed (do not require Weyl² insertion):
    - Λ ↔ Euler: cosmological constant couples to the topological sector via
      the volume form, not through Weyl².  This survives W²=0.
    - Fermion/topological ↔ Euler: G_B_ferm is itself topological; coupling
      between topological sectors does not require Weyl² insertion.
    - All diagonal entries: self-couplings on S⁴ use the background Ricci
      scalar (non-zero), not Weyl tensor.

    Parameters
    ----------
    lambda_euler : float
        Λ→Euler coupling (unchanged from unconstrained matrix).

    Returns
    -------
    np.ndarray, shape (9, 9)
        The W²=0-constrained beta-function matrix.
    """
    # Start from the structural estimate matrix
    M = build_matrix(lambda_euler=lambda_euler).copy()

    WEYL_RESIDUAL = 0.005  # conservative non-zero residual for Ricci-channel coupling

    # ---- Zero Weyl-sector ↔ Euler off-diagonals ----
    # Operators 0 (R²) and 2 (□R) are Weyl-sector; operator 1 is Euler.
    for weyl_op in [0, 2]:
        M[weyl_op, 1] = WEYL_RESIDUAL
        M[1, weyl_op] = WEYL_RESIDUAL

    # ---- Zero Gauge ↔ Euler (Weyl-insertion required) ----
    # Operators 5 (Tr(F²)·R²) and 6 (Tr(F·G_B)) ↔ Euler (1)
    for gauge_op in [5, 6]:
        M[gauge_op, 1] = WEYL_RESIDUAL
        M[1, gauge_op] = WEYL_RESIDUAL

    # ---- Zero Mixed_EW ↔ Euler ----
    M[8, 1] = WEYL_RESIDUAL
    M[1, 8] = WEYL_RESIDUAL

    return M


def evolve_euler_channel(M: np.ndarray) -> tuple[float, float]:
    """
    Evolve C₀ = (0, R_bare, 0, …, 0) from Planck to Hubble via exp(M·t).

    Returns
    -------
    R_predicted : Euler-channel value at Hubble scale
    beta_eff    : derived from matrix (= ln(R_predicted/R_bare) / t)
    """
    C0 = np.zeros(9)
    C0[1] = R_BARE_PLANCK

    M_evolved = expm(M * T_PLANCK_TO_HUBBLE)
    C_hubble = M_evolved @ C0

    R_predicted = float(C_hubble[1])
    if R_predicted > 0 and R_BARE_PLANCK > 0:
        beta_eff = math.log(R_predicted / R_BARE_PLANCK) / T_PLANCK_TO_HUBBLE
    else:
        beta_eff = float("nan")

    return R_predicted, beta_eff


def run_resolution(lambda_euler: float = 0.92) -> Dict[str, Any]:
    """
    Full resolution for a given Λ→Euler coupling.

    Returns a dict with all diagnostic quantities.
    """
    M = build_matrix(lambda_euler=lambda_euler)

    # ---- Consistency check ----
    matrix_trace = float(np.trace(M))
    eigenvalues_computed = sorted(np.linalg.eigvals(M).real, reverse=True)
    eigenvalue_sum_computed = float(sum(eigenvalues_computed))
    eigenvalue_sum_v43 = sum(V43_EIGENVALUES)

    trace_match_computed = abs(matrix_trace - eigenvalue_sum_computed) < 1e-6
    v43_consistent = abs(eigenvalue_sum_v43 - matrix_trace) < 0.05  # 5% tolerance

    # ---- Euler channel evolution ----
    R_predicted, beta_eff_derived = evolve_euler_channel(M)
    error_pct = abs(R_predicted - R_OBSERVED) / R_OBSERVED * 100

    # ---- Provenance classification ----
    if not trace_match_computed:
        provenance = "matrix_construction_error"
    elif abs(beta_eff_derived - abs(BETA_EFF_V43)) / abs(BETA_EFF_V43) < 0.05:
        # beta_eff from matrix agrees with V4.3 back-solved value to within 5%
        provenance = "independent"  # matrix gives same beta_eff without using R_obs
    elif error_pct < 5.0:
        provenance = "approximately_independent"
    else:
        provenance = "circular"  # matrix alone doesn't give R ≈ 1.154

    return {
        "lambda_euler": lambda_euler,
        "matrix_trace": round(matrix_trace, 6),
        "eigenvalue_sum_computed": round(eigenvalue_sum_computed, 6),
        "eigenvalue_sum_v43_stated": round(eigenvalue_sum_v43, 6),
        "trace_equals_eigensum": trace_match_computed,
        "v43_eigenvalues_consistent_with_matrix": v43_consistent,
        "eigenvalues_computed": [round(e, 4) for e in eigenvalues_computed],
        "eigenvalues_v43_stated": sorted(V43_EIGENVALUES, reverse=True),
        "R_predicted": round(R_predicted, 6),
        "R_observed": R_OBSERVED,
        "error_percent": round(error_pct, 2),
        "beta_eff_derived": round(beta_eff_derived, 6),
        "beta_eff_v43_calibrated": BETA_EFF_V43,
        "provenance": provenance,
    }


def run_lambda_sweep(lo: float = 0.80, hi: float = 1.00, steps: int = 9) -> list[Dict[str, Any]]:
    """
    Sweep Λ→Euler coupling and record R_predicted at each value.
    """
    results = []
    for i in range(steps):
        lam = lo + (hi - lo) * i / (steps - 1)
        r = run_resolution(lambda_euler=round(lam, 3))
        results.append({
            "lambda_euler": r["lambda_euler"],
            "R_predicted": r["R_predicted"],
            "error_percent": r["error_percent"],
            "beta_eff_derived": r["beta_eff_derived"],
            "provenance": r["provenance"],
        })
    return results


def print_report(result: Dict[str, Any]) -> None:
    """Pretty-print the resolution report."""
    print("\n" + "=" * 70)
    print("V4 MATRIX RESOLUTION REPORT")
    print("=" * 70)

    print(f"\n  λ_Euler (Λ→Euler coupling)   : {result['lambda_euler']}")
    print(f"\n--- Consistency Check ---")
    print(f"  matrix trace                 : {result['matrix_trace']}")
    print(f"  sum of computed eigenvalues  : {result['eigenvalue_sum_computed']}")
    print(f"  sum of V4.3-stated eigenvalues: {result['eigenvalue_sum_v43_stated']}")
    print(f"  trace == computed eig_sum    : {result['trace_equals_eigensum']}")
    print(f"  V4.3 eigenvalues consistent  : {result['v43_eigenvalues_consistent_with_matrix']}")

    print(f"\n--- Eigenvalues ---")
    print(f"  Computed : {result['eigenvalues_computed']}")
    print(f"  V4.3     : {result['eigenvalues_v43_stated']}")

    print(f"\n--- R Prediction (from matrix, NO observational input) ---")
    print(f"  R_predicted                  : {result['R_predicted']}")
    print(f"  R_observed                   : {result['R_observed']}")
    print(f"  Error                        : {result['error_percent']}%")

    print(f"\n--- β_eff ---")
    print(f"  Derived from matrix          : {result['beta_eff_derived']}")
    print(f"  V4.3 back-solved from R_obs  : {result['beta_eff_v43_calibrated']}")

    print(f"\n--- Provenance Verdict ---")
    print(f"  {result['provenance'].upper()}")

    verdict_map = {
        "independent": "  ✅ Matrix naturally gives R ≈ 1.154. V4 is a genuine prediction.",
        "approximately_independent": "  ⚠️  Matrix gives R within 5% of 1.154. Approximately independent.",
        "circular": "  ❌ Matrix alone does NOT give R ≈ 1.154. β_eff = -0.1215 was fitted.",
        "matrix_construction_error": "  ❌ Matrix construction error (trace ≠ eigenvalue sum).",
    }
    print(verdict_map.get(result["provenance"], "  ? Unknown provenance."))
    print("=" * 70 + "\n")


def run_gate_b_test(lambda_euler: float = 0.92) -> Dict[str, Any]:
    """
    Gate B of the open-question #20 proof strategy.

    Applies the S⁴ Weyl²=0 constraint (build_matrix_s4_geometry_constrained)
    and reports:
      - Whether the Euler channel's projection onto the dominant eigenvector
        collapses from ~0.322 to < 0.01
      - Whether the dominant eigenvalue decouples from the Euler sector
      - What R_predicted becomes
      - Whether the nearest-to-0.1215 eigenvalue shifts closer
      - Overall Gate B verdict: PASS / FAIL / PARTIAL

    Returns a dict suitable for printing and for automated test assertions.
    """
    M_raw = build_matrix(lambda_euler=lambda_euler)
    M_s4  = build_matrix_s4_geometry_constrained(lambda_euler=lambda_euler)

    def _projection_onto_dominant(M: np.ndarray) -> tuple[float, float, float]:
        """Return (dominant_eigenvalue, euler_proj_on_dominant, nearest_to_required)."""
        vals, vecs = np.linalg.eig(M)
        C0 = np.zeros(9); C0[1] = 1.0
        try:
            coeffs = np.linalg.solve(vecs, C0)
        except np.linalg.LinAlgError:
            return float("nan"), float("nan"), float("nan")
        idx_dom = int(np.argmax(vals.real))
        proj_on_dominant = float(abs(coeffs[idx_dom]))
        nearest_eig = float(min(vals.real, key=lambda x: abs(x - 0.1215)))
        return float(vals[idx_dom].real), proj_on_dominant, nearest_eig

    dom_raw, proj_raw, near_raw = _projection_onto_dominant(M_raw)
    dom_s4,  proj_s4,  near_s4  = _projection_onto_dominant(M_s4)

    R_s4, beta_s4 = evolve_euler_channel(M_s4)
    error_s4 = abs(R_s4 - R_OBSERVED) / R_OBSERVED * 100

    # Gate B pass conditions
    projection_collapsed = proj_s4 < 0.01          # from 0.322 → < 0.01
    eigenvalue_refined   = abs(near_s4 - 0.1215) / 0.1215 < 0.05  # within 5%
    r_in_range           = error_s4 < 5.0           # R within 5% of 1.154

    if projection_collapsed and eigenvalue_refined and r_in_range:
        gate_b_verdict = "PASS"
    elif projection_collapsed and eigenvalue_refined:
        gate_b_verdict = "PARTIAL — projection collapsed, eigenvalue refined, but R still off (diagonals need first-principles values)"
    elif projection_collapsed:
        gate_b_verdict = "PARTIAL — projection collapsed but eigenvalue not yet at 0.1215"
    else:
        gate_b_verdict = "FAIL — W²=0 constraint insufficient to collapse dominant-mode projection"

    return {
        # Before constraint
        "dominant_eigenvalue_raw":          round(dom_raw, 4),
        "euler_proj_on_dominant_raw":        round(proj_raw, 4),
        "nearest_eigenvalue_to_0.1215_raw":  round(near_raw, 4),
        # After S⁴ W²=0 constraint
        "dominant_eigenvalue_s4":           round(dom_s4, 4),
        "euler_proj_on_dominant_s4":         round(proj_s4, 6),
        "nearest_eigenvalue_to_0.1215_s4":   round(near_s4, 4),
        "R_predicted_s4":                    R_s4,
        "R_observed":                        R_OBSERVED,
        "error_percent_s4":                  round(error_s4, 2),
        "beta_eff_s4":                       round(beta_s4, 6),
        # Pass conditions
        "gate_b_projection_collapsed":       projection_collapsed,
        "gate_b_eigenvalue_refined":         eigenvalue_refined,
        "gate_b_r_in_range":                 r_in_range,
        "gate_b_verdict":                    gate_b_verdict,
    }


def print_gate_b_report(r: Dict[str, Any]) -> None:
    print("\n" + "=" * 70)
    print("GATE B TEST — S⁴ Weyl²=0 Geometric Constraint")
    print("=" * 70)

    print("\n--- Before constraint (structural estimates) ---")
    print(f"  Dominant eigenvalue          : {r['dominant_eigenvalue_raw']}")
    print(f"  Euler proj on dominant mode  : {r['euler_proj_on_dominant_raw']}  (target: < 0.01)")
    print(f"  Nearest eig to 0.1215        : {r['nearest_eigenvalue_to_0.1215_raw']}  (target: within 1%)")

    print("\n--- After W²=0 constraint ---")
    print(f"  Dominant eigenvalue          : {r['dominant_eigenvalue_s4']}")
    print(f"  Euler proj on dominant mode  : {r['euler_proj_on_dominant_s4']}  ({'✅ collapsed' if r['gate_b_projection_collapsed'] else '❌ still large'})")
    print(f"  Nearest eig to 0.1215        : {r['nearest_eigenvalue_to_0.1215_s4']}  ({'✅ refined' if r['gate_b_eigenvalue_refined'] else '❌ not refined'})")
    print(f"  R_predicted (S⁴ constrained) : {r['R_predicted_s4']:.6g}")
    print(f"  R_observed                   : {r['R_observed']}")
    print(f"  Error                        : {r['error_percent_s4']}%  ({'✅ in range' if r['gate_b_r_in_range'] else '❌ outside range'})")
    print(f"  β_eff (S⁴ constrained)       : {r['beta_eff_s4']}")

    print(f"\n--- Gate B Verdict ---")
    icon = "✅" if r['gate_b_verdict'] == "PASS" else ("⚠️ " if "PARTIAL" in r['gate_b_verdict'] else "❌")
    print(f"  {icon}  {r['gate_b_verdict']}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # ----- Primary resolution at λ = 0.92 (baseline, structural estimates) -----
    result = run_resolution(lambda_euler=0.92)
    print_report(result)

    # ----- Gate B: S⁴ Weyl²=0 constraint test -----
    gate_b = run_gate_b_test(lambda_euler=0.92)
    print_gate_b_report(gate_b)

    # ----- Sensitivity sweep (structural estimates) -----
    print("ΛAMBDA SWEEP (R_predicted vs λ_Euler, structural estimates)\n")
    print(f"{'λ':>6}  {'R_pred':>10}  {'error%':>8}  {'β_eff':>10}  provenance")
    print("-" * 60)
    sweep = run_lambda_sweep()
    for row in sweep:
        print(
            f"{row['lambda_euler']:>6.3f}  "
            f"{row['R_predicted']:>10.4g}  "
            f"{row['error_percent']:>8.2f}%  "
            f"{row['beta_eff_derived']:>10.4f}  "
            f"{row['provenance']}"
        )
    print()
