"""Phase D6 — Companion Architecture and Dual-Sector Metric Integration.

Tests whether two independently-motivated sectors can jointly restore global
metric positivity when neither sector alone is sufficient:

  Sector 1 (Macro):  GRUT scalar-memory — provides Component A (~1/r^4)
  Sector 2 (Defect): Curvature-triggered O(3) hedgehog — provides Component B (~1/r^2)

The combined effective stress-energy T_total = T_macro + T_defect (no cross-terms)
is injected into the Phase 6 metric framework.

PRINCIPAL RESULTS:

  Result 1 — Architecture Definition:
    Dual-sector additive approximation documented.

  Result 2 — Trigger Regime:
    Curvature trigger verified: deep core >> exterior.  Explicit activation law
    defines where defect sector is "on".

  Result 3 — Macro Sector:
    Analytic epsilon_macro and Sigma_macro from scalar-memory at two baselines
    (A=1 and A=A_crit).

  Result 4 — Defect Sector:
    Numerical BVP solution + energy extraction from D2.

  Result 5 — Dual-Sector Combination:
    Combined epsilon_total and Sigma_total.  Comparison with epsilon_min target.

  Result 6 — Metric Injection:
    f_corrected(r) = -2*(delta - Sigma_total)/r.  Metric positivity test.

  Result 7 — Lambda Scan:
    Lambda scan at both baselines (A=1 and A=A_crit).

  Result 8 — Classification:
    (determined by numerical outcome)

Imports: solve_hedgehog_bvp, extract_defect_energy from grut.numerical_monopole.
Sigma integration reimplemented locally (8 lines) to avoid private-function import.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

# ---- Import D2 BVP solver and energy extraction ----
from grut.numerical_monopole import (
    NumericalMonopoleParams,
    HedgehogBVPSolution,
    DefectEnergyProfile,
    solve_hedgehog_bvp,
    extract_defect_energy,
    ETA_MATCH,
    LAMBDA_SCAN_VALUES as D2_LAMBDA_SCAN,
)


# ================================================================
# Constants
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
C_COMPACTNESS = R_S / R_EQ
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)
A_CRIT = 1.062
A_CRIT_SQUARED = A_CRIT ** 2

COMP_B_COEFF = 1.0 / (8.0 * math.pi)
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
ETA_SQUARED = ETA_TARGET ** 2  # = COMP_B_COEFF
LAMBDA_DEFAULT = 8.0 * math.pi

MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
R_EXT = 2.0 * R_S

KRETSCHNER_COEFF = 48.0 * M_EXT ** 2  # K = KRETSCHNER_COEFF / r^6
XI_DEFAULT = 1.0  # curvature coupling (from D4)

# Phase 6 locked
PHASE6_F_AT_REQ = -17.71

# Lambda scan values for D6
LAMBDA_SCAN_VALUES = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]

# Number of sectors
N_SECTORS = 2

# Number of cross-terms documented
N_CROSS_TERMS = 4

# Key radii for accounting
KEY_RADII = [R_EQ, 0.5, 0.75, 1.0]


# ================================================================
# Assumptions
# ================================================================

COMPANION_ASSUMPTIONS = [
    "1. Dual-sector additive approximation: T_total = T_macro + T_defect "
    "(no cross-terms between sectors).",

    "2. Macro sector uses the GRUT scalar-memory energy density: "
    "epsilon_macro = A^2 * M^2 / (2*tau^2*r^4).",

    "3. Defect sector uses the D2 hedgehog BVP solution at matched "
    "eta^2 = 1/(8*pi).",

    "4. Two macro baselines tested: A=1 (clean structural test) and "
    "A=A_crit=1.062 (permissive test).",

    "5. Sigma_macro is analytic: A^2 * MASS_COEFF * (1/r - 1/R_ext).",

    "6. Sigma_defect is numerical: integral_r^R_ext 4*pi*r'^2 * epsilon_defect dr'.",

    "7. Curvature trigger activation law: defect active when "
    "xi * sqrt(K)(r) > |m_0^2| = lambda * eta^2.",

    "8. Lambda scan over [5, 10, 25, 50, 100, 200] at both A=1 and A=A_crit.",

    "9. Cross-terms explicitly inventoried and documented as neglected.",

    "10. Background metric held fixed (Schwarzschild); no back-reaction.",
]

COMPANION_NONCLAIMS = [
    "1. This phase does NOT prove the final unified theory.",

    "2. A viable companion result establishes numerical feasibility, "
    "not physical derivation.",

    "3. The additive stress-energy approximation neglects all cross-terms.",

    "4. A positive D6 result at A=A_crit alone is weaker scientifically "
    "(could be 'overshoot + defect').",

    "5. The best result is A=1 + defect restoring positivity.",

    "6. The lambda scan is bounded, not exhaustive.",

    "7. The curvature trigger threshold is a diagnostic, not a first-"
    "principles derivation.",

    "8. Defect sector energy computed on Schwarzschild background, not "
    "self-consistent corrected metric.",

    "9. The metric injection uses linearized deficit framework inherited "
    "from Phase 6.",

    "10. Classification is within the D6 numerical framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class CompanionParams:
    """Parameters for Phase D6."""
    eta: float = ETA_TARGET
    lam: float = LAMBDA_DEFAULT
    xi: float = XI_DEFAULT
    r_min: float = 0.01
    r_max: float = 5.0
    n_grid: int = 300
    n_interior: int = 400
    M: float = M_EXT
    tau: float = TAU_CANONICAL
    R_ext: float = R_EXT
    lambda_scan: List[float] = field(
        default_factory=lambda: list(LAMBDA_SCAN_VALUES)
    )


@dataclass
class ArchitectureDefinition:
    """Level 0: Documents the dual-sector additive approximation."""
    n_sectors: int
    sector_names: List[str]
    combination_rule: str
    cross_term_treatment: str
    macro_description: str
    defect_description: str
    notes: List[str] = field(default_factory=list)


@dataclass
class TriggerRegimeResult:
    """Level 1: Curvature trigger evaluation at key radii."""
    sqrt_K_at_Req: float
    sqrt_K_at_Rext: float
    sqrt_K_at_half: float
    core_to_exterior_ratio: float
    # Activation law
    K_crit: float  # = lambda * eta^2 / xi
    activation_radius: float  # r where xi*sqrt(K) = |m0^2|
    active_at_Req: bool
    active_at_Rext: bool
    activation_formula: str
    notes: List[str] = field(default_factory=list)


@dataclass
class MacroSectorProfile:
    """Level 2: Analytic macro sector at a given scalar amplitude."""
    scalar_A: float
    r_grid: np.ndarray
    epsilon_macro: np.ndarray
    sigma_macro: np.ndarray
    sigma_at_Req: float
    label: str  # "baseline_A1" or "critical_Acrit"
    notes: List[str] = field(default_factory=list)


@dataclass
class DefectSectorProfile:
    """Level 3: Defect sector from D2 BVP."""
    lam: float
    bvp_converged: bool
    r_interior: np.ndarray
    epsilon_defect: np.ndarray
    sigma_defect: np.ndarray
    sigma_at_Req: float
    tail_exponent: float
    tail_coefficient: float
    notes: List[str] = field(default_factory=list)


@dataclass
class DualSectorDecomposition:
    """Level 4: Combined dual-sector epsilon and Sigma."""
    scalar_A: float
    label: str
    r_grid: np.ndarray
    epsilon_macro: np.ndarray
    epsilon_defect: np.ndarray
    epsilon_total: np.ndarray
    sigma_macro: np.ndarray
    sigma_defect: np.ndarray
    sigma_total: np.ndarray
    # Comparison with target
    epsilon_min_target: np.ndarray
    epsilon_ratio_mean: float  # mean(epsilon_total / epsilon_min) over interior
    notes: List[str] = field(default_factory=list)


@dataclass
class SectorDominanceResult:
    """Level 5: Which sector dominates where."""
    crossover_radius: float  # where macro == defect
    macro_dominates_inner: bool
    defect_dominates_outer: bool
    ratio_at_Req: float  # macro/defect at R_eq
    ratio_at_Rext: float  # macro/defect at R_ext
    notes: List[str] = field(default_factory=list)


@dataclass
class CompanionMetricInjectionResult:
    """Level 6: Metric injection from combined source."""
    scalar_A: float
    label: str
    r_grid: np.ndarray
    delta: np.ndarray
    sigma_total: np.ndarray
    f_corrected: np.ndarray
    f_min: float
    f_min_radius: float
    metric_positive: bool
    # Budget at key radii
    budget: Dict[str, Dict[str, float]]
    notes: List[str] = field(default_factory=list)


@dataclass
class CompanionLambdaScanEntry:
    """One entry in the lambda scan (both baselines)."""
    lam: float
    bvp_converged: bool
    # A=1 results
    f_min_A1: float
    metric_positive_A1: bool
    sigma_defect_fraction_A1: float
    # A=A_crit results
    f_min_Acrit: float
    metric_positive_Acrit: bool
    sigma_defect_fraction_Acrit: float
    notes: str = ""


@dataclass
class CompanionLambdaScanResult:
    """Level 7: Full lambda scan result."""
    entries: List[CompanionLambdaScanEntry]
    n_scanned: int
    n_converged: int
    # A=1 summary
    n_positive_A1: int
    best_lambda_A1: Optional[float]
    best_fmin_A1: float
    # A=A_crit summary
    n_positive_Acrit: int
    best_lambda_Acrit: Optional[float]
    best_fmin_Acrit: float
    notes: List[str] = field(default_factory=list)


@dataclass
class CrossTermEntry:
    """One neglected cross-term."""
    name: str
    description: str
    severity: str  # "moderate", "significant", etc.
    physical_effect: str


@dataclass
class CrossTermInventory:
    """Level 8: Neglected cross-terms."""
    entries: List[CrossTermEntry]
    n_cross_terms: int
    additive_approximation_justified: bool
    main_approximation: str
    notes: List[str] = field(default_factory=list)


@dataclass
class CompanionClassification:
    """Level 9: Final D6 classification."""
    classification: str
    phase_status: str
    metric_positive_A1: bool
    metric_positive_Acrit: bool
    best_fmin_A1: float
    best_fmin_Acrit: float
    viable_lambda_window_A1: List[float]
    viable_lambda_window_Acrit: List[float]
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class CompanionArchitectureResult:
    """Master result container for Phase D6."""
    valid: bool
    params: CompanionParams
    architecture: Optional[ArchitectureDefinition] = None
    trigger_regime: Optional[TriggerRegimeResult] = None
    macro_baseline: Optional[MacroSectorProfile] = None
    macro_critical: Optional[MacroSectorProfile] = None
    defect_sector: Optional[DefectSectorProfile] = None
    decomposition_A1: Optional[DualSectorDecomposition] = None
    decomposition_Acrit: Optional[DualSectorDecomposition] = None
    dominance: Optional[SectorDominanceResult] = None
    metric_A1: Optional[CompanionMetricInjectionResult] = None
    metric_Acrit: Optional[CompanionMetricInjectionResult] = None
    lambda_scan: Optional[CompanionLambdaScanResult] = None
    cross_terms: Optional[CrossTermInventory] = None
    classification: Optional[CompanionClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)


# ================================================================
# Helpers (local reimplementations to avoid private imports)
# ================================================================

def _sigma_from_profile(r: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """Compute Sigma(r) = integral_r^r_max 4*pi*r'^2 * epsilon(r') dr'.

    Cumulative trapezoid from the right.  Reimplemented locally from D2
    to avoid importing a private function.
    """
    integrand = 4.0 * math.pi * r ** 2 * epsilon
    sigma = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = r[i + 1] - r[i]
        sigma[i] = sigma[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * dr
    return sigma


def _fit_exponent(r: np.ndarray, y: np.ndarray) -> float:
    """Fit power-law exponent: y ~ r^alpha in log-log."""
    mask = (y > 0) & np.isfinite(y)
    if np.sum(mask) < 3:
        return float("nan")
    lr = np.log(r[mask])
    ly = np.log(y[mask])
    n = len(lr)
    sx, sy = np.sum(lr), np.sum(ly)
    sxx, sxy = np.sum(lr ** 2), np.sum(lr * ly)
    d = n * sxx - sx * sx
    if abs(d) < 1e-30:
        return float("nan")
    return float((n * sxy - sx * sy) / d)


def _sqrt_kretschner(r: float) -> float:
    """sqrt(K) = sqrt(48) * M / r^3."""
    return math.sqrt(KRETSCHNER_COEFF) / r ** 3


# ================================================================
# Level 0: Architecture Definition
# ================================================================

def define_architecture(params: CompanionParams) -> ArchitectureDefinition:
    """Document the dual-sector additive approximation."""
    return ArchitectureDefinition(
        n_sectors=N_SECTORS,
        sector_names=["macro_scalar_memory", "defect_hedgehog"],
        combination_rule="T_total = T_macro + T_defect (additive, no cross-terms)",
        cross_term_treatment="inventoried_and_neglected",
        macro_description=(
            "GRUT scalar-memory sector: epsilon_macro = A^2 * M^2 / (2*tau^2*r^4). "
            "Provides Component A (~1/r^4) from gravitationally-sourced kinetic "
            "processing."
        ),
        defect_description=(
            "Curvature-triggered O(3) hedgehog defect: epsilon_defect from BVP "
            "solution with eta^2 = 1/(8*pi). Provides Component B (~1/r^2) from "
            "topological angular gradient."
        ),
        notes=[
            "Two macro baselines: A=1 (clean structural test) and A=A_crit (permissive).",
            "Best scientific result: A=1 + defect restores metric positivity.",
            "Additive approximation neglects 4 cross-terms (documented in Level 8).",
        ],
    )


# ================================================================
# Level 1: Trigger Regime Verification
# ================================================================

def verify_trigger_regime(params: CompanionParams) -> TriggerRegimeResult:
    """Evaluate sqrt(K) at key radii and define activation law.

    Activation criterion: defect SSB occurs when
        xi * sqrt(K)(r) > |m_0^2| = lambda * eta^2

    The activation radius r_act solves:
        xi * sqrt(48) * M / r_act^3 = lambda * eta^2
    =>  r_act = (xi * sqrt(48) * M / (lambda * eta^2))^(1/3)
    """
    xi = params.xi
    lam = params.lam
    eta = params.eta

    sqrt_K_Req = _sqrt_kretschner(R_EQ)
    sqrt_K_Rext = _sqrt_kretschner(R_EXT)
    sqrt_K_half = _sqrt_kretschner(0.5)

    ratio = sqrt_K_Req / sqrt_K_Rext if sqrt_K_Rext > 0 else float("inf")

    # Activation law
    m0_sq = lam * eta ** 2  # |m_0^2| (broken-phase mass squared)
    K_crit = m0_sq / xi if xi > 0 else float("inf")

    # Solve for activation radius
    # xi * sqrt(KRETSCHNER_COEFF) / r^3 = m0_sq
    # r^3 = xi * sqrt(KRETSCHNER_COEFF) / m0_sq
    r_act_cubed = xi * math.sqrt(KRETSCHNER_COEFF) / m0_sq if m0_sq > 0 else 0.0
    r_act = r_act_cubed ** (1.0 / 3.0) if r_act_cubed > 0 else 0.0

    # Is defect active at R_eq and R_ext?
    active_Req = (xi * sqrt_K_Req > m0_sq)
    active_Rext = (xi * sqrt_K_Rext > m0_sq)

    return TriggerRegimeResult(
        sqrt_K_at_Req=sqrt_K_Req,
        sqrt_K_at_Rext=sqrt_K_Rext,
        sqrt_K_at_half=sqrt_K_half,
        core_to_exterior_ratio=ratio,
        K_crit=K_crit,
        activation_radius=r_act,
        active_at_Req=active_Req,
        active_at_Rext=active_Rext,
        activation_formula=(
            "Theta(r) = Heaviside(xi * sqrt(K)(r) - lambda * eta^2); "
            f"K_crit = lambda*eta^2/xi = {K_crit:.4f}; "
            f"r_act = {r_act:.4f}"
        ),
        notes=[
            f"sqrt(K) at R_eq={R_EQ:.4f}: {sqrt_K_Req:.4f}",
            f"sqrt(K) at R_ext={R_EXT:.4f}: {sqrt_K_Rext:.4f}",
            f"sqrt(K) at r=0.5: {sqrt_K_half:.4f}",
            f"Core-to-exterior ratio: {ratio:.1f}x",
            f"|m_0^2| = lam*eta^2 = {m0_sq:.4f}",
            f"K_crit = {K_crit:.4f}",
            f"Activation radius: r_act = {r_act:.4f}",
            f"Active at R_eq: {active_Req}",
            f"Active at R_ext: {active_Rext}",
        ],
    )


# ================================================================
# Level 2: Macro Sector
# ================================================================

def construct_macro_sector(
    r_grid: np.ndarray,
    scalar_A: float,
    params: CompanionParams,
) -> MacroSectorProfile:
    """Construct the macro scalar-memory sector.

    epsilon_macro = A^2 * M^2 / (2*tau^2*r^4) = A^2 * RHO_EQ_COEFF / r^4
    Sigma_macro   = A^2 * MASS_COEFF * (1/r - 1/R_ext)
    """
    M = params.M
    tau = params.tau
    R_ext = params.R_ext

    rho_eq_coeff = M ** 2 / (2.0 * tau ** 2)
    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2

    eps = scalar_A ** 2 * rho_eq_coeff / r_grid ** 4
    sig = scalar_A ** 2 * mass_coeff * (1.0 / r_grid - 1.0 / R_ext)

    # Sigma at R_eq
    sig_Req = scalar_A ** 2 * mass_coeff * (1.0 / R_EQ - 1.0 / R_ext)

    if abs(scalar_A - 1.0) < 0.01:
        label = "baseline_A1"
    elif abs(scalar_A - A_CRIT) < 0.01:
        label = "critical_Acrit"
    else:
        label = f"custom_A={scalar_A:.3f}"

    return MacroSectorProfile(
        scalar_A=scalar_A,
        r_grid=r_grid,
        epsilon_macro=eps,
        sigma_macro=sig,
        sigma_at_Req=sig_Req,
        label=label,
        notes=[
            f"Scalar amplitude A = {scalar_A:.4f}",
            f"epsilon_macro(R_eq) = {scalar_A**2 * rho_eq_coeff / R_EQ**4:.6f}",
            f"Sigma_macro(R_eq) = {sig_Req:.6f}",
        ],
    )


# ================================================================
# Level 3: Defect Sector
# ================================================================

def construct_defect_sector(
    params: CompanionParams,
    lam_override: Optional[float] = None,
) -> DefectSectorProfile:
    """Import D2 hedgehog BVP, solve, and interpolate onto interior grid.

    Returns defect energy density and Sigma_defect on interior grid [R_eq, R_ext].
    """
    lam = lam_override if lam_override is not None else params.lam

    # Build D2 params
    d2_params = NumericalMonopoleParams(
        eta=params.eta,
        lam=lam,
        r_min=params.r_min,
        r_max=params.r_max,
        n_grid=params.n_grid,
        M=params.M,
        tau=params.tau,
        R_ext=params.R_ext,
    )

    # Solve BVP
    bvp = solve_hedgehog_bvp(d2_params)

    # Extract energy profile
    energy = extract_defect_energy(bvp, d2_params)

    # Build interior grid [R_eq+epsilon, R_ext]
    n_int = params.n_interior
    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, n_int)

    # Interpolate defect epsilon onto interior grid
    eps_interp = np.interp(r_int, energy.r_grid, energy.total_epsilon)

    # Compute Sigma_defect
    sig_defect = _sigma_from_profile(r_int, eps_interp)

    # Sigma at R_eq
    sig_Req = float(sig_defect[0])

    # Tail analysis
    tail_exp = energy.tail_exponent
    tail_coeff = energy.tail_coefficient

    return DefectSectorProfile(
        lam=lam,
        bvp_converged=bvp.converged,
        r_interior=r_int,
        epsilon_defect=eps_interp,
        sigma_defect=sig_defect,
        sigma_at_Req=sig_Req,
        tail_exponent=tail_exp,
        tail_coefficient=tail_coeff,
        notes=[
            f"Lambda = {lam:.2f}",
            f"BVP converged: {bvp.converged}",
            f"Interior grid: [{R_EQ + 1e-6:.6f}, {params.R_ext:.4f}] ({n_int} pts)",
            f"Sigma_defect(R_eq) = {sig_Req:.6f}",
            f"Tail exponent: {tail_exp:.4f}",
            f"Tail coefficient: {tail_coeff:.6f}",
        ],
    )


# ================================================================
# Level 4: Dual-Sector Decomposition
# ================================================================

def decompose_dual_sector(
    macro: MacroSectorProfile,
    defect: DefectSectorProfile,
    params: CompanionParams,
) -> DualSectorDecomposition:
    """Combine macro + defect on interior grid.

    epsilon_total = epsilon_macro + epsilon_defect
    Sigma_total   = Sigma_macro + Sigma_defect

    Compare with epsilon_min = RHO_EQ_COEFF/r^4 + COMP_B_COEFF/r^2.
    """
    r = defect.r_interior

    # Macro onto same grid
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    rho_eq_coeff = M ** 2 / (2.0 * tau ** 2)
    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2

    eps_macro = macro.scalar_A ** 2 * rho_eq_coeff / r ** 4
    sig_macro = macro.scalar_A ** 2 * mass_coeff * (1.0 / r - 1.0 / R_ext)

    eps_defect = defect.epsilon_defect
    sig_defect = defect.sigma_defect

    eps_total = eps_macro + eps_defect
    sig_total = sig_macro + sig_defect

    # Target: epsilon_min = RHO_EQ_COEFF / r^4 + COMP_B_COEFF / r^2
    eps_min = rho_eq_coeff / r ** 4 + COMP_B_COEFF / r ** 2

    # Mean ratio (avoid division by zero)
    mask = eps_min > 1e-30
    if np.sum(mask) > 0:
        ratios = eps_total[mask] / eps_min[mask]
        ratio_mean = float(np.mean(ratios))
    else:
        ratio_mean = 0.0

    return DualSectorDecomposition(
        scalar_A=macro.scalar_A,
        label=macro.label,
        r_grid=r,
        epsilon_macro=eps_macro,
        epsilon_defect=eps_defect,
        epsilon_total=eps_total,
        sigma_macro=sig_macro,
        sigma_defect=sig_defect,
        sigma_total=sig_total,
        epsilon_min_target=eps_min,
        epsilon_ratio_mean=ratio_mean,
        notes=[
            f"Scalar A = {macro.scalar_A:.4f} ({macro.label})",
            f"Mean epsilon ratio (total/target): {ratio_mean:.4f}",
            f"Sigma_total(R_eq) = {float(sig_total[0]):.6f}",
        ],
    )


# ================================================================
# Level 5: Sector Dominance
# ================================================================

def analyze_sector_dominance(
    decomposition: DualSectorDecomposition,
    params: CompanionParams,
) -> SectorDominanceResult:
    """Find crossover radius and dominance ratios."""
    r = decomposition.r_grid
    eps_m = decomposition.epsilon_macro
    eps_d = decomposition.epsilon_defect

    # Find crossover: where |macro - defect| is minimized
    diff = eps_m - eps_d
    # Look for sign change
    crossover_r = float("nan")
    for i in range(len(diff) - 1):
        if diff[i] * diff[i + 1] < 0:
            # Linear interpolation
            frac = abs(diff[i]) / (abs(diff[i]) + abs(diff[i + 1]))
            crossover_r = float(r[i] + frac * (r[i + 1] - r[i]))
            break

    if math.isnan(crossover_r):
        # No crossover — one dominates everywhere
        if diff[0] > 0:
            crossover_r = float(r[-1])  # macro always dominates
        else:
            crossover_r = float(r[0])  # defect always dominates

    # Dominance at inner and outer edges
    macro_dom_inner = bool(eps_m[0] > eps_d[0])
    defect_dom_outer = bool(eps_d[-1] > eps_m[-1])

    # Ratios at key radii
    ratio_Req = float(eps_m[0] / eps_d[0]) if eps_d[0] > 1e-30 else float("inf")
    ratio_Rext = float(eps_m[-1] / eps_d[-1]) if eps_d[-1] > 1e-30 else float("inf")

    return SectorDominanceResult(
        crossover_radius=crossover_r,
        macro_dominates_inner=macro_dom_inner,
        defect_dominates_outer=defect_dom_outer,
        ratio_at_Req=ratio_Req,
        ratio_at_Rext=ratio_Rext,
        notes=[
            f"Crossover radius: {crossover_r:.4f}",
            f"Macro dominates inner (R_eq): {macro_dom_inner}",
            f"Defect dominates outer (R_ext): {defect_dom_outer}",
            f"Macro/defect ratio at R_eq: {ratio_Req:.4f}",
            f"Macro/defect ratio at R_ext: {ratio_Rext:.6f}",
        ],
    )


# ================================================================
# Level 6: Metric Injection
# ================================================================

def inject_companion_metric(
    decomposition: DualSectorDecomposition,
    params: CompanionParams,
) -> CompanionMetricInjectionResult:
    """Inject combined source into metric: f_corrected = -2*(delta - Sigma_total)/r.

    delta(r) = m(r) - r/2
    m(r) = M + MASS_COEFF * (1/r - 1/R_ext)
    """
    r = decomposition.r_grid
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2

    # Static mass profile
    m_r = M + mass_coeff * (1.0 / r - 1.0 / R_ext)
    delta = m_r - r / 2.0

    sig_total = decomposition.sigma_total

    # Corrected metric
    f_corrected = -2.0 * (delta - sig_total) / r

    f_min = float(np.min(f_corrected))
    f_min_idx = int(np.argmin(f_corrected))
    f_min_r = float(r[f_min_idx])
    metric_pos = bool(f_min > 0)

    # Budget at key radii
    budget: Dict[str, Dict[str, float]] = {}
    for r_key in KEY_RADII:
        if R_EQ <= r_key <= R_ext:
            idx = int(np.argmin(np.abs(r - r_key)))
            budget[f"r={r_key:.4f}"] = {
                "delta": float(delta[idx]),
                "sigma_macro": float(decomposition.sigma_macro[idx]),
                "sigma_defect": float(decomposition.sigma_defect[idx]),
                "sigma_total": float(sig_total[idx]),
                "f_corrected": float(f_corrected[idx]),
                "deficit_closed": bool(sig_total[idx] >= delta[idx]),
            }

    return CompanionMetricInjectionResult(
        scalar_A=decomposition.scalar_A,
        label=decomposition.label,
        r_grid=r,
        delta=delta,
        sigma_total=sig_total,
        f_corrected=f_corrected,
        f_min=f_min,
        f_min_radius=f_min_r,
        metric_positive=metric_pos,
        budget=budget,
        notes=[
            f"Scalar A = {decomposition.scalar_A:.4f} ({decomposition.label})",
            f"f_min = {f_min:.6f} at r = {f_min_r:.4f}",
            f"Metric globally positive: {metric_pos}",
        ],
    )


# ================================================================
# Level 7: Lambda Scan
# ================================================================

def scan_lambda_companion(
    params: CompanionParams,
) -> CompanionLambdaScanResult:
    """Scan lambda at both macro baselines (A=1 and A=A_crit).

    For each lambda:
      1. Construct defect sector (BVP at this lambda)
      2. Construct macro at A=1 and A=A_crit
      3. Combine, inject, record f_min
    """
    entries: List[CompanionLambdaScanEntry] = []

    for lam_val in params.lambda_scan:
        # Defect at this lambda
        defect = construct_defect_sector(params, lam_override=lam_val)

        results = {}
        for scalar_A, key in [(1.0, "A1"), (A_CRIT, "Acrit")]:
            r_int = defect.r_interior
            macro = construct_macro_sector(r_int, scalar_A, params)
            decomp = decompose_dual_sector(macro, defect, params)
            metric = inject_companion_metric(decomp, params)
            results[key] = metric

        # Defect fraction at R_eq for A=1
        sig_d_Req = defect.sigma_at_Req
        sig_t_A1 = float(results["A1"].sigma_total[0])
        frac_A1 = sig_d_Req / sig_t_A1 if sig_t_A1 > 1e-30 else 0.0

        sig_t_Acrit = float(results["Acrit"].sigma_total[0])
        frac_Acrit = sig_d_Req / sig_t_Acrit if sig_t_Acrit > 1e-30 else 0.0

        entries.append(CompanionLambdaScanEntry(
            lam=lam_val,
            bvp_converged=defect.bvp_converged,
            f_min_A1=results["A1"].f_min,
            metric_positive_A1=results["A1"].metric_positive,
            sigma_defect_fraction_A1=frac_A1,
            f_min_Acrit=results["Acrit"].f_min,
            metric_positive_Acrit=results["Acrit"].metric_positive,
            sigma_defect_fraction_Acrit=frac_Acrit,
            notes=f"lam={lam_val:.1f}",
        ))

    n_scanned = len(entries)
    n_conv = sum(1 for e in entries if e.bvp_converged)

    # A=1 summary
    pos_A1 = [e for e in entries if e.metric_positive_A1]
    n_pos_A1 = len(pos_A1)
    if pos_A1:
        best_A1 = max(pos_A1, key=lambda e: e.f_min_A1)
        best_lam_A1 = best_A1.lam
        best_fmin_A1 = best_A1.f_min_A1
    else:
        # Take least negative
        best_entry_A1 = max(entries, key=lambda e: e.f_min_A1)
        best_lam_A1 = best_entry_A1.lam
        best_fmin_A1 = best_entry_A1.f_min_A1

    # A=A_crit summary
    pos_Acrit = [e for e in entries if e.metric_positive_Acrit]
    n_pos_Acrit = len(pos_Acrit)
    if pos_Acrit:
        best_Acrit = max(pos_Acrit, key=lambda e: e.f_min_Acrit)
        best_lam_Acrit = best_Acrit.lam
        best_fmin_Acrit = best_Acrit.f_min_Acrit
    else:
        best_entry_Acrit = max(entries, key=lambda e: e.f_min_Acrit)
        best_lam_Acrit = best_entry_Acrit.lam
        best_fmin_Acrit = best_entry_Acrit.f_min_Acrit

    return CompanionLambdaScanResult(
        entries=entries,
        n_scanned=n_scanned,
        n_converged=n_conv,
        n_positive_A1=n_pos_A1,
        best_lambda_A1=best_lam_A1,
        best_fmin_A1=best_fmin_A1,
        n_positive_Acrit=n_pos_Acrit,
        best_lambda_Acrit=best_lam_Acrit,
        best_fmin_Acrit=best_fmin_Acrit,
        notes=[
            f"Scanned {n_scanned} lambda values, {n_conv} converged.",
            f"A=1: {n_pos_A1} positive, best fmin = {best_fmin_A1:.6f} at lam = {best_lam_A1}",
            f"A=A_crit: {n_pos_Acrit} positive, best fmin = {best_fmin_Acrit:.6f} at lam = {best_lam_Acrit}",
        ],
    )


# ================================================================
# Level 8: Cross-Term Inventory
# ================================================================

def inventory_cross_terms(params: CompanionParams) -> CrossTermInventory:
    """Document the neglected cross-terms in the additive approximation."""
    entries = [
        CrossTermEntry(
            name="back_reaction",
            description=(
                "Defect stress-energy modifies the metric, which modifies "
                "the BVP domain boundaries and the static mass profile."
            ),
            severity="moderate",
            physical_effect=(
                "The corrected metric differs from Schwarzschild; the defect "
                "BVP should be solved on the corrected background."
            ),
        ),
        CrossTermEntry(
            name="scalar_defect_coupling",
            description=(
                "The scalar-memory field Phi and the hedgehog triplet phi^a "
                "may interact via a portal coupling |Phi|^2 |phi|^2 or similar."
            ),
            severity="moderate",
            physical_effect=(
                "Could enhance or suppress either sector's effective mass, "
                "modifying the energy density profiles."
            ),
        ),
        CrossTermEntry(
            name="trigger_self_consistency",
            description=(
                "The Kretschner scalar sqrt(K) is evaluated on the Schwarzschild "
                "background, not the corrected metric."
            ),
            severity="minor",
            physical_effect=(
                "The true curvature trigger may differ from the Schwarzschild "
                "estimate, shifting the activation radius."
            ),
        ),
        CrossTermEntry(
            name="defect_feedback_on_macro_driver",
            description=(
                "The defect sector modifies the effective gravitational source "
                "X(r) that drives the macro scalar-memory amplitude. This is "
                "the main physical approximation in the Companion model."
            ),
            severity="significant",
            physical_effect=(
                "The macro amplitude A is treated as a free parameter, but in "
                "a self-consistent theory it would depend on the total "
                "stress-energy (including the defect contribution)."
            ),
        ),
    ]

    return CrossTermInventory(
        entries=entries,
        n_cross_terms=len(entries),
        additive_approximation_justified=False,
        main_approximation=(
            "Defect feedback on macro driver X(r) is neglected. The macro "
            "amplitude A is treated as a free parameter independent of the "
            "defect sector."
        ),
        notes=[
            f"{len(entries)} cross-terms documented.",
            "Additive approximation is a working hypothesis, not justified "
            "from first principles.",
            "The most significant cross-term is defect feedback on the macro "
            "driver — the main physical approximation.",
        ],
    )


# ================================================================
# Level 9: Classification
# ================================================================

def classify_companion(
    lambda_scan: CompanionLambdaScanResult,
    cross_terms: CrossTermInventory,
    trigger: TriggerRegimeResult,
    params: CompanionParams,
) -> CompanionClassification:
    """Classify the companion architecture result.

    Options:
      - companion_architecture_viable:       A=1 + defect gives f > 0 in some lambda window
      - dual_sector_partially_viable:        A=A_crit + defect gives f > 0 but A=1 does not
      - dual_sector_insufficient:            Neither baseline gives f > 0
      - trigger_regime_incorrect:            Trigger not active at R_eq
      - unresolved_cross_terms:              Cross-terms dominate uncertainty
    """
    # Check trigger
    if not trigger.active_at_Req:
        classification = "trigger_regime_incorrect"
        summary = (
            "Curvature trigger not active at R_eq — defect sector not "
            "expected to contribute in the relevant domain."
        )
    elif lambda_scan.n_positive_A1 > 0:
        classification = "companion_architecture_viable"
        summary = (
            f"A=1 + defect restores metric positivity for "
            f"{lambda_scan.n_positive_A1} lambda values. "
            f"Best f_min = {lambda_scan.best_fmin_A1:.6f} at "
            f"lambda = {lambda_scan.best_lambda_A1}."
        )
    elif lambda_scan.n_positive_Acrit > 0:
        classification = "dual_sector_partially_viable"
        summary = (
            f"A=A_crit + defect restores metric positivity for "
            f"{lambda_scan.n_positive_Acrit} lambda values, "
            f"but A=1 does not. This is the weaker result "
            f"('overshoot + defect')."
        )
    else:
        classification = "dual_sector_insufficient"
        summary = (
            "Neither A=1 nor A=A_crit + defect restores metric positivity "
            "at any scanned lambda."
        )

    # Viable lambda windows
    viable_A1 = [e.lam for e in lambda_scan.entries if e.metric_positive_A1]
    viable_Acrit = [e.lam for e in lambda_scan.entries if e.metric_positive_Acrit]

    phase_status = f"ASSESSED ({classification})"

    phase_lock = {
        "phase_6_f_Req": "LOCKED (-17.71)",
        "phase_6B_A_crit": "LOCKED (1.062)",
        "phase_6C_deficit": "LOCKED (Component A + Component B)",
        "route_C": "LOCKED (insufficient)",
        "route_B": "LOCKED (closed)",
        "source_law_I": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "LOCKED (provisional candidate formulated)",
        "defect_D2": "LOCKED (defect_candidate_numerically_viable)",
        "unification_D3": "LOCKED (scalar_triplet_embedding_most_promising)",
        "unification_D4": "LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified)",
        "source_coupled_D5": "LOCKED (source_coupling_insufficient)",
        "companion_D6": phase_status,
    }

    return CompanionClassification(
        classification=classification,
        phase_status=phase_status,
        metric_positive_A1=lambda_scan.n_positive_A1 > 0,
        metric_positive_Acrit=lambda_scan.n_positive_Acrit > 0,
        best_fmin_A1=lambda_scan.best_fmin_A1,
        best_fmin_Acrit=lambda_scan.best_fmin_Acrit,
        viable_lambda_window_A1=viable_A1,
        viable_lambda_window_Acrit=viable_Acrit,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 10: Master Computation
# ================================================================

def compute_companion_architecture(
    params: Optional[CompanionParams] = None,
) -> CompanionArchitectureResult:
    """Run the full Phase D6 companion architecture analysis."""
    if params is None:
        params = CompanionParams()

    result = CompanionArchitectureResult(
        valid=True,
        params=params,
        nonclaims=list(COMPANION_NONCLAIMS),
        assumptions=list(COMPANION_ASSUMPTIONS),
    )

    # Level 0: Architecture definition
    result.architecture = define_architecture(params)

    # Level 1: Trigger regime
    result.trigger_regime = verify_trigger_regime(params)

    # Level 3: Defect sector (at default lambda)
    result.defect_sector = construct_defect_sector(params)

    # Build interior grid from defect
    r_int = result.defect_sector.r_interior

    # Level 2: Macro sectors (both baselines)
    result.macro_baseline = construct_macro_sector(r_int, 1.0, params)
    result.macro_critical = construct_macro_sector(r_int, A_CRIT, params)

    # Level 4: Dual-sector decomposition (both baselines)
    result.decomposition_A1 = decompose_dual_sector(
        result.macro_baseline, result.defect_sector, params
    )
    result.decomposition_Acrit = decompose_dual_sector(
        result.macro_critical, result.defect_sector, params
    )

    # Level 5: Sector dominance (at A=1 baseline)
    result.dominance = analyze_sector_dominance(result.decomposition_A1, params)

    # Level 6: Metric injection (both baselines)
    result.metric_A1 = inject_companion_metric(result.decomposition_A1, params)
    result.metric_Acrit = inject_companion_metric(result.decomposition_Acrit, params)

    # Level 7: Lambda scan
    result.lambda_scan = scan_lambda_companion(params)

    # Level 8: Cross-term inventory
    result.cross_terms = inventory_cross_terms(params)

    # Level 9: Classification
    result.classification = classify_companion(
        result.lambda_scan,
        result.cross_terms,
        result.trigger_regime,
        params,
    )

    return result


# ================================================================
# Level 11: Serialization
# ================================================================

def companion_architecture_result_to_dict(
    result: CompanionArchitectureResult,
) -> Dict[str, Any]:
    """Serialize the full result to a JSON-compatible dict."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "phase": "D6",
        "title": "Companion Architecture and Dual-Sector Metric Integration",
    }

    # Architecture
    if result.architecture:
        a = result.architecture
        d["architecture"] = {
            "n_sectors": a.n_sectors,
            "sector_names": a.sector_names,
            "combination_rule": a.combination_rule,
            "cross_term_treatment": a.cross_term_treatment,
            "notes": a.notes,
        }

    # Trigger regime
    if result.trigger_regime:
        t = result.trigger_regime
        d["trigger_regime"] = {
            "sqrt_K_at_Req": t.sqrt_K_at_Req,
            "sqrt_K_at_Rext": t.sqrt_K_at_Rext,
            "core_to_exterior_ratio": t.core_to_exterior_ratio,
            "K_crit": t.K_crit,
            "activation_radius": t.activation_radius,
            "active_at_Req": t.active_at_Req,
            "active_at_Rext": t.active_at_Rext,
            "activation_formula": t.activation_formula,
        }

    # Macro sectors
    for key, macro in [("macro_baseline", result.macro_baseline),
                       ("macro_critical", result.macro_critical)]:
        if macro:
            d[key] = {
                "scalar_A": macro.scalar_A,
                "sigma_at_Req": macro.sigma_at_Req,
                "label": macro.label,
                "notes": macro.notes,
            }

    # Defect sector
    if result.defect_sector:
        ds = result.defect_sector
        d["defect_sector"] = {
            "lam": ds.lam,
            "bvp_converged": ds.bvp_converged,
            "sigma_at_Req": ds.sigma_at_Req,
            "tail_exponent": ds.tail_exponent,
            "tail_coefficient": ds.tail_coefficient,
            "notes": ds.notes,
        }

    # Decompositions
    for key, decomp in [("decomposition_A1", result.decomposition_A1),
                        ("decomposition_Acrit", result.decomposition_Acrit)]:
        if decomp:
            d[key] = {
                "scalar_A": decomp.scalar_A,
                "label": decomp.label,
                "epsilon_ratio_mean": decomp.epsilon_ratio_mean,
                "notes": decomp.notes,
            }

    # Dominance
    if result.dominance:
        dom = result.dominance
        d["dominance"] = {
            "crossover_radius": dom.crossover_radius,
            "macro_dominates_inner": dom.macro_dominates_inner,
            "defect_dominates_outer": dom.defect_dominates_outer,
            "ratio_at_Req": dom.ratio_at_Req,
            "ratio_at_Rext": dom.ratio_at_Rext,
        }

    # Metric injection
    for key, met in [("metric_A1", result.metric_A1),
                     ("metric_Acrit", result.metric_Acrit)]:
        if met:
            d[key] = {
                "scalar_A": met.scalar_A,
                "label": met.label,
                "f_min": met.f_min,
                "f_min_radius": met.f_min_radius,
                "metric_positive": met.metric_positive,
                "budget": met.budget,
                "notes": met.notes,
            }

    # Lambda scan
    if result.lambda_scan:
        ls = result.lambda_scan
        d["lambda_scan"] = {
            "n_scanned": ls.n_scanned,
            "n_converged": ls.n_converged,
            "n_positive_A1": ls.n_positive_A1,
            "best_lambda_A1": ls.best_lambda_A1,
            "best_fmin_A1": ls.best_fmin_A1,
            "n_positive_Acrit": ls.n_positive_Acrit,
            "best_lambda_Acrit": ls.best_lambda_Acrit,
            "best_fmin_Acrit": ls.best_fmin_Acrit,
            "entries": [
                {
                    "lam": e.lam,
                    "bvp_converged": e.bvp_converged,
                    "f_min_A1": e.f_min_A1,
                    "metric_positive_A1": e.metric_positive_A1,
                    "sigma_defect_fraction_A1": e.sigma_defect_fraction_A1,
                    "f_min_Acrit": e.f_min_Acrit,
                    "metric_positive_Acrit": e.metric_positive_Acrit,
                    "sigma_defect_fraction_Acrit": e.sigma_defect_fraction_Acrit,
                }
                for e in ls.entries
            ],
            "notes": ls.notes,
        }

    # Cross-terms
    if result.cross_terms:
        ct = result.cross_terms
        d["cross_terms"] = {
            "n_cross_terms": ct.n_cross_terms,
            "additive_approximation_justified": ct.additive_approximation_justified,
            "main_approximation": ct.main_approximation,
            "entries": [
                {
                    "name": e.name,
                    "description": e.description,
                    "severity": e.severity,
                    "physical_effect": e.physical_effect,
                }
                for e in ct.entries
            ],
            "notes": ct.notes,
        }

    # Classification
    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "metric_positive_A1": cl.metric_positive_A1,
            "metric_positive_Acrit": cl.metric_positive_Acrit,
            "best_fmin_A1": cl.best_fmin_A1,
            "best_fmin_Acrit": cl.best_fmin_Acrit,
            "viable_lambda_window_A1": cl.viable_lambda_window_A1,
            "viable_lambda_window_Acrit": cl.viable_lambda_window_Acrit,
            "summary": cl.summary,
        }

    # Nonclaims & assumptions
    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
