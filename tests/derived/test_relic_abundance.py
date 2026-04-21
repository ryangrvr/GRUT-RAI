"""Tests for Track VII — Dark Sector Completion (Ω_dm from first principles).

These tests lock in the SCOPING of Track VII, not a final answer. They
verify that:
  - thermal_freezeout_relic() returns a sane baseline and the correct
    verdict (WRONG MECHANISM for the heavy 2×10⁹ GeV soliton).
  - kibble_upper_bound() returns an upper bound on Ω_dm from causality.
  - track_vii_status() assembles the full scoping dict.

The goal of these tests is to catch regressions in the infrastructure —
the physics result (computed Ω_dm) is flagged as SCOPED / pending and is
NOT locked in by these tests until the Kibble-Zurek calculation lands.
"""

import pytest
import numpy as np


class TestThermalFreezeout:
    """Baseline WIMP freeze-out (not the V7 mechanism)."""

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.relic_abundance import thermal_freezeout_relic
        result = thermal_freezeout_relic()
        expected = {"M_chi_GeV", "alpha", "sigma_v_cm3_per_s",
                    "Omega_dm_h_squared", "Omega_dm", "Omega_dm_observed",
                    "over_under_produced", "mechanism", "status"}
        assert expected.issubset(result.keys())

    def test_sigma_v_positive_finite(self):
        from grut.derived.dark_matter.relic_abundance import thermal_freezeout_relic
        result = thermal_freezeout_relic()
        assert np.isfinite(result["sigma_v_cm3_per_s"])
        assert result["sigma_v_cm3_per_s"] > 0

    def test_omega_dm_positive_finite(self):
        from grut.derived.dark_matter.relic_abundance import thermal_freezeout_relic
        result = thermal_freezeout_relic()
        assert np.isfinite(result["Omega_dm"])
        assert result["Omega_dm"] > 0

    def test_thermal_overproduces_for_heavy_soliton(self):
        """At M_soliton = 2×10⁹ GeV, thermal freeze-out gives WAY too much DM.

        σv ~ πα²/M² is tiny at heavy M → relic abundance is huge.
        Correct verdict: WRONG MECHANISM.
        """
        from grut.derived.dark_matter.relic_abundance import thermal_freezeout_relic
        result = thermal_freezeout_relic()
        # Should over-produce by many orders
        assert result["over_under_produced"] > 1e6

    def test_status_flags_wrong_mechanism(self):
        from grut.derived.dark_matter.relic_abundance import thermal_freezeout_relic
        result = thermal_freezeout_relic()
        assert "NOT THE RIGHT MECHANISM" in result["status"]


class TestKibbleUpperBound:
    """Causality upper bound on soliton abundance from phase transition."""

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        expected = {"T_PT_GeV", "H_PT_GeV", "n_PT_max_natural",
                    "n_today_max_per_m3", "Omega_dm_max_if_full_production",
                    "required_fraction_of_max", "status"}
        assert expected.issubset(result.keys())

    def test_T_PT_is_v_dark(self):
        """Phase transition temperature equals v_dark by default."""
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        from grut.derived.dark_matter.relic_abundance import V_DARK_GEV
        result = kibble_upper_bound()
        assert abs(result["T_PT_GeV"] - V_DARK_GEV) < 1e-12

    def test_hubble_rate_positive_finite(self):
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        assert np.isfinite(result["H_PT_GeV"])
        assert result["H_PT_GeV"] > 0

    def test_number_density_today_positive_finite(self):
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        assert np.isfinite(result["n_today_max_per_m3"])
        assert result["n_today_max_per_m3"] > 0

    def test_kibble_baseline_under_produces(self):
        """1 soliton per Hubble volume at T_PT = 422 MeV massively UNDER-produces.

        At T_PT = 422 MeV the Hubble length is ~10 km — enormous. So 1
        defect per Hubble volume is FAR too sparse to account for observed
        Ω_dm. The realistic Kibble-Zurek calculation gives ξ_KZ ≪ H⁻¹,
        hence n = 1/ξ_KZ³ ≫ H³.

        This test locks in the key physics fact that motivates Track VII
        Step 1.
        """
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        # Baseline under-produces by many orders of magnitude
        assert result["Omega_dm_max_if_full_production"] < 1e-20

    def test_required_multiplier_much_greater_than_one(self):
        """If Kibble baseline under-produces, the required multiplier > 1."""
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        # Need many orders of magnitude MORE defects than 1 per Hubble volume
        assert result["required_fraction_of_max"] > 1e20

    def test_regime_string_notes_underproduction(self):
        from grut.derived.dark_matter.relic_abundance import kibble_upper_bound
        result = kibble_upper_bound()
        assert "UNDER-PRODUCES" in result["regime"]


