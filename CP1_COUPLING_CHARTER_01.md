# CP-1 — CAN THE MINIMAL-STRESS COUPLING BE SELECTED WITHOUT INSERTING IT? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner ruling given in-session,
recorded in `GR1_CP1_OWNER_RULING_01.md`. **Question (owner, verbatim):**
*Can the minimal-stress coupling form be selected from 𝔠_full + access +
geometry, without inserting it?* The answer is NOT presumed. Allowed
outcomes (owner): **COUPLING-DERIVED · CONSTRAINED-NONUNIQUE ·
CLASS-SPLIT · IRREDUCIBLE-INPUT · FAILS.**

**Held fixed and NOT attacked here (owner: kept separate):** the
retained-sector import — every leg assumes the gapless retained sector
with its declared dispersion; nothing below is allowed to explain
gaplessness. Geometry-selection stays a separate fork. **Fences:** ω⁷ not
reopened or relabeled (v3 20/20 by hash only); the GR-1 3D red stays red;
no Einstein/field equations; ℏ located-not-generated; no absolute
exponent compared across conventions (increments and classes only);
Λ_R, Matsubara, Π₀, U5 fenced; type-III boundary map only.

## 1. THE DECLARED COUPLING FAMILY (frozen before any number)

Symmetric rank-2 vertices bilinear in two scalar legs p₁, p₂, local, at
most two derivatives, parity- and time-reversal-even, in the basis

  **V^{μν} = a·(p₁^μp₂^ν + p₂^μp₁^ν) + g·(p₁^μp₁^ν + p₂^μp₂^ν)
            + b·η^{μν}(p₁·p₂) + c·η^{μν}**   (mostly-plus η).

Named members: **canonical minimal stress (1, 0, −1, 0)**; the
**improvement direction** ξ(η^{μν}k² − k^μk^ν), k = p₁ + p₂, which on
massless legs is ξ·(−1, −1, 2, 0). **Strain-probe kinematics** (the GR-1
L-X class: zero net spatial momentum, p₁ = (ω, q), p₂ = (ω, −q)):
V^{xx} = −2aq² + 2gq² − b(ω² + q²) + c. **Analytic exponent classes
(predictions):** with ω ≈ q, V^{xx} ≈ 2(−a + g − b)q² + c + O(q⁴); so
c ≠ 0 → slope 0; (−a + g − b) ≠ 0 → base 4; the **+4 locus**
{c = 0, a − g + b = 0, b ≠ 0} → 8. The locus is a PLANE, not a point.

## 2. THE LEGS (frozen)

All exponents use GR-1's L-X instrument unchanged (ω(q) = q − αq³,
α = 0.05; exact Newton roots; J = V²/|dω_tot/dq|; slope =
log₂[J(0.2)/J(0.1)]).

- **L-F (exponent map + non-injectivity):** canonical (1,0,−1,0) → 8;
  improved ξ = 0.2, i.e. (0.8,−0.2,−0.6,0) → 4; **on-locus but
  non-canonical (0,1,1,0) → 8**; contact (1,0,−1,0.01) → 0. Gates ±0.2
  each. Frozen consequence: if (0,1,1,0) lands at 8, the exponent does
  not identify the coupling (the +4 is a property of a plane of
  couplings, not of minimal stress as such).
- **L-H (𝔠_full as a selector — expected NULL):** 30-mode baths
  (ω_tot ∈ [0.05, 1.0]) built from four vertices — canonical, improved
  ξ = 0.2, contact, and the non-metric "mass-only" modulation of L-M —
  3×3 two-time Gram over {B(0), B(4), B(11)}; gate: each PSD
  (min eig / C₀ ≥ −1e-12). Frozen consequence: all admissible ⇒ the
  admissible hierarchy does not select the coupling (NULL as selector).
- **L-C (conservation — locality + symmetry):** constraint rows
  k_μV^{μν} = 0 on 16 random on-shell massless pairs (mixing co- and
  counter-movers in D = 2; generic in D = 4). Null space by eigenvalues
  of the 4×4 Gram (tol 1e-10 × max). **Predictions:** nullity 2 in both
  D; canonical and improvement vectors each lie in it (residual
  < 1e-10). Frozen consequence: CONSTRAINED-NONUNIQUE — one free ξ.
