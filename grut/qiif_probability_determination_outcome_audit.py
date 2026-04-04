"""
Appendix Q-II.F --- Probability, Determination, and Outcome Extensions Audit
=============================================================================
GRUT Quantum Program --- Phase Q-II.F

This module audits what probability, determination, or outcome-selection
structures are justified in the GRUT quantum extension.

Key finding summary
-------------------
The current GRUT quantum extension provides:

1. DIAGNOSTIC WEIGHTS (not probabilities):
   - Density-matrix diagonal entries rho_nn in pointer basis
   - Reduced-state eigenvalues (purity, entropy)
   - Decoherence-suppressed off-diagonals (visibility decay)
   - Mode occupation numbers n_i = sigma_+ sigma_-
   These are CALCULABLE NUMBERS from the density-matrix formalism.
   They satisfy sum = 1, non-negative, etc.  But they are NOT
   probabilities unless we POSTULATE the Born rule.

2. DECOHERENCE provides diagonal dominance, NOT outcome selection:
   - Off-diagonals -> 0: leaves diagonal entries as stable weights
   - But the density matrix remains a MIXTURE, not a single outcome
   - Decoherence selects a BASIS (pointer basis), not an OUTCOME
   - The "preferred branches" are mathematical sectors, not selected realities

3. THE BORN RULE is a separate postulate:
   - Born rule: P(outcome n) = rho_nn = <n|rho|n> in measurement basis
   - This IDENTIFIES density-matrix diagonals AS probabilities
   - It is NOT derivable from Lindblad dynamics, decoherence, or density-matrix
     formalism alone
   - It requires a MEASUREMENT EVENT INTERPRETATION that the current package
     does not provide

4. OUTCOME SELECTION is absent:
   - No mechanism selects one diagonal entry as "the actual outcome"
   - Decoherence + Born rule gives probabilities but not selection
   - Collapse/update/branching would be additional postulates
   - The measurement problem remains open at this stage

Minimum extension route:
   The smallest route to probabilities is to POSTULATE the Born rule as
   an extension-level axiom (MIP): P(n) = Tr(rho P_n) where P_n is the
   projector onto outcome n.  This is:
   - Convergently motivated (standard QM, consistent with all Part I/II results)
   - No new DOF required (uses existing density-matrix formalism)
   - MIP classification (motivated independent postulation)
   - Does NOT solve outcome selection (only provides probabilities, not actuality)
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
N_ELIGIBILITY_INGREDIENTS: int = 5
N_WEIGHT_CANDIDATES: int = 6
N_DETERMINATION_LEVELS: int = 5
N_OUTCOME_CANDIDATES: int = 6
N_DECOHERENCE_BOUNDARY_TESTS: int = 4
N_COMPOSITE_TESTS: int = 4
N_MANYMODE_TESTS: int = 4
N_EXTENSION_CANDIDATES: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_QIIF_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
QIIE_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QIIF"

# Q-II.F Verdict strings
QIIF_PROBABILITY_VERDICT: str = "diagnostic_weights_available_but_not_probabilities"
QIIF_DETERMINATION_VERDICT: str = "decoherence_and_diagonal_dominance_only"
QIIF_OUTCOME_VERDICT: str = "born_rule_and_outcome_selection_not_derived"
QIIF_EXTENSION_ROUTE_VERDICT: str = "minimum_probability_extension_identified"
QIIF_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QIIG"
QIIF_OVERALL_APPENDIX_P_CLASS: str = "bounded_structural_result"

# Frozensets
ALLOWED_PROBABILITY_VERDICTS: frozenset = frozenset({
    "diagnostic_weights_available_but_not_probabilities",
    "effective_probability_candidates_present_but_unbuilt",
    "no_probability_structure_yet",
    "probability_structure_blocked",
})
ALLOWED_DETERMINATION_VERDICTS: frozenset = frozenset({
    "decoherence_and_diagonal_dominance_only",
    "effective_determination_tendency_present",
    "determination_structure_structurally_plausible_but_unbuilt",
    "no_determination_structure_yet",
})
ALLOWED_OUTCOME_VERDICTS: frozenset = frozenset({
    "born_rule_and_outcome_selection_not_derived",
    "non_born_outcome_tendency_candidate_present",
    "outcome_rule_structurally_plausible_but_unbuilt",
    "outcome_rule_blocked",
})
ALLOWED_EXTENSION_ROUTE_VERDICTS: frozenset = frozenset({
    "minimum_probability_extension_identified",
    "probability_extension_route_structurally_plausible_but_unbuilt",
    "probability_extension_route_underdetermined",
    "no_coherent_probability_extension_route",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QIIG",
    "authorized_only_for_further_probability_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_QIID_or_QIIE",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8)
QIIF_NONCLAIMS: List[str] = [
    "NOT_claiming_diagonal_density_entries_therefore_Born_rule__"
    "diagonal_entries_are_diagnostic_weights_not_probabilities_without_Born_postulate",
    "NOT_claiming_decoherence_therefore_probabilities__"
    "decoherence_selects_basis_not_outcome_and_does_not_assign_probability_weights",
    "NOT_claiming_pointer_basis_therefore_outcome_selection__"
    "pointer_basis_stabilization_determines_which_basis_not_which_outcome",
    "NOT_claiming_reduced_state_eigenvalues_therefore_laboratory_frequencies__"
    "eigenvalues_are_mathematical_spectrum_not_measurement_statistics",
    "NOT_claiming_entanglement_therefore_probability_closure__"
    "entanglement_adds_correlation_structure_not_probability_interpretation",
    "NOT_claiming_many_mode_occupations_therefore_measurement_probabilities__"
    "occupation_numbers_are_bookkeeping_not_observed_frequencies",
    "NOT_claiming_extension_level_weighting_rule_therefore_native_canon__"
    "Born_rule_if_postulated_carries_MIP_classification",
    "NOT_claiming_outcome_tendency_therefore_unique_reality_selected__"
    "diagonal_dominance_is_tendency_toward_classical_appearance_not_actuality",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIFEligibilityIngredient:
    ingredient_id: str
    ingredient_name: str
    description: str
    status: str
    source: str
    notes: List[str]


@dataclass
class QIIFProbabilityEligibilityAudit:
    ingredients: List[QIIFEligibilityIngredient]
    n_ingredients: int
    n_present: int
    n_absent: int
    n_extension_level: int
    eligibility_verdict: str
    notes: List[str]


@dataclass
class QIIFWeightCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    status: str  # "diagnostic_only", "effective_candidate", "underdetermined", "blocked"
    sum_to_one: bool
    non_negative: bool
    probability_without_born: bool
    notes: List[str]


@dataclass
class QIIFWeightVsProbabilityAudit:
    candidates: List[QIIFWeightCandidate]
    n_candidates: int
    n_diagnostic: int
    n_effective_candidate: int
    probability_verdict: str
    notes: List[str]


@dataclass
class QIIFDeterminationLevel:
    level_id: str
    level_name: str
    description: str
    achieved: bool
    notes: List[str]


@dataclass
class QIIFDeterminationTendencyAudit:
    levels: List[QIIFDeterminationLevel]
    n_levels: int
    highest_achieved_id: str
    determination_verdict: str
    notes: List[str]


@dataclass
class QIIFOutcomeCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    status: str
    notes: List[str]


@dataclass
class QIIFOutcomeSelectionAudit:
    candidates: List[QIIFOutcomeCandidate]
    n_candidates: int
    outcome_verdict: str
    born_rule_derived: bool
    outcome_selection_derived: bool
    notes: List[str]


@dataclass
class QIIFDecoherenceBoundaryTest:
    test_id: str
    test_name: str
    description: str
    result: str
    notes: List[str]


@dataclass
class QIIFDecoherenceProbabilityBoundaryAudit:
    tests: List[QIIFDecoherenceBoundaryTest]
    n_tests: int
    decoherence_sufficient_for_probability: bool
    notes: List[str]


@dataclass
class QIIFCompositeTest:
    test_id: str
    test_name: str
    description: str
    adds_probability_content: bool
    notes: List[str]


@dataclass
class QIIFCompositeEntangledProbabilityAudit:
    tests: List[QIIFCompositeTest]
    n_tests: int
    n_adds_content: int
    notes: List[str]


@dataclass
class QIIFManyModeTest:
    test_id: str
    test_name: str
    description: str
    adds_probability_content: bool
    notes: List[str]


@dataclass
class QIIFManyModeProbabilityAudit:
    tests: List[QIIFManyModeTest]
    n_tests: int
    n_adds_content: int
    notes: List[str]


@dataclass
class QIIFExtensionCandidate:
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    appendix_p_class: str
    minimum_additional_structure: str
    notes: List[str]


@dataclass
class QIIFMinimalProbabilityExtensionAudit:
    candidates: List[QIIFExtensionCandidate]
    n_candidates: int
    n_viable: int
    chosen_candidate_id: str
    extension_route_verdict: str
    notes: List[str]


@dataclass
class QIIFAppendixPEntry:
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIIFAppendixPAudit:
    entries: List[QIIFAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIIFAuthorizationAudit:
    qiig_authorized: bool
    authorization_basis: List[str]
    qiig_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QIIFNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIFProbabilityDeterminationOutcomeResult:
    valid: bool
    track_a_eligibility: QIIFProbabilityEligibilityAudit
    track_b_weight_vs_prob: QIIFWeightVsProbabilityAudit
    track_c_determination: QIIFDeterminationTendencyAudit
    track_d_outcome: QIIFOutcomeSelectionAudit
    track_e_decoherence_boundary: QIIFDecoherenceProbabilityBoundaryAudit
    track_f_composite: QIIFCompositeEntangledProbabilityAudit
    track_g_manymode: QIIFManyModeProbabilityAudit
    track_h_extension: QIIFMinimalProbabilityExtensionAudit
    track_i_appendix_p: QIIFAppendixPAudit
    track_j_authorization: QIIFAuthorizationAudit
    track_k_nonclaims: QIIFNonclaimFirewall
    # Five hard-gated verdicts
    probability_verdict: str
    determination_verdict: str
    outcome_verdict: str
    extension_route_verdict: str
    authorization_verdict: str
    # Summary
    qiif_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIIFProbabilityEligibilityAudit:
    ingredients = [
        QIIFEligibilityIngredient("PE1", "normalized_state_weights",
            "Density-matrix diagonal entries sum to 1, non-negative.", "present",
            "Part I density-matrix formalism",
            ["Tr(rho) = 1; diagonal entries rho_nn >= 0; sum_n rho_nn = 1"]),
        QIIFEligibilityIngredient("PE2", "positive_candidate_assignments",
            "Candidate probability assignments P(n) = rho_nn.", "extension_level",
            "Born rule (not yet postulated)",
            ["The IDENTIFICATION of rho_nn as P(n) IS the Born rule",
             "Without Born postulate, rho_nn is a diagnostic weight, not a probability"]),
        QIIFEligibilityIngredient("PE3", "repeatable_measurement_interpretation",
            "Interpretation of rho_nn as frequency in repeated measurements.", "absent",
            "Requires measurement theory (not available)",
            ["No measurement framework in current package",
             "Frequency interpretation requires: ensemble, repeated preparation, detection"]),
        QIIFEligibilityIngredient("PE4", "observable_event_map",
            "Map from observable eigenvalues to measurement events.", "absent",
            "Requires measurement postulate",
            ["No measurement postulate in current package",
             "Observable eigenvalues are mathematical; events require physical detection"]),
        QIIFEligibilityIngredient("PE5", "decoherence_pointer_compatibility",
            "Compatibility with decoherence/pointer framework.", "present",
            "Part I Q-D pointer basis",
            ["Decoherence selects pointer basis; diagonals in that basis are stable",
             "This is necessary but not sufficient for probability"]),
    ]
    n_p = sum(1 for i in ingredients if i.status == "present")
    n_a = sum(1 for i in ingredients if i.status == "absent")
    n_e = sum(1 for i in ingredients if i.status == "extension_level")
    return QIIFProbabilityEligibilityAudit(
        ingredients=ingredients, n_ingredients=N_ELIGIBILITY_INGREDIENTS,
        n_present=n_p, n_absent=n_a, n_extension_level=n_e,
        eligibility_verdict="partially_eligible_missing_measurement_framework",
        notes=["2 present (normalized weights, pointer compatibility)",
               "2 absent (measurement interpretation, observable-event map)",
               "1 extension-level (Born-rule identification)",
               "Probability requires Born postulate + measurement framework"],
    )


def _build_track_b() -> QIIFWeightVsProbabilityAudit:
    candidates = [
        QIIFWeightCandidate("WP1", "density_matrix_diagonals",
            "rho_nn in pointer basis: stable after decoherence.",
            "diagnostic_only", True, True, False,
            ["Sum to 1, non-negative, stable under decoherence",
             "But: are diagnostic weights, not probabilities without Born rule"]),
        QIIFWeightCandidate("WP2", "reduced_state_eigenvalues",
            "Eigenvalues of rho_A = Tr_B(rho_AB).",
            "diagnostic_only", True, True, False,
            ["Sum to 1, non-negative; characterize subsystem mixedness",
             "Diagnostic of entanglement, not measurement probabilities"]),
        QIIFWeightCandidate("WP3", "purity_entropy_weights",
            "Tr(rho^2), S(rho) = -Tr(rho ln rho).",
            "diagnostic_only", False, True, False,
            ["Purity: single number in [1/d, 1]; entropy: in [0, ln d]",
             "Do not sum to 1; not probability candidates",
             "Global diagnostics, not outcome weights"]),
        QIIFWeightCandidate("WP4", "decoherence_branch_weights",
            "Diagonal entries after long-time decoherence evolution.",
            "effective_candidate", True, True, False,
            ["After decoherence: rho -> sum_n rho_nn |n><n|",
             "rho_nn are EFFECTIVE probability candidates",
             "But: the identification rho_nn = P(n) IS the Born rule",
             "Status: effective candidate only, not probability without postulate"]),
        QIIFWeightCandidate("WP5", "mode_occupation_weights",
            "n_i = <sigma_+^i sigma_-^i> = expectation of occupation.",
            "diagnostic_only", False, True, False,
            ["Expectation value of number operator on site i",
             "In [0, 1] for qubits; does not sum to 1 across outcomes",
             "Diagnostic of excitation level, not outcome probability"]),
        QIIFWeightCandidate("WP6", "no_valid_probability_objects",
            "Null candidate.", "rejected", False, False, False,
            ["Rejected: diagnostic weights ARE available (WP1, WP2, WP4)"]),
    ]
    n_diag = sum(1 for c in candidates if c.status == "diagnostic_only")
    n_eff = sum(1 for c in candidates if c.status == "effective_candidate")
    return QIIFWeightVsProbabilityAudit(
        candidates=candidates, n_candidates=N_WEIGHT_CANDIDATES,
        n_diagnostic=n_diag, n_effective_candidate=n_eff,
        probability_verdict=QIIF_PROBABILITY_VERDICT,
        notes=["3 diagnostic-only (diagonals, eigenvalues, occupation)",
               "1 effective candidate (decoherence branch weights)",
               "1 non-candidate (purity/entropy: wrong structure)",
               "Key distinction: diagnostic weights exist; probabilities require Born rule",
               "Verdict: diagnostic_weights_available_but_not_probabilities"],
    )


def _build_track_c() -> QIIFDeterminationTendencyAudit:
    levels = [
        QIIFDeterminationLevel("DT1", "decoherence_suppression",
            "Off-diagonal suppression: rho_mn -> 0 for m != n.", True,
            ["Established in Part I Q-D; confirmed for composites in Q-II.B"]),
        QIIFDeterminationLevel("DT2", "pointer_basis_stabilization",
            "Pointer-basis diagonal entries survive decoherence.", True,
            ["Part I Q-D: sigma_z eigenstates are pointer states",
             "Diagonal entries rho_nn are the stable sector"]),
        QIIFDeterminationLevel("DT3", "diagonal_dominance_tendency",
            "Long-time density matrix approaches diagonal form.", True,
            ["rho(t -> inf) -> sum_n rho_nn |n><n| in pointer basis",
             "This IS diagonal dominance: a classical-LOOKING mixture",
             "But it is still a mixture, not a determined outcome"]),
        QIIFDeterminationLevel("DT4", "effective_determination_tendency",
            "Something beyond diagonal dominance toward actual outcomes.", False,
            ["NOT achieved: diagonal dominance is the ceiling",
             "No mechanism selects one rho_nn as actual",
             "Lindblad evolution is deterministic for rho, not for outcomes"]),
        QIIFDeterminationLevel("DT5", "no_determination",
            "No determination structure at all.", False,
            ["Rejected: DT1-DT3 are achieved (decoherence provides diagonal dominance)"]),
    ]
    achieved = [l for l in levels if l.achieved]
    highest = achieved[-1].level_id + "_" + achieved[-1].level_name if achieved else "none"
    return QIIFDeterminationTendencyAudit(
        levels=levels, n_levels=N_DETERMINATION_LEVELS,
        highest_achieved_id=highest,
        determination_verdict=QIIF_DETERMINATION_VERDICT,
        notes=["DT1-DT3 achieved: decoherence -> pointer stabilization -> diagonal dominance",
               "DT4 NOT achieved: no mechanism beyond diagonal dominance",
               "Verdict: decoherence_and_diagonal_dominance_only",
               "This is the honest ceiling: classical APPEARANCE, not actuality"],
    )


def _build_track_d() -> QIIFOutcomeSelectionAudit:
    candidates = [
        QIIFOutcomeCandidate("OS1", "no_outcome_selection",
            "No mechanism selects a single outcome.", "confirmed_absent",
            ["The density matrix remains a mixture after decoherence",
             "No branch is selected as actual; all branches coexist in rho"]),
        QIIFOutcomeCandidate("OS2", "effective_non_born_tendency",
            "Some non-Born tendency toward outcomes.", "absent",
            ["No non-Born outcome tendency identified in current package",
             "Lindblad is deterministic for rho; no stochastic element"]),
        QIIFOutcomeCandidate("OS3", "born_rule_candidate",
            "Born rule: P(n) = rho_nn as probability postulate.", "extension_level",
            ["Born rule is the standard QM probability axiom",
             "Would IDENTIFY diagnostic weights as probabilities",
             "Must be explicitly postulated (MIP); not derivable from current package",
             "Does NOT solve outcome selection (gives probabilities, not actuality)"]),
        QIIFOutcomeCandidate("OS4", "collapse_update_rule",
            "State update rho -> |n><n| upon outcome n.", "extension_level",
            ["Would require: Born rule (OS3) + collapse postulate",
             "Two additional postulates beyond current package",
             "Standard QM includes this; GRUT does not (yet)"]),
        QIIFOutcomeCandidate("OS5", "many_worlds_branch",
            "All branches persist; no selection.", "compatible_but_ad_hoc",
            ["Compatible with current formalism (no selection needed)",
             "But: adds interpretive framework, not physics",
             "CAH: compatible but not motivated by GRUT architecture"]),
        QIIFOutcomeCandidate("OS6", "outcome_blocked",
            "Outcome selection is blocked.", "rejected",
            ["Rejected: outcome selection is ABSENT, not BLOCKED",
             "The path exists (Born rule + collapse); it is just not taken"]),
    ]
    return QIIFOutcomeSelectionAudit(
        candidates=candidates, n_candidates=N_OUTCOME_CANDIDATES,
        outcome_verdict=QIIF_OUTCOME_VERDICT,
        born_rule_derived=False,
        outcome_selection_derived=False,
        notes=["OS1 confirmed: no outcome selection mechanism present",
               "OS3: Born rule is the minimum probability extension (MIP)",
               "OS4: collapse requires Born rule + additional postulate",
               "Born rule NOT derived; outcome selection NOT derived",
               "Verdict: born_rule_and_outcome_selection_not_derived"],
    )


def _build_track_e() -> QIIFDecoherenceProbabilityBoundaryAudit:
    tests = [
        QIIFDecoherenceBoundaryTest("DB1", "decoherence_licenses_stable_sectors",
            "Decoherence produces stable pointer-basis diagonal sectors.", "confirmed",
            ["Part I Q-D: off-diagonals suppressed, diagonals stable",
             "This IS what decoherence does: selects a classical-looking sector"]),
        QIIFDecoherenceBoundaryTest("DB2", "decoherence_licenses_diagonal_weights",
            "Diagonal entries rho_nn are well-defined weights after decoherence.", "confirmed",
            ["Sum to 1, non-negative, stable: proper weight structure",
             "But WEIGHTS, not PROBABILITIES (without Born rule)"]),
        QIIFDecoherenceBoundaryTest("DB3", "decoherence_plus_postulate_licenses_probability",
            "Decoherence + Born rule postulate = probability structure.", "extension_level",
            ["If we POSTULATE P(n) = rho_nn (Born rule), then decoherence ensures "
             "the probability is assigned in the stable (pointer) basis",
             "This is the standard decoherence + Born route",
             "Extension-level: requires Born postulate"]),
        QIIFDecoherenceBoundaryTest("DB4", "decoherence_alone_insufficient",
            "Decoherence alone is insufficient for probability.", "confirmed",
            ["Decoherence gives diagonal dominance but NOT probability assignment",
             "Decoherence gives basis selection but NOT outcome selection",
             "The gap between weights and probabilities is the Born rule"]),
    ]
    return QIIFDecoherenceProbabilityBoundaryAudit(
        tests=tests, n_tests=N_DECOHERENCE_BOUNDARY_TESTS,
        decoherence_sufficient_for_probability=False,
        notes=["DB1-DB2: decoherence produces stable diagonal weights (confirmed)",
               "DB3: decoherence + Born = probability (extension-level)",
               "DB4: decoherence ALONE insufficient (confirmed)",
               "Central finding: decoherence is NECESSARY but NOT SUFFICIENT"],
    )


def _build_track_f() -> QIIFCompositeEntangledProbabilityAudit:
    tests = [
        QIIFCompositeTest("CP1", "reduced_state_mixedness_diagnostic_only",
            "Reduced-state mixedness is a diagnostic, not a probability.", False,
            ["Tr(rho_A^2) < 1 for entangled states: diagnostic of entanglement",
             "Does not add probability content"]),
        QIIFCompositeTest("CP2", "entanglement_adds_correlation_only",
            "Entanglement adds correlation structure, not probability.", False,
            ["<A tensor B> - <A><B> != 0 for entangled states",
             "Correlation is mathematical; probability interpretation requires Born rule"]),
        QIIFCompositeTest("CP3", "composite_enables_stronger_weighting",
            "Composite structure enables any stronger weighting rule.", False,
            ["No: composite structure adds state space, not probability axiom",
             "Born rule is independent of whether state is composite or single"]),
        QIIFCompositeTest("CP4", "no_new_probability_closure",
            "No new probability closure from composite/entanglement.", True,
            ["Confirmed: composite and entanglement add structure, not probability",
             "Born-rule gap persists regardless of state-space extensions"]),
    ]
    n_adds = sum(1 for t in tests if t.adds_probability_content)
    return QIIFCompositeEntangledProbabilityAudit(
        tests=tests, n_tests=N_COMPOSITE_TESTS,
        n_adds_content=n_adds,
        notes=["No new probability content from composite/entanglement",
               "Born-rule gap is INDEPENDENT of state-space structure",
               "CP4 confirms: no probability closure from Q-II.B/C"],
    )


def _build_track_g() -> QIIFManyModeProbabilityAudit:
    tests = [
        QIIFManyModeTest("MM1", "occupation_bookkeeping_only",
            "Mode occupation n_i = <sigma_+ sigma_-> is bookkeeping.", False,
            ["Expectation value of number operator; in [0,1] for qubits",
             "Not a probability of outcomes; a diagnostic of excitation level"]),
        QIIFManyModeTest("MM2", "effective_rate_weighting",
            "Lindblad rates give effective decay rates, not measurement probabilities.", False,
            ["Decay rate gamma = 1/tau characterizes relaxation speed",
             "Not a probability of finding a specific outcome"]),
        QIIFManyModeTest("MM3", "probability_under_extra_assumptions",
            "Under Born rule + measurement, n_i would give detection probability.", False,
            ["If Born rule postulated: P(site i excited) = <n_i> = rho_ii^{(i)}",
             "But this requires Born rule (not yet available)"]),
        QIIFManyModeTest("MM4", "no_probability_gain",
            "No probability gain from many-mode structure.", True,
            ["Confirmed: many-mode adds excitation language, not probability",
             "Born-rule gap persists regardless of mode structure"]),
    ]
    n_adds = sum(1 for t in tests if t.adds_probability_content)
    return QIIFManyModeProbabilityAudit(
        tests=tests, n_tests=N_MANYMODE_TESTS,
        n_adds_content=n_adds,
        notes=["No probability gain from many-mode excitation structure",
               "Occupation numbers are diagnostics, not probabilities",
               "Born-rule gap is independent of excitation grammar"],
    )


def _build_track_h() -> QIIFMinimalProbabilityExtensionAudit:
    candidates = [
        QIIFExtensionCandidate("PX1", "born_rule_postulation",
            "Postulate: P(n) = Tr(rho P_n) where P_n = |n><n| is projector.",
            True, "motivated_independent_postulation",
            "One axiom: P(n) = Tr(rho P_n) in pointer basis",
            ["Smallest route: one postulate, no new DOF",
             "Convergently motivated: standard QM, consistent with all prior results",
             "MIP classification: motivated by decoherence selecting pointer basis",
             "Does NOT solve outcome selection (gives probabilities, not actuality)",
             "Enables: Bell-inequality evaluation, expectation-value interpretation"]),
        QIIFExtensionCandidate("PX2", "born_rule_plus_collapse",
            "Born rule + state update rho -> P_n rho P_n / Tr(rho P_n).",
            True, "motivated_independent_postulation",
            "Two axioms: Born probability + state update",
            ["Larger extension: two postulates",
             "Provides both probabilities AND outcome selection",
             "Standard QM measurement postulate"]),
        QIIFExtensionCandidate("PX3", "gleason_theorem_route",
            "Derive Born rule from non-contextuality (Gleason's theorem).",
            False, "motivated_but_unbuilt",
            "Requires: dim >= 3 Hilbert space + non-contextuality axiom",
            ["Not viable for C^2 (Gleason requires dim >= 3)",
             "Could work for composite C^4 but requires non-contextuality postulate",
             "The postulate itself is an MIP; not a derivation from GRUT"]),
        QIIFExtensionCandidate("PX4", "no_extension_route",
            "No coherent probability extension route.", False, "forbidden_or_inconsistent",
            "N/A",
            ["Rejected: PX1 provides a clean extension route"]),
    ]
    n_v = sum(1 for c in candidates if c.viable)
    return QIIFMinimalProbabilityExtensionAudit(
        candidates=candidates, n_candidates=N_EXTENSION_CANDIDATES,
        n_viable=n_v, chosen_candidate_id="PX1_born_rule_postulation",
        extension_route_verdict=QIIF_EXTENSION_ROUTE_VERDICT,
        notes=["PX1 chosen: Born rule as single MIP postulate",
               "Smallest route: one axiom, no new DOF, convergently motivated",
               "PX2 also viable but larger (two postulates)",
               "PX3 not viable for C^2 (Gleason requires dim >= 3)",
               "Verdict: minimum_probability_extension_identified"],
    )


def _build_track_i() -> QIIFAppendixPAudit:
    entries = [
        QIIFAppendixPEntry("QIIF_diagnostic_weights", "Diagnostic weights",
            "bounded_structural_result",
            "Diagnostic weights (density-matrix diagonals) are available and well-defined",
            "Diagnostic weights are probabilities",
            "Part I density-matrix formalism"),
        QIIFAppendixPEntry("QIIF_born_absence", "Born-rule absence",
            "bounded_structural_result",
            "Born rule is absent: explicitly documented as not derived",
            "Born rule follows from decoherence or pointer-basis selection",
            "Part I Q-D: born_rule_or_outcome_selection_not_natively_derived"),
        QIIFAppendixPEntry("QIIF_outcome_absence", "Outcome-selection absence",
            "bounded_structural_result",
            "Outcome selection is absent: no mechanism for single-outcome actuality",
            "Outcome selection follows from diagonal dominance",
            "Part I Q-D: all 4 outcome mechanisms absent"),
        QIIFAppendixPEntry("QIIF_decoherence_boundary", "Decoherence-probability boundary",
            "bounded_structural_result",
            "Decoherence is necessary but not sufficient for probability",
            "Decoherence alone provides probabilities",
            "Part I Q-D, Q-F decoherence architecture"),
        QIIFAppendixPEntry("QIIF_born_extension_route", "Born-rule extension route",
            "motivated_independent_postulation",
            "Born-rule postulation identified as minimum probability extension (MIP)",
            "Born rule derived from GRUT architecture",
            "Decoherence + pointer basis motivate but do not derive Born rule"),
        QIIFAppendixPEntry("QIIF_no_new_from_composite", "No probability from composite",
            "bounded_structural_result",
            "Composite/entanglement/many-mode add no probability content",
            "State-space extensions provide probability closure",
            "Q-II.B through Q-II.E"),
        QIIFAppendixPEntry("QIIF_overall", "Q-II.F overall",
            "bounded_structural_result",
            "Probability gap fully documented; minimum extension identified",
            "Probability closure achieved",
            "All Q-II.F tracks"),
    ]
    return QIIFAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIIF_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["5 BSR (absences and boundaries documented), 1 MIP (extension route)",
               "Overall: BSR — this appendix documents what is absent and the path forward",
               "No native canon; no probability derived"],
    )


def _build_track_j() -> QIIFAuthorizationAudit:
    return QIIFAuthorizationAudit(
        qiig_authorized=True,
        authorization_basis=[
            "probability_gap_fully_documented",
            "diagnostic_weights_characterized",
            "decoherence_probability_boundary_established",
            "minimum_born_rule_extension_route_identified",
            "composite_and_manymode_probability_contribution_assessed",
        ],
        qiig_constraints=[
            "QIIG_must_synthesize_all_Part_II_results_for_matter_readiness",
            "QIIG_must_document_Born_rule_absence_as_matter_prerequisite_gap",
            "QIIG_must_not_assume_probability_closure",
            "QIIG_results_inherit_BSR_or_MBU_floor",
            "QIIG_must_formalize_handoff_conditions_to_Appendix_R",
        ],
        authorization_verdict=QIIF_AUTHORIZATION_VERDICT,
        notes=["Q-II.G authorized: probability gap fully documented, "
               "extension route identified",
               "Q-II.G must produce the final matter-readiness map",
               "Born-rule absence is a documented gap, not a blocker for Q-II.G"],
    )


def _build_track_k() -> QIIFNonclaimFirewall:
    return QIIFNonclaimFirewall(
        nonclaims=QIIF_NONCLAIMS, n_nonclaims=N_QIIF_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_qiif_probability_determination_outcome_audit() -> QIIFProbabilityDeterminationOutcomeResult:
    """Run the full Q-II.F Probability, Determination, and Outcome Extensions Audit."""
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
        "Diagnostic weights (density-matrix diagonals, reduced-state eigenvalues) "
        "are well-defined and available throughout the extension package",
        "Decoherence provides diagonal dominance in pointer basis: "
        "classical-looking mixture, not probability assignment",
        "Born rule is absent: not derived from decoherence, pointer basis, "
        "or any Part I/II result",
        "Outcome selection is absent: no mechanism for single-outcome actuality "
        "in the current package",
        "Minimum probability extension identified: Born rule as single MIP "
        "postulate P(n) = Tr(rho P_n)",
        "Composite, entanglement, and many-mode structures add no new "
        "probability content (Born gap is structure-independent)",
        "Q-II.G authorized: probability gap documented, extension route identified",
    ]

    forbidden_claims: List[str] = [
        "Diagonal density entries imply Born rule",
        "Decoherence implies probabilities",
        "Pointer-basis selection implies outcome selection",
        "Reduced-state eigenvalues imply laboratory frequencies",
        "Entanglement implies probability closure",
        "Many-mode occupation numbers imply measurement probabilities",
        "Extension-level weighting rule implies native canon",
    ]

    diagnostics: Dict[str, Any] = {
        "n_eligibility_ingredients": N_ELIGIBILITY_INGREDIENTS,
        "n_present": ta.n_present,
        "n_absent": ta.n_absent,
        "n_extension_level": ta.n_extension_level,
        "n_weight_candidates": N_WEIGHT_CANDIDATES,
        "n_diagnostic_weights": tb.n_diagnostic,
        "n_effective_candidates": tb.n_effective_candidate,
        "born_rule_derived": td.born_rule_derived,
        "outcome_selection_derived": td.outcome_selection_derived,
        "decoherence_sufficient_for_probability": te.decoherence_sufficient_for_probability,
        "n_composite_adds_content": tf.n_adds_content,
        "n_manymode_adds_content": tg.n_adds_content,
        "n_extension_viable": th.n_viable,
        "n_nonclaims": N_QIIF_NONCLAIMS,
    }

    result = QIIFProbabilityDeterminationOutcomeResult(
        valid=True,
        track_a_eligibility=ta, track_b_weight_vs_prob=tb,
        track_c_determination=tc, track_d_outcome=td,
        track_e_decoherence_boundary=te, track_f_composite=tf,
        track_g_manymode=tg, track_h_extension=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        probability_verdict=tb.probability_verdict,
        determination_verdict=tc.determination_verdict,
        outcome_verdict=td.outcome_verdict,
        extension_route_verdict=th.extension_route_verdict,
        authorization_verdict=tj.authorization_verdict,
        qiif_appendix_p_class=QIIF_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIIF_NONCLAIMS,
        diagnostics=diagnostics,
    )
    validate_qiif_result(result)
    return result


def validate_qiif_result(result: QIIFProbabilityDeterminationOutcomeResult) -> None:
    checks = [
        (result.probability_verdict, ALLOWED_PROBABILITY_VERDICTS, "Probability"),
        (result.determination_verdict, ALLOWED_DETERMINATION_VERDICTS, "Determination"),
        (result.outcome_verdict, ALLOWED_OUTCOME_VERDICTS, "Outcome"),
        (result.extension_route_verdict, ALLOWED_EXTENSION_ROUTE_VERDICTS, "Extension route"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.qiif_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class not in allowed")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}': class not in allowed")
    if result.track_k_nonclaims.n_nonclaims != N_QIIF_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.qiig_authorized:
        raise ValueError("qiig_authorized must be True")
    if result.track_d_outcome.born_rule_derived:
        raise ValueError("born_rule_derived must be False")
    if result.track_d_outcome.outcome_selection_derived:
        raise ValueError("outcome_selection_derived must be False")
    if result.track_e_decoherence_boundary.decoherence_sufficient_for_probability:
        raise ValueError("decoherence_sufficient must be False")


def _self_test() -> bool:
    r = run_qiif_probability_determination_outcome_audit()
    assert r.valid is True
    assert r.probability_verdict == QIIF_PROBABILITY_VERDICT
    assert r.determination_verdict == QIIF_DETERMINATION_VERDICT
    assert r.outcome_verdict == QIIF_OUTCOME_VERDICT
    assert r.extension_route_verdict == QIIF_EXTENSION_ROUTE_VERDICT
    assert r.authorization_verdict == QIIF_AUTHORIZATION_VERDICT
    assert r.diagnostics["born_rule_derived"] is False
    assert r.diagnostics["outcome_selection_derived"] is False
    assert r.diagnostics["decoherence_sufficient_for_probability"] is False
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.F self-test passed.")
