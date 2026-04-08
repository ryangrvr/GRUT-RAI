"""
GRUT USL — Unified Scaling Laws

ALL scaling relations in one place. The universality of scaling is the
organizing principle of the entire framework.
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, AMU
from grut_solver.usl.gravitational import lambda_grav, suppression_factor, boundary_mass


# =============================================================================
# MASS SCALING
# =============================================================================

def mass_scaling_exponent(m: float, l: float, rho: float) -> float:
    """Effective mass-scaling exponent d(log Lambda)/d(log m) at given (m, l, rho).

    In the point-mass limit (l >> 2R): exponent = 2.0 exactly (Lambda ~ m^2).
    In the near-field (l << 2R): exponent ~ 1.0 (Lambda ~ m * (l/R)^3 / l).
    The extended-body correction reduces the effective exponent for large m.

    Parameters
    ----------
    m : float
        Mass [kg].
    l : float
        Superposition separation [m].
    rho : float
        Material density [kg/m^3].

    Returns
    -------
    float
        Effective local mass-scaling exponent (between 1 and 2).
    """
    R = (3 * m / (4 * np.pi * rho)) ** (1.0 / 3.0)
    ratio = l / R

    if ratio >= 2.0:
        # Far field: Lambda ~ m^2/l, slope = 2
        return 2.0
    else:
        # Near field: Lambda ~ m^2 * (l/R)^3 / l
        # R ~ m^{1/3}, so (l/R)^3 ~ m^{-1}
        # Lambda ~ m^2 * m^{-1} / l = m/l, slope = 1
        # Transition region: interpolate
        # Exact: d(log Lambda)/d(log m) = 2 + d(log S)/d(log m)
        # S = (l/R)^3 / 6, R = (3m/(4pi rho))^{1/3}
        # d(log S)/d(log m) = 3 * d(log(l/R))/d(log m) = 3 * (-1/3) = -1
        # So effective exponent = 2 - 1 = 1 in the deep near-field
        # Smooth transition around ratio ~ 2
        return 2.0 - (1.0 - ratio / 2.0)  # linear interpolation


# =============================================================================
# GEOMETRY SCALING
# =============================================================================

def geometry_scaling_table(m: float, l: float, densities: dict[str, float]) -> dict:
    """GRUT prediction for same-mass, different-density particles.

    This is the F2 discriminant: Lambda depends on R (through density)
    even at fixed mass. Point-mass models predict no R dependence.

    Parameters
    ----------
    m : float
        Mass [kg] (same for all materials).
    l : float
        Superposition separation [m].
    densities : dict
        Material name -> density [kg/m^3].

    Returns
    -------
    dict
        Material name -> {R, S, lambda_grav, lambda_point, ratio}.
    """
    results = {}
    lambda_pt = G * m**2 / (HBAR * l)

    for name, rho in densities.items():
        R = (3 * m / (4 * np.pi * rho)) ** (1.0 / 3.0)
        S = suppression_factor(l, R)
        lam = lambda_pt * S

        results[name] = {
            "R_m": R,
            "R_nm": R * 1e9,
            "S": S,
            "lambda_grav": lam,
            "lambda_point": lambda_pt,
            "grut_over_dp": S,  # ratio Lambda_GRUT / Lambda_DP
        }

    return results


# =============================================================================
# PRESSURE SCALING (CROSSOVER)
# =============================================================================

def crossover_pressure(m: float, R: float, l: float, T: float,
                       m_gas: float = None) -> float:
    """Pressure at which gas decoherence equals gravitational decoherence.

    Below this pressure, the GRUT gravitational signal dominates.
    Above it, gas collisions mask the signal.

    Parameters
    ----------
    m : float
        Particle mass [kg].
    R : float
        Particle radius [m].
    l : float
        Superposition separation [m].
    T : float
        Gas temperature [K].
    m_gas : float, optional
        Gas molecule mass [kg]. Default: N2.

    Returns
    -------
    float
        Crossover pressure P* [Pa].
    """
    from grut_solver.constants import K_B, M_N2
    if m_gas is None:
        m_gas = M_N2

    # Lambda_grav = G m^2 S(l/R) / (hbar l)
    S = suppression_factor(l, R)
    Lg = G * m**2 * S / (HBAR * l)

    # Lambda_gas ~ n * sigma * v_th * (l/lambda_dB)^2
    # n = P / (kT)
    # sigma = pi R^2
    # v_th = sqrt(8 kT / (pi m_gas))
    # lambda_dB = hbar / (m_gas v_th)
    v_th = np.sqrt(8 * K_B * T / (np.pi * m_gas))
    sigma = np.pi * R**2
    lambda_dB = HBAR / (m_gas * v_th)

    if l < lambda_dB:
        # Lambda_gas = (P / kT) * sigma * v_th * (l / lambda_dB)^2
        coeff = sigma * v_th * (l / lambda_dB)**2 / (K_B * T)
    else:
        coeff = sigma * v_th / (K_B * T)

    if coeff <= 0:
        return float('inf')

    return Lg / coeff


# =============================================================================
# FULL SCALING SUMMARY
# =============================================================================

def scaling_summary(m: float, l: float, R: float) -> dict:
    """Complete scaling summary for a given (m, l, R).

    Returns all GRUT scaling predictions in one dict.
    """
    S = suppression_factor(l, R)
    Lg = lambda_grav(m, l, R)
    Lpt = G * m**2 / (HBAR * l)

    return {
        "m_kg": m,
        "m_amu": m / AMU,
        "l_m": l,
        "l_nm": l * 1e9,
        "R_m": R,
        "R_nm": R * 1e9,
        "l_over_R": l / R,
        "S_extended": S,
        "lambda_grav_hz": Lg,
        "lambda_point_hz": Lpt,
        "t_coherence_s": 1.0 / Lg if Lg > 0 else float('inf'),
        "suppression_factor_x": 1.0 / S if S > 0 else float('inf'),
        "regime": "far-field" if l >= 2 * R else "near-field",
    }
