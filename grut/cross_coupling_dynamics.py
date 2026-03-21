"""Phase D7 — Cross-Coupling Dynamics and Back-Reaction Test.

Tests whether cross-coupling between the macro (scalar-memory) and defect
(hedgehog) sectors preserves, shifts, or destroys the D6 metric rescue.

SCOPE: D7 is a back-reaction stress test, not a final derivation of the
coupled Companion theory.  The alpha_BR and beta_XR channels are effective
phenomenological response channels — structurally motivated proxies for the
leading unresolved interactions identified in the D6 cross-term inventory.
They are not yet derived from a dual-sector action.

Two effective response channels:

  Channel 1 — Gravitational back-reaction (alpha_BR):
    The defect energy gravitates, increasing the enclosed mass.
    DESTRUCTIVE: reduces the net metric benefit of the defect sector.

  Channel 2 — Source amplification (beta_XR):
    The defect modifies the effective gravitational source, amplifying the
    macro amplitude.
    CONSTRUCTIVE: increases the macro Sigma contribution.

LEADING APPROXIMATIONS:
  1. Defect-shape freezing: hedgehog profile held fixed on Schwarzschild
     background while coupling channels modify the metric budget.
  2. Effective phenomenological channels: alpha_BR, beta_XR are scanned
     proxies, not derived coupling constants.
  3. Linear amplitude model: A_eff(r) = A_0 * m_eff(r)/M.

Imports: solve_hedgehog_bvp, extract_defect_energy from grut.numerical_monopole.
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
ETA_SQUARED = ETA_TARGET ** 2
LAMBDA_DEFAULT = 8.0 * math.pi

MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
R_EXT = 2.0 * R_S

KRETSCHNER_COEFF = 48.0 * M_EXT ** 2
XI_DEFAULT = 1.0

# D7-specific
ALPHA_BR_SCAN = [0.0, 0.25, 0.5, 0.75, 1.0]
BETA_XR_SCAN = [0.0, 0.25, 0.5, 0.75, 1.0]
LAMBDA_SCAN_VALUES = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]
N_INTERACTION_CHANNELS = 2
UNIT_BENCHMARK = (1.0, 1.0)  # canonical reference, not physically derived

# Key radii for accounting
KEY_RADII = [R_EQ, 0.5, 0.75, 1.0]


# ================================================================
# Assumptions
# ================================================================

CROSS_COUPLING_ASSUMPTIONS = [
    "1. Two effective phenomenological response channels tested: gravitational "
    "back-reaction (alpha_BR) and source amplification (beta_XR).",

    "2. Gravitational back-reaction: defect energy increases enclosed mass by "
    "alpha_BR * Sigma_defect(r), increasing the deficit.",

    "3. Source amplification: defect modifies effective gravitational source, "
    "changing macro amplitude to A_eff(r) = A_0 * m_eff(r)/M.",

    "4. Defect-shape freezing: the hedgehog BVP solution is held fixed on "
    "Schwarzschild background. This is the leading technical approximation.",

    "5. Coupling strengths scanned over [0, 0.25, 0.5, 0.75, 1.0] for each "
    "channel. The (1,1) point is a unit-normalized benchmark, not derived.",

    "6. A_eff(r) is radius-dependent; Sigma_macro_coupled computed numerically.",

    "7. At alpha_BR=0, beta_XR=0 the D6 additive result is exactly recovered.",

    "8. Lambda scan inherited from D6: [5, 10, 25, 50, 100, 200].",

    "9. Focus on A=1 baseline (the strong D6 result).",

    "10. D7 is a back-reaction stress test, not a final coupled derivation.",
]

CROSS_COUPLING_NONCLAIMS = [
    "1. This phase does NOT prove the final unified field theory.",

    "2. A surviving D7 result establishes coupled viability in the tested "
    "framework, not final canon.",

    "3. A failed D7 result does NOT invalidate D1-D6; it shows the Companion "
    "architecture needs revision beyond the additive approximation.",

    "4. The alpha_BR and beta_XR channels are effective phenomenological "
    "proxies, not unique derivations from a dual-sector action.",

    "5. The defect-shape freezing approximation may miss important "
    "self-consistent profile modifications.",

    "6. The linear amplitude model A_eff = A_0 * m_eff/M is a leading-order "
    "approximation. Nonlinear responses are not tested.",

    "7. The coupling-strength scan is bounded, not exhaustive.",

    "8. The (1,1) unit benchmark is a canonical reference point, not a "
    "physically derived coupling strength.",

    "9. This phase does NOT justify metaphysical or observer-based interpretation.",

    "10. Classification is within the D7 numerical framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class CrossCouplingParams:
    """Parameters for Phase D7."""
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
    scalar_A: float = 1.0  # baseline macro amplitude (A=1 is the strong D6 result)
    alpha_BR: float = 1.0  # gravitational back-reaction strength
    beta_XR: float = 1.0   # source amplification strength
    alpha_BR_scan: List[float] = field(
        default_factory=lambda: list(ALPHA_BR_SCAN)
    )
    beta_XR_scan: List[float] = field(
        default_factory=lambda: list(BETA_XR_SCAN)
    )
    lambda_scan: List[float] = field(
        default_factory=lambda: list(LAMBDA_SCAN_VALUES)
    )


@dataclass
class InteractionChannelDefinition:
    """One effective response channel."""
    name: str
    parameter: str
    formula: str
    physical_mechanism: str
    effect_on_metric: str  # "destructive" or "constructive"
    d6_limit: str
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledModelDefinition:
    """Level 0: Full coupled model documentation."""
    n_channels: int
    channels: List[InteractionChannelDefinition]
    combined_formula: str
    d6_recovery_condition: str
    unit_benchmark: Tuple[float, float]
    scope_statement: str
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledSectorProfiles:
    """Level 1: Computed sectors with coupling active."""
    alpha_BR: float
    beta_XR: float
    scalar_A: float
    lam: float
    r_grid: np.ndarray
    # Defect (unchanged under coupling — frozen-profile approximation)
    epsilon_defect: np.ndarray
    sigma_defect: np.ndarray
    sigma_defect_at_Req: float
    bvp_converged: bool
    # Coupled macro
    A_eff: np.ndarray
    A_eff_at_Req: float
    epsilon_macro_coupled: np.ndarray
    sigma_macro_coupled: np.ndarray
    sigma_macro_coupled_at_Req: float
    # Totals
    sigma_total: np.ndarray
    # D6 reference
    sigma_macro_d6_at_Req: float
    sigma_total_d6_at_Req: float
    notes: List[str] = field(default_factory=list)


@dataclass
class BackReactionAssessment:
    """Level 2: Per-channel back-reaction classification."""
    alpha_BR: float
    beta_XR: float
    # Gravitational channel (destructive)
    delta_increase_at_Req: float
    # Source amplification channel (constructive)
    sigma_macro_increase_at_Req: float
    A_eff_at_Req: float
    amplification_factor: float  # A_eff^2 / A_0^2
    # Net effect
    net_metric_shift_at_Req: float  # f_coupled(R_eq) - f_d6(R_eq)
    net_classification: str  # "constructive", "destructive", "neutral"
    constructive_dominates: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledMetricInjectionResult:
    """Level 3: Metric injection with both channels."""
    alpha_BR: float
    beta_XR: float
    scalar_A: float
    lam: float
    r_grid: np.ndarray
    delta_coupled: np.ndarray
    sigma_total_coupled: np.ndarray
    f_coupled: np.ndarray
    f_min: float
    f_min_radius: float
    metric_positive: bool
    f_at_Req: float
    f_d6_at_Req: float
    metric_shift: float  # f_coupled(R_eq) - f_d6(R_eq)
    budget: Dict[str, Dict[str, float]]
    notes: List[str] = field(default_factory=list)


@dataclass
class CouplingStrengthScanEntry:
    """One point in the (alpha_BR, beta_XR) scan."""
    alpha_BR: float
    beta_XR: float
    f_min: float
    f_at_Req: float
    metric_positive: bool
    A_eff_at_Req: float
    net_classification: str
    notes: str = ""


@dataclass
class CouplingStrengthScanResult:
    """Level 4: Full 5x5 coupling strength scan."""
    entries: List[CouplingStrengthScanEntry]
    n_scanned: int
    n_positive: int
    # Unit benchmark result
    unit_benchmark_f_min: float
    unit_benchmark_positive: bool
    unit_benchmark_classification: str
    # Three named slices
    pure_backreaction: Optional[CouplingStrengthScanEntry]  # (1,0)
    pure_amplification: Optional[CouplingStrengthScanEntry]  # (0,1)
    unit_benchmark_entry: Optional[CouplingStrengthScanEntry]  # (1,1)
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledLambdaScanEntry:
    """One lambda in the coupled scan."""
    lam: float
    bvp_converged: bool
    f_min_d6: float
    f_min_coupled: float
    metric_positive_d6: bool
    metric_positive_coupled: bool
    f_shift: float  # coupled - D6
    net_classification: str
    notes: str = ""


@dataclass
class CoupledLambdaScanResult:
    """Level 5: Lambda scan at unit benchmark vs D6 baseline."""
    entries: List[CoupledLambdaScanEntry]
    n_scanned: int
    n_converged: int
    n_positive_d6: int
    n_positive_coupled: int
    best_lambda_coupled: Optional[float]
    best_fmin_coupled: float
    rescue_preserved: bool  # coupled still positive for lambda >= 25?
    viable_lambda_d6: List[float]
    viable_lambda_coupled: List[float]
    threshold_shift: str  # "unchanged", "lower", "higher", "destroyed"
    notes: List[str] = field(default_factory=list)


@dataclass
class CrossCouplingClassification:
    """Level 6: Final D7 classification."""
    classification: str
    phase_status: str
    d6_additive_pessimistic: bool  # True if back-reaction helps
    unit_benchmark_positive: bool
    viable_lambda_window_coupled: List[float]
    viable_lambda_window_d6: List[float]
    threshold_shift: str
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class CrossCouplingResult:
    """Master result container for Phase D7."""
    valid: bool
    params: CrossCouplingParams
    model_definition: Optional[CoupledModelDefinition] = None
    coupled_sectors: Optional[CoupledSectorProfiles] = None
    back_reaction: Optional[BackReactionAssessment] = None
    metric_injection: Optional[CoupledMetricInjectionResult] = None
    coupling_scan: Optional[CouplingStrengthScanResult] = None
    lambda_scan: Optional[CoupledLambdaScanResult] = None
    classification: Optional[CrossCouplingClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)


# ================================================================
# Helpers
# ================================================================

def _sigma_from_profile(r: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """Compute Sigma(r) = integral_r^r_max 4*pi*r'^2 * epsilon(r') dr'.

    Cumulative trapezoid from the right.  Reimplemented locally.
    """
    integrand = 4.0 * math.pi * r ** 2 * epsilon
    sigma = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = r[i + 1] - r[i]
        sigma[i] = sigma[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * dr
    return sigma


def _solve_defect_on_grid(
    params: CrossCouplingParams,
    lam_override: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, bool]:
    """Solve D2 BVP and return (r_interior, epsilon_defect, sigma_defect, converged).

    Shared helper: solves BVP once, interpolates onto interior grid.
    """
    lam = lam_override if lam_override is not None else params.lam

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

    bvp = solve_hedgehog_bvp(d2_params)
    energy = extract_defect_energy(bvp, d2_params)

    n_int = params.n_interior
    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, n_int)
    eps_interp = np.interp(r_int, energy.r_grid, energy.total_epsilon)
    sig_defect = _sigma_from_profile(r_int, eps_interp)

    return r_int, eps_interp, sig_defect, bvp.converged


def _compute_coupled_macro(
    r: np.ndarray,
    sigma_defect: np.ndarray,
    scalar_A: float,
    beta_XR: float,
    M: float,
    tau: float,
    R_ext: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute coupled macro sector: A_eff, epsilon, sigma.

    Returns (A_eff, epsilon_macro_coupled, sigma_macro_coupled).
    """
    rho_eq_coeff = M ** 2 / (2.0 * tau ** 2)

    # m_eff(r) = M + beta_XR * sigma_defect(r)
    m_eff = M + beta_XR * sigma_defect

    # A_eff(r) = A_0 * m_eff(r) / M  (radius-dependent)
    A_eff = scalar_A * m_eff / M

    # epsilon_macro_coupled(r) = A_eff(r)^2 * RHO_EQ_COEFF / r^4
    eps_macro = A_eff ** 2 * rho_eq_coeff / r ** 4

    # Sigma_macro_coupled: numerical integral (no longer analytic)
    sig_macro = _sigma_from_profile(r, eps_macro)

    return A_eff, eps_macro, sig_macro


