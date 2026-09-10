#!/usr/bin/env python3
"""
HISA-01 — EVIDENCE CONTAINMENT AUDITOR (reusable mechanical gate).

Citation/containment audit ONLY. Does not adjudicate referents, does not
repair evidence, does not consult external sources.

Inputs (treated as immutable):
    program/HISA01_FROZEN_EVIDENCE_PACKAGE.json
    program/HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION.json

Outputs:
    program/HISA01_EVIDENCE_CONTAINMENT_AUDIT.json
    program/HISA01_EVIDENCE_CONTAINMENT_AUDIT.md

Core rule: a quote cited as exact_source_line must be an exact substring of
the frozen exact_source_line for the cited statement (byte/string containment,
no normalization applied in the primary test). A quote cited as
bounded_context_window must be an exact substring of the frozen per-term
context window for that candidate term.

No cross-line concatenation, paraphrase, fuzzy matching, quote completion,
or reconstruction of any kind is permitted. A quote that exists elsewhere in
the package (another line, another statement, another context window) does
NOT validate the citation.
"""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROG = ROOT / "program"
FROZEN = PROG / "HISA01_FROZEN_EVIDENCE_PACKAGE.json"
ADJUD = PROG / "HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION.json"
OUT_JSON = PROG / "HISA01_EVIDENCE_CONTAINMENT_AUDIT.json"
OUT_MD = PROG / "HISA01_EVIDENCE_CONTAINMENT_AUDIT.md"

# ---------------------------------------------------------------- utilities

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_quote(ref):
    """Extract the quoted citation text from an evidence_reference string.

    Returns (quote_or_None, kind_or_None). kind is 'exact_source_line' or
    'bounded_context_window'. No normalization of the quote is performed.
    """
    s = ref.strip()
    m = re.match(
        r"(exact_source_line|bounded_context_window)"   # scope tag
        r"(?:\s*\(([^)]*)\))?\s*:",                     # optional (field) qualifier
        s)
    if not m:
        return None, None
    kind = m.group(1)
    field = (m.group(2) or "").strip().strip("'")
    rest = s[m.end():]
    q = re.search(r"'(.*)'|\"(.*)\"", rest, re.S)
    if not q:
        return None, kind
    return (q.group(1) if q.group(1) is not None else q.group(2)), kind


def contains(hay, needle):
    """Exact substring test. No normalization, no fuzz."""
    return isinstance(needle, str) and needle != "" and needle in hay


def fragment_check(quote, hay):
    """DIAGNOSTIC ONLY — never upgrades a classification.

    Splits a quote on ellipsis joins ('...', '…') and reports whether every
    fragment is individually contained in the frozen string. A quote whose
    fragments are individually present but which fails whole-quote containment
    is an ellipsis-reconstruction / cross-boundary assembly; per protocol it
    FAILS.
    """
    if hay is None:
        return None
    frags = [f.strip() for f in re.split(r"\.\.\.|…", quote) if f.strip()]
    if len(frags) <= 1:
        return None
    return {
        "quote_split_on_ellipsis": True,
        "all_fragments_individually_contained": all(
            contains(hay, f) for f in frags),
        "note": ("quote is an ellipsis-joined assembly of fragments from the "
                 "frozen string; reconstruction across boundaries is not "
                 "permitted — classification remains FAIL"),
    }


def markdown_strip_check(quote, hay):
    """DIAGNOSTIC ONLY. Tests whether the quote matches the frozen string
    once markdown emphasis markers ('**') are stripped from the frozen side.
    This is NOT a permitted normalization; it only documents that the sole
    difference is stripped markup."""
    if hay is None:
        return None
    stripped = hay.replace("**", "")
    if quote in stripped and quote not in hay:
        return {"quote_matches_after_stripping_markdown_emphasis": True,
                "note": "only difference is stripped '**' markup; punctuation "
                        "normalization is not permitted — classification "
                        "remains FAIL"}
    return None


# ---------------------------------------------------------------- main audit

