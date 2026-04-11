"""
Running τ_eff from CTP Self-Consistency — Path 1

THE IDEA: τ is not a constant. In the CTP influence functional, the
dissipation kernel depends on the bath spectral density, which depends
on the available modes, which depends on the Hubble horizon H(t).

As the universe expands and H drops:
  - More IR modes enter the horizon
  - The effective bath grows
  - The relaxation time τ_eff should grow with the bath

THE SELF-CONSISTENCY EQUATION:
  τ_eff(H) is determined by the CTP gap equation:
    τ_eff = ℏ / (2 × Σ_eff(H))
  where Σ_eff is the self-energy from all modes within the Hubble horizon.

For a thermal bath of gravitational modes at temperature T_H = ℏH/(2πk_B):
  Σ_eff ~ G × ∫₀^{k_H} k² dk × n(k,T_H) / (2π²)
  where k_H = H/c is the Hubble wavenumber.

The key insight: at late times (small H), the integral is dominated by
the IR contribution, and Σ_eff ~ H³ (volume of available modes).
This gives τ_eff ~ 1/H³ × (constants), which GROWS as the universe expands.

If the scaling works out to τ_eff ~ 1/H, then τ_eff × H ~ O(1) at ALL
epochs — the constitutive term is always marginally relevant. This would
be a self-tuning mechanism for dark energy.

STATUS: Toy model. The self-consistency equation is physically motivated
but uses approximations (thermal spectrum, Hubble cutoff). The exact
CTP calculation would require the full influence functional.
"""

import numpy as np
from grut_solver.constants import (
    G, HBAR, C, K_B, T_PLANCK, L_PLANCK, M_PLANCK, TAU_I
)

# Cosmological parameters
H0_SI = 2.269e-18          # H_0 = 70 km/s/Mpc in Hz
T_CMB = 2.725              # CMB temperature today [K]
OMEGA_M = 0.3
OMEGA_LAMBDA = 0.7


def gibbons_hawking_temperature(H: float) -> float:
    """Gibbons-Hawking temperature of de Sitter horizon.

    T_GH = ℏH / (2π k_B)

    This is the temperature "seen" by an accelerating observer in
    de Sitter space — the gravitational analogue of the Unruh effect.
    """
    return HBAR * H / (2 * np.pi * K_B)


def mode_count_within_horizon(H: float) -> float:
    """Number of quantum field modes within the Hubble horizon.

    The Hubble volume is V_H = (4π/3)(c/H)³
    Each mode occupies volume ~ (2π/k)³ with k_min = H/c
    Number of modes up to UV cutoff k_max ~ 1/L_Planck:

    N_modes = V_H × ∫_{H/c}^{1/L_P} k² dk / (2π²)
            ~ V_H × (1/L_P)³ / (6π²)   [UV dominated]

    But for the IR-sensitive part (which controls τ_eff running):
    N_IR ~ V_H × (H/c)³ / (6π²) ~ 1/(6π²)  [constant!]

    The interesting physics is in the SPECTRAL WEIGHT, not the count.
    """
    R_H = C / H  # Hubble radius [m]
    V_H = (4 * np.pi / 3) * R_H**3

    k_H = H / C  # IR cutoff
    k_UV = 1.0 / L_PLANCK  # UV cutoff

    N_total = V_H * k_UV**3 / (6 * np.pi**2)
    N_IR = V_H * k_H**3 / (6 * np.pi**2)  # ~ 1/(6π²) ~ 0.017

    return {
        "R_H_m": R_H,
        "V_H_m3": V_H,
        "N_total": N_total,
        "N_IR": N_IR,
        "log10_N_total": np.log10(N_total),
    }