def _compute_d6_reference(
    r_Req: float,
    sigma_defect_Req: float,
    scalar_A: float,
    M: float,
    tau: float,
    R_ext: float,
) -> Tuple[float, float, float]:
    """Compute D6 additive reference values at R_eq.

    Returns (sigma_macro_d6, sigma_total_d6, f_d6) at R_eq.
    """
    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2
    sig_macro_d6 = scalar_A ** 2 * mass_coeff * (1.0 / r_Req - 1.0 / R_ext)
    sig_total_d6 = sig_macro_d6 + sigma_defect_Req

    # f_d6 at R_eq
    m_static = M + mass_coeff * (1.0 / r_Req - 1.0 / R_ext)
    delta_static = m_static - r_Req / 2.0
    f_d6 = -2.0 * (delta_static - sig_total_d6) / r_Req

    return sig_macro_d6, sig_total_d6, f_d6


# ================================================================
# Level 0: Coupled Model Definition
# ================================================================

def define_coupled_model(params: CrossCouplingParams) -> CoupledModelDefinition:
    """Document the two effective response channels."""
    ch1 = InteractionChannelDefinition(
        name="gravitational_back_reaction",
        parameter="alpha_BR",
        formula="m_coupled(r) = m_static(r) + alpha_BR * Sigma_defect(r)",
        physical_mechanism=(
            "Defect energy density gravitates, increasing the enclosed mass "
            "and worsening the metric deficit."
        ),
        effect_on_metric="destructive",
        d6_limit="alpha_BR = 0 recovers D6 additive (defect does not gravitate)",
        notes=[
            "At alpha_BR = 1: defect contribution to Sigma is exactly cancelled "
            "by the increase in delta.",
            "Net defect benefit scaled by (1 - alpha_BR).",
        ],
    )

    ch2 = InteractionChannelDefinition(
        name="source_amplification",
        parameter="beta_XR",
        formula="A_eff(r) = A_0 * (M + beta_XR * Sigma_defect(r)) / M",
        physical_mechanism=(
            "Defect modifies the effective gravitational source X_eff(r), "
            "amplifying the macro scalar-memory amplitude."
        ),
        effect_on_metric="constructive",
        d6_limit="beta_XR = 0 recovers D6 additive (macro amplitude unchanged)",
        notes=[
            "A_eff is radius-dependent: largest at small r where Sigma_defect "
            "is largest.",
            "Sigma_macro_coupled must be computed numerically (no longer analytic).",
        ],
    )

    return CoupledModelDefinition(
        n_channels=N_INTERACTION_CHANNELS,
        channels=[ch1, ch2],
        combined_formula=(
            "delta_coupled = m_static + alpha_BR*Sigma_defect - r/2; "
            "Sigma_total = Sigma_macro_coupled(A_eff) + Sigma_defect; "
            "f_coupled = -2*(delta_coupled - Sigma_total)/r"
        ),
        d6_recovery_condition="alpha_BR = 0, beta_XR = 0",
        unit_benchmark=UNIT_BENCHMARK,
        scope_statement=(
            "D7 is a back-reaction stress test using effective phenomenological "
            "response channels. The alpha_BR and beta_XR parameters are "
            "structurally motivated proxies, not derived from a dual-sector "
            "action. The defect profile is frozen (not re-solved under coupling)."
        ),
        notes=[
            "Two competing effects: gravitational penalty (destructive) vs "
            "source amplification (constructive).",
            "The (1,1) unit benchmark tests full-strength coupling in both channels.",
            "D6 additive result recovered exactly at (0,0).",
        ],
    )


