"""Tests for grut.derived.decoherence.csl_discriminator — the
GRUT-vs-CSL isotope-pair discriminator.

The framework's m² scaling vs CSL's linear-in-mass scaling is testable
via isotope substitution. These tests pin the predicted ratios for
three canonical isotope pairs (Si, Ag, W), the structural relation
between the discriminator and the mass ratio, and the
λ-cancellation property that makes the discriminator parameter-free.
"""

import math
from pathlib import Path

import pytest

from grut.derived.decoherence.csl_discriminator import (
    CANONICAL_PAIRS,
    DiscriminatorReport,
    Isotope,
    IsotopePair,
    ISOTOPES,
    all_reports,
    csl_predicted_ratio_coherent_small_system,
    csl_predicted_ratio_linear_n,
    csl_predicted_ratio_mass_proportional,
    discriminator_report,
    grut_predicted_ratio,
    render_full_report,
    render_table,
    verify,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestIsotopeData:
    def test_seven_isotopes_present(self):
        """Si × 3, Ag × 2, W × 3."""
        assert len(ISOTOPES) >= 7

    def test_si_28_mass(self):
        """²⁸Si atomic mass ≈ 27.977 amu (IUPAC)."""
        assert abs(ISOTOPES["28Si"].mass_amu - 27.9769265) < 0.0001

    def test_ag_107_mass(self):
        assert abs(ISOTOPES["107Ag"].mass_amu - 106.905097) < 0.0001

    def test_w_184_mass(self):
        assert abs(ISOTOPES["184W"].mass_amu - 183.950932) < 0.0001

    def test_each_isotope_has_consistent_Z_and_A(self):
        for iso in ISOTOPES.values():
            assert iso.Z > 0
            assert iso.A >= iso.Z


class TestIsotopePair:
    def test_pair_requires_same_element(self):
        with pytest.raises(AssertionError):
            IsotopePair(ISOTOPES["28Si"], ISOTOPES["107Ag"])

    def test_pair_orders_light_before_heavy(self):
        with pytest.raises(AssertionError):
            # Reversed (heavy first) should fail
            IsotopePair(ISOTOPES["30Si"], ISOTOPES["28Si"])

    def test_si_pair_mass_ratio_about_1p07(self):
        pair = IsotopePair(ISOTOPES["28Si"], ISOTOPES["30Si"])
        assert abs(pair.mass_ratio - 30.0 / 28.0) < 0.001

    def test_ag_pair_mass_ratio_about_1p019(self):
        pair = IsotopePair(ISOTOPES["107Ag"], ISOTOPES["109Ag"])
        assert abs(pair.mass_ratio - 109.0 / 107.0) < 0.001


class TestGRUTPrediction:
    def test_grut_quadratic_in_mass_ratio(self):
        for pair in CANONICAL_PAIRS:
            grut = grut_predicted_ratio(pair)
            assert abs(grut - pair.mass_ratio ** 2) < 1e-12

    def test_si_grut_around_1p148(self):
        pair = IsotopePair(ISOTOPES["28Si"], ISOTOPES["30Si"])
        grut = grut_predicted_ratio(pair)
        assert 1.14 < grut < 1.15

    def test_ag_grut_around_1p038(self):
        pair = IsotopePair(ISOTOPES["107Ag"], ISOTOPES["109Ag"])
        grut = grut_predicted_ratio(pair)
        assert 1.035 < grut < 1.040

    def test_w_grut_around_1p022(self):
        pair = IsotopePair(ISOTOPES["182W"], ISOTOPES["184W"])
        grut = grut_predicted_ratio(pair)
        assert 1.020 < grut < 1.025


class TestCSLPredictions:
    def test_csl_linear_n_uses_nucleon_count(self):
        for pair in CANONICAL_PAIRS:
            csl = csl_predicted_ratio_linear_n(pair)
            assert abs(csl - pair.heavy.A / pair.light.A) < 1e-12

    def test_csl_mass_prop_uses_mass_ratio(self):
        for pair in CANONICAL_PAIRS:
            csl = csl_predicted_ratio_mass_proportional(pair)
            assert abs(csl - pair.mass_ratio) < 1e-12

    def test_csl_coherent_quadratic_in_nucleons(self):
        """Small-system regime: N²; not experimentally relevant but listed."""
        for pair in CANONICAL_PAIRS:
            csl = csl_predicted_ratio_coherent_small_system(pair)
            assert abs(csl - (pair.heavy.A / pair.light.A) ** 2) < 1e-12

    def test_csl_variants_agree_to_0p1_pct(self):
        """Standard linear-N and Adler mass-prop give nearly identical
        ratios since N ≈ m in amu."""
        for pair in CANONICAL_PAIRS:
            n = csl_predicted_ratio_linear_n(pair)
            m = csl_predicted_ratio_mass_proportional(pair)
            assert abs(n - m) / n < 0.001


class TestDiscriminator:
    def test_grut_larger_than_csl_for_all_pairs(self):
        """Heavy isotope decoheres more under GRUT than under CSL."""
        for r in all_reports():
            assert r.grut_ratio > r.csl_linear_n_ratio

    def test_si_discriminator_around_7_pct(self):
        rep = discriminator_report(
            IsotopePair(ISOTOPES["28Si"], ISOTOPES["30Si"])
        )
        assert 6.5 < rep.grut_minus_csl_linear_pct < 8.0

    def test_ag_discriminator_around_2_pct(self):
        rep = discriminator_report(
            IsotopePair(ISOTOPES["107Ag"], ISOTOPES["109Ag"])
        )
        assert 1.5 < rep.grut_minus_csl_linear_pct < 2.5

    def test_w_discriminator_around_1_pct(self):
        rep = discriminator_report(
            IsotopePair(ISOTOPES["182W"], ISOTOPES["184W"])
        )
        assert 0.8 < rep.grut_minus_csl_linear_pct < 1.5

    def test_discriminator_equals_mass_ratio_minus_1(self):
        """Structural identity: GRUT/CSL = m_ratio, so discriminator
        in % = (m_ratio - 1) × 100%."""
        for pair in CANONICAL_PAIRS:
            rep = discriminator_report(pair)
            expected_pct = (pair.mass_ratio - 1.0) * 100
            # Within 0.5 percentage points (small N-vs-m-amu approximation
            # difference)
            assert abs(rep.grut_minus_csl_linear_pct - expected_pct) < 0.5

    def test_si_largest_discriminator(self):
        """Si has the largest discriminator (~7%) — smallest precision needed."""
        reports = all_reports()
        si_pct = abs(reports[0].grut_minus_csl_linear_pct)
        ag_pct = abs(reports[1].grut_minus_csl_linear_pct)
        w_pct = abs(reports[2].grut_minus_csl_linear_pct)
        assert si_pct > ag_pct > w_pct


class TestExperimentalReach:
    def test_si_precision_under_5_pct(self):
        """Si discriminator detectable at <5% precision."""
        reports = all_reports()
        assert reports[0].discriminating_precision_required < 0.05

    def test_ag_precision_under_1p5_pct(self):
        reports = all_reports()
        assert reports[1].discriminating_precision_required < 0.015

    def test_w_precision_under_0p7_pct(self):
        reports = all_reports()
        assert reports[2].discriminating_precision_required < 0.007


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"CSL discriminator verify failures: {failed}"

    def test_returns_six_legs(self):
        assert len(verify()) == 6


class TestRender:
    def test_table_renders(self):
        out = render_table()
        assert "GRUT" in out
        assert "CSL" in out
        for r in all_reports():
            assert r.pair_name in out

    def test_full_report_includes_framing(self):
        out = render_full_report()
        # Must include the parameter-free / λ-independence framing
        assert "parameter-free" in out.lower()
        assert "λ-independent" in out.lower() or "cancels" in out.lower()

    def test_full_report_includes_experimental_program(self):
        out = render_full_report()
        assert "MAQRO" in out


class TestDocumentExists:
    def test_isotope_csl_doc_present(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_ISOTOPE_CSL_DISCRIMINATOR.md"
        assert doc.is_file()

    def test_doc_substantive(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_ISOTOPE_CSL_DISCRIMINATOR.md"
        text = doc.read_text(encoding="utf-8")
        assert len(text.splitlines()) > 30
        # All three canonical pairs should appear
        assert "30Si" in text
        assert "109Ag" in text
        assert "184W" in text


class TestHonestFraming:
    """The module should be honest about CSL parameterization variants."""

    def test_module_doc_acknowledges_lambda_dependence(self):
        from grut.derived.decoherence import csl_discriminator
        doc = csl_discriminator.__doc__ or ""
        assert "λ" in doc or "lambda" in doc.lower()

    def test_module_doc_acknowledges_csl_variants(self):
        from grut.derived.decoherence import csl_discriminator
        doc = csl_discriminator.__doc__ or ""
        # Must mention multiple CSL formulations
        assert "GRW" in doc or "Adler" in doc

    def test_module_doc_acknowledges_regime_dependence(self):
        from grut.derived.decoherence import csl_discriminator
        doc = csl_discriminator.__doc__ or ""
        # Small-system vs large-system regime
        assert "regime" in doc.lower()
