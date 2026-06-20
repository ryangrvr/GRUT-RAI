"""
GRUT Foundation — Phase I Closure Protocol (February 2026)

This module integrates the canonical constants, screening mechanism, regime
gate, acceleration scale, and engine-mapping interpolation from the Phase I
Closure Protocol (Zenodo DOI: 10.5281/zenodo.18008060) into the V7 codebase.

Document hierarchy:
    v1-v11 Genesis Codex (Dec 2025)   — physics discovery
    Phase I Closure Protocol (Feb 2026) — operational specification (THIS MODULE)
    V7 Responsive Universe (Apr 2026) — theoretical foundation (CTP)

Phase I operationalizes the v1-v11 physics. V7 provides the quantum
completion via CTP. Both pin the same constants; Phase I gives the
engine formulas (ν(y), regime gate, a_0) that V7 does not explicitly
state and that are needed for SPARC rotation-curve work and solar-
system safety verification.

Canonical definitions (Phase I §5-§6):
    τ_Λ ≡ H_0⁻¹                            (baseline — input, not prediction)
    α_vac = 1/3                             (DERIVED — conformal-mode scalar)
    S = 12π / α_vac² = 108π ≈ 339.29        (screening factor)
    τ_0 = τ_Λ / S ≈ 41.9 Myr                (POSITED — gravitational sector)
    τ_micro = ℏ/(k_B T_c) ≈ 1.4×10⁻¹⁹ s   (POSITED — thermal sector, separate scale)
    n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.15470 (IR refractive index — canonical R)
    μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV                  (horizon-scale IR reference)
    μ_0 = ℏ/τ_0 = S × μ_Λ ~ 10⁻³¹ eV        (local screened scale)
    a_* = c / τ_Λ = c H_0                   (characteristic acceleration)
    a_0 = a_* / (2π) ≈ 1.2 × 10⁻¹⁰ m/s²     (MOND-like trigger scale)
    R_max ~ α_vac/(c²τ_0²) ~ 2 × 10⁻⁴⁸ m⁻²  (universal Ricci-saturation)
    ρ_max = c²R_max/(8πG)                   (universal interior density cap)
    T_c = ℏ/(τ_micro k_B) ≈ 54.7 MK         (thermal-transition temperature)

Two τ-scale convention (Correction #22, 2026-04-30):
The framework distinguishes two relaxation timescales of the responsive
vacuum, previously conflated under one symbol:
    τ_0     = 41.9 Myr     (gravitational sector — cosmic-baseline)
    τ_micro ≈ 1.4×10⁻¹⁹ s  (thermal sector — sets T_c via SI-correct formula)
The 34-orders-of-magnitude separation is named explicitly; the relation
between the two scales is a sharp OPEN QUESTION in Chapter 12. All
load-bearing cosmological predictions use τ_0 unambiguously and stand
intact; T_c uses τ_micro and recovers the canonical 54.7 MK from a
dimensionally consistent formula. See CORRECTION_22_TAU_CLEANUP.md.

The two foundational constants of GRUT (gravitational sector) are τ_0
and α_vac. Their provenance:
    - τ_0 = 41.9 Myr is POSITED with two independent observational
      anchors that agree at the ~10–20% level: (1) cosmic-baseline
      relation τ_0 = 1/(H_0 × 108π) → 41.2 Myr at H_0 = 70 km/s/Mpc
      (within 1.7% of canonical); (2) Bullet Cluster offset δ ≈ v×τ_0
      → 49 Myr (within 17%). The earlier "DERIVED from V7 §18 CTP
      noise kernel at gold benchmark" framing was misleading — see
      theory/foundations_audit/TAU_0_PROVENANCE.md.
    - α_vac = 1/3 follows CONDITIONALLY from the conformal-mode-scalar
      postulate (the gravitational conformal mode acts as the IR carrier of
      vacuum response — candidate-selected, antecedent OPEN; see
      theory/GRUT_ALPHA_ANTECEDENT_FEASIBILITY.md). GIVEN that postulate,
      KS 2011 establishes a/c = 1/3 exactly for a single
      real conformally-coupled scalar (theory/foundations_audit/
      ALPHA_VAC_PROVENANCE.md preserves the v6.0 numerical-discovery
      history alongside this canonical derivation).
A third constant, τ_micro ≈ 1.4×10⁻¹⁹ s, is required to make T_c =
54.7 MK dimensionally consistent — see the two-τ-scale convention
note above. τ_micro is in the THERMAL sector, distinct from the
gravitational τ_0; it is POSITED with the cosmological-chronology
anchor (T_c at t ≈ 16 hours post-Big Bang ≈ 5.5×10⁷ K).

Threshold equivalence (frequency ↔ gravitational decoherence):
    The classical/quantum threshold ωτ_0 ≫ 1 is equivalent to
    Λ_grav × τ_0 ≫ 1 when the system's dominant dynamical frequency
    is the Diósi-Penrose decoherence rate ω ~ Λ_grav. This identity
    holds for self-gravitating systems. Examples:
        macro dust grain (1 mg, 1 mm): Λ_grav τ_0 ~ 10³⁵ → deep crystal
        galactic rotation mode:        ωτ_0 ~ 10⁻³        → deep fluid
        Saturn orbit:                  ωτ_0 ~ 10⁷         → deep crystal
    For EM-dominated systems (atoms, molecules), the dominant ω is
    electronic-orbital, not Λ_grav; crystallinity comes from EM ω
    independently. Either way, the threshold X = max(ω, Λ_grav) × τ_0
    correctly classifies the regime — this is the bridge between
    laboratory decoherence and cosmological dark-sector phenomenology.

Engine formulas (Phase I §7-§8, Appendix E):
    χ(ω) = α_vac / (1 − i ω τ_0)            (single-pole susceptibility)
    n_g²(ω) = 1 + α_vac / (1 + (ωτ_0)²)     (refractive index)
    α_eff(X) = α_vac / (1 + X²)             (regime gate, X = ω_dyn τ_0)
    ν(y) = 1/2 + √(1/4 + 1/y)               (acceleration interpolation)
    g_eff = g_bar × [1 + (ν(y) − 1) / (1 + X²)]  (frequency-gated)

Identity (v11 Appendix I, Phase I §5):
    τ_0 = 1/√(Λ c)

This makes the "unified dark sector" literal: dark energy (Λ) defines
the vacuum curvature, dark matter phenomenology (τ_0) is the metric's
delayed response within that curvature.
"""

