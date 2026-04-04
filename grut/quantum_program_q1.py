"""GRUT Phase Q1 — Micro-to-Macro Construction Test.

Determines whether the published GRUT constitutive memory law

    τ dΦ/dt + Φ = X

can be treated as an emergent dissipative limit of a deeper microphysical
substrate. Evaluates four candidate architecture families and classifies
their viability, recovery-map completeness, and hard blockers.

STATUS: PHASE Q1 — FIRST POSITIVE CONSTRUCTION STEP
  This module does NOT simulate quantum dynamics.
  This module does NOT derive Born probabilities.
  This module does NOT model interference or measurement.
  This module classifies candidate micro-to-macro recovery routes and
  identifies the narrowest viable Q1 foundation.

LOCKED BOUNDARY (from Appendix C):
  The published GRUT architecture does not contain: amplitudes, phase
  superposition, Born rule, detector coupling, collapse/decoherence
  dynamics, quantitative fringe law, or GRUT-native microphysical
  ontology for double-slit processes. All five Appendix C subproblems
  face structural blockers.

ANCHOR CONSTRAINT:
  Any microphysical substrate must recover τ dΦ/dt + Φ = X in the
  appropriate macroscopic/classical limit. This is non-negotiable.

NONCLAIMS:
  1. This module does NOT claim that any candidate family is correct.
  2. This module does NOT derive or simulate quantum mechanics.
  3. This module does NOT compute probabilities, amplitudes, or phases.
  4. This module does NOT claim that the CTP interpretation is established.
  5. This module does NOT claim that GRUT has a quantum program — it tests
     whether Q1 foundations exist for building one.
  6. Recovery maps are SCHEMATIC — they identify steps, not derivations.
  7. Viability classification is a NECESSARY-CONDITION test, not validation.
  8. The term "viable_for_q1" means "worth investigating further," not
     "confirmed" or "derived."

See: action_principle.py, galley_memory.py, galley_truncation.py,
     route_c_nonmarkov_kernel.py for existing GRUT recovery-route work.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Literal


# ================================================================
# Constants
# ================================================================

# Appendix C locked structural blockers (cannot be bypassed by Q1)
APPENDIX_C_STRUCTURAL_BLOCKERS = [
    "no_amplitude_formalism",
    "no_phase_superposition",
    "no_born_rule",
    "no_slit_detector_coupling",
    "no_collapse_decoherence_dynamics",
    "no_quantitative_fringe_law",
    "no_experiment_fit_framework",
    "no_microphysical_ontology",
]

# What Q1 is allowed to address (the micro-to-macro gap only)
Q1_SCOPE = [
    "identify_microphysical_object",
    "specify_microdynamic_law",
    "identify_dissipation_mechanism",
    "construct_recovery_map_to_constitutive_law",
    "classify_candidate_viability",
    "list_remaining_hard_blockers",
]

# What Q1 is NOT allowed to claim
Q1_FORBIDDEN_CLAIMS = [
    "derives_born_rule",
    "derives_interference",
    "derives_measurement_theory",
    "derives_collapse",
    "derives_decoherence",
    "derives_particle_ontology",
    "solves_double_slit",
    "explains_quantum_mechanics",
    "provides_quantum_gravity",
    "resolves_appendix_c_blockers",
]

# Published GRUT modules that bear on Q1
GRUT_RECOVERY_MODULES = {
    "action_principle": {
        "file": "grut/action_principle.py",
        "relevance": "Four candidate action formulations; theorem-level "
                     "obstruction; overdamped limit recovery",
        "families_supported": ["A", "B"],
    },
    "galley_memory": {
        "file": "grut/galley_memory.py",
        "relevance": "Galley doubled-field T^Phi derivation in physical limit; "
                     "exact recovery of constitutive law",
        "families_supported": ["B"],
    },
    "galley_truncation": {
        "file": "grut/galley_truncation.py",
        "relevance": "Ghost mode analysis; CTP boundary condition; consistent "
                     "truncation (not attractor) classification",
        "families_supported": ["B"],
    },
    "route_c_nonmarkov_kernel": {
        "file": "grut/route_c_nonmarkov_kernel.py",
        "relevance": "Spectral-representable kernels; exponential kernel to "
                     "ODE reduction; source-profile locking theorem",
        "families_supported": ["D"],
    },
}


# ================================================================
# Vocabulary Control
# ================================================================

# Terms this module may use
ALLOWED_VOCABULARY = [
    "candidate", "family", "recovery_map", "schematic", "viable",
    "blocker", "obstruction", "extendable", "structural", "unknown",
    "constitutive_law", "classical_limit", "coarse_grained", "saddle_point",
    "open_system", "influence_functional", "dissipative_kernel",
    "physical_limit", "tree_level", "bath", "hidden_dof",
    "microphysical_object", "microdynamic_law", "dissipation_mechanism",
]

# Terms this module must NOT use (would imply unsupported claims)
FORBIDDEN_VOCABULARY = [
    "derives", "proves", "solves", "explains", "predicts",
    "quantum_state", "wavefunction", "born_probability", "amplitude",
    "interference_pattern", "fringe", "collapse", "measurement",
    "entanglement", "superposition", "detector", "observer_effect",
]


# ================================================================
# Data Structures — Microphysical Candidates
# ================================================================

MicrophysicalObjectType = Literal[
    "scalar_field",
    "doubled_field",
    "complex_field",
    "operator",
    "history_functional",
    "unspecified",
]

MicrodynamicLawType = Literal[
    "reversible_hamiltonian",
    "quasi_reversible",
    "effective_open_system",
    "undefined",
]

DissipationMechanism = Literal[
    "coarse_graining",
    "subsystem_reduction",
    "bath_coupling",
    "overdamped_limit",
    "ctp_boundary_condition",
    "emergent_arrow",
    "not_explained",
]

CandidateStatus = Literal[
    "viable_for_q1",
    "conceptually_interesting_but_premature",
    "too_speculative",
    "reject",
]

BlockerType = Literal[
    "structural",
    "currently_missing_potentially_extendable",
    "unknown",
]


@dataclass
class RecoveryMapStep:
    """One step in the schematic recovery from microphysics to constitutive law."""
    step_number: int
    description: str
    what_becomes_phi: str = ""
    what_becomes_tau: str = ""
    what_becomes_X: str = ""
    approximation_required: str = ""
    is_exact: bool = False
    is_approximate: bool = False
    grut_module_evidence: str = ""
    status: str = ""  # "established", "schematic", "assumed", "missing"


@dataclass
class RecoveryMap:
    """Schematic recovery map from a microphysical candidate to τ dΦ/dt + Φ = X."""
    family: str
    steps: List[RecoveryMapStep] = field(default_factory=list)
    overall_recovery_exact: bool = False
    overall_recovery_approximate: bool = False
    missing_pieces: List[str] = field(default_factory=list)
    phi_identification: str = ""
    tau_identification: str = ""
    x_identification: str = ""
    why_first_order: str = ""
    what_generates_arrow: str = ""
    assessment: str = ""  # "complete_classical", "partial", "schematic_only", "absent"

    def is_viable(self) -> bool:
        """A recovery map is viable if it has at least a schematic path and
        identifies Φ, τ, and X roles."""
        has_steps = len(self.steps) >= 2
        has_phi = bool(self.phi_identification)
        has_tau = bool(self.tau_identification)
        has_x = bool(self.x_identification)
        has_arrow = bool(self.what_generates_arrow)
        return has_steps and has_phi and has_tau and has_x and has_arrow


@dataclass
class HardBlocker:
    """A hard blocker preventing further formalization."""
    name: str
    description: str
    blocker_type: BlockerType = "structural"
    prevents: str = ""  # what this blocker prevents
    q1_can_address: bool = False
    survives_even_if_q1_succeeds: bool = True


@dataclass
class CandidateFamily:
    """A candidate architecture family for the GRUT microphysical substrate."""
    name: str
    label: str
    core_idea: str

    # Microphysical specification
    microphysical_object: MicrophysicalObjectType = "unspecified"
    microdynamic_law: MicrodynamicLawType = "undefined"
    dissipation_mechanism: DissipationMechanism = "not_explained"

    # GRUT compatibility
    grut_compatibility: str = ""  # "highest", "high", "moderate", "low"
    grut_modules_supporting: List[str] = field(default_factory=list)
    preserves_constitutive_law: bool = False
    preserves_memory_tensor: bool = False
    preserves_two_component: bool = False

    # Assumptions
    new_assumptions: List[str] = field(default_factory=list)
    assumption_severity: str = ""  # "mild", "moderate", "major", "theory_rebuilding"

    # Recovery map
    recovery_map: Optional[RecoveryMap] = None
    recovery_path_visible: bool = False
    recovery_is_exact: bool = False
    recovery_is_approximate: bool = False

    # Code assessment
    code_would_clarify: bool = False
    code_would_create_false_authority: bool = False

    # Blockers
    structural_blockers: List[str] = field(default_factory=list)

    # Classification
    status: CandidateStatus = "reject"

    # Nonclaims
    nonclaims: List[str] = field(default_factory=list)

    def passes_minimum_criteria(self) -> bool:
        """Check whether this candidate answers the five minimum Q1 criteria."""
        has_object = self.microphysical_object != "unspecified"
        has_law = self.microdynamic_law != "undefined"
        has_dissipation = self.dissipation_mechanism != "not_explained"
        has_recovery = (self.recovery_map is not None
                        and self.recovery_map.is_viable())
        has_continuity = (self.preserves_constitutive_law
                          and self.preserves_memory_tensor)
        return (has_object and has_law and has_dissipation
                and has_recovery and has_continuity)


@dataclass
class Q1Result:
    """Master result from the Phase Q1 Micro-to-Macro Construction Test."""
    # Executive determination
    executive_determination: str = ""
    # One of:
    #   "narrow_q1_foundation_identified"
    #   "promising_families_but_no_code_warranted"
    #   "document_only_conceptual"
    #   "no_viable_q1_foundation"

    # Candidate families
    families: List[CandidateFamily] = field(default_factory=list)
    strongest_candidate: str = ""
    strongest_candidate_status: str = ""

    # Hard blockers (survive even if Q1 succeeds)
    hard_blockers: List[HardBlocker] = field(default_factory=list)

    # Q1 scope
    q1_addresses: List[str] = field(default_factory=list)
    q1_does_not_address: List[str] = field(default_factory=list)

    # Appendix C boundary (locked)
    appendix_c_blockers_inherited: List[str] = field(default_factory=list)
    appendix_c_blockers_resolved_by_q1: int = 0  # must be 0

    # Safe and unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)

    # Classification
    q1_classification: str = ""
    # One of:
    #   "recovery_program"
    #   "mechanism_proposal"
    #   "structured_extension"
    #   "speculative_horizon"
    #   "failure"

    nonclaims: List[str] = field(default_factory=list)
    valid: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Export full result to dictionary."""
        return {
            "executive_determination": self.executive_determination,
            "strongest_candidate": self.strongest_candidate,
            "strongest_candidate_status": self.strongest_candidate_status,
            "families": [
                {
                    "name": f.name,
                    "label": f.label,
                    "status": f.status,
                    "microphysical_object": f.microphysical_object,
                    "microdynamic_law": f.microdynamic_law,
                    "dissipation_mechanism": f.dissipation_mechanism,
                    "grut_compatibility": f.grut_compatibility,
                    "assumption_severity": f.assumption_severity,
                    "recovery_path_visible": f.recovery_path_visible,
                    "recovery_is_exact": f.recovery_is_exact,
                    "passes_minimum_criteria": f.passes_minimum_criteria(),
                    "structural_blockers": f.structural_blockers,
                    "nonclaims": f.nonclaims,
                }
                for f in self.families
            ],
            "hard_blockers": [
                {
                    "name": b.name,
                    "blocker_type": b.blocker_type,
                    "prevents": b.prevents,
                    "survives_even_if_q1_succeeds": b.survives_even_if_q1_succeeds,
                }
                for b in self.hard_blockers
            ],
            "q1_addresses": self.q1_addresses,
            "q1_does_not_address": self.q1_does_not_address,
            "appendix_c_blockers_inherited": self.appendix_c_blockers_inherited,
            "appendix_c_blockers_resolved_by_q1": self.appendix_c_blockers_resolved_by_q1,
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "q1_classification": self.q1_classification,
            "nonclaims": self.nonclaims,
            "valid": self.valid,
        }


