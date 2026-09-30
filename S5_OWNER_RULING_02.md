# S5 — OWNER RULING 02 (S5-1 pre-freeze review; one analytic execution authorized)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5904251680`**, after review of
`S5_CONSERVATIVE_ORIGIN_01.md` at `4761f6c`, the accepted S5-0 ruling and correction, and the exact
Level-0 kernel definition. The comment is authoritative; this file records it.

**Decision.** The charter is **APPROVED WITH AMENDMENTS.** Once the amendments are frozen at a new
commit, **ONE S5-1 analytic physics execution is authorized**, with a campaign-specific post-v4
exception for S5-1 only.

## 1. OR-A: admitted limits

- **L-N (N → ∞ at fixed declared local parameters):** APPROVED unchanged. It is the primary
  parent-preserving route.
- **L-vH:** APPROVED as an **admitted controlled deformation of the declared parent class, not an
  already-evaluated O-6 member.** The family is:
  - K₁₁ = 2.3 fixed and K_BB fixed;
  - **only** K₁₂ = K₂₁ = −g varies, with 0 < g ≤ 1; every other entry is fixed;
  - N → ∞ first, then g → 0 with τ = g²t fixed.

  Conditions:
  - Results are labelled **conditional on the weak-coupling deformation**, because O-6 was
    evaluated at g = 1.
  - **Positive definiteness must be proved for the whole family** before the family is used.
- **Correction to §6 of the draft.** Do not write a finite rescaled-time "lab-frame limit generator"
  M = −A₀ + Γ; that mixes physical and kinetic time. Freeze instead:

  Ψ_g(τ) = e^{−A₀τ/g²} Φ_{∞,g}(τ/g²),

  with the primary question whether Ψ_g(τ) → e^{Bτ}, compact-uniformly on every finite τ-interval,
  with B derived from the parent spectral measure. **Then separately reconstruct the physical
  retained dynamics.**
  - An interaction-picture Markov envelope counts toward MARKOV-LIMIT-OTHER-CLASS **only if** the
    derivation also yields a controlled, time-homogeneous, damped-oscillator effective generator in
    the physical variables (equivalently A₀ + g²B_eff + ⋯ on kinetic times).
  - The free oscillation may not be discarded when assigning M-1 vs M-2.

  > **An interaction-picture exponential by itself is not a Level-0 G-D derivation.**
- **L-WB: NOT ADMITTED.** It is a named missing ingredient only: a singular parent deformation that
  scales the bath scales and g jointly.
- **L-OD: NOT ADMITTED.** It is a named missing ingredient only: the parent has no independently
  tunable mass or friction scale.

## 2. OR-B: execution mode

A new analytic derivation **is physics work** and needs the exception. It is granted, after the
freeze, for one execution.

**The execution may produce:**
- exact spectral-measure derivations;
- Laplace, resolvent, branch-point and pole analysis;
- the finite-N recurrence proof and the infinite-N asymptotic proof;
- the exact CM tests;
- the admitted L-vH derivation;
- the NI audit;
- the terminal verdict.

**Numerical cross-checks** are allowed **only as non-adjudicating checks, after the analytic result
they check has been derived.**
- **Members:** N ∈ {23, 47, 95}, and the K(g) family at g-values pre-listed in the charter.
- **Purposes:**
  - verify closed-form spectra;
  - check a derived bound-state statement;
  - check asymptotic formulas;
  - check the derived weak-coupling approximation.
- **Not allowed:**
  - exponential fitting treated as evidence;
  - choosing windows post hoc;
  - deciding a theorem claim the analytics did not settle;
  - searching g.
- **Defects:** a defect in a declared cross-check is preserved, and the run stops before any re-run,
  unless the analytic terminal is wholly independent of that check.

## 3. OR-C: MARKOV-LIMIT-OTHER-CLASS is ACCEPTED as a distinct frozen outcome

It is not folded into REQUIRES-SINGULAR/NEW-PARENT.

> **MARKOV-LIMIT-OTHER-CLASS:** an admitted limit derives a genuine time-homogeneous Markov
> semigroup/effective generator for the retained physical variables, but its structural type is not
> the Level-0 first-order CM/real-spectrum G-D class.

A rotating-frame envelope without a controlled physical-variable effective generator is not enough.

## 4. OR-D: scalar reading R2

p₁(0) = 0 is approved **only as a scalar response preparation**:
φ_N(t) = e₁ᵀcos(√K_N t)e₁, from q₁(0) = 1, p₁(0) = 0, bath at rest.

- C₀′ is **not** an invariant one-dimensional state space, because the parent immediately generates
  p₁(t) ≠ 0.
