"""Phase D12 -- Canonical Source/Charge Derivation.

Determines the ontological status of Q in the GRUT strong-field interior
program.  After D11 established that the dual-sector Companion architecture
survives exact two-field treatment, the remaining main blocker before honest
ToE language is the source ontology gap: Q is used in the defect sector
(Family 4, X = M/r^2 + Q/r) but has never been canonically derived.

MISSION: Classify Q's ontological status by testing candidate ontologies
against the explicit requirements that prior phases impose.

D12 DOES NOT:
  - Introduce new numerics (no PDEs, no BVPs)
  - Replace any prior phase result
  - Promote any candidate to canon without derivational warrant

D12 DOES:
  - Reconstruct the full requirement chain from Phase 6C through D11
  - Enumerate and test candidate ontologies for Q
  - Perform systematic elimination and ranking
  - Produce a final canon classification

CANDIDATE ONTOLOGIES TESTED:
  1. topological_winding_number:  Q = n * eta from pi_2(S^2) = Z
  2. noether_charge:              Q from continuous O(3) global symmetry
  3. geometric_support_invariant: Q defined by Component B coefficient match
  4. curvature_triggered_source:  Q from R * |vec_Phi|^2 coupling
  5. memory_sector_emergent:      Q from scalar-memory integral kernel
  6. effective_defect_charge:     Q as phenomenological long-range parameter

CLASSIFICATION OPTIONS:
  - canonically_derived
  - principled_and_strongly_constrained
  - defect_realized_but_not_uniquely_derived
  - still_effective_only
  - unresolved

LOCKED INHERITANCE:
  Phase 6C:  current_closure_insufficient__minimal_additive_source_identified
  Route B/C: insufficient within tested framework
  SLP-I:     source_law_loophole_5_partially_viable__no_grut_native_mechanism
  D1:        provisional_candidate_extension_formulated
  D2:        defect_candidate_numerically_viable
  D3:        scalar_triplet_embedding_most_promising
  D6:        companion_architecture_viable
  D8:        d7_channels_largely_action_derived
  D9:        self_consistent_coupling_viable (proxy-dependent)
  D11:       exact_closure_strongly_supports_d9

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports
(requirements and candidates are reconstructed from documented prior results,
not by calling other modules at runtime).
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants (inherited from prior phases)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC                          # = 1/3
TAU_CANONICAL = math.sqrt((R_S / R_EQ) / 2.0)   # ~ 1.2247
A_CRIT = 1.062
LAMBDA_DEFAULT = 8.0 * math.pi
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)     # ~ 0.1995
COMP_B_COEFF = 1.0 / (8.0 * math.pi)            # ~ 0.03979
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)

# Derived identities used in ontology testing
ETA_SQUARED = ETA_TARGET ** 2                    # = COMP_B_COEFF = 1/(8*pi)
WINDING_NUMBER_N1 = 1                            # minimal hedgehog winding
Q_TOPO_N1 = WINDING_NUMBER_N1 * ETA_TARGET       # ~ 0.1995

# Phase locks referenced
PHASE6_F_AT_REQ = -17.71
N_CANDIDATE_ONTOLOGIES = 6
N_REQUIREMENT_SOURCES = 5


# ================================================================
# Assumptions
# ================================================================

D12_ASSUMPTIONS = [
    "1. Q refers to the charge-like parameter in the Family 4 source law "
    "modification X = M/r^2 + Q/r, where the Q/r term produces the 1/r^2 "
    "energy density (Component B) identified in Phase 6C as missing from "
    "standard GRUT.",

    "2. The requirement chain is reconstructed from documented prior-phase "
    "results: Phase 6C (two-component decomposition), Route B/C closure "
    "(GRUT-native mechanisms insufficient), SLP-I (Family 4 cleanest "
    "candidate), D1-D2 (O(3) triplet admissibility and numerical viability), "
    "D6-D11 (Companion architecture and exact closure).",

    "3. Candidate ontologies are tested against five explicit requirements: "
    "support-class shape match, coefficient logic, GRUT-native origin, "
    "conservation/quantization, and defect-realization alignment.",

    "4. The topological winding number analysis uses the standard result "
    "pi_2(S^2) = Z for the O(3) triplet vacuum manifold.",

    "5. The hedgehog tail energy density eta^2/r^2 is taken from D1-D2 "
    "analytic and numerical results (locked).",

    "6. No new physics is introduced in D12.  All candidate ontologies are "
    "assessed using material already present in D1-D11.",

    "7. The classification logic is deterministic: given the same requirement "
    "matches and ontology test results, the same final classification is "
    "always returned.",

    "8. Conservation of topological charge means: for smooth field "
    "configurations, the winding number n is integer-valued and cannot "
    "change by continuous deformation.  This is topological conservation, "
    "not Noether conservation.",

    "9. The coefficient matching condition eta^2 = 1/(8*pi) = COMP_B_COEFF "
    "is treated as a REQUIREMENT from Phase 6C, not as a prediction of "
    "any candidate ontology.",

    "10. D12 does not address particle identification, quantum corrections, "
    "or phenomenological mass predictions.  It addresses source ontology only.",
]

D12_NONCLAIMS = [
    "1. D12 does NOT claim Q is derived from first principles if the O(3) "
    "triplet sector itself is an extension rather than a consequence of "
    "the scalar-memory theory.",

    "2. D12 does NOT equate topological grounding with canonical derivation. "
    "A quantity can be topologically well-defined and still not uniquely "
    "required by the deeper theory.",

    "3. The classification 'principled and strongly constrained' does NOT "
    "mean 'proven necessary.'  It means the ontology is mathematically "
    "grounded, coefficient-matched, and compatible with all tested "
    "requirements, but the defect sector's existence is not derived.",

    "4. D12 does NOT prove the O(3) triplet is the unique field content "
    "for metric positivity.  It proves only that it is the minimal "
    "admissible content from D1's homotopy analysis.",

    "5. No consciousness, observer, metaphysical, or philosophical argument "
    "is used.  No elegance or thematic similarity is treated as evidence.",

    "6. D12 does NOT close the ontology gap completely.  It narrows the gap "
    "and classifies its current status precisely.",

    "7. The winding number n = 1 for the minimal hedgehog is assumed, not "
    "derived from a stability or energetic argument.",

    "8. D12 does NOT address whether the GRUT framework uniquely requires "
    "metric positivity in the strong-field interior.  It addresses what "
    "Q must be IF metric positivity is demanded.",

    "9. The requirement-matching table is exact for the tested candidate "
    "ontologies.  Untested ontologies may exist.",

    "10. D12 makes no prediction about the value of lambda (defect "
    "self-coupling) or g_p (portal coupling).  These remain scanned "
    "parameters through D11.",
]


# ================================================================
# Dataclasses -- Requirements
# ================================================================

@dataclass
class PhaseRequirement:
    """A single requirement that prior phases impose on Q."""
    requirement_id: str = ""
    source_phase: str = ""
    description: str = ""
    what_q_must_supply: str = ""
    formal_condition: str = ""
    locked: bool = False


@dataclass
class RequirementSet:
    """Complete set of requirements from the prior-phase chain."""
    requirements: List[PhaseRequirement] = field(default_factory=list)
    n_requirements: int = 0
    source_phases: List[str] = field(default_factory=list)


# ================================================================
# Dataclasses -- Ontology Candidates
# ================================================================

@dataclass
class OntologyTest:
    """Result of testing one requirement against one ontology candidate."""
    requirement_id: str = ""
    satisfied: bool = False
    strength: str = ""        # "strong", "partial", "weak", "none"
    explanation: str = ""


@dataclass
class OntologyCandidate:
    """A candidate ontology for Q with all test results."""
    candidate_id: str = ""
    name: str = ""
    description: str = ""
    formula: str = ""
    source_of_justification: str = ""

    # Test results
    support_class_match: bool = False
    support_class_detail: str = ""
    coefficient_match: bool = False
    coefficient_detail: str = ""
    topology_geometry_status: str = ""
    conservation_quantization: str = ""
    grut_native: bool = False
    grut_native_detail: str = ""
    generalizes_beyond_implementation: bool = False
    generalization_detail: str = ""

    # Per-requirement test results
    requirement_tests: List[OntologyTest] = field(default_factory=list)
    n_requirements_satisfied: int = 0
    n_requirements_partial: int = 0
    n_requirements_failed: int = 0

    # Final rating
    rating: str = ""  # "eliminated", "weakly_viable", "strongly_viable",
    #                    "best_supported", "derived"
    rating_explanation: str = ""


@dataclass
class OntologyRanking:
    """Ranked list of ontology candidates."""
    candidates: List[OntologyCandidate] = field(default_factory=list)
    best_candidate_id: str = ""
    best_rating: str = ""
    ranking_order: List[str] = field(default_factory=list)
    ranking_method: str = ""


# ================================================================
# Dataclasses -- Requirement-Candidate Matching
# ================================================================

@dataclass
class RequirementMatchEntry:
    """One row of the requirement-matching table."""
    requirement_id: str = ""
    requirement_description: str = ""
    what_q_must_supply: str = ""
    candidate_id: str = ""
    satisfied: bool = False
    strength: str = ""
    comment: str = ""


@dataclass
class RequirementMatchingTable:
    """Full requirement x candidate matching table."""
    entries: List[RequirementMatchEntry] = field(default_factory=list)
    n_candidates: int = 0
    n_requirements: int = 0


# ================================================================
# Dataclasses -- Logical Circle Closure
# ================================================================

@dataclass
class LogicalCircleClosure:
    """The 'closure of the logical circle' linking all prior phases."""
    phase_6c_link: str = ""
    source_law_link: str = ""
    family_4_link: str = ""
    defect_realization_link: str = ""
    d11_exact_closure_link: str = ""
    closure_paragraph: str = ""
    circle_closed: bool = False
    closure_qualification: str = ""


# ================================================================
# Dataclasses -- Final Classification
# ================================================================

CLASSIFICATION_OPTIONS = [
    "canonically_derived",
    "principled_and_strongly_constrained",
    "defect_realized_but_not_uniquely_derived",
    "still_effective_only",
    "unresolved",
]

ONTOLOGY_RATING_OPTIONS = [
    "eliminated",
    "weakly_viable",
    "strongly_viable",
    "best_supported",
    "derived",
]

REQUIREMENT_STRENGTH_OPTIONS = [
    "strong",
    "partial",
    "weak",
    "none",
]


@dataclass
class D12Classification:
    """Final Phase D12 classification of Q's ontological status."""
    classification: str = ""
    best_ontology: str = ""
    best_ontology_rating: str = ""
    n_eliminated: int = 0
    n_weakly_viable: int = 0
    n_strongly_viable: int = 0
    n_best_supported: int = 0
    n_derived: int = 0
    summary: str = ""
    canon_statement: str = ""
    remaining_gap: str = ""


