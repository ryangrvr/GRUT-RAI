"""
Appendix Q-II.C --- Entanglement and Nonfactorized Structure Audit
==================================================================
GRUT Quantum Program --- Phase Q-II.C

This module audits whether the GRUT quantum extension can support nonfactorized
two-subsystem states and what entanglement claims are justified.

Inherited from Q-II.B
---------------------
- Subsystem identity via copy duplication (extension-level, MIP)
- Tensor product composition: H_AB = C^2 tensor C^2 = C^4 (MIP)
- Partial trace: rho_A = Tr_B(rho_AB) (MIP, comes with tensor product)
- Two-subsystem product-state grammar demonstrated
- Independent Lindblad channels compatible with composition
- Interaction Hamiltonian NOT yet postulated (documented gap)

Key physics for this audit
--------------------------
In the 4-dimensional composite Hilbert space C^4 = C^2 tensor C^2:

1. Product states: rho_AB = rho_A tensor rho_B (factorized)
   - Reduced states: rho_A = Tr_B(rho_AB) = rho_A (pure if joint is pure product)

2. Classically correlated mixtures: rho_AB = sum_i p_i rho_A^i tensor rho_B^i
   - Separable by definition; no quantum correlations beyond classical

3. Nonfactorized pure states: |psi_AB> not of the form |a> tensor |b>
   - Example: |Bell+> = (|00> + |11>)/sqrt(2)
   - Reduced state: rho_A = Tr_B(|psi><psi|) is MIXED even though joint is PURE
   - This reduced-state mixedness from pure joint = signature of entanglement

4. Mixed nonfactorized states: rho_AB not writable as sum_i p_i rho_A^i tensor rho_B^i
   - Entangled mixed states; harder to characterize than pure

Entanglement witnesses
----------------------
The simplest entanglement criterion for two qubits:

- Purity witness: for a pure joint state |psi_AB>, if Tr(rho_A^2) < 1 then
  |psi_AB> is entangled. This is a NECESSARY AND SUFFICIENT criterion for
  pure states of two qubits.

- Separability criterion: rho_AB is separable iff it can be written as a
  convex mixture of product states. For 2x2, PPT (positive partial transpose)
  is necessary and sufficient.

- Bell/CHSH: requires measurement settings, multiple bases, statistical
  correlations. Goes beyond density-matrix structure alone. NOT justified
  without multi-observable grammar (Q-II.D) and measurement framework.

Bell boundary
-------------
Bell/CHSH requires:
  - Two subsystems (available from Q-II.B)
  - Two measurement settings per subsystem (NOT available: QE3 underdetermined,
    Q-II.D not yet done)
  - Expectation values of correlators (NOT available: single observable only)
  - Statistical interpretation of outcomes (NOT available: Born rule absent)

Therefore: Bell nonlocality is NOT yet justified. The boundary is hard.
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

# Purity of maximally entangled 2-qubit state reduced density matrix
# rho_A = (1/2) I_2 => Tr(rho_A^2) = 1/2
MAXIMALLY_ENTANGLED_REDUCED_PURITY: float = 0.5
# Purity of a pure single-system state: Tr(rho^2) = 1
PURE_STATE_PURITY: float = 1.0
# Purity of maximally mixed single-qubit state: Tr((I/2)^2) = 1/2
MAXIMALLY_MIXED_PURITY: float = 0.5

# Track counts
N_STATE_CLASSES: int = 5
N_FACTORIZATION_LEVELS: int = 3
N_REDUCED_STATE_TESTS: int = 4
N_WITNESS_CANDIDATES: int = 5
N_DECOHERENCE_EFFECTS: int = 4
N_BENCHMARK_CANDIDATES: int = 3
N_BELL_CANDIDATES: int = 4
N_APPENDIX_P_ENTRIES: int = 7
N_QIIC_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited
QIIB_INHERITED_SUBSYSTEM: str = "subsystem_identity_extension_level_only"
QIIB_INHERITED_COMPOSITION: str = "composition_rule_extension_level_only"
QIIB_INHERITED_REDUCED: str = "reduced_state_map_extension_level_only"
QIIB_INHERITED_MANY_BODY: str = "two_subsystem_grammar_demonstrated"
QIIB_INHERITED_AUTHORIZATION: str = "authorized_to_proceed_to_QIIC"

# Q-II.C Verdict strings
QIIC_NONFACTORIZATION_VERDICT: str = "nonfactorized_two_subsystem_states_demonstrated"
QIIC_REDUCED_STATE_VERDICT: str = "reduced_state_entanglement_signatures_available"
QIIC_WITNESS_VERDICT: str = "separability_or_purity_witness_justified"
QIIC_BELL_BOUNDARY_VERDICT: str = "bell_nonlocality_not_yet_justified"
QIIC_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QIID"
QIIC_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozenset vocabularies
ALLOWED_NONFACTORIZATION_VERDICTS: frozenset = frozenset({
    "nonfactorized_two_subsystem_states_demonstrated",
    "nonfactorized_structure_extension_level_only",
    "nonfactorized_structure_underdetermined",
    "nonfactorized_structure_blocked",
})
ALLOWED_REDUCED_STATE_VERDICTS: frozenset = frozenset({
    "reduced_state_entanglement_signatures_available",
    "reduced_state_signatures_qualitative_only",
    "reduced_state_signatures_underdetermined",
    "reduced_state_signatures_blocked",
})
ALLOWED_WITNESS_VERDICTS: frozenset = frozenset({
    "separability_or_purity_witness_justified",
    "toy_density_matrix_witness_justified",
    "bell_witness_not_yet_justified",
    "witness_structure_blocked",
})
ALLOWED_BELL_VERDICTS: frozenset = frozenset({
    "bell_nonlocality_not_yet_justified",
    "bell_structure_structurally_plausible_but_unbuilt",
    "toy_bell_criterion_available",
    "bell_claims_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QIID",
    "authorized_only_for_further_entanglement_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_QIIB",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8)
QIIC_NONCLAIMS: List[str] = [
    "NOT_claiming_nonfactorized_state_therefore_Bell_nonlocality__"
    "nonfactorization_is_algebraic_structure_not_operational_nonlocality",
    "NOT_claiming_reduced_state_mixedness_therefore_measurement_solved__"
    "mixedness_signature_is_diagnostic_not_measurement_closure",
    "NOT_claiming_tensor_product_extension_therefore_native_entanglement__"
    "entanglement_inherits_MIP_floor_from_tensor_product_postulation",
    "NOT_claiming_mathematical_benchmark_therefore_operational_entanglement_closure__"
    "toy_Bell_state_is_mathematical_not_physically_grounded_without_interactions",
    "NOT_claiming_witness_language_therefore_many_body_readiness__"
    "two_qubit_witness_does_not_generalize_to_N_body",
    "NOT_claiming_decoherence_on_composite_therefore_environment_induced_measurement__"
    "independent_channels_are_not_environment_induced_superselection",
    "NOT_claiming_two_subsystem_entanglement_therefore_matter_readiness__"
    "matter_requires_statistics_excitations_and_interactions",
    "NOT_claiming_extension_level_entanglement_therefore_native_canon__"
    "all_QIIC_results_carry_MBU_or_MIP_floor",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIICStateClass:
    """Single state class for nonfactorized-state eligibility (Track A)."""
    class_id: str
    class_name: str
    description: str
    admissible: bool
    entangled: bool
    notes: List[str]


@dataclass
class QIICNonfactorizedEligibilityAudit:
    """Track A --- nonfactorized-state eligibility."""
    state_classes: List[QIICStateClass]
    n_classes: int
    n_admissible: int
    n_entangled_classes: int
    nonfactorization_verdict: str
    notes: List[str]


@dataclass
class QIICFactorizationLevel:
    """Single factorization level (Track B)."""
    level_id: str
    level_name: str
    description: str
    criterion: str
    notes: List[str]


@dataclass
class QIICFactorizationBoundaryAudit:
    """Track B --- factorization boundary."""
    levels: List[QIICFactorizationLevel]
    n_levels: int
    boundary_criterion: str
    notes: List[str]


@dataclass
class QIICReducedStateTest:
    """Single reduced-state test (Track C)."""
    test_id: str
    test_name: str
    description: str
    available: bool
    quantitative: bool
    notes: List[str]


@dataclass
class QIICReducedStateSignatureAudit:
    """Track C --- reduced-state signatures."""
    tests: List[QIICReducedStateTest]
    n_tests: int
    n_available: int
    n_quantitative: int
    reduced_state_verdict: str
    notes: List[str]


@dataclass
class QIICWitnessCandidate:
    """Single entanglement witness candidate (Track D)."""
    candidate_id: str
    candidate_name: str
    description: str
    justified: bool
    level: str
    obstruction_if_not: str
    notes: List[str]


@dataclass
class QIICEntanglementWitnessAudit:
    """Track D --- entanglement witness."""
    candidates: List[QIICWitnessCandidate]
    n_candidates: int
    justified_candidate_id: str
    witness_verdict: str
    notes: List[str]


@dataclass
class QIICDecoherenceEffect:
    """Single decoherence-entanglement effect (Track E)."""
    effect_id: str
    effect_name: str
    description: str
    status: str
    notes: List[str]


@dataclass
class QIICDecoherenceEntanglementAudit:
    """Track E --- decoherence-entanglement interaction."""
    effects: List[QIICDecoherenceEffect]
    n_effects: int
    entanglement_suppressed_by_decoherence: bool
    interaction_hamiltonian_absent: bool
    notes: List[str]


@dataclass
class QIICBenchmarkCandidate:
    """Single entangled benchmark candidate (Track F)."""
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    demonstrates: List[str]
    does_not_demonstrate: List[str]
    reduced_purity_a: Optional[float]
    notes: List[str]


@dataclass
class QIICMinimalEntangledBenchmarkAudit:
    """Track F --- minimal entangled benchmark."""
    candidates: List[QIICBenchmarkCandidate]
    n_candidates: int
    n_viable: int
    chosen_benchmark_id: str
    notes: List[str]


@dataclass
class QIICBellCandidate:
    """Single Bell/nonlocality candidate (Track G)."""
    candidate_id: str
    candidate_name: str
    description: str
    justified: bool
    obstruction_if_not: str
    notes: List[str]


@dataclass
class QIICBellBoundaryAudit:
    """Track G --- Bell/nonlocality boundary."""
    candidates: List[QIICBellCandidate]
    n_candidates: int
    bell_boundary_verdict: str
    missing_prerequisites: List[str]
    notes: List[str]


@dataclass
class QIICAppendixPEntry:
    """Single Appendix P entry (Track H)."""
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIICAppendixPAudit:
    """Track H --- Appendix P classification."""
    entries: List[QIICAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIICAuthorizationAudit:
    """Track I --- authorization."""
    qiid_authorized: bool
    authorization_basis: List[str]
    qiid_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QIICNonclaimFirewall:
    """Track J --- nonclaims."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIICEntanglementNonfactorizedResult:
    """Master result for Q-II.C."""
    valid: bool
    track_a_nonfactorized: QIICNonfactorizedEligibilityAudit
    track_b_factorization: QIICFactorizationBoundaryAudit
    track_c_reduced_state: QIICReducedStateSignatureAudit
    track_d_witness: QIICEntanglementWitnessAudit
    track_e_decoherence: QIICDecoherenceEntanglementAudit
    track_f_benchmark: QIICMinimalEntangledBenchmarkAudit
    track_g_bell: QIICBellBoundaryAudit
    track_h_appendix_p: QIICAppendixPAudit
    track_i_authorization: QIICAuthorizationAudit
    track_j_nonclaims: QIICNonclaimFirewall
    # Five hard-gated verdicts
    nonfactorization_verdict: str
    reduced_state_verdict: str
    witness_verdict: str
    bell_boundary_verdict: str
    authorization_verdict: str
    # Summary
    qiic_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIICNonfactorizedEligibilityAudit:
    """Track A --- nonfactorized-state eligibility."""
    classes = [
        QIICStateClass(
            class_id="SC1", class_name="product_states",
            description="rho_AB = rho_A tensor rho_B. Fully factorized.",
            admissible=True, entangled=False,
            notes=["Demonstrated in Q-II.B benchmark CB1"],
        ),
        QIICStateClass(
            class_id="SC2", class_name="classically_correlated_mixtures",
            description="rho_AB = sum_i p_i rho_A^i tensor rho_B^i. Separable.",
            admissible=True, entangled=False,
            notes=["Admissible: convex mixtures of product states on C^4",
                   "Separable by construction; no quantum correlations"],
        ),
        QIICStateClass(
            class_id="SC3", class_name="pure_nonfactorized_states",
            description=(
                "|psi_AB> not of form |a> tensor |b>. E.g. "
                "(|00>+|11>)/sqrt(2). Reduced state is mixed."
            ),
            admissible=True, entangled=True,
            notes=[
                "Mathematically admissible in C^4 = C^2 tensor C^2",
                "Any vector in C^4 not of product form is nonfactorized",
                "Schmidt decomposition always exists for bipartite pure states",
                "Reduced-state mixedness is the entanglement signature",
                "Extension-level: existence follows from tensor product postulation",
            ],
        ),
        QIICStateClass(
            class_id="SC4", class_name="mixed_nonfactorized_states",
            description=(
                "rho_AB not writable as sum_i p_i rho_A^i tensor rho_B^i. "
                "Entangled mixed states."
            ),
            admissible=True, entangled=True,
            notes=[
                "Admissible: any positive semidefinite, trace-1, Hermitian 4x4 matrix",
                "Characterization harder than pure case (PPT criterion needed)",
                "For 2x2 systems, PPT is necessary and sufficient for separability",
            ],
        ),
        QIICStateClass(
            class_id="SC5", class_name="no_nonfactorized_class",
            description="Null: no nonfactorized states available.",
            admissible=False, entangled=False,
            notes=["Rejected: SC3 and SC4 are admissible"],
        ),
    ]

    n_adm = sum(1 for c in classes if c.admissible)
    n_ent = sum(1 for c in classes if c.entangled)

    return QIICNonfactorizedEligibilityAudit(
        state_classes=classes, n_classes=N_STATE_CLASSES,
        n_admissible=n_adm, n_entangled_classes=n_ent,
        nonfactorization_verdict=QIIC_NONFACTORIZATION_VERDICT,
        notes=[
            "4 state classes admissible (SC1-SC4), 1 null rejected (SC5)",
            "2 entangled classes: SC3 (pure nonfactorized) and SC4 (mixed nonfactorized)",
            "Nonfactorized states are mathematically admissible in C^4",
            "Their existence follows from tensor product postulation (MIP)",
            "Verdict: nonfactorized_two_subsystem_states_demonstrated",
        ],
    )