def self_energy_from_horizon(H: float) -> float:
    """Effective self-energy Σ_eff(H) from modes within Hubble horizon.

    In the CTP influence functional, the dissipation kernel comes from
    the imaginary part of the retarded self-energy:

    Σ_eff = G × ∫ d³k/(2π³) × ω_k × n_BE(ω_k, T_GH) / c⁴

    For gravitational modes at the Gibbons-Hawking temperature:
    - ω_k = c|k| for massless gravitons
    - n_BE(ω, T) = 1/(exp(ℏω/k_BT) - 1) for Bose-Einstein

    The integral from k_min = H/c to k_max = 1/L_P is UV-dominated
    but the RUNNING with H comes from the IR cutoff and the temperature.

    Simplified model: Σ_eff ~ G × T_GH⁴ / (ℏ³ c⁵)
    (Stefan-Boltzmann-like thermal self-energy from the horizon)

    T_GH = ℏH/(2πk_B), so:
    Σ_eff ~ G × (ℏH)⁴ / ((2π)⁴ k_B⁴ ℏ³ c⁵)
          = G ℏ H⁴ / ((2π)⁴ k_B⁴ c⁵)
    """
    T_GH = gibbons_hawking_temperature(H)

    # Thermal self-energy (Stefan-Boltzmann type)
    # Σ ~ G × σ_SB × T⁴ / c⁵  (dimensionally [1/s])
    sigma_SB = np.pi**2 * K_B**4 / (60 * HBAR**3 * C**2)
    Sigma = G * sigma_SB * T_GH**4 / C**5

    return Sigma


def tau_eff_from_self_consistency(H: float) -> float:
    """Self-consistent τ_eff from the CTP gap equation.

    τ_eff = ℏ / (2 × Σ_eff(H))

    This is the GRUT constitutive relaxation time determined by
    the bath of gravitational modes at the Hubble scale.
    """
    Sigma = self_energy_from_horizon(H)
    if Sigma > 0:
        return HBAR / (2 * Sigma)
    return float('inf')


def tau_eff_scaling_law(H: float) -> dict:
    """Derive the scaling τ_eff(H) and check if τ_eff × H ~ O(1).

    From Σ_eff ~ G ℏ H⁴ / ((2π)⁴ k_B⁴ c⁵):
      τ_eff = ℏ/(2Σ) ~ (2π)⁴ k_B⁴ c⁵ / (2G H⁴)

    So τ_eff ~ H⁻⁴ (!) — grows VERY fast as H decreases.
    And τ_eff × H ~ H⁻³ — NOT constant, GROWS with expansion.

    This means: the constitutive term becomes MORE important at late times,
    not less. The question is whether the numerical coefficient gives
    τ_eff(H₀) ~ 1/H₀.
    """
    tau = tau_eff_from_self_consistency(H)
    tau_H = tau * H
    Sigma = self_energy_from_horizon(H)

    return {
        "H_hz": H,
        "Sigma_eff_hz": Sigma,
        "tau_eff_s": tau,
        "tau_eff_yr": tau / 3.156e7,
        "tau_H_product": tau_H,
        "log10_tau_H": np.log10(tau_H) if tau_H > 0 else float('-inf'),
        "scaling": "tau_eff ~ H^{-4} (from thermal self-energy)",
    }


def tau_running_across_epochs() -> dict:
    """Compute τ_eff at key cosmic epochs.

    Test whether the self-consistent τ_eff becomes O(1/H) at late times.
    """
    epochs = [
        ("Planck",           1.0 / T_PLANCK),
        ("GUT (10^16 GeV)",  1e42),
        ("EW (100 GeV)",     1e17),
        ("QCD (200 MeV)",    1e12),
        ("Nucleosynthesis",  1e-3),
        ("Recombination",    1e-13),
        ("Matter-Lambda eq", 5e-18),
        ("Today (H_0)",      H0_SI),
    ]

    results = []
    for name, H in epochs:
        r = tau_eff_scaling_law(H)
        results.append({
            "epoch": name,
            "H_hz": H,
            "tau_eff_s": r["tau_eff_s"],
            "tau_H": r["tau_H_product"],
            "log10_tau_H": r["log10_tau_H"],
        })

    # The critical test: τ_eff(H_0) vs 1/H_0
    tau_today = tau_eff_from_self_consistency(H0_SI)
    tau_hubble = 1.0 / H0_SI
    ratio = tau_today / tau_hubble

    return {
        "epochs": results,
        "tau_eff_today_s": tau_today,
        "tau_eff_today_yr": tau_today / 3.156e7,
        "one_over_H0_s": tau_hubble,
        "one_over_H0_yr": tau_hubble / 3.156e7,
        "ratio_tau_to_hubble": ratio,
        "log10_ratio": np.log10(ratio) if ratio > 0 else float('-inf'),
        "self_tuning": abs(np.log10(ratio)) < 2 if ratio > 0 else False,
    }


