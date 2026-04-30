"""Tests for the appendix renderers (D, E, F).

These pin the discipline pattern: each appendix is a function of the
registry + dependencies module, regenerable on demand, and structurally
consistent with the codebase state.
"""

from __future__ import annotations

import re

import pytest

from grut.toe.dependencies import roots
from grut.toe.registry import REGISTRY, by_id
from grut.toe.render_appendices import (
    render_all_appendices,
    render_appendix_d_derivation_index,
    render_appendix_e_claim_registry,
    render_appendix_f_dependency_graph,
)


# ─────────────────────────────────────────────────────────────────────
# Appendix D — Derivation Index
# ─────────────────────────────────────────────────────────────────────

class TestAppendixDDerivationIndex:
    def test_renders_to_string(self):
        out = render_appendix_d_derivation_index()
        assert isinstance(out, str)
        assert len(out) > 500

    def test_has_title(self):
        out = render_appendix_d_derivation_index()
        assert "Appendix D" in out
        assert "Derivation Index" in out

    def test_states_auto_generated(self):
        out = render_appendix_d_derivation_index()
        assert "Auto-generated" in out
        assert "registry.py" in out

    def test_includes_all_computed_claims(self):
        """Every tier='computed' claim appears as a backticked ID."""
        out = render_appendix_d_derivation_index()
        for c in REGISTRY:
            if c.tier == "computed":
                assert f"`{c.id}`" in out, (
                    f"Computed claim {c.id} missing from Appendix D"
                )

    def test_includes_all_anchored_claims(self):
        """Every tier='anchored' claim appears as a backticked ID."""
        out = render_appendix_d_derivation_index()
        for c in REGISTRY:
            if c.tier == "anchored":
                assert f"`{c.id}`" in out, (
                    f"Anchored claim {c.id} missing from Appendix D"
                )

    def test_excludes_open_negatives(self):
        """Open negatives have their own home in Chapter 12; not as
        primary entries in D. (They may still appear in `upstream:`
        dep lists of computed claims that depend on them — that's the
        dependency graph correctly showing the gate.)"""
        out = render_appendix_d_derivation_index()
        for c in REGISTRY:
            if c.tier == "open_negative":
                bullet_pattern = f"- **`{c.id}`**"
                assert bullet_pattern not in out, (
                    f"Open negative {c.id} should not have a primary "
                    f"bullet entry in Appendix D"
                )

    def test_excludes_conjectural_claims(self):
        """Conjectural claims are framing-tier, not derivations."""
        out = render_appendix_d_derivation_index()
        for c in REGISTRY:
            if c.tier == "conjectural":
                # Should NOT appear as primary entry
                # (May appear in deps lists of other claims, so we look
                # for the leading-bullet `- **\`id\`**` pattern)
                bullet_pattern = f"- **`{c.id}`**"
                assert bullet_pattern not in out

    def test_excludes_meta_claims(self):
        """Meta claims describe infrastructure, not derivations."""
        out = render_appendix_d_derivation_index()
        for c in REGISTRY:
            if c.tier == "meta":
                bullet_pattern = f"- **`{c.id}`**"
                assert bullet_pattern not in out

    def test_groups_by_chapter(self):
        """Output has chapter section headers in numeric order."""
        out = render_appendix_d_derivation_index()
        chapter_headers = re.findall(r"^## Chapter (\d+) — ", out, re.MULTILINE)
        chapter_nums = [int(c) for c in chapter_headers]
        assert chapter_nums == sorted(chapter_nums)

    def test_coverage_count_matches_registry(self):
        """The 'Coverage' line states the right number of derivations."""
        out = render_appendix_d_derivation_index()
        match = re.search(r"\*\*Coverage:\*\* (\d+) derivations", out)
        assert match is not None
        rendered_count = int(match.group(1))
        expected = sum(
            1 for c in REGISTRY if c.tier in ("computed", "anchored")
        )
        assert rendered_count == expected


# ─────────────────────────────────────────────────────────────────────
# Appendix E — Full Claim Registry
# ─────────────────────────────────────────────────────────────────────

class TestAppendixEClaimRegistry:
    def test_renders_to_string(self):
        out = render_appendix_e_claim_registry()
        assert isinstance(out, str)

    def test_has_title(self):
        out = render_appendix_e_claim_registry()
        assert "Appendix E" in out
        assert "Claim Registry" in out

    def test_total_count_matches_registry(self):
        out = render_appendix_e_claim_registry()
        match = re.search(r"\*\*Total: (\d+) claims\*\*", out)
        assert match is not None
        assert int(match.group(1)) == len(REGISTRY)

    def test_every_claim_appears(self):
        """All 74 claims appear in the table."""
        out = render_appendix_e_claim_registry()
        for c in REGISTRY:
            assert f"`{c.id}`" in out, (
                f"Claim {c.id} missing from Appendix E"
            )

    def test_table_has_pipe_columns(self):
        """Output is a proper Markdown pipe table."""
        out = render_appendix_e_claim_registry()
        assert "| Ch | Claim ID |" in out
        # Every claim row should be a pipe row starting with chapter
        n_pipe_rows = sum(
            1 for line in out.splitlines()
            if re.match(r"^\| \d+ \| `", line)
        )
        assert n_pipe_rows == len(REGISTRY)

    def test_pipe_chars_in_statements_escaped(self):
        """Statements with pipes don't break the table."""
        out = render_appendix_e_claim_registry()
        # No row should have an unescaped pipe in the statement column
        # (Markdown table rows would break — counting columns per row)
        for line in out.splitlines():
            if re.match(r"^\| \d+ \| `", line):
                # Each row should have exactly 7 pipe chars (6 columns)
                # — escaped pipes (\|) don't count
                escaped = line.replace(r"\|", "")
                pipe_count = escaped.count("|")
                assert pipe_count == 7, (
                    f"Row has {pipe_count} unescaped pipes (expected 7): "
                    f"{line[:80]}..."
                )


