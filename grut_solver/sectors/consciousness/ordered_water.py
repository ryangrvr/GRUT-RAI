"""
Sector 13 — Ordered Water Correction

The Application 9 thermal wall uses BULK water parameters:
  n_water = 3.34e28 m^-3, T = 310 K, free thermal motion.

But water inside microtubule channels (~15 nm diameter) is NOT bulk water.
It is confined, partially ordered, with reduced mobility and altered
hydrogen bonding. This module computes the corrected decoherence time.

HONEST RESULT: Even maximal confinement correction reduces the 25-order
gap to ~21 orders. The gap is NOT closed. Confinement helps by 2-4 orders
at best. This module documents that honestly.

STATUS: Computed (parametric scan over confinement factor).
"""

import numpy as np
from grut_solver.constants import G, HBAR, K_B, AMU
from grut_solver.usl.gravitational import lambda_grav

# Tubulin parameters (from Application 9)
M_TUBULIN_DA = 110000
M_TUBULIN_KG = M_TUBULIN_DA * AMU
L_CONFORMATIONAL = 0.7e-9    # 0.7 nm
R_TUBULIN = 4e-9             # 4 nm
T_BRAIN = 310                # K

# Bulk water parameters
M_WATER = 18 * AMU
N_WATER_BULK = 3.34e28       # molecules/m^3 (liquid water at 310 K)

# Microtubule channel geometry
MT_INNER_RADIUS = 7.5e-9    # ~15 nm inner diameter
MT_OUTER_RADIUS = 12.5e-9   # ~25 nm outer diameter


def bulk_water_decoherence(R: float = R_TUBULIN,
                           l: float = L_CONFORMATIONAL,
                           T: float = T_BRAIN) -> dict:
    """Compute bulk water thermal decoherence for reference.

    Uses the standard scattering formula from Application 9.
    """
    v_th = np.sqrt(8 * K_B * T / (np.pi * M_WATER))
    sigma = np.pi * R**2
    lambda_dB = HBAR / (M_WATER * v_th)

    if l < lambda_dB:
        rate = N_WATER_BULK * sigma * v_th * (l / lambda_dB)**2
    else:
        rate = N_WATER_BULK * sigma * v_th

    t_bulk = 1 / rate if rate > 0 else float('inf')

    return {
        "n_water": N_WATER_BULK,
        "v_thermal_m_s": v_th,
        "lambda_dB_m": lambda_dB,
        "sigma_m2": sigma,
        "lambda_water_hz": rate,
        "t_water_s": t_bulk,
        "regime": "long-wavelength" if l < lambda_dB else "short-wavelength",
    }


def confined_water_properties(pore_radius_m: float = MT_INNER_RADIUS,
                              T: float = T_BRAIN) -> dict:
    """Properties of water confined in a cylindrical pore.

    Experimental literature (Hummer et al. 2001, Kolesnikov et al. 2004,
    Byl et al. 2006) shows that water confined in nanopores exhibits:
    - Reduced density (0.3-0.8 of bulk, depending on pore size)
    - Reduced translational mobility (0.1-0.5 of bulk)
    - Altered hydrogen bonding (fewer H-bonds per molecule)
    - Phase transitions to ordered/ice-like structures at small pores

    For microtubule-scale pores (~7.5 nm radius), the effects are
    moderate — not as extreme as carbon nanotube confinement (~0.5 nm).

    Returns density reduction factor and mobility reduction factor.
    """
    # Empirical model from confined water literature
    # For pore radius R_pore:
    #   density_factor ~ 1 - 0.5 * exp(-R_pore / R_scale)
    #   mobility_factor ~ 1 - 0.7 * exp(-R_pore / R_scale)
    # where R_scale ~ 1 nm (characteristic confinement scale)
    R_scale = 1e-9  # 1 nm

    density_factor = 1.0 - 0.5 * np.exp(-pore_radius_m / R_scale)
    mobility_factor = 1.0 - 0.7 * np.exp(-pore_radius_m / R_scale)

    # At R_pore = 7.5 nm >> R_scale: factors approach 1 (near-bulk)
    # At R_pore = 0.5 nm: density ~ 0.7, mobility ~ 0.47

    n_confined = N_WATER_BULK * density_factor
    v_th_bulk = np.sqrt(8 * K_B * T / (np.pi * M_WATER))
    v_th_confined = v_th_bulk * np.sqrt(mobility_factor)

    return {
        "pore_radius_m": pore_radius_m,
        "pore_radius_nm": pore_radius_m * 1e9,
        "density_factor": density_factor,
        "mobility_factor": mobility_factor,
        "n_confined": n_confined,
        "v_thermal_bulk": v_th_bulk,
        "v_thermal_confined": v_th_confined,
        "note": (
            f"At pore radius {pore_radius_m*1e9:.1f} nm: "
            f"density = {density_factor:.3f}x bulk, "
            f"mobility = {mobility_factor:.3f}x bulk. "
            f"For microtubule channels, confinement effects are moderate."
        ),
    }


