# V3 Phase 7 — correction: a frequency count was substituted for a classification,
# and the corpus was measuring the audit

> Corrects the Phase 7 result only. Phases 1, 2, 3, 5 and 8 stand. **NOTHING BANKED**;
> `claims.json` untouched; `validate.py` PASS. **Phase 6 must not run until Phase 7 is defensible.**

---

## 1. The substitution

Phase 7 required every candidate reference to be classified as one of
`FORMALISM-DEPENDENT` / `ONTOLOGY-DEPENDENT` / `AMBIGUOUS` / `CITATION-ONLY` / `NEGATED` /
`HISTORICAL-RETRACTED`. What was returned is a **raw term-frequency tally** (ontology 451,
formalism 221).

**These answer different questions:**

| measurement | asks |
|---|---|
| term frequency | how often does this vocabulary occur? |
| edge classification | does this particular claim actually DEPEND on the formalism or the ontology? |

**Only the second answers the audit's question.** And the substitution silently discards the
retraction- and negation-awareness that Phase 2 built: the sentence *"the single-pole reading is
retracted"* increments the ontology tally while being a `NEGATED` edge. A frequency count cannot
distinguish use from mention, citation from dependence, or assertion from retraction.

**The 451/221 figure is therefore reclassified as HISTORICAL / DIAGNOSTIC ONLY. It is not a
dependency result and must not be quoted as one.**

## 2. The corpus was measuring the audit

**48% of ontology-term occurrences are in files this audit wrote in the last two days.**

| population | ontology | formalism | ratio |
|---|---|---|---|
| full corpus | 444 | 211 | **2.10** |
| audit-generated (since 2026-08-22) | 214 | 74 | |
| **pre-existing** | **230** | **137** | **1.68** |

*(counted with a hyphen/space-tolerant matcher over every `.md` outside `.git`; small differences
from the V3 figures are regex-detail, not disagreement)*

**The three most ontology-dense files in the repository are all audit-generated:**

| file | ontology terms |
|---|---|
| `provenance/CLASS_C_CONSEQUENCE_MAP_UNSEALED.md` | 86 |
| `provenance/REALITY_AUDIT_V2_CORRECTION_2026-08-23.md` | 38 |
| `provenance/CLASS_C_CONTAMINATION_AUDIT.md` | 32 |

The consequence map contributes 86 because it is a 27,000-word document *about* memory and pole
structure — evidence that we recently wrote at length on the topic, **not** evidence about GRUT's
dependency architecture. **`CLASS_C_CONTAMINATION_AUDIT.md` is itself contaminating the count.**

**This is a circular measurement, not incidental noise.** The added files are not random growth;
they are documents explicitly discussing the exact ontology being measured. The corpus grew ~40%
this week and the growth is commentary on the question.

**Provenance, recorded plainly: I wrote most of the contaminating files.** The consequence map came
from a workflow I launched; the V2 correction is mine. The checker contaminated the corpus it then
audited, and the contamination was found only by partitioning on authorship date — a check nobody
had specified.

## 3. A unit collision, recorded so progress is not misread

Three different quantities are now in play and none is comparable to the others:

    46 / 50   node -> node prose edges        (v1 / v2 extractors)
    658       node -> file edges              (V3 HIGH pass)
    451 / 221 raw vocabulary occurrences      (V3 Phase 7)

**46 -> 658 is not a 14x improvement. It is a different measurement.** Every future report must
name the unit beside the number.

## 4. What Phase 7 must do instead

1. **Partition by epoch.** `PRE_EXISTING` (content predating 2026-08-22) / `AUDIT_GENERATED` /
   `UNKNOWN` where creation time is unreliable — **mark UNKNOWN rather than guessing, and never
   infer epoch from filename.** The pre-existing corpus is the primary evidence for GRUT's
   pre-audit dependency architecture; the audit-generated corpus is evidence about the audit.
   **Never merge the populations.** A combined table may appear only as a secondary descriptive
   result and may not be the headline.
2. **Classify edges, with retraction/negation applied BEFORE counting.** Authoritative unit:
   `SOURCE FILE + LINE/RANGE + TARGET OBJECT + MATCHED FORM + CLASSIFICATION + REASON`. Every
   classification traceable to source text. Citation of Schwinger/Keldysh/Feynman-Vernon without
   use is `CITATION-ONLY`; generic `dissipation` beside `K_R` is formalism or ambiguous, never
   automatically ontology; **do not classify by proximity.**
3. **Test the incumbent rather than preserve it.** Does the *pre-existing* corpus support
   *"formalism carries the architecture, ontology carries the distinctive claims"*? **No
   reconciliation toward 6-of-27, 2.10, or 1.68.** If the ontology share falls, report it. If it
   rises, report it. If it becomes ambiguous or unsupported, say so.
4. **Stop condition:** if semantic edge classification cannot be performed reliably from the
   available text, emit `CLASSIFICATION-UNMEASURABLE`. **Do not substitute term frequency again.**

## 5. What stands, including two firsts

Phases 1, 2, 3, 5 and 8 are sound. The file denominator is now independently established
(105 = 104 + 1, discovery by walk rather than an include-list, `MISSING_EXPECTED_FILE` fired
correctly on the `GRUT_I_II_What_Survived` typo). The target denominator exists
(SEARCHABLE 90 + UNSEARCHABLE 10), and the 9 semantic terms in UNSEARCHABLE are the Defect-2 class
named honestly rather than hidden.

**Two firsts worth recording:**

- **The instrument caught itself.** The rename mutant preserved counts and passed a count-only
  gate; the builder reported that failure and repaired it with expected-membership verification
  rather than shipping 9/9. **First self-catch of this session** — every prior defect was found
  externally.
- **`SELF-REFERENTIAL-GATE` was flagged on the builder's own adversarial harness**, on the
  artifact's face rather than buried.

The denominator discipline is working. **This correction is that discipline finding a way the
result could have been manufactured by the audit itself — which is the outcome the V3 brief was
written to produce.**

## 6. Standing

Fifteenth defect; **still zero physics errors.** This one is unusual in that the checker caused a
material part of it: the contaminating documents are largely mine, and the contamination was
invisible to every gate because no gate partitioned on authorship. **A corpus that grows while it
is being measured needs an epoch axis, and nothing in the instrument had one.**