- **Short-time control:** φ_N(0) = 1, φ_N′(0) = 0, φ_N″(0) = −K₁₁. A nontrivial exact scalar law
  e^{−γt} with γ > 0 is incompatible at t = 0 for every regular member. This is to be **proved
  formally**; it is not a previewed terminal.
- **Scalar Markov success requires one of:**
  - a proven limiting slaving relation that eliminates p₁;
  - a directly proven scalar semigroup with restartability that does not depend on hidden
    momentum or history.

  Otherwise the scalar result is graded at **kernel/response level only.**

## 5. OR-E: kernel form (correction)

- **The draft made a category mismatch.** The Level-0 object k_D(t) = e₁ᵀe^{−K_b t}e₁ is the
  **retained response**, not the GLE friction kernel.
- **Primary K-L0 target:** the parent's **retained response/propagator.** For R2 this is φ_N; for R1
  the charter must state the component and how the comparison is made.
- **Memory diagnostic, kept separate:** derive and report the exact GLE friction kernel
  Γ_fric(t) = g²e₁ᵀK_BB⁻¹cos(√K_BB t)e₁, and optionally the sine/self-energy form. These **explain**
  (non-)Markovianity. They are not identified with k_D.
- **Exact local CM attack:** Γ_fric″(0) = −g²e₁ᵀe₁ < 0 (with the exact derived normalization) and
  φ″(0) = −K₁₁ < 0, while complete monotonicity requires f″(0) ≥ 0. Do not rely only on late-time
  tails.

## 6. Target levels (renamed)

| Level | Name | Definition |
|---|---|---|
| **M-1** | PHYSICAL MARKOV | A closed retained physical-variable map that is a time-homogeneous, strictly dissipative semigroup. |
| **M-2** | G-D-PROPER | M-1, plus an autonomous first-order retained law, real non-negative decay spectrum (up to clock rescaling), and a CM scalar response where applicable. |
| **K-L0** | RETAINED-KERNEL-CLASS | The parent's **retained response** (not its GLE memory kernel) lies in the Level-0 response-kernel class. |

## 7. Outcome order (frozen, with one tightening)

1. UNFORMULABLE
2. EXACT-GENERATOR-DERIVED
3. MARKOV-LIMIT-DERIVED
4. MARKOV-LIMIT-OTHER-CLASS
5. REQUIRES-SINGULAR/NEW-PARENT
6. NONMARKOVIAN-DISSIPATION-ONLY
7. UNDERDETERMINED

**Item 5 fires only if** the analysis establishes that M-2 requires a **specifically identified**
non-admitted ingredient. It does not fire merely because L-N and L-vH fail. If the ingredient is not
established and the parent yields only decay with memory, the outcome is item 6.

## 8. Required analytic sequence

1. **Finite-N theorem:** recurrence/almost-periodicity; no exact strictly decaying semigroup; the R2
   short-time obstruction.
2. **Infinite-N spectral theorem:** the spectral measure or resolvent; a bound-state audit; band-edge
   branch structure; the long-time class.
3. **Kernel-class theorem:** local CM tests; the pole/branch-cut distinction; the exact GLE friction
   kernel, kept separate from k_D.
4. **Weak-coupling theorem:**
   - validity of the K(g) family;
   - the isolated frequency relative to the bath spectrum;
   - the van Hove semigroup (or its failure);
   - reconstruction of the physical-variable dynamics;
   - assignment of M-1/M-2 in that sense.
5. **NI audit.**
6. **Mechanical terminal.**

The optional cross-checks run only after steps 1–4.

## 9. Freeze requirements

1. Apply OR-A … OR-E exactly as ruled.
2. Correct the van Hove statement.
3. Put K-L0 on the retained response.
4. Make the friction kernel a separate diagnostic.
5. Add R2 closure/restartability and the short-time control.
6. Freeze MARKOV-LIMIT-OTHER-CLASS.
7. Freeze the cross-check g-values.
8. Replace the open items with these rulings.
9. Commit.
10. Record the hash in CURRENT_STATE as the **frozen S5-1 charter.**

**No S5-1 member calculation before that commit.**

## 10. Exception scope

**Covered, and nothing else:**
- the fixed O-6 parent;
- L-N and the admitted L-vH family;
- the theorem sequence;
- the pre-frozen non-adjudicating cross-checks.

**Not covered:**
- L-WB or L-OD as derivation routes;
- another spectral density, added friction or noise, or a second parent;
- a re-run after a charter change;
- S5-2 or SF-2;
- gravity, Π₀ or cosmology.

**After the verdict: HARD STOP for owner adjudication.**

> **Objective:** determine whether the declared local conservative GRUT parent derives the actual
> Level-0 Markov generator, derives only a different Markov effective law, or yields irreducibly
> non-Markovian dissipation.
