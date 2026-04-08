"""Blackbody photon decoherence channel.

Emission from internal temperature and scattering from environmental photons.
Joos-Zeh / Chang et al formulation.
"""

import numpy as np
from grut_solver.constants import HBAR, K_B, C, SIGMA_SB


def lambda_bb_scatter(R: float, l: float, T_env: float) -> float:
    """Blackbody photon scattering decoherence [Hz].

    Rayleigh regime (R << lambda_thermal):
      Lambda ~ (c/lambda_th) * (R/lambda_th)^6 * (l/lambda_th)^2 * prefactor

    Geometric regime (R >> lambda_thermal):
      Lambda ~ n_photon * sigma_geom * c * min(1, (l*kT/(hbar c))^2)

    Parameters
    ----------
    R : float       Particle radius [m].
    l : float       Superposition separation [m].
    T_env : float   Environment temperature [K].
    """
    if T_env < 1e-6 or R <= 0 or l <= 0:
        return 0.0

    lambda_th = HBAR * C / (K_B * T_env)
    r_ratio = R / lambda_th
    l_ratio = l / lambda_th

    if r_ratio < 0.1:
        # Rayleigh regime: Lambda ~ prefactor * (c/lambda_th) * r^6 * l^2
        # prefactor from Joos-Zeh: 8 * pi^5 * 8 * 8! / 9 ~ 1.07e7
        prefactor = 8.0 * np.pi**5 * 8.0 * 40320.0 / 9.0
        return prefactor * (C / lambda_th) * r_ratio**6 * l_ratio**2
    else:
        # Geometric regime
        n_photon = 2.404 * (K_B * T_env)**3 / (np.pi**2 * (HBAR * C)**3)
        sigma_geom = np.pi * R**2
        return n_photon * sigma_geom * C * min(1.0, l_ratio**2)


def lambda_bb_emission(R: float, T_int: float) -> float:
    """Blackbody emission decoherence [Hz].

    Thermal photon emission from the particle's internal temperature.
    Each emitted photon carries momentum ~ kT/c, giving a recoil.
    Rate ~ (total radiated power) / (energy per photon).

    This is typically subdominant unless T_int >> T_env.
    """
    if T_int < 1e-6 or R <= 0:
        return 0.0

    P_rad = SIGMA_SB * T_int**4 * 4 * np.pi * R**2  # total radiated power [W]
    E_photon = K_B * T_int                             # typical photon energy [J]

    if E_photon <= 0:
        return 0.0

    return P_rad / E_photon  # emission rate [Hz]
