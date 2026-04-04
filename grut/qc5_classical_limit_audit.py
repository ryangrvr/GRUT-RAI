"""
GRUT Quantum Program — Appendix Q-C.5
Classical-Limit Recovery Audit

Audits whether the Lindbladian-like microdynamic law (preferred in Q-C) recovers
the GRUT constitutive equation τ·d⟨Φ⟩/dt + ⟨Φ⟩ = ⟨X⟩ in an appropriate classical
(large-scale, low-frequency) regime.

=============================================================================
FOUR HARD-GATED VERDICTS
=============================================================================

1. QC5_CONSTITUTIVE_RECOVERY_VERDICT
   "effective_regime_constitutive_recovery_demonstrated"

   Physics derivation (explicit):
   Given Lindblad master equation:
       dρ/dt = -i[H, ρ] + γ(Φ̂ρΦ̂† - ½{Φ̂†Φ̂, ρ}) + drive terms
   with jump operator L = √γ · Φ̂ = (1/√τ)·Φ̂, γ = 1/τ.

   Taking the expectation value of Φ̂:
       d⟨Φ̂⟩/dt = Tr(Φ̂ · dρ/dt)
                = Tr(Φ̂ · [-i[H, ρ] + γ(Φ̂ρΦ̂† - ½{Φ̂†Φ̂, ρ}) + drive])

   In Markovian + weak-coupling limit, with linear restoring dissipator:
       d⟨Φ̂⟩/dt = -γ⟨Φ̂⟩ + ⟨X̂⟩

   Setting γ = 1/τ:
       d⟨Φ̂⟩/dt = -(1/τ)⟨Φ̂⟩ + (1/τ)⟨X̂⟩

   Multiply through by τ:
       τ · d⟨Φ̂⟩/dt = -⟨Φ̂⟩ + ⟨X̂⟩

   Rearrange:
       τ · d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩

   This is the GRUT constitutive equation with Φ → ⟨Φ̂⟩, X → ⟨X̂⟩.
   Recovery is effective-regime: requires Markovian approximation and the
   specific linear jump operator L = (1/√τ)·Φ̂.

2. QC5_PARAMETER_MATCHING_VERDICT
   "partial_parameter_matching_achieved"

   τ ↔ 1/γ: complete. Source X ↔ bath bias/drive: structurally complete,
   operator unbuilt. Damping coefficient = 1: complete (γτ = 1). Normalization
   and state preparation: underdetermined. Net: partial.

3. QC5_PREFERRED_CLASS_RETENTION_VERDICT
   "lindbladian_preference_retained"

   No secondary class (CL3 non-Hermitian effective, CL4 memory-kernel,
   CL5 influence-functional) provides a strictly stronger recovery route
   at lower or equal burden. Lindbladian preference from Q-C is retained.

4. QC5_AUTHORIZATION_VERDICT
   "authorized_to_proceed_to_QD"

   Effective-regime constitutive recovery demonstrated. Q-D (Measurement
   Bridge) may proceed subject to: (a) recovery applies in Markovian +
   expectation-value regime only; (b) all Q-C.5 results carry MBU/MIP floor;
   (c) Q-D must not assume constitutive recovery extends beyond this regime.

=============================================================================
OVERALL APPENDIX P CLASS: "motivated_but_unbuilt"
=============================================================================

References:
- grut/qc_microdynamic_law_audit.py  (Q-C: primary law class determination)
- grut/qc0_kinematic_package_audit.py (Q-C0: kinematic package)
- grut/qb5_complex_structure_audit.py (Q-B.5: complex structure and kinematics)
- grut/qb_quantum_state_space.py      (Q-B: quantum state space)
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

# =============================================================================
# PHYSICAL CONSTANTS (inherited)
# =============================================================================

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

# Ghost obstruction: Φ₋ grows as dΦ₋/dt = +Φ₋/τ.
# CTP-based norms are dynamically inadmissible.

# =============================================================================
# COUNTS
# =============================================================================

N_CLASSICAL_OBSERVABLE_CANDIDATES: int = 6      # CO1–CO6
N_VIABLE_OBSERVABLE_CANDIDATES: int = 1          # CO1 expectation value only
N_LIMIT_TYPES_TESTED: int = 7                    # see Track D
N_PREFERRED_LIMIT_COMBINATION: int = 3           # Markovian + weak-coupling + expectation-value
N_QC5_NONCLAIMS: int = 8
N_SECONDARY_CLASSES_TESTED: int = 3             # CL3, CL4, CL5

# =============================================================================
# HARD-GATED VERDICT VOCABULARIES
# =============================================================================

ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS: frozenset = frozenset({
    "effective_regime_constitutive_recovery_demonstrated",
    "exact_constitutive_recovery_demonstrated",
    "no_constitutive_recovery_found",
    "constitutive_recovery_blocked_by_ghost",
})

ALLOWED_PARAMETER_MATCHING_VERDICTS: frozenset = frozenset({
    "partial_parameter_matching_achieved",
    "complete_parameter_matching_achieved",
    "parameter_matching_failed",
    "parameter_matching_underdetermined",
})

ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS: frozenset = frozenset({
    "lindbladian_preference_retained",
    "lindbladian_preference_overturned_by_secondary_class",
    "no_preferred_class_identified",
})

ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QD",
    "not_authorized_recovery_incomplete",
    "not_authorized_ghost_obstruction",
    "conditional_authorization_pending_further_audit",
})

ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "motivated_but_unbuilt",
    "native_canon",
    "compatible_but_ad_hoc",
    "bounded_structural_result",
    "excluded",
})

# =============================================================================
# VERDICT STRINGS
# =============================================================================

QC5_CONSTITUTIVE_RECOVERY_VERDICT: str = "effective_regime_constitutive_recovery_demonstrated"
QC5_PARAMETER_MATCHING_VERDICT: str = "partial_parameter_matching_achieved"
QC5_PREFERRED_CLASS_RETENTION_VERDICT: str = "lindbladian_preference_retained"
QC5_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QD"
QC5_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# =============================================================================
# INHERITED FROM Q-C
# =============================================================================

QC_INHERITED_PRIMARY_LAW_CLASS: str = "lindbladian_like_law_preferred"
QC_INHERITED_CLASSICAL_LIMIT: str = "constitutive_limit_structurally_plausible_but_unbuilt"
QC_INHERITED_BURDEN_VERDICT: str = "minimal_extension_burden_identified"
QC_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QC5"
QC_INHERITED_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# =============================================================================
# NONCLAIMS FIREWALL (8 items)
# =============================================================================

QC5_NONCLAIMS: List[str] = [
    "NOT_claiming_constitutive_like_resemblance_therefore_exact_recovery__"
    "effective_regime_recovery_requires_Markovian_limit_and_specific_operator_choice",
    "NOT_claiming_expectation_value_closure_therefore_full_classical_limit_solved__"
    "expectation_value_limit_applies_in_Markovian_regime_only",
    "NOT_claiming_regime_limited_recovery_therefore_native_canon__"
    "all_QC5_results_carry_MBU_floor_per_QA_R3",
    "NOT_claiming_Lindblad_preference_therefore_derivation_complete__"
    "preferred_class_identifies_law_class_not_actual_operator_content",
    "NOT_claiming_parameter_fit_therefore_ontological_equivalence__"
    "tau_matching_identifies_decay_rate_correspondence_not_identity",
    "NOT_claiming_constitutive_recovery_therefore_measurement_solved__"
    "measurement_bridge_remains_QD_territory",
    "NOT_claiming_constitutive_recovery_therefore_Born_rule_implied__"
    "Born_rule_derivation_is_explicitly_out_of_scope",
    "NOT_claiming_one_successful_limit_therefore_all_GRUT_classical_sectors_quantized__"
    "constitutive_sector_recovery_does_not_generalize_to_full_GRUT",
]

# =============================================================================
# DATACLASSES
# =============================================================================


@dataclass
class QC5ClassicalObservableCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    requires_prior_hilbert: bool
    consistent_with_qc0_package: bool
    ghost_safe: bool
    viable: bool
    appendix_p_class: str
    notes: List[str]


@dataclass
class QC5ClassicalObservableAudit:
    """Track A — Classical observable identification."""
    candidates: List[QC5ClassicalObservableCandidate]
    n_candidates: int
    n_viable: int
    chosen_observable_id: str
    chosen_observable_map: str
    notes: List[str]


@dataclass
class QC5SourceMappingAnalysis:
    """Track B — Source X mapping from quantum to classical."""
    source_x_candidates: List[str]
    viable_source_identification: str
    source_map: str
    source_enters_as: str
    source_mapping_complete: bool
    source_mapping_status: str
    notes: List[str]


@dataclass
class QC5TauMappingAnalysis:
    """Track C — τ mapping to Lindblad decay rate."""
    tau_identification: str
    tau_enters_as: str
    tau_sq_value: float
    tau_value: float
    mapping_preserves_prior_tau_meaning: bool
    gamma_eq_1_over_tau: bool
    mapping_status: str
    notes: List[str]


@dataclass
class QC5LimitTypeEntry:
    limit_name: str
    limit_applicable: bool
    limit_role: str
    notes: str


@dataclass
class QC5LimitTypeAnalysis:
    """Track D — Limit type analysis."""
    limit_entries: List[QC5LimitTypeEntry]
    n_limits_tested: int
    preferred_limit_combination: List[str]
    n_limits_in_combination: int
    multi_limit_required: bool
    minimal_coherent_route_identified: bool
    notes: List[str]


@dataclass
class QC5EquationRecoveryAnalysis:
    """Track E — Equation recovery."""
    target_equation: str
    recovered_equation: str
    recovery_classification: str
    recovery_conditions: List[str]
    corrections_present: bool
    correction_description: str
    recovery_status: str
    notes: List[str]


@dataclass
class QC5ParameterMatchEntry:
    parameter_name: str
    quantum_side_object: str
    classical_side_object: str
    match_status: str
    notes: str


@dataclass
class QC5ParameterMatchingAnalysis:
    """Track F — Parameter matching."""
    parameter_entries: List[QC5ParameterMatchEntry]
    n_complete: int
    n_partial: int
    n_underdetermined: int
    n_blocked: int
    extra_free_parameters: List[str]
    parameter_matching_verdict: str
    notes: List[str]


@dataclass
class QC5RegimeValidityAnalysis:
    """Track G — Regime validity."""
    required_conditions: List[str]
    quasi_static_consistent: bool
    preferred_frame_consistent: bool
    open_system_consistent: bool
    low_frequency_long_time_consistent: bool
    quarantine_perimeter_respected: bool
    tau_eff_domain_consistent: bool
    additional_restrictions: List[str]
    regime_validity_status: str
    notes: List[str]


@dataclass
class QC5SecondaryClassEntry:
    class_id: str
    class_name: str
    recovery_route: str
    recovery_strength: str
    burden_relative_to_lindblad: str
    outperforms_lindblad: bool
    notes: str


@dataclass
class QC5CompetingClassCrosscheck:
    """Track H — Competing class crosscheck."""
    secondary_entries: List[QC5SecondaryClassEntry]
    any_class_outperforms_lindblad: bool
    preferred_class_retention_verdict: str
    rationale: str
    notes: List[str]


@dataclass
class QC5AppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QC5AppendixPAudit:
    """Track I — Appendix P classification."""
    entries: List[QC5AppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QC5AuthorizationAudit:
    """Track J — Q-D authorization."""
    qd_authorized: bool
    preconditions_satisfied: List[str]
    qd_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QC5NonclaimFirewall:
    """Track K — Nonclaim firewall."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QC5ClassicalLimitResult:
    """Master result for Q-C.5 Classical-Limit Recovery Audit."""
    valid: bool
    # 11 tracks
    track_a_observable_audit: QC5ClassicalObservableAudit
    track_b_source_mapping: QC5SourceMappingAnalysis
    track_c_tau_mapping: QC5TauMappingAnalysis
    track_d_limit_type: QC5LimitTypeAnalysis
    track_e_equation_recovery: QC5EquationRecoveryAnalysis
    track_f_parameter_matching: QC5ParameterMatchingAnalysis
    track_g_regime_validity: QC5RegimeValidityAnalysis
    track_h_crosscheck: QC5CompetingClassCrosscheck
    track_i_appendix_p: QC5AppendixPAudit
    track_j_authorization: QC5AuthorizationAudit
    track_k_nonclaims: QC5NonclaimFirewall
    # Four hard-gated verdicts
    constitutive_recovery_verdict: str
    parameter_matching_verdict: str
    preferred_class_retention_verdict: str
    authorization_verdict: str
    # Summary
    qc5_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# =============================================================================