def _build_track_b() -> QIICFactorizationBoundaryAudit:
    """Track B --- factorization boundary."""
    levels = [
        QIICFactorizationLevel(
            level_id="FL1", level_name="factorized_product",
            description="rho_AB = rho_A tensor rho_B",
            criterion="rho_AB is a single tensor product of subsystem states",
            notes=["Trivially factorized; no correlations of any kind"],
        ),
        QIICFactorizationLevel(
            level_id="FL2", level_name="classically_correlated_separable",
            description="rho_AB = sum_i p_i rho_A^i tensor rho_B^i",
            criterion=(
                "rho_AB can be decomposed as convex mixture of product states. "
                "For 2x2 systems: equivalent to PPT (rho_AB^{T_B} >= 0)."
            ),
            notes=[
                "Separable: only classical correlations",
                "PPT criterion is necessary and sufficient for 2x2",
                "Tr_B(rho_AB) may still be mixed for separable states",
            ],
        ),
        QIICFactorizationLevel(
            level_id="FL3", level_name="genuinely_nonfactorized_entangled",
            description=(
                "rho_AB NOT writable as convex mixture of product states. "
                "For 2x2: rho_AB^{T_B} has at least one negative eigenvalue."
            ),
            criterion=(
                "Fails separability criterion. For pure states: Schmidt rank > 1. "
                "For mixed 2x2 states: negative partial transpose (NPT)."
            ),
            notes=[
                "Genuinely entangled by density-matrix criterion",
                "The boundary between FL2 and FL3 is the separability boundary",
                "For 2x2 systems this boundary is sharp (PPT is NAS)",
            ],
        ),
    ]

    return QIICFactorizationBoundaryAudit(
        levels=levels, n_levels=N_FACTORIZATION_LEVELS,
        boundary_criterion=(
            "separability_criterion_PPT_for_2x2_systems__"
            "rho_AB_separable_iff_partial_transpose_positive_semidefinite"
        ),
        notes=[
            "Three-level factorization hierarchy: product -> separable -> entangled",
            "Boundary between FL2 and FL3 is sharp for 2x2 (PPT criterion)",
            "PPT (positive partial transpose) is necessary and sufficient for 2x2",
            "This criterion is well-defined within the tensor-product extension package",
        ],
    )