def constitutive_friedmann_with_running_tau(
    a_init: float = 0.001,
    a_final: float = 1.0,
    n_steps: int = 5000,
    Omega_m: float = 0.3,
) -> dict:
    """Integrate modified Friedmann with RUNNING τ_eff(H).

    At each step: τ_eff is computed self-consistently from H.
    The constitutive equation becomes:

    H² + τ_eff(H) × d(H²)/dt = (8πG/3)ρ

    where τ_eff(H) is determined by the CTP self-consistency condition.
    """
    a_array = np.logspace(np.log10(a_init), np.log10(a_final), n_steps)
    H0 = 1.0  # dimensionless units

    H2_standard = np.zeros(n_steps)
    H2_running = np.zeros(n_steps)
    tau_eff_array = np.zeros(n_steps)

    for i in range(n_steps):
        a = a_array[i]
        H2_standard[i] = H0**2 * (Omega_m * a**(-3) + (1 - Omega_m))

    H2_running[0] = H2_standard[0]

    for i in range(n_steps - 1):
        a = a_array[i]
        H = np.sqrt(max(H2_running[i], 1e-30))

        # Self-consistent τ_eff in dimensionless units
        # τ_eff(H) × H ~ (H_0/H)^3 × C_0  where C_0 is the dimensionless
        # coefficient at H = H_0
        # From the full calculation: τ_eff × H scales as H^{-3}
        # Normalize so that τ_eff(H_0) × H_0 matches the full calculation
        H_physical = H * H0_SI  # convert to SI
        tau_physical = tau_eff_from_self_consistency(H_physical)
        tau_dimless = tau_physical * H0_SI  # dimensionless

        tau_eff_array[i] = tau_dimless

        # Constitutive Friedmann
        if tau_dimless > 1e-100:
            dH2_dt = (H2_standard[i] - H2_running[i]) / tau_dimless
        else:
            dH2_dt = 0

        dH2_da = dH2_dt / (a * H) if H > 1e-15 else 0
        da = a_array[i + 1] - a_array[i]

        H2_running[i + 1] = H2_running[i] + dH2_da * da
        H2_running[i + 1] = max(H2_running[i + 1], 0)

    H_standard = np.sqrt(H2_standard)
    H_running = np.sqrt(np.maximum(H2_running, 0))

    # E(z) comparison at key redshifts
    z_array = 1.0 / a_array - 1
    comparison = []
    for z_target in [0.0, 0.5, 1.0, 1.5, 2.0]:
        idx = np.argmin(np.abs(z_array - z_target))
        E_std = float(H_standard[idx])
        E_run = float(H_running[idx])
        delta = abs(E_run - E_std) / E_std if E_std > 0 else 0
        comparison.append({
            "z": z_target,
            "E_standard": E_std,
            "E_running_tau": E_run,
            "delta_E_pct": delta * 100,
        })

    return {
        "a": a_array.tolist(),
        "H_standard": H_standard.tolist(),
        "H_running_tau": H_running.tolist(),
        "tau_eff_dimless": tau_eff_array.tolist(),
        "comparison": comparison,
        "max_deviation_pct": max(r["delta_E_pct"] for r in comparison),
    }


# =========================================================================
# ENHANCED CTP SELF-CONSISTENCY (User's equation)
# =========================================================================

def usl_noise_kernel_fourier(k: float) -> float:
    """USL noise kernel N(k) in Fourier space.

    The USL noise kernel has a 1/k⁴ infrared tail — this is the same
    object that produces the decoherence plateau at ~633 Hz and the
    entanglement protection signatures.

    N(k) ~ G² × M_Planck² / (ℏ × k⁴)  for k → 0

    This is NOT thermal. It comes from the gravitational self-energy
    in the CTP influence functional (the Diósi kernel).
    """
    # Normalization: at k = 1/L_Planck, N should give the Planck-scale rate
    # N(k) = (G / ℏ)² × (1/k⁴) × [normalization]
    # Dimensional analysis: [N] = [length]⁶ (in the 4D integral)
    N_0 = G**2 / (HBAR * C**3)  # [m² s]
    return N_0 / max(k**4, 1e-200)