# ================================================================
# Recovery Map Builders
# ================================================================

def build_recovery_map_family_a() -> RecoveryMap:
    """Family A: KG overdamped limit (Mori-Zwanzig route).

    Hamiltonian KG dynamics → overdamped limit → constitutive law.
    Recovery is APPROXIMATE (drops ∂²Φ/∂t²).
    """
    steps = [
        RecoveryMapStep(
            step_number=1,
            description=(
                "Start with Klein-Gordon scalar field in curved spacetime: "
                "□Φ + m²Φ = m²X, where m² = 1/τ²."
            ),
            what_becomes_phi="The KG field Φ itself",
            what_becomes_tau="τ = 1/m = inverse KG mass",
            what_becomes_X="Source term J/m² from matter-gravity coupling",
            status="established",
            grut_module_evidence="action_principle.py: build_candidate_klein_gordon()",
        ),
        RecoveryMapStep(
            step_number=2,
            description=(
                "In a cosmological or collapse background, the field "
                "experiences effective damping from Hubble friction (3H dΦ/dt "
                "in FRW) or gravitational drag."
            ),
            approximation_required=(
                "Damping must dominate: overdamped_ratio = damping/ω₀ >> 1"
            ),
            is_approximate=True,
            status="established",
            grut_module_evidence="action_principle.py: OverdampedLimitCheck",
        ),
        RecoveryMapStep(
            step_number=3,
            description=(
                "Drop the ∂²Φ/∂t² term (negligible in overdamped regime). "
                "The remaining equation is τ dΦ/dt + Φ = X."
            ),
            is_approximate=True,
            status="established",
            grut_module_evidence=(
                "action_principle.py: overdamped_cosmo and overdamped_collapse "
                "verify recovery numerically"
            ),
        ),
    ]

    return RecoveryMap(
        family="A",
        steps=steps,
        overall_recovery_exact=False,
        overall_recovery_approximate=True,
        phi_identification="The KG scalar field Φ in the overdamped regime",
        tau_identification=(
            "τ = 1/m_KG = inverse Klein-Gordon mass; equivalently "
            "τ = ω₀⁻¹ (inverse natural frequency)"
        ),
        x_identification=(
            "The gravitational source X[g, T] from matter coupling"
        ),
        why_first_order=(
            "In the overdamped limit, the second-order KG dynamics reduces "
            "to first-order because the inertial (∂²Φ/∂t²) term is negligible "
            "compared to the damping ((1/τ)∂Φ/∂t) and mass (Φ/τ²) terms."
        ),
        what_generates_arrow=(
            "Environmental damping (Hubble friction in cosmology, gravitational "
            "drag in collapse). The dissipative arrow is inherited from the "
            "cosmological or gravitational environment, not intrinsic to the "
            "scalar field."
        ),
        missing_pieces=[
            "What provides damping in the collapse sector is not specified",
            "Propagating KG modes (absent from GRUT) are physical or artifacts — unresolved",
            "Quantization of the KG parent would be the quantum extension",
            "The overdamped condition may not hold in all regimes",
        ],
        assessment="complete_classical",
    )


