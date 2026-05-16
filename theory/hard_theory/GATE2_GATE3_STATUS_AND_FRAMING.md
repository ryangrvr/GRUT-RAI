# Gate 2 and Gate 3 Status and Framing

Date: May 9, 2026  
Status: Cross-gate interpretation locked.

## Current Two-Route Status

| Route | Current status |
|------|----------------|
| Gate 2 / V5 flow route | R improved from ~1.32 to ~1.148 after M[1,5] correction |
| Gate 3 / protected Euler quotient | Symbolic quotient exists, but coefficient values are still null |

## What 3-loop Could Do

### 1. Direct resolution (preferred)

If the protected Euler-channel extraction yields

R_3loop = C_Euler,final / C_Euler,cosmo ~ 1.154,

then Gate 3 becomes the sharper extraction route and V5 remains an approximate flow model.

This is the strongest outcome, but full native S4 3-loop promotion remains blocked until:
- coefficient extraction,
- scheme checks,
- Ward validation,
- and independent replication
are complete.

### 2. Indirect resolution (residual explanation)

If Gate 3 does not directly produce R, it may still explain the remaining ~0.6% Gate 2 residual via:
- S4 projection normalization,
- counterterm finite subtraction,
- Euler-gauge mixing coefficient,
- protected/local separation.

This is consistent with current Gate 2 diagnostics, where remaining uncertainty is concentrated in convention-sensitive provenance terms.

## Non-Patch Rule for Gate 3

3-loop cannot be used as a numerical patch for Gate 2.

A 3-loop value near 1.154 is only promotable if:
- Euler-channel coefficients are explicitly computed,
- quotient is scheme-legal,
- S4 projection is clean,
- counterterm handling is independently fixed,
- and the result is not retrofitted into V5.

Otherwise, numerical agreement is not sufficient.

## Best Current Framing

Yes, the remaining residual could be a genuine 3-loop effect.  
But Gate 3 must be treated as an independent extraction route, not a repair knob for Gate 2.

If Gate 3 lands near 1.154, then convergence across independent routes is strong:

| Route | Result |
|------|--------|
| canonical sqrt(4/3) | 1.15470 |
| V5 corrected flow | ~1.148 |
| 3-loop Euler quotient | pending coefficient extraction |
| Osborn/local RG | ~1.15367 |

## Locked Interim Status

Gate 2 brings R into the sub-percent regime.  
Gate 3 may either:
- close the remaining gap,
- independently confirm the canonical value,
- or falsify the 3-loop route.
