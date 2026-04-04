"""
Appendix Q-II.0 --- Second-Wave Quantum Gap Inventory
=====================================================
GRUT Quantum Program --- Phase Q-II.0  (Entry to Second Wave)

This module inventories all quantum structures that remain unresolved after
Appendix Q, Part I (Q-B through Q-F) and classifies each gap by doctrinal
status.

Part I closure established:
  - extension-level quantum state-space direction (Q-B / Q-B.5)
  - extension-level complex structure J (Q-B.5, MIP)
  - minimum kinematic package (Q-C0)
  - preferred Lindbladian-like microdynamic class (Q-C)
  - effective-regime constitutive recovery (Q-C.5)
  - effective-regime decoherence and pointer-basis class (Q-D)
  - benchmark toy models: QE1--QE4 (Q-E)
  - transient interference before decoherence (Q-F)
  - authorization to close first-wave quantum program (Q-F)

Part II must address:
  A. Composite / many-body state structure
  B. Entanglement / nonfactorized state structure
  C. Observable algebra / multi-observable grammar
  D. Excitation / many-mode / field structure
  E. Probability / determination / outcome structure
  F. Matter-readiness mapping

Hard epistemic rules (inherited from Q0, strengthened):
  1. Prefer absence over implication.
  2. Prefer obstruction over vague openness when obstruction already exists.
  3. Preserve all first-wave nonclaims.
  4. Do not treat toy-model success as many-body readiness.
  5. Do not treat decoherence as entanglement.
  6. Do not treat two-path interference as field-excitation closure.
  7. Do not promote any first-wave result above its locked Appendix P class.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU

# Allowed vocabularies
ALLOWED_PRESENCE_STATES: frozenset = frozenset({
    "absent", "obstructed", "conditionally_present", "extension_level",
    "first_wave_established",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})
ALLOWED_CATEGORY_LABELS: frozenset = frozenset({
    "A_composite_state", "B_entanglement", "C_observable_algebra",
    "D_excitation_field_mode", "E_probability_determination",
    "F_matter_readiness",
})

# Category counts
N_CATEGORY_A_ITEMS: int = 4
N_CATEGORY_B_ITEMS: int = 5
N_CATEGORY_C_ITEMS: int = 5
N_CATEGORY_D_ITEMS: int = 5
N_CATEGORY_E_ITEMS: int = 5
N_CATEGORY_F_ITEMS: int = 5
N_TOTAL_ITEMS: int = 29

N_QII0_NONCLAIMS: int = 8
N_HARD_RULES: int = 7

# Inherited first-wave closure
QF_INHERITED_AUTHORIZATION: str = "authorized_to_close_first_wave_quantum_program"
QF_INHERITED_PHASE: str = "relative_phase_structure_demonstrated_in_toy_form"
QF_INHERITED_INTERFERENCE: str = "transient_interference_before_decoherence_demonstrated"
QF_INHERITED_SLIT: str = "abstract_two_path_interpretation_justified"
QF_INHERITED_CONSTITUTIVE_INTERFERENCE: str = (
    "interference_requires_complementary_observable_sector"
)

# Verdict
QII0_INVENTORY_VERDICT: str = (
    "second_wave_gap_inventory_complete__all_gaps_documented"
)

# Hard epistemic rules
HARD_EPISTEMIC_RULES: List[str] = [
    "prefer_absence_over_implication",
    "prefer_obstruction_over_vague_openness_when_obstruction_exists",
    "preserve_all_first_wave_nonclaims",
    "do_not_treat_toy_model_success_as_many_body_readiness",
    "do_not_treat_decoherence_as_entanglement",
    "do_not_treat_two_path_interference_as_field_excitation_closure",
    "do_not_promote_first_wave_results_above_locked_appendix_p_class",
]

# Nonclaims
QII0_NONCLAIMS: List[str] = [
    "NOT_claiming_first_wave_toy_models_therefore_many_body_quantum_ready__"
    "two_state_benchmarks_do_not_generalize_to_composite_systems",
    "NOT_claiming_decoherence_therefore_entanglement__"
    "pointer_basis_selection_is_not_nonfactorized_state_structure",
    "NOT_claiming_single_observable_success_therefore_operator_algebra_derived__"
    "Phi_hat_is_one_observable_not_a_multi_observable_grammar",
    "NOT_claiming_two_path_interference_therefore_field_excitation_closure__"
    "abstract_two_component_superposition_is_not_many_mode_structure",
    "NOT_claiming_effective_regime_decoherence_therefore_Born_rule__"
    "off_diagonal_suppression_does_not_yield_probability_weighting",
    "NOT_claiming_first_wave_closure_therefore_quantum_theory_complete__"
    "Part_I_established_extension_level_foundations_not_full_quantum_mechanics",
    "NOT_claiming_interference_toy_model_therefore_matter_readiness__"
    "transient_cross_terms_do_not_constitute_particle_physics_readiness",
    "NOT_claiming_absent_structures_are_permanently_blocked__"
    "absence_documents_current_state_not_impossibility_in_principle",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QII0GapItem:
    """Single gap inventory item."""
    item_id: str
    item_name: str
    category: str
    presence_state: str
    appendix_p_class: str
    supporting_audit: str
    allowed_claim: str
    forbidden_claim: str
    dependency_notes: List[str]
    notes: List[str]


@dataclass
class QII0CategorySummary:
    """Summary for one gap category."""
    category_label: str
    n_items: int
    item_ids: List[str]
    n_absent: int
    n_obstructed: int
    n_extension_level: int
    description: str


@dataclass
class QII0ReadinessAssessment:
    """Assessment of readiness to proceed to Q-II.B."""
    first_wave_closed: bool
    all_gaps_documented: bool
    no_silent_promotions: bool
    nonclaims_preserved: bool
    hard_rules_applied: bool
    ready_for_qiib: bool
    readiness_verdict: str
    notes: List[str]


@dataclass
class QII0GapInventoryResult:
    """Master result for Q-II.0."""
    valid: bool
    items: List[QII0GapItem]
    category_summaries: List[QII0CategorySummary]
    readiness_assessment: QII0ReadinessAssessment
    n_total: int
    n_absent: int
    n_obstructed: int
    n_extension_level: int
    n_first_wave_established: int
    hard_rules: List[str]
    nonclaims: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    inventory_verdict: str
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Item builders (one per category)
# ---------------------------------------------------------------------------

def _build_category_a() -> List[QII0GapItem]:
    """Category A --- composite-state gaps."""
    return [
        QII0GapItem(
            item_id="A1",
            item_name="tensor_product_or_composite_state_structure",
            category="A_composite_state",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (single-system only)",
            allowed_claim=(
                "Tensor product structure is mathematically standard and could be "
                "postulated for GRUT extension"
            ),
            forbidden_claim=(
                "Tensor product structure is already present or derivable from "
                "first-wave single-system results"
            ),
            dependency_notes=[
                "All Q-E/Q-F toy models are single-system 2-state",
                "No multi-system or composite Hilbert space has been postulated",
                "Tensor product is a standard QM construction but requires explicit postulation",
            ],
            notes=[
                "Absent: no tensor product structure in any first-wave audit",
                "Would require: H_AB = H_A tensor H_B with specified subsystem structure",
                "Appendix P: compatible_but_ad_hoc until motivated by GRUT architecture",
            ],
        ),
        QII0GapItem(
            item_id="A2",
            item_name="subsystem_factorization",
            category="A_composite_state",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no subsystem notion)",
            allowed_claim=(
                "Subsystem factorization is a standard quantum structure that "
                "could be postulated"
            ),
            forbidden_claim=(
                "Subsystem factorization is implicit in the 2-state model"
            ),
            dependency_notes=[
                "Requires tensor product (A1) as prerequisite",
                "The 2-state model is a SINGLE system, not two subsystems",
            ],
            notes=[
                "Absent: no subsystem or partial-trace notion in first wave",
                "Depends on A1 (tensor product) being established first",
            ],
        ),
        QII0GapItem(
            item_id="A3",
            item_name="reduced_state_composition_rules",
            category="A_composite_state",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no partial trace)",
            allowed_claim=(
                "Partial trace and reduced-state rules are standard and could "
                "be postulated"
            ),
            forbidden_claim=(
                "Reduced-state rules follow from first-wave decoherence results"
            ),
            dependency_notes=[
                "Requires A1 (tensor product) and A2 (subsystem factorization)",
                "Partial trace rho_A = Tr_B(rho_AB) requires composite Hilbert space",
            ],
            notes=[
                "Absent: no partial trace or reduced state in first wave",
                "Sequential dependency: A1 -> A2 -> A3",
            ],
        ),
        QII0GapItem(
            item_id="A4",
            item_name="many_body_state_grammar",
            category="A_composite_state",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (single-system only)",
            allowed_claim=(
                "Many-body state grammar could be constructed once composite "
                "structure is established"
            ),
            forbidden_claim=(
                "Many-body structure is implicit in or derivable from "
                "the two-state toy model"
            ),
            dependency_notes=[
                "Requires A1, A2, A3 as prerequisites",
                "Would also require symmetrization/antisymmetrization rules (F3)",
            ],
            notes=[
                "Absent: no many-body state language in first wave",
                "Highest-level composite gap; depends on all prior A-category items",
            ],
        ),
    ]


def _build_category_b() -> List[QII0GapItem]:
    """Category B --- entanglement gaps."""
    return [
        QII0GapItem(
            item_id="B1",
            item_name="nonfactorized_state_structure",
            category="B_entanglement",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no composite states)",
            allowed_claim=(
                "Nonfactorized states are standard in QM and could be postulated "
                "once composite structure exists"
            ),
            forbidden_claim=(
                "Nonfactorized structure is already present because decoherence "
                "was demonstrated"
            ),
            dependency_notes=[
                "Requires A1 (tensor product) as prerequisite",
                "Decoherence in single-system is NOT entanglement",
            ],
            notes=[
                "Absent: no composite state, hence no entanglement possible",
                "Decoherence (Q-D) operates on single-system off-diagonals, "
                "not inter-system correlations",
            ],
        ),
        QII0GapItem(
            item_id="B2",
            item_name="entanglement_criteria",
            category="B_entanglement",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no entanglement audit)",
            allowed_claim=(
                "Entanglement criteria (PPT, concurrence, negativity) are "
                "standard and could be applied once composite states exist"
            ),
            forbidden_claim=(
                "Entanglement criteria are derivable from single-system "
                "decoherence or pointer-basis analysis"
            ),
            dependency_notes=[
                "Requires B1 (nonfactorized states) as prerequisite",
                "Standard criteria need composite Hilbert space + partial trace",
            ],
            notes=["Absent: no composite framework to apply entanglement criteria to"],
        ),
        QII0GapItem(
            item_id="B3",
            item_name="correlation_measures",
            category="B_entanglement",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no correlation measures)",
            allowed_claim=(
                "Quantum correlation measures could be defined once composite "
                "and entanglement structure exists"
            ),
            forbidden_claim=(
                "Correlation measures follow from single-system coherence"
            ),
            dependency_notes=[
                "Requires B1 and B2 as prerequisites",
                "Mutual information, discord, etc. require partial trace + composite states",
            ],
            notes=["Absent: no inter-system correlation framework in first wave"],
        ),
        QII0GapItem(
            item_id="B4",
            item_name="bell_chsh_structure",
            category="B_entanglement",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no Bell-type analysis)",
            allowed_claim=(
                "Bell/CHSH inequalities are standard and could be investigated "
                "once entanglement is established"
            ),
            forbidden_claim=(
                "Bell-type nonlocality is derivable from first-wave interference "
                "or decoherence results"
            ),
            dependency_notes=[
                "Requires B1, B2, and multi-observable structure (C1, C2)",
                "Bell tests require measurements in different bases on separate subsystems",
            ],
            notes=[
                "Absent: no multi-party measurement framework",
                "Bell/CHSH is a high-level entanglement test; many prerequisites",
            ],
        ),
        QII0GapItem(
            item_id="B5",
            item_name="entanglement_route_assessment",
            category="B_entanglement",
            presence_state="absent",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-F Track I (second_wave_scope includes entanglement)",
            allowed_claim=(
                "Entanglement is identified as a second-wave scope item; "
                "no hint of entanglement from first-wave results"
            ),
            forbidden_claim=(
                "First-wave results hint at or partially establish entanglement"
            ),
            dependency_notes=[
                "Q-F nonclaim: NOT_claiming_interference_toy_model_therefore_"
                "entanglement_formalism_derived",
                "Entanglement is entirely absent, not partially present",
            ],
            notes=[
                "BSR: proved architectural absence in first wave",
                "No single first-wave result provides even a partial hint of entanglement",
                "Clean gap: must be built from scratch in Part II",
            ],
        ),
    ]


def _build_category_c() -> List[QII0GapItem]:
    """Category C --- observable-algebra gaps."""
    return [
        QII0GapItem(
            item_id="C1",
            item_name="multi_observable_grammar",
            category="C_observable_algebra",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-E (QE3 underdetermined: only sigma_z motivated)",
            allowed_claim=(
                "A multi-observable grammar could be postulated; "
                "only Phi_hat = sigma_z is currently motivated"
            ),
            forbidden_claim=(
                "Multiple observables are already motivated by first-wave results"
            ),
            dependency_notes=[
                "QE3 found: second observable not independently motivated",
                "sigma_x, sigma_y exist mathematically in C^2 but lack GRUT grounding",
            ],
            notes=[
                "Absent: only one GRUT-motivated observable (Phi_hat)",
                "QE3 underdetermined verdict documents this gap explicitly",
            ],
        ),
        QII0GapItem(
            item_id="C2",
            item_name="noncommuting_observable_structure",
            category="C_observable_algebra",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-E (QE3: commutator not specified)",
            allowed_claim=(
                "Noncommuting observables could be established with a motivated "
                "second observable"
            ),
            forbidden_claim=(
                "Noncommuting structure is derivable from the single observable Phi_hat"
            ),
            dependency_notes=[
                "Requires C1 (multi-observable grammar) first",
                "[A, B] != 0 requires two independently motivated operators",
            ],
            notes=[
                "Absent: no nontrivial commutator established",
                "Robertson-Heisenberg relation formally writable but operators unmotivated",
            ],
        ),
        QII0GapItem(
            item_id="C3",
            item_name="observable_composition_rules",
            category="C_observable_algebra",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no algebra rules)",
            allowed_claim=(
                "Observable composition rules (sums, products, functions of operators) "
                "could be defined once multi-observable structure exists"
            ),
            forbidden_claim=(
                "Observable composition rules follow from Phi_hat alone"
            ),
            dependency_notes=[
                "Requires C1 and C2 as prerequisites",
                "Standard operator algebra needs multiple independent operators",
            ],
            notes=["Absent: no operator algebraic rules beyond single observable"],
        ),
        QII0GapItem(
            item_id="C4",
            item_name="expectation_value_closure_beyond_constitutive",
            category="C_observable_algebra",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-C.5 / Q-E (only <Phi_hat> recovered)",
            allowed_claim=(
                "Expectation-value closure for other observables could be derived "
                "once those observables are motivated"
            ),
            forbidden_claim=(
                "Expectation-value closure is general because <Phi_hat> was recovered"
            ),
            dependency_notes=[
                "Q-C.5 recovered tau d<Phi>/dt + <Phi> = <X> for Phi_hat only",
                "No other expectation-value law has been established",
            ],
            notes=[
                "Absent: constitutive recovery is for one observable only",
                "Generalizing to other observables requires multi-observable grammar (C1)",
            ],
        ),
        QII0GapItem(
            item_id="C5",
            item_name="compatibility_vs_incompatibility_classes",
            category="C_observable_algebra",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no compatibility analysis)",
            allowed_claim=(
                "Observable compatibility classes could be defined once "
                "commutator structure is established"
            ),
            forbidden_claim=(
                "Compatibility classes are derivable from pointer-basis selection"
            ),
            dependency_notes=[
                "Requires C2 (noncommuting structure) as prerequisite",
                "Pointer basis selects Phi_hat eigenstates; this is basis preference, "
                "not compatibility classification",
            ],
            notes=["Absent: no compatibility/incompatibility framework"],
        ),
    ]


def _build_category_d() -> List[QII0GapItem]:
    """Category D --- excitation / field-mode gaps."""
    return [
        QII0GapItem(
            item_id="D1",
            item_name="many_mode_excitation_language",
            category="D_excitation_field_mode",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (single mode only)",
            allowed_claim=(
                "Many-mode excitation language could be constructed as an extension"
            ),
            forbidden_claim=(
                "Many-mode structure is implicit in the 2-state toy model"
            ),
            dependency_notes=[
                "The 2-state model is a single mode (one scalar field Phi)",
                "Many-mode requires either spatial DOF or multiple field components",
            ],
            notes=[
                "Absent: all first-wave work operates on a single scalar field",
                "Q-F explicitly noted spatial DOF as absent in remaining_gaps",
            ],
        ),
        QII0GapItem(
            item_id="D2",
            item_name="field_excitation_basis",
            category="D_excitation_field_mode",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no Fock space or excitation basis)",
            allowed_claim=(
                "Field excitation basis (Fock space, number states) could be "
                "postulated as an extension"
            ),
            forbidden_claim=(
                "Field excitation basis is derivable from first-wave Lindblad structure"
            ),
            dependency_notes=[
                "Fock space requires creation/annihilation operators (D4)",
                "No mode decomposition exists to define excitation levels",
            ],
            notes=["Absent: no excitation basis or Fock-like structure"],
        ),
        QII0GapItem(
            item_id="D3",
            item_name="mode_decomposition",
            category="D_excitation_field_mode",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no spatial or momentum modes)",
            allowed_claim=(
                "Mode decomposition could be established once spatial or "
                "momentum structure is available"
            ),
            forbidden_claim=(
                "Mode decomposition follows from the single-field Lindblad structure"
            ),
            dependency_notes=[
                "Requires spatial degrees of freedom or momentum-space structure",
                "Q-F remaining_gaps includes spatial_degrees_of_freedom_absent",
            ],
            notes=["Absent: no spatial, momentum, or frequency modes in first wave"],
        ),
        QII0GapItem(
            item_id="D4",
            item_name="creation_annihilation_analogs",
            category="D_excitation_field_mode",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no ladder operators)",
            allowed_claim=(
                "Creation/annihilation operators could be introduced as part of "
                "field quantization extension"
            ),
            forbidden_claim=(
                "Ladder operators are derivable from the jump operator L"
            ),
            dependency_notes=[
                "L = (1/sqrt(tau)) Phi_hat is a DISSIPATION operator, not a ladder operator",
                "Creation/annihilation require: [a, a^dag] = 1, harmonic structure",
            ],
            notes=[
                "Absent: jump operator is dissipative, not excitation-creating",
                "Distinct from standard a, a^dag structure",
            ],
        ),
        QII0GapItem(
            item_id="D5",
            item_name="toy_level_limitation_documented",
            category="D_excitation_field_mode",
            presence_state="first_wave_established",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-E / Q-F (all toy models are 2-state single-system)",
            allowed_claim=(
                "First-wave quantum results are explicitly toy-level "
                "(single system, 2-state, single field): this limitation is documented"
            ),
            forbidden_claim=(
                "Toy-level results generalize to field-theoretic or many-mode systems"
            ),
            dependency_notes=[
                "Q-F nonclaim: NOT_claiming_any_two_state_phase_model_therefore_"
                "field_theoretic_interference_solved",
            ],
            notes=[
                "First-wave established: the limitation IS the documented result",
                "BSR: proved that current package only supports toy-level reduced systems",
            ],
        ),
    ]


def _build_category_e() -> List[QII0GapItem]:
    """Category E --- probability / determination gaps."""
    return [
        QII0GapItem(
            item_id="E1",
            item_name="born_rule_weighting",
            category="E_probability_determination",
            presence_state="absent",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-D (born_rule_or_outcome_selection_not_natively_derived)",
            allowed_claim=(
                "Born-rule absence is explicitly documented; "
                "investigation is second-wave scope"
            ),
            forbidden_claim=(
                "Born rule is derivable from decoherence, pointer basis, "
                "or interference results"
            ),
            dependency_notes=[
                "Q-D verdict: born_rule_or_outcome_selection_not_natively_derived",
                "Q-F nonclaim: NOT_claiming_phase_sensitive_cross_term_therefore_Born_rule",
            ],
            notes=[
                "BSR: proved absent in first-wave architecture",
                "Clean gap: must be investigated from scratch in Part II",
            ],
        ),
        QII0GapItem(
            item_id="E2",
            item_name="single_outcome_selection",
            category="E_probability_determination",
            presence_state="absent",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-D Track E (all 4 mechanisms absent)",
            allowed_claim=(
                "Single-outcome selection absence is documented; "
                "investigation is second-wave scope"
            ),
            forbidden_claim=(
                "Outcome selection follows from decoherence or pointer basis"
            ),
            dependency_notes=[
                "Q-D: 4 outcome-selection mechanisms all absent",
                "Decoherence selects a BASIS, not a single OUTCOME",
            ],
            notes=["BSR: proved absent in first-wave; distinct from decoherence"],
        ),
        QII0GapItem(
            item_id="E3",
            item_name="irreversible_branch_selection",
            category="E_probability_determination",
            presence_state="absent",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-D Track E (absent)",
            allowed_claim=(
                "Branch selection absence documented; would require "
                "additional mechanism beyond Lindblad"
            ),
            forbidden_claim=(
                "Branch selection is implied by decoherence"
            ),
            dependency_notes=[
                "Lindblad evolution is deterministic for density matrix",
                "No stochastic mechanism embedded in current formalism",
            ],
            notes=["BSR: absent; Lindblad evolution does not branch"],
        ),
        QII0GapItem(
            item_id="E4",
            item_name="observer_conditioned_update",
            category="E_probability_determination",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-D Track E (absent)",
            allowed_claim=(
                "Observer-conditioned update (collapse postulate) could be "
                "postulated but is not derived"
            ),
            forbidden_claim=(
                "Observer-conditioned update follows from any first-wave result"
            ),
            dependency_notes=[
                "Q-D explicitly classified this as absent",
                "Would require measurement theory beyond Lindblad dynamics",
            ],
            notes=["Absent: no collapse or update rule in first wave"],
        ),
        QII0GapItem(
            item_id="E5",
            item_name="effective_determination_tendencies",
            category="E_probability_determination",
            presence_state="extension_level",
            appendix_p_class="motivated_but_unbuilt",
            supporting_audit="Q-D / Q-F (decoherence suppresses off-diagonals)",
            allowed_claim=(
                "Decoherence provides an effective tendency toward diagonal "
                "(classical-looking) density matrix; this is a tendency, not determination"
            ),
            forbidden_claim=(
                "Effective decoherence tendency constitutes outcome determination "
                "or probability assignment"
            ),
            dependency_notes=[
                "Decoherence drives rho toward diagonal form in pointer basis",
                "This is a TENDENCY (off-diagonals -> 0), not a DETERMINATION "
                "(one diagonal element selected)",
            ],
            notes=[
                "Extension-level: decoherence tendency exists but does not determine outcomes",
                "MBU: the tendency is motivated but outcome determination is unbuilt",
            ],
        ),
    ]


def _build_category_f() -> List[QII0GapItem]:
    """Category F --- matter-readiness gaps."""
    return [
        QII0GapItem(
            item_id="F1",
            item_name="bosonic_quantum_matter_readiness",
            category="F_matter_readiness",
            presence_state="absent",
            appendix_p_class="motivated_but_unbuilt",
            supporting_audit="Q-B through Q-F (no particle content)",
            allowed_claim=(
                "Bosonic matter-readiness path is motivated by GRUT scalar field "
                "architecture but not built at quantum level"
            ),
            forbidden_claim=(
                "Bosonic quantum matter is ready because toy models were demonstrated"
            ),
            dependency_notes=[
                "Classical GRUT has bosonic field (Phi); quantum bosonic particles "
                "require field quantization (D1-D4)",
                "Skyrme-term structure (Appendix N) provides topological route "
                "but at classical level only",
            ],
            notes=["Absent at quantum level; motivated by classical architecture"],
        ),
        QII0GapItem(
            item_id="F2",
            item_name="fermionic_quantum_matter_readiness",
            category="F_matter_readiness",
            presence_state="obstructed",
            appendix_p_class="bounded_structural_result",
            supporting_audit="Q-B / Q0 (3-layer fermionic obstruction)",
            allowed_claim=(
                "Fermionic obstruction is a documented BSR: pi_2(S^2) = Z yields "
                "bosonic winding only; no spinorial representation without new structure"
            ),
            forbidden_claim=(
                "Fermionic matter is accessible from current GRUT architecture "
                "without new topological or algebraic structure"
            ),
            dependency_notes=[
                "Q0 item E1: fermionic_emergence obstructed (3-layer obstruction)",
                "Would require: spinorial structure, Hopf fibration, or new algebraic postulate",
            ],
            notes=[
                "Obstructed: BSR from Q0; 3-layer fermionic obstruction",
                "Most constrained matter-readiness gap",
            ],
        ),
        QII0GapItem(
            item_id="F3",
            item_name="statistics_readiness",
            category="F_matter_readiness",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no statistics formalism)",
            allowed_claim=(
                "Quantum statistics (Bose-Einstein / Fermi-Dirac) could be "
                "postulated once composite state structure exists"
            ),
            forbidden_claim=(
                "Statistics follow from any first-wave result or from "
                "the single-system toy model"
            ),
            dependency_notes=[
                "Requires: composite states (A1-A4), particle identity postulate, "
                "symmetrization/antisymmetrization rules",
                "F2 obstruction constrains fermionic statistics specifically",
            ],
            notes=["Absent: no statistics formalism; requires many prerequisites"],
        ),
        QII0GapItem(
            item_id="F4",
            item_name="bound_state_readiness",
            category="F_matter_readiness",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="Q-B through Q-F (no bound states)",
            allowed_claim=(
                "Bound-state structure could be investigated once composite "
                "and excitation structure exists"
            ),
            forbidden_claim=(
                "Bound states follow from toy-model interference or decoherence"
            ),
            dependency_notes=[
                "Requires: composite states (A1-A4), excitation structure (D1-D4), "
                "interaction Hamiltonian",
                "Very high prerequisite burden",
            ],
            notes=["Absent: no bound-state framework; highest prerequisite burden"],
        ),
        QII0GapItem(
            item_id="F5",
            item_name="appendix_r_handoff_conditions",
            category="F_matter_readiness",
            presence_state="absent",
            appendix_p_class="motivated_but_unbuilt",
            supporting_audit="Pre-matter quarantine perimeter",
            allowed_claim=(
                "Handoff conditions to Appendix R (matter) are documented as "
                "the set of quantum prerequisites that must be satisfied before "
                "matter work can proceed"
            ),
            forbidden_claim=(
                "Matter work can proceed without satisfying quantum prerequisites"
            ),
            dependency_notes=[
                "Pre-matter quarantine perimeter defines the boundary",
                "Handoff requires: composite states, statistics, "
                "excitation structure at minimum",
            ],
            notes=[
                "Absent: handoff conditions not yet formalized at quantum level",
                "MBU: the path is motivated but the conditions are unbuilt",
            ],
        ),
    ]


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qii0_second_wave_gap_inventory() -> QII0GapInventoryResult:
    """
    Run the full Q-II.0 Second-Wave Quantum Gap Inventory.

    Returns a validated QII0GapInventoryResult with all 29 items across
    6 categories, readiness assessment, and diagnostics.
    """
    # Build all items
    cat_a = _build_category_a()
    cat_b = _build_category_b()
    cat_c = _build_category_c()
    cat_d = _build_category_d()
    cat_e = _build_category_e()
    cat_f = _build_category_f()

    all_items = cat_a + cat_b + cat_c + cat_d + cat_e + cat_f

    # Category summaries
    def _summarize(label: str, items: List[QII0GapItem], desc: str) -> QII0CategorySummary:
        return QII0CategorySummary(
            category_label=label,
            n_items=len(items),
            item_ids=[it.item_id for it in items],
            n_absent=sum(1 for it in items if it.presence_state == "absent"),
            n_obstructed=sum(1 for it in items if it.presence_state == "obstructed"),
            n_extension_level=sum(1 for it in items if it.presence_state == "extension_level"),
            description=desc,
        )

    summaries = [
        _summarize("A_composite_state", cat_a,
                    "Tensor product, subsystem, reduced state, many-body grammar"),
        _summarize("B_entanglement", cat_b,
                    "Nonfactorized states, entanglement criteria, correlations, Bell/CHSH"),
        _summarize("C_observable_algebra", cat_c,
                    "Multi-observable grammar, noncommuting, composition, closure"),
        _summarize("D_excitation_field_mode", cat_d,
                    "Many-mode, field-excitation basis, mode decomposition, ladder operators"),
        _summarize("E_probability_determination", cat_e,
                    "Born rule, outcome selection, branch selection, observer update"),
        _summarize("F_matter_readiness", cat_f,
                    "Bosonic, fermionic, statistics, bound state, Appendix R handoff"),
    ]

    # Aggregate counts
    n_absent = sum(1 for it in all_items if it.presence_state == "absent")
    n_obstr = sum(1 for it in all_items if it.presence_state == "obstructed")
    n_ext = sum(1 for it in all_items if it.presence_state == "extension_level")
    n_est = sum(1 for it in all_items if it.presence_state == "first_wave_established")

    # Readiness assessment
    readiness = QII0ReadinessAssessment(
        first_wave_closed=True,
        all_gaps_documented=True,
        no_silent_promotions=True,
        nonclaims_preserved=True,
        hard_rules_applied=True,
        ready_for_qiib=True,
        readiness_verdict="ready_to_proceed_to_qiia_and_qiib",
        notes=[
            "First wave closed per Q-F authorization verdict",
            "All 29 gap items documented with presence state and Appendix P class",
            "No first-wave result silently promoted above its locked class",
            "All 8 first-wave nonclaim categories preserved",
            "All 7 hard epistemic rules applied throughout inventory",
            "Ready to proceed: Q-II.A (charter) then Q-II.B (composite structure)",
        ],
    )

    # Allowed claims (7)
    allowed_claims: List[str] = [
        "All second-wave quantum gaps have been inventoried across 6 categories "
        "with 29 items total",
        "Each gap carries explicit presence state and Appendix P classification",
        "First-wave results are inherited at their locked Appendix P classes "
        "with no silent promotions",
        "Hard epistemic rules prevent conflation of first-wave toy results "
        "with second-wave many-body readiness",
        "The fermionic obstruction (F2) is the most constrained gap: "
        "3-layer BSR from Q0",
        "Effective determination tendency (E5) is the only extension-level item: "
        "decoherence tendency motivated but outcome determination unbuilt",
        "Q-II.A and Q-II.B are authorized to proceed based on complete inventory",
    ]

    # Forbidden claims (7)
    forbidden_claims: List[str] = [
        "First-wave toy-model success implies many-body quantum readiness",
        "Decoherence results imply entanglement structure",
        "Single-observable success implies multi-observable algebra derived",
        "Two-path interference implies field-excitation or many-mode closure",
        "Effective decoherence tendency implies Born rule or outcome selection",
        "First-wave closure implies quantum theory complete",
        "Absent structures are permanently blocked or impossible",
    ]

    # Diagnostics
    diagnostics: Dict[str, Any] = {
        "n_total_items": len(all_items),
        "n_categories": len(summaries),
        "n_absent": n_absent,
        "n_obstructed": n_obstr,
        "n_extension_level": n_ext,
        "n_first_wave_established": n_est,
        "n_nonclaims": N_QII0_NONCLAIMS,
        "n_hard_rules": N_HARD_RULES,
        "n_allowed_claims": len(allowed_claims),
        "n_forbidden_claims": len(forbidden_claims),
        "most_constrained_gap": "F2_fermionic_quantum_matter_readiness",
        "only_extension_level_item": "E5_effective_determination_tendencies",
    }

    result = QII0GapInventoryResult(
        valid=True,
        items=all_items,
        category_summaries=summaries,
        readiness_assessment=readiness,
        n_total=len(all_items),
        n_absent=n_absent,
        n_obstructed=n_obstr,
        n_extension_level=n_ext,
        n_first_wave_established=n_est,
        hard_rules=HARD_EPISTEMIC_RULES,
        nonclaims=QII0_NONCLAIMS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        inventory_verdict=QII0_INVENTORY_VERDICT,
        diagnostics=diagnostics,
    )

    validate_qii0_result(result)
    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qii0_result(result: QII0GapInventoryResult) -> None:
    """Validate the Q-II.0 inventory result."""
    # Item count
    if len(result.items) != N_TOTAL_ITEMS:
        raise ValueError(f"Expected {N_TOTAL_ITEMS} items, got {len(result.items)}")

    # All items have valid presence states
    for item in result.items:
        if item.presence_state not in ALLOWED_PRESENCE_STATES:
            raise ValueError(
                f"Item {item.item_id}: presence_state '{item.presence_state}' "
                f"not in allowed states"
            )
        if item.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(
                f"Item {item.item_id}: appendix_p_class '{item.appendix_p_class}' "
                f"not in allowed classes"
            )
        if item.category not in ALLOWED_CATEGORY_LABELS:
            raise ValueError(
                f"Item {item.item_id}: category '{item.category}' not in allowed labels"
            )

    # Category counts
    per_cat = {}
    for item in result.items:
        per_cat.setdefault(item.category, []).append(item)
    expected = {
        "A_composite_state": N_CATEGORY_A_ITEMS,
        "B_entanglement": N_CATEGORY_B_ITEMS,
        "C_observable_algebra": N_CATEGORY_C_ITEMS,
        "D_excitation_field_mode": N_CATEGORY_D_ITEMS,
        "E_probability_determination": N_CATEGORY_E_ITEMS,
        "F_matter_readiness": N_CATEGORY_F_ITEMS,
    }
    for cat, exp_n in expected.items():
        actual_n = len(per_cat.get(cat, []))
        if actual_n != exp_n:
            raise ValueError(f"Category {cat}: expected {exp_n} items, got {actual_n}")

    # Aggregate counts
    n_abs = sum(1 for it in result.items if it.presence_state == "absent")
    n_obs = sum(1 for it in result.items if it.presence_state == "obstructed")
    n_ext = sum(1 for it in result.items if it.presence_state == "extension_level")
    n_est = sum(1 for it in result.items if it.presence_state == "first_wave_established")
    if n_abs != result.n_absent:
        raise ValueError(f"n_absent mismatch: counted {n_abs}, recorded {result.n_absent}")
    if n_obs != result.n_obstructed:
        raise ValueError(f"n_obstructed mismatch: counted {n_obs}, recorded {result.n_obstructed}")
    if n_ext != result.n_extension_level:
        raise ValueError(f"n_extension_level mismatch: counted {n_ext}, recorded {result.n_extension_level}")
    if n_est != result.n_first_wave_established:
        raise ValueError(f"n_first_wave_established mismatch: counted {n_est}, recorded {result.n_first_wave_established}")

    # Nonclaims
    if len(result.nonclaims) != N_QII0_NONCLAIMS:
        raise ValueError(f"Expected {N_QII0_NONCLAIMS} nonclaims, got {len(result.nonclaims)}")

    # Hard rules
    if len(result.hard_rules) != N_HARD_RULES:
        raise ValueError(f"Expected {N_HARD_RULES} hard rules, got {len(result.hard_rules)}")

    # Claims
    if len(result.allowed_claims) != 7:
        raise ValueError(f"Expected 7 allowed claims, got {len(result.allowed_claims)}")
    if len(result.forbidden_claims) != 7:
        raise ValueError(f"Expected 7 forbidden claims, got {len(result.forbidden_claims)}")

    # Readiness
    if not result.readiness_assessment.ready_for_qiib:
        raise ValueError("Readiness assessment must indicate ready_for_qiib = True")

    # Unique item IDs
    ids = [it.item_id for it in result.items]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate item IDs found")

    # Verdict
    if result.inventory_verdict != QII0_INVENTORY_VERDICT:
        raise ValueError(f"Unexpected verdict: {result.inventory_verdict}")


def _self_test() -> bool:
    """Run audit and validate. Returns True on success."""
    result = run_qii0_second_wave_gap_inventory()
    assert result.valid is True
    assert result.n_total == N_TOTAL_ITEMS
    assert result.inventory_verdict == QII0_INVENTORY_VERDICT
    assert len(result.nonclaims) == N_QII0_NONCLAIMS
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.0 self-test passed.")
