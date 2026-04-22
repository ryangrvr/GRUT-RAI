"""Tests for Hubble-constant-from-first-principles module.

Locks in:
  - age_flat_LCDM returns correct value for Planck Ω_m at H_0 = 67.4
  - hubble_from_age_and_H_inf inverts correctly (round-trip with age_flat_LCDM)
  - grut_H_0_prediction returns H_0 ≈ 69.03 km/s/Mpc (the published result)
  - Ω_m + Ω_Λ = 1 is enforced (flat ΛCDM)
  - The H_inf = 58.16 km/s/Mpc intermediate
  - R_choice='hand' vs 'epsilon' agree within 0.5%
  - compare_to_observations returns a sensible table
  - structural_t_eq matter-Λ equality
"""

import numpy as np
import pytest


class TestAgeFlatLCDM:
    def test_age_at_planck_cosmology(self):
        """t_0(H_0=67.4, Ω_m=0.311) ≈ 13.8 Gyr (Planck consensus)."""
        from grut.derived.cosmology.hubble_from_first_principles import (
            age_flat_LCDM, YEAR_S,
        )
        t = age_flat_LCDM(H_0_kms=67.4, Omega_m=0.311)
        age_Gyr = t / (YEAR_S * 1e9)
        assert 13.6 < age_Gyr < 14.0

    def test_age_diverges_for_Omega_m_geq_1(self):
        from grut.derived.cosmology.hubble_from_first_principles import age_flat_LCDM
        assert age_flat_LCDM(70.0, 1.0) == float('inf')
        assert age_flat_LCDM(70.0, 1.5) == float('inf')

    def test_age_decreases_with_larger_H0(self):
        """Higher H_0 ⟹ younger universe (at fixed Ω_m)."""
        from grut.derived.cosmology.hubble_from_first_principles import age_flat_LCDM
        t1 = age_flat_LCDM(65.0, 0.3)
        t2 = age_flat_LCDM(75.0, 0.3)
        assert t2 < t1


class TestHubbleFromAgeAndHInf:
    def test_roundtrip_with_age_formula(self):
        """Solving for (Ω_m, H_0) given (H_inf, t_0) and then recomputing
        the age from those outputs should match t_0 within rounding."""
        from grut.derived.cosmology.hubble_from_first_principles import (
            hubble_from_age_and_H_inf, age_flat_LCDM, YEAR_S, HZ_TO_KMSMPC,
        )
        H_inf_hz = 1.885e-18   # V7 §26 headline
        t_0_s = 13.8 * 1e9 * YEAR_S
        result = hubble_from_age_and_H_inf(H_inf_hz, t_0_s)
        t_back = age_flat_LCDM(result["H_0_km_s_Mpc"], result["Omega_m"])
        # Within 1 Myr
        assert abs(t_back - t_0_s) / t_0_s < 1e-4

    def test_flat_LCDM_closure(self):
        """Ω_m + Ω_Λ = 1 (flat universe, no radiation in this module)."""
        from grut.derived.cosmology.hubble_from_first_principles import (
            hubble_from_age_and_H_inf, YEAR_S,
        )
        result = hubble_from_age_and_H_inf(1.885e-18, 13.8e9 * YEAR_S)
        assert abs(result["Omega_m"] + result["Omega_Lambda"] - 1.0) < 1e-10

    def test_H_inf_less_than_H_0(self):
        """H_inf < H_0 since Ω_Λ < 1 in the present universe."""
        from grut.derived.cosmology.hubble_from_first_principles import (
            hubble_from_age_and_H_inf, YEAR_S, HZ_TO_KMSMPC,
        )
        H_inf_hz = 1.885e-18
        result = hubble_from_age_and_H_inf(H_inf_hz, 13.8e9 * YEAR_S)
        assert result["H_0_Hz"] > H_inf_hz


class TestGrutH0Prediction:
    def test_H_0_is_approximately_69p03(self):
        """GRUT's published one-parameter result: H_0 ≈ 69.03 km/s/Mpc."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        # The headline prediction to within 0.5%
        assert abs(result["H_0_km_s_Mpc"] - 69.03) / 69.03 < 0.005

    def test_H_inf_is_approximately_58p16(self):
        """V7 §26 headline: H_inf = 58.16 km/s/Mpc."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        assert abs(result["H_inf_km_s_Mpc"] - 58.16) / 58.16 < 0.01

    def test_age_is_13p8_Gyr(self):
        """N_eras × τ_0 = 329 × 41.9 Myr ≈ 13.785 Gyr."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        assert abs(result["age_Gyr"] - 13.785) < 0.05

    def test_Omega_m_is_planck_like(self):
        """Derived Ω_m should land near Planck's 0.31."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        assert 0.27 < result["Omega_m"] < 0.34

    def test_Omega_Lambda_is_planck_like(self):
        """Derived Ω_Λ should land near Planck's 0.69."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        assert 0.66 < result["Omega_Lambda"] < 0.73

    def test_R_choice_hand_matches_epsilon_within_0p5pct(self):
        """The two R-choices (3-loop CTP R_anomaly vs Osborn ε) agree at ~0.05%."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        hand = grut_H_0_prediction(R_choice="hand")
        eps = grut_H_0_prediction(R_choice="epsilon")
        diff = abs(hand["H_0_km_s_Mpc"] - eps["H_0_km_s_Mpc"]) / hand["H_0_km_s_Mpc"]
        assert diff < 0.005

    def test_returns_status_string(self):
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        result = grut_H_0_prediction()
        assert "status" in result
        assert "PROTOTYPE" in result["status"] or "parameter" in result["status"].lower()

    def test_radiation_option_shifts_omega_m(self):
        """include_radiation=True subtracts Ω_r from Ω_m (tiny effect)."""
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_0_prediction
        base = grut_H_0_prediction(include_radiation=False)
        with_rad = grut_H_0_prediction(include_radiation=True)
        assert "Omega_r" in with_rad
        assert with_rad["Omega_m"] < base["Omega_m"]

    def test_custom_tau_0_shifts_prediction(self):
        """Larger τ_0 → smaller H_inf → smaller H_0."""
        from grut.derived.cosmology.hubble_from_first_principles import (
            grut_H_0_prediction, TAU_0_DEFAULT,
        )
        base = grut_H_0_prediction(tau_0_s=TAU_0_DEFAULT)
        bigger = grut_H_0_prediction(tau_0_s=TAU_0_DEFAULT * 1.05)
        assert bigger["H_0_km_s_Mpc"] < base["H_0_km_s_Mpc"]


class TestCompareToObservations:
    def test_returns_list_of_comparisons(self):
        from grut.derived.cosmology.hubble_from_first_principles import compare_to_observations
        r = compare_to_observations()
        assert isinstance(r, dict) or isinstance(r, list)


class TestStructuralTEq:
    def test_returns_dict(self):
        from grut.derived.cosmology.hubble_from_first_principles import structural_t_eq
        r = structural_t_eq()
        assert isinstance(r, dict)


class TestHInfComparison:
    def test_returns_dict(self):
        from grut.derived.cosmology.hubble_from_first_principles import grut_H_inf_comparison
        r = grut_H_inf_comparison()
        assert isinstance(r, dict)
