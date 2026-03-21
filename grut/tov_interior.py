"""Numerical integration of the modified TOV system — Phase 6.

This module solves the coupled Einstein-scalar ODE system derived in
Phase 4 (xAct Symbolic Offensive, grut_einstein_tphi.wl) for a static
spherically symmetric interior metric supported by the locked T^Phi.

PRINCIPAL RESULTS:

  Result 1 — Mass Accumulation (Phase 4 sign correction):
    The equilibrium scalar field has rho_eq = -X^2/(2 tau^2) < 0.
    Since dm/dr = 4 pi r^2 rho < 0 and we integrate from R_ext INWARD,
    the interior mass function m(r) INCREASES toward the center
    (dm/dr < 0 means m decreases with increasing r, equivalently
    m increases with decreasing r).  This is a CORRECTION to the
    Phase 4 sign interpretation, which incorrectly stated "mass
    DECREASES toward the center."

  Result 2 — Metric Worsening (quantitative):
    The mass accumulation causes f(R_eq) = 1 - 2m(R_eq)/R_eq to
    become MORE negative than the Schwarzschild value A_schw.
    At canonical parameters, the linearized analytical solution gives
    f(R_eq) << A_schw < A_eff < 0.  The scalar field equilibrium
    WORSENS the metric positivity problem, not improves it.

  Result 3 — Phase V Reappraisal:
    The Phase V Constitutive Lapse Insufficiency is NOT an ansatz
    artifact.  The full Einstein solution gives f(R_eq) even more
    negative than the constitutive A_eff = -1.  The constitutive
    ansatz was MORE optimistic than the full calculation because it
    used fixed exterior mass M, while the full Einstein equations
    show increased interior mass m(R_eq) > M.

  Result 4 — Self-Consistent Singularity:
    The homogeneous self-consistent ODE dm/dr = -2 pi m^2/(tau^2 r^2)
    has a singularity at r ~ 1.023 r_s (at canonical parameters),
    where m(r) diverges.  This indicates the static self-consistent
    equilibrium does not admit a smooth interior solution.

ODE SYSTEM (from Phase 4 xAct derivation):
    State: y = [m(r), nu(r), Phi(r), Phi'(r)]
    Metric: ds^2 = -e^{2nu} dt^2 + (1-2m/r)^{-1} dr^2 + r^2 dOmega^2
    Source: T^Phi with V(Phi) = Phi^2/(2 tau^2), J = X/tau
    Self-consistent: X(r) = m(r)/r^2 (gravitational acceleration)

SELF-CONTAINED: Depends only on math, numpy, scipy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

try:
    from scipy.integrate import solve_ivp
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# ================================================================
# Constants — canonical GRUT parameters
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
R_S = 1.0                       # Schwarzschild radius (normalized)
M_EXT = R_S / 2.0               # Exterior mass = r_s / 2
R_EQ_OVER_RS = ALPHA_VAC        # = 1/3
R_EQ = R_S * R_EQ_OVER_RS       # = 1/3
C_COMPACTNESS = R_S / R_EQ      # = 3
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)  # ~ 1.2247 (from dim. analysis)

# Phase V constitutive result for comparison
A_EFF_CONSTITUTIVE = 1.0 - C_COMPACTNESS * BETA_Q / (1.0 + BETA_Q)  # = -1
A_SCHW = 1.0 - 2.0 * M_EXT / R_EQ  # = -2


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class TOVParams:
    """Parameters for the modified TOV integration."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S       # Integration start (well outside horizon)
    R_min: float = 0.05             # Integration stop (near center)
    rtol: float = 1e-10
    atol: float = 1e-12
    max_step_fraction: float = 0.005  # max step as fraction of R_ext


