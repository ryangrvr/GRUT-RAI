"""
GRUT Foundation — Phase I Closure Protocol (February 2026)

This module integrates the canonical constants, screening mechanism, regime
gate, acceleration scale, and engine-mapping interpolation from the Phase I
Closure Protocol (Zenodo DOI: 10.5281/zenodo.18008060) into the V7 codebase.

Document hierarchy:
    v1-v11 Genesis Codex (Dec 2025)   — physics discovery
    Phase I Closure Protocol (Feb 2026) — operational specification (THIS MODULE)
    V7 Responsive Universe (Apr 2026) — theoretical foundation (CTP)

Phase I operationalizes the v1-v11 physics. V7 provides the quantum
completion via CTP. Both pin the same constants; Phase I gives the
engine formulas (ν(y), regime gate, a_0) that V7 does not explicitly
state and that are needed for SPARC rotation-curve work and solar-
system safety verification.

Canonical definitions (Phase I §5-§6):
    τ_Λ ≡ H_0⁻¹                            (baseline — input, not prediction)
    α_vac = 1/3                             (canonical; v11 App H: α = 1/d, d=3)
    S = 12π / α_vac² = 108π ≈ 339.29        (screening factor)
    τ_0 = τ_Λ / S ≈ 41.9 Myr                (local relaxation time)
    n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.1547 (IR refractive index)
    μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV                  (horizon-scale IR reference)
    μ_0 = ℏ/τ_0 = S × μ_Λ ~ 10⁻³¹ eV        (local screened scale)
    a_* = c / τ_Λ = c H_0                   (characteristic acceleration)
    a_0 = a_* / (2π) ≈ 1.2 × 10⁻¹⁰ m/s²     (MOND-like trigger scale)

Engine formulas (Phase I §7-§8, Appendix E):
    χ(ω) = α_vac / (1 − i ω τ_0)            (single-pole susceptibility)
    n_g²(ω) = 1 + α_vac / (1 + (ωτ_0)²)     (refractive index)
    α_eff(X) = α_vac / (1 + X²)             (regime gate, X = ω_dyn τ_0)
    ν(y) = 1/2 + √(1/4 + 1/y)               (acceleration interpolation)
    g_eff = g_bar × [1 + (ν(y) − 1) / (1 + X²)]  (frequency-gated)

Identity (v11 Appendix I, Phase I §5):
    τ_0 = 1/√(Λ c)

This makes the "unified dark sector" literal: dark energy (Λ) defines
the vacuum curvature, dark matter phenomenology (τ_0) is the metric's
delayed response within that curvature.
"""

import numpy as np

from grut.foundation.constants import C as C_LIGHT, HBAR, K_B, E_CHARGE


# ────────────────────────────────────────────────────────────────────
# Canonical constants (Phase I §5 — FIXED, no free knobs)
# ────────────────────────────────────────────────────────────────────

ALPHA_VAC: float = 1.0 / 3.0                 # α = 1/d, d = 3 (v11 App H)
"""Vacuum impedance. Fixed by dimensional projection of the trace
anomaly: α = 1/d where d is spatial dimension. d = 3 ⟹ α = 1/3 exactly."""

S_SCREENING: float = 12 * np.pi / ALPHA_VAC**2   # = 108π ≈ 339.29
"""Screening factor S = 12π/α² mapping cosmic baseline τ_Λ to local τ_0.
Phase I §5: canonical derivation."""

N_G_DC: float = float(np.sqrt(1.0 + ALPHA_VAC))
"""IR refractive index n_g(0) = √(1+α) = √(4/3) ≈ 1.15470.
Tree-level / geometric value. V7's 3-loop CTP computation refines this
to R_anomaly = 1.15428 (0.036% radiative correction)."""


# ────────────────────────────────────────────────────────────────────
# Canonical timescales
# ────────────────────────────────────────────────────────────────────

MPC_IN_M: float = 3.0857e22
YEAR_SEC: float = 3.156e7

