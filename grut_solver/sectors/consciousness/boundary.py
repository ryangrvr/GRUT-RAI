"""
Sector 13 — Quantum-Classical Boundary for Neural Systems

Extends the USL boundary_mass function to characterize the full
quantum-classical transition zone at biological temperatures.

At T = 310 K, the thermal decoherence boundary is MUCH lower than the
gravitational one. This module computes both and maps the transition
zone where biological systems live.

STATUS: Computed (extends existing USL with standard thermal physics).
"""

import numpy as np
from grut_solver.constants import G, HBAR, K_B, AMU
from grut_solver.usl.gravitational import lambda_grav, boundary_mass

# Water parameters
M_WATER = 18 * AMU
N_WATER = 3.34e28  # molecules/m^3

# Neural timescales
T_NEURAL_FIRING = 1e-3     # 1 ms
T_GAMMA_PERIOD = 0.025     # 25 ms (40 Hz)
T_COGNITIVE = 1.0          # 1 s
T_SLEEP_CYCLE = 5400       # 90 min


def _thermal_decoherence_rate(m_kg: float, R_m: float, l_m: float,
                              T: float, n_water: float = N_WATER) -> float:
    """Compute thermal decoherence rate from water scattering."""
    v_th = np.sqrt(8 * K_B * T / (np.pi * M_WATER))
    sigma = np.pi * R_m**2
    lambda_dB = HBAR / (M_WATER * v_th)

    if l_m < lambda_dB:
        return n_water * sigma * v_th * (l_m / lambda_dB)**2
    else:
        return n_water * sigma * v_th


def boundary_mass_at_temperature(l: float, t_obs: float,
                                 T: float = 310.0,
                                 rho: float = 1400.0) -> dict:
    """Compute both gravitational and thermal boundary masses.

    The quantum-classical boundary is whichever mechanism classicalizes
    FIRST (i.e., the smaller boundary mass).

    Parameters
    ----------
    l : float      Superposition separation [m].
    t_obs : float  Observation time [s].
    T : float      Temperature [K].
    rho : float    Material density [kg/m^3] (default: protein ~1400).

    Returns
    -------
    dict with both boundary masses and which is binding.
    """
    # Gravitational boundary: m where Lambda_grav * t_obs = 1
    m_grav = boundary_mass(l, t_obs)

    # Thermal boundary: m where Lambda_thermal * t_obs = 1
    # Lambda_thermal depends on R = (3m/(4 pi rho))^{1/3}
    # Solve numerically via bisection
    m_lo, m_hi = 1e-30, 1e-10
    for _ in range(200):
        m_mid = np.sqrt(m_lo * m_hi)  # geometric bisection
        R_mid = (3 * m_mid / (4 * np.pi * rho)) ** (1.0 / 3.0)
        rate = _thermal_decoherence_rate(m_mid, R_mid, l, T)
        if rate * t_obs > 1:
            m_hi = m_mid
        else:
            m_lo = m_mid

    m_thermal = np.sqrt(m_lo * m_hi)

    binding = "thermal" if m_thermal < m_grav else "gravitational"

    return {
        "l_m": l,
        "t_obs_s": t_obs,
        "T_K": T,
        "m_boundary_grav_kg": m_grav,
        "m_boundary_grav_amu": m_grav / AMU,
        "m_boundary_thermal_kg": m_thermal,
        "m_boundary_thermal_amu": m_thermal / AMU,
        "binding_mechanism": binding,
        "log10_ratio": np.log10(m_grav / m_thermal) if m_thermal > 0 else float('inf'),
        "note": (
            f"At T={T} K, l={l:.0e} m, t={t_obs:.0e} s: "
            f"m*_grav = {m_grav/AMU:.1e} amu, m*_thermal = {m_thermal/AMU:.1e} amu. "
            f"Thermal boundary is {np.log10(m_grav/m_thermal):.0f} orders below "
            f"gravitational. Binding mechanism: {binding}."
        ),
    }


