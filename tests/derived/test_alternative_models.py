"""Tests for grut.derived.decoherence.alternative_models — the F1-F6
comparison across CSL, Diósi-Penrose, Anastopoulos-Hu, Adler, GRW.

The framework's Chapter 5 claim "no tested alternative model
reproduces all six scaling laws simultaneously" is now backed by a
codified comparison rather than an unsupported assertion. The honest
caveat that AH is foundational rather than competitor is built into
the data structure.
"""

import pytest

from grut.derived.decoherence.alternative_models import (
    ALTERNATIVE_MODELS,
    ASSESSMENTS,
    AlternativeModel,
    SIX_LAWS,
    ScalingLaw,
    ScalingLawAssessment,
    assessment,
    comparison_matrix,
    model_by_id,
    models_satisfying_all_six,
    render_markdown_table,
    scores_per_model,
    verify,
)


class TestModelRegistry:
    def test_five_models_present(self):
        assert len(ALTERNATIVE_MODELS) == 5

    def test_unique_short_ids(self):
        ids = [m.short_id for m in ALTERNATIVE_MODELS]
        assert len(ids) == len(set(ids))

    def test_each_model_has_reference(self):
        for m in ALTERNATIVE_MODELS:
            assert m.reference.strip()

    def test_each_model_has_notes(self):
        for m in ALTERNATIVE_MODELS:
            assert m.notes.strip()

    def test_only_one_foundational(self):
        """AH is the only foundational entry; DP/CSL/Adler/GRW are competitors."""
        foundational = [m for m in ALTERNATIVE_MODELS if not m.is_competitor]
        assert len(foundational) == 1
        assert foundational[0].short_id == "AH"


class TestSixLaws:
    def test_six_laws_present(self):
        assert len(SIX_LAWS) == 6

    def test_law_ids_F1_through_F6(self):
        ids = [law.short_id for law in SIX_LAWS]
        assert ids == ["F1", "F2", "F3", "F4", "F5", "F6"]

    def test_each_law_has_description(self):
        for law in SIX_LAWS:
            assert law.description.strip()


class TestAssessmentCoverage:
    def test_assessment_for_every_model_law_pair(self):
        """5 models × 6 laws = 30 assessments."""
        assert len(ASSESSMENTS) == 30

    def test_no_duplicate_assessments(self):
        keys = [(a.model_id, a.law_id) for a in ASSESSMENTS]
        assert len(keys) == len(set(keys))

    def test_every_assessment_has_reasoning(self):
        for a in ASSESSMENTS:
            assert a.reasoning.strip(), (
                f"{a.model_id}/{a.law_id} has empty reasoning"
            )

    def test_every_assessment_has_valid_status(self):
        valid = {"satisfied", "partial", "fails", "n/a"}
        for a in ASSESSMENTS:
            assert a.status in valid


class TestPerModelExpectations:
    """Spot-check the canonical expected scores."""

    def test_dp_satisfies_4_of_6(self):
        s = scores_per_model()["DP"]
        assert s["satisfied"] == 4
        assert s["fails"] == 2

    def test_dp_fails_F3_and_F5(self):
        # Strict criteria — F3 (specific 689 Hz value) and F5 (native DFS)
        # are the two DP fails
        assert assessment("DP", "F3").status == "fails"
        assert assessment("DP", "F5").status == "fails"

    def test_ah_has_partials_not_fails(self):
        """AH is foundational — partial on F3/F5 because GRUT's
        contribution is the constitutive extension."""
        s = scores_per_model()["AH"]
        assert s["fails"] == 0
        assert s["partial"] == 2

    def test_csl_zero_satisfied(self):
        assert scores_per_model()["CSL"]["satisfied"] == 0

    def test_adler_one_satisfied(self):
        """Adler matches F1 (mass-proportional by design) only."""
        assert scores_per_model()["Adler"]["satisfied"] == 1
        assert assessment("Adler", "F1").status == "satisfied"

    def test_grw_zero_satisfied(self):
        assert scores_per_model()["GRW"]["satisfied"] == 0


