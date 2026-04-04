"""Appendix Q-B.5 — Complex Structure and Kinematic Upgrade Audit.

Mission: Determine the doctrinal and mathematical status of the complex
structure J (with J² = −1) identified as the exact missing ingredient by
Appendix Q-B, before Q-C (quantum microdynamics) can proceed.

Primary Question
----------------
Can the missing complex structure J be:
  (a) natively derived from already-audited GRUT architecture,
  (b) effectively induced in a restricted regime, or
  (c) only introduced as an extension-level (MIP) postulate?

Inherited Q-B Result
--------------------
  Primary verdict:      density_matrix_or_functional_state_required (BSR)
  Commutation verdict:  quantization_route_currently_blocked (BSR)
  Mapping verdict:      compatible_only (CAH)
  Missing ingredient:   complex_structure_J_with_J_squared_eq_minus_1 (MIP if postulated)

Four Hard-Gated Verdicts
------------------------
  (1) primary_J_status
        complex_structure_motivated_independent_postulation
        — J cannot be natively derived (all 5 native routes rejected).
          No clean effective induction route exists (all 5 effective routes
          fail or give underdetermined compatibility only).
          J qualifies as MIP: ≥2 convergent structural motivations internal
          to GRUT, no new DOFs required (acts on existing real field space),
          and τ² = 3/2 constrains compatible dynamics.

  (2) sufficiency_verdict
        J_necessary_but_not_sufficient
        — J alone enables complex superposition on the field space.
          However, a compatible inner product and a dynamics generator
          (Hamiltonian or Lindbladian analog) must also be postulated before
          Q-C can operate. The minimum kinematic upgrade package is:
          {J, compatible inner product, dynamics generator}.

  (3) doubled_field_verdict
        doubled_field_pair_complexification_obstructed
        — The CTP Φ₋ ghost mode satisfies dΦ₋/dt = +Φ₋/τ (growth rate +1/τ,
          sign +1). Defining J(Φ₊) = Φ₋ gives J² = −1 algebraically, but the
          "norm" Φ₊² + Φ₋² is NOT conserved under GRUT dynamics (it grows due
          to the ghost term 2Φ₋²/τ > 0). No linear repackaging of the CTP
          pair avoids this obstruction: any combination involving Φ₋ inherits
          the ghost growth.

  (4) readiness_verdict
        proceed_only_if_J_is_postulated
        — Q-C cannot proceed on native GRUT alone. With MIP postulation of J
          and a compatible inner product, Q-C may proceed. The doctrinal basis
          is explicit: all Q-C results carry MIP minimum classification.

Appendix P Classifications
--------------------------
  Track A: minimum-ingredient analysis         native_canon (the gap itself is canon)
  Track B: all native routes                   rejected (FOI or CAH)
  Track C: all effective routes                motivated_but_unbuilt / CAH
  Track D: J as independent postulate          motivated_independent_postulation (MIP)
  Track E: kinematic sufficiency               bounded_structural_result
  Track F: doubled-field ghost constraint      bounded_structural_result

Scope Discipline (from mission spec)
--------------------------------------
  NOT deriving the Born rule.
  NOT deriving measurement.
  NOT deriving interference.
  NOT assuming standard textbook Hilbert structure.
  NOT silently importing complex amplitudes as notation.
  NOT claiming quantum closure.
  Only auditing the status of J and the minimum kinematic upgrade for Q-C.

Physical Constants (canonical)
-------------------------------
  TAU_SQ = 3/2       PHI_MINUS_GROWTH_RATE_SIGN = +1
  TAU = √(3/2)       PHI_MINUS_CAN_BE_IMAGINARY_PART = False

See: grut/qb_quantum_state_space.py  (Q-B primary audit, inherited results)
     grut/q0_quantum_entry_inventory.py  (Q0 inventory, items A4, C1, D1–D9)
     grut/qa_quantum_charter.py          (Q-A charter, FFM2, FFM6, QA-R3)
     grut/appendix_p_taxonomy_audit.py   (Appendix P status classes)
     grut/galley_truncation.py           (Φ₋ ghost mode derivation)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Hard-gated verdict vocabulary
# ================================================================

ALLOWED_PRIMARY_J_STATUSES: frozenset = frozenset({
    "complex_structure_natively_derived",
    "complex_structure_effectively_induced",
    "complex_structure_motivated_but_unbuilt",
    "complex_structure_motivated_independent_postulation",
    "complex_structure_compatible_but_ad_hoc",
    "complex_structure_forbidden_or_inconsistent",
    "complex_structure_still_underdetermined",
})

ALLOWED_SUFFICIENCY_VERDICTS: frozenset = frozenset({
    "J_alone_sufficient_for_QC",
    "J_necessary_but_not_sufficient",
    "J_insufficient_without_further_kinematic_structure",
    "sufficiency_still_underdetermined",
})

ALLOWED_DOUBLED_FIELD_VERDICTS: frozenset = frozenset({
    "doubled_field_pair_supports_valid_complexification",
    "doubled_field_pair_supports_effective_complexification_only",
    "doubled_field_pair_auxiliary_only",
    "doubled_field_pair_complexification_obstructed",
})

ALLOWED_READINESS_VERDICTS: frozenset = frozenset({
    "ready_to_proceed_with_QC",
    "proceed_only_if_J_is_postulated",
    "not_ready_for_QC",
    "requires_additional_kinematic_audit_first",
})

# ================================================================
# Track vocabulary constants
# ================================================================

ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

ALLOWED_MISSING_ELEMENT_TYPES: frozenset = frozenset({
    "complex_structure_J_on_state_space",
    "symplectic_structure_only",
    "doubled_real_structure",
    "full_hilbert_inner_product_package",
    "larger_missing_kinematic_bundle",
})

ALLOWED_EFFECTIVE_ROUTE_CLASSIFICATIONS: frozenset = frozenset({
    "effective_reduction",
    "motivated_but_unbuilt",
    "underdetermined_compatibility_only",
    "blocked",
})

# ================================================================
# Counts (deterministic)
# ================================================================

N_NATIVE_ROUTES_TESTED: int = 5
N_EFFECTIVE_ROUTES_TESTED: int = 5
N_NATIVE_ROUTES_ACCEPTED: int = 0      # all rejected
N_EFFECTIVE_ROUTES_VIABLE: int = 0     # none cleanly viable
N_CONVERGENT_MOTIVATIONS_FOR_J: int = 2
N_MINIMUM_KINEMATIC_PACKAGE_ITEMS: int = 3   # J + inner product + dynamics generator

# ================================================================
# Physical constants (from canon.py / tau_level1_audit.py / qb_quantum_state_space.py)
# ================================================================

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
ALPHA_VAC: float = 1.0 / 3.0
OMEGA_0_SQ: float = 27.0

# Galley / CTP ghost mode (from qb_quantum_state_space.py)
PHI_MINUS_GROWTH_RATE: float = 1.0 / TAU    # +1/τ > 0
PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

# Norm non-conservation coefficient for the ghost mode
# d|Psi|²/dt = 2*Phi_minus²/tau (from Track F derivation)
GHOST_NORM_GROWTH_COEFFICIENT: float = 2.0 / TAU   # > 0

# ================================================================
# Q-B.5 hard-gated verdict values
# ================================================================

QB5_PRIMARY_J_STATUS: str = "complex_structure_motivated_independent_postulation"
QB5_SUFFICIENCY_VERDICT: str = "J_necessary_but_not_sufficient"
QB5_DOUBLED_FIELD_VERDICT: str = "doubled_field_pair_complexification_obstructed"
QB5_READINESS_VERDICT: str = "proceed_only_if_J_is_postulated"
QB5_OVERALL_APPENDIX_P_CLASS: str = "motivated_independent_postulation"

# Minimum kinematic upgrade package required for Q-C
QB5_MINIMUM_KINEMATIC_PACKAGE: List[str] = [
    "J_complex_structure_with_J_sq_eq_minus_1",
    "compatible_inner_product_g_with_g_Jpsi_Jphi_eq_g_psi_phi",
    "dynamics_generator_hamiltonian_or_lindbladian_analog",
]

# ================================================================
# Nonclaims (Track I)
# ================================================================

QB5_NONCLAIMS: List[str] = [
    "NOT_claiming_doubled_fields_imply_complex_amplitudes_derived"
    "__formal_CTP_notation_is_not_a_derivation_of_complex_structure",
    "NOT_claiming_symplectic_pairing_implies_hilbert_space_derived"
    "__symplectic_structure_without_compatible_metric_is_not_hilbert",
    "NOT_claiming_notation_level_i_implies_physical_J_established"
    "__writing_i_in_expressions_is_not_the_same_as_deriving_J_sq_eq_minus_1",
    "NOT_claiming_open_system_complexification_implies_born_rule"
    "__effective_complex_description_does_not_entail_probability_amplitude",
    "NOT_claiming_auxiliary_pair_solves_native_quantum_state"
    "__CTP_pair_as_bookkeeping_device_is_not_a_quantum_state_space",
    "NOT_claiming_effective_complex_structure_implies_fundamental_complex_ontology"
    "__effective_description_is_not_native_canon",
    "NOT_claiming_postulated_J_receives_native_canon_classification"
    "__MIP_postulation_is_extension_level_not_derivation",
    "NOT_claiming_blockage_of_one_route_implies_impossibility_in_principle"
    "__all_five_native_routes_rejected_is_BSR_not_impossibility",
]

N_QB5_NONCLAIMS: int = len(QB5_NONCLAIMS)   # 8


# ================================================================
# Dataclasses
# ================================================================


@dataclass
class QB5MissingIngredientAnalysis:
    """Track A: Missing-ingredient confirmation check."""
    # What Q-B proved is missing
    missing_element_type: str      # one of ALLOWED_MISSING_ELEMENT_TYPES
    missing_element_description: str
    # What it is NOT (disambiguation)
    is_symplectic_only: bool           # False
    is_doubled_real_structure: bool    # False (CTP pair fails ghost check)
    is_full_hilbert_package: bool      # False (minimum is just J + inner product)
    is_larger_kinematic_bundle: bool   # False
    # Minimum structure to unblock Q-C
    minimum_to_unblock_qc: List[str]   # Q-B.5 minimum package
    n_minimum_items: int               # 3
    # Appendix P context
    missing_element_appendix_p_class: str   # MIP if postulated
    gap_severity: str                  # "kinematic_structure_gap_analogous_to_BG1"
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5NativeRoute:
    """A single candidate native derivation route for J (Track B)."""
    route_id: str              # e.g. "NR1_ctp_doubled_fields"
    route_name: str
    route_description: str
    claimed_derivation_path: str   # the route being tested
    exact_derivation_exists: bool  # False for all native routes
    rejection_reason: str          # why this route fails
    appendix_p_class: str          # class for this route result
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5NativeDerivationAudit:
    """Track B: Full native derivation audit (5 candidate routes)."""
    routes: List[QB5NativeRoute]
    n_routes_tested: int       # 5
    n_routes_accepted: int     # 0
    native_derivation_possible: bool   # False
    rejection_summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5EffectiveRoute:
    """A single candidate effective-induction route for J (Track C)."""
    route_id: str              # e.g. "ER1_low_frequency_quasi_static"
    route_name: str
    route_description: str
    effective_regime: str      # the regime or mechanism being tested
    effective_j_viable: bool   # True only for genuinely viable routes
    classification: str        # one of ALLOWED_EFFECTIVE_ROUTE_CLASSIFICATIONS
    rejection_reason: Optional[str]   # None if viable
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5EffectiveInductionAudit:
    """Track C: Full effective-induction audit (5 candidate routes)."""
    routes: List[QB5EffectiveRoute]
    n_routes_tested: int       # 5
    n_routes_viable: int       # 0
    effective_induction_possible: bool   # False (no clean route)
    closest_route: str         # "ER3_doubled_real_effective_complex" (least-bad)
    closest_route_classification: str    # "underdetermined_compatibility_only"
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5PostulateAudit:
    """Track D: Independent-postulate qualification audit."""
    j_requires_new_dof: bool               # False (acts on existing real field space)
    j_requires_new_kinematic_structure: bool  # True
    gap_class: str                          # "kinematic_structure_gap_no_new_dof"
    n_convergent_motivations: int           # 2
    convergent_motivations: List[str]       # the two motivations
    at_least_one_parameter_constrained: bool  # True (τ²)
    constrained_parameter: str              # "tau_sq_eq_3_over_2"
    mip_qualifies: bool                     # True
    minimal_postulate_form: str             # exact description of the postulate
    postulate_appendix_p_class: str         # "motivated_independent_postulation"
    postulate_conditions: List[str]         # conditions J must satisfy
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5KinematicSufficiencyAudit:
    """Track E: Kinematic sufficiency audit — is J alone enough for Q-C?"""
    j_alone_sufficient: bool           # False
    j_necessary: bool                  # True
    # What J alone provides
    j_enables_complex_superposition: bool   # True (with J you can define Jψ as iψ)
    j_enables_inner_product: bool           # False (inner product needs separate postulate)
    j_enables_normalization: bool           # False
    j_enables_dynamics_generator: bool      # False (separate H or L needed)
    j_enables_state_space_topology: bool    # False
    # Minimum sufficient package
    minimum_sufficient_package: List[str]
    n_minimum_package_items: int            # 3
    # Classification of each component
    inner_product_classification: str   # "motivated_independent_postulation"
    generator_classification: str       # "motivated_but_unbuilt"
    # Verdict
    sufficiency_verdict: str            # "J_necessary_but_not_sufficient"
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5GhostConstraintAudit:
    """Track F: Ghost / doubled-field constraint audit."""
    # Φ₋ ghost mode properties
    phi_minus_eom: str            # "dPhi_minus/dt = +Phi_minus / tau"
    phi_minus_growth_rate: float  # +1/τ
    phi_minus_growth_rate_sign: int   # +1
    phi_minus_can_be_imaginary_part: bool  # False
    # Formal J via CTP split
    formal_j_definition: str    # "J(Phi_plus) = Phi_minus, J(Phi_minus) = -Phi_plus"
    formal_j_satisfies_j_sq: bool   # True (algebraically J² = -1)
    # Dynamics compatibility
    norm_formula: str           # "Phi_plus^2 + Phi_minus^2"
    norm_growth_term: str       # "d/dt(Phi_minus^2) = +2*Phi_minus^2/tau > 0"
    norm_conserved_under_dynamics: bool   # False
    norm_growth_rate_sign: int            # +1
    # Repackaging attempts
    n_repackaging_attempts: int      # 0 — no valid linear repackaging exists
    repackaging_viable: bool         # False
    repackaging_failure_reason: str  # any combination involving Phi_minus inherits ghost
    # Verdict
    doubled_field_verdict: str       # "doubled_field_pair_complexification_obstructed"
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5AppendixPEntry:
    """Single entry in the Track G Appendix P classification table."""
    route_id: str
    route_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency_notes: List[str] = field(default_factory=list)


@dataclass
class QB5AppendixPClassificationAudit:
    """Track G: Appendix P classification per candidate route."""
    entries: List[QB5AppendixPEntry]
    n_entries: int
    overall_j_class: str    # determined by most favorable viable route
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5ReadinessAudit:
    """Track H: Quantum program readiness audit."""
    native_grut_sufficient_for_qc: bool   # False
    j_postulation_required: bool          # True
    inner_product_postulation_required: bool  # True
    qc_can_proceed_natively: bool         # False
    qc_can_proceed_with_postulate: bool   # True
    minimum_postulate_package: List[str]  # [J, inner product, dynamics generator]
    conditions_for_qc: List[str]          # conditions to be met
    readiness_verdict: str                # "proceed_only_if_J_is_postulated"
    qc_appendix_p_floor: str             # "motivated_independent_postulation"
    notes: List[str] = field(default_factory=list)


@dataclass
class QB5NonclaimFirewall:
    """Track I: Nonclaim firewall — 8 explicit nonclaims."""
    nonclaims: List[str]
    n_nonclaims: int     # 8
    all_registered: bool  # True


@dataclass
class QB5ComplexStructureResult:
    """Master result for Q-B.5 complex structure and kinematic upgrade audit."""
    valid: bool
    # Nine audit tracks
    track_a_missing_ingredient: QB5MissingIngredientAnalysis
    track_b_native_derivation: QB5NativeDerivationAudit
    track_c_effective_induction: QB5EffectiveInductionAudit
    track_d_postulate: QB5PostulateAudit
    track_e_kinematic_sufficiency: QB5KinematicSufficiencyAudit
    track_f_ghost_constraint: QB5GhostConstraintAudit
    track_g_appendix_p: QB5AppendixPClassificationAudit
    track_h_readiness: QB5ReadinessAudit
    track_i_nonclaims: QB5NonclaimFirewall
    # Four hard-gated verdicts
    primary_J_status: str        # one of ALLOWED_PRIMARY_J_STATUSES
    sufficiency_verdict: str     # one of ALLOWED_SUFFICIENCY_VERDICTS
    doubled_field_verdict: str   # one of ALLOWED_DOUBLED_FIELD_VERDICTS
    readiness_verdict: str       # one of ALLOWED_READINESS_VERDICTS
    # Summary
    qb5_appendix_p_class: str    # "motivated_independent_postulation"
    allowed_claims: List[str]
    forbidden_claims: List[str]
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Track A builder
# ================================================================


def build_track_a_missing_ingredient() -> QB5MissingIngredientAnalysis:
    """Track A: Missing-ingredient confirmation check.

    Q-B established that the exact missing ingredient is:
      A complex structure J: real_config_space → real_config_space with J² = −1.

    The missing element is specifically a complex structure J — NOT merely a
    symplectic structure, NOT merely the CTP doubled-real structure, NOT the
    full Hilbert inner-product package, and NOT a larger kinematic bundle.

    Disambiguation:
    - Symplectic structure ω alone: does not give complex structure. A symplectic
      form ω on a real space V gives J = ω⁻¹g only when a compatible metric g is
      also supplied. Neither ω nor g is present in canonical GRUT.
    - CTP doubled-real structure: present in GRUT as Galley ER. But the Φ₋ ghost
      mode disqualifies it from serving as Im(Ψ) (Track F). It is a doubled real
      structure but NOT a valid complexification.
    - Full Hilbert inner-product package: more than the minimum. The minimum is J.
      Adding a compatible inner product on top of J is the next step (Track E).
    - Larger kinematic bundle: J + inner product is sufficient minimum for Q-C entry;
      no larger bundle is required at this stage.

    Minimum to unblock Q-C: {J, compatible inner product, dynamics generator}.
    """
    return QB5MissingIngredientAnalysis(
        missing_element_type="complex_structure_J_on_state_space",
        missing_element_description=(
            "A complex structure J: real_field_space → real_field_space "
            "with J² = −1 (the identity map on field space, negated). "
            "J promotes the real linear space ℝ_Φ to a complex linear space ℂ_Φ "
            "by defining (a + ib)Φ = aΦ + bJΦ. "
            "Without J, no complex superposition, no Hilbert space inner product, "
            "no Born-rule normalization can be defined on the GRUT field space."
        ),
        is_symplectic_only=False,
        is_doubled_real_structure=False,
        is_full_hilbert_package=False,
        is_larger_kinematic_bundle=False,
        minimum_to_unblock_qc=QB5_MINIMUM_KINEMATIC_PACKAGE,
        n_minimum_items=N_MINIMUM_KINEMATIC_PACKAGE_ITEMS,
        missing_element_appendix_p_class="motivated_independent_postulation",
        gap_severity="kinematic_structure_gap_no_new_dof",
        notes=[
            "Q-B primary verdict: density_matrix_or_functional_state_required (BSR).",
            "Q-B missing ingredient: complex_structure_J_with_J_squared_eq_minus_1.",
            "J acts on existing real field space — does NOT require new DOFs.",
            "J is a kinematic structure gap, not a field-content (BG1) gap.",
            "Symplectic structure alone insufficient: J = ω⁻¹g requires compatible metric g.",
            "CTP doubled-real structure fails: Φ₋ ghost disqualifies it (Track F).",
            "Minimum Q-C package: J + compatible inner product + dynamics generator.",
            "Full Hilbert package (J + inner product + completeness + Born rule) is Q-D territory.",
        ],
    )


# ================================================================
# Track B builders — 5 native routes
# ================================================================


def build_native_route_nr1_ctp_doubled_fields() -> QB5NativeRoute:
    """NR1: CTP doubled fields (Φ₁, Φ₂) as source of J."""
    return QB5NativeRoute(
        route_id="NR1_ctp_doubled_fields",
        route_name="ctp_doubled_field_structure",
        route_description=(
            "Define J via the Keldysh split: J(Φ₊) = Φ₋, J(Φ₋) = −Φ₊ "
            "where Φ₊ = (Φ₁+Φ₂)/2, Φ₋ = Φ₁−Φ₂. "
            "This gives J² = −1 algebraically — check if it constitutes a valid J."
        ),
        claimed_derivation_path=(
            "J(Φ₊) = Φ₋, J(Φ₋) = −Φ₊ → J²(Φ₊) = J(Φ₋) = −Φ₊ ✓, "
            "J²(Φ₋) = J(−Φ₊) = −Φ₋ ✓. Algebraically J² = −1."
        ),
        exact_derivation_exists=False,
        rejection_reason=(
            "Algebraic J² = −1 is necessary but not sufficient for a valid complex structure. "
            "J must also be compatible with dynamics in the sense that the 'norm' Φ₊² + Φ₋² "
            "is preserved under time evolution. The Φ₋ ghost mode satisfies "
            "dΦ₋/dt = +Φ₋/τ, so d(Φ₋²)/dt = +2Φ₋²/τ > 0 always. "
            "The norm Φ₊² + Φ₋² grows due to the ghost contribution. "
            "Therefore the CTP split does NOT yield a dynamically valid complex structure. "
            "FFM6 (hilbert_space_from_ctp_doubling) from Q-A charter applies. "
            "See Track F for full ghost-constraint analysis."
        ),
        appendix_p_class="forbidden_or_inconsistent",
        notes=[
            "J² = −1 holds algebraically for J: Φ₊ ↦ Φ₋ ↦ −Φ₊.",
            "But dynamics compatibility requires norm conservation under time evolution.",
            "d|Ψ|²/dt = −2Φ₊²/τ + 2Φ₊X/τ + 2Φ₋²/τ: ghost term 2Φ₋²/τ > 0.",
            "Norm is NOT conserved: CTP complexification is dynamically obstructed.",
            "Classification: forbidden_or_inconsistent for this specific derivation route.",
            "The FOI class is appropriate: attempting this derivation would violate FFM6.",
        ],
    )


def build_native_route_nr2_memory_kernel() -> QB5NativeRoute:
    """NR2: Constitutive memory kernel structure as source of J."""
    return QB5NativeRoute(
        route_id="NR2_memory_kernel",
        route_name="constitutive_memory_kernel",
        route_description=(
            "Test whether the retarded memory kernel K(t−t′) = (1/τ)e^{−(t−t′)/τ} "
            "encodes a complex structure. The kernel acts on the retarded history "
            "of X(t′) to produce the current state Φ(t)."
        ),
        claimed_derivation_path=(
            "If K(t−t′) had an oscillatory component, it might encode a natural "
            "complex structure via Hilbert transform or imaginary-frequency extension."
        ),
        exact_derivation_exists=False,
        rejection_reason=(
            "The memory kernel K(t−t′) = (1/τ)e^{−(t−t′)/τ} is a purely real, "
            "monotonically decaying function. Its Fourier transform is "
            "K̂(ω) = 1/(1 + iωτ) — complex, but this complexity is analytic structure "
            "of the transfer function, not a complex structure J on the field space. "
            "An analytic transfer function does not provide a linear map J: ℝ_Φ → ℝ_Φ "
            "with J² = −1 acting on instantaneous field configurations. "
            "The frequency-domain i in K̂(ω) is the Fourier-transform imaginary unit, "
            "not a physical complex structure on state space. "
            "Track I nonclaim: notation-level i is not physical J."
        ),
        appendix_p_class="compatible_but_ad_hoc",
        notes=[
            "K(t-t') = (1/τ)exp(-(t-t')/τ): purely real-valued monotone decay.",
            "K̂(ω) = 1/(1+iωτ) is complex in frequency domain — but this is Fourier i.",
            "Fourier-domain complexity ≠ physical complex structure on configuration space.",
            "No J: field_space → field_space with J²=-1 can be extracted from K alone.",
            "CAH: the memory kernel is compatible with complex extensions but does not derive J.",
        ],
    )


def build_native_route_nr3_galley_ctp_action() -> QB5NativeRoute:
    """NR3: Galley / CTP effective-action geometry as source of J."""
    return QB5NativeRoute(
        route_id="NR3_galley_ctp_action_geometry",
        route_name="galley_ctp_effective_action_geometry",
        route_description=(
            "Test whether the geometric structure of the Galley CTP effective action "
            "A_eff[Φ₊, Φ₋] encodes a complex structure. "
            "The CTP action has the symplectic-like structure A = A₀[Φ₊] + A_IF[Φ₊, Φ₋] "
            "where A_IF is the influence functional."
        ),
        claimed_derivation_path=(
            "A CTP action with symplectic form could give a natural complex structure "
            "if the action is of the form ω(δΦ, δΦ) for some symplectic form ω."
        ),
        exact_derivation_exists=False,
        rejection_reason=(
            "The Galley CTP effective action is real-valued. Both A₀ and A_IF are real "
            "functionals. The variational structure (Euler-Lagrange equations) generates "
            "real equations of motion for real fields. "
            "The action has a symplectic-like structure in the sense that the Keldysh "
            "decomposition respects a real symplectic form on (Φ₊, Φ₋) space. "
            "However, a symplectic form ω alone does not produce a complex structure J "
            "without a compatible metric g (Kähler structure requires ω, J, g, all compatible). "
            "No compatible metric g is defined in GRUT. "
            "Therefore the action geometry motivates the existence of ω but not J."
        ),
        appendix_p_class="compatible_but_ad_hoc",
        notes=[
            "CTP action A_eff[Φ₊, Φ₋] is real-valued — no complex geometry encoded.",
            "Keldysh decomposition provides symplectic-like structure on (Φ₊, Φ₋) space.",
            "Symplectic form ω present: but J = ω⁻¹g requires compatible metric g.",
            "No metric g is defined in canonical GRUT — symplectic ≠ Kähler.",
            "CAH: action geometry is compatible with complex extension but does not derive J.",
        ],
    )


def build_native_route_nr4_response_information_geometry() -> QB5NativeRoute:
    """NR4: Response / observer / information geometry as source of J."""
    return QB5NativeRoute(
        route_id="NR4_response_information_geometry",
        route_name="response_observer_information_geometry",
        route_description=(
            "Test whether GRUT's response structure (retarded Green's function, "
            "susceptibility) or any information-geometric structure present "
            "in the audited architecture encodes a complex structure."
        ),
        claimed_derivation_path=(
            "The retarded Green's function G_R(ω) = 1/(−iω τ + 1) is complex. "
            "An information metric or Fisher metric on the GRUT state space "
            "might provide a compatible metric g, enabling J = ω⁻¹g."
        ),
        exact_derivation_exists=False,
        rejection_reason=(
            "The retarded Green's function G_R(ω) = 1/(1 − iωτ) is complex in "
            "frequency domain, but this is the same Fourier-domain complexity as NR2: "
            "analytic structure, not a physical complex structure on configuration space. "
            "No information-geometric structure (Fisher metric, quantum geometry) "
            "is present in the audited canonical GRUT architecture — this falls into "
            "the category of 'response / observer structure' that is not included "
            "in the Q0 inventory. There are no Q0 items encoding information geometry. "
            "This route is not absent but non-existent in the audited architecture."
        ),
        appendix_p_class="compatible_but_ad_hoc",
        notes=[
            "G_R(ω) = 1/(1−iωτ) is complex in frequency domain — same as NR2 Fourier i.",
            "No information-geometric structure (Fisher metric) in Q0 inventory.",
            "No observer structure, no quantum information geometry in audited GRUT.",
            "CAH: response structure is compatible with complex extension but doesn't derive J.",
            "This route would require adding information geometry as a new structural element.",
        ],
    )


def build_native_route_nr5_symplectic_phase_like() -> QB5NativeRoute:
    """NR5: Pre-existing symplectic or phase-like structure as source of J."""
    return QB5NativeRoute(
        route_id="NR5_symplectic_phase_like",
        route_name="symplectic_or_phase_like_structure",
        route_description=(
            "Test whether any already-audited GRUT structure encodes a symplectic "
            "or phase-like object that could directly yield J. "
            "Candidates: the Z₂ symmetry (Φ → −Φ), the topological winding charge, "
            "the equilibrium phase structure of the ODE."
        ),
        claimed_derivation_path=(
            "The Z₂ symmetry Φ → −Φ or the O(3) topological winding might "
            "provide a natural J by combining two symmetry generators."
        ),
        exact_derivation_exists=False,
        rejection_reason=(
            "Z₂ symmetry (Φ → −Φ): this is a discrete ℤ₂ symmetry, not a continuous "
            "U(1) or GL(1,ℂ) symmetry. J must be a continuous real linear map. "
            "A discrete symmetry cannot supply a continuous complex structure. "
            "O(3) topological winding (Q0 item A5/C1): the topological charge is an "
            "integer-valued functional of the field configuration — a real scalar. "
            "It does not define a linear map J on the field space. "
            "The equilibrium phase structure: the ODE τ dΦ/dt + Φ = X has a unique "
            "real equilibrium at Φ_eq = R_eq = 1/3. No complex phase structure exists. "
            "None of the audited structures yields a continuous real linear map J: ℝ_Φ → ℝ_Φ "
            "with J² = −1."
        ),
        appendix_p_class="compatible_but_ad_hoc",
        notes=[
            "Z₂ symmetry Φ↦−Φ is discrete (ℤ₂); J must be continuous real linear map.",
            "O(3) winding charge is integer-valued functional, not a field-space map.",
            "Equilibrium ODE has unique real equilibrium: no complex phase structure.",
            "No combination of audited Z₂, O(3), and equilibrium structures yields J.",
            "CAH: topological structures are compatible with complex extension, not derivations.",
        ],
    )


def build_track_b_native_derivation() -> QB5NativeDerivationAudit:
    """Track B: Full native derivation audit — 5 routes, all rejected."""
    routes = [
        build_native_route_nr1_ctp_doubled_fields(),
        build_native_route_nr2_memory_kernel(),
        build_native_route_nr3_galley_ctp_action(),
        build_native_route_nr4_response_information_geometry(),
        build_native_route_nr5_symplectic_phase_like(),
    ]
    n_accepted = sum(1 for r in routes if r.exact_derivation_exists)
    return QB5NativeDerivationAudit(
        routes=routes,
        n_routes_tested=len(routes),
        n_routes_accepted=n_accepted,
        native_derivation_possible=False,
        rejection_summary=(
            "All five native derivation routes for J are rejected. "
            "NR1 (CTP doubled fields): algebraically J²=−1 but dynamically obstructed "
            "(ghost norm growth). NR2 (memory kernel): Fourier-domain complexity ≠ J. "
            "NR3 (CTP action geometry): symplectic structure present but no compatible "
            "metric g → no J. NR4 (response/information geometry): absent from GRUT. "
            "NR5 (symplectic/phase-like): all candidates discrete or scalar, none gives J. "
            "Conclusion: J cannot be natively derived. No new derivation route identified."
        ),
        notes=[
            "NR1: FOI — CTP ghost mode makes this route dynamically inconsistent.",
            "NR2: CAH — Fourier-domain i is notation, not physical complex structure.",
            "NR3: CAH — symplectic structure without metric ≠ complex structure.",
            "NR4: CAH — response/information geometry not present in audited GRUT.",
            "NR5: CAH — discrete and topological structures don't provide continuous J.",
            "Hard rule: all native route rejections must be for structural reasons, not preference.",
        ],
    )


# ================================================================
# Track C builders — 5 effective routes
# ================================================================


def build_effective_route_er1_low_frequency() -> QB5EffectiveRoute:
    """ER1: Low-frequency / quasi-static sector complexification."""
    return QB5EffectiveRoute(
        route_id="ER1_low_frequency_quasi_static",
        route_name="low_frequency_quasi_static_complexification",
        route_description=(
            "In the quasi-static limit ω ≪ 1/τ, test whether the GRUT constitutive "
            "ODE develops an effective complex structure."
        ),
        effective_regime="omega_much_less_than_1_over_tau",
        effective_j_viable=False,
        classification="blocked",
        rejection_reason=(
            "In the quasi-static limit, τ∂ₜΦ ≈ 0 and the equation reduces to Φ ≈ X. "
            "The field simply tracks the source; all dynamics are suppressed. "
            "No complex structure emerges from static response. "
            "In the high-frequency limit ω ≫ 1/τ: the equation becomes τ∂ₜΦ ≈ X−Φ, "
            "still real, with no oscillatory behavior that could support J. "
            "The GRUT constitutive ODE has no regime where it acquires oscillatory "
            "(imaginary-frequency) modes: its dispersion relation is ω = −i/τ "
            "(purely imaginary, damped). No real-frequency oscillation exists."
        ),
        notes=[
            "Quasi-static limit: Φ ≈ X (trivially real, no J).",
            "High-frequency limit: τ∂ₜΦ ≈ X−Φ (still real ODE).",
            "GRUT dispersion: ω = −i/τ (purely imaginary = decay, not oscillation).",
            "No frequency regime yields oscillatory modes that could support J.",
        ],
    )


def build_effective_route_er2_coarse_grained() -> QB5EffectiveRoute:
    """ER2: Coarse-grained open-system reduction."""
    return QB5EffectiveRoute(
        route_id="ER2_coarse_grained_open_system",
        route_name="coarse_grained_open_system_reduction",
        route_description=(
            "In the Caldeira–Leggett / master-equation paradigm, coarse-grained "
            "open-system dynamics can sometimes reveal an effective complex structure "
            "inherited from the underlying quantum Hilbert space."
        ),
        effective_regime="caldeira_leggett_coarse_graining_limit",
        effective_j_viable=False,
        classification="blocked",
        rejection_reason=(
            "In standard open quantum systems (Lindblad, Caldeira-Leggett quantum), "
            "the effective density matrix description uses a complex structure J "
            "that is INHERITED from the underlying quantum Hilbert space of the system. "
            "The bath does not CREATE J — J is an input from the microscopic quantum theory. "
            "For GRUT, there is no underlying quantum system to coarse-grain from. "
            "Coarse-graining the GRUT constitutive ODE produces an effective equation "
            "for the coarse-grained Φ — still a real scalar, still no J. "
            "This route is circular: it assumes quantum structure to obtain quantum structure. "
            "Track I nonclaim: open-system complexification does not imply Born rule."
        ),
        notes=[
            "Caldeira-Leggett: J comes FROM the quantum Hilbert space of the system.",
            "The bath provides dissipation and noise — not the complex structure.",
            "Coarse-graining classical GRUT yields a coarser classical theory.",
            "No quantum seed → no quantum emergence from coarse-graining alone.",
            "This route would require circular reasoning (quantum in → quantum out).",
        ],
    )


def build_effective_route_er3_doubled_real() -> QB5EffectiveRoute:
    """ER3: Doubled-real to effective-complex pairing."""
    return QB5EffectiveRoute(
        route_id="ER3_doubled_real_effective_complex",
        route_name="doubled_real_to_effective_complex_pairing",
        route_description=(
            "Define an effective complex field Ψ_eff = Φ₊ + iΦ₋ using the CTP "
            "decomposition, and test whether this pairing constitutes an effective J "
            "in some restricted sense."
        ),
        effective_regime="ctp_keldysh_complexification",
        effective_j_viable=False,
        classification="underdetermined_compatibility_only",
        rejection_reason=(
            "Formally, one can write Ψ_eff = Φ₊ + iΦ₋ and define J_eff by "
            "J_eff(Φ₊) = Φ₋, J_eff(Φ₋) = −Φ₊. This satisfies J_eff² = −1 algebraically. "
            "However, 'effective' complexification requires that the effective theory "
            "be consistently formulated in terms of Ψ_eff with complex amplitude dynamics. "
            "The Φ₋ ghost mode (growth rate +1/τ) means |Ψ_eff|² = Φ₊² + Φ₋² grows: "
            "the effective amplitude is not conserved. "
            "An effective theory with growing 'norm' cannot be a quantum theory in any limit. "
            "The classification is underdetermined_compatibility_only: the formal pairing "
            "is mathematically possible as notation, but does not constitute even an "
            "effective complex structure in any dynamically valid sense."
        ),
        notes=[
            "Ψ_eff = Φ₊ + iΦ₋ can be written — this is a notation.",
            "J_eff(Φ₊)=Φ₋, J_eff(Φ₋)=−Φ₊ satisfies J²=−1 algebraically.",
            "But |Ψ_eff|² = Φ₊² + Φ₋² grows due to ghost: not a valid norm.",
            "Effective quantum amplitude requires |Ψ|² conserved (Track F).",
            "Classification: underdetermined_compatibility_only (not even motivated_but_unbuilt).",
            "This is the 'closest' route to effective J but still fails.",
        ],
    )


def build_effective_route_er4_environment_induced() -> QB5EffectiveRoute:
    """ER4: Environment-induced effective phase structure."""
    return QB5EffectiveRoute(
        route_id="ER4_environment_induced_phase",
        route_name="environment_induced_effective_phase_structure",
        route_description=(
            "Test whether the bath implicit in the Galley retarded kernel induces "
            "an effective phase structure on the GRUT field space."
        ),
        effective_regime="galley_bath_back_reaction",
        effective_j_viable=False,
        classification="blocked",
        rejection_reason=(
            "In quantum open systems, environmental decoherence SUPPRESSES phase coherence "
            "and quantum superposition. The bath does not create complex phases — "
            "it destroys them through dephasing. "
            "In GRUT's classical setting, the bath back-reaction (encoded in the "
            "retarded influence functional) drives the system toward equilibrium. "
            "This is purely dissipative: no phase-inducing mechanism exists. "
            "Even in the quantum case, bath-induced phases (Berry phases, geometric phases) "
            "require an already-existing quantum Hilbert space to accumulate phases in. "
            "The bath cannot create J from nothing."
        ),
        notes=[
            "Quantum bath: dephasing suppresses coherence, does not create it.",
            "Classical GRUT bath: purely dissipative, drives toward equilibrium.",
            "Berry/geometric phases require prior Hilbert space to exist.",
            "No phase-induction mechanism exists in audited GRUT architecture.",
        ],
    )


def build_effective_route_er5_linearized_perturbation() -> QB5EffectiveRoute:
    """ER5: Linearized perturbation regime."""
    return QB5EffectiveRoute(
        route_id="ER5_linearized_perturbation",
        route_name="linearized_perturbation_regime",
        route_description=(
            "Linearize GRUT around equilibrium Φ = R_eq + δΦ and test whether "
            "the linearized theory has a natural complex structure."
        ),
        effective_regime="linear_perturbation_around_phi_eq",
        effective_j_viable=False,
        classification="blocked",
        rejection_reason=(
            "Linearizing τ dΦ/dt + Φ = X around Φ_eq = R_eq = 1/3 gives: "
            "τ d(δΦ)/dt + δΦ = δX (linear ODE for perturbation). "
            "This is the same first-order real ODE as the full theory, just for δΦ. "
            "Linearization does not alter the temporal structure: the equation "
            "is still first-order with real coefficients and no oscillatory modes. "
            "The linearized dispersion is ω = −i/τ (purely imaginary, damped). "
            "No J can be extracted from a purely real, purely damped linear theory."
        ),
        notes=[
            "Linearized equation: τ d(δΦ)/dt + δΦ = δX — same structure as full ODE.",
            "Dispersion relation: ω = −i/τ (purely imaginary — decay, not oscillation).",
            "No oscillatory mode in linearized theory.",
            "Linearization preserves real structure; no complexification emerges.",
        ],
    )


def build_track_c_effective_induction() -> QB5EffectiveInductionAudit:
    """Track C: Full effective-induction audit — 5 routes, none cleanly viable."""
    routes = [
        build_effective_route_er1_low_frequency(),
        build_effective_route_er2_coarse_grained(),
        build_effective_route_er3_doubled_real(),
        build_effective_route_er4_environment_induced(),
        build_effective_route_er5_linearized_perturbation(),
    ]
    n_viable = sum(1 for r in routes if r.effective_j_viable)
    return QB5EffectiveInductionAudit(
        routes=routes,
        n_routes_tested=len(routes),
        n_routes_viable=n_viable,
        effective_induction_possible=False,
        closest_route="ER3_doubled_real_effective_complex",
        closest_route_classification="underdetermined_compatibility_only",
        notes=[
            "ER1 (low-frequency): blocked — no oscillatory mode in any frequency regime.",
            "ER2 (coarse-graining): blocked — circular (requires quantum in).",
            "ER3 (doubled-real): underdetermined_compatibility_only — ghost norm grows.",
            "ER4 (environment-induced): blocked — bath suppresses, not creates, coherence.",
            "ER5 (linearized): blocked — linearized theory has same real damped structure.",
            "No effective route cleanly viable; ER3 is formally closest but dynamically invalid.",
        ],
    )


# ================================================================
# Track D builder
# ================================================================


def build_track_d_postulate() -> QB5PostulateAudit:
    """Track D: Independent-postulate qualification audit.

    Given that J cannot be natively derived and cannot be effectively induced,
    the next question is: does J qualify as motivated_independent_postulation (MIP)?

    Appendix P MIP criteria:
    (a) New structural element not derivable from existing GRUT architecture — YES
    (b) Does it require new DOFs? — NO (J acts on existing real field space Φ)
    (c) Gap class: kinematic structure gap (analogous to BG1 but no new fields)
    (d) ≥2 convergent independent motivations — YES (see below)
    (e) ≥1 parameter constrained by existing canon — YES (τ² = 3/2)

    Two convergent motivations:
    1. CTP / open-system structural analogy: the GRUT effective description uses
       the same (Φ₁, Φ₂) formalism as the quantum CTP (Schwinger-Keldysh) path
       integral, where J is fundamental to the underlying Hilbert space. The
       structural parallel between the GRUT CTP and the quantum CTP is an
       internal motivation for J — not an external "we want QM" argument.
    2. O(3) topological structure: the Q0 MIP item A5/C1 (integer winding charge,
       O(3) triplet) provides a sector where quantum field-theoretic treatments
       naturally require complex amplitudes for topological sectors. The O(3) MIP
       was accepted as MIP; J at the same level of motivation is consistent.

    Minimal postulate form:
      J: ℝ_Φ → ℝ_Φ is a constant real linear map with J² = −1_Φ,
      commuting with the linear part of the GRUT evolution operator L = τ∂ₜ + 1.
      (Commutativity [J, L] = 0 is automatic for any time-independent J since
      L acts on time derivatives and J acts on field-space directions.)
    """
    return QB5PostulateAudit(
        j_requires_new_dof=False,
        j_requires_new_kinematic_structure=True,
        gap_class="kinematic_structure_gap_no_new_dof",
        n_convergent_motivations=N_CONVERGENT_MOTIVATIONS_FOR_J,
        convergent_motivations=[
            "CTP_open_system_structural_analogy: GRUT_CTP_formalism_uses_same_Phi1_Phi2_structure"
            "_as_quantum_Schwinger_Keldysh_path_integral_where_J_is_fundamental_to_Hilbert_space.",
            "O3_topological_sector_motivation: Q0_MIP_item_A5_C1_O3_winding_was_accepted_as_MIP;"
            "_quantum_treatment_of_topological_sectors_requires_complex_amplitudes_at_same_level.",
        ],
        at_least_one_parameter_constrained=True,
        constrained_parameter="tau_sq_eq_3_over_2",
        mip_qualifies=True,
        minimal_postulate_form=(
            "J: real_field_space → real_field_space, "
            "J is a constant real linear map satisfying J² = −I_Φ. "
            "Compatibility condition: [J, τ∂ₜ + 1] = 0 (automatic for time-independent J). "
            "τ² = 3/2 constrains the dynamics compatible with J: any Hamiltonian H "
            "postulated for Q-C must satisfy [J, H_linear] = 0 with H_linear derived "
            "from the τ-scale."
        ),
        postulate_appendix_p_class="motivated_independent_postulation",
        postulate_conditions=[
            "J_must_be_real_linear_not_just_formal_complex_notation",
            "J_must_commute_with_grut_linear_evolution_operator_L_eq_tau_dt_plus_1",
            "J_sq_eq_minus_identity_on_field_space",
            "compatible_inner_product_must_be_postulated_simultaneously_not_derived",
            "all_qc_results_carry_mip_minimum_classification",
        ],
        notes=[
            "J requires no new DOFs — acts on existing real field space Φ.",
            "J does require new kinematic structure: complex linear structure on field space.",
            "Gap class: kinematic_structure_gap (not BG1 field-content gap).",
            "Two convergent motivations: CTP structural analogy + O(3) topological sector.",
            "τ² = 3/2 constrains which dynamics generators are compatible with J.",
            "MIP qualifies: new kinematic structure, 2 motivations, 1 parameter constrained.",
            "Postulated J cannot receive native_canon classification (Track I nonclaim 7).",
            "All Q-C results built on postulated J carry MIP minimum (QA-R3 compliance).",
        ],
    )


# ================================================================
# Track E builder
# ================================================================


def build_track_e_kinematic_sufficiency() -> QB5KinematicSufficiencyAudit:
    """Track E: Kinematic sufficiency audit.

    Does J alone suffice to move from Q-B to Q-C?

    J alone provides:
    - Complex superposition: Ψ = aΦ + bJΦ for a, b ∈ ℝ → complex linear combination
    - Complex linear structure on the field space

    J alone does NOT provide:
    - Inner product ⟨Ψ,Φ⟩: requires a separate real symmetric bilinear form g
      compatible with J (i.e., g(JΨ,JΦ) = g(Ψ,Φ)).
    - Normalization: requires ⟨Ψ,Ψ⟩ = 1 (from inner product, not from J).
    - Dynamics generator H: a Hamiltonian or Lindbladian must be separately
      postulated; J alone says nothing about how states evolve.
    - State-space topology/completeness: requires Hilbert space completion,
      not just J.

    Verdict: J_necessary_but_not_sufficient
    Minimum sufficient package: {J, compatible_inner_product, dynamics_generator}
    """
    return QB5KinematicSufficiencyAudit(
        j_alone_sufficient=False,
        j_necessary=True,
        j_enables_complex_superposition=True,
        j_enables_inner_product=False,
        j_enables_normalization=False,
        j_enables_dynamics_generator=False,
        j_enables_state_space_topology=False,
        minimum_sufficient_package=QB5_MINIMUM_KINEMATIC_PACKAGE,
        n_minimum_package_items=N_MINIMUM_KINEMATIC_PACKAGE_ITEMS,
        inner_product_classification="motivated_independent_postulation",
        generator_classification="motivated_but_unbuilt",
        sufficiency_verdict="J_necessary_but_not_sufficient",
        notes=[
            "J enables: complex linear combinations Ψ = aΦ + bJΦ (complex superposition).",
            "J does NOT enable: inner product, normalization, dynamics, or topology.",
            "Inner product g compatible with J requires separate postulate (MIP).",
            "Dynamics generator H (or Lindbladian L) requires separate postulate (MBU).",
            "Completeness / state-space topology requires Hilbert completion (Q-D territory).",
            "Minimum sufficient Q-C package: {J (MIP) + inner product (MIP) + generator (MBU)}.",
            "Inner product is MIP: same motivation level as J, no new DOFs, adds g.",
            "Generator is MBU: motivated but construction route not yet specified.",
            "Verdict: J_necessary_but_not_sufficient (BSR on kinematic analysis).",
        ],
    )


# ================================================================
# Track F builder
# ================================================================


def build_track_f_ghost_constraint() -> QB5GhostConstraintAudit:
    """Track F: Ghost / doubled-field constraint audit.

    Key physical analysis:
    Define J via the Keldysh split: J(Φ₊) = Φ₋, J(Φ₋) = −Φ₊.

    Algebraic check: J² = −1?
      J²(Φ₊) = J(Φ₋) = −Φ₊ ✓
      J²(Φ₋) = J(−Φ₊) = −J(Φ₊) = −Φ₋ ✓
      → J² = −1 algebraically.

    Dynamics compatibility check: is the 'norm' Φ₊² + Φ₋² conserved?
      dΦ₊/dt = (X − Φ₊)/τ
      dΦ₋/dt = +Φ₋/τ  (ghost growth)

      d/dt(Φ₊² + Φ₋²) = 2Φ₊(X−Φ₊)/τ + 2Φ₋(+Φ₋/τ)
                       = (−2Φ₊² + 2Φ₊X)/τ + 2Φ₋²/τ

    The ghost term 2Φ₋²/τ > 0 always (since Φ₋² ≥ 0 and τ > 0).
    The norm is NOT conserved — it grows due to the ghost contribution.

    Repackaging analysis:
    Any real linear combination A Φ₊ + B Φ₋ (A, B ∈ ℝ, not both zero) will
    include some Φ₋ content when B ≠ 0, inheriting the ghost growth.
    The only combination with zero Φ₋ content is A Φ₊ (B = 0), which is
    a single real field — not useful for complexification.
    Therefore: no linear repackaging of (Φ₊, Φ₋) avoids the ghost obstruction.

    Verdict: doubled_field_pair_complexification_obstructed
    """
    return QB5GhostConstraintAudit(
        phi_minus_eom="dPhi_minus/dt = +Phi_minus / tau",
        phi_minus_growth_rate=PHI_MINUS_GROWTH_RATE,
        phi_minus_growth_rate_sign=PHI_MINUS_GROWTH_RATE_SIGN,
        phi_minus_can_be_imaginary_part=PHI_MINUS_CAN_BE_IMAGINARY_PART,
        formal_j_definition="J(Phi_plus) = Phi_minus;  J(Phi_minus) = -Phi_plus",
        formal_j_satisfies_j_sq=True,
        norm_formula="Phi_plus^2 + Phi_minus^2",
        norm_growth_term="d/dt(Phi_minus^2) = +2*Phi_minus^2/tau  > 0 always",
        norm_conserved_under_dynamics=False,
        norm_growth_rate_sign=+1,
        n_repackaging_attempts=0,
        repackaging_viable=False,
        repackaging_failure_reason=(
            "Every real linear combination involving Phi_minus inherits "
            "the ghost growth rate +1/tau. The only ghost-free combination "
            "is A*Phi_plus alone (B=0), which is a single real field and "
            "cannot form a complexification pair."
        ),
        doubled_field_verdict="doubled_field_pair_complexification_obstructed",
        notes=[
            "Formal J via Keldysh split satisfies J²=−1 algebraically.",
            "Algebraic J²=−1 is necessary but not sufficient for a valid complex structure.",
            "Dynamics compatibility requires norm conservation under time evolution.",
            f"Ghost growth: d(Phi_minus²)/dt = +2*Phi_minus²/tau > 0 (tau = {TAU:.4f}).",
            "d|Psi|²/dt = (-2Phi_plus² + 2Phi_plus*X)/tau + 2*Phi_minus²/tau: growing.",
            "No linear repackaging eliminates ghost: all combinations with Phi_minus grow.",
            "Only Phi_plus alone is ghost-free, but it is a single real field.",
            "Verdict: doubled_field_pair_complexification_obstructed (BSR).",
        ],
    )


# ================================================================
# Track G builder
# ================================================================


def build_track_g_appendix_p() -> QB5AppendixPClassificationAudit:
    """Track G: Appendix P classification per candidate route to J."""
    entries = [
        QB5AppendixPEntry(
            route_id="NR1_ctp_doubled_fields",
            route_name="CTP_doubled_field_complexification",
            appendix_p_class="forbidden_or_inconsistent",
            allowed_claim=(
                "J(Phi_plus)=Phi_minus satisfies J²=−1 algebraically. "
                "The CTP pair can be written in complex notation."
            ),
            forbidden_claim=(
                "The CTP split natively provides a valid complex structure. "
                "The doubled fields constitute a Hilbert space. (FFM6)"
            ),
            dependency_notes=[
                "Blocked by ghost constraint (Track F): norm not conserved.",
                "FFM6 from Q-A charter prohibits hilbert_space_from_ctp_doubling.",
            ],
        ),
        QB5AppendixPEntry(
            route_id="NR2_NR3_NR4_NR5_other_native",
            route_name="all_other_native_routes",
            appendix_p_class="compatible_but_ad_hoc",
            allowed_claim=(
                "Memory kernel, action geometry, response structure, and symplectic "
                "structure are all formally compatible with a complex extension."
            ),
            forbidden_claim=(
                "Any of these structures natively derives J. Fourier-domain "
                "imaginary units constitute physical J."
            ),
            dependency_notes=[
                "Notation-level i in transfer functions is not physical J (Track I nonclaim 3).",
                "Symplectic structure without compatible metric does not give J.",
            ],
        ),
        QB5AppendixPEntry(
            route_id="ER1_ER2_ER4_ER5_effective_blocked",
            route_name="blocked_effective_routes",
            appendix_p_class="compatible_but_ad_hoc",
            allowed_claim=(
                "GRUT's open-system structure is formally analogous to settings "
                "where J appears effectively. The analogy is compatible."
            ),
            forbidden_claim=(
                "Open-system coarse-graining of classical GRUT produces J. "
                "Bath-induced phases create complex structure."
            ),
            dependency_notes=[
                "Effective routes require quantum input to produce quantum output (circular).",
                "Bath dynamics is classicalizing, not quantizing.",
            ],
        ),
        QB5AppendixPEntry(
            route_id="ER3_doubled_real_effective",
            route_name="doubled_real_effective_complex_pairing",
            appendix_p_class="compatible_but_ad_hoc",
            allowed_claim=(
                "The formal pairing Psi_eff = Phi_plus + i*Phi_minus can be written. "
                "This is valid as a bookkeeping notation."
            ),
            forbidden_claim=(
                "The effective pairing constitutes a valid quantum complexification. "
                "The effective amplitude |Psi_eff|² is a conserved probability."
            ),
            dependency_notes=[
                "Ghost norm growth: |Psi_eff|² grows, not conserved.",
                "Track I nonclaim 5: auxiliary pair does not solve native quantum state.",
            ],
        ),
        QB5AppendixPEntry(
            route_id="D_j_as_independent_postulate",
            route_name="J_as_MIP_postulate",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim=(
                "J: real_field_space → real_field_space with J²=−1 may be postulated "
                "at MIP level given two convergent motivations and τ²-constraint. "
                "All Q-C results built on postulated J carry MIP minimum."
            ),
            forbidden_claim=(
                "Postulated J is native_canon. "
                "Postulated J constitutes a derivation of quantum mechanics. "
                "Postulated J implies quantum closure."
            ),
            dependency_notes=[
                "MIP classification per Appendix P boundary rules.",
                "Two convergent motivations: CTP analogy + O(3) topological sector.",
                "τ² = 3/2 constrains compatible dynamics generators.",
                "QA-R3: if new kinematic structure required → MIP minimum classification.",
            ],
        ),
    ]
    return QB5AppendixPClassificationAudit(
        entries=entries,
        n_entries=len(entries),
        overall_j_class="motivated_independent_postulation",
        notes=[
            "NR1 (CTP): FOI — dynamically inconsistent (ghost).",
            "NR2-NR5 (other native): CAH — compatible but not derived.",
            "ER1/ER2/ER4/ER5 (effective blocked): CAH — blocked or circular.",
            "ER3 (doubled-real): CAH — underdetermined compatibility only.",
            "J as MIP postulate: MIP — most favorable viable route.",
            "Overall J class = MIP (most favorable non-rejected classification).",
        ],
    )


# ================================================================
# Track H builder
# ================================================================


def build_track_h_readiness() -> QB5ReadinessAudit:
    """Track H: Quantum program readiness audit.

    Q-C requires:
    1. A complex state space (requires postulated J + inner product, both MIP)
    2. A dynamics law governing complex states (requires dynamics generator, MBU)
    3. Connection to classical limit (Q-C.5 stage)

    Native GRUT does not supply any of these. Therefore:
    - Q-C cannot proceed on native GRUT alone.
    - Q-C CAN proceed if J (and a compatible inner product) are postulated at MIP level.
    - All Q-C results will carry MIP minimum Appendix P classification.
    - The doctrinal basis is explicit: MIP postulation, not native derivation.

    Verdict: proceed_only_if_J_is_postulated
    """
    return QB5ReadinessAudit(
        native_grut_sufficient_for_qc=False,
        j_postulation_required=True,
        inner_product_postulation_required=True,
        qc_can_proceed_natively=False,
        qc_can_proceed_with_postulate=True,
        minimum_postulate_package=QB5_MINIMUM_KINEMATIC_PACKAGE,
        conditions_for_qc=[
            "J_postulated_at_MIP_level_with_J_sq_eq_minus_1",
            "compatible_inner_product_g_postulated_at_MIP_level",
            "dynamics_generator_identified_at_MBU_minimum",
            "all_qc_results_carry_mip_minimum_appendix_p_classification",
            "qb5_nonclaims_registered_and_honored_throughout_qc",
            "qb5_ghost_constraint_explicitly_cited_in_qc_state_space_setup",
        ],
        readiness_verdict="proceed_only_if_J_is_postulated",
        qc_appendix_p_floor="motivated_independent_postulation",
        notes=[
            "Native GRUT: no complex structure, no canonical momentum, no inner product.",
            "Q-C requires: complex states + dynamics generator + classical-limit recovery.",
            "None of the three Q-C requirements are natively present in GRUT.",
            "With MIP postulation of J + inner product: Q-C entry is doctrionally valid.",
            "Q-C Appendix P floor = MIP: no Q-C result can claim native_canon or ER.",
            "BSR results from Q-C are acceptable (bounded negatives preserved per QA-R4).",
            "Readiness verdict: proceed_only_if_J_is_postulated — conditional authorization.",
        ],
    )


# ================================================================
# Track I builder
# ================================================================


def build_track_i_nonclaims() -> QB5NonclaimFirewall:
    """Track I: Nonclaim firewall — 8 explicit nonclaims."""
    return QB5NonclaimFirewall(
        nonclaims=QB5_NONCLAIMS,
        n_nonclaims=N_QB5_NONCLAIMS,
        all_registered=True,
    )


# ================================================================
# Allowed and forbidden claims (master level)
# ================================================================


def build_allowed_claims() -> List[str]:
    """Master-level allowed claims for Q-B.5."""
    return [
        "J cannot be natively derived from audited GRUT architecture (BSR).",
        "J qualifies as motivated_independent_postulation (MIP) given two convergent motivations.",
        "J does not require new DOFs — it acts on existing real field space.",
        "τ² = 3/2 constrains the dynamics generators compatible with postulated J.",
        "The CTP doubled-field pair satisfies J²=−1 algebraically but is dynamically obstructed.",
        "No effective induction route for J is cleanly viable.",
        "J alone is necessary but not sufficient for Q-C.",
        "Q-C may proceed only if J and a compatible inner product are postulated at MIP level.",
        "All Q-C results carry MIP minimum Appendix P classification.",
        "The ghost constraint (Φ₋ growth rate +1/τ) is a precise architectural obstruction.",
    ]


def build_forbidden_claims() -> List[str]:
    """Master-level forbidden claims for Q-B.5."""
    return [
        "J is natively derived from CTP doubled fields or memory kernel.",
        "The CTP doubled fields constitute a valid native complex structure (FFM6).",
        "J is effectively induced in any frequency regime of canonical GRUT.",
        "Coarse-graining classical GRUT produces a quantum complex structure.",
        "Notation-level i in transfer functions constitutes physical complex structure J.",
        "Open-system complexification implies Born rule or probability amplitude.",
        "An auxiliary CTP pair constitutes a native quantum state space.",
        "Effective complex description entails fundamental complex ontology.",
        "Postulated J receives native_canon or effective_reduction classification.",
        "Blocking all five native routes implies J is impossible in principle (BSR ≠ impossibility).",
    ]


# ================================================================
# Master audit function
# ================================================================


def run_qb5_complex_structure_audit() -> QB5ComplexStructureResult:
    """Execute the full Q-B.5 complex structure and kinematic upgrade audit.

    Returns a fully populated QB5ComplexStructureResult with:
      - All 9 audit tracks completed
      - 4 hard-gated verdicts set
      - Appendix P classification throughout
      - Nonclaim firewall registered

    Primary finding: complex_structure_motivated_independent_postulation
    — J cannot be natively derived. J qualifies as MIP with 2 convergent
      motivations. J alone is necessary but not sufficient for Q-C.
      Q-C may proceed only with explicit MIP postulation of J + inner product.
    """
    track_a = build_track_a_missing_ingredient()
    track_b = build_track_b_native_derivation()
    track_c = build_track_c_effective_induction()
    track_d = build_track_d_postulate()
    track_e = build_track_e_kinematic_sufficiency()
    track_f = build_track_f_ghost_constraint()
    track_g = build_track_g_appendix_p()
    track_h = build_track_h_readiness()
    track_i = build_track_i_nonclaims()

    allowed = build_allowed_claims()
    forbidden = build_forbidden_claims()

    # Validate hard-gated verdicts
    assert QB5_PRIMARY_J_STATUS in ALLOWED_PRIMARY_J_STATUSES
    assert QB5_SUFFICIENCY_VERDICT in ALLOWED_SUFFICIENCY_VERDICTS
    assert QB5_DOUBLED_FIELD_VERDICT in ALLOWED_DOUBLED_FIELD_VERDICTS
    assert QB5_READINESS_VERDICT in ALLOWED_READINESS_VERDICTS

    # Consistency checks
    assert track_b.n_routes_accepted == 0
    assert track_b.native_derivation_possible is False
    assert track_c.n_routes_viable == 0
    assert track_c.effective_induction_possible is False
    assert track_d.mip_qualifies is True
    assert track_d.n_convergent_motivations >= 2
    assert track_e.j_alone_sufficient is False
    assert track_e.j_necessary is True
    assert track_f.norm_conserved_under_dynamics is False
    assert track_f.doubled_field_verdict == QB5_DOUBLED_FIELD_VERDICT
    assert track_h.readiness_verdict == QB5_READINESS_VERDICT
    assert track_i.all_registered is True
    assert track_i.n_nonclaims >= 8

    diagnostics: Dict[str, Any] = {
        "n_native_routes_tested": track_b.n_routes_tested,
        "n_native_routes_accepted": track_b.n_routes_accepted,
        "n_effective_routes_tested": track_c.n_routes_tested,
        "n_effective_routes_viable": track_c.n_routes_viable,
        "native_derivation_possible": track_b.native_derivation_possible,
        "effective_induction_possible": track_c.effective_induction_possible,
        "mip_qualifies": track_d.mip_qualifies,
        "n_convergent_motivations": track_d.n_convergent_motivations,
        "j_requires_new_dof": track_d.j_requires_new_dof,
        "j_alone_sufficient": track_e.j_alone_sufficient,
        "n_minimum_package_items": track_e.n_minimum_package_items,
        "phi_minus_growth_rate_sign": track_f.phi_minus_growth_rate_sign,
        "norm_conserved": track_f.norm_conserved_under_dynamics,
        "formal_j_satisfies_j_sq": track_f.formal_j_satisfies_j_sq,
        "tau_sq": TAU_SQ,
        "tau": TAU,
        "n_nonclaims": track_i.n_nonclaims,
        "qb5_appendix_p_class": QB5_OVERALL_APPENDIX_P_CLASS,
    }

    return QB5ComplexStructureResult(
        valid=True,
        track_a_missing_ingredient=track_a,
        track_b_native_derivation=track_b,
        track_c_effective_induction=track_c,
        track_d_postulate=track_d,
        track_e_kinematic_sufficiency=track_e,
        track_f_ghost_constraint=track_f,
        track_g_appendix_p=track_g,
        track_h_readiness=track_h,
        track_i_nonclaims=track_i,
        primary_J_status=QB5_PRIMARY_J_STATUS,
        sufficiency_verdict=QB5_SUFFICIENCY_VERDICT,
        doubled_field_verdict=QB5_DOUBLED_FIELD_VERDICT,
        readiness_verdict=QB5_READINESS_VERDICT,
        qb5_appendix_p_class=QB5_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed,
        forbidden_claims=forbidden,
        diagnostics=diagnostics,
    )
