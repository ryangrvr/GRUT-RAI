"""Chapter 12 ledger renderer — auto-generates the Open Questions
section of the GRUT ToE document directly from the registry and the
open-question ledger.

The principle: documents drift from code unless the synchronization is
mechanical. The ledger renderer makes Chapter 12's open-questions
section a function of the codebase, not a hand-curated artifact.

Workflow:
    1. Add or update an open_negative claim in `grut/toe/registry.py`
    2. Add or update its entry in `grut/toe/ledger.py`
    3. Run `python3 -m grut.toe.render > /tmp/chapter12.md`
    4. Paste/include the rendered Markdown in the canonical ToE document

The renderer produces:
    - A summary table (one row per open negative)
    - A topologically-ordered detailed listing (each entry with
      statement, closure condition, effort, affects, blocked_by,
      last_review)
    - A dependency map showing which closures unlock which others
    - A high-fan-out summary (which open negatives, if closed, would
      strengthen the most downstream claims)

Design constraints:
    - Reads the registry and ledger; writes Markdown.
    - Pure function of codebase state — no external configuration.
    - No silent special-casing: every entry shows the same fields.
    - Claim IDs surfaced in code formatting so they're greppable.
"""

from __future__ import annotations

import io
from typing import Iterable

from grut.toe.dependencies import (
    fan_out,
    high_value_open_negatives,
)
from grut.toe.ledger import (
    LedgerEntry,
    OPEN_NEGATIVES,
    by_claim,
    closure_dependency_chain,
    coverage_report,
)
from grut.toe.registry import REGISTRY, Claim, by_id, by_tier


# ─────────────────────────────────────────────────────────────────────
# Section renderers
# ─────────────────────────────────────────────────────────────────────

def render_summary_table(entries: Iterable[LedgerEntry] | None = None) -> str:
    """Markdown table — one row per open negative, sortable by chapter."""
    if entries is None:
        entries = OPEN_NEGATIVES
    entries = list(entries)

    # Pair each entry with its registry claim for chapter / fan-out info
    rows: list[tuple[int, str, int, str, str]] = []
    for e in entries:
        c = by_id(e.claim_id)
        if c is None:
            continue
        rows.append((
            c.chapter,
            c.id,
            fan_out(c.id),
            e.closure_effort,
            ", ".join(e.affects) if e.affects else "—",
        ))
    rows.sort(key=lambda r: (r[0], -r[2], r[1]))

    out = io.StringIO()
    out.write("| Ch | Claim ID | Fan-out | Effort | Affects |\n")
    out.write("|:---|:---|---:|:---|:---|\n")
    for ch, cid, fo, eff, aff in rows:
        # Truncate long effort strings for table readability
        eff_short = eff if len(eff) <= 50 else eff[:47] + "..."
        aff_short = aff if len(aff) <= 60 else aff[:57] + "..."
        out.write(
            f"| {ch} | `{cid}` | {fo} | {eff_short} | {aff_short} |\n"
        )
    return out.getvalue()


def render_open_negative_entry(claim_id: str) -> str:
    """Render one open negative as a self-contained Markdown subsection."""
    entry = by_claim(claim_id)
    claim = by_id(claim_id)
    if entry is None or claim is None:
        return f"### {claim_id} — entry missing\n"

    out = io.StringIO()
    out.write(f"### {claim.id}\n\n")
    out.write(f"**Chapter.** {claim.chapter}\n\n")
    out.write(f"**Statement.** {claim.statement}\n\n")
    out.write(f"**Closure condition.** {entry.closure_condition}\n\n")
    out.write(f"**Closure effort.** {entry.closure_effort}\n\n")

    if entry.affects:
        out.write("**Affects (claims hardened on closure).**\n")
        for a in entry.affects:
            target = by_id(a)
            if target is not None:
                fo = fan_out(target.id)
                out.write(f"- `{a}` (Ch {target.chapter}, fan-out {fo})\n")
            else:
                out.write(f"- `{a}` *(claim not in registry)*\n")
        out.write("\n")
    else:
        out.write("**Affects.** No directly-dependent claims.\n\n")

    if entry.blocked_by:
        out.write("**Blocked by (upstream open negatives).**\n")
        for b in entry.blocked_by:
            blocker = by_claim(b)
            if blocker is not None:
                out.write(f"- `{b}` — must close before this can close\n")
            else:
                out.write(f"- `{b}` *(blocker not in ledger)*\n")
        out.write("\n")

    chain = closure_dependency_chain(claim_id)
    if chain:
        out.write("**Closure dependency chain.** ")
        chain_str = " → ".join(f"`{c}`" for c in chain)
        out.write(f"`{claim_id}` blocked through {chain_str}.\n\n")

    if claim.refs:
        out.write("**References.**\n")
        for r in claim.refs:
            out.write(f"- {r}\n")
        out.write("\n")

    if claim.tests:
        out.write("**Tests pinning the gap.**\n")
        for t in claim.tests:
            out.write(f"- `{t}`\n")
        out.write("\n")

    if entry.last_review:
        out.write(f"**Last reviewed.** {entry.last_review}\n\n")

    out.write("---\n\n")
    return out.getvalue()


