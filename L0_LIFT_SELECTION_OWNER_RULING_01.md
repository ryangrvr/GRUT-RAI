# L0 LIFT SELECTION — OWNER RULING 01 (pre-registration approved with amendments)

**Date:** 2026-09-29 · **Recorded by the owner on Issue #2, comment `5899215672`**, reviewing
`L0_LIFT_SELECTION_01.md` at commit `66725e5`. This file records that ruling. The comment is
authoritative; any misstatement here is corrected by owner edit.

## R-0 rulings

| Discriminator | Ruling | Binding interpretation (owner) |
|---|---|---|
| **D-1** retained-site kernel / P_memory / P_positivity / earned geometry-support content | **EARNED** | Only the predicates actually earned, at their recorded scope. Geometry that needs unearned multi-site access is not smuggled into this row. |
| **D-2** one lift must canonically cover the whole earned linear + nonlinear class | **CRITERION** | A universality requirement. It cannot exclude the quasi-free lifts. Lack of nonlinear coverage is recorded as a price/scope limitation. |
| **D-3** classical/FDT correspondence | **CRITERION** | L0-1e is a declared extension, and the correspondence principle is not earned. It cannot select statistics. |
| **D-4** | **AMENDED → EARNED (narrowed)** | Compatibility with the earned source-level passivity/accretivity structure on the descended classical/one-particle sector. **CP is lift-internal consistency/pricing only, not a Level-0 selector.** |
| **D-5** | **AMENDED → EARNED (narrowed)** | Preservation/representation of the O-5 earned ordering/Lyapunov structure on the source-descended observables. A particular quantum relative-entropy functional would be a new criterion. |
| **D-6** commuting local net | **CRITERION as written** | The earned fact is commuting classical site coordinates. It does not follow that every odd generator of a lifted local algebra must commute across sites. CAR can realize graded locality while disjoint even/physical observable algebras commute. **Usable as a compatibility check only; no fermion exclusion.** |
| **D-7** one real coordinate per site | **CRITERION as a selector** | The fact is earned. "No additional complex structure" is a minimality criterion. A supplied complex structure is a **price**, not an exclusion. |

**The EARNED selectors after amendment are D-1, narrowed D-4 and narrowed D-5.**
- D-2, D-3, D-6 and D-7 are priced criteria. They never count toward SELECTED-IN-CLASS,
  CONSTRAINED-NONUNIQUE or REPRESENTATIONAL-ONLY.
- **No discriminator outside D-1 … D-7 may be added after evaluation begins.**

> If the earned record fails to select among lifts once extra minimality/correspondence/local-field
> assumptions are removed, that is the result; do not rescue selection by promoting those
> assumptions after evaluation.

## Required amendments (applied in the frozen `L0_LIFT_SELECTION_01.md`)

- **A. D-4:**

  > source passivity/accretivity compatibility: does the lift preserve the already-earned
  > passive/accretive contraction structure on the classical/one-particle sector from which it
  > descends?

  CP is reported separately, as an internal property, and is not an earned discriminator.
- **B. D-5:**

  > source ordering compatibility: does the lift preserve or faithfully represent the strict
  > Lyapunov/order structure earned in O-5 when restricted to the descended source observables?

  No lifted entropy functional is required unless separately chartered.
- **C. D-6:** the fact is kept. Whether a physical lift must realize it as tensor-product locality
  of all field generators, rather than as graded locality with commuting even algebras, is not
  earned. **D-6 is CRITERION, and the fermionic "exclusion" is only a priced interpretation.**
- **D. D-7:** "one real coordinate per site" is earned. Requiring **no** additional complex
  structure is a minimality criterion. **D-7 is CRITERION**, and any complex structure is reported
  as supplied structure/price.

## Independent verification: AUTHORIZED

- **Output:** `L0_LIFT_SELECTION_VERIFICATION_01.md`.
- **Verdicts:** VERIFIED / VERIFIED-WITH-NARROWER-SCOPE / IMPORTED-STANDARD / NOT-ESTABLISHED /
  COUNTEREXAMPLE.
- **Allowed:** exact algebra, standard theorems with their hypotheses, abstract mathematics only.

**Items:**
- **V-1: I-1, lift by lift.** What exactly does each reproduce: the one-particle map, the retained
  kernel, a reduced semigroup, or only a representation of the same generator? Do not say every
  Hamiltonian extension reproduces the earned kernel unless that is part of its
  construction/hypotheses.
- **V-2: I-2.** Distinguish (1) occupation structure (repeated occupation vs none) from (2)
  numerical generator eigenvalues. Resonances such as 2λ_k = λ_i + λ_j can defeat "the first
  spectral discriminator is −2λ_k", which therefore needs a non-resonance condition. **The safer
  invariant discriminator is repeated-mode occupation, the two-particle algebra, or the associated
  higher correlation structure.** Verify permanent vs determinant at its exact scope.
- **V-3 (PRIORITY): Koopman vs the real bosonic lift.** **Do not merge them because the spectra
  match.** Test whether the deterministic composition f ↦ f(e^{−Kt}x) and bosonic second
  quantization under Wiener–Itô/Segal are the same semigroup. The expected subtlety: second
  quantization of a contraction corresponds to a **Mehler/OU Markov operator**,
  (P_T f)(x) = ∫ f(Tx + √(I−TT\*) y) dγ(y). Merge under R-2 **only on proven unitary/intertwining
  equivalence** of the semigroups and their observable content.
- **V-4: I-3, interface-relative.** "Distinct dilations that realize the same reduced
  retained-site dynamics are indistinguishable **at that earned interface**." Do not claim their
  only differences in all mathematics are bath observables unless proved.
- **V-5: I-4.** Quasi-free second quantization is canonical for linear contractions. Extending
  the nonlinear flow to a non-representational interacting quantum theory needs additional
  choices. **Not quasi-free ≠ no lift exists.** This records scope and price only (D-2 is
  CRITERION).
- **V-6: D-6.** Odd CAR generators in disjoint regions anticommute, while the even subalgebras
  commute under the standard graded-local construction. If that holds, **the predicted fermion
  exclusion is withdrawn.**
- **V-7: D-7.** Where exactly does a noncommutative bosonic lift from a real one-particle space
  need a complex/symplectic structure, as distinct from the commutative real Gaussian/Mehler
  construction? Price it; do not exclude it.

## Evaluation authorization

1. If any claim in I-1 … I-4 fails, apply an additive correction and strike every dependent
   prediction **before** selector evaluation.
2. Evaluate **only** D-1, narrowed D-4 and narrowed D-5.
3. D-2, D-3, D-6 and D-7 are reported as prices/criteria only.
4. Apply R-2 mergers only on proved equivalence.
5. Apply the pre-registered terminal mapping mechanically. **No new discriminator after this
   point.**

## Interpretation fence

- Do not optimize for a positive selector. IRREDUCIBLE/SUPPLIED is a valid terminal at this gate's
  scope, but **only** by the frozen death criterion after verification and evaluation, never from
  the prediction.
- The "different possible universes / formation sectors" discussion is **not** a selector. It
  remains a conceptual possibility, not evidence.

## HARD STOP

After: record → amend and freeze → verify → correct → evaluate D-1/D-4n/D-5n → assign the terminal
mechanically → **HARD STOP.**

No S-5. No EA-1. No gravity reopening. No empirical Standard-Model selector. No numerical physics
campaign.
