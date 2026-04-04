"""GRUT Phase Q2 — Bath Specification and Reduction Test.

Determines whether the CTP/Galley recovery route (Q1 Family B) can be
sharpened by identifying plausible hidden degrees of freedom whose
reduction yields the published GRUT constitutive memory law.

CENTRAL FINDING:
  The published τ_eff formula,

    τ_eff = τ₀ / (1 + (ω·τ₀)²)

  where ω = |V/R| (collapse) or ω = H (cosmology), has the EXACT
  functional form of the effective susceptibility arising from a
  single-pole (Drude/Lorentzian) bath spectral density:

    J(ω) ~ η·ω·Ω² / (ω² + Ω²),    Ω = 1/τ₀

  This identifies the TYPE of bath that would produce the published
  dynamics but does NOT constitute a derivation of the bath from
  first principles.

STATUS: PHASE Q2 — BATH SPECIFICATION
  This module classifies candidate bath families and their reduction
  maps to the published constitutive law.

LOCKED BOUNDARIES:
  Appendix C: No amplitudes, Born rule, interference, measurement theory,
              collapse/decoherence, particle ontology.
  Q1: CTP/Galley is strongest recovery route; recovery is exact at tree
      level; bath DOF unspecified; loop corrections unknown.

NONCLAIMS:
  1. This module does NOT derive the bath from first principles.
  2. This module does NOT claim the Drude structural match IS a derivation.
  3. This module does NOT simulate bath dynamics or open-system evolution.
  4. This module does NOT compute quantum corrections or noise spectra.
  5. This module does NOT resolve any Appendix C or Q1 hard blocker.
  6. The Drude/Lorentzian match is a STRUCTURAL OBSERVATION, not a proof.
  7. "Best Q2 candidate" means "most structurally motivated," not "correct."
  8. No bath candidate is validated — all are candidates for future work.

See: quantum_program_q1.py, galley_truncation.py, interior_pde.py,
     operators.py, collapse.py for upstream structures.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Literal


# ================================================================
# Constants — Locked Inheritance
# ================================================================

# From Q1: Appendix C structural blockers (still locked)
Q1_HARD_BLOCKERS_INHERITED = [
    "no_born_rule",
    "no_measurement_coupling",
    "no_interference_formalism",
    "no_particle_ontology",
    "no_experiment_framework",
    "bath_dof_unspecified",       # Q2 targets THIS blocker
    "loop_corrections_unknown",
    "metric_doubling_ghost",
]

# From Q1: the blocker Q2 addresses
Q2_TARGET_BLOCKER = "bath_dof_unspecified"

# Published GRUT τ_eff formulas (constitutive, not derived)
TAU_EFF_COLLAPSE = "tau_eff = tau_0 / (1 + (|V/R| * tau_0)^2)"
TAU_EFF_COSMOLOGICAL = "tau_eff = tau_0 / (1 + (H * tau_0)^2)"

# Interior PDE dispersion relation (derived from linearisation)
DISPERSION_RELATION = "omega^2 = omega_0^2 + 2*alpha*omega_g^2 / (1 + i*omega*tau_eff)"

# Structural identity at equilibrium
STRUCTURAL_IDENTITY = "omega_0 * tau_eff = 1"

# Drude/Lorentzian bath spectral density
DRUDE_SPECTRAL_DENSITY = "J(omega) = eta * omega * Omega^2 / (omega^2 + Omega^2)"
DRUDE_CUTOFF = "Omega = 1 / tau_0"

# What Q2 is NOT allowed to claim
Q2_FORBIDDEN_CLAIMS = [
    "derives_bath_from_first_principles",
    "proves_drude_match_is_physical",
    "derives_born_rule",
    "derives_interference",
    "derives_measurement",
    "resolves_appendix_c_blockers",
    "completes_quantum_program",
    "validates_any_bath_candidate",
    "derives_noise_spectrum",
    "computes_quantum_corrections",
]


# ================================================================
# Type Definitions
# ================================================================

BathStatus = Literal[
    "best_q2_candidate",
    "viable_but_underdetermined",
    "formally_possible_but_physically_weak",
    "reject",
]

MarkovianStatus = Literal[
    "genuinely_markovian",
    "approximately_markovian",
    "genuinely_non_markovian",
    "unclear",
]

ReductionAssessment = Literal[
    "complete_schematic",
    "partial_schematic",
    "formal_only",
    "absent",
]

TauInterpretation = Literal[
    "damping_timescale",
    "memory_kernel_timescale",
    "effective_susceptibility_timescale",
    "unknown",
]


# ================================================================
# Data Structures
# ================================================================

@dataclass
class DrudeStructuralMatch:
    """Analysis of the structural match between published τ_eff and
    the Drude/Lorentzian bath spectral density.

    This is a STRUCTURAL OBSERVATION, not a derivation.
    """
    # Published GRUT formula
    tau_eff_formula: str = TAU_EFF_COLLAPSE
    # Lorentzian functional form: χ(ω) = 1/(1 + (ω/Ω)²)
    lorentzian_susceptibility: str = "chi(omega) = 1 / (1 + (omega * tau_0)^2)"
    # Match: τ_eff = τ₀ · χ(ω)
    structural_match: bool = True
    match_description: str = (
        "The published τ_eff = τ₀/(1+(ω·τ₀)²) is identically "
        "τ₀ times the Lorentzian susceptibility χ(ω) = 1/(1+(ω/Ω)²) "
        "with Ω = 1/τ₀. In open-system theory, this form arises from "
        "a Drude bath spectral density J(ω) = η·ω·Ω²/(ω²+Ω²)."
    )
    # What this match implies
    implies_bath_type: str = (
        "Single-pole ohmic bath with Lorentzian cutoff at Ω = 1/τ₀"
    )
    # What this match does NOT imply
    does_not_imply: List[str] = field(default_factory=lambda: [
        "That the bath exists (structural match ≠ existence proof)",
        "That the bath is unique (other spectral densities may produce "
        "similar effective τ_eff in restricted regimes)",
        "That the match is exact at all frequencies (it may be the "
        "leading-order term of a more complex spectral density)",
        "That the bath DOF are identified (what oscillators comprise "
        "the bath remains open)",
    ])
    # Connection to structural identity
    resonance_condition: str = (
        "At equilibrium, ω₀·τ_eff = 1 (structural identity). This is the "
        "condition that the system frequency matches the bath cutoff: "
        "ω₀ = Ω = 1/τ₀. The system sits at the critical point between "
        "underdamped (ω₀·τ₀ < 1) and overdamped (ω₀·τ₀ > 1)."
    )
    # Dispersion relation connection
    dispersion_connection: str = (
        "The interior PDE dispersion relation contains the factor "
        "1/(1 + i·ω·τ_eff), which is the single-pole frequency-dependent "
        "susceptibility of the memory sector. This is the response "
        "function of a system coupled to a single-relaxation-time bath."
    )
    # Classification
    match_strength: str = "structural_not_derivational"


@dataclass
class BathReductionMap:
    """Schematic reduction from a candidate bath to τ dΦ/dt + Φ = X."""
    bath_family: str
    parent_variables: str = ""
    retained_slow_variable: str = ""
    eliminated_dof: str = ""
    source_becomes_X: str = ""
    why_first_order: str = ""
    tau_interpretation: TauInterpretation = "unknown"
    markovian_status: MarkovianStatus = "unclear"
    is_local_in_time: bool = True
    assessment: ReductionAssessment = "absent"
    missing_pieces: List[str] = field(default_factory=list)

    def is_viable(self) -> bool:
        """A reduction map is viable if it identifies the key roles."""
        return (
            bool(self.retained_slow_variable)
            and bool(self.eliminated_dof)
            and bool(self.why_first_order)
            and self.tau_interpretation != "unknown"
            and self.assessment in ("complete_schematic", "partial_schematic")
        )


@dataclass
class CanonCompatibility:
    """Assessment of whether a bath candidate threatens published canon."""
    preserves_constitutive_law: bool = False
    contradicts_strong_field: bool = False
    destabilizes_phenomenology: bool = False
    requires_failed_tensor_memory: bool = False
    imports_inconsistent_ontology: bool = False
    assessment: str = ""  # "compatible", "tension", "incompatible"

    def is_compatible(self) -> bool:
        return (
            self.preserves_constitutive_law
            and not self.contradicts_strong_field
            and not self.destabilizes_phenomenology
            and not self.requires_failed_tensor_memory
            and not self.imports_inconsistent_ontology
        )


@dataclass
class BathCandidate:
    """A candidate bath family for the CTP/Galley recovery route."""
    name: str
    label: str
    core_idea: str

    # What is being integrated out
    integrated_out_dof: str = ""
    why_hidden: str = ""
    why_dissipative: str = ""

    # Physical vs formal
    is_physically_motivated: bool = False
    is_formally_possible: bool = False

    # Reduction
    reduction_map: Optional[BathReductionMap] = None
    reduction_visible: bool = False

    # Markovian analysis
    markovian_status: MarkovianStatus = "unclear"
    markovian_justification: str = ""

    # τ interpretation
    tau_interpretable: bool = False
    tau_interpretation: str = ""

    # Assumptions
    new_assumptions: List[str] = field(default_factory=list)
    assumption_severity: str = ""  # "mild", "moderate", "major", "theory_rebuilding"

    # Canon compatibility
    canon_compatibility: Optional[CanonCompatibility] = None

    # Blockers
    structural_blockers: List[str] = field(default_factory=list)

    # Classification
    status: BathStatus = "reject"

    # Nonclaims
    nonclaims: List[str] = field(default_factory=list)

    def passes_q2_criteria(self) -> bool:
        """Check the six minimum Q2 criteria (A-F from the prompt)."""
        a_dof_identified = bool(self.integrated_out_dof)
        b_why_hidden = bool(self.why_hidden)
        c_why_dissipative = bool(self.why_dissipative)
        d_grut_compatible = self.is_physically_motivated
        e_preserves_law = (
            self.canon_compatibility is not None
            and self.canon_compatibility.preserves_constitutive_law
        )
        f_sharpens_q1 = (
            self.reduction_map is not None
            and self.reduction_map.is_viable()
        )
        return all([a_dof_identified, b_why_hidden, c_why_dissipative,
                     d_grut_compatible, e_preserves_law, f_sharpens_q1])


@dataclass
class Q2Result:
    """Master result from Phase Q2 Bath Specification Test."""
    # Executive
    executive_determination: str = ""
    # One of:
    #   "best_physical_bath_identified"
    #   "several_viable_but_underdetermined"
    #   "only_formal_shell_survives"
    #   "no_defensible_bath"

    # Drude structural match (the key Q2 finding)
    drude_match: Optional[DrudeStructuralMatch] = None

    # Bath candidates
    bath_candidates: List[BathCandidate] = field(default_factory=list)
    best_candidate: str = ""
    best_candidate_status: str = ""

    # Hard blockers after Q2
    hard_blockers_after_q2: List[Dict[str, Any]] = field(default_factory=list)
    q1_blockers_inherited: List[str] = field(default_factory=list)
    q2_blocker_addressed: str = ""
    q2_blocker_resolution_level: str = ""
    # One of: "fully_resolved", "partially_sharpened", "renamed_not_resolved", "unresolved"

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)

    # Classification
    q2_classification: str = ""
    # One of:
    #   "bath_specification_program"
    #   "reduction_clarification"
    #   "structured_extension"
    #   "speculative_horizon"
    #   "failure"

    nonclaims: List[str] = field(default_factory=list)
    valid: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Export full result to dictionary."""
        return {
            "executive_determination": self.executive_determination,
            "best_candidate": self.best_candidate,
            "best_candidate_status": self.best_candidate_status,
            "drude_match": {
                "structural_match": self.drude_match.structural_match
                    if self.drude_match else False,
                "match_strength": self.drude_match.match_strength
                    if self.drude_match else "none",
                "implies_bath_type": self.drude_match.implies_bath_type
                    if self.drude_match else "",
            },
            "bath_candidates": [
                {
                    "name": b.name,
                    "label": b.label,
                    "status": b.status,
                    "is_physically_motivated": b.is_physically_motivated,
                    "markovian_status": b.markovian_status,
                    "tau_interpretable": b.tau_interpretable,
                    "assumption_severity": b.assumption_severity,
                    "passes_q2_criteria": b.passes_q2_criteria(),
                    "reduction_viable": (b.reduction_map.is_viable()
                                         if b.reduction_map else False),
                    "canon_compatible": (b.canon_compatibility.is_compatible()
                                         if b.canon_compatibility else False),
                    "structural_blockers": b.structural_blockers,
                }
                for b in self.bath_candidates
            ],
            "hard_blockers_after_q2": self.hard_blockers_after_q2,
            "q2_blocker_addressed": self.q2_blocker_addressed,
            "q2_blocker_resolution_level": self.q2_blocker_resolution_level,
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "q2_classification": self.q2_classification,
            "nonclaims": self.nonclaims,
            "valid": self.valid,
        }


