"""Tests for the Koide sector — mass formula and N=3 generation uniqueness.

V7 Section 29: K = (Σ m)/(Σ √m)² = 2/3 to 0.005% for charged leptons.
"""

import pytest
import numpy as np


class TestKoideCheck:
    """Tests for koide_check — the K=2/3 formula for charged leptons."""

    def test_returns_expected_keys(self):
        from grut.derived.koide.identity import koide_check
        result = koide_check()
        for key in ("K", "exact", "deviation_pct", "status"):
            assert key in result

    def test_exact_is_2_over_3(self):
        from grut.derived.koide.identity import koide_check
        result = koide_check()
        assert abs(result["exact"] - 2.0/3.0) < 1e-12

    def test_K_matches_2_over_3_to_percent(self):
        """V7: Koide identity is satisfied to 0.005% for measured lepton masses."""
        from grut.derived.koide.identity import koide_check
        result = koide_check()
        assert abs(result["K"] - 2.0/3.0) < 0.001

    def test_deviation_under_0p01pct(self):
        """V7 central claim: deviation is 0.005% — tolerate 0.01% in tests."""
        from grut.derived.koide.identity import koide_check
        result = koide_check()
        assert abs(result["deviation_pct"]) < 0.01

    def test_status_is_PROVEN(self):
        from grut.derived.koide.identity import koide_check
        result = koide_check()
        assert "PROVEN" in result["status"]

    def test_custom_masses_electron_muon_tau(self):
        """Explicit PDG values reproduce K ≈ 2/3."""
        from grut.derived.koide.identity import koide_check
        # PDG 2022 charged lepton masses in MeV
        masses = [0.51099895, 105.6583755, 1776.86]
        result = koide_check(masses=masses)
        assert abs(result["K"] - 2.0/3.0) < 0.001


class TestNGenerationUniqueness:
    """Tests for n_generation_uniqueness — N=3 is uniquely selected."""

    def test_N_3_is_constant(self):
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert result["results"][3]["constant"]

    def test_N_3_K_mean_equals_2_over_3(self):
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert abs(result["results"][3]["K_mean"] - 2.0/3.0) < 1e-10

    def test_N_3_K_std_is_essentially_zero(self):
        """At N=3, K is invariant across all input distributions → std=0."""
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert result["results"][3]["K_std"] < 1e-10

    def test_N_2_is_not_constant(self):
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert not result["results"][2]["constant"]

    def test_unique_N_is_3(self):
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert result["unique_N"] == 3

    def test_status_is_PROVEN(self):
        from grut.derived.koide.identity import n_generation_uniqueness
        result = n_generation_uniqueness(n_max=5)
        assert "PROVEN" in result["status"]


class TestFitLeptons:
    """Tests for fit_leptons — the (M0, θ) Koide-operator parameters."""

    def test_returns_M0_and_theta(self):
        from grut.derived.koide.identity import fit_leptons
        result = fit_leptons()
        for key in ("M0", "theta_rad", "theta_deg"):
            assert key in result

    def test_M0_is_positive_finite(self):
        from grut.derived.koide.identity import fit_leptons
        result = fit_leptons()
        assert np.isfinite(result["M0"])
        assert result["M0"] > 0

    def test_theta_in_valid_range(self):
        from grut.derived.koide.identity import fit_leptons
        result = fit_leptons()
        assert np.isfinite(result["theta_rad"])
        # theta is an angle; allow full [0, 2π) range
        assert 0 <= result["theta_rad"] <= 2 * np.pi

    def test_theta_deg_consistent_with_theta_rad(self):
        from grut.derived.koide.identity import fit_leptons
        result = fit_leptons()
        expected_deg = result["theta_rad"] * 180 / np.pi
        assert abs(result["theta_deg"] - expected_deg) < 1e-6

    def test_status_is_FITTED(self):
        """V7 §29: M0 and θ are FITTED, not DERIVED. Track II goal is to derive."""
        from grut.derived.koide.identity import fit_leptons
        result = fit_leptons()
        assert "FITTED" in result["status"] or "MAPPED" in result["status"]
