"""Route B (Galley doubled-field) pre-projection Component B test.

Tests whether full pre-projection Route B — i.e. the doubled-field /
doubled-metric sector BEFORE the physical-limit projection Phi_1 = Phi_2
and g_1 = g_2 — can generate the missing 1/r^2-type support identified
in Phase 6C.

PRINCIPAL RESULTS (three-part answer):

  A. Post-projection Route B cannot solve Component B — it collapses to
     Route C-like 1/r^4 support (identical standard scalar T^Phi).

  B. The already-computed pre-projection sectors do not supply a clean
     physical 1/r^2 support — they are ghost-driven, IC-dependent, or
     projection-sensitive.

  C. The remaining g_- / doubled-metric sector is still the unresolved
     residue — its energy density has not been computed in closed form,
     so a full Route B no-go cannot be returned.  This phase localizes
     the remaining unknown.

UNCOMPUTED-SECTOR BARRIER:
  This module does NOT compute the pre-projection g_- energy density or
  the full doubled-metric variation.  Therefore it cannot return a full
  Route B no-go.  It can only classify the already-computed sectors and
  localize the remaining unknown to the g_- / doubled-metric channel.

CLASSIFICATION:
  route_b_post_projection_insufficient__preprojection_unresolved

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


# ================================================================
# Constants — canonical GRUT parameters (from metric_deficit.py)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ_OVER_RS = ALPHA_VAC
R_EQ = R_S * R_EQ_OVER_RS           # = 1/3
C_COMPACTNESS = R_S / R_EQ          # = 3
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)  # ~ 1.2247

# Phase 6/6B/6C locked values
PHASE6_F_AT_REQ = -17.71
PHASE6B_A_CRIT_NATURAL = 1.062
MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / (TAU_CANONICAL ** 2)

# Route B specific (post-projection identical to Route C)
A_CRIT = PHASE6B_A_CRIT_NATURAL
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
EPSILON_RC_COEFF = A_CRIT ** 2 * RHO_EQ_COEFF
COMP_B_COEFF = 1.0 / (8.0 * math.pi)

# Route B ghost sector
PHI_GOLDEN = (1.0 + math.sqrt(5.0)) / 2.0  # ~ 1.618


# ================================================================
# Assumptions — explicitly documented
# ================================================================

ROUTE_B_ASSUMPTIONS = [
    "1. Post-projection T^Phi is the standard minimally-coupled scalar "
    "form (from galley_memory.py line 266-311).  In the physical limit "
    "Phi_1 = Phi_2 = Phi, the metric variation of each scalar copy "
    "gives the same T^Phi as Route C.",

    "2. The physical-limit projection is Phi_1 = Phi_2 = Phi, "
    "g^(1) = g^(2) = g, imposed as a constraint (not emergent from "
    "the dynamics).  The Galley EOM are derived BEFORE projection.",

    "3. Phi_- dynamics follow the Galley cross-coupled EOMs "
    "(from galley_truncation.py): dPhi_1/dt = (X - Phi_2)/tau, "
    "dPhi_2/dt = (X - Phi_1)/tau.  In +/- variables: "
    "dPhi_-/dt = Phi_-/tau (exponential growth).",

    "4. The equilibrium profile is Phi_eq = X_eq = M/r^2 "
    "(same as Route C).  At equilibrium the memory field tracks "
    "its source (force balance).",

    "5. The Phi_- spatial profile is determined by initial conditions, "
    "NOT by the geometric source X = M/r^2.  Because Phi_- is sourced "
    "by perturbation ICs rather than geometry, it cannot be treated as "
    "an independently derived geometric Component B carrier.",

    "6. The g_- sector energy density has NOT been computed in closed "
    "form.  The doubled-metric variation delta S / delta g_- has not "
    "been evaluated.  A full Route B no-go would require computing "
    "this sector.",
]


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. Post-projection equivalence with Route C applies ONLY to the "
    "standard minimally-coupled scalar T^Phi form.  Other action "
    "structures could give different post-projection T^Phi.",

    "2. The Phi_- sector analysis uses the Galley cross-coupled EOMs, "
    "NOT independent relaxation.  Independent relaxation gives "
    "Phi_- DECAYING, but that is NOT the Galley dynamics.",

    "3. The CTP boundary condition Phi_-(t_final) = 0 is a FEATURE "
    "of the Galley formalism, not a defect.  It is what enforces "
    "the physical limit at the final time.",

    "4. The ghost-like growth in Phi_- at rate phi/tau is a structural "
    "feature of the Galley CTP encoding of dissipation.  Whether that "
    "feature is merely formal or physically admissible depends on the "
    "projected interpretation and is not settled here.",

    "5. The g_- sector has NOT been evaluated for its energy density "
    "scaling; 1/r^2 CANNOT be ruled out there.  This is the key "
    "unresolved pre-projection channel.  A full Route B no-go would "
    "require computing the g_- energy density in closed form.",

    "6. This assessment does NOT test whether a non-Galley doubled-field "
    "construction could avoid the ghost sector.  Alternative CTP "
    "formalisms may produce different ghost structures.",

    "7. The classification applies to the Galley doubled-field formalism "
    "as implemented in galley_memory.py and galley_truncation.py.  "
    "Other doubled-field constructions are not assessed.",

    "8. S_diss analysis assumes the observer-flow-projected form from "
    "galley_memory.py line 280.  Other dissipative kernel forms "
    "could produce different pre-projection structure.",

    "9. The provisional ranking update is a classification tool, not a "
    "prediction.  Rankings may change with new theoretical input or "
    "computational results, especially if the g_- sector is computed.",

    "10. 'Ghost-contaminated' means wrong-sign kinetic energy.  Whether "
    "this is merely a formal property of the CTP encoding or a physical "
    "pathology depends on the interpretation of the physical-limit "
    "projection and is not resolved here.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class RouteBParams:
    """Parameters for the Route B Component B test."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S
    R_min: float = 0.05
    n_r: int = 500
    A_crit: float = A_CRIT
    phi_golden: float = PHI_GOLDEN


