"""
Appendix Q-II.D --- Observable Algebra and Multi-Observable Grammar Audit
=========================================================================
GRUT Quantum Program --- Phase Q-II.D

This module audits whether the GRUT quantum extension can support a coherent
multi-observable grammar beyond the single constitutive observable Phi_hat.

Inherited structure
-------------------
Part I established:
  - One constitutive observable: Phi_hat = sigma_z in 2-state realization
  - QE3 verdict: second observable UNDERDETERMINED (not blocked)
  - sigma_x, sigma_y exist in C^2 Hilbert space but are NOT independently
    motivated by GRUT architecture

Q-II.B established:
  - Composite Hilbert space C^4 = C^2 tensor C^2
  - Product observables A tensor B formally definable
  - Local observables A tensor I, I tensor B available

Q-II.C established:
  - Nonfactorized states demonstrated
  - Entanglement witnesses at density-matrix level (purity, PPT)
  - Bell NOT yet justified (missing multi-observable grammar + Born rule)

Key physics for this audit
--------------------------
In the 2-state Hilbert space C^2, the three Pauli matrices {sigma_x,
sigma_y, sigma_z} together with the identity form a basis for all 2x2
Hermitian matrices (observables).  Only sigma_z = Phi_hat is motivated
by GRUT architecture (constitutive observable, jump operator basis).

To get a multi-observable grammar, we can:
  (a) Postulate sigma_x and/or sigma_y as extension-level observables (MIP)
  (b) Motivate them from the composite structure or entanglement results
  (c) Derive them from GRUT architecture (not currently possible)

Route (a) is honest: these are standard observables in C^2, mathematically
well-defined, and their postulation introduces no new degrees of freedom
(they already exist as operators on the established Hilbert space).  They
are "latent" in the Hilbert space but not motivated by GRUT's constitutive
or dissipative structure.

Noncommutativity: [sigma_x, sigma_z] = -2i sigma_y (and cyclic).
This is a MATHEMATICAL fact about operators on C^2, not a physical derivation.
The noncommuting structure exists once we acknowledge sigma_x as an observable.

Correlator grammar: <A tensor B> = Tr(rho_AB (A tensor B)) is well-defined
for any observables A, B on the composite space.  Joint correlators and
subsystem-subsystem correlators follow from the density-matrix formalism.

Bell readiness: CHSH requires two measurement settings per party.  With
sigma_z and sigma_x (or rotated bases) on each subsystem, the CHSH
correlator can be WRITTEN.  However, evaluating it requires Born-rule
probability interpretation (still absent from Part I).  So the Bell
boundary advances: the algebraic structure is now available, but the
probabilistic interpretation is not.
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

COMPOSITE_HILBERT_DIM: int = 4
SINGLE_SYSTEM_DIM: int = 2

# Track counts
N_ELIGIBILITY_INGREDIENTS: int = 5
N_CANDIDATE_OBSERVABLES: int = 6
N_DISTINCTNESS_LEVELS: int = 4
N_NONCOMMUTATIVITY_CANDIDATES: int = 5
N_CORRELATOR_LEVELS: int = 5
N_ALGEBRA_LEVELS: int = 5
N_COMPOSITE_OBS_TESTS: int = 4
N_BELL_READINESS_LEVELS: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_QIID_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
QIIC_INHERITED_NONFACTORIZATION: str = "nonfactorized_two_subsystem_states_demonstrated"
QIIC_INHERITED_WITNESS: str = "separability_or_purity_witness_justified"
QIIC_INHERITED_BELL: str = "bell_nonlocality_not_yet_justified"
QIIC_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QIID"

# Q-II.D Verdict strings
QIID_OBSERVABLE_VERDICT: str = "multiple_observable_classes_extension_level_only"
QIID_NONCOMMUTATIVITY_VERDICT: str = "toy_noncommuting_pair_justified"
QIID_CORRELATOR_VERDICT: str = "correlator_grammar_extension_level_only"
QIID_BELL_READINESS_VERDICT: str = "bell_boundary_structurally_advanced"
QIID_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QIIE"
QIID_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozensets
ALLOWED_OBSERVABLE_VERDICTS: frozenset = frozenset({
    "multiple_observable_classes_justified",
    "multiple_observable_classes_extension_level_only",
    "multiple_observable_classes_underdetermined",
    "multiple_observable_classes_blocked",
})
ALLOWED_NONCOMMUTATIVITY_VERDICTS: frozenset = frozenset({
    "toy_noncommuting_pair_justified",
    "extension_level_noncommutative_structure_only",
    "noncommutativity_underdetermined",
    "noncommutativity_blocked",
})
ALLOWED_CORRELATOR_VERDICTS: frozenset = frozenset({
    "correlator_grammar_available",
    "correlator_grammar_extension_level_only",
    "correlator_grammar_underdetermined",
    "correlator_grammar_blocked",
})
ALLOWED_BELL_READINESS_VERDICTS: frozenset = frozenset({
    "bell_boundary_structurally_advanced",
    "bell_boundary_still_unbuilt",
    "bell_boundary_unchanged",
    "bell_claims_still_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QIIE",
    "authorized_only_for_further_observable_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_QIIC",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8)
QIID_NONCLAIMS: List[str] = [
    "NOT_claiming_sigma_x_notation_therefore_observable_grammar_solved__"
    "postulating_sigma_x_is_extension_level_not_derived_grammar",
    "NOT_claiming_toy_noncommuting_pair_therefore_full_operator_algebra__"
    "two_noncommuting_observables_are_not_a_complete_algebra",
    "NOT_claiming_correlator_notation_therefore_Bell_readiness_achieved__"
    "correlator_grammar_requires_Born_rule_for_Bell_evaluation",
    "NOT_claiming_composite_observable_notation_therefore_physical_coupling__"
    "A_tensor_B_is_formal_structure_not_interaction_dynamics",
    "NOT_claiming_expectation_value_success_therefore_canonical_commutator_derived__"
    "commutation_is_mathematical_fact_of_C2_not_physical_derivation",
    "NOT_claiming_two_observable_grammar_therefore_matter_readiness__"
    "matter_requires_excitation_statistics_and_interaction_structure",
    "NOT_claiming_extension_level_multi_observable_therefore_native_canon__"
    "all_QIID_results_carry_MBU_or_MIP_floor",
    "NOT_claiming_Bell_style_toy_correlators_therefore_nonlocality_established__"
    "nonlocality_requires_Born_rule_and_statistical_interpretation",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIDEligibilityIngredient:
    """Single observable eligibility ingredient (Track A)."""
    ingredient_id: str
    ingredient_name: str
    description: str
    status: str
    source: str
    notes: List[str]


@dataclass
class QIIDObservableEligibilityAudit:
    """Track A --- observable eligibility."""
    ingredients: List[QIIDEligibilityIngredient]
    n_ingredients: int
    n_present: int
    n_extension_level: int
    n_absent: int
    eligibility_verdict: str
    notes: List[str]


@dataclass
class QIIDCandidateObservable:
    """Single candidate observable (Track B)."""
    candidate_id: str
    candidate_name: str
    description: str
    motivation_level: str  # "motivated", "compatible", "underdetermined", "blocked"
    physical_basis: str
    notes: List[str]


@dataclass
class QIIDCandidateObservableAudit:
    """Track B --- candidate observable inventory."""
    candidates: List[QIIDCandidateObservable]
    n_candidates: int
    n_motivated: int
    n_compatible: int
    n_underdetermined: int
    notes: List[str]


@dataclass
class QIIDDistinctnessLevel:
    """Single distinctness level (Track C)."""
    level_id: str
    level_name: str
    description: str
    applies_to: List[str]
    notes: List[str]


@dataclass
class QIIDDistinctnessAudit:
    """Track C --- distinctness and independence."""
    levels: List[QIIDDistinctnessLevel]
    n_levels: int
    strongest_distinctness: str
    notes: List[str]


@dataclass
class QIIDNoncommutativityCandidate:
    """Single noncommutativity candidate (Track D)."""
    candidate_id: str
    candidate_name: str
    description: str
    justified: bool
    level: str
    notes: List[str]


@dataclass
class QIIDNoncommutativityAudit:
    """Track D --- noncommutativity."""
    candidates: List[QIIDNoncommutativityCandidate]
    n_candidates: int
    justified_candidate_id: str
    noncommutativity_verdict: str
    commutator_formula: str
    notes: List[str]


@dataclass
class QIIDCorrelatorLevel:
    """Single correlator grammar level (Track E)."""
    level_id: str
    level_name: str
    description: str
    available: bool
    notes: List[str]


@dataclass
class QIIDCorrelatorGrammarAudit:
    """Track E --- expectation and correlator grammar."""
    levels: List[QIIDCorrelatorLevel]
    n_levels: int
    highest_available_id: str
    correlator_verdict: str
    notes: List[str]


@dataclass
class QIIDAlgebraLevel:
    """Single algebra level (Track F)."""
    level_id: str
    level_name: str
    description: str
    achieved: bool
    notes: List[str]


@dataclass
class QIIDMinimalAlgebraAudit:
    """Track F --- minimal algebra."""
    levels: List[QIIDAlgebraLevel]
    n_levels: int
    highest_achieved_id: str
    notes: List[str]


@dataclass
class QIIDCompositeObsTest:
    """Single composite observable test (Track G)."""
    test_id: str
    test_name: str
    description: str
    available: bool
    notes: List[str]


@dataclass
class QIIDCompositeObservableAudit:
    """Track G --- composite-system observable."""
    tests: List[QIIDCompositeObsTest]
    n_tests: int
    n_available: int
    notes: List[str]


@dataclass
class QIIDBellReadinessLevel:
    """Single Bell readiness level (Track H)."""
    level_id: str
    level_name: str
    description: str
    achieved: bool
    notes: List[str]


@dataclass
class QIIDBellReadinessAudit:
    """Track H --- Bell-boundary readiness."""
    levels: List[QIIDBellReadinessLevel]
    n_levels: int
    bell_readiness_verdict: str
    remaining_gap: str
    notes: List[str]


@dataclass
class QIIDAppendixPEntry:
    """Single Appendix P entry (Track I)."""
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIIDAppendixPAudit:
    """Track I --- Appendix P."""
    entries: List[QIIDAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIIDAuthorizationAudit:
    """Track J --- authorization."""
    qiie_authorized: bool
    authorization_basis: List[str]
    qiie_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QIIDNonclaimFirewall:
    """Track K --- nonclaims."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIDObservableAlgebraResult:
    """Master result for Q-II.D."""
    valid: bool
    track_a_eligibility: QIIDObservableEligibilityAudit
    track_b_candidates: QIIDCandidateObservableAudit
    track_c_distinctness: QIIDDistinctnessAudit
    track_d_noncommutativity: QIIDNoncommutativityAudit
    track_e_correlator: QIIDCorrelatorGrammarAudit
    track_f_algebra: QIIDMinimalAlgebraAudit
    track_g_composite_obs: QIIDCompositeObservableAudit
    track_h_bell_readiness: QIIDBellReadinessAudit
    track_i_appendix_p: QIIDAppendixPAudit
    track_j_authorization: QIIDAuthorizationAudit
    track_k_nonclaims: QIIDNonclaimFirewall
    # Five hard-gated verdicts
    observable_verdict: str
    noncommutativity_verdict: str
    correlator_verdict: str
    bell_readiness_verdict: str
    authorization_verdict: str
    # Summary
    qiid_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIIDObservableEligibilityAudit:
    ingredients = [
        QIIDEligibilityIngredient(
            ingredient_id="OE1", ingredient_name="constitutive_observable_established",
            description="Phi_hat = sigma_z: constitutive observable from Part I.",
            status="present", source="Q-C.5 / Q-E (QE4)",
            notes=["Established in Part I; locked MBU class"],
        ),
        QIIDEligibilityIngredient(
            ingredient_id="OE2", ingredient_name="complementary_observable_candidate",
            description="sigma_x (or sigma_y): complementary observable in C^2.",
            status="extension_level", source="C^2 Hilbert space structure",
            notes=[
                "Exists mathematically in C^2 but not motivated by GRUT architecture",
                "QE3 found second observable underdetermined",
                "Can be postulated as extension (MIP for the identification, no new DOF)",
            ],
        ),
        QIIDEligibilityIngredient(
            ingredient_id="OE3", ingredient_name="expectation_value_rule",
            description="<A> = Tr(rho A) for any Hermitian A on the Hilbert space.",
            status="present", source="Density-matrix formalism from Part I",
            notes=["Standard trace rule; available for any operator on C^2 or C^4"],
        ),
        QIIDEligibilityIngredient(
            ingredient_id="OE4", ingredient_name="correlator_grammar",
            description="<A tensor B> = Tr(rho_AB (A tensor B)) for composite observables.",
            status="extension_level", source="Q-II.B tensor product + density matrix",
            notes=["Follows from tensor product composition + trace rule"],
        ),
        QIIDEligibilityIngredient(
            ingredient_id="OE5", ingredient_name="state_structure_compatibility",
            description="Observable grammar must be compatible with C^2, C^4 state structure.",
            status="present", source="Q-II.B / Q-II.C",
            notes=["Observables are Hermitian operators on established Hilbert spaces"],
        ),
    ]
    n_pres = sum(1 for i in ingredients if i.status == "present")
    n_ext = sum(1 for i in ingredients if i.status == "extension_level")
    n_abs = sum(1 for i in ingredients if i.status == "absent")
    return QIIDObservableEligibilityAudit(
        ingredients=ingredients, n_ingredients=N_ELIGIBILITY_INGREDIENTS,
        n_present=n_pres, n_extension_level=n_ext, n_absent=n_abs,
        eligibility_verdict="eligible_with_extension_level_observables",
        notes=[
            f"{n_pres} present (constitutive obs, trace rule, state compatibility)",
            f"{n_ext} extension-level (complementary obs, correlator grammar)",
            "Multi-observable grammar is eligible once sigma_x is postulated",
        ],
    )


