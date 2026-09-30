# S6 — OWNER RULING 02 (S6-1 accepted; LS-1/2/3 banked; O-6 additive correction; S-6 closed; SYN-0 opened)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5915173769`**. Records reviewed:
- charter `fbd15c8`;
- verified theorem block `122928a`;
- pre-run script `84e244d`;
- single result and verdict `3753210`.

The comment is authoritative; this file records it.

## 1. Primary: **S6-1 = NET-ARROW-CONFIRMED** (accepted at the frozen scope)

> **In the declared infinite conservative pinned chain, the integrated bath-self-energy transfer and the
> reduced-state entropy-reference measure retain a net forward direction despite arbitrarily late microscopic
> backflow.**

**Bath-self-energy transfer.** Forward X_J(∞) = ±[(T_s − T_b) + ½T_b r²], with r = (2.3 − √1.29)/2.

| Pair | Forward X_J(∞) |
|---|---|
| (2, 1) | 1.16943 |
| (10, 1) | 9.16943 |
| (1/2, 1) | 0.33057 |
| (1/10, 1) | 0.73057 |

**Entropy-reference measure.** X_σ(∞) = D(0) > 0 at all four pairs.

**So T-1 and T-2 are TRUE for every member.**

## 2. Secondary: **NO-ERASURE-ON-OPEN-MEMBERS** (accepted)

**Proved.**
- X_J(T) > 0 for all T > 0 on (2, 1) and (10, 1).
- X_σ(T) > 0 for all T > 0 on (1/2, 1) and (1/10, 1).

**The protocol is accepted:**
- a certified small-T Taylor region;
- deterministic interval certification of the whole main region;
- analytic tail positivity beyond the formula-derived T\*.

No box was left unresolved, and the resource limits were not exhausted.

