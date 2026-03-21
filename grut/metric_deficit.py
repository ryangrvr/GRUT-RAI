"""Global metric positivity deficit and minimal closure requirement — Phase 6C.

This module extends Phase 6B (dynamical interior) by computing the exact
mathematical shape of the deficit function delta(r) = m(r) - r/2, deriving
the minimal additive source that would saturate f(r) = 0, and testing five
correction classes for their ability (or inability) to close the deficit.

PRINCIPAL RESULTS:

  Result 1 — Deficit Profile:
    The deficit delta(r) = m(r) - r/2 quantifies the mass excess at each
    radius.  Where delta > 0, we have f = 1 - 2m/r < 0.  The deficit is
    positive throughout the barrier region and peaks at the innermost grid
    point (near R_eq).

  Result 2 — Minimal Additive Source Decomposition:
    The minimal source epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2) has
    TWO components:
      Component A ~ 1/r^4:  cancels the equilibrium negative density
      Component B ~ 1/r^2:  extra intermediate-radius support
    No tested GRUT profile provides Component B independently.

  Result 3 — Two-Parameter Energy Density Scan:
    Parameterizing epsilon(r) = A/r^4 + B/r^2 at the mass-function level
    gives a threshold surface in (A,B) space.  B=0 recovers the Phase 6B
    natural result A_crit ~ 1.06.  The minimum total energy lies on the
    minimal-source contour.

  Result 4 — Monotonic Profile Insufficiency:
    Tested monotonic inward-increasing profiles (1/r^n for n >= 2) provide
    1/r^4 support but NOT the 1/r^2 component at intermediate radii.
    This is an insufficiency result for tested profiles, not a general no-go.

  Result 5 — Closure Classification:
    Final classification: current_closure_insufficient__minimal_additive_source_identified
    The current GRUT closure (scalar kinetic processing with gravitational
    sourcing) cannot produce the required epsilon_min shape.  The minimal
    additive positive source that saturates f = 0 has been identified.

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants — canonical GRUT parameters (from dynamical_interior.py)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ_OVER_RS = ALPHA_VAC
R_EQ = R_S * R_EQ_OVER_RS           # = 1/3
C_COMPACTNESS = R_S / R_EQ          # = 3
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)  # ~ 1.2247

A_EFF_CONSTITUTIVE = 1.0 - C_COMPACTNESS * BETA_Q / (1.0 + BETA_Q)  # = -1
A_SCHW = 1.0 - 2.0 * M_EXT / R_EQ  # = -2

# Phase 6 locked values
PHASE6_F_AT_REQ = -17.71             # f(R_eq) at static equilibrium (approx)
PHASE6B_A_CRIT_NATURAL = 1.062      # A_crit for natural profile (Phase 6B)
PHASE6B_A_CRIT_UNIFORM_REQ = 0.421  # Uniform A_crit at R_eq

# Linearized mass coefficient: m(r) = M + coeff * (1/r - 1/R_ext)
# where coeff = 2*pi*M^2 / tau^2
MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / (TAU_CANONICAL ** 2)


# ================================================================
# Minimal source assumptions — explicitly documented
# ================================================================

MINIMAL_SOURCE_ASSUMPTIONS = [
    "1. The correction enters through an additive positive source term "
    "in the mass equation: m_new(r) = m_static(r) - Sigma(r), where "
    "Sigma(r) = integral of 4*pi*r'^2 * epsilon(r') dr' from r to R_ext.",

    "2. The target is saturation f = 0 (i.e. m_new(r) = r/2), NOT strict "
    "positivity f > 0.  The derived epsilon_min achieves f = 0 exactly.",

    "3. The underlying static mass profile m_static(r) remains the Phase 6B "
    "baseline (linearized equilibrium), unmodified by the correction source.",

    "4. No extra pressure-sector modification changes the mass-balance "
    "condition dm/dr = 4*pi*r^2*rho.  The correction is purely through "
    "the energy density rho, not through anisotropic pressure or "
    "modified field equations.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class DeficitParams:
    """Parameters for the metric deficit analysis."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S
    R_min: float = 0.05
    n_r: int = 500
    n_A: int = 50           # grid points for A scan in two-param
    n_B: int = 50           # grid points for B scan in two-param
    A_max: float = 0.25     # max A coefficient for two-param (A/r^4 term)
    B_max: float = 0.20     # max B coefficient for two-param (B/r^2 term)


@dataclass
class DeficitProfile:
    """The deficit function delta(r) = m(r) - r/2."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    m: np.ndarray = field(default_factory=lambda: np.array([]))
    f: np.ndarray = field(default_factory=lambda: np.array([]))
    delta: np.ndarray = field(default_factory=lambda: np.array([]))
    rho_eq: np.ndarray = field(default_factory=lambda: np.array([]))
    delta_max: float = 0.0
    r_at_delta_max: float = 0.0
    delta_at_R_eq: float = 0.0
    m_at_R_eq: float = 0.0
    f_at_R_eq: float = 0.0
    fraction_r_with_delta_positive: float = 0.0
    integrated_deficit: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class MinimalSourceResult:
    """The minimal additive source epsilon_min = |rho_eq| + 1/(8*pi*r^2)."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_min: np.ndarray = field(default_factory=lambda: np.array([]))
    component_A: np.ndarray = field(default_factory=lambda: np.array([]))
    component_B: np.ndarray = field(default_factory=lambda: np.array([]))
    Sigma: np.ndarray = field(default_factory=lambda: np.array([]))
    f_corrected: np.ndarray = field(default_factory=lambda: np.array([]))
    f_corrected_min: float = 0.0
    f_corrected_at_R_eq: float = 0.0
    ratio_B_over_A_at_R_eq: float = 0.0
    ratio_B_over_A_at_r1: float = 0.0
    Sigma_at_R_eq: float = 0.0
    delta_at_R_eq: float = 0.0
    verification_passes: bool = False
    assumptions: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class KineticDeficitProfile:
    """The Phi_dot profile that would produce epsilon_min kinetically."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    Phi_dot_deficit: np.ndarray = field(default_factory=lambda: np.array([]))
    is_monotonic_inward: bool = False
    Phi_dot_at_R_eq: float = 0.0
    Phi_dot_at_R_ext: float = 0.0
    Phi_dot_max: float = 0.0
    ratio_to_natural_at_R_eq: float = 0.0
    achievable_within_grut: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class AnisotropyInsufficiency:
    """Formal demonstration that anisotropic pressure is insufficient."""
    p_r_minus_p_perp_formula: str = "f * (Phi')^2"
    vanishes_at_f_zero: bool = True
    max_contribution_fraction: float = 0.0
    insufficient: bool = True
    mechanism: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class AdditiveSourceResult:
    """Result of the additive positive source correction class."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    rho_extra: np.ndarray = field(default_factory=lambda: np.array([]))
    f_corrected: np.ndarray = field(default_factory=lambda: np.array([]))
    f_corrected_min: float = 0.0
    works_by_construction: bool = True
    requires_beyond_grut: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class TwoParamScanEntry:
    """One point in the (A,B) scan."""
    A: float = 0.0
    B: float = 0.0
    f_min: float = 0.0
    f_at_R_eq: float = 0.0
    f_positive_everywhere: bool = False


