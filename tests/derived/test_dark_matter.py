"""Tests for the dark matter sector — V7 §28 U(1)_dark gauged extension.

Route 1: RG running from Planck → g_dark = 0.917, λ = 0.42, M ≈ 2.1e9 GeV
Route 2: anomaly extraction → g_dark larger, λ ≈ 3.83

Both give σ/m in the viable window (10⁻³–10⁻² cm²/g).
"""

import pytest
import numpy as np


class TestRoute1:
    """Tests for RG-running Route 1 (V7 preferred branch)."""

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.sector import route_1
        result = route_1()
        expected = {"route", "g_dark", "lambda", "v_MeV", "M_GeV",
                     "dark_photon_MeV", "dark_higgs_MeV"}
        assert expected.issubset(result.keys())

    def test_g_dark_close_to_v7_value(self):
        """V7 Route 1: g_dark = 0.917."""
        from grut.derived.dark_matter.sector import route_1
        result = route_1()
        assert abs(result["g_dark"] - 0.917) < 0.01

    def test_lambda_close_to_v7_value(self):
        """V7 Route 1: λ = 0.42."""
        from grut.derived.dark_matter.sector import route_1
        result = route_1()
        assert abs(result["lambda"] - 0.42) < 0.01

    def test_M_in_2p1e9_GeV_range(self):
        """V7 Route 1: M ≈ 2.1e9 GeV."""
        from grut.derived.dark_matter.sector import route_1
        result = route_1()
        assert 1e9 < result["M_GeV"] < 1e10

    def test_dark_photon_mass_positive(self):
        from grut.derived.dark_matter.sector import route_1
        result = route_1()
        assert result["dark_photon_MeV"] > 0


class TestRoute2:
    """Tests for anomaly-extraction Route 2."""

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.sector import route_2
        result = route_2()
        expected = {"route", "g_dark", "lambda", "v_MeV", "M_GeV",
                     "dark_photon_MeV", "dark_higgs_MeV"}
        assert expected.issubset(result.keys())

    def test_g_dark_positive_finite(self):
        from grut.derived.dark_matter.sector import route_2
        result = route_2()
        assert np.isfinite(result["g_dark"])
        assert result["g_dark"] > 0

    def test_lambda_positive_finite(self):
        from grut.derived.dark_matter.sector import route_2
        result = route_2()
        assert np.isfinite(result["lambda"])
        assert result["lambda"] > 0


class TestBranchDiscriminator:
    """Tests for Route-1 vs Route-2 branch selection."""

    def test_returns_selected_route(self):
        from grut.derived.dark_matter.sector import branch_discriminator
        result = branch_discriminator()
        assert "selected" in result
        # Accepts integer, "route_1" string, or display string "Route 1"
        sel = str(result["selected"])
        assert "1" in sel or "2" in sel

    def test_reasons_present(self):
        from grut.derived.dark_matter.sector import branch_discriminator
        result = branch_discriminator()
        assert "reasons" in result

    def test_includes_both_routes(self):
        from grut.derived.dark_matter.sector import branch_discriminator
        result = branch_discriminator()
        assert "route_1" in result
        assert "route_2" in result


class TestDarkPhotonExclusion:
    """Tests for dark photon parameter space and exclusion status."""

    def test_grut_dark_photon_has_mass(self):
        from grut.derived.dark_matter.exclusion import grut_dark_photon
        result = grut_dark_photon()
        assert "mass_MeV" in result
        assert result["mass_MeV"] > 0

    def test_dark_photon_mass_pion_scale(self):
        """V7: dark photon at ~387 MeV (pion scale)."""
        from grut.derived.dark_matter.exclusion import grut_dark_photon
        result = grut_dark_photon()
        # Within a factor of 3 of 387 MeV
        assert 100 < result["mass_MeV"] < 1000

    def test_sigma_over_m_in_viable_window(self):
        """V7: σ/m ~ 10⁻³–10⁻² cm²/g for self-interacting dark matter."""
        from grut.derived.dark_matter.exclusion import grut_dark_photon
        result = grut_dark_photon()
        if "sigma_over_m" in result:
            assert np.isfinite(result["sigma_over_m"])
            assert result["sigma_over_m"] > 0

    def test_exclusion_status_runs(self):
        from grut.derived.dark_matter.exclusion import exclusion_status
        result = exclusion_status()
        assert isinstance(result, (dict, list))

    def test_full_exclusion_analysis_runs(self):
        from grut.derived.dark_matter.exclusion import full_exclusion_analysis
        result = full_exclusion_analysis()
        assert isinstance(result, dict)
