"""
GRUT Phase D15 -- Non-Minimal Curvature Coupling and Weyl-Induced Vector Deployment Test
=========================================================================================

LOCKED INHERITANCE
------------------
- D8: coupled action S_total = S_grav + S_macro + S_defect + S_trigger + S_portal (LOCKED)
- D11: exact two-field BVP converges; companion architecture survives (STRONGLY SUPPORTED)
- D12: Q = n*eta principled and strongly constrained (PRINCIPLED)
- D13: O(3) sector partially_motivated_not_derived; memory tensorization best pathway
- D14: tensor_memory_completion_fails_to_upgrade_D13 (NEGATIVE CLOSURE)
  * Fierz-Pauli eliminates spin-1 as constraint
  * Non-FP activates spin-1 but introduces Boulware-Deser ghost
  * Proca extraction is circular (adds O(3) action structure)
  * Constrained tensor kills vector by transversality
  * First-order relaxation cannot support SSB
- Phase IV: scalar Phi is symmetry-reduced limit of rank-2 Phi_ab (ESTABLISHED)
- Phase IV: rank-2 tensor decomposition: trace(1) + vector(3) + tensor(5) = 10 DOF

SCOPE
-----
D14 tested MINIMAL tensor-memory completions and found all routes blocked.
D15 tests whether NON-MINIMAL curvature coupling (Weyl/tidal family) can
alter the mode structure to reopen a spin-1/vector deployment channel.

This is the strongest remaining native derivation loophole because:
1. D14 considered only minimal curvature coupling (R*Phi, R_ab*Phi^ab)
2. Non-minimal Weyl-tensor couplings act differently on different spin sectors
3. Tidal curvature distinguishes spin-0/spin-1/spin-2 via Weyl projections
4. Strong-curvature regime amplifies non-minimal effects

CORE QUESTION
-------------
Can non-minimal tidal-curvature coupling alter the tensor-memory mode
structure enough to induce the effective O(3)-like sector required by
the strong-field program, without inserting that sector by hand?

RESULT
------
See compute_weyl_coupling_result() for the final determination.

CLASSIFICATION OPTIONS
----------------------
- nonminimal_curvature_route_fails
- nonminimal_curvature_route_suggestive_only
- nonminimal_curvature_route_opens_vector_channel
- nonminimal_curvature_route_strongly_induces_effective_triplet
- nonminimal_curvature_route_derives_effective_O3_sector
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Tuple


# ---------------------------------------------------------------------------
# Classification vocabularies
# ---------------------------------------------------------------------------

D15_CLASSIFICATION_OPTIONS = [
    "nonminimal_curvature_route_fails",
    "nonminimal_curvature_route_suggestive_only",
    "nonminimal_curvature_route_opens_vector_channel",
    "nonminimal_curvature_route_strongly_induces_effective_triplet",
    "nonminimal_curvature_route_derives_effective_O3_sector",
]

COUPLING_TYPES = [
    "scalar_curvature",       # R * f(Phi_ab)
    "ricci_tensor",           # R_ab * Phi^ac
    "weyl_tensor",            # C_abcd * Phi^ac * Phi^bd
    "kretschner_effective",   # K * f(Phi_ab)
    "gauss_bonnet_family",    # G_4 * f(Phi)
]

ACTION_VERDICTS = [
    "derived",
    "strongly_motivated",
    "partially_motivated",
    "suggestive_only",
    "fails",
]

INSTABILITY_LEVELS = [
    "absent",
    "weak_suggestive",
    "curvature_sensitive_stable",
    "weakly_unstable",
    "strongly_unstable",
    "derivationally_decisive",
]

GHOST_STATUSES = [
    "ghost_free",
    "ghost_risky",
    "ghost_present",
    "undecidable",
]

SUPPORT_CLASS_STRENGTHS = [
    "exact",
    "strong",
    "partial",
    "absent",
    "fails",
]

ETA_OUTCOMES = [
    "derived",
    "constrained",
    "related_to_parameters",
    "matched_only",
    "fails",
]

D14_VS_D15_UPGRADE_LEVELS = [
    "no_upgrade",
    "conceptual_only",
    "opens_channel",
    "strong_induction",
    "full_derivation",
]


# ---------------------------------------------------------------------------
# Physical constants
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
class NonMinimalActionCandidate:
    """A candidate non-minimal curvature-coupled tensor-memory action."""
    name: str
    coupling_type: str
    action_term: str
    inherited_content: List[str]
    new_completion_content: List[str]
    coupling_parameters: List[str]
    ghost_status: str
    mode_modification: str
    vector_sector_effect: str
    verdict: str
    reasoning: str

    def __post_init__(self) -> None:
        if self.coupling_type not in COUPLING_TYPES:
            raise ValueError(
                f"Invalid coupling type '{self.coupling_type}'. "
                f"Must be one of {COUPLING_TYPES}"
            )
        if self.verdict not in ACTION_VERDICTS:
            raise ValueError(
                f"Invalid verdict '{self.verdict}'. "
                f"Must be one of {ACTION_VERDICTS}"
            )
        if self.ghost_status not in GHOST_STATUSES:
            raise ValueError(
                f"Invalid ghost status '{self.ghost_status}'. "
                f"Must be one of {GHOST_STATUSES}"
            )


@dataclass
class ModeEffectiveMassEntry:
    """One row of the mode/instability analysis under non-minimal coupling."""
    mode_sector: str
    exists: bool
    curvature_sensitive: bool
    effective_mass_shift: str
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
class ModeDecompositionD15:
    """Full D15 mode decomposition result."""
    entries: List[ModeEffectiveMassEntry]
    vector_exists: bool
    vector_curvature_sensitive: bool
    vector_instability: str
    best_candidate_for_vector: str
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
    """One mechanism tested for eta prediction in D15."""
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
    """Full eta analysis result."""
    entries: List[EtaAnalysisEntry]
    best_outcome: str
    summary: str


@dataclass
class D14vsD15Entry:
    """One comparison criterion between D14 and D15."""
    criterion: str
    d14_result: str
    d15_result: str
    upgrade: bool
    comment: str


@dataclass
class D14vsD15Comparison:
    """Full D14 vs D15 comparison."""
    entries: List[D14vsD15Entry]
    overall_upgrade: str  # one of D14_VS_D15_UPGRADE_LEVELS
    summary: str


@dataclass
class FoundationalGap:
    """A remaining foundational gap after D15."""
    gap: str
    severity: str
    notes: str


@dataclass
class D15Classification:
    """Final D15 classification."""
    classification: str
    justification: str
    vector_channel_opened: bool
    instability_achieved: bool
    support_class_continuity: bool
    eta_progress: bool
    upgrade_over_d14: str

    def __post_init__(self) -> None:
        if self.classification not in D15_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid D15 classification '{self.classification}'. "
                f"Must be one of {D15_CLASSIFICATION_OPTIONS}"
            )
        if self.upgrade_over_d14 not in D14_VS_D15_UPGRADE_LEVELS:
            raise ValueError(
                f"Invalid upgrade level '{self.upgrade_over_d14}'. "
                f"Must be one of {D14_VS_D15_UPGRADE_LEVELS}"
            )


@dataclass
class D15Result:
    """Top-level D15 result."""
    valid: bool
    action_candidates: List[NonMinimalActionCandidate]
    mode_decomposition: ModeDecompositionD15
    support_class_result: SupportClassResult
    eta_analysis: EtaAnalysisResult
    d14_comparison: D14vsD15Comparison
    classification: D15Classification
    remaining_gaps: List[FoundationalGap]
    nonclaims: List[str]


# ===================================================================
# Part A: Why D14 does not close all tensor-memory routes
# ===================================================================

D14_LOOPHOLE_STATEMENT = """
D14 tested five minimal tensor-memory completions and found every route
blocked. However, D14's analysis was restricted to MINIMAL curvature
couplings: R*Phi (scalar-curvature) and R_ab*Phi^ab (Ricci-tensor).

