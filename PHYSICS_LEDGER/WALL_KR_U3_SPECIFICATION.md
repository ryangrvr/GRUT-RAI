# U3 FOUNDATIONAL SPECIFICATION AUDIT

**Date:** 2026-09-02 · **Instrument:** `wall_kr_u3_specification_audit.py` ·
**Artifact:** `WALL_KR_U3_SPECIFICATION_RESULT.json` · **Battery: 40/40, zero failures.**
**Read-only** (register sha256 identical pre/post; worktree unchanged). **No physics. No A-F
selection. U3 not solved, and not pre-answered in either direction.** W-0.

## CLASSIFICATION: **2 — FORMALIZABLE BUT UNDERSPECIFIED**

U3 is a real research problem with a strict, symmetric success test. It is **not yet a
mathematical target**, because the object it asks about is not pinned down.

## PART 1 — THE OBJECT

`tier: to-derive` · `grut_standing: open field` · `ledger_delta: 0` · `depends_on: []` ·
`domain: universality-classification` · `sources: [zurek2003, mori1965_zwanzig]` ·
`differentiator: NON-DIFFERENTIATING` · `sub_status: default-BROKEN`, fenced.

Two things are worth noticing immediately. The domain is **universality-classification**, not
"foundations" or "ontology". And U3 is declared **NON-DIFFERENTIATING** — solving it would not
by itself distinguish GRUT from anything else.

## PART 2 — WHAT "SYSTEM/BATH SPLIT" ACTUALLY MEANS HERE: **UNDERSPECIFIED**

The record supports **six** distinct notions and selects none:

| notion | what supports it |
|---|---|
| **A** Hilbert tensor factorization | `zurek2003` (einselection presumes H_S ⊗ H_B) |
| **B** algebraic projection | `mori1965_zwanzig` (a projector P defines relevant/irrelevant) |
| **C** operational / accessible observables | `zurek2003` (pointer states) |
| **D** coarse-graining partition | `mori1965_zwanzig`; and the statement's own slash |
| **E** EFT retained vs integrated-out | the Feynman-Vernon lineage |
| **F** open-system reduced dynamics | Feynman-Vernon, named in the statement |

Notion **G** (spacetime/causal partition) is **not** supported.

**Ambiguity on its face:** the statement writes *"system/bath split / coarse-graining"* — the
same slash-as-conflation defect found in the Class-C certificate. A tensor factorization and a
coarse-graining are not the same object.

## PART 3 — WELL-POSED AS A TEST, UNDERSPECIFIED AS AN OBJECT

The question is a **binary with both horns named** and a symmetric success condition:
*"only an exhibited derivation graduates this, in either direction."* The register also
records that **V2 is STRUCTURAL, not empirical** — no experiment adjudicates U3; only a
derivation does.

What the record does **not** distinguish, anywhere, is the modality: **ontological necessity
vs mathematical convenience vs calculational convenience vs operational necessity.** That is
the principal missing definition.

## PART 5 — THE BOOTSTRAP PROBLEM

**No instance found.** Nothing in the record justifies the split by the response kernel.

But the specific loop worth guarding is **named by the record itself**. U3's `sub_status`
says: *"The thermodynamics analogy (response universal-like-thermo) is the program's GOAL, NOT
a claim -- it requires an actual micro->response universality derivation."*

That identifies the exact circle: **if U3 were "solved" by arguing the split exists because it
yields universal response structure, that would use third-rung content to justify a
below-rung1 claim.** The temptation is structural, not accidental.

**The fence is already machine-watched.** It lives in `sub_status` — the field the resident
scans per CHARTER §7 — not in prose, and the record states that any change to the statement,
tier or sub_status trips the substantive-change firewall. This is the pre-registration
discipline working as designed.

## PART 6 — DOES THE SPLIT PRECEDE COARSE-GRAINING, OR THE REVERSE?

**The record's own two sources embody the two competing orderings — and it does not
adjudicate between them.**

- **Zurek:** a tensor factorization exists *first*; tracing follows. → *split → coarse-graining*
- **Mori-Zwanzig:** choosing the projector **P** *is* the partition. → *coarse-graining → split*

A third alternative — both arising from a deeper primitive — remains open. **None is
selected.** This is the sharpest single result of the audit: U3's ambiguity is not vagueness
in the wording, it is a genuine unresolved disagreement between the two frameworks the record
cites as its basis.