@dataclass
class D12Result:
    """Master result container for Phase D12."""
    valid: bool = False
    requirements: Optional[RequirementSet] = None
    candidates: Optional[List[OntologyCandidate]] = None
    ranking: Optional[OntologyRanking] = None
    matching_table: Optional[RequirementMatchingTable] = None
    logical_circle: Optional[LogicalCircleClosure] = None
    classification: Optional[D12Classification] = None


# ================================================================
# Requirement reconstruction
# ================================================================

def build_requirement_set() -> RequirementSet:
    """Reconstruct the full requirement chain from Phase 6C through D11.

    Each requirement specifies what prior phases demand of Q.  These are
    NOT inferred or expanded beyond what is documented in D1-D11.
    """
    reqs = [
        PhaseRequirement(
            requirement_id="REQ_6C_SHAPE",
            source_phase="Phase 6C",
            description=(
                "Metric positivity requires a two-component energy density: "
                "Component A (~1/r^4) from the scalar-memory sector and "
                "Component B (~1/r^2) from an as-yet-unidentified source."
            ),
            what_q_must_supply=(
                "A mechanism that produces energy density with a 1/r^2 "
                "radial profile in the strong-field interior."
            ),
            formal_condition="epsilon_B(r) ~ C_B / r^2 for some C_B > 0",
            locked=True,
        ),
        PhaseRequirement(
            requirement_id="REQ_6C_COEFF",
            source_phase="Phase 6C",
            description=(
                "The Component B coefficient is determined by the metric "
                "positivity condition: C_B = 1/(8*pi) = COMP_B_COEFF."
            ),
            what_q_must_supply=(
                "An energy density whose 1/r^2 coefficient equals or can be "
                "tuned to 1/(8*pi)."
            ),
            formal_condition="C_B = 1/(8*pi) ~ 0.03979",
            locked=True,
        ),
        PhaseRequirement(
            requirement_id="REQ_ROUTEBC_CLOSURE",
            source_phase="Route B/C closure + SLP-I",
            description=(
                "No GRUT-native classical mechanism tested in Route B, "
                "Route C, or Source-Law Program I produces Component B. "
                "Family 4 (Q/r) is the cleanest viable mechanism but "
                "requires a charge Q not defined in canonical GRUT."
            ),
            what_q_must_supply=(
                "Either a GRUT-native origin or a principled extension "
                "that justifies introducing Q into the source law."
            ),
            formal_condition=(
                "Q must be either derivable from the GRUT action or "
                "justified by a principled extension mechanism"
            ),
            locked=True,
        ),
        PhaseRequirement(
            requirement_id="REQ_D1_ADMISSIBILITY",
            source_phase="D1 (defect admissibility)",
            description=(
                "The O(3) triplet with vacuum manifold S^2 is the minimal "
                "field content supporting monopole configurations via "
                "pi_2(S^2) = Z.  The hedgehog tail gives epsilon ~ eta^2/r^2."
            ),
            what_q_must_supply=(
                "Alignment with the O(3) hedgehog defect realization: "
                "Q must be identifiable with a parameter of the hedgehog "
                "configuration, and the tail energy must match Component B."
            ),
            formal_condition=(
                "Q identifiable with hedgehog parameter such that "
                "Q-sourced energy ~ eta^2/r^2 with eta^2 = 1/(8*pi)"
            ),
            locked=True,
        ),
        PhaseRequirement(
            requirement_id="REQ_D11_VIABILITY",
            source_phase="D11 (exact two-field closure)",
            description=(
                "The dual-sector Companion architecture survives exact "
                "two-field treatment.  The defect sector provides "
                "Component B that combines with the macro Component A "
                "to achieve metric positivity on [R_eq, R_ext]."
            ),
            what_q_must_supply=(
                "Consistency with the D11 exact coupled solution: Q's "
                "ontology must not contradict the stable, convergent "
                "defect profile found in D11."
            ),
            formal_condition=(
                "Q-ontology consistent with D11 coupled BVP solution "
                "for f(r) on [0.01, 5.0]"
            ),
            locked=True,
        ),
    ]

    return RequirementSet(
        requirements=reqs,
        n_requirements=len(reqs),
        source_phases=list(set(r.source_phase for r in reqs)),
    )


