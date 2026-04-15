"""
GRUT Foundation — The Constitutive Equation

    tau dz/dt + z = z_target[z]                                    (5)

Derived from three independent routes:
    Route 1: CTP variation (A0 + A1)
    Route 2: Mori-Zwanzig memory kernel (coarse-grained open system)
    Route 3: Gradient flow (variational relaxation)

The target functional:
    z_target[z] = z - (dF/dz)^(-1) F[z]                           (6)

is the Newton-Raphson step toward F[z] = 0.
"""

import numpy as np


def constitutive_step(z, z_target, tau, dt):
    """Exact solution of tau dz/dt + z = z_target over interval dt.

    For constant z_target:
        z(t+dt) = z_target + (z - z_target) exp(-dt/tau)

    This is exact, numerically stable for any dt/tau ratio.
    """
    if tau <= 0:
        return z_target
    decay = np.exp(-dt / tau)
    return z_target + (z - z_target) * decay


def fixed_point_residual(z, z_target_func):
    """Compute z - z_target[z]. Zero at the fixed point.

    At the fixed point: z* = z_target[z*], residual = 0.
    """
    return z - z_target_func(z)


def jacobian_eigenvalues(z_target_func, z_star, epsilon=1e-8):
    """Eigenvalues of dz_target/dz at the fixed point.

    Stable if all |lambda_i| < 1.
    """
    n = len(z_star) if hasattr(z_star, '__len__') else 1

    if n == 1:
        # Scalar: numerical derivative
        z_s = float(z_star)
        dz = epsilon * max(abs(z_s), 1.0)
        J = (z_target_func(z_s + dz) - z_target_func(z_s - dz)) / (2 * dz)
        return np.array([J])

    # Vector: Jacobian matrix
    z_s = np.array(z_star, dtype=float)
    J = np.zeros((n, n))
    for j in range(n):
        dz = np.zeros(n)
        dz[j] = epsilon * max(abs(z_s[j]), 1.0)
        J[:, j] = (z_target_func(z_s + dz) - z_target_func(z_s - dz)) / (2 * dz[j])

    return np.linalg.eigvals(J)


def is_stable(eigenvalues):
    """Check if all eigenvalues have magnitude < 1 (stable attractor)."""
    return all(abs(ev) < 1.0 for ev in eigenvalues)


def newton_target(F, dF_dz, z):
    """The Newton-Raphson target: z_target = z - (dF/dz)^(-1) F[z].

    This is the unique self-consistent solution operator (equation 6).
    """
    F_val = F(z)
    J_val = dF_dz(z)

    if hasattr(J_val, '__len__') and hasattr(J_val, 'shape'):
        # Matrix: solve J × delta = -F
        delta = np.linalg.solve(J_val, -F_val)
    else:
        # Scalar
        delta = -F_val / J_val if J_val != 0 else 0.0

    return z + delta


def verify() -> dict:
    """Self-test constitutive equation."""
    # Test 1: constitutive_step with tau >> dt → z unchanged
    z0 = 1.0
    z_tgt = 0.0
    z_new = constitutive_step(z0, z_tgt, tau=1e10, dt=1.0)
    large_tau = abs(z_new - z0) < 0.01

    # Test 2: constitutive_step with tau << dt → z = z_target
    z_new2 = constitutive_step(z0, z_tgt, tau=1e-10, dt=1.0)
    small_tau = abs(z_new2 - z_tgt) < 0.01

    # Test 3: fixed point has zero residual
    z_tgt_func = lambda z: 0.5 * z  # fixed point at z = 0
    residual = fixed_point_residual(0.0, z_tgt_func)
    fp_zero = abs(residual) < 1e-15

    return {
        "large_tau_holds": large_tau,
        "small_tau_tracks": small_tau,
        "fixed_point_zero": fp_zero,
    }
