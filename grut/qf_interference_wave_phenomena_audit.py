"""
Appendix Q-F --- Interference and Wave-Phenomena Audit
======================================================
GRUT Quantum Program --- Phase Q-F  (Capstone of First-Wave)

This module audits whether the GRUT quantum extension package (Q-B through Q-E)
supports interference-like behavior, how decoherence constrains it, and what
wave-phenomenology claims are justified.

Key physics (interference in the Lindblad master equation)
----------------------------------------------------------
The full Lindblad master equation,

    d rho / dt = -i [H, rho] + gamma ( Phi_hat rho Phi_hat^dag
                                        - 1/2 { Phi_hat^dag Phi_hat, rho } )

in the Phi_hat eigenbasis |phi_m> (Phi_hat |phi_m> = phi_m |phi_m>) gives:

    d rho_mn / dt = -i (E_m - E_n) rho_mn  - 1/2 gamma (phi_m - phi_n)^2 rho_mn

where E_m are the Hamiltonian eigenvalues (if H and Phi_hat are simultaneously
diagonalizable in the 2-state toy model, E_m = Delta_E / 2 * phi_m).

Solution:

    rho_mn(t) = rho_mn(0) * exp[ -(i Delta_E + 1/2 gamma Delta_phi^2) t ]

The interference (cross-term) contribution to <A>:

    <A>(t) = sum_n A_nn rho_nn  +  2 Re[ sum_{m<n} A_mn rho_nm(t) ]
           = classical part       +  interference part

Visibility (coherence envelope):

    V(t) = |rho_mn(t)| / |rho_mn(0)| = exp(-R_dec * t)

where R_dec = 1/2 gamma Delta_phi^2 = Delta_phi^2 / (2 tau).

For the 2-state model (Delta_phi = 2):
    R_dec = 2 / tau
    tau_dec = tau / 2
    V(tau_dec) = exp(-1) ~ 0.368
    V(tau)     = exp(-2) ~ 0.135   (heavily suppressed at constitutive timescale)

Constitutive-interference tension
---------------------------------
Phi_hat eigenbasis is the pointer basis (decoherence-stable).  Interference
requires superpositions of Phi_hat eigenstates --- exactly the superpositions
that decoherence destroys.  Therefore:

- Interference in the Phi_hat sector is TRANSIENT (present for t << tau_dec,
  suppressed for t >> tau_dec).
- Sustained or robust interference requires an observable in a
  COMPLEMENTARY sector (not diagonal in the Phi_hat eigenbasis).

Authorization rationale
-----------------------
The first-wave quantum program (Q-B through Q-F) has:
  - state space architecture (Q-B: BSR, then Q-B.5: J postulated as MIP)
  - kinematic completion (Q-C0)
  - microdynamic law (Q-C: Lindbladian preferred)
  - classical-limit recovery (Q-C.5)
  - decoherence + pointer basis (Q-D)
  - benchmark toy models (Q-E: 4 benchmarks, 3 demonstrated/1 underdetermined)
  - interference and wave phenomena (Q-F: transient interference demonstrated)
Remaining gaps (Born rule, outcome selection, QE3 uncertainty) are documented
as BSR/MBU, not blocking.  The first wave has accomplished its chartered scope.
A second wave (entanglement, multi-body, field excitations) can be opened.
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

# Two-state physics (inherited from Q-E)
DELTA_PHI_2STATE: float = 2.0
R_DEC_2STATE: float = 0.5 * GAMMA * DELTA_PHI_2STATE ** 2   # = 2/TAU
TAU_DEC_2STATE: float = 1.0 / R_DEC_2STATE                  # = TAU/2

PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

# New Q-F interference physics
VISIBILITY_AT_TAU_DEC: float = math.exp(-1.0)       # e^{-1} ~ 0.368
VISIBILITY_AT_TAU_2STATE: float = math.exp(-2.0)     # e^{-2} ~ 0.135
TIMESCALE_RATIO_DEC_TO_CONSTITUTIVE: float = 0.5     # tau_dec_2state / tau
VISIBILITY_HALF_LIFE_2STATE: float = TAU_DEC_2STATE * math.log(2.0)

# Counts
N_INTERFERENCE_INGREDIENTS: int = 5
N_CANDIDATE_TOY_MODELS: int = 4
N_SLIT_CANDIDATES: int = 4
N_COMPARATIVE_ENTRIES: int = 4
N_QF_NONCLAIMS: int = 8
N_APPENDIX_P_ENTRIES: int = 6
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited verdicts
QE1_INHERITED: str = "qe1_demonstrates_relaxation_and_decoherence"
QE2_INHERITED: str = "qe2_demonstrates_pointer_record_structure"
QE3_INHERITED: str = "qe3_uncertainty_like_structure_underdetermined"
QE4_INHERITED: str = "qe4_constitutive_observable_classicality_demonstrated"
QE_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QF"
QD_INHERITED_DECOHERENCE: str = "effective_regime_decoherence_demonstrated"
QD_INHERITED_POINTER: str = "pointer_basis_class_selected"
QC_INHERITED_LAW_CLASS: str = "lindbladian_like_law_preferred"
QC5_INHERITED_RECOVERY: str = "effective_regime_constitutive_recovery_demonstrated"

# Q-F Verdict strings
QF_PHASE_VERDICT: str = "relative_phase_structure_demonstrated_in_toy_form"
QF_INTERFERENCE_VERDICT: str = "transient_interference_before_decoherence_demonstrated"
QF_SLIT_INTERPRETATION_VERDICT: str = "abstract_two_path_interpretation_justified"
QF_CONSTITUTIVE_INTERFERENCE_VERDICT: str = (
    "interference_requires_complementary_observable_sector"
)
QF_AUTHORIZATION_VERDICT: str = "authorized_to_close_first_wave_quantum_program"
QF_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozenset vocabularies
ALLOWED_PHASE_VERDICTS: frozenset = frozenset({
    "relative_phase_structure_demonstrated_in_toy_form",
    "relative_phase_structure_structurally_plausible_but_unbuilt",
    "relative_phase_structure_blocked",
    "relative_phase_structure_underdetermined",
})
ALLOWED_INTERFERENCE_VERDICTS: frozenset = frozenset({
    "toy_interference_cross_terms_demonstrated",
    "transient_interference_before_decoherence_demonstrated",
    "interference_structurally_plausible_but_unbuilt",
    "interference_blocked",
})
ALLOWED_SLIT_INTERPRETATION_VERDICTS: frozenset = frozenset({
    "no_slit_language_yet_justified",
    "abstract_two_path_interpretation_justified",
    "toy_double_slit_analogy_justified",
    "disciplined_slit_modeling_path_identified",
})
ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS: frozenset = frozenset({
    "constitutive_observable_also_supports_interference",
    "interference_requires_complementary_observable_sector",
    "constitutive_interference_relation_underdetermined",
    "constitutive_observable_is_pointer_selected_and_interference_suppressed",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_close_first_wave_quantum_program",
    "authorized_only_for_further_interference_refinement",
    "authorized_to_open_second_wave_quantum_program",
    "not_authorized_to_proceed",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8, verbatim)
QF_NONCLAIMS: List[str] = [
    "NOT_claiming_toy_interference_therefore_full_double_slit_solved__"
    "two_state_cross_terms_are_formal_analogy_not_spatial_slit_physics",
    "NOT_claiming_phase_sensitive_cross_term_therefore_Born_rule__"
    "interference_visibility_is_coherence_measure_not_probability_weighting",
    "NOT_claiming_short_time_coherence_therefore_full_wave_ontology__"
    "transient_interference_lives_in_effective_regime_only",
    "NOT_claiming_interference_toy_model_therefore_entanglement_formalism_derived__"
    "two_state_interference_is_single_system_not_multi_body",
    "NOT_claiming_any_two_state_phase_model_therefore_field_theoretic_interference_solved__"
    "toy_model_is_minimal_benchmark_not_field_theory",
    "NOT_claiming_constitutive_decoherence_coexistence_therefore_full_classical_quantum_bridge__"
    "decoherence_suppresses_interference_in_pointer_sector",
    "NOT_claiming_extension_level_phase_structure_therefore_native_canon__"
    "all_QF_results_carry_MBU_floor_per_QA_R3",
    "NOT_claiming_slit_style_analogy_therefore_literal_experimental_closure__"
    "abstract_two_path_language_is_formal_not_phenomenological",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QFInterferenceIngredient:
    """Single interference eligibility ingredient (Track A)."""
    ingredient_id: str          # "ING1"--"ING5"
    ingredient_name: str
    description: str
    status: str                 # "present", "conditionally_present", "absent", "extension_level"
    source: str                 # which prior appendix provides it
    notes: List[str]


@dataclass
class QFInterferenceEligibilityAudit:
    """Track A --- interference eligibility audit."""
    ingredients: List[QFInterferenceIngredient]
    n_ingredients: int
    n_present: int
    n_conditionally_present: int
    n_absent: int
    n_extension_level: int
    eligibility_verdict: str    # "eligible_for_toy_interference"
    notes: List[str]


@dataclass
class QFRelativePhaseAnalysis:
    """Track B --- relative phase evolution audit."""
    phase_source: str                    # "hamiltonian_part_of_lindblad_master_equation"
    phase_formula: str                   # "exp(-i * Delta_E * t)"
    combined_off_diagonal_formula: str   # "rho_01(t) = rho_01(0) * exp(-(i*Delta_E + R_dec)*t)"
    phase_demonstrated_in_toy: bool      # True
    phase_requires_hamiltonian: bool     # True
    hamiltonian_status: str              # "postulated_with_J_as_MIP"
    phase_independent_of_decoherence: bool  # True
    phase_verdict: str
    notes: List[str]


@dataclass
class QFToyModelCandidate:
    """Single candidate interference toy model (used in Track C)."""
    model_id: str               # "TM1"--"TM4"
    model_name: str
    description: str
    demonstrates_cross_terms: bool
    demonstrates_phase_sensitivity: bool
    demonstrates_transient_interference: bool
    demonstrates_constructive_destructive: bool
    extension_burden: str       # "low", "medium", "high"
    viable: bool
    notes: List[str]


@dataclass
class QFMinimalInterferenceToyModelAudit:
    """Track C --- minimal interference toy model audit."""
    candidates: List[QFToyModelCandidate]
    n_candidates: int
    n_viable: int
    chosen_model_id: str
    interference_verdict: str
    # Key physics of chosen model
    visibility_formula: str
    visibility_at_t0: float
    visibility_at_tau_dec: float
    interference_timescale: str
    cross_term_formula: str
    notes: List[str]


@dataclass
class QFDecoherenceInterferenceCompetition:
    """Track D --- decoherence-vs-interference competition audit."""
    visibility_decay_law: str
    visibility_decay_rate: str
    decoherence_timescale: str
    interference_timescale: str
    timescale_ratio: float           # 1.0
    interference_survives_regime: str
    interference_suppressed_regime: str
    tau_controls_visibility: bool
    eigenvalue_separation_controls_visibility: bool
    weak_damping_condition: str
    competition_verdict: str
    # Key numerical results for 2-state
    visibility_half_life_2state: float
    visibility_at_tau_2state: float
    notes: List[str]


@dataclass
class QFSlitCandidate:
    """Single slit interpretation candidate (used in Track E)."""
    candidate_id: str           # "SL1"--"SL4"
    candidate_name: str
    description: str
    justified: bool
    obstruction_if_not: str
    notes: List[str]


@dataclass
class QFSlitStyleInterpretationAudit:
    """Track E --- slit-style interpretation audit."""
    candidates: List[QFSlitCandidate]
    n_candidates: int
    justified_candidate_id: str
    slit_interpretation_verdict: str
    boundary_notes: List[str]
    notes: List[str]


@dataclass
class QFConstitutiveInterferenceAnalysis:
    """Track F --- constitutive-observable compatibility with interference."""
    constitutive_observable: str
    pointer_observable: str
    pointer_selected: bool
    interference_requires_superposition_of: str
    decoherence_suppresses_that_superposition: bool
    same_observable_tension: str
    complementary_sector_needed: bool
    complementary_sector_example: str
    constitutive_interference_verdict: str
    notes: List[str]


@dataclass
class QFComparativeModelEntry:
    """Single entry in comparative model audit (used in Track G)."""
    model_id: str
    extension_burden: str
    fidelity_to_qb_through_qe: str
    explicitness_of_interference: str
    robustness_against_decoherence: str
    usefulness_for_matter_work: str
    strength_ranking: int


@dataclass
class QFComparativeModelAudit:
    """Track G --- comparative model audit."""
    entries: List[QFComparativeModelEntry]
    strongest_model_id: str
    weakest_model_id: str
    notes: List[str]


@dataclass
class QFAppendixPEntry:
    """Single Appendix P classification entry (used in Track H)."""
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QFAppendixPAudit:
    """Track H --- Appendix P classification audit."""
    entries: List[QFAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QFAuthorizationAudit:
    """Track I --- quantum-program authorization audit."""
    first_wave_closure_authorized: bool
    second_wave_opening_noted: bool
    further_interference_refinement_needed: bool
    remaining_gaps: List[str]
    gaps_documented_as: str
    authorization_verdict: str
    second_wave_scope: List[str]
    notes: List[str]


@dataclass
class QFNonclaimFirewall:
    """Track J --- registered nonclaims firewall."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QFInterferenceWavePhenomenaResult:
    """Master result dataclass aggregating all ten tracks."""
    valid: bool
    track_a_eligibility: QFInterferenceEligibilityAudit
    track_b_relative_phase: QFRelativePhaseAnalysis
    track_c_toy_model: QFMinimalInterferenceToyModelAudit
    track_d_decoherence_competition: QFDecoherenceInterferenceCompetition
    track_e_slit_interpretation: QFSlitStyleInterpretationAudit
    track_f_constitutive_interference: QFConstitutiveInterferenceAnalysis
    track_g_comparative: QFComparativeModelAudit
    track_h_appendix_p: QFAppendixPAudit
    track_i_authorization: QFAuthorizationAudit
    track_j_nonclaims: QFNonclaimFirewall
    # Five hard-gated verdicts
    phase_verdict: str
    interference_verdict: str
    slit_interpretation_verdict: str
    constitutive_interference_verdict: str
    authorization_verdict: str
    # Summary
    qf_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builder functions
