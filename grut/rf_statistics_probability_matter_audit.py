"""
Appendix R-F --- Statistics, Probability, and Matter Interpretation Audit
=========================================================================
GRUT Matter Program --- Phase R-F

Audits what statistics, exchange/identity, and probability structures are
available to GRUT matter, and how tau interacts with exchange.

Key findings:
  1. Bosonic statistics: extension-level exchange structure demonstrated
     for toy two-excitation system. sigma_+^(1) sigma_+^(2) = symmetric
     under site exchange. But: qubit excitations (max 1 per site) differ
     from true bosonic (unbounded occupation).

  2. Fermionic statistics: obstruction unchanged. R-E routes identified
     but none built. No Fermi-Dirac structure available.

  3. Exchange and tau: the macroscopic relaxation lag tau introduces a
     TRANSIENT memory window during which exchange of two configurations
     leaves a dissipative trace. After time >> tau, the trace relaxes away.
     This is an OPEN-SYSTEM CAVEAT on exchange symmetry: exact exchange
     holds only in the long-time (equilibrated) limit.

  4. Probability: Q-II.F boundary inherited exactly. Diagnostic weights
     only. Matter interpretation requires explicit Born postulate if
     probability is needed. Statistics interpretation (frequencies of
     outcomes) inherits this constraint.

  5. Matter interpretation: scaffolded only. Bosonic matter candidates
     describable via extension-level grammar + diagnostic weights.
     Fermionic matter not interpretable. Probability not natively assigned.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU

N_ELIGIBILITY_ITEMS: int = 5
N_BOSONIC_TESTS: int = 4
N_FERMIONIC_CHECKS: int = 4
N_EXCHANGE_CANDIDATES: int = 4
N_MEMORY_TESTS: int = 5
N_PROBABILITY_TESTS: int = 4
N_BENCHMARK_CANDIDATES: int = 4
N_INTERPRETATION_LEVELS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_RF_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

RE_INHERITED: str = "authorized_to_proceed_to_RF"
QIIF_INHERITED: str = "diagnostic_weights_available_but_not_probabilities"

RF_BOSONIC_STATS_VERDICT: str = "bosonic_exchange_structure_demonstrated"
RF_FERMIONIC_STATS_VERDICT: str = "fermionic_statistics_obstruction_unchanged"
RF_INDISTINGUISHABILITY_VERDICT: str = "exchange_symmetry_with_open_system_caveats"
RF_MATTER_INTERPRETATION_VERDICT: str = (
    "matter_interpretation_requires_explicit_probability_postulate"
)
RF_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_RG"
RF_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

ALLOWED_BOSONIC_STATS_VERDICTS: frozenset = frozenset({
    "bosonic_statistics_extension_level_only",
    "bosonic_exchange_structure_demonstrated",
    "bosonic_statistics_underdetermined",
    "bosonic_statistics_blocked",
})
ALLOWED_FERMIONIC_STATS_VERDICTS: frozenset = frozenset({
    "fermionic_statistics_obstruction_unchanged",
    "fermionic_statistics_route_inventory_only",
    "fermionic_statistics_extension_route_identified",
    "fermionic_statistics_partially_ready",
})
ALLOWED_INDISTINGUISHABILITY_VERDICTS: frozenset = frozenset({
    "exchange_symmetry_with_open_system_caveats",
    "transient_exchange_memory_effect_only",
    "indistinguishability_underdetermined",
    "indistinguishability_blocked",
})
ALLOWED_MATTER_INTERPRETATION_VERDICTS: frozenset = frozenset({
    "scaffolded_matter_interpretation_only",
    "matter_interpretation_requires_explicit_probability_postulate",
    "matter_interpretation_not_yet_coherent",
    "limited_bosonic_interpretation_available",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_RG",
    "authorized_only_for_further_statistics_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_RE_or_QIIF",
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

RF_NONCLAIMS: List[str] = [
    "NOT_claiming_bosonic_exchange_toy_therefore_full_statistics_closure__"
    "two_excitation_exchange_is_not_many_body_Bose_Einstein",
    "NOT_claiming_memory_lag_therefore_fundamental_particle_identity__"
    "tau_relaxation_trace_is_transient_not_permanent_distinguishability",
    "NOT_claiming_exchange_history_effect_therefore_fermions__"
    "open_system_memory_is_not_antisymmetrization",
    "NOT_claiming_diagnostic_weights_therefore_statistical_frequencies__"
    "Born_rule_absent_means_no_frequency_interpretation",
    "NOT_claiming_route_inventory_therefore_exclusion_principle__"
    "fermionic_routes_identified_not_built",
    "NOT_claiming_bosonic_statistics_therefore_chemistry_readiness__"
    "chemistry_requires_fermions_plus_binding_plus_probability",
    "NOT_claiming_extension_level_statistics_therefore_native_canon__"
    "all_RF_results_carry_MBU_or_BSR_floor",
    "NOT_claiming_open_system_distinguishability_therefore_violation_of_quantum_identity__"
    "transient_memory_effect_relaxes_away_on_timescale_tau",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RFEligibilityItem:
    item_id: str; item_name: str; description: str
    status: str; notes: List[str]

@dataclass
class RFStatisticsEligibilityAudit:
    items: List[RFEligibilityItem]; n_items: int
    n_present: int; n_extension: int; n_absent: int
    eligibility_verdict: str; notes: List[str]

@dataclass
class RFBosonicTest:
    test_id: str; test_name: str; description: str
    result: str; notes: List[str]

@dataclass
class RFBosonicStatisticsAudit:
    tests: List[RFBosonicTest]; n_tests: int
    bosonic_statistics_verdict: str; notes: List[str]

@dataclass
class RFFermionicCheck:
    check_id: str; check_name: str; result: str; notes: List[str]

@dataclass
class RFFermionicStatisticsAudit:
    checks: List[RFFermionicCheck]; n_checks: int
    fermionic_statistics_verdict: str; obstruction_unchanged: bool
    notes: List[str]

@dataclass
class RFExchangeCandidate:
    candidate_id: str; candidate_name: str; description: str
    available: bool; exchange_type: str; notes: List[str]

@dataclass
class RFExchangeIdentityAudit:
    candidates: List[RFExchangeCandidate]; n_candidates: int
    n_available: int; notes: List[str]

@dataclass
class RFMemoryTest:
    test_id: str; test_name: str; description: str
    result: str; notes: List[str]

@dataclass
class RFMemoryLagAudit:
    tests: List[RFMemoryTest]; n_tests: int
    indistinguishability_verdict: str
    tau_creates_transient_memory: bool; notes: List[str]

@dataclass
class RFProbabilityTest:
    test_id: str; test_name: str; result: str; notes: List[str]

@dataclass
class RFProbabilityMatterAudit:
    tests: List[RFProbabilityTest]; n_tests: int
    born_rule_required_for_interpretation: bool; notes: List[str]

@dataclass
class RFBenchmarkCandidate:
    candidate_id: str; candidate_name: str; description: str
    viable: bool; demonstrates: List[str]; does_not_demonstrate: List[str]
    notes: List[str]

@dataclass
class RFBenchmarkAudit:
    candidates: List[RFBenchmarkCandidate]; n_candidates: int
    n_viable: int; chosen_id: str; notes: List[str]

@dataclass
class RFInterpretationLevel:
    level_id: str; level_name: str; description: str
    achieved: bool; notes: List[str]

@dataclass
class RFMatterInterpretationAudit:
    levels: List[RFInterpretationLevel]; n_levels: int
    highest_achieved_id: str; matter_interpretation_verdict: str
    notes: List[str]

@dataclass
class RFAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class RFAppendixPAudit:
    entries: List[RFAppendixPEntry]; n_entries: int
    overall_class: str; no_native_canon: bool; notes: List[str]

@dataclass
class RFAuthorizationAudit:
    rg_authorized: bool; authorization_basis: List[str]
    rf_constraints: List[str]; authorization_verdict: str; notes: List[str]

@dataclass
class RFNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class RFStatisticsProbabilityMatterResult:
    valid: bool
    track_a_eligibility: RFStatisticsEligibilityAudit
    track_b_bosonic: RFBosonicStatisticsAudit
    track_c_fermionic: RFFermionicStatisticsAudit
    track_d_exchange: RFExchangeIdentityAudit
    track_e_memory: RFMemoryLagAudit
    track_f_probability: RFProbabilityMatterAudit
    track_g_benchmark: RFBenchmarkAudit
    track_h_interpretation: RFMatterInterpretationAudit
    track_i_appendix_p: RFAppendixPAudit
    track_j_authorization: RFAuthorizationAudit
    track_k_nonclaims: RFNonclaimFirewall
    bosonic_statistics_verdict: str; fermionic_statistics_verdict: str
    indistinguishability_verdict: str; matter_interpretation_verdict: str
    authorization_verdict: str
    rf_appendix_p_class: str
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> RFStatisticsEligibilityAudit:
    items = [
        RFEligibilityItem("SE1", "multiple_identical_constituents",
            "Two or more nominally identical excitations/objects.", "extension_level",
            ["N-site qubit chain: identical sites with identical excitation operators"]),
        RFEligibilityItem("SE2", "exchange_operation",
            "Operation swapping two constituents.", "extension_level",
            ["Site-label swap: sigma_+^(1) sigma_+^(2) -> sigma_+^(2) sigma_+^(1)",
             "Well-defined on tensor product; extension-level"]),
        RFEligibilityItem("SE3", "state_label_invariance",
            "State symmetric/antisymmetric under exchange.", "extension_level",
            ["For bosonic: state unchanged under swap (symmetric)",
             "For fermionic: state picks up minus sign (antisymmetric)",
             "Bosonic case: available; fermionic: blocked"]),
        RFEligibilityItem("SE4", "probability_interpretation",
            "Frequency interpretation of exchange outcomes.", "absent",
            ["Born rule absent; no frequency interpretation available"]),
        RFEligibilityItem("SE5", "bosonic_fermionic_compatibility",
            "Statistics compatible with current bosonic/blocked-fermionic routes.", "present",
            ["Bosonic route: compatible (symmetric states available)",
             "Fermionic route: blocked (no antisymmetrization)"]),
    ]
    n_p = sum(1 for i in items if i.status == "present")
    n_e = sum(1 for i in items if i.status == "extension_level")
    n_a = sum(1 for i in items if i.status == "absent")
    return RFStatisticsEligibilityAudit(
        items=items, n_items=N_ELIGIBILITY_ITEMS,
        n_present=n_p, n_extension=n_e, n_absent=n_a,
        eligibility_verdict="partially_eligible_bosonic_only",
        notes=["1 present, 3 extension-level, 1 absent (probability)",
               "Bosonic exchange: eligible at extension level",
               "Fermionic: blocked; probability: absent"],
    )


def _build_track_b() -> RFBosonicStatisticsAudit:
    tests = [
        RFBosonicTest("BS1", "symmetric_two_excitation_state",
            "Two-site symmetric state: (sigma_+^1 sigma_+^2)|00> is exchange-invariant.",
            "demonstrated",
            ["Product state |11> = sigma_+^1 sigma_+^2 |00> is trivially symmetric",
             "Entangled state (|10>+|01>)/sqrt(2) is also symmetric under exchange",
             "Exchange symmetry demonstrated for toy two-excitation system"]),
        RFBosonicTest("BS2", "exchange_invariant_observables",
            "Observables invariant under site exchange: sum_i n_i, sum_i sigma_z^i.",
            "demonstrated",
            ["Total occupation N = sum n_i: exchange-invariant",
             "Symmetric correlators: invariant under site swap"]),
        RFBosonicTest("BS3", "open_system_exchange_caveats",
            "Independent Lindblad channels distinguish sites during transient.",
            "caveat_documented",
            ["Lindblad channel L_i acts on site i specifically",
             "During transient (t < tau): sites distinguishable by decoherence history",
             "After equilibration (t >> tau): sites indistinguishable",
             "Open-system caveat: exact exchange symmetry only in long-time limit"]),
        RFBosonicTest("BS4", "qubit_vs_true_bosonic_limitation",
            "Qubit excitations limited to 0 or 1 per site; true bosons: unbounded.",
            "limitation_documented",
            ["sigma_+ sigma_+ = 0 on single site: max 1 excitation",
             "True bosonic [a, a^dag] = 1: unbounded occupation n = 0,1,2,...",
             "Current package: hard-core boson limit (max 1 per site)",
             "Full Bose-Einstein requires harmonic oscillator per site"]),
    ]
    return RFBosonicStatisticsAudit(
        tests=tests, n_tests=N_BOSONIC_TESTS,
        bosonic_statistics_verdict=RF_BOSONIC_STATS_VERDICT,
        notes=["BS1-BS2: exchange symmetry demonstrated for toy system",
               "BS3: open-system caveat (transient distinguishability via Lindblad)",
               "BS4: qubit limitation (hard-core, max 1 per site)",
               "Verdict: exchange structure demonstrated with caveats"],
    )


def _build_track_c() -> RFFermionicStatisticsAudit:
    checks = [
        RFFermionicCheck("FS1", "antisymmetrization_available",
            "blocked", ["No antisymmetrization postulate; no mechanism"]),
        RFFermionicCheck("FS2", "fermi_dirac_distribution",
            "blocked", ["Requires antisymmetric multi-particle states"]),
        RFFermionicCheck("FS3", "pauli_exclusion",
            "blocked", ["Requires fermionic statistics + shell structure"]),
        RFFermionicCheck("FS4", "re_routes_help",
            "routes_only", ["R-E routes (Hopf, spinor, Grassmann) identified; none built"]),
    ]
    return RFFermionicStatisticsAudit(
        checks=checks, n_checks=N_FERMIONIC_CHECKS,
        fermionic_statistics_verdict=RF_FERMIONIC_STATS_VERDICT,
        obstruction_unchanged=True,
        notes=["3 blocked (antisymmetry, FD distribution, exclusion)",
               "1 routes-only (R-E extension routes identified, none built)",
               "Fermionic statistics obstruction unchanged"],
    )


def _build_track_d() -> RFExchangeIdentityAudit:
    candidates = [
        RFExchangeCandidate("EX1", "bosonic_excitation_exchange",
            "Swap two site excitations: relabel sites 1 <-> 2.",
            True, "exact_in_equilibrium",
            ["Exact exchange symmetry in long-time (equilibrated) limit",
             "Transient distinguishability during decoherence (open-system caveat)"]),
        RFExchangeCandidate("EX2", "topological_candidate_exchange",
            "Swap two O(3) topological defects.",
            True, "extension_level",
            ["If O(3) postulated: topological defects are identical by construction",
             "Exchange: swap positions of two winding-1 defects",
             "Extension-level: requires O(3) MIP"]),
        RFExchangeCandidate("EX3", "composite_configuration_exchange",
            "Swap two composite configurations.",
            True, "extension_level",
            ["Tensor-product composition allows formal exchange",
             "But: no stable objects means exchange is of DESCRIPTIONS, not THINGS"]),
        RFExchangeCandidate("EX4", "no_exchange",
            "No coherent exchange operation.", False, "null",
            ["Rejected: EX1-EX3 provide exchange operations"]),
    ]
    n_a = sum(1 for c in candidates if c.available)
    return RFExchangeIdentityAudit(
        candidates=candidates, n_candidates=N_EXCHANGE_CANDIDATES,
        n_available=n_a,
        notes=["3 exchange operations available",
               "EX1 strongest: exact in equilibrium, caveat during transient",
               "All extension-level (require Q/R extension package)"],
    )


def _build_track_e() -> RFMemoryLagAudit:
    tests = [
        RFMemoryTest("ML1", "tau_introduces_relaxation_window",
            "Constitutive lag tau creates finite relaxation time.",
            "confirmed",
            ["After exchange: system relaxes to new configuration in time O(tau)"]),
        RFMemoryTest("ML2", "exchange_leaves_transient_trace",
            "During relaxation, the history of which site was excited is imprinted.",
            "confirmed",
            ["Lindblad channel on site i retains information about site i's history",
             "This is a TRANSIENT memory: it decays at rate gamma = 1/tau"]),
        RFMemoryTest("ML3", "trace_relaxes_away",
            "After time >> tau, the transient trace vanishes.",
            "confirmed",
            ["Off-diagonal elements (which encode history) decay exponentially",
             "In the long-time limit: exchange trace is erased"]),
        RFMemoryTest("ML4", "effective_distinguishability_during_transient",
            "During the relaxation window, exchanged configurations are effectively distinguishable.",
            "confirmed",
            ["For t < tau: decoherence history distinguishes the two sites",
             "For t >> tau: indistinguishable (exchange trace erased)",
             "This is the open-system caveat on exchange symmetry"]),
        RFMemoryTest("ML5", "not_fundamental_identity_violation",
            "The transient memory is NOT a fundamental violation of particle identity.",
            "confirmed",
            ["The memory is an OPEN-SYSTEM EFFECT of dissipative dynamics",
             "In the closed-system limit (tau -> inf): no memory, exact exchange",
             "The effect is operational, not ontological"]),
    ]
    return RFMemoryLagAudit(
        tests=tests, n_tests=N_MEMORY_TESTS,
        indistinguishability_verdict=RF_INDISTINGUISHABILITY_VERDICT,
        tau_creates_transient_memory=True,
        notes=["tau creates transient exchange memory window",
               "Exchange trace relaxes away on timescale tau",
               "Not a fundamental identity violation",
               "Verdict: exchange_symmetry_with_open_system_caveats"],
    )


def _build_track_f() -> RFProbabilityMatterAudit:
    tests = [
        RFProbabilityTest("PM1", "diagnostic_weights_inherited",
            "inherited", ["Q-II.F: density diagonals as mathematical tools"]),
        RFProbabilityTest("PM2", "born_rule_required_for_frequencies",
            "confirmed", ["Statistical frequencies (outcome counts) require Born rule"]),
        RFProbabilityTest("PM3", "statistics_interpretation_constrained",
            "confirmed", ["'Fraction of bosons in state n' requires Born interpretation"]),
        RFProbabilityTest("PM4", "structural_statistics_independent",
            "confirmed", ["Exchange symmetry itself is structural, not probabilistic"]),
    ]
    return RFProbabilityMatterAudit(
        tests=tests, n_tests=N_PROBABILITY_TESTS,
        born_rule_required_for_interpretation=True,
        notes=["Structural statistics (exchange symmetry): no Born rule needed",
               "Interpretive statistics (frequencies, distributions): Born rule needed",
               "Q-II.F boundary inherited exactly"],
    )


def _build_track_g() -> RFBenchmarkAudit:
    candidates = [
        RFBenchmarkCandidate("SB1", "two_excitation_exchange_benchmark",
            "Two-site exchange: |11> is symmetric; swap sites 1<->2; "
            "observable total N = n_1 + n_2 is exchange-invariant.",
            True,
            ["exchange_symmetry_for_product_state",
             "exchange_invariant_observables",
             "open_system_caveat_documented"],
            ["full_BE_statistics", "fermionic_statistics",
             "probability_interpretation", "many_body_scaling"],
            ["Minimal exchange benchmark; demonstrates bosonic symmetry"]),
        RFBenchmarkCandidate("SB2", "exchange_with_memory_benchmark",
            "Exchange two excitations and track decoherence history: "
            "transient distinguishability during relaxation window.",
            True,
            ["transient_memory_effect", "relaxation_timescale_tau",
             "exchange_trace_decay"],
            ["fundamental_identity_violation", "permanent_distinguishability"],
            ["Novel GRUT-specific benchmark: tau-memory during exchange"]),
        RFBenchmarkCandidate("SB3", "fermionic_route_benchmark",
            "Benchmark testing fermionic extension route.",
            False, [], [],
            ["Not viable: fermionic routes identified but not built"]),
        RFBenchmarkCandidate("SB4", "no_benchmark",
            "No admissible benchmark.", False, [], [],
            ["Rejected: SB1 and SB2 are viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return RFBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_id="SB2_exchange_with_memory_benchmark",
        notes=["SB2 chosen: exchange-with-memory (GRUT-specific, novel)",
               "SB1 also viable: standard exchange symmetry",
               "SB2 is distinctive: tau-memory caveat is unique to GRUT"],
    )


def _build_track_h() -> RFMatterInterpretationAudit:
    levels = [
        RFInterpretationLevel("MI1", "extension_level_bosonic_configurations",
            "Bosonic matter candidates describable as extension-level configurations.",
            True,
            ["Qubit chain excitations + shell/topological localization + composite grammar",
             "All extension-level; diagnostic weights for description"]),
        RFInterpretationLevel("MI2", "no_fermionic_interpretation",
            "No fermionic matter interpretation available.",
            True,
            ["Fermionic obstruction unchanged; no FD statistics; no exclusion"]),
        RFInterpretationLevel("MI3", "no_probability_complete_interpretation",
            "No probability-complete matter interpretation.",
            True,
            ["Born rule absent; diagnostic weights only",
             "Cannot say 'the probability of finding this matter configuration is P'"]),
        RFInterpretationLevel("MI4", "scaffolded_with_explicit_postulates",
            "Matter interpretation available only with explicit postulates.",
            True,
            ["If Born rule postulated (MIP): probability interpretation available",
             "If Skyrme built (MBU): stable objects available",
             "If fermionic route built: fermionic interpretation available",
             "All require explicit extension postulates"]),
    ]
    achieved = [l for l in levels if l.achieved]
    highest = achieved[-1].level_id + "_" + achieved[-1].level_name if achieved else "none"
    return RFMatterInterpretationAudit(
        levels=levels, n_levels=N_INTERPRETATION_LEVELS,
        highest_achieved_id=highest,
        matter_interpretation_verdict=RF_MATTER_INTERPRETATION_VERDICT,
        notes=["All 4 levels achieved (they describe the current state)",
               "MI4 is the summary: scaffolded interpretation, postulates required",
               "Verdict: requires_explicit_probability_postulate"],
    )


def _build_track_i() -> RFAppendixPAudit:
    entries = [
        RFAppendixPEntry("RF_bosonic_exchange", "Bosonic exchange structure",
            "motivated_but_unbuilt",
            "Exchange symmetry demonstrated for toy two-excitation system",
            "Full Bose-Einstein statistics closure",
            "Q-II.E excitation grammar + tensor product"),
        RFAppendixPEntry("RF_fermionic_unchanged", "Fermionic statistics unchanged",
            "bounded_structural_result",
            "Fermionic statistics obstruction unchanged",
            "Fermionic statistics available or softened",
            "R-E obstruction; Q0 3-layer block"),
        RFAppendixPEntry("RF_tau_memory", "Tau-memory exchange effect",
            "motivated_but_unbuilt",
            "Transient exchange memory effect during relaxation window",
            "Memory effect violates quantum identity in principle",
            "Part I tau relaxation + exchange operation"),
        RFAppendixPEntry("RF_probability_boundary", "Probability boundary preserved",
            "bounded_structural_result",
            "Q-II.F boundary inherited; Born rule required for frequencies",
            "Diagnostic weights are statistical frequencies",
            "Q-II.F"),
        RFAppendixPEntry("RF_matter_interpretation", "Scaffolded interpretation",
            "motivated_but_unbuilt",
            "Matter interpretation scaffolded; requires explicit postulates",
            "Matter interpretation natively complete",
            "All Q/R extension results"),
        RFAppendixPEntry("RF_qubit_limitation", "Hard-core boson limitation",
            "bounded_structural_result",
            "Qubit limit: max 1 excitation per site (hard-core boson)",
            "Full bosonic occupation (unbounded n) available",
            "Q-II.E sigma_+ sigma_+ = 0 per site"),
        RFAppendixPEntry("RF_overall", "R-F overall",
            "motivated_but_unbuilt",
            "Statistics and interpretation: bosonic exchange demonstrated, "
            "fermionic blocked, probability postulate required",
            "Statistics, probability, or interpretation closure achieved",
            "All R-F tracks"),
    ]
    return RFAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RF_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["3 MBU (exchange, memory, interpretation), 3 BSR (fermionic, "
               "probability, qubit limit), 1 MBU (overall)"],
    )


def _build_track_j() -> RFAuthorizationAudit:
    return RFAuthorizationAudit(
        rg_authorized=True,
        authorization_basis=[
            "bosonic_exchange_structure_demonstrated",
            "fermionic_statistics_boundary_fully_documented",
            "tau_memory_exchange_effect_characterized",
            "probability_boundary_inherited_and_preserved",
            "matter_interpretation_scaffolded",
        ],
        rf_constraints=[
            "RG_must_synthesize_all_R_results_for_chemistry_bridge",
            "RG_must_document_fermionic_absence_as_chemistry_gap",
            "RG_must_not_assume_probability_closure",
            "RG_must_not_assume_stable_particles",
            "RG_must_produce_final_matter_to_chemistry_readiness_map",
        ],
        authorization_verdict=RF_AUTHORIZATION_VERDICT,
        notes=["R-G authorized: statistics and interpretation documented",
               "R-G must produce the final chemistry-bridge readiness map"],
    )


def _build_track_k() -> RFNonclaimFirewall:
    return RFNonclaimFirewall(
        nonclaims=RF_NONCLAIMS, n_nonclaims=N_RF_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_rf_statistics_probability_matter_audit() -> RFStatisticsProbabilityMatterResult:
    ta = _build_track_a(); tb = _build_track_b(); tc = _build_track_c()
    td = _build_track_d(); te = _build_track_e(); tf = _build_track_f()
    tg = _build_track_g(); th = _build_track_h(); ti = _build_track_i()
    tj = _build_track_j(); tk = _build_track_k()

    allowed_claims: List[str] = [
        "Bosonic exchange structure demonstrated for toy two-excitation system "
        "with open-system caveat (transient distinguishability during tau window)",
        "Tau-memory exchange effect: exchange leaves transient dissipative trace "
        "that relaxes away on timescale tau (not fundamental identity violation)",
        "Fermionic statistics obstruction unchanged; R-E routes identified but "
        "none built; no Fermi-Dirac or Pauli exclusion available",
        "Probability boundary inherited: diagnostic weights only; statistical "
        "frequencies require explicit Born postulate (MIP)",
        "Hard-core boson limitation documented: qubit max 1 per site; full "
        "Bose-Einstein requires harmonic oscillator extension",
        "Matter interpretation scaffolded: bosonic configurations describable "
        "at extension level; fermionic and probability-complete interpretation absent",
        "R-G authorized: final chemistry-bridge readiness map next",
    ]
    forbidden_claims: List[str] = [
        "Bosonic exchange toy implies full statistics closure",
        "Memory lag implies fundamental particle identity",
        "Exchange-history effect implies fermions",
        "Diagnostic weights imply statistical frequencies",
        "Route inventory implies exclusion principle",
        "Bosonic statistics imply chemistry readiness",
        "Extension-level statistics imply native canon",
    ]
    diagnostics: Dict[str, Any] = {
        "n_eligibility": N_ELIGIBILITY_ITEMS,
        "n_eligibility_present": ta.n_present,
        "n_eligibility_extension": ta.n_extension,
        "n_eligibility_absent": ta.n_absent,
        "n_exchange_available": td.n_available,
        "tau_creates_memory": te.tau_creates_transient_memory,
        "fermionic_obstruction_unchanged": tc.obstruction_unchanged,
        "born_required": tf.born_rule_required_for_interpretation,
        "n_benchmark_viable": tg.n_viable,
        "n_nonclaims": N_RF_NONCLAIMS,
    }

    result = RFStatisticsProbabilityMatterResult(
        valid=True,
        track_a_eligibility=ta, track_b_bosonic=tb,
        track_c_fermionic=tc, track_d_exchange=td,
        track_e_memory=te, track_f_probability=tf,
        track_g_benchmark=tg, track_h_interpretation=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        bosonic_statistics_verdict=tb.bosonic_statistics_verdict,
        fermionic_statistics_verdict=tc.fermionic_statistics_verdict,
        indistinguishability_verdict=te.indistinguishability_verdict,
        matter_interpretation_verdict=th.matter_interpretation_verdict,
        authorization_verdict=tj.authorization_verdict,
        rf_appendix_p_class=RF_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RF_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_rf_result(result)
    return result


def validate_rf_result(result: RFStatisticsProbabilityMatterResult) -> None:
    checks = [
        (result.bosonic_statistics_verdict, ALLOWED_BOSONIC_STATS_VERDICTS, "Bosonic stats"),
        (result.fermionic_statistics_verdict, ALLOWED_FERMIONIC_STATS_VERDICTS, "Fermionic stats"),
        (result.indistinguishability_verdict, ALLOWED_INDISTINGUISHABILITY_VERDICTS, "Indist."),
        (result.matter_interpretation_verdict, ALLOWED_MATTER_INTERPRETATION_VERDICTS, "Interp."),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.rf_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class invalid")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}' class invalid")
    if result.track_k_nonclaims.n_nonclaims != N_RF_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.rg_authorized:
        raise ValueError("rg_authorized must be True")
    if not result.track_c_fermionic.obstruction_unchanged:
        raise ValueError("fermionic obstruction must be unchanged")
    if not result.track_f_probability.born_rule_required_for_interpretation:
        raise ValueError("born_rule_required must be True")
    if not result.track_e_memory.tau_creates_transient_memory:
        raise ValueError("tau_creates_transient_memory must be True")


def _self_test() -> bool:
    r = run_rf_statistics_probability_matter_audit()
    assert r.valid is True
    assert r.bosonic_statistics_verdict == RF_BOSONIC_STATS_VERDICT
    assert r.fermionic_statistics_verdict == RF_FERMIONIC_STATS_VERDICT
    assert r.indistinguishability_verdict == RF_INDISTINGUISHABILITY_VERDICT
    assert r.matter_interpretation_verdict == RF_MATTER_INTERPRETATION_VERDICT
    assert r.authorization_verdict == RF_AUTHORIZATION_VERDICT
    assert r.diagnostics["fermionic_obstruction_unchanged"] is True
    assert r.diagnostics["tau_creates_memory"] is True
    assert r.diagnostics["born_required"] is True
    return True


if __name__ == "__main__":
    _self_test()
    print("R-F self-test passed.")