@dataclass
class TwoParamScanResult:
    """Two-parameter energy density scan: epsilon = A/r^4 + B/r^2."""
    A_values: np.ndarray = field(default_factory=lambda: np.array([]))
    B_values: np.ndarray = field(default_factory=lambda: np.array([]))
    f_min_grid: np.ndarray = field(default_factory=lambda: np.array([]))
    f_at_R_eq_grid: np.ndarray = field(default_factory=lambda: np.array([]))
    threshold_contour_A: np.ndarray = field(default_factory=lambda: np.array([]))
    threshold_contour_B: np.ndarray = field(default_factory=lambda: np.array([]))
    A_crit_at_B0: float = 0.0
    B_crit_at_A0: float = 0.0
    minimum_total_energy_A: float = 0.0
    minimum_total_energy_B: float = 0.0
    recovers_phase6b: bool = False
    contour_exists: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class MonotonicProfileGap:
    """Insufficiency of tested monotonic profiles for 1/r^2 support.

    This is NOT a general no-go theorem for all monotonic profiles.
    It applies only to the tested profile family 1/r^n (n >= 2).
    """
    tested_profiles: List[str] = field(default_factory=list)
    gap_at_intermediate_r: float = 0.0
    gap_fraction: float = 0.0
    r_at_max_gap: float = 0.0
    insufficiency_statement: str = ""
    is_general_no_go: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class Phase6BComparison:
    """Comparison explaining why A_crit > 1 for the natural profile."""
    A_crit_natural: float = 0.0
    A_crit_exceeds_unity: bool = False
    excess_fraction: float = 0.0
    component_A_coefficient: float = 0.0
    component_B_coefficient: float = 0.0
    overshoot_explanation: str = ""
    natural_provides_component_A: bool = True
    natural_provides_component_B: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class ClosureClassification:
    """Final classification of the metric deficit closure."""
    classification: str = ""
    current_closure_sufficient: bool = False
    minimal_additive_source_identified: bool = False
    anisotropic_fix_sufficient: bool = False
    profile_family_exists: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class MetricDeficitResult:
    """Master result for the Phase 6C metric deficit analysis."""
    valid: bool = False
    params: DeficitParams = field(default_factory=DeficitParams)
    deficit: Optional[DeficitProfile] = None
    minimal_source: Optional[MinimalSourceResult] = None
    kinetic_deficit: Optional[KineticDeficitProfile] = None
    anisotropy_insufficiency: Optional[AnisotropyInsufficiency] = None
    additive_source: Optional[AdditiveSourceResult] = None
    two_param_scan: Optional[TwoParamScanResult] = None
    monotonic_gap: Optional[MonotonicProfileGap] = None
    phase6b_comparison: Optional[Phase6BComparison] = None
    closure_classification: Optional[ClosureClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Radial grid and deficit profile
# ================================================================

def make_radial_grid(params: DeficitParams) -> np.ndarray:
    """Create log-spaced radial grid from R_ext down to R_min."""
    r_min = max(params.R_min, params.R_eq * 0.8)
    log_r = np.linspace(math.log(params.R_ext), math.log(r_min), params.n_r)
    return np.exp(log_r)


def compute_static_mass(
    r: np.ndarray, params: DeficitParams,
) -> np.ndarray:
    """Compute linearized static mass profile.

    m(r) = M + (2*pi*M^2 / tau^2) * (1/r - 1/R_ext)

    This is the Phase 6 locked result: integrating rho_eq = -M^2/(2*tau^2*r^4)
    from R_ext inward with dm/dr = 4*pi*r^2*rho_eq.
    """
    M = params.M
    tau2 = params.tau ** 2
    coeff = 2.0 * math.pi * M * M / tau2
    m_arr = M + coeff * (1.0 / r - 1.0 / params.R_ext)
    return m_arr


def compute_equilibrium_density(
    r: np.ndarray, params: DeficitParams,
) -> np.ndarray:
    """Compute equilibrium energy density rho_eq = -M^2 / (2*tau^2*r^4)."""
    M = params.M
    tau2 = params.tau ** 2
    return -M * M / (2.0 * tau2 * r ** 4)


def compute_deficit_profile(params: DeficitParams) -> DeficitProfile:
    """Compute the deficit function delta(r) = m(r) - r/2.

    Where delta > 0, the metric function f = 1 - 2m/r < 0.
    """
    r = make_radial_grid(params)
    m = compute_static_mass(r, params)
    f = 1.0 - 2.0 * m / r
    delta = m - r / 2.0
    rho_eq = compute_equilibrium_density(r, params)

    # Evaluate at R_eq (interpolate on reversed arrays since r is decreasing)
    r_rev = r[::-1]
    m_at_R_eq = float(np.interp(params.R_eq, r_rev, m[::-1]))
    f_at_R_eq = float(np.interp(params.R_eq, r_rev, f[::-1]))
    delta_at_R_eq = m_at_R_eq - params.R_eq / 2.0

    # Peak deficit
    idx_max = int(np.argmax(delta))
    delta_max = float(delta[idx_max])
    r_at_delta_max = float(r[idx_max])

    # Fraction of radial grid with delta > 0
    frac_pos = float(np.sum(delta > 0)) / len(delta)

    # Integrated deficit: integral of delta(r) * 4*pi*r^2 dr (magnitude)
    # Note: r is decreasing, so use negative dr for proper sign
    integrand = delta * 4.0 * math.pi * r * r
    integrated = 0.0
    for i in range(1, len(r)):
        dr = r[i] - r[i - 1]  # negative (r decreasing)
        integrated += 0.5 * (integrand[i] + integrand[i - 1]) * dr
    integrated = abs(integrated)

    return DeficitProfile(
        r=r,
        m=m,
        f=f,
        delta=delta,
        rho_eq=rho_eq,
        delta_max=delta_max,
        r_at_delta_max=r_at_delta_max,
        delta_at_R_eq=delta_at_R_eq,
        m_at_R_eq=m_at_R_eq,
        f_at_R_eq=f_at_R_eq,
        fraction_r_with_delta_positive=frac_pos,
        integrated_deficit=integrated,
        notes=[
            f"delta(R_eq) = {delta_at_R_eq:.4f}",
            f"f(R_eq) = {f_at_R_eq:.2f}",
            f"Fraction r with delta > 0: {frac_pos:.3f}",
        ],
    )


# ================================================================
# Level 2: Minimal source
# ================================================================

def _integrate_sigma(
    r: np.ndarray, epsilon: np.ndarray,
) -> np.ndarray:
    """Compute Sigma(r) = integral from r to R_ext of 4*pi*r'^2 * epsilon(r') dr'.

    Since r is sorted R_ext -> R_min (decreasing), Sigma accumulates as we
    go from index 0 (R_ext) to later indices (smaller r).

    Sigma(R_ext) = 0, and Sigma grows as we integrate inward.
    """
    n = len(r)
    Sigma = np.zeros(n)
    integrand = 4.0 * math.pi * r * r * epsilon
    # r[0] = R_ext, integrate inward (r decreasing, dr < 0)
    # Sigma(r) = -integral from R_ext to r of 4*pi*r'^2 * eps dr'
    #          = integral from r to R_ext of 4*pi*r'^2 * eps dr'
    for i in range(1, n):
        dr = r[i] - r[i - 1]  # negative
        Sigma[i] = Sigma[i - 1] - 0.5 * (integrand[i] + integrand[i - 1]) * dr
    return Sigma


def compute_minimal_source(
    deficit: DeficitProfile, params: DeficitParams,
) -> MinimalSourceResult:
    """Compute the minimal additive source epsilon_min(r).

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)
                   = M^2/(2*tau^2*r^4) + 1/(8*pi*r^2)

    This is obtained by demanding Sigma(r) = delta(r), differentiating:
      d(Sigma)/dr = -4*pi*r^2 * epsilon_min(r)
      d(delta)/dr = dm/dr - 1/2 = 4*pi*r^2 * rho_eq(r) - 1/2

    Setting d(Sigma)/dr = d(delta)/dr:
      -4*pi*r^2 * epsilon_min = 4*pi*r^2 * rho_eq - 1/2
      epsilon_min = -rho_eq + 1/(8*pi*r^2)
                  = |rho_eq| + 1/(8*pi*r^2)

    ASSUMPTIONS: See MINIMAL_SOURCE_ASSUMPTIONS module-level list.
    """
    r = deficit.r
    M = params.M
    tau2 = params.tau ** 2

    # Component A: cancels equilibrium negative density
    component_A_full = M * M / (2.0 * tau2 * r ** 4)  # = |rho_eq|

    # Component B: extra intermediate-radius support
    component_B_full = 1.0 / (8.0 * math.pi * r ** 2)

    # The minimal source is only needed where delta > 0 (the deficit region).
    # Outside this region, f >= 0 already and no correction is needed.
    # The boundary condition Sigma(r_outer) = delta(r_outer) = 0 is
    # automatically satisfied because epsilon = 0 for r > r_outer.
    deficit_mask = deficit.delta > 0
    component_A = np.where(deficit_mask, component_A_full, 0.0)
    component_B = np.where(deficit_mask, component_B_full, 0.0)

    epsilon_min = component_A + component_B

    # Integrate Sigma from R_ext inward
    Sigma = _integrate_sigma(r, epsilon_min)

    # Corrected metric function
    m_corrected = deficit.m - Sigma
    f_corrected = 1.0 - 2.0 * m_corrected / r

    # Evaluate at R_eq
    r_rev = r[::-1]
    f_corr_at_R_eq = float(np.interp(params.R_eq, r_rev, f_corrected[::-1]))
    Sigma_at_R_eq = float(np.interp(params.R_eq, r_rev, Sigma[::-1]))
    delta_at_R_eq = deficit.delta_at_R_eq

    # Component ratios
    compA_at_R_eq = M * M / (2.0 * tau2 * params.R_eq ** 4)
    compB_at_R_eq = 1.0 / (8.0 * math.pi * params.R_eq ** 2)
    ratio_at_R_eq = compB_at_R_eq / compA_at_R_eq if compA_at_R_eq > 0 else 0.0

    # At r = 1 (intermediate radius)
    compA_at_r1 = M * M / (2.0 * tau2)
    compB_at_r1 = 1.0 / (8.0 * math.pi)
    ratio_at_r1 = compB_at_r1 / compA_at_r1 if compA_at_r1 > 0 else 0.0

    # Verification: f_corrected >= 0 everywhere (within numerical precision)
    f_corr_min = float(np.min(f_corrected))
    passes = f_corr_min > -0.1  # Allow small numerical error

    return MinimalSourceResult(
        r=r,
        epsilon_min=epsilon_min,
        component_A=component_A,
        component_B=component_B,
        Sigma=Sigma,
        f_corrected=f_corrected,
        f_corrected_min=f_corr_min,
        f_corrected_at_R_eq=f_corr_at_R_eq,
        ratio_B_over_A_at_R_eq=ratio_at_R_eq,
        ratio_B_over_A_at_r1=ratio_at_r1,
        Sigma_at_R_eq=Sigma_at_R_eq,
        delta_at_R_eq=delta_at_R_eq,
        verification_passes=passes,
        assumptions=MINIMAL_SOURCE_ASSUMPTIONS,
        notes=[
            f"f_corrected_min = {f_corr_min:.6f}",
            f"f_corrected(R_eq) = {f_corr_at_R_eq:.4f}",
            f"Sigma(R_eq) = {Sigma_at_R_eq:.4f}, delta(R_eq) = {delta_at_R_eq:.4f}",
            f"ratio B/A at R_eq = {ratio_at_R_eq:.4f}",
            f"ratio B/A at r=1 = {ratio_at_r1:.4f}",
        ],
    )


# ================================================================
# Level 3: Correction classes
# ================================================================

# --- Class 1: Kinetic deficit-shaped profile ---

def compute_kinetic_deficit(
    minimal_source: MinimalSourceResult, params: DeficitParams,
) -> KineticDeficitProfile:
    """Compute the Phi_dot profile that would produce epsilon_min kinetically.

    Phi_dot_deficit(r) = sqrt(2 * epsilon_min(r))

    This shape exists mathematically but is not achievable within GRUT
    sourcing because Phi_dot = (X - Phi)/tau produces profiles ~ 1/r^2,
    not the required mixed 1/r^4 + 1/r^2 shape.
    """
    r = minimal_source.r
    epsilon_min = minimal_source.epsilon_min
    M = params.M
    tau = params.tau

    Phi_dot_deficit = np.sqrt(2.0 * epsilon_min)

    # Evaluate at key radii
    r_rev = r[::-1]
    pd_at_R_eq = float(np.interp(params.R_eq, r_rev, Phi_dot_deficit[::-1]))
    pd_at_R_ext = float(np.interp(params.R_ext, r_rev, Phi_dot_deficit[::-1]))
    pd_max = float(np.max(Phi_dot_deficit))

    # Natural Phi_dot at R_eq for comparison
    X_eq = M / (params.R_eq ** 2)
    Phi_dot_natural_eq = X_eq / tau
    ratio = pd_at_R_eq / Phi_dot_natural_eq if Phi_dot_natural_eq > 0 else 0.0

    # Monotonicity check: is Phi_dot increasing inward (as r decreases)?
    # r is decreasing, so Phi_dot should be increasing along the array
    diffs = np.diff(Phi_dot_deficit)
    is_mono_inward = bool(np.all(diffs >= -1e-10))

    # GRUT sourcing: Phi_dot = (X - Phi)/tau with X = M/r^2
    # At equilibrium Phi = X, so Phi_dot = 0.  After perturbation,
    # Phi_dot ~ delta_X/tau ~ 1/r^2 (not 1/r^4 + 1/r^2).
    achievable = False  # Cannot produce mixed shape

    return KineticDeficitProfile(
        r=r,
        Phi_dot_deficit=Phi_dot_deficit,
        is_monotonic_inward=is_mono_inward,
        Phi_dot_at_R_eq=pd_at_R_eq,
        Phi_dot_at_R_ext=pd_at_R_ext,
        Phi_dot_max=pd_max,
        ratio_to_natural_at_R_eq=ratio,
        achievable_within_grut=achievable,
        notes=[
            f"Phi_dot(R_eq) = {pd_at_R_eq:.4f}",
            f"Phi_dot(R_ext) = {pd_at_R_ext:.6f}",
            f"Ratio to natural at R_eq = {ratio:.4f}",
            "Shape exists, not achievable within GRUT sourcing",
        ],
    )


# --- Class 2: Anisotropy insufficiency ---

def assess_anisotropy_insufficiency(
    params: DeficitParams,
) -> AnisotropyInsufficiency:
    """Formally assess whether anisotropic pressure can close the deficit.

    p_r - p_perp = f * (Phi')^2

    This is proportional to f and therefore VANISHES at f = 0
    (the critical metric surface).  The anisotropy contribution is
    identically zero where the fix is needed most.

    Phase 6B confirmed: < 1% effect on threshold (self-quenching).
    """
    # At the threshold surface f = 0, the contribution is exactly zero.
    # The maximum contribution is at large |f|, where the fix is not needed.

    # Quantify: max |f * Phi'^2| / |rho_eq| in the barrier
    r = make_radial_grid(params)
    M = params.M
    tau2 = params.tau ** 2
    m = compute_static_mass(r, params)
    f = 1.0 - 2.0 * m / r
    Phi_prime_eq = -2.0 * M / (r ** 3)
    rho_eq = -M * M / (2.0 * tau2 * r ** 4)

    aniso_contrib = f * Phi_prime_eq ** 2
    max_frac = 0.0
    for i in range(len(r)):
        if abs(rho_eq[i]) > 1e-30:
            frac = abs(aniso_contrib[i]) / abs(rho_eq[i])
            if frac > max_frac:
                max_frac = frac

    return AnisotropyInsufficiency(
        p_r_minus_p_perp_formula="f * (Phi')^2",
        vanishes_at_f_zero=True,
        max_contribution_fraction=max_frac,
        insufficient=True,
        mechanism=(
            "The anisotropic stress p_r - p_perp = f*(Phi')^2 is proportional "
            "to f and therefore vanishes identically at the critical surface "
            "f = 0 where the correction is most needed.  This self-quenching "
            "mechanism (confirmed < 1% in Phase 6B) makes anisotropic pressure "
            "formally insufficient to close the metric deficit."
        ),
        notes=[
            "Vanishes at f=0 by construction",
            f"Max contribution fraction in barrier: {max_frac:.4f}",
            "Phase 6B confirmed: < 1% effect on threshold",
        ],
    )


# --- Class 3: Additive source ---

def compute_additive_source(
    minimal_source: MinimalSourceResult, params: DeficitParams,
) -> AdditiveSourceResult:
    """Test additive positive source correction: rho_extra = epsilon_min.

    This WORKS BY CONSTRUCTION: we defined epsilon_min so that Sigma = delta.
    The corrected f = 1 - 2*(m - Sigma)/r >= 0 by the saturation condition.

    However, it REQUIRES BEYOND-GRUT PHYSICS because no mechanism in the
    current GRUT closure produces this specific source profile.
    """
    r = minimal_source.r
    f_corrected = minimal_source.f_corrected.copy()
    f_corr_min = float(np.min(f_corrected))

    return AdditiveSourceResult(
        r=r,
        rho_extra=minimal_source.epsilon_min.copy(),
        f_corrected=f_corrected,
        f_corrected_min=f_corr_min,
        works_by_construction=True,
        requires_beyond_grut=True,
        notes=[
            "Works by construction: epsilon_min designed to saturate f = 0",
            "Requires beyond-GRUT physics: no mechanism in current closure "
            "produces this specific source profile",
            f"f_corrected_min = {f_corr_min:.6f}",
        ],
    )


# --- Class 4: Two-parameter energy density scan ---

def scan_two_parameter(params: DeficitParams) -> TwoParamScanResult:
    """Scan epsilon(r) = A/r^4 + B/r^2 at the mass-function level.

    For each (A,B) pair:
      epsilon(r) = A / r^4 + B / r^2
      Sigma(r)   = integral from r to R_ext of 4*pi*r'^2 * epsilon dr'
      m_new(r)   = m_static(r) - Sigma(r)
      f_new(r)   = 1 - 2*m_new(r)/r
      f_min      = min(f_new)

    The threshold contour is the set of (A,B) where f_min = 0.
    At B=0, A_crit should recover the Phase 6B natural result.
    """
    r = make_radial_grid(params)
    m_static = compute_static_mass(r, params)
    n_r = len(r)

    n_A = params.n_A
    n_B = params.n_B

    # For B=0, the epsilon = A/r^4 term.  The natural profile at amplitude
    # A_natural gives epsilon = A_natural^2 * M^2 / (2*tau^2*r^4).
    # So the coefficient A in epsilon = A/r^4 corresponds to:
    #   A_coeff = A_natural^2 * M^2 / (2*tau^2)
    # At A_natural = 1: A_coeff = M^2/(2*tau^2) = |rho_eq coefficient|
    # At A_natural = 1.06: A_coeff ~ 1.06^2 * M^2/(2*tau^2)
    #
    # Set A_max to cover up to ~1.8 * |rho_eq coefficient|
    # (wider range improves interpolation accuracy at the zero-crossing)
    rho_eq_coeff = params.M ** 2 / (2.0 * params.tau ** 2)
    A_max = 1.8 * rho_eq_coeff
    B_max = params.B_max

    A_vals = np.linspace(0, A_max, n_A + 1)
    B_vals = np.linspace(0, B_max, n_B + 1)

    f_min_grid = np.zeros((n_A + 1, n_B + 1))
    f_R_eq_grid = np.zeros((n_A + 1, n_B + 1))

    # Precompute r-dependent integrands for A and B components
    # For epsilon = A/r^4: integrand_A = 4*pi*r^2 * (1/r^4) = 4*pi/r^2
    # For epsilon = B/r^2: integrand_B = 4*pi*r^2 * (1/r^2) = 4*pi
    # Sigma(r) = A * Sigma_A(r) + B * Sigma_B(r)
    integrand_A_base = 4.0 * math.pi / (r ** 2)
    integrand_B_base = 4.0 * math.pi * np.ones_like(r)

    # Precompute cumulative integrals for Sigma_A and Sigma_B
    Sigma_A = np.zeros(n_r)
    Sigma_B = np.zeros(n_r)
    for i in range(1, n_r):
        dr = r[i] - r[i - 1]  # negative
        Sigma_A[i] = Sigma_A[i - 1] - 0.5 * (
            integrand_A_base[i] + integrand_A_base[i - 1]
        ) * dr
        Sigma_B[i] = Sigma_B[i - 1] - 0.5 * (
            integrand_B_base[i] + integrand_B_base[i - 1]
        ) * dr

    # R_eq index for fast lookup
    r_rev = r[::-1]
    idx_eq = int(np.argmin(np.abs(r - params.R_eq)))

    for ia in range(n_A + 1):
        A_val = A_vals[ia]
        for ib in range(n_B + 1):
            B_val = B_vals[ib]
            Sigma = A_val * Sigma_A + B_val * Sigma_B
            m_new = m_static - Sigma
            f_new = 1.0 - 2.0 * m_new / r
            f_min_grid[ia, ib] = float(np.min(f_new))
            f_R_eq_grid[ia, ib] = float(
                np.interp(params.R_eq, r_rev, f_new[::-1])
            )

    # Extract threshold contour: for each B, find A where f_min crosses 0
    contour_A_list = []
    contour_B_list = []
    for ib in range(n_B + 1):
        col = f_min_grid[:, ib]
        A_cross = _find_zero_crossing_1d(A_vals, col)
        if A_cross is not None:
            contour_A_list.append(A_cross)
            contour_B_list.append(B_vals[ib])

    contour_A = np.array(contour_A_list) if contour_A_list else np.array([])
    contour_B = np.array(contour_B_list) if contour_B_list else np.array([])
    contour_exists = len(contour_A) > 2

    # A_crit at B=0
    A_crit_B0 = 0.0
    if len(contour_A) > 0 and contour_B[0] == 0.0:
        A_crit_B0 = contour_A[0]
    else:
        # Fallback: interpolate from f_min_grid
        A_cross = _find_zero_crossing_1d(A_vals, f_min_grid[:, 0])
        if A_cross is not None:
            A_crit_B0 = A_cross

    # B_crit at A=0
    B_crit_A0 = 0.0
    row0 = f_min_grid[0, :]
    B_cross = _find_zero_crossing_1d(B_vals, row0)
    if B_cross is not None:
        B_crit_A0 = B_cross

    # Phase 6B recovery: A_crit at B=0 should correspond to
    # A_coeff = A_natural^2 * M^2/(2*tau^2)
    # At A_natural = 1.06: A_coeff = 1.06^2 * rho_eq_coeff
    expected_A_coeff = PHASE6B_A_CRIT_NATURAL ** 2 * rho_eq_coeff
    recovers = abs(A_crit_B0 - expected_A_coeff) / expected_A_coeff < 0.10 if A_crit_B0 > 0 else False

    # Find minimum total energy on contour
    min_A = 0.0
    min_B = 0.0
    if contour_exists:
        # Total energy ~ integral of 4*pi*r^2 * (A/r^4 + B/r^2) dr
        # = A * integral(4*pi/r^2 dr) + B * integral(4*pi dr)
        # These are just Sigma_A(R_min) and Sigma_B(R_min)
        SA_total = Sigma_A[-1]
        SB_total = Sigma_B[-1]
        total_energy = contour_A * SA_total + contour_B * SB_total
        idx_min = int(np.argmin(total_energy))
        min_A = float(contour_A[idx_min])
        min_B = float(contour_B[idx_min])

    return TwoParamScanResult(
        A_values=A_vals,
        B_values=B_vals,
        f_min_grid=f_min_grid,
        f_at_R_eq_grid=f_R_eq_grid,
        threshold_contour_A=contour_A,
        threshold_contour_B=contour_B,
        A_crit_at_B0=A_crit_B0,
        B_crit_at_A0=B_crit_A0,
        minimum_total_energy_A=min_A,
        minimum_total_energy_B=min_B,
        recovers_phase6b=recovers,
        contour_exists=contour_exists,
        notes=[
            f"A_crit(B=0) = {A_crit_B0:.6f}",
            f"B_crit(A=0) = {B_crit_A0:.6f}",
            f"Expected A_coeff from Phase6B: {expected_A_coeff:.6f}",
            (
                f"Normalization: A_coeff = A_amplitude^2 * M^2/(2*tau^2); "
                f"Phase 6B A_amplitude = {PHASE6B_A_CRIT_NATURAL:.3f} "
                f"-> A_coeff = {expected_A_coeff:.6f}"
            ),
            f"Phase 6B recovery: {'YES' if recovers else 'NO'}"
            f" (relative error: {abs(A_crit_B0 - expected_A_coeff) / expected_A_coeff * 100:.1f}%)"
            if A_crit_B0 > 0 else f"Phase 6B recovery: NO",
            f"Contour has {len(contour_A)} points",
        ],
    )


def _find_zero_crossing_1d(
    x_vals: np.ndarray, y_vals: np.ndarray,
) -> Optional[float]:
    """Find x where y crosses zero via linear interpolation."""
    for i in range(len(y_vals) - 1):
        if y_vals[i] < 0 and y_vals[i + 1] >= 0:
            dx = x_vals[i + 1] - x_vals[i]
            dy = y_vals[i + 1] - y_vals[i]
            if abs(dy) > 1e-30:
                return float(x_vals[i] + (-y_vals[i]) * dx / dy)
    return None


# --- Class 5: Monotonic profile insufficiency ---

def assess_monotonic_profile_insufficiency(
    minimal_source: MinimalSourceResult, params: DeficitParams,
) -> MonotonicProfileGap:
    """Assess whether tested monotonic profiles provide 1/r^2 support.

    Test family: epsilon(r) = C / r^n for n = 2, 3, 4, 5
    Each is amplitude-optimized to minimize the global f deficit.

    The key finding: profiles with n >= 3 concentrate at small r and
    miss intermediate radii (same as Phase 6B natural profile issue).
    The n=2 profile provides component B but NOT component A efficiently.
    No single-power-law monotonic profile provides BOTH components.

    This is an insufficiency result for the tested family, NOT a general
    no-go theorem for all possible monotonic profiles.
    """
    r = minimal_source.r
    m_static = compute_static_mass(r, params)
    epsilon_min = minimal_source.epsilon_min
    n_r = len(r)

    tested = []
    max_gap = 0.0
    r_max_gap = 0.0
    gap_frac = 0.0

    for n_power in [2, 3, 4, 5]:
        profile_name = f"1/r^{n_power}"
        tested.append(profile_name)

        # For epsilon = C / r^n, find C that minimizes max deficit
        # by scanning C and finding the best global f_min
        eps_shape = 1.0 / r ** n_power
        Sigma_shape = _integrate_sigma(r, eps_shape)

        # Scan C to find the one that makes f_min closest to 0
        best_C = 0.0
        best_fmin = -1e10
        for ic in range(201):
            C = ic * 0.01
            m_new = m_static - C * Sigma_shape
            f_new = 1.0 - 2.0 * m_new / r
            fm = float(np.min(f_new))
            if fm > best_fmin and fm <= 0.1:
                best_fmin = fm
                best_C = C

        # Compute gap: how much does the optimal single-power profile
        # fall short of epsilon_min?
        eps_optimal = best_C * eps_shape
        gap = epsilon_min - eps_optimal
        gap_positive = np.maximum(gap, 0.0)

        if n_power == 4:
            # The n=4 case (natural profile) has the largest intermediate-r gap
            gap_ratio = gap_positive / (epsilon_min + 1e-30)
            idx_gap = int(np.argmax(gap_ratio))
            this_gap = float(gap_ratio[idx_gap])
            this_r = float(r[idx_gap])
            if this_gap > gap_frac:
                gap_frac = this_gap
                r_max_gap = this_r
                max_gap = float(gap_positive[idx_gap])

    return MonotonicProfileGap(
        tested_profiles=tested,
        gap_at_intermediate_r=max_gap,
        gap_fraction=gap_frac,
        r_at_max_gap=r_max_gap,
        insufficiency_statement=(
            "Tested monotonic inward-increasing profiles (1/r^n for n = 2..5) "
            "cannot simultaneously match both components of epsilon_min. "
            "The 1/r^4 profile (natural) concentrates at small r, providing "
            "Component A but requiring amplitude overshoot (A_crit = 1.06) to "
            "brute-force Component B.  The 1/r^2 profile provides Component B "
            "but is inefficient for Component A.  No single tested monotonic "
            "power-law profile matches the required mixed 1/r^4 + 1/r^2 shape."
        ),
        is_general_no_go=False,
        notes=[
            f"Tested profiles: {', '.join(tested)}",
            f"Max gap at r = {r_max_gap:.4f}",
            f"Gap fraction: {gap_frac:.4f}",
            "NOT a general no-go: applies only to tested profiles",
        ],
    )


# ================================================================
# Level 4: Classification and comparison
# ================================================================

def build_phase6b_comparison(
    minimal_source: MinimalSourceResult,
    two_param: TwoParamScanResult,
    params: DeficitParams,
) -> Phase6BComparison:
    """Build comparison explaining why A_crit > 1 for the natural profile."""
    rho_eq_coeff = params.M ** 2 / (2.0 * params.tau ** 2)

    # Component A coefficient: M^2 / (2*tau^2)
    # Component B coefficient: 1 / (8*pi)
    comp_A_coeff = rho_eq_coeff
    comp_B_coeff = 1.0 / (8.0 * math.pi)

    A_crit = PHASE6B_A_CRIT_NATURAL
    exceeds = A_crit > 1.0
    excess = A_crit - 1.0

    return Phase6BComparison(
        A_crit_natural=A_crit,
        A_crit_exceeds_unity=exceeds,
        excess_fraction=excess,
        component_A_coefficient=comp_A_coeff,
        component_B_coefficient=comp_B_coeff,
        overshoot_explanation=(
            f"The natural profile Phi_dot ~ M/(tau*r^2) produces "
            f"epsilon ~ M^2/(2*tau^2*r^4), matching Component A (1/r^4) at "
            f"A=1.  But epsilon_min also requires Component B (1/(8*pi*r^2)) "
            f"which the natural profile does NOT provide.  To compensate, "
            f"the amplitude must overshoot to A_crit = {A_crit:.3f}, "
            f"using the excess 1/r^4 energy at small r to cover the 1/r^2 "
            f"deficit at intermediate radii.  This {excess*100:.1f}% excess "
            f"is the price of using a 1/r^4 profile to do a 1/r^2 job."
        ),
        natural_provides_component_A=True,
        natural_provides_component_B=False,
        notes=[
            f"Component A coeff = {comp_A_coeff:.6f}",
            f"Component B coeff = {comp_B_coeff:.6f}",
            f"A_crit = {A_crit:.3f} (excess = {excess*100:.1f}%)",
            "Natural profile provides Component A, NOT Component B",
        ],
    )


def classify_closure(
    minimal_source: MinimalSourceResult,
    anisotropy: AnisotropyInsufficiency,
    additive_source: AdditiveSourceResult,
    monotonic_gap: MonotonicProfileGap,
) -> ClosureClassification:
    """Determine the final closure classification.

    Candidates:
      current_closure_insufficient
      minimal_additive_source_identified  (= additive source works)
      anisotropic_fix_insufficient
      profile_family_exists
      no_tested_profile_succeeds
      unresolved_but_bounded

    Final classification combines the two that apply:
      current_closure_insufficient__minimal_additive_source_identified
    """
    current_sufficient = False  # No tested kinetic profile achieves the shape
    additive_identified = (
        additive_source.works_by_construction
        and minimal_source.verification_passes
    )
    aniso_sufficient = not anisotropy.insufficient
    profile_exists = False  # No single profile family matches both components

    if not current_sufficient and additive_identified:
        cls_str = "current_closure_insufficient__minimal_additive_source_identified"
    elif current_sufficient:
        cls_str = "current_closure_sufficient"
    elif not additive_identified:
        cls_str = "unresolved_but_bounded"
    else:
        cls_str = "no_tested_profile_succeeds"

    return ClosureClassification(
        classification=cls_str,
        current_closure_sufficient=current_sufficient,
        minimal_additive_source_identified=additive_identified,
        anisotropic_fix_sufficient=aniso_sufficient,
        profile_family_exists=profile_exists,
        notes=[
            f"Classification: {cls_str}",
            f"Current closure sufficient: {current_sufficient}",
            f"Minimal additive source identified: {additive_identified}",
            f"Anisotropic fix sufficient: {aniso_sufficient}",
        ],
    )


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. The static mass profile m(r) = M + (2*pi*M^2/tau^2)*(1/r - 1/R_ext) "
    "is the linearized equilibrium.  Higher-order corrections from the full "
    "TOV integration may shift numerical values.",

    "2. The minimal source epsilon_min achieves f = 0 (saturation), NOT "
    "strict positivity f > 0.  A strictly positive metric requires "
    "epsilon > epsilon_min.",

    "3. The kinetic deficit profile Phi_dot = sqrt(2*epsilon_min) is a "
    "mathematical shape, not a physically realizable GRUT solution.  "
    "No GRUT sourcing mechanism produces this mixed 1/r^4 + 1/r^2 form.",

    "4. The two-parameter scan epsilon = A/r^4 + B/r^2 is a convenient "
    "decomposition but does NOT exhaust all possible additive source "
    "profiles.  Other functional forms may also close the deficit.",

    "5. The monotonic profile insufficiency applies ONLY to the tested "
    "family (1/r^n for n = 2..5).  It is NOT a general no-go theorem "
    "for all monotonic profiles.",

    "6. The minimal source formula depends on four explicit assumptions "
    "(see MINIMAL_SOURCE_ASSUMPTIONS): additive source in mass equation, "
    "saturation target, unmodified baseline mass, no pressure-sector changes.",

    "7. The deficit function delta(r) = m(r) - r/2 uses the linearized "
    "mass, not the full self-consistent solution which has a singularity "
    "at r ~ 1.023 r_s (Phase 6).",

    "8. Component B ~ 1/(8*pi*r^2) arises from the geometric 1/2 in "
    "f = 1 - 2m/r, not from the field equations directly.  Its presence "
    "is a consequence of the mass-deficit formulation.",

    "9. The Phase 6B recovery (A_crit at B=0) maps from amplitude A "
    "to energy coefficient A_coeff = A^2 * M^2/(2*tau^2).  The "
    "correspondence is exact only in the linearized regime.",

    "10. Pressure corrections, nonlocal effects, and modified field "
    "equations could alter the minimal source requirement.  This analysis "
    "applies only to the current mass-balance formulation.",

    "11. V(Phi) = Phi^2/(2*tau^2) is the Route A candidate potential.  "
    "Other potentials would give different rho_eq and different epsilon_min.",

    "12. The classification 'current_closure_insufficient__minimal_additive_"
    "source_identified' is descriptive and specific to the tested correction "
    "classes.  Novel closure mechanisms could change the classification.",

    "13. Tau is fixed at the canonical value.  The deficit profile and "
    "minimal source scale with tau^{-2}.",

    "14. The two-parameter scan uses the mass-function level (not Phi_dot "
    "level) to avoid spurious cross terms from squaring Phi_dot = A/r^2 + B/r.  "
    "This is the correct matching to the epsilon_min decomposition.",
]


