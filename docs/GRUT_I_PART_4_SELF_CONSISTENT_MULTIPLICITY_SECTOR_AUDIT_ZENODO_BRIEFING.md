# GRUT-I Part 4: Self-Consistent Multiplicity Sector Audit — Zenodo Upload Briefing

## Instructions for Claude Chat

You are creating two documents. This was previously "GRUT-IV" — a sector audit testing whether the self-consistent back-reaction loop Phi ↔ X(Phi) produces multiple fixed points.

---

# DOCUMENT 1: Main Manuscript

## Title

**GRUT-I Part 4: Self-Consistent Fixed-Point Multiplicity — Search and Artifact Identification**

## Author

D. Ryan Grover

## What This Document Is

Two-stage audit testing whether the self-consistent equation Phi = X(Phi) has multiple solutions, potentially breaking the unique-attractor theorem. Alpha found two roots in a shell approximation. Beta proved the shell result is an artifact: the exact self-consistent equilibrium is a Bernoulli ODE with a unique analytical solution.

## Narrative

**Alpha (Multiplicity Search):** The self-consistent fixed-point equation Phi = X(Phi), where X depends on Phi through T^Phi → Einstein → m(r) → X, reduces to a quadratic at each radius in the uniform-shell approximation. At radii r > 1.77 r_s, the quadratic has two positive roots. At zero additional cost (only constitutive equation + Phase 4 T^Phi + Einstein equations).

**Beta (Stability and Global Branch Audit):** The stability analysis found 26 radii with apparently two stable roots — impossible for a 1D autonomous flow. The resolution: the single-radius shell approximation is WRONG. The exact self-consistent equilibrium (Phi = X everywhere, simultaneously at all radii) reduces to dm/dr = -alpha m^2/r^2, a Bernoulli ODE with a UNIQUE analytical solution. The second root was an artifact of assuming Phi uniform in the shell while the exact solution has Phi varying continuously as m(r)/r^2.

**Verdict:** multiple_roots_but_single_attractor — confirmed at the global level. The self-consistent architecture does NOT produce multiple basins.

## Key Formal Objects
- Self-consistent equation: Phi = X(Phi) where X = m(r)/r^2 and dm/dr = 4pi r^2 rho(Phi, X)
- Shell approximation: quadratic a Phi^2 + b Phi + c = 0 (two roots at r > 1.77 r_s)
- Exact solution: Bernoulli ODE dm/dr = -6.07 m^2/r^2; m(r) = M/(1 + 6.07 M(1/R_ext - 1/r))
- Exact: UNIQUE. Shell: ARTIFACT.

## Source Documents (2)
- grut/self_consistent_multiplicity.py (Alpha computation)
- grut/global_branch_solver.py (Beta computation)

---

## Zenodo Metadata

- **Title:** GRUT-I Part 4: Self-Consistent Fixed-Point Multiplicity — Search and Artifact Identification
- **Authors:** D. Ryan Grover
- **Keywords:** GRUT, self-consistency, fixed points, multiplicity, Bernoulli ODE, approximation artifact
- **License:** CC BY 4.0
- **Upload type:** Publication / Preprint
