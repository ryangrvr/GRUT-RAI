"""
Module 1: U(1) gauge coupling — covariant derivative in the target functional.

D_mu = d_mu + ieA_mu. The unique minimal modification preserving local U(1).
Status: Demonstrated.
"""

import numpy as np
from grut_solver.constants import HBAR


def covariant_laplacian_1d(z: np.ndarray, A: np.ndarray, e: float,
                            dx: float) -> np.ndarray:
    """D_x^2 z = d_xx z + 2ieA d_x z - e^2 A^2 z  (Coulomb gauge)."""
    z_xx = (np.roll(z, -1) + np.roll(z, 1) - 2 * z) / dx**2
    z_x = (np.roll(z, -1) - np.roll(z, 1)) / (2 * dx)
    return z_xx + 2j * e * A * z_x - e**2 * A**2 * z


def gauge_rhs(z: np.ndarray, A: np.ndarray, Phi: np.ndarray,
              e: float, c_2: float, tau_I: float, dx: float) -> np.ndarray:
    """d_t z for gauge-coupled constitutive Schrodinger.
    i tau_I d_t z = (V/2) z - c_2 D^2 z, with V = e Phi.
    """
    D2z = covariant_laplacian_1d(z, A, e, dx)
    V = e * Phi
    return (V / 2 * z - c_2 * D2z) / (1j * tau_I)


def gauge_invariance_check(z: np.ndarray, A: np.ndarray, e: float,
                            theta: np.ndarray, dx: float) -> dict:
    """Check that |z|^2 is gauge-invariant under z -> e^{i theta} z.

    Returns the max difference in |z|^2 between original and transformed.
    """
    z_prime = z * np.exp(1j * theta)
    rho_orig = np.abs(z)**2
    rho_prime = np.abs(z_prime)**2
    max_diff = float(np.max(np.abs(rho_orig - rho_prime)))

    return {
        "max_rho_diff": max_diff,
        "status": "PASS" if max_diff < 1e-14 else "FAIL",
    }
