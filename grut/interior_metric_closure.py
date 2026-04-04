"""GRUT Appendix J — Interior Metric Closure Analysis.

This module synthesises the three-layer metric deficit chain identified in
Phase 6 / Phase 6B and derives the conditions under which the Killing horizon
condition f(R_eq) = 0 can be achieved, the surface gravity at that horizon,
and the implied Killing temperature — a new, covariant, GRUT-native temperature
candidate that does not appear in the five candidates enumerated in the
thermodynamic sector.

PRINCIPAL RESULTS
-----------------
  Result 1 — Three-Layer Deficit Chain:
    The interior metric f(R_eq) passes through three well-defined levels as
    successively more complete physics is accounted for:

    Layer 0 (Schwarzschild reference):
      f_Schw(R_eq) = 1 - 2M/R_eq = 1 - 6 = -5   [C = 3, M = r_s/2]
      (NOT a GRUT result; reference baseline)

    Layer 1 (Constitutive lapse, post-Newtonian correction):
      A_eff = A_schw + delta_A = -2 + 1 = -1
      Constitutive correction contributes +1 toward the horizon.
      Still negative. (Lapse Insufficiency Theorem: A_eff < 0 for all finite beta_Q.)

    Layer 2 (Static TOV equilibrium, full negative-rho profile):
      f(R_eq) = -17.71  [locked from tov_interior.py]
      m(R_eq) = 3.118   [locked from tov_interior.py]
      Equilibrium rho_eq < 0 causes mass ACCUMULATION inward (dm/dr < 0),
      pushing f far below Schwarzschild. The self-consistent equilibrium
      develops a singularity at r_star ~ 1.023 r_s.

    Layer 3a (Dynamical kinetic, natural profile, A = 1 natural rate):
      f(R_eq) = -2 = A_Schw  [locked from dynamical_interior.py]
      At A = 1 (natural processing rate), kinetic energy density exactly
      cancels equilibrium rho_eq (rho_total = 0), recovering Schwarzschild.

    Layer 3b (Dynamical kinetic, supercritical A = A_crit):
      f(R_eq) = 0  [transient Killing horizon at R_eq]
      Requires A_crit > 1: processing rate must EXCEED the natural rate.

  Result 2 — A_crit Derivation (exact, canonical units):
    In canonical units (r_s = 1, M = 1/2, R_eq = 1/3, tau^2 = 3/2):

      m(R_eq, A) = M + 2*pi*M^2*(A^2-1)/tau^2 * (1/R_ext - 1/R_eq)

    f(R_eq) = 0  requires  m(R_eq) = R_eq/2

      A_crit^2 = 1 + (M - R_eq/2) / [2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext)]

    With R_ext = 2*r_s (canonical external matching radius):

      (M - R_eq/2) = 1/3
      2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext) = 5*pi/6

      A_crit^2 = 1 + 2/(5*pi)
      A_crit = sqrt(1 + 2/(5*pi)) ~ 1.062  [6.2% above natural rate]

    This is consistent with the locked numerical value A_crit ~ 1.06 from
    dynamical_interior.py tests.

  Result 3 — Surface Gravity at the Killing Horizon:
    At A = A_crit, the metric f passes through zero at R_eq with derivative:

      f'(R_eq) = [1 - 4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq)] / R_eq

    With canonical parameters:

      4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq) = 4/5

      f'(R_eq) = (1 - 4/5) / (1/3) = 3/5

    Surface gravity:
      kappa_GRUT = f'(R_eq)/2 = 3/10

    Schwarzschild reference:
      kappa_Schw = 1/(4M) = 1/2

    Ratio:
      kappa_GRUT / kappa_Schw = (3/10) / (1/2) = 3/5

  Result 4 — Killing Temperature (new T candidate):
    Via the standard Wald-Unruh formula T = hbar*kappa/(2*pi*k_B):

      T_Killing / T_Hawking = kappa_GRUT / kappa_Schw = 3/5

    T_Killing_GRUT = (3/5) * T_Hawking

    This is a NEW temperature candidate not enumerated in the five candidates
    of the thermodynamic sector. It is GRUT-covariant in the sense that:
    (a) it is derived from the dynamical interior metric, which is a GRUT object;
    (b) it uses only GRUT-locked parameters (M, R_eq, tau, A_crit);
    (c) it does not import standard Hawking radiation machinery — it identifies
        kappa_GRUT from the interior metric's radial derivative at the horizon,
        then uses the Unruh-Wald formula which requires only classical GR + QFT
        input, not GRUT-specific Hawking mechanics.

    T_Killing = (3/5) * hbar*c^3 / (8*pi*G*M*k_B) = 0.6 * T_Hawking

  Result 5 — Transient Caveat:
    The Killing horizon at R_eq is TRANSIENT. It exists only while the scalar
    field has active kinetic processing (Phi_dot ~ A_crit * M/(tau*r^2)),
    which decays as exp(-t/tau) during dynamical relaxation. At late times
    f(R_eq) returns toward the static equilibrium value f = -17.71. The metric
    positivity window has duration of order tau.

    Classification: metric_positivity_achievable_transient_supercritical_processing

  Result 6 — Special Case: Extremal Horizon:
    When R_ext → r_s (exterior matching at the Schwarzschild radius):
      A_crit^2 = 1 + 1/(2*pi)
      f'(R_eq) → 0  (kappa → 0)
      T_Killing → 0 (extremal, zero-temperature horizon)

    This is a self-consistency marker: the extremal limit occurs when the
    interior and exterior matching surfaces coincide, leaving no room for
    the mass integral correction.

INHERITED LOCKED VALUES
-----------------------
  f(R_eq) = -17.71   [static TOV; tov_interior.py]
  m(R_eq) = 3.118    [static TOV; tov_interior.py]
  A_crit ~ 1.06      [dynamical interior; dynamical_interior.py]
  f(R_eq)|_{A=1} = -2.0  [Schwarzschild; dynamical_interior.py]
  alpha_vac = 1/3, beta_Q = 2, epsilon_Q = 1/9  [Phase III]
  R_eq/r_s = 1/3     [Phase V]

NONCLAIMS
---------
1. T_Killing is NOT proven to be the physical temperature of the GRUT interior.
   It is a new candidate derived from the interior metric.
2. The transient horizon is NOT a permanent equilibrium configuration.
3. A_crit > 1 is NOT shown to be physically realised — it sets a threshold.
4. This module does NOT claim that the ghost-free status of the Galley route
   is resolved; T_Killing is independent of the Galley sector.
5. This module does NOT assert that the first-law gap (Appendix I) is closed
   by T_Killing; that requires cross-checking T_Killing against T_1stlaw.
6. All Appendix C quantum blockers remain in force.

EXECUTIVE DETERMINATION
-----------------------
  interior_metric_positivity_achievable_transient_supercritical_processing

SCOPE STATEMENT
---------------
  This module establishes the interior metric closure conditions and derives
  the Killing temperature at the transient horizon. It does not claim that
  this temperature is the physically realised temperature; it identifies it
  as a new GRUT-covariant candidate and records its ratio to Hawking.

SELF-CONTAINED: Depends only on math.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


# ================================================================
# Physical constants (SI)
# ================================================================

G_SI = 6.674e-11           # m^3 kg^-1 s^-2
C_SI = 299_792_458.0       # m/s
HBAR_SI = 1.054571817e-34  # J·s
K_B = 1.380649e-23         # J/K

M_SUN_KG = 1.989e30        # kg

# ================================================================
# Canonical GRUT parameters (normalised units: r_s = 1)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
EPSILON_Q = ALPHA_VAC ** BETA_Q   # = 1/9
R_S = 1.0
M_EXT = R_S / 2.0                 # M = r_s/2  (Schwarzschild)
R_EQ = ALPHA_VAC * R_S            # = 1/3
C_EQ = R_S / R_EQ                 # = 3  (compactness at equilibrium)
TAU_SQ = C_EQ / 2.0               # = 3/2  (tau^2 canonical)
TAU = math.sqrt(TAU_SQ)           # = sqrt(3/2)
R_EXT_CANONICAL = 2.0 * R_S       # canonical external matching radius

# Layer values locked from upstream modules
F_STATIC_AT_REQ = -17.71          # static TOV (tov_interior.py)
M_STATIC_AT_REQ = 3.118           # static TOV (tov_interior.py)
F_AT_A1 = -2.0                    # A=1 (natural rate); == A_SCHW
A_SCHW = 1.0 - 2.0 * M_EXT / R_EQ  # = -2
A_EFF_CONSTITUTIVE = -1.0         # Layer 1: constitutive lapse correction
A_CRIT_NUMERICAL = 1.06           # locked from dynamical_interior.py tests

# Exact analytical A_crit (with R_ext = 2)
_NUMERATOR = M_EXT - R_EQ / 2.0   # = 1/3
_DENOM_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ   # 2*pi*M^2/tau^2
_DENOM = _DENOM_COEFF * (1.0 / R_EQ - 1.0 / R_EXT_CANONICAL)  # 5*pi/6
A_CRIT_EXACT_SQ = 1.0 + _NUMERATOR / _DENOM
A_CRIT_EXACT = math.sqrt(A_CRIT_EXACT_SQ)

# Surface gravity at the Killing horizon
_F_PRIME_NUM = 1.0 - 4.0 * math.pi * M_EXT ** 2 * (A_CRIT_EXACT_SQ - 1.0) / (
    TAU_SQ * R_EQ
)
F_PRIME_AT_REQ = _F_PRIME_NUM / R_EQ   # = 3/5  in canonical units
KAPPA_GRUT = 0.5 * F_PRIME_AT_REQ      # = 3/10

KAPPA_SCHW = 1.0 / (4.0 * M_EXT)       # = 1/2  (Schwarzschild surface gravity)
KAPPA_RATIO = KAPPA_GRUT / KAPPA_SCHW  # = 3/5  (exact)

# T_Killing / T_Hawking  (same ratio as kappa)
T_KILLING_OVER_T_HAWKING = KAPPA_RATIO  # = 3/5

# Extremal-limit A_crit (R_ext -> r_s)
A_CRIT_EXTREMAL_SQ = 1.0 + 1.0 / (2.0 * math.pi)
A_CRIT_EXTREMAL = math.sqrt(A_CRIT_EXTREMAL_SQ)

# ================================================================
# Classification vocabularies
# ================================================================

EXECUTIVE_CLASSIFICATIONS = [
    "interior_metric_positivity_achievable_transient_supercritical_processing",
    "interior_metric_positivity_blocked_by_mass_accumulation",
    "interior_metric_positivity_achievable_with_moderate_kinetic_boost",
    "interior_metric_closure_underdetermined",
]

METRIC_LAYER_CLASSIFICATIONS = [
    "sub_schwarzschild",        # f < -5
    "near_schwarzschild",       # -5 <= f < 0
    "killing_horizon",          # f = 0
    "metric_positive",          # f > 0
]

HORIZON_STATUS = [
    "no_horizon",
    "transient_killing_horizon",
    "permanent_killing_horizon",
    "extremal_horizon",
]

TEMPERATURE_STATUS = [
    "new_candidate_grut_covariant",
    "identical_to_existing_candidate",
    "below_existing_candidates",
    "above_existing_candidates",
]

FORBIDDEN_CLAIMS = [
    "t_killing_is_the_physical_temperature",
    "transient_horizon_is_permanent",
    "a_crit_is_physically_realised",
    "first_law_gap_is_closed",
    "ghost_route_resolved",
    "appendix_c_blockers_overridden",
    "hawking_radiation_derived",
    "information_paradox_resolved",
]


# ================================================================
# Data structures
# ================================================================

@dataclass
class MetricLayer:
    """One layer in the three-layer deficit chain."""
    name: str
    description: str
    f_at_R_eq: float
    m_at_R_eq: Optional[float]
    source: str                 # module or derivation that locks this value
    locked: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class ACritResult:
    """Result of the A_crit derivation."""
    R_ext: float = 0.0
    numerator: float = 0.0          # M - R_eq/2
    denominator: float = 0.0        # 2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext)
    A_crit_sq: float = 0.0
    A_crit: float = 0.0
    A_crit_percent: float = 0.0     # percentage above natural rate
    consistent_with_locked: bool = False
    tolerance: float = 0.0
    extremal_limit_A_crit: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class SurfaceGravityResult:
    """Surface gravity and Killing temperature at the horizon."""
    f_prime_at_R_eq: float = 0.0
    kappa_GRUT: float = 0.0
    kappa_Schw: float = 0.0
    kappa_ratio: float = 0.0
    T_Killing_over_T_Hawking: float = 0.0
    T_Killing_SI: float = 0.0       # SI, for reference M = 30 M_sun
    T_Hawking_SI: float = 0.0       # SI, for reference M = 30 M_sun
    temperature_status: str = ""
    derivation: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class TransientCaveat:
    """Quantitative statement of the transient nature of the Killing horizon."""
    decay_timescale: str = ""       # "order tau"
    mechanism: str = ""
    late_time_f: float = 0.0        # f(R_eq) as t -> infinity
    classification: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class FirstLawCrossCheck:
    """Cross-check of T_Killing against the first-law gap."""
    T_Killing_over_T_Hawking: float = 0.0
    T_1stlaw_over_T_Hawking: float = 0.0     # from Appendix I (option b)
    ratio_T_Killing_to_1stlaw: float = 0.0
    gap_closed: bool = False
    gap_fraction: float = 0.0
    verdict: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class InteriorMetricClosureResult:
    """Master result for the interior metric closure analysis."""
    valid: bool = False
    layers: List[MetricLayer] = field(default_factory=list)
    A_crit_result: Optional[ACritResult] = None
    surface_gravity: Optional[SurfaceGravityResult] = None
    transient_caveat: Optional[TransientCaveat] = None
    first_law_cross_check: Optional[FirstLawCrossCheck] = None
    executive: str = ""
    nonclaims: List[str] = field(default_factory=list)
    forbidden_claims: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Layer builders
# ================================================================

def build_deficit_chain() -> List[MetricLayer]:
    """Build the three-layer metric deficit chain.

    Returns the ordered list of metric layers from least to most complete
    physical description.
    """
    # Layer 0: Schwarzschild reference (not a GRUT result)
    f_schw = 1.0 - 2.0 * M_EXT / R_EQ   # = -2  (this is A_SCHW)
    # NB: Schwarzschild formula gives f = 1 - 2M/r; the compactness C = r_s/R_eq = 3
    # means f_Schw(R_eq) = 1 - C = 1 - 3 = -2 (note: C = R_S/R_EQ = 1/ALPHA_VAC = 3)
    layer0 = MetricLayer(
        name="schwarzschild_reference",
        description=(
            "Schwarzschild metric at R_eq: f = 1 - 2M/R_eq = 1 - C = -2. "
            "This is not a GRUT result; it is the baseline GR metric with no "
            "interior matter support."
        ),
        f_at_R_eq=A_SCHW,
        m_at_R_eq=M_EXT,
        source="Schwarzschild metric (GR baseline, not GRUT)",
        locked=True,
        notes=[
            "f_Schw(R_eq) = 1 - r_s/R_eq = 1 - 3 = -2",
            "Compactness C = R_S/R_EQ = 3 (deeply sub-horizon)",
        ],
    )

    # Layer 1: Constitutive lapse correction
    layer1 = MetricLayer(
        name="constitutive_lapse_correction",
        description=(
            "Constitutive lapse correction: A_eff = A_Schw + delta_A = -2 + 1 = -1. "
            "The constitutive post-Newtonian correction contributes +1, but A_eff "
            "remains negative. The Lapse Insufficiency Theorem (covariant_interior.py) "
            "proves A_eff < 0 for all finite beta_Q."
        ),
        f_at_R_eq=A_EFF_CONSTITUTIVE,
        m_at_R_eq=None,
        source="covariant_interior.py — Constitutive Lapse Insufficiency Theorem",
        locked=True,
        notes=[
            "A_eff = 1 - C*beta_Q/(1+beta_Q) = 1 - 3*2/3 = -1",
            "delta_A = +1 constitutive correction, insufficient to reach f = 0",
            "Theorem: A_eff < 0 for alpha_vac <= e^{-1/2}, for ALL finite beta_Q",
        ],
    )

    # Layer 2: Static TOV equilibrium
    layer2 = MetricLayer(
        name="static_tov_equilibrium",
        description=(
            "Full static TOV integration with equilibrium rho_eq = -M^2/(2 tau^2 r^4) < 0. "
            "Negative energy density causes mass ACCUMULATION inward (dm/dr < 0), "
            "pushing f far below Schwarzschild. A singularity develops at r_star ~ 1.023 r_s."
        ),
        f_at_R_eq=F_STATIC_AT_REQ,
        m_at_R_eq=M_STATIC_AT_REQ,
        source="tov_interior.py — locked numerical result",
        locked=True,
        notes=[
            f"f(R_eq) = {F_STATIC_AT_REQ} (far below Schwarzschild -2)",
            f"m(R_eq) = {M_STATIC_AT_REQ} >> M = {M_EXT}",
            "Singularity at r_star ~ 1.023 r_s prevents self-consistent static solution",
            "Mass accumulation: coeff = 2*pi*M^2/tau^2 ~ 0.524",
        ],
    )

    # Layer 3a: Dynamical kinetic, natural rate A = 1
    layer3a = MetricLayer(
        name="dynamical_natural_rate_A1",
        description=(
            "Dynamic T^Phi with natural-profile Phi_dot(r) = A*M/(tau*r^2) at A = 1. "
            "Kinetic energy density epsilon = 0.5*Phi_dot^2 = M^2/(2*tau^2*r^4) exactly "
            "cancels rho_eq, giving rho_total = 0 and recovering f = A_Schw = -2."
        ),
        f_at_R_eq=F_AT_A1,
        m_at_R_eq=M_EXT,
        source="dynamical_interior.py — locked at A = 1 (natural rate)",
        locked=True,
        notes=[
            "rho_total = rho_eq + epsilon = 0 exactly at A = 1",
            "No mass accumulation correction: m(R_eq) = M_EXT",
            "f(R_eq) = A_Schw = -2 (pure Schwarzschild recovered)",
            "A = 1 is the 'natural' processing rate — 100% of equilibrium forcing",
        ],
    )

    # Layer 3b: Dynamical kinetic, supercritical A = A_crit
    layer3b = MetricLayer(
        name="dynamical_supercritical_A_crit",
        description=(
            "Supercritical kinetic amplitude A > 1 causes kinetic energy to EXCEED "
            "the equilibrium deficit, reducing m(R_eq) below M_EXT. At A = A_crit, "
            "m(R_eq) = R_eq/2, giving the Killing horizon condition f(R_eq) = 0."
        ),
        f_at_R_eq=0.0,
        m_at_R_eq=R_EQ / 2.0,
        source="dynamical_interior.py — A_crit derivation (Result 2 of this module)",
        locked=False,
        notes=[
            f"A_crit = sqrt(1 + 2/(5*pi)) ~ {A_CRIT_EXACT:.4f}",
            "A_crit ~ 1.062: requires 6.2% above natural rate",
            "m(R_eq, A_crit) = R_eq/2 = 1/6 < M_EXT = 0.5",
            "Transient: valid only during active scalar field processing",
        ],
    )

    return [layer0, layer1, layer2, layer3a, layer3b]


# ================================================================
# A_crit derivation
# ================================================================

def compute_A_crit(
    R_ext: float = R_EXT_CANONICAL,
    M: float = M_EXT,
    R_eq: float = R_EQ,
    tau_sq: float = TAU_SQ,
    tolerance: float = 0.02,
) -> ACritResult:
    """Derive the critical kinetic amplitude A_crit analytically.

    The mass profile for the natural Phi_dot = A*M/(tau*r^2):

      m(R_eq, A) = M + 2*pi*M^2*(A^2-1)/tau^2 * (1/R_ext - 1/R_eq)

    The Killing horizon condition f(R_eq) = 0 requires m(R_eq) = R_eq/2:

      A_crit^2 = 1 + (M - R_eq/2) / [2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext)]

    Parameters
    ----------
    R_ext:
        Exterior matching radius (units: r_s = 1). Default: 2*r_s.
    M:
        ADM mass (units: r_s = 1). Default: 0.5.
    R_eq:
        Equilibrium radius (units: r_s = 1). Default: 1/3.
    tau_sq:
        tau^2 (units: r_s^2). Default: 3/2.
    tolerance:
        Fractional tolerance for consistency check with locked numerical value.

    Returns
    -------
    ACritResult
        Complete derivation record.
    """
    numerator = M - R_eq / 2.0

    coeff = 2.0 * math.pi * M * M / tau_sq
    denom = coeff * (1.0 / R_eq - 1.0 / R_ext)

    A_crit_sq = 1.0 + numerator / denom
    A_crit = math.sqrt(A_crit_sq) if A_crit_sq > 0 else float("nan")
    A_crit_percent = (A_crit - 1.0) * 100.0

    # Consistency check with locked numerical value
    consistent = (
        abs(A_crit - A_CRIT_NUMERICAL) / A_CRIT_NUMERICAL < tolerance
    )

    # Extremal limit: R_ext -> r_s = 1
    denom_extremal = coeff * (1.0 / R_eq - 1.0 / R_S)
    A_crit_extremal_sq = 1.0 + numerator / denom_extremal
    A_crit_extremal = (
        math.sqrt(A_crit_extremal_sq) if A_crit_extremal_sq > 0 else float("nan")
    )

    notes = [
        f"Numerator  (M - R_eq/2):          {numerator:.6f}",
        f"Denominator 2pi*M^2/tau^2*(1/R_eq-1/R_ext): {denom:.6f}",
        f"A_crit^2 = 1 + {numerator:.6f}/{denom:.6f} = {A_crit_sq:.6f}",
        f"A_crit = sqrt({A_crit_sq:.6f}) = {A_crit:.4f}",
        f"A_crit percent above natural rate: {A_crit_percent:.2f}%",
        f"Locked numerical value: {A_CRIT_NUMERICAL}",
        f"Consistent (tol={tolerance:.2f}): {consistent}",
        f"Extremal limit (R_ext->r_s): A_crit = {A_crit_extremal:.4f}",
        "Analytic form: A_crit^2 = 1 + 2/(5*pi) with R_ext = 2*r_s",
    ]

    return ACritResult(
        R_ext=R_ext,
        numerator=numerator,
        denominator=denom,
        A_crit_sq=A_crit_sq,
        A_crit=A_crit,
        A_crit_percent=A_crit_percent,
        consistent_with_locked=consistent,
        tolerance=tolerance,
        extremal_limit_A_crit=A_crit_extremal,
        notes=notes,
    )


# ================================================================
# Surface gravity and Killing temperature
# ================================================================

def compute_surface_gravity(
    A_crit_sq: float,
    M: float = M_EXT,
    R_eq: float = R_EQ,
    tau_sq: float = TAU_SQ,
    M_SI: float = 30.0 * M_SUN_KG,
) -> SurfaceGravityResult:
    """Compute the surface gravity and Killing temperature at the transient horizon.

    At f(R_eq) = 0 (m = R_eq/2), with rho_total = M^2*(A^2-1)/(2*tau^2*r^4):

      dm/dr|_{R_eq} = 2*pi*M^2*(A_crit^2-1) / (tau^2 * R_eq^2)

      f'(R_eq) = [1 - 2*R_eq*(dm/dr)] / R_eq
               = [1 - 4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq)] / R_eq

      kappa_GRUT = f'(R_eq) / 2

    Temperature:
      T_Killing = hbar * kappa_GRUT / (2*pi*k_B * G/c^3)
    where the geometric-to-SI conversion factor is c^3/G.

    For Schwarzschild: T_Hawking = hbar*c^3/(8*pi*G*M*k_B)

    Parameters
    ----------
    A_crit_sq:
        A_crit^2 value from compute_A_crit.
    M:
        ADM mass in canonical units.
    R_eq:
        Equilibrium radius in canonical units.
    tau_sq:
        tau^2 in canonical units.
    M_SI:
        Physical mass in kg (for SI temperature evaluation).
    """
    A_crit_sq_minus_1 = A_crit_sq - 1.0

    # dm/dr at R_eq (in canonical units r_s = 1)
    dm_dr = 2.0 * math.pi * M * M * A_crit_sq_minus_1 / (tau_sq * R_eq * R_eq)

    # f'(R_eq)
    f_prime = (1.0 - 2.0 * R_eq * dm_dr) / R_eq

    kappa_grut = 0.5 * f_prime
    kappa_schw = 0.5 / (2.0 * M)   # = 1/(4M) in canonical units
    kappa_ratio = kappa_grut / kappa_schw

    # SI temperature: T_Killing = hbar * kappa_SI / (2*pi*k_B)
    # kappa_SI = kappa_grut * c^3 / (G * M_SI)  [conversion from c=G=1 to SI]
    kappa_SI_factor = C_SI ** 3 / (G_SI * M_SI)
    # In canonical units, kappa_grut is in units of c^3/(G*M_ADM) for mass M (in r_s units)
    # The geometric unit kappa in c=G=1 with length r_s corresponds to c/r_s
    # But since r_s = 2*G*M_SI/c^2, we have:
    # kappa_SI = kappa_grut * c^3 / (2*G*M_SI)
    # where kappa_grut uses M = 0.5, r_s = 1
    kappa_SI = kappa_grut * C_SI ** 3 / (2.0 * G_SI * M_SI)
    T_Killing_SI = HBAR_SI * kappa_SI / (2.0 * math.pi * K_B)

    # Hawking temperature (SI)
    T_Hawking_SI = HBAR_SI * C_SI ** 3 / (8.0 * math.pi * G_SI * M_SI * K_B)

    # Ratio check
    T_ratio = T_Killing_SI / T_Hawking_SI if T_Hawking_SI > 0 else float("nan")

    notes = [
        f"A_crit^2 - 1 = {A_crit_sq_minus_1:.6f}",
        f"dm/dr|_{{R_eq}} = {dm_dr:.6f}  (canonical units)",
        f"f'(R_eq) = {f_prime:.6f}  (canonical units)",
        f"kappa_GRUT = {kappa_grut:.6f}  (canonical units)",
        f"kappa_Schw  = {kappa_schw:.6f}  (canonical units)",
        f"kappa ratio = {kappa_ratio:.6f}  (should be 3/5 = 0.600...)",
        f"T_Killing/T_Hawking = {T_ratio:.6f}  (should equal kappa ratio)",
        f"T_Hawking (30 Msun) = {T_Hawking_SI:.4e} K",
        f"T_Killing (30 Msun) = {T_Killing_SI:.4e} K",
        "Derivation: Wald-Unruh formula T = hbar*kappa/(2*pi*k_B)",
        "kappa derived from f'(R_eq) of the dynamical interior metric",
        "T_Killing is a NEW candidate not in the 5-candidate thermodynamic set",
    ]

    return SurfaceGravityResult(
        f_prime_at_R_eq=f_prime,
        kappa_GRUT=kappa_grut,
        kappa_Schw=kappa_schw,
        kappa_ratio=kappa_ratio,
        T_Killing_over_T_Hawking=T_ratio,
        T_Killing_SI=T_Killing_SI,
        T_Hawking_SI=T_Hawking_SI,
        temperature_status="new_candidate_grut_covariant",
        derivation=(
            "f'(R_eq) from dynamical interior metric at A = A_crit; "
            "kappa = f'(R_eq)/2; T = hbar*kappa/(2*pi*k_B)"
        ),
        notes=notes,
    )


# ================================================================
# Transient caveat
# ================================================================

def build_transient_caveat() -> TransientCaveat:
    """Construct the transient-horizon caveat object."""
    return TransientCaveat(
        decay_timescale="order tau (one relaxation time)",
        mechanism=(
            "Phi_dot ~ A_crit * M/(tau*r^2) decays as exp(-t/tau) during "
            "dynamical relaxation. The kinetic energy surplus that drives "
            "f(R_eq) to 0 dissipates on the relaxation timescale."
        ),
        late_time_f=F_STATIC_AT_REQ,
        classification="metric_positivity_achievable_transient_supercritical_processing",
        notes=[
            "Metric positivity window: O(tau)",
            f"Late-time f(R_eq) -> {F_STATIC_AT_REQ} (static TOV value)",
            "No permanent Killing horizon exists in the static equilibrium",
            "Physical interpretation: the Killing temperature is associated "
            "with the active-processing phase, not the static endpoint",
        ],
    )


# ================================================================
# First-law cross-check
# ================================================================

def compute_first_law_cross_check(
    T_Killing_ratio: float,
    T_1stlaw_ratio: float = 9.0,   # Appendix I, option (b): T_1stlaw = 9*T_Hawking
) -> FirstLawCrossCheck:
    """Cross-check T_Killing against the first-law temperature target.

    From Appendix I, option (b), the first-law gap closes if
    T_1stlaw = 9 * T_Hawking (the 'viable' thermodynamic option).

    T_Killing = 3/5 * T_Hawking is far below this — the Killing temperature
    does NOT close the first-law gap; it is a separate candidate.

    Parameters
    ----------
    T_Killing_ratio:
        T_Killing / T_Hawking from this module.
    T_1stlaw_ratio:
        T_1stlaw / T_Hawking from Appendix I option (b).  Default: 9.0.
    """
    ratio = T_Killing_ratio / T_1stlaw_ratio if T_1stlaw_ratio > 0 else float("nan")
    gap_fraction = abs(T_Killing_ratio - T_1stlaw_ratio) / T_1stlaw_ratio
    gap_closed = gap_fraction < 0.01

    verdict = (
        "NOT_CLOSED — T_Killing is {:.1f}x BELOW the first-law temperature "
        "target T_1stlaw = {} * T_Hawking. They are distinct candidates "
        "addressing different aspects of the thermodynamic sector.".format(
            1.0 / ratio if ratio > 0 else float("inf"),
            T_1stlaw_ratio,
        )
    )

    notes = [
        f"T_Killing / T_Hawking  = {T_Killing_ratio:.4f}",
        f"T_1stlaw  / T_Hawking  = {T_1stlaw_ratio:.4f}  [Appendix I, option b]",
        f"T_Killing / T_1stlaw   = {ratio:.4f}",
        f"Gap fraction           = {gap_fraction:.4f}",
        "Interpretation: T_Killing is a new temperature scale associated "
        "with the dynamical metric horizon; T_1stlaw is a thermostatic "
        "requirement from the first law. They coexist as independent "
        "constraints on the temperature structure of the GRUT interior.",
    ]

    return FirstLawCrossCheck(
        T_Killing_over_T_Hawking=T_Killing_ratio,
        T_1stlaw_over_T_Hawking=T_1stlaw_ratio,
        ratio_T_Killing_to_1stlaw=ratio,
        gap_closed=gap_closed,
        gap_fraction=gap_fraction,
        verdict=verdict,
        notes=notes,
    )


# ================================================================
# Master audit
# ================================================================

def run_interior_metric_closure(
    M_ref_SI: float = 30.0 * M_SUN_KG,
) -> InteriorMetricClosureResult:
    """Run the complete interior metric closure analysis.

    Parameters
    ----------
    M_ref_SI:
        Physical mass for SI temperature evaluation.

    Returns
    -------
    InteriorMetricClosureResult
        Complete analysis.
    """
    layers = build_deficit_chain()
    A_crit_result = compute_A_crit()
    surface_gravity = compute_surface_gravity(
        A_crit_sq=A_crit_result.A_crit_sq,
        M_SI=M_ref_SI,
    )
    transient_caveat = build_transient_caveat()
    first_law_cross_check = compute_first_law_cross_check(
        T_Killing_ratio=surface_gravity.T_Killing_over_T_Hawking,
    )

    diagnostics = {
        "alpha_vac": ALPHA_VAC,
        "beta_Q": BETA_Q,
        "epsilon_Q": EPSILON_Q,
        "R_eq_over_r_s": float(R_EQ),
        "M_EXT": M_EXT,
        "tau_sq": TAU_SQ,
        "A_SCHW": A_SCHW,
        "A_eff_constitutive": A_EFF_CONSTITUTIVE,
        "f_static_at_R_eq": F_STATIC_AT_REQ,
        "m_static_at_R_eq": M_STATIC_AT_REQ,
        "f_at_A1": F_AT_A1,
        "A_crit_exact": A_CRIT_EXACT,
        "A_crit_numerical_locked": A_CRIT_NUMERICAL,
        "kappa_GRUT": KAPPA_GRUT,
        "kappa_Schw": KAPPA_SCHW,
        "kappa_ratio": KAPPA_RATIO,
        "T_Killing_over_T_Hawking": T_KILLING_OVER_T_HAWKING,
        "n_layers": len(layers),
        "n_forbidden_claims": len(FORBIDDEN_CLAIMS),
    }

    nonclaims = [
        "T_Killing is NOT proven to be the physical temperature of the GRUT interior",
        "The transient Killing horizon is NOT a permanent equilibrium",
        "A_crit > 1 is NOT shown to be physically realised; it is a threshold",
        "The first-law gap (Appendix I) is NOT closed by T_Killing",
        "Ghost-free status of the Galley route is NOT addressed here",
        "All Appendix C quantum blockers remain in force",
        "Hawking radiation is NOT derived",
        "Information paradox is NOT addressed",
    ]

    return InteriorMetricClosureResult(
        valid=True,
        layers=layers,
        A_crit_result=A_crit_result,
        surface_gravity=surface_gravity,
        transient_caveat=transient_caveat,
        first_law_cross_check=first_law_cross_check,
        executive=(
            "interior_metric_positivity_achievable_transient_supercritical_processing"
        ),
        nonclaims=nonclaims,
        forbidden_claims=FORBIDDEN_CLAIMS,
        diagnostics=diagnostics,
    )


# ================================================================
# Analytical identities (for tests)
# ================================================================

def check_layer_3a_cancellation(
    M: float = M_EXT,
    tau_sq: float = TAU_SQ,
    n_points: int = 100,
) -> Dict[str, Any]:
    """Verify that at A = 1 the kinetic term exactly cancels rho_eq.

    rho_eq    = -M^2 / (2 * tau^2 * r^4)
    epsilon   =  0.5 * Phi_dot^2 = 0.5 * (M/(tau*r^2))^2 = M^2/(2*tau^2*r^4)
    rho_total = rho_eq + epsilon = 0

    Returns a dict with 'max_residual' and 'cancellation_exact'.
    """
    import math as _math
    r_min = 0.05
    r_max = 3.0
    max_residual = 0.0
    for i in range(n_points):
        r = r_min + (r_max - r_min) * i / (n_points - 1)
        r4 = r ** 4
        rho_eq = -M * M / (2.0 * tau_sq * r4)
        epsilon_A1 = M * M / (2.0 * tau_sq * r4)
        rho_total = rho_eq + epsilon_A1
        max_residual = max(max_residual, abs(rho_total))

    return {
        "max_residual": max_residual,
        "cancellation_exact": max_residual < 1e-14,
    }


def verify_f_static_at_A0(
    M: float = M_EXT,
    R_eq: float = R_EQ,
    R_ext: float = R_EXT_CANONICAL,
    tau_sq: float = TAU_SQ,
) -> Dict[str, Any]:
    """Verify that A = 0 reproduces the locked static TOV value f = -17.71.

    Mass formula (integrating inward from R_ext to R_eq):

      m(R_eq, A) = M - 2*pi*M^2*(A^2-1)/tau^2 * (1/R_eq - 1/R_ext)

    Let delta_m_nat = 2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext)  [positive]

    Then m(R_eq, A) = M - delta_m_nat * (A^2 - 1)

    At A = 0: m(R_eq, 0) = M - delta_m_nat * (-1) = M + delta_m_nat

      f(R_eq) = 1 - 2*m(R_eq)/R_eq
    """
    coeff = 2.0 * math.pi * M * M / tau_sq
    delta_m_nat = coeff * (1.0 / R_eq - 1.0 / R_ext)   # positive
    # A = 0: (A^2 - 1) = -1, so correction is +delta_m_nat
    m_at_req = M - delta_m_nat * (0.0 ** 2 - 1.0)   # = M + delta_m_nat
    f_at_req = 1.0 - 2.0 * m_at_req / R_eq

    return {
        "coeff": coeff,
        "delta_m_nat": delta_m_nat,
        "m_at_R_eq_A0": m_at_req,
        "f_at_R_eq_A0": f_at_req,
        "locked_m": M_STATIC_AT_REQ,
        "locked_f": F_STATIC_AT_REQ,
        "m_consistent": abs(m_at_req - M_STATIC_AT_REQ) / abs(M_STATIC_AT_REQ) < 0.01,
        "f_consistent": abs(f_at_req - F_STATIC_AT_REQ) / abs(F_STATIC_AT_REQ) < 0.01,
    }


def verify_f_at_A1(
    M: float = M_EXT,
    R_eq: float = R_EQ,
    R_ext: float = R_EXT_CANONICAL,
    tau_sq: float = TAU_SQ,
) -> Dict[str, Any]:
    """Verify A = 1 gives f(R_eq) = A_SCHW = -2."""
    coeff = 2.0 * math.pi * M * M / tau_sq
    delta_m_factor = coeff * (1.0 / R_eq - 1.0 / R_ext)
    A = 1.0
    m_at_req = M + delta_m_factor * (A ** 2 - 1.0)   # = M (since A^2-1=0)
    f_at_req = 1.0 - 2.0 * m_at_req / R_eq
    a_schw = 1.0 - 2.0 * M / R_eq

    return {
        "m_at_R_eq_A1": m_at_req,
        "f_at_R_eq_A1": f_at_req,
        "A_SCHW": a_schw,
        "consistent": abs(f_at_req - a_schw) < 1e-14,
    }


def verify_kappa_ratio(
    A_crit_sq: float = A_CRIT_EXACT_SQ,
    M: float = M_EXT,
    R_eq: float = R_EQ,
    tau_sq: float = TAU_SQ,
) -> Dict[str, Any]:
    """Verify kappa_GRUT/kappa_Schw = 3/5 analytically.

    The exact ratio:
      kappa_GRUT = (1/2) * [1 - 4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq)] / R_eq
      kappa_Schw = 1/(4*M)

    With A_crit^2 - 1 = 2/(5*pi), M = 1/2, tau^2 = 3/2, R_eq = 1/3:
      4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq) = 4/5
      f'(R_eq) = (1 - 4/5)/(1/3) = 3/5
      kappa_GRUT = 3/10
      kappa_Schw = 1/2
      ratio = 3/5
    """
    factor = 4.0 * math.pi * M * M * (A_crit_sq - 1.0) / (tau_sq * R_eq)
    f_prime = (1.0 - factor) / R_eq
    kappa_grut = 0.5 * f_prime
    kappa_schw = 0.5 / (2.0 * M)
    ratio = kappa_grut / kappa_schw

    return {
        "factor_4pi_M2_etc": factor,
        "f_prime": f_prime,
        "kappa_GRUT": kappa_grut,
        "kappa_Schw": kappa_schw,
        "ratio": ratio,
        "expected_ratio": 3.0 / 5.0,
        "exact_3_5": abs(ratio - 3.0 / 5.0) < 1e-12,
        "T_Killing_over_T_Hawking": ratio,  # same ratio
    }
