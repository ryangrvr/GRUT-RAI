"""Appendix Q-C0 — Kinematic Package Completion Audit.

Mission: Determine the minimal additional kinematic package required for GRUT
to support a well-defined quantum dynamics layer, and the doctrinal status of
each required element.

Primary Question
----------------
Given Q-B (no native quantum state space, quantization blocked, CTP compatible only)
and Q-B.5 (J is MIP, J not sufficient, doubled-field obstructed, conditional Q-C
authorization), what is the minimal kinematic package required before Q-C
(quantum microdynamics) can be meaningfully attempted?

Inherited Results
-----------------
  Q-B:   density_matrix_or_functional_state_required (BSR)
         quantization_route_currently_blocked (BSR)
         CTP mapping: compatible_only (CAH)

  Q-B.5: primary_J_status: complex_structure_motivated_independent_postulation (MIP)
         sufficiency_verdict: J_necessary_but_not_sufficient
         doubled_field_verdict: doubled_field_pair_complexification_obstructed
         readiness_verdict: proceed_only_if_J_is_postulated
         Minimum Q-B.5 package: {J (MIP), inner product (MIP), generator (MBU)}

Five Hard-Gated Verdicts
------------------------
  (1) package_verdict
        minimum_kinematic_package_identified
        — Minimum package: {J (MIP) + compatible inner product g (MIP) +
          generator class Lindbladian-like (MBU)}. Three elements, all specified
          with their Appendix P classification.

  (2) inner_product_verdict
        inner_product_motivated_independent_postulation
        — No native inner product is present in GRUT. The natural candidate is
          a J-compatible positive-definite bilinear form g postulated at MIP level,
          using the native real L² pairing on field space as the structural base
          (real bilinear part is native; J-compatibility requires MIP postulate).

  (3) positivity_verdict
        positivity_requires_postulate
        — No positivity structure is natively present. The CTP ghost obstruction
          (Φ₋ growth rate +1/τ, Q-B.5 Track F) rules out all ghost-contaminated norms.
          Positivity is a condition on the postulated inner product g: require g to be
          positive definite. This is part of the MIP inner-product postulate.

  (4) generator_class_verdict
        lindbladian_like_generator_kinematically_admissible
        — Given the kinematic package {J, g}, multiple generator classes are
          kinematically consistent. The Lindbladian is the minimal Markovian
          open-system generator compatible with GRUT's dissipative first-order ODE
          structure. Memory-kernel and influence-functional generators are also
          kinematically admissible (more general). Pure Hamiltonian is kinematically
          possible but inconsistent with GRUT's intrinsically dissipative character.

  (5) readiness_verdict
        ready_only_if_package_is_postulated
        — Q-C cannot begin on native GRUT. Q-C may begin once J and g are postulated
          at MIP level and generator class is identified. All Q-C results carry
          MIP minimum Appendix P classification.

Appendix P Classifications
--------------------------
  J (complex structure):              motivated_independent_postulation (from Q-B.5)
  Compatible inner product g:         motivated_independent_postulation
  Norm ||ψ||² = g(ψ,ψ):              motivated_independent_postulation (follows from g)
  Positivity (g positive definite):   motivated_independent_postulation (part of g postulate)
  State-space topology (pre-Hilbert): bounded_structural_result (derived from J + g)
  Generator class (Lindbladian-like): motivated_but_unbuilt
  Observable structure:               compatible_but_ad_hoc (not needed for Q-C)

Scope Discipline
----------------
  NOT deriving the Born rule.
  NOT deriving measurement.
  NOT deriving interference.
  NOT building toy models.
  NOT silently importing full textbook Hilbert-space QM.
  NOT assuming Hermiticity, unitarity, or Lindblad structure unless supported.
  Only auditing the minimum kinematic package for Q-C entry.

Physical Constants
------------------
  TAU_SQ = 3/2       (canonical, NC — tau_level1_audit.py)
  PHI_MINUS_GROWTH_RATE_SIGN = +1   (ghost, Q-B.5 Track F)

See: grut/qb_quantum_state_space.py      (Q-B)
     grut/qb5_complex_structure_audit.py (Q-B.5)
     grut/q0_quantum_entry_inventory.py  (Q0 inventory)
     grut/qa_quantum_charter.py          (Q-A charter)
     grut/appendix_p_taxonomy_audit.py   (Appendix P)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Hard-gated verdict vocabulary (5 verdicts)
# ================================================================

ALLOWED_PACKAGE_VERDICTS: frozenset = frozenset({
    "minimum_kinematic_package_identified",
    "package_identified_but_still_insufficient",
    "package_still_underdetermined",
    "no_coherent_package_found",
})

ALLOWED_INNER_PRODUCT_VERDICTS: frozenset = frozenset({
    "native_inner_product_available",
    "effective_inner_product_possible",
    "inner_product_motivated_independent_postulation",
    "inner_product_compatible_but_ad_hoc",
    "inner_product_blocked_or_inconsistent",
    "inner_product_still_underdetermined",
})

ALLOWED_POSITIVITY_VERDICTS: frozenset = frozenset({
    "positivity_natively_available",
    "positivity_effectively_recoverable",
    "positivity_requires_postulate",
    "positivity_currently_unavailable",
    "positivity_still_underdetermined",
})

ALLOWED_GENERATOR_CLASS_VERDICTS: frozenset = frozenset({
    "hamiltonian_like_generator_kinematically_admissible",
    "lindbladian_like_generator_kinematically_admissible",
    "memory_kernel_generator_kinematically_admissible",
    "influence_functional_generator_kinematically_admissible",
    "generator_class_still_underdetermined",
    "no_admissible_generator_class_yet",
})

ALLOWED_READINESS_VERDICTS: frozenset = frozenset({
    "ready_to_attempt_QC",
    "ready_only_if_package_is_postulated",
    "still_not_ready_for_QC",
    "requires_further_kinematic_closure",
})

# ================================================================
# Track vocabulary
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

ALLOWED_PACKAGE_ITEM_STATUSES: frozenset = frozenset({
    "already_present",
    "partially_present",
    "absent",
    "obstructed",
    "extension_level_only",
})

ALLOWED_OBSERVABLE_VERDICTS: frozenset = frozenset({
    "not_needed_yet_for_QC",
    "minimally_needed",
    "inseparable_from_inner_product",
    "underdetermined",
})

# ================================================================
# Counts (deterministic)
# ================================================================

N_PACKAGE_ITEMS: int = 7                   # Track A inventory items
N_INNER_PRODUCT_CANDIDATES: int = 5        # Track B candidates
N_INNER_PRODUCT_VIABLE: int = 1            # Only MIP postulate is viable
N_MINIMUM_PACKAGE_ELEMENTS: int = 3        # {J, g, generator class}
N_QC0_NONCLAIMS: int = 8

# Item status counts (Track A)
N_ITEMS_ALREADY_PRESENT: int = 0
N_ITEMS_PARTIALLY_PRESENT: int = 1         # state-space topology (real linear native)
N_ITEMS_ABSENT: int = 5                    # inner product, norm, positivity, generator, observable
N_ITEMS_OBSTRUCTED: int = 0
N_ITEMS_EXTENSION_LEVEL: int = 1           # J (MIP from Q-B.5)

# ================================================================
# Physical constants (canonical GRUT)
# ================================================================

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
ALPHA_VAC: float = 1.0 / 3.0
OMEGA_0_SQ: float = 27.0
R_EQ: float = 1.0 / 3.0

# Q-B.5 inherited constants
PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

# ================================================================
# Q-C0 hard-gated verdict values
# ================================================================

QC0_PACKAGE_VERDICT: str = "minimum_kinematic_package_identified"
QC0_INNER_PRODUCT_VERDICT: str = "inner_product_motivated_independent_postulation"
QC0_POSITIVITY_VERDICT: str = "positivity_requires_postulate"
QC0_GENERATOR_CLASS_VERDICT: str = "lindbladian_like_generator_kinematically_admissible"
QC0_READINESS_VERDICT: str = "ready_only_if_package_is_postulated"
QC0_OVERALL_APPENDIX_P_CLASS: str = "motivated_independent_postulation"

# Minimum kinematic package for Q-C
QC0_MINIMUM_PACKAGE_ELEMENTS: List[str] = [
    "J_complex_structure_mip__j_sq_eq_minus_1",
    "compatible_inner_product_g_mip__g_jpsi_jphi_eq_g_psi_phi__positive_definite",
    "generator_class_lindbladian_like_mbu__markovian_open_system_generator",
]

# ================================================================
# Nonclaims (Track J)
# ================================================================

QC0_NONCLAIMS: List[str] = [
    "NOT_claiming_J_alone_solves_full_quantum_kinematics"
    "__J_enables_complex_superposition_only__not_norm_dynamics_or_observables",
    "NOT_claiming_any_bilinear_form_establishes_physical_inner_product"
    "__real_L2_pairing_is_native_but_J_compatibility_and_positivity_are_postulated",
    "NOT_claiming_any_norm_implies_positivity_is_solved"
    "__ghost_obstruction_rules_out_CTP_based_norms__positivity_requires_postulate",
    "NOT_claiming_open_system_compatibility_implies_Lindblad_structure_is_derived"
    "__Lindblad_class_is_kinematically_admissible__not_derived_from_GRUT_architecture",
    "NOT_claiming_generator_class_compatibility_implies_actual_microdynamics_is_derived"
    "__identifying_generator_class_is_not_the_same_as_finding_the_law__that_is_QC",
    "NOT_claiming_state_space_topology_guess_solves_state_ontology"
    "__pre_Hilbert_topology_is_the_minimum__completeness_and_Born_rule_are_QD",
    "NOT_claiming_postulated_package_receives_native_canon_classification"
    "__all_QC_results_carry_MIP_minimum_per_QA_charter_rule_QA_R3",
    "NOT_claiming_density_matrix_compatibility_implies_full_quantum_closure"
    "__density_matrix_language_is_compatible_but_quantum_closure_is_not_established",
]


# ================================================================
# Dataclasses
# ================================================================


@dataclass
class QC0PackageItem:
    """Single kinematic ingredient in the missing-package inventory (Track A)."""
    item_id: str        # e.g. "KI1_complex_structure_j"
    item_name: str
    status: str         # one of ALLOWED_PACKAGE_ITEM_STATUSES
    appendix_p_class: str
    description: str
    grut_native_analog: Optional[str]   # native GRUT feature that partially satisfies
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0MissingPackageInventory:
    """Track A: Complete inventory of kinematic ingredients."""
    items: List[QC0PackageItem]
    n_items: int           # 7
    n_already_present: int  # 0
    n_partially_present: int  # 1
    n_absent: int          # 5
    n_obstructed: int      # 0
    n_extension_level: int  # 1
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0InnerProductCandidate:
    """Single inner-product candidate route (Track B)."""
    candidate_id: str      # e.g. "IP1_constitutive_field_space"
    candidate_name: str
    description: str
    viable: bool
    classification: str    # Appendix P class for this candidate
    rejection_reason: Optional[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0InnerProductAudit:
    """Track B: Inner product / bilinear pairing audit (5 candidates)."""
    candidates: List[QC0InnerProductCandidate]
    n_candidates: int     # 5
    n_viable: int         # 1
    primary_candidate_id: str  # "IP5_postulated_j_compatible"
    inner_product_verdict: str
    real_bilinear_native: bool  # True — L² real pairing is native
    complex_inner_product_native: bool  # False — needs J
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0NormPositivityAudit:
    """Track C: Norm and positivity audit."""
    ghost_obstruction_inherited: bool    # True (from Q-B.5)
    phi_minus_growth_rate_sign: int      # +1
    ctp_based_norm_ghost_contaminated: bool  # True
    ctp_based_norm_valid: bool           # False
    j_compatible_norm_available_with_postulate: bool  # True
    positivity_native: bool              # False
    positivity_effectively_recoverable: bool  # False
    positivity_requires_postulate: bool  # True
    positivity_open_system_compatible: bool  # True (density matrix ≥ 0 for Lindblad)
    positivity_verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0StateSpaceTopologyAudit:
    """Track D: State-space topology audit."""
    native_topology: str          # "real_linear_field_space"
    minimum_topology_for_qc: str  # "complex_linear_prehilbert_space"
    topology_after_j: str         # "complex_vector_space"
    topology_after_j_and_g: str   # "pre_hilbert_space_without_completeness"
    projective_space_needed_for_qc: bool   # False (needed for Born rule, Q-D)
    density_operator_cone_needed: bool     # False at minimum
    completeness_needed_for_qc: bool       # False (Q-D territory)
    functional_space_over_histories: bool  # Compatible but not minimum
    minimum_topology_description: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0GeneratorAudit:
    """Track E: Generator class audit."""
    # Kinematic admissibility (consistent with J + g + open-system character)
    hamiltonian_kinematically_admissible: bool    # True (but dissipation-inconsistent)
    lindbladian_kinematically_admissible: bool    # True (consistent with Markovian open system)
    memory_kernel_kinematically_admissible: bool  # True (consistent with retarded structure)
    influence_functional_kinematically_admissible: bool  # True (natural for CTP)
    non_hermitian_effective_kinematically_admissible: bool  # True (effective level)
    # Consistency with GRUT's dissipative character
    hamiltonian_grut_consistent: bool    # False (GRUT is dissipative, not closed)
    lindbladian_grut_consistent: bool    # True
    memory_kernel_grut_consistent: bool  # True
    # Primary verdict
    primary_admissible_class: str        # "lindbladian_like"
    additional_admissible_classes: List[str]
    generator_class_verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0ObservableAudit:
    """Track F: Observable / expectation-value structure audit."""
    needed_before_qc: bool            # False
    inseparable_from_inner_product: bool  # True (when needed)
    expectation_value_formula: str    # "Tr(rho * O) in density matrix language"
    observable_verdict: str           # "not_needed_yet_for_QC"
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0MinimumPackage:
    """Track G: Minimum kinematic package for Q-C."""
    package_elements: List[str]    # the 3 elements
    n_elements: int                # 3
    all_elements_specified: bool   # True
    package_appendix_p_classes: List[str]  # class per element
    package_verdict: str
    what_is_not_in_package: List[str]  # items deferred to Q-D or later
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0AppendixPEntry:
    """Single entry in Track H Appendix P table."""
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency_notes: List[str] = field(default_factory=list)


@dataclass
class QC0AppendixPAudit:
    """Track H: Appendix P classification for all package elements."""
    entries: List[QC0AppendixPEntry]
    n_entries: int
    overall_package_class: str    # "motivated_independent_postulation"
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0ReadinessAudit:
    """Track I: Quantum program readiness audit."""
    native_grut_sufficient_for_qc: bool    # False
    package_postulation_required: bool     # True
    j_postulated: bool                     # Required
    inner_product_postulated: bool         # Required
    generator_class_identified: bool       # Required
    qc_can_proceed_with_postulate: bool    # True
    readiness_verdict: str
    qc_appendix_p_floor: str              # "motivated_independent_postulation"
    conditions_for_qc: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class QC0NonclaimFirewall:
    """Track J: Nonclaim firewall — 8 explicit nonclaims."""
    nonclaims: List[str]
    n_nonclaims: int     # 8
    all_registered: bool  # True


@dataclass
class QC0KinematicPackageResult:
    """Master result for Q-C0 kinematic package completion audit."""
    valid: bool
    # Ten audit tracks
    track_a_package_inventory: QC0MissingPackageInventory
    track_b_inner_product: QC0InnerProductAudit
    track_c_norm_positivity: QC0NormPositivityAudit
    track_d_state_space_topology: QC0StateSpaceTopologyAudit
    track_e_generator: QC0GeneratorAudit
    track_f_observable: QC0ObservableAudit
    track_g_minimum_package: QC0MinimumPackage
    track_h_appendix_p: QC0AppendixPAudit
    track_i_readiness: QC0ReadinessAudit
    track_j_nonclaims: QC0NonclaimFirewall
    # Five hard-gated verdicts
    package_verdict: str
    inner_product_verdict: str
    positivity_verdict: str
    generator_class_verdict: str
    readiness_verdict: str
    # Summary
    qc0_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Track A builder
# ================================================================


def build_track_a_package_inventory() -> QC0MissingPackageInventory:
    """Track A: Missing-package inventory — 7 kinematic ingredients."""
    items = [
        QC0PackageItem(
            item_id="KI1_complex_structure_j",
            item_name="complex_structure_J",
            status="extension_level_only",
            appendix_p_class="motivated_independent_postulation",
            description=(
                "J: real_field_space → real_field_space with J² = −1. "
                "Enables complex superposition. Not natively present. "
                "Qualifies as MIP (Q-B.5 Track D: two convergent motivations, "
                "no new DOFs, τ² constrains compatible dynamics)."
            ),
            grut_native_analog="CTP_phi_minus_keldysh_split__algebraically_J_sq_eq_minus_1__but_dynamically_obstructed",
            notes=[
                "From Q-B.5: primary_J_status = complex_structure_motivated_independent_postulation.",
                "CTP analog satisfies J²=−1 algebraically but is dynamically obstructed (ghost).",
                "MIP postulate: J is a constant real linear map commuting with GRUT evolution operator.",
            ],
        ),
        QC0PackageItem(
            item_id="KI2_inner_product",
            item_name="compatible_inner_product_g",
            status="absent",
            appendix_p_class="motivated_independent_postulation",
            description=(
                "A J-compatible positive-definite bilinear form g on field space "
                "satisfying g(Jψ,Jφ) = g(ψ,φ). "
                "Natively GRUT has a real L² pairing on field configurations — "
                "this is the natural structural base. The J-compatibility condition "
                "requires MIP postulate alongside J."
            ),
            grut_native_analog="real_L2_pairing_integral_phi_psi_dx__present_natively_as_real_bilinear",
            notes=[
                "Real L² pairing ∫φψ dx is native to the real field space (NC-level structure).",
                "J-compatibility condition g(Jψ,Jφ)=g(ψ,φ) requires the MIP postulate.",
                "The natural minimal choice: use native L² form and require J to be its isometry.",
            ],
        ),
        QC0PackageItem(
            item_id="KI3_norm_normalization",
            item_name="norm_normalization_rule",
            status="absent",
            appendix_p_class="motivated_independent_postulation",
            description=(
                "The norm ||ψ||² = g(ψ,ψ) follows from the inner product g. "
                "Once g is postulated (positive definite), the norm is defined. "
                "Normalization ψ → ψ/||ψ|| is a derived consequence of the norm."
            ),
            grut_native_analog="none__no_normalization_structure_in_native_grut",
            notes=[
                "Norm follows from g: not an independent postulate once g is specified.",
                "Classified MIP because it inherits from the MIP inner product postulate.",
                "Normalization as Born-rule interpretation is Q-D territory — NOT claimed here.",
            ],
        ),
        QC0PackageItem(
            item_id="KI4_positivity",
            item_name="positivity_condition",
            status="absent",
            appendix_p_class="motivated_independent_postulation",
            description=(
                "The positivity condition g(ψ,ψ) ≥ 0 with equality only for ψ = 0. "
                "This is part of the inner product postulate (positive definiteness of g). "
                "The Q-B.5 ghost obstruction (Φ₋ growth rate +1/τ) rules out "
                "any CTP-based norm as a valid positivity source."
            ),
            grut_native_analog="none__ctp_based_norm_phi_plus_sq_plus_phi_minus_sq_grows_due_to_ghost",
            notes=[
                "Ghost obstruction: d|Ψ_CTP|²/dt > 0 — CTP norm is not positive-definite dynamically.",
                "Positivity requires g to be postulated as positive definite (MIP).",
                "Open-system positivity: Lindblad dynamics preserves ρ ≥ 0 once established.",
            ],
        ),
        QC0PackageItem(
            item_id="KI5_state_space_topology",
            item_name="state_space_topology",
            status="partially_present",
            appendix_p_class="bounded_structural_result",
            description=(
                "The state-space topology is partially present: GRUT natively has a "
                "real linear vector space of field configurations (NC). "
                "The quantum extension requires a complex linear space (after J), "
                "then a pre-Hilbert space (after J + g), then a Hilbert space (after "
                "completion — Q-D territory). Minimum for Q-C: pre-Hilbert space."
            ),
            grut_native_analog="real_linear_field_space_phi_x_native_canon",
            notes=[
                "Native: real linear space ℝ_Φ of field configurations (NC).",
                "After J (MIP): complex linear space ℂ_Φ.",
                "After J + g (MIP): pre-Hilbert space (complex inner product space).",
                "Completion to full Hilbert space is Q-D territory (not needed for Q-C).",
                "BSR: the topology progression is a deterministic consequence of the package.",
            ],
        ),
        QC0PackageItem(
            item_id="KI6_dynamics_generator",
            item_name="dynamics_generator",
            status="absent",
            appendix_p_class="motivated_but_unbuilt",
            description=(
                "A generator specifying how quantum states evolve. The generator type "
                "(class) is kinematically constrained by the package: given dissipative "
                "open-system character, Lindbladian-like is the minimum admissible class. "
                "The actual generator law is Q-C's primary deliverable — not specified here."
            ),
            grut_native_analog="grut_constitutive_ode_tau_dt_phi_plus_phi_eq_x__classical_analog_of_markovian_generator",
            notes=[
                "Generator class = Lindbladian-like (Markovian open system, consistent with ODE).",
                "Actual generator value is NOT determined here — that is Q-C.",
                "MBU: motivated by open-system character and CTP structure; construction not yet done.",
                "τ² = 3/2 constrains compatible generators: [J, H_linear] = 0 required.",
            ],
        ),
        QC0PackageItem(
            item_id="KI7_observable_structure",
            item_name="observable_expectation_structure",
            status="absent",
            appendix_p_class="compatible_but_ad_hoc",
            description=(
                "An observable map O: state_space → ℝ and an expectation-value rule "
                "⟨O⟩ = Tr(ρO) (in density-matrix language). "
                "Not needed for Q-C (which is about finding the dynamics law). "
                "Relevant in Q-D (measurement) and Q-E (benchmark problems). "
                "Inseparable from the inner product choice when eventually needed."
            ),
            grut_native_analog="none__no_observable_structure_in_native_grut",
            notes=[
                "Observable structure is Q-D/Q-E territory: not a Q-C prerequisite.",
                "Expectation value formula Tr(ρO) inseparable from inner product g.",
                "CAH: compatible with quantum extension but not motivated independently of g.",
                "Deferring to Q-D avoids premature Born-rule commitment.",
            ],
        ),
    ]

    counts = {s: sum(1 for it in items if it.status == s)
              for s in ALLOWED_PACKAGE_ITEM_STATUSES}

    return QC0MissingPackageInventory(
        items=items,
        n_items=len(items),
        n_already_present=counts.get("already_present", 0),
        n_partially_present=counts.get("partially_present", 0),
        n_absent=counts.get("absent", 0),
        n_obstructed=counts.get("obstructed", 0),
        n_extension_level=counts.get("extension_level_only", 0),
        notes=[
            "7 kinematic ingredients audited for quantum dynamics layer readiness.",
            "KI1 (J): extension_level_only — MIP from Q-B.5.",
            "KI2 (inner product): absent — MIP postulate needed.",
            "KI3 (norm): absent — derived from inner product once postulated.",
            "KI4 (positivity): absent — part of inner product postulate.",
            "KI5 (topology): partially_present — real linear space native; pre-Hilbert needs J+g.",
            "KI6 (generator): absent — generator class identified (MBU); value is Q-C.",
            "KI7 (observable): absent — not needed for Q-C; CAH when needed.",
        ],
    )


# ================================================================
# Track B builders
# ================================================================


def build_inner_product_candidate_ip1() -> QC0InnerProductCandidate:
    """IP1: Constitutive field-space pairing — real L² bilinear (native)."""
    return QC0InnerProductCandidate(
        candidate_id="IP1_constitutive_field_space",
        candidate_name="real_L2_field_space_pairing",
        description=(
            "The natural real bilinear pairing g_R(ψ,φ) = ∫ψ(x)φ(x)dx on the "
            "real scalar field configuration space. This is a native, positive-definite "
            "real symmetric bilinear form on the real linear space ℝ_Φ."
        ),
        viable=False,
        classification="compatible_but_ad_hoc",
        rejection_reason=(
            "The real L² pairing is a valid REAL inner product but not a complex "
            "inner product without J. To become a complex (Hermitian) inner product, "
            "we need g_R(ψ,φ) + ig_R(Jψ,φ) — which requires J (an MIP postulate). "
            "The real pairing alone does not constitute a quantum inner product. "
            "However, IP1 serves as the NATURAL STRUCTURAL BASE for the IP5 postulate: "
            "postulating that J is an isometry of g_R upgrades it to a Hermitian form. "
            "Classified CAH: real pairing present natively, complex upgrade requires MIP."
        ),
        notes=[
            "∫ψφ dx is native to the real field space — present as NC-level structure.",
            "Positive definite as a real form (∫ψ²dx > 0 for ψ ≠ 0).",
            "Cannot be a complex inner product without J (MIP postulate).",
            "IP1 is the structural base that IP5 builds upon.",
        ],
    )


def build_inner_product_candidate_ip2() -> QC0InnerProductCandidate:
    """IP2: CTP doubled-field pairing — ghost-contaminated."""
    return QC0InnerProductCandidate(
        candidate_id="IP2_ctp_doubled_field",
        candidate_name="ctp_doubled_field_pairing",
        description=(
            "The CTP structure (Φ₁, Φ₂) suggests a bilinear pairing defined via "
            "the Keldysh decomposition: ⟨Ψ|Φ⟩ ~ ∫Φ₊ψ₊ + Φ₋ψ₋ dx, or equivalently "
            "the physical-limit pairing at Φ₁=Φ₂=Φ: ∫ΦΨdx (collapses to IP1)."
        ),
        viable=False,
        classification="forbidden_or_inconsistent",
        rejection_reason=(
            "Any CTP-based inner product that uses Φ₋ as a basis element inherits "
            "the ghost obstruction from Q-B.5 Track F: the norm Φ₊² + Φ₋² grows "
            "at rate 2Φ₋²/τ > 0 under GRUT dynamics. "
            "An inner product that grows under the dynamics is not dynamically admissible: "
            "it cannot serve as a physical probability norm. "
            "The physical limit (Φ₁=Φ₂=Φ, Φ₋→0) collapses to IP1 (real L² pairing) — "
            "not useful for complexification. "
            "FOI: any inner product built on the CTP ghost pair violates the "
            "ghost-contamination prohibition from Q-B.5."
        ),
        notes=[
            "CTP ghost obstruction: d|Ψ_CTP|²/dt = 2Φ₋²/τ > 0 (Q-B.5 Track F).",
            "Physical limit Φ₁=Φ₂=Φ collapses to IP1 (real L², no complexification).",
            "FOI: ghost-contaminated CTP norms are dynamically inadmissible.",
        ],
    )


def build_inner_product_candidate_ip3() -> QC0InnerProductCandidate:
    """IP3: O(3)-sector induced pairing — not applicable to scalar sector."""
    return QC0InnerProductCandidate(
        candidate_id="IP3_o3_sector_induced",
        candidate_name="o3_sector_induced_pairing",
        description=(
            "The O(3) hedgehog target manifold S² carries a natural SO(3)-invariant "
            "metric inherited from the round metric on S². This defines a pairing on "
            "Map(D, S²) via the induced L² metric on sections."
        ),
        viable=False,
        classification="compatible_but_ad_hoc",
        rejection_reason=(
            "The O(3) sector metric is defined on the O(3) target space Map(D, S²), "
            "not on the scalar field configuration space {Φ: D → ℝ}. "
            "The canonical GRUT scalar field Φ takes values in ℝ (one-dimensional), "
            "not in S² (two-sphere). The O(3) MIP (Q0 item A5/C1) is conditionally "
            "present and lives in a separate sector from the canonical real scalar. "
            "The O(3) metric cannot be transferred to the scalar field sector without "
            "a further postulate linking the two sectors."
        ),
        notes=[
            "O(3) metric is on Map(D, S²), not on the real scalar field space.",
            "GRUT canonical scalar Φ ∈ ℝ, not in S².",
            "O(3) sector is conditionally present (MIP, item A5/C1) — separate sector.",
            "CAH: compatible with quantum extension in O(3) sector only, not scalar sector.",
        ],
    )


def build_inner_product_candidate_ip4() -> QC0InnerProductCandidate:
    """IP4: Effective coarse-grained open-system pairing — circular."""
    return QC0InnerProductCandidate(
        candidate_id="IP4_effective_open_system",
        candidate_name="effective_open_system_hilbert_schmidt",
        description=(
            "In open quantum systems, the Hilbert-Schmidt inner product "
            "⟨ρ,σ⟩_HS = Tr(ρ†σ) is natural on the space of density operators. "
            "Could GRUT's effective description give this structure?"
        ),
        viable=False,
        classification="compatible_but_ad_hoc",
        rejection_reason=(
            "The Hilbert-Schmidt inner product Tr(ρ†σ) requires: "
            "(1) a prior Hilbert space ℋ to take the trace over, and "
            "(2) density operators ρ, σ ∈ B(ℋ) (bounded operators on ℋ). "
            "GRUT does not supply ℋ natively (Q-B: D1 absent). "
            "This route is circular: it requires importing a Hilbert space "
            "(the very thing we are trying to construct) to define the inner product. "
            "Q-B.5 ER2 (coarse-grained open-system) was rejected on the same grounds."
        ),
        notes=[
            "Tr(ρ†σ) requires prior Hilbert space — circular for GRUT.",
            "Same circularity as Q-B.5 ER2: quantum in → quantum out.",
            "CAH: formal structure compatible, but circular for GRUT's purposes.",
        ],
    )


def build_inner_product_candidate_ip5() -> QC0InnerProductCandidate:
    """IP5: Postulated J-compatible inner product — the viable MIP route."""
    return QC0InnerProductCandidate(
        candidate_id="IP5_postulated_j_compatible",
        candidate_name="postulated_j_compatible_positive_definite_g",
        description=(
            "Postulate a positive-definite real symmetric bilinear form g on field space "
            "satisfying the J-compatibility condition: g(Jψ, Jφ) = g(ψ, φ). "
            "The natural minimal choice is to use the native real L² pairing (IP1) and "
            "require J to be its isometry. The Hermitian inner product is then: "
            "⟨ψ|φ⟩_ℂ = g(ψ,φ) + ig(Jψ,φ). "
            "This is the least-invasive extension of the native real structure."
        ),
        viable=True,
        classification="motivated_independent_postulation",
        rejection_reason=None,
        notes=[
            "Postulate: g is real symmetric, positive definite, J-compatible.",
            "Natural base: native real L² pairing ∫φψ dx (IP1 as structural foundation).",
            "J-compatibility: g(Jψ,Jφ)=g(ψ,φ) requires J to be a g-isometry.",
            "Hermitian form: ⟨ψ|φ⟩_ℂ = g(ψ,φ) + ig(Jψ,φ).",
            "MIP: two convergent motivations (same as J from Q-B.5), τ²-constrained.",
            "This is the primary viable inner-product route.",
        ],
    )


def build_track_b_inner_product() -> QC0InnerProductAudit:
    """Track B: Full inner product / bilinear pairing audit."""
    candidates = [
        build_inner_product_candidate_ip1(),
        build_inner_product_candidate_ip2(),
        build_inner_product_candidate_ip3(),
        build_inner_product_candidate_ip4(),
        build_inner_product_candidate_ip5(),
    ]
    n_viable = sum(1 for c in candidates if c.viable)
    return QC0InnerProductAudit(
        candidates=candidates,
        n_candidates=len(candidates),
        n_viable=n_viable,
        primary_candidate_id="IP5_postulated_j_compatible",
        inner_product_verdict=QC0_INNER_PRODUCT_VERDICT,
        real_bilinear_native=True,
        complex_inner_product_native=False,
        notes=[
            "IP1 (real L²): native real bilinear, not complex inner product without J.",
            "IP2 (CTP): FOI — ghost-contaminated (d|Ψ|²/dt > 0, Q-B.5 Track F).",
            "IP3 (O(3)): CAH — O(3) metric is on different sector (Map(D, S²)).",
            "IP4 (Hilbert-Schmidt): CAH — circular (requires prior Hilbert space).",
            "IP5 (MIP postulate): viable — uses IP1 as base + J-compatibility condition.",
            "Overall: inner_product_motivated_independent_postulation.",
        ],
    )


# ================================================================
# Track C builder
# ================================================================


def build_track_c_norm_positivity() -> QC0NormPositivityAudit:
    """Track C: Norm and positivity audit.

    The Q-B.5 ghost obstruction (Φ₋ growth rate sign +1) rules out all
    CTP-based norms as dynamically admissible. Any norm construction must
    avoid ghost-contamination.

    The J-compatible inner product g (postulated at MIP level in Track B)
    provides a ghost-safe norm: ||ψ||² = g(ψ,ψ) > 0. This is independent
    of the CTP ghost structure because g is defined on the real field space
    BEFORE complexification — the CTP pair is not used in the norm definition.

    Open-system positivity: in the Lindbladian picture, the density matrix
    ρ satisfies ρ ≥ 0 and Tr(ρ) = 1. Once g is postulated, the trace-class
    condition can be defined, and Lindblad evolution preserves positivity.

    Positivity verdict: positivity_requires_postulate
    """
    return QC0NormPositivityAudit(
        ghost_obstruction_inherited=True,
        phi_minus_growth_rate_sign=PHI_MINUS_GROWTH_RATE_SIGN,
        ctp_based_norm_ghost_contaminated=True,
        ctp_based_norm_valid=False,
        j_compatible_norm_available_with_postulate=True,
        positivity_native=False,
        positivity_effectively_recoverable=False,
        positivity_requires_postulate=True,
        positivity_open_system_compatible=True,
        positivity_verdict=QC0_POSITIVITY_VERDICT,
        notes=[
            "Ghost obstruction: d|Ψ_CTP|²/dt = +2Φ₋²/τ > 0 (Q-B.5 Track F).",
            "Any CTP-based norm that includes Φ₋ component is dynamically growing.",
            "Ghost-safe norm: g(ψ,ψ) from postulated J-compatible g (IP5).",
            "g is defined on real field space independently of CTP ghost structure.",
            "Positivity native: False — no positive definite form defined natively.",
            "Positivity effective: False — no regime where positivity emerges without postulate.",
            "Positivity requires postulate: True — postulate g to be positive definite (MIP).",
            "Open-system compatible: Lindblad dynamics preserves ρ ≥ 0 once established.",
            "Verdict: positivity_requires_postulate (BSR for this finding).",
        ],
    )


# ================================================================
# Track D builder
# ================================================================


def build_track_d_state_space_topology() -> QC0StateSpaceTopologyAudit:
    """Track D: State-space topology audit.

    Native GRUT topology: a real linear vector space ℝ_Φ of field configurations.

    After the kinematic package is installed:
    1. After J (MIP): complex vector space ℂ_Φ (ℝ_Φ with J-defined complex scalar action)
    2. After J + g (MIP): pre-Hilbert space (ℂ_Φ with Hermitian inner product, no completeness)
    3. After completeness (Q-D): full Hilbert space

    For Q-C minimum: a pre-Hilbert space (step 2) is sufficient. We do not need:
    - Projective space CP(ℋ) (needed for Born rule normalization, Q-D)
    - Density-operator cone (needed for mixed states, partially Q-C but separately derivable)
    - Functional space over histories (compatible but not minimum)
    - Topological completeness (Q-D territory)

    Minimum topology: complex linear pre-Hilbert space without completeness.
    """
    return QC0StateSpaceTopologyAudit(
        native_topology="real_linear_field_space_over_R",
        minimum_topology_for_qc="complex_linear_prehilbert_space",
        topology_after_j="complex_vector_space_over_C",
        topology_after_j_and_g="pre_hilbert_space_without_completeness",
        projective_space_needed_for_qc=False,
        density_operator_cone_needed=False,
        completeness_needed_for_qc=False,
        functional_space_over_histories=False,
        minimum_topology_description=(
            "A complex inner-product space (pre-Hilbert space) over ℂ, "
            "without the completeness requirement. Derived from J (MIP) + g (MIP). "
            "This is the minimum topology for defining quantum states and their "
            "overlaps. Dynamics (Q-C) can be formulated on a pre-Hilbert space; "
            "completeness (Hilbert space) is needed for spectral theory and Q-D."
        ),
        notes=[
            "Native: ℝ_Φ = real linear space of scalar field configurations (NC).",
            "After J (MIP): ℂ_Φ = complex linear space (J defines complex scalar action).",
            "After J + g (MIP): pre-Hilbert space = complex inner-product space.",
            "Projective space CP(ℋ): needed for Born rule normalization (Q-D).",
            "Completeness / Hilbert space: needed for spectral theory (Q-D).",
            "Density operator cone: naturally derived from pre-Hilbert space.",
            "Minimum for Q-C: pre-Hilbert space (complex inner product, no completeness).",
            "BSR: this topology determination is a deterministic consequence of J + g.",
        ],
    )


# ================================================================
# Track E builder
# ================================================================


def build_track_e_generator() -> QC0GeneratorAudit:
    """Track E: Generator class audit.

    Given the kinematic package {J (MIP), g (MIP)} installed, what generator
    classes are kinematically admissible for the quantum dynamics law?

    Kinematic admissibility means: the generator is consistent with the
    pre-Hilbert space structure and does not violate GRUT's architectural constraints.

    Analysis:
    - Hamiltonian H (pure unitary evolution iℏ ∂ₜΨ = HΨ):
      Kinematically admissible (any Hermitian H on pre-Hilbert space is a valid generator).
      However, GRUT is intrinsically dissipative: τ dΦ/dt + Φ = X has no conserved
      energy — the equilibrium is set by dissipation, not a potential minimum.
      Pure Hamiltonian evolution would conflict with GRUT's dissipative character.
      Admissible kinematically; GRUT-inconsistent structurally.

    - Lindbladian L[ρ] = −i[H,ρ] + Σ_k(L_k ρ L_k† − ½{L_k†L_k, ρ}):
      Kinematically admissible. Consistent with GRUT's open-system Markovian structure
      (first-order ODE corresponds to Markovian dynamics). Preserves density matrix
      positivity (ρ ≥ 0) and trace (Tr(ρ) = 1). GRUT's constitutive ODE is the
      classical analog of a Markovian master equation. Primary admissible class.

    - Memory-kernel generator ∂ₜρ(t) = ∫₀ᵗ K(t−s) ρ(s) ds:
      Kinematically admissible. Consistent with GRUT's retarded kernel structure
      (Galley CTP, Q0 item C4). More general than Lindblad; non-Markovian.
      Natural candidate for Q-C given CTP retarded structure.

    - Influence-functional generator (path integral weight):
      Kinematically admissible. Most natural for CTP formalism. Compatible with
      Feynman-Vernon / Caldeira-Leggett structure already implicit in GRUT.

    - Non-Hermitian effective generator (e.g., Gamow states, resonances):
      Kinematically admissible as effective description. Relevant if Q-C identifies
      only an effective non-Hermitian law. Not fundamental.

    Primary verdict: lindbladian_like (minimal Markovian open-system generator,
    consistent with first-order ODE structure and open-system character).
    Memory-kernel and influence-functional are also admissible (more general).
    """
    return QC0GeneratorAudit(
        hamiltonian_kinematically_admissible=True,
        lindbladian_kinematically_admissible=True,
        memory_kernel_kinematically_admissible=True,
        influence_functional_kinematically_admissible=True,
        non_hermitian_effective_kinematically_admissible=True,
        hamiltonian_grut_consistent=False,
        lindbladian_grut_consistent=True,
        memory_kernel_grut_consistent=True,
        primary_admissible_class="lindbladian_like",
        additional_admissible_classes=[
            "memory_kernel",
            "influence_functional",
            "non_hermitian_effective",
        ],
        generator_class_verdict=QC0_GENERATOR_CLASS_VERDICT,
        notes=[
            "Hamiltonian: kinematically admissible but GRUT-inconsistent (dissipation).",
            "Lindbladian: kinematically admissible AND GRUT-consistent (Markovian ODE).",
            "Memory-kernel: admissible, GRUT-consistent, more general (retarded CTP).",
            "Influence-functional: admissible, most natural for CTP path-integral language.",
            "Non-Hermitian effective: admissible as effective description.",
            "Primary verdict: Lindbladian (minimal Markovian open-system generator).",
            "Q-C will determine actual generator value — class is constrained here, not value.",
            "MBU: generator class is motivated and constrained; construction is Q-C's task.",
        ],
    )


# ================================================================
# Track F builder
# ================================================================


def build_track_f_observable() -> QC0ObservableAudit:
    """Track F: Observable / expectation-value structure audit.

    Q-C's primary deliverable is the dynamics law — the generator that governs
    how quantum states (density matrices) evolve. Observables are needed to
    extract predictions from states, but Q-C does not require prediction extraction —
    only the law itself.

    Observables become needed in:
    - Q-D (measurement and decoherence): observable = measurement operator
    - Q-E (benchmark toy problems): observable = measurable quantity to compare

    However, the observable structure is not independent of the inner product:
    the expectation value ⟨O⟩_ψ = ⟨ψ|O|ψ⟩ requires the inner product g.
    When observable structure is eventually needed (Q-D), it is inseparable from g.

    Verdict: not_needed_yet_for_QC (but inseparable from g when needed)
    """
    return QC0ObservableAudit(
        needed_before_qc=False,
        inseparable_from_inner_product=True,
        expectation_value_formula="Tr(rho * O)  [density matrix language, when g is established]",
        observable_verdict="not_needed_yet_for_QC",
        notes=[
            "Q-C deliverable: dynamics law (generator). Not prediction extraction.",
            "Observables needed in Q-D (measurement) and Q-E (benchmarks).",
            "⟨O⟩ = Tr(ρO) requires trace structure, inseparable from inner product g.",
            "Deferring observable structure to Q-D avoids premature Born-rule commitment.",
            "CAH: observable structure compatible with the package; not a Q-C prerequisite.",
        ],
    )


# ================================================================
# Track G builder
# ================================================================


def build_track_g_minimum_package() -> QC0MinimumPackage:
    """Track G: Minimum kinematic package for Q-C — 3 elements."""
    return QC0MinimumPackage(
        package_elements=QC0_MINIMUM_PACKAGE_ELEMENTS,
        n_elements=N_MINIMUM_PACKAGE_ELEMENTS,
        all_elements_specified=True,
        package_appendix_p_classes=[
            "motivated_independent_postulation",   # J
            "motivated_independent_postulation",   # inner product g
            "motivated_but_unbuilt",               # generator class
        ],
        package_verdict=QC0_PACKAGE_VERDICT,
        what_is_not_in_package=[
            "born_rule__deferred_to_QD",
            "measurement_postulate__deferred_to_QD",
            "completeness_hilbert_space__deferred_to_QD",
            "observable_structure__deferred_to_QD_QE",
            "entanglement_structure__not_addressed_in_QC0",
            "interference_formalism__deferred_to_QF",
        ],
        notes=[
            "Minimum package: {J (MIP), g (MIP), generator class (MBU)}.",
            "J + g together define a pre-Hilbert space — the minimum quantum state space.",
            "Generator class (Lindbladian-like) identifies what Q-C must construct.",
            "Norm and positivity follow from g (not independent elements).",
            "State-space topology (pre-Hilbert) is a derived consequence of J + g.",
            "Observables, Born rule, completeness deferred to Q-D and later.",
            "Package is minimal: removing any element makes Q-C undefined.",
        ],
    )


# ================================================================
# Track H builder
# ================================================================


def build_track_h_appendix_p() -> QC0AppendixPAudit:
    """Track H: Appendix P classification per package element."""
    entries = [
        QC0AppendixPEntry(
            item_id="KI1_J",
            item_name="complex_structure_J",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim=(
                "J: ℝ_Φ → ℝ_Φ with J² = −1 may be postulated at MIP level. "
                "Enables complex superposition. Constrained by τ² = 3/2."
            ),
            forbidden_claim=(
                "J is natively derived from GRUT. "
                "Postulated J receives native_canon classification."
            ),
            dependency_notes=[
                "From Q-B.5: CTP route to J is dynamically obstructed (ghost).",
                "Two convergent motivations: CTP structural analogy + O(3) sector.",
                "All Q-C results built on J carry MIP minimum (QA-R3).",
            ],
        ),
        QC0AppendixPEntry(
            item_id="KI2_inner_product_g",
            item_name="compatible_inner_product_g",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim=(
                "A positive-definite J-compatible bilinear form g may be postulated "
                "at MIP level, using the native real L² pairing as structural base."
            ),
            forbidden_claim=(
                "The native real L² pairing constitutes a complex inner product. "
                "Any bilinear form establishes a physical quantum inner product."
            ),
            dependency_notes=[
                "Native real L² pairing ∫φψ dx is the structural base (NC).",
                "J-compatibility condition g(Jψ,Jφ)=g(ψ,φ) requires MIP postulate.",
                "CTP-based inner products are ghost-contaminated (FOI).",
            ],
        ),
        QC0AppendixPEntry(
            item_id="KI3_norm",
            item_name="norm_from_g",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim=(
                "||ψ||² = g(ψ,ψ) > 0 is a ghost-safe norm derived from postulated g."
            ),
            forbidden_claim=(
                "Any norm implies positivity is solved. "
                "CTP-based norm |Ψ_CTP|² = Φ₊² + Φ₋² is dynamically admissible."
            ),
            dependency_notes=[
                "Ghost obstruction: CTP norm grows at rate 2Φ₋²/τ > 0.",
                "Ghost-safe norm requires g defined independently of CTP structure.",
            ],
        ),
        QC0AppendixPEntry(
            item_id="KI4_positivity",
            item_name="positivity_from_g_positive_definite",
            appendix_p_class="motivated_independent_postulate",
            allowed_claim=(
                "Positivity g(ψ,ψ) > 0 for ψ ≠ 0 is the positive-definiteness "
                "condition on postulated g. Lindblad evolution preserves ρ ≥ 0."
            ),
            forbidden_claim=(
                "Positivity is natively available. "
                "Open-system compatibility implies Lindblad structure is derived."
            ),
            dependency_notes=[
                "Positivity is a condition on g: postulate g to be positive definite.",
                "Lindblad preserves positivity — consistent check, not a derivation.",
            ],
        ),
        QC0AppendixPEntry(
            item_id="KI5_topology",
            item_name="pre_hilbert_space_topology",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "Pre-Hilbert space topology is the deterministic consequence of J + g: "
                "a complex inner-product space without completeness requirement."
            ),
            forbidden_claim=(
                "State-space topology alone solves state ontology. "
                "Pre-Hilbert space implies Born rule or full quantum closure."
            ),
            dependency_notes=[
                "Topology is derived from J + g: not an independent postulate.",
                "Completeness (Hilbert space) deferred to Q-D.",
                "BSR: deterministic consequence, bounded analysis.",
            ],
        ),
        QC0AppendixPEntry(
            item_id="KI6_generator_class",
            item_name="lindbladian_like_generator_class",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Lindbladian-like generator is kinematically admissible given "
                "GRUT's Markovian dissipative structure. Generator class is identified. "
                "Actual law construction is Q-C's deliverable."
            ),
            forbidden_claim=(
                "Identifying generator class implies actual microdynamics is derived. "
                "Lindblad structure is derived from GRUT architecture."
            ),
            dependency_notes=[
                "Generator CLASS (Lindbladian-like) is identified; VALUE is Q-C.",
                "Memory-kernel and influence-functional also kinematically admissible.",
                "MBU: construction path clear; actual construction not yet done.",
            ],
        ),
    ]

    # Fix typo: motivated_independent_postulate → motivated_independent_postulation for KI4
    for e in entries:
        if e.appendix_p_class == "motivated_independent_postulate":
            e.appendix_p_class = "motivated_independent_postulation"

    return QC0AppendixPAudit(
        entries=entries,
        n_entries=len(entries),
        overall_package_class="motivated_independent_postulation",
        notes=[
            "J: MIP — Q-B.5 result preserved.",
            "Inner product g: MIP — same motivation as J, natural L² base.",
            "Norm: MIP — derived from g, inherits MIP classification.",
            "Positivity: MIP — condition on g postulate.",
            "Topology: BSR — deterministic consequence of J + g.",
            "Generator class: MBU — motivated, constrained, construction deferred to Q-C.",
            "Overall: MIP (dominant classification for the two primary elements).",
        ],
    )


# ================================================================
# Track I builder
# ================================================================


def build_track_i_readiness() -> QC0ReadinessAudit:
    """Track I: Quantum program readiness audit.

    Q-C requires: a pre-Hilbert space (J + g) + a generator class specification.
    None of these are native to GRUT. Therefore Q-C cannot proceed on native GRUT.

    With MIP postulation of J + g, and MBU specification of Lindbladian generator
    class, Q-C may begin. All Q-C results carry MIP minimum Appendix P classification.

    Verdict: ready_only_if_package_is_postulated
    """
    return QC0ReadinessAudit(
        native_grut_sufficient_for_qc=False,
        package_postulation_required=True,
        j_postulated=True,
        inner_product_postulated=True,
        generator_class_identified=True,
        qc_can_proceed_with_postulate=True,
        readiness_verdict=QC0_READINESS_VERDICT,
        qc_appendix_p_floor="motivated_independent_postulation",
        conditions_for_qc=[
            "J_postulated_at_MIP_level__J_sq_eq_minus_1__commutes_with_grut_evolution",
            "inner_product_g_postulated_at_MIP_level__J_compatible__positive_definite",
            "generator_class_lindbladian_like_accepted_as_qc_search_space",
            "all_qc_results_carry_mip_minimum_appendix_p_floor",
            "qc0_nonclaims_registered_and_honored_throughout_qc",
            "ghost_obstruction_explicitly_cited__ctp_based_norms_excluded",
            "qc_deliverable_is_generator_value_not_generator_class",
        ],
        notes=[
            "Native GRUT: no J, no g, no generator — Q-C cannot start.",
            "Package conditions: J (MIP) + g (MIP) + generator class (MBU) all specified.",
            "Q-C task: find the actual generator law (Lindbladian-like or more general).",
            "BSR results from Q-C are valid — bounded negative findings accepted.",
            "Appendix P floor = MIP: no Q-C result may claim NC, ER, or WCH.",
            "Readiness conditional: ready only if package is explicitly postulated.",
        ],
    )


# ================================================================
# Track J builder
# ================================================================


def build_track_j_nonclaims() -> QC0NonclaimFirewall:
    """Track J: Nonclaim firewall — 8 explicit nonclaims."""
    return QC0NonclaimFirewall(
        nonclaims=QC0_NONCLAIMS,
        n_nonclaims=N_QC0_NONCLAIMS,
        all_registered=True,
    )


# ================================================================
# Allowed and forbidden claims (master level)
# ================================================================


def build_allowed_claims() -> List[str]:
    return [
        "Minimum kinematic package for Q-C is identified: {J (MIP), g (MIP), generator class (MBU)}.",
        "The inner product verdict is inner_product_motivated_independent_postulation.",
        "Positivity requires postulate: ghost-contaminated CTP norms are dynamically inadmissible.",
        "The Lindbladian generator class is kinematically admissible given GRUT's Markovian structure.",
        "Pre-Hilbert space (complex inner-product space without completeness) is the minimum topology.",
        "The native real L² pairing serves as the structural base for the MIP inner product postulate.",
        "Observable structure is not a Q-C prerequisite; it is deferred to Q-D.",
        "Q-C readiness verdict: ready_only_if_package_is_postulated.",
        "All Q-C results carry MIP minimum Appendix P classification.",
        "Memory-kernel and influence-functional generators are also kinematically admissible.",
    ]


def build_forbidden_claims() -> List[str]:
    return [
        "J alone solves full quantum kinematics.",
        "The native real L² pairing constitutes a complex inner product.",
        "Any bilinear form establishes a physical quantum inner product.",
        "The CTP norm |Ψ|² = Φ₊² + Φ₋² is dynamically admissible (ghost-contaminated).",
        "Open-system compatibility implies Lindblad structure is derived from GRUT.",
        "Generator class identification implies the microdynamic law is derived.",
        "Pre-Hilbert space topology solves state ontology.",
        "Postulated kinematic package receives native_canon classification.",
        "Density-matrix compatibility implies full quantum closure.",
        "Positivity is natively available or effectively recoverable without postulate.",
    ]


# ================================================================
# Master audit function
# ================================================================


def run_qc0_kinematic_package_audit() -> QC0KinematicPackageResult:
    """Execute the full Q-C0 kinematic package completion audit.

    Returns a fully populated QC0KinematicPackageResult with:
      - All 10 audit tracks completed
      - 5 hard-gated verdicts set
      - Appendix P classification throughout
      - Nonclaim firewall registered

    Primary finding: minimum_kinematic_package_identified
    — {J (MIP) + compatible inner product g (MIP) + Lindbladian generator class (MBU)}.
      Q-C may proceed only if this package is explicitly postulated.
    """
    track_a = build_track_a_package_inventory()
    track_b = build_track_b_inner_product()
    track_c = build_track_c_norm_positivity()
    track_d = build_track_d_state_space_topology()
    track_e = build_track_e_generator()
    track_f = build_track_f_observable()
    track_g = build_track_g_minimum_package()
    track_h = build_track_h_appendix_p()
    track_i = build_track_i_readiness()
    track_j = build_track_j_nonclaims()

    allowed = build_allowed_claims()
    forbidden = build_forbidden_claims()

    # Validate hard-gated verdicts
    assert QC0_PACKAGE_VERDICT in ALLOWED_PACKAGE_VERDICTS
    assert QC0_INNER_PRODUCT_VERDICT in ALLOWED_INNER_PRODUCT_VERDICTS
    assert QC0_POSITIVITY_VERDICT in ALLOWED_POSITIVITY_VERDICTS
    assert QC0_GENERATOR_CLASS_VERDICT in ALLOWED_GENERATOR_CLASS_VERDICTS
    assert QC0_READINESS_VERDICT in ALLOWED_READINESS_VERDICTS

    # Consistency checks
    assert track_a.n_items == N_PACKAGE_ITEMS
    assert track_b.n_candidates == N_INNER_PRODUCT_CANDIDATES
    assert track_b.n_viable == N_INNER_PRODUCT_VIABLE
    assert track_c.ctp_based_norm_valid is False
    assert track_c.positivity_requires_postulate is True
    assert track_e.lindbladian_grut_consistent is True
    assert track_e.hamiltonian_grut_consistent is False
    assert track_g.n_elements == N_MINIMUM_PACKAGE_ELEMENTS
    assert track_g.all_elements_specified is True
    assert track_i.readiness_verdict == QC0_READINESS_VERDICT
    assert track_j.n_nonclaims == N_QC0_NONCLAIMS
    assert track_j.all_registered is True

    diagnostics: Dict[str, Any] = {
        "n_package_items": track_a.n_items,
        "n_items_absent": track_a.n_absent,
        "n_items_extension_level": track_a.n_extension_level,
        "n_items_partially_present": track_a.n_partially_present,
        "n_inner_product_candidates": track_b.n_candidates,
        "n_inner_product_viable": track_b.n_viable,
        "ctp_norm_valid": track_c.ctp_based_norm_valid,
        "positivity_requires_postulate": track_c.positivity_requires_postulate,
        "ghost_obstruction_inherited": track_c.ghost_obstruction_inherited,
        "phi_minus_growth_rate_sign": PHI_MINUS_GROWTH_RATE_SIGN,
        "minimum_topology": track_d.minimum_topology_for_qc,
        "lindbladian_grut_consistent": track_e.lindbladian_grut_consistent,
        "hamiltonian_grut_consistent": track_e.hamiltonian_grut_consistent,
        "observable_needed_before_qc": track_f.needed_before_qc,
        "n_minimum_package_elements": track_g.n_elements,
        "n_nonclaims": track_j.n_nonclaims,
        "tau_sq": TAU_SQ,
        "qc0_appendix_p_class": QC0_OVERALL_APPENDIX_P_CLASS,
    }

    return QC0KinematicPackageResult(
        valid=True,
        track_a_package_inventory=track_a,
        track_b_inner_product=track_b,
        track_c_norm_positivity=track_c,
        track_d_state_space_topology=track_d,
        track_e_generator=track_e,
        track_f_observable=track_f,
        track_g_minimum_package=track_g,
        track_h_appendix_p=track_h,
        track_i_readiness=track_i,
        track_j_nonclaims=track_j,
        package_verdict=QC0_PACKAGE_VERDICT,
        inner_product_verdict=QC0_INNER_PRODUCT_VERDICT,
        positivity_verdict=QC0_POSITIVITY_VERDICT,
        generator_class_verdict=QC0_GENERATOR_CLASS_VERDICT,
        readiness_verdict=QC0_READINESS_VERDICT,
        qc0_appendix_p_class=QC0_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed,
        forbidden_claims=forbidden,
        diagnostics=diagnostics,
    )
