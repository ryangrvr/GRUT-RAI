# S-6 COARSE-GRAINED ARROW — DEPOSIT 01 (closed; no new analysis)

**Authority:** `S6_OWNER_RULING_02.md` (Issue #2 comment `5915173769`). **Accepted terminals only.**
**Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## The chain

| Gate | Terminal | Records |
|---|---|---|
| **O-6** (floor) | **FALSIFIED** for strict pointwise / whole-window ordering | `L0_1G_OWNER_RULING_02.md`; additive correction `L0_1G_CORRECTIONS_01.md` |
| **S6-0** | **PRINCIPLED-COARSE-ARROW-TEST-FOUND** | `S6_COARSEGRAINED_ARROW_01.md` (pre-registered `fc51def`); `S6_OWNER_RULING_01.md` |
| **S6-1** | **NET-ARROW-CONFIRMED**, with secondary **NO-ERASURE-ON-OPEN-MEMBERS** | charter `fbd15c8`; verified theorem `122928a`; script `84e244d`; one run → `3753210`; `S6_OWNER_RULING_02.md` |

## Accepted results

1. **The criterion is threshold-free:** B_f(∞) < ½ ⟺ X_f(∞) > 0.
2. **LS-1, return to equilibrium (theorem):** S₁(t) → T_b·diag(r, 1), with r = (K_∞⁻¹)₁₁ = (2.3 − √1.29)/2.
   - The global Gibbs state is invariant.
   - The initial deviation is finite-rank.
   - The spectrum is absolutely continuous, with no bound state.
   - Riemann–Lebesgue gives the decay.
3. **LS-2, closed forms (theorem):**
   - X_J(∞) = (T_s − T_b) + ½T_b r² (bath self-energy; the offset ½T_b r² is interaction bookkeeping);
   - X_σ(∞) = D(0) > 0.
4. **Net arrow on every member.** The forward X_J(∞) values are:

   | Pair | Forward X_J(∞) |
   |---|---|
   | (2, 1) | 1.16943 |
   | (10, 1) | 9.16943 |
   | (1/2, 1) | 0.33057 |
   | (1/10, 1) | 0.73057 |

   X_σ(∞) > 0 at all four pairs.
5. **No erasure on the direction-matched members.** X_J(T) > 0 for all T on L1, and X_σ(T) > 0 for all T on L2.
   This is interval-certified. The opposite-direction members start wrong-signed (K-2 is FALSE there).
6. **LS-3, entropy tail:** D = t⁻⁶P + O(t⁻⁷) and Ḋ = t⁻⁶P′ + O(t⁻⁷). P is non-constant, so Ḋ reverses sign arbitrarily
   late.

> **Pointwise arrow: NO. Integrated/net direction: YES.** Irreversibility need not mean pointwise monotonicity.

## Fences

**Not established:**
- broken microscopic reversibility;
- a fundamental thermodynamic arrow;
- an O-6 repair;
- a forward-pointing instantaneous flux;
- J as a unique heat current;
- a dynamically derived coarse-graining.

**Scope of the arrow:** it is **integrated / ensemble / preparation-relative**.

## Status

- **S-6 is CLOSED. No S6-2.**
- **Next:** SYN-0, the working-theory synthesis (read-only).
