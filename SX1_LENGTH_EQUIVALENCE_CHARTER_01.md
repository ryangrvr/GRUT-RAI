# SX-1 — CAN Sel-4x (CONSTANT LENGTH RESCALING = PURE UNIT CHANGE) BE SELECTED? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner direction given in-session
after the GS-1 ruling (Issue #2 comment 5837782502, which cleared the
hard stop for the next chartered fork). The owner chose **Sel-4x
(length equivalence) before D = 4 TT/ξ**, because the spatial coupling
question sits underneath the graviton channel.

**Target (owner, verbatim):** *Can Sel-4x — constant spatial/length
rescaling as pure unit change — be selected from the already-earned
influence/access structure, or does it remain an irreducible input?*
More concretely: is a constant rescaling of spatial length necessarily
represented as a pure change of units once the geometry is dynamically
reconstructed, while genuinely physical deformations remain observable?
**The critical distinction: a unit change ≠ a physical geometric
deformation.**

**Status of inputs:**
- **Earned input:** GS-1's access-relative geometry, namely that
  influence plus access data distinguish geometries as far as access
  reaches, and that the dynamic hierarchy sees what static geometry
  cannot.
- **On trial:** the principle identifying a constant length rescaling
  with a unit change.
- **Unresolved and kept separate:** absolute geometry.

**Forbidden as selectors (owner):** CARRIER; GeoInv; the desired TT
stress tensor; ω⁷; the supplied massless probe structure; a preselected
spatial coupling; the conclusion that lengths must transform as units;
any reconstruction of a chosen metric that merely reproduces itself.

**Outcomes (owner):**
1. **DERIVED:** earned structure forces length-unit equivalence.
2. **CONSTRAINED-NONUNIQUE:** it restricts length behaviour but leaves
   physically distinct possibilities.
3. **CLASS-SPLIT:** the result depends on access or dynamical class.
4. **IRREDUCIBLE INPUT:** length equivalence needs an additional
   supplied principle.
5. **FAILS/NULL:** the discriminator itself doesn't survive.

**Most important control (owner):** *a true counterexample*, i.e. two
spatial descriptions with the same earned influence/access data that
differ in whether the transformation is merely a unit change.

## 1. THE DISCRIMINATOR (frozen before any number)

A transformation is a **pure unit change** iff it leaves every
**dimensionless accessible datum** invariant. For a unit-mass network K
(springs plus on-site pins), the dimensionless set 𝒟 is:
- (i) the normalized mode spectrum sₙ = (ωₙ − ω₀)/(ω_max − ω₀);
- (ii) the normalized resistance profile R(0,j)/R(0,1) along a lattice
  direction;
- (iii) the anisotropy ratio R(0, x-neighbour)/R(0, y-neighbour);
- (iv) the static–dynamic product R(0,1)·ω²_max, which is invariant
  under joint length and time unit changes;
- (v) hop distances, which are graph-integer.

The discriminator is |Δ𝒟| = the maximum absolute change over (i)–(iv),
with (v) compared exactly.

## 2. THE LEGS (frozen, predictions written before any number)

Substrate: a periodic 6 × 6 grid (N = 36), springs 1, pins 0.2, unit
masses, and a constant action with λ = 1.3.

- **L-U (co-stretch: every coupling, springs AND pins, scaled by
  1/λ).** **Prediction:** |Δ𝒟| < 1e-12 (halt-grade identity).
  Frozen consequence: a uniform co-stretch **is** a pure unit change,
  a data identity. This is the classification half of Sel-4x, and it
  follows from dimensional analysis. It is not a selection.
- **L-R (rigid stretch: springs scaled by 1/λ, pins held fixed).** The
  geometric couplings stretch while the intrinsic scale (correlation
  length ξ² = k/p) does not. **Prediction:** |Δ𝒟| > 1e-3. Frozen
  consequence: a **constant rescaling of spatial couplings is not
  necessarily a unit change.** Whether a given one is depends on
  whether the intrinsic scales co-stretch. That choice is the content
  of Sel-4x, and it is exactly EQ-1's rigid-scale issue.
- **L-A (genuine deformations).**
  - Anisotropic: only the x-springs scaled by 1/λ.
  - Inhomogeneous: springs in half the grid (columns 0–2) scaled by
    1/λ.

  **Predictions:** |Δ𝒟| > 1e-3 for both, with the anisotropy ratio
  moving off 1 for the anisotropic case. Hop geometry (v) is unchanged
  in both, recorded: weights are invisible to graph-integer geometry
  and visible to metric/dynamic data.
- **L-P (earned admissibility).** Every modified K in L-U, L-R and L-A
  is PSD (min eigenvalue > 0), so 𝔠_full admits it. Frozen
  consequence: earned admissibility does not forbid a constant probe
  that acts as a rigid stretch or a deformation.
- **L-C (the owner's counterexample, under limited access).**
  - Hidden network: the GS-1 path a–1–2
    (K = [[1.2, −1, 0], [−1, 1.7, −0.7], [0, −0.7, 0.7]]), accessed at
    a only.
  - Description 1: a pure unit change, K/λ.
  - Description 2: the unit change composed with a non-isometric
    interior deformation, (1 ⊕ O(0.4))(K/λ)(1 ⊕ O(0.4))ᵀ.
  - **Predictions:** single-site data G_aa(ω) at ω = 0.3 and 0.9 are
    identical to < 1e-12 (halt-grade). Description 2 is not a pure
    unit change of the hidden network (a couples to node 2), so its
    full-access data differ by > 1e-3.

  Frozen consequence: under limited access, **"unit change" and "unit
  change plus physical deformation" cannot be told apart.** The
  counterexample survives.

## 3. OUTCOME RULE (frozen, mechanical)

- **Classification:** if L-U holds, "uniform co-stretch ≡ unit change"
  is a data identity.
- **The Sel-4x hypothesis ("any constant length rescaling is a unit
  change"):** FALSE as a general statement if L-R shows a constant
  rescaling that is observable.
- **Selection:**
  - DERIVED only if some earned constraint excludes the rigid-stretch
    and deformation actions.
  - If L-P admits all of them: **IRREDUCIBLE INPUT**, reduced to the
    co-stretch declaration ("a constant probe rescales every scale,
    intrinsic ones included").
- **Decidability:** if full-access data separate the two descriptions
  (L-C) while limited-access data cannot, then **CLASS-SPLIT by
  access**.
- **Overall:** the components are reported separately.

## 4. CONTROLS

- Halt-grade: the L-U identity.
- Halt-grade: the L-C single-site identity.
- Exact eigenvalues use cyclic Jacobi.
- Resistance uses an exact inverse (pins make K invertible).
- None of the forbidden selectors appears anywhere.

## 5. DELIVERABLES AND STOP

1. `calc/sx1_length.py` (pure stdlib; emits `SX1_LENGTH_RESULT.json`,
   sha-hashed).
2. `SX1_LENGTH_EQUIVALENCE_VERDICT_01.md` and a closing comment on
   Issue #2.
3. **HARD STOP after the Sel-4x verdict.** No D = 4 TT/ξ.
