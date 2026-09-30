# S5 — OWNER RULING 03 (S5-1 terminal accepted; S-5 closed at current-parent scope)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5904495463`**, after review of
`d603db5` (charter), `6170129` (analytic derivation, pre-cross-check), `ed2bbe3` (pre-run script) and
`6a17b57` (result/verdict). The comment is authoritative; this file records it.

## 1. Terminal: ACCEPTED

> **S5-1 = MARKOV-LIMIT-OTHER-CLASS**, conditional on the admitted L-vH weak-coupling deformation.

> **The declared local conservative parent does not derive the Level-0 first-order G-D generator. It
> does, however, derive a controlled Markov effective law of a different structural class in the
> admitted weak-coupling limit: an underdamped oscillator on the retained phase-space variables.**

This is a genuine positive derivation result and a genuine negative result for the Level-0
generator.

## 2. Provenance: valid

- The sequence was d603db5 → 6170129 → ed2bbe3 → 6a17b57.
- The charter, derivation and script are each **byte-identical** between their commit and
  `6a17b57`.
- There was no re-run.

## 3. Analytic core: ACCEPTED

- **Finite N:**
  - positive definiteness for K_N(g);
  - simple Jacobi spectrum with positive weights;
  - almost periodicity and recurrence;
  - no exact strictly dissipative semigroup and no exact semigroup on R1;
  - the R2 short-time obstruction φ(0) = 1, φ′(0) = 0, φ″(0) = −K₁₁, so e^{−γt} is impossible.
- **Native N = ∞, g = 1:**
  - purely a.c. on [0.3, 4.3], with no bound state;
  - √ branch points and a non-rational Laplace transform;
  - t^{−3/2} oscillatory tails.

  This gives **L-N, g = 1: NON-MARKOVIAN DISSIPATION ONLY**, consistent with the O-6 t^{−3}
  bilinear tail.
- **K-L0 FAILS** for every finite N, for N = ∞, and for every fixed g > 0. The local obstruction
  φ″(0) = −K₁₁ < 0 kills CM, and the late-time branch cut is an independent obstruction.
- **GLE memory diagnostic:** φ is the K-L0 object, and Γ_fric is a separate diagnostic.
  Γ_fric″(0) = −g² < 0. There is no white friction kernel at fixed g.

## 4. Weak-coupling theorem: ACCEPTED

- **Resolvent and density:** F_g(z) = 1/(2.3 − z − g²F(z)). The exact density is accepted, and there
  are no bound states for 0 < g ≤ 1.
- **Scaled limit:** g²ρ̃_g(ω_s + g²x) → (1/π)κ/(x² + κ²), with κ = 1/(2√2.3).
- **Scheffé is legitimate:** both sides are probability densities and pointwise convergence is
  derived, so the convergence is L¹. **This controls the Fourier transforms uniformly in time.**
- **Uniform approximation:** with concentration of the bounded ω and 1/ω weights,
  sup_{t≥0}‖Φ_g(t) − e^{(A₀ − κg²I)t}‖ → 0. **The terminal is not inferred from X-5.**
- **Interaction picture:** Ψ_g(τ) → e^{−κτ}I is accepted.

## 5. Physical reconstruction: ACCEPTED, with precise wording

- **The effective generator:** A_eff(g) = A₀ − κg²I, with eigenvalues −κg² ± iω_s and second-order
  form q̈ + 2κg²q̇ + (ω_s² + κ²g⁴)q = 0.
- **M-1: YES** (in the controlled weak-coupling sense).
- **M-2: NO.**
  - Inertia survives and the spectrum stays complex.
  - The response oscillates and is not CM.
  - q₁ is not autonomous.
  - L-vH produces no slaving or overdamped reduction.
- **Required wording:**

  > **The weak-coupling kinetic limit derives a controlled underdamped Markov effective dynamics,
  > with a parent-derived damping rate of order g².**

  Do **not** write "the g → 0 parent has finite physical damping" without the qualifier. In physical
  time the rate κg² → 0; the finite decay is on the kinetic scale τ = g²t. **That distinction travels
  with the terminal.**

## 6. The S-5 supplementary false flag

- **It does not void the execution.** At x = 0 the scaled exact density equals the target **for
  every g**: g²ρ̃_g(ω_s) = 2ω_s/π = 1/(πκ). A strict-decrease criterion was therefore mathematically
  impossible there.
- **The substantive checks pass:** `sympy_limit_matches: true`, and the deviations at nonzero x are
  O(g²).
- **Record correction:**
  - The JSON `"defects": []` is explained by the script: that field records X-block exceptions, not
    false supplementary predicates.
  - **Do not rewrite the JSON.** Add `S5_CONSERVATIVE_ORIGIN_CORRECTIONS_01.md` instead.

## 7. What S5-1 changes

- S5-0 stays valid: earned static structure does not imply a unique generator.
- **New constructive fact:** conservative local parent + controlled weak coupling ⟹ Markov
  effective dynamics. This is possible in the declared class, so **"a Markov generator must always be
  primitive" is false.**
- **But:** the conservative parent does **not** reach G-D-proper by the admitted routes.
- **The distinction:** *Markovianity can emerge; the specific inertia-free CM Level-0 generator does
  not.*

## 8. Status of the Level-0 generator

> **The Level-0 first-order G-D generator remains IRREDUCIBLE/SUPPLIED relative to the current GRUT
> parent and admitted reductions.**

- Do not shorten this to "the generator is supplied" without scope, because S5-1 derived another
  generator class.
- **Do not say:**
  - conservative dynamics cannot yield Markovianity;
  - all dissipation is non-Markovian;
  - an overdamped limit is impossible;
  - a wide-band limit is necessary;
  - the G-D generator can never be derived.

  The last two are only indicated future ingredients, not necessity theorems.

## 9. S-5 current-scope terminal

The pair: **S5-0 = GENERATOR-IRREDUCIBLE/SUPPLIED** and **S5-1 = MARKOV-LIMIT-OTHER-CLASS.**

> **Static GRUT structure does not select the temporal generator. The existing conservative parent
> can derive an underdamped Markov effective law in a controlled weak-coupling limit, but neither the
> native parent nor that admitted limit derives the Level-0 first-order completely-monotone
> generator.**

## 10. No automatic rescue

L-WB and L-OD are **not** opened as S5-2. Opening them now would violate the no-rescue discipline.
They are preserved as **future named options only:**
- **S5-WB:** can a principled wide-band parent limit derive local friction?
- **S5-OD:** can an independently earned overdamped/slaving hierarchy derive the inertia-free G-D
  law?

Neither is selected.

## 11. Actions / HARD STOP

**Actions:**
- create this ruling;
- add the verdict banner;
- create `S5_CONSERVATIVE_ORIGIN_CORRECTIONS_01.md`;
- create `S5_GENERATOR_ORIGIN_DEPOSIT_01.md` (no new analysis);
- update CURRENT_STATE.
- Then **HARD STOP** for the owner's selection of a genuinely new campaign.

**Not authorized:**
- S5-2 or a re-run;
- a new parent or SF-2;
- gravity, Π₀ or cosmology.

> **GRUT's conservative parent can generate Markovianity, but not the Markovianity GRUT originally
> assumed.**