def render_high_value_section() -> str:
    """Open negatives ranked by downstream fan-out — closure priority."""
    ranks = high_value_open_negatives()
    out = io.StringIO()
    out.write("### Closure-priority ranking\n\n")
    out.write(
        "Each open negative's _fan-out_ is the number of downstream "
        "claims that depend (transitively) on the gap. Closing a "
        "high-fan-out gap hardens more of the framework than closing "
        "a low-fan-out one. The list is auto-ranked from the dependency "
        "graph; this is the recommended attack order, not a wish list.\n\n"
    )
    out.write("| Rank | Fan-out | Claim ID | Effort |\n")
    out.write("|---:|---:|:---|:---|\n")
    for i, (claim, score) in enumerate(ranks, start=1):
        entry = by_claim(claim.id)
        eff = entry.closure_effort if entry else "—"
        eff_short = eff if len(eff) <= 50 else eff[:47] + "..."
        out.write(f"| {i} | {score} | `{claim.id}` | {eff_short} |\n")
    out.write("\n")
    return out.getvalue()


def render_dependency_map() -> str:
    """ASCII-art-ish map of closure dependencies between open negatives."""
    out = io.StringIO()
    out.write("### Inter-gap dependency map\n\n")
    out.write(
        "Some open negatives are blocked by others — closing the "
        "blocker is a prerequisite. The arrows below read 'closure of "
        "X requires closure of Y'.\n\n"
    )
    out.write("```\n")
    any_blocking = False
    for e in OPEN_NEGATIVES:
        if e.blocked_by:
            any_blocking = True
            for b in e.blocked_by:
                out.write(f"  {e.claim_id}\n")
                out.write(f"    └── blocked by → {b}\n")
    if not any_blocking:
        out.write("  (No inter-gap blockers — all open negatives are\n")
        out.write("   independently closable from the framework's standpoint.)\n")
    out.write("```\n\n")
    return out.getvalue()


def render_coverage_report() -> str:
    """Report any drift between the registry's open_negative claims and
    the ledger's coverage."""
    rep = coverage_report()
    out = io.StringIO()
    out.write("### Coverage check\n\n")
    if rep["coverage_complete"]:
        out.write(
            f"All {len(rep['ledger_entries'])} registry open negatives "
            f"have ledger entries. ✓\n\n"
        )
    else:
        out.write("⚠ **Drift between registry and ledger.**\n\n")
        if rep["in_registry_not_ledger"]:
            out.write("*Registry open negatives without ledger entries:*\n")
            for c in rep["in_registry_not_ledger"]:
                out.write(f"- `{c}`\n")
            out.write("\n")
        if rep["in_ledger_not_registry"]:
            out.write("*Ledger entries without registry claims:*\n")
            for c in rep["in_ledger_not_registry"]:
                out.write(f"- `{c}`\n")
            out.write("\n")
    return out.getvalue()


# ─────────────────────────────────────────────────────────────────────
# Top-level: full Chapter 12 Open Questions section
# ─────────────────────────────────────────────────────────────────────

def render_chapter_12_open_questions(
    title: str = "## Open Questions — Auto-rendered Ledger",
    preface: str | None = None,
) -> str:
    """Full Markdown section for inclusion in Chapter 12.

    Render order:
        1. Title + preface
        2. Coverage check (drift between registry and ledger)
        3. Summary table (chapter, claim ID, fan-out, effort, affects)
        4. Closure-priority ranking (by fan-out)
        5. Inter-gap dependency map
        6. Detailed entries (one Markdown subsection per open negative,
           sorted by chapter then by claim ID for stable diff-friendly
           ordering)
    """
    out = io.StringIO()

    out.write(f"{title}\n\n")

    if preface is None:
        preface = (
            "*This section is auto-generated from "
            "`grut/toe/ledger.py` and `grut/toe/registry.py`. To update, "
            "edit the ledger entry or registry claim and re-render via "
            "`python3 -m grut.toe.render`. Manual edits below this "
            "header will be overwritten on regeneration.*\n\n"
            "Each open negative below names a specific gap in the "
            "framework, with a falsifiable closure condition, a rough "
            "effort estimate, and the downstream claims that would be "
            "hardened by closure. Open negatives are not deferred "
            "promises — they are documented limits on what the "
            "framework currently predicts. A specialist reading this "
            "section should leave with a complete map of what is open, "
            "what would close each item, and what depends on each "
            "closure.\n\n"
        )
    out.write(preface)

    out.write(render_coverage_report())

    out.write("### Summary\n\n")
    out.write(render_summary_table())
    out.write("\n")

    out.write(render_high_value_section())
    out.write(render_dependency_map())

    out.write("### Detailed entries\n\n")
    # Order: by chapter, then by claim ID
    sorted_entries = sorted(
        OPEN_NEGATIVES,
        key=lambda e: (
            (by_id(e.claim_id).chapter if by_id(e.claim_id) else 99),
            e.claim_id,
        ),
    )
    for e in sorted_entries:
        out.write(render_open_negative_entry(e.claim_id))

    return out.getvalue()