# ================================================================
# Bath Candidate Builders
# ================================================================

def build_bath_a() -> BathCandidate:
    """Bath A — Gravitational-sector bath."""
    reduction = BathReductionMap(
        bath_family="A",
        parent_variables=(
            "Full interior metric perturbations h_μν plus memory field Φ "
            "in the linearised GRUT system around equilibrium"
        ),
        retained_slow_variable=(
            "Scalar memory trace Φ (the l=0 spherical mode of the "
            "memory response)"
        ),
        eliminated_dof=(
            "Higher multipole metric perturbations (l≥1), gravitational "
            "wave modes, and dynamical velocity/acceleration DOF (R, V) "
            "of the collapse solver"
        ),
        source_becomes_X=(
            "The gravitational source GM/R² projected onto the equilibrium "
            "background, with fast oscillations averaged out"
        ),
        why_first_order=(
            "The R-V kinetic modes oscillate on dynamical timescale "
            "t_dyn ~ √(R³/GM) which is fast compared to τ₀ when τ₀ >> t_dyn. "
            "Integrating out the fast kinetic modes produces an effective "
            "friction on the slow memory mode, yielding first-order relaxation."
        ),
        tau_interpretation="damping_timescale",
        markovian_status="approximately_markovian",
        is_local_in_time=True,
        assessment="partial_schematic",
        missing_pieces=[
            "Full covariant interior metric is not available (Phase V obstruction)",
            "Higher multipole mode spectrum not computed",
            "The separation t_dyn << τ₀ requires verification across mass range",
            "Coupling between gravitational modes and memory not fully specified",
        ],
    )

    canon = CanonCompatibility(
        preserves_constitutive_law=True,
        contradicts_strong_field=False,
        destabilizes_phenomenology=False,
        requires_failed_tensor_memory=False,
        imports_inconsistent_ontology=False,
        assessment="compatible",
    )

    return BathCandidate(
        name="A",
        label="Gravitational-Sector Bath",
        core_idea=(
            "Hidden or traced-out gravitational DOF (metric perturbations, "
            "interior oscillation modes, velocity/acceleration dynamics) "
            "act as the bath for the slow memory scalar Φ."
        ),
        integrated_out_dof=(
            "Interior oscillation modes at frequency ω_core ~ √(β_Q·GM/R_eq³), "
            "velocity/acceleration DOF (R, V) of the collapse state vector, "
            "higher-multipole metric perturbations"
        ),
        why_hidden=(
            "The collapse solver tracks [R, V, M_drive] as a coupled system, "
            "but the published constitutive law τ dΦ/dt + Φ = X retains only "
            "M_drive (≡ Φ). The R-V dynamics are 'integrated out' in the "
            "effective description."
        ),
        why_dissipative=(
            "Interior oscillation modes at ω_core are damped by γ_eff "
            "(solver dissipation + memory coupling). When these modes are "
            "averaged over, their effect on the slow memory mode is an "
            "effective friction."
        ),
        is_physically_motivated=True,
        is_formally_possible=True,
        reduction_map=reduction,
        reduction_visible=True,
        markovian_status="approximately_markovian",
        markovian_justification=(
            "If the interior oscillation modes decay on timescale "
            "1/γ_eff << τ₀, the bath correlation function decays fast "
            "relative to the memory evolution, justifying a Markovian "
            "approximation. This requires Q = ω_core/(2γ_eff) not too large."
        ),
        tau_interpretable=True,
        tau_interpretation=(
            "τ₀ is the effective damping timescale set by the coupling "
            "between the slow memory mode and the fast gravitational modes. "
            "The velocity dependence τ_eff = τ₀/(1+(|V/R|·τ₀)²) reflects "
            "that faster gravitational dynamics increases the effective "
            "dissipation rate."
        ),
        new_assumptions=[
            "There exists a timescale separation t_dyn << τ₀ justifying "
            "the Markovian approximation",
            "The R-V dynamics can be treated as a 'bath' for the memory mode",
            "Higher multipole modes do not qualitatively change the effective "
            "dynamics of the scalar trace",
            "The interior metric perturbation spectrum is well-approximated "
            "by the zeroth-order collapse ODE linearisation",
        ],
        assumption_severity="moderate",
        canon_compatibility=canon,
        structural_blockers=[
            "Covariant interior metric not available (Phase V obstruction)",
            "Full perturbation mode spectrum not computed",
            "Timescale separation t_dyn << τ₀ not verified across mass range",
            "Coupling constants between gravitational modes and memory not "
            "derived from action principle",
        ],
        status="viable_but_underdetermined",
        nonclaims=[
            "Bath A does NOT claim that the gravitational modes have been "
            "identified — it proposes them as candidates",
            "The R-V → Φ reduction is a schematic, not a derivation",
            "The Markovian approximation requires a timescale separation "
            "that has not been verified",
        ],
    )