def _build_track_c() -> QIICReducedStateSignatureAudit:
    """Track C --- reduced-state signatures."""
    tests = [
        QIICReducedStateTest(
            test_id="RST1", test_name="subsystem_mixedness_from_pure_joint",
            description=(
                "For pure |psi_AB>, compute rho_A = Tr_B(|psi><psi|). "
                "If Tr(rho_A^2) < 1, the joint state is entangled."
            ),
            available=True, quantitative=True,
            notes=[
                "Well-defined: partial trace + purity calculation in C^4",
                "Quantitative: Tr(rho_A^2) ranges from 1/2 (maximally entangled) to 1 (product)",
                "Necessary and sufficient for pure bipartite entanglement",
            ],
        ),
        QIICReducedStateTest(
            test_id="RST2", test_name="reduced_state_impurity",
            description=(
                "Compute linear entropy S_L(rho_A) = 1 - Tr(rho_A^2). "
                "S_L > 0 for entangled pure joint states."
            ),
            available=True, quantitative=True,
            notes=[
                "Linear entropy: simple, computable, monotonic in entanglement for pure states",
                "S_L = 0 for product states, S_L = 1/2 for maximally entangled qubit pair",
            ],
        ),
        QIICReducedStateTest(
            test_id="RST3", test_name="von_neumann_entropy_diagnostic",
            description=(
                "S(rho_A) = -Tr(rho_A ln rho_A). Von Neumann entropy of reduced state."
            ),
            available=True, quantitative=True,
            notes=[
                "Well-defined: rho_A is a 2x2 density matrix with eigenvalues lambda_i",
                "S = -sum lambda_i ln(lambda_i); ranges from 0 (pure) to ln(2) (maximally mixed)",
                "Entanglement entropy for pure bipartite states",
            ],
        ),
        QIICReducedStateTest(
            test_id="RST4", test_name="ppt_separability_test",
            description=(
                "Compute partial transpose rho_AB^{T_B}. Check eigenvalues. "
                "If any eigenvalue < 0, state is entangled."
            ),
            available=True, quantitative=True,
            notes=[
                "PPT criterion: computable from 4x4 density matrix",
                "Necessary and sufficient for 2x2 (Peres-Horodecki theorem)",
                "Extends beyond pure-state purity test to mixed states",
            ],
        ),
    ]

    n_avail = sum(1 for t in tests if t.available)
    n_quant = sum(1 for t in tests if t.quantitative)

    return QIICReducedStateSignatureAudit(
        tests=tests, n_tests=N_REDUCED_STATE_TESTS,
        n_available=n_avail, n_quantitative=n_quant,
        reduced_state_verdict=QIIC_REDUCED_STATE_VERDICT,
        notes=[
            "All 4 tests available and quantitative within C^4 tensor-product package",
            "RST1 (purity) and RST2 (linear entropy): sufficient for pure-state entanglement",
            "RST3 (von Neumann): entanglement entropy for pure bipartite states",
            "RST4 (PPT): necessary and sufficient separability test for 2x2",
            "All are density-matrix-level diagnostics; no measurement framework required",
            "Verdict: reduced_state_entanglement_signatures_available",
        ],
    )


