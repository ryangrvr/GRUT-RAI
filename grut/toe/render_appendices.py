"""GRUT ToE — appendix renderers (D, E, F).

Auto-generates the three back-matter reference appendices directly from
the registry and dependency graph. Same discipline pattern as
`grut/toe/render.py` (which renders Chapter 12's open-question ledger):
the document is a function of the codebase, not a hand-curated
artifact.

Workflow:
    python3 -m grut.toe.render_appendices > /tmp/appendices.md

The renderers produce:
    Appendix D — Derivation Index
        Per-chapter walk of computed and anchored claims with statement,
        tier, dependency count, and test count. The "what's been derived"
        cross-section of the framework, organized by chapter.

    Appendix E — Full Claim Registry
        Markdown table covering all registry entries (every tier).
        Columns: ID, tier, chapter, statement (truncated), deps, tests.
        The "every claim in one place" reference.

    Appendix F — Dependency Graph
        Three sections: roots (entry points), fan-out top 10 (load-
        bearing claims), closure-priority chains (which gaps unlock
        which others). The "where to push next" reference.

Design constraints (mirrors render.py):
    - Reads registry + dependencies module; writes Markdown.
    - Pure function of codebase state.
    - No silent special-casing.
    - Claim IDs surfaced in code formatting for greppability.
"""

from __future__ import annotations

import io
from collections import defaultdict

from grut.toe.dependencies import (
    direct_dependencies,
    fan_in,
    fan_out,
    fan_out_ranking,
    graph_summary,
    high_value_open_negatives,
    leaves,
    roots,
)
from grut.toe.ledger import OPEN_NEGATIVES, by_claim
from grut.toe.registry import CHAPTER_TITLES, REGISTRY, by_id


# ─────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────

def _first_sentence(text: str, max_chars: int = 200) -> str:
    """First sentence of a statement, truncated for table-cell readability."""
    sentence = text.split(". ")[0].rstrip()
    if not sentence.endswith("."):
        sentence = sentence + "."
    if len(sentence) > max_chars:
        sentence = sentence[: max_chars - 3].rstrip() + "..."
    return sentence


def _truncate(text: str, max_chars: int) -> str:
    return text if len(text) <= max_chars else text[: max_chars - 3].rstrip() + "..."


# ─────────────────────────────────────────────────────────────────────
# Appendix D — Derivation Index
# ─────────────────────────────────────────────────────────────────────

DERIVATION_INDEX_TIERS = ("computed", "anchored")


def render_appendix_d_derivation_index(
    title: str = "# Appendix D — Derivation Index (auto-rendered)",
    preface: str | None = None,
) -> str:
    """Per-chapter walk of computed and anchored claims.

    For each tier in {computed, anchored}: ID, statement first sentence,
    tier, direct-dependency count, test count. Grouped by chapter, with
    chapter titles from `CHAPTER_TITLES`.

    Conjectural, foundational, meta, and open_negative claims are
    excluded — open negatives have their own auto-rendered home in
    Chapter 12, conjectural and foundational claims are framing-tier,
    and meta claims describe infrastructure rather than derivations.
    """
    out = io.StringIO()
    out.write(f"{title}\n\n")

    if preface is None:
        preface = (
            "*Auto-generated from `grut/toe/registry.py` via "
            "`python3 -m grut.toe.render_appendices`. To update an entry, "
            "edit the registry claim and regenerate. Manual edits below "
            "this header will be overwritten.*\n\n"
            "This index lists every framework claim at tier `computed` or "
            "`anchored` — claims whose physical content has been derived, "
            "computed, or empirically anchored, and which are pinned by "
            "passing tests. Claims at tier `open_negative` are documented "
            "separately in Chapter 12; `conjectural`, `foundational`, and "
            "`meta` claims are framing-tier and are not derivations. "
            "Entries are grouped by chapter and sorted by claim ID within "
            "each chapter.\n\n"
        )
    out.write(preface)

    by_chapter: dict[int, list] = defaultdict(list)
    for c in REGISTRY:
        if c.tier in DERIVATION_INDEX_TIERS:
            by_chapter[c.chapter].append(c)

    total = sum(len(v) for v in by_chapter.values())
    out.write(f"**Coverage:** {total} derivations across "
              f"{len(by_chapter)} chapters.\n\n")

    for chapter in sorted(by_chapter.keys()):
        title_str = CHAPTER_TITLES.get(chapter, f"Chapter {chapter}")
        claims = sorted(by_chapter[chapter], key=lambda c: c.id)

        out.write(f"## Chapter {chapter} — {title_str}\n\n")
        out.write(f"*{len(claims)} derivation"
                  f"{'s' if len(claims) != 1 else ''}.*\n\n")

        for c in claims:
            n_deps = len(c.deps)
            n_tests = len(c.tests)
            statement = _first_sentence(c.statement)
            out.write(f"- **`{c.id}`** [{c.tier}] — {statement}\n")
            meta_parts = [
                f"deps: {n_deps}",
                f"tests: {n_tests}",
                f"fan-out: {fan_out(c.id)}",
            ]
            if c.deps:
                deps_preview = ", ".join(f"`{d}`" for d in c.deps[:3])
                if len(c.deps) > 3:
                    deps_preview += f", +{len(c.deps) - 3} more"
                meta_parts.append(f"upstream: {deps_preview}")
            out.write(f"  · *{' · '.join(meta_parts)}*\n")
        out.write("\n")

    return out.getvalue()