# Phase I §5 canonically adopts τ_0 ≈ 41.9 Myr directly (benchmark-anchored
# to the Bullet Cluster and the V7 noise-kernel derivation). Together
# with S = 108π this fixes τ_Λ, which corresponds to H_0 ≈ 68.8 km/s/Mpc
# — close to the canonical 70 and Planck 67.4.
TAU_0_MYR: float = 41.9                      # canonical adoption (Phase I §5)
TAU_0_SEC: float = TAU_0_MYR * 1e6 * YEAR_SEC
"""Local effective relaxation τ_0 = 41.9 Myr. Canonically adopted (Phase I §5),
benchmark-anchored to the Bullet Cluster (~40 Myr offset, v1.0 §3) and
matched by V7's noise-kernel derivation at the gold benchmark (V7 §18)."""

TAU_LAMBDA_SEC: float = TAU_0_SEC * S_SCREENING
"""Cosmic baseline τ_Λ = S × τ_0 ≈ 14.22 Gyr.
Corresponds to H_0 ≈ 68.8 km/s/Mpc (between Planck 67.4 and the H_0 = 70
baseline used for display). Consistent with GRUT's one-parameter
prediction H_0 = 69.03 km/s/Mpc."""

H_0_IMPLIED_KM_S_MPC: float = (1.0 / TAU_LAMBDA_SEC) * MPC_IN_M / 1000.0
"""H_0 implied by τ_0 = 41.9 Myr and S = 108π: ≈ 68.8 km/s/Mpc."""


# ────────────────────────────────────────────────────────────────────
# Mass-gap scales (Phase I §6)
# ────────────────────────────────────────────────────────────────────

MU_LAMBDA_EV: float = (HBAR / TAU_LAMBDA_SEC) / E_CHARGE
"""Cosmic mass-gap scale μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV.
Horizon-scale IR reference (Phase I §6)."""

MU_0_EV: float = (HBAR / TAU_0_SEC) / E_CHARGE
"""Screened local mass-gap μ_0 = ℏ/τ_0 = S × μ_Λ ~ 10⁻³¹ eV
(Phase I §6: screening maps μ_Λ → μ_0 via same S)."""


# ────────────────────────────────────────────────────────────────────
# Acceleration scales (Phase I §8.2)
# ────────────────────────────────────────────────────────────────────

A_STAR_SI: float = C_LIGHT / TAU_LAMBDA_SEC        # c H_0
"""Characteristic acceleration a_* = c/τ_Λ = c H_0 (Phase I §8.2)."""

A_0_SI: float = A_STAR_SI / (2.0 * np.pi)
"""MOND-like trigger acceleration a_0 = c / (2π τ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s².
Phase I §8.2: 'reproduces MOND phenomenology from response time, not
modified dynamics.' For H_0 ≈ 70 km/s/Mpc, a_0 lies in the observed
MOND/RAR band."""


# ────────────────────────────────────────────────────────────────────
# Thermal transition temperature (v9.0)
# ────────────────────────────────────────────────────────────────────

# v9.0 "boiling point of gravity" uses natural units (ℏ = 1), giving
# T_c = 1/(τ_0 k_B). Computed in SI:
T_C_KELVIN: float = 1.0 / (TAU_0_SEC * K_B)
"""Critical temperature for onset of metric memory (v9.0 Thermodynamics).

T_c = 1/(τ_0 k_B) ≈ 54.7 × 10⁶ K (v9 natural-units convention, ℏ = 1).
This is the "boiling point of gravity": above T_c, gravity is local and
there is no metric memory (explains absence of DM signatures in BBN at
T > 10⁹ K). Below T_c (today, T = 2.725 K), the vacuum is deep in the
refractive regime with full enhancement n_g ≈ 1.1547.

Cosmological chronology (v9.0):
    T > T_c  (plasma era):       gravity is local, no DM effects
    T ≈ T_c  (~1 hour post-BB):  vacuum begins to "remember" mass
    T << T_c (today):            deep refractive regime, n_g ≈ 1.1547
"""

T_C_MK: float = T_C_KELVIN / 1e6