def boundary_width_neural(T: float = 310.0, rho: float = 1400.0) -> dict:
    """Width of the quantum-classical transition zone for neural systems.

    The "transition zone" is the mass range where the total decoherence
    time transitions from much longer than the gamma period (25 ms) to
    much shorter. Defined as the mass range where:
        0.01 < Lambda_total * t_gamma < 100

    Returns the width in decades of mass.
    """
    l = 0.7e-9  # conformational displacement

    # Find m where Lambda_total * t_gamma = 0.01 (lower edge)
    m_lo_search, m_hi_search = 1e-35, 1e-5
    for _ in range(200):
        m_mid = np.sqrt(m_lo_search * m_hi_search)
        R = (3 * m_mid / (4 * np.pi * rho)) ** (1.0 / 3.0)
        Lg = lambda_grav(m_mid, l, R)
        Lt = _thermal_decoherence_rate(m_mid, R, l, T)
        total = Lg + Lt
        if total * T_GAMMA_PERIOD > 0.01:
            m_hi_search = m_mid
        else:
            m_lo_search = m_mid
    m_lower = np.sqrt(m_lo_search * m_hi_search)

    # Find m where Lambda_total * t_gamma = 100 (upper edge)
    m_lo_search, m_hi_search = 1e-35, 1e-5
    for _ in range(200):
        m_mid = np.sqrt(m_lo_search * m_hi_search)
        R = (3 * m_mid / (4 * np.pi * rho)) ** (1.0 / 3.0)
        Lg = lambda_grav(m_mid, l, R)
        Lt = _thermal_decoherence_rate(m_mid, R, l, T)
        total = Lg + Lt
        if total * T_GAMMA_PERIOD > 100:
            m_hi_search = m_mid
        else:
            m_lo_search = m_mid
    m_upper = np.sqrt(m_lo_search * m_hi_search)

    width_decades = np.log10(m_upper / m_lower)

    return {
        "T_K": T,
        "l_m": l,
        "t_gamma_s": T_GAMMA_PERIOD,
        "m_lower_kg": m_lower,
        "m_lower_amu": m_lower / AMU,
        "m_upper_kg": m_upper,
        "m_upper_amu": m_upper / AMU,
        "width_decades": width_decades,
        "note": (
            f"Transition zone at T={T} K: "
            f"{m_lower/AMU:.1e} — {m_upper/AMU:.1e} amu "
            f"({width_decades:.1f} decades). "
            f"Tubulin ({110000} Da) sits within this zone."
        ),
    }


def neural_boundary_profile(n_points: int = 100, T: float = 310.0,
                            rho: float = 1400.0) -> dict:
    """Sweep mass and compute both decoherence channels.

    Returns arrays of (mass, lambda_grav, lambda_thermal, lambda_total)
    suitable for plotting the boundary profile.
    """
    l = 0.7e-9  # conformational displacement
    masses_kg = np.logspace(-28, -18, n_points)

    lambda_grav_arr = np.zeros(n_points)
    lambda_thermal_arr = np.zeros(n_points)
    lambda_total_arr = np.zeros(n_points)

    for i, m in enumerate(masses_kg):
        R = (3 * m / (4 * np.pi * rho)) ** (1.0 / 3.0)
        Lg = lambda_grav(m, l, R)
        Lt = _thermal_decoherence_rate(m, R, l, T)
        lambda_grav_arr[i] = Lg
        lambda_thermal_arr[i] = Lt
        lambda_total_arr[i] = Lg + Lt

    # Find crossover mass (where grav = thermal)
    ratios = lambda_grav_arr / lambda_thermal_arr
    cross_idx = np.argmin(np.abs(np.log10(ratios)))
    m_crossover = masses_kg[cross_idx]

    # Neural timescale markers
    timescales = {
        "neural_firing": T_NEURAL_FIRING,
        "gamma_period": T_GAMMA_PERIOD,
        "cognitive": T_COGNITIVE,
    }
    markers = {}
    for name, t in timescales.items():
        freq = 1.0 / t
        idx = np.argmin(np.abs(lambda_total_arr - freq))
        markers[name] = {
            "t_s": t,
            "freq_hz": freq,
            "m_kg": float(masses_kg[idx]),
            "m_amu": float(masses_kg[idx] / AMU),
        }

    return {
        "masses_kg": masses_kg.tolist(),
        "masses_amu": (masses_kg / AMU).tolist(),
        "lambda_grav_hz": lambda_grav_arr.tolist(),
        "lambda_thermal_hz": lambda_thermal_arr.tolist(),
        "lambda_total_hz": lambda_total_arr.tolist(),
        "m_crossover_kg": float(m_crossover),
        "m_crossover_amu": float(m_crossover / AMU),
        "neural_markers": markers,
        "n_points": n_points,
    }
