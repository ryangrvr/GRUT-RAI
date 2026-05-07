# Investigation: TJI Phase-0.5 MS-bar Reconciliation

**Date:** 2026-05-06
**Status:** PENDING — Failure Mode (A)

## Summary

Phase-0.5 investigates reconciliation of flat-space 2-loop T_2 reduction from raw dimensional regularization to MS-bar convention.

**Result**: Transcendental terms (γ_E, log(2), log(π)) do not cancel with standard Collins MS-bar absorption, preventing expected conversion to Fraction(7, 4).

## Implementation

Created full Phase-0.5 infrastructure:
- `grut_solver/derivation/tji/flat_space.py` — reconciliation module
- `tests/derivation/tji/test_ms_bar_reconciliation.py` — test suite

## Failure Mode (A): Transcendentals Not Canceling

The standard MS-bar absorption factor [Γ(1+ε)⁻¹ · (4π)^ε]² produces transcendental terms that persist after all simplification passes.

**Cross terms computed:**
- T₁ = (-1/64) × [absorption ε² coefficient] → contains transcendentals
- T₂ = (-25/384) × [2γ_E + 2ln(π) + 4ln(2)] → transcendental
- T₃ = -541/2304 → rational

**Sum T₁ + T₂ + T₃:** Still contains γ_E, ln(2), ln(π), π² terms.

## Possible Explanations

1. **Scheme variant**: FeynCalc may use MS-dagger, MS-prime, or other MS-family variant with different absorption formula
2. **Raw scheme mismatch**: TJI Phase-0 coefficients may be in different regularization prescription
3. **Reconciliation misunderstanding**: The conversion process may require different approach

##  Recommendations

1. Check V7 §26.2.3 for explicit scheme specification
2. If variant identified, update `ms_bar_absorption_factor()` and retry
3. Phase-0.5 remains PENDING; not a blocker for Phase-1

---

Reference: Phase-0.5 plan at `/Users/mpg/.claude/plans/stateful-napping-snail.md`
*Investigation completed 2026-05-06. Awaiting scheme clarification.*