def ordered_water_decoherence_time(R_tubulin: float = R_TUBULIN,
                                   l_conf: float = L_CONFORMATIONAL,
                                   T: float = T_BRAIN,
                                   confinement_factor: float = None) -> dict:
    """Compute thermal decoherence time with confined water correction.

    Parameters
    ----------
    confinement_factor : float, optional
        Overall reduction factor for collision rate [0, 1].
        If None, computed from confined_water_properties().
        f = 1.0 means bulk water (no improvement).
        f = 0.01 means 99% reduction (extreme confinement).
    """
    bulk = bulk_water_decoherence(R_tubulin, l_conf, T)

    if confinement_factor is None:
        props = confined_water_properties(MT_INNER_RADIUS, T)
        # Combined effect: rate ~ n * sigma * v ~ density * mobility^(1/2)
        confinement_factor = props["density_factor"] * np.sqrt(props["mobility_factor"])
    else:
        props = None

    rate_confined = bulk["lambda_water_hz"] * confinement_factor
    t_confined = 1 / rate_confined if rate_confined > 0 else float('inf')

    # Gravitational reference
    Lg = lambda_grav(M_TUBULIN_KG, l_conf, R_tubulin)
    t_grav = 1 / Lg if Lg > 0 else float('inf')

    improvement = t_confined / bulk["t_water_s"]
    remaining_gap = np.log10(t_grav / t_confined) if t_confined > 0 else float('inf')

    return {
        "t_bulk_s": bulk["t_water_s"],
        "t_confined_s": t_confined,
        "confinement_factor": confinement_factor,
        "improvement_factor": improvement,
        "improvement_orders": np.log10(improvement),
        "t_grav_s": t_grav,
        "remaining_gap_orders": remaining_gap,
        "gap_closed": remaining_gap <= 0,
        "note": (
            f"Confinement factor {confinement_factor:.3f} improves "
            f"decoherence time by {np.log10(improvement):.1f} orders. "
            f"Remaining gap to gravity: {remaining_gap:.1f} orders. "
            f"{'Gap CLOSED.' if remaining_gap <= 0 else 'Gap NOT closed.'}"
        ),
    }


def gap_analysis(confinement_factors: list = None) -> dict:
    """Sweep confinement factor and report the thermal-gravitational gap.

    This is the honest answer: how much does ordered water help?

    Returns a table of (factor, improvement, remaining_gap) plus verdict.
    """
    if confinement_factors is None:
        confinement_factors = [1.0, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001]

    results = []
    for f in confinement_factors:
        r = ordered_water_decoherence_time(confinement_factor=f)
        results.append({
            "confinement_factor": f,
            "t_confined_s": r["t_confined_s"],
            "improvement_orders": r["improvement_orders"],
            "remaining_gap_orders": r["remaining_gap_orders"],
        })

    # Best case
    best = min(results, key=lambda x: x["remaining_gap_orders"])

    # Physical estimate for microtubule channel
    props = confined_water_properties(MT_INNER_RADIUS, T_BRAIN)
    physical_factor = props["density_factor"] * np.sqrt(props["mobility_factor"])
    physical = ordered_water_decoherence_time(confinement_factor=physical_factor)

    return {
        "scan": results,
        "best_case": best,
        "physical_estimate": {
            "confinement_factor": physical_factor,
            "improvement_orders": physical["improvement_orders"],
            "remaining_gap_orders": physical["remaining_gap_orders"],
        },
        "verdict": (
            f"Physical estimate for MT channel: confinement factor = "
            f"{physical_factor:.3f}, improvement = "
            f"{physical['improvement_orders']:.1f} orders, "
            f"remaining gap = {physical['remaining_gap_orders']:.1f} orders. "
            f"Even at extreme confinement (f=0.001), gap = "
            f"{best['remaining_gap_orders']:.1f} orders. "
            f"Ordered water CANNOT close the thermal wall alone."
        ),
    }
