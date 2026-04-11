"""
Era Map — The Universe as a Discrete Constitutive Iteration

THE IDEA: The universe doesn't relax continuously. It processes in
discrete τ₀ = 41.9 Myr eras. Each era:
  1. Takes the current state (H², a, ρ) as input
  2. Runs one constitutive relaxation cycle (τ₀ seconds)
  3. Outputs the evolved state
  4. That output becomes the NEXT era's input

Over 330 eras, the iterated map x_{n+1} = f(x_n) produces the full
expansion history. This is fundamentally different from a continuous
ODE because discrete maps can produce slow drift, oscillation, and
emergent behavior that continuous relaxation cannot.

STATUS: Exploratory. Does the iterated map naturally produce three phases?
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, K_B

TAU_0_S = 41.9e6 * 3.1557e7   # 41.9 Myr in seconds
TAU_0_YR = 41.9e6
H0_SI = 70.0 * 1e3 / 3.086e22
OMEGA_R = 9.0e-5
OMEGA_M = 0.3
OMEGA_LAMBDA = 1.0 - OMEGA_M - OMEGA_R
T_UNIVERSE_YR = 13.8e9
N_ERAS = int(T_UNIVERSE_YR / TAU_0_YR)  # ~329


def one_era_evolution(H2_in: float, a_in: float, tau: float = TAU_0_S) -> dict:
    """Evolve one constitutive era: τ₀ seconds of expansion.

    Within one era:
      - Matter/radiation dilute as a expands
      - H² relaxes toward the instantaneous target
      - The constitutive equation governs the relaxation

    Returns the state at the END of the era.
    """
    # Subdivide one era into small steps
    n_sub = 200
    dt = tau / n_sub

    H2 = H2_in
    a = a_in

    for _ in range(n_sub):
        H = np.sqrt(max(H2, 1e-60))

        # Current target (standard Friedmann without Lambda)
        z_target_matter = H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3))

        # Constitutive relaxation within this sub-step
        dH2_dt = (z_target_matter - H2) / tau
        H2 = H2 + dH2_dt * dt
        H2 = max(H2, 1e-60)

        # Scale factor evolution
        H = np.sqrt(max(H2, 1e-60))
        a = a + a * H * dt

    return {"H2_out": H2, "a_out": a, "H_out": np.sqrt(max(H2, 0))}


def era_map_no_lambda(n_eras: int = N_ERAS) -> dict:
    """Iterate the era map WITHOUT cosmological constant.

    Each era processes one τ₀ cycle. The output of era N becomes
    the input of era N+1. No Λ — we want to see if the iterated
    map generates effective late-time acceleration on its own.
    """
    # Initial state: radiation-dominated early universe
    a_init = 1e-4
    H2_init = H0_SI**2 * (OMEGA_R * a_init**(-4) + OMEGA_M * a_init**(-3))

    H2_history = [H2_init]
    a_history = [a_init]
    H_history = [np.sqrt(H2_init)]

    H2 = H2_init
    a = a_init

    for era in range(n_eras):
        result = one_era_evolution(H2, a)
        H2 = result["H2_out"]
        a = result["a_out"]
        H2_history.append(H2)
        a_history.append(a)
        H_history.append(result["H_out"])

    # Compare to standard ΛCDM at same scale factors
    a_arr = np.array(a_history)
    H_arr = np.array(H_history)
    E_map = H_arr / H0_SI

    # Standard ΛCDM at the same scale factors
    E_standard = np.sqrt(OMEGA_R * a_arr**(-4) + OMEGA_M * a_arr**(-3) + OMEGA_LAMBDA)
    E_no_lambda = np.sqrt(OMEGA_R * a_arr**(-4) + OMEGA_M * a_arr**(-3))

    # Deceleration parameter from the map
    # q = -a a''/(a')² = -1 - (dH/dt)/H²
    # From the map: approximate q from successive H values
    q_map = np.zeros(len(H_arr))
    for i in range(1, len(H_arr) - 1):
        dH = (H_arr[i+1] - H_arr[i-1]) / (2 * TAU_0_S)
        if H_arr[i] > 0:
            q_map[i] = -1 - dH / H_arr[i]**2

    # Extract at key era numbers
    eras_check = [0, 10, 50, 100, 200, 300, 329]
    comparison = []
    for n in eras_check:
        if n < len(a_arr):
            t_gyr = n * TAU_0_YR / 1e9
            z_red = 1.0 / a_arr[n] - 1 if a_arr[n] > 0 else float('inf')
            comparison.append({
                "era": n,
                "t_gyr": t_gyr,
                "a": float(a_arr[n]),
                "z": float(z_red) if np.isfinite(z_red) else 999,
                "E_map": float(E_map[n]),
                "E_lcdm": float(E_standard[n]),
                "E_no_lambda": float(E_no_lambda[n]),
                "q_map": float(q_map[n]),
            })

    # Did the map produce acceleration (q < 0)?
    q_today = float(q_map[min(329, len(q_map)-1)])
    q_negative_eras = [i for i in range(len(q_map)) if q_map[i] < -0.01]

    return {
        "n_eras": n_eras,
        "comparison": comparison,
        "q_today": q_today,
        "accelerating": q_today < 0,
        "n_accelerating_eras": len(q_negative_eras),
        "first_accelerating_era": q_negative_eras[0] if q_negative_eras else None,
        "a_final": float(a_arr[-1]),
        "H_final_hz": float(H_arr[-1]),
    }


def era_map_with_residual(n_eras: int = N_ERAS,
                          residual_fraction: float = 0.0) -> dict:
    """Era map where each era leaves a small RESIDUAL.

    The idea: each constitutive relaxation cycle doesn't reach
    equilibrium perfectly. A fraction ε of the deviation persists
    as a "memory residual" that accumulates across eras.

    After N eras: accumulated residual ~ N × ε × (typical deviation)

    If ε is set by the constitutive equation's own structure
    (e.g., ε = exp(-1) ≈ 0.368 — one e-folding per era), then
    the accumulated residual after 330 eras could be significant.

    residual_fraction: fraction of (z_target - H²) that persists
    after each era. If 0, computed from exp(-tau_era/tau_0) = exp(-1).
    """
    if residual_fraction <= 0:
        # One era = one τ₀ → residual = exp(-1) ≈ 0.368
        residual_fraction = np.exp(-1)

    a_init = 1e-4
    H2_init = H0_SI**2 * (OMEGA_R * a_init**(-4) + OMEGA_M * a_init**(-3))

    H2_history = [H2_init]
    a_history = [a_init]
    accumulated_residual = 0.0
    residual_history = [0.0]

    H2 = H2_init
    a = a_init

    n_sub = 200
    dt = TAU_0_S / n_sub

    for era in range(n_eras):
        # Evolve one era with matter content
        for _ in range(n_sub):
            H = np.sqrt(max(H2, 1e-60))
            z_target = H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3))

            # The effective target includes accumulated residual
            z_eff = z_target + accumulated_residual

            dH2_dt = (z_eff - H2) / TAU_0_S
            H2 = H2 + dH2_dt * dt
            H2 = max(H2, 1e-60)

            H = np.sqrt(max(H2, 1e-60))
            a = a + a * H * dt

        # End of era: compute residual
        z_target_end = H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3))
        era_deviation = abs(z_target_end - H2)
        accumulated_residual += residual_fraction * era_deviation

        H2_history.append(H2)
        a_history.append(a)
        residual_history.append(accumulated_residual)

    a_arr = np.array(a_history)
    H_arr = np.sqrt(np.array(H2_history))
    res_arr = np.array(residual_history)

    # What fraction of H² today is from accumulated residual?
    H2_today = H2_history[-1]
    res_fraction = accumulated_residual / H2_today if H2_today > 0 else 0

    # Compare residual to Ω_Λ × H₀²
    lambda_H2 = OMEGA_LAMBDA * H0_SI**2
    res_vs_lambda = accumulated_residual / lambda_H2 if lambda_H2 > 0 else 0

    # E(z) comparison at key eras
    comparison = []
    for n in [0, 50, 100, 200, 300, 329]:
        if n < len(a_arr):
            E_map = float(H_arr[n] / H0_SI)
            z_red = 1.0 / a_arr[n] - 1 if a_arr[n] > 0 else 999
            E_lcdm = float(np.sqrt(OMEGA_R * a_arr[n]**(-4) + OMEGA_M * a_arr[n]**(-3) + OMEGA_LAMBDA))
            comparison.append({
                "era": n, "t_gyr": n * TAU_0_YR / 1e9,
                "E_map": E_map, "E_lcdm": E_lcdm,
                "residual": float(res_arr[n]),
            })

    return {
        "n_eras": n_eras,
        "residual_fraction_per_era": residual_fraction,
        "accumulated_residual_H2": accumulated_residual,
        "residual_as_fraction_of_H2": res_fraction,
        "residual_vs_lambda_H2": res_vs_lambda,
        "comparison": comparison,
        "interpretation": (
            f"After {n_eras} eras with ε = {residual_fraction:.3f} per era: "
            f"accumulated residual = {accumulated_residual:.2e} Hz². "
            f"Fraction of H² today: {res_fraction:.2e}. "
            f"Ratio to Ω_Λ H₀²: {res_vs_lambda:.2e}. "
            f"{'SIGNIFICANT' if res_vs_lambda > 0.01 else 'Negligible'}."
        ),
    }


def full_era_analysis() -> dict:
    """Complete era map analysis."""
    no_lambda = era_map_no_lambda()
    with_residual = era_map_with_residual()

    # Also try different residual fractions
    residual_scan = []
    for eps in [0.01, 0.1, 0.368, 0.5, 0.9, 0.99]:
        r = era_map_with_residual(residual_fraction=eps)
        residual_scan.append({
            "epsilon": eps,
            "accumulated": r["accumulated_residual_H2"],
            "fraction_of_H2": r["residual_as_fraction_of_H2"],
            "vs_lambda": r["residual_vs_lambda_H2"],
        })

    return {
        "no_lambda": no_lambda,
        "with_residual": with_residual,
        "residual_scan": residual_scan,
        "n_eras_in_universe": N_ERAS,
        "tau_0_myr": TAU_0_YR / 1e6,
    }
