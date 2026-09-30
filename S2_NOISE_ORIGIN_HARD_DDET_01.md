# S2-0 — HARD D-DET / NOISE-ORIGIN DISCRIMINATOR: formulation / class-selection gate

> **OWNER RULING (Issue #2 comment `5905401028`; `S2_OWNER_RULING_01.md`):**
> - **F-1 = (b):** M2 stays **arbitrary**, as pre-registered.
> - **S2-0 = CLASS-SPLIT** (accepted). The proposed MINIMAL-CLASS-FOUND is **NOT ADOPTED yet.**
> - **Binding qualifier:** C-B is theorem-level distinguishable on the retained mean response under
>   M1, and under M2 for preparation-independent hidden laws with the required finite moments;
>   arbitrary M2 remains open. C-A, C-C and C-D remain equivalent on the frozen control-blind
>   observables at their audited scopes.
> - **Accepted at theorem scope:** m₁^𝒮 − m₁^𝒟 = −12βT₁a·t² + O(t³) (C-B, M1).
> - **F-2 and F-3 accepted.** The SECOND-ORDER-EQUIVALENT labels are to be read narrowly, as
>   O-1/O-2 at the audited scope only.
> - **T-HT is mandatory in S2-1.**
>
> §§0–5 below are preserved as filed.

**STATUS: AUDIT COMPLETE.**
- §§0–3 were pre-registered at `8e1c8e7` and are unchanged.
- §4 (the audit) and §5 (the proposed outcome, **MINIMAL-CLASS-FOUND (C-B)**, conditional on flag
  F-1) have been added.
- The S2-1 charter is drafted, not frozen.
- **HARD STOP.**
- **Authority:** `S2_CAMPAIGN_OWNER_DIRECTION_01.md` (Issue #2 comment `5904589246`).
- **Audit/formulation only:** no simulation, no RNG, no sweep, no v4 exception.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosure (prior expectations, not results).** Reading the direction and the S-1/F-5 record, the
auditor expects two things:
- **(a)** Whenever the canonical (Itô) drift is linear, the conditional mean closes exactly, so
  first-moment objects stay noise-blind **whatever the noise law is.**
- **(b)** A nonlinear drift breaks that closure.

§3 is written so that these expectations are tested by the §2 obligations, not decided by wording.

## §0 Question (direction, verbatim)

> Is there a minimal declared stochastic extension of the Level-0 substrate for which primitive
> stochastic forcing changes a retained observable in a way that cannot be reproduced by
> deterministic evolution with only randomized initial data, while holding the deterministic
> drift/substrate fixed?

## §1 Frozen definitions

**D-1. Ingredient ledger.** The declared ingredients are:
- K = K_b, the sealed bath block (`L0_1E_CHARTER_01.md` §1; `L0_1C_CHARTER_01.md` §1);
- the **L0-1c cubic drift** f_β(x) = −Kx − 4βx^{∘3}, with β ∈ {0.03, 0.1, 0.3, 1.0, 3.0} declared;
- the **L0-1e additive noise** Q = BBᵀ = 2·diag(T_i), with the declared profiles (for example member
  F, T_i ≡ 1);
- the **L0-1c probe** x(0) = a·e₁, with a ∈ {0.001, 1.0, 3.0} declared.

**New ingredients by candidate:**

| Candidate | New ingredients |
|---|---|
| C-0 (control, L0-1e) | 0 |
| C-B | 0 (the combination of the declared drift and the declared noise only) |
| C-A | multiplicative noise matrices G_a |
| C-C | a correlation matrix Γ and an auxiliary state η |
| C-D | a non-Gaussian increment law |

**"Minimal"** means the fewest new ingredients. Ties are broken by the direction's order.

**D-2. The candidates.**
- **C-0 (control):** dx = −Kx dt + B dW (L0-1e). This is the S-1 class.
- **C-A:** dx = −Kx dt + Σ_a G_a x ⋆dW_a, where ⋆ is either Itô or Stratonovich.
- **C-B:** dx = f_β(x)dt + B dW. The noise is additive, so Itô and Stratonovich coincide.
- **C-C:** dx = f(x)dt + Bη dt, dη = −Γη dt + dW. The Markov state is (x, η).
- **C-D:** dx = −Kx dt + dL, where L is a zero-mean, square-integrable non-Gaussian Lévy process.

**D-3. Canonical drift and the Itô/Stratonovich firewall.**
- **Definition.** The **canonical drift** f_can of a process is the first-order coefficient of its
  backward generator 𝓛, which is the Itô drift. 𝓛 is convention-invariant as an operator, so f_can is
  too.
- **The deterministic comparator always uses f_can.** A Stratonovich model is first rewritten in Itô
  form. f and G are held fixed **as a process**, not as written symbols.
- A difference obtained by comparing with the *Stratonovich* drift is exactly the conversion term
  ½Σ(G_a·∇)G_a. **It is labelled SECTOR-SMUGGLED (convention) and never counts as evidence.**

**D-4. Preparations.**
- **(P-imp) retained impulse:** x(0) = a·e₁ with the bath at rest. This is the declared L0-1c probe.
  For theorem statements a ranges over an interval containing the declared values. Any finite
  evaluation uses **at least five distinct nonzero a**, including the declared {1.0, 3.0} and their
  negatives.
- **(P-st) stationary:** x(0) ~ π_𝒮, the stationary law of 𝒮, where it exists.

**D-5. Comparison modes** (𝒮 = stochastic member; 𝒟 = deterministic flow φ_t of the same f_can):
- **M1 (direction §6, literal):** same f_can and **same P₀**; 𝒟 has no forcing after t = 0.
- **M2 (uncertain initial state; "cannot be matched merely by choosing P₀"):**
  - Same f_can.
  - 𝒟 starts from x(0) = a·e₁ + ξ, where the hidden initial datum ξ ~ ν is **arbitrary** (any law on
    the Markov state space; any mean, covariance or higher moments) but **independent of the
    preparation a.**
  - The question is existential: does some ν reproduce 𝒮's observable at every declared a?
- **Enlarged states (C-C):** if 𝒮's Markov state includes auxiliary variables, 𝒟 lives on the same
  enlarged space. The auxiliary variables are then part of the hidden initial data.

**D-6. Observables** (retained site 1; lowest order first):
- **O-1, the retained mean response map:** m₁(t; a) = 𝔼[x₁(t) | x(0) = a·e₁] for 𝒮, and its 𝒟
  counterpart under M1/M2.
- **O-2, the anchored lag correlation:** R(τ) = 𝔼[x₁(τ)x₁(0)] from (P-st). This is the S-1 object.
- **O-3:** non-anchored C₁₁(t, s), and higher cumulants.
- **No exotic readout** (direction §6).

**D-7. Control rule (consuming S-1).**
- An observable **can count as an S-2 discriminator only if it is noise-blind (𝒮 ≡ 𝒟) in the control
  class C-0 under the same mode.** Otherwise it would separate the classes merely by the diffusion
  term, which is the T4 warning.
- Declared now, to be **re-verified in §4:** 𝒪_blind(C-0) = {O-1, O-2}. O-3 separates already in C-0
  (fluctuations build up from 0 under noise but decay under the deterministic flow), so it counts
  **only** as higher-order data.

## §2 Theorem obligations (direction §8), required in §4 for each candidate

- **T1:** d/dt 𝔼[x | x₀] and where the noise enters, derived for the exact form. Multiplicative noise
  changing the mean is **not assumed.**
- **T2:** the 𝒟 hierarchy under M1 and M2, and the first observable in {O-1, O-2, O-3} where they
  differ.
- **T3:** prove or kill *"if 𝒮 and 𝒟 have identical one-time distributions for all t, the
  discriminator is impossible."*
- **T4:** Fokker–Planck vs Liouville. Show where the diffusion term reaches (or fails to reach) the
  𝒪_blind observables.

## §3 Grades, per-candidate labels and gate rule (frozen)

**Per-candidate grades** (direction §7), read on **𝒪_blind** under M1 **and** M2:

| Grade | Meaning |
|---|---|
| IDENTITY-DISTINGUISHABLE | a theorem shows 𝒮 ≠ 𝒟 on an 𝒪_blind observable for every nonzero noise strength in the class, and under M2 for every admissible ν. Declared non-degeneracy conditions (e.g. β > 0, a ≠ 0) must be stated. |
| PARAMETER-REGIME-DISTINGUISHABLE | the difference holds only in a defined region or beyond a threshold |
| SECOND-ORDER-EQUIVALENT | 𝒪_blind is equivalent, and only O-3 or higher separates |
| OBSERVATIONALLY-EQUIVALENT-IN-CLASS | every frozen observable is reproducible by an M2 ensemble |
| SECTOR-SMUGGLED | the separation needs a change of drift, readout or convention (D-3) |
| UNFORMULABLE | no fair common comparison exists |

**Gate outcome** (the first matching item decides; per-candidate labels are always reported):
1. **UNFORMULABLE:** no candidate admits a fair common comparison.
2. **MINIMAL-CLASS-FOUND:** a candidate with **no new undeclared ingredient, or the fewest** (D-1) is
   **IDENTITY-DISTINGUISHABLE** on 𝒪_blind under M1 and M2, with the firewall respected. The
   per-candidate pattern is recorded as a sub-label (for example, the others equivalent).
3. **REQUIRES-NEW-PARENT:** every candidate that separates on 𝒪_blind needs structure not already
   present or minimally extendable.
4. **CLASS-SPLIT:** some candidates separate on 𝒪_blind (only PARAMETER-REGIME, or only under M1), and
   the others are equivalent.
5. **ONLY-HIGHER-ORDER-DISTINGUISHABLE:** all candidates are equivalent on 𝒪_blind, and some separate
   on O-3 beyond the control-class separation.
6. **NO-DISCRIMINATOR-IN-DECLARED-CLASSES.**

**Branch.** Only if item 2 fires, or item 4 fires with a clean executable candidate: draft
`S2_NOISE_ORIGIN_CHARTER_01.md`, then HARD STOP.

**Fences:**
- No simulation or RNG.
- No Hamiltonian-bath comparison in this phase.
- No S-3, S-6, S5-WB/OD.
- No gravity, Π₀ or cosmology.

## §4 Audit

**Method.**
- Theorem-first work by the auditor.
- An **independent adversarial verifier** checked the five load-bearing claims, read-only, using
  symbolic sympy on generic 2- and 4-site chains with symbolic K, β, T and a. Its scratch scripts are
  in the session scratchpad.
- No declared member was evaluated. No simulation and no RNG.
- **Verifier verdicts:**
  - Claims 1, 3 and 5 were **qualified**.
  - Claim 2 was **confirmed exactly**.
  - Claim 4 was **refuted as first worded**; it is corrected below.
- All corrections are applied in this section.

### §4.1 Theorem LD (linear canonical drift closes the conditional mean)

**Statement.** Suppose the canonical (Itô) drift is linear, f_can(x) = −Mx, and the noise term is a
**true** zero-mean martingale. That covers:
- an Itô integral ∫G(x)dW that does not explode, with 𝔼|x_t| < ∞ and 𝔼∫|G(x_s)|²ds < ∞;
- a compensated, zero-mean Lévy term with finite first moment.

Then 𝔼[x(t) | x₀] = e^{−Mt}x₀ = φ_t(x₀) exactly.

**Proof.** 𝔼x(t) = x₀ − M∫₀ᵗ𝔼x(s)ds.

**Consequences.**
- **O-1:** m₁(t; a) is identical for 𝒮 and 𝒟, under M1, and under M2 with ν = δ₀.
- **O-2:** 𝔼_π[x₁(τ)x₁(0)] = (e^{−Mτ}Σ_π)₁₁ = 𝒟's value from π. This uses the Markov property and
  needs π to have second moments.

**Control rule re-verified.**
- **C-0 is blind on {O-1, O-2}**, by LD, F-5 and S-1.
- **O-3 separates in C-0:** the conditional variance grows from 0 under noise, while under 𝒟 any
  hidden spread decays to 0 (the drift is Hurwitz).
- So 𝒪_blind(C-0) = {O-1, O-2}, as declared. ✓

### §4.2 Per-candidate audit (T1–T4)

**C-A (multiplicative, linear drift).**
- **T1.** Itô: 𝔼[G_a x dW] = 0, so **G never enters the mean directly.** Stratonovich:
  f_can = −(K − ½ΣG_a²)x, which is still linear (matrix square; verified symbolically).
- **LD ⇒ 𝒪_blind noise-blind** against f_can, whatever the convention.
- **Firewall:** comparing against the Stratonovich drift gives exactly the conversion term ½ΣG_a²x.
  That is **SECTOR-SMUGGLED (convention)** and not evidence.
- **O-2 is degenerate:** 0 is a fixed point, so π is typically δ₀ or has no second moments.
- **T3 is not vacuous here** (P₀ = δ₀ gives identical laws), but it is moot, since 𝒪_blind is already
  blind.
- **Label: SECOND-ORDER-EQUIVALENT** (𝒪_blind equivalent by identity; only O-3 separates, as in the
  control).

**C-C (colored noise).**
- With linear f, the enlarged state (x, η) has a linear drift, so **LD applies on the enlarged space**
  (D-5). 𝒪_blind is equivalent, with η(0) part of the shared initial law.
- A separation seen only on the x-marginal (O-2 via η–x correlation) is an artefact of restricting
  the state space. It is **SECTOR-SMUGGLED (state space)** if claimed.
- With nonlinear f, any separation comes from the C-B mechanism, at a higher price.
- **Label: SECOND-ORDER-EQUIVALENT** (linear drift). It is not minimal.

**C-D (non-Gaussian additive).**
- The canonical drift is linear (zero-mean jumps), so **LD applies**, and 𝒪_blind is equivalent.
- Only higher cumulants separate, and O-3 separates in the control anyway.
- It needs a new, undeclared ingredient (the increment law).
- **Label: SECOND-ORDER-EQUIVALENT.**

**C-B (L0-1c cubic drift + L0-1e additive noise).**
- **Convention-free:** the noise is additive, so Itô = Stratonovich.
- **No new ingredient** (D-1).
- **T1.** d/dt 𝔼[x | x₀] = −K𝔼x − 4β𝔼[x^{∘3}], with 𝔼x_i³ = (𝔼x_i)³ + 3𝔼x_i·Var x_i + κ₃. **The noise
  enters the mean through the cubic moment coupling.**
- **T2 (M1), a short-time identity, verifier-CONFIRMED:**

  m₁^𝒮(t; a) − φ_t(a·e₁)₁ = (t²/4)·Q:∇∇f₁ = **−12βT₁a·t² + O(t³)**

  - Next term (verifier): +4βT₁a(44βa² + 5K₁₁)t³.
  - **Conditions:** β ≥ 0 makes |x|^{2p} a Lyapunov function, so all moments are bounded. The
    remainder needs sup_{s≤t}𝔼|x_s|⁷ < ∞, which holds.
  - **Nonzero iff β > 0, T₁ > 0 and a ≠ 0.**
- **T2 (M2, the response map; verifier-CONFIRMED with a moment condition).** For hidden ν
  independent of a, with **finite 7th moments**:
  - O(t⁰) gives 𝔼ξ₁ = 0.
  - At O(t), the coefficient difference is −12βa𝔼ξ₁² − 4β𝔼ξ₁³ − K₁₂𝔼ξ₂, which is affine in a. Two
    distinct a force ξ₁ = 0 a.s., and then 𝔼ξ₂ = 0.
  - At O(t²), the difference is c = K₁₂(4β𝔼ξ₂³ + K₂₃𝔼ξ₃), which is **independent of a**, whereas 𝒮
    needs −24βT₁a.
  - **Two distinct preparations make matching impossible.** ∎
- **Single-preparation caveat** (verifier-strengthened): for **one** a, a **Dirac shift**
  ξ = −24βT₁a·e₃ matches O(t⁰), O(t) and O(t²), because f₁ does not depend on x₃.
  - **A single-preparation mean is not decisive.**
  - The discriminator is the **response map** over ≥ 2 preparations with preparation-independent
    hidden data. This is exactly the direction's "cannot be matched merely by choosing P₀".
- **Open gap (flag F-1):**
  - For ν with 𝔼|ξ| = ∞, m₁^𝒟 is undefined, so it cannot match.
  - For ν with 𝔼|ξ| < ∞ but infinite higher moments, the Taylor argument does not apply. This case is
    plausibly excluded (m₁^𝒟′(0) would diverge), but **it is not proved.**
- **T3.** For additive noise, T3's premise never holds. If the one-time laws agreed for all t, then
  d/dt𝔼|x|² would agree, but 𝒮 carries an extra tr Q > 0 (use test functions with compact support if
  moments are lacking). **T3 is vacuous for C-B**, and the response-map observable does not rely on it.
- **T4, corrected wording.**
  - ∫x_i∂_a∂_b(Q_ab P) = 0 for any Q(x). **The diffusion term never acts on d/dt⟨x⟩ directly.** It
    reaches the mean only through ⟨f(x)⟩ ≠ f(⟨x⟩).
  - *Corrected:* the S-1 equivalence on 𝒪_blind breaks when **curvature in some component that
    feeds x₁ (directly or through the chain) is reached by the noise spread.** It is not only
    curvature "along the retained component".
  - Verifier counterexample: curvature only on x₂ gives a separation at O(t⁴), even with noise only
    on x₂. In C-B every site is cubic, so this is immaterial here.
- **Label: IDENTITY-DISTINGUISHABLE** on O-1:
  - under M1, fully;
  - under M2, for every ν with finite 7th moments;
  - with non-degeneracy conditions β > 0, T₁ > 0, a ≠ 0, and ≥ 2 distinct preparations.
  - The heavy-tail gap is flag F-1.

### §4.3 Structural answer (direction §9)

> **The S-1 equivalence breaks in C-B, and the breaking ingredient is the curvature of the canonical
> drift** (nonlinear moment coupling) reached by the noise spread.

- **Not "stochasticity itself".** The controls (C-0, C-A, C-C, C-D) show that noise type alone —
  multiplicative, colored or non-Gaussian — cannot reach 𝒪_blind while the canonical drift is linear
  (Theorem LD).
- **Not the Itô/Stratonovich conversion,** which the firewall excludes.
- **Conditional on the declared L0-1c drift.** Per S-5, that drift is itself a supplied premise.

## §5 Outcome

**Mechanical application of §3:**
1. **UNFORMULABLE:** no.
2. **MINIMAL-CLASS-FOUND:** **C-B**.
   - It has 0 new ingredients.
   - It is **IDENTITY-DISTINGUISHABLE** on O-1 under M1, and under M2 for finite-moment ν.
   - The firewall is respected (additive noise).

> **S2-0 OUTCOME (proposed): MINIMAL-CLASS-FOUND: C-B (L0-1c cubic drift + L0-1e additive noise).**
> - **Per-candidate pattern (sub-label):** C-A, C-C and C-D are SECOND-ORDER-EQUIVALENT by Theorem LD.
>   That is the CLASS-SPLIT pattern, recorded but not the terminal, because item 2 precedes item 4.
> - **The discriminator** is the retained **mean response map** over ≥ 2 preparations, at lowest order
>   (O-1). The effect is −12βT₁a·t², which a preparation-independent hidden initial law cannot
>   reproduce.

**Flag F-1 (owner ruling needed).** D-5 admitted an "arbitrary" ν. The M2 no-go is proved for ν with
finite 7th moments; heavy-tailed ν with finite mean is open. Two options:
- **(a)** Rule that admissible ν must have finite moments of the order needed, i.e. the same
  regularity class as 𝒮's own preparation, which has all moments. Then item 2 fires as stated.
- **(b)** Keep ν arbitrary. Then the heavy-tail gap becomes a mandatory theorem obligation (T-HT) of
  S2-1, and the terminal is **MINIMAL-CLASS-FOUND, conditional on T-HT.**

The S2-1 charter draft covers both.

**Other items for the owner:**
- **F-2:** the T4 wording correction (the verifier's counterexample).
- **F-3:** C-A's O-2 is degenerate and its T3 is non-vacuous. Both are moot for the outcome.

**Scope.** First-gate comparison only: the deterministic initial ensemble on the same Markov state
space. **The Hamiltonian-bath (enlarged deterministic) comparison is deferred**, per the direction.
Nothing here says noise is primitive. It says only that, in C-B, primitive forcing leaves response
structure that preparation-independent initial uncertainty cannot reproduce.

**Branch.** Item 2 fires, so `S2_NOISE_ORIGIN_CHARTER_01.md` is **drafted, not frozen and not run.**
**HARD STOP.**
