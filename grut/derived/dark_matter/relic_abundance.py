"""
Track VII Prototype — Relic abundance Ω_dm from first principles.

Goal: compute Ω_dm natively from GRUT's dark sector parameters, without
using the observed matter density as input. If successful, this closes
the zero-parameter H_0 prediction (via Ω_m = Ω_b + Ω_dm and Friedmann).

Status: SCOPING + first-pass calculations.

GRUT's dark sector (V7 §28, Route 1):
    M_soliton = 2.11 × 10⁹ GeV    (DM candidate)
    m_A'      = 387 MeV            (dark photon mediator)
    m_h'      = 387 MeV            (dark Higgs)
    g_dark    = 0.917
    α_dark    = 0.067
    v_dark    = 422 MeV            (dark Higgs VEV, phase transition scale)
    σ/m       = 10⁻³ cm²/g         (self-interaction, SIDM viable)

Production mechanism (V7 claim): solitons form at the dark-sector
phase transition when T ~ v_dark ≈ 422 MeV. Not standard thermal
freeze-out (soliton mass too heavy for that).

This module provides:
    1. thermal_freezeout_relic() — textbook WIMP calculation (baseline)
    2. kibble_estimate() — Kibble-mechanism upper bound on solitons/Hubble volume
    3. required_production_fraction() — fraction of Kibble-maximum needed to hit observed Ω_dm

The honest result: with current V7 parameters, neither thermal freeze-out
nor naive Kibble gives observed Ω_dm. A specific model of the dark
phase transition (bubble nucleation rate, soliton formation probability
per bubble) is needed to close the calculation. This module scopes that gap.
"""

import numpy as np


# Physical constants
M_PL_GeV = 1.22e19            # Planck mass in GeV
T_CMB_GeV = 2.35e-13          # CMB temperature today in GeV
RHO_CRIT_GEV_PER_M3 = 5.3     # critical density today in GeV/m³ (for H_0 = 70)
OMEGA_DM_OBS = 0.263          # Planck observed Ω_dm ≈ 0.263
OMEGA_B_OBS = 0.0486
# Ω_m_obs = 0.3111 = Ω_b + Ω_dm

# GRUT dark sector (Route 1, from grut.derived.dark_matter.sector.route_1)
M_SOLITON_GEV = 2.11e9         # heavy soliton DM mass
M_DARK_PHOTON_GEV = 0.387      # mediator mass
V_DARK_GEV = 0.422             # dark Higgs VEV = phase transition scale
G_DARK = 0.917
ALPHA_DARK = G_DARK**2 / (4 * np.pi)


def thermal_freezeout_relic(M_chi_GeV=M_SOLITON_GEV, alpha=ALPHA_DARK):
    """Standard thermal WIMP freeze-out estimate.

    For χχ → A'A' annihilation via dark photons:
        ⟨σv⟩ ≈ π α² / M_chi²

    Relic abundance (WIMP miracle):
        Ω_dm h² ≈ (3 × 10⁻²⁷ cm³/s) / ⟨σv⟩

    For the V7 soliton at 2×10⁹ GeV, this grossly UNDER-produces
    (cross section too small → relic too large). Not the right mechanism.
    """
    sigma_v_natural = np.pi * alpha**2 / M_chi_GeV**2     # in GeV⁻²
    sigma_v_cm3s = sigma_v_natural * 3.89e-28             # convert to cm³/s
    # WIMP relic formula: Ω h² ≈ 3e-27 cm³/s / ⟨σv⟩
    omega_h2 = 3e-27 / sigma_v_cm3s
    # h² ≈ 0.49 for H_0 = 70 km/s/Mpc
    omega_dm = omega_h2 / 0.49

    return {
        "M_chi_GeV": M_chi_GeV,
        "alpha": alpha,
        "sigma_v_cm3_per_s": sigma_v_cm3s,
        "Omega_dm_h_squared": omega_h2,
        "Omega_dm": omega_dm,
        "Omega_dm_observed": OMEGA_DM_OBS,
        "over_under_produced": omega_dm / OMEGA_DM_OBS,
        "mechanism": "thermal freeze-out (WIMP miracle)",
        "status": (
            "NOT THE RIGHT MECHANISM for V7's heavy soliton. At M_soliton = "
            "2×10⁹ GeV, thermal freeze-out under-produces DM by many orders. "
            "V7 claims solitons form at the dark phase transition instead."
        ),
    }


def hubble_rate_radiation(T_GeV, g_star=106.75):
    """Hubble rate in a radiation-dominated universe at temperature T.

    H(T) = sqrt(π² g_* / 90) × T² / M_Pl
    """
    return np.sqrt(np.pi**2 * g_star / 90.0) * T_GeV**2 / M_PL_GeV


