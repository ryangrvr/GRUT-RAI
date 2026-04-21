"""
Track VII — Bandwidth Integral for Dielectric Dark Matter (brother's protocol).

Six-step protocol for the P(k)-weighted integral of the refractive
enhancement over the observable matter power spectrum:

    Step 1: Load/build P(k) — here we use BBKS (Bardeen-Bond-Kaiser-Szalay
            1986) analytical transfer function with standard cosmological
            parameters. NIS-certifiable; no external dependency on CAMB/CLASS
            for first-cut. Swap in CAMB/CLASS later if desired.

    Step 2: ω(k) = k × σ_v(k). First pass: ω(k) = k × c_s with c_s = 200 km/s
            (approximate linear velocity dispersion). Sensitivity sweep
            documented.

    Step 3: Lorentzian enhancement E(k) = α / (1 + (ω(k) τ_0)²).
            α = 1/3 (Phase I canonical), τ_0 = 41.9 Myr.

    Step 4: Dimensionless power spectrum Δ²(k) = k³ P(k) / (2π²).
            Weighted average Ω_dm,eff = ∫ E(k) Δ²(k) dk / ∫ Δ²(k) dk.

    Step 5: Compare to Ω_dm,observed = 0.263.

    Step 6: Sensitivity analysis:
            - c_s ∈ [50, 500] km/s
            - τ_0 ± 10%
            - α ± 5%

Expected result (brother's prediction):
    At the P(k) peak (k ≈ 0.02 h/Mpc), ωτ_0 ≈ 10⁻⁴ with c_s = 200 km/s.
    Full enhancement E ≈ α = 0.333 across most of the P(k) support.
    Integral should give ≈ 0.333, about 27% above observed Ω_dm = 0.263.

    If the integral gives ≈ 0.333 rather than 0.263, that is still a
    result: GRUT predicts slightly MORE effective dark matter than
    ΛCDM analyses infer. This could mean ΛCDM underestimates Ω_dm
    because it assumes the wrong expansion history, or it could mean
    the pure dielectric interpretation overshoots and needs a
    subtractive correction (e.g. from soliton annihilation or higher-
    order corrections to n_g²).
"""

import numpy as np

from grut.foundation.closure_protocol import ALPHA_VAC, TAU_0_SEC


# Cosmological parameters (Planck 2018 fiducial)
H_0_KM_S_MPC = 70.0
H_LITTLE = 0.70                    # h = H_0/100
OMEGA_M = 0.311                    # matter density
OMEGA_B = 0.0486                   # baryon density
OMEGA_DM_OBS = 0.263               # observed dark-matter density
N_S_PRIMORDIAL = 0.965             # scalar spectral index (Planck)

# Unit conversions
MPC_IN_M = 3.0857e22
KM = 1000.0


# ────────────────────────────────────────────────────────────────────
# Step 1: The matter power spectrum (BBKS analytical)
# ────────────────────────────────────────────────────────────────────

def bbks_transfer_function(k_h_per_Mpc, Omega_m=OMEGA_M, Omega_b=OMEGA_B,
                            h=H_LITTLE):
    """BBKS (1986) transfer function with simple Γ shape parameter.

    T(q) = [ln(1 + 2.34q) / (2.34q)] ×
           [1 + 3.89q + (16.1q)² + (5.46q)³ + (6.71q)⁴]^(−1/4)

    where q = k / Γ (in h/Mpc), and the shape parameter:

        Γ = Ω_m × h × exp(-Ω_b × (1 + √(2h)/Ω_m))

    Sugiyama (1995) correction to account for baryons.
    """
    Gamma = Omega_m * h * np.exp(-Omega_b * (1 + np.sqrt(2*h) / Omega_m))
    q = k_h_per_Mpc / Gamma
    q = np.where(q > 0, q, 1e-30)
    # Logarithm term (with small-q safety)
    log_term = np.where(q > 1e-6,
                         np.log(1 + 2.34*q) / (2.34*q),
                         1.0 - 1.17*q + 1.37*q**2)   # Taylor for small q
    # Polynomial denominator
    poly = 1.0 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4
    T = log_term * poly**(-0.25)
    return T


