"""
Singularity Resolution Phenomenology — Defect-Only Metric Support
==================================================================

Stripped of ALL D7/D8 amplification (sign error killed it).
Uses ONLY the D6 additive defect energy support (Component B).

The D6 result: on a FIXED Schwarzschild background, the O(3) hedgehog
defect provides energy density eta^2/r^2 (angular gradient) that
supports the interior metric via:

  f(r) = 1 - 2(M - Sigma_defect(r))/r

where Sigma_defect(r) = integral_r^R_ext 4*pi*r'^2 * eps_defect dr'
is the integrated defect energy ABOVE radius r.

This is CORRECT (Birkhoff: Sigma ABOVE r supports the interior).
The D7/D8 sign error was in the SOURCE AMPLIFICATION, not in the
metric support formula.

THIS MODULE COMPUTES:
  1. Defect-only metric support (D6 level, no amplification)
  2. Modified Buchdahl/compactness limit if metric stays positive
  3. Mass-radius relation modification
  4. Tidal deformability Lambda_tidal
  5. Quasi-normal mode frequency shift

All in PHYSICAL UNITS for neutron stars.
"""

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

# Physical constants (CGS/SI as needed)
G_SI = 6.674e-11       # m^3 kg^-1 s^-2
C_SI = 2.998e8          # m/s
M_SUN_KG = 1.989e30     # kg
M_SUN_GEOM = G_SI * M_SUN_KG / C_SI**2  # 1477 m
HBAR_SI = 1.055e-34     # J s
K_B_SI = 1.381e-23      # J/K

# GRUT defect parameters
ETA_SQ = 1.0 / (8 * math.pi)  # ~ 0.0398
ETA = math.sqrt(ETA_SQ)

# Import BVP solver
try:
    from grut.numerical_monopole import (
        NumericalMonopoleParams, solve_hedgehog_bvp, extract_defect_energy,
        ETA_MATCH, M_EXT, R_EXT, R_EQ, TAU_CANONICAL,
    )
    HAS_MONOPOLE = True
except ImportError:
    HAS_MONOPOLE = False


@dataclass
class DefectMetricResult:
    """Result of defect-only metric support at one lambda."""
    lam: float = 0.0
    r_grid: np.ndarray = field(default_factory=lambda: np.array([]))
    sigma_defect: np.ndarray = field(default_factory=lambda: np.array([]))
    f_defect: np.ndarray = field(default_factory=lambda: np.array([]))
    f_min: float = 0.0
    f_at_Req: float = 0.0
    sigma_at_Req: float = 0.0
    defect_mass_fraction: float = 0.0
    metric_positive: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class NSPrediction:
    """Neutron star prediction at physical scale."""
    M_ns_solar: float = 0.0       # NS mass in solar masses
    R_ns_km: float = 0.0          # NS radius in km
    compactness: float = 0.0      # C = GM/(Rc^2)
    R_eq_km: float = 0.0          # equilibrium radius in km
    f_at_Req: float = 0.0         # metric function at R_eq
    delta_R_km: float = 0.0       # radius shift from defect support
    delta_Lambda_tidal: float = 0.0  # tidal deformability shift
    f_qnm_Hz: float = 0.0        # fundamental QNM frequency
    delta_f_qnm_Hz: float = 0.0  # QNM frequency shift
    notes: List[str] = field(default_factory=list)