def build_bath_b() -> BathCandidate:
    """Bath B — Matter-coupled bath."""
    reduction = BathReductionMap(
        bath_family="B",
        parent_variables="Memory field Φ coupled to baryonic matter DOF",
        retained_slow_variable="Memory scalar Φ",
        eliminated_dof="Baryonic microdegrees of freedom",
        source_becomes_X="Matter-sourced gravitational potential",
        why_first_order=(
            "If matter DOF equilibrate fast relative to τ₀, they produce "
            "an effective friction. But the published constitutive law "
            "has X = GM/R² (gravitational source), not a matter-dependent "
            "source. The matter bath would need to couple THROUGH gravity."
        ),
        tau_interpretation="unknown",
        markovian_status="unclear",
        is_local_in_time=True,
        assessment="formal_only",
        missing_pieces=[
            "No direct matter-memory coupling in published GRUT",
            "Source X is gravitational, not matter-dependent",
            "Baryonic DOF have no specified coupling to Φ",
            "Collapse dynamics is dust (pressureless) — no microphysics",
        ],
    )

    canon = CanonCompatibility(
        preserves_constitutive_law=True,
        contradicts_strong_field=False,
        destabilizes_phenomenology=False,
        requires_failed_tensor_memory=False,
        imports_inconsistent_ontology=True,
        assessment="tension",
    )

    return BathCandidate(
        name="B",
        label="Matter-Coupled Bath",
        core_idea=(
            "Ordinary matter or baryonic microdegrees of freedom coupled "
            "to the memory field act as the bath."
        ),
        integrated_out_dof="Baryonic matter microdegrees of freedom",
        why_hidden=(
            "Individual matter particles/modes are not tracked in the "
            "constitutive description; only their bulk gravitational "
            "effect enters through X = GM/R²"
        ),
        why_dissipative=(
            "Matter DOF would equilibrate fast, producing effective "
            "friction on the memory mode. However, the coupling path "
            "is indirect (through gravity), making the dissipation "
            "mechanism unclear."
        ),
        is_physically_motivated=False,
        is_formally_possible=True,
        reduction_map=reduction,
        reduction_visible=False,
        markovian_status="unclear",
        markovian_justification="No specified coupling timescale",
        tau_interpretable=False,
        tau_interpretation="",
        new_assumptions=[
            "Matter couples directly to memory (not in published GRUT)",
            "Baryonic microphysics generates an effective friction kernel",
            "The coupling preserves the form of the constitutive law",
        ],
        assumption_severity="major",
        canon_compatibility=canon,
        structural_blockers=[
            "No direct matter-memory coupling in published architecture",
            "Source X is gravitational, not matter-sourced",
            "Collapse uses pressureless dust — no baryon microphysics",
            "Would import matter-sector ontology not present in GRUT",
        ],
        status="formally_possible_but_physically_weak",
        nonclaims=[
            "Bath B is included for completeness but has weak physical "
            "motivation within the published GRUT architecture",
        ],
    )