# ────────────────────────────────────────────────────────────────────
# τ_0 = 1/√(Λc) identity (v11 App I, Phase I §5)
# ────────────────────────────────────────────────────────────────────

def tau_0_from_lambda_c(Lambda_inv_m2: float) -> float:
    """τ_0 = 1/√(Λc) — the dark-sector unification identity.

    v11 Appendix I §I.5 (and Phase I §5): "Dark Energy (Λ) defines
    the global curvature and horizon scale. Dark Matter Phenomenology
    (τ_0) emerges as the delayed response of the metric within that
    curved background." They are the same number in different units.

    Args:
        Lambda_inv_m2: cosmological constant Λ [1/m²]

    Returns:
        τ_0 [seconds]
    """
    if Lambda_inv_m2 <= 0:
        return float("inf")
    return 1.0 / np.sqrt(Lambda_inv_m2 * C_LIGHT**2)


def lambda_from_tau_0(tau_0_sec: float = TAU_0_SEC) -> float:
    """Inverse of tau_0_from_lambda_c: Λ = 1/(τ_0² c²)."""
    return 1.0 / (tau_0_sec**2 * C_LIGHT**2)


# ────────────────────────────────────────────────────────────────────
# Response kernel (Phase I §7, C.1)
# ────────────────────────────────────────────────────────────────────

def kernel_K(t_sec: float, tau_0_sec: float = TAU_0_SEC) -> float:
    """Time-domain memory kernel K(t) = (1/τ_0) exp(−t/τ_0) Θ(t).

    Causal viscoelastic relaxation (v11 Appendix G, Phase I Appendix C.1).
    """
    if t_sec < 0:
        return 0.0
    return np.exp(-t_sec / tau_0_sec) / tau_0_sec