## PART 7 — RELATION MATRIX

| against | classification |
|---|---|
| `background_time_translation_flow` | **NO RELATION** — u3 is outside its blast radius and uses no kernel |
| `rung1_inin_formalism` | **CONCEPTUAL PREREQUISITE (inverted)** — rung1 *assumes* what u3 questions |
| `rung2_kms_gate` | NO DIRECT RELATION |
| `rung3_single_pole` | DOCUMENTARY — the ladder's third rung |
| `u4_constitutive_origin` | **SHARED PRIMITIVE** (coarse-graining); ordering **UNRESOLVED** |
| `u5`, `u6` | NO RELATION (both are branches of u4) |
| the K_R construction | **CONCEPTUAL PREREQUISITE (inverted)** — K_R presupposes the split |
| the declared TT-bath prescription | **CONCEPTUAL PREREQUISITE (inverted)** — naming a *bath* instantiates the very split u3 questions |

No graph metadata was modified.

## PART 8 — OUTSIDE PHYSICS

- **SOURCE FACT:** both cited sources are established literature, not GRUT constructions.
- **INFERENCE:** U3 is a **reformulation of several known open questions** — subsystem
  decomposition / factorization, the choice of the Mori-Zwanzig projector, and einselection's
  preferred-basis problem.
- **OPEN GRUT QUESTION:** whether those share a common answer that *also* yields constitutive
  response. That combination is not a standard question.
- **No validation is claimed.** Resemblance to established open problems is not evidence for
  GRUT and is not recorded as such.

## PART 9 — SOLUTION CRITERION, AND A NEGATIVE CONTROL FROM U3's OWN SOURCE

**U3 SOLVED** requires an exhibited derivation, in either direction: the split shown
irreducibly fundamental, or shown to emerge *with the mechanism exhibited*. Everything weaker
stops at: `U3 ASSUMED → MOTIVATED → FORMALIZED → COMPATIBLE → MODELLED`.

**Negative control — standard decoherence/einselection.** It *appears* to explain the
system/bath split by showing why a pointer basis is selected. It does not: it takes
H = H_S ⊗ H_B as an **input** and selects a basis *within* it. It answers "which states
survive", not "why is there a factorization".

The control is drawn from **u3's own cited source**. The record cites a framework that does
not answer its question — which is itself the warning any U3 candidate must be tested against.

## PART 10 — MINIMAL PROGRAM

Each stage is forced by a defect this audit actually found, not invented:

1. **U3.1** define the object — choose among notions A–F, or prove them equivalent.
2. **U3.2** fix the modality — ontological / mathematical / calculational / operational.
3. **U3.3** identify the candidate primitive and settle the split↔coarse-graining ordering.
4. **U3.4** derive the split, or exhibit it as irreducible.
5. **U3.5** prove representation / observer / scale properties.
6. **U3.6** state handoff conditions to U4.

## PART 11 — FINAL

**Classification: 2 — FORMALIZABLE BUT UNDERSPECIFIED.**

**A. Reason.** The success test is strict and symmetric, but the object is not pinned to one
of six supported notions, and the record's own two sources disagree about the ordering.

**B. Missing definitions.** Which notion of "split"; which modality; the ordering.

**C. Can U3 precede U4?** **Yes.** Per `ba67454`, u4 needs u3's *object*, not u3's *answer*.

**D. Dependency on A–F?** **None.** U3 names no new accepted input and uses no kernel.

**E. Would solving U3 deepen the GUF?** **Qualified yes — with a charter constraint that
must not be skipped.** The register calls a derivation of the split *"a foundational result
(relay-gated)"*. But **CHARTER §8 binds all Version II work**:

> "The purpose of GRUT II is not to derive a Theory of Everything. It is to determine whether
> constitutive response possesses mathematical structures universal across microscopic
> realizations. Every branch is a constrained classification problem with explicit failure
> states — never an ontology to defend."

So a solved U3 would be a foundational **classification** result. An **ontological** reading —
"GRUT has found the architecture of reality" — is **charter-barred**, and U3's own
`differentiator` field independently marks it NON-DIFFERENTIATING.

## W-0 STATUS — U3 specification audited; no physics executed; A-F unchanged; nothing banked.