def matter_power_spectrum(k_h_per_Mpc, Omega_m=OMEGA_M, Omega_b=OMEGA_B,
                           h=H_LITTLE, n_s=N_S_PRIMORDIAL):
    """P(k) = A × k^n_s × T²(k), BBKS shape.

    Normalization A is arbitrary because it cancels in
    the ratio Ω_dm,eff = ∫ E P̂ dk / ∫ P̂ dk. Units: Mpc³/h³ up
    to the normalization constant.
    """
    T = bbks_transfer_function(k_h_per_Mpc, Omega_m, Omega_b, h)
    return k_h_per_Mpc ** n_s * T**2


def dimensionless_power_spectrum(k_h_per_Mpc, **kwargs):
    """Δ²(k) = k³ P(k) / (2π²) — variance per log k interval.

    Up to the same arbitrary normalization as P(k). Peaks near
    k ≈ 0.02 h/Mpc for BBKS with Planck cosmology.
    """
    P = matter_power_spectrum(k_h_per_Mpc, **kwargs)
    return k_h_per_Mpc**3 * P / (2 * np.pi**2)


# ────────────────────────────────────────────────────────────────────
# Step 2: Dynamical frequency ω(k)
# ────────────────────────────────────────────────────────────────────

def omega_of_k(k_h_per_Mpc, c_s_m_per_s=200e3, h=H_LITTLE):
    """ω(k) = k × c_s.

    Converts k (in h/Mpc) to physical wavenumber (1/m) and multiplies
    by c_s. Returns ω in Hz.

    First-cut choice: c_s = 200 km/s as a linear-theory velocity-
    dispersion scale. The linear σ_v(k) from the growth rate is a
    better estimate; this approximation is validated by the sensitivity
    sweep over c_s.
    """
    # k (h/Mpc) → 1/m: divide by (Mpc/h) in meters
    k_per_m = k_h_per_Mpc * h / MPC_IN_M
    return k_per_m * c_s_m_per_s


# ────────────────────────────────────────────────────────────────────
# Step 3: The Lorentzian enhancement
# ────────────────────────────────────────────────────────────────────

def enhancement_E(k_h_per_Mpc, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC,
                   c_s_m_per_s=200e3, h=H_LITTLE):
    """Lorentzian enhancement per mode:

        E(k) = α / (1 + (ω(k) τ_0)²)

    Limits:
        k → 0  (DC):   E → α
        k → ∞  (UV):   E → α / (k × c_s × τ_0)² → 0
    """
    omega = omega_of_k(k_h_per_Mpc, c_s_m_per_s=c_s_m_per_s, h=h)
    x = omega * tau_0_sec
    return alpha / (1.0 + x**2)


# ────────────────────────────────────────────────────────────────────
# Step 4: The integrated Ω_dm,eff
# ────────────────────────────────────────────────────────────────────