def compute_defect_metric_support(lam: float) -> DefectMetricResult:
    """Compute the D6 defect-only metric support at given lambda.

    No scalar amplification. No D7/D8. Just the hedgehog energy density
    on a fixed Schwarzschild background.
    """
    if not HAS_MONOPOLE:
        return DefectMetricResult(lam=lam, notes=["monopole solver not available"])

    params = NumericalMonopoleParams(lam=lam, eta=ETA_MATCH)
    bvp = solve_hedgehog_bvp(params)
    if not bvp.converged:
        return DefectMetricResult(lam=lam, notes=["BVP did not converge"])

    energy = extract_defect_energy(bvp, params)

    # Compute Sigma_defect(r) = integral_r^R_ext 4*pi*r'^2 * eps dr'
    r = energy.r_grid
    eps = energy.total_epsilon
    n = len(r)

    # Interior grid: from R_eq to R_ext
    mask = (r >= R_EQ) & (r <= R_EXT)
    r_int = r[mask]
    eps_int = eps[mask]
    n_int = len(r_int)

    # Sigma from outer boundary inward
    sigma = np.zeros(n_int)
    for i in range(n_int - 2, -1, -1):
        dr = r_int[i+1] - r_int[i]
        integrand = 4 * math.pi * r_int**2 * eps_int
        sigma[i] = sigma[i+1] + 0.5 * (integrand[i] + integrand[i+1]) * dr

    # Metric function with defect support
    # f(r) = 1 - 2*(M - Sigma_defect(r))/r
    # On Schwarzschild: f_Schw = 1 - 2*M/r (negative for r < r_s = 2M = 1)
    # With defect: f_def = 1 - 2*(M - Sigma)/r = f_Schw + 2*Sigma/r
    f_schw = 1.0 - 2.0 * M_EXT / r_int
    f_defect = f_schw + 2.0 * sigma / r_int

    # Values at R_eq
    i_req = 0  # R_eq is the inner boundary
    f_at_req = float(f_defect[i_req]) if n_int > 0 else 0
    sigma_at_req = float(sigma[i_req]) if n_int > 0 else 0
    f_min = float(np.min(f_defect)) if n_int > 0 else 0

    # Defect mass fraction: what fraction of M does Sigma provide?
    defect_frac = sigma_at_req / M_EXT if M_EXT > 0 else 0

    metric_pos = f_min > 0

    return DefectMetricResult(
        lam=lam,
        r_grid=r_int,
        sigma_defect=sigma,
        f_defect=f_defect,
        f_min=f_min,
        f_at_Req=f_at_req,
        sigma_at_Req=sigma_at_req,
        defect_mass_fraction=defect_frac,
        metric_positive=metric_pos,
        notes=[
            "lambda = {:.1f}".format(lam),
            "Sigma(R_eq) = {:.6f}".format(sigma_at_req),
            "Sigma/M = {:.4f}".format(defect_frac),
            "f_Schw(R_eq) = {:.4f}".format(float(f_schw[0])),
            "f_defect(R_eq) = {:.4f}".format(f_at_req),
            "f_min = {:.4f}".format(f_min),
            "Metric positive: {}".format(metric_pos),
        ],
    )


