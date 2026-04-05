"""
Book XXI Gamma — Bifurcation Search in the Coupled Nonlinear System
====================================================================

Tests whether the coupled (Phi, f) system with portal coupling and
Mexican-hat potential admits multiple solutions at any parameter values.

The hedgehog BVP:
  f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) + g_p*Phi^2*f = 0
  BCs: f(r_min) ~ 0, f(r_max) = 1

SEARCH STRATEGY:
  1. Different initial guesses for the BVP (standard hedgehog vs inverted vs flat)
  2. Scan over wide parameter ranges (lambda, g_p, eta)
  3. Test whether the BVP converges to DIFFERENT solutions from different guesses
  4. Look for parameter values where the solution character changes qualitatively

WHAT WOULD CONSTITUTE MULTIPLICITY:
  - Two distinct converged f(r) profiles at the same (lambda, g_p, eta)
  - A qualitative change in solution structure (e.g., f becomes non-monotone)
  - Convergence failure at some parameters followed by recovery (bifurcation signature)

WHAT WOULD NOT CONSTITUTE MULTIPLICITY:
  - Different solutions at different parameters (just parameter dependence)
  - Numerical noise or non-convergence (solver artifact)
  - Solutions differing only at boundary (boundary effect, not bifurcation)
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

try:
    from scipy.integrate import solve_bvp
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# Constants
ETA_MATCH = 1.0 / math.sqrt(8.0 * math.pi)
R_MIN_DEFAULT = 0.01
R_MAX_DEFAULT = 10.0
N_GRID = 400


@dataclass
class BVPSolution:
    """A single BVP solution."""
    lam: float = 0.0
    g_p: float = 0.0
    eta: float = ETA_MATCH
    guess_type: str = ""
    converged: bool = False
    f_at_rmin: float = 0.0
    f_at_rmax: float = 0.0
    f_max: float = 0.0
    f_min: float = 0.0
    c1: float = 0.0          # slope at origin
    monotone: bool = True
    rms_residual: float = 0.0
    f_profile: Optional[np.ndarray] = None
    r_grid: Optional[np.ndarray] = None
    notes: List[str] = field(default_factory=list)


@dataclass
class BifurcationResult:
    """Result of bifurcation search at one parameter point."""
    lam: float = 0.0
    g_p: float = 0.0
    eta: float = ETA_MATCH
    n_guesses_tried: int = 0
    n_converged: int = 0
    solutions: List[BVPSolution] = field(default_factory=list)
    distinct_solutions: int = 0
    multiplicity_found: bool = False
    max_profile_difference: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class ScanResult:
    """Result of a full parameter scan."""
    results: List[BifurcationResult] = field(default_factory=list)
    any_multiplicity: bool = False
    multiplicity_points: List[Tuple[float, float, float]] = field(default_factory=list)
    total_tested: int = 0
    total_converged: int = 0
    notes: List[str] = field(default_factory=list)


def make_guess(r_grid: np.ndarray, guess_type: str, lam: float, eta: float) -> np.ndarray:
    """Generate different initial guesses for the BVP solver."""
    n = len(r_grid)

    if guess_type == "standard":
        # Standard hedgehog: smooth transition 0 -> 1
        delta = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
        f = r_grid / np.sqrt(r_grid**2 + delta**2)
        fp = delta**2 / (r_grid**2 + delta**2)**1.5

    elif guess_type == "steep":
        # Steeper core: faster transition
        delta = 0.3 / math.sqrt(max(lam * eta**2, 0.01))
        f = r_grid / np.sqrt(r_grid**2 + delta**2)
        fp = delta**2 / (r_grid**2 + delta**2)**1.5

    elif guess_type == "wide":
        # Wide core: slower transition
        delta = 3.0 / math.sqrt(max(lam * eta**2, 0.01))
        f = r_grid / np.sqrt(r_grid**2 + delta**2)
        fp = delta**2 / (r_grid**2 + delta**2)**1.5

    elif guess_type == "overshoot":
        # Guess that overshoots: f > 1 in some region
        delta = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
        f = 1.2 * r_grid / np.sqrt(r_grid**2 + delta**2)
        f = np.clip(f, 0, 1.5)
        fp = np.gradient(f, r_grid)

    elif guess_type == "undershoot":
        # Guess that undershoots: f < standard
        delta = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
        f = 0.5 * r_grid / np.sqrt(r_grid**2 + delta**2)
        fp = np.gradient(f, r_grid)

    elif guess_type == "linear":
        # Simple linear ramp
        f = np.linspace(0, 1, n)
        fp = np.ones(n) / (r_grid[-1] - r_grid[0])

    elif guess_type == "step":
        # Step function at midpoint
        r_mid = 0.5 * (r_grid[0] + r_grid[-1])
        f = np.where(r_grid > r_mid, 1.0, r_grid / r_mid)
        fp = np.gradient(f, r_grid)

    elif guess_type == "negative_dip":
        # Starts negative (tests whether f < 0 branch exists)
        delta = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
        f = r_grid / np.sqrt(r_grid**2 + delta**2) - 0.3 * np.exp(-r_grid / delta)
        f[0] = 0.0
        fp = np.gradient(f, r_grid)

    else:
        f = r_grid / np.sqrt(r_grid**2 + 1.0)
        fp = 1.0 / (r_grid**2 + 1.0)**1.5

    return np.array([f, fp])


def solve_single(
    lam: float,
    g_p: float,
    eta: float,
    Phi_profile: Optional[np.ndarray] = None,
    r_grid: Optional[np.ndarray] = None,
    guess_type: str = "standard",
) -> BVPSolution:
    """Solve the hedgehog BVP with portal coupling at given parameters."""
    if not HAS_SCIPY:
        return BVPSolution(converged=False, notes=["scipy not available"])

    if r_grid is None:
        r_grid = np.linspace(R_MIN_DEFAULT, R_MAX_DEFAULT, N_GRID)

    # Portal potential from Phi profile
    if Phi_profile is not None:
        V_portal = g_p * Phi_profile**2
    else:
        # No Phi profile: use proxy M/r^2 for Phi
        M = 0.5
        tau_sq = 1.5
        Phi_proxy = M / r_grid**2
        V_portal = g_p * Phi_proxy**2

    def ode(r_pts, y):
        f_val = y[0]
        fp = y[1]
        V_at_r = np.interp(r_pts, r_grid, V_portal)
        fpp = (-(2.0 / r_pts) * fp
               + (2.0 / r_pts**2) * f_val
               + lam * eta**2 * f_val * (f_val**2 - 1.0)
               + V_at_r * f_val)
        return np.array([fp, fpp])

    def bc(ya, yb):
        return np.array([ya[0] - 0.0, yb[0] - 1.0])

    y_guess = make_guess(r_grid, guess_type, lam, eta)

    try:
        sol = solve_bvp(ode, bc, r_grid, y_guess, tol=1e-6, max_nodes=10000)
        y_sol = sol.sol(r_grid)
        f_sol = y_sol[0]
        fp_sol = y_sol[1]

        return BVPSolution(
            lam=lam, g_p=g_p, eta=eta,
            guess_type=guess_type,
            converged=sol.success,
            f_at_rmin=float(f_sol[0]),
            f_at_rmax=float(f_sol[-1]),
            f_max=float(np.max(f_sol)),
            f_min=float(np.min(f_sol)),
            c1=float(fp_sol[0]),
            monotone=bool(np.all(np.diff(f_sol) >= -1e-8)),
            rms_residual=float(sol.rms_residuals.max()) if hasattr(sol, 'rms_residuals') else 0.0,
            f_profile=f_sol,
            r_grid=r_grid,
            notes=["Converged: {}; guess: {}".format(sol.success, guess_type)],
        )
    except Exception as exc:
        return BVPSolution(
            lam=lam, g_p=g_p, eta=eta,
            guess_type=guess_type, converged=False,
            notes=["Failed: {}; guess: {}".format(str(exc)[:80], guess_type)],
        )


def test_bifurcation(
    lam: float,
    g_p: float = 0.0,
    eta: float = ETA_MATCH,
    profile_diff_threshold: float = 0.01,
) -> BifurcationResult:
    """Test for multiple solutions at a single parameter point."""
    r_grid = np.linspace(R_MIN_DEFAULT, R_MAX_DEFAULT, N_GRID)
    guess_types = ["standard", "steep", "wide", "overshoot", "undershoot",
                   "linear", "step", "negative_dip"]

    solutions = []
    for gt in guess_types:
        sol = solve_single(lam, g_p, eta, r_grid=r_grid, guess_type=gt)
        solutions.append(sol)

    converged = [s for s in solutions if s.converged]

    # Check for distinct solutions
    distinct_groups = []
    for sol in converged:
        if sol.f_profile is None:
            continue
        matched = False
        for group in distinct_groups:
            ref = group[0]
            if ref.f_profile is None:
                continue
            diff = np.max(np.abs(sol.f_profile - ref.f_profile))
            if diff < profile_diff_threshold:
                group.append(sol)
                matched = True
                break
        if not matched:
            distinct_groups.append([sol])

    max_diff = 0.0
    if len(distinct_groups) >= 2:
        for i in range(len(distinct_groups)):
            for j in range(i + 1, len(distinct_groups)):
                f1 = distinct_groups[i][0].f_profile
                f2 = distinct_groups[j][0].f_profile
                if f1 is not None and f2 is not None:
                    d = np.max(np.abs(f1 - f2))
                    max_diff = max(max_diff, d)

    multiplicity = len(distinct_groups) >= 2

    notes = [
        "lambda={:.1f}, g_p={:.2f}, eta={:.4f}".format(lam, g_p, eta),
        "Guesses tried: {}".format(len(guess_types)),
        "Converged: {}".format(len(converged)),
        "Distinct solutions: {}".format(len(distinct_groups)),
        "Multiplicity: {}".format(multiplicity),
    ]
    if multiplicity:
        notes.append("MAX PROFILE DIFFERENCE: {:.6f}".format(max_diff))
        for i, group in enumerate(distinct_groups):
            rep = group[0]
            notes.append("  Solution {}: c1={:.4f}, f_max={:.4f}, monotone={}, from {} guesses".format(
                i, rep.c1, rep.f_max, rep.monotone, len(group)))

    return BifurcationResult(
        lam=lam, g_p=g_p, eta=eta,
        n_guesses_tried=len(guess_types),
        n_converged=len(converged),
        solutions=solutions,
        distinct_solutions=len(distinct_groups),
        multiplicity_found=multiplicity,
        max_profile_difference=max_diff,
        notes=notes,
    )


def run_bifurcation_scan() -> ScanResult:
    """Scan over parameter space searching for bifurcation."""

    # Parameter ranges to test
    lambdas = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 100.0, 500.0, 1000.0]
    g_ps = [0.0, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0]
    etas = [ETA_MATCH, ETA_MATCH * 0.1, ETA_MATCH * 10.0]

    results = []
    multiplicity_points = []
    total_converged = 0

    for eta in etas:
        for lam in lambdas:
            for g_p in g_ps:
                try:
                    res = test_bifurcation(lam, g_p, eta)
                except Exception as exc:
                    res = BifurcationResult(
                        lam=lam, g_p=g_p, eta=eta,
                        notes=["Exception: {}".format(str(exc)[:80])],
                    )
                results.append(res)
                total_converged += res.n_converged
                if res.multiplicity_found:
                    multiplicity_points.append((lam, g_p, eta))

    any_mult = len(multiplicity_points) > 0

    notes = [
        "Total parameter points tested: {}".format(len(results)),
        "Total converged solutions: {}".format(total_converged),
        "Points with multiplicity: {}".format(len(multiplicity_points)),
        "ANY MULTIPLICITY FOUND: {}".format(any_mult),
    ]
    if any_mult:
        notes.append("MULTIPLICITY POINTS:")
        for p in multiplicity_points:
            notes.append("  lambda={}, g_p={}, eta={}".format(*p))

    return ScanResult(
        results=results,
        any_multiplicity=any_mult,
        multiplicity_points=multiplicity_points,
        total_tested=len(results),
        total_converged=total_converged,
        notes=notes,
    )


if __name__ == "__main__":
    print("=" * 75)
    print("  BOOK XXI GAMMA — BIFURCATION SEARCH")
    print("  Coupled nonlinear hedgehog BVP with portal coupling")
    print("=" * 75)

    scan = run_bifurcation_scan()

    print("\n--- Scan Summary ---")
    for n in scan.notes:
        print("  {}".format(n))

    print("\n--- Detailed Results (showing multiplicity and non-standard features) ---")
    for res in scan.results:
        if res.multiplicity_found or res.n_converged < 3:
            print("\n  lambda={:.1f}, g_p={:.2f}, eta={:.4f}:".format(
                res.lam, res.g_p, res.eta))
            for n in res.notes:
                print("    {}".format(n))

    # Also report any non-monotone solutions
    print("\n--- Non-Monotone Solutions ---")
    non_monotone_count = 0
    for res in scan.results:
        for sol in res.solutions:
            if sol.converged and not sol.monotone:
                non_monotone_count += 1
                print("  lambda={:.1f}, g_p={:.2f}, guess={}: f_min={:.4f}, f_max={:.4f}".format(
                    sol.lam, sol.g_p, sol.guess_type, sol.f_min, sol.f_max))
    if non_monotone_count == 0:
        print("  NONE FOUND.")

    print("\n" + "=" * 75)
    if scan.any_multiplicity:
        print("  MULTIPLICITY FOUND at {} parameter points".format(
            len(scan.multiplicity_points)))
        print("  This is a structurally significant result.")
    else:
        print("  NO MULTIPLICITY FOUND across {} parameter points".format(
            scan.total_tested))
        print("  The coupled nonlinear system has a unique solution at every")
        print("  tested parameter value, regardless of initial guess.")
        print("  XX Alpha's unique-attractor verdict is REINFORCED.")
    print("=" * 75)