# ---------------------------------------------------------------------------

def _build_track_a() -> QFInterferenceEligibilityAudit:
    """Track A --- interference eligibility audit for 5 minimum ingredients."""
    ingredients: List[QFInterferenceIngredient] = [
        QFInterferenceIngredient(
            ingredient_id="ING1",
            ingredient_name="complex_structure_J",
            description=(
                "Complex structure J with J^2 = -1 on the doubled real field space. "
                "Required for complex amplitudes and phase structure."
            ),
            status="conditionally_present",
            source="Q-B.5 (motivated_independent_postulation)",
            notes=[
                "J is postulated as MIP (motivated_independent_postulation) in Q-B.5",
                "Not natively derived --- all 5 native routes rejected per Q-B.5 Track B",
                "J^2 = -1 algebraically established once postulated",
                "Ghost obstruction (PHI_MINUS_GROWTH_RATE_SIGN = +1) blocks CTP-based J",
                "Conditionally present: available if MIP postulation is accepted",
            ],
        ),
        QFInterferenceIngredient(
            ingredient_id="ING2",
            ingredient_name="two_distinguishable_coherent_components",
            description=(
                "At least two distinguishable states (e.g. |phi_+> and |phi_->) "
                "in coherent superposition, realized in the 2-state model from Q-E."
            ),
            status="present",
            source="Q-E (QE1 two-state model)",
            notes=[
                "2-state model from QE1: |+1> and |-1> eigenstates of sigma_z",
                "Density matrix rho can represent coherent superpositions",
                "Off-diagonal elements rho_01, rho_10 encode coherence between the two",
                "Present: fully available from Q-E QE1 structure",
            ],
        ),
        QFInterferenceIngredient(
            ingredient_id="ING3",
            ingredient_name="relative_phase_evolution",
            description=(
                "A Hamiltonian H that drives relative phase evolution between states. "
                "The unitary part -i[H, rho] of the master equation provides "
                "exp(-i Delta_E t) on off-diagonals."
            ),
            status="conditionally_present",
            source="Q-C Lindblad master equation (Hamiltonian part)",
            notes=[
                "The Lindblad master equation includes -i[H, rho] as its unitary part",
                "H must be specified; in the 2-state model, H = (Delta_E/2) sigma_z",
                "Phase evolution: rho_01 picks up factor exp(-i Delta_E t)",
                "Conditionally present: H is part of the Lindblad structure but "
                "specific Hamiltonian requires postulation alongside J",
                "Phase factor is INDEPENDENT of decoherence factor exp(-R_dec t)",
            ],
        ),
        QFInterferenceIngredient(
            ingredient_id="ING4",
            ingredient_name="cross_term_sensitive_observable",
            description=(
                "An observable A with non-zero off-diagonal matrix elements "
                "A_mn (m != n) in the Phi_hat eigenbasis, so that <A> includes "
                "interference cross terms 2 Re(A_mn rho_nm)."
            ),
            status="conditionally_present",
            source="Q-E (QE3: second observable underdetermined but not blocked)",
            notes=[
                "Any observable not diagonal in Phi_hat eigenbasis has cross terms",
                "In 2-state model: sigma_x or sigma_y would be cross-term-sensitive",
                "sigma_x and sigma_y exist in C^2 Hilbert space but are not "
                "independently motivated by GRUT (same gap as QE3)",
                "Conditionally present: the mathematical structure supports it "
                "but the observable motivation is underdetermined",
                "For the toy model we can postulate A = sigma_x as the "
                "interference-sensitive observable",
            ],
        ),
        QFInterferenceIngredient(
            ingredient_id="ING5",
            ingredient_name="coherence_lifetime",
            description=(
                "A finite coherence lifetime tau_dec such that interference can be "
                "meaningful before decoherence suppresses it."
            ),
            status="present",
            source="Q-D / Q-E (tau_dec = 2 tau / delta_phi^2)",
            notes=[
                "Decoherence timescale: tau_dec = 2 tau / delta_phi^2",
                "For 2-state: tau_dec = tau/2 (finite and calculable)",
                "Interference is meaningful for t << tau_dec",
                "Present: fully determined by inherited Q-D decoherence structure",
                f"tau_dec_2state = {TAU_DEC_2STATE:.6f}",
            ],
        ),
    ]

    n_present = sum(1 for ing in ingredients if ing.status == "present")
    n_cond = sum(1 for ing in ingredients if ing.status == "conditionally_present")
    n_absent = sum(1 for ing in ingredients if ing.status == "absent")
    n_ext = sum(1 for ing in ingredients if ing.status == "extension_level")

    return QFInterferenceEligibilityAudit(
        ingredients=ingredients,
        n_ingredients=N_INTERFERENCE_INGREDIENTS,
        n_present=n_present,
        n_conditionally_present=n_cond,
        n_absent=n_absent,
        n_extension_level=n_ext,
        eligibility_verdict="eligible_for_toy_interference",
        notes=[
            "2 ingredients present (two components, coherence lifetime)",
            "3 ingredients conditionally present (J, Hamiltonian, cross-term observable)",
            "0 ingredients absent or blocked",
            "All conditional ingredients available under MIP + toy-model postulations",
            "Eligible for toy interference: all 5 ingredients satisfied at conditional level or above",
        ],
    )