# ================================================================
# Level 1: Coupled Sector Profiles
# ================================================================

def compute_coupled_sectors(
    params: CrossCouplingParams,
    lam_override: Optional[float] = None,
    defect_cache: Optional[Tuple[np.ndarray, np.ndarray, np.ndarray, bool]] = None,
) -> CoupledSectorProfiles:
    """Compute defect (frozen) + coupled macro profiles.

    If defect_cache is provided, reuse the BVP solution (optimization for scans).
    """
    lam = lam_override if lam_override is not None else params.lam

    if defect_cache is not None:
        r_int, eps_defect, sig_defect, converged = defect_cache
    else:
        r_int, eps_defect, sig_defect, converged = _solve_defect_on_grid(
            params, lam_override=lam
        )

    sigma_defect_Req = float(sig_defect[0])

    # Coupled macro
    A_eff, eps_macro, sig_macro = _compute_coupled_macro(
        r_int, sig_defect, params.scalar_A, params.beta_XR,
        params.M, params.tau, params.R_ext,
    )
    sig_macro_Req = float(sig_macro[0])
    A_eff_Req = float(A_eff[0])

    sig_total = sig_macro + sig_defect

    # D6 reference
    sig_macro_d6, sig_total_d6, _ = _compute_d6_reference(
        R_EQ + 1e-6, sigma_defect_Req, params.scalar_A,
        params.M, params.tau, params.R_ext,
    )

    return CoupledSectorProfiles(
        alpha_BR=params.alpha_BR,
        beta_XR=params.beta_XR,
        scalar_A=params.scalar_A,
        lam=lam,
        r_grid=r_int,
        epsilon_defect=eps_defect,
        sigma_defect=sig_defect,
        sigma_defect_at_Req=sigma_defect_Req,
        bvp_converged=converged,
        A_eff=A_eff,
        A_eff_at_Req=A_eff_Req,
        epsilon_macro_coupled=eps_macro,
        sigma_macro_coupled=sig_macro,
        sigma_macro_coupled_at_Req=sig_macro_Req,
        sigma_total=sig_total,
        sigma_macro_d6_at_Req=sig_macro_d6,
        sigma_total_d6_at_Req=sig_total_d6,
        notes=[
            f"alpha_BR={params.alpha_BR}, beta_XR={params.beta_XR}",
            f"A_eff(R_eq) = {A_eff_Req:.4f} (uncoupled: {params.scalar_A:.4f})",
            f"Sigma_macro_coupled(R_eq) = {sig_macro_Req:.6f} "
            f"(D6: {sig_macro_d6:.6f})",
            f"Sigma_defect(R_eq) = {sigma_defect_Req:.6f}",
        ],
    )