def main():
    h_frozen_before, h_adjud_before = sha256(FROZEN), sha256(ADJUD)
    frozen = json.loads(FROZEN.read_text())
    adjud = json.loads(ADJUD.read_text())
    stmts = frozen["statements"]
    # Global corpus of all frozen evidence strings (used ONLY to annotate
    # "exists elsewhere" — an elsewhere match never validates a citation).
    all_frozen_lines = [s["exact_source_line"] for s in stmts]
    all_frozen_ctx = [v for s in stmts for v in s["bounded_context_window"].values()]

    results = []
    counts = {
        "PASS_EXACT_SOURCE_CONTAINMENT": 0,
        "PASS_CONTEXT_CONTAINMENT": 0,
        "FAIL_SOURCE_NOT_CONTAINED": 0,
        "FAIL_CONTEXT_NOT_CONTAINED": 0,
        "FAIL_WRONG_EVIDENCE_SCOPE": 0,
        "FAIL_TERM_EVIDENCE_MISMATCH": 0,
        "FAIL_MISSING_EVIDENCE_REFERENCE": 0,
        "FAIL_MALFORMED_REFERENCE": 0,
        "REQUIRES_HUMAN_REVIEW": 0,
    }

    for rec in adjud["adjudication_records"]:
        si = rec["statement_index"]
        st = stmts[si]
        src = st["exact_source_line"]
        bcw = st["bounded_context_window"]
        # Adjacent frozen lines, used ONLY to document (not excuse) the
        # multiline-reconstruction failure mode.
        adj = ""
        if si + 1 < len(stmts):
            adj = all_frozen_lines[si] + "\n" + all_frozen_lines[si + 1]

        for adjd in rec["adjudications"]:
            term = adjd.get("candidate_term", "")
            ref = adjd.get("evidence_reference", "") or ""
            base = {
                "statement_index": si,
                "statement_id": st.get("statement_id"),
                "source_path": st.get("source_path"),
                "source_line": st.get("source_line"),
                "candidate_term": term,
                "evidence_reference": ref,
            }

            # --- missing reference -------------------------------------
            if not ref.strip():
                base.update(failure_class="FAIL_MISSING_EVIDENCE_REFERENCE",
                            explanation="No evidence_reference supplied.")
                counts["FAIL_MISSING_EVIDENCE_REFERENCE"] += 1
                results.append(base)
                continue

            quote, kind = extract_quote(ref)

            # --- malformed ----------------------------------------------
            if kind is None:
                base.update(
                    failure_class="FAIL_MALFORMED_REFERENCE",
                    explanation=(
                        "evidence_reference does not begin with an "
                        "exact_source_line: or bounded_context_window: scope "
                        "tag; no mechanically verifiable citation exists."),
                )
                counts["FAIL_MALFORMED_REFERENCE"] += 1
                results.append(base)
                continue

            if quote is None:
                # Scope tag present but no quoted evidence text at all
                # (e.g. 'bounded_context_window only', 'exact_source_line as
                # above'). If it explicitly declares the other scope than its
                # tag, it is a scope admission; either way no quote = missing
                # verifiable evidence. Classify as wrong scope when the text
                # itself declares the evidence is NOT of the tagged scope.
                declares_other = bool(re.search(
                    r"(only|absent|not in|as above)", ref, re.I))
                if declares_other:
                    base.update(
                        failure_class="FAIL_WRONG_EVIDENCE_SCOPE",
                        explanation=(
                            "Reference declares evidence lies outside the "
                            "tagged scope ('%s') and supplies no quoted "
                            "evidence text; nothing to contain-test." % ref.strip()),
                    )
                    counts["FAIL_WRONG_EVIDENCE_SCOPE"] += 1
                else:
                    base.update(
                        failure_class="FAIL_MISSING_EVIDENCE_REFERENCE",
                        explanation=(
                            "Scope tag present but no quoted evidence text "
                            "supplied."),
                    )
                    counts["FAIL_MISSING_EVIDENCE_REFERENCE"] += 1
                results.append(base)
                continue

            # --- exact_source_line citations -----------------------------
            if kind == "exact_source_line":
                if contains(src, quote):
                    # candidate-term bearing check (mechanical only)
                    if term and term.lower() not in quote.lower() and \
                       term.lower() not in src.lower():
                        base.update(
                            cited_quote=quote,
                            frozen_exact_source_line=src,
                            failure_class="FAIL_TERM_EVIDENCE_MISMATCH",
                            explanation=(
                                "Quote is contained in the cited frozen source "
                                "line, but neither the quote nor the line "
                                "mentions the candidate term '%s'." % term),
                        )
                        counts["FAIL_TERM_EVIDENCE_MISMATCH"] += 1
                    else:
                        base.update(
                            cited_quote=quote,
                            frozen_exact_source_line=src,
                            failure_class="PASS_EXACT_SOURCE_CONTAINMENT",
                            explanation=(
                                "Exact substring of the frozen exact_source_line."),
                        )
                        counts["PASS_EXACT_SOURCE_CONTAINMENT"] += 1
                    results.append(base)
                    continue

                # failure: gather diagnostic data (never upgrades the class)
                diag = {}
                for d in (fragment_check(quote, src),
                          markdown_strip_check(quote, src),
                          fragment_check(quote, bcw.get(term, ""))):
                    if d:
                        diag.update(d)
                in_ctx = contains(bcw.get(term, ""), quote)
                in_any_ctx = any(contains(c, quote) for c in bcw.values())
                in_adjacent = contains(adj, quote)
                elsewhere = contains(src, quote) is False and (
                    any(contains(l, quote) for l in all_frozen_lines)
                    or any(contains(c, quote) for c in all_frozen_ctx))

                if in_ctx or in_any_ctx:
                    cls = "FAIL_WRONG_EVIDENCE_SCOPE"
                    expl = ("Quote occurs in the frozen bounded_context_window "
                            "but NOT in the cited exact_source_line; a context "
                            "quote may not be presented as exact-line evidence.")
                elif elsewhere:
                    cls = "FAIL_SOURCE_NOT_CONTAINED"
                    expl = ("Quote does not occur in the cited frozen "
                            "exact_source_line (it occurs in some other frozen "
                            "record; that does not validate the citation).")
                else:
                    cls = "FAIL_SOURCE_NOT_CONTAINED"
                    expl = ("Quote does not occur verbatim in the cited frozen "
                            "exact_source_line.")
                if in_adjacent:
                    expl += (" NOTE: the quote spans the boundary of frozen "
                             "lines %d/%d (multiline reconstruction pattern)."
                             % (si, si + 1))
                base.update(
                    cited_quote=quote,
                    frozen_exact_source_line=src,
                    failure_class=cls,
                    explanation=expl,
                    **{"diagnostic_checks": diag} if diag else {},
                )
                if in_ctx or in_any_ctx:
                    base["frozen_context_window"] = bcw.get(term, "")
                    base["context_comparison_result"] = (
                        "quote contained in frozen context window for term "
                        "'%s'" % term if in_ctx else
                        "quote contained in a context window for a DIFFERENT term")
                counts[cls] += 1
                results.append(base)
                continue

            # --- bounded_context_window citations ------------------------
            window = bcw.get(term)
            if window is None:
                base.update(
                    cited_quote=quote,
                    frozen_context_window=None,
                    failure_class="FAIL_MALFORMED_REFERENCE",
                    explanation=(
                        "No frozen context window exists for candidate term "
                        "'%s' in this statement (available keys: %s)."
                        % (term, sorted(bcw.keys()))),
                )
                counts["FAIL_MALFORMED_REFERENCE"] += 1
                results.append(base)
                continue

            if contains(window, quote):
                if term and term.lower() not in quote.lower() and \
                   term.lower() not in window.lower():
                    base.update(
                        cited_quote=quote,
                        frozen_context_window=window,
                        failure_class="FAIL_TERM_EVIDENCE_MISMATCH",
                        explanation=(
                            "Quote is contained in the frozen context window, "
                            "but neither quote nor window mentions the "
                            "candidate term '%s'." % term),
                    )
                    counts["FAIL_TERM_EVIDENCE_MISMATCH"] += 1
                else:
                    base.update(
                        cited_quote=quote,
                        frozen_context_window=window,
                        failure_class="PASS_CONTEXT_CONTAINMENT",
                        explanation=(
                            "Exact substring of the frozen per-term context "
                            "window."),
                    )
                    counts["PASS_CONTEXT_CONTAINMENT"] += 1
                results.append(base)
                continue

            in_src = contains(src, quote)
            cls = "FAIL_CONTEXT_NOT_CONTAINED"
            expl = ("Quote does not occur verbatim in the frozen context "
                    "window for term '%s'." % term)
            if in_src:
                expl += (" The quote occurs in the exact_source_line; a "
                         "single-line quote does not satisfy a "
                         "context-window citation if it is absent from the "
                         "frozen window (scope preserved, no promotion).")
            base.update(
                cited_quote=quote,
                frozen_context_window=window,
                failure_class=cls,
                explanation=expl,
            )
            counts[cls] += 1
            results.append(base)

    # ---- integrity --------------------------------------------------------
    h_frozen_after, h_adjud_after = sha256(FROZEN), sha256(ADJUD)
    total = len(results)
    integrity = {
        "frozen_package_sha256_before": h_frozen_before,
        "frozen_package_sha256_after": h_frozen_after,
        "frozen_package_unchanged": h_frozen_before == h_frozen_after,
        "adjudication_sha256_before": h_adjud_before,
        "adjudication_sha256_after": h_adjud_after,
        "adjudication_unchanged": h_adjud_before == h_adjud_after,
        "term_occurrences_examined": total,
        "expected_term_occurrences": 62,
        "every_occurrence_classified": total == len(
            {id(r) for r in results}) and total == sum(
            sum(len(rec["adjudications"]) for rec in adjud["adjudication_records"]) for _ in [0]),
        "normalization_applied": "NONE — exact byte/string containment only",
    }
    integrity["count_matches_adjudication_entries"] = (
        total == sum(len(rec["adjudications"])
                     for rec in adjud["adjudication_records"]))

    report = {
        "audit": "HISA01_EVIDENCE_CONTAINMENT_AUDIT",
        "audit_type": "citation/containment only — no referent adjudication",
        "inputs": {
            "frozen_package": str(FROZEN),
            "adjudication": str(ADJUD),
        },
        "integrity": integrity,
        "summary": counts,
        "total": total,
        "results": results,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2))

    # ---- markdown ----------------------------------------------------------
    lines = [
        "# HISA-01 — Evidence Containment Audit",
        "",
        "Mechanical citation/containment audit. Exact byte/string containment",
        "only; no normalization, no fuzzy matching, no reconstruction.",
        "",
        "## Integrity",
        "",
        "- frozen package sha256 `%s` — %s" % (
            h_frozen_after, "UNCHANGED" if integrity["frozen_package_unchanged"] else "CHANGED"),
        "- adjudication sha256 `%s` — %s" % (
            h_adjud_after, "UNCHANGED" if integrity["adjudication_unchanged"] else "CHANGED"),
        "- term occurrences examined: **%d** (expected 62)" % total,
        "",
        "## Summary",
        "",
        "| class | count |",
        "|---|---|",
    ]
    for k, v in counts.items():
        lines.append("| %s | %d |" % (k, v))
    lines += ["", "## Failed occurrences", ""]
    for r in results:
        if r["failure_class"].startswith("PASS"):
            continue
        lines.append(
            "- **stmt %s** (`%s`) term `%s` — %s\n  quote: %s\n  %s"
            % (r["statement_index"], r.get("source_line"), r["candidate_term"],
               r["failure_class"],
               (r.get("cited_quote") or "(no quote)")[:160],
               r["explanation"]))
    OUT_MD.write_text("\n".join(lines) + "\n")

    print(json.dumps({"total": total, "summary": counts,
                      "integrity_ok": all([
                          integrity["frozen_package_unchanged"],
                          integrity["adjudication_unchanged"],
                          integrity["count_matches_adjudication_entries"]])},
                     indent=2))


if __name__ == "__main__":
    main()
