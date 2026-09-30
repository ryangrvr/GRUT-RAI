# S2 — OWNER RULING 01 (S2-0 terminal; S2-1 pre-freeze review; one exact execution authorized)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5905401028`**, after review of
`8e1c8e7` (pre-registration) and `47a9a7b` (audit and draft charter). The comment is authoritative;
this file records it.

## 1. F-1: option (b). M2 stays ARBITRARY

- The hidden law ν stays **arbitrary**, as pre-registered, subject only to preparation-independence.
  M2 is **not** retroactively restricted to finite 7th moments.
- The finite-moment no-go does not meet the frozen IDENTITY-DISTINGUISHABLE grade, which needs every
  admissible ν. So **MINIMAL-CLASS-FOUND is NOT ADOPTED yet.**
- *This is a pre-registration ruling, not a negative physics ruling.*

## 2. S2-0 terminal: CLASS-SPLIT (accepted)

> **C-B is theorem-level distinguishable on the retained mean response under M1, and under M2 for
> preparation-independent hidden laws with the required finite moments; arbitrary-M2 remains open.
> C-A, C-C and C-D remain equivalent on the frozen control-blind observables at their audited
> scopes.**

- This is frozen item 4: a clean candidate separates, but not yet at the full M2 grade.
- **Accepted now, at theorem scope** (C-B, M1):

  m₁^𝒮(t; a) − m₁^𝒟(t; a) = −12βT₁a·t² + O(t³).

- **Accepted structural reading:**

  > **The S-1 equivalence breaks when noise-generated spread reaches curvature of the canonical drift
  > that can feed the retained observable.**

  - Do not shorten this to "nonlinearity always makes noise observable".
  - The result is conditional on the declared L0-1c drift, a supplied premise.

## 3. F-2: the corrected T4 wording is ACCEPTED

- ∫x_i∂_a∂_b(Q_ab P) = 0 under the boundary and integrability conditions, so noise reaches the mean
  only through 𝔼f(x) ≠ f(𝔼x).
- **The relevant curvature need not be at site 1.** The verifier's counterexample is carried as the
  reason the old wording is retired.

## 4. F-3: ACCEPTED

- **C-A:**
  - O-1 is noise-blind given the canonical Itô drift.
  - O-2 can be degenerate.
  - T3 is non-vacuous there, but that does not change the outcome.
- **Scope of the SECOND-ORDER-EQUIVALENT label:** read it **narrowly**, as *equivalent on the frozen
  O-1/O-2 at the audited scope.* It does not claim all multiplicative-noise second-order statistics
  are equivalent (O-3 can differ). The same discipline applies to C-C and C-D.

## 5. T-HT is MANDATORY in S2-1

**Setting:** the comparator x(0) = a·e₁ + ξ, with ξ ~ ν independent of a, and the O-1 mean defined.
S2-1 must do one of the following:

| Route | What it requires |
|---|---|
| **HT-A** | Matching the C-B response for all frozen preparations on some 0 ≤ t < ε **forces** enough integrability for the finite-moment no-go. |
| **HT-B** | A **moment-free** no-go: no admissible preparation-independent ν reproduces the response map across the frozen preparations. |
| **HT-C** | An explicit admissible heavy-tailed ν that reproduces the **full response map** across all frozen preparations on a nonzero interval. |

- Finite Taylor matching is **not** HT-C.
- Failing to prove HT-A or HT-B is **not** evidence for HT-C.

## 6. S2-1 charter: APPROVED WITH AMENDMENTS

- **OR-1:** arbitrary M2; T-HT mandatory.
- **OR-2:**
  - **n_max = 4.**
  - The **full** member set: β ∈ {0, 0.03, 0.1, 0.3, 1, 3}; a ∈ {±0.001, ±1, ±3}; the OR-4 profiles.
  - Symbolic derivation first, then exact instantiation. No sweep and no numerical integration.