def kibble_upper_bound(T_PT_GeV=V_DARK_GEV, M_soliton_GeV=M_SOLITON_GEV, g_star=15):
    """Kibble baseline: 1 soliton per Hubble volume at the dark phase transition.

    NOTE on naming: at the GUT scale this formula gives a huge overabundance
    (the original "monopole problem"), but at T_PT = v_dark = 422 MeV the
    Hubble volume is ENORMOUS (~10 km size) and one soliton per Hubble
    volume UNDER-produces observed Ω_dm by ~40 orders of magnitude.

    The REAL physics: the Kibble-Zurek mechanism gives a correlation
    length ξ_KZ ≪ H⁻¹ for fast transitions, and n = 1/ξ_KZ³ ≫ H³. So the
    "1 per Hubble volume" number computed here is a LOWER bound for the
    realistic density, not an upper bound.

    n_soliton(T_PT) ~ H(T_PT)³   (1 per Hubble volume, baseline only)

    Redshift to today via entropy conservation (aT ≈ const):
        n_today = n(T_PT) × (T_today/T_PT)³

    Ω_soliton = ρ_soliton / ρ_crit = M_soliton × n_today / ρ_crit

    g_star at 400 MeV (post-QCD): ~15 for SM below QCD transition.
    """
    H_PT = hubble_rate_radiation(T_PT_GeV, g_star=g_star)  # in GeV
    # Hubble volume in natural units
    n_PT_max = H_PT**3   # GeV³, one per Hubble volume
    # Redshift factor (entropy conservation)
    # Actually: s = (2π²/45) g_*s T³, s × a³ = const
    # So n/s is conserved. n_today = n_PT × (s_today × a_today³)/(s_PT × a_PT³) × ... complicated.
    # Use simpler: a × T = const (to leading order), so a_PT/a_0 = T_0/T_PT
    a_ratio = T_CMB_GeV / T_PT_GeV  # a_PT / a_0
    n_today_max = n_PT_max * a_ratio**3  # in GeV³

    # Convert to /m³
    # 1 GeV³ = (GeV / ℏc)³ where ℏc ≈ 0.197 GeV·fm → 1 fm⁻¹
    # 1 GeV³ = (1/(0.197 fm))³ = 130 fm⁻³ = 130 × 10⁴⁵ m⁻³ = 1.30×10⁴⁷ /m³
    n_today_per_m3 = n_today_max * 1.30e47

    # Energy density
    rho_soliton = M_soliton_GeV * n_today_max  # GeV⁴ natural
    # Compare to rho_crit ≈ 5.3 GeV/m³ ≈ 5.3 × 1.60×10⁻¹⁰ J/m³ ...
    # Easier: Ω = (M × n_today_per_m3) / rho_crit_kg_per_m3 × (convert GeV to kg)
    rho_soliton_kg_per_m3 = M_soliton_GeV * 1.78e-27 * n_today_per_m3
    rho_crit_kg_per_m3 = 9.47e-27
    omega_max = rho_soliton_kg_per_m3 / rho_crit_kg_per_m3

    return {
        "T_PT_GeV": T_PT_GeV,
        "H_PT_GeV": H_PT,
        "hubble_volume_natural": 1 / H_PT**3,
        "n_PT_max_natural": n_PT_max,
        "n_today_max_per_m3": n_today_per_m3,
        "rho_soliton_kg_per_m3": rho_soliton_kg_per_m3,
        "Omega_dm_max_if_full_production": omega_max,
        "Omega_dm_observed": OMEGA_DM_OBS,
        "required_fraction_of_max": OMEGA_DM_OBS / omega_max if omega_max > 0 else float('inf'),
        "mechanism": "Kibble baseline (1 soliton per Hubble volume at phase transition)",
        "regime": (
            "UNDER-PRODUCES by ~40 orders of magnitude. At T_PT = 422 MeV the "
            "Hubble length is ~10 km, so 1 defect per Hubble volume is far too "
            "sparse. The observed Ω_dm ≈ 0.26 requires many defects per Hubble "
            "volume, i.e. a correlation length ξ_KZ ≪ H⁻¹."
        ),
        "status": (
            "Baseline estimate. Actual Ω_dm requires the Kibble-Zurek correlation "
            "length ξ_KZ from the cooling rate + critical exponents of the dark "
            "phase transition. In GRUT, ξ_KZ picks up a constitutive correction "
            "from the memory kernel at T = v_dark. NOT YET in V7 core — Track VII Step 1."
        ),
    }