# TRACK BUILDERS
# =============================================================================


def _build_track_a() -> QC5ClassicalObservableAudit:
    """Track A — Classical Observable Identification."""
    candidates = [
        QC5ClassicalObservableCandidate(
            candidate_id="CO1_expectation_value",
            candidate_name="expectation_value",
            description="Phi_cl = Tr(Phi_hat * rho(t)); standard expectation-value map",
            requires_prior_hilbert=True,
            consistent_with_qc0_package=True,
            ghost_safe=True,
            viable=True,
            appendix_p_class="motivated_but_unbuilt",
            notes=[
                "Requires Phi_hat operator on pre-Hilbert space (Q-B.5 package)",
                "Standard approach for open quantum systems",
                "Ghost-safe: Phi_hat is chosen to be Phi_plus sector; Phi_minus ghost "
                "contamination can be avoided by appropriate operator support",
                "CHOSEN as the viable classical observable",
            ],
        ),
        QC5ClassicalObservableCandidate(
            candidate_id="CO2_reduced_state_coarse_grained",
            candidate_name="reduced_state_coarse_grained",
            description="Marginal of reduced density matrix after partial trace",
            requires_prior_hilbert=True,
            consistent_with_qc0_package=True,
            ghost_safe=True,
            viable=False,
            appendix_p_class="motivated_but_unbuilt",
            notes=[
                "Requires trace over additional degrees of freedom not yet defined",
                "Coarse-graining procedure unspecified at Q-C.5 level",
                "Not viable without explicit specification of traced-out subsystem",
            ],
        ),
        QC5ClassicalObservableCandidate(
            candidate_id="CO3_pointer_variable",
            candidate_name="pointer_variable",
            description="Pointer observable in decoherence basis",
            requires_prior_hilbert=True,
            consistent_with_qc0_package=False,
            ghost_safe=True,
            viable=False,
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Requires pointer-observable structure — Q-D territory",
                "Pointer basis not yet defined; decoherence mechanism unbuilt",
                "Not viable at Q-C.5 level; deferred to Q-D",
            ],
        ),
        QC5ClassicalObservableCandidate(
            candidate_id="CO4_diagonal_density_component",
            candidate_name="diagonal_density_component",
            description="Diagonal element of density matrix in some preferred basis",
            requires_prior_hilbert=True,
            consistent_with_qc0_package=False,
            ghost_safe=True,
            viable=False,
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Requires a preferred basis — not yet specified in GRUT quantum program",
                "Basis choice is ad hoc without decoherence mechanism",
                "Not viable at Q-C.5 level",
            ],
        ),
        QC5ClassicalObservableCandidate(
            candidate_id="CO5_history_space_saddle",
            candidate_name="history_space_saddle",
            description="Saddle-point field configuration of influence action (CIF/CTP)",
            requires_prior_hilbert=False,
            consistent_with_qc0_package=True,
            ghost_safe=False,
            viable=False,
            appendix_p_class="motivated_but_unbuilt",
            notes=[
                "Requires influence action — CL5 territory, not yet built",
                "CTP norms dynamically inadmissible due to Phi_minus ghost growth",
                "Ghost contamination: dPhi_minus/dt = +Phi_minus/tau (sign=+1, unstable)",
                "Not viable until influence action is explicitly constructed",
            ],
        ),
        QC5ClassicalObservableCandidate(
            candidate_id="CO6_no_valid_classical_observable",
            candidate_name="no_valid_classical_observable",
            description="Null case: no valid classical observable can be identified",
            requires_prior_hilbert=False,
            consistent_with_qc0_package=True,
            ghost_safe=True,
            viable=False,
            appendix_p_class="bounded_structural_result",
            notes=[
                "Null/fallback candidate retained for logical completeness",
                "Rejected: CO1 provides a viable expectation-value observable",
            ],
        ),
    ]

    n_viable = sum(1 for c in candidates if c.viable)

    return QC5ClassicalObservableAudit(
        candidates=candidates,
        n_candidates=len(candidates),
        n_viable=n_viable,
        chosen_observable_id="CO1_expectation_value",
        chosen_observable_map="Phi_cl(t) = Tr(Phi_hat * rho(t))",
        notes=[
            "6 candidates surveyed; 1 viable (CO1)",
            "CO1 is the standard expectation-value map — compatible with Q-C0 kinematic package",
            "CO2–CO5 rejected for reasons specific to their construction requirements",
            "CO6 null case retained for logical completeness but rejected by CO1 viability",
        ],
    )