- **Normalization (mandatory).** With c_n = (𝓛ⁿx₁)(a·e₁) and m₁(t) = Σ c_n tⁿ/n!:

  | | Dynkin coefficient | Coefficient of tⁿ |
  |---|---|---|
  | n = 2 | **Δc₂ = −24βT₁a** | **−12βT₁a** |
  | n = 3 | **Δc₃ = 24βT₁a(44βa² + 5K₁₁)** | **4βT₁a(44βa² + 5K₁₁)** |

  This applies consistently to §0, E-4 and the terminals. **A factorial mismatch must not become a
  false integrity failure.**
- **OR-3:** no finite-window remainder bound. Stay at exact local/Taylor grade. A nonzero exact
  derivative mismatch at t = 0 (with the stated regularity) is enough.
- **OR-4: the profiles, exactly:**
  - **F** (T_i = 1): the primary member.
  - **G(∞)** (T₁ = 0): the downstream control. **Δc₂ = 0 is an integrity identity.** Report the
    first nonzero order ≤ 4 **without pre-registering its sign or value.**
  - **GR(∞)** (hot retained site, reversed): the orientation/locality control. Test whether the
    leading coefficient follows T₁ independently of remote orientation. **No downstream threshold
    claim.**
  - No finite-R sweep.

## 7. S2-1 frozen outcome set

| Outcome | Condition | Meaning |
|---|---|---|
| **RUN VOID** | a frozen exact-arithmetic or integrity identity fails | Preserve the artifact. No re-run without a ruling. |
| **FULL-DISCRIMINATOR-CONFIRMED** | (1) the coefficient identities and controls pass; (2) the finite-moment M2 no-go is reproduced; (3) **T-HT closes by HT-A or HT-B**; (4) no arbitrary preparation-independent ν reproduces O-1 across the frozen preparations | *Primitive forcing in C-B leaves retained mean-response structure that no deterministic initial ensemble on the same state space can reproduce.* This is **not** proof that noise is ontologically primitive. |
| **FINITE-MOMENT-DISCRIMINATOR-CONFIRMED** | the identities and the finite-moment theorem pass; T-HT is unresolved | A valid partial terminal. |
| **ARBITRARY-M2-COUNTEREXAMPLE** | HT-C succeeds | The full discriminator is refuted. **The finite-moment result is not erased.** |
| **COEFFICIENT/CONTROL-REFUTED** | the coefficient identity or the finite-moment theorem fails, without an implementation defect | |

## 8. Execution order

1. Write the analytic derivation, **including T-HT**, before any instantiation script.
2. Commit it.
3. Commit `calc/s2_noise_origin.py`.
4. Run it **once**.
5. Write the result and verdict.
6. HARD STOP.

The script is an instantiation and verification instrument, **not the source of the heavy-tail
theorem.** No RNG, no SDE simulation, no stochastic trajectories.

## 9. The v4 exception (S2-1 only)

**ONE S2-1 ANALYTIC / EXACT PHYSICS EXECUTION** is authorized once the amended charter is frozen.

**Covered:**
- the T-HT attempt;
- exact Dynkin derivation through n = 4;
- exact instantiation for F, G(∞) and GR(∞);
- the finite-moment M2 proof;
- the single script run;
- the result and verdict.

**Not covered:**
- RNG or simulation;
- a second run;
- a Hamiltonian-bath comparison;
- changing the drift or noise after the freeze;
- S-3 or the reversal diagnostic;
- S-6;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

## 10. Interpretation fence

Even FULL-DISCRIMINATOR-CONFIRMED allows at most:

> **Within the declared nonlinear C-B class, ongoing primitive forcing is observationally
> distinguishable in the retained mean-response map from uncertainty confined to the initial
> condition on the same deterministic state space.**

It does **not** establish:
- fundamental noise in nature;
- that GRUT requires ontologically primitive randomness;
- that enlarged deterministic baths cannot reproduce the same reduced process;
- quantum outcome selection;
- Born probabilities.

## 11. Actions

- Create this ruling.
- Add a banner to the S2-0 file, preserving the proposed MINIMAL text.
- Record S2-0 = CLASS-SPLIT.
- Amend and freeze the charter, and record its hash.
- Execute per §8.
- Then HARD STOP.

> **Objective:** test whether the first failure of the S-1 equivalence survives even when the
> deterministic alternative is allowed arbitrary preparation-independent hidden initial uncertainty.
