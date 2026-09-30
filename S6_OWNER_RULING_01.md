# S6 — OWNER RULING 01 (S6-0 accepted; A-1 … A-5; S6-1 pre-freeze; one execution authorized)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5914432316`**, after review of the S6-0
pre-registration `fc51def`, the audit and draft charter `a9017e8`, the accepted O-6 ruling and review, and
the S5 infinite-chain spectral results. The comment is authoritative; this file records it.

## 1. S6-0 terminal: ACCEPTED

**S6-0 = PRINCIPLED-COARSE-ARROW-TEST-FOUND.** The criterion is threshold-free:

> B_f(∞) < ½ ⟺ X_f(∞) > 0.

It needs no smoothing scale, blocking scale, fitted tolerance or "mostly monotone" notion.

> **The declared conservative-chain class supports a mathematically principled test of whether net
> integrated direction survives despite arbitrarily late microscopic backflow.**

**What this acceptance does not do:**
- It does **not** bank the audit-derived positive value of K-1 (see A-2).
- It does not affect O-6, which remains FALSIFIED for strict pointwise ordering.

## 2. Provenance of the O-6 objects

The O-6 charter was never frozen. S6 may still consume the **confirmed record objects**, because the
pre-freeze mathematics review confirmed them and the accepted O-6 ruling relies on that review:
- the parent;
- the ensemble;
- J = g⟨p₂q₁⟩;
- S_ref;
- Ḋ;
- the moment derivatives.

S5 reused the same definitions.

**S6 may not inherit any unfrozen O-6 numerical gate, tolerance or window as authority.**

## 3. A-1: member aggregation (family-level, unresolved dominates)

For one pair (K, f) evaluated across its declared members, apply these rules in order:

1. If any member is UNDEF, the pair is UNDEF.
2. Otherwise, if any member is NEEDS-CG, the pair is NEEDS-CG.
3. Otherwise, if any member is ARBITRARY, the pair is ARBITRARY.
4. Otherwise, if **every** member is DECIDED, the pair is DECIDED, and the member-by-member TRUE/FALSE
   pattern is reported.
5. Otherwise the pair is EXECUTABLE, and any already-DECIDED member values are reported separately.

**Applied to S6-0:**

| Pair | Class |
|---|---|
| K-1/J | EXECUTABLE |
| K-1/σ | EXECUTABLE |
| K-2/J | EXECUTABLE (the L2 members are already DECIDED FALSE) |
| K-2/σ | EXECUTABLE (the L1 members are already DECIDED FALSE) |
| K-3/J and K-3/σ | ARBITRARY |

**Consequences:**
- **O-1 is primary.**
- **O-2 is not a formal sub-label**, because no whole pair is DECIDED.
- The member-level note is preserved instead: **"IDENTITY-DECIDED FALSE members exist for K-2."** It must
  not be relabeled as O-2.

## 4. A-2: K-1 stays EXECUTABLE

A theorem discovered and checked **during** the audit cannot convert the same gate to DECIDED.

- The return-to-equilibrium result is **REPORT-ONLY UNTIL S6-1 FORMALLY BANKS IT.**
- S6-1 must state and prove the theorem cleanly under its frozen charter.

## 5. A-3: J is the bath self-energy flux

J = d⟨E_B⟩/dt = g⟨p₂q₁⟩, where E_B is the bath **self-energy** (interaction excluded).

**Naming:**
- Its name is **bath self-energy flux / bath self-energy transfer**, not an unqualified heat flux.
- **No symmetrized flux is to be introduced.** That would be new structure.

**The J and σ claims must be kept separate:**
- **J:** net oriented bath self-energy transfer survives microscopic backflow.
- **σ:** net reduction toward the declared reduced Gibbs reference survives microscopic backflow.
- **Only σ** may be called the entropy-side coarse arrow without the J bookkeeping caveat.

**Reporting:** the equal-temperature offset **½T_b r²** is reported next to every closed-form J conclusion.

## 6. A-4: integration starts at t = 0 (kept)

X_f(T) = ∫₀ᵀ f dt, and the origin is not moved.

The two switch-on failures stand, and they answer the stronger criterion "never completely erased from
switch-on":
- K-2/J is FALSE on the L2 members;
- K-2/σ is FALSE on the L1 members.

## 7. A-5: the Ḋ tail

- **The likely correction to O(t⁻⁶) is not written into O-6 yet.** The old t⁻³ statement is enough for
  integrability.
- **S6-1 must derive the leading entropy asymptotic explicitly.** It must decide whether the O-6 wording is
  a loose upper bound or an incorrect statement of the leading power.
- **Any O-6 correction is additive** and is recorded only after that theorem is accepted.
- **No O-6 terminal changes.**

## 8. S6-1 targets (the draft is approved with amendments)

| Target | Content | Members |
|---|---|---|
| **T-1** | net bath self-energy transfer: the sign of X_J(∞), forward-oriented | all four pairs |
| **T-2** | net entropy-reference approach: X_σ(∞) = D(0) − D(∞) | all four pairs |
| **T-3** | no erasure for J | L1 (2, 1) and (10, 1) |
| **T-4** | no erasure for σ | L2 (1/2, 1) and (1/10, 1) |

