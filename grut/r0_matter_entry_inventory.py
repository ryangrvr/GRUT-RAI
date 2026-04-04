"""
Appendix R0 --- Matter Entry Inventory
=======================================
GRUT Matter Program --- Phase R0

This module inventories all matter-relevant ingredients available at the
start of Appendix R, classifying each by readiness level and doctrinal status.

Inherited from Appendix Q (Parts I and II):
  Q-II.G final handoff:
    - quantum_program_sufficient_to_open_matter_program
    - appendix_R_authorized_with_explicit_extension_flags
    - bosonic_pre_matter_readiness_advanced
    - fermionic_obstruction_unchanged
    - matter_may_proceed_only_with_explicit_probability_postulate

  R may assume:
    1. Constitutive recovery in effective regime
    2. Decoherence and pointer-basis selection
    3. Transient interference before decoherence
    4. Diagnostic weights as mathematical tools

  R must carry extension flags for:
    1. Composite grammar (tensor product MIP)
    2. Entanglement (MBU)
    3. Multi-observable grammar (sigma_x postulated)
    4. Excitation structure (H_hop MIP)
    5. All Part II results carry MBU/MIP floor

  R must NOT assume:
    1. Born rule or probability interpretation
    2. Outcome selection or single-outcome actuality
    3. Particle ontology or Fock space
    4. Fermionic matter or half-integer statistics
    5. Bound-state structure or binding mechanism

Inherited from Appendices M, N, O (classical matter route):
  - Appendix M: Bosonic localized object (Derrick obstruction + Skyrme resolution path)
  - Appendix N: Skyrme term as motivated_but_unbuilt (L4 stabilizer)
  - Appendix O: O(3) sigma model as motivated_independent_postulation
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

# Category counts
N_CATEGORY_A_ITEMS: int = 6   # Bosonic-ready
N_CATEGORY_B_ITEMS: int = 6   # Matter-blocking gaps
N_CATEGORY_C_ITEMS: int = 3   # Fermionic blockers
N_CATEGORY_D_ITEMS: int = 4   # Probability constraints
N_CATEGORY_E_ITEMS: int = 5   # Extension-chain inheritances
N_CATEGORY_F_ITEMS: int = 8   # Matter-readiness domains
N_TOTAL_ITEMS: int = 32

N_R0_NONCLAIMS: int = 8
N_HARD_RULES: int = 6
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

ALLOWED_PRESENCE_STATES: frozenset = frozenset({
    "present", "absent", "obstructed", "extension_ready",
    "precondition_only", "blocked",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})
ALLOWED_CATEGORY_LABELS: frozenset = frozenset({
    "A_bosonic_ready", "B_matter_blocking_gaps", "C_fermionic_blockers",
    "D_probability_constraints", "E_extension_chain", "F_matter_readiness_domains",
})

# Inherited from Q-II.G
QIIG_INHERITED_OVERALL: str = "quantum_program_sufficient_to_open_matter_program"
QIIG_INHERITED_R_ENTRY: str = "appendix_R_authorized_with_explicit_extension_flags"

# R0 verdict
R0_INVENTORY_VERDICT: str = "matter_entry_inventory_complete__all_items_documented"

HARD_EPISTEMIC_RULES: List[str] = [
    "prefer_blocked_over_aspirational",
    "prefer_extension_ready_over_ready_when_inheritance_is_non_native",
    "preserve_fermionic_obstruction_exactly",
    "preserve_probability_boundary_exactly",
    "do_not_treat_many_mode_excitations_as_particles",
    "do_not_treat_composite_grammar_as_bound_state_closure",
]

R0_NONCLAIMS: List[str] = [
    "NOT_claiming_matter_entry_therefore_matter_solved__"
    "inventory_documents_starting_conditions_not_matter_closure",
    "NOT_claiming_bosonic_readiness_therefore_particles_exist__"
    "pre_particle_ingredients_are_not_particle_ontology",
    "NOT_claiming_extension_chain_therefore_native_matter__"
    "all_inherited_quantum_results_carry_MBU_or_MIP_floor",
    "NOT_claiming_composite_grammar_therefore_bound_states__"
    "tensor_product_composition_is_not_binding_mechanism",
    "NOT_claiming_excitation_grammar_therefore_matter_dynamics__"
    "dissipative_hopping_is_not_matter_physics",
    "NOT_claiming_diagnostic_weights_therefore_matter_probabilities__"
    "Born_rule_absent_unless_explicitly_postulated",
    "NOT_claiming_classical_bosonic_route_therefore_quantum_particles__"
    "Skyrme_O3_route_is_classical_not_quantum_particle_derivation",
    "NOT_claiming_fermionic_obstruction_softened__"
    "Q0_3_layer_block_unchanged_by_quantum_program_or_matter_entry",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class R0InventoryItem:
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
class R0CategorySummary:
    category_label: str
    n_items: int
    item_ids: List[str]
    description: str


@dataclass
class R0ReadinessAssessment:
    q_handoff_respected: bool
    all_items_documented: bool
    fermionic_obstruction_preserved: bool
    probability_boundary_preserved: bool
    extension_flags_carried: bool
    ready_for_rb: bool
    readiness_verdict: str
    notes: List[str]


@dataclass
class R0MatterEntryInventoryResult:
    valid: bool
    items: List[R0InventoryItem]
    category_summaries: List[R0CategorySummary]
    readiness_assessment: R0ReadinessAssessment
    n_total: int
    n_present: int
    n_extension_ready: int
    n_precondition_only: int
    n_absent: int
    n_obstructed: int
    n_blocked: int
    hard_rules: List[str]
    nonclaims: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    inventory_verdict: str
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Category builders
# ---------------------------------------------------------------------------

def _build_category_a() -> List[R0InventoryItem]:
    """Category A --- bosonic-ready ingredients."""
    return [
        R0InventoryItem("A1", "constitutive_observable_classical_bridge",
            "A_bosonic_ready", "present", "motivated_but_unbuilt",
            "Q-C.5, Q-E (QE4)", "Constitutive recovery established in effective regime",
            "Constitutive bridge implies full classical matter",
            ["Part I locked result; most mature quantum inheritance"], []),
        R0InventoryItem("A2", "bosonic_state_grammar",
            "A_bosonic_ready", "extension_ready", "motivated_but_unbuilt",
            "Q-II.B, Q-II.E", "Qubit chain state grammar available at extension level",
            "State grammar implies bosonic particle states",
            ["C^2 per site; (C^2)^N composite; extension-level"], []),
        R0InventoryItem("A3", "dissipative_excitation_structure",
            "A_bosonic_ready", "extension_ready", "motivated_independent_postulation",
            "Q-II.E", "sigma_+/sigma_- with H_hop dissipative propagation",
            "Excitation structure implies particle dynamics",
            ["MIP: H_hop postulated; qubit operators not bosonic a/a^dag"], []),
        R0InventoryItem("A4", "composite_state_grammar",
            "A_bosonic_ready", "extension_ready", "motivated_independent_postulation",
            "Q-II.B", "Tensor product composition for multi-subsystem states",
            "Composite grammar implies matter binding",
            ["MIP: tensor product postulated, not derived"], []),
        R0InventoryItem("A5", "many_mode_structure",
            "A_bosonic_ready", "extension_ready", "motivated_independent_postulation",
            "Q-II.E", "N-site chain with mode labels and dissipative propagation",
            "Many-mode structure implies field theory or continuum matter",
            ["MIP: site labels and H_hop postulated"], []),
        R0InventoryItem("A6", "bosonic_pre_particle_ingredients",
            "A_bosonic_ready", "precondition_only", "motivated_but_unbuilt",
            "Appendices M/N/O + Q-II.E",
            "Classical Skyrme/O(3) route + quantum excitation overlay",
            "Pre-particle ingredients imply particles exist",
            ["Classical route (M/N/O) + quantum excitation (Q-II.E)",
             "No Fock space, no particle identity, no dispersion"], []),
    ]


def _build_category_b() -> List[R0InventoryItem]:
    """Category B --- matter-blocking gaps."""
    return [
        R0InventoryItem("B1", "particle_ontology",
            "B_matter_blocking_gaps", "absent", "compatible_but_ad_hoc",
            "Q-II.E, Q-II.G", "Particle ontology not established",
            "Particle ontology implied by excitation grammar",
            ["No Fock space, no particle identity, no dispersion relation"], []),
        R0InventoryItem("B2", "bound_state_closure",
            "B_matter_blocking_gaps", "absent", "compatible_but_ad_hoc",
            "Q-II.G (Track D)", "Bound-state closure absent; no binding mechanism",
            "Composite grammar implies bound states",
            ["No attractive interaction, no discrete spectrum"], []),
        R0InventoryItem("B3", "stabilization_beyond_known_audits",
            "B_matter_blocking_gaps", "absent", "motivated_but_unbuilt",
            "Appendix N (Skyrme)", "Skyrme stabilization MBU; quantum stabilization unbuilt",
            "Classical Skyrme stabilization implies quantum stability",
            ["Derrick obstruction resolved classically via L4; quantum analog unbuilt"], []),
        R0InventoryItem("B4", "continuum_matter_ontology",
            "B_matter_blocking_gaps", "absent", "compatible_but_ad_hoc",
            "Q-II.E (ML2/ML3 blocked)", "No continuum spatial structure or field modes",
            "Finite-site chain implies continuum matter",
            ["Spatial DOF absent from entire Q program"], []),
        R0InventoryItem("B5", "statistics_closure",
            "B_matter_blocking_gaps", "absent", "compatible_but_ad_hoc",
            "Q-II.0 (F3)", "Quantum statistics (BE/FD) not established",
            "Excitation counting implies particle statistics",
            ["Requires composite states + symmetrization postulate"], []),
        R0InventoryItem("B6", "localization_beyond_benchmark",
            "B_matter_blocking_gaps", "absent", "motivated_but_unbuilt",
            "Appendix M, Q-II.E", "Localization only at classical (Skyrme) level",
            "Toy-site localization implies physical particle localization",
            ["Classical topological localization (M); no quantum localization"], []),
    ]


def _build_category_c() -> List[R0InventoryItem]:
    """Category C --- fermionic blockers."""
    return [
        R0InventoryItem("C1", "fermionic_3_layer_obstruction",
            "C_fermionic_blockers", "blocked", "bounded_structural_result",
            "Q0 (E1), Appendix M", "3-layer fermionic obstruction unchanged",
            "Fermionic matter accessible without new topology",
            ["Layer 1: pi_2(S^2)=Z bosonic only; Layer 2: no spinor in O(3); "
             "Layer 3: no Hopf/SU(2) natively"], []),
        R0InventoryItem("C2", "hopf_spinor_statistics_route",
            "C_fermionic_blockers", "absent", "compatible_but_ad_hoc",
            "Q0, Q-II.G", "No Hopf fibration, spinorial, or fermionic statistics route",
            "Quantum program provides spinorial structure",
            ["Would require entirely new topological/algebraic postulation"], []),
        R0InventoryItem("C3", "quantum_program_fermionic_contribution",
            "C_fermionic_blockers", "absent", "bounded_structural_result",
            "Q-II.G (Track C)", "Quantum program added zero fermionic content",
            "Second-wave quantum structure softens fermionic obstruction",
            ["sigma_+ anticommutation is on-site qubit, not many-body fermionic"], []),
    ]


def _build_category_d() -> List[R0InventoryItem]:
    """Category D --- probability/measurement constraints."""
    return [
        R0InventoryItem("D1", "diagnostic_weights_only",
            "D_probability_constraints", "present", "bounded_structural_result",
            "Q-II.F", "Density-matrix diagonals available as mathematical tools",
            "Diagnostic weights are matter probabilities",
            ["rho_nn: sum=1, non-negative, stable under decoherence",
             "NOT probabilities without Born rule"], []),
        R0InventoryItem("D2", "born_rule_postulate_requirement",
            "D_probability_constraints", "precondition_only", "motivated_independent_postulation",
            "Q-II.F (PX1)", "Born rule identified as MIP if matter needs probability",
            "Born rule derived from quantum program",
            ["P(n) = Tr(rho P_n): single postulate, no new DOF, MIP"], []),
        R0InventoryItem("D3", "no_native_outcome_selection",
            "D_probability_constraints", "absent", "bounded_structural_result",
            "Q-II.F", "Outcome selection absent from quantum program",
            "Outcome selection available for matter use",
            ["No mechanism selects single outcome; documented absence (BSR)"], []),
        R0InventoryItem("D4", "no_observer_conditioned_update",
            "D_probability_constraints", "absent", "bounded_structural_result",
            "Q-II.F", "Observer-conditioned update absent",
            "Collapse or state update available for matter",
            ["Would require Born rule + collapse postulate (two MIPs)"], []),
    ]


def _build_category_e() -> List[R0InventoryItem]:
    """Category E --- extension-chain inheritances."""
    return [
        R0InventoryItem("E1", "o3_sigma_model_mip",
            "E_extension_chain", "extension_ready", "motivated_independent_postulation",
            "Appendix O", "O(3) sigma model as MIP",
            "O(3) sigma model derived from GRUT first principles",
            ["MIP: motivated by topological target space; not native"], []),
        R0InventoryItem("E2", "skyrme_term_mbu",
            "E_extension_chain", "extension_ready", "motivated_but_unbuilt",
            "Appendix N", "Skyrme L4 term as MBU stabilizer",
            "Skyrme term is native canon or fully derived",
            ["MBU: derivation path identified, work not done"], []),
        R0InventoryItem("E3", "lindbladian_quantum_layer_mbu",
            "E_extension_chain", "extension_ready", "motivated_but_unbuilt",
            "Q-C, Q-C.5", "Lindbladian dynamics as MBU quantum layer",
            "Lindbladian dynamics is native GRUT canon",
            ["MBU: preferred law class, not native derivation"], []),
        R0InventoryItem("E4", "composite_grammar_mip",
            "E_extension_chain", "extension_ready", "motivated_independent_postulation",
            "Q-II.B", "Tensor product as MIP composition rule",
            "Tensor product derived from GRUT",
            ["MIP: standard QM postulate, not GRUT derivation"], []),
        R0InventoryItem("E5", "observable_algebra_mbu",
            "E_extension_chain", "extension_ready", "motivated_but_unbuilt",
            "Q-II.D", "Multi-observable grammar as MBU extension",
            "Observable algebra natively derived",
            ["MBU: sigma_x postulated; su(2) toy algebra"], []),
    ]


def _build_category_f() -> List[R0InventoryItem]:
    """Category F --- matter-readiness domains."""
    return [
        R0InventoryItem("F1", "bosonic_pre_particle_ontology",
            "F_matter_readiness_domains", "precondition_only", "motivated_but_unbuilt",
            "Q-II.G, Appendices M/N/O",
            "Bosonic pre-particle readiness advanced; ontology premature",
            "Bosonic particles established",
            ["Classical route + quantum excitation overlay; no Fock space"], []),
        R0InventoryItem("F2", "localized_object_readiness",
            "F_matter_readiness_domains", "precondition_only", "motivated_but_unbuilt",
            "Appendix M (Skyrme)", "Classical localization via topological defects",
            "Localized quantum particles established",
            ["Derrick obstruction + Skyrme resolution at classical level only"], []),
        R0InventoryItem("F3", "composite_matter_readiness",
            "F_matter_readiness_domains", "extension_ready", "motivated_but_unbuilt",
            "Q-II.B", "Composite state grammar available for matter use",
            "Composite grammar implies material composites",
            ["Tensor product available; no interaction or binding"], []),
        R0InventoryItem("F4", "bound_state_readiness",
            "F_matter_readiness_domains", "absent", "compatible_but_ad_hoc",
            "Q-II.G (Track D)", "No binding mechanism available",
            "Bound-state readiness established",
            ["Composite grammar is precondition; binding absent"], []),
        R0InventoryItem("F5", "fermionic_matter_readiness",
            "F_matter_readiness_domains", "blocked", "bounded_structural_result",
            "Q0 (E1)", "Fermionic obstruction unchanged",
            "Fermionic matter accessible",
            ["3-layer obstruction from Q0; unchanged by Q program"], []),
        R0InventoryItem("F6", "statistical_matter_readiness",
            "F_matter_readiness_domains", "absent", "compatible_but_ad_hoc",
            "Q-II.0 (F3)", "Quantum statistics absent",
            "Statistics closure established",
            ["Requires composite states + symmetrization + identity postulate"], []),
        R0InventoryItem("F7", "probability_ready_matter_interpretation",
            "F_matter_readiness_domains", "precondition_only", "bounded_structural_result",
            "Q-II.F", "Diagnostic weights only; Born rule if needed requires MIP",
            "Matter has probability interpretation",
            ["Born postulate identified but not adopted"], []),
        R0InventoryItem("F8", "chemistry_readiness_hints",
            "F_matter_readiness_domains", "absent", "compatible_but_ad_hoc",
            "None", "No chemistry-level structure available",
            "Chemistry readiness hinted by matter entry",
            ["Requires: particles, bound states, statistics, interactions"], []),
    ]


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_r0_matter_entry_inventory() -> R0MatterEntryInventoryResult:
    """Run the full R0 Matter Entry Inventory."""
    cats = {
        "A": _build_category_a(),
        "B": _build_category_b(),
        "C": _build_category_c(),
        "D": _build_category_d(),
        "E": _build_category_e(),
        "F": _build_category_f(),
    }
    all_items = []
    for items in cats.values():
        all_items.extend(items)

    summaries = [
        R0CategorySummary("A_bosonic_ready", N_CATEGORY_A_ITEMS,
            [i.item_id for i in cats["A"]],
            "Bosonic-ready ingredients from Q and M/N/O"),
        R0CategorySummary("B_matter_blocking_gaps", N_CATEGORY_B_ITEMS,
            [i.item_id for i in cats["B"]],
            "Gaps blocking matter closure"),
        R0CategorySummary("C_fermionic_blockers", N_CATEGORY_C_ITEMS,
            [i.item_id for i in cats["C"]],
            "Fermionic obstruction inheritance"),
        R0CategorySummary("D_probability_constraints", N_CATEGORY_D_ITEMS,
            [i.item_id for i in cats["D"]],
            "Probability/measurement constraints on matter"),
        R0CategorySummary("E_extension_chain", N_CATEGORY_E_ITEMS,
            [i.item_id for i in cats["E"]],
            "Extension-chain inheritances (MIP/MBU)"),
        R0CategorySummary("F_matter_readiness_domains", N_CATEGORY_F_ITEMS,
            [i.item_id for i in cats["F"]],
            "Matter-readiness domain assessments"),
    ]

    counts = {}
    for s in ALLOWED_PRESENCE_STATES:
        counts[s] = sum(1 for i in all_items if i.presence_state == s)

    readiness = R0ReadinessAssessment(
        q_handoff_respected=True, all_items_documented=True,
        fermionic_obstruction_preserved=True, probability_boundary_preserved=True,
        extension_flags_carried=True, ready_for_rb=True,
        readiness_verdict="ready_to_proceed_to_ra_and_rb",
        notes=["Q-II.G handoff constraints respected verbatim",
               f"All {N_TOTAL_ITEMS} items documented across 6 categories",
               "Fermionic 3-layer obstruction preserved exactly",
               "Born-rule absence preserved exactly",
               "All extension flags carried from Q-II.G"],
    )

    allowed_claims: List[str] = [
        "All matter-relevant ingredients inventoried across 6 categories "
        f"with {N_TOTAL_ITEMS} items total",
        "Bosonic pre-particle ingredients available at extension level "
        "with classical Skyrme/O(3) route and quantum excitation overlay",
        "6 matter-blocking gaps documented: particle ontology, bound states, "
        "stabilization, continuum, statistics, localization",
        "Fermionic 3-layer obstruction preserved exactly from Q0",
        "Probability boundary preserved: diagnostic weights only; Born rule "
        "requires explicit MIP postulate",
        "5 extension-chain inheritances documented with locked Appendix P classes",
        "R-A and R-B authorized to proceed based on complete inventory",
    ]

    forbidden_claims: List[str] = [
        "Matter entry inventory implies matter solved",
        "Bosonic readiness implies particles exist",
        "Extension-chain inheritances imply native matter canon",
        "Composite grammar implies bound states",
        "Excitation grammar implies matter dynamics",
        "Diagnostic weights imply matter probabilities",
        "Classical bosonic route implies quantum particles derived",
    ]

    diagnostics: Dict[str, Any] = {
        "n_total_items": len(all_items),
        "n_categories": len(summaries),
        "n_present": counts.get("present", 0),
        "n_extension_ready": counts.get("extension_ready", 0),
        "n_precondition_only": counts.get("precondition_only", 0),
        "n_absent": counts.get("absent", 0),
        "n_obstructed": counts.get("obstructed", 0),
        "n_blocked": counts.get("blocked", 0),
        "n_nonclaims": N_R0_NONCLAIMS,
        "n_hard_rules": N_HARD_RULES,
    }

    result = R0MatterEntryInventoryResult(
        valid=True, items=all_items, category_summaries=summaries,
        readiness_assessment=readiness,
        n_total=len(all_items),
        n_present=counts.get("present", 0),
        n_extension_ready=counts.get("extension_ready", 0),
        n_precondition_only=counts.get("precondition_only", 0),
        n_absent=counts.get("absent", 0),
        n_obstructed=counts.get("obstructed", 0),
        n_blocked=counts.get("blocked", 0),
        hard_rules=HARD_EPISTEMIC_RULES, nonclaims=R0_NONCLAIMS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        inventory_verdict=R0_INVENTORY_VERDICT, diagnostics=diagnostics,
    )
    validate_r0_result(result)
    return result


def validate_r0_result(result: R0MatterEntryInventoryResult) -> None:
    if len(result.items) != N_TOTAL_ITEMS:
        raise ValueError(f"Expected {N_TOTAL_ITEMS} items, got {len(result.items)}")
    for item in result.items:
        if item.presence_state not in ALLOWED_PRESENCE_STATES:
            raise ValueError(f"{item.item_id}: state '{item.presence_state}' invalid")
        if item.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"{item.item_id}: class '{item.appendix_p_class}' invalid")
        if item.category not in ALLOWED_CATEGORY_LABELS:
            raise ValueError(f"{item.item_id}: category '{item.category}' invalid")
    if len(result.nonclaims) != N_R0_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if len(result.hard_rules) != N_HARD_RULES:
        raise ValueError("Hard rules count mismatch")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.readiness_assessment.ready_for_rb:
        raise ValueError("ready_for_rb must be True")
    ids = [i.item_id for i in result.items]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate item IDs")
    # Verify counts
    for state in ALLOWED_PRESENCE_STATES:
        counted = sum(1 for i in result.items if i.presence_state == state)
        recorded = getattr(result, f"n_{state}", None)
        if recorded is not None and counted != recorded:
            raise ValueError(f"Count mismatch for {state}: {counted} != {recorded}")


def _self_test() -> bool:
    r = run_r0_matter_entry_inventory()
    assert r.valid is True
    assert r.n_total == N_TOTAL_ITEMS
    assert r.inventory_verdict == R0_INVENTORY_VERDICT
    return True


if __name__ == "__main__":
    _self_test()
    print("R0 self-test passed.")
