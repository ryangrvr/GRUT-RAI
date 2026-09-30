# S6-0 — COARSE-GRAINED ARROW 01 (formulation/audit gate only)

**STATUS: PRE-REGISTERED.**
- §§0–3 are frozen at the commit that introduces this file, **before any candidate measure is
  evaluated and before the O-6 records are re-inspected for this gate**.
- The audit (§4) and the assignment (§5) are appended later, in separate commits.

**Authority:** `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_OWNER_RULING_01.md` §§8-15 (Issue #2 comment
`5913714570`). **All candidate measures below are the ruling's own (§10); none is invented here.**

**Scope of this gate:**
- audit only;
- no physics run, no v4 exception, no RNG;
- no numerical evaluation of members;
- abstract symbolic reasoning only.

**Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Question

> **Can the already-declared conservative pinned-chain parent (O-6) exhibit a threshold-free,
> mathematically principled coarse-grained temporal arrow, even though band-edge memory destroys
> strict pointwise ordering?**

**Background:**
- **O-6 is FALSIFIED for its strict charter.** Band-edge memory gives infinitely many sign reversals.
- **S-6 is the question O-6 preserved:** whether a coarse-grained arrow survives.

**Interpretation fence (ruling §14).** A positive result means only:

> **net/integrated directional transport survives despite arbitrarily late microscopic backflow.**

It does not restore any of these:
- strict Lyapunov ordering;
- pointwise monotonicity;
- a fundamental thermodynamic arrow;
- O-6;
- the reversal hypothesis.

## §1 Definitions (frozen)

### 1.1 Parent and observables

**Parent.** The declared O-6 conservative pinned chain, with its declared split, its declared initial
ensemble and its declared temperature pairs. The audit locates and cites them.

**Observables.** The **declared** O-6 observables, which the audit locates:
- **J(t):** the signed energy/heat flux;
- **Ḋ(t):** the reduced relative-entropy derivative.

If either is not fully declared (definition, sign, and which subsystem it belongs to), the audit
reports it as undefined (ruling Q1).

### 1.2 Orientation (fixed before evaluation)

"Forward" is the direction fixed by the **declared initial hot/cold ordering**. Each observable is
oriented so that forward transport is positive:
- **J:** J > 0 means energy flows from the initially hotter subsystem to the initially colder one.
- **Ḋ:** the forward-oriented entropy observable is σ := −Ḋ. So σ > 0 means the reduced relative
  entropy is decreasing.

**Governing rules:**
- If the record's own sign convention differs, **the record's convention is translated into this
  orientation**; it is never re-chosen per result.
- If the record declares no hot/cold ordering for a member (for example, equal temperatures), that
  member has no orientation and is excluded, and the exclusion is reported.

### 1.3 Primary object: the recurrence-free N → ∞ limit

- **Primary object.** The recurrence-free N → ∞ object is the one the O-6 record declares (for
  example, the admitted L-N limit).
- **Finite-N guarded windows** may be used **only** as cross-checks, never as the definition (ruling
  Q4).
- **Missing object.** If no N → ∞ object is declared for J or Ḋ, the audit reports it (Q2).

### 1.4 Integrated quantities

For a forward-oriented observable f (f = J or f = σ):

| Symbol | Definition |
|---|---|
| X_f(T) | ∫₀ᵀ f dt |
| A_f(T) | ∫₀ᵀ \|f\| dt |
| f⁻ | max(−f, 0) |
| B_f(T) | ∫₀ᵀ f⁻ dt / A_f(T), defined when A_f(T) > 0 |
| X_f(∞), A_f(∞), B_f(∞) | the limits as T → ∞, **where they exist** |

**Identity (frozen):** B_f(T) < 1/2 ⟺ X_f(T) > 0.

### 1.5 Candidate criteria (from ruling §§10-11; each classified separately)