# ================================================================
# Level 2: Back-Reaction Assessment
# ================================================================

def assess_back_reaction(
    coupled: CoupledSectorProfiles,
    params: CrossCouplingParams,
) -> BackReactionAssessment:
    """Classify back-reaction as constructive, destructive, or neutral."""
    alpha_BR = params.alpha_BR
    beta_XR = params.beta_XR

    # Gravitational penalty: delta increases by this amount
    delta_increase = alpha_BR * coupled.sigma_defect_at_Req

    # Macro amplification: Sigma_macro increases by this amount
    sigma_macro_increase = coupled.sigma_macro_coupled_at_Req - coupled.sigma_macro_d6_at_Req

    A_eff_Req = coupled.A_eff_at_Req
    amplification = A_eff_Req ** 2 / params.scalar_A ** 2

    # Net metric shift at R_eq
    # f_coupled - f_d6 = -2*(delta_increase - sigma_macro_increase) / R_eq
    # (sigma_defect cancels in the difference since it's the same)
    r_Req = R_EQ + 1e-6
    net_shift = -2.0 * (delta_increase - sigma_macro_increase) / r_Req

    # Classification
    if net_shift > 0.01:
        cls = "constructive"
    elif net_shift < -0.01:
        cls = "destructive"
    else:
        cls = "neutral"

    return BackReactionAssessment(
        alpha_BR=alpha_BR,
        beta_XR=beta_XR,
        delta_increase_at_Req=delta_increase,
        sigma_macro_increase_at_Req=sigma_macro_increase,
        A_eff_at_Req=A_eff_Req,
        amplification_factor=amplification,
        net_metric_shift_at_Req=net_shift,
        net_classification=cls,
        constructive_dominates=bool(sigma_macro_increase > delta_increase),
        notes=[
            f"Gravitational penalty (delta increase): {delta_increase:.6f}",
            f"Macro amplification (Sigma increase): {sigma_macro_increase:.6f}",
            f"A_eff^2/A_0^2 = {amplification:.4f}",
            f"Net metric shift at R_eq: {net_shift:.6f}",
            f"Classification: {cls}",
            f"Constructive dominates: {sigma_macro_increase > delta_increase}",
        ],
    )


