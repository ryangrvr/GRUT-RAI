"""Tests for the Correction #16 structural identification.

Locks in:
  - SM field counts (scalars 4, Weyl fermions 45, gauge bosons 12)
  - 1-loop conformal-anomaly numerators (a = 1991/2, c = 418)
  - U(1)_Y 1-loop β = 20/3 (= 2/3 × ΣY²)
  - Conformal-mode kinetic sign = −1 (Gibbons-Hawking-Perry 1978)
  - 2-loop U(1)² species factor = 100
  - 2-loop normalization denominator = 256 (→ 1/(256π⁴), matches C_Cosmo)
  - Structural coefficient under s4_geometric_factor = 1 gives −100
  - Three falsifiers codified with correct status fields
"""

from fractions import Fraction
import pytest


class TestConformalAnomaly:
    def test_sm_field_counts(self):
        from grut.derivation.minus_100.conformal_anomaly import (
            N_SCALARS_SM, N_WEYL_FERMIONS_SM, N_GAUGE_BOSONS_SM,
        )
        assert N_SCALARS_SM == 4
        assert N_WEYL_FERMIONS_SM == 45
        assert N_GAUGE_BOSONS_SM == 12

    def test_a_coefficient_numerator_exact(self):
        from grut.derivation.minus_100.conformal_anomaly import a_coefficient_numerator
        # 4 + (11/2)(45) + 62(12) = 4 + 495/2 + 744 = 1991/2
        assert a_coefficient_numerator() == Fraction(1991, 2)

    def test_c_coefficient_numerator_exact(self):
        from grut.derivation.minus_100.conformal_anomaly import c_coefficient_numerator
        # 4 + 6(45) + 12(12) = 4 + 270 + 144 = 418
        assert c_coefficient_numerator() == Fraction(418)

    def test_U1_beta_is_20_over_3(self):
        from grut.derivation.minus_100.conformal_anomaly import U1_beta_function_one_loop
        assert U1_beta_function_one_loop() == Fraction(20, 3)

    def test_verify_all_pass(self):
        from grut.derivation.minus_100.conformal_anomaly import verify
        for k, v in verify().items():
            assert v, f"conformal_anomaly.verify() failed: {k}"


