"""
Appendix R-E --- Fermionic Matter Boundary and Extension Routes Audit
=====================================================================
GRUT Matter Program --- Phase R-E

Audits what fermionic routes exist, what remains blocked, and what
minimum structure is needed before fermionic matter can enter the program.

The 3-layer fermionic obstruction (Q0 E1, Appendix M):
  Layer 1: pi_2(S^2) = Z gives INTEGER (bosonic) winding only.
           No half-integer winding in O(3) sigma model.
  Layer 2: No spinorial representation in O(3) target space.
           O(3) = SO(3) is doubly connected; its universal cover SU(2)
           carries spinors, but SU(2) is not natively available.
  Layer 3: No Hopf fibration S^3 -> S^2 natively installed.
           Hopf map provides the topological route to spinors/fermions
           but requires SU(2) or S^3 structure not present in O(3).

All three layers remain unchanged through the entire quantum program
(Q Parts I/II) and matter program (R-B through R-D).

Extension routes identified (none built):
  ER1: Hopf-term route -- postulate Hopf invariant as topological phase.
       Would require S^3 or SU(2) target space. MIP classification.
  ER2: Explicit spinor-sector -- postulate spinor fields alongside scalars.
       Direct but introduces fundamentally new DOF. MIP classification.
  ER3: Algebraic / Grassmann route -- postulate anticommuting variables.
       Formal but disconnected from GRUT architecture. CAH.
  ER4: O(3)+Skyrme+statistics -- add symmetrization postulate to bosonic
       objects. Would give bosonic statistics but NOT fermionic. BLOCKED
       for fermions (can only give BE, not FD, without spinorial structure).

Key finding: routes EXIST but ALL require new postulates (MIP minimum).
None is derivable from current GRUT+Q+R architecture.
Fermionic matter IS needed for later chemistry/life (exclusion principle,
shell structure, periodic table).
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_INHERITANCE_ITEMS: int = 5
N_REQUIREMENT_ITEMS: int = 6
N_EXTENSION_ROUTES: int = 4
N_QUANTUM_CHECKS: int = 5
N_ORGANIZATION_ITEMS: int = 4
N_BENCHMARK_CANDIDATES: int = 4
N_READINESS_DOMAINS: int = 6
N_PROBABILITY_TESTS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_RE_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
RD_INHERITED_FERMIONIC: str = "fermionic_boundary_unchanged"
RD_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_RE"
M_INHERITED_OBSTRUCTION: str = "fermionic_emergence_obstructed_3_layers"

# R-E Verdict strings
RE_OBSTRUCTION_VERDICT: str = "fermionic_obstruction_unchanged"
RE_ROUTE_VERDICT: str = "coherent_extension_routes_identified"
RE_MATTER_ROLE_VERDICT: str = "fermionic_matter_needed_for_later_matter_organization"
RE_READINESS_VERDICT: str = "fermionic_precondition_map_complete"
RE_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_RF"
RE_OVERALL_APPENDIX_P_CLASS: str = "bounded_structural_result"

ALLOWED_OBSTRUCTION_VERDICTS: frozenset = frozenset({
    "fermionic_obstruction_unchanged",
    "fermionic_obstruction_softened_but_not_removed",
    "fermionic_obstruction_extension_route_identified",
    "fermionic_obstruction_overturned",
})
ALLOWED_ROUTE_VERDICTS: frozenset = frozenset({
    "coherent_extension_routes_identified",
    "extension_routes_structurally_plausible_but_unbuilt",
    "extension_routes_underdetermined",
    "no_coherent_extension_route",
})
ALLOWED_MATTER_ROLE_VERDICTS: frozenset = frozenset({
    "fermionic_matter_needed_for_later_matter_organization",
    "fermionic_route_only_relevant_at_later_chemistry_stage",
    "fermionic_role_still_underdetermined",
    "fermionic_role_not_yet_assessable",
})
ALLOWED_READINESS_VERDICTS: frozenset = frozenset({
    "fermionic_matter_still_blocked",
    "fermionic_extension_readiness_only",
    "fermionic_precondition_map_complete",
    "fermionic_matter_partially_ready",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_RF",
    "authorized_only_for_further_fermionic_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_M_or_QIIF",
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

RE_NONCLAIMS: List[str] = [
    "NOT_claiming_bosonic_composite_therefore_fermions__"
    "bosonic_winding_and_composition_do_not_generate_fermionic_statistics",
    "NOT_claiming_many_mode_excitations_therefore_Fermi_statistics__"
    "qubit_sigma_plus_anticommutation_is_on_site_not_many_body_fermionic",
    "NOT_claiming_topological_charge_therefore_spin_half__"
    "integer_winding_pi2_S2_Z_is_bosonic_not_spinorial",
    "NOT_claiming_O3_extension_therefore_fermionic_matter_solved__"
    "O3_target_space_is_SO3_not_SU2_no_spinors",
    "NOT_claiming_entanglement_therefore_exclusion_principle__"
    "nonfactorized_states_are_correlation_not_antisymmetrization",
    "NOT_claiming_route_inventory_therefore_fermionic_closure__"
    "identifying_routes_is_not_building_them",
    "NOT_claiming_extension_level_fermionic_route_therefore_native_canon__"
    "all_fermionic_extension_routes_carry_MIP_floor",
    "NOT_claiming_fermionic_progress_therefore_chemistry_readiness__"
    "chemistry_requires_fermions_plus_binding_plus_probability",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class REInheritanceItem:
    item_id: str; item_name: str; original_status: str
    changed_by_later_work: bool; current_status: str; notes: List[str]

@dataclass
class REFermionicInheritanceAudit:
    items: List[REInheritanceItem]; n_items: int
    any_changed: bool; obstruction_verdict: str; notes: List[str]

@dataclass
class RERequirementItem:
    item_id: str; item_name: str; description: str
    status: str; notes: List[str]

@dataclass
class REFermionicRequirementAudit:
    items: List[RERequirementItem]; n_items: int
    n_absent: int; n_blocked: int; notes: List[str]

@dataclass
class REExtensionRoute:
    route_id: str; route_name: str; description: str
    viability: str; appendix_p_class: str
    minimum_new_structure: str; notes: List[str]

@dataclass
class REExtensionRouteAudit:
    routes: List[REExtensionRoute]; n_routes: int
    n_viable: int; strongest_route_id: str
    route_verdict: str; notes: List[str]

@dataclass
class REQuantumCheck:
    check_id: str; check_name: str; adds_fermionic: bool; notes: List[str]

@dataclass
class REQuantumToFermionAudit:
    checks: List[REQuantumCheck]; n_checks: int
    n_adds_fermionic: int; notes: List[str]

@dataclass
class REOrganizationItem:
    item_id: str; item_name: str; fermionic_needed: bool
    notes: List[str]

@dataclass
class REMatterOrganizationAudit:
    items: List[REOrganizationItem]; n_items: int
    n_needs_fermionic: int; matter_role_verdict: str; notes: List[str]

@dataclass
class REBenchmarkCandidate:
    candidate_id: str; candidate_name: str; description: str
    viable: bool; demonstrates: List[str]
    does_not_demonstrate: List[str]; notes: List[str]

@dataclass
class REBenchmarkAudit:
    candidates: List[REBenchmarkCandidate]; n_candidates: int
    n_viable: int; chosen_id: str; notes: List[str]

@dataclass
class REReadinessEntry:
    domain: str; readiness_level: str; notes: str

@dataclass
class REReadinessTable:
    entries: List[REReadinessEntry]; n_entries: int

@dataclass
class REProbabilityTest:
    test_id: str; test_name: str; result: str; notes: List[str]

@dataclass
class REProbabilityBoundaryAudit:
    tests: List[REProbabilityTest]; n_tests: int
    fermionic_route_independent_of_probability: bool; notes: List[str]

@dataclass
class REAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class REAppendixPAudit:
    entries: List[REAppendixPEntry]; n_entries: int
    overall_class: str; no_native_canon: bool; notes: List[str]

@dataclass
class REAuthorizationAudit:
    rf_authorized: bool; authorization_basis: List[str]
    re_constraints: List[str]; authorization_verdict: str; notes: List[str]

@dataclass
class RENonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class REFermionicMatterBoundaryResult:
    valid: bool
    track_a_inheritance: REFermionicInheritanceAudit
    track_b_requirements: REFermionicRequirementAudit
    track_c_routes: REExtensionRouteAudit
    track_d_quantum: REQuantumToFermionAudit
    track_e_organization: REMatterOrganizationAudit
    track_f_benchmark: REBenchmarkAudit
    track_g_readiness: REReadinessTable
    track_h_probability: REProbabilityBoundaryAudit
    track_i_appendix_p: REAppendixPAudit
    track_j_authorization: REAuthorizationAudit
    track_k_nonclaims: RENonclaimFirewall
    obstruction_verdict: str; route_verdict: str
    matter_role_verdict: str; readiness_verdict: str
    authorization_verdict: str
    re_appendix_p_class: str
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> REFermionicInheritanceAudit:
    items = [
        REInheritanceItem("FI1", "spin_half_obstruction",
            "obstructed_pi2_S2_Z_bosonic_only", False, "unchanged",
            ["Layer 1: pi_2(S^2)=Z gives integer winding only; no half-integer"]),
        REInheritanceItem("FI2", "fermionic_statistics_obstruction",
            "obstructed_no_antisymmetrization_available", False, "unchanged",
            ["No symmetrization/antisymmetrization postulate; no FD statistics"]),
        REInheritanceItem("FI3", "hopf_term_absence",
            "absent_no_hopf_invariant_installed", False, "unchanged",
            ["Hopf map S^3->S^2 not natively available; requires SU(2) or S^3"]),
        REInheritanceItem("FI4", "spinorial_structure_absence",
            "absent_no_spinor_fields_or_representations", False, "unchanged",
            ["O(3) = SO(3); spinors require SU(2) (universal cover); not available"]),
        REInheritanceItem("FI5", "quantum_program_fermionic_contribution",
            "zero_contribution_from_q_program", False, "unchanged",
            ["Q Parts I/II, R-B/C/D: all confirmed zero fermionic contribution"]),
    ]
    any_changed = any(i.changed_by_later_work for i in items)
    return REFermionicInheritanceAudit(
        items=items, n_items=N_INHERITANCE_ITEMS, any_changed=any_changed,
        obstruction_verdict=RE_OBSTRUCTION_VERDICT,
        notes=["ALL 5 inheritance items UNCHANGED",
               "3-layer obstruction fully intact: spin, statistics, topology",
               "Q program and R-B/C/D added zero fermionic content"],
    )


def _build_track_b() -> REFermionicRequirementAudit:
    items = [
        RERequirementItem("FR1", "spinorial_state_structure",
            "Spin-1/2 representations on the quantum state space.", "blocked",
            ["Requires SU(2) structure; O(3) provides SO(3) only",
             "Blocked by Layer 2 of obstruction"]),
        RERequirementItem("FR2", "fermi_dirac_statistics",
            "Antisymmetrization of multi-particle states.", "blocked",
            ["Requires particle identity + antisymmetrization postulate",
             "Blocked: no particle ontology, no symmetrization framework"]),
        RERequirementItem("FR3", "complementary_algebra_support",
            "Observable algebra supporting spinorial observables.", "absent",
            ["Q-II.D provides su(2) on C^2 (qubit), not spinorial su(2)",
             "Qubit su(2) is representation theory; spinorial is geometric"]),
        RERequirementItem("FR4", "stable_fermionic_object",
            "Stable localized fermionic configuration.", "blocked",
            ["Requires: spinorial structure + stabilization",
             "Both missing (FR1 blocked + R-C stability gap)"]),
        RERequirementItem("FR5", "exclusion_shell_structure",
            "Pauli-exclusion-based shell filling.", "blocked",
            ["Requires: fermions + statistics + binding",
             "All prerequisites absent or blocked"]),
        RERequirementItem("FR6", "probability_interpretation",
            "Detection probability for fermionic objects.", "absent",
            ["Born rule absent (Q-II.F); fermionic detection needs it",
             "Absent but independent of fermionic obstruction"]),
    ]
    n_abs = sum(1 for i in items if i.status == "absent")
    n_blk = sum(1 for i in items if i.status == "blocked")
    return REFermionicRequirementAudit(
        items=items, n_items=N_REQUIREMENT_ITEMS,
        n_absent=n_abs, n_blocked=n_blk,
        notes=[f"{n_blk} blocked (spin, statistics, stable object, exclusion)",
               f"{n_abs} absent (complementary algebra, probability)",
               "All 6 requirements are unmet; fermionic matter cannot proceed yet"],
    )


def _build_track_c() -> REExtensionRouteAudit:
    routes = [
        REExtensionRoute("ER1", "hopf_term_topological_phase",
            "Postulate Hopf invariant as topological phase term; "
            "maps S^3 -> S^2; introduces half-integer topological charge.",
            "motivated_but_unbuilt", "motivated_independent_postulation",
            "SU(2) or S^3 target space + Hopf term in action",
            ["Strongest topological route to fermions",
             "Would give pi_3(S^3)=Z topological charge (spinorial)",
             "Requires lifting O(3)=SO(3) to SU(2): new MIP postulate",
             "Route identified in condensed-matter Skyrme model literature"]),
        REExtensionRoute("ER2", "explicit_spinor_sector",
            "Postulate spinor fields psi alongside scalar Phi.",
            "motivated_but_unbuilt", "motivated_independent_postulation",
            "Spinor field psi + Dirac-like action + coupling to Phi",
            ["Direct route: introduces spin-1/2 as fundamental new DOF",
             "MIP: fundamentally new field content",
             "Most standard approach but least connected to GRUT architecture"]),
        REExtensionRoute("ER3", "grassmann_algebraic",
            "Postulate anticommuting (Grassmann) variables.",
            "compatible_but_ad_hoc", "compatible_but_ad_hoc",
            "Grassmann-valued fields + fermionic path integral",
            ["Formally possible but disconnected from GRUT architecture",
             "CAH: compatible but not motivated by any GRUT structure",
             "No convergent structural motivation identified"]),
        REExtensionRoute("ER4", "o3_skyrme_statistics_postulate",
            "Add symmetrization postulate to O(3)+Skyrme objects.",
            "blocked_for_fermions", "bounded_structural_result",
            "Symmetrization postulate (bosonic only without spinors)",
            ["Can give Bose-Einstein statistics for topological solitons",
             "CANNOT give Fermi-Dirac: integer winding = bosonic",
             "Blocked for fermionic purpose; useful for bosonic statistics only"]),
    ]
    n_viable = sum(1 for r in routes
                   if r.viability in ("motivated_but_unbuilt", "compatible_but_ad_hoc"))
    return REExtensionRouteAudit(
        routes=routes, n_routes=N_EXTENSION_ROUTES,
        n_viable=n_viable, strongest_route_id="ER1_hopf_term_topological_phase",
        route_verdict=RE_ROUTE_VERDICT,
        notes=["ER1 (Hopf) is strongest: topological, motivated, MIP",
               "ER2 (spinor) is direct but least GRUT-connected",
               "ER3 (Grassmann) is CAH: compatible but unmotivated",
               "ER4 blocked for fermions (bosonic statistics only)",
               "3 routes viable (ER1-ER3); none built"],
    )


def _build_track_d() -> REQuantumToFermionAudit:
    checks = [
        REQuantumCheck("QF1", "state_space_support", False,
            ["C^2 qubit: has su(2) algebra but as REPRESENTATION, not geometry"]),
        REQuantumCheck("QF2", "observable_grammar", False,
            ["su(2) observables: qubit algebra, not spinorial structure"]),
        REQuantumCheck("QF3", "many_mode_support", False,
            ["N-site chain: site excitations, not fermionic occupations"]),
        REQuantumCheck("QF4", "entanglement_structure", False,
            ["Nonfactorized states: correlation, not antisymmetrization"]),
        REQuantumCheck("QF5", "no_fermionic_support", False,
            ["Q program adds zero fermionic content; confirmed across all Q/R audits"]),
    ]
    n_f = sum(1 for c in checks if c.adds_fermionic)
    return REQuantumToFermionAudit(
        checks=checks, n_checks=N_QUANTUM_CHECKS,
        n_adds_fermionic=n_f,
        notes=["Q program adds 0 fermionic contributions",
               "Qubit su(2) is representation algebra, not spinorial geometry",
               "On-site anticommutation {sigma_+,sigma_-}=I is NOT FD statistics"],
    )


def _build_track_e() -> REMatterOrganizationAudit:
    items = [
        REOrganizationItem("MO1", "exclusion_principle_for_shell_filling",
            True, ["Pauli exclusion required for: electron shells, periodic table"]),
        REOrganizationItem("MO2", "fermionic_matter_for_stability",
            True, ["Fermionic degeneracy pressure: stabilizes white dwarfs, neutron stars"]),
        REOrganizationItem("MO3", "spin_statistics_for_chemistry",
            True, ["Spin-statistics theorem: fermions for matter, bosons for forces"]),
        REOrganizationItem("MO4", "antisymmetry_for_molecular_structure",
            True, ["Slater determinants, covalent bonding: require antisymmetrization"]),
    ]
    n_needs = sum(1 for i in items if i.fermionic_needed)
    return REMatterOrganizationAudit(
        items=items, n_items=N_ORGANIZATION_ITEMS,
        n_needs_fermionic=n_needs,
        matter_role_verdict=RE_MATTER_ROLE_VERDICT,
        notes=["ALL 4 matter-organization items require fermionic matter",
               "Without fermions: no shells, no periodic table, no chemistry",
               "Fermionic matter is ESSENTIAL for later matter organization"],
    )


def _build_track_f() -> REBenchmarkAudit:
    candidates = [
        REBenchmarkCandidate("FB1", "route_inventory_benchmark",
            "Document which extension routes exist and their requirements.",
            True,
            ["extension_route_catalog", "requirement_mapping",
             "obstruction_documentation"],
            ["fermionic_state", "fermionic_statistics", "spinorial_structure"],
            ["Minimal benchmark: inventory of what would be needed"]),
        REBenchmarkCandidate("FB2", "hopf_phase_extension_benchmark",
            "If Hopf term postulated: topological phase with half-integer charge.",
            True,
            ["extension_level_topological_phase", "half_integer_charge_structure"],
            ["native_derivation", "fermionic_statistics", "stable_fermion"],
            ["Extension-level: requires SU(2) MIP + Hopf term"]),
        REBenchmarkCandidate("FB3", "spinor_extension_benchmark",
            "If spinor field postulated: Dirac-like state on GRUT background.",
            True,
            ["extension_level_spinor_state", "spin_half_representation"],
            ["native_derivation", "statistics_from_grut", "stable_fermion"],
            ["Extension-level: requires new spinor DOF"]),
        REBenchmarkCandidate("FB4", "no_benchmark",
            "No admissible benchmark.", False, [], [],
            ["Rejected: FB1-FB3 are viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return REBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_id="FB1_route_inventory_benchmark",
        notes=["FB1 chosen: route inventory (strongest current benchmark)",
               "FB2/FB3 conditional on extension postulations (not yet adopted)",
               "All benchmarks are ROUTE documentation, not fermionic physics"],
    )


def _build_track_g() -> REReadinessTable:
    entries = [
        REReadinessEntry("spinorial_matter", "blocked",
            "Layer 2 obstruction: no spinors in O(3); requires SU(2) MIP"),
        REReadinessEntry("fermionic_statistics", "blocked",
            "No antisymmetrization; no particle identity; no FD framework"),
        REReadinessEntry("stable_fermionic_object", "blocked",
            "Requires spinors + stabilization; both absent"),
        REReadinessEntry("exclusion_shell_structure", "blocked",
            "Requires fermions + statistics + binding; all absent"),
        REReadinessEntry("chemistry_relevant_fermionic", "blocked",
            "Requires all prior items; furthest from current state"),
        REReadinessEntry("extension_route_clarity", "extension_ready",
            "Routes ER1-ER3 identified with requirements; route map complete"),
    ]
    return REReadinessTable(entries=entries, n_entries=N_READINESS_DOMAINS)


def _build_track_h() -> REProbabilityBoundaryAudit:
    tests = [
        REProbabilityTest("PB1", "route_identification_structural",
            "independent", ["Route inventory is structural, not probabilistic"]),
        REProbabilityTest("PB2", "spinorial_structure_structural",
            "independent", ["Spinor geometry is algebraic/topological"]),
        REProbabilityTest("PB3", "fermionic_detection_needs_born",
            "conditional", ["'Probability of detecting a fermion' needs Born rule"]),
        REProbabilityTest("PB4", "exclusion_interpretation_needs_born",
            "conditional", ["'Probability of shell occupation' needs Born rule"]),
    ]
    return REProbabilityBoundaryAudit(
        tests=tests, n_tests=N_PROBABILITY_TESTS,
        fermionic_route_independent_of_probability=True,
        notes=["Route identification: structural, independent of probability",
               "Interpretive fermionic claims: conditional on Born postulate"],
    )


def _build_track_i() -> REAppendixPAudit:
    entries = [
        REAppendixPEntry("RE_obstruction", "3-layer obstruction unchanged",
            "bounded_structural_result",
            "All 3 layers intact; no softening by Q or R work",
            "Obstruction softened or overturned",
            "Appendix M; Q0 E1; confirmed through R-D"),
        REAppendixPEntry("RE_routes", "Extension routes identified",
            "motivated_but_unbuilt",
            "ER1 (Hopf), ER2 (spinor), ER3 (Grassmann) identified as routes",
            "Routes imply fermionic matter available",
            "Literature: Skyrme model, Hopf fibration, Dirac theory"),
        REAppendixPEntry("RE_hopf_strongest", "Hopf route strongest",
            "motivated_independent_postulation",
            "ER1 Hopf-term route: strongest, most GRUT-connected, MIP",
            "Hopf route is native or already built",
            "Requires SU(2) target space + Hopf invariant"),
        REAppendixPEntry("RE_quantum_zero", "Q adds zero fermionic",
            "bounded_structural_result",
            "Quantum program contributes zero fermionic content",
            "Quantum excitation grammar provides fermionic structure",
            "Q-II.E, R-B through R-D confirmations"),
        REAppendixPEntry("RE_matter_role", "Fermions needed for organization",
            "bounded_structural_result",
            "Fermionic matter essential for: shells, exclusion, chemistry",
            "Bosonic matter sufficient for chemistry",
            "Standard physics: spin-statistics, Pauli exclusion"),
        REAppendixPEntry("RE_precondition_map", "Precondition map complete",
            "bounded_structural_result",
            "Requirements, routes, and obstructions fully documented",
            "Precondition map implies fermionic readiness",
            "All R-E tracks"),
        REAppendixPEntry("RE_overall", "R-E overall",
            "bounded_structural_result",
            "Fermionic boundary documented; routes identified; obstruction preserved",
            "Fermionic matter established or route built",
            "All R-E tracks"),
    ]
    return REAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RE_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["4 BSR (obstruction, Q contribution, matter role, overall), "
               "1 MBU (routes), 1 MIP (Hopf strongest), 1 BSR (precondition map)"],
    )


def _build_track_j() -> REAuthorizationAudit:
    return REAuthorizationAudit(
        rf_authorized=True,
        authorization_basis=[
            "fermionic_obstruction_fully_documented",
            "extension_routes_identified_and_classified",
            "fermionic_role_in_matter_organization_established",
            "precondition_map_complete",
            "probability_boundary_preserved",
        ],
        re_constraints=[
            "RF_must_address_statistics_framework_bosonic_and_fermionic",
            "RF_must_address_probability_interpretation_for_matter",
            "RF_must_not_assume_fermionic_matter_available",
            "RF_results_inherit_BSR_or_MBU_floor",
            "RF_must_preserve_fermionic_obstruction_unless_new_route_built",
        ],
        authorization_verdict=RE_AUTHORIZATION_VERDICT,
        notes=["R-F authorized: fermionic boundary documented, "
               "statistics and probability investigation next"],
    )


def _build_track_k() -> RENonclaimFirewall:
    return RENonclaimFirewall(
        nonclaims=RE_NONCLAIMS, n_nonclaims=N_RE_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_re_fermionic_matter_boundary_audit() -> REFermionicMatterBoundaryResult:
    ta = _build_track_a(); tb = _build_track_b(); tc = _build_track_c()
    td = _build_track_d(); te = _build_track_e(); tf = _build_track_f()
    tg = _build_track_g(); th = _build_track_h(); ti = _build_track_i()
    tj = _build_track_j(); tk = _build_track_k()

    allowed_claims: List[str] = [
        "Fermionic 3-layer obstruction unchanged through entire Q and R program: "
        "spin, statistics, and Hopf/spinor layers all intact",
        "3 coherent extension routes identified: ER1 (Hopf MIP), ER2 (spinor MIP), "
        "ER3 (Grassmann CAH); ER4 blocked for fermions (bosonic only)",
        "ER1 (Hopf-term topological phase) is the strongest route: "
        "most connected to GRUT topology, requires SU(2) MIP",
        "Quantum program adds zero fermionic content: confirmed across "
        "all Q Parts I/II and R-B through R-D audits",
        "Fermionic matter essential for later matter organization: "
        "exclusion principle, shell structure, periodic table, chemistry",
        "Fermionic precondition map complete: requirements, routes, "
        "and obstructions fully documented",
        "R-F authorized: statistics and probability investigation next",
    ]
    forbidden_claims: List[str] = [
        "Bosonic composite structure implies fermions",
        "Many-mode excitations imply Fermi statistics",
        "Topological charge implies spin-1/2",
        "O(3) extension implies fermionic matter solved",
        "Entanglement implies exclusion principle",
        "Route inventory implies fermionic closure",
        "Extension-level fermionic route implies native canon",
    ]
    diagnostics: Dict[str, Any] = {
        "n_inheritance_items": N_INHERITANCE_ITEMS,
        "any_inheritance_changed": ta.any_changed,
        "n_requirements": N_REQUIREMENT_ITEMS,
        "n_requirements_blocked": tb.n_blocked,
        "n_requirements_absent": tb.n_absent,
        "n_extension_routes": N_EXTENSION_ROUTES,
        "n_viable_routes": tc.n_viable,
        "quantum_adds_fermionic": td.n_adds_fermionic,
        "n_organization_needs_fermionic": te.n_needs_fermionic,
        "n_benchmark_viable": tf.n_viable,
        "fermionic_route_independent_of_probability": th.fermionic_route_independent_of_probability,
        "n_nonclaims": N_RE_NONCLAIMS,
    }

    result = REFermionicMatterBoundaryResult(
        valid=True,
        track_a_inheritance=ta, track_b_requirements=tb,
        track_c_routes=tc, track_d_quantum=td,
        track_e_organization=te, track_f_benchmark=tf,
        track_g_readiness=tg, track_h_probability=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        obstruction_verdict=ta.obstruction_verdict,
        route_verdict=tc.route_verdict,
        matter_role_verdict=te.matter_role_verdict,
        readiness_verdict=RE_READINESS_VERDICT,
        authorization_verdict=tj.authorization_verdict,
        re_appendix_p_class=RE_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RE_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_re_result(result)
    return result


def validate_re_result(result: REFermionicMatterBoundaryResult) -> None:
    checks = [
        (result.obstruction_verdict, ALLOWED_OBSTRUCTION_VERDICTS, "Obstruction"),
        (result.route_verdict, ALLOWED_ROUTE_VERDICTS, "Route"),
        (result.matter_role_verdict, ALLOWED_MATTER_ROLE_VERDICTS, "Matter role"),
        (result.readiness_verdict, ALLOWED_READINESS_VERDICTS, "Readiness"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.re_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class invalid")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}' class invalid")
    if result.track_k_nonclaims.n_nonclaims != N_RE_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.rf_authorized:
        raise ValueError("rf_authorized must be True")
    if result.track_a_inheritance.any_changed:
        raise ValueError("inheritance any_changed must be False")
    if result.track_d_quantum.n_adds_fermionic != 0:
        raise ValueError("quantum adds_fermionic must be 0")
    for e in result.track_g_readiness.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"Readiness '{e.domain}': invalid level")


def _self_test() -> bool:
    r = run_re_fermionic_matter_boundary_audit()
    assert r.valid is True
    assert r.obstruction_verdict == RE_OBSTRUCTION_VERDICT
    assert r.route_verdict == RE_ROUTE_VERDICT
    assert r.matter_role_verdict == RE_MATTER_ROLE_VERDICT
    assert r.readiness_verdict == RE_READINESS_VERDICT
    assert r.authorization_verdict == RE_AUTHORIZATION_VERDICT
    assert r.diagnostics["any_inheritance_changed"] is False
    assert r.diagnostics["quantum_adds_fermionic"] == 0
    assert r.diagnostics["n_organization_needs_fermionic"] == 4
    return True


if __name__ == "__main__":
    _self_test()
    print("R-E self-test passed.")