def build_bath_c() -> BathCandidate:
    """Bath C — Self-bath / internal memory substructure.

    This is the STRONGEST Q2 candidate due to the Drude structural match.
    """
    reduction = BathReductionMap(
        bath_family="C",
        parent_variables=(
            "A spectral decomposition of the memory sector into modes "
            "{Φ_ω} with relaxation timescales 1/ω, weighted by spectral "
            "density ρ(ω). The physical field is Φ = ∫ρ(ω)Φ_ω dω."
        ),
        retained_slow_variable=(
            "The effective scalar memory Φ_eff — the spectral integral "
            "over all modes, dominated by modes near ω ~ 1/τ₀"
        ),
        eliminated_dof=(
            "Fast memory modes with ω >> 1/τ₀ (these equilibrate "
            "rapidly and contribute only as effective friction). "
            "In the Drude interpretation, Ω = 1/τ₀ is the spectral "
            "cutoff separating fast from slow modes."
        ),
        source_becomes_X=(
            "The gravitational source X = GM/R², which drives all "
            "spectral modes equally: (1/ω)dΦ_ω/dt + Φ_ω = X"
        ),
        why_first_order=(
            "Each spectral mode satisfies a first-order equation "
            "(1/ω)dΦ_ω/dt + Φ_ω = X. The effective equation for the "
            "spectral integral is first-order when the spectral density "
            "is dominated by a single pole (Drude/Lorentzian). The "
            "single-pole approximation produces τ_eff = τ₀/(1+(ω·τ₀)²), "
            "which is EXACTLY the published GRUT formula."
        ),
        tau_interpretation="effective_susceptibility_timescale",
        markovian_status="approximately_markovian",
        is_local_in_time=True,
        assessment="complete_schematic",
        missing_pieces=[
            "The spectral density ρ(ω) is not derived from GRUT microphysics",
            "What physical degrees of freedom the spectral modes represent "
            "is not specified (they could be gravitational, tensorial, or "
            "something else)",
            "The Drude form J(ω) ~ ω·Ω²/(ω²+Ω²) is the SIMPLEST single-pole "
            "spectral density — the actual spectral density may have richer "
            "structure (multi-pole, power-law, etc.)",
            "The connection between spectral modes and the Galley ghost field "
            "Φ₋ is not established",
        ],
    )

    canon = CanonCompatibility(
        preserves_constitutive_law=True,
        contradicts_strong_field=False,
        destabilizes_phenomenology=False,
        requires_failed_tensor_memory=False,
        imports_inconsistent_ontology=False,
        assessment="compatible",
    )

    return BathCandidate(
        name="C",
        label="Self-Bath / Internal Memory Substructure (Drude)",
        core_idea=(
            "Short-scale or fast modes of the memory sector itself are "
            "integrated out, leaving the slow constitutive mode. The "
            "published τ_eff formula has the exact Drude/Lorentzian form, "
            "which arises from a single-pole ohmic bath spectral density "
            "with cutoff Ω = 1/τ₀."
        ),
        integrated_out_dof=(
            "Fast memory modes with frequency ω >> Ω = 1/τ₀. These are "
            "internal substructure of the memory sector that equilibrate "
            "rapidly. Their spectral weight is described by the Drude "
            "density J(ω) = η·ω·Ω²/(ω²+Ω²)."
        ),
        why_hidden=(
            "The constitutive law τ dΦ/dt + Φ = X tracks only the "
            "effective (spectrally-integrated) memory field. Fast modes "
            "with ω >> 1/τ₀ have already equilibrated and contribute "
            "only through their integrated effect on the effective τ_eff."
        ),
        why_dissipative=(
            "Integrating out fast spectral modes produces effective "
            "friction on the slow mode. The Drude spectral density "
            "produces ohmic friction (proportional to velocity) in the "
            "low-frequency limit ω << Ω, which yields first-order "
            "relaxation. The published τ_eff formula IS the frequency-"
            "dependent susceptibility of this effective friction."
        ),
        is_physically_motivated=True,
        is_formally_possible=True,
        reduction_map=reduction,
        reduction_visible=True,
        markovian_status="approximately_markovian",
        markovian_justification=(
            "The Drude spectral density produces a bath correlation "
            "function that decays on timescale τ₀. When the system "
            "evolves on timescales >> τ₀, the Markovian approximation "
            "holds. When ω·τ₀ ~ 1 (resonance), non-Markovian corrections "
            "become important — this is precisely the regime where τ_eff "
            "deviates most from τ₀."
        ),
        tau_interpretable=True,
        tau_interpretation=(
            "τ₀ is the bath correlation time / spectral cutoff timescale. "
            "The velocity-dependent τ_eff = τ₀/(1+(ω·τ₀)²) is the "
            "effective susceptibility: at low frequencies (ω << 1/τ₀), "
            "τ_eff ≈ τ₀ (full relaxation); at high frequencies "
            "(ω >> 1/τ₀), τ_eff → 0 (instantaneous response). The "
            "crossover at ω = 1/τ₀ is the Drude cutoff."
        ),
        new_assumptions=[
            "The memory sector has internal spectral substructure beyond "
            "the single scalar trace (not contradicted by published GRUT, "
            "which is agnostic about substructure)",
            "The spectral density is approximately single-pole Drude "
            "(simplest assumption consistent with the published τ_eff form)",
            "The fast modes equilibrate on timescale ≪ τ₀ (Markovian "
            "regime for low-frequency dynamics)",
            "The spectral modes couple universally to the gravitational "
            "source X (each mode sees the same X)",
        ],
        assumption_severity="mild",
        canon_compatibility=canon,
        structural_blockers=[
            "Spectral density ρ(ω) not derived from first principles",
            "Physical identity of spectral modes unknown (gravitational? "
            "tensorial? something else?)",
            "Drude form is simplest assumption — actual spectral density "
            "may be more complex",
            "Connection to Galley ghost field Φ₋ not established",
            "Non-Markovian corrections at ω·τ₀ ~ 1 not computed",
        ],
        status="best_q2_candidate",
        nonclaims=[
            "Bath C does NOT derive the spectral density from GRUT microphysics "
            "— it observes that the published τ_eff has the Drude form",
            "The Drude structural match is an OBSERVATION, not a proof that "
            "the bath exists or has this spectral density",
            "The physical DOF comprising the spectral modes are not identified",
            "'Best Q2 candidate' means most structurally motivated, not confirmed",
            "The Markovian approximation requires verification across regimes",
        ],
    )


