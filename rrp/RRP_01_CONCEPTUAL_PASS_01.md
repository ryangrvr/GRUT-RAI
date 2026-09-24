# RRP_01_CONCEPTUAL_PASS_01 — first analysis of the law/state interface

**Date:** 2026-09-23. **Grade: CONCEPTUAL, UNCHALLENGED — nothing here banks.** This is the
phase's opening analysis, produced inline from the existing verified record (corpus, Stage-4
adjudications, archive). Every candidate explanation below carries its kill condition and
awaits its own adversarial pass. Provenance: entries cited as `domain/field` refer to
`rrp/corpus/domains/`; core items refer to `RRP_00_REQUIREMENTS_PICTURE_01.md` §2.

## 1. Sharpening the pattern before explaining it

Two observations from the record that any explanation must fit — both easy to miss:

**1a. The priced inventory is not homogeneous: it has a law-side and a state-side, and
items MOVE between them.** Branch weights, boundary/initial asymmetry, vacuum/state
selection, and subsystem decomposition are state-side (data about *which* configuration).
G and Λ present as law-side (coefficients *in* the dynamics) — yet the record itself shows Λ
relocating across the boundary: coupling constant in EH form, **integration constant** in
unimodular form, modulus elsewhere (core item D(i)'s "sometimes relocated"). And in the
algebraic frame the traffic reverses direction entirely: Tomita–Takesaki *derives a
dynamics* from an (algebra, state) pair — law from state — at the price of supplying the
pair (archive: `PRIMITIVE_INVERSION_SCOPE.md`; the modular-theory boundary result). So the
law/state boundary is not rigid; specific items cross it under reformulation, in both
directions. Any explanation of the split must explain a *movable* boundary, not a wall.

**1b. The split survives even where the law is not time-symmetric.** Weak-sector T
violation exists (CP violation, CPT-preserving) and is law-side — yet the thermodynamic
arrow still enters as state data everywhere on the record
(statistical_mechanics_thermodynamics/empirical_inputs/0; R9-2′). A law-side asymmetry of
the wrong type does nothing for the state-side asymmetry the phenomena need. Explanations
that say only "symmetric laws can't pick directions" are therefore too coarse; the operative
fact is which *orbit structure* the law's asymmetry does and does not act on.
[Status: the CP-violation half is community-standard but NOT yet a corpus entry —
TO-VERIFY; flagged as this pass's one uncorpused load-bearing input.]

## 2. Candidate explanations, by outcome class, each with its kill condition

### C-I. The invariance argument (classes 1+2: the split's EXISTENCE is theorem-shaped)

**Claim-candidate.** In any formulation of the type (state space X, law = a group or
semigroup of structure-preserving maps on X, state = a point/measure on X), the law cannot
select among configurations it maps into one another or generate quantities it preserves.
Whatever the law's action *preserves* (unitary invariants — hence branch weights; measure —
hence no monotone microstate entropy; time-reversal covariance in the relevant sector —
hence no relaxation direction; covariance under frame/decomposition changes — hence no
selected split) must, if the description needs a value for it, enter as orbit-selection
data. And "orbit-selection data on X" is what *state* means in this presentation. The
split's existence is then a theorem of the presentation: **laws-as-symmetries cannot choose
among their own orbits; choices are therefore state, by construction.**

Fit to the record: unitarity preserves amplitudes → weights inherited (R7.2′, exactly the
RC-04 mechanism); measure preservation + reversibility → direction state-supplied with
magnitude free (R9-2′ — |Im Σ| is not conserved-quantity-like, so dynamics may fix it; the
sign rides an orbit pairing); covariance of the field equations over state space → SJ vs BD
undecided by dynamics (R10.2′); §1b's nuance fits: weak T-violation acts on the wrong orbits
(flavor sector), leaving macroscopic time-orbits paired.

**What this would make the split:** class 2 (consequence of the symmetry structure of laws)
wearing class 1 clothes (relative to the (X, law, state) presentation — a presentation that
is itself near-universal in the audited corpus but is still a declared class, per C5).

**Kill conditions.** (i) Exhibit an audited formulation NOT of (X, law-as-automorphisms,
state) type that still shows the split — then the argument explains less than the pattern.
(The algebraic (M, φ) frame is the candidate: there dynamics is *derived*, yet the supplied
pair still carries the selections — which suggests the invariance argument is a special
case of something broader, not the root.) (ii) Show the argument is itself the vocabulary
trap — that "law" is *defined* as the invariant part, making C-I circular; this is C-III's
job below, and if C-III holds, C-I demotes from theorem-about-physics to
theorem-about-bookkeeping. (iii) A formal counterexample: a symmetric law with an
attractor-like mechanism generating an asymmetry without state input in the tested classes
(the record holds none: "no washing-out/attractor mechanism," R7.2′).

### C-II. The conservation-of-priced-input conjecture (class 2: the regress is a trade, never a discharge)

**Claim-candidate.** In the audited record, no reconstruction, reformulation, or derivation
strictly reduces the independent supplied content of a description; each converts priced
inputs into other priced inputs (usually relocating them upstream or across the law/state
boundary). If true at generality, "derive" in derive-or-price is *always* local — a
re-pricing — and the split is globally irreducible within the audited formalism space.

**Preliminary ledger check (from the existing corpus — single-pass, unchallenged):**

| Machinery | Consumes (priced) | Produces (derived) | Net supplied content |
|---|---|---|---|
| Gleason | projection lattice; noncontextuality; dim ≥ 3 | Born *form* | not reduced — relocated upstream (math_foundations, Gleason entries) |
| POVM-Gleason | effect-noncontextuality (strictly stronger) | Born form incl. dim 2 | traded up |
| CPR | spectrum; k-locality demand; genericity; *existence* | uniqueness of factorization | conditional; selection → criterion (qm/primitives/2) |
| Tomita–Takesaki | (algebra M, state φ) | dynamics (modular flow) | law derived, pair supplied; "M cannot select M" (archive) |
| Solèr | orthomodular lattice + infinite orthonormal sequence | Hilbert structure | relocated |
| Operational reconstructions | axioms incl. local tomography (the composite rule — a selection-type input) | QM formalism | composite structure priced as axiom |
| Jacobson route | area entropy + Unruh temperature | Einstein equation | imports named (R8.2′) |
| No-boundary-class proposals (class-4 candidates; NOT in corpus) | contour/measure choice (reported in literature) | initial state from law | TO-AUDIT — the crunch case |

Every audited row conserves or increases supplied content while changing its *type* and
*location*. This is X1 (`RAI_DIALECTIC_CHAMBER`, capped SUPPORTED) sharpened into a
bookkeeping-testable form, and it is the freeze's "shorten and relocate the input list"
promoted from observation to conjecture.

**Kill conditions.** (i) One audited counterexample: a reconstruction whose input ledger is
strictly smaller (count *and* type) than its output's former price — the class-4 gate of the
charter, applied retrospectively. The named crunch cases to audit: no-boundary/tunneling
proposals (state-from-law; do contour and measure choices re-price it fully?), and CPR's
existence half. (ii) Formalization failure: if "independent supplied content" cannot be
given a formulation-invariant measure, the conjecture is not well-posed — this is the
conjecture's own ill-posedness risk, and finding *that* would itself be a class-1 result
about the split (the ledger can't be summed across formulations ⇒ the split's "size" is
vocabulary). Note the archive's own precedent for refusing type-mixed sums
(`VACUUM_CLUSTER_MAP`: "if the integer is a type-mixed sum, don't ship an integer").

### C-III. The one-preparation reading (class 3 + class 1: the split's CONTENT is the universe's single preparation; its BOUNDARY is the operational method's shadow)

**Claim-candidate, part A (deflationary).** Operationally, "law" names the regularities
invariant across the preparations we can vary; "state" names what preparations vary. Under
that reading the split is analytic in the experimental method itself — laws *cannot* fix
what preparations select because law was defined as the preparation-invariant part.

**Part B (the bite — where A stops being empty).** The reading makes one sharp,
record-checkable prediction: the law/state classification should become *ambiguous exactly
where the ensemble of preparations collapses to one* — the unrepeatable, cosmological
items. And that is precisely what the record shows: the items that wander across the
boundary or resist classification are Λ (constant ↔ integration constant), G, the past
hypothesis/initial condition, the vacuum choice, and the global decomposition — **the
priced-input inventory of core item D is, almost exactly, the specification of the one
preparation we cannot vary.** Meanwhile the cleanly law-side items (coupling *runnings*,
spectra, |Im Σ|) are those tested across many preparations. Even the archive's T1 result
takes this shape: every well-typed split "is indexed to something a describer brings" — the
describer being the one who fixes the preparation frame.

**What this would make the split:** boundary = class 1 (method artifact, movable);
content = class 3 (contingent single-preparation data). Jointly with C-I it composes into a
layered answer rather than competing with it.

**Kill conditions.** (i) A clean counterexample either way: a many-preparation-varied
quantity that nonetheless resists law-side classification, or a genuinely
preparation-invariant quantity that the record forces onto the state side. (ii) The
firewall check: part A must not smuggle "reality is observer-dependent" — it is a claim
about *classification*, not about what exists; if its content cannot be stated without that
smuggle, part A dies as vocabulary. (iii) If part B's correlation (boundary-ambiguity ↔
unrepeatability) fails under a systematic corpus sweep, part B dies as a coincidence read
off four examples.

