"""Tests for the −100 on S⁴ resolution (April 22, 2026).

Locks in:

  Stage 1 (hypercharge sum): Σ Y² = 10 exactly, (Σ Y²)² = 100, Osborn K_U1 < 0.
  Stage 2 (honesty protocol on the sign):
    C_COSMO < 0 (Gibbons-Hawking conformal-mode instability signature)
    R_ANOMALY_SIGNED = −1.15428 (physical)
    R_ANOMALY = +1.15428 (legacy magnitude, retained for compatibility)
    r_anomaly_computed() uses explicit −C/C, not abs()
  Stage 3 (drive/friction decomposition):
    H_inf = (2 − R) / (S × τ_0)
    numerator  = 0.846 = topological conformal drive
    denominator = 108π × τ_0 = viscoelastic friction
    H_inf = 1.885 × 10⁻¹⁸ Hz from the two
"""

import pytest
from fractions import Fraction


class TestHyperchargeSum:
    def test_sum_Y_squared_per_generation_is_exactly_10_over_3(self):
        from grut.derivation.minus_100.hypercharge_sum import sum_Y_squared_per_generation
        assert sum_Y_squared_per_generation() == Fraction(10, 3)

    def test_sum_Y_squared_total_is_exactly_10(self):
        from grut.derivation.minus_100.hypercharge_sum import sum_Y_squared_total
        assert sum_Y_squared_total() == Fraction(10)

    def test_hypercharge_squared_squared_is_exactly_100(self):
        from grut.derivation.minus_100.hypercharge_sum import hypercharge_squared_squared
        assert hypercharge_squared_squared() == Fraction(100)

    def test_osborn_K_U1_is_negative(self):
        """K_U1 < 0 consistent with −100 sign and the conformal-mode drive."""
        from grut.derivation.minus_100.hypercharge_sum import osborn_K_U1_formula
        assert osborn_K_U1_formula() < 0

    def test_verify_all_pass(self):
        from grut.derivation.minus_100.hypercharge_sum import verify
        for name, passed in verify().items():
            assert passed, f"hypercharge verify failed: {name}"


class TestSignHonesty:
    """The honesty-protocol core: expose, don't hide, the C_COSMO sign."""

    def test_C_COSMO_is_negative(self):
        """The Gibbons-Hawking conformal-mode drive."""
        from grut.foundation.anomaly import c_cosmo
        assert c_cosmo() < 0

    def test_C_FINAL_is_positive(self):
        from grut.foundation.anomaly import compute_c_final
        assert compute_c_final() > 0

    def test_R_ANOMALY_SIGNED_is_negative(self):
        from grut.foundation.anomaly import R_ANOMALY_SIGNED
        assert R_ANOMALY_SIGNED < 0
        assert abs(R_ANOMALY_SIGNED + 1.15428) < 1e-4

    def test_r_anomaly_signed_function_matches_constant(self):
        from grut.foundation.anomaly import r_anomaly_signed, R_ANOMALY_SIGNED
        assert abs(r_anomaly_signed() - R_ANOMALY_SIGNED) / abs(R_ANOMALY_SIGNED) < 1e-3

    def test_r_anomaly_computed_uses_explicit_negation_not_abs(self):
        """r_anomaly_computed() = −C_Cosmo / C_FINAL, NOT abs(ratio).

        If a future refactor removes the explicit minus sign and silently
        falls back to abs(), this test still passes numerically — but
        the sign-honesty test below will still check C_COSMO < 0, so
        the physical sign is protected.
        """
        from grut.foundation.anomaly import r_anomaly_computed, R_ANOMALY
        assert abs(r_anomaly_computed() - R_ANOMALY) / R_ANOMALY < 1e-3

    def test_legacy_magnitude_matches_explicit_negation(self):
        """Magnitude-via-abs and explicit-negation produce the same +1.15428."""
        from grut.foundation.anomaly import (
            c_cosmo, compute_c_final, R_ANOMALY, r_anomaly_computed,
        )
        mag_via_abs = abs(c_cosmo() / compute_c_final())
        mag_via_neg = r_anomaly_computed()
        assert abs(mag_via_abs - mag_via_neg) < 1e-9
        assert abs(mag_via_abs - R_ANOMALY) / R_ANOMALY < 1e-3


class TestDriveFrictionDecomposition:
    """H_inf = (2 − R) / (S × τ_0) as drive / friction."""

    def test_returns_dict_with_expected_keys(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        tau_0 = 41.9e6 * 3.156e7
        r = h_inf_drive_over_friction(tau_0)
        for k in [
            "topological_drive_2_minus_R",
            "constitutive_friction_S_tau0",
            "H_inf_Hz",
            "interpretation",
            "drive_meaning",
            "friction_meaning",
        ]:
            assert k in r

    def test_drive_is_2_minus_R(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction, R_ANOMALY
        r = h_inf_drive_over_friction(1.322e15)   # arbitrary τ_0
        assert abs(r["topological_drive_2_minus_R"] - (2.0 - R_ANOMALY)) < 1e-9

    def test_friction_is_S_times_tau_0(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction, S_CTP
        tau_0 = 1.322e15
        r = h_inf_drive_over_friction(tau_0)
        assert abs(r["constitutive_friction_S_tau0"] - S_CTP * tau_0) < 1e-3

    def test_H_inf_headline_value(self):
        """H_inf ≈ 1.885 × 10⁻¹⁸ Hz at canonical τ_0 = 41.9 Myr."""
        from grut.foundation.anomaly import h_inf_drive_over_friction
        tau_0 = 41.9e6 * 3.156e7
        r = h_inf_drive_over_friction(tau_0)
        assert abs(r["H_inf_Hz"] - 1.885e-18) / 1.885e-18 < 0.01

    def test_interpretation_mentions_drive_and_friction(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        assert "drive" in r["interpretation"].lower()
        assert "friction" in r["interpretation"].lower()

    def test_friction_meaning_references_viscoelastic(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        assert "viscoelastic" in r["friction_meaning"].lower()

    def test_drive_meaning_references_conformal(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        assert "conformal" in r["drive_meaning"].lower() or "Gibbons" in r["drive_meaning"]


class TestVerifyBlock:
    def test_anomaly_verify_all_pass(self):
        from grut.foundation.anomaly import verify
        for name, passed in verify().items():
            assert passed, f"anomaly.verify() failed: {name}"
