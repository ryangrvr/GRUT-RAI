# S6-1 — COARSE-GRAINED ARROW CHARTER 01 (DRAFT — NOT FROZEN; EXECUTION BLOCKED)

**STATUS: DRAFT.** It was produced under S6-0 §3.2(3), because the proposed S6-0 terminal is
PRINCIPLED-COARSE-ARROW-TEST-FOUND.
- **It freezes nothing and authorizes nothing.**
- It becomes frozen only after the owner accepts S6-0, rules on A-1 … A-5, and authorizes an
  execution.
- **HARD STOP before any run.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Target (only the EXECUTABLE pairs of S6-0 §4.6)

| Item | Target | Members |
|---|---|---|
| **T-1** | K-1 for J: the sign of X_J(∞) = ∫₀^∞ f_J dt | all four declared pairs, forward-oriented per S6-0 §4.2 Q5 |
| **T-2** | K-1 for σ: the sign of X_σ(∞) = D(0) − D(∞) | all four declared pairs |
| **T-3** | K-2 for J: X_J(T) > 0 for all T > 0 | J-L1 members (2, 1), (10, 1) only |
| **T-4** | K-2 for σ: X_σ(T) > 0 for all T > 0 | σ-L2 members (1/2, 1), (1/10, 1) only |

**Excluded:**
- **K-3** (ARBITRARY).
- **K-2 on J-L2 and σ-L1.** These are already FALSE by I-5. They are reported, not re-tested.

## §1 Parent and objects (all declared; no new ingredient)

- **Parent and ensemble:** O-6 as declared (`L0_1G_CHARTER_01.md` §1).
- **Observables:** J = g⟨p₂q₁⟩, carrying the §4.4 meaning caveat (bath self-energy); S_ref; Ḋ.
- **Primary object:** N = ∞ (K_∞ = 2.3 − T; L-N), with integrals from 0 (S6-0 §1.4).
- **Cross-checks only:** the finite-N guarded windows for N ∈ {23, 47, 95}.

## §2 Execution (proposed; exact / analytic; no RNG; no simulation)

**1. Analytic derivation, written and verified before any script.**
- **Theorem LS (return to equilibrium):** S₁(t) → S_ref at N = ∞. The route is Gibbs invariance, the
  rank-≤3 perturbation, absolute continuity, and Riemann–Lebesgue (S6-0 §4.4).
- **Closed forms:**
  - X_J(∞) = (T_s − T_b) + ½·T_b·r²;
  - X_σ(∞) = D(0);
  - r = (2.3 − √1.29)/2.
- **This settles T-1 and T-2 analytically.** The owner may instead rule under A-2 that they are
  already DECIDED.

**2. T-3 and T-4 (K-2 on the gated members).**
- Write an exact spectral representation of X_f(T) at N = ∞: finite sums of products of band
  integrals over the declared μ.
- Add a **rigorous tail bound** |X_f(T) − X_f(∞)| ≤ C·T⁻², with an explicit C. That C comes from the
  O(t^{-5/2}) remainder, which the record does not state and which must be derived.
- Then carry out an exact or interval-certified evaluation of X_f on [0, T*], with T* chosen from
  that bound.
- **Finite-N values are cross-checks only.**

**3. One run.** Then result, verdict, and HARD STOP.

## §3 Outcomes (proposed; the owner may revise before freezing)

| Outcome | Condition |
|---|---|
| **NET-ARROW-CONFIRMED** | T-1 and T-2 are TRUE at every member. Reported separately for heat and for entropy. |
| **NET-ARROW-PARTIAL** | T-1 or T-2 is TRUE at some members and FALSE at others, or TRUE for one observable only. |
| **NO-NET-ARROW** | T-1 and T-2 are FALSE. |
| **Sub-outcome NO-ERASURE-ON-GATED-MEMBERS** | T-3 and T-4 hold. |
| **Sub-outcome ERASURE-OCCURS** | T-3 or T-4 fails at some T. |
| **RUN VOID** | An implementation or integrity failure. |

## §4 Fences

- **A positive result means only** "net integrated transport survives despite arbitrarily late
  backflow".
- **It does not restore** strict ordering, pointwise monotonicity, a fundamental arrow, O-6, or the
  reversal hypothesis.
- **J is bath self-energy, not a unique hot → cold flux.** Its equal-temperature offset ½·T·r² must be
  reported alongside every J result.

## §5 Open items that must be ruled before freezing

1. **A-1:** member aggregation.
2. **A-2:** whether T-1 and T-2 are already DECIDED by the audit-derived Theorem LS. If so, they drop
   from the run.
3. **A-3:** whether the J caveat is adequate or a symmetric flux should be preferred. The record
   declares none, so a symmetric flux would be new structure.
4. **A-4:** keep §1.4's integration from 0.
5. **A-5:** the D-1 Ḋ-tail wording.
6. **Whether a v4 exception is granted for S6-1.**