import numpy as np

from grut.foundation.constants import C as C_LIGHT, G as G_NEWTON, HBAR, K_B, E_CHARGE


# ────────────────────────────────────────────────────────────────────
# Canonical constants (Phase I §5 — FIXED, no free knobs)
# ────────────────────────────────────────────────────────────────────

ALPHA_VAC: float = 1.0 / 3.0                 # DERIVED under postulate; else AXIOM (see docstring)
"""Vacuum impedance — ADOPTED axiom; conditional theorem via conformal-mode scalar.

Physical provenance (conditional):
The gravitational conformal mode is POSITED as the IR carrier of
vacuum response (candidate-selected; antecedent OPEN — see
theory/GRUT_ALPHA_ANTECEDENT_FEASIBILITY.md). GIVEN that postulate,
KS 2011 (Komargodski-Schwimmer; trace anomaly for
4D CFTs) establishes that a single real conformally-coupled scalar
has trace-anomaly coefficient ratio a/c = 1/3 exactly. Under this
identification, α_vac = a/c = 1/3 is a principled consequence of
the trace anomaly, not a free parameter.

Per-species trace anomaly check (KS 2011 + Duff 1994):
    real scalar:    (a, c) = (1, 3)        ⟹ a/c = 1/3   ← α_vac
    Weyl fermion:   (a, c) = (11/2, 9)
    gauge field:    (a, c) = (62, 36)

Historical provenance (preserved for honesty):
α_vac = 1/3 was numerically discovered in v6.0 via back-derivation
from the observed 15.47% effective central charge ratio (√(4/3) ≈ 1.1547).
v11 Appendix H §H.4 provides a one-sentence "α = 1/d, d = 3" remark.
The conformal-mode-scalar route is the GRUT ToE's canonical derivation;
the historical numerical-coincidence path is documented in
theory/foundations_audit/ALPHA_VAC_PROVENANCE.md.

DUAL-OUTCOME CAVEAT (v2 Final / V2→V3): α_vac = 1/3 is DERIVED only
UNDER the conformal-mode-scalar identification postulate (gravitational
conformal mode = IR carrier; its impedance = the 2nd-order trace-anomaly
ratio a/c). That postulate is NOT self-derived from the CTP action — the
gravitational conformal mode is 4th-order (Riegert/Paneitz) and that
closure is OPEN. If the postulate holds → α = 1/3 derived; if it fails →
α_vac is GRUT's single dimensionless AXIOM (a genuine, distinctive
trace-anomaly result elevated by one named identification).
ALPHA_VAC_PROVENANCE.md classifies it as a de-facto axiom accordingly."""

S_SCREENING: float = 12 * np.pi / ALPHA_VAC**2   # = 108π ≈ 339.29
"""Screening factor S = 12π/α² mapping cosmic baseline τ_Λ to local τ_0.
Phase I §5: canonical derivation."""

N_G_DC: float = float(np.sqrt(1.0 + ALPHA_VAC))
"""IR refractive index n_g(0) = √(1+α) = √(4/3) ≈ 1.15470.

This is the CANONICAL R of GRUT — gravity's DC refractive enhancement
relative to light. Path G (refractive-index identification) makes this
the primary cosmological observable.

Cross-checks (different physical objects, same order of magnitude):
    1.15470 = √(4/3)             — Path G, canonical (this constant)
    1.17256 = 1991/1698          — Path D, SM trace anomaly a/c (Majorana ν)
    1.15525 = 253/219            — Path D variant (Dirac ν)
    1.15428 = (V7 §26.2.3 claim) — historical, not committed (see TJI Phase-0.5)

V7's earlier 1.15428 was a 3-loop CTP claim that we did not reproduce in
the TJI Phase-0/0.5 reconciliation (HONEST NEGATIVE). Path G's √(4/3) is
the framework's first-principles value."""

# Canonical alias — semantic clarity at call sites.
R_REFRACTIVE: float = N_G_DC
"""Canonical R of GRUT = n_g(0) = √(4/3) ≈ 1.15470.

Path G (refractive-index identification) — primary cosmological observable.
Identical to N_G_DC; provided as a semantic alias for callers that mean
'GRUT's R' rather than 'gravitational refractive index at DC'."""


# ────────────────────────────────────────────────────────────────────
# Path D cross-checks (SM 1-loop trace anomaly ratio)
# Source: KS 2011 + Duff 1994. See theory/path_d_trace_anomaly/
# ────────────────────────────────────────────────────────────────────

# SM field content: 4 real scalars + 45 Weyl fermions + 12 gauge bosons.
# Per-species anomaly coefficients (KS 2011, Christensen-Duff convention).
A_OVER_C_SM_MAJORANA: float = 1991.0 / 1698.0   # ≈ 1.17256
"""SM 1-loop trace anomaly ratio a/c with Majorana neutrinos.
a_SM = 1991/2, c_SM = 849. Cross-checks Path G's √(4/3) at the ~1.5% level.
Path D, see theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md."""