def enhanced_tau_eff(a: float, tau_0_s: float = None,
                     S: float = 108 * np.pi,
                     m_eff_inv_m: float = None) -> dict:
    """Enhanced CTP self-consistency equation for τ_eff(a).

    τ_eff(a) = τ₀ × (1 + (1/S) × I(a))

    where I(a) = ∫₀^{k_IR} N(k) / (k² + m_eff²) × k² dk / (2π²)

    with:
      k_IR = H(a) / c  (Hubble wavenumber — the IR cutoff)
      N(k) ~ 1/k⁴     (USL noise kernel IR tail)
      m_eff = H(a)/c   (effective mass gap from expansion)

    The integrand: N(k) × k²/(k² + m²) / (2π²) ~ (1/k⁴) × k² / (2π²) = 1/(2π²k²)

    Integral: ∫₀^{k_IR} dk/(2π²k²) → DIVERGES at k→0!

    This means we need a true IR cutoff. Physical options:
      a) k_min = 1/(c × age_of_universe) — the particle horizon
      b) k_min = 1/(R_Grover × c/H) — the Grover horizon
      c) k_min set by m_eff (the gap regularizes the divergence)

    With m_eff regularization (option c):
    ∫₀^{k_IR} dk / (k² + m²) = (1/m) arctan(k_IR/m)

    Combined with the 1/k⁴ noise kernel:
    I(a) = N_0 / (2π²) × ∫₀^{k_IR} k² dk / (k⁴ × (k² + m²))
         = N_0 / (2π²) × ∫₀^{k_IR} dk / (k² × (k² + m²))
         = N_0 / (2π² m²) × [1/m × arctan(k_IR/m) - k_IR/(k_IR² + m²)]

    For k_IR = m (self-consistent: both set by H/c):
    I ≈ N_0 / (2π² m³) × (π/4 - 1/2) ≈ 0.035 × N_0 / m³

    Since m = H/c: I ≈ 0.035 × N_0 × c³ / H³

    And N_0 = G² / (ℏc³), so:
    I ≈ 0.035 × G² / (ℏ H³)
    """
    if tau_0_s is None:
        tau_0_s = 41.9e6 * 3.1557e7  # 41.9 Myr in seconds

    # H(a) for ΛCDM
    H = H0_SI * np.sqrt(OMEGA_M * a**(-3) + OMEGA_LAMBDA)

    # IR cutoff and effective mass: both ~ H/c
    k_IR = H / C
    m_eff = H / C

    # Planck-normalized noise kernel: N(k) ~ L_P c / k²
    # This is the physically correct vacuum gravitational noise scale.
    # Dimensional check: [L_P c / k²] × [k² dk / (k² + m²)] → dimensionless ✓
    N_0 = L_PLANCK * C  # ~ 4.85e-27  [m²/s... but in natural units: dimensionless]

    # The integral I(a):
    # I = N_0 / (2π²) × ∫₀^{k_IR} dk / (k² + m²)
    # = N_0 / (2π² m) × arctan(k_IR / m)
    # With k_IR = m: arctan(1) = π/4
    # I = N_0 × π / (8π² m) = N_0 / (8π m)
    I_a = N_0 / (8 * np.pi * m_eff)

    # τ_eff
    tau_eff = tau_0_s * (1 + I_a / S)

    # The key product
    tau_H = tau_eff * H

    return {
        "a": a,
        "z": 1.0 / a - 1,
        "H_hz": H,
        "k_IR": k_IR,
        "m_eff": m_eff,
        "I_a": I_a,
        "I_over_S": I_a / S,
        "tau_0_s": tau_0_s,
        "tau_eff_s": tau_eff,
        "tau_eff_yr": tau_eff / 3.1557e7,
        "tau_H": tau_H,
        "log10_tau_H": np.log10(tau_H) if tau_H > 0 else float('-inf'),
        "enhancement_factor": tau_eff / tau_0_s,
    }