def omega_dm_bandwidth_integral(
    alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC, c_s_m_per_s=200e3,
    Omega_m=OMEGA_M, Omega_b=OMEGA_B, h=H_LITTLE, n_s=N_S_PRIMORDIAL,
    k_min=1e-4, k_max=0.3, n_k=4096,
):
    """Compute Ω_dm,eff = ∫ E(k) Δ²(k) dk / ∫ Δ²(k) dk.

    Per brother's Step 4. Integration in log-k for numerical stability.
    Uses dimensionless power spectrum Δ²(k) as the weight.

    Default range: k ∈ [1e-4, 0.3] h/Mpc — the LINEAR regime relevant
    for CMB and large-scale-structure cosmological inference. Above
    k ≈ 0.3 h/Mpc linear theory breaks down (nonlinear evolution, which
    is beyond the scope of Ω_dm parameter extraction from cosmic
    observations). BBKS linear P(k) artificially keeps growing at
    small scales — not physical.

    Returns dict with the result, diagnostic scales, and integrand sample.
    """
    k = np.logspace(np.log10(k_min), np.log10(k_max), n_k)   # h/Mpc

    Delta2 = dimensionless_power_spectrum(
        k, Omega_m=Omega_m, Omega_b=Omega_b, h=h, n_s=n_s,
    )
    E = enhancement_E(
        k, alpha=alpha, tau_0_sec=tau_0_sec,
        c_s_m_per_s=c_s_m_per_s, h=h,
    )

    # Weighted average of E over P(k). Use dk (as written by brother) or
    # dln k (more standard for Δ² weighting). Both computed below;
    # primary result reported with dln k measure since Δ² is naturally
    # "variance per log k."
    omega_eff_dk = np.trapezoid(E * Delta2, k) / np.trapezoid(Delta2, k)
    omega_eff_dlnk = np.trapezoid(E * Delta2, np.log(k)) / np.trapezoid(Delta2, np.log(k))

    # Peak of Δ² for diagnostic
    peak_idx = int(np.argmax(Delta2))
    k_peak = float(k[peak_idx])
    omega_peak = float(omega_of_k(k_peak, c_s_m_per_s=c_s_m_per_s, h=h))
    x_peak = float(omega_peak * tau_0_sec)

    # Scale where ωτ_0 = 1
    k_per_m_transition = 1.0 / (c_s_m_per_s * tau_0_sec)
    k_h_per_Mpc_transition = k_per_m_transition * MPC_IN_M / h

    return {
        "alpha":                    alpha,
        "tau_0_sec":                tau_0_sec,
        "c_s_m_per_s":              c_s_m_per_s,
        "Omega_dm_eff_dk":          omega_eff_dk,
        "Omega_dm_eff_dlnk":        omega_eff_dlnk,
        "Omega_dm_observed":        OMEGA_DM_OBS,
        "dk_over_observed":         omega_eff_dk / OMEGA_DM_OBS,
        "dlnk_over_observed":       omega_eff_dlnk / OMEGA_DM_OBS,
        "k_peak_h_per_Mpc":         k_peak,
        "omega_peak_Hz":            omega_peak,
        "omega_tau_at_peak":        x_peak,
        "k_transition_h_per_Mpc":   k_h_per_Mpc_transition,
        "interpretation": _interpretation(omega_eff_dk, alpha, k_h_per_Mpc_transition),
    }


def _interpretation(omega_eff, alpha, k_trans):
    """Short human-readable summary of the integral result."""
    diff = (omega_eff - OMEGA_DM_OBS) / OMEGA_DM_OBS
    if abs(diff) < 0.05:
        return (f"Ω_dm,eff = {omega_eff:.4f} within 5% of observed {OMEGA_DM_OBS:.4f} — "
                "dielectric interpretation closes at first cut.")
    if diff > 0:
        return (
            f"Ω_dm,eff = {omega_eff:.4f} OVERSHOOTS observed {OMEGA_DM_OBS:.4f} by "
            f"{100*diff:+.1f}%. Dielectric interpretation gives MORE effective DM than "
            "inferred by ΛCDM. Either ΛCDM's analysis underestimates Ω_dm (by assuming "
            "a wrong expansion history) or a subtractive correction to the pure Lorentzian "
            "is needed. At c_s = 200 km/s the transition k ≈ {:.1f} h/Mpc is far above the "
            "P(k) support, so enhancement saturates at α = {:.3f} for all dominant modes."
            .format(k_trans, alpha)
        )
    return (
        f"Ω_dm,eff = {omega_eff:.4f} UNDERSHOOTS observed {OMEGA_DM_OBS:.4f} by "
        f"{100*diff:+.1f}%. Dielectric interpretation alone does not account for the "
        "full observed dark matter abundance."
    )


# ────────────────────────────────────────────────────────────────────
# Step 6: Sensitivity analysis
# ────────────────────────────────────────────────────────────────────

def sensitivity_c_s(c_s_range_km_s=(50, 500), n=10, **kwargs):
    """Sweep sound-speed c_s ∈ [50, 500] km/s (brother's Step 6)."""
    c_s_values = np.linspace(c_s_range_km_s[0], c_s_range_km_s[1], n)
    out = []
    for c_s in c_s_values:
        r = omega_dm_bandwidth_integral(c_s_m_per_s=c_s * KM, **kwargs)
        out.append({
            "c_s_km_s":      float(c_s),
            "Omega_dm_eff":  r["Omega_dm_eff_dk"],
            "k_transition":  r["k_transition_h_per_Mpc"],
        })
    return out


