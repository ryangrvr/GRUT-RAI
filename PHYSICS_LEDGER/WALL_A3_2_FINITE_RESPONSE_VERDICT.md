# WALL A3-2 FINITE RESPONSE -- VERDICT

**Task**: the finite eps^0 retarded kernel Sigma_R^finite(omega,k,H,m) of the D2 assembly (A3-2A..A3-2F), assembled from the A3-1 validated masters.
**Verdict**: PASS
**Gate counts**: 204/204 gates passed; 3/3 controls detected; 0 failures.
**W-0**: computed-and-reported, NOT banked. No register edits.

## The five A3-2E checks
1. Scalar-bubble finite limit: B(K2) anchors vs A3-1 route-A (3 spacelike Re + timelike Im = +pi*sqrt(1-4/5)), plus the monomial-class referee battery vs A3-1's own trace-composition quadrature (incl. omega-derivative depths through the exact fdiff tower).
2. H^0 flat limit: the finite seagull identity (m^4/2)[sqrt(-g)]_{h^2} x (1+kappa-ln(m^2/mu^2)) exact; the K=0 cross-route; structural H-grading.
3. Retarded support/sign: Im == 0 below K^2 = 4m^2 (all H^0/H^2 slots, all no-cut samples); the +pi*Int_{cut} y^n(1-y)^np D^e sign law on every G-atom above threshold (sign-carrying: negative for odd e, since D < 0 on the cut).
4. Subtraction locality: Pi_local^MS fingerprint e2f0bbfe6fd4c89d reproduced from THIS assembly's own c-sector; 100% of pole terms F1-local under the independent classifier port; the finite sector byte-untouched.
5. Wrong-branch negative control: DETECTED at master level and at component level (the +i0 branch disagrees; the branch is load-bearing).

## Method (the twin law)
pole(j,N) = c*moment*P*Delta^s and fin(j,N) = moment*Delta^s*[P*(kappa - ln((Delta-i0)/mu^2) + s_j) + C(j,N-1) + Q], with the exact-d moment correction s_j = psi(j+2)-psi(2). Quadruple-verified against A3-1: the pole grid 25/25 byte-identical to Ipole_scalar; M_1..M_4 and the T2/T4 exact-d compositions exact. All Delta are Delta-i0 (the A3-1 branch law).

## Representation
Local finite sector: closed sympy forms (pass the frozen F1 predicate verbatim; kappa/ln(mu^2)/ln(m^2/mu^2) are V4-local coefficient logs). Nonlocal sector: the closed atom families G[n,np,e], R[n,np,e] -- exact 1-D Feynman-parameter integrals with exact fdiff recurrences; no Li_2/Clausen class can arise (gated on the assembled object).

## Limitations
- SKIPBAT=1 construction load: the 23-min Level-2 battery is NOT re-run (last PASSED at 195a481, all five cases with the broken control failing); the L2-discriminating s^1 case IS gated here in finite mode with its own broken control
- referee independence scope: atom values are direct mpmath quadratures of their DEFINITIONS (no analytic primitive); the composition coefficients are the validated engine routing (shared lineage, byte-replayed against the frozen cache); the master law itself is refereed at monomial level against A3-1's own trace composition (E1), including omega-derivative depths through the fdiff tower
- E1 is a TWO-PATH agreement test and cannot by itself certify the atom quadrature (the missing-cut-breakpoints defect survived it at 3.1e+06 with BOTH paths sharing it); the quadrature authority is the EXTERNAL analytic settlement (e1_settle_report.txt: partial-fraction closed forms for all 28 R-atoms, dual-rule dps-60 values for all 24 G-atoms at the cut sample, out-of-sample-validated at K^2=24), embedded as STEP-2 regression gates against externally derived constants
- the K^2 = 4m^2 threshold point itself is excluded from the battery (the A3-1 bisection boundary); the timelike R-atom referee uses complex-eps Richardson WITH THE CUT POINTS AS BREAKPOINTS (3-point @ eta = 2e-5, the settlement-validated scheme); the timelike composition referee takes the -i0 by SECTOR (pole-free z^{s-k} terms at the exact boundary value z = D - i*1e-30, pole terms by the breakpoint Richardson)
- sympy closed forms are EXPOSITORY, gated against the referee (never the reverse); where not obtained within 300s this is recorded and the referee remains the authority
- the O(H) finite sector parity class is recorded under the standing T4 fence, NOT interpreted
- the TT view is derived-only (post-freeze, used in no gate); the assembly carries all E/P slots (no early projection)
- the finite block cache is a staging artifact (tag A32fin-v1, A32_CACHE_DIR); the frozen object is complete in the claimed outputs; a cache-off replay gate proves no cache drift

## Hard stop
A3-3 freeze complete (see Sigma_R_finite_full.json and its verdict). Q1-Q5, J(omega), PV, spectral classification, basis work, refits and register edits remain LOCKED. The next stage begins only after owner/reviewer inspection of this record.
