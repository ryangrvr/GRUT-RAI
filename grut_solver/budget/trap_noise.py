"""Trap noise decoherence channels.

Optical trap: laser photon recoil heating.
Magnetic trap: Johnson noise from nearby conductors.
"""

import numpy as np
from grut_solver.constants import HBAR, C


def lambda_photon_recoil(P_laser: float, omega_laser: float,
                         R: float, l: float) -> float:
    """Decoherence from laser photon scattering in an optical trap [Hz].

    Each scattered photon transfers momentum ~hbar*omega/c.
    Rate of scattering ~ P_laser * sigma / (hbar omega).
    Decoherence per scatter ~ (l * hbar omega / c)^2 / hbar^2 = (l omega/c)^2.

    Parameters
    ----------
    P_laser : float     Laser power at the particle [W].
    omega_laser : float Angular frequency of trapping laser [rad/s].
    R : float           Particle radius [m].
    l : float           Superposition separation [m].
    """
    if P_laser <= 0 or omega_laser <= 0 or R <= 0 or l <= 0:
        return 0.0

    E_photon = HBAR * omega_laser
    sigma_scat = np.pi * R**2  # geometric (Rayleigh correction would apply for small R)
    scatter_rate = P_laser * sigma_scat / E_photon  # photons/s hitting particle

    # Each scatter gives decoherence ~ (l / lambda_photon)^2
    lambda_photon = 2 * np.pi * C / omega_laser
    if l < lambda_photon:
        decoh_per_scatter = (l / lambda_photon)**2
    else:
        decoh_per_scatter = 1.0

    return scatter_rate * decoh_per_scatter