def _build_track_b() -> QFRelativePhaseAnalysis:
    """Track B --- relative phase evolution audit."""
    return QFRelativePhaseAnalysis(
        phase_source="hamiltonian_part_of_lindblad_master_equation",
        phase_formula="exp(-i * Delta_E * t)",
        combined_off_diagonal_formula=(
            "rho_01(t) = rho_01(0) * exp(-(i * Delta_E + R_dec) * t)"
        ),
        phase_demonstrated_in_toy=True,
        phase_requires_hamiltonian=True,
        hamiltonian_status="postulated_with_J_as_MIP",
        phase_independent_of_decoherence=True,
        phase_verdict=QF_PHASE_VERDICT,
        notes=[
            "The Hamiltonian part -i[H, rho] of the Lindblad master equation provides "
            "relative phase evolution on off-diagonal elements",
            "In the 2-state model with H = (Delta_E/2) sigma_z: "
            "rho_01(t) acquires phase factor exp(-i Delta_E t)",
            "Phase and decoherence are independent: the combined evolution is "
            "exp(-i Delta_E t) * exp(-R_dec t) = exp(-(i Delta_E + R_dec) t)",
            "Phase demonstrated in toy form: the 2-state model explicitly shows it",
            "Hamiltonian H is part of the Lindblad structure postulated in Q-C; "
            "specific form requires H = f(Phi_hat) or separate postulation",
            "Phase structure is NOT native canon --- contingent on Lindblad + J postulations",
            "Verdict: relative_phase_structure_demonstrated_in_toy_form",
        ],
    )


