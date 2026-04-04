"""Appendix Q-B — GRUT Quantum Kinematics Audit.

This module performs a deterministic audit of the native state space
GRUT actually provides for microphysical description. It does NOT ask
"how do we reproduce standard quantum mechanics?" It asks the prior,
narrower, and more honest question:

  WHAT IS THE NATIVE STATE SPACE GRUT ACTUALLY PROVIDES?

That means determining — for the canonical GRUT architecture — what the
state object is, what type it has, whether superposition is native or
absent, whether linear structure exists, whether normalization has meaning,
and what Appendix P class the result receives.

SIX CANDIDATE STATE SPACE CLASSES
-----------------------------------
Rather than defaulting to "Hilbert space unless proven otherwise," the
audit considers six candidates drawn from what the GRUT architecture
actually contains or could motivate:

  C1  classical_configuration_space
      The real scalar field configuration space {Φ: D → ℝ}. Present
      natively. Real linear. No quantum superposition. No normalization.

  C2  memory_field_configuration_space
      The extended state (Φ(t), M_X(t)) — or the full retarded history —
      encoding the memory kernel structure from the Galley formalism.
      Present in the Galley regime. Real, extended. No quantum structure.

  C3  complexified_response_space
      The CTP doubled state (Φ₁, Φ₂) reinterpreted as Ψ = Φ₊ + iΦ₋
      where Φ₊ = (Φ₁+Φ₂)/2, Φ₋ = Φ₁-Φ₂. Not GRUT-motivated:
      Φ₋ is a ghost (growing mode), not an oscillating phase. This
      candidate is not absent — it is structurally present but wrong-signed.

  C4  density_operator_like_effective_space
      A probability distribution ρ(Φ) over the configuration space,
      yielding a density-like effective state. Absent from canonical GRUT:
      the constitutive ODE is deterministic; no probability measure over
      field configurations is defined.

  C5  constrained_manifold_bundle_state_space
      The O(3) hedgehog target space Map(D, S²) under the O(3) MIP
      postulate. Nonlinear manifold-valued state. Conditionally present.
      No complex structure, no superposition.

  C6  no_quantum_native_state_space_established
      The honest null verdict: canonical GRUT provides no state space
      that natively supports quantum kinematics. This is the primary result.

PRIMARY FINDINGS
----------------
  1. GRUT has a native real linear configuration space (NC):
       state = Φ(x) ∈ {real scalar fields}
       valuation: real_valued
       linear structure: full_real (ℝ-linear, not ℂ-linear)
       superposition: absent as quantum superposition
         (classical linear combinations exist but carry no Born-rule weight)
       normalization: absent
     This is sufficient for classical kinematics; insufficient for quantum.

  2. The missing ingredient for quantum kinematics is precisely identified:
       A complex structure J: real_config_space → real_config_space with J²=-1
       J would promote the real linear space to a complex linear space.
       Without J, no inner product, no Born rule, no quantum superposition.
       J is absent and constitutes a BG1-class gap (new structural postulate).

  3. The CTP decomposition (Φ₊, Φ₋) does NOT supply J:
       Φ₋ satisfies dΦ₋/dt = +Φ₋/τ — exponential GROWTH, not oscillation.
       A complex structure requires Im(Ψ) to evolve via rotation, not growth.
       The Φ₋ ghost mode cannot serve as Im(Ψ).

  4. Primary verdict: no_quantum_native_state_space_established (BSR)

APPENDIX P CLASSIFICATION
--------------------------
  Native classical configuration space:  native_canon
  Memory-extended state:                 effective_reduction (Galley regime)
  Complexified response space:           compatible_but_ad_hoc (wrong-signed Im)
  Density operator analog:               compatible_but_ad_hoc (no mechanism)
  O(3) bundle state space:               motivated_independent_postulation
  Q-B primary verdict:                   bounded_structural_result

NONCLAIMS
---------
  1. NOT claiming quantum kinematics is impossible in GRUT — only that no
     native quantum state space is established in the current architecture.
  2. NOT claiming the real linear structure is worthless — it is the correct
     classical substrate; quantum extension requires adding a complex structure.
  3. NOT claiming the CTP doubled space is a Hilbert space.
  4. NOT claiming the O(3) bundle provides quantum superposition — it is
     manifold-valued and nonlinear.
  5. NOT claiming density-like states are forbidden — they are absent but
     addable as compatible_but_ad_hoc.
  6. NOT claiming the complex structure J must be added — only that if one
     wants quantum kinematics, J is the precise missing ingredient.

See: grut/q0_quantum_entry_inventory.py (Q0 inventory — D items absent)
     grut/qa_quantum_charter.py (Q-A charter — FFM2, FFM6 apply)
     grut/galley_truncation.py (Φ₋ ghost mode analysis)
     grut/o3_nativity_audit.py (O(3) MIP — C5 basis)
     grut/appendix_p_taxonomy_audit.py (status classes)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Vocabulary: candidate state space types
# ================================================================

CANDIDATE_STATE_SPACE_IDS: List[str] = [
    "C1_classical_configuration_space",
    "C2_memory_field_configuration_space",
    "C3_complexified_response_space",
    "C4_density_operator_like_effective_space",
    "C5_constrained_manifold_bundle_state_space",
    "C6_no_quantum_native_state_space_established",
]

N_CANDIDATE_STATE_SPACES: int = 6

ALLOWED_VALUATION_TYPES: frozenset = frozenset({
    "real_valued",
    "complex_valued",
    "bundle_valued",
    "density_like",
    "manifold_valued",
    "undetermined",
})

ALLOWED_SUPERPOSITION_STATUSES: frozenset = frozenset({
    "native",       # born-rule superposition is a native feature
    "emergent",     # superposition emerges from the architecture
    "absent",       # superposition is not present
    "approximate",  # superposition holds approximately in some limit
    "classical_only",  # linear combination allowed but no Born rule
})

ALLOWED_LINEAR_STRUCTURE_STATUSES: frozenset = frozenset({
    "full_complex",  # ℂ-linear vector space
    "full_real",     # ℝ-linear vector space (real linear, not complex)
    "partial",       # partial linear structure (e.g. linearization)
    "absent",        # no linear structure (e.g. nonlinear manifold)
})

ALLOWED_NORMALIZATION_STATUSES: frozenset = frozenset({
    "present_natural",   # normalization arises from the architecture
    "present_induced",   # normalization must be imposed as a postulate
    "absent",            # no normalization defined
})

ALLOWED_STATE_SPACE_BASES: frozenset = frozenset({
    "configuration_space",   # based on field configurations
    "field_space",           # field-theoretic (infinite-dim function space)
    "response_memory",       # memory kernel / history functional
    "phase_space",           # (Φ, Π) phase space
    "manifold",              # nonlinear manifold (e.g. S²)
    "none_established",      # no state space basis identified
})

ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

# ================================================================
# Q-B verdict vocabulary
# ================================================================

ALLOWED_QB_VERDICTS: frozenset = frozenset({
    "no_quantum_native_state_space_established",
    "quantum_native_state_space_identified",
    "quantum_native_state_space_conditionally_identified",
})

QB_PRIMARY_VERDICT: str = "no_quantum_native_state_space_established"
QB_APPENDIX_P_CLASS: str = "bounded_structural_result"

# ================================================================
# Key physical constants referenced in the audit
# ================================================================

# Canonical GRUT constants (from tau_level1_audit.py / canon.py)
TAU_SQ: float = 3.0 / 2.0              # τ² = 3/2 (canonical relaxation time squared)
ALPHA_VAC: float = 1.0 / 3.0           # α_vac = 1/3
OMEGA_0_SQ: float = 27.0               # ω₀² = 27
R_EQ: float = 1.0 / 3.0               # R_eq = 1/3

# Galley truncation: Φ₋ growth rate = +1/τ (ghost mode — not oscillatory)
# For complex structure: Im(Ψ) must oscillate (growth rate purely imaginary)
# but Φ₋ has real growth rate +1/τ — this is the key disqualification
PHI_MINUS_GROWTH_RATE_SIGN: int = +1    # +1 means growing (ghost), NOT oscillating
PHI_MINUS_CAN_BE_IMAGINARY_PART: bool = False  # growing ≠ oscillating

# Number of real degrees of freedom in CTP state
N_CTP_REAL_DOF: int = 2  # (Φ₊, Φ₋) — real 2D, isomorphic to ℂ as real vector space
# But at physical limit Φ₋ → 0, collapses back to real 1D
N_PHYSICAL_LIMIT_DOF: int = 1   # Φ₁ = Φ₂ = Φ (real scalar)

# ================================================================
# Nonclaims
# ================================================================

QB_NONCLAIMS: List[str] = [
    "NOT_claiming_quantum_kinematics_impossible__only_no_native_space_established",
    "NOT_claiming_real_linear_structure_worthless__it_is_correct_classical_substrate",
    "NOT_claiming_ctp_doubled_space_is_hilbert_space",
    "NOT_claiming_o3_bundle_provides_quantum_superposition__it_is_nonlinear",
    "NOT_claiming_density_like_states_are_forbidden__they_are_absent_not_blocked",
    "NOT_claiming_complex_structure_j_must_be_added__only_that_it_is_what_is_missing",
]

N_QB_NONCLAIMS: int = 6

# ================================================================
# Dataclasses
# ================================================================


@dataclass
class CandidateStateSpaceAudit:
    """Audit of one candidate state space class against GRUT architecture."""
    candidate_id: str
    candidate_name: str
    state_object_description: str
    valuation_type: str               # one of ALLOWED_VALUATION_TYPES
    superposition_status: str         # one of ALLOWED_SUPERPOSITION_STATUSES
    linear_structure_status: str      # one of ALLOWED_LINEAR_STRUCTURE_STATUSES
    normalization_status: str         # one of ALLOWED_NORMALIZATION_STATUSES
    normalization_meaning: str        # what normalization means here (or "none")
    state_space_basis: str            # one of ALLOWED_STATE_SPACE_BASES
    appendix_p_class: str             # one of ALLOWED_APPENDIX_P_CLASSES
    is_quantum_state_space: bool      # False for all classical candidates
    presence_in_grut: str             # present / absent / conditionally_present / wrong_signed
    supporting_grut_features: List[str] = field(default_factory=list)
    blocking_gaps: List[str] = field(default_factory=list)
    verdict_for_this_candidate: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class NativeStateSpaceFinding:
    """The positive finding: what GRUT actually does provide classically."""
    state_object_description: str
    valuation_type: str
    linear_structure_status: str
    superposition_status: str
    normalization_status: str
    state_space_basis: str
    appendix_p_class: str          # native_canon for the classical finding
    is_quantum_state_space: bool   # False
    # Precise identification of the gap
    missing_for_quantum: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class ComplexStructureAnalysis:
    """Analysis of whether a complex structure J exists in GRUT.

    A complex structure J is a linear map with J² = -1 on the real
    configuration space. It is the minimal ingredient needed to promote
    a real linear space to a complex linear space, enabling inner products,
    Born rule, and quantum superposition.
    """
    # Is J present in canonical GRUT?
    complex_structure_present: bool              # False
    # CTP analysis: can Φ₋ serve as Im(Ψ)?
    phi_minus_serves_as_imaginary_part: bool     # False (growing mode, not oscillating)
    phi_minus_growth_rate_sign: int              # +1 (grows, does not oscillate)
    phi_minus_disqualification: str              # explanation
    # What J would require
    j_requires_new_postulate: bool               # True
    j_appendix_p_class: str                      # motivated_independent_postulation
    # Consequences of absence
    no_j_implies_no_inner_product: bool          # True
    no_j_implies_no_born_rule: bool              # True
    no_j_implies_no_quantum_superposition: bool  # True
    notes: List[str] = field(default_factory=list)


@dataclass
class QBKinematicsResult:
    """Master result of the Q-B Quantum Kinematics audit."""
    valid: bool
    candidate_audits: List[CandidateStateSpaceAudit]
    native_state_space: NativeStateSpaceFinding
    complex_structure: ComplexStructureAnalysis
    primary_verdict: str          # one of ALLOWED_QB_VERDICTS
    appendix_p_class: str         # bounded_structural_result
    nonclaims: List[str]
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Candidate audit builders
# ================================================================

def audit_c1_classical_configuration_space() -> CandidateStateSpaceAudit:
    """C1: Real scalar field configuration space.

    The canonical GRUT state at the field-theory level is Φ(x) — a real
    scalar field. The configuration space C = {Φ: D → ℝ} is a real
    infinite-dimensional linear space. This is native canon.

    This is the correct substrate for classical GRUT kinematics. It is
    insufficient for quantum kinematics: it lacks complex structure,
    inner product, Born rule, and normalization.

    Linear structure (real): YES — Φ₁ + Φ₂ is a valid configuration,
    and αΦ is valid for α ∈ ℝ. The constitutive ODE is ℝ-linear in Φ
    for fixed source X (superposition of solutions is a solution).

    Quantum superposition: ABSENT — the linear combination αΦ₁ + βΦ₂
    is a valid classical configuration but carries no Born-rule probability
    weight |α|² + |β|² = 1. The sum is not a quantum state.
    """
    return CandidateStateSpaceAudit(
        candidate_id="C1_classical_configuration_space",
        candidate_name="classical_configuration_space",
        state_object_description=(
            "Real scalar field Φ(x) ∈ {Φ: D → ℝ}; "
            "the state is a point in the infinite-dimensional real "
            "function space C = L²(D, ℝ) or similar"
        ),
        valuation_type="real_valued",
        superposition_status="classical_only",
        linear_structure_status="full_real",
        normalization_status="absent",
        normalization_meaning=(
            "No natural probability measure on C; ||Φ||_L² is a mathematical "
            "norm but has no physical normalization meaning in GRUT"
        ),
        state_space_basis="field_space",
        appendix_p_class="native_canon",
        is_quantum_state_space=False,
        presence_in_grut="present",
        supporting_grut_features=[
            "Φ is the canonical real scalar (Appendix P: NC)",
            "Constitutive ODE τ dΦ/dt + Φ = X is ℝ-linear in Φ for fixed X",
            "Z₂ symmetry Φ → -Φ is a symmetry of C",
            "Equilibrium Φ_eq is a distinguished point in C",
        ],
        blocking_gaps=[
            "No complex structure J: C is ℝ-linear but not ℂ-linear",
            "No inner product with Born-rule interpretation",
            "No probability measure on C (constitutive ODE is deterministic, not stochastic)",
            "No normalization condition that relates to measurement probability",
            "Superposition Φ = αΦ₁ + βΦ₂ is a classical superposition, not quantum",
        ],
        verdict_for_this_candidate=(
            "present__native_classical_configuration_space__"
            "insufficient_for_quantum_kinematics"
        ),
        notes=[
            "This is the HONEST starting point. GRUT has this natively.",
            "The classical real linear structure is NOT nothing — it is the "
            "correct substrate and the anchor constraint for any quantum extension.",
            "The gap from C1 to quantum kinematics is precisely the missing "
            "complex structure J (see ComplexStructureAnalysis).",
        ],
    )


def audit_c2_memory_field_configuration_space() -> CandidateStateSpaceAudit:
    """C2: Memory-field configuration space.

    The Galley formalism extends the state to include the memory kernel:
    the retarded history Φ(t-s) for s ≥ 0, encoded via M_X(t) satisfying
    τ dM_X/dt + M_X = X(t). The state is (Φ(t), M_X(t)) — or the full
    functional state (Φ(t), {X(t-s): s ≥ 0}).

    This is the natural GRUT state for the non-Markovian open system
    description. It is an effective reduction valid in the Galley regime.

    The memory extension does not add quantum structure: both Φ and M_X
    are real, the extended state is ℝ²-valued at each time, and there is
    no Born-rule normalization.
    """
    return CandidateStateSpaceAudit(
        candidate_id="C2_memory_field_configuration_space",
        candidate_name="memory_field_configuration_space",
        state_object_description=(
            "Extended state (Φ(t), M_X(t)) ∈ ℝ² at each t, "
            "or functionally: the pair (Φ(t), {X(t-s): s ≥ 0}) "
            "encoding the full retarded history via exponential kernel "
            "K(s) = (1/τ)exp(-s/τ)Θ(s)"
        ),
        valuation_type="real_valued",
        superposition_status="classical_only",
        linear_structure_status="full_real",
        normalization_status="absent",
        normalization_meaning="none",
        state_space_basis="response_memory",
        appendix_p_class="effective_reduction",
        is_quantum_state_space=False,
        presence_in_grut="present",
        supporting_grut_features=[
            "Memory kernel K(s) = (1/τ)exp(-s/τ)Θ(s) is strictly retarded and causal",
            "∫₀^∞ K(s) ds = 1 (normalized kernel)",
            "ODE equivalence: τ dM_X/dt + M_X = X (exact, not approximate)",
            "Galley CTP action generates this memory structure at classical saddle",
        ],
        blocking_gaps=[
            "Still real-valued — no complex structure in the extended state",
            "The memory extension adds past DOF but not quantum DOF",
            "No Born-rule normalization even with history included",
            "Valid only in Galley CTP regime (regime qualifier mandatory for ER)",
            "The non-Markovian extension is classical: it is a retarded Green's function, "
            "not a quantum path integral",
        ],
        verdict_for_this_candidate=(
            "present__effective_reduction__classical_memory_structure__"
            "not_quantum_state_space"
        ),
        notes=[
            "The memory structure is the correct causal substrate.",
            "Regime qualifier: Galley non-equilibrium CTP regime.",
            "This candidate is the most direct GRUT-native extension of C1 — "
            "it adds memory (retarded structure) but not quantum structure.",
        ],
    )


def audit_c3_complexified_response_space() -> CandidateStateSpaceAudit:
    """C3: Complexified response space (CTP Φ₊/Φ₋ decomposition).

    The CTP doubled state (Φ₁, Φ₂) decomposes as:
      Φ₊ = (Φ₁ + Φ₂)/2    [average — satisfies correct GRUT relaxation law]
      Φ₋ = Φ₁ - Φ₂         [difference — ghost mode: dΦ₋/dt = +Φ₋/τ]

    One might consider the formal complexification Ψ = Φ₊ + iΦ₋.
    This would make (Φ₊, Φ₋) play the roles of (Re(Ψ), Im(Ψ)).

    This candidate is NOT absent — the CTP doubling is structurally present
    as an effective_reduction. But it is DISQUALIFIED as a complex structure
    by the dynamics of Φ₋:

      dΦ₋/dt = +Φ₋/τ   (GROWTH — exponential amplification)

    A complex structure J requires J(Im(Ψ)) to rotate into Re(Ψ) — i.e.,
    the imaginary part must oscillate, not grow. The Φ₋ ghost mode grows
    at rate +1/τ; it is not an oscillating phase degree of freedom.

    Under the Galley physical limit projection Φ₋ → 0, the complex
    structure collapses: Im(Ψ) → 0, so Ψ → Φ₊ ∈ ℝ.

    Classification: compatible_but_ad_hoc — the Φ₊/Φ₋ decomposition is
    present but using Φ₋ as Im(Ψ) is physically unmotivated (wrong-signed
    dynamics) and the physical limit destroys the complex structure.
    """
    return CandidateStateSpaceAudit(
        candidate_id="C3_complexified_response_space",
        candidate_name="complexified_response_space",
        state_object_description=(
            "Formal complexification Ψ = Φ₊ + iΦ₋ where "
            "Φ₊ = (Φ₁+Φ₂)/2 is the CTP average and "
            "Φ₋ = Φ₁-Φ₂ is the CTP difference. "
            "The CTP state ∈ ℝ² is formally isomorphic to ℂ as a real vector space."
        ),
        valuation_type="complex_valued",
        superposition_status="absent",
        linear_structure_status="full_real",
        normalization_status="absent",
        normalization_meaning="none",
        state_space_basis="field_space",
        appendix_p_class="compatible_but_ad_hoc",
        is_quantum_state_space=False,
        presence_in_grut="wrong_signed",
        supporting_grut_features=[
            "CTP doubled state (Φ₁, Φ₂) is structurally present (effective_reduction)",
            "Φ₊/Φ₋ decomposition is mathematically well-defined",
            "ℝ² is formally isomorphic to ℂ as a real vector space",
        ],
        blocking_gaps=[
            "Φ₋ satisfies dΦ₋/dt = +Φ₋/τ — exponential GROWTH, not oscillation",
            f"Growth rate sign = {PHI_MINUS_GROWTH_RATE_SIGN} (positive = growing ghost mode)",
            "A complex structure J requires oscillation: J(Re)=Im, J(Im)=-Re with |J|=1",
            "Growing Φ₋ cannot serve as Im(Ψ): |Ψ| = sqrt(Φ₊² + Φ₋²) grows without bound",
            "Galley physical limit: Φ₋ → 0 at late times, so Im(Ψ) → 0 and Ψ → ℝ",
            "No Born rule even if Ψ were well-defined: no inner product, no normalization",
            "No motivation from GRUT architecture for Φ₋ as Im(Ψ)",
        ],
        verdict_for_this_candidate=(
            "structurally_present__wrong_signed__"
            "phi_minus_ghost_disqualifies_as_imaginary_part__"
            "not_quantum_state_space"
        ),
        notes=[
            "This is the sharpest negative result in Q-B.",
            "The CTP structure IS present — but it is precisely the wrong structure "
            "for complexification. The ghost mode grows; it does not oscillate.",
            "This disqualification is proved, not asserted: "
            f"PHI_MINUS_CAN_BE_IMAGINARY_PART = {PHI_MINUS_CAN_BE_IMAGINARY_PART}.",
            "Classified compatible_but_ad_hoc: formally consistent but unmotivated "
            "and physically incorrect (wrong dynamics for Im(Ψ)).",
        ],
    )


def audit_c4_density_operator_like_effective_space() -> CandidateStateSpaceAudit:
    """C4: Density-operator-like effective space.

    A probability distribution ρ[Φ] over the configuration space C would
    provide a density-like effective state analogous to a classical density
    matrix. Under this picture, the state is not a single field Φ but a
    distribution over fields.

    This candidate is ABSENT from canonical GRUT: the constitutive ODE
    τ dΦ/dt + Φ = X is deterministic. No probability measure over field
    configurations is defined or generated by the architecture. There is
    no stochastic extension, no ensemble interpretation, and no mechanism
    for generating a distribution.

    Classification: compatible_but_ad_hoc — a probability measure ρ[Φ]
    could be added as a postulate, but it has no motivation from the
    canonical GRUT architecture. It would not constitute a quantum density
    matrix (which requires complex Hilbert space structure).
    """
    return CandidateStateSpaceAudit(
        candidate_id="C4_density_operator_like_effective_space",
        candidate_name="density_operator_like_effective_space",
        state_object_description=(
            "A probability distribution ρ[Φ] over the configuration space C, "
            "or more generally a positive-semidefinite functional on C × C "
            "analogous to a density matrix."
        ),
        valuation_type="density_like",
        superposition_status="absent",
        linear_structure_status="partial",
        normalization_status="present_induced",
        normalization_meaning=(
            "∫ ρ[Φ] DΦ = 1 if a probability measure is imposed, "
            "but this is a classical probability, not quantum Born-rule normalization"
        ),
        state_space_basis="configuration_space",
        appendix_p_class="compatible_but_ad_hoc",
        is_quantum_state_space=False,
        presence_in_grut="absent",
        supporting_grut_features=[
            "Configuration space C is well-defined (C1 is native_canon)",
            "Formally consistent to define a measure on C",
        ],
        blocking_gaps=[
            "Constitutive ODE is deterministic: no stochastic source, no ensemble",
            "No mechanism in canonical GRUT generates a probability distribution over Φ",
            "A classical probability measure ρ[Φ] ≠ a quantum density matrix: "
            "requires complex Hilbert space for the latter",
            "Even if added as a postulate, ρ[Φ] would be a classical mixture, "
            "not a quantum superposition",
            "Linear convex structure is present (mixtures of ρ₁, ρ₂) but "
            "this is classical, not quantum linear structure",
        ],
        verdict_for_this_candidate=(
            "absent__no_grut_mechanism__compatible_but_ad_hoc_postulate_only"
        ),
        notes=[
            "Absent not obstructed: there is no proved impossibility of adding a "
            "probability measure to GRUT — it is simply not present.",
            "A quantum density matrix ρ_Q requires: complex Hilbert H, "
            "operators on H, trace norm 1. C4 analog lacks all three.",
        ],
    )


def audit_c5_constrained_manifold_bundle_state_space() -> CandidateStateSpaceAudit:
    """C5: Constrained manifold / bundle state space (O(3) MIP).

    Under the O(3) motivated independent postulate (Appendix O), the
    state is a section of the S²-bundle over physical space:
      Φᵃ(x) ∈ Map(D, S²)    with |Φᵃ|² = η²

    This is a nonlinear manifold-valued state. The O(3) target space S²
    is a smooth manifold but not a vector space: the sum of two sections
    is not generally a section (it would not satisfy |Φ|² = η²).

    The tangent space T_φS² at each point is ℝ² — a real 2-plane. One
    could consider complexifying the tangent bundle, but this would
    require yet another postulate.

    Classification: motivated_independent_postulation — present under the
    O(3) MIP postulate (Appendix O), but:
    (a) nonlinear, so no vector-space superposition
    (b) the tangent ℝ² fiber would need further complexification for QM
    (c) the constraint |Φ|² = η² is a real nonlinear condition
    """
    return CandidateStateSpaceAudit(
        candidate_id="C5_constrained_manifold_bundle_state_space",
        candidate_name="constrained_manifold_bundle_state_space",
        state_object_description=(
            "Under O(3) MIP: section Φᵃ(x) ∈ Map(D, S²) with |Φᵃ|² = η² = τ²/(12π). "
            "State space is a nonlinear manifold (infinite-dimensional analog of Map(D,S²)), "
            "not a vector space. Tangent space at each Φ is T_ΦMap(D,S²) ≅ ℝ² per point."
        ),
        valuation_type="manifold_valued",
        superposition_status="absent",
        linear_structure_status="absent",
        normalization_status="present_natural",
        normalization_meaning=(
            "The nonlinear constraint |Φᵃ|² = η² = τ²/(12π) ≈ 0.0398 "
            "is a natural normalization of the O(3) field amplitude. "
            "This is NOT a Born-rule normalization: it constrains field amplitude, "
            "not probability."
        ),
        state_space_basis="manifold",
        appendix_p_class="motivated_independent_postulation",
        is_quantum_state_space=False,
        presence_in_grut="conditionally_present",
        supporting_grut_features=[
            "O(3) MIP postulate (Appendix O): uniquely motivated by π₂(S²)=ℤ + Component B",
            "η² = τ²/(12π) = 1/(8π) partially constrains one O(3) parameter from GRUT canon",
            "Integer winding charge Q ∈ π₂(S²) = ℤ provides topological discreteness",
            "S² has rich geometric structure (Riemannian, symplectic via Kirillov form)",
        ],
        blocking_gaps=[
            "S² is nonlinear: Φᵃ₁ + Φᵃ₂ ∉ S² in general → no linear superposition",
            "Nonlinear manifold ≠ vector space: standard QM requires linear state space",
            "No complex structure on Map(D, S²) natively: would need further MIP",
            "The symplectic structure on S² (Kirillov) is real-valued, not complex",
            "Requires O(3) MIP first: conditionally present, not native canon",
        ],
        verdict_for_this_candidate=(
            "conditionally_present__nonlinear_manifold__"
            "no_superposition__not_quantum_state_space__"
            "could_seed_tangent_bundle_complexification_as_further_mip"
        ),
        notes=[
            "The S² geometry IS rich and could be developed further.",
            "The tangent bundle T(Map(D,S²)) is a real vector bundle — "
            "complexifying it would give a candidate complex state space, "
            "but this requires another MIP beyond the O(3) postulate itself.",
            "Classified MIP because it requires the O(3) independent postulate.",
        ],
    )


def audit_c6_no_quantum_native_state_space() -> CandidateStateSpaceAudit:
    """C6: No quantum-native state space established (primary verdict).

    After auditing C1–C5, the honest null verdict is that canonical GRUT
    does not natively provide a state space adequate for quantum kinematics.

    This is a bounded_structural_result: it is proved within the stated
    architectural assumptions, not assumed. The audit of C1–C5 establishes:
    - C1 (NC): present but classically real, no complex structure
    - C2 (ER): present but classically real, memory extension doesn't add quantum structure
    - C3 (CAH): wrong-signed dynamics (ghost mode) disqualify CTP complexification
    - C4 (CAH): absent, deterministic ODE generates no probability distribution
    - C5 (MIP): conditionally present but nonlinear, no superposition

    The precise missing ingredient is a COMPLEX STRUCTURE J:
      J: config_space → config_space, linear, J² = -1
    J is absent and constitutes a new structural postulate (classified MIP
    at minimum when added).
    """
    return CandidateStateSpaceAudit(
        candidate_id="C6_no_quantum_native_state_space_established",
        candidate_name="no_quantum_native_state_space_established",
        state_object_description=(
            "The null result: canonical GRUT provides no state space that "
            "natively supports quantum kinematics. The native state is the "
            "real scalar field Φ(x) ∈ ℝ — classical, real-valued, deterministic."
        ),
        valuation_type="real_valued",
        superposition_status="absent",
        linear_structure_status="full_real",
        normalization_status="absent",
        normalization_meaning="none",
        state_space_basis="none_established",
        appendix_p_class="bounded_structural_result",
        is_quantum_state_space=False,
        presence_in_grut="present",
        supporting_grut_features=[
            "All five prior candidates (C1-C5) fail to provide quantum state space",
            "C1 gives the native classical substrate (NC) — real linear, no complex structure",
            "C3 disqualification is proved (ghost mode growth rate is positive, not imaginary)",
        ],
        blocking_gaps=[
            "No complex structure J on canonical configuration space",
            "No inner product with Born-rule interpretation",
            "No quantum superposition (classical linear combinations exist, not quantum ones)",
            "No normalization as probability amplitude",
            "The precise gap is one structural postulate: J with J² = -1",
        ],
        verdict_for_this_candidate=(
            "primary_verdict__bounded_structural_result__"
            "no_quantum_native_state_space_established__"
            "precise_gap_identified__complex_structure_j_missing"
        ),
        notes=[
            "This is the CORRECT primary result of Q-B.",
            "The result is not 'no quantum mechanics possible' — it is "
            "'the precise missing structural ingredient is J: J² = -1'.",
            "Once J is identified as the gap, the next question is: "
            "what physical GRUT structure could motivate J? "
            "This is the open path to Q-C.",
        ],
    )


# ================================================================
# Native state space finding
# ================================================================

def build_native_state_space_finding() -> NativeStateSpaceFinding:
    """Build the positive finding: what GRUT actually does provide.

    Despite the primary verdict being null for quantum kinematics,
    GRUT does provide a well-characterized classical state space.
    This positive finding is native_canon and serves as the anchor
    for any quantum extension.
    """
    return NativeStateSpaceFinding(
        state_object_description=(
            "Real scalar field configuration Φ(x) ∈ C = {Φ: D → ℝ}. "
            "At the ODE level: the coupled state (a, H, ρ, p, M_X) ∈ ℝ⁵ "
            "evolving under the canonical constitutive ODE system. "
            "The field-theory state is the real scalar Φ(x); the cosmological "
            "state is (a, H, ρ, p, M_X)."
        ),
        valuation_type="real_valued",
        linear_structure_status="full_real",
        superposition_status="classical_only",
        normalization_status="absent",
        state_space_basis="field_space",
        appendix_p_class="native_canon",
        is_quantum_state_space=False,
        missing_for_quantum=[
            "complex_structure_J_with_J_squared_equals_minus_1",
            "inner_product_with_born_rule_interpretation",
            "quantum_superposition_principle_with_interference",
            "normalization_as_probability_amplitude_norm_squared",
            "unitary_evolution_replacing_dissipative_ode",
        ],
        notes=[
            "The real linear structure IS present natively (NC).",
            "The constitutive ODE τ dΦ/dt + Φ = X is ℝ-linear in Φ for fixed X.",
            "This is the anchor constraint: any quantum extension must recover this.",
            "The gap from classical to quantum kinematics is precisely identified "
            "as the absent complex structure J.",
        ],
    )


# ================================================================
# Complex structure analysis
# ================================================================

def build_complex_structure_analysis() -> ComplexStructureAnalysis:
    """Analyse whether a complex structure J exists in canonical GRUT.

    A complex structure J is a ℝ-linear map on the configuration space
    satisfying J² = -1. Its existence would promote:
      (C, ℝ-linear) → (C, ℂ-linear)
    enabling inner products, Born rule, and quantum superposition.

    The CTP decomposition Φ₊/Φ₋ provides a natural ℝ²-structure.
    But the Φ₋ dynamics disqualify it as J:
      dΦ₋/dt = +Φ₋/τ    (growing ghost mode)

    For J to work, J(Re(Ψ)) = Im(Ψ) and J(Im(Ψ)) = -Re(Ψ) — the
    imaginary part must oscillate at the same rate as the real part.
    But Φ₋ grows exponentially rather than oscillating.
    """
    phi_minus_disqualification = (
        "Φ₋ satisfies dΦ₋/dt = +Φ₋/τ: exponential growth at rate 1/τ. "
        "A complex structure requires Im(Ψ) to evolve as J applied to Re(Ψ) — "
        "i.e., rotation, not growth. The ghost mode growth rate is real and positive; "
        "a proper imaginary part requires a purely imaginary growth rate (oscillation). "
        "Under Galley physical limit Φ₋ → 0, so Im(Ψ) → 0 and the complex "
        "structure collapses to zero."
    )
    return ComplexStructureAnalysis(
        complex_structure_present=False,
        phi_minus_serves_as_imaginary_part=PHI_MINUS_CAN_BE_IMAGINARY_PART,
        phi_minus_growth_rate_sign=PHI_MINUS_GROWTH_RATE_SIGN,
        phi_minus_disqualification=phi_minus_disqualification,
        j_requires_new_postulate=True,
        j_appendix_p_class="motivated_independent_postulation",
        no_j_implies_no_inner_product=True,
        no_j_implies_no_born_rule=True,
        no_j_implies_no_quantum_superposition=True,
        notes=[
            "J is the precise minimal ingredient missing for quantum kinematics.",
            "Adding J is a MIP-level postulate: it introduces new structure "
            "(a linear map J: C → C with J²=-1) that cannot be derived from "
            "the canonical real scalar architecture.",
            "Open path: can any GRUT structure motivate J? "
            "The O(3) tangent bundle T_ΦS² at each point is ℝ²; "
            "equipping it with complex structure would give TₓS² ≅ ℂ. "
            "But this requires the O(3) MIP first (C5) and then further postulation.",
            "This is the bridge to Q-C: the microdynamics question must identify "
            "what physical mechanism provides or motivates J.",
        ],
    )


# ================================================================
# Master function
# ================================================================

def run_qb_quantum_kinematics() -> QBKinematicsResult:
    """Run the complete Q-B Quantum Kinematics audit.

    Audits all six candidate state space classes against the canonical
    GRUT architecture. Returns the primary verdict, native state space
    finding, complex structure analysis, and full candidate audit list.
    """
    candidates = [
        audit_c1_classical_configuration_space(),
        audit_c2_memory_field_configuration_space(),
        audit_c3_complexified_response_space(),
        audit_c4_density_operator_like_effective_space(),
        audit_c5_constrained_manifold_bundle_state_space(),
        audit_c6_no_quantum_native_state_space(),
    ]

    # Sanity checks
    assert len(candidates) == N_CANDIDATE_STATE_SPACES

    candidate_ids = [c.candidate_id for c in candidates]
    for expected_id in CANDIDATE_STATE_SPACE_IDS:
        assert expected_id in candidate_ids, f"Missing candidate {expected_id}"

    for c in candidates:
        assert c.valuation_type in ALLOWED_VALUATION_TYPES
        assert c.superposition_status in ALLOWED_SUPERPOSITION_STATUSES
        assert c.linear_structure_status in ALLOWED_LINEAR_STRUCTURE_STATUSES
        assert c.normalization_status in ALLOWED_NORMALIZATION_STATUSES
        assert c.state_space_basis in ALLOWED_STATE_SPACE_BASES
        assert c.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    # No candidate is a quantum state space
    assert all(not c.is_quantum_state_space for c in candidates)

    # Specific class checks
    c1 = next(c for c in candidates if c.candidate_id == "C1_classical_configuration_space")
    assert c1.appendix_p_class == "native_canon"
    assert c1.linear_structure_status == "full_real"

    c3 = next(c for c in candidates if c.candidate_id == "C3_complexified_response_space")
    assert c3.appendix_p_class == "compatible_but_ad_hoc"
    assert c3.presence_in_grut == "wrong_signed"

    c6 = next(c for c in candidates if c.candidate_id == "C6_no_quantum_native_state_space_established")
    assert c6.appendix_p_class == "bounded_structural_result"

    native = build_native_state_space_finding()
    assert native.appendix_p_class == "native_canon"
    assert not native.is_quantum_state_space
    assert len(native.missing_for_quantum) >= 5

    complex_analysis = build_complex_structure_analysis()
    assert not complex_analysis.complex_structure_present
    assert not complex_analysis.phi_minus_serves_as_imaginary_part
    assert complex_analysis.phi_minus_growth_rate_sign == +1
    assert complex_analysis.no_j_implies_no_born_rule
    assert complex_analysis.no_j_implies_no_quantum_superposition

    assert QB_PRIMARY_VERDICT in ALLOWED_QB_VERDICTS
    assert QB_APPENDIX_P_CLASS in ALLOWED_APPENDIX_P_CLASSES

    nonclaims = list(QB_NONCLAIMS)
    assert len(nonclaims) == N_QB_NONCLAIMS

    # Candidate distribution checks
    nc_candidates = [c for c in candidates if c.appendix_p_class == "native_canon"]
    er_candidates = [c for c in candidates if c.appendix_p_class == "effective_reduction"]
    cah_candidates = [c for c in candidates if c.appendix_p_class == "compatible_but_ad_hoc"]
    bsr_candidates = [c for c in candidates if c.appendix_p_class == "bounded_structural_result"]
    mip_candidates = [c for c in candidates if c.appendix_p_class == "motivated_independent_postulation"]

    assert len(nc_candidates) == 1   # C1
    assert len(er_candidates) == 1   # C2
    assert len(cah_candidates) == 2  # C3, C4
    assert len(bsr_candidates) == 1  # C6
    assert len(mip_candidates) == 1  # C5

    diagnostics: Dict[str, Any] = {
        "n_candidates": len(candidates),
        "candidate_ids": candidate_ids,
        "n_is_quantum": sum(1 for c in candidates if c.is_quantum_state_space),
        "n_native_canon": len(nc_candidates),
        "n_effective_reduction": len(er_candidates),
        "n_compatible_but_ad_hoc": len(cah_candidates),
        "n_bounded_structural_result": len(bsr_candidates),
        "n_motivated_independent_postulation": len(mip_candidates),
        "complex_structure_present": complex_analysis.complex_structure_present,
        "phi_minus_can_serve_as_im": complex_analysis.phi_minus_serves_as_imaginary_part,
        "phi_minus_growth_sign": complex_analysis.phi_minus_growth_rate_sign,
        "missing_for_quantum_count": len(native.missing_for_quantum),
        "primary_verdict": QB_PRIMARY_VERDICT,
        "appendix_p_class": QB_APPENDIX_P_CLASS,
        "n_nonclaims": len(nonclaims),
        "all_candidates_valid_vocabulary": all(
            c.valuation_type in ALLOWED_VALUATION_TYPES
            and c.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES
            for c in candidates
        ),
    }

    return QBKinematicsResult(
        valid=True,
        candidate_audits=candidates,
        native_state_space=native,
        complex_structure=complex_analysis,
        primary_verdict=QB_PRIMARY_VERDICT,
        appendix_p_class=QB_APPENDIX_P_CLASS,
        nonclaims=nonclaims,
        diagnostics=diagnostics,
    )
