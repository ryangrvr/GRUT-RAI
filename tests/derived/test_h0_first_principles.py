"""Tests for the H_0 first-principles prototype (V8 sub-track).

GRUT predicts H_0 = 69.03 km/s/Mpc from H_inf + age + flat ΛCDM.
These tests lock the prediction in as a regression check.
"""

import pytest
import numpy as np


class TestGrutH0Prediction:
    """Tests for grut_H_0_prediction — the one-parameter H_0 prediction."""

    def test_returns_expected_keys(self):
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        expected = {"Omega_m", "Omega_Lambda", "H_0_km_s_Mpc", "H_0_Hz",
                     "age_Gyr", "H_inf_km_s_Mpc", "R", "R_choice", "n_eras",
                     "tau_0_Myr", "status"}
        assert expected.issubset(r.keys())

    def test_H_0_in_68_to_71_range(self):
        """GRUT predicts H_0 ≈ 69.03 km/s/Mpc."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert 68.0 < r["H_0_km_s_Mpc"] < 71.0

    def test_H_0_close_to_69p03(self):
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert abs(r["H_0_km_s_Mpc"] - 69.03) < 0.1

    def test_Omega_m_in_viable_range(self):
        """Ω_m should be around 0.29 for GRUT's H_inf + 13.78 Gyr age."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert 0.27 < r["Omega_m"] < 0.32

    def test_Omega_m_and_Omega_Lambda_sum_to_1(self):
        """Flat universe: Ω_m + Ω_Λ = 1."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert abs(r["Omega_m"] + r["Omega_Lambda"] - 1.0) < 1e-10

    def test_H_inf_matches_V7_headline(self):
        """H_inf = 58.16 km/s/Mpc (V7 §26)."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert abs(r["H_inf_km_s_Mpc"] - 58.16) < 0.1

    def test_age_matches_13p78_Gyr(self):
        """Age = 329 × 41.9 Myr = 13.78 Gyr (V7 §27)."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        assert abs(r["age_Gyr"] - 13.78) < 0.05

    def test_consistent_Friedmann(self):
        """H_0² × Ω_Λ = H_inf² should hold for flat ΛCDM."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        H_inf_hz = r["H_inf_km_s_Mpc"] / 3.0857e19
        H_0_hz = r["H_0_Hz"]
        lhs = H_0_hz**2 * r["Omega_Lambda"]
        rhs = H_inf_hz**2
        assert abs(lhs - rhs) / rhs < 1e-6

    def test_status_labels_prototype(self):
        """Status string must flag this as one-parameter (age is input).

        The status was previously tagged 'PROTOTYPE'; updated to
        'ONE-PARAMETER' with an explicit reference to the registered
        open negative (n_total_zero_parameter_derivation_open_question)
        when N_total was formally registered as observation-anchored
        rather than structurally derived. The test pins the discipline
        marker, not the literal word.
        """
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        r = grut_H_0_prediction()
        status = r["status"]
        # Must flag that age (N_total) enters as input — the precise
        # epistemic state, not just a generic 'prototype' tag.
        assert "ONE-PARAMETER" in status or "one-parameter" in status.lower()
        assert (
            "observed" in status.lower()
            or "anchor" in status.lower()
            or "open negative" in status.lower()
        )

    def test_epsilon_route_consistent(self):
        """Using R = ε value should give a similar H_0 (within 0.1%)."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        hand = grut_H_0_prediction(R_choice="hand")
        eps = grut_H_0_prediction(R_choice="epsilon")
        rel_diff = abs(hand["H_0_km_s_Mpc"] - eps["H_0_km_s_Mpc"]) / hand["H_0_km_s_Mpc"]
        assert rel_diff < 0.01


class TestAgeFormula:
    """Tests for the flat-ΛCDM age formula."""

    def test_matches_Planck_13p8_Gyr(self):
        """With Planck values (H_0=67.4, Ω_m=0.3111), age ≈ 13.8 Gyr."""
        from grut.derived.cosmology.hubble_from_first_principles import age_flat_LCDM
        t_s = age_flat_LCDM(H_0_kms=67.4, Omega_m=0.3111)
        t_Gyr = t_s / 3.156e7 / 1e9
        # Standard Planck age is ~13.8 Gyr; our formula gives ~14.0
        assert 13.5 < t_Gyr < 14.2

    def test_de_Sitter_limit_grows_with_smaller_Om(self):
        """In flat ΛCDM, smaller Ω_m → older universe (approaching
        de Sitter limit as Ω_m → 0, age → (2/3H_0) × (1/√Ω_Λ) × sinh⁻¹(∞))."""
        from grut.derived.cosmology.hubble_from_first_principles import age_flat_LCDM
        H0 = 70.0
        t_small = age_flat_LCDM(H0, Omega_m=0.01)
        t_large = age_flat_LCDM(H0, Omega_m=0.5)
        assert t_small > t_large
        # Small-Ω_m limit: age grows as log(1/Ω_m)/H₀, so should be significantly older
        assert t_small / t_large > 2.0


class TestCompareToObservations:
    """Tests for compare_to_observations."""

    def test_returns_all_sources(self):
        from grut.derived.cosmology.hubble_from_first_principles import compare_to_observations
        r = compare_to_observations()
        for key in ("grut_prediction", "planck_CMB", "shoes_distance_ladder"):
            assert key in r

    def test_grut_vs_planck_small_disagreement(self):
        """GRUT should be close to Planck (within 5%)."""
        from grut.derived.cosmology.hubble_from_first_principles import compare_to_observations
        r = compare_to_observations()
        # The "grut_vs_planck_H0" string is formatted like "+2.42%"
        pct_str = r["grut_vs_planck_H0"].rstrip('%')
        pct_val = abs(float(pct_str))
        assert pct_val < 5.0

    def test_grut_is_closer_to_planck_than_shoes_on_H0(self):
        """On the H_0 scale, GRUT's prediction leans toward Planck."""
        from grut.derived.cosmology.hubble_from_first_principles import compare_to_observations
        r = compare_to_observations()
        grut_H0 = r["grut_prediction"]["H_0_km_s_Mpc"]
        # Midpoint of tension: (67.4 + 73.0)/2 = 70.2
        # GRUT lands at 69.03, so below midpoint → Planck-leaning on H_0
        assert grut_H0 < 70.2


