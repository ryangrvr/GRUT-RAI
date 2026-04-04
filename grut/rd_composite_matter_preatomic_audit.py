"""
Appendix R-D --- Composite Matter and Pre-Atomic Structure Audit
================================================================
GRUT Matter Program --- Phase R-D

Audits whether anything beyond single-object-candidate language is justified,
what composite or pre-atomic structure is supportable, and what remains
blocked by missing stabilization and probability structure.

Key finding: composite GRAMMAR is extension-ready; composite MATTER is not.
  - Composition rule (tensor product MIP) enables multi-object description
  - Entanglement/correlation grammar from Q-II.C/D enables relational language
  - But: no stable objects (R-C), no binding mechanism, no discrete spectrum
  - Pre-atomic grammar is available as formal language, not physical structure
  - True composite matter requires: stable objects + binding + statistics
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

N_ELIGIBILITY_CRITERIA: int = 6
N_BOSONIC_ROUTE_LEVELS: int = 5
N_BINDING_CANDIDATES: int = 5
N_PREATOMIC_LEVELS: int = 5
N_BENCHMARK_CANDIDATES: int = 4
N_QUANTUM_CONTRIBUTIONS: int = 5
N_FERMIONIC_CHECKS: int = 4
N_READINESS_DOMAINS: int = 7
N_PROBABILITY_TESTS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_RD_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
RC_INHERITED_STABILITY: str = "no_native_stabilizer_found"
RC_INHERITED_BOUND: str = "bosonic_bound_structure_not_yet_established"
RC_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_RD"

# R-D Verdict strings
RD_COMPOSITE_VERDICT: str = "bosonic_composite_configurations_extension_ready"
RD_BINDING_VERDICT: str = "no_true_binding_criterion_found"
RD_PREATOMIC_VERDICT: str = "pre_atomic_grammar_only"
RD_FERMIONIC_BOUNDARY_VERDICT: str = "fermionic_boundary_unchanged"
RD_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_RE"
RD_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

ALLOWED_COMPOSITE_VERDICTS: frozenset = frozenset({
    "bosonic_composite_configurations_extension_ready",
    "bosonic_composite_structure_structurally_plausible_but_unbuilt",
    "bosonic_composite_structure_not_yet_established",
    "composite_route_blocked",
})
ALLOWED_BINDING_VERDICTS: frozenset = frozenset({
    "no_true_binding_criterion_found",
    "binding_criterion_structurally_plausible_but_unbuilt",
    "extension_level_binding_candidate_identified",
    "binding_route_blocked",
})
ALLOWED_PREATOMIC_VERDICTS: frozenset = frozenset({
    "pre_atomic_grammar_only",
    "pre_atomic_benchmark_candidate_extension_ready",
    "pre_atomic_structure_not_yet_established",
    "pre_atomic_route_blocked",
})
ALLOWED_FERMIONIC_VERDICTS: frozenset = frozenset({
    "fermionic_composite_route_still_blocked",
    "fermionic_boundary_unchanged",
    "fermionic_extension_route_identified",
    "fermionic_boundary_requires_reopening",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_RE",
    "authorized_only_for_further_composite_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_RC_or_QIIG",
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

RD_NONCLAIMS: List[str] = [
    "NOT_claiming_coexistence_therefore_binding__"
    "two_configurations_side_by_side_is_not_bound_structure",
    "NOT_claiming_entanglement_therefore_composite_matter__"
    "nonfactorized_quantum_state_is_not_material_binding",
    "NOT_claiming_topological_pairing_therefore_stable_composite__"
    "winding_charge_association_is_not_stable_bound_object",
    "NOT_claiming_metastable_pair_therefore_pre_atomic_closure__"
    "metastability_is_delayed_decay_not_atomic_structure",
    "NOT_claiming_bosonic_composite_grammar_therefore_chemistry_readiness__"
    "composite_grammar_is_language_not_chemistry",
    "NOT_claiming_many_mode_coupling_therefore_particle_ontology__"
    "H_hop_coupling_is_excitation_transfer_not_particle_interaction",
    "NOT_claiming_extension_level_composite_therefore_native_canon__"
    "all_RD_results_carry_MBU_or_BSR_floor",
    "NOT_claiming_composite_matter_progress_therefore_fermionic_route_softened__"
    "fermionic_3_layer_obstruction_unchanged",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RDEligibilityCriterion:
    criterion_id: str; criterion_name: str; description: str
    status: str; notes: List[str]

@dataclass
class RDCompositeEligibilityAudit:
    criteria: List[RDEligibilityCriterion]; n_criteria: int
    n_satisfied: int; n_partial: int; n_not_satisfied: int; notes: List[str]

@dataclass
class RDBosonicRouteLevel:
    level_id: str; level_name: str; description: str
    achieved: bool; notes: List[str]

@dataclass
class RDBosonicCompositeRouteAudit:
    levels: List[RDBosonicRouteLevel]; n_levels: int
    highest_achieved_id: str; composite_verdict: str; notes: List[str]

@dataclass
class RDBindingCandidate:
    candidate_id: str; candidate_name: str; description: str
    provides_binding: bool; binding_type: str; notes: List[str]

@dataclass
class RDBindingCriterionAudit:
    candidates: List[RDBindingCandidate]; n_candidates: int
    n_provides: int; binding_verdict: str; notes: List[str]

@dataclass
class RDPreAtomicLevel:
    level_id: str; level_name: str; description: str
    achieved: bool; notes: List[str]

@dataclass
class RDPreAtomicAudit:
    levels: List[RDPreAtomicLevel]; n_levels: int
    highest_achieved_id: str; pre_atomic_verdict: str; notes: List[str]

@dataclass
class RDBenchmarkCandidate:
    candidate_id: str; candidate_name: str; description: str
    viable: bool; demonstrates: List[str]; does_not_demonstrate: List[str]
    notes: List[str]

@dataclass
class RDBenchmarkAudit:
    candidates: List[RDBenchmarkCandidate]; n_candidates: int
    n_viable: int; chosen_id: str; notes: List[str]

@dataclass
class RDQuantumContribution:
    contribution_id: str; contribution_name: str
    adds_composite_matter: bool; adds_grammar_only: bool; notes: List[str]

@dataclass
class RDQuantumContributionAudit:
    contributions: List[RDQuantumContribution]; n_contributions: int
    n_adds_matter: int; notes: List[str]

@dataclass
class RDFermionicCheck:
    check_id: str; check_name: str; result: str; notes: List[str]

@dataclass
class RDFermionicBoundaryAudit:
    checks: List[RDFermionicCheck]; n_checks: int
    fermionic_boundary_verdict: str; obstruction_unchanged: bool; notes: List[str]

@dataclass
class RDReadinessEntry:
    domain: str; readiness_level: str; notes: str

@dataclass
class RDReadinessTable:
    entries: List[RDReadinessEntry]; n_entries: int

@dataclass
class RDProbabilityTest:
    test_id: str; test_name: str; result: str; notes: List[str]

@dataclass
class RDProbabilityBoundaryAudit:
    tests: List[RDProbabilityTest]; n_tests: int
    composite_independent_of_probability: bool; notes: List[str]

@dataclass
class RDAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class RDAppendixPAudit:
    entries: List[RDAppendixPEntry]; n_entries: int
    overall_class: str; no_native_canon: bool; notes: List[str]

@dataclass
class RDAuthorizationAudit:
    re_authorized: bool; authorization_basis: List[str]
    rd_constraints: List[str]; authorization_verdict: str; notes: List[str]

@dataclass
class RDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class RDCompositeMatterPreAtomicResult:
    valid: bool
    track_a_eligibility: RDCompositeEligibilityAudit
    track_b_bosonic_route: RDBosonicCompositeRouteAudit
    track_c_binding: RDBindingCriterionAudit
    track_d_preatomic: RDPreAtomicAudit
    track_e_benchmark: RDBenchmarkAudit
    track_f_quantum: RDQuantumContributionAudit
    track_g_fermionic: RDFermionicBoundaryAudit
    track_h_readiness: RDReadinessTable
    track_i_probability: RDProbabilityBoundaryAudit
    track_j_appendix_p: RDAppendixPAudit
    track_k_authorization: RDAuthorizationAudit
    track_l_nonclaims: RDNonclaimFirewall
    composite_verdict: str; binding_verdict: str
    pre_atomic_verdict: str; fermionic_boundary_verdict: str
    authorization_verdict: str
    rd_appendix_p_class: str
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> RDCompositeEligibilityAudit:
    criteria = [
        RDEligibilityCriterion("CE1", "distinguishable_constituents",
            "Two or more distinguishable localized structures.", "partially",
            ["Site labels (Q-II.B/E); shell localization (M); topological defects (O)",
             "Partial: localization available but not stable objects"]),
        RDEligibilityCriterion("CE2", "coherent_composition_rule",
            "Rule for describing joint state of multiple constituents.", "extension_ready",
            ["Tensor product (Q-II.B MIP): H_AB = H_A tensor H_B",
             "Extension-ready: composition grammar available"]),
        RDEligibilityCriterion("CE3", "persistent_relational_structure",
            "Constituents maintain relation over time.", "precondition_only",
            ["Requires stable objects (R-C: not established)",
             "Metastable: relational structure persists temporarily"]),
        RDEligibilityCriterion("CE4", "joint_observable_structure",
            "Observables on composite system (A tensor B, correlators).", "extension_ready",
            ["Q-II.D: multi-observable grammar on C^4 available"]),
        RDEligibilityCriterion("CE5", "binding_or_association_criterion",
            "Mechanism that holds constituents together.", "not_satisfied",
            ["R-C: no binding mechanism found",
             "H_hop: excitation transfer, not binding"]),
        RDEligibilityCriterion("CE6", "probability_boundary_compatibility",
            "Compatible with diagnostic-weights-only constraint.", "extension_ready",
            ["Composite grammar is structural, not probabilistic",
             "Interpretive claims would need Born postulate"]),
    ]
    n_s = sum(1 for c in criteria if c.status == "satisfied")
    n_p = sum(1 for c in criteria if c.status in ("partially", "precondition_only"))
    n_n = sum(1 for c in criteria if c.status == "not_satisfied")
    return RDCompositeEligibilityAudit(
        criteria=criteria, n_criteria=N_ELIGIBILITY_CRITERIA,
        n_satisfied=n_s, n_partial=n_p, n_not_satisfied=n_n,
        notes=["0 satisfied, 2 partial/precondition, 1 not satisfied (binding), "
               "3 extension-ready",
               "Key blocker: binding criterion (CE5) absent"],
    )


def _build_track_b() -> RDBosonicCompositeRouteAudit:
    levels = [
        RDBosonicRouteLevel("BR1", "multiple_excitations",
            "Multiple site excitations on qubit chain.", True,
            ["sigma_+^(i) for multiple sites i: multiple excitations",
             "N_tot = sum n_i: total excitation count"]),
        RDBosonicRouteLevel("BR2", "correlated_configurations",
            "Correlated or entangled multi-excitation states.", True,
            ["Nonfactorized states on composite C^4 (Q-II.C)",
             "Correlation grammar from Q-II.D"]),
        RDBosonicRouteLevel("BR3", "metastable_composite",
            "Metastable multi-object configuration.", True,
            ["If two metastable configurations coexist: composite persists "
             "on timescale >> tau before decay",
             "Metastability from R-C dissipation analysis"]),
        RDBosonicRouteLevel("BR4", "extension_composite_candidate",
            "Extension-level composite with topological + quantum overlay.", True,
            ["O(3) defect pair + tensor product state + correlators",
             "Extension-level: requires O(3) MIP + Skyrme MBU + Q extensions"]),
        RDBosonicRouteLevel("BR5", "true_composite_matter",
            "Stable, bound composite matter.", False,
            ["Not achieved: requires stable objects (R-C gap) + binding",
             "Neither stability nor binding established"]),
    ]
    achieved = [l for l in levels if l.achieved]
    highest = achieved[-1].level_id + "_" + achieved[-1].level_name if achieved else "none"
    return RDBosonicCompositeRouteAudit(
        levels=levels, n_levels=N_BOSONIC_ROUTE_LEVELS,
        highest_achieved_id=highest,
        composite_verdict=RD_COMPOSITE_VERDICT,
        notes=["BR1-BR4 achieved; BR5 (true composite matter) not achieved",
               "Highest: extension-level composite candidate (BR4)",
               "Verdict: bosonic_composite_configurations_extension_ready"],
    )


def _build_track_c() -> RDBindingCriterionAudit:
    candidates = [
        RDBindingCandidate("BC1", "topological_association",
            "Two topological defects near each other.", False, "association_not_binding",
            ["Topological charges can coexist but nothing binds them",
             "No attractive force between defects in current package"]),
        RDBindingCandidate("BC2", "shell_shared_support",
            "Two configurations sharing a shell/boundary region.", False, "proximity_not_binding",
            ["Shared support region is geometric proximity",
             "No energy advantage to sharing vs. separation"]),
        RDBindingCandidate("BC3", "dissipative_co_localization",
            "Dissipation co-localizes excitations temporarily.", False, "transient_not_binding",
            ["Dissipation can slow separation but not prevent it",
             "Co-localization is metastable, not bound"]),
        RDBindingCandidate("BC4", "composite_quantum_correlation",
            "Entangled state correlates subsystems.", False, "correlation_not_binding",
            ["Entanglement (Q-II.C) provides correlation in state space",
             "Correlation is informational, not energetic binding"]),
        RDBindingCandidate("BC5", "no_binding",
            "No true binding criterion found.", True, "confirmed_absence",
            ["All 4 candidates fail: association, proximity, co-localization, "
             "and correlation are NOT binding",
             "Binding requires: attractive interaction + energy minimum"]),
    ]
    n_prov = sum(1 for c in candidates if c.provides_binding and c.candidate_id != "BC5")
    return RDBindingCriterionAudit(
        candidates=candidates, n_candidates=N_BINDING_CANDIDATES,
        n_provides=n_prov, binding_verdict=RD_BINDING_VERDICT,
        notes=["All 4 binding candidates fail",
               "BC5 confirmed: no true binding criterion found",
               "Binding requires attractive interaction (not in current package)"],
    )


def _build_track_d() -> RDPreAtomicAudit:
    levels = [
        RDPreAtomicLevel("PA1", "no_pre_atomic_structure",
            "No pre-atomic language justified.", False,
            ["Rejected: some pre-atomic grammar IS available (formal language)"]),
        RDPreAtomicLevel("PA2", "pre_atomic_grammar_only",
            "Formal language for describing composite configurations.", True,
            ["Tensor product + correlators + multi-observable: the grammar exists",
             "Can DESCRIBE composite configurations formally",
             "But: no stable objects, no binding, no discrete spectrum"]),
        RDPreAtomicLevel("PA3", "pre_atomic_benchmark_configuration",
            "Specific benchmark configuration with pre-atomic character.", False,
            ["Not achieved: benchmark (Track E) shows coexistence/correlation",
             "But cannot demonstrate binding or stability"]),
        RDPreAtomicLevel("PA4", "extension_level_pre_atomic",
            "Extension-level pre-atomic candidate.", False,
            ["Would require: O(3) + Skyrme + binding interaction",
             "All extension-level; not yet assembled"]),
        RDPreAtomicLevel("PA5", "atomic_analogy",
            "Full atom-like composite structure.", False,
            ["Blocked: requires stable particles + binding + statistics + probability",
             "Far beyond current package"]),
    ]
    achieved = [l for l in levels if l.achieved]
    highest = achieved[-1].level_id + "_" + achieved[-1].level_name if achieved else "none"
    return RDPreAtomicAudit(
        levels=levels, n_levels=N_PREATOMIC_LEVELS,
        highest_achieved_id=highest,
        pre_atomic_verdict=RD_PREATOMIC_VERDICT,
        notes=["PA2 achieved: formal pre-atomic grammar available",
               "PA3-PA5 not achieved: no benchmark, no extension candidate, no atom analog",
               "Verdict: pre_atomic_grammar_only"],
    )


def _build_track_e() -> RDBenchmarkAudit:
    candidates = [
        RDBenchmarkCandidate("CM1", "two_excitation_coexistence",
            "Two site excitations on qubit chain: sigma_+^(1) sigma_+^(2) |00>.",
            True,
            ["multi_excitation_coexistence", "independent_decoherence_per_site",
             "composite_state_on_C4"],
            ["binding", "stability", "pre_atomic_character", "particle_pair"],
            ["Demonstrates coexistence of excitations, nothing more"]),
        RDBenchmarkCandidate("CM2", "entangled_pair_configuration",
            "Entangled two-excitation state (|10> + |01>)/sqrt(2).",
            True,
            ["entangled_excitation_pair", "quantum_correlation",
             "nonfactorized_state", "reduced_state_mixedness"],
            ["binding", "stability", "spatial_proximity", "material_composite"],
            ["Demonstrates correlation, not binding"]),
        RDBenchmarkCandidate("CM3", "extension_topological_pair",
            "Two O(3) topological defects with quantum state overlay.",
            True,
            ["topological_charge_pair", "extension_level_composite",
             "formal_relational_structure"],
            ["binding_between_defects", "stability_of_pair",
             "energy_advantage_of_proximity"],
            ["Extension-level: O(3) MIP + quantum extension",
             "Strongest benchmark but no binding"]),
        RDBenchmarkCandidate("CM4", "no_benchmark",
            "No admissible composite benchmark.", False, [], [],
            ["Rejected: CM1-CM3 are viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return RDBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_id="CM2_entangled_pair_configuration",
        notes=["CM2 chosen: entangled excitation pair (best correlation benchmark)",
               "CM3 stronger (topological) but requires more extensions",
               "All benchmarks demonstrate coexistence/correlation, NOT binding"],
    )


def _build_track_f() -> RDQuantumContributionAudit:
    contributions = [
        RDQuantumContribution("QC1", "composition_grammar", False, True,
            ["Tensor product: formal composition, not material binding"]),
        RDQuantumContribution("QC2", "entanglement_correlation", False, True,
            ["Nonfactorized states: correlation, not binding"]),
        RDQuantumContribution("QC3", "multi_observable_support", False, True,
            ["Correlators <A tensor B>: relational language, not matter"]),
        RDQuantumContribution("QC4", "many_mode_bookkeeping", False, True,
            ["N-site chain: multi-excitation description, not composite matter"]),
        RDQuantumContribution("QC5", "no_binding_from_quantum", False, False,
            ["Q program adds grammar, not binding or stability"]),
    ]
    n_m = sum(1 for c in contributions if c.adds_composite_matter)
    return RDQuantumContributionAudit(
        contributions=contributions, n_contributions=N_QUANTUM_CONTRIBUTIONS,
        n_adds_matter=n_m,
        notes=["Q adds 0 composite-matter contributions, 4 grammar contributions",
               "Consistent with R-B/R-C: Q adds readiness/grammar, not matter"],
    )


def _build_track_g() -> RDFermionicBoundaryAudit:
    checks = [
        RDFermionicCheck("FB1", "obstruction_from_q0",
            "unchanged", ["Q0 3-layer fermionic obstruction: pi_2(S^2)=Z bosonic only"]),
        RDFermionicCheck("FB2", "q_program_contribution",
            "zero", ["Q Parts I/II added zero fermionic content"]),
        RDFermionicCheck("FB3", "composite_matter_contribution",
            "zero", ["Bosonic composite grammar does not create fermionic routes"]),
        RDFermionicCheck("FB4", "statistics_dependent_matter",
            "blocked", ["BE/FD statistics absent; statistics-dependent composites blocked"]),
    ]
    return RDFermionicBoundaryAudit(
        checks=checks, n_checks=N_FERMIONIC_CHECKS,
        fermionic_boundary_verdict=RD_FERMIONIC_BOUNDARY_VERDICT,
        obstruction_unchanged=True,
        notes=["Fermionic boundary completely unchanged",
               "Bosonic composite work does not affect fermionic obstruction"],
    )


def _build_track_h() -> RDReadinessTable:
    entries = [
        RDReadinessEntry("composite_bosonic_configurations", "extension_ready",
            "Multi-excitation, correlated, metastable configurations"),
        RDReadinessEntry("relational_structure", "extension_ready",
            "Correlators and entanglement grammar on composites"),
        RDReadinessEntry("binding_criterion", "precondition_only",
            "No binding mechanism; only association/proximity/correlation"),
        RDReadinessEntry("pre_atomic_grammar", "extension_ready",
            "Formal language available; no physical pre-atomic structure"),
        RDReadinessEntry("pre_atomic_benchmark", "precondition_only",
            "Benchmarks show coexistence/correlation, not pre-atomic character"),
        RDReadinessEntry("true_composite_matter", "precondition_only",
            "Requires stable objects + binding + statistics"),
        RDReadinessEntry("fermionic_composite", "blocked",
            "3-layer obstruction unchanged"),
    ]
    return RDReadinessTable(entries=entries, n_entries=N_READINESS_DOMAINS)


def _build_track_i() -> RDProbabilityBoundaryAudit:
    tests = [
        RDProbabilityTest("PB1", "composite_grammar_structural",
            "independent", ["Composition grammar is algebraic, not probabilistic"]),
        RDProbabilityTest("PB2", "binding_structural",
            "independent", ["Binding (if found) would be energetic, not probabilistic"]),
        RDProbabilityTest("PB3", "benchmark_structural",
            "independent", ["Benchmarks describe states, not measurement outcomes"]),
        RDProbabilityTest("PB4", "interpretive_claims_conditional",
            "conditional", ["'What is the probability of finding this composite?' "
                            "requires Born rule"]),
    ]
    return RDProbabilityBoundaryAudit(
        tests=tests, n_tests=N_PROBABILITY_TESTS,
        composite_independent_of_probability=True,
        notes=["Structural composite claims independent of probability",
               "Interpretive claims would need Born postulate"],
    )


def _build_track_j() -> RDAppendixPAudit:
    entries = [
        RDAppendixPEntry("RD_composite_grammar", "Composite configuration grammar",
            "motivated_but_unbuilt",
            "Bosonic composite configurations extension-ready",
            "Composite grammar implies composite matter",
            "Q-II.B tensor product, Q-II.C entanglement"),
        RDAppendixPEntry("RD_binding_absence", "No binding criterion",
            "bounded_structural_result",
            "All binding candidates fail; no attractive interaction",
            "Association or correlation implies binding",
            "R-C stability gap, no interaction potential"),
        RDAppendixPEntry("RD_preatomic_grammar", "Pre-atomic grammar",
            "motivated_but_unbuilt",
            "Formal pre-atomic grammar available",
            "Pre-atomic grammar implies atomic structure",
            "Tensor product + correlators + multi-observable"),
        RDAppendixPEntry("RD_benchmark", "Composite benchmarks",
            "motivated_but_unbuilt",
            "Benchmarks demonstrate coexistence and correlation",
            "Benchmarks demonstrate binding or pre-atomic character",
            "Q-II.C/D entanglement and observable grammar"),
        RDAppendixPEntry("RD_fermionic_unchanged", "Fermionic boundary unchanged",
            "bounded_structural_result",
            "Fermionic obstruction completely unchanged by composite work",
            "Composite matter softens fermionic obstruction",
            "Q0 3-layer obstruction"),
        RDAppendixPEntry("RD_quantum_grammar_only", "Q adds grammar only",
            "bounded_structural_result",
            "Quantum program adds composition/correlation grammar, not matter",
            "Quantum composite grammar establishes material composites",
            "Q-II.B through Q-II.D"),
        RDAppendixPEntry("RD_overall", "R-D overall",
            "motivated_but_unbuilt",
            "Composite grammar extension-ready; binding absent; pre-atomic grammar only",
            "Composite matter or pre-atomic structure established",
            "All R-D tracks"),
    ]
    return RDAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RD_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["3 MBU (grammar/benchmarks), 3 BSR (absences), 1 MBU (overall)"],
    )


def _build_track_k() -> RDAuthorizationAudit:
    return RDAuthorizationAudit(
        re_authorized=True,
        authorization_basis=[
            "composite_grammar_extension_ready",
            "binding_absence_documented",
            "pre_atomic_grammar_available",
            "fermionic_boundary_assessed_unchanged",
            "probability_boundary_preserved",
        ],
        rd_constraints=[
            "RE_must_investigate_fermionic_obstruction_directly",
            "RE_must_not_assume_bosonic_results_dissolve_fermionic_block",
            "RE_must_assess_extension_routes_for_fermionic_matter",
            "RE_results_inherit_BSR_or_MBU_floor",
            "RE_must_preserve_probability_boundary",
        ],
        authorization_verdict=RD_AUTHORIZATION_VERDICT,
        notes=["R-E authorized: composite matter investigation complete, "
               "fermionic boundary is the next target"],
    )


def _build_track_l() -> RDNonclaimFirewall:
    return RDNonclaimFirewall(
        nonclaims=RD_NONCLAIMS, n_nonclaims=N_RD_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_rd_composite_matter_preatomic_audit() -> RDCompositeMatterPreAtomicResult:
    ta = _build_track_a(); tb = _build_track_b(); tc = _build_track_c()
    td = _build_track_d(); te = _build_track_e(); tf = _build_track_f()
    tg = _build_track_g(); th = _build_track_h(); ti = _build_track_i()
    tj = _build_track_j(); tk = _build_track_k(); tl = _build_track_l()

    allowed_claims: List[str] = [
        "Bosonic composite configurations extension-ready: multiple excitations, "
        "correlated states, metastable composites, and extension-level candidates",
        "No true binding criterion found: topological association, shell proximity, "
        "dissipative co-localization, and quantum correlation all fail as binding",
        "Pre-atomic grammar available as formal language for describing "
        "composite configurations (tensor product + correlators + multi-observable)",
        "Composite benchmarks demonstrate coexistence and correlation only, "
        "not binding or pre-atomic physical character",
        "Quantum program adds composition/correlation grammar, not composite "
        "matter or binding; consistent with R-B/R-C findings",
        "Fermionic boundary completely unchanged by composite matter work",
        "R-E authorized: composite matter investigation complete, fermionic "
        "boundary investigation next",
    ]
    forbidden_claims: List[str] = [
        "Coexistence implies binding",
        "Entanglement implies composite matter",
        "Topological pairing implies stable composite",
        "Metastable pair implies pre-atomic closure",
        "Bosonic composite grammar implies chemistry readiness",
        "Many-mode coupling implies particle ontology",
        "Extension-level composite implies native canon",
    ]
    diagnostics: Dict[str, Any] = {
        "n_eligibility_criteria": N_ELIGIBILITY_CRITERIA,
        "n_criteria_satisfied": ta.n_satisfied,
        "n_criteria_not_satisfied": ta.n_not_satisfied,
        "n_bosonic_route_achieved": sum(1 for l in tb.levels if l.achieved),
        "n_binding_provides": tc.n_provides,
        "n_preatomic_achieved": sum(1 for l in td.levels if l.achieved),
        "n_benchmark_viable": te.n_viable,
        "quantum_adds_matter": tf.n_adds_matter,
        "fermionic_obstruction_unchanged": tg.obstruction_unchanged,
        "composite_independent_of_probability": ti.composite_independent_of_probability,
        "n_nonclaims": N_RD_NONCLAIMS,
    }

    result = RDCompositeMatterPreAtomicResult(
        valid=True,
        track_a_eligibility=ta, track_b_bosonic_route=tb,
        track_c_binding=tc, track_d_preatomic=td,
        track_e_benchmark=te, track_f_quantum=tf,
        track_g_fermionic=tg, track_h_readiness=th,
        track_i_probability=ti, track_j_appendix_p=tj,
        track_k_authorization=tk, track_l_nonclaims=tl,
        composite_verdict=tb.composite_verdict,
        binding_verdict=tc.binding_verdict,
        pre_atomic_verdict=td.pre_atomic_verdict,
        fermionic_boundary_verdict=tg.fermionic_boundary_verdict,
        authorization_verdict=tk.authorization_verdict,
        rd_appendix_p_class=RD_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RD_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_rd_result(result)
    return result


def validate_rd_result(result: RDCompositeMatterPreAtomicResult) -> None:
    checks = [
        (result.composite_verdict, ALLOWED_COMPOSITE_VERDICTS, "Composite"),
        (result.binding_verdict, ALLOWED_BINDING_VERDICTS, "Binding"),
        (result.pre_atomic_verdict, ALLOWED_PREATOMIC_VERDICTS, "Pre-atomic"),
        (result.fermionic_boundary_verdict, ALLOWED_FERMIONIC_VERDICTS, "Fermionic"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.rd_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class invalid")
    for e in result.track_j_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}' class invalid")
    if result.track_l_nonclaims.n_nonclaims != N_RD_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_l_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_j_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_k_authorization.re_authorized:
        raise ValueError("re_authorized must be True")
    if not result.track_g_fermionic.obstruction_unchanged:
        raise ValueError("obstruction_unchanged must be True")
    if result.track_c_binding.n_provides != 0:
        raise ValueError("n_provides binding must be 0")
    if result.track_f_quantum.n_adds_matter != 0:
        raise ValueError("quantum n_adds_matter must be 0")
    for e in result.track_h_readiness.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"Readiness '{e.domain}': level invalid")


def _self_test() -> bool:
    r = run_rd_composite_matter_preatomic_audit()
    assert r.valid is True
    assert r.composite_verdict == RD_COMPOSITE_VERDICT
    assert r.binding_verdict == RD_BINDING_VERDICT
    assert r.pre_atomic_verdict == RD_PREATOMIC_VERDICT
    assert r.fermionic_boundary_verdict == RD_FERMIONIC_BOUNDARY_VERDICT
    assert r.authorization_verdict == RD_AUTHORIZATION_VERDICT
    assert r.diagnostics["n_binding_provides"] == 0
    assert r.diagnostics["quantum_adds_matter"] == 0
    assert r.diagnostics["fermionic_obstruction_unchanged"] is True
    return True


if __name__ == "__main__":
    _self_test()
    print("R-D self-test passed.")