def build_recovery_map_family_b() -> RecoveryMap:
    """Family B: CTP/Galley classical saddle.

    CTP path integral → classical saddle (Φ₁=Φ₂) → Galley physical limit
    → constitutive law. Recovery is EXACT at tree level.
    """
    steps = [
        RecoveryMapStep(
            step_number=1,
            description=(
                "Posit a CTP (closed-time-path / Schwinger-Keldysh) path "
                "integral for the memory field coupled to hidden DOF (bath): "
                "Z = ∫DΦ₁DΦ₂ exp(i[S₁ - S₂ + S_IF])."
            ),
            what_becomes_phi=(
                "The physical-limit field Φ_+ = (Φ₁+Φ₂)/2 at the classical "
                "saddle Φ₁ = Φ₂ = Φ_cl"
            ),
            what_becomes_tau=(
                "The dissipation timescale τ encoded in the influence "
                "functional S_IF (set by bath spectral density)"
            ),
            what_becomes_X="The source J from matter-gravity coupling",
            status="schematic",
            grut_module_evidence=(
                "galley_memory.py: GalleyActionCandidate with S₁ - S₂ + S_diss"
            ),
        ),
        RecoveryMapStep(
            step_number=2,
            description=(
                "Take the classical saddle point: δS/δΦ₁ = δS/δΦ₂ = 0. "
                "This produces the Galley equations of motion with "
                "cross-coupling between Φ₁ and Φ₂."
            ),
            is_exact=True,
            status="established",
            grut_module_evidence=(
                "galley_truncation.py: cross-coupled EOMs "
                "dΦ₁/dt = (X-Φ₂)/τ, dΦ₂/dt = (X-Φ₁)/τ"
            ),
        ),
        RecoveryMapStep(
            step_number=3,
            description=(
                "Apply the physical limit Φ₁ = Φ₂ = Φ (equivalently "
                "Φ₋ = 0, the CTP boundary condition). The Φ₊ equation "
                "becomes τ dΦ/dt + Φ = X exactly."
            ),
            is_exact=True,
            status="established",
            grut_module_evidence=(
                "galley_truncation.py: 'Scalar consistent truncation: EXACT', "
                "'physical_limit_recovers_grut: True'"
            ),
        ),
    ]

    return RecoveryMap(
        family="B",
        steps=steps,
        overall_recovery_exact=True,
        overall_recovery_approximate=False,
        phi_identification=(
            "The physical-limit field Φ₊ = (Φ₁+Φ₂)/2 evaluated at the "
            "CTP classical saddle Φ₁ = Φ₂"
        ),
        tau_identification=(
            "The dissipation timescale in the Galley kernel S_diss; in the "
            "CTP interpretation, set by the influence functional of the bath "
            "(hidden DOF spectral density)"
        ),
        x_identification=(
            "The gravitational source X[g, T], entering symmetrically in "
            "both field copies"
        ),
        why_first_order=(
            "The Galley formalism is DESIGNED to produce first-order "
            "dissipative equations from a doubled action. In the +/- "
            "decomposition, Φ₊ obeys relaxation (first-order) and Φ₋ "
            "obeys growth (also first-order). The CTP boundary condition "
            "kills Φ₋, leaving only the dissipative Φ₊ equation."
        ),
        what_generates_arrow=(
            "The CTP boundary condition Φ₋(T) = 0. In the path-integral "
            "interpretation, this is the condition that the forward and "
            "backward time contours meet at the final time. It encodes "
            "the arrow of time by selecting the retarded (causal) "
            "propagator over the advanced one."
        ),
        missing_pieces=[
            "The bath DOF are not specified — what hidden degrees of freedom "
            "produce the influence functional?",
            "The connection 'Galley formalism = CTP classical limit' is "
            "standard in the literature but not formally verified within GRUT",
            "Loop corrections (Φ₋ fluctuations) are not computed — these "
            "would be the first quantum corrections",
            "The metric-doubling sector has undetermined ghost status",
            "The bath spectral density determining τ is not derived from "
            "first principles",
        ],
        assessment="complete_classical",
    )