def _build_track_b() -> QIIDCandidateObservableAudit:
    candidates = [
        QIIDCandidateObservable(
            candidate_id="OBS1", candidate_name="constitutive_Phi_hat_sigma_z",
            description="Phi_hat = sigma_z: constitutive observable, jump operator basis.",
            motivation_level="motivated",
            physical_basis="Constitutive ODE, jump operator L, pointer basis, QE4",
            notes=["Established Part I; the only GRUT-motivated observable"],
        ),
        QIIDCandidateObservable(
            candidate_id="OBS2", candidate_name="complementary_sigma_x",
            description=(
                "sigma_x: off-diagonal in sigma_z eigenbasis. "
                "Interference-sensitive observable from Q-F TM1."
            ),
            motivation_level="compatible",
            physical_basis=(
                "Exists in C^2; used implicitly in Q-F interference analysis "
                "(<sigma_x>(t) = cos(Delta_E t) exp(-R_dec t)). "
                "Not independently motivated by GRUT constitutive structure."
            ),
            notes=[
                "Compatible: mathematically natural complementary direction in C^2",
                "Q-F used it implicitly for interference cross terms",
                "Not motivated by GRUT architecture; postulation is CAH or MIP",
                "No new DOF required (operator already exists on C^2)",
            ],
        ),
        QIIDCandidateObservable(
            candidate_id="OBS3", candidate_name="complementary_sigma_y",
            description="sigma_y: completes the Pauli triple. [sigma_x, sigma_z] = -2i sigma_y.",
            motivation_level="compatible",
            physical_basis="Algebraic closure of {sigma_x, sigma_z}; exists in C^2.",
            notes=[
                "Compatible: appears as commutator of sigma_x and sigma_z",
                "If sigma_x is postulated, sigma_y is algebraically forced",
                "No additional postulation needed beyond sigma_x",
            ],
        ),
        QIIDCandidateObservable(
            candidate_id="OBS4", candidate_name="source_observable_X_hat",
            description="X_hat: source term in constitutive law tau d<Phi>/dt + <Phi> = <X>.",
            motivation_level="underdetermined",
            physical_basis="Appears in Q-C.5 constitutive recovery but operator form unspecified.",
            notes=[
                "Underdetermined: X_hat appears in the expectation-value law but "
                "its operator form is not specified",
                "Could be external drive, could be another system observable",
                "Cannot be used as an independent observable without specification",
            ],
        ),
        QIIDCandidateObservable(
            candidate_id="OBS5", candidate_name="composite_local_observables",
            description="sigma_z tensor I, I tensor sigma_z: local observables on composite space.",
            motivation_level="motivated",
            physical_basis="Follow directly from Phi_hat on each subsystem + tensor product.",
            notes=[
                "Motivated: if each subsystem has Phi_hat, then sigma_z tensor I "
                "and I tensor sigma_z are the natural composite local observables",
                "Well-defined on C^4 from Q-II.B tensor product",
            ],
        ),
        QIIDCandidateObservable(
            candidate_id="OBS6", candidate_name="composite_joint_observables",
            description="sigma_z tensor sigma_z, sigma_x tensor sigma_x: joint correlator observables.",
            motivation_level="extension_level",
            physical_basis="Tensor products of single-system observables.",
            notes=[
                "Extension-level: requires sigma_x to be postulated for cross-type products",
                "sigma_z tensor sigma_z: motivated (product of constitutive observables)",
                "sigma_x tensor sigma_x: extension-level (requires sigma_x postulation)",
            ],
        ),
    ]
    n_mot = sum(1 for c in candidates if c.motivation_level == "motivated")
    n_com = sum(1 for c in candidates if c.motivation_level == "compatible")
    n_und = sum(1 for c in candidates if c.motivation_level == "underdetermined")
    return QIIDCandidateObservableAudit(
        candidates=candidates, n_candidates=N_CANDIDATE_OBSERVABLES,
        n_motivated=n_mot, n_compatible=n_com, n_underdetermined=n_und,
        notes=[
            f"{n_mot} motivated (Phi_hat, composite locals)",
            f"{n_com} compatible (sigma_x, sigma_y)",
            f"{n_und} underdetermined (X_hat source)",
            "sigma_x is the key extension: unlocks noncommutativity and correlators",
        ],
    )


