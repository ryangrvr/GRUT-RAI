"""
Gravitational Wave Propagation in Constitutive Gravity

In linearized constitutive gravity, the wave equation becomes:
  (1 + τ_grav ∂_t) □h_μν^TT = -16πG T_μν

The transfer function for GW propagation:
  H(f) = 1 / (1 + 2πi f τ_grav)

This gives frequency-dependent amplitude suppression, phase shift,
and group delay. All predictions are computed for both τ_grav candidates.

HONEST RESULT: For τ_grav = T_Planck ~ 5.4e-44 s, the maximum phase
shift at LIGO frequencies is ~10^-41 rad — 38 orders below sensitivity.
For τ_grav = τ_I = ℏ/2 ~ 5.3e-35 s, it's ~10^-32 rad — still far out.
These effects are observationally dead with foreseeable technology.

STATUS: Computed. Observationally silent (locked negative result).
"""

import numpy as np
from grut_solver.constants import (
    G, HBAR, C, T_PLANCK, TAU_I,
    LIGO_F_LOW, LIGO_F_HIGH, LISA_F_LOW, LISA_F_HIGH
)

MPC_TO_M = 3.086e22  # 1 Mpc in meters


def dispersion_relation(f_hz: np.ndarray, tau_grav: float) -> dict:
    """Constitutive GW dispersion relation.

    For a plane wave h ~ exp(i(kx - ωt)), the constitutive equation
    (1 + iωτ)(ω² - k²c²) = source gives the dispersion:

    In vacuum (source = 0): ω² = k²c² still holds for propagating modes.
    The constitutive term modifies the AMPLITUDE transfer, not the
    dispersion relation itself. GWs still propagate at c.

    The transfer function H(ω) = 1/(1 + iωτ) gives:
    - Amplitude: |H| = 1/sqrt(1 + (ωτ)²)
    - Phase: φ = -arctan(ωτ)
    """
    omega = 2 * np.pi * f_hz
    omega_tau = omega * tau_grav

    amplitude = 1.0 / np.sqrt(1 + omega_tau**2)
    phase_rad = -np.arctan(omega_tau)
    group_delay_s = tau_grav / (1 + omega_tau**2)

    return {
        "f_hz": f_hz.tolist() if hasattr(f_hz, 'tolist') else [f_hz],
        "omega_tau": omega_tau.tolist() if hasattr(omega_tau, 'tolist') else [omega_tau],
        "amplitude_ratio": amplitude.tolist() if hasattr(amplitude, 'tolist') else [amplitude],
        "phase_shift_rad": phase_rad.tolist() if hasattr(phase_rad, 'tolist') else [phase_rad],
        "group_delay_s": group_delay_s.tolist() if hasattr(group_delay_s, 'tolist') else [group_delay_s],
        "propagation_speed": "c (unchanged — constitutive term modifies amplitude, not speed)",
    }


def gw_transfer_function(f_hz: float, tau_grav: float) -> dict:
    """Transfer function H(f) for a single frequency."""
    omega = 2 * np.pi * f_hz
    omega_tau = omega * tau_grav

    amplitude = 1.0 / np.sqrt(1 + omega_tau**2)
    phase_rad = -np.arctan(omega_tau)
    group_delay = tau_grav / (1 + omega_tau**2)

    return {
        "f_hz": f_hz,
        "tau_grav_s": tau_grav,
        "omega_tau": omega_tau,
        "amplitude_ratio": amplitude,
        "amplitude_change_dB": 20 * np.log10(amplitude) if amplitude > 0 else float('-inf'),
        "phase_shift_rad": phase_rad,
        "group_delay_s": group_delay,
    }


def ligo_observability(tau_grav: float = None) -> dict:
    """Predict observability of constitutive effect in LIGO band (10-5000 Hz).

    LIGO phase sensitivity: ~10^-3 rad (design sensitivity).
    """
    if tau_grav is None:
        tau_grav = T_PLANCK

    f_ref = 100.0  # Hz — typical GW frequency
    f_array = np.logspace(np.log10(LIGO_F_LOW), np.log10(LIGO_F_HIGH), 100)

    disp = dispersion_relation(f_array, tau_grav)
    phases = np.array(disp["phase_shift_rad"])

    max_phase = float(np.max(np.abs(phases)))
    max_amplitude_change = float(1.0 - np.min(np.array(disp["amplitude_ratio"])))

    ligo_sensitivity_rad = 1e-3

    return {
        "tau_grav_s": tau_grav,
        "f_range_hz": (LIGO_F_LOW, LIGO_F_HIGH),
        "max_phase_shift_rad": max_phase,
        "log10_max_phase": np.log10(max_phase) if max_phase > 0 else float('-inf'),
        "max_amplitude_change": max_amplitude_change,
        "ligo_sensitivity_rad": ligo_sensitivity_rad,
        "detectable": max_phase > ligo_sensitivity_rad,
        "orders_below_sensitivity": np.log10(ligo_sensitivity_rad / max_phase) if max_phase > 0 else float('inf'),
        "note": (
            f"At tau_grav = {tau_grav:.2e} s: max phase shift = {max_phase:.2e} rad. "
            f"LIGO sensitivity: ~{ligo_sensitivity_rad:.0e} rad. "
            f"{'DETECTABLE' if max_phase > ligo_sensitivity_rad else 'UNDETECTABLE'} — "
            f"{np.log10(ligo_sensitivity_rad/max_phase):.0f} orders below sensitivity."
        ),
    }