# ─────────────────────────────────────────────────────────────────────
# Appendix E — Full Claim Registry
# ─────────────────────────────────────────────────────────────────────

def render_appendix_e_claim_registry(
    title: str = "# Appendix E — Claim Registry (auto-rendered)",
    preface: str | None = None,
) -> str:
    """Full registry as a Markdown reference table.

    Every claim, every tier. Columns: ID, tier, chapter, statement
    (truncated), deps (count), tests (count). Sorted by chapter then
    by claim ID for stable diff-friendly ordering.
    """
    out = io.StringIO()
    out.write(f"{title}\n\n")

    if preface is None:
        preface = (
            "*Auto-generated from `grut/toe/registry.py` via "
            "`python3 -m grut.toe.render_appendices`. The complete "
            "registry — every framework claim across every tier — in "
            "one reference table. Sorted by chapter then claim ID.*\n\n"
        )
    out.write(preface)

    # Tier counts for the summary header
    tier_counts: dict[str, int] = defaultdict(int)
    for c in REGISTRY:
        tier_counts[c.tier] += 1
    summary_parts = [f"{n} {t}" for t, n in sorted(tier_counts.items())]
    out.write(f"**Total: {len(REGISTRY)} claims** "
              f"({', '.join(summary_parts)}).\n\n")

    out.write("| Ch | Claim ID | Tier | Statement | Deps | Tests |\n")
    out.write("|---:|:---|:---|:---|---:|---:|\n")

    sorted_claims = sorted(REGISTRY, key=lambda c: (c.chapter, c.id))
    for c in sorted_claims:
        statement = _truncate(_first_sentence(c.statement, max_chars=300), 140)
        # Escape pipe characters in statement so Markdown table doesn't break
        statement = statement.replace("|", "\\|")
        out.write(
            f"| {c.chapter} | `{c.id}` | {c.tier} | {statement} | "
            f"{len(c.deps)} | {len(c.tests)} |\n"
        )

    out.write("\n")
    return out.getvalue()


# ─────────────────────────────────────────────────────────────────────
# Appendix F — Dependency Graph
# ─────────────────────────────────────────────────────────────────────

FAN_OUT_TOP_N = 10