def build_bath_d() -> BathCandidate:
    """Bath D — Mixed bath (memory fast modes + gravitational modes)."""
    reduction = BathReductionMap(
        bath_family="D",
        parent_variables=(
            "Memory spectral modes {Φ_ω} PLUS interior oscillation modes "
            "(R-V dynamics) PLUS gravitational perturbation modes, all "
            "coupled to the slow memory scalar Φ_eff"
        ),
        retained_slow_variable=(
            "The effective scalar memory Φ_eff at frequencies ω << 1/τ₀"
        ),
        eliminated_dof=(
            "Fast memory submodes (ω >> 1/τ₀), interior velocity/acceleration "
            "dynamics (timescale t_dyn), and metric perturbation modes"
        ),
        source_becomes_X=(
            "The gravitational source X, with fast oscillations from all "
            "bath sectors averaged into the effective τ_eff"
        ),
        why_first_order=(
            "Multiple fast-mode sectors all contribute to the effective "
            "friction on the slow memory mode. If the combined bath spectral "
            "density is still approximately single-pole Drude, the result is "
            "the same first-order relaxation with the same τ_eff form. The "
            "mixed bath merely provides a richer microphysical origin for the "
            "effective spectral density."
        ),
        tau_interpretation="effective_susceptibility_timescale",
        markovian_status="approximately_markovian",
        is_local_in_time=True,
        assessment="partial_schematic",
        missing_pieces=[
            "How multiple bath sectors combine into an effective single-pole "
            "spectral density is not shown",
            "Whether gravitational and memory-internal modes are independent "
            "or coupled is unknown",
            "The relative spectral weights of different bath sectors are "
            "not determined",
        ],
    )

    canon = CanonCompatibility(
        preserves_constitutive_law=True,
        contradicts_strong_field=False,
        destabilizes_phenomenology=False,
        requires_failed_tensor_memory=False,
        imports_inconsistent_ontology=False,
        assessment="compatible",
    )

    return BathCandidate(
        name="D",
        label="Mixed Bath (Memory + Gravitational Modes)",
        core_idea=(
            "The effective bath is a combination of fast memory submodes "
            "and gravitational oscillation modes. The published τ_eff "
            "emerges from the combined spectral density of multiple "
            "sectors, not a single sector."
        ),
        integrated_out_dof=(
            "Fast memory submodes (Bath C contribution) plus interior "
            "gravitational oscillation modes (Bath A contribution), "
            "combined into a single effective spectral density"
        ),
        why_hidden=(
            "Both fast memory modes and gravitational oscillation modes "
            "are not tracked in the constitutive description. The "
            "published law sees only the integrated slow response."
        ),
        why_dissipative=(
            "Multiple fast-mode sectors independently produce friction "
            "contributions. Their combined effect yields the effective "
            "dissipation encoded in τ_eff."
        ),
        is_physically_motivated=True,
        is_formally_possible=True,
        reduction_map=reduction,
        reduction_visible=True,
        markovian_status="approximately_markovian",
        markovian_justification=(
            "If all fast-mode sectors have correlation times shorter than "
            "the slow-mode evolution timescale, the combined bath is "
            "Markovian. This is plausible if the Drude cutoff Ω = 1/τ₀ "
            "is the dominant timescale for all sectors."
        ),
        tau_interpretable=True,
        tau_interpretation=(
            "τ₀ is the combined correlation time of the mixed bath. "
            "The Lorentzian τ_eff form persists if the combined "
            "spectral density remains approximately single-pole."
        ),
        new_assumptions=[
            "Multiple bath sectors combine into approximately single-pole "
            "effective spectral density",
            "Gravitational and memory-internal modes are approximately "
            "independent (or their coupling does not change the effective "
            "single-pole character)",
            "All fast-mode sectors have correlation times ≤ τ₀",
        ],
        assumption_severity="moderate",
        canon_compatibility=canon,
        structural_blockers=[
            "How multiple sectors combine into a single Drude pole is not shown",
            "Relative spectral weights unknown",
            "More complex than Bath C with less structural motivation",
        ],
        status="viable_but_underdetermined",
        nonclaims=[
            "Bath D does NOT claim that the bath is mixed — it notes that "
            "a mixed bath is plausible but less parsimonious than Bath C",
            "The assumption that multiple sectors produce a single-pole "
            "density is unverified",
        ],
    )