# ─────────────────────────────────────────────────────────────────────
# Per-chapter claim renderer (for auto-syncing the chapter footer's
# "Registry claims:" line)
# ─────────────────────────────────────────────────────────────────────

def render_chapter_claims_footer(chapter: int) -> str:
    """One-line summary of the registry claims pinned to a given chapter.

    Output format matches the ToE document's existing convention:
        *Registry claims: claim_a (computed), claim_b (anchored), ...*
    """
    claims = [c for c in REGISTRY if c.chapter == chapter]
    claims.sort(key=lambda c: c.id)
    parts = [f"{c.id} ({c.tier})" for c in claims]
    return f"*Registry claims: {', '.join(parts)}*"


def render_chapter_open_negatives(chapter: int) -> str:
    """Markdown block listing open negatives that AFFECT a given chapter.

    Output format (paste between chapter prose and registry-claims footer):
        > **Open questions affecting this chapter:**
        > - `claim_id_a` (Ch X): one-line statement [auto-rendered from ledger]
        > - `claim_id_b` (Ch Y): ...

    Two ways an open negative can affect a chapter:
      1. The open negative IS in this chapter (claim.chapter == chapter)
      2. The open negative AFFECTS a registered claim in this chapter
         (via ledger entry's `affects` field)
    """
    chapter_claim_ids = {c.id for c in REGISTRY if c.chapter == chapter}
    relevant: list[tuple[str, str]] = []  # (claim_id, reason)

    # Open negatives in this chapter directly
    for c in REGISTRY:
        if c.tier == "open_negative" and c.chapter == chapter:
            relevant.append((c.id, "in this chapter"))

    # Open negatives that affect claims in this chapter
    for entry in OPEN_NEGATIVES:
        for affected_id in entry.affects:
            if affected_id in chapter_claim_ids:
                # Avoid double-listing if already in chapter
                if not any(r[0] == entry.claim_id for r in relevant):
                    relevant.append((
                        entry.claim_id,
                        f"affects `{affected_id}`",
                    ))
                break

    if not relevant:
        return ""

    out = io.StringIO()
    out.write("> **Open questions affecting this chapter:**\n")
    for claim_id, reason in relevant:
        c = by_id(claim_id)
        if c is None:
            out.write(f"> - `{claim_id}` — *(claim missing from registry)*\n")
            continue
        # First sentence of the statement, truncated for readability
        first_sentence = c.statement.split(". ")[0]
        if len(first_sentence) > 120:
            first_sentence = first_sentence[:117] + "..."
        out.write(
            f"> - `{claim_id}` (Ch {c.chapter}; {reason}): "
            f"{first_sentence}\n"
        )
    out.write(">\n")
    out.write(
        "> *Auto-rendered from `grut/toe/ledger.py`. "
        "Full closure conditions in Chapter 12.*\n"
    )
    return out.getvalue()


def render_chapter_full_footer(chapter: int) -> str:
    """Combined chapter footer: open-questions block + registry-claims line.

    Use this to replace ad-hoc `[OPEN]` / `Outstanding verification`
    paragraphs scattered across chapters. The output is paste-ready
    Markdown for the bottom of any chapter.
    """
    out = io.StringIO()
    open_block = render_chapter_open_negatives(chapter)
    if open_block:
        out.write(open_block)
        out.write("\n")
    out.write(render_chapter_claims_footer(chapter))
    return out.getvalue()


def render_all_chapter_footers() -> str:
    """All twelve chapters' full footers, for sync verification."""
    out = io.StringIO()
    for ch in range(1, 13):
        out.write(f"#### Chapter {ch}\n")
        out.write(render_chapter_full_footer(ch))
        out.write("\n\n")
    return out.getvalue()


if __name__ == "__main__":
    print(render_chapter_12_open_questions())