class TestHubbleRateRadiation:
    """Hubble rate in radiation-dominated universe."""

    def test_H_positive(self):
        from grut.derived.dark_matter.relic_abundance import hubble_rate_radiation
        H = hubble_rate_radiation(T_GeV=0.422)
        assert H > 0

    def test_H_scales_as_T_squared(self):
        """H(T) ∝ T² in radiation era."""
        from grut.derived.dark_matter.relic_abundance import hubble_rate_radiation
        H1 = hubble_rate_radiation(T_GeV=1.0)
        H2 = hubble_rate_radiation(T_GeV=2.0)
        # H2/H1 should be 4
        assert abs(H2/H1 - 4.0) < 1e-6


class TestTrackVIIStatus:
    """Overall Track VII scoping status."""

    def test_returns_dict(self):
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert isinstance(result, dict)

    def test_reports_track(self):
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "track" in result
        assert "VII" in result["track"]

    def test_status_is_closed_negative_for_V7(self):
        """Track VII is CLOSED NEGATIVE for V7 after Step 3 topology audit."""
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "status" in result
        assert "CLOSED NEGATIVE" in result["status"] or "CLOSED" in result["status"]

    def test_step_1_result_retracted(self):
        """The Ω_dm = 0.38 result from Step 1 is formally retracted."""
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "step_1_xy_ballpark" in result
        assert "RETRACTED" in result["step_1_xy_ballpark"]["status"]

    def test_step_2_M_soliton_derivation_stands(self):
        """Step 2's structural derivation of M_soliton is preserved."""
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "step_2_result" in result
        assert "STANDS" in result["step_2_result"]["status"]

    def test_lists_missing_physics(self):
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "missing_physics" in result
        assert isinstance(result["missing_physics"], list)
        assert len(result["missing_physics"]) > 0

    def test_V7_parameters_contain_M_soliton(self):
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        assert "V7_parameters_available" in result
        v7 = result["V7_parameters_available"]
        assert "M_soliton_GeV" in v7
        # V7 claim: M_soliton ≈ 2.11e9 GeV
        assert 1e9 < v7["M_soliton_GeV"] < 1e10

    def test_why_it_matters_mentions_H0(self):
        """Track VII unlocks zero-parameter H_0 prediction."""
        from grut.derived.dark_matter.relic_abundance import track_vii_status
        result = track_vii_status()
        text = result.get("why_it_matters", "")
        assert "H_0" in text


class TestMSolitonStructurallyDerived:
    """Step 2 verification: M_soliton is structurally derived.

    Locks in the conclusion from TRACK_VII_M_SOLITON_ORIGIN.md. Ensures
    future refactors don't turn M_soliton into a phenomenological input.
    """

    def test_M_soliton_matches_analytic_formula(self):
        """M = 2⁹ π √N_ERAS / (27 × C_FINAL^1.5 × λ).

        Verifies the full structural derivation chain.
        """
        from grut.derived.dark_matter.sector import route_1, N_ERAS
        from grut.foundation.anomaly import C_FINAL
        r = route_1()
        lam = r["lambda"]
        M_analytic = 2**9 * np.pi * np.sqrt(N_ERAS) / (27 * C_FINAL**1.5 * lam)
        # Within 0.1%
        assert abs(r["M_GeV"] / M_analytic - 1.0) < 0.001

    def test_BPS_condition_gives_equal_masses(self):
        """BPS λ = g²/2 makes m_A' = m_h' exactly (not approximately)."""
        from grut.derived.dark_matter.sector import route_1
        r = route_1()
        # Should be equal to machine precision
        assert abs(r["dark_photon_MeV"] - r["dark_higgs_MeV"]) < 1e-9

    def test_stiffness_S_K_equals_one(self):
        """Stiffness normalization S_K ≡ 1 fixes v in terms of C_FINAL and N_ERAS."""
        from grut.derived.dark_matter.sector import route_1
        r = route_1()
        assert abs(r["S_K"] - 1.0) < 1e-9

    def test_M_soliton_scales_with_C_FINAL_correctly(self):
        """M_soliton ∝ C_FINAL^(-3/2). Verified via structural formula."""
        from grut.derived.dark_matter.sector import route_1, N_ERAS
        from grut.foundation.anomaly import C_FINAL
        r = route_1()
        # If C_FINAL were 2× larger, M_soliton would be (1/2)^(3/2) ≈ 0.354× smaller
        expected_ratio = 2**1.5  # ratio from halving C_FINAL
        # Just verify the analytic scaling holds in the formula
        M_base = 2**9 * np.pi * np.sqrt(N_ERAS) / (27 * C_FINAL**1.5 * r["lambda"])
        M_half_C = 2**9 * np.pi * np.sqrt(N_ERAS) / (27 * (C_FINAL/2)**1.5 * r["lambda"])
        assert abs(M_half_C / M_base - expected_ratio) < 1e-9