def build_bath_e() -> BathCandidate:
    """Bath E — No physical bath (formal shell only)."""
    return BathCandidate(
        name="E",
        label="No Physical Bath (Formal Shell Only)",
        core_idea=(
            "The CTP/Galley structure remains a formal doubling device "
            "with no presently defensible physical bath interpretation. "
            "The doubled fields are variational auxiliaries, not physical "
            "degrees of freedom."
        ),
        integrated_out_dof="None specified",
        why_hidden="Not applicable — no bath posited",
        why_dissipative=(
            "Dissipation is encoded in the CTP boundary condition and "
            "Galley kernel, which are formal devices. The physical origin "
            "of dissipation remains unspecified."
        ),
        is_physically_motivated=False,
        is_formally_possible=True,
        reduction_map=None,
        reduction_visible=False,
        markovian_status="unclear",
        markovian_justification="No bath → no Markovian analysis",
        tau_interpretable=False,
        tau_interpretation="",
        new_assumptions=[
            "The CTP/Galley framework is a formal variational device only",
            "There is no underlying bath to discover",
            "Dissipation is constitutive and fundamental, not emergent",
        ],
        assumption_severity="mild",
        canon_compatibility=CanonCompatibility(
            preserves_constitutive_law=True,
            contradicts_strong_field=False,
            destabilizes_phenomenology=False,
            requires_failed_tensor_memory=False,
            imports_inconsistent_ontology=False,
            assessment="compatible",
        ),
        structural_blockers=[
            "Does not advance Q2 — leaves bath question unanswered",
            "Cannot explain the physical origin of τ₀",
            "Cannot explain the Drude/Lorentzian form of τ_eff",
        ],
        status="formally_possible_but_physically_weak",
        nonclaims=[
            "Bath E is not a failure — it is the conservative position that "
            "the bath question may not yet have a defensible answer",
            "The CTP/Galley formalism remains valid as a variational device "
            "regardless of whether a physical bath exists",
        ],
    )


