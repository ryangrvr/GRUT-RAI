"""
Appendix Q-II.G --- Quantum Matter-Readiness Map
=================================================
GRUT Quantum Program --- Phase Q-II.G  (Final Second-Wave Stage)

This module produces the formal readiness map for Appendix R (Matter Program),
synthesizing all results from Appendix Q Parts I and II.

Summary of quantum program achievements
----------------------------------------
Part I (Q-B through Q-F):
  - State space: C^2 with density matrix (MIP: J postulated)
  - Dynamics: Lindbladian with L = sqrt(gamma) Phi_hat, gamma = 1/tau
  - Recovery: tau d<Phi>/dt + <Phi> = <X> in effective regime
  - Decoherence: pointer-basis selection in Phi_hat eigenstates
  - Interference: transient, V(t) = exp(-R_dec t)
  - All single-system; all extension-level (MBU/MIP floor)

Part II (Q-II.B through Q-II.F):
  - Composite: tensor product C^4 = C^2 tensor C^2 (MIP)
  - Entanglement: nonfactorized states; purity/PPT witness (MBU)
  - Observables: multi-observable grammar; su(2) toy algebra (MBU)
  - Excitations: sigma_+/sigma_- on N-site chain; H_hop propagation (MIP)
  - Probability: diagnostic weights only; Born rule NOT derived (BSR)
  - Outcome: selection absent; minimum extension (Born MIP) identified

What Appendix R inherits
-------------------------
1. READY: constitutive observable, decoherence/pointer, classical bridge
2. EXTENSION-READY: composite states, entanglement, observables, excitations
3. NOT READY: probability/measurement, particle ontology, bound states
4. BLOCKED: fermionic matter (Q0 3-layer obstruction unchanged)

Appendix R entry conditions:
  - R may assume constitutive/decoherence structure
  - R must flag all composite/entanglement/excitation as extension-level
  - R must NOT assume Born rule, outcome selection, or particle ontology
  - R must preserve fermionic obstruction
  - R must re-audit any claims that exceed the Q readiness map
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

# Handoff inventory items
N_HANDOFF_ITEMS: int = 9
# Readiness domains
N_READINESS_DOMAINS: int = 10
# Appendix R entry conditions
N_R_ASSUMES: int = 4
N_R_EXTENSION_FLAGS: int = 5
N_R_MUST_NOT_ASSUME: int = 5
N_R_MUST_REAUDIT: int = 3

N_APPENDIX_P_ENTRIES: int = 7
N_QIIG_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Readiness levels
ALLOWED_READINESS_LEVELS: frozenset = frozenset({
    "ready", "extension_ready", "precondition_only", "blocked",
})

# Inherited terminal verdicts from Q-II.F
QIIF_INHERITED_PROBABILITY: str = "diagnostic_weights_available_but_not_probabilities"
QIIF_INHERITED_OUTCOME: str = "born_rule_and_outcome_selection_not_derived"
QIIF_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QIIG"

# Q-II.G Verdict strings
QIIG_BOSONIC_VERDICT: str = "bosonic_pre_matter_readiness_advanced"
QIIG_FERMIONIC_VERDICT: str = "fermionic_obstruction_unchanged"
QIIG_PROBABILITY_BOUNDARY_VERDICT: str = (
    "matter_may_proceed_only_with_explicit_probability_postulate"
)
QIIG_APPENDIX_R_ENTRY_VERDICT: str = (
    "appendix_R_authorized_with_explicit_extension_flags"
)
QIIG_OVERALL_VERDICT: str = "quantum_program_sufficient_to_open_matter_program"
QIIG_OVERALL_APPENDIX_P_CLASS: str = "bounded_structural_result"

# Frozensets
ALLOWED_BOSONIC_VERDICTS: frozenset = frozenset({
    "bosonic_pre_matter_readiness_advanced",
    "bosonic_readiness_extension_only",
    "bosonic_particle_route_still_blocked",
    "bosonic_matter_readiness_blocked",
})
ALLOWED_FERMIONIC_VERDICTS: frozenset = frozenset({
    "fermionic_obstruction_unchanged",
    "fermionic_route_structurally_advanced_but_blocked",
    "fermionic_extension_route_identified",
    "fermionic_matter_readiness_blocked",
})
ALLOWED_PROBABILITY_BOUNDARY_VERDICTS: frozenset = frozenset({
    "matter_must_inherit_diagnostic_weights_only",
    "matter_may_proceed_only_with_explicit_probability_postulate",
    "probability_boundary_still_blocking_matter_use",
    "probability_boundary_underdetermined",
})
ALLOWED_APPENDIX_R_ENTRY_VERDICTS: frozenset = frozenset({
    "appendix_R_authorized_with_explicit_extension_flags",
    "appendix_R_authorized_for_pre_matter_scaffolding_only",
    "appendix_R_not_yet_authorized",
    "appendix_R_requires_further_quantum_refinement",
})
ALLOWED_OVERALL_VERDICTS: frozenset = frozenset({
    "quantum_program_sufficient_to_open_matter_program",
    "quantum_program_sufficient_only_for_scaffolded_matter_entry",
    "quantum_program_not_yet_sufficient_for_matter",
    "matter_handoff_still_blocked",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

QIIG_NONCLAIMS: List[str] = [
    "NOT_claiming_many_mode_excitations_therefore_particles__"
    "excitation_grammar_is_not_particle_ontology",
    "NOT_claiming_entanglement_therefore_matter_binding__"
    "nonfactorized_states_are_not_bound_states",
    "NOT_claiming_pointer_structure_therefore_classical_matter_ontology__"
    "pointer_basis_selects_quantum_basis_not_material_objects",
    "NOT_claiming_diagnostic_weights_therefore_matter_probabilities__"
    "Born_rule_absent_means_no_probability_inheritance_without_postulate",
    "NOT_claiming_bosonic_excitation_grammar_therefore_bosonic_matter_closure__"
    "excitation_counting_is_not_particle_physics",
    "NOT_claiming_second_wave_quantum_therefore_fermionic_obstruction_dissolved__"
    "Q0_3_layer_fermionic_obstruction_unchanged_by_quantum_program",
    "NOT_claiming_extension_ready_therefore_native_matter_canon__"
    "all_quantum_results_carry_MBU_or_MIP_floor_into_matter",
    "NOT_claiming_readiness_map_therefore_matter_solved__"
    "readiness_map_documents_entry_conditions_not_matter_closure",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIGHandoffItem:
    item_id: str
    item_name: str
    source: str
    readiness: str  # ready, extension_ready, precondition_only, blocked
    appendix_p_class: str
    what_r_may_assume: str
    what_r_must_not_assume: str
    notes: List[str]


@dataclass
class QIIGHandoffInventory:
    items: List[QIIGHandoffItem]
    n_items: int
    n_ready: int
    n_extension_ready: int
    n_precondition: int
    n_blocked: int
    notes: List[str]


@dataclass
class QIIGBosonicReadinessAudit:
    state_grammar_ready: bool
    excitation_structure_ready: bool
    constitutive_bridge_ready: bool
    composite_structure_ready: bool
    particle_like_readiness: bool
    bound_state_readiness: bool
    bosonic_readiness_verdict: str
    notes: List[str]


@dataclass
class QIIGFermionicReadinessAudit:
    obstruction_changed: bool
    new_route_identified: bool
    fermionic_readiness_verdict: str
    obstruction_description: str
    notes: List[str]


@dataclass
class QIIGBoundStateAudit:
    composite_grammar_available: bool
    interaction_hamiltonian_available: bool
    binding_mechanism_available: bool
    bound_state_verdict: str
    notes: List[str]


@dataclass
class QIIGProbabilityBoundaryAudit:
    born_rule_derived: bool
    diagnostic_weights_available: bool
    extension_route_identified: bool
    probability_boundary_verdict: str
    notes: List[str]


@dataclass
class QIIGReadinessEntry:
    domain: str
    readiness_level: str
    notes: str


@dataclass
class QIIGReadinessTable:
    entries: List[QIIGReadinessEntry]
    n_entries: int
    n_ready: int
    n_extension_ready: int
    n_precondition: int
    n_blocked: int


@dataclass
class QIIGAppendixREntryConditions:
    r_may_assume: List[str]
    r_must_carry_extension_flags: List[str]
    r_must_not_assume: List[str]
    r_must_reaudit: List[str]
    appendix_r_entry_verdict: str
    notes: List[str]


@dataclass
class QIIGAppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIIGAppendixPAudit:
    entries: List[QIIGAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIIGNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIGQuantumMatterReadinessResult:
    valid: bool
    track_a_handoff: QIIGHandoffInventory
    track_b_bosonic: QIIGBosonicReadinessAudit
    track_c_fermionic: QIIGFermionicReadinessAudit
    track_d_bound_state: QIIGBoundStateAudit
    track_e_probability: QIIGProbabilityBoundaryAudit
    track_f_readiness_table: QIIGReadinessTable
    track_g_r_entry: QIIGAppendixREntryConditions
    track_h_appendix_p: QIIGAppendixPAudit
    track_i_nonclaims: QIIGNonclaimFirewall
    # Five hard-gated verdicts
    bosonic_readiness_verdict: str
    fermionic_readiness_verdict: str
    probability_boundary_verdict: str
    appendix_r_entry_verdict: str
    overall_q_to_r_verdict: str
    # Summary
    qiig_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIIGHandoffInventory:
    items = [
        QIIGHandoffItem("HI1", "constitutive_observable_and_classical_bridge",
            "Q-C.5, Q-E (QE4)", "ready", "motivated_but_unbuilt",
            "Constitutive recovery tau d<Phi>/dt + <Phi> = <X> in effective regime",
            "Constitutive bridge implies full classical matter ontology",
            ["Established in Part I; most mature quantum result"]),
        QIIGHandoffItem("HI2", "decoherence_and_pointer_basis",
            "Q-D, Q-E (QE1)", "ready", "motivated_but_unbuilt",
            "Pointer-basis selection and decoherence rates in effective regime",
            "Decoherence implies measurement closure or Born rule",
            ["Established in Part I; locked MBU class"]),
        QIIGHandoffItem("HI3", "composite_state_grammar",
            "Q-II.B", "extension_ready", "motivated_independent_postulation",
            "Tensor product composition for multi-subsystem states",
            "Composite grammar implies physical subsystem coupling",
            ["MIP: tensor product is postulated, not derived"]),
        QIIGHandoffItem("HI4", "entanglement_nonfactorized_structure",
            "Q-II.C", "extension_ready", "motivated_but_unbuilt",
            "Nonfactorized states and purity/PPT entanglement witnesses",
            "Entanglement implies matter binding or Bell nonlocality",
            ["MBU: extension-level; Bell not yet justified"]),
        QIIGHandoffItem("HI5", "multi_observable_grammar",
            "Q-II.D", "extension_ready", "motivated_but_unbuilt",
            "Toy noncommuting pair and correlator grammar",
            "Multi-observable grammar implies full operator algebra",
            ["MBU: sigma_x postulated, not derived"]),
        QIIGHandoffItem("HI6", "many_mode_excitation_structure",
            "Q-II.E", "extension_ready", "motivated_independent_postulation",
            "N-site chain with sigma_+/sigma_- and dissipative propagation",
            "Excitation grammar implies particles or field theory",
            ["MIP: H_hop postulated; dissipative propagation only"]),
        QIIGHandoffItem("HI7", "probability_and_outcome_gap",
            "Q-II.F", "precondition_only", "bounded_structural_result",
            "Diagnostic weights available; Born rule absent; extension route identified",
            "Diagnostic weights are probabilities or Born rule is derived",
            ["BSR: absence documented; minimum extension identified"]),
        QIIGHandoffItem("HI8", "fermionic_obstruction",
            "Q0 (E1), Appendix M", "blocked", "bounded_structural_result",
            "3-layer fermionic obstruction documented and unchanged by Q program",
            "Fermionic matter accessible without new topological structure",
            ["BSR: pi_2(S^2) = Z; bosonic winding only; 3-layer block"]),
        QIIGHandoffItem("HI9", "bosonic_object_skyrme_o3_chain",
            "Appendices M, N, O", "extension_ready", "motivated_but_unbuilt",
            "Classical bosonic object route via Skyrme/O(3) topology",
            "Classical topological objects are quantum particles",
            ["Classical route established; quantum excitation overlay from Q-II.E"]),
    ]
    n_r = sum(1 for i in items if i.readiness == "ready")
    n_e = sum(1 for i in items if i.readiness == "extension_ready")
    n_p = sum(1 for i in items if i.readiness == "precondition_only")
    n_b = sum(1 for i in items if i.readiness == "blocked")
    return QIIGHandoffInventory(
        items=items, n_items=N_HANDOFF_ITEMS,
        n_ready=n_r, n_extension_ready=n_e, n_precondition=n_p, n_blocked=n_b,
        notes=[f"{n_r} ready, {n_e} extension-ready, {n_p} precondition, {n_b} blocked",
               "2 ready (constitutive, decoherence): Part I mature results",
               "4 extension-ready (composite, entanglement, observables, excitations, bosonic chain)",
               "1 precondition (probability gap)",
               "1 blocked (fermionic obstruction)"],
    )


def _build_track_b() -> QIIGBosonicReadinessAudit:
    return QIIGBosonicReadinessAudit(
        state_grammar_ready=True,
        excitation_structure_ready=True,
        constitutive_bridge_ready=True,
        composite_structure_ready=True,
        particle_like_readiness=False,
        bound_state_readiness=False,
        bosonic_readiness_verdict=QIIG_BOSONIC_VERDICT,
        notes=[
            "State grammar: C^2 per site, (C^2)^N composite (extension-level)",
            "Excitation: sigma_+/sigma_- with H_hop propagation (extension-level)",
            "Constitutive: tau d<Phi>/dt + <Phi> = <X> per site (Part I)",
            "Composite: tensor product composition (MIP)",
            "Particle-like: NOT ready (no Fock space, no particle identity, no dispersion)",
            "Bound state: NOT ready (no interaction beyond H_hop, no binding mechanism)",
            "Verdict: pre-matter readiness ADVANCED; particle ontology PREMATURE"],
    )


def _build_track_c() -> QIIGFermionicReadinessAudit:
    return QIIGFermionicReadinessAudit(
        obstruction_changed=False,
        new_route_identified=False,
        fermionic_readiness_verdict=QIIG_FERMIONIC_VERDICT,
        obstruction_description=(
            "Q0 item E1: 3-layer fermionic obstruction. "
            "Layer 1: pi_2(S^2) = Z gives integer (bosonic) winding only. "
            "Layer 2: no spinorial representation in O(3) sigma model. "
            "Layer 3: no Hopf fibration or SU(2) structure natively available. "
            "The quantum program (Q-B through Q-II.F) operates on the scalar "
            "field Phi and its 2-state quantization. Nothing in the quantum "
            "program introduces spinorial, half-integer, or fermionic structure. "
            "The obstruction is UNCHANGED."
        ),
        notes=[
            "Obstruction unchanged: Q program adds quantum overlay, not new topology",
            "sigma_+ on qubit is NOT fermionic creation operator",
            "Qubit anticommutation {sigma_+, sigma_-} = I is on-site, not many-body",
            "Fermionic statistics requires multi-body antisymmetrization: absent",
            "No new route identified by Q program"],
    )


def _build_track_d() -> QIIGBoundStateAudit:
    return QIIGBoundStateAudit(
        composite_grammar_available=True,
        interaction_hamiltonian_available=False,
        binding_mechanism_available=False,
        bound_state_verdict="precondition_only_no_binding_mechanism",
        notes=[
            "Composite grammar (Q-II.B): available but not binding",
            "H_hop (Q-II.E): excitation hopping, not binding interaction",
            "No attractive interaction potential postulated",
            "Bound states require: attractive interaction + discrete spectrum",
            "Current package provides only preconditions (composite space)"],
    )


def _build_track_e() -> QIIGProbabilityBoundaryAudit:
    return QIIGProbabilityBoundaryAudit(
        born_rule_derived=False,
        diagnostic_weights_available=True,
        extension_route_identified=True,
        probability_boundary_verdict=QIIG_PROBABILITY_BOUNDARY_VERDICT,
        notes=[
            "Born rule NOT derived (Q-II.F BSR)",
            "Diagnostic weights available (density-matrix diagonals)",
            "Minimum extension: Born rule as MIP postulate P(n) = Tr(rho P_n)",
            "Matter program may use diagnostic weights as mathematical tools",
            "Matter program must NOT interpret diagnostic weights as probabilities "
            "unless Born rule is explicitly postulated",
            "Verdict: matter may proceed only with explicit probability postulate"],
    )


def _build_track_f() -> QIIGReadinessTable:
    entries = [
        QIIGReadinessEntry("constitutive_observables", "ready",
            "Part I established; locked MBU class"),
        QIIGReadinessEntry("bosonic_excitations", "extension_ready",
            "Q-II.E: sigma_+/sigma_- on N-site chain with H_hop"),
        QIIGReadinessEntry("composite_structure", "extension_ready",
            "Q-II.B: tensor product C^4 (MIP)"),
        QIIGReadinessEntry("entanglement", "extension_ready",
            "Q-II.C: nonfactorized states and witnesses (MBU)"),
        QIIGReadinessEntry("multi_observable_algebra", "extension_ready",
            "Q-II.D: su(2) toy algebra with correlators (MBU)"),
        QIIGReadinessEntry("many_mode_dynamics", "extension_ready",
            "Q-II.E: dissipative propagation on chain (MIP)"),
        QIIGReadinessEntry("probability_measurement", "precondition_only",
            "Q-II.F: diagnostic weights only; Born rule absent (BSR)"),
        QIIGReadinessEntry("bosonic_particle_ontology", "precondition_only",
            "No Fock space, no particle identity; excitation grammar only"),
        QIIGReadinessEntry("fermionic_matter", "blocked",
            "Q0 3-layer obstruction unchanged"),
        QIIGReadinessEntry("bound_states", "precondition_only",
            "Composite grammar available but no binding mechanism"),
    ]
    n_r = sum(1 for e in entries if e.readiness_level == "ready")
    n_e = sum(1 for e in entries if e.readiness_level == "extension_ready")
    n_p = sum(1 for e in entries if e.readiness_level == "precondition_only")
    n_b = sum(1 for e in entries if e.readiness_level == "blocked")
    return QIIGReadinessTable(
        entries=entries, n_entries=N_READINESS_DOMAINS,
        n_ready=n_r, n_extension_ready=n_e, n_precondition=n_p, n_blocked=n_b,
    )


def _build_track_g() -> QIIGAppendixREntryConditions:
    return QIIGAppendixREntryConditions(
        r_may_assume=[
            "constitutive_recovery_tau_dPhi_dt_plus_Phi_equals_X_in_effective_regime",
            "decoherence_and_pointer_basis_selection_in_Phi_hat_eigenstates",
            "transient_interference_before_decoherence_V_exp_neg_R_dec_t",
            "diagnostic_weights_density_matrix_diagonals_as_mathematical_tools",
        ],
        r_must_carry_extension_flags=[
            "composite_state_grammar_tensor_product_is_MIP_not_native",
            "entanglement_nonfactorized_structure_is_MBU_extension_level",
            "multi_observable_grammar_sigma_x_postulated_not_derived",
            "excitation_structure_H_hop_is_MIP_postulation",
            "all_Part_II_results_carry_MBU_or_MIP_floor",
        ],
        r_must_not_assume=[
            "Born_rule_or_probability_interpretation_of_diagnostic_weights",
            "outcome_selection_or_single_outcome_actuality",
            "particle_ontology_or_Fock_space_structure",
            "fermionic_matter_or_half_integer_statistics",
            "bound_state_structure_or_binding_mechanism",
        ],
        r_must_reaudit=[
            "any_claim_that_exceeds_the_quantum_readiness_map",
            "any_probability_claim_beyond_diagnostic_weights",
            "any_fermionic_or_spinorial_claim",
        ],
        appendix_r_entry_verdict=QIIG_APPENDIX_R_ENTRY_VERDICT,
        notes=[
            "Appendix R authorized with explicit extension flags",
            "4 items R may assume (Part I mature results)",
            "5 items R must carry as extension-level",
            "5 items R must NOT assume",
            "3 re-audit requirements"],
    )


def _build_track_h() -> QIIGAppendixPAudit:
    entries = [
        QIIGAppendixPEntry("QIIG_handoff_inventory", "Quantum-to-matter handoff",
            "bounded_structural_result",
            "Complete handoff inventory with 9 items classified by readiness",
            "Handoff inventory implies matter closure",
            "All Q Part I and Part II results"),
        QIIGAppendixPEntry("QIIG_bosonic_readiness", "Bosonic pre-matter readiness",
            "motivated_but_unbuilt",
            "Bosonic pre-matter readiness advanced; particle ontology premature",
            "Bosonic readiness implies bosonic matter derived",
            "Q-II.E excitations, Appendices M/N/O classical route"),
        QIIGAppendixPEntry("QIIG_fermionic_block", "Fermionic obstruction",
            "bounded_structural_result",
            "Fermionic 3-layer obstruction unchanged by quantum program",
            "Quantum program dissolves fermionic obstruction",
            "Q0 item E1, Appendix M"),
        QIIGAppendixPEntry("QIIG_probability_boundary", "Probability/matter boundary",
            "bounded_structural_result",
            "Matter inherits diagnostic weights only; Born rule requires postulate",
            "Diagnostic weights are matter probabilities",
            "Q-II.F probability audit"),
        QIIGAppendixPEntry("QIIG_r_entry_conditions", "Appendix R entry conditions",
            "bounded_structural_result",
            "Formal entry conditions for Appendix R documented",
            "Entry conditions imply matter program will succeed",
            "All Q-II.G tracks"),
        QIIGAppendixPEntry("QIIG_readiness_table", "Readiness-level table",
            "bounded_structural_result",
            "10 matter-relevant domains classified by readiness level",
            "Readiness classification implies matter readiness achieved",
            "All Q Part I and Part II results"),
        QIIGAppendixPEntry("QIIG_overall", "Q-II.G overall",
            "bounded_structural_result",
            "Quantum matter-readiness map complete; Appendix R authorized with flags",
            "Readiness map implies quantum-to-matter transition solved",
            "All Q-II.G tracks"),
    ]
    return QIIGAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIIG_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["5 BSR (boundaries/absences documented), 1 MBU (bosonic readiness)",
               "Overall: BSR — this is a readiness map, not a derivation"],
    )


def _build_track_i() -> QIIGNonclaimFirewall:
    return QIIGNonclaimFirewall(
        nonclaims=QIIG_NONCLAIMS, n_nonclaims=N_QIIG_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_qiig_quantum_matter_readiness_map() -> QIIGQuantumMatterReadinessResult:
    """Run the full Q-II.G Quantum Matter-Readiness Map."""
    ta = _build_track_a()
    tb = _build_track_b()
    tc = _build_track_c()
    td = _build_track_d()
    te = _build_track_e()
    tf = _build_track_f()
    tg = _build_track_g()
    th = _build_track_h()
    ti = _build_track_i()

    allowed_claims: List[str] = [
        "Quantum-to-matter handoff inventory complete: 9 items classified "
        "(2 ready, 5 extension-ready, 1 precondition, 1 blocked)",
        "Bosonic pre-matter readiness advanced: state grammar, excitations, "
        "constitutive bridge, and composite structure all available at extension level",
        "Fermionic obstruction unchanged: Q0 3-layer block (pi_2(S^2) = Z) "
        "not affected by quantum program",
        "Probability/matter boundary established: diagnostic weights only; "
        "Born rule requires explicit MIP postulate for matter use",
        "Readiness-level table: 1 ready, 5 extension-ready, 3 precondition, 1 blocked "
        "across 10 matter-relevant domains",
        "Appendix R entry conditions formalized: 4 assumptions, 5 extension flags, "
        "5 prohibitions, 3 re-audit requirements",
        "Appendix R authorized with explicit extension flags to begin matter program",
    ]

    forbidden_claims: List[str] = [
        "Many-mode excitations imply particles",
        "Entanglement implies matter binding",
        "Pointer structure implies classical matter ontology",
        "Diagnostic weights imply matter probabilities",
        "Bosonic excitation grammar implies bosonic matter closure",
        "Second-wave quantum structure dissolves fermionic obstruction",
        "Extension-ready implies native matter canon",
    ]

    diagnostics: Dict[str, Any] = {
        "n_handoff_items": N_HANDOFF_ITEMS,
        "n_handoff_ready": ta.n_ready,
        "n_handoff_extension_ready": ta.n_extension_ready,
        "n_handoff_precondition": ta.n_precondition,
        "n_handoff_blocked": ta.n_blocked,
        "n_readiness_domains": N_READINESS_DOMAINS,
        "n_domains_ready": tf.n_ready,
        "n_domains_extension_ready": tf.n_extension_ready,
        "n_domains_precondition": tf.n_precondition,
        "n_domains_blocked": tf.n_blocked,
        "born_rule_derived": te.born_rule_derived,
        "fermionic_obstruction_changed": tc.obstruction_changed,
        "particle_ontology_ready": tb.particle_like_readiness,
        "bound_state_ready": tb.bound_state_readiness,
        "n_r_assumes": len(tg.r_may_assume),
        "n_r_extension_flags": len(tg.r_must_carry_extension_flags),
        "n_r_must_not_assume": len(tg.r_must_not_assume),
        "n_r_must_reaudit": len(tg.r_must_reaudit),
        "n_nonclaims": N_QIIG_NONCLAIMS,
    }

    result = QIIGQuantumMatterReadinessResult(
        valid=True,
        track_a_handoff=ta, track_b_bosonic=tb,
        track_c_fermionic=tc, track_d_bound_state=td,
        track_e_probability=te, track_f_readiness_table=tf,
        track_g_r_entry=tg, track_h_appendix_p=th,
        track_i_nonclaims=ti,
        bosonic_readiness_verdict=tb.bosonic_readiness_verdict,
        fermionic_readiness_verdict=tc.fermionic_readiness_verdict,
        probability_boundary_verdict=te.probability_boundary_verdict,
        appendix_r_entry_verdict=tg.appendix_r_entry_verdict,
        overall_q_to_r_verdict=QIIG_OVERALL_VERDICT,
        qiig_appendix_p_class=QIIG_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIIG_NONCLAIMS,
        diagnostics=diagnostics,
    )
    validate_qiig_result(result)
    return result


def validate_qiig_result(result: QIIGQuantumMatterReadinessResult) -> None:
    checks = [
        (result.bosonic_readiness_verdict, ALLOWED_BOSONIC_VERDICTS, "Bosonic"),
        (result.fermionic_readiness_verdict, ALLOWED_FERMIONIC_VERDICTS, "Fermionic"),
        (result.probability_boundary_verdict, ALLOWED_PROBABILITY_BOUNDARY_VERDICTS, "Probability"),
        (result.appendix_r_entry_verdict, ALLOWED_APPENDIX_R_ENTRY_VERDICTS, "R entry"),
        (result.overall_q_to_r_verdict, ALLOWED_OVERALL_VERDICTS, "Overall"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.qiig_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class not in allowed")
    for e in result.track_h_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}': class not in allowed")
    if result.track_i_nonclaims.n_nonclaims != N_QIIG_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_i_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_h_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if result.track_e_probability.born_rule_derived:
        raise ValueError("born_rule_derived must be False")
    if result.track_c_fermionic.obstruction_changed:
        raise ValueError("fermionic obstruction_changed must be False")
    if result.track_b_bosonic.particle_like_readiness:
        raise ValueError("particle_like_readiness must be False")
    # Handoff counts
    hi = result.track_a_handoff
    if hi.n_items != N_HANDOFF_ITEMS:
        raise ValueError(f"Handoff items: {hi.n_items} != {N_HANDOFF_ITEMS}")
    n_r = sum(1 for i in hi.items if i.readiness == "ready")
    if n_r != hi.n_ready:
        raise ValueError("Handoff ready count mismatch")
    # Readiness table
    rt = result.track_f_readiness_table
    if rt.n_entries != N_READINESS_DOMAINS:
        raise ValueError(f"Readiness entries: {rt.n_entries} != {N_READINESS_DOMAINS}")
    for e in rt.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"'{e.domain}': level '{e.readiness_level}' not allowed")
    # R entry conditions counts
    rg = result.track_g_r_entry
    if len(rg.r_may_assume) != N_R_ASSUMES:
        raise ValueError(f"r_may_assume: {len(rg.r_may_assume)} != {N_R_ASSUMES}")
    if len(rg.r_must_carry_extension_flags) != N_R_EXTENSION_FLAGS:
        raise ValueError(f"extension_flags: {len(rg.r_must_carry_extension_flags)} != {N_R_EXTENSION_FLAGS}")
    if len(rg.r_must_not_assume) != N_R_MUST_NOT_ASSUME:
        raise ValueError(f"must_not_assume: {len(rg.r_must_not_assume)} != {N_R_MUST_NOT_ASSUME}")
    if len(rg.r_must_reaudit) != N_R_MUST_REAUDIT:
        raise ValueError(f"must_reaudit: {len(rg.r_must_reaudit)} != {N_R_MUST_REAUDIT}")


def _self_test() -> bool:
    r = run_qiig_quantum_matter_readiness_map()
    assert r.valid is True
    assert r.bosonic_readiness_verdict == QIIG_BOSONIC_VERDICT
    assert r.fermionic_readiness_verdict == QIIG_FERMIONIC_VERDICT
    assert r.probability_boundary_verdict == QIIG_PROBABILITY_BOUNDARY_VERDICT
    assert r.appendix_r_entry_verdict == QIIG_APPENDIX_R_ENTRY_VERDICT
    assert r.overall_q_to_r_verdict == QIIG_OVERALL_VERDICT
    assert r.diagnostics["born_rule_derived"] is False
    assert r.diagnostics["fermionic_obstruction_changed"] is False
    assert r.diagnostics["particle_ontology_ready"] is False
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.G self-test passed.")
