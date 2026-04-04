"""
Appendix Q-D — Decoherence and Measurement Bridge Audit
GRUT Quantum Program | Phase Q

PHYSICS DERIVATION — DECOHERENCE FROM LINDBLAD GENERATOR
=========================================================

Given Lindblad generator with L = (1/sqrt(tau)) * Phi_hat, gamma = 1/tau,
in eigenbasis of Phi_hat where Phi_hat|phi_n> = phi_n|phi_n>:

  <phi_m| [gamma(Phi_hat rho Phi_hat_dag - 1/2{Phi_hat_dag Phi_hat, rho})] |phi_n>
    = gamma[phi_m * phi_n * rho_mn - 1/2*(phi_m^2 + phi_n^2)*rho_mn]
    = -1/2 * gamma * (phi_m - phi_n)^2 * rho_mn

  Therefore: drho_mn/dt|_diss = -1/2 * gamma * (phi_m - phi_n)^2 * rho_mn

  Decoherence rate:      R_dec(Delta_phi) = Delta_phi^2 / (2*tau)
  Decoherence timescale: tau_dec(Delta_phi) = 2*tau / Delta_phi^2
  When Delta_phi = sqrt(2): tau_dec = tau  (decoherence on the constitutive relaxation timescale)

FIVE HARD-GATED VERDICTS
=========================

1. QD_DECOHERENCE_VERDICT = "effective_regime_decoherence_demonstrated"
   Rationale: Off-diagonal density-matrix elements decay at rate (phi_m - phi_n)^2/(2*tau)
   under the Lindblad master equation with L = Phi_hat/sqrt(tau). Demonstrated within the
   same Markovian + weak-coupling effective regime established in Q-C.5. Not exact
   (regime-limited), but structurally valid and internally consistent.

2. QD_POINTER_VERDICT = "pointer_basis_class_selected"
   Rationale: The Phi_hat-eigenbasis is identified as the pointer-basis class via two
   consistent routes: (PB1) zero decoherence rate for diagonal elements, (PB3) dynamical
   selection by the jump operator L prop Phi_hat. A unique basis within the class is not
   guaranteed because the spectrum of Phi_hat is unspecified and degeneracies are possible.
   One class is identified via two routes; count as 1 viable class.

3. QD_MEASUREMENT_SCOPE_VERDICT = "decoherence_plus_pointer_structure"
   Rationale: Measurement scope extends beyond decoherence-only by virtue of pointer-basis
   class identification, but does not reach partial-determination, full closure, or Born-rule
   weighting. Scope verdict is strictly the two levels achieved.

4. QD_OUTCOME_SELECTION_VERDICT = "born_rule_or_outcome_selection_not_natively_derived"
   Rationale: All four outcome-selection mechanisms (single-outcome selection, Born-rule
   probabilities, irreversible branch selection, observer-conditioned update) are absent
   from the audited structure. The Lindblad master equation is deterministic for rho;
   no stochastic or branch-selecting mechanism is embedded in the law class. All four
   absences are classified BSR (bounded structural result: documented absence, not
   permanent impossibility).

5. QD_AUTHORIZATION_VERDICT = "authorized_to_proceed_to_QE"
   Rationale: Decoherence + pointer-basis class constitute a sufficient structural
   foundation for Q-E benchmark toy-model work. Authorization is conditional: Q-E must
   not assume Born rule or outcome selection, must not assume full measurement closure,
   and all Q-E results inherit the MBU/MIP floor from Q-D.

AUDIT FRAMING NOTE
==================

GRUT's preferred open-system extension demonstrates effective-regime decoherence and a
pointer-basis class, while leaving outcome selection and Born-rule weighting unresolved.
The decoherence verdict must not be read as measurement-bridge solved.

The gap between "decoherence_plus_pointer_structure" and "full_measurement_closure" is a
documented, bounded structural result — not an oversight and not a permanent impossibility.
It is precisely what this appendix exists to record.
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
PHI_MINUS_GROWTH_RATE_SIGN: int = +1
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False

N_POINTER_BASIS_CANDIDATES: int = 5
N_VIABLE_POINTER_BASES: int = 1
N_OUTCOME_SELECTION_MECHANISMS: int = 4
N_OUTCOME_MECHANISMS_PRESENT: int = 0
N_QD_NONCLAIMS: int = 8

QC_INHERITED_LAW_CLASS: str = "lindbladian_like_law_preferred"
QC5_INHERITED_RECOVERY: str = "effective_regime_constitutive_recovery_demonstrated"
QC5_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QD"

QD_DECOHERENCE_VERDICT: str = "effective_regime_decoherence_demonstrated"
QD_POINTER_VERDICT: str = "pointer_basis_class_selected"
QD_MEASUREMENT_SCOPE_VERDICT: str = "decoherence_plus_pointer_structure"
QD_OUTCOME_SELECTION_VERDICT: str = "born_rule_or_outcome_selection_not_natively_derived"
QD_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QE"
QD_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

ALLOWED_DECOHERENCE_VERDICTS: frozenset = frozenset({
    "effective_regime_decoherence_demonstrated",
    "decoherence_structurally_plausible_but_unbuilt",
    "decoherence_blocked",
    "decoherence_underdetermined",
})
ALLOWED_POINTER_VERDICTS: frozenset = frozenset({
    "unique_pointer_basis_selected",
    "pointer_basis_class_selected",
    "pointer_basis_underdetermined",
    "pointer_basis_blocked",
})
ALLOWED_MEASUREMENT_SCOPE_VERDICTS: frozenset = frozenset({
    "decoherence_only",
    "decoherence_plus_pointer_structure",
    "decoherence_plus_partial_determination_structure",
    "full_measurement_closure_demonstrated",
    "measurement_scope_underdetermined",
})
ALLOWED_OUTCOME_SELECTION_VERDICTS: frozenset = frozenset({
    "born_rule_or_outcome_selection_not_natively_derived",
    "effective_outcome_tendency_only",
    "outcome_selection_structurally_plausible_but_unbuilt",
    "native_outcome_selection_demonstrated",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QE",
    "authorized_only_for_further_measurement_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_QC_or_QC5",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

QD_NONCLAIMS: List[str] = [
    "NOT_claiming_decoherence_therefore_collapse__"
    "off_diagonal_suppression_does_not_select_single_outcomes",
    "NOT_claiming_pointer_basis_therefore_Born_rule__"
    "basis_stability_does_not_yield_probability_weighting",
    "NOT_claiming_off_diagonal_suppression_therefore_single_outcome__"
    "decoherence_removes_interference_not_branches",
    "NOT_claiming_effective_regime_result_therefore_native_canon__"
    "all_QD_results_carry_MBU_floor_per_QA_R3",
    "NOT_claiming_constitutive_observable_recovery_therefore_full_measurement_solved__"
    "QC5_recovery_is_expectation_value_level_only",
    "NOT_claiming_Lindbladian_decoherence_therefore_observer_problem_solved__"
    "observer_problem_requires_outcome_selection_which_is_not_demonstrated",
    "NOT_claiming_open_system_dynamics_therefore_probabilities_derived__"
    "Born_rule_derivation_is_explicitly_out_of_scope",
    "NOT_claiming_basis_stability_therefore_ontology_fixed__"
    "pointer_basis_class_is_kinematic_not_ontological",
]

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QDDecoherenceAnalysis:
    off_diagonal_decay_rate_formula: str   # "0.5 * gamma * (phi_m - phi_n)**2"
    decoherence_basis: str                 # "eigenbasis_of_Phi_hat"
    decoherence_regime_conditions: List[str]
    decoherence_status: str                # "demonstrated_in_effective_regime"
    decoherence_verdict: str
    notes: List[str]


@dataclass
class QDPointerBasisCandidate:
    basis_id: str
    basis_name: str
    description: str
    viable: bool
    selection_mechanism: str
    appendix_p_class: str
    notes: List[str]


@dataclass
class QDPointerBasisAnalysis:
    candidates: List[QDPointerBasisCandidate]
    n_candidates: int
    n_viable: int
    chosen_pointer_basis_id: str
    chosen_pointer_basis_name: str
    unique_basis: bool
    pointer_verdict: str
    notes: List[str]


@dataclass
class QDTimescaleAnalysis:
    decoherence_rate_formula: str
    decoherence_timescale_formula: str
    timescale_governed_by: str
    tau_sq_value: float
    gamma_value: float
    characteristic_decoherence_timescale: str
    consistent_with_prior_timescales: bool
    notes: List[str]


@dataclass
class QDMeasurementBridgeEntry:
    level_name: str
    achieved: bool
    justification: str


@dataclass
class QDMeasurementBridgeAnalysis:
    entries: List[QDMeasurementBridgeEntry]
    decoherence_achieved: bool
    pointer_structure_achieved: bool
    partial_determination_achieved: bool
    full_measurement_achieved: bool
    born_rule_achieved: bool
    measurement_scope_verdict: str
    notes: List[str]


@dataclass
class QDOutcomeSelectionMechanism:
    mechanism_name: str
    present: bool
    obstruction_or_reason: str
    appendix_p_class: str


@dataclass
class QDOutcomeSelectionAnalysis:
    mechanisms: List[QDOutcomeSelectionMechanism]
    n_mechanisms: int
    n_present: int
    any_outcome_selection_present: bool
    outcome_selection_verdict: str
    notes: List[str]


@dataclass
class QDObservableClassicalityAnalysis:
    constitutive_observable: str
    pointer_observable: str
    same_observable: bool
    strength_of_identification: str
    classicality_verdict: str
    appendix_p_class: str
    notes: List[str]


@dataclass
class QDAppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QDAppendixPAudit:
    entries: List[QDAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QDAuthorizationAudit:
    qe_authorized: bool
    preconditions_satisfied: List[str]
    qe_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QDNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QDMeasurementBridgeResult:
    valid: bool
    track_a_decoherence: QDDecoherenceAnalysis
    track_b_pointer_basis: QDPointerBasisAnalysis
    track_c_timescale: QDTimescaleAnalysis
    track_d_measurement_bridge: QDMeasurementBridgeAnalysis
    track_e_outcome_selection: QDOutcomeSelectionAnalysis
    track_f_observable_classicality: QDObservableClassicalityAnalysis
    track_g_appendix_p: QDAppendixPAudit
    track_h_authorization: QDAuthorizationAudit
    track_i_nonclaims: QDNonclaimFirewall
    decoherence_verdict: str
    pointer_verdict: str
    measurement_scope_verdict: str
    outcome_selection_verdict: str
    authorization_verdict: str
    qd_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builder functions
# ---------------------------------------------------------------------------

def _build_track_a() -> QDDecoherenceAnalysis:
    """Track A: Decoherence from Lindblad generator."""
    return QDDecoherenceAnalysis(
        off_diagonal_decay_rate_formula="0.5 * gamma * (phi_m - phi_n)**2",
        decoherence_basis="eigenbasis_of_Phi_hat",
        decoherence_regime_conditions=[
            "markovian_approximation_bath_memory_time_much_less_than_tau",
            "weak_system_bath_coupling_Born_Markov_valid",
            "linear_jump_operator_L_eq_one_over_sqrt_tau_times_Phi_hat",
            "expectation_value_limit_already_established_in_QC5",
        ],
        decoherence_status="demonstrated_in_effective_regime",
        decoherence_verdict=QD_DECOHERENCE_VERDICT,
        notes=[
            "Derivation: <phi_m|gamma*(Phi_hat rho Phi_hat_dag - 1/2{Phi_hat_dag Phi_hat, rho})|phi_n>",
            "= gamma * [phi_m * phi_n * rho_mn - 1/2*(phi_m^2 + phi_n^2)*rho_mn]",
            "= -1/2 * gamma * (phi_m - phi_n)^2 * rho_mn",
            "Off-diagonal decay rate: R_dec = (phi_m - phi_n)^2 / (2*tau)",
            "Diagonal elements (phi_m = phi_n): R_dec = 0 — no decoherence on diagonal",
            "Same effective regime as Q-C.5: Markovian + weak-coupling",
            "Verdict: effective_regime_decoherence_demonstrated (not exact — regime-limited)",
        ],
    )


def _build_track_b() -> QDPointerBasisAnalysis:
    """Track B: Pointer-basis candidate analysis."""
    candidates = [
        QDPointerBasisCandidate(
            basis_id="PB1_phi_hat_eigenbasis",
            basis_name="phi_hat_eigenbasis",
            description=(
                "Eigenbasis of the constitutive observable Phi_hat. "
                "Diagonal elements have zero decoherence rate under the Lindblad generator."
            ),
            viable=True,
            selection_mechanism=(
                "zero_decoherence_rate_for_diagonal_elements_of_Phi_hat_eigenbasis"
            ),
            appendix_p_class="motivated_but_unbuilt",
            notes=[
                "Observable-language description of the pointer class",
                "Diagonal elements satisfy R_dec = 0 — basis is stable under decoherence",
                "Identified via the stability (zero-rate) criterion, not a dynamical argument",
                "Same class as PB3; PB3 is chosen as canonical because the mechanism is dynamical",
            ],
        ),
        QDPointerBasisCandidate(
            basis_id="PB2_x_hat_eigenbasis",
            basis_name="x_hat_eigenbasis",
            description=(
                "Eigenbasis of a putative position-like observable X_hat, "
                "not yet specified in the GRUT quantum extension."
            ),
            viable=False,
            selection_mechanism="not_applicable_X_hat_not_yet_specified",
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "X_hat operator content deferred to Q-D/Q-E; no dynamical selection mechanism identified",
                "Cannot be evaluated without specifying X_hat and its relation to Phi_hat",
                "Not viable at the current stage of the audit",
            ],
        ),
        QDPointerBasisCandidate(
            basis_id="PB3_jump_operator_eigenbasis",
            basis_name="jump_operator_eigenbasis",
            description=(
                "Eigenbasis selected dynamically by the jump operator L prop Phi_hat. "
                "The jump operator L = Phi_hat/sqrt(tau) defines stability in the Phi_hat-eigenbasis."
            ),
            viable=True,
            selection_mechanism=(
                "dynamical_selection_jump_operator_L_prop_Phi_hat_defines_stable_basis"
            ),
            appendix_p_class="motivated_but_unbuilt",
            notes=[
                "Dynamical-mechanism description of the same class as PB1; "
                "PB3 is chosen as canonical selection label because the selection mechanism is the jump operator",
                "The jump operator L = Phi_hat/sqrt(tau) naturally selects the Phi_hat-eigenbasis as stable",
                "Coherent with Q-C.5 operator content — no new operators required",
                "Appendix P: motivated_but_unbuilt — spectrum of Phi_hat unspecified",
            ],
        ),
        QDPointerBasisCandidate(
            basis_id="PB4_reduced_classical_observable_basis",
            basis_name="reduced_classical_observable_basis",
            description=(
                "Basis defined by the reduced classical observable in the expectation-value limit, "
                "inherited from Q-C.5 constitutive recovery."
            ),
            viable=False,
            selection_mechanism=(
                "not_independent_same_as_PB1_in_expectation_value_limit"
            ),
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Identical to PB1 in the expectation-value limit; not independently motivated",
                "Does not provide a distinct pointer-basis class beyond PB1/PB3",
                "Classified not viable to avoid double-counting the same class",
            ],
        ),
        QDPointerBasisCandidate(
            basis_id="PB5_no_unique_pointer_basis",
            basis_name="no_unique_pointer_basis",
            description=(
                "Null/fallback case: no viable pointer basis identified. "
                "Retained as an explicit rejection record."
            ),
            viable=False,
            selection_mechanism="null_case",
            appendix_p_class="bounded_structural_result",
            notes=[
                "Null/fallback case rejected because PB3 provides a viable candidate",
                "Retained in the candidate list to document that the null case was considered and rejected",
                "If PB3 were invalidated, this would become the operative verdict",
            ],
        ),
    ]
    return QDPointerBasisAnalysis(
        candidates=candidates,
        n_candidates=N_POINTER_BASIS_CANDIDATES,
        n_viable=N_VIABLE_POINTER_BASES,
        chosen_pointer_basis_id="PB3_jump_operator_eigenbasis",
        chosen_pointer_basis_name="jump_operator_eigenbasis",
        unique_basis=False,
        pointer_verdict=QD_POINTER_VERDICT,
        notes=[
            "PB1 and PB3 describe the same basis class under two languages. "
            "PB3 is chosen as canonical because the selection mechanism is dynamical. "
            "n_viable=1 reflects one class identified via two consistent routes.",
            "unique_basis=False: spectrum of Phi_hat is unspecified; degeneracies are possible",
            "pointer_basis_class_selected is the correct verdict — not unique_pointer_basis_selected",
            "PB2 deferred; PB4 non-independent; PB5 null case explicitly rejected",
        ],
    )


def _build_track_c() -> QDTimescaleAnalysis:
    """Track C: Decoherence timescale analysis."""
    return QDTimescaleAnalysis(
        decoherence_rate_formula="0.5 * gamma * delta_phi_sq",
        decoherence_timescale_formula="2 * tau / delta_phi_sq",
        timescale_governed_by="tau_and_eigenvalue_separation",
        tau_sq_value=TAU_SQ,
        gamma_value=GAMMA,
        characteristic_decoherence_timescale="tau_when_delta_phi_eq_sqrt_2",
        consistent_with_prior_timescales=True,
        notes=[
            f"tau_sq = 3/2 = {TAU_SQ}",
            f"tau = sqrt(3/2) = {TAU:.10f}",
            f"gamma = 1/tau = {GAMMA:.10f}",
            "Decoherence rate: R_dec(delta_phi) = delta_phi^2 / (2 * tau)",
            "Decoherence timescale: tau_dec(delta_phi) = 2 * tau / delta_phi^2",
            "At delta_phi = sqrt(2): R_dec = 1/tau, tau_dec = tau",
            "tau remains the single master timescale — eigenvalue separation sets the proportionality",
            "Consistent with constitutive relaxation timescale tau from Q-C.5",
        ],
    )


def _build_track_d() -> QDMeasurementBridgeAnalysis:
    """Track D: Measurement bridge ladder analysis."""
    entries = [
        QDMeasurementBridgeEntry(
            level_name="decoherence_only",
            achieved=True,
            justification=(
                "Off-diagonal elements decay at rate (phi_m-phi_n)^2/(2*tau) in the "
                "Phi_hat-eigenbasis — demonstrated in effective regime"
            ),
        ),
        QDMeasurementBridgeEntry(
            level_name="decoherence_plus_pointer_structure",
            achieved=True,
            justification=(
                "PB3 (jump-operator eigenbasis = Phi_hat-eigenbasis) identified as "
                "stable pointer-basis class"
            ),
        ),
        QDMeasurementBridgeEntry(
            level_name="decoherence_plus_partial_determination_structure",
            achieved=False,
            justification=(
                "No tendency toward specific outcomes demonstrated; diagonal populations "
                "evolve but not toward a predetermined selection"
            ),
        ),
        QDMeasurementBridgeEntry(
            level_name="full_measurement_closure",
            achieved=False,
            justification=(
                "No collapse mechanism, no Born-rule weighting, no irreversible branch "
                "selection — all absent"
            ),
        ),
        QDMeasurementBridgeEntry(
            level_name="born_rule_weighting",
            achieved=False,
            justification=(
                "Born-rule derivation explicitly out of scope; no probability mechanism "
                "in the audited structure"
            ),
        ),
    ]
    return QDMeasurementBridgeAnalysis(
        entries=entries,
        decoherence_achieved=True,
        pointer_structure_achieved=True,
        partial_determination_achieved=False,
        full_measurement_achieved=False,
        born_rule_achieved=False,
        measurement_scope_verdict=QD_MEASUREMENT_SCOPE_VERDICT,
        notes=[
            "Two levels achieved: decoherence_only and decoherence_plus_pointer_structure",
            "Measurement scope ends at decoherence + pointer class — outcome selection is absent",
            "IMPORTANT: decoherence_plus_pointer_structure does NOT imply measurement solved",
            "The gap between decoherence and full measurement closure is documented as BSR (bounded negative)",
        ],
    )


def _build_track_e() -> QDOutcomeSelectionAnalysis:
    """Track E: Outcome-selection mechanism audit."""
    mechanisms = [
        QDOutcomeSelectionMechanism(
            mechanism_name="single_outcome_selection",
            present=False,
            obstruction_or_reason=(
                "Lindblad master equation is deterministic for the density matrix — "
                "no stochastic selection of outcomes is embedded in the law class"
            ),
            appendix_p_class="bounded_structural_result",
        ),
        QDOutcomeSelectionMechanism(
            mechanism_name="born_rule_probabilities",
            present=False,
            obstruction_or_reason=(
                "No probability-weighting formula is present in the kinematic package "
                "(Q-C0 through Q-D); Born rule is explicitly out of scope per Q-A charter FFM1"
            ),
            appendix_p_class="bounded_structural_result",
        ),
        QDOutcomeSelectionMechanism(
            mechanism_name="irreversible_branch_selection",
            present=False,
            obstruction_or_reason=(
                "Lindblad evolution is norm-preserving and trace-preserving; density matrix "
                "evolves continuously without branch collapse"
            ),
            appendix_p_class="bounded_structural_result",
        ),
        QDOutcomeSelectionMechanism(
            mechanism_name="observer_conditioned_update",
            present=False,
            obstruction_or_reason=(
                "No observer or detector coupling is defined in the GRUT quantum extension "
                "at this stage; measurement model not yet introduced"
            ),
            appendix_p_class="bounded_structural_result",
        ),
    ]
    return QDOutcomeSelectionAnalysis(
        mechanisms=mechanisms,
        n_mechanisms=N_OUTCOME_SELECTION_MECHANISMS,
        n_present=N_OUTCOME_MECHANISMS_PRESENT,
        any_outcome_selection_present=False,
        outcome_selection_verdict=QD_OUTCOME_SELECTION_VERDICT,
        notes=[
            "All 4 outcome-selection mechanisms absent from the audited structure",
            "All 4 classified BSR (bounded structural result: documented absence, not permanent impossibility)",
            "Decoherence suppresses interference but does not select outcomes",
            "Outcome-selection gap is documented — not a blocker for Q-E benchmark models",
        ],
    )


def _build_track_f() -> QDObservableClassicalityAnalysis:
    """Track F: Observable classicality analysis."""
    return QDObservableClassicalityAnalysis(
        constitutive_observable="Phi_hat",
        pointer_observable="Phi_hat_eigenbasis_selected_by_jump_operator_L_prop_Phi_hat",
        same_observable=True,
        strength_of_identification=(
            "conditional_on_QC5_jump_operator_choice_L_prop_Phi_hat"
        ),
        classicality_verdict=(
            "constitutive_and_pointer_observables_coincide_conditionally_on_jump_operator_choice"
        ),
        appendix_p_class="motivated_but_unbuilt",
        notes=[
            "HEADLINE: The constitutive observable Phi_hat and the pointer observable coincide "
            "conditionally on the Q-C.5 jump-operator choice L prop Phi_hat.",
            "This identification is internally coherent but NOT independently derived.",
            "It is a structural consequence of the same operator choice that yielded "
            "constitutive recovery in Q-C.5.",
            "Do not read this as: Phi_hat is GRUT's unique classical observable by necessity.",
            "The same-observable result requires the specific L choice — if L were changed, "
            "the coincidence would break.",
            "Appendix P: motivated_but_unbuilt — coherent and notable but dependent on "
            "unbuilt operator content.",
        ],
    )


def _build_track_g() -> QDAppendixPAudit:
    """Track G: Appendix-P classification audit."""
    entries = [
        QDAppendixPEntry(
            item_id="decoherence_result",
            item_name="effective_regime_decoherence",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Effective-regime decoherence of off-diagonal elements demonstrated "
                "in Phi_hat-eigenbasis"
            ),
            forbidden_claim="Decoherence therefore collapse or measurement solved",
            dependency="Inherits Markovian + weak-coupling regime from Q-C.5",
        ),
        QDAppendixPEntry(
            item_id="pointer_basis_selection",
            item_name="pointer_basis_class_PB3",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Pointer-basis class identified as Phi_hat-eigenbasis via dynamical "
                "jump-operator selection"
            ),
            forbidden_claim=(
                "Unique pointer basis derived or Born rule follows from basis selection"
            ),
            dependency="Requires jump operator L prop Phi_hat from Q-C.5",
        ),
        QDAppendixPEntry(
            item_id="decoherence_timescale",
            item_name="tau_dec_eq_2tau_over_delta_phi_sq",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Decoherence timescale identified as 2*tau/delta_phi^2; "
                "equals tau when delta_phi=sqrt(2)"
            ),
            forbidden_claim=(
                "Decoherence timescale derived from first principles without regime conditions"
            ),
            dependency="Inherits tau = sqrt(3/2) from canonical NC constant",
        ),
        QDAppendixPEntry(
            item_id="measurement_scope",
            item_name="decoherence_plus_pointer_scope",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "Measurement scope established as decoherence + pointer class — "
                "not full measurement closure"
            ),
            forbidden_claim=(
                "Decoherence plus pointer structure implies full measurement solved"
            ),
            dependency="Q-D scope does not extend to outcome selection",
        ),
        QDAppendixPEntry(
            item_id="outcome_selection_absent",
            item_name="outcome_selection_mechanisms_absent",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "All four outcome-selection mechanisms (single-outcome, Born rule, "
                "branch, observer-update) are absent from the audited structure"
            ),
            forbidden_claim=(
                "Any outcome-selection mechanism is present or derivable from Q-D structure"
            ),
            dependency="Absence documented as BSR — not permanent impossibility",
        ),
    ]
    return QDAppendixPAudit(
        entries=entries,
        n_entries=len(entries),
        overall_class=QD_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=[
            "Overall Appendix P class: motivated_but_unbuilt",
            "No item reaches native_canon — all results carry MBU or BSR floor",
            "The MBU floor is inherited from Q-A R3 and the effective-regime regime conditions",
            "BSR items document bounded negative results — important for audit completeness",
            "no_native_canon=True: consistent with Q-A charter and Q-C inheritance",
        ],
    )


def _build_track_h() -> QDAuthorizationAudit:
    """Track H: Q-E authorization audit."""
    return QDAuthorizationAudit(
        qe_authorized=True,
        preconditions_satisfied=[
            "effective_regime_decoherence_demonstrated",
            "pointer_basis_class_identified",
            "outcome_selection_gap_documented_as_BSR",
        ],
        qe_constraints=[
            "QE_must_not_assume_Born_rule_or_outcome_selection",
            "QE_results_carry_MBU_or_MIP_floor_inherited_from_QD",
            "QE_must_not_assume_full_measurement_closure",
        ],
        authorization_verdict=QD_AUTHORIZATION_VERDICT,
        notes=[
            "Q-E (benchmark toy models) authorized",
            "Decoherence + pointer structure is sufficient foundation for toy-model work",
            "Q-E must explicitly acknowledge that outcome selection is not available",
            "All Q-E results inherit MBU floor from Q-D",
        ],
    )


def _build_track_i() -> QDNonclaimFirewall:
    """Track I: Non-claim firewall."""
    return QDNonclaimFirewall(
        nonclaims=QD_NONCLAIMS,
        n_nonclaims=N_QD_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qd_result(result: QDMeasurementBridgeResult) -> None:
    """
    Validate all five hard-gated verdict strings against their allowed frozensets.
    Raises ValueError if any verdict is not in its allowed set.
    """
    checks = [
        ("decoherence_verdict", result.decoherence_verdict, ALLOWED_DECOHERENCE_VERDICTS),
        ("pointer_verdict", result.pointer_verdict, ALLOWED_POINTER_VERDICTS),
        ("measurement_scope_verdict", result.measurement_scope_verdict, ALLOWED_MEASUREMENT_SCOPE_VERDICTS),
        ("outcome_selection_verdict", result.outcome_selection_verdict, ALLOWED_OUTCOME_SELECTION_VERDICTS),
        ("authorization_verdict", result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS),
    ]
    for field_name, verdict, allowed in checks:
        if verdict not in allowed:
            raise ValueError(
                f"QD validation failed: {field_name}={verdict!r} is not in "
                f"allowed set {sorted(allowed)}"
            )
    # Also validate the appendix-P class
    if result.qd_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError(
            f"QD validation failed: qd_appendix_p_class={result.qd_appendix_p_class!r} "
            f"is not in allowed set {sorted(ALLOWED_APPENDIX_P_CLASSES)}"
        )


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qd_measurement_bridge_audit() -> QDMeasurementBridgeResult:
    """
    Run the full Q-D Decoherence and Measurement Bridge Audit.

    Assembles all nine tracks, sets all five hard-gated verdicts, builds the
    diagnostics dictionary, and returns a fully populated QDMeasurementBridgeResult.

    Preconditions (inherited):
      - QC_INHERITED_LAW_CLASS = "lindbladian_like_law_preferred"
      - QC5_INHERITED_RECOVERY = "effective_regime_constitutive_recovery_demonstrated"
      - QC5_INHERITED_AUTHORIZATION = "authorized_to_proceed_to_QD"

    Returns:
        QDMeasurementBridgeResult with valid=True if all verdicts pass validation.

    Raises:
        ValueError: if any verdict string is outside its allowed frozenset.
    """
    # Build all nine tracks
    track_a = _build_track_a()
    track_b = _build_track_b()
    track_c = _build_track_c()
    track_d = _build_track_d()
    track_e = _build_track_e()
    track_f = _build_track_f()
    track_g = _build_track_g()
    track_h = _build_track_h()
    track_i = _build_track_i()

    # Set the five hard-gated verdicts
    decoherence_verdict = QD_DECOHERENCE_VERDICT
    pointer_verdict = QD_POINTER_VERDICT
    measurement_scope_verdict = QD_MEASUREMENT_SCOPE_VERDICT
    outcome_selection_verdict = QD_OUTCOME_SELECTION_VERDICT
    authorization_verdict = QD_AUTHORIZATION_VERDICT

    # Diagnostics dictionary
    diagnostics: Dict[str, Any] = {
        "tau_sq": TAU_SQ,
        "tau": TAU,
        "gamma": GAMMA,
        "gamma_tau": GAMMA * TAU,   # must be 1.0
        "n_pointer_candidates": N_POINTER_BASIS_CANDIDATES,
        "n_viable_pointer": N_VIABLE_POINTER_BASES,
        "n_outcome_mechanisms": N_OUTCOME_SELECTION_MECHANISMS,
        "n_outcome_present": N_OUTCOME_MECHANISMS_PRESENT,
        "n_nonclaims": N_QD_NONCLAIMS,
        "decoherence_rate_formula": "0.5 * gamma * delta_phi_sq",
        "decoherence_timescale_formula": "2 * tau / delta_phi_sq",
        "decoherence_rate_at_delta_phi_sqrt2": 0.5 * GAMMA * 2.0,   # = 1/tau = GAMMA
        "decoherence_timescale_at_delta_phi_sqrt2": 2.0 * TAU / 2.0,  # = TAU
    }

    # Allowed claims
    allowed_claims: List[str] = [
        "Effective-regime decoherence of off-diagonal density-matrix elements demonstrated "
        "in the Phi_hat-eigenbasis",
        "Pointer-basis class identified as eigenbasis of Phi_hat via dynamical jump-operator "
        "selection (L prop Phi_hat)",
        "Decoherence timescale identified as 2*tau/delta_phi^2; reduces to tau when eigenvalue "
        "separation is sqrt(2)",
        "Constitutive and pointer observables coincide conditionally on the Q-C.5 "
        "jump-operator choice",
        "Measurement scope established as decoherence_plus_pointer_structure — not full "
        "measurement closure",
        "All four outcome-selection mechanisms absent; documented as BSR",
        "Q-E (benchmark toy models) authorized subject to stated constraints",
    ]

    # Forbidden claims
    forbidden_claims: List[str] = [
        "Decoherence implies or causes wavefunction collapse",
        "Pointer-basis selection implies Born-rule probability weighting",
        "Off-diagonal suppression yields single-outcome selection",
        "The decoherence result is native GRUT canon",
        "Constitutive-observable recovery (Q-C.5) implies full measurement solved",
        "Observer problem solved by Lindbladian open-system dynamics",
        "Born rule is derived from or implied by Q-D results",
        "Pointer-basis identification fixes the ontology of measurement outcomes",
    ]

    result = QDMeasurementBridgeResult(
        valid=False,  # set after validation
        track_a_decoherence=track_a,
        track_b_pointer_basis=track_b,
        track_c_timescale=track_c,
        track_d_measurement_bridge=track_d,
        track_e_outcome_selection=track_e,
        track_f_observable_classicality=track_f,
        track_g_appendix_p=track_g,
        track_h_authorization=track_h,
        track_i_nonclaims=track_i,
        decoherence_verdict=decoherence_verdict,
        pointer_verdict=pointer_verdict,
        measurement_scope_verdict=measurement_scope_verdict,
        outcome_selection_verdict=outcome_selection_verdict,
        authorization_verdict=authorization_verdict,
        qd_appendix_p_class=QD_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=list(QD_NONCLAIMS),
        diagnostics=diagnostics,
    )

    # Validate all verdicts — raises ValueError on failure
    validate_qd_result(result)

    # Mark valid only after successful validation
    result.valid = True
    return result