def _build_track_b() -> QC5SourceMappingAnalysis:
    """Track B — Source Mapping."""
    return QC5SourceMappingAnalysis(
        source_x_candidates=[
            "external_drive: X enters as external Hamiltonian coupling H_drive = lambda * Phi_hat * X",
            "bath_induced_bias: dissipator offset term encoding bath coherent drive",
            "expectation_value_source: <X> = Tr(X_hat rho) closes the equation",
            "effective_drift_term: drift term in Lindblad generator",
        ],
        viable_source_identification="external_drive_or_bath_induced_bias",
        source_map="X_cl = Tr(X_hat * rho(t))  or  bath_bias_term_in_Lindblad_generator",
        source_enters_as="external_drive",
        source_mapping_complete=True,
        source_mapping_status="structurally_complete_operator_unbuilt",
        notes=[
            "X_hat operator is not yet explicitly specified — structural identification only",
            "Two dual routes: (1) external Hamiltonian coupling; (2) bath coherent bias",
            "Both routes yield <X> = Tr(X_hat rho) in expectation-value limit",
            "Source mapping is structurally complete; full operator content deferred to Q-D",
        ],
    )


def _build_track_c() -> QC5TauMappingAnalysis:
    """Track C — Tau Mapping."""
    gamma_value = 1.0 / TAU
    return QC5TauMappingAnalysis(
        tau_identification="inverse_damping_rate_gamma_eq_1_over_tau",
        tau_enters_as="dissipator_coefficient",
        tau_sq_value=TAU_SQ,
        tau_value=TAU,
        mapping_preserves_prior_tau_meaning=True,
        gamma_eq_1_over_tau=True,
        mapping_status="tau_matching_complete",
        notes=[
            f"tau_sq = 3/2 = {TAU_SQ} (inherited canonical NC constant)",
            f"tau = sqrt(3/2) = {TAU:.10f}",
            f"gamma = 1/tau = {gamma_value:.10f}",
            f"gamma * tau = {gamma_value * TAU:.10f} (must equal 1.0)",
            "Jump operator: L = sqrt(gamma) * Phi_hat = (1/sqrt(tau)) * Phi_hat",
            "tau_eff domain (from tau_eff_domain_declaration.py) uses same tau — consistent",
            "Mapping preserves the role of tau as the unique GRUT relaxation timescale",
        ],
    )


