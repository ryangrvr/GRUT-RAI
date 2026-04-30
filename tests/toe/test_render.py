"""Tests for grut.toe.render — Chapter 12 ledger renderer.

The renderer produces Markdown that's pasted into the canonical ToE
document. These tests pin the structural properties of the output:
every open negative appears exactly once, every claim ID is greppable,
the dependency map is correct, and the per-chapter footer matches the
registry.
"""

import pytest

from grut.toe.ledger import OPEN_NEGATIVES
from grut.toe.registry import REGISTRY, by_id, by_tier
from grut.toe.render import (
    render_all_chapter_footers,
    render_chapter_12_open_questions,
    render_chapter_claims_footer,
    render_coverage_report,
    render_dependency_map,
    render_high_value_section,
    render_open_negative_entry,
    render_summary_table,
)


class TestSummaryTable:
    def test_returns_markdown_table(self):
        s = render_summary_table()
        assert s.startswith("| Ch")
        assert "| Claim ID" in s
        assert "Fan-out" in s

    def test_lists_every_open_negative(self):
        s = render_summary_table()
        for e in OPEN_NEGATIVES:
            assert f"`{e.claim_id}`" in s, (
                f"summary table missing entry for {e.claim_id!r}"
            )

    def test_each_row_has_claim_id_in_backticks(self):
        s = render_summary_table()
        for e in OPEN_NEGATIVES:
            # Claim IDs are wrapped in backticks for grep-ability
            assert f"`{e.claim_id}`" in s


class TestOpenNegativeEntry:
    def test_renders_existing_entry(self):
        first = OPEN_NEGATIVES[0]
        s = render_open_negative_entry(first.claim_id)
        assert first.claim_id in s
        assert "**Statement.**" in s
        assert "**Closure condition.**" in s
        assert "**Closure effort.**" in s

    def test_unknown_claim_returns_missing_marker(self):
        s = render_open_negative_entry("not_a_real_claim_id")
        assert "missing" in s.lower() or "not_a_real" in s

    def test_includes_chapter_field(self):
        for e in OPEN_NEGATIVES:
            s = render_open_negative_entry(e.claim_id)
            assert "**Chapter.**" in s

    def test_includes_references_when_present(self):
        for e in OPEN_NEGATIVES:
            c = by_id(e.claim_id)
            if c is None or not c.refs:
                continue
            s = render_open_negative_entry(e.claim_id)
            assert "**References.**" in s

    def test_includes_tests_when_present(self):
        any_tested = False
        for e in OPEN_NEGATIVES:
            c = by_id(e.claim_id)
            if c is not None and c.tests:
                any_tested = True
                s = render_open_negative_entry(e.claim_id)
                assert "Tests pinning the gap" in s
        assert any_tested  # at least one open negative carries tests

    def test_includes_dependency_chain_for_blocked_entry(self):
        # tji_7_4 is blocked by allen_jacobson — chain must surface
        s = render_open_negative_entry("tji_7_4_open_negative")
        assert "Closure dependency chain" in s
        assert "allen_jacobson_phase1_stub_open_negative" in s

    def test_includes_last_review_when_present(self):
        for e in OPEN_NEGATIVES:
            if not e.last_review:
                continue
            s = render_open_negative_entry(e.claim_id)
            assert e.last_review in s


class TestHighValueSection:
    def test_table_present(self):
        s = render_high_value_section()
        assert "| Rank |" in s
        assert "Fan-out" in s

    def test_includes_all_open_negatives(self):
        s = render_high_value_section()
        for e in OPEN_NEGATIVES:
            assert f"`{e.claim_id}`" in s

    def test_ranking_is_descending_by_fan_out(self):
        from grut.toe.dependencies import high_value_open_negatives
        ranks = high_value_open_negatives()
        scores = [score for _, score in ranks]
        assert scores == sorted(scores, reverse=True)


class TestDependencyMap:
    def test_includes_blocking_relationships(self):
        s = render_dependency_map()
        # tji_7_4 is blocked_by allen_jacobson — must be in the map
        assert "tji_7_4_open_negative" in s
        assert "allen_jacobson_phase1_stub_open_negative" in s

    def test_uses_visual_blocked_by_arrow(self):
        s = render_dependency_map()
        assert "blocked by" in s


