# L0-1 FLOOR — REGISTRY RULINGS R-1 … R-4 (owner rulings recorded; the amended registry)

**Date:** 2026-09-29 · **Given in-session by the owner** on
`L0_1_FLOOR_DESIGN_01.md` §3 (commit `ee12396`; Issue #2 comment
`5882934415`). Recorded from the owner's own words; any misstatement
is corrected by owner edit, not defended.

## The rulings

| Registry | Decision |
|---|---|
| **R-1** envelope comparator | **ACCEPTED** |
| **R-2** P^resp / P^corr split | **ACCEPTED** |
| **R-3** static (resolvent / Jacobi) readings | **ACCEPTED AT DECLARED LINEAR-CLASS SCOPE** |
| **R-4** passivity = accretivity | **ACCEPTED** — spectral stability recorded as distinct and weaker |

**R-1 (the owner's reasoning, preserved):** the envelope comparator
E(τ) = max_{τ′∈[τ,40]} |k(τ′)| is the right extension for oscillatory
kernels because it prevents ln(k) from becoming an accidental
instrument failure. On the already certified class, where k is
positive and decreasing, E = k, so no previous reading changes.

**R-2:** additive noise leaves the mean response unchanged while the
covariance/correlation sector can change materially; treating them as
one object would collapse two mathematically distinct questions.

**R-3, with the owner's qualification binding on every future face:**
the resolvent G(z) = e₁ᵀ(K + zI)⁻¹e₁ and the Jacobi/Favard structure
are a legitimate static formulation of the linear problem where their
hypotheses hold. The record must **not** say "every time-domain
predicate is interchangeable with a static predicate everywhere." The
equivalence holds within the declared linear class and the stated
mathematical hypotheses. This removes primitive time from the
*formulation* where possible, without pretending that every dynamical
notion has thereby disappeared.

**R-4:** for non-normal generators the passivity notion is
**accretivity**, K_s = (K + Kᵀ)/2 ⪰ 0; **spectral stability**,
Re λ_j ≥ 0, is recorded as a distinct, weaker property, because
non-normal matrices can be spectrally stable and still allow
transient growth. D-HERM must not silently carry the symmetric-case
meaning of "passive" over to the non-normal case.

## The amended predicate registry (effective for every floor charter)

- **P_memory:** the frozen L0-1a comparator applied to the envelope
  E(τ) (R-1). Identical to the certified reading on every positive
  decreasing kernel.
- **P_positivity:** read in named components, never composed:
  (a) nonnegativity; (b) monotone decrease; (c) complete monotonicity
  — via the trajectory Gram (L0-1c), or via the static Jacobi/Favard
  reading at linear-class scope (R-3). A certificate names which
  components it adjudicated.
- **Passivity (as a deleted or held axiom):** accretivity (R-4).
  Spectral stability is a separate, weaker property and is always
  named as such.
- **Stochastic substrates:** every predicate splits into P^resp and
  P^corr (R-2).
- **Static readings:** theorem-equivalent to the time-domain readings
  **within the declared linear class and under the stated
  hypotheses only** (R-3).

## The hypothesis stays a hypothesis (the owner's instruction)

**Dissipation** and **detailed balance** remain *hypotheses suggested
by the design analysis, not results.* The owner noted specifically
that D-HERM may show cycle affinity breaking one structure while
leaving another intact, and that D-DET may show the
fluctuation–dissipation relation, rather than determinism itself,
carrying the correlation constraint.

## Order (authorized)

**D-HERM → D-DET → D-ORD**, with D-ORD starting as the theorem /
formulability treatment and only then getting its conservative-class
numerical fork. **The pin-free locality fork is not moved ahead of
this sequence;** it stays an important unresolved branch that answers
a different question.

## Condition set by the owner before D-HERM freezes

The successor termination condition must be established first. The
owner's constraint on its form: it must not be "until GRUT
succeeds." It should be structural, a finite set of obligations
whose possible outcomes are **discharged, falsified, class-split, or
shown unformulable with a documented reason**. That gives the floor a
real endpoint and leaves the broader scientific exploration
completely open. Drafted for owner adoption in
`L0_1_FLOOR_TERMINATION_DRAFT_01.md`.
