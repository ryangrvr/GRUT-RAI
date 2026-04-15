"""
GRUT Foundation — Axioms and Normalization

A0: CTP Doubling (Schwinger-Keldysh closed time path)
A1: Retarded Variation (causal, forward-in-time dynamics)
N0: tau_I = hbar/2 (normalization connecting CTP to QM)

Everything in the framework follows from these three statements.
"""

import numpy as np
from grut.foundation.constants import HBAR


# =============================================================================
# AXIOM A0: CTP DOUBLING
# =============================================================================

def keldysh_basis(z_plus: np.ndarray, z_minus: np.ndarray) -> tuple:
    """Transform from forward/backward paths to Keldysh basis.

    A0: Physics is formulated on the closed time path.

    z_r = (z+ + z-) / 2   (classical / retarded field)
    z_a = z+ - z-          (quantum / advanced field)

    The CTP effective action in this basis:
        S_CTP = z_a F[z_r] + (i/2) z_a N z_a

    Returns (z_r, z_a).
    """
    z_r = (z_plus + z_minus) / 2
    z_a = z_plus - z_minus
    return z_r, z_a


def inverse_keldysh(z_r: np.ndarray, z_a: np.ndarray) -> tuple:
    """Transform from Keldysh basis back to forward/backward paths.

    Returns (z_plus, z_minus).
    """
    z_plus = z_r + z_a / 2
    z_minus = z_r - z_a / 2
    return z_plus, z_minus


# =============================================================================
# AXIOM A1: RETARDED VARIATION
# =============================================================================

def retarded_eom(F_operator, z_r: np.ndarray) -> np.ndarray:
    """The retarded equation of motion from A1.

    A1: delta S_CTP / delta z_a |_{z_a=0} = 0  →  F[z_r] = 0

    This selects the causal (forward-in-time) dynamics.
    The variation with respect to z_a gives the retarded propagator.

    Parameters
    ----------
    F_operator : callable
        The equation-of-motion operator from S_classical.
    z_r : np.ndarray
        The classical field configuration.

    Returns
    -------
    np.ndarray
        F[z_r] — vanishes at the physical solution.
    """
    return F_operator(z_r)


# =============================================================================
# NORMALIZATION N0
# =============================================================================

TAU_I: float = HBAR / 2
"""The constitutive relaxation parameter.

N0: tau_I = hbar/2. This connects the CTP formalism to quantum mechanics
in the non-relativistic limit. It is a normalization choice — different
values give different tau. This value recovers the Schrodinger equation.
"""


# =============================================================================
# SELF-TEST
# =============================================================================

def verify() -> dict:
    """Verify axiom implementation."""
    # A0: Keldysh basis is invertible
    z_p = np.array([1.0, 2.0, 3.0])
    z_m = np.array([0.5, 1.5, 2.5])
    z_r, z_a = keldysh_basis(z_p, z_m)
    z_p2, z_m2 = inverse_keldysh(z_r, z_a)
    invertible = np.allclose(z_p, z_p2) and np.allclose(z_m, z_m2)

    # N0: tau_I = hbar/2
    tau_correct = TAU_I == HBAR / 2

    return {
        "A0_invertible": invertible,
        "N0_tau_I": tau_correct,
    }
