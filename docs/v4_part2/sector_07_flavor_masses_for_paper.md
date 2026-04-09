# Sector 7 — Flavor / Masses

**Status: Open, with exploratory entry point**

## What GRUT already has
The electroweak host (Sector 2) provides the mass-generation mechanism M_f = y_f v/sqrt(2). Yukawa couplings are free parameters, identical to the SM. Mass-matrix and CKM diagnostic utilities are provided. The fermion mass hierarchy (y_top/y_electron = 338,552) is documented but not explained.

## Minimal sector equations
| # | Equation | Status |
|---|----------|--------|
| 1 | M_f = y_f v / sqrt(2) | Inherited from Sector 2 |
| 2 | M_diag = U_L^dag M_Yukawa U_R | Bi-unitary diagonalization |
| 3 | V_CKM = U_L^{up,dag} U_L^{down} | CKM from up/down misalignment |

## Derived observables
All values are INPUT DATA from the SM, not GRUT predictions.

## Validation summary
| Test | Status |
|------|--------|
| 9 Yukawa couplings documented | **PASS** |
| Hierarchy ratio = 338,552 | **PASS** |
| Mass-matrix diagonalization | **PASS** |
| CKM row norms ~ 1 | **PASS** |
| CKM hierarchy documented | **PASS** |
| No overclaiming | **PASS** |

**6/6 pass.**

## What remains open
Mass hierarchy derivation, CKM derivation, generation count, Yukawa reduction — all open.

## Closure condition
Derive at least one mass ratio, CKM angle, or generation count from GRUT structure.