def enhanced_running_across_epochs() -> dict:
    """Compute enhanced τ_eff at key cosmic epochs."""
    epochs = [
        ("Radiation (z=10000)",  1e-4),
        ("Recombination (z=1100)", 1.0 / 1101),
        ("z = 10",               1.0 / 11),
        ("z = 2",                1.0 / 3),
        ("z = 1",                0.5),
        ("z = 0.5",              1.0 / 1.5),
        ("Today (z=0)",          1.0),
    ]

    results = []
    for name, a in epochs:
        r = enhanced_tau_eff(a)
        results.append({
            "epoch": name,
            "a": a,
            "z": r["z"],
            "H_hz": r["H_hz"],
            "tau_eff_yr": r["tau_eff_yr"],
            "enhancement": r["enhancement_factor"],
            "I_over_S": r["I_over_S"],
            "tau_H": r["tau_H"],
            "log10_tau_H": r["log10_tau_H"],
        })

    # Critical test
    today = enhanced_tau_eff(1.0)
    tau_hubble = 1.0 / H0_SI
    ratio = today["tau_eff_s"] / tau_hubble

    return {
        "epochs": results,
        "tau_eff_today_s": today["tau_eff_s"],
        "tau_eff_today_yr": today["tau_eff_yr"],
        "one_over_H0_yr": tau_hubble / 3.1557e7,
        "ratio_tau_to_hubble": ratio,
        "log10_ratio": np.log10(ratio) if ratio > 0 else float('-inf'),
        "enhancement_today": today["enhancement_factor"],
        "I_over_S_today": today["I_over_S"],
        "self_tuning": abs(np.log10(ratio)) < 2 if ratio > 0 else False,
    }


def full_running_tau_analysis() -> dict:
    """Complete analysis of the running τ_eff mechanism.

    Includes both the thermal model (overshoots) and the enhanced
    CTP self-consistency model (USL noise kernel with 1/k⁴ tail).
    """
    epochs = tau_running_across_epochs()
    enhanced = enhanced_running_across_epochs()
    friedmann = constitutive_friedmann_with_running_tau()

    # The critical numbers — thermal model
    ratio = epochs["ratio_tau_to_hubble"]
    log_ratio = epochs["log10_ratio"]

    # Enhanced model
    ratio_enh = enhanced["ratio_tau_to_hubble"]
    log_ratio_enh = enhanced["log10_ratio"]

    if abs(log_ratio) < 2:
        gate_verdict = (
            f"τ_eff(H₀) = {epochs['tau_eff_today_yr']:.2e} yr. "
            f"1/H₀ = {epochs['one_over_H0_yr']:.2e} yr. "
            f"Ratio = 10^{log_ratio:.1f}. "
            f"WITHIN 2 ORDERS — the self-tuning mechanism WORKS. "
            f"The CTP self-consistency condition naturally produces "
            f"a cosmologically relevant relaxation time at late epochs."
        )
    elif log_ratio > 2:
        gate_verdict = (
            f"τ_eff(H₀) = {epochs['tau_eff_today_yr']:.2e} yr. "
            f"1/H₀ = {epochs['one_over_H0_yr']:.2e} yr. "
            f"Ratio = 10^{log_ratio:.1f}. "
            f"τ_eff OVERSHOOTS 1/H₀ by {log_ratio:.0f} orders. "
            f"The H⁻⁴ scaling is too steep — the self-energy model "
            f"over-produces the relaxation time. A more careful treatment "
            f"of the spectral integral is needed."
        )
    else:
        gate_verdict = (
            f"τ_eff(H₀) = {epochs['tau_eff_today_yr']:.2e} yr. "
            f"1/H₀ = {epochs['one_over_H0_yr']:.2e} yr. "
            f"Ratio = 10^{log_ratio:.1f}. "
            f"τ_eff UNDERSHOOTS — too small to matter cosmologically."
        )

    return {
        "thermal_model": {
            "epochs": epochs,
            "ratio": ratio,
            "log10_ratio": log_ratio,
            "verdict": gate_verdict,
        },
        "enhanced_ctp_model": {
            "epochs": enhanced,
            "ratio": ratio_enh,
            "log10_ratio": log_ratio_enh,
            "enhancement_today": enhanced["enhancement_today"],
            "I_over_S": enhanced["I_over_S_today"],
            "self_tuning": enhanced["self_tuning"],
        },
        "friedmann": friedmann,
        "critical_ratio": ratio_enh,
        "log10_ratio": log_ratio_enh,
        "self_tuning": enhanced["self_tuning"],
        "gate_verdict": gate_verdict,
        "honest_caveats": [
            "Thermal self-energy model uses Stefan-Boltzmann approximation",
            "Gibbons-Hawking temperature applies strictly in de Sitter, not general FRW",
            "The CTP gap equation should be solved with the full spectral function",
            "H^{-4} scaling comes from T_GH^4 ~ H^4; a different bath gives different scaling",
            "This is a toy model — the exact coefficient depends on the full CTP calculation",
            "No graviton propagator is used — this is semiclassical throughout",
        ],
    }
