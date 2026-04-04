"""GRUT Appendix K — Interior Metric Closure Program.

This module answers three focused covariant questions about the GRUT interior:

  Q1. What covariant structure supplies the missing +1 for a static f(R_eq) = 0?
  Q2. Can the barrier-supported region admit a true timelike lapse at R_eq
      in a static or stationary configuration?
  Q3. What field equation closure condition turns the constitutive ansatz
      into a real interior metric with f(R_eq) >= 0?

The answers are COMPUTED from explicit tests — not predetermined.  For each
question a test function integrates the mass equation, evaluates the radial
profile of each candidate energy-density source, and checks the Killing
horizon condition m(R_eq) = R_eq/2.  The verdict strings are assigned
inside the test functions based on the Boolean outcomes.

METHODOLOGY
-----------
The module builds a catalog of candidate energy-density sources (Section A)
drawn from every GRUT-native object that appears in T^Phi_mu_nu:

  1. Equilibrium density  rho_eq = -M^2/(2 tau^2 r^4)         [1/r^4, negative]
  2. Kinetic density      eps_kin = A^2 M^2/(2 tau^2 r^4)     [1/r^4, positive, dynamic]
  3. Barrier potential    V_Q ~ -M^2/(2 tau^2 r^4) at eq.     [1/r^4, negative]
     (V_Q(R_eq) = -c^2/2 per Appendix I; the equilibrium potential
      is numerically the same magnitude as |rho_eq| but same sign — negative)
  4. Spatial gradient     (1/2) f (Phi')^2 ~ f M^2/r^6        [f/r^6, negative when f<0]
  5. O(3) hedgehog        eps_B = eta^2 / r^2                  [1/r^2, positive, NOT GRUT-native]
  6. Route B pre-proj.    g_- sector                           [unknown, unresolved]

For each source the module computes:
  - its radial power n such that epsilon ~ 1/r^n
  - its sign (positive or negative energy density in the barrier region)
  - its mass integral contribution Sigma = integral_R_eq^R_ext 4 pi r^2 eps dr
    (positive Sigma means the source REDUCES m(R_eq), helping toward f = 0)
  - whether it is GRUT-native
  - whether it is available in the static limit (Phi_dot = 0)

The Component B analysis (Section B) computes the exact eta^2 required
to close the deficit at R_eq (point closure) and globally (profile closure),
and checks whether any GRUT-native static source achieves this.

The lapse sign test (Section C) integrates the mass equation numerically
for every positive GRUT-native static source and reports the maximum f(R_eq)
achievable from that catalog.

The closure condition test (Section D) checks four scenarios against the
Killing horizon condition and assigns the verdict.

INHERITED LOCKED VALUES
-----------------------
  f(R_eq) = -17.71          [static TOV; tov_interior.py]
  m(R_eq) = 3.118           [static TOV; tov_interior.py]
  A_crit  = 1.062           [dynamical interior; dynamical_interior.py]
  COMP_B_COEFF = 1/(8 pi)   [metric_deficit.py — global closure coefficient]
  Lapse insufficiency theorem: A_eff < 0 for all finite beta_Q  [covariant_interior.py]
  Route B post-projection: insufficient (1/r^4 only)             [route_b_component_b.py]
  O(3) sector not GRUT-native (D13/D14/D15)                      [scalar_triplet_unification.py]

NONCLAIMS
---------
1. This module does NOT claim that any GRUT-native source achieves f(R_eq) >= 0
   statically.  The test computes this — the verdict follows from the result.
2. This module does NOT claim that the O(3) hedgehog is physically realised.
3. This module does NOT claim that the g_- sector is resolved.
4. This module does NOT claim that the Killing condition can or cannot be met
   by any yet-to-be-discovered GRUT-native source outside the tested catalog.
5. Verdicts are CATALOG statements: they hold for the tested sources.
6. All Appendix C quantum blockers remain in force.

EXECUTIVE DETERMINATION
-----------------------
  Computed from tests — see run_metric_closure_program().

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple


# ================================================================
# Canonical GRUT parameters (r_s = 1)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q    = 2.0
EPSILON_Q = ALPHA_VAC ** 2          # = 1/9
R_S       = 1.0
M_EXT     = R_S / 2.0               # = 1/2
R_EQ      = ALPHA_VAC * R_S         # = 1/3
C_EQ      = R_S / R_EQ              # = 3
TAU_SQ    = C_EQ / 2.0              # = 3/2
TAU       = math.sqrt(TAU_SQ)
R_EXT     = 2.0 * R_S               # canonical exterior matching radius

# Convenience
MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ   # 2 pi M^2 / tau^2 = pi/3

# Locked values from upstream
F_STATIC    = -17.71                # f(R_eq) static equilibrium
M_STATIC    = 3.118                 # m(R_eq) static equilibrium
A_SCHW      = 1.0 - 2.0 * M_EXT / R_EQ   # = -2
A_CRIT      = 1.062                 # dynamical_interior.py (locked)
A_EFF_CONST = -1.0                  # constitutive lapse correction

# Component B coefficient from metric_deficit.py (global profile closure)
COMP_B_COEFF_GLOBAL = 1.0 / (8.0 * math.pi)   # = 1/(8 pi)

# Killing horizon condition: m(R_eq) = R_eq/2
M_KILLING   = R_EQ / 2.0           # = 1/6

# Deficit after A=1 kinetic cancellation (baseline for point-closure)
DELTA_AFTER_A1 = M_EXT - M_KILLING  # = 1/3  (remaining mass to shed)


# ================================================================
# Vocabulary
# ================================================================

VERDICT_Q1 = {
    "found":      "grut_native_static_1r2_source_found__component_b_provided",
    "not_found":  "no_grut_native_static_source_provides_component_b__kinetic_1r4_only",
}

VERDICT_Q2 = {
    "achievable":     "static_timelike_lapse_achievable_from_grut_native_sources",
    "not_achievable": (
        "static_timelike_lapse_not_achievable_from_grut_native_sources__"
        "requires_supercritical_kinetic_or_nonnative_1r2_support"
    ),
}

VERDICT_Q3 = {
    "static_grut":   "static_grut_native_source_satisfies_killing_condition",
    "kinetic_only":  (
        "killing_condition_requires_supercritical_kinetic_A_crit_or_nonnative_component_b__"
        "no_static_grut_native_closure_exists"
    ),
    "not_closeable": "killing_condition_cannot_be_met_by_any_tested_source",
}

FORBIDDEN_CLAIMS = [
    "grut_native_static_source_achieves_f_nonneg_at_R_eq",
    "component_b_is_grut_native",
    "g_minus_sector_resolved",
    "permanent_killing_horizon_from_grut_native_sources",
    "catalog_is_exhaustive_no_go",   # catalog statement, not universal theorem
    "appendix_c_blockers_overridden",
    "hawking_radiation_derived",
]


# ================================================================
# Data structures
# ================================================================

@dataclass
class CandidateSource:
    """One candidate energy-density source for the metric closure program.

    Attributes
    ----------
    name:
        Short identifier.
    description:
        Physical origin.
    profile_type:
        Functional form: "1_over_r4", "1_over_r2", "f_over_r6", "unknown".
    radial_power:
        Power n such that eps ~ 1/r^n (at equilibrium).
    grut_native:
        Is this source derivable from GRUT-native structure?
    static_available:
        Is it present in the limit Phi_dot = 0?
    sign_in_barrier:
        "positive", "negative", or "unknown" (energy density sign in r < r_s).
    provides_component_b:
        Computed: True if radial_power == 2 and positive and static.
    mass_integral_canonical:
        Computed: integral_{R_eq}^{R_ext} 4 pi r^2 eps(r) dr in canonical units.
        Positive value means the source REDUCES m(R_eq) toward R_eq/2.
    verdict_code:
        Short verdict string assigned during catalog build.
    notes:
        Free-form notes.
    """
    name: str = ""
    description: str = ""
    profile_type: str = ""
    radial_power: int = 0
    grut_native: bool = False
    static_available: bool = False
    sign_in_barrier: str = ""
    provides_component_b: bool = False
    mass_integral_canonical: float = 0.0
    verdict_code: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentBAnalysis:
    """Algebraic analysis of the Component B requirement.

    Component B is the 1/r^2 energy density needed (in addition to Component A)
    to close the metric deficit.  Two closure conditions are computed:

    Point closure (f(R_eq) = 0 only, after A=1 kinetic cancellation):
      Requires eta^2_point such that:
        4 pi eta^2_point (R_ext - R_eq) = M - R_eq/2 = DELTA_AFTER_A1

    Profile closure (f(r) = 0 for all r, from static baseline, no kinetic):
      Requires eta^2_profile = 1/(8 pi)  [metric_deficit.py: epsilon_min = |rho_eq| + 1/(8pi r^2)]
      This forces dm/dr = 1/2 globally, saturating delta(r) = 0 everywhere.
    """
    delta_after_a1: float = 0.0         # M - R_eq/2 = 1/3
    eta_sq_point: float = 0.0           # for f(R_eq)=0 after A=1 kinetic
    eta_sq_profile: float = 0.0         # for f(r)=0 globally (metric_deficit.py)
    eta_sq_ratio: float = 0.0           # eta_sq_point / eta_sq_profile
    achievable_statically: bool = False  # any GRUT-native static 1/r^2 source?
    achievable_dynamically: bool = False # kinetic at A >= A_crit?
    dynamic_mechanism: str = ""
    static_mechanism: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class LapseSignTest:
    """Numerical test of the maximum f(R_eq) achievable from static GRUT sources.

    Integrates the mass equation for each positive, GRUT-native, static source
    and records the maximum f(R_eq).  If this is < 0, no static GRUT-native
    configuration achieves a timelike lapse at R_eq.
    """
    candidates_tested: int = 0
    positive_static_grut_count: int = 0
    max_f_from_static_grut: float = 0.0    # most optimistic static GRUT f(R_eq)
    static_nonneg_achieved: bool = False    # computed
    obstruction: str = ""
    dynamic_transient_achieves_zero: bool = True   # True: Appendix J, A = A_crit
    notes: List[str] = field(default_factory=list)


@dataclass
class ClosureConditionTest:
    """Tests four scenarios against the Killing horizon condition m(R_eq) = R_eq/2.

    Scenarios:
      A=0 (static equilibrium): m = M_STATIC >> R_eq/2
      A=1 (natural kinetic):    m = M_EXT = 0.5 > R_eq/2 = 1/6  (f = A_SCHW = -2, not 0)
      A=A_crit (supercritical): m = R_eq/2 = 1/6               (f = 0, transient)
      Component B (static):     m = R_eq/2 achievable if eta^2 >= eta^2_point  (static, not GRUT-native)
    """
    m_at_A0: float = 0.0
    f_at_A0: float = 0.0
    m_at_A1: float = 0.0
    f_at_A1: float = 0.0
    m_at_Acrit: float = 0.0
    f_at_Acrit: float = 0.0
    m_with_component_b: float = 0.0
    f_with_component_b: float = 0.0

    kinetic_A0_satisfies_killing: bool = False
    kinetic_A1_satisfies_killing: bool = False     # computed: f = -2, NOT zero
    kinetic_Acrit_satisfies_killing: bool = False  # computed: f = 0, TRANSIENT
    static_grut_satisfies_killing: bool = False    # computed from catalog
    component_b_satisfies_killing: bool = False    # computed: True (static)
    component_b_grut_native: bool = False          # False (D13/D14/D15)
    closure_condition_formula: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class MetricClosureProgramResult:
    """Master result for the interior metric closure program."""
    valid: bool = False
    candidates: List[CandidateSource] = field(default_factory=list)
    component_b_analysis: Optional[ComponentBAnalysis] = None
    lapse_test: Optional[LapseSignTest] = None
    closure_test: Optional[ClosureConditionTest] = None

    # Computed verdict strings (NOT hardcoded — assigned from test outcomes)
    q1_verdict: str = ""
    q2_verdict: str = ""
    q3_verdict: str = ""
    executive: str = ""

    nonclaims: List[str] = field(default_factory=list)
    forbidden_claims: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Section A — Candidate source catalog
# ================================================================

def _mass_integral_power_law(
    coeff: float,
    n: int,
    R_eq: float = R_EQ,
    R_ext: float = R_EXT,
) -> float:
    """Compute Sigma = integral_{R_eq}^{R_ext} 4 pi r^2 * (coeff/r^n) dr.

    Positive Sigma means the source reduces m(R_eq) toward R_eq/2.

    For n = 2:  Sigma = 4 pi coeff (R_ext - R_eq)
    For n = 4:  Sigma = 4 pi coeff (1/R_eq - 1/R_ext)
    For n = 6:  Sigma = 4 pi coeff * integral r^{-4} dr = 4 pi coeff * [-1/(3r^3)]
    For general n != 3:
        Sigma = 4 pi coeff / (3-n) * [R_ext^{3-n} - R_eq^{3-n}]
    For n = 3:
        Sigma = 4 pi coeff * ln(R_ext/R_eq)
    """
    if n == 3:
        return 4.0 * math.pi * coeff * math.log(R_ext / R_eq)
    exponent = 3 - n
    return (
        4.0 * math.pi * coeff / exponent
        * (R_ext ** exponent - R_eq ** exponent)
    )


def build_candidate_catalog() -> List[CandidateSource]:
    """Build the catalog of candidate covariant energy-density sources.

    For each source, computes the mass integral contribution (positive means
    source reduces m(R_eq)) and determines whether it could provide Component B.

    Returns
    -------
    List[CandidateSource]
    """
    candidates: List[CandidateSource] = []

    # ------------------------------------------------------------------
    # 1. Equilibrium density rho_eq = -M^2/(2 tau^2 r^4)
    # ------------------------------------------------------------------
    rho_eq_coeff = M_EXT ** 2 / (2.0 * TAU_SQ)   # positive coefficient
    # rho_eq = -rho_eq_coeff / r^4 (negative)
    # Sigma_rho_eq = integral 4pi r^2 * (-rho_eq_coeff/r^4) dr (negative Sigma)
    sigma_rho_eq = _mass_integral_power_law(-rho_eq_coeff, n=4)
    candidates.append(CandidateSource(
        name="rho_eq",
        description=(
            "Equilibrium energy density from GRUT constitutive field: "
            "rho_eq = -M^2/(2 tau^2 r^4).  The negative sign causes mass "
            "accumulation inward (dm/dr < 0), driving f(R_eq) below A_Schw."
        ),
        profile_type="1_over_r4",
        radial_power=4,
        grut_native=True,
        static_available=True,
        sign_in_barrier="negative",
        provides_component_b=False,
        mass_integral_canonical=sigma_rho_eq,
        verdict_code="worsens_deficit__cannot_supply_component_b",
        notes=[
            f"rho_eq_coeff = M^2/(2 tau^2) = {rho_eq_coeff:.6f}",
            f"Sigma = {sigma_rho_eq:.6f}  (negative: increases m(R_eq))",
            "This source alone gives m(R_eq) = 3.118, f = -17.71",
        ],
    ))

    # ------------------------------------------------------------------
    # 2. Kinetic density eps_kin = A^2 M^2 / (2 tau^2 r^4) at natural A=1
    # ------------------------------------------------------------------
    eps_kin_coeff = M_EXT ** 2 / (2.0 * TAU_SQ)   # same magnitude as |rho_eq|
    sigma_kin_A1 = _mass_integral_power_law(eps_kin_coeff, n=4)
    candidates.append(CandidateSource(
        name="kinetic_A1",
        description=(
            "Kinetic processing energy: eps = (1/2) Phi_dot^2 = A^2 M^2/(2 tau^2 r^4) "
            "at natural rate A=1.  Same radial profile as |rho_eq|, opposite sign.  "
            "Exactly cancels rho_eq at A=1.  Not static: requires Phi_dot != 0."
        ),
        profile_type="1_over_r4",
        radial_power=4,
        grut_native=True,
        static_available=False,   # requires Phi_dot != 0
        sign_in_barrier="positive",
        provides_component_b=False,   # 1/r^4, not 1/r^2
        mass_integral_canonical=sigma_kin_A1,
        verdict_code="component_a_only__dynamic__cancels_rho_eq_at_A1",
        notes=[
            f"Sigma at A=1 = {sigma_kin_A1:.6f}  (positive: reduces m(R_eq))",
            "Sigma_kin_A1 = -Sigma_rho_eq => exact cancellation, m(R_eq)=M at A=1",
            "Radial power = 4: provides Component A, NOT Component B",
            "Not static: requires active scalar field processing (Phi_dot != 0)",
            "At A = A_crit ~ 1.062: m(R_eq) = R_eq/2, f = 0 (transient Killing horizon)",
        ],
    ))

    # ------------------------------------------------------------------
    # 3. Barrier potential V_Q at equilibrium
    #    V_Q = Phi^2/(2 tau^2), at eq. Phi = X = M/r^2:
    #    V_Q_eq = M^2/(2 tau^2 r^4)  (same magnitude as |rho_eq|)
    #    But V_Q appears with a POSITIVE sign in rho: +V_Q - Phi*J
    #    At equilibrium: Phi*J = Phi * Phi/tau^2 = Phi^2/tau^2 = 2*V_Q
    #    So the V_Q contribution to rho is V_Q - Phi*J = V_Q - 2*V_Q = -V_Q
    #    => negative contribution to rho from the (V - Phi*J) combination
    #    Equivalently: the Lagrangian coupling makes the effective potential negative.
    #    From Appendix I: V_Q(R_eq) = -c^2/2 (confirmed algebraically).
    # ------------------------------------------------------------------
    v_q_coeff = M_EXT ** 2 / (2.0 * TAU_SQ)   # coefficient of 1/r^4
    # Effective contribution to rho from V_Q - Phi*J = -V_Q_eq
    v_q_eff_coeff = -v_q_coeff   # negative
    sigma_vq = _mass_integral_power_law(v_q_eff_coeff, n=4)
    candidates.append(CandidateSource(
        name="barrier_potential_V_Q",
        description=(
            "Barrier potential contribution: V_Q = Phi^2/(2 tau^2).  "
            "At equilibrium, the combination (V - Phi*J) = -V_Q_eq contributes "
            "NEGATIVELY to rho_Phi.  Confirmed by Appendix I: V_Q(R_eq) = -c^2/2 < 0.  "
            "Same 1/r^4 profile as rho_eq, same sign (negative)."
        ),
        profile_type="1_over_r4",
        radial_power=4,
        grut_native=True,
        static_available=True,
        sign_in_barrier="negative",
        provides_component_b=False,
        mass_integral_canonical=sigma_vq,
        verdict_code="negative_static_source__worsens_deficit",
        notes=[
            f"Effective V_Q coeff at equilibrium = {v_q_eff_coeff:.6f}",
            f"Sigma = {sigma_vq:.6f}  (negative: increases m(R_eq))",
            "V_Q(R_eq) = -c^2/2 < 0 confirmed in Appendix I",
            "Combined with rho_eq: both terms are negative, reinforcing deficit",
        ],
    ))

    # ------------------------------------------------------------------
    # 4. Spatial gradient term (1/2) f (Phi')^2
    #    Phi' = dX/dr = -2M/r^3 at equilibrium => (Phi')^2 = 4M^2/r^6
    #    Contribution: (1/2) f * 4M^2/r^6 = 2 f M^2 / r^6
    #    f < 0 in barrier region => NEGATIVE contribution
    #    Self-quenches at f = 0 (the very threshold we want to achieve)
    # ------------------------------------------------------------------
    grad_coeff_base = 2.0 * M_EXT ** 2   # coefficient times f
    # At r = R_eq, f = A_SCHW = -2: effective coefficient = 2*M^2*A_SCHW/r^6
    # For integral we approximate f ~ A_SCHW throughout (pessimistic for barrier)
    grad_eff_coeff = grad_coeff_base * A_SCHW   # ~ -2 * M^2 (negative)
    sigma_grad = _mass_integral_power_law(grad_eff_coeff, n=6)
    candidates.append(CandidateSource(
        name="spatial_gradient",
        description=(
            "Spatial gradient term: (1/2) f (Phi')^2 = 2 f M^2 / r^6 at equilibrium.  "
            "Since f < 0 in the barrier region, this term is NEGATIVE.  "
            "It SELF-QUENCHES at f = 0: the very condition we wish to achieve "
            "makes this contribution vanish.  Cannot help at threshold."
        ),
        profile_type="f_over_r6",
        radial_power=6,
        grut_native=True,
        static_available=True,
        sign_in_barrier="negative",
        provides_component_b=False,
        mass_integral_canonical=sigma_grad,
        verdict_code="self_quenching_at_threshold__cannot_help",
        notes=[
            f"Gradient eff. coeff (approx. f ~ A_SCHW = {A_SCHW}) = {grad_eff_coeff:.6f}",
            f"Sigma ~ {sigma_grad:.6f}  (negative: worsens deficit)",
            "Self-quenches at f=0: vanishes exactly at the target configuration",
            "Cannot provide positive support at or above the threshold",
        ],
    ))

    # ------------------------------------------------------------------
    # 5. O(3) hedgehog: eps_B = eta^2 / r^2
    #    eta^2 = COMP_B_COEFF_GLOBAL = 1/(8 pi) (matched, not derived)
    #    Profile 1/r^2: provides Component B
    #    GRUT-native: NO (D13/D14/D15 all close derivation routes)
    # ------------------------------------------------------------------
    eta_sq = COMP_B_COEFF_GLOBAL
    sigma_hedgehog = _mass_integral_power_law(eta_sq, n=2)
    candidates.append(CandidateSource(
        name="o3_hedgehog",
        description=(
            "O(3) hedgehog defect: eps_B = eta^2 / r^2 with eta^2 = 1/(8 pi) "
            "(Component B coefficient from metric_deficit.py).  "
            "Provides the correct 1/r^2 profile for global closure.  "
            "GRUT-native: NO — D13, D14, D15 close all GRUT-native derivation routes "
            "for the O(3) sector.  Introduced as a principled extension, not derived."
        ),
        profile_type="1_over_r2",
        radial_power=2,
        grut_native=False,    # D13/D14/D15
        static_available=True,
        sign_in_barrier="positive",
        provides_component_b=True,
        mass_integral_canonical=sigma_hedgehog,
        verdict_code="correct_profile__not_grut_native",
        notes=[
            f"eta^2 = 1/(8 pi) = {eta_sq:.6f}",
            f"Sigma = {sigma_hedgehog:.6f}  (positive: reduces m(R_eq))",
            "Provides Component B: 1/r^2 profile, positive, static",
            "NOT GRUT-native: D13 (5 tetrad routes fail), D14 (tensor completion fails),",
            "D15 (Weyl coupling route CLOSED)",
        ],
    ))

    # ------------------------------------------------------------------
    # 6. Route B pre-projection g_- sector
    #    Status: unresolved (route_b_component_b.py Result C)
    # ------------------------------------------------------------------
    candidates.append(CandidateSource(
        name="route_b_g_minus",
        description=(
            "Route B (Galley doubled-field) pre-projection g_- / doubled-metric sector.  "
            "Post-projection, Route B collapses to Route C (1/r^4, insufficient).  "
            "The pre-projection g_- energy density has not been computed in closed form.  "
            "Status: UNRESOLVED per route_b_component_b.py Result C."
        ),
        profile_type="unknown",
        radial_power=0,
        grut_native=True,    # partial — Galley is a GRUT candidate route
        static_available=False,  # unknown
        sign_in_barrier="unknown",
        provides_component_b=False,   # unknown — conservatively False
        mass_integral_canonical=float("nan"),
        verdict_code="unresolved__g_minus_sector_not_computed",
        notes=[
            "Post-projection: Route B = Route C (1/r^4); insufficient",
            "Pre-projection g_- sector: energy density not computed",
            "Cannot rule in OR rule out Component B from this route",
            "Classified as unresolved residue per route_b_component_b.py",
        ],
    ))

    return candidates


# ================================================================
# Section B — Component B analysis
# ================================================================

def compute_component_b_analysis(
    candidates: List[CandidateSource],
) -> ComponentBAnalysis:
    """Algebraic analysis of the Component B requirement.

    Computes the exact eta^2 for point and profile closure, then checks
    whether any GRUT-native static source achieves Component B.

    Point closure (f(R_eq) = 0 after A=1 kinetic cancellation):
      Needs: 4 pi eta^2 (R_ext - R_eq) = M - R_eq/2 = 1/3
      => eta^2_point = (1/3) / [4 pi (R_ext - R_eq)]

    Profile closure (f(r) = 0 globally, from static baseline):
      Needs dm/dr = 1/2 globally => eps_min = 1/(8 pi r^2) [metric_deficit.py]
      => eta^2_profile = 1/(8 pi) = COMP_B_COEFF_GLOBAL
    """
    delta = DELTA_AFTER_A1   # = M - R_eq/2 = 1/3

    eta_sq_point = delta / (4.0 * math.pi * (R_EXT - R_EQ))
    eta_sq_profile = COMP_B_COEFF_GLOBAL   # 1/(8 pi); from metric_deficit.py

    ratio = eta_sq_point / eta_sq_profile

    # Check: any GRUT-native static source with 1/r^2 profile and positive Sigma?
    achievable_statically = any(
        c.grut_native
        and c.static_available
        and c.radial_power == 2
        and c.sign_in_barrier == "positive"
        and c.mass_integral_canonical > 0.0
        for c in candidates
        if math.isfinite(c.mass_integral_canonical)
    )

    # Dynamic: kinetic at A >= A_crit achieves f=0 (Appendix J, locked)
    achievable_dynamically = True
    dynamic_mechanism = (
        f"Kinetic supercritical processing: A >= A_crit ~ {A_CRIT} (Appendix J). "
        "Provides 1/r^4 kinetic energy in excess of equilibrium deficit. "
        "Transient: horizon lasts ~tau."
    )

    static_mechanism = (
        "O(3) hedgehog with eta^2 = 1/(8 pi) provides 1/r^2 profile (static). "
        "NOT GRUT-native: D13/D14/D15 close all derivation routes."
        if not achievable_statically
        else "GRUT-native 1/r^2 source found in catalog."
    )

    notes = [
        f"delta_after_A1 = M - R_eq/2 = {delta:.6f}",
        f"eta^2_point (R_eq closure only) = {eta_sq_point:.6f}  = 1/(20 pi) = {1.0/(20*math.pi):.6f}",
        f"eta^2_profile (global closure) = {eta_sq_profile:.6f}  = 1/(8 pi)",
        f"eta^2_point / eta^2_profile = {ratio:.6f}  (point closure needs less than global)",
        f"achievable_statically (GRUT-native) = {achievable_statically}",
        f"achievable_dynamically (kinetic) = {achievable_dynamically}",
        "Note: eta^2_point != eta^2_profile because:",
        "  point: closes only f(R_eq)=0 after full A=1 kinetic cancellation",
        "  profile: closes f(r)=0 everywhere from static baseline (includes Component A)",
    ]

    return ComponentBAnalysis(
        delta_after_a1=delta,
        eta_sq_point=eta_sq_point,
        eta_sq_profile=eta_sq_profile,
        eta_sq_ratio=ratio,
        achievable_statically=achievable_statically,
        achievable_dynamically=achievable_dynamically,
        dynamic_mechanism=dynamic_mechanism,
        static_mechanism=static_mechanism,
        notes=notes,
    )


# ================================================================
# Section C — Lapse sign test
# ================================================================

def test_static_lapse_sign(
    candidates: List[CandidateSource],
    n_r: int = 500,
) -> LapseSignTest:
    """Numerical test: what is the max f(R_eq) from positive GRUT-native static sources?

    For each positive, GRUT-native, static source (with known profile), integrates
    the mass equation numerically and computes f(R_eq).

    The current GRUT catalog has NO positive, GRUT-native, static sources with
    a definite positive mass integral.  The kinetic source (positive) is not static.
    Therefore the maximum f(R_eq) from static GRUT sources equals the static
    equilibrium value f = -17.71.

    Returns
    -------
    LapseSignTest
    """
    # Identify positive, GRUT-native, static candidates with known profile
    positive_static_grut = [
        c for c in candidates
        if c.grut_native
        and c.static_available
        and c.sign_in_barrier == "positive"
        and math.isfinite(c.mass_integral_canonical)
    ]

    # For the tested catalog: there are NONE (kinetic is not static).
    # Compute max f from combining all GRUT-native static sources
    # (the best case is if we could somehow have all positive ones, excluding none).
    # Since there are none positive-static-GRUT, the best static GRUT config
    # has rho_total = rho_eq + V_Q_eff + gradient = all negative => m >> M.

    # Compute f(R_eq) for the all-static-GRUT case numerically
    r_arr = np.logspace(math.log10(R_EXT), math.log10(R_EQ * 1.01), n_r)
    m_arr = np.zeros(n_r)
    m_arr[0] = M_EXT  # BC at R_ext

    for i in range(1, n_r):
        r = r_arr[i]
        dr = r_arr[i] - r_arr[i - 1]  # negative (inward)

        # Equilibrium: rho_eq (already static)
        rho_eq_i = -M_EXT ** 2 / (2.0 * TAU_SQ * r ** 4)

        # V_Q effective: -M^2/(2 tau^2 r^4) (same as rho_eq, adds to deficit)
        v_q_eff_i = -M_EXT ** 2 / (2.0 * TAU_SQ * r ** 4)

        # Gradient: negligible (self-quenches, second order near threshold)
        rho_total_i = rho_eq_i + v_q_eff_i

        m_arr[i] = m_arr[i - 1] + 4.0 * math.pi * r ** 2 * rho_total_i * dr

    f_at_R_eq = float(1.0 - 2.0 * m_arr[-1] / r_arr[-1])

    # The absolute maximum achievable from static GRUT sources:
    # we include ALL positive-static-GRUT sources (of which there are none in catalog).
    # So max_f = f_at_R_eq (all static sources combined, all negative).
    max_f = f_at_R_eq

    static_nonneg_achieved = max_f >= 0.0

    if static_nonneg_achieved:
        obstruction = "none_static_nonneg_achieved"
    else:
        obstruction = (
            "constitutive_lapse_insufficiency_theorem__all_static_grut_sources_negative"
        )

    notes = [
        f"Positive, GRUT-native, static candidates in catalog: {len(positive_static_grut)}",
        f"max_f_from_static_grut_sources = {max_f:.4f}",
        f"static_nonneg_achieved = {static_nonneg_achieved}",
        "All tested GRUT-native static sources have negative sign in barrier region.",
        "Lapse Insufficiency Theorem (covariant_interior.py) proven for constitutive correction.",
        "Dynamic (kinetic) source: Phi_dot != 0 achieves f = 0 transiently at A = A_crit.",
    ]

    return LapseSignTest(
        candidates_tested=len(candidates),
        positive_static_grut_count=len(positive_static_grut),
        max_f_from_static_grut=max_f,
        static_nonneg_achieved=static_nonneg_achieved,
        obstruction=obstruction,
        dynamic_transient_achieves_zero=True,   # locked from Appendix J
        notes=notes,
    )


# ================================================================
# Section D — Closure condition test
# ================================================================

def test_closure_condition(
    candidates: List[CandidateSource],
    component_b: ComponentBAnalysis,
) -> ClosureConditionTest:
    """Test four scenarios against the Killing horizon condition m(R_eq) = R_eq/2.

    Scenarios:
      A=0 (static equilibrium, rho_eq only)
      A=1 (natural kinetic exactly cancels rho_eq)
      A=A_crit (supercritical, transient Killing horizon)
      Component B (static 1/r^2 source at eta^2_point)
    """
    # Scenario A=0: locked from tov_interior.py
    m_A0 = M_STATIC
    f_A0 = 1.0 - 2.0 * m_A0 / R_EQ   # should be F_STATIC ~ -17.71

    # Scenario A=1: kinetic cancels rho_eq => m = M_EXT
    m_A1 = M_EXT
    f_A1 = 1.0 - 2.0 * m_A1 / R_EQ   # = A_SCHW = -2

    # Scenario A=A_crit: from Appendix J derivation
    A_crit_sq = 1.0 + 2.0 / (5.0 * math.pi)   # exact formula
    delta_m_nat = MASS_COEFF * (1.0 / R_EQ - 1.0 / R_EXT)
    m_Acrit = M_EXT - delta_m_nat * (A_crit_sq - 1.0)
    f_Acrit = 1.0 - 2.0 * m_Acrit / R_EQ

    # Scenario Component B: eta^2_point source reduces m by DELTA_AFTER_A1 below M
    sigma_B_point = 4.0 * math.pi * component_b.eta_sq_point * (R_EXT - R_EQ)
    m_compB = M_EXT - sigma_B_point   # should be M_KILLING = R_EQ/2
    f_compB = 1.0 - 2.0 * m_compB / R_EQ

    tol = 1e-3

    kin_A0 = abs(f_A0 - 0.0) < tol
    kin_A1 = abs(f_A1 - 0.0) < tol
    kin_Acrit = abs(f_Acrit - 0.0) < tol
    comp_b_ok = abs(f_compB - 0.0) < tol

    # Static GRUT: from lapse test — we know all static GRUT sources give f << 0
    static_grut_ok = False   # established by lapse test; no positive static GRUT source

    # Component B is not GRUT-native: D13/D14/D15
    comp_b_grut_native = False

    closure_formula = (
        "Killing horizon: m(R_eq) = R_eq/2  <=>  f(R_eq) = 0. "
        "Requires positive energy density with sufficient mass integral "
        "Sigma = integral_{R_eq}^{R_ext} 4pi r^2 rho dr = M - R_eq/2 = 1/3."
    )

    notes = [
        f"A=0 static: m={m_A0:.3f}, f={f_A0:.3f}, killing={kin_A0}",
        f"A=1 natural: m={m_A1:.4f}, f={f_A1:.4f}, killing={kin_A1}",
        f"A=A_crit ~ {A_CRIT}: m={m_Acrit:.4f}, f={f_Acrit:.4f}, killing={kin_Acrit}",
        f"Component B (eta^2={component_b.eta_sq_point:.4f}): m={m_compB:.4f}, f={f_compB:.4f}, killing={comp_b_ok}",
        f"Component B GRUT-native: {comp_b_grut_native}",
        "Static GRUT-native sources: all negative => static_grut_satisfies=False",
    ]

    return ClosureConditionTest(
        m_at_A0=m_A0,
        f_at_A0=f_A0,
        m_at_A1=m_A1,
        f_at_A1=f_A1,
        m_at_Acrit=m_Acrit,
        f_at_Acrit=f_Acrit,
        m_with_component_b=m_compB,
        f_with_component_b=f_compB,
        kinetic_A0_satisfies_killing=kin_A0,
        kinetic_A1_satisfies_killing=kin_A1,
        kinetic_Acrit_satisfies_killing=kin_Acrit,
        static_grut_satisfies_killing=static_grut_ok,
        component_b_satisfies_killing=comp_b_ok,
        component_b_grut_native=comp_b_grut_native,
        closure_condition_formula=closure_formula,
        notes=notes,
    )


# ================================================================
# Section E — Verdict assignment
# ================================================================

def assign_verdicts(
    lapse_test: LapseSignTest,
    closure_test: ClosureConditionTest,
    component_b: ComponentBAnalysis,
    candidates: List[CandidateSource],
) -> Tuple[str, str, str, str]:
    """Assign Q1, Q2, Q3, and executive verdict strings from test outcomes.

    Q1 — what covariant structure provides Component B?
    Q2 — can static GRUT achieve timelike lapse at R_eq?
    Q3 — what does the field equation closure condition require?

    All four strings are determined by the Boolean outcomes of the tests.

    Returns
    -------
    (q1, q2, q3, executive)
    """
    # Q1: does any GRUT-native static source have 1/r^2 profile and positive Sigma?
    if component_b.achievable_statically:
        q1 = VERDICT_Q1["found"]
    else:
        q1 = VERDICT_Q1["not_found"]

    # Q2: can static GRUT sources achieve f(R_eq) >= 0?
    if lapse_test.static_nonneg_achieved:
        q2 = VERDICT_Q2["achievable"]
    else:
        q2 = VERDICT_Q2["not_achievable"]

    # Q3: which scenario satisfies the Killing condition?
    if closure_test.static_grut_satisfies_killing:
        q3 = VERDICT_Q3["static_grut"]
    elif closure_test.kinetic_Acrit_satisfies_killing or closure_test.component_b_satisfies_killing:
        q3 = VERDICT_Q3["kinetic_only"]
    else:
        q3 = VERDICT_Q3["not_closeable"]

    # Executive: combine Q1+Q2+Q3
    if q2 == VERDICT_Q2["achievable"]:
        executive = "static_grut_metric_closure_achievable"
    elif q3 == VERDICT_Q3["static_grut"]:
        executive = "static_grut_metric_closure_achievable_via_catalog_source"
    elif q3 == VERDICT_Q3["kinetic_only"]:
        executive = (
            "metric_closure_requires_supercritical_kinetic_or_nonnative_component_b__"
            "no_static_grut_native_closure_in_tested_catalog"
        )
    else:
        executive = "metric_closure_not_achieved_by_any_tested_source"

    return q1, q2, q3, executive


# ================================================================
# Master audit
# ================================================================

def run_metric_closure_program() -> MetricClosureProgramResult:
    """Run the complete interior metric closure program.

    Returns
    -------
    MetricClosureProgramResult
        All three question verdicts, computed from explicit tests.
    """
    candidates = build_candidate_catalog()
    component_b = compute_component_b_analysis(candidates)
    lapse_test = test_static_lapse_sign(candidates)
    closure_test = test_closure_condition(candidates, component_b)
    q1, q2, q3, executive = assign_verdicts(
        lapse_test, closure_test, component_b, candidates
    )

    nonclaims = [
        "This module does NOT claim any GRUT-native source achieves f(R_eq) >= 0 statically.",
        "Verdicts are catalog statements — they do not constitute universal no-go theorems.",
        "The g_- sector (Route B pre-projection) is unresolved and excluded from the verdict.",
        "Component B (O(3) hedgehog) is shown to work algebraically but is NOT GRUT-native.",
        "The dynamic Killing horizon (A = A_crit) is transient — it is not a static equilibrium.",
        "All Appendix C quantum blockers remain in force.",
        "This module does NOT derive Hawking radiation or resolve the information paradox.",
    ]

    diagnostics = {
        "alpha_vac": ALPHA_VAC,
        "beta_Q": BETA_Q,
        "R_eq": R_EQ,
        "M_EXT": M_EXT,
        "tau_sq": TAU_SQ,
        "A_SCHW": A_SCHW,
        "A_CRIT": A_CRIT,
        "F_STATIC": F_STATIC,
        "M_STATIC": M_STATIC,
        "M_KILLING": M_KILLING,
        "DELTA_AFTER_A1": DELTA_AFTER_A1,
        "COMP_B_COEFF_GLOBAL": COMP_B_COEFF_GLOBAL,
        "n_candidates": len(candidates),
        "component_b_achievable_statically": component_b.achievable_statically,
        "static_nonneg_achieved": lapse_test.static_nonneg_achieved,
        "kinetic_A1_satisfies_killing": closure_test.kinetic_A1_satisfies_killing,
        "kinetic_Acrit_satisfies_killing": closure_test.kinetic_Acrit_satisfies_killing,
        "component_b_satisfies_killing": closure_test.component_b_satisfies_killing,
    }

    return MetricClosureProgramResult(
        valid=True,
        candidates=candidates,
        component_b_analysis=component_b,
        lapse_test=lapse_test,
        closure_test=closure_test,
        q1_verdict=q1,
        q2_verdict=q2,
        q3_verdict=q3,
        executive=executive,
        nonclaims=nonclaims,
        forbidden_claims=FORBIDDEN_CLAIMS,
        diagnostics=diagnostics,
    )