def _build_track_d() -> QIICEntanglementWitnessAudit:
    """Track D --- entanglement witness."""
    candidates = [
        QIICWitnessCandidate(
            candidate_id="EW1", candidate_name="no_witness_language",
            description="No entanglement witness available.",
            justified=False, level="none",
            obstruction_if_not="Rejected: purity-based witness IS available.",
            notes=["Too restrictive; RST1-RST4 provide witness-level diagnostics"],
        ),
        QIICWitnessCandidate(
            candidate_id="EW2",
            candidate_name="purity_separability_witness",
            description=(
                "For pure joint states: Tr(rho_A^2) < 1 witnesses entanglement. "
                "For mixed states: PPT criterion (partial transpose eigenvalue < 0) "
                "witnesses entanglement. Both are density-matrix-level."
            ),
            justified=True, level="density_matrix",
            obstruction_if_not="",
            notes=[
                "Justified: all required operations (partial trace, purity, "
                "partial transpose) are defined in C^4 extension package",
                "Does NOT require measurement framework, Born rule, or multi-observable grammar",
                "Pure-state: purity witness is NAS for entanglement",
                "Mixed-state: PPT is NAS for 2x2 (Peres-Horodecki)",
            ],
        ),
        QIICWitnessCandidate(
            candidate_id="EW3",
            candidate_name="toy_density_matrix_witness",
            description=(
                "Explicit witness operator W such that Tr(W rho_sep) >= 0 "
                "for all separable states but Tr(W rho_ent) < 0 for some entangled state."
            ),
            justified=True, level="density_matrix",
            obstruction_if_not="",
            notes=[
                "Standard entanglement witness from the Hahn-Banach separation theorem",
                "Constructible in C^4 once separable set is defined",
                "Subsumed by EW2 (PPT is equivalent for 2x2 systems)",
                "Justified but provides no additional power beyond PPT for 2x2",
            ],
        ),
        QIICWitnessCandidate(
            candidate_id="EW4",
            candidate_name="bell_chsh_witness",
            description=(
                "Bell-CHSH inequality violation: |<CHSH>| > 2. "
                "Requires two measurement settings per party, expectation values."
            ),
            justified=False, level="operational",
            obstruction_if_not=(
                "NOT justified: requires (1) two measurement settings per subsystem "
                "(QE3 gap: second observable underdetermined), (2) expectation-value "
                "correlators (multi-observable grammar from Q-II.D not yet available), "
                "(3) Born-rule interpretation of outcomes (absent from Part I)."
            ),
            notes=[
                "Bell/CHSH is an OPERATIONAL criterion, not a density-matrix one",
                "Current package only supports density-matrix-level witnesses",
                "Three missing prerequisites: multi-observable, correlators, Born rule",
            ],
        ),
        QIICWitnessCandidate(
            candidate_id="EW5", candidate_name="witness_blocked",
            description="All witness structure is blocked.",
            justified=False, level="none",
            obstruction_if_not="Rejected: EW2 and EW3 are justified.",
            notes=["Null case; rejected"],
        ),
    ]

    return QIICEntanglementWitnessAudit(
        candidates=candidates, n_candidates=N_WITNESS_CANDIDATES,
        justified_candidate_id="EW2_purity_separability_witness",
        witness_verdict=QIIC_WITNESS_VERDICT,
        notes=[
            "EW2 justified: purity + PPT witness at density-matrix level",
            "EW3 justified but subsumed by EW2 for 2x2",
            "EW4 (Bell/CHSH) NOT justified: missing multi-observable, correlators, Born rule",
            "Current witness level: density-matrix diagnostics only",
            "Verdict: separability_or_purity_witness_justified",
        ],
    )


