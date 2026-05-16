# Gate 3 Mathematica/HypExp Handoff

Date: May 9, 2026  
Scope: Protected round-S4 Euler-channel 3-loop coefficient extraction.

## Exact Integral Target

Evaluate the Euler-channel scalar building block:

I(D) = Integral_{-1}^{1} [2F1(h_plus, h_minus; D/2; (1+Z)/2)]^3 * (1 - Z^2)^((D-3)/2) dZ

with D = 4 - 2 epsilon.

This is the blocker integral appearing in the Allen-Jacobson S4 route.

## Definitions

- D = 4 - 2 epsilon
- epsilon: dimensional regulator
- Z in [-1, 1]: S4 invariant distance variable
- h_plus, h_minus: Allen-Jacobson hypergeometric indices for chosen mass/coupling branch
- round-S4 projection: enforce W^2 = 0 (Euler-only channel)
- regulator: dimensional regularization around epsilon -> 0
- scheme: OR4-compatible Euler-channel scheme only

## Required Laurent Expansion

Expand the integrated result around epsilon = 0 to at least:
- pole terms: 1/epsilon^n (as present)
- finite term: epsilon^0

Minimum requirement for Gate 3 landing:
- explicit finite epsilon^0 coefficient for C_Euler_cosmo and C_Euler_final candidates
- explicit pole structure used to verify subtraction/legality chain

## Required Outputs

For each coefficient candidate (C_Euler_cosmo, C_Euler_final), report:
1. Laurent pole terms
2. finite epsilon^0 part
3. normalization conventions used
4. regulator and scheme metadata
5. protection assessment:
   - protected Euler-channel coefficient
   - or scheme-fragile local contamination

## Mathematica/HypExp Skeleton

```mathematica
(* Symbols and assumptions *)
Clear[eps, D, Z, hp, hm];
D = 4 - 2 eps;
Assuming[eps > 0 && -1 <= Z <= 1,
  integrand = (Hypergeometric2F1[hp, hm, D/2, (1 + Z)/2])^3 * (1 - Z^2)^((D - 3)/2);
];

(* Step 1: if possible, transform hypergeometric structure to series-friendly form *)
(* Use HypExp-compatible transforms on 2F1 parameters around eps expansion point *)

(* Step 2: perform or represent integral *)
Iraw = Integrate[integrand, {Z, -1, 1}, Assumptions -> eps > 0];

(* Step 3: Laurent expansion around eps -> 0 *)
Iseries = Series[Iraw, {eps, 0, 0}] // Normal;

(* Step 4: extract pole and finite parts *)
poles = SeriesCoefficient[Iraw, {eps, 0, -1}];
finite = SeriesCoefficient[Iraw, {eps, 0, 0}];

(* Step 5: export structured result with metadata *)
```

## Acceptance Criteria

1. Computed coefficients land cleanly:
   - C_Euler_cosmo and C_Euler_final produced with pole and finite parts and full metadata.
2. Scheme contamination detected:
   - output explicitly marks scheme-fragile local contamination when present.
3. Integral remains analytically blocked:
   - output returns explicit blocker statement (no fake finite coefficients).
4. Quotient invalid:
   - output marks invalid if denominator is zero/undefined or legality conditions fail.

## Rejection Criteria

- Manual coefficient insertion
- Using target R to choose finite parts
- Mixing Weyl channel on round S4 (W^2 = 0)
- Using Im-log/CTP causal channel without a derived CTP-to-Euler projection

## Governance

Gate 3 is independent of Gate 2 and must not be used as a patch channel.
Any numeric result is non-promotable until legality, protection, and replication gates pass.