- **L-W (conservation + IR Weyl/tracelessness):** add rows
  η_μνV^{μν} = 0 on-shell (the retained sector is gapless and IR
  scale-invariant; tracelessness is its Weyl symmetry — a symmetry
  already in the class, not an import). **Predictions:** nullity 1 in
  both D; **D = 2 direction = canonical** (residual < 1e-10); **D = 4
  direction ∝ (2, −1, −1, 0)** (the improved, conformally-coupled
  tensor). Strain-probe slopes of the selected directions: **D = 2 → 8
  (on-locus); D = 4 → 4 (off-locus)**, gates ±0.2.
- **L-TT (access class — the transverse-traceless probe, D = 4):** for
  16 random pairs, project each basis tensor's spatial block with the
  TT projector relative to k̂ (Λ(X) = PXP − ½P·tr(PX), P = 1 − k̂k̂).
  **Predictions:** TT(b) = TT(c) = 0 and TT(g) = −TT(a) (each < 1e-12);
  the TT image of the whole family has **rank 1**. Frozen consequence:
  for TT probes the coupling FORM is forced up to amplitude — the
  minimal-stress import is VACUOUS in that access class (whether the
  TT channel then carries +4 is kinematic, v3 territory, NOT
  re-adjudicated here).
- **L-M (geometric coupling — a CANDIDATE principle, chartered as its own
  hypothesis, not assumed):** "the probe couples to the retained sector
  only through proper distance" = metric variation of the retained
  dispersion under g_xx = 1 + h: **V_metric = ½[q²D′(q²) − D(q²)]**,
  D = ω². Two dispersions: continuum D = (q − αq³)² and nearest-neighbour
  lattice D = 4 sin²(q/2). **Predictions:** slopes 8 ± 0.2 on both;
  V_metric/q⁴ → −α (continuum) and −1/24 (lattice) within 1% at
  q = 0.05; V_metric/V_canonical → 0.5 within 1% at q = 0.05 (metric
  coupling IS canonical minimal stress in the IR, up to normalization).
  **Counterfactual — material modulations** (mass × (1+μh), stiffness
  × (1+κh)): V = −(μ + κ)D/2; on the impedance locus μ = −κ the vertex
  is identically zero (< 1e-14, both dispersions); mass-only (1,0) and
  stiffness-only (0,1) → slope 4 ± 0.2. Frozen consequence: if these
  land, then within {mass, stiffness, proper-distance} modulations the
  +4 arises ONLY from proper-distance (metric) coupling — the
  minimal-stress import REDUCES to the geometric-coupling (equivalence)
  principle at ξ = 0. Because that principle is not already in 𝒯, a
  reduction is **not** a discharge.

## 3. OUTCOME RULE (frozen, mechanical)

- **COUPLING-DERIVED** only if some principle ALREADY in 𝒯 (locality,
  symmetry incl. conservation and IR Weyl, 𝔠_full, access, recovered
  geometry) selects the on-locus coupling uniquely in EVERY tested class.
- **CLASS-SPLIT** if selection succeeds in some classes and fails in
  others (expected branch: D = 2 selected; D = 4 strain not; TT vacuous).
- **CONSTRAINED-NONUNIQUE** for any class where a free parameter spans
  on- and off-locus members.
- **IRREDUCIBLE-INPUT** if no tested principle constrains beyond the
  family.
- **FAILS** if any construction fails.
Components reported per class, never averaged. **Class-4 consequence:**
the minimal-stress import is DISCHARGED only on COUPLING-DERIVED;
otherwise it stays load-bearing, restated in its reduced form with the
exact residual named. Class-4 stays open unless both remaining imports
are discharged, and the retained-sector import is not attacked here.

## 4. CONTROLS

Halt-grade: the L-M impedance-locus zero and the L-TT algebraic
identities (a breach is an instrument bug, never physics). Null-space
tolerance fixed above; each null vector is re-verified against every
constraint row. Matched control: canonical slope recomputed in-run
must reproduce GR-1's 8.005 to 1e-9. Random momenta from a fixed seed
(frozen: 20260925).

## 5. DELIVERABLES AND STOP

1. `calc/cp1_coupling.py` (pure stdlib; emits `CP1_COUPLING_RESULT.json`,
   sha-hashed).
2. `CP1_COUPLING_VERDICT_01.md` + closing comment on Issue #2.
3. **HARD STOP at the verdict.** The retained-sector import and
   geometry-selection remain separate forks for the owner.