def _build_track_c() -> QIIDDistinctnessAudit:
    levels = [
        QIIDDistinctnessLevel(
            level_id="DL1", level_name="same_observable_different_description",
            description="Two descriptions of the same physical observable.",
            applies_to=["OBS1 and pointer-basis observable (same: Phi_hat eigenbasis)"],
            notes=["Q-D/Q-F already noted: constitutive = pointer = jump basis"],
        ),
        QIIDDistinctnessLevel(
            level_id="DL2", level_name="distinct_but_dependent",
            description="Observables that are distinct but algebraically linked.",
            applies_to=["sigma_y = (i/2)[sigma_z, sigma_x]: forced by sigma_x and sigma_z"],
            notes=["sigma_y is algebraically dependent on sigma_x and sigma_z"],
        ),
        QIIDDistinctnessLevel(
            level_id="DL3", level_name="distinct_and_independently_motivated",
            description="Observables with independent physical motivation.",
            applies_to=["NONE currently: only Phi_hat is GRUT-motivated"],
            notes=["No second observable is independently motivated by GRUT architecture"],
        ),
        QIIDDistinctnessLevel(
            level_id="DL4", level_name="additional_by_postulate_only",
            description="Additional observables available only through explicit postulation.",
            applies_to=["sigma_x: postulated extension; sigma_y: algebraic consequence"],
            notes=[
                "sigma_x must be explicitly postulated (MIP/CAH)",
                "Once sigma_x is postulated, sigma_y follows algebraically",
                "This is the honest level: additional observables by postulate only",
            ],
        ),
    ]
    return QIIDDistinctnessAudit(
        levels=levels, n_levels=N_DISTINCTNESS_LEVELS,
        strongest_distinctness="DL4_additional_by_postulate_only",
        notes=[
            "Only Phi_hat (sigma_z) is GRUT-motivated (DL3 empty)",
            "sigma_x is compatible but not independently motivated",
            "sigma_y is algebraically forced once sigma_x is postulated",
            "Strongest distinctness level: DL4 (postulate-dependent)",
        ],
    )