# ================================================================
# Ontology candidate construction and testing
# ================================================================

def _test_candidate_against_requirements(
    candidate: OntologyCandidate,
    requirements: RequirementSet,
) -> OntologyCandidate:
    """Test a single ontology candidate against all requirements.

    Returns the candidate with requirement_tests populated.
    The testing logic is explicit and deterministic -- no hidden scoring.
    """
    tests = []
    n_strong = 0
    n_partial = 0
    n_fail = 0

    for req in requirements.requirements:
        test = _evaluate_single_match(candidate, req)
        tests.append(test)
        if test.strength == "strong":
            n_strong += 1
        elif test.strength == "partial":
            n_partial += 1
        else:
            n_fail += 1

    candidate.requirement_tests = tests
    candidate.n_requirements_satisfied = n_strong
    candidate.n_requirements_partial = n_partial
    candidate.n_requirements_failed = n_fail

    return candidate


def _evaluate_single_match(
    candidate: OntologyCandidate,
    req: PhaseRequirement,
) -> OntologyTest:
    """Evaluate whether a candidate satisfies a single requirement.

    This function encodes the explicit matching logic for each
    (candidate, requirement) pair.  It is structured as a dispatch
    on requirement_id and candidate_id so that every evaluation is
    traceable and auditable.
    """
    cid = candidate.candidate_id
    rid = req.requirement_id

    # ------- REQ_6C_SHAPE: 1/r^2 energy density profile -------
    if rid == "REQ_6C_SHAPE":
        if cid == "topological_winding_number":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="strong",
                explanation=(
                    "Hedgehog tail gives epsilon ~ n^2 * eta^2 / r^2.  "
                    "For n=1: epsilon ~ eta^2 / r^2, matching 1/r^2 shape."
                ),
            )
        elif cid == "noether_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "O(3) Noether charges exist pre-symmetry-breaking but "
                    "the hedgehog breaks O(3) completely.  No conserved "
                    "Noether current survives to source a 1/r^2 tail."
                ),
            )
        elif cid == "geometric_support_invariant":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "Defines Q by requiring 1/r^2 shape, so shape match "
                    "is tautological.  Does not explain WHY the shape is "
                    "1/r^2, only that it must be."
                ),
            )
        elif cid == "curvature_triggered_source":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "A coupling R * |vec_Phi|^2 could source defect "
                    "formation, but the tail profile depends on the "
                    "curvature profile, not guaranteed to be 1/r^2."
                ),
            )
        elif cid == "memory_sector_emergent":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Source-Law Program I showed Family 5 (processing-"
                    "invariant) collapses to Family 1 at equilibrium.  "
                    "No independent 1/r^2 mechanism from memory sector."
                ),
            )
        elif cid == "effective_defect_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="strong",
                explanation=(
                    "By definition, the effective defect charge "
                    "parameterizes the long-range 1/r^2 tail.  "
                    "Shape match is definitional."
                ),
            )

    # ------- REQ_6C_COEFF: coefficient = 1/(8*pi) -------
    elif rid == "REQ_6C_COEFF":
        if cid == "topological_winding_number":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="strong",
                explanation=(
                    "eta^2 = 1/(8*pi) fixes the coefficient.  With n=1: "
                    "epsilon_tail = eta^2/r^2 = COMP_B_COEFF/r^2.  "
                    "Coefficient is determined by eta, which is the VEV "
                    "of the O(3) triplet.  The value eta^2 = 1/(8*pi) is "
                    "required by Phase 6C, not predicted by the topology."
                ),
            )
        elif cid == "noether_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Noether charges from O(3) are broken by the hedgehog.  "
                    "No surviving charge to fix the coefficient."
                ),
            )
        elif cid == "geometric_support_invariant":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="weak",
                explanation=(
                    "Coefficient is defined to match 1/(8*pi) by "
                    "construction.  Circular: no independent prediction."
                ),
            )
        elif cid == "curvature_triggered_source":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="weak",
                explanation=(
                    "Curvature coupling coefficient is a free parameter "
                    "(not fixed to 1/(8*pi) by any known mechanism)."
                ),
            )
        elif cid == "memory_sector_emergent":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "No memory-sector mechanism produces Component B.  "
                    "Coefficient question is moot."
                ),
            )
        elif cid == "effective_defect_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="weak",
                explanation=(
                    "Effective charge is tuned to match 1/(8*pi).  "
                    "No deeper explanation of the coefficient value."
                ),
            )

    # ------- REQ_ROUTEBC_CLOSURE: GRUT-native or principled extension -------
    elif rid == "REQ_ROUTEBC_CLOSURE":
        if cid == "topological_winding_number":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "The winding number is topologically principled "
                    "(pi_2(S^2) = Z) but requires the O(3) triplet, which "
                    "is an extension of canonical GRUT, not derived from it.  "
                    "The extension is minimal (D1) and uniquely selected by "
                    "the homotopy requirement, but it is still an extension."
                ),
            )
        elif cid == "noether_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Noether charge from O(3) does not survive hedgehog "
                    "symmetry breaking.  Cannot serve as principled Q."
                ),
            )
        elif cid == "geometric_support_invariant":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="weak",
                explanation=(
                    "Defining Q by requirement does not provide a "
                    "principled extension mechanism.  It restates the "
                    "need without satisfying it."
                ),
            )
        elif cid == "curvature_triggered_source":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "Curvature-triggered defect formation is physically "
                    "motivated (strong gravity nucleates defects), but the "
                    "R * |vec_Phi|^2 coupling introduces a free parameter "
                    "and is not uniquely selected."
                ),
            )
        elif cid == "memory_sector_emergent":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Memory-sector mechanisms are GRUT-native but "
                    "Source-Law Program I showed they cannot produce "
                    "Component B.  Fails on mechanism, not on nativeness."
                ),
            )
        elif cid == "effective_defect_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "A purely phenomenological effective charge provides "
                    "no principled extension mechanism."
                ),
            )

    # ------- REQ_D1_ADMISSIBILITY: alignment with O(3) hedgehog -------
    elif rid == "REQ_D1_ADMISSIBILITY":
        if cid == "topological_winding_number":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="strong",
                explanation=(
                    "The winding number IS the hedgehog's topological "
                    "invariant.  Q = n * eta directly parameterizes the "
                    "hedgehog configuration with n from pi_2(S^2) = Z "
                    "and eta from the O(3) VEV.  Perfect alignment."
                ),
            )
        elif cid == "noether_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="weak",
                explanation=(
                    "Noether charges exist for the unbroken O(3) symmetry "
                    "but the hedgehog maps spatial to field directions, "
                    "breaking all three generators.  No Noether charge "
                    "survives to characterize the hedgehog."
                ),
            )
        elif cid == "geometric_support_invariant":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="weak",
                explanation=(
                    "A geometric support invariant defined by 1/(8*pi) "
                    "does not naturally align with the hedgehog ansatz "
                    "Phi_a = eta * f(r) * hat{x}_a.  It is a spectator "
                    "to the defect topology."
                ),
            )
        elif cid == "curvature_triggered_source":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "Curvature triggering could explain WHY the hedgehog "
                    "forms (high curvature nucleates defects) but does not "
                    "identify Q with any hedgehog parameter.  Triggering "
                    "mechanism is compatible but orthogonal to Q-identity."
                ),
            )
        elif cid == "memory_sector_emergent":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Memory sector has no connection to O(3) hedgehog "
                    "topology.  Entirely separate field content."
                ),
            )
        elif cid == "effective_defect_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "The effective charge parameterizes the hedgehog's "
                    "long-range field but does not identify its topological "
                    "or geometric origin within the ansatz."
                ),
            )

    # ------- REQ_D11_VIABILITY: consistency with exact coupled solution -------
    elif rid == "REQ_D11_VIABILITY":
        if cid == "topological_winding_number":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="strong",
                explanation=(
                    "The winding number is preserved by continuous "
                    "deformations of f(r).  The D11 exact coupled BVP "
                    "solution for f(r) is a smooth deformation of the "
                    "uncoupled hedgehog with the same BCs (f=0 at core, "
                    "f=1 at vacuum).  Winding number n=1 is maintained."
                ),
            )
        elif cid == "noether_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "No Noether charge survives the hedgehog.  Not "
                    "relevant to D11 viability."
                ),
            )
        elif cid == "geometric_support_invariant":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="weak",
                explanation=(
                    "Compatible with D11 by definition (does not "
                    "predict anything that D11 could contradict)."
                ),
            )
        elif cid == "curvature_triggered_source":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "Compatible with D11: curvature-triggered formation "
                    "does not constrain the coupled BVP solution.  But "
                    "adds no content beyond compatibility."
                ),
            )
        elif cid == "memory_sector_emergent":
            return OntologyTest(
                requirement_id=rid, satisfied=False, strength="none",
                explanation=(
                    "Memory-sector emergent Q is not viable (eliminated "
                    "by SLP-I).  D11 viability is irrelevant."
                ),
            )
        elif cid == "effective_defect_charge":
            return OntologyTest(
                requirement_id=rid, satisfied=True, strength="partial",
                explanation=(
                    "Effective charge is compatible with any f(r) solution "
                    "by construction (it is defined from the solution's "
                    "long-range behavior).  Weak: does not add content."
                ),
            )

    # Fallback (should not reach here if all combinations are covered)
    return OntologyTest(
        requirement_id=rid, satisfied=False, strength="none",
        explanation=f"No matching logic for ({cid}, {rid}).",
    )