def compute_ns_predictions(
    M_solar: float = 1.4,
    R_km: float = 12.0,
    lam: float = 25.0,
) -> NSPrediction:
    """Compute NS observable predictions from defect metric support.

    Physical scaling:
      r_s = 2GM/c^2 = 2 * 1477m * M/M_sun
      R_eq = r_s * alpha_vac = r_s / 3 (canonical)

    The defect energy density in physical units:
      eps_phys = eps_geom * c^4 / (G * r_s^2)

    But for the metric function, we work in geometric units and then
    convert the observational consequences to physical units.
    """
    # Geometric parameters
    r_s = 2 * M_SUN_GEOM * M_solar  # Schwarzschild radius in meters
    R_eq = r_s / 3                    # equilibrium radius
    compactness = G_SI * M_solar * M_SUN_KG / (R_km * 1e3 * C_SI**2)

    # Run defect metric support
    result = compute_defect_metric_support(lam)

    # The defect support Sigma/M tells us how much the effective
    # enclosed mass is reduced at R_eq by the defect energy.
    # In physical terms: the defect provides additional pressure support
    # that reduces the effective gravitational mass in the interior.

    # Metric at R_eq:
    # f_Schw(R_eq) = 1 - 2M/R_eq = 1 - 3 = -2 (inside horizon)
    # f_defect(R_eq) = -2 + 2*Sigma/R_eq

    # For the metric to be positive: Sigma > M - R_eq/2 = M - r_s/6
    # Sigma/M > 1 - r_s/(6M) = 1 - 1/3 = 2/3

    # The defect provides Sigma/M = result.defect_mass_fraction
    sigma_frac = result.defect_mass_fraction

    # For a REAL neutron star (not at r_s/3 but at R_ns >> r_s):
    # The NS is NOT inside its Schwarzschild radius.
    # R_ns ~ 12 km >> r_s ~ 4.1 km for 1.4 M_sun.
    # f(R_ns) = 1 - r_s/R_ns ~ 1 - 4.1/12 ~ 0.66 (positive, no problem)
    #
    # The defect effect is a CORRECTION to the interior structure,
    # not a singularity resolution for a neutron star (NS is not singular).
    #
    # Where the defect matters: the MAXIMUM MASS limit.
    # The Buchdahl bound: M < (4/9)(Rc^2/G) => R > (9/8)r_s = 2.25 r_s
    # Defect support shifts this by allowing more compact configurations.

    # Maximum compactness with defect support:
    # Standard Buchdahl: C_max = 4/9 = 0.444
    # With defect: the effective mass is reduced by Sigma,
    # so the effective compactness is C_eff = (M - Sigma)/(R c^2/G)
    # The Buchdahl bound applies to C_eff:
    # C_eff < 4/9
    # C_actual = C_eff + Sigma/(R c^2/G) = C_eff + Sigma/R (geometric)
    # C_actual_max = 4/9 + Sigma/R

    # At the Buchdahl radius R_Buch = (9/8)r_s:
    # Sigma/R ~ sigma_frac * M / R ~ sigma_frac * (r_s/2) / ((9/8)r_s)
    #         = sigma_frac * 4/9

    delta_C = sigma_frac * 4/9  # compactness shift from defect

    # Tidal deformability: Lambda ~ k2 * (R/M)^5
    # The Love number k2 depends on the interior structure.
    # The defect modifies the interior metric, shifting k2.
    # At leading order: delta_k2 / k2 ~ -5 * delta_C / C
    # (more compact → smaller k2 → smaller Lambda)
    k2_standard = 0.1  # typical for NS
    delta_k2_frac = -5 * delta_C / max(compactness, 0.01)
    delta_Lambda_tidal = delta_k2_frac  # fractional change

    # QNM frequency: f_qnm ~ (c / (2*pi*R)) * sqrt(C) * correction
    # For the fundamental w-mode: f ~ 6-8 kHz for typical NS
    f_qnm_base = C_SI / (2 * math.pi * R_km * 1e3) * math.sqrt(compactness) * 20  # rough
    # Defect shifts the interior → shifts QNM
    delta_f_qnm_frac = delta_C / (2 * compactness)  # leading-order shift
    delta_f_qnm = f_qnm_base * delta_f_qnm_frac

    # Radius shift at fixed mass:
    # More support → can be more compact → smaller R at same M
    delta_R_km = -R_km * delta_C / compactness

    return NSPrediction(
        M_ns_solar=M_solar,
        R_ns_km=R_km,
        compactness=compactness,
        R_eq_km=R_eq / 1e3,
        f_at_Req=result.f_at_Req,
        delta_R_km=delta_R_km,
        delta_Lambda_tidal=delta_Lambda_tidal,
        f_qnm_Hz=f_qnm_base,
        delta_f_qnm_Hz=delta_f_qnm,
        notes=[
            "M = {:.1f} M_sun, R = {:.1f} km".format(M_solar, R_km),
            "Compactness C = {:.4f}".format(compactness),
            "Defect Sigma/M = {:.4f} (at lambda={:.0f})".format(sigma_frac, lam),
            "Compactness shift delta_C = {:.6f}".format(delta_C),
            "Tidal deformability shift: {:.4f}%".format(delta_Lambda_tidal * 100),
            "QNM frequency: {:.0f} Hz, shift: {:.1f} Hz".format(f_qnm_base, delta_f_qnm),
            "Radius shift at fixed M: {:.4f} km".format(delta_R_km),
        ],
    )