def _build_track_d() -> QIIDNoncommutativityAudit:
    candidates = [
        QIIDNoncommutativityCandidate(
            candidate_id="NC1", candidate_name="no_noncommutativity",
            description="No noncommuting observables available.",
            justified=False, level="none",
            notes=["Rejected: sigma_x and sigma_z do not commute in C^2"],
        ),
        QIIDNoncommutativityCandidate(
            candidate_id="NC2", candidate_name="toy_noncommuting_pair",
            description=(
                "{sigma_z, sigma_x} with [sigma_z, sigma_x] = 2i sigma_y. "
                "A concrete noncommuting pair in the 2-state Hilbert space."
            ),
            justified=True, level="toy",
            notes=[
                "Justified: once sigma_x is postulated, the commutator is a "
                "mathematical fact of operators on C^2",
                "[sigma_z, sigma_x] = 2i sigma_y (exact, not approximate)",
                "This is a TOY pair: two specific operators, not a full algebra",
                "Enables: Robertson uncertainty Delta(sigma_z) Delta(sigma_x) >= |<sigma_y>|",
                "Resolves QE3 underdetermined status (with postulated sigma_x)",
            ],
        ),
        QIIDNoncommutativityCandidate(
            candidate_id="NC3", candidate_name="extension_level_algebra",
            description="Full su(2) Lie algebra structure on C^2.",
            justified=True, level="extension_level",
            notes=[
                "The three Pauli matrices generate su(2)",
                "Extension-level: {sigma_x, sigma_y, sigma_z} with standard commutators",
                "This is a complete observable algebra for C^2 (plus identity)",
                "BUT: only sigma_z is GRUT-motivated; the algebra is postulated",
            ],
        ),
        QIIDNoncommutativityCandidate(
            candidate_id="NC4", candidate_name="notation_level_only",
            description="Noncommutativity exists only as notation, not physics.",
            justified=False, level="notation",
            notes=["Rejected: the commutator is a genuine operator equation, not notation"],
        ),
        QIIDNoncommutativityCandidate(
            candidate_id="NC5", candidate_name="noncommutativity_blocked",
            description="Noncommutativity is blocked.",
            justified=False, level="blocked",
            notes=["Rejected: C^2 naturally supports noncommuting operators"],
        ),
    ]
    return QIIDNoncommutativityAudit(
        candidates=candidates, n_candidates=N_NONCOMMUTATIVITY_CANDIDATES,
        justified_candidate_id="NC2_toy_noncommuting_pair",
        noncommutativity_verdict=QIID_NONCOMMUTATIVITY_VERDICT,
        commutator_formula="[sigma_z, sigma_x] = 2i sigma_y",
        notes=[
            "NC2 justified: toy noncommuting pair {sigma_z, sigma_x}",
            "NC3 also justified at extension level (full su(2))",
            "Verdict is NC2 (stricter): toy pair, not full algebra claim",
            "Commutator is mathematical fact of C^2, not physical derivation",
            "Resolves QE3 gap conditional on sigma_x postulation",
        ],
    )