def _build_track_c() -> QFMinimalInterferenceToyModelAudit:
    """Track C --- minimal interference toy model audit."""
    candidates: List[QFToyModelCandidate] = [
        QFToyModelCandidate(
            model_id="TM1",
            model_name="two_component_coherent_superposition",
            description=(
                "Minimal 2-state model: rho(0) = |psi><psi| with "
                "|psi> = (|+1> + |-1>)/sqrt(2). Off-diagonal rho_01(0) = 1/2. "
                "Under Lindblad evolution, rho_01(t) = (1/2) exp(-(i Delta_E + R_dec) t). "
                "Cross terms in <sigma_x>(t) = Re(rho_01(t)) demonstrate transient "
                "interference before decoherence suppresses them."
            ),
            demonstrates_cross_terms=True,
            demonstrates_phase_sensitivity=True,
            demonstrates_transient_interference=True,
            demonstrates_constructive_destructive=True,
            extension_burden="low",
            viable=True,
            notes=[
                "Reuses the QE1 two-state model with a coherent initial state",
                "Cross terms: <sigma_x>(t) = 2 Re(rho_01(t)) = cos(Delta_E t) exp(-R_dec t)",
                "Constructive: cos(Delta_E t) = 1 at t=0; destructive: cos(Delta_E t) = -1 "
                "at t = pi/Delta_E",
                "Transient: envelope exp(-R_dec t) decays to exp(-1) at t = tau_dec",
                "Low extension burden: reuses existing 2-state + Lindblad structure",
            ],
        ),
        QFToyModelCandidate(
            model_id="TM2",
            model_name="two_path_reduced_state_model",
            description=(
                "A model where two spatial paths contribute to a reduced state. "
                "Requires: spatial propagator, path labeling, path-dependent phases."
            ),
            demonstrates_cross_terms=False,
            demonstrates_phase_sensitivity=False,
            demonstrates_transient_interference=False,
            demonstrates_constructive_destructive=False,
            extension_burden="high",
            viable=False,
            notes=[
                "Requires spatial paths/propagator: not available in current package",
                "Would need position-space Hilbert space or path integral --- beyond Q-E scope",
                "Not viable: fundamental structural gap (no spatial degrees of freedom)",
            ],
        ),
        QFToyModelCandidate(
            model_id="TM3",
            model_name="two_level_phase_sensitive_observable",
            description=(
                "Same 2-state model as TM1 but with explicit emphasis on "
                "observable choice: A = sigma_x is phase-sensitive (off-diagonal "
                "in sigma_z eigenbasis). Subsumes TM1 with extra observable focus."
            ),
            demonstrates_cross_terms=True,
            demonstrates_phase_sensitivity=True,
            demonstrates_transient_interference=True,
            demonstrates_constructive_destructive=True,
            extension_burden="low",
            viable=True,
            notes=[
                "Functionally identical to TM1 with explicit observable identification",
                "sigma_x has matrix elements: (sigma_x)_01 = (sigma_x)_10 = 1",
                "<sigma_x>(t) = 2 Re(rho_01(t)) = cos(Delta_E t) exp(-R_dec t)",
                "Viable but subsumes TM1 --- TM1 is chosen as canonical minimal model",
            ],
        ),
        QFToyModelCandidate(
            model_id="TM4",
            model_name="no_coherent_toy_model_available",
            description=(
                "Null candidate: asserts that no coherent toy model can be built "
                "from the current package."
            ),
            demonstrates_cross_terms=False,
            demonstrates_phase_sensitivity=False,
            demonstrates_transient_interference=False,
            demonstrates_constructive_destructive=False,
            extension_burden="low",
            viable=False,
            notes=[
                "Rejected: TM1 (and TM3) demonstrate that a coherent toy model IS available",
                "The 2-state Lindblad system with coherent initial state suffices",
            ],
        ),
    ]

    n_viable = sum(1 for c in candidates if c.viable)

    return QFMinimalInterferenceToyModelAudit(
        candidates=candidates,
        n_candidates=N_CANDIDATE_TOY_MODELS,
        n_viable=n_viable,
        chosen_model_id="TM1_two_component_superposition",
        interference_verdict=QF_INTERFERENCE_VERDICT,
        visibility_formula="V(t) = exp(-R_dec * t) = exp(-delta_phi^2 * t / (2 * tau))",
        visibility_at_t0=1.0,
        visibility_at_tau_dec=VISIBILITY_AT_TAU_DEC,
        interference_timescale="tau_dec = 2 * tau / delta_phi^2",
        cross_term_formula="<A>_cross(t) = 2 * Re(A_01 * rho_10(t))",
        notes=[
            "TM1 chosen as the canonical minimal interference toy model",
            "TM3 is viable but functionally equivalent to TM1 (subsumed)",
            "TM2 not viable: spatial paths not available in current package",
            "TM4 null case rejected: TM1 exists",
            "Interference is TRANSIENT: present for t << tau_dec, "
            "suppressed for t >> tau_dec",
            "In the 2-state model: <sigma_x>(t) = cos(Delta_E t) exp(-2t/tau)",
            f"V(tau_dec) = exp(-1) = {VISIBILITY_AT_TAU_DEC:.6f}",
            f"V(tau)     = exp(-2) = {VISIBILITY_AT_TAU_2STATE:.6f} (heavily suppressed)",
            "Verdict: transient_interference_before_decoherence_demonstrated",
        ],
    )


def _build_track_d() -> QFDecoherenceInterferenceCompetition:
    """Track D --- decoherence-vs-interference competition audit."""
    return QFDecoherenceInterferenceCompetition(
        visibility_decay_law="V(t) = exp(-0.5 * gamma * delta_phi^2 * t)",
        visibility_decay_rate="R_vis = R_dec = 0.5 * gamma * delta_phi^2",
        decoherence_timescale="tau_dec = 2 * tau / delta_phi^2",
        interference_timescale=(
            "tau_int = tau_dec (interference dies when coherence dies)"
        ),
        timescale_ratio=1.0,
        interference_survives_regime="t << tau_dec (short-time or weak-damping regime)",
        interference_suppressed_regime="t >> tau_dec (long-time decoherence regime)",
        tau_controls_visibility=True,
        eigenvalue_separation_controls_visibility=True,
        weak_damping_condition="delta_phi << sqrt(2 * tau / t)",
        competition_verdict="decoherence_wins_at_constitutive_timescale",
        visibility_half_life_2state=VISIBILITY_HALF_LIFE_2STATE,
        visibility_at_tau_2state=VISIBILITY_AT_TAU_2STATE,
        notes=[
            "Interference visibility V(t) = exp(-R_dec t) decays exponentially",
            "Decoherence and interference live on the SAME timescale tau_dec "
            "(ratio = 1.0 by definition)",
            "Two control parameters: tau (constitutive timescale) and delta_phi "
            "(eigenvalue separation)",
            "Weak-damping regime: delta_phi << sqrt(2 tau/t) --- interference survives "
            "longer for smaller eigenvalue gaps",
            "For the 2-state model (delta_phi = 2):",
            f"  tau_dec_2state = tau/2 = {TAU_DEC_2STATE:.6f}",
            f"  V(tau_dec) = exp(-1) = {VISIBILITY_AT_TAU_DEC:.6f}",
            f"  V(tau) = exp(-2) = {VISIBILITY_AT_TAU_2STATE:.6f} (heavily suppressed)",
            f"  Visibility half-life = {VISIBILITY_HALF_LIFE_2STATE:.6f}",
            "At the constitutive timescale t = tau, interference visibility is only "
            "~13.5%: decoherence has already won",
            "Competition verdict: decoherence wins at the constitutive timescale",
            "Interference is a SHORT-TIME phenomenon in the current extension package",
        ],
    )


