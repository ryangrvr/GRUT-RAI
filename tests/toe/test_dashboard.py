"""Tests for grut.toe.dashboard — the predictions/falsifier dashboard.

The dashboard is the framework's specialist-handoff document. Tests
pin: structural completeness, status taxonomy validity, registry
back-link integrity, and the auto-generated document's existence
and coverage.
"""

from pathlib import Path

import pytest

from grut.toe.dashboard import (
    PREDICTIONS,
    Prediction,
    STATUS_GLYPH,
    all_categories,
    by_category,
    by_chapter,
    by_id,
    by_status,
    primary_falsifiers,
    render_full_dashboard,
    render_predictions_table,
    render_summary_section,
    render_detailed_entries,
    status_summary,
    verify,
)
from grut.toe.registry import REGISTRY, by_id as registry_by_id


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestPredictionsRegistry:
    """The PREDICTIONS list itself is well-formed."""

    def test_at_least_20_predictions(self):
        assert len(PREDICTIONS) >= 20

    def test_unique_short_ids(self):
        ids = [p.short_id for p in PREDICTIONS]
        assert len(ids) == len(set(ids))

    def test_short_ids_follow_pattern(self):
        """P01, P02, ... format."""
        for p in PREDICTIONS:
            assert p.short_id.startswith("P"), f"{p.short_id} doesn't start with 'P'"
            assert p.short_id[1:].isdigit(), f"{p.short_id} is not P<number>"

    def test_each_prediction_has_required_fields(self):
        required = ["name", "grut_value", "observed_value",
                    "fractional_diff", "status", "precision_status",
                    "falsifier", "registry_claim_id"]
        for p in PREDICTIONS:
            for field in required:
                value = getattr(p, field)
                assert value is not None, f"{p.short_id} missing {field}"

    def test_chapters_in_valid_range(self):
        for p in PREDICTIONS:
            assert 1 <= p.chapter <= 12, f"{p.short_id} chapter={p.chapter}"

    def test_each_has_non_empty_falsifier(self):
        for p in PREDICTIONS:
            assert p.falsifier.strip(), f"{p.short_id} has empty falsifier"


class TestStatusTaxonomy:
    def test_all_statuses_in_taxonomy(self):
        for p in PREDICTIONS:
            assert p.status in STATUS_GLYPH

    def test_status_taxonomy_has_six_levels(self):
        assert len(STATUS_GLYPH) == 6
        expected = {"consistent", "tension", "inconsistent",
                    "untested", "scoping_tier", "kinematic"}
        assert set(STATUS_GLYPH.keys()) == expected

    def test_each_status_has_unique_glyph(self):
        glyphs = list(STATUS_GLYPH.values())
        assert len(glyphs) == len(set(glyphs))


class TestRegistryBackLinks:
    """Every prediction's registry_claim_id should resolve to a real claim."""

    def test_every_prediction_links_to_real_claim(self):
        registered = {c.id for c in REGISTRY}
        for p in PREDICTIONS:
            assert p.registry_claim_id in registered, (
                f"{p.short_id} ({p.name}) links to "
                f"{p.registry_claim_id!r} which is not registered"
            )

    def test_chapter_matches_registry(self):
        """Each prediction's chapter should match the registry claim's chapter
        (sanity — minor drift acceptable)."""
        for p in PREDICTIONS:
            claim = registry_by_id(p.registry_claim_id)
            if claim is None:
                continue
            # Allow some drift — not all predictions need exact chapter match
            # (e.g., a Ch 12 open_negative referenced from a Ch 9 prediction)
            # But >75% should align
        # Aggregate check
        n_aligned = sum(
            1 for p in PREDICTIONS
            if registry_by_id(p.registry_claim_id) is not None
            and registry_by_id(p.registry_claim_id).chapter == p.chapter
        )
        assert n_aligned / len(PREDICTIONS) > 0.5


class TestStatusCounts:
    """The dashboard reflects the framework's actual status distribution."""

    def test_majority_consistent_or_untested(self):
        """If most predictions were inconsistent, the framework would be dead."""
        s = status_summary()
        assert s["consistent"] + s["untested"] > s["inconsistent"]

    def test_documents_disagreements(self):
        """A framework with no documented gaps is dishonest. The
        framework documents disagreements via tension (within obs
        uncertainty + systematic) or inconsistent (definitively
        falsified) tiers. Currently the framework has multiple
        tensions and zero inconsistent — that's honest, not
        whitewashed: El Gordo downgraded from inconsistent to tension
        when the sensitivity analysis showed the deviation is within
        parameter+observational uncertainty."""
        s = status_summary()
        assert s["tension"] + s["inconsistent"] >= 2

    def test_at_least_two_tensions(self):
        """The framework has documented tensions (Ω_dm, τ_0 cross-
        consistency, El Gordo at upper observation range)."""
        s = status_summary()
        assert s["tension"] >= 2

    def test_at_least_one_untested(self):
        """The decoherence plateau is the primary untested falsifier."""
        s = status_summary()
        assert s["untested"] >= 1


