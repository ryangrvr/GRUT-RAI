# Reality Prose Audit V3

Generated from `REALITY_PROSE_AUDIT_V3.json` by `prose_audit_v3.py`. Not hand-created.

**105 audited markdown files; 104 scanned; 1 explicitly excluded; 105 = 104 + 1**

## Phase 1 — corpus denominator

| measure | value |
|---|---|
| DISCOVERED | 105 |
| SCANNED | 104 |
| EXCLUDED | 1 |
| UNJUSTIFIED-EXCLUSION | 0 |
| MISSING_EXPECTED_FILE | 1 |

`GRUT_I_II_What_Survived.md` — diagnostics only: GRUT_II_What_Survived.md, GRUT_I_What_Survived.md

## Phase 2 — target denominator [V3-1]

| measure | value |
|---|---|
| DISCOVERED_TARGETS | 100 |
| SEARCHABLE | 90 |
| UNSEARCHABLE | 10 |

- `single-pole` (semantic-term): not a node id; clause inside rung1_inin_action
- `single pole` (semantic-term): not a node id; clause inside rung1_inin_action
- `finite-memory` (semantic-term): not a node id; clause inside rung1_inin_action
- `finite memory` (semantic-term): not a node id; clause inside rung1_inin_action
- `responsive-medium` (semantic-term): not a node id; clause inside rung1_inin_action
- `responsive medium` (semantic-term): not a node id; clause inside rung1_inin_action
- `relaxing` (semantic-term): not a node id; clause inside rung1_inin_action
- `relaxor` (semantic-term): not a node id; clause inside rung1_inin_action
- `two-scale` (semantic-term): not a node id; clause inside rung1_inin_action
- `aliases (short forms)` (alias): no canonical alias-to-id mapping; LOW-confidence only

HIGH edges: 658 · LOW short refs: 515 · LOW ontology refs: 428. Never merged.

## Phase 5 — adversarial mutants [V3-2]

| mutant | detected | exit nonzero | summary blocked |
|---|---|---|---|
| remove-load-bearing-file | True | True | True |
| rename-file | True | True | True |
| add-unreferenced-file | True | True | True |
| duplicate-file | True | True | True |
| file-with-known-dependency | True | True | True |
| remove-from-scan-path | True | True | True |
| reintroduce-filename-typo | True | True | True |
| only-short-forms-file | True | True | True |
| only-ontology-refs-file | True | True | True |

## Phase 7 — classification BEFORE incumbent comparison [V3-4]

| term class | full-corpus count (104 files) |
|---|---|
| FORMALISM vocabulary | 221 |
| ONTOLOGY vocabulary | 451 |

Incumbent (28-file corpus): 6 of 27 dependents ontology-dependent. Full-corpus ontology-term count (451) exceeds formalism (221); reported as a finding — not reconciled toward either.

## Phase 8 — auditor audit

One gate flagged SELF-REFERENTIAL-GATE (adversarial harness mutates its own list; independent fact is filesystem state). All other gates anchored outside the instrument.

> This audit cannot discharge the external-validation debt. An instrument passing its own internal checks is not evidence the instrument is complete.

---

# PHASE 7 REDO (appended) — supersedes the term-frequency section above

**Status:** the 451/221 figure above is reclassified **HISTORICAL / DIAGNOSTIC ONLY** — a raw vocabulary tally, not a dependency result. The redo classifies EDGES with retraction/negation applied BEFORE counting.

## Epoch partition (filesystem birth+mod times; never filename)

| epoch | files | ONT-DEP | FORM-DEP | AMBIG | NEGATED | HIST-RETR |
|---|---|---|---|---|---|---|
| PRE_EXISTING | 64 | 181 | 93 | 44 | 4 | 5 |
| AUDIT_GENERATED | 44 | 226 | 70 | 20 | 2 | 2 |
| UNKNOWN | 0 | — | — | — | — | — |

Records: **517 total · 493 confident · 24 ambiguous**. Authoritative unit: `file + line + matched form + classification + reason` — every record traceable to source text.

## Incumbent test — REPLACED per owner instruction

The pre-existing corpus is ontology-dense at **1.95:1 by classified prose-edge count**. The V2
node-dependency structure is formalism-dominant at approximately **2.8:1**. These are different
observables: prose-edge frequency measures *discussion/attention*; node reach measures
*architectural dependence*. Neither substitutes for the other.

**Principal Phase-7 finding — the discussion-versus-dependence gap:** GRUT discusses its
distinctive ontology substantially more heavily than that ontology appears to carry the dependency
structure. The prose is ontology-dense while the verified node-dependency structure is
formalism-dominant. This is a descriptive architectural contrast, not evidence that either side is
physically correct.

**Caveat preserved:** rule-based single-line classification; semantic recall RECALL-UNMEASURABLE
until stratified hand-validation; 1.95:1 is provisional and not a hand-verified semantic
measurement.

## Caveat on this artifact's face

Rule-based single-line classification with traceable records; NOT yet a hand-validated semantic dependency graph. Precision/recall remain unmeasured until the stratified hand-check runs. RECALL-UNMEASURABLE stands for the semantic layer.