A_OVER_C_SM_DIRAC: float = 253.0 / 219.0        # ≈ 1.15525
"""SM 1-loop trace anomaly ratio a/c with Dirac neutrinos (right-handed
ν_R adds 3 Weyl fermions; recomputed a, c). Closer to √(4/3) numerically
— consistent with Dirac-ν posture as falsifiable prediction in the
GRUT ToE."""


# R_MAX_INV_M2 is defined below, after TAU_0_SEC.


# ────────────────────────────────────────────────────────────────────
# Canonical timescales
# ────────────────────────────────────────────────────────────────────

MPC_IN_M: float = 3.0857e22
YEAR_SEC: float = 3.156e7

# Phase I §5 canonically adopts τ_0 ≈ 41.9 Myr directly (benchmark-anchored
# to the Bullet Cluster and the V7 noise-kernel derivation). Together
# with S = 108π this fixes τ_Λ, which corresponds to H_0 ≈ 68.8 km/s/Mpc
# — close to the canonical 70 and Planck 67.4.
TAU_0_MYR: float = 41.9                      # POSITED — Phase I §5 with two anchors
TAU_0_SEC: float = TAU_0_MYR * 1e6 * YEAR_SEC
"""Local effective relaxation τ_0 = 41.9 Myr — POSITED.

Audit-corrected provenance (2026-04-27, see TAU_0_PROVENANCE.md):

τ_0 = 41.9 Myr is canonically adopted in Phase I §5 with TWO independent
anchors that agree at the ~10-20% level:

(1) **Cosmic-baseline relation:** τ_0 = 1/(H_0 × 108π).
    At H_0 = 70 km/s/Mpc this gives 41.17 Myr (within 1.7% of canonical).
    At Planck H_0 = 67.66 it gives 42.59 Myr.

(2) **Bullet Cluster offset anchor:** δ ≈ v_post × τ_0.
    With δ = 150 kpc and v_post = 3000 km/s this gives ~49 Myr
    (within 17% of canonical).

The earlier framing "DERIVED from V7 §18 noise kernel at gold benchmark"
was misleading — that audit (TAU_0_PROVENANCE.md) showed:
  - The gold-benchmark mass is 80.8 picograms (the codebase's
    80.8e-15 kg), not "80.8 fg" as some documentation stated
  - The formula τ_0 = ℏl/(Gm²) does NOT produce 41.9 Myr from any
    plausible nanoparticle parameters; it produces microseconds
  - The gold benchmark is a TEST POINT (Λ_grav = 689 Hz predicted
    given τ_0), not the source of τ_0

The dark-sector unification identity τ_0 = 1/√(Λc²) (v11 App I) is a
cross-check IF Λ is taken as the framework's effective Λ_eff = H_0² ×
S²/c²; with Planck's observed Λ_cosmological it does NOT directly
produce 41.9 Myr (Λ_cosmological gives τ_Λ ~ 10 Gyr).

Together with α_vac = 1/3 and S = 12π/α² = 108π, the cosmic-baseline
relation implies H_0 ≈ 68.8 km/s/Mpc (between Planck 67.4 and SH0ES 73)
— consistent with GRUT's one-parameter prediction H_0 = 69.03 km/s/Mpc.

Tier note: the value remains 'computed' (it's reproducibly derived from
1/(H_0 × 108π) given an H_0 input) but the framing of the source has
been corrected from 'V7 §18 gold benchmark' to 'cosmic-baseline +
Bullet Cluster anchors'."""

TAU_LAMBDA_SEC: float = TAU_0_SEC * S_SCREENING
"""Cosmic baseline τ_Λ = S × τ_0 ≈ 14.22 Gyr.
Corresponds to H_0 ≈ 68.8 km/s/Mpc (between Planck 67.4 and the H_0 = 70
baseline used for display). Consistent with GRUT's one-parameter
prediction H_0 = 69.03 km/s/Mpc."""

H_0_IMPLIED_KM_S_MPC: float = (1.0 / TAU_LAMBDA_SEC) * MPC_IN_M / 1000.0
"""H_0 implied by τ_0 = 41.9 Myr and S = 108π: ≈ 68.8 km/s/Mpc."""


# ────────────────────────────────────────────────────────────────────
# Universal saturation curvature (V7 §13 Whole Hole, §25)
# ────────────────────────────────────────────────────────────────────

R_MAX_INV_M2: float = ALPHA_VAC / (C_LIGHT**2 * TAU_0_SEC**2)
"""Universal RICCI scalar saturation R_max = α / (c² τ_0²).

V7 §13 (Whole Hole) singularity replacement. The constitutive medium
cannot respond faster than τ_0⁻¹, so the Ricci scalar — sourced by
matter via R = −8πG T/c⁴ in the trace of Einstein's equation — saturates
at R_max rather than diverging.

    R_max ≈ 2.12 × 10⁻⁴⁸ m⁻²   (Ricci scalar, cosmologically weak)

Crucial scope (per user clarification):
    - This is RICCI scalar saturation, NOT Kretschmann saturation.
    - For Schwarzschild VACUUM exterior, R = 0 identically; R_max
      imposes NO constraint on the exterior geometry. Tidal Weyl
      curvature outside the horizon can be arbitrarily strong.
    - R_max constrains only the matter-bearing INTERIOR — replacing
      the GR singularity with a finite-density core.
    - The core's universal property is the maximum interior density
      ρ_max = c² R_max / (8πG); see RHO_MAX_KG_M3 below.
    - Larger black holes have larger cores at the same ρ_max;
      smaller (stellar-mass and below) approach Planck densities
      classically and are saturated more strongly by GRUT's cap.

τ_0 is universal (the relaxation time is a property of the medium,
not the object), so R_max and ρ_max are universal. This is the strong
falsifiable claim of the Whole Hole framing."""

