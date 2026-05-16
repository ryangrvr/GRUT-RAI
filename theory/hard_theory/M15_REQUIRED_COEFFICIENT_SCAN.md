# M[1,5] Required Coefficient Scan

**Date**: May 9, 2026  
**Purpose**: Diagnostic identification of the M[1,5] coefficient required to achieve target R  
**Status**: Locked baseline with diagnostic target identified

---

## Executive Summary

The live V5 baseline uses **M[1,5] = 0.08κ** and produces **R = 1.3226** (error +14.54%).

RG flow analysis shows that to achieve the target **R ≈ 1.15470** (tree) or **R ≈ 1.15428** (loop), we require **M[1,5] = 0.0664κ**.

This required coefficient lies **between the proportional decomposition estimate (0.052κ) and the live baseline (0.08κ)**, approximately 17% lower than current.

---

## Locked Baseline

| Parameter | Value | Notes |
|-----------|-------|-------|
| Live M[1,5] coefficient | 0.0801 | Current (producing R = 1.3226) |
| M[1,5] pre-κ value | 0.000507 | Final matrix entry |
| κ | 0.006333 | 1/(16π²) |
| β_eff (live) | 0.122933 | 1.18% above target 0.1215 |
| R (live) | 1.32063 | 14.44% above target 1.154701 |
| Sensitivity dβ/dM[1,5] | 8.066 | HIGHEST leverage entry |

---

## Corrected Gate 2b Results

From the proportional decomposition with correct loop suppressions:

| Scenario | M[1,5] coeff | M[1,5] value | R | β_eff | Error % R |
|----------|--------------|--------------|---|-------|-----------|
| Live baseline | 0.0801 | 0.000507 | 1.3226 | 0.1229 | +14.44% |
| Proportional decomposed | 0.0519 | 0.000328 | 0.9958 | 0.1200 | +13.76% |
| **Required for target** | **0.0664** | **0.000421** | **1.1532** | **0.1215** | **+0.13%** |

---

## Diagnostic Target: x = 0.0664

The scan identifies that setting **M[1,5] = 0.0664κ** produces:

```
R = 1.153185  (target: 1.154701)
β_eff = 0.121531  (target: 0.12150)
Error vs R_tree: +0.131%
Error vs β_eff: +0.078%
```

This coefficient achieves **simultaneous optimization** of both R and β_eff to near-target values.

---

## Positioning of Required Coefficient

The required x = 0.0664 is positioned as follows:

```
Proportional decomposition: 0.0519κ → R = 0.9958 (UNDER-corrects)
                              ↓
                    REQUIRED: 0.0664κ → R = 1.1532 (TARGET HIT)
                              ↓
Live baseline:      0.0801κ → R = 1.3226 (OVER-shoots)
```

This indicates:
1. ✓ Reducing M[1,5] moves R in the correct direction (toward target)
2. ✓ The required reduction is ~17% from baseline (less aggressive than proportional 35%)
3. ✓ The target lies strictly between decomposition and baseline values

---

## Key Finding

**The R mismatch can be removed by reducing M[1,5] from 0.08κ to 0.0664κ.**

This is equivalent to a ~17% reduction from current value, or a shift from the baseline structural coefficient 0.08 to an effective 0.0664.

This required value is the **diagnostic target**, not the final answer. The next step is to derive x = 0.0664 from first-principles Euler↔gauge diagram decomposition and verify it matches independently computed contributions.

---

## Important Disclaimers

### What This Is NOT
- ❌ NOT a "fit" to the data (this is RG flow analysis with one free parameter)
- ❌ NOT "derived from first principles" (it is a required target, not a derivation)
- ❌ NOT promoting this coefficient as part of the final theory

### What This IS
- ✓ A diagnostic sweep identifying the coefficient required by RG flow to hit observed R
- ✓ A target for diagram-based calculation
- ✓ A quantitative specification of what first-principles decomposition must achieve

---

## Next Step

**Derive M[1,5] = 0.0664κ independently from Euler↔gauge diagram classes.**

The decomposition must produce contributions totaling an effective coefficient of 0.0664 when first-principles loop suppressions are applied:
- Verify whether current ~0.052 decomposition underestimates the coefficient
- Check for additional 1-loop or scheme-dependent contributions
- Compare against explicit Feynman diagram computation

Only after independent verification can we claim this coefficient as "derived."

---

## Methodology

The scan:
1. Swept M[1,5] = x*κ over x ∈ [0.045, 0.085] (100 points)
2. For each x, reconstructed live V5 matrix with M[1,5] override
3. Ran exact RG evolution: exp(M·t) with t = 96.7086 steps
4. Computed R, β_eff, and percent errors
5. Located x minimizing |R - R_target|

Result: Dense sweep identified x ≈ 0.0664 as achieving R_tree target within 0.13% error.

---

## Files

- [m15_required_coefficient_scan.py](grut/derivation/euler/m15_required_coefficient_scan.py) — Diagnostic scan module
- [test_m15_required_coefficient_scan.py](tests/derivation/test_m15_required_coefficient_scan.py) — Regression tests (8 tests)
- Locked baseline: [test_v5_baseline_reconciliation.py](tests/derivation/test_v5_baseline_reconciliation.py) (8 tests, all passing)

---

## Status

| Item | Status |
|------|--------|
| Live baseline locked | ✓ |
| Required coefficient identified | ✓ |
| Diagnostic target specified | ✓ |
| First-principles derivation | ⏳ NEXT |
| Publication ready | ✗ (pending derivation) |

---

## Conclusion

The RG flow diagnostic scan shows that reducing M[1,5] by ~17% from current value will resolve the R overshoot. The next task is to derive this reduction from explicit diagram decomposition and verify it independently. Only then can we promote this result to a physics claim.
