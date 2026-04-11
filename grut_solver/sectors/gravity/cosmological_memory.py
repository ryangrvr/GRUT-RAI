"""
Cosmological Memory — Modified Friedmann Evolution

The constitutive Friedmann equation:
  H² + τ_grav d(H²)/dt = (8πG/3)ρ

Equivalently: H² relaxes toward its GR target on timescale τ_grav.

At late times (H ~ H_0): the correction is τ_grav × H_0 ~ 10^-61.
Utterly negligible. The dark energy problem is NOT solved by this term.

At early times (near Planck epoch): the correction is O(1).
This is where the constitutive modification matters — singularity resolution.

The user's independent FLRW mocks showed:
  - Direction 2 (dissipative) can source late-time acceleration with
    τ_grav tuned in Hubble units, but requires careful tuning
  - Direction 1 (stochastic back-reaction) produces gentler E(z) shapes
    closer to ΛCDM
  - Both achieve q < 0 today

STATUS: Computed. Late-time: negligible for physical τ_grav.
User's mocks show viability with τ_grav in Hubble units (phenomenological).
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, T_PLANCK, TAU_I, K_B


def modified_friedmann_evolution(z_max: float = 10.0, tau_grav: float = None,
                                 Omega_m: float = 0.3,
                                 H0_km_s_Mpc: float = 67.4,
                                 n_points: int = 1000) -> dict:
    """Integrate modified Friedmann from z_max to z=0.

    Standard: E²(z) = Ω_m(1+z)³ + (1-Ω_m)
    Constitutive: dE²/dz = (1/τ̃) × (E²_target - E²) × (1+z)/E
      where τ̃ = τ_grav × H_0 (dimensionless)

    For physical τ_grav = T_Planck: τ̃ ~ 10^-61, correction is zero.
    """
    if tau_grav is None:
        tau_grav = T_PLANCK

    H0_si = H0_km_s_Mpc * 1e3 / 3.086e22  # Hz
    tau_tilde = tau_grav * H0_si  # dimensionless

    z_array = np.linspace(z_max, 0, n_points)
    dz = np.abs(np.diff(z_array))

    E2_standard = np.zeros(n_points)
    E2_constitutive = np.zeros(n_points)

    for i in range(n_points):
        z = z_array[i]
        E2_standard[i] = Omega_m * (1 + z)**3 + (1 - Omega_m)

    E2_constitutive[0] = E2_standard[0]

    # For extremely small tau_tilde (< 1e-10), the relaxation is instant:
    # the constitutive solution IS the standard solution.
    if tau_tilde < 1e-10:
        E2_constitutive = E2_standard.copy()
    else:
        for i in range(n_points - 1):
            z = z_array[i]
            E = np.sqrt(max(E2_constitutive[i], 1e-30))

            # dE²/dz = -(1/τ̃) × (E²_target - E²) × (1+z) / E
            dE2_dz = -(1.0 / tau_tilde) * (E2_standard[i] - E2_constitutive[i]) * (1 + z) / E

            # z is decreasing, so dz is negative
            E2_constitutive[i + 1] = E2_constitutive[i] + dE2_dz * (z_array[i + 1] - z_array[i])
            E2_constitutive[i + 1] = max(E2_constitutive[i + 1], 0)

    E_standard = np.sqrt(E2_standard)
    E_constitutive = np.sqrt(np.maximum(E2_constitutive, 0))

    delta_E = np.abs(E_constitutive - E_standard)
    max_dev = float(np.max(delta_E / E_standard)) if np.all(E_standard > 0) else 0

    return {
        "z": z_array.tolist(),
        "E_standard": E_standard.tolist(),
        "E_constitutive": E_constitutive.tolist(),
        "tau_grav_s": tau_grav,
        "tau_tilde": tau_tilde,
        "max_fractional_deviation": max_dev,
        "log10_max_deviation": np.log10(max_dev) if max_dev > 0 else float('-inf'),
        "observable": max_dev > 0.01,
    }


def dark_energy_compatibility(tau_grav: float = None) -> dict:
    """Does the constitutive term help with dark energy?

    Short answer: NO for physical τ_grav values.
    The constitutive term is a MEMORY effect — it becomes important
    when curvature changes rapidly (early universe, near singularities).
    Dark energy requires an effect that grows at LATE times / LOW curvature.
    These are opposite regimes.

    The user's FLRW mocks showed viability with τ_grav ~ 0.001-0.1 in
    Hubble units — but this corresponds to τ_grav ~ 10^17 s (billions of
    years), far from either Planck or τ_I candidate.
    """
    if tau_grav is None:
        tau_grav = T_PLANCK

    H0 = 2.3e-18  # H_0 in Hz
    correction_at_z0 = tau_grav * H0

    # What τ_grav would be needed for O(1) effect at z=0?
    tau_needed = 1.0 / H0  # ~ 1/H_0 ~ age of universe

    return {
        "tau_grav_s": tau_grav,
        "correction_at_z0": correction_at_z0,
        "log10_correction": np.log10(correction_at_z0) if correction_at_z0 > 0 else float('-inf'),
        "helps_dark_energy": correction_at_z0 > 0.01,
        "tau_needed_for_de_s": tau_needed,
        "tau_needed_yr": tau_needed / 3.156e7,
        "ratio_to_planck": tau_needed / T_PLANCK,
        "ratio_to_tau_I": tau_needed / TAU_I,
        "note": (
            f"At τ_grav = {tau_grav:.2e} s: correction at z=0 is {correction_at_z0:.2e}. "
            f"For O(1) effect: need τ_grav ~ {tau_needed:.2e} s (~{tau_needed/3.156e7:.1e} yr). "
            f"This is {tau_needed/T_PLANCK:.1e}× T_Planck, {tau_needed/TAU_I:.1e}× τ_I. "
            f"Physical τ candidates cannot source dark energy. "
            f"The user's phenomenological mocks use τ ~ 0.001-0.1 H_0^(-1), "
            f"which IS in this range but requires τ_grav >> T_Planck."
        ),
    }


def expansion_history_deviation(tau_grav: float = None,
                                z_values: list = None) -> dict:
    """Compute fractional δH/H at selected redshifts."""
    if tau_grav is None:
        tau_grav = T_PLANCK
    if z_values is None:
        z_values = [0.0, 0.5, 1.0, 1.5, 2.0, 5.0, 10.0]

    evol = modified_friedmann_evolution(z_max=max(z_values) + 1, tau_grav=tau_grav)
    z_arr = np.array(evol["z"])
    E_std = np.array(evol["E_standard"])
    E_con = np.array(evol["E_constitutive"])

    table = []
    for z in z_values:
        idx = np.argmin(np.abs(z_arr - z))
        if E_std[idx] > 0:
            delta = abs(E_con[idx] - E_std[idx]) / E_std[idx]
        else:
            delta = 0
        table.append({"z": z, "E_standard": float(E_std[idx]),
                       "E_constitutive": float(E_con[idx]),
                       "delta_E_over_E": float(delta)})

    return {
        "tau_grav_s": tau_grav,
        "table": table,
        "max_deviation": max(r["delta_E_over_E"] for r in table),
    }


def early_universe_modification(tau_grav: float = None,
                                T_K: float = 1e12) -> dict:
    """Compute constitutive correction at early universe temperature.

    At temperature T, the Hubble rate is:
      H ~ sqrt(8πG ρ / 3) where ρ ~ g* π² T⁴ / (30 c² ℏ³)

    The constitutive correction is τ_grav × dH/dt.
    For radiation: dH/dt = -2H² → correction = 2 τ_grav H.
    """
    if tau_grav is None:
        tau_grav = T_PLANCK

    g_star = 106.75
    rho = g_star * np.pi**2 * (K_B * T_K)**4 / (30 * C**2 * HBAR**3)
    H = np.sqrt(8 * np.pi * G * rho / 3)

    correction = 2 * tau_grav * H
    T_planck_K = 1.416e32

    return {
        "T_K": T_K,
        "T_over_T_planck": T_K / T_planck_K,
        "H_hz": H,
        "tau_grav_s": tau_grav,
        "tau_H": tau_grav * H,
        "fractional_correction": correction,
        "significant": correction > 0.01,
        "note": (
            f"At T = {T_K:.0e} K ({T_K/T_planck_K:.1e} T_Planck): "
            f"H = {H:.2e} Hz, τ×H = {tau_grav*H:.2e}. "
            f"Correction = {correction:.2e}. "
            f"{'SIGNIFICANT' if correction > 0.01 else 'Negligible'}."
        ),
    }