class TestConformalModeCoefficient:
    def test_sign_is_minus_one_from_GHP(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import conformal_mode_kinetic_sign
        assert conformal_mode_kinetic_sign() == -1

    def test_species_factor_is_100(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import two_loop_U1_squared_species_factor
        assert two_loop_U1_squared_species_factor() == 100

    def test_normalization_denominator_is_256(self):
        """1/(16π²)² = 1/(256π⁴) matches C_Cosmo prefactor exactly."""
        from grut.derivation.minus_100.conformal_mode_coefficient import two_loop_normalization_denominator
        assert two_loop_normalization_denominator() == 256

    def test_structural_coefficient_is_minus_100_under_s4_eq_1(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import structural_coefficient
        assert structural_coefficient(Fraction(1)) == Fraction(-100)

    def test_structural_coefficient_scales_linearly_with_geometric_factor(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import structural_coefficient
        base = structural_coefficient(Fraction(1))   # −100
        half = structural_coefficient(Fraction(1, 2))  # −50
        assert half == base / 2

    def test_identification_status_reports_all_four_rigor_components(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import identification_status
        r = identification_status()
        shown = r["shown_rigorously"]
        for k in [
            "A_sign_is_negative_from_GHP_1978",
            "B_species_factor_is_100",
            "C_normalization_is_1_over_256_pi4",
            "C_matches_C_Cosmo_prefactor",
            "D_expected_coefficient_under_s4=1",
        ]:
            assert shown[k] is True, f"Structural component {k} should be True"

    def test_identification_names_narrow_specialist_task(self):
        from grut.derivation.minus_100.conformal_mode_coefficient import identification_status
        r = identification_status()
        task = r["open_narrow_specialist_task"]["description"]
        assert "S⁴" in task
        assert "Allen-Jacobson" in task
        # Task description should reference the unity / geometric-factor hypothesis
        assert "to 1" in task or "unity" in task.lower()


class TestFalsifiers:
    def test_F1_pending_by_default(self):
        from grut.derivation.minus_100.falsifiers import falsifier_1_s4_geometric_factor
        r = falsifier_1_s4_geometric_factor()
        assert r["status"] == "PENDING"
        assert r["falsifier"] == "F1"

    def test_F1_passes_when_measured_equals_one(self):
        from grut.derivation.minus_100.falsifiers import falsifier_1_s4_geometric_factor
        r = falsifier_1_s4_geometric_factor(measured_factor=Fraction(1))
        assert r["status"] == "PASSED"

    def test_F1_falsified_when_measured_differs(self):
        from grut.derivation.minus_100.falsifiers import falsifier_1_s4_geometric_factor
        r = falsifier_1_s4_geometric_factor(measured_factor=Fraction(3, 2))
        assert r["status"] == "FALSIFIED"

    def test_F2_pending_by_default(self):
        from grut.derivation.minus_100.falsifiers import falsifier_2_tau_0_consistency
        r = falsifier_2_tau_0_consistency()
        assert r["status"] == "PENDING"

    def test_F2_passes_for_close_tau_0(self):
        from grut.derivation.minus_100.falsifiers import falsifier_2_tau_0_consistency
        r = falsifier_2_tau_0_consistency(measured_tau_0_myr=42.5)   # ~1.4% off
        assert r["status"] == "PASSED"

    def test_F2_falsified_for_distant_tau_0(self):
        from grut.derivation.minus_100.falsifiers import falsifier_2_tau_0_consistency
        r = falsifier_2_tau_0_consistency(measured_tau_0_myr=10.0)   # 76% off
        assert r["status"] == "FALSIFIED"

    def test_F3_pending_by_default(self):
        from grut.derivation.minus_100.falsifiers import falsifier_3_w_of_z_deviations
        r = falsifier_3_w_of_z_deviations()
        assert r["status"] == "PENDING"

    def test_F3_falsified_for_null_w_of_z(self):
        from grut.derivation.minus_100.falsifiers import falsifier_3_w_of_z_deviations
        # DESI finds w consistent with −1 at high precision
        r = falsifier_3_w_of_z_deviations(
            measured_delta_w_vs_minus1={"z": 0.5, "delta_w": 0.001, "sigma": 0.3}
        )
        assert "FALSIFIED" in r["status"]

    def test_summary_reports_three_falsifiers(self):
        from grut.derivation.minus_100.falsifiers import falsification_status
        r = falsification_status()
        for key in ["F1", "F2", "F3"]:
            assert key in r


class TestHInfFrictionCalibration:
    """The calibration fix: engine strings are reviewer-neutral."""

    def test_drive_meaning_is_factual_not_evocative(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        # Contains the technical term "conformal-mode coefficient", not
        # evocative language like "screaming outward" or "wants to explode"
        drive_text = r["drive_meaning"].lower()
        assert "conformal-mode" in drive_text or "conformal mode" in drive_text
        # No rhetoric leaks
        for forbidden in ("screaming", "wants to explode", "blow up"):
            assert forbidden not in drive_text

    def test_standard_comparison_cites_ghp_1978(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        assert "GHP" in r["standard_comparison"] or "Gibbons-Hawking" in r["standard_comparison"]

    def test_friction_meaning_is_technical(self):
        from grut.foundation.anomaly import h_inf_drive_over_friction
        r = h_inf_drive_over_friction(1.322e15)
        f = r["friction_meaning"].lower()
        # Mentions the concrete technical elements
        assert "viscoelastic" in f or "constitutive" in f
        assert "noise-kernel" in f or "memory kernel" in f.replace("memory-kernel", "memory kernel") or "dissipative" in f