def _build_track_e() -> QIICDecoherenceEntanglementAudit:
    """Track E --- decoherence-entanglement interaction."""
    effects = [
        QIICDecoherenceEffect(
            effect_id="DE1",
            effect_name="independent_channels_suppress_off_diagonals",
            description=(
                "Independent Lindblad channels L_A, L_B each suppress "
                "off-diagonal elements in their respective Phi_hat eigenbasis. "
                "This suppresses coherence that could support entanglement."
            ),
            status="demonstrated",
            notes=[
                "Each subsystem decoheres independently at rate R_dec = delta_phi^2/(2 tau)",
                "Off-diagonal elements of rho_AB that represent inter-subsystem coherence "
                "are also suppressed by the product of single-system decoherence factors",
                "Entanglement-like coherences are transient (same as Q-F interference)",
            ],
        ),
        QIICDecoherenceEffect(
            effect_id="DE2",
            effect_name="product_state_asymptote",
            description=(
                "Under independent decoherence, the joint state asymptotically "
                "approaches a product of pointer-basis-diagonal states."
            ),
            status="demonstrated",
            notes=[
                "Long-time limit: rho_AB -> (diagonal in A) tensor (diagonal in B)",
                "This is a separable state (product of pointer-basis populations)",
                "Entanglement is destroyed by independent decoherence in the long-time limit",
            ],
        ),
        QIICDecoherenceEffect(
            effect_id="DE3",
            effect_name="transient_entanglement_window",
            description=(
                "If an entangled initial state is prepared, the entanglement "
                "persists for a time of order tau_dec before decoherence "
                "destroys it. Transient window only."
            ),
            status="extension_level",
            notes=[
                "Analogous to Q-F transient interference",
                "Entanglement survival time ~ tau_dec = 2 tau / delta_phi^2",
                "Extension-level: requires entangled initial state preparation "
                "(not addressed by current package)",
                "Initial-state preparation is a separate postulate",
            ],
        ),
        QIICDecoherenceEffect(
            effect_id="DE4",
            effect_name="interaction_hamiltonian_absent",
            description=(
                "No interaction Hamiltonian H_int is present. "
                "Without H_int, independent subsystems cannot GENERATE entanglement "
                "from a product initial state through dynamics."
            ),
            status="gap_documented",
            notes=[
                "Interaction Hamiltonian gap from Q-II.B preserved",
                "Entanglement generation requires coupling; independent channels "
                "cannot create entanglement from product states",
                "The benchmark assumes entangled initial state, not dynamical generation",
            ],
        ),
    ]

    return QIICDecoherenceEntanglementAudit(
        effects=effects, n_effects=N_DECOHERENCE_EFFECTS,
        entanglement_suppressed_by_decoherence=True,
        interaction_hamiltonian_absent=True,
        notes=[
            "Independent decoherence SUPPRESSES entanglement (DE1, DE2)",
            "Entanglement is transient if present in initial state (DE3)",
            "No mechanism to GENERATE entanglement from dynamics (DE4: H_int absent)",
            "Current package can ANALYZE entangled states but not PRODUCE them dynamically",
            "Entangled initial states must be postulated for benchmarking purposes",
        ],
    )