**The controls (J on L2, σ on L1) start in the wrong direction.** They do **not** satisfy K-2 ("never erased from
switch-on"), even though their net K-1 direction is positive. **K-1 and K-2 must not be blurred.**

## 3. Provenance: accepted

The chain ran charter → verified theorem → committed script → one execution → result and verdict.
- VC-1 and VC-2 came before the script was committed and before the execution.
- All P-7 checks pass, and defects = [].
- **No rerun is needed or authorized.**

## 4. LS-1: return to equilibrium, **theorem-grade**

> S₁(t) → S_ref = T_b·diag(r, 1), with r = (K_∞⁻¹)₁₁.

**Mechanism:**
- the global Gibbs covariance at T_b is invariant;
- the declared initial product state differs from it by a finite-rank deviation;
- the spectrum is purely absolutely continuous (no bound state);
- the spectral weights are L¹;
- Riemann–Lebesgue decay applies to every retained deviation element.

**Banked at the S6 parent scope.**

## 5. LS-2: closed forms, **theorem-grade**

**Bath self-energy.** X_J(∞) = (T_s − T_b) + ½T_b r², in the record convention.
- **The offset ½T_b r²** is the correlation / interaction-energy bookkeeping. It stays attached to every
  interpretation of J.
- J remains the **bath self-energy flux**, not a unique heat current.

**Entropy reference.** X_σ(∞) = D(0) > 0 for every declared non-equilibrium pair.

## 6. LS-3: entropy tail, accepted

**The leading forms are**

> D = t⁻⁶P + O(t⁻⁷),  Ḋ = t⁻⁶P′ + O(t⁻⁷).

- **p₄,₀ > 0** for all positive T_s, T_b. So P is non-constant, and Ḋ **changes sign at arbitrarily late times**,
  with envelope t⁻⁶ (not t⁻³).
- This **strengthens** O-6's qualitative conclusion.

## 7. Additive O-6 correction: authorized

**Create `L0_1G_CORRECTIONS_01.md`, stating:**
1. The O-6 phrase "t⁻³ sign-alternating ripples" for Ḋ is correct as a loose O(t⁻³) bound, but not as the leading
   power.
2. S6-1 proves D = t⁻⁶P + O(t⁻⁷) and Ḋ = t⁻⁶P′ + O(t⁻⁷).
3. P is non-constant, so late sign reversal survives.
4. **No O-6 terminal changes.**

**Constraints:**
- Do not rewrite the original O-6 ruling or its historical records.
- **O-6 stays FALSIFIED** for strict pointwise / whole-window ordering.

## 8. Synthesis of S-6

**Pointwise arrow: NO. Integrated/net direction: YES.** In detail:
- reversals recur arbitrarily late (band-edge memory);
- the tails are absolutely integrable, so total backflow is finite;
- the integrated direction is positive on every member;
- on the four direction-matched targets, progress is never completely erased.

**Status:** this is a genuine coarse-grained arrow result. It is **not** a restored Lyapunov function.

> **Irreversibility need not mean pointwise monotonicity.**

## 9. Fences

**Do not claim any of the following:**
- microscopic reversibility is broken;
- a fundamental thermodynamic arrow has been derived;
- O-6 is repaired;
- every instantaneous flux points forward;
- J is a unique heat current;
- coarse-graining itself has been dynamically derived.

**Scope of the arrow:** it is **integrated / ensemble / preparation-relative**, and specific to the declared
initial asymmetry and observables.

## 10. Close S-6

**Create:**
- this ruling;
- the banner in `S6_1_VERDICT_01.md`;
- `S6_COARSEGRAINED_ARROW_DEPOSIT_01.md`;
- `L0_1G_CORRECTIONS_01.md`;
- the CURRENT_STATE update.

**Deposit:**
- S6-0 = PRINCIPLED-COARSE-ARROW-TEST-FOUND;
- S6-1 = NET-ARROW-CONFIRMED, with secondary NO-ERASURE-ON-OPEN-MEMBERS.

**S-6 is CLOSED. No S6-2.**

## 11. Not selected

- **S-7 and S-8** are not selected. They are legitimate, but the floor records them as not the priority front.
- **S-4** is preserved but not selected, because it would repair an already-failed hypothesis.
- **Why synthesis now:** S-1, S-2, S-3, S-5 and S-6 have been attacked deeply enough that synthesis is now worth
  more than another local fork.

## 12–14. Next: SYN-0, the GRUT working-theory synthesis

**Scope of the campaign:**
- read-only;
- file `GRUT_WORKING_THEORY_SYNTHESIS_01.md`;
- **no new physics, no gap-filling equations, no v4 exception, no numerical run.**

> **Central question: what is the strongest coherent theory GRUT can honestly state today, using only accepted
> results, with every supplied primitive, conditional emergence, falsified route and unresolved frontier made
> explicit?**

**Ledgers.**

| Ledger | Content |
|---|---|
| **A — primitive / supplied** | At minimum: the static substrate (K-type); the Level-0 temporal generator choice; the physical quantum lift; ℏ; the outcome-selection rule; the gravitational branch/coupling choice; the physical bath/noise origin beyond unrestricted path-space realization. Each entry cites the ruling that leaves it supplied. |
| **B — earned / derived** | Accepted results only. At minimum: gap → memory; passivity → positivity; locality → geometry; the nonlinear admissible relaxation class; the observability/access theorem; SF-1 sector-conditioned law formation; S5-1 controlled underdamped Markov emergence; the S2-1 nonlinear noise discriminator; S6-1 return to equilibrium and the integrated coarse arrow. |
| **C — conditional emergence** | Separates what is derived from the GRUT core from what is derived only after a supplied parent, sector or lift is admitted. |
| **D — failed / blocked** | At minimum: ℏ emergence failure; outcome selection / Born weights; gravity underdetermination; the Π₀ frontier block; reversal/self-duality NOT SUPPORTED; strict pointwise arrow falsified; physical-noise origin unresolved; unique lift failure. **Terminals are not softened.** |
| **E — minimal architecture** | The smallest directed architecture consistent with the record. **The dead reversal diagram must not be imposed.** The candidate form below is to be *audited*, not assumed. Every arrow is marked DERIVED / CONDITIONAL / SUPPLIED / BLOCKED / FALSIFIED-NON-IMPLICATION. |

The candidate architecture to audit is substrate + generator + state/sector + environment + physical lift →
effective observables/laws.

**Deliverable: answer four questions.**
1. **What is GRUT now:** a fundamental theory, an EFT or constitutive framework, a theory-construction program, or a
   scoped combination?
2. **What does it actually explain or derive?**
3. **What must still be assumed?**
4. **Which single unresolved primitive is most valuable to attack next?** This is analysis only, **not an
   authorization.**

**HARD STOP after the synthesis.**

**Not authorized:**
- S-7 or S-8;
- S-4;
- a new bath;
- reopening gravity or Π₀;
- a new quantum route.