# ================================================================
# Level 3: Coupled Metric Injection
# ================================================================

def inject_coupled_metric(
    coupled: CoupledSectorProfiles,
    params: CrossCouplingParams,
) -> CoupledMetricInjectionResult:
    """Inject coupled source into metric.

    delta_coupled(r) = m_static(r) + alpha_BR * Sigma_defect(r) - r/2
    f_coupled(r) = -2*(delta_coupled - Sigma_total) / r
    """
    r = coupled.r_grid
    M = params.M
    tau = params.tau
    R_ext = params.R_ext
    alpha_BR = params.alpha_BR
    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2

    # Static mass and deficit
    m_static = M + mass_coeff * (1.0 / r - 1.0 / R_ext)
    delta_coupled = m_static + alpha_BR * coupled.sigma_defect - r / 2.0

    sig_total = coupled.sigma_total
    f_coupled = -2.0 * (delta_coupled - sig_total) / r

    f_min = float(np.min(f_coupled))
    f_min_idx = int(np.argmin(f_coupled))
    f_min_r = float(r[f_min_idx])
    metric_pos = bool(f_min > 0)

    f_at_Req = float(f_coupled[0])

    # D6 reference at R_eq
    _, _, f_d6 = _compute_d6_reference(
        float(r[0]), coupled.sigma_defect_at_Req, params.scalar_A,
        M, tau, R_ext,
    )

    metric_shift = f_at_Req - f_d6

    # Budget at key radii
    budget: Dict[str, Dict[str, float]] = {}
    for r_key in KEY_RADII:
        if R_EQ <= r_key <= R_ext:
            idx = int(np.argmin(np.abs(r - r_key)))
            budget[f"r={r_key:.4f}"] = {
                "delta_coupled": float(delta_coupled[idx]),
                "sigma_macro_coupled": float(coupled.sigma_macro_coupled[idx]),
                "sigma_defect": float(coupled.sigma_defect[idx]),
                "sigma_total": float(sig_total[idx]),
                "f_coupled": float(f_coupled[idx]),
            }

    return CoupledMetricInjectionResult(
        alpha_BR=alpha_BR,
        beta_XR=params.beta_XR,
        scalar_A=params.scalar_A,
        lam=coupled.lam,
        r_grid=r,
        delta_coupled=delta_coupled,
        sigma_total_coupled=sig_total,
        f_coupled=f_coupled,
        f_min=f_min,
        f_min_radius=f_min_r,
        metric_positive=metric_pos,
        f_at_Req=f_at_Req,
        f_d6_at_Req=f_d6,
        metric_shift=metric_shift,
        budget=budget,
        notes=[
            f"alpha_BR={alpha_BR}, beta_XR={params.beta_XR}",
            f"f_min = {f_min:.6f} at r = {f_min_r:.4f}",
            f"f(R_eq) = {f_at_Req:.6f} (D6: {f_d6:.6f})",
            f"Metric shift at R_eq: {metric_shift:.6f}",
            f"Metric globally positive: {metric_pos}",
        ],
    )


# ================================================================
# Level 4: Coupling Strength Scan
# ================================================================

