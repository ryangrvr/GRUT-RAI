# WALL A, STAGE A3 — V3 AMENDMENT: the de Sitter organisation of the loop (Option B)

**Date:** 2026-08-25 · **Cites:** the frozen v1
`WALL_A_A3_DECLARATIONS.md` (sha256 `87e2d24d5be6d67970f4089a09aa61a28d4de8cf6471f987af3db1c2ac015f6e`),
its registry (sha256 `faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55`),
and the v2 amendment (sha256 `6f2a762f4a4a01cd4794d029eecb2f1aadace9cd52637f12d3529e0564ce3d53`).
No frozen file is edited. Every clause of v1 (+v2) stands except as extended below.
**Provenance:** the ASSEMBLY-2 adjudication (coordination log, 2026-08-25; commit
`2c40ab4`) surfaced that a FRW-dressed vertex against undressed flat propagators is not
a consistent microscopic object; the owner ruled on the resulting organisational fork.

## The ruled organisation (owner, 2026-08-25)

**Option B — controlled adiabatic/H expansion — is the PRIMARY computational route** for
the de Sitter self-energy, with **Option A — exact de Sitter (Bunch–Davies) propagators
G_BD(η,η′;k) and the full time-dependent Σ(η,η′,k) — retained as the robustness
CROSS-CHECK TARGET.** The choice is methodological: the flat anchor is independently
verified (the fish+seagull divergence reproduces the Gilkey/'t Hooft–Veltman
minimal-scalar coefficients exactly), and the adiabatic route lets every retained order
be validated against that anchor.

## The binding condition (owner's words, the spine of this amendment)

> B is an **approximation scheme, not a new physical assumption**.

Operationally, every instrument working under this amendment MUST:

1. **Declare the expansion parameter and the retained order** on the artifact's face
   (e.g. powers of H relative to the declared comparison scales — the instrument names
   the dimensionless parameter it actually expands in), and **report the convergence
   or regime of validity** of the truncation. An undeclared truncation is a violation,
   not a simplification.
2. **Dress consistently at every retained order**: vertex dressing AND propagator
   dressing carried to the SAME order in the expansion parameter. The
   dressed-vertex/undressed-propagator hybrid is PROHIBITED — it was the defect that
   forced this amendment.
3. **Recover the flat plant at each order**: the H → 0 limit of every retained order
   must reproduce the independently verified flat structure (at zeroth order, the
   full Gilkey coefficient set {m⁴/2, m²R/6, R²/120, R_mn²/60}/(16π²ε) with the
   seagull included).
4. **Keep Option A as the declared cross-check target**: any result whose physical
   interpretation depends on the truncation must state what the exact-dS comparison
   would test, so the robustness check is a defined future computation, not a gesture.

## Locked-in identification lessons (from the same adjudication, binding)

- **Multi-K² identification is mandatory**: at any single K the O(h²) basis kernels
  satisfy the exact null relation (Gauss–Bonnet plus 2R_mn² − R² = −K²·EH); the design
  matrix has rank 3, not 4. Pole identification uses at least two distinct K² samples
  (with a held-out sample where feasible) and states uniqueness modulo the exact null
  space. "Unique fit with zero free parameters at a single K" is unsatisfiable by
  construction and may not be used as a criterion.
- **Same-footing comparison**: target and basis kernels enter the fit in the same
  representation (K symbolic on both sides, or the same numeric K substituted into
  both). Mixed-representation fits are void.
- **Basis kernels are gated, not trusted**: every basis kernel used in an
  identification must pass (i) linearised gauge invariance and (ii) the Gauss–Bonnet
  identity, as executed checks on the artifact's face.
- **The seagull is part of the assembly proper**: the O(κ²) hh–φφ tadpole diagram is a
  required component of the one-loop self-energy (Λ-coefficient value and Ward
  consistency), not a calibration afterthought.

This amendment is immutable once hashed; its sha256 is recorded in
AGENT_COORDINATION.md and the commit. Any further change requires a v4 citing this file.
