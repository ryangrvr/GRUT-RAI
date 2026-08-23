# Prose-instrument correction — two distinct defects

> Corrects `provenance/prose_extractor.py`'s reported result. The extractor and its output are left
> untouched as immutable history. **NOTHING BANKED**; `claims.json` untouched; `validate.py` PASS.
>
> **These are TWO defects, not one, and conflating them would produce the wrong repair.**
> Defect 1 is a tuning failure and is fixable in the extractor. Defect 2 is a schema limitation and
> is not fixable in any extractor.

---

## DEFECT 1 — the instrument optimised PRECISION before establishing RECALL

**Reported:** *"0 substring collisions (full-id word-boundary matching per [A-2])"* and 46 live
prose edges.

**The zero-collision result is TRUE and stays.** It is relabelled: **a precision diagnostic, not a
coverage diagnostic.** Full-ID matching is the high-confidence pass and it should not be weakened.

**What it cannot see.** This corpus refers to claims by short form, counted across 97 prose files:

| form | occurrences |
|---|---|
| `rung3` | 201 |
| `rung1` | 68 |
| `rung7` | 56 |
| `rung 3` | 41 |
| `rung4` | 23 |
| `rung 7` | 11 |
| `rung9` | 2 |

**~400 short-form references, none visible to full-ID matching.** For calibration, full-ID
occurrences across the same corpus total 1051, and the V1 digest estimated prose carries ~0.78x the
graph's node-to-node structure (56 references against 72 edges). The extractor returned **46** —
*fewer* — while the short-form count says the true figure is materially higher. **46 is a severe
undercount and the load-bearing map must not consume it as coverage.**

**Provenance of this defect, recorded because it matters:** addendum [A-2] told the builder that
false positives were the dominant risk and did not fence the opposite direction. The builder
eliminated false positives exactly as instructed and the error swung to false negatives. **The
instruction caused the defect.** The builder did flag its unmeasured false-positive rate honestly;
the complementary error went unflagged because nobody had asked for it.

**The repair is two-pass, not stricter and not looser:**

    full-ID pass (HIGH-CONFIDENCE)  ->  short-form/ontology pass (LOW-CONFIDENCE CANDIDATE)
        ->  sampled hand validation ON THE LOW-CONFIDENCE PASS  ->  precision AND recall, separately
        ->  emitted prose dependency map

**Hard rule: low-confidence matches NEVER enter the authoritative graph automatically.** They are
candidate edges until validated. **And precision and recall are never merged into one "accuracy"
number** — the current state measured one and reported it as though it were both.

---

## DEFECT 2 — the graph cannot represent a dependency whose object is not a node

**This is the more important one and no extractor tuning fixes it.**

`single-pole` occurs **196 times** in the corpus. It is not a node id. It is a clause inside
`rung1_inin_action`'s statement. So there is **nowhere to attach those references.**

The same holds for `finite-memory`, `responsive-medium` and `relaxing` — the exact vocabulary the
V2 correction established as carrying GRUT's distinctive novelty (`rung3_single_pole`, the `rung7`
family). **The instrument layer is structurally blind to the dependency the reality audit just
identified as the most important in the program**, and it will remain blind however the matcher is
tuned.

**Stated generally, because it is the transferable lesson:**

> A dependency graph cannot represent a dependency whose semantic object is not itself a node.

### The R1 split is now an ARCHITECTURE REQUIREMENT, established twice independently

| route | why R1 must split |
|---|---|
| **reality audit** (V2 correction) | formalism != ontology; 17 of 27 dependents are formalism-only while 6 are ontology-dependent, and the six carry the novelty |
| **dependency instrumentation** (this file) | the ontology is invisible to the graph because it has no id |

Two independent routes, one conclusion. **That converts the split from a writing cleanup into a
schema change**, and it is a prerequisite for the instrument layer being trustworthy rather than a
tidiness preference.

Proposed ids, exact form to be determined against the register schema:

    rung1_inin_formalism          the SK/FV influence action: K_R + (i/2)N, doubled fields.
                                  Borrowed and genuinely `shown` (Schwinger 1961, Keldysh 1964,
                                  Feynman-Vernon 1963, Calzetta-Hu).
    rung1_ontology_finite_memory  the gravitational vacuum IS a responsive medium with finite,
                                  single-pole memory. A STANCE -- the node's own ledger_note says
                                  "STANCE, not derivation."

**Migration constraints:** preserve provenance; no silent live-register mutation; **the delta-4
allocation is NOT proposed here** and remains an owner adjudication per [A-5]. Reassign prose
dependencies to R1-ONTOLOGY only where hand validation establishes the sentence is using the
ontology rather than generic dissipation terminology — `dissipat*` remains genuinely shared, since
K_R *is* the dissipation kernel.

---

## Also: a required output was not emitted

`REALITY_PROSE_DEPENDENCY_MAP.md` was required by the builder brief and does not exist;
`PROSE_LOAD_BEARING.json` was produced in its place. **Do not hand-create the map.** It must be
emitted from the JSON by the same emitter, per the standing numerical rule — a hand-written
dependency map is the exact artifact class that has drifted five times in this stretch.

## What stands

The extractor's mechanics are sound: retraction-awareness works (1 INACTIVE edge correctly
excluded), NEGATION edges are correctly excluded from blast radius (4), the emitter fails loudly on
duplicate ids and corpus mismatch, and the builder declined to claim the audit complete because the
tools exist. **The 65 UNRESOLVED-BLOCKED stand.** Do not re-run the 65-node adjudication until the
dependency instrumentation is trustworthy.

## Standing

**Thirteenth defect in this stretch; still zero physics errors.** This one is the most instructive:
an instrument that eliminated one error class while silently creating its complement, because the
instruction named only one direction. **Both metrics, always, from here** — a repair that reports
only the error it was asked to fix is indistinguishable from a repair that works.