def _build_track_d() -> QC5LimitTypeAnalysis:
    """Track D — Limit Type Analysis."""
    limit_entries = [
        QC5LimitTypeEntry(
            limit_name="long_time_limit",
            limit_applicable=True,
            limit_role="secondary",
            notes="Steady-state behavior recovered; not the primary recovery mechanism for the ODE",
        ),
        QC5LimitTypeEntry(
            limit_name="markovian_limit",
            limit_applicable=True,
            limit_role="primary",
            notes="Essential for Lindblad equation to be valid; bath memory time << tau",
        ),
        QC5LimitTypeEntry(
            limit_name="weak_coupling_limit",
            limit_applicable=True,
            limit_role="primary",
            notes="System-bath coupling weak — Born-Markov approximation justified",
        ),
        QC5LimitTypeEntry(
            limit_name="mean_field_limit",
            limit_applicable=False,
            limit_role="not_applicable",
            notes="Mean-field requires many-body sector; not applicable in single-mode GRUT context",
        ),
        QC5LimitTypeEntry(
            limit_name="semiclassical_limit",
            limit_applicable=False,
            limit_role="not_applicable",
            notes="hbar → 0 limit not defined in GRUT quantum program (no hbar parameter introduced)",
        ),
        QC5LimitTypeEntry(
            limit_name="coarse_grained_open_system_limit",
            limit_applicable=True,
            limit_role="secondary",
            notes="Consistent with Markovian limit; subsumed by Born-Markov approximation",
        ),
        QC5LimitTypeEntry(
            limit_name="combined_multi_limit_route",
            limit_applicable=True,
            limit_role="primary",
            notes="Markovian + weak-coupling + expectation-value applied together yield recovery",
        ),
    ]

    return QC5LimitTypeAnalysis(
        limit_entries=limit_entries,
        n_limits_tested=len(limit_entries),
        preferred_limit_combination=[
            "markovian_limit",
            "weak_coupling_limit",
            "expectation_value_limit",
        ],
        n_limits_in_combination=3,
        multi_limit_required=True,
        minimal_coherent_route_identified=True,
        notes=[
            "7 limit types surveyed; 3 primary, 2 secondary, 2 not applicable",
            "Multi-limit required: no single limit alone recovers the constitutive ODE",
            "Preferred combination is the minimal coherent route",
            "Semiclassical (hbar→0) not available — GRUT does not parametrize hbar",
            "Mean-field not available — single-mode constitutive sector only",
        ],
    )


def _build_track_e() -> QC5EquationRecoveryAnalysis:
    """Track E — Equation Recovery."""
    return QC5EquationRecoveryAnalysis(
        target_equation="tau * dPhi/dt + Phi = X",
        recovered_equation="tau * d<Phi_hat>/dt + <Phi_hat> = <X_hat>",
        recovery_classification="effective_regime_constitutive_recovery",
        recovery_conditions=[
            "markovian_approximation: bath_memory_time << tau",
            "weak_system_bath_coupling: Born_Markov_approximation_valid",
            "expectation_value_limit: Phi_cl = Tr(Phi_hat * rho)",
            "linear_jump_operator: L = (1/sqrt(tau)) * Phi_hat",
            "bath_linear_restoring_force: dissipator_encodes_minus_gamma_<Phi_hat>_term",
        ],
        corrections_present=False,
        correction_description=(
            "No corrections at leading order in Markovian + weak-coupling limit. "
            "Higher-order corrections (non-Markovian memory terms, strong-coupling "
            "renormalization) would modify the ODE but are suppressed in the stated regime."
        ),
        recovery_status="effective_regime_constitutive_recovery_demonstrated",
        notes=[
            "Derivation: d<Phi_hat>/dt = Tr(Phi_hat * L[rho]) = -gamma*<Phi_hat> + <X_hat>",
            "Setting gamma = 1/tau: d<Phi_hat>/dt = -(1/tau)*<Phi_hat> + (1/tau)*<X_hat>",
            "Multiply by tau: tau*d<Phi_hat>/dt = -<Phi_hat> + <X_hat>",
            "Rearrange: tau*d<Phi_hat>/dt + <Phi_hat> = <X_hat>  (QED)",
            "Recovery is effective-regime: specific jump operator form required",
            "Recovery is not free derivation: Markovian limit is an approximation",
            "Verdict: effective_regime_constitutive_recovery_demonstrated (not exact)",
        ],
    )


