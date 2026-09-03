# H¹ = 0 — STRUCTURAL THEOREM / COUNTEREXAMPLE CAMPAIGN

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_theorem_campaign.py` ·
**Artifact:** `WALL_KR_H1_THEOREM_RESULT.json` · **Battery: 21/21, zero failures.**
**Kernel-form mathematics only** — no new loop calculation, no ω ≪ H, no IR prescription, no
A-F selection, register sha256 identical pre/post, worktree unchanged, nothing banked. W-0.

## VERDICT: **H1-REFUTED** — as a structural theorem over the registered structural assumptions

**The computed fact H¹ = 0 stands untouched.** What is refuted is its promotion to a symmetry
consequence: every candidate forcing mechanism fails at an identified step, and an admissible
O(H) form is exhibited.

## THE COUNTEREXAMPLE FORM — EXECUTED, NOT ASSERTED

$$ f(\omega) = i\,b\,\omega^3 \,\mathrm{Log}(-i\omega/\mu), \quad b \in \mathbb R $$

- satisfies the retarded reality condition f(−ω̄)* = f(ω) **exactly** — defect 0 at 40-digit
  precision over 29 UHP points including near-real-axis;
- is UHP-analytic (causal/retarded);
- has boundary values Re f = (π/2)b|ω|³ (even), Im f = bω³ log|ω|/μ (odd) — a legitimate
  dispersive + absorptive pair;
- sits dimensionally in the H¹ slot.

**Controls:** the real-coefficient ω³ form FAILS the condition (defect ~10²) — the test has
teeth; the registered-form analogue ω⁴ℓ passes.

## WHERE EACH PROOF ROUTE BREAKS

| route | breaks at |
|---|---|
| parity / hermiticity | the exhibited form **passes** — the route never starts |
| curvature evenness | **false for nonlocal objects**: □_FRW = −∂_t² − 3H∂_t + a⁻²∇² carries the friction term *exactly linear in H*. Valid only for the local counterterm sector — consistent with the even 1b basis |
| exact dS invariance | Σ = H⁴ g(ω/H); an O(H) term is an x³ term in g's large-x expansion, **unforbidden by the symmetry**; flat-limit matching constrains only the leading term |
| CTP structure | consistent-with, but yields no theorem |
| "BD is dS-invariant, so no H term" | **insufficient** — by the scaling argument, even exact invariance admits x³ |

## THE COUNTEREXAMPLE BATTERY — theorem vs declaration, kept apart

Five templates. **Exactly one exclusion is evidenced**: the u_b boundary class, excluded by the
verified base-time independence through O(H²). The other four (α-vacuum-like deformation,
chart-dependent subtraction, noncovariant regulator, nonlocal state-dependent term) are
excluded only by **declarations** — which is precisely the distinction the audit was required
to preserve.

## WHAT REMAINS — THE ACTUAL THEOREM, NOW PRECISELY POSED

The weakest missing assumption is an **asymptotic/adiabatic-order condition on the scaling
function g** — equivalently, on the declared state's large-ω/H structure — that kills the x³
term. That condition is **neither standard nor registered**; it would be new input. Proving it
*from* the declared BD/Option-B construction is the real remaining theorem:

> **Does the adiabatic order of the declared vacuum force the absence of the x³ term in the
> large-argument expansion of the dS scaling function?**

## GENERALIZATION — the surprise inverts

The refutation legs are sector-blind: FRW friction is linear in H for *any* field, so **O(H)
terms are generic in FRW open systems**. The gravitational H¹ = 0 is therefore *more*
surprising than it looked, not less.

## LEVEL-2 CANDIDACY

**Dead as a symmetry premise.** Alive only as a possible *dynamical regularity* — "adiabatic
vacua kill the x³ term" — which would itself need derivation before serving as a shared
non-input premise.

## INDEPENDENT VERIFICATION

Three adversarial verification legs dispatched to independent agents; **PENDING at freeze**,
recorded honestly (the fd6d6fd lesson: a pending run is never reported as a final one). The
campaign's own executed check — leg 1 with its detecting control — does not depend on them.
A reconciliation follows when they return.

## W-0 STATUS — H¹ structural theorem/counterexample campaign completed; no low-frequency physics; A-F unchanged; nothing banked.
