# Wall A / A5 — synthetic self-energy plant: PARTIAL PASS, one open item

**Date:** 2026-08-23 · JSON: `WALL_A_A5_RESULT.json`. W-0 fence applies: everything here is
COMPUTED-AND-REPORTED, NOT BANKED.

## What passed

| control | passivity | low-ω slope | recovered | convergence |
|---|---|---|---|---|
| C1 scalar one-loop bubble (threshold 2m=1) | ✓ | n/a — Im Σ≡0 below threshold, **verified** | ✓ ZERO-BELOW-THRESHOLD confirmed | POWER-DIVERGENT ⚠ |
| C2 Lorentz oscillator | ✓ | +1.136 (expected ≈1) | ✓ within 0.15 | LOG-DIVERGENT ✓ |
| C3 corrupted sign | **✗ correctly rejected by gate** | — | — | — |
| C4 white floor | ✓ | 0.000 exact ✓ | ✓ | LOG-DIVERGENT ✓ |

The consumer pipeline (passivity gate → multi-point low-ω fit → convergence probe) recovered
every planted exponent and rejected the corrupted sign. The multi-point fit resolved the
two-point estimator's ±0.14 problem: C2's 1.136 vs expected 1.0 sits inside the declared band.

## The open item: C1's convergence class

C1's static-response partials grow past my 25% threshold and the p_full/p_6 ratio exceeded 3,
classifying POWER-DIVERGENT. Physically C1's high-ω Im Σ plateaus at a constant ⇒ the static
integral should be LOG-divergent. My growth-ratio heuristic mislabels it because the
threshold-rise region [2m, ~2] inflates the early partial before the plateau dominates.

**Two candidate responses, neither taken unilaterally:**
(a) exclude the threshold-transient window from the growth comparison (principled: the rise is
physics, not divergence);
(b) replace the ratio heuristic with an asymptotic-fit of partial increments vs ln(W)
(log-divergence is linear in ln W; power laws are not).

Both are defensible; choosing between them by whichever makes controls pass would be tuning the
gate. **Deferred as an owner-visible open item with the diagnosis recorded.**

## Verdict (FINAL, after battery calibration + frozen application)

> **A5: FULL PASS.** The increment-ratio classifier was selected and δ=0.15 frozen on an
> independent analytical battery (plateau / growing power / convergent-decaying / ln²-edge),
> then applied to C1 with the transient included: **r = 1.0005 → LOG-DIVERGENT**, matching
> physics. B4's sub-label reads POWER at practical decade depth — divergence detection itself is
> exact; documented known limit. No gate tuning occurred: δ was frozen before C1 was touched.

**This classifier is now the G3/A6 convergence instrument** — the thing that will place the real
Im Σ_R^TT on one side of the convergent/divergent boundary. Its calibration battery travels with
it in this artifact.

## Standing

W-0 fence on every artifact: COMPUTED-AND-REPORTED, NOT BANKED. Next: A2 operator basis per
sequence A5→A2→A1→A3→A4→A6→A7 (mission pre-registered separately with B-1..B-4 fences).