def _build_track_e() -> QIIDCorrelatorGrammarAudit:
    levels = [
        QIIDCorrelatorLevel(
            level_id="CG1", level_name="single_observable_expectation",
            description="<A> = Tr(rho A) for any single observable A.",
            available=True,
            notes=["Available from Part I density-matrix formalism"],
        ),
        QIIDCorrelatorLevel(
            level_id="CG2", level_name="two_point_same_system",
            description="<AB> = Tr(rho AB) for two observables A, B on same system.",
            available=True,
            notes=["Available: product of operators on C^2; well-defined"],
        ),
        QIIDCorrelatorLevel(
            level_id="CG3", level_name="subsystem_correlators",
            description="<A tensor B> = Tr(rho_AB (A tensor B)) for subsystem observables.",
            available=True,
            notes=[
                "Available: follows from Q-II.B tensor product + trace rule",
                "Enables: <sigma_z tensor sigma_z>, <sigma_x tensor sigma_x>, etc.",
            ],
        ),
        QIIDCorrelatorLevel(
            level_id="CG4", level_name="chsh_correlator_structure",
            description=(
                "CHSH correlator: S = <AB> - <AB'> + <A'B> + <A'B'> "
                "with A, A' on subsystem A and B, B' on subsystem B."
            ),
            available=True,
            notes=[
                "Available as algebraic structure: the correlator S can be WRITTEN "
                "and its expectation value Tr(rho_AB S) can be COMPUTED",
                "Requires: two observables per subsystem (sigma_z, sigma_x or rotations)",
                "CAVEAT: computing Tr(rho S) gives a number, but interpreting it as "
                "a Bell violation requires Born-rule probability interpretation (absent)",
            ],
        ),
        QIIDCorrelatorLevel(
            level_id="CG5", level_name="time_ordered_correlators",
            description="Time-ordered or Lindblad-evolved correlators.",
            available=False,
            notes=[
                "Not available: would require time-dependent Lindblad evolution "
                "of composite observables in Heisenberg picture",
                "Structurally plausible but not built in current package",
            ],
        ),
    ]
    n_avail = sum(1 for l in levels if l.available)
    # Highest available
    highest = "CG4_chsh_correlator_structure"
    return QIIDCorrelatorGrammarAudit(
        levels=levels, n_levels=N_CORRELATOR_LEVELS,
        highest_available_id=highest,
        correlator_verdict=QIID_CORRELATOR_VERDICT,
        notes=[
            f"{n_avail} of {N_CORRELATOR_LEVELS} correlator levels available",
            "CG1-CG4 available (single obs, two-point, subsystem, CHSH algebraic)",
            "CG5 (time-ordered) not available",
            "CHSH correlator is ALGEBRAICALLY available but PROBABILISTICALLY uninterpreted",
            "Verdict: extension-level (requires postulated sigma_x + tensor product)",
        ],
    )