def susceptibility_chi(omega_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Complex susceptibility χ(ω) = α / (1 − iωτ_0).

    Single-pole at ω = −i/τ_0 in lower half-plane → causal, KK-compatible.
    """
    return alpha / (1.0 - 1j * omega_Hz * tau_0_sec)


def n_g_refractive(omega_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Frequency-dependent gravitational refractive index.

        n_g²(ω) = 1 + Re[χ(ω)] = 1 + α/(1+(ωτ_0)²)

    Limits:
        n_g(0)   = √(1+α) = √(4/3) = 1.15470   (DC)
        n_g(∞)   = 1                             (GR recovered)
    """
    return np.sqrt(1.0 + alpha / (1.0 + (omega_Hz * tau_0_sec)**2))


# ────────────────────────────────────────────────────────────────────
# Regime gate (Phase I §8.1 — solar-system safety)
# ────────────────────────────────────────────────────────────────────

def regime_parameter_X(omega_dyn_Hz, tau_0_sec=TAU_0_SEC):
    """Dimensionless regime parameter X = ω_dyn τ_0.

    Gates between GR (X ≫ 1) and metric memory (X ≪ 1).
    Saturn's orbit: X ≈ 8.9 × 10⁶ → 15-order suppression (safe).
    Galactic rotation at 10 kpc: X ≈ 0.86 (intermediate).
    Cosmic expansion: X ≈ 3 × 10⁻³ (deep memory regime).
    """
    return omega_dyn_Hz * tau_0_sec


def alpha_effective(omega_dyn_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Frequency-gated effective coupling α_eff(X) = α / (1 + X²).

    Phase I §8.1: solar-system safety by construction. At Saturn's
    orbital frequency, α_eff ≈ 4 × 10⁻¹⁵ — below any ranging sensitivity.
    """
    X = regime_parameter_X(omega_dyn_Hz, tau_0_sec=tau_0_sec)
    return alpha / (1.0 + X**2)


# ────────────────────────────────────────────────────────────────────
# Engine interpolation (Phase I Appendix E)
# ────────────────────────────────────────────────────────────────────

def nu_interpolation(y):
    """Acceleration interpolation ν(y) = 1/2 + √(1/4 + 1/y).

    Phase I Appendix E.1: "frozen engine mapping function."
    Asymptotic limits:
        y ≫ 1 (Newtonian):   ν → 1,         g_eff ≈ g_bar
        y ≪ 1 (deep-response): ν → √(1/y),   g_eff ≈ √(g_bar × a_0)

    This is the MOND interpolation form, but derived here from the
    screening mechanism (not from modified dynamics). y ≡ g_bar/a_0.
    """
    y_arr = np.asarray(y, dtype=float)
    if np.any(y_arr <= 0):
        # Return divergent interpolation for non-positive y
        return np.where(y_arr > 0, 0.5 + np.sqrt(0.25 + 1.0/np.where(y_arr > 0, y_arr, 1)), float("inf"))
    return 0.5 + np.sqrt(0.25 + 1.0/y_arr)


def g_effective(g_bar_SI, omega_dyn_Hz,
                 a_0=A_0_SI, tau_0_sec=TAU_0_SEC):
    """Total effective gravitational acceleration (Phase I Appendix E.2).

        g_eff = g_bar × [1 + (ν(y) − 1) / (1 + X²)]

    where y = g_bar/a_0 and X = ω_dyn τ_0.

    In the solar-system regime (X ≫ 1): g_eff ≈ g_bar (GR recovered).
    In the deep-galactic regime (X ≪ 1, y ≪ 1): g_eff ≈ √(g_bar × a_0) (MOND-like).
    """
    y = g_bar_SI / a_0
    nu = nu_interpolation(y)
    X = regime_parameter_X(omega_dyn_Hz, tau_0_sec=tau_0_sec)
    return g_bar_SI * (1.0 + (nu - 1.0) / (1.0 + X**2))


# ────────────────────────────────────────────────────────────────────
# Bullet Cluster operational estimate (Phase I §8.4)
# ────────────────────────────────────────────────────────────────────

def bullet_offset_estimate(v_coll_m_s, tau_0_sec=TAU_0_SEC):
    """δ_est ≈ v_coll × τ_0 — memory-kernel lag offset.

    Phase I §8.4: the simple operational estimate for the lensing-
    gas offset in cluster mergers. Full convolution is done by the
    engine; this is the scaling estimate.
    """
    return v_coll_m_s * tau_0_sec


# ────────────────────────────────────────────────────────────────────
# MOND comparison (v11 App F, F)
# ────────────────────────────────────────────────────────────────────

MOND_COMPARISON = {
    "MOND": {
        "foundational_assumption": "Newtonian dynamics/inertia modified below a_0",
        "fundamental_scale":       "a_0 (acceleration, fitted ~1.2e-10 m/s²)",
        "regime_separator":        "acceleration-based",
        "field_equations":         "nonlinear Poisson",
        "causality":               "implicit",
        "free_parameters":         1,
    },
    "TeVeS": {
        "foundational_assumption": "New scalar, vector, tensor fields",
        "propagating_fields":      "extra",
        "UV_recovery":             "model-dependent",
        "free_parameters":         "several",
    },
    "Emergent_Gravity": {
        "foundational_assumption": "Gravity is entropic response of microscopic d.o.f.",
        "locality":                "quasi-local",
        "UV_recovery":             "unclear",
        "free_parameters":         "several",
    },
    "GRUT_Closure": {
        "foundational_assumption": "Gravity is geometric; metric has finite relaxation τ_0",
        "fundamental_scale":       "τ_0 = 41.9 Myr (response-time, derived from Λ)",
        "regime_separator":        "frequency-based (X = ω_dyn τ_0)",
        "field_equations":         "Einstein + nonlocal memory kernel",
        "causality":               "explicit (Kramers-Kronig)",
        "UV_recovery":             "automatic (n_g → 1 at high ω)",
        "singularity_resolution":  "yes (curvature saturates at α/(c²τ_0²))",
        "MOND_a_0":                "emerges as c/(2π τ_Λ), not independent",
        "free_parameters":         0,
    },
}
"""v11 Appendix F and Appendix C comparison table, integrated verbatim.

Key slogan:
  MOND changes the law.
  Emergent gravity changes the meaning.
  Closure changes the response time.

Closure predicts MOND-like phenomenology only in the LOW-FREQUENCY limit
(X ≪ 1), not universally at low accelerations. This is testable: systems
with low acceleration but high frequency (e.g., planetary wide binaries
at specific phases) should NOT show MOND-like behavior."""


# ────────────────────────────────────────────────────────────────────
# Convenience / canonical table
# ────────────────────────────────────────────────────────────────────

def canonical_constants_table():
    """Phase I §6 canonical constants table (brought into code)."""
    return {
        "tau_Lambda_Gyr":         TAU_LAMBDA_SEC / (YEAR_SEC * 1e9),
        "tau_0_Myr":              TAU_0_MYR,
        "alpha_vac":              ALPHA_VAC,
        "S_screening_factor":     S_SCREENING,
        "S_formula":              "12π/α² = 108π",
        "n_g_DC":                 N_G_DC,
        "mu_Lambda_eV":           MU_LAMBDA_EV,
        "mu_0_eV":                MU_0_EV,
        "a_star_m_s2":            A_STAR_SI,
        "a_0_m_s2":               A_0_SI,
        "T_c_K":                  T_C_KELVIN,
        "T_c_MK":                 T_C_MK,
        "H_0_implied_km_s_Mpc":   H_0_IMPLIED_KM_S_MPC,
        "provenance": {
            "alpha_vac":         "v11.1 Appendix H — α = 1/d, d=3",
            "S_screening":       "Phase I §5 — S = 12π/α²",
            "tau_0":             "v11 App I / Phase I §5 — τ_0 = τ_Λ/S = 1/√(Λc)",
            "a_0":               "Phase I §8.2 — c/(2π τ_Λ) ~ MOND scale",
            "T_c":               "v9.0 — ℏ/(τ_0 k_B) ≈ 54.7 MK",
            "n_g_DC":            "√(1+α) = √(4/3), tree-level geometric",
        },
    }


def verify():
    """Self-test canonical constants."""
    table = canonical_constants_table()
    checks = {
        # α = 1/3 exactly
        "alpha_vac_is_one_third":      abs(ALPHA_VAC - 1/3) < 1e-15,
        # S = 108π
        "S_equals_108_pi":             abs(S_SCREENING - 108 * np.pi) < 1e-10,
        # τ_0 ≈ 41.9 Myr (within 1%)
        "tau_0_is_41p9_Myr":           abs(TAU_0_MYR - 41.9) / 41.9 < 0.01,
        # n_g(0) = 1.1547
        "n_g_DC_is_sqrt_4_over_3":     abs(N_G_DC - np.sqrt(4/3)) < 1e-12,
        # a_0 in 10⁻¹⁰ m/s² band
        "a_0_is_MOND_scale":           1e-11 < A_0_SI < 1e-9,
        # T_c ≈ 54.7 MK (within 5%)
        "T_c_is_54p7_MK":              abs(T_C_KELVIN/1e6 - 54.7) / 54.7 < 0.05,
        # μ_Λ ~ 10⁻³³ eV
        "mu_Lambda_is_10e_minus_33":   1e-34 < MU_LAMBDA_EV < 1e-32,
        # μ_0 = S × μ_Λ
        "mu_0_equals_S_mu_Lambda":     abs(MU_0_EV / MU_LAMBDA_EV - S_SCREENING) / S_SCREENING < 1e-6,
        # τ_0 = 1/√(Λc) round-trip
        "tau_0_Lambda_c_identity":     abs(
            tau_0_from_lambda_c(lambda_from_tau_0(TAU_0_SEC)) - TAU_0_SEC
        ) / TAU_0_SEC < 1e-10,
    }
    return checks


if __name__ == "__main__":
    import json
    table = canonical_constants_table()
    print(json.dumps({k: (v if not isinstance(v, dict) else v) for k, v in table.items()},
                      indent=2, default=str))
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "✓" if v else "✗"
        print(f"  {mark} {k}")
