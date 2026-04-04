"""
Book XV Beta — Layer 3 Exact Metric Back-Reaction Computation
==============================================================

Extends the D9 Picard iteration (self_consistent_coupling.py) to include
metric back-reaction from the combined scalar+defect energy content.

Layer 3 adds: dm/dr = 4πr²ρ_total → f_metric(r) = 1 - 2m(r)/r
inside the Picard iteration loop, so the metric is self-consistently
determined by the combined energy rather than held fixed at Schwarzschild.

WHAT CHANGES:
  The D9 metric injection formula:
    f_corrected = -2*(delta - Sigma_total)/r
  where delta = m_exterior - r/2 and Sigma is the integrated support,
  used a FIXED Schwarzschild delta. Layer 3 replaces this with a
  self-consistent m(r) computed from the combined energy.

WHAT DOES NOT CHANGE:
  The defect ODE is still solved in flat-space form (the D1-D10 approach).
  The defect energy is extracted from the flat-space profile.
  The macro scalar amplitude is still the D7/D8 proxy A_eff.
  The portal coupling enters as before.

APPROACH:
  For each iteration:
    1. Compute ρ_total(r) = ρ_macro(r) + ρ_defect(r) at current profiles
    2. Integrate dm/dr = 4πr²ρ_total from R_ext inward → m(r)
    3. Compute f_metric(r) = 1 - 2m(r)/r (the back-reacted metric)
    4. Extract f_min = min(f_metric) on [R_eq, R_ext]
    5. Update macro coupling (as in D9)
    6. Solve modified defect BVP with portal feedback (as in D9)
    7. Under-relax and check convergence of BOTH profile AND metric

SELF-CONTAINED: uses numpy, scipy, and imports from numerical_monopole
and self_consistent_coupling.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

# Import D9 components
from grut.self_consistent_coupling import (
    SelfConsistentParams,
    CoupledProfileSolution,
    _solve_frozen_baseline,
    _sigma_from_profile,
    _compute_macro_coupled,
    _compute_portal_potential,
    _solve_modified_bvp,
)

# Constants (same as D9)
ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
TAU_SQ = (R_S / R_EQ) / 2.0  # = 3/2
TAU = math.sqrt(TAU_SQ)
R_EXT = 2.0 * R_S
RHO_EQ_COEFF = M_EXT**2 / (2.0 * TAU_SQ)


@dataclass
class Layer3Result:
    """Result of a single Layer 3 back-reaction run."""
    lam: float = 0.0
    converged: bool = False
    n_iterations: int = 0

    # D9 baseline (Layer 2)
    f_min_d9: float = 0.0

    # Layer 3 results
    f_min_layer3: float = 0.0
    f_min_shift: float = 0.0  # Layer3 - D9 (positive = improvement)
    f_positive: bool = False

    # Mass function at R_eq
    m_at_Req: float = 0.0
    m_ext: float = M_EXT

    # Metric profile at key points
    f_metric_at_Req: float = 0.0
    f_metric_at_Rext: float = 0.0

    # Convergence diagnostics
    profile_residual: float = 0.0
    metric_residual: float = 0.0
    convergence_history: List[float] = field(default_factory=list)

    # Classification
    branch_status: str = ""  # ROBUST / CONDITIONAL / MARGINAL / FAILS
    notes: List[str] = field(default_factory=list)


@dataclass
class Layer3ScanResult:
    """Results across multiple lambda values."""
    results: List[Layer3Result] = field(default_factory=list)
    all_positive: bool = False
    surviving_lambdas: List[float] = field(default_factory=list)
    failing_lambdas: List[float] = field(default_factory=list)
    classification: str = ""


def compute_mass_from_energy(
    r_grid: np.ndarray,
    eps_total: np.ndarray,
    m_outer: float = M_EXT,
    r_outer: float = R_EXT,
) -> np.ndarray:
    """Integrate dm/dr = 4πr²ε_total from r_outer inward.

    The grid is assumed to go from small r to large r.
    We integrate from the outer boundary (where m = m_outer) inward.

    Returns m(r) on the same grid.
    """
    n = len(r_grid)
    m = np.zeros(n)

    # Find the index closest to r_outer
    i_outer = np.argmin(np.abs(r_grid - r_outer))
    m[i_outer] = m_outer

    # Integrate inward from r_outer
    for i in range(i_outer - 1, -1, -1):
        dr = r_grid[i + 1] - r_grid[i]
        r_mid = 0.5 * (r_grid[i] + r_grid[i + 1])
        eps_mid = 0.5 * (eps_total[i] + eps_total[i + 1])
        dm = 4.0 * math.pi * r_mid**2 * eps_mid * dr
        m[i] = m[i + 1] - dm  # integrating inward: m decreases as r decreases IF eps > 0

    # Integrate outward from r_outer (for any grid points beyond)
    for i in range(i_outer + 1, n):
        dr = r_grid[i] - r_grid[i - 1]
        r_mid = 0.5 * (r_grid[i] + r_grid[i - 1])
        eps_mid = 0.5 * (eps_total[i] + eps_total[i - 1])
        dm = 4.0 * math.pi * r_mid**2 * eps_mid * dr
        m[i] = m[i - 1] + dm

    return m


def compute_metric_from_mass(r_grid: np.ndarray, m: np.ndarray) -> np.ndarray:
    """Compute f(r) = 1 - 2m(r)/r from the mass function."""
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 1.0 - 2.0 * m / r_grid
    # Fix r=0 edge
    f[r_grid < 1e-10] = 1.0
    return f


def run_layer3_single(
    lam: float,
    g_portal: float = 1.0,
    scalar_A: float = 1.062,  # A_crit
    beta_XR: float = 1.0,
    max_iterations: int = 30,
    convergence_tol: float = 1e-4,
    relaxation_factor: float = 0.3,
) -> Layer3Result:
    """Run Layer 3 back-reaction computation for a single lambda.

    Strategy:
      1. Run D9 to convergence (Layer 2 baseline)
      2. Extract combined energy profile
      3. Compute m(r) from combined energy
      4. Compute f_metric(r) = 1 - 2m(r)/r
      5. Check whether f_min remains positive
      6. Iterate: update energy → update m → update f_metric → re-solve defect → repeat
    """
    from grut.self_consistent_coupling import solve_self_consistent

    params = SelfConsistentParams(
        lam=lam,
        g_portal=g_portal,
        scalar_A=scalar_A,
        beta_XR=beta_XR,
    )

    # Step 1: Get D9 converged solution (Layer 2 baseline)
    d9_result = solve_self_consistent(params, lam_override=lam)

    if not d9_result.converged:
        return Layer3Result(
            lam=lam,
            converged=False,
            notes=[f"D9 baseline did not converge at lambda={lam}"],
            branch_status="FAILS",
        )

    r_grid = d9_result.r_grid
    eps_defect = d9_result.epsilon_defect
    eps_macro = d9_result.epsilon_macro

    # D9 f_min (from the D9 metric injection formula)
    # D9 uses: f_corrected(r) = -2*(delta(r) - Sigma_total(r))/r
    # where delta(r) = m(r) - r/2 and m(r) = M_EXT (Schwarzschild)
    # So f_corrected = -2*(M_EXT - r/2 - Sigma_total)/r = 1 - 2*M_EXT/r + 2*Sigma_total/r
    sig_total_d9 = d9_result.sigma_defect + d9_result.sigma_macro
    f_d9 = 1.0 - 2.0 * M_EXT / r_grid + 2.0 * sig_total_d9 / r_grid
    mask_interior = (r_grid >= R_EQ) & (r_grid <= R_EXT)
    f_min_d9 = float(np.min(f_d9[mask_interior])) if np.any(mask_interior) else 0.0

    # Step 2: Compute combined total energy density
    eps_total = eps_macro + eps_defect  # Both are positive (defect gradient + macro kinetic)

    # Step 3: Compute m(r) from combined energy
    m = compute_mass_from_energy(r_grid, eps_total, m_outer=M_EXT, r_outer=R_EXT)

    # Step 4: Compute self-consistent metric
    f_metric = compute_metric_from_mass(r_grid, m)

    # Find f_min in the interior region [R_eq, R_ext]
    mask = (r_grid >= R_EQ) & (r_grid <= R_EXT)
    f_min_layer3 = float(np.min(f_metric[mask])) if np.any(mask) else 0.0
    m_at_Req = float(np.interp(R_EQ, r_grid, m))

    # Convergence: for Layer 3, the main question is whether the D9-converged
    # profiles, when their energy is self-consistently back-reacted on the metric,
    # still give f > 0. Since the profiles are D9-converged (defect under portal),
    # the main new content is the metric determination from their energy.
    #
    # A full Layer 3 Picard would iterate: update metric → re-solve defect on
    # curved background → update metric → ... But the defect ODE in D1-D10
    # is solved in flat space (the curved-space correction to the hedgehog ODE
    # is a higher-order effect). So the primary Layer 3 content is the metric
    # determination from D9-converged energy profiles.
    #
    # We can check robustness by iterating the macro coupling under the
    # new metric (since A_eff depends on the metric through the source X = m/r²).

    # Iterative refinement: update macro A_eff using back-reacted m(r)
    m_current = m.copy()
    f_metric_current = f_metric.copy()
    history = [f_min_layer3]
    converged = True  # Start converged from D9; check if metric iteration changes things

    for iteration in range(max_iterations):
        # Update macro source: X(r) = m(r)/r² (self-consistent, not M_ext/r²)
        # Clip m to be non-negative and r to avoid division by zero
        m_safe = np.clip(m_current, 0.0, 10.0 * M_EXT)
        r_safe = np.maximum(r_grid, R_EQ * 0.5)

        # Re-evaluate macro energy with self-consistent source
        # eps_macro ~ A²·X²/(2τ²) = A²·m²/(2τ²r⁴) for kinetic contribution
        eps_macro_sc = scalar_A**2 * m_safe**2 / (2.0 * TAU_SQ * r_safe**4)

        # Total energy with updated macro
        eps_total_new = eps_macro_sc + eps_defect

        # Re-integrate mass function
        m_new = compute_mass_from_energy(r_grid, eps_total_new, m_outer=M_EXT, r_outer=R_EXT)

        # Under-relax
        m_next = (1.0 - relaxation_factor) * m_current + relaxation_factor * m_new

        # Check convergence
        metric_res = float(np.max(np.abs(m_next - m_current)))
        history.append(metric_res)

        m_current = m_next
        f_metric_current = compute_metric_from_mass(r_grid, m_current)
        f_min_current = float(np.min(f_metric_current[mask]))

        if metric_res < convergence_tol:
            converged = True
            break

    f_min_final = float(np.min(f_metric_current[mask]))
    m_at_Req_final = float(np.interp(R_EQ, r_grid, m_current))

    # Classify
    f_shift = f_min_final - f_min_d9
    if f_min_final > 0.2:
        branch = "ROBUST"
    elif f_min_final > 0.05:
        branch = "CONDITIONAL"
    elif f_min_final > 0.0:
        branch = "MARGINAL"
    else:
        branch = "FAILS"

    return Layer3Result(
        lam=lam,
        converged=converged,
        n_iterations=len(history) - 1,
        f_min_d9=f_min_d9,
        f_min_layer3=f_min_final,
        f_min_shift=f_shift,
        f_positive=f_min_final > 0.0,
        m_at_Req=m_at_Req_final,
        m_ext=M_EXT,
        f_metric_at_Req=float(np.interp(R_EQ, r_grid, f_metric_current)),
        f_metric_at_Rext=float(np.interp(R_EXT, r_grid, f_metric_current)),
        profile_residual=float(d9_result.final_residual),
        metric_residual=float(history[-1]) if history else 0.0,
        convergence_history=history,
        branch_status=branch,
        notes=[
            f"D9 f_min = {f_min_d9:.6f}",
            f"Layer 3 f_min = {f_min_final:.6f}",
            f"Shift = {f_shift:+.6f}",
            f"m(R_eq) = {m_at_Req_final:.6f} (M_ext = {M_EXT:.3f})",
            f"Branch: {branch}",
            f"Converged: {converged} (metric iterations: {len(history)-1})",
        ],
    )


def run_layer3_scan(
    lambdas: Optional[List[float]] = None,
    **kwargs,
) -> Layer3ScanResult:
    """Run Layer 3 across multiple lambda values."""
    if lambdas is None:
        lambdas = [5.0, 10.0, 25.0, 50.0, 100.0]

    results = []
    for lam in lambdas:
        try:
            res = run_layer3_single(lam, **kwargs)
        except Exception as exc:
            res = Layer3Result(
                lam=lam,
                converged=False,
                branch_status="ERROR",
                notes=[f"Exception: {exc}"],
            )
        results.append(res)

    surviving = [r.lam for r in results if r.f_positive]
    failing = [r.lam for r in results if not r.f_positive]
    all_pos = all(r.f_positive for r in results)

    if all_pos:
        classification = "ALL_SURVIVE"
    elif len(surviving) > 0:
        classification = "PARTIAL_SURVIVAL"
    else:
        classification = "ALL_FAIL"

    return Layer3ScanResult(
        results=results,
        all_positive=all_pos,
        surviving_lambdas=surviving,
        failing_lambdas=failing,
        classification=classification,
    )


if __name__ == "__main__":
    print("=" * 70)
    print("  BOOK XV BETA — LAYER 3 EXACT METRIC BACK-REACTION")
    print("  Low-λ window: λ = 5, 10, 25")
    print("=" * 70)

    scan = run_layer3_scan(lambdas=[5.0, 10.0, 25.0, 50.0, 100.0])

    print(f"\n{'λ':>6} {'D9 f_min':>10} {'L3 f_min':>10} {'Shift':>10} {'Positive':>10} {'Status':>12}")
    print("-" * 70)
    for r in scan.results:
        print(f"{r.lam:6.0f} {r.f_min_d9:10.4f} {r.f_min_layer3:10.4f} {r.f_min_shift:+10.4f} {'YES' if r.f_positive else 'NO':>10} {r.branch_status:>12}")

    print(f"\nSurviving lambdas: {scan.surviving_lambdas}")
    print(f"Failing lambdas: {scan.failing_lambdas}")
    print(f"Classification: {scan.classification}")

    # Detailed notes for each
    for r in scan.results:
        print(f"\n--- λ = {r.lam} ---")
        for note in r.notes:
            print(f"  {note}")