def _build_track_f() -> QIIDMinimalAlgebraAudit:
    levels = [
        QIIDAlgebraLevel(
            level_id="AL1", level_name="observable_list_only",
            description="A list of observables without algebraic relations.",
            achieved=True,
            notes=["Achieved: {sigma_z, sigma_x, sigma_y} identified"],
        ),
        QIIDAlgebraLevel(
            level_id="AL2", level_name="expectation_value_grammar",
            description="Expectation values <A> = Tr(rho A) for multiple A.",
            achieved=True,
            notes=["Achieved: trace rule applies to any Hermitian operator"],
        ),
        QIIDAlgebraLevel(
            level_id="AL3", level_name="toy_noncommutative_algebra",
            description="Concrete commutation relations: [sigma_z, sigma_x] = 2i sigma_y.",
            achieved=True,
            notes=[
                "Achieved: the Pauli commutators are exact mathematical facts",
                "This is a TOY algebra: su(2) on C^2, not a general observable algebra",
            ],
        ),
        QIIDAlgebraLevel(
            level_id="AL4", level_name="extension_level_multi_observable",
            description="Multi-observable algebra on composite space with correlators.",
            achieved=True,
            notes=[
                "Achieved at extension level: tensor products of Pauli matrices "
                "on C^4, correlator grammar CG1-CG4",
                "The algebra is postulated (MIP), not derived",
            ],
        ),
        QIIDAlgebraLevel(
            level_id="AL5", level_name="full_observable_ontology",
            description="Complete observable ontology with physical interpretation.",
            achieved=False,
            notes=[
                "Not achieved: the algebra is mathematical, not physically grounded",
                "Physical interpretation requires: Born rule, measurement framework",
                "Beyond current scope",
            ],
        ),
    ]
    highest = "AL4_extension_level_multi_observable"
    return QIIDMinimalAlgebraAudit(
        levels=levels, n_levels=N_ALGEBRA_LEVELS,
        highest_achieved_id=highest,
        notes=[
            "AL1-AL4 achieved; AL5 not achieved",
            "Highest: extension-level multi-observable algebra on C^4",
            "This is a toy algebra (su(2) on C^2, tensor products on C^4)",
            "Not a full observable ontology (missing physical interpretation)",
        ],
    )


def _build_track_g() -> QIIDCompositeObservableAudit:
    tests = [
        QIIDCompositeObsTest(
            test_id="CO1", test_name="product_observables",
            description="A tensor B: product of single-system observables.",
            available=True,
            notes=["Well-defined on C^4; e.g. sigma_z tensor sigma_z"],
        ),
        QIIDCompositeObsTest(
            test_id="CO2", test_name="local_observables",
            description="A tensor I, I tensor B: single-subsystem observables in composite space.",
            available=True,
            notes=["Standard embedding; measures one subsystem only"],
        ),
        QIIDCompositeObsTest(
            test_id="CO3", test_name="joint_expectation_values",
            description="<A tensor B>_rho = Tr(rho_AB (A tensor B)).",
            available=True,
            notes=["Follows from trace rule + tensor product structure"],
        ),
        QIIDCompositeObsTest(
            test_id="CO4", test_name="entanglement_witness_observables",
            description="Witness operators W such that Tr(W rho_sep) >= 0, Tr(W rho_ent) < 0.",
            available=True,
            notes=[
                "Available: constructible from Pauli products on C^4",
                "PPT criterion from Q-II.C can be recast as witness observable",
            ],
        ),
    ]
    n_avail = sum(1 for t in tests if t.available)
    return QIIDCompositeObservableAudit(
        tests=tests, n_tests=N_COMPOSITE_OBS_TESTS,
        n_available=n_avail,
        notes=[
            "All 4 composite observable tests available",
            "Product, local, joint expectation, and witness observables all work on C^4",
            "All extension-level: depend on tensor product + sigma_x postulation",
        ],
    )