def track_vii_status():
    """Status of Track VII: Dark Sector Completion.

    Reports what's computable now, what's missing, and what blocks the
    zero-parameter H_0 derivation.
    """
    thermal = thermal_freezeout_relic()
    kibble = kibble_upper_bound()

    return {
        "track": "VII — Dark Sector Completion",
        "goal": "Compute Ω_dm natively from GRUT dark sector parameters",
        "why_it_matters": (
            "If Ω_dm is COMPUTED, then Ω_m = Ω_b + Ω_dm is COMPUTED. "
            "Combined with H_inf (V7 §26.2 COMPUTED), H_0 = H_inf/√(1-Ω_m) "
            "becomes a zero-parameter prediction."
        ),
        "V7_parameters_available": {
            "M_soliton_GeV": M_SOLITON_GEV,
            "m_mediator_MeV": M_DARK_PHOTON_GEV * 1000,
            "v_dark_MeV": V_DARK_GEV * 1000,
            "g_dark": G_DARK,
            "alpha_dark": ALPHA_DARK,
            "Omega_b_from_baryogenesis": 0.053,  # from GRUT eta_B ≈ 6.57e-10
        },
        "thermal_freezeout_estimate": {
            "Omega_dm": thermal["Omega_dm"],
            "vs_observed": thermal["over_under_produced"],
            "verdict": "WRONG MECHANISM — soliton too heavy for WIMP freeze-out",
        },
        "kibble_baseline_1_per_hubble_volume": {
            "Omega_dm_baseline": kibble["Omega_dm_max_if_full_production"],
            "required_multiplier_over_baseline": kibble["required_fraction_of_max"],
            "verdict": (
                "1 per Hubble volume UNDER-produces by ~40 orders. Observed Ω_dm "
                "requires n_defect ≫ H³, i.e. correlation length ξ_KZ ≪ H⁻¹ from "
                "the Kibble-Zurek cooling-rate calculation."
            ),
        },
        "step_2_result": {
            "claim": "M_soliton = 2.11×10⁹ GeV is structurally derived",
            "formula": "M = 2⁹π√N_ERAS / (27 × C_FINAL^(3/2) × λ)",
            "status": "STANDS — mathematically correct, traces to C_FINAL and BPS λ=g²/2",
            "caveat": (
                "The PHYSICAL identification of this mass as the dark matter "
                "particle is not established. Step 3 showed that M_soliton "
                "does NOT match the Kibble-Zurek-produced vorton mass on a "
                "U(1) cosmic-string network. M_soliton's actual physical "
                "referent is an open question (V8 Track VII)."
            ),
        },
        "step_1_xy_ballpark": {
            "claim_retracted": "Ω_dm = 0.38 from XY-universality KZ",
            "reason": (
                "Step 1 used monopole scaling (n ~ 1/ξ³) with M_soliton as the "
                "defect mass. U(1)_dark has π_2 = 0 (no monopoles), so this "
                "topology is forbidden. The 'factor of 2' agreement with "
                "observed Ω_dm was two errors partially cancelling."
            ),
            "status": "RETRACTED (April 20, 2026)",
        },
        "step_3_vortex_result": {
            "topology": "cosmic strings (π_1(U(1)) = ℤ)",
            "Omega_vorton_XY": 0.008,
            "ratio_to_observed": 0.032,
            "verdict": (
                "With correct U(1)_dark topology and XY universality (the right "
                "class for U(1) breaking), Kibble-Zurek vortons from ξ_KZ-size "
                "loops give Ω_dm = 0.008 — factor 33 LOW of observed 0.263. "
                "The dark sector as currently specified in V7 does NOT produce "
                "the observed dark matter abundance via Kibble-Zurek. See "
                "vortex_strings.py for the full calculation."
            ),
        },
        "overall_verdict": (
            "Track VII CLOSED NEGATIVE for V7. Omega_dm is NOT a native V7 "
            "output under the simplest dark-matter production mechanisms "
            "(thermal freeze-out, Kibble-Zurek string vortons) given the "
            "stated U(1)_dark sector. H_0 stays as a one-parameter prediction "
            "(H_0 = 69.03 km/s/Mpc) using observed Ω_dm as input. Track VII "
            "continues in V8 with the re-identification of M_soliton and "
            "possible dark-sector extension (SU(2)_dark → U(1)_dark two-step "
            "breaking, non-topological solitons, or dark baryons). See "
            "theory/derivation/V8_TRACK_VII_ROADMAP.md."
        ),
        "missing_physics": [
            "Physical referent of M_soliton (non-topological soliton? dark baryon? "
            "SU(2)_dark monopole at UV scale?)",
            "Dark-sector UV completion (SU(2)_dark → U(1)_dark breaking chain)",
            "Soliton stability against decay (lifetime > age of universe)",
            "Dark sector phase-transition dynamics (first/second order)",
            "Non-Kibble-Zurek production mechanisms (Affleck-Dine, confining dynamics)",
        ],
        "what_would_close_the_track_in_V8": (
            "Extend V7's dark sector with SU(2)_dark → U(1)_dark at a UV scale "
            "above v_dark = 422 MeV. Monopoles form at the SU(2) breaking "
            "(π_2(SU(2)/U(1)) = ℤ), with mass ~M_soliton = 2.11×10⁹ GeV "
            "and Kibble-Zurek density n ~ 1/ξ_KZ³ at the UV scale. Strings "
            "form at the subsequent U(1) breaking (cosmologically negligible). "
            "This would reconcile M_soliton with topological DM and give "
            "Ω_dm a structural derivation from the UV scale."
        ),
        "status": "CLOSED NEGATIVE for V7. Continues in V8 (roadmap filed).",
    }


if __name__ == "__main__":
    import json
    status = track_vii_status()
    # Pretty print, handling numpy types
    def clean(obj):
        if isinstance(obj, dict):
            return {k: clean(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [clean(x) for x in obj]
        elif isinstance(obj, (np.floating, np.integer)):
            return float(obj)
        return obj
    print(json.dumps(clean(status), indent=2))