| # | Criterion | Statement |
|---|---|---|
| **K-1** | asymptotic dominance | B_f(∞) < 1/2, equivalently X_f(∞) > 0, given that A_f(∞) is finite and positive |
| **K-2** | no complete erasure | X_f(T) > 0 for all T > 0 (equivalently B_f(T) < 1/2 for all T > 0). This is the ruling's "cumulative progress never completely erased". |
| **K-3** | normalized drawdown | worst drawdown divided by net rise, compared with a chosen level. **It counts as threshold-free only if the audit derives the comparison level from an identity**, not from a chosen tolerance (ruling §10 D). |

Each of K-1, K-2 and K-3 is evaluated for **f = J** and for **f = σ**, and the two results are reported
separately. **Agreement between the heat measure and the entropy measure is not assumed.**

### 1.6 Criterion classes

Each (criterion, observable) pair is placed in exactly one class. Classes are checked in this order,
and the first that applies is assigned.

| Class | Definition |
|---|---|
| **UNDEF** | A load-bearing object is not declared. Examples: J or Ḋ undeclared; no orientation; no N → ∞ object; A_f(∞) infinite or zero, making B_f(∞) undefined. |
| **NEEDS-CG** | Defining the criterion needs an undeclared smoothing kernel, window, blocking scale or other coarse-graining (ruling Q3). |
| **ARBITRARY** | The criterion's truth condition contains a free tolerance or scale not fixed by an identity. |
| **DECIDED** | The criterion is threshold-free and needs no new coarse-graining, and its truth value **follows from accepted O-6 identities and asymptotics**, plus general facts that hold on the declared parent. Examples of such facts: energy conservation, absolute integrability of a declared tail, and the identity in 1.4. The value (TRUE/FALSE) is reported. **The independent verifier must confirm it.** |
| **EXECUTABLE** | The criterion is threshold-free and needs no new coarse-graining, but its truth value is **not** fixed by accepted identities. Settling it needs an exact analytic derivation or an exact finite-member evaluation, which is not performed at this gate (ruling Q7). |

### 1.7 Asymptotic audit (ruling §11; done before any classification)

**Question:** is the declared tail f(t) ~ t⁻³ × (oscillatory) **absolutely integrable**, and is A_f(∞)
therefore finite?

**If yes, the audit records the consequences** (abstract mathematics, not evaluation):
- the total late-time backflow is finite;
- B_f(∞) is well defined when A_f(∞) > 0;
- infinitely many sign reversals do **not** imply B_f(∞) = 1/2;
- K-1 reduces to the sign of the finite integrated imbalance X_f(∞).

**The audit also checks:**
- whether the early-time behaviour, including t → 0, keeps A_f finite;
- whether the tail exponent and form are actually declared for J and for σ, or only for one of them.

## §2 Per-object audit template (frozen)

Every answer carries a file:line citation; an uncited answer counts as undefined.
- **Q1–Q7** of ruling §12, answered in turn.
- **The declared forms of:**
  - J and Ḋ;
  - their signs and subsystems;
  - the initial ensemble and temperature pairs;
  - the N → ∞ object;
  - the tail asymptotics, with exponents and the declared prefactor structure;
  - any accepted identity involving ∫J or ∫Ḋ, such as energy balance or a relative-entropy identity.
- **Classification:** each (K, f) pair gets a class from 1.6, with its ground.

## §3 Frozen outcomes and mechanical rule

### 3.1 Outcomes (ruling §13, verbatim labels)

| # | Outcome | Predicate |
|---|---|---|
| O-1 | **PRINCIPLED-COARSE-ARROW-TEST-FOUND** | at least one (K, f) pair is EXECUTABLE |
| O-2 | **IDENTITY-DECIDED** | at least one (K, f) pair is DECIDED (value reported) |
| O-3 | **ONLY-ARBITRARY-THRESHOLDS** | every (K, f) pair that is not UNDEF is ARBITRARY |
| O-4 | **FORMULABLE-ONLY-WITH-NEW-COARSE-GRAINING** | no pair is EXECUTABLE or DECIDED, and at least one is NEEDS-CG |
| O-5 | **UNFORMULABLE** | every (K, f) pair is UNDEF |

### 3.2 Mechanical rule