### C-IV. Class-4 status: open, with the gate fixed

No audited machinery derives the split or any priced input outright. The record's two
candidate shapes: CPR (uniqueness-given-existence — a *conditional* derivation whose
existence half is the unpaid price) and the no-boundary class (state-from-law, unaudited,
with contour/measure choices as the suspect re-pricing). The charter's strict-reduction
criterion is the gate; C-II, if it survives challenge, is the standing conjecture that the
gate never opens. **These are opposed predictions, and that is healthy: C-II vs any
class-4 candidate is the phase's first genuine contest.**

## 3. The layered picture this pass proposes (for challenge, not for banking)

- **Existence** of the split: theorem-shaped, from the symmetry structure of laws in the
  (X, law, state) presentation class (C-I) — class 2 relative to a declared class 1 frame.
- **Location** of the boundary: formulation-relative and movable (1a; C-III part A) —
  class 1.
- **Content** of the supplied side: the single-preparation data of our universe (C-III
  part B) — class 3.
- **Global reducibility**: conjectured NO (C-II), with named crunch cases and a live
  class-4 contest.

And the residual question this layering exposes — the phase's possible successor question,
noted, not opened: **not "why is there a supplied side" (C-I answers that within its class)
but "why is the supplied side so SMALL"** — a handful of constants, one low-entropy
condition, near-universal selections. The compressibility of the state side is the one
feature none of C-I/II/III touches.

