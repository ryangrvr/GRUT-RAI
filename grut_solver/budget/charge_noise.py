"""Charge noise decoherence channel.

Stray electric fields and patch potentials on nearby surfaces.
"""

import numpy as np
from grut_solver.constants import E_CHARGE, EPSILON_0, K_B


def lambda_charge(n_charges: int, E_noise_V_per_m: float,
                  m: float, l: float, omega_trap: float) -> float:
    """Decoherence from stray electric field noise [Hz].

    A charged nanoparticle (net charge q = n_charges * e) in a fluctuating
    E field sees random force kicks F = qE, each transferring momentum
    delta_p = q * E * delta_t.

    Decoherence rate ~ (q * S_E / m)^2 * l^2 where S_E is the noise PSD.

    Simplified: Lambda ~ (n_charges * e * E_noise)^2 * l^2 / (hbar^2 * omega_trap)

    Parameters
    ----------
    n_charges : int         Net charges on particle.
    E_noise_V_per_m : float Electric field noise amplitude [V/m].
    m : float               Particle mass [kg].
    l : float               Superposition separation [m].
    omega_trap : float      Trap frequency [rad/s] (sets coherence bandwidth).
    """
    if n_charges == 0 or E_noise_V_per_m <= 0 or l <= 0 or omega_trap <= 0:
        return 0.0

    from grut_solver.constants import HBAR
    q = abs(n_charges) * E_CHARGE
    # Force noise PSD: S_F = q^2 * S_E (white noise approximation)
    # Momentum diffusion: D_p = S_F / (2 pi)
    # Decoherence: Lambda ~ D_p * l^2 / hbar^2
    # With S_E ~ E_noise^2 / omega_trap (noise in bandwidth omega_trap)
    S_F = q**2 * E_noise_V_per_m**2 / omega_trap
    return S_F * l**2 / HBAR**2


def lambda_patch_potential(V_patch: float, d_surface: float,
                           R: float, l: float, m: float) -> float:
    """Decoherence from surface patch potentials [Hz].

    Metallic surfaces have fluctuating patch potentials (~10-100 mV)
    that create position-dependent electric fields.

    Parameters
    ----------
    V_patch : float     RMS patch potential [V].
    d_surface : float   Distance to nearest surface [m].
    R : float           Particle radius [m].
    l : float           Superposition separation [m].
    m : float           Particle mass [kg].
    """
    if V_patch <= 0 or d_surface <= 0 or R <= 0 or l <= 0:
        return 0.0

    from grut_solver.constants import HBAR
    # Gradient of patch field: E_patch ~ V_patch / d_surface
    # Force gradient: dF/dx ~ q * dE/dx ~ (4pi eps0 R^2 V_patch) * V_patch / d_surface^3
    # Simplified decoherence estimate
    E_patch = V_patch / d_surface
    alpha_pol = 4 * np.pi * EPSILON_0 * R**3  # polarizability of dielectric sphere
    F_patch = alpha_pol * E_patch**2 / d_surface  # gradient force
    # Decoherence from force fluctuations
    return F_patch * l / HBAR if HBAR > 0 else 0.0