# ================================================================
# Hard Blockers After Q2
# ================================================================

def build_hard_blockers_after_q2() -> List[Dict[str, Any]]:
    """Hard blockers that remain even if Q2 succeeds."""
    return [
        {
            "name": "no_born_rule",
            "type": "structural",
            "survives_q2": True,
            "description": (
                "No probability measure over outcomes. Even with a Drude "
                "bath identified, deriving Born probabilities requires "
                "measurement theory beyond Q2 scope."
            ),
        },
        {
            "name": "no_measurement_coupling",
            "type": "structural",
            "survives_q2": True,
            "description": "No detector-system interaction model.",
        },
        {
            "name": "no_interference_formalism",
            "type": "structural",
            "survives_q2": True,
            "description": (
                "No amplitude superposition, no phase, no interference law."
            ),
        },
        {
            "name": "no_particle_ontology",
            "type": "structural",
            "survives_q2": True,
            "description": "No Fock space, no asymptotic states.",
        },
        {
            "name": "no_experiment_framework",
            "type": "structural",
            "survives_q2": True,
            "description": "No contact with laboratory quantum experiments.",
        },
        {
            "name": "spectral_density_not_derived",
            "type": "currently_missing_potentially_extendable",
            "survives_q2": True,
            "description": (
                "The Drude spectral density J(ω) is INFERRED from the "
                "functional form of τ_eff, not derived from GRUT microphysics. "
                "What physical modes comprise the bath is unknown."
            ),
        },
        {
            "name": "loop_corrections_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q2": True,
            "description": (
                "Quantum corrections (CTP loop diagrams, Φ₋ fluctuations) "
                "are not computed. These would be the first quantum effects."
            ),
        },
        {
            "name": "metric_doubling_ghost",
            "type": "unknown",
            "survives_q2": True,
            "description": (
                "Doubled-metric sector ghost status undetermined."
            ),
        },
        {
            "name": "noise_spectrum_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q2": True,
            "description": (
                "A Drude bath would produce a fluctuation-dissipation "
                "noise spectrum. This noise has not been computed or "
                "identified in GRUT. Its detection would be the first "
                "empirical test of the bath interpretation."
            ),
        },
    ]


# ================================================================
# Master Builder
# ================================================================