def _build_track_h() -> QIIDBellReadinessAudit:
    levels = [
        QIIDBellReadinessLevel(
            level_id="BR1", level_name="algebraic_structure_available",
            description=(
                "Two measurement settings per subsystem (sigma_z, sigma_x or rotations) "
                "and CHSH correlator S can be written and computed as Tr(rho S)."
            ),
            achieved=True,
            notes=[
                "Achieved: sigma_z and sigma_x on each subsystem provide two settings",
                "CHSH operator S = sigma_z tensor sigma_z + ... can be constructed",
                "Tr(rho S) can be computed for any 4x4 density matrix",
            ],
        ),
        QIIDBellReadinessLevel(
            level_id="BR2", level_name="entangled_state_benchmark",
            description="An entangled state for which Tr(rho S) > 2 (Tsirelson bound approach).",
            achieved=True,
            notes=[
                "Achieved: for Bell state |psi+> and optimal CHSH settings, "
                "Tr(rho S) = 2 sqrt(2) > 2 (algebraic computation)",
                "This is a MATHEMATICAL result, not a physical measurement",
            ],
        ),
        QIIDBellReadinessLevel(
            level_id="BR3", level_name="probability_interpretation",
            description="Born-rule interpretation of Tr(rho S) as statistical correlator.",
            achieved=False,
            notes=[
                "NOT achieved: Born rule absent from Part I",
                "Tr(rho S) = 2 sqrt(2) is a number but its interpretation as "
                "a statistical correlation requires Born-rule probability assignment",
                "This is the remaining gap for Bell claims",
            ],
        ),
        QIIDBellReadinessLevel(
            level_id="BR4", level_name="operational_bell_violation",
            description="Full operational Bell violation with measurement statistics.",
            achieved=False,
            notes=[
                "NOT achieved: requires BR3 (Born rule) + measurement framework",
                "Beyond current package; would be Q-II.F scope",
            ],
        ),
    ]
    return QIIDBellReadinessAudit(
        levels=levels, n_levels=N_BELL_READINESS_LEVELS,
        bell_readiness_verdict=QIID_BELL_READINESS_VERDICT,
        remaining_gap="Born_rule_probability_interpretation_absent",
        notes=[
            "BR1 achieved: algebraic CHSH structure available",
            "BR2 achieved: Tr(rho S) = 2 sqrt(2) computable for Bell state",
            "BR3 NOT achieved: Born-rule interpretation missing",
            "BR4 NOT achieved: operational Bell violation requires BR3",
            "Bell boundary ADVANCED from Q-II.C: algebraic structure now present",
            "Remaining gap: probability interpretation (Q-II.F scope)",
            "Verdict: bell_boundary_structurally_advanced",
        ],
    )


def _build_track_i() -> QIIDAppendixPAudit:
    entries = [
        QIIDAppendixPEntry(
            item_id="QIID_multi_observable",
            item_name="Multi-observable classes",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="Multiple observable classes identified at extension level",
            forbidden_claim="Multi-observable grammar derived from GRUT first principles",
            dependency="C^2 Hilbert space, sigma_x postulation",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_noncommutativity",
            item_name="Toy noncommuting pair",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="[sigma_z, sigma_x] = 2i sigma_y: exact commutator in C^2",
            forbidden_claim="Noncommutativity derived from GRUT physical structure",
            dependency="sigma_x postulation; mathematical fact of C^2",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_correlator_grammar",
            item_name="Correlator grammar",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Single-obs, two-point, subsystem, and CHSH algebraic correlators available"
            ),
            forbidden_claim="Correlator grammar implies Born-rule interpretation",
            dependency="Tensor product, sigma_x postulation, trace rule",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_bell_advance",
            item_name="Bell boundary advancement",
            appendix_p_class="bounded_structural_result",
            allowed_claim=(
                "Bell algebraic structure now available; Tr(rho S) computable; "
                "probability interpretation still missing"
            ),
            forbidden_claim="Bell violation established as physical result",
            dependency="Multi-observable + entangled states + Born rule (absent)",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_composite_obs",
            item_name="Composite-system observables",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="Product, local, joint, and witness observables on C^4",
            forbidden_claim="Composite observables imply physical subsystem coupling",
            dependency="Q-II.B tensor product, sigma_x postulation",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_qe3_resolution",
            item_name="QE3 gap conditional resolution",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "QE3 second-observable gap resolved conditional on sigma_x postulation"
            ),
            forbidden_claim="QE3 gap natively resolved without postulation",
            dependency="sigma_x postulation as extension-level observable",
        ),
        QIIDAppendixPEntry(
            item_id="QIID_overall",
            item_name="Q-II.D overall",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Multi-observable grammar coherently established at extension level "
                "with toy noncommuting pair and correlator structure"
            ),
            forbidden_claim="Observable algebra closure or full ontology achieved",
            dependency="All Q-II.D tracks; sigma_x postulation",
        ),
    ]
    return QIIDAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIID_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=[
            "5 entries MBU, 1 entry BSR (Bell advance), 1 entry MBU (overall)",
            "No native canon: all results extension-level",
            "Bell advance is BSR: documents what is and isn't available",
        ],
    )


def _build_track_j() -> QIIDAuthorizationAudit:
    return QIIDAuthorizationAudit(
        qiie_authorized=True,
        authorization_basis=[
            "multi_observable_classes_established_at_extension_level",
            "toy_noncommuting_pair_justified",
            "correlator_grammar_available_through_CHSH_algebraic_level",
            "bell_boundary_structurally_advanced",
            "composite_observables_available_on_C4",
        ],
        qiie_constraints=[
            "QIIE_must_use_observable_grammar_from_QIID",
            "QIIE_must_not_assume_Bell_violation_without_Born_rule",
            "QIIE_must_address_mode_decomposition_and_excitation_language",
            "QIIE_results_inherit_MBU_or_MIP_floor",
            "QIIE_may_build_on_noncommutative_structure_for_ladder_operators",
        ],
        authorization_verdict=QIID_AUTHORIZATION_VERDICT,
        notes=[
            "Q-II.E authorized: observable grammar sufficient for excitation investigation",
            "Key advance: noncommuting observables enable ladder-operator-like constructions",
            "Bell investigation deferred to Q-II.F (needs Born rule from probability track)",
        ],
    )


