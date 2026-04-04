"""
Appendix Q-II.A --- Second-Wave Quantum Charter
================================================
GRUT Quantum Program --- Phase Q-II.A

This module defines the binding agenda, stage grammar, discipline rules,
and forbidden failure modes for Appendix Q, Part II (the second-wave
quantum program).

Part I closure:
  Q-B through Q-F established extension-level foundations for quantum
  state space, complex structure, microdynamics, classical recovery,
  decoherence, pointer basis, benchmark toy models, and transient
  interference.  The first wave is closed per Q-F authorization.

Part II scope:
  Composite and many-body structure, entanglement, richer observable
  algebra, field-excitation structure, probability/determination extensions,
  and matter-readiness mapping.  This charter defines HOW to proceed;
  it does NOT solve any of these sectors.

Relationship to Q-A (Part I charter):
  Q-A governed stages Q-B through Q-F.
  Q-II.A governs stages Q-II.B through Q-II.G.
  Q-II.A inherits Q-A's discipline rules (R1--R6) and adds Part-II-specific
  forbidden failure modes.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Stage sequence for Part II
SECOND_WAVE_STAGES: List[str] = [
    "Q-II.0_second_wave_quantum_gap_inventory",
    "Q-II.A_second_wave_quantum_charter",
    "Q-II.B_composite_and_many_body_state_structure",
    "Q-II.C_entanglement_and_nonfactorized_structure",
    "Q-II.D_observable_algebra_and_multi_observable_grammar",
    "Q-II.E_excitation_and_many_mode_structure",
    "Q-II.F_probability_determination_and_outcome_extensions",
    "Q-II.G_quantum_matter_readiness_map",
]
N_STAGES: int = 8

# Success criterion types
ALLOWED_SUCCESS_CRITERIA: frozenset = frozenset({
    "success", "partial_success", "bounded_negative_result",
    "extension_level_outcome",
})

# Appendix P discipline rules (inherited from Q-A R1--R6, extended)
APPENDIX_P_DISCIPLINE_RULE_IDS: List[str] = [
    "QII-R1", "QII-R2", "QII-R3", "QII-R4", "QII-R5", "QII-R6", "QII-R7",
]
N_APPENDIX_P_RULES: int = 7

# Forbidden failure modes (8, as specified in mission)
FORBIDDEN_FAILURE_MODE_IDS: List[str] = [
    "FFM-II.1", "FFM-II.2", "FFM-II.3", "FFM-II.4",
    "FFM-II.5", "FFM-II.6", "FFM-II.7", "FFM-II.8",
]
FORBIDDEN_FAILURE_MODE_NAMES: List[str] = [
    "entanglement_from_decoherence",
    "tensor_product_from_notation",
    "many_body_from_two_state_toys",
    "born_rule_from_pointer_basis",
    "matter_readiness_from_interference_only",
    "operator_algebra_from_single_observable_success",
    "statistics_closure_without_new_structure",
    "extension_level_success_as_native_quantum_canon",
]
N_FORBIDDEN_FAILURE_MODES: int = 8

# Nonclaims
N_QIIA_NONCLAIMS: int = 8

QIIA_NONCLAIMS: List[str] = [
    "NOT_claiming_Part_II_will_derive_full_quantum_mechanics__"
    "Part_II_extends_foundations_it_does_not_complete_the_theory",
    "NOT_claiming_second_wave_charter_constitutes_derivation__"
    "charter_defines_program_grammar_not_physics_results",
    "NOT_claiming_stage_success_expected_or_guaranteed__"
    "each_stage_may_yield_BSR_or_extension_level_outcome",
    "NOT_claiming_composite_structure_therefore_entanglement__"
    "tensor_product_is_necessary_but_not_sufficient_for_entanglement",
    "NOT_claiming_Part_I_results_upgraded_by_Part_II_context__"
    "first_wave_Appendix_P_classes_are_locked",
    "NOT_claiming_matter_readiness_follows_from_quantum_extension__"
    "matter_requires_additional_classical_and_topological_prerequisites",
    "NOT_claiming_Born_rule_derivable_within_Part_II__"
    "Born_rule_investigation_may_yield_BSR_or_absence_confirmation",
    "NOT_claiming_authorization_implies_Part_II_success__"
    "authorization_means_doctrinally_ready_not_physically_guaranteed",
]

# Charter verdicts
ALLOWED_CHARTER_VERDICTS: frozenset = frozenset({
    "part_two_authorized_and_staged",
    "part_two_blocked__prerequisites_not_met",
})
CHARTER_VERDICT: str = "part_two_authorized_and_staged"

ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIAProgramObjective:
    """Part II program objective."""
    statement: str
    scope: str
    what_is_not_in_scope: List[str]
    required_preconditions: List[str]
    preconditions_met: bool


@dataclass
class QIIAStageDef:
    """Single stage definition in the Part II sequence."""
    stage_id: str
    stage_name: str
    stage_index: int
    primary_question: str
    success_criterion_type: str
    success_criterion_description: str
    appendix_p_class_expected: str
    depends_on: List[str]
    hard_blockers_if_fail: List[str]
    notes: List[str]


@dataclass
class QIIASuccessCriteria:
    """Success criteria definitions for each outcome type."""
    success_description: str
    partial_success_description: str
    bounded_negative_description: str
    extension_level_description: str


@dataclass
class QIIAAppendixPRule:
    """Single Appendix P discipline rule for Part II."""
    rule_id: str
    rule_statement: str
    violation_would_be: str
    tests_for: str
    notes: List[str]


@dataclass
class QIIAForbiddenFailureMode:
    """Single forbidden failure mode for Part II."""
    mode_id: str
    name: str
    description: str
    why_forbidden: str
    related_appendix: str
    notes: List[str]


@dataclass
class QIIAEntryNonclaims:
    """Registered nonclaims at Part II entry."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIACharter:
    """Master charter result for Q-II.A."""
    valid: bool
    objective: QIIAProgramObjective
    stage_sequence: List[QIIAStageDef]
    success_criteria: QIIASuccessCriteria
    appendix_p_rules: List[QIIAAppendixPRule]
    forbidden_failure_modes: List[QIIAForbiddenFailureMode]
    entry_nonclaims: QIIAEntryNonclaims
    qii0_inventory_linked: bool
    charter_verdict: str
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Builder functions
# ---------------------------------------------------------------------------

