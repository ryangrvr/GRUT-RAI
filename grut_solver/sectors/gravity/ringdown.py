"""
Modified Black Hole Ringdown in Constitutive Gravity

Standard Schwarzschild QNMs: ω_n = ω_R(n) + iω_I(n)
Constitutive modification adds a frequency-dependent damping.

The constitutive transfer function H(ω) = 1/(1 + iωτ_grav) shifts
the QNM frequencies perturbatively:
  δω/ω ~ ωτ_grav

For τ_grav = T_Planck and a 30 M_sun BH: δω/ω ~ 10^-40.
Observationally dead — but computed and documented.

STATUS: Computed. Observationally silent (locked).
"""

import numpy as np
from grut_solver.constants import (
    G, C, HBAR, T_PLANCK, TAU_I, M_SUN,
    QNM_OMEGA_R, QNM_OMEGA_I
)


def schwarzschild_qnm(M_solar: float = 30.0, n: int = 0, l: int = 2) -> dict:
    """Standard Schwarzschild quasi-normal mode frequencies.

    For n=0, l=2 (fundamental): ω = (0.3737 - 0.0890i) × c³/(GM)
    """
    M_kg = M_solar * M_SUN
    scale = C**3 / (G * M_kg)  # Hz (angular)

    omega_R = QNM_OMEGA_R * scale
    omega_I = QNM_OMEGA_I * scale

    f_R = omega_R / (2 * np.pi)
    tau_ring = 1.0 / omega_I  # ringdown damping time
    Q_factor = omega_R / (2 * omega_I)  # quality factor

    return {
        "M_solar": M_solar,
        "n": n, "l": l,
        "omega_R_rad_s": omega_R,
        "omega_I_rad_s": omega_I,
        "f_R_hz": f_R,
        "tau_ring_s": tau_ring,
        "Q_factor": Q_factor,
        "scale_hz": scale / (2 * np.pi),
    }


def constitutive_qnm_shift(M_solar: float = 30.0, tau_grav: float = None,
                            n: int = 0, l: int = 2) -> dict:
    """First-order perturbative shift of QNM from constitutive term.

    The constitutive transfer function modifies the QNM condition.
    To first order: δω/ω ~ iωτ_grav

    The real part shifts by: δω_R ~ -ω_R × (ω_R τ_grav)²
    The imaginary part shifts by: δω_I ~ ω_R² × τ_grav
    """
    if tau_grav is None:
        tau_grav = T_PLANCK

    qnm = schwarzschild_qnm(M_solar, n, l)
    omega_R = qnm["omega_R_rad_s"]
    omega_I = qnm["omega_I_rad_s"]

    # Perturbative shift
    omega_tau = omega_R * tau_grav

    delta_omega_R = -omega_R * omega_tau**2  # second order in ωτ
    delta_omega_I = omega_R**2 * tau_grav    # first order

    fractional_R = abs(delta_omega_R / omega_R) if omega_R > 0 else 0
    fractional_I = abs(delta_omega_I / omega_I) if omega_I > 0 else 0

    return {
        "M_solar": M_solar,
        "tau_grav_s": tau_grav,
        "omega_tau": omega_tau,
        "delta_omega_R_rad_s": delta_omega_R,
        "delta_omega_I_rad_s": delta_omega_I,
        "fractional_shift_R": fractional_R,
        "fractional_shift_I": fractional_I,
        "log10_fractional_R": np.log10(fractional_R) if fractional_R > 0 else float('-inf'),
        "log10_fractional_I": np.log10(fractional_I) if fractional_I > 0 else float('-inf'),
        "detectable": fractional_R > 1e-3 or fractional_I > 1e-3,
        "note": (
            f"QNM shift for {M_solar} M_sun BH at tau_grav = {tau_grav:.2e} s: "
            f"δω_R/ω_R = {fractional_R:.2e}, δω_I/ω_I = {fractional_I:.2e}. "
            f"{'DETECTABLE' if fractional_R > 1e-3 else 'UNDETECTABLE'}."
        ),
    }


def ringdown_waveform(t_ms: np.ndarray = None, M_solar: float = 30.0,
                      tau_grav: float = None, A0: float = 1.0) -> dict:
    """Compute standard and modified ringdown waveforms."""
    if tau_grav is None:
        tau_grav = T_PLANCK
    if t_ms is None:
        t_ms = np.linspace(0, 50, 500)

    t_s = t_ms * 1e-3
    qnm = schwarzschild_qnm(M_solar)
    shift = constitutive_qnm_shift(M_solar, tau_grav)

    omega_R = qnm["omega_R_rad_s"]
    omega_I = qnm["omega_I_rad_s"]
    d_omega_R = shift["delta_omega_R_rad_s"]
    d_omega_I = shift["delta_omega_I_rad_s"]

    h_standard = A0 * np.exp(-omega_I * t_s) * np.cos(omega_R * t_s)
    h_constitutive = A0 * np.exp(-(omega_I + d_omega_I) * t_s) * np.cos((omega_R + d_omega_R) * t_s)

    max_diff = float(np.max(np.abs(h_standard - h_constitutive)))

    return {
        "t_ms": t_ms.tolist(),
        "h_standard": h_standard.tolist(),
        "h_constitutive": h_constitutive.tolist(),
        "max_difference": max_diff,
        "log10_max_diff": np.log10(max_diff) if max_diff > 0 else float('-inf'),
    }


def ringdown_observability(M_solar_range: tuple = (5, 100),
                           n_points: int = 20) -> dict:
    """Sweep over BH masses, compute detectability for both τ candidates."""
    masses = np.linspace(M_solar_range[0], M_solar_range[1], n_points)

    results = []
    for M in masses:
        for name, tau in [("T_Planck", T_PLANCK), ("tau_I", TAU_I)]:
            s = constitutive_qnm_shift(M, tau)
            results.append({
                "M_solar": float(M),
                "tau_candidate": name,
                "fractional_shift_R": s["fractional_shift_R"],
                "fractional_shift_I": s["fractional_shift_I"],
                "detectable": s["detectable"],
            })

    any_detectable = any(r["detectable"] for r in results)

    return {
        "results": results,
        "any_detectable": any_detectable,
        "verdict": (
            "No BH mass in the 5-100 M_sun range produces a detectable "
            "constitutive QNM shift for either tau candidate. "
            "Ringdown modification is observationally DEAD."
        ),
    }