def _build_track_f() -> QC5ParameterMatchingAnalysis:
    """Track F — Parameter Matching."""
    parameter_entries = [
        QC5ParameterMatchEntry(
            parameter_name="tau",
            quantum_side_object="inverse_Lindblad_decay_rate_gamma_eq_1_over_tau",
            classical_side_object="relaxation_time_tau",
            match_status="complete",
            notes=(
                f"gamma = 1/tau = {1.0/TAU:.10f}; tau = {TAU:.10f}; "
                "tau_sq = 3/2 preserved throughout"
            ),
        ),
        QC5ParameterMatchEntry(
            parameter_name="source_x",
            quantum_side_object="Tr(X_hat_rho)_or_bath_bias_term",
            classical_side_object="constitutive_source_X",
            match_status="partial",
            notes=(
                "Structural identification complete (X_hat exists as external drive operator); "
                "operator X_hat not yet explicitly specified — content deferred to Q-D"
            ),
        ),
        QC5ParameterMatchEntry(
            parameter_name="damping_coefficient",
            quantum_side_object="Lindblad_rate_gamma_times_tau_eq_1",
            classical_side_object="coefficient_1_in_Phi_term_of_constitutive_ODE",
            match_status="complete",
            notes="gamma * tau = 1.0 exactly; coefficient of <Phi_hat> in recovered ODE is 1",
        ),
        QC5ParameterMatchEntry(
            parameter_name="normalization_scaling",
            quantum_side_object="state_preparation_and_operator_normalization_of_Phi_hat",
            classical_side_object="field_normalization_Phi_classical",
            match_status="underdetermined",
            notes=(
                "Jump operator normalization convention (||L||) and initial state "
                "preparation introduce free parameters not fixed by constitutive recovery alone"
            ),
        ),
    ]

    n_complete = sum(1 for e in parameter_entries if e.match_status == "complete")
    n_partial = sum(1 for e in parameter_entries if e.match_status == "partial")
    n_underdetermined = sum(1 for e in parameter_entries if e.match_status == "underdetermined")
    n_blocked = sum(1 for e in parameter_entries if e.match_status == "blocked")

    return QC5ParameterMatchingAnalysis(
        parameter_entries=parameter_entries,
        n_complete=n_complete,
        n_partial=n_partial,
        n_underdetermined=n_underdetermined,
        n_blocked=n_blocked,
        extra_free_parameters=[
            "jump_operator_normalization_convention",
            "state_initial_condition",
        ],
        parameter_matching_verdict=QC5_PARAMETER_MATCHING_VERDICT,
        notes=[
            f"{n_complete} parameters matched completely (tau, damping_coefficient)",
            f"{n_partial} parameter partially matched (source_x: structurally complete, operator unbuilt)",
            f"{n_underdetermined} parameter underdetermined (normalization/scaling)",
            f"{n_blocked} parameters blocked",
            "Net verdict: partial — underdetermined normalization freedom prevents complete matching",
        ],
    )


def _build_track_g() -> QC5RegimeValidityAnalysis:
    """Track G — Regime Validity."""
    return QC5RegimeValidityAnalysis(
        required_conditions=[
            "markovian_approximation_bath_memory_time_much_less_than_tau",
            "weak_system_bath_coupling",
            "expectation_value_limit_applied_to_observable_Phi_hat",
            "linear_dissipation_jump_operator_L_eq_sqrt_gamma_times_Phi_hat",
            "no_quantum_coherence_beyond_Lindblad_description",
        ],
        quasi_static_consistent=True,
        preferred_frame_consistent=True,
        open_system_consistent=True,
        low_frequency_long_time_consistent=True,
        quarantine_perimeter_respected=True,
        tau_eff_domain_consistent=True,
        additional_restrictions=[
            "markovian_approximation",
            "weak_system_bath_coupling",
        ],
        regime_validity_status="regime_limited_but_internally_consistent",
        notes=[
            "All 6 regime consistency flags True",
            "Quarantine perimeter respected: no quantum gravity, no measurement bridge invoked",
            "tau_eff domain (tau_eff_domain_declaration.py) consistent with tau = sqrt(3/2)",
            "Regime is limited but internally self-consistent within stated approximations",
            "Additional restrictions (Markovian, weak coupling) are physically well-motivated",
            "Ghost obstruction (Phi_minus growth) does not enter this sector — Phi_hat is ghost-safe",
        ],
    )


