# GS-1 — CAN GEOMETRY BE SELECTED FROM INFLUENCE/ACCESS DATA? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5837643174**. CA-1 was accepted at recorded strength. **Binding
status:**
- CARRIER is IRREDUCIBLE/SUPPLIED (an access-seed coincidence);
- the shared-substrate result is a representational/access degeneracy
  in the tested class, **not** a universal ontology;
- the classical-dissipative escape remains open.

**Target (owner, verbatim):** *Can the G-2 geometry itself be derived
from the already-earned influence/access structure without identifying
it with a chosen substrate operator, coordinate representation, or
preselected metric?*

**Outcomes:** DERIVED/SELECTED · CONSTRAINED BUT NONUNIQUE · CLASS-SPLIT ·
IRREDUCIBLE INPUT · FAILS/NULL.

**Success bar (owner):** a geometry selector is earned only if
previously established influence/access structure **eliminates a
genuinely different geometric candidate**. *Showing that a chosen K
reconstructs itself is not selection.*

**Design compliance:**
1. *Start from influence/access data.* Each leg generates interface
   data G_AA(ω) = [(K − ω²)⁻¹]_AA from a hidden network. The only
   reconstruction and selection inputs are that data. The legs then
   ask which **genuinely different candidate geometries** the data
   eliminates.
2. *Candidates that agree on low-order data but differ globally or
   metrically:*
   - an isospectral partner (all trace moments matched);
   - a degree-preserving rewire;
   - the Y–Δ pair (static data identical);
   - a single-site realization family (full dynamic data identical);
   - prism vs Möbius ladder (local walks matched to order n − 1).
3. *G-2's one-site collapse and sub-circumference limits are preserved*
   in legs L-P and L-T. They are not claimed solved.
4. *First distinguishing accessible invariant:* reported per pair.
5. *Machinery vs selection kept separate.* Inverses, Schur complements,
   spectral matching and walk counts are standard mathematics
   (NULL-REDUNDANT). Only *what the data eliminates* is a finding.
6. *Not used as selectors:* ω⁷, probe-field assumptions, retained-sector
   assumptions, GeoInv, Sel-4x or CARRIER.
   - The one extra criterion used, **LocPos** (every edge weight and
     on-site pin ≥ 0: a network of passive elements), is chartered as
     a CANDIDATE, not earned. 𝔠_full requires only that K is PSD
     overall.
7. *C_cons and universal reach* are recorded as dependencies of the
   gravity chain. They play no role here.
8. *Fences:* ω⁷, ℏ, GR-1 3D red, D = 4 TT/ξ and operator ordering are
   untouched.

## 1. THE LEGS (frozen, predictions written before any number)

Unit masses throughout, so a network is K = weighted Laplacian + pins.

- **L-F (full site-resolved access).**
  - *Hidden network:* a 3×3 grid, unit springs, pins 0.1 (N = 9).
    Data: the full G(ω) at ω = 0.5.
  - (a) The reconstruction K̂ = ω² + G(ω)⁻¹ equals the hidden K to
    < 1e-9 (halt-grade; machinery).
  - (b) **Isospectral candidate** K_Q = QKQᵀ, with Q a product of
    frozen Givens rotations. Trace moments tr K^m, m = 1..8, match to
    1e-10 relative, so every global spectral moment agrees. Yet the
    **site-resolved data differ by > 1e-3: eliminated.** Global
    spectral data cannot select this geometry; local access can.
  - (c) **Degree-preserving rewire:** the 2-switch (0,1),(7,8) →
    (0,8),(1,7). Local data differ by > 1e-3: eliminated. The first
    differing trace-moment order is reported.
- **L-M (multi-site boundary access: static vs dynamic).**
  - *Hidden network:* a **Y**, i.e. boundary sites a, b, c plus an
    interior node o, with spring weights 1.0, 1.5, 2.0 and boundary
    pins 0.1. Access A = {a, b, c}.
  - *Candidate:* the **Δ** on a, b, c with star–mesh weights
    w_ij = w_i w_j / Σw and the same pins.
  - (a) Static boundary data (Schur complement at ω = 0) are identical
    to < 1e-12 (halt-grade). **G-2's static resistance geometry cannot
    tell Y from Δ.**
  - (b) Dynamic boundary data at ω = 0.3 differ by > 1e-3. **The
    dynamic influence hierarchy eliminates Δ.**
  - (c) The first distinguishing invariant is the ω² coefficient of
    the low-frequency expansion of G_AA⁻¹. The order-0 difference is
    < 1e-12 and the order-ω² difference is ‖K_AI K_II⁻² K_IA‖ > 1e-3.
- **L-P (single-site access: the one-site collapse, carried).**
  - *Hidden network:* the path a–1–2 with weights w₁ = 1 and w₂ = 0.7,
    pin_a = 0.2, no interior pins. Access A = {a}.
  - *Candidate family:* interior rotations
    K(θ) = (1 ⊕ O(θ)) K (1 ⊕ O(θ))ᵀ for θ ∈ [0, π), 3600 points.
  - (a) The data G_aa(ω) at ω = 0.3 and 0.9 are identical across the
    family to < 1e-12 (halt-grade).
  - (b) The family is **non-isometric**: for generic θ, a couples to
    both interior nodes, which changes the edge set.
  - (c) 𝔠_full admits every member (the spectrum is invariant).
  - (d) **LocPos (candidate):** the admissible θ set is **REPORTED**.
    That is the count of LocPos-admissible θ more than 1e-3 away from
    the isometric images θ ∈ {0, π/2}.
  - Frozen consequence: under single-site access, earned structure
    leaves a non-isometric family (UNDERDETERMINED, G-2's collapse
    carried). Whether LocPos cuts it is read mechanically.
- **L-T (topology: the horizon, carried).** Prism C₈ × K₂ vs Möbius
  ladder M₁₆: both 3-regular and locally identical. **Prediction:**
  the local closed-walk counts (A^m)₀₀ are equal as exact integers for
  m < 8 and first differ at **m = 8 = n**. The global spectra differ
  (distinguishable only with complete data). Consistent with G-2's
  invariant-order ladder.

## 2. OUTCOME RULE (frozen, mechanical)

- **Bar met** iff at least one genuinely different candidate is
  eliminated by influence/access data: (L-F b or c) or (L-M b).
- **Full access:** **SELECTED-IN-CLASS** (unique up to relabeling) if
  L-F holds.
- **Multi-site boundary access:**
  - the dynamic hierarchy selects the interior *dimension* (Y over Δ);
  - the interior geometry follows L-P: **CONSTRAINED-NONUNIQUE**.
- **Single-site access:** **UNDERDETERMINED**, unless LocPos leaves
  only isometric images. In that case: "selected by LocPos
  (candidate)", not earned.
- **Overall: CLASS-SPLIT by access.** Geometry is determined exactly as
  far as access reaches. The access boundary itself is supplied
  (P-5, P-6).

## 3. CONTROLS

- Halt-grade: the full-access reconstruction.
- Halt-grade: the Y–Δ static identity.
- Halt-grade: the single-site family data identity.
- Walk counts are exact integers.
- Matrix inverses use Gaussian elimination with partial pivoting.

## 4. DELIVERABLES AND STOP

1. `calc/gs1_geometry.py` (pure stdlib; emits `GS1_GEOMETRY_RESULT.json`,
   sha-hashed).
2. `GS1_GEOMETRY_SELECTION_VERDICT_01.md` and a closing comment on
   Issue #2.
3. **HARD STOP after the geometry verdict.** No D = 4 TT/ξ and no
   Sel-4x.