def build_recovery_map_family_c() -> RecoveryMap:
    """Family C: Complexified memory.

    No viable recovery map — would smuggle standard QM.
    """
    return RecoveryMap(
        family="C",
        steps=[
            RecoveryMapStep(
                step_number=1,
                description=(
                    "Replace real Φ with complex Ψ = Φ + iΠ and posit "
                    "unitary dynamics."
                ),
                status="assumed",
            ),
            RecoveryMapStep(
                step_number=2,
                description=(
                    "Invoke phase averaging or decoherence to eliminate Π "
                    "and recover real Φ dynamics."
                ),
                approximation_required=(
                    "Requires decoherence mechanism — which Appendix C "
                    "identified as a structural blocker"
                ),
                status="missing",
            ),
        ],
        overall_recovery_exact=False,
        overall_recovery_approximate=False,
        phi_identification="Real part of Ψ after phase averaging",
        tau_identification="",
        x_identification="",
        why_first_order="",
        what_generates_arrow="",
        missing_pieces=[
            "No published complex-field structure in GRUT",
            "Requires decoherence mechanism (Appendix C structural blocker)",
            "Recovery map is indistinguishable from 'assume QM, take classical limit'",
            "Does not add to GRUT — would import standard QM machinery",
        ],
        assessment="absent",
    )