- **Controls, not targets:** the opposite-direction K-2 members, which are already DECIDED FALSE.
- **Excluded:** K-3.

## 9. Mandatory analytic theorem block (before any certified evaluation)

**LS-1 — return to equilibrium: S₁(t) → S_ref.** The proof must state:
- the global Gibbs covariance at T_b;
- the finite-rank localized perturbation;
- the spectral representation;
- the absolute-continuity / no-bound-state fact consumed from S5;
- the Riemann–Lebesgue step;
- why the needed matrix elements are L¹ in the spectral variables.

It may **not** merely cite "dephasing".

**LS-2 — closed forms:**
- X_J(∞) = (T_s − T_b) + ½T_b r², in the bath-self-energy convention, with the sign reversed for L2;
- X_σ(∞) = D(0) if D(∞) = 0;
- r = (K_∞⁻¹)₁₁ = (2.3 − √1.29)/2.

**LS-3 — the leading asymptotic class of D and Ḋ.**
- It must show the quadratic expansion.
- It must give the leading oscillatory coefficient and the non-degeneracy needed for any sign-reversal
  claim.
- Power counting alone is not enough.

**T-1 and T-2 become theorem-grade only after LS-1 and LS-2 pass.**

## 10. The T-3/T-4 certification protocol (frozen before the charter freeze)

**Required elements:**
1. an exact spectral representation of X_f(T);
2. an explicit rigorous tail bound |X_f(T) − X_f(∞)| ≤ C_f T⁻², or a stronger one;
3. **T\* chosen by a formula** from that bound and the proven asymptotic margin, never by inspection;
4. deterministic interval arithmetic / Taylor-model certification of the continuum interval [0, T\*];
5. the precision, subdivision rule and stopping rule frozen before execution.

**Per-member verdicts:**
- **TRUE:** a rigorous lower bound shows X_f > 0 on all of (0, T\*], and the tail bound covers everything
  after.
- **FALSE:** a rigorous interval upper bound is negative somewhere.
- **UNRESOLVED:** the fixed resources prove neither.

**Forbidden:** adaptive plotting, ordinary float grids, or a post-hoc window.

**New secondary outcome:** **NO-ERASURE-UNRESOLVED** is added.

## 11. S6-1 outcome map

**Primary outcomes:**

| Outcome | Condition |
|---|---|
| **NET-ARROW-CONFIRMED** | T-1 and T-2 are TRUE for every member |
| **NET-ARROW-PARTIAL** | the result splits by observable or by member |
| **NO-NET-ARROW** | neither retained K-1 observable carries the forward sign on the declared family |
| **RUN VOID** | a theorem or integrity implementation failure |

**Secondary outcomes (K-2):**
- **NO-ERASURE-ON-OPEN-MEMBERS**
- **ERASURE-OCCURS-ON-OPEN-MEMBER**
- **NO-ERASURE-UNRESOLVED**

The decided switch-on failures on J-L2 and σ-L1 are always reported separately.

## 12. Campaign-specific v4 exception

After the amended charter is frozen: **ONE S6-1 ANALYTIC / CERTIFIED EXECUTION IS AUTHORIZED.**

**It covers:**
- LS-1, LS-2 and LS-3;
- the exact spectral forms for T-3 and T-4;
- one deterministic interval-certified execution under the frozen protocol;
- finite-N values, as non-adjudicating cross-checks only;
- the result and verdict.

**Excluded:**
- RNG and stochastic simulation;
- any ordinary-grid sign test used as a gate.

If the resources are exhausted, the result is **UNRESOLVED**. Resources may not be increased for a rerun
without an owner ruling.

## 13. Interpretation fence

The strongest allowed statement, even if NET-ARROW-CONFIRMED lands:

> **In the declared infinite conservative pinned chain, the integrated bath-self-energy transfer and the
> reduced-state entropy measure retain a net direction despite arbitrarily late band-edge-memory
> backflow.**

**Not allowed:**
- "strict monotonicity is restored";
- "O-6 is repaired";
- "microscopic reversibility is gone";
- "a fundamental thermodynamic arrow has been derived";
- "J is a unique heat current".

The distinction under test: **pointwise arrow: NO**, while possibly **integrated/net arrow: YES**.

## 14. Record actions and sequence

**Record actions:**
- create this ruling;
- add the S6-0 banner (CLOSED / ACCEPTED);
- record A-1 and A-2;
- amend the S6-1 charter with §§8–12 and freeze it at a new commit;
- record that hash in CURRENT_STATE.

**Execution sequence:**
1. the analytic theorem document;
2. commit;
3. the deterministic certification script;
4. commit;
5. **one** execution;
6. the result and verdict;
7. **HARD STOP.**

**Not authorized:**
- S-4, S-7 or S-8;
- S5-WB or S5-OD;
- a new reversal diagnostic;
- gravity, Π₀ or cosmology.