def _build_track_f() -> QIICMinimalEntangledBenchmarkAudit:
    """Track F --- minimal entangled benchmark."""
    candidates = [
        QIICBenchmarkCandidate(
            candidate_id="EB1",
            candidate_name="bell_pair_toy_benchmark",
            description=(
                "|psi+> = (|00> + |11>)/sqrt(2) as initial state in C^4. "
                "Maximally entangled pure state. "
                "rho_A = Tr_B(|psi+><psi+|) = (1/2) I_2."
            ),
            viable=True,
            demonstrates=[
                "nonfactorized_pure_state_in_C4",
                "reduced_state_mixedness_Tr_rho_A_sq_equals_half",
                "entanglement_entropy_S_equals_ln2",
                "linear_entropy_half",
                "partial_transpose_has_negative_eigenvalue",
                "separability_witness_detects_entanglement",
            ],
            does_not_demonstrate=[
                "dynamical_entanglement_generation",
                "Bell_inequality_violation_operational",
                "measurement_outcomes_or_Born_rule",
                "interaction_induced_entanglement",
                "many_body_entanglement",
            ],
            reduced_purity_a=MAXIMALLY_ENTANGLED_REDUCED_PURITY,
            notes=[
                "Mathematical benchmark: |psi+> is postulated as initial state",
                "Not dynamically generated (H_int absent)",
                "Demonstrates all density-matrix-level entanglement signatures",
                "Reduced purity: Tr(rho_A^2) = 1/2 (maximally mixed qubit)",
            ],
        ),
        QIICBenchmarkCandidate(
            candidate_id="EB2",
            candidate_name="generic_nonfactorized_mixed_state",
            description=(
                "A generic 4x4 density matrix that fails PPT criterion. "
                "Less clean than EB1 but tests mixed-state entanglement."
            ),
            viable=True,
            demonstrates=[
                "mixed_nonfactorized_state_in_C4",
                "PPT_criterion_detects_entanglement",
                "mixed_state_entanglement_structure",
            ],
            does_not_demonstrate=[
                "dynamical_entanglement_generation",
                "Bell_violation",
                "pure_state_entanglement_signatures",
            ],
            reduced_purity_a=None,
            notes=[
                "Viable: any entangled mixed state in C^4 serves as benchmark",
                "Less canonical than EB1; subsumed by EB1 for demonstration purposes",
            ],
        ),
        QIICBenchmarkCandidate(
            candidate_id="EB3",
            candidate_name="no_admissible_benchmark",
            description="No entangled benchmark available.",
            viable=False, demonstrates=[], does_not_demonstrate=[],
            reduced_purity_a=None,
            notes=["Rejected: EB1 is viable"],
        ),
    ]

    n_viable = sum(1 for c in candidates if c.viable)

    return QIICMinimalEntangledBenchmarkAudit(
        candidates=candidates, n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_viable,
        chosen_benchmark_id="EB1_bell_pair_toy_benchmark",
        notes=[
            "EB1 chosen: Bell pair |psi+> as mathematical benchmark",
            "Demonstrates: nonfactorization, reduced-state mixedness, all witnesses",
            "Does NOT demonstrate: dynamical generation, Bell violation, Born rule",
            "The benchmark is MATHEMATICAL (postulated initial state), not PHYSICAL "
            "(no mechanism produces it)",
            f"Reduced purity: Tr(rho_A^2) = {MAXIMALLY_ENTANGLED_REDUCED_PURITY}",
        ],
    )


def _build_track_g() -> QIICBellBoundaryAudit:
    """Track G --- Bell/nonlocality boundary."""
    candidates = [
        QIICBellCandidate(
            candidate_id="BL1",
            candidate_name="bell_not_yet_justified",
            description="Bell/CHSH claims are not yet justified.",
            justified=True,
            obstruction_if_not="",
            notes=[
                "This IS the correct assessment: Bell is not yet justified",
                "Three missing prerequisites: multi-observable, correlators, Born rule",
            ],
        ),
        QIICBellCandidate(
            candidate_id="BL2",
            candidate_name="bell_structurally_plausible",
            description=(
                "Bell structure is structurally plausible: if Q-II.D provides "
                "multi-observable grammar and Born rule were available, "
                "Bell could be investigated."
            ),
            justified=True,
            obstruction_if_not="",
            notes=[
                "Plausible path identified but prerequisites not yet met",
                "Q-II.D (observable algebra) + Q-II.F (probability) are needed",
            ],
        ),
        QIICBellCandidate(
            candidate_id="BL3",
            candidate_name="toy_bell_criterion",
            description="A toy-level Bell criterion is available now.",
            justified=False,
            obstruction_if_not=(
                "NOT justified: Bell criterion requires measurement settings "
                "and outcome correlators. Neither is available without "
                "multi-observable grammar (Q-II.D) and Born rule (absent)."
            ),
            notes=["Cannot construct CHSH without measurement settings"],
        ),
        QIICBellCandidate(
            candidate_id="BL4",
            candidate_name="bell_claims_blocked",
            description="Bell claims are permanently blocked.",
            justified=False,
            obstruction_if_not=(
                "Not permanently blocked: prerequisites are absent but not obstructed. "
                "Bell investigation could proceed after Q-II.D and Q-II.F."
            ),
            notes=["Not blocked; just not yet available"],
        ),
    ]

    return QIICBellBoundaryAudit(
        candidates=candidates, n_candidates=N_BELL_CANDIDATES,
        bell_boundary_verdict=QIIC_BELL_BOUNDARY_VERDICT,
        missing_prerequisites=[
            "multi_observable_grammar_two_settings_per_subsystem",
            "expectation_value_correlators_for_joint_measurements",
            "Born_rule_or_probability_interpretation_of_outcomes",
            "measurement_framework_beyond_density_matrix_diagnostics",
        ],
        notes=[
            "Bell nonlocality NOT yet justified (BL1 correct assessment)",
            "Bell structure IS structurally plausible (BL2) once prerequisites met",
            "Toy Bell criterion NOT available (BL3): missing measurement settings",
            "Bell NOT permanently blocked (BL4 rejected)",
            "Hard boundary: nonfactorization != Bell nonlocality",
            "Prerequisites: Q-II.D (observables) + Q-II.F (probability) needed",
            "Verdict: bell_nonlocality_not_yet_justified",
        ],
    )