class TestCoverageReport:
    def test_coverage_passes_when_complete(self):
        s = render_coverage_report()
        # With all 8 entries present, the coverage check should pass
        assert "✓" in s or "complete" in s.lower()


class TestFullChapter12:
    def test_renders_full_section(self):
        s = render_chapter_12_open_questions()
        # Must include all major sub-sections
        assert "Open Questions" in s
        assert "Coverage check" in s
        assert "Summary" in s
        assert "Closure-priority ranking" in s
        assert "Inter-gap dependency map" in s
        assert "Detailed entries" in s

    def test_every_open_negative_appears_in_full_render(self):
        s = render_chapter_12_open_questions()
        for e in OPEN_NEGATIVES:
            # Each claim ID must appear at least once in the rendered output
            assert e.claim_id in s, f"missing {e.claim_id!r}"

    def test_auto_generated_disclaimer_present(self):
        s = render_chapter_12_open_questions()
        assert "auto-generated" in s.lower() or "auto-rendered" in s.lower()

    def test_custom_title_propagates(self):
        s = render_chapter_12_open_questions(title="## Custom Title")
        assert "## Custom Title" in s


class TestChapterFooter:
    def test_footer_format_matches_doc_convention(self):
        s = render_chapter_claims_footer(2)
        assert s.startswith("*Registry claims:")
        assert s.endswith("*")

    def test_footer_includes_all_chapter_claims(self):
        # Chapter 2 has tau_0_derivation, alpha_vac_derivation, zero_free_parameters
        s = render_chapter_claims_footer(2)
        assert "tau_0_derivation" in s
        assert "alpha_vac_derivation" in s
        assert "zero_free_parameters" in s

    def test_footer_includes_tier_for_each_claim(self):
        s = render_chapter_claims_footer(7)
        for c in REGISTRY:
            if c.chapter == 7:
                assert f"{c.id} ({c.tier})" in s

    def test_all_chapter_footers_render(self):
        s = render_all_chapter_footers()
        for ch in range(1, 13):
            assert f"#### Chapter {ch}" in s


class TestPerChapterOpenNegatives:
    """render_chapter_open_negatives surfaces gaps that affect each chapter."""

    def test_chapter_with_no_open_negatives_returns_empty(self):
        # Ch 4 (The Crystal and the Fluid) has 4 computed claims, no open
        # negatives directly in it; check whether any ledger entry affects
        # one of its claims. If none do, returns "".
        from grut.toe.render import render_chapter_open_negatives
        from grut.toe.ledger import OPEN_NEGATIVES
        from grut.toe.registry import REGISTRY

        ch4_claims = {c.id for c in REGISTRY if c.chapter == 4}
        affects_ch4 = any(
            any(a in ch4_claims for a in e.affects)
            for e in OPEN_NEGATIVES
        )
        out = render_chapter_open_negatives(4)
        if not affects_ch4:
            assert out == ""

    def test_chapter_12_lists_its_own_open_negatives(self):
        from grut.toe.render import render_chapter_open_negatives
        from grut.toe.registry import REGISTRY
        out = render_chapter_open_negatives(12)
        # Ch 12 has multiple open negatives; they should all appear
        ch12_open = [
            c for c in REGISTRY
            if c.chapter == 12 and c.tier == "open_negative"
        ]
        for c in ch12_open:
            assert c.id in out, f"missing {c.id!r} in Ch 12 open-questions render"

    def test_chapter_7_includes_tji_via_chapter(self):
        """tji_7_4 is in Ch 7 and is open_negative — must appear."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(7)
        assert "tji_7_4_open_negative" in out

    def test_chapter_6_includes_nonlinear_ladder(self):
        """nonlinear_ladder_4_of_8 is in Ch 6, open_negative."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(6)
        assert "nonlinear_ladder_4_of_8" in out

    def test_chapter_6_includes_constitutive_projection_via_affects(self):
        """The constitutive-projection open question lives in Ch 12 but
        affects gr_recovery in Ch 6 — should surface in Ch 6's render.
        Post-Correction-#23: the original heuristic open question is
        resolved at the linearized level; the curved-background extension
        is the remaining open question and is what should now surface."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(6)
        assert "phi_munu_curved_background_extension_open_question" in out

    def test_chapter_9_includes_cmb_blocker(self):
        """cmb_boltzmann_scoping is in Ch 9 (anchored). The n_g(ω)
        covariance question is in Ch 12 (open_negative) and affects
        cmb_boltzmann_scoping. Should surface in Ch 9's render."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(9)
        assert "n_g_omega_cosmological_covariance_open_question" in out

    def test_chapter_7_includes_three_routes_blocker(self):
        """The two-route physical-equivalence open question affects
        three_routes_convergence in Ch 7."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(7)
        assert "two_route_convergence_physical_equivalence_open_question" in out

    def test_render_format_uses_blockquote(self):
        """Output uses Markdown blockquote (>) for visual distinction
        from chapter prose."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(7)
        assert out.startswith(">")

    def test_render_includes_auto_rendered_disclaimer(self):
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(7)
        assert "Auto-rendered" in out or "auto-rendered" in out

    def test_no_double_listing_when_in_chapter_and_affects_chapter(self):
        """A claim in Ch 12 that affects Ch 12 itself should not list twice."""
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_open_negatives(12)
        # Each claim ID should appear at most once
        from grut.toe.registry import by_tier
        for c in by_tier("open_negative"):
            count = out.count(f"`{c.id}`")
            assert count <= 1, f"{c.id} listed {count} times in Ch 12"