## 4. What this pass could not settle by analysis, and what it asks for next

Smallest sufficient instruments, in order, all cheap and all owner-visible before launch:
1. **Adversarial pass on C-I, C-II, C-III** (three refuters, the Stage-4 discipline —
   small, bounded; the vocabulary-trap route is the main threat to all three).
2. **The ledger audit** completing §2's table against sources: the no-boundary/tunneling
   crunch case (literature, read-level), the CPR existence half, and formalization of
   "independent supplied content" or a reasoned verdict that it cannot be formalized.
3. **Corpus sweep for C-III part B** (mechanical: classify every priced/ambiguous item by
   repeatability; test the correlation; the corpus already contains the data).
4. One TO-VERIFY discharge: the weak-sector T-violation entry (§1b) into the corpus.

No computational campaign is requested. Items 1–3 are read-and-adjudicate work over the
existing record; each carries its kill conditions above.

---

## CORRECTION 01 (2026-09-24, visible per house rule — from the challenge round)

§1a wrongly grouped **G** with Λ among boundary-wandering items. The C-III sweep
(48-item classification) found no corpus support for any relocation of G: its value is
many-preparation lab-measurable and its classification is stable. The movable-boundary
observation stands on Λ and the framework-scale items alone. Verdicts and narrowed forms:
`rrp/rrp01/CHALLENGE_ROUND_01.md`.
