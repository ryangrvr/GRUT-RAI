"""
Module 3: SU(3) covariant derivative and gauge covariance checks.

Status: Implemented and validated.
"""

import numpy as np
from scipy.linalg import expm
from grut_solver.sectors.qcd.su3_structure import T_GEN, N_GEN, N_C, I3


def covariant_derivative(q: np.ndarray, A_a: np.ndarray,
                          g_s: float) -> np.ndarray:
    """Apply SU(3) gauge field to a color triplet (at a single point).

    D q = (spatial derivative part) + i g_s T^a A^a q

    This computes only the gauge part (no spatial derivative — that
    requires a lattice or continuum discretization).

    Parameters
    ----------
    q : (3,) complex array   Color triplet.
    A_a : (8,) float array   Gauge field components A^a at this point.
    g_s : float              Strong coupling constant.

    Returns
    -------
    (3,) complex array: the gauge-connection contribution i g_s T^a A^a q.
    """
    A_matrix = sum(A_a[a] * T_GEN[a] for a in range(N_GEN))
    return 1j * g_s * A_matrix @ q


def gauge_transform(q: np.ndarray, theta_a: np.ndarray) -> tuple:
    """Apply SU(3) gauge transformation.

    q -> U q, where U = exp(i theta^a T^a).

    Returns (q_transformed, U_matrix).
    """
    generator = sum(theta_a[a] * T_GEN[a] for a in range(N_GEN))
    U = expm(1j * generator)
    return U @ q, U


def covariance_check(g_s: float = 1.0) -> dict:
    """Verify that D_mu q transforms covariantly: D' q' = U (D q).

    Uses random q, A^a, and theta^a.
    """
    np.random.seed(42)
    q = np.random.randn(N_C) + 1j * np.random.randn(N_C)
    A_a = np.random.randn(N_GEN)
    theta_a = 0.3 * np.random.randn(N_GEN)

    # Original: D q (gauge part only)
    D_q = covariant_derivative(q, A_a, g_s)

    # Transform
    q_p, U = gauge_transform(q, theta_a)
    # Transformed gauge field: A' = U A U^dag (for constant U, the derivative term vanishes)
    A_matrix = sum(A_a[a] * T_GEN[a] for a in range(N_GEN))
    A_matrix_p = U @ A_matrix @ U.conj().T
    # Extract A'^a from A'_matrix
    A_a_p = np.array([2 * np.real(np.trace(T_GEN[a] @ A_matrix_p)) for a in range(N_GEN)])

    D_q_p = covariant_derivative(q_p, A_a_p, g_s)
    U_D_q = U @ D_q

    err = float(np.max(np.abs(D_q_p - U_D_q)))

    # Also check |D q|^2 invariance
    norm_before = float(np.real(np.vdot(D_q, D_q)))
    norm_after = float(np.real(np.vdot(D_q_p, D_q_p)))
    inv_err = abs(norm_before - norm_after)

    return {
        "covariance_error": err,
        "norm_invariance_error": inv_err,
        "status": "PASS" if err < 1e-10 and inv_err < 1e-10 else "FAIL",
    }


def field_strength_commutator(A_mu_a: np.ndarray, A_nu_a: np.ndarray,
                               g_s: float) -> np.ndarray:
    """Compute the non-abelian field strength contribution [A_mu, A_nu].

    F_{mu nu} = d_mu A_nu - d_nu A_mu + i g_s [A_mu, A_nu]
    This returns the commutator part only.
    """
    A_mu = sum(A_mu_a[a] * T_GEN[a] for a in range(N_GEN))
    A_nu = sum(A_nu_a[a] * T_GEN[a] for a in range(N_GEN))
    return 1j * g_s * (A_mu @ A_nu - A_nu @ A_mu)


def field_strength_covariance_check(g_s: float = 1.0) -> dict:
    """Verify F_{mu nu} transforms as F' = U F U^dag."""
    np.random.seed(123)
    A_mu_a = np.random.randn(N_GEN)
    A_nu_a = np.random.randn(N_GEN)
    theta_a = 0.2 * np.random.randn(N_GEN)

    F = field_strength_commutator(A_mu_a, A_nu_a, g_s)

    generator = sum(theta_a[a] * T_GEN[a] for a in range(N_GEN))
    U = expm(1j * generator)

    F_prime = U @ F @ U.conj().T

    # Transform A fields
    A_mu_mat = sum(A_mu_a[a] * T_GEN[a] for a in range(N_GEN))
    A_nu_mat = sum(A_nu_a[a] * T_GEN[a] for a in range(N_GEN))
    A_mu_p = U @ A_mu_mat @ U.conj().T
    A_nu_p = U @ A_nu_mat @ U.conj().T
    F_from_transformed = 1j * g_s * (A_mu_p @ A_nu_p - A_nu_p @ A_mu_p)

    err = float(np.max(np.abs(F_prime - F_from_transformed)))

    # Tr(F^2) invariance
    trF2_before = float(np.real(np.trace(F @ F)))
    trF2_after = float(np.real(np.trace(F_prime @ F_prime)))
    tr_err = abs(trF2_before - trF2_after)

    return {
        "F_covariance_error": err,
        "TrF2_invariance_error": tr_err,
        "status": "PASS" if err < 1e-10 and tr_err < 1e-10 else "FAIL",
    }
