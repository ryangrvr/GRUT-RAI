"""
GRUT Bridge Phase — Parameter Authority Map
============================================

SCOPE
-----
Classify every major GRUT constant and parameter by authority level,
sector membership, derivation status, and future reduction path.

Provide the cross-sector dependency map, observable roadmap entries,
and theory-wide canon hierarchy as explicit, inspectable data structures.

This module serves the bridge document
docs/GRUT_BRIDGE_PHENOMENOLOGY_INTEGRATION.md
and supports Omni-ToE v3 synthesis.

AUTHORITY CLASSES
-----------------
- inherited       : fixed by standard physics or prior locked phase
- derived         : follows from the GRUT action/equations within tested scope
- matched         : value set to reproduce a known physical requirement
- phenomenological: introduced to close a phenomenological gap; not derived
- open            : free parameter, currently scanned or unconstrained

SECTOR TAXONOMY
---------------
1. gravitational           — Einstein/metric sector
2. macro_scalar_memory     — Phi(r) memory-kernel macro field
3. defect_triplet          — O(3) hedgehog vec_Phi^a
4. curvature_trigger       — Kretschner-coupled activation
5. portal_interaction      — g_p Phi^2 |vec_Phi|^2 inter-sector coupling
6. cosmology               — Hubble tension / LCDM / background sector
7. observational            — ringdown, lensing, tidal, phenomenology

CANON HIERARCHY LEVELS
----------------------
- LOCKED
- STRONGLY_SUPPORTED
- PRINCIPLED_AND_STRONGLY_CONSTRAINED
- PROVISIONAL
- FRAMEWORK_CONDITIONAL
- PROXY_DEPENDENT
- EFFECTIVE_OR_PHENOMENOLOGICAL
- REJECTED_IN_TESTED_FORM
- OPEN
- NONCLAIM

BRIDGE CLASSIFICATION OPTIONS
-----------------------------
- sufficient_for_final_toe_synthesis
- strong_but_missing_one_major_bridge
- informative_but_not_yet_enough_for_final_toe_presentation
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


# ---------------------------------------------------------------------------
# Authority class vocabulary
# ---------------------------------------------------------------------------
AUTHORITY_CLASSES = [
    "inherited",
    "derived",
    "matched",
    "phenomenological",
    "open",
]

# ---------------------------------------------------------------------------
# Sector vocabulary
# ---------------------------------------------------------------------------
SECTORS = [
    "gravitational",
    "macro_scalar_memory",
    "defect_triplet",
    "curvature_trigger",
    "portal_interaction",
    "cosmology",
    "observational",
]

# ---------------------------------------------------------------------------
# Canon hierarchy vocabulary
# ---------------------------------------------------------------------------
CANON_HIERARCHY_LEVELS = [
    "LOCKED",
    "STRONGLY_SUPPORTED",
    "PRINCIPLED_AND_STRONGLY_CONSTRAINED",
    "PROVISIONAL",
    "FRAMEWORK_CONDITIONAL",
    "PROXY_DEPENDENT",
    "EFFECTIVE_OR_PHENOMENOLOGICAL",
    "REJECTED_IN_TESTED_FORM",
    "OPEN",
    "NONCLAIM",
]

# ---------------------------------------------------------------------------
# Bridge classification vocabulary
# ---------------------------------------------------------------------------
BRIDGE_CLASSIFICATION_OPTIONS = [
    "sufficient_for_final_toe_synthesis",
    "strong_but_missing_one_major_bridge",
    "informative_but_not_yet_enough_for_final_toe_presentation",
]

# ---------------------------------------------------------------------------
# Observable effect types
# ---------------------------------------------------------------------------
EFFECT_TYPES = [
    "sign",
    "scaling",
    "threshold",
    "deformation",
    "family_of_behaviors",
    "spectral_shift",
    "mass_radius_modification",
    "tidal_modification",
]


# ===================================================================
# Dataclasses
# ===================================================================

@dataclass
class ParameterEntry:
    """A single parameter or constant in the GRUT framework."""
    name: str
    symbol: str
    value: Optional[float]
    value_expr: str
    sectors: List[str]
    authority_class: str
    fixed_by: str
    current_role: str
    structurally_central: bool
    future_reduction_path: str
    notes: str = ""

    def __post_init__(self) -> None:
        if self.authority_class not in AUTHORITY_CLASSES:
            raise ValueError(
                f"Invalid authority class '{self.authority_class}'. "
                f"Must be one of {AUTHORITY_CLASSES}"
            )
        for s in self.sectors:
            if s not in SECTORS:
                raise ValueError(
                    f"Invalid sector '{s}'. Must be one of {SECTORS}"
                )


@dataclass
class ParameterAuthorityMap:
    """Complete parameter/constant authority map."""
    entries: List[ParameterEntry]
    inherited_count: int = 0
    derived_count: int = 0
    matched_count: int = 0
    phenomenological_count: int = 0
    open_count: int = 0

    def __post_init__(self) -> None:
        self._recount()

    def _recount(self) -> None:
        self.inherited_count = sum(
            1 for e in self.entries if e.authority_class == "inherited"
        )
        self.derived_count = sum(
            1 for e in self.entries if e.authority_class == "derived"
        )
        self.matched_count = sum(
            1 for e in self.entries if e.authority_class == "matched"
        )
        self.phenomenological_count = sum(
            1 for e in self.entries if e.authority_class == "phenomenological"
        )
        self.open_count = sum(
            1 for e in self.entries if e.authority_class == "open"
        )


@dataclass
class SectorDependency:
    """One row of the cross-sector dependency table."""
    sector: str
    depends_on: List[str]
    inherited_structures: List[str]
    exported_structures: List[str]
    current_status: str

    def __post_init__(self) -> None:
        if self.sector not in SECTORS:
            raise ValueError(
                f"Invalid sector '{self.sector}'. Must be one of {SECTORS}"
            )
        if self.current_status not in CANON_HIERARCHY_LEVELS:
            raise ValueError(
                f"Invalid status '{self.current_status}'. "
                f"Must be one of {CANON_HIERARCHY_LEVELS}"
            )


@dataclass
class CrossSectorMap:
    """Full cross-sector dependency map."""
    dependencies: List[SectorDependency]
    minimal_backbone: List[str]
    backbone_summary: str
    unity_argument: str


@dataclass
class ObservableEntry:
    """One candidate observable for the empirical roadmap."""
    observable: str
    sectors_probed: List[str]
    relevant_parameters: List[str]
    predicted_effect_type: str
    predicted_effect_description: str
    support_criterion: str
    tension_criterion: str
    falsification_criterion: str
    observational_class: str
    notes: str = ""

    def __post_init__(self) -> None:
        if self.predicted_effect_type not in EFFECT_TYPES:
            raise ValueError(
                f"Invalid effect type '{self.predicted_effect_type}'. "
                f"Must be one of {EFFECT_TYPES}"
            )


@dataclass
class ObservableRoadmap:
    """Complete empirical/observational roadmap."""
    entries: List[ObservableEntry]
    observational_classes: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.observational_classes = sorted(set(
            e.observational_class for e in self.entries
        ))


@dataclass
class CanonHierarchyEntry:
    """One row of the theory-wide canon hierarchy table."""
    claim_or_sector: str
    current_status: str
    basis: str
    caveat: str

    def __post_init__(self) -> None:
        if self.current_status not in CANON_HIERARCHY_LEVELS:
            raise ValueError(
                f"Invalid status '{self.current_status}'. "
                f"Must be one of {CANON_HIERARCHY_LEVELS}"
            )


@dataclass
class CanonHierarchy:
    """Theory-wide canon hierarchy."""
    entries: List[CanonHierarchyEntry]


@dataclass
class BridgeGap:
    """One remaining bridge gap."""
    gap: str
    severity: str  # "critical", "significant", "minor"
    sector: str
    notes: str


@dataclass
class BridgeClassification:
    """Final bridge classification."""
    classification: str
    justification: str
    locked_count: int
    supported_count: int
    open_count: int
    critical_gaps: int

    def __post_init__(self) -> None:
        if self.classification not in BRIDGE_CLASSIFICATION_OPTIONS:
            raise ValueError(
                f"Invalid classification '{self.classification}'. "
                f"Must be one of {BRIDGE_CLASSIFICATION_OPTIONS}"
            )


@dataclass
class BridgeResult:
    """Top-level result of the bridge phenomenology/integration analysis."""
    valid: bool
    parameter_authority_map: ParameterAuthorityMap
    cross_sector_map: CrossSectorMap
    observable_roadmap: ObservableRoadmap
    canon_hierarchy: CanonHierarchy
    bridge_gaps: List[BridgeGap]
    bridge_classification: BridgeClassification
    omni_toe_v3_may_claim: List[str]
    omni_toe_v3_may_not_claim: List[str]


# ===================================================================
# Parameter Authority Map Construction
# ===================================================================

def build_parameter_authority_map() -> ParameterAuthorityMap:
    """Build the complete parameter authority map.

    Every entry is explicit and deterministic. No hidden scoring.
    Authority classes follow strict criteria:
    - inherited: value fixed by GR, standard model, or locked prior phase
    - derived: follows from GRUT action/equations
    - matched: set to reproduce Phase 6C or other physical requirement
    - phenomenological: introduced to close a gap; not derived
    - open: free parameter, scanned but unconstrained
    """
    entries = [
        # --- Gravitational / background parameters ---
        ParameterEntry(
            name="Gravitational constant",
            symbol="G",
            value=1.0,
            value_expr="1 (geometric units)",
            sectors=["gravitational"],
            authority_class="inherited",
            fixed_by="General relativity (geometric units)",
            current_role="Sets gravitational coupling; G=1 in natural units",
            structurally_central=True,
            future_reduction_path="None needed; inherited from GR",
        ),
        ParameterEntry(
            name="Schwarzschild radius",
            symbol="R_S",
            value=1.0,
            value_expr="1 (geometric units, defines length scale)",
            sectors=["gravitational", "macro_scalar_memory", "defect_triplet"],
            authority_class="inherited",
            fixed_by="Schwarzschild solution; sets the unit of length",
            current_role="Fundamental length scale for entire strong-field program",
            structurally_central=True,
            future_reduction_path="None needed; coordinate choice",
        ),
        ParameterEntry(
            name="External mass",
            symbol="M_ext",
            value=0.5,
            value_expr="R_S / 2 = 0.5",
            sectors=["gravitational", "macro_scalar_memory"],
            authority_class="inherited",
            fixed_by="Schwarzschild relation M = R_S/2",
            current_role="Mass parameter in source term X(r) = M/r^2",
            structurally_central=True,
            future_reduction_path="None needed; follows from R_S",
        ),
        ParameterEntry(
            name="Vacuum alpha parameter",
            symbol="alpha_vac",
            value=1.0 / 3.0,
            value_expr="1/3",
            sectors=["gravitational", "macro_scalar_memory"],
            authority_class="inherited",
            fixed_by="Phase 5 locking (GRUT vacuum structure)",
            current_role="Determines R_eq = alpha_vac * R_S; sets onset of strong-field region",
            structurally_central=True,
            future_reduction_path="None needed; locked by vacuum sector",
        ),
        ParameterEntry(
            name="Equilibrium radius",
            symbol="R_eq",
            value=1.0 / 3.0,
            value_expr="alpha_vac * R_S = 1/3",
            sectors=["gravitational", "macro_scalar_memory", "defect_triplet"],
            authority_class="derived",
            fixed_by="Derived from alpha_vac and R_S",
            current_role="Inner boundary of metric comparison domain; strong-field onset",
            structurally_central=True,
            future_reduction_path="None needed; derived",
        ),
        ParameterEntry(
            name="Exterior matching radius",
            symbol="R_ext",
            value=2.0,
            value_expr="2 * R_S = 2.0",
            sectors=["gravitational", "macro_scalar_memory", "defect_triplet"],
            authority_class="inherited",
            fixed_by="Convention: 2*R_S as exterior boundary",
            current_role="Outer boundary of metric comparison domain",
            structurally_central=True,
            future_reduction_path="None needed; boundary convention",
        ),
        # --- Macro scalar / memory sector ---
        ParameterEntry(
            name="Memory kernel time scale",
            symbol="tau",
            value=math.sqrt(1.5),
            value_expr="sqrt(3/2) = sqrt((R_S/R_eq)/2)",
            sectors=["macro_scalar_memory"],
            authority_class="derived",
            fixed_by="Derived from R_S and R_eq: tau^2 = R_S/(2*R_eq)",
            current_role="Sets macro energy density scale: eps_macro = Phi^2/(2*tau^2)",
            structurally_central=True,
            future_reduction_path="None needed; derived from locked parameters",
        ),
        ParameterEntry(
            name="Critical scalar amplitude",
            symbol="A_crit",
            value=1.062,
            value_expr="1.062 (Phase 6B locked)",
            sectors=["macro_scalar_memory"],
            authority_class="inherited",
            fixed_by="Phase 6B numerical locking",
            current_role="Amplitude of scalar overshoot at horizon; sets Component A strength",
            structurally_central=True,
            future_reduction_path="None needed; locked by Phase 6B",
        ),
        ParameterEntry(
            name="Macro energy density prefactor",
            symbol="rho_eq_coeff",
            value=0.5 ** 2 / (2 * 1.5),
            value_expr="M^2 / (2*tau^2) = 1/12",
            sectors=["macro_scalar_memory"],
            authority_class="derived",
            fixed_by="Derived from M_ext and tau",
            current_role="Prefactor in eps_macro = rho_eq_coeff / r^4",
            structurally_central=True,
            future_reduction_path="None needed; derived",
        ),
        ParameterEntry(
            name="Mass integral coefficient",
            symbol="mass_coeff",
            value=math.pi / 3.0,
            value_expr="pi/3 = 2*pi*M^2/tau^2",
            sectors=["macro_scalar_memory", "gravitational"],
            authority_class="derived",
            fixed_by="Derived from M_ext and tau via mass integral",
            current_role="Coefficient in m(r) = M + mass_coeff*(1/r - 1/R_ext)",
            structurally_central=True,
            future_reduction_path="None needed; derived",
        ),
        # --- Defect / source sector ---
        ParameterEntry(
            name="Source charge",
            symbol="Q",
            value=None,
            value_expr="Q = n * eta, n in Z (principled, not uniquely derived)",
            sectors=["defect_triplet"],
            authority_class="matched",
            fixed_by="D12: topological winding number in O(3) hedgehog; matched to Phase 6C requirement",
            current_role="Generates Component B ~ 1/r^2 support via defect energy",
            structurally_central=True,
            future_reduction_path="Derive O(3) sector necessity from deeper GRUT structure; derive n=1 selection",
            notes="D12 classification: principled_and_strongly_constrained",
        ),
        ParameterEntry(
            name="Defect VEV",
            symbol="eta",
            value=1.0 / math.sqrt(8 * math.pi),
            value_expr="1/sqrt(8*pi) ~ 0.1995; eta^2 = 1/(8*pi)",
            sectors=["defect_triplet"],
            authority_class="matched",
            fixed_by="Phase 6C coefficient requirement: Component B coefficient = 1/(8*pi)",
            current_role="Sets defect energy density scale; eta^2 = COMP_B_COEFF",
            structurally_central=True,
            future_reduction_path="Derive eta from GRUT-native structure or renormalization constraint",
            notes="Value set by matching, not predicted",
        ),
        ParameterEntry(
            name="Defect self-coupling",
            symbol="lambda",
            value=8 * math.pi,
            value_expr="8*pi ~ 25.133 (default; scanned over [5, 200])",
            sectors=["defect_triplet"],
            authority_class="open",
            fixed_by="Not fixed; default value chosen for lambda*eta^2 = 1; scanned in D9/D11",
            current_role="Controls defect profile steepness f(r); affects f_min and metric correction",
            structurally_central=True,
            future_reduction_path="Derive from renormalization or stability argument; "
                                  "narrow scan range via observational constraints",
        ),
        ParameterEntry(
            name="Component B coefficient",
            symbol="comp_B_coeff",
            value=1.0 / (8 * math.pi),
            value_expr="1/(8*pi) = eta^2",
            sectors=["defect_triplet", "gravitational"],
            authority_class="matched",
            fixed_by="Phase 6C requirement for Component B energy density",
            current_role="Coefficient in eps_B = comp_B_coeff / r^2",
            structurally_central=True,
            future_reduction_path="Would be derived if eta is derived",
        ),
        # --- Curvature trigger sector ---
        ParameterEntry(
            name="Curvature coupling",
            symbol="xi",
            value=1.0,
            value_expr="1.0 (default; scanned in D4/D6)",
            sectors=["curvature_trigger"],
            authority_class="open",
            fixed_by="Not fixed; default xi=1; scanned",
            current_role="Couples Kretschner scalar to defect activation; controls trigger threshold",
            structurally_central=False,
            future_reduction_path="Derive from conformal coupling argument or renormalization",
        ),
        ParameterEntry(
            name="Kretschner coefficient",
            symbol="K_coeff",
            value=48.0 * 0.25,
            value_expr="48*M^2 = 12.0 (Schwarzschild)",
            sectors=["curvature_trigger", "gravitational"],
            authority_class="inherited",
            fixed_by="Schwarzschild geometry: K = 48*M^2/r^6",
            current_role="Sets curvature scale for trigger activation",
            structurally_central=True,
            future_reduction_path="None needed; inherited from GR",
        ),
        # --- Portal interaction sector ---
        ParameterEntry(
            name="Portal coupling",
            symbol="g_p",
            value=1.0,
            value_expr="1.0 (default; scanned over [0, 2])",
            sectors=["portal_interaction", "macro_scalar_memory", "defect_triplet"],
            authority_class="open",
            fixed_by="Not fixed; scanned in D9/D11; D11 shows negligible effect in tested regime",
            current_role="Strength of Phi^2 * |vec_Phi|^2 interaction; cross-sector coupling",
            structurally_central=False,
            future_reduction_path="Derive from renormalization or matching to observational constraint; "
                                  "D11 suggests may be negligible on physical domain",
            notes="D11: portal coupling negligible in tested regime",
        ),
        # --- Cosmology sector ---
        ParameterEntry(
            name="Hubble constant (GRUT)",
            symbol="H_0",
            value=None,
            value_expr="Framework-dependent; not directly constrained by strong-field program",
            sectors=["cosmology"],
            authority_class="phenomenological",
            fixed_by="Cosmological observations; GRUT modifies interpretation via memory kernel",
            current_role="Background expansion rate; GRUT proposes memory-kernel correction to tension",
            structurally_central=False,
            future_reduction_path="Determine whether memory-kernel cosmology survives precision tests",
        ),
        ParameterEntry(
            name="Memory kernel cosmology scale",
            symbol="tau_cosmo",
            value=None,
            value_expr="Not identified with strong-field tau in current canon",
            sectors=["cosmology", "macro_scalar_memory"],
            authority_class="phenomenological",
            fixed_by="Cosmological sector fitting; not derived from strong-field program",
            current_role="Controls late-time memory effects in cosmological expansion",
            structurally_central=False,
            future_reduction_path="Unify with strong-field tau or derive separate scale from action",
        ),
        # --- Source / amplitude ---
        ParameterEntry(
            name="Source profile",
            symbol="X(r)",
            value=None,
            value_expr="X(r) = M / r^2 (frozen classical source)",
            sectors=["macro_scalar_memory", "gravitational"],
            authority_class="inherited",
            fixed_by="Classical Schwarzschild interior; frozen in D11",
            current_role="Source term in macro field equation; drives Phi(r)",
            structurally_central=True,
            future_reduction_path="Promote to dynamical source in future phase",
            notes="Frozen throughout D1-D12; unfreezing is a D13+ task",
        ),
        # --- BVP domain parameters ---
        ParameterEntry(
            name="BVP inner radius",
            symbol="r_min",
            value=0.01,
            value_expr="0.01",
            sectors=["defect_triplet", "macro_scalar_memory"],
            authority_class="inherited",
            fixed_by="Numerical convenience; well inside R_eq",
            current_role="Inner boundary for BVP solve; f(r_min) = 0",
            structurally_central=False,
            future_reduction_path="None needed; numerical parameter",
        ),
        ParameterEntry(
            name="BVP outer radius",
            symbol="r_max",
            value=5.0,
            value_expr="5.0",
            sectors=["defect_triplet", "macro_scalar_memory"],
            authority_class="inherited",
            fixed_by="Numerical convenience; well outside R_ext",
            current_role="Outer boundary for BVP solve; f(r_max) = 1",
            structurally_central=False,
            future_reduction_path="None needed; numerical parameter",
        ),
        # --- Winding number ---
        ParameterEntry(
            name="Winding number",
            symbol="n",
            value=1.0,
            value_expr="n = 1 (assumed; pi_2(S^2) = Z)",
            sectors=["defect_triplet"],
            authority_class="phenomenological",
            fixed_by="Assumed minimal topological charge; not derived from stability",
            current_role="Sets Q = n * eta; n=1 gives minimal-energy hedgehog",
            structurally_central=True,
            future_reduction_path="Derive n=1 selection from stability or energetic argument",
        ),
    ]

    pam = ParameterAuthorityMap(entries=entries)
    return pam


# ===================================================================
# Cross-Sector Dependency Map
# ===================================================================

def build_cross_sector_map() -> CrossSectorMap:
    """Build the cross-sector dependency map.

    Describes how the 7 major GRUT sectors depend on and export
    structure to each other.
    """
    deps = [
        SectorDependency(
            sector="gravitational",
            depends_on=[],
            inherited_structures=["GR field equations", "Schwarzschild solution", "Kretschner scalar"],
            exported_structures=["metric g_ab", "curvature invariants", "R_S, M, R_eq"],
            current_status="LOCKED",
        ),
        SectorDependency(
            sector="macro_scalar_memory",
            depends_on=["gravitational"],
            inherited_structures=["background metric", "source profile X(r) = M/r^2", "alpha_vac, R_eq, tau"],
            exported_structures=[
                "macro field Phi(r)", "Component A energy density ~ 1/r^4",
                "mass function m(r)", "A_crit amplitude",
            ],
            current_status="STRONGLY_SUPPORTED",
        ),
        SectorDependency(
            sector="defect_triplet",
            depends_on=["gravitational"],
            inherited_structures=["background metric (flat-space BVP in current implementation)"],
            exported_structures=[
                "defect profile f(r)", "Component B energy density ~ 1/r^2",
                "topological charge Q = n*eta", "hedgehog configuration",
            ],
            current_status="PRINCIPLED_AND_STRONGLY_CONSTRAINED",
        ),
        SectorDependency(
            sector="curvature_trigger",
            depends_on=["gravitational", "defect_triplet"],
            inherited_structures=["Kretschner scalar K(r)", "defect field vec_Phi"],
            exported_structures=["trigger threshold", "activation profile", "Kretschner family selection"],
            current_status="FRAMEWORK_CONDITIONAL",
        ),
        SectorDependency(
            sector="portal_interaction",
            depends_on=["macro_scalar_memory", "defect_triplet"],
            inherited_structures=["macro field Phi(r)", "defect field vec_Phi"],
            exported_structures=["cross-sector coupling g_p Phi^2 |vec_Phi|^2"],
            current_status="STRONGLY_SUPPORTED",
            # D11 shows it converges but is negligible in tested regime
        ),
        SectorDependency(
            sector="cosmology",
            depends_on=["gravitational", "macro_scalar_memory"],
            inherited_structures=["memory kernel structure", "background expansion equations"],
            exported_structures=["Hubble tension modification", "late-time memory effects"],
            current_status="PROVISIONAL",
        ),
        SectorDependency(
            sector="observational",
            depends_on=[
                "gravitational", "macro_scalar_memory",
                "defect_triplet", "curvature_trigger",
            ],
            inherited_structures=[
                "modified interior metric", "mass function", "defect profile",
                "trigger threshold", "curvature invariants",
            ],
            exported_structures=["QNM predictions", "tidal deformability", "lensing signatures"],
            current_status="OPEN",
        ),
    ]

    return CrossSectorMap(
        dependencies=deps,
        minimal_backbone=[
            "gravitational",
            "macro_scalar_memory",
            "defect_triplet",
        ],
        backbone_summary=(
            "The minimal GRUT backbone consists of three sectors: "
            "(1) gravitational (GR + Schwarzschild background), "
            "(2) macro scalar memory (Phi(r) driven by X(r) = M/r^2, producing Component A), and "
            "(3) defect triplet (O(3) hedgehog with topological charge Q = n*eta, producing Component B). "
            "The curvature trigger and portal interaction are structurally present in the D8 action "
            "but contribute negligibly on the physical test domain [R_eq, R_ext] in D11. "
            "The cosmology sector shares the memory-kernel structure but is not yet "
            "integrated at the level of a single action principle with the strong-field program. "
            "The observational sector is downstream of all others and currently defines a roadmap, "
            "not tested predictions."
        ),
        unity_argument=(
            "GRUT is best described as one theory with multiple limits rather than a modular assembly, "
            "because: (1) the gravitational sector provides the universal background for all others; "
            "(2) the macro and defect sectors are unified through the D8 coupled action "
            "S_total = S_grav + S_macro + S_defect + S_trigger + S_portal; "
            "(3) the cosmology sector inherits the same memory-kernel structure that defines "
            "the macro sector; (4) the observational sector is determined by the interior solution, "
            "not independently specified. However, the cosmology-to-strong-field integration is not yet "
            "derived from a single cosmological+interior action, and the trigger sector's coupling constant "
            "xi remains open. The theory is therefore unified in architecture but not yet in all parameters."
        ),
    )


# ===================================================================
# Observable Roadmap
# ===================================================================

def build_observable_roadmap() -> ObservableRoadmap:
    """Build the empirical/observational roadmap.

    Each entry describes a candidate observable, what GRUT predicts,
    and what would count as support, tension, or falsification.

    This is a roadmap, not evidence of validation.
    """
    entries = [
        # --- Compact object interior / structure ---
        ObservableEntry(
            observable="Compact object mass-radius relation",
            sectors_probed=["gravitational", "macro_scalar_memory", "defect_triplet"],
            relevant_parameters=["M_ext", "tau", "eta", "lambda", "alpha_vac"],
            predicted_effect_type="mass_radius_modification",
            predicted_effect_description=(
                "GRUT interior regularity replaces the Schwarzschild singularity with a "
                "finite-density core. The mass function m(r) acquires a correction "
                "m(r) = M + (pi/3)*(1/r - 1/R_ext) inside R_ext. This modifies the "
                "effective compactness and could produce observable deviations in "
                "mass-radius relations for ultracompact objects, if such objects exist."
            ),
            support_criterion=(
                "Detection of compact objects with compactness ratios deviating from "
                "classical BH predictions in a direction consistent with interior regularity"
            ),
            tension_criterion=(
                "Precision measurements of compact object properties fully consistent "
                "with classical Kerr to within measurement uncertainty"
            ),
            falsification_criterion=(
                "Observation of singularity-consistent signatures (e.g., infinite tidal forces "
                "at horizon approach) that exclude any regular interior"
            ),
            observational_class="compact_object_structure",
        ),
        ObservableEntry(
            observable="Interior density profile signatures",
            sectors_probed=["macro_scalar_memory", "defect_triplet"],
            relevant_parameters=["tau", "eta", "lambda", "A_crit"],
            predicted_effect_type="deformation",
            predicted_effect_description=(
                "The dual-sector energy density eps(r) = Component_A/r^4 + Component_B/r^2 "
                "produces a specific radial profile that differs from both vacuum Schwarzschild "
                "and simple fluid interiors. The crossover radius where defect energy overtakes "
                "macro energy (~1.67 R_S) is a structural prediction."
            ),
            support_criterion=(
                "Any indirect evidence for dual-component interior energy profiles "
                "with the predicted crossover structure"
            ),
            tension_criterion=(
                "Evidence for single-component interior energy or profiles inconsistent "
                "with 1/r^4 + 1/r^2 decomposition"
            ),
            falsification_criterion=(
                "Direct measurement excluding any interior matter/energy content"
            ),
            observational_class="compact_object_structure",
        ),
        # --- Gravitational wave observables ---
        ObservableEntry(
            observable="Quasinormal mode spectrum",
            sectors_probed=["gravitational", "macro_scalar_memory", "defect_triplet"],
            relevant_parameters=["M_ext", "tau", "eta", "lambda"],
            predicted_effect_type="spectral_shift",
            predicted_effect_description=(
                "GRUT's modified interior metric changes the effective potential for "
                "perturbations, which modifies quasinormal mode frequencies and damping times. "
                "The direction of the shift depends on the balance between Component A "
                "and Component B contributions to the interior metric."
            ),
            support_criterion=(
                "QNM frequency shifts from classical Schwarzschild/Kerr predictions "
                "in a direction and magnitude consistent with GRUT interior corrections"
            ),
            tension_criterion=(
                "QNM measurements precisely matching classical predictions to within "
                "the sensitivity threshold of GRUT corrections"
            ),
            falsification_criterion=(
                "QNM shifts in the opposite direction from GRUT predictions, or "
                "complete absence of any deviation at sensitivity levels that should "
                "resolve GRUT effects"
            ),
            observational_class="gravitational_wave",
        ),
        ObservableEntry(
            observable="Ringdown echoes",
            sectors_probed=["gravitational", "macro_scalar_memory"],
            relevant_parameters=["M_ext", "tau", "R_eq"],
            predicted_effect_type="family_of_behaviors",
            predicted_effect_description=(
                "If the GRUT interior produces an effective cavity between R_eq and R_S, "
                "post-merger ringdown may exhibit echo signatures at delay times set by "
                "the light-crossing time of the interior region. The echo amplitude "
                "depends on the reflectivity of the effective potential barrier."
            ),
            support_criterion=(
                "Detection of post-ringdown echoes with timing consistent with "
                "GRUT interior structure"
            ),
            tension_criterion=(
                "Non-detection of echoes at sensitivity levels sufficient to probe "
                "GRUT-scale interior structure"
            ),
            falsification_criterion=(
                "Definitive exclusion of any post-ringdown structure at relevant timescales "
                "across multiple events"
            ),
            observational_class="gravitational_wave",
        ),
        ObservableEntry(
            observable="Tidal deformability / Love numbers",
            sectors_probed=["gravitational", "macro_scalar_memory", "defect_triplet"],
            relevant_parameters=["M_ext", "tau", "eta", "lambda"],
            predicted_effect_type="tidal_modification",
            predicted_effect_description=(
                "Classical black holes have zero tidal Love numbers. GRUT's regular interior "
                "with non-zero energy density generically produces non-zero Love numbers. "
                "The magnitude depends on the interior equation of state implied by the "
                "dual-sector energy decomposition."
            ),
            support_criterion=(
                "Measurement of non-zero Love numbers for compact objects in the "
                "BH mass range, consistent with GRUT interior EOS"
            ),
            tension_criterion=(
                "Love number measurements consistent with zero to within uncertainties "
                "that probe GRUT correction magnitudes"
            ),
            falsification_criterion=(
                "Precision measurement of exactly zero Love numbers for BH-mass objects, "
                "excluding any interior matter content"
            ),
            observational_class="gravitational_wave",
        ),
        # --- Strong-field lensing ---
        ObservableEntry(
            observable="Photon ring fine structure",
            sectors_probed=["gravitational", "macro_scalar_memory"],
            relevant_parameters=["M_ext", "tau", "A_crit"],
            predicted_effect_type="deformation",
            predicted_effect_description=(
                "GRUT's modified metric near the photon sphere could produce "
                "deviations in the photon ring structure visible to space-based "
                "VLBI or next-generation EHT observations. The effect is a "
                "small deformation of the critical impact parameter."
            ),
            support_criterion=(
                "Photon ring substructure deviations from Kerr predictions "
                "in a direction consistent with GRUT metric modifications"
            ),
            tension_criterion=(
                "Photon ring observations fully consistent with Kerr to "
                "relevant precision"
            ),
            falsification_criterion=(
                "Photon ring measurements excluding the class of metric "
                "modifications that GRUT produces"
            ),
            observational_class="strong_field_lensing",
        ),
        ObservableEntry(
            observable="Shadow size and shape",
            sectors_probed=["gravitational"],
            relevant_parameters=["M_ext", "R_eq"],
            predicted_effect_type="deformation",
            predicted_effect_description=(
                "The black hole shadow boundary depends on the metric near "
                "the photon sphere. GRUT modifications to the interior metric "
                "could propagate to the shadow boundary if they extend to "
                "r ~ 3M. Current strong-field program tests on [R_eq, R_ext] = "
                "[1/3, 2.0] cover this region."
            ),
            support_criterion=(
                "Shadow size/shape deviations from Kerr at percent level, "
                "consistent with GRUT metric"
            ),
            tension_criterion=(
                "Shadow measurements consistent with Kerr to sub-percent precision"
            ),
            falsification_criterion=(
                "Shadow measurements excluding any regular-interior modification"
            ),
            observational_class="strong_field_lensing",
        ),
        # --- Cosmology-linked ---
        ObservableEntry(
            observable="Late-time expansion memory correction",
            sectors_probed=["cosmology", "macro_scalar_memory"],
            relevant_parameters=["tau_cosmo", "H_0"],
            predicted_effect_type="scaling",
            predicted_effect_description=(
                "If the GRUT memory kernel applies at cosmological scales, it "
                "modifies the late-time expansion history in a way that could "
                "address the Hubble tension. The modification is a scale-dependent "
                "correction to the effective dark energy equation of state."
            ),
            support_criterion=(
                "Resolution of Hubble tension via memory-kernel correction "
                "with tau_cosmo in a physically reasonable range"
            ),
            tension_criterion=(
                "Hubble tension resolution requiring tau_cosmo values "
                "inconsistent with strong-field program"
            ),
            falsification_criterion=(
                "Definitive resolution of Hubble tension by non-GRUT mechanism, "
                "or exclusion of memory-kernel cosmology class"
            ),
            observational_class="cosmology",
            notes="Cosmology sector not yet integrated with strong-field action",
        ),
        # --- Trigger threshold ---
        ObservableEntry(
            observable="Curvature threshold for defect activation",
            sectors_probed=["curvature_trigger", "gravitational"],
            relevant_parameters=["xi", "K_coeff", "eta"],
            predicted_effect_type="threshold",
            predicted_effect_description=(
                "GRUT predicts that the defect sector activates only above a "
                "Kretschner curvature threshold set by xi and eta. This implies "
                "that objects below a certain compactness should not exhibit "
                "defect-sector effects. The threshold creates a mass/compactness "
                "boundary for GRUT interior modifications."
            ),
            support_criterion=(
                "Evidence for a compactness threshold below which compact objects "
                "behave classically and above which they show interior modifications"
            ),
            tension_criterion=(
                "Evidence for interior modifications at arbitrarily low curvatures, "
                "or no modifications at any curvature"
            ),
            falsification_criterion=(
                "Measurement of interior properties inconsistent with any "
                "curvature-triggered activation mechanism"
            ),
            observational_class="compact_object_structure",
        ),
    ]

    return ObservableRoadmap(entries=entries)


# ===================================================================
# Canon Hierarchy
# ===================================================================

def build_canon_hierarchy() -> CanonHierarchy:
    """Build the theory-wide canon hierarchy table.

    Classifies every major claim/sector by current status, basis,
    and remaining caveats.
    """
    entries = [
        CanonHierarchyEntry(
            claim_or_sector="Classical GR frontier closure",
            current_status="LOCKED",
            basis="Standard GR; Schwarzschild solution; geometric units",
            caveat="None within tested scope",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Vacuum memory-kernel structure (alpha_vac = 1/3)",
            current_status="LOCKED",
            basis="Phase 5 vacuum sector locking",
            caveat="Tested on Schwarzschild background only",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Component A recovery (macro scalar, ~1/r^4)",
            current_status="STRONGLY_SUPPORTED",
            basis="Phases 4, 6B, D4; scalar amplitude A_crit = 1.062 locked",
            caveat="Shape exponent -2.89 vs target -4.0 (D4 SUGGESTIVE, not exact)",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Component B recovery (defect, ~1/r^2)",
            current_status="STRONGLY_SUPPORTED",
            basis="Phases 6C, D1-D2; hedgehog BVP numerically viable",
            caveat="Coefficient matched (eta), not predicted",
        ),
        CanonHierarchyEntry(
            claim_or_sector="O(3) scalar triplet embedding",
            current_status="LOCKED",
            basis="D3: O(3) embedding most promising among candidates tested",
            caveat="O(3) sector is minimal extension, not derived from GRUT-native structure",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Companion dual-sector architecture",
            current_status="STRONGLY_SUPPORTED",
            basis="D6-D7: companion architecture viable; D11 exact closure confirms",
            caveat="Tested on Schwarzschild background with frozen source only",
        ),
        CanonHierarchyEntry(
            claim_or_sector="D8 coupled action S_total",
            current_status="LOCKED",
            basis="D8: action-derived; D7 channels largely recovered from action",
            caveat="Portal uniqueness scoped to non-derivative polynomial renormalizable Z2 x O(3)-invariant",
        ),
        CanonHierarchyEntry(
            claim_or_sector="D9 self-consistent coupling (proxy)",
            current_status="PROXY_DEPENDENT",
            basis="D9: Picard iteration converges; metric positive on [R_eq, R_ext]",
            caveat="Uses macro-amplitude proxy A_eff(r)^2; D11 shows broadly valid but not exact",
        ),
        CanonHierarchyEntry(
            claim_or_sector="D10 Kretschner trigger family",
            current_status="FRAMEWORK_CONDITIONAL",
            basis="D10: Kretschner family best supported within D8/D9 framework",
            caveat="Conditional on D8/D9 approximations; xi remains open",
        ),
        CanonHierarchyEntry(
            claim_or_sector="D11 exact two-field closure",
            current_status="STRONGLY_SUPPORTED",
            basis="D11: exact coupled BVP converges; companion architecture survives",
            caveat="Boundary-sensitive on extended domain; portal negligible in tested regime",
        ),
        CanonHierarchyEntry(
            claim_or_sector="D12 Q source ontology",
            current_status="PRINCIPLED_AND_STRONGLY_CONSTRAINED",
            basis="D12: topological winding Q = n*eta best supported; 4/5 requirements strong",
            caveat="O(3) sector not derived from GRUT; eta matched not predicted; n=1 assumed",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Metric positivity on physical domain",
            current_status="STRONGLY_SUPPORTED",
            basis="D9/D11: g_tt > 0 on [R_eq, R_ext] for tested lambda set",
            caveat="Tested lambda in {5, 10, 25, 50, 100, 200}; not proven for all lambda",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Trigger-family classification",
            current_status="FRAMEWORK_CONDITIONAL",
            basis="D10: Kretschner best within tested families",
            caveat="Other trigger families not exhaustively tested",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Empirical/observational program",
            current_status="OPEN",
            basis="Bridge document: roadmap defined; no data confrontation yet",
            caveat="All observables are predictions, not confirmations",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Cosmology sector integration",
            current_status="PROVISIONAL",
            basis="Memory-kernel cosmology shares structural elements with strong-field sector",
            caveat="Not yet derived from single action; tau_cosmo not identified with tau",
        ),
        CanonHierarchyEntry(
            claim_or_sector="Final ToE status",
            current_status="OPEN",
            basis="Architecture closed; source ontology principled; empirical roadmap defined",
            caveat="Multiple open parameters; no observational confirmation; "
                   "O(3) not derived; cosmology not integrated at action level",
        ),
    ]

    return CanonHierarchy(entries=entries)


# ===================================================================
# Bridge Gaps
# ===================================================================

def identify_bridge_gaps() -> List[BridgeGap]:
    """Identify remaining bridge gaps before final ToE language."""
    return [
        BridgeGap(
            gap="O(3) sector derivation from GRUT-native structure",
            severity="critical",
            sector="defect_triplet",
            notes="The O(3) triplet is a minimal extension, not a consequence of "
                  "GRUT's scalar-memory structure. Deriving its necessity would "
                  "upgrade Q from principled to derived.",
        ),
        BridgeGap(
            gap="Prediction of eta, lambda, g_p from deeper structure",
            severity="significant",
            sector="defect_triplet",
            notes="eta is matched to Phase 6C; lambda is scanned; g_p is scanned "
                  "and negligible in D11. Predicting any of these from renormalization "
                  "or consistency would strengthen the theory.",
        ),
        BridgeGap(
            gap="Empirical confrontation with observational data",
            severity="critical",
            sector="observational",
            notes="No GRUT prediction has been confronted with data. The roadmap "
                  "defines what to look for but has not been tested.",
        ),
        BridgeGap(
            gap="Cosmology-to-strong-field action-level integration",
            severity="significant",
            sector="cosmology",
            notes="The cosmology sector shares memory-kernel structure but is not yet "
                  "derived from the same action as the strong-field program.",
        ),
        BridgeGap(
            gap="Winding number selection (n=1)",
            severity="minor",
            sector="defect_triplet",
            notes="n=1 is assumed as the minimal-energy hedgehog. A stability "
                  "argument would close this gap.",
        ),
        BridgeGap(
            gap="Non-Schwarzschild backgrounds (Kerr, RN, cosmological)",
            severity="significant",
            sector="gravitational",
            notes="The entire D-program is tested on Schwarzschild only. Extension "
                  "to rotating or charged backgrounds is needed for astrophysical realism.",
        ),
        BridgeGap(
            gap="Dynamical source promotion",
            severity="minor",
            sector="macro_scalar_memory",
            notes="X(r) = M/r^2 is frozen throughout D1-D12. A fully dynamical "
                  "source would test whether the interior solution is self-consistent.",
        ),
        BridgeGap(
            gap="Linear stability of self-consistent interior",
            severity="significant",
            sector="macro_scalar_memory",
            notes="The static interior solution has not been tested for stability "
                  "against linear perturbations.",
        ),
    ]


# ===================================================================
# Bridge Classification
# ===================================================================

def classify_bridge(
    canon_hierarchy: CanonHierarchy,
    bridge_gaps: List[BridgeGap],
) -> BridgeClassification:
    """Classify the bridge status from explicit criteria.

    Classification logic (deterministic, no hidden weights):
    - Count LOCKED + STRONGLY_SUPPORTED + PRINCIPLED entries
    - Count OPEN entries
    - Count critical gaps
    - Apply threshold rules
    """
    locked = sum(
        1 for e in canon_hierarchy.entries
        if e.current_status == "LOCKED"
    )
    supported = sum(
        1 for e in canon_hierarchy.entries
        if e.current_status in (
            "STRONGLY_SUPPORTED",
            "PRINCIPLED_AND_STRONGLY_CONSTRAINED",
        )
    )
    open_entries = sum(
        1 for e in canon_hierarchy.entries
        if e.current_status == "OPEN"
    )
    critical_gaps = sum(
        1 for g in bridge_gaps if g.severity == "critical"
    )

    total = len(canon_hierarchy.entries)
    strong_fraction = (locked + supported) / total if total > 0 else 0.0

    # Deterministic classification rules:
    # 1. If critical gaps >= 2: not yet enough
    # 2. If critical gaps == 1 and strong_fraction >= 0.5: strong but missing one bridge
    # 3. If critical gaps == 0 and strong_fraction >= 0.7: sufficient
    # 4. Otherwise: informative but not enough

    if critical_gaps >= 2:
        classification = "strong_but_missing_one_major_bridge"
        justification = (
            f"The theory has {locked} locked and {supported} strongly supported entries "
            f"out of {total} total ({strong_fraction:.0%}), but {critical_gaps} critical "
            f"gaps remain: {', '.join(g.gap for g in bridge_gaps if g.severity == 'critical')}. "
            f"The architecture is strong but the critical gaps prevent final ToE synthesis."
        )
    elif critical_gaps == 1 and strong_fraction >= 0.5:
        classification = "strong_but_missing_one_major_bridge"
        justification = (
            f"The theory has {locked} locked and {supported} strongly supported entries "
            f"out of {total} total ({strong_fraction:.0%}), with exactly one critical "
            f"gap: {next(g.gap for g in bridge_gaps if g.severity == 'critical')}. "
            f"The architecture is strong but this single gap prevents final synthesis."
        )
    elif critical_gaps == 0 and strong_fraction >= 0.7:
        classification = "sufficient_for_final_toe_synthesis"
        justification = (
            f"All critical gaps resolved. {locked} locked and {supported} strongly supported "
            f"entries out of {total} total ({strong_fraction:.0%})."
        )
    else:
        classification = "informative_but_not_yet_enough_for_final_toe_presentation"
        justification = (
            f"The theory has {locked} locked and {supported} strongly supported entries "
            f"out of {total} total ({strong_fraction:.0%}), with {critical_gaps} critical gaps."
        )

    return BridgeClassification(
        classification=classification,
        justification=justification,
        locked_count=locked,
        supported_count=supported,
        open_count=open_entries,
        critical_gaps=critical_gaps,
    )


# ===================================================================
# Omni-ToE v3 Claims
# ===================================================================

def determine_omni_toe_claims(
    bridge_classification: BridgeClassification,
) -> tuple:
    """Determine what Omni-ToE v3 may and may not claim.

    Returns (may_claim: list[str], may_not_claim: list[str]).
    """
    may_claim = [
        "GRUT is a unified architecture with a defined strong-field interior "
        "solution, a principled source ontology, and a falsifiability roadmap.",

        "The strong-field interior program (D1-D12) closes the classical "
        "vacuum/source frontier within tested scope on a Schwarzschild background.",

        "The Companion dual-sector architecture survives exact two-field treatment "
        "(D11) on the physical test domain [R_eq, R_ext] = [1/3, 2.0].",

        "The source charge Q is principled and strongly constrained as a topological "
        "winding number Q = n*eta in the O(3) hedgehog sector (D12).",

        "The theory has a defined parameter authority map distinguishing inherited, "
        "derived, matched, phenomenological, and open quantities.",

        "The theory defines explicit observational targets (QNMs, Love numbers, "
        "photon ring, echoes, tidal deformability) with stated support, tension, "
        "and falsification criteria.",

        "The major GRUT sectors (gravitational, macro, defect, trigger, portal) "
        "are connected through the D8 coupled action and share explicit structure.",
    ]

    may_not_claim = [
        "GRUT has been observationally confirmed or tested against data.",

        "All parameters are predicted from first principles. eta is matched, "
        "lambda and g_p are scanned, xi is open.",

        "The O(3) defect sector is derived from GRUT-native structure. "
        "It remains a minimal extension.",

        "The cosmology sector is integrated with the strong-field program "
        "at the action level.",

        "The interior solution has been tested on rotating (Kerr) or "
        "charged (Reissner-Nordstrom) backgrounds.",

        "The static interior solution has been demonstrated to be linearly stable.",

        "GRUT constitutes a complete, final theory of everything in the "
        "traditional sense. Multiple open parameters and untested sectors remain.",

        "The winding number n=1 is derived rather than assumed.",
    ]

    return may_claim, may_not_claim


# ===================================================================
# Main computation
# ===================================================================

def compute_bridge_result() -> BridgeResult:
    """Compute the full bridge phenomenology/integration result.

    This is the top-level entry point. Returns a BridgeResult
    containing all sub-results.
    """
    pam = build_parameter_authority_map()
    csm = build_cross_sector_map()
    roadmap = build_observable_roadmap()
    hierarchy = build_canon_hierarchy()
    gaps = identify_bridge_gaps()
    classification = classify_bridge(hierarchy, gaps)
    may_claim, may_not_claim = determine_omni_toe_claims(classification)

    return BridgeResult(
        valid=True,
        parameter_authority_map=pam,
        cross_sector_map=csm,
        observable_roadmap=roadmap,
        canon_hierarchy=hierarchy,
        bridge_gaps=gaps,
        bridge_classification=classification,
        omni_toe_v3_may_claim=may_claim,
        omni_toe_v3_may_not_claim=may_not_claim,
    )


# ===================================================================
# Export
# ===================================================================

def bridge_result_to_dict(result: BridgeResult) -> Dict[str, Any]:
    """Convert BridgeResult to a JSON-serializable dictionary."""
    return asdict(result)


def export_bridge_result_json(result: BridgeResult, path: str) -> None:
    """Export BridgeResult to a JSON file."""
    d = bridge_result_to_dict(result)
    with open(path, "w") as f:
        json.dump(d, f, indent=2, default=str)


# ===================================================================
# Module-level constants for external inspection
# ===================================================================

ASSUMPTIONS = [
    "Schwarzschild background throughout D1-D12",
    "Static spherically symmetric interior",
    "Frozen classical source X(r) = M/r^2",
    "O(3) hedgehog ansatz for defect sector",
    "Flat-space BVP for defect profile (no gravitational back-reaction on defect equation)",
    "Tested lambda range: {5, 10, 25, 50, 100, 200}",
    "Tested g_p range: {0, 0.1, 0.5, 1.0, 2.0}",
    "Boundary conditions: f(r_min)=0, f(r_max)=1, Phi(r_min)=M/r_min^2, Phi(r_max)=M/r_max^2",
]

NONCLAIMS = [
    "This bridge document does not claim observational confirmation of any GRUT prediction.",
    "This bridge document does not claim that all parameters are derived from first principles.",
    "This bridge document does not claim that the O(3) sector follows from GRUT-native structure.",
    "This bridge document does not claim that the cosmology sector is action-integrated with strong-field.",
    "This bridge document does not claim final ToE status for GRUT.",
    "This bridge document does not claim linear stability of the interior solution.",
    "This bridge document does not flatten open parameters into derived ones.",
]