def build_ontology_candidates(
    requirements: RequirementSet,
) -> List[OntologyCandidate]:
    """Construct and test all candidate ontologies for Q.

    Each candidate is built with its properties, then tested against
    all requirements.  The testing logic is in _evaluate_single_match.
    """
    candidates = []

    # ---- Candidate 1: Topological Winding Number ----
    c1 = OntologyCandidate(
        candidate_id="topological_winding_number",
        name="Topological Winding Number",
        description=(
            "Q = n * eta where n is the integer winding number from "
            "pi_2(S^2) = Z classifying the hedgehog configuration of the "
            "O(3) triplet, and eta is the vacuum expectation value. "
            "The winding number is a topological invariant: it cannot "
            "change by continuous deformation of the field."
        ),
        formula="Q = n * eta, n in Z, eta = 1/sqrt(8*pi)",
        source_of_justification=(
            "Homotopy theory: pi_2(S^2) = Z (D1); hedgehog ansatz "
            "Phi_a = eta*f(r)*hat{x}_a (D1); tail energy eta^2/r^2 (D1-D2)"
        ),
        support_class_match=True,
        support_class_detail=(
            "Hedgehog tail: epsilon -> eta^2/r^2 as r -> infinity. "
            "Matches Component B 1/r^2 shape exactly."
        ),
        coefficient_match=True,
        coefficient_detail=(
            "eta^2 = 1/(8*pi) = COMP_B_COEFF fixes the coefficient. "
            "This is required by Phase 6C, not predicted by the topology. "
            "However, eta is the SINGLE free parameter that determines "
            "both the VEV and the Component B coefficient."
        ),
        topology_geometry_status=(
            "Topological: n is an integer homotopy invariant. "
            "Geometric: eta parameterizes the vacuum manifold radius."
        ),
        conservation_quantization=(
            "Quantized: n in Z (integer winding number). "
            "Topologically conserved: n cannot change by continuous "
            "deformation.  NOT Noether-conserved."
        ),
        grut_native=False,
        grut_native_detail=(
            "Requires the O(3) triplet, which is an extension of "
            "canonical GRUT.  D1 shows it is the MINIMAL admissible "
            "extension (selected by homotopy), but it is not derived "
            "from the scalar-memory sector."
        ),
        generalizes_beyond_implementation=True,
        generalization_detail=(
            "pi_2(S^2) = Z applies for arbitrary O(3) triplet "
            "configurations, not only the spherically symmetric hedgehog.  "
            "Higher winding n > 1 configurations exist in principle."
        ),
    )
    c1 = _test_candidate_against_requirements(c1, requirements)
    candidates.append(c1)

    # ---- Candidate 2: Noether Charge ----
    c2 = OntologyCandidate(
        candidate_id="noether_charge",
        name="Noether Charge from O(3)",
        description=(
            "Q as a conserved charge from the continuous O(3) global "
            "symmetry of the triplet Lagrangian.  Three Noether charges "
            "exist (one per generator) in the unbroken phase."
        ),
        formula="Q_a = integral d^3x (partial L / partial dot{Phi}_a) (static: Q_a = 0)",
        source_of_justification=(
            "Noether theorem applied to O(3)-invariant Lagrangian"
        ),
        support_class_match=False,
        support_class_detail=(
            "Noether charges are broken by the hedgehog (O(3) -> nothing).  "
            "No surviving charge to produce a long-range 1/r^2 tail."
        ),
        coefficient_match=False,
        coefficient_detail="No coefficient: charge does not survive.",
        topology_geometry_status=(
            "Geometric (continuous symmetry), but broken by the hedgehog."
        ),
        conservation_quantization=(
            "Would be conserved if O(3) were unbroken.  But the hedgehog "
            "completely breaks O(3), so Noether charges are not conserved "
            "in the defect background."
        ),
        grut_native=False,
        grut_native_detail=(
            "Requires O(3) triplet (same extension as topological candidate).  "
            "Additionally, the charges do not survive symmetry breaking."
        ),
        generalizes_beyond_implementation=False,
        generalization_detail=(
            "Noether charges vanish in any hedgehog background.  "
            "No generalization pathway."
        ),
    )
    c2 = _test_candidate_against_requirements(c2, requirements)
    candidates.append(c2)

    # ---- Candidate 3: Geometric Support Invariant ----
    c3 = OntologyCandidate(
        candidate_id="geometric_support_invariant",
        name="Geometric Support Invariant",
        description=(
            "Q defined implicitly as whatever parameter produces the "
            "Component B coefficient 1/(8*pi).  This is a backward "
            "definition from the requirement, not a forward derivation."
        ),
        formula="Q_geom defined by: Q_geom^2 / (2*tau^2) = 1/(8*pi)",
        source_of_justification=(
            "Phase 6C metric positivity condition (requirement, not derivation)"
        ),
        support_class_match=True,
        support_class_detail=(
            "1/r^2 shape match is tautological: Q_geom is defined to "
            "produce it."
        ),
        coefficient_match=True,
        coefficient_detail=(
            "Coefficient match is tautological: Q_geom is defined to "
            "give 1/(8*pi)."
        ),
        topology_geometry_status="Geometric by name only.  No topological content.",
        conservation_quantization=(
            "No conservation or quantization: Q_geom is a free parameter, "
            "not an integer invariant."
        ),
        grut_native=False,
        grut_native_detail=(
            "Defined from the requirement, not from GRUT structure.  "
            "Purely phenomenological."
        ),
        generalizes_beyond_implementation=False,
        generalization_detail=(
            "No generalization: defined only for the specific "
            "Phase 6C requirement."
        ),
    )
    c3 = _test_candidate_against_requirements(c3, requirements)
    candidates.append(c3)

    # ---- Candidate 4: Curvature-Triggered Source ----
    c4 = OntologyCandidate(
        candidate_id="curvature_triggered_source",
        name="Curvature-Triggered Source Invariant",
        description=(
            "Q arises from a direct coupling between spacetime curvature "
            "and the defect field: L_trigger = xi * R * |vec_Phi|^2.  "
            "In regions of strong curvature (near r = 0), this coupling "
            "could nucleate or stabilize the hedgehog defect."
        ),
        formula="L_trigger = xi * R * |vec_Phi|^2; Q_curv ~ sqrt(xi * R(r))",
        source_of_justification=(
            "Standard non-minimal coupling in curved-space QFT; "
            "D10 trigger analysis (Kretschner family best-supported)"
        ),
        support_class_match=True,
        support_class_detail=(
            "If the coupling produces a stable hedgehog, the tail "
            "gives 1/r^2.  But the intermediate-radius profile depends "
            "on the curvature profile R(r), which is NOT generically 1/r^2."
        ),
        coefficient_match=False,
        coefficient_detail=(
            "xi is a free coupling constant.  No mechanism fixes "
            "xi to produce eta^2 = 1/(8*pi) without external input."
        ),
        topology_geometry_status=(
            "Geometric (curvature-dependent) but not topological.  "
            "The coupling xi * R * |Phi|^2 is a standard non-minimal "
            "coupling, not a topological invariant."
        ),
        conservation_quantization=(
            "Not quantized: xi is continuous.  Not conserved: the "
            "curvature-triggered charge is curvature-dependent and "
            "varies with the metric."
        ),
        grut_native=False,
        grut_native_detail=(
            "Requires both the O(3) triplet extension AND a new "
            "non-minimal coupling parameter xi.  Less minimal than "
            "the topological candidate."
        ),
        generalizes_beyond_implementation=True,
        generalization_detail=(
            "Applies to any curved spacetime, not only the Schwarzschild "
            "interior.  But adds a free parameter (xi) at each application."
        ),
    )
    c4 = _test_candidate_against_requirements(c4, requirements)
    candidates.append(c4)

    # ---- Candidate 5: Memory-Sector Emergent Charge ----
    c5 = OntologyCandidate(
        candidate_id="memory_sector_emergent",
        name="Memory-Sector Emergent Charge",
        description=(
            "Q as an emergent quantity from the scalar-memory integral "
            "kernel.  If the memory equation tau*dPhi/dt + Phi = X(r) "
            "could generate an effective 1/r contribution through "
            "nonlocal kernel effects, Q would be GRUT-native."
        ),
        formula="Q_mem = functional of integral kernel K(t-t')",
        source_of_justification=(
            "GRUT memory equation; Route C analysis; Source-Law Program I "
            "Family 5 (processing-invariant)"
        ),
        support_class_match=False,
        support_class_detail=(
            "Source-Law Program I proved: (a) Route C with any kernel "
            "locks the profile to 1/r^4 (source-profile locking theorem); "
            "(b) Family 5 collapses to Family 1 at equilibrium.  "
            "No 1/r^2 mechanism from the memory sector."
        ),
        coefficient_match=False,
        coefficient_detail="Moot: no 1/r^2 mechanism exists.",
        topology_geometry_status="Neither topological nor geometric.",
        conservation_quantization="Not applicable: no charge emerges.",
        grut_native=True,
        grut_native_detail=(
            "This IS the GRUT-native candidate.  However, SLP-I proves "
            "it cannot produce Component B.  GRUT-native but mechanism-"
            "eliminated."
        ),
        generalizes_beyond_implementation=False,
        generalization_detail="Eliminated by SLP-I.  No pathway remains.",
    )
    c5 = _test_candidate_against_requirements(c5, requirements)
    candidates.append(c5)

    # ---- Candidate 6: Effective Defect Charge ----
    c6 = OntologyCandidate(
        candidate_id="effective_defect_charge",
        name="Effective Defect Charge",
        description=(
            "Q as a phenomenological parameter that captures the "
            "long-range influence of the defect without specifying "
            "its microscopic origin.  Q_eff is defined operationally: "
            "it is whatever coefficient appears in the 1/r^2 tail "
            "of the defect energy density."
        ),
        formula="Q_eff defined by: epsilon_defect(r) -> Q_eff^2 / r^2 as r -> infty",
        source_of_justification=(
            "Operational definition from defect energy density "
            "(D2 numerical extraction)"
        ),
        support_class_match=True,
        support_class_detail=(
            "By definition.  Effective charge is extracted from the "
            "1/r^2 tail of any defect configuration."
        ),
        coefficient_match=True,
        coefficient_detail=(
            "By tuning: Q_eff is set to match 1/(8*pi) by choosing "
            "eta appropriately.  No independent prediction."
        ),
        topology_geometry_status=(
            "Neither topological nor geometric: purely phenomenological."
        ),
        conservation_quantization=(
            "Not quantized.  Not conserved in any formal sense.  "
            "Stable only if the defect configuration is stable."
        ),
        grut_native=False,
        grut_native_detail=(
            "Requires the O(3) triplet extension.  Additionally, "
            "the effective charge adds no explanatory content beyond "
            "parameterization."
        ),
        generalizes_beyond_implementation=False,
        generalization_detail=(
            "Applies to any defect configuration with a 1/r^2 tail, "
            "but does not predict or constrain which configurations "
            "are physically relevant."
        ),
    )
    c6 = _test_candidate_against_requirements(c6, requirements)
    candidates.append(c6)

    return candidates


