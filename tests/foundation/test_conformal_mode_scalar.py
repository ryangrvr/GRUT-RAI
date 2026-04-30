"""Tests for grut.foundation.conformal_mode_scalar — the KS 2011 derivation
that hardens α_vac = 1/3 from anchored to computed.

The dependency graph identified `alpha_vac_derivation` as the second-highest
fan-out claim (29 downstream dependencies). These tests promote it from
anchored to computed by codifying the conditional theorem:

    Postulate: gravitational conformal mode is the IR carrier of vacuum response
    Theorem (KS 2011 / Christensen-Duff 1980):
        a/c |_{single real conformally-coupled scalar} = 1/3 EXACTLY
    Conclusion: α_vac = 1/3

The test asserts the algebra under the postulate, not the postulate itself
(the postulate remains a physical assumption — see the registry note).
"""

from fractions import Fraction
import pytest

from grut.foundation.conformal_mode_scalar import (
    A_REAL_SCALAR, C_REAL_SCALAR,
    A_WEYL_FERMION, C_WEYL_FERMION,
    A_GAUGE_BOSON, C_GAUGE_BOSON,
    a_over_c, a_over_c_real_scalar, a_over_c_sm_dirac, a_over_c_sm_majorana,
    a_total, alpha_vac_from_conformal_mode_scalar,
    alpha_vac_postulate_statement, c_total, verify,
)


class TestPerSpeciesCoefficients:
    """KS 2011 / Christensen-Duff per-species (a, c) values are exact."""

    def test_real_scalar_a_is_one(self):
        assert A_REAL_SCALAR == Fraction(1, 1)

    def test_real_scalar_c_is_three(self):
        assert C_REAL_SCALAR == Fraction(3, 1)

    def test_weyl_fermion_a_is_eleven_halves(self):
        assert A_WEYL_FERMION == Fraction(11, 2)

    def test_weyl_fermion_c_is_nine(self):
        assert C_WEYL_FERMION == Fraction(9, 1)

    def test_gauge_boson_a_is_sixty_two(self):
        assert A_GAUGE_BOSON == Fraction(62, 1)

    def test_gauge_boson_c_is_thirty_six(self):
        assert C_GAUGE_BOSON == Fraction(36, 1)


class TestKSTheorem:
    """The core theorem: a/c for a single real scalar IS 1/3 exactly."""

    def test_real_scalar_ratio_is_exactly_one_third(self):
        """KS 2011 / Christensen-Duff: a/c for single conformal scalar = 1/3."""
        assert a_over_c_real_scalar() == Fraction(1, 3)

    def test_alpha_vac_derivation_is_one_third(self):
        """Under the postulate, α_vac = 1/3 exactly (Fraction equality)."""
        assert alpha_vac_from_conformal_mode_scalar() == Fraction(1, 3)

    def test_postulate_statement_is_explicit(self):
        """The postulate that conditions the derivation is named, not hidden."""
        s = alpha_vac_postulate_statement()
        assert "Postulate" in s
        assert "conformal mode" in s
        assert "IR carrier" in s


class TestAlphaVacWiring:
    """closure_protocol.ALPHA_VAC matches the conformal-mode-scalar value."""

    def test_alpha_vac_matches_closure_protocol(self):
        """Float-level agreement with the canonical constant."""
        from grut.foundation.closure_protocol import ALPHA_VAC
        assert float(alpha_vac_from_conformal_mode_scalar()) == ALPHA_VAC

    def test_alpha_vac_matches_to_machine_precision(self):
        from grut.foundation.closure_protocol import ALPHA_VAC
        derived = float(alpha_vac_from_conformal_mode_scalar())
        assert abs(derived - ALPHA_VAC) < 1e-15

    def test_alpha_vac_matches_one_third_exactly_as_fraction(self):
        """The derived value IS the rational 1/3 — no float approximation."""
        assert alpha_vac_from_conformal_mode_scalar() == Fraction(1, 3)


class TestSMCrossChecks:
    """The same machinery reproduces Path D Majorana and Dirac values exactly."""

    def test_sm_majorana_a_total(self):
        """SM Majorana: a = 4 + 45·11/2 + 12·62 = 1991/2."""
        assert a_total(n_0=4, n_half=45, n_1=12) == Fraction(1991, 2)

    def test_sm_majorana_c_total(self):
        """SM Majorana: c = 4·3 + 45·9 + 12·36 = 849."""
        assert c_total(n_0=4, n_half=45, n_1=12) == Fraction(849)

    def test_sm_majorana_ratio_is_1991_1698(self):
        """a/c = (1991/2) / 849 = 1991/1698 ≈ 1.17256."""
        assert a_over_c_sm_majorana() == Fraction(1991, 1698)

    def test_sm_dirac_ratio_is_253_219(self):
        """SM with 3 added ν_R Weyls: (a, c) = (4·1 + 48·11/2 + 12·62, 4·3 + 48·9 + 12·36).

        a = 4 + 264 + 744 = 1012 = 4 × 253
        c = 12 + 432 + 432 = 876 = 4 × 219
        a/c = 253/219.
        """
        assert a_over_c_sm_dirac() == Fraction(253, 219)

    def test_sm_majorana_matches_closure_protocol(self):
        from grut.foundation.closure_protocol import A_OVER_C_SM_MAJORANA
        assert float(a_over_c_sm_majorana()) == A_OVER_C_SM_MAJORANA

    def test_sm_dirac_matches_closure_protocol(self):
        from grut.foundation.closure_protocol import A_OVER_C_SM_DIRAC
        assert float(a_over_c_sm_dirac()) == A_OVER_C_SM_DIRAC


class TestVerifyHarness:
    """The module's own verify() returns all-true."""

    def test_verify_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Conformal-mode-scalar verify failures: {failed}"


class TestGeneralRatioSanity:
    """The general a_over_c() function behaves as expected for edge cases."""

    def test_pure_scalar_input_gives_one_third(self):
        assert a_over_c(n_0=1, n_half=0, n_1=0) == Fraction(1, 3)

    def test_pure_weyl_input_gives_11_over_18(self):
        """11/2 / 9 = 11/18."""
        assert a_over_c(n_0=0, n_half=1, n_1=0) == Fraction(11, 18)

    def test_pure_gauge_input_gives_62_over_36(self):
        """62/36 = 31/18."""
        assert a_over_c(n_0=0, n_half=0, n_1=1) == Fraction(31, 18)

    def test_zero_content_raises(self):
        with pytest.raises(ZeroDivisionError):
            a_over_c(n_0=0, n_half=0, n_1=0)