def render_appendix_f_dependency_graph(
    title: str = "# Appendix F — Dependency Graph (auto-rendered)",
    preface: str | None = None,
) -> str:
    """Dependency-graph reference: roots, top fan-out, closure chains.

    Sections:
        F.1 Graph summary    (node/edge counts, max fan-out, etc.)
        F.2 Roots            (zero-dependency entry points to the framework)
        F.3 Top by fan-out   (load-bearing claims; highest downstream impact)
        F.4 Closure-priority (open-negative blockers; what unlocks what)
    """
    out = io.StringIO()
    out.write(f"{title}\n\n")

    if preface is None:
        preface = (
            "*Auto-generated from `grut/toe/registry.py` and "
            "`grut/toe/dependencies.py` via "
            "`python3 -m grut.toe.render_appendices`. The framework's "
            "dependency structure: which claims are entry points, which "
            "are load-bearing, and which open negatives block which "
            "others.*\n\n"
        )
    out.write(preface)

    # ── F.1 Graph summary ───────────────────────────────────────────
    summary = graph_summary()
    out.write("## F.1 Graph summary\n\n")
    out.write("| Metric | Value |\n")
    out.write("|:---|---:|\n")
    out.write(f"| Total claims (nodes) | {summary['n_nodes']} |\n")
    out.write(f"| Dependency edges | {summary['n_edges']} |\n")
    out.write(f"| Roots (zero deps) | {summary['n_roots']} |\n")
    out.write(f"| Leaves (no dependents) | {summary['n_leaves']} |\n")
    out.write(f"| Max downstream fan-out | {summary['max_fan_out']} |\n")
    out.write(f"| Max upstream fan-in | {summary['max_fan_in']} |\n")
    out.write("\n")

    # ── F.2 Roots ────────────────────────────────────────────────────
    out.write("## F.2 Roots — framework entry points\n\n")
    out.write(
        "Claims with zero registry dependencies. These are the seams "
        "the framework rests on: postulates, foundational definitions, "
        "and externally-anchored values that the rest of the registry "
        "builds from.\n\n"
    )
    out.write("| Claim ID | Tier | Chapter | Fan-out | First sentence |\n")
    out.write("|:---|:---|---:|---:|:---|\n")
    root_list = sorted(roots(), key=lambda c: (-fan_out(c.id), c.id))
    for c in root_list:
        first = _truncate(_first_sentence(c.statement), 100)
        first = first.replace("|", "\\|")
        out.write(
            f"| `{c.id}` | {c.tier} | {c.chapter} | "
            f"{fan_out(c.id)} | {first} |\n"
        )
    out.write("\n")

    # ── F.3 Top fan-out ─────────────────────────────────────────────
    out.write(f"## F.3 Top {FAN_OUT_TOP_N} claims by downstream fan-out\n\n")
    out.write(
        "The most load-bearing claims in the framework, ranked by the "
        "number of downstream claims that depend (transitively) on each. "
        "Failure of a high-fan-out claim cascades furthest; rigor on "
        "these is highest-leverage.\n\n"
    )
    out.write("| Rank | Fan-out | Claim ID | Tier | Chapter |\n")
    out.write("|---:|---:|:---|:---|---:|\n")
    for i, (c, score) in enumerate(fan_out_ranking()[:FAN_OUT_TOP_N], start=1):
        out.write(
            f"| {i} | {score} | `{c.id}` | {c.tier} | {c.chapter} |\n"
        )
    out.write("\n")

    # ── F.4 Closure-priority chains ─────────────────────────────────
    out.write("## F.4 Closure-priority — open-negative dependency chains\n\n")
    out.write(
        "Open negatives ranked by downstream fan-out (closure-priority "
        "order), with explicit blockers shown for each. An open negative "
        "blocked by another cannot close until the blocker closes; the "
        "chain shows the prerequisite ordering.\n\n"
    )
    out.write("| Rank | Fan-out | Open negative | Blocked by |\n")
    out.write("|---:|---:|:---|:---|\n")
    for i, (c, score) in enumerate(high_value_open_negatives(), start=1):
        ledger = by_claim(c.id)
        if ledger and ledger.blocked_by:
            blockers = ", ".join(f"`{b}`" for b in ledger.blocked_by)
        else:
            blockers = "—"
        out.write(f"| {i} | {score} | `{c.id}` | {blockers} |\n")
    out.write("\n")

    # ── F.5 Inter-gap dependency map (ASCII) ────────────────────────
    has_chains = any(
        e.blocked_by for e in OPEN_NEGATIVES
    )
    if has_chains:
        out.write("## F.5 Inter-gap blocking chains\n\n")
        out.write("```\n")
        for e in OPEN_NEGATIVES:
            for b in e.blocked_by:
                out.write(f"  {e.claim_id}\n")
                out.write(f"    └── blocked by → {b}\n")
        out.write("```\n\n")

    return out.getvalue()


# ─────────────────────────────────────────────────────────────────────
# Top-level: all three appendices in one document
# ─────────────────────────────────────────────────────────────────────

def render_all_appendices() -> str:
    """Concatenated D + E + F, ready to paste into the ToE document."""
    out = io.StringIO()
    out.write(render_appendix_d_derivation_index())
    out.write("\n---\n\n")
    out.write(render_appendix_e_claim_registry())
    out.write("\n---\n\n")
    out.write(render_appendix_f_dependency_graph())
    return out.getvalue()


if __name__ == "__main__":
    print(render_all_appendices())