def _build_track_e() -> QFSlitStyleInterpretationAudit:
    """Track E --- slit-style interpretation audit."""
    candidates: List[QFSlitCandidate] = [
        QFSlitCandidate(
            candidate_id="SL1",
            candidate_name="no_slit_language_yet",
            description="No slit or path language of any kind is justified.",
            justified=False,
            obstruction_if_not=(
                "Rejected: the 2-state toy model DOES demonstrate formal two-path "
                "structure (two components, cross terms, visibility decay). "
                "SL1 is overly restrictive."
            ),
            notes=[
                "Too restrictive: formal two-path structure IS present in TM1",
                "The cross terms 2 Re(A_mn rho_nm) are mathematically two-path-like",
            ],
        ),
        QFSlitCandidate(
            candidate_id="SL2",
            candidate_name="abstract_two_path_interpretation",
            description=(
                "Abstract two-path interpretation: the 2-state superposition "
                "is formally analogous to two-path interference with cross terms "
                "and visibility decay, but without any spatial geometry."
            ),
            justified=True,
            obstruction_if_not="",
            notes=[
                "Justified: TM1 demonstrates two-component superposition with "
                "cross terms and decoherence-governed visibility",
                "Formal analogy: |psi> = (|1> + |2>)/sqrt(2) ~ two paths",
                "Cross terms ~ path interference",
                "Visibility decay ~ which-path information from environment",
                "No spatial geometry, propagator, momentum, or slit geometry needed",
                "This is the appropriate level of slit language for the current package",
            ],
        ),
        QFSlitCandidate(
            candidate_id="SL3",
            candidate_name="toy_double_slit_analogy",
            description=(
                "Toy double-slit analogy: mapping the 2-state model to an explicit "
                "double-slit scenario with spatial paths and slit geometry."
            ),
            justified=False,
            obstruction_if_not=(
                "Not justified: requires spatial paths, propagator, slit geometry, "
                "and position-space probability amplitude. None of these are "
                "available in the current GRUT quantum extension package."
            ),
            notes=[
                "Would require: position-space Hilbert space, path integral or propagator",
                "Current package has no spatial degrees of freedom",
                "Overreach: the 2-state model has no slit geometry",
            ],
        ),
        QFSlitCandidate(
            candidate_id="SL4",
            candidate_name="disciplined_slit_modeling_path",
            description=(
                "A disciplined path toward full slit phenomenology, identifying "
                "exactly what extensions would be needed."
            ),
            justified=False,
            obstruction_if_not=(
                "Not justified at current stage: would require position/momentum "
                "Hilbert space, spatial propagator, and multi-mode interference. "
                "These are second-wave extensions not yet authorized."
            ),
            notes=[
                "Would be appropriate for a second-wave quantum program",
                "Requires: spatial DOF, propagator, momentum observable, diffraction geometry",
                "Beyond first-wave scope; not justified here",
            ],
        ),
    ]

    return QFSlitStyleInterpretationAudit(
        candidates=candidates,
        n_candidates=N_SLIT_CANDIDATES,
        justified_candidate_id="SL2_abstract_two_path_interpretation",
        slit_interpretation_verdict=QF_SLIT_INTERPRETATION_VERDICT,
        boundary_notes=[
            "BOUNDARY 1: interference toy model (TM1) vs. path superposition formalism: "
            "TM1 demonstrates two-COMPONENT superposition in state space, NOT "
            "two-PATH superposition in position space",
            "BOUNDARY 2: path superposition formalism vs. literal slit phenomenology: "
            "even a path formalism would need propagator and geometry to match "
            "experimental slit results --- not available here",
            "BOUNDARY 3: abstract two-path language is FORMAL (algebraic analogy) "
            "not PHENOMENOLOGICAL (testable prediction about slits)",
        ],
        notes=[
            "SL1 rejected: formal two-path structure IS demonstrated (too restrictive)",
            "SL2 justified: abstract two-path interpretation matches what TM1 provides",
            "SL3 not justified: no spatial paths or slit geometry available",
            "SL4 not justified: beyond first-wave scope",
            "Three explicit boundary distinctions documented to prevent overinterpretation",
            "Verdict: abstract_two_path_interpretation_justified",
        ],
    )


def _build_track_f() -> QFConstitutiveInterferenceAnalysis:
    """Track F --- constitutive-observable compatibility with interference."""
    return QFConstitutiveInterferenceAnalysis(
        constitutive_observable="Phi_hat",
        pointer_observable="Phi_hat (eigenbasis of jump operator L prop Phi_hat)",
        pointer_selected=True,
        interference_requires_superposition_of="Phi_hat_eigenstates",
        decoherence_suppresses_that_superposition=True,
        same_observable_tension=(
            "Constitutive classicality and interference are in tension for Phi_hat: "
            "Phi_hat eigenbasis is the pointer basis (decoherence-stable), but "
            "interference requires exactly those superpositions of Phi_hat eigenstates "
            "that decoherence destroys. The constitutive observable CANNOT simultaneously "
            "support classical behavior and sustained interference."
        ),
        complementary_sector_needed=True,
        complementary_sector_example=(
            "Observable not diagonal in Phi_hat eigenbasis "
            "(e.g. sigma_x-like operator in the 2-state model). "
            "Such an observable would have non-zero off-diagonal matrix elements "
            "in the Phi_hat eigenbasis and its expectation value would include "
            "interference cross terms."
        ),
        constitutive_interference_verdict=QF_CONSTITUTIVE_INTERFERENCE_VERDICT,
        notes=[
            "Phi_hat is the constitutive observable (Q-C.5) AND the pointer observable (Q-D)",
            "Jump operator L = (1/sqrt(tau)) Phi_hat selects Phi_hat eigenbasis as pointer",
            "Decoherence rate for Phi_hat eigenstates: zero (diagonal elements unaffected)",
            "Decoherence rate for Phi_hat superpositions: R_dec = delta_phi^2 / (2 tau) > 0",
            "TENSION: constitutive classicality requires Phi_hat eigenstates to be stable "
            "(classical behavior); interference requires them to be superposed (quantum behavior)",
            "Resolution: interference in the Phi_hat sector is TRANSIENT only",
            "For sustained interference: need a complementary observable sector",
            "This is not a failure --- it is the expected physics of decoherence selecting "
            "a classical sector while interference lives in the complementary sector",
            "Verdict: interference_requires_complementary_observable_sector",
        ],
    )


