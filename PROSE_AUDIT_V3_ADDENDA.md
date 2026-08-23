# Prose audit V3 — addenda to the owner's denominator-independence brief

*The owner's eight-phase brief is authoritative. Four additions.*

## [V3-1] There are TWO denominators, and the brief establishes only one

Phase 1 fixes the **file** denominator: which documents are in the universe. **There is a second
denominator with exactly the same defect, and Phase 2 will hit it:** the **target** denominator —
*which objects are we searching FOR?*

The v1/v2 extractors searched for node ids drawn from `claims.json` (71). But:

- **`rung1_inin_formalism` and `rung1_ontology_finite_memory` are not in `claims.json`** — Phase 3
  requires them as instrument-level objects, so the target set is no longer the register.
- **The ontology terms are not nodes at all.** `single-pole`, `finite-memory`, `responsive-medium`
  are clauses, and they are the reason Defect 2 existed.
- Aliases, short forms and historical names have no canonical list anywhere.

**Apply Phase 1's discipline to the target set as well:**

    DISCOVERED_TARGETS   = register ids + instrument-level objects + declared semantic terms + declared aliases
    SEARCHABLE_TARGETS   = those the matcher can actually match
    UNSEARCHABLE_TARGETS = those it cannot, each with a reason

    Invariant:  SEARCHABLE + UNSEARCHABLE = DISCOVERED_TARGETS

**An UNSEARCHABLE target is a first-class result, not an omission** — it says a dependency exists in
the corpus that this instrument structurally cannot see, which is exactly what Defect 2 was. Emit
the list. **A recall number computed against an unenumerated target set is the same error as a
coverage number computed against an unenumerated corpus.**

## [V3-2] A detected mutant must FAIL, not warn

Phase 5's nine mutants test **detection**. Detection into a log nobody reads is nearly as bad as
no detection — this program has five prose-drift instances establishing that warnings do not
propagate.

**Require: each mutant causes a NON-ZERO EXIT and blocks summary generation.** The pass criterion
is not "the discrepancy appears in the output" but **"the instrument refused to produce a green
summary."** Report per mutant: detected (y/n) · exit code · whether a summary was still emitted.
**A mutant that is detected but still yields a green summary is a FAILED INSTRUMENT**, same as one
that passes silently.

## [V3-3] An ambiguous exclusion must not stall Phase 1 — fail toward inclusion

Phase 1's `SCANNED + EXCLUDED = DISCOVERED` with "no silent exclusions" is right, and it can
deadlock: a file whose exclusion justification is genuinely uncertain blocks the whole audit at
Phase 1.

**Resolution rule: when an exclusion cannot be confidently justified, mark it
`UNJUSTIFIED-EXCLUSION` and COUNT IT AS SCANNED.** Fail toward inclusion. A wrongly-included file
adds noise that precision measurement will surface; a wrongly-excluded file is invisible forever and
is precisely the failure being repaired. Emit the `UNJUSTIFIED-EXCLUSION` list as its own number so
the judgement is visible rather than buried.

## [V3-4] Phase 7 must classify BEFORE looking at the incumbent

Phase 7 re-tests the current finding (ontology carries the distinctive claims; formalism carries the
bulk) and correctly says do not assume it survives. **But the incumbent number is known — 6 of 27 —
and knowing the answer invites reproducing it.**

**Compute the full-corpus classification first, write it down, and only then compare to the previous
result.** Report both, and if they differ, report the difference as a finding rather than
reconciling toward either. This is plant-and-recover applied to a re-test: **a re-test that can only
confirm the incumbent is a confirmation pipeline, not a re-test.**

Note also that the incumbent was computed over the 27 `rung1` dependents on a **28-file** corpus. The
full corpus is ~104 files. **The classification may move substantially, in either direction, and
both directions are publishable.** If the ontology's share falls, the V2 correction weakens; if it
rises, it strengthens. Neither outcome is the target.

---

## The pattern these four share, and the reason the brief is right

Three consecutive instrument failures — full-ID precision without recall, short-form recall without
corpus coverage, corpus coverage checked against itself — are one defect wearing three costumes:

> **a measurement taken against a denominator that was assumed rather than established.**

The owner's Phase 8 names it (`SELF-REFERENTIAL-GATE`). [V3-1] extends it to the target set, because
otherwise Phase 2 measures recall against an unenumerated universe of things to find, and the fourth
costume arrives on schedule.