@dataclass
class PostProjectionEquivalence:
    """Post-projection Route B T^Phi = Route C T^Phi = pure 1/r^4.

    In the physical limit, the Galley doubled-field action reduces to
    the standard minimally-coupled scalar action.  The metric variation
    gives the same T^Phi as Route C.  Therefore the post-projection
    energy density is identical to Route C: epsilon = A_crit^2 * M^2 /
    (2 * tau^2 * r^4) — pure 1/r^4, no 1/r^2.
    """
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_post_proj: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_min: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_RC_coeff: float = 0.0
    ratio_at_R_eq: float = 0.0
    ratio_at_r1: float = 0.0
    identical_to_route_c: bool = False
    provides_component_B: bool = False
    shape_mismatch: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class PhiMinusSectorAnalysis:
    """Analysis of the Phi_- (ghost / difference) sector.

    Phi_- = Phi_1 - Phi_2 has wrong-sign kinetic energy, grows
    exponentially at rate 1/tau (simple) or phi/tau (full KG+Galley),
    has IC-dependent spatial profile (not geometric), and is killed
    by the CTP boundary condition at t_final.
    """
    # Growth rates
    simple_growth_rate: float = 0.0       # 1/tau
    full_kg_growth_rate: float = 0.0      # phi/tau
    full_kg_decay_rate: float = 0.0       # 1/(phi*tau)

    # Kinetic sign
    kinetic_sign: int = 0                 # -1 = wrong-sign (ghost)
    is_ghost: bool = False

    # Spatial profile
    spatial_profile_geometric: bool = False  # sourced by X = M/r^2?
    spatial_profile_source: str = ""         # "initial_conditions"

    # CTP boundary
    ctp_kills_at_final_time: bool = False

    # Component B
    provides_component_B: bool = False
    provides_1r2: bool = False

    notes: List[str] = field(default_factory=list)


@dataclass
class GMinusSectorAnalysis:
    """Analysis of the g_- (metric-difference) sector.

    S_grav = S_EH[g_1] - S_EH[g_2] => linearized g_- has wrong-sign
    kinetic energy (gravitational ghost).  g_- = 0 is a consistent
    truncation but is expected unstable.

    CRITICALLY: the g_- energy density has NOT been computed in closed
    form.  This is the key unresolved pre-projection channel.
    """
    # Action structure
    wrong_sign_eh: bool = False
    consistent_truncation: bool = False
    expected_unstable: bool = False

    # Energy density
    energy_density_computed: bool = False
    energy_density_scaling: str = ""    # "uncomputed"

    # Status
    status: str = ""     # "uncomputed_and_projection_sensitive"
    provides_component_B: str = ""  # "undetermined"

    # This is the key statement
    is_key_unresolved_channel: bool = False

    notes: List[str] = field(default_factory=list)


@dataclass
class DissipativeKernelAnalysis:
    """Analysis of the dissipative kernel S_diss contribution.

    S_diss ~ (Phi_1 - Phi_2) * nabla(Phi_1 + Phi_2) / (2*tau)
           = Phi_- * Phi_dot_plus / tau

    In the physical limit: Phi_- = 0 => S_diss = 0 => zero energy density.
    Pre-projection: inherits Phi_- ghost pathology.
    """
    s_diss_at_physical_limit: float = 0.0    # exact 0
    vanishes_in_physical_limit: bool = False
    pre_projection_ghost_coupled: bool = False
    provides_component_B: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class CandidateCarrier:
    """One candidate energy-density carrier for Component B.

    Carriers are distinguished by carrier_type:
      - projected_observable: post-projection physical observable
      - computed_sector: pre-projection sector with known energy density
      - formal_variation_channel: variational placeholder, not yet computed
    """
    carrier_number: int = 0
    name: str = ""
    sector: str = ""
    carrier_type: str = ""       # projected_observable / computed_sector / formal_variation_channel
    scaling_if_known: str = ""   # "1/r^4", "IC-dependent", "0", "uncomputed"
    ghost_status: str = ""       # "none", "wrong_sign_kinetic", "ghost_coupled", "wrong_sign_eh"
    projection_status: str = ""  # "survives", "killed", "projection_sensitive", "uncomputed"
    status_summary: str = ""     # INSUFFICIENT / PATHOLOGICAL / PROJECTION-KILLED / UNCOMPUTED / etc
    provides_component_B: str = ""  # "no", "undetermined"
    notes: List[str] = field(default_factory=list)


