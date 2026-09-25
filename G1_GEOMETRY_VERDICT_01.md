# G-1 — DOES INFLUENCE DATA + ACCESS RECONSTRUCT GEOMETRY? VERDICT

**Date:** 2026-09-25 · **Charter:** `G1_GEOMETRY_CHARTER_01.md` (frozen at
`f9b043b` before the run) · **Authority:** GitHub Issue #2, owner comment
5827519334 · **Instrument:** `calc/g1_geometry.py` · **Artifact:**
`G1_GEOMETRY_RESULT.json` (sha `0f07c17c672b187a…`) · **Battery 26/34 —
EIGHT frozen gates failed and stay red.** Zero halts: every halt-grade
analytic identity held (reciprocity 8.7e-17, representation invariance
2.0e-15, Krylov identity 1.4e-15); matched controls exact. This is the
program's weakest quantitative result since reopening, and it is
reported at exactly that strength.

## VERDICT

> **GEOMETRY-PARTIAL, at reduced strength, with the failure surface
> fully recorded** — by the owner's frozen decision rule ("a
> geometry-related invariant is reconstructed but the full
> metric/curvature is not"). Geometry-related **invariants** are
> recovered from interface data alone; **quantitative metric
> reconstruction failed in-class**, and the obstruction is located.

### What certified at frozen strength (green gates)

- **1D dimension** from ball growth (d̂ = 0.714 ∈ [0.65, 1.35]).
- **The metric's rank:** top-2 MDS eigenvalues capture **0.917** of the
  anchor τ-data — the interface data is effectively 2-dimensional, an
  invariant read without ball counting, without labels, without
  gravity.
- **Exact reciprocity** at trace level (8.7e-17) — the causal metric
  class is symmetric, measured not assumed.
- **L-REP:** the frozen 30-rotation substrate scramble leaves the
  interface kernel identical to 2.0e-15 — every reconstruction is
  representation-invariant; **REPRESENTATIONAL** layer confirmed.
- **L-ISO (counterattack from below):** the 10×10 grid accessed at one
  corner and its Lanczos chain (Krylov dim 93; min effective on-site
  term −0.863, disclosed) have **identical complete single-site
  influence data** (1.4e-15). Under single-site access, geometry —
  dimension included — is **GEOMETRY-UNDERDETERMINED**. The Lanczos map
  is standard mathematics: **NULL-REDUNDANT** as a principle.
- **L-TOP (counterattack from above):** rings 40 vs 80 with identical
  local structure are indistinguishable on [0, 10] (0.0e+00) and
  differ by 0.31 once the wrap returns — **global topology is
  invisible inside the causal horizon of the data** and visible exactly
  beyond it.

### What failed at frozen strength (eight red gates, preserved)

- **2D and 3D ball dimension:** d̂ = 1.506 and 1.674 (gates 2 ± 0.35,
  3 ± 0.35).
- **Quantum (XX one-magnon) dimension and additivity:** d̂ = 0.485;
  additivity violation 0.333.
- **Both held-out metric predictions:** rel errors 0.366 and 0.374
  (gate 0.2).
- **Both L-CRV gates** (after the disclosed baseline repair): speed
  ratio 1.106 vs the predicted 1.5 (rel err 0.263); held-out travel
  time rel err 0.165 (gate 0.15).

### The located obstruction (this is the finding)

**Arrival-time functionals of interface data are not a metric on
finite dispersive substrates at these scales.** The frozen absolute
threshold reads the evanescent precursor tail (crossings travel faster
than any group velocity, with strongly non-metric t(r) — in the
quantum leg, literally the solution of J_r(2t) = ε). The labeled
front-peak diagnostic partially recovers dimension (1.12 / 1.94 / 1.73;
quantum 0.918) but is itself contaminated by boundary reflections
(diagnostic MDS capture collapses to 0.605, held-out errors up to
1.87, quantum additivity 0.398). L-CRV adds a third mechanism:
**impedance mismatch** — at the stiffness step the transmitted front
is reshaped, and the measured speed ratio (1.106) does not track √k
(1.5) through a threshold detector. Dispersion, reflection, and
impedance are physics of the substrate–interface pair, not numerics:
in this class, *time-of-flight geometry is confounded by everything
that is not geometry*. The information that survives confounding is
**invariant/structural**: rank (effective dimension of the τ-data),
symmetry (reciprocity), horizon structure (topology visibility), and
access-relativity (single-site dimensional collapse).

### The access–geometry law (certified component, stated at strength)

Combining the green legs: **how much geometry the interface determines
is a function of the access structure.** One site: none (a 2D world
and a 1D chain are the same interface object — constructed, not
conjectured). Five sites: rank and ordinal structure. Any finite
window: topology only inside its causal horizon. This extends P-5/P-6
("access lives at its changes") to the geometry layer: **geometry, as
seen by the interface, is access-relative and horizon-bounded.**

## DEFECT HISTORY (disclosed)

1. First run, L-CRV: the displacement source's mean-subtraction left a
   constant −1/N offset at every site, so the 1e-4 threshold fired at
   step 1 everywhere (t₆₀ = t₇₀ → division by zero). The detector
   measured the subtracted constant — nothing physical. Fixed by
   detecting deviation from the initial baseline profile; source,
   threshold, and gates unchanged. The gates then failed on physics
   and are preserved red.
2. The composite notes were rewritten after the diagnostic results to
   describe the measured record (the pre-written text had anticipated
   diagnostic recovery that did not occur); no gate, threshold, or
   verdict-bearing quantity was altered.

## FENCES AND SCOPE

No gravity input anywhere in G-1 (the owner's core rule held: geometry
was attacked from influence data first; gravity remains downstream and
fenced). Rider H carried: substrates static, stationarity by
construction in-class, not presumed beyond. Λ_R, Matsubara, Π₀, U5,
ω⁷/class-4 fenced; ℏ located-not-generated; type-III boundary map
only; finite type-I results not generalized.

## HARD STOP

Verdict recorded: **GEOMETRY-PARTIAL** (invariants: rank, reciprocity,
horizon, access-relativity — recovered and counterattack-tested) +
**GEOMETRY-UNDERDETERMINED** (single-site access; sub-horizon
topology) + **REPRESENTATIONAL** (labels) + **NULL-REDUNDANT**
(reconstruction machinery), with the quantitative metric/curvature
reconstruction **failed in-class at frozen strength**. Per the owner's
decision rule, a second geometry attack (better-conditioned
instruments: absorbing boundaries, larger substrates,
frequency-domain/spectral-distance functionals instead of
time-of-flight) or a gravity comparison opens **only by explicit owner
ruling**. Nothing is folded into 𝒯 on the strength of a plausible
picture.
