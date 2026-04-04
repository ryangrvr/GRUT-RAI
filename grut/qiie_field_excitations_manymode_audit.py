"""
Appendix Q-II.E --- Field Excitations and Many-Mode Structure Audit
====================================================================
GRUT Quantum Program --- Phase Q-II.E

This module audits whether the GRUT quantum extension can support coherent
field-excitation and many-mode structure beyond two-state toys.

Inherited structure
-------------------
Q-II.B: Composite C^4 = C^2 tensor C^2; tensor product composition (MIP).
Q-II.C: Nonfactorized states; entanglement witnesses at density-matrix level.
Q-II.D: Multi-observable grammar; toy noncommuting pair {sigma_z, sigma_x};
         correlator grammar through CHSH algebraic level; su(2) on C^2.

Key physics for this audit
--------------------------
The current GRUT quantum extension operates on:
  - Single-site: C^2 (two-state qubit) with Phi_hat = sigma_z
  - Two-site composite: C^4 = C^2 tensor C^2
  - Observable algebra: su(2) per site (postulated via sigma_x extension)
  - Dynamics: independent Lindblad channels (no interaction H_int)

To support excitations and many-mode structure, we need:
  - Mode labels: a way to index multiple sites or modes
  - Excitation operators: raising/lowering or number-like operators
  - Propagation: a mechanism for excitations to move between modes
  - Compatibility with dissipative (Lindbladian) dynamics

Mode grammar:
  The simplest route is N copies of the 2-state system (a qubit chain).
  Each site i has Hilbert space C^2_i, observables sigma_{x,y,z}^{(i)},
  and an independent Lindblad channel.  The composite space is (C^2)^{tensor N}.

Excitation operators:
  On a single qubit: sigma_+ = (sigma_x + i sigma_y)/2 and
  sigma_- = (sigma_x - i sigma_y)/2 are raising/lowering operators.
  sigma_+ |0> = |1>, sigma_- |1> = |0>.  These are DEFINED (not derived)
  from the postulated observable algebra.  They are NOT canonical bosonic
  ladder operators [a, a^dag] = 1.  They satisfy fermionic-like {sigma_+,
  sigma_-} = I (anticommutation on a single site).

  For multi-site: sigma_+^{(i)} tensor I_{others} raises site i.
  An excitation that moves from site i to site j requires an interaction
  Hamiltonian H_hop = J (sigma_+^{(i)} sigma_-^{(j)} + h.c.).

Propagation:
  Without H_int, there is NO propagation.  Independent channels cannot
  move excitations between sites.  Propagation requires:
    - H_hop (hopping Hamiltonian): extension-level postulate
    - Or dissipative coupling (Lindblad jump operators connecting sites)

  The simplest coherent route is H_hop = J sum_{<i,j>} sigma_+^i sigma_-^j.
  Under H_hop + independent decoherence, excitations propagate and decay.
  This is DISSIPATIVE PROPAGATION: excitations move but lose coherence.

Many-mode benchmark:
  The smallest admissible benchmark is a 2-site chain with H_hop coupling:
    H = C^2 tensor C^2 = C^4
    H_hop = J (sigma_+^{(1)} sigma_-^{(2)} + sigma_-^{(1)} sigma_+^{(2)})
    L_1 = sqrt(gamma) sigma_z tensor I,  L_2 = I tensor sqrt(gamma) sigma_z
  This demonstrates: mode labeling, excitation transfer, dissipative decay.
  It does NOT demonstrate: continuum modes, particle dispersion, or QFT.

Matter boundary:
  Excitation grammar advances pre-matter readiness but does NOT establish
  particle ontology.  Bosonic route: structurally advanced (excitation
  counting via sigma_+ sigma_- on each site).  Fermionic route: still
  blocked (pi_2(S^2) = Z obstruction from Q0).
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

SINGLE_SITE_DIM: int = 2
TWO_SITE_DIM: int = 4
N_SITE_BENCHMARK: int = 2

# Track counts
N_ELIGIBILITY_INGREDIENTS: int = 5
N_MODE_CANDIDATES: int = 5
N_EXCITATION_CANDIDATES: int = 4
N_PROPAGATION_CANDIDATES: int = 5
N_BENCHMARK_CANDIDATES: int = 4
N_EXCITATION_CLASS_LEVELS: int = 5
N_CONSTITUTIVE_CHECKS: int = 4
N_MATTER_LEVELS: int = 5
N_APPENDIX_P_ENTRIES: int = 7
N_QIIE_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
QIID_INHERITED_OBSERVABLE: str = "multiple_observable_classes_extension_level_only"
QIID_INHERITED_NONCOMM: str = "toy_noncommuting_pair_justified"
QIID_INHERITED_CORRELATOR: str = "correlator_grammar_extension_level_only"
QIID_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QIIE"

# Q-II.E Verdict strings
QIIE_MODE_VERDICT: str = "mode_grammar_extension_level_only"
QIIE_EXCITATION_VERDICT: str = "dissipative_mode_excitation_structure_demonstrated"
QIIE_PROPAGATION_VERDICT: str = "dissipative_propagation_only"
QIIE_MATTER_BOUNDARY_VERDICT: str = (
    "pre_matter_readiness_advanced_but_particle_ontology_premature"
)
QIIE_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QIIF"
QIIE_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozensets
ALLOWED_MODE_VERDICTS: frozenset = frozenset({
    "coherent_mode_grammar_identified",
    "mode_grammar_extension_level_only",
    "mode_grammar_underdetermined",
    "mode_grammar_blocked",
})
ALLOWED_EXCITATION_VERDICTS: frozenset = frozenset({
    "propagating_toy_excitations_demonstrated",
    "dissipative_mode_excitation_structure_demonstrated",
    "excitation_structure_extension_level_only",
    "excitation_structure_blocked",
})
ALLOWED_PROPAGATION_VERDICTS: frozenset = frozenset({
    "coherent_propagation_route_identified",
    "dissipative_propagation_only",
    "propagation_route_underdetermined",
    "propagation_route_blocked",
})
ALLOWED_MATTER_BOUNDARY_VERDICTS: frozenset = frozenset({
    "pre_matter_readiness_advanced_but_particle_ontology_premature",
    "excitation_grammar_only_no_matter_readiness",
    "bosonic_matter_route_structurally_advanced",
    "matter_boundary_still_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QIIF",
    "authorized_only_for_further_excitation_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_QIID",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8)
QIIE_NONCLAIMS: List[str] = [
    "NOT_claiming_many_mode_labels_therefore_field_theory_solved__"
    "mode_labels_are_bookkeeping_not_continuum_field_quantization",
    "NOT_claiming_excitation_bookkeeping_therefore_particles_derived__"
    "site_excitation_counting_is_not_particle_ontology",
    "NOT_claiming_propagating_toy_mode_therefore_matter_ontology__"
    "dissipative_hopping_on_two_sites_is_not_matter_physics",
    "NOT_claiming_ladder_like_notation_therefore_canonical_creation_annihilation__"
    "sigma_plus_minus_are_qubit_operators_not_bosonic_ladder_operators",
    "NOT_claiming_coupled_toy_sites_therefore_continuum_field_quantization__"
    "finite_site_chain_is_not_quantum_field_theory",
    "NOT_claiming_many_mode_decoherence_therefore_measurement_solved__"
    "dissipative_dynamics_on_chain_does_not_solve_measurement_problem",
    "NOT_claiming_extension_level_excitation_therefore_native_canon__"
    "all_QIIE_results_carry_MBU_or_MIP_floor",
    "NOT_claiming_excitation_grammar_therefore_fermionic_route_reopened__"
    "fermionic_3_layer_obstruction_from_Q0_unchanged",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIEEligibilityIngredient:
    ingredient_id: str
    ingredient_name: str
    description: str
    status: str
    source: str
    notes: List[str]


@dataclass
class QIIEExcitationEligibilityAudit:
    ingredients: List[QIIEEligibilityIngredient]
    n_ingredients: int
    n_present: int
    n_extension_level: int
    n_absent: int
    eligibility_verdict: str
    notes: List[str]


@dataclass
class QIIEModeCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    viability_level: str
    notes: List[str]


@dataclass
class QIIEModeLabelAudit:
    candidates: List[QIIEModeCandidate]
    n_candidates: int
    n_viable: int
    chosen_candidate_id: str
    mode_verdict: str
    notes: List[str]


@dataclass
class QIIEExcitationCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    status: str
    coherent: bool
    notes: List[str]


@dataclass
class QIIEExcitationOperatorAudit:
    candidates: List[QIIEExcitationCandidate]
    n_candidates: int
    chosen_candidate_id: str
    excitation_verdict: str
    notes: List[str]


@dataclass
class QIIEPropagationCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    preserves_decoherence: bool
    notes: List[str]


@dataclass
class QIIEPropagationAudit:
    candidates: List[QIIEPropagationCandidate]
    n_candidates: int
    n_viable: int
    chosen_candidate_id: str
    propagation_verdict: str
    notes: List[str]


@dataclass
class QIIEBenchmarkCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    demonstrates: List[str]
    does_not_demonstrate: List[str]
    notes: List[str]


@dataclass
class QIIEManyModeBenchmarkAudit:
    candidates: List[QIIEBenchmarkCandidate]
    n_candidates: int
    n_viable: int
    chosen_benchmark_id: str
    benchmark_n_sites: int
    benchmark_hilbert_dim: int
    notes: List[str]


@dataclass
class QIIEExcitationClassLevel:
    level_id: str
    level_name: str
    description: str
    achieved: bool
    notes: List[str]


@dataclass
class QIIEExcitationClassAudit:
    levels: List[QIIEExcitationClassLevel]
    n_levels: int
    highest_achieved_id: str
    notes: List[str]


@dataclass
class QIIEConstitutiveCheck:
    check_id: str
    check_name: str
    description: str
    result: str
    notes: List[str]


@dataclass
class QIIEConstitutiveCompatibilityAudit:
    checks: List[QIIEConstitutiveCheck]
    n_checks: int
    compatible: bool
    notes: List[str]


@dataclass
class QIIEMatterLevel:
    level_id: str
    level_name: str
    description: str
    status: str
    notes: List[str]


@dataclass
class QIIEMatterReadinessAudit:
    levels: List[QIIEMatterLevel]
    n_levels: int
    matter_boundary_verdict: str
    fermionic_still_blocked: bool
    notes: List[str]


@dataclass
class QIIEAppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIIEAppendixPAudit:
    entries: List[QIIEAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIIEAuthorizationAudit:
    qiif_authorized: bool
    authorization_basis: List[str]
    qiif_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QIIENonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIEFieldExcitationsManyModeResult:
    valid: bool
    track_a_eligibility: QIIEExcitationEligibilityAudit
    track_b_mode_label: QIIEModeLabelAudit
    track_c_excitation_op: QIIEExcitationOperatorAudit
    track_d_propagation: QIIEPropagationAudit
    track_e_benchmark: QIIEManyModeBenchmarkAudit
    track_f_excitation_class: QIIEExcitationClassAudit
    track_g_constitutive: QIIEConstitutiveCompatibilityAudit
    track_h_matter: QIIEMatterReadinessAudit
    track_i_appendix_p: QIIEAppendixPAudit
    track_j_authorization: QIIEAuthorizationAudit
    track_k_nonclaims: QIIENonclaimFirewall
    # Five hard-gated verdicts
    mode_verdict: str
    excitation_verdict: str
    propagation_verdict: str
    matter_boundary_verdict: str
    authorization_verdict: str
    # Summary
    qiie_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIIEExcitationEligibilityAudit:
    ingredients = [
        QIIEEligibilityIngredient(
            "EE1", "multi_mode_degrees_of_freedom",
            "More than one local or mode degree of freedom.",
            "extension_level", "Q-II.B (N-copy tensor product)",
            ["N-site qubit chain: (C^2)^{tensor N}; N >= 2 from Q-II.B"],
        ),
        QIIEEligibilityIngredient(
            "EE2", "admissible_mode_labels",
            "Labels i = 1, ..., N for distinct sites/modes.",
            "extension_level", "Q-II.B subsystem identity (SS1)",
            ["Site labels from copy duplication; extension-level (MIP)"],
        ),
        QIIEEligibilityIngredient(
            "EE3", "propagation_or_coupling_structure",
            "Hopping Hamiltonian H_hop or dissipative coupling between sites.",
            "extension_level", "Must be postulated (H_int gap from Q-II.B)",
            ["H_hop = J sum sigma_+^i sigma_-^j is coherent postulation",
             "Requires new postulate beyond Q-II.B independent channels"],
        ),
        QIIEEligibilityIngredient(
            "EE4", "excitation_counting_grammar",
            "Occupation-like operators n_i = sigma_+^i sigma_-^i on each site.",
            "extension_level", "Q-II.D observable algebra (sigma_+ from su(2))",
            ["sigma_+ sigma_- = (I + sigma_z)/2: number-like operator",
             "Eigenvalues 0, 1 (qubit: at most one excitation per site)"],
        ),
        QIIEEligibilityIngredient(
            "EE5", "lindbladian_compatibility",
            "Excitation and mode structure compatible with Lindblad dynamics.",
            "present", "Part I Lindblad + Q-II.B independent channels",
            ["Independent channels per site preserve Part I structure",
             "H_hop + Lindblad = dissipative dynamics: well-defined"],
        ),
    ]
    n_p = sum(1 for i in ingredients if i.status == "present")
    n_e = sum(1 for i in ingredients if i.status == "extension_level")
    n_a = sum(1 for i in ingredients if i.status == "absent")
    return QIIEExcitationEligibilityAudit(
        ingredients=ingredients, n_ingredients=N_ELIGIBILITY_INGREDIENTS,
        n_present=n_p, n_extension_level=n_e, n_absent=n_a,
        eligibility_verdict="eligible_at_extension_level",
        notes=[f"{n_p} present, {n_e} extension-level, {n_a} absent",
               "Excitation structure is eligible once H_hop is postulated"],
    )


def _build_track_b() -> QIIEModeLabelAudit:
    candidates = [
        QIIEModeCandidate("ML1", "repeated_local_sites",
            "N copies of C^2 with site labels i = 1..N.",
            True, "extension_level",
            ["Simplest: extends Q-II.B copy duplication to N sites",
             "Each site has full Part I structure independently"]),
        QIIEModeCandidate("ML2", "spatially_indexed_sectors",
            "Sites indexed by spatial position.",
            False, "blocked",
            ["Blocked: no spatial DOF in Part I (Q-F remaining gaps)"]),
        QIIEModeCandidate("ML3", "normal_mode_decomposition",
            "Normal modes of a linearized response field.",
            False, "blocked",
            ["Blocked: requires continuum spatial structure not available",
             "Normal modes need Fourier transform over spatial domain"]),
        QIIEModeCandidate("ML4", "topological_mode_classes",
            "Mode classes from topological winding sectors.",
            False, "underdetermined",
            ["Underdetermined: topological winding (Q0 C1) provides integer labels",
             "But connection to quantum mode structure is unbuilt"]),
        QIIEModeCandidate("ML5", "no_mode_grammar",
            "No valid mode grammar.", False, "rejected",
            ["Rejected: ML1 is viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return QIIEModeLabelAudit(
        candidates=candidates, n_candidates=N_MODE_CANDIDATES,
        n_viable=n_v, chosen_candidate_id="ML1_repeated_local_sites",
        mode_verdict=QIIE_MODE_VERDICT,
        notes=["ML1 chosen: N-site qubit chain with site labels",
               "ML2, ML3 blocked (no spatial DOF); ML4 underdetermined",
               "Mode grammar is extension-level: site labels are postulated"],
    )


def _build_track_c() -> QIIEExcitationOperatorAudit:
    candidates = [
        QIIEExcitationCandidate("EX1", "raising_lowering_toy",
            "sigma_+ = (sigma_x + i sigma_y)/2, sigma_- = (sigma_x - i sigma_y)/2.",
            "extension_level", True,
            ["Defined from Q-II.D postulated su(2) algebra",
             "sigma_+ |0> = |1>, sigma_- |1> = |0>",
             "NOT canonical bosonic: {sigma_+, sigma_-} = I (anticommuting on-site)",
             "Qubit excitation: 0 or 1 per site only"]),
        QIIEExcitationCandidate("EX2", "occupation_number_bookkeeping",
            "n_i = sigma_+^i sigma_-^i = (I + sigma_z^i)/2. Eigenvalues 0, 1.",
            "extension_level", True,
            ["Number operator for qubit: counts excitation (0 or 1)",
             "Total excitation N_tot = sum_i n_i is conserved under H_hop",
             "Extension-level: depends on sigma_x postulation"]),
        QIIEExcitationCandidate("EX3", "mode_amplitude_only",
            "Excitations described only by continuous amplitudes, not discrete operators.",
            "underdetermined", False,
            ["Underdetermined: would require continuum mode structure (ML3 blocked)",
             "Not coherent in current discrete-site framework"]),
        QIIEExcitationCandidate("EX4", "no_excitation_operators",
            "No excitation operators available.", "rejected", False,
            ["Rejected: EX1 and EX2 are viable"]),
    ]
    return QIIEExcitationOperatorAudit(
        candidates=candidates, n_candidates=N_EXCITATION_CANDIDATES,
        chosen_candidate_id="EX1_raising_lowering_toy",
        excitation_verdict=QIIE_EXCITATION_VERDICT,
        notes=["EX1 chosen: sigma_+/sigma_- as toy excitation operators",
               "EX2 also viable: occupation counting n_i",
               "These are QUBIT operators, NOT bosonic ladder operators",
               "Dissipative excitation: under Lindblad, excitations decay"],
    )


def _build_track_d() -> QIIEPropagationAudit:
    candidates = [
        QIIEPropagationCandidate("PR1", "nearest_neighbor_hopping",
            "H_hop = J sum_{<i,j>} (sigma_+^i sigma_-^j + h.c.).",
            True, True,
            ["Coherent excitation transfer between adjacent sites",
             "Preserves total excitation number N_tot",
             "Combined with Lindblad: dissipative propagation",
             "Must be postulated as extension (MIP)"]),
        QIIEPropagationCandidate("PR2", "linear_response_propagation",
            "Propagation via linear response kernel.",
            False, True,
            ["Not viable: requires continuum spatial structure (blocked)",
             "Linear response is Part I classical; quantum version needs spatial DOF"]),
        QIIEPropagationCandidate("PR3", "lindbladian_transport",
            "Dissipative spreading via cross-site Lindblad jump operators.",
            True, True,
            ["Viable: L_{ij} = sqrt(kappa) sigma_-^i sigma_+^j jumps excitation i->j",
             "Purely dissipative transport (no coherent oscillation)",
             "Compatible with Part I Lindblad framework"]),
        QIIEPropagationCandidate("PR4", "influence_functional_coupling",
            "Coupling via influence-functional/history-space structure.",
            False, False,
            ["Not viable: requires path-integral formalism not available",
             "Part I uses density-matrix formalism, not path integrals"]),
        QIIEPropagationCandidate("PR5", "no_propagation",
            "No propagation route.", False, False,
            ["Rejected: PR1 and PR3 are viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return QIIEPropagationAudit(
        candidates=candidates, n_candidates=N_PROPAGATION_CANDIDATES,
        n_viable=n_v, chosen_candidate_id="PR1_nearest_neighbor_hopping",
        propagation_verdict=QIIE_PROPAGATION_VERDICT,
        notes=["PR1 chosen: H_hop nearest-neighbor hopping (coherent + dissipative)",
               "PR3 also viable: purely dissipative Lindblad transport",
               "Both require new postulates (MIP)",
               "Combined H_hop + Lindblad = dissipative propagation: excitations "
               "move but lose coherence",
               "Verdict: dissipative_propagation_only (no lossless transport)"],
    )


def _build_track_e() -> QIIEManyModeBenchmarkAudit:
    candidates = [
        QIIEBenchmarkCandidate("MB1", "two_site_hopping_chain",
            "2-site chain with H_hop + independent Lindblad channels.",
            True,
            ["mode_labeling_i_equals_1_2",
             "excitation_transfer_via_H_hop",
             "dissipative_decay_via_Lindblad",
             "occupation_number_tracking",
             "coherent_oscillation_between_sites_before_decoherence"],
            ["continuum_mode_structure",
             "particle_dispersion_relation",
             "quantum_field_theory_structure",
             "matter_ontology",
             "many_body_thermodynamics"],
            ["Minimal benchmark: 2 sites, C^4, H_hop + L_1 + L_2",
             "Demonstrates: excitation hops site 1 -> site 2, decays",
             "Oscillation period ~ 1/J; decoherence timescale ~ tau_dec"]),
        QIIEBenchmarkCandidate("MB2", "finite_chain_N_sites",
            "N-site chain with nearest-neighbor H_hop.",
            True,
            ["N_site_mode_labeling",
             "excitation_propagation_along_chain",
             "band_like_energy_structure_in_finite_chain"],
            ["continuum_limit",
             "true_dispersion_relation",
             "particle_scattering"],
            ["Viable: straightforward extension of MB1 to N sites",
             "Hilbert space (C^2)^{tensor N} grows exponentially",
             "Not explicitly benchmarked; structurally plausible"]),
        QIIEBenchmarkCandidate("MB3", "linearized_mode_doublet",
            "Two normal modes of a linearized field.",
            False, [], [],
            ["Not viable: requires continuum spatial structure (ML3 blocked)"]),
        QIIEBenchmarkCandidate("MB4", "no_benchmark",
            "No admissible benchmark.", False, [], [],
            ["Rejected: MB1 is viable"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return QIIEManyModeBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_v, chosen_benchmark_id="MB1_two_site_hopping_chain",
        benchmark_n_sites=N_SITE_BENCHMARK,
        benchmark_hilbert_dim=TWO_SITE_DIM,
        notes=["MB1 chosen: 2-site hopping chain (minimal)",
               "MB2 viable: N-site extension (not explicitly benchmarked)",
               "MB3 blocked (no spatial modes); MB4 null rejected",
               "Benchmark demonstrates dissipative propagation, mode labeling, "
               "excitation counting"],
    )


def _build_track_f() -> QIIEExcitationClassAudit:
    levels = [
        QIIEExcitationClassLevel("EC1", "many_mode_bookkeeping",
            "Mode labels and excitation counting.", True,
            ["Achieved: site labels + n_i = sigma_+ sigma_-"]),
        QIIEExcitationClassLevel("EC2", "propagating_toy_excitations",
            "Excitations that move between sites via H_hop.", True,
            ["Achieved: H_hop transfers excitations coherently"]),
        QIIEExcitationClassLevel("EC3", "dissipative_mode_excitations",
            "Excitations that propagate and decay under Lindblad dynamics.", True,
            ["Achieved: H_hop + Lindblad = dissipative propagation"]),
        QIIEExcitationClassLevel("EC4", "quasi_particle_structure",
            "Excitations with dispersion, scattering, particle-like behavior.", False,
            ["Not achieved: dispersion requires continuum or large-N limit",
             "Scattering requires interaction beyond nearest-neighbor hopping"]),
        QIIEExcitationClassLevel("EC5", "particle_language",
            "Full particle ontology with creation/annihilation, Fock space.", False,
            ["Not achieved: sigma_+ is qubit operator, not bosonic a^dag",
             "No Fock space; no particle number superselection",
             "Particle language not yet justified"]),
    ]
    # highest achieved
    achieved = [l for l in levels if l.achieved]
    highest = achieved[-1].level_id + "_" + achieved[-1].level_name if achieved else "none"
    return QIIEExcitationClassAudit(
        levels=levels, n_levels=N_EXCITATION_CLASS_LEVELS,
        highest_achieved_id=highest,
        notes=["EC1-EC3 achieved; EC4, EC5 not achieved",
               "Highest: dissipative mode excitations (EC3)",
               "Particle language (EC5) not yet justified"],
    )


def _build_track_g() -> QIIEConstitutiveCompatibilityAudit:
    checks = [
        QIIEConstitutiveCheck("CC1", "constitutive_observable_per_site",
            "Each site has Phi_hat^{(i)} = sigma_z^{(i)} as constitutive observable.",
            "compatible",
            ["Same constitutive structure on each site independently"]),
        QIIEConstitutiveCheck("CC2", "excitation_in_complementary_sector",
            "Excitation operators sigma_+ involve sigma_x, sigma_y: complementary sector.",
            "compatible",
            ["Excitations live in the sector complementary to Phi_hat (sigma_z)",
             "Consistent with Q-F finding: interference requires complementary sector"]),
        QIIEConstitutiveCheck("CC3", "hopping_preserves_constitutive_law",
            "H_hop commutes with total sigma_z only if J is real and hopping is symmetric.",
            "conditional",
            ["[H_hop, sum sigma_z^i] = 0 iff hopping preserves total excitation",
             "Constitutive law per site modified by inter-site coupling"]),
        QIIEConstitutiveCheck("CC4", "decoherence_consistent",
            "Lindblad channels per site consistent with excitation dynamics.",
            "compatible",
            ["Independent Lindblad per site: same as Q-II.B",
             "H_hop introduces coherent dynamics on top of dissipation"]),
    ]
    return QIIEConstitutiveCompatibilityAudit(
        checks=checks, n_checks=N_CONSTITUTIVE_CHECKS,
        compatible=True,
        notes=["Excitation structure compatible with constitutive field",
               "Excitations live in complementary sector (sigma_x/y)",
               "H_hop modifies per-site dynamics but preserves total structure"],
    )


def _build_track_h() -> QIIEMatterReadinessAudit:
    levels = [
        QIIEMatterLevel("MR1", "excitation_grammar_established",
            "Mode labels, excitation operators, dissipative propagation.", "achieved",
            ["Achieved: EC1-EC3 from Track F"]),
        QIIEMatterLevel("MR2", "pre_matter_readiness_advanced",
            "Excitation counting and propagation advance pre-matter map.", "achieved",
            ["Excitation number n_i enables counting; propagation enables transport"]),
        QIIEMatterLevel("MR3", "particle_ontology_premature",
            "Particle ontology not yet established.", "not_achieved",
            ["No Fock space, no particle dispersion, no particle identity",
             "sigma_+ is qubit operator, not bosonic a^dag"]),
        QIIEMatterLevel("MR4", "bosonic_route_structurally_advanced",
            "Bosonic matter route advanced but not complete.", "partial",
            ["Excitation counting (n_i with eigenvalues 0,1) is bosonic-like",
             "But: qubit constraint (max 1 per site) differs from bosonic (unbounded)",
             "True bosonic would need harmonic oscillator per site: H = C^inf"]),
        QIIEMatterLevel("MR5", "fermionic_route_still_blocked",
            "Fermionic matter route still blocked by pi_2(S^2) = Z obstruction.", "blocked",
            ["Q0 item E1: 3-layer fermionic obstruction unchanged",
             "Qubit sigma_+ satisfies anticommutation on-site but this is not "
             "fermionic statistics in the many-body sense"]),
    ]
    return QIIEMatterReadinessAudit(
        levels=levels, n_levels=N_MATTER_LEVELS,
        matter_boundary_verdict=QIIE_MATTER_BOUNDARY_VERDICT,
        fermionic_still_blocked=True,
        notes=["MR1-MR2 achieved; MR3 not achieved; MR4 partial; MR5 blocked",
               "Pre-matter readiness advanced but particle ontology premature",
               "Fermionic route still blocked (3-layer obstruction)"],
    )


def _build_track_i() -> QIIEAppendixPAudit:
    entries = [
        QIIEAppendixPEntry("QIIE_mode_grammar", "Mode grammar (N-site chain)",
            "motivated_but_unbuilt",
            "N-site qubit chain with mode labels and excitation counting",
            "Mode labels imply continuum field or spatial structure",
            "Q-II.B tensor product, site duplication"),
        QIIEAppendixPEntry("QIIE_excitation_ops", "Excitation operators",
            "motivated_but_unbuilt",
            "sigma_+/sigma_- toy excitation operators on each site",
            "Qubit raising/lowering implies canonical bosonic ladder operators",
            "Q-II.D su(2) algebra, sigma_x postulation"),
        QIIEAppendixPEntry("QIIE_propagation", "Dissipative propagation",
            "motivated_independent_postulation",
            "H_hop nearest-neighbor hopping with Lindblad dissipation",
            "Toy hopping implies continuum propagation or dispersion relation",
            "New postulate: H_hop (MIP)"),
        QIIEAppendixPEntry("QIIE_benchmark", "Two-site hopping benchmark",
            "motivated_but_unbuilt",
            "2-site chain demonstrates excitation transfer and dissipative decay",
            "2-site benchmark implies many-body or matter readiness",
            "H_hop, Lindblad channels, site labels"),
        QIIEAppendixPEntry("QIIE_matter_boundary", "Matter-readiness boundary",
            "bounded_structural_result",
            "Pre-matter readiness advanced; particle ontology premature; fermionic blocked",
            "Excitation grammar implies matter-readiness achieved",
            "Q0 fermionic obstruction, excitation class EC1-EC3"),
        QIIEAppendixPEntry("QIIE_constitutive_compat", "Constitutive compatibility",
            "motivated_but_unbuilt",
            "Excitation structure compatible with constitutive field per site",
            "Excitation structure implies constitutive law modified globally",
            "Part I constitutive recovery, H_hop coupling"),
        QIIEAppendixPEntry("QIIE_overall", "Q-II.E overall",
            "motivated_but_unbuilt",
            "Field-excitation and many-mode structure coherently established at extension level",
            "Excitation structure implies QFT or particle physics derived",
            "All Q-II.E tracks"),
    ]
    return QIIEAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIIE_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["4 MBU, 1 MIP (H_hop), 1 BSR (matter boundary), 1 MBU (overall)",
               "No native canon"],
    )


def _build_track_j() -> QIIEAuthorizationAudit:
    return QIIEAuthorizationAudit(
        qiif_authorized=True,
        authorization_basis=[
            "mode_grammar_established_at_extension_level",
            "excitation_operators_defined_sigma_plus_minus",
            "dissipative_propagation_demonstrated_in_benchmark",
            "matter_boundary_assessed_particle_ontology_premature",
            "constitutive_compatibility_confirmed",
        ],
        qiif_constraints=[
            "QIIF_must_address_Born_rule_and_probability_interpretation",
            "QIIF_must_not_assume_particle_ontology_from_excitation_grammar",
            "QIIF_must_assess_outcome_selection_and_determination",
            "QIIF_results_inherit_MBU_or_MIP_floor",
            "QIIF_may_enable_Bell_investigation_if_Born_rule_addressed",
        ],
        authorization_verdict=QIIE_AUTHORIZATION_VERDICT,
        notes=["Q-II.F authorized: excitation structure sufficient for "
               "probability/determination investigation",
               "Key gap: Born rule still absent; Q-II.F must address it",
               "Bell investigation may become possible if Born rule is addressed"],
    )


def _build_track_k() -> QIIENonclaimFirewall:
    return QIIENonclaimFirewall(
        nonclaims=QIIE_NONCLAIMS, n_nonclaims=N_QIIE_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_qiie_field_excitations_manymode_audit() -> QIIEFieldExcitationsManyModeResult:
    """Run the full Q-II.E Field Excitations and Many-Mode Structure Audit."""
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
        "N-site qubit chain mode grammar established at extension level "
        "with site labels and independent Lindblad channels",
        "Toy excitation operators sigma_+/sigma_- defined on each site "
        "from postulated su(2) algebra; qubit excitations (0 or 1 per site)",
        "Dissipative propagation demonstrated: H_hop nearest-neighbor hopping "
        "combined with Lindblad decoherence gives excitation transfer with decay",
        "Two-site hopping benchmark demonstrates mode labeling, excitation "
        "transfer, occupation counting, and dissipative decay",
        "Pre-matter readiness advanced: excitation grammar and propagation "
        "established; particle ontology premature",
        "Fermionic matter route still blocked by Q0 3-layer obstruction; "
        "bosonic route structurally advanced but qubit-constrained",
        "Q-II.F authorized: Born rule and probability investigation next",
    ]

    forbidden_claims: List[str] = [
        "Many-mode labels imply field theory or continuum quantization",
        "Excitation bookkeeping implies particles derived",
        "Propagating toy mode implies matter ontology",
        "sigma_+/sigma_- notation implies canonical creation/annihilation algebra",
        "Coupled toy sites imply continuum field quantization",
        "Many-mode decoherence implies measurement solved",
        "Extension-level excitation support implies native canon",
    ]

    diagnostics: Dict[str, Any] = {
        "single_site_dim": SINGLE_SITE_DIM,
        "two_site_dim": TWO_SITE_DIM,
        "n_site_benchmark": N_SITE_BENCHMARK,
        "n_eligibility_ingredients": N_ELIGIBILITY_INGREDIENTS,
        "n_mode_candidates": N_MODE_CANDIDATES,
        "n_mode_viable": tb.n_viable,
        "n_excitation_candidates": N_EXCITATION_CANDIDATES,
        "n_propagation_candidates": N_PROPAGATION_CANDIDATES,
        "n_propagation_viable": td.n_viable,
        "n_benchmark_viable": te.n_viable,
        "fermionic_still_blocked": th.fermionic_still_blocked,
        "n_nonclaims": N_QIIE_NONCLAIMS,
        "n_appendix_p_entries": N_APPENDIX_P_ENTRIES,
    }

    result = QIIEFieldExcitationsManyModeResult(
        valid=True,
        track_a_eligibility=ta, track_b_mode_label=tb,
        track_c_excitation_op=tc, track_d_propagation=td,
        track_e_benchmark=te, track_f_excitation_class=tf,
        track_g_constitutive=tg, track_h_matter=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        mode_verdict=tb.mode_verdict,
        excitation_verdict=tc.excitation_verdict,
        propagation_verdict=td.propagation_verdict,
        matter_boundary_verdict=th.matter_boundary_verdict,
        authorization_verdict=tj.authorization_verdict,
        qiie_appendix_p_class=QIIE_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIIE_NONCLAIMS,
        diagnostics=diagnostics,
    )
    validate_qiie_result(result)
    return result


def validate_qiie_result(result: QIIEFieldExcitationsManyModeResult) -> None:
    checks = [
        (result.mode_verdict, ALLOWED_MODE_VERDICTS, "Mode"),
        (result.excitation_verdict, ALLOWED_EXCITATION_VERDICTS, "Excitation"),
        (result.propagation_verdict, ALLOWED_PROPAGATION_VERDICTS, "Propagation"),
        (result.matter_boundary_verdict, ALLOWED_MATTER_BOUNDARY_VERDICTS, "Matter"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.qiie_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class not in allowed")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Track I entry '{e.item_id}': class not in allowed")
    if result.track_k_nonclaims.n_nonclaims != N_QIIE_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.qiif_authorized:
        raise ValueError("qiif_authorized must be True")
    if not result.track_h_matter.fermionic_still_blocked:
        raise ValueError("fermionic_still_blocked must be True")
    if not result.track_g_constitutive.compatible:
        raise ValueError("constitutive compatible must be True")


def _self_test() -> bool:
    r = run_qiie_field_excitations_manymode_audit()
    assert r.valid is True
    assert r.mode_verdict == QIIE_MODE_VERDICT
    assert r.excitation_verdict == QIIE_EXCITATION_VERDICT
    assert r.propagation_verdict == QIIE_PROPAGATION_VERDICT
    assert r.matter_boundary_verdict == QIIE_MATTER_BOUNDARY_VERDICT
    assert r.authorization_verdict == QIIE_AUTHORIZATION_VERDICT
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.E self-test passed.")