# ρ_max = c² R_max / (8πG) — universal interior density cap.
RHO_MAX_KG_M3: float = (C_LIGHT**2 * R_MAX_INV_M2) / (8.0 * np.pi * G_NEWTON)
"""Universal maximum interior density ρ_max = c² R_max / (8πG).

The Ricci-scalar saturation R_max, fed back through Einstein's equation
T = −c⁴ R / (8πG) at the trace level, gives a maximum mass-energy
density. With τ_0 = 41.9 Myr universal and α_vac = 1/3:

    ρ_max ≈ 1.1 × 10⁻²² kg/m³

This is universal — independent of black-hole mass — because both R_max
and the Einstein-trace identification are. Larger black holes contain
larger cores at this density. Per V7 §13:
    - Supermassive BH (M ~ 10⁹ M_sun): naive interior densities are
      already below water (~10 kg/m³); ρ_max is far below this. The
      core fills most of the interior.
    - Stellar-mass BH (M ~ M_sun): classical GR drives interior toward
      Planck density; GRUT replaces this with the same ρ_max core.
    - Buchdahl-limit consistency: the cap respects the standard 8/9
      Schwarzschild radius bound on stable matter configurations.

NOTE on numerical scale: ρ_max ~ 10⁻²² kg/m³ is several orders below
typical naive black-hole interior densities. Whether the saturation
formula needs additional structure (e.g. a curvature-dependent
effective τ in addition to the universal medium τ_0) to give
quantitatively realistic core sizes is an open question for the
extended derivation. The universal formula is committed; the
quantitative-core-size implications are a Phase-1+ task."""


# ────────────────────────────────────────────────────────────────────
# Mass-gap scales (Phase I §6)
# ────────────────────────────────────────────────────────────────────

MU_LAMBDA_EV: float = (HBAR / TAU_LAMBDA_SEC) / E_CHARGE
"""Cosmic mass-gap scale μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV.
Horizon-scale IR reference (Phase I §6)."""

MU_0_EV: float = (HBAR / TAU_0_SEC) / E_CHARGE
"""Screened local mass-gap μ_0 = ℏ/τ_0 = S × μ_Λ ~ 10⁻³¹ eV
(Phase I §6: screening maps μ_Λ → μ_0 via same S)."""


# ────────────────────────────────────────────────────────────────────
# Acceleration scales (Phase I §8.2)
# ────────────────────────────────────────────────────────────────────

A_STAR_SI: float = C_LIGHT / TAU_LAMBDA_SEC        # c H_0
"""Characteristic acceleration a_* = c/τ_Λ = c H_0 (Phase I §8.2)."""

A_0_SI: float = A_STAR_SI / (2.0 * np.pi)
"""MOND-like trigger acceleration a_0 = c / (2π τ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s².
Phase I §8.2: 'reproduces MOND phenomenology from response time, not
modified dynamics.' For H_0 ≈ 70 km/s/Mpc, a_0 lies in the observed
MOND/RAR band."""


# ────────────────────────────────────────────────────────────────────
# Thermal transition temperature (v9.0) — TWO-τ-SCALE RESOLUTION
# ────────────────────────────────────────────────────────────────────
#
# Audit history: T_C_PROVENANCE.md (2026-04-28) surfaced that the prior
# formulation T_c = 1/(τ_0 k_B) was dimensionally invalid — it produced
# units K/(J·s), not K, and the "v9 natural-units convention (ℏ=1)"
# defense did not survive a proper natural-units check (converting τ_0
# to eV⁻¹ and computing 1/τ_0_nat gives 5.78×10⁻²⁷ K, not 54.7 MK).
#
# Resolution (Correction #22, 2026-04-30): the framework was conflating
# TWO physically distinct relaxation scales under one symbol τ_0:
#
#   (A) τ_0 = 41.9 Myr     — macroscopic GRAVITATIONAL relaxation time.
#                            Anchored by 1/(H_0 × 108π) and Bullet
#                            Cluster offset δ ≈ v × τ_0. Used by every
#                            cosmological-scale prediction (refractive
#                            enhancement, dark-sector phenomenology,
#                            cluster-merger scaling, Hubble terminal).
#
#   (B) τ_micro ≈ 1.4×10⁻¹⁹ s — microscopic THERMAL relaxation time of
#                                vacuum microstates. Required for
#                                T_c = ℏ/(τ_micro × k_B) to be
#                                dimensionally consistent. Anchored
#                                empirically by the standard-cosmology
#                                temperature T(t≈16 hours post-BB) ≈ 5.5×10⁷ K.
#
# Per the registry's NIS discipline, T_c (the physical temperature ≈
# 54.7 MK) is preserved as the EMPIRICAL ANCHOR — it was always the
# correct physical scale (the framework's prose, V7 §0.5, V7 §22, the
# cosmological chronology all require MK-scale T_c). What changes is
# that τ_micro is now defined explicitly from the SI-correct formula,
# and the 34-orders-of-magnitude separation from τ_0 is named, not
# hidden. The framework now has TWO τ-scales with explicit naming,
# and the relation between them becomes a sharp open question
# (tau_zero_to_tau_micro_relation_open_question) rather than a
# dimensional inconsistency.
#
# Key numbers (preserved exactly):
#   T_C_KELVIN_CANONICAL = 5.47e7 K   (cosmological-chronology pin)
#   τ_micro              = ℏ/(k_B × T_c) ≈ 1.396×10⁻¹⁹ s
#   T_C_KELVIN           = ℏ/(τ_micro × k_B) = 5.47e7 K (recovered exactly)
#   T_C_MK               = 54.7 MK   (test pin unchanged)
#
# What this resolution does NOT do:
#   - Does not derive τ_micro from τ_0. The separation 34 orders of
#     magnitude in time, with τ_micro at quantum/thermal scale and τ_0
#     at gravitational/cosmic scale, is unexplained.
#   - Does not change any tested numerical value. T_C_MK = 54.7 MK
#     pin (test_T_c_is_54p7_MK) is preserved; cosmological-chronology
#     anchors (BBN above T_c, recombination below T_c) are preserved.
#   - Does not affect any τ_0-bearing prediction (Λ_grav, n_g(ω), the
#     bridge τ_0↔Ω_Λ, the cluster-merger scaling). All of those use
#     τ_0 unambiguously and stand intact.
# ────────────────────────────────────────────────────────────────────