class TestNoCompetitorAllSix:
    """The framework's load-bearing claim."""

    def test_no_competitor_satisfies_all_six(self):
        passing = models_satisfying_all_six()
        for model_id in passing:
            m = model_by_id(model_id)
            assert not m.is_competitor, (
                f"{model_id} is a competitor and satisfies all six — "
                f"falsifies the framework's Chapter 5 claim"
            )

    def test_at_most_foundational_passes_strict_criteria(self):
        """Only AH could conceivably pass; under strict criteria
        (which require AH to predict 689 Hz and DFS structure
        natively, which it doesn't), no model passes."""
        passing = models_satisfying_all_six()
        # Under STRICT criteria, even AH only has 'partial' on F3/F5,
        # so it doesn't satisfy "all six" by the strict 'satisfied'-
        # only metric. No model passes.
        assert len(passing) == 0


class TestAccessors:
    def test_model_by_id(self):
        assert model_by_id("DP").short_id == "DP"
        assert model_by_id("xyzzy") is None

    def test_assessment_lookup(self):
        a = assessment("DP", "F1")
        assert a is not None
        assert a.status == "satisfied"

    def test_assessment_lookup_unknown_returns_none(self):
        assert assessment("xyzzy", "F1") is None
        assert assessment("DP", "F99") is None

    def test_comparison_matrix_complete(self):
        m = comparison_matrix()
        for model in ALTERNATIVE_MODELS:
            assert model.short_id in m
            for law in SIX_LAWS:
                assert law.short_id in m[model.short_id]


class TestMarkdownRender:
    def test_render_returns_table(self):
        out = render_markdown_table()
        assert "F1 mass²" in out
        assert "F6 kink" in out

    def test_render_includes_all_models(self):
        out = render_markdown_table()
        for m in ALTERNATIVE_MODELS:
            assert m.name in out

    def test_render_marks_ah_as_foundational(self):
        out = render_markdown_table()
        assert "foundational" in out.lower()

    def test_render_includes_legend(self):
        out = render_markdown_table()
        assert "Legend" in out
        assert "✓" in out
        assert "✗" in out

    def test_render_includes_reading_block(self):
        out = render_markdown_table()
        assert "Reading" in out
        # Honest framing: state that no COMPETITOR satisfies all six,
        # not "no model"
        assert "COMPETITOR" in out or "competitor" in out


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Alternative-models verify failures: {failed}"

    def test_dp_is_closest_competitor(self):
        """DP is recognized as the closest classical competitor (≥4 of 6)."""
        checks = verify()
        assert checks["dp_is_closest_competitor_4_of_6"]


class TestHonestFraming:
    """Tests that pin the document's honest-framing requirements."""

    def test_dp_notes_acknowledge_kernel_match(self):
        """DP shares the G/(ℏ|x-x'|) kernel with GRUT — must be acknowledged."""
        m = model_by_id("DP")
        assert "kernel" in m.notes.lower() or "G/" in m.notes

    def test_ah_notes_state_foundational_not_competitor(self):
        m = model_by_id("AH")
        assert "FOUNDATIONAL" in m.notes or "foundational" in m.notes
        assert "not a competitor" in m.notes.lower() or "extension" in m.notes.lower()

    def test_csl_notes_acknowledge_N_squared_not_m_squared(self):
        m = model_by_id("CSL")
        assert "N" in m.notes  # nucleon-count scaling distinct from m²


class TestReproducibilityWithLiterature:
    """Spot-check that literature claims are sourced."""

    def test_dp_cites_diosi_or_penrose(self):
        m = model_by_id("DP")
        assert "Diósi" in m.reference or "Penrose" in m.reference

    def test_ah_cites_anastopoulos(self):
        m = model_by_id("AH")
        assert "Anastopoulos" in m.reference

    def test_csl_cites_pearle_or_grp(self):
        m = model_by_id("CSL")
        assert "Pearle" in m.reference or "Ghirardi" in m.reference

    def test_adler_cites_adler(self):
        m = model_by_id("Adler")
        assert "Adler" in m.reference

    def test_grw_cites_grw_paper(self):
        m = model_by_id("GRW")
        assert "Ghirardi" in m.reference and "Rimini" in m.reference
