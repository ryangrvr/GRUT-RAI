"""GRUT Phase Q3 — Interior Mode / Spectral Origin Test.

Determines whether the published GRUT interior dynamics can supply a
microphysical origin for the Q2 Drude/Lorentzian bath-type clue.

CENTRAL FINDING:
  The published interior PDE dispersion relation,

    F(ω) = ω² - ω₀² - 2α·ω_g² / (1 + iωτ)

  EXPLICITLY CONTAINS the single-pole Lorentzian 1/(1+iωτ) as a
  derived structural element. The memory-mediated damping rate,

    γ_mem = α·ω²·τ / (2·(1 + (ωτ)²))

  is the imaginary part of this response. The Q2 Drude/Lorentzian
  clue is ALGEBRAICALLY GROUNDED in the published interior sector.

CRITICAL DISTINCTION — ALGEBRAIC GROUNDING VS DERIVATION:
  The single-pole form appears BECAUSE the memory equation is first-order.
  This is an algebraic consequence, not a first-principles derivation.
  The circularity is: the Lorentzian arises from the constitutive law,
  which is what we are trying to derive from a deeper substrate.

  However, non-circular elements exist:
  - The coupling constant 2αω_g² is derived from gravitational structure
  - The three-pole structure (1 relaxation + 2 oscillatory) is emergent
  - The structural identity ω₀τ = 1 is a constraint, not an input
  - The damping rate formula is derived from linearisation, not postulated

STATUS: PHASE Q3 — SPECTRAL ORIGIN
  Route B (Interior PDE / Susceptibility) is the strongest Q3 candidate.
  The Drude/Lorentzian clue has algebraic grounding in the published GRUT
  interior sector but is NOT derived from a deeper substrate.

LOCKED BOUNDARIES:
  Appendix C: No amplitudes, Born rule, interference, measurement.
  Q1: CTP/Galley recovery shell; exact at tree level.
  Q2: Drude/Lorentzian bath-type identification; structural match.

NONCLAIMS:
  1. This module does NOT derive the bath from first principles.
  2. The algebraic grounding is NOT a derivation of the first-order law.
  3. The circularity (first-order → Lorentzian → first-order) is explicit.
  4. No quantum corrections, noise spectra, or measurement theory.
  5. "Algebraic grounding" means the Lorentzian is present in the published
     PDE, not that the PDE explains why the memory law is first-order.
  6. The three-pole structure is the FULL content of the linearised interior;
     whether additional modes exist (from tensor memory, non-radial coupling,
     etc.) is undetermined.

See: interior_pde.py, interior_waves.py, collapse.py,
     quantum_program_q1.py, quantum_program_q2.py for upstream structures.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Literal


# ================================================================
# Constants — Locked Inheritance
# ================================================================

# Q2 Drude/Lorentzian structural match
Q2_DRUDE_MATCH = "tau_eff = tau_0 / (1 + (omega * tau_0)^2)"
Q2_DRUDE_SPECTRAL_DENSITY = "J(omega) = eta * omega * Omega^2 / (omega^2 + Omega^2)"

# Published interior PDE dispersion relation
INTERIOR_DISPERSION = "F(omega) = omega^2 - omega_0^2 - 2*alpha*omega_g^2 / (1 + i*omega*tau)"

# Memory-mediated damping (from interior_waves.py)
MEMORY_DAMPING_FORMULA = "gamma_mem = alpha * omega^2 * tau / (2 * (1 + (omega*tau)^2))"

# The single-pole susceptibility (the Lorentzian kernel)
SINGLE_POLE_SUSCEPTIBILITY = "chi_mem(omega) = 1 / (1 + i*omega*tau)"

# Structural identity at equilibrium
STRUCTURAL_IDENTITY = "omega_0 * tau_eff = 1"

# Canonical GRUT parameters
ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0

# Blockers inherited from Q1 and Q2
Q2_HARD_BLOCKERS_INHERITED = [
    "no_born_rule",
    "no_measurement_coupling",
    "no_interference_formalism",
    "no_particle_ontology",
    "no_experiment_framework",
    "spectral_density_not_derived",
    "loop_corrections_unknown",
    "metric_doubling_ghost",
    "noise_spectrum_unknown",
]

Q3_FORBIDDEN_CLAIMS = [
    "derives_first_order_law",
    "derives_bath_from_first_principles",
    "breaks_circularity",
    "derives_born_rule",
    "derives_interference",
    "derives_measurement",
    "resolves_appendix_c",
    "completes_quantum_program",
    "computes_noise_spectrum",
]


# ================================================================
# Type Definitions
# ================================================================

RouteStatus = Literal[
    "best_q3_candidate",
    "viable_but_underdetermined",
    "structurally_suggestive_only",
    "reject",
]

TransferFunctionType = Literal[
    "single_pole_lorentzian",
    "approximately_single_pole",
    "multi_pole",
    "oscillatory_plus_relaxation",
    "underdetermined",
]

GroundingLevel = Literal[
    "algebraic_grounding",
    "derivational",
    "structural_match_only",
    "no_grounding",
]


# ================================================================
# Data Structures
# ================================================================

@dataclass
class PoleAnalysis:
    """Analysis of the pole structure from the interior dispersion relation.

    The dispersion relation F(ω) = ω² - ω₀² - 2αω_g²/(1+iωτ) = 0,
    when cleared of denominators, is a CUBIC in ω:

      iτω³ + ω² - iτω₀²ω - (ω₀² + 2αω_g²) = 0

    This has exactly three roots (poles):
    - Two complex conjugate: oscillatory-damped (BDCC vibration modes)
    - One pure imaginary: relaxation mode (memory sector)
    """
    # Characteristic equation
    characteristic_equation: str = (
        "i*tau*omega^3 + omega^2 - i*tau*omega_0^2*omega "
        "- (omega_0^2 + 2*alpha*omega_g^2) = 0"
    )
    polynomial_degree: int = 3

    # Pole structure
    n_oscillatory_poles: int = 2  # complex conjugate pair
    n_relaxation_poles: int = 1   # pure imaginary (memory mode)
    total_poles: int = 3

    # Which pole is the Lorentzian?
    lorentzian_pole_origin: str = (
        "The relaxation pole arises from the memory sector. Its location "
        "ω = -i/τ is the pole of the susceptibility 1/(1+iωτ). This is "
        "the algebraic origin of the single-pole Lorentzian structure."
    )

    # Circularity analysis
    is_circular: bool = True
    circularity_description: str = (
        "The relaxation pole ω = -i/τ exists BECAUSE the memory equation "
        "is first-order (τ dΦ/dt + Φ = X). A first-order ODE has a single "
        "exponential decay mode with timescale τ. In frequency space, this "
        "is a single pole at ω = -i/τ, which is the Lorentzian. The "
        "circularity: we are 'deriving' the Lorentzian from the equation "
        "whose origin we are trying to explain."
    )

    # Non-circular elements
    non_circular_elements: List[str] = field(default_factory=lambda: [
        "The coupling constant 2αω_g² between memory and oscillatory "
        "sectors is derived from gravitational structure (linearisation "
        "of the collapse equations around equilibrium)",
        "The three-pole structure (1 relaxation + 2 oscillatory) is "
        "emergent from the coupled [R, V, M_drive] system",
        "The structural identity ω₀τ = 1 at equilibrium is a derived "
        "constraint from the parameter relationships, not an input",
        "The damping rate γ_mem = αω²τ/(2(1+(ωτ)²)) is derived from "
        "the linearisation, not postulated separately",
        "The Q-factor and response classification (reactive/dissipative/"
        "mixed) follow from the pole locations, not from the memory "
        "equation alone",
    ])


@dataclass
class TransferFunctionAnalysis:
    """Transfer-function analysis for a spectral-origin route."""
    route: str
    quantity_analyzed: str = ""
    fast_variable: str = ""
    slow_variable: str = ""
    response_function: str = ""
    transfer_function_type: TransferFunctionType = "underdetermined"
    is_single_pole: bool = False
    is_approximately_single_pole: bool = False
    pole_count: int = 0
    dominant_pole_location: str = ""
    tau_interpretation: str = ""
    approximations_needed: List[str] = field(default_factory=list)
    assessment: str = ""

    def is_viable(self) -> bool:
        return (
            bool(self.response_function)
            and self.transfer_function_type != "underdetermined"
            and bool(self.tau_interpretation)
        )


@dataclass
class CircularityAudit:
    """Audit of the circularity in the spectral-origin claim."""
    has_circularity: bool = True
    circular_chain: str = ""
    non_circular_elements: List[str] = field(default_factory=list)
    net_assessment: str = ""  # "pure_circularity", "partial_circularity", "non_circular"


@dataclass
class SpectralOriginRoute:
    """A candidate route for grounding the Q2 Drude clue in GRUT internals."""
    name: str
    label: str
    core_idea: str

    # GRUT structure used
    grut_structure: str = ""
    structure_explicit_in_canon: bool = False
    structure_source: str = ""  # file/module reference

    # Why single-pole
    why_single_pole: str = ""

    # Transfer function
    transfer_function: Optional[TransferFunctionAnalysis] = None

    # Pole analysis
    pole_analysis: Optional[PoleAnalysis] = None

    # Circularity
    circularity: Optional[CircularityAudit] = None

    # Grounding level
    grounding_level: GroundingLevel = "no_grounding"

    # Route classification
    derivationally_visible: bool = False
    structurally_suggestive: bool = False

    # Assumptions
    new_assumptions: List[str] = field(default_factory=list)
    assumption_severity: str = ""

    # Canon compatibility
    preserves_constitutive_law: bool = False
    compatible_with_strong_field: bool = False
    compatible_with_phenomenology: bool = False

    # Blockers
    structural_blockers: List[str] = field(default_factory=list)

    # Status
    status: RouteStatus = "reject"

    # Nonclaims
    nonclaims: List[str] = field(default_factory=list)

    def passes_q3_criteria(self) -> bool:
        """Check the six minimum Q3 criteria (A-F)."""
        a_modes_identified = bool(self.grut_structure)
        b_genuinely_grut = self.structure_explicit_in_canon
        c_why_single_pole = bool(self.why_single_pole)
        d_grounding = self.grounding_level in (
            "algebraic_grounding", "derivational"
        )
        e_canon_ok = (self.preserves_constitutive_law
                       and self.compatible_with_strong_field)
        f_sharpens_q2 = self.grounding_level != "structural_match_only"
        return all([a_modes_identified, b_genuinely_grut, c_why_single_pole,
                     d_grounding, e_canon_ok, f_sharpens_q2])


@dataclass
class InteriorLinearizationResult:
    """Result of inspecting the linearised interior for single-pole dominance."""
    # Mode content
    characteristic_degree: int = 3
    n_relaxation_modes: int = 1
    n_oscillatory_modes: int = 2
    single_pole_dominant: bool = False
    single_pole_reason: str = ""

    # Spectrum character
    spectrum_broad: bool = False
    spectrum_oscillatory: bool = True
    spectrum_overdamped: bool = False
    spectrum_underdetermined: bool = False

    # Q2 compatibility
    drude_compatible: bool = False
    drude_compatibility_reason: str = ""

    # Evidence quality
    evidence_for_single_pole: str = ""
    evidence_against_single_pole: str = ""


@dataclass
class Q3Result:
    """Master result from Phase Q3 Spectral Origin Test."""
    executive_determination: str = ""
    # One of:
    #   "strongest_spectral_origin_identified"
    #   "several_routes_viable_underdetermined"
    #   "structural_suggestiveness_only"
    #   "no_defensible_interior_origin"

    # Routes
    routes: List[SpectralOriginRoute] = field(default_factory=list)
    best_route: str = ""
    best_route_status: str = ""
    best_route_grounding: str = ""

    # Interior linearization
    linearization: Optional[InteriorLinearizationResult] = None

    # Hard blockers after Q3
    hard_blockers_after_q3: List[Dict[str, Any]] = field(default_factory=list)

    # Circularity
    circularity_acknowledged: bool = True
    circularity_description: str = ""

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)

    # Classification
    q3_classification: str = ""
    # One of:
    #   "spectral_origin_program"
    #   "algebraic_grounding"
    #   "reduction_clarification"
    #   "speculative_horizon"
    #   "failure"

    nonclaims: List[str] = field(default_factory=list)
    valid: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "executive_determination": self.executive_determination,
            "best_route": self.best_route,
            "best_route_status": self.best_route_status,
            "best_route_grounding": self.best_route_grounding,
            "circularity_acknowledged": self.circularity_acknowledged,
            "routes": [
                {
                    "name": r.name,
                    "label": r.label,
                    "status": r.status,
                    "grounding_level": r.grounding_level,
                    "passes_q3_criteria": r.passes_q3_criteria(),
                    "structure_explicit_in_canon": r.structure_explicit_in_canon,
                    "assumption_severity": r.assumption_severity,
                    "structural_blockers": r.structural_blockers,
                }
                for r in self.routes
            ],
            "linearization": {
                "characteristic_degree": self.linearization.characteristic_degree,
                "n_relaxation_modes": self.linearization.n_relaxation_modes,
                "n_oscillatory_modes": self.linearization.n_oscillatory_modes,
                "single_pole_dominant": self.linearization.single_pole_dominant,
                "drude_compatible": self.linearization.drude_compatible,
            } if self.linearization else None,
            "hard_blockers_after_q3": self.hard_blockers_after_q3,
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "q3_classification": self.q3_classification,
            "nonclaims": self.nonclaims,
            "valid": self.valid,
        }


# ================================================================
# Route Builders
# ================================================================

def build_route_a() -> SpectralOriginRoute:
    """Route A — Linearized self-mode route."""
    tf = TransferFunctionAnalysis(
        route="A",
        quantity_analyzed=(
            "Memory field Φ response to perturbation δX in the source"
        ),
        fast_variable="None (memory has only one scalar mode)",
        slow_variable="Φ (the memory scalar)",
        response_function=(
            "δΦ(ω)/δX(ω) = 1/(1 + iωτ) — the single-pole susceptibility "
            "of the first-order memory equation"
        ),
        transfer_function_type="single_pole_lorentzian",
        is_single_pole=True,
        pole_count=1,
        dominant_pole_location="ω = -i/τ (pure relaxation)",
        tau_interpretation=(
            "τ is the relaxation timescale of the memory ODE; the pole "
            "location is directly the inverse relaxation time"
        ),
        approximations_needed=[
            "Memory field is treated as a single scalar (no tensor or "
            "vector substructure)",
            "Linearisation around equilibrium Φ = X",
        ],
        assessment=(
            "The self-mode transfer function IS the Lorentzian by "
            "construction. This is algebraically exact but fully circular: "
            "the first-order ODE τ dΦ/dt + Φ = X has transfer function "
            "1/(1+iωτ) by definition."
        ),
    )

    circ = CircularityAudit(
        has_circularity=True,
        circular_chain=(
            "First-order ODE → single exponential → Laplace transform → "
            "1/(1+sτ) → Lorentzian. This is algebraic identity, "
            "not a derivation of why the ODE is first-order."
        ),
        non_circular_elements=[],
        net_assessment="pure_circularity",
    )

    return SpectralOriginRoute(
        name="A",
        label="Linearized Self-Mode Route",
        core_idea=(
            "The linearized fast modes of the memory sector yield a "
            "single-pole relaxation response."
        ),
        grut_structure="Memory equation τ dΦ/dt + Φ = X",
        structure_explicit_in_canon=True,
        structure_source="collapse.py (M_drive ODE), operators.py (_tau_eff)",
        why_single_pole=(
            "A first-order ODE has exactly one relaxation mode. Its "
            "transfer function is 1/(1+iωτ) by algebraic identity."
        ),
        transfer_function=tf,
        pole_analysis=None,
        circularity=circ,
        grounding_level="structural_match_only",
        derivationally_visible=False,
        structurally_suggestive=True,
        new_assumptions=[],
        assumption_severity="mild",
        preserves_constitutive_law=True,
        compatible_with_strong_field=True,
        compatible_with_phenomenology=True,
        structural_blockers=[
            "Purely circular: the Lorentzian is the first-order ODE in "
            "frequency space, not a derivation of it",
            "No fast modes exist in the scalar memory sector alone — "
            "there is only one mode",
        ],
        status="structurally_suggestive_only",
        nonclaims=[
            "Route A restates the Q2 match in frequency-domain language "
            "but does not ground it in interior mode structure",
        ],
    )


def build_route_b() -> SpectralOriginRoute:
    """Route B — Interior PDE / susceptibility route.

    This is the STRONGEST Q3 candidate.
    """
    tf = TransferFunctionAnalysis(
        route="B",
        quantity_analyzed=(
            "Coupled [R, V, M_drive] perturbation response about the "
            "BDCC equilibrium (R_eq, V=0, M_drive=a_grav)"
        ),
        fast_variable=(
            "R-V oscillatory modes (BDCC vibration at ω_core)"
        ),
        slow_variable=(
            "M_drive relaxation mode (memory sector at rate 1/τ_eff)"
        ),
        response_function=(
            "The memory-sector contribution to the dispersion relation: "
            "χ_mem(ω) = 2α·ω_g² / (1 + iωτ). This is a Lorentzian with "
            "coupling strength 2αω_g² and pole at ω = -i/τ."
        ),
        transfer_function_type="oscillatory_plus_relaxation",
        is_single_pole=False,
        is_approximately_single_pole=True,
        pole_count=3,
        dominant_pole_location=(
            "Memory relaxation pole at ω ≈ -i/τ; oscillatory poles at "
            "ω ≈ ±ω_eff - i·γ_eff where ω_eff and γ_eff depend on "
            "mass and coupling parameters"
        ),
        tau_interpretation=(
            "τ is the pole location of the memory susceptibility "
            "χ_mem(ω) = 1/(1+iωτ) in the coupled three-variable system. "
            "It is simultaneously: (1) the constitutive relaxation time, "
            "(2) the susceptibility pole, (3) the Drude cutoff. These "
            "are algebraically identical."
        ),
        approximations_needed=[
            "Linearisation around equilibrium (small perturbations only)",
            "Spherical symmetry (radial modes only)",
            "Scalar memory (no tensor or vector substructure)",
            "Single-shell approximation (no inter-shell coupling)",
            "τ perturbations neglected (zeroth order in δτ)",
        ],
        assessment=(
            "The three-pole structure (1 relaxation + 2 oscillatory) is "
            "DERIVED from the linearised coupled equations, not assumed. "
            "The memory susceptibility 1/(1+iωτ) appears as the memory "
            "sector's contribution to the full dispersion relation. The "
            "circularity is partial: the single-pole form follows from "
            "the first-order memory law, but the coupling constant, "
            "damping rates, and mode structure are derived."
        ),
    )

    poles = PoleAnalysis()

    circ = CircularityAudit(
        has_circularity=True,
        circular_chain=(
            "Memory ODE is first-order → memory contribution to dispersion "
            "is 1/(1+iωτ) → single-pole Lorentzian. The single-pole form "
            "is algebraically guaranteed by the first-order axiom."
        ),
        non_circular_elements=[
            "Coupling constant 2αω_g² is derived from gravitational structure",
            "Three-pole structure is emergent from coupled [R,V,M_drive] system",
            "Structural identity ω₀τ = 1 is a constraint, not an input",
            "Damping rate γ_mem = αω²τ/(2(1+(ωτ)²)) is derived from "
            "linearisation of the coupled system",
            "Q-factor and response classification follow from pole locations",
            "The velocity-dependent τ_eff = τ₀/(1+(|V/R|τ₀)²) is a "
            "constitutive input, but its Lorentzian form is consistent with "
            "(and independently motivates) the Drude interpretation",
        ],
        net_assessment="partial_circularity",
    )

    return SpectralOriginRoute(
        name="B",
        label="Interior PDE / Susceptibility Route",
        core_idea=(
            "The published interior PDE dispersion relation explicitly "
            "contains the single-pole Lorentzian 1/(1+iωτ) as the memory "
            "sector's susceptibility contribution. The full three-pole "
            "structure (1 relaxation + 2 oscillatory) is derived from "
            "linearising the coupled [R, V, M_drive] system."
        ),
        grut_structure=(
            "Interior PDE dispersion relation: "
            "F(ω) = ω² - ω₀² - 2αω_g²/(1+iωτ) = 0. "
            "Memory-mediated damping: γ_mem = αω²τ/(2(1+(ωτ)²))."
        ),
        structure_explicit_in_canon=True,
        structure_source=(
            "interior_pde.py: dispersion_relation(), solve_dispersion(); "
            "interior_waves.py: memory_mediated_damping()"
        ),
        why_single_pole=(
            "The memory contribution to the dispersion relation is "
            "2αω_g²/(1+iωτ), which is a Lorentzian with pole at ω=-i/τ. "
            "This arises because the memory ODE is first-order. The full "
            "characteristic equation is cubic (three poles total): "
            "the memory relaxation pole plus two oscillatory BDCC modes."
        ),
        transfer_function=tf,
        pole_analysis=poles,
        circularity=circ,
        grounding_level="algebraic_grounding",
        derivationally_visible=True,
        structurally_suggestive=True,
        new_assumptions=[
            "Linearisation valid (small perturbations about equilibrium)",
            "Spherical symmetry, radial modes only",
            "τ perturbations are higher-order and neglected",
        ],
        assumption_severity="mild",
        preserves_constitutive_law=True,
        compatible_with_strong_field=True,
        compatible_with_phenomenology=True,
        structural_blockers=[
            "Partial circularity: single-pole form follows from "
            "first-order axiom, not from a deeper principle",
            "Coupling constant 2αω_g² is derived but its fundamental "
            "origin (why α_vac = 1/3) is not explained",
            "Full covariant interior metric not available — linearisation "
            "is based on the collapse ODE, not a wave equation",
            "Additional poles from tensor memory, non-radial modes, or "
            "non-linear coupling could modify the spectrum",
        ],
        status="best_q3_candidate",
        nonclaims=[
            "Route B provides ALGEBRAIC GROUNDING for the Q2 Drude clue, "
            "not a first-principles derivation",
            "The single-pole form is algebraically guaranteed by the "
            "first-order memory law — this is partially circular",
            "The coupling constant, damping rates, and mode structure "
            "ARE non-circular derived elements",
            "Additional interior modes beyond the linearised [R,V,M_drive] "
            "system could modify the effective spectral density",
        ],
    )


def build_route_c() -> SpectralOriginRoute:
    """Route C — Gravitational interior mode route."""
    tf = TransferFunctionAnalysis(
        route="C",
        quantity_analyzed=(
            "Gravitational perturbation modes h_μν in the BDCC interior"
        ),
        fast_variable="Metric perturbation modes (l≥2 multipoles)",
        slow_variable="Background geometry + memory field",
        response_function="Not available — covariant interior metric unknown",
        transfer_function_type="underdetermined",
        is_single_pole=False,
        pole_count=0,
        dominant_pole_location="Unknown",
        tau_interpretation="unknown",
        approximations_needed=[
            "Covariant interior metric (Phase V obstruction — missing)",
            "GR perturbation theory on GRUT-modified background",
            "Mode decomposition in non-Schwarzschild geometry",
        ],
        assessment=(
            "Cannot be evaluated: the covariant interior metric is not "
            "available (Phase V lapse obstruction). Without the metric, "
            "gravitational perturbation modes cannot be computed."
        ),
    )

    return SpectralOriginRoute(
        name="C",
        label="Gravitational Interior Mode Route",
        core_idea=(
            "Gravitational perturbation modes in the BDCC interior "
            "generate the effective single-pole response after reduction."
        ),
        grut_structure=(
            "Interior gravitational modes — but the covariant interior "
            "metric is not available (Phase V obstruction)"
        ),
        structure_explicit_in_canon=False,
        structure_source="NOT AVAILABLE: Phase V lapse obstruction",
        why_single_pole="Cannot be determined — modes not computable",
        transfer_function=tf,
        circularity=None,
        grounding_level="no_grounding",
        derivationally_visible=False,
        structurally_suggestive=False,
        new_assumptions=[
            "Covariant interior metric exists and is computable",
            "Gravitational modes have a spectral density approximating Drude",
        ],
        assumption_severity="major",
        preserves_constitutive_law=True,
        compatible_with_strong_field=True,
        compatible_with_phenomenology=True,
        structural_blockers=[
            "Covariant interior metric not available (Phase V obstruction)",
            "Cannot compute gravitational mode spectrum",
            "Cannot verify single-pole dominance without mode content",
        ],
        status="viable_but_underdetermined",
        nonclaims=[
            "Route C cannot be evaluated at present — the required "
            "covariant interior metric is a missing closure",
            "This does NOT mean gravitational modes are irrelevant — "
            "only that they cannot currently be computed",
        ],
    )


def build_route_d() -> SpectralOriginRoute:
    """Route D — Mixed fast-sector route."""
    tf = TransferFunctionAnalysis(
        route="D",
        quantity_analyzed=(
            "Combined response of memory + gravitational fast modes"
        ),
        fast_variable="Memory fast modes + gravitational perturbation modes",
        slow_variable="Effective scalar memory at ω << 1/τ₀",
        response_function=(
            "Would be the sum of memory susceptibility (known: 1/(1+iωτ)) "
            "plus gravitational mode contribution (unknown)"
        ),
        transfer_function_type="underdetermined",
        is_single_pole=False,
        pole_count=0,
        dominant_pole_location="Unknown (gravitational contribution missing)",
        tau_interpretation="unknown",
        approximations_needed=[
            "All Route B approximations PLUS covariant metric for "
            "gravitational sector",
        ],
        assessment=(
            "Inherits Route B's memory susceptibility (known) but cannot "
            "add the gravitational contribution (Route C blocked). Reduces "
            "to Route B at present."
        ),
    )

    return SpectralOriginRoute(
        name="D",
        label="Mixed Fast-Sector Route",
        core_idea=(
            "Combination of memory fast modes and gravitational submodes "
            "produces the effective Drude response."
        ),
        grut_structure=(
            "Route B's linearised [R,V,M_drive] system plus unknown "
            "gravitational perturbation contribution"
        ),
        structure_explicit_in_canon=False,
        structure_source="Partial: interior_pde.py (memory part only)",
        why_single_pole=(
            "Memory contribution is single-pole; gravitational contribution "
            "unknown. Whether the combined spectrum remains approximately "
            "single-pole cannot be determined."
        ),
        transfer_function=tf,
        circularity=None,
        grounding_level="no_grounding",
        derivationally_visible=False,
        structurally_suggestive=True,
        new_assumptions=[
            "Gravitational modes contribute without destroying single-pole "
            "character (unverifiable at present)",
            "Combined spectral density remains approximately Drude",
        ],
        assumption_severity="moderate",
        preserves_constitutive_law=True,
        compatible_with_strong_field=True,
        compatible_with_phenomenology=True,
        structural_blockers=[
            "Gravitational contribution unknown (Route C blocked)",
            "Whether multi-sector combination preserves single-pole "
            "character is undetermined",
            "Reduces to Route B at present",
        ],
        status="viable_but_underdetermined",
        nonclaims=[
            "Route D currently adds nothing beyond Route B — the "
            "gravitational contribution cannot be computed",
        ],
    )


def build_route_e() -> SpectralOriginRoute:
    """Route E — No derivational origin yet."""
    return SpectralOriginRoute(
        name="E",
        label="No Derivational Origin (Q2 Match Only)",
        core_idea=(
            "The current interior sector does not derive the spectral "
            "clue. Q2 remains only a formal structural match."
        ),
        grut_structure="None beyond what Q2 already identified",
        structure_explicit_in_canon=True,
        structure_source="quantum_program_q2.py",
        why_single_pole=(
            "Q2 identified the match; Q3 does not add a derivational origin."
        ),
        transfer_function=None,
        circularity=None,
        grounding_level="structural_match_only",
        derivationally_visible=False,
        structurally_suggestive=True,
        new_assumptions=[],
        assumption_severity="mild",
        preserves_constitutive_law=True,
        compatible_with_strong_field=True,
        compatible_with_phenomenology=True,
        structural_blockers=[
            "Does not advance beyond Q2",
        ],
        status="structurally_suggestive_only",
        nonclaims=[
            "Route E is the conservative fallback: Q2 stands as a "
            "structural match, and Q3 does not add derivational content",
        ],
    )


# ================================================================
# Interior Linearization Analysis
# ================================================================

def build_linearization_result() -> InteriorLinearizationResult:
    """Inspect the linearised interior for single-pole dominance."""
    return InteriorLinearizationResult(
        characteristic_degree=3,
        n_relaxation_modes=1,
        n_oscillatory_modes=2,
        single_pole_dominant=False,
        single_pole_reason=(
            "The memory relaxation pole is NOT dominant in the sense of "
            "being the only pole. The full spectrum has three poles: "
            "one relaxation (memory) and two oscillatory (BDCC). The "
            "memory susceptibility contribution to the dispersion "
            "relation is single-pole, but the full response is three-pole."
        ),
        spectrum_broad=False,
        spectrum_oscillatory=True,
        spectrum_overdamped=False,
        spectrum_underdetermined=False,
        drude_compatible=True,
        drude_compatibility_reason=(
            "The Q2 Drude clue identifies the MEMORY SECTOR's "
            "contribution, not the full interior response. The memory "
            "susceptibility 1/(1+iωτ) is genuinely single-pole. The "
            "full three-pole spectrum is consistent with a Drude-bath "
            "interpretation where the 'bath' is the oscillatory sector "
            "and the 'system' is the memory relaxation mode."
        ),
        evidence_for_single_pole=(
            "The memory sector's contribution to the dispersion relation "
            "is explicitly single-pole Lorentzian: 2αω_g²/(1+iωτ). "
            "The memory-mediated damping γ_mem = αω²τ/(2(1+(ωτ)²)) is "
            "the imaginary part of this Lorentzian. Both are derived from "
            "the linearised equations, not assumed."
        ),
        evidence_against_single_pole=(
            "The full interior response is three-pole, not single-pole. "
            "Additional modes from tensor memory, non-radial coupling, "
            "or nonlinear effects could modify the effective spectral "
            "density. The linearisation is zeroth-order and approximate."
        ),
    )


# ================================================================
# Hard Blockers After Q3
# ================================================================

def build_hard_blockers_after_q3() -> List[Dict[str, Any]]:
    """Hard blockers that remain even if Q3 succeeds."""
    return [
        {
            "name": "circularity_not_broken",
            "type": "structural",
            "survives_q3": True,
            "description": (
                "The single-pole Lorentzian is algebraically guaranteed by "
                "the first-order memory law. Q3 grounds this in the interior "
                "PDE but does not explain why the memory law is first-order."
            ),
        },
        {
            "name": "no_born_rule",
            "type": "structural",
            "survives_q3": True,
            "description": "No probability measure over outcomes.",
        },
        {
            "name": "no_measurement_coupling",
            "type": "structural",
            "survives_q3": True,
            "description": "No detector-system interaction model.",
        },
        {
            "name": "no_interference_formalism",
            "type": "structural",
            "survives_q3": True,
            "description": "No amplitude superposition or interference law.",
        },
        {
            "name": "no_particle_ontology",
            "type": "structural",
            "survives_q3": True,
            "description": "No Fock space, no asymptotic states.",
        },
        {
            "name": "no_experiment_framework",
            "type": "structural",
            "survives_q3": True,
            "description": "No contact with laboratory quantum experiments.",
        },
        {
            "name": "spectral_density_not_first_principles",
            "type": "currently_missing_potentially_extendable",
            "survives_q3": True,
            "description": (
                "The Drude spectral density is algebraically grounded in "
                "the interior PDE but not derived from a deeper substrate. "
                "Partially sharpened from Q2's 'not derived.'"
            ),
        },
        {
            "name": "covariant_interior_metric_missing",
            "type": "structural",
            "survives_q3": True,
            "description": (
                "Phase V lapse obstruction blocks computation of the "
                "full gravitational mode spectrum."
            ),
        },
        {
            "name": "noise_spectrum_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q3": True,
            "description": "No noise spectrum computed or testable.",
        },
        {
            "name": "loop_corrections_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q3": True,
            "description": "Quantum corrections not computed.",
        },
    ]


# ================================================================
# Master Builder
# ================================================================

def run_q3_assessment() -> Q3Result:
    """Execute Phase Q3 Interior Mode / Spectral Origin Test."""

    routes = [
        build_route_a(),
        build_route_b(),
        build_route_c(),
        build_route_d(),
        build_route_e(),
    ]

    linearization = build_linearization_result()
    hard_blockers = build_hard_blockers_after_q3()

    best = "B"
    best_status = "best_q3_candidate"
    best_grounding = "algebraic_grounding"

    safe_claims = [
        "The published interior PDE dispersion relation explicitly contains "
        "the single-pole Lorentzian 1/(1+iωτ) as the memory sector's "
        "susceptibility contribution.",

        "The memory-mediated damping rate γ_mem = αω²τ/(2(1+(ωτ)²)) is "
        "the imaginary part of this Lorentzian susceptibility, derived "
        "from the linearised [R, V, M_drive] system.",

        "The Q2 Drude/Lorentzian clue is algebraically grounded in the "
        "published interior sector: the Lorentzian is explicitly present "
        "in the dispersion relation, not merely matched externally.",

        "The full characteristic equation is cubic (three poles): "
        "one memory relaxation pole plus two oscillatory BDCC modes.",

        "The non-circular elements include: the coupling constant 2αω_g², "
        "the three-pole structure, the structural identity ω₀τ=1, and "
        "the derived damping rate formula.",

        "The algebraic grounding is PARTIALLY circular: the single-pole "
        "form follows from the first-order memory law, which is the axiom "
        "at the base of the tower.",

        "All Appendix C, Q1, and Q2 blockers remain in force.",
    ]

    unsafe_claims = [
        "The Lorentzian is derived from first principles.",
        "The circularity is broken.",
        "The first-order memory law is explained by the interior dynamics.",
        "The bath DOF are identified with specific physical modes.",
        "Q3 constitutes a derivation of the Drude spectral density.",
        "The three-pole spectrum is the complete interior mode content.",
        "Any Appendix C blocker is resolved.",
        "The noise spectrum is computable from Q3 results.",
        "The algebraic grounding constitutes physical validation.",
    ]

    result = Q3Result(
        executive_determination="strongest_spectral_origin_identified",
        routes=routes,
        best_route=best,
        best_route_status=best_status,
        best_route_grounding=best_grounding,
        linearization=linearization,
        hard_blockers_after_q3=hard_blockers,
        circularity_acknowledged=True,
        circularity_description=(
            "The single-pole Lorentzian in the interior PDE is an algebraic "
            "consequence of the first-order memory law. The chain "
            "'first-order ODE → single exponential → Lorentzian susceptibility' "
            "is identity, not derivation. Q3 establishes that this identity "
            "is EMBEDDED in the published interior sector with non-trivial "
            "coupling and mode structure, but does NOT break the circularity."
        ),
        safe_claims=safe_claims,
        unsafe_claims=unsafe_claims,
        q3_classification="algebraic_grounding",
        nonclaims=[
            "Q3 does NOT derive the first-order memory law from a deeper "
            "principle.",
            "'Algebraic grounding' means the Lorentzian is present in the "
            "published PDE, not that the PDE explains the first-order axiom.",
            "The circularity is acknowledged and cannot be broken at Q3 level.",
            "The three-pole structure may be incomplete (tensor memory, "
            "non-radial modes, nonlinear coupling could add poles).",
            "No quantum corrections, noise spectra, or measurement theory.",
            "Route B is 'best Q3 candidate' = most internally grounded, "
            "not 'correct' or 'proven.'",
        ],
        valid=True,
    )

    _validate_q3(result)
    return result


def _validate_q3(result: Q3Result) -> None:
    """Validate that Q3 result does not overclaim."""
    allowed_executives = {
        "strongest_spectral_origin_identified",
        "several_routes_viable_underdetermined",
        "structural_suggestiveness_only",
        "no_defensible_interior_origin",
    }
    if result.executive_determination not in allowed_executives:
        raise ValueError(
            f"Executive '{result.executive_determination}' not in "
            f"{allowed_executives}"
        )

    allowed_classifications = {
        "spectral_origin_program",
        "algebraic_grounding",
        "reduction_clarification",
        "speculative_horizon",
        "failure",
    }
    if result.q3_classification not in allowed_classifications:
        raise ValueError(
            f"Classification '{result.q3_classification}' not in "
            f"{allowed_classifications}"
        )

    if not result.circularity_acknowledged:
        raise ValueError(
            "Q3 MUST acknowledge the circularity. The single-pole form "
            "is algebraically guaranteed by the first-order axiom."
        )

    for r in result.routes:
        if r.status == "best_q3_candidate":
            if not r.passes_q3_criteria():
                raise ValueError(
                    f"Route '{r.name}' is best_q3_candidate but does "
                    f"not pass minimum Q3 criteria."
                )
            if r.grounding_level == "no_grounding":
                raise ValueError(
                    f"Route '{r.name}' is best_q3_candidate but has "
                    f"no_grounding — contradiction."
                )
