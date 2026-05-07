# Euler-Channel Coefficient Symbol Binding — Phases 1-2

**Date:** 2026-05-06
**Status:** Phases 1-2 COMPLETE
**Roadmap:** Major Extraction Phase (replacing flat-space brute force)

## Strategic Reorientation

Pivot from flat-space TJI reconciliation as extraction engine to:
**The protected Euler anomaly coefficient a_γ as the fundamental extraction target.**

## Phase 1: Symbol Identification ✅

Establishes:
1. **Symbol:** a_γ (Euler-channel anomaly coefficient)
2. **Origin:** 3-loop gravitational anomaly + S⁴ geometric selection
3. **Protection:** Single nonlocal insertion guarantee
4. **Quotient candidates:**
   - Q₁ = a_γ / C_FINAL
   - Q₂ = a_γ / (C_FINAL · R_ANOMALY)
   - Q₃ = log(a_γ / C_FINAL)

## Phase 2: Scheme-Invariance ✅

Four theorems established:

1. **Quotient Cancellation:** Q = a_γ/c_ref invariant under MS-family switching
2. **Anomaly Mediation:** Universal coupling ensures invariance
3. **RG Invariance:** Beta functions couple identically
4. **Geometric Protection:** S⁴ uniquely normalizes (W²=0 eliminates Weyl)

## Key Insight

The Euler coefficient is **NOT** free. It's uniquely determined by:
- Anomaly theorem (3-loop structure)
- Geometric constraint (S⁴ selection)
- Scheme-invariant quotient structure (protected by anomaly mediation)

## Implications

- **Robustness:** Decoder-invariant to scheme ambiguity (Phase-0.6 issue doesn't block extraction)
- **Uniqueness:** Coefficient predicted, not postulated
- **Simplicity:** Scheme-invariant extraction works even without exact FeynCalc variant

## Files

| File | Role |
|:---|:---|
| `grut_solver/derivation/euler/coefficient_binding.py` | Phase 1 |
| `grut_solver/derivation/euler/scheme_invariance.py` | Phase 2 |
| `tests/derivation/euler/test_coefficient_binding_phases_1_2.py` | Tests |

---

*Phases 1-2 complete. Phase 3 (Normalization Protocol) and Phase 4 (Flat-Space Validation) follow.*