def scan_coupling_strength(
    params: CrossCouplingParams,
) -> CouplingStrengthScanResult:
    """Scan the 5x5 (alpha_BR, beta_XR) grid at default lambda.

    Optimized: solve BVP once, reuse defect profile for all 25 configs.
    """
    # Solve BVP once
    defect_cache = _solve_defect_on_grid(params)

    entries: List[CouplingStrengthScanEntry] = []

    for alpha in params.alpha_BR_scan:
        for beta in params.beta_XR_scan:
            p = CrossCouplingParams(
                eta=params.eta, lam=params.lam, xi=params.xi,
                r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
                n_interior=params.n_interior, M=params.M, tau=params.tau,
                R_ext=params.R_ext, scalar_A=params.scalar_A,
                alpha_BR=alpha, beta_XR=beta,
            )

            coupled = compute_coupled_sectors(p, defect_cache=defect_cache)
            metric = inject_coupled_metric(coupled, p)
            br = assess_back_reaction(coupled, p)

            entries.append(CouplingStrengthScanEntry(
                alpha_BR=alpha,
                beta_XR=beta,
                f_min=metric.f_min,
                f_at_Req=metric.f_at_Req,
                metric_positive=metric.metric_positive,
                A_eff_at_Req=coupled.A_eff_at_Req,
                net_classification=br.net_classification,
                notes=f"alpha={alpha}, beta={beta}",
            ))

    n_pos = sum(1 for e in entries if e.metric_positive)

    # Named slices
    def _find(a: float, b: float) -> Optional[CouplingStrengthScanEntry]:
        for e in entries:
            if abs(e.alpha_BR - a) < 1e-10 and abs(e.beta_XR - b) < 1e-10:
                return e
        return None

    ub = _find(1.0, 1.0)
    pure_br = _find(1.0, 0.0)
    pure_amp = _find(0.0, 1.0)

    return CouplingStrengthScanResult(
        entries=entries,
        n_scanned=len(entries),
        n_positive=n_pos,
        unit_benchmark_f_min=ub.f_min if ub else float("nan"),
        unit_benchmark_positive=ub.metric_positive if ub else False,
        unit_benchmark_classification=ub.net_classification if ub else "unknown",
        pure_backreaction=pure_br,
        pure_amplification=pure_amp,
        unit_benchmark_entry=ub,
        notes=[
            f"Scanned {len(entries)} coupling configurations.",
            f"{n_pos} configurations give positive metric.",
            f"Unit benchmark (1,1): f_min = {ub.f_min:.6f}, positive = {ub.metric_positive}"
            if ub else "Unit benchmark not found.",
            f"Pure back-reaction (1,0): f_min = {pure_br.f_min:.6f}" if pure_br else "",
            f"Pure amplification (0,1): f_min = {pure_amp.f_min:.6f}" if pure_amp else "",
        ],
    )


# ================================================================
# Level 5: Lambda Scan
# ================================================================

def scan_lambda_coupled(
    params: CrossCouplingParams,
) -> CoupledLambdaScanResult:
    """Lambda scan: D6 baseline (0,0) vs unit benchmark (1,1) for each lambda."""
    entries: List[CoupledLambdaScanEntry] = []

    for lam_val in params.lambda_scan:
        # Solve BVP once per lambda
        defect_cache = _solve_defect_on_grid(params, lam_override=lam_val)
        converged = defect_cache[3]

        # D6 baseline: alpha=0, beta=0
        p_d6 = CrossCouplingParams(
            eta=params.eta, lam=lam_val, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=0.0, beta_XR=0.0,
        )
        coupled_d6 = compute_coupled_sectors(p_d6, lam_override=lam_val,
                                              defect_cache=defect_cache)
        metric_d6 = inject_coupled_metric(coupled_d6, p_d6)

        # Unit benchmark: alpha=1, beta=1
        p_ub = CrossCouplingParams(
            eta=params.eta, lam=lam_val, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=1.0, beta_XR=1.0,
        )
        coupled_ub = compute_coupled_sectors(p_ub, lam_override=lam_val,
                                              defect_cache=defect_cache)
        metric_ub = inject_coupled_metric(coupled_ub, p_ub)

        f_shift = metric_ub.f_min - metric_d6.f_min
        if f_shift > 0.01:
            cls = "constructive"
        elif f_shift < -0.01:
            cls = "destructive"
        else:
            cls = "neutral"

        entries.append(CoupledLambdaScanEntry(
            lam=lam_val,
            bvp_converged=converged,
            f_min_d6=metric_d6.f_min,
            f_min_coupled=metric_ub.f_min,
            metric_positive_d6=metric_d6.metric_positive,
            metric_positive_coupled=metric_ub.metric_positive,
            f_shift=f_shift,
            net_classification=cls,
            notes=f"lam={lam_val}",
        ))

    n_scanned = len(entries)
    n_conv = sum(1 for e in entries if e.bvp_converged)
    n_pos_d6 = sum(1 for e in entries if e.metric_positive_d6)
    n_pos_ub = sum(1 for e in entries if e.metric_positive_coupled)

    viable_d6 = [e.lam for e in entries if e.metric_positive_d6]
    viable_ub = [e.lam for e in entries if e.metric_positive_coupled]

    if n_pos_ub > 0:
        best = max([e for e in entries if e.metric_positive_coupled],
                   key=lambda e: e.f_min_coupled)
        best_lam = best.lam
        best_fmin = best.f_min_coupled
    else:
        best = max(entries, key=lambda e: e.f_min_coupled)
        best_lam = best.lam
        best_fmin = best.f_min_coupled

    # Rescue preserved?
    d6_threshold_lambdas = [e.lam for e in entries if e.metric_positive_d6 and e.lam >= 25]
    ub_threshold_lambdas = [e.lam for e in entries if e.metric_positive_coupled and e.lam >= 25]
    rescue_preserved = len(ub_threshold_lambdas) >= len(d6_threshold_lambdas) and len(d6_threshold_lambdas) > 0

    # Threshold shift
    if viable_ub == viable_d6:
        shift = "unchanged"
    elif len(viable_ub) > len(viable_d6):
        shift = "lower"  # more lambdas viable → threshold moved down
    elif len(viable_ub) < len(viable_d6):
        shift = "higher"  # fewer lambdas viable → threshold moved up
    elif len(viable_ub) == 0:
        shift = "destroyed"
    else:
        shift = "shifted"

    return CoupledLambdaScanResult(
        entries=entries,
        n_scanned=n_scanned,
        n_converged=n_conv,
        n_positive_d6=n_pos_d6,
        n_positive_coupled=n_pos_ub,
        best_lambda_coupled=best_lam,
        best_fmin_coupled=best_fmin,
        rescue_preserved=rescue_preserved,
        viable_lambda_d6=viable_d6,
        viable_lambda_coupled=viable_ub,
        threshold_shift=shift,
        notes=[
            f"Scanned {n_scanned} lambda values, {n_conv} converged.",
            f"D6 positive: {n_pos_d6}, Coupled positive: {n_pos_ub}",
            f"Viable D6: {viable_d6}",
            f"Viable coupled: {viable_ub}",
            f"Threshold shift: {shift}",
            f"Rescue preserved: {rescue_preserved}",
        ],
    )