def sensitivity_tau_0(tau_0_range_factor=(0.9, 1.1), n=5, **kwargs):
    """Sweep τ_0 ± 10%."""
    base = TAU_0_SEC
    factors = np.linspace(tau_0_range_factor[0], tau_0_range_factor[1], n)
    return [{
        "tau_0_Myr":     float(base * f / (3.156e7 * 1e6)),
        "factor":        float(f),
        "Omega_dm_eff":  omega_dm_bandwidth_integral(tau_0_sec=base * f, **kwargs)["Omega_dm_eff_dk"],
    } for f in factors]


def sensitivity_alpha(alpha_range_factor=(0.95, 1.05), n=5, **kwargs):
    """Sweep α ± 5%."""
    base = ALPHA_VAC
    factors = np.linspace(alpha_range_factor[0], alpha_range_factor[1], n)
    return [{
        "alpha":         float(base * f),
        "factor":        float(f),
        "Omega_dm_eff":  omega_dm_bandwidth_integral(alpha=base * f, **kwargs)["Omega_dm_eff_dk"],
    } for f in factors]


def sensitivity_viable_region(tolerance=(0.24, 0.28), n=5):
    """Find (c_s, τ_0, α) triples that land Ω_dm,eff ∈ [0.24, 0.28]."""
    hits = []
    c_s_values = np.linspace(50e3, 500e3, n)
    tau_0_factors = np.linspace(0.9, 1.1, n)
    alpha_factors = np.linspace(0.95, 1.05, n)
    for c_s in c_s_values:
        for t_f in tau_0_factors:
            for a_f in alpha_factors:
                r = omega_dm_bandwidth_integral(
                    alpha=ALPHA_VAC * a_f,
                    tau_0_sec=TAU_0_SEC * t_f,
                    c_s_m_per_s=c_s,
                )
                omega_eff = r["Omega_dm_eff_dk"]
                if tolerance[0] <= omega_eff <= tolerance[1]:
                    hits.append({
                        "c_s_km_s":       c_s / KM,
                        "tau_0_factor":   t_f,
                        "alpha_factor":   a_f,
                        "Omega_dm_eff":   omega_eff,
                    })
    return hits


# ────────────────────────────────────────────────────────────────────
# Summary
# ────────────────────────────────────────────────────────────────────

def track_vii_bandwidth_summary():
    """Complete protocol result — brother's 6 steps integrated."""
    # Step 1-5: the main integral
    main = omega_dm_bandwidth_integral()
    # Step 6: sensitivity
    c_s_scan = sensitivity_c_s()
    tau_0_scan = sensitivity_tau_0()
    alpha_scan = sensitivity_alpha()
    viable = sensitivity_viable_region()
    return {
        "protocol":          "Brother's Track VII bandwidth integral, 6 steps",
        "fixed_inputs": {
            "alpha":          ALPHA_VAC,
            "tau_0_Myr":      TAU_0_SEC / (3.156e7 * 1e6),
            "c_s_km_s":       200.0,
            "cosmology":      "Planck 2018 (Omega_m=0.311, Omega_b=0.0486, h=0.7)",
            "power_spectrum": "BBKS transfer function (analytical)",
        },
        "main_result":        main,
        "sensitivity_c_s":    c_s_scan,
        "sensitivity_tau_0":  tau_0_scan,
        "sensitivity_alpha":  alpha_scan,
        "viable_region":      viable,
        "verdict": (
            f"Integrated Ω_dm,eff = {main['Omega_dm_eff_dk']:.4f}. "
            f"Observed Ω_dm = {OMEGA_DM_OBS:.4f}. "
            f"Ratio = {main['Omega_dm_eff_dk']/OMEGA_DM_OBS:.3f}. "
            + main["interpretation"]
        ),
    }


if __name__ == "__main__":
    import json
    def clean(obj):
        if isinstance(obj, dict):
            return {k: clean(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [clean(x) for x in obj]
        elif isinstance(obj, (np.floating, np.integer)):
            return float(obj)
        return obj
    r = track_vii_bandwidth_summary()
    print(json.dumps(clean(r), indent=2, default=str))