@dataclass
class CandidateCarrierCatalog:
    """Catalog of all 5 candidate energy-density carriers."""
    carriers: List[CandidateCarrier] = field(default_factory=list)
    n_carriers: int = 0
    n_physical: int = 0
    n_pathological: int = 0
    n_projection_killed: int = 0
    n_uncomputed: int = 0
    n_projected_observable: int = 0
    n_computed_sector: int = 0
    n_formal_variation_channel: int = 0
    notes: List[str] = field(default_factory=list)


@dataclass
class ObstructionEntry:
    """One obstruction to Component B support from Route B."""
    obstruction_number: int = 0
    name: str = ""
    sector: str = ""
    obstruction_type: str = ""  # "structural", "ghost", "projection", "gap"
    severity: str = ""          # "high", "medium", "low"
    description: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class ObstructionCatalog:
    """Catalog of all obstructions."""
    obstructions: List[ObstructionEntry] = field(default_factory=list)
    n_obstructions: int = 0
    n_high_severity: int = 0
    n_medium_severity: int = 0
    n_low_severity: int = 0
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentBAssessment:
    """Aggregate assessment: no computed carrier supplies Component B.

    Post-projection: insufficient (collapses to Route C 1/r^4).
    Computed pre-projection: pathological or projection-killed.
    Uncomputed: g_- / doubled-metric remains as key unresolved channel.
    """
    post_projection_sufficient: bool = False
    computed_preprojection_sufficient: bool = False
    uncomputed_sector_remains: bool = False
    uncomputed_sector_name: str = ""
    is_general_no_go: bool = False
    classification_string: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBClassification:
    """Provisional classification of the Route B Component B test.

    This is a BOUNDED result: Route B cannot provide Component B through
    any computed channel, but the g_- sector is not fully ruled out.
    """
    classification: str = ""
    post_projection_status: str = ""
    phi_minus_status: str = ""
    s_diss_status: str = ""
    g_minus_status: str = ""
    is_general_no_go: bool = False
    uncomputed_sector_remains: bool = False
    route_b_previous_status: str = ""
    route_b_current_status: str = ""
    is_provisional: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBComponentBResult:
    """Master result for the Route B Component B test."""
    valid: bool = False
    params: RouteBParams = field(default_factory=RouteBParams)
    post_projection: Optional[PostProjectionEquivalence] = None
    phi_minus_sector: Optional[PhiMinusSectorAnalysis] = None
    g_minus_sector: Optional[GMinusSectorAnalysis] = None
    dissipative_kernel: Optional[DissipativeKernelAnalysis] = None
    carrier_catalog: Optional[CandidateCarrierCatalog] = None
    obstruction_catalog: Optional[ObstructionCatalog] = None
    assessment: Optional[ComponentBAssessment] = None
    classification: Optional[RouteBClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Radial grid and baseline
# ================================================================

def make_radial_grid(params: RouteBParams) -> np.ndarray:
    """Create log-spaced radial grid from R_ext down to R_min."""
    r_min = max(params.R_min, params.R_eq * 0.8)
    log_r = np.linspace(math.log(params.R_ext), math.log(r_min), params.n_r)
    return np.exp(log_r)


def compute_static_mass(
    r: np.ndarray, params: RouteBParams,
) -> np.ndarray:
    """Compute linearized static mass profile.

    m(r) = M + (2*pi*M^2 / tau^2) * (1/r - 1/R_ext)
    """
    M = params.M
    tau2 = params.tau ** 2
    coeff = 2.0 * math.pi * M * M / tau2
    return M + coeff * (1.0 / r - 1.0 / params.R_ext)


def compute_equilibrium_density(
    r: np.ndarray, params: RouteBParams,
) -> np.ndarray:
    """Compute equilibrium energy density rho_eq = -M^2 / (2*tau^2*r^4)."""
    M = params.M
    tau2 = params.tau ** 2
    return -M * M / (2.0 * tau2 * r ** 4)


# ================================================================
# Level 2: Post-Projection Equivalence
# ================================================================

def analyze_post_projection_equivalence(
    params: RouteBParams,
) -> PostProjectionEquivalence:
    """Show post-projection Route B T^Phi = Route C T^Phi = pure 1/r^4.

    In the physical limit (Phi_1 = Phi_2 = Phi, g_1 = g_2 = g):
    - S_1 - S_2 -> 0 (copies cancel)
    - S_diss -> 0 (Phi_1 - Phi_2 = 0)
    - EOM from variation before projection reduces to GRUT relaxation
    - T^Phi from metric variation = standard minimally-coupled scalar
    - epsilon = (1/2)(Phi_dot)^2 = A_crit^2 * M^2 / (2 * tau^2 * r^4)

    This is IDENTICAL to Route C.  Therefore the same shape mismatch
    applies: overcovering at R_eq, undercovering at r=1.
    """
    r = make_radial_grid(params)
    m = compute_static_mass(r, params)
    rho_eq = compute_equilibrium_density(r, params)
    delta = m - r / 2.0
    deficit_mask = delta > 0

    # Post-projection energy density: pure 1/r^4 (SAME as Route C)
    eps_coeff = params.A_crit ** 2 * params.M ** 2 / (2.0 * params.tau ** 2)
    epsilon_post = eps_coeff / r ** 4

    # Minimal source from Phase 6C
    component_A = np.where(deficit_mask, np.abs(rho_eq), 0.0)
    component_B = np.where(deficit_mask, 1.0 / (8.0 * math.pi * r ** 2), 0.0)
    epsilon_min = component_A + component_B

    # Deficit ratio
    safe_min = np.where(epsilon_min > 0, epsilon_min, 1.0)
    deficit_ratio = np.where(epsilon_min > 0, epsilon_post / safe_min, 0.0)

    # Interpolation at key radii
    r_rev = r[::-1]

    def _interp(arr, r_target):
        return float(np.interp(r_target, r_rev, arr[::-1]))

    ratio_at_R_eq = _interp(deficit_ratio, params.R_eq)
    ratio_at_r1 = _interp(deficit_ratio, 1.0)

    # Verify identity with Route C
    route_c_coeff = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
    identical = abs(eps_coeff - route_c_coeff) / route_c_coeff < 1e-10

    return PostProjectionEquivalence(
        r=r,
        epsilon_post_proj=epsilon_post,
        epsilon_min=epsilon_min,
        epsilon_RC_coeff=eps_coeff,
        ratio_at_R_eq=ratio_at_R_eq,
        ratio_at_r1=ratio_at_r1,
        identical_to_route_c=identical,
        provides_component_B=False,
        shape_mismatch=(
            "Post-projection Route B inherits Route C's shape mismatch: "
            "1/r^4 support is too concentrated — it oversupplies the core "
            f"(ratio {ratio_at_R_eq:.3f} > 1 at R_eq) while undersupplying "
            f"intermediate radii (ratio {ratio_at_r1:.3f} < 1 at r=1).  "
            "The failure is one of shape, not amplitude."
        ),
        notes=[
            f"Post-projection epsilon_coeff = {eps_coeff:.6f}",
            f"Route C epsilon_coeff = {route_c_coeff:.6f}",
            f"Identical to Route C: {identical}",
            f"Ratio at R_eq = {ratio_at_R_eq:.4f} (overcovering)",
            f"Ratio at r=1 = {ratio_at_r1:.4f} (undercovering)",
            "Post-projection Route B T^Phi is the standard minimally-coupled "
            "scalar form — same as Route C.",
        ],
    )


# ================================================================
# Level 3: Pre-Projection Sector Analyses
# ================================================================

def analyze_phi_minus_sector(
    params: RouteBParams,
) -> PhiMinusSectorAnalysis:
    """Analyze the Phi_- (ghost / difference) sector.

    The Galley cross-coupled EOMs:
      dPhi_1/dt = (X - Phi_2) / tau
      dPhi_2/dt = (X - Phi_1) / tau

    In +/- variables:
      dPhi_+/dt = (X - Phi_+) / tau   [GRUT relaxation]
      dPhi_-/dt = Phi_- / tau          [exponential GROWTH]

    Full KG+Galley:
      d^2 Phi_-/dt^2 - (1/tau) dPhi_-/dt - (1/tau^2) Phi_- = 0
      => growth rate = phi/tau (golden ratio)

    Key physics:
    - Kinetic sign: WRONG (-1, ghost)
    - Spatial profile: IC-dependent, NOT sourced by X = M/r^2
    - CTP boundary: Phi_-(t_final) = 0 => killed at final time
    - Cannot provide geometric Component B
    """
    tau = params.tau
    phi = params.phi_golden

    # Growth rates
    simple_rate = 1.0 / tau
    full_rate = phi / tau
    decay_rate = 1.0 / (phi * tau)

    return PhiMinusSectorAnalysis(
        simple_growth_rate=simple_rate,
        full_kg_growth_rate=full_rate,
        full_kg_decay_rate=decay_rate,
        kinetic_sign=-1,
        is_ghost=True,
        spatial_profile_geometric=False,
        spatial_profile_source="initial_conditions",
        ctp_kills_at_final_time=True,
        provides_component_B=False,
        provides_1r2=False,
        notes=[
            f"Simple Galley growth rate: 1/tau = {simple_rate:.6f}",
            f"Full KG+Galley growth rate: phi/tau = {full_rate:.6f}",
            f"Full KG+Galley decay rate: 1/(phi*tau) = {decay_rate:.6f}",
            "Kinetic sign = -1 (wrong-sign, ghost mode)",
            "Spatial profile is IC-dependent, NOT sourced by geometric X = M/r^2",
            "Because the Phi_- spatial profile is initial-condition dependent "
            "rather than sourced by the geometric X = M/r^2 profile, it cannot "
            "be treated as an independently derived geometric Component B carrier.",
            "CTP boundary condition Phi_-(t_final) = 0 kills Phi_- at final time",
            "Phi_- does NOT provide Component B: ghost-contaminated, "
            "spatially non-geometric, and CTP-killed",
        ],
    )


def analyze_g_minus_sector(
    params: RouteBParams,
) -> GMinusSectorAnalysis:
    """Analyze the g_- (metric-difference) sector.

    The doubled-metric action:
      S_grav = (1/(16*pi*G)) int [sqrt(-g_1) R_1 - sqrt(-g_2) R_2]

    In the +/- decomposition:
      g_+ = (g_1 + g_2) / 2  (physical metric)
      g_- = g_1 - g_2         (difference metric)

    The linearized g_- action has WRONG-SIGN kinetic energy (gravitational
    ghost).  g_- = 0 is a consistent truncation but is expected unstable.

    CRITICAL: The g_- energy density scaling has NOT been computed in
    closed form.  This is the key unresolved channel — 1/r^2 CANNOT
    be ruled out.  But the sector is ghost-contaminated (wrong-sign EH)
    and projection-sensitive.
    """
    return GMinusSectorAnalysis(
        wrong_sign_eh=True,
        consistent_truncation=True,
        expected_unstable=True,
        energy_density_computed=False,
        energy_density_scaling="uncomputed",
        status="uncomputed_and_projection_sensitive",
        provides_component_B="undetermined",
        is_key_unresolved_channel=True,
        notes=[
            "S_grav = S_EH[g_1] - S_EH[g_2] => linearized g_- has wrong-sign kinetic",
            "g_- = 0 is a consistent truncation (analogous to scalar Phi_- = 0)",
            "g_- = 0 is expected UNSTABLE from wrong-sign Einstein-Hilbert action",
            "g_- energy density scaling: NOT COMPUTED in closed form",
            "This is the key unresolved pre-projection channel",
            "Cannot rule out 1/r^2 from g_-; but sector is ghost-contaminated",
            "Status: uncomputed_and_projection_sensitive (NOT simply projection-killed)",
            "A full Route B no-go would require computing this sector",
        ],
    )


def analyze_dissipative_kernel(
    params: RouteBParams,
) -> DissipativeKernelAnalysis:
    """Analyze the dissipative kernel S_diss contribution.

    S_diss ~ (Phi_1 - Phi_2) * u^a nabla_a (Phi_1 + Phi_2) / (2*tau)
           = Phi_- * Phi_dot_plus / tau

    In the physical limit (Phi_- = 0):
      S_diss = 0 exactly
      => zero energy density from this channel

    Pre-projection: S_diss inherits Phi_- ghost pathology since it is
    proportional to Phi_-.
    """
    return DissipativeKernelAnalysis(
        s_diss_at_physical_limit=0.0,
        vanishes_in_physical_limit=True,
        pre_projection_ghost_coupled=True,
        provides_component_B=False,
        notes=[
            "S_diss = (Phi_1 - Phi_2) * Phi_dot_plus / tau = Phi_- * Phi_dot_plus / tau",
            "Physical limit: Phi_- = 0 => S_diss = 0 (exact)",
            "Zero energy density from S_diss in the physical limit",
            "Pre-projection: S_diss is proportional to Phi_-, "
            "inheriting its ghost-like growth and CTP boundary condition",
            "S_diss is projection-killed and ghost-coupled through Phi_-",
        ],
    )


# ================================================================
# Level 4: Candidate Carrier Catalog
# ================================================================

def build_candidate_carrier_catalog(
    params: RouteBParams,
) -> CandidateCarrierCatalog:
    """Build catalog of all 5 candidate energy-density carriers.

    Carriers are distinguished by carrier_type:
      projected_observable:     post-projection physical observable
      computed_sector:          pre-projection sector with known structure
      formal_variation_channel: variational placeholder, not yet computed
    """
    carriers = [
        CandidateCarrier(
            carrier_number=1,
            name="post_projection_tphi_kinetic",
            sector="post_projection",
            carrier_type="projected_observable",
            scaling_if_known="1/r^4",
            ghost_status="none",
            projection_status="survives",
            status_summary="INSUFFICIENT",
            provides_component_B="no",
            notes=["Pure 1/r^4, identical to Route C, no 1/r^2 component"],
        ),
        CandidateCarrier(
            carrier_number=2,
            name="phi_minus_kinetic_energy",
            sector="phi_minus",
            carrier_type="computed_sector",
            scaling_if_known="IC_dependent",
            ghost_status="wrong_sign_kinetic",
            projection_status="killed",
            status_summary="PATHOLOGICAL",
            provides_component_B="no",
            notes=[
                "Wrong-sign kinetic energy (ghost)",
                "Spatial profile IC-dependent, not geometric 1/r^2",
                "CTP boundary kills at t_final",
            ],
        ),
        CandidateCarrier(
            carrier_number=3,
            name="s_diss_energy_density",
            sector="dissipative_kernel",
            carrier_type="computed_sector",
            scaling_if_known="0_in_phys_limit",
            ghost_status="ghost_coupled",
            projection_status="killed",
            status_summary="PROJECTION_KILLED",
            provides_component_B="no",
            notes=[
                "Vanishes exactly in physical limit (Phi_- = 0)",
                "Ghost-coupled through Phi_- pre-projection",
            ],
        ),
        CandidateCarrier(
            carrier_number=4,
            name="g_minus_gravitational_energy",
            sector="g_minus",
            carrier_type="formal_variation_channel",
            scaling_if_known="uncomputed",
            ghost_status="wrong_sign_eh",
            projection_status="projection_sensitive",
            status_summary="UNCOMPUTED_GHOST_CONTAMINATED",
            provides_component_B="undetermined",
            notes=[
                "Wrong-sign Einstein-Hilbert action (gravitational ghost)",
                "Energy density scaling NOT computed in closed form",
                "Key unresolved channel — 1/r^2 cannot be ruled out",
                "Status: uncomputed_and_projection_sensitive",
            ],
        ),
        CandidateCarrier(
            carrier_number=5,
            name="doubled_metric_variation",
            sector="doubled_metric",
            carrier_type="formal_variation_channel",
            scaling_if_known="uncomputed",
            ghost_status="wrong_sign_eh",
            projection_status="projection_sensitive",
            status_summary="UNCOMPUTED",
            provides_component_B="undetermined",
            notes=[
                "delta S / delta g_- has not been evaluated",
                "Formal variation channel, not a computed sector",
            ],
        ),
    ]

    # Counts by status
    n_physical = sum(1 for c in carriers if c.provides_component_B == "yes")
    n_pathological = sum(
        1 for c in carriers
        if c.status_summary == "PATHOLOGICAL"
    )
    n_projection_killed = sum(
        1 for c in carriers
        if c.status_summary == "PROJECTION_KILLED"
    )
    n_uncomputed = sum(
        1 for c in carriers
        if "UNCOMPUTED" in c.status_summary
    )

    # Counts by carrier_type
    n_proj_obs = sum(1 for c in carriers if c.carrier_type == "projected_observable")
    n_comp_sect = sum(1 for c in carriers if c.carrier_type == "computed_sector")
    n_formal = sum(1 for c in carriers if c.carrier_type == "formal_variation_channel")

    return CandidateCarrierCatalog(
        carriers=carriers,
        n_carriers=len(carriers),
        n_physical=n_physical,
        n_pathological=n_pathological,
        n_projection_killed=n_projection_killed,
        n_uncomputed=n_uncomputed,
        n_projected_observable=n_proj_obs,
        n_computed_sector=n_comp_sect,
        n_formal_variation_channel=n_formal,
        notes=[
            f"Total carriers: {len(carriers)}",
            f"Physical: {n_physical}",
            f"Pathological (ghost + CTP-killed): {n_pathological}",
            f"Projection-killed: {n_projection_killed}",
            f"Uncomputed (including ghost-contaminated): {n_uncomputed}",
            f"carrier_type breakdown: {n_proj_obs} projected_observable, "
            f"{n_comp_sect} computed_sector, {n_formal} formal_variation_channel",
            "The two formal variation channels (g_- energy, delta S/delta g_-) "
            "are the unresolved residue",
        ],
    )


# ================================================================
# Level 5: Obstruction Catalog
# ================================================================

def build_obstruction_catalog() -> ObstructionCatalog:
    """Build catalog of obstructions to Component B support from Route B.

    5 obstructions with severity:
      3 high (structural + ghost obstructions)
      2 medium (projection + gap obstructions)
    """
    obstructions = [
        ObstructionEntry(
            obstruction_number=1,
            name="post_projection_identity_with_route_c",
            sector="post_projection",
            obstruction_type="structural",
            severity="high",
            description=(
                "Post-projection Route B T^Phi is identical to Route C T^Phi "
                "(standard minimally-coupled scalar).  The post-projection energy "
                "density is pure 1/r^4, providing Component A but not Component B.  "
                "This is a structural identity, not a numerical accident."
            ),
            notes=[
                "This obstruction closes the post-projection channel completely",
                "Shape mismatch: overcovering at R_eq, undercovering at r=1",
            ],
        ),
        ObstructionEntry(
            obstruction_number=2,
            name="phi_minus_wrong_sign_kinetic",
            sector="phi_minus",
            obstruction_type="ghost",
            severity="high",
            description=(
                "The Phi_- kinetic energy has wrong sign (-(1/2)(nabla Phi_-)^2 "
                "in the doubled action), making it a ghost mode.  The energy "
                "density is unbounded from below in this sector."
            ),
            notes=[
                "Ghost sign is a structural feature of the Galley CTP encoding",
                "Whether this is a formal or physical pathology is not settled",
            ],
        ),
        ObstructionEntry(
            obstruction_number=3,
            name="ctp_boundary_kills_phi_minus",
            sector="phi_minus",
            obstruction_type="projection",
            severity="medium",
            description=(
                "The CTP boundary condition Phi_-(t_final) = 0 kills the "
                "Phi_- mode at the final time.  Combined with ghost growth, "
                "this means Phi_- has no permanent contribution at equilibrium."
            ),
            notes=[
                "CTP is what makes the Galley formalism encode dissipation",
                "Without CTP, Phi_- grows without bound",
            ],
        ),
        ObstructionEntry(
            obstruction_number=4,
            name="g_minus_wrong_sign_einstein_hilbert",
            sector="g_minus",
            obstruction_type="ghost",
            severity="high",
            description=(
                "The doubled-metric action S_grav = S_EH[g_1] - S_EH[g_2] "
                "gives g_- a wrong-sign Einstein-Hilbert action.  This is a "
                "gravitational ghost analogous to the scalar ghost in Phi_-."
            ),
            notes=[
                "g_- = 0 is a consistent truncation, expected unstable",
                "Whether g_- ghost is formal or physical is not settled",
            ],
        ),
        ObstructionEntry(
            obstruction_number=5,
            name="g_minus_energy_density_uncomputed",
            sector="g_minus",
            obstruction_type="gap",
            severity="medium",
            description=(
                "The g_- energy density scaling has NOT been computed in closed "
                "form.  The full doubled-metric variation delta S / delta g_- "
                "has not been evaluated.  Therefore 1/r^2 cannot be ruled out "
                "from this sector.  This is the key unresolved channel."
            ),
            notes=[
                "A full Route B no-go requires computing this sector",
                "This gap prevents returning a complete classification",
            ],
        ),
    ]

    n_high = sum(1 for o in obstructions if o.severity == "high")
    n_medium = sum(1 for o in obstructions if o.severity == "medium")
    n_low = sum(1 for o in obstructions if o.severity == "low")

    return ObstructionCatalog(
        obstructions=obstructions,
        n_obstructions=len(obstructions),
        n_high_severity=n_high,
        n_medium_severity=n_medium,
        n_low_severity=n_low,
        notes=[
            f"Total obstructions: {len(obstructions)}",
            f"High severity: {n_high} (structural + ghost)",
            f"Medium severity: {n_medium} (projection + gap)",
            f"Low severity: {n_low}",
            "Obstruction 5 (gap) is the key barrier to a full no-go",
        ],
    )


# ================================================================
# Level 6: Assessment & Classification
# ================================================================

def assess_component_b_support(
    params: RouteBParams,
) -> ComponentBAssessment:
    """Assess whether Route B can provide Component B support.

    Three-level assessment:
    1. Post-projection: insufficient (collapses to Route C 1/r^4)
    2. Computed pre-projection (Phi_-, S_diss): pathological or killed
    3. Uncomputed (g_-, doubled-metric): key unresolved channel

    No computed carrier supplies Component B.  Unresolved formal
    variation channels remain in the g_- / doubled-metric sector.
    """
    return ComponentBAssessment(
        post_projection_sufficient=False,
        computed_preprojection_sufficient=False,
        uncomputed_sector_remains=True,
        uncomputed_sector_name="g_minus_doubled_metric",
        is_general_no_go=False,
        classification_string=(
            "route_b_post_projection_insufficient__preprojection_unresolved"
        ),
        notes=[
            "Post-projection: INSUFFICIENT — collapses to Route C 1/r^4",
            "Phi_-: PATHOLOGICAL — ghost, IC-dependent, CTP-killed",
            "S_diss: PROJECTION-KILLED — vanishes in physical limit",
            "g_-: UNRESOLVED — energy density not computed, key open channel",
            "delta S / delta g_-: UNRESOLVED — not evaluated",
            "No computed carrier supplies physical Component B",
            "is_general_no_go = False: g_- sector uncomputed prevents full no-go",
            "This phase does not compute the pre-projection g_- energy density "
            "or the full doubled-metric variation.  Therefore it cannot return "
            "a full Route B no-go.  It can only classify the already-computed "
            "sectors and localize the remaining unknown to the g_- / "
            "doubled-metric channel.",
        ],
    )


def classify_route_b_component_b(
    post_proj: PostProjectionEquivalence,
    phi_minus: PhiMinusSectorAnalysis,
    g_minus: GMinusSectorAnalysis,
    s_diss: DissipativeKernelAnalysis,
    assessment: ComponentBAssessment,
) -> RouteBClassification:
    """Provisional classification of the Route B Component B test.

    Classification: route_b_post_projection_insufficient__preprojection_unresolved

    This is a BOUNDED result:
    - Post-projection channel: insufficient (closed)
    - Phi_-: pathological (ghost, IC-dependent, CTP-killed)
    - S_diss: vanishes in physical limit
    - g_- / doubled-metric: unresolved (key open channel)
    """
    return RouteBClassification(
        classification=(
            "route_b_post_projection_insufficient__preprojection_unresolved"
        ),
        post_projection_status="insufficient",
        phi_minus_status="pathological",
        s_diss_status="vanishes_in_physical_limit",
        g_minus_status="unresolved",
        is_general_no_go=False,
        uncomputed_sector_remains=True,
        route_b_previous_status="provisional__highest_untested_candidate",
        route_b_current_status=(
            "post_projection_insufficient__preprojection_unresolved"
        ),
        is_provisional=True,
        notes=[
            "Classification: route_b_post_projection_insufficient__preprojection_unresolved",
            "Post-projection: INSUFFICIENT (collapses to Route C 1/r^4)",
            "Phi_-: PATHOLOGICAL (ghost, IC-dependent, CTP-killed)",
            "S_diss: VANISHES in physical limit",
            "g_- / doubled-metric: UNRESOLVED (key open channel, uncomputed)",
            "This is a BOUNDED result, not a full no-go",
            "Route B is NOT downgraded to fully closed — g_- remains open",
            "Provisional ranking update: Route B bounded but not resolved",
        ],
    )


# ================================================================
# Master function
# ================================================================

def compute_route_b_component_b_assessment(
    params: Optional[RouteBParams] = None,
    do_post_projection: bool = True,
    do_phi_minus: bool = True,
    do_g_minus: bool = True,
    do_dissipative: bool = True,
    do_carriers: bool = True,
    do_obstructions: bool = True,
    do_assessment: bool = True,
    do_classification: bool = True,
) -> RouteBComponentBResult:
    """Master function: Route B Component B test.

    Tests whether pre-projection Route B can generate the missing 1/r^2
    support identified in Phase 6C.

    UNCOMPUTED-SECTOR BARRIER: This module does not compute the g_-
    energy density or the full doubled-metric variation.  It cannot
    return a full Route B no-go.
    """
    if params is None:
        params = RouteBParams()

    result = RouteBComponentBResult(
        params=params,
        nonclaims=NONCLAIMS,
        assumptions=ROUTE_B_ASSUMPTIONS,
    )

    # Level 2: Post-projection equivalence
    post_proj = None
    if do_post_projection:
        post_proj = analyze_post_projection_equivalence(params)
        result.post_projection = post_proj

    # Level 3: Pre-projection sectors
    phi_minus = None
    if do_phi_minus:
        phi_minus = analyze_phi_minus_sector(params)
        result.phi_minus_sector = phi_minus

    g_minus = None
    if do_g_minus:
        g_minus = analyze_g_minus_sector(params)
        result.g_minus_sector = g_minus

    s_diss = None
    if do_dissipative:
        s_diss = analyze_dissipative_kernel(params)
        result.dissipative_kernel = s_diss

    # Level 4: Carrier catalog
    if do_carriers:
        result.carrier_catalog = build_candidate_carrier_catalog(params)

    # Level 5: Obstruction catalog
    if do_obstructions:
        result.obstruction_catalog = build_obstruction_catalog()

    # Level 6: Assessment and classification
    assessment = None
    if do_assessment:
        assessment = assess_component_b_support(params)
        result.assessment = assessment

    if (do_classification and post_proj is not None and phi_minus is not None
            and g_minus is not None and s_diss is not None
            and assessment is not None):
        result.classification = classify_route_b_component_b(
            post_proj, phi_minus, g_minus, s_diss, assessment,
        )

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def route_b_result_to_dict(result: RouteBComponentBResult) -> Dict[str, Any]:
    """Serialize the master result to a dictionary."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "params": {
            "r_s": result.params.r_s,
            "M": result.params.M,
            "R_eq": result.params.R_eq,
            "tau": result.params.tau,
            "R_ext": result.params.R_ext,
            "n_r": result.params.n_r,
            "A_crit": result.params.A_crit,
            "phi_golden": result.params.phi_golden,
        },
    }

    if result.post_projection:
        pp = result.post_projection
        d["post_projection"] = {
            "epsilon_RC_coeff": pp.epsilon_RC_coeff,
            "ratio_at_R_eq": pp.ratio_at_R_eq,
            "ratio_at_r1": pp.ratio_at_r1,
            "identical_to_route_c": pp.identical_to_route_c,
            "provides_component_B": pp.provides_component_B,
        }

    if result.phi_minus_sector:
        pm = result.phi_minus_sector
        d["phi_minus_sector"] = {
            "simple_growth_rate": pm.simple_growth_rate,
            "full_kg_growth_rate": pm.full_kg_growth_rate,
            "kinetic_sign": pm.kinetic_sign,
            "is_ghost": pm.is_ghost,
            "spatial_profile_geometric": pm.spatial_profile_geometric,
            "ctp_kills_at_final_time": pm.ctp_kills_at_final_time,
            "provides_component_B": pm.provides_component_B,
        }

    if result.g_minus_sector:
        gm = result.g_minus_sector
        d["g_minus_sector"] = {
            "wrong_sign_eh": gm.wrong_sign_eh,
            "energy_density_computed": gm.energy_density_computed,
            "status": gm.status,
            "provides_component_B": gm.provides_component_B,
            "is_key_unresolved_channel": gm.is_key_unresolved_channel,
        }

    if result.dissipative_kernel:
        dk = result.dissipative_kernel
        d["dissipative_kernel"] = {
            "s_diss_at_physical_limit": dk.s_diss_at_physical_limit,
            "vanishes_in_physical_limit": dk.vanishes_in_physical_limit,
            "provides_component_B": dk.provides_component_B,
        }

    if result.carrier_catalog:
        cc = result.carrier_catalog
        d["carrier_catalog"] = {
            "n_carriers": cc.n_carriers,
            "n_physical": cc.n_physical,
            "n_pathological": cc.n_pathological,
            "n_projection_killed": cc.n_projection_killed,
            "n_uncomputed": cc.n_uncomputed,
            "n_projected_observable": cc.n_projected_observable,
            "n_computed_sector": cc.n_computed_sector,
            "n_formal_variation_channel": cc.n_formal_variation_channel,
            "carriers": [
                {
                    "carrier_number": c.carrier_number,
                    "name": c.name,
                    "carrier_type": c.carrier_type,
                    "status_summary": c.status_summary,
                    "provides_component_B": c.provides_component_B,
                }
                for c in cc.carriers
            ],
        }

    if result.obstruction_catalog:
        oc = result.obstruction_catalog
        d["obstruction_catalog"] = {
            "n_obstructions": oc.n_obstructions,
            "n_high_severity": oc.n_high_severity,
            "n_medium_severity": oc.n_medium_severity,
            "obstructions": [
                {
                    "obstruction_number": o.obstruction_number,
                    "name": o.name,
                    "severity": o.severity,
                }
                for o in oc.obstructions
            ],
        }

    if result.assessment:
        a = result.assessment
        d["assessment"] = {
            "post_projection_sufficient": a.post_projection_sufficient,
            "computed_preprojection_sufficient": a.computed_preprojection_sufficient,
            "uncomputed_sector_remains": a.uncomputed_sector_remains,
            "is_general_no_go": a.is_general_no_go,
            "classification_string": a.classification_string,
        }

    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "post_projection_status": cl.post_projection_status,
            "phi_minus_status": cl.phi_minus_status,
            "s_diss_status": cl.s_diss_status,
            "g_minus_status": cl.g_minus_status,
            "is_general_no_go": cl.is_general_no_go,
            "uncomputed_sector_remains": cl.uncomputed_sector_remains,
            "is_provisional": cl.is_provisional,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
