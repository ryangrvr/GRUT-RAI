# M15 Diagram-Origin Derivation

Date: May 9, 2026  
Status: Gate 2 numerically resolved at diagnostic and diagram-assembly level; not yet promoted to full physical derivation.

## Status Distinction

Gate 2 is numerically resolved at the diagnostic and diagram-assembly level, but not yet promoted to a physical derivation until each component coefficient in the assembly has independent provenance.

That distinction is mandatory for publication discipline.

## Current Structure

| Step | Status |
|------|--------|
| Live V5 baseline locked | done |
| Required M[1,5] found by scan | done |
| Independent diagram-origin assembly created | done |
| Assembly lands near target without using target during construction | strong result |
| Regression tests enforce no-fitting rule | done |
| Full physical derivation of each component coefficient | still needed |

## Assembly Discipline

The module assembles

M[1,5] = M_box + M_triangle + M_bubble + M_counterterm + M_S4_projection

before comparing to the diagnostic reference x_required ~ 0.0664.

The diagram-origin assembly independently produces x_derived = 0.065963, close to the diagnostic required value x_required ~ 0.0664. This supports Gate 2 as a resolved diagnostic mechanism. The result is not yet promoted as a physical derivation until the component coefficients are independently derived from explicit diagram calculations.

## Numerical Loop Closure at x_derived

Injected into live V5 flow:

M[1,5] = 0.065963 * kappa

Results:

| Metric | Value |
|--------|-------|
| beta_eff | 0.121483827 |
| R | 1.147963340 |
| error vs 1.15470 | 0.583458% |
| error vs 1.15428 | 0.547238% |

Interpretation:
- The injected diagram-origin value is in the correct regime and dramatically improves over live baseline.
- It is close to, but not identical with, the scan-optimized diagnostic coefficient.
- This is expected while component coefficients are still estimate-grade rather than fully derived.

## Coefficient Provenance Table

| Component | Coefficient in assembly | x-contribution in M[1,5] = x*kappa | Status | Source label |
|-----------|-------------------------|------------------------------------|--------|--------------|
| box | 0.046867 (1-loop structural) | +0.046867 | estimated | internal topology+multiplicity estimate |
| triangle | 0.015725 (1-loop structural) | +0.015725 | estimated | internal mixed-vertex estimate |
| bubble | 0.006475 at loop order 2 | +0.000041 (after kappa suppression in x-units) | heuristic | internal effective-2-loop bookkeeping |
| counterterm | 0.002220 (1-loop subtraction) | -0.002220 | estimated, scheme-sensitive | internal scheme-subtraction placeholder |
| S4 projection | 0.005550 (geometric correction) | +0.005550 | heuristic geometric | internal curved-space projection estimate |

## Credibility Gate Remaining

The next credibility gate is coefficient provenance completion:
1. Replace estimate and heuristic coefficients with explicit derivations or external references.
2. Mark scheme choices for counterterm handling and show stability checks.
3. Re-run the same no-fitting assembly with derived coefficients only.

Only after this step can Gate 2 be promoted from strong diagnostic resolution to physical derivation claim.