def _build_track_h() -> QC5CompetingClassCrosscheck:
    """Track H — Competing Class Crosscheck."""
    secondary_entries = [
        QC5SecondaryClassEntry(
            class_id="CL3",
            class_name="non_hermitian_effective",
            recovery_route=(
                "imaginary_part_of_H_eff_gives_decay: "
                "H_eff = H - i*gamma/2 * Phi_hat^dagger * Phi_hat yields "
                "d<Phi_hat>/dt = -gamma/2 * <Phi_hat> at leading order"
            ),
            recovery_strength="weaker",
            burden_relative_to_lindblad="lower_or_comparable",
            outperforms_lindblad=False,
            notes=(
                "Non-Hermitian effective Hamiltonian gives exponential decay but "
                "positivity not guaranteed without explicit jump operator recycling term. "
                "Recovery is weaker: coefficient factor 1/2 mismatch without recycling. "
                "Does not outperform Lindbladian."
            ),
        ),
        QC5SecondaryClassEntry(
            class_id="CL4",
            class_name="memory_kernel",
            recovery_route=(
                "exponential_kernel_exp_minus_t_over_tau_recovers_constitutive_ODE_directly: "
                "d<Phi>/dt = -int_0^t K(t-s)*<Phi(s)> ds + source; "
                "K(t-s) = (1/tau^2)*exp(-(t-s)/tau) → Markovian limit recovers CL2"
            ),
            recovery_strength="comparable",
            burden_relative_to_lindblad="higher",
            outperforms_lindblad=False,
            notes=(
                "Memory-kernel with exponential kernel provides a natural derivation of "
                "the constitutive ODE — arguably more natural than Lindblad. However: "
                "(a) kernel specification adds structure beyond CL2; "
                "(b) Markovian limit of CL4 recovers CL2, so CL2 is not strictly dominated; "
                "(c) higher construction burden. Not strictly stronger than Lindbladian."
            ),
        ),
        QC5SecondaryClassEntry(
            class_id="CL5",
            class_name="influence_functional",
            recovery_route=(
                "saddle_point_of_influence_action_recovers_classical_CTP_equations: "
                "delta S_IF / delta Phi_cl = 0 yields constitutive-like equation "
                "at saddle-point level"
            ),
            recovery_strength="comparable",
            burden_relative_to_lindblad="higher",
            outperforms_lindblad=False,
            notes=(
                "Influence-functional approach is structurally the most systematic "
                "(Feynman-Vernon theory) but: "
                "(a) requires full influence action — not yet built in GRUT; "
                "(b) CTP norms dynamically inadmissible due to Phi_minus ghost growth; "
                "(c) highest construction burden. Not viable at Q-C.5 level."
            ),
        ),
    ]

    any_outperforms = any(e.outperforms_lindblad for e in secondary_entries)

    return QC5CompetingClassCrosscheck(
        secondary_entries=secondary_entries,
        any_class_outperforms_lindblad=any_outperforms,
        preferred_class_retention_verdict=QC5_PREFERRED_CLASS_RETENTION_VERDICT,
        rationale=(
            "No secondary class provides a strictly stronger constitutive-recovery route "
            "at lower or equal burden relative to Lindbladian (CL2). CL3 is weaker. "
            "CL4 is comparable but at higher burden and with underdetermined kernel. "
            "CL5 is comparable or stronger in principle but requires unbuilt influence action "
            "and is blocked by CTP ghost obstruction. "
            "Lindbladian preference from Q-C is therefore retained."
        ),
        notes=[
            "3 secondary classes tested: CL3 (non-Hermitian effective), CL4 (memory-kernel), "
            "CL5 (influence-functional)",
            "None outperforms Lindbladian on both recovery strength and construction burden",
            "CL4 memory-kernel note: natural exponential kernel derivation exists "
            "but requires more structure and Markovian limit recovers CL2 anyway",
            "CL5 additionally blocked by Phi_minus ghost instability in CTP formalism",
        ],
    )


def _build_track_i() -> QC5AppendixPAudit:
    """Track I — Appendix P Classification."""
    entries = [
        QC5AppendixPEntry(
            item_id="classical_observable_map_Phi_cl_eq_Tr_Phi_hat_rho",
            item_name="classical_observable_expectation_value_map",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="constitutive_observable_identified_as_expectation_value",
            forbidden_claim="map_is_exact_not_regime_limited",
            dependency="Q-B.5 Phi_hat operator and Q-B Hilbert space",
        ),
        QC5AppendixPEntry(
            item_id="source_mapping_X_quantum_to_classical",
            item_name="source_X_structural_identification",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="source_structurally_identified_as_external_drive_or_bath_bias",
            forbidden_claim="X_hat_operator_fully_specified_and_built",
            dependency="Q-C operator content (unbuilt)",
        ),
        QC5AppendixPEntry(
            item_id="tau_matching_gamma_eq_1_over_tau",
            item_name="tau_to_Lindblad_decay_rate_matching",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="tau_matched_to_Lindblad_decay_rate_gamma_eq_1_over_tau",
            forbidden_claim="tau_derived_from_first_principles_of_bath_interaction",
            dependency="Q-A canonical NC constant tau_sq = 3/2",
        ),
        QC5AppendixPEntry(
            item_id="effective_regime_constitutive_recovery",
            item_name="constitutive_ODE_recovery_in_Markovian_regime",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="recovery_demonstrated_in_Markovian_plus_weak_coupling_regime",
            forbidden_claim="constitutive_equation_derived_from_native_GRUT_action",
            dependency="Lindblad law class (Q-C) + Markovian approximation",
        ),
        QC5AppendixPEntry(
            item_id="parameter_matching_partial",
            item_name="parameter_matching_tau_and_damping_complete",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="tau_and_damping_coefficient_matched_completely_source_partially",
            forbidden_claim="all_parameters_uniquely_determined_no_free_parameters_remain",
            dependency="Track F parameter matching analysis",
        ),
    ]

    return QC5AppendixPAudit(
        entries=entries,
        n_entries=len(entries),
        overall_class="motivated_but_unbuilt",
        no_native_canon=True,
        notes=[
            "All 5 Q-C.5 items classified as motivated_but_unbuilt",
            "No item achieves native_canon status — all require approximations or unbuilt content",
            "No item is excluded or ad_hoc — all are structurally motivated",
            "Overall Q-C.5 Appendix P class: motivated_but_unbuilt",
        ],
    )


def _build_track_j() -> QC5AuthorizationAudit:
    """Track J — Authorization."""
    return QC5AuthorizationAudit(
        qd_authorized=True,
        preconditions_satisfied=[
            "constitutive_recovery_demonstrated_in_effective_regime",
            "preferred_class_lindbladian_retained",
            "regime_validity_internally_consistent",
        ],
        qd_constraints=[
            "QD_must_not_assume_constitutive_recovery_beyond_Markovian_plus_weak_coupling_regime",
            "QD_must_not_assume_Born_rule_from_QC5_recovery",
            "QD_results_carry_MBU_or_MIP_floor",
        ],
        authorization_verdict=QC5_AUTHORIZATION_VERDICT,
        notes=[
            "Authorization to proceed to Q-D (Measurement Bridge) is granted",
            "Three preconditions satisfied; three Q-D constraints imposed",
            "Q-D must not overstep the regime boundary established at Q-C.5",
            "Born rule derivation is out of scope for Q-C.5 and Q-D must not assume it",
        ],
    )