def run_q2_assessment() -> Q2Result:
    """Execute Phase Q2 Bath Specification and Reduction Test."""

    # Build Drude structural match analysis
    drude_match = DrudeStructuralMatch()

    # Build bath candidates
    bath_a = build_bath_a()
    bath_b = build_bath_b()
    bath_c = build_bath_c()
    bath_d = build_bath_d()
    bath_e = build_bath_e()

    candidates = [bath_a, bath_b, bath_c, bath_d, bath_e]

    # Identify best candidate
    best = "C"
    best_status = "best_q2_candidate"

    # Hard blockers
    hard_blockers = build_hard_blockers_after_q2()

    # Q2 blocker resolution level
    # Q1 listed "bath_dof_unspecified" as a blocker.
    # Q2 identifies a structural candidate (Drude self-bath) but does not
    # derive it from first principles. This is a partial sharpening.
    blocker_resolution = "partially_sharpened"

    # Safe claims
    safe_claims = [
        "The published τ_eff = τ₀/(1+(ω·τ₀)²) has the exact functional "
        "form of the Lorentzian susceptibility χ(ω) = 1/(1+(ω/Ω)²).",

        "In open-system theory, this Lorentzian form arises from a Drude "
        "(single-pole ohmic) bath spectral density J(ω) = η·ω·Ω²/(ω²+Ω²) "
        "with cutoff Ω = 1/τ₀.",

        "This structural match identifies the TYPE of bath that would produce "
        "the published dynamics: a single-pole ohmic bath with Lorentzian cutoff.",

        "The structural identity ω₀·τ_eff = 1 at equilibrium corresponds to "
        "the system frequency matching the bath cutoff: ω₀ = Ω = 1/τ₀.",

        "The interior PDE dispersion relation contains the factor "
        "1/(1+iωτ_eff), which is the single-pole memory susceptibility "
        "consistent with the Drude bath interpretation.",

        "Bath C (self-bath / internal memory substructure) is the most "
        "parsimonious candidate: it requires only that the memory sector "
        "has internal spectral substructure, which is not contradicted by "
        "published GRUT.",

        "All Appendix C structural blockers and all Q1 hard blockers "
        "except 'bath_dof_unspecified' remain fully in force after Q2.",

        "The Q1 blocker 'bath_dof_unspecified' is partially sharpened: "
        "the bath TYPE is identified (Drude) but the physical DOF "
        "comprising it are not.",
    ]

    # Unsafe claims
    unsafe_claims = [
        "The Drude bath has been derived from GRUT first principles.",
        "The spectral density is known or validated.",
        "The physical bath DOF are identified.",
        "The bath interpretation is confirmed (it is a structural candidate).",
        "Q2 resolves the bath specification problem (it partially sharpens it).",
        "The noise spectrum of the Drude bath has been computed or detected.",
        "Q2 provides quantum corrections to GRUT.",
        "GRUT has a validated open-system quantum description.",
        "Any Appendix C blocker is resolved.",
        "The Markovian approximation holds in all regimes.",
        "The Drude form is exact (it may be the leading-order term of a "
        "richer spectral density).",
    ]

    result = Q2Result(
        executive_determination="best_physical_bath_identified",
        drude_match=drude_match,
        bath_candidates=candidates,
        best_candidate=best,
        best_candidate_status=best_status,
        hard_blockers_after_q2=hard_blockers,
        q1_blockers_inherited=list(Q1_HARD_BLOCKERS_INHERITED),
        q2_blocker_addressed=Q2_TARGET_BLOCKER,
        q2_blocker_resolution_level=blocker_resolution,
        safe_claims=safe_claims,
        unsafe_claims=unsafe_claims,
        q2_classification="bath_specification_program",
        nonclaims=[
            "This assessment does NOT claim the Drude bath is correct.",
            "The structural match is an observation, not a derivation.",
            "'Best Q2 candidate' means most structurally motivated, not validated.",
            "The physical DOF of the bath are not identified.",
            "Q2 partially sharpens but does not resolve the bath question.",
            "All Q1 and Appendix C constraints remain locked.",
            "No quantum corrections, noise spectra, or measurement theory "
            "is provided by Q2.",
            "The Drude form may be only the leading-order approximation "
            "to a richer spectral structure.",
        ],
        valid=True,
    )

    _validate_q2(result)
    return result


def _validate_q2(result: Q2Result) -> None:
    """Validate that Q2 result does not overclaim."""
    # Executive must be in allowed set
    allowed_executives = {
        "best_physical_bath_identified",
        "several_viable_but_underdetermined",
        "only_formal_shell_survives",
        "no_defensible_bath",
    }
    if result.executive_determination not in allowed_executives:
        raise ValueError(
            f"Executive '{result.executive_determination}' not in {allowed_executives}"
        )

    # Classification must be in allowed set
    allowed_classifications = {
        "bath_specification_program",
        "reduction_clarification",
        "structured_extension",
        "speculative_horizon",
        "failure",
    }
    if result.q2_classification not in allowed_classifications:
        raise ValueError(
            f"Classification '{result.q2_classification}' not in "
            f"{allowed_classifications}"
        )

    # Blocker resolution must not be "fully_resolved"
    # (Q2 cannot fully resolve the bath question)
    if result.q2_blocker_resolution_level == "fully_resolved":
        raise ValueError(
            "Q2 CANNOT claim to fully resolve the bath specification. "
            "The spectral density is inferred from τ_eff form, not derived."
        )

    # Best candidate must pass minimum criteria
    for b in result.bath_candidates:
        if b.status == "best_q2_candidate":
            if not b.passes_q2_criteria():
                raise ValueError(
                    f"Bath '{b.name}' is best_q2_candidate but does not "
                    f"pass minimum Q2 criteria."
                )

    # No forbidden claim in safe claims
    for claim in result.safe_claims:
        claim_lower = claim.lower()
        if "derives" in claim_lower and "born" in claim_lower:
            raise ValueError(f"Safe claim appears to derive Born rule: {claim}")
        if "proves" in claim_lower and "bath" in claim_lower:
            raise ValueError(f"Safe claim appears to prove bath: {claim}")