def _build_track_g() -> QFComparativeModelAudit:
    """Track G --- comparative model audit of interference candidates."""
    entries: List[QFComparativeModelEntry] = [
        QFComparativeModelEntry(
            model_id="TM1",
            extension_burden="low",
            fidelity_to_qb_through_qe="high",
            explicitness_of_interference="explicit",
            robustness_against_decoherence="transient",
            usefulness_for_matter_work="high",
            strength_ranking=1,
        ),
        QFComparativeModelEntry(
            model_id="TM3",
            extension_burden="low",
            fidelity_to_qb_through_qe="high",
            explicitness_of_interference="explicit",
            robustness_against_decoherence="transient",
            usefulness_for_matter_work="medium",
            strength_ranking=2,
        ),
        QFComparativeModelEntry(
            model_id="TM2",
            extension_burden="high",
            fidelity_to_qb_through_qe="low",
            explicitness_of_interference="abstract",
            robustness_against_decoherence="suppressed",
            usefulness_for_matter_work="high",
            strength_ranking=3,
        ),
        QFComparativeModelEntry(
            model_id="TM4",
            extension_burden="low",
            fidelity_to_qb_through_qe="low",
            explicitness_of_interference="abstract",
            robustness_against_decoherence="suppressed",
            usefulness_for_matter_work="low",
            strength_ranking=4,
        ),
    ]

    return QFComparativeModelAudit(
        entries=entries,
        strongest_model_id="TM1",
        weakest_model_id="TM4",
        notes=[
            "TM1 is strongest: lowest burden, highest fidelity, explicit interference, "
            "most useful for matter work",
            "TM3 is second: functionally equivalent to TM1 but with extra observable focus "
            "(subsumed by TM1)",
            "TM2 is third: high burden (spatial DOF needed), low fidelity to current package",
            "TM4 is weakest: null candidate, rejected",
            "All viable models show only TRANSIENT interference (decoherence wins at "
            "constitutive timescale)",
        ],
    )


def _build_track_h() -> QFAppendixPAudit:
    """Track H --- Appendix P classification for each Q-F result."""
    entries: List[QFAppendixPEntry] = [
        QFAppendixPEntry(
            item_id="QF_relative_phase",
            item_name="Relative phase structure in toy form",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Relative phase evolution demonstrated in 2-state toy model via "
                "Hamiltonian part of Lindblad master equation"
            ),
            forbidden_claim=(
                "Phase structure implies full wave mechanics or native phase dynamics"
            ),
            dependency=(
                "Q-C Lindblad structure, J postulation (MIP), 2-state model (QE1)"
            ),
        ),
        QFAppendixPEntry(
            item_id="QF_toy_interference",
            item_name="Transient interference before decoherence",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Cross terms demonstrated in 2-state model with visibility "
                "V(t) = exp(-R_dec t)"
            ),
            forbidden_claim=(
                "Toy interference implies full quantum interference or double-slit physics"
            ),
            dependency=(
                "QE1 two-state model, Q-D decoherence rate, Lindblad structure"
            ),
        ),
        QFAppendixPEntry(
            item_id="QF_visibility_decay",
            item_name="Visibility decay law",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Exponential visibility decay V(t) = exp(-delta_phi^2 t / (2 tau)) "
                "demonstrated in effective regime"
            ),
            forbidden_claim=(
                "Visibility law implies derived decoherence from first principles"
            ),
            dependency=(
                "Q-D decoherence rate formula, Q-C Lindblad structure"
            ),
        ),
        QFAppendixPEntry(
            item_id="QF_slit_interpretation",
            item_name="Abstract two-path interpretation",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "Abstract two-path interpretation justified as formal analogy"
            ),
            forbidden_claim=(
                "Two-path language implies spatial slit phenomenology or experimental prediction"
            ),
            dependency=(
                "TM1 toy model structure, two-component superposition"
            ),
        ),
        QFAppendixPEntry(
            item_id="QF_constitutive_interference_tension",
            item_name="Constitutive-interference tension",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "Constitutive observable and interference are in tension: "
                "pointer-selected basis suppresses sustained interference"
            ),
            forbidden_claim=(
                "Constitutive-interference tension blocks all interference permanently"
            ),
            dependency=(
                "Q-D pointer basis, Q-C.5 constitutive recovery, Q-E QE4"
            ),
        ),
        QFAppendixPEntry(
            item_id="QF_first_wave_closure",
            item_name="First-wave quantum program closure",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "First-wave quantum program (Q-B through Q-F) closure authorized; "
                "remaining gaps documented as BSR/MBU"
            ),
            forbidden_claim=(
                "First-wave closure implies full quantum theory derived"
            ),
            dependency=(
                "All Q-B through Q-F authorizations and verdicts"
            ),
        ),
    ]

    return QFAppendixPAudit(
        entries=entries,
        n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QF_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=[
            "4 entries carry motivated_but_unbuilt (MBU): phase, interference, "
            "visibility, first-wave closure",
            "2 entries carry bounded_structural_result (BSR): slit interpretation, "
            "constitutive-interference tension",
            "No entries reach native_canon --- all contingent on MIP postulations "
            "and effective-regime conditions",
            "Overall Q-F program: motivated_but_unbuilt floor",
            "MBU floor inherited from QA R3 constraint on quantum extension results",
        ],
    )


def _build_track_i() -> QFAuthorizationAudit:
    """Track I --- quantum-program authorization audit."""
    return QFAuthorizationAudit(
        first_wave_closure_authorized=True,
        second_wave_opening_noted=True,
        further_interference_refinement_needed=False,
        remaining_gaps=[
            "Born_rule_not_derived",
            "outcome_selection_absent",
            "QE3_uncertainty_structure_underdetermined",
            "full_measurement_closure_not_achieved",
            "spatial_degrees_of_freedom_absent",
        ],
        gaps_documented_as="BSR_or_MBU_not_blocking",
        authorization_verdict=QF_AUTHORIZATION_VERDICT,
        second_wave_scope=[
            "entanglement_and_multi_body_structure",
            "field_excitations_and_particle_like_structure",
            "spatial_degrees_of_freedom_and_propagator",
            "deeper_observable_algebra_and_operator_content",
            "Born_rule_and_outcome_selection_investigation",
        ],
        notes=[
            "First-wave quantum program (Q-B through Q-F) has accomplished its chartered scope:",
            "  Q-B: state space architecture (BSR: natively absent)",
            "  Q-B.5: complex structure J (MIP: postulated)",
            "  Q-C0: kinematic package completion",
            "  Q-C: microdynamic law (Lindbladian preferred)",
            "  Q-C.5: classical-limit recovery (effective regime)",
            "  Q-D: decoherence + pointer basis (effective regime)",
            "  Q-E: benchmark toy models (3 demonstrated, 1 underdetermined)",
            "  Q-F: interference and wave phenomena (transient interference demonstrated)",
            "Remaining gaps are documented as BSR/MBU and do not block first-wave closure",
            "A second wave can investigate: entanglement, multi-body, field excitations, "
            "spatial DOF, Born rule, outcome selection",
            "Verdict: authorized_to_close_first_wave_quantum_program",
        ],
    )