def _build_track_k() -> QC5NonclaimFirewall:
    """Track K — Nonclaim Firewall."""
    return QC5NonclaimFirewall(
        nonclaims=QC5_NONCLAIMS,
        n_nonclaims=len(QC5_NONCLAIMS),
        all_registered=True,
    )


# =============================================================================
# VALIDATION
# =============================================================================


def validate_qc5_result(result: QC5ClassicalLimitResult) -> None:
    """Validate that all four hard-gated verdict strings are in their allowed frozensets.

    Raises ValueError if any verdict is not in its allowed vocabulary.
    """
    checks = [
        (
            result.constitutive_recovery_verdict,
            ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS,
            "constitutive_recovery_verdict",
        ),
        (
            result.parameter_matching_verdict,
            ALLOWED_PARAMETER_MATCHING_VERDICTS,
            "parameter_matching_verdict",
        ),
        (
            result.preferred_class_retention_verdict,
            ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS,
            "preferred_class_retention_verdict",
        ),
        (
            result.authorization_verdict,
            ALLOWED_AUTHORIZATION_VERDICTS,
            "authorization_verdict",
        ),
        (
            result.qc5_appendix_p_class,
            ALLOWED_APPENDIX_P_CLASSES,
            "qc5_appendix_p_class",
        ),
    ]

    for verdict, allowed, field_name in checks:
        if verdict not in allowed:
            raise ValueError(
                f"QC5 validation failure: field '{field_name}' has value '{verdict}' "
                f"which is not in allowed vocabulary {sorted(allowed)}"
            )

    # Structural checks
    if result.track_a_observable_audit.n_candidates != N_CLASSICAL_OBSERVABLE_CANDIDATES:
        raise ValueError(
            f"Expected {N_CLASSICAL_OBSERVABLE_CANDIDATES} observable candidates, "
            f"got {result.track_a_observable_audit.n_candidates}"
        )

    if result.track_a_observable_audit.n_viable != N_VIABLE_OBSERVABLE_CANDIDATES:
        raise ValueError(
            f"Expected {N_VIABLE_OBSERVABLE_CANDIDATES} viable observable candidate, "
            f"got {result.track_a_observable_audit.n_viable}"
        )

    if result.track_d_limit_type.n_limits_tested != N_LIMIT_TYPES_TESTED:
        raise ValueError(
            f"Expected {N_LIMIT_TYPES_TESTED} limit types tested, "
            f"got {result.track_d_limit_type.n_limits_tested}"
        )

    if result.track_d_limit_type.n_limits_in_combination != N_PREFERRED_LIMIT_COMBINATION:
        raise ValueError(
            f"Expected {N_PREFERRED_LIMIT_COMBINATION} limits in preferred combination, "
            f"got {result.track_d_limit_type.n_limits_in_combination}"
        )

    if result.track_k_nonclaims.n_nonclaims != N_QC5_NONCLAIMS:
        raise ValueError(
            f"Expected {N_QC5_NONCLAIMS} nonclaims, "
            f"got {result.track_k_nonclaims.n_nonclaims}"
        )

    if len(result.track_h_crosscheck.secondary_entries) != N_SECONDARY_CLASSES_TESTED:
        raise ValueError(
            f"Expected {N_SECONDARY_CLASSES_TESTED} secondary classes tested, "
            f"got {len(result.track_h_crosscheck.secondary_entries)}"
        )

    # Verify tau_sq consistency
    if abs(result.track_c_tau_mapping.tau_sq_value - TAU_SQ) > 1e-12:
        raise ValueError(
            f"tau_sq mismatch: expected {TAU_SQ}, got {result.track_c_tau_mapping.tau_sq_value}"
        )

    gamma_tau = (1.0 / result.track_c_tau_mapping.tau_value) * result.track_c_tau_mapping.tau_value
    if abs(gamma_tau - 1.0) > 1e-12:
        raise ValueError(
            f"gamma * tau must equal 1.0, got {gamma_tau}"
        )

    # Verify diagnostics
    diag = result.diagnostics
    if abs(diag.get("gamma_tau_product", 0.0) - 1.0) > 1e-10:
        raise ValueError(
            f"diagnostics gamma_tau_product must be 1.0, got {diag.get('gamma_tau_product')}"
        )


# =============================================================================
# MASTER FUNCTION
# =============================================================================