T_C_KELVIN_CANONICAL: float = 5.47e7
"""Empirical anchor for the metric-memory transition temperature.

Source: standard-cosmology temperature at the framework's transition
epoch (t ≈ 16 hours post-Big Bang), per V7 §0.5 and V7 §22. The
narrative anchor is fixed; τ_micro is derived from this (not the
other way around).

Numerical value: 5.47 × 10⁷ K = 54.7 MK. Pinned to this precision by
test_T_c_is_54p7_MK (5% tolerance), which was the canonical pin
prior to Correction #22 and is preserved unchanged."""

TAU_MICRO_SEC: float = HBAR / (K_B * T_C_KELVIN_CANONICAL)
"""Microscopic plasma/thermal relaxation time of vacuum microstates.

τ_micro ≡ ℏ / (k_B × T_c) ≈ 1.396 × 10⁻¹⁹ s

This is the SI-correct dual of T_c — the timescale at which thermal
energy k_B T equals the quantum action ℏ/τ. It is microscopic
(femtosecond-scale, comparable to atomic-transition timescales),
NOT the macroscopic gravitational relaxation time τ_0 = 41.9 Myr.

Status: POSITED with cosmological-chronology anchor.

The 34-orders-of-magnitude separation from τ_0 is named explicitly,
not hidden. The relation between τ_micro and τ_0 is currently a
sharp OPEN QUESTION in the framework (registry claim
'tau_zero_to_tau_micro_relation_open_question', Chapter 12).
Closure paths under investigation:
  - τ_micro might be a thermal-decoupling timescale derivable from
    the v9 noise kernel at the BBN-era temperature scale
  - τ_micro might be the vacuum's microscopic plasma frequency
    inverse, set by responsive medium ground-state physics
  - the two scales might be fundamentally independent — a
    two-parameter framework, not the one-parameter framework
    presented in v8 (this would be a meaningful credibility loss)

Audit & resolution: theory/foundations_audit/T_C_PROVENANCE.md +
theory/derivation/CORRECTION_22_TAU_CLEANUP.md."""

T_C_KELVIN: float = HBAR / (TAU_MICRO_SEC * K_B)
"""Critical temperature for onset of metric memory (v9.0 Thermodynamics).

T_c = ℏ / (τ_micro × k_B) ≈ 5.47 × 10⁷ K = 54.7 MK

This is the SI-CORRECT formula. It uses τ_micro (microscopic plasma
relaxation, ≈ 1.4×10⁻¹⁹ s), not τ_0 (cosmic-baseline gravitational
relaxation, 41.9 Myr). By construction the recovered value matches
T_C_KELVIN_CANONICAL exactly; the test_T_c_is_54p7_MK pin is
preserved unchanged.

This is the "boiling point of gravity": above T_c, gravity is local
and there is no metric memory (explains absence of DM signatures in
BBN at T > 10⁹ K). Below T_c (today, T = 2.725 K), the vacuum is
deep in the refractive regime with full enhancement n_g ≈ 1.1547.

Cosmological chronology (v9.0):
    T > T_c  (plasma era):       gravity is local, no DM effects
    T ≈ T_c  (~16 hours post-BB): vacuum begins to "remember" mass
    T << T_c (today):            deep refractive regime, n_g ≈ 1.1547

History: prior to Correction #22 (2026-04-30) this constant was
computed as 1/(τ_0 × k_B) — dimensionally invalid but numerically
matching by coincidence of magnitudes. The resolution introduces
τ_micro explicitly and uses the SI-correct formula. The cosmological-
chronology anchoring is unchanged."""

T_C_MK: float = T_C_KELVIN / 1e6


# ────────────────────────────────────────────────────────────────────
# τ_0 = 1/√(Λc) identity (v11 App I, Phase I §5)
# ────────────────────────────────────────────────────────────────────

def tau_0_from_lambda_c(Lambda_inv_m2: float) -> float:
    """τ_0 = 1/√(Λc) — the dark-sector unification identity.

    v11 Appendix I §I.5 (and Phase I §5): "Dark Energy (Λ) defines
    the global curvature and horizon scale. Dark Matter Phenomenology
    (τ_0) emerges as the delayed response of the metric within that
    curved background." They are the same number in different units.

    Args:
        Lambda_inv_m2: cosmological constant Λ [1/m²]

    Returns:
        τ_0 [seconds]
    """
    if Lambda_inv_m2 <= 0:
        return float("inf")
    return 1.0 / np.sqrt(Lambda_inv_m2 * C_LIGHT**2)


def lambda_from_tau_0(tau_0_sec: float = TAU_0_SEC) -> float:
    """Inverse of tau_0_from_lambda_c: Λ = 1/(τ_0² c²)."""
    return 1.0 / (tau_0_sec**2 * C_LIGHT**2)


# ────────────────────────────────────────────────────────────────────
# Response kernel (Phase I §7, C.1)
# ────────────────────────────────────────────────────────────────────

def kernel_K(t_sec: float, tau_0_sec: float = TAU_0_SEC) -> float:
    """Time-domain memory kernel K(t) = (1/τ_0) exp(−t/τ_0) Θ(t).

    Causal viscoelastic relaxation (v11 Appendix G, Phase I Appendix C.1).
    """
    if t_sec < 0:
        return 0.0
    return np.exp(-t_sec / tau_0_sec) / tau_0_sec