# ================================================================
# Ranking
# ================================================================

def rank_ontology_candidates(
    candidates: List[OntologyCandidate],
) -> OntologyRanking:
    """Rank candidates by requirement satisfaction and ontological depth.

    Ranking method: lexicographic on (n_strong, n_partial, -n_fail),
    with ties broken by topological/conservation status.

    Rating assignment:
      - derived:         n_strong == n_req AND grut_native
      - best_supported:  n_strong >= 3 AND quantized AND non-circular
      - strongly_viable: n_strong >= 2
      - weakly_viable:   n_strong + n_partial >= 2
      - eliminated:      otherwise
    """
    for c in candidates:
        # Assign rating based on explicit criteria
        has_quantization = "quantized" in c.conservation_quantization.lower()
        has_topology = "topological" in c.topology_geometry_status.lower()
        non_circular = "tautological" not in c.support_class_detail.lower()
        n_req = len(c.requirement_tests)

        if (c.n_requirements_satisfied == n_req and c.grut_native
                and non_circular):
            c.rating = "derived"
            c.rating_explanation = (
                "All requirements strongly satisfied and GRUT-native."
            )
        elif (c.n_requirements_satisfied >= 3 and has_quantization
              and non_circular):
            c.rating = "best_supported"
            c.rating_explanation = (
                f"{c.n_requirements_satisfied}/{n_req} requirements strongly "
                f"satisfied, quantized, and non-circular."
            )
        elif c.n_requirements_satisfied >= 2:
            c.rating = "strongly_viable"
            c.rating_explanation = (
                f"{c.n_requirements_satisfied}/{n_req} requirements strongly "
                f"satisfied."
            )
        elif (c.n_requirements_satisfied + c.n_requirements_partial) >= 2:
            c.rating = "weakly_viable"
            c.rating_explanation = (
                f"{c.n_requirements_satisfied} strong + "
                f"{c.n_requirements_partial} partial requirement matches."
            )
        else:
            c.rating = "eliminated"
            c.rating_explanation = (
                f"Insufficient requirement satisfaction: "
                f"{c.n_requirements_satisfied} strong, "
                f"{c.n_requirements_partial} partial, "
                f"{c.n_requirements_failed} failed."
            )

    # Sort: (rating_rank, -n_strong, -n_partial, n_fail)
    rating_rank = {
        "derived": 0, "best_supported": 1, "strongly_viable": 2,
        "weakly_viable": 3, "eliminated": 4,
    }
    sorted_candidates = sorted(
        candidates,
        key=lambda c: (
            rating_rank.get(c.rating, 5),
            -c.n_requirements_satisfied,
            -c.n_requirements_partial,
            c.n_requirements_failed,
        ),
    )

    ranking_order = [c.candidate_id for c in sorted_candidates]
    best = sorted_candidates[0] if sorted_candidates else None

    return OntologyRanking(
        candidates=sorted_candidates,
        best_candidate_id=best.candidate_id if best else "",
        best_rating=best.rating if best else "",
        ranking_order=ranking_order,
        ranking_method=(
            "Lexicographic on (rating_tier, -n_strong, -n_partial, n_fail). "
            "Rating tiers: derived > best_supported > strongly_viable > "
            "weakly_viable > eliminated.  Tier assignment uses explicit "
            "criteria (see rank_ontology_candidates docstring)."
        ),
    )