@dataclass
class TOVProfile:
    """Radial profile from the TOV integration."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    m: np.ndarray = field(default_factory=lambda: np.array([]))
    nu: np.ndarray = field(default_factory=lambda: np.array([]))
    f: np.ndarray = field(default_factory=lambda: np.array([]))
    Phi: np.ndarray = field(default_factory=lambda: np.array([]))
    Phi_prime: np.ndarray = field(default_factory=lambda: np.array([]))
    rho: np.ndarray = field(default_factory=lambda: np.array([]))
    p_r: np.ndarray = field(default_factory=lambda: np.array([]))
    p_perp: np.ndarray = field(default_factory=lambda: np.array([]))
    X: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class MetricPositivityResult:
    """The central metric positivity result."""
    f_at_R_eq: float = 0.0
    f_is_positive: bool = False
    m_at_R_eq: float = 0.0
    mass_change_fraction: float = 0.0  # (m(R_eq) - M) / M  (positive = accumulation)
    nu_at_R_eq: float = 0.0
    Phi_at_R_eq: float = 0.0
    X_at_R_eq: float = 0.0

    # Phase V comparison
    A_schw: float = A_SCHW
    A_eff_constitutive: float = A_EFF_CONSTITUTIVE
    f_relative_to_constitutive: float = 0.0  # f(R_eq) - A_eff


@dataclass
class AnalyticalMassResult:
    """Analytical mass profile from linearized or homogeneous ODE.

    Two modes:
      'linearized': Fixed-source X = M/r^2. Clean analytical solution.
                    m(r) = M + (2 pi M^2 / tau^2)(1/r - 1/R_ext)
      'homogeneous': Self-consistent X = m(r)/r^2. Has singularity.
                    1/m(r) = 1/M + (2 pi / tau^2)(1/R_ext - 1/r)
    """
    method: str = ""  # 'linearized' or 'homogeneous'

    # Key values at R_eq
    m_at_R_eq: float = 0.0
    f_at_R_eq: float = 0.0
    dm_dr_at_R_eq: float = 0.0

    # Mass accumulation (m(R_eq) - M)
    delta_m: float = 0.0           # m(R_eq) - M (positive = accumulation)
    delta_m_fraction: float = 0.0  # (m(R_eq) - M) / M

    # For homogeneous: singularity info
    has_singularity: bool = False
    r_singularity: float = 0.0     # radius where m -> +/- infinity
    singularity_in_domain: bool = False  # True if r* is between R_eq and R_ext

    # Profile arrays (optional — filled if r_array provided)
    r: Optional[np.ndarray] = None
    m: Optional[np.ndarray] = None
    f: Optional[np.ndarray] = None
    rho: Optional[np.ndarray] = None

    # Notes
    notes: List[str] = field(default_factory=list)


@dataclass
class ConservationCheck:
    """Numerical verification of conservation (Bianchi consistency)."""
    max_residual: float = 0.0
    mean_residual: float = 0.0
    conservation_satisfied: bool = False
    tolerance: float = 1e-6


@dataclass
class TauScanEntry:
    """Result of a single tau value in the parameter scan."""
    tau: float = 0.0
    f_at_R_eq: float = 0.0
    m_at_R_eq: float = 0.0
    delta_m_fraction: float = 0.0  # (m(R_eq) - M) / M
    method: str = "linearized"
    has_singularity: bool = False
    r_singularity: float = 0.0


@dataclass
class PhaseVComparison:
    """Direct comparison with Phase V constitutive result."""
    A_schw: float = A_SCHW
    A_eff_constitutive: float = A_EFF_CONSTITUTIVE
    f_linearized: float = 0.0      # from linearized analytical
    f_homogeneous: float = 0.0     # from homogeneous (formal, past singularity)
    m_at_R_eq_constitutive: float = M_EXT  # Phase V uses fixed M
    m_at_R_eq_linearized: float = 0.0
    delta_m_fraction: float = 0.0
    sign_correction_confirmed: bool = False  # True when f < A_eff
    notes: List[str] = field(default_factory=list)


@dataclass
class TOVInteriorResult:
    """Master result for the TOV integration."""
    valid: bool = False
    params: TOVParams = field(default_factory=TOVParams)

    # Analytical solutions (PRIMARY)
    linearized: Optional[AnalyticalMassResult] = None
    homogeneous: Optional[AnalyticalMassResult] = None

    # Numerical ODE (SUPPLEMENTARY — may be unstable)
    profile: Optional[TOVProfile] = None
    metric_result: Optional[MetricPositivityResult] = None

    # Critical processing analysis
    processing: Optional[CriticalProcessingResult] = None

    # Comparisons and checks
    phase_v_comparison: Optional[PhaseVComparison] = None
    conservation_check: Optional[ConservationCheck] = None
    tau_scan: List[TauScanEntry] = field(default_factory=list)
    integration_info: Dict[str, Any] = field(default_factory=dict)
    nonclaims: List[str] = field(default_factory=list)


# ================================================================
# Stress-energy functions
# ================================================================

def stress_energy(r: float, m: float, Phi: float, Phi_prime: float,
                  tau: float) -> Tuple[float, float, float]:
    """Compute T^Phi components at a given radius.

    Returns (rho, p_r, p_perp).

    V(Phi) = Phi^2 / (2 tau^2)
    J = X/tau where X = m/r^2 (self-consistent gravitational acceleration)
    f = 1 - 2m/r
    """
    if r < 1e-30:
        return 0.0, 0.0, 0.0

    f = 1.0 - 2.0 * m / r
    X = m / (r * r)

    kinetic = 0.5 * Phi_prime * Phi_prime * f
    V_pot = Phi * Phi / (2.0 * tau * tau)
    Phi_J = Phi * X / tau

    rho = kinetic + V_pot - Phi_J
    p_r = kinetic - V_pot + Phi_J
    p_perp = -kinetic - V_pot + Phi_J

    return rho, p_r, p_perp


# ================================================================
# ODE right-hand side
# ================================================================

def tov_rhs(r: float, y: np.ndarray, tau: float) -> np.ndarray:
    """Right-hand side of the modified TOV system.

    State: y = [m, nu, Phi, Phi_prime]

    Returns: dy/dr = [dm/dr, dnu/dr, dPhi/dr, dPhi_prime/dr]

    Note: we integrate INWARD (r decreasing), so solve_ivp sees
    the 'time' variable decreasing.  We define the RHS as d/dr
    (not d/(-r)), and solve_ivp handles the direction automatically.
    """
    m_val, nu_val, Phi_val, Phi_prime_val = y

    if r < 1e-30:
        return np.array([0.0, 0.0, 0.0, 0.0])

    f = 1.0 - 2.0 * m_val / r
    X = m_val / (r * r)

    # Stress-energy
    kinetic = 0.5 * Phi_prime_val * Phi_prime_val * f
    V_pot = Phi_val * Phi_val / (2.0 * tau * tau)
    Phi_J = Phi_val * X / tau

    rho = kinetic + V_pot - Phi_J
    p_r = kinetic - V_pot + Phi_J

    # ODE 1: Mass equation
    dm_dr = 4.0 * math.pi * r * r * rho

    # Handle near-singular region where f ~ 0
    F = r - 2.0 * m_val  # = r * f

    if abs(F) < 1e-30:
        # At or very near a trapping surface — regularize
        return np.array([dm_dr, 0.0, Phi_prime_val, 0.0])

    # ODE 2: Lapse equation
    dnu_dr = (m_val + 4.0 * math.pi * r * r * r * p_r) / (r * F)

    # ODE 3: Phi' = Phi_prime (trivial)
    dPhi_dr = Phi_prime_val

    # ODE 4: Scalar field second-order equation
    # Phi'' + [2/r + nu' - lambda'] Phi' + (1/f)*(-Phi/tau^2 + X/tau) = 0
    # lambda' = (dm_dr * r - m) / (r^2 * f) = (dm_dr * r - m) / (r * F)
    lambda_prime = (dm_dr * r - m_val) / (r * F)

    coeff = 2.0 / r + dnu_dr - lambda_prime
    source = (-Phi_val / (tau * tau) + X / tau) / f

    dPhi_prime_dr = -coeff * Phi_prime_val - source

    return np.array([dm_dr, dnu_dr, dPhi_dr, dPhi_prime_dr])


# ================================================================
# Boundary conditions (Schwarzschild exterior matching)
# ================================================================

def exterior_boundary_conditions(params: TOVParams) -> np.ndarray:
    """Compute initial conditions at R_ext (Schwarzschild matching).

    At R_ext, we match to the exterior Schwarzschild solution:
      m = M (total exterior mass)
      nu = (1/2) ln(1 - 2M/R_ext)  (Schwarzschild lapse)
      Phi = X(R_ext) = M/R_ext^2   (equilibrium)
      Phi' = dX/dr = -2M/R_ext^3   (derivative of X = m/r^2 at exterior)
    """
    M = params.M
    R = params.R_ext

    f_ext = 1.0 - 2.0 * M / R
    if f_ext <= 0:
        raise ValueError(
            f"R_ext = {R} is inside the horizon (f = {f_ext} <= 0). "
            f"Choose R_ext > r_s = {params.r_s}."
        )

    m0 = M
    nu0 = 0.5 * math.log(f_ext)
    Phi0 = M / (R * R)
    Phi_prime0 = -2.0 * M / (R * R * R)

    return np.array([m0, nu0, Phi0, Phi_prime0])


# ================================================================
# Analytical Solutions — PRIMARY CALCULATIONS
# ================================================================

def linearized_mass_solution(params: TOVParams,
                             n_points: int = 2000
                             ) -> AnalyticalMassResult:
    """Fixed-source (X = M/r^2) analytical mass profile.

    At equilibrium (Phi' ~ 0, Phi = X = M/r^2):
      rho = -M^2 / (2 tau^2 r^4)
      dm/dr = 4 pi r^2 rho = -2 pi M^2 / (tau^2 r^2)

    Integrating from R_ext inward:
      m(r) = M + (2 pi M^2 / tau^2)(1/r - 1/R_ext)

    Since r < R_ext => 1/r > 1/R_ext => correction is POSITIVE.
    Mass INCREASES going inward.  f(R_eq) gets MORE negative.
    """
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    R_eq = params.R_eq
    tau2 = tau * tau

    # Profile
    r_min = max(params.R_min, R_eq * 0.8)
    r_arr = np.linspace(R_ext, r_min, n_points)

    coeff = 2.0 * math.pi * M * M / tau2

    m_arr = M + coeff * (1.0 / r_arr - 1.0 / R_ext)
    f_arr = 1.0 - 2.0 * m_arr / r_arr
    rho_arr = -M * M / (2.0 * tau2 * r_arr**4)

    # Values at R_eq
    m_eq = M + coeff * (1.0 / R_eq - 1.0 / R_ext)
    f_eq = 1.0 - 2.0 * m_eq / R_eq
    dm_dr_eq = -2.0 * math.pi * M * M / (tau2 * R_eq * R_eq)

    delta_m = m_eq - M
    delta_m_frac = delta_m / M if M > 0 else 0.0

    notes = [
        f"Linearized (fixed X = M/r^2): m(R_eq) = {m_eq:.6f}",
        f"Mass accumulation: Delta_m = m(R_eq) - M = {delta_m:.6f} > 0",
        f"f(R_eq) = {f_eq:.6f} < A_Schw = {A_SCHW:.1f}",
        "Scalar field equilibrium WORSENS metric positivity",
        "Phase 4 sign interpretation corrected: mass INCREASES inward",
    ]

    return AnalyticalMassResult(
        method="linearized",
        m_at_R_eq=m_eq,
        f_at_R_eq=f_eq,
        dm_dr_at_R_eq=dm_dr_eq,
        delta_m=delta_m,
        delta_m_fraction=delta_m_frac,
        r=r_arr,
        m=m_arr,
        f=f_arr,
        rho=rho_arr,
        notes=notes,
    )


def homogeneous_mass_solution(params: TOVParams,
                              n_points: int = 2000
                              ) -> AnalyticalMassResult:
    """Self-consistent (X = m/r^2) analytical mass profile.

    At equilibrium with Phi = X = m/r^2:
      rho = -m^2 / (2 tau^2 r^4)
      dm/dr = -2 pi m^2 / (tau^2 r^2)

    This is separable with solution:
      1/m(r) = 1/M + (2 pi / tau^2)(1/R_ext - 1/r)

    WARNING: This solution has a SINGULARITY where 1/m = 0 (m -> +/- infinity).
    At canonical parameters, the singularity is at r ~ 1.023 r_s.
    """
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    R_eq = params.R_eq
    tau2 = tau * tau

    # Find singularity radius r* where 1/m(r*) = 0
    # 1/M + (2 pi / tau^2)(1/R_ext - 1/r*) = 0
    # 1/r* = 1/R_ext + tau^2 / (2 pi M)
    inv_r_star = 1.0 / R_ext + tau2 / (2.0 * math.pi * M)
    r_star = 1.0 / inv_r_star

    has_sing = (r_star > params.R_min) and (r_star < R_ext)
    sing_in_domain = has_sing and (r_star > R_eq) and (r_star < R_ext)

    # Profile
    r_min = max(params.R_min, R_eq * 0.8)
    r_arr = np.linspace(R_ext, r_min, n_points)

    inv_m_arr = 1.0 / M + (2.0 * math.pi / tau2) * (1.0 / R_ext - 1.0 / r_arr)

    # Where inv_m is near zero, m diverges — mark as NaN
    m_arr = np.where(np.abs(inv_m_arr) > 1e-10, 1.0 / inv_m_arr, np.nan)
    f_arr = np.where(np.isnan(m_arr), np.nan, 1.0 - 2.0 * m_arr / r_arr)
    rho_arr = np.where(
        np.isnan(m_arr), np.nan,
        -m_arr**2 / (2.0 * tau2 * r_arr**4)
    )

    # Formal value at R_eq (may be past the singularity)
    inv_m_eq = 1.0 / M + (2.0 * math.pi / tau2) * (1.0 / R_ext - 1.0 / R_eq)

    if abs(inv_m_eq) > 1e-10:
        m_eq = 1.0 / inv_m_eq
        f_eq = 1.0 - 2.0 * m_eq / R_eq
        dm_eq = -2.0 * math.pi * m_eq**2 / (tau2 * R_eq**2)
    else:
        m_eq = float('inf')
        f_eq = float('-inf')
        dm_eq = float('-inf')

    delta_m = m_eq - M
    delta_m_frac = delta_m / M if (M > 0 and math.isfinite(m_eq)) else float('inf')

    notes = [
        f"Self-consistent (X = m/r^2): 1/m(r) = 1/M + (2pi/tau^2)(1/R_ext - 1/r)",
        f"Singularity at r* = {r_star:.6f} (1/m = 0, m -> +/- infinity)",
    ]

    if sing_in_domain:
        notes.append(
            f"SINGULARITY at r* = {r_star:.6f} lies BETWEEN R_eq = {R_eq:.4f} "
            f"and R_ext = {R_ext:.1f}: static self-consistent equilibrium "
            "does NOT admit a smooth solution"
        )
        notes.append(
            f"Formal value past singularity: m(R_eq) = {m_eq:.6f}, "
            f"f(R_eq) = {f_eq:.6f} — NOT physically meaningful"
        )
    else:
        notes.append(f"m(R_eq) = {m_eq:.6f}, f(R_eq) = {f_eq:.6f}")

    return AnalyticalMassResult(
        method="homogeneous",
        m_at_R_eq=m_eq,
        f_at_R_eq=f_eq,
        dm_dr_at_R_eq=dm_eq,
        delta_m=delta_m,
        delta_m_fraction=delta_m_frac,
        has_singularity=has_sing,
        r_singularity=r_star,
        singularity_in_domain=sing_in_domain,
        r=r_arr,
        m=m_arr,
        f=f_arr,
        rho=rho_arr,
        notes=notes,
    )


# ================================================================
# Critical Processing Analysis — Φ̇ Threshold for Metric Positivity
# ================================================================

@dataclass
class ProcessingScanEntry:
    """One point in the processing energy scan."""
    epsilon: float = 0.0       # uniform processing energy density
    m_at_R_eq: float = 0.0
    f_at_R_eq: float = 0.0
    f_positive: bool = False


@dataclass
class CriticalProcessingResult:
    """Result of the kinetic processing analysis.

    The equilibrium has rho_eq < 0, causing mass accumulation and f < 0.
    Adding a uniform positive "processing" energy density epsilon
    (from kinetic Phi-dot) can counteract the mass accumulation.

    This dataclass reports:
      - epsilon_crit: the minimum uniform processing energy for f(R_eq) = 0
      - Phi_dot_crit: the corresponding Phi-dot (approx)
      - comparison with natural GRUT scales
      - scan of f(R_eq) vs epsilon
    """
    # Critical processing for f(R_eq) = 0
    epsilon_crit: float = 0.0              # critical uniform energy density
    Phi_dot_crit: float = 0.0             # ~ sqrt(2 * epsilon_crit)

    # The mass budget
    m_static_at_R_eq: float = 0.0         # mass from equilibrium alone
    m_target: float = 0.0                 # R_eq / 2 (for f = 0)
    delta_m_to_remove: float = 0.0        # m_static - m_target

    # Volume integral
    barrier_volume_integral: float = 0.0   # integral of 4 pi r^2 dr over barrier

    # Comparison with natural scales
    rho_eq_at_R_eq: float = 0.0           # |rho_eq| at R_eq
    rho_eq_at_R_ext: float = 0.0          # |rho_eq| at R_ext
    epsilon_over_rho_eq_R_eq: float = 0.0  # epsilon_crit / |rho_eq(R_eq)|
    epsilon_over_rho_eq_R_ext: float = 0.0

    # GRUT natural processing rate
    Phi_dot_natural: float = 0.0          # ~ X(R_eq) / tau (from KG source)
    Phi_dot_ratio: float = 0.0            # Phi_dot_crit / Phi_dot_natural

    # Processing scan: f(R_eq) as function of epsilon
    scan: List[ProcessingScanEntry] = field(default_factory=list)

    notes: List[str] = field(default_factory=list)


def critical_processing_analysis(params: TOVParams,
                                 n_scan: int = 50,
                                 ) -> CriticalProcessingResult:
    """Compute the critical kinetic processing (Phi-dot) for metric positivity.

    Physical setup:
      rho_total(r) = rho_eq(r) + epsilon
                   = -M^2/(2 tau^2 r^4) + epsilon

    where epsilon >= 0 is the uniform "processing" energy density from
    kinetic Phi-dot (time variation of the scalar field).

    Mass function with processing:
      m(r) = M + (2 pi M^2 / tau^2)(1/r - 1/R_ext)
           + (4 pi epsilon / 3)(r^3 - R_ext^3)

    The processing term is NEGATIVE for r < R_ext (reduces mass inward),
    counteracting the equilibrium mass accumulation.

    Critical epsilon for f(R_eq) = 0:
      m(R_eq) = R_eq / 2
      epsilon_crit = (m_static(R_eq) - R_eq/2) / |volume_integral|
    """
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    R_eq = params.R_eq
    tau2 = tau * tau

    # Static mass at R_eq (from linearized solution)
    coeff_eq = 2.0 * math.pi * M * M / tau2
    m_static = M + coeff_eq * (1.0 / R_eq - 1.0 / R_ext)

    # Target mass for f(R_eq) = 0
    m_target = R_eq / 2.0

    # Mass to remove
    delta_m_remove = m_static - m_target

    # Volume integral: integral of 4 pi r^2 dr from R_eq to R_ext
    # This appears as the processing contribution to the mass:
    #   Delta_m_proc = epsilon * (4 pi / 3)(R_eq^3 - R_ext^3)
    # Since R_eq < R_ext, this is negative (mass REDUCTION from processing)
    # The magnitude: |4 pi / 3| * (R_ext^3 - R_eq^3)
    vol_integral = (4.0 * math.pi / 3.0) * (R_ext**3 - R_eq**3)

    # Critical epsilon: delta_m_remove = epsilon_crit * vol_integral
    epsilon_crit = delta_m_remove / vol_integral

    # Critical Phi-dot (Painleve-Gullstrand frame: rho_kinetic ~ 1/2 Phi_dot^2)
    Phi_dot_crit = math.sqrt(2.0 * epsilon_crit)

    # Natural GRUT scales
    X_eq = M / (R_eq * R_eq)  # gravitational acceleration at R_eq
    rho_eq_R_eq = M * M / (2.0 * tau2 * R_eq**4)      # |rho_eq| at R_eq
    rho_eq_R_ext = M * M / (2.0 * tau2 * R_ext**4)     # |rho_eq| at R_ext

    # Natural processing rate from KG source: Phi_dot ~ X/tau (source term)
    Phi_dot_natural = X_eq / tau

    Phi_dot_ratio = Phi_dot_crit / Phi_dot_natural if Phi_dot_natural > 0 else float('inf')

    # Processing scan
    scan = []
    eps_max = 3.0 * epsilon_crit
    for i in range(n_scan + 1):
        eps = eps_max * i / n_scan
        # m(R_eq) with processing
        m_eq = m_static + (4.0 * math.pi * eps / 3.0) * (R_eq**3 - R_ext**3)
        f_eq = 1.0 - 2.0 * m_eq / R_eq
        scan.append(ProcessingScanEntry(
            epsilon=eps,
            m_at_R_eq=m_eq,
            f_at_R_eq=f_eq,
            f_positive=(f_eq > 0),
        ))

    notes = [
        f"Critical processing energy: epsilon_crit = {epsilon_crit:.6f}",
        f"Critical Phi-dot: |Phi_dot|_crit = {Phi_dot_crit:.6f}",
        f"Natural Phi-dot (X/tau at R_eq): {Phi_dot_natural:.4f}",
        f"Ratio Phi_dot_crit / Phi_dot_natural = {Phi_dot_ratio:.4f} "
        f"({Phi_dot_ratio * 100:.1f}%)",
        f"Only {Phi_dot_ratio * 100:.1f}% of the natural processing rate "
        "is needed for metric positivity",
        f"epsilon/|rho_eq(R_eq)| = {epsilon_crit / rho_eq_R_eq:.6f} "
        f"(tiny fraction at R_eq)",
        f"epsilon/|rho_eq(R_ext)| = {epsilon_crit / rho_eq_R_ext:.4f} "
        f"(large fraction at R_ext)",
    ]

    return CriticalProcessingResult(
        epsilon_crit=epsilon_crit,
        Phi_dot_crit=Phi_dot_crit,
        m_static_at_R_eq=m_static,
        m_target=m_target,
        delta_m_to_remove=delta_m_remove,
        barrier_volume_integral=vol_integral,
        rho_eq_at_R_eq=rho_eq_R_eq,
        rho_eq_at_R_ext=rho_eq_R_ext,
        epsilon_over_rho_eq_R_eq=epsilon_crit / rho_eq_R_eq,
        epsilon_over_rho_eq_R_ext=epsilon_crit / rho_eq_R_ext,
        Phi_dot_natural=Phi_dot_natural,
        Phi_dot_ratio=Phi_dot_ratio,
        scan=scan,
        notes=notes,
    )


# ================================================================
# Main numerical integrator
# ================================================================

def integrate_tov(params: TOVParams,
                  method: str = "Radau") -> Tuple[Optional[TOVProfile], Dict[str, Any]]:
    """Integrate the modified TOV system from R_ext inward.

    Returns (profile, info_dict) where profile is None if integration fails.

    NOTE: At canonical parameters, the full coupled system is numerically
    UNSTABLE due to the self-consistent feedback loop X = m/r^2 -> rho -> m.
    The scalar field equation has 1/f terms that diverge near f = 0,
    amplifying perturbations.  Results from this integrator should be
    cross-checked against the analytical solutions.
    """
    if not HAS_SCIPY:
        raise ImportError("scipy is required for TOV integration.")

    y0 = exterior_boundary_conditions(params)

    # Integration direction: R_ext -> R_min (decreasing r)
    r_span = (params.R_ext, params.R_min)

    # Dense output points for profile
    n_points = 2000
    r_eval = np.linspace(params.R_ext, params.R_min, n_points)

    # Event: detect f = 0 (trapping surface)
    def f_zero_event(r, y):
        return 1.0 - 2.0 * y[0] / r
    f_zero_event.terminal = False
    f_zero_event.direction = 0  # detect both crossings

    max_step = params.max_step_fraction * params.R_ext

    try:
        sol = solve_ivp(
            fun=lambda r, y: tov_rhs(r, y, params.tau),
            t_span=r_span,
            y0=y0,
            method=method,
            t_eval=r_eval,
            events=[f_zero_event],
            dense_output=True,
            rtol=params.rtol,
            atol=params.atol,
            max_step=max_step,
        )
    except Exception as e:
        return None, {"error": str(e), "success": False}

    info = {
        "success": sol.success,
        "message": sol.message,
        "nfev": sol.nfev,
        "status": sol.status,
    }

    if sol.t_events and len(sol.t_events[0]) > 0:
        info["f_zero_crossings"] = sol.t_events[0].tolist()

    if not sol.success:
        return None, info

    # Build profile
    r_arr = sol.t
    m_arr = sol.y[0]
    nu_arr = sol.y[1]
    Phi_arr = sol.y[2]
    Phi_prime_arr = sol.y[3]

    f_arr = 1.0 - 2.0 * m_arr / r_arr
    X_arr = m_arr / (r_arr * r_arr)

    rho_arr = np.zeros_like(r_arr)
    p_r_arr = np.zeros_like(r_arr)
    p_perp_arr = np.zeros_like(r_arr)

    for i in range(len(r_arr)):
        rho_arr[i], p_r_arr[i], p_perp_arr[i] = stress_energy(
            r_arr[i], m_arr[i], Phi_arr[i], Phi_prime_arr[i], params.tau
        )

    profile = TOVProfile(
        r=r_arr,
        m=m_arr,
        nu=nu_arr,
        f=f_arr,
        Phi=Phi_arr,
        Phi_prime=Phi_prime_arr,
        rho=rho_arr,
        p_r=p_r_arr,
        p_perp=p_perp_arr,
        X=X_arr,
    )

    return profile, info


# ================================================================
# Post-processing: extract results at R_eq (numerical profile)
# ================================================================

def evaluate_at_R_eq(profile: TOVProfile, params: TOVParams
                     ) -> MetricPositivityResult:
    """Extract the metric positivity result at R_eq from numerical profile."""
    R_eq = params.R_eq

    # Find the index closest to R_eq
    idx = np.argmin(np.abs(profile.r - R_eq))

    # If R_eq is within the integration domain, interpolate
    if R_eq >= profile.r[-1] and R_eq <= profile.r[0]:
        # profile.r is decreasing (inward integration)
        m_eq = np.interp(R_eq, profile.r[::-1], profile.m[::-1])
        nu_eq = np.interp(R_eq, profile.r[::-1], profile.nu[::-1])
        Phi_eq = np.interp(R_eq, profile.r[::-1], profile.Phi[::-1])
        X_eq = m_eq / (R_eq * R_eq)
    else:
        m_eq = profile.m[idx]
        nu_eq = profile.nu[idx]
        Phi_eq = profile.Phi[idx]
        X_eq = profile.X[idx]

    f_eq = 1.0 - 2.0 * m_eq / R_eq
    mass_change = (m_eq - params.M) / params.M if params.M > 0 else 0.0

    return MetricPositivityResult(
        f_at_R_eq=f_eq,
        f_is_positive=(f_eq > 0),
        m_at_R_eq=m_eq,
        mass_change_fraction=mass_change,
        nu_at_R_eq=nu_eq,
        Phi_at_R_eq=Phi_eq,
        X_at_R_eq=X_eq,
        A_schw=A_SCHW,
        A_eff_constitutive=A_EFF_CONSTITUTIVE,
        f_relative_to_constitutive=f_eq - A_EFF_CONSTITUTIVE,
    )


# ================================================================
# Conservation check
# ================================================================

def check_conservation(profile: TOVProfile, params: TOVParams
                       ) -> ConservationCheck:
    """Numerical check of the Bianchi identity / T^Phi conservation.

    The TOV equation dp_r/dr = -(rho + p_r) dnu/dr + (2/r)(p_perp - p_r)
    should be satisfied identically.  We check this at each grid point.
    """
    r = profile.r
    n = len(r)
    residuals = []

    for i in range(1, n - 1):
        dr = r[i + 1] - r[i - 1]
        if abs(dr) < 1e-30:
            continue

        # Numerical derivatives
        dp_r_dr = (profile.p_r[i + 1] - profile.p_r[i - 1]) / dr
        dnu_dr_num = (profile.nu[i + 1] - profile.nu[i - 1]) / dr

        # TOV equation residual
        aniso_term = (2.0 / r[i]) * (profile.p_perp[i] - profile.p_r[i])
        rhs_val = -(profile.rho[i] + profile.p_r[i]) * dnu_dr_num + aniso_term
        residual = abs(dp_r_dr - rhs_val)

        # Normalize by scale
        scale = max(abs(profile.rho[i]), abs(profile.p_r[i]), 1e-30)
        residuals.append(residual / scale)

    if not residuals:
        return ConservationCheck()

    max_res = max(residuals)
    mean_res = sum(residuals) / len(residuals)

    return ConservationCheck(
        max_residual=max_res,
        mean_residual=mean_res,
        conservation_satisfied=(max_res < 1e-3),  # relaxed for numerical derivs
        tolerance=1e-3,
    )


# ================================================================
# Parameter scan over tau (using analytical solutions)
# ================================================================

def scan_tau_analytical(tau_values: List[float], params: TOVParams
                        ) -> List[TauScanEntry]:
    """Scan over tau values using the linearized analytical solution."""
    results = []

    for tau_val in tau_values:
        p = TOVParams(
            r_s=params.r_s, M=params.M, R_eq=params.R_eq,
            tau=tau_val, R_ext=params.R_ext, R_min=params.R_min,
        )

        lin = linearized_mass_solution(p, n_points=100)
        hom = homogeneous_mass_solution(p, n_points=100)

        results.append(TauScanEntry(
            tau=tau_val,
            f_at_R_eq=lin.f_at_R_eq,
            m_at_R_eq=lin.m_at_R_eq,
            delta_m_fraction=lin.delta_m_fraction,
            method="linearized",
            has_singularity=hom.has_singularity,
            r_singularity=hom.r_singularity,
        ))

    return results


# ================================================================
# Phase V comparison
# ================================================================

def build_phase_v_comparison(linearized: AnalyticalMassResult,
                             homogeneous: AnalyticalMassResult,
                             ) -> PhaseVComparison:
    """Build the comparison between Phase V constitutive and full Einstein.

    KEY FINDING: The full Einstein solution gives f(R_eq) WORSE than
    the constitutive A_eff = -1.  The scalar field mass accumulation
    makes the metric more negative, not less.
    """
    f_lin = linearized.f_at_R_eq
    f_hom = homogeneous.f_at_R_eq

    notes = []

    # The central finding: f < A_eff
    notes.append(
        f"Linearized f(R_eq) = {f_lin:.4f} vs constitutive A_eff = "
        f"{A_EFF_CONSTITUTIVE:.1f}: Einstein solution is "
        + ("WORSE" if f_lin < A_EFF_CONSTITUTIVE else "BETTER")
        + " than constitutive."
    )

    notes.append(
        f"Mass accumulation: m(R_eq) = {linearized.m_at_R_eq:.4f} > "
        f"M = {M_EXT} (Delta_m/M = {linearized.delta_m_fraction:.4f})."
    )

    notes.append(
        "Phase 4 sign correction: dm/dr < 0 means mass INCREASES "
        "inward (decreasing r), not decreases."
    )

    if homogeneous.singularity_in_domain:
        notes.append(
            f"Self-consistent equilibrium has SINGULARITY at "
            f"r* = {homogeneous.r_singularity:.4f}: no smooth static solution."
        )

    sign_correction = (f_lin < A_EFF_CONSTITUTIVE)

    return PhaseVComparison(
        A_schw=A_SCHW,
        A_eff_constitutive=A_EFF_CONSTITUTIVE,
        f_linearized=f_lin,
        f_homogeneous=f_hom,
        m_at_R_eq_constitutive=M_EXT,
        m_at_R_eq_linearized=linearized.m_at_R_eq,
        delta_m_fraction=linearized.delta_m_fraction,
        sign_correction_confirmed=sign_correction,
        notes=notes,
    )


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. The linearized analytical solution uses fixed exterior X = M/r^2; "
    "the self-consistent solution (X = m/r^2) develops a singularity, "
    "indicating the equilibrium assumption breaks down.",

    "2. The mass ACCUMULATION (not reduction) finding is for the "
    "static equilibrium Phi = X; dynamical or off-equilibrium "
    "configurations may behave differently.",

    "3. The Phase 4 sign correction (dm/dr < 0 means mass increases "
    "inward, not decreases) applies to the specific directional "
    "interpretation, not to the ODE or T^Phi themselves, which are correct.",

    "4. The self-consistent singularity at r ~ 1.023 r_s suggests "
    "the static self-consistent equilibrium is not the correct "
    "physical picture for the interior; a dynamical treatment may "
    "be needed.",

    "5. The numerical ODE integration is unstable due to the "
    "self-consistent feedback loop X = m/r^2 -> rho -> m and the "
    "1/f singularity at f = 0; the analytical solutions are the "
    "reliable primary results.",

    "6. The scalar field is treated as STATIC; dynamical stability "
    "and time-dependent collapse scenarios are not addressed.",

    "7. tau is treated as a free parameter with a canonical value "
    "from dimensional analysis; its value is not derived from "
    "first principles.",

    "8. Whether a non-equilibrium or dynamical scalar field "
    "configuration can achieve metric positivity remains OPEN.",

    "9. The boundary condition Phi(R_ext) = X(R_ext) = M/R_ext^2 "
    "assumes perfect equilibrium at the matching surface; "
    "transition effects are not modeled.",

    "10. The Phase V Constitutive Lapse Insufficiency is CONFIRMED "
    "(not reclassified) by the full Einstein analysis; the "
    "constitutive result A_eff = -1 was actually more optimistic "
    "than the full calculation.",

    "11. The NEC saturation rho + p_perp = 0 is a kinematic property "
    "of the minimally-coupled scalar, not a general GRUT feature.",

    "12. The mass accumulation mechanism (negative rho -> increased "
    "interior mass) is a general consequence of negative energy "
    "density in any shell and is not specific to GRUT.",
]


# ================================================================
# Master analysis function
# ================================================================

def compute_tov_analysis(
    params: Optional[TOVParams] = None,
    do_tau_scan: bool = True,
    tau_scan_values: Optional[List[float]] = None,
    do_numerical: bool = True,
) -> TOVInteriorResult:
    """Run the complete TOV interior metric analysis.

    This is the master function that:
    1. Computes the linearized analytical solution (PRIMARY)
    2. Computes the homogeneous self-consistent solution (singularity detection)
    3. Optionally integrates the full numerical ODE (SUPPLEMENTARY)
    4. Compares with Phase V constitutive result
    5. Scans over tau (if requested)
    """
    if params is None:
        params = TOVParams()

    result = TOVInteriorResult(params=params, nonclaims=NONCLAIMS)

    # Step 1: Linearized analytical solution (PRIMARY)
    result.linearized = linearized_mass_solution(params)

    # Step 2: Homogeneous self-consistent solution
    result.homogeneous = homogeneous_mass_solution(params)

    # Step 3: Critical processing analysis
    result.processing = critical_processing_analysis(params)

    # Step 4: Phase V comparison
    result.phase_v_comparison = build_phase_v_comparison(
        result.linearized, result.homogeneous
    )

    # Step 5: Numerical ODE integration (SUPPLEMENTARY)
    if do_numerical:
        profile, info = integrate_tov(params)
        result.integration_info = info
        result.profile = profile

        if profile is not None:
            result.metric_result = evaluate_at_R_eq(profile, params)
            result.conservation_check = check_conservation(profile, params)
    else:
        result.integration_info = {"note": "Numerical integration skipped."}

    # Step 6: Tau scan (analytical)
    if do_tau_scan:
        if tau_scan_values is None:
            tau_scan_values = [
                0.5, 0.75, 1.0, TAU_CANONICAL, 1.5, 2.0, 3.0, 5.0, 10.0
            ]
        result.tau_scan = scan_tau_analytical(tau_scan_values, params)

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def tov_result_to_dict(result: TOVInteriorResult) -> Dict[str, Any]:
    """Convert the master result to a serializable dictionary."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "params": {
            "r_s": result.params.r_s,
            "M": result.params.M,
            "R_eq": result.params.R_eq,
            "tau": result.params.tau,
            "R_ext": result.params.R_ext,
        },
    }

    if result.linearized:
        lin = result.linearized
        d["linearized_analytical"] = {
            "m_at_R_eq": lin.m_at_R_eq,
            "f_at_R_eq": lin.f_at_R_eq,
            "delta_m": lin.delta_m,
            "delta_m_fraction": lin.delta_m_fraction,
            "notes": lin.notes,
        }

    if result.homogeneous:
        hom = result.homogeneous
        d["homogeneous_analytical"] = {
            "m_at_R_eq": hom.m_at_R_eq,
            "f_at_R_eq": hom.f_at_R_eq,
            "has_singularity": hom.has_singularity,
            "r_singularity": hom.r_singularity,
            "singularity_in_domain": hom.singularity_in_domain,
            "notes": hom.notes,
        }

    if result.processing:
        pr = result.processing
        d["critical_processing"] = {
            "epsilon_crit": pr.epsilon_crit,
            "Phi_dot_crit": pr.Phi_dot_crit,
            "Phi_dot_natural": pr.Phi_dot_natural,
            "Phi_dot_ratio": pr.Phi_dot_ratio,
            "m_static_at_R_eq": pr.m_static_at_R_eq,
            "m_target": pr.m_target,
            "delta_m_to_remove": pr.delta_m_to_remove,
            "epsilon_over_rho_eq_R_eq": pr.epsilon_over_rho_eq_R_eq,
            "notes": pr.notes,
        }

    if result.metric_result:
        mr = result.metric_result
        d["numerical_ode"] = {
            "f_at_R_eq": mr.f_at_R_eq,
            "f_is_positive": mr.f_is_positive,
            "m_at_R_eq": mr.m_at_R_eq,
            "mass_change_fraction": mr.mass_change_fraction,
            "note": "Numerical ODE may be unstable; cross-check with analytical.",
        }

    if result.phase_v_comparison:
        pv = result.phase_v_comparison
        d["phase_v_comparison"] = {
            "A_eff_constitutive": pv.A_eff_constitutive,
            "f_linearized": pv.f_linearized,
            "f_homogeneous": pv.f_homogeneous,
            "sign_correction_confirmed": pv.sign_correction_confirmed,
            "notes": pv.notes,
        }

    if result.conservation_check:
        cc = result.conservation_check
        d["conservation"] = {
            "max_residual": cc.max_residual,
            "mean_residual": cc.mean_residual,
            "satisfied": cc.conservation_satisfied,
        }

    if result.tau_scan:
        d["tau_scan"] = [
            {
                "tau": e.tau,
                "f_at_R_eq": e.f_at_R_eq,
                "m_at_R_eq": e.m_at_R_eq,
                "delta_m_fraction": e.delta_m_fraction,
                "has_singularity": e.has_singularity,
                "r_singularity": e.r_singularity,
            }
            for e in result.tau_scan
        ]

    d["nonclaims"] = result.nonclaims
    d["integration_info"] = result.integration_info

    return d