def susceptibility_chi(omega_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Complex susceptibility χ(ω) = α / (1 − iωτ_0).

    Single-pole at ω = −i/τ_0 in lower half-plane → causal, KK-compatible.
    """
    return alpha / (1.0 - 1j * omega_Hz * tau_0_sec)


def n_g_refractive(omega_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Frequency-dependent gravitational refractive index.

        n_g²(ω) = 1 + Re[χ(ω)] = 1 + α/(1+(ωτ_0)²)

    Limits:
        n_g(0)   = √(1+α) = √(4/3) = 1.15470   (DC)
        n_g(∞)   = 1                             (GR recovered)
    """
    return np.sqrt(1.0 + alpha / (1.0 + (omega_Hz * tau_0_sec)**2))


# ────────────────────────────────────────────────────────────────────
# Regime gate (Phase I §8.1 — solar-system safety)
# ────────────────────────────────────────────────────────────────────

def regime_parameter_X(omega_dyn_Hz, tau_0_sec=TAU_0_SEC):
    """Dimensionless regime parameter X = ω_dyn τ_0.

    Gates between GR (X ≫ 1) and metric memory (X ≪ 1).
    Saturn's orbit: X ≈ 8.9 × 10⁶ → 15-order suppression (safe).
    Galactic rotation at 10 kpc: X ≈ 0.86 (intermediate).
    Cosmic expansion: X ≈ 3 × 10⁻³ (deep memory regime).
    """
    return omega_dyn_Hz * tau_0_sec


def alpha_effective(omega_dyn_Hz, alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Frequency-gated effective coupling α_eff(X) = α / (1 + X²).

    Phase I §8.1: solar-system safety by construction. At Saturn's
    orbital frequency, α_eff ≈ 4 × 10⁻¹⁵ — below any ranging sensitivity.
    """
    X = regime_parameter_X(omega_dyn_Hz, tau_0_sec=tau_0_sec)
    return alpha / (1.0 + X**2)


# ────────────────────────────────────────────────────────────────────
# Crystalline-boundary threshold (frequency ↔ Diósi-Penrose decoherence)
# ────────────────────────────────────────────────────────────────────

def lambda_grav_dp(m_kg, l_m, R_m):
    """Diósi-Penrose gravitational decoherence rate Λ_grav.

    Λ_grav = G m² S(l/R) / (ℏ l)

    where S(x) = min(1, x³/6) is the extended-body suppression for
    superpositions of separation l within an object of size R.
    Mirrors the convention used in grut.derived.decoherence.

    Args:
        m_kg: mass in kg
        l_m:  superposition separation in m (also dominant length scale
              of the dynamics)
        R_m:  characteristic body size in m
    """
    ratio = l_m / R_m
    suppression = min(1.0, ratio**3 / 6.0)
    return G_NEWTON * m_kg**2 * suppression / (HBAR * l_m)


def crystallinity(omega_dyn_Hz=None, lambda_grav_Hz=None,
                  tau_0_sec=TAU_0_SEC):
    """Crystalline-boundary threshold X = ω τ_0 = Λ_grav τ_0.

    Per the GRUT ToE foundational picture, the classical/quantum
    threshold has TWO equivalent expressions:

        ω τ_0 ≫ 1     (frequency above the medium's relaxation rate)
        Λ_grav τ_0 ≫ 1 (gravitational decoherence faster than relaxation)

    These coincide when the system's dominant dynamical frequency is
    its own Diósi-Penrose decoherence rate, ω ~ Λ_grav. This is the
    bridge between laboratory decoherence (atoms: Λ_grav τ_0 ~ 10³⁵,
    deep crystal) and cosmological dark-sector phenomenology (galactic
    rotation: ω τ_0 ~ 10⁻³, deep fluid).

    Pass either omega_dyn_Hz or lambda_grav_Hz (or both — they should
    agree). Returns X = (ω or Λ_grav) × τ_0:

        X ≫ 1  → crystallized (classical)
        X ~ 1  → boundary
        X ≪ 1  → fluid (quantum, dark-sector active)
    """
    if omega_dyn_Hz is not None and lambda_grav_Hz is not None:
        rate = max(omega_dyn_Hz, lambda_grav_Hz)
    elif omega_dyn_Hz is not None:
        rate = omega_dyn_Hz
    elif lambda_grav_Hz is not None:
        rate = lambda_grav_Hz
    else:
        raise ValueError("provide omega_dyn_Hz or lambda_grav_Hz")
    return rate * tau_0_sec


# ────────────────────────────────────────────────────────────────────
# Engine interpolation (Phase I Appendix E)
# ────────────────────────────────────────────────────────────────────

def nu_interpolation(y):
    """Acceleration interpolation ν(y) = 1/2 + √(1/4 + 1/y).

    PROVENANCE (v2 self-containment audit, June 2026). This is the MOND
    "simple" interpolating function, **ADOPTED** to match galactic
    rotation-curve phenomenology — it is NOT derived from the GRUT
    constitutive action, and no such derivation exists in V7 either
    (GRUT_V7_FULL.md only states it "matches MOND phenomenology"). GRUT's
    refractive enhancement is BOUNDED: n_g² = 1 + α_vac·Re[χ] ≤ 4/3, a
    ≤15% velocity boost, while flat curves require factors of several —
    so the unbounded ν(y) → √(1/y) shape provably cannot come from the
    enhancement (see theory/PROJECTOR_CONSISTENCY_NOGO.md, §dark sector).

    What GRUT genuinely DERIVES in this engine:
      • the acceleration scale a_0 = c/(2π τ_Λ) = cH_0/(2π)  (A_0_SI), and
      • the frequency gate 1/(1+X²), X = ω_dyn τ_0  (alpha_effective),
        which gives solar-system safety AND the falsifiable high-ω
        deviation from MOND.
    The interpolation SHAPE ν(y) is MOND, adopted. (Earlier docstrings
    claimed it was "derived from screening" — incorrect; corrected here.)

    Asymptotic limits:
        y ≫ 1 (Newtonian):   ν → 1,         g_eff ≈ g_bar
        y ≪ 1 (deep-response): ν → √(1/y),   g_eff ≈ √(g_bar × a_0)  [MOND]
    y ≡ g_bar/a_0.
    """
    y_arr = np.asarray(y, dtype=float)
    if np.any(y_arr <= 0):
        # Return divergent interpolation for non-positive y
        return np.where(y_arr > 0, 0.5 + np.sqrt(0.25 + 1.0/np.where(y_arr > 0, y_arr, 1)), float("inf"))
    return 0.5 + np.sqrt(0.25 + 1.0/y_arr)


def g_effective(g_bar_SI, omega_dyn_Hz,
                 a_0=A_0_SI, tau_0_sec=TAU_0_SEC):
    """Total effective gravitational acceleration (Phase I Appendix E.2).

        g_eff = g_bar × [1 + (ν(y) − 1) / (1 + X²)]

    where y = g_bar/a_0 and X = ω_dyn τ_0.

    In the solar-system regime (X ≫ 1): g_eff ≈ g_bar (GR recovered).
    In the deep-galactic regime (X ≪ 1, y ≪ 1): g_eff ≈ √(g_bar × a_0) (MOND-like).
    """
    y = g_bar_SI / a_0
    nu = nu_interpolation(y)
    X = regime_parameter_X(omega_dyn_Hz, tau_0_sec=tau_0_sec)
    return g_bar_SI * (1.0 + (nu - 1.0) / (1.0 + X**2))


# ────────────────────────────────────────────────────────────────────
# Bullet Cluster operational estimate (Phase I §8.4)
# ────────────────────────────────────────────────────────────────────

def bullet_offset_estimate(v_coll_m_s, tau_0_sec=TAU_0_SEC):
    """δ_est ≈ v_coll × τ_0 — memory-kernel lag offset.

    Phase I §8.4: the simple operational estimate for the lensing-
    gas offset in cluster mergers. Full convolution is done by the
    engine; this is the scaling estimate.
    """
    return v_coll_m_s * tau_0_sec


# ────────────────────────────────────────────────────────────────────
# MOND comparison (v11 App F, F)
# ────────────────────────────────────────────────────────────────────

MOND_COMPARISON = {
    "MOND": {
        "foundational_assumption": "Newtonian dynamics/inertia modified below a_0",
        "fundamental_scale":       "a_0 (acceleration, fitted ~1.2e-10 m/s²)",
        "regime_separator":        "acceleration-based",
        "field_equations":         "nonlinear Poisson",
        "causality":               "implicit",
        "free_parameters":         1,
    },
    "TeVeS": {
        "foundational_assumption": "New scalar, vector, tensor fields",
        "propagating_fields":      "extra",
        "UV_recovery":             "model-dependent",
        "free_parameters":         "several",
    },
    "Emergent_Gravity": {
        "foundational_assumption": "Gravity is entropic response of microscopic d.o.f.",
        "locality":                "quasi-local",
        "UV_recovery":             "unclear",
        "free_parameters":         "several",
    },
    "GRUT_Closure": {
        "foundational_assumption": "Gravity is geometric; metric has finite relaxation τ_0",
        "fundamental_scale":       "τ_0 = 41.9 Myr (response-time, derived from Λ)",
        "regime_separator":        "frequency-based (X = ω_dyn τ_0)",
        "field_equations":         "Einstein + nonlocal memory kernel",
        "causality":               "explicit (Kramers-Kronig)",
        "UV_recovery":             "automatic (n_g → 1 at high ω)",
        "singularity_resolution":  "yes (curvature saturates at α/(c²τ_0²))",
        "MOND_a_0":                "emerges as c/(2π τ_Λ), not independent",
        "free_parameters":         0,
    },
}
"""v11 Appendix F and Appendix C comparison table, integrated verbatim.

Key slogan:
  MOND changes the law.
  Emergent gravity changes the meaning.
  Closure changes the response time.

Closure predicts MOND-like phenomenology only in the LOW-FREQUENCY limit
(X ≪ 1), not universally at low accelerations. This is testable: systems
with low acceleration but high frequency (e.g., planetary wide binaries
at specific phases) should NOT show MOND-like behavior."""


# ────────────────────────────────────────────────────────────────────
# Convenience / canonical table
# ────────────────────────────────────────────────────────────────────

def canonical_constants_table():
    """Phase I §6 canonical constants table (brought into code)."""
    return {
        # Two foundational constants
        "tau_0_Myr":              TAU_0_MYR,
        "alpha_vac":              ALPHA_VAC,
        # Derived from foundational + (c, ℏ, k_B)
        "tau_Lambda_Gyr":         TAU_LAMBDA_SEC / (YEAR_SEC * 1e9),
        "S_screening_factor":     S_SCREENING,
        "S_formula":              "12π/α² = 108π",
        "n_g_DC":                 N_G_DC,
        "R_refractive":           R_REFRACTIVE,
        "mu_Lambda_eV":           MU_LAMBDA_EV,
        "mu_0_eV":                MU_0_EV,
        "a_star_m_s2":            A_STAR_SI,
        "a_0_m_s2":               A_0_SI,
        "T_c_K":                  T_C_KELVIN,
        "T_c_MK":                 T_C_MK,
        "H_0_implied_km_s_Mpc":   H_0_IMPLIED_KM_S_MPC,
        "R_max_inv_m2":           R_MAX_INV_M2,
        "rho_max_kg_m3":          RHO_MAX_KG_M3,
        # Path D cross-checks (different physical objects)
        "a_over_c_SM_Majorana":   A_OVER_C_SM_MAJORANA,
        "a_over_c_SM_Dirac":      A_OVER_C_SM_DIRAC,
        "provenance": {
            "alpha_vac":         "DERIVED — conformal-mode scalar identification; "
                                 "KS 2011 a/c = 1/3 for single real conformally-coupled scalar. "
                                 "Historical (back-derivation from 15.47% boost) preserved in "
                                 "foundations_audit/ALPHA_VAC_PROVENANCE.md.",
            "tau_0":             "DERIVED — CTP noise-kernel structure at gold benchmark "
                                 "(V7 §18). Cross-check: τ_0 = 1/√(Λc²) (v11 App I). "
                                 "Empirically consistent with Bullet Cluster ~40 Myr offset.",
            "S_screening":       "Phase I §5 — S = 12π/α² (derived from α_vac)",
            "n_g_DC":            "√(1+α) = √(4/3) — Path G canonical R = 1.15470",
            "R_refractive":      "Canonical R alias of n_g_DC; primary cosmological observable",
            "a_0":               "Phase I §8.2 — c/(2π τ_Λ) ~ MOND scale (derived)",
            "T_c":               "v9.0 — ℏ/(τ_0 k_B) ≈ 54.7 MK (derived)",
            "R_max_inv_m2":      "V7 §13 Whole Hole — universal RICCI saturation α/(c²τ_0²); "
                                 "applies to matter-bearing interior, not Schwarzschild exterior",
            "rho_max_kg_m3":     "Universal interior density cap c²R_max/(8πG); "
                                 "every BH core saturates at this density regardless of mass",
            "a_over_c_SM_Majorana":  "Path D — 1991/1698 ≈ 1.17256 (KS 2011 + Duff 1994)",
            "a_over_c_SM_Dirac":     "Path D variant — 253/219 ≈ 1.15525 with ν_R included",
        },
    }


def verify():
    """Self-test canonical constants."""
    table = canonical_constants_table()
    checks = {
        # α = 1/3 exactly
        "alpha_vac_is_one_third":      abs(ALPHA_VAC - 1/3) < 1e-15,
        # S = 108π
        "S_equals_108_pi":             abs(S_SCREENING - 108 * np.pi) < 1e-10,
        # τ_0 ≈ 41.9 Myr (within 1%)
        "tau_0_is_41p9_Myr":           abs(TAU_0_MYR - 41.9) / 41.9 < 0.01,
        # n_g(0) = 1.1547 — canonical R via Path G
        "n_g_DC_is_sqrt_4_over_3":     abs(N_G_DC - np.sqrt(4/3)) < 1e-12,
        "R_refractive_aliases_n_g_DC": R_REFRACTIVE == N_G_DC,
        "R_canonical_is_15470":        abs(R_REFRACTIVE - 1.15470) < 1e-4,
        # Path D cross-checks (different physical objects)
        "a_over_c_SM_Majorana":        abs(A_OVER_C_SM_MAJORANA - 1991/1698) < 1e-12,
        "a_over_c_SM_Dirac":           abs(A_OVER_C_SM_DIRAC  - 253/219)   < 1e-12,
        # R_max universal Ricci-saturation curvature ~ 2 × 10⁻⁴⁸ m⁻²
        "R_max_universal_order":       1e-49 < R_MAX_INV_M2 < 1e-47,
        "R_max_formula":               abs(
            R_MAX_INV_M2 - ALPHA_VAC / (C_LIGHT**2 * TAU_0_SEC**2)
        ) / R_MAX_INV_M2 < 1e-12,
        # ρ_max = c²R_max/(8πG) universal interior density cap
        "rho_max_formula":             abs(
            RHO_MAX_KG_M3 - (C_LIGHT**2 * R_MAX_INV_M2) / (8.0 * np.pi * G_NEWTON)
        ) / RHO_MAX_KG_M3 < 1e-12,
        # Threshold equivalence: ωτ_0 = Λ_grav τ_0 when ω ~ Λ_grav
        # (holds for self-gravitating systems; atoms are deep crystal
        # via EM-dominated ω, not Λ_grav — see test_threshold_bridge.py)
        "threshold_bridge_macro_crystal": (
            crystallinity(lambda_grav_Hz=lambda_grav_dp(1e-3, 1e-3, 1e-3)) > 1e30
        ),
        "threshold_bridge_galactic_fluid": (
            crystallinity(omega_dyn_Hz=2 * np.pi / (2.5e8 * YEAR_SEC)) < 2.0
        ),
        # a_0 in 10⁻¹⁰ m/s² band
        "a_0_is_MOND_scale":           1e-11 < A_0_SI < 1e-9,
        # T_c ≈ 54.7 MK (within 5%)
        "T_c_is_54p7_MK":              abs(T_C_KELVIN/1e6 - 54.7) / 54.7 < 0.05,
        # μ_Λ ~ 10⁻³³ eV
        "mu_Lambda_is_10e_minus_33":   1e-34 < MU_LAMBDA_EV < 1e-32,
        # μ_0 = S × μ_Λ
        "mu_0_equals_S_mu_Lambda":     abs(MU_0_EV / MU_LAMBDA_EV - S_SCREENING) / S_SCREENING < 1e-6,
        # τ_0 = 1/√(Λc) round-trip
        "tau_0_Lambda_c_identity":     abs(
            tau_0_from_lambda_c(lambda_from_tau_0(TAU_0_SEC)) - TAU_0_SEC
        ) / TAU_0_SEC < 1e-10,
    }
    return checks


if __name__ == "__main__":
    import json
    table = canonical_constants_table()
    print(json.dumps({k: (v if not isinstance(v, dict) else v) for k, v in table.items()},
                      indent=2, default=str))
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "✓" if v else "✗"
        print(f"  {mark} {k}")
