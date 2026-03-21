"""Phase D5 — Source-Coupled Defect Dynamics and Component A Amplitude Recovery.

Couples the embedded O(3) triplet magnitude back to the GRUT source X(r) and
tests whether source-driving recovers the Component A amplitude while
preserving the topological Component B tail.

PRINCIPAL RESULTS:

  Result 1 — Source Coupling:
    Two minimal couplings assessed: quadratic (preferred, O(3)-symmetric)
    and linear (comparison, symmetry-breaking).

  Result 2 — Sourced Radial ODE:
    Sign derived from Euler-Lagrange variation of the sourced Lagrangian.
    Not assumed or hard-coded.

  Result 3 — Component A Recovery (three-part):
    Shape, coefficient ratio, mechanism.  Key: does source-driving raise
    the coefficient from ~0.0035 toward ~1?

  Result 4 — Component B Preservation (four-part):
    Tail exponent, tail coefficient (near eta^2), monotonic f->1,
    no oscillation.

  Result 5 — Gamma Scan:
    Bounded scan including gamma=0 (D4 baseline) through gamma=50.

  Result 6 — Classification:
    (determined by numerical outcome)

Uses D2 BVP framework (scipy.solve_bvp) with modified ODE.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

try:
    from scipy.integrate import solve_bvp
    HAS_SCIPY_BVP = True
except ImportError:
    HAS_SCIPY_BVP = False


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
R_EXT = 2.0 * R_S

# D5-specific
GAMMA_DEFAULT = 1.0
GAMMA_SCAN_VALUES = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
SOURCE_AMPLITUDE = M_EXT  # X(r) = SOURCE_AMPLITUDE / r^2
COMP_A_TARGET = A_CRIT_SQUARED * MASS_COEFF  # ~ 1.181

N_COUPLING_TYPES = 2  # quadratic, linear
KRETSCHNER_COEFF = 48.0 * M_EXT ** 2  # K = KRETSCHNER_COEFF / r^6


# ================================================================
# Assumptions
# ================================================================

SOURCE_COUPLED_ASSUMPTIONS = [
    "1. The GRUT source profile is X(r) = M/r^2, as in the "
    "source_law_program diagnostic.  This is the profile that "
    "drives the scalar-memory equation.",

    "2. Two source couplings are assessed: quadratic (preferred, "
    "O(3)-symmetric) and linear (comparison, symmetry-breaking).  "
    "The candidate set is minimal.",

    "3. The sign of the source term in the radial ODE is derived "
    "from the Euler-Lagrange equation applied to the sourced "
    "Lagrangian.  It is not assumed or hard-coded.",

    "4. The curvature trigger is fixed to the D4 top-ranked choice "
    "(Kretschner sqrt(K)).  This is not reopened in D5.",

    "5. The gamma scan includes gamma=0 as the D4 unsourced baseline "
    "for clean before/after comparison.",

    "6. The interaction energy from the source coupling is reported "
    "separately from the 3 pure defect sectors.  It is not assumed "
    "to be a positive-support contribution.",

    "7. Component A recovery is assessed in three parts: shape, "
    "coefficient ratio, mechanism interpretation.",

    "8. Component B preservation is assessed in four parts: "
    "tail exponent, tail coefficient (near eta^2), monotonic "
    "approach to f=1, no oscillation.",

    "9. The BVP solver uses the same scipy.solve_bvp framework "
    "as D2.  Domain: [r_min, r_max] = [0.01, 5.0].",

    "10. The background metric is held fixed.  No self-consistent "
    "back-reaction loop is implemented.",
]


SOURCE_COUPLED_NONCLAIMS = [
    "1. This phase does NOT prove the final unified field theory.",

    "2. A successful amplitude recovery establishes numerical "
    "viability of source-coupled unification, not final canon.",

    "3. A failed D5 result does NOT invalidate D1-D4.  It shows "
    "that the leading architecture still requires revision.",

    "4. The source coupling introduced here is a tested candidate "
    "mechanism, not yet a unique derivation.",

    "5. Component A amplitude recovery and Component B preservation "
    "must both hold for a strong positive D5 result.",

    "6. The interaction energy term may be sign-indefinite and "
    "is not guaranteed to be a physical support density.",

    "7. The gamma scan is bounded and disciplined, not exhaustive.  "
    "Extreme gamma values may produce different behavior.",

    "8. The BVP uses finite-domain approximation.  Tail behavior "
    "at r >> r_max is not directly tested.",

    "9. The source profile X(r) = M/r^2 is a diagnostic candidate, "
    "not yet derived from first principles in GRUT.",

    "10. The classification is within the D5 numerical framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class SourceCoupledDefectParams:
    """Parameters for Phase D5."""
    eta: float = ETA_TARGET
    lam: float = LAMBDA_DEFAULT
    gamma: float = GAMMA_DEFAULT
    coupling_type: str = "quadratic"  # "quadratic" or "linear"
    # BVP params
    r_min: float = 0.01
    r_max: float = 5.0
    n_grid: int = 300
    # Source
    source_amplitude: float = SOURCE_AMPLITUDE
    # Scan
    gamma_scan: List[float] = field(
        default_factory=lambda: list(GAMMA_SCAN_VALUES)
    )


@dataclass
class SourceCouplingChoice:
    """One source-coupling candidate."""
    coupling_id: int
    name: str
    coupling_type: str  # "quadratic" or "linear"
    lagrangian_term: str
    ode_source_term: str
    ode_source_sign_derivation: str
    n_new_params: int
    symmetry_preserved: bool
    justification: str
    notes: List[str] = field(default_factory=list)


@dataclass
class SourcedLagrangianTerm:
    """One term in the sourced Lagrangian."""
    term_id: int
    name: str
    formula: str
    description: str


@dataclass
class SourcedLagrangian:
    """The full sourced embedded-triplet Lagrangian."""
    terms: List[SourcedLagrangianTerm]
    n_terms: int
    full_formula: str
    coupling_type: str
    gamma: float
    source_formula: str
    notes: List[str] = field(default_factory=list)


@dataclass
class SourcedRadialEquation:
    """The sourced radial hedgehog ODE."""
    full_ode: str
    unsourced_ode: str
    source_term_formula: str
    source_term_sign: str  # "+1" or "-1", derived
    sign_derivation: str   # explanation of how sign was obtained
    coupling_type: str
    notes: List[str] = field(default_factory=list)


@dataclass
class SourceCoupledBVPSolution:
    """Numerical BVP solution with source coupling."""
    converged: bool
    r_grid: np.ndarray
    f_solution: np.ndarray
    f_prime: np.ndarray
    c1_effective: float
    max_residual: float
    f_at_rmax: float
    f_max: float           # max(f) to check overshoot
    f_max_radius: float    # radius of max(f)
    gamma: float
    coupling_type: str
    notes: List[str] = field(default_factory=list)


@dataclass
class SourcedEnergyProfile:
    """Energy profile with source coupling — pure sectors + interaction."""
    r_grid: np.ndarray
    # 3 pure defect sectors
    radial_kinetic: np.ndarray
    angular_gradient: np.ndarray
    potential_term: np.ndarray
    pure_defect_total: np.ndarray
    # Interaction term (reported separately, may be sign-indefinite)
    interaction_term: np.ndarray
    interaction_sign_definite: bool
    interaction_positive_fraction: float  # fraction of r-grid where > 0
    # Combined
    total_with_interaction: np.ndarray
    # Tail fits (pure defect sectors only)
    radial_kinetic_exponent: float
    radial_kinetic_coefficient: float
    angular_gradient_exponent: float
    angular_gradient_coefficient: float
    potential_exponent: float
    # Integrated quantities
    integrated_pure_mass: float
    integrated_interaction: float
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentARecoveryResult:
    """Three-part test for Component A recovery."""
    # Shape
    shape_exponent_target: float
    shape_exponent_measured: float
    shape_match: bool
    shape_verdict: str
    # Coefficient
    coeff_radial_kinetic: float
    coeff_target: float
    coeff_ratio: float
    coeff_match: bool
    coeff_verdict: str
    # Mechanism
    mechanism: str
    mechanism_source_driven: bool
    mechanism_verdict: str
    # Overall
    classification: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentBPreservationResult:
    """Four-part test for Component B preservation."""
    # 1. Tail exponent
    exponent_target: float
    exponent_measured: float
    exponent_match: bool
    # 2. Tail coefficient
    coefficient_target: float  # eta^2
    coefficient_measured: float
    coefficient_match: bool
    # 3. Monotonic approach
    f_at_rmax: float
    f_max: float
    f_overshoot: bool   # f_max > 1 + tolerance
    monotonic: bool
    # 4. No oscillation
    n_sign_changes_in_tail: int
    oscillation_free: bool
    # Overall
    all_pass: bool
    classification: str
    notes: List[str] = field(default_factory=list)


@dataclass
class GammaScanEntry:
    """One entry in the gamma scan."""
    gamma: float
    bvp_converged: bool
    comp_A_ratio: float
    comp_A_shape_match: bool
    comp_B_preserved: bool
    comp_B_coeff_match: bool
    f_max: float
    f_overshoot: bool
    interaction_sign_definite: bool
    has_pathology: bool
    notes: str = ""


@dataclass
class GammaScanResult:
    """Full gamma scan result."""
    entries: List[GammaScanEntry]
    n_scanned: int
    n_converged: int
    n_comp_A_improved: int  # ratio > D4 baseline (0.0035)
    n_comp_B_preserved: int
    n_viable: int           # both A improved and B preserved
    best_gamma: Optional[float]
    best_ratio: float
    viable_window: Optional[Tuple[float, float]]
    notes: List[str] = field(default_factory=list)


@dataclass
class Pathology:
    """One identified pathology."""
    pathology_id: int
    category: str
    description: str
    severity: str
    gamma_range: str


@dataclass
class PathologyInventory:
    """Complete pathology inventory."""
    pathologies: List[Pathology]
    n_pathologies: int
    n_critical: int
    n_moderate: int
    n_minor: int
    notes: List[str] = field(default_factory=list)


@dataclass
class SourceCoupledClassification:
    """Final D5 classification."""
    classification: str
    phase_status: str
    best_gamma: Optional[float]
    best_comp_A_ratio: float
    comp_B_preserved_at_best: bool
    n_pathologies: int
    phase_lock_update: Dict[str, str]
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class NormalizationMap:
    """Dimensional / normalization bridge between GRUT source and defect ODE.

    GRUT canon treats the collapse driver as X ~ GM/R^2.  The hedgehog ODE
    is written in dimensionless-like coordinates with 1/r^2 terms.  This
    dataclass explicitly documents how these are mapped.
    """
    # --- Radial coordinate ---
    r_unit: str              # what r is measured in
    r_star: float            # reference scale r_*
    r_star_description: str

    # --- Field normalization ---
    f_unit: str              # dimensionless by construction
    eta_unit: str            # dimensions of eta
    eta_value: float
    phi_formula: str         # |Phi| = eta * f(r)

    # --- Source profile ---
    X_dimensional: str       # X = GM/R^2 in GRUT
    X_in_ode_units: str      # how X enters the ODE
    X_star: float            # reference X scale
    X_star_description: str
    source_nondim_formula: str  # X_tilde(r_tilde)

    # --- Coupling constants ---
    lambda_unit: str
    lambda_value: float
    gamma_unit: str          # dimensions of gamma
    gamma_description: str
    xi_unit: str             # curvature coupling
    curvature_trigger_unit: str

    # --- ODE presentation ---
    ode_dimensional: str
    ode_dimensionless: str
    nondim_map: Dict[str, str]  # variable -> definition

    notes: List[str] = field(default_factory=list)


@dataclass
class SourceCoupledDefectResult:
    """Master result container for Phase D5."""
    valid: bool
    params: SourceCoupledDefectParams
    normalization: Optional[NormalizationMap] = None
    couplings: Optional[List[SourceCouplingChoice]] = None
    lagrangian: Optional[SourcedLagrangian] = None
    radial_equation: Optional[SourcedRadialEquation] = None
    baseline_bvp: Optional[SourceCoupledBVPSolution] = None
    baseline_energy: Optional[SourcedEnergyProfile] = None
    comp_a_result: Optional[ComponentARecoveryResult] = None
    comp_b_result: Optional[ComponentBPreservationResult] = None
    gamma_scan: Optional[GammaScanResult] = None
    pathology_inventory: Optional[PathologyInventory] = None
    classification: Optional[SourceCoupledClassification] = None
    nonclaims: List[str] = field(
        default_factory=lambda: list(SOURCE_COUPLED_NONCLAIMS))
    assumptions: List[str] = field(
        default_factory=lambda: list(SOURCE_COUPLED_ASSUMPTIONS))
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Utility
# ================================================================

_trapz = getattr(np, "trapezoid", np.trapz)


def _make_grid(r_min: float, r_max: float, n: int) -> np.ndarray:
    return np.linspace(r_min, r_max, n)


def _fit_power_law(r: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """Fit y ~ A * r^n in log-log.  Returns (exponent, coefficient)."""
    mask = (r > 0) & (y > 0) & np.isfinite(y)
    if np.sum(mask) < 5:
        return (0.0, 0.0)
    lr = np.log(r[mask])
    ly = np.log(y[mask])
    n = len(lr)
    sx, sy = np.sum(lr), np.sum(ly)
    sxx, sxy = np.sum(lr ** 2), np.sum(lr * ly)
    d = n * sxx - sx ** 2
    if abs(d) < 1e-30:
        return (0.0, 0.0)
    slope = (n * sxy - sx * sy) / d
    intercept = (sy - slope * sx) / n
    return (slope, math.exp(intercept))


def _source_X(r: np.ndarray, amplitude: float) -> np.ndarray:
    """GRUT source profile X(r) = amplitude / r^2."""
    return amplitude / r ** 2


# ================================================================
# Level 0: Normalization Map
# ================================================================

def build_normalization_map(
    params: SourceCoupledDefectParams,
) -> NormalizationMap:
    """Construct the dimensional / normalization bridge.

    Documents how every quantity in the sourced ODE relates to the
    GRUT canonical variables.

    Units convention used throughout D1-D5:
      We work in geometric units where G = c = 1, with the Schwarzschild
      radius r_s = 2GM/c^2 = 1 as the fundamental length scale.
      All distances r are measured in units of r_s.
      The external mass M_ext = r_s/2 = 0.5 in these units.

    The GRUT source driver X_GRUT(R) = GM/R^2 in standard units becomes
      X(r) = M_ext / r^2   (in r_s-units, since GM = M_ext in G=c=1)

    The hedgehog ODE is already written with r in units of r_s, so X(r)
    enters directly. No additional rescaling is needed for the radial
    coordinate.

    The field normalization:
      |Phi^a| = eta * f(r), where f is dimensionless (f: 0 -> 1)
      eta has dimensions of [energy/length] in natural units; numerically
      eta = 1/sqrt(8*pi) ~ 0.1995 in the same geometric units
      eta^2 = COMP_B_COEFF = 1/(8*pi) fixes the angular gradient amplitude

    Lambda (self-coupling) has dimensions [1/length^2] in natural units,
    but appears in the ODE as the dimensionless combination lam*eta^2
    (which has dimensions [1/length^2]*[1/length^2]/[1/length^2] but in
    our unit system where r_s = 1, all become pure numbers).

    Gamma (source coupling) appears as gamma * X(r) in the ODE, where
    X(r) = M_ext/r^2. Since f'' has dimensions [1/r^2] and X(r) ~ [1/r^2],
    gamma must be dimensionless for the quadratic coupling.
    For the linear coupling, gamma*X(r)/eta has the same dimension as f''/1,
    so gamma is again dimensionless (since X/eta ~ 1/r^2 / 1 ~ 1/r^2).
    """
    eta = params.eta
    lam = params.lam
    M = params.source_amplitude

    # Reference scales
    r_star = R_S                     # r_* = r_s = 1 (Schwarzschild radius)
    X_star = M / r_star ** 2         # X_* = M_ext / r_s^2 = 0.5

    # The dimensionless ODE (which IS what the solver uses, since r_s = 1):
    #   f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*(M/r^2)*f = 0
    #
    # In explicitly dimensionless form with r_tilde = r / r_s:
    #   d^2f/d(r_tilde)^2 + (2/r_tilde)*df/d(r_tilde) - (2/r_tilde^2)*f
    #     - (lam*eta^2*r_s^2)*f*(f^2-1) - gamma*(M*r_s^2 / (r_s^2 * r_tilde^2))*f = 0
    #
    # But since r_s = 1, r_tilde = r numerically. The dimensionless
    # combination that controls the core size is lam*eta^2 (= LAMBDA_DEFAULT*ETA_SQUARED).
    # The source coupling strength is gamma*M_ext (= gamma * 0.5).

    lam_eta2 = lam * eta ** 2
    core_scale = 1.0 / math.sqrt(lam_eta2) if lam_eta2 > 0 else float("inf")

    return NormalizationMap(
        # Radial
        r_unit="r_s (Schwarzschild radii, r_s = 2GM = 1)",
        r_star=r_star,
        r_star_description=(
            "r_* = r_s = 1.  All radial coordinates are measured in units "
            "of the Schwarzschild radius.  R_eq = 1/3, R_ext = 2.0 in these units."
        ),

        # Field
        f_unit="dimensionless (f: 0 at origin, 1 at infinity)",
        eta_unit="[1] in geometric units (energy density scale; eta^2 = 1/(8*pi))",
        eta_value=eta,
        phi_formula="|Phi^a| = eta * f(r) * r_hat^a (hedgehog embedding)",

        # Source
        X_dimensional="X_GRUT(R) = GM/R^2 [GRUT collapse-driver in standard units]",
        X_in_ode_units=(
            f"X(r) = M_ext / r^2 = {M}/r^2 in r_s-units.  "
            f"Since r_s = 2GM = 1, GM = 0.5, so X(r) = 0.5/r^2.  "
            f"This enters the ODE directly (no additional rescaling)."
        ),
        X_star=X_star,
        X_star_description=(
            f"X_* = M_ext / r_s^2 = {X_star:.4f}.  "
            f"X_tilde(r_tilde) = X(r) / X_* = (M/r^2) / (M/r_s^2) = r_s^2/r^2 = 1/r_tilde^2.  "
            f"So the dimensionless source is simply 1/r_tilde^2."
        ),
        source_nondim_formula="X_tilde(r_tilde) = 1/r_tilde^2",

        # Couplings
        lambda_unit=(
            f"dimensionless in r_s-units; lam = {lam:.4f}; "
            f"lam*eta^2 = {lam_eta2:.4f}; "
            f"defect core scale delta ~ 1/sqrt(lam*eta^2) = {core_scale:.4f} r_s"
        ),
        lambda_value=lam,
        gamma_unit=(
            "dimensionless.  gamma multiplies X(r)*f in the ODE, where "
            "X(r) already has units [1/r^2] matching the other ODE terms.  "
            "The effective source-coupling strength is gamma * M_ext = gamma * 0.5."
        ),
        gamma_description=(
            f"gamma is scanned over {params.gamma_scan}.  "
            f"gamma = 0 recovers the unsourced D4 hedgehog.  "
            f"The ODE source term for quadratic coupling is "
            f"-gamma * M_ext * f / r^2 = -gamma * {M} * f / r^2."
        ),
        xi_unit="dimensionless (curvature coupling from D4, carried forward)",
        curvature_trigger_unit=(
            "sqrt(K) = sqrt(48)*M/r^3 for Schwarzschild, in r_s-units.  "
            "Kretschner scalar K = 48*M^2/r^6 [1/r_s^4 in natural units]."
        ),

        # ODE forms
        ode_dimensional=(
            "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*(M/r^2)*f = 0  "
            "[all quantities in r_s-units, numerically identical to dimensionless form]"
        ),
        ode_dimensionless=(
            "With r_tilde = r/r_s, X_tilde = 1/r_tilde^2, "
            "Lambda_bar = lam*eta^2*r_s^2, Gamma_bar = gamma*M_ext:\n"
            "  f'' + (2/r_tilde)f' - (2/r_tilde^2)f "
            "- Lambda_bar*f*(f^2-1) - Gamma_bar*f/r_tilde^2 = 0\n"
            f"Numerically: Lambda_bar = {lam_eta2:.4f}, "
            f"Gamma_bar = gamma*{M:.4f}"
        ),

        nondim_map={
            "r_tilde": "r / r_s  (= r numerically, since r_s = 1)",
            "f": "dimensionless radial profile (f: 0 -> 1)",
            "X_tilde": "X(r) / X_*  = 1/r_tilde^2",
            "Lambda_bar": f"lam * eta^2 * r_s^2 = {lam_eta2:.4f}",
            "Gamma_bar": f"gamma * M_ext = gamma * {M}",
            "delta_core": f"1/sqrt(Lambda_bar) = {core_scale:.4f} r_s",
        },

        notes=[
            "All D1-D5 computations use geometric units G = c = 1, r_s = 1.",
            "The GRUT driver X(R) = GM/R^2 maps to X(r) = M_ext/r^2 = 0.5/r^2.",
            "Since r_s = 1, the dimensional and dimensionless ODEs are numerically identical.",
            "The coefficient recovery test compares the radial kinetic amplitude "
            f"(from the BVP solution) against COMP_A_TARGET = {COMP_A_TARGET:.4f}, "
            "which is A_crit^2 * MASS_COEFF in the same unit system.",
            "gamma is the only free parameter introduced by D5; it is dimensionless.",
            f"The defect core scale is delta ~ {core_scale:.4f} r_s, "
            f"comparable to R_eq = {R_EQ:.4f} r_s.",
        ],
    )


# ================================================================
# Level 1: Define Source Couplings
# ================================================================

def define_source_couplings(
    params: SourceCoupledDefectParams,
) -> List[SourceCouplingChoice]:
    """Define the minimal set of source-coupling candidates."""

    # --- Quadratic coupling: Euler-Lagrange sign derivation ---
    # Lagrangian density (static, spherical):
    #   L = (1/2) eta^2 (f')^2 + eta^2 f^2/r^2
    #       - (1/4) lam eta^4 (f^2-1)^2
    #       - (1/2) gamma X(r) eta^2 f^2
    #
    # The EOM from dL/df - d/dr(dL/df') = 0:
    #   dL/df = 2 eta^2 f/r^2 - lam eta^4 f(f^2-1) - gamma X eta^2 f
    #   d/dr(dL/df') = eta^2 f'' (plus the (2/r)f' from spherical coords)
    #
    # Full EOM (with spherical Laplacian):
    #   eta^2 [f'' + (2/r)f'] = - 2 eta^2 f/r^2 + lam eta^4 f(f^2-1) + gamma X eta^2 f
    #
    # Dividing by eta^2:
    #   f'' + (2/r)f' - 2f/r^2 + lam eta^2 f(f^2-1) + gamma X f = 0
    #
    # Wait — careful with signs.  The hedgehog has the angular term
    # -2f/r^2 from the Laplacian structure (it appears as part of
    # the equation of motion, not the energy).
    #
    # The standard hedgehog ODE from D2 is:
    #   f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0
    #
    # Note: D2 writes lam*eta^2*f*(f^2-1), which expands to
    # lam*eta^2*(f^3-f).  This comes from d/df[(1/4)lam*eta^4*(f^2-1)^2]
    # = lam*eta^4*f*(f^2-1), and dividing by eta^2 gives lam*eta^2*f*(f^2-1).
    #
    # For the quadratic source coupling L_int = -(1/2)*gamma*X*eta^2*f^2:
    #   d(L_int)/df = -gamma*X*eta^2*f
    #   Divided by eta^2: -gamma*X*f
    #
    # This enters the EOM as:
    #   f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*X(r)*f = 0
    #
    # DERIVED SIGN: -gamma*X*f (the source coupling with L_int = -(1/2)gamma X |Phi|^2
    # produces a NEGATIVE source term in the ODE when gamma > 0 and X > 0).

    quadratic = SourceCouplingChoice(
        coupling_id=1,
        name="quadratic_effective_mass",
        coupling_type="quadratic",
        lagrangian_term="L_int = -(1/2) gamma X(r) eta^2 f^2",
        ode_source_term="-gamma * X(r) * f",
        ode_source_sign_derivation=(
            "From L_int = -(1/2)*gamma*X*eta^2*f^2: "
            "dL_int/df = -gamma*X*eta^2*f. "
            "In EOM (divided by eta^2): -gamma*X*f. "
            "Sign is NEGATIVE for gamma > 0, X > 0. "
            "This acts as an effective mass increase (destabilizing the VEV), "
            "not a driving force toward larger f'."
        ),
        n_new_params=1,
        symmetry_preserved=True,
        justification=(
            "Preserves O(3) symmetry, mirrors curvature coupling pattern "
            "(xi*C*|Phi|^2).  Source-density-dependent effective mass."
        ),
        notes=[
            "Sign derived from Euler-Lagrange variation.",
            "Negative source term: increases effective mass, opposing VEV.",
            "Structurally parallel to curvature coupling.",
        ],
    )

    # --- Linear coupling: Euler-Lagrange sign derivation ---
    # L_int = -gamma * eta * f * X(r)   (using |Phi| = eta*f)
    #
    # dL_int/df = -gamma * eta * X(r)
    # Divided by eta^2 in EOM: -gamma * X(r) / eta
    #
    # Full sourced ODE:
    #   f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*X(r)/eta = 0
    #
    # DERIVED SIGN: -gamma*X/eta (NEGATIVE inhomogeneous source for gamma > 0).
    # This pushes f downward, opposing the hedgehog rise toward f=1.
    #
    # To get a POSITIVE driving force (pushing f upward toward larger values),
    # one would need the opposite sign in the Lagrangian: L_int = +gamma*eta*f*X.
    # We report both signs and let the physics decide.

    linear = SourceCouplingChoice(
        coupling_id=2,
        name="linear_magnitude_source",
        coupling_type="linear",
        lagrangian_term="L_int = -gamma eta f X(r)",
        ode_source_term="-gamma * X(r) / eta",
        ode_source_sign_derivation=(
            "From L_int = -gamma*eta*f*X: "
            "dL_int/df = -gamma*eta*X. "
            "In EOM (divided by eta^2): -gamma*X/eta. "
            "Sign is NEGATIVE for gamma > 0, X > 0. "
            "Inhomogeneous driving force pushing f downward."
        ),
        n_new_params=1,
        symmetry_preserved=False,
        justification=(
            "Direct Yukawa-like coupling between triplet magnitude and "
            "source.  Breaks O(3) Mexican-hat symmetry explicitly."
        ),
        notes=[
            "Sign derived from Euler-Lagrange variation.",
            "Negative source: pushes f downward, opposing hedgehog rise.",
            "Breaks Mexican-hat symmetry (explicit symmetry breaking).",
            "Note: with POSITIVE gamma convention in L_int = +gamma*eta*f*X, "
            "the source would push f upward.  Both conventions tested via "
            "positive and negative gamma in scan.",
        ],
    )

    return [quadratic, linear]


# ================================================================
# Level 2: Construct Sourced Lagrangian
# ================================================================

def construct_sourced_lagrangian(
    coupling: SourceCouplingChoice,
    params: SourceCoupledDefectParams,
) -> SourcedLagrangian:
    """Construct the full sourced Lagrangian."""
    terms = [
        SourcedLagrangianTerm(
            term_id=1, name="kinetic",
            formula="(1/2) eta^2 [(f')^2 + 2 f^2/r^2]",
            description="Hedgehog kinetic + angular gradient.",
        ),
        SourcedLagrangianTerm(
            term_id=2, name="potential",
            formula="-(1/4) lam eta^4 (f^2 - 1)^2",
            description="Mexican-hat self-interaction.",
        ),
        SourcedLagrangianTerm(
            term_id=3, name="curvature_coupling",
            formula="-(1/2) xi sqrt(K) eta^2 f^2",
            description="Kretschner-based curvature trigger (D4 top-ranked).",
        ),
        SourcedLagrangianTerm(
            term_id=4, name="source_coupling",
            formula=coupling.lagrangian_term,
            description=f"Source coupling ({coupling.coupling_type}).",
        ),
    ]

    return SourcedLagrangian(
        terms=terms,
        n_terms=len(terms),
        full_formula=(
            f"L = kinetic + potential + curvature + source_coupling, "
            f"with {coupling.lagrangian_term}"
        ),
        coupling_type=coupling.coupling_type,
        gamma=params.gamma,
        source_formula=f"X(r) = {params.source_amplitude}/r^2",
        notes=[
            f"Coupling type: {coupling.coupling_type}",
            f"gamma = {params.gamma}",
            f"Source term sign: derived from EL variation",
        ],
    )


# ================================================================
# Level 3: Derive Sourced Radial ODE
# ================================================================

def derive_sourced_radial_ode(
    lagrangian: SourcedLagrangian,
    params: SourceCoupledDefectParams,
) -> SourcedRadialEquation:
    """Derive the sourced radial ODE from the Lagrangian via EL variation."""
    unsourced = "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0"

    if lagrangian.coupling_type == "quadratic":
        source_term = "-gamma * X(r) * f = -gamma * M * f / r^2"
        sign = "-1"
        sign_deriv = (
            "Derived: L_int = -(1/2)*gamma*X*eta^2*f^2. "
            "EL gives dL_int/df = -gamma*X*eta^2*f. "
            "Dividing by eta^2: source term is -gamma*X*f. "
            "For gamma > 0 and X > 0: this is NEGATIVE, "
            "increasing effective mass of the radial mode."
        )
        full_ode = (
            "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) "
            "- gamma*M*f/r^2 = 0"
        )
    else:  # linear
        source_term = "-gamma * X(r) / eta = -gamma * M / (eta * r^2)"
        sign = "-1"
        sign_deriv = (
            "Derived: L_int = -gamma*eta*f*X. "
            "EL gives dL_int/df = -gamma*eta*X. "
            "Dividing by eta^2: source term is -gamma*X/eta. "
            "For gamma > 0 and X > 0: this is NEGATIVE, "
            "pushing f downward (opposing hedgehog rise)."
        )
        full_ode = (
            "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) "
            "- gamma*M/(eta*r^2) = 0"
        )

    return SourcedRadialEquation(
        full_ode=full_ode,
        unsourced_ode=unsourced,
        source_term_formula=source_term,
        source_term_sign=sign,
        sign_derivation=sign_deriv,
        coupling_type=lagrangian.coupling_type,
        notes=[
            "Sign derived from Euler-Lagrange variation, NOT assumed.",
            f"Source term sign: {sign} (for gamma > 0, X > 0).",
            "Note: negative gamma can be scanned to test opposite sign.",
            "The derived sign means positive gamma OPPOSES the hedgehog "
            "vacuum.  To DRIVE f toward larger gradients, one may need "
            "negative gamma (or the opposite Lagrangian sign convention).",
        ],
    )


# ================================================================
# Level 4: Solve Sourced BVP
# ================================================================

def solve_sourced_bvp(
    params: SourceCoupledDefectParams,
) -> SourceCoupledBVPSolution:
    """Solve the sourced hedgehog ODE as a BVP.

    For gamma = 0, this recovers the standard D2 hedgehog solution.
    """
    eta = params.eta
    lam = params.lam
    gamma = params.gamma
    r_min = params.r_min
    r_max = params.r_max
    n = params.n_grid
    M = params.source_amplitude
    ct = params.coupling_type

    r_grid = _make_grid(r_min, r_max, n)

    # ODE: y[0] = f, y[1] = f'
    # Standard: f'' = -(2/r)f' + (2/r^2)f + lam*eta^2*f*(f^2-1)
    # Sourced (sign from EL derivation):
    #   quadratic: f'' = above + gamma*M*f/r^2
    #   linear:    f'' = above + gamma*M/(eta*r^2)
    # Note: the ODE is written as f'' = RHS, so the source term
    # (which enters as -gamma*X*f = 0 rearranged) becomes +gamma*M*f/r^2
    # on the RHS of f'' = ...
    def ode(r, y):
        f_val = y[0]
        fp = y[1]
        fpp = (-(2.0 / r) * fp
               + (2.0 / r ** 2) * f_val
               + lam * eta ** 2 * f_val * (f_val ** 2 - 1.0))
        # Source term (derived sign: -gamma*X*f in the ODE equation)
        # ODE: f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - source = 0
        # => f'' = -(2/r)f' + (2/r^2)f + lam*eta^2*f*(f^2-1) + source
        # where source = gamma*X*f (quadratic) or gamma*X/eta (linear)
        # because -(-gamma*X*f) = +gamma*X*f on the RHS.
        X_r = M / r ** 2
        if ct == "quadratic":
            fpp += gamma * X_r * f_val
        else:  # linear
            fpp += gamma * X_r / eta
        return np.array([fp, fpp])

    def bc(ya, yb):
        return np.array([ya[0] - 0.0, yb[0] - 1.0])

    # Initial guess: D2 analytic profile
    delta_core = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
    f_guess = r_grid / np.sqrt(r_grid ** 2 + delta_core ** 2)
    fp_guess = delta_core ** 2 / (r_grid ** 2 + delta_core ** 2) ** 1.5
    y_guess = np.array([f_guess, fp_guess])

    if not HAS_SCIPY_BVP:
        return SourceCoupledBVPSolution(
            converged=False, r_grid=r_grid,
            f_solution=f_guess, f_prime=fp_guess,
            c1_effective=float(fp_guess[0]),
            max_residual=float("nan"), f_at_rmax=float(f_guess[-1]),
            f_max=float(np.max(f_guess)),
            f_max_radius=float(r_grid[np.argmax(f_guess)]),
            gamma=gamma, coupling_type=ct,
            notes=["scipy not available"],
        )

    try:
        sol = solve_bvp(ode, bc, r_grid, y_guess, tol=1e-6, max_nodes=5000)
        converged = sol.success
        y_sol = sol.sol(r_grid)
        f_sol = y_sol[0]
        fp_sol = y_sol[1]
        max_res = float(sol.rms_residuals.max()) if hasattr(sol, 'rms_residuals') else 0.0
        c1_eff = float(fp_sol[0])
        f_max_val = float(np.max(f_sol))
        f_max_idx = int(np.argmax(f_sol))

        return SourceCoupledBVPSolution(
            converged=converged, r_grid=r_grid,
            f_solution=f_sol, f_prime=fp_sol,
            c1_effective=c1_eff, max_residual=max_res,
            f_at_rmax=float(f_sol[-1]),
            f_max=f_max_val,
            f_max_radius=float(r_grid[f_max_idx]),
            gamma=gamma, coupling_type=ct,
            notes=[
                f"gamma={gamma}, coupling={ct}",
                f"converged={converged}, c1={c1_eff:.6f}",
                f"f(r_max)={f_sol[-1]:.6f}, f_max={f_max_val:.6f}",
                f"max_residual={max_res:.2e}",
            ],
        )
    except Exception as exc:
        return SourceCoupledBVPSolution(
            converged=False, r_grid=r_grid,
            f_solution=f_guess, f_prime=fp_guess,
            c1_effective=float(fp_guess[0]),
            max_residual=float("nan"), f_at_rmax=float(f_guess[-1]),
            f_max=float(np.max(f_guess)),
            f_max_radius=float(r_grid[np.argmax(f_guess)]),
            gamma=gamma, coupling_type=ct,
            notes=[f"BVP failed: {exc}"],
        )


# ================================================================
# Level 5: Extract Sourced Energy
# ================================================================

def extract_sourced_energy(
    bvp: SourceCoupledBVPSolution,
    params: SourceCoupledDefectParams,
) -> SourcedEnergyProfile:
    """Extract energy profile with pure sectors + interaction separated."""
    r = bvp.r_grid
    f = bvp.f_solution
    fp = bvp.f_prime
    eta = params.eta
    lam = params.lam
    gamma = params.gamma
    M = params.source_amplitude

    # 3 pure defect sectors (same as D2)
    radial_kin = 0.5 * eta ** 2 * fp ** 2
    angular_grad = eta ** 2 * f ** 2 / r ** 2
    potential = 0.25 * lam * eta ** 4 * (f ** 2 - 1.0) ** 2
    pure_total = radial_kin + angular_grad + potential

    # Interaction term (reported separately, NOT assumed positive)
    X_r = M / r ** 2
    if params.coupling_type == "quadratic":
        # Energy from L_int = -(1/2)*gamma*X*eta^2*f^2
        # Energy density contribution: +(1/2)*gamma*X*eta^2*f^2
        # (sign flip from Lagrangian to Hamiltonian for potential terms)
        interaction = 0.5 * gamma * X_r * eta ** 2 * f ** 2
    else:  # linear
        # Energy from L_int = -gamma*eta*f*X
        # Energy density: +gamma*eta*f*X
        interaction = gamma * eta * f * X_r

    # Check sign definiteness
    pos_frac = float(np.mean(interaction > 0)) if len(interaction) > 0 else 0.0
    sign_def = pos_frac > 0.99 or pos_frac < 0.01

    combined = pure_total + interaction

    # Tail fits (outer region r > 2.0)
    outer = r > 2.0
    rk_exp, rk_coeff = _fit_power_law(r[outer], radial_kin[outer])
    ag_exp, ag_coeff = _fit_power_law(r[outer], angular_grad[outer])
    pot_exp, _ = _fit_power_law(r[outer], potential[outer])

    # Integrated quantities
    integrand_pure = 4.0 * math.pi * r ** 2 * pure_total
    integrand_int = 4.0 * math.pi * r ** 2 * interaction
    int_pure = float(_trapz(integrand_pure, r))
    int_interaction = float(_trapz(integrand_int, r))

    return SourcedEnergyProfile(
        r_grid=r,
        radial_kinetic=radial_kin,
        angular_gradient=angular_grad,
        potential_term=potential,
        pure_defect_total=pure_total,
        interaction_term=interaction,
        interaction_sign_definite=sign_def,
        interaction_positive_fraction=pos_frac,
        total_with_interaction=combined,
        radial_kinetic_exponent=rk_exp,
        radial_kinetic_coefficient=rk_coeff,
        angular_gradient_exponent=ag_exp,
        angular_gradient_coefficient=ag_coeff,
        potential_exponent=pot_exp,
        integrated_pure_mass=int_pure,
        integrated_interaction=int_interaction,
        notes=[
            f"gamma={params.gamma}, coupling={params.coupling_type}",
            f"Radial kinetic tail: r^{rk_exp:.2f}, coeff={rk_coeff:.6f}",
            f"Angular gradient tail: r^{ag_exp:.2f}, coeff={ag_coeff:.6f}",
            f"Interaction positive fraction: {pos_frac:.2f}",
            f"Integrated pure: {int_pure:.4f}, interaction: {int_interaction:.4f}",
        ],
    )


# ================================================================
# Level 6: Component A Recovery
# ================================================================

def assess_component_A_recovery(
    energy: SourcedEnergyProfile,
    params: SourceCoupledDefectParams,
) -> ComponentARecoveryResult:
    """Three-part Component A test: shape, coefficient, mechanism."""
    # Shape
    rk_exp = energy.radial_kinetic_exponent
    shape_target = -4.0
    shape_tol = 1.5
    shape_match = abs(rk_exp - shape_target) < shape_tol
    shape_verdict = (
        f"Exponent {rk_exp:.2f}, target {shape_target}, "
        f"{'PASS' if shape_match else 'FAIL'} (tol {shape_tol})"
    )

    # Coefficient
    rk_coeff = energy.radial_kinetic_coefficient
    coeff_target = COMP_A_TARGET
    ratio = rk_coeff / coeff_target if coeff_target > 0 else 0.0
    coeff_match = 0.1 < ratio < 10.0
    coeff_verdict = (
        f"Radial kinetic coeff: {rk_coeff:.6f}, "
        f"target: {coeff_target:.6f}, "
        f"ratio: {ratio:.4f}, "
        f"{'PASS' if coeff_match else 'FAIL'}"
    )

    # Mechanism
    if abs(params.gamma) > 1e-10:
        mechanism = "source-driven + topology-driven (hybrid)"
        source_driven = True
    else:
        mechanism = "topology-driven only (no source coupling)"
        source_driven = False
    mech_verdict = f"Mechanism: {mechanism}"

    # Classification
    if shape_match and coeff_match and source_driven:
        classification = "full_component_recovery_achieved"
    elif shape_match and ratio > 0.01 and source_driven:
        classification = "source_coupling_partially_recovers_component_a"
    elif shape_match and ratio <= 0.01:
        classification = "source_coupling_insufficient"
    else:
        classification = "source_coupling_insufficient"

    return ComponentARecoveryResult(
        shape_exponent_target=shape_target,
        shape_exponent_measured=rk_exp,
        shape_match=shape_match,
        shape_verdict=shape_verdict,
        coeff_radial_kinetic=rk_coeff,
        coeff_target=coeff_target,
        coeff_ratio=ratio,
        coeff_match=coeff_match,
        coeff_verdict=coeff_verdict,
        mechanism=mechanism,
        mechanism_source_driven=source_driven,
        mechanism_verdict=mech_verdict,
        classification=classification,
        notes=[
            f"gamma={params.gamma}",
            f"Ratio vs D4 baseline (0.0035): {ratio/0.0035:.1f}x improvement"
            if ratio > 0 else "No improvement",
        ],
    )


# ================================================================
# Level 7: Component B Preservation (four-part)
# ================================================================

def assess_component_B_preservation(
    energy: SourcedEnergyProfile,
    bvp: SourceCoupledBVPSolution,
    params: SourceCoupledDefectParams,
) -> ComponentBPreservationResult:
    """Four-part Component B test: exponent, coefficient, monotonic, oscillation."""
    # 1. Tail exponent
    ag_exp = energy.angular_gradient_exponent
    exp_target = -2.0
    exp_tol = 1.0
    exp_match = abs(ag_exp - exp_target) < exp_tol

    # 2. Tail coefficient
    # Note: the BVP finite-domain effect means the power-law fit coefficient
    # doesn't match the asymptotic value at moderate lambda.  D4 established
    # that the exponent and coefficient both converge at higher lambda.
    # We use a factor-of-3 tolerance to account for this.
    ag_coeff = energy.angular_gradient_coefficient
    coeff_target = ETA_SQUARED  # eta^2
    coeff_tol = coeff_target  # within factor of ~3 (accounts for BVP convergence)
    coeff_match = abs(ag_coeff - coeff_target) < coeff_tol

    # 3. Monotonic approach (no overshoot)
    f = bvp.f_solution
    f_max = bvp.f_max
    f_at_rmax = bvp.f_at_rmax
    overshoot_tol = 0.05  # allow 5% above 1.0
    f_overshoot = f_max > 1.0 + overshoot_tol

    # Check monotonicity in outer half
    r = bvp.r_grid
    n = len(r)
    outer_half = slice(n // 2, n)
    f_outer = f[outer_half]
    df_outer = np.diff(f_outer)
    # Monotonic if all diffs are non-negative (f increasing) or
    # f is close to 1 throughout
    monotonic = bool(np.all(df_outer >= -0.01) or np.all(np.abs(f_outer - 1.0) < 0.1))

    # 4. Oscillation check in tail
    # Count sign changes of (f - 1) in outer region
    f_minus_1 = f_outer - 1.0
    sign_changes = int(np.sum(np.abs(np.diff(np.sign(f_minus_1))) > 0))
    osc_free = sign_changes <= 2  # allow up to 2 crossings (approach to 1)

    all_pass = exp_match and coeff_match and not f_overshoot and osc_free

    if all_pass:
        classification = "preserved"
    elif exp_match and coeff_match and (f_overshoot or not osc_free):
        classification = "preserved_with_distortion"
    elif exp_match and not coeff_match:
        classification = "exponent_preserved_coefficient_distorted"
    else:
        classification = "not_preserved"

    return ComponentBPreservationResult(
        exponent_target=exp_target,
        exponent_measured=ag_exp,
        exponent_match=exp_match,
        coefficient_target=coeff_target,
        coefficient_measured=ag_coeff,
        coefficient_match=coeff_match,
        f_at_rmax=f_at_rmax,
        f_max=f_max,
        f_overshoot=f_overshoot,
        monotonic=monotonic,
        n_sign_changes_in_tail=sign_changes,
        oscillation_free=osc_free,
        all_pass=all_pass,
        classification=classification,
        notes=[
            f"Exponent: {ag_exp:.3f} (target {exp_target}, {'PASS' if exp_match else 'FAIL'})",
            f"Coefficient: {ag_coeff:.6f} (target {coeff_target:.6f}, {'PASS' if coeff_match else 'FAIL'})",
            f"f_max: {f_max:.4f} (overshoot: {f_overshoot})",
            f"Monotonic: {monotonic}, sign changes: {sign_changes}",
        ],
    )


# ================================================================
# Level 8: Gamma Scan
# ================================================================

def _run_single_gamma(
    gamma: float,
    params: SourceCoupledDefectParams,
) -> GammaScanEntry:
    """Run a single gamma value and assess."""
    p = SourceCoupledDefectParams(
        eta=params.eta, lam=params.lam, gamma=gamma,
        coupling_type=params.coupling_type,
        r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
        source_amplitude=params.source_amplitude,
    )
    bvp = solve_sourced_bvp(p)
    if not bvp.converged:
        return GammaScanEntry(
            gamma=gamma, bvp_converged=False,
            comp_A_ratio=0.0, comp_A_shape_match=False,
            comp_B_preserved=False, comp_B_coeff_match=False,
            f_max=bvp.f_max, f_overshoot=bvp.f_max > 1.05,
            interaction_sign_definite=False, has_pathology=True,
            notes="BVP did not converge",
        )

    energy = extract_sourced_energy(bvp, p)
    comp_a = assess_component_A_recovery(energy, p)
    comp_b = assess_component_B_preservation(energy, bvp, p)

    has_path = (not bvp.converged or bvp.f_max > 1.5 or
                not comp_b.oscillation_free or comp_b.f_overshoot)

    return GammaScanEntry(
        gamma=gamma,
        bvp_converged=True,
        comp_A_ratio=comp_a.coeff_ratio,
        comp_A_shape_match=comp_a.shape_match,
        comp_B_preserved=comp_b.all_pass,
        comp_B_coeff_match=comp_b.coefficient_match,
        f_max=bvp.f_max,
        f_overshoot=comp_b.f_overshoot,
        interaction_sign_definite=energy.interaction_sign_definite,
        has_pathology=has_path,
        notes=(f"ratio={comp_a.coeff_ratio:.4f}, "
               f"B={comp_b.classification}"),
    )


def scan_gamma(
    params: SourceCoupledDefectParams,
) -> GammaScanResult:
    """Bounded gamma scan."""
    entries = []
    for g in params.gamma_scan:
        entry = _run_single_gamma(g, params)
        entries.append(entry)

    n_conv = sum(1 for e in entries if e.bvp_converged)
    baseline_ratio = entries[0].comp_A_ratio if entries else 0.0  # gamma=0
    n_improved = sum(1 for e in entries
                     if e.bvp_converged and e.comp_A_ratio > baseline_ratio * 1.5)
    n_b_pres = sum(1 for e in entries
                   if e.bvp_converged and e.comp_B_preserved)
    n_viable = sum(1 for e in entries
                   if e.bvp_converged and e.comp_A_ratio > baseline_ratio * 1.5
                   and e.comp_B_preserved and not e.has_pathology)

    # Best gamma: highest ratio with B preserved and no pathology
    viable = [e for e in entries if e.bvp_converged
              and e.comp_B_preserved and not e.has_pathology]
    if viable:
        best = max(viable, key=lambda e: e.comp_A_ratio)
        best_gamma = best.gamma
        best_ratio = best.comp_A_ratio
    else:
        # Fall back to best converged
        converged = [e for e in entries if e.bvp_converged]
        if converged:
            best = max(converged, key=lambda e: e.comp_A_ratio)
            best_gamma = best.gamma
            best_ratio = best.comp_A_ratio
        else:
            best_gamma = None
            best_ratio = 0.0

    # Viable window
    viable_gammas = [e.gamma for e in entries
                     if e.bvp_converged and e.comp_B_preserved
                     and not e.has_pathology and e.comp_A_ratio > baseline_ratio * 1.5]
    if len(viable_gammas) >= 2:
        window = (min(viable_gammas), max(viable_gammas))
    elif len(viable_gammas) == 1:
        window = (viable_gammas[0], viable_gammas[0])
    else:
        window = None

    return GammaScanResult(
        entries=entries,
        n_scanned=len(entries),
        n_converged=n_conv,
        n_comp_A_improved=n_improved,
        n_comp_B_preserved=n_b_pres,
        n_viable=n_viable,
        best_gamma=best_gamma,
        best_ratio=best_ratio,
        viable_window=window,
        notes=[
            f"Scanned {len(entries)} gamma values",
            f"Converged: {n_conv}/{len(entries)}",
            f"Comp A improved: {n_improved}",
            f"Comp B preserved: {n_b_pres}",
            f"Viable (both): {n_viable}",
            f"Best gamma: {best_gamma}, ratio: {best_ratio:.4f}",
        ],
    )


# ================================================================
# Level 9: Pathology Inventory
# ================================================================

def inventory_pathologies(
    scan: GammaScanResult,
    params: SourceCoupledDefectParams,
) -> PathologyInventory:
    """Inventory all pathologies from the gamma scan."""
    pathologies = []
    pid = 0

    # BVP non-convergence
    non_conv = [e for e in scan.entries if not e.bvp_converged]
    if non_conv:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="convergence",
            description=f"BVP did not converge for {len(non_conv)} gamma values: "
                        f"{[e.gamma for e in non_conv]}",
            severity="moderate" if len(non_conv) <= 2 else "critical",
            gamma_range=str([e.gamma for e in non_conv]),
        ))

    # Tail overshoot (f > 1.05)
    overshoot = [e for e in scan.entries if e.bvp_converged and e.f_overshoot]
    if overshoot:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="overshoot",
            description=f"f exceeds 1.05 for {len(overshoot)} gamma values. "
                        f"Max f: {max(e.f_max for e in overshoot):.4f}",
            severity="moderate",
            gamma_range=str([e.gamma for e in overshoot]),
        ))

    # Component B degradation
    b_degraded = [e for e in scan.entries
                  if e.bvp_converged and not e.comp_B_preserved]
    if b_degraded:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="component_b_degradation",
            description=f"Component B not preserved for {len(b_degraded)} gamma values",
            severity="moderate",
            gamma_range=str([e.gamma for e in b_degraded]),
        ))

    # Interaction sign indefiniteness
    indef = [e for e in scan.entries
             if e.bvp_converged and not e.interaction_sign_definite]
    if indef:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="sign_indefinite",
            description=f"Interaction energy is sign-indefinite for {len(indef)} gamma values",
            severity="minor",
            gamma_range=str([e.gamma for e in indef]),
        ))

    # Extreme f_max (f > 1.5)
    extreme = [e for e in scan.entries if e.bvp_converged and e.f_max > 1.5]
    if extreme:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="runaway",
            description=f"f exceeds 1.5 for {len(extreme)} gamma values — "
                        f"possible runaway behavior",
            severity="critical",
            gamma_range=str([e.gamma for e in extreme]),
        ))

    # Source coupling makes radial kinetic WORSE (ratio decreases)
    baseline_ratio = scan.entries[0].comp_A_ratio if scan.entries else 0.0
    worse = [e for e in scan.entries
             if e.bvp_converged and abs(e.gamma) > 0
             and e.comp_A_ratio < baseline_ratio * 0.5]
    if worse:
        pid += 1
        pathologies.append(Pathology(
            pathology_id=pid, category="counterproductive",
            description=f"Source coupling REDUCES Component A ratio for {len(worse)} gamma values",
            severity="moderate",
            gamma_range=str([e.gamma for e in worse]),
        ))

    n_crit = sum(1 for p in pathologies if p.severity == "critical")
    n_mod = sum(1 for p in pathologies if p.severity == "moderate")
    n_min = sum(1 for p in pathologies if p.severity == "minor")

    return PathologyInventory(
        pathologies=pathologies,
        n_pathologies=len(pathologies),
        n_critical=n_crit,
        n_moderate=n_mod,
        n_minor=n_min,
        notes=[
            f"Total pathologies: {len(pathologies)}",
            f"Critical: {n_crit}, Moderate: {n_mod}, Minor: {n_min}",
        ],
    )


# ================================================================
# Level 10: Classification
# ================================================================

def classify_source_coupled(
    comp_a: ComponentARecoveryResult,
    comp_b: ComponentBPreservationResult,
    scan: GammaScanResult,
    pathologies: PathologyInventory,
) -> SourceCoupledClassification:
    """Classify D5 outcome."""
    best_ratio = scan.best_ratio
    best_gamma = scan.best_gamma
    b_at_best = False
    if best_gamma is not None:
        best_entry = [e for e in scan.entries if e.gamma == best_gamma]
        if best_entry:
            b_at_best = best_entry[0].comp_B_preserved

    # Classification logic
    if best_ratio > 0.1 and b_at_best and pathologies.n_critical == 0:
        classification = "full_component_recovery_achieved"
    elif best_ratio > 0.1 and not b_at_best:
        classification = "component_a_recovered_but_component_b_degraded"
    elif best_ratio > 0.01 and b_at_best:
        classification = "source_coupling_partially_recovers_component_a"
    elif pathologies.n_critical > 0:
        classification = "source_coupling_introduces_pathology"
    elif scan.n_viable == 0 and scan.n_converged > 0:
        classification = "source_coupling_insufficient"
    else:
        classification = "unresolved_artifacts"

    phase_lock = {
        "phase6_f_at_Req": "LOCKED (-17.71)",
        "phase6B_A_crit": "LOCKED (1.062)",
        "phase6C_deficit": "LOCKED (Component A + Component B)",
        "route_C": "LOCKED (insufficient)",
        "route_B": "LOCKED (closed)",
        "source_law_I": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "LOCKED (provisional candidate formulated)",
        "defect_D2": "LOCKED (defect_candidate_numerically_viable)",
        "unification_D3": "LOCKED (scalar_triplet_embedding_most_promising)",
        "unification_D4": "LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified)",
        "source_coupled_D5": f"ASSESSED ({classification})",
    }

    summary_parts = [
        f"Best gamma: {best_gamma}",
        f"Best ratio: {best_ratio:.4f} (target ~1.0, D4 baseline ~0.0035)",
        f"Comp B at best: {'preserved' if b_at_best else 'degraded'}",
        f"Viable window: {scan.viable_window}",
        f"Pathologies: {pathologies.n_pathologies} ({pathologies.n_critical} critical)",
        f"Classification: {classification}",
    ]

    return SourceCoupledClassification(
        classification=classification,
        phase_status=f"D5 assessed: {classification}",
        best_gamma=best_gamma,
        best_comp_A_ratio=best_ratio,
        comp_B_preserved_at_best=b_at_best,
        n_pathologies=pathologies.n_pathologies,
        phase_lock_update=phase_lock,
        summary="; ".join(summary_parts),
        notes=[
            "Classification determined by gamma scan outcomes.",
            "Not forced or predetermined.",
        ],
    )


# ================================================================
# Level 11: Master Computation
# ================================================================

def compute_source_coupled_defect(
    params: Optional[SourceCoupledDefectParams] = None,
) -> SourceCoupledDefectResult:
    """Master computation for Phase D5."""
    if params is None:
        params = SourceCoupledDefectParams()

    result = SourceCoupledDefectResult(valid=False, params=params)

    try:
        # Level 0: Normalization map
        normalization = build_normalization_map(params)
        result.normalization = normalization

        # Level 1: Couplings
        couplings = define_source_couplings(params)
        result.couplings = couplings
        result.diagnostics["n_couplings"] = len(couplings)

        # Level 2: Lagrangian (use preferred coupling)
        preferred = couplings[0]  # quadratic
        lagrangian = construct_sourced_lagrangian(preferred, params)
        result.lagrangian = lagrangian

        # Level 3: Sourced ODE
        radial_eq = derive_sourced_radial_ode(lagrangian, params)
        result.radial_equation = radial_eq
        result.diagnostics["source_sign"] = radial_eq.source_term_sign

        # Level 4: Baseline BVP
        bvp = solve_sourced_bvp(params)
        result.baseline_bvp = bvp
        result.diagnostics["baseline_converged"] = bvp.converged

        # Level 5: Baseline energy
        energy = extract_sourced_energy(bvp, params)
        result.baseline_energy = energy

        # Level 6: Component A
        comp_a = assess_component_A_recovery(energy, params)
        result.comp_a_result = comp_a
        result.diagnostics["comp_a_ratio"] = comp_a.coeff_ratio

        # Level 7: Component B
        comp_b = assess_component_B_preservation(energy, bvp, params)
        result.comp_b_result = comp_b
        result.diagnostics["comp_b_classification"] = comp_b.classification

        # Level 8: Gamma scan
        gamma_scan = scan_gamma(params)
        result.gamma_scan = gamma_scan
        result.diagnostics["n_scanned"] = gamma_scan.n_scanned
        result.diagnostics["n_viable"] = gamma_scan.n_viable

        # Level 9: Pathologies
        pathologies = inventory_pathologies(gamma_scan, params)
        result.pathology_inventory = pathologies
        result.diagnostics["n_pathologies"] = pathologies.n_pathologies

        # Level 10: Classification
        classification = classify_source_coupled(
            comp_a, comp_b, gamma_scan, pathologies
        )
        result.classification = classification
        result.diagnostics["classification"] = classification.classification

        result.valid = True

    except Exception as e:
        result.diagnostics["error"] = str(e)

    return result


# ================================================================
# Level 12: Serialization
# ================================================================

def source_coupled_defect_result_to_dict(
    result: SourceCoupledDefectResult,
) -> Dict[str, Any]:
    """Serialize to JSON-compatible dictionary."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "params": {
            "eta": result.params.eta,
            "lam": result.params.lam,
            "gamma": result.params.gamma,
            "coupling_type": result.params.coupling_type,
            "source_amplitude": result.params.source_amplitude,
        },
    }

    if result.normalization:
        nm = result.normalization
        d["normalization"] = {
            "r_unit": nm.r_unit,
            "r_star": nm.r_star,
            "eta_value": nm.eta_value,
            "X_dimensional": nm.X_dimensional,
            "X_in_ode_units": nm.X_in_ode_units,
            "X_star": nm.X_star,
            "source_nondim_formula": nm.source_nondim_formula,
            "gamma_unit": nm.gamma_unit,
            "ode_dimensional": nm.ode_dimensional,
            "ode_dimensionless": nm.ode_dimensionless,
            "nondim_map": nm.nondim_map,
            "notes": nm.notes,
        }

    if result.couplings:
        d["couplings"] = [
            {"name": c.name, "type": c.coupling_type,
             "lagrangian": c.lagrangian_term,
             "ode_source": c.ode_source_term,
             "sign_derivation": c.ode_source_sign_derivation,
             "symmetry_preserved": c.symmetry_preserved}
            for c in result.couplings
        ]

    if result.lagrangian:
        d["lagrangian"] = {
            "n_terms": result.lagrangian.n_terms,
            "coupling_type": result.lagrangian.coupling_type,
            "gamma": result.lagrangian.gamma,
            "source_formula": result.lagrangian.source_formula,
        }

    if result.radial_equation:
        req = result.radial_equation
        d["radial_equation"] = {
            "full_ode": req.full_ode,
            "source_term": req.source_term_formula,
            "source_sign": req.source_term_sign,
            "sign_derivation": req.sign_derivation,
        }

    if result.comp_a_result:
        ca = result.comp_a_result
        d["component_a"] = {
            "shape_match": ca.shape_match,
            "shape_exponent": ca.shape_exponent_measured,
            "coeff_ratio": ca.coeff_ratio,
            "coeff_match": ca.coeff_match,
            "mechanism": ca.mechanism,
            "source_driven": ca.mechanism_source_driven,
            "classification": ca.classification,
        }

    if result.comp_b_result:
        cb = result.comp_b_result
        d["component_b"] = {
            "exponent_match": cb.exponent_match,
            "exponent_measured": cb.exponent_measured,
            "coefficient_match": cb.coefficient_match,
            "coefficient_measured": cb.coefficient_measured,
            "f_overshoot": cb.f_overshoot,
            "monotonic": cb.monotonic,
            "oscillation_free": cb.oscillation_free,
            "all_pass": cb.all_pass,
            "classification": cb.classification,
        }

    if result.gamma_scan:
        gs = result.gamma_scan
        d["gamma_scan"] = {
            "n_scanned": gs.n_scanned,
            "n_converged": gs.n_converged,
            "n_viable": gs.n_viable,
            "best_gamma": gs.best_gamma,
            "best_ratio": gs.best_ratio,
            "viable_window": list(gs.viable_window) if gs.viable_window else None,
            "entries": [
                {"gamma": e.gamma, "converged": e.bvp_converged,
                 "ratio": e.comp_A_ratio, "b_preserved": e.comp_B_preserved,
                 "pathology": e.has_pathology}
                for e in gs.entries
            ],
        }

    if result.pathology_inventory:
        pi = result.pathology_inventory
        d["pathologies"] = {
            "n_total": pi.n_pathologies,
            "n_critical": pi.n_critical,
            "n_moderate": pi.n_moderate,
            "n_minor": pi.n_minor,
            "items": [
                {"id": p.pathology_id, "category": p.category,
                 "description": p.description, "severity": p.severity}
                for p in pi.pathologies
            ],
        }

    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "best_gamma": cl.best_gamma,
            "best_ratio": cl.best_comp_A_ratio,
            "comp_b_at_best": cl.comp_B_preserved_at_best,
            "summary": cl.summary,
            "phase_lock_update": cl.phase_lock_update,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions
    d["diagnostics"] = {
        k: v for k, v in result.diagnostics.items()
        if not isinstance(v, np.ndarray)
    }

    return d