def build_recovery_map_family_d() -> RecoveryMap:
    """Family D: History functional / nonlocal kernel.

    Partial recovery — kernel-to-ODE exact, but path-integral parent unspecified.
    """
    steps = [
        RecoveryMapStep(
            step_number=1,
            description=(
                "Define the memory field as a history convolution: "
                "Φ(t) = ∫₀^∞ K(s) X(t-s) ds with K(s) = (1/τ)e^{-s/τ}."
            ),
            what_becomes_phi="The convolution integral over source history",
            what_becomes_tau="Decay timescale of the exponential kernel K(s)",
            what_becomes_X="The gravitational source at past times X(t-s)",
            is_exact=True,
            status="established",
            grut_module_evidence="route_c_nonmarkov_kernel.py: exponential kernel",
        ),
        RecoveryMapStep(
            step_number=2,
            description=(
                "Differentiate the convolution: τ dΦ/dt = -Φ + X(t). "
                "This is exact for exponential kernel (Markovian)."
            ),
            is_exact=True,
            status="established",
            grut_module_evidence=(
                "route_c_nonmarkov_kernel.py: spectral component ODE "
                "(1/w)dΦ_w/dt + Φ_w = X"
            ),
        ),
    ]

    return RecoveryMap(
        family="D",
        steps=steps,
        overall_recovery_exact=True,
        overall_recovery_approximate=False,
        phi_identification=(
            "The weighted history integral ∫K(s)X(t-s)ds"
        ),
        tau_identification=(
            "The kernel decay timescale; for exponential kernel K(s)=(1/τ)e^{-s/τ}"
        ),
        x_identification="The gravitational source at past times",
        why_first_order=(
            "The exponential kernel is the unique kernel for which the "
            "history convolution satisfies a first-order ODE. This is "
            "because the exponential is the eigenfunction of differentiation."
        ),
        what_generates_arrow=(
            "The retarded kernel K(s) = (1/τ)e^{-s/τ}Θ(s) — the Heaviside "
            "step function Θ(s) enforces causality (past sources only). "
            "The arrow is built into the kernel's retarded structure."
        ),
        missing_pieces=[
            "No specified path-integral parent for the history functional",
            "No measure over field histories defined",
            "Observer-flow dependence (kernel retardation defined along specific timelike curve)",
            "Generalization to non-exponential kernels changes temporal dynamics but "
            "not spatial scaling (source-profile locking theorem)",
        ],
        assessment="partial",
    )


# ================================================================
# Candidate Family Builders
# ================================================================

def build_family_a() -> CandidateFamily:
    """Family A — Reversible substrate + coarse graining (Mori-Zwanzig / KG)."""
    return CandidateFamily(
        name="A",
        label="Reversible Substrate + Coarse Graining (Mori-Zwanzig / KG)",
        core_idea=(
            "A deeper reversible Hamiltonian dynamics (Klein-Gordon scalar "
            "field) exists. The observed GRUT constitutive lag is the "
            "macroscopic coarse-grained overdamped limit. The dissipation "
            "arises from environmental friction (Hubble expansion, "
            "gravitational drag)."
        ),
        microphysical_object="scalar_field",
        microdynamic_law="reversible_hamiltonian",
        dissipation_mechanism="overdamped_limit",
        grut_compatibility="high",
        grut_modules_supporting=[
            "action_principle.py (Candidate 1: Klein-Gordon)",
            "action_principle.py (OverdampedLimitCheck)",
        ],
        preserves_constitutive_law=True,
        preserves_memory_tensor=True,
        preserves_two_component=True,
        new_assumptions=[
            "The memory field Φ is the overdamped limit of a Klein-Gordon field",
            "There exists an environment providing strong damping (overdamped ratio >> 1)",
            "Propagating KG modes are physical but suppressed in the overdamped regime",
            "Classical limit applies (ℏ-corrections negligible for macroscopic Φ)",
        ],
        assumption_severity="mild_to_moderate",
        recovery_map=build_recovery_map_family_a(),
        recovery_path_visible=True,
        recovery_is_exact=False,
        recovery_is_approximate=True,
        code_would_clarify=True,
        code_would_create_false_authority=False,
        structural_blockers=[
            "KG introduces propagating modes absent from published GRUT",
            "What provides damping in collapse sector is unspecified",
            "Overdamped condition may break in strong-field regimes",
        ],
        status="viable_for_q1",
        nonclaims=[
            "Family A does NOT claim that Φ is a Klein-Gordon field — it "
            "identifies KG as a viable classical parent",
            "The overdamped limit is approximate, not exact",
            "Propagating KG modes are neither confirmed nor excluded",
            "Quantization of the KG parent is a future step, not a Q1 claim",
        ],
    )


