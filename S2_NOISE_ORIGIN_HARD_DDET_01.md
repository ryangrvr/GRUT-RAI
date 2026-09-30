# S2-0 — HARD D-DET / NOISE-ORIGIN DISCRIMINATOR: formulation / class-selection gate

**STATUS: §§0–3 PRE-REGISTERED** before any candidate is evaluated. §4 (the audit) and §5 (the
outcome) will be added in a later commit.
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

*(Added in a later commit.)*

## §5 Outcome

*(Added in a later commit.)*
