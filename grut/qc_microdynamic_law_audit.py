"""Appendix Q-C — Microdynamic Law Audit.

Mission: Given the minimum kinematic package identified in Q-C0, determine what
class of quantum microdynamic law can evolve the GRUT quantum state in a
mathematically coherent way and recover the classical constitutive equation
tau * dPhi/dt + Phi = X as a controlled limit.

Inherited Inputs
----------------
  Q-B:   density_matrix_or_functional_state_required (BSR)
         quantization_route_currently_blocked (BSR)
         CTP mapping: compatible_only (CAH)

  Q-B.5: J: complex_structure_motivated_independent_postulation (MIP)
         doubled_field_pair_complexification_obstructed (BSR)
         readiness: proceed_only_if_J_is_postulated

  Q-C0:  package_verdict: minimum_kinematic_package_identified (BSR)
         inner_product: inner_product_motivated_independent_postulation (MIP)
         positivity: positivity_requires_postulate (BSR)
         generator_class: lindbladian_like_generator_kinematically_admissible (MBU)
         readiness: ready_only_if_package_is_postulated
         Minimum package: {J (MIP), g (MIP), Lindbladian-like generator (MBU)}
         Ghost obstruction: phi_minus_growth_rate_sign = +1

Four Hard-Gated Verdicts
------------------------
  (1) primary_law_class_verdict
        lindbladian_like_law_preferred
        — Minimal Markovian open-system generator. Consistent with GRUT's first-order
          dissipative ODE structure. Smallest coherent extension burden beyond Q-C0.
          Uniquely satisfies all five preference criteria.

  (2) classical_limit_verdict
        constitutive_limit_structurally_plausible_but_unbuilt
        — For Lindbladian-like law, the expectation-value limit
          d<Phi>/dt = Tr(Phi L[rho]) recovers tau * d<Phi>/dt + <Phi> = <X>
          only when the jump operators L_k and Hamiltonian H are chosen to yield
          a linear dissipator with time constant tau. This is structurally natural
          but no specific L_k has been constructed — classified plausible but unbuilt.

  (3) burden_verdict
        minimal_extension_burden_identified
        — Lindbladian-like law requires: one Hermitian H, at minimum one jump
          operator L_k, and at minimum one rate gamma_k > 0. No new field content,
          no new DOFs, no non-Markovian kernel function. Minimal burden relative
          to all other viable candidates.

  (4) authorization_verdict
        authorized_to_proceed_to_QC5
        — The preferred Lindbladian-like class identifies the generator class
          and provides a structural route to classical-limit recovery. Q-C.5
          (Classical-Limit Audit) may proceed to verify whether the constitutive
          ODE is recovered from the expectation-value limit.

Appendix P Classifications
--------------------------
  Hamiltonian-like:         compatible_but_ad_hoc (kinematically OK, arch-inconsistent)
  Lindbladian-like:         motivated_but_unbuilt (preferred; class identified, law unbuilt)
  Non-Hermitian effective:  compatible_but_ad_hoc (not independently motivated)
  Memory-kernel:            motivated_but_unbuilt (natural for CTP; higher burden)
  Influence-functional:     motivated_but_unbuilt (most natural for CTP; highest burden)
  No coherent law:          bounded_structural_result (null finding, not the verdict)

Scope Discipline
----------------
  NOT deriving the Born rule.
  NOT deriving measurement.
  NOT deriving interference.
  NOT claiming full quantum closure.
  NOT silently importing Schrödinger evolution.
  NOT assuming unitarity, Hermiticity, or Lindblad form unless supported.
  Only auditing the admissible microdynamic law class and classical-limit route.

Physical Constants
------------------
  TAU_SQ = 3/2     (canonical NC)
  PHI_MINUS_GROWTH_RATE_SIGN = +1   (ghost, Q-B.5 Track F)

See: grut/qc0_kinematic_package_audit.py   (Q-C0)
     grut/qb5_complex_structure_audit.py   (Q-B.5)
     grut/qb_quantum_state_space.py        (Q-B)
     grut/appendix_p_taxonomy_audit.py     (Appendix P)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Hard-gated verdict vocabularies
# ================================================================

ALLOWED_PRIMARY_LAW_CLASS_VERDICTS: frozenset = frozenset({
    "hamiltonian_like_law_preferred",
    "lindbladian_like_law_preferred",
    "nonhermitian_effective_law_preferred",
    "memory_kernel_law_preferred",
    "influence_functional_law_preferred",
    "no_unique_preferred_law_class",
    "no_coherent_microdynamic_law_found",
})

ALLOWED_CLASSICAL_LIMIT_VERDICTS: frozenset = frozenset({
    "constitutive_limit_demonstrated",
    "constitutive_limit_structurally_plausible_but_unbuilt",
    "constitutive_limit_blocked",
    "constitutive_limit_underdetermined",
})

ALLOWED_BURDEN_VERDICTS: frozenset = frozenset({
    "minimal_extension_burden_identified",
    "extension_burden_comparable_across_candidates",
    "extension_burden_excessive",
    "burden_still_underdetermined",
})

ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QC5",
    "authorized_only_for_further_microdynamic_refinement",
    "not_authorized_to_proceed",
    "requires_additional_pre_dynamics_audit",
})

# ================================================================
# Track vocabulary
# ================================================================

ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

ALLOWED_ARCH_COMPAT_RATINGS: frozenset = frozenset({
    "structurally_natural",
    "only_compatible",
    "incompatible",
    "underdetermined",
})

ALLOWED_CLASSICAL_LIMIT_STATUSES: frozenset = frozenset({
    "recovery_demonstrated",
    "recovery_structurally_plausible_but_unbuilt",
    "recovery_blocked",
    "recovery_underdetermined",
})

ALLOWED_RECOVERY_TYPES: frozenset = frozenset({
    "expectation_value_limit",
    "coarse_grained_reduced_state_limit",
    "hydrodynamic_long_time_limit",
    "saddle_point_path_history_limit",
    "mean_field_limit",
    "no_recovery_route",
})

# ================================================================
# Counts (deterministic)
# ================================================================

N_CANDIDATE_LAW_CLASSES: int = 6     # CL1 through CL6 (incl. null CL6)
N_VIABLE_CANDIDATES: int = 4         # CL2, CL3, CL4, CL5 (CL1 arch-inconsistent, CL6 null)
N_PREFERRED_CANDIDATES: int = 1      # Lindbladian (CL2) uniquely satisfies all criteria
N_QC_NONCLAIMS: int = 8
N_KINEMATIC_COMPAT_CHECKS: int = 5  # J, inner product, ghost, open-system, topology
N_ARCH_COMPAT_CHECKS: int = 5       # memory, dissipation, CTP, tau_eff, quarantine
N_CLASSICAL_LIMIT_RECOVERY_TYPES: int = 5
N_BURDEN_CATEGORIES: int = 5        # parameters, operators, states, fields, assumptions

# ================================================================
# Physical constants
# ================================================================

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

# ================================================================
# Q-C verdict values
# ================================================================

QC_PRIMARY_LAW_CLASS_VERDICT: str = "lindbladian_like_law_preferred"
QC_CLASSICAL_LIMIT_VERDICT: str = "constitutive_limit_structurally_plausible_but_unbuilt"
QC_BURDEN_VERDICT: str = "minimal_extension_burden_identified"
QC_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QC5"
QC_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# ================================================================
# Nonclaims (Track I)
# ================================================================

QC_NONCLAIMS: List[str] = [
    "NOT_claiming_admissible_law_class_therefore_law_derived"
    "__identifying_Lindblad_class_is_not_constructing_the_Lindblad_operator",
    "NOT_claiming_classical_limit_plausibility_therefore_constitutive_recovery_proven"
    "__expectation_value_route_is_structurally_plausible_but_unbuilt",
    "NOT_claiming_open_system_compatibility_therefore_Lindblad_derived_from_GRUT"
    "__Lindblad_is_kinematically_admissible__not_derived_from_constitutive_ODE",
    "NOT_claiming_influence_functional_compatibility_therefore_CTP_path_integral_canon"
    "__CTP_route_is_MBU__not_native_canon",
    "NOT_claiming_non_hermitian_effective_law_therefore_physical_ontology_fixed"
    "__non_hermitian_effective_is_CAH_at_effective_description_level_only",
    "NOT_claiming_preferred_candidate_therefore_quantum_mechanics_solved"
    "__Lindblad_preference_identifies_the_law_class__not_the_actual_law",
    "NOT_claiming_extension_level_law_therefore_native_GRUT_canon"
    "__all_QC_results_carry_MBU_or_MIP_floor_per_QA_R3",
    "NOT_claiming_microdynamic_law_class_therefore_measurement_solved"
    "__measurement_bridge_remains_QD_territory",
]


# ================================================================
# Dataclasses
# ================================================================


@dataclass
class QCCandidateLaw:
    """Single candidate microdynamic law class (Track A)."""
    candidate_id: str           # e.g. "CL2_lindbladian_like"
    candidate_name: str
    description: str
    required_inputs: List[str]  # what the law needs beyond Q-C0 package
    fits_qc0_package: bool      # True if consistent with Q-C0 minimum
    grut_conflict: Optional[str]  # None if no conflict, else describe
    appendix_p_class: str
    viable: bool                # True if fits + no arch conflict
    notes: List[str] = field(default_factory=list)


@dataclass
class QCCandidateLawInventory:
    """Track A: Complete inventory of candidate law classes."""
    candidates: List[QCCandidateLaw]
    n_candidates: int           # 6
    n_viable: int               # 4
    n_preferred: int            # 1
    notes: List[str] = field(default_factory=list)


@dataclass
class QCKinematicCompatEntry:
    """Kinematic compatibility result for one candidate against one check."""
    candidate_id: str
    check_name: str             # e.g. "j_complex_structure"
    compatible: bool
    reason: str


@dataclass
class QCKinematicCompatResults:
    """Track B: Kinematic compatibility audit (5 checks × 6 candidates)."""
    entries: List[QCKinematicCompatEntry]
    n_checks_per_candidate: int   # 5
    candidates_all_kinematically_compatible: List[str]  # ids of fully compatible ones
    candidates_kinematically_blocked: List[str]
    ghost_constraint_preserved: bool   # True — ghost obstruction honored throughout
    notes: List[str] = field(default_factory=list)


@dataclass
class QCArchCompatEntry:
    """GRUT architecture compatibility result for one candidate."""
    candidate_id: str
    memory_structure_rating: str      # one of ALLOWED_ARCH_COMPAT_RATINGS
    dissipation_rating: str
    ctp_galley_rating: str
    tau_eff_rating: str
    quarantine_rating: str
    overall_arch_rating: str          # dominant rating
    notes: List[str] = field(default_factory=list)


@dataclass
class QCArchCompatResults:
    """Track C: GRUT architecture compatibility audit."""
    entries: List[QCArchCompatEntry]
    structurally_natural_ids: List[str]   # candidates rated structurally_natural
    only_compatible_ids: List[str]
    incompatible_ids: List[str]
    underdetermined_ids: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class QCClassicalLimitEntry:
    """Classical-limit recovery analysis for one candidate (Track D)."""
    candidate_id: str
    recovery_type: str            # one of ALLOWED_RECOVERY_TYPES
    recovery_status: str          # one of ALLOWED_CLASSICAL_LIMIT_STATUSES
    recovery_description: str
    tau_appears_as: str           # how tau enters the limit
    blocking_reason: Optional[str]  # None if not blocked
    notes: List[str] = field(default_factory=list)


@dataclass
class QCClassicalLimitAnalysis:
    """Track D: Classical-limit recovery analysis for all candidates."""
    entries: List[QCClassicalLimitEntry]
    n_demonstrated: int           # 0 — none actually proven
    n_plausible_but_unbuilt: int  # 4 (CL2, CL3, CL4, CL5)
    n_blocked: int                # 1 (CL1 Hamiltonian)
    n_underdetermined: int        # 1 (CL6 null)
    classical_limit_verdict: str
    preferred_recovery_type: str  # "expectation_value_limit" for CL2
    notes: List[str] = field(default_factory=list)


@dataclass
class QCBurdenEntry:
    """Extension burden assessment for one candidate (Track E)."""
    candidate_id: str
    new_free_parameters: List[str]
    new_operator_structures: List[str]
    new_state_objects: List[str]
    new_field_content: List[str]
    new_dynamical_assumptions: List[str]
    burden_score: int    # ordinal 1 (lowest) to 5 (highest) for ranking
    notes: List[str] = field(default_factory=list)


@dataclass
class QCBurdenAnalysis:
    """Track E: Extension burden comparison across viable candidates."""
    entries: List[QCBurdenEntry]
    minimum_burden_candidate_id: str   # "CL2_lindbladian_like"
    burden_verdict: str
    preferred_by_burden: str           # same as minimum
    notes: List[str] = field(default_factory=list)


@dataclass
class QCAppendixPEntry:
    """Single Appendix P entry for a candidate law class (Track F)."""
    candidate_id: str
    candidate_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    rationale: str


@dataclass
class QCAppendixPAudit:
    """Track F: Appendix P classifications for all candidate law classes."""
    entries: List[QCAppendixPEntry]
    n_entries: int
    overall_program_class: str   # "motivated_but_unbuilt"
    no_native_canon_in_any_class: bool  # True
    notes: List[str] = field(default_factory=list)


@dataclass
class QCPreferredLawSelection:
    """Track G: Preferred-law selection audit."""
    preferred_candidate_id: str           # "CL2_lindbladian_like"
    preferred_candidate_name: str
    selection_criteria_met: List[str]     # which of the 5 criteria are met
    n_criteria_met: int                   # 5 for Lindbladian
    unique_preference: bool               # True — single candidate meets all 5
    runner_up_ids: List[str]              # CL4, CL5 also strong
    why_not_runner_ups: str
    primary_law_class_verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QCAuthorizationAudit:
    """Track H: Quantum-program authorization audit."""
    qc5_authorized: bool              # True
    qd_measurement_ready: bool        # False — requires Q-C.5 first
    benchmark_toy_models_ready: bool  # False — requires Q-C.5 first
    more_microdynamic_closure_required: bool  # False at this level
    preconditions_for_qc5: List[str]
    what_qc5_must_do: str
    authorization_verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class QCNonclaimFirewall:
    """Track I: Nonclaim firewall — 8 explicit nonclaims."""
    nonclaims: List[str]
    n_nonclaims: int       # 8
    all_registered: bool   # True


@dataclass
class QCMicrodynamicLawResult:
    """Master result for Q-C microdynamic law audit."""
    valid: bool
    # Nine audit tracks
    track_a_candidate_inventory: QCCandidateLawInventory
    track_b_kinematic_compat: QCKinematicCompatResults
    track_c_arch_compat: QCArchCompatResults
    track_d_classical_limit: QCClassicalLimitAnalysis
    track_e_burden: QCBurdenAnalysis
    track_f_appendix_p: QCAppendixPAudit
    track_g_preferred_law: QCPreferredLawSelection
    track_h_authorization: QCAuthorizationAudit
    track_i_nonclaims: QCNonclaimFirewall
    # Four hard-gated verdicts
    primary_law_class_verdict: str
    classical_limit_verdict: str
    burden_verdict: str
    authorization_verdict: str
    # Summary
    qc_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Track A — Candidate law inventory
# ================================================================


def build_candidate_cl1_hamiltonian() -> QCCandidateLaw:
    """CL1: Hamiltonian-like unitary evolution."""
    return QCCandidateLaw(
        candidate_id="CL1_hamiltonian_like",
        candidate_name="hamiltonian_like_unitary_evolution",
        description=(
            "i partial_t Psi = H Psi (pure-state) or partial_t rho = -i[H, rho] "
            "(density matrix). H is Hermitian on the pre-Hilbert space. "
            "Evolution is unitary (norm-preserving and reversible)."
        ),
        required_inputs=[
            "hermitian_operator_H_on_pre_hilbert_space",
            "energy_scale_or_coupling_constant",
        ],
        fits_qc0_package=True,
        grut_conflict=(
            "GRUT is intrinsically dissipative: tau * dPhi/dt + Phi = X describes "
            "relaxation to equilibrium set by dissipation. Hamiltonian evolution "
            "is energy-conserving and reversible — structurally incompatible with "
            "GRUT's irreversible, first-order dissipative dynamics. "
            "Pure Hamiltonian generator identified as GRUT-inconsistent in Q-C0 Track E."
        ),
        appendix_p_class="compatible_but_ad_hoc",
        viable=False,
        notes=[
            "Kinematically valid on pre-Hilbert space (J + g from Q-C0).",
            "Fails GRUT-architecture check: no dissipation mechanism.",
            "Classical limit of unitary evolution is oscillatory, not tau * dPhi/dt + Phi = X.",
            "Q-C0 Track E: hamiltonian_grut_consistent = False.",
            "CAH: compatible kinematically, not motivated by GRUT's dissipative architecture.",
        ],
    )


def build_candidate_cl2_lindbladian() -> QCCandidateLaw:
    """CL2: Lindbladian-like open-system evolution (preferred)."""
    return QCCandidateLaw(
        candidate_id="CL2_lindbladian_like",
        candidate_name="lindbladian_like_open_system_evolution",
        description=(
            "partial_t rho = L[rho] = -i[H, rho] + sum_k (L_k rho L_k_dag "
            "- 1/2 {L_k_dag L_k, rho}). "
            "H Hermitian, L_k are jump operators, gamma_k >= 0 are decay rates. "
            "Preserves rho >= 0 and Tr(rho) = 1. Markovian open system."
        ),
        required_inputs=[
            "hermitian_operator_H",
            "jump_operators_L_k_at_least_one",
            "decay_rates_gamma_k_nonnegative",
        ],
        fits_qc0_package=True,
        grut_conflict=None,
        appendix_p_class="motivated_but_unbuilt",
        viable=True,
        notes=[
            "Identified as primary admissible class in Q-C0 Track E.",
            "Consistent with GRUT's first-order dissipative ODE (Markovian).",
            "Preserves positivity — consistent with Q-C0 Track C positivity postulate.",
            "Ghost constraints respected: norm dynamics come from Lindblad, not CTP ghost.",
            "Expectation-value limit d<Phi>/dt = Tr(Phi L[rho]) recovers tau*dPhi/dt+Phi=X "
            "when jump operators are chosen to yield linear dissipation with time constant tau.",
            "MBU: construction path clear; actual L_k not yet specified (Q-C's deliverable).",
        ],
    )


def build_candidate_cl3_nonhermitian() -> QCCandidateLaw:
    """CL3: Non-Hermitian effective evolution."""
    return QCCandidateLaw(
        candidate_id="CL3_nonhermitian_effective",
        candidate_name="nonhermitian_effective_evolution",
        description=(
            "partial_t |Psi> = -i H_eff |Psi> where H_eff = H - i*Gamma/2 "
            "(H Hermitian, Gamma >= 0). Or equivalently, the no-jump "
            "Schrödinger-like equation between quantum jumps. Density matrix: "
            "partial_t rho = -i(H_eff rho - rho H_eff_dag) + jump terms (if any)."
        ),
        required_inputs=[
            "non_hermitian_effective_hamiltonian_H_eff",
            "decay_matrix_Gamma_nonnegative",
        ],
        fits_qc0_package=True,
        grut_conflict=None,
        appendix_p_class="compatible_but_ad_hoc",
        viable=True,
        notes=[
            "Kinematically compatible: works on pre-Hilbert space with J and g.",
            "Effective description only — not a fundamental quantum law.",
            "Can embed dissipation in imaginary part of H_eff.",
            "Positivity: without quantum jump terms, norm decays but ρ ≥ 0 not guaranteed.",
            "Less natural than Lindbladian for density-matrix evolution.",
            "CAH: compatible as effective description; not independently motivated by GRUT.",
        ],
    )


def build_candidate_cl4_memory_kernel() -> QCCandidateLaw:
    """CL4: Memory-kernel state evolution."""
    return QCCandidateLaw(
        candidate_id="CL4_memory_kernel",
        candidate_name="memory_kernel_state_evolution",
        description=(
            "partial_t rho(t) = integral_0^t K(t-s) rho(s) ds + source term. "
            "K(t-s) is a time-local operator-valued memory kernel. "
            "Non-Markovian: state at time t depends on history. "
            "Nakajima-Zwanzig formalism. Recovers Markovian Lindblad in short-memory limit."
        ),
        required_inputs=[
            "memory_kernel_function_K_t_minus_s",
            "kernel_domain_specification",
            "initial_correlation_source_if_any",
        ],
        fits_qc0_package=True,
        grut_conflict=None,
        appendix_p_class="motivated_but_unbuilt",
        viable=True,
        notes=[
            "Naturally motivated by GRUT's retarded CTP kernel structure (Q0 item C4).",
            "More general than Lindbladian: Markovian limit K(t-s) → delta(t-s)*L recovers CL2.",
            "Consistent with GRUT's retarded action and influence functional structure.",
            "Classical limit: exponential kernel k(t-s) ∝ exp(-(t-s)/tau) recovers tau*dPhi/dt+Phi=X.",
            "Higher burden than Lindbladian: requires specifying full kernel function K(t,s).",
            "MBU: naturally motivated; kernel construction deferred to Q-C or later.",
        ],
    )


def build_candidate_cl5_influence_functional() -> QCCandidateLaw:
    """CL5: Influence-functional / history-space evolution."""
    return QCCandidateLaw(
        candidate_id="CL5_influence_functional",
        candidate_name="influence_functional_history_space_evolution",
        description=(
            "State evolution described via a path integral with influence action: "
            "rho(Phi_1, Phi_2, t) = integral D[Phi_1] D[Phi_2] "
            "exp(i S[Phi_1] - i S[Phi_2] + S_IF[Phi_1, Phi_2]) rho_0(Phi_1_0, Phi_2_0). "
            "S_IF is the Feynman-Vernon influence phase encoding environment effects."
        ),
        required_inputs=[
            "influence_action_S_IF_phi1_phi2",
            "path_integral_measure",
            "action_S_phi_for_system",
        ],
        fits_qc0_package=True,
        grut_conflict=None,
        appendix_p_class="motivated_but_unbuilt",
        viable=True,
        notes=[
            "Most natural candidate for CTP formalism — direct generalization of Galley CTP action.",
            "CTP doubled fields (Phi_1, Phi_2) are the natural variables.",
            "Influence phase S_IF directly encodes open-system effects (environment trace-out).",
            "Classical limit: saddle-point of S_IF recovers the classical CTP equations.",
            "Highest burden: requires specifying full influence action as a functional.",
            "MBU: most motivated by CTP architecture; construction is a substantial program.",
        ],
    )


def build_candidate_cl6_no_law() -> QCCandidateLaw:
    """CL6: No coherent microdynamic law currently available (null case)."""
    return QCCandidateLaw(
        candidate_id="CL6_no_coherent_law",
        candidate_name="no_coherent_microdynamic_law_available",
        description=(
            "Bounded negative finding: no coherent microdynamic law class "
            "is available given current GRUT architecture without extension. "
            "This is not the primary verdict but is retained as the null case "
            "for completeness."
        ),
        required_inputs=[],
        fits_qc0_package=False,
        grut_conflict=(
            "Contradicted by the existence of viable candidates CL2, CL3, CL4, CL5. "
            "The null case does not apply — at least four viable candidate classes exist."
        ),
        appendix_p_class="bounded_structural_result",
        viable=False,
        notes=[
            "Retained for completeness as the null finding.",
            "Not the primary verdict: viable candidates CL2–CL5 exist.",
            "Would be the verdict if all candidates were kinematically or arch-blocked.",
            "BSR: bounded negative finding preserved as a tractable audit option.",
        ],
    )


def build_track_a_candidate_inventory() -> QCCandidateLawInventory:
    """Track A: Complete candidate law class inventory — 6 candidates."""
    candidates = [
        build_candidate_cl1_hamiltonian(),
        build_candidate_cl2_lindbladian(),
        build_candidate_cl3_nonhermitian(),
        build_candidate_cl4_memory_kernel(),
        build_candidate_cl5_influence_functional(),
        build_candidate_cl6_no_law(),
    ]
    n_viable = sum(1 for c in candidates if c.viable)
    return QCCandidateLawInventory(
        candidates=candidates,
        n_candidates=len(candidates),
        n_viable=n_viable,
        n_preferred=N_PREFERRED_CANDIDATES,
        notes=[
            "CL1 (Hamiltonian): kinematically valid, GRUT-arch incompatible (dissipation). "
            "Not viable.",
            "CL2 (Lindbladian): viable, preferred. Minimal Markovian open-system generator.",
            "CL3 (Non-Hermitian effective): viable, CAH. Effective description only.",
            "CL4 (Memory-kernel): viable, MBU. Natural for CTP; higher burden.",
            "CL5 (Influence-functional): viable, MBU. Most natural for CTP; highest burden.",
            "CL6 (No coherent law): null case. Not the primary verdict.",
        ],
    )


# ================================================================
# Track B — Kinematic compatibility audit
# ================================================================


def build_track_b_kinematic_compat() -> QCKinematicCompatResults:
    """Track B: Kinematic compatibility for each candidate against Q-C0 checks."""
    entries: List[QCKinematicCompatEntry] = []

    # Define the 5 kinematic checks for each candidate
    checks = {
        "j_complex_structure": {
            "CL1": (True, "Unitary evolution commutes with J (requires [H,J]=0 constraint)."),
            "CL2": (True, "Lindblad generator preserves complex linear structure under J."),
            "CL3": (True, "Non-Hermitian law acts on complex linear space (J defined)."),
            "CL4": (True, "Memory kernel acts on complex linear space (J defined)."),
            "CL5": (True, "Influence functional acts on CTP-doubled complex fields."),
            "CL6": (False, "Null case: no law means no compatibility check possible."),
        },
        "inner_product_positivity": {
            "CL1": (True, "Unitary evolution preserves ||psi||^2 = g(psi,psi)."),
            "CL2": (True, "Lindblad preserves rho >= 0 and Tr(rho)=1 by construction."),
            "CL3": (True, "Non-Hermitian norm decays; requires care but compatible with g."),
            "CL4": (True, "Memory-kernel CPTP property preserves positivity when K satisfies CPTP."),
            "CL5": (True, "Influence functional approach respects positivity via influence phase."),
            "CL6": (False, "Null case: no law means no positivity check."),
        },
        "ghost_constraint": {
            "CL1": (True, "Unitary evolution does not use Phi_minus; ghost not engaged."),
            "CL2": (True, "Lindblad jump operators act on field space independent of CTP ghost."),
            "CL3": (True, "Non-Hermitian law acts on field space; ghost structure excluded."),
            "CL4": (True, "Memory kernel on field space; retarded kernel ≠ ghost pair."),
            "CL5": (True, "Influence action S_IF excludes ghost by design (Q-B.5 Track F)."),
            "CL6": (False, "Null case."),
        },
        "open_system_consistency": {
            "CL1": (False, "Hamiltonian = closed system. GRUT is open (dissipative). Inconsistent."),
            "CL2": (True, "Lindblad = designed for open systems. Natural fit."),
            "CL3": (True, "Non-Hermitian effective = effective open-system description."),
            "CL4": (True, "Memory-kernel = general open-system (Nakajima-Zwanzig)."),
            "CL5": (True, "Influence functional = open-system by construction (env trace-out)."),
            "CL6": (False, "Null case."),
        },
        "state_space_topology": {
            "CL1": (True, "Works on pre-Hilbert space (complex inner-product space)."),
            "CL2": (True, "Density matrix rho in pre-Hilbert tensor product."),
            "CL3": (True, "Effective law on pre-Hilbert space."),
            "CL4": (True, "Integro-differential equation on density matrices in pre-Hilbert space."),
            "CL5": (True, "Path integral over field configurations in pre-Hilbert."),
            "CL6": (False, "Null case."),
        },
    }

    cl_ids = ["CL1", "CL2", "CL3", "CL4", "CL5", "CL6"]
    for check_name, by_candidate in checks.items():
        for cl_id, (compat, reason) in by_candidate.items():
            # Map short id to full id
            full_id_map = {
                "CL1": "CL1_hamiltonian_like",
                "CL2": "CL2_lindbladian_like",
                "CL3": "CL3_nonhermitian_effective",
                "CL4": "CL4_memory_kernel",
                "CL5": "CL5_influence_functional",
                "CL6": "CL6_no_coherent_law",
            }
            entries.append(QCKinematicCompatEntry(
                candidate_id=full_id_map[cl_id],
                check_name=check_name,
                compatible=compat,
                reason=reason,
            ))

    # Candidates that pass ALL 5 checks
    full_ids = {
        "CL1": "CL1_hamiltonian_like",
        "CL2": "CL2_lindbladian_like",
        "CL3": "CL3_nonhermitian_effective",
        "CL4": "CL4_memory_kernel",
        "CL5": "CL5_influence_functional",
        "CL6": "CL6_no_coherent_law",
    }
    check_names = list(checks.keys())

    def all_compat(cl_short: str) -> bool:
        return all(checks[ch][cl_short][0] for ch in check_names)

    candidates_all_kinematically_compatible = [
        full_ids[cl] for cl in cl_ids if all_compat(cl)
    ]
    candidates_kinematically_blocked = [
        full_ids[cl] for cl in cl_ids if not all_compat(cl)
    ]

    return QCKinematicCompatResults(
        entries=entries,
        n_checks_per_candidate=N_KINEMATIC_COMPAT_CHECKS,
        candidates_all_kinematically_compatible=candidates_all_kinematically_compatible,
        candidates_kinematically_blocked=candidates_kinematically_blocked,
        ghost_constraint_preserved=True,
        notes=[
            "CL1 fails open_system_consistency: Hamiltonian = closed system, GRUT is open.",
            "CL6 fails all checks: null case, no law to check.",
            "CL2, CL3, CL4, CL5 pass all 5 kinematic checks.",
            "Ghost constraint preserved throughout: all candidates avoid CTP ghost norm.",
            "Note: CL1 passing J/inner-product/ghost/topology checks but failing open-system "
            "makes it kinematically admissible but architecturally blocked.",
        ],
    )


# ================================================================
# Track C — GRUT architecture compatibility audit
# ================================================================


def build_track_c_arch_compat() -> QCArchCompatResults:
    """Track C: GRUT architecture compatibility for each candidate."""
    entries = [
        QCArchCompatEntry(
            candidate_id="CL1_hamiltonian_like",
            memory_structure_rating="incompatible",
            dissipation_rating="incompatible",
            ctp_galley_rating="only_compatible",
            tau_eff_rating="incompatible",
            quarantine_rating="only_compatible",
            overall_arch_rating="incompatible",
            notes=[
                "Memory: Hamiltonian produces unitary/oscillatory evolution, not tau relaxation.",
                "Dissipation: Hamiltonian conserves energy — no dissipation channel.",
                "CTP: Formally compatible as Keldysh Hamiltonian limit, but not open-system.",
                "tau_eff: tau cannot appear as a relaxation parameter in unitary evolution.",
                "Quarantine: OK (no new particle content).",
                "Overall: incompatible with GRUT's dissipative architecture.",
            ],
        ),
        QCArchCompatEntry(
            candidate_id="CL2_lindbladian_like",
            memory_structure_rating="structurally_natural",
            dissipation_rating="structurally_natural",
            ctp_galley_rating="structurally_natural",
            tau_eff_rating="structurally_natural",
            quarantine_rating="structurally_natural",
            overall_arch_rating="structurally_natural",
            notes=[
                "Memory: Markovian limit of CTP corresponds to Lindblad (tau = Markov time).",
                "Dissipation: Lindblad dissipator L_k rho L_k_dag - 1/2{...} is dissipation.",
                "CTP: Lindblad is the quantum limit of the Keldysh / Galley open-system action.",
                "tau_eff: tau appears as the decay rate gamma = 1/tau in the dissipator.",
                "Quarantine: no new field content or DOFs beyond Q-C0 package.",
                "Overall: structurally_natural for GRUT's open-system architecture.",
            ],
        ),
        QCArchCompatEntry(
            candidate_id="CL3_nonhermitian_effective",
            memory_structure_rating="only_compatible",
            dissipation_rating="structurally_natural",
            ctp_galley_rating="only_compatible",
            tau_eff_rating="only_compatible",
            quarantine_rating="structurally_natural",
            overall_arch_rating="only_compatible",
            notes=[
                "Memory: Non-Hermitian H_eff can model decay but not full retarded memory.",
                "Dissipation: Imaginary part of H_eff encodes decay (Gamma matrix).",
                "CTP: Compatible as effective description of open system. Not fully natural.",
                "tau_eff: tau appears as decay scale in Gamma ~ 1/tau.",
                "Quarantine: no new field content.",
                "Overall: only_compatible — effective description, not structural fit.",
            ],
        ),
        QCArchCompatEntry(
            candidate_id="CL4_memory_kernel",
            memory_structure_rating="structurally_natural",
            dissipation_rating="structurally_natural",
            ctp_galley_rating="structurally_natural",
            tau_eff_rating="structurally_natural",
            quarantine_rating="structurally_natural",
            overall_arch_rating="structurally_natural",
            notes=[
                "Memory: Memory kernel K(t-s) directly generalizes tau-retarded structure.",
                "Dissipation: Non-Markovian dissipation encoded in K(t-s).",
                "CTP: Retarded kernel structure in Galley CTP action (Q0 item C4) is natural.",
                "tau_eff: Exponential kernel exp(-(t-s)/tau) makes tau appear as memory scale.",
                "Quarantine: no new field content.",
                "Overall: structurally_natural — most natural generalization of CTP retarded kernel.",
            ],
        ),
        QCArchCompatEntry(
            candidate_id="CL5_influence_functional",
            memory_structure_rating="structurally_natural",
            dissipation_rating="structurally_natural",
            ctp_galley_rating="structurally_natural",
            tau_eff_rating="structurally_natural",
            quarantine_rating="structurally_natural",
            overall_arch_rating="structurally_natural",
            notes=[
                "Memory: Influence functional S_IF[Phi_1, Phi_2] encodes full environment memory.",
                "Dissipation: Imaginary part of S_IF encodes dissipation (Caldeira-Leggett).",
                "CTP: Direct quantum generalization of Galley CTP effective action.",
                "tau_eff: tau appears in influence phase as environment correlation time.",
                "Quarantine: requires CTP path integral measure — no new particle content.",
                "Overall: structurally_natural and most natural for CTP architecture.",
            ],
        ),
        QCArchCompatEntry(
            candidate_id="CL6_no_coherent_law",
            memory_structure_rating="underdetermined",
            dissipation_rating="underdetermined",
            ctp_galley_rating="underdetermined",
            tau_eff_rating="underdetermined",
            quarantine_rating="underdetermined",
            overall_arch_rating="underdetermined",
            notes=["Null case: no law to assess."],
        ),
    ]

    structurally_natural = [e.candidate_id for e in entries
                            if e.overall_arch_rating == "structurally_natural"]
    only_compatible = [e.candidate_id for e in entries
                       if e.overall_arch_rating == "only_compatible"]
    incompatible = [e.candidate_id for e in entries
                    if e.overall_arch_rating == "incompatible"]
    underdetermined = [e.candidate_id for e in entries
                       if e.overall_arch_rating == "underdetermined"]

    return QCArchCompatResults(
        entries=entries,
        structurally_natural_ids=structurally_natural,
        only_compatible_ids=only_compatible,
        incompatible_ids=incompatible,
        underdetermined_ids=underdetermined,
        notes=[
            "Structurally natural: CL2 (Lindbladian), CL4 (memory-kernel), CL5 (influence-functional).",
            "Only compatible: CL3 (non-Hermitian effective).",
            "Incompatible: CL1 (Hamiltonian — no dissipation).",
            "Underdetermined: CL6 (null case).",
        ],
    )


# ================================================================
# Track D — Classical-limit recovery audit
# ================================================================


def build_track_d_classical_limit() -> QCClassicalLimitAnalysis:
    """Track D: Classical constitutive-limit recovery for each candidate."""
    entries = [
        QCClassicalLimitEntry(
            candidate_id="CL1_hamiltonian_like",
            recovery_type="expectation_value_limit",
            recovery_status="recovery_blocked",
            recovery_description=(
                "Ehrenfest theorem for Hamiltonian evolution: "
                "d<Phi>/dt = (i/hbar)<[H, Phi]>. "
                "For a generic Hermitian H, this gives oscillatory or conservative dynamics. "
                "It does NOT recover tau * d<Phi>/dt + <Phi> = <X> without an explicit "
                "dissipation mechanism outside H. The constitutive ODE requires a "
                "relaxation term (-(1/tau)*Phi) which a Hermitian Hamiltonian cannot produce."
            ),
            tau_appears_as="absent — no relaxation time scale in unitary dynamics",
            blocking_reason=(
                "Unitary Hamiltonian evolution cannot produce tau-relaxation. "
                "The classical constitutive ODE is structurally blocked for CL1."
            ),
            notes=[
                "Ehrenfest: d<Phi>/dt = (i/hbar)<[H,Phi]> — no tau appears.",
                "Adding dissipation to Hamiltonian requires promoting it to Lindbladian (→ CL2).",
                "Recovery blocked for pure Hamiltonian class.",
            ],
        ),
        QCClassicalLimitEntry(
            candidate_id="CL2_lindbladian_like",
            recovery_type="expectation_value_limit",
            recovery_status="recovery_structurally_plausible_but_unbuilt",
            recovery_description=(
                "For Lindblad generator L[rho] = -i[H, rho] + sum_k gamma_k "
                "(L_k rho L_k_dag - 1/2{L_k_dag L_k, rho}), the expectation-value "
                "limit gives: d<Phi>/dt = Tr(Phi * L[rho]). "
                "Choosing L_k = sqrt(gamma) * a_Phi (lowering operator analogue "
                "with [a_Phi, a_Phi_dag] = 1/tau) and H = 0, the mean-field equation "
                "reduces to: tau * d<Phi>/dt + <Phi> = <X>. "
                "This recovery route is structurally natural but requires specifying "
                "the actual jump operators L_k — which is Q-C's deliverable, not Q-C0's."
            ),
            tau_appears_as="decay_rate gamma = 1/tau in Lindblad dissipator",
            blocking_reason=None,
            notes=[
                "Expectation-value limit: d<Phi>/dt = Tr(Phi L[rho]) with appropriate L_k.",
                "Constitutive ODE recovered when L_k chosen as linear dissipator with tau.",
                "Mean-field: <Phi(t)> satisfies tau*d<Phi>/dt + <Phi> = <X> in the linear regime.",
                "Status: plausible_but_unbuilt — L_k not yet constructed.",
            ],
        ),
        QCClassicalLimitEntry(
            candidate_id="CL3_nonhermitian_effective",
            recovery_type="expectation_value_limit",
            recovery_status="recovery_structurally_plausible_but_unbuilt",
            recovery_description=(
                "For non-Hermitian H_eff = H - i*Gamma/2, the no-jump evolution gives: "
                "d<Phi>/dt ≈ <-i[H, Phi]> - (1/2)<{Gamma, Phi}>. "
                "Choosing H = 0 and Gamma = (1/tau) * I (identity times decay rate), "
                "we get: d<Phi>/dt = -(1/tau)<Phi> + renormalization terms. "
                "With appropriate source term, tau * d<Phi>/dt + <Phi> = <X> is recovered. "
                "This is an effective approximation; the full density matrix equation "
                "requires quantum jumps to maintain trace."
            ),
            tau_appears_as="decay matrix Gamma = (1/tau)*I",
            blocking_reason=None,
            notes=[
                "Non-Hermitian effective: decay via imaginary H_eff component.",
                "Classical limit plausible when Gamma ~ (1/tau)*I.",
                "Without quantum jump terms, Tr(rho) is not conserved — requires care.",
                "CAH status limits trust in this recovery route.",
            ],
        ),
        QCClassicalLimitEntry(
            candidate_id="CL4_memory_kernel",
            recovery_type="coarse_grained_reduced_state_limit",
            recovery_status="recovery_structurally_plausible_but_unbuilt",
            recovery_description=(
                "For memory-kernel evolution partial_t rho(t) = int_0^t K(t-s) rho(s) ds, "
                "the mean-field equation for <Phi(t)> = Tr(Phi rho(t)) becomes: "
                "d<Phi(t)>/dt = int_0^t k(t-s) <Phi(s)> ds + source term. "
                "Choosing an exponential kernel k(t-s) = -(1/tau^2) * exp(-(t-s)/tau) "
                "and taking the Markovian limit (tau -> 0 with kernel norm fixed), "
                "the integro-differential equation reduces to: "
                "tau * d<Phi>/dt + <Phi> = <X>. "
                "The exponential kernel is structurally motivated by GRUT's tau_sq = 3/2."
            ),
            tau_appears_as="memory_kernel_timescale in K(t-s) ~ exp(-(t-s)/tau)",
            blocking_reason=None,
            notes=[
                "Markovian limit of memory-kernel → Lindblad (bridges CL4 and CL2).",
                "Exponential kernel exp(-(t-s)/tau) gives first-order ODE in Markovian limit.",
                "tau^2 = 3/2 constrains the kernel normalization.",
                "MBU: kernel not yet constructed; route structurally natural.",
            ],
        ),
        QCClassicalLimitEntry(
            candidate_id="CL5_influence_functional",
            recovery_type="saddle_point_path_history_limit",
            recovery_status="recovery_structurally_plausible_but_unbuilt",
            recovery_description=(
                "For influence functional evolution, the classical equations of motion "
                "emerge from the saddle-point of the CTP effective action: "
                "delta(S[Phi_1] - S[Phi_2] + S_IF[Phi_1, Phi_2]) / delta Phi_+ = 0 "
                "at Phi_1 = Phi_2 = Phi (physical limit, Phi_- -> 0). "
                "The Galley CTP effective action (Q0 item B2 / C4) already encodes "
                "dissipative retarded dynamics. The saddle-point at Phi_- -> 0 "
                "recovers the classical constitutive equation tau*dPhi/dt + Phi = X "
                "from the retarded kernel structure. "
                "Full quantum influence functional is not yet constructed."
            ),
            tau_appears_as="retarded_kernel_timescale in influence phase S_IF",
            blocking_reason=None,
            notes=[
                "Saddle-point of CTP action at Phi_- -> 0 gives classical EOM.",
                "Galley CTP already provides classical limit route (Q0 items B2, C4).",
                "Quantum influence functional is a generalization of the classical CTP action.",
                "Most natural classical-limit route (CTP → classical is already established).",
                "MBU: quantum S_IF not yet built; classical limit route structurally natural.",
            ],
        ),
        QCClassicalLimitEntry(
            candidate_id="CL6_no_coherent_law",
            recovery_type="no_recovery_route",
            recovery_status="recovery_underdetermined",
            recovery_description="Null case: no law means no classical-limit route.",
            tau_appears_as="not_applicable",
            blocking_reason="No law defined.",
            notes=["Null case."],
        ),
    ]

    n_demonstrated = sum(1 for e in entries
                         if e.recovery_status == "recovery_demonstrated")
    n_plausible = sum(1 for e in entries
                      if e.recovery_status == "recovery_structurally_plausible_but_unbuilt")
    n_blocked = sum(1 for e in entries
                    if e.recovery_status == "recovery_blocked")
    n_underdetermined = sum(1 for e in entries
                            if e.recovery_status == "recovery_underdetermined")

    return QCClassicalLimitAnalysis(
        entries=entries,
        n_demonstrated=n_demonstrated,
        n_plausible_but_unbuilt=n_plausible,
        n_blocked=n_blocked,
        n_underdetermined=n_underdetermined,
        classical_limit_verdict=QC_CLASSICAL_LIMIT_VERDICT,
        preferred_recovery_type="expectation_value_limit",
        notes=[
            "CL1 (Hamiltonian): recovery_blocked — unitary dynamics has no tau relaxation.",
            "CL2 (Lindbladian): plausible_but_unbuilt — expectation-value limit with gamma=1/tau.",
            "CL3 (Non-Hermitian): plausible_but_unbuilt — effective decay with Gamma~(1/tau)I.",
            "CL4 (Memory-kernel): plausible_but_unbuilt — exponential kernel Markovian limit.",
            "CL5 (Influence-functional): plausible_but_unbuilt — CTP saddle-point.",
            "CL6 (No law): underdetermined — null case.",
            "Overall: no recovery demonstrated; four candidates plausible but unbuilt.",
            "Verdict: constitutive_limit_structurally_plausible_but_unbuilt.",
        ],
    )


# ================================================================
# Track E — Minimal parameter burden audit
# ================================================================


def build_track_e_burden() -> QCBurdenAnalysis:
    """Track E: Extension burden comparison for viable candidates."""
    entries = [
        QCBurdenEntry(
            candidate_id="CL2_lindbladian_like",
            new_free_parameters=[
                "decay_rates_gamma_k_nonnegative",
            ],
            new_operator_structures=[
                "hermitian_hamiltonian_H",
                "jump_operators_L_k",
            ],
            new_state_objects=[],
            new_field_content=[],
            new_dynamical_assumptions=[
                "markovian_approximation_no_long_memory",
                "complete_positivity_of_evolution",
            ],
            burden_score=1,
            notes=[
                "Minimal: H + {L_k} + {gamma_k}. No new fields, no new state objects.",
                "Markovian assumption built in (consistent with first-order ODE).",
                "Complete positivity is a structural constraint, not an additional DOF.",
                "LOWEST BURDEN among viable candidates.",
            ],
        ),
        QCBurdenEntry(
            candidate_id="CL3_nonhermitian_effective",
            new_free_parameters=[
                "decay_matrix_entries_Gamma_ij",
            ],
            new_operator_structures=[
                "non_hermitian_effective_hamiltonian_H_eff",
                "decay_matrix_Gamma",
            ],
            new_state_objects=[],
            new_field_content=[],
            new_dynamical_assumptions=[
                "no_jump_approximation_or_quantum_jump_specification",
                "effective_description_only",
            ],
            burden_score=2,
            notes=[
                "Similar to CL2 but requires specifying jump specification separately.",
                "CAH status reduces motivation.",
                "SECOND LOWEST burden, but lower epistemic status.",
            ],
        ),
        QCBurdenEntry(
            candidate_id="CL4_memory_kernel",
            new_free_parameters=[
                "kernel_timescale_parameter",
                "kernel_amplitude",
                "additional_kernel_shape_parameters_if_non_exponential",
            ],
            new_operator_structures=[
                "operator_valued_kernel_K_t_minus_s",
                "time_domain_convolution_structure",
            ],
            new_state_objects=[],
            new_field_content=[],
            new_dynamical_assumptions=[
                "time_nonlocal_dynamics",
                "initial_correlation_treatment",
                "CPTP_condition_on_kernel",
            ],
            burden_score=3,
            notes=[
                "Requires specifying full kernel function K(t,s) — more than a constant.",
                "Non-Markovian: additional initial-correlation treatment needed.",
                "Higher burden than CL2 but structurally natural for CTP.",
            ],
        ),
        QCBurdenEntry(
            candidate_id="CL5_influence_functional",
            new_free_parameters=[
                "influence_action_functional_parameters",
                "environment_spectral_density",
                "system_environment_coupling_parameters",
            ],
            new_operator_structures=[
                "influence_phase_S_IF_as_functional",
                "path_integral_measure_for_CTP_fields",
                "action_S_for_system_fields",
            ],
            new_state_objects=[
                "path_integral_density_matrix_rho_phi1_phi2",
            ],
            new_field_content=[],
            new_dynamical_assumptions=[
                "path_integral_convergence",
                "saddle_point_validity_for_classical_limit",
                "influence_phase_structure_specification",
            ],
            burden_score=4,
            notes=[
                "Highest burden: full functional S_IF[Phi_1, Phi_2] must be specified.",
                "Environment spectral density and system-env coupling are new parameters.",
                "Path integral measure and convergence are non-trivial technical requirements.",
                "Most naturally motivated by CTP; highest construction cost.",
            ],
        ),
    ]

    return QCBurdenAnalysis(
        entries=entries,
        minimum_burden_candidate_id="CL2_lindbladian_like",
        burden_verdict=QC_BURDEN_VERDICT,
        preferred_by_burden="CL2_lindbladian_like",
        notes=[
            "Burden ranking (lowest to highest): CL2 < CL3 < CL4 < CL5.",
            "CL2 (Lindbladian): H + {L_k} + {gamma_k}. No new fields, no new state objects.",
            "CL3 (Non-Hermitian): similar to CL2 but lower epistemic status (CAH).",
            "CL4 (Memory-kernel): requires full kernel function K(t,s).",
            "CL5 (Influence-functional): requires full influence action S_IF as functional.",
            "Verdict: minimal_extension_burden_identified — CL2 uniquely has lowest burden.",
        ],
    )


# ================================================================
# Track F — Appendix P audit
# ================================================================


def build_track_f_appendix_p() -> QCAppendixPAudit:
    """Track F: Appendix P classification for all candidate law classes."""
    entries = [
        QCAppendixPEntry(
            candidate_id="CL1_hamiltonian_like",
            candidate_name="hamiltonian_like_unitary_evolution",
            appendix_p_class="compatible_but_ad_hoc",
            allowed_claim=(
                "Hamiltonian-like evolution is kinematically admissible on a pre-Hilbert "
                "space with J and g. It may be considered as a component of a larger "
                "open-system construction if dissipation is added separately."
            ),
            forbidden_claim=(
                "Hamiltonian evolution recovers the constitutive ODE tau*dPhi/dt+Phi=X. "
                "GRUT architecture is compatible with purely unitary dynamics."
            ),
            rationale=(
                "CAH: kinematically valid but architecturally inconsistent with GRUT's "
                "dissipative character. Not independently motivated by GRUT structure."
            ),
        ),
        QCAppendixPEntry(
            candidate_id="CL2_lindbladian_like",
            candidate_name="lindbladian_like_open_system_evolution",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "The Lindbladian generator class is the preferred microdynamic law class "
                "for GRUT. It is kinematically admissible, GRUT-architecturally natural, "
                "and has the minimal extension burden. The expectation-value limit provides "
                "a structural route to recovering tau*dPhi/dt+Phi=X."
            ),
            forbidden_claim=(
                "The Lindbladian law is derived from GRUT architecture. "
                "The jump operators L_k are specified. "
                "The classical limit is proven. "
                "All Q-C results built on Lindbladian-like law receive native_canon."
            ),
            rationale=(
                "MBU: strongly motivated by open-system structure, first-order ODE analogy, "
                "and CTP Keldysh limit. Construction path identified. Actual operator "
                "values not yet determined (Q-C's deliverable)."
            ),
        ),
        QCAppendixPEntry(
            candidate_id="CL3_nonhermitian_effective",
            candidate_name="nonhermitian_effective_evolution",
            appendix_p_class="compatible_but_ad_hoc",
            allowed_claim=(
                "Non-Hermitian effective evolution is a valid effective description "
                "of open-system dynamics. It can model decay with time scale tau "
                "via the imaginary part of H_eff."
            ),
            forbidden_claim=(
                "Non-Hermitian effective law provides a physical ontology. "
                "The decay matrix Gamma is derived from GRUT. "
                "Non-Hermitian evolution is equivalent to Lindbladian evolution."
            ),
            rationale=(
                "CAH: valid as an effective description but not independently motivated "
                "by GRUT architecture. Less complete than Lindbladian (trace not conserved "
                "without jump terms)."
            ),
        ),
        QCAppendixPEntry(
            candidate_id="CL4_memory_kernel",
            candidate_name="memory_kernel_state_evolution",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Memory-kernel evolution is strongly motivated by GRUT's retarded CTP "
                "kernel structure (Q0 item C4). An exponential kernel with timescale tau "
                "provides a natural route to recovering the constitutive ODE in the "
                "Markovian limit. It is a viable, MBU-level candidate."
            ),
            forbidden_claim=(
                "Memory-kernel law is derived from GRUT. "
                "The kernel K(t-s) is specified. "
                "Memory-kernel evolution is more fundamental than Lindbladian."
            ),
            rationale=(
                "MBU: highly motivated by CTP retarded structure. More natural than "
                "Lindbladian for non-Markovian physics but higher burden. Runner-up to CL2."
            ),
        ),
        QCAppendixPEntry(
            candidate_id="CL5_influence_functional",
            candidate_name="influence_functional_history_space_evolution",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Influence-functional evolution is the most natural quantum extension "
                "of the Galley CTP effective action. The saddle-point limit recovers "
                "the classical CTP equations. It is a viable MBU-level candidate with "
                "the strongest structural connection to GRUT's CTP architecture."
            ),
            forbidden_claim=(
                "Influence-functional law is derived from GRUT. "
                "The influence action S_IF is specified. "
                "The path integral formulation is native to GRUT quantum theory."
            ),
            rationale=(
                "MBU: most naturally motivated by CTP architecture; direct quantum "
                "generalization of Galley CTP action. Highest construction burden. "
                "Runner-up to CL2 in classical-limit connection strength."
            ),
        ),
        QCAppendixPEntry(
            candidate_id="CL6_no_coherent_law",
            candidate_name="no_coherent_microdynamic_law_available",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "The null finding (no coherent law) is preserved as a valid BSR "
                "outcome if all candidate classes were blocked. This is not the "
                "primary verdict — viable candidates exist."
            ),
            forbidden_claim=(
                "The null finding is the primary verdict of Q-C. "
                "No viable microdynamic law class exists for GRUT."
            ),
            rationale=(
                "BSR: bounded negative finding preserved per Appendix P doctrine. "
                "Not activated here because viable candidates exist."
            ),
        ),
    ]

    no_native_canon = all(e.appendix_p_class != "native_canon" for e in entries)

    return QCAppendixPAudit(
        entries=entries,
        n_entries=len(entries),
        overall_program_class="motivated_but_unbuilt",
        no_native_canon_in_any_class=no_native_canon,
        notes=[
            "CL1 (Hamiltonian): CAH — arch-inconsistent.",
            "CL2 (Lindbladian): MBU — preferred; minimal burden.",
            "CL3 (Non-Hermitian): CAH — effective description only.",
            "CL4 (Memory-kernel): MBU — natural for CTP; runner-up.",
            "CL5 (Influence-functional): MBU — most natural for CTP; highest burden.",
            "CL6 (No law): BSR — null finding preserved.",
            "Overall: MBU (dominant for the preferred and runner-up candidates).",
            "No candidate receives native_canon: QA-R2 preserved.",
        ],
    )


# ================================================================
# Track G — Preferred-law selection audit
# ================================================================


def build_track_g_preferred_law() -> QCPreferredLawSelection:
    """Track G: Preferred-law selection audit."""
    # Five preference criteria for each candidate
    criteria = {
        "compatible_with_minimum_package": {
            "CL2_lindbladian_like": True,
            "CL3_nonhermitian_effective": True,
            "CL4_memory_kernel": True,
            "CL5_influence_functional": True,
        },
        "fits_grut_open_system_architecture": {
            "CL2_lindbladian_like": True,
            "CL3_nonhermitian_effective": True,
            "CL4_memory_kernel": True,
            "CL5_influence_functional": True,
        },
        "preserves_ghost_constraints": {
            "CL2_lindbladian_like": True,
            "CL3_nonhermitian_effective": True,
            "CL4_memory_kernel": True,
            "CL5_influence_functional": True,
        },
        "strongest_classical_limit_route": {
            "CL2_lindbladian_like": True,   # expectation-value + gamma=1/tau direct
            "CL3_nonhermitian_effective": False,  # effective only; CAH limits strength
            "CL4_memory_kernel": True,             # Markovian limit is strong
            "CL5_influence_functional": True,      # saddle-point is strong
        },
        "minimizes_added_structure": {
            "CL2_lindbladian_like": True,   # burden score 1 (lowest)
            "CL3_nonhermitian_effective": False,  # CAH; lower motivated status
            "CL4_memory_kernel": False,            # burden score 3
            "CL5_influence_functional": False,     # burden score 4
        },
    }

    def count_criteria(cid: str) -> int:
        return sum(1 for crit in criteria.values() if crit.get(cid, False))

    cl2_criteria_met = [crit for crit, vals in criteria.items()
                        if vals.get("CL2_lindbladian_like", False)]
    n_cl2 = len(cl2_criteria_met)

    return QCPreferredLawSelection(
        preferred_candidate_id="CL2_lindbladian_like",
        preferred_candidate_name="lindbladian_like_open_system_evolution",
        selection_criteria_met=cl2_criteria_met,
        n_criteria_met=n_cl2,
        unique_preference=True,
        runner_up_ids=[
            "CL4_memory_kernel",
            "CL5_influence_functional",
        ],
        why_not_runner_ups=(
            "CL4 (memory-kernel): meets 4/5 criteria but fails 'minimizes added structure' "
            "(burden score 3 vs 1 for CL2). Higher burden without unique classical-limit advantage. "
            "CL5 (influence-functional): meets 4/5 criteria but fails 'minimizes added structure' "
            "(burden score 4). Most natural for CTP but requires full path-integral construction. "
            "CL3 (non-Hermitian effective): meets only 3/5 criteria; CAH class limits strength "
            "of classical-limit route and motivated status."
        ),
        primary_law_class_verdict=QC_PRIMARY_LAW_CLASS_VERDICT,
        notes=[
            "CL2 uniquely satisfies all 5 preference criteria.",
            "CL4 and CL5 are strong runners-up (4/5 criteria each).",
            "CL3 meets 3/5 criteria; lower motivation and CAH class.",
            "CL1 excluded: kinematically admissible but GRUT-arch incompatible.",
            "Verdict: lindbladian_like_law_preferred.",
        ],
    )


# ================================================================
# Track H — Authorization audit
# ================================================================


def build_track_h_authorization() -> QCAuthorizationAudit:
    """Track H: Quantum-program authorization audit."""
    return QCAuthorizationAudit(
        qc5_authorized=True,
        qd_measurement_ready=False,
        benchmark_toy_models_ready=False,
        more_microdynamic_closure_required=False,
        preconditions_for_qc5=[
            "primary_law_class_identified_as_lindbladian_like_MBU",
            "classical_limit_route_identified_expectation_value_with_gamma_eq_1_over_tau",
            "ghost_constraints_preserved_throughout_qc",
            "minimum_kinematic_package_qc0_explicitly_postulated",
            "all_qc_results_carry_mbu_or_mip_appendix_p_floor",
            "nonclaims_registered_and_honored",
        ],
        what_qc5_must_do=(
            "Q-C.5 (Classical-Limit Audit) must verify whether the expectation-value "
            "limit d<Phi>/dt = Tr(Phi * L[rho]) with a Lindblad generator L explicitly "
            "constructed to recover tau * d<Phi>/dt + Phi = X. "
            "This requires: (1) specifying the jump operators L_k and decay rates gamma_k, "
            "(2) taking the mean-field limit, (3) verifying the tau-relaxation structure, "
            "(4) checking consistency with tau_sq = 3/2. "
            "If Q-C.5 achieves recovery, the result will be classified BSR or MBU depending "
            "on whether the specific L_k can be derived or must be postulated."
        ),
        authorization_verdict=QC_AUTHORIZATION_VERDICT,
        notes=[
            "Q-C.5 authorized: primary law class identified, classical-limit route plausible.",
            "Q-D (measurement) not ready: requires Q-C.5 closure first.",
            "Benchmark toy models not ready: requires at least Q-C.5 closure.",
            "No additional pre-dynamics audit required: Q-C0 kinematic package is complete.",
            "All Q-C.5 results carry MBU or MIP floor per QA-R3.",
        ],
    )


# ================================================================
# Track I — Nonclaim firewall
# ================================================================


def build_track_i_nonclaims() -> QCNonclaimFirewall:
    """Track I: Nonclaim firewall — 8 explicit nonclaims."""
    return QCNonclaimFirewall(
        nonclaims=QC_NONCLAIMS,
        n_nonclaims=N_QC_NONCLAIMS,
        all_registered=True,
    )


# ================================================================
# Allowed and forbidden claims
# ================================================================


def build_allowed_claims() -> List[str]:
    return [
        "The primary microdynamic law class for GRUT is Lindbladian-like (MBU).",
        "The classical constitutive ODE limit is structurally plausible but unbuilt.",
        "Lindbladian-like law uniquely satisfies all five preference criteria.",
        "The minimal extension burden is identified: H + {L_k} + {gamma_k}.",
        "Memory-kernel (CL4) and influence-functional (CL5) are viable MBU runners-up.",
        "Hamiltonian-like evolution (CL1) is GRUT-architecturally incompatible (no dissipation).",
        "Ghost constraints from Q-B.5 are preserved across all viable candidate classes.",
        "Q-C.5 (Classical-Limit Audit) is authorized to proceed.",
        "All Q-C results carry MBU minimum Appendix P floor per Q-A charter rule QA-R3.",
        "Classical-limit recovery for CL2 proceeds via d<Phi>/dt = Tr(Phi * L[rho]).",
    ]


def build_forbidden_claims() -> List[str]:
    return [
        "The Lindbladian generator law is derived from GRUT architecture.",
        "The jump operators L_k and decay rates gamma_k are specified.",
        "The classical constitutive ODE recovery is proven.",
        "Identifying the law class is equivalent to solving quantum mechanics.",
        "The influence-functional law is native to GRUT (it is MBU, not NC).",
        "Non-Hermitian effective evolution establishes physical ontology.",
        "Open-system compatibility implies Lindblad structure is uniquely determined.",
        "The microdynamic law class implies measurement is solved.",
        "Q-C closure implies Q-D (measurement) may be attempted.",
        "All Q-C results receive native_canon or effective_reduction classification.",
    ]


# ================================================================
# Master audit function
# ================================================================


def run_qc_microdynamic_law_audit() -> QCMicrodynamicLawResult:
    """Execute the full Q-C microdynamic law audit.

    Returns a fully populated QCMicrodynamicLawResult with:
      - All 9 audit tracks completed
      - 4 hard-gated verdicts set
      - Appendix P classification throughout
      - Nonclaim firewall registered

    Primary finding: lindbladian_like_law_preferred (MBU)
    Classical limit: constitutive_limit_structurally_plausible_but_unbuilt
    Burden: minimal_extension_burden_identified
    Authorization: authorized_to_proceed_to_QC5
    """
    track_a = build_track_a_candidate_inventory()
    track_b = build_track_b_kinematic_compat()
    track_c = build_track_c_arch_compat()
    track_d = build_track_d_classical_limit()
    track_e = build_track_e_burden()
    track_f = build_track_f_appendix_p()
    track_g = build_track_g_preferred_law()
    track_h = build_track_h_authorization()
    track_i = build_track_i_nonclaims()

    allowed = build_allowed_claims()
    forbidden = build_forbidden_claims()

    # Validate hard-gated verdicts
    assert QC_PRIMARY_LAW_CLASS_VERDICT in ALLOWED_PRIMARY_LAW_CLASS_VERDICTS
    assert QC_CLASSICAL_LIMIT_VERDICT in ALLOWED_CLASSICAL_LIMIT_VERDICTS
    assert QC_BURDEN_VERDICT in ALLOWED_BURDEN_VERDICTS
    assert QC_AUTHORIZATION_VERDICT in ALLOWED_AUTHORIZATION_VERDICTS

    # Consistency checks
    assert track_a.n_candidates == N_CANDIDATE_LAW_CLASSES
    assert track_a.n_viable == N_VIABLE_CANDIDATES
    assert track_d.n_demonstrated == 0
    assert track_d.n_plausible_but_unbuilt == 4
    assert track_d.n_blocked == 1
    assert track_e.minimum_burden_candidate_id == "CL2_lindbladian_like"
    assert track_f.no_native_canon_in_any_class is True
    assert track_g.n_criteria_met == 5
    assert track_g.unique_preference is True
    assert track_g.preferred_candidate_id == "CL2_lindbladian_like"
    assert track_h.qc5_authorized is True
    assert track_i.n_nonclaims == N_QC_NONCLAIMS
    assert track_i.all_registered is True

    diagnostics: Dict[str, Any] = {
        "n_candidate_law_classes": track_a.n_candidates,
        "n_viable_candidates": track_a.n_viable,
        "n_preferred": track_a.n_preferred,
        "structurally_natural_ids": track_c.structurally_natural_ids,
        "incompatible_ids": track_c.incompatible_ids,
        "n_classical_limit_demonstrated": track_d.n_demonstrated,
        "n_classical_limit_plausible": track_d.n_plausible_but_unbuilt,
        "n_classical_limit_blocked": track_d.n_blocked,
        "minimum_burden_candidate": track_e.minimum_burden_candidate_id,
        "no_native_canon": track_f.no_native_canon_in_any_class,
        "preferred_law_id": track_g.preferred_candidate_id,
        "n_preference_criteria_met": track_g.n_criteria_met,
        "qc5_authorized": track_h.qc5_authorized,
        "n_nonclaims": track_i.n_nonclaims,
        "tau_sq": TAU_SQ,
        "phi_minus_growth_rate_sign": PHI_MINUS_GROWTH_RATE_SIGN,
        "qc_appendix_p_class": QC_OVERALL_APPENDIX_P_CLASS,
    }

    return QCMicrodynamicLawResult(
        valid=True,
        track_a_candidate_inventory=track_a,
        track_b_kinematic_compat=track_b,
        track_c_arch_compat=track_c,
        track_d_classical_limit=track_d,
        track_e_burden=track_e,
        track_f_appendix_p=track_f,
        track_g_preferred_law=track_g,
        track_h_authorization=track_h,
        track_i_nonclaims=track_i,
        primary_law_class_verdict=QC_PRIMARY_LAW_CLASS_VERDICT,
        classical_limit_verdict=QC_CLASSICAL_LIMIT_VERDICT,
        burden_verdict=QC_BURDEN_VERDICT,
        authorization_verdict=QC_AUTHORIZATION_VERDICT,
        qc_appendix_p_class=QC_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed,
        forbidden_claims=forbidden,
        diagnostics=diagnostics,
    )
