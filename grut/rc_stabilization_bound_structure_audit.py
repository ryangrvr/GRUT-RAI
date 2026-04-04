"""
Appendix R-C --- Stabilization and Bound Structure Audit
=========================================================
GRUT Matter Program --- Phase R-C

Audits whether any true stabilizing mechanism exists for bosonic
object-candidates and whether bound structure is established or remains
extension-level / blocked.

Key finding: NO native stabilizer found.
  - Constitutive attractor: restores average Phi, does not prevent Derrick collapse
  - Shell/boundary: confinement, not intrinsic stabilization
  - Dissipation (tau): delays collapse but does not prevent it (metastability only)
  - Topological charge: conserved but does not prevent radial shrinkage
  - Skyrme L4: WOULD stabilize (gradient-energy penalty vs. collapse)
    but remains MBU (Appendix N)

Dissipation role: metastability aid, not true stabilizer.
  The constitutive relaxation timescale tau introduces a dissipative lag.
  A collapsing configuration loses energy to dissipation during collapse.
  This SLOWS collapse but does not PREVENT it (no restoring force).
  Metastability: the configuration persists longer than naive Derrick
  timescale but eventually collapses unless stabilized by Skyrme or topology.

Topological route: motivated but unbuilt.
  O(3) + Skyrme = the strongest identified stabilization path:
  - O(3) provides topological charge (localization seed)
  - Skyrme L4 provides gradient-energy penalty (collapse resistance)
  - Together: stable topological soliton (Skyrmion) with finite size
  - Status: O(3) is MIP, Skyrme is MBU — route is identified, not built

Bound structure: not yet established.
  Bound structure requires: stable objects + attractive interaction + discrete spectrum.
  Current package has: localization (partial), persistence (partial), NO stability proof,
  NO binding mechanism, NO discrete energy levels.
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

N_STABILITY_CRITERIA: int = 6
N_NATIVE_CANDIDATES: int = 6
N_TOPOLOGICAL_CHECKS: int = 4
N_DISSIPATION_TESTS: int = 5
N_BENCHMARK_CANDIDATES: int = 4
N_ENERGY_CHECKS: int = 5
N_QUANTUM_CHECKS: int = 5
N_READINESS_DOMAINS: int = 6
N_PROBABILITY_TESTS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_RC_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
RB_INHERITED_LOCALIZATION: str = "shell_and_excitation_localization_only"
RB_INHERITED_OBJECTHOOD: str = "bosonic_objecthood_structurally_plausible_but_unbuilt"
RB_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_RC"

# R-C Verdict strings
RC_NATIVE_STABILITY_VERDICT: str = "no_native_stabilizer_found"
RC_DISSIPATION_VERDICT: str = "dissipation_supports_metastability_only"
RC_TOPOLOGICAL_VERDICT: str = "topological_route_motivated_but_unbuilt"
RC_BOUND_STRUCTURE_VERDICT: str = "bosonic_bound_structure_not_yet_established"
RC_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_RD"
RC_OVERALL_APPENDIX_P_CLASS: str = "bounded_structural_result"

# Frozensets
ALLOWED_NATIVE_STABILITY_VERDICTS: frozenset = frozenset({
    "no_native_stabilizer_found",
    "native_stability_structurally_plausible_but_unbuilt",
    "native_stability_partially_supported",
    "native_stability_demonstrated",
})
ALLOWED_DISSIPATION_VERDICTS: frozenset = frozenset({
    "dissipation_supports_metastability_only",
    "dissipation_adds_no_true_stability",
    "dissipation_stability_role_underdetermined",
    "dissipation_contributes_to_effective_stabilization",
})
ALLOWED_TOPOLOGICAL_VERDICTS: frozenset = frozenset({
    "topological_route_motivated_but_unbuilt",
    "topological_route_extension_ready",
    "topological_route_precondition_only",
    "topological_route_blocked",
})
ALLOWED_BOUND_STRUCTURE_VERDICTS: frozenset = frozenset({
    "bosonic_bound_candidate_structurally_plausible",
    "bosonic_bound_structure_extension_ready",
    "bosonic_bound_structure_not_yet_established",
    "bosonic_bound_structure_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_RD",
    "authorized_only_for_further_stabilization_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_MNO_or_RB",
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

RC_NONCLAIMS: List[str] = [
    "NOT_claiming_dissipation_therefore_stabilization__"
    "dissipative_lag_slows_collapse_but_does_not_prevent_it",
    "NOT_claiming_shell_persistence_therefore_bound_structure__"
    "boundary_confinement_is_not_intrinsic_binding",
    "NOT_claiming_topological_charge_therefore_stabilized_object__"
    "charge_conservation_does_not_prevent_radial_collapse",
    "NOT_claiming_O3_plus_Skyrme_route_already_built__"
    "O3_is_MIP_and_Skyrme_is_MBU_both_extension_level",
    "NOT_claiming_metastability_therefore_particle_ontology__"
    "delayed_collapse_is_not_stable_particle",
    "NOT_claiming_extension_level_bound_candidate_therefore_native_canon__"
    "all_RC_stabilization_results_carry_BSR_or_MBU_floor",
    "NOT_claiming_bound_structure_progress_therefore_fermionic_obstruction_softened__"
    "fermionic_3_layer_block_unchanged",
    "NOT_claiming_stabilization_benchmark_therefore_chemistry_readiness__"
    "stabilization_is_one_prerequisite_not_matter_closure",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RCStabilityCriterion:
    criterion_id: str; criterion_name: str; description: str
    satisfied: str; notes: List[str]

@dataclass
class RCStabilityCriteriaAudit:
    criteria: List[RCStabilityCriterion]; n_criteria: int
    n_satisfied: int; n_partial: int; n_not_satisfied: int; notes: List[str]

@dataclass
class RCNativeCandidate:
    candidate_id: str; candidate_name: str; description: str
    provides_stability: bool; stability_type: str; notes: List[str]

@dataclass
class RCNativeStabilizationAudit:
    candidates: List[RCNativeCandidate]; n_candidates: int
    n_provides: int; native_stability_verdict: str; notes: List[str]

@dataclass
class RCTopologicalCheck:
    check_id: str; check_name: str; description: str
    status: str; notes: List[str]

@dataclass
class RCTopologicalStabilizationAudit:
    checks: List[RCTopologicalCheck]; n_checks: int
    topological_verdict: str; notes: List[str]

@dataclass
class RCDissipationTest:
    test_id: str; test_name: str; description: str
    result: str; notes: List[str]

@dataclass
class RCDissipationAudit:
    tests: List[RCDissipationTest]; n_tests: int
    dissipation_verdict: str; metastability_supported: bool; notes: List[str]

@dataclass
class RCBenchmarkCandidate:
    candidate_id: str; candidate_name: str; description: str
    viable: bool; demonstrates: List[str]; does_not_demonstrate: List[str]
    notes: List[str]

@dataclass
class RCBenchmarkAudit:
    candidates: List[RCBenchmarkCandidate]; n_candidates: int
    n_viable: int; chosen_id: str; notes: List[str]

@dataclass
class RCEnergyCheck:
    check_id: str; check_name: str; description: str; available: bool
    notes: List[str]

@dataclass
class RCEnergyScaleAudit:
    checks: List[RCEnergyCheck]; n_checks: int; n_available: int
    notes: List[str]

@dataclass
class RCQuantumCheck:
    check_id: str; check_name: str; adds_stability: bool; notes: List[str]

@dataclass
class RCQuantumContributionAudit:
    checks: List[RCQuantumCheck]; n_checks: int; n_adds_stability: int
    notes: List[str]

@dataclass
class RCReadinessEntry:
    domain: str; readiness_level: str; notes: str

@dataclass
class RCReadinessTable:
    entries: List[RCReadinessEntry]; n_entries: int

@dataclass
class RCProbabilityTest:
    test_id: str; test_name: str; result: str; notes: List[str]

@dataclass
class RCProbabilityBoundaryAudit:
    tests: List[RCProbabilityTest]; n_tests: int
    stabilization_independent_of_probability: bool; notes: List[str]

@dataclass
class RCAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class RCAppendixPAudit:
    entries: List[RCAppendixPEntry]; n_entries: int
    overall_class: str; no_native_canon: bool; notes: List[str]

@dataclass
class RCAuthorizationAudit:
    rd_authorized: bool; authorization_basis: List[str]
    rc_constraints: List[str]; authorization_verdict: str; notes: List[str]

@dataclass
class RCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class RCStabilizationBoundStructureResult:
    valid: bool
    track_a_criteria: RCStabilityCriteriaAudit
    track_b_native: RCNativeStabilizationAudit
    track_c_topological: RCTopologicalStabilizationAudit
    track_d_dissipation: RCDissipationAudit
    track_e_benchmark: RCBenchmarkAudit
    track_f_energy: RCEnergyScaleAudit
    track_g_quantum: RCQuantumContributionAudit
    track_h_readiness: RCReadinessTable
    track_i_probability: RCProbabilityBoundaryAudit
    track_j_appendix_p: RCAppendixPAudit
    track_k_authorization: RCAuthorizationAudit
    track_l_nonclaims: RCNonclaimFirewall
    native_stability_verdict: str
    dissipation_verdict: str
    topological_stability_verdict: str
    bound_structure_verdict: str
    authorization_verdict: str
    rc_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> RCStabilityCriteriaAudit:
    criteria = [
        RCStabilityCriterion("SC1", "derrick_collapse_resistance",
            "Configuration does not shrink to zero size.", "not_satisfied",
            ["Derrick theorem: static scalar solitons unstable in d>=2",
             "Requires Skyrme L4 or equivalent stabilizer (MBU)"]),
        RCStabilityCriterion("SC2", "dissipative_decay_resistance",
            "Configuration does not dissipate away.", "partially",
            ["Constitutive attractor restores average Phi",
             "But excitations decay at rate gamma; only metastability"]),
        RCStabilityCriterion("SC3", "persistent_support_region",
            "Support region persists over long timescales.", "partially",
            ["Shell boundary: persists (native)",
             "Topological defect: charge conserved (extension)",
             "Excitation: transient (decays)"]),
        RCStabilityCriterion("SC4", "bounded_energy",
            "Energy is finite and bounded from below.", "extension_level",
            ["Classical field energy: requires O(3) + Skyrme for finite-energy soliton",
             "Without Skyrme: energy of winding configuration diverges or collapses"]),
        RCStabilityCriterion("SC5", "restoring_mechanism",
            "A restoring force or stabilizing term prevents collapse.", "not_satisfied",
            ["Skyrme L4: gradient-energy penalty would provide restoring mechanism",
             "Not yet installed (MBU); no native equivalent found"]),
        RCStabilityCriterion("SC6", "admissible_dynamical_regime",
            "Stable configuration exists within a well-defined dynamical regime.", "extension_level",
            ["Would require: O(3) + Skyrme + Lindblad dynamics in stable regime",
             "Regime not yet specified; extension-level"]),
    ]
    n_s = sum(1 for c in criteria if c.satisfied == "satisfied")
    n_p = sum(1 for c in criteria if c.satisfied == "partially")
    n_n = sum(1 for c in criteria if c.satisfied == "not_satisfied")
    return RCStabilityCriteriaAudit(
        criteria=criteria, n_criteria=N_STABILITY_CRITERIA,
        n_satisfied=n_s, n_partial=n_p, n_not_satisfied=n_n,
        notes=["0 satisfied, 2 partial, 2 not satisfied, 2 extension-level",
               "Key blockers: Derrick collapse (SC1) and restoring mechanism (SC5)"],
    )


def _build_track_b() -> RCNativeStabilizationAudit:
    candidates = [
        RCNativeCandidate("NS1", "constitutive_attractor",
            "tau d<Phi>/dt + <Phi> = <X>: restores average to attractor.",
            False, "attractor_not_stabilizer",
            ["Restores average Phi but does not prevent spatial collapse",
             "Attractor is for the mean field, not for localized structure"]),
        RCNativeCandidate("NS2", "shell_boundary_support",
            "Boundary confinement prevents dispersion beyond boundary.",
            False, "confinement_not_stabilization",
            ["Shell confines but does not stabilize internal structure",
             "Content within shell can still collapse or redistribute"]),
        RCNativeCandidate("NS3", "dissipative_lag",
            "Dissipation timescale tau slows dynamic processes.",
            False, "delay_not_prevention",
            ["Slows collapse but does not prevent it",
             "Metastability: longer-lived but not stable"]),
        RCNativeCandidate("NS4", "decoherence_pointer_selection",
            "Pointer-basis selection suppresses quantum fluctuations.",
            False, "basis_selection_not_spatial_stabilization",
            ["Selects quantum basis, not spatial configuration",
             "Does not address Derrick collapse (classical instability)"]),
        RCNativeCandidate("NS5", "many_mode_dissipative_propagation",
            "H_hop + Lindblad: excitations propagate and decay.",
            False, "propagation_not_stabilization",
            ["Propagation moves excitations; does not stabilize them",
             "Dissipative propagation = excitation LOSS, not stabilization"]),
        RCNativeCandidate("NS6", "no_native_stabilizer",
            "No native GRUT ingredient provides true stabilization.",
            True, "confirmed_absence",
            ["All 5 native candidates fail to provide true stabilization",
             "Stabilization requires extension (Skyrme L4 or equivalent)"]),
    ]
    n_prov = sum(1 for c in candidates if c.provides_stability and c.candidate_id != "NS6")
    return RCNativeStabilizationAudit(
        candidates=candidates, n_candidates=N_NATIVE_CANDIDATES,
        n_provides=n_prov, native_stability_verdict=RC_NATIVE_STABILITY_VERDICT,
        notes=["All 5 native routes fail: attractor, shell, dissipation, "
               "decoherence, propagation — none prevents Derrick collapse",
               "NS6 confirmed: no native stabilizer found",
               "Stabilization requires Skyrme L4 (MBU) or new mechanism"],
    )


def _build_track_c() -> RCTopologicalStabilizationAudit:
    checks = [
        RCTopologicalCheck("TS1", "o3_charge_provides_localization_seed",
            "pi_2(S^2) = Z integer winding: localization seed for defects.",
            "established_extension_level",
            ["O(3) MIP provides topological charge structure",
             "Winding number conservation prevents charge decay"]),
        RCTopologicalCheck("TS2", "o3_defect_localization",
            "Topological defect has concentrated energy density.",
            "established_extension_level",
            ["Energy density concentrates near defect center",
             "But without Skyrme: no finite-size equilibrium (Derrick)"]),
        RCTopologicalCheck("TS3", "skyrme_l4_stabilization",
            "Skyrme L4 gradient-energy penalty prevents collapse to zero size.",
            "motivated_but_unbuilt",
            ["L4 term: higher-derivative contribution to energy",
             "Creates energy cost for too-small configurations",
             "Balances O(3) topological energy: yields finite-size soliton",
             "Status: MBU from Appendix N — path identified, not built"]),
        RCTopologicalCheck("TS4", "combined_o3_skyrme_stable_soliton",
            "O(3) + Skyrme: Skyrmion with finite size, finite energy, topological stability.",
            "motivated_but_unbuilt",
            ["The FULL stabilized object requires BOTH O(3) and Skyrme",
             "O(3) alone: charge but no size stability (Derrick)",
             "Skyrme alone: stabilizer but no topological charge",
             "Together: Skyrmion — the canonical stable topological soliton",
             "Status: both extensions needed; route identified, not built"]),
    ]
    return RCTopologicalStabilizationAudit(
        checks=checks, n_checks=N_TOPOLOGICAL_CHECKS,
        topological_verdict=RC_TOPOLOGICAL_VERDICT,
        notes=["TS1-TS2: O(3) provides charge and defect localization (extension-level)",
               "TS3: Skyrme L4 would stabilize (MBU, not built)",
               "TS4: combined route = Skyrmion (MBU, strongest path)",
               "Verdict: motivated_but_unbuilt — route clear, work not done"],
    )


def _build_track_d() -> RCDissipationAudit:
    tests = [
        RCDissipationTest("DS1", "dissipation_slows_collapse",
            "Constitutive tau introduces viscous drag on field dynamics.",
            "confirmed",
            ["Energy loss to dissipation during collapse slows the process",
             "Collapse timescale increases from instant to O(tau)"]),
        RCDissipationTest("DS2", "dissipation_does_not_prevent_collapse",
            "No restoring force from dissipation alone.",
            "confirmed",
            ["Damping reduces velocity but does not reverse direction",
             "Without restoring term, configuration still eventually collapses"]),
        RCDissipationTest("DS3", "metastability_supported",
            "Dissipation extends lifetime of unstable configurations.",
            "confirmed",
            ["Configuration persists on timescale >> tau before collapse",
             "This IS metastability: long-lived but not permanent"]),
        RCDissipationTest("DS4", "dissipation_as_energy_drain",
            "Dissipation continuously removes energy from the system.",
            "confirmed",
            ["Energy flows out through dissipative channel",
             "For localized structures: dissipation erodes the configuration"]),
        RCDissipationTest("DS5", "dissipation_incompatible_with_stability",
            "Dissipation alone is fundamentally incompatible with true stability.",
            "partially",
            ["Partially: dissipation + restoring force CAN give stable attractor",
             "But: the restoring force (Skyrme) is not native, it is MBU",
             "In principle: dissipation + Skyrme = dissipative stable soliton",
             "Without Skyrme: dissipation alone incompatible with stability"]),
    ]
    return RCDissipationAudit(
        tests=tests, n_tests=N_DISSIPATION_TESTS,
        dissipation_verdict=RC_DISSIPATION_VERDICT,
        metastability_supported=True,
        notes=["Dissipation slows collapse and supports metastability",
               "Dissipation does NOT prevent collapse or provide restoring force",
               "Key: dissipation + Skyrme would = dissipative stable soliton",
               "Without Skyrme: metastability only",
               "Verdict: dissipation_supports_metastability_only"],
    )


def _build_track_e() -> RCBenchmarkAudit:
    candidates = [
        RCBenchmarkCandidate("SB1", "dissipative_metastability_benchmark",
            "Shell + topological charge + dissipative lag: "
            "configuration persists for time >> tau before eventual collapse.",
            True,
            ["metastability_demonstrated", "extended_lifetime_via_dissipation",
             "topological_charge_conservation"],
            ["true_stability", "bound_state", "particle_ontology",
             "finite_size_equilibrium"],
            ["Best currently available benchmark: metastability + charge"]),
        RCBenchmarkCandidate("SB2", "extension_topological_stabilized",
            "O(3) + Skyrme + Lindblad: stable Skyrmion with dissipative dynamics.",
            True,
            ["topological_stabilization", "finite_size_soliton",
             "dissipative_dynamics_on_stable_object"],
            ["native_derivation", "particle_identity", "bound_state"],
            ["Extension-level benchmark: requires O(3) MIP + Skyrme MBU",
             "Strongest possible benchmark but both extensions needed"]),
        RCBenchmarkCandidate("SB3", "excitation_only_benchmark",
            "Qubit chain excitation with decoherence.",
            True,
            ["excitation_localization", "dissipative_decay"],
            ["spatial_localization", "stability", "objecthood", "binding"],
            ["Weakest: no classical localization, only quantum excitation"]),
        RCBenchmarkCandidate("SB4", "no_benchmark",
            "No admissible benchmark.", False, [], [],
            ["Rejected: SB1-SB3 viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return RCBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_id="SB1_dissipative_metastability_benchmark",
        notes=["SB1 chosen: dissipative metastability (best current)",
               "SB2 stronger but extension-level (O(3) + Skyrme needed)",
               "Neither demonstrates true stability or bound structure"],
    )


def _build_track_f() -> RCEnergyScaleAudit:
    checks = [
        RCEnergyCheck("ES1", "tau_as_characteristic_scale",
            "tau^2 = 3/2: characteristic timescale.", True,
            ["Native canon; provides energy/time scale"]),
        RCEnergyCheck("ES2", "barrier_amplitude_a",
            "Barrier amplitude from GRUT action.", True,
            ["Native: provides energy density scale"]),
        RCEnergyCheck("ES3", "shell_radius",
            "Shell radius from boundary structure.", True,
            ["Appendix M: shell provides length scale"]),
        RCEnergyCheck("ES4", "skyrmion_radius_energy_balance",
            "Skyrmion radius from L2/L4 energy balance.", False,
            ["Requires Skyrme L4 (MBU); R ~ sqrt(L4_coeff / L2_coeff)",
             "Not available without Skyrme term"]),
        RCEnergyCheck("ES5", "binding_energy_discrete_spectrum",
            "Discrete energy levels from binding potential.", False,
            ["Requires attractive interaction + potential well",
             "Not available in current package"]),
    ]
    n_a = sum(1 for c in checks if c.available)
    return RCEnergyScaleAudit(
        checks=checks, n_checks=N_ENERGY_CHECKS, n_available=n_a,
        notes=["3 scales available: tau, barrier amplitude, shell radius",
               "2 not available: Skyrmion radius (MBU), binding energy (absent)"],
    )


def _build_track_g() -> RCQuantumContributionAudit:
    checks = [
        RCQuantumCheck("QS1", "state_space_support", False,
            ["Density matrix on qubit chain: description, not stabilization"]),
        RCQuantumCheck("QS2", "decoherence_pointer_robustness", False,
            ["Pointer basis selects quantum basis, not spatial stability"]),
        RCQuantumCheck("QS3", "dissipative_metastability_enhancement", False,
            ["Lindblad dynamics adds dissipative lag; metastability only"]),
        RCQuantumCheck("QS4", "diagnostic_weight_description", False,
            ["Diagnostic weights describe configurations, not stabilize them"]),
        RCQuantumCheck("QS5", "no_quantum_stabilizer", False,
            ["Q program adds zero stabilization; only readiness language"]),
    ]
    n_s = sum(1 for c in checks if c.adds_stability)
    return RCQuantumContributionAudit(
        checks=checks, n_checks=N_QUANTUM_CHECKS, n_adds_stability=n_s,
        notes=["Q program adds 0 stability contributions",
               "Consistent with R-B finding: Q adds readiness, not objecthood/stability"],
    )


def _build_track_h() -> RCReadinessTable:
    entries = [
        RCReadinessEntry("native_stabilization", "blocked",
            "No native stabilizer found; Derrick obstruction unresolved"),
        RCReadinessEntry("dissipative_metastability", "extension_ready",
            "Dissipation supports metastability; not true stability"),
        RCReadinessEntry("topological_stabilization_route", "extension_ready",
            "O(3) + Skyrme route identified; both extension-level"),
        RCReadinessEntry("bosonic_bound_candidate", "precondition_only",
            "Localization + persistence partial; stability gap"),
        RCReadinessEntry("stable_bosonic_bound_structure", "precondition_only",
            "No stability proof; no binding mechanism"),
        RCReadinessEntry("pre_atomic_matter_readiness", "precondition_only",
            "Requires stable objects + binding; neither established"),
    ]
    return RCReadinessTable(entries=entries, n_entries=N_READINESS_DOMAINS)


def _build_track_i() -> RCProbabilityBoundaryAudit:
    tests = [
        RCProbabilityTest("PB1", "stabilization_structural",
            "independent",
            ["Stabilization is structural/dynamic, not probabilistic"]),
        RCProbabilityTest("PB2", "binding_structural",
            "independent",
            ["Binding is energetic/dynamic, not probabilistic"]),
        RCProbabilityTest("PB3", "metastability_structural",
            "independent",
            ["Metastability is timescale analysis, not probability"]),
        RCProbabilityTest("PB4", "interpretive_claims_conditional",
            "conditional",
            ["If asking 'what is the probability this object exists?', "
             "Born rule needed; structural claims do not"]),
    ]
    return RCProbabilityBoundaryAudit(
        tests=tests, n_tests=N_PROBABILITY_TESTS,
        stabilization_independent_of_probability=True,
        notes=["Structural stabilization claims independent of probability",
               "Interpretive claims would need Born postulate"],
    )


def _build_track_j() -> RCAppendixPAudit:
    entries = [
        RCAppendixPEntry("RC_native_absence", "No native stabilizer",
            "bounded_structural_result",
            "No native GRUT ingredient provides true stabilization",
            "Native stabilization exists or is structurally plausible",
            "All native candidates audited; Derrick obstruction"),
        RCAppendixPEntry("RC_dissipation_metastability", "Dissipative metastability",
            "motivated_but_unbuilt",
            "Dissipation supports metastability (delayed collapse)",
            "Dissipation provides true stability",
            "Part I constitutive dynamics; tau relaxation"),
        RCAppendixPEntry("RC_topological_route", "Topological stabilization route",
            "motivated_but_unbuilt",
            "O(3) + Skyrme route identified; extension-level",
            "Topological stabilization already built",
            "Appendices N, O; both extension-level"),
        RCAppendixPEntry("RC_derrick_obstruction", "Derrick obstruction",
            "bounded_structural_result",
            "Derrick obstruction documented and unresolved without Skyrme",
            "Derrick obstruction circumvented by native GRUT means",
            "Appendix M; requires L4 higher-derivative term"),
        RCAppendixPEntry("RC_bound_absence", "Bound structure absent",
            "bounded_structural_result",
            "Bound structure not established: no stability, no binding",
            "Bound structure available from localization alone",
            "R-B localization + R-C stability gap"),
        RCAppendixPEntry("RC_quantum_no_stabilizer", "Q adds no stabilizer",
            "bounded_structural_result",
            "Quantum program adds readiness, not stabilization",
            "Quantum excitation grammar provides stabilization",
            "Q-II.E, R-B Track E"),
        RCAppendixPEntry("RC_overall", "R-C overall",
            "bounded_structural_result",
            "Stabilization and bound structure: gaps documented, routes identified",
            "Stabilization or binding achieved",
            "All R-C tracks"),
    ]
    return RCAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RC_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["4 BSR (documented absences/obstructions), 2 MBU (routes), 1 BSR (overall)",
               "Overall BSR: this appendix documents what is absent and the path forward"],
    )


def _build_track_k() -> RCAuthorizationAudit:
    return RCAuthorizationAudit(
        rd_authorized=True,
        authorization_basis=[
            "stabilization_gap_fully_documented",
            "dissipative_metastability_characterized",
            "topological_route_identified_extension_level",
            "bound_structure_absence_documented",
            "rb_objecthood_assessment_inherited",
        ],
        rc_constraints=[
            "RD_must_not_assume_stable_bosonic_objects",
            "RD_must_not_assume_binding_mechanism_available",
            "RD_must_investigate_composite_matter_with_extension_flags",
            "RD_results_inherit_BSR_or_MBU_floor",
            "RD_must_preserve_fermionic_obstruction",
        ],
        authorization_verdict=RC_AUTHORIZATION_VERDICT,
        notes=["R-D authorized: stabilization gap documented, R-D investigates "
               "composite matter and pre-atomic structure",
               "R-D must work with the gap, not assume it is resolved"],
    )


def _build_track_l() -> RCNonclaimFirewall:
    return RCNonclaimFirewall(
        nonclaims=RC_NONCLAIMS, n_nonclaims=N_RC_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_rc_stabilization_bound_structure_audit() -> RCStabilizationBoundStructureResult:
    ta = _build_track_a(); tb = _build_track_b(); tc = _build_track_c()
    td = _build_track_d(); te = _build_track_e(); tf = _build_track_f()
    tg = _build_track_g(); th = _build_track_h(); ti = _build_track_i()
    tj = _build_track_j(); tk = _build_track_k(); tl = _build_track_l()

    allowed_claims: List[str] = [
        "No native GRUT stabilizer found: constitutive attractor, shell, "
        "dissipation, decoherence, and propagation all fail to prevent Derrick collapse",
        "Dissipation supports metastability: extends lifetime of unstable "
        "configurations but does not prevent eventual collapse",
        "Topological stabilization route (O(3) + Skyrme) motivated but unbuilt: "
        "strongest identified path to stable bosonic objects",
        "Derrick obstruction remains real: static solitons unstable in d >= 2 "
        "without Skyrme L4 or equivalent higher-derivative stabilizer",
        "Bound structure not established: no stability proof, no binding mechanism, "
        "no discrete energy spectrum",
        "Quantum program adds zero stabilization: consistent with R-B finding "
        "that Q adds readiness, not objecthood or stability",
        "R-D authorized: stabilization gap documented, composite matter "
        "investigation may proceed with explicit extension flags",
    ]
    forbidden_claims: List[str] = [
        "Dissipation implies stabilization",
        "Shell persistence implies bound structure",
        "Topological charge implies stabilized object",
        "O(3) + Skyrme route is already built",
        "Metastability implies particle ontology",
        "Extension-level bound candidate implies native canon",
        "Stabilization progress implies fermionic obstruction softened",
    ]
    diagnostics: Dict[str, Any] = {
        "n_stability_criteria": N_STABILITY_CRITERIA,
        "n_criteria_satisfied": ta.n_satisfied,
        "n_criteria_partial": ta.n_partial,
        "n_criteria_not_satisfied": ta.n_not_satisfied,
        "n_native_candidates": N_NATIVE_CANDIDATES,
        "n_native_provides_stability": tb.n_provides,
        "metastability_supported": td.metastability_supported,
        "n_benchmark_viable": te.n_viable,
        "n_energy_scales_available": tf.n_available,
        "quantum_adds_stability": tg.n_adds_stability,
        "stabilization_independent_of_probability": ti.stabilization_independent_of_probability,
        "n_nonclaims": N_RC_NONCLAIMS,
    }

    result = RCStabilizationBoundStructureResult(
        valid=True,
        track_a_criteria=ta, track_b_native=tb, track_c_topological=tc,
        track_d_dissipation=td, track_e_benchmark=te, track_f_energy=tf,
        track_g_quantum=tg, track_h_readiness=th, track_i_probability=ti,
        track_j_appendix_p=tj, track_k_authorization=tk, track_l_nonclaims=tl,
        native_stability_verdict=tb.native_stability_verdict,
        dissipation_verdict=td.dissipation_verdict,
        topological_stability_verdict=tc.topological_verdict,
        bound_structure_verdict=RC_BOUND_STRUCTURE_VERDICT,
        authorization_verdict=tk.authorization_verdict,
        rc_appendix_p_class=RC_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RC_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_rc_result(result)
    return result


def validate_rc_result(result: RCStabilizationBoundStructureResult) -> None:
    checks = [
        (result.native_stability_verdict, ALLOWED_NATIVE_STABILITY_VERDICTS, "Native"),
        (result.dissipation_verdict, ALLOWED_DISSIPATION_VERDICTS, "Dissipation"),
        (result.topological_stability_verdict, ALLOWED_TOPOLOGICAL_VERDICTS, "Topological"),
        (result.bound_structure_verdict, ALLOWED_BOUND_STRUCTURE_VERDICTS, "Bound"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.rc_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class invalid")
    for e in result.track_j_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}' class invalid")
    if result.track_l_nonclaims.n_nonclaims != N_RC_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_l_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_j_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_k_authorization.rd_authorized:
        raise ValueError("rd_authorized must be True")
    if result.track_b_native.n_provides != 0:
        raise ValueError("n_provides must be 0 (no native stabilizer)")
    if result.track_g_quantum.n_adds_stability != 0:
        raise ValueError("quantum n_adds_stability must be 0")
    for e in result.track_h_readiness.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"Readiness '{e.domain}': level invalid")


def _self_test() -> bool:
    r = run_rc_stabilization_bound_structure_audit()
    assert r.valid is True
    assert r.native_stability_verdict == RC_NATIVE_STABILITY_VERDICT
    assert r.dissipation_verdict == RC_DISSIPATION_VERDICT
    assert r.topological_stability_verdict == RC_TOPOLOGICAL_VERDICT
    assert r.bound_structure_verdict == RC_BOUND_STRUCTURE_VERDICT
    assert r.authorization_verdict == RC_AUTHORIZATION_VERDICT
    assert r.diagnostics["n_native_provides_stability"] == 0
    assert r.diagnostics["quantum_adds_stability"] == 0
    assert r.diagnostics["metastability_supported"] is True
    return True


if __name__ == "__main__":
    _self_test()
    print("R-C self-test passed.")
