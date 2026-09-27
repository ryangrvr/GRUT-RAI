# REPRODUCTION NOTE 01 — independent reconstruction of the C1-a epoch kernels

**Date:** 2026-09-27.
**What happened:** the owner independently rebuilt the C1-a stepped
network described in the public record (24 sites, one observed, unit
nearest-neighbour springs, pins 0.3, hidden springs (1,2)–(4,5) modulated)
using a matrix-exponential reconstruction written without reference to the
repository's instrument code, and reported the same-lag kernels of the two
stationary epochs.

**Reported values (owner's reconstruction):**

| lag τ | epoch A (ε_m = 0) | epoch B (ε_m = 1) |
|---|---|---|
| 1.0 | 0.1594754 | 0.1328810 |
| 0.5 | 0.3579003 | 0.2874716 |

**Verification against the committed instrument** (session agent,
2026-09-27; `calc/c1_seam.py` `World(24, ε).frozen(e, τ)`, run from a copy
outside the repository):

| lag τ | instrument epoch A | instrument epoch B |
|---|---|---|
| 1.0 | 0.1594754 | 0.1328810 |
| 0.5 | 0.3579003 | 0.2874716 |

All four values agree to every reported digit between two independent
implementations (matrix exponentials versus per-epoch eigendecomposition).

**What this reproduces, precisely.** Equal lag, different epoch, different
kernel: within the evolving world, no single kernel of the form $k(t-s)$
represents the response across epochs. This is the anchor-dependence
(local-anchor) half of the C1-a/C1-a2 finding. It does not by itself
reproduce the cross-boundary two-time kernel (which requires the mixing
matrix $C=V_B^{\mathsf T}V_A$), the certified A2-gates, or the specificity
control that separates nonstationarity from mere kernel difference; those
remain as recorded in C1-a and C1-a2.

**Scope.** This is an in-house check by the program's owner with tool
assistance, under standing direction D-1. It is an independent
*implementation*, not external review, and it changes no status.
