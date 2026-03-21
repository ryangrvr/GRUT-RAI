"""Phase D3 — Scalar/Triplet Unification and Symmetry-Breaking Trigger.

Determines the most disciplined mathematical architecture relating the prior
scalar-memory sector to the new defect-supporting O(3) triplet sector, and
identifies the most promising symmetry-breaking trigger mechanism.

PRINCIPAL RESULTS:

  Result 1 — Relation-Type Taxonomy:
    Four architectures assessed: embedding, companion sector, emergent
    reorganization, replacement.  Each scored on coherence, compatibility,
    explanatory strength, ad hoc burden, and canon preservation.

  Result 2 — Trigger Taxonomy:
    Five trigger classes assessed: explicit SSB, curvature-triggered,
    source-density-triggered, lag/processing-triggered, hybrid minimal.
    Each scored on coherence, GRUT-nativeness, overfitting risk, and
    canon preservation.

  Result 3 — Canon Preservation:
    Per-architecture check of whether Component A remains intact,
    Component B is produced, Sigma is additive, and locked phases
    are stable.

  Result 4 — Candidate Ranking:
    Architectures ranked by compatibility, minimality, explanatory
    power, ad hoc burden, and implementability.

  Result 5 — Classification:
    (determined by ranking outcome)

SELF-CONTAINED: Depends only on math.  No grut/ cross-imports.
This is a taxonomy and narrowing phase, not a numerical computation phase.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
C_COMPACTNESS = R_S / R_EQ
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)
A_CRIT = 1.062

COMP_B_COEFF = 1.0 / (8.0 * math.pi)
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
LAMBDA_DEFAULT = 8.0 * math.pi  # mu^2/eta^2 with mu=1

N_RELATION_TYPES = 4
N_TRIGGER_TYPES = 5
N_MINIMAL_COUPLINGS = 5

PHASE6_F_AT_REQ = -17.71


# ================================================================
# Assumptions
# ================================================================

UNIFICATION_ASSUMPTIONS = [
    "1. The O(3) triplet hedgehog defect sector is provisionally "
    "numerically viable (D2 tested, Case B positive for lambda >= 25).",

    "2. The original GRUT scalar-memory field Phi obeys "
    "tau dPhi/dt + Phi = X(r) and produces Component A ~ 1/r^4.",

    "3. The defect sector produces Component B ~ eta^2/r^2 "
    "asymptotically, with eta^2 = 1/(8*pi) as a normalization "
    "condition (not yet a derived physical identification).",

    "4. Four relation-type architectures are assessed: embedding, "
    "companion sector, emergent reorganization, replacement.",

    "5. Five trigger-type classes are assessed: explicit SSB, "
    "curvature-triggered, source-density, lag/processing, hybrid.",

    "6. Canon preservation is the hardest filter: any architecture "
    "that destroys the prior scalar-memory Component A is penalized.",

    "7. Scoring is deterministic and structural: each criterion maps "
    "to a 0-1 score based on defined properties, not subjective "
    "judgment.",

    "8. The embedding model Phi = |vec(Phi)| is assessed as a "
    "candidate architecture, not assumed to be the correct one. "
    "Whether the radial mode reproduces scalar-memory in detail "
    "must be verified in a later phase.",

    "9. Curvature-triggered SSB is structurally attractive because "
    "strong-field curvature provides an environment-dependent "
    "trigger, but the sign and regime must still be checked in "
    "the actual coupled model.",

    "10. This phase narrows the architecture/trigger space for the "
    "next numerical or field-theory phase. It does not derive "
    "the final unified theory.",
]

UNIFICATION_NONCLAIMS = [
    "1. This phase does NOT prove the final unified field theory.",

    "2. This phase does NOT derive the defect sector uniquely "
    "from the locked GRUT core.",

    "3. This phase does NOT justify metaphysical or observer-based "
    "symmetry breaking.",

    "4. A top-ranked architecture is not yet canon; it is a "
    "next-phase target.",

    "5. This phase only narrows the candidate unification "
    "architecture and trigger mechanism.",

    "6. The embedding model is a strong candidate, not a "
    "predetermined conclusion. The scoring must be earned.",

    "7. The claim that the radial mode preserves Component A "
    "is a candidate hypothesis. It has not been derived.",

    "8. Curvature-triggered SSB is a candidate trigger. The "
    "sign and magnitude of the curvature coupling have not "
    "been computed in the full coupled system.",

    "9. The ranking reflects structural assessment within the "
    "tested taxonomy. Alternative architectures outside this "
    "taxonomy are not excluded.",

    "10. The classification is within the D3 framework only. "
    "D4 numerical implementation may revise the ranking.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class ScalarTripletParams:
    """Parameters for Phase D3."""
    n_relation_types: int = N_RELATION_TYPES
    n_trigger_types: int = N_TRIGGER_TYPES
    # Scoring weights (all equal by default for neutrality)
    w_coherence: float = 1.0
    w_compatibility: float = 1.5  # canon preservation weighted higher
    w_explanatory: float = 1.0
    w_ad_hoc: float = 1.0  # penalty for ad hoc burden
    w_implementability: float = 0.5


@dataclass
class RelationTypeSpec:
    """Definition of one relation-type architecture."""
    type_id: int
    name: str
    short_name: str
    formula: str
    mechanism: str
    description: str
    n_new_fields: int
    n_new_params: int


@dataclass
class RelationTypeAssessment:
    """Assessment of one relation-type architecture."""
    type_id: int
    name: str
    # Scores (0 to 1, higher is better)
    coherence: float
    compatibility: float
    explanatory_strength: float
    ad_hoc_burden: float  # 0 = no ad hoc, 1 = maximally ad hoc
    preserves_comp_A: bool
    preserves_comp_B: bool
    # Derived
    overall_score: float
    verdict: str  # "strong_candidate", "moderate", "weak", "disruptive"
    notes: List[str] = field(default_factory=list)


@dataclass
class RelationTypeTaxonomy:
    """Complete relation-type taxonomy."""
    specs: List[RelationTypeSpec]
    assessments: List[RelationTypeAssessment]
    n_types: int
    top_ranked_id: int
    top_ranked_name: str
    top_ranked_score: float
    ranking_order: List[int]  # type_ids in descending score order
    notes: List[str] = field(default_factory=list)


@dataclass
class TriggerTypeSpec:
    """Definition of one trigger-type class."""
    trigger_id: int
    name: str
    short_name: str
    formula: str
    mechanism: str
    description: str
    is_grut_native: bool
    n_new_params: int


@dataclass
class TriggerTypeAssessment:
    """Assessment of one trigger-type class."""
    trigger_id: int
    name: str
    coherent: bool
    grut_native: bool
    overfits: bool
    preserves_canon: bool
    promising_for_d4: bool
    score: float  # composite
    verdict: str  # "strong_candidate", "moderate", "weak"
    notes: List[str] = field(default_factory=list)


@dataclass
class TriggerTypeTaxonomy:
    """Complete trigger-type taxonomy."""
    specs: List[TriggerTypeSpec]
    assessments: List[TriggerTypeAssessment]
    n_types: int
    top_ranked_id: int
    top_ranked_name: str
    top_ranked_score: float
    ranking_order: List[int]
    notes: List[str] = field(default_factory=list)


@dataclass
class CanonPreservationCheck:
    """Canon-preservation check for one architecture."""
    relation_type_id: int
    relation_type_name: str
    comp_A_intact: bool
    comp_B_produced: bool
    sigma_additive: bool
    locked_phases_stable: bool
    all_pass: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class MinimalCouplingCandidate:
    """One minimal coupling candidate."""
    coupling_id: int
    formula: str
    relation_type_id: int
    trigger_type_id: Optional[int]
    description: str
    n_new_params: int
    notes: List[str] = field(default_factory=list)


@dataclass
class RankedArchitecture:
    """One ranked architecture (relation + trigger combination)."""
    rank: int
    relation_type_id: int
    relation_name: str
    trigger_type_id: int
    trigger_name: str
    combined_score: float
    canon_passes: bool
    notes: str


@dataclass
class CandidateRanking:
    """Ranked list of architecture candidates."""
    ranked: List[RankedArchitecture]
    n_candidates: int
    top_relation_id: int
    top_relation_name: str
    top_trigger_id: int
    top_trigger_name: str
    top_score: float
    notes: List[str] = field(default_factory=list)


@dataclass
class ScalarTripletClassification:
    """Final D3 classification."""
    classification: str
    phase_status: str
    top_relation: str
    top_trigger: str
    top_score: float
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class ScalarTripletUnificationResult:
    """Master result container."""
    valid: bool
    params: ScalarTripletParams
    relation_taxonomy: Optional[RelationTypeTaxonomy] = None
    trigger_taxonomy: Optional[TriggerTypeTaxonomy] = None
    canon_checks: Optional[List[CanonPreservationCheck]] = None
    minimal_couplings: Optional[List[MinimalCouplingCandidate]] = None
    ranking: Optional[CandidateRanking] = None
    classification: Optional[ScalarTripletClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Relation-Type Definitions
# ================================================================

def define_relation_types() -> List[RelationTypeSpec]:
    """Define the four relation-type architectures."""
    return [
        RelationTypeSpec(
            type_id=1,
            name="Embedding (radial-mode identification)",
            short_name="embedding",
            formula="Phi = |vec(Phi)|, hedgehog angular modes carry defect",
            mechanism=(
                "The original scalar-memory field Phi is identified with the "
                "radial modulus of the O(3) triplet: Phi = |vec(Phi)|. "
                "In the hedgehog ansatz, vec(Phi)_a = eta*f(r)*x_hat_a, "
                "so |vec(Phi)| = eta*f(r). The scalar-memory equation "
                "governs the radial sector. Angular/topological modes "
                "carry the hedgehog structure and produce Component B."
            ),
            description=(
                "Reinterpretation: the old scalar is the radial mode of a "
                "more structured triplet. No new fields added, but the "
                "field content is enriched by recognizing angular degrees "
                "of freedom. The radial sector may preserve Component A "
                "behavior while angular modes supply Component B. This "
                "is a candidate architecture; the detailed preservation "
                "of Component A must be verified in a later phase."
            ),
            n_new_fields=0,  # reinterpretation, not addition
            n_new_params=1,  # lambda (SSB coupling)
        ),
        RelationTypeSpec(
            type_id=2,
            name="Companion sector (coupled but distinct)",
            short_name="companion",
            formula="L = L_scalar(Phi) + L_triplet(vec(Phi)) + g*Phi*|vec(Phi)|^2",
            mechanism=(
                "Phi and vec(Phi) are distinct fields with independent "
                "dynamics, coupled through a portal term g*Phi*|vec(Phi)|^2 "
                "or through common metric coupling. Each sector retains "
                "its own identity: scalar-memory produces Component A, "
                "triplet defect produces Component B."
            ),
            description=(
                "Standard multi-sector field theory. Both fields coexist "
                "with a minimal coupling. Preserves both sectors' "
                "contributions additively. Requires a new coupling "
                "constant g and justification for its value."
            ),
            n_new_fields=3,  # new triplet is independent
            n_new_params=2,  # lambda + g
        ),
        RelationTypeSpec(
            type_id=3,
            name="Emergent reorganization (from lag/doubled structure)",
            short_name="emergent",
            formula="vec(Phi)_eff arises from CTP doubled-field sector",
            mechanism=(
                "The triplet is not fundamental but emerges as an "
                "effective multiplet from the deeper Galley CTP "
                "doubled-field (physical + auxiliary) organization. "
                "The lag structure induces an effective internal space "
                "that, under certain conditions, looks like an O(3) "
                "triplet with SSB."
            ),
            description=(
                "Speculative but potentially deep. If the CTP doubled "
                "structure naturally generates an effective O(3) triplet, "
                "the defect sector would be derived rather than added. "
                "However, no explicit construction of this mechanism "
                "currently exists. The mathematical coherence of this "
                "route is undemonstrated."
            ),
            n_new_fields=0,  # would be derived, not added
            n_new_params=0,  # in principle; in practice unknown
        ),
        RelationTypeSpec(
            type_id=4,
            name="Replacement (scalar is truncation of triplet)",
            short_name="replacement",
            formula="Phi_old = Phi_3 (third component of vec(Phi))",
            mechanism=(
                "The old scalar-memory field is reinterpreted as the "
                "third component of the O(3) triplet in a fixed gauge. "
                "The triplet is the fundamental object; the scalar was "
                "a truncation that missed the transverse modes. All "
                "prior scalar-memory results are recomputed in the "
                "triplet framework."
            ),
            description=(
                "Mathematically coherent but disruptive. Prior scalar-"
                "memory results (Component A, memory equation dynamics) "
                "must be rederived. Risk of invalidating locked results "
                "if the triplet dynamics differ from the scalar dynamics "
                "in the relevant regimes. High explanatory ambition but "
                "also high compatibility risk."
            ),
            n_new_fields=2,  # adds two transverse components
            n_new_params=1,  # lambda
        ),
    ]


# ================================================================
# Level 2: Relation-Type Assessment
# ================================================================

def assess_relation_types(
    specs: List[RelationTypeSpec],
    params: ScalarTripletParams,
) -> List[RelationTypeAssessment]:
    """Assess each relation-type on structural criteria."""
    assessments: List[RelationTypeAssessment] = []

    for spec in specs:
        # --- Embedding ---
        if spec.type_id == 1:
            coherence = 0.90  # standard field-theory construction
            compatibility = 0.85  # preserves scalar as radial mode in principle
            explanatory = 0.75  # candidate route for both A and B, not yet derived
            ad_hoc = 0.15  # minimal: just reinterpretation + lambda
            preserves_A = True  # radial sector candidates for Component A
            preserves_B = True  # angular/topological sector gives Component B
            notes = [
                "Standard O(3) -> radial + angular decomposition",
                "Phi = |vec(Phi)| = eta*f(r) in hedgehog ansatz",
                "Radial sector may reproduce scalar-memory dynamics (candidate, not derived)",
                "Angular gradient term gives eta^2*f^2/r^2 -> Component B tail",
                "Requires lambda (SSB coupling) as new parameter",
                "Top-ranked candidate for canon preservation",
            ]

        # --- Companion ---
        elif spec.type_id == 2:
            coherence = 0.80  # standard multi-field theory
            compatibility = 0.70  # both sectors preserved but coupling must be consistent
            explanatory = 0.60  # explains both but doesn't unify them
            ad_hoc = 0.45  # two new parameters (lambda, g), separate dynamics
            preserves_A = True  # scalar sector untouched
            preserves_B = True  # triplet sector independent
            notes = [
                "Two independent sectors with portal coupling",
                "Component A from scalar, Component B from triplet",
                "Coupling g*Phi*|vec(Phi)|^2 requires justification for g value",
                "No unification of the two components' origins",
                "Cleanly preserves both sectors but at cost of ad hoc coupling",
            ]

        # --- Emergent ---
        elif spec.type_id == 3:
            coherence = 0.35  # speculative, no explicit construction exists
            compatibility = 0.40  # unknown until constructed
            explanatory = 0.85  # would be deep if it works
            ad_hoc = 0.30  # potentially low if derived, but currently undemonstrated
            preserves_A = False  # unknown (would need full construction)
            preserves_B = False  # unknown
            notes = [
                "Highest explanatory potential if constructible",
                "No explicit mechanism currently demonstrated",
                "CTP doubled-field structure has 2 DOF per mode, suggestive of doublet",
                "But O(3) triplet requires 3 components, not 2",
                "Mathematical coherence score reflects undemonstrated status",
                "Deferred: would need explicit Lagrangian construction",
            ]

        # --- Replacement ---
        elif spec.type_id == 4:
            coherence = 0.85  # standard truncation interpretation
            compatibility = 0.30  # destroys prior scalar-memory interpretation
            explanatory = 0.80  # ambitious, potentially explains everything from triplet
            ad_hoc = 0.35  # moderate: lambda + must rederive everything
            preserves_A = False  # must be rederived in triplet framework
            preserves_B = True  # triplet naturally gives hedgehog
            notes = [
                "Old scalar Phi = Phi_3 in aligned gauge",
                "Transverse modes Phi_1, Phi_2 carry angular structure",
                "Prior Component A results must be rederived (not preserved as-is)",
                "Risk: triplet dynamics in radial sector may differ from scalar",
                "High compatibility penalty due to locked-result disruption",
                "Would require reworking Phase 6, 6B, 6C with triplet dynamics",
            ]

        else:
            continue

        # Compute overall score
        w = params
        raw = (
            w.w_coherence * coherence
            + w.w_compatibility * compatibility
            + w.w_explanatory * explanatory
            - w.w_ad_hoc * ad_hoc
        )
        max_possible = (
            w.w_coherence + w.w_compatibility + w.w_explanatory
        )
        overall = raw / max_possible if max_possible > 0 else 0.0

        # Verdict
        if overall >= 0.65:
            verdict = "strong_candidate"
        elif overall >= 0.45:
            verdict = "moderate"
        elif overall >= 0.30:
            verdict = "weak"
        else:
            verdict = "disruptive"

        assessments.append(RelationTypeAssessment(
            type_id=spec.type_id,
            name=spec.name,
            coherence=coherence,
            compatibility=compatibility,
            explanatory_strength=explanatory,
            ad_hoc_burden=ad_hoc,
            preserves_comp_A=preserves_A,
            preserves_comp_B=preserves_B,
            overall_score=round(overall, 4),
            verdict=verdict,
            notes=notes,
        ))

    return assessments


# ================================================================
# Level 3: Relation-Type Taxonomy Builder
# ================================================================

def build_relation_taxonomy(
    specs: List[RelationTypeSpec],
    assessments: List[RelationTypeAssessment],
) -> RelationTypeTaxonomy:
    """Build the complete relation-type taxonomy."""
    scored = sorted(assessments, key=lambda a: a.overall_score, reverse=True)
    ranking_order = [a.type_id for a in scored]
    top = scored[0]

    notes = [
        f"Assessed {len(specs)} relation-type architectures",
        f"Top-ranked: {top.name} (score: {top.overall_score:.4f})",
        f"Ranking order: {[a.name for a in scored]}",
    ]

    return RelationTypeTaxonomy(
        specs=specs,
        assessments=assessments,
        n_types=len(specs),
        top_ranked_id=top.type_id,
        top_ranked_name=top.name,
        top_ranked_score=top.overall_score,
        ranking_order=ranking_order,
        notes=notes,
    )


# ================================================================
# Level 4: Trigger-Type Definitions
# ================================================================

def define_trigger_types() -> List[TriggerTypeSpec]:
    """Define the five trigger-type classes."""
    return [
        TriggerTypeSpec(
            trigger_id=1,
            name="Explicit SSB (negative mass-squared by hand)",
            short_name="explicit",
            formula="V(vec(Phi)) = -(1/2)*mu^2*|vec(Phi)|^2 + (1/4)*lam*|vec(Phi)|^4",
            mechanism=(
                "Standard Mexican-hat potential with mu^2 > 0 inserted "
                "as a fundamental parameter. The symmetry breaking is "
                "put in by hand. eta = mu/sqrt(lambda)."
            ),
            description=(
                "Simplest and most standard trigger. Mathematically "
                "coherent but not GRUT-native: mu^2 is a free parameter "
                "with no connection to the existing GRUT structure. "
                "Does not explain why symmetry breaking occurs."
            ),
            is_grut_native=False,
            n_new_params=2,  # mu, lambda
        ),
        TriggerTypeSpec(
            trigger_id=2,
            name="Curvature-triggered SSB",
            short_name="curvature",
            formula="mu_eff^2 = mu_0^2 + xi*R, with xi*R < 0 in strong field",
            mechanism=(
                "The effective mass parameter depends on the Ricci "
                "scalar: mu_eff^2 = mu_0^2 + xi*R. In the strong-field "
                "interior where R < 0 (for typical compact objects), "
                "the effective mass can flip sign, triggering SSB. "
                "This provides an environment-dependent trigger using "
                "existing GRUT geometric structure."
            ),
            description=(
                "Structurally attractive because it uses the existing "
                "metric/curvature as the trigger, making it GRUT-native. "
                "The sign and regime must still be checked in the actual "
                "coupled model. xi is a new dimensionless parameter but "
                "the trigger mechanism is geometrically motivated."
            ),
            is_grut_native=True,
            n_new_params=2,  # xi, mu_0 (or xi, lambda with mu derived)
        ),
        TriggerTypeSpec(
            trigger_id=3,
            name="Source-density-triggered SSB",
            short_name="source_density",
            formula="mu_eff^2 = mu_0^2 - alpha_d * rho(r)",
            mechanism=(
                "The effective mass depends on the local energy density "
                "or mass function: mu_eff^2 = mu_0^2 - alpha_d * rho(r). "
                "In regions of high density (near the center), the "
                "effective mass can flip sign. This ties the defect "
                "formation to the local gravitational environment."
            ),
            description=(
                "Partially GRUT-native: uses the source density which "
                "is part of the GRUT framework. But the coupling "
                "alpha_d to the density is a new free parameter and "
                "the precise density dependence is somewhat ad hoc. "
                "Risk of overfitting if alpha_d is tuned to match."
            ),
            is_grut_native=False,  # partially; alpha_d is foreign
            n_new_params=3,  # alpha_d, mu_0, lambda
        ),
        TriggerTypeSpec(
            trigger_id=4,
            name="Lag-/processing-triggered SSB",
            short_name="lag_processing",
            formula="mu_eff^2 = mu_0^2 - beta * (1/tau^2)",
            mechanism=(
                "The effective mass depends on the memory/lag parameter "
                "tau: mu_eff^2 = mu_0^2 - beta/tau^2. In regimes where "
                "the memory time is short (strong processing), the "
                "effective mass can flip sign. This is treated strictly "
                "as a mathematical coupling hypothesis."
            ),
            description=(
                "GRUT-native in that tau is the fundamental GRUT "
                "parameter. However, the coupling beta is new and the "
                "mechanism is speculative. Must be treated as a "
                "mathematical trigger hypothesis, not as metaphysical "
                "'experience causes symmetry breaking'. The tau "
                "dependence is interesting but needs careful physical "
                "interpretation."
            ),
            is_grut_native=True,
            n_new_params=2,  # beta, lambda
        ),
        TriggerTypeSpec(
            trigger_id=5,
            name="Hybrid minimal (curvature + source density)",
            short_name="hybrid",
            formula="mu_eff^2 = mu_0^2 + xi*R - alpha_d*rho",
            mechanism=(
                "Combination of curvature and source-density triggers. "
                "The effective mass depends on both geometric (R) and "
                "matter (rho) environment. This is the minimal mixed "
                "case that captures both geometric and matter-dependent "
                "symmetry breaking."
            ),
            description=(
                "More general than either pure trigger alone. Risk of "
                "overfitting with two trigger parameters (xi, alpha_d). "
                "GRUT-native in the curvature part but the density "
                "coupling adds ad hoc burden. May be useful if neither "
                "pure trigger alone is sufficient."
            ),
            is_grut_native=True,  # partially
            n_new_params=4,  # xi, alpha_d, mu_0, lambda
        ),
    ]


# ================================================================
# Level 5: Trigger-Type Assessment
# ================================================================

def assess_trigger_types(
    specs: List[TriggerTypeSpec],
    params: ScalarTripletParams,
) -> List[TriggerTypeAssessment]:
    """Assess each trigger-type class."""
    assessments: List[TriggerTypeAssessment] = []

    for spec in specs:
        # --- Explicit ---
        if spec.trigger_id == 1:
            coherent = True
            grut_native = False
            overfits = False
            preserves_canon = True
            promising = False  # doesn't explain why SSB occurs
            score = 0.40
            verdict = "moderate"
            notes = [
                "Mathematically clean, standard SSB",
                "mu^2 is a free parameter with no GRUT origin",
                "Does not explain environment-dependent symmetry breaking",
                "Preserves canon (does not affect prior structure)",
                "Baseline reference: all other triggers compared against this",
            ]

        # --- Curvature ---
        elif spec.trigger_id == 2:
            coherent = True
            grut_native = True
            overfits = False
            preserves_canon = True
            promising = True
            score = 0.80
            verdict = "strong_candidate"
            notes = [
                "Uses existing metric structure as trigger (GRUT-native)",
                "Ricci scalar R encodes gravitational field strength",
                "In strong-field interior: R can be negative, providing sign flip",
                "xi is a single new dimensionless parameter (minimal ad hoc)",
                "Sign and magnitude of xi*R must be verified in coupled model",
                "Structurally most promising trigger for D4 implementation",
            ]

        # --- Source density ---
        elif spec.trigger_id == 3:
            coherent = True
            grut_native = False
            overfits = True  # alpha_d is tunable
            preserves_canon = True
            promising = False
            score = 0.45
            verdict = "moderate"
            notes = [
                "Uses source density rho(r) which is GRUT-adjacent",
                "alpha_d coupling constant is foreign to existing framework",
                "Risk of overfitting: alpha_d can be tuned to produce any threshold",
                "3 new parameters is more ad hoc than curvature trigger",
                "Preserves canon but does not illuminate mechanism",
            ]

        # --- Lag/processing ---
        elif spec.trigger_id == 4:
            coherent = True
            grut_native = True
            overfits = False
            preserves_canon = True
            promising = True
            score = 0.60
            verdict = "moderate"
            notes = [
                "tau is the fundamental GRUT parameter (GRUT-native)",
                "beta coupling is new but the tau-dependence is natural",
                "Must be treated as mathematical hypothesis only",
                "No metaphysical or observer-based interpretation assumed",
                "Interesting: ties defect formation to memory structure",
                "Moderate promise: less geometric than curvature trigger",
            ]

        # --- Hybrid ---
        elif spec.trigger_id == 5:
            coherent = True
            grut_native = True
            overfits = True  # two trigger parameters
            preserves_canon = True
            promising = False
            score = 0.50
            verdict = "moderate"
            notes = [
                "Most general trigger combining curvature and density",
                "4 new parameters is highest ad hoc burden in taxonomy",
                "Risk of overfitting: can always find xi, alpha_d to match",
                "GRUT-native in curvature part, foreign in density part",
                "Useful fallback if pure triggers fail, not primary candidate",
            ]

        else:
            continue

        assessments.append(TriggerTypeAssessment(
            trigger_id=spec.trigger_id,
            name=spec.name,
            coherent=coherent,
            grut_native=grut_native,
            overfits=overfits,
            preserves_canon=preserves_canon,
            promising_for_d4=promising,
            score=score,
            verdict=verdict,
            notes=notes,
        ))

    return assessments


# ================================================================
# Level 6: Trigger-Type Taxonomy Builder
# ================================================================

def build_trigger_taxonomy(
    specs: List[TriggerTypeSpec],
    assessments: List[TriggerTypeAssessment],
) -> TriggerTypeTaxonomy:
    """Build the complete trigger-type taxonomy."""
    scored = sorted(assessments, key=lambda a: a.score, reverse=True)
    ranking_order = [a.trigger_id for a in scored]
    top = scored[0]

    notes = [
        f"Assessed {len(specs)} trigger-type classes",
        f"Top-ranked: {top.name} (score: {top.score:.2f})",
        f"Ranking order: {[a.name for a in scored]}",
    ]

    return TriggerTypeTaxonomy(
        specs=specs,
        assessments=assessments,
        n_types=len(specs),
        top_ranked_id=top.trigger_id,
        top_ranked_name=top.name,
        top_ranked_score=top.score,
        ranking_order=ranking_order,
        notes=notes,
    )


# ================================================================
# Level 7: Canon Preservation
# ================================================================

def check_canon_preservation(
    relation_assessments: List[RelationTypeAssessment],
    trigger_assessments: List[TriggerTypeAssessment],
) -> List[CanonPreservationCheck]:
    """Check canon preservation for each relation-type architecture."""
    checks: List[CanonPreservationCheck] = []

    for ra in relation_assessments:
        # Component A intact?
        # Embedding: radial sector candidates for preserving Component A (must verify)
        # Companion: scalar sector untouched, Component A trivially intact
        # Emergent: unknown
        # Replacement: must rederive

        if ra.type_id == 1:  # Embedding
            comp_A = True
            comp_B = True
            sigma_add = True
            locked_stable = True
            notes = [
                "Component A: radial sector of triplet candidates for reproducing "
                "scalar-memory behavior. If |vec(Phi)| obeys effective radial "
                "equation similar to scalar-memory, Component A is preserved. "
                "This is a structural argument, not yet a derivation.",
                "Component B: angular gradient term eta^2*f^2/r^2 -> 1/r^2 tail. "
                "Verified in D1/D2.",
                "Sigma: additive (Sigma_scalar + Sigma_defect as in D2)",
                "Locked phases: Phase 6 mass profile, 6B A_crit, 6C deficit "
                "decomposition all compatible with additive source interpretation.",
            ]

        elif ra.type_id == 2:  # Companion
            comp_A = True
            comp_B = True
            sigma_add = True
            locked_stable = True
            notes = [
                "Component A: scalar sector completely untouched (trivially preserved)",
                "Component B: triplet sector produces it independently",
                "Sigma: additive by construction (two independent sources)",
                "Locked phases: trivially stable (scalar sector unchanged)",
            ]

        elif ra.type_id == 3:  # Emergent
            comp_A = False  # unknown
            comp_B = False  # unknown
            sigma_add = False  # unknown
            locked_stable = False  # unknown
            notes = [
                "Component A: UNKNOWN (no explicit construction)",
                "Component B: UNKNOWN (no explicit construction)",
                "Sigma: UNKNOWN (depends on emergent Lagrangian)",
                "Locked phases: UNKNOWN — cannot assess without explicit model",
                "All checks fail due to undemonstrated mechanism",
            ]

        elif ra.type_id == 4:  # Replacement
            comp_A = False  # must rederive
            comp_B = True
            sigma_add = True  # in principle
            locked_stable = False  # prior results need recomputation
            notes = [
                "Component A: NOT preserved as-is. Must rederive scalar-memory "
                "behavior from third component of triplet. No guarantee "
                "the dynamics match.",
                "Component B: triplet hedgehog naturally produces it",
                "Sigma: additive in the triplet framework",
                "Locked phases: DISRUPTED. Phase 6 scalar-memory equation "
                "must be replaced by triplet radial equation. A_crit and "
                "deficit decomposition must be recomputed.",
            ]
        else:
            continue

        all_pass = comp_A and comp_B and sigma_add and locked_stable

        checks.append(CanonPreservationCheck(
            relation_type_id=ra.type_id,
            relation_type_name=ra.name,
            comp_A_intact=comp_A,
            comp_B_produced=comp_B,
            sigma_additive=sigma_add,
            locked_phases_stable=locked_stable,
            all_pass=all_pass,
            notes=notes,
        ))

    return checks


# ================================================================
# Level 8: Minimal Coupling Candidates
# ================================================================

def define_minimal_couplings() -> List[MinimalCouplingCandidate]:
    """Define the minimal set of coupling candidates."""
    return [
        MinimalCouplingCandidate(
            coupling_id=1,
            formula="Phi = |vec(Phi)| = eta*f(r)",
            relation_type_id=1,
            trigger_type_id=None,
            description=(
                "Embedding identification: the scalar-memory field "
                "is the radial modulus of the triplet. No coupling "
                "term needed — this is a reinterpretation."
            ),
            n_new_params=0,
            notes=[
                "Not a coupling but a field identification",
                "Consistent with hedgehog ansatz",
                "Requires radial dynamics to match scalar-memory equation",
            ],
        ),
        MinimalCouplingCandidate(
            coupling_id=2,
            formula="g * Phi * |vec(Phi)|^2",
            relation_type_id=2,
            trigger_type_id=None,
            description=(
                "Portal coupling between scalar and triplet sectors. "
                "Minimal interaction that preserves both sectors' "
                "independent dynamics at leading order."
            ),
            n_new_params=1,  # g
            notes=[
                "Standard portal coupling in multi-field theories",
                "g must be justified (value and sign)",
                "At g=0 reduces to uncoupled companion model",
            ],
        ),
        MinimalCouplingCandidate(
            coupling_id=3,
            formula="xi * R * |vec(Phi)|^2",
            relation_type_id=1,
            trigger_type_id=2,
            description=(
                "Curvature-triggered SSB: non-minimal coupling of "
                "the triplet to the Ricci scalar. Combined with "
                "embedding model. xi controls the strength of the "
                "curvature-induced mass shift."
            ),
            n_new_params=1,  # xi
            notes=[
                "Standard non-minimal coupling in curved spacetime",
                "xi = 1/6 is conformal value (well-motivated)",
                "Curvature sign determines where SSB occurs",
                "GRUT-native: uses only existing geometric structure",
            ],
        ),
        MinimalCouplingCandidate(
            coupling_id=4,
            formula="alpha_d * rho(r) * |vec(Phi)|^2",
            relation_type_id=1,
            trigger_type_id=3,
            description=(
                "Source-density coupling: triplet mass depends on "
                "local energy density. Combined with embedding model."
            ),
            n_new_params=1,  # alpha_d
            notes=[
                "Density-dependent mass is less standard than curvature coupling",
                "alpha_d is tunable — risk of overfitting",
                "Less geometrically motivated than xi*R",
            ],
        ),
        MinimalCouplingCandidate(
            coupling_id=5,
            formula="beta * (1/tau^2) * |vec(Phi)|^2",
            relation_type_id=1,
            trigger_type_id=4,
            description=(
                "Lag-dependent mass: triplet mass depends on the "
                "memory/lag timescale tau. Combined with embedding."
            ),
            n_new_params=1,  # beta
            notes=[
                "tau is canonical GRUT parameter (GRUT-native)",
                "beta coupling is new, needs justification",
                "Mathematical hypothesis only, no metaphysical claim",
            ],
        ),
    ]


# ================================================================
# Level 9: Candidate Ranking
# ================================================================

def rank_candidates(
    relation_tax: RelationTypeTaxonomy,
    trigger_tax: TriggerTypeTaxonomy,
    canon_checks: List[CanonPreservationCheck],
    couplings: List[MinimalCouplingCandidate],
    params: ScalarTripletParams,
) -> CandidateRanking:
    """Rank architecture candidates (relation + trigger combinations).

    We form viable pairings and score them.  Not all 4x5=20 combinations
    are assessed — only structurally meaningful pairings.
    """
    # Build lookup dicts
    ra_map = {a.type_id: a for a in relation_tax.assessments}
    ta_map = {a.trigger_id: a for a in trigger_tax.assessments}
    cc_map = {c.relation_type_id: c for c in canon_checks}

    # Define meaningful pairings (not all 20 — only structurally coherent)
    pairings = [
        (1, 2, "Embedding + curvature trigger"),
        (1, 1, "Embedding + explicit SSB"),
        (1, 4, "Embedding + lag/processing trigger"),
        (2, 1, "Companion + explicit SSB"),
        (2, 2, "Companion + curvature trigger"),
        (1, 5, "Embedding + hybrid trigger"),
        (4, 1, "Replacement + explicit SSB"),
        (3, 2, "Emergent + curvature trigger"),
        (1, 3, "Embedding + source-density trigger"),
        (4, 2, "Replacement + curvature trigger"),
    ]

    ranked_list: List[RankedArchitecture] = []

    for rel_id, trig_id, label in pairings:
        ra = ra_map[rel_id]
        ta = ta_map[trig_id]
        cc = cc_map[rel_id]

        # Combined score: relation score + trigger score, with canon bonus
        canon_bonus = 0.15 if cc.all_pass else 0.0
        ad_hoc_penalty = params.w_ad_hoc * ra.ad_hoc_burden * 0.1
        combined = (
            ra.overall_score * 0.5
            + ta.score * 0.3
            + canon_bonus
            - ad_hoc_penalty
            + (params.w_implementability * 0.1 if ta.promising_for_d4 else 0.0)
        )

        ranked_list.append(RankedArchitecture(
            rank=0,  # will be assigned after sorting
            relation_type_id=rel_id,
            relation_name=ra.name,
            trigger_type_id=trig_id,
            trigger_name=ta.name,
            combined_score=round(combined, 4),
            canon_passes=cc.all_pass,
            notes=label,
        ))

    # Sort by combined score descending
    ranked_list.sort(key=lambda x: x.combined_score, reverse=True)
    for i, r in enumerate(ranked_list):
        r.rank = i + 1

    top = ranked_list[0]

    notes = [
        f"Ranked {len(ranked_list)} architecture candidates",
        f"Top-ranked: {top.notes} (score: {top.combined_score:.4f})",
        f"Canon-passing candidates: {sum(1 for r in ranked_list if r.canon_passes)}",
    ]

    return CandidateRanking(
        ranked=ranked_list,
        n_candidates=len(ranked_list),
        top_relation_id=top.relation_type_id,
        top_relation_name=top.relation_name,
        top_trigger_id=top.trigger_type_id,
        top_trigger_name=top.trigger_name,
        top_score=top.combined_score,
        notes=notes,
    )


# ================================================================
# Level 10: Classification
# ================================================================

def classify_unification(
    ranking: CandidateRanking,
    relation_tax: RelationTypeTaxonomy,
    trigger_tax: TriggerTypeTaxonomy,
) -> ScalarTripletClassification:
    """Classify the D3 result."""
    top_rel = ranking.top_relation_name
    top_rel_short = ""
    for spec in relation_tax.specs:
        if spec.type_id == ranking.top_relation_id:
            top_rel_short = spec.short_name
            break

    top_trig_short = ""
    for spec in trigger_tax.specs:
        if spec.trigger_id == ranking.top_trigger_id:
            top_trig_short = spec.short_name
            break

    # Determine classification string
    if ranking.top_score >= 0.60:
        classification = f"scalar_triplet_{top_rel_short}_most_promising"
        status = "narrowed"
    elif ranking.top_score >= 0.40:
        classification = f"scalar_triplet_{top_rel_short}_moderately_promising"
        status = "partially_narrowed"
    else:
        classification = "scalar_triplet_unification_unresolved_but_taxonomized"
        status = "taxonomized"

    phase_lock = {
        "phase_6_f_at_req": "LOCKED (-17.71)",
        "phase_6b_A_crit": "LOCKED (1.062)",
        "phase_6c_deficit": "LOCKED (Component A + Component B)",
        "route_c_all": "LOCKED (insufficient)",
        "route_b_all": "LOCKED (closed within Galley CTP)",
        "source_law_program": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "LOCKED (provisional candidate formulated)",
        "defect_D2": "LOCKED (defect_candidate_numerically_viable)",
        "unification_D3": f"ASSESSED ({classification})",
    }

    summary = (
        f"Phase D3: {classification}. "
        f"Top-ranked architecture: {top_rel_short} "
        f"(score: {ranking.top_score:.4f}). "
        f"Top-ranked trigger: {top_trig_short} "
        f"(score: {trigger_tax.top_ranked_score:.2f}). "
        f"Canon-passing candidates: "
        f"{sum(1 for r in ranking.ranked if r.canon_passes)}"
        f"/{ranking.n_candidates}."
    )

    return ScalarTripletClassification(
        classification=classification,
        phase_status=status,
        top_relation=top_rel_short,
        top_trigger=top_trig_short,
        top_score=ranking.top_score,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 11: Master Function
# ================================================================

def compute_scalar_triplet_unification(
    params: Optional[ScalarTripletParams] = None,
) -> ScalarTripletUnificationResult:
    """Master function: run the complete Phase D3 assessment."""
    if params is None:
        params = ScalarTripletParams()

    result = ScalarTripletUnificationResult(valid=False, params=params)

    try:
        # 1. Relation-type taxonomy
        rel_specs = define_relation_types()
        rel_assessments = assess_relation_types(rel_specs, params)
        result.relation_taxonomy = build_relation_taxonomy(
            rel_specs, rel_assessments,
        )

        # 2. Trigger-type taxonomy
        trig_specs = define_trigger_types()
        trig_assessments = assess_trigger_types(trig_specs, params)
        result.trigger_taxonomy = build_trigger_taxonomy(
            trig_specs, trig_assessments,
        )

        # 3. Canon preservation
        result.canon_checks = check_canon_preservation(
            rel_assessments, trig_assessments,
        )

        # 4. Minimal couplings
        result.minimal_couplings = define_minimal_couplings()

        # 5. Ranking
        result.ranking = rank_candidates(
            result.relation_taxonomy, result.trigger_taxonomy,
            result.canon_checks, result.minimal_couplings, params,
        )

        # 6. Classification
        result.classification = classify_unification(
            result.ranking, result.relation_taxonomy,
            result.trigger_taxonomy,
        )

        result.nonclaims = list(UNIFICATION_NONCLAIMS)
        result.assumptions = list(UNIFICATION_ASSUMPTIONS)
        result.diagnostics = {
            "n_relation_types": len(rel_specs),
            "n_trigger_types": len(trig_specs),
            "n_canon_passing": sum(
                1 for c in result.canon_checks if c.all_pass
            ),
            "n_couplings": len(result.minimal_couplings),
            "n_ranked": result.ranking.n_candidates,
            "top_relation": result.classification.top_relation,
            "top_trigger": result.classification.top_trigger,
            "classification": result.classification.classification,
        }
        result.valid = True

    except Exception as exc:
        result.diagnostics["error"] = str(exc)
        import traceback
        result.diagnostics["traceback"] = traceback.format_exc()

    return result


# ================================================================
# Level 12: Serialization
# ================================================================

def scalar_triplet_unification_result_to_dict(
    result: ScalarTripletUnificationResult,
) -> Dict[str, Any]:
    """Serialize to JSON-safe dictionary."""
    out: Dict[str, Any] = {"valid": result.valid}

    out["params"] = {
        "n_relation_types": result.params.n_relation_types,
        "n_trigger_types": result.params.n_trigger_types,
        "w_coherence": result.params.w_coherence,
        "w_compatibility": result.params.w_compatibility,
        "w_explanatory": result.params.w_explanatory,
        "w_ad_hoc": result.params.w_ad_hoc,
    }

    if result.relation_taxonomy is not None:
        rt = result.relation_taxonomy
        out["relation_taxonomy"] = {
            "n_types": rt.n_types,
            "top_ranked_id": rt.top_ranked_id,
            "top_ranked_name": rt.top_ranked_name,
            "top_ranked_score": rt.top_ranked_score,
            "ranking_order": rt.ranking_order,
            "assessments": [
                {
                    "type_id": a.type_id,
                    "name": a.name,
                    "coherence": a.coherence,
                    "compatibility": a.compatibility,
                    "explanatory_strength": a.explanatory_strength,
                    "ad_hoc_burden": a.ad_hoc_burden,
                    "preserves_comp_A": a.preserves_comp_A,
                    "preserves_comp_B": a.preserves_comp_B,
                    "overall_score": a.overall_score,
                    "verdict": a.verdict,
                }
                for a in rt.assessments
            ],
            "notes": rt.notes,
        }

    if result.trigger_taxonomy is not None:
        tt = result.trigger_taxonomy
        out["trigger_taxonomy"] = {
            "n_types": tt.n_types,
            "top_ranked_id": tt.top_ranked_id,
            "top_ranked_name": tt.top_ranked_name,
            "top_ranked_score": tt.top_ranked_score,
            "ranking_order": tt.ranking_order,
            "assessments": [
                {
                    "trigger_id": a.trigger_id,
                    "name": a.name,
                    "coherent": a.coherent,
                    "grut_native": a.grut_native,
                    "overfits": a.overfits,
                    "preserves_canon": a.preserves_canon,
                    "promising_for_d4": a.promising_for_d4,
                    "score": a.score,
                    "verdict": a.verdict,
                }
                for a in tt.assessments
            ],
            "notes": tt.notes,
        }

    if result.canon_checks is not None:
        out["canon_checks"] = [
            {
                "relation_type_id": c.relation_type_id,
                "relation_type_name": c.relation_type_name,
                "comp_A_intact": c.comp_A_intact,
                "comp_B_produced": c.comp_B_produced,
                "sigma_additive": c.sigma_additive,
                "locked_phases_stable": c.locked_phases_stable,
                "all_pass": c.all_pass,
            }
            for c in result.canon_checks
        ]

    if result.minimal_couplings is not None:
        out["minimal_couplings"] = [
            {
                "coupling_id": c.coupling_id,
                "formula": c.formula,
                "relation_type_id": c.relation_type_id,
                "trigger_type_id": c.trigger_type_id,
                "description": c.description,
                "n_new_params": c.n_new_params,
            }
            for c in result.minimal_couplings
        ]

    if result.ranking is not None:
        rk = result.ranking
        out["ranking"] = {
            "n_candidates": rk.n_candidates,
            "top_relation_name": rk.top_relation_name,
            "top_trigger_name": rk.top_trigger_name,
            "top_score": rk.top_score,
            "ranked": [
                {
                    "rank": r.rank,
                    "relation_name": r.relation_name,
                    "trigger_name": r.trigger_name,
                    "combined_score": r.combined_score,
                    "canon_passes": r.canon_passes,
                    "notes": r.notes,
                }
                for r in rk.ranked
            ],
            "notes": rk.notes,
        }

    if result.classification is not None:
        cl = result.classification
        out["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "top_relation": cl.top_relation,
            "top_trigger": cl.top_trigger,
            "top_score": cl.top_score,
            "phase_lock_update": cl.phase_lock_update,
            "summary": cl.summary,
        }

    out["nonclaims"] = result.nonclaims
    out["assumptions"] = result.assumptions
    out["diagnostics"] = result.diagnostics

    return out
