"""
GRUT Appendix A — Cosmological Singularity and Bounce Extension
================================================================

LOCKED INHERITANCE
------------------
- D8: coupled action S_total = S_grav + S_macro + S_defect + S_trigger + S_portal (LOCKED)
- D11: exact two-field BVP converges; companion architecture survives (STRONGLY SUPPORTED)
- D12: Q = n*eta principled and strongly constrained (PRINCIPLED)
- D13: O(3) sector partially_motivated_not_derived (PARTIALLY MOTIVATED)
- D14: tensor memory completion fails to upgrade D13 (NEGATIVE CLOSURE)
- Bridge: strong_but_missing_one_major_bridge
- Phase IV: scalar Phi is symmetry-reduced limit of rank-2 Phi_ab (ESTABLISHED)
- Phase IV: constitutive first-order relaxation memory (LOCKED)

SCOPE
-----
Test whether GRUT's strong-field closure logic — memory response, support
deficit resolution, curvature-triggered activation — can be extended to
the cosmological (FRW) regime to produce singularity avoidance or bounce,
without assuming the result.

CORE QUESTION
-------------
Can the GRUT response/support architecture produce a cosmological bounce
or singularity avoidance mechanism in the limit of extreme early-universe
curvature, without simply assuming a bounce by analogy?

RESULT
------
See compute_cosmological_bounce_result() for the final determination.

CLASSIFICATION OPTIONS
----------------------
- cosmological_bounce_derived_within_current_grut
- cosmological_bounce_strongly_suggested_by_extension
- singularity_softened_but_not_bounced
- structurally_analogous_but_not_derived
- extension_attempt_failed
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Tuple


# ---------------------------------------------------------------------------
# Classification vocabularies
# ---------------------------------------------------------------------------

APPENDIX_A_CLASSIFICATION_OPTIONS = [
    "cosmological_bounce_derived_within_current_grut",
    "cosmological_bounce_strongly_suggested_by_extension",
    "singularity_softened_but_not_bounced",
    "structurally_analogous_but_not_derived",
    "extension_attempt_failed",
]

TRANSLATION_QUALITY_LEVELS = [
    "exact",
    "heuristic",
    "structurally_analogous_only",
    "fails",
]

SCENARIO_TYPES = [
    "classical_baseline",
    "grut_memory_only",
    "grut_memory_plus_trigger",
]

BOUNCE_STATUSES = [
    "full_bounce",
    "singularity_softened",
    "singularity_persists",
    "indeterminate",
]

ASSUMPTION_ORIGINS = [
    "current_canon",
    "extension_assumption",
    "speculative_analogy",
]


# ---------------------------------------------------------------------------
# Physical / canonical constants (geometric units G = c = 1)
# ---------------------------------------------------------------------------

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
TAU_CANONICAL = math.sqrt(1.5)
LAMBDA_DEFAULT = 8.0 * math.pi
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
COMP_B_COEFF = 1.0 / (8.0 * math.pi)


# ===================================================================
# Part A — Translation Problem
# ===================================================================

@dataclass
class TranslationEntry:
    """One row of the strong-field → cosmology translation table."""
    strong_field_concept: str
    cosmological_parallel: str
    translation_quality: str
    reasoning: str
    assumption_origin: str

    def __post_init__(self) -> None:
        if self.translation_quality not in TRANSLATION_QUALITY_LEVELS:
            raise ValueError(
                f"Invalid translation quality '{self.translation_quality}'. "
                f"Must be one of {TRANSLATION_QUALITY_LEVELS}"
            )
        if self.assumption_origin not in ASSUMPTION_ORIGINS:
            raise ValueError(
                f"Invalid assumption origin '{self.assumption_origin}'. "
                f"Must be one of {ASSUMPTION_ORIGINS}"
            )


@dataclass
class TranslationMap:
    """Complete strong-field → cosmology translation map."""
    entries: List[TranslationEntry]
    overall_quality: str
    summary: str

    def __post_init__(self) -> None:
        if self.overall_quality not in TRANSLATION_QUALITY_LEVELS:
            raise ValueError(
                f"Invalid overall quality '{self.overall_quality}'. "
                f"Must be one of {TRANSLATION_QUALITY_LEVELS}"
            )


def build_translation_map() -> TranslationMap:
    """Construct the strong-field → cosmology translation map.

    This is the central conceptual step: identify what each element of
    the compact-object strong-field program becomes (or fails to become)
    in the cosmological setting.
    """
    entries = [
        # 1. Support deficit → Friedmann tension
        TranslationEntry(
            strong_field_concept="support_deficit_in_interior",
            cosmological_parallel="Friedmann_singularity_as_curvature_divergence",
            translation_quality="structurally_analogous_only",
            reasoning=(
                "In the strong-field interior, the support deficit is the failure "
                "of gravity alone to prevent singular collapse.  In cosmology, the "
                "analogous problem is the Big Bang singularity where a(t)->0, "
                "H(t)->infinity, and curvature scalars diverge.  Both involve "
                "curvature divergence in the absence of new physics, but the "
                "geometric settings differ fundamentally: spherical static vs. "
                "homogeneous expanding."
            ),
            assumption_origin="extension_assumption",
        ),

        # 2. Trigger regime → early-universe curvature regime
        TranslationEntry(
            strong_field_concept="curvature_trigger_regime_Kretschner",
            cosmological_parallel="early_universe_high_curvature_regime",
            translation_quality="heuristic",
            reasoning=(
                "The GRUT curvature trigger activates the defect/support sector "
                "when the Kretschner scalar K exceeds a threshold.  In FRW "
                "cosmology, K = 12*H^4 + ... diverges as a(t)->0.  A threshold-"
                "based activation therefore fires in the early universe.  However, "
                "the Kretschner trigger was calibrated for the compact-object "
                "regime (static, spherically symmetric); applying the same "
                "threshold function to cosmology is a heuristic extension, not "
                "a derivation."
            ),
            assumption_origin="extension_assumption",
        ),

        # 3. Component A (memory scalar) → cosmological memory scalar
        TranslationEntry(
            strong_field_concept="component_A_memory_scalar_Phi",
            cosmological_parallel="homogeneous_memory_scalar_Phi_of_t",
            translation_quality="heuristic",
            reasoning=(
                "The memory scalar Phi(r) in the strong-field program satisfies "
                "a first-order relaxation equation sourced by curvature.  In FRW, "
                "the spatial dependence drops out by homogeneity, leaving "
                "Phi(t) with relaxation: tau * dPhi/dt + Phi = S(H,a).  This is "
                "structurally clean but involves extending the source function "
                "S from the spherically-symmetric context to the cosmological "
                "one, which is an assumption."
            ),
            assumption_origin="extension_assumption",
        ),

        # 4. Component B (defect triplet) → cosmological analogue
        TranslationEntry(
            strong_field_concept="component_B_defect_triplet_O3",
            cosmological_parallel="no_direct_cosmological_analogue",
            translation_quality="fails",
            reasoning=(
                "Component B is the O(3) hedgehog defect Phi_a = eta*f(r)*x_hat_a "
                "with angular gradient energy ~ eta^2*f^2/r^2.  This requires "
                "a spatial center (the compact object), a radial coordinate, "
                "and breaking of spherical symmetry through internal O(3) DOF "
                "winding around S^2.  In FRW cosmology there is no spatial "
                "center, no preferred radial direction, and the homogeneous "
                "background cannot support a topological hedgehog.  The Component "
                "B sector does not translate to cosmology.  Any cosmological "
                "bounce must rely on Component A (memory) alone."
            ),
            assumption_origin="current_canon",
        ),

        # 5. Two-component support → single-component support
        TranslationEntry(
            strong_field_concept="two_component_support_A_plus_B",
            cosmological_parallel="single_component_memory_only",
            translation_quality="structurally_analogous_only",
            reasoning=(
                "The strong-field closure requires BOTH Component A and Component "
                "B to achieve nonsingular interiors.  Since Component B has no "
                "cosmological analogue, cosmological extension can only deploy "
                "Component A (memory scalar).  This is a fundamental reduction "
                "in support architecture: a theory that requires two components "
                "is being tested with only one.  Whether one component suffices "
                "is an open question."
            ),
            assumption_origin="extension_assumption",
        ),

        # 6. Constitutive relaxation → cosmological relaxation
        TranslationEntry(
            strong_field_concept="constitutive_first_order_relaxation",
            cosmological_parallel="cosmological_relaxation_tau_dPhi_dt_plus_Phi_eq_S",
            translation_quality="heuristic",
            reasoning=(
                "The GRUT memory is constitutive: tau * dPhi/dr + Phi = S(r) "
                "in the static case.  The cosmological translation "
                "tau * dPhi/dt + Phi = S(t) preserves the first-order structure "
                "and the relaxation timescale tau.  This is the most direct "
                "translation in the entire map, but the source function S(t) "
                "must be specified independently for the cosmological context."
            ),
            assumption_origin="extension_assumption",
        ),
    ]

    # Determine overall quality: weakest link
    quality_order = {
        "exact": 3,
        "heuristic": 2,
        "structurally_analogous_only": 1,
        "fails": 0,
    }
    worst = min(entries, key=lambda e: quality_order.get(e.translation_quality, 0))

    # Component B fails to translate, so overall is structurally_analogous_only
    overall = "structurally_analogous_only"

    summary = (
        "The strong-field → cosmology translation is structurally incomplete. "
        "The memory scalar (Component A) and its constitutive relaxation "
        "translate heuristically to FRW cosmology.  The curvature trigger "
        "translates heuristically via Kretschner threshold.  However, the "
        "O(3) defect sector (Component B) has NO cosmological analogue: "
        "the hedgehog requires a spatial center and radial topology that "
        "FRW does not provide.  The two-component support architecture "
        "reduces to single-component (memory-only) in cosmology."
    )

    return TranslationMap(
        entries=entries,
        overall_quality=overall,
        summary=summary,
    )


# ===================================================================
# Part B — Minimal Cosmological GRUT Model
# ===================================================================

@dataclass
class CosmologicalAssumption:
    """One explicit assumption in the cosmological extension."""
    assumption: str
    origin: str  # current_canon | extension_assumption | speculative_analogy
    notes: str

    def __post_init__(self) -> None:
        if self.origin not in ASSUMPTION_ORIGINS:
            raise ValueError(
                f"Invalid origin '{self.origin}'. "
                f"Must be one of {ASSUMPTION_ORIGINS}"
            )


@dataclass
class CosmologicalModel:
    """The minimal cosmological GRUT model specification."""
    background_geometry: str
    metric_form: str
    dynamical_variables: List[str]
    curvature_scalars: List[str]
    memory_sector_description: str
    trigger_sector_description: str
    defect_sector_status: str
    assumptions: List[CosmologicalAssumption]
    inherited_from_canon: List[str]
    newly_introduced: List[str]
    friedmann_equation_standard: str
    friedmann_equation_modified: str
    memory_equation: str
    effective_pressure_contribution: str
    summary: str


def build_cosmological_model() -> CosmologicalModel:
    """Construct the minimal cosmological GRUT model.

    Background: flat FRW with scale factor a(t), Hubble H = da/dt / a.
    Memory sector: homogeneous scalar Phi(t) with first-order relaxation.
    Trigger sector: Kretschner-threshold activation (heuristic extension).
    Defect sector: absent (no cosmological analogue).

    The modified Friedmann equation includes an effective energy density
    contribution from the memory scalar:

        H^2 = (8*pi/3) * (rho_matter + rho_memory)

    where rho_memory = (1/2) * (dPhi/dt)^2 + V_eff(Phi)
    arises from the memory-sector stress-energy.

    The key question is whether rho_memory + p_memory can violate the
    strong energy condition (SEC): rho + 3p > 0.  SEC violation is
    necessary for a cosmological bounce (H = 0, dH/dt > 0).
    """
    assumptions = [
        CosmologicalAssumption(
            assumption="Flat FRW background: ds^2 = -dt^2 + a(t)^2 dx^2",
            origin="current_canon",
            notes="Standard cosmological background; required by homogeneity/isotropy",
        ),
        CosmologicalAssumption(
            assumption="Memory scalar Phi becomes homogeneous: Phi = Phi(t)",
            origin="extension_assumption",
            notes="Spatial gradients dropped by cosmological symmetry",
        ),
        CosmologicalAssumption(
            assumption=(
                "Memory relaxation equation: tau * dPhi/dt + Phi = S(H, K) "
                "where S is the cosmological source function"
            ),
            origin="extension_assumption",
            notes=(
                "The source function S(H,K) is the cosmological analogue of the "
                "strong-field source.  Its functional form is NOT derived from "
                "current canon but assumed to be monotonic in curvature."
            ),
        ),
        CosmologicalAssumption(
            assumption=(
                "Memory stress-energy: rho_mem = (1/2)(dPhi/dt)^2 + V_eff(Phi), "
                "p_mem = (1/2)(dPhi/dt)^2 - V_eff(Phi)"
            ),
            origin="extension_assumption",
            notes=(
                "Standard scalar-field stress-energy form.  The GRUT memory is "
                "constitutive (relaxation), not variational.  Treating it as a "
                "stress-energy source is a heuristic extension: the memory does "
                "not have a standard Lagrangian from which T_ab derives."
            ),
        ),
        CosmologicalAssumption(
            assumption=(
                "Effective potential V_eff(Phi) is assumed to be bounded and "
                "non-negative, of order V ~ Phi^2 / (2*tau^2)"
            ),
            origin="extension_assumption",
            notes=(
                "The GRUT memory has no variational potential.  V_eff is an "
                "effective description of the relaxation-restoring dynamics."
            ),
        ),
        CosmologicalAssumption(
            assumption=(
                "Curvature trigger activation occurs when K > K_threshold, "
                "where K_threshold is calibrated from the compact-object regime"
            ),
            origin="extension_assumption",
            notes=(
                "The trigger threshold was derived for static spherical geometry.  "
                "Applying it to FRW is a heuristic step."
            ),
        ),
        CosmologicalAssumption(
            assumption=(
                "O(3) defect sector is absent in cosmology: no hedgehog, "
                "no Component B support"
            ),
            origin="current_canon",
            notes=(
                "The hedgehog requires a spatial center and S^2 winding topology.  "
                "FRW has neither.  This is not an assumption but a structural fact."
            ),
        ),
        CosmologicalAssumption(
            assumption=(
                "No new fields, potentials, or couplings are introduced beyond "
                "the memory scalar and its effective stress-energy"
            ),
            origin="current_canon",
            notes="Minimal extension principle: add nothing beyond what canon provides",
        ),
    ]

    return CosmologicalModel(
        background_geometry="Flat FRW: ds^2 = -dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)",
        metric_form="g_ab = diag(-1, a^2, a^2, a^2)",
        dynamical_variables=["a(t)", "H(t) = da/dt / a", "Phi(t)"],
        curvature_scalars=[
            "R = 6(dH/dt + 2H^2)",
            "K = R_abcd R^abcd = 12(dH/dt + H^2)^2 + 12 H^4",
        ],
        memory_sector_description=(
            "Homogeneous memory scalar Phi(t) satisfying first-order relaxation: "
            "tau * dPhi/dt + Phi = S(H, K).  Contributes to Friedmann equation "
            "through effective stress-energy rho_mem, p_mem."
        ),
        trigger_sector_description=(
            "Kretschner-threshold activation: memory source S(H,K) is suppressed "
            "below K_threshold and saturates above it.  This is a heuristic "
            "cosmological extension of the compact-object trigger."
        ),
        defect_sector_status=(
            "ABSENT. The O(3) hedgehog defect has no cosmological analogue.  "
            "Component B support is not available in FRW."
        ),
        assumptions=assumptions,
        inherited_from_canon=[
            "Metric gravity (Einstein equations)",
            "Memory scalar Phi as GRUT response field",
            "First-order constitutive relaxation structure",
            "Relaxation timescale tau",
            "Curvature-threshold activation concept",
        ],
        newly_introduced=[
            "Cosmological source function S(H, K) — form assumed, not derived",
            "Effective stress-energy T_ab^mem — heuristic for constitutive field",
            "Application of Kretschner threshold to FRW geometry",
        ],
        friedmann_equation_standard="H^2 = (8*pi/3) * rho_matter",
        friedmann_equation_modified=(
            "H^2 = (8*pi/3) * (rho_matter + rho_memory), "
            "where rho_memory = (1/2)(dPhi/dt)^2 + V_eff(Phi)"
        ),
        memory_equation="tau * dPhi/dt + Phi = S(H, K)",
        effective_pressure_contribution=(
            "p_mem = (1/2)(dPhi/dt)^2 - V_eff(Phi).  "
            "For SEC violation (bounce requirement): rho_mem + 3*p_mem < 0, "
            "i.e., 2*(dPhi/dt)^2 - 2*V_eff < 0, i.e., V_eff > (dPhi/dt)^2.  "
            "This requires the effective potential to dominate the kinetic energy."
        ),
        summary=(
            "The minimal cosmological GRUT model retains only the memory scalar "
            "sector with constitutive relaxation.  The defect/support sector is "
            "absent.  The model introduces 3 extension assumptions beyond current "
            "canon: the cosmological source function, the effective stress-energy "
            "treatment, and the FRW Kretschner trigger application."
        ),
    )


# ===================================================================
# Part C — Bounce / Singularity-Avoidance Analysis
# ===================================================================

@dataclass
class BounceTest:
    """One specific test of bounce / singularity avoidance."""
    test_name: str
    question: str
    result: str  # "yes", "no", "conditional", "indeterminate"
    reasoning: str
    depends_on: List[str]  # which assumptions it depends on


@dataclass
class BounceAnalysis:
    """Complete bounce / singularity-avoidance analysis."""
    tests: List[BounceTest]
    sec_violation_possible: bool
    sec_violation_conditional_on: List[str]
    a_avoids_zero: str  # "yes", "no", "conditional", "indeterminate"
    H_remains_finite: str
    curvature_remains_finite: str
    effective_repulsion: str
    sign_structure_change: str
    overall_bounce_status: str  # from BOUNCE_STATUSES
    summary: str

    def __post_init__(self) -> None:
        if self.overall_bounce_status not in BOUNCE_STATUSES:
            raise ValueError(
                f"Invalid bounce status '{self.overall_bounce_status}'. "
                f"Must be one of {BOUNCE_STATUSES}"
            )


def analyze_bounce_criteria() -> BounceAnalysis:
    """Evaluate whether GRUT's cosmological extension produces a bounce.

    The key physics:
    For a bounce in FRW, we need H = 0 and dH/dt > 0 at some time t_b.
    The Raychaudhuri equation gives:
        dH/dt = -(4*pi/3) * (rho_total + 3*p_total)
    So dH/dt > 0 requires rho + 3p < 0 (SEC violation).

    For the memory scalar:
        rho_mem + 3*p_mem = 2*(dPhi/dt)^2 - 2*V_eff(Phi)
    SEC violation requires: V_eff(Phi) > (dPhi/dt)^2.

    The fundamental question: does the GRUT memory architecture produce
    a potential-dominated phase in the early universe?
    """
    tests = [
        # Test 1: Can the memory scalar violate the SEC?
        BounceTest(
            test_name="SEC_violation_from_memory",
            question=(
                "Can the GRUT memory scalar Phi(t) violate the strong energy "
                "condition rho + 3p > 0 in the early universe?"
            ),
            result="conditional",
            reasoning=(
                "The effective memory stress-energy has rho_mem + 3*p_mem = "
                "2*(dPhi/dt)^2 - 2*V_eff.  SEC violation requires V_eff > "
                "(dPhi/dt)^2.  The GRUT memory is constitutive (first-order "
                "relaxation), NOT variational.  It does not have a native "
                "potential V_eff.  If one imposes an effective potential to "
                "model the relaxation restoring force, SEC violation is "
                "possible in principle when the potential dominates.  But this "
                "requires assuming a potential-like structure that the "
                "constitutive memory does not naturally possess.  This is "
                "the central obstruction: constitutive relaxation pushes Phi "
                "toward its attractor, producing kinetic-dominated behavior "
                "(like a damped oscillator), not potential-dominated behavior.  "
                "SEC violation is conditional on an assumed effective potential "
                "that is NOT derived from the GRUT architecture."
            ),
            depends_on=[
                "effective_potential_assumption",
                "cosmological_source_function",
            ],
        ),

        # Test 2: Does the relaxation structure favor bounce?
        BounceTest(
            test_name="relaxation_structure_bounce_tendency",
            question=(
                "Does the GRUT constitutive relaxation tau*dPhi/dt + Phi = S "
                "naturally produce conditions for a bounce?"
            ),
            result="no",
            reasoning=(
                "The relaxation equation tau*dPhi/dt + Phi = S(t) has the "
                "general solution Phi(t) = Phi_0 * exp(-t/tau) + integral of "
                "S(t') * exp(-(t-t')/tau) dt'.  This is overdamped exponential "
                "approach to the source value S.  The kinetic energy "
                "(dPhi/dt)^2 ~ (S - Phi)^2 / tau^2 is always positive and "
                "the 'restoring force' is not a potential gradient but a "
                "dissipative relaxation.  This structure CANNOT produce a "
                "slow-roll or potential-dominated phase that would drive SEC "
                "violation.  The relaxation is kinetic-dominated by construction: "
                "the field rushes toward its attractor value, dissipating energy, "
                "rather than sitting at a potential maximum."
            ),
            depends_on=[],
        ),

        # Test 3: Can curvature trigger produce effective repulsion?
        BounceTest(
            test_name="trigger_effective_repulsion",
            question=(
                "Can the Kretschner trigger mechanism produce an effective "
                "repulsive contribution in the Friedmann equation?"
            ),
            result="conditional",
            reasoning=(
                "The trigger mechanism activates the memory source when K > "
                "K_threshold.  In the early universe K diverges, so the trigger "
                "fires.  This amplifies the memory scalar Phi, increasing "
                "rho_mem.  However, adding positive energy density rho_mem "
                "to the Friedmann equation INCREASES H^2, making the expansion "
                "faster, not slower.  For repulsion (deceleration / bounce), "
                "we need NEGATIVE effective pressure, not just positive density.  "
                "The trigger amplifies the memory but does not change its "
                "equation-of-state character.  Effective repulsion requires "
                "the memory to have w_mem < -1/3, which returns to the "
                "potential-dominance problem of Test 1."
            ),
            depends_on=[
                "effective_potential_assumption",
                "kretschner_trigger_FRW_extension",
            ],
        ),

        # Test 4: Sign structure of modified Friedmann equation
        BounceTest(
            test_name="sign_structure_friedmann",
            question=(
                "Does the GRUT memory correction change the sign structure "
                "of the Friedmann/Raychaudhuri equations?"
            ),
            result="no",
            reasoning=(
                "Standard Friedmann: H^2 = (8pi/3)*rho, dH/dt = -4pi*(rho+p).  "
                "With memory: H^2 = (8pi/3)*(rho_m + rho_mem), "
                "dH/dt = -4pi*(rho_m + p_m + rho_mem + p_mem).  "
                "For the constitutive memory: rho_mem >= 0 (positive-definite "
                "kinetic energy + positive V_eff).  The pressure p_mem can be "
                "negative only if V_eff > (dPhi/dt)^2 / 2, but as argued in "
                "Test 2, the relaxation dynamics keeps dPhi/dt ~ (S-Phi)/tau "
                "and the effective 'potential' V ~ Phi^2/(2*tau^2) is of the "
                "same order.  There is no natural hierarchy that forces "
                "V_eff >> kinetic, so the sign structure is not changed "
                "by the memory sector."
            ),
            depends_on=[],
        ),

        # Test 5: Can a(t) avoid reaching zero?
        BounceTest(
            test_name="scale_factor_avoids_zero",
            question=(
                "Can the modified evolution equations prevent a(t) from "
                "reaching zero?"
            ),
            result="indeterminate",
            reasoning=(
                "Preventing a(t) -> 0 requires either a bounce (H=0 with "
                "dH/dt > 0) or an asymptotic approach (H -> -infinity slower "
                "than 1/a).  The memory correction adds positive energy density "
                "without a clear mechanism for SEC violation (Tests 1-4).  "
                "If an effective potential IS assumed with V_eff >> kinetic, "
                "then a bounce is possible in principle, but this is an assumed "
                "potential, not a derived GRUT feature.  Without it, the memory "
                "correction makes the singularity WORSE (more energy density "
                "-> faster contraction) not better.  Whether a(t) avoids zero "
                "depends entirely on the assumed V_eff form, which is not "
                "determined by GRUT."
            ),
            depends_on=[
                "effective_potential_assumption",
                "cosmological_source_function",
            ],
        ),

        # Test 6: H(t) finiteness
        BounceTest(
            test_name="hubble_finiteness",
            question="Can H(t) be kept finite by the memory correction?",
            result="conditional",
            reasoning=(
                "H^2 = (8pi/3)*(rho_m + rho_mem).  As a -> 0, "
                "rho_m ~ a^-3 (matter) or a^-4 (radiation) diverges.  "
                "rho_mem is bounded if Phi and dPhi/dt remain finite, which "
                "they do (the relaxation solution is bounded for finite tau).  "
                "So the memory adds a bounded contribution to a divergent "
                "background.  H -> infinity persists unless the memory somehow "
                "cancels the matter divergence, which would require "
                "rho_mem -> -infinity — impossible for positive-definite "
                "energy.  Only with an assumed effective potential that grows "
                "sufficiently negative (violating energy conditions) could H "
                "be bounded.  This is not a feature of the GRUT memory."
            ),
            depends_on=["effective_potential_assumption"],
        ),

        # Test 7: Comparison to compact-object closure
        BounceTest(
            test_name="compact_object_comparison",
            question=(
                "Does the cosmological extension preserve the two-component "
                "support structure that resolves the compact-object singularity?"
            ),
            result="no",
            reasoning=(
                "The compact-object singularity resolution requires BOTH "
                "Component A (memory, providing smooth envelope) and "
                "Component B (defect, providing 1/r^2 angular gradient "
                "energy).  In cosmology, Component B is absent (no hedgehog "
                "in FRW).  The cosmological extension retains only one of "
                "the two required support components.  The structural reason "
                "the compact-object interior is nonsingular — two complementary "
                "support mechanisms — does NOT carry over to cosmology."
            ),
            depends_on=[],
        ),
    ]

    # Evaluate SEC violation possibility
    sec_violation_possible = True  # possible in principle IF potential assumed
    sec_conditional_on = [
        "effective potential V_eff(Phi) assumed (not derived from constitutive relaxation)",
        "V_eff must dominate over kinetic energy (dPhi/dt)^2",
        "relaxation dynamics must be augmented to allow slow-roll behavior",
    ]

    # Overall assessment: singularity softened at best
    # The memory scalar adds a bounded energy density, which CAN slow
    # the approach to singularity but CANNOT prevent it without
    # assumptions beyond GRUT canon.
    overall_status = "singularity_softened"

    return BounceAnalysis(
        tests=tests,
        sec_violation_possible=sec_violation_possible,
        sec_violation_conditional_on=sec_conditional_on,
        a_avoids_zero="conditional",
        H_remains_finite="conditional",
        curvature_remains_finite="conditional",
        effective_repulsion="conditional",
        sign_structure_change="no",
        overall_bounce_status="singularity_softened",
        summary=(
            "The GRUT memory scalar in FRW cosmology adds a bounded positive "
            "energy density contribution to the Friedmann equation.  This "
            "contribution is sourced by curvature through the trigger mechanism "
            "and grows as the universe contracts.  However, the constitutive "
            "relaxation structure of the GRUT memory is fundamentally kinetic-"
            "dominated: it cannot naturally produce the potential-dominated "
            "phase required for SEC violation and bounce.  The memory correction "
            "SOFTENS the approach to the singularity (slowing divergence rates) "
            "but does not PREVENT it.  A full bounce would require either: "
            "(1) an assumed effective potential not present in GRUT canon, or "
            "(2) the missing Component B analogue, which does not exist in FRW.  "
            "The singularity is softened but not bounced."
        ),
    )


# ===================================================================
# Part D — Comparison Scenarios
# ===================================================================

@dataclass
class ScenarioResult:
    """Result for one comparison scenario."""
    scenario_type: str
    label: str
    description: str
    singularity_outcome: str  # from BOUNCE_STATUSES
    H_diverges: bool
    a_reaches_zero: bool
    curvature_diverges: bool
    sec_violated: bool
    depends_on_extra_assumptions: bool
    extra_assumptions: List[str]
    summary: str

    def __post_init__(self) -> None:
        if self.scenario_type not in SCENARIO_TYPES:
            raise ValueError(
                f"Invalid scenario type '{self.scenario_type}'. "
                f"Must be one of {SCENARIO_TYPES}"
            )
        if self.singularity_outcome not in BOUNCE_STATUSES:
            raise ValueError(
                f"Invalid singularity outcome '{self.singularity_outcome}'. "
                f"Must be one of {BOUNCE_STATUSES}"
            )


@dataclass
class ComparisonResult:
    """Complete three-scenario comparison."""
    scenarios: List[ScenarioResult]
    bounce_depends_on_memory_alone: bool
    bounce_depends_on_trigger_extension: bool
    bounce_depends_on_extra_assumptions: bool
    summary: str


def build_comparison_scenarios() -> ComparisonResult:
    """Construct and evaluate the three required comparison scenarios.

    1. Classical baseline: standard FRW cosmology, no GRUT corrections
    2. GRUT memory-only: memory scalar with constitutive relaxation
    3. GRUT memory + trigger: memory scalar with curvature-threshold activation
    """
    scenarios = [
        # Scenario 1: Classical baseline
        ScenarioResult(
            scenario_type="classical_baseline",
            label="Classical FRW Cosmology",
            description=(
                "Standard Friedmann cosmology with radiation + matter.  "
                "H^2 = (8pi/3)*rho, rho ~ a^-4 (radiation era).  "
                "As t -> 0, a -> 0, H -> infinity, K -> infinity.  "
                "The Big Bang singularity is a curvature singularity with "
                "geodesic incompleteness."
            ),
            singularity_outcome="singularity_persists",
            H_diverges=True,
            a_reaches_zero=True,
            curvature_diverges=True,
            sec_violated=False,
            depends_on_extra_assumptions=False,
            extra_assumptions=[],
            summary="Classical cosmology has a Big Bang singularity: a(0)=0, H->inf.",
        ),

        # Scenario 2: GRUT memory-only
        ScenarioResult(
            scenario_type="grut_memory_only",
            label="GRUT Memory-Only Cosmology",
            description=(
                "FRW cosmology with GRUT memory scalar Phi(t) satisfying "
                "tau*dPhi/dt + Phi = S_0, where S_0 is a constant source.  "
                "The memory approaches Phi -> S_0 exponentially.  Energy "
                "density rho_mem = (1/2)(dPhi/dt)^2 + V_eff ~ bounded.  "
                "This adds a bounded positive contribution to H^2 but does "
                "not modify the singular behavior of the matter/radiation "
                "sector as a -> 0."
            ),
            singularity_outcome="singularity_softened",
            H_diverges=True,
            a_reaches_zero=True,
            curvature_diverges=True,
            sec_violated=False,
            depends_on_extra_assumptions=False,
            extra_assumptions=[],
            summary=(
                "Memory-only cosmology: the scalar adds bounded energy but "
                "cannot prevent a(t)->0 or H->infinity.  Singularity softened "
                "(rate of divergence slightly modified) but not avoided."
            ),
        ),

        # Scenario 3: GRUT memory + trigger
        ScenarioResult(
            scenario_type="grut_memory_plus_trigger",
            label="GRUT Memory + Trigger Cosmology",
            description=(
                "FRW cosmology with GRUT memory scalar Phi(t) and "
                "Kretschner-threshold trigger: S(H,K) activates when "
                "K > K_threshold.  In the early universe K diverges, "
                "so the trigger fires and amplifies the memory source.  "
                "This increases rho_mem, which increases H^2, making the "
                "approach to the singularity FASTER, not slower.  The "
                "trigger mechanism, designed for the compact-object regime "
                "where it activates a support structure, does not produce "
                "the same effect in cosmology because Component B is absent."
            ),
            singularity_outcome="singularity_softened",
            H_diverges=True,
            a_reaches_zero=True,
            curvature_diverges=True,
            sec_violated=False,
            depends_on_extra_assumptions=True,
            extra_assumptions=[
                "Kretschner trigger threshold applied to FRW (heuristic extension)",
                "Source function S(H,K) assumed monotonic in K",
            ],
            summary=(
                "Memory + trigger cosmology: the trigger amplifies the memory "
                "in the early universe, but this adds more positive energy "
                "density rather than producing repulsion.  Without Component B "
                "(absent in FRW), the trigger-activated memory cannot change "
                "the singularity structure.  Softened but not bounced."
            ),
        ),
    ]

    return ComparisonResult(
        scenarios=scenarios,
        bounce_depends_on_memory_alone=False,
        bounce_depends_on_trigger_extension=False,
        bounce_depends_on_extra_assumptions=True,
        summary=(
            "All three scenarios produce a singularity or softened singularity.  "
            "No scenario achieves a full bounce within GRUT's current architecture.  "
            "The memory-only correction softens the singularity by adding a bounded "
            "energy contribution that slightly modifies the divergence rate.  The "
            "trigger extension amplifies this effect but cannot change its character "
            "because the missing Component B means no new support mechanism is "
            "activated.  A full bounce would require assumptions BEYOND current GRUT "
            "canon — specifically, an effective potential structure that the "
            "constitutive relaxation memory does not possess."
        ),
    )


# ===================================================================
# Part E — Classification
# ===================================================================

@dataclass
class RemainingGap:
    """One remaining gap or upgrade path for cosmological extension."""
    gap: str
    severity: str  # "critical", "significant", "minor"
    notes: str


@dataclass
class AppendixAResult:
    """Complete Appendix A result."""
    translation_map: TranslationMap
    cosmological_model: CosmologicalModel
    bounce_analysis: BounceAnalysis
    comparison: ComparisonResult
    classification: str
    justification: str
    remaining_gaps: List[RemainingGap]
    nonclaims: List[str]
    upgrade_paths: List[str]

    def __post_init__(self) -> None:
        if self.classification not in APPENDIX_A_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid classification '{self.classification}'. "
                f"Must be one of {APPENDIX_A_CLASSIFICATION_OPTIONS}"
            )

    def to_dict(self) -> Dict[str, Any]:
        """Export entire result as a serializable dictionary."""
        return {
            "translation_map": {
                "overall_quality": self.translation_map.overall_quality,
                "summary": self.translation_map.summary,
                "entries": [asdict(e) for e in self.translation_map.entries],
            },
            "cosmological_model": {
                "background_geometry": self.cosmological_model.background_geometry,
                "dynamical_variables": self.cosmological_model.dynamical_variables,
                "defect_sector_status": self.cosmological_model.defect_sector_status,
                "inherited_from_canon": self.cosmological_model.inherited_from_canon,
                "newly_introduced": self.cosmological_model.newly_introduced,
                "summary": self.cosmological_model.summary,
            },
            "bounce_analysis": {
                "overall_bounce_status": self.bounce_analysis.overall_bounce_status,
                "sec_violation_possible": self.bounce_analysis.sec_violation_possible,
                "sec_violation_conditional_on": self.bounce_analysis.sec_violation_conditional_on,
                "a_avoids_zero": self.bounce_analysis.a_avoids_zero,
                "H_remains_finite": self.bounce_analysis.H_remains_finite,
                "curvature_remains_finite": self.bounce_analysis.curvature_remains_finite,
                "summary": self.bounce_analysis.summary,
            },
            "comparison": {
                "bounce_depends_on_memory_alone": self.comparison.bounce_depends_on_memory_alone,
                "bounce_depends_on_trigger_extension": self.comparison.bounce_depends_on_trigger_extension,
                "bounce_depends_on_extra_assumptions": self.comparison.bounce_depends_on_extra_assumptions,
                "scenarios": [asdict(s) for s in self.comparison.scenarios],
                "summary": self.comparison.summary,
            },
            "classification": self.classification,
            "justification": self.justification,
            "remaining_gaps": [asdict(g) for g in self.remaining_gaps],
            "nonclaims": self.nonclaims,
            "upgrade_paths": self.upgrade_paths,
        }

    def to_json(self, indent: int = 2) -> str:
        """Serialize result to JSON."""
        return json.dumps(self.to_dict(), indent=indent)


def classify_cosmological_bounce(
    translation: TranslationMap,
    bounce: BounceAnalysis,
    comparison: ComparisonResult,
) -> Tuple[str, str]:
    """Determine the final Appendix A classification.

    Classification logic (explicit, no hidden scoring):

    1. If bounce is achieved within current canon → cosmological_bounce_derived
    2. If bounce is achieved with defensible extensions → strongly_suggested
    3. If singularity is softened but not bounced → singularity_softened
    4. If only structural analogy, no softening → structurally_analogous
    5. If the extension attempt fails entirely → extension_attempt_failed

    The classification is determined by:
    - translation quality (how well does the strong-field logic carry over?)
    - bounce analysis (does the modified Friedmann eq. produce a bounce?)
    - comparison (does any scenario achieve bounce without extra assumptions?)
    """
    # Check: did ANY scenario achieve a full bounce?
    any_bounce = any(
        s.singularity_outcome == "full_bounce"
        for s in comparison.scenarios
    )

    # Check: did any scenario achieve bounce without extra assumptions?
    bounce_without_extra = any(
        s.singularity_outcome == "full_bounce" and not s.depends_on_extra_assumptions
        for s in comparison.scenarios
    )

    # Check: is the overall bounce status "singularity_softened"?
    softened = bounce.overall_bounce_status == "singularity_softened"

    # Check: does translation at least reach heuristic quality?
    translation_has_content = translation.overall_quality in ("exact", "heuristic")

    # Decision tree
    if bounce_without_extra:
        classification = "cosmological_bounce_derived_within_current_grut"
        justification = (
            "A full cosmological bounce is achieved within current GRUT "
            "architecture without additional assumptions."
        )
    elif any_bounce:
        classification = "cosmological_bounce_strongly_suggested_by_extension"
        justification = (
            "A cosmological bounce is achieved but requires assumptions "
            "beyond current GRUT canon."
        )
    elif softened:
        classification = "singularity_softened_but_not_bounced"
        justification = (
            "The GRUT memory correction softens the cosmological singularity "
            "by adding a bounded energy contribution that modifies the "
            "divergence rate, but does not achieve a full bounce.  The "
            "constitutive relaxation structure cannot produce the potential-"
            "dominated phase needed for SEC violation.  The missing "
            "Component B (no cosmological hedgehog analogue) means the "
            "two-component support architecture is incomplete."
        )
    elif translation_has_content:
        classification = "structurally_analogous_but_not_derived"
        justification = (
            "The strong-field → cosmology translation has some heuristic "
            "content but the bounce is not achieved and the singularity is "
            "not materially softened."
        )
    else:
        classification = "extension_attempt_failed"
        justification = (
            "The cosmological extension does not produce meaningful "
            "singularity modification."
        )

    return classification, justification


def compute_cosmological_bounce_result() -> AppendixAResult:
    """Main entry point: compute the full Appendix A result.

    Returns a complete, inspectable, serializable result.
    """
    # Part A: Translation
    translation = build_translation_map()

    # Part B: Model
    model = build_cosmological_model()

    # Part C: Bounce analysis
    bounce = analyze_bounce_criteria()

    # Part D: Comparison
    comparison = build_comparison_scenarios()

    # Part E: Classification
    classification, justification = classify_cosmological_bounce(
        translation, bounce, comparison,
    )

    # Remaining gaps
    remaining_gaps = [
        RemainingGap(
            gap="Constitutive relaxation cannot produce SEC violation",
            severity="critical",
            notes=(
                "The first-order relaxation structure is kinetic-dominated.  "
                "SEC violation requires potential-dominated behavior.  This is "
                "a fundamental structural mismatch, not a tuning problem."
            ),
        ),
        RemainingGap(
            gap="Component B has no cosmological analogue",
            severity="critical",
            notes=(
                "The hedgehog defect requires a spatial center and S^2 topology.  "
                "FRW has neither.  The two-component support architecture that "
                "resolves the compact-object singularity cannot be replicated "
                "in cosmology."
            ),
        ),
        RemainingGap(
            gap="Cosmological source function S(H,K) is assumed, not derived",
            severity="significant",
            notes=(
                "The strong-field source function was calibrated for static "
                "spherical geometry.  Its cosmological form is a free choice."
            ),
        ),
        RemainingGap(
            gap="Effective stress-energy for constitutive memory is heuristic",
            severity="significant",
            notes=(
                "A constitutive (non-variational) field does not have a "
                "standard T_ab derivation.  The scalar-field stress-energy form "
                "is assumed, not derived from the constitutive structure."
            ),
        ),
    ]

    # Nonclaims
    nonclaims = [
        "This appendix does NOT claim that GRUT resolves the cosmological singularity.",
        "This appendix does NOT claim that a cosmological bounce is derived.",
        "This appendix does NOT claim that the strong-field closure logic translates "
        "exactly to cosmology.",
        "This appendix does NOT claim that the memory scalar alone can provide "
        "the same support architecture as the two-component (A+B) strong-field system.",
        "This appendix does NOT claim that the O(3) defect sector has any cosmological "
        "analogue.",
        "This appendix does NOT claim that constitutive relaxation can naturally "
        "produce SEC violation.",
        "This appendix does NOT claim that singularity softening is observationally "
        "significant.",
        "The effective stress-energy treatment of the constitutive memory is "
        "a heuristic, not a derivation.",
    ]

    # Upgrade paths
    upgrade_paths = [
        "1. Derive an effective potential V_eff(Phi) from the constitutive structure "
        "(not yet possible; would require extending GRUT's memory formulation).",
        "2. Identify a cosmological analogue of Component B — perhaps an anisotropic "
        "stress sector from the tensor memory decomposition (requires new physics).",
        "3. Test whether the tensor memory extension (Phi_ab rather than Phi) provides "
        "additional DOF that can serve a support role in cosmology.",
        "4. Compute the actual magnitude of the singularity softening to determine "
        "whether it is observationally relevant even without a full bounce.",
        "5. Compare to established bouncing cosmology models (LQC, ekpyrotic, etc.) "
        "to identify what structural features GRUT would need to import.",
    ]

    return AppendixAResult(
        translation_map=translation,
        cosmological_model=model,
        bounce_analysis=bounce,
        comparison=comparison,
        classification=classification,
        justification=justification,
        remaining_gaps=remaining_gaps,
        nonclaims=nonclaims,
        upgrade_paths=upgrade_paths,
    )
