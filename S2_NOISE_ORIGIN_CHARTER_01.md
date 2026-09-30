# S2-1 — NOISE-ORIGIN DISCRIMINATOR CHARTER 01 (C-B)

**STATUS: FROZEN FOR EXECUTION** (amended per `S2_OWNER_RULING_01.md`, Issue #2 comment `5905401028`).
- **The frozen commit is the commit that introduces this revision.** CURRENT_STATE records its hash.
- **ONE S2-1 analytic/exact physics execution is authorized**, with a campaign-specific v4 exception
  for S2-1 only.
- **Draft history:** the draft is at `47a9a7b`, and the amendment log is §8.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Target

At exact (theorem/rational) grade, for **C-B**: dx = [−Kx − 4βx^{∘3}]dt + B dW, Q = BBᵀ = 2·diag(T_i),
on K = K_b.

**(a) Coefficient identities.** With c_n := (𝓛ⁿx₁)(a·e₁), 𝓛 = f·∇ + ½Q:∇∇, c_n^φ := ((f·∇)ⁿx₁)(a·e₁),
Δc_n := c_n − c_n^φ, and m₁(t) = Σ_n c_n tⁿ/n!:

- **Δc₂ = −24βT₁a**, so the coefficient of t² is **−12βT₁a**.
- **Δc₃ = 24βT₁a(44βa² + 5K₁₁)**, so the coefficient of t³ is **4βT₁a(44βa² + 5K₁₁)**.

(Dynkin coefficients versus ordinary Taylor coefficients: the factor n! is frozen here.)

**(b) T-HT (mandatory).** Decide whether any **arbitrary** preparation-independent hidden law ν on
the full state space (x(0) = a·e₁ + ξ, ξ ~ ν, with the O-1 mean defined) reproduces the C-B response
map m₁(t; a) for all frozen a on some 0 ≤ t < ε. Do this by HT-A, HT-B or HT-C (§3).

## §1 Parent and members (all declared; no new ingredient)

- **K = K_b:** the sealed 23-site bath block; rational entries 23/10 (13/10 at site 23), with
  off-diagonal −1.
- **Drift:** f_β = −Kx − 4βx^{∘3}.
- **Noise:** additive, so it is convention-free.
- **β ∈ {0, 3/100, 1/10, 3/10, 1, 3}.**
- **a ∈ {±1/1000, ±1, ±3}.**
- **Profiles** (OR-4, exactly):
  - **F:** T_i = 1;
  - **G(∞):** T_i = (i−1)/22, so T₁ = 0;
  - **GR(∞):** T_i = (23−i)/22, so T₁ = 1.
- No finite-R profile.

## §2 Execution (frozen order; exact; no RNG; no simulation; no stochastic trajectories)

1. **Analytic derivation, written and committed first** (`S2_NOISE_ORIGIN_DERIVATION_01.md`):
   - the general Δc₂ and Δc₃ at a·e₁;
   - the finite-moment M2 no-go, restated;
   - **T-HT**, by HT-A, HT-B or HT-C, with proofs.
2. **`calc/s2_noise_origin.py`, committed before its single run.** It contains:
   - **E-1:** exact symbolic 𝓛ⁿx₁ and (f·∇)ⁿx₁ for n ≤ **4** (n_max = 4) on the full 23-site K_b,
     instantiated exactly (sympy Rational) at every (β, a, profile).
   - **E-2:** a symbolic re-derivation of the finite-moment M2 coefficient algebra and of the
     ξ-independence identities that T-HT uses, on generic symbolic data.
   - **E-3:** structural checks: K_b is symmetric positive definite with non-positive off-diagonal
     (so the drift is cooperative); f is odd.
3. **One run.** Then the result, the verdict, and HARD STOP.

## §3 T-HT routes (ruling §5)

| Route | Requirement |
|---|---|
| **HT-A** | Matching on 0 ≤ t < ε for the frozen preparations forces enough integrability for the finite-moment no-go. |
| **HT-B** | A moment-free no-go: no admissible preparation-independent ν reproduces the response map across the frozen preparations. |
| **HT-C** | An explicit admissible heavy-tailed ν reproduces the **full response map** across all frozen preparations on a nonzero interval. |

- Finite Taylor matching is not HT-C.
- Failing HT-A or HT-B is not evidence for HT-C.
- **"Admissible"** means any law on ℝ²³, independent of a, **such that the O-1 mean is defined on the
  matching interval, including t = 0** (for t = 0 this means 𝔼|ξ₁| < ∞). No other moment condition
  may be assumed.

## §4 Integrity identities and controls (frozen)

| # | Identity | Kind |
|---|---|---|
| I-1 | **F:** Δc₂ = −24βT₁a and Δc₃ = 24βT₁a(44βa² + 5K₁₁), exactly, with T₁ = 1 and K₁₁ = 23/10, at every β and a | coefficient identity |
| I-2 | **β = 0:** Δc_n = 0 for n ≤ 4, at every profile and a (Theorem LD instantiated) | control identity |
| I-3 | **G(∞):** Δc₂ = 0 exactly (T₁ = 0) | control identity |
| I-4 | **GR(∞):** Δc₂ = −24βT₁a with T₁ = 1 | the "leading coefficient follows T₁" test (a coefficient identity) |
| I-5 | E-3 structural checks, and the E-2 symbolic re-derivations | integrity |

**Reported only, with no pre-registered sign or value:**
- G(∞): Δc₃ and Δc₄, and its first nonzero order ≤ 4 (if any);
- the difference between F and GR(∞) in Δc₃ and Δc₄ (the remote-orientation effect);
- all Δc_n tables.

## §5 Outcomes (frozen; ruling §7)

The first matching item decides:

1. **RUN VOID:** a frozen exact-arithmetic or integrity identity (I-1 … I-5) fails for an
   implementation reason. Preserve the artifact; no re-run without a ruling.
2. **COEFFICIENT/CONTROL-REFUTED:** a coefficient identity (I-1, I-4) or the finite-moment M2 theorem
   fails, without an implementation defect.
3. **FULL-DISCRIMINATOR-CONFIRMED:** I-1 … I-5 pass; the finite-moment M2 no-go is reproduced; **T-HT
   closes by HT-A or HT-B**; and no arbitrary preparation-independent ν reproduces O-1 across the
   frozen preparations.
4. **ARBITRARY-M2-COUNTEREXAMPLE:** HT-C succeeds. The finite-moment result stands separately.
5. **FINITE-MOMENT-DISCRIMINATOR-CONFIRMED:** the identities and the finite-moment theorem pass, but
   T-HT is unresolved.

There is **no finite-time magnitude or remainder bound** (OR-3). The result stays at exact
local/Taylor grade.

## §6 Fences (ruling §§9–10)

**Strongest allowed statement:**

> **Within the declared nonlinear C-B class, ongoing primitive forcing is observationally
> distinguishable in the retained mean-response map from uncertainty confined to the initial condition
> on the same deterministic state space.**

**Not established:**
- fundamental noise;
- that GRUT requires primitive randomness;
- that enlarged deterministic baths cannot reproduce the reduced process (the Hamiltonian-bath
  comparison is deferred);
- quantum outcome selection or Born probabilities.

**Conditional on the L0-1c drift**, a supplied premise (S-5).

**Not authorized:**
- RNG or simulation;
- a second run, or any drift/noise change after the freeze;
- S-3, the reversal diagnostic, S-6;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

## §7 Owner rulings replacing the draft's open items

| Item | Ruling |
|---|---|
| OR-1 | Arbitrary M2; T-HT mandatory |
| OR-2 | n_max = 4; the full member set |
| OR-3 | No finite-time bound |
| OR-4 | Exactly the profiles F, G(∞) and GR(∞) |

## §8 Amendment log (draft `47a9a7b` → frozen)

| # | Change | Source |
|---|---|---|
| AM-1 | M2 arbitrary; T-HT mandatory, with routes HT-A, HT-B and HT-C and the admissibility clause | ruling §§1, 5 |
| AM-2 | n_max 6 → **4**; the full member set | ruling §6 OR-2 |
| AM-3 | **Normalization frozen:** Δc₂ = −24βT₁a (t² coefficient −12βT₁a); Δc₃ = 24βT₁a(44βa² + 5K₁₁) (t³ coefficient 4βT₁a(44βa² + 5K₁₁)), consistently in §0, §4 and §5 | ruling §6 |
| AM-4 | The OR-3 finite-time bound is removed | ruling §6 |
| AM-5 | The profiles are exactly F, G(∞) and GR(∞). G(∞) has only Δc₂ = 0 frozen; the rest is reported without a pre-registered sign or value. GR(∞) tests the leading coefficient against T₁. | ruling §6 OR-4 |
| AM-6 | The outcome set is replaced by the ruling §7 set | ruling §7 |
| AM-7 | The execution order is frozen: derivation (with T-HT), then the committed script, then one run | ruling §8 |
| AM-8 | **Auditor pre-freeze note (disclosed):** Δc₃ at a·e₁ depends only on T₁, not on T₂. In 𝓛³x₁, the ½Q₂₂∂₂² term acts on f·∇f₁ and leaves only 24βK₁₂x₂, which is 0 at a·e₁. The I-1/I-4 Δc₃ identity is therefore well-posed for every profile; I-4 freezes only Δc₂ per the ruling. | pre-freeze; no member computed |
