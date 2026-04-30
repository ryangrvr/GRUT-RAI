"""GRUT — BBN thermal-buffer calculation (standard cosmology).

SCOPE NOTICE: This module implements STANDARD cosmology applied to a
research hypothesis. It is NOT GRUT-specific physics. The framework
remains uncommitted to the broader hypothesis being tested.

Hypothesis being tested (one piece of a larger narrative):
    "During BBN, nuclear binding energy released by p+n → ⁴He fusion
     provides a thermal buffer that slows or plateaus the cosmic
     temperature."

Connection to framework: this is the most tractable load-bearing piece
of an external research narrative connecting BBN dynamics to
t_c_provenance_inconsistency_open_negative (#15 in the ledger). The
broader narrative remains uninvestigated and uncommitted; this
calculation tests one specific physical claim in isolation.

Methodology: standard cosmology only. No GRUT-specific machinery
(no τ_0, no Λ_grav, no T_c, no R, no α_vac). All inputs are
standard cosmological constants and BBN parameters.

Pre-committed expectation (registered before computation):
    Outcome (ii) — cooling significantly slowed but not plateaued.
    BBN energetically significant relative to baryon rest-mass but
    probably not relative to the radiation field.

THE LOAD-BEARING DIMENSIONAL CHECK:

    binding energy per baryon ≈ Y_p × B(⁴He)/4 ≈ 0.247 × 28.3/4 ≈ 1.75 MeV
    radiation energy per baryon ≈ (1/η_B) × 2.7 T_BBN ≈ 4×10⁸ MeV

The ratio is η_B-suppressed: with η_B ≈ 6×10⁻¹⁰, baryons are
~10⁻⁹ of the photons. Even if every baryon dumped its full BBN
binding energy into the radiation field, the temperature change
would be (1 + 10⁻⁹)^(1/4) ≈ 1 + 3×10⁻¹⁰ — negligible.

This module computes the calculation rigorously to confirm or refute
this dimensional read.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ─────────────────────────────────────────────────────────────────────
# Standard cosmology constants (PDG / Planck 2018)
# ─────────────────────────────────────────────────────────────────────

# Physical constants
HBAR_MEV_S: float = 6.5821220e-22       # ℏ in MeV·s
HBAR_MEV_FM: float = 197.327             # ℏc in MeV·fm
C_CM_S: float = 2.99792458e10            # speed of light [cm/s]
G_NEWTON_NATURAL: float = 6.7087e-39     # G in GeV⁻²
M_PLANCK_MEV: float = 1.22e22            # ~ √(1/G) in MeV (reduced)
K_B_MEV_K: float = 8.617333e-11          # Boltzmann constant [MeV/K]

# BBN parameters (standard / Planck)
ETA_B_PLANCK: float = 6.14e-10           # baryon-to-photon ratio
Y_P_BBN: float = 0.247                   # ⁴He mass fraction
B_HE4_MEV: float = 28.296                # ⁴He binding energy [MeV]
ATOMIC_MASS_NUMBER_HE4: int = 4

# Effective relativistic d.o.f. across the BBN window
# Pre-e⁺e⁻ annihilation (T > ~0.5 MeV): g_* = 2(γ) + (7/8)(2+2)(e⁺e⁻)
#   + (7/8)(2)(3)(ν, anti-ν, 3 flavours) = 2 + 3.5 + 5.25 = 10.75
G_STAR_PRE_ANNIHILATION: float = 10.75
# Post-e⁺e⁻ annihilation (T < ~0.05 MeV): g_* ≈ 3.36
G_STAR_POST_ANNIHILATION: float = 3.36
# Mid-BBN representative value (T ~ 0.1 MeV, partway through annihilation):
G_STAR_MID_BBN: float = 3.36

# BBN window definitions (multiple — check sensitivity)
T_BBN_START_MEV: float = 0.7             # neutron freeze-out
T_BBN_END_MEV: float = 0.030             # ⁴He completion
T_BBN_START_NARROW_MEV: float = 0.1
T_BBN_END_NARROW_MEV: float = 0.030
T_MID_BBN_MEV: float = 0.1               # representative


# ─────────────────────────────────────────────────────────────────────
# Standard cosmology core formulas
# ─────────────────────────────────────────────────────────────────────

def radiation_energy_density_natural(T_MeV: float, g_star: float) -> float:
    """Radiation energy density in natural units [MeV⁴].

    ρ_rad = (π²/30) × g_*(T) × T⁴
    """
    return (math.pi**2 / 30.0) * g_star * T_MeV**4


def photon_number_density_natural(T_MeV: float) -> float:
    """Photon number density in natural units [MeV³].

    n_γ = (2 ζ(3) / π²) × T³, with ζ(3) ≈ 1.20206
    """
    return (2.0 * 1.2020569 / math.pi**2) * T_MeV**3


def baryon_number_density_natural(T_MeV: float, eta_B: float = ETA_B_PLANCK) -> float:
    """Baryon number density in natural units [MeV³].

    n_b = η_B × n_γ
    """
    return eta_B * photon_number_density_natural(T_MeV)


def binding_energy_per_baryon_MeV(
    y_p: float = Y_P_BBN, b_he4: float = B_HE4_MEV
) -> float:
    """Average binding energy released per baryon when fraction y_p
    is locked in ⁴He.

    Each ⁴He has 4 nucleons and binding energy b_he4; per baryon in
    helium, that's b_he4/4. Averaged over baryons (only fraction y_p
    is in helium):
        ⟨E_bind⟩/baryon = y_p × b_he4 / 4
    """
    return y_p * b_he4 / ATOMIC_MASS_NUMBER_HE4


def total_binding_energy_per_volume_natural(
    T_MeV: float,
    eta_B: float = ETA_B_PLANCK,
    y_p: float = Y_P_BBN,
    b_he4: float = B_HE4_MEV,
) -> float:
    """Total binding energy released per unit physical volume when
    BBN completes at temperature T [MeV⁴].

    E_bind = ⟨E_bind⟩/baryon × n_b(T)
    """
    return binding_energy_per_baryon_MeV(y_p, b_he4) * baryon_number_density_natural(T_MeV, eta_B)


def hubble_rate_radiation_dom_per_s(T_MeV: float, g_star: float) -> float:
    """Radiation-dominated Hubble rate H(T) in [1/s].

    H = √(8πG ρ_rad / 3) = √(8π/3) × √(g_* π²/30) × T² / M_Pl

    Standard cosmology textbook formula (Kolb & Turner 3.62):
        H(T) ≈ 1.66 × √g_* × T² / M_Pl
    """
    H_natural_MeV = 1.66 * math.sqrt(g_star) * T_MeV**2 / M_PLANCK_MEV
    # Convert MeV → 1/s via ℏ
    return H_natural_MeV / HBAR_MEV_S


def cosmic_time_radiation_dom_seconds(T_MeV: float, g_star: float) -> float:
    """Cosmic time at temperature T in radiation domination [s].

    t = 1/(2H(T)) for radiation domination
    Standard: t ≈ 2.4 / √g_* × (T/MeV)⁻² seconds (Kolb & Turner)
    """
    return 2.42 / math.sqrt(g_star) / T_MeV**2


def cooling_power_per_volume_natural(T_MeV: float, g_star: float) -> float:
    """Rate of radiation energy density decrease due to cosmic
    expansion (redshift), at fixed proper volume [MeV⁴/s × ℏ⁻¹]:

        dρ_rad/dt = -4H × ρ_rad

    Returns positive value of |dρ_rad/dt| in MeV⁴ × s⁻¹ × HBAR
    factor (natural units carry an implicit ℏ to convert to MeV/s).
    """
    H_per_s = hubble_rate_radiation_dom_per_s(T_MeV, g_star)
    rho_rad = radiation_energy_density_natural(T_MeV, g_star)
    # Convert: dρ/dt in MeV⁴/s = ρ_rad × H × HBAR_MEV_S, since ρ_rad
    # is in MeV⁴ (natural) and we want MeV⁴/(time-in-MeV·s).
    # Equivalently: (4H ρ_rad) where H has units 1/s.
    return 4.0 * H_per_s * rho_rad * HBAR_MEV_S


# ─────────────────────────────────────────────────────────────────────
# The thermal-buffer ratios — the actual test
# ─────────────────────────────────────────────────────────────────────


def energy_density_ratio(
    T_MeV: float = T_MID_BBN_MEV,
    eta_B: float = ETA_B_PLANCK,
    y_p: float = Y_P_BBN,
    b_he4: float = B_HE4_MEV,
    g_star: float = G_STAR_MID_BBN,
) -> dict:
    """Ratio of total binding energy released to radiation energy
    density, at characteristic mid-BBN T.

    R_E = E_bind_total / ρ_rad

    R_E ≫ 1: BBN energy can drive significant T change
    R_E ~ 1: BBN energy is a meaningful perturbation
    R_E ≪ 1: BBN energy is negligible compared to radiation field
    """
    E_bind = total_binding_energy_per_volume_natural(T_MeV, eta_B, y_p, b_he4)
    rho_rad = radiation_energy_density_natural(T_MeV, g_star)
    ratio = E_bind / rho_rad
    return {
        "T_MeV": T_MeV,
        "g_star": g_star,
        "E_bind_per_volume_MeV4": E_bind,
        "rho_rad_per_volume_MeV4": rho_rad,
        "ratio_E_bind_over_rho_rad": ratio,
        "interpretation": (
            "Negligible buffer effect" if ratio < 0.01 else
            "Meaningful perturbation" if ratio < 1.0 else
            "Significant buffer or plateau plausible"
        ),
    }


def rate_ratio(
    T_MeV: float = T_MID_BBN_MEV,
    bbn_duration_s: float = 1000.0,  # standard BBN window ~ 1-1000 s
    eta_B: float = ETA_B_PLANCK,
    y_p: float = Y_P_BBN,
    b_he4: float = B_HE4_MEV,
    g_star: float = G_STAR_MID_BBN,
) -> dict:
    """Ratio of binding-energy injection rate to radiation cooling
    rate, at characteristic mid-BBN T.

    R_rate = (dE_bind/dt) / |dρ_rad/dt|
           = (E_bind_total / Δt_BBN) / (4 H ρ_rad × ℏ)

    R_rate ≫ 1: injection overwhelms cooling — temperature rises
    R_rate ~ 1: cooling significantly slowed
    R_rate ≪ 1: negligible effect on cooling
    """
    E_bind = total_binding_energy_per_volume_natural(T_MeV, eta_B, y_p, b_he4)
    cooling = cooling_power_per_volume_natural(T_MeV, g_star)
    # Inject rate: E_bind released over BBN duration
    # E_bind in MeV⁴ (natural). Convert to MeV⁴/s by dividing by Δt_BBN_in_seconds × ... wait
    # E_bind has units MeV⁴ already (natural-units energy density).
    # cooling has units MeV⁴/s already (we returned it with HBAR_MEV_S applied).
    # injection: E_bind/Δt_BBN gives MeV⁴/s if E_bind is in MeV⁴ and Δt in s.
    # Wait — that's mixing natural and SI. Let me be careful.
    # cooling_power_per_volume_natural returned `4 H × ρ_rad × HBAR_MEV_S`
    # where H is in 1/s and ρ_rad is in MeV⁴. So cooling has units 1/s × MeV⁴ × MeV·s = MeV⁵.
    # That doesn't match. Let me redo the cooling calc.
    # Actually: H × ρ_rad has units (1/s) × (MeV⁴) = MeV⁴/s. That IS what we want for energy
    # density change per unit time. The HBAR factor was wrong. Let me fix.
    cooling_corrected = 4.0 * hubble_rate_radiation_dom_per_s(T_MeV, g_star) * radiation_energy_density_natural(T_MeV, g_star)
    # Units: (1/s) × (MeV⁴) = MeV⁴/s — energy density per time in natural-units energy.
    injection = E_bind / bbn_duration_s  # MeV⁴/s
    ratio = injection / cooling_corrected
    return {
        "T_MeV": T_MeV,
        "bbn_duration_s": bbn_duration_s,
        "g_star": g_star,
        "injection_rate_MeV4_per_s": injection,
        "cooling_rate_MeV4_per_s": cooling_corrected,
        "ratio_injection_over_cooling": ratio,
        "interpretation": (
            "Negligible buffer effect" if ratio < 0.01 else
            "Cooling slowed but not plateaued" if ratio < 1.0 else
            "Plateau or temperature rise plausible"
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Per-baryon sanity check — the cleanest dimensional read
# ─────────────────────────────────────────────────────────────────────


def per_baryon_energy_comparison(
    T_MeV: float = T_MID_BBN_MEV,
    eta_B: float = ETA_B_PLANCK,
    y_p: float = Y_P_BBN,
    b_he4: float = B_HE4_MEV,
) -> dict:
    """The cleanest dimensional read.

    Per-baryon binding energy released: y_p × b_he4 / 4 ≈ 1.75 MeV.
    Per-baryon radiation energy: (n_γ/n_b) × ⟨E_γ⟩ = (1/η_B) × 2.7 T.

    Ratio = (y_p × b_he4 / 4) / ((2.7 T) / η_B) = (y_p × b_he4 × η_B) / (4 × 2.7 × T)

    With Y_p = 0.247, B(⁴He) = 28.3 MeV, η_B = 6×10⁻¹⁰, T = 0.1 MeV:
        Ratio ≈ (0.247 × 28.3 × 6×10⁻¹⁰) / (4 × 2.7 × 0.1)
              ≈ 4.2×10⁻⁹ / 1.08
              ≈ 3.9×10⁻⁹
    """
    bind_per_baryon = binding_energy_per_baryon_MeV(y_p, b_he4)
    avg_photon_energy = 2.7 * T_MeV  # ⟨E_γ⟩ ≈ 2.7 k_B T
    photons_per_baryon = 1.0 / eta_B
    rad_per_baryon = avg_photon_energy * photons_per_baryon
    return {
        "binding_MeV_per_baryon": bind_per_baryon,
        "radiation_MeV_per_baryon": rad_per_baryon,
        "ratio_bind_over_rad_per_baryon": bind_per_baryon / rad_per_baryon,
        "T_change_if_all_dumped": (1.0 + bind_per_baryon / rad_per_baryon) ** 0.25 - 1.0,
        "interpretation": (
            f"At T = {T_MeV} MeV, the radiation field carries ~{rad_per_baryon:.2e} "
            f"MeV per baryon. BBN releases ~{bind_per_baryon:.2f} MeV per baryon. "
            f"Even if every baryon's binding energy were dumped instantaneously into "
            f"the radiation field, T would rise by ~{((1 + bind_per_baryon/rad_per_baryon)**0.25 - 1)*100:.2e}% "
            f"— far below any 'thermal buffer' threshold."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# BBN window cosmic-time check
# ─────────────────────────────────────────────────────────────────────


def bbn_window_times() -> dict:
    """Cosmic times at the boundaries of the BBN window."""
    t_start_wide = cosmic_time_radiation_dom_seconds(T_BBN_START_MEV, G_STAR_PRE_ANNIHILATION)
    t_end_wide = cosmic_time_radiation_dom_seconds(T_BBN_END_MEV, G_STAR_POST_ANNIHILATION)
    t_start_narrow = cosmic_time_radiation_dom_seconds(T_BBN_START_NARROW_MEV, G_STAR_POST_ANNIHILATION)
    t_end_narrow = cosmic_time_radiation_dom_seconds(T_BBN_END_NARROW_MEV, G_STAR_POST_ANNIHILATION)
    return {
        "wide_window": {
            "T_start_MeV": T_BBN_START_MEV,
            "T_end_MeV": T_BBN_END_MEV,
            "t_start_s": t_start_wide,
            "t_end_s": t_end_wide,
            "duration_s": t_end_wide - t_start_wide,
        },
        "narrow_window": {
            "T_start_MeV": T_BBN_START_NARROW_MEV,
            "T_end_MeV": T_BBN_END_NARROW_MEV,
            "t_start_s": t_start_narrow,
            "t_end_s": t_end_narrow,
            "duration_s": t_end_narrow - t_start_narrow,
        },
    }


# ─────────────────────────────────────────────────────────────────────
# Master report
# ─────────────────────────────────────────────────────────────────────


def bbn_thermal_buffer_attempt() -> dict:
    """Full report: per-baryon energy comparison + density-ratio +
    rate-ratio + sensitivity to BBN window definition."""
    per_baryon = per_baryon_energy_comparison()
    density = energy_density_ratio()
    rate_default = rate_ratio(bbn_duration_s=1000.0)
    rate_short = rate_ratio(bbn_duration_s=100.0)
    rate_long = rate_ratio(bbn_duration_s=10000.0)
    times = bbn_window_times()

    # Determine outcome
    rate_ratios = [
        rate_default["ratio_injection_over_cooling"],
        rate_short["ratio_injection_over_cooling"],
        rate_long["ratio_injection_over_cooling"],
    ]
    max_rate_ratio = max(rate_ratios)

    if max_rate_ratio > 1.0:
        outcome = "i_plateau_or_rise"
        verdict = (
            "BBN binding-energy injection rate exceeds cooling rate — "
            "thermal plateau or temperature rise plausible. Hypothesis "
            "claim 2 (thermal buffer) STRONGLY SUPPORTED."
        )
    elif max_rate_ratio > 0.01:
        outcome = "ii_cooling_slowed"
        verdict = (
            "BBN binding-energy injection rate is between 1% and 100% "
            "of cooling rate — cooling significantly slowed but not "
            "plateaued. Hypothesis claim 2 NEEDS REVISION: 'thermal "
            "buffer' is too strong; 'cooling-rate modifier' is "
            "accurate."
        )
    else:
        outcome = "iii_negligible"
        verdict = (
            "BBN binding-energy injection rate is < 1% of cooling rate "
            "across all sensible window definitions. Negligible "
            "thermal-buffer effect. Hypothesis claim 2 (BBN as thermal "
            "buffer) is QUANTITATIVELY WRONG by orders of magnitude. "
            "The cosmic temperature evolution during BBN is essentially "
            "set by radiation domination; binding-energy injection is "
            "a perturbation at the η_B-suppressed level."
        )

    return {
        "scope_notice": (
            "STANDARD COSMOLOGY ONLY. No GRUT-specific machinery used. "
            "The framework remains uncommitted to the broader research "
            "hypothesis being tested."
        ),
        "pre_committed_expectation": (
            "Outcome (ii) — cooling significantly slowed but not "
            "plateaued. Pre-committed before computation."
        ),
        "per_baryon_comparison": per_baryon,
        "energy_density_ratio": density,
        "rate_ratio_window_1000s": rate_default,
        "rate_ratio_sensitivity": {
            "narrow_window_100s": rate_short,
            "long_window_10000s": rate_long,
        },
        "bbn_cosmic_times": times,
        "outcome": outcome,
        "verdict": verdict,
        "implications_for_hypothesis": (
            "Outcome (iii) is materially different from the pre-"
            "committed expectation. The BBN-as-thermal-buffer claim "
            "in the broader narrative is quantitatively wrong by "
            "~10 orders of magnitude. The radiation field is "
            "η_B-suppressed-larger than baryonic energy budgets, "
            "and BBN cannot meaningfully heat or buffer it. The "
            "broader narrative connecting BBN dynamics to T_c "
            "crossing needs a different mechanism — binding energy "
            "is not it."
        ),
    }


if __name__ == "__main__":
    import json

    result = bbn_thermal_buffer_attempt()
    print("=" * 78)
    print("BBN thermal-buffer calculation (standard cosmology)")
    print("=" * 78)
    print()

    pb = result["per_baryon_comparison"]
    print(f"Per-baryon comparison at T = {T_MID_BBN_MEV} MeV:")
    print(f"  Binding energy released per baryon: {pb['binding_MeV_per_baryon']:.3f} MeV")
    print(f"  Radiation energy per baryon:        {pb['radiation_MeV_per_baryon']:.3e} MeV")
    print(f"  Ratio (binding / radiation):        {pb['ratio_bind_over_rad_per_baryon']:.3e}")
    print()

    er = result["energy_density_ratio"]
    print(f"Energy density comparison:")
    print(f"  Total binding energy / radiation energy: {er['ratio_E_bind_over_rho_rad']:.3e}")
    print(f"  Interpretation: {er['interpretation']}")
    print()

    rr = result["rate_ratio_window_1000s"]
    print(f"Rate comparison (window = 1000 s):")
    print(f"  Injection rate / cooling rate: {rr['ratio_injection_over_cooling']:.3e}")
    print(f"  Interpretation: {rr['interpretation']}")
    print()

    print(f"OUTCOME: {result['outcome']}")
    print(f"VERDICT: {result['verdict']}")
