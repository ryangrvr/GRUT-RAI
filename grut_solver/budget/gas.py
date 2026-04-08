"""Gas collision decoherence channel.

Based on Hornberger-Sipe scattering theory and Joos-Zeh momentum transfer.
"""

import numpy as np
from grut_solver.constants import HBAR, K_B, M_N2


def lambda_gas(m: float, R: float, l: float, T: float, P: float,
               m_gas: float = None) -> float:
    """Gas collision decoherence rate [Hz].

    In the long-wavelength limit (l << lambda_dB_gas):
      Lambda_gas = n * sigma * v_th * (l / lambda_dB)^2

    In the short-wavelength limit (l >> lambda_dB_gas):
      Lambda_gas = n * sigma * v_th  (saturated)

    Parameters
    ----------
    m : float   Particle mass [kg] (unused in geometric cross-section limit).
    R : float   Particle radius [m].
    l : float   Superposition separation [m].
    T : float   Gas temperature [K].
    P : float   Gas pressure [Pa].
    m_gas : float, optional  Gas molecule mass [kg]. Default: N2.

    Returns
    -------
    float   Decoherence rate [Hz].
    """
    if m_gas is None:
        m_gas = M_N2
    if P <= 0 or T <= 0 or R <= 0 or l <= 0:
        return 0.0

    n = P / (K_B * T)                                    # number density [m^-3]
    v_th = np.sqrt(8 * K_B * T / (np.pi * m_gas))       # mean thermal speed [m/s]
    sigma = np.pi * R**2                                  # geometric cross section [m^2]
    lambda_dB = HBAR / (m_gas * v_th)                     # thermal de Broglie [m]

    if l < lambda_dB:
        return n * sigma * v_th * (l / lambda_dB)**2
    else:
        return n * sigma * v_th
