# RRP_00_CHARTER — Reality Reconstruction Program, Phase 00: the structural-requirements investigation

**Date:** 2026-09-23. **Authority:** owner opening ("go for it"), issued after — and expressly
distinguished from — the GRUT program closure (`GRUT_PROGRAM_CLOSURE_01.md`, commit
`232e432`). **Status of this document:** charter and gate record. Nothing in it is a physical
claim. Nothing banks from it.

## 0. The question

> Given the structures that physics demonstrably has — quantum amplitudes,
> locality/nonlocality, symmetry, spacetime geometry, statistical behavior, decoherence,
> thermodynamic irreversibility — **what is the smallest set of structural requirements that
> any successful underlying theory must satisfy?**

(Owner's formulation, 2026-09-23.) The deliverable of this program is a **requirements set
with its assumptions priced and its failure points named** — not a theory, not an ontology,
not a candidate framework.

## 1. What this program is not

Not GRUT-2. Not a responsive-medium rung. Not `STRUCTURE_REQUIREMENT_SET_00` as a theory
architecture (ruled out, closure §8). Not a search for the next fundamental rung, and not a
large blind AI campaign (owner prohibition stands). GRUT remains a closed historical
candidate; this program owes it nothing and may not borrow its ontology. The standing rule
"GRUT is the name of whatever survives" applies only if, someday, something survives.

## 2. Gate satisfaction (why opening this does not violate the freeze)

The freeze stopping rule (`GRUT_PROGRAM_FREEZE.md` §1) permits a new effort only under an
**independently motivated** principle identifying something the existing framework cannot
represent — never "we need X because not-X failed." This question is independently motivated:
it is the constraint-space question already chartered before GRUT's failure
(`TOE_LAB_CHARTER.md` §6: treat causality, unitarity, diffeo covariance, KMS/FDT,
decoherence, Lorentz symmetry, quantum statistics and observed cosmology "as constraints on a
space of theories"), and its object is established physics, not GRUT's rescue. The closure
ruling made the three infrastructure items *available, not mandated*, gated on "a concrete
scientific question that cannot be answered without it." The owner has now named the
question, and each tool binds to it directly: the **corpus** (one cannot extract the minimal
requirements of "structures physics demonstrably has" without a verified inventory of them);
the **correspondence-typing engine** (requirements recur across domains only if
correspondences are typed — identity vs analogy vs vocabulary; the archive's recorded failure
mode is "collapsing distinct referents"); the **capability contract** (governs everything
this program builds). Gate: SATISFIED, by owner ruling.

## 3. Inheritance — cite, never rebuild

This program extends the existing record and duplicates nothing: `REALITY_PICTURE_01.md` is
the corpus seed; RC-05's per-case procedure (recursive input ledger → provenance chain →
identifiability → prediction test) is the encoding method; `EC01_ITER3` edge records are the
typing precedent; the vacuum-cluster typed inventory is the form; the eleven controlled
vocabularies stand with their separation rule; `HOW_TO_VERIFY.md` disciplines apply
(emitted-never-typed; guard suite before any irreversible act); `GRUT_MINIMUM_CORE.md`,
`NO_GO_LEDGER.md` completion-specs, and `S_IF.md` §6's two-sided statement form are the
house patterns for requirement statements.

**New vocabulary declared here** (permitted: it grades a new object class, requirement
claims): every requirement arrow carries an **M/D/P/O stamp** — M mathematically admissible ·
D dynamically realizable · P physically realizable · O observationally compatible — with no
inference across stamps (M⇏D, D⇏P, P⇏O), and every cross-domain correspondence carries one
of seven classes: IDENTITY · MATHEMATICAL_ANALOGY · STRUCTURAL_ISOMORPHISM · LIMIT_RELATION ·
EFFECTIVE_CORRESPONDENCE · EMPIRICAL_CORRELATION · VOCABULARY_ONLY (plus UNRESOLVED).

## 4. CONTROL 5 — discharged (read before build)

Carcassi & Aidala, *Reverse Physics: From Laws to Physical Assumptions*, Found. Phys. 52:40
(2022), arXiv:2111.09107 — **verified and read at source 2026-09-23** (abstract + full-text
case extraction). What it provides: law↔assumption *equivalences* — Hamiltonian mechanics for
one degree of freedom equivalent to six characterizations (divergenceless phase-space flow;
area preservation; deterministic-and-reversible evolution; thermodynamically reversible
evolution; information-entropy conservation; constant measurement precision); the uncertainty
principle traced to an entropy bound on pure states (one-directional); the third law
reconceptualized as zero entropy of the empty system. Method rules we adopt: validation by
equivalence proof; the assumption/principle/phenomenological/conceptual distinction;
"pinpoint what part of a theory is responsible for which effect." Scope it does NOT cover —
and where this program's archive holds content it does not: the measurement problem, gravity,
SM parameters. **Binding consequence: their cases enter the corpus as COMMUNITY-DERIVED
entries with citations; this program never re-derives them. Their umbrella project
("Assumptions of Physics") is standing prior art, screened again at every Stage-2 domain it
touches.** CONTROL 6 (Metamath/Lean/reverse-mathematics/RM-Zoo prior-art screen) remains a
hard gate before any engine software is written (Stage 3).

## 5. Constraints register — what the archive already taught (initial entries)

Archive-earned, carried at recorded strength, each an input to the requirements extraction:

- **C1.** Selections are empirically contentful — SJ ≠ BD changes predictions; "choices are
  physics, not notation" (ESTABLISHED; `RAI_GORILLA_T1.md` §XVI-C).
- **C2.** Every description that has successfully closed consumed at least one contentful
  input it did not generate (X1: ESTABLISHED per-case, SUPPORTED as generalization; CPR is
  the lone conditional positive control — uniqueness-given-existence).
- **C3.** Decoherence yields suppression, never outcomes or weights, in the tested class
  (`REALITY_CHECK_04`; cross-validated).
- **C4.** Apparent universal structural gaps decompose per-ontology when typed — "the
  partition of the claim is the finding" (GAP-TRANSFORMS).
- **C5.** Universally-quantified "no formalism can X" claims die at the typing layer, into
  tautology or counterexample (G-WEAK closure, `GRUT_PROGRAM_CLOSURE_01.md` §7). Rule:
  quantify over declared ontologies with frozen predicates, or do not quantify.
- **Firewalls** (owner, 2026-09-23 — firewalls, not conclusions): relation ≠ space ·
  directed update ≠ time · connectivity ≠ geometry · complex amplitude ≠ quantum mechanics ·
  interference ≠ Born rule · stable pattern ≠ particle.

## 6. Stages and gates

- **Stage 0 — this charter + prior-art read.** DONE at commit of this document.
- **Stage 1 — corpus schema + pilot.** Schema in `rrp/corpus/CORPUS_SCHEMA.md`; one PILOT
  domain record (quantum mechanics) demonstrating provenance classes and TO-VERIFY
  discipline. PILOT grade: nothing banks; the pilot exists to be attacked. Begins with this
  commit.
- **Stage 2 — corpus fan-out. OWNER GATE.** Domain list, per-domain effort bound, and
  verification budget set by the owner before any fan-out. Primary-source verification
  converts TO-VERIFY entries or deletes them. No entry enters as established without a
  citation; program results enter only as PROGRAM-RESULT.
- **Stage 3 — engine + contract. OWNER GATE + CONTROL 6 screen.** The correspondence-typing
  engine (schema-and-validator, "never an adjudicator") and the unified capability contract
  (codification of the freeze rule + instrument discipline + cannot-establish statements).
- **Stage 4 — requirements extraction.** Phenomenon → formal requirement → candidate
  structure, every arrow carrying evidence and an M/D/P/O stamp; requirement relativity
  stated (a requirement is FORCED only relative to a declared formalization, alternatives
  inventoried first).
- **Stage 5 — adjudication.** The requirements set confronted with established reality;
  deliverable per §0.

## 7. Stop conditions (pre-registered)

Each stage opens with its own kill conditions; additionally, program-wide: (i) a design gate
showing a step cannot discriminate from input statuses alone stops that step; (ii) the empty
or deflationary result is first-class — **"the minimal requirement set is trivial," "already
known," or "not uniquely determined" are pre-registered legitimate outcomes**; (iii) needed
capability ≠ evidence — a tool that cannot be built under its contract stops its question and
proves nothing; (iv) one bounded attempt per registered question, written verdict; (v) any
drift toward candidate-theory construction stops the phase — theories are out of scope for
RRP-00 entirely; (vi) the owner's standing prohibition on large blind campaigns binds every
fan-out sizing.