def build_family_b() -> CandidateFamily:
    """Family B — Doubled system / CTP / Galley route."""
    return CandidateFamily(
        name="B",
        label="CTP / Galley Open-System Route",
        core_idea=(
            "The GRUT memory field is an open subsystem coupled to hidden "
            "degrees of freedom. The Galley doubled-field action "
            "S[Φ₁,Φ₂] = S₁ - S₂ + S_IF is the classical limit of the "
            "Schwinger-Keldysh (CTP) path integral. The physical limit "
            "Φ₁ = Φ₂ IS the classical saddle point. Dissipation arises "
            "from the influence functional encoding the bath."
        ),
        microphysical_object="doubled_field",
        microdynamic_law="effective_open_system",
        dissipation_mechanism="ctp_boundary_condition",
        grut_compatibility="highest",
        grut_modules_supporting=[
            "galley_memory.py (GalleyActionCandidate, physical-limit T^Φ)",
            "galley_truncation.py (ghost mode, CTP boundary, truncation analysis)",
            "action_principle.py (Candidate 2: Galley doubled-field)",
        ],
        preserves_constitutive_law=True,
        preserves_memory_tensor=True,
        preserves_two_component=True,
        new_assumptions=[
            "The Galley doubled-field structure has a CTP path-integral parent",
            "There exist hidden DOF whose influence functional produces the "
            "dissipative Galley kernel",
            "The physical limit Φ₁=Φ₂ corresponds to the classical/tree-level "
            "saddle of the CTP integral",
        ],
        assumption_severity="mild",
        recovery_map=build_recovery_map_family_b(),
        recovery_path_visible=True,
        recovery_is_exact=True,
        recovery_is_approximate=False,
        code_would_clarify=True,
        code_would_create_false_authority=False,
        structural_blockers=[
            "Bath DOF are not specified",
            "Galley-to-CTP connection is standard in literature but not formally "
            "verified within GRUT",
            "Loop corrections (quantum Φ₋ fluctuations) not computed",
            "Metric-doubling sector has undetermined ghost status",
            "Bath spectral density determining τ is not derived",
        ],
        status="viable_for_q1",
        nonclaims=[
            "Family B does NOT claim that the CTP interpretation is established "
            "— it identifies CTP as the natural parent formalism for the "
            "existing Galley structure",
            "The bath DOF are not specified — 'hidden DOF' is a placeholder",
            "The recovery is exact at tree level; quantum corrections are unknown",
            "This does NOT constitute a quantum theory of GRUT memory",
            "The term 'open system' means the memory field is coupled to "
            "unmodeled DOF — it does NOT imply a quantum open-system description",
        ],
    )


def build_family_c() -> CandidateFamily:
    """Family C — Complexified memory kinematics."""
    return CandidateFamily(
        name="C",
        label="Complexified Memory Kinematics",
        core_idea=(
            "Replace real Φ with complex Ψ = Φ + iΠ carrying phase. "
            "The constitutive law emerges after phase averaging or "
            "decohering reduction."
        ),
        microphysical_object="complex_field",
        microdynamic_law="undefined",
        dissipation_mechanism="not_explained",
        grut_compatibility="low",
        grut_modules_supporting=[],
        preserves_constitutive_law=False,
        preserves_memory_tensor=False,
        preserves_two_component=True,
        new_assumptions=[
            "Φ has a hidden imaginary partner Π with no GRUT precedent",
            "There exists unitary dynamics for Ψ (not specified)",
            "Phase averaging or decoherence eliminates Π (requires mechanism "
            "identified as structural blocker in Appendix C)",
            "The real part's reduced dynamics is the constitutive law (not shown)",
        ],
        assumption_severity="major",
        recovery_map=build_recovery_map_family_c(),
        recovery_path_visible=False,
        recovery_is_exact=False,
        recovery_is_approximate=False,
        code_would_clarify=False,
        code_would_create_false_authority=True,
        structural_blockers=[
            "No published complex-field structure in GRUT",
            "Requires decoherence mechanism (Appendix C structural blocker #5)",
            "Recovery map is indistinguishable from importing standard QM",
            "Doubles field content without GRUT precedent",
        ],
        status="too_speculative",
        nonclaims=[
            "Family C is included for completeness but does NOT pass the "
            "minimum viability threshold",
            "Complexification is not rejected in principle — it is rejected "
            "at the Q1 stage because it requires assumptions that are not "
            "grounded in published GRUT architecture",
        ],
    )


