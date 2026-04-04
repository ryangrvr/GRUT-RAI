"""
Appendix R-B --- Bosonic Objecthood and Localization Audit
==========================================================
GRUT Matter Program --- Phase R-B  (First Substantive Matter Stage)

This module audits what forms of bosonic objecthood and localization are
justified in GRUT, given the completed pre-matter (M/N/O), quantum (Q),
and matter-entry (R0/R-A) audits.

Inherited from Appendix M (Bosonic Object Audit):
  - particle_candidate_not_yet_established
  - shell_localization_only (boundary-confined, not free-space localized)
  - distributed_profile_without_objecthood
  - Derrick obstruction: static scalar solitons unstable in d >= 2

Inherited from Appendix N (Skyrme Nativity):
  - no_native_skyrme_support_found
  - effective_skyrme_analog_possible (motivated_but_unbuilt)
  - L4 Skyrme term would stabilize against Derrick collapse

Inherited from Appendix O (O(3) Nativity):
  - O(3) sigma model as motivated_independent_postulation
  - Topological charge pi_2(S^2) = Z: integer winding numbers
  - Target-space topology provides localization seed (topological defects)

Inherited from Q program:
  - Extension-level bosonic state grammar (C^2 per site, tensor product)
  - Dissipative excitation structure (sigma_+/sigma_-, H_hop)
  - Decoherence and pointer-basis selection per site
  - Diagnostic weights (not probabilities)
  - No particle ontology, no Fock space, no dispersion relation

Key analysis
------------
Objecthood requires MORE than localization. A bosonic "object" must satisfy:
  1. Localization: spatially/configurationally concentrated structure
  2. Persistence: survives over timescales >> tau
  3. Identifiable support: distinguishable from background
  4. Distinguishability: can be told apart from other configurations
  5. Stability: resistant to small perturbations
  6. Admissible state description: quantum state can be assigned

GRUT currently provides:
  - Profile localization: constitutive field Phi(x) can have concentrated profiles
    (classical level, from GRUT ODE/PDE structure)
  - Shell localization: boundary-confined configurations (Appendix M)
  - Topological localization: winding-number defects (Appendix O, if O(3) postulated)
  - Excitation localization: site-specific excitations on qubit chain (Q-II.E)

None of these individually constitute "objecthood" in the particle sense.
The strongest current candidate is: topological defect in O(3) sigma model
with Skyrme stabilization — but this is extension-level (O(3) is MIP,
Skyrme is MBU) and classical (quantum overlay from Q-II.E does not give
particle ontology).
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

# Track counts
N_OBJECTHOOD_CRITERIA: int = 6
N_LOCALIZATION_CANDIDATES: int = 6
N_PERSISTENCE_CANDIDATES: int = 6
N_MNO_ITEMS: int = 5
N_QUANTUM_CONTRIBUTIONS: int = 6
N_BENCHMARK_CANDIDATES: int = 4
N_READINESS_DOMAINS: int = 6
N_PROBABILITY_TESTS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_RB_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
M_INHERITED: str = "particle_candidate_not_yet_established"
N_INHERITED: str = "no_native_skyrme_support_found"
O_INHERITED: str = "o3_motivated_independent_postulation"
R0_INHERITED: str = "matter_entry_inventory_complete__all_items_documented"

# R-B Verdict strings
RB_LOCALIZATION_VERDICT: str = "shell_and_excitation_localization_only"
RB_PERSISTENCE_VERDICT: str = "persistence_criteria_partially_satisfied"
RB_OBJECTHOOD_VERDICT: str = "bosonic_objecthood_structurally_plausible_but_unbuilt"
RB_TOPOLOGICAL_ROUTE_VERDICT: str = "topological_object_route_motivated_but_unbuilt"
RB_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_RC"
RB_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozensets
ALLOWED_LOCALIZATION_VERDICTS: frozenset = frozenset({
    "localization_beyond_profile_demonstrated",
    "shell_and_excitation_localization_only",
    "localization_extension_level_only",
    "localization_blocked",
})
ALLOWED_PERSISTENCE_VERDICTS: frozenset = frozenset({
    "persistence_criteria_partially_satisfied",
    "persistence_extension_level_only",
    "persistence_precondition_only",
    "persistence_blocked",
})
ALLOWED_OBJECTHOOD_VERDICTS: frozenset = frozenset({
    "bosonic_object_candidate_extension_ready",
    "bosonic_objecthood_structurally_plausible_but_unbuilt",
    "bosonic_objecthood_not_yet_established",
    "bosonic_particle_like_status_blocked",
})
ALLOWED_TOPOLOGICAL_VERDICTS: frozenset = frozenset({
    "topological_object_route_extension_ready",
    "topological_object_route_motivated_but_unbuilt",
    "topological_object_route_still_precondition_only",
    "topological_object_route_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_RC",
    "authorized_only_for_further_objecthood_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_MNO_or_QIIG",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})
ALLOWED_READINESS_LEVELS: frozenset = frozenset({
    "ready", "extension_ready", "precondition_only", "blocked",
})

RB_NONCLAIMS: List[str] = [
    "NOT_claiming_dissipative_excitation_therefore_particle__"
    "site_excitation_is_qubit_bookkeeping_not_particle_ontology",
    "NOT_claiming_shell_localization_therefore_bosonic_object_closure__"
    "shell_confinement_is_boundary_effect_not_free_space_objecthood",
    "NOT_claiming_topological_charge_therefore_stable_object__"
    "winding_number_is_conserved_quantity_not_stability_proof",
    "NOT_claiming_O3_extension_therefore_bosonic_matter_solved__"
    "O3_sigma_model_is_MIP_not_native_bosonic_derivation",
    "NOT_claiming_many_mode_grammar_therefore_localized_bosonic_ontology__"
    "N_site_chain_has_no_spatial_localization",
    "NOT_claiming_extension_level_object_candidate_therefore_native_canon__"
    "all_RB_results_carry_MBU_or_MIP_floor",
    "NOT_claiming_object_benchmark_therefore_bound_state__"
    "localization_plus_persistence_is_not_binding",
    "NOT_claiming_bosonic_objecthood_progress_therefore_fermionic_route_reopened__"
    "fermionic_3_layer_obstruction_unchanged",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RBObjecthoodCriterion:
    criterion_id: str
    criterion_name: str
    description: str
    currently_satisfied: str  # "satisfied", "partially", "not_satisfied", "extension_level"
    notes: List[str]

@dataclass
class RBObjecthoodCriteriaAudit:
    criteria: List[RBObjecthoodCriterion]
    n_criteria: int
    n_satisfied: int
    n_partial: int
    n_not_satisfied: int
    notes: List[str]

@dataclass
class RBLocalizationCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    available: bool
    localization_type: str
    notes: List[str]

@dataclass
class RBLocalizationAudit:
    candidates: List[RBLocalizationCandidate]
    n_candidates: int
    n_available: int
    localization_verdict: str
    notes: List[str]

@dataclass
class RBPersistenceCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    satisfied: bool
    level: str
    notes: List[str]

@dataclass
class RBPersistenceAudit:
    candidates: List[RBPersistenceCandidate]
    n_candidates: int
    n_satisfied: int
    persistence_verdict: str
    notes: List[str]

@dataclass
class RBMNOItem:
    item_id: str
    item_name: str
    original_verdict: str
    changed_by_q: bool
    current_status: str
    notes: List[str]

@dataclass
class RBMNOInheritanceAudit:
    items: List[RBMNOItem]
    n_items: int
    any_changed: bool
    notes: List[str]

@dataclass
class RBQuantumContribution:
    contribution_id: str
    contribution_name: str
    adds_objecthood: bool
    adds_readiness_only: bool
    notes: List[str]

@dataclass
class RBQuantumToObjecthoodAudit:
    contributions: List[RBQuantumContribution]
    n_contributions: int
    n_adds_objecthood: int
    notes: List[str]

@dataclass
class RBBenchmarkCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    demonstrates: List[str]
    does_not_demonstrate: List[str]
    notes: List[str]

@dataclass
class RBBenchmarkAudit:
    candidates: List[RBBenchmarkCandidate]
    n_candidates: int
    n_viable: int
    chosen_id: str
    notes: List[str]

@dataclass
class RBReadinessEntry:
    domain: str
    readiness_level: str
    notes: str

@dataclass
class RBReadinessTable:
    entries: List[RBReadinessEntry]
    n_entries: int

@dataclass
class RBProbabilityTest:
    test_id: str
    test_name: str
    result: str
    notes: List[str]

@dataclass
class RBProbabilityBoundaryAudit:
    tests: List[RBProbabilityTest]
    n_tests: int
    objecthood_independent_of_probability: bool
    notes: List[str]

@dataclass
class RBAppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str

@dataclass
class RBAppendixPAudit:
    entries: List[RBAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]

@dataclass
class RBAuthorizationAudit:
    rc_authorized: bool
    authorization_basis: List[str]
    rc_constraints: List[str]
    authorization_verdict: str
    notes: List[str]

@dataclass
class RBNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool

@dataclass
class RBBosonicObjecthoodResult:
    valid: bool
    track_a_objecthood: RBObjecthoodCriteriaAudit
    track_b_localization: RBLocalizationAudit
    track_c_persistence: RBPersistenceAudit
    track_d_mno: RBMNOInheritanceAudit
    track_e_quantum: RBQuantumToObjecthoodAudit
    track_f_benchmark: RBBenchmarkAudit
    track_g_readiness: RBReadinessTable
    track_h_probability: RBProbabilityBoundaryAudit
    track_i_appendix_p: RBAppendixPAudit
    track_j_authorization: RBAuthorizationAudit
    track_k_nonclaims: RBNonclaimFirewall
    localization_verdict: str
    persistence_verdict: str
    objecthood_verdict: str
    topological_route_verdict: str
    authorization_verdict: str
    rb_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> RBObjecthoodCriteriaAudit:
    criteria = [
        RBObjecthoodCriterion("OC1", "localization",
            "Spatially or configurationally concentrated structure.",
            "partially",
            ["Shell localization (M): boundary-confined, not free-space",
             "Topological localization (O): winding defects if O(3) postulated",
             "Excitation localization (Q-II.E): site-specific, no spatial DOF"]),
        RBObjecthoodCriterion("OC2", "persistence",
            "Survives over timescales significantly longer than tau.",
            "partially",
            ["Constitutive attractor: persists (classical level)",
             "Topological charge: conserved (if O(3))",
             "Dissipative excitation: decays at rate gamma (transient)"]),
        RBObjecthoodCriterion("OC3", "identifiable_support",
            "Distinguishable support region in configuration space.",
            "extension_level",
            ["Topological defect has identifiable winding structure",
             "Shell has identifiable boundary",
             "Both require O(3) or boundary to be specified"]),
        RBObjecthoodCriterion("OC4", "distinguishability",
            "Can be told apart from other configurations and background.",
            "extension_level",
            ["Winding number provides integer label (distinguishable charges)",
             "Requires O(3) postulation for winding; extension-level"]),
        RBObjecthoodCriterion("OC5", "stability",
            "Resistant to small perturbations.",
            "not_satisfied",
            ["Derrick obstruction: static solitons unstable in d >= 2 without Skyrme",
             "Skyrme term (N): MBU, not yet installed",
             "No current stability proof for bosonic object candidates"]),
        RBObjecthoodCriterion("OC6", "admissible_state_description",
            "Quantum state can be coherently assigned to the object.",
            "extension_level",
            ["Density matrix on qubit chain: extension-level state description",
             "No Fock space or particle-state formalism",
             "State description available but not particle-level"]),
    ]
    n_s = sum(1 for c in criteria if c.currently_satisfied == "satisfied")
    n_p = sum(1 for c in criteria if c.currently_satisfied == "partially")
    n_n = sum(1 for c in criteria if c.currently_satisfied == "not_satisfied")
    return RBObjecthoodCriteriaAudit(
        criteria=criteria, n_criteria=N_OBJECTHOOD_CRITERIA,
        n_satisfied=n_s, n_partial=n_p, n_not_satisfied=n_n,
        notes=["0 fully satisfied, 2 partially (localization, persistence), "
               "3 extension-level, 1 not satisfied (stability)",
               "Key blocker: stability (OC5) requires Skyrme term (MBU)"],
    )


def _build_track_b() -> RBLocalizationAudit:
    candidates = [
        RBLocalizationCandidate("LC1", "distributed_constitutive_profile",
            "Phi(x) field profile: classical, distributed, no sharp boundary.",
            True, "profile_only",
            ["Native GRUT: constitutive field has spatial profile",
             "Not localized in object sense: no sharp boundary"]),
        RBLocalizationCandidate("LC2", "shell_boundary_localization",
            "Barrier/shell confinement from GRUT boundary structure.",
            True, "shell_confined",
            ["Appendix M: shell localization established",
             "Boundary-confined, not free-space localized object"]),
        RBLocalizationCandidate("LC3", "topological_localization",
            "Winding-number defect in O(3) sigma model.",
            True, "topological",
            ["Appendix O: O(3) MIP provides topological defect structure",
             "Localization via topological charge concentration",
             "Extension-level: requires O(3) postulation"]),
        RBLocalizationCandidate("LC4", "dissipative_mode_localization",
            "Site-specific excitation on qubit chain.",
            True, "excitation_only",
            ["Q-II.E: sigma_+ on site i creates site-localized excitation",
             "No spatial DOF; 'localization' is in site-label space only"]),
        RBLocalizationCandidate("LC5", "composite_benchmark_localization",
            "Localization within composite Hilbert space structure.",
            False, "not_spatial",
            ["Not viable: composite C^4 has no spatial interpretation",
             "Hilbert-space structure is algebraic, not geometric"]),
        RBLocalizationCandidate("LC6", "no_localization",
            "No coherent localization.", False, "null",
            ["Rejected: LC1-LC4 provide various localization forms"]),
    ]
    n_a = sum(1 for c in candidates if c.available)
    return RBLocalizationAudit(
        candidates=candidates, n_candidates=N_LOCALIZATION_CANDIDATES,
        n_available=n_a, localization_verdict=RB_LOCALIZATION_VERDICT,
        notes=["4 localization forms available: profile, shell, topological, excitation",
               "None constitutes object-level localization by itself",
               "Shell + topological = strongest combination (extension-level)",
               "Verdict: shell_and_excitation_localization_only"],
    )


def _build_track_c() -> RBPersistenceAudit:
    candidates = [
        RBPersistenceCandidate("PS1", "constitutive_attractor",
            "Phi relaxes to attractor: tau d<Phi>/dt + <Phi> = <X>.",
            True, "native",
            ["Classical attractor: persists indefinitely once reached",
             "Part I locked result"]),
        RBPersistenceCandidate("PS2", "shell_supported",
            "Shell/boundary provides persistent confinement.",
            True, "native",
            ["Appendix M: shell is a boundary condition, not dynamic",
             "Persists as long as boundary exists"]),
        RBPersistenceCandidate("PS3", "dissipative_excitation",
            "Qubit excitation decays at rate gamma = 1/tau.",
            False, "transient",
            ["Transient: excitation decays to ground state",
             "Persistence timescale = tau (constitutive timescale)",
             "Not persistent enough for objecthood"]),
        RBPersistenceCandidate("PS4", "topological_persistence",
            "Topological charge conserved: winding number is integer.",
            True, "extension_level",
            ["If O(3) postulated: topological charge is exactly conserved",
             "Strongest persistence mechanism (topological protection)",
             "Extension-level: requires O(3) MIP"]),
        RBPersistenceCandidate("PS5", "skyrme_stabilization",
            "Skyrme L4 term prevents Derrick collapse.",
            False, "extension_unbuilt",
            ["Appendix N: Skyrme term is MBU",
             "Would stabilize topological defect against radial collapse",
             "Not yet installed: extension path identified but unbuilt"]),
        RBPersistenceCandidate("PS6", "no_persistence",
            "No persistence.", False, "null",
            ["Rejected: PS1, PS2, PS4 provide persistence forms"]),
    ]
    n_s = sum(1 for c in candidates if c.satisfied)
    return RBPersistenceAudit(
        candidates=candidates, n_candidates=N_PERSISTENCE_CANDIDATES,
        n_satisfied=n_s, persistence_verdict=RB_PERSISTENCE_VERDICT,
        notes=["3 satisfied: attractor (native), shell (native), topological (extension)",
               "1 transient: excitation decays at rate gamma",
               "1 unbuilt: Skyrme stabilization (MBU)",
               "Verdict: persistence_criteria_partially_satisfied"],
    )


def _build_track_d() -> RBMNOInheritanceAudit:
    items = [
        RBMNOItem("MNO1", "appendix_m_particle_status",
            "particle_candidate_not_yet_established", False, "unchanged",
            ["Q program did not establish particle candidacy"]),
        RBMNOItem("MNO2", "appendix_m_shell_localization",
            "shell_localization_only", False, "unchanged",
            ["Shell localization still the native localization form"]),
        RBMNOItem("MNO3", "appendix_n_skyrme_status",
            "no_native_skyrme_support_found", False, "unchanged",
            ["Skyrme term still MBU; Q program did not build it"]),
        RBMNOItem("MNO4", "appendix_o_o3_status",
            "o3_motivated_independent_postulation", False, "unchanged",
            ["O(3) still MIP; Q program did not promote it"]),
        RBMNOItem("MNO5", "derrick_obstruction",
            "derrick_obstruction_present", False, "unchanged",
            ["Static solitons unstable in d >= 2 without Skyrme stabilizer"]),
    ]
    any_changed = any(i.changed_by_q for i in items)
    return RBMNOInheritanceAudit(
        items=items, n_items=N_MNO_ITEMS, any_changed=any_changed,
        notes=["ALL 5 M/N/O items UNCHANGED by Q program",
               "Q program improved quantum READINESS but not classical OBJECTHOOD",
               "Particle candidacy, Skyrme status, O(3) status: all locked"],
    )


def _build_track_e() -> RBQuantumToObjecthoodAudit:
    contributions = [
        RBQuantumContribution("QO1", "state_grammar_for_candidates",
            False, True,
            ["C^2 per site: state description available but not objecthood"]),
        RBQuantumContribution("QO2", "excitation_grammar",
            False, True,
            ["sigma_+/sigma_-: excitation language, not object language"]),
        RBQuantumContribution("QO3", "composite_grammar",
            False, True,
            ["Tensor product: enables multi-part description, not binding"]),
        RBQuantumContribution("QO4", "decoherence_pointer_selection",
            False, True,
            ["Pointer basis: selects classical-looking sector, aids interpretation"]),
        RBQuantumContribution("QO5", "diagnostic_weights",
            False, True,
            ["Density-matrix diagonals: mathematical tools for object description"]),
        RBQuantumContribution("QO6", "no_objecthood_from_quantum",
            False, False,
            ["Q program adds READINESS, not OBJECTHOOD",
             "No quantum result by itself establishes bosonic object"]),
    ]
    n_obj = sum(1 for c in contributions if c.adds_objecthood)
    return RBQuantumToObjecthoodAudit(
        contributions=contributions, n_contributions=N_QUANTUM_CONTRIBUTIONS,
        n_adds_objecthood=n_obj,
        notes=["Q program adds 0 objecthood contributions, 5 readiness contributions",
               "Quantum overlay improves description, not ontology",
               "Objecthood requires classical localization + stability first"],
    )


def _build_track_f() -> RBBenchmarkAudit:
    candidates = [
        RBBenchmarkCandidate("OB1", "shell_plus_excitation_benchmark",
            "Shell-confined region with qubit excitation overlay: "
            "shell (M) provides localization, excitation (Q-II.E) provides "
            "quantum state, decoherence selects pointer basis.",
            True,
            ["shell_localization", "excitation_state_overlay",
             "decoherence_pointer_selection", "diagnostic_weight_description"],
            ["free_space_localization", "stability_proof",
             "particle_identity", "bound_state_structure"],
            ["Minimal benchmark combining M + Q results"]),
        RBBenchmarkCandidate("OB2", "topological_defect_benchmark",
            "O(3) winding-number defect with quantum state overlay.",
            True,
            ["topological_localization", "charge_conservation",
             "quantum_state_on_defect", "strongest_persistence"],
            ["skyrme_stability", "particle_ontology", "spatial_dynamics"],
            ["Extension-level: requires O(3) MIP + quantum overlay"]),
        RBBenchmarkCandidate("OB3", "dissipative_excitation_only",
            "Site excitation on qubit chain without classical localization.",
            True,
            ["site_excitation", "dissipative_propagation"],
            ["spatial_localization", "persistence", "objecthood"],
            ["Weakest: excitation only, no classical localization support"]),
        RBBenchmarkCandidate("OB4", "no_benchmark",
            "No admissible benchmark.", False, [], [],
            ["Rejected: OB1-OB3 are viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return RBBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_id="OB1_shell_plus_excitation_benchmark",
        notes=["OB1 chosen: shell + excitation (M + Q combination)",
               "OB2 also strong: topological defect + quantum (O + Q)",
               "Neither demonstrates objecthood; both demonstrate readiness",
               "Particle-like status not achieved by any benchmark"],
    )


def _build_track_g() -> RBReadinessTable:
    entries = [
        RBReadinessEntry("bosonic_localization", "extension_ready",
            "Shell + topological + excitation forms available"),
        RBReadinessEntry("bosonic_persistence", "extension_ready",
            "Attractor + shell + topological persistence; Skyrme unbuilt"),
        RBReadinessEntry("bosonic_object_candidate", "precondition_only",
            "Localization + persistence partially satisfied; stability gap"),
        RBReadinessEntry("bosonic_particle_like", "precondition_only",
            "No Fock space, no particle identity, no dispersion"),
        RBReadinessEntry("bosonic_bound_structure", "precondition_only",
            "Composite grammar available; no binding mechanism"),
        RBReadinessEntry("topological_object_route", "extension_ready",
            "O(3) + Skyrme path identified; both extension-level"),
    ]
    return RBReadinessTable(entries=entries, n_entries=N_READINESS_DOMAINS)


def _build_track_h() -> RBProbabilityBoundaryAudit:
    tests = [
        RBProbabilityTest("PB1", "localization_independent_of_probability",
            "independent",
            ["Localization is geometric/topological, not probabilistic"]),
        RBProbabilityTest("PB2", "persistence_independent_of_probability",
            "independent",
            ["Persistence is dynamic/topological, not probabilistic"]),
        RBProbabilityTest("PB3", "objecthood_criteria_mostly_independent",
            "mostly_independent",
            ["5 of 6 criteria are structural; state description (OC6) "
             "uses density matrix but not Born-rule probability"]),
        RBProbabilityTest("PB4", "interpretive_objecthood_may_need_born",
            "conditional",
            ["If matter program later asks 'what is the probability of "
             "finding the object here?', Born rule needed",
             "Structural objecthood criteria do not require probability"]),
    ]
    return RBProbabilityBoundaryAudit(
        tests=tests, n_tests=N_PROBABILITY_TESTS,
        objecthood_independent_of_probability=True,
        notes=["Structural objecthood criteria (localization, persistence, stability) "
               "are independent of probability",
               "Interpretive questions (detection probability) would need Born rule",
               "Current R-B audit is structural, not interpretive"],
    )


def _build_track_i() -> RBAppendixPAudit:
    entries = [
        RBAppendixPEntry("RB_localization", "Localization forms",
            "motivated_but_unbuilt",
            "Shell, topological, and excitation localization available",
            "Localization forms imply free-space objecthood",
            "Appendices M, O, Q-II.E"),
        RBAppendixPEntry("RB_persistence", "Persistence criteria",
            "motivated_but_unbuilt",
            "Attractor, shell, and topological persistence partially satisfied",
            "Persistence criteria imply stable particle",
            "Part I, Appendices M, O"),
        RBAppendixPEntry("RB_objecthood", "Objecthood status",
            "motivated_but_unbuilt",
            "Bosonic objecthood structurally plausible but unbuilt",
            "Bosonic objecthood established or particles derived",
            "All R-B tracks; stability gap (Skyrme MBU)"),
        RBAppendixPEntry("RB_topological_route", "Topological object route",
            "motivated_but_unbuilt",
            "O(3) + Skyrme route identified; extension-level",
            "Topological objects are native GRUT particles",
            "Appendices N, O"),
        RBAppendixPEntry("RB_mno_unchanged", "M/N/O inheritance unchanged",
            "bounded_structural_result",
            "All M/N/O limits preserved; Q program did not change objecthood",
            "Q program upgraded M/N/O objecthood status",
            "Appendices M, N, O; Q-II.G"),
        RBAppendixPEntry("RB_quantum_readiness_only", "Q adds readiness only",
            "bounded_structural_result",
            "Quantum program adds readiness language, not objecthood",
            "Quantum excitation grammar establishes bosonic objects",
            "Q-II.E, Q-II.G"),
        RBAppendixPEntry("RB_overall", "R-B overall",
            "motivated_but_unbuilt",
            "Bosonic objecthood investigated; structurally plausible, unbuilt",
            "Bosonic matter closure or particle derivation achieved",
            "All R-B tracks"),
    ]
    return RBAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RB_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["4 MBU, 2 BSR, 1 MBU (overall); no native canon"],
    )


def _build_track_j() -> RBAuthorizationAudit:
    return RBAuthorizationAudit(
        rc_authorized=True,
        authorization_basis=[
            "localization_forms_documented_shell_topological_excitation",
            "persistence_criteria_partially_satisfied",
            "objecthood_structurally_plausible_but_stability_gap_identified",
            "topological_route_motivated_but_unbuilt",
            "mno_inheritance_preserved_and_documented",
        ],
        rc_constraints=[
            "RC_must_address_stability_gap_Skyrme_or_alternative",
            "RC_must_not_assume_objecthood_established_by_RB",
            "RC_must_investigate_binding_mechanism_for_bound_structures",
            "RC_results_inherit_MBU_or_MIP_floor",
            "RC_must_preserve_fermionic_obstruction",
        ],
        authorization_verdict=RB_AUTHORIZATION_VERDICT,
        notes=["R-C authorized: objecthood investigation sufficient for stabilization work",
               "Key gap for R-C: stability (Skyrme MBU) is the main target",
               "R-C must also address binding mechanism for bound structure"],
    )


def _build_track_k() -> RBNonclaimFirewall:
    return RBNonclaimFirewall(
        nonclaims=RB_NONCLAIMS, n_nonclaims=N_RB_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_rb_bosonic_objecthood_localization_audit() -> RBBosonicObjecthoodResult:
    ta = _build_track_a()
    tb = _build_track_b()
    tc = _build_track_c()
    td = _build_track_d()
    te = _build_track_e()
    tf = _build_track_f()
    tg = _build_track_g()
    th = _build_track_h()
    ti = _build_track_i()
    tj = _build_track_j()
    tk = _build_track_k()

    allowed_claims: List[str] = [
        "Shell, topological, and excitation localization forms all available "
        "(shell native, topological extension-level, excitation extension-level)",
        "Persistence criteria partially satisfied: attractor and shell (native), "
        "topological charge (extension-level), excitation transient (not persistent)",
        "Bosonic objecthood structurally plausible but unbuilt: stability gap "
        "(Derrick obstruction, Skyrme MBU) is the main blocker",
        "Topological object route (O(3) + Skyrme) motivated but unbuilt: "
        "strongest path to bosonic objecthood",
        "All M/N/O limits preserved: Q program added readiness, not objecthood",
        "Quantum program contributes readiness language (state grammar, excitations, "
        "decoherence) but zero objecthood contributions",
        "R-C authorized: stabilization and binding investigation next",
    ]

    forbidden_claims: List[str] = [
        "Dissipative excitation implies particle",
        "Shell localization implies bosonic object closure",
        "Topological charge implies stable object",
        "O(3) extension implies bosonic matter solved",
        "Many-mode grammar implies localized bosonic ontology",
        "Extension-level object candidate implies native canon",
        "Object benchmark implies bound state",
    ]

    diagnostics: Dict[str, Any] = {
        "n_objecthood_criteria": N_OBJECTHOOD_CRITERIA,
        "n_criteria_satisfied": ta.n_satisfied,
        "n_criteria_partial": ta.n_partial,
        "n_criteria_not_satisfied": ta.n_not_satisfied,
        "n_localization_available": tb.n_available,
        "n_persistence_satisfied": tc.n_satisfied,
        "mno_any_changed": td.any_changed,
        "quantum_adds_objecthood": te.n_adds_objecthood,
        "n_benchmark_viable": tf.n_viable,
        "objecthood_independent_of_probability": th.objecthood_independent_of_probability,
        "n_nonclaims": N_RB_NONCLAIMS,
    }

    result = RBBosonicObjecthoodResult(
        valid=True,
        track_a_objecthood=ta, track_b_localization=tb,
        track_c_persistence=tc, track_d_mno=td,
        track_e_quantum=te, track_f_benchmark=tf,
        track_g_readiness=tg, track_h_probability=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        localization_verdict=tb.localization_verdict,
        persistence_verdict=tc.persistence_verdict,
        objecthood_verdict=RB_OBJECTHOOD_VERDICT,
        topological_route_verdict=RB_TOPOLOGICAL_ROUTE_VERDICT,
        authorization_verdict=tj.authorization_verdict,
        rb_appendix_p_class=RB_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RB_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_rb_result(result)
    return result


def validate_rb_result(result: RBBosonicObjecthoodResult) -> None:
    checks = [
        (result.localization_verdict, ALLOWED_LOCALIZATION_VERDICTS, "Localization"),
        (result.persistence_verdict, ALLOWED_PERSISTENCE_VERDICTS, "Persistence"),
        (result.objecthood_verdict, ALLOWED_OBJECTHOOD_VERDICTS, "Objecthood"),
        (result.topological_route_verdict, ALLOWED_TOPOLOGICAL_VERDICTS, "Topological"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.rb_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class not in allowed")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}': class not in allowed")
    if result.track_k_nonclaims.n_nonclaims != N_RB_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.rc_authorized:
        raise ValueError("rc_authorized must be True")
    if result.track_d_mno.any_changed:
        raise ValueError("MNO any_changed must be False")
    if result.track_e_quantum.n_adds_objecthood != 0:
        raise ValueError("Quantum adds_objecthood must be 0")
    for e in result.track_g_readiness.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"Readiness '{e.domain}': level invalid")


def _self_test() -> bool:
    r = run_rb_bosonic_objecthood_localization_audit()
    assert r.valid is True
    assert r.localization_verdict == RB_LOCALIZATION_VERDICT
    assert r.persistence_verdict == RB_PERSISTENCE_VERDICT
    assert r.objecthood_verdict == RB_OBJECTHOOD_VERDICT
    assert r.topological_route_verdict == RB_TOPOLOGICAL_ROUTE_VERDICT
    assert r.authorization_verdict == RB_AUTHORIZATION_VERDICT
    assert r.diagnostics["mno_any_changed"] is False
    assert r.diagnostics["quantum_adds_objecthood"] == 0
    return True


if __name__ == "__main__":
    _self_test()
    print("R-B self-test passed.")
