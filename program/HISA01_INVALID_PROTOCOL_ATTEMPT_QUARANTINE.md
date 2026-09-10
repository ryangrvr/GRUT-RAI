# HISA01 INVALID PROTOCOL ATTEMPT — QUARANTINED

Artifact: `HISA01_INDEPENDENT_ADJUDICATION.json` (same directory)

Status: **INVALID / PROTOCOL VIOLATION — DO NOT RECONCILE. DO NOT CITE AS A SCIENTIFIC RESULT.**

## Why it is invalid

1. **Wrong unit of adjudication.** HISA-01 is statement-level (mention → referent → type).
   The artifact adjudicated prior PAIR CLASSIFICATIONS instead
   (`prior_pair`, `prior_classification`, `SAME_CONSTRUCTION`, `DISTINCT_CONSTRUCTION`,
   `CONFLICT_IDENTIFIED`, `NOT_A_CONFLICT`), expanding 31 statements into 17 pair records.
2. **Contamination was used as input, not metadata.** The build script contained a
   hand-authored dictionary mapping previous machine classifications to new classes
   (`SAME_CONSTRUCTION → CONFLICT_IDENTIFIED`, etc.). The prior machine output therefore
   *controlled* the result instead of being quarantined as contamination metadata.
3. **Invented adjudication classes.** `CONFLICT_IDENTIFIED` / `NOT_A_CONFLICT` are not
   permitted HISA-01 output values.

The 17 "conflicts" in that artifact are **not findings**. They are artifacts of the
mapping table.

The frozen evidence package `HISA01_FROZEN_EVIDENCE_PACKAGE.json` is untouched and
remains valid. The valid replacement is
`HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION.json` (+ `_REPORT.md`), which contains
exactly one adjudication record per frozen statement (31 → 31), adjudicated only from
the frozen quote, bounded context, candidate term and provenance.