# ================================================================
# Requirement-Matching Table
# ================================================================

def build_matching_table(
    candidates: List[OntologyCandidate],
    requirements: RequirementSet,
) -> RequirementMatchingTable:
    """Build the full requirement x candidate matching table."""
    entries = []
    for c in candidates:
        for test in c.requirement_tests:
            req = next(
                (r for r in requirements.requirements
                 if r.requirement_id == test.requirement_id),
                None,
            )
            entries.append(RequirementMatchEntry(
                requirement_id=test.requirement_id,
                requirement_description=req.description if req else "",
                what_q_must_supply=req.what_q_must_supply if req else "",
                candidate_id=c.candidate_id,
                satisfied=test.satisfied,
                strength=test.strength,
                comment=test.explanation,
            ))

    return RequirementMatchingTable(
        entries=entries,
        n_candidates=len(candidates),
        n_requirements=requirements.n_requirements,
    )


# ================================================================
# Logical Circle Closure
# ================================================================

def build_logical_circle_closure(
    ranking: OntologyRanking,
) -> LogicalCircleClosure:
    """Construct the 'closure of the logical circle' statement.

    Links Phase 6C -> source-law narrowing -> Family 4 -> defect realization
    -> D11 exact closure into a single coherent chain.
    """
    best_id = ranking.best_candidate_id
    best_rating = ranking.best_rating

    phase_6c_link = (
        "Phase 6C identifies that metric positivity in the strong-field "
        "interior requires a two-component energy density: Component A "
        "(~1/r^4, from the scalar-memory sector) and Component B "
        "(~1/r^2, coefficient 1/(8*pi), from an unknown source)."
    )

    source_law_link = (
        "Route B/C closure and Source-Law Program I systematically exhaust "
        "all GRUT-native classical mechanisms for generating Component B.  "
        "The source-profile locking theorem proves that no kernel "
        "modification of the memory equation changes the 1/r^4 spatial "
        "profile.  Of five tested source families, only Family 4 "
        "(defect/topological: X = M/r^2 + Q/r) cleanly produces the "
        "required 1/r^2 energy density."
    )

    family_4_link = (
        "Family 4 requires a charge-like parameter Q not present in "
        "canonical GRUT.  The homotopy analysis of D1 identifies the "
        "O(3) triplet with vacuum manifold S^2 as the minimal field "
        "content supporting monopole configurations (pi_2(S^2) = Z).  "
        "The hedgehog ansatz Phi_a = eta * f(r) * hat{x}_a produces "
        "a radial profile whose asymptotic energy density is exactly "
        "eta^2/r^2, matching Component B when eta^2 = 1/(8*pi)."
    )

    defect_realization_link = (
        "D2 confirms numerical viability of the hedgehog BVP.  D6 "
        "establishes the Companion architecture (macro + defect sectors).  "
        "D8 derives the portal coupling from the action.  D9 demonstrates "
        "self-consistent viability (proxy-dependent).  The defect "
        "realization of Component B is thus not a single-step assumption "
        "but a multi-phase construction tested across D1-D9."
    )

    d11_link = (
        "D11 replaces the D9 proxy with an exact two-field BVP for "
        "Phi(r) and f(r).  The Companion architecture survives exact "
        "treatment on [R_eq, R_ext], and D9 is retrospectively assessed "
        "as a good approximation.  The defect sector's contribution to "
        "metric positivity is not an artifact of the proxy closure."
    )

    # Determine circle closure status
    if best_rating in ("derived", "best_supported"):
        circle_closed = True
        if best_rating == "derived":
            qualification = (
                "The logical circle is closed: Q is canonically derived "
                "from the GRUT structure."
            )
        else:
            qualification = (
                "The logical circle is closed at the level of principled "
                "constraint: Q is identified with the topological winding "
                "number of the O(3) hedgehog (n * eta), which is quantized, "
                "topologically conserved, and coefficient-matched to "
                "Component B.  However, the circle is not closed at the "
                "level of strict derivation because the O(3) triplet "
                "sector is an extension of canonical GRUT, not a "
                "consequence of it."
            )
    else:
        circle_closed = False
        qualification = (
            "The logical circle is not closed.  The best-supported "
            f"ontology ({best_id}) has rating '{best_rating}', which "
            "does not constitute principled closure."
        )

    closure_paragraph = (
        "Phase 6C identifies the metric positivity obstruction and its "
        "two-component decomposition (A ~ 1/r^4, B ~ 1/r^2).  "
        "Route B/C and Source-Law Program I exhaust GRUT-native mechanisms, "
        "isolating Family 4 (Q/r) as the only clean candidate.  "
        "D1's homotopy analysis selects the O(3) triplet as the minimal "
        "admissible field content (pi_2(S^2) = Z), whose hedgehog "
        "configuration produces Q = n * eta with tail energy eta^2/r^2.  "
        "D2 through D9 construct and validate the dual-sector architecture, "
        "and D11 confirms it survives exact treatment.  "
        "Q is therefore best understood as the topological winding number "
        "(n = 1) times the O(3) vacuum expectation value (eta), with "
        "eta^2 = 1/(8*pi) fixed by the Component B requirement.  "
        "This identification is principled and strongly constrained -- "
        "the topology selects the field content, the homotopy quantizes "
        "the winding number, and the coefficient is determined by a single "
        "parameter (eta) -- but it is not a canonical derivation because "
        "the O(3) sector is an extension of GRUT, not derived from it."
    )

    return LogicalCircleClosure(
        phase_6c_link=phase_6c_link,
        source_law_link=source_law_link,
        family_4_link=family_4_link,
        defect_realization_link=defect_realization_link,
        d11_exact_closure_link=d11_link,
        closure_paragraph=closure_paragraph,
        circle_closed=circle_closed,
        closure_qualification=qualification,
    )