# ─────────────────────────────────────────────────────────────────────
# Appendix F — Dependency Graph
# ─────────────────────────────────────────────────────────────────────

class TestAppendixFDependencyGraph:
    def test_renders_to_string(self):
        out = render_appendix_f_dependency_graph()
        assert isinstance(out, str)

    def test_has_title(self):
        out = render_appendix_f_dependency_graph()
        assert "Appendix F" in out
        assert "Dependency Graph" in out

    def test_has_all_subsections(self):
        out = render_appendix_f_dependency_graph()
        for section in ("F.1", "F.2", "F.3", "F.4"):
            assert section in out

    def test_summary_metrics_match_codebase(self):
        """The graph summary table reports the live registry size."""
        out = render_appendix_f_dependency_graph()
        match = re.search(r"Total claims \(nodes\) \| (\d+)", out)
        assert match is not None
        assert int(match.group(1)) == len(REGISTRY)

    def test_lists_all_roots(self):
        """Every root claim appears in the F.2 table."""
        out = render_appendix_f_dependency_graph()
        for c in roots():
            assert f"`{c.id}`" in out, f"Root {c.id} missing from Appendix F"

    def test_top_fan_out_section_is_present(self):
        out = render_appendix_f_dependency_graph()
        assert "Top 10 claims by downstream fan-out" in out
        # Highest fan-out claim should be ctp_action_structure (the
        # framework's central CTP action — this is structural, not just
        # a current-state pin)
        # We don't pin the specific number, but we pin that ctp_action_structure
        # appears in the top 10.
        top_section = out[out.index("F.3"):out.index("F.4")]
        assert "`ctp_action_structure`" in top_section

    def test_closure_priority_lists_all_open_negatives(self):
        """Every open_negative appears in the F.4 table."""
        out = render_appendix_f_dependency_graph()
        f4 = out[out.index("F.4"):]
        for c in REGISTRY:
            if c.tier == "open_negative":
                assert f"`{c.id}`" in f4, (
                    f"Open negative {c.id} missing from F.4"
                )

    def test_blocking_chain_renders_when_present(self):
        """If any open negative has blocked_by, F.5 surfaces it."""
        out = render_appendix_f_dependency_graph()
        # Currently tji_7_4_open_negative blocked by allen_jacobson_phase1_stub
        if "F.5" in out:
            assert "blocked by" in out


# ─────────────────────────────────────────────────────────────────────
# Combined render_all_appendices
# ─────────────────────────────────────────────────────────────────────

class TestRenderAllAppendices:
    def test_renders_all_three_appendices(self):
        out = render_all_appendices()
        assert "Appendix D" in out
        assert "Appendix E" in out
        assert "Appendix F" in out

    def test_separator_between_appendices(self):
        """Each appendix is followed by a horizontal rule before the next."""
        out = render_all_appendices()
        # At least 2 horizontal rules separating D-E and E-F
        n_rules = out.count("\n---\n")
        assert n_rules >= 2

    def test_total_length_reasonable(self):
        """Combined output is substantial (>5KB) but not absurd (<1MB)."""
        out = render_all_appendices()
        assert 5_000 < len(out) < 1_000_000


# ─────────────────────────────────────────────────────────────────────
# Cross-renderer discipline
# ─────────────────────────────────────────────────────────────────────

class TestRendererDiscipline:
    def test_appendix_d_plus_open_negatives_equals_registry_minus_framing(self):
        """Appendix D (computed+anchored) plus open negatives plus
        framing tiers should account for every registry claim. No claim
        slips through the cracks."""
        d_tiers = {"computed", "anchored"}
        framing_tiers = {"conjectural", "foundational", "meta"}
        ledger_tiers = {"open_negative"}
        all_accounted = d_tiers | framing_tiers | ledger_tiers
        for c in REGISTRY:
            assert c.tier in all_accounted, (
                f"Claim {c.id} has tier {c.tier} not covered by any "
                f"renderer category"
            )

    def test_no_renderer_emits_python_repr(self):
        """Output should be Markdown, not str(Claim) reprs."""
        for renderer in (
            render_appendix_d_derivation_index,
            render_appendix_e_claim_registry,
            render_appendix_f_dependency_graph,
        ):
            out = renderer()
            assert "Claim(id=" not in out
            assert "<Claim" not in out
