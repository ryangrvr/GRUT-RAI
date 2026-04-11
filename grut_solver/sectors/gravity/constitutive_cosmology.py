"""
Constitutive Cosmology — The Universe as a Constitutive System

THE IDEA: Apply the GRUT constitutive equation directly to the universe
as a whole. Not a perturbative correction to Friedmann. The Friedmann
equation IS the constitutive equation.

  τ₀ dz/dt + z = z_target[z]

where z is the cosmic state and z_target is the de Sitter vacuum
that everything relaxes toward.

The insight: after 330 time constants (13.8 Gyr / 41.9 Myr), the
relaxation is essentially complete. Late-time behavior = exponential
approach to z_target = constant H. This IS the observed acceleration.
No dark energy field. No cosmological constant. Just relaxation.

STATUS: Toy model → test whether the constitutive equation with τ₀
reproduces radiation → matter → acceleration with zero additional parameters.
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, K_B

# Canonical GRUT scale
TAU_0_YR = 41.9e6              # 41.9 Myr
TAU_0_S = TAU_0_YR * 3.1557e7  # in seconds

# Cosmological parameters (inputs, not free parameters)
H0_KM_S_MPC = 70.0
H0_SI = H0_KM_S_MPC * 1e3 / 3.086e22  # Hz
T_UNIVERSE_S = 13.8e9 * 3.1557e7       # age of universe in seconds
T_UNIVERSE_YR = 13.8e9

# Standard densities
OMEGA_M = 0.3
OMEGA_R = 9.0e-5
OMEGA_LAMBDA = 1.0 - OMEGA_M - OMEGA_R


# =========================================================================
# MODEL 1: Linear constitutive Friedmann
# =========================================================================

def linear_constitutive_H(n_steps: int = 10000) -> dict:
    """Simplest model: H(t) satisfies the constitutive equation directly.

    τ₀ dH/dt + H = H_target

    where H_target = H_∞ = const (the de Sitter target).

    Solution: H(t) = H_∞ + (H_0_init - H_∞) exp(-t/τ₀)

    At early times (t << τ₀): H changes rapidly (radiation/matter-like)
    At late times (t >> τ₀): H → H_∞ (de Sitter, constant H = acceleration)

    Problem: this is too simple — it gives pure exponential decay to H_∞,
    no radiation/matter transition. But it shows the principle.
    """
    H_inf = H0_SI * np.sqrt(OMEGA_LAMBDA)  # de Sitter target
    H_init = H0_SI * 100  # rough early-universe H (much larger)

    t_array = np.linspace(0, T_UNIVERSE_S, n_steps)
    H_array = H_inf + (H_init - H_inf) * np.exp(-t_array / TAU_0_S)

    # Scale factor from H = da/(a dt)
    a_array = np.zeros(n_steps)
    a_array[0] = 1e-4  # early scale factor
    dt = t_array[1] - t_array[0]
    for i in range(n_steps - 1):
        a_array[i + 1] = a_array[i] * (1 + H_array[i] * dt)

    # After 330 τ₀: exp(-330) ~ 10^-143 → H ≈ H_∞ exactly
    n_tau = T_UNIVERSE_S / TAU_0_S

    return {
        "model": "linear",
        "t_yr": (t_array / 3.1557e7).tolist(),
        "H_hz": H_array.tolist(),
        "a": a_array.tolist(),
        "H_inf_hz": H_inf,
        "n_tau_constants": n_tau,
        "H_final_over_H_inf": H_array[-1] / H_inf,
        "note": (
            f"After {n_tau:.0f} time constants, H = H_∞ to 10^{-n_tau/np.log(10):.0f}. "
            f"The linear model gives pure de Sitter approach but no matter era."
        ),
    }


# =========================================================================
# MODEL 2: Nonlinear constitutive Friedmann
# =========================================================================

def nonlinear_z_target(z: float, a: float) -> float:
    """Nonlinear target functional z_target[z, a].

    z = H² (Hubble rate squared, the natural Friedmann variable)

    The target: z_target encodes what the universe is relaxing TOWARD
    at each epoch. This is determined by the energy content:

    z_target(a) = H₀² [Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ]

    This IS the standard Friedmann equation rewritten as a target.
    The constitutive equation says H² approaches this target with
    relaxation time τ₀.

    The key: the target itself depends on a, which depends on H,
    which depends on how fast we're approaching the target.
    This is SELF-REFERENTIAL — z_target depends on the history of z.
    """
    return H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3) + OMEGA_LAMBDA)


def constitutive_friedmann(n_steps: int = 50000,
                           tau_factor: float = 1.0) -> dict:
    """The full nonlinear constitutive Friedmann equation.

    Let z = H². The constitutive equation is:

      τ₀ dz/dt + z = z_target[a(t)]

    where a(t) evolves via da/dt = a × sqrt(z).

    This is a coupled ODE system:
      dz/dt = (z_target(a) - z) / τ₀
      da/dt = a × sqrt(max(z, 0))

    The standard Friedmann equation is the τ₀ → 0 limit:
      z = z_target instantly → H² = H₀²[Ω_r/a⁴ + Ω_m/a³ + Ω_Λ]

    With finite τ₀, H² LAGS behind the target. The question:
    does this lag produce the right expansion history?
    """
    tau = TAU_0_S * tau_factor

    # Integration: from early times to today
    # Use conformal-like variable: integrate in ln(a) for stability
    ln_a_init = np.log(1e-6)  # a = 10^-6 (deep radiation era)
    ln_a_final = 0.0          # a = 1 (today)

    ln_a = np.linspace(ln_a_init, ln_a_final, n_steps)
    d_ln_a = ln_a[1] - ln_a[0]
    a_array = np.exp(ln_a)

    z_standard = np.zeros(n_steps)  # H² from standard Friedmann
    z_constitutive = np.zeros(n_steps)
    t_array = np.zeros(n_steps)

    # Standard H²
    for i in range(n_steps):
        a = a_array[i]
        z_standard[i] = nonlinear_z_target(0, a)

    # Initial condition: start at standard value (in equilibrium at early times)
    z_constitutive[0] = z_standard[0]

    for i in range(n_steps - 1):
        a = a_array[i]
        H = np.sqrt(max(z_constitutive[i], 1e-50))

        # dt = da / (a H) = d(ln a) / H
        dt = d_ln_a / H if H > 1e-50 else 1e30

        # Constitutive relaxation
        z_target = nonlinear_z_target(z_constitutive[i], a)
        dz_dt = (z_target - z_constitutive[i]) / tau

        z_constitutive[i + 1] = z_constitutive[i] + dz_dt * dt
        z_constitutive[i + 1] = max(z_constitutive[i + 1], 1e-50)

        t_array[i + 1] = t_array[i] + dt

    H_standard = np.sqrt(z_standard)
    H_constitutive = np.sqrt(np.maximum(z_constitutive, 0))

    # E(z_redshift) = H / H_0
    E_standard = H_standard / H0_SI
    E_constitutive = H_constitutive / H0_SI

    # Deceleration parameter: q = -1 - (dH/dt)/H²
    # In ln(a): q = -1 - (1/H) dH/d(ln a)
    q_standard = np.zeros(n_steps)
    q_constitutive = np.zeros(n_steps)
    for i in range(1, n_steps - 1):
        if H_standard[i] > 0:
            dH = (H_standard[i + 1] - H_standard[i - 1]) / (2 * d_ln_a)
            q_standard[i] = -1 - dH / H_standard[i]
        if H_constitutive[i] > 0:
            dH = (H_constitutive[i + 1] - H_constitutive[i - 1]) / (2 * d_ln_a)
            q_constitutive[i] = -1 - dH / H_constitutive[i]

    # Extract at key redshifts
    z_redshift = 1.0 / a_array - 1
    comparison = []
    for z_target_val in [0.0, 0.5, 1.0, 1.5, 2.0, 5.0, 10.0]:
        idx = np.argmin(np.abs(z_redshift - z_target_val))
        E_s = float(E_standard[idx])
        E_c = float(E_constitutive[idx])
        delta = abs(E_c - E_s) / E_s if E_s > 0 else 0
        q_s = float(q_standard[idx])
        q_c = float(q_constitutive[idx])
        comparison.append({
            "z": z_target_val,
            "E_standard": E_s,
            "E_constitutive": E_c,
            "delta_E_pct": delta * 100,
            "q_standard": q_s,
            "q_constitutive": q_c,
        })

    # The critical question: is q < 0 today?
    q_today_std = float(q_standard[np.argmin(np.abs(z_redshift))])
    q_today_con = float(q_constitutive[np.argmin(np.abs(z_redshift))])

    # Transition redshift: where q crosses zero
    z_trans_std = None
    z_trans_con = None
    for i in range(len(q_standard) - 1):
        if q_standard[i] > 0 and q_standard[i + 1] < 0 and z_trans_std is None:
            z_trans_std = float(z_redshift[i])
        if q_constitutive[i] > 0 and q_constitutive[i + 1] < 0 and z_trans_con is None:
            z_trans_con = float(z_redshift[i])

    return {
        "model": "nonlinear_constitutive",
        "tau_0_yr": TAU_0_YR * tau_factor,
        "tau_0_s": tau * tau_factor,
        "n_tau_in_universe": T_UNIVERSE_S / tau,
        "comparison": comparison,
        "q_today_standard": q_today_std,
        "q_today_constitutive": q_today_con,
        "accelerating_standard": q_today_std < 0,
        "accelerating_constitutive": q_today_con < 0,
        "z_transition_standard": z_trans_std,
        "z_transition_constitutive": z_trans_con,
        "max_deviation_pct": max(r["delta_E_pct"] for r in comparison),
        "z_redshift": z_redshift.tolist(),
        "E_standard": E_standard.tolist(),
        "E_constitutive": E_constitutive.tolist(),
        "q_standard": q_standard.tolist(),
        "q_constitutive": q_constitutive.tolist(),
        "t_gyr": (t_array / (3.1557e7 * 1e9)).tolist(),
    }


# =========================================================================
# MODEL 3: Pure constitutive (no Friedmann — derive expansion from τ alone)
# =========================================================================

def pure_constitutive_universe(n_steps: int = 50000) -> dict:
    """What if the expansion history IS the constitutive relaxation?

    The most radical model: there is no separate Friedmann equation.
    The scale factor a(t) IS z(t), and z_target is the de Sitter
    fixed point a_∞ (or more precisely, the state where da/dt = H_∞ a).

    In this picture:
      τ₀ d²a/dt² + da/dt = H_∞ a

    This is a damped oscillator with exponential driving.
    The solution has:
      - Transient: decaying modes ~ exp(-t/τ₀) [early universe: fast dynamics]
      - Steady state: a ~ exp(H_∞ t) [late universe: de Sitter]

    The transition from transient to steady state IS the matter→acceleration
    transition.
    """
    H_inf = H0_SI * np.sqrt(OMEGA_LAMBDA)  # de Sitter attractor

    # ODE: τ₀ a'' + a' = H_∞ a
    # Let v = a' = da/dt. Then:
    # τ₀ dv/dt + v = H_∞ a
    # da/dt = v

    t_max = T_UNIVERSE_S * 1.2
    dt = t_max / n_steps
    t = np.zeros(n_steps)
    a = np.zeros(n_steps)
    v = np.zeros(n_steps)  # da/dt

    # Initial conditions: early universe
    a[0] = 1e-10
    v[0] = H_inf * a[0] * 1e6  # initially expanding much faster than de Sitter

    for i in range(n_steps - 1):
        t[i + 1] = t[i] + dt

        # τ₀ dv/dt = H_∞ a - v
        dv_dt = (H_inf * a[i] - v[i]) / TAU_0_S

        v[i + 1] = v[i] + dv_dt * dt
        a[i + 1] = a[i] + v[i] * dt

        # Prevent negative scale factor
        if a[i + 1] <= 0:
            a[i + 1] = a[i] * 0.999
            v[i + 1] = max(v[i + 1], 0)

    # Hubble parameter H = v/a
    H = np.where(a > 1e-30, v / a, 0)

    # Deceleration parameter
    q = np.zeros(n_steps)
    for i in range(1, n_steps - 1):
        if H[i] > 0:
            dH_dt = (H[i + 1] - H[i - 1]) / (2 * dt)
            q[i] = -1 - dH_dt / H[i]**2

    # Normalize a so a(today) = 1
    t_today_idx = np.argmin(np.abs(t - T_UNIVERSE_S))
    a_today = a[t_today_idx]
    if a_today > 0:
        a = a / a_today

    # Effective equation of state w from q: q = (1+3w)/2 for single component
    w_eff = (2 * q - 1) / 3

    return {
        "model": "pure_constitutive",
        "t_gyr": (t / (3.1557e7 * 1e9)).tolist(),
        "a": a.tolist(),
        "H_hz": H.tolist(),
        "q": q.tolist(),
        "w_eff": w_eff.tolist(),
        "H_inf_hz": H_inf,
        "H_today_hz": float(H[t_today_idx]),
        "q_today": float(q[t_today_idx]),
        "accelerating": float(q[t_today_idx]) < 0,
        "a_normalized": True,
    }


# =========================================================================
# COMPARISON AND VERDICT
# =========================================================================

def full_constitutive_cosmology_analysis() -> dict:
    """Run all three models and compare."""
    linear = linear_constitutive_H()
    nonlinear = constitutive_friedmann()
    pure = pure_constitutive_universe()

    return {
        "linear": {
            "n_tau": linear["n_tau_constants"],
            "H_final_over_H_inf": linear["H_final_over_H_inf"],
            "produces_acceleration": True,
            "produces_matter_era": False,
            "verdict": "Too simple — pure exponential, no matter era",
        },
        "nonlinear": {
            "comparison": nonlinear["comparison"],
            "q_today": nonlinear["q_today_constitutive"],
            "accelerating": nonlinear["accelerating_constitutive"],
            "z_transition": nonlinear["z_transition_constitutive"],
            "max_deviation_pct": nonlinear["max_deviation_pct"],
            "produces_acceleration": nonlinear["accelerating_constitutive"],
            "produces_matter_era": nonlinear["z_transition_constitutive"] is not None,
            "verdict": (
                f"Nonlinear constitutive: q_today = {nonlinear['q_today_constitutive']:.3f}, "
                f"z_transition = {nonlinear['z_transition_constitutive']}, "
                f"max deviation from LCDM = {nonlinear['max_deviation_pct']:.2f}%. "
                f"{'ACCELERATING' if nonlinear['accelerating_constitutive'] else 'NOT accelerating'} today."
            ),
        },
        "pure": {
            "q_today": pure["q_today"],
            "accelerating": pure["accelerating"],
            "H_today": pure["H_today_hz"],
            "produces_acceleration": pure["accelerating"],
            "verdict": (
                f"Pure constitutive: q_today = {pure['q_today']:.3f}. "
                f"{'ACCELERATING' if pure['accelerating'] else 'NOT accelerating'}. "
                f"Damped approach to de Sitter with τ₀ = 41.9 Myr."
            ),
        },
        "tau_0_yr": TAU_0_YR,
        "n_tau_in_universe": T_UNIVERSE_YR / TAU_0_YR,
    }