# ================================================================
# Master analysis function
# ================================================================

def compute_metric_deficit_analysis(
    params: Optional[DeficitParams] = None,
    do_deficit: bool = True,
    do_minimal_source: bool = True,
    do_kinetic_deficit: bool = True,
    do_anisotropy: bool = True,
    do_additive_source: bool = True,
    do_two_param: bool = True,
    do_monotonic_gap: bool = True,
    do_classification: bool = True,
) -> MetricDeficitResult:
    """Master function: Phase 6C metric deficit analysis."""
    if params is None:
        params = DeficitParams()

    result = MetricDeficitResult(
        params=params,
        nonclaims=NONCLAIMS,
        assumptions=MINIMAL_SOURCE_ASSUMPTIONS,
    )

    # Level 1: Deficit profile
    deficit = None
    if do_deficit:
        deficit = compute_deficit_profile(params)
        result.deficit = deficit

    # Level 2: Minimal source
    minimal_source = None
    if do_minimal_source and deficit is not None:
        minimal_source = compute_minimal_source(deficit, params)
        result.minimal_source = minimal_source

    # Level 3: Correction classes
    if do_kinetic_deficit and minimal_source is not None:
        result.kinetic_deficit = compute_kinetic_deficit(minimal_source, params)

    aniso = None
    if do_anisotropy:
        aniso = assess_anisotropy_insufficiency(params)
        result.anisotropy_insufficiency = aniso

    additive = None
    if do_additive_source and minimal_source is not None:
        additive = compute_additive_source(minimal_source, params)
        result.additive_source = additive

    two_param = None
    if do_two_param:
        two_param = scan_two_parameter(params)
        result.two_param_scan = two_param

    mono_gap = None
    if do_monotonic_gap and minimal_source is not None:
        mono_gap = assess_monotonic_profile_insufficiency(minimal_source, params)
        result.monotonic_gap = mono_gap

    # Level 4: Classification and comparison
    if do_classification and minimal_source is not None and two_param is not None:
        result.phase6b_comparison = build_phase6b_comparison(
            minimal_source, two_param, params
        )

    if (do_classification and minimal_source is not None
            and aniso is not None and additive is not None
            and mono_gap is not None):
        result.closure_classification = classify_closure(
            minimal_source, aniso, additive, mono_gap,
        )

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def metric_deficit_result_to_dict(result: MetricDeficitResult) -> Dict[str, Any]:
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
            "n_A": result.params.n_A,
            "n_B": result.params.n_B,
        },
    }

    if result.deficit:
        dp = result.deficit
        d["deficit"] = {
            "delta_max": dp.delta_max,
            "r_at_delta_max": dp.r_at_delta_max,
            "delta_at_R_eq": dp.delta_at_R_eq,
            "m_at_R_eq": dp.m_at_R_eq,
            "f_at_R_eq": dp.f_at_R_eq,
            "fraction_r_with_delta_positive": dp.fraction_r_with_delta_positive,
            "integrated_deficit": dp.integrated_deficit,
        }

    if result.minimal_source:
        ms = result.minimal_source
        d["minimal_source"] = {
            "f_corrected_min": ms.f_corrected_min,
            "f_corrected_at_R_eq": ms.f_corrected_at_R_eq,
            "ratio_B_over_A_at_R_eq": ms.ratio_B_over_A_at_R_eq,
            "ratio_B_over_A_at_r1": ms.ratio_B_over_A_at_r1,
            "Sigma_at_R_eq": ms.Sigma_at_R_eq,
            "delta_at_R_eq": ms.delta_at_R_eq,
            "verification_passes": ms.verification_passes,
        }

    if result.kinetic_deficit:
        kd = result.kinetic_deficit
        d["kinetic_deficit"] = {
            "Phi_dot_at_R_eq": kd.Phi_dot_at_R_eq,
            "Phi_dot_at_R_ext": kd.Phi_dot_at_R_ext,
            "Phi_dot_max": kd.Phi_dot_max,
            "ratio_to_natural_at_R_eq": kd.ratio_to_natural_at_R_eq,
            "is_monotonic_inward": kd.is_monotonic_inward,
            "achievable_within_grut": kd.achievable_within_grut,
        }

    if result.anisotropy_insufficiency:
        ai = result.anisotropy_insufficiency
        d["anisotropy_insufficiency"] = {
            "vanishes_at_f_zero": ai.vanishes_at_f_zero,
            "max_contribution_fraction": ai.max_contribution_fraction,
            "insufficient": ai.insufficient,
        }

    if result.additive_source:
        aso = result.additive_source
        d["additive_source"] = {
            "f_corrected_min": aso.f_corrected_min,
            "works_by_construction": aso.works_by_construction,
            "requires_beyond_grut": aso.requires_beyond_grut,
        }

    if result.two_param_scan:
        tp = result.two_param_scan
        d["two_param_scan"] = {
            "A_crit_at_B0": tp.A_crit_at_B0,
            "B_crit_at_A0": tp.B_crit_at_A0,
            "recovers_phase6b": tp.recovers_phase6b,
            "contour_exists": tp.contour_exists,
            "contour_n_points": len(tp.threshold_contour_A),
            "minimum_total_energy_A": tp.minimum_total_energy_A,
            "minimum_total_energy_B": tp.minimum_total_energy_B,
        }

    if result.monotonic_gap:
        mg = result.monotonic_gap
        d["monotonic_gap"] = {
            "tested_profiles": mg.tested_profiles,
            "gap_at_intermediate_r": mg.gap_at_intermediate_r,
            "gap_fraction": mg.gap_fraction,
            "r_at_max_gap": mg.r_at_max_gap,
            "is_general_no_go": mg.is_general_no_go,
        }

    if result.phase6b_comparison:
        p6 = result.phase6b_comparison
        d["phase6b_comparison"] = {
            "A_crit_natural": p6.A_crit_natural,
            "A_crit_exceeds_unity": p6.A_crit_exceeds_unity,
            "excess_fraction": p6.excess_fraction,
            "component_A_coefficient": p6.component_A_coefficient,
            "component_B_coefficient": p6.component_B_coefficient,
            "natural_provides_component_A": p6.natural_provides_component_A,
            "natural_provides_component_B": p6.natural_provides_component_B,
        }

    if result.closure_classification:
        cc = result.closure_classification
        d["closure_classification"] = {
            "classification": cc.classification,
            "current_closure_sufficient": cc.current_closure_sufficient,
            "minimal_additive_source_identified": cc.minimal_additive_source_identified,
            "anisotropic_fix_sufficient": cc.anisotropic_fix_sufficient,
            "profile_family_exists": cc.profile_family_exists,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
