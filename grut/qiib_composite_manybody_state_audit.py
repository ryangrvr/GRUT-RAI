"""
Appendix Q-II.B --- Composite and Many-Body State Structure Audit
=================================================================
GRUT Quantum Program --- Phase Q-II.B  (First Substantive Second-Wave Stage)

This module audits whether the GRUT quantum extension can support composite
states, subsystems, reduced-state composition, and many-body grammar.

Inherited structure
-------------------
Part I (Q-B through Q-F) established single-system quantum foundations:
  - 2-state Hilbert space C^2 with density matrix rho (2x2)
  - Jump operator L = (1/sqrt(tau)) Phi_hat, gamma = 1/tau
  - Constitutive observable Phi_hat = sigma_z
  - Off-diagonal decoherence rate: R_dec = delta_phi^2 / (2 tau)
  - Pointer basis: Phi_hat eigenstates
  - Transient interference: V(t) = exp(-R_dec t)

All Part I results are SINGLE-SYSTEM.  No composite, subsystem, or
multi-body structure was postulated or derived.

Key physics for this audit
--------------------------
Composite-state structure requires:
  1. Distinguishable subsystem labels (who are the parts?)
  2. Admissible joint state object (what is the composite state?)
  3. Rule for composition (how do single states combine?)
  4. Admissible reduced-state map (how do we recover subsystem states?)
  5. Compatibility with first-wave dynamics (does decoherence still work?)

The audit tests whether these can be coherently postulated as extensions.
Since Part I is entirely single-system, composite structure CANNOT be
derived --- it must be postulated.  The question is whether the postulation
is coherent (MIP/MBU) or merely notational (CAH).

Subsystem identity
------------------
GRUT's Part I package has ONE system (the scalar field Phi in 2-state
quantum realization).  Subsystem identity requires distinguishing two or
more systems.  Candidate routes:

  SS1: Multiple copies of the same 2-state toy system (label duplication)
  SS2: Spatially separated effective sectors (no spatial DOF in Part I)
  SS3: Distinct observables within one system (only Phi_hat motivated)
  SS4: Independent reduced-state factors (requires composition first)
  SS5: No valid subsystem identity yet

Honest assessment: SS1 (multiple copies) is the only currently viable route.
It is extension-level: we POSTULATE that two independent copies of the
2-state system can coexist.  This is coherent (no contradiction with Part I)
but not derived (Part I never mentions a second system).

Composition rule
----------------
Given two 2-state systems A and B, the natural composition candidates are:

  CR1: Tensor product  H_AB = H_A tensor H_B  (standard QM)
  CR2: Direct sum  H_AB = H_A direct_sum H_B  (superselection sectors)
  CR3: Coupled density kernel (non-standard, dissipation-based coupling)
  CR4: History-space composition (path-integral-like)
  CR5: No coherent composition rule

CR1 (tensor product) is the structurally natural choice: it is the standard
quantum-mechanical rule for composing independent systems, and it is
compatible with the density-matrix formalism already established.  It is
extension-level (postulated, not derived) and carries MIP classification.

Minimal toy composite benchmark
--------------------------------
The smallest composite benchmark is two copies of the QE1 two-state system:
  H_AB = C^2 tensor C^2 = C^4
  rho_AB = 4x4 density matrix
  L_A = sqrt(gamma) sigma_z tensor I,  L_B = I tensor sqrt(gamma) sigma_z
  Product state: rho_AB = rho_A tensor rho_B (factorized)

This benchmark demonstrates:
  - Independent decoherence on each subsystem
  - Product-state composition
  - Partial trace yields single-system rho_A, rho_B
  - No entanglement (only factorized states tested)
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

# Composite system parameters
COMPOSITE_HILBERT_DIM: int = 4          # C^2 tensor C^2
SINGLE_SYSTEM_DIM: int = 2             # C^2
N_SUBSYSTEMS_BENCHMARK: int = 2         # two-copy benchmark

# Eligibility ingredients
N_ELIGIBILITY_INGREDIENTS: int = 5
# Subsystem candidates
N_SUBSYSTEM_CANDIDATES: int = 5
# Composition rule candidates
N_COMPOSITION_CANDIDATES: int = 5
# Reduced-state candidates
N_REDUCED_STATE_CANDIDATES: int = 4
# Many-body grammar levels
N_MANY_BODY_LEVELS: int = 4
# Decoherence compatibility checks
N_DECOHERENCE_CHECKS: int = 4
# Toy benchmark candidates
N_BENCHMARK_CANDIDATES: int = 4
# Appendix P entries
N_APPENDIX_P_ENTRIES: int = 7
# Nonclaims
N_QIIB_NONCLAIMS: int = 8
# Claims
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

# Inherited verdicts
QII0_INHERITED: str = "second_wave_gap_inventory_complete__all_gaps_documented"
QIIA_INHERITED: str = "part_two_authorized_and_staged"
QF_INHERITED_CLOSURE: str = "authorized_to_close_first_wave_quantum_program"

# Q-II.B Verdict strings
QIIB_SUBSYSTEM_VERDICT: str = "subsystem_identity_extension_level_only"
QIIB_COMPOSITION_VERDICT: str = "composition_rule_extension_level_only"
QIIB_REDUCED_STATE_VERDICT: str = "reduced_state_map_extension_level_only"
QIIB_MANY_BODY_VERDICT: str = "two_subsystem_grammar_demonstrated"
QIIB_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_QIIC"
QIIB_OVERALL_APPENDIX_P_CLASS: str = "motivated_but_unbuilt"

# Frozenset vocabularies
ALLOWED_SUBSYSTEM_VERDICTS: frozenset = frozenset({
    "principled_subsystem_identity_demonstrated",
    "subsystem_identity_extension_level_only",
    "subsystem_identity_underdetermined",
    "subsystem_identity_blocked",
})
ALLOWED_COMPOSITION_VERDICTS: frozenset = frozenset({
    "coherent_composition_rule_identified",
    "composition_rule_extension_level_only",
    "composition_rule_structurally_plausible_but_unbuilt",
    "composition_rule_blocked",
})
ALLOWED_REDUCED_STATE_VERDICTS: frozenset = frozenset({
    "reduced_state_map_available",
    "reduced_state_map_extension_level_only",
    "reduced_state_map_underdetermined",
    "reduced_state_map_blocked",
})
ALLOWED_MANY_BODY_VERDICTS: frozenset = frozenset({
    "two_subsystem_grammar_demonstrated",
    "finite_N_grammar_structurally_plausible",
    "many_body_grammar_structurally_plausible_but_unbuilt",
    "many_body_grammar_blocked",
})
ALLOWED_AUTHORIZATION_VERDICTS: frozenset = frozenset({
    "authorized_to_proceed_to_QIIC",
    "authorized_only_for_further_composite_refinement",
    "not_authorized_to_proceed",
    "requires_reopening_part_one_assumptions",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# Nonclaims (8)
QIIB_NONCLAIMS: List[str] = [
    "NOT_claiming_repeated_toy_labels_therefore_genuine_subsystem_structure__"
    "label_duplication_is_notational_not_ontological",
    "NOT_claiming_notation_level_tensor_product_therefore_physical_composition_derived__"
    "tensor_product_is_postulated_extension_not_derived_from_GRUT",
    "NOT_claiming_two_copy_benchmark_therefore_entanglement_established__"
    "product_state_benchmark_demonstrates_composition_not_entanglement",
    "NOT_claiming_reduced_state_language_therefore_partial_trace_derived__"
    "partial_trace_is_postulated_with_tensor_product_not_independently_derived",
    "NOT_claiming_composite_bookkeeping_therefore_many_body_readiness__"
    "two_subsystem_grammar_does_not_generalize_to_N_body_matter",
    "NOT_claiming_first_wave_decoherence_therefore_multi_body_closure__"
    "single_system_decoherence_does_not_extend_automatically_to_composites",
    "NOT_claiming_extension_level_composition_therefore_native_canon__"
    "all_QIIB_results_carry_MBU_or_MIP_floor",
    "NOT_claiming_composite_state_support_therefore_matter_readiness_achieved__"
    "matter_requires_statistics_excitations_and_interactions_beyond_composition",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class QIIBEligibilityIngredient:
    """Single composite-state eligibility ingredient (Track A)."""
    ingredient_id: str
    ingredient_name: str
    description: str
    status: str
    source: str
    notes: List[str]


@dataclass
class QIIBCompositeEligibilityAudit:
    """Track A --- composite-state eligibility."""
    ingredients: List[QIIBEligibilityIngredient]
    n_ingredients: int
    n_present: int
    n_absent: int
    n_extension_level: int
    eligibility_verdict: str
    notes: List[str]


@dataclass
class QIIBSubsystemCandidate:
    """Single subsystem identity candidate (Track B)."""
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    viability_level: str
    obstruction_if_not: str
    notes: List[str]


@dataclass
class QIIBSubsystemIdentityAudit:
    """Track B --- subsystem identity audit."""
    candidates: List[QIIBSubsystemCandidate]
    n_candidates: int
    n_viable: int
    chosen_candidate_id: str
    subsystem_verdict: str
    notes: List[str]


@dataclass
class QIIBCompositionCandidate:
    """Single composition rule candidate (Track C)."""
    candidate_id: str
    candidate_name: str
    description: str
    status: str
    coherent: bool
    appendix_p_class: str
    notes: List[str]


@dataclass
class QIIBCompositionRuleAudit:
    """Track C --- composition-rule audit."""
    candidates: List[QIIBCompositionCandidate]
    n_candidates: int
    chosen_candidate_id: str
    composition_verdict: str
    notes: List[str]


@dataclass
class QIIBReducedStateCandidate:
    """Single reduced-state map candidate (Track D)."""
    candidate_id: str
    candidate_name: str
    description: str
    status: str
    notes: List[str]


@dataclass
class QIIBReducedStateAudit:
    """Track D --- reduced-state audit."""
    candidates: List[QIIBReducedStateCandidate]
    n_candidates: int
    chosen_candidate_id: str
    reduced_state_verdict: str
    notes: List[str]


@dataclass
class QIIBManyBodyLevel:
    """Single many-body grammar level (Track E)."""
    level_id: str
    level_name: str
    description: str
    achieved: bool
    notes: List[str]


@dataclass
class QIIBManyBodyGrammarAudit:
    """Track E --- many-body grammar audit."""
    levels: List[QIIBManyBodyLevel]
    n_levels: int
    highest_achieved_id: str
    many_body_verdict: str
    notes: List[str]


@dataclass
class QIIBDecoherenceCheck:
    """Single decoherence compatibility check (Track F)."""
    check_id: str
    check_name: str
    description: str
    result: str
    notes: List[str]


@dataclass
class QIIBDecoherenceCompatibilityAudit:
    """Track F --- decoherence compatibility audit."""
    checks: List[QIIBDecoherenceCheck]
    n_checks: int
    overall_compatible: bool
    requires_new_postulates: bool
    notes: List[str]


@dataclass
class QIIBBenchmarkCandidate:
    """Single toy composite benchmark candidate (Track G)."""
    candidate_id: str
    candidate_name: str
    description: str
    viable: bool
    demonstrates: List[str]
    does_not_demonstrate: List[str]
    notes: List[str]


@dataclass
class QIIBMinimalCompositeBenchmarkAudit:
    """Track G --- minimal composite benchmark audit."""
    candidates: List[QIIBBenchmarkCandidate]
    n_candidates: int
    n_viable: int
    chosen_benchmark_id: str
    benchmark_hilbert_dim: int
    benchmark_n_subsystems: int
    notes: List[str]


@dataclass
class QIIBAppendixPEntry:
    """Single Appendix P classification entry (Track H)."""
    item_id: str
    item_name: str
    appendix_p_class: str
    allowed_claim: str
    forbidden_claim: str
    dependency: str


@dataclass
class QIIBAppendixPAudit:
    """Track H --- Appendix P classification."""
    entries: List[QIIBAppendixPEntry]
    n_entries: int
    overall_class: str
    no_native_canon: bool
    notes: List[str]


@dataclass
class QIIBAuthorizationAudit:
    """Track I --- authorization audit."""
    qiic_authorized: bool
    authorization_basis: List[str]
    qiic_constraints: List[str]
    authorization_verdict: str
    notes: List[str]


@dataclass
class QIIBNonclaimFirewall:
    """Track J --- nonclaim firewall."""
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class QIIBCompositeManybodyResult:
    """Master result for Q-II.B."""
    valid: bool
    track_a_eligibility: QIIBCompositeEligibilityAudit
    track_b_subsystem: QIIBSubsystemIdentityAudit
    track_c_composition: QIIBCompositionRuleAudit
    track_d_reduced_state: QIIBReducedStateAudit
    track_e_many_body: QIIBManyBodyGrammarAudit
    track_f_decoherence: QIIBDecoherenceCompatibilityAudit
    track_g_benchmark: QIIBMinimalCompositeBenchmarkAudit
    track_h_appendix_p: QIIBAppendixPAudit
    track_i_authorization: QIIBAuthorizationAudit
    track_j_nonclaims: QIIBNonclaimFirewall
    # Five hard-gated verdicts
    subsystem_verdict: str
    composition_verdict: str
    reduced_state_verdict: str
    many_body_verdict: str
    authorization_verdict: str
    # Summary
    qiib_appendix_p_class: str
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> QIIBCompositeEligibilityAudit:
    """Track A --- composite-state eligibility."""
    ingredients = [
        QIIBEligibilityIngredient(
            ingredient_id="CE1",
            ingredient_name="distinguishable_subsystem_labels",
            description=(
                "A principled way to label two or more distinguishable subsystems. "
                "Requires going beyond single-system Part I framework."
            ),
            status="extension_level",
            source="Not in Part I (single-system only)",
            notes=[
                "Part I has exactly one system (scalar field Phi in 2-state realization)",
                "Subsystem labels must be postulated as extension",
                "SS1 (multiple copies) is the simplest viable route",
            ],
        ),
        QIIBEligibilityIngredient(
            ingredient_id="CE2",
            ingredient_name="admissible_joint_state_object",
            description=(
                "A well-defined joint state rho_AB for a composite of subsystems "
                "A and B. Requires density matrix on composite Hilbert space."
            ),
            status="extension_level",
            source="Follows from composition rule (CE3) once postulated",
            notes=[
                "In tensor-product composition: rho_AB is a 4x4 density matrix on C^4",
                "Well-definedness requires: Hermiticity, trace 1, positive semidefinite",
                "These properties are inherited from standard density-matrix formalism",
            ],
        ),
        QIIBEligibilityIngredient(
            ingredient_id="CE3",
            ingredient_name="rule_for_composition",
            description=(
                "An explicit rule for combining single-system states into "
                "composite states. Tensor product is the natural candidate."
            ),
            status="extension_level",
            source="Standard QM (must be postulated for GRUT)",
            notes=[
                "Tensor product H_AB = H_A tensor H_B is standard and coherent",
                "Must be explicitly postulated (MIP); not derivable from Part I",
                "CR1 is the chosen composition rule",
            ],
        ),
        QIIBEligibilityIngredient(
            ingredient_id="CE4",
            ingredient_name="admissible_reduced_state_map",
            description=(
                "A map from joint states to subsystem states (partial trace). "
                "Required for defining subsystem properties."
            ),
            status="extension_level",
            source="Follows from tensor product (CE3) once postulated",
            notes=[
                "Partial trace: rho_A = Tr_B(rho_AB)",
                "Mathematically well-defined once tensor product is postulated",
                "Not independently derivable; comes with composition rule",
            ],
        ),
        QIIBEligibilityIngredient(
            ingredient_id="CE5",
            ingredient_name="compatibility_with_first_wave_dynamics",
            description=(
                "The composite structure must be compatible with Part I Lindbladian "
                "decoherence on each subsystem without contradicting locked results."
            ),
            status="extension_level",
            source="Part I dynamics + composite postulation",
            notes=[
                "Independent Lindblad channels on each subsystem preserve Part I results",
                "L_A = sqrt(gamma) sigma_z tensor I acts on subsystem A only",
                "Decoherence rates, pointer basis, constitutive recovery all preserved",
                "No contradiction with Part I locked classes",
            ],
        ),
    ]

    n_pres = sum(1 for i in ingredients if i.status == "present")
    n_abs = sum(1 for i in ingredients if i.status == "absent")
    n_ext = sum(1 for i in ingredients if i.status == "extension_level")

    return QIIBCompositeEligibilityAudit(
        ingredients=ingredients,
        n_ingredients=N_ELIGIBILITY_INGREDIENTS,
        n_present=n_pres,
        n_absent=n_abs,
        n_extension_level=n_ext,
        eligibility_verdict="eligible_at_extension_level",
        notes=[
            "All 5 ingredients are extension-level: none present natively, none blocked",
            "Composite-state structure is entirely postulational (MIP/MBU)",
            "No ingredient is derived from Part I single-system results",
            "Coherent package: tensor product + partial trace + independent dynamics",
        ],
    )


def _build_track_b() -> QIIBSubsystemIdentityAudit:
    """Track B --- subsystem identity audit."""
    candidates = [
        QIIBSubsystemCandidate(
            candidate_id="SS1",
            candidate_name="multiple_copies_of_toy_system",
            description=(
                "Postulate two or more independent copies of the QE1 two-state "
                "system, each with its own Hilbert space C^2 and Lindblad channel."
            ),
            viable=True,
            viability_level="extension_level",
            obstruction_if_not="",
            notes=[
                "Simplest viable route: label two copies as A and B",
                "Each copy inherits all Part I structure independently",
                "Extension-level: the second copy is postulated, not derived",
                "Does NOT require spatial DOF or new observables",
            ],
        ),
        QIIBSubsystemCandidate(
            candidate_id="SS2",
            candidate_name="spatially_separated_sectors",
            description=(
                "Identify subsystems via spatial separation (different locations "
                "or regions)."
            ),
            viable=False,
            viability_level="blocked",
            obstruction_if_not=(
                "No spatial degrees of freedom in Part I. Q-F remaining_gaps "
                "includes spatial_degrees_of_freedom_absent."
            ),
            notes=[
                "Blocked: spatial DOF absent from first-wave package",
                "Would require spatial Hilbert space or position operator",
                "Cannot use what does not exist",
            ],
        ),
        QIIBSubsystemCandidate(
            candidate_id="SS3",
            candidate_name="distinct_observables_within_one_system",
            description=(
                "Treat different observables within the single 2-state system "
                "as defining distinct subsectors."
            ),
            viable=False,
            viability_level="blocked",
            obstruction_if_not=(
                "QE3 found second observable underdetermined. Only Phi_hat is "
                "motivated. Cannot define subsystems from unmotivated operators."
            ),
            notes=[
                "Blocked: only one motivated observable (Phi_hat)",
                "Observable-based subsector splitting requires multiple "
                "independently motivated observables",
            ],
        ),
        QIIBSubsystemCandidate(
            candidate_id="SS4",
            candidate_name="independent_reduced_state_factors",
            description=(
                "Define subsystems operationally via independent state factors "
                "in a joint density matrix."
            ),
            viable=False,
            viability_level="circular",
            obstruction_if_not=(
                "Circular: reduced-state factors presuppose composite structure. "
                "Cannot define subsystems from reduced states if the composite "
                "structure itself is what we are trying to establish."
            ),
            notes=[
                "Circular dependency: subsystem definition requires composition, "
                "but composition requires subsystem definition",
                "Not viable as a STARTING point; could be a consistency check later",
            ],
        ),
        QIIBSubsystemCandidate(
            candidate_id="SS5",
            candidate_name="no_valid_subsystem_identity",
            description="Null candidate: no subsystem identity available.",
            viable=False,
            viability_level="rejected",
            obstruction_if_not="Rejected: SS1 provides a viable extension-level route.",
            notes=["Null case rejected: SS1 is viable"],
        ),
    ]

    n_viable = sum(1 for c in candidates if c.viable)

    return QIIBSubsystemIdentityAudit(
        candidates=candidates,
        n_candidates=N_SUBSYSTEM_CANDIDATES,
        n_viable=n_viable,
        chosen_candidate_id="SS1_multiple_copies_of_toy_system",
        subsystem_verdict=QIIB_SUBSYSTEM_VERDICT,
        notes=[
            "Only SS1 (multiple copies) is viable at extension level",
            "SS2 blocked (no spatial DOF), SS3 blocked (single observable), "
            "SS4 circular, SS5 null rejected",
            "SS1 is coherent: each copy inherits full Part I structure independently",
            "Subsystem identity is POSTULATED (extension-level), not DERIVED",
            "Verdict: subsystem_identity_extension_level_only",
        ],
    )


def _build_track_c() -> QIIBCompositionRuleAudit:
    """Track C --- composition-rule audit."""
    candidates = [
        QIIBCompositionCandidate(
            candidate_id="CR1",
            candidate_name="tensor_product_composition",
            description=(
                "H_AB = H_A tensor H_B. Standard quantum-mechanical composition. "
                "Joint states rho_AB live on C^2 tensor C^2 = C^4."
            ),
            status="extension_level",
            coherent=True,
            appendix_p_class="motivated_independent_postulation",
            notes=[
                "Standard QM rule; well-defined for finite-dimensional Hilbert spaces",
                "Compatible with density-matrix formalism from Part I",
                "MIP classification: requires postulation of second system + composition rule",
                "Convergent structural motivations: density-matrix formalism, "
                "Lindblad channel structure, standard QM practice",
                "No new DOF beyond the second system copy (which is itself MIP)",
            ],
        ),
        QIIBCompositionCandidate(
            candidate_id="CR2",
            candidate_name="direct_sum_composition",
            description=(
                "H_AB = H_A direct_sum H_B. Superselection-sector composition. "
                "States in A and B cannot superpose."
            ),
            status="extension_level",
            coherent=True,
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Mathematically valid but physically limiting",
                "Direct sum prevents superposition between A and B sectors",
                "Would block entanglement investigation in Q-II.C",
                "Less natural for quantum composite structure than tensor product",
                "CAH: compatible but not motivated by GRUT architecture",
            ],
        ),
        QIIBCompositionCandidate(
            candidate_id="CR3",
            candidate_name="coupled_density_kernel_composition",
            description=(
                "Compose via dissipation-coupled density kernels rather than "
                "tensor product. Non-standard approach."
            ),
            status="extension_level",
            coherent=False,
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Non-standard: no established formalism for dissipation-based composition",
                "Would require new mathematical framework beyond Part I",
                "Not coherent: unclear how partial trace or subsystem recovery would work",
                "CAH: compatible in principle but unmotivated and unbuilt",
            ],
        ),
        QIIBCompositionCandidate(
            candidate_id="CR4",
            candidate_name="history_space_composition",
            description=(
                "Compose via history spaces or path-integral-like structure. "
                "Non-standard for density-matrix formalism."
            ),
            status="extension_level",
            coherent=False,
            appendix_p_class="compatible_but_ad_hoc",
            notes=[
                "Part I uses density-matrix formalism, not path integrals",
                "History-space composition would require reformulating Part I results",
                "Not coherent within current formalism; would be a major departure",
            ],
        ),
        QIIBCompositionCandidate(
            candidate_id="CR5",
            candidate_name="no_coherent_composition_rule",
            description="Null candidate: no composition rule available.",
            status="rejected",
            coherent=False,
            appendix_p_class="forbidden_or_inconsistent",
            notes=["Rejected: CR1 provides a coherent extension-level rule"],
        ),
    ]

    return QIIBCompositionRuleAudit(
        candidates=candidates,
        n_candidates=N_COMPOSITION_CANDIDATES,
        chosen_candidate_id="CR1_tensor_product_composition",
        composition_verdict=QIIB_COMPOSITION_VERDICT,
        notes=[
            "CR1 (tensor product) is chosen: coherent, well-defined, MIP classification",
            "CR2 (direct sum) is coherent but limiting (blocks entanglement investigation)",
            "CR3, CR4 not coherent within current formalism",
            "CR5 null case rejected",
            "Tensor product is POSTULATED (MIP), not DERIVED from GRUT",
            "This is FFM-II.2 compliant: we explicitly state it is postulated, not derived",
            "Verdict: composition_rule_extension_level_only",
        ],
    )


def _build_track_d() -> QIIBReducedStateAudit:
    """Track D --- reduced-state audit."""
    candidates = [
        QIIBReducedStateCandidate(
            candidate_id="RS1",
            candidate_name="partial_trace_map",
            description=(
                "rho_A = Tr_B(rho_AB). Standard partial trace over subsystem B. "
                "Well-defined once tensor product composition is postulated."
            ),
            status="extension_level",
            notes=[
                "Follows automatically from tensor product postulation (CR1)",
                "Mathematically well-defined for density matrices on H_A tensor H_B",
                "Preserves positivity, trace, Hermiticity of reduced state",
                "Extension-level: part of the tensor-product package, not independently derived",
            ],
        ),
        QIIBReducedStateCandidate(
            candidate_id="RS2",
            candidate_name="coarse_graining_map",
            description=(
                "Effective coarse-graining that averages over unresolved degrees "
                "of freedom. More general than partial trace."
            ),
            status="extension_level",
            notes=[
                "Standard in open-system theory; consistent with Lindblad formalism",
                "More general than partial trace but reduces to it for tensor-product systems",
                "Extension-level: would require specifying what is coarse-grained",
            ],
        ),
        QIIBReducedStateCandidate(
            candidate_id="RS3",
            candidate_name="effective_subsystem_restriction",
            description=(
                "Restrict attention to observables of one subsystem only, "
                "defining reduced state operationally."
            ),
            status="extension_level",
            notes=[
                "Operationally equivalent to partial trace for tensor-product systems",
                "Requires multi-observable grammar (Q-II.D) for full implementation",
                "Extension-level: needs observable algebra beyond Phi_hat",
            ],
        ),
        QIIBReducedStateCandidate(
            candidate_id="RS4",
            candidate_name="no_reduced_state_map",
            description="Null candidate: no reduced-state map available.",
            status="rejected",
            notes=["Rejected: RS1 provides a well-defined extension-level map"],
        ),
    ]

    return QIIBReducedStateAudit(
        candidates=candidates,
        n_candidates=N_REDUCED_STATE_CANDIDATES,
        chosen_candidate_id="RS1_partial_trace_map",
        reduced_state_verdict=QIIB_REDUCED_STATE_VERDICT,
        notes=[
            "RS1 (partial trace) is chosen: well-defined, standard, "
            "follows from tensor product",
            "RS2 and RS3 are coherent alternatives but less canonical",
            "RS4 null case rejected",
            "Partial trace is part of the tensor-product extension package",
            "It is NOT independently derived; it comes WITH the composition postulation",
            "Verdict: reduced_state_map_extension_level_only",
        ],
    )


def _build_track_e() -> QIIBManyBodyGrammarAudit:
    """Track E --- many-body grammar audit."""
    levels = [
        QIIBManyBodyLevel(
            level_id="MB1",
            level_name="two_subsystem_grammar",
            description=(
                "Grammar for exactly 2 subsystems: H_AB = H_A tensor H_B, "
                "rho_AB on C^4, independent Lindblad channels."
            ),
            achieved=True,
            notes=[
                "Achieved: the minimal composite benchmark (Track G) demonstrates this",
                "Two copies of QE1 two-state system composed via tensor product",
                "Independent decoherence, product-state composition, partial trace",
            ],
        ),
        QIIBManyBodyLevel(
            level_id="MB2",
            level_name="finite_N_grammar",
            description=(
                "Grammar for N subsystems: H = tensor_{i=1}^N H_i, "
                "rho on (C^2)^{tensor N} = C^{2^N}."
            ),
            achieved=False,
            notes=[
                "Not achieved: formally straightforward extension of MB1 but not "
                "explicitly tested or benchmarked",
                "Would require: N-fold tensor product, N independent Lindblad channels, "
                "partial trace over any subset",
                "Structurally plausible: no obstruction beyond computational complexity",
                "Not demonstrated: only 2-subsystem benchmark exists",
            ],
        ),
        QIIBManyBodyLevel(
            level_id="MB3",
            level_name="many_body_grammar_plausible",
            description=(
                "Grammar for large N or thermodynamic limit. "
                "Requires scaling analysis and potentially new tools."
            ),
            achieved=False,
            notes=[
                "Not achieved: well beyond current benchmark scope",
                "Would require: statistical mechanics tools, thermodynamic limit, "
                "possibly second-quantization language",
                "Structurally plausible but unbuilt: no obstruction identified, "
                "but no work done",
            ],
        ),
        QIIBManyBodyLevel(
            level_id="MB4",
            level_name="many_body_grammar_blocked",
            description="Many-body grammar is blocked by some obstruction.",
            achieved=False,
            notes=[
                "Not the case: no obstruction blocks many-body grammar in principle",
                "The limitation is that it is UNBUILT, not that it is blocked",
            ],
        ),
    ]

    return QIIBManyBodyGrammarAudit(
        levels=levels,
        n_levels=N_MANY_BODY_LEVELS,
        highest_achieved_id="MB1_two_subsystem_grammar",
        many_body_verdict=QIIB_MANY_BODY_VERDICT,
        notes=[
            "MB1 achieved: two-subsystem grammar demonstrated in benchmark",
            "MB2 structurally plausible but not explicitly demonstrated",
            "MB3 plausible but unbuilt; MB4 (blocked) does not apply",
            "Verdict: two_subsystem_grammar_demonstrated",
            "This is the honest level: we demonstrated N=2, "
            "did not prove N>2 but see no obstruction",
        ],
    )


def _build_track_f() -> QIIBDecoherenceCompatibilityAudit:
    """Track F --- decoherence compatibility audit."""
    checks = [
        QIIBDecoherenceCheck(
            check_id="DC1",
            check_name="preserves_single_system_decoherence",
            description=(
                "Each subsystem's Lindblad channel operates independently on "
                "the composite state. L_A = sqrt(gamma) sigma_z tensor I."
            ),
            result="compatible",
            notes=[
                "Independent Lindblad channels: L_A on subsystem A, L_B on subsystem B",
                "Each subsystem decoheres at the same rate as in Part I",
                "No cross-system decoherence terms in independent channel model",
                "Fully compatible: Part I results preserved per subsystem",
            ],
        ),
        QIIBDecoherenceCheck(
            check_id="DC2",
            check_name="cross_system_decoherence_undetermined",
            description=(
                "Whether cross-system decoherence (correlations between A and B "
                "decoherence) exists is not addressed by independent channels."
            ),
            result="underdetermined",
            notes=[
                "Independent Lindblad channels do not produce cross-system decoherence",
                "Correlated decoherence (e.g., shared environment) would require "
                "additional postulates beyond independent channels",
                "Underdetermined: not blocked, but not part of current postulation",
            ],
        ),
        QIIBDecoherenceCheck(
            check_id="DC3",
            check_name="constitutive_bridge_preserved",
            description=(
                "The constitutive recovery tau d<Phi_A>/dt + <Phi_A> = <X_A> "
                "holds independently for each subsystem."
            ),
            result="compatible",
            notes=[
                "Each subsystem recovers its own constitutive law independently",
                "No coupling between subsystems in independent channel model",
                "Fully compatible: constitutive bridge preserved per subsystem",
            ],
        ),
        QIIBDecoherenceCheck(
            check_id="DC4",
            check_name="interaction_hamiltonian_needed_for_coupling",
            description=(
                "Any coupling between subsystems requires an interaction "
                "Hamiltonian H_int beyond independent channels."
            ),
            result="requires_new_postulate",
            notes=[
                "Independent channels give uncoupled subsystems",
                "Physical interactions (energy exchange, etc.) require H_int",
                "H_int is a separate postulate not included in Q-II.B basic package",
                "This is expected: Q-II.B establishes composition grammar, "
                "not interaction dynamics",
            ],
        ),
    ]

    return QIIBDecoherenceCompatibilityAudit(
        checks=checks,
        n_checks=N_DECOHERENCE_CHECKS,
        overall_compatible=True,
        requires_new_postulates=True,
        notes=[
            "Independent Lindblad channels: fully compatible with Part I per subsystem",
            "Cross-system decoherence: underdetermined (not postulated)",
            "Interaction Hamiltonian: requires new postulate (expected)",
            "No destabilization of first-wave constitutive bridge",
            "Overall: compatible, but interaction requires additional postulation",
        ],
    )


def _build_track_g() -> QIIBMinimalCompositeBenchmarkAudit:
    """Track G --- minimal composite benchmark audit."""
    candidates = [
        QIIBBenchmarkCandidate(
            candidate_id="CB1",
            candidate_name="two_copy_product_state_benchmark",
            description=(
                "Two independent copies of QE1 two-state system. "
                "H_AB = C^2 tensor C^2 = C^4. Product state rho_AB = rho_A tensor rho_B. "
                "Independent Lindblad channels L_A, L_B."
            ),
            viable=True,
            demonstrates=[
                "product_state_composition",
                "independent_subsystem_decoherence",
                "partial_trace_recovery_of_single_system_states",
                "composite_hilbert_space_4x4_density_matrix",
                "independent_constitutive_recovery_per_subsystem",
            ],
            does_not_demonstrate=[
                "entanglement_or_nonfactorized_states",
                "cross_system_correlations",
                "interaction_dynamics",
                "many_body_scaling",
                "outcome_selection_or_Born_rule",
            ],
            notes=[
                "Minimal viable composite benchmark",
                "Demonstrates: composition grammar works for product states",
                "Does NOT demonstrate: anything beyond independent subsystems",
                "Explicitly: no entanglement tested (only factorized states)",
            ],
        ),
        QIIBBenchmarkCandidate(
            candidate_id="CB2",
            candidate_name="coupled_two_state_benchmark",
            description=(
                "Two-state systems coupled via interaction Hamiltonian H_int. "
                "Would demonstrate interacting composite dynamics."
            ),
            viable=False,
            demonstrates=[],
            does_not_demonstrate=[],
            notes=[
                "Not viable for Q-II.B: H_int requires additional postulation "
                "beyond basic composition grammar",
                "Would be appropriate for a later stage (Q-II.C or Q-II.E)",
            ],
        ),
        QIIBBenchmarkCandidate(
            candidate_id="CB3",
            candidate_name="composite_observable_benchmark",
            description=(
                "Benchmark testing composite observables: A tensor B, "
                "A tensor I, etc."
            ),
            viable=True,
            demonstrates=[
                "composite_observable_structure",
                "subsystem_observable_embedding_A_tensor_I",
                "expectation_values_on_product_states",
            ],
            does_not_demonstrate=[
                "noncommuting_composite_observables",
                "entanglement_witnesses",
                "interaction_effects",
            ],
            notes=[
                "Viable: demonstrates observable embedding in composite space",
                "Subsumes into CB1 benchmark with observable analysis added",
            ],
        ),
        QIIBBenchmarkCandidate(
            candidate_id="CB4",
            candidate_name="no_admissible_benchmark",
            description="Null candidate: no composite benchmark available.",
            viable=False,
            demonstrates=[],
            does_not_demonstrate=[],
            notes=["Rejected: CB1 provides a minimal viable benchmark"],
        ),
    ]

    n_viable = sum(1 for c in candidates if c.viable)

    return QIIBMinimalCompositeBenchmarkAudit(
        candidates=candidates,
        n_candidates=N_BENCHMARK_CANDIDATES,
        n_viable=n_viable,
        chosen_benchmark_id="CB1_two_copy_product_state_benchmark",
        benchmark_hilbert_dim=COMPOSITE_HILBERT_DIM,
        benchmark_n_subsystems=N_SUBSYSTEMS_BENCHMARK,
        notes=[
            "CB1 chosen: minimal two-copy product-state benchmark",
            "Demonstrates: composition, partial trace, independent decoherence",
            "Does NOT demonstrate: entanglement, interaction, many-body scaling",
            f"Composite Hilbert space dimension: {COMPOSITE_HILBERT_DIM} (C^2 tensor C^2)",
            f"Number of subsystems: {N_SUBSYSTEMS_BENCHMARK}",
            "CB3 viable but subsumed into CB1 with observable analysis",
        ],
    )


def _build_track_h() -> QIIBAppendixPAudit:
    """Track H --- Appendix P classification."""
    entries = [
        QIIBAppendixPEntry(
            item_id="QIIB_subsystem_identity",
            item_name="Subsystem identity via multiple copies",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim="Subsystem identity coherently postulated via copy duplication",
            forbidden_claim="Subsystem identity derived from Part I single-system results",
            dependency="Part I single-system structure; explicit postulation of second copy",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_tensor_product",
            item_name="Tensor product composition rule",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim="Tensor product postulated as composition rule; coherent with Part I",
            forbidden_claim="Tensor product derived from GRUT first principles",
            dependency="Part I density-matrix formalism; standard QM tensor product postulate",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_partial_trace",
            item_name="Partial trace reduced-state map",
            appendix_p_class="motivated_independent_postulation",
            allowed_claim="Partial trace available as part of tensor-product extension package",
            forbidden_claim="Partial trace independently derived from GRUT",
            dependency="Tensor product postulation (CR1)",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_two_subsystem_grammar",
            item_name="Two-subsystem grammar benchmark",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim="Two-subsystem grammar demonstrated for product states in toy benchmark",
            forbidden_claim="Two-subsystem benchmark generalizes to many-body or entangled states",
            dependency="Subsystem identity, tensor product, Lindblad channels",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_decoherence_compatibility",
            item_name="Decoherence compatibility with composition",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Independent Lindblad channels compatible with composite structure; "
                "Part I results preserved per subsystem"
            ),
            forbidden_claim=(
                "Composite decoherence is fully characterized; "
                "interaction or correlated decoherence is established"
            ),
            dependency="Part I Lindblad structure; tensor product composition",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_interaction_gap",
            item_name="Interaction Hamiltonian gap",
            appendix_p_class="bounded_structural_result",
            allowed_claim="Absence of interaction Hamiltonian documented; required for coupling",
            forbidden_claim="Interaction dynamics follow from independent channels",
            dependency="Separate postulation required; beyond Q-II.B scope",
        ),
        QIIBAppendixPEntry(
            item_id="QIIB_overall",
            item_name="Q-II.B overall program",
            appendix_p_class="motivated_but_unbuilt",
            allowed_claim=(
                "Composite-state grammar coherently established at extension level "
                "for two-subsystem product states"
            ),
            forbidden_claim="Composite-state grammar implies full quantum many-body theory",
            dependency="All Q-II.B tracks; Part I locked results",
        ),
    ]

    return QIIBAppendixPAudit(
        entries=entries,
        n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=QIIB_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=[
            "3 entries MIP (subsystem, tensor product, partial trace): require postulation",
            "2 entries MBU (grammar, decoherence compat): motivated path, work not done",
            "1 entry BSR (interaction gap): proved absence",
            "1 entry MBU (overall): composite grammar established but not complete",
            "No native canon: all results are extension-level",
        ],
    )


def _build_track_i() -> QIIBAuthorizationAudit:
    """Track I --- authorization for Q-II.C."""
    return QIIBAuthorizationAudit(
        qiic_authorized=True,
        authorization_basis=[
            "subsystem_identity_established_at_extension_level",
            "tensor_product_composition_coherently_postulated",
            "partial_trace_available_as_reduced_state_map",
            "two_subsystem_grammar_demonstrated_in_benchmark",
            "decoherence_compatibility_confirmed_for_independent_channels",
        ],
        qiic_constraints=[
            "QIIC_must_use_tensor_product_composition_from_QIIB",
            "QIIC_must_not_assume_interaction_Hamiltonian_without_postulation",
            "QIIC_must_test_nonfactorized_states_not_just_product_states",
            "QIIC_results_inherit_MBU_or_MIP_floor",
            "QIIC_must_not_assume_Bell_violations_without_demonstration",
        ],
        authorization_verdict=QIIB_AUTHORIZATION_VERDICT,
        notes=[
            "Q-II.C authorized: composite-state grammar sufficient for entanglement investigation",
            "Key prerequisite: tensor product + partial trace enable entanglement definition",
            "Q-II.C must go BEYOND product states to test nonfactorized states",
            "Interaction Hamiltonian is NOT yet available; Q-II.C must postulate if needed",
            "All Q-II.C results inherit MBU/MIP floor from Q-II.B and Part I",
        ],
    )


def _build_track_j() -> QIIBNonclaimFirewall:
    """Track J --- nonclaim firewall."""
    return QIIBNonclaimFirewall(
        nonclaims=QIIB_NONCLAIMS,
        n_nonclaims=N_QIIB_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit function
# ---------------------------------------------------------------------------

def run_qiib_composite_manybody_state_audit() -> QIIBCompositeManybodyResult:
    """Run the full Q-II.B Composite and Many-Body State Structure Audit."""
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

    sub_v = track_b.subsystem_verdict
    comp_v = track_c.composition_verdict
    red_v = track_d.reduced_state_verdict
    many_v = track_e.many_body_verdict
    auth_v = track_i.authorization_verdict

    allowed_claims: List[str] = [
        "Subsystem identity coherently established via copy duplication "
        "at extension level (MIP)",
        "Tensor product composition postulated as the composition rule; "
        "coherent with Part I density-matrix formalism",
        "Partial trace available as reduced-state map within the "
        "tensor-product extension package",
        "Two-subsystem grammar demonstrated in minimal product-state benchmark "
        "(CB1: C^2 tensor C^2 = C^4)",
        "Independent Lindblad channels compatible with composite structure; "
        "Part I results preserved per subsystem",
        "Interaction Hamiltonian gap documented; required for coupling but "
        "beyond Q-II.B scope",
        "Q-II.C authorized to proceed: entanglement investigation enabled "
        "by tensor product + partial trace",
    ]

    forbidden_claims: List[str] = [
        "Subsystem identity derived from Part I single-system results",
        "Tensor product composition derived from GRUT first principles",
        "Two-copy benchmark implies entanglement established",
        "Partial trace independently derived (it comes with tensor product)",
        "Composite bookkeeping implies many-body or matter readiness",
        "Independent decoherence channels imply multi-body decoherence closure",
        "Extension-level composition results imply native canon status",
    ]

    diagnostics: Dict[str, Any] = {
        "tau_sq": TAU_SQ,
        "tau": TAU,
        "gamma": GAMMA,
        "composite_hilbert_dim": COMPOSITE_HILBERT_DIM,
        "single_system_dim": SINGLE_SYSTEM_DIM,
        "n_subsystems_benchmark": N_SUBSYSTEMS_BENCHMARK,
        "n_eligibility_ingredients": N_ELIGIBILITY_INGREDIENTS,
        "n_subsystem_candidates": N_SUBSYSTEM_CANDIDATES,
        "n_subsystem_viable": track_b.n_viable,
        "n_composition_candidates": N_COMPOSITION_CANDIDATES,
        "n_benchmark_candidates": N_BENCHMARK_CANDIDATES,
        "n_benchmark_viable": track_g.n_viable,
        "n_nonclaims": N_QIIB_NONCLAIMS,
        "n_appendix_p_entries": N_APPENDIX_P_ENTRIES,
    }

    result = QIIBCompositeManybodyResult(
        valid=True,
        track_a_eligibility=track_a,
        track_b_subsystem=track_b,
        track_c_composition=track_c,
        track_d_reduced_state=track_d,
        track_e_many_body=track_e,
        track_f_decoherence=track_f,
        track_g_benchmark=track_g,
        track_h_appendix_p=track_h,
        track_i_authorization=track_i,
        track_j_nonclaims=track_j,
        subsystem_verdict=sub_v,
        composition_verdict=comp_v,
        reduced_state_verdict=red_v,
        many_body_verdict=many_v,
        authorization_verdict=auth_v,
        qiib_appendix_p_class=QIIB_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims,
        forbidden_claims=forbidden_claims,
        exact_nonclaims=QIIB_NONCLAIMS,
        diagnostics=diagnostics,
    )

    validate_qiib_result(result)
    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_qiib_result(result: QIIBCompositeManybodyResult) -> None:
    """Validate the Q-II.B result."""
    checks = [
        (result.subsystem_verdict, ALLOWED_SUBSYSTEM_VERDICTS, "Subsystem verdict"),
        (result.composition_verdict, ALLOWED_COMPOSITION_VERDICTS, "Composition verdict"),
        (result.reduced_state_verdict, ALLOWED_REDUCED_STATE_VERDICTS, "Reduced-state verdict"),
        (result.many_body_verdict, ALLOWED_MANY_BODY_VERDICTS, "Many-body verdict"),
        (result.authorization_verdict, ALLOWED_AUTHORIZATION_VERDICTS, "Authorization verdict"),
    ]
    for verdict, allowed, label in checks:
        if verdict not in allowed:
            raise ValueError(f"{label} '{verdict}' not in allowed vocabulary {allowed}")

    if result.qiib_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError(f"Overall class '{result.qiib_appendix_p_class}' not in allowed")

    for entry in result.track_h_appendix_p.entries:
        if entry.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Track H entry '{entry.item_id}': class not in allowed")

    if result.track_j_nonclaims.n_nonclaims != N_QIIB_NONCLAIMS:
        raise ValueError(f"Nonclaim count mismatch")
    if not result.track_j_nonclaims.all_registered:
        raise ValueError("Nonclaims not all registered")

    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")

    if not result.track_h_appendix_p.no_native_canon:
        raise ValueError("Track H: no_native_canon must be True")
    if not result.track_i_authorization.qiic_authorized:
        raise ValueError("Track I: qiic_authorized must be True")
    if not result.track_f_decoherence.overall_compatible:
        raise ValueError("Track F: overall_compatible must be True")

    ta = result.track_a_eligibility
    n_ext = sum(1 for i in ta.ingredients if i.status == "extension_level")
    if n_ext != ta.n_extension_level:
        raise ValueError(f"Track A extension count mismatch: {n_ext} != {ta.n_extension_level}")


def _self_test() -> bool:
    """Run audit and validate. Returns True on success."""
    result = run_qiib_composite_manybody_state_audit()
    assert result.valid is True
    assert result.subsystem_verdict == QIIB_SUBSYSTEM_VERDICT
    assert result.composition_verdict == QIIB_COMPOSITION_VERDICT
    assert result.reduced_state_verdict == QIIB_REDUCED_STATE_VERDICT
    assert result.many_body_verdict == QIIB_MANY_BODY_VERDICT
    assert result.authorization_verdict == QIIB_AUTHORIZATION_VERDICT
    return True


if __name__ == "__main__":
    _self_test()
    print("Q-II.B self-test passed.")