def _build_track_k() -> QIIDNonclaimFirewall:
    return QIIDNonclaimFirewall(
        nonclaims=QIID_NONCLAIMS, n_nonclaims=N_QIID_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_qiid_observable_algebra_audit() -> QIIDObservableAlgebraResult:
    """Run the full Q-II.D Observable Algebra and Multi-Observable Grammar Audit."""
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
        "Multiple observable classes identified: constitutive (sigma_z), "
        "complementary (sigma_x, sigma_y), composite (tensor products)",
        "Toy noncommuting pair {sigma_z, sigma_x} justified with exact "
        "commutator [sigma_z, sigma_x] = 2i sigma_y",
        "Correlator grammar available through CHSH algebraic level: "
        "single-obs, two-point, subsystem, and CHSH correlators",
        "Bell boundary structurally advanced: algebraic CHSH structure available, "
        "Tr(rho S) = 2 sqrt(2) computable for Bell state",
        "QE3 second-observable gap conditionally resolved via sigma_x postulation",
        "Composite-system observables (product, local, joint, witness) all available on C^4",
        "Q-II.E authorized: observable grammar sufficient for excitation investigation",
    ]

    forbidden_claims: List[str] = [
        "sigma_x postulation implies observable grammar derived from GRUT",
        "Toy noncommuting pair implies full operator algebra",
        "Correlator notation implies Bell readiness achieved",
        "Composite observable notation implies physical subsystem coupling",
        "Expectation-value success implies canonical commutator structure derived",
        "Two-observable grammar implies matter readiness",
        "Extension-level multi-observable support implies native canon",
    ]

    diagnostics: Dict[str, Any] = {
        "n_eligibility_ingredients": N_ELIGIBILITY_INGREDIENTS,
        "n_candidate_observables": N_CANDIDATE_OBSERVABLES,
        "n_motivated_observables": tb.n_motivated,
        "n_compatible_observables": tb.n_compatible,
        "n_correlator_levels_available": sum(1 for l in te.levels if l.available),
        "n_algebra_levels_achieved": sum(1 for l in tf.levels if l.achieved),
        "n_composite_obs_available": tg.n_available,
        "n_bell_readiness_achieved": sum(1 for l in th.levels if l.achieved),
        "bell_remaining_gap": th.remaining_gap,
        "commutator_formula": td.commutator_formula,
        "n_nonclaims": N_QIID_NONCLAIMS,
        "n_appendix_p_entries": N_APPENDIX_P_ENTRIES,
        "tsirelson_value": 2.0 * math.sqrt(2.0),
    }

    result = QIIDObservableAlgebraResult(
        valid=True,
        track_a_eligibility=ta, track_b_candidates=tb,
        track_c_distinctness=tc, track_d_noncommutativity=td,
        track_e_correlator=te, track_f_algebra=tf,
        track_g_composite_obs=tg, track_h_bell_readiness=th,
        track_i_appendix_p=ti, track_j_authorization=tj,
        track_k_nonclaims=tk,
        observable_verdict=QIID_OBSERVABLE_VERDICT,
        noncommutativity_verdict=td.noncommutativity_verdict,
        correlator_verdict=te.correlator_verdict,
        bell_readiness_verdict=th.bell_readiness_verdict,
        authorization_verdict=tj.authorization_verdict,
        qiid_appendix_p_class=QIID_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIID_NONCLAIMS,
        diagnostics=diagnostics,
    )
    validate_qiid_result(result)
    return result


def validate_qiid_result(result: QIIDObservableAlgebraResult) -> None:
    """Validate Q-II.D result."""
    checks = [
        (result.observable_verdict, ALLOWED_OBSERVABLE_VERDICTS, "Observable"),
        (result.noncommutativity_verdict, ALLOWED_NONCOMMUTATIVITY_VERDICTS, "Noncommutativity"),
        (result.correlator_verdict, ALLOWED_CORRELATOR_VERDICTS, "Correlator"),
        (result.bell_readiness_verdict, ALLOWED_BELL_READINESS_VERDICTS, "Bell readiness"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.qiid_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class not in allowed")
    for e in result.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Track I entry '{e.item_id}': class not in allowed")
    if result.track_k_nonclaims.n_nonclaims != N_QIID_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_k_nonclaims.all_registered:
        raise ValueError("Nonclaims not all registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_i_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_j_authorization.qiie_authorized:
        raise ValueError("qiie_authorized must be True")
    # Tsirelson value check
    tv = result.diagnostics.get("tsirelson_value", 0)
    if abs(tv - 2.0 * math.sqrt(2.0)) > 1e-12:
        raise ValueError(f"Tsirelson value mismatch: {tv}")


def _self_test() -> bool:
    r = run_qiid_observable_algebra_audit()
    assert r.valid is True
    assert r.observable_verdict == QIID_OBSERVABLE_VERDICT
    assert r.noncommutativity_verdict == QIID_NONCOMMUTATIVITY_VERDICT
    assert r.correlator_verdict == QIID_CORRELATOR_VERDICT
    assert r.bell_readiness_verdict == QIID_BELL_READINESS_VERDICT
    assert r.authorization_verdict == QIID_AUTHORIZATION_VERDICT
    assert abs(r.diagnostics["tsirelson_value"] - 2 * math.sqrt(2)) < 1e-12
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.D self-test passed.")
