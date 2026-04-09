"""
Module 1: Constitutive QM — base objects and dimensional bookkeeping.

The directed-response constitutive law:
    (tau_R + i tau_I) d_t z = z_target[z] - z

with tau_I = hbar/2 and z_target = delta F / delta z*.
"""

import numpy as np
from grut_solver.constants import HBAR, TAU_I


def constitutive_params(m: float, V: np.ndarray = None) -> dict:
    """Return the constitutive parameters for a particle of mass m.

    Parameters
    ----------
    m : float       Particle mass [kg].
    V : ndarray     Potential energy on the spatial grid [J]. Optional.

    Returns
    -------
    dict with tau_I, c_0, c_2, and derived quantities.
    """
    tau_I = TAU_I
    c_2 = tau_I**2 / m
    c_0 = 1.0  # constitutive fixed point (no potential)

    return {
        "tau_I": tau_I,
        "tau_R": 0.0,          # unitary limit
        "c_2": c_2,
        "c_0": c_0,
        "m": m,
        "hbar": HBAR,
        "hbar_check": 2 * tau_I,   # should equal HBAR
    }


def z_target_free(z: np.ndarray, c_2: float, dx: float) -> np.ndarray:
    """Compute z_target for a free particle: z_target = z - c_2 nabla^2 z.

    Uses second-order central finite differences with periodic BC.
    """
    z_xx = (np.roll(z, -1) + np.roll(z, 1) - 2 * z) / dx**2
    return z - c_2 * z_xx


def z_target_potential(z: np.ndarray, c_0: np.ndarray, c_2: float,
                       dx: float) -> np.ndarray:
    """Compute z_target with potential: z_target = c_0(x) z - c_2 nabla^2 z.

    c_0(x) = 1 + V(x)/2 in the constitutive convention.
    """
    z_xx = (np.roll(z, -1) + np.roll(z, 1) - 2 * z) / dx**2
    return c_0 * z - c_2 * z_xx


def constitutive_rhs(z: np.ndarray, z_tgt: np.ndarray,
                     tau_R: float, tau_I: float) -> np.ndarray:
    """RHS of the constitutive equation: d_t z = (z_target - z) / (tau_R + i tau_I)."""
    tau = tau_R + 1j * tau_I
    return (z_tgt - z) / tau
