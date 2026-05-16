# Gate 2b Diagnostic: Clarifying the Baseline

**Date**: May 9, 2026  
**Issue**: Gate 2b comparison shows large R values (51, 23) vs. actual current V5 (R = 1.32)

---

## The Discrepancy

**Three scenarios executed:**

| Scenario | M[1,5] value | β_eff | R predicted | Notes |
|----------|--------------|-------|------------|-------|
| Current V5 (actual code) | 0.08κ = 0.000506 | 0.1229 | 1.32 | ✓ Matches expected state |
| Monolithic test (0.92 before κ) | 0.92κ = 0.005826 | 0.1607 | 51.1 | ⚠ Much larger than current |
| Decomposed test (0.60+0.30) | 0.60κ + 0.30κ² = 0.003812 | 0.1524 | 22.9 | ⚠ Improves vs mono, but still high |

---

## What This Means

### Hypothesis 1: M[1,5] = 0.92 is Too Large
If the audit identified M[1,5] coefficient as 0.92, but applying it as 0.92κ destabilizes the system (R → 51), then:
- Either 0.92 is not the right structural estimate
- Or 0.92 applies to a different quantity (not final M[1,5] value)
- Or there's an interaction effect when M[1,5] becomes ~11× larger

### Hypothesis 2: The Audit is Theoretical
The decomposition module (m15_diagram_decomposition.py) analyzed "what M[1,5] should be" based on diagram counting, but:
- It used 0.92κ as a reference value for comparison purposes
- The actual current V5 may not have M[1,5] = 0.92κ at all
- It has M[1,5] = 0.08κ instead (from generic Gauge↔Gravity coupling in build_matrix)

### Hypothesis 3: Two Different Correction Tracks
- **Current state**: M[1,5] = 0.08κ, gives R = 1.32 (14% error)
- **Proposed correction**: Use decomposition insight to reweight M[1,5]
  - But what's the right baseline?
  - Is it 0.92? Or something else?

---

## Decision Point

**Before proceeding further, clarify:**

1. **Is the audit's "0.92" the structural estimate for M[1,5]?**
   - If yes: why does setting M[1,5] = 0.92κ give R = 51 instead of reasonable values?
   - If no: what does the 0.92 refer to?

2. **Should the comparison be relative to current 0.08κ?**
   - Current V5: M[1,5] = 0.08κ → R = 1.32
   - Proposed change: M[1,5] = 0.08κ decomposed with loop ordering?
   - Or: completely different baseline?

3. **What is the actual physical M[1,5] the audit found?**
   - Is it really 0.92? (seems to destabilize)
   - Or is it smaller, and the decomposition 0.60+0.30 is the correction?

---

## Current Results (If Hypothesis 2 is Correct)

If the 0.92 is just a reference for the decomposition audit, then:
- **Monolithic 0.92κ**: Hypothetical worst case (shows what NOT to do) → R = 51
- **Decomposed 0.60κ + 0.30κ²**: Better direction (55% toward target) → R = 23
- **Still not matching observed**: Both need further investigation

This would mean Gate 2a showed:
✓ Decomposition moves in right direction (confirmed)
✗ But 0.92 baseline is wrong (magnitude doesn't match reality)

---

## Next Action

**Option A:** Clarify whether 0.92 is truly the current M[1,5]
- If yes: debug why it destabilizes the matrix
- If no: repeat Gate 2b with the actual current baseline (0.08κ) and show decomposition effect

**Option B:** Proceed with current results as-is
- Interpretation: Decomposition principle is sound (55% improvement), but baseline needs identification
- Next: Run Gates 1 & 4 independently to find missing corrections

**Recommendation:** Clarify Hypothesis 1 vs. 2 before running major corrections, to avoid chasing the wrong problem.

---

## Code Verification

All code is executing correctly:
- ✓ build_v5_matrix_with_m15_override() properly applies loop suppressions
- ✓ evolve_euler_channel() correctly computes RG flow
- ✓ Eigenvalue spectrum and projections match V5 theory
- ✓ Decomposition formula is correct (0.60κ + 0.30κ²)

**Issue is not in code, but in baseline specification.**