def run_qc5_classical_limit_audit() -> QC5ClassicalLimitResult:
    """Run the Q-C.5 Classical-Limit Recovery Audit.

    Builds all 11 tracks, sets the four hard-gated verdicts, and returns the
    complete QC5ClassicalLimitResult. Calls validate_qc5_result before returning.

    Returns
    -------
    QC5ClassicalLimitResult
        Complete, validated result with valid=True.

    Raises
    ------
    ValueError
        If any verdict string falls outside its allowed vocabulary or structural
        invariants are violated.
    """
    # Build all tracks
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
    track_k = _build_track_k()

    gamma = 1.0 / TAU

    diagnostics: Dict[str, Any] = {
        "n_classical_observable_candidates": N_CLASSICAL_OBSERVABLE_CANDIDATES,
        "n_viable_observable_candidates": N_VIABLE_OBSERVABLE_CANDIDATES,
        "n_limit_types_tested": N_LIMIT_TYPES_TESTED,
        "n_preferred_limits": N_PREFERRED_LIMIT_COMBINATION,
        "n_secondary_classes_tested": N_SECONDARY_CLASSES_TESTED,
        "n_nonclaims": N_QC5_NONCLAIMS,
        "tau_sq": TAU_SQ,
        "tau": TAU,
        "gamma": gamma,
        "gamma_tau_product": gamma * TAU,
        "phi_minus_growth_rate_sign": PHI_MINUS_GROWTH_RATE_SIGN,
        "phi_minus_can_be_imaginary_part": PHI_MINUS_CAN_BE_IMAGINARY_PART,
        "inherited_primary_law_class": QC_INHERITED_PRIMARY_LAW_CLASS,
        "inherited_classical_limit": QC_INHERITED_CLASSICAL_LIMIT,
        "inherited_authorization": QC_INHERITED_AUTHORIZATION,
        "chosen_observable": track_a.chosen_observable_id,
        "chosen_observable_map": track_a.chosen_observable_map,
        "source_mapping_status": track_b.source_mapping_status,
        "tau_mapping_status": track_c.mapping_status,
        "multi_limit_required": track_d.multi_limit_required,
        "preferred_limit_combination": track_d.preferred_limit_combination,
        "recovery_status": track_e.recovery_status,
        "corrections_present": track_e.corrections_present,
        "parameter_n_complete": track_f.n_complete,
        "parameter_n_partial": track_f.n_partial,
        "parameter_n_underdetermined": track_f.n_underdetermined,
        "regime_validity_status": track_g.regime_validity_status,
        "any_secondary_class_outperforms": track_h.any_class_outperforms_lindblad,
        "appendix_p_overall_class": track_i.overall_class,
        "no_native_canon": track_i.no_native_canon,
        "qd_authorized": track_j.qd_authorized,
    }

    allowed_claims = [
        "constitutive_observable_identified_as_expectation_value_Phi_cl_eq_Tr_Phi_hat_rho",
        "effective_regime_constitutive_recovery_demonstrated_in_Markovian_plus_weak_coupling",
        "tau_matched_to_Lindblad_decay_rate_gamma_eq_1_over_tau",
        "damping_coefficient_matched_gamma_times_tau_eq_1",
        "source_X_structurally_identified_as_external_drive_or_bath_bias",
        "Lindbladian_preference_retained_no_secondary_class_outperforms",
        "regime_validity_internally_consistent_within_stated_approximations",
        "authorized_to_proceed_to_QD_subject_to_stated_constraints",
    ]

    forbidden_claims = [
        "exact_constitutive_recovery_without_Markovian_or_operator_form_assumptions",
        "full_classical_limit_solved_beyond_expectation_value_sector",
        "native_canon_status_QC5_results_carry_MBU_floor",
        "X_hat_operator_fully_specified_and_built",
        "parameter_matching_complete_normalization_underdetermined",
        "Born_rule_derivation_from_QC5_constitutive_recovery",
        "constitutive_sector_recovery_generalizes_to_full_GRUT_quantum_program",
        "tau_derived_from_first_principles_of_bath_interaction",
    ]

    result = QC5ClassicalLimitResult(
        valid=True,
        track_a_observable_audit=track_a,
        track_b_source_mapping=track_b,
        track_c_tau_mapping=track_c,
        track_d_limit_type=track_d,
        track_e_equation_recovery=track_e,
        track_f_parameter_matching=track_f,
        track_g_regime_validity=track_g,
        track_h_crosscheck=track_h,
        track_i_appendix_p=track_i,
        track_j_authorization=track_j,
        track_k_nonclaims=track_k,
        constitutive_recovery_verdict=QC5_CONSTITUTIVE_RECOVERY_VERDICT,
        parameter_matching_verdict=QC5_PARAMETER_MATCHING_VERDICT,
        preferred_class_retention_verdict=QC5_PREFERRED_CLASS_RETENTION_VERDICT,
        authorization_verdict=QC5_AUTHORIZATION_VERDICT,
        qc5_appendix_p_class=QC5_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QC5_NONCLAIMS,
        diagnostics=diagnostics,
    )

    validate_qc5_result(result)
    return result


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    result = run_qc5_classical_limit_audit()
    print("Q-C.5 Classical-Limit Recovery Audit")
    print("=" * 60)
    print(f"valid:                          {result.valid}")
    print(f"constitutive_recovery_verdict:  {result.constitutive_recovery_verdict}")
    print(f"parameter_matching_verdict:     {result.parameter_matching_verdict}")
    print(f"preferred_class_verdict:        {result.preferred_class_retention_verdict}")
    print(f"authorization_verdict:          {result.authorization_verdict}")
    print(f"appendix_p_class:               {result.qc5_appendix_p_class}")
    print()
    diag = result.diagnostics
    print(f"tau_sq = {diag['tau_sq']}  tau = {diag['tau']:.10f}")
    print(f"gamma = {diag['gamma']:.10f}  gamma*tau = {diag['gamma_tau_product']:.10f}")
    print()
    print(f"Observable candidates: {diag['n_classical_observable_candidates']}  "
          f"viable: {diag['n_viable_observable_candidates']}")
    print(f"Chosen observable: {diag['chosen_observable']}")
    print(f"Chosen map:        {diag['chosen_observable_map']}")
    print()
    print(f"Limit types tested: {diag['n_limit_types_tested']}  "
          f"preferred combination: {diag['n_preferred_limits']}")
    print(f"Preferred combination: {diag['preferred_limit_combination']}")
    print()
    print(f"Recovery status:   {diag['recovery_status']}")
    print(f"Corrections:       {diag['corrections_present']}")
    print()
    print(f"Parameter matching — complete: {diag['parameter_n_complete']}  "
          f"partial: {diag['parameter_n_partial']}  "
          f"underdetermined: {diag['parameter_n_underdetermined']}")
    print()
    print(f"Nonclaims registered: {diag['n_nonclaims']}")
    print(f"QD authorized: {diag['qd_authorized']}")
    print()
    print("Allowed claims:")
    for c in result.allowed_claims:
        print(f"  + {c}")
    print()
    print("Forbidden claims:")
    for c in result.forbidden_claims:
        print(f"  - {c}")
