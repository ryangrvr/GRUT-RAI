"""
GRUT Phase D13 -- Geometric Induction of the O(3) Sector
=========================================================

LOCKED INHERITANCE
------------------
- D1: pi_2(S^2) = Z uniquely selects O(3) triplet for monopole-class defects (LOCKED)
- D3: O(3) embedding/companion most promising (LOCKED)
- D8: coupled action S_total = S_grav + S_macro + S_defect + S_trigger + S_portal (LOCKED)
- D11: exact two-field BVP converges; companion architecture survives (STRONGLY SUPPORTED)
- D12: Q = n*eta principled and strongly constrained; O(3) sector not GRUT-native (PRINCIPLED)
- Bridge: O(3) sector derivation is critical gap #1

SCOPE
-----
Test whether the O(3) defect sector can be derived, induced, or strongly
motivated from GRUT-native geometric structure rather than inserted as
an external extension.

MISSION
-------
Evaluate three candidate pathways:
  1. Tetrad / geometric induction from spatial frame structure
  2. Anisotropic memory-kernel tensorization
  3. UV-completion / hidden multiplet interpretation

For each, determine whether it generates:
  - an effective 3-component structure
  - hedgehog/source-class behavior
  - the 1/r^2 Component B support class
  - the eta^2 = 1/(8*pi) coefficient logic
  - strong-curvature activation
  - without smuggling in O(3) by hand

RESULT
------
See classify_geometric_induction() for the final determination.

CLASSIFICATION OPTIONS
----------------------
- canonically_derived_from_geometry
- effectively_induced_but_not_fundamental
- partially_motivated_not_derived
- principled_extension_still_required
- derivation_attempt_failed
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Tuple


# ---------------------------------------------------------------------------
# Classification vocabularies
# ---------------------------------------------------------------------------

D13_CLASSIFICATION_OPTIONS = [
    "canonically_derived_from_geometry",
    "effectively_induced_but_not_fundamental",
    "partially_motivated_not_derived",
    "principled_extension_still_required",
    "derivation_attempt_failed",
]

CONSTRUCTION_VERDICTS = [
    "derived",
    "strongly_induced",
    "partially_motivated",
    "suggestive_only",
    "fails",
]

PATHWAY_VERDICTS = [
    "derived",
    "strongly_supported",
    "partially_motivated",
    "suggestive_only",
    "unsupported",
    "overextended",
]

REQUIREMENT_MATCH_LEVELS = [
    "strong",
    "partial",
    "weak",
    "none",
    "not_applicable",
]

# ---------------------------------------------------------------------------
# Prior-phase requirements (carried from D12)
# ---------------------------------------------------------------------------

PRIOR_REQUIREMENTS = [
    "REQ_6C_SHAPE",       # Component B ~ 1/r^2 radial profile
    "REQ_6C_COEFF",       # Coefficient eta^2 = 1/(8*pi)
    "REQ_ROUTEBC",        # GRUT-native origin or principled extension
    "REQ_D1_HOMOTOPY",    # pi_2 != 0 for monopole-class defects
    "REQ_D11_VIABILITY",  # Consistent with exact coupled BVP
    "REQ_D12_ONTOLOGY",   # Continuity with Q = n*eta winding ontology
]

# ---------------------------------------------------------------------------
# Derivation target criteria
# ---------------------------------------------------------------------------

DERIVATION_CRITERIA = [
    "three_component_structure",   # why 3 components appear
    "o3_organization",             # why O(3)-like symmetry
    "strong_curvature_activation", # why it turns on in strong-field region
    "support_class_1_over_r2",     # produces Component B ~ 1/r^2
    "coefficient_constraint",      # fixes or constrains eta^2 = 1/(8*pi)
    "charge_ontology_alignment",   # aligns with D12 Q = n*eta
]


# ===================================================================
# Dataclasses
# ===================================================================

@dataclass
class DerivationTarget:
    """What it means to 'derive the O(3) sector' -- explicit criteria."""
    criteria: List[str]
    description: str


@dataclass
class CandidateConstruction:
    """A specific geometric construction tested for O(3) induction."""
    name: str
    pathway: str  # "tetrad_geometric", "memory_tensorization", "uv_completion"
    ingredients: List[str]
    construction_description: str
    # Evaluation results
    symmetry_status: str
    grut_native: bool
    support_class_outcome: str
    coefficient_outcome: str
    strong_field_activation: str
    hedgehog_emergence: str
    verdict: str
    reasoning: str

    def __post_init__(self) -> None:
        if self.verdict not in CONSTRUCTION_VERDICTS:
            raise ValueError(
                f"Invalid verdict '{self.verdict}'. "
                f"Must be one of {CONSTRUCTION_VERDICTS}"
            )


@dataclass
class PathwayAssessment:
    """Assessment of a full derivation pathway."""
    pathway: str
    native_to_grut: bool
    mathematical_discipline: str  # "rigorous", "semi_rigorous", "heuristic", "speculative"
    support_class_success: bool
    coefficient_constraint: bool
    ontology_continuity: bool
    strong_field_necessity: bool
    constructions: List[CandidateConstruction]
    verdict: str
    summary: str

    def __post_init__(self) -> None:
        if self.verdict not in PATHWAY_VERDICTS:
            raise ValueError(
                f"Invalid pathway verdict '{self.verdict}'. "
                f"Must be one of {PATHWAY_VERDICTS}"
            )


@dataclass
class RequirementMatchEntry:
    """One row of the requirement-matching table."""
    requirement: str
    tetrad_induction: str
    tensorized_memory: str
    uv_completion: str
    comments: str

    def __post_init__(self) -> None:
        for val in [self.tetrad_induction, self.tensorized_memory, self.uv_completion]:
            if val not in REQUIREMENT_MATCH_LEVELS:
                raise ValueError(
                    f"Invalid match level '{val}'. "
                    f"Must be one of {REQUIREMENT_MATCH_LEVELS}"
                )


@dataclass
class RequirementMatchingTable:
    """Full requirement-matching table across all pathways."""
    entries: List[RequirementMatchEntry]


@dataclass
class DerivationCriterionResult:
    """Result for one derivation criterion across all pathways."""
    criterion: str
    tetrad_result: str
    memory_result: str
    uv_result: str
    best_pathway: str
    notes: str


@dataclass
class D13Classification:
    """Final D13 classification."""
    classification: str
    best_pathway: str
    justification: str
    derivation_criteria_met: int
    derivation_criteria_total: int
    requirements_strong: int
    requirements_total: int

    def __post_init__(self) -> None:
        if self.classification not in D13_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid D13 classification '{self.classification}'. "
                f"Must be one of {D13_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class FoundationalGap:
    """A remaining foundational gap after D13."""
    gap: str
    severity: str  # "critical", "significant", "minor"
    notes: str


@dataclass
class D13Result:
    """Top-level D13 result."""
    valid: bool
    derivation_target: DerivationTarget
    constructions: List[CandidateConstruction]
    pathway_assessments: List[PathwayAssessment]
    requirement_matching: RequirementMatchingTable
    derivation_criteria_results: List[DerivationCriterionResult]
    classification: D13Classification
    remaining_gaps: List[FoundationalGap]
    nonclaims: List[str]


# ===================================================================
# Derivation Target
# ===================================================================

def define_derivation_target() -> DerivationTarget:
    """Define what counts as deriving the O(3) sector.

    A genuine derivation must satisfy all 6 criteria in DERIVATION_CRITERIA.
    Anything less is partial motivation, not derivation.
    """
    return DerivationTarget(
        criteria=list(DERIVATION_CRITERIA),
        description=(
            "A true derivation of the O(3) sector from GRUT-native geometry must "
            "demonstrate that the geometric structure of the GRUT interior necessarily "
            "produces: (1) an effective 3-component field structure, (2) with O(3)-like "
            "organization or effective equivalent, (3) that activates specifically in "
            "the strong-curvature regime, (4) generates a 1/r^2 support class matching "
            "Component B, (5) fixes or constrains the coefficient eta^2 = 1/(8*pi), and "
            "(6) is consistent with the D12 topological winding ontology Q = n*eta. "
            "Failure on any criterion means the construction is at most partial motivation, "
            "not derivation."
        ),
    )


# ===================================================================
# Candidate Constructions
# ===================================================================

def build_candidate_constructions() -> List[CandidateConstruction]:
    """Build and evaluate all candidate geometric constructions.

    Three pathways, each with specific constructions.
    Evaluations are explicit and conservative.
    """
    constructions = []

    # ---------------------------------------------------------------
    # PATHWAY 1: Tetrad / Geometric Induction
    # ---------------------------------------------------------------

    # Construction 1A: Spatial frame projection of scalar field
    constructions.append(CandidateConstruction(
        name="Spatial frame projection Phi_a = Phi * e^i_a",
        pathway="tetrad_geometric",
        ingredients=[
            "scalar memory field Phi(r)",
            "spatial orthonormal triad e^i_a (i=1,2,3)",
            "Schwarzschild spatial metric",
        ],
        construction_description=(
            "Construct a triplet-like object by projecting the scalar Phi onto "
            "the spatial orthonormal frame: Phi_a(r) = Phi(r) * e^r_a, where e^r_a "
            "is the radial leg of the spatial triad. In spherical symmetry the triad "
            "is e^r = dr-hat, e^theta = d-theta-hat, e^phi = d-phi-hat. The projection "
            "Phi(r) * e^r_a yields a single radial component, not a genuine triplet. "
            "One could define Phi_a = Phi(r) * x_hat_a (unit radial vector in Cartesian "
            "embedding), but this smuggles in the Cartesian embedding structure -- the "
            "x_hat_a are defined in R^3, not intrinsically on the Schwarzschild manifold."
        ),
        symmetry_status="SO(3) of spatial rotations, not internal O(3)",
        grut_native=True,
        support_class_outcome=(
            "Phi ~ M/r^2 gives eps ~ Phi^2/tau^2 ~ 1/r^4, not 1/r^2. The spatial "
            "frame projection does not change the radial falloff of the scalar. "
            "Component B requires angular gradient energy ~ f^2/r^2, which the scalar "
            "frame projection does not produce because the scalar has no angular variation."
        ),
        coefficient_outcome="No constraint on eta; eta does not appear",
        strong_field_activation=(
            "The triad exists everywhere, not just in strong-field region. "
            "No curvature-triggered activation mechanism."
        ),
        hedgehog_emergence=(
            "The unit radial vector x_hat_a has hedgehog topology pi_2(S^2) = Z, "
            "but this is a property of the R^3 embedding, not of the metric or the "
            "scalar field. Calling Phi(r)*x_hat_a a hedgehog conflates a coordinate "
            "artifact with a dynamical field configuration."
        ),
        verdict="fails",
        reasoning=(
            "Spatial frame projection of the scalar does not produce a genuine "
            "internal-triplet structure. The 3 components come from the spatial "
            "embedding (R^3 Cartesian), not from the field dynamics. The construction "
            "fails on support class (still 1/r^4) and on hedgehog dynamics (no angular "
            "gradient energy). It also fails on strong-field activation (triad is global)."
        ),
    ))

    # Construction 1B: Curvature-weighted radial composite
    constructions.append(CandidateConstruction(
        name="Curvature-weighted composite Psi_a = sqrt(K) * Phi * x_hat_a",
        pathway="tetrad_geometric",
        ingredients=[
            "scalar memory field Phi(r)",
            "Kretschner scalar K(r) = 48*M^2/r^6",
            "unit radial vector x_hat_a",
        ],
        construction_description=(
            "Weight the spatial frame projection by the curvature invariant: "
            "Psi_a(r) = sqrt(K(r)) * Phi(r) * x_hat_a. With K = 48*M^2/r^6 and "
            "Phi ~ M/r^2, this gives Psi_a ~ M^2/r^5 * x_hat_a. The stress-energy "
            "would scale as Psi^2 ~ 1/r^10, far steeper than the required 1/r^2."
        ),
        symmetry_status="SO(3) spatial rotation symmetry; Cartesian embedding required",
        grut_native=True,
        support_class_outcome=(
            "eps ~ Psi^2 ~ M^4/r^10. This is drastically steeper than 1/r^2. "
            "The curvature weighting makes the radial falloff worse, not better."
        ),
        coefficient_outcome="No constraint on eta; wrong radial scaling entirely",
        strong_field_activation=(
            "K(r) ~ 1/r^6 grows inward, providing implicit curvature weighting. "
            "But this is just algebraic multiplication, not a dynamical activation."
        ),
        hedgehog_emergence="Same x_hat_a embedding issue as Construction 1A",
        verdict="fails",
        reasoning=(
            "Curvature weighting of the scalar-frame projection makes the radial "
            "falloff steeper (1/r^10), further from the required 1/r^2. This "
            "construction fails on the most basic requirement."
        ),
    ))

    # Construction 1C: Tidal tensor eigenvectors as internal frame
    constructions.append(CandidateConstruction(
        name="Tidal eigenvector triplet from E_ab decomposition",
        pathway="tetrad_geometric",
        ingredients=[
            "electric part of Weyl tensor E_ab = C_0a0b u^0 u^b",
            "spatial metric h_ab",
            "scalar field Phi(r)",
        ],
        construction_description=(
            "The electric part of the Weyl tensor E_ab is a symmetric trace-free "
            "spatial tensor with 3 eigenvalues in 3 spatial dimensions. In spherical "
            "symmetry, E_ab = diag(E_r, E_theta, E_phi) with E_r = -2M/r^3 and "
            "E_theta = E_phi = M/r^3 (for Schwarzschild). The three eigenvectors "
            "define a spatial frame. However, in spherical symmetry this frame is "
            "just the coordinate frame -- it carries no new information. The "
            "eigenvalues are not independent (E_r + E_theta + E_phi = 0, trace-free). "
            "One could define Phi_a = Phi * lambda_a where lambda_a are eigenvalues, "
            "but in spherical symmetry lambda = (-2M/r^3, M/r^3, M/r^3) which gives "
            "a 1+2 decomposition, not a genuine O(3) triplet. The two degenerate "
            "eigenvalues break the construction to SO(2), not SO(3)."
        ),
        symmetry_status="SO(2) axial around radial direction; NOT O(3)",
        grut_native=True,
        support_class_outcome=(
            "Even if we define Phi_a from eigenvalues: Phi*lambda_a ~ M^2/(r^2 * r^3) = "
            "M^2/r^5. Energy ~ 1/r^10. Fails."
        ),
        coefficient_outcome="No eta constraint; wrong structure",
        strong_field_activation=(
            "E_ab grows as 1/r^3 inward -- curvature-dependent. But the tidal tensor "
            "exists everywhere, including in the weak-field region."
        ),
        hedgehog_emergence=(
            "Fails. In spherical symmetry E_ab has 1+2 eigenvalue structure (radial "
            "vs tangential), not the 3-fold degeneracy needed for O(3). There is no "
            "mechanism to produce hedgehog topology from tidal eigenvectors."
        ),
        verdict="fails",
        reasoning=(
            "The tidal tensor eigenvector construction in spherical symmetry has "
            "SO(2) symmetry (1 radial + 2 degenerate tangential), not O(3). It "
            "cannot produce a genuine O(3) triplet or hedgehog configuration. "
            "The support class is also wrong (~1/r^10)."
        ),
    ))

    # Construction 1D: Self-dual Weyl components as triplet
    constructions.append(CandidateConstruction(
        name="Self-dual Weyl tensor components as O(3) triplet",
        pathway="tetrad_geometric",
        ingredients=[
            "Weyl tensor C_abcd",
            "self-dual decomposition C^+ = (C + *C)/2",
            "spatial duality operation",
        ],
        construction_description=(
            "The Weyl tensor in 4D has 10 independent components. Under the spatial "
            "duality decomposition it splits into self-dual C^+_abcd and anti-self-dual "
            "C^-_abcd, each with 5 real components (or 5 complex = 10 real total). "
            "Alternatively, the Weyl tensor maps to the symmetric trace-free matrices "
            "E_ab and B_ab (electric and magnetic parts, 5+5 = 10 DOF). In vacuum "
            "Schwarzschild: B_ab = 0 (static, purely electric). The 5 components of "
            "E_ab in spherical symmetry reduce to 1 independent function (E_r, with "
            "E_theta = E_phi = -E_r/2 by trace-freeness). This does not give 3 "
            "independent components for an O(3) triplet. The self-dual decomposition "
            "of C_abcd gives complex 3x3 symmetric traceless matrices (Petrov "
            "classification), but in Schwarzschild (Type D) this has only 1 complex "
            "DOF (the Weyl scalar Psi_2). There is no mechanism to extract 3 "
            "independent real components matching an O(3) triplet."
        ),
        symmetry_status="Petrov Type D: single complex DOF Psi_2; not O(3)",
        grut_native=True,
        support_class_outcome="Only 1 DOF in spherical symmetry; cannot produce triplet",
        coefficient_outcome="No constraint possible; wrong DOF count",
        strong_field_activation="Psi_2 ~ M/r^3 grows inward; curvature-dependent",
        hedgehog_emergence=(
            "Impossible. In Petrov Type D, the Weyl tensor has no 3-fold internal "
            "structure. The O(3) triplet requires 3 independent DOF with O(3) "
            "transformation properties; the Weyl tensor in spherical symmetry has 1."
        ),
        verdict="fails",
        reasoning=(
            "The self-dual Weyl decomposition in spherically symmetric spacetime "
            "(Petrov Type D) has only 1 complex degree of freedom (Psi_2), not 3. "
            "There is no way to extract an O(3) triplet from the Weyl tensor in "
            "this symmetry class. The construction is mathematically blocked."
        ),
    ))

    # Construction 1E: Tangent bundle of 2-spheres at each radius
    constructions.append(CandidateConstruction(
        name="Tangent bundle of S^2 fibers: T(S^2_r) as O(3) frame",
        pathway="tetrad_geometric",
        ingredients=[
            "foliation of spatial sections by 2-spheres S^2_r at each r",
            "tangent bundle T(S^2_r) with structure group SO(2)",
            "normal bundle N(S^2_r) in the 3-space",
            "scalar field Phi(r)",
        ],
        construction_description=(
            "At each radius r, the spatial 3-geometry foliates into 2-spheres S^2_r "
            "with normal direction dr. The tangent bundle of S^2_r has structure "
            "group SO(2) (rotations within the sphere). Together with the normal "
            "direction, this gives a 3-frame at each point: (n_r, e_theta, e_phi). "
            "The structure group of the normal + tangent frame is SO(1) x SO(2) = SO(2), "
            "not SO(3). The full spatial tangent bundle has structure group SO(3) "
            "(frame rotations in 3D), which IS the rotation group. However, the "
            "foliating 2-spheres select a preferred direction (radial), reducing "
            "SO(3) to SO(2). To get an O(3) triplet, one would need the full "
            "unreduced SO(3) frame bundle, but spherical symmetry itself reduces it. "
            "Paradoxically, the O(3) symmetry of the hedgehog requires breaking "
            "the very SO(3) that the background geometry preserves. The hedgehog "
            "is equivariant under combined spatial + internal O(3), i.e., it breaks "
            "both and preserves the diagonal."
        ),
        symmetry_status=(
            "SO(3) spatial rotation is the isometry group. The hedgehog uses the "
            "diagonal subgroup of SO(3)_spatial x O(3)_internal. The spatial geometry "
            "provides SO(3)_spatial but NOT O(3)_internal independently."
        ),
        grut_native=True,
        support_class_outcome=(
            "The 2-sphere area element goes as r^2. Angular gradients on the "
            "2-sphere of a hedgehog configuration give energy ~ eta^2*f^2/r^2. "
            "This IS the correct 1/r^2 support class. However, the angular gradient "
            "energy comes from the defect field varying across the 2-sphere -- it "
            "requires the defect field to exist as an independent dynamical field, "
            "not just as a geometric composite of the scalar."
        ),
        coefficient_outcome=(
            "The area element of S^2_r is 4*pi*r^2. The angular gradient energy "
            "integrates to 4*pi*eta^2*f^2. The coefficient eta^2 is not determined "
            "by the geometry; it is the VEV of the defect field."
        ),
        strong_field_activation=(
            "The 2-sphere foliation exists everywhere, not just in strong-field. "
            "The construction does not explain curvature-triggered activation."
        ),
        hedgehog_emergence=(
            "The tangent bundle argument shows that the spatial geometry naturally "
            "supports maps from S^2_r to the field space with winding number "
            "(pi_2(S^2) = Z). This is the homotopy argument of D1. However, it "
            "does not force the scalar Phi(r) to 'split' into a hedgehog. The "
            "topology permits hedgehogs but does not require them without an "
            "independent O(3)-valued field."
        ),
        verdict="partially_motivated",
        reasoning=(
            "The 2-sphere foliation of the spatial geometry provides the topological "
            "substrate for hedgehog configurations (pi_2(S^2) = Z) and the angular "
            "gradient energy naturally produces the 1/r^2 support class. This "
            "strongly motivates WHY the O(3) hedgehog is well-adapted to the "
            "geometry. But it does not derive the O(3) field from the geometry: "
            "the scalar Phi(r) is rotationally invariant and cannot develop angular "
            "structure without an independent internal DOF. The spatial O(3) provides "
            "the geometric context but not the dynamical field content."
        ),
    ))

    # ---------------------------------------------------------------
    # PATHWAY 2: Memory-Kernel Tensorization
    # ---------------------------------------------------------------

    # Construction 2A: Rank-2 memory tensor decomposition
    constructions.append(CandidateConstruction(
        name="Rank-2 memory tensor Phi_ab -> trace + vector + tensor",
        pathway="memory_tensorization",
        ingredients=[
            "rank-2 symmetric memory tensor Phi_ab",
            "SO(3) spatial symmetry reduction",
            "irreducible decomposition under SO(3)",
        ],
        construction_description=(
            "The existing tensorial memory framework (tensorial_memory.py) already "
            "establishes that the scalar Phi is the isotropic limit of a rank-2 "
            "symmetric tensor Phi_ab. Under SO(3) decomposition: "
            "Phi_ab = (1/3)*Phi*g_ab + sigma_ab + symmetrized(v_(a)*n_b)). "
            "The trace Phi (1 DOF) is the existing scalar. The trace-free symmetric "
            "part sigma_ab has 5 DOF in general, but under SO(3) symmetry of the "
            "Schwarzschild background, it reduces to at most 2 independent components "
            "(1 radial + 1 tangential, by spherical symmetry). The vector part v_a "
            "has 3 DOF in general, but under SO(3) symmetry it reduces to 1 component "
            "(radial only). Total in spherical symmetry: 1 (trace) + 2 (sigma) + 1 (v) "
            "= 4 DOF, not the 3 needed for O(3). Moreover, the sigma_ab components "
            "transform as scalars under SO(3) (they are the eigenvalues), not as a "
            "vector/triplet. The vector v_a in spherical symmetry is purely radial. "
            "Neither sigma_ab nor v_a produces an O(3) triplet in spherical symmetry."
        ),
        symmetry_status=(
            "SO(3) reduction of rank-2 tensor: irreps are 0 + 1 + 2 (spin-0, spin-1, spin-2). "
            "The spin-1 part (v_a, 3 DOF) transforms as an SO(3) triplet in general. "
            "But in spherically symmetric backgrounds, SO(3) symmetry forces v_a to "
            "be purely radial (1 DOF), killing the triplet structure."
        ),
        grut_native=True,
        support_class_outcome=(
            "In general (non-spherically-symmetric perturbations), the spin-1 sector "
            "v_a could carry angular momentum and produce angular gradients. But this "
            "requires breaking spherical symmetry, which is not the current GRUT setup."
        ),
        coefficient_outcome=(
            "No constraint on eta. The tensor decomposition does not fix the VEV "
            "of any component."
        ),
        strong_field_activation=(
            "The tensor decomposition exists for any background. There is no "
            "curvature-dependent mechanism that activates the spin-1 sector "
            "preferentially in strong-field regions."
        ),
        hedgehog_emergence=(
            "In general 3D (no spherical symmetry): the spin-1 part v_a transforms "
            "as an SO(3) vector and could in principle support a hedgehog configuration "
            "v_a = v(r)*x_hat_a. But this requires breaking the background SO(3) "
            "symmetry, which means the hedgehog must be a spontaneous symmetry-breaking "
            "configuration of the tensor field -- i.e., the O(3) structure appears "
            "through SSB of the memory tensor, not through geometric induction."
        ),
        verdict="partially_motivated",
        reasoning=(
            "The rank-2 memory tensor contains a spin-1 (vector) sector that "
            "transforms as an SO(3) triplet. This provides a GRUT-native field "
            "content that could, in principle, support an O(3)-valued hedgehog. "
            "However, in the spherically symmetric background, the spin-1 sector "
            "is frozen to a single radial DOF. To produce a hedgehog, one must "
            "consider perturbations that break spherical symmetry -- i.e., the "
            "hedgehog would be an SSB configuration of the memory tensor, not a "
            "geometric consequence of the background. This is partially motivating "
            "but does not constitute derivation."
        ),
    ))

    # Construction 2B: Curvature-induced anisotropy lifting
    constructions.append(CandidateConstruction(
        name="Curvature-induced anisotropy: tidal tensor lifts sigma_ab",
        pathway="memory_tensorization",
        ingredients=[
            "rank-2 memory tensor Phi_ab",
            "tidal tensor E_ab",
            "coupling term E_ab * Phi^ab in action",
        ],
        construction_description=(
            "Add a coupling E_ab * Phi^ab to the memory tensor action, where "
            "E_ab is the electric part of the Weyl/Riemann tensor. This couples "
            "the anisotropic part of the memory tensor to the tidal field. In "
            "Schwarzschild: E_ab = diag(-2M/r^3, M/r^3, M/r^3) in the spatial "
            "orthonormal frame. The coupling E_ab*sigma^ab sources the trace-free "
            "memory components. In spherical symmetry this gives: "
            "E_r*sigma_r + 2*E_theta*sigma_theta, which is a scalar combination "
            "(1 DOF), not a triplet. The tidal-memory coupling in spherical symmetry "
            "activates the anisotropic memory sector but keeps it at 2 independent "
            "components (radial + tangential), not 3."
        ),
        symmetry_status="Still SO(2) in spherical symmetry; tidal field is 1+2 decomposed",
        grut_native=True,
        support_class_outcome=(
            "The tidal sourcing sigma ~ E/m^2_eff ~ M/(r^3 * m^2_eff). If m_eff ~ 1/tau, "
            "then sigma ~ M*tau^2/r^3. Energy ~ sigma^2 ~ 1/r^6. Wrong scaling."
        ),
        coefficient_outcome="No eta constraint; wrong scaling",
        strong_field_activation=(
            "Yes: E_ab ~ 1/r^3 grows in strong field. The anisotropic memory sector "
            "is preferentially sourced in the strong-curvature region."
        ),
        hedgehog_emergence="Cannot produce hedgehog in spherical symmetry (2 DOF, not 3)",
        verdict="suggestive_only",
        reasoning=(
            "Tidal-memory coupling provides a geometrically natural mechanism for "
            "strong-field activation of anisotropic memory components. However, "
            "in spherical symmetry it produces only 2 independent components (not 3), "
            "and the stress-energy scaling is wrong (~1/r^6 not ~1/r^2). The "
            "construction is suggestive of how curvature could activate extended "
            "memory structure, but it does not derive the O(3) sector."
        ),
    ))

    # Construction 2C: Memory tensor SSB in non-spherical perturbation
    constructions.append(CandidateConstruction(
        name="Memory tensor SSB: spin-1 sector hedgehog as instability",
        pathway="memory_tensorization",
        ingredients=[
            "rank-2 memory tensor Phi_ab with spin-1 sector v_a",
            "Mexican-hat-type potential for |v|^2",
            "curvature-dependent effective mass for v_a",
        ],
        construction_description=(
            "If the memory tensor action includes a potential V(Phi_ab) that "
            "admits a vacuum manifold with non-zero v_a, and if the effective "
            "mass m^2_v of the spin-1 sector becomes negative in strong-curvature "
            "regions (m^2_v = m^2_0 - xi_v * K), then the spin-1 sector would "
            "undergo curvature-triggered SSB producing a hedgehog v_a = v_0(r)*x_hat_a. "
            "This would be GRUT-native (memory tensor is already in the theory) and "
            "curvature-triggered. The resulting energy would be "
            "eps ~ v_0^2/r^2 (angular gradient) = eta_v^2 * f^2/r^2 if v_0(r) = "
            "eta_v * f(r). This matches the 1/r^2 support class. "
            "HOWEVER: (a) the potential V(Phi_ab) must be specified -- it is not "
            "currently in the GRUT action; (b) the spin-1 sector stability analysis "
            "has not been done; (c) identifying v_a with vec_Phi^a is an additional "
            "assumption; (d) the coefficient eta_v^2 = 1/(8*pi) must be imposed, not "
            "predicted. This construction is structurally promising but requires "
            "extending the GRUT action with a tensor memory potential."
        ),
        symmetry_status=(
            "O(3) internal from spin-1 sector of Phi_ab; background SO(3) broken "
            "to diagonal by hedgehog"
        ),
        grut_native=True,  # memory tensor exists in theory; potential is an extension
        support_class_outcome=(
            "Correct: angular gradient of hedgehog gives eta_v^2*f^2/r^2 = Component B. "
            "This matches if eta_v = eta."
        ),
        coefficient_outcome=(
            "eta_v must be imposed to match eta^2 = 1/(8*pi). The tensor "
            "decomposition does not predict this value."
        ),
        strong_field_activation=(
            "Yes, if effective mass m^2_v = m^2_0 - xi_v*K becomes negative "
            "in strong-field. This is the same curvature-trigger mechanism as D10."
        ),
        hedgehog_emergence=(
            "Yes, the spin-1 sector v_a with negative m^2_v would spontaneously "
            "form a hedgehog configuration by the same homotopy argument as D1."
        ),
        verdict="partially_motivated",
        reasoning=(
            "This is the most promising construction tested. The spin-1 sector of "
            "the rank-2 memory tensor provides GRUT-native O(3)-valued field content. "
            "Curvature-triggered SSB of this sector would naturally produce hedgehog "
            "configurations with the correct 1/r^2 support class. However, the "
            "construction requires: (a) a tensor potential not in the current action, "
            "(b) stability analysis confirming spin-1 instability, (c) eta_v = eta "
            "imposed not predicted. It is partially motivated because the field "
            "content exists natively but the dynamics are not yet derived."
        ),
    ))

    # ---------------------------------------------------------------
    # PATHWAY 3: UV-completion / Hidden Multiplet
    # ---------------------------------------------------------------

    # Construction 3A: Scalar as radial mode of fundamental triplet
    constructions.append(CandidateConstruction(
        name="Scalar Phi as radial modulus of UV-complete O(3) multiplet",
        pathway="uv_completion",
        ingredients=[
            "hypothetical UV-complete O(3) multiplet Phi^a",
            "identification Phi = |Phi^a| (radial mode)",
            "angular modes as Goldstone bosons",
        ],
        construction_description=(
            "Postulate that the scalar memory field Phi is the radial mode of a "
            "more fundamental O(3) triplet: Phi = |vec_Phi|, with the angular "
            "Goldstone modes corresponding to the hedgehog configuration. At low "
            "energies in the symmetric phase, only the radial mode Phi is visible "
            "(cosmology, weak-field). In strong-field regions, the full triplet "
            "is revealed through SSB. This is the D3 'embedding' architecture. "
            "It provides the correct structure but introduces the O(3) triplet "
            "at the fundamental level -- it does not derive it from the scalar."
        ),
        symmetry_status="O(3) fundamental; not derived from geometry",
        grut_native=False,  # introduces O(3) at UV level
        support_class_outcome="Correct by construction (hedgehog reproduces Component B)",
        coefficient_outcome="eta must still be imposed",
        strong_field_activation=(
            "SSB mechanism provides activation, but O(3) is assumed, not derived"
        ),
        hedgehog_emergence="By construction",
        verdict="suggestive_only",
        reasoning=(
            "UV-completion with a fundamental O(3) triplet trivially recovers "
            "the defect sector but does not derive it from geometry. It replaces "
            "the question 'why O(3)?' with 'why is the UV theory O(3)?'. No "
            "explanatory gain for the foundational question."
        ),
    ))

    # Construction 3B: Scalar condensate from higher-spin sector
    constructions.append(CandidateConstruction(
        name="O(3) triplet as composite of higher-spin memory excitations",
        pathway="uv_completion",
        ingredients=[
            "hypothetical higher-spin spectrum in memory sector",
            "spin-1 bound state or condensate",
            "confinement/condensation mechanism",
        ],
        construction_description=(
            "If the GRUT memory sector has UV degrees of freedom beyond the "
            "scalar, a spin-1 bound state could form in the strong-field regime. "
            "This is analogous to Cooper pairing or chiral symmetry breaking "
            "in QCD. However: (a) there is no evidence for a UV-complete memory "
            "sector with higher-spin excitations; (b) the bound-state mechanism "
            "requires specifying the UV theory; (c) this is speculative beyond "
            "the current GRUT framework."
        ),
        symmetry_status="Would depend on UV theory; currently unspecified",
        grut_native=False,
        support_class_outcome="Unknown; depends on UV dynamics",
        coefficient_outcome="Unknown",
        strong_field_activation="Possible via confinement; speculative",
        hedgehog_emergence="Unknown; would require dynamical calculation",
        verdict="suggestive_only",
        reasoning=(
            "Pure speculation. No UV-complete memory sector exists in GRUT. "
            "The construction cannot be evaluated without specifying the UV "
            "theory, which would itself require new physics."
        ),
    ))

    return constructions


# ===================================================================
# Pathway Assessments
# ===================================================================

def assess_pathways(
    constructions: List[CandidateConstruction],
) -> List[PathwayAssessment]:
    """Assess each derivation pathway based on its constructions."""

    # Group constructions by pathway
    tetrad = [c for c in constructions if c.pathway == "tetrad_geometric"]
    memory = [c for c in constructions if c.pathway == "memory_tensorization"]
    uv = [c for c in constructions if c.pathway == "uv_completion"]

    assessments = []

    # Pathway 1: Tetrad / Geometric Induction
    tetrad_verdicts = [c.verdict for c in tetrad]
    best_tetrad = "partially_motivated" if "partially_motivated" in tetrad_verdicts else "fails"
    assessments.append(PathwayAssessment(
        pathway="tetrad_geometric",
        native_to_grut=True,
        mathematical_discipline="semi_rigorous",
        support_class_success=False,  # no construction achieves 1/r^2 from geometry alone
        coefficient_constraint=False,
        ontology_continuity=False,
        strong_field_necessity=False,
        constructions=tetrad,
        verdict="partially_motivated",
        summary=(
            "The spatial geometry (2-sphere foliation, SO(3) frame bundle) provides "
            "the topological substrate for hedgehog configurations and the angular "
            "gradient mechanism that produces the 1/r^2 support class. This strongly "
            "motivates why the O(3) hedgehog is geometrically natural. However, no "
            "tetrad/frame construction succeeds in deriving the O(3) field content "
            "from the scalar memory field and the metric alone. The fundamental "
            "obstruction is that the scalar Phi(r) is spherically symmetric and "
            "cannot develop angular structure without independent internal DOF. "
            "The spatial SO(3) provides the geometric context but not the dynamical "
            "field content."
        ),
    ))

    # Pathway 2: Memory-Kernel Tensorization
    memory_verdicts = [c.verdict for c in memory]
    assessments.append(PathwayAssessment(
        pathway="memory_tensorization",
        native_to_grut=True,
        mathematical_discipline="semi_rigorous",
        support_class_success=True,  # Construction 2C achieves 1/r^2 via hedgehog SSB
        coefficient_constraint=False,  # eta must be imposed
        ontology_continuity=True,  # spin-1 sector naturally produces winding
        strong_field_necessity=True,  # curvature-triggered SSB mechanism
        constructions=memory,
        verdict="partially_motivated",
        summary=(
            "The memory-kernel tensorization pathway is the most promising. The "
            "existing tensorial memory framework establishes that Phi is the "
            "isotropic limit of a rank-2 tensor Phi_ab. The spin-1 sector of this "
            "tensor (v_a, 3 DOF) transforms as an SO(3) triplet and could, under "
            "curvature-triggered SSB, produce a hedgehog with the correct 1/r^2 "
            "support class. The construction is GRUT-native in field content but "
            "requires: (a) a tensor potential not in the current action, (b) stability "
            "analysis, (c) eta imposed not predicted. It upgrades the O(3) sector "
            "from 'external extension' to 'partially motivated by GRUT-native tensor "
            "structure' but does not achieve full derivation."
        ),
    ))

    # Pathway 3: UV-completion
    assessments.append(PathwayAssessment(
        pathway="uv_completion",
        native_to_grut=False,
        mathematical_discipline="speculative",
        support_class_success=False,  # trivially by assumption, not by derivation
        coefficient_constraint=False,
        ontology_continuity=False,
        strong_field_necessity=False,
        constructions=uv,
        verdict="suggestive_only",
        summary=(
            "UV-completion pathways either smuggle in the O(3) sector at a "
            "fundamental level (not deriving it) or require specifying a UV "
            "theory that does not yet exist. Neither construction provides "
            "explanatory gain for the foundational question."
        ),
    ))

    return assessments


# ===================================================================
# Requirement Matching
# ===================================================================

def build_requirement_matching(
    pathway_assessments: List[PathwayAssessment],
) -> RequirementMatchingTable:
    """Build the requirement-matching table across all pathways."""

    entries = [
        RequirementMatchEntry(
            requirement="REQ_6C_SHAPE: Component B ~ 1/r^2",
            tetrad_induction="partial",
            tensorized_memory="strong",
            uv_completion="not_applicable",
            comments=(
                "Tetrad: 2-sphere foliation explains WHY 1/r^2 from angular gradients, "
                "but cannot produce the field. Memory tensor: spin-1 hedgehog SSB gives "
                "exact 1/r^2. UV: trivially by assumption."
            ),
        ),
        RequirementMatchEntry(
            requirement="REQ_6C_COEFF: eta^2 = 1/(8*pi)",
            tetrad_induction="none",
            tensorized_memory="none",
            uv_completion="none",
            comments=(
                "No pathway predicts eta. The coefficient must still be matched to "
                "Phase 6C. This is a persistent gap across all pathways."
            ),
        ),
        RequirementMatchEntry(
            requirement="REQ_ROUTEBC: GRUT-native origin",
            tetrad_induction="partial",
            tensorized_memory="partial",
            uv_completion="none",
            comments=(
                "Tetrad: geometry motivates hedgehog but does not produce field. "
                "Memory tensor: field content is GRUT-native; dynamics require extension. "
                "UV: introduces new physics."
            ),
        ),
        RequirementMatchEntry(
            requirement="REQ_D1_HOMOTOPY: pi_2 != 0",
            tetrad_induction="strong",
            tensorized_memory="strong",
            uv_completion="strong",
            comments=(
                "All pathways that produce an O(3)-valued field inherit pi_2(S^2) = Z. "
                "Tetrad: spatial 2-spheres provide topological substrate. "
                "Memory tensor: spin-1 sector supports hedgehog. "
                "UV: by construction."
            ),
        ),
        RequirementMatchEntry(
            requirement="REQ_D11_VIABILITY: consistent with exact BVP",
            tetrad_induction="weak",
            tensorized_memory="partial",
            uv_completion="not_applicable",
            comments=(
                "Tetrad: no dynamical field to solve BVP with. "
                "Memory tensor: spin-1 hedgehog BVP would be structurally identical to "
                "D11, but this has not been solved. "
                "UV: not testable without UV theory."
            ),
        ),
        RequirementMatchEntry(
            requirement="REQ_D12_ONTOLOGY: Q = n*eta continuity",
            tetrad_induction="partial",
            tensorized_memory="strong",
            uv_completion="partial",
            comments=(
                "Tetrad: homotopy argument preserved but no dynamical Q. "
                "Memory tensor: Q = n*eta_v from spin-1 winding, continuous with D12. "
                "UV: Q = n*eta by construction."
            ),
        ),
    ]

    return RequirementMatchingTable(entries=entries)


# ===================================================================
# Derivation Criteria Assessment
# ===================================================================

def assess_derivation_criteria(
    pathway_assessments: List[PathwayAssessment],
) -> List[DerivationCriterionResult]:
    """Assess each derivation criterion across all pathways."""

    results = [
        DerivationCriterionResult(
            criterion="three_component_structure",
            tetrad_result="fails: spatial frame gives 3 components from embedding, not from dynamics",
            memory_result="partial: spin-1 sector of Phi_ab provides 3 DOF natively",
            uv_result="assumed: O(3) triplet postulated",
            best_pathway="memory_tensorization",
            notes=(
                "Only the memory tensor pathway provides a GRUT-native 3-component "
                "structure without introducing it by hand or relying on coordinate "
                "embedding."
            ),
        ),
        DerivationCriterionResult(
            criterion="o3_organization",
            tetrad_result="fails: spatial SO(3) is isometry group, not internal symmetry",
            memory_result="partial: spin-1 sector transforms as SO(3) vector; would need SSB potential",
            uv_result="assumed",
            best_pathway="memory_tensorization",
            notes=(
                "The memory tensor spin-1 sector automatically transforms as an "
                "SO(3) vector under spatial rotations. This is not an internal O(3) "
                "symmetry, but under the hedgehog ansatz the spatial and internal "
                "transformations lock together (diagonal subgroup). The distinction "
                "between spatial SO(3) and internal O(3) becomes moot for the hedgehog."
            ),
        ),
        DerivationCriterionResult(
            criterion="strong_curvature_activation",
            tetrad_result="fails: no curvature-dependent activation mechanism",
            memory_result="partial: curvature-triggered SSB of spin-1 sector, same mechanism as D10",
            uv_result="speculative: possible via confinement",
            best_pathway="memory_tensorization",
            notes=(
                "The curvature-triggered SSB mechanism (m^2_v = m^2_0 - xi_v*K) "
                "is natural and mirrors the D10 Kretschner trigger."
            ),
        ),
        DerivationCriterionResult(
            criterion="support_class_1_over_r2",
            tetrad_result="partial: explains WHY from geometry; cannot produce the field",
            memory_result="strong: hedgehog of spin-1 gives eta_v^2*f^2/r^2 exactly",
            uv_result="assumed",
            best_pathway="memory_tensorization",
            notes=(
                "Memory tensor pathway achieves the correct support class through "
                "the same hedgehog mechanism as D1-D2, but with GRUT-native field content."
            ),
        ),
        DerivationCriterionResult(
            criterion="coefficient_constraint",
            tetrad_result="none",
            memory_result="none: eta_v must be imposed, not predicted",
            uv_result="none",
            best_pathway="none",
            notes=(
                "No pathway predicts eta^2 = 1/(8*pi). This coefficient remains "
                "a matching condition from Phase 6C. This is the hardest remaining "
                "gap across all pathways."
            ),
        ),
        DerivationCriterionResult(
            criterion="charge_ontology_alignment",
            tetrad_result="partial: homotopy preserved from spatial 2-spheres",
            memory_result="strong: Q = n*eta_v from spin-1 winding, continuous with D12",
            uv_result="assumed",
            best_pathway="memory_tensorization",
            notes=(
                "The memory tensor pathway produces charge ontology Q = n*eta_v "
                "that is structurally identical to D12's Q = n*eta."
            ),
        ),
    ]

    return results


# ===================================================================
# Classification
# ===================================================================

def classify_geometric_induction(
    pathway_assessments: List[PathwayAssessment],
    derivation_criteria: List[DerivationCriterionResult],
    requirement_matching: RequirementMatchingTable,
) -> D13Classification:
    """Classify the D13 result from explicit criteria.

    Classification logic (deterministic, no hidden weights):

    1. Count how many derivation criteria are met by the best pathway
       - "strong" or "derived" = met
       - "partial" = half credit
       - "none", "fails", "assumed" = not met

    2. Count how many requirements are matched at "strong" level
       by the best pathway

    3. Apply threshold rules:
       - 6/6 criteria strong + 6/6 requirements strong = canonically_derived
       - >= 4/6 criteria strong + >= 4/6 requirements strong = effectively_induced
       - >= 3/6 criteria partial or better + >= 3/6 requirements partial = partially_motivated
       - < 3/6 on either = principled_extension_still_required
       - best pathway verdict = "fails" or "unsupported" = derivation_attempt_failed
    """

    # Find best pathway (tie-break by support_class_success, then strong_field_necessity)
    pathway_order = {
        "derived": 5, "strongly_supported": 4, "partially_motivated": 3,
        "suggestive_only": 2, "unsupported": 1, "overextended": 0,
    }
    best = max(
        pathway_assessments,
        key=lambda p: (
            pathway_order.get(p.verdict, 0),
            int(p.support_class_success),
            int(p.ontology_continuity),
            int(p.strong_field_necessity),
        ),
    )
    best_pathway = best.pathway

    # Count criteria met by best pathway
    criteria_strong = 0
    criteria_partial = 0
    for dc in derivation_criteria:
        if best_pathway == "tetrad_geometric":
            result = dc.tetrad_result
        elif best_pathway == "memory_tensorization":
            result = dc.memory_result
        else:
            result = dc.uv_result

        if result.startswith("strong") or result.startswith("derived"):
            criteria_strong += 1
        elif result.startswith("partial"):
            criteria_partial += 1

    criteria_effective = criteria_strong + 0.5 * criteria_partial
    criteria_total = len(derivation_criteria)

    # Count requirements matched at "strong" by best pathway
    req_strong = 0
    req_partial = 0
    for entry in requirement_matching.entries:
        if best_pathway == "tetrad_geometric":
            level = entry.tetrad_induction
        elif best_pathway == "memory_tensorization":
            level = entry.tensorized_memory
        else:
            level = entry.uv_completion

        if level == "strong":
            req_strong += 1
        elif level == "partial":
            req_partial += 1

    req_total = len(requirement_matching.entries)

    # Threshold classification
    if best.verdict in ("fails", "unsupported"):
        classification = "derivation_attempt_failed"
    elif criteria_strong >= 5 and req_strong >= 5:
        classification = "canonically_derived_from_geometry"
    elif criteria_strong >= 4 and req_strong >= 4:
        classification = "effectively_induced_but_not_fundamental"
    elif criteria_effective >= 3.0 and (req_strong + req_partial) >= 3:
        classification = "partially_motivated_not_derived"
    else:
        classification = "principled_extension_still_required"

    justification = (
        f"Best pathway: {best_pathway}. "
        f"Derivation criteria: {criteria_strong} strong, {criteria_partial} partial "
        f"out of {criteria_total} ({criteria_effective:.1f} effective). "
        f"Requirements: {req_strong} strong, {req_partial} partial out of {req_total}. "
        f"The memory-kernel tensorization pathway provides GRUT-native O(3)-valued "
        f"field content (spin-1 sector of rank-2 memory tensor) that could undergo "
        f"curvature-triggered SSB to produce a hedgehog with the correct 1/r^2 "
        f"support class. However, the construction requires a tensor potential "
        f"not in the current action, the coefficient eta^2 = 1/(8*pi) must still "
        f"be imposed, and the stability analysis has not been performed. The O(3) "
        f"sector is partially motivated by GRUT-native structure but not derived."
    )

    return D13Classification(
        classification=classification,
        best_pathway=best_pathway,
        justification=justification,
        derivation_criteria_met=criteria_strong,
        derivation_criteria_total=criteria_total,
        requirements_strong=req_strong,
        requirements_total=req_total,
    )


# ===================================================================
# Remaining Gaps
# ===================================================================

def identify_remaining_gaps(
    classification: D13Classification,
) -> List[FoundationalGap]:
    """Identify remaining foundational gaps after D13."""

    gaps = [
        FoundationalGap(
            gap="Tensor memory potential V(Phi_ab) not specified",
            severity="critical",
            notes=(
                "The most promising pathway (memory-kernel tensorization) requires "
                "a potential for the rank-2 tensor Phi_ab that admits spin-1 SSB. "
                "This potential is not in the current GRUT action. Specifying it "
                "would be a non-trivial extension."
            ),
        ),
        FoundationalGap(
            gap="Spin-1 sector stability analysis not performed",
            severity="critical",
            notes=(
                "The curvature-triggered SSB of the spin-1 sector requires "
                "demonstrating that m^2_v < 0 in strong-field regions. This "
                "stability analysis has not been done."
            ),
        ),
        FoundationalGap(
            gap="Coefficient eta^2 = 1/(8*pi) not predicted by any pathway",
            severity="significant",
            notes=(
                "No D13 pathway predicts the defect VEV. The coefficient remains "
                "a matching condition from Phase 6C across all pathways."
            ),
        ),
        FoundationalGap(
            gap="Spatial SO(3) vs internal O(3) distinction",
            severity="significant",
            notes=(
                "The memory tensor spin-1 sector transforms under spatial SO(3). "
                "The hedgehog locks spatial and internal transformations together. "
                "Whether this constitutes a genuine internal O(3) or just spatial "
                "SO(3) acting on a vector field remains a foundational question."
            ),
        ),
        FoundationalGap(
            gap="Empirical confrontation still absent",
            severity="critical",
            notes="Inherited from bridge document. No GRUT prediction has been tested."
        ),
    ]

    return gaps


# ===================================================================
# Main computation
# ===================================================================

NONCLAIMS = [
    "D13 does not claim to have derived the O(3) sector from GRUT-native geometry.",
    "D13 does not claim that spatial SO(3) is the same as internal O(3).",
    "D13 does not claim that the memory tensor potential V(Phi_ab) is specified.",
    "D13 does not claim that eta^2 = 1/(8*pi) is predicted by any pathway.",
    "D13 does not claim that the spin-1 instability has been demonstrated.",
    "D13 does not treat structural elegance or thematic analogy as derivation.",
    "D13 does not claim that the UV-completion pathway is viable without new physics.",
    "D13 does not conflate tetrad/spatial indices with internal symmetry indices.",
]


def compute_geometric_induction() -> D13Result:
    """Compute the full D13 result.

    This is the top-level entry point. Returns D13Result containing
    all sub-results, assessments, and the final classification.
    """
    target = define_derivation_target()
    constructions = build_candidate_constructions()
    pathways = assess_pathways(constructions)
    req_matching = build_requirement_matching(pathways)
    criteria_results = assess_derivation_criteria(pathways)
    classification = classify_geometric_induction(
        pathways, criteria_results, req_matching,
    )
    gaps = identify_remaining_gaps(classification)

    return D13Result(
        valid=True,
        derivation_target=target,
        constructions=constructions,
        pathway_assessments=pathways,
        requirement_matching=req_matching,
        derivation_criteria_results=criteria_results,
        classification=classification,
        remaining_gaps=gaps,
        nonclaims=list(NONCLAIMS),
    )


# ===================================================================
# Export
# ===================================================================

def d13_result_to_dict(result: D13Result) -> Dict[str, Any]:
    """Convert D13Result to a JSON-serializable dictionary."""
    return asdict(result)


def export_d13_result_json(result: D13Result, path: str) -> None:
    """Export D13Result to a JSON file."""
    d = d13_result_to_dict(result)
    with open(path, "w") as f:
        json.dump(d, f, indent=2, default=str)