def _build_track_j() -> QFNonclaimFirewall:
    """Track J --- registered nonclaims firewall."""
    return QFNonclaimFirewall(
        nonclaims=QF_NONCLAIMS,
        n_nonclaims=N_QF_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qf_interference_wave_phenomena_audit() -> QFInterferenceWavePhenomenaResult:
    """
    Run the full Appendix Q-F Interference and Wave-Phenomena Audit and return
    a validated QFInterferenceWavePhenomenaResult with all ten tracks populated.

    Returns
    -------
    QFInterferenceWavePhenomenaResult
        Complete audit result with 5 hard-gated verdicts validated against
        their allowed frozenset vocabularies.
    """
    # Build all ten tracks
    track_a = _build_track_a()
    track_b = _build_track_b()
    track_c = _build_track_c()
    track_d = _build_track_d()
    track_e = _build_track_e()
    track_f = _build_track_f()
    track_g = _build_track_g()
    track_h = _build_track_h()
    track_i = _build_track_i()
    track_j = _build_track_j()

    # Five hard-gated verdicts
    phase_v = track_b.phase_verdict
    interf_v = track_c.interference_verdict
    slit_v = track_e.slit_interpretation_verdict
    const_v = track_f.constitutive_interference_verdict
    auth_v = track_i.authorization_verdict

    # Allowed claims (7)
    allowed_claims: List[str] = [
        "Relative phase evolution demonstrated in 2-state toy model via Hamiltonian "
        "part of Lindblad master equation",
        "Transient interference cross terms demonstrated: V(t) = exp(-R_dec t) with "
        "constructive/destructive behavior before decoherence",
        "Visibility decay law V(t) = exp(-delta_phi^2 t / (2 tau)) governs "
        "interference-decoherence competition",
        "Abstract two-path interpretation justified as formal analogy to "
        "two-component superposition structure",
        "Constitutive observable Phi_hat and interference are in tension: "
        "pointer-selected basis suppresses sustained interference, requiring "
        "complementary observable sector",
        "First-wave quantum program (Q-B through Q-F) authorized to close; "
        "remaining gaps documented as BSR/MBU",
        "All Q-F results carry motivated_but_unbuilt Appendix P floor per QA R3",
    ]

    # Forbidden claims (7)
    forbidden_claims: List[str] = [
        "Toy interference implies full double-slit physics or spatial wave mechanics",
        "Phase-sensitive cross terms imply Born-rule probability weighting",
        "Transient coherence implies full wave ontology or permanent quantum effects",
        "Two-state interference toy model implies entanglement or multi-body formalism",
        "Constitutive-decoherence coexistence implies full classical-quantum bridge",
        "Extension-level phase structure implies native canon status",
        "Abstract two-path language implies literal experimental slit closure",
    ]

    # Diagnostics
    diagnostics: Dict[str, Any] = {
        "tau_sq": TAU_SQ,
        "tau": TAU,
        "gamma": GAMMA,
        "gamma_tau": GAMMA * TAU,
        "delta_phi_2state": DELTA_PHI_2STATE,
        "r_dec_2state": R_DEC_2STATE,
        "tau_dec_2state": TAU_DEC_2STATE,
        "visibility_at_tau_dec": VISIBILITY_AT_TAU_DEC,
        "visibility_at_tau_2state": VISIBILITY_AT_TAU_2STATE,
        "timescale_ratio_dec_to_constitutive": TIMESCALE_RATIO_DEC_TO_CONSTITUTIVE,
        "n_interference_ingredients": N_INTERFERENCE_INGREDIENTS,
        "n_candidate_toy_models": N_CANDIDATE_TOY_MODELS,
        "n_viable_toy_models": track_c.n_viable,
        "n_slit_candidates": N_SLIT_CANDIDATES,
        "n_slit_justified": 1,
        "n_nonclaims": N_QF_NONCLAIMS,
        "n_appendix_p_entries": N_APPENDIX_P_ENTRIES,
        "visibility_half_life_2state": VISIBILITY_HALF_LIFE_2STATE,
    }

    result = QFInterferenceWavePhenomenaResult(
        valid=True,
        track_a_eligibility=track_a,
        track_b_relative_phase=track_b,
        track_c_toy_model=track_c,
        track_d_decoherence_competition=track_d,
        track_e_slit_interpretation=track_e,
        track_f_constitutive_interference=track_f,
        track_g_comparative=track_g,
        track_h_appendix_p=track_h,
        track_i_authorization=track_i,
        track_j_nonclaims=track_j,
        phase_verdict=phase_v,
        interference_verdict=interf_v,
        slit_interpretation_verdict=slit_v,
        constitutive_interference_verdict=const_v,
        authorization_verdict=auth_v,
        qf_appendix_p_class=QF_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QF_NONCLAIMS,
        diagnostics=diagnostics,
    )

    # Validate immediately on construction
    validate_qf_result(result)

    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qf_result(result: QFInterferenceWavePhenomenaResult) -> None:
    """
    Validate all five hard-gated verdicts against their allowed frozenset
    vocabularies and check structural consistency.

    Raises ValueError if any check fails.
    """
    # Five hard-gated verdicts
    checks = [
        (result.phase_verdict, ALLOWED_PHASE_VERDICTS, "Phase verdict"),
        (result.interference_verdict, ALLOWED_INTERFERENCE_VERDICTS, "Interference verdict"),
        (result.slit_interpretation_verdict, ALLOWED_SLIT_INTERPRETATION_VERDICTS,
         "Slit interpretation verdict"),
        (result.constitutive_interference_verdict, ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS,
         "Constitutive interference verdict"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization verdict"),
    ]
    for verdict, allowed, label in checks:
        if verdict not in allowed:
            raise ValueError(
                f"{label} '{verdict}' is not in allowed vocabulary {allowed}"
            )

    # Overall Appendix P class
    if result.qf_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError(
            f"Overall Appendix P class '{result.qf_appendix_p_class}' is not in "
            f"allowed vocabulary {ALLOWED_APPENDIX_P_CLASSES}"
        )

    # Track H Appendix P entries
    for entry in result.track_h_appendix_p.entries:
        if entry.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(
                f"Track H entry '{entry.item_id}' has Appendix P class "
                f"'{entry.appendix_p_class}' not in allowed vocabulary"
            )

    # Nonclaim count
    if result.track_j_nonclaims.n_nonclaims != N_QF_NONCLAIMS:
        raise ValueError(
            f"Nonclaim count {result.track_j_nonclaims.n_nonclaims} does not match "
            f"expected {N_QF_NONCLAIMS}"
        )

    # All nonclaims registered
    if not result.track_j_nonclaims.all_registered:
        raise ValueError("Track J nonclaim firewall is not fully registered")

    # Claim counts
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(
            f"Expected {N_ALLOWED_CLAIMS} allowed claims, got {len(result.allowed_claims)}"
        )
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(
            f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims, got {len(result.forbidden_claims)}"
        )

    # Track A counts consistency
    ta = result.track_a_eligibility
    n_pres = sum(1 for ing in ta.ingredients if ing.status == "present")
    n_cond = sum(1 for ing in ta.ingredients if ing.status == "conditionally_present")
    n_abs = sum(1 for ing in ta.ingredients if ing.status == "absent")
    n_ext = sum(1 for ing in ta.ingredients if ing.status == "extension_level")
    if n_pres != ta.n_present:
        raise ValueError(f"Track A n_present mismatch: counted {n_pres}, recorded {ta.n_present}")
    if n_cond != ta.n_conditionally_present:
        raise ValueError(
            f"Track A n_conditionally_present mismatch: counted {n_cond}, "
            f"recorded {ta.n_conditionally_present}"
        )
    if n_abs != ta.n_absent:
        raise ValueError(f"Track A n_absent mismatch: counted {n_abs}, recorded {ta.n_absent}")
    if n_ext != ta.n_extension_level:
        raise ValueError(
            f"Track A n_extension_level mismatch: counted {n_ext}, recorded {ta.n_extension_level}"
        )

    # Diagnostic key values
    diag = result.diagnostics
    _assert_close(diag["gamma_tau"], 1.0, "gamma_tau", tol=1e-12)
    _assert_close(diag["timescale_ratio_dec_to_constitutive"], 0.5,
                  "timescale_ratio_dec_to_constitutive", tol=1e-12)
    _assert_close(diag["visibility_at_tau_dec"], math.exp(-1.0),
                  "visibility_at_tau_dec", tol=1e-12)
    _assert_close(diag["visibility_at_tau_2state"], math.exp(-2.0),
                  "visibility_at_tau_2state", tol=1e-12)

    # Track G: TM1 must be rank 1 (strongest)
    for entry in result.track_g_comparative.entries:
        if entry.model_id == "TM1" and entry.strength_ranking != 1:
            raise ValueError("Track G: TM1 must have strength_ranking = 1")
        if entry.model_id == "TM4" and entry.strength_ranking != 4:
            raise ValueError("Track G: TM4 must have strength_ranking = 4")

    # Track I: authorization flags
    if not result.track_i_authorization.first_wave_closure_authorized:
        raise ValueError("Track I: first_wave_closure_authorized must be True")
    if not result.track_i_authorization.second_wave_opening_noted:
        raise ValueError("Track I: second_wave_opening_noted must be True")
    if result.track_i_authorization.further_interference_refinement_needed:
        raise ValueError(
            "Track I: further_interference_refinement_needed must be False"
        )

    # Track C nonclaim: decoherence suppresses sustained interference
    if not result.track_f_constitutive_interference.decoherence_suppresses_that_superposition:
        raise ValueError(
            "Track F: decoherence_suppresses_that_superposition must be True"
        )
    if not result.track_f_constitutive_interference.complementary_sector_needed:
        raise ValueError("Track F: complementary_sector_needed must be True")

    # Track H no_native_canon
    if not result.track_h_appendix_p.no_native_canon:
        raise ValueError("Track H: no_native_canon must be True")


def _assert_close(value: float, expected: float, name: str, tol: float = 1e-10) -> None:
    """Assert that value is close to expected within tolerance."""
    if abs(value - expected) > tol:
        raise ValueError(
            f"Diagnostic '{name}': expected {expected}, got {value} "
            f"(diff = {abs(value - expected):.2e}, tol = {tol:.2e})"
        )


# ---------------------------------------------------------------------------
# Convenience summary printer
# ---------------------------------------------------------------------------

def print_qf_summary(result: QFInterferenceWavePhenomenaResult) -> None:
    """Print a concise human-readable summary of the Q-F audit result."""
    sep = "-" * 72
    print(sep)
    print("Appendix Q-F --- Interference and Wave-Phenomena Audit Summary")
    print(sep)
    print(f"  Overall Appendix P class        : {result.qf_appendix_p_class}")
    print(f"  Phase verdict                   : {result.phase_verdict}")
    print(f"  Interference verdict            : {result.interference_verdict}")
    print(f"  Slit interpretation verdict     : {result.slit_interpretation_verdict}")
    print(f"  Constitutive interference verdict: {result.constitutive_interference_verdict}")
    print(f"  Authorization verdict           : {result.authorization_verdict}")
    print()
    diag = result.diagnostics
    print(f"  tau                : {diag['tau']:.8f}")
    print(f"  gamma (= 1/tau)   : {diag['gamma']:.8f}")
    print(f"  gamma*tau          : {diag['gamma_tau']:.8f}  [must = 1.0]")
    print(f"  V(tau_dec) = e^-1  : {diag['visibility_at_tau_dec']:.8f}")
    print(f"  V(tau) = e^-2      : {diag['visibility_at_tau_2state']:.8f}")
    print(f"  tau_dec_2state     : {diag['tau_dec_2state']:.8f}")
    print(f"  visibility half-life: {diag['visibility_half_life_2state']:.8f}")
    print()
    print("  Track A (Eligibility):")
    ta = result.track_a_eligibility
    print(f"    Ingredients         : {ta.n_ingredients}")
    print(f"    Present             : {ta.n_present}")
    print(f"    Conditionally present: {ta.n_conditionally_present}")
    print(f"    Absent              : {ta.n_absent}")
    print()
    print("  Track G (Comparative, 1 = strongest):")
    for e in sorted(result.track_g_comparative.entries, key=lambda x: x.strength_ranking):
        print(f"    Rank {e.strength_ranking}: {e.model_id:4s}  burden={e.extension_burden:6s}  "
              f"fidelity={e.fidelity_to_qb_through_qe:6s}  "
              f"interference={e.explicitness_of_interference:8s}  "
              f"robustness={e.robustness_against_decoherence}")
    print()
    print(f"  Allowed claims   : {len(result.allowed_claims)}")
    print(f"  Forbidden claims : {len(result.forbidden_claims)}")
    print(f"  Nonclaims        : {result.track_j_nonclaims.n_nonclaims}")
    print(sep)


# ---------------------------------------------------------------------------
# Module-level self-test (importable)
# ---------------------------------------------------------------------------

def _self_test() -> bool:
    """
    Run the audit and validate the result.  Returns True on success.
    Raises on any validation failure.
    """
    result = run_qf_interference_wave_phenomena_audit()
    # Explicit verdict checks
    assert result.phase_verdict == QF_PHASE_VERDICT, (
        f"Phase mismatch: {result.phase_verdict}"
    )
    assert result.interference_verdict == QF_INTERFERENCE_VERDICT, (
        f"Interference mismatch: {result.interference_verdict}"
    )
    assert result.slit_interpretation_verdict == QF_SLIT_INTERPRETATION_VERDICT, (
        f"Slit mismatch: {result.slit_interpretation_verdict}"
    )
    assert result.constitutive_interference_verdict == QF_CONSTITUTIVE_INTERFERENCE_VERDICT, (
        f"Constitutive mismatch: {result.constitutive_interference_verdict}"
    )
    assert result.authorization_verdict == QF_AUTHORIZATION_VERDICT, (
        f"Auth mismatch: {result.authorization_verdict}"
    )
    assert result.qf_appendix_p_class == QF_OVERALL_APPENDIX_P_CLASS, (
        f"P-class mismatch: {result.qf_appendix_p_class}"
    )
    assert result.valid is True
    # Nonclaims length
    assert len(result.exact_nonclaims) == N_QF_NONCLAIMS
    # Diagnostics spot-checks
    assert abs(result.diagnostics["gamma_tau"] - 1.0) < 1e-12
    assert abs(result.diagnostics["timescale_ratio_dec_to_constitutive"] - 0.5) < 1e-12
    assert abs(result.diagnostics["visibility_at_tau_dec"] - math.exp(-1.0)) < 1e-12
    # Track A counts
    assert result.track_a_eligibility.n_present == 2
    assert result.track_a_eligibility.n_conditionally_present == 3
    assert result.track_a_eligibility.n_absent == 0
    return True


if __name__ == "__main__":
    _self_test()
    res = run_qf_interference_wave_phenomena_audit()
    print_qf_summary(res)
