"""
GRUT Appendix B — Dark Matter and Dark Energy in the GRUT Vacuum
=================================================================

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
- Appendix A: singularity_softened_but_not_bounced (ESTABLISHED)

PUBLIC BOUNDARY
---------------
This module uses only published D10-D14 + Omni-ToE v3 content.
No D15 or later results are referenced.

SCOPE
-----
Test whether the published GRUT architecture can support dark-matter and
dark-energy interpretations, separately and honestly, without adding
arbitrary new matter by hand.

CORE QUESTION
-------------
Can the GRUT memory field and responsive vacuum architecture produce
mathematically defensible dark-sector interpretations for:
  1. dark-matter-like gravitational behavior (Bullet Cluster, halos)
  2. dark-energy-like large-scale vacuum tension
and if so, at what epistemic level?

RESULT
------
See compute_dark_sector_result() for the final determination.

CLASSIFICATION OPTIONS
----------------------
Dark Matter track:
  - dark_matter_interpretation_derived_within_published_grut
  - dark_matter_interpretation_strongly_suggested_by_extension
  - dark_matter_interpretation_effective_only
  - dark_matter_interpretation_partial_mimic
  - dark_matter_interpretation_failed

Dark Energy track:
  - dark_energy_interpretation_derived_within_published_grut
  - dark_energy_interpretation_strongly_suggested_by_extension
  - dark_energy_interpretation_effective_only
  - dark_energy_interpretation_reframes_but_does_not_solve
  - dark_energy_interpretation_failed

Overall Appendix B:
  - dual_dark_sector_extension_strong
  - dark_matter_stronger_than_dark_energy
  - dark_energy_stronger_than_dark_matter
  - mixed_and_partial
  - appendix_b_failed
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


# ---------------------------------------------------------------------------
# Classification vocabularies
# ---------------------------------------------------------------------------

DM_CLASSIFICATION_OPTIONS = [
    "dark_matter_interpretation_derived_within_published_grut",
    "dark_matter_interpretation_strongly_suggested_by_extension",
    "dark_matter_interpretation_effective_only",
    "dark_matter_interpretation_partial_mimic",
    "dark_matter_interpretation_failed",
]

DE_CLASSIFICATION_OPTIONS = [
    "dark_energy_interpretation_derived_within_published_grut",
    "dark_energy_interpretation_strongly_suggested_by_extension",
    "dark_energy_interpretation_effective_only",
    "dark_energy_interpretation_reframes_but_does_not_solve",
    "dark_energy_interpretation_failed",
]

APPENDIX_B_CLASSIFICATION_OPTIONS = [
    "dual_dark_sector_extension_strong",
    "dark_matter_stronger_than_dark_energy",
    "dark_energy_stronger_than_dark_matter",
    "mixed_and_partial",
    "appendix_b_failed",
]

INTERPRETATION_LEVELS = [
    "derived",
    "strongly_suggested",
    "effective_only",
    "partial_mimic",
    "reframes_only",
    "failed",
]

SCENARIO_TYPES = [
    "classical_baseline",
    "grut_memory_only",
    "grut_memory_plus_extension",
]

ASSUMPTION_STATUSES = [
    "inherited_from_canon",
    "extension_assumption",
    "phenomenological",
    "speculative",
]

PARAMETER_AUTHORITY_LEVELS = [
    "inherited",
    "derived",
    "matched",
    "phenomenological",
    "open",
]

SECTOR_RELEVANCE_LEVELS = [
    "directly_relevant",
    "conditionally_relevant",
    "dormant",
    "absent",
    "not_applicable",
]


# ---------------------------------------------------------------------------
# Physical / canonical constants (geometric units G = c = 1)
# ---------------------------------------------------------------------------

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
TAU_CANONICAL = math.sqrt(1.5)
LAMBDA_DEFAULT = 8.0 * math.pi
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
COMP_B_COEFF = 1.0 / (8.0 * math.pi)


# ===================================================================
# Dataclasses
# ===================================================================

@dataclass
class SectorRelevance:
    """Relevance of one GRUT sector to a dark-sector problem."""
    sector: str
    relevance: str
    reasoning: str

    def __post_init__(self) -> None:
        if self.relevance not in SECTOR_RELEVANCE_LEVELS:
            raise ValueError(
                f"Invalid relevance '{self.relevance}'. "
                f"Must be one of {SECTOR_RELEVANCE_LEVELS}"
            )


@dataclass
class DarkSectorProblem:
    """Definition of one dark-sector problem (DM or DE)."""
    name: str
    description: str
    relevant_grut_sectors: List[SectorRelevance]
    requires_extension: bool
    shared_field_content: bool
    key_observational_signatures: List[str]


@dataclass
class DarkMatterTest:
    """One test of dark matter interpretation viability."""
    test_name: str
    question: str
    result: str
    viable: bool
    interpretation_level: str
    comment: str

    def __post_init__(self) -> None:
        if self.interpretation_level not in INTERPRETATION_LEVELS:
            raise ValueError(
                f"Invalid interpretation level '{self.interpretation_level}'. "
                f"Must be one of {INTERPRETATION_LEVELS}"
            )


@dataclass
class DarkMatterResult:
    """Complete dark matter analysis."""
    tests: List[DarkMatterTest]
    memory_gravitates_independently: bool
    memory_collisionless: bool
    memory_survives_cluster_collision: bool
    defect_sector_relevant: bool
    scaling_matches_cdm: bool
    has_stable_weak_field_phenomenology: bool
    classification: str
    justification: str
    summary: str

    def __post_init__(self) -> None:
        if self.classification not in DM_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid DM classification '{self.classification}'. "
                f"Must be one of {DM_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class DarkEnergyTest:
    """One test of dark energy interpretation viability."""
    test_name: str
    question: str
    result: str
    viable: bool
    interpretation_level: str
    comment: str

    def __post_init__(self) -> None:
        if self.interpretation_level not in INTERPRETATION_LEVELS:
            raise ValueError(
                f"Invalid interpretation level '{self.interpretation_level}'. "
                f"Must be one of {INTERPRETATION_LEVELS}"
            )


@dataclass
class DarkEnergyResult:
    """Complete dark energy analysis."""
    tests: List[DarkEnergyTest]
    produces_negative_pressure: bool
    equation_of_state_w_minus_1: bool
    vacuum_tension_derived: bool
    cosmological_constant_explained: bool
    requires_cosmological_extension: bool
    classification: str
    justification: str
    summary: str

    def __post_init__(self) -> None:
        if self.classification not in DE_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid DE classification '{self.classification}'. "
                f"Must be one of {DE_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class ParameterEntry:
    """One parameter in the dark-sector model."""
    name: str
    value_or_form: str
    authority: str
    source: str

    def __post_init__(self) -> None:
        if self.authority not in PARAMETER_AUTHORITY_LEVELS:
            raise ValueError(
                f"Invalid authority '{self.authority}'. "
                f"Must be one of {PARAMETER_AUTHORITY_LEVELS}"
            )


@dataclass
class MinimalModel:
    """Minimal mathematical model for one dark-sector interpretation."""
    track: str
    field_content: str
    regime: str
    effective_equations: List[str]
    parameters: List[ParameterEntry]
    interpretation_type: str
    summary: str


@dataclass
class ScenarioComparison:
    """Comparison row for one scenario."""
    scenario: str
    outcome: str
    assumptions_needed: List[str]
    comment: str

    def __post_init__(self) -> None:
        if self.scenario not in SCENARIO_TYPES:
            raise ValueError(
                f"Invalid scenario '{self.scenario}'. "
                f"Must be one of {SCENARIO_TYPES}"
            )


@dataclass
class ComparisonResult:
    """Full comparison across scenarios for one track."""
    track: str
    scenarios: List[ScenarioComparison]
    best_scenario: str
    extra_extension_mild_or_substantial: str
    summary: str


@dataclass
class AssumptionEntry:
    """One assumption in the appendix."""
    assumption: str
    status: str
    source: str
    comment: str

    def __post_init__(self) -> None:
        if self.status not in ASSUMPTION_STATUSES:
            raise ValueError(
                f"Invalid assumption status '{self.status}'. "
                f"Must be one of {ASSUMPTION_STATUSES}"
            )


@dataclass
class FoundationalGap:
    """One remaining foundational gap."""
    gap: str
    severity: str
    notes: str


@dataclass
class AppendixBClassification:
    """Final dual-track + overall classification."""
    dm_classification: str
    de_classification: str
    overall_classification: str
    dm_justification: str
    de_justification: str
    overall_justification: str

    def __post_init__(self) -> None:
        if self.dm_classification not in DM_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid DM classification '{self.dm_classification}'. "
                f"Must be one of {DM_CLASSIFICATION_OPTIONS}"
            )
        if self.de_classification not in DE_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid DE classification '{self.de_classification}'. "
                f"Must be one of {DE_CLASSIFICATION_OPTIONS}"
            )
        if self.overall_classification not in APPENDIX_B_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid overall classification '{self.overall_classification}'. "
                f"Must be one of {APPENDIX_B_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class AppendixBResult:
    """Top-level Appendix B result."""
    valid: bool
    problem_definitions: List[DarkSectorProblem]
    dark_matter_result: DarkMatterResult
    dark_energy_result: DarkEnergyResult
    minimal_models: List[MinimalModel]
    comparisons: List[ComparisonResult]
    classification: AppendixBClassification
    assumptions: List[AssumptionEntry]
    remaining_gaps: List[FoundationalGap]
    nonclaims: List[str]


# ===================================================================
# Part A — Separate the two problems
# ===================================================================

def define_dark_sector_problems() -> List[DarkSectorProblem]:
    """Define the dark matter and dark energy problems in GRUT terms.

    These are explicitly separated: different regimes, different
    observational signatures, different GRUT sectors relevant.
    """
    dm_sectors = [
        SectorRelevance(
            sector="gravitational",
            relevance="directly_relevant",
            reasoning=(
                "The gravitational sector provides the metric potential wells "
                "in which any dark-matter-like effect must manifest."
            ),
        ),
        SectorRelevance(
            sector="macro_scalar_memory",
            relevance="directly_relevant",
            reasoning=(
                "The memory scalar Phi produces stress-energy T^Phi_ab that "
                "gravitates.  In a potential well, the memory field responds "
                "to local curvature via constitutive relaxation, producing an "
                "effective gravitating mass contribution.  This is the primary "
                "candidate for dark-matter-like behavior."
            ),
        ),
        SectorRelevance(
            sector="defect_triplet",
            relevance="absent",
            reasoning=(
                "The O(3) hedgehog defect requires a spatial center and S^2 "
                "winding topology.  Galaxy/cluster-scale systems are not "
                "compact objects with strong-field interiors.  The defect "
                "sector has no cosmological or cluster-scale analogue."
            ),
        ),
        SectorRelevance(
            sector="curvature_trigger",
            relevance="dormant",
            reasoning=(
                "The Kretschner trigger is calibrated for the strong-field "
                "compact-object regime.  In galaxy/cluster-scale weak-field "
                "environments, K is many orders of magnitude below the "
                "strong-field threshold.  The trigger does not fire."
            ),
        ),
        SectorRelevance(
            sector="portal_interaction",
            relevance="dormant",
            reasoning=(
                "Portal coupling g_p Phi^2 |Phi_vec|^2 is relevant only when "
                "both macro and defect sectors are active.  Since the defect "
                "sector is absent at cosmological/cluster scales, portal "
                "coupling is inoperative."
            ),
        ),
    ]

    de_sectors = [
        SectorRelevance(
            sector="gravitational",
            relevance="directly_relevant",
            reasoning=(
                "The gravitational sector provides the cosmological background "
                "via the Friedmann equations."
            ),
        ),
        SectorRelevance(
            sector="macro_scalar_memory",
            relevance="directly_relevant",
            reasoning=(
                "The memory scalar Phi(t) in the cosmological (FRW) regime "
                "produces effective stress-energy with equation of state w_Phi.  "
                "At equilibrium (Phi = source): rho_Phi -> 0, w_Phi -> -1.  "
                "During transients: rho_Phi nonzero, w_Phi varies.  This is "
                "the primary candidate for dark-energy-like behavior."
            ),
        ),
        SectorRelevance(
            sector="defect_triplet",
            relevance="absent",
            reasoning=(
                "Same as for dark matter: no cosmological analogue for the "
                "hedgehog defect."
            ),
        ),
        SectorRelevance(
            sector="curvature_trigger",
            relevance="conditionally_relevant",
            reasoning=(
                "In the very early universe, K diverges and the trigger fires.  "
                "At late times (current epoch), K is small and the trigger is "
                "dormant.  Relevant only for early-universe dark-energy "
                "transients, not for late-time acceleration."
            ),
        ),
        SectorRelevance(
            sector="portal_interaction",
            relevance="absent",
            reasoning="Portal coupling inoperative without defect sector.",
        ),
    ]

    dm_problem = DarkSectorProblem(
        name="dark_matter",
        description=(
            "Test whether the GRUT memory field can produce an effective "
            "gravitating component that mimics dark matter behavior in "
            "galaxy/cluster-scale systems, particularly in cluster collision "
            "scenarios like the Bullet Cluster where mass and gas separate."
        ),
        relevant_grut_sectors=dm_sectors,
        requires_extension=True,
        shared_field_content=True,
        key_observational_signatures=[
            "galaxy_rotation_curves",
            "cluster_mass_gas_separation_bullet_cluster",
            "gravitational_lensing_mass_excess",
            "CMB_matter_power_spectrum",
            "cosmic_structure_formation",
        ],
    )

    de_problem = DarkSectorProblem(
        name="dark_energy",
        description=(
            "Test whether the GRUT memory field and vacuum architecture can "
            "produce an effective large-scale vacuum tension or negative-"
            "pressure-like behavior that could account for observed cosmic "
            "acceleration."
        ),
        relevant_grut_sectors=de_sectors,
        requires_extension=True,
        shared_field_content=True,
        key_observational_signatures=[
            "cosmic_acceleration_SNIa",
            "BAO_distance_scale",
            "CMB_integrated_Sachs_Wolfe",
            "equation_of_state_w_near_minus_1",
        ],
    )

    return [dm_problem, de_problem]


# ===================================================================
# Part B — Dark Matter Analysis
# ===================================================================

def analyze_dark_matter() -> DarkMatterResult:
    """Analyze whether the GRUT memory field can serve as dark matter.

    The analysis uses hard-gated classification logic:
    - If memory_collisionless == False AND scaling_matches_cdm == False:
      BLOCK 'derived' and 'strongly_suggested'
      Default to 'partial_mimic'
      Allow 'effective_only' ONLY with stable weak-field phenomenology
    """
    tests = [
        # Test 1: Memory stress-energy nonzero
        DarkMatterTest(
            test_name="memory_stress_energy_nonzero",
            question=(
                "Does the GRUT memory field produce nonzero stress-energy "
                "T^Phi_ab that enters the Einstein equations?"
            ),
            result="yes",
            viable=True,
            interpretation_level="effective_only",
            comment=(
                "The memory scalar Phi produces nonzero stress-energy that "
                "enters the Einstein equations as a source term.  In a "
                "potential well, the constitutive relaxation tau * dPhi/dr + "
                "Phi = S(r) means Phi tracks the local curvature source with "
                "a spatial lag.  The lag produces a nonzero gradient (dPhi/dr) "
                "and therefore nonzero T^Phi_ab.  This stress-energy "
                "contribution is a constitutive response to the local metric, "
                "not an independent matter sector."
            ),
        ),

        # Test 2: Memory is collisionless
        DarkMatterTest(
            test_name="memory_collisionless",
            question=(
                "Is the GRUT memory field collisionless like CDM particles?"
            ),
            result="no",
            viable=False,
            interpretation_level="failed",
            comment=(
                "The memory field is constitutive (first-order relaxation), not "
                "a population of collisionless particles governed by the Boltzmann "
                "equation.  It has no particle number, no phase space distribution, "
                "no velocity dispersion, and no collisionless dynamics.  This is a "
                "fundamental ontological mismatch with CDM: the memory field is a "
                "geometric response, not a matter species."
            ),
        ),

        # Test 3: Cluster-collision constitutive response
        DarkMatterTest(
            test_name="cluster_collision_constitutive_response",
            question=(
                "Does the GRUT constitutive response provide a qualitative "
                "analogy to cluster-collision mass-gas offset?"
            ),
            result="qualitative_analogy_only",
            viable=False,
            interpretation_level="partial_mimic",
            comment=(
                "In a cluster collision, the gas (baryonic) component is shocked "
                "and decelerated while the dominant gravitating mass passes "
                "through.  The GRUT memory field, being sourced by local "
                "curvature/geometry, would track the total gravitational "
                "potential well rather than the gas distribution.  This "
                "provides a qualitative analogy to mass-gas offset.  "
                "However: no dynamical cluster-collision model is constructed; "
                "no lensing map is computed; no Bullet Cluster signature is "
                "reproduced or semi-reproduced; the mechanism is constitutive "
                "(not collisionless); and no empirical confrontation is "
                "performed.  This is an analogy identification, not a "
                "derivation or prediction."
            ),
        ),

        # Test 4: Defect sector relevant cosmologically
        DarkMatterTest(
            test_name="defect_sector_cosmological_relevance",
            question=(
                "Is the O(3) defect sector relevant for dark matter at "
                "galaxy/cluster scales?"
            ),
            result="no",
            viable=False,
            interpretation_level="failed",
            comment=(
                "The O(3) hedgehog defect requires a spatial center and S^2 "
                "winding topology (pi_2(S^2) = Z).  Galaxy and cluster-scale "
                "systems are not compact objects.  The defect sector has no "
                "analogue at these scales.  Component B support (1/r^2) is "
                "strictly a strong-field-interior phenomenon."
            ),
        ),

        # Test 5: Scaling matches CDM
        DarkMatterTest(
            test_name="scaling_matches_cdm",
            question=(
                "Does the memory field energy density scale as rho ~ a^-3 "
                "like CDM in an expanding universe?"
            ),
            result="no",
            viable=False,
            interpretation_level="failed",
            comment=(
                "CDM dilutes as rho_CDM ~ a^-3 (matter dilution law) in an "
                "expanding universe, which is essential for CMB and BBN "
                "concordance.  The GRUT memory energy density rho_Phi depends "
                "on the lag (Phi - source), not on cosmological dilution.  "
                "At equilibrium (Phi = source), rho_Phi -> 0.  Out of "
                "equilibrium, rho_Phi depends on the relaxation dynamics and "
                "source evolution, not on a^-3 scaling.  The memory field "
                "therefore fails to supply the standard CDM dilution law and "
                "is not presently compatible with a standard CDM role in "
                "early-universe concordance without further extension."
            ),
        ),

        # Test 6: Halo profiles
        DarkMatterTest(
            test_name="halo_profile_structure",
            question=(
                "Can the memory field produce stable halo-like mass profiles "
                "in galaxies?"
            ),
            result="qualitative_only",
            viable=False,
            interpretation_level="partial_mimic",
            comment=(
                "The memory stress-energy produces an effective mass "
                "contribution in gravitational potential wells.  The "
                "resulting profile is set by the source geometry (the "
                "baryonic mass distribution and resulting curvature), not "
                "by virial equilibrium of a collisionless particle "
                "population.  The memory response is a constitutive "
                "echo of the baryonic potential, not an independent halo "
                "structure.  Whether this produces rotation-curve-like "
                "behavior depends on the specific source-response relation "
                "at galactic scales, which is not derived here."
            ),
        ),
    ]

    # Key boolean criteria
    memory_gravitates = True
    memory_collisionless = False
    memory_survives_collision = False  # qualitative pathway only, not demonstrated
    defect_relevant = False
    scaling_matches = False
    has_stable_pheno = False  # no quantitative weak-field regime derivation

    # Hard-gated classification logic
    # Gate 1: collisionless=False AND scaling=False → block upper classifications
    if not memory_collisionless and not scaling_matches:
        if has_stable_pheno:
            classification = "dark_matter_interpretation_effective_only"
        else:
            classification = "dark_matter_interpretation_partial_mimic"
    elif memory_gravitates and memory_collisionless and scaling_matches:
        # Unreachable given above, but logically complete
        if defect_relevant:
            classification = "dark_matter_interpretation_derived_within_published_grut"
        else:
            classification = "dark_matter_interpretation_strongly_suggested_by_extension"
    else:
        classification = "dark_matter_interpretation_failed"

    justification = (
        "The GRUT memory field produces nonzero stress-energy that enters "
        "the Einstein equations, and the constitutive response to potential "
        "rather than gas provides a qualitative analogy to mass-gas offset.  "
        "However, the memory field is fundamentally NOT collisionless "
        "(constitutive relaxation, not Boltzmann dynamics), does NOT "
        "reproduce CDM scaling (rho depends on lag, not a^-3), and does "
        "NOT constitute an independent matter sector (it is a geometric "
        "response).  These foundational failures block 'derived' and "
        "'strongly_suggested'.  No stable weak-field phenomenology with "
        "explicit regime bounds is derived, blocking 'effective_only'.  "
        "Classification: partial_mimic — qualitative analogy, wrong "
        "ontology, wrong scaling law, no cosmological consistency."
    )

    summary = (
        "The GRUT memory field produces nonzero stress-energy in potential "
        "wells, and its constitutive response to curvature rather than gas "
        "provides a qualitative analogy to mass-gas offset in cluster "
        "collisions.  But it is not dark matter: it is not collisionless, "
        "does not scale as a^-3, is not an independent matter sector, and "
        "has no cosmological concordance with CMB/BBN.  The defect sector "
        "is entirely absent at these scales.  No dynamical cluster-collision "
        "model is constructed.  Best classification: partial mimic."
    )

    return DarkMatterResult(
        tests=tests,
        memory_gravitates_independently=memory_gravitates,
        memory_collisionless=memory_collisionless,
        memory_survives_cluster_collision=memory_survives_collision,
        defect_sector_relevant=defect_relevant,
        scaling_matches_cdm=scaling_matches,
        has_stable_weak_field_phenomenology=has_stable_pheno,
        classification=classification,
        justification=justification,
        summary=summary,
    )


# ===================================================================
# Part C — Dark Energy Analysis
# ===================================================================

def analyze_dark_energy() -> DarkEnergyResult:
    """Analyze whether the GRUT memory field can serve as dark energy.

    The analysis uses hard-gated classification logic:
    - If vacuum_tension_derived == False AND cc_explained == False:
      BLOCK 'derived' and 'strongly_suggested'
      Default to 'reframes_but_does_not_solve' if reframing value exists
    """
    tests = [
        # Test 1: Produces negative pressure
        DarkEnergyTest(
            test_name="produces_negative_pressure",
            question=(
                "Can the GRUT memory field produce negative pressure (w < 0) "
                "in a cosmological setting?"
            ),
            result="yes_conditionally",
            viable=True,
            interpretation_level="effective_only",
            comment=(
                "During transients when the memory field lags its source "
                "(Phi != S), the effective stress-energy can have p_Phi < 0.  "
                "Specifically, when the effective potential energy dominates "
                "the kinetic energy: V_eff(Phi) > (dPhi/dt)^2 / 2.  However, "
                "this condition is transient: the constitutive relaxation "
                "drives Phi toward S, dissipating the lag.  The negative "
                "pressure is therefore temporary, not sustained."
            ),
        ),

        # Test 2: Equation of state w = -1
        DarkEnergyTest(
            test_name="equation_of_state_w_minus_1",
            question=(
                "Does the memory field produce w = -1 (cosmological constant "
                "equation of state)?"
            ),
            result="yes_trivially",
            viable=False,
            interpretation_level="reframes_only",
            comment=(
                "At equilibrium (Phi = source, dPhi/dt = 0): rho_Phi -> 0 "
                "and w_Phi -> -1 as a limiting ratio (0/0 form regularized).  "
                "This is cosmological-constant-like but trivially so: the "
                "energy density is ZERO at equilibrium.  A w = -1 equation "
                "of state with rho = 0 is indistinguishable from empty vacuum.  "
                "This is not a prediction of dark energy; it is a statement "
                "that the equilibrium state is vacuum."
            ),
        ),

        # Test 3: Vacuum tension derived
        DarkEnergyTest(
            test_name="vacuum_tension_derived",
            question=(
                "Does the GRUT architecture derive a persistent vacuum "
                "tension (positive cosmological constant) from the memory "
                "field?"
            ),
            result="no",
            viable=False,
            interpretation_level="failed",
            comment=(
                "The memory field generates effective tension during transients "
                "but not a persistent vacuum tension.  The constitutive "
                "relaxation structure (tau * dPhi/dt + Phi = S) drives the "
                "field toward equilibrium on a timescale tau.  At late times, "
                "the memory relaxes to its source value and rho_Phi -> 0.  "
                "There is no mechanism within the published architecture to "
                "sustain a nonzero vacuum energy density indefinitely.  The "
                "GRUT memory cannot generate Lambda."
            ),
        ),

        # Test 4: Cosmological constant explained
        DarkEnergyTest(
            test_name="cosmological_constant_explained",
            question=(
                "Does GRUT explain the observed value of the cosmological "
                "constant Lambda ~ 10^-122 M_Pl^4?"
            ),
            result="no",
            viable=False,
            interpretation_level="failed",
            comment=(
                "GRUT does not address the cosmological constant problem.  "
                "The fundamental question — why the vacuum energy density is "
                "~120 orders of magnitude below naive quantum field theory "
                "expectations — is not resolved or even reframed by the "
                "memory architecture.  The memory field produces zero vacuum "
                "energy at equilibrium, which is consistent with Lambda = 0 "
                "but does not explain Lambda > 0."
            ),
        ),

        # Test 5: Requires cosmological extension
        DarkEnergyTest(
            test_name="requires_cosmological_extension",
            question=(
                "Does the dark energy interpretation require assumptions "
                "beyond published GRUT canon?"
            ),
            result="yes",
            viable=False,
            interpretation_level="failed",
            comment=(
                "The cosmological dark energy interpretation requires: "
                "(1) specifying the cosmological source function S(H, K), "
                "whose form is not derived from canon; "
                "(2) identifying the cosmological relaxation timescale "
                "tau_cosmo, which may differ from the compact-object tau; "
                "(3) treating the constitutive memory field as if it has "
                "standard stress-energy, which is a heuristic extension for "
                "a field without a Lagrangian.  All three are extension "
                "assumptions, not inherited canon."
            ),
        ),
    ]

    # Key boolean criteria
    produces_neg_pressure = True
    w_minus_1 = True  # trivially, at equilibrium with rho=0
    vacuum_tension = False
    cc_explained = False
    requires_ext = True

    # Hard-gated classification logic
    # Gate 1: vacuum_tension=False AND cc_explained=False → block upper
    if not vacuum_tension and not cc_explained:
        if produces_neg_pressure or w_minus_1:
            classification = "dark_energy_interpretation_reframes_but_does_not_solve"
        else:
            classification = "dark_energy_interpretation_failed"
    elif vacuum_tension and cc_explained:
        classification = "dark_energy_interpretation_derived_within_published_grut"
    elif vacuum_tension or cc_explained:
        classification = "dark_energy_interpretation_strongly_suggested_by_extension"
    else:
        classification = "dark_energy_interpretation_failed"

    justification = (
        "The GRUT memory field produces transient negative pressure during "
        "out-of-equilibrium periods and w = -1 trivially at equilibrium "
        "(where rho = 0).  However, no persistent vacuum tension is derived "
        "and the cosmological constant problem is not addressed.  These two "
        "foundational failures block 'derived' and 'strongly_suggested'.  "
        "The reframing value is: GRUT replaces 'what is Lambda?' with 'why "
        "does cosmological memory lag persist?' — a different question but "
        "not a solution.  Classification: reframes_but_does_not_solve."
    )

    summary = (
        "The GRUT memory architecture provides a qualitative reframing of "
        "the dark energy problem: if a persistent cosmological memory lag "
        "exists, it would produce transient negative pressure and effective "
        "vacuum tension.  But the architecture does not explain WHY such a "
        "lag would persist (constitutive relaxation dissipates it), does not "
        "derive Lambda, and requires extension assumptions for the "
        "cosmological source function and timescale.  The dark energy "
        "interpretation is a reframing, not a solution."
    )

    return DarkEnergyResult(
        tests=tests,
        produces_negative_pressure=produces_neg_pressure,
        equation_of_state_w_minus_1=w_minus_1,
        vacuum_tension_derived=vacuum_tension,
        cosmological_constant_explained=cc_explained,
        requires_cosmological_extension=requires_ext,
        classification=classification,
        justification=justification,
        summary=summary,
    )


# ===================================================================
# Part D — Minimal Mathematical Models
# ===================================================================

def build_minimal_models() -> List[MinimalModel]:
    """Build minimal mathematical models for both tracks."""
    dm_model = MinimalModel(
        track="dark_matter",
        field_content="Scalar memory field Phi(r) in weak-field potential wells",
        regime=(
            "Weak-field galaxy/cluster-scale: Phi << 1, dPhi/dr << 1, "
            "curvature well below strong-field threshold"
        ),
        effective_equations=[
            "Constitutive relaxation: tau * dPhi/dr + Phi = S(r) = alpha_vac * M(r)/r",
            "Effective gravitating mass: Delta_M(r) ~ integral[T^Phi_tt * 4*pi*r^2 dr]",
            "T^Phi_tt ~ (1/2)(dPhi/dr)^2 ~ (alpha_vac * M / r)^2 / (2 * tau^2) at lag",
            "Weak-field metric correction: delta_g_tt ~ -2 * Delta_M(r) / r",
        ],
        parameters=[
            ParameterEntry(
                name="alpha_vac",
                value_or_form="1/3",
                authority="inherited",
                source="GRUT canonical vacuum ratio",
            ),
            ParameterEntry(
                name="tau",
                value_or_form="sqrt(3/2) in strong-field units",
                authority="inherited",
                source="GRUT canonical relaxation timescale",
            ),
            ParameterEntry(
                name="S(r)",
                value_or_form="alpha_vac * M(r)/r (assumed form)",
                authority="phenomenological",
                source="Extension from strong-field source to weak-field regime",
            ),
            ParameterEntry(
                name="tau_galactic",
                value_or_form="unidentified",
                authority="open",
                source="Galactic relaxation timescale not derived from canon",
            ),
        ],
        interpretation_type="phenomenological",
        summary=(
            "The dark matter minimal model uses the GRUT memory scalar in "
            "weak-field potential wells.  The memory tracks local curvature "
            "with a spatial lag, producing effective gravitating stress-energy.  "
            "The model is phenomenological: the weak-field source function "
            "S(r) and galactic relaxation scale tau_galactic are not derived "
            "from published canon.  No particle dark matter is introduced."
        ),
    )

    de_model = MinimalModel(
        track="dark_energy",
        field_content="Homogeneous scalar memory field Phi(t) in FRW cosmology",
        regime=(
            "Late-time cosmology: H ~ H_0, K << K_threshold, "
            "memory near equilibrium with possible residual lag"
        ),
        effective_equations=[
            "Constitutive relaxation: tau_cosmo * dPhi/dt + Phi = S(H, K)",
            "Effective energy density: rho_Phi = (1/2)(dPhi/dt)^2 + V_eff(Phi)",
            "Effective pressure: p_Phi = (1/2)(dPhi/dt)^2 - V_eff(Phi)",
            "Modified Friedmann: H^2 = (8*pi/3)(rho_matter + rho_Phi)",
            "Equation of state: w_Phi = p_Phi / rho_Phi -> -1 at equilibrium",
        ],
        parameters=[
            ParameterEntry(
                name="tau_cosmo",
                value_or_form="unidentified cosmological relaxation timescale",
                authority="open",
                source="Not derived from compact-object tau",
            ),
            ParameterEntry(
                name="S(H,K)",
                value_or_form="assumed monotonic in curvature, form not derived",
                authority="phenomenological",
                source="Extension from strong-field source function",
            ),
            ParameterEntry(
                name="V_eff",
                value_or_form="~ Phi^2 / (2*tau^2) (effective, not variational)",
                authority="phenomenological",
                source="Effective description of relaxation restoring dynamics",
            ),
            ParameterEntry(
                name="H_0",
                value_or_form="~70 km/s/Mpc (observed)",
                authority="phenomenological",
                source="Cosmological observation, not GRUT-derived",
            ),
        ],
        interpretation_type="phenomenological",
        summary=(
            "The dark energy minimal model uses the homogeneous GRUT memory "
            "scalar in FRW cosmology.  At equilibrium: rho = 0, w = -1 "
            "(trivially vacuum).  During transients: negative pressure is "
            "possible but dissipates.  The model is phenomenological: "
            "tau_cosmo, S(H,K), and V_eff are not derived from canon."
        ),
    )

    return [dm_model, de_model]


# ===================================================================
# Part E — Comparison Classes
# ===================================================================

def build_comparisons(
    dm_result: DarkMatterResult,
    de_result: DarkEnergyResult,
) -> List[ComparisonResult]:
    """Build three-scenario comparisons for both tracks."""
    dm_comparison = ComparisonResult(
        track="dark_matter",
        scenarios=[
            ScenarioComparison(
                scenario="classical_baseline",
                outcome=(
                    "No dark matter without explicit CDM particle species.  "
                    "GR + baryons alone fails rotation curves, Bullet Cluster, "
                    "CMB power spectrum, structure formation."
                ),
                assumptions_needed=["CDM particle species (WIMP, axion, etc.)"],
                comment="Standard Lambda-CDM requires an explicit dark matter sector.",
            ),
            ScenarioComparison(
                scenario="grut_memory_only",
                outcome=(
                    "Nonzero memory stress-energy in potential wells.  "
                    "Constitutive response tracks potential, not gas, providing "
                    "qualitative analogy to mass-gas offset.  "
                    "But: not collisionless, wrong scaling (no a^-3), not an "
                    "independent matter sector, no CMB/BBN concordance."
                ),
                assumptions_needed=[
                    "Weak-field source function S(r) form",
                    "Galactic relaxation timescale tau_galactic",
                ],
                comment="Partial analogy only: right qualitative direction, wrong ontology.",
            ),
            ScenarioComparison(
                scenario="grut_memory_plus_extension",
                outcome=(
                    "If one adds a phenomenological weak-field enhancement "
                    "(e.g., slower relaxation at galactic scales, modified "
                    "source function), the memory stress could be tuned to "
                    "match rotation curves in specific galaxies.  But this "
                    "is parameter fitting, not derivation, and still lacks "
                    "collisionless dynamics and CDM scaling."
                ),
                assumptions_needed=[
                    "Weak-field source function S(r) form",
                    "Galactic relaxation timescale tau_galactic",
                    "Phenomenological enhancement at galactic scales",
                ],
                comment=(
                    "Extension is substantial: requires fitting parameters "
                    "that are not derived from published canon."
                ),
            ),
        ],
        best_scenario="grut_memory_only",
        extra_extension_mild_or_substantial="substantial",
        summary=(
            "The memory-only scenario provides the most honest interpretation: "
            "nonzero constitutive stress-energy in potential wells, but "
            "ontologically and cosmologically incompatible with standard CDM.  "
            "Lambda-CDM outperforms GRUT on every dark-matter observable.  "
            "Further extension adds parameter freedom but not derivational "
            "progress."
        ),
    )

    de_comparison = ComparisonResult(
        track="dark_energy",
        scenarios=[
            ScenarioComparison(
                scenario="classical_baseline",
                outcome=(
                    "Dark energy requires an explicit cosmological constant "
                    "Lambda or dynamical dark energy field (quintessence).  "
                    "Lambda fits observations but the value Lambda ~ 10^-122 "
                    "M_Pl^4 is unexplained."
                ),
                assumptions_needed=["Cosmological constant Lambda (value unexplained)"],
                comment="Standard Lambda-CDM requires Lambda as a free parameter.",
            ),
            ScenarioComparison(
                scenario="grut_memory_only",
                outcome=(
                    "Memory field at equilibrium: rho = 0, w = -1 (trivially "
                    "vacuum).  During transients: negative pressure possible "
                    "but dissipates on timescale tau.  Cannot sustain late-time "
                    "acceleration.  Reframes the question as 'why does lag "
                    "persist?' but does not answer it."
                ),
                assumptions_needed=[
                    "Cosmological source function S(H,K) form",
                    "Cosmological relaxation timescale tau_cosmo",
                    "Effective potential V_eff form",
                ],
                comment="Reframing value but no solution to Lambda problem.",
            ),
            ScenarioComparison(
                scenario="grut_memory_plus_extension",
                outcome=(
                    "If one assumes a slowly-evolving cosmological source that "
                    "maintains a persistent lag (Phi != S indefinitely), then "
                    "rho_Phi > 0 and w_Phi < 0 can be sustained.  But this "
                    "requires the source function to evolve in a way that "
                    "prevents equilibration — effectively introducing a "
                    "fine-tuning problem analogous to the Lambda problem itself."
                ),
                assumptions_needed=[
                    "Slowly-evolving source function (fine-tuned)",
                    "Cosmological relaxation timescale tau_cosmo",
                    "Persistence mechanism for cosmological lag",
                ],
                comment=(
                    "Extension is substantial and potentially circular: "
                    "the fine-tuning of the source function mirrors the "
                    "Lambda fine-tuning it was meant to explain."
                ),
            ),
        ],
        best_scenario="grut_memory_only",
        extra_extension_mild_or_substantial="substantial",
        summary=(
            "The memory-only scenario provides the most honest interpretation: "
            "limited conceptual reframing of the vacuum problem, but no "
            "solution.  Lambda-CDM outperforms GRUT on dark energy observables.  "
            "Further extension risks circularity (fine-tuning the source to "
            "maintain lag is analogous to fine-tuning Lambda)."
        ),
    )

    return [dm_comparison, de_comparison]


# ===================================================================
# Part F — Classification
# ===================================================================

def classify_appendix_b(
    dm_result: DarkMatterResult,
    de_result: DarkEnergyResult,
) -> AppendixBClassification:
    """Produce the final dual-track and overall classification.

    The overall classification reflects the combined status of both tracks.
    """
    dm_class = dm_result.classification
    de_class = de_result.classification

    # Overall classification logic
    dm_level = DM_CLASSIFICATION_OPTIONS.index(dm_class)
    de_level = DE_CLASSIFICATION_OPTIONS.index(de_class)

    # Both derived or strongly suggested → dual strong
    if dm_level <= 1 and de_level <= 1:
        overall = "dual_dark_sector_extension_strong"
    # One failed → check the other
    elif dm_level == 4 and de_level == 4:
        overall = "appendix_b_failed"
    elif dm_level < de_level:
        overall = "dark_matter_stronger_than_dark_energy"
    elif de_level < dm_level:
        overall = "dark_energy_stronger_than_dark_matter"
    else:
        overall = "mixed_and_partial"

    overall_justification = (
        f"Dark matter track: {dm_class} (level {dm_level}/4).  "
        f"Dark energy track: {de_class} (level {de_level}/4).  "
        "Both tracks yield partial results: limited analogy for DM "
        "and limited reframing for DE.  Neither dark-sector target "
        "is derived or strongly suggested within the published "
        "architecture.  Overall: mixed_and_partial."
    )

    return AppendixBClassification(
        dm_classification=dm_class,
        de_classification=de_class,
        overall_classification=overall,
        dm_justification=dm_result.justification,
        de_justification=de_result.justification,
        overall_justification=overall_justification,
    )


# ===================================================================
# Assumptions
# ===================================================================

def build_assumptions() -> List[AssumptionEntry]:
    """Build the explicit assumption table for Appendix B."""
    return [
        AssumptionEntry(
            assumption="Memory scalar Phi produces gravitating stress-energy T^Phi_ab",
            status="inherited_from_canon",
            source="Phase IV memory tensor stress-energy",
            comment="Established in the published architecture.",
        ),
        AssumptionEntry(
            assumption="Constitutive relaxation: tau * dPhi/dt + Phi = S",
            status="inherited_from_canon",
            source="Phase IV first-order memory structure",
            comment="Locked in published canon.",
        ),
        AssumptionEntry(
            assumption="O(3) defect sector absent at cosmological/cluster scales",
            status="inherited_from_canon",
            source="Appendix A structural finding",
            comment="Hedgehog requires spatial center + S^2 topology.",
        ),
        AssumptionEntry(
            assumption="Weak-field source function S(r) for DM interpretation",
            status="extension_assumption",
            source="Extended from strong-field canon",
            comment="Form not derived; needed for DM minimal model.",
        ),
        AssumptionEntry(
            assumption="Galactic relaxation timescale tau_galactic",
            status="phenomenological",
            source="Not derived from canon",
            comment="May differ from compact-object tau.",
        ),
        AssumptionEntry(
            assumption="Cosmological source function S(H,K) for DE interpretation",
            status="extension_assumption",
            source="Extended from strong-field canon",
            comment="Form not derived; needed for DE minimal model.",
        ),
        AssumptionEntry(
            assumption="Cosmological relaxation timescale tau_cosmo",
            status="phenomenological",
            source="Not derived from canon",
            comment="May differ from compact-object tau.",
        ),
        AssumptionEntry(
            assumption="Effective potential V_eff(Phi) for DE stress-energy",
            status="extension_assumption",
            source="Heuristic description of relaxation restoring dynamics",
            comment="The constitutive memory has no variational potential.",
        ),
        AssumptionEntry(
            assumption="No new fields or particle species introduced",
            status="inherited_from_canon",
            source="Minimal extension principle",
            comment="Only published GRUT field content used.",
        ),
    ]


# ===================================================================
# Nonclaims
# ===================================================================

def build_nonclaims() -> List[str]:
    """Build the explicit nonclaims list for Appendix B."""
    return [
        (
            "Appendix B does not derive cold dark matter.  The memory field "
            "is a constitutive geometric response, not a collisionless "
            "particle species.  It has no particle number, no phase space "
            "distribution, no velocity dispersion, and no self-gravitating "
            "virial equilibrium."
        ),
        (
            "Appendix B does not derive a cosmological constant.  No "
            "persistent vacuum tension is produced.  At equilibrium the "
            "memory contributes zero energy density.  The fundamental "
            "question of why Lambda ~ 10^-122 M_Pl^4 is not addressed."
        ),
        (
            "Appendix B does not reproduce the Bullet Cluster.  No dynamical "
            "cluster-collision model is constructed.  No lensing map is "
            "computed.  No mass-gas separation is derived.  The appendix "
            "identifies only a qualitative analogy by which a constitutive "
            "geometric response could track potential rather than gas."
        ),
        (
            "Appendix B does not establish early-universe concordance.  The "
            "memory field does not scale as a^-3 and is not presently "
            "compatible with a standard CDM role in CMB acoustic peaks, "
            "BBN, or structure formation without fundamental extension "
            "beyond published canon."
        ),
        (
            "Appendix B does not close the dark sector within published "
            "GRUT.  Neither the dark matter nor the dark energy "
            "interpretation is derived or strongly suggested.  Both remain "
            "at the level of limited analogy or limited reframing."
        ),
        (
            "The O(3) defect sector is not invoked for any dark-sector "
            "interpretation.  It has no cosmological or cluster-scale "
            "analogue."
        ),
        (
            "The dark-energy w = -1 at equilibrium is trivially vacuum, "
            "not a prediction.  Zero energy density with w = -1 is "
            "indistinguishable from empty space.  No observational "
            "consequence follows."
        ),
        (
            "Memory lag is not persistent vacuum energy.  The constitutive "
            "structure actively dissipates the lag via exponential "
            "relaxation toward equilibrium.  The reframing ('why does lag "
            "persist?') immediately raises a question the architecture "
            "does not answer."
        ),
        (
            "No empirical confrontation is performed.  Neither "
            "interpretation has been tested against rotation curves, "
            "lensing data, SNIa, BAO, CMB power spectrum, or any other "
            "observational dataset."
        ),
        (
            "Parameters tau_cosmo, tau_galactic, S(H,K), S(r), and V_eff "
            "are not derived from published canon.  They are extension "
            "assumptions or phenomenological placeholders."
        ),
        (
            "The memory stress-energy does not constitute an independent "
            "matter sector.  It is a constitutive response to the local "
            "metric, sourced by and determined by the baryonic "
            "gravitational potential.  It is not autonomous."
        ),
        (
            "Appendix B does not claim the memory field is equivalent to "
            "modified gravity (MOND, f(R), etc.).  The constitutive memory "
            "mechanism has different physical content from modified-gravity "
            "theories."
        ),
    ]


# ===================================================================
# Remaining Gaps
# ===================================================================

def identify_remaining_gaps() -> List[FoundationalGap]:
    """Identify remaining foundational gaps after Appendix B."""
    return [
        FoundationalGap(
            gap=(
                "No collisionless dynamics: the memory field cannot replicate "
                "the collisionless behavior essential to CDM's success in "
                "structure formation, CMB acoustic peaks, and Bullet Cluster "
                "interpretation."
            ),
            severity="critical",
            notes=(
                "This is a structural limitation, not a parameter gap.  "
                "The constitutive/dissipative nature of GRUT memory is "
                "fundamentally different from collisionless particle dynamics."
            ),
        ),
        FoundationalGap(
            gap=(
                "No CDM scaling law: memory energy density does not dilute "
                "as a^-3, breaking concordance with standard cosmological "
                "evolution."
            ),
            severity="critical",
            notes=(
                "The memory field's energy density depends on lag dynamics, "
                "not on cosmological dilution."
            ),
        ),
        FoundationalGap(
            gap=(
                "No persistent vacuum tension: constitutive relaxation drives "
                "the memory toward equilibrium, precluding sustained dark "
                "energy without fine-tuned source evolution."
            ),
            severity="critical",
            notes=(
                "This is the constitutive obstruction inherited from "
                "Appendix A: first-order relaxation dissipates, not sustains."
            ),
        ),
        FoundationalGap(
            gap=(
                "Weak-field phenomenology not derived: the source function "
                "S(r) at galactic/cluster scales is not derived from "
                "published canon."
            ),
            severity="significant",
            notes=(
                "Deriving S(r) in the weak-field regime would be needed "
                "to upgrade DM from partial_mimic to effective_only."
            ),
        ),
        FoundationalGap(
            gap=(
                "No empirical confrontation: neither interpretation has "
                "been tested against rotation curves, lensing data, SNIa, "
                "BAO, or CMB observations."
            ),
            severity="significant",
            notes="Observable roadmap exists from Bridge document but is untested.",
        ),
    ]


# ===================================================================
# Master compute function
# ===================================================================

def compute_dark_sector_result() -> AppendixBResult:
    """Execute the full Appendix B analysis.

    Returns the complete dual-track dark-sector analysis with
    separate dark matter and dark energy results, minimal models,
    comparisons, classification, assumptions, gaps, and nonclaims.
    """
    problems = define_dark_sector_problems()
    dm_result = analyze_dark_matter()
    de_result = analyze_dark_energy()
    models = build_minimal_models()
    comparisons = build_comparisons(dm_result, de_result)
    classification = classify_appendix_b(dm_result, de_result)
    assumptions = build_assumptions()
    gaps = identify_remaining_gaps()
    nonclaims = build_nonclaims()

    return AppendixBResult(
        valid=True,
        problem_definitions=problems,
        dark_matter_result=dm_result,
        dark_energy_result=de_result,
        minimal_models=models,
        comparisons=comparisons,
        classification=classification,
        assumptions=assumptions,
        remaining_gaps=gaps,
        nonclaims=nonclaims,
    )


# ===================================================================
# Serialization
# ===================================================================

def _serialize(obj: Any) -> Any:
    """Recursively serialize dataclass instances to dicts."""
    if hasattr(obj, "__dataclass_fields__"):
        return {k: _serialize(v) for k, v in asdict(obj).items()}
    if isinstance(obj, list):
        return [_serialize(item) for item in obj]
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    return obj


def appendix_b_result_to_dict(result: AppendixBResult) -> Dict[str, Any]:
    """Convert an AppendixBResult to a plain dict."""
    return _serialize(result)


def appendix_b_result_to_json(result: AppendixBResult) -> str:
    """Convert an AppendixBResult to a JSON string."""
    return json.dumps(appendix_b_result_to_dict(result), indent=2)


def export_appendix_b_result_json(
    result: AppendixBResult,
    path: str = "appendix_b_result.json",
) -> str:
    """Write the result to a JSON file and return the path."""
    data = appendix_b_result_to_json(result)
    with open(path, "w") as f:
        f.write(data)
    return path