# ================================================================
# Level 6: Classification
# ================================================================

def classify_cross_coupling(
    coupling_scan: CouplingStrengthScanResult,
    lambda_scan: CoupledLambdaScanResult,
    params: CrossCouplingParams,
) -> CrossCouplingClassification:
    """Classify the D7 cross-coupling result."""
    ub_pos = coupling_scan.unit_benchmark_positive
    ub_cls = coupling_scan.unit_benchmark_classification

    viable_d6 = lambda_scan.viable_lambda_d6
    viable_ub = lambda_scan.viable_lambda_coupled

    if ub_pos and lambda_scan.rescue_preserved and ub_cls == "constructive":
        classification = "fully_coupled_viable"
        summary = (
            f"Unit benchmark (1,1) preserves metric positivity. "
            f"Back-reaction is net constructive. "
            f"D6 additive approximation was pessimistic. "
            f"Viable lambda window: {viable_ub}."
        )
    elif lambda_scan.rescue_preserved and ub_pos:
        if lambda_scan.threshold_shift == "lower":
            classification = "viability_window_shifted_but_survives"
            summary = (
                f"Coupling shifts the viable window downward (more permissive). "
                f"Viable: {viable_ub} (D6: {viable_d6})."
            )
        elif lambda_scan.threshold_shift == "higher":
            classification = "viability_window_shifted_but_survives"
            summary = (
                f"Coupling shifts the viable window upward (more restrictive). "
                f"Viable: {viable_ub} (D6: {viable_d6})."
            )
        else:
            classification = "viability_window_shifted_but_survives"
            summary = (
                f"Viable window shifted. "
                f"Viable: {viable_ub} (D6: {viable_d6})."
            )
    elif len(viable_ub) > 0:
        classification = "partially_viable_under_coupling"
        summary = (
            f"Some lambda values survive coupling but rescue is reduced. "
            f"Viable: {viable_ub} (D6: {viable_d6})."
        )
    elif not ub_pos and len(viable_ub) == 0:
        classification = "destroyed_by_back_reaction"
        summary = (
            "Back-reaction eliminates metric positivity at all scanned lambda. "
            "The D6 rescue does not survive full coupling."
        )
    else:
        classification = "unresolved_coupled_artifacts"
        summary = "Mixed or unresolvable results."

    d6_pessimistic = ub_cls == "constructive"

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
        "companion_D6": "LOCKED (companion_architecture_viable)",
        "cross_coupling_D7": phase_status,
    }

    return CrossCouplingClassification(
        classification=classification,
        phase_status=phase_status,
        d6_additive_pessimistic=d6_pessimistic,
        unit_benchmark_positive=ub_pos,
        viable_lambda_window_coupled=viable_ub,
        viable_lambda_window_d6=viable_d6,
        threshold_shift=lambda_scan.threshold_shift,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 7: Master Computation
# ================================================================

def compute_cross_coupling(
    params: Optional[CrossCouplingParams] = None,
) -> CrossCouplingResult:
    """Run the full Phase D7 cross-coupling analysis."""
    if params is None:
        params = CrossCouplingParams()

    result = CrossCouplingResult(
        valid=True,
        params=params,
        nonclaims=list(CROSS_COUPLING_NONCLAIMS),
        assumptions=list(CROSS_COUPLING_ASSUMPTIONS),
    )

    # Level 0: Model definition
    result.model_definition = define_coupled_model(params)

    # Level 1: Coupled sectors at default params (unit benchmark)
    result.coupled_sectors = compute_coupled_sectors(params)

    # Level 2: Back-reaction assessment
    result.back_reaction = assess_back_reaction(result.coupled_sectors, params)

    # Level 3: Metric injection
    result.metric_injection = inject_coupled_metric(result.coupled_sectors, params)

    # Level 4: Coupling strength scan
    result.coupling_scan = scan_coupling_strength(params)

    # Level 5: Lambda scan
    result.lambda_scan = scan_lambda_coupled(params)

    # Level 6: Classification
    result.classification = classify_cross_coupling(
        result.coupling_scan, result.lambda_scan, params,
    )

    return result


# ================================================================
# Level 8: Serialization
# ================================================================

def cross_coupling_result_to_dict(
    result: CrossCouplingResult,
) -> Dict[str, Any]:
    """Serialize to JSON-compatible dict."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "phase": "D7",
        "title": "Cross-Coupling Dynamics and Back-Reaction Test",
    }

    # Model definition
    if result.model_definition:
        md = result.model_definition
        d["model_definition"] = {
            "n_channels": md.n_channels,
            "channels": [
                {
                    "name": ch.name,
                    "parameter": ch.parameter,
                    "formula": ch.formula,
                    "effect_on_metric": ch.effect_on_metric,
                    "d6_limit": ch.d6_limit,
                }
                for ch in md.channels
            ],
            "combined_formula": md.combined_formula,
            "d6_recovery_condition": md.d6_recovery_condition,
            "unit_benchmark": list(md.unit_benchmark),
            "scope_statement": md.scope_statement,
        }

    # Coupled sectors
    if result.coupled_sectors:
        cs = result.coupled_sectors
        d["coupled_sectors"] = {
            "alpha_BR": cs.alpha_BR,
            "beta_XR": cs.beta_XR,
            "sigma_defect_at_Req": cs.sigma_defect_at_Req,
            "A_eff_at_Req": cs.A_eff_at_Req,
            "sigma_macro_coupled_at_Req": cs.sigma_macro_coupled_at_Req,
            "sigma_macro_d6_at_Req": cs.sigma_macro_d6_at_Req,
            "sigma_total_d6_at_Req": cs.sigma_total_d6_at_Req,
            "bvp_converged": cs.bvp_converged,
            "notes": cs.notes,
        }

    # Back-reaction
    if result.back_reaction:
        br = result.back_reaction
        d["back_reaction"] = {
            "alpha_BR": br.alpha_BR,
            "beta_XR": br.beta_XR,
            "delta_increase_at_Req": br.delta_increase_at_Req,
            "sigma_macro_increase_at_Req": br.sigma_macro_increase_at_Req,
            "A_eff_at_Req": br.A_eff_at_Req,
            "amplification_factor": br.amplification_factor,
            "net_metric_shift_at_Req": br.net_metric_shift_at_Req,
            "net_classification": br.net_classification,
            "constructive_dominates": br.constructive_dominates,
        }

    # Metric injection
    if result.metric_injection:
        mi = result.metric_injection
        d["metric_injection"] = {
            "f_min": mi.f_min,
            "f_min_radius": mi.f_min_radius,
            "metric_positive": mi.metric_positive,
            "f_at_Req": mi.f_at_Req,
            "f_d6_at_Req": mi.f_d6_at_Req,
            "metric_shift": mi.metric_shift,
            "budget": mi.budget,
        }

    # Coupling scan
    if result.coupling_scan:
        cs2 = result.coupling_scan
        d["coupling_scan"] = {
            "n_scanned": cs2.n_scanned,
            "n_positive": cs2.n_positive,
            "unit_benchmark_f_min": cs2.unit_benchmark_f_min,
            "unit_benchmark_positive": cs2.unit_benchmark_positive,
            "unit_benchmark_classification": cs2.unit_benchmark_classification,
            "pure_backreaction_f_min": cs2.pure_backreaction.f_min if cs2.pure_backreaction else None,
            "pure_amplification_f_min": cs2.pure_amplification.f_min if cs2.pure_amplification else None,
            "entries": [
                {
                    "alpha_BR": e.alpha_BR,
                    "beta_XR": e.beta_XR,
                    "f_min": e.f_min,
                    "metric_positive": e.metric_positive,
                    "net_classification": e.net_classification,
                }
                for e in cs2.entries
            ],
        }

    # Lambda scan
    if result.lambda_scan:
        ls = result.lambda_scan
        d["lambda_scan"] = {
            "n_scanned": ls.n_scanned,
            "n_converged": ls.n_converged,
            "n_positive_d6": ls.n_positive_d6,
            "n_positive_coupled": ls.n_positive_coupled,
            "best_lambda_coupled": ls.best_lambda_coupled,
            "best_fmin_coupled": ls.best_fmin_coupled,
            "rescue_preserved": ls.rescue_preserved,
            "viable_lambda_d6": ls.viable_lambda_d6,
            "viable_lambda_coupled": ls.viable_lambda_coupled,
            "threshold_shift": ls.threshold_shift,
            "entries": [
                {
                    "lam": e.lam,
                    "f_min_d6": e.f_min_d6,
                    "f_min_coupled": e.f_min_coupled,
                    "metric_positive_d6": e.metric_positive_d6,
                    "metric_positive_coupled": e.metric_positive_coupled,
                    "f_shift": e.f_shift,
                    "net_classification": e.net_classification,
                }
                for e in ls.entries
            ],
        }

    # Classification
    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "d6_additive_pessimistic": cl.d6_additive_pessimistic,
            "unit_benchmark_positive": cl.unit_benchmark_positive,
            "viable_lambda_window_coupled": cl.viable_lambda_window_coupled,
            "viable_lambda_window_d6": cl.viable_lambda_window_d6,
            "threshold_shift": cl.threshold_shift,
            "summary": cl.summary,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