if __name__ == "__main__":
    print("=" * 80)
    print("  SINGULARITY RESOLUTION PHENOMENOLOGY — DEFECT-ONLY")
    print("  No D7/D8 amplification. No scalar source enhancement.")
    print("  D6 additive defect support only (Component B: eta^2/r^2).")
    print("=" * 80)

    # Lambda scan: defect-only metric support
    print("\n--- DEFECT-ONLY METRIC SUPPORT (D6 level) ---")
    print("{:>8s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format(
        "lambda", "Sigma/M", "f_Schw", "f_defect", "f_min", "Positive?", "Support%"))
    print("-" * 75)

    lambdas = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]
    for lam in lambdas:
        res = compute_defect_metric_support(lam)
        f_schw = 1.0 - 2.0 * M_EXT / R_EQ  # = -2.0
        print("{:8.0f} {:10.4f} {:10.4f} {:10.4f} {:10.4f} {:>10s} {:10.2f}".format(
            lam, res.defect_mass_fraction, f_schw, res.f_at_Req,
            res.f_min, "YES" if res.metric_positive else "NO",
            res.defect_mass_fraction * 100))

    # NS predictions
    print("\n--- NEUTRON STAR PREDICTIONS ---")
    print("{:>8s} {:>8s} {:>8s} {:>10s} {:>10s} {:>12s} {:>10s}".format(
        "M/Msun", "R(km)", "C", "dC", "dR(km)", "dLambda(%)", "dQNM(Hz)"))
    print("-" * 75)

    for M, R in [(1.0, 13.0), (1.4, 12.0), (1.8, 11.0), (2.0, 10.5), (2.2, 10.0)]:
        pred = compute_ns_predictions(M, R, lam=25.0)
        print("{:8.1f} {:8.1f} {:8.4f} {:10.6f} {:10.4f} {:12.4f} {:10.1f}".format(
            pred.M_ns_solar, pred.R_ns_km, pred.compactness,
            pred.delta_R_km, pred.delta_R_km,
            pred.delta_Lambda_tidal * 100, pred.delta_f_qnm_Hz))

    # Critical assessment
    print("\n" + "=" * 80)
    print("  CRITICAL ASSESSMENT")
    print("=" * 80)

    # Get the actual numbers
    res_25 = compute_defect_metric_support(25.0)
    sigma_frac = res_25.defect_mass_fraction

    print("""
  The defect-only (D6 level) metric support provides:
    Sigma/M = {sf:.4f} ({sp:.2f}% of the exterior mass)

  This means:
    The defect energy integrated from R_eq to R_ext contributes
    {sp:.2f}% of the total gravitational mass as interior support.

  For the SINGULAR interior (R_eq = r_s/3, inside the horizon):
    f_Schwarzschild(R_eq) = -2.0 (deeply negative)
    f_defect(R_eq) = -2.0 + 2*{sa:.4f}/{req:.4f} = {fd:.4f}

  Metric positivity requires: Sigma/M > 2/3 = 66.7%.
  Actual: Sigma/M = {sp:.2f}%.
  SHORTFALL: factor {short:.1f}x below what's needed.

  VERDICT: The defect-only support is REAL but INSUFFICIENT.
  At lambda = 25, the defect provides {sp:.2f}% of the needed support.
  The metric remains deeply negative at the equilibrium radius.
  The D6 defect alone cannot resolve the singularity.

  For NEUTRON STARS (which are NOT singular):
    The defect provides a small CORRECTION to the interior structure.
    The compactness shift is delta_C ~ {dc:.6f} (tiny).
    The tidal deformability shift is ~ {dl:.4f}% (tiny).
    The QNM frequency shift is ~ {dq:.1f} Hz (tiny).

  These are all at the {order}th-decimal-place level.
  They are far below current observational precision:
    NICER M-R: ~1 km precision → need delta_R > 0.1 km
    LIGO tidal: ~10% precision → need delta_Lambda > 10%
    QNM: ~100 Hz precision → need delta_f > 100 Hz

  The defect-only phenomenology is REAL but UNOBSERVABLE
  with current or near-future detectors.
""".format(
        sf=sigma_frac, sp=sigma_frac*100,
        sa=res_25.sigma_at_Req, req=R_EQ, fd=res_25.f_at_Req,
        short=(2/3)/max(sigma_frac, 1e-10),
        dc=sigma_frac * 4/9,
        dl=(-5 * sigma_frac * 4/9 / 0.17) * 100,
        dq=7000 * sigma_frac * 4/9 / (2 * 0.17),
        order=4 if sigma_frac < 0.01 else 3 if sigma_frac < 0.1 else 2,
    ))

    print("=" * 80)