class TestChapterFullFooter:
    """render_chapter_full_footer combines open-questions + registry-claims."""

    def test_includes_registry_claims_line(self):
        from grut.toe.render import render_chapter_full_footer
        out = render_chapter_full_footer(2)
        assert "*Registry claims:" in out

    def test_includes_open_questions_when_present(self):
        from grut.toe.render import render_chapter_full_footer
        out = render_chapter_full_footer(7)
        assert "Open questions affecting this chapter" in out

    def test_omits_open_questions_block_when_chapter_has_none(self):
        """Ch 8 (The Terminal Velocity) has 6 computed claims, none open
        negative directly. If no ledger entry affects them, the open-
        questions block should be omitted (just the registry-claims line)."""
        from grut.toe.render import render_chapter_full_footer
        from grut.toe.render import render_chapter_open_negatives
        out = render_chapter_full_footer(8)
        # Either has open questions or doesn't; both are valid;
        # what matters: it doesn't emit an empty blockquote header
        if not render_chapter_open_negatives(8):
            assert "Open questions affecting this chapter" not in out


class TestAllFootersRender:
    def test_all_12_chapters_renderable(self):
        """No chapter raises an error when rendering its full footer."""
        from grut.toe.render import render_chapter_full_footer
        for ch in range(1, 13):
            out = render_chapter_full_footer(ch)
            assert out  # non-empty

    def test_all_chapter_footers_aggregated(self):
        from grut.toe.render import render_all_chapter_footers
        out = render_all_chapter_footers()
        for ch in range(1, 13):
            assert f"Chapter {ch}" in out


class TestRenderStability:
    """The renderer's output should be deterministic given the same
    registry/ledger state — important for diff-friendly regeneration."""

    def test_output_is_deterministic(self):
        a = render_chapter_12_open_questions()
        b = render_chapter_12_open_questions()
        assert a == b

    def test_summary_table_deterministic(self):
        a = render_summary_table()
        b = render_summary_table()
        assert a == b


class TestRendererReadsLatestState:
    """Sanity: the renderer reflects the current registry/ledger,
    not a stale snapshot."""

    def test_el_gordo_appears_in_render(self):
        """The El Gordo open negative was added in this session.
        It must surface in the renderer output."""
        s = render_chapter_12_open_questions()
        assert "el_gordo_outlier_open_question" in s

    def test_summary_table_count_matches_ledger(self):
        s = render_summary_table()
        # Each table row has '| Ch |' prefix; count rows
        rows = [
            line for line in s.split("\n")
            if line.startswith("| ") and "Claim ID" not in line
            and "---" not in line and not line.startswith("|:---")
        ]
        # Also exclude header divider rows
        data_rows = [r for r in rows if not r.startswith("|:")]
        assert len(data_rows) == len(OPEN_NEGATIVES)
