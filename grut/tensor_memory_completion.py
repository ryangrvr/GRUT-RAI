"""
GRUT Phase D14 -- Tensor Memory Completion and Defect-Sector Derivation Test
=============================================================================

LOCKED INHERITANCE
------------------
- D8: coupled action S_total = S_grav + S_macro + S_defect + S_trigger + S_portal (LOCKED)
- D11: exact two-field BVP converges; companion architecture survives (STRONGLY SUPPORTED)
- D12: Q = n*eta principled and strongly constrained (PRINCIPLED)
- D13: O(3) sector partially_motivated_not_derived; memory tensorization best pathway
- Phase IV: scalar Phi is symmetry-reduced limit of rank-2 Phi_ab (ESTABLISHED)
- Phase IV: rank-2 tensor decomposition: trace(1) + vector(3) + tensor(5) = 10 DOF

SCOPE
-----
Focused foundational derivation phase. Attempts to upgrade the D13 result
by constructing explicit tensor-memory action candidates and testing whether
they produce a spin-1 instability that generates the effective O(3) sector.

MISSION
-------
Work Program A: Construct candidate tensor-memory actions
Work Program B: Mode decomposition and spin-1 sector analysis
Work Program C: Strong-curvature instability test
Work Program D: Support-class and hedgehog continuity test
Work Program E: Eta prediction / constraint analysis
Work Program F: Final D14 classification

RESULT
------
See compute_tensor_memory_completion() for the final determination.

CLASSIFICATION OPTIONS
----------------------
- tensor_memory_completion_derives_effective_O3_sector
- tensor_memory_completion_strongly_induces_triplet_but_not_full_derivation
- tensor_memory_completion_partially_supports_O3_motivation
- tensor_memory_completion_fails_to_upgrade_D13
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

D14_CLASSIFICATION_OPTIONS = [
    "tensor_memory_completion_derives_effective_O3_sector",
    "tensor_memory_completion_strongly_induces_triplet_but_not_full_derivation",
    "tensor_memory_completion_partially_supports_O3_motivation",
    "tensor_memory_completion_fails_to_upgrade_D13",
    "derivation_attempt_failed",
]

ACTION_VERDICTS = [
    "derived",
    "strongly_motivated",
    "partially_motivated",
    "speculative",
    "fails",
]

INSTABILITY_LEVELS = [
    "absent",
    "weak_suggestive",
    "strong",
    "derivationally_decisive",
]

SUPPORT_CLASS_STRENGTHS = [
    "exact",
    "strong",
    "partial",
    "fails",
]

ETA_OUTCOMES = [
    "derived",
    "constrained",
    "related_to_parameters",
    "matched_only",
    "fails",
]

# ---------------------------------------------------------------------------
# Physical constants for the strong-field program
# ---------------------------------------------------------------------------
ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = 0.5
R_EQ = R_S * ALPHA_VAC
R_EXT = 2.0 * R_S
TAU_CANONICAL = math.sqrt(1.5)
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
LAMBDA_DEFAULT = 8.0 * math.pi
COMP_B_COEFF = 1.0 / (8.0 * math.pi)


# ===================================================================
# Dataclasses
# ===================================================================

@dataclass
class TensorActionCandidate:
    """A candidate tensor-memory action."""
    name: str
    field_content: str
    symmetry_class: str
    kinetic_structure: str
    potential_structure: str
    curvature_coupling: str
    scalar_coupling: str
    inherited_content: List[str]
    new_completion_content: List[str]
    mode_structure: str
    new_parameters: List[str]
    verdict: str
    reasoning: str

    def __post_init__(self) -> None:
        if self.verdict not in ACTION_VERDICTS:
            raise ValueError(
                f"Invalid verdict '{self.verdict}'. "
                f"Must be one of {ACTION_VERDICTS}"
            )


@dataclass
class ModeAnalysisEntry:
    """One row of the mode/instability analysis."""
    mode_sector: str
    exists: bool
    dof_count: int
    curvature_sensitive: bool
    instability_status: str
    triplet_relevance: str
    verdict: str
    analysis: str

    def __post_init__(self) -> None:
        if self.instability_status not in INSTABILITY_LEVELS:
            raise ValueError(
                f"Invalid instability status '{self.instability_status}'. "
                f"Must be one of {INSTABILITY_LEVELS}"
            )


@dataclass
class ModeDecomposition:
    """Full mode decomposition result."""
    entries: List[ModeAnalysisEntry]
    spin1_exists: bool
    spin1_instability: str
    summary: str


@dataclass
class SupportClassTest:
    """One support-class continuity test."""
    test: str
    result: str
    strength: str
    comment: str

    def __post_init__(self) -> None:
        if self.strength not in SUPPORT_CLASS_STRENGTHS:
            raise ValueError(
                f"Invalid strength '{self.strength}'. "
                f"Must be one of {SUPPORT_CLASS_STRENGTHS}"
            )


@dataclass
class SupportClassResult:
    """Full support-class continuity result."""
    tests: List[SupportClassTest]
    overall_continuity: bool
    summary: str


@dataclass
class EtaAnalysisEntry:
    """One mechanism tested for eta prediction."""
    mechanism: str
    eta_derived: bool
    eta_constrained: bool
    eta_matched_only: bool
    outcome: str
    comment: str

    def __post_init__(self) -> None:
        if self.outcome not in ETA_OUTCOMES:
            raise ValueError(
                f"Invalid eta outcome '{self.outcome}'. "
                f"Must be one of {ETA_OUTCOMES}"
            )


@dataclass
class EtaAnalysisResult:
    """Full eta prediction/constraint result."""
    entries: List[EtaAnalysisEntry]
    best_outcome: str
    summary: str


@dataclass
class D14Classification:
    """Final D14 classification."""
    classification: str
    justification: str
    spin1_instability_achieved: bool
    support_class_continuity: bool
    eta_progress: bool
    upgrade_over_d13: bool

    def __post_init__(self) -> None:
        if self.classification not in D14_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid D14 classification '{self.classification}'. "
                f"Must be one of {D14_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class FoundationalGap:
    """A remaining foundational gap after D14."""
    gap: str
    severity: str
    notes: str


@dataclass
class D14Result:
    """Top-level D14 result."""
    valid: bool
    action_candidates: List[TensorActionCandidate]
    mode_decomposition: ModeDecomposition
    support_class_result: SupportClassResult
    eta_analysis: EtaAnalysisResult
    classification: D14Classification
    remaining_gaps: List[FoundationalGap]
    nonclaims: List[str]


# ===================================================================
# Work Program A: Tensor Memory Action Candidates
# ===================================================================

def build_action_candidates() -> List[TensorActionCandidate]:
    """Construct and evaluate candidate tensor-memory actions.

    Each candidate is explicitly decomposed into inherited GRUT content
    and new completion content. The key question: does the completion
    naturally yield a spin-1 sector without smuggling in O(3)?
    """
    candidates = []

    # Candidate A1: Minimal massive rank-2 (Fierz-Pauli type)
    candidates.append(TensorActionCandidate(
        name="Minimal massive rank-2 tensor memory (Fierz-Pauli type)",
        field_content=(
            "Rank-2 symmetric tensor Phi_ab with 10 components. "
            "3+1 decomposition: trace Phi (1 DOF, = existing scalar), "
            "vector v_i (3 DOF), trace-free tensor sigma_ij (5 DOF)."
        ),
        symmetry_class="Lorentz covariant, no internal symmetry imposed",
        kinetic_structure=(
            "S_kin = integral sqrt(-g) [-(1/2)(nabla_c Phi_ab)(nabla^c Phi^ab) "
            "+ (1/2)(nabla_c Phi)(nabla^c Phi) + (nabla_a Phi^ab)(nabla_c Phi^cb) "
            "- (nabla_a Phi^ab)(nabla_b Phi)] "
            "This is the Fierz-Pauli kinetic structure for a massive spin-2 field. "
            "It propagates 5 DOF (massive spin-2) and is ghost-free at linear level."
        ),
        potential_structure=(
            "V(Phi_ab) = (1/2)mu^2 [Phi_ab Phi^ab - Phi^2] (Fierz-Pauli mass term). "
            "This gives equal mass to all components. The mass term does NOT "
            "distinguish between scalar, vector, and tensor sectors. All modes "
            "have the same mass mu. No preferential selection of spin-1."
        ),
        curvature_coupling=(
            "Minimal: R * Phi (trace coupling to Ricci scalar). "
            "Non-minimal: R_ab Phi^ab (Ricci tensor coupling) or "
            "C_abcd Phi^ac g^bd (Weyl coupling). The Weyl coupling "
            "C_abcd Phi^ac g^bd sources different components differently "
            "in strong-curvature regions."
        ),
        scalar_coupling=(
            "The trace Phi = g^ab Phi_ab IS the existing scalar memory field. "
            "No additional coupling needed; the scalar sector is automatically inherited."
        ),
        inherited_content=[
            "Trace sector (Phi = g^ab Phi_ab) = existing scalar memory field",
            "Background Schwarzschild metric",
            "Kretschner scalar K for curvature coupling",
        ],
        new_completion_content=[
            "Fierz-Pauli kinetic structure (ghost-free at linear level)",
            "Mass parameter mu (1 new parameter)",
            "Non-minimal curvature coupling coefficients (1-2 new parameters)",
            "Potential V(Phi_ab) with Fierz-Pauli mass term",
        ],
        mode_structure=(
            "In the FP framework: 5 massive spin-2 DOF + 0 spin-1 + 0 spin-0 "
            "(after constraint elimination). The vector/spin-1 sector is a "
            "CONSTRAINT MODE in Fierz-Pauli theory, not a propagating DOF. "
            "This is the Boulware-Deser analysis: the FP mass term specifically "
            "eliminates the scalar ghost and the vector sector as propagating modes. "
            "IMPLICATION: the Fierz-Pauli completion does NOT provide a "
            "propagating spin-1 sector."
        ),
        new_parameters=["mu (tensor mass)", "alpha_R (curvature coupling)"],
        verdict="fails",
        reasoning=(
            "The Fierz-Pauli massive spin-2 theory is ghost-free precisely because "
            "it eliminates the vector (spin-1) and scalar ghost sectors via constraints. "
            "This means the most natural rank-2 completion of the memory tensor does "
            "NOT produce a propagating spin-1 mode. The very feature that makes FP "
            "theoretically healthy (ghost freedom) removes the sector needed for O(3) "
            "induction. This is a structural obstruction, not a parameter choice."
        ),
    ))

    # Candidate A2: Non-Fierz-Pauli mass term (spin-1 active)
    candidates.append(TensorActionCandidate(
        name="Non-Fierz-Pauli mass term: spin-1 active but ghostly",
        field_content=(
            "Same rank-2 Phi_ab, but with a mass term that does NOT satisfy "
            "the Fierz-Pauli tuning: V = (1/2)m_2^2 Phi_ab Phi^ab - (1/2)m_0^2 Phi^2 "
            "with m_0 != m_2 (the FP condition is m_0 = m_2)."
        ),
        symmetry_class="Lorentz covariant; no internal symmetry",
        kinetic_structure="Same as Candidate A1 (standard rank-2 kinetic term)",
        potential_structure=(
            "V = (1/2)m_2^2 Phi_ab Phi^ab - (1/2)m_0^2 Phi^2 with m_0 != m_2. "
            "Detuning from FP: when m_0 != m_2, the scalar constraint is lost "
            "and a spin-0 ghost (Boulware-Deser ghost) propagates. More critically, "
            "the vector sector v_i also becomes dynamical when m_0 != m_2."
        ),
        curvature_coupling="Same as A1",
        scalar_coupling="Trace Phi = existing scalar",
        inherited_content=["Trace sector", "Background metric", "Kretschner scalar"],
        new_completion_content=[
            "Non-FP mass term (2 independent mass parameters)",
            "Active spin-1 sector (3 DOF)",
            "Active scalar ghost (1 DOF) -- problematic",
        ],
        mode_structure=(
            "Detuned mass: 5 (spin-2) + 3 (spin-1) + 1 (spin-0 ghost) = 9 propagating DOF. "
            "The spin-1 sector v_i has 3 propagating DOF with effective mass "
            "m_v^2 = m_2^2 (from the tensor mass). These 3 DOF transform as a "
            "spatial SO(3) vector. However, the scalar ghost mode has wrong-sign "
            "kinetic term, making the theory unstable at the classical level. "
            "The Boulware-Deser ghost is not removable by parameter tuning "
            "within this class of theories."
        ),
        new_parameters=["m_2 (spin-2 mass)", "m_0 (scalar mass, m_0 != m_2)"],
        verdict="fails",
        reasoning=(
            "Detuning from Fierz-Pauli activates the spin-1 sector (3 propagating DOF "
            "transforming as SO(3) vector) but simultaneously introduces the Boulware-Deser "
            "ghost. The theory is classically unstable. One cannot use the spin-1 sector "
            "as a physically meaningful O(3) triplet candidate in a theory that is already "
            "sick. The ghost problem is not a technical detail but a fundamental obstruction: "
            "the Hamiltonian is unbounded below, and the vacuum is unstable."
        ),
    ))

    # Candidate A3: Proca-type vector extraction from tensor
    candidates.append(TensorActionCandidate(
        name="Proca vector extraction: v_i from Phi_ab decomposition",
        field_content=(
            "Extract the vector sector v_i directly from the 3+1 decomposition "
            "of Phi_ab and treat it as an independent Proca (massive vector) field. "
            "Phi_ab = (1/3)Phi g_ab + sigma_ab + sym(v_i n^j). "
            "Promote v_i to dynamical field with Proca action."
        ),
        symmetry_class="Spatial SO(3) vector; Lorentz broken by 3+1 split",
        kinetic_structure=(
            "S_v = integral sqrt(-g) [-(1/4)F_ij F^ij - (1/2)m_v^2 v_i v^i] "
            "where F_ij = nabla_i v_j - nabla_j v_i. This is the standard "
            "Proca action for a massive vector. 3 propagating DOF, no ghosts."
        ),
        potential_structure=(
            "V(v) = (1/2)m_v^2 |v|^2 + (1/4)lambda_v (|v|^2 - eta_v^2)^2. "
            "The Mexican-hat potential would drive SSB: v_i acquires VEV "
            "eta_v when m_v^2 < 0 (tachyonic). In the hedgehog ansatz: "
            "v_i = eta_v f_v(r) x_hat_i."
        ),
        curvature_coupling=(
            "m_v^2(r) = m_v0^2 - xi_v * K(r). When xi_v * K > m_v0^2, "
            "the effective mass becomes tachyonic, triggering SSB. "
            "K = 48*M^2/r^6 grows strongly inward."
        ),
        scalar_coupling=(
            "Portal: g_pv * Phi^2 * |v|^2 (same structure as existing portal). "
            "The scalar Phi and vector v interact through the portal term."
        ),
        inherited_content=[
            "Scalar Phi from trace sector",
            "Background metric and K(r)",
            "Curvature-trigger mechanism from D10",
        ],
        new_completion_content=[
            "Proca kinetic term for v_i (standard, ghost-free)",
            "Mexican-hat potential for v_i (SSB mechanism)",
            "Curvature-dependent mass: m_v^2(r) = m_v0^2 - xi_v*K(r)",
            "Portal coupling g_pv (optional)",
        ],
        mode_structure=(
            "3 propagating DOF (massive Proca vector). No ghosts, no scalar "
            "ghost problem (unlike A2). The vector has well-defined mass "
            "and kinetic structure. Under curvature-triggered SSB: "
            "v_i -> eta_v f_v(r) x_hat_i (hedgehog), with angular gradient "
            "energy eps ~ eta_v^2 f_v^2 / r^2."
        ),
        new_parameters=[
            "m_v0 (bare vector mass)",
            "xi_v (curvature coupling)",
            "lambda_v (self-coupling)",
            "eta_v (VEV, = eta if matched to Phase 6C)",
            "g_pv (portal coupling, optional)",
        ],
        verdict="partially_motivated",
        reasoning=(
            "The Proca extraction is technically clean: 3 ghost-free propagating DOF, "
            "well-defined SSB mechanism, natural curvature triggering. The vector v_i "
            "transforms as SO(3) under spatial rotations, supports hedgehog ansatz, "
            "and produces the correct 1/r^2 support class via angular gradients. "
            "However, this construction faces two fundamental issues: "
            "(1) The extraction of v_i from Phi_ab is not unique -- it depends on the "
            "3+1 foliation, breaking manifest covariance. The vector sector of a rank-2 "
            "tensor is a gauge artifact in the massless limit and only physical in the "
            "massive theory. Treating it as independent requires justification. "
            "(2) The Mexican-hat potential and curvature coupling are NEW additions to "
            "the GRUT action, not derived from it. They are exactly the same structure "
            "as the existing O(3) defect sector (D8 S_defect + S_trigger), just relabeled. "
            "The construction is therefore circular: to derive the O(3) sector from "
            "the tensor memory, we must add to the tensor memory exactly the same "
            "action structure that defines the O(3) sector."
        ),
    ))

    # Candidate A4: Constrained tensor with enhanced curvature coupling
    candidates.append(TensorActionCandidate(
        name="Constrained tensor with Weyl-tensor sourcing of vector mode",
        field_content=(
            "Rank-2 Phi_ab with additional constraint: nabla^a Phi_ab = 0 "
            "(transversality), reducing DOF to 6. Decomposition: "
            "1 (trace) + 0 (vector, killed by constraint) + 5 (tensor)."
        ),
        symmetry_class="Lorentz covariant; transversality-constrained",
        kinetic_structure=(
            "S = integral sqrt(-g) [-(1/2)(nabla_c Phi_ab)(nabla^c Phi^ab) "
            "+ lambda_constraint * (nabla^a Phi_ab)^2] "
            "with lambda_constraint -> infinity enforcing transversality."
        ),
        potential_structure=(
            "V = (1/2)mu^2 [Phi_ab Phi^ab - alpha_trace * Phi^2]. "
            "Transversality constraint kills the vector sector entirely."
        ),
        curvature_coupling=(
            "R_abcd Phi^ac Phi^bd (curvature-tensor coupling). Sources "
            "anisotropic components in strong-field region."
        ),
        scalar_coupling="Trace Phi = existing scalar",
        inherited_content=["Trace sector", "Background metric"],
        new_completion_content=[
            "Transversality constraint",
            "Tensor mass mu",
            "Curvature-tensor coupling",
        ],
        mode_structure=(
            "6 DOF: 1 (scalar trace) + 5 (traceless-transverse tensor). "
            "The vector sector is ELIMINATED by the transversality constraint. "
            "This is the natural completion for gravitational-wave-like memory "
            "but provides NO spin-1 sector at all."
        ),
        new_parameters=["mu (tensor mass)", "curvature coupling coefficient"],
        verdict="fails",
        reasoning=(
            "The transversality constraint explicitly kills the vector sector. "
            "This is the cleanest tensor completion (no ghosts, well-defined "
            "propagation) but it cannot produce an O(3)-like triplet because "
            "the relevant DOF are absent by construction."
        ),
    ))

    # Candidate A5: First-order (relaxation) tensor memory
    candidates.append(TensorActionCandidate(
        name="First-order relaxation tensor (GRUT-native memory structure)",
        field_content=(
            "Rank-2 symmetric Phi_ab treated as a non-propagating memory field "
            "with first-order relaxation dynamics: tau * d/dt Phi_ab = -Phi_ab + S_ab. "
            "This is the tensorial extension of the GRUT memory relation "
            "tau * dPhi/dt = -Phi + S_Phi."
        ),
        symmetry_class="No Lorentz invariance (first-order in time); spatial SO(3)",
        kinetic_structure=(
            "NOT a standard kinetic term. The GRUT memory field obeys a "
            "first-order relaxation equation, not a second-order wave equation. "
            "The tensor version: tau * d/dt Phi_ab = -Phi_ab + S_ab(g, R, ...). "
            "This is a constitutive relation, not a variational field theory. "
            "The D8 action adds a Laplacian (spatial second derivative) for the "
            "macro field equation, but the original GRUT memory relation is "
            "first-order in time."
        ),
        potential_structure=(
            "No potential in the variational sense. The equilibrium is determined "
            "by the source: Phi_ab^eq = S_ab. The 'potential' is the deviation "
            "from equilibrium: V ~ (1/2)|Phi_ab - S_ab|^2 / tau^2."
        ),
        curvature_coupling=(
            "Through the source: S_ab depends on curvature. In the scalar case: "
            "S_Phi = M/r^2. For the tensor: S_ab could include R_ab, C_abcd, etc."
        ),
        scalar_coupling="Trace: tau*dPhi/dt = -Phi + S_Phi is the existing scalar memory",
        inherited_content=[
            "First-order memory structure (GRUT-native)",
            "Trace sector = existing scalar",
            "Source S_Phi = M/r^2 for trace",
        ],
        new_completion_content=[
            "Tensor source S_ab (must be specified for non-trace components)",
            "Relaxation time tau_ab (could differ by sector: tau_scalar, tau_vector, tau_tensor)",
            "No new fundamental parameters beyond source specification",
        ],
        mode_structure=(
            "First-order dynamics: NO propagating modes at all. The tensor memory "
            "relaxes to its source on timescale tau. In the static limit (d/dt = 0): "
            "Phi_ab = S_ab. The vector sector v_i = S_v_i (sourced by curvature). "
            "In spherical symmetry with S_ab from the Schwarzschild tidal field: "
            "S_ab = diag(S_tt, S_rr, S_theta, S_theta) with 2 independent components. "
            "The vector source S_v_i = 0 in spherical symmetry (no preferred direction). "
            "PROBLEM: the first-order relaxation structure does not support SSB "
            "because there is no potential energy landscape -- the field simply "
            "tracks its source. There is no Mexican-hat potential, no VEV, no "
            "spontaneous breaking."
        ),
        new_parameters=["tau_v (vector relaxation time, if different from tau)"],
        verdict="fails",
        reasoning=(
            "The first-order relaxation structure is the most GRUT-native tensor "
            "completion, but it fundamentally cannot support spontaneous symmetry "
            "breaking. SSB requires a potential energy landscape with multiple minima; "
            "the relaxation equation has a single equilibrium (Phi_ab = S_ab) determined "
            "by the source. Without SSB, there is no hedgehog, no VEV, no topological "
            "charge. The GRUT memory structure is constitutive, not variational, and "
            "this distinction is precisely what prevents it from generating the O(3) "
            "sector natively."
        ),
    ))

    return candidates


# ===================================================================
# Work Program B: Mode Decomposition
# ===================================================================

def analyze_mode_decomposition(
    candidates: List[TensorActionCandidate],
) -> ModeDecomposition:
    """Analyze the mode structure of tensor-memory candidates.

    Focus on whether a spin-1 sector exists and is dynamically accessible.
    """
    entries = [
        # Scalar trace (always present)
        ModeAnalysisEntry(
            mode_sector="scalar_trace",
            exists=True,
            dof_count=1,
            curvature_sensitive=True,
            instability_status="absent",
            triplet_relevance="none -- this IS the existing scalar memory field",
            verdict="not_relevant",
            analysis=(
                "The scalar trace Phi = g^ab Phi_ab is the existing GRUT scalar memory "
                "field. It is always present, always stable (first-order relaxation "
                "to equilibrium). It does not contribute to the O(3) sector question."
            ),
        ),
        # Vector / spin-1 sector
        ModeAnalysisEntry(
            mode_sector="vector_spin1",
            exists=True,
            dof_count=3,
            curvature_sensitive=True,
            instability_status="absent",
            triplet_relevance=(
                "If propagating AND unstable: could serve as effective O(3) triplet. "
                "BUT: in Fierz-Pauli (A1) it is a constraint, not propagating. "
                "In non-FP (A2) it propagates but with ghost. "
                "In Proca extraction (A3) it propagates but requires adding the same "
                "action structure as the O(3) sector. "
                "In constrained (A4) it is killed. "
                "In relaxation (A5) it does not support SSB."
            ),
            verdict="structurally_blocked",
            analysis=(
                "The spin-1 sector exists in the general rank-2 decomposition (3 DOF). "
                "However, every consistent tensor completion either eliminates it "
                "(FP, constrained), makes it ghostly (non-FP), or requires adding "
                "exactly the O(3) action structure to make it physical (Proca extraction). "
                "The GRUT-native first-order relaxation does not support SSB. "
                "There is no pathway from a healthy tensor-memory completion to a "
                "propagating, unstable spin-1 sector WITHOUT adding new physics "
                "equivalent to the O(3) sector itself."
            ),
        ),
        # Tensor / spin-2 sector
        ModeAnalysisEntry(
            mode_sector="tensor_spin2",
            exists=True,
            dof_count=5,
            curvature_sensitive=True,
            instability_status="absent",
            triplet_relevance="none -- spin-2 cannot serve as spin-1 triplet",
            verdict="not_relevant",
            analysis=(
                "The trace-free symmetric tensor sigma_ij has 5 DOF and transforms "
                "as spin-2 under spatial rotations. It cannot serve as an O(3) triplet "
                "(wrong spin). Relevant for gravitational-wave memory but not for "
                "the defect sector."
            ),
        ),
    ]

    # Determine overall spin-1 status
    spin1_entry = next(e for e in entries if e.mode_sector == "vector_spin1")
    spin1_exists = spin1_entry.exists
    spin1_instability = spin1_entry.instability_status

    return ModeDecomposition(
        entries=entries,
        spin1_exists=spin1_exists,
        spin1_instability=spin1_instability,
        summary=(
            "The spin-1 sector (3 DOF) exists in the general rank-2 decomposition "
            "but is structurally blocked from serving as an effective O(3) triplet "
            "in every consistent tensor-memory completion tested. The fundamental "
            "obstruction takes different forms depending on the completion: "
            "eliminated by FP constraints, ghostly when constraints relaxed, "
            "circular when independently promoted, or incompatible with SSB in "
            "the GRUT-native first-order relaxation structure."
        ),
    )


# ===================================================================
# Work Program C: Strong-Curvature Instability
# ===================================================================
# This is assessed within the mode decomposition. The key finding:
# no consistent tensor completion produces a curvature-triggered
# spin-1 instability. The instability analysis is implicit in the
# mode decomposition verdicts.


# ===================================================================
# Work Program D: Support-Class Continuity
# ===================================================================

def test_support_class_continuity() -> SupportClassResult:
    """Test whether the tensor-memory completion can reproduce Component B."""
    tests = [
        SupportClassTest(
            test="Does any tensor completion produce eps ~ 1/r^2?",
            result=(
                "Only the Proca extraction (A3) produces eps ~ eta_v^2 f^2/r^2, "
                "but this requires adding a Mexican-hat potential and curvature "
                "coupling that are equivalent to the existing O(3) sector action."
            ),
            strength="fails",
            comment="The 1/r^2 is achieved circularly, not derivationally.",
        ),
        SupportClassTest(
            test="Does the tensor trace sector produce 1/r^2?",
            result=(
                "No. The trace sector gives eps_macro ~ Phi^2/(2*tau^2) ~ 1/r^4. "
                "This is Component A, not Component B."
            ),
            strength="fails",
            comment="The scalar/trace sector always gives 1/r^4.",
        ),
        SupportClassTest(
            test="Does the tensor spin-2 sector produce 1/r^2?",
            result=(
                "No. The spin-2 sector sigma_ij in the FP theory has energy "
                "eps ~ sigma^2, which depends on the sourcing. In spherical "
                "symmetry with tidal sourcing: sigma ~ M/r^3, giving eps ~ 1/r^6."
            ),
            strength="fails",
            comment="Spin-2 gives 1/r^6, not 1/r^2.",
        ),
        SupportClassTest(
            test="Does any GRUT-native mechanism produce angular gradient energy?",
            result=(
                "Angular gradient energy ~ f^2/r^2 requires a field that varies "
                "across the 2-sphere at each radius. The scalar Phi(r) is spherically "
                "symmetric. The tensor components in spherical symmetry are radial "
                "functions only. Angular variation requires breaking spherical symmetry, "
                "which means the hedgehog must be a NEW configuration, not a consequence "
                "of the background geometry."
            ),
            strength="fails",
            comment=(
                "Fundamental: 1/r^2 requires angular variation, which requires "
                "spherical symmetry breaking, which requires an independent field."
            ),
        ),
        SupportClassTest(
            test="Is the hedgehog ansatz compatible with tensor-memory structure?",
            result=(
                "Yes, structurally: if v_i is promoted to an independent field with SSB, "
                "v_i = eta_v f(r) x_hat_i is a valid hedgehog. But this promotion "
                "is the O(3) sector, not a derivation of it."
            ),
            strength="partial",
            comment="Compatible but circular.",
        ),
    ]

    # Overall: no genuine derivational continuity
    return SupportClassResult(
        tests=tests,
        overall_continuity=False,
        summary=(
            "No tensor-memory completion produces the 1/r^2 support class "
            "without adding action structure equivalent to the existing O(3) "
            "defect sector. The fundamental obstruction is that the 1/r^2 "
            "scaling requires angular gradient energy, which requires a field "
            "that varies across the 2-sphere, which requires breaking spherical "
            "symmetry through an independent internal DOF. The tensor memory "
            "in spherical symmetry has only radial-function components."
        ),
    )


# ===================================================================
# Work Program E: Eta Prediction / Constraint
# ===================================================================

def analyze_eta_prediction() -> EtaAnalysisResult:
    """Test whether tensor-memory completion can derive or constrain eta."""
    entries = [
        EtaAnalysisEntry(
            mechanism="Fierz-Pauli mass matching",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=False,
            outcome="fails",
            comment=(
                "FP theory has mass parameter mu but no VEV. There is no eta "
                "in a theory without SSB."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="Non-FP detuning parameter",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=False,
            outcome="fails",
            comment="Ghost-ridden theory; eta is not meaningful.",
        ),
        EtaAnalysisEntry(
            mechanism="Proca VEV from potential minimum",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=True,
            outcome="matched_only",
            comment=(
                "The Proca Mexican-hat potential has VEV eta_v = mu_v / sqrt(lambda_v), "
                "which is a free parameter combination. Setting eta_v = 1/sqrt(8*pi) "
                "is matching, not derivation. The potential parameters mu_v and lambda_v "
                "are independent and not constrained by GRUT-native structure."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="Curvature-induced VEV from strong-field equilibrium",
            eta_derived=False,
            eta_constrained=True,
            eta_matched_only=False,
            outcome="related_to_parameters",
            comment=(
                "If m_v^2(r) = m_v0^2 - xi_v*K(r), then the VEV at radius r is "
                "eta_v(r) = sqrt((xi_v*K(r) - m_v0^2) / lambda_v). At R_eq: "
                "K(R_eq) = 48*M^2/R_eq^6 = 8748 (with M=0.5, R_eq=1/3). "
                "eta_v^2 = (xi_v*8748 - m_v0^2) / lambda_v. Setting this equal "
                "to 1/(8*pi) constrains a COMBINATION of xi_v, m_v0, and lambda_v, "
                "but does not uniquely determine any of them. This is a constraint "
                "relation, not a prediction."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="First-order relaxation equilibrium",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=False,
            outcome="fails",
            comment=(
                "The relaxation equation Phi_ab -> S_ab has no VEV concept. "
                "The equilibrium is determined by the source, not by a potential."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="Dimensional analysis from tau and curvature",
            eta_derived=False,
            eta_constrained=True,
            eta_matched_only=False,
            outcome="related_to_parameters",
            comment=(
                "The GRUT parameters tau^2 = 3/2 and K(R_eq) = 8748 define a "
                "natural scale: tau^2 / K(R_eq)^{1/2} ~ 1.5 / 93.5 ~ 0.016. "
                "Compare eta^2 = 1/(8*pi) ~ 0.040. The ratio is O(1) but not "
                "exact. No dimensionally unique combination of GRUT parameters "
                "produces 1/(8*pi) without arbitrary numerical factors."
            ),
        ),
    ]

    # Best outcome
    outcomes = [e.outcome for e in entries]
    if "derived" in outcomes:
        best = "derived"
    elif "constrained" in outcomes:
        best = "constrained"
    elif "related_to_parameters" in outcomes:
        best = "related_to_parameters"
    elif "matched_only" in outcomes:
        best = "matched_only"
    else:
        best = "fails"

    return EtaAnalysisResult(
        entries=entries,
        best_outcome=best,
        summary=(
            "No mechanism derives eta^2 = 1/(8*pi) from tensor-memory completion. "
            "The best outcome is 'related_to_parameters': the curvature-induced VEV "
            "constrains a COMBINATION of new parameters (xi_v, m_v0, lambda_v) to "
            "match eta, but this is not a prediction. Dimensional analysis from "
            "GRUT-native parameters (tau, K) gives the right order of magnitude "
            "but not the exact value. eta remains a matching condition."
        ),
    )


# ===================================================================
# Work Program F: Classification
# ===================================================================

def classify_d14(
    mode_decomposition: ModeDecomposition,
    support_class_result: SupportClassResult,
    eta_analysis: EtaAnalysisResult,
) -> D14Classification:
    """Classify the D14 result from explicit criteria.

    Classification logic (deterministic, no hidden weights):

    To upgrade beyond D13, ALL THREE must be achieved:
    1. Curvature-triggered spin-1 instability
    2. Support-class continuity ~ 1/r^2
    3. Eta derivational progress (derived or constrained)

    - All 3 strong: derives_effective_O3
    - 2 of 3 strong: strongly_induces
    - 1 of 3: partially_supports
    - 0 of 3: fails_to_upgrade
    """
    spin1_achieved = mode_decomposition.spin1_instability in (
        "strong", "derivationally_decisive",
    )
    support_achieved = support_class_result.overall_continuity
    eta_progress = eta_analysis.best_outcome in ("derived", "constrained")

    score = sum([spin1_achieved, support_achieved, eta_progress])

    if score == 3:
        classification = "tensor_memory_completion_derives_effective_O3_sector"
    elif score == 2:
        classification = "tensor_memory_completion_strongly_induces_triplet_but_not_full_derivation"
    elif score == 1:
        classification = "tensor_memory_completion_partially_supports_O3_motivation"
    elif score == 0:
        # Check if any candidate has non-failing verdict
        classification = "tensor_memory_completion_fails_to_upgrade_D13"
    else:
        classification = "derivation_attempt_failed"

    upgrade = score >= 2

    justification = (
        f"Spin-1 instability: {'achieved' if spin1_achieved else 'NOT achieved'} "
        f"(status: {mode_decomposition.spin1_instability}). "
        f"Support-class continuity: {'achieved' if support_achieved else 'NOT achieved'}. "
        f"Eta progress: {'achieved' if eta_progress else 'NOT achieved'} "
        f"(best: {eta_analysis.best_outcome}). "
        f"Score: {score}/3. "
        f"The tensor-memory completion does not upgrade the O(3) sector beyond D13 "
        f"because the spin-1 sector is structurally blocked in every consistent "
        f"completion, and the support-class requires adding the O(3) action structure "
        f"(circular). Eta remains a matching condition."
    )

    return D14Classification(
        classification=classification,
        justification=justification,
        spin1_instability_achieved=spin1_achieved,
        support_class_continuity=support_achieved,
        eta_progress=eta_progress,
        upgrade_over_d13=upgrade,
    )


# ===================================================================
# Remaining Gaps
# ===================================================================

def identify_remaining_gaps(
    classification: D14Classification,
) -> List[FoundationalGap]:
    """Identify remaining foundational gaps after D14."""
    gaps = [
        FoundationalGap(
            gap="O(3) sector remains a principled extension, not derived",
            severity="critical",
            notes=(
                "D14 shows the tensor-memory route cannot derive the O(3) sector "
                "without adding action structure equivalent to the sector itself. "
                "The defect sector remains the most principled extension available "
                "but is not a consequence of GRUT-native structure."
            ),
        ),
        FoundationalGap(
            gap="Fundamental obstruction identified: SSB requires variational structure",
            severity="critical",
            notes=(
                "The GRUT memory field is constitutive (first-order relaxation). "
                "SSB requires a variational field with a potential landscape. "
                "These are structurally incompatible. This is not a technical gap "
                "but a category distinction."
            ),
        ),
        FoundationalGap(
            gap="Coefficient eta^2 = 1/(8*pi) remains a matching condition",
            severity="significant",
            notes=(
                "No tensor-memory mechanism predicts this value. The best outcome "
                "is that curvature parameters can be combined to match it, but the "
                "combination is not unique."
            ),
        ),
        FoundationalGap(
            gap="Empirical confrontation still absent",
            severity="critical",
            notes="Inherited from bridge document.",
        ),
        FoundationalGap(
            gap="Healthy spin-1 sector requires independent field introduction",
            severity="significant",
            notes=(
                "The spin-1 sector of a rank-2 tensor is either a constraint (FP), "
                "ghostly (non-FP), or must be independently promoted (Proca). "
                "No tensor completion naturally produces a healthy propagating "
                "spin-1 sector."
            ),
        ),
    ]
    return gaps


# ===================================================================
# Nonclaims
# ===================================================================

NONCLAIMS = [
    "D14 does not claim that the tensor-memory completion derives the O(3) sector.",
    "D14 does not claim that any candidate action is free of theoretical issues.",
    "D14 does not claim that eta^2 = 1/(8*pi) is predicted or derived.",
    "D14 does not claim that the spin-1 sector is dynamically accessible in any consistent completion.",
    "D14 does not conflate the existence of 3 DOF in a tensor decomposition with an O(3) triplet.",
    "D14 does not treat structural elegance or mode counting as derivation.",
    "D14 does not claim the GRUT-native relaxation structure supports SSB.",
    "D14 does not inflate partial motivation into effective induction.",
]


# ===================================================================
# Main computation
# ===================================================================

def compute_tensor_memory_completion() -> D14Result:
    """Compute the full D14 result.

    Top-level entry point. Evaluates all tensor-memory action candidates,
    performs mode decomposition, tests support-class continuity,
    analyzes eta prediction, and classifies the result.
    """
    candidates = build_action_candidates()
    modes = analyze_mode_decomposition(candidates)
    support = test_support_class_continuity()
    eta = analyze_eta_prediction()
    classification = classify_d14(modes, support, eta)
    gaps = identify_remaining_gaps(classification)

    return D14Result(
        valid=True,
        action_candidates=candidates,
        mode_decomposition=modes,
        support_class_result=support,
        eta_analysis=eta,
        classification=classification,
        remaining_gaps=gaps,
        nonclaims=list(NONCLAIMS),
    )


# ===================================================================
# Export
# ===================================================================

def d14_result_to_dict(result: D14Result) -> Dict[str, Any]:
    """Convert D14Result to a JSON-serializable dictionary."""
    return asdict(result)


def export_d14_result_json(result: D14Result, path: str) -> None:
    """Export D14Result to a JSON file."""
    d = d14_result_to_dict(result)
    with open(path, "w") as f:
        json.dump(d, f, indent=2, default=str)