def lisa_observability(tau_grav: float = None) -> dict:
    """Predict observability in LISA band (10^-4 to 0.1 Hz)."""
    if tau_grav is None:
        tau_grav = T_PLANCK

    f_array = np.logspace(np.log10(LISA_F_LOW), np.log10(LISA_F_HIGH), 100)
    disp = dispersion_relation(f_array, tau_grav)
    phases = np.array(disp["phase_shift_rad"])

    max_phase = float(np.max(np.abs(phases)))
    lisa_sensitivity_rad = 1e-4

    return {
        "tau_grav_s": tau_grav,
        "f_range_hz": (LISA_F_LOW, LISA_F_HIGH),
        "max_phase_shift_rad": max_phase,
        "log10_max_phase": np.log10(max_phase) if max_phase > 0 else float('-inf'),
        "detectable": max_phase > lisa_sensitivity_rad,
        "orders_below_sensitivity": np.log10(lisa_sensitivity_rad / max_phase) if max_phase > 0 else float('inf'),
    }


def arrival_time_difference(tau_grav: float, f1_hz: float, f2_hz: float,
                            distance_mpc: float = 100.0) -> dict:
    """Frequency-dependent arrival time difference for GW signal.

    The group delay at frequency f is: τ_g(f) = τ_grav / (1 + (2πfτ)²)

    The arrival time difference between two frequencies:
      Δt = τ_g(f1) - τ_g(f2)

    For propagation over distance D, this accumulates.
    """
    D_m = distance_mpc * MPC_TO_M
    travel_time = D_m / C

    omega1 = 2 * np.pi * f1_hz
    omega2 = 2 * np.pi * f2_hz

    tg1 = tau_grav / (1 + (omega1 * tau_grav)**2)
    tg2 = tau_grav / (1 + (omega2 * tau_grav)**2)

    # The accumulated delay over distance D is roughly N_wavelengths * delta_tg
    # More precisely: phase accumulation difference
    delta_phase1 = omega1 * travel_time * (omega1 * tau_grav) / (1 + (omega1 * tau_grav)**2)
    delta_phase2 = omega2 * travel_time * (omega2 * tau_grav) / (1 + (omega2 * tau_grav)**2)

    delta_t = abs(delta_phase1 / omega1 - delta_phase2 / omega2) if omega1 > 0 and omega2 > 0 else 0

    return {
        "tau_grav_s": tau_grav,
        "f1_hz": f1_hz,
        "f2_hz": f2_hz,
        "distance_mpc": distance_mpc,
        "delta_t_s": delta_t,
        "timing_sensitivity_s": 1e-4,  # ~0.1 ms for LIGO
        "detectable": delta_t > 1e-4,
    }


def gw_summary() -> dict:
    """Complete GW propagation summary for both τ candidates."""
    results = {}
    for cand in [("T_Planck", T_PLANCK), ("tau_I", TAU_I)]:
        name, tau = cand
        ligo = ligo_observability(tau)
        lisa = lisa_observability(tau)
        dt = arrival_time_difference(tau, 50.0, 200.0, 100.0)

        results[name] = {
            "tau_s": tau,
            "ligo_max_phase_rad": ligo["max_phase_shift_rad"],
            "ligo_detectable": ligo["detectable"],
            "lisa_max_phase_rad": lisa["max_phase_shift_rad"],
            "lisa_detectable": lisa["detectable"],
            "arrival_dt_s": dt["delta_t_s"],
            "arrival_detectable": dt["detectable"],
        }

    return {
        "candidates": results,
        "verdict": (
            "Both tau candidates produce effects far below detector sensitivity. "
            f"T_Planck: LIGO phase ~ {results['T_Planck']['ligo_max_phase_rad']:.1e} rad. "
            f"tau_I: LIGO phase ~ {results['tau_I']['ligo_max_phase_rad']:.1e} rad. "
            "Constitutive GW effects are observationally DEAD with foreseeable technology."
        ),
    }
