"""
Appendix R-A --- Matter Program Charter
========================================
GRUT Matter Program --- Phase R-A

This module defines the binding agenda, stage grammar, discipline rules,
and forbidden failure modes for Appendix R (the GRUT Matter Program).

Appendix R builds on:
  - Appendix Q, Parts I and II (quantum foundations)
  - Appendices M, N, O (bosonic object support, Skyrme nativity, O(3) nativity)
  - Appendix R0 (matter entry inventory)

The matter program investigates whether GRUT can support particle-like
objects, bound structures, statistics, and eventually chemistry-relevant
matter, while honestly documenting where the theory reaches its current
boundaries.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MATTER_PROGRAM_STAGES: List[str] = [
    "R0_matter_entry_inventory",
    "R-A_matter_program_charter",
    "R-B_bosonic_objecthood_and_localization",
    "R-C_stabilization_and_bound_structure",
    "R-D_composite_matter_and_pre_atomic_structure",
    "R-E_fermionic_matter_boundary_and_extension_routes",
    "R-F_statistics_probability_and_matter_interpretation",
    "R-G_matter_readiness_to_chemistry_bridge",
]
N_STAGES: int = 8

ALLOWED_SUCCESS_CRITERIA: frozenset = frozenset({
    "success", "partial_success", "bounded_negative_result",
    "extension_level_outcome",
})

APPENDIX_P_DISCIPLINE_RULE_IDS: List[str] = [
    "R-R1", "R-R2", "R-R3", "R-R4", "R-R5", "R-R6", "R-R7", "R-R8",
]
N_APPENDIX_P_RULES: int = 8

FORBIDDEN_FAILURE_MODE_IDS: List[str] = [
    "FFM-R.1", "FFM-R.2", "FFM-R.3", "FFM-R.4",
    "FFM-R.5", "FFM-R.6", "FFM-R.7", "FFM-R.8",
]
FORBIDDEN_FAILURE_MODE_NAMES: List[str] = [
    "particle_from_excitation_grammar",
    "bound_states_from_composite_notation",
    "fermions_from_second_wave_quantum_by_default",
    "born_rule_smuggled_into_matter",
    "bosonic_extension_as_native_matter_canon",
    "many_mode_as_continuum_matter_closure",
    "localized_benchmark_as_particle_ontology",
    "chemistry_readiness_from_matter_entry_only",
]
N_FORBIDDEN_FAILURE_MODES: int = 8

N_RA_NONCLAIMS: int = 8

RA_NONCLAIMS: List[str] = [
    "NOT_claiming_matter_program_will_derive_full_particle_physics__"
    "matter_program_extends_foundations_not_completes_particle_theory",
    "NOT_claiming_matter_charter_constitutes_derivation__"
    "charter_defines_program_grammar_not_physics_results",
    "NOT_claiming_stage_success_expected_or_guaranteed__"
    "each_stage_may_yield_BSR_or_extension_level_outcome",
    "NOT_claiming_bosonic_objecthood_therefore_particles__"
    "localized_objects_are_not_particles_without_full_ontology",
    "NOT_claiming_quantum_inheritance_upgraded_by_matter_context__"
    "Q_Appendix_P_classes_are_locked_in_R",
    "NOT_claiming_stabilization_therefore_bound_states__"
    "topological_stabilization_is_not_binding_mechanism",
    "NOT_claiming_fermionic_route_available__"
    "3_layer_obstruction_unchanged_unless_explicitly_overturned",
    "NOT_claiming_authorization_implies_matter_success__"
    "authorization_means_doctrinally_ready_not_physically_guaranteed",
]

ALLOWED_CHARTER_VERDICTS: frozenset = frozenset({
    "matter_program_authorized_and_staged",
    "matter_program_blocked__prerequisites_not_met",
})
CHARTER_VERDICT: str = "matter_program_authorized_and_staged"

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
class RAProgramObjective:
    statement: str
    scope: str
    what_is_not_in_scope: List[str]
    required_preconditions: List[str]
    preconditions_met: bool


@dataclass
class RAStageDef:
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
class RASuccessCriteria:
    success_description: str
    partial_success_description: str
    bounded_negative_description: str
    extension_level_description: str


@dataclass
class RAAppendixPRule:
    rule_id: str
    rule_statement: str
    violation_would_be: str
    tests_for: str
    notes: List[str]


@dataclass
class RAForbiddenFailureMode:
    mode_id: str
    name: str
    description: str
    why_forbidden: str
    related_appendix: str
    notes: List[str]


@dataclass
class RAEntryNonclaims:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class RACharter:
    valid: bool
    objective: RAProgramObjective
    stage_sequence: List[RAStageDef]
    success_criteria: RASuccessCriteria
    appendix_p_rules: List[RAAppendixPRule]
    forbidden_failure_modes: List[RAForbiddenFailureMode]
    entry_nonclaims: RAEntryNonclaims
    r0_inventory_linked: bool
    charter_verdict: str
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def _build_objective() -> RAProgramObjective:
    return RAProgramObjective(
        statement=(
            "Appendix R investigates whether GRUT can support matter-like structure "
            "-- bosonic objecthood, localization, stabilization, composite matter, "
            "and eventually a disciplined path toward chemistry-level phenomena -- "
            "building on the quantum foundations (Q Parts I/II) and classical "
            "bosonic object route (M/N/O)."
        ),
        scope=(
            "Six investigative stages (R-B through R-G) governed by Appendix P "
            "discipline, building on the matter entry inventory (R0) and this "
            "charter (R-A). All results carry MBU or higher floor per inherited "
            "Q/R discipline rules."
        ),
        what_is_not_in_scope=[
            "Deriving a complete particle physics from GRUT",
            "Deriving fermionic matter without overturning the 3-layer obstruction",
            "Deriving the Born rule from matter structure",
            "Deriving bound states without explicit binding mechanism",
            "Deriving chemistry without particles and bound states first",
            "Reopening closed Q or pre-matter audits except to classify inheritance",
            "Promoting extension-ready quantum results to native matter canon",
        ],
        required_preconditions=[
            "Q-II.G verdict: quantum_program_sufficient_to_open_matter_program",
            "Q-II.G verdict: appendix_R_authorized_with_explicit_extension_flags",
            "R0 inventory: matter_entry_inventory_complete",
            "Q-II.G handoff constraints carried verbatim",
            "Appendix P taxonomy operational",
            "Pre-matter quarantine perimeter respected",
        ],
        preconditions_met=True,
    )


def _build_stage_sequence() -> List[RAStageDef]:
    return [
        RAStageDef("R0", "Matter entry inventory", 0,
            "What matter-relevant ingredients are available at R entry?",
            "success", "All items inventoried and classified",
            "bounded_structural_result", ["Q-II.G_closure"],
            ["All subsequent R stages"],
            ["Entry audit; must complete before R-A"]),
        RAStageDef("R-A", "Matter program charter", 1,
            "What governs the matter program?",
            "success", "Charter defined and staged",
            "bounded_structural_result", ["R0"],
            ["All subsequent R stages"],
            ["Governance audit; must complete before R-B"]),
        RAStageDef("R-B", "Bosonic objecthood and localization", 2,
            "Can GRUT support bosonic localized objects at quantum level?",
            "extension_level_outcome",
            "Bosonic localized object investigated; quantum overlay assessed",
            "motivated_but_unbuilt", ["R-A"],
            ["R-C (stabilization requires objecthood)"],
            ["Builds on Appendix M Derrick + Appendix N Skyrme + Q-II.E excitations",
             "Must not assume particle ontology from classical localization"]),
        RAStageDef("R-C", "Stabilization and bound structure", 3,
            "Can GRUT localized objects be stabilized and bound?",
            "extension_level_outcome",
            "Stabilization mechanisms assessed; binding routes identified or bounded",
            "motivated_but_unbuilt", ["R-B"],
            ["R-D (composite matter requires stable objects)"],
            ["Builds on Appendix N Skyrme stabilization",
             "Must not assume bound states from composite grammar alone"]),
        RAStageDef("R-D", "Composite matter and pre-atomic structure", 4,
            "Can stable GRUT objects compose into pre-atomic structures?",
            "extension_level_outcome",
            "Composite matter structures investigated",
            "motivated_but_unbuilt", ["R-B", "R-C"],
            [],
            ["Builds on Q-II.B composite grammar + R-B/R-C stable objects",
             "Must not assume atomic structure from composite grammar"]),
        RAStageDef("R-E", "Fermionic matter boundary and extension routes", 5,
            "Is there any disciplined route to fermionic matter in GRUT?",
            "extension_level_outcome",
            "Fermionic obstruction re-assessed; extension routes identified or confirmed blocked",
            "bounded_structural_result", ["R-A"],
            [],
            ["May proceed in parallel with R-B through R-D",
             "Must preserve Q0 3-layer obstruction unless explicitly overturned",
             "BSR (confirmed block) is a valid and valuable outcome"]),
        RAStageDef("R-F", "Statistics, probability, and matter interpretation", 6,
            "What statistical and probabilistic structure supports matter?",
            "extension_level_outcome",
            "Statistics routes assessed; probability constraints formalized",
            "motivated_but_unbuilt", ["R-B", "R-E"],
            [],
            ["Builds on Q-II.F probability gap + R-E fermionic boundary",
             "Must not smuggle Born rule without explicit postulation"]),
        RAStageDef("R-G", "Matter readiness to chemistry bridge", 7,
            "What is the exact readiness state for chemistry-level work?",
            "extension_level_outcome",
            "Chemistry-readiness map produced",
            "motivated_but_unbuilt", ["R-B", "R-C", "R-D", "R-E", "R-F"],
            [],
            ["Final R stage; synthesizes all prior results",
             "Must document what chemistry can and cannot assume from R"]),
    ]


def _build_success_criteria() -> RASuccessCriteria:
    return RASuccessCriteria(
        success_description=(
            "The stage's primary question is answered positively: the targeted "
            "matter structure is demonstrated or cleanly postulated within "
            "Appendix P discipline."
        ),
        partial_success_description=(
            "Some matter sub-structures are established while others remain "
            "underdetermined or require additional postulates."
        ),
        bounded_negative_description=(
            "The stage proves that the targeted matter structure is absent, "
            "blocked, or obstructed within current architecture. BSR is a "
            "valid and valuable outcome."
        ),
        extension_level_description=(
            "The stage's result requires extension-level postulation (MIP/MBU). "
            "Not natively derivable but cleanly addable."
        ),
    )


def _build_appendix_p_rules() -> List[RAAppendixPRule]:
    return [
        RAAppendixPRule("R-R1",
            "Every matter claim must carry explicit Appendix P class.",
            "undisciplined_matter_claim", "classification completeness",
            ["Inherited from QA-R1 / QII-R1"]),
        RAAppendixPRule("R-R2",
            "No native_canon for matter claims unless derived from GRUT first "
            "principles without new DOF.",
            "usefulness_as_nativity", "nativity discipline",
            ["Matter results almost always require extension postulates"]),
        RAAppendixPRule("R-R3",
            "New field content or structural postulate requires MIP minimum.",
            "unbuilt_route_as_solved", "DOF accounting",
            ["Critical for binding mechanisms, stabilizers, etc."]),
        RAAppendixPRule("R-R4",
            "Bounded negatives preserved as BSR; not silently demoted.",
            "obstruction_as_impossibility_in_principle", "obstruction preservation",
            ["Especially relevant for fermionic obstruction"]),
        RAAppendixPRule("R-R5",
            "Effective_reduction claims must state the regime.",
            "effective_regime_success_as_covariant_canon", "regime qualification",
            ["Inherited from QA-R5"]),
        RAAppendixPRule("R-R6",
            "Compatible_but_ad_hoc requires explicit non-motivation statement.",
            "compatibility_as_derivation", "motivation transparency",
            ["Inherited from QA-R6"]),
        RAAppendixPRule("R-R7",
            "Q Appendix P classes are LOCKED. No R audit may upgrade a Q result "
            "above its documented class without explicit re-derivation.",
            "retroactive_promotion_of_quantum_results", "Q-class immutability",
            ["Inherited from QII-R7; extends to all of R"]),
        RAAppendixPRule("R-R8",
            "Classical matter results (M/N/O) carry their own locked classes. "
            "No R audit may promote classical MBU to quantum-derived native canon.",
            "classical_result_promotion", "classical-class immutability",
            ["New rule for R: protects M/N/O locked classes"]),
    ]


def _build_forbidden_failure_modes() -> List[RAForbiddenFailureMode]:
    return [
        RAForbiddenFailureMode("FFM-R.1", "particle_from_excitation_grammar",
            "Claiming particles exist because excitation grammar is available.",
            "Excitation grammar (sigma_+/sigma_-) is qubit bookkeeping, not particle "
            "ontology. Particles require Fock space, identity, dispersion.",
            "Q-II.E, Q-II.G",
            ["sigma_+ is qubit raising, not bosonic a^dag"]),
        RAForbiddenFailureMode("FFM-R.2", "bound_states_from_composite_notation",
            "Claiming bound states from tensor product grammar alone.",
            "Tensor product is composition rule (MIP), not binding mechanism. "
            "Bound states require attractive interaction + discrete spectrum.",
            "Q-II.B, Q-II.G (Track D)",
            ["Composite grammar is necessary but not sufficient for binding"]),
        RAForbiddenFailureMode("FFM-R.3", "fermions_from_second_wave_quantum_by_default",
            "Claiming fermionic matter available because Q Part II was completed.",
            "Q Part II added zero fermionic content. 3-layer obstruction unchanged. "
            "Fermionic matter requires new topology/algebra beyond Q program.",
            "Q0 (E1), Q-II.G (Track C)",
            ["On-site qubit anticommutation is NOT many-body fermionic statistics"]),
        RAForbiddenFailureMode("FFM-R.4", "born_rule_smuggled_into_matter",
            "Using Born-rule probability in matter without explicit postulation.",
            "Born rule absent from Q program (Q-II.F BSR). Matter may use diagnostic "
            "weights but must not interpret them as probabilities without Born MIP.",
            "Q-II.F, Q-II.G",
            ["P(n) = Tr(rho P_n) is a postulate, not a consequence"]),
        RAForbiddenFailureMode("FFM-R.5", "bosonic_extension_as_native_matter_canon",
            "Treating extension-level bosonic structure as native matter derivation.",
            "All bosonic results carry MBU/MIP floor from Q and M/N/O. "
            "Extension-level is not native canon.",
            "Q-II.G, Appendices M/N/O",
            ["QII-R7 and R-R7 protect locked classes"]),
        RAForbiddenFailureMode("FFM-R.6", "many_mode_as_continuum_matter_closure",
            "Treating finite-site chain as continuum matter.",
            "N-site qubit chain has no spatial DOF, no continuum limit, "
            "no field-theoretic modes. Finite chain is toy, not continuum.",
            "Q-II.E",
            ["Spatial DOF absent from entire Q program"]),
        RAForbiddenFailureMode("FFM-R.7", "localized_benchmark_as_particle_ontology",
            "Treating classical localized objects (Skyrme topological defects) "
            "as quantum particles.",
            "Classical localization (Appendix M/N) is topological, not quantum-mechanical. "
            "Quantum particle identity requires Fock space + statistics.",
            "Appendices M, N",
            ["Derrick + Skyrme is classical stabilization, not quantum particle"]),
        RAForbiddenFailureMode("FFM-R.8", "chemistry_readiness_from_matter_entry_only",
            "Claiming chemistry readiness from matter entry inventory alone.",
            "Chemistry requires: particles, bound states, statistics, interactions, "
            "and probability. None of these are established at R entry.",
            "R0, Q-II.G",
            ["Chemistry is the END of the matter program, not the beginning"]),
    ]


def _build_nonclaims() -> RAEntryNonclaims:
    return RAEntryNonclaims(
        nonclaims=RA_NONCLAIMS, n_nonclaims=N_RA_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_ra_matter_program_charter() -> RACharter:
    """Run the full R-A Matter Program Charter."""
    obj = _build_objective()
    stages = _build_stage_sequence()
    criteria = _build_success_criteria()
    rules = _build_appendix_p_rules()
    ffms = _build_forbidden_failure_modes()
    nonclaims = _build_nonclaims()

    diagnostics: Dict[str, Any] = {
        "n_stages": N_STAGES,
        "n_appendix_p_rules": N_APPENDIX_P_RULES,
        "n_forbidden_failure_modes": N_FORBIDDEN_FAILURE_MODES,
        "n_nonclaims": N_RA_NONCLAIMS,
        "n_not_in_scope": len(obj.what_is_not_in_scope),
        "n_preconditions": len(obj.required_preconditions),
        "preconditions_met": obj.preconditions_met,
        "first_substantive_stage": "R-B",
        "fermionic_boundary_stage": "R-E",
        "final_stage": "R-G",
    }

    result = RACharter(
        valid=True, objective=obj, stage_sequence=stages,
        success_criteria=criteria, appendix_p_rules=rules,
        forbidden_failure_modes=ffms, entry_nonclaims=nonclaims,
        r0_inventory_linked=True, charter_verdict=CHARTER_VERDICT,
        diagnostics=diagnostics,
    )
    validate_ra_result(result)
    return result


def validate_ra_result(result: RACharter) -> None:
    if len(result.stage_sequence) != N_STAGES:
        raise ValueError(f"Expected {N_STAGES} stages")
    for i, s in enumerate(result.stage_sequence):
        if s.stage_index != i:
            raise ValueError(f"Stage {s.stage_id}: index mismatch")
    if len(result.appendix_p_rules) != N_APPENDIX_P_RULES:
        raise ValueError(f"Expected {N_APPENDIX_P_RULES} rules")
    if len(result.forbidden_failure_modes) != N_FORBIDDEN_FAILURE_MODES:
        raise ValueError(f"Expected {N_FORBIDDEN_FAILURE_MODES} FFMs")
    ffm_names = [f.name for f in result.forbidden_failure_modes]
    for expected in FORBIDDEN_FAILURE_MODE_NAMES:
        if expected not in ffm_names:
            raise ValueError(f"Missing FFM: {expected}")
    if result.entry_nonclaims.n_nonclaims != N_RA_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.entry_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if result.charter_verdict not in ALLOWED_CHARTER_VERDICTS:
        raise ValueError(f"Invalid verdict: {result.charter_verdict}")
    if not result.objective.preconditions_met:
        raise ValueError("Preconditions not met")
    if not result.r0_inventory_linked:
        raise ValueError("R0 not linked")
    if len(result.objective.what_is_not_in_scope) < 5:
        raise ValueError("Not-in-scope too short")


def _self_test() -> bool:
    r = run_ra_matter_program_charter()
    assert r.valid is True
    assert r.charter_verdict == CHARTER_VERDICT
    assert len(r.stage_sequence) == N_STAGES
    assert len(r.forbidden_failure_modes) == N_FORBIDDEN_FAILURE_MODES
    return True


if __name__ == "__main__":
    _self_test()
    print("R-A self-test passed.")