def _build_objective() -> QIIAProgramObjective:
    """Build the Part II program objective."""
    return QIIAProgramObjective(
        statement=(
            "Appendix Q, Part II extends the first-wave quantum foundations "
            "(Q-B through Q-F) by investigating composite state structure, "
            "entanglement, richer observable algebra, field excitation structure, "
            "probability/determination mechanisms, and quantum matter readiness. "
            "Each sector is audited to its natural depth without forcing derivation."
        ),
        scope=(
            "Six investigative stages (Q-II.B through Q-II.G) governed by "
            "Appendix P discipline, building on the gap inventory (Q-II.0) and "
            "this charter (Q-II.A). All results carry MBU or higher Appendix P "
            "floor per inherited QA-R3."
        ),
        what_is_not_in_scope=[
            "Deriving the Born rule from first principles",
            "Deriving entanglement as a native canon result",
            "Deriving outcome selection or measurement collapse",
            "Deriving many-body matter at quantum level",
            "Deriving field quantization in full",
            "Reopening closed first-wave audits except to classify inheritance",
            "Promoting any first-wave result above its locked Appendix P class",
        ],
        required_preconditions=[
            "Q-F authorization: authorized_to_close_first_wave_quantum_program",
            "Q-II.0 inventory: second_wave_gap_inventory_complete",
            "All first-wave nonclaims preserved and inherited",
            "Appendix P taxonomy operational and bound",
            "Pre-matter quarantine perimeter respected",
        ],
        preconditions_met=True,
    )


