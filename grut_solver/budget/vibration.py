"""Vibrational / seismic decoherence channel."""

import numpy as np
from grut_solver.constants import HBAR, K_B


def lambda_vibration(m: float, omega_trap: float, S_x: float, l: float) -> float:
    """Decoherence from seismic/vibrational noise coupling [Hz].

    The trap center jitters due to seismic vibrations. This couples to
    the particle's position through the trapping potential.

    Parameters
    ----------
    m : float           Particle mass [kg].
    omega_trap : float  Trap angular frequency [rad/s].
    S_x : float         Position noise PSD of the trap center [m^2/Hz].
    l : float           Superposition separation [m].
    """
    if S_x <= 0 or omega_trap <= 0 or l <= 0 or m <= 0:
        return 0.0

    # Force noise from trap jitter: S_F = (m omega_trap^2)^2 * S_x
    S_F = (m * omega_trap**2)**2 * S_x
    # Momentum diffusion -> decoherence
    return S_F * l**2 / HBAR**2


def lambda_internal_phonon(R: float, T_int: float, rho: float,
                           c_sound: float, l: float) -> float:
    """Decoherence from internal phonon emission [Hz].

    Hot nanoparticle radiates phonons (acoustic emission).
    Each phonon carries momentum ~kT/c_sound.

    Parameters
    ----------
    R : float       Particle radius [m].
    T_int : float   Internal temperature [K].
    rho : float     Material density [kg/m^3].
    c_sound : float Speed of sound in material [m/s].
    l : float       Superposition separation [m].
    """
    if T_int < 1e-6 or R <= 0 or l <= 0:
        return 0.0

    # Thermal phonon emission rate ~ (kT/hbar) * (R/lambda_phonon)^3
    # where lambda_phonon = c_sound * hbar / (kT)
    omega_thermal = K_B * T_int / HBAR
    lambda_phonon = c_sound / omega_thermal

    if R < lambda_phonon:
        # Small particle: suppressed emission
        emission_rate = omega_thermal * (R / lambda_phonon)**3
    else:
        emission_rate = omega_thermal

    # Each phonon gives decoherence ~ (l * kT / (c_sound * hbar))^2
    decoh_per_phonon = min(1.0, (l * K_B * T_int / (c_sound * HBAR))**2)

    return emission_rate * decoh_per_phonon