# ================================================================
# Final D12 Classification
# ================================================================

def classify_d12(
    ranking: OntologyRanking,
    logical_circle: LogicalCircleClosure,
) -> D12Classification:
    """Produce the final D12 classification of Q's ontological status.

    Classification logic:
      - If best_rating == "derived": canonically_derived
      - If best_rating == "best_supported" AND circle_closed:
            principled_and_strongly_constrained
      - If best_rating == "strongly_viable":
            defect_realized_but_not_uniquely_derived
      - If best_rating == "weakly_viable": still_effective_only
      - Otherwise: unresolved
    """
    best_rating = ranking.best_rating
    best_id = ranking.best_candidate_id

    # Count ratings
    counts = {"eliminated": 0, "weakly_viable": 0, "strongly_viable": 0,
              "best_supported": 0, "derived": 0}
    for c in ranking.candidates:
        counts[c.rating] = counts.get(c.rating, 0) + 1

    # Classification dispatch
    if best_rating == "derived":
        classification = "canonically_derived"
        summary = (
            "Q is canonically derived from the GRUT structure.  "
            "All requirements are strongly satisfied by a GRUT-native "
            "mechanism."
        )
        canon_statement = (
            "Q is the topological charge of the hedgehog defect "
            "configuration, canonically derived from the GRUT field "
            "equations."
        )
        remaining_gap = "None within the tested framework."

    elif best_rating == "best_supported" and logical_circle.circle_closed:
        classification = "principled_and_strongly_constrained"
        summary = (
            "Q is principled and strongly constrained but not canonically "
            "derived.  The best-supported ontology (topological winding "
            "number) satisfies the shape, coefficient, admissibility, and "
            "viability requirements, and is quantized via pi_2(S^2) = Z.  "
            "However, the O(3) triplet sector is an extension of canonical "
            "GRUT, not derived from the scalar-memory theory."
        )
        canon_statement = (
            "Q is the topological winding number (n) times the O(3) "
            "vacuum expectation value (eta): Q = n * eta with n in Z "
            "and eta^2 = 1/(8*pi).  This identification is principled "
            "(topologically grounded, quantized, conserved) and strongly "
            "constrained (uniquely selected by the homotopy requirement "
            "and coefficient matching), but not canonically derived "
            "(the O(3) sector is a minimal extension, not a consequence "
            "of GRUT)."
        )
        remaining_gap = (
            "The O(3) triplet sector is not derived from the GRUT "
            "scalar-memory structure.  Closing this gap would require "
            "either: (a) showing that the GRUT field equations or their "
            "quantum corrections necessarily produce an O(3) triplet, or "
            "(b) identifying a deeper principle that simultaneously "
            "requires both the scalar-memory sector and the defect sector."
        )

    elif best_rating == "strongly_viable":
        classification = "defect_realized_but_not_uniquely_derived"
        summary = (
            "Q is realized through the defect sector but not uniquely "
            "derived.  Multiple strongly viable ontologies remain."
        )
        canon_statement = (
            "Q is best understood as a defect-sector parameter, but "
            "its unique ontological identification is not yet achieved."
        )
        remaining_gap = (
            "Multiple viable ontologies; unique selection not possible "
            "from current material."
        )

    elif best_rating == "weakly_viable":
        classification = "still_effective_only"
        summary = (
            "Q remains effectively parameterized but not ontologically "
            "grounded.  No candidate achieves strong viability."
        )
        canon_statement = (
            "Q is a phenomenological parameter.  Its ontological status "
            "is unresolved."
        )
        remaining_gap = "Full source ontology gap remains open."

    else:
        classification = "unresolved"
        summary = (
            "No candidate ontology achieves even weak viability.  "
            "The source ontology gap is fully open."
        )
        canon_statement = "Q is undefined.  Source ontology is unresolved."
        remaining_gap = "Complete: no viable ontology candidate identified."

    return D12Classification(
        classification=classification,
        best_ontology=best_id,
        best_ontology_rating=best_rating,
        n_eliminated=counts.get("eliminated", 0),
        n_weakly_viable=counts.get("weakly_viable", 0),
        n_strongly_viable=counts.get("strongly_viable", 0),
        n_best_supported=counts.get("best_supported", 0),
        n_derived=counts.get("derived", 0),
        summary=summary,
        canon_statement=canon_statement,
        remaining_gap=remaining_gap,
    )