1. **Primary terminal:** the first true predicate in the order O-1 … O-5 (the ruling's list order).
2. **Sub-labels:** every other true predicate. O-1 and O-2 can hold together, with some pairs decided
   and others executable. In that case every DECIDED value is reported as well.
3. **If O-1 is primary:** draft an S6-1 charter for the EXECUTABLE pair(s), and **HARD STOP before any
   run** (ruling §13).
4. **Otherwise:** HARD STOP for the owner.

### 3.3 Audit method (frozen)

- **Read-only.**
- **Two parallel auditors:**
  - **A** covers the O-6 declarations: parent, split, ensemble, J, Ḋ, signs, the N → ∞ object, the
    finite-N windows, and the preserved S-6 / O-6 review text on B and D.
  - **B** covers the asymptotics: the declared tail forms and exponents, absolute integrability,
    early-time behaviour, energy-balance or entropy identities, and the S5-1 derivation's spectral
    weights where O-6 relies on them.
- **One independent adversarial verifier** checks:
  - every DECIDED and EXECUTABLE classification;
  - every UNDEF claim;
  - the primary terminal.

### 3.4 Fences

**Not authorized:**
- an S6 run;
- S-4, S-7 or S-8;
- a new reversal diagnostic;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

**No drawdown threshold is frozen** unless an identity derives it (1.5 K-3).

### 3.5 Prior expectations (disclosed; not evidence)

These are recalled from earlier gates, not taken from inspection at this gate.

**Expectation 1: the tail is absolutely integrable.**
- The t⁻³ oscillatory tail is absolutely integrable.
- So A_f(∞) is finite and B_f(∞) is well defined.
- Therefore the recurring reversals do not force B_∞ = 1/2.

**Expectation 2: K-1 for J may be DECIDED.**
- By energy conservation, X_J(∞) equals the net energy the initially hotter subsystem loses between
  t = 0 and its asymptotic state.
- If the record fixes that asymptotic state, for example as relaxation to the bath temperature in the
  L-N limit, then K-1 for J is DECIDED.
- The coupling-energy bookkeeping may complicate this, and so may whether the retained site
  thermalizes at all. S5-1 reported non-Markovian dissipation only at g = 1.

**Expectation 3: K-2 is likely EXECUTABLE, and K-3 may be ARBITRARY.**
- K-2 depends on the early-time signs, not only on the asymptotics.
- K-3 may be ARBITRARY unless "complete erasure" (K-2) is identified as its only principled form.

**Expectation 4: the entropy observable σ may differ from J.**

**Hence the expected terminal:** PRINCIPLED-COARSE-ARROW-TEST-FOUND, with sub-label IDENTITY-DECIDED.
This must be tested, not assumed.

## §4 Audit

**How it was run.**
- §§0–3 were frozen at `fc51def`.
- Two read-only auditors: A on the O-6 declarations, B on the asymptotics and identities.
- One independent adversarial verifier, on F1–F8.
- No code was run on members. The only arithmetic was closed-form work on declared constants.

### 4.1 Provenance of the O-6 objects

**The O-6 charter was never frozen.**
- Its banner reads "DRAFT — NOT YET FROZEN" (`L0_1G_CHARTER_01.md:3-5`).
- "L0-1g is not frozen, not run" (`L0_1G_PREFREEZE_REVIEW_01.md:111`).
- O-6 = FALSIFIED was ruled from the pre-freeze review (`L0_1G_OWNER_RULING_02.md:3-16`).

**Its objects were nonetheless confirmed and reused:**
- the parent, J, S_ref and Ḋ were confirmed by the reviewer (`PREFREEZE:59-68`);
- S5 reuses them as "record definitions" (`S5_CONSERVATIVE_ORIGIN_01.md:32-40`).

### 4.2 Declarations (Q1–Q7)

**Q1. The parent, the pairs, J and Ḋ.**
- **Parent:** K_N, N ∈ {23, 47, 95}, split at site 1, with g = 1 (`CHARTER:45-53`).
- **Ensemble:** a Gaussian product of uncoupled Gibbs states (`:54-58`).
- **Temperature pairs:** L1 (2, 1), (10, 1) and L2 (1/2, 1), (1/10, 1) (`:59-61`). None has equal temperatures, so §1.2 excludes nothing.
- **J = d⟨E_B⟩/dt = g⟨p₂q₁⟩**, where E_B is the bath **self-energy**; the coupling −g q₁q₂ is excluded (`CHARTER:81-84`).
- **Ḋ** comes from D = KL(𝒩(0, S₁) ‖ 𝒩(0, S_ref)), with S_ref = T_b·diag((K⁻¹)₁₁, 1) (`:85-93`).
- **Both are declared on all four pairs** (RC-6 at `:114-118`; `PREFREEZE:53`). The strict gates used J on L1 and Ḋ on L2 only (`CHARTER:121-124`).

**Q2. The N → ∞ object is declared by reference.**
- L-N is admitted (`S5_CONSERVATIVE_ORIGIN_01.md:50`).
- K_∞ with strong convergence (`S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md:36-37,73-79`).
- D-1 names J and Ḋ on the infinite chain (`PREFREEZE:31-32`; `L0_1G_OWNER_RULING_02.md:36-38`).
- The moment formulas carry over to K_∞.
- **Caveat:** S5's L-N admission covers the bath-at-rest class C₀ only. The thermal ensemble at N = ∞ rests on the O-6 records (I-5, D-1).

**Q3. B_∞ needs no window.** X, A and B are plain integrals from 0 to T, and J_∞ exists pointwise.

**Q4. The finite-N windows.**
- They are [t_s, T_rec) (`CHARTER:69-76`), with an echo guard (`PREFREEZE:52`).
- In O-6 they *were* the definition; here they are **cross-checks only** (§1.3).
- **Mismatch:** the O-6 windows start at t_s, whereas §1.4 integrates from 0 (frozen).

**Q5. Orientation (a sign translation only).**

| Pairs | Forward J |
|---|---|
| L1 | f = +J |
| L2 | f = −J (the bath is hotter, so forward is a fall in bath self-energy) |

σ = −Ḋ for every pair.

**Q6. No threshold numbers anywhere.**
- The record never declares a backflow or drawdown threshold.
- The review proposed "worst drawdown of ⟨E_B⟩ normalized by its net rise; backflow fraction ∫J⁻/∫|J|; analogues for D" as **maps, not gates** (`PREFREEZE:55,84-89`; S-6 row at `L0_1_FLOOR_SUCCESSOR_LIST.md:20`).
- The only identity-fixed level is B < 1/2 ⟺ X > 0.

**Q7. Identities.**
- The local energy balance J = −Ė₁ − Ė_int holds exactly (verifier).
- ⟨E_int⟩(0) = 0.
- X_σ(T) = D(0) − D(T).
- I-5 is accepted (`L0_1G_OWNER_RULING_01.md:12-13`; `…_02.md:34-35`).
- D-1 is accepted as an "asymptotic identity, generic".
- **The asymptotic reduced state is NOT stated by any accepted record.**
  - `DESIGN:171-175` and `CHARTER:87-88` give it only as the motivation for choosing S_ref.
  - D-1 speaks of "its asymptote" without naming it.

### 4.3 Asymptotics (§1.7)

**J = O(t⁻³).**
- The covariance deviation e^{At}ΔX₀e^{Aᵀt} is bilinear in response elements.
- Each element is O(t^{−3/2}), from the square-root band-edge density (`S5_…_DERIVATION_01.md:92-104`, purely absolutely continuous, no bound state, `:74-77`).

**Ḋ decays faster.**
- Ḋ = O(t⁻⁶) if S₁ → S_ref, because both factors are O(t⁻³).
- **Record defect:** D-1's "likewise Ḋ … t⁻³" is a loose upper bound. It does not affect integrability.

**Near t = 0 both are entire functions**, because the spectrum is compact and S₁ ≻ 0.

**Consequences:**
- A_f(∞) is finite.
- A_f(∞) > 0, since f is analytic and not identically zero (the leading terms of I-5 are nonzero).
- **B_f(∞) is well defined.**
- **The infinitely many sign reversals do not force B_∞ = 1/2.**
- K-1 reduces to the sign of X_f(∞).

### 4.4 The limit state and X_f(∞): derived at this gate, verified sound, but not on the record

**Derivation.**
- The global Gibbs covariance T_b·diag(K⁻¹, I) is invariant under the flow.
- The declared product ensemble differs from it by a perturbation ΔX₀ of rank ≤ 3, localized on (e₁, 0), (K⁻¹e₁, 0) and (0, e₁). This follows from the Schur complement.
- The spectrum is absolutely continuous, so Riemann–Lebesgue gives **S₁ → S_ref** and ⟨q₁q₂⟩ → T_b(K⁻¹)₁₂.

**Values.** Let r := (K_∞⁻¹)₁₁ = (2.3 − √1.29)/2 ≈ 0.582, and note g(K⁻¹)₁₂ = r².

**X_J,record(∞) = (T_s − T_b) + ½·T_b·r².** The forward values are:

| Pair (T_s, T_b) | X_f(∞) |
|---|---|
| (2, 1) | ≈ 1.17 |
| (10, 1) | ≈ 9.17 |
| (1/2, 1) | ≈ 0.33 |
| (1/10, 1) | ≈ 0.73 |

**X_σ(∞) = D(0) > 0 at every pair.**

**Meaning caveat on J (verifier).** J measures the change in bath self-energy, not a unique hot → cold flux, because E_int is a third energy store.
- At T_s = T_b it still integrates to +½·T·r².
- The two L2 members come out positive only because T_s/T_b < 1 − r²/2 ≈ 0.83.

**Classification under §1.6.** DECIDED requires the truth value to "follow from accepted O-6 identities and asymptotics plus general facts". The limit state is a short **new theorem** (return to equilibrium) derived at this gate. The record never states it, and §3.5 Expectation 2 conditioned DECIDED on the record fixing it. **The strict literal reading therefore classes K-1 as EXECUTABLE** ("needs an exact analytic derivation … not performed at this gate"). The derived values above are reported as audit-derived and verifier-checked, **not as DECIDED**. The owner may rule otherwise (A-2).

### 4.5 K-2 and K-3

**K-2, from the I-5 switch-on identities (accepted):**
- J_record ≈ g²(T_s/K₁₁)·t > 0 for **every** T_s (`DESIGN:129-131`).
- D(t) − D(0) ≈ ½·g²(K_BB⁻¹)₁₁(1 − T_b/T_s)·t² (`CHARTER:111-112`; `PREFREEZE:58`; re-derived by the verifier).

| Member | X_f(T) at small T | K-2 |
|---|---|---|
| J on L2 | < 0 | **FALSE by identity** |
| σ on L1 | < 0 | **FALSE by identity** |
| J on L1 | positive at the start and in the limit; intermediate sign not fixed by the record | **EXECUTABLE** |
| σ on L2 | positive at the start and in the limit; intermediate sign not fixed by the record | **EXECUTABLE** |

The FALSE cases lie entirely inside the switch-on slip [0, t_s). They follow from §1.4's frozen integration from 0.

**K-3 (drawdown / net rise): ARBITRARY for J and σ.**
- No identity fixes a level for this ratio.
- The only identity-grounded level (running-peak normalization at 1) just restates K-2.
- "Net rise" does not fix which T it is measured at.

### 4.6 Classification table (strict §1.6 reading)

| Pair | Class | Values / members |
|---|---|---|
| K-1, J | **EXECUTABLE** | audit-derived TRUE at all four pairs (not DECIDED) |
| K-1, σ | **EXECUTABLE** | audit-derived TRUE at all four pairs (not DECIDED) |
| K-2, J | members split: **DECIDED FALSE** on L2, **EXECUTABLE** on L1 | aggregation depends on A-1 |
| K-2, σ | members split: **DECIDED FALSE** on L1, **EXECUTABLE** on L2 | aggregation depends on A-1 |
| K-3, J and σ | **ARBITRARY** | — |

### 4.7 The terminal matrix (verifier) and items for adjudication

Rows are the A-1 aggregation reading; columns are the A-2 reading of K-1.

| | K-1 DECIDED | K-1 EXECUTABLE (strict reading) |
|---|---|---|
| **(a) universal over members** | **O-2** primary (no pair is EXECUTABLE) | **O-1** primary, sub-label O-2 |
| **(b) per member** | **O-1** primary, sub-label O-2 | **O-1** primary; O-2 as a sub-label only if member-level DECIDED FALSE results count |

**Items for adjudication:**

| # | Item |
|---|---|
| **A-1** | §1.6 has no rule for aggregating members into a pair class. |
| **A-2** | §1.6's DECIDED "general facts" list is open-ended ("examples"). Does the gate-derived limit-state theorem count? |
| **A-3** | §1.2's "hot → cold flux" is not unique once E_int is a separate store. The J results carry the meaning caveat of §4.4. |
| **A-4** | §1.4 integrates from 0, not from t_s. This is why K-2 is forced FALSE on the opposite-direction members. |
| **A-5** | D-1's t⁻³ tail for Ḋ is inconsistent with S₁ → S_ref (it should be O(t⁻⁶)). This has no effect here. |

### 4.8 The prior expectations of §3.5

| # | Expectation | Outcome |
|---|---|---|
| 1 | The tail is integrable. | **Confirmed.** Correction: Ḋ decays as O(t⁻⁶). |
| 2 | K-1 for J is DECIDED. | **Not confirmed as DECIDED.** The record does not fix the limit state; it is derivable at the gate and the value is TRUE. The identity I wrote in §3.5, "E_hot(0) − E_hot(∞)", is exact only in the L2 orientation; the coupling offset ½·T_b·r² enters. |
| 3 | K-2 is EXECUTABLE. | **Partly contradicted:** it is FALSE by identity on the opposite-direction members. K-3 is ARBITRARY, as expected. |
| 4 | σ differs from J. | **Confirmed.** They differ in tail exponent, in the identity behind X(∞), and in which members fail K-2. |

## §5 Mechanical assignment

**Reading applied: strict literal §1.6** (A-2 → EXECUTABLE). Under it, **O-1 holds whatever A-1 says.** It is also the only reading in which the primary terminal does not depend on A-1.

| Predicate | Value |
|---|---|
| **O-1 PRINCIPLED-COARSE-ARROW-TEST-FOUND** | **true.** K-1 for J and for σ is EXECUTABLE and threshold-free (B_∞ < 1/2 ⟺ X_∞ > 0). No new coarse-graining is needed. The same holds for K-2 on the members J-L1 and σ-L2. |
| O-2 IDENTITY-DECIDED | **true as a sub-label under A-1 reading (a):** K-2 is DECIDED FALSE for both J and σ. Under (b) it holds only if member-level DECIDED results count. |
| O-3 ONLY-ARBITRARY-THRESHOLDS | false (only K-3 is ARBITRARY) |
| O-4 NEEDS-CG | false |
| O-5 UNFORMULABLE | false |

> **S6-0 = PRINCIPLED-COARSE-ARROW-TEST-FOUND** (proposed, mechanical, under the strict reading).
>
> **Sub-label:** IDENTITY-DECIDED (A-1-dependent). The switch-on identity I-5 makes K-2 ("no complete
> erasure") **FALSE** on the opposite-direction members J-L2 and σ-L1.
>
> **Report-only (audit-derived and verifier-checked, not DECIDED):** the reduced state relaxes to the
> reduced global Gibbs state, and **K-1 would be TRUE for both J and σ at all four declared pairs.**
> - J: X_f(∞) ≈ 1.17, 9.17, 0.33, 0.73.
> - σ: X_σ(∞) = D(0) > 0.
>
> In words: the late microscopic backflow is finite and cannot erase the net transport.

**Reading (fenced by §0).**
- **What does survive:** the record supports a threshold-free coarse-arrow test, and the audit-derived asymptotic answer is a **net integrated arrow for both heat and entropy.**
- **What does not:** the stronger criterion "progress is never completely erased" already fails at switch-on on two members.
- **None of this restores O-6.** O-6 stays FALSIFIED for its strict charter.

**Next, per §3.2(3):** `S6_1_COARSEGRAINED_ARROW_CHARTER_01.md` is drafted (not frozen) for the EXECUTABLE pairs. **HARD STOP before any run.**
