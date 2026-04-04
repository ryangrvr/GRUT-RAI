"""O(3) Sector Nativity Audit.

The Skyrme term nativity audit (skyrme_term_nativity_audit.py) established
that Route 3 — the O(3) derivative expansion — is the structural path from
'particle_candidate_not_yet_established' to a stable bosonic localized object.
But Route 3 is conditioned on O(3) nativity.  This module audits that condition
directly.

PRIMARY QUESTION
---------------
Does GRUT's canonical scalar / barrier / constitutive architecture force,
derive, or uniquely motivate an effective O(3) field sector as a native
regime description?

Not: "Is O(3) useful?"
Not: "Can O(3) model the same phenomena?"
But: Does the canonical GRUT architecture produce, require, or uniquely select
the O(3) triplet as an emergent or effective description?

ARCHITECTURAL GROUND TRUTH (from defect_admissibility.py)
----------------------------------------------------------
  Phase D1 explicitly states:
    "This phase does NOT derive the defect from the already-locked GRUT core.
    The triplet is introduced as a candidate extension."
  Classification: provisional_candidate_extension_formulated

  This is the honest starting point.  The O(3) triplet Φᵃ (a=1,2,3) is
  introduced by hand in Phase D1+.  The audit tests whether this introduction
  can be justified architecturally, or must remain an independent postulate.

THE FIVE AUDIT TRACKS
----------------------
  A. Canonical scalar → O(3) triplet
     Can the single real scalar Φ be promoted to an O(3) triplet without
     introducing new field content?

  B. Target-space geometry: ℝ → S²
     Can GRUT's barrier / constitutive / CTP architecture generate the
     S² vacuum manifold (the Mexican hat constraint |Φᵃ|² = η²)?

  C. Internal symmetry origin
     Does GRUT's canonical architecture generate or imply an O(3) internal
     symmetry group acting on a triplet of scalar fields?

  D. Parameter mapping
     Can the O(3) parameters (η, μ, λ) be tied to GRUT canonical constants
     (α_vac, β_Q, τ², M_ext, R_eq, ω₀)?

  E. Uniqueness
     Is O(3) the unique minimal real-scalar extension that provides the
     topological structure (π₂(M) ≠ 0) GRUT needs for bosonic winding charge?

THREE BLOCKING GAPS
--------------------
  BG1 — Discrete DOF change (1 → 3 scalar fields):
    A single real scalar Φ has field space ℝ with no internal symmetry group.
    An O(3) triplet Φᵃ has field space ℝ³ (or S² after constraint) with an
    O(3) internal symmetry acting as Φᵃ → R^a_b Φᵇ.
    Going from 1 to 3 real scalars is a DISCRETE CHANGE in field content.
    No gradient expansion, CTP integration, or effective field theory argument
    turns one real scalar into three real scalars with an internal symmetry.
    This gap is NOT closeable by mathematical derivation — it requires a
    deliberate new field postulate.  It is the most fundamental blocking gap.

  BG2 — Target-space geometry (ℝ → S²):
    The canonical GRUT scalar Φ takes values in ℝ (unbounded).
    The O(3) triplet constrained to S² requires a symmetry-breaking mechanism:
    V(Φ) = -(1/2)μ²|Φ|² + (1/4)λ|Φ|⁴, which spontaneously breaks O(3) to
    O(2) ≅ U(1) and forces the VEV |Φᵃ|² = η² = μ²/λ.
    Neither the constitutive ODE (τ_eff · dΦ/dt + Φ = X) nor the barrier
    action (a_Q ~ (r_s/R)^β_Q) generates such a potential for a field triplet.
    The Mexican hat parameters μ, λ are free; the VEV η is free.
    This gap is closeable only if a symmetry-breaking mechanism is derived
    from GRUT (not currently present).

  BG3 — Internal symmetry origin:
    The GRUT canonical scalar has no continuous internal symmetry (at most Z₂:
    Φ → -Φ).  The O(3) triplet requires an SO(3) internal symmetry group.
    The spatial SO(3) rotation symmetry IS present in GRUT (spherical symmetry).
    The hedgehog ansatz Φᵃ = η·f(r)·x̂ᵃ locks internal O(3) to spatial SO(3),
    allowing hedgehog configurations to preserve a diagonal symmetry.
    But: the internal O(3) and spatial SO(3) are distinct groups.  Identifying
    them via the hedgehog ansatz is a specific kinematic choice, not a derivation
    of an internal symmetry group from canonical GRUT.
    This gap is PARTIALLY addressable: if spatial SO(3) can be shown to generate
    the relevant topological structure when restricted to the shell surface,
    the internal O(3) can be understood as the spatial rotational symmetry acting
    on a 3-vector field — but this requires explicit construction.

TWO CONVERGENT MOTIVATIONS
---------------------------
  CM1 — Topological gap fill (unique minimal real-scalar extension):
    The canonical GRUT scalar has π₂(ℝ) = 0: no topological winding in 3D.
    For bosonic winding charge (particle-like bosonic objects), GRUT needs a
    field sector with π₂(M) ≠ 0 where M is the vacuum manifold.
    For REAL scalar fields in 3+1D with π₂(M) ≠ 0: need M homeomorphic to S².
    Minimal real-scalar field content giving S² vacuum manifold:
      3 real scalars with |Φᵃ|² = η² constraint → vacuum manifold S² = SO(3)/SO(2).
    This is the O(3) triplet.  No smaller real-scalar system achieves π₂ ≠ 0.
    Therefore: O(3) is the unique minimal real-scalar extension for π₂ ≠ 0.
    This is the STRONGEST motivation — not from phenomenology but from topology.

  CM2 — Component B tail matching (phenomenological):
    The interior deficit program (Phase 6C) requires a Component B contribution
    to the energy density with tail ε_B ~ A_B/r² as r → ∞.
    From defect_admissibility.py Result 5: the O(3) hedgehog asymptotic tail is
    ε_hedge(r) → η²/r² in the limit f(r) → 1 (vacuum region).
    Matching condition: η² = A_B = COMP_B_COEFF = 1/(8π) ≈ 0.03979.
    This matching makes O(3) the field content that naturally produces the
    required Component B profile shape AND normalization.
    One parameter (η) is thereby CONSTRAINED by an interior GRUT requirement.

PARAMETER CONNECTION (one partial link found)
---------------------------------------------
  The Component B coefficient COMP_B_COEFF = 1/(8π) relates to the canonical
  GRUT relaxation time as follows:

      COMP_B_COEFF = 1/(8π) = (3/2)/(12π) = TAU_SQ / (12π)

  Since TAU_SQ = 3/2 exactly in canonical GRUT, the Component B matching
  condition η² = 1/(8π) = TAU_SQ/(12π) represents a numerical connection
  between the O(3) amplitude scale η and the canonical GRUT parameter τ².

  STATUS: numerical coincidence — the physical mechanism for this connection
  is not established.  Whether the factor 1/(12π) has architectural meaning
  or is an artifact of the Component B normalization convention is unknown.
  This is noted as a partial parameter link, NOT as a derived connection.

NATIVITY CRITERIA (all four assessed)
--------------------------------------
  N1 — Field-content derivability: 1 scalar → O(3) triplet without new postulate?
    FAILS HARD — BG1: discrete DOF change; mathematically irresolvable by derivation.

  N2 — Target-space derivability: ℝ → S² from GRUT barrier/constitutive mechanics?
    FAILS — BG2: no mechanism generates Mexican hat constraint from canonical GRUT.

  N3 — Internal symmetry emergence: O(3) internal symmetry from canonical architecture?
    CONDITIONALLY PARTIAL — BG3: spatial SO(3) present; hedgehog locks to spatial
    rotations; but internal O(3) and spatial SO(3) are distinct groups.  Partial
    addressability via hedgehog diagonal symmetry, not a full derivation.

  N4 — Parameter determination: η, μ, λ from GRUT canon?
    PARTIALLY OPEN — One connection: η² = τ²/(12π) (numerical coincidence via
    Component B matching).  μ and λ individually are free; only λ/μ² = η² is
    constrained (not μ and λ separately).

UNIQUENESS RESULT
-----------------
  O(3) is the unique minimal real-scalar field extension with π₂(M) ≠ 0 in
  3+1 dimensions.  No smaller real-scalar system achieves the required topology.
  This uniqueness makes O(3) a NECESSARY postulate (if GRUT pursues winding charge)
  rather than an ARBITRARY postulate.  The motivation is structural, not aesthetic.

  Uniqueness does NOT imply nativity.  The fact that O(3) is the unique choice
  does not mean it is derived from canonical GRUT — it means that if you want
  bosonic winding charge from real scalars, you have no other option.

PATCHWORK CLASSIFICATION
------------------------
  Unlike the Skyrme term (where the derivation COULD be built by establishing
  O(3) nativity), O(3) itself CANNOT be derived from canonical GRUT because:

    Blocking Gap BG1 (1 → 3 real scalars) is NOT closeable by derivation.
    It can only be resolved by a new field postulate.

  The honest patchwork classification is:
    derives_from_canonical_scalar:    False (mathematically impossible via BG1)
    motivated_independent_postulation: True (topology + Component B make it necessary)
    arbitrary_auxiliary_extension:    False (uniqueness and convergent motivations rule this out)
    incompatible_with_canonical:      False (fully compatible; no prior audit violated)

  Patchwork verdict: "motivated_independent_postulation"

  This is HARDER than the Skyrme result ("motivated_but_unbuilt"):
    - Skyrme: blocked by O(3) nativity prerequisite; buildable once prerequisite met.
    - O(3):   blocked by irreducible field-content change; NOT buildable; must be postulated.

  What changes: The Skyrme term can become native once O(3) is established.
  The O(3) triplet can NEVER become "derived from canonical GRUT scalar."
  But it CAN become a well-motivated, uniquely-selected, parameter-constrained
  postulate — which is the best outcome achievable for a field-content extension.

PRINCIPAL RESULTS
-----------------
  canonical_scalar_implies_o3:       False  (BG1 hard)
  target_space_generated_by_grut:    False  (BG2)
  internal_symmetry_from_grut:       False  (BG3 — partial only)
  o3_is_unique_minimal_extension:    True   (topology uniqueness)
  component_b_motivates_o3:          True   (tail matching)
  parameter_connection_found:        True   (η² = τ²/(12π), mechanism unknown)
  parameter_connection_mechanism_known: False
  all_nativity_criteria_pass:        False
  doctrine_compatible:               True

  primary_verdict:   "o3_auxiliary_but_minimally_motivated"
  secondary_verdict: "o3_requires_independent_field_postulation"
  patchwork:         "motivated_independent_postulation"

NONCLAIMS
---------
  1. NOT claiming O(3) is arbitrary — two convergent motivations (CM1, CM2) make
     it uniquely selected and phenomenologically required.
  2. NOT claiming O(3) can never have a deeper derivation — only claiming that no
     derivation from CANONICAL SCALAR is possible given BG1.
  3. NOT claiming the η² = τ²/(12π) connection is meaningless — it is a real
     numerical fact; what is missing is the physical mechanism behind it.
  4. NOT claiming adding O(3) violates prior GRUT doctrine — it is fully compatible.
  5. NOT claiming BG3 (internal symmetry) cannot be partially addressed — the
     hedgehog ansatz provides a partial identification of internal and spatial SO(3);
     this identification is not a derivation but it narrows the gap.
  6. NOT claiming the defect language is wrong — it is correctly formulated and
     shape-compatible with Component B; the issue is nativity, not validity.

References
----------
  grut/defect_admissibility.py             — Phase D1+: O(3) candidate extension;
                                             ETA_TARGET = 1/sqrt(8*pi); COMP_B_COEFF
  grut/localized_bosonic_object_audit.py   — Appendix M: particle_candidate status
  grut/skyrme_term_nativity_audit.py       — Skyrme audit: Route 3 conditional on O(3)
  grut/fermionic_emergence_audit.py        — O(3) homotopy: pi_2(S^2) = Z, Hopf absent
  grut/phi_sector_bifurcation.py           — Phi trajectory vs field distinction
  grut/tau_eff_domain_declaration.py       — Domain: spherical, quasi-static, preferred-frame
  grut/barrier_action_sector.py            — Barrier action underdetermination theorem
  grut/g_minus_closure_audit.py            — g_- source vanishes at equilibrium
  Derrick (1964), J. Math. Phys. 5, 1252   — no-go for scalar solitons (motivates O(3))
  Weinberg (1979), Physica A 96, 327       — EFT derivative expansion (O(3) → L_4 unique)
  Homotopy: pi_2(S^2) = Z, pi_2(R^N) = 0  — topological uniqueness of O(3) among scalars
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, FrozenSet, List, Optional


# ---------------------------------------------------------------------------
# Locked constants — canonical GRUT equilibrium (β_Q = 2)
# ---------------------------------------------------------------------------

M_EXT: float = 0.5
R_EQ: float = 1.0 / 3.0
TAU_SQ: float = 1.5              # τ² = 3/2 (canonical)
ALPHA_VAC: float = 1.0 / 3.0
BETA_Q_CANON: float = 2.0

OMEGA_0_SQ: float = BETA_Q_CANON * M_EXT / (R_EQ ** 3)   # = 27.0
OMEGA_0: float = math.sqrt(OMEGA_0_SQ)

X_EQ: float = M_EXT / (R_EQ ** 2)   # = 4.5

# Spatial dimension
SPATIAL_DIMENSION: int = 3

# O(3) field content
N_O3_FIELDS: int = 3            # three real scalar fields Φ¹, Φ², Φ³
N_CANONICAL_FIELDS: int = 1     # one real scalar Φ in canonical GRUT

# Homotopy groups
PI2_REAL_SCALAR: int = 0        # π₂(ℝ) = 0: no topological defects
PI2_S2: str = "Z"               # π₂(S²) = ℤ: integer winding numbers

# Component B matching from defect_admissibility.py
# COMP_B_COEFF = 1/(8π): the coefficient in ε_B = COMP_B_COEFF/r²
COMP_B_COEFF: float = 1.0 / (8.0 * math.pi)   # ≈ 0.03979

# O(3) VEV from Component B matching: η² = COMP_B_COEFF
ETA_SQ_FROM_COMP_B: float = COMP_B_COEFF      # ≈ 0.03979
ETA_FROM_COMP_B: float = math.sqrt(ETA_SQ_FROM_COMP_B)  # ≈ 0.1995

# Numerical parameter connection (mechanism unknown):
# η² = COMP_B_COEFF = 1/(8π) = TAU_SQ/(12π)
# because 1/(8π) = (3/2)/(12π) = TAU_SQ/(12π)
ETA_SQ_FROM_TAU_FORMULA: float = TAU_SQ / (12.0 * math.pi)  # = 1/(8π) exactly

# Verification: this must equal COMP_B_COEFF
assert abs(ETA_SQ_FROM_TAU_FORMULA - COMP_B_COEFF) < 1e-12, (
    f"Tau² parameter link broken: {ETA_SQ_FROM_TAU_FORMULA} != {COMP_B_COEFF}"
)

# Mexican hat free parameters (from defect_admissibility.py defaults)
# MU_DEFAULT = 1.0, LAMBDA_DEFAULT = 8π ≈ 25.13
MU_DEFAULT: float = 1.0
LAMBDA_DEFAULT: float = MU_DEFAULT ** 2 / ETA_SQ_FROM_COMP_B  # = 8π

# Blocking gap count
N_BLOCKING_GAPS: int = 3        # BG1, BG2, BG3
N_CONVERGENT_MOTIVATIONS: int = 2  # CM1 (topological), CM2 (Component B)
N_NATIVITY_CRITERIA: int = 4    # N1-N4

# ---------------------------------------------------------------------------
# Closed verdict and vocabulary sets
# ---------------------------------------------------------------------------

ALLOWED_NATIVITY_VERDICTS: FrozenSet[str] = frozenset({
    "no_native_o3_derivation_found",
    "o3_auxiliary_but_minimally_motivated",
    "o3_conditionally_derivable_from_collective_modes",
    "o3_requires_independent_field_postulation",
})

ALLOWED_ROUTE_STATUSES: FrozenSet[str] = frozenset({
    "not_derivable",
    "conditionally_partial",
    "phenomenological_motivation",
    "speculative_domain_constrained",
    "open_but_unbuilt",
    "established",
    "unique_minimal",
})

ALLOWED_PATCHWORK_CLASSES: FrozenSet[str] = frozenset({
    "derives_from_canonical_scalar",
    "motivated_independent_postulation",
    "arbitrary_auxiliary_extension",
    "incompatible_with_canonical_architecture",
})

ALLOWED_GAP_CLOSEABILITY: FrozenSet[str] = frozenset({
    "not_closeable_by_derivation",
    "partially_closeable",
    "closeable_under_conditions",
    "already_closed",
})


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class AuditTrack:
    """One of the five audit tracks (A–E)."""
    track_id: str                        # "A", "B", "C", "D", "E"
    name: str                            # short label
    question: str                        # exact question asked
    status: str                          # from ALLOWED_ROUTE_STATUSES
    finding: str                         # what the track finds
    contributes_to_nativity: bool        # True if finding supports nativity
    blocking_gap_ref: Optional[str]      # "BG1", "BG2", "BG3", or None
    motivation_ref: Optional[str]        # "CM1", "CM2", or None
    notes: List[str] = field(default_factory=list)


@dataclass
class BlockingGap:
    """One of the three blocking gaps preventing O(3) nativity."""
    gap_id: str                          # "BG1", "BG2", "BG3"
    name: str
    description: str
    closeability: str                    # from ALLOWED_GAP_CLOSEABILITY
    what_would_close_it: Optional[str]
    closes_nativity_question: bool       # True if closing this gap gives nativity
    is_mathematical_impossibility: bool  # True if closing via derivation is impossible
    notes: List[str] = field(default_factory=list)


@dataclass
class ConvergentMotivation:
    """One of the two convergent motivations for O(3)."""
    motivation_id: str                   # "CM1", "CM2"
    name: str
    description: str
    is_topological: bool                 # True if motivation comes from topology
    is_phenomenological: bool            # True if from data/tail-matching
    motivates_o3_uniquely: bool          # True if this alone singles out O(3)
    parameter_constrained: bool          # True if this constrains a parameter
    parameter_constraint: Optional[str]  # e.g. "eta^2 = 1/(8*pi)"
    notes: List[str] = field(default_factory=list)


@dataclass
class NativityCriterion:
    """One of the four nativity criteria for O(3)."""
    criterion_id: int                    # 1, 2, 3, 4
    name: str                            # N1 ... N4
    description: str
    passes: bool
    pass_level: str                      # "hard_fail", "soft_fail", "partial", "pass"
    reason: str                          # why it passes or fails
    blocking_gap_ref: Optional[str]
    conditional_path: Optional[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class UniquenessCheck:
    """Assessment of whether O(3) is the unique minimal extension needed."""
    question: str
    o3_is_minimal_for_pi2_nonzero: bool     # True — smallest real-scalar field content
    alternative_with_fewer_real_fields: bool  # False — no smaller option works
    cp1_equivalent: bool                      # True — CP(1) ≅ S², equivalent topology
    cp1_uses_same_dof_count: bool             # True — 2 complex = 4 real with 1 constraint = 3 real
    uniqueness_verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ParameterMapping:
    """Assessment of O(3) parameter connections to GRUT canonical constants."""
    eta_sq_from_comp_b: float           # = 1/(8π), from Component B matching
    eta_sq_from_tau_formula: float      # = τ²/(12π), numerical coincidence
    tau_connection_holds_numerically: bool  # True (verified above)
    tau_connection_mechanism_known: bool   # False (coincidence, not derived)
    mu_fixed_by_grut: bool              # False — free parameter
    lambda_fixed_by_grut: bool          # False — free parameter (only λ/μ² = η² constrained)
    ratio_lambda_over_mu_sq_constrained: bool  # True (= 1/η² from VEV condition)
    grut_constants_not_used: List[str]  # which GRUT params don't appear
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class DoctrineCompatibilityCheck:
    """Whether adding O(3) violates any prior GRUT audit verdict."""
    consistent_with_phi_bifurcation: bool      # True — O(3) is Φᵃ, not trajectory Φ
    consistent_with_tau_eff_domain: bool       # True — static O(3) sector
    consistent_with_beta_q_hypothesis: bool    # True — O(3) independent of β_Q
    consistent_with_fermionic_audit: bool      # True — O(3) is bosonic (hedgehog)
    consistent_with_appendix_m: bool           # True — O(3) was the candidate already
    consistent_with_skyrme_audit: bool         # True — O(3) nativity is Route 3 prereq
    introduces_new_field_content: bool         # True — 3 new scalar fields
    introduces_new_free_parameters: bool       # True — μ, λ (or equivalently η and λ/μ²)
    compatible_with_prior_doctrine: bool       # True
    doctrine_impact: str
    notes: List[str] = field(default_factory=list)


@dataclass
class PatchworkAssessment:
    """Assessment of O(3) patchwork vs native status."""
    derives_from_canonical_scalar: bool         # False — BG1 is irresolvable by derivation
    motivated_independent_postulation: bool     # True — topological + Component B motivate
    arbitrary_auxiliary_extension: bool         # False — uniqueness + convergences rule this out
    incompatible_with_canonical_architecture: bool  # False
    patchwork_verdict: str                      # from ALLOWED_PATCHWORK_CLASSES
    comparison_to_skyrme_term: str              # key difference from Skyrme patchwork result
    what_best_outcome_looks_like: str           # best achievable status for O(3) in GRUT
    notes: List[str] = field(default_factory=list)


@dataclass
class O3NativityResult:
    """Master result of the O(3) sector nativity audit."""

    # Structural analysis
    tracks: List[AuditTrack]
    blocking_gaps: List[BlockingGap]
    convergent_motivations: List[ConvergentMotivation]
    nativity_criteria: List[NativityCriterion]
    uniqueness_check: UniquenessCheck
    parameter_mapping: ParameterMapping
    doctrine_check: DoctrineCompatibilityCheck
    patchwork: PatchworkAssessment

    # Top-level Boolean summary
    canonical_scalar_implies_o3: bool               # False — BG1
    target_space_generated_by_grut: bool            # False — BG2
    internal_symmetry_from_grut: bool               # False — BG3 (partial only)
    o3_is_unique_minimal_extension: bool            # True — topological uniqueness
    component_b_motivates_o3: bool                  # True — CM2
    parameter_connection_found: bool                # True — η² = τ²/(12π)
    parameter_connection_mechanism_known: bool      # False — numerical coincidence
    all_nativity_criteria_pass: bool                # False — none pass fully

    # O(3) source characterization
    n_canonical_fields: int                         # 1
    n_o3_fields: int                                # 3
    field_content_change_is_discrete: bool          # True — cannot be derived
    doctrine_compatible: bool                       # True

    # Verdicts
    primary_verdict: str                            # "o3_auxiliary_but_minimally_motivated"
    secondary_verdict: str                          # "o3_requires_independent_field_postulation"

    # Doctrine
    nonclaims: List[str]
    forbidden_inferences: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def build_track_a() -> AuditTrack:
    """Track A: Can the canonical scalar be promoted to an O(3) triplet?"""
    return AuditTrack(
        track_id="A",
        name="canonical_scalar_promotion",
        question=(
            "Can the single real scalar Φ be promoted to an O(3) triplet Φᵃ "
            "without introducing new field content as a separate postulate?"
        ),
        status="not_derivable",
        finding=(
            "A single real scalar Φ has field space ℝ with no internal symmetry "
            "group.  An O(3) triplet Φᵃ (a=1,2,3) has field space ℝ³ with an "
            "O(3) internal symmetry acting as Φᵃ → R^a_b Φᵇ.  This is a discrete "
            "change in the number of degrees of freedom (1 → 3 real scalars).  "
            "No continuous deformation, gradient expansion, CTP integration, or "
            "EFT argument converts one real scalar into three real scalars with "
            "an O(3) symmetry.  defect_admissibility.py is explicit: 'The triplet "
            "is introduced as a candidate extension' — it is not derived."
        ),
        contributes_to_nativity=False,
        blocking_gap_ref="BG1",
        motivation_ref=None,
        notes=[
            "Single real scalar Φ: target space ℝ, no internal symmetry.",
            "O(3) triplet Φᵃ: target space ℝ³, O(3) = SO(3)/Z₂ internal symmetry.",
            "DOF count: 1 vs 3 real scalars.  The difference is 2 new real DOF.",
            "Z₂ symmetry (Φ → -Φ) of the canonical scalar is NOT an O(3) subgroup.",
            "Duplication: introducing Φ¹ = Φ², Φ³ = 0 would not give O(3) symmetry.",
            "The promotion requires an explicit field-content postulate.",
            "defect_admissibility.py DEFECT_NONCLAIMS[2]: 'does NOT derive the "
            "defect from the already-locked GRUT core'.",
            "This is the fundamental track: if A fails, no other track can give nativity.",
        ],
    )


def build_track_b() -> AuditTrack:
    """Track B: Can GRUT architecture generate the S² target space?"""
    return AuditTrack(
        track_id="B",
        name="target_space_geometry",
        question=(
            "Can GRUT's barrier / constitutive / CTP architecture generate the "
            "S² vacuum manifold (|Φᵃ|² = η² = const) as a derived constraint, "
            "rather than requiring the Mexican hat potential to be introduced by hand?"
        ),
        status="not_derivable",
        finding=(
            "The S² vacuum manifold requires the Mexican hat potential: "
            "V(Φ) = -(1/2)μ²|Φ|² + (1/4)λ|Φ|⁴.  This potential spontaneously "
            "breaks O(3) → U(1) and enforces |Φᵃ|² = μ²/λ ≡ η².  "
            "The constitutive ODE (τ_eff · dΦ/dt + Φ = X) is linear and scalar; "
            "it does not generate a quartic potential for a triplet.  "
            "The barrier action (a_Q ~ (r_s/R)^β_Q) is a radial/gravitational "
            "effect in the collapse sector; it does not generate an internal-space "
            "potential.  The CTP g_- sector (g_minus_closure_audit.py) has "
            "vanishing source at equilibrium; its fluctuation-level computation "
            "might generate an effective potential term, but this is uncomputed "
            "and would not obviously produce the specific Mexican hat form.  "
            "The parameters μ, λ are free (LAMBDA_DEFAULT = 8π, MU_DEFAULT = 1.0 "
            "in defect_admissibility.py — set by hand for phenomenological matching)."
        ),
        contributes_to_nativity=False,
        blocking_gap_ref="BG2",
        motivation_ref=None,
        notes=[
            "Mexican hat V(Φ): SSB potential for O(3) → U(1), free parameters μ, λ.",
            "VEV: η = μ/√λ — set by LAMBDA_DEFAULT = 8π and MU_DEFAULT = 1.0.",
            "Constitutive ODE: linear, scalar — no triplet potential.",
            "Barrier a_Q: radial/gravitational — no internal-space potential.",
            "CTP g_- sector: vanishing at equilibrium; fluctuation potential uncomputed.",
            "For comparison: in the Higgs mechanism, the Mexican hat is also added by hand.",
            "One partial connection: η² = 1/(8π) = τ²/(12π) (see parameter mapping).",
            "But the mechanism for η = f(τ²) is not established — only numerical.",
        ],
    )


def build_track_c() -> AuditTrack:
    """Track C: Does GRUT generate or imply an O(3) internal symmetry?"""
    return AuditTrack(
        track_id="C",
        name="internal_symmetry_origin",
        question=(
            "Does GRUT's canonical architecture generate or imply an O(3) internal "
            "symmetry group acting on a 3-component scalar field?"
        ),
        status="conditionally_partial",
        finding=(
            "The canonical GRUT scalar has no continuous internal symmetry (at most "
            "the discrete Z₂: Φ → -Φ).  The spatial SO(3) rotation symmetry IS "
            "present (GRUT enforces spherical symmetry).  The hedgehog ansatz "
            "Φᵃ = η·f(r)·x̂ᵃ locks the internal O(3) index to the spatial direction "
            "x̂ᵃ, meaning the configuration is invariant under the DIAGONAL symmetry "
            "L+T where L = spatial rotation and T = internal O(3) rotation.  "
            "This diagonal symmetry is real — hedgehog configurations DO preserve "
            "SO(3)_diag and this is consistent with GRUT's spherical symmetry "
            "requirement.  However: the identification x̂ᵃ = Φᵃ/|Φᵃ| is a kinematic "
            "choice that comes FROM the hedgehog ansatz, not FROM canonical GRUT.  "
            "Spatial SO(3) ≠ internal O(3): they act on different spaces (x vs Φ).  "
            "The diagonal identification is a partial bridge, not a full derivation."
        ),
        contributes_to_nativity=False,
        blocking_gap_ref="BG3",
        motivation_ref=None,
        notes=[
            "Canonical scalar Z₂: Φ → -Φ (discrete, not O(3)).",
            "Spatial SO(3): rotations of xᵃ (present in GRUT by spherical symmetry).",
            "Internal O(3): rotations of Φᵃ components (absent from canonical GRUT).",
            "Hedgehog: Φᵃ = η·f(r)·x̂ᵃ locks Φ-direction to x-direction.",
            "Diagonal SO(3): acts as (x,Φ) → (Rx, RΦ) simultaneously — preserved.",
            "This is a property of the hedgehog configuration, not of canonical GRUT.",
            "The internal O(3) must first be postulated, then the hedgehog can be used.",
            "Partially addressable: once O(3) is postulated, spatial SO(3) provides",
            "  the symmetry identification that makes the hedgehog spherically symmetric.",
            "But this is a POST-HOC identification, not a PRE-HOC derivation.",
        ],
    )


def build_track_d() -> AuditTrack:
    """Track D: Can O(3) parameters be tied to GRUT canonical constants?"""
    return AuditTrack(
        track_id="D",
        name="parameter_mapping",
        question=(
            "Can the O(3) parameters (η, μ, λ) be expressed in terms of canonical "
            "GRUT constants (α_vac, β_Q, τ², M_ext, R_eq, ω₀) through architectural "
            "relationships rather than free choices?"
        ),
        status="phenomenological_motivation",
        finding=(
            "One partial connection is found: η² = COMP_B_COEFF = 1/(8π).  "
            f"Since TAU_SQ = {TAU_SQ} exactly, this equals τ²/(12π) = "
            f"{TAU_SQ}/(12π) = {ETA_SQ_FROM_COMP_B:.8f}.  "
            "The numerical connection η² = τ²/(12π) holds exactly at canonical values.  "
            "However, the PHYSICAL MECHANISM for this connection is not established.  "
            "The Component B coefficient 1/(8π) comes from the interior deficit program "
            "(Phase 6C) and may itself depend on τ² through the deficit structure, "
            "or may be coincidental.  The parameters μ and λ are individually free: "
            f"MU_DEFAULT = {MU_DEFAULT}, LAMBDA_DEFAULT = 8π ≈ {LAMBDA_DEFAULT:.4f} "
            "in defect_admissibility.py — set by phenomenological convention.  "
            "Only the RATIO λ/μ² = 1/η² is constrained (by the VEV condition).  "
            "The GRUT constants α_vac, β_Q, ω₀, R_eq do not appear explicitly in the "
            "current O(3) sector formulation."
        ),
        contributes_to_nativity=False,
        blocking_gap_ref=None,
        motivation_ref="CM2",
        notes=[
            f"η² = COMP_B_COEFF = 1/(8π) = {COMP_B_COEFF:.8f}.",
            f"τ²/(12π) = {TAU_SQ}/(12π) = {ETA_SQ_FROM_TAU_FORMULA:.8f} — exact match.",
            "Mechanism: unknown — could be (a) Component B derives from τ² through",
            "  the deficit chain; (b) numerical coincidence; (c) undiscovered relationship.",
            f"α_vac = {ALPHA_VAC}: not explicitly in O(3) sector.",
            f"β_Q = {BETA_Q_CANON}: not explicitly in O(3) sector.",
            f"ω₀ = {OMEGA_0:.4f}: not explicitly in O(3) sector.",
            f"R_eq = {R_EQ:.4f}: not explicitly in O(3) sector (hedgehog core set by 1/√(λ·η²)).",
            "If the deficit chain is fully traced: the 1/(8π) normalization might be",
            "  derived from τ² through the self-healing condition and Φ_eq structure.",
            "This would be the most important parameter connection to establish.",
        ],
    )


def build_track_e() -> AuditTrack:
    """Track E: Is O(3) the unique minimal extension for bosonic winding charge?"""
    return AuditTrack(
        track_id="E",
        name="uniqueness_of_o3",
        question=(
            "Is O(3) the unique minimal real-scalar field extension that provides "
            "π₂(M) ≠ 0, giving bosonic winding charge in 3+1 dimensions?"
        ),
        status="unique_minimal",
        finding=(
            "For π₂(M) ≠ 0 from real scalar fields in 3+1D, the target manifold M "
            "must have non-trivial second homotopy group.  The simplest option is M = S², "
            "which has π₂(S²) = ℤ.  S² is a 2-dimensional manifold; the minimal real-scalar "
            "field content that lives on S² is 3 real scalars Φᵃ with one constraint "
            "|Φᵃ|² = η² (so 3-1 = 2 independent real DOF = dim(S²)).  This is the O(3) "
            "triplet.  No real-scalar system with fewer than 3 real scalars can achieve "
            "π₂ ≠ 0: a single real scalar has π₂(ℝ) = 0; two unconstrained reals have "
            "π₂(ℝ²) = 0.  The only 2-DOF alternative with π₂ ≠ 0 is CP(1) (1 complex "
            "scalar with a U(1) fiber), which has the same target space S² ≅ CP(1) and "
            "the same homotopy groups.  CP(1) and O(3)/S² are topologically equivalent.  "
            "Conclusion: O(3) IS the unique minimal REAL-SCALAR field extension for "
            "π₂ ≠ 0 in 3+1D.  This makes it a NECESSARY, not arbitrary, choice."
        ),
        contributes_to_nativity=False,
        blocking_gap_ref=None,
        motivation_ref="CM1",
        notes=[
            "Real scalar field, 1 DOF: π₂(ℝ) = 0 — no winding.",
            "Two real scalars, unconstrained: π₂(ℝ²) = 0 — no winding.",
            "Three real scalars, |Φᵃ|² = η² constraint: target S², π₂(S²) = ℤ — WINDING.",
            "This is the O(3) triplet with Mexican hat.  Minimal real-scalar option.",
            "CP(1): 2 complex scalars with |z₁|²+|z₂|²=1 → S³/S¹ = S² — equivalent.",
            "CP(1) has 4 real DOF with 1 constraint = 3 real, then 1 U(1) = 2 DOF.",
            "CP(1) and O(3) have the same target space — same topology, different description.",
            "For real scalar description: O(3) is unique (CP(1) uses complex scalars).",
            "Uniqueness: NOT 'uniquely forced by GRUT'; but 'the only minimal real choice'.",
            "This makes O(3) a NECESSARY postulate (not arbitrary) if winding is required.",
            "Necessary postulate ≠ derived from canonical architecture (BG1 still holds).",
        ],
    )


def build_blocking_gaps() -> List[BlockingGap]:
    """Build the three blocking gaps."""

    bg1 = BlockingGap(
        gap_id="BG1",
        name="discrete_dof_change",
        description=(
            "Going from 1 to 3 real scalar fields is a discrete change in field content.  "
            "No mathematical derivation converts one real scalar into three real scalars "
            "with an O(3) internal symmetry.  This gap is the most fundamental: it cannot "
            "be closed by any gradient expansion, CTP integration, or EFT argument because "
            "the DOF count itself changes.  The only resolution is a new field postulate."
        ),
        closeability="not_closeable_by_derivation",
        what_would_close_it=(
            "Nothing closes BG1 by pure derivation.  The best achievable outcome is: "
            "designate O(3) as a 'necessary motivated postulate' based on the topological "
            "uniqueness argument (Track E / CM1) and the Component B convergence (CM2).  "
            "This makes the postulation principled rather than ad hoc."
        ),
        closes_nativity_question=False,
        is_mathematical_impossibility=True,
        notes=[
            "DOF: 1 real scalar → 3 real scalars = 2 new real DOF introduced.",
            "Internal symmetry: none → O(3) = new symmetry group introduced.",
            "This is analogous to introducing a quark doublet from a single quark: impossible by EFT.",
            "Mathematical fact: no redefinition of a single real scalar produces O(3) symmetry.",
            "Consequence: O(3) will always require an explicit field-content postulate in GRUT.",
            "This makes the Skyrme term situation (motivated_but_unbuilt) vs O(3) situation",
            "  (motivated_independent_postulation) fundamentally different in kind.",
        ],
    )

    bg2 = BlockingGap(
        gap_id="BG2",
        name="target_space_constraint",
        description=(
            "The S² vacuum manifold requires the Mexican hat potential V(Φ) = -(μ²/2)|Φ|² + (λ/4)|Φ|⁴ "
            "to be present in the O(3) sector Lagrangian.  This potential is introduced by hand in "
            "defect_admissibility.py with free parameters μ, λ.  No mechanism in GRUT's canonical "
            "architecture (constitutive ODE, barrier action, CTP g_-) generates a quartic triplet "
            "potential.  The VEV η = μ/√λ sets the symmetry-breaking scale."
        ),
        closeability="closeable_under_conditions",
        what_would_close_it=(
            "Three options: (1) derive the Mexican hat V(Φ) from a CTP effective potential "
            "(CTP one-loop computation of the O(3) effective action); (2) show that the GRUT "
            "barrier sector generates an effective potential for the O(3) triplet; (3) derive "
            "η from GRUT constants (the numerical connection η² = τ²/(12π) hints at option 3)."
        ),
        closes_nativity_question=False,
        is_mathematical_impossibility=False,
        notes=[
            "Mexican hat parameters in defect_admissibility.py: MU_DEFAULT=1, LAMBDA_DEFAULT=8π.",
            "These values are set phenomenologically to satisfy η² = 1/(8π) from Component B.",
            "The ratio λ/μ² = 1/η² is constrained; μ and λ individually are free.",
            f"Partial parameter link: η² = τ²/(12π) = {ETA_SQ_FROM_TAU_FORMULA:.6f}.",
            "If the deficit chain can be traced to yield 1/(8π) from τ²: BG2 becomes partial.",
            "This gap is more closeable than BG1 — it's about parameters, not DOF count.",
        ],
    )

    bg3 = BlockingGap(
        gap_id="BG3",
        name="internal_symmetry_origin",
        description=(
            "The O(3) internal symmetry group (acting on the triplet index a=1,2,3) has no "
            "origin in canonical GRUT's scalar architecture.  The canonical scalar has only "
            "Z₂ symmetry at best.  The spatial SO(3) is present (spherical symmetry), but "
            "internal O(3) and spatial SO(3) are distinct groups acting on different spaces."
        ),
        closeability="partially_closeable",
        what_would_close_it=(
            "Partial closure via the hedgehog diagonal symmetry: the ansatz Φᵃ = η·f(r)·x̂ᵃ "
            "identifies internal O(3) with spatial SO(3) for hedgehog configurations.  This "
            "makes the two groups effectively the same for the winding-number classification.  "
            "Full closure would require showing that the spatial SO(3) of GRUT can be "
            'promoted to an internal O(3) through some "orientifold-like" construction.'
        ),
        closes_nativity_question=False,
        is_mathematical_impossibility=False,
        notes=[
            "Spatial SO(3) in GRUT: x → Rx for spatial rotations.  Real, present.",
            "Internal O(3): Φᵃ → R^a_b Φᵇ for component rotations.  Must be postulated.",
            "Hedgehog diagonal: Φᵃ = η·f(r)·x̂ᵃ → invariant under (L+T) = diagonal SO(3).",
            "The hedgehog is 'spherically symmetric' under diagonal SO(3), not independently.",
            "Once O(3) is postulated, BG3 is partially addressed by the hedgehog ansatz.",
            "BG3 is less fundamental than BG1: it's about symmetry identification, not DOF count.",
        ],
    )

    return [bg1, bg2, bg3]


def build_convergent_motivations() -> List[ConvergentMotivation]:
    """Build the two convergent motivations for O(3)."""

    cm1 = ConvergentMotivation(
        motivation_id="CM1",
        name="topological_gap_fill",
        description=(
            "The canonical GRUT architecture has π₂(ℝ) = 0: no bosonic topological winding "
            "charge.  For bosonic particle-like objects, GRUT needs a field sector with "
            "π₂(M) ≠ 0.  O(3) is the unique minimal real-scalar extension achieving this.  "
            "This motivation is structural (from topology), not phenomenological."
        ),
        is_topological=True,
        is_phenomenological=False,
        motivates_o3_uniquely=True,
        parameter_constrained=False,
        parameter_constraint=None,
        notes=[
            "π₂(ℝ) = 0: canonical scalar cannot support bosonic winding charge.",
            "π₂(S²) = ℤ: O(3) triplet supports integer bosonic winding number n.",
            "Topological necessity: if bosonic winding charge is required, O(3) is required.",
            "Uniqueness: no smaller real-scalar system gives π₂ ≠ 0 (Track E establishes this).",
            "This makes O(3) the NECESSARY MINIMAL CHOICE, not an arbitrary choice.",
            "Strength: this is the strongest motivation — structural, not phenomenological.",
        ],
    )

    cm2 = ConvergentMotivation(
        motivation_id="CM2",
        name="component_b_tail_matching",
        description=(
            "The interior deficit program (Phase 6C) requires a Component B contribution "
            "ε_B ~ A_B/r² with A_B = 1/(8π).  The O(3) hedgehog asymptotic tail exactly "
            "reproduces this profile with the matching condition η² = 1/(8π).  This is "
            "phenomenological motivation: O(3) produces the exact required tail shape "
            "and normalization."
        ),
        is_topological=False,
        is_phenomenological=True,
        motivates_o3_uniquely=False,
        parameter_constrained=True,
        parameter_constraint=f"eta^2 = 1/(8*pi) = COMP_B_COEFF ≈ {COMP_B_COEFF:.6f}",
        notes=[
            f"COMP_B_COEFF = 1/(8π) ≈ {COMP_B_COEFF:.6f}.",
            f"η² = COMP_B_COEFF: matching condition from defect_admissibility.py Result 5.",
            f"Numerical connection: η² = τ²/(12π) = {TAU_SQ}/(12π) ≈ {ETA_SQ_FROM_TAU_FORMULA:.6f}.",
            "This constrains ONE O(3) parameter from a GRUT-derived requirement.",
            "Phenomenological, not topological: other field content might also produce 1/r² tail.",
            "Combined with CM1: two independent convergences make O(3) strongly motivated.",
            "Strength: strong but not unique — the tail shape alone doesn't uniquely select O(3).",
        ],
    )

    return [cm1, cm2]


def build_nativity_criteria(
    tracks: List[AuditTrack],
    blocking_gaps: List[BlockingGap],
) -> List[NativityCriterion]:
    """Build the four nativity criteria."""

    n1 = NativityCriterion(
        criterion_id=1,
        name="N1_field_content_derivability",
        description="Can the O(3) triplet be derived from canonical GRUT's single real scalar without new field content postulate?",
        passes=False,
        pass_level="hard_fail",
        reason=(
            "BG1 is a mathematical impossibility: no derivation converts 1 real scalar "
            "into 3 real scalars with O(3) symmetry.  Track A (canonical scalar promotion) "
            "is 'not_derivable'.  The defect_admissibility.py module explicitly states "
            "the triplet is a candidate extension, not a derivation.  N1 cannot pass."
        ),
        blocking_gap_ref="BG1",
        conditional_path=None,
        notes=[
            "N1 failure is irresolvable by derivation.",
            "The only resolution: designate O(3) as a necessary postulate.",
            "This changes the question from 'can we derive O(3)?' to 'is the postulate motivated?'",
        ],
    )

    n2 = NativityCriterion(
        criterion_id=2,
        name="N2_target_space_derivability",
        description="Can the S² vacuum manifold (Mexican hat constraint) be derived from GRUT's barrier/constitutive/CTP architecture?",
        passes=False,
        pass_level="soft_fail",
        reason=(
            "BG2: No mechanism in canonical GRUT (constitutive ODE, barrier action, CTP) "
            "generates the Mexican hat potential V(Φ) for a field triplet.  "
            "The parameters μ, λ are free in defect_admissibility.py.  "
            "One partial connection exists: η² = τ²/(12π) (mechanism unknown).  "
            "N2 is a soft fail: BG2 is potentially closeable (unlike BG1) but currently open."
        ),
        blocking_gap_ref="BG2",
        conditional_path=(
            "If the interior deficit program (Phase 6C) can be shown to derive "
            "COMP_B_COEFF = 1/(8π) from τ² through the self-healing / metric-deficit chain, "
            "then η would be partially constrained by GRUT architecture.  This would "
            "partially satisfy N2 for the η parameter, leaving μ and λ individually free."
        ),
        notes=[
            "N2 is a soft fail — potentially closeable via Component B derivation chain.",
            "The numerical link η² = τ²/(12π) is real but mechanism-unknown.",
            "CTP route: g_- effective potential computation might generate a term like V(Φ).",
        ],
    )

    n3 = NativityCriterion(
        criterion_id=3,
        name="N3_internal_symmetry_emergence",
        description="Does GRUT's canonical architecture generate or imply an O(3) internal symmetry group?",
        passes=False,
        pass_level="partial",
        reason=(
            "BG3 (partial): Spatial SO(3) is present in GRUT (spherical symmetry).  "
            "The hedgehog ansatz locks internal O(3) to spatial SO(3) via "
            "Φᵃ = η·f(r)·x̂ᵃ.  This makes the hedgehog spherically symmetric under "
            "the diagonal symmetry.  However, the internal O(3) must first be postulated "
            "(BG1); only then can the spatial SO(3) identification be made.  "
            "N3 is at most a partial: spatial SO(3) provides the symmetry ONCE the triplet "
            "is introduced, but does not generate the triplet itself."
        ),
        blocking_gap_ref="BG3",
        conditional_path=(
            "Once O(3) is postulated (BG1 resolved by motivated postulate), the hedgehog "
            "diagonal symmetry identification makes N3 partially satisfied: the internal "
            "O(3) is identified with spatial SO(3) for hedgehog configurations.  "
            "This is the best achievable N3 outcome in GRUT's spherically symmetric domain."
        ),
        notes=[
            "N3 is the 'partially closeable' criterion — depends on BG3 resolution.",
            "Spatial SO(3) present: this is real and useful for the hedgehog.",
            "Internal O(3) absent: must be postulated first, then identified with spatial SO(3).",
            "N3 partial pass: achievable AFTER O(3) postulation, not before.",
        ],
    )

    n4 = NativityCriterion(
        criterion_id=4,
        name="N4_parameter_determination",
        description="Can the O(3) parameters η, μ, λ be determined from GRUT canonical constants without free choices?",
        passes=False,
        pass_level="partial",
        reason=(
            f"One partial connection: η² = τ²/(12π) = {ETA_SQ_FROM_COMP_B:.6f} "
            f"(since τ² = {TAU_SQ} and 1/(8π) ≈ {COMP_B_COEFF:.6f}).  "
            "This constrains the VEV η from the Component B matching condition, "
            "which traces back to GRUT's interior deficit program.  "
            "However: μ and λ individually are free (MU_DEFAULT=1.0, LAMBDA_DEFAULT=8π "
            "in defect_admissibility.py — set by phenomenological convention).  "
            "Only the ratio λ/μ² = 1/η² is determined.  "
            "The mechanism for η² = τ²/(12π) is unknown.  "
            f"GRUT constants α_vac = {ALPHA_VAC}, β_Q = {BETA_Q_CANON}, "
            f"ω₀ = {OMEGA_0:.3f}, R_eq = {R_EQ:.3f} do not appear in the O(3) sector."
        ),
        blocking_gap_ref=None,
        conditional_path=(
            "Full determination requires: (1) deriving η from the GRUT deficit chain "
            "(establishing the mechanism for η² = τ²/(12π)); (2) deriving the ratio "
            "λ/μ² from stability or normalization conditions; (3) deriving μ individually "
            "from a mass scale in GRUT (possibly ω₀ or 1/R_eq).  "
            "Step (1) is the most promising — it requires tracing COMP_B_COEFF back "
            "through Phase 6C to τ²."
        ),
        notes=[
            f"η² = {ETA_SQ_FROM_COMP_B:.8f} = 1/(8π): one constraint from Component B.",
            f"τ²/(12π) = {ETA_SQ_FROM_TAU_FORMULA:.8f}: exactly equal — numerical link.",
            "λ/μ² = 1/η² ≈ 8π: constrained by VEV condition — but μ and λ individually free.",
            "Mass dimension: μ has dimension of mass; no GRUT mass scale tied to μ yet.",
            "ω₀ = √27: candidate mass scale — if μ ~ ω₀, then λ ~ ω₀²/η² — unverified.",
        ],
    )

    return [n1, n2, n3, n4]


def build_uniqueness_check() -> UniquenessCheck:
    """Assess whether O(3) is uniquely minimal for π₂ ≠ 0."""
    return UniquenessCheck(
        question=(
            "Is O(3) the unique minimal real-scalar field extension that provides "
            "π₂(M) ≠ 0 in 3+1 dimensions?"
        ),
        o3_is_minimal_for_pi2_nonzero=True,
        alternative_with_fewer_real_fields=False,
        cp1_equivalent=True,
        cp1_uses_same_dof_count=True,
        uniqueness_verdict=(
            "o3_is_unique_minimal_real_scalar_extension__"
            "cp1_is_topologically_equivalent_but_uses_complex_scalars__"
            "no_smaller_real_scalar_system_achieves_pi2_nonzero"
        ),
        notes=[
            "1 real scalar: π₂(ℝ) = 0 — impossible.",
            "2 real scalars (unconstrained): π₂(ℝ²) = 0 — impossible.",
            "2 real scalars (S¹ constraint: |Φ|² = η²): π₂(S¹) = 0 — impossible.",
            "3 real scalars (S² constraint: |Φᵃ|² = η²): π₂(S²) = ℤ — works! (O(3))",
            "CP(1): 4 real scalars (2 complex) with |z₁|²+|z₂|²=1 → S² — equivalent.",
            "CP(1) has the same target space S² as O(3) — topologically equivalent.",
            "For REAL scalar field content: O(3) is the unique minimal option.",
            "Uniqueness: not 'derived by GRUT' but 'the only right thing to add'.",
            "This is the strongest argument for O(3) over all other possible extensions.",
            "Conclusion: O(3) is a NECESSARY postulate (not arbitrary) IF winding charge is needed.",
        ],
    )


def build_parameter_mapping() -> ParameterMapping:
    """Assess O(3) parameter connections to canonical GRUT."""
    return ParameterMapping(
        eta_sq_from_comp_b=ETA_SQ_FROM_COMP_B,
        eta_sq_from_tau_formula=ETA_SQ_FROM_TAU_FORMULA,
        tau_connection_holds_numerically=True,
        tau_connection_mechanism_known=False,
        mu_fixed_by_grut=False,
        lambda_fixed_by_grut=False,
        ratio_lambda_over_mu_sq_constrained=True,
        grut_constants_not_used=["alpha_vac", "beta_Q", "omega_0", "R_eq"],
        summary=(
            f"One partial connection: η² = τ²/(12π) = {ETA_SQ_FROM_COMP_B:.8f} "
            f"(from Component B matching, mechanism unknown).  "
            f"Parameters μ, λ individually free.  "
            f"GRUT constants α_vac, β_Q, ω₀, R_eq do not appear in the O(3) sector."
        ),
        notes=[
            f"η = {ETA_FROM_COMP_B:.6f}: constrained via Component B (η² = 1/(8π)).",
            f"τ² = {TAU_SQ}: gives η² = τ²/(12π) — exact match at canonical values.",
            f"μ = {MU_DEFAULT}: free (set by convention in defect_admissibility.py).",
            f"λ = 8π ≈ {LAMBDA_DEFAULT:.4f}: constrained only by λ = μ²/η² = 8π when μ=1.",
            "The pair (μ=1, λ=8π) is a choice within the family satisfying η² = 1/(8π).",
            "Many other pairs (μ=2, λ=32π), (μ=0.5, λ=2π) etc. give same η.",
            "True free parameters: one mass scale (e.g., μ) and η (constrained by Component B).",
            "Agenda item: trace COMP_B_COEFF = 1/(8π) back through Phase 6C to τ².",
        ],
    )


def build_doctrine_compatibility() -> DoctrineCompatibilityCheck:
    """Check doctrine compatibility of adding O(3) as a motivated postulate."""
    return DoctrineCompatibilityCheck(
        consistent_with_phi_bifurcation=True,
        consistent_with_tau_eff_domain=True,
        consistent_with_beta_q_hypothesis=True,
        consistent_with_fermionic_audit=True,
        consistent_with_appendix_m=True,
        consistent_with_skyrme_audit=True,
        introduces_new_field_content=True,
        introduces_new_free_parameters=True,
        compatible_with_prior_doctrine=True,
        doctrine_impact=(
            "Adding O(3) as a motivated independent postulate is COMPATIBLE with all prior "
            "GRUT audits.  It does not: (a) contradict the Φ bifurcation — O(3) triplet Φᵃ "
            "is distinct from both the trajectory M_drive and the constitutive Φ(r,t); "
            "(b) violate the τ_eff domain — the O(3) sector is a static/quasi-static field, "
            "consistent with the declared domain; (c) conflict with the fermionic emergence "
            "audit — O(3) hedgehog has bosonic statistics (no Hopf term); "
            "(d) conflict with Appendix M — O(3) was already the identified candidate; "
            "(e) conflict with the Skyrme audit — O(3) nativity was the explicit prerequisite.  "
            "It DOES introduce: (i) 3 new real scalar fields (BG1 — new postulate); "
            "(ii) at least one new free parameter (mass scale μ; η is constrained by Component B)."
        ),
        notes=[
            "Φ bifurcation: O(3) triplet Φᵃ ≠ M_drive(t) ≠ Φ(r,t). Three distinct objects.",
            "τ_eff domain: O(3) static energy is evaluated in quasi-static limit (consistent).",
            "β_Q: Skyrme audit showed L₄ independent of β_Q; O(3) similarly independent.",
            "Fermionic audit: O(3) bosonic — confirmed (hedgehog statistics bosonic, Hopf absent).",
            "Appendix M: O(3) hedgehog n=1 was already the identified candidate entity.",
            "Skyrme audit: Route 3 was explicitly conditional on O(3) nativity — now audited.",
            "New field content: 3 real scalars Φᵃ introduced explicitly.",
            "New free parameters: one mass scale (μ) and the ratio λ/μ² (set by η).",
        ],
    )


def build_patchwork_assessment(
    blocking_gaps: List[BlockingGap],
    criteria: List[NativityCriterion],
    motivations: List[ConvergentMotivation],
    uniqueness: UniquenessCheck,
) -> PatchworkAssessment:
    """Assess O(3) patchwork vs native status."""
    bg1_irresolvable = next(g for g in blocking_gaps if g.gap_id == "BG1")
    motivated_by_cm1 = any(m.motivates_o3_uniquely for m in motivations)
    motivated_by_cm2 = any(m.parameter_constrained for m in motivations)

    return PatchworkAssessment(
        derives_from_canonical_scalar=False,
        motivated_independent_postulation=motivated_by_cm1 and uniqueness.o3_is_minimal_for_pi2_nonzero,
        arbitrary_auxiliary_extension=False,
        incompatible_with_canonical_architecture=False,
        patchwork_verdict="motivated_independent_postulation",
        comparison_to_skyrme_term=(
            "The Skyrme term nativity audit returned 'motivated_but_unbuilt': the Skyrme "
            "term could become native once O(3) nativity is established (Route 3 closes).  "
            "The O(3) nativity audit returns 'motivated_independent_postulation': O(3) can "
            "NEVER be derived from the canonical scalar (BG1 is a mathematical impossibility).  "
            "However: the MOTIVATION for O(3) is STRONGER than for the Skyrme term — it is "
            "backed by topological uniqueness (CM1) AND phenomenological convergence (CM2).  "
            "The Skyrme term was 'motivated' only because it is the next-order term in an EFT "
            "that GRUT hasn't built yet.  O(3) is 'motivated' because it is the ONLY choice "
            "if GRUT wants bosonic winding charge from real scalar fields.  "
            "Summary: Skyrme term → derivable if O(3) is established.  "
            "O(3) → always postulated, but postulated necessarily and non-arbitrarily."
        ),
        what_best_outcome_looks_like=(
            "The best achievable outcome for O(3) in GRUT is: "
            "(1) O(3) is formally designated as a 'necessary motivated postulate' (not 'derived'); "
            "(2) the topological uniqueness argument (CM1) is the primary justification; "
            "(3) the Component B matching (CM2) provides a phenomenological anchor; "
            "(4) the parameter η is expressed in terms of τ² (via COMP_B_COEFF = τ²/(12π)); "
            "(5) the mass scale μ is either derived from GRUT (e.g., μ ~ ω₀ or μ ~ 1/R_eq) "
            "    or designated as a new working canon hypothesis (analogous to β_Q = 2); "
            "(6) the Skyrme audit's Route 3 then closes: O(3) postulated → Skyrme L₄ is natural "
            "    next-order term → stable bosonic hedgehog candidate established.  "
            "This is the full chain from canonical GRUT to a stable bosonic particle candidate."
        ),
        notes=[
            "BG1 irresolvable by derivation: motivated_independent_postulation is the correct verdict.",
            "Not arbitrary: CM1 (topological uniqueness) + CM2 (Component B) provide two convergences.",
            "Not incompatible: all prior doctrine is preserved.",
            "Key insight: O(3) postulation is QUALITATIVELY different from Skyrme postulation.",
            "  Skyrme: could be derived from O(3) (same field content, next EFT order).",
            "  O(3): requires new field content — irreducible postulate.",
            "Best status achievable: 'necessary motivated postulate', not 'derived native sector'.",
        ],
    )


def assign_verdicts(
    criteria: List[NativityCriterion],
    uniqueness: UniquenessCheck,
    blocking_gaps: List[BlockingGap],
) -> tuple[str, str]:
    """Assign primary and secondary verdicts from the closed label set.

    Deterministic rules:
      If all criteria pass: o3_conditionally_derivable_from_collective_modes
      If N1 hard-fails but motivations strong: o3_auxiliary_but_minimally_motivated
      If N1 hard-fails and no motivation: no_native_o3_derivation_found
      If N1 hard-fails and postulation clearly required: o3_requires_independent_field_postulation
    """
    n1_fails = not criteria[0].passes  # N1 is always criteria[0]
    bg1_irresolvable = blocking_gaps[0].is_mathematical_impossibility  # BG1
    uniquely_motivated = uniqueness.o3_is_minimal_for_pi2_nonzero

    all_pass = all(c.passes for c in criteria)

    if all_pass:
        primary = "o3_conditionally_derivable_from_collective_modes"
        secondary = "o3_auxiliary_but_minimally_motivated"
    elif n1_fails and bg1_irresolvable and uniquely_motivated:
        # Standard case: BG1 irresolvable, but topological uniqueness motivates
        primary = "o3_auxiliary_but_minimally_motivated"
        secondary = "o3_requires_independent_field_postulation"
    elif n1_fails and bg1_irresolvable and not uniquely_motivated:
        primary = "no_native_o3_derivation_found"
        secondary = "o3_requires_independent_field_postulation"
    else:
        primary = "no_native_o3_derivation_found"
        secondary = "o3_requires_independent_field_postulation"

    assert primary in ALLOWED_NATIVITY_VERDICTS, f"Bad primary: {primary}"
    assert secondary in ALLOWED_NATIVITY_VERDICTS, f"Bad secondary: {secondary}"
    return primary, secondary


def _build_nonclaims() -> List[str]:
    return [
        "NOT claiming O(3) is arbitrary — two convergent motivations (CM1: topological "
        "uniqueness, CM2: Component B tail) make it the non-arbitrary minimal choice.",

        "NOT claiming O(3) can never have a deeper justification — only that it cannot "
        "be DERIVED from the canonical scalar (BG1 is irresolvable by derivation).  "
        "The best achievable status is 'necessary motivated postulate'.",

        "NOT claiming the η² = τ²/(12π) connection is meaningless — it is a real numerical "
        "fact at canonical GRUT values; the physical mechanism behind it is the open question.",

        "NOT claiming adding O(3) violates prior GRUT doctrine — it is fully compatible "
        "with all audited prior results.",

        "NOT claiming BG3 (internal symmetry) cannot be partially addressed — the hedgehog "
        "diagonal symmetry identification provides a real partial closure of BG3.",

        "NOT claiming the defect language in Phase D1+ is incorrect — it is correctly "
        "formulated and shape-compatible with Component B.  The audit questions nativity, "
        "not validity.",

        "NOT claiming O(3) must be abandoned — on the contrary, it should be retained as "
        "a formally-declared necessary postulate with the two convergent motivations recorded.",

        "NOT ruling out that the Skyrme term can eventually be native — once O(3) is "
        "formally postulated (with motivations recorded), Route 3 of the Skyrme audit "
        "closes: L₄ becomes the natural next-order term in the O(3) EFT.",
    ]


def _build_forbidden_inferences() -> List[str]:
    return [
        "o3_is_derived_from_canonical_grut_scalar",
        "topological_uniqueness_implies_architectural_derivation",
        "component_b_matching_implies_o3_nativity",
        "hedgehog_ansatz_derives_internal_o3_symmetry",
        "eta_tau_connection_implies_full_parameter_derivation",
        "motivated_postulate_means_same_as_native_sector",
        "bg1_is_closeable_by_gradient_expansion_or_ctp",
        "o3_postulation_is_arbitrary_because_not_derived",
    ]


def run_o3_nativity_audit() -> O3NativityResult:
    """Run the O(3) sector nativity audit.

    Returns a deterministic O3NativityResult with five audit tracks,
    three blocking gaps, two convergent motivations, four nativity criteria,
    a uniqueness check, parameter mapping, doctrine compatibility, and
    patchwork assessment.  Primary and secondary verdicts are assigned from
    the closed label set.
    """
    tracks = [
        build_track_a(),
        build_track_b(),
        build_track_c(),
        build_track_d(),
        build_track_e(),
    ]

    blocking_gaps = build_blocking_gaps()
    convergent_motivations = build_convergent_motivations()
    criteria = build_nativity_criteria(tracks, blocking_gaps)
    uniqueness = build_uniqueness_check()
    param_map = build_parameter_mapping()
    doctrine = build_doctrine_compatibility()
    patchwork = build_patchwork_assessment(
        blocking_gaps, criteria, convergent_motivations, uniqueness
    )

    primary, secondary = assign_verdicts(criteria, uniqueness, blocking_gaps)

    # Top-level Booleans
    canonical_scalar_implies_o3 = False
    target_space_generated_by_grut = False
    internal_symmetry_from_grut = False     # BG3 partial only
    o3_is_unique_minimal_extension = uniqueness.o3_is_minimal_for_pi2_nonzero
    component_b_motivates_o3 = any(m.parameter_constrained for m in convergent_motivations)
    parameter_connection_found = param_map.tau_connection_holds_numerically
    parameter_connection_mechanism_known = param_map.tau_connection_mechanism_known
    all_nativity_criteria_pass = all(c.passes for c in criteria)

    diagnostics: Dict[str, Any] = {
        "M_EXT": M_EXT,
        "R_EQ": R_EQ,
        "TAU_SQ": TAU_SQ,
        "ALPHA_VAC": ALPHA_VAC,
        "BETA_Q_CANON": BETA_Q_CANON,
        "OMEGA_0_SQ": OMEGA_0_SQ,
        "OMEGA_0": OMEGA_0,
        "SPATIAL_DIMENSION": SPATIAL_DIMENSION,
        "N_CANONICAL_FIELDS": N_CANONICAL_FIELDS,
        "N_O3_FIELDS": N_O3_FIELDS,
        "PI2_REAL_SCALAR": PI2_REAL_SCALAR,
        "PI2_S2": PI2_S2,
        "COMP_B_COEFF": COMP_B_COEFF,
        "ETA_SQ_FROM_COMP_B": ETA_SQ_FROM_COMP_B,
        "ETA_SQ_FROM_TAU_FORMULA": ETA_SQ_FROM_TAU_FORMULA,
        "eta_tau_connection_holds": param_map.tau_connection_holds_numerically,
        "eta_tau_mechanism_known": param_map.tau_connection_mechanism_known,
        "LAMBDA_DEFAULT": LAMBDA_DEFAULT,
        "canonical_scalar_implies_o3": canonical_scalar_implies_o3,
        "target_space_generated_by_grut": target_space_generated_by_grut,
        "internal_symmetry_from_grut": internal_symmetry_from_grut,
        "o3_is_unique_minimal_extension": o3_is_unique_minimal_extension,
        "component_b_motivates_o3": component_b_motivates_o3,
        "parameter_connection_found": parameter_connection_found,
        "all_nativity_criteria_pass": all_nativity_criteria_pass,
        "n_blocking_gaps": len(blocking_gaps),
        "n_convergent_motivations": len(convergent_motivations),
        "n_nativity_criteria": len(criteria),
        "bg1_irresolvable_by_derivation": blocking_gaps[0].is_mathematical_impossibility,
        "bg2_partially_closeable": blocking_gaps[1].closeability == "closeable_under_conditions",
        "bg3_partially_closeable": blocking_gaps[2].closeability == "partially_closeable",
        "patchwork_verdict": patchwork.patchwork_verdict,
        "doctrine_compatible": doctrine.compatible_with_prior_doctrine,
        "primary_verdict": primary,
        "secondary_verdict": secondary,
    }

    return O3NativityResult(
        tracks=tracks,
        blocking_gaps=blocking_gaps,
        convergent_motivations=convergent_motivations,
        nativity_criteria=criteria,
        uniqueness_check=uniqueness,
        parameter_mapping=param_map,
        doctrine_check=doctrine,
        patchwork=patchwork,
        canonical_scalar_implies_o3=canonical_scalar_implies_o3,
        target_space_generated_by_grut=target_space_generated_by_grut,
        internal_symmetry_from_grut=internal_symmetry_from_grut,
        o3_is_unique_minimal_extension=o3_is_unique_minimal_extension,
        component_b_motivates_o3=component_b_motivates_o3,
        parameter_connection_found=parameter_connection_found,
        parameter_connection_mechanism_known=parameter_connection_mechanism_known,
        all_nativity_criteria_pass=all_nativity_criteria_pass,
        n_canonical_fields=N_CANONICAL_FIELDS,
        n_o3_fields=N_O3_FIELDS,
        field_content_change_is_discrete=True,
        doctrine_compatible=doctrine.compatible_with_prior_doctrine,
        primary_verdict=primary,
        secondary_verdict=secondary,
        nonclaims=_build_nonclaims(),
        forbidden_inferences=_build_forbidden_inferences(),
        diagnostics=diagnostics,
    )
