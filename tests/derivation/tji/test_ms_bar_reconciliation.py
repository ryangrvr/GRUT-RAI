"""Regression tests for TJI Phase-0.5: MS-bar scheme reconciliation.

Phase-0.5 outcome: HONEST NEGATIVE on FeynCalc 7/4 match.

The systematic enumeration of 24 scheme configurations (6 absorption
factors × {include/exclude π^D} × {±1 sign}) produces rationals
clustering around ±541/2304 + {0, ±π²/384, ±π²/192}. NONE reproduces
Fraction(7, 4).

The canonical MS-bar scheme (standard F2: (4π)^ε · Γ(1+ε)⁻¹ per loop,
squared for 2 loops) is pinned as the V7/V8 reference. It produces
-541/2304 + π²/192 at the finite ε⁰ level, with:
  - γ_E cleanly absorbed (algebraic cancellation)
  - logs grouped as pure log(4π) (linear ratio 2:1 verified)
  - log(4π) itself NOT fully absorbed (standard MS-bar leaves this
    as a renormalization-scale artifact; the "log(4π) → 0" step is
    a convention choice, not a derivation).

These tests pin the honest-negative finding exactly. If a future
Phase-0.5-redux investigates FeynCalc internals and reproduces 7/4
via a non-standard convention, these tests are updated to assert the
successful match AND the specific convention used.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp
import pytest


# ─────────────────────────────────────────────────────────────────────
# MS-bar absorption factor structure
# ─────────────────────────────────────────────────────────────────────


class TestMSBarAbsorptionFactor:
    """The absorption factor [(4π)^ε · Γ(1+ε)⁻¹]² at 2 loops, expanded
    to ε² order. Per-factor Taylor series:

        Γ(1+ε)⁻¹ = 1 + γ_E·ε + (γ_E²/2 − π²/12)·ε² + O(ε³)
        (4π)^ε   = 1 + log(4π)·ε + log(4π)²/2·ε² + O(ε³)

    After squaring and expanding, ε¹ coefficient should be
    2(γ_E + log(4π)) exactly. This is the algebraic reason MS-bar works:
    γ_E and log(4π) always appear in the combination (γ_E + log(4π))."""

    def test_eps0_coefficient_is_one(self):
        from grut.derivation.tji.flat_space import ms_bar_absorption_factor
        F = ms_bar_absorption_factor(n_loops=2, order=3)
        assert F["eps0_coeff"] == 1

    def test_eps1_coefficient_is_2_times_gamma_E_plus_log4pi(self):
        """Load-bearing: if this fails, the absorption factor is
        structurally wrong and everything downstream is suspect."""
        from grut.derivation.tji.flat_space import ms_bar_absorption_factor
        F = ms_bar_absorption_factor(n_loops=2, order=3)
        expected = 2 * sp.EulerGamma + 2 * sp.log(sp.pi) + 4 * sp.log(2)
        # log(4π) = 2·log(2) + log(π); 2·(γ_E + log(4π)) = 2γ_E + 2log(π) + 4log(2)
        assert sp.simplify(F["eps1_coeff"] - expected) == 0

    def test_eps2_coefficient_contains_expected_structure(self):
        """At ε²: (γ_E + log(4π))² − π²/6, accounting for squaring."""
        from grut.derivation.tji.flat_space import ms_bar_absorption_factor
        F = ms_bar_absorption_factor(n_loops=2, order=3)
        # Expected: 2(γ_E + log(4π))² − π²/6 (from the squaring of the
        # per-loop factor and the ζ(2)/12 coefficient in Γ(1+ε)⁻¹)
        # log(4π) = 2·log(2) + log(π), so (γ_E + log(4π))² expanded:
        L4pi = 2 * sp.log(2) + sp.log(sp.pi)
        expected = 2 * (sp.EulerGamma + L4pi) ** 2 - sp.pi ** 2 / 6
        assert sp.simplify(F["eps2_coeff"] - expected) == 0

    def test_n_loops_parameter_works(self):
        from grut.derivation.tji.flat_space import ms_bar_absorption_factor
        F1 = ms_bar_absorption_factor(n_loops=1, order=3)
        F2 = ms_bar_absorption_factor(n_loops=2, order=3)
        # ε¹ coefficient at 1 loop vs 2 loops should differ by factor 2
        assert sp.simplify(F2["eps1_coeff"] - 2 * F1["eps1_coeff"]) == 0


# ─────────────────────────────────────────────────────────────────────
# MS-bar applied to the raw Laurent
# ─────────────────────────────────────────────────────────────────────


class TestMSBarAppliedToRawLaurent:
    """Apply MS-bar absorption to the raw Laurent and verify the exact
    result structure."""

    def test_rational_part_is_minus_541_over_2304(self):
        """After MS-bar and dropping γ_E, log(2), log(π), π²: rational
        part is unchanged from raw (-541/2304). MS-bar doesn't shift
        the pure rational; it only shifts the π² coefficient."""
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        r = m["rational_part"]
        assert isinstance(r, sp.Rational)
        assert Fraction(int(r.p), int(r.q)) == Fraction(-541, 2304)

    def test_pi_squared_coefficient_is_one_over_192(self):
        """MS-bar shifts π² coefficient from 1/384 (raw) to 1/192."""
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        pi_sq = m["pi_squared_coeff"]
        assert isinstance(pi_sq, sp.Rational)
        assert Fraction(int(pi_sq.p), int(pi_sq.q)) == Fraction(1, 192)

    def test_gamma_E_is_absorbed(self):
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        assert m["transcendentals_canceled"]["EulerGamma"] is True

    def test_log_structure_is_pure_log_4pi(self):
        """The residual log terms (log(2), log(π)) must appear only in
        the combination log(4π). Structural check: linear log(2)
        coefficient = 2 × linear log(π) coefficient."""
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        assert m["transcendentals_canceled"]["log_structure_is_pure_log_4pi"] is True
        c2 = m["linear_log2_coefficient"]
        cpi = m["linear_logpi_coefficient"]
        assert sp.simplify(c2 - 2 * cpi) == 0

    def test_linear_log2_coefficient_is_minus_25_over_96(self):
        """Exact pin on the log(2) coefficient in the MS-bar result."""
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        c2 = m["linear_log2_coefficient"]
        assert sp.nsimplify(c2, rational=True) == sp.Rational(-25, 96)

    def test_linear_logpi_coefficient_is_minus_25_over_192(self):
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        cpi = m["linear_logpi_coefficient"]
        assert sp.nsimplify(cpi, rational=True) == sp.Rational(-25, 192)


# ─────────────────────────────────────────────────────────────────────
# HONEST NEGATIVE on FeynCalc 7/4 match
# ─────────────────────────────────────────────────────────────────────


class TestHonestNegativeOnFeynCalc7Over4:
    """The core Phase-0.5 finding: standard MS-bar does NOT reproduce
    the V7 §26.2.3 FeynCalc reference value of 7/4. Systematic
    enumeration of 24 scheme configurations confirms this."""

    def test_canonical_scheme_does_NOT_match_7_over_4(self):
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        assert m["matches_feyncalc_7_over_4"] is False

    def test_shift_from_raw_rational_is_zero(self):
        """MS-bar preserves the pure rational; the shift is entirely
        in the π² coefficient. 4573/2304 (the hypothetical 7/4 shift)
        is NOT what MS-bar produces."""
        from grut.derivation.tji.flat_space import finite_rational_ms_bar_scheme
        m = finite_rational_ms_bar_scheme()
        shift = m["shift_from_raw_eps0_rational"]
        assert shift == 0 or sp.simplify(shift) == 0

    def test_expected_feyncalc_shift_would_be_4573_over_2304(self):
        """Documentary: IF Phase-0.5 had reproduced 7/4, the shift
        from the raw -541/2304 would have been 4573/2304. Pinning
        this value so the correction log and the probe arithmetic
        stay consistent."""
        expected_shift = Fraction(7, 4) - Fraction(-541, 2304)
        assert expected_shift == Fraction(4573, 2304)
        assert expected_shift.numerator == 4573
        assert expected_shift.denominator == 2304


class TestSchemeEnumeration:
    """The 24-configuration systematic sweep of MS-bar-family variants.
    All configurations are exhaustively tested; none match 7/4."""

    def test_enumeration_tests_24_configurations(self):
        from grut.derivation.tji.flat_space import scheme_enumeration
        e = scheme_enumeration()
        assert e["configurations_tested"] == 24

    def test_no_configuration_matches_7_over_4(self):
        from grut.derivation.tji.flat_space import scheme_enumeration
        e = scheme_enumeration()
        assert e["any_matches_7_over_4"] is False

    def test_rationals_encountered_cluster_around_541_over_2304(self):
        """Empirical finding: the enumeration produces either
        ±541/2304 as the rational part (with π² attached or not).
        This test pins that cluster."""
        from grut.derivation.tji.flat_space import scheme_enumeration
        e = scheme_enumeration()
        rationals = set(e["rationals_encountered"])
        # Should contain -541/2304 and 541/2304 (absolute symmetry under sign flip)
        assert "-541/2304" in rationals
        assert "541/2304" in rationals

    def test_each_configuration_produces_a_rational_or_None(self):
        from grut.derivation.tji.flat_space import scheme_enumeration
        e = scheme_enumeration()
        for key, result in e["configurations"].items():
            r = result["rational_part"]
            assert r is None or isinstance(r, sp.Rational), (
                f"Config {key} has non-rational rational_part: {r} "
                f"(type {type(r)})"
            )

    def test_standard_MS_bar_config_1_matches_module_canonical(self):
        """Config 1 (piD=no, sign=+, F2_MS_bar_standard) must match
        finite_rational_ms_bar_scheme() — this is the canonical.
        Test pins the consistency."""
        from grut.derivation.tji.flat_space import (
            scheme_enumeration, finite_rational_ms_bar_scheme,
        )
        e = scheme_enumeration()
        canonical = finite_rational_ms_bar_scheme()
        # Find the F2, no piD, no sign flip config
        for key, result in e["configurations"].items():
            if "F2_MS_bar_standard" in key and "piD=no" in key and "sign=+" in key:
                assert result["rational_part"] == canonical["rational_part"]
                return
        pytest.fail("F2 standard MS-bar (no pi^D, no sign) not found in enumeration")


# ─────────────────────────────────────────────────────────────────────
# Self-test block (verify())
# ─────────────────────────────────────────────────────────────────────


class TestVerifyBlock:
    def test_verify_returns_all_true(self):
        """After Phase-0.5, every self-test check in the flat_space
        module must pass. This includes Phase-0 raw-scheme and
        Phase-0.5 MS-bar checks."""
        from grut.derivation.tji.flat_space import verify
        v = verify()
        for key, val in v.items():
            assert val is True, f"verify() check failed: {key} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Pinned expected constants
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    """The convention_declaration() must explicitly state all conventions
    under which every Fraction equality in the module is asserted.
    This is the NIS (numerical integrity statement) guardrail: if
    conventions change, the whole pipeline must be re-examined."""

    def test_convention_declaration_importable(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        assert isinstance(d, dict)

    def test_C1_states_d_equals_4_minus_2_epsilon(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        assert "4 - 2" in d["C1_dimensional_regularization"]

    def test_C2_describes_prefactor_and_gamma_ratio(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        c2 = d["C2_raw_laurent_form"]
        assert "Γ(2ε-1)" in c2 or "Gamma(2e-1)" in c2.replace("ε", "e")
        assert "(D-2)" in c2
        assert "64" in c2

    def test_C3_pins_raw_sign_pattern(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        c3 = d["C3_raw_laurent_sign_pattern"]
        assert "-1/64" in c3["eps_minus_2_coeff"]
        assert "-25/384" in c3["eps_minus_1_rational_part"]
        assert "-541/2304" in c3["eps_zero_rational_part"]
        assert "flips" in c3["eps_minus_1_rational_part"].lower() or \
               "flip" in c3["eps_minus_1_rational_part"].lower()

    def test_C3_sanity_statement_warns_on_sign_flip(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        sanity = d["C3_raw_laurent_sign_pattern"]["sanity_statement"]
        assert "+25/384" in sanity
        assert "re-examined" in sanity or "re-examine" in sanity.lower()

    def test_C4_matches_C1_convention(self):
        """MS-bar absorption factor must be Γ(1+ε)⁻¹ style (C4), which
        is the matching convention for d = 4 - 2ε (C1). Applying the
        wrong-convention absorption to the right-convention raw would
        produce garbage."""
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        c4 = d["C4_ms_bar_absorption_factor"]
        # Must reference either "Gamma(1+eps)" or "(4π)^ε" structure
        assert "Gamma(1+" in c4 or "Γ(1+ε)" in c4 or "(4π)^ε" in c4

    def test_C5_lists_absorbed_vs_physical_transcendentals(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        c5 = d["C5_transcendentals_absorbed_vs_physical"]
        assert "EulerGamma" in c5["absorbed_to_zero"]
        assert any("log(4" in item for item in c5["absorbed_to_zero"])
        assert any("pi**2" in item or "zeta(2)" in item for item in c5["kept_as_physical"])

    def test_C6_documents_feyncalc_7_over_4_is_unreconstructable(self):
        """The crucial honest documentation: 7/4 came from a specific
        FeynCalc session whose convention is unarchived and NOT
        reproducible from standard MS-bar variants."""
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        c6 = d["C6_feyncalc_reference_7_over_4_status"]
        assert "NOT documented" in c6 or "not documented" in c6.lower()
        assert "HONEST NEGATIVE" in c6 or "honest negative" in c6.lower()

    def test_raw_laurent_sign_pattern_matches_C3_declaration(self):
        """Load-bearing: the actual raw Laurent output MUST match the
        sign pattern declared in C3. If these disagree, the convention
        declaration is lying."""
        from grut.derivation.tji.flat_space import (
            pole_structure, finite_rational_raw_scheme,
        )
        p = pole_structure()
        assert p["double_pole_as_fraction"] == Fraction(-1, 64)
        assert p["single_pole_rational_fraction"] == Fraction(-25, 384)
        r = finite_rational_raw_scheme()
        assert r["python_fraction"] == Fraction(-541, 2304)

    def test_phase_0p5_status_is_HONEST_NEGATIVE(self):
        from grut.derivation.tji.flat_space import convention_declaration
        d = convention_declaration()
        assert "HONEST NEGATIVE" in d["phase_0p5_status"]


class TestPhase05PinnedConstants:
    def test_module_exposes_MS_BAR_EPSILON_ZERO_EXPECTED(self):
        from grut.derivation.tji.flat_space import MS_BAR_EPSILON_ZERO_EXPECTED
        assert MS_BAR_EPSILON_ZERO_EXPECTED == Fraction(7, 4)

    def test_feyncalc_reference_updated_to_honest_negative(self):
        from grut.derivation.tji.flat_space import feyncalc_reference
        ref = feyncalc_reference()
        status = ref["status_vs_this_module"]
        assert "Phase-0.5" in status
        assert ("HONEST NEGATIVE" in status
                or "honest-negative" in status.lower())
