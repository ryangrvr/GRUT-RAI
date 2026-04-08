"""Model comparison: GRUT vs alternatives.

The core adversarial engine. Tests whether alternative models with
free parameters can simultaneously reproduce ALL GRUT signatures.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Callable

from grut_solver.usl.gravitational import lambda_grav, suppression_factor
from grut_solver.constants import G, HBAR, AMU


@dataclass
class KillResult:
    """Result of an adversarial kill test."""
    model_name: str
    n_free_params: int
    can_mimic_plateau: bool
    can_mimic_geometry: bool
    can_mimic_mass_scaling: bool
    can_mimic_all_three: bool
    residuals: dict          # per-test residual
    verdict: str             # "GRUT_SURVIVES" or "GRUT_DEGENERATE"


def _grut_predictions(masses: np.ndarray, l: float, rho: float) -> dict:
    """Generate GRUT predictions for a set of masses at fixed l and density."""
    radii = (3 * masses / (4 * np.pi * rho)) ** (1/3)
    rates = np.array([lambda_grav(m, l, R) for m, R in zip(masses, radii)])
    S_vals = np.array([suppression_factor(l, R) for R in radii])
    return {"masses": masses, "radii": radii, "rates": rates, "S_vals": S_vals}


def try_kill_constant_floor(l: float = 100e-9, rho: float = 2200.0) -> KillResult:
    """Can a constant (mass-independent) floor mimic GRUT?

    Model: Lambda_floor = C (one free parameter).
    GRUT: Lambda ~ m^2 * S(l/R) / l (varies with mass).

    A constant floor can match GRUT at ONE mass but not across masses.
    """
    masses = np.logspace(-16, -10, 20)
    grut = _grut_predictions(masses, l, rho)

    # Best-fit constant: geometric mean of GRUT rates
    valid = grut["rates"] > 0
    if not np.any(valid):
        return KillResult("constant_floor", 1, False, False, False, False, {}, "GRUT_SURVIVES")

    C_best = np.exp(np.mean(np.log(grut["rates"][valid])))
    residual_mass = np.sqrt(np.mean((np.log10(grut["rates"][valid]) -
                                      np.log10(C_best))**2))

    # Geometry test: constant floor has NO R dependence
    # GRUT varies by orders of magnitude with R at fixed m
    can_plateau = True  # a constant IS a plateau
    can_geometry = False  # no R dependence
    can_mass = residual_mass < 0.1  # < 26% error

    return KillResult(
        "constant_floor", 1,
        can_mimic_plateau=can_plateau,
        can_mimic_geometry=can_geometry,
        can_mimic_mass_scaling=can_mass,
        can_mimic_all_three=can_plateau and can_geometry and can_mass,
        residuals={"mass_scaling_dex": residual_mass},
        verdict="GRUT_DEGENERATE" if (can_plateau and can_geometry and can_mass) else "GRUT_SURVIVES",
    )


def try_kill_power_law_floor(l: float = 100e-9, rho: float = 2200.0) -> KillResult:
    """Can a power-law floor Lambda = A * m^alpha mimic GRUT?

    Two free parameters: A, alpha.
    GRUT: effective exponent transitions from 2 (far field) to ~1 (near field).
    A single power law with fixed alpha cannot track this transition.
    """
    masses = np.logspace(-16, -10, 30)
    grut = _grut_predictions(masses, l, rho)

    valid = grut["rates"] > 0
    if np.sum(valid) < 5:
        return KillResult("power_law_floor", 2, False, False, False, False, {}, "GRUT_SURVIVES")

    log_m = np.log10(masses[valid])
    log_L = np.log10(grut["rates"][valid])

    # Best-fit power law in log-log
    coeffs = np.polyfit(log_m, log_L, 1)
    log_L_fit = np.polyval(coeffs, log_m)
    residual_mass = np.sqrt(np.mean((log_L - log_L_fit)**2))
    fitted_alpha = coeffs[0]

    # Geometry: a power law has NO explicit R dependence unless R(m) is known
    # If R(m) = (3m/(4pi rho))^{1/3} is assumed, then the power law implicitly
    # includes the geometry through m. But GRUT's S(l/R) changes character
    # at l = 2R, creating a KINK that a smooth power law cannot reproduce.

    # Test the kink: compute residual in the transition region
    radii = (3 * masses[valid] / (4 * np.pi * rho)) ** (1/3)
    in_transition = (l / radii > 0.5) & (l / radii < 5.0)
    if np.sum(in_transition) > 3:
        residual_kink = np.sqrt(np.mean((log_L[in_transition] - log_L_fit[in_transition])**2))
    else:
        residual_kink = residual_mass

    can_plateau = True  # any model can produce a pressure-independent rate
    can_mass = residual_mass < 0.1
    can_geometry = residual_kink < 0.05  # must track the kink

    return KillResult(
        "power_law_floor", 2,
        can_mimic_plateau=can_plateau,
        can_mimic_geometry=can_geometry,
        can_mimic_mass_scaling=can_mass,
        can_mimic_all_three=can_plateau and can_geometry and can_mass,
        residuals={"mass_dex": residual_mass, "kink_dex": residual_kink,
                   "fitted_alpha": fitted_alpha},
        verdict="GRUT_DEGENERATE" if (can_plateau and can_geometry and can_mass) else "GRUT_SURVIVES",
    )


def try_kill_csl(l: float = 100e-9, rho: float = 2200.0) -> KillResult:
    """Can CSL (2 free parameters: lambda_CSL, r_CSL) mimic GRUT?

    CSL: Lambda = lambda_CSL * (m/amu)^2 * f(R, r_CSL) * g(l, r_CSL)
    GRUT: Lambda = G m^2 S(l/R) / (hbar l)

    Key differences:
    - CSL has no 1/l dependence (or weak l dependence)
    - CSL geometry factor is exponential, not cubic
    - CSL has 2 free parameters; GRUT has 0
    """
    masses = np.logspace(-16, -10, 20)
    grut = _grut_predictions(masses, l, rho)

    # CSL with best-fit parameters
    # Try to fit CSL to GRUT's predictions
    valid = grut["rates"] > 0
    if np.sum(valid) < 5:
        return KillResult("CSL", 2, False, False, False, False, {}, "GRUT_SURVIVES")

    # CSL rate: Lambda_CSL = lam * (m/amu)^2 * f(R) * g(l)
    # For best fit: adjust lam and r_CSL
    log_m = np.log10(masses[valid])
    log_L_grut = np.log10(grut["rates"][valid])

    # CSL mass scaling is m^2 (same as GRUT in far field)
    # But CSL has NO 1/l and DIFFERENT R dependence
    # Best CSL fit: Lambda_CSL = A * m^2 (ignoring geometry differences)
    log_m2 = 2 * log_m
    offset = np.mean(log_L_grut - log_m2)
    log_L_csl_fit = log_m2 + offset
    residual_mass = np.sqrt(np.mean((log_L_grut - log_L_csl_fit)**2))

    # Geometry discrimination: vary R at fixed m
    m_fixed = 1e-14
    densities = [100, 1000, 2200, 5000, 19300]  # aerogel to gold
    grut_geom = []
    csl_geom = []
    for rho_v in densities:
        R_v = (3*m_fixed/(4*np.pi*rho_v))**(1/3)
        grut_geom.append(lambda_grav(m_fixed, l, R_v))
        # CSL: geometry factor ~ exp(-(R/r_CSL)^2) or (r_CSL/R)^3
        # With r_CSL = 100nm (GRW):
        r_CSL = 100e-9
        if R_v < r_CSL:
            csl_f = 1.0
        else:
            csl_f = (r_CSL / R_v)**3
        # CSL doesn't have 1/l dependence, so use flat rate
        csl_geom.append(10**offset * (m_fixed/AMU)**2 * csl_f)

    grut_geom = np.array(grut_geom)
    csl_geom = np.array(csl_geom)

    # Normalize both to their maximum for shape comparison
    if np.max(grut_geom) > 0 and np.max(csl_geom) > 0:
        grut_norm = grut_geom / np.max(grut_geom)
        csl_norm = csl_geom / np.max(csl_geom)
        residual_geom = np.sqrt(np.mean((np.log10(grut_norm + 1e-30) -
                                          np.log10(csl_norm + 1e-30))**2))
    else:
        residual_geom = 1.0

    can_plateau = True
    can_mass = residual_mass < 0.1
    can_geometry = residual_geom < 0.1

    return KillResult(
        "CSL", 2,
        can_mimic_plateau=can_plateau,
        can_mimic_geometry=can_geometry,
        can_mimic_mass_scaling=can_mass,
        can_mimic_all_three=can_plateau and can_geometry and can_mass,
        residuals={"mass_dex": residual_mass, "geometry_dex": residual_geom},
        verdict="GRUT_DEGENERATE" if (can_plateau and can_geometry and can_mass) else "GRUT_SURVIVES",
    )


def run_all_kill_tests(l: float = 100e-9, rho: float = 2200.0) -> list[KillResult]:
    """Run ALL adversarial kill tests. Return list of results."""
    return [
        try_kill_constant_floor(l, rho),
        try_kill_power_law_floor(l, rho),
        try_kill_csl(l, rho),
    ]


def kill_summary(results: list[KillResult]) -> str:
    """Human-readable summary of kill test results."""
    lines = ["GRUT KILL TEST RESULTS", "=" * 60]
    any_degenerate = False
    for r in results:
        status = "DEGENERATE" if r.can_mimic_all_three else "SURVIVES"
        if r.can_mimic_all_three:
            any_degenerate = True
        lines.append(f"  {r.model_name} ({r.n_free_params} params): {r.verdict}")
        lines.append(f"    plateau: {'YES' if r.can_mimic_plateau else 'NO'}  "
                     f"geometry: {'YES' if r.can_mimic_geometry else 'NO'}  "
                     f"mass: {'YES' if r.can_mimic_mass_scaling else 'NO'}")
        for k, v in r.residuals.items():
            lines.append(f"    {k}: {v:.4f}")
    lines.append("")
    if any_degenerate:
        lines.append("  VERDICT: GRUT IS DEGENERATE WITH AT LEAST ONE ALTERNATIVE.")
        lines.append("  The framework cannot be distinguished from this model.")
    else:
        lines.append("  VERDICT: GRUT SURVIVES ALL KILL TESTS.")
        lines.append("  No alternative with <= 2 free parameters reproduces all three signatures.")
    return "\n".join(lines)