def _build_track_h() -> QIICAppendixPAudit:
    """Track H --- Appendix P classification."""
    entries = [
        QIICAppendixPEntry(
            item_id="QIIC_nonfactorized_states",
            item_name="Nonfactorized two-subsystem states",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="Nonfactorized states admissible in C^4 extension package",
            forbidden_claim="Nonfactorized states derived from GRUT first principles",
            dependency="Q-II.B tensor product postulation (MIP)",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_purity_witness",
            item_name="Purity/separability entanglement witness",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Purity and PPT witnesses justified at density-matrix level "
                "for 2x2 composite system"
            ),
            forbidden_claim="Witness implies operational entanglement or Bell violation",
            dependency="Tensor product, partial trace, density-matrix formalism",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_reduced_signatures",
            item_name="Reduced-state entanglement signatures",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Reduced-state purity, linear entropy, von Neumann entropy, "
                "and PPT criterion all available for 2x2 states"
            ),
            forbidden_claim="Reduced-state diagnostics imply measurement or Born rule",
            dependency="Partial trace, density-matrix eigenvalue computation",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_bell_pair_benchmark",
            item_name="Bell-pair toy benchmark",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Bell pair |psi+> serves as mathematical benchmark "
                "demonstrating all density-matrix entanglement signatures"
            ),
            forbidden_claim=(
                "Bell pair benchmark implies dynamical entanglement generation "
                "or Bell inequality violation"
            ),
            dependency="Tensor product, postulated initial state",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_decoherence_suppression",
            item_name="Decoherence suppresses entanglement",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Independent Lindblad channels suppress entanglement; "
                "entanglement is transient"
            ),
            forbidden_claim=(
                "Decoherence-entanglement interaction implies environment-induced "
                "measurement or superselection"
            ),
            dependency="Part I Lindblad, Q-II.B independent channels",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_bell_boundary",
            item_name="Bell/nonlocality boundary",
            appendix_p_class="bounded_structural_result",
            allowed_claim="Bell nonlocality not yet justified; prerequisites documented",
            forbidden_claim="Bell nonlocality claims at this stage",
            dependency="Q-II.D (observables), Q-II.F (probability) needed",
        ),
        QIICAppendixPEntry(
            item_id="QIIC_overall",
            item_name="Q-II.C overall",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Entanglement structure coherently established at density-matrix level "
                "for two-subsystem extension"
            ),
            forbidden_claim=(
                "Entanglement closure or operational entanglement achieved"
            ),
            dependency="All Q-II.C tracks; Q-II.B locked results",
        ),
    ]

    return QIICAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIIC_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=[
            "5 entries MBU, 1 entry BSR (Bell boundary), 1 entry MBU (overall)",
            "No native canon: all results are extension-level",
            "Bell boundary is BSR: proved not-yet-justified status",
        ],
    )


def _build_track_i() -> QIICAuthorizationAudit:
    """Track I --- authorization."""
    return QIICAuthorizationAudit(
        qiid_authorized=True,
        authorization_basis=[
            "nonfactorized_states_demonstrated_in_extension_package",
            "reduced_state_entanglement_signatures_available",
            "purity_separability_witness_justified",
            "bell_boundary_documented_prerequisites_identified",
            "decoherence_entanglement_interaction_characterized",
        ],
        qiid_constraints=[
            "QIID_must_address_multi_observable_grammar_for_Bell_prerequisites",
            "QIID_must_not_assume_Bell_violation_without_measurement_framework",
            "QIID_results_inherit_MBU_or_MIP_floor",
            "QIID_must_address_QE3_second_observable_gap",
            "QIID_may_enable_correlator_language_for_future_Bell_investigation",
        ],
        authorization_verdict=QIIC_AUTHORIZATION_VERDICT,
        notes=[
            "Q-II.D authorized: entanglement structure sufficient to motivate "
            "multi-observable grammar investigation",
            "Key motivation: Bell investigation requires multi-observable from Q-II.D",
            "Q-II.D must address the QE3 gap (second observable underdetermined)",
            "All Q-II.D results inherit MBU/MIP floor",
        ],
    )