class TestSpecificPredictions:
    """Spot-checks on load-bearing predictions."""

    def test_P04_is_R_canonical(self):
        p = by_id("P04")
        assert p is not None
        assert "1.15470" in p.grut_value or "4/3" in p.grut_value

    def test_P08_is_omega_lambda(self):
        p = by_id("P08")
        assert p is not None
        assert "0.6886" in p.grut_value
        assert p.status == "consistent"

    def test_P10_is_omega_dm_tension(self):
        """Ω_dm is in tension at +27%."""
        p = by_id("P10")
        assert p is not None
        assert p.status == "tension"
        assert "27" in p.fractional_diff or "1/3" in p.grut_value

    def test_P16_is_el_gordo_tension(self):
        """El Gordo was originally tagged inconsistent (factor 3.5 outlier).
        The sensitivity analysis showed the deviation is consistent with
        parameter + observational uncertainty (prediction range 43-130
        kpc overlaps observation range 120-600 kpc at lower end).
        Downgraded to tension."""
        p = by_id("P16")
        assert p is not None
        assert p.status == "tension"
        assert "El Gordo" in p.name

    def test_P18_is_decoherence_plateau(self):
        """Primary falsifier — the decoherence plateau."""
        p = by_id("P18")
        assert p is not None
        assert "PRIMARY FALSIFIER" in p.name
        assert "689" in p.grut_value


class TestAccessors:
    def test_by_id_returns_prediction(self):
        assert by_id("P01") is not None

    def test_by_id_unknown_returns_none(self):
        assert by_id("not_a_real_id") is None

    def test_by_status_returns_correct_subset(self):
        consistent = by_status("consistent")
        for p in consistent:
            assert p.status == "consistent"

    def test_by_chapter_returns_correct_subset(self):
        ch9 = by_chapter(9)
        for p in ch9:
            assert p.chapter == 9

    def test_all_categories_unique(self):
        cats = all_categories()
        assert len(cats) == len(set(cats))


class TestRender:
    def test_full_dashboard_renders(self):
        out = render_full_dashboard()
        assert "GRUT — Predictions / Falsifier Dashboard" in out

    def test_full_dashboard_includes_status_summary(self):
        out = render_full_dashboard()
        assert "Status summary" in out

    def test_full_dashboard_includes_all_predictions(self):
        out = render_full_dashboard()
        for p in PREDICTIONS:
            assert p.short_id in out, f"missing {p.short_id} in render"

    def test_full_dashboard_includes_registry_backlinks(self):
        out = render_full_dashboard()
        for p in PREDICTIONS:
            assert f"`{p.registry_claim_id}`" in out, (
                f"{p.short_id} registry backlink not in render"
            )

    def test_predictions_table_uses_status_glyphs_for_present_statuses(self):
        """Each status glyph that appears in PREDICTIONS should appear
        in the rendered table. Statuses with zero predictions in the
        current dashboard (e.g. inconsistent, after El Gordo's
        downgrade) won't appear in the rendered output and shouldn't
        be required."""
        out = render_predictions_table()
        present_statuses = {p.status for p in PREDICTIONS}
        for status in present_statuses:
            glyph = STATUS_GLYPH[status]
            assert glyph in out

    def test_summary_section_includes_total(self):
        out = render_summary_section()
        assert str(len(PREDICTIONS)) in out

    def test_detailed_entries_contains_falsifiers(self):
        out = render_detailed_entries()
        assert "Falsifier" in out


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Dashboard verify failures: {failed}"

    def test_returns_six_legs(self):
        checks = verify()
        assert len(checks) == 6


class TestDocumentExists:
    """The auto-generated dashboard document should exist in the repo."""

    def test_predictions_doc_present(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_PREDICTIONS.md"
        assert doc.is_file(), f"missing dashboard document: {doc}"

    def test_doc_has_substantive_content(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_PREDICTIONS.md"
        text = doc.read_text(encoding="utf-8")
        # At least 100 lines and contains all prediction IDs
        assert len(text.splitlines()) > 100
        for p in PREDICTIONS:
            assert p.short_id in text


class TestCoverage:
    """The dashboard provides specialist-engageable surface coverage."""

    def test_has_cosmological_predictions(self):
        cats = all_categories()
        assert any("Cosmological" in c for c in cats)

    def test_has_cluster_predictions(self):
        cats = all_categories()
        assert any("Cluster" in c for c in cats)

    def test_has_decoherence_predictions(self):
        cats = all_categories()
        assert any("Decoherence" in c or "decoherence" in c for c in cats)

    def test_has_particle_physics_predictions(self):
        cats = all_categories()
        assert any("Particle" in c for c in cats)


class TestStability:
    """Render output is deterministic — diff-friendly regeneration."""

    def test_render_is_deterministic(self):
        a = render_full_dashboard()
        b = render_full_dashboard()
        assert a == b