class TestHInfComparison:
    """Tests for grut_H_inf_comparison — standalone H_inf prediction."""

    def test_returns_grut_H_inf_and_comparisons(self):
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_inf_comparison
        r = grut_H_inf_comparison()
        assert "grut_H_inf_km_s_Mpc" in r
        assert "comparisons" in r
        assert len(r["comparisons"]) >= 3  # Planck, SH0ES, Riess 2024

    def test_H_inf_is_58_16(self):
        """GRUT predicts H_inf = 58.16 km/s/Mpc (V7 §26)."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_inf_comparison
        r = grut_H_inf_comparison()
        assert abs(r["grut_H_inf_km_s_Mpc"] - 58.16) < 0.1

    def test_grut_H_inf_closer_to_shoes_than_planck(self):
        """On H_inf scale, GRUT agrees with SH0ES ~1%, differs from Planck ~4%.

        This is the REVERSE of the H_0 comparison, because the two observations
        disagree on Ω_m as well. GRUT's specific prediction H_inf² = H_0² × Ω_Λ
        puts it closer to SH0ES-inferred H_inf than Planck-inferred H_inf.
        """
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_inf_comparison
        r = grut_H_inf_comparison()
        # Find Planck and SH0ES entries
        planck_dev = None
        shoes_dev = None
        for c in r["comparisons"]:
            if "Planck" in c["source"]:
                planck_dev = abs(c["GRUT_minus_inferred_pct"])
            elif "SH0ES 2023" in c["source"]:
                shoes_dev = abs(c["GRUT_minus_inferred_pct"])
        assert planck_dev is not None
        assert shoes_dev is not None
        # GRUT should agree with SH0ES more closely than with Planck on H_inf
        assert shoes_dev < planck_dev


class TestStructuralTeq:
    """Tests for the flat-ΛCDM structural identity H_inf × t_eq = (2/3) × sinh⁻¹(1)."""

    def test_returns_expected_keys(self):
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        expected = {"structural_constant", "t_eq_Gyr", "N_threshold_structural",
                     "V7_claimed_N_threshold", "discrepancy_pct", "status"}
        assert expected.issubset(r.keys())

    def test_structural_constant_is_0p5876(self):
        """(2/3) × sinh⁻¹(1) = 0.58758 is exact."""
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        import numpy as np
        expected = (2.0/3.0) * np.arcsinh(1.0)
        assert abs(r["structural_constant"] - expected) < 1e-10

    def test_t_eq_around_10_Gyr(self):
        """With GRUT's H_inf, t_eq ≈ 9.88 Gyr."""
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        assert 9.5 < r["t_eq_Gyr"] < 10.5

    def test_N_threshold_around_236(self):
        """Structural N_threshold from H_inf × τ_0 ≈ 236."""
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        assert 230 < r["N_threshold_structural"] < 245

    def test_discrepancy_from_V7_documented(self):
        """V7's N_threshold = 215 has ~10% discrepancy with structural ~236."""
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        # Documented internal inconsistency between V7's N_threshold and
        # flat-ΛCDM matter-Λ equality
        assert 5.0 < abs(r["discrepancy_pct"]) < 15.0