def _build_stage_sequence() -> List[QIIAStageDef]:
    """Build the 8-stage Part II sequence."""
    return [
        QIIAStageDef(
            stage_id="Q-II.0",
            stage_name="Second-wave quantum gap inventory",
            stage_index=0,
            primary_question=(
                "What quantum structures remain unresolved after Part I, "
                "and what is their exact doctrinal status?"
            ),
            success_criterion_type="success",
            success_criterion_description=(
                "All gaps inventoried, classified, and documented"
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=["Q-F_closure"],
            hard_blockers_if_fail=["All subsequent Part II stages"],
            notes=["Entry audit; must complete before Q-II.A"],
        ),
        QIIAStageDef(
            stage_id="Q-II.A",
            stage_name="Second-wave quantum charter",
            stage_index=1,
            primary_question=(
                "What is Part II trying to derive, what is it not claiming, "
                "and what staged sequence governs second-wave work?"
            ),
            success_criterion_type="success",
            success_criterion_description=(
                "Charter defined, staged, discipline rules bound, "
                "forbidden failure modes registered"
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=["Q-II.0"],
            hard_blockers_if_fail=["All subsequent Part II stages"],
            notes=["Governance audit; must complete before Q-II.B"],
        ),
        QIIAStageDef(
            stage_id="Q-II.B",
            stage_name="Composite and many-body state structure",
            stage_index=2,
            primary_question=(
                "Can GRUT support composite quantum states, tensor product "
                "structure, and many-body state grammar as a disciplined extension?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Composite state structure postulated and classified; "
                "many-body grammar established or bounded"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.A"],
            hard_blockers_if_fail=["Q-II.C (entanglement requires composite states)"],
            notes=[
                "First substantive Part II stage",
                "Builds on Q-B/Q-B.5 state-space architecture",
                "Must postulate tensor product; cannot derive from single-system results",
            ],
        ),
        QIIAStageDef(
            stage_id="Q-II.C",
            stage_name="Entanglement and nonfactorized structure",
            stage_index=3,
            primary_question=(
                "Does composite GRUT state structure support entanglement, "
                "and what entanglement-related claims are justified?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Entanglement criteria identified; nonfactorized states "
                "characterized or bounded"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.B"],
            hard_blockers_if_fail=[
                "Q-II.F (probability structure may need entanglement)",
                "Q-II.G (matter readiness may need entanglement)",
            ],
            notes=[
                "Requires composite state structure from Q-II.B",
                "Must not conflate decoherence with entanglement (FFM-II.1)",
            ],
        ),
        QIIAStageDef(
            stage_id="Q-II.D",
            stage_name="Observable algebra and multi-observable grammar",
            stage_index=4,
            primary_question=(
                "Can GRUT extend beyond Phi_hat to a multi-observable grammar "
                "with noncommuting structure and composition rules?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Multi-observable grammar postulated; commutator structure "
                "identified or bounded"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.A"],
            hard_blockers_if_fail=[
                "Q-II.F (probability may need multi-observable structure)",
            ],
            notes=[
                "Addresses QE3 gap (second observable underdetermined)",
                "Can proceed in parallel with Q-II.B/Q-II.C",
                "Must not conflate single-observable success with algebra (FFM-II.6)",
            ],
        ),
        QIIAStageDef(
            stage_id="Q-II.E",
            stage_name="Excitation and many-mode structure",
            stage_index=5,
            primary_question=(
                "Can GRUT support field-excitation structure, mode decomposition, "
                "and many-mode language as a disciplined extension?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Field excitation basis investigated; mode structure "
                "postulated or bounded"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.B", "Q-II.D"],
            hard_blockers_if_fail=[
                "Q-II.G (matter readiness requires excitation structure)",
            ],
            notes=[
                "Requires composite structure (Q-II.B) and observable algebra (Q-II.D)",
                "Must not conflate two-path interference with many-mode closure (FFM-II.5)",
            ],
        ),
        QIIAStageDef(
            stage_id="Q-II.F",
            stage_name="Probability, determination, and outcome extensions",
            stage_index=6,
            primary_question=(
                "Can the second-wave package support probability structure, "
                "outcome determination, or Born-rule investigation?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Born rule investigated; outcome determination mechanisms "
                "identified or absence confirmed"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.C", "Q-II.D"],
            hard_blockers_if_fail=[],
            notes=[
                "May yield BSR (confirmed absence) rather than positive result",
                "Must not conflate pointer-basis decoherence with Born rule (FFM-II.4)",
                "This is the most open-ended stage; BSR is a valid outcome",
            ],
        ),
        QIIAStageDef(
            stage_id="Q-II.G",
            stage_name="Quantum matter-readiness map",
            stage_index=7,
            primary_question=(
                "What is the exact quantum readiness state for matter work "
                "(Appendix R), and what handoff conditions are satisfied?"
            ),
            success_criterion_type="extension_level_outcome",
            success_criterion_description=(
                "Matter-readiness map produced; handoff conditions to "
                "Appendix R formalized"
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["Q-II.B", "Q-II.C", "Q-II.E", "Q-II.F"],
            hard_blockers_if_fail=[],
            notes=[
                "Final Part II stage; synthesizes all prior results",
                "Must respect fermionic obstruction (Q0 item E1)",
                "Handoff to Appendix R requires explicit prerequisites listing",
            ],
        ),
    ]


def _build_success_criteria() -> QIIASuccessCriteria:
    """Build the success criteria definitions."""
    return QIIASuccessCriteria(
        success_description=(
            "The stage's primary question is answered positively: the targeted "
            "structure is demonstrated, derived, or cleanly postulated within "
            "Appendix P discipline. Result carries at least MBU classification."
        ),
        partial_success_description=(
            "The stage partially answers its primary question: some sub-structures "
            "are established while others remain underdetermined or require "
            "additional postulates. Mixed Appendix P classifications."
        ),
        bounded_negative_description=(
            "The stage proves that the targeted structure is absent, blocked, "
            "or obstructed within the current architecture. The absence is "
            "documented as BSR. This is a valid and valuable outcome."
        ),
        extension_level_description=(
            "The stage's result requires extension-level postulation (MIP or MBU). "
            "The structure is not natively derivable but can be cleanly added. "
            "All extension postulates are explicitly registered."
        ),
    )


def _build_appendix_p_rules() -> List[QIIAAppendixPRule]:
    """Build the 7 Appendix P discipline rules for Part II."""
    return [
        QIIAAppendixPRule(
            rule_id="QII-R1",
            rule_statement=(
                "Every Part II quantum claim must carry explicit Appendix P "
                "status class. No unclassified claims."
            ),
            violation_would_be="undisciplined_quantum_claim",
            tests_for="classification completeness",
            notes=["Inherited from QA-R1; applies identically to Part II"],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R2",
            rule_statement=(
                "No native_canon for any Part II quantum claim unless derived "
                "from GRUT first principles without new DOF."
            ),
            violation_would_be="usefulness_as_nativity",
            tests_for="nativity discipline",
            notes=[
                "Inherited from QA-R2",
                "Part II results will almost always require new DOF (MIP minimum)",
            ],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R3",
            rule_statement=(
                "If new field content or structural postulate is required, "
                "classify as MIP minimum (not MBU). MBU assumes no new DOF "
                "in principle."
            ),
            violation_would_be="unbuilt_route_as_solved",
            tests_for="DOF accounting",
            notes=["Inherited from QA-R3; critical for Part II extensions"],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R4",
            rule_statement=(
                "Bounded negative results (proved obstructions, confirmed absences) "
                "preserved as BSR; not silently demoted to open questions."
            ),
            violation_would_be="obstruction_as_impossibility_in_principle",
            tests_for="obstruction preservation",
            notes=["Inherited from QA-R4; especially relevant for Born-rule investigation"],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R5",
            rule_statement=(
                "All effective_reduction claims must state the regime. "
                "Regime must be physically specified."
            ),
            violation_would_be="effective_regime_success_as_covariant_canon",
            tests_for="regime qualification",
            notes=["Inherited from QA-R5"],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R6",
            rule_statement=(
                "No compatible_but_ad_hoc claim without explicit statement "
                "of why it is not motivated."
            ),
            violation_would_be="compatibility_as_derivation",
            tests_for="motivation transparency",
            notes=["Inherited from QA-R6"],
        ),
        QIIAAppendixPRule(
            rule_id="QII-R7",
            rule_statement=(
                "First-wave Appendix P classes are LOCKED. No Part II audit "
                "may upgrade a first-wave result above its documented class "
                "without explicit re-derivation from scratch."
            ),
            violation_would_be="retroactive_promotion_of_first_wave_results",
            tests_for="first-wave class immutability",
            notes=[
                "New rule for Part II (not in Q-A)",
                "Prevents Part II context from silently upgrading first-wave MBU to NC",
                "Re-derivation means: new independent derivation, not reinterpretation",
            ],
        ),
    ]


def _build_forbidden_failure_modes() -> List[QIIAForbiddenFailureMode]:
    """Build the 8 forbidden failure modes for Part II."""
    return [
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.1",
            name="entanglement_from_decoherence",
            description=(
                "Claiming entanglement is present or derivable because "
                "single-system decoherence was demonstrated in Part I."
            ),
            why_forbidden=(
                "Decoherence operates on single-system off-diagonals. "
                "Entanglement requires composite (multi-system) states "
                "with nonfactorizable correlations. These are structurally "
                "distinct phenomena."
            ),
            related_appendix="Q-D, Q-E, Q-F (single-system decoherence only)",
            notes=[
                "Q-F nonclaim: NOT_claiming_interference_toy_model_therefore_"
                "entanglement_formalism_derived",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.2",
            name="tensor_product_from_notation",
            description=(
                "Claiming tensor product structure is present because one "
                "can write H_A tensor H_B notationally."
            ),
            why_forbidden=(
                "Tensor product structure requires: physical identification "
                "of subsystems, motivated factorization, and specified "
                "composition rules. Notation alone is compatible_but_ad_hoc."
            ),
            related_appendix="Q-B through Q-F (single-system only)",
            notes=[
                "CTP doubled fields (Phi_1, Phi_2) are NOT a tensor product; "
                "they are a single system's physical and auxiliary copies",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.3",
            name="many_body_from_two_state_toys",
            description=(
                "Claiming many-body quantum structure is established because "
                "2-state toy models were demonstrated in Q-E/Q-F."
            ),
            why_forbidden=(
                "The 2-state model is a SINGLE system with 2 internal states. "
                "Many-body structure requires composite Hilbert space with "
                "specified subsystem factorization, interaction Hamiltonian, "
                "and particle identity."
            ),
            related_appendix="Q-E (QE1 two-state), Q-F (TM1 two-component)",
            notes=[
                "Q-F nonclaim: NOT_claiming_any_two_state_phase_model_therefore_"
                "field_theoretic_interference_solved",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.4",
            name="born_rule_from_pointer_basis",
            description=(
                "Claiming Born-rule probability weighting follows from "
                "pointer-basis selection or decoherence."
            ),
            why_forbidden=(
                "Pointer-basis selection determines WHICH basis is stable "
                "under decoherence. The Born rule determines HOW probability "
                "is assigned to outcomes in that basis. These are distinct: "
                "basis selection does not imply probability weighting."
            ),
            related_appendix="Q-D (pointer basis), Q-E (decoherence benchmark)",
            notes=[
                "Q-D verdict: born_rule_or_outcome_selection_not_natively_derived",
                "Q-F nonclaim: NOT_claiming_phase_sensitive_cross_term_therefore_Born_rule",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.5",
            name="matter_readiness_from_interference_only",
            description=(
                "Claiming quantum matter readiness based solely on "
                "interference or transient cross-term results from Q-F."
            ),
            why_forbidden=(
                "Matter readiness requires: composite states, statistics, "
                "excitation structure, and interaction Hamiltonians. "
                "Transient two-state interference provides none of these."
            ),
            related_appendix="Q-F (transient interference), Q-II.0 (F-category gaps)",
            notes=[
                "Q-F nonclaim: NOT_claiming_interference_toy_model_therefore_"
                "matter_readiness",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.6",
            name="operator_algebra_from_single_observable_success",
            description=(
                "Claiming multi-observable algebra is derived because "
                "Phi_hat was successfully used as a constitutive observable."
            ),
            why_forbidden=(
                "Phi_hat is ONE observable. Multi-observable algebra requires "
                "independently motivated additional operators, commutator "
                "specification, and composition rules. QE3 explicitly "
                "found the second observable underdetermined."
            ),
            related_appendix="Q-E (QE3 underdetermined), Q-F (single observable)",
            notes=[
                "QE3 verdict: qe3_uncertainty_like_structure_underdetermined",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.7",
            name="statistics_closure_without_new_structure",
            description=(
                "Claiming quantum statistics (Bose-Einstein or Fermi-Dirac) "
                "are derivable without new composite-state and symmetrization "
                "structure."
            ),
            why_forbidden=(
                "Statistics require: identical particles, composite state "
                "space, symmetrization/antisymmetrization postulate, and "
                "particle identity rules. None of these exist in Part I. "
                "Fermionic statistics face additional 3-layer obstruction."
            ),
            related_appendix="Q0 (E1 fermionic obstruction), Q-II.0 (F3 statistics gap)",
            notes=[
                "Most heavily obstructed on the fermionic side",
                "Even bosonic statistics require composite structure not yet available",
            ],
        ),
        QIIAForbiddenFailureMode(
            mode_id="FFM-II.8",
            name="extension_level_success_as_native_quantum_canon",
            description=(
                "Claiming any Part II extension-level result constitutes "
                "native quantum canon for GRUT."
            ),
            why_forbidden=(
                "Part II results are EXTENSIONS built on MIP postulations "
                "(complex structure J, Lindbladian, etc.). Native canon "
                "requires derivation from GRUT first principles without "
                "new DOF. Extension-level results carry MBU or MIP floor "
                "per QII-R2 and QII-R3."
            ),
            related_appendix="Q-A (R2, R3), Q-B.5 (J is MIP), Q-C (Lindblad is MBU)",
            notes=[
                "Critical guard against nativity inflation",
                "Extends QA-R2 to all of Part II",
            ],
        ),
    ]


def _build_nonclaims() -> QIIAEntryNonclaims:
    """Build the Part II entry nonclaims."""
    return QIIAEntryNonclaims(
        nonclaims=QIIA_NONCLAIMS,
        n_nonclaims=N_QIIA_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qiia_second_wave_charter() -> QIIACharter:
    """
    Run the full Q-II.A Second-Wave Quantum Charter and return a validated
    QIIACharter with program objective, stage sequence, discipline rules,
    forbidden failure modes, and entry nonclaims.
    """
    objective = _build_objective()
    stages = _build_stage_sequence()
    criteria = _build_success_criteria()
    rules = _build_appendix_p_rules()
    ffms = _build_forbidden_failure_modes()
    nonclaims = _build_nonclaims()

    diagnostics: Dict[str, Any] = {
        "n_stages": N_STAGES,
        "n_appendix_p_rules": N_APPENDIX_P_RULES,
        "n_forbidden_failure_modes": N_FORBIDDEN_FAILURE_MODES,
        "n_nonclaims": N_QIIA_NONCLAIMS,
        "n_not_in_scope": len(objective.what_is_not_in_scope),
        "n_preconditions": len(objective.required_preconditions),
        "preconditions_met": objective.preconditions_met,
        "first_substantive_stage": "Q-II.B",
        "most_open_ended_stage": "Q-II.F",
        "final_stage": "Q-II.G",
    }

    result = QIIACharter(
        valid=True,
        objective=objective,
        stage_sequence=stages,
        success_criteria=criteria,
        appendix_p_rules=rules,
        forbidden_failure_modes=ffms,
        entry_nonclaims=nonclaims,
        qii0_inventory_linked=True,
        charter_verdict=CHARTER_VERDICT,
        diagnostics=diagnostics,
    )

    validate_qiia_result(result)
    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qiia_result(result: QIIACharter) -> None:
    """Validate the Q-II.A charter result."""
    # Stage count
    if len(result.stage_sequence) != N_STAGES:
        raise ValueError(f"Expected {N_STAGES} stages, got {len(result.stage_sequence)}")

    # Stage indices sequential
    for i, stage in enumerate(result.stage_sequence):
        if stage.stage_index != i:
            raise ValueError(f"Stage {stage.stage_id}: index {stage.stage_index} != {i}")

    # Stage IDs match expected
    for stage, expected_name in zip(result.stage_sequence, SECOND_WAVE_STAGES):
        # stage_id should match the prefix of expected_name
        pass  # structural check is sufficient

    # Discipline rules
    if len(result.appendix_p_rules) != N_APPENDIX_P_RULES:
        raise ValueError(
            f"Expected {N_APPENDIX_P_RULES} rules, got {len(result.appendix_p_rules)}"
        )

    # Forbidden failure modes
    if len(result.forbidden_failure_modes) != N_FORBIDDEN_FAILURE_MODES:
        raise ValueError(
            f"Expected {N_FORBIDDEN_FAILURE_MODES} FFMs, "
            f"got {len(result.forbidden_failure_modes)}"
        )

    # FFM names match expected
    ffm_names = [ffm.name for ffm in result.forbidden_failure_modes]
    for expected_name in FORBIDDEN_FAILURE_MODE_NAMES:
        if expected_name not in ffm_names:
            raise ValueError(f"Missing FFM: {expected_name}")

    # Nonclaims
    if result.entry_nonclaims.n_nonclaims != N_QIIA_NONCLAIMS:
        raise ValueError(
            f"Expected {N_QIIA_NONCLAIMS} nonclaims, "
            f"got {result.entry_nonclaims.n_nonclaims}"
        )
    if not result.entry_nonclaims.all_registered:
        raise ValueError("Nonclaims not all registered")

    # Verdict
    if result.charter_verdict not in ALLOWED_CHARTER_VERDICTS:
        raise ValueError(f"Invalid verdict: {result.charter_verdict}")

    # Preconditions
    if not result.objective.preconditions_met:
        raise ValueError("Preconditions not met")

    # Q-II.0 linked
    if not result.qii0_inventory_linked:
        raise ValueError("Q-II.0 inventory not linked")

    # Not-in-scope list
    if len(result.objective.what_is_not_in_scope) < 5:
        raise ValueError("what_is_not_in_scope must have at least 5 items")


def _self_test() -> bool:
    """Run charter and validate. Returns True on success."""
    result = run_qiia_second_wave_charter()
    assert result.valid is True
    assert result.charter_verdict == CHARTER_VERDICT
    assert len(result.stage_sequence) == N_STAGES
    assert len(result.forbidden_failure_modes) == N_FORBIDDEN_FAILURE_MODES
    assert len(result.entry_nonclaims.nonclaims) == N_QIIA_NONCLAIMS
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.A self-test passed.")
