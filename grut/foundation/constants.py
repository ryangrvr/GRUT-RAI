"""
GRUT Foundation — Physical Constants

SINGLE SOURCE OF TRUTH. Every constant used anywhere in the framework
is defined here. CODATA 2018 values where available.

These are INPUTS to the theory, not outputs.
"""

import numpy as np

# =============================================================================
# FUNDAMENTAL CONSTANTS (CODATA 2018)
# =============================================================================

G: float = 6.67430e-11            # Gravitational constant [m^3 kg^-1 s^-2]
HBAR: float = 1.054571817e-34     # Reduced Planck constant [J s]
C: float = 2.99792458e8           # Speed of light [m/s]
K_B: float = 1.380649e-23         # Boltzmann constant [J/K]
E_CHARGE: float = 1.602176634e-19 # Elementary charge [C]
EPSILON_0: float = 8.8541878128e-12  # Vacuum permittivity [F/m]
AMU: float = 1.66053906660e-27    # Atomic mass unit [kg]

# =============================================================================
# DERIVED SCALES
# =============================================================================

M_PLANCK: float = np.sqrt(HBAR * C / G)
L_PLANCK: float = np.sqrt(HBAR * G / C**3)
T_PLANCK: float = L_PLANCK / C
E_PLANCK: float = M_PLANCK * C**2
ALPHA_EM: float = E_CHARGE**2 / (4 * np.pi * EPSILON_0 * HBAR * C)

# =============================================================================
# MATHEMATICAL CONSTANTS
# =============================================================================

ZETA_3: float = 1.2020569031595942  # Riemann zeta(3), Apery's constant


def verify() -> dict:
    """Self-test all constants against known values."""
    checks = {
        "M_PLANCK": abs(M_PLANCK - 2.176e-8) / 2.176e-8 < 1e-3,
        "ALPHA_EM": abs(1/ALPHA_EM - 137.036) / 137.036 < 1e-4,
        "T_PLANCK": abs(T_PLANCK - 5.391e-44) / 5.391e-44 < 1e-3,
    }
    return checks