The loophole: Non-minimal curvature couplings — specifically Weyl-tensor
contractions C_abcd*Phi^ac*Phi^bd — act DIFFERENTLY on different spin
sectors. The Weyl tensor is trace-free, so it couples only to the
traceless part of Phi_ab, which includes both the vector (spin-1) and
tensor (spin-2) sectors but NOT the scalar trace. This means:

1. Weyl coupling can split the effective mass of vector vs tensor modes
2. In strong curvature (near r ~ R_S), Weyl effects are large
3. The mass splitting could in principle make the vector sector tachyonic
   while keeping the tensor sector stable
4. A tachyonic vector sector could trigger SSB if a potential is present

Why Weyl/tidal family is the best remaining candidate:
- Ricci curvature vanishes in vacuum (R_ab = 0 outside matter), so Ricci
  couplings contribute nothing in the exterior strong-field region
- Weyl curvature dominates in vacuum strong-field regions
- The Weyl tensor's irreducible structure naturally distinguishes between
  spin sectors of a rank-2 field

What would count as a genuine upgrade beyond D14:
- A non-minimal coupling that opens a vector channel WITHOUT ghost
- Curvature-triggered instability in the vector sector specifically
- Support-class continuity with 1/r^2 Component B
- Some progress on eta derivation or constraint
All four would be needed for a strong upgrade. Any one alone is suggestive.
"""


# ===================================================================
# Part B: Candidate Non-Minimal Tensor-Memory Actions
# ===================================================================

def build_nonminimal_candidates() -> List[NonMinimalActionCandidate]:
    """Construct candidate non-minimal curvature-coupled tensor-memory actions.

    Each candidate includes a non-minimal curvature coupling beyond what
    D14 considered. The question: does any such coupling materially alter
    the mode structure to open a vector deployment channel?
    """
    candidates = []

    # Candidate B1: Weyl-tensor quadratic coupling
    candidates.append(NonMinimalActionCandidate(
        name="Weyl-tensor quadratic coupling to rank-2 memory",
        coupling_type="weyl_tensor",
        action_term=(
            "S_Weyl = xi_W * integral sqrt(-g) C_abcd Phi^ac Phi^bd. "
            "This contracts the Weyl tensor with two copies of the memory "
            "tensor. Since C_abcd is trace-free (C^a_{bad} = 0), this term "
            "couples ONLY to the traceless part of Phi_ab."
        ),
        inherited_content=[
            "Rank-2 Phi_ab from Phase IV tensor extension",
            "Trace Phi = existing scalar memory",
            "Background Schwarzschild metric and Weyl tensor",
            "D14 minimal kinetic and mass structure",
        ],
        new_completion_content=[
            "Weyl coupling coefficient xi_W (1 new parameter)",
            "Non-minimal Weyl-Phi-Phi vertex",
        ],
        coupling_parameters=["xi_W (Weyl coupling strength, dimensionless)"],
        ghost_status="ghost_risky",
        mode_modification=(
            "In Schwarzschild background, C_abcd has electric (E_ij) and "
            "magnetic (B_ij) tidal components. E_ij = diag(2M/r^3, -M/r^3, -M/r^3) "
            "in an orthonormal frame. The Weyl coupling generates an effective "
            "mass correction: delta_m^2_ij ~ xi_W * E_ij for the traceless sector. "
            "3+1 decomposition of the Weyl-Phi-Phi term: the vector sector v_i "
            "receives a curvature-dependent effective mass shift from E_ij contraction "
            "of the form delta_m_v^2 ~ -xi_W * M / r^3. "
            "The tensor sector sigma_ij receives delta_m_sigma^2 ~ xi_W * M / r^3 "
            "(different sign for different polarizations). "
            "KEY ISSUE: in the Fierz-Pauli framework the vector sector is a "
            "constraint, not a propagating mode. The Weyl coupling modifies the "
            "constraint equation but does NOT promote the vector to a propagating "
            "DOF. To have a propagating vector, one must already depart from FP, "
            "which reintroduces the Boulware-Deser ghost. The Weyl coupling alone "
            "cannot overcome the FP constraint structure."
        ),
        vector_sector_effect=(
            "In FP completion: vector remains constrained. Weyl coupling modifies "
            "the constraint relation but does not convert it to a dynamical equation. "
            "In non-FP completion: vector is dynamical but ghostly. Weyl coupling "
            "modifies the ghost's mass but does not cure the ghost. "
            "Net effect on vector deployment: ABSENT."
        ),
        verdict="fails",
        reasoning=(
            "The Weyl-tensor quadratic coupling C_abcd*Phi^ac*Phi^bd is the most "
            "natural non-minimal coupling for a rank-2 field. It provides "
            "curvature-dependent mass splitting between spin sectors. However, "
            "it cannot overcome the fundamental FP constraint structure: the vector "
            "sector is a constraint mode in FP theory, and a non-minimal coupling "
            "to the background curvature modifies the constraint equation but does "
            "not promote it to a dynamical equation. The constraint structure is "
            "determined by the kinetic term, not the mass/coupling terms. "
            "Non-minimal coupling is a mass-level effect; the FP obstruction is a "
            "kinetic-level structure."
        ),
    ))

    # Candidate B2: Ricci-tensor contraction
    candidates.append(NonMinimalActionCandidate(
        name="Ricci-tensor contraction with memory tensor",
        coupling_type="ricci_tensor",
        action_term=(
            "S_Ric = xi_R * integral sqrt(-g) R_ab Phi^ab. "
            "Linear coupling of Ricci tensor to memory tensor trace."
        ),
        inherited_content=[
            "Rank-2 Phi_ab from Phase IV",
            "Background metric",
        ],
        new_completion_content=[
            "Ricci coupling coefficient xi_R (1 new parameter)",
        ],
        coupling_parameters=["xi_R (Ricci coupling strength)"],
        ghost_status="ghost_free",
        mode_modification=(
            "R_ab = 0 in vacuum Schwarzschild exterior. The Ricci coupling "
            "vanishes identically in the vacuum strong-field region where the "
            "defect sector is needed. It can contribute only inside matter "
            "(R_ab != 0), but the O(3) hedgehog operates in the exterior/vacuum "
            "strong-field zone. This coupling is structurally irrelevant for "
            "the vector deployment question."
        ),
        vector_sector_effect="None. R_ab = 0 in vacuum; coupling vanishes where needed.",
        verdict="fails",
        reasoning=(
            "Ricci-tensor coupling vanishes in the vacuum exterior where the "
            "O(3) defect sector operates. The strong-field region near r ~ R_S "
            "in Schwarzschild is vacuum (R_ab = 0). Only the Weyl tensor is "
            "nonzero there. Ricci coupling is therefore structurally irrelevant "
            "for the vector deployment question, regardless of coupling strength."
        ),
    ))

    # Candidate B3: Kretschner-scalar effective coupling
    candidates.append(NonMinimalActionCandidate(
        name="Kretschner-scalar effective coupling to tensor bilinear",
        coupling_type="kretschner_effective",
        action_term=(
            "S_K = xi_K * integral sqrt(-g) K * Phi_ab Phi^ab, "
            "where K = R_abcd R^abcd = 48 M^2 / r^6 (Schwarzschild). "
            "This is a scalar-curvature coupling to the tensor norm."
        ),
        inherited_content=[
            "Rank-2 Phi_ab from Phase IV",
            "Kretschner scalar K from D10 trigger logic",
        ],
        new_completion_content=[
            "Kretschner coupling coefficient xi_K",
        ],
        coupling_parameters=["xi_K (Kretschner coupling to tensor norm)"],
        ghost_status="ghost_risky",
        mode_modification=(
            "K is a scalar, so K * Phi_ab Phi^ab shifts the mass of ALL sectors "
            "equally: delta_m^2 ~ xi_K * K for scalar, vector, and tensor alike. "
            "This does NOT produce differential mass splitting between spin sectors. "
            "If xi_K < 0: all modes become tachyonic simultaneously at high curvature. "
            "If xi_K > 0: all modes gain mass simultaneously. "
            "Neither case opens the vector sector selectively. "
            "The Kretschner scalar is a scalar invariant and cannot distinguish "
            "between spin-0, spin-1, and spin-2 components of Phi_ab."
        ),
        vector_sector_effect=(
            "Mass shift is universal across all sectors. No selective vector "
            "deployment. If tachyonic: all sectors go tachyonic simultaneously, "
            "which is a general instability, not a vector-specific effect."
        ),
        verdict="fails",
        reasoning=(
            "Kretschner-scalar coupling K * Phi_ab*Phi^ab is a scalar coupling "
            "that treats all spin sectors of the tensor equally. It cannot produce "
            "the differential mass splitting needed to selectively open the vector "
            "sector. Any instability it produces affects all modes equally, which "
            "does not generate an effective triplet. This is consistent with D10's "
            "trigger mechanism (K-based) operating on the scalar sector; the same "
            "scalar-valued trigger cannot selectively deploy one spin sector."
        ),
    ))

    # Candidate B4: Weyl-tidal electric coupling (spin-selective)
    candidates.append(NonMinimalActionCandidate(
        name="Weyl electric tidal coupling: E_ij decomposition",
        coupling_type="weyl_tensor",
        action_term=(
            "S_tidal = xi_E * integral sqrt(-g) E_ij sigma^ij, "
            "where E_ij = C_{0i0j} is the electric part of the Weyl tensor "
            "and sigma^ij is the traceless spatial part of Phi_ab. "
            "This couples only the tensor sector to the tidal field."
        ),
        inherited_content=[
            "Traceless tensor sigma_ij from rank-2 decomposition",
            "Electric tidal tensor E_ij from Schwarzschild Weyl tensor",
        ],
        new_completion_content=[
            "Tidal-tensor coupling xi_E",
            "3+1 decomposition fixing (foliation dependence)",
        ],
        coupling_parameters=["xi_E (tidal-tensor coupling)"],
        ghost_status="undecidable",
        mode_modification=(
            "E_ij sigma^ij couples only to the spin-2 traceless sector, "
            "NOT to the vector sector. The 3+1 decomposition of the Weyl-Phi-Phi "
            "term yields: electric E_ij couples to sigma_ij (tensor-tensor), "
            "and magnetic B_ij couples to a cross term (vector-tensor mixing). "
            "However, the vector-tensor mixing via B_ij is a derivative coupling "
            "(involves gradients of v_i contracted with sigma_ij), not a mass term. "
            "In the FP framework where v_i is a constraint, this mixing does not "
            "restore the vector as a propagating mode. "
            "The electric tidal term E_ij*sigma^ij is purely tensor-sector."
        ),
        vector_sector_effect=(
            "Direct: none (E_ij couples to tensor sector only). "
            "Indirect: B_ij magnetic tidal provides vector-tensor derivative mixing, "
            "but this is a gradient coupling, not a mass term, and cannot overcome "
            "the FP constraint structure."
        ),
        verdict="fails",
        reasoning=(
            "The electric Weyl tidal coupling E_ij*sigma^ij acts only on the "
            "tensor (spin-2) sector. The magnetic component B_ij provides "
            "derivative mixing between vector and tensor sectors, but derivative "
            "coupling cannot convert a constraint equation (FP vector) into a "
            "dynamical equation. The tidal decomposition confirms that Weyl "
            "coupling does not selectively open the vector sector."
        ),
    ))

    # Candidate B5: Non-minimal Weyl coupling with non-FP mass (combined attempt)
    candidates.append(NonMinimalActionCandidate(
        name="Non-minimal Weyl coupling with relaxed (non-FP) mass structure",
        coupling_type="weyl_tensor",
        action_term=(
            "S_combined = S_kin[Phi_ab] + S_mass[non-FP, m_0 != m_2] "
            "+ xi_W * integral sqrt(-g) C_abcd Phi^ac Phi^bd. "
            "Combined: non-FP mass (vector active) + Weyl coupling (mass splitting). "
            "The non-FP mass activates the vector, and Weyl coupling provides "
            "differential mass shifts."
        ),
        inherited_content=[
            "Rank-2 Phi_ab, trace sector, background metric",
            "Weyl tensor, Kretschner from D10",
        ],
        new_completion_content=[
            "Non-FP mass term (m_0 != m_2)",
            "Weyl coupling xi_W",
            "Combined: 3 new parameters",
        ],
        coupling_parameters=["m_0 (scalar mass)", "m_2 (tensor mass)", "xi_W (Weyl coupling)"],
        ghost_status="ghost_present",
        mode_modification=(
            "Non-FP mass: activates vector sector (3 propagating DOF) but "
            "introduces Boulware-Deser ghost (scalar sector, wrong-sign kinetic). "
            "Weyl coupling: adds curvature-dependent mass splitting "
            "delta_m_v^2 ~ xi_W * M / r^3 to the vector sector. "
            "Combined effective vector mass: m_v^2(r) = m_2^2 + xi_W * C_terms(r). "
            "This CAN produce a curvature-triggered tachyonic vector mass. "
            "However, the ghost is STILL PRESENT regardless of the Weyl coupling. "
            "Non-minimal curvature coupling cannot cure the Boulware-Deser ghost "
            "because the ghost is a kinetic-structure problem (wrong-sign kinetic "
            "term for the scalar mode), not a mass/potential problem. "
            "Adding Weyl coupling to a ghostly theory gives a ghostly theory "
            "with curvature-dependent masses."
        ),
        vector_sector_effect=(
            "Vector is dynamically active AND curvature-sensitive. "
            "Weyl coupling can make vector tachyonic in strong curvature. "
            "BUT: the theory is sick (BD ghost). The vector deployment is "
            "technically present but in an unstable (ghostly) theory. "
            "The ghost energy is unbounded below; the vector tachyon triggers "
            "simultaneous scalar ghost runaway. Not physically meaningful."
        ),
        verdict="fails",
        reasoning=(
            "This is the strongest combined attempt: non-FP mass activates the "
            "vector, and Weyl coupling makes it curvature-sensitive with differential "
            "mass splitting. In principle this can produce a curvature-triggered "
            "vector tachyon. However, the Boulware-Deser ghost is incurable by "
            "non-minimal coupling. The ghost is a property of the kinetic structure "
            "(the specific combination of second-derivative terms), and no "
            "potential/mass/curvature-coupling modification can remove it. "
            "The only known ghost-free massive spin-2 theories are Fierz-Pauli "
            "(linearized) and de Rham-Gabadadze-Tolley (dRGT, nonlinear), "
            "both of which eliminate the vector sector as a constraint. "
            "Non-minimal curvature coupling cannot escape this dichotomy."
        ),
    ))

    # Candidate B6: Gauss-Bonnet family scalar-tensor coupling
    candidates.append(NonMinimalActionCandidate(
        name="Gauss-Bonnet family: G_4 * f(Phi) scalar-tensor coupling",
        coupling_type="gauss_bonnet_family",
        action_term=(
            "S_GB = integral sqrt(-g) f(Phi) * G_4, "
            "where G_4 = R^2 - 4 R_ab R^ab + R_abcd R^abcd is the Gauss-Bonnet "
            "invariant and f(Phi) = alpha_GB * Phi (scalar trace). "
            "In 4D, G_4 is topological when f = const, but dynamical when "
            "coupled to a scalar."
        ),
        inherited_content=[
            "Scalar Phi = trace of Phi_ab (existing memory field)",
            "Gauss-Bonnet invariant G_4 (computed from background metric)",
        ],
        new_completion_content=[
            "GB coupling coefficient alpha_GB",
            "Function f(Phi) choice",
        ],
        coupling_parameters=["alpha_GB (Gauss-Bonnet coupling)"],
        ghost_status="ghost_free",
        mode_modification=(
            "GB coupling f(Phi)*G_4 modifies the SCALAR sector equations of motion. "
            "It adds a term proportional to G_4 * f'(Phi) to the scalar EOM. "
            "This is a scalar-curvature coupling that affects only the trace Phi, "
            "not the vector or tensor sectors of Phi_ab. "
            "In the tensor memory context: the GB term is a scalar-sector effect. "
            "It does not open or modify the vector channel. "
            "GB coupling is known for its scalar-tensor gravity applications "
            "(Horndeski class) but is irrelevant for vector sector deployment."
        ),
        vector_sector_effect=(
            "None. Gauss-Bonnet coupling acts on the scalar sector only. "
            "It cannot promote, activate, or destabilize the vector sector."
        ),
        verdict="fails",
        reasoning=(
            "Gauss-Bonnet family couplings f(Phi)*G_4 are scalar-sector modifications "
            "that are structurally irrelevant for vector sector deployment. They are "
            "ghost-free and well-studied in scalar-tensor gravity, but they cannot "
            "address the spin-1 question because they couple only to the scalar trace "
            "of the memory tensor."
        ),
    ))

    return candidates


# ===================================================================
# Part C: Mode Decomposition and Effective Mass Analysis
# ===================================================================

def analyze_mode_decomposition(
    candidates: List[NonMinimalActionCandidate],
) -> ModeDecompositionD15:
    """Analyze the mode structure under non-minimal curvature coupling.

    For each spin sector, determine whether non-minimal coupling modifies
    the effective mass structure and whether the vector sector becomes
    dynamically available.
    """
    entries = [
        # Scalar trace
        ModeEffectiveMassEntry(
            mode_sector="scalar_trace",
            exists=True,
            curvature_sensitive=True,
            effective_mass_shift=(
                "Kretschner coupling (B3): delta_m^2 ~ xi_K * K = xi_K * 48*M^2/r^6. "
                "GB coupling (B6): adds G_4*f'(Phi) to EOM. "
                "Both affect scalar sector but are not relevant to O(3) question."
            ),
            instability_status="curvature_sensitive_stable",
            triplet_relevance="none -- this IS the existing scalar memory field",
            verdict="not_relevant",
            analysis=(
                "Non-minimal couplings can modify the scalar effective mass but "
                "this is the existing memory field. Stability is maintained for "
                "physical coupling values. Not relevant to triplet question."
            ),
        ),
        # Vector / spin-1 sector
        ModeEffectiveMassEntry(
            mode_sector="vector_spin1",
            exists=True,
            curvature_sensitive=True,
            effective_mass_shift=(
                "In FP framework: vector is constrained (not propagating). "
                "Weyl coupling (B1) modifies the constraint equation by "
                "delta_constraint ~ xi_W * E_ij * v^j but does NOT convert "
                "the constraint to a dynamical equation. The mass shift is "
                "formally delta_m_v^2 ~ -xi_W * M/r^3 but applies to a "
                "non-propagating mode. "
                "In non-FP framework (B5): vector propagates with effective mass "
                "m_v^2(r) = m_2^2 + xi_W * C_terms(r). Curvature-triggered "
                "tachyon possible but ghost is incurable."
            ),
            instability_status="curvature_sensitive_stable",
            triplet_relevance=(
                "The vector sector has 3 DOF (spatial SO(3) vector) which is "
                "formally the correct content for a triplet. However: "
                "(1) In ghost-free completions (FP, constrained): vector is not dynamical "
                "(2) In ghost-afflicted completions (non-FP): vector is dynamical but sick "
                "(3) Non-minimal curvature coupling cannot bridge this gap "
                "The curvature sensitivity of the vector effective mass IS real, "
                "but it operates on either a constraint mode or a ghostly mode. "
                "Neither case produces a physically meaningful triplet."
            ),
            verdict="curvature_sensitive_but_blocked",
            analysis=(
                "Non-minimal Weyl coupling introduces genuine curvature-dependent "
                "mass splitting between spin sectors. The vector effective mass IS "
                "modified by tidal curvature. This is a real physical effect. However, "
                "the D14 obstruction is kinetic-level (FP constraint structure), and "
                "non-minimal coupling is mass-level. Mass-level modifications cannot "
                "convert a constraint equation into a dynamical equation. "
                "The vector sector is curvature-sensitive but structurally blocked."
            ),
        ),
        # Tensor / spin-2 sector
        ModeEffectiveMassEntry(
            mode_sector="tensor_spin2",
            exists=True,
            curvature_sensitive=True,
            effective_mass_shift=(
                "Weyl coupling (B1,B4): delta_m_sigma^2 ~ xi_W * E_ij (tidal). "
                "Kretschner (B3): delta_m_sigma^2 ~ xi_K * K. "
                "Both modify the tensor sector effective mass. "
                "E_ij has anisotropic structure that splits tensor polarizations."
            ),
            instability_status="curvature_sensitive_stable",
            triplet_relevance="none -- spin-2 cannot serve as spin-1 triplet",
            verdict="not_relevant",
            analysis=(
                "The tensor sector gains curvature-dependent mass corrections from "
                "Weyl and Kretschner couplings. These could be relevant for "
                "gravitational-wave memory but not for the O(3) triplet question."
            ),
        ),
    ]

    # Overall vector assessment
    vector_entry = next(e for e in entries if e.mode_sector == "vector_spin1")

    return ModeDecompositionD15(
        entries=entries,
        vector_exists=vector_entry.exists,
        vector_curvature_sensitive=vector_entry.curvature_sensitive,
        vector_instability=vector_entry.instability_status,
        best_candidate_for_vector="B5_nonFP_plus_Weyl",
        summary=(
            "Non-minimal curvature coupling produces real, curvature-dependent mass "
            "splitting between spin sectors of the tensor memory. The vector effective "
            "mass IS modified by Weyl/tidal curvature. However, this is a mass-level "
            "effect operating on a mode whose dynamical status is determined by the "
            "kinetic structure. In all ghost-free completions, the vector is a "
            "constraint mode, and mass modifications cannot convert it to a dynamical "
            "mode. In ghost-afflicted completions, the vector is dynamical but the "
            "theory is sick. Non-minimal coupling does NOT resolve the D14 obstruction."
        ),
    )


# ===================================================================
# Part D: Strong-Curvature Instability / Deployment Test
# ===================================================================

def analyze_curvature_deployment(
    mode_decomp: ModeDecompositionD15,
    candidates: List[NonMinimalActionCandidate],
) -> Dict[str, Any]:
    """Analyze whether strong curvature can induce vector deployment.

    Returns a structured assessment of the deployment test.
    """
    # The relevant trigger quantity
    trigger_quantity = (
        "Weyl electric tidal: E_ij = C_{0i0j} = diag(2M/r^3, -M/r^3, -M/r^3). "
        "Grows as M/r^3 inward. Becomes large at r ~ R_S."
    )

    # Sign structure of effective mass shift
    sign_structure = (
        "For Weyl coupling B1: delta_m_v^2 ~ -xi_W * Tr(E_ij) = 0 (E_ij is traceless). "
        "The trace of the electric tidal tensor vanishes: this is a consequence of R_ab=0 "
        "in vacuum. The vector sector mass shift from Weyl coupling has ZERO net effect "
        "on the vector mass when summed over components, because E_ij is traceless. "
        "Individual components are shifted differently (radial vs tangential) but "
        "the net tachyonic trigger is absent. "
        "For non-FP + Weyl (B5): same sign structure applies; net effect zero on vector mass."
    )

    # Threshold / instability condition
    threshold_analysis = (
        "No threshold exists for vector instability via Weyl coupling alone because: "
        "(1) In FP: vector is constrained (no instability possible for a constraint). "
        "(2) In non-FP: the BD ghost instability dominates; any vector tachyon is "
        "    secondary to the ghost runaway. "
        "(3) The traceless property of E_ij means the net vector mass shift is zero. "
        "Conclusion: there is no curvature threshold for vector deployment via "
        "non-minimal Weyl coupling."
    )

    # Vector sector classification
    vector_classification = "curvature_sensitive_stable"

    return {
        "trigger_quantity": trigger_quantity,
        "sign_structure": sign_structure,
        "threshold_analysis": threshold_analysis,
        "vector_classification": vector_classification,
        "vector_deployed": False,
        "summary": (
            "The strong-curvature deployment test for the vector sector yields a "
            "negative result. The Weyl tensor's tracelessness (R_ab = 0 in vacuum) "
            "means the net effective mass shift on the vector sector from Weyl coupling "
            "vanishes when summed over components. Individual polarization splitting "
            "occurs but does not produce a net tachyonic instability. The vector "
            "sector is curvature-sensitive but NOT deployed. This closes the "
            "non-minimal Weyl coupling route for vector sector activation."
        ),
    }


# ===================================================================
# Part E: Support-Class Continuity Test
# ===================================================================

def analyze_support_class(
    mode_decomp: ModeDecompositionD15,
) -> SupportClassResult:
    """Test whether any induced vector structure has support-class continuity.

    Since the vector sector is not deployed, these tests evaluate the
    hypothetical support class assuming a vector were present.
    """
    tests = [
        SupportClassTest(
            test="Hedgehog configuration from Weyl-coupled vector",
            result=(
                "Not applicable. The vector sector is not deployed as a "
                "propagating mode in any ghost-free completion. A hedgehog "
                "requires a dynamical field with a VEV; a constraint mode "
                "or ghostly mode cannot support a hedgehog."
            ),
            strength="absent",
            comment=(
                "Support-class test is moot because the prerequisite "
                "(dynamical vector sector) is not achieved."
            ),
        ),
        SupportClassTest(
            test="Angular gradient energy ~ 1/r^2 from non-minimal coupling",
            result=(
                "If a dynamical vector v_i were present with Weyl-modified mass, "
                "the angular gradient energy would be eps ~ v^2/r^2 (same "
                "structure as standard hedgehog). But Weyl coupling does not "
                "deploy the vector, so this is hypothetical."
            ),
            strength="absent",
            comment=(
                "The 1/r^2 support class WOULD follow from a deployed vector "
                "hedgehog. The Weyl coupling does not obstruct the support class "
                "structure itself — it obstructs the deployment of the vector."
            ),
        ),
        SupportClassTest(
            test="D12 Q-ontology continuity with Weyl-coupled sector",
            result=(
                "Q = n*eta requires a topological charge n from a VEV eta. "
                "Without vector deployment, there is no VEV and no topological "
                "charge in the Weyl-coupled tensor sector."
            ),
            strength="absent",
            comment="No Q-ontology because no deployed vector sector.",
        ),
        SupportClassTest(
            test="Component B stress-energy from Weyl-modified tensor sector",
            result=(
                "The traceless tensor sector sigma_ij IS modified by Weyl coupling "
                "and does produce curvature-dependent stress-energy. However, "
                "sigma_ij is spin-2, not spin-1, and its stress-energy does not "
                "have the angular-gradient 1/r^2 structure of the hedgehog. "
                "Tensor stress-energy goes as ~ sigma^2/r^2 * (tidal structure), "
                "but this is an anisotropic tensor contribution, not a Component B "
                "support contribution."
            ),
            strength="fails",
            comment=(
                "Tensor sector stress-energy from Weyl coupling exists but does "
                "not match Component B support class. Wrong spin, wrong structure."
            ),
        ),
    ]

    overall = all(t.strength in ("exact", "strong") for t in tests)

    return SupportClassResult(
        tests=tests,
        overall_continuity=overall,
        summary=(
            "Support-class continuity fails across all tests because the vector "
            "sector is not deployed. The hedgehog, angular gradient energy, "
            "and Q-ontology all require a dynamical vector with a VEV, which "
            "non-minimal Weyl coupling does not produce. The tensor sector "
            "gains Weyl-modified stress-energy but this is spin-2, not spin-1, "
            "and does not match the Component B ~ 1/r^2 support class."
        ),
    )


# ===================================================================
# Part F: Eta Analysis
# ===================================================================

def analyze_eta(
    candidates: List[NonMinimalActionCandidate],
    mode_decomp: ModeDecompositionD15,
) -> EtaAnalysisResult:
    """Test whether non-minimal curvature coupling makes progress on eta."""
    entries = [
        EtaAnalysisEntry(
            mechanism="Weyl coupling mass splitting",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=True,
            outcome="matched_only",
            comment=(
                "Weyl coupling introduces xi_W but this parameter is independent "
                "of eta. The coupling strength xi_W relates Weyl curvature to "
                "tensor mass splitting, not to the defect VEV scale. "
                "No relationship between xi_W and eta = 1/sqrt(8*pi) is derivable."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="Kretschner coupling threshold",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=True,
            outcome="matched_only",
            comment=(
                "Kretschner coupling xi_K * K * Phi_ab*Phi^ab introduces a "
                "curvature-dependent mass but the threshold condition (if any) "
                "relates xi_K to geometric parameters (M, r), not to eta. "
                "eta remains a matched parameter of the defect sector, not "
                "derivable from curvature coupling."
            ),
        ),
        EtaAnalysisEntry(
            mechanism="Tidal-driven VEV from vector deployment",
            eta_derived=False,
            eta_constrained=False,
            eta_matched_only=True,
            outcome="fails",
            comment=(
                "If vector deployment had succeeded, one could ask whether the "
                "VEV scale is set by curvature parameters: eta^2 ~ M^2/(r^3 * xi_W). "
                "This would relate eta to xi_W and M, potentially constraining it. "
                "But vector deployment does not succeed, so this route is closed."
            ),
        ),
    ]

    # Find best outcome
    outcome_order = {v: i for i, v in enumerate(ETA_OUTCOMES)}
    best = min(entries, key=lambda e: outcome_order.get(e.outcome, 99))

    return EtaAnalysisResult(
        entries=entries,
        best_outcome=best.outcome,
        summary=(
            "Non-minimal curvature coupling makes no progress on eta. "
            "The coupling parameters (xi_W, xi_K) are structurally independent "
            "of the defect VEV scale eta. Even in the hypothetical scenario "
            "where vector deployment succeeded, eta would depend on additional "
            "parameters, not be derived from curvature coupling alone. "
            "eta remains matched only."
        ),
    )


# ===================================================================
# Part G: Comparison to D14
# ===================================================================

def compare_d14_d15(
    mode_decomp: ModeDecompositionD15,
    support_result: SupportClassResult,
    eta_result: EtaAnalysisResult,
) -> D14vsD15Comparison:
    """Compare D15 results to D14 baseline."""
    entries = [
        D14vsD15Entry(
            criterion="Vector sector status",
            d14_result="Constrained (FP) or ghostly (non-FP); structurally blocked",
            d15_result="Curvature-sensitive but still constrained (FP) or ghostly (non-FP)",
            upgrade=False,
            comment=(
                "Non-minimal coupling modifies vector effective mass but does not "
                "resolve the kinetic-level obstruction identified in D14."
            ),
        ),
        D14vsD15Entry(
            criterion="Ghost freedom",
            d14_result="FP ghost-free but no vector; non-FP has vector but ghost",
            d15_result="Same dichotomy persists; Weyl coupling cannot cure BD ghost",
            upgrade=False,
            comment="Ghost structure is a kinetic-level property, unaffected by mass-level coupling.",
        ),
        D14vsD15Entry(
            criterion="Curvature-triggered instability",
            d14_result="Not achieved; no curvature-dependent vector mass in minimal coupling",
            d15_result=(
                "Curvature-dependent mass splitting IS present from Weyl coupling, "
                "but applies to a constrained or ghostly mode"
            ),
            upgrade=False,
            comment=(
                "D15 adds curvature sensitivity but cannot deploy it productively "
                "because the underlying mode is not dynamical (FP) or is sick (non-FP)."
            ),
        ),
        D14vsD15Entry(
            criterion="Support-class continuity",
            d14_result="Fails; no deployed vector",
            d15_result="Fails; still no deployed vector",
            upgrade=False,
            comment="Support class requires deployed vector; both D14 and D15 fail.",
        ),
        D14vsD15Entry(
            criterion="Eta progress",
            d14_result="related_to_parameters; no derivation or constraint",
            d15_result="matched_only; no progress",
            upgrade=False,
            comment="Non-minimal coupling parameters are independent of eta.",
        ),
        D14vsD15Entry(
            criterion="Structural understanding of obstruction",
            d14_result="Identified: FP constraint vs ghost dichotomy",
            d15_result=(
                "Sharpened: the obstruction is KINETIC-LEVEL, not mass-level. "
                "Non-minimal coupling (mass-level) cannot overcome kinetic obstruction."
            ),
            upgrade=True,
            comment=(
                "D15 provides a conceptual upgrade: it clarifies WHY non-minimal "
                "curvature coupling cannot resolve the D14 obstruction. The FP "
                "constraint structure is determined by the kinetic term, and mass/ "
                "potential/coupling modifications cannot alter it."
            ),
        ),
    ]

    # Count upgrades
    n_upgrades = sum(1 for e in entries if e.upgrade)
    # Only structural understanding upgraded; no physical deployment
    if n_upgrades == 0:
        overall = "no_upgrade"
    elif n_upgrades <= 1 and not any(
        e.upgrade and "vector" in e.criterion.lower() for e in entries
    ):
        overall = "conceptual_only"
    else:
        overall = "opens_channel"

    return D14vsD15Comparison(
        entries=entries,
        overall_upgrade=overall,
        summary=(
            "D15 does NOT materially upgrade D14 in terms of vector deployment, "
            "instability, support-class continuity, or eta progress. "
            "D15 provides one conceptual upgrade: it sharpens the understanding "
            "that the D14 obstruction is kinetic-level (FP constraint structure), "
            "not mass-level, and therefore cannot be resolved by non-minimal "
            "curvature coupling of any form. This CLOSES the Weyl/non-minimal "
            "loophole as a derivation route for the O(3) sector, sharpening "
            "the boundary of the remaining derivation space."
        ),
    )


# ===================================================================
# Remaining Gaps
# ===================================================================

def identify_remaining_gaps(
    classification: D15Classification,
) -> List[FoundationalGap]:
    """Identify foundational gaps remaining after D15."""
    gaps = [
        FoundationalGap(
            gap="O(3) defect sector remains a principled extension, not derived",
            severity="critical",
            notes=(
                "D13 established partially_motivated_not_derived. "
                "D14 closed the minimal tensor-memory route. "
                "D15 closes the non-minimal curvature coupling route. "
                "The O(3) sector must still be introduced as an extension "
                "to the GRUT action, not derived from it."
            ),
        ),
        FoundationalGap(
            gap="All rank-2 tensor-memory routes to O(3) induction are now exhausted",
            severity="critical",
            notes=(
                "Minimal completions (D14): blocked by FP constraint or ghost. "
                "Non-minimal curvature coupling (D15): blocked because mass-level "
                "coupling cannot overcome kinetic-level constraint. "
                "Remaining loopholes: (a) non-perturbative / lattice effects, "
                "(b) higher-spin / extended multiplet, (c) UV completion beyond "
                "effective field theory, (d) fundamentally new sector not related "
                "to tensor-memory decomposition."
            ),
        ),
        FoundationalGap(
            gap="eta = 1/sqrt(8*pi) remains a matched parameter",
            severity="significant",
            notes=(
                "Neither D14 nor D15 makes progress on deriving or constraining eta. "
                "eta is set by matching to the required Component B support class "
                "coefficient. Its value has no derivation from within GRUT."
            ),
        ),
        FoundationalGap(
            gap="Empirical confrontation of the strong-field interior not achieved",
            severity="critical",
            notes=(
                "Independent of the O(3) derivation question, the strong-field "
                "interior predictions (ringdown modification, echo channel, "
                "tidal deformability) have not been confronted with observation."
            ),
        ),
    ]
    return gaps


# ===================================================================
# Classification Logic
# ===================================================================

def classify_d15(
    mode_decomp: ModeDecompositionD15,
    support_result: SupportClassResult,
    eta_result: EtaAnalysisResult,
    comparison: D14vsD15Comparison,
) -> D15Classification:
    """Compute the final D15 classification from explicit criteria.

    Classification logic:
    - vector_channel_opened: True if vector sector becomes dynamical and ghost-free
    - instability_achieved: True if curvature triggers vector instability productively
    - support_class_continuity: True if deployed sector has Component B ~ 1/r^2
    - eta_progress: True if eta is derived or constrained (not just matched)

    Score:
    - 0 criteria met: nonminimal_curvature_route_fails
    - 1 criterion met: nonminimal_curvature_route_suggestive_only
    - 2 criteria met: nonminimal_curvature_route_opens_vector_channel
    - 3 criteria met: nonminimal_curvature_route_strongly_induces_effective_triplet
    - 4 criteria met: nonminimal_curvature_route_derives_effective_O3_sector
    """
    # Evaluate each criterion
    vector_opened = (
        mode_decomp.vector_exists
        and mode_decomp.vector_instability in ("weakly_unstable", "strongly_unstable", "derivationally_decisive")
    )
    instability_achieved = mode_decomp.vector_instability in (
        "strongly_unstable", "derivationally_decisive"
    )
    support_continuity = support_result.overall_continuity
    eta_progress = eta_result.best_outcome in ("derived", "constrained")

    score = sum([vector_opened, instability_achieved, support_continuity, eta_progress])

    classification_map = {
        0: "nonminimal_curvature_route_fails",
        1: "nonminimal_curvature_route_suggestive_only",
        2: "nonminimal_curvature_route_opens_vector_channel",
        3: "nonminimal_curvature_route_strongly_induces_effective_triplet",
        4: "nonminimal_curvature_route_derives_effective_O3_sector",
    }

    classification = classification_map[score]

    # Justification
    justification = (
        f"D15 classification: {classification}. "
        f"Criteria met: {score}/4. "
        f"vector_channel_opened={vector_opened}, "
        f"instability_achieved={instability_achieved}, "
        f"support_class_continuity={support_continuity}, "
        f"eta_progress={eta_progress}. "
        "Non-minimal Weyl/tidal curvature coupling produces real curvature-dependent "
        "mass splitting in the tensor-memory sector, but this is a mass-level effect "
        "that cannot overcome the kinetic-level FP constraint structure identified in D14. "
        "The Weyl coupling loophole is CLOSED: non-minimal curvature coupling of any "
        "form cannot resolve the vector deployment obstruction."
    )

    return D15Classification(
        classification=classification,
        justification=justification,
        vector_channel_opened=vector_opened,
        instability_achieved=instability_achieved,
        support_class_continuity=support_continuity,
        eta_progress=eta_progress,
        upgrade_over_d14=comparison.overall_upgrade,
    )


# ===================================================================
# Nonclaims
# ===================================================================

D15_NONCLAIMS = [
    "D15 does not claim that non-minimal curvature coupling is irrelevant to GRUT; "
    "it is irrelevant specifically for the vector sector deployment question.",

    "D15 does not claim that the tensor memory sector gains nothing from Weyl coupling; "
    "the tensor (spin-2) sector gains curvature-dependent mass splitting that may be "
    "relevant for gravitational-wave memory effects.",

    "D15 does not claim to have exhausted ALL possible O(3) derivation routes; "
    "it closes the non-minimal curvature coupling route specifically. Remaining "
    "loopholes include non-perturbative effects, higher-spin content, UV completion, "
    "and fundamentally new sectors.",

    "D15 does not claim that the O(3) sector is wrong or unnecessary; "
    "it remains a principled extension (D12, D13 level) that must be introduced "
    "rather than derived from the tensor memory.",

    "D15 does not prove that the kinetic-mass level separation is absolute in all "
    "possible extensions; non-perturbative or strongly-coupled regimes might blur "
    "this distinction. D15 operates within the perturbative effective field theory "
    "framework.",

    "D15 does not address whether the dRGT (de Rham-Gabadadze-Tolley) nonlinear "
    "massive gravity completion could change the picture. dRGT is ghost-free and "
    "nonlinear, but its vector sector structure has the same constraint property as FP.",

    "D15 does not claim that Weyl-tensor physics is unimportant for GRUT; "
    "tidal effects enter the D10 trigger mechanism and the D11 two-field structure. "
    "The negative result is specifically about using Weyl coupling to DEPLOY a "
    "vector sector from the tensor memory.",
]


# ===================================================================
# Master Computation
# ===================================================================

def compute_weyl_coupling_result() -> D15Result:
    """Execute the full D15 analysis.

    Returns
    -------
    D15Result
        Complete result object with all components.
    """
    # Part B: Build candidates
    candidates = build_nonminimal_candidates()

    # Part C: Mode decomposition
    mode_decomp = analyze_mode_decomposition(candidates)

    # Part D: Curvature deployment (integrated into mode analysis)
    deployment = analyze_curvature_deployment(mode_decomp, candidates)

    # Part E: Support-class continuity
    support_result = analyze_support_class(mode_decomp)

    # Part F: Eta analysis
    eta_result = analyze_eta(candidates, mode_decomp)

    # Part G: D14 comparison
    comparison = compare_d14_d15(mode_decomp, support_result, eta_result)

    # Classification
    classification = classify_d15(mode_decomp, support_result, eta_result, comparison)

    # Remaining gaps
    remaining_gaps = identify_remaining_gaps(classification)

    return D15Result(
        valid=True,
        action_candidates=candidates,
        mode_decomposition=mode_decomp,
        support_class_result=support_result,
        eta_analysis=eta_result,
        d14_comparison=comparison,
        classification=classification,
        remaining_gaps=remaining_gaps,
        nonclaims=D15_NONCLAIMS,
    )


# ===================================================================
# Serialization
# ===================================================================

def _candidate_to_dict(c: NonMinimalActionCandidate) -> Dict[str, Any]:
    return {
        "name": c.name,
        "coupling_type": c.coupling_type,
        "action_term": c.action_term,
        "inherited_content": c.inherited_content,
        "new_completion_content": c.new_completion_content,
        "coupling_parameters": c.coupling_parameters,
        "ghost_status": c.ghost_status,
        "mode_modification": c.mode_modification,
        "vector_sector_effect": c.vector_sector_effect,
        "verdict": c.verdict,
        "reasoning": c.reasoning,
    }


def _mode_entry_to_dict(e: ModeEffectiveMassEntry) -> Dict[str, Any]:
    return {
        "mode_sector": e.mode_sector,
        "exists": e.exists,
        "curvature_sensitive": e.curvature_sensitive,
        "effective_mass_shift": e.effective_mass_shift,
        "instability_status": e.instability_status,
        "triplet_relevance": e.triplet_relevance,
        "verdict": e.verdict,
    }


def _support_test_to_dict(t: SupportClassTest) -> Dict[str, Any]:
    return {
        "test": t.test,
        "result": t.result,
        "strength": t.strength,
        "comment": t.comment,
    }


def _eta_entry_to_dict(e: EtaAnalysisEntry) -> Dict[str, Any]:
    return {
        "mechanism": e.mechanism,
        "eta_derived": e.eta_derived,
        "eta_constrained": e.eta_constrained,
        "eta_matched_only": e.eta_matched_only,
        "outcome": e.outcome,
        "comment": e.comment,
    }


def _d14_comparison_entry_to_dict(e: D14vsD15Entry) -> Dict[str, Any]:
    return {
        "criterion": e.criterion,
        "d14_result": e.d14_result,
        "d15_result": e.d15_result,
        "upgrade": e.upgrade,
        "comment": e.comment,
    }


def _gap_to_dict(g: FoundationalGap) -> Dict[str, Any]:
    return {"gap": g.gap, "severity": g.severity, "notes": g.notes}


def d15_result_to_dict(result: D15Result) -> Dict[str, Any]:
    """Serialize D15Result to dict for JSON export."""
    return {
        "valid": result.valid,
        "action_candidates": [_candidate_to_dict(c) for c in result.action_candidates],
        "mode_decomposition": {
            "entries": [_mode_entry_to_dict(e) for e in result.mode_decomposition.entries],
            "vector_exists": result.mode_decomposition.vector_exists,
            "vector_curvature_sensitive": result.mode_decomposition.vector_curvature_sensitive,
            "vector_instability": result.mode_decomposition.vector_instability,
            "best_candidate_for_vector": result.mode_decomposition.best_candidate_for_vector,
            "summary": result.mode_decomposition.summary,
        },
        "support_class_result": {
            "tests": [_support_test_to_dict(t) for t in result.support_class_result.tests],
            "overall_continuity": result.support_class_result.overall_continuity,
            "summary": result.support_class_result.summary,
        },
        "eta_analysis": {
            "entries": [_eta_entry_to_dict(e) for e in result.eta_analysis.entries],
            "best_outcome": result.eta_analysis.best_outcome,
            "summary": result.eta_analysis.summary,
        },
        "d14_comparison": {
            "entries": [_d14_comparison_entry_to_dict(e) for e in result.d14_comparison.entries],
            "overall_upgrade": result.d14_comparison.overall_upgrade,
            "summary": result.d14_comparison.summary,
        },
        "classification": {
            "classification": result.classification.classification,
            "justification": result.classification.justification,
            "vector_channel_opened": result.classification.vector_channel_opened,
            "instability_achieved": result.classification.instability_achieved,
            "support_class_continuity": result.classification.support_class_continuity,
            "eta_progress": result.classification.eta_progress,
            "upgrade_over_d14": result.classification.upgrade_over_d14,
        },
        "remaining_gaps": [_gap_to_dict(g) for g in result.remaining_gaps],
        "nonclaims": result.nonclaims,
    }


def d15_result_to_json(result: D15Result) -> str:
    """Serialize D15Result to JSON string."""
    return json.dumps(d15_result_to_dict(result), indent=2)