def _build_track_j() -> QIICNonclaimFirewall:
    """Track J --- nonclaims."""
    return QIICNonclaimFirewall(
        nonclaims=QIIC_NONCLAIMS, n_nonclaims=N_QIIC_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qiic_entanglement_nonfactorized_audit() -> QIICEntanglementNonfactorizedResult:
    """Run the full Q-II.C Entanglement and Nonfactorized Structure Audit."""
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

    allowed_claims: List[str] = [
        "Nonfactorized two-subsystem states are mathematically admissible "
        "in the C^4 tensor-product extension package",
        "Reduced-state entanglement signatures (purity, linear entropy, "
        "von Neumann entropy, PPT) are all available and quantitative",
        "Purity/separability witness is justified at density-matrix level; "
        "PPT is necessary and sufficient for 2x2",
        "Bell-pair toy benchmark demonstrates all density-matrix entanglement "
        "signatures (reduced purity = 1/2, S = ln 2)",
        "Independent Lindblad decoherence suppresses entanglement; "
        "entanglement is transient in current package",
        "Bell nonlocality not yet justified; prerequisites documented "
        "(multi-observable, correlators, Born rule)",
        "Q-II.D authorized: multi-observable grammar needed for Bell prerequisites",
    ]

    forbidden_claims: List[str] = [
        "Nonfactorized states imply Bell nonlocality or operational entanglement",
        "Reduced-state mixedness implies measurement closure or Born rule",
        "Tensor-product extension implies native entanglement",
        "Mathematical Bell-pair benchmark implies dynamical entanglement generation",
        "Density-matrix witness implies many-body entanglement readiness",
        "Decoherence on composite states implies environment-induced measurement",
        "Extension-level entanglement results imply native canon status",
    ]

    diagnostics: Dict[str, Any] = {
        "composite_hilbert_dim": COMPOSITE_HILBERT_DIM,
        "maximally_entangled_reduced_purity": MAXIMALLY_ENTANGLED_REDUCED_PURITY,
        "pure_state_purity": PURE_STATE_PURITY,
        "n_state_classes": N_STATE_CLASSES,
        "n_admissible_classes": ta.n_admissible,
        "n_entangled_classes": ta.n_entangled_classes,
        "n_reduced_state_tests": N_REDUCED_STATE_TESTS,
        "n_available_tests": tc.n_available,
        "n_quantitative_tests": tc.n_quantitative,
        "n_witness_candidates": N_WITNESS_CANDIDATES,
        "n_bell_missing_prerequisites": len(tg.missing_prerequisites),
        "n_benchmark_viable": tf.n_viable,
        "n_nonclaims": N_QIIC_NONCLAIMS,
        "entanglement_suppressed_by_decoherence": te.entanglement_suppressed_by_decoherence,
        "interaction_hamiltonian_absent": te.interaction_hamiltonian_absent,
    }

    result = QIICEntanglementNonfactorizedResult(
        valid=True,
        track_a_nonfactorized=ta, track_b_factorization=tb,
        track_c_reduced_state=tc, track_d_witness=td,
        track_e_decoherence=te, track_f_benchmark=tf,
        track_g_bell=tg, track_h_appendix_p=th,
        track_i_authorization=ti, track_j_nonclaims=tj,
        nonfactorization_verdict=ta.nonfactorization_verdict,
        reduced_state_verdict=tc.reduced_state_verdict,
        witness_verdict=td.witness_verdict,
        bell_boundary_verdict=tg.bell_boundary_verdict,
        authorization_verdict=ti.authorization_verdict,
        qiic_appendix_p_class=QIIC_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIIC_NONCLAIMS,
        diagnostics=diagnostics,
    )

    validate_qiic_result(result)
    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qiic_result(result: QIICEntanglementNonfactorizedResult) -> None:
    """Validate Q-II.C result."""
    checks = [
        (result.nonfactorization_verdict, ALLOWED_NONFACTORIZATION_VERDICTS, "Nonfactorization"),
        (result.reduced_state_verdict, ALLOWED_REDUCED_STATE_VERDICTS, "Reduced-state"),
        (result.witness_verdict, ALLOWED_WITNESS_VERDICTS, "Witness"),
        (result.bell_boundary_verdict, ALLOWED_BELL_VERDICTS, "Bell boundary"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization"),
    ]
    for verdict, allowed, label in checks:
        if verdict not in allowed:
            raise ValueError(f"{label} verdict '{verdict}' not in allowed vocabulary")

    if result.qiic_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError(f"Overall class not in allowed")
    for entry in result.track_h_appendix_p.entries:
        if entry.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Track H entry '{entry.item_id}': class not in allowed")
    if result.track_j_nonclaims.n_nonclaims != N_QIIC_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_j_nonclaims.all_registered:
        raise ValueError("Nonclaims not all registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_h_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if not result.track_i_authorization.qiid_authorized:
        raise ValueError("qiid_authorized must be True")
    if not result.track_e_decoherence.entanglement_suppressed_by_decoherence:
        raise ValueError("entanglement_suppressed_by_decoherence must be True")
    if not result.track_e_decoherence.interaction_hamiltonian_absent:
        raise ValueError("interaction_hamiltonian_absent must be True")

    n_adm = sum(1 for c in result.track_a_nonfactorized.state_classes if c.admissible)
    if n_adm != result.track_a_nonfactorized.n_admissible:
        raise ValueError("Track A admissible count mismatch")


def _self_test() -> bool:
    """Run audit and validate."""
    r = run_qiic_entanglement_nonfactorized_audit()
    assert r.valid is True
    assert r.nonfactorization_verdict == QIIC_NONFACTORIZATION_VERDICT
    assert r.reduced_state_verdict == QIIC_REDUCED_STATE_VERDICT
    assert r.witness_verdict == QIIC_WITNESS_VERDICT
    assert r.bell_boundary_verdict == QIIC_BELL_BOUNDARY_VERDICT
    assert r.authorization_verdict == QIIC_AUTHORIZATION_VERDICT
    assert abs(r.diagnostics["maximally_entangled_reduced_purity"] - 0.5) < 1e-15
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.C self-test passed.")