def build_family_d() -> CandidateFamily:
    """Family D — Functional / history-based state description."""
    return CandidateFamily(
        name="D",
        label="History Functional / Nonlocal Kernel Route",
        core_idea=(
            "The fundamental object is a weighted history functional — the "
            "convolution Φ(t) = ∫K(s)X(t-s)ds with retarded kernel. The "
            "constitutive ODE is exact for exponential kernel. The deeper "
            "structure would be a path integral over field histories whose "
            "saddle point yields the retarded convolution."
        ),
        microphysical_object="history_functional",
        microdynamic_law="quasi_reversible",
        dissipation_mechanism="bath_coupling",
        grut_compatibility="moderate",
        grut_modules_supporting=[
            "route_c_nonmarkov_kernel.py (spectral kernels, source-profile locking)",
            "action_principle.py (Candidate 3: Nonlocal retarded action)",
        ],
        preserves_constitutive_law=True,
        preserves_memory_tensor=True,
        preserves_two_component=True,
        new_assumptions=[
            "The history convolution has a path-integral parent",
            "The retarded kernel K(s) is the saddle-point weight of a "
            "well-defined measure over histories",
            "Fluctuations around the saddle correspond to quantum corrections",
        ],
        assumption_severity="moderate",
        recovery_map=build_recovery_map_family_d(),
        recovery_path_visible=True,
        recovery_is_exact=True,
        recovery_is_approximate=False,
        code_would_clarify=False,
        code_would_create_false_authority=False,
        structural_blockers=[
            "Effective action S_eff over histories is not specified",
            "Measure over field histories is not defined",
            "Observer-flow dependence makes theory not manifestly covariant",
            "Connection to path-integral quantization is assumed, not derived",
        ],
        status="conceptually_interesting_but_premature",
        nonclaims=[
            "Family D does NOT claim a path-integral parent exists — it "
            "identifies the nonlocal retarded kernel as a candidate seed "
            "for such a construction",
            "The kernel-to-ODE reduction is exact; the deeper history-functional "
            "structure is speculative",
            "Observer-flow dependence is a known obstruction for covariance",
        ],
    )


# ================================================================
# Hard Blocker Builder
# ================================================================