# ================================================================
# Master computation
# ================================================================

def compute_canonical_q_derivation() -> D12Result:
    """Run the full D12 canonical Q derivation analysis.

    Steps:
      1. Reconstruct requirement set from Phase 6C through D11
      2. Build and test ontology candidates
      3. Rank candidates
      4. Build requirement-matching table
      5. Construct logical circle closure statement
      6. Produce final classification

    Returns a D12Result containing all intermediate and final results.
    """
    # Step 1: Requirements
    requirements = build_requirement_set()

    # Step 2: Build and test candidates
    candidates = build_ontology_candidates(requirements)

    # Step 3: Rank
    ranking = rank_ontology_candidates(candidates)

    # Step 4: Matching table
    matching_table = build_matching_table(candidates, requirements)

    # Step 5: Logical circle
    logical_circle = build_logical_circle_closure(ranking)

    # Step 6: Classification
    classification = classify_d12(ranking, logical_circle)

    return D12Result(
        valid=True,
        requirements=requirements,
        candidates=ranking.candidates,  # sorted by rank
        ranking=ranking,
        matching_table=matching_table,
        logical_circle=logical_circle,
        classification=classification,
    )


# ================================================================
# Serialization
# ================================================================

def d12_result_to_dict(result: D12Result) -> Dict[str, Any]:
    """Convert D12Result to a JSON-serializable dictionary."""
    if not result.valid:
        return {"valid": False}

    def _req_to_dict(r: PhaseRequirement) -> Dict[str, Any]:
        return {
            "requirement_id": r.requirement_id,
            "source_phase": r.source_phase,
            "description": r.description,
            "what_q_must_supply": r.what_q_must_supply,
            "formal_condition": r.formal_condition,
            "locked": r.locked,
        }

    def _test_to_dict(t: OntologyTest) -> Dict[str, Any]:
        return {
            "requirement_id": t.requirement_id,
            "satisfied": t.satisfied,
            "strength": t.strength,
            "explanation": t.explanation,
        }

    def _candidate_to_dict(c: OntologyCandidate) -> Dict[str, Any]:
        return {
            "candidate_id": c.candidate_id,
            "name": c.name,
            "description": c.description,
            "formula": c.formula,
            "source_of_justification": c.source_of_justification,
            "support_class_match": c.support_class_match,
            "support_class_detail": c.support_class_detail,
            "coefficient_match": c.coefficient_match,
            "coefficient_detail": c.coefficient_detail,
            "topology_geometry_status": c.topology_geometry_status,
            "conservation_quantization": c.conservation_quantization,
            "grut_native": c.grut_native,
            "grut_native_detail": c.grut_native_detail,
            "generalizes_beyond_implementation":
                c.generalizes_beyond_implementation,
            "generalization_detail": c.generalization_detail,
            "requirement_tests": [_test_to_dict(t)
                                  for t in c.requirement_tests],
            "n_requirements_satisfied": c.n_requirements_satisfied,
            "n_requirements_partial": c.n_requirements_partial,
            "n_requirements_failed": c.n_requirements_failed,
            "rating": c.rating,
            "rating_explanation": c.rating_explanation,
        }

    def _match_entry_to_dict(e: RequirementMatchEntry) -> Dict[str, Any]:
        return {
            "requirement_id": e.requirement_id,
            "candidate_id": e.candidate_id,
            "satisfied": e.satisfied,
            "strength": e.strength,
            "comment": e.comment,
        }

    reqs = result.requirements
    ranking = result.ranking
    mt = result.matching_table
    lc = result.logical_circle
    cls = result.classification

    return {
        "valid": True,
        "requirements": {
            "n_requirements": reqs.n_requirements,
            "source_phases": reqs.source_phases,
            "requirements": [_req_to_dict(r) for r in reqs.requirements],
        },
        "candidates": [_candidate_to_dict(c) for c in result.candidates],
        "ranking": {
            "best_candidate_id": ranking.best_candidate_id,
            "best_rating": ranking.best_rating,
            "ranking_order": ranking.ranking_order,
            "ranking_method": ranking.ranking_method,
        },
        "matching_table": {
            "n_candidates": mt.n_candidates,
            "n_requirements": mt.n_requirements,
            "entries": [_match_entry_to_dict(e) for e in mt.entries],
        },
        "logical_circle": {
            "phase_6c_link": lc.phase_6c_link,
            "source_law_link": lc.source_law_link,
            "family_4_link": lc.family_4_link,
            "defect_realization_link": lc.defect_realization_link,
            "d11_exact_closure_link": lc.d11_exact_closure_link,
            "closure_paragraph": lc.closure_paragraph,
            "circle_closed": lc.circle_closed,
            "closure_qualification": lc.closure_qualification,
        },
        "classification": {
            "classification": cls.classification,
            "best_ontology": cls.best_ontology,
            "best_ontology_rating": cls.best_ontology_rating,
            "n_eliminated": cls.n_eliminated,
            "n_weakly_viable": cls.n_weakly_viable,
            "n_strongly_viable": cls.n_strongly_viable,
            "n_best_supported": cls.n_best_supported,
            "n_derived": cls.n_derived,
            "summary": cls.summary,
            "canon_statement": cls.canon_statement,
            "remaining_gap": cls.remaining_gap,
        },
    }
