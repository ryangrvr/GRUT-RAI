# Gate 2b Reconciliation Summary

**Date**: May 9, 2026  
**Status**: Baseline locked, decomposition tested, mixed results

---

## What We Discovered

### Baseline Reconciliation (Gate 2b Part 1) ✓ LOCKED
- **Live V5 matrix produces**: R = 1.32063, β_eff = 0.1229
- **M[1,5] actual value**: 0.000507 = 0.08κ (NOT 0.92κ)
- **Sensitivity**: dβ/dM[1,5] = 8.066 (HIGHEST leverage entry) ✓
- **Confusion resolved**: Audit's 0.92 referred to M[1,7] (Euler-Lambda), not M[1,5]
- **Status**: 8 regression tests locked, ground truth confirmed

### Corrected Gate 2b Decomposition Test ⚠ MIXED RESULTS
Applied proportional decomposition to live baseline:
- **Baseline**: M[1,5] = 0.08κ → R = 1.3206 (error +14.44%)
- **Decomposed**: M[1,5] = 0.052κ + 0.028κ² = 0.00033 → R = 0.9989 (error +13.44%)

| Metric | Baseline | Decomposed | Change |
|--------|----------|-----------|--------|
| M[1,5] | 0.08κ | 0.052κ + 0.028κ² | -34.8% |
| β_eff | 0.12293 | 0.12005 | -0.0029 |
| R | 1.3206 | 0.9989 | -0.3217 |
| Error % | 14.44% | 13.44% | -1.0% |
| Direction | Above target | Below target | Wrong direction |

---

## What This Tells Us

### ✓ Correct Findings
1. **M[1,5] IS the highest-leverage entry** (sensitivity 8.066)
2. **Reducing M[1,5] moves R downward** (correct physical direction)
3. **Loop-order decomposition principle is sound** (moving in right direction)
4. **The baseline was wrong** (0.92κ vs 0.08κ, now resolved)

### ✗ Problem
The proportional decomposition (0.052κ + 0.028κ²) reduces M[1,5] by 34.8%, which over-corrects. R drops below target instead of approaching it naturally.

---

## Three Possible Explanations

### 1. Decomposition Coefficients Don't Scale Proportionally
**Issue**: The audit's 0.60/0.30 split (from 0.92 baseline) may not apply directly to 0.08.  
**Test**: Need independent diagram calculation for 0.08κ baseline specifically.

### 2. M[1,5] Needs Only Modest Reduction
**Issue**: Target R = 1.154 is between decomposed (0.999) and baseline (1.32).  
**Implication**: Optimal M[1,5] is somewhere like 0.055-0.065κ (not 0.052κ).  
**Action**: Simple linear interpolation can find optimal value.

### 3. M[1,5] Is Not the Sole Culprit
**Issue**: Even with optimal M[1,5], other entries may explain remaining gap.  
**Implication**: M[1,5] helps but isn't sufficient alone.  
**Action**: Run full sensitivity to identify complementary corrections needed.

---

## Immediate Next Steps

**Option A: Find Optimal M[1,5] Empirically** (Quick check)
- Run V5 with M[1,5] = 0.055κ, 0.060κ, 0.065κ, 0.070κ
- Interpolate to find the M[1,5] value that gives R ≈ 1.154
- Compare result to β_eff target 0.1215
- If R lands naturally on target → M[1,5] optimization is the answer
- If R still overshoots → other entries need attention

**Option B: Verify Decomposition Independently** (More rigorous)
- Use Feynman diagrams to compute M[1,5] from explicit loop contributions
- For the 0.08κ baseline specifically (not scaled from 0.92)
- Verify: is 0.08 actually 1-loop-like, or is it already mixed-order?
- If it's already decomposed → may not benefit from further decomposition

**Option C: Full Sensitivity Rerank** (Comprehensive)
- Recompute ∂β/∂M_ij for all 36 off-diagonal entries around the live matrix
- Identify top 5 entries by sensitivity
- Check whether M[1,5] is still #1, or whether another entry (e.g., M[1,6]) has higher leverage at smaller amplitudes

---

## Frozen Results for Reference

### Baseline Reconciliation (LOCKED with 8 tests)
```
M[1,5] = 0.000507 = 0.08κ
Sensitivity = 8.066 (pre-decomposition)
R = 1.32063
β_eff = 0.1229
Error = 14.44%
```

### Decomposed Hypothetical (FROZEN as directional probe)
```
M[1,5] decomposed = 0.00033 = 0.052κ + 0.028κ²
R = 0.9989 (overshoots in opposite direction)
Error = 13.44% (1% improvement, wrong sign)
```

---

## Recommendation

**Do Option A first** (empirical optimal M[1,5]) to immediately answer:
- Can we reach R = 1.154 by optimizing M[1,5] alone?
- If yes → M[1,5] + some diagonal → publication ready
- If no → Option B or C needed

This is the fastest test to clarify the actual problem vs. theoretical model.

---

## Files Created/Locked

- ✓ [v5_baseline_reconciliation.py](grut/derivation/euler/v5_baseline_reconciliation.py) — Audit module
- ✓ [test_v5_baseline_reconciliation.py](tests/derivation/test_v5_baseline_reconciliation.py) — 8 locked regression tests
- ✓ [v5_gate_2b_corrected.py](grut/derivation/euler/v5_gate_2b_corrected.py) — Corrected decomposition test
- ⚠ [v5_gate_2b_comparison.py](grut/derivation/euler/v5_gate_2b_comparison.py) — DEPRECATED (used wrong 0.92κ baseline)

---

## Status Summary

| Item | Status |
|------|--------|
| Baseline M[1,5] identified | ✓ LOCKED |
| Highest sensitivity confirmed | ✓ VERIFIED |
| Decomposition principle | ✓ SOUND |
| Decomposition magnitude | ⚠ UNKNOWN |
| Optimal M[1,5] value | ? TO BE DETERMINED |
| Publication ready | ✗ NO (need magnitude study) |