def build_hard_blockers() -> List[HardBlocker]:
    """Hard blockers that survive even if Q1 succeeds."""
    return [
        HardBlocker(
            name="no_born_rule",
            description=(
                "No probability measure over outcomes. The constitutive law "
                "is deterministic. Even if a microphysical substrate is "
                "identified, deriving Born probabilities requires a separate "
                "measurement theory."
            ),
            blocker_type="structural",
            prevents="probability predictions, interference fringe computation",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="no_measurement_coupling",
            description=(
                "No formalism for how a detector couples to the memory field "
                "or its microphysical substrate. Which-path information, "
                "complementarity, and measurement back-reaction require a "
                "detector model."
            ),
            blocker_type="structural",
            prevents="measurement theory, which-path analysis, detector design",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="no_interference_formalism",
            description=(
                "No amplitude superposition, no phase variable, no "
                "interference law. Even with a KG or CTP parent, deriving "
                "interference requires retaining quantum coherence (loop "
                "corrections) rather than taking the classical limit."
            ),
            blocker_type="structural",
            prevents="interference pattern computation, fringe visibility",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="no_particle_ontology",
            description=(
                "No particle states, no Fock space, no asymptotic states. "
                "GRUT operates at the level of classical fields. Particle "
                "ontology requires quantization of the field."
            ),
            blocker_type="structural",
            prevents="particle interpretation, scattering theory, creation/annihilation",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="no_experiment_framework",
            description=(
                "No apparatus for comparing predictions against laboratory "
                "quantum experiments (double-slit, interferometry, etc.). "
                "No parameter-fitting procedure for quantum observables."
            ),
            blocker_type="structural",
            prevents="experimental contact with quantum phenomena",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="bath_dof_unspecified",
            description=(
                "In Families A and B, the 'bath' or 'environment' providing "
                "dissipation is not specified. What degrees of freedom are "
                "being traced out? This is the deepest open question for Q2."
            ),
            blocker_type="currently_missing_potentially_extendable",
            prevents="concrete microphysical model, first-principles τ derivation",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="loop_corrections_unknown",
            description=(
                "In Family B, the classical saddle (physical limit) is exact. "
                "But quantum corrections (Φ₋ fluctuations, loop diagrams in "
                "the CTP integral) are not computed. These corrections would "
                "be the first quantum effects beyond classical GRUT."
            ),
            blocker_type="currently_missing_potentially_extendable",
            prevents="quantum corrections to GRUT, coherence effects",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
        HardBlocker(
            name="metric_doubling_ghost",
            description=(
                "In the Galley doubled-field formalism, the metric-difference "
                "sector (g₁ ≠ g₂) has undetermined ghost status. This is an "
                "open obstruction for the full covariant theory."
            ),
            blocker_type="unknown",
            prevents="covariant doubled-field gravity, full Galley-Einstein system",
            q1_can_address=False,
            survives_even_if_q1_succeeds=True,
        ),
    ]


# ================================================================
# Master Builder
# ================================================================

def run_q1_assessment() -> Q1Result:
    """Execute the Phase Q1 Micro-to-Macro Construction Test.

    Returns a fully classified result with candidate families, recovery
    maps, hard blockers, and safe/unsafe claims.
    """
    # Build candidate families
    family_a = build_family_a()
    family_b = build_family_b()
    family_c = build_family_c()
    family_d = build_family_d()

    families = [family_a, family_b, family_c, family_d]

    # Determine strongest candidate
    viable = [f for f in families if f.status == "viable_for_q1"]
    if not viable:
        strongest = ""
        strongest_status = "no_viable_candidate"
    else:
        # Family B is strongest: exact recovery, highest GRUT compatibility,
        # mildest assumptions, most GRUT-module evidence
        strongest = "B"
        strongest_status = "viable_for_q1"

    # Hard blockers
    hard_blockers = build_hard_blockers()

    # Verify Appendix C boundary is locked
    # Q1 must NOT claim to resolve any Appendix C blocker
    appendix_c_resolved = 0

    # Determine executive classification
    # Two families are viable, both have complete classical recovery maps
    # Family B has exact recovery with the most GRUT precedent
    # This is a genuine Q1 foundation — narrow but real
    executive = "narrow_q1_foundation_identified"

    # Safe claims
    safe_claims = [
        "The published Galley doubled-field formalism has the structural form "
        "of a CTP (closed-time-path) classical limit, which is the standard "
        "framework for deriving dissipative dynamics from a deeper theory.",

        "The recovery map from Galley physical limit to the constitutive law "
        "τ dΦ/dt + Φ = X is exact (not approximate) at tree level.",

        "The Klein-Gordon overdamped limit provides an approximate but "
        "explicit recovery of the constitutive law from second-order dynamics.",

        "Both Family A and Family B identify a schematic micro-to-macro path "
        "with mild-to-moderate assumptions grounded in existing GRUT modules.",

        "All Appendix C structural blockers (no amplitudes, no Born rule, no "
        "interference, no measurement theory) remain fully in force after Q1.",

        "The Q1 result is a recovery program — it identifies the structure "
        "needed for a future quantum extension, not the extension itself.",

        "The dissipative character of the constitutive law is the natural "
        "signature of a reduced/open-system description.",

        "The ghost mode Φ₋ in the Galley formalism (growth rate 1/τ) is "
        "maintained at zero by the CTP boundary condition, not by dynamics. "
        "This is a standard feature of the Galley/CTP framework.",
    ]

    # Unsafe claims
    unsafe_claims = [
        "GRUT derives or explains quantum mechanics.",
        "GRUT has a quantum program (it has at most a Q1 foundation for one).",
        "The CTP interpretation is established or confirmed within GRUT.",
        "The bath DOF are known or specified.",
        "Q1 resolves any Appendix C structural blocker.",
        "The Galley formalism provides quantum corrections to GRUT.",
        "Family B 'derives' the constitutive law from quantum field theory.",
        "The recovery map constitutes a derivation (it is schematic).",
        "GRUT can predict interference, probabilities, or measurement outcomes.",
        "The micro-to-macro construction is complete (the bath is unspecified, "
        "loop corrections are unknown, and metric doubling is undetermined).",
    ]

    # Build master result
    result = Q1Result(
        executive_determination=executive,
        families=families,
        strongest_candidate=strongest,
        strongest_candidate_status=strongest_status,
        hard_blockers=hard_blockers,
        q1_addresses=list(Q1_SCOPE),
        q1_does_not_address=list(Q1_FORBIDDEN_CLAIMS),
        appendix_c_blockers_inherited=list(APPENDIX_C_STRUCTURAL_BLOCKERS),
        appendix_c_blockers_resolved_by_q1=appendix_c_resolved,
        safe_claims=safe_claims,
        unsafe_claims=unsafe_claims,
        q1_classification="recovery_program",
        nonclaims=[
            "This assessment does NOT claim any candidate family is correct.",
            "Viability means 'worth investigating,' not 'confirmed.'",
            "Recovery maps are schematic — they identify steps, not derivations.",
            "The term 'foundation' means 'a starting point exists,' not "
            "'the program is complete.'",
            "No quantum dynamics are simulated or computed.",
            "No probabilities, amplitudes, or phases are produced.",
            "All Appendix C blockers remain locked and unresolved.",
            "The CTP interpretation of the Galley formalism is a candidate "
            "reading, not a confirmed result.",
        ],
        valid=True,
    )

    # Final validation: ensure no forbidden claim is made
    _validate_no_forbidden_claims(result)

    return result


def _validate_no_forbidden_claims(result: Q1Result) -> None:
    """Verify that the result does not make any forbidden claims."""
    # Appendix C boundary must be locked
    if result.appendix_c_blockers_resolved_by_q1 != 0:
        raise ValueError(
            "Q1 CANNOT claim to resolve Appendix C blockers. "
            f"Found: {result.appendix_c_blockers_resolved_by_q1} claimed resolved."
        )

    # No family should claim to derive QM
    for family in result.families:
        if family.status == "viable_for_q1":
            # Viable families must preserve constitutive law
            if not family.preserves_constitutive_law:
                raise ValueError(
                    f"Family {family.name} is viable_for_q1 but does not "
                    f"preserve the constitutive law — this is impossible."
                )

    # Executive must not overclaim
    allowed_executives = {
        "narrow_q1_foundation_identified",
        "promising_families_but_no_code_warranted",
        "document_only_conceptual",
        "no_viable_q1_foundation",
    }
    if result.executive_determination not in allowed_executives:
        raise ValueError(
            f"Executive determination '{result.executive_determination}' "
            f"is not in allowed set: {allowed_executives}"
        )

    # Q1 classification must not overclaim
    allowed_classifications = {
        "recovery_program",
        "mechanism_proposal",
        "structured_extension",
        "speculative_horizon",
        "failure",
    }
    if result.q1_classification not in allowed_classifications:
        raise ValueError(
            f"Q1 classification '{result.q1_classification}' "
            f"is not in allowed set: {allowed_classifications}"
        )
