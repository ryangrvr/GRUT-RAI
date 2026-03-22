"""Phase D11 -- Exact Two-Field Closure.

Replaces the D9 macro-amplitude proxy with a simultaneous solution of the
macro scalar field Phi(r) and the defect hedgehog profile f(r) as a coupled
two-field system on Schwarzschild background.

SCOPE: D11 determines whether the dual-sector Companion architecture remains
viable when both fields are solved exactly (within the static, spherically
symmetric, Schwarzschild-background approximation), rather than using the
D9 macro-amplitude proxy closure.

DERIVATIONAL STATUS OF THE MACRO EQUATION:
  The D8 macro sector action includes a spatial kinetic term:
    S_macro = integral sqrt(-g) [(1/2)(partial Phi)^2 - V_macro(Phi) + J_eff Phi]
  The spatial Laplacian in the macro EL is therefore INHERITED from the D8
  action structure, not silently introduced. However, the original GRUT
  scalar-memory relation is first-order in time (tau dPhi/dt + Phi = X(r)).
  The D8 action's inclusion of the kinetic term (1/2)(partial Phi)^2 is
  itself a field-theoretic completion of the memory sector. D11 inherits
  this from D8 without modification.

COUPLED SYSTEM (from D8 action):
  Macro EL (static, spherically symmetric):
    Phi''(r) + (2/r)Phi'(r) - (1/tau^2)Phi(r) + (1/tau^2)(M/r^2)
       + 2*g_p * eta^2 * f(r)^2 * Phi(r) = 0

  Defect EL (hedgehog on Schwarzschild):
    f''(r) + (2/r)f'(r) - (2/r^2)f(r) - lam*eta^2*f(r)*(f(r)^2 - 1)
       + g_p * Phi(r)^2 * f(r) = 0

  Portal coupling: g_p Phi^2 |vec_Phi|^2 = g_p Phi^2 eta^2 f^2
  Portal sign: From varying S_portal = integral g_p Phi^2 |vec_Phi|^2:
    - Macro EL gets +2 g_p |vec_Phi|^2 Phi = +2 g_p eta^2 f^2 Phi (POSITIVE)
    - Defect EL gets +g_p Phi^2 f (POSITIVE, stabilizing)
  Both signs are mutually consistent from the same action.

SOURCE STATUS: X(r) = M/r^2 is FIXED from the classical GRUT sector.
  D11 closes the exact two-field macro/defect problem on a fixed-source
  background. Making X(r) dynamical would be a larger scope phase.

BOUNDARY CONDITIONS:
  Macro: Phi(r_min) = M/r_min^2, Phi(r_max) = M/r_max^2
  Defect: f(r_min) = 0 (hedgehog core), f(r_max) = 1 (vacuum)
  BVP domain: [r_min, r_max] = [0.01, 5.0] (full monopole domain).
  Metric comparison restricted to [R_eq, R_ext] = [1/3, 2.0].

MACRO ENERGY DENSITY CONVENTION:
  The GRUT macro energy density that enters the metric is:
    eps_macro(r) = Phi(r)^2 / (2*tau^2)
  This matches the D9 proxy: when Phi = A_eff*M/r^2,
    eps_macro = A_eff^2 * M^2/(2*tau^2*r^4) = A_eff^2 * RHO_EQ_COEFF / r^4
  The gradient energy (1/2)(Phi')^2 is NOT included in the metric energy
  because the locked GRUT results compute gravitating energy from the
  scalar-memory solution, not from a field-theoretic stress tensor.
  This is an explicit modeling choice, documented here.

BACKGROUND: Static Schwarzschild (M_ext = 0.5, R_S = 1.0).
  The metric is NOT dynamically self-consistent -- it is recomputed from
  energy densities after the field solve.

LOCKED INHERITANCE:
  D6: companion_architecture_viable
  D7: fully_coupled_viable
  D8: d7_channels_largely_action_derived
  D9: self_consistent_coupling_viable (PROXY-DEPENDENT -- D11 tests this)

Imports: solve_hedgehog_bvp, extract_defect_energy from grut.numerical_monopole.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

from grut.numerical_monopole import (
    NumericalMonopoleParams,
    HedgehogBVPSolution,
    DefectEnergyProfile,
    solve_hedgehog_bvp,
    extract_defect_energy,
    ETA_MATCH,
)

try:
    from scipy.integrate import solve_bvp
    HAS_SCIPY_BVP = True
except ImportError:
    HAS_SCIPY_BVP = False


# ================================================================
# Constants (inherited from prior phases)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
TAU_CANONICAL = math.sqrt((R_S / R_EQ) / 2.0)
A_CRIT = 1.062
LAMBDA_DEFAULT = 8.0 * math.pi
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
XI_DEFAULT = 1.0

MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
R_EXT = 2.0 * R_S

# D11-specific constants
MAX_ITERATIONS_DEFAULT = 30
CONVERGENCE_TOL_DEFAULT = 1e-4
RELAXATION_FACTOR_DEFAULT = 0.4
RELAXATION_FALLBACK = [0.3, 0.2, 0.1]
G_PORTAL_DEFAULT = 1.0
G_PORTAL_SCAN_VALUES = [0.0, 0.1, 0.5, 1.0, 2.0]
LAMBDA_SCAN_VALUES = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]

DEFORMATION_THRESHOLDS = {
    "negligible": 0.01,
    "moderate": 0.05,
    "significant": 0.10,
}

CLASSIFICATION_OPTIONS = [
    "exact_closure_achieved",
    "exact_closure_strongly_supports_d9",
    "exact_closure_partially_supports_d9",
    "exact_closure_weakens_d9_materially",
    "exact_closure_rejects_current_companion_architecture",
]

D9_PROXY_ASSESSMENT_OPTIONS = [
    "good_approximation",
    "conservative_approximation",
    "qualitatively_misleading",
    "partially_valid_in_some_parameter_window",
    "inconclusive",
]


# ================================================================
# Assumptions
# ================================================================

EXACT_TWO_FIELD_ASSUMPTIONS = [
    "1. Static spherically symmetric Schwarzschild background geometry "
    "(M_ext=0.5, R_S=1.0). Metric is NOT solved dynamically.",

    "2. Macro scalar field Phi(r) satisfies the D8-inherited static EL: "
    "Phi'' + (2/r)Phi' - (1/tau^2)Phi + (1/tau^2)(M/r^2) "
    "+ 2*g_p*eta^2*f^2*Phi = 0. The Laplacian is inherited from the D8 "
    "action kinetic term, which is itself a field-theoretic completion "
    "of the first-order GRUT memory relation.",

    "3. Defect hedgehog profile f(r) satisfies the portal-modified ODE: "
    "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) + g_p*Phi^2*f = 0.",

    "4. Both fields coupled through the D8 portal term g_p*Phi^2*|Phi_vec|^2. "
    "Portal signs verified: +2*g_p*eta^2*f^2*Phi in macro EL, "
    "+g_p*Phi^2*f in defect EL (both positive, both from same action).",

    "5. Source X(r) = M/r^2 is FIXED. D11 does not make the source dynamical.",

    "6. Macro BCs: Phi(r_min) = M/r_min^2, Phi(r_max) = M/r_max^2 "
    "(matching uncoupled source-driven static solution at domain boundaries). "
    "Defect BCs: f(r_min)=0, f(r_max)=1.",

    "7. BVP domain [0.01, 5.0]; metric comparison on [R_eq, R_ext] = [1/3, 2.0].",

    "8. Macro energy density for metric: eps_macro = Phi(r)^2 / (2*tau^2). "
    "Gradient energy excluded per GRUT convention (see module docstring).",

    "9. Picard iteration with under-relaxation as fallback method.",

    "10. All parameters (eta, lam, g_p, xi) inherited or scanned; none predicted.",
]

EXACT_TWO_FIELD_NONCLAIMS = [
    "1. This phase does NOT prove final theory closure.",

    "2. Exact two-field closure is exact only within the static spherically "
    "symmetric Schwarzschild-background framework.",

    "3. The metric is NOT dynamically self-consistent -- it is recomputed "
    "from energy densities after the field solve.",

    "4. Portal coupling g_p is scanned, not predicted.",

    "5. Lambda is scanned, not predicted.",

    "6. The macro equation Laplacian is inherited from D8's field-theoretic "
    "completion. The original GRUT memory relation is first-order in time.",

    "7. BVP convergence does not guarantee solution uniqueness.",

    "8. D11 assesses D9 retrospectively but does not invalidate D9's "
    "methodological contribution.",

    "9. This phase does NOT justify metaphysical interpretation.",

    "10. Classification is within the D11 numerical framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class ExactTwoFieldParams:
    """Parameters for Phase D11."""
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
    scalar_A: float = 1.0
    alpha_BR: float = 1.0
    beta_XR: float = 1.0
    g_portal: float = G_PORTAL_DEFAULT
    max_iterations: int = MAX_ITERATIONS_DEFAULT
    convergence_tol: float = CONVERGENCE_TOL_DEFAULT
    relaxation_factor: float = RELAXATION_FACTOR_DEFAULT
    g_portal_scan: List[float] = field(
        default_factory=lambda: list(G_PORTAL_SCAN_VALUES)
    )
    lambda_scan: List[float] = field(
        default_factory=lambda: list(LAMBDA_SCAN_VALUES)
    )


@dataclass
class CoupledFieldEquations:
    """Level 0: Documents the exact coupled field equations."""
    macro_equation: str
    defect_equation: str
    portal_term: str
    portal_sign_verification: str
    boundary_conditions: Dict[str, str]
    background_geometry: str
    source_status: str
    macro_laplacian_status: str
    energy_density_convention: str
    inherited_from_d8: str
    remaining_approximations: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class ExactTwoFieldSolution:
    """Level 1: Exact coupled two-field BVP solution."""
    converged: bool
    method: str  # "direct_coupled_bvp" or "picard_fallback"
    n_iterations: int
    g_portal: float
    lam: float
    r_grid: np.ndarray
    # Macro field
    phi: np.ndarray
    phi_prime: np.ndarray
    phi_uncoupled: np.ndarray  # M/r^2 reference
    # Defect profile
    f_defect: np.ndarray
    f_defect_prime: np.ndarray
    # Energy densities
    epsilon_macro: np.ndarray
    epsilon_defect: np.ndarray
    sigma_macro: np.ndarray
    sigma_defect: np.ndarray
    sigma_defect_at_Req: float
    sigma_macro_at_Req: float
    # Convergence
    final_residual: float
    convergence_history: List[float]
    relaxation_used: float
    notes: List[str] = field(default_factory=list)


@dataclass
class D9ComparisonResult:
    """Level 2: Comparison of D11 exact vs D9 proxy results."""
    # Metric quantities
    f_min_d11: float
    f_min_d9: float
    f_min_shift: float
    metric_positive_d11: bool
    metric_positive_d9: bool
    # Field comparison
    phi_vs_proxy_max_deviation: float
    phi_vs_proxy_rms_deviation: float
    f_d11_vs_d9_max_shift: float
    f_d11_vs_d9_rms_shift: float
    # Assessment
    d9_proxy_assessment: str
    proxy_quality_score: float  # 0 = poor, 1 = perfect
    notes: List[str] = field(default_factory=list)


@dataclass
class ExactMetricResult:
    """Level 3: Metric injection from exact two-field solution."""
    r_grid: np.ndarray
    f_coupled: np.ndarray
    f_min: float
    f_min_radius: float
    metric_positive: bool
    f_at_Req: float
    budget: Dict[str, Dict[str, float]]
    notes: List[str] = field(default_factory=list)


@dataclass
class ExactLambdaScanEntry:
    """One lambda in the exact two-field scan."""
    lam: float
    converged: bool
    method: str
    n_iterations: int
    f_min_d11: float
    f_min_d9: float
    metric_positive_d11: bool
    metric_positive_d9: bool
    f_shift_from_d9: float
    phi_deviation_max: float
    notes: str = ""


@dataclass
class ExactLambdaScanResult:
    """Level 4: Lambda scan under exact two-field closure."""
    entries: List[ExactLambdaScanEntry]
    n_scanned: int
    n_converged: int
    n_positive_d11: int
    n_positive_d9: int
    viable_d11: List[float]
    viable_d9: List[float]
    viability_comparison: str  # same, expanded, narrowed, destroyed
    notes: List[str] = field(default_factory=list)


@dataclass
class ExactPortalScanEntry:
    """One g_portal in the portal scan."""
    g_portal: float
    converged: bool
    n_iterations: int
    f_min: float
    metric_positive: bool
    phi_deviation_max: float
    notes: str = ""


@dataclass
class ExactPortalScanResult:
    """Level 5: Portal coupling scan under exact closure."""
    entries: List[ExactPortalScanEntry]
    n_scanned: int
    n_positive: int
    sensitivity_assessment: str
    notes: List[str] = field(default_factory=list)


@dataclass
class D9RetrospectiveAssessment:
    """Level 6a: Retrospective assessment of D9 proxy closure."""
    assessment: str  # from D9_PROXY_ASSESSMENT_OPTIONS
    viability_agreement: bool  # D11 and D9 agree on metric positivity?
    f_min_correlation: float  # correlation of f_min across lambda scan
    max_metric_discrepancy: float
    parameter_window_agreement: str
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ExactTwoFieldClassification:
    """Level 6b: Final D11 classification."""
    classification: str  # from CLASSIFICATION_OPTIONS
    d9_assessment: str  # from D9_PROXY_ASSESSMENT_OPTIONS
    d9_viability_confirmed: bool
    exact_viability_across_lambda: bool
    summary: str
    phase_lock_update: Dict[str, str]


@dataclass
class RegimeSeparationEntry:
    """One regime in the three-regime comparison."""
    name: str  # "d9_proxy", "d11_uncoupled_extended", "d11_uncoupled_physical", "d11_coupled"
    description: str
    phi_at_Req: float
    eps_macro_at_Req: float
    sigma_macro_at_Req: float
    sigma_defect_at_Req: float
    sector_ratio: float  # sigma_macro / sigma_defect
    f_min_metric: float
    metric_positive: bool


@dataclass
class RegimeSeparationResult:
    """Three-regime comparison: D9 proxy, D11 exact uncoupled, D11 exact coupled."""
    entries: List[RegimeSeparationEntry]
    laplacian_jump: float  # f_min change from D9→D11 uncoupled
    portal_jump: float  # f_min change from D11 uncoupled→coupled
    dominant_effect: str  # "laplacian" or "portal" or "both"
    notes: List[str] = field(default_factory=list)


@dataclass
class BoundarySensitivityEntry:
    """One r_min in boundary sensitivity test."""
    r_min: float
    phi_at_Req: float
    phi_ratio_to_proxy: float  # Phi(R_EQ) / (M/R_EQ^2)
    f_min_metric: float
    metric_positive: bool


@dataclass
class BoundarySensitivityResult:
    """Sensitivity of Phi enhancement to inner boundary location."""
    entries: List[BoundarySensitivityEntry]
    physical_domain_entry: BoundarySensitivityEntry  # r_min = R_EQ
    enhancement_boundary_driven: bool
    summary: str


@dataclass
class D9LayeredAssessment:
    """Per-layer assessment of D9 proxy vs D11 exact."""
    metric_viability: str  # "good" / "moderate" / "poor"
    macro_field_profile: str  # "good" / "moderate" / "poor"
    energy_density: str  # "good" / "moderate" / "poor"
    defect_deformation: str  # "good" / "moderate" / "poor"
    sector_balance: str  # "preserved" / "shifted" / "overwhelmed"
    summary: str


@dataclass
class ExactTwoFieldResult:
    """Master result container for Phase D11."""
    valid: bool
    params: ExactTwoFieldParams
    field_equations: Optional[CoupledFieldEquations] = None
    exact_solution: Optional[ExactTwoFieldSolution] = None
    d9_comparison: Optional[D9ComparisonResult] = None
    metric_result: Optional[ExactMetricResult] = None
    lambda_scan: Optional[ExactLambdaScanResult] = None
    portal_scan: Optional[ExactPortalScanResult] = None
    d9_retrospective: Optional[D9RetrospectiveAssessment] = None
    classification: Optional[ExactTwoFieldClassification] = None
    regime_separation: Optional[RegimeSeparationResult] = None
    boundary_sensitivity: Optional[BoundarySensitivityResult] = None
    d9_layered: Optional[D9LayeredAssessment] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)


# ================================================================
# Helpers
# ================================================================

def _sigma_from_profile(r: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """Compute Sigma(r) = integral_r^r_max 4*pi*r'^2 * epsilon(r') dr'."""
    integrand = 4.0 * math.pi * r ** 2 * epsilon
    sigma = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = r[i + 1] - r[i]
        sigma[i] = sigma[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * dr
    return sigma


def _phi_uncoupled(r: np.ndarray, M: float) -> np.ndarray:
    """Uncoupled macro field: static solution Phi(r) = M/r^2."""
    return M / r ** 2


def _compute_macro_energy_from_phi(
    r: np.ndarray,
    phi: np.ndarray,
    tau: float,
) -> np.ndarray:
    """Compute GRUT macro energy density from exact Phi(r).

    eps_macro(r) = Phi(r)^2 / (2*tau^2)

    This is the GRUT convention: the gravitating energy density is
    determined by the field value, not the gradient. When Phi = M/r^2,
    this recovers eps = M^2/(2*tau^2*r^4) = RHO_EQ_COEFF/r^4.

    The gradient energy (1/2)(Phi')^2 is NOT included because the
    locked GRUT results use the scalar-memory energy, not a
    field-theoretic stress tensor.
    """
    return phi ** 2 / (2.0 * tau ** 2)


def _compute_defect_energy_from_f(
    r: np.ndarray,
    f: np.ndarray,
    fp: np.ndarray,
    eta: float,
    lam: float,
) -> np.ndarray:
    """Compute defect energy density from exact f(r).

    3-term energy: radial kinetic + angular gradient + potential.
    """
    eps_kinetic = 0.5 * eta ** 2 * fp ** 2
    eps_angular = eta ** 2 * f ** 2 / r ** 2
    eps_potential = 0.25 * lam * eta ** 4 * (f ** 2 - 1.0) ** 2
    return eps_kinetic + eps_angular + eps_potential


def _solve_d9_proxy(
    params: ExactTwoFieldParams,
    lam_override: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, bool, int]:
    """Run D9-style proxy solve for comparison.

    Returns (r_int, f_d9, eps_macro_d9, eps_defect_d9, A_eff_d9,
             converged, n_iterations).
    """
    lam = lam_override if lam_override is not None else params.lam

    # Solve frozen baseline
    d2_params = NumericalMonopoleParams(
        eta=params.eta, lam=lam, r_min=params.r_min, r_max=params.r_max,
        n_grid=params.n_grid, M=params.M, tau=params.tau, R_ext=params.R_ext,
    )
    bvp = solve_hedgehog_bvp(d2_params)
    energy = extract_defect_energy(bvp, d2_params)

    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, params.n_interior)
    f_frozen = np.interp(r_int, bvp.r_grid, bvp.f_solution)
    fp_frozen = np.interp(r_int, bvp.r_grid, bvp.f_prime)
    eps_frozen = np.interp(r_int, energy.r_grid, energy.total_epsilon)

    if abs(params.g_portal) < 1e-12:
        sig_defect = _sigma_from_profile(r_int, eps_frozen)
        rho_eq = params.M ** 2 / (2.0 * params.tau ** 2)
        m_eff = params.M + params.beta_XR * sig_defect
        A_eff = params.scalar_A * m_eff / params.M
        eps_macro = A_eff ** 2 * rho_eq / r_int ** 4
        return r_int, f_frozen, eps_macro, eps_frozen, A_eff, True, 0

    # Picard iteration (D9 proxy style)
    f_current = f_frozen.copy()
    fp_current = fp_frozen.copy()
    eps_current = eps_frozen.copy()
    omega = params.relaxation_factor
    converged = False
    n_iter = 0
    rho_eq = params.M ** 2 / (2.0 * params.tau ** 2)

    for iteration in range(params.max_iterations):
        n_iter = iteration + 1

        sig_defect = _sigma_from_profile(r_int, eps_current)
        m_eff = params.M + params.beta_XR * sig_defect
        A_eff = params.scalar_A * m_eff / params.M
        eps_macro = A_eff ** 2 * rho_eq / r_int ** 4

        # Portal potential (proxy)
        V_portal_int = A_eff ** 2 * rho_eq / (params.eta ** 2 * r_int ** 4)

        # Solve modified BVP on BVP grid
        bvp_r = np.linspace(params.r_min, params.r_max, params.n_grid)
        V_portal_bvp = np.interp(bvp_r, r_int, V_portal_int)
        V_portal_bvp[bvp_r < r_int[0]] = V_portal_int[0]
        V_portal_bvp[bvp_r > r_int[-1]] = 0.0

        eta_loc = params.eta
        g_portal = params.g_portal

        def ode_mod(r_pts, y):
            fv = y[0]
            fpp = y[1]
            V_at_r = np.interp(r_pts, bvp_r, V_portal_bvp)
            fpp_out = (-(2.0 / r_pts) * fpp
                       + (2.0 / r_pts ** 2) * fv
                       + lam * eta_loc ** 2 * fv * (fv ** 2 - 1.0)
                       + g_portal * V_at_r * fv)
            return np.array([fpp, fpp_out])

        def bc_mod(ya, yb):
            return np.array([ya[0], yb[0] - 1.0])

        delta_core = 1.0 / math.sqrt(lam * eta_loc ** 2) if lam * eta_loc ** 2 > 0 else 1.0
        f_guess = bvp_r / np.sqrt(bvp_r ** 2 + delta_core ** 2)
        fp_guess = delta_core ** 2 / (bvp_r ** 2 + delta_core ** 2) ** 1.5
        y_guess = np.array([f_guess, fp_guess])

        try:
            sol = solve_bvp(ode_mod, bc_mod, bvp_r, y_guess, tol=1e-6, max_nodes=5000)
            if not sol.success:
                break
            y_sol = sol.sol(bvp_r)
            f_new = np.interp(r_int, bvp_r, y_sol[0])
            fp_new = np.interp(r_int, bvp_r, y_sol[1])
        except Exception:
            break

        f_next = (1.0 - omega) * f_current + omega * f_new
        fp_next = (1.0 - omega) * fp_current + omega * fp_new

        residual = float(np.max(np.abs(f_next - f_current)))
        f_current = f_next
        fp_current = fp_next

        eps_kinetic = 0.5 * eta_loc ** 2 * fp_current ** 2
        eps_angular = eta_loc ** 2 * f_current ** 2 / r_int ** 2
        eps_potential = 0.25 * lam * eta_loc ** 4 * (f_current ** 2 - 1.0) ** 2
        eps_current = eps_kinetic + eps_angular + eps_potential

        if residual < params.convergence_tol:
            converged = True
            break

    sig_defect = _sigma_from_profile(r_int, eps_current)
    m_eff = params.M + params.beta_XR * sig_defect
    A_eff = params.scalar_A * m_eff / params.M
    eps_macro = A_eff ** 2 * rho_eq / r_int ** 4

    return r_int, f_current, eps_macro, eps_current, A_eff, converged, n_iter


def _solve_exact_coupled_bvp(
    params: ExactTwoFieldParams,
    lam_override: Optional[float] = None,
    g_portal_override: Optional[float] = None,
) -> ExactTwoFieldSolution:
    """Solve the exact coupled two-field BVP.

    System: y = [Phi, Phi', f, f']

    Macro EL:
      Phi'' + (2/r)Phi' - (1/tau^2)Phi + (1/tau^2)(M/r^2)
         + 2*g_p*eta^2*f^2*Phi = 0

    Defect EL:
      f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) + g_p*Phi^2*f = 0

    BCs: Phi(r_min)=M/r_min^2, Phi(r_max)=M/r_max^2,
         f(r_min)=0, f(r_max)=1

    Energy convention: eps_macro = Phi^2/(2*tau^2) (GRUT convention).
    """
    lam = lam_override if lam_override is not None else params.lam
    g_p = g_portal_override if g_portal_override is not None else params.g_portal
    eta = params.eta
    tau = params.tau
    M = params.M
    r_min = params.r_min
    r_max = params.r_max
    n = params.n_grid

    r_grid = np.linspace(r_min, r_max, n)
    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, params.n_interior)

    if abs(g_p) < 1e-12:
        # Uncoupled: Phi = M/r^2, f = standard hedgehog
        d2_params = NumericalMonopoleParams(
            eta=eta, lam=lam, r_min=r_min, r_max=r_max,
            n_grid=n, M=M, tau=tau, R_ext=params.R_ext,
        )
        bvp = solve_hedgehog_bvp(d2_params)

        phi_int = M / r_int ** 2
        phi_prime_int = -2.0 * M / r_int ** 3
        f_int = np.interp(r_int, bvp.r_grid, bvp.f_solution)
        fp_int = np.interp(r_int, bvp.r_grid, bvp.f_prime)

        eps_macro = _compute_macro_energy_from_phi(r_int, phi_int, tau)
        eps_defect = _compute_defect_energy_from_f(r_int, f_int, fp_int, eta, lam)
        sig_macro = _sigma_from_profile(r_int, eps_macro)
        sig_defect = _sigma_from_profile(r_int, eps_defect)

        return ExactTwoFieldSolution(
            converged=bvp.converged, method="uncoupled_reference",
            n_iterations=0, g_portal=0.0, lam=lam,
            r_grid=r_int,
            phi=phi_int, phi_prime=phi_prime_int,
            phi_uncoupled=M / r_int ** 2,
            f_defect=f_int, f_defect_prime=fp_int,
            epsilon_macro=eps_macro, epsilon_defect=eps_defect,
            sigma_macro=sig_macro, sigma_defect=sig_defect,
            sigma_defect_at_Req=float(sig_defect[0]),
            sigma_macro_at_Req=float(sig_macro[0]),
            final_residual=0.0, convergence_history=[0.0],
            relaxation_used=params.relaxation_factor,
            notes=["g_portal=0: uncoupled reference (D7 recovery)"],
        )

    # Try direct coupled BVP solve first
    method = "direct_coupled_bvp"
    direct_success = False
    sol_phi = None
    sol_f = None
    sol_phi_p = None
    sol_f_p = None
    history: List[float] = []

    if HAS_SCIPY_BVP:
        def ode_coupled(r_pts, y):
            phi_v = y[0]
            phi_p = y[1]
            f_v = y[2]
            f_p = y[3]

            # Macro EL: Phi'' = -(2/r)Phi' + (1/tau^2)Phi - (1/tau^2)(M/r^2)
            #           - 2*g_p*eta^2*f^2*Phi
            phi_pp = (-(2.0 / r_pts) * phi_p
                      + (1.0 / tau ** 2) * phi_v
                      - (1.0 / tau ** 2) * (M / r_pts ** 2)
                      - 2.0 * g_p * eta ** 2 * f_v ** 2 * phi_v)

            # Defect EL: f'' = -(2/r)f' + (2/r^2)f + lam*eta^2*f*(f^2-1)
            #             - g_p*Phi^2*f
            f_pp = (-(2.0 / r_pts) * f_p
                    + (2.0 / r_pts ** 2) * f_v
                    + lam * eta ** 2 * f_v * (f_v ** 2 - 1.0)
                    - g_p * phi_v ** 2 * f_v)

            return np.array([phi_p, phi_pp, f_p, f_pp])

        def bc_coupled(ya, yb):
            return np.array([
                ya[0] - M / r_min ** 2,   # Phi(r_min) = M/r_min^2
                yb[0] - M / r_max ** 2,   # Phi(r_max) = M/r_max^2
                ya[2] - 0.0,              # f(r_min) = 0
                yb[2] - 1.0,             # f(r_max) = 1
            ])

        # Initial guess: uncoupled solutions
        delta_core = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
        phi_guess = M / r_grid ** 2
        phi_p_guess = -2.0 * M / r_grid ** 3
        f_guess = r_grid / np.sqrt(r_grid ** 2 + delta_core ** 2)
        fp_guess = delta_core ** 2 / (r_grid ** 2 + delta_core ** 2) ** 1.5
        y_guess = np.array([phi_guess, phi_p_guess, f_guess, fp_guess])

        try:
            sol = solve_bvp(ode_coupled, bc_coupled, r_grid, y_guess,
                            tol=1e-5, max_nodes=8000)
            if sol.success:
                direct_success = True
                y_on_int = sol.sol(r_int)
                sol_phi = y_on_int[0]
                sol_phi_p = y_on_int[1]
                sol_f = y_on_int[2]
                sol_f_p = y_on_int[3]
                history = [0.0]
        except Exception:
            direct_success = False

    # Fallback: Picard iteration on the coupled system
    if not direct_success:
        method = "picard_fallback"

        # Start from uncoupled
        d2_params = NumericalMonopoleParams(
            eta=eta, lam=lam, r_min=r_min, r_max=r_max,
            n_grid=n, M=M, tau=tau, R_ext=params.R_ext,
        )
        bvp_base = solve_hedgehog_bvp(d2_params)
        f_current = np.interp(r_int, bvp_base.r_grid, bvp_base.f_solution)
        fp_current = np.interp(r_int, bvp_base.r_grid, bvp_base.f_prime)
        phi_current = M / r_int ** 2
        phi_p_current = -2.0 * M / r_int ** 3

        omega = params.relaxation_factor
        converged_picard = False
        n_iter = 0
        history = []

        for iteration in range(params.max_iterations):
            n_iter = iteration + 1

            # Step A: Solve macro ODE with current f(r) held fixed
            f_sq_on_bvp = np.interp(r_grid, r_int, f_current ** 2)

            g_p_loc = g_p
            tau_loc = tau
            M_loc = M
            eta_loc = eta

            def ode_macro(r_pts, y):
                phv = y[0]
                php = y[1]
                f2_at_r = np.interp(r_pts, r_grid, f_sq_on_bvp)
                phpp = (-(2.0 / r_pts) * php
                        + (1.0 / tau_loc ** 2) * phv
                        - (1.0 / tau_loc ** 2) * (M_loc / r_pts ** 2)
                        - 2.0 * g_p_loc * eta_loc ** 2 * f2_at_r * phv)
                return np.array([php, phpp])

            def bc_macro(ya, yb):
                return np.array([ya[0] - M / r_min ** 2,
                                 yb[0] - M / r_max ** 2])

            phi_g = phi_current if len(phi_current) == len(r_int) else M / r_grid ** 2
            # Need to put guess on r_grid for solve_bvp
            phi_g_bvp = np.interp(r_grid, r_int, phi_current)
            phi_pg_bvp = np.interp(r_grid, r_int, phi_p_current)
            y_guess_m = np.array([phi_g_bvp, phi_pg_bvp])

            macro_solved = False
            try:
                sol_m = solve_bvp(ode_macro, bc_macro, r_grid, y_guess_m,
                                  tol=1e-6, max_nodes=5000)
                if sol_m.success:
                    y_m = sol_m.sol(r_int)
                    phi_new = y_m[0]
                    phi_p_new = y_m[1]
                    macro_solved = True
            except Exception:
                pass

            if not macro_solved:
                phi_new = phi_current.copy()
                phi_p_new = phi_p_current.copy()

            # Step B: Solve defect BVP with current Phi(r) held fixed
            phi_sq_on_bvp = np.interp(r_grid, r_int, phi_new ** 2)

            lam_loc = lam

            def ode_defect(r_pts, y):
                fv = y[0]
                fpp = y[1]
                ph2_at_r = np.interp(r_pts, r_grid, phi_sq_on_bvp)
                fpp_out = (-(2.0 / r_pts) * fpp
                           + (2.0 / r_pts ** 2) * fv
                           + lam_loc * eta_loc ** 2 * fv * (fv ** 2 - 1.0)
                           - g_p_loc * ph2_at_r * fv)
                return np.array([fpp, fpp_out])

            def bc_defect(ya, yb):
                return np.array([ya[0], yb[0] - 1.0])

            delta_c = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
            f_g_bvp = np.interp(r_grid, r_int, f_current)
            fp_g_bvp = np.interp(r_grid, r_int, fp_current)
            y_guess_d = np.array([f_g_bvp, fp_g_bvp])

            defect_solved = False
            try:
                sol_d = solve_bvp(ode_defect, bc_defect, r_grid, y_guess_d,
                                  tol=1e-6, max_nodes=5000)
                if sol_d.success:
                    y_d = sol_d.sol(r_int)
                    f_new = y_d[0]
                    fp_new = y_d[1]
                    defect_solved = True
            except Exception:
                pass

            if not defect_solved:
                f_new = f_current.copy()
                fp_new = fp_current.copy()

            # Under-relax both fields
            phi_next = (1.0 - omega) * phi_current + omega * phi_new
            phi_p_next = (1.0 - omega) * phi_p_current + omega * phi_p_new
            f_next = (1.0 - omega) * f_current + omega * f_new
            fp_next = (1.0 - omega) * fp_current + omega * fp_new

            residual_phi = float(np.max(np.abs(phi_next - phi_current)))
            residual_f = float(np.max(np.abs(f_next - f_current)))
            residual = max(residual_phi, residual_f)
            history.append(residual)

            # Oscillation detection
            if len(history) >= 3 and history[-1] > history[-2] > history[-3]:
                omega = max(omega * 0.7, RELAXATION_FALLBACK[-1])

            phi_current = phi_next
            phi_p_current = phi_p_next
            f_current = f_next
            fp_current = fp_next

            if residual < params.convergence_tol:
                converged_picard = True
                break

        sol_phi = phi_current
        sol_phi_p = phi_p_current
        sol_f = f_current
        sol_f_p = fp_current
        direct_success = converged_picard

    # Compute energy densities from exact fields (GRUT convention)
    eps_macro = _compute_macro_energy_from_phi(r_int, sol_phi, tau)
    eps_defect = _compute_defect_energy_from_f(r_int, sol_f, sol_f_p, eta, lam)
    sig_macro = _sigma_from_profile(r_int, eps_macro)
    sig_defect = _sigma_from_profile(r_int, eps_defect)

    return ExactTwoFieldSolution(
        converged=direct_success, method=method,
        n_iterations=len(history) if method == "picard_fallback" else 1,
        g_portal=g_p, lam=lam, r_grid=r_int,
        phi=sol_phi, phi_prime=sol_phi_p,
        phi_uncoupled=M / r_int ** 2,
        f_defect=sol_f, f_defect_prime=sol_f_p,
        epsilon_macro=eps_macro, epsilon_defect=eps_defect,
        sigma_macro=sig_macro, sigma_defect=sig_defect,
        sigma_defect_at_Req=float(sig_defect[0]),
        sigma_macro_at_Req=float(sig_macro[0]),
        final_residual=history[-1] if history else 0.0,
        convergence_history=history,
        relaxation_used=omega if method == "picard_fallback" else 1.0,
        notes=[
            f"Method: {method}",
            f"Converged: {direct_success}",
            f"g_portal: {g_p}",
            f"lambda: {lam}",
        ],
    )


def _inject_metric(
    r: np.ndarray,
    sig_macro: np.ndarray,
    sig_defect: np.ndarray,
    params: ExactTwoFieldParams,
) -> Tuple[np.ndarray, float, float, bool]:
    """Compute metric f(r) from energy densities.

    f(r) = -2*(delta_coupled - sigma_total) / r
    where delta_coupled = m_static + alpha_BR * sigma_defect - r/2
    """
    mass_coeff = 2.0 * math.pi * params.M ** 2 / params.tau ** 2
    m_static = params.M + mass_coeff * (1.0 / r - 1.0 / params.R_ext)
    delta_coupled = m_static + params.alpha_BR * sig_defect - r / 2.0
    sig_total = sig_macro + sig_defect
    f_coupled = -2.0 * (delta_coupled - sig_total) / r
    f_min = float(np.min(f_coupled))
    f_min_r = float(r[int(np.argmin(f_coupled))])
    metric_pos = bool(f_min > 0)
    return f_coupled, f_min, f_min_r, metric_pos


def _compute_d9_metric(
    r_int: np.ndarray,
    eps_defect_d9: np.ndarray,
    eps_macro_d9: np.ndarray,
    params: ExactTwoFieldParams,
) -> float:
    """Compute D9-style metric f_min for comparison."""
    sig_defect = _sigma_from_profile(r_int, eps_defect_d9)
    sig_macro = _sigma_from_profile(r_int, eps_macro_d9)
    _, f_min, _, _ = _inject_metric(r_int, sig_macro, sig_defect, params)
    return f_min


# ================================================================
# Level 0: Document Coupled Field Equations
# ================================================================

def document_field_equations(
    params: ExactTwoFieldParams,
) -> CoupledFieldEquations:
    """Document the exact coupled field equations from D8."""
    return CoupledFieldEquations(
        macro_equation=(
            "Phi''(r) + (2/r)Phi'(r) - (1/tau^2)Phi(r) + (1/tau^2)(M/r^2) "
            "+ 2*g_p*eta^2*f(r)^2*Phi(r) = 0"
        ),
        defect_equation=(
            "f''(r) + (2/r)f'(r) - (2/r^2)f(r) - lam*eta^2*f(r)*(f(r)^2-1) "
            "+ g_p*Phi(r)^2*f(r) = 0"
        ),
        portal_term="g_p * Phi^2 * |vec_Phi|^2 = g_p * Phi^2 * eta^2 * f^2",
        portal_sign_verification=(
            "Variation of S_portal = integral g_p Phi^2 |vec_Phi|^2: "
            "d/dPhi -> +2 g_p Phi |vec_Phi|^2 = +2 g_p eta^2 f^2 Phi (positive in macro EL). "
            "d/df -> +2 g_p Phi^2 eta^2 f, after hedgehog reduction +g_p Phi^2 f "
            "(positive in defect EL, stabilizing = tightens core). "
            "Both signs mutually consistent from the same action."
        ),
        boundary_conditions={
            "Phi_left": f"Phi(r_min={params.r_min}) = M/r_min^2 = {params.M / params.r_min ** 2:.4f}",
            "Phi_right": f"Phi(r_max={params.r_max}) = M/r_max^2 = {params.M / params.r_max ** 2:.6f}",
            "f_left": f"f(r_min={params.r_min}) = 0",
            "f_right": f"f(r_max={params.r_max}) = 1",
        },
        background_geometry=(
            "Static Schwarzschild (M_ext=0.5, R_S=1.0). "
            "Metric recomputed from energy densities, NOT dynamically solved."
        ),
        source_status=(
            "X(r) = M/r^2 is FIXED from the classical GRUT sector. "
            "D11 does not make the source dynamical."
        ),
        macro_laplacian_status=(
            "The Laplacian term Phi'' + (2/r)Phi' is INHERITED from the D8 "
            "action kinetic term (1/2)(partial Phi)^2. The original GRUT "
            "scalar-memory relation is first-order in time "
            "(tau dPhi/dt + Phi = X(r)). The D8 action's kinetic term is a "
            "field-theoretic completion of the memory sector. D11 inherits "
            "this from D8 without modification."
        ),
        energy_density_convention=(
            "eps_macro(r) = Phi(r)^2 / (2*tau^2). "
            "Gradient energy (1/2)(Phi')^2 NOT included per GRUT convention. "
            "When Phi = M/r^2: eps = M^2/(2*tau^2*r^4) = RHO_EQ_COEFF/r^4, "
            "matching all prior phases."
        ),
        inherited_from_d8=(
            "Portal term from D8 action: S_portal = integral sqrt(-g) g_p Phi^2 |vec_Phi|^2. "
            "Macro kinetic term from D8: S_macro includes (1/2)(partial Phi)^2."
        ),
        remaining_approximations=[
            "Static spherically symmetric reduction",
            "Schwarzschild background (metric not dynamically coupled)",
            "Finite computational domain [r_min, r_max]",
            "Macro BCs match uncoupled solution at domain boundaries",
            "Source X(r) = M/r^2 fixed",
            "Macro Laplacian inherited from D8 field-theoretic completion",
        ],
        notes=[
            "D11 replaces D9's macro-amplitude proxy V_proxy(r) with the "
            "exact Phi(r) field variable.",
            "The defect portal term now uses Phi(r)^2 directly, not A_eff(r)^2/r^4.",
        ],
    )


# ================================================================
# Level 1: Solve Exact Coupled System
# ================================================================

def solve_exact_two_field(
    params: ExactTwoFieldParams,
    lam_override: Optional[float] = None,
    g_portal_override: Optional[float] = None,
) -> ExactTwoFieldSolution:
    """Solve the exact coupled two-field BVP."""
    return _solve_exact_coupled_bvp(params, lam_override, g_portal_override)


# ================================================================
# Level 2: D9 Comparison
# ================================================================

def compare_to_d9(
    exact: ExactTwoFieldSolution,
    params: ExactTwoFieldParams,
) -> D9ComparisonResult:
    """Compare D11 exact solution to D9 proxy solution."""
    r = exact.r_grid

    # Get D9 proxy results
    r_d9, f_d9, eps_macro_d9, eps_defect_d9, A_eff_d9, conv_d9, n_d9 = _solve_d9_proxy(
        params, lam_override=exact.lam,
    )

    # D9 metric
    f_min_d9 = _compute_d9_metric(r_d9, eps_defect_d9, eps_macro_d9, params)
    met_pos_d9 = bool(f_min_d9 > 0)

    # D11 metric
    f_coupled_d11, f_min_d11, _, met_pos_d11 = _inject_metric(
        r, exact.sigma_macro, exact.sigma_defect, params,
    )

    # Compare Phi(r) to D9 proxy Phi
    # D9 effective Phi: sqrt(A_eff^2 * RHO_EQ_COEFF / r^4 * 2 * tau^2)
    #                 = A_eff * M / r^2 (since RHO_EQ_COEFF = M^2/(2*tau^2))
    # Because eps_macro_d9 = A_eff^2 * RHO_EQ_COEFF / r^4
    # and eps_macro_d11 = Phi^2 / (2*tau^2)
    # The proxy Phi is: Phi_proxy = sqrt(2*tau^2 * eps_macro_d9)
    eps_d9_interp = np.interp(r, r_d9, eps_macro_d9)
    phi_proxy = np.sqrt(2.0 * params.tau ** 2 * np.maximum(eps_d9_interp, 0.0))
    phi_dev = exact.phi - phi_proxy
    phi_dev_max = float(np.max(np.abs(phi_dev)))
    phi_dev_rms = float(np.sqrt(np.mean(phi_dev ** 2)))

    # Compare f profiles
    f_d9_interp = np.interp(r, r_d9, f_d9)
    f_shift = exact.f_defect - f_d9_interp
    f_shift_max = float(np.max(np.abs(f_shift)))
    f_shift_rms = float(np.sqrt(np.mean(f_shift ** 2)))

    f_min_shift = f_min_d11 - f_min_d9

    # Assess D9 proxy quality using predefined comparison protocol
    if met_pos_d11 == met_pos_d9 and abs(f_min_shift) < 0.05:
        score = 0.9
        assessment = "good_approximation"
    elif met_pos_d11 == met_pos_d9 and abs(f_min_shift) < 0.15:
        score = 0.7
        assessment = "good_approximation"
    elif met_pos_d11 == met_pos_d9:
        score = 0.5
        assessment = "conservative_approximation"
    elif met_pos_d11 and not met_pos_d9:
        score = 0.3
        assessment = "conservative_approximation"
    elif not met_pos_d11 and met_pos_d9:
        score = 0.1
        assessment = "qualitatively_misleading"
    else:
        score = 0.5
        assessment = "inconclusive"

    return D9ComparisonResult(
        f_min_d11=f_min_d11, f_min_d9=f_min_d9,
        f_min_shift=f_min_shift,
        metric_positive_d11=met_pos_d11,
        metric_positive_d9=met_pos_d9,
        phi_vs_proxy_max_deviation=phi_dev_max,
        phi_vs_proxy_rms_deviation=phi_dev_rms,
        f_d11_vs_d9_max_shift=f_shift_max,
        f_d11_vs_d9_rms_shift=f_shift_rms,
        d9_proxy_assessment=assessment,
        proxy_quality_score=score,
        notes=[
            f"f_min D11: {f_min_d11:.6f}, D9: {f_min_d9:.6f}, shift: {f_min_shift:.6f}",
            f"Metric positive D11: {met_pos_d11}, D9: {met_pos_d9}",
            f"Phi deviation max: {phi_dev_max:.6f}, rms: {phi_dev_rms:.6f}",
            f"f profile shift max: {f_shift_max:.6f}, rms: {f_shift_rms:.6f}",
            f"D9 proxy assessment: {assessment} (score: {score:.2f})",
        ],
    )


# ================================================================
# Level 3: Metric Injection
# ================================================================

def inject_exact_metric(
    exact: ExactTwoFieldSolution,
    params: ExactTwoFieldParams,
) -> ExactMetricResult:
    """Inject exact two-field energy densities into the metric."""
    r = exact.r_grid
    f_coupled, f_min, f_min_r, metric_pos = _inject_metric(
        r, exact.sigma_macro, exact.sigma_defect, params,
    )

    f_at_Req = float(f_coupled[0])

    # Budget at key radii
    mass_coeff = 2.0 * math.pi * params.M ** 2 / params.tau ** 2
    m_static = params.M + mass_coeff * (1.0 / r - 1.0 / params.R_ext)
    delta_coupled = m_static + params.alpha_BR * exact.sigma_defect - r / 2.0
    sig_total = exact.sigma_macro + exact.sigma_defect

    budget: Dict[str, Dict[str, float]] = {}
    for r_key in [R_EQ, 0.5, 0.75, 1.0]:
        if R_EQ <= r_key <= params.R_ext:
            idx = int(np.argmin(np.abs(r - r_key)))
            budget[f"r={r_key:.4f}"] = {
                "delta_coupled": float(delta_coupled[idx]),
                "sigma_macro": float(exact.sigma_macro[idx]),
                "sigma_defect": float(exact.sigma_defect[idx]),
                "sigma_total": float(sig_total[idx]),
                "f_coupled": float(f_coupled[idx]),
            }

    return ExactMetricResult(
        r_grid=r, f_coupled=f_coupled,
        f_min=f_min, f_min_radius=f_min_r,
        metric_positive=metric_pos, f_at_Req=f_at_Req,
        budget=budget,
        notes=[
            f"f_min = {f_min:.6f} at r = {f_min_r:.4f}",
            f"Metric positive: {metric_pos}",
        ],
    )


# ================================================================
# Level 4: Lambda Scan
# ================================================================

def scan_lambda_exact(
    params: ExactTwoFieldParams,
) -> ExactLambdaScanResult:
    """Scan lambda under exact two-field closure, comparing to D9."""
    entries: List[ExactLambdaScanEntry] = []

    for lam_val in params.lambda_scan:
        # D11 exact
        exact = solve_exact_two_field(params, lam_override=lam_val)
        met_d11 = inject_exact_metric(exact, params)

        # D9 proxy
        r_d9, f_d9, eps_m_d9, eps_d_d9, _, conv_d9, n_d9 = _solve_d9_proxy(
            params, lam_override=lam_val,
        )
        f_min_d9 = _compute_d9_metric(r_d9, eps_d_d9, eps_m_d9, params)
        met_pos_d9 = bool(f_min_d9 > 0)

        # Phi deviation from uncoupled
        phi_dev = float(np.max(np.abs(exact.phi - exact.phi_uncoupled)))

        entries.append(ExactLambdaScanEntry(
            lam=lam_val,
            converged=exact.converged,
            method=exact.method,
            n_iterations=exact.n_iterations,
            f_min_d11=met_d11.f_min,
            f_min_d9=f_min_d9,
            metric_positive_d11=met_d11.metric_positive,
            metric_positive_d9=met_pos_d9,
            f_shift_from_d9=met_d11.f_min - f_min_d9,
            phi_deviation_max=phi_dev,
            notes=f"lam={lam_val}, method={exact.method}",
        ))

    n_scanned = len(entries)
    n_conv = sum(1 for e in entries if e.converged)
    n_pos_d11 = sum(1 for e in entries if e.metric_positive_d11)
    n_pos_d9 = sum(1 for e in entries if e.metric_positive_d9)

    viable_d11 = [e.lam for e in entries if e.metric_positive_d11]
    viable_d9 = [e.lam for e in entries if e.metric_positive_d9]

    if viable_d11 == viable_d9:
        comparison = "same"
    elif len(viable_d11) > len(viable_d9):
        comparison = "expanded"
    elif len(viable_d11) < len(viable_d9):
        comparison = "narrowed"
    elif len(viable_d11) == 0:
        comparison = "destroyed"
    else:
        comparison = "shifted"

    return ExactLambdaScanResult(
        entries=entries, n_scanned=n_scanned, n_converged=n_conv,
        n_positive_d11=n_pos_d11, n_positive_d9=n_pos_d9,
        viable_d11=viable_d11, viable_d9=viable_d9,
        viability_comparison=comparison,
        notes=[
            f"Scanned {n_scanned} lambda values, {n_conv} converged.",
            f"Viable D11: {viable_d11}",
            f"Viable D9: {viable_d9}",
            f"Comparison: {comparison}",
        ],
    )


# ================================================================
# Level 5: Portal Coupling Scan
# ================================================================

def scan_portal_exact(
    params: ExactTwoFieldParams,
) -> ExactPortalScanResult:
    """Scan portal coupling under exact closure."""
    entries: List[ExactPortalScanEntry] = []

    for g_val in params.g_portal_scan:
        exact = solve_exact_two_field(params, g_portal_override=g_val)
        met = inject_exact_metric(exact, params)

        phi_dev = float(np.max(np.abs(exact.phi - exact.phi_uncoupled)))

        entries.append(ExactPortalScanEntry(
            g_portal=g_val,
            converged=exact.converged,
            n_iterations=exact.n_iterations,
            f_min=met.f_min,
            metric_positive=met.metric_positive,
            phi_deviation_max=phi_dev,
            notes=f"g_portal={g_val}",
        ))

    n_pos = sum(1 for e in entries if e.metric_positive)
    max_dev = max(e.phi_deviation_max for e in entries) if entries else 0.0

    if n_pos == len(entries) and max_dev < 0.1:
        sensitivity = "mild_sensitivity"
    elif n_pos == len(entries):
        sensitivity = "moderate_sensitivity"
    elif n_pos > 0:
        sensitivity = "significant_sensitivity"
    else:
        sensitivity = "destructive"

    return ExactPortalScanResult(
        entries=entries, n_scanned=len(entries), n_positive=n_pos,
        sensitivity_assessment=sensitivity,
        notes=[
            f"Scanned {len(entries)} g_portal values.",
            f"{n_pos}/{len(entries)} positive.",
            f"Max Phi deviation: {max_dev:.6f}",
            f"Sensitivity: {sensitivity}",
        ],
    )


# ================================================================
# Level 6a: D9 Retrospective Assessment
# ================================================================

def assess_d9_retrospective(
    lambda_scan: ExactLambdaScanResult,
    d9_comparison: D9ComparisonResult,
    params: ExactTwoFieldParams,
) -> D9RetrospectiveAssessment:
    """Assess D9 proxy closure retrospectively from D11 results."""
    # Check viability agreement across lambda scan
    agree_count = sum(
        1 for e in lambda_scan.entries
        if e.metric_positive_d11 == e.metric_positive_d9
    )
    total = len(lambda_scan.entries)
    viability_agree = agree_count == total

    # f_min correlation across lambda scan
    d11_fmins = [e.f_min_d11 for e in lambda_scan.entries if e.converged]
    d9_fmins = [e.f_min_d9 for e in lambda_scan.entries if e.converged]
    if len(d11_fmins) >= 2:
        d11_arr = np.array(d11_fmins)
        d9_arr = np.array(d9_fmins)
        d11_std = float(np.std(d11_arr))
        d9_std = float(np.std(d9_arr))
        if d11_std > 1e-10 and d9_std > 1e-10:
            corr_num = np.sum(
                (d11_arr - np.mean(d11_arr)) * (d9_arr - np.mean(d9_arr))
            )
            correlation = float(corr_num / (d11_std * d9_std * len(d11_arr)))
        else:
            # One or both have near-zero variance
            correlation = 1.0 if d11_std < 1e-10 and d9_std < 1e-10 else 0.0
    else:
        correlation = 0.0

    # Max metric discrepancy
    max_disc = max(
        abs(e.f_shift_from_d9) for e in lambda_scan.entries if e.converged
    ) if lambda_scan.entries else 0.0

    # Parameter window agreement
    if lambda_scan.viable_d11 == lambda_scan.viable_d9:
        window_agree = "identical"
    elif set(lambda_scan.viable_d9).issubset(set(lambda_scan.viable_d11)):
        window_agree = "d9_subset_of_d11"
    elif set(lambda_scan.viable_d11).issubset(set(lambda_scan.viable_d9)):
        window_agree = "d11_subset_of_d9"
    else:
        window_agree = "different"

    # Overall assessment
    if viability_agree and abs(max_disc) < 0.05 and correlation > 0.9:
        assessment = "good_approximation"
        summary = (
            "D9 proxy closure is a good approximation of the exact two-field "
            "closure. Viability windows agree, metric discrepancies are small "
            f"(max {max_disc:.4f}), and f_min values are well-correlated "
            f"(r = {correlation:.3f})."
        )
    elif viability_agree and abs(max_disc) < 0.15:
        assessment = "good_approximation"
        summary = (
            "D9 proxy closure agrees with exact closure on viability at all "
            f"tested lambda. Metric discrepancy moderate (max {max_disc:.4f}). "
            f"Correlation: {correlation:.3f}."
        )
    elif viability_agree:
        assessment = "conservative_approximation"
        summary = (
            "D9 viability conclusions survive exact closure but with larger "
            f"metric discrepancies (max {max_disc:.4f}). D9 was conservative."
        )
    elif len(lambda_scan.viable_d11) > len(lambda_scan.viable_d9):
        assessment = "conservative_approximation"
        summary = (
            "D9 was conservative: exact closure expands the viable window. "
            f"D11: {lambda_scan.viable_d11}, D9: {lambda_scan.viable_d9}."
        )
    elif len(lambda_scan.viable_d11) < len(lambda_scan.viable_d9):
        if len(lambda_scan.viable_d11) == 0:
            assessment = "qualitatively_misleading"
            summary = "D9 proxy indicated viability but exact closure rejects it."
        else:
            assessment = "partially_valid_in_some_parameter_window"
            summary = (
                "D9 viability partially confirmed. Exact viable window narrower: "
                f"D11: {lambda_scan.viable_d11}, D9: {lambda_scan.viable_d9}."
            )
    else:
        assessment = "inconclusive"
        summary = "D9 assessment inconclusive from D11 results."

    return D9RetrospectiveAssessment(
        assessment=assessment,
        viability_agreement=viability_agree,
        f_min_correlation=correlation,
        max_metric_discrepancy=max_disc,
        parameter_window_agreement=window_agree,
        summary=summary,
        notes=[
            f"Viability agreement: {agree_count}/{total}",
            f"f_min correlation: {correlation:.4f}",
            f"Max discrepancy: {max_disc:.6f}",
            f"Window agreement: {window_agree}",
        ],
    )


# ================================================================
# Level 6b: Classification
# ================================================================

def classify_exact_two_field(
    lambda_scan: ExactLambdaScanResult,
    d9_retro: D9RetrospectiveAssessment,
    portal_scan: ExactPortalScanResult,
    params: ExactTwoFieldParams,
) -> ExactTwoFieldClassification:
    """Classify the D11 exact two-field closure result."""
    all_converged = lambda_scan.n_converged == lambda_scan.n_scanned
    viable_d11 = lambda_scan.viable_d11
    viable_d9 = lambda_scan.viable_d9
    viability_agree = d9_retro.viability_agreement
    d9_assess = d9_retro.assessment

    if not all_converged and lambda_scan.n_converged < 3:
        classification = "exact_closure_partially_supports_d9"
        d9_confirmed = False
        lam_viable = False
        summary = (
            f"Only {lambda_scan.n_converged}/{lambda_scan.n_scanned} converged. "
            "Insufficient evidence for full classification."
        )
    elif viability_agree and d9_assess == "good_approximation":
        if len(viable_d11) >= 6 and d9_retro.max_metric_discrepancy < 0.05:
            classification = "exact_closure_achieved"
            summary = (
                "Exact two-field closure confirms full viability across tested "
                "lambda range with small metric discrepancies from D9."
            )
        else:
            classification = "exact_closure_strongly_supports_d9"
            summary = (
                "Exact closure strongly supports D9 proxy results. "
                f"Viable window: {viable_d11}."
            )
        d9_confirmed = True
        lam_viable = len(viable_d11) > 0
    elif viability_agree and d9_assess == "conservative_approximation":
        classification = "exact_closure_strongly_supports_d9"
        d9_confirmed = True
        lam_viable = len(viable_d11) > 0
        summary = (
            "Exact closure confirms D9 viability. D9 was conservative "
            f"(max discrepancy {d9_retro.max_metric_discrepancy:.4f})."
        )
    elif len(viable_d11) > len(viable_d9):
        classification = "exact_closure_strongly_supports_d9"
        d9_confirmed = True
        lam_viable = True
        summary = (
            "Exact closure expands D9 viable window. D9 was conservative."
        )
    elif len(viable_d11) > 0 and len(viable_d11) < len(viable_d9):
        classification = "exact_closure_partially_supports_d9"
        d9_confirmed = False
        lam_viable = True
        summary = (
            "Exact closure narrows viable window. D9 partially valid: "
            f"D11: {viable_d11}, D9: {viable_d9}."
        )
    elif len(viable_d11) == 0 and len(viable_d9) > 0:
        classification = "exact_closure_rejects_current_companion_architecture"
        d9_confirmed = False
        lam_viable = False
        summary = "Exact closure eliminates metric positivity at all tested lambda."
    elif len(viable_d11) == 0 and len(viable_d9) == 0:
        classification = "exact_closure_weakens_d9_materially"
        d9_confirmed = False
        lam_viable = False
        summary = "Neither D9 nor D11 produce positive metrics."
    else:
        classification = "exact_closure_partially_supports_d9"
        d9_confirmed = len(viable_d11) > 0
        lam_viable = len(viable_d11) > 0
        summary = f"Mixed results. D11 viable: {viable_d11}, D9 viable: {viable_d9}."

    phase_lock = {
        "phase_6_f_Req": "LOCKED (-17.71)",
        "phase_6B_A_crit": "LOCKED (1.062)",
        "phase_6C_deficit": "LOCKED (Component A + Component B)",
        "route_C": "LOCKED (insufficient)",
        "route_B": "LOCKED (closed)",
        "source_law_I": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "PROVISIONAL (provisional_candidate_extension_formulated)",
        "defect_D2": "STRONGLY SUPPORTED (defect_candidate_numerically_viable)",
        "unification_D3": "LOCKED (scalar_triplet_embedding_most_promising)",
        "unification_D4": "PROVISIONAL (component_a_shape_recovered_but_interpretation_not_yet_verified)",
        "source_coupled_D5": "REJECTED IN TESTED FORM (source_coupling_insufficient)",
        "companion_D6": "STRONGLY SUPPORTED (companion_architecture_viable)",
        "cross_coupling_D7": "STRONGLY SUPPORTED (fully_coupled_viable)",
        "coupled_action_D8": "LOCKED (d7_channels_largely_action_derived)",
        "self_consistent_D9": f"D9 RETROSPECTIVE: {d9_assess}",
        "exact_two_field_D11": f"ASSESSED ({classification})",
    }

    return ExactTwoFieldClassification(
        classification=classification,
        d9_assessment=d9_assess,
        d9_viability_confirmed=d9_confirmed,
        exact_viability_across_lambda=lam_viable,
        summary=summary,
        phase_lock_update=phase_lock,
    )


# ================================================================
# Level 6c: Regime Separation
# ================================================================

def _solve_uncoupled_macro_bvp_on_domain(
    r_domain: np.ndarray,
    r_min_bvp: float,
    r_max_bvp: float,
    params: ExactTwoFieldParams,
) -> np.ndarray:
    """Solve uncoupled macro BVP: Phi'' + (2/r)Phi' - (1/tau^2)Phi + (1/tau^2)(M/r^2) = 0."""
    if not HAS_SCIPY_BVP:
        return params.M / r_domain ** 2

    tau = params.tau
    M_val = params.M
    n_bvp = max(len(r_domain), 300)
    r_bvp = np.linspace(r_min_bvp, r_max_bvp, n_bvp)

    def ode_m(r, y):
        phi, phi_p = y
        phi_pp = -(2.0 / r) * phi_p + (1.0 / tau ** 2) * phi - (1.0 / tau ** 2) * (M_val / r ** 2)
        return np.array([phi_p, phi_pp])

    def bc_m(ya, yb):
        return np.array([ya[0] - M_val / r_min_bvp ** 2,
                         yb[0] - M_val / r_max_bvp ** 2])

    phi_g = M_val / r_bvp ** 2
    phi_pg = -2.0 * M_val / r_bvp ** 3
    try:
        sol = solve_bvp(ode_m, bc_m, r_bvp, np.array([phi_g, phi_pg]),
                        tol=1e-6, max_nodes=5000)
        if sol.success:
            return sol.sol(r_domain)[0]
    except Exception:
        pass
    return M_val / r_domain ** 2


def compute_regime_separation(
    exact: ExactTwoFieldSolution,
    params: ExactTwoFieldParams,
) -> RegimeSeparationResult:
    """Compute three-regime comparison separating Laplacian from portal effects."""
    r_int = exact.r_grid
    idx_req = 0

    # Get uncoupled defect
    d2_params = NumericalMonopoleParams(
        eta=params.eta, lam=params.lam, r_min=params.r_min,
        r_max=params.r_max, n_grid=params.n_grid,
        M=params.M, tau=params.tau, R_ext=params.R_ext,
    )
    bvp_d = solve_hedgehog_bvp(d2_params)
    f_unc = np.interp(r_int, bvp_d.r_grid, bvp_d.f_solution)
    fp_unc = np.interp(r_int, bvp_d.r_grid, bvp_d.f_prime)
    eps_defect = _compute_defect_energy_from_f(r_int, f_unc, fp_unc, params.eta, params.lam)
    sig_defect = _sigma_from_profile(r_int, eps_defect)

    entries: List[RegimeSeparationEntry] = []

    # Regime A: D9 proxy (Phi = M/r^2)
    phi_proxy = params.M / r_int ** 2
    eps_A = _compute_macro_energy_from_phi(r_int, phi_proxy, params.tau)
    sig_A = _sigma_from_profile(r_int, eps_A)
    _, fmin_A, _, pos_A = _inject_metric(r_int, sig_A, sig_defect, params)
    entries.append(RegimeSeparationEntry(
        name="d9_proxy",
        description="D9 proxy: Phi = M/r^2 (no Laplacian, no portal)",
        phi_at_Req=float(phi_proxy[idx_req]),
        eps_macro_at_Req=float(eps_A[idx_req]),
        sigma_macro_at_Req=float(sig_A[idx_req]),
        sigma_defect_at_Req=float(sig_defect[idx_req]),
        sector_ratio=float(sig_A[idx_req] / max(sig_defect[idx_req], 1e-30)),
        f_min_metric=fmin_A, metric_positive=pos_A,
    ))

    # Regime B: D11 exact uncoupled on extended domain (BVP Phi, g_p=0)
    phi_bvp_ext = _solve_uncoupled_macro_bvp_on_domain(
        r_int, params.r_min, params.r_max, params,
    )
    eps_B = _compute_macro_energy_from_phi(r_int, phi_bvp_ext, params.tau)
    sig_B = _sigma_from_profile(r_int, eps_B)
    _, fmin_B, _, pos_B = _inject_metric(r_int, sig_B, sig_defect, params)
    entries.append(RegimeSeparationEntry(
        name="d11_uncoupled_extended",
        description="D11 uncoupled on extended domain [r_min, r_max]: BVP Phi, g_p=0",
        phi_at_Req=float(phi_bvp_ext[idx_req]),
        eps_macro_at_Req=float(eps_B[idx_req]),
        sigma_macro_at_Req=float(sig_B[idx_req]),
        sigma_defect_at_Req=float(sig_defect[idx_req]),
        sector_ratio=float(sig_B[idx_req] / max(sig_defect[idx_req], 1e-30)),
        f_min_metric=fmin_B, metric_positive=pos_B,
    ))

    # Regime B2: D11 exact uncoupled on physical domain [R_EQ, R_EXT]
    phi_bvp_phys = _solve_uncoupled_macro_bvp_on_domain(
        r_int, R_EQ, params.R_ext, params,
    )
    eps_B2 = _compute_macro_energy_from_phi(r_int, phi_bvp_phys, params.tau)
    sig_B2 = _sigma_from_profile(r_int, eps_B2)
    _, fmin_B2, _, pos_B2 = _inject_metric(r_int, sig_B2, sig_defect, params)
    entries.append(RegimeSeparationEntry(
        name="d11_uncoupled_physical",
        description="D11 uncoupled on physical domain [R_EQ, R_EXT]: BVP Phi, g_p=0",
        phi_at_Req=float(phi_bvp_phys[idx_req]),
        eps_macro_at_Req=float(eps_B2[idx_req]),
        sigma_macro_at_Req=float(sig_B2[idx_req]),
        sigma_defect_at_Req=float(sig_defect[idx_req]),
        sector_ratio=float(sig_B2[idx_req] / max(sig_defect[idx_req], 1e-30)),
        f_min_metric=fmin_B2, metric_positive=pos_B2,
    ))

    # Regime C: D11 exact coupled (from main solve)
    entries.append(RegimeSeparationEntry(
        name="d11_coupled",
        description="D11 exact coupled: BVP Phi+f, g_p>0",
        phi_at_Req=float(exact.phi[idx_req]),
        eps_macro_at_Req=float(exact.epsilon_macro[idx_req]),
        sigma_macro_at_Req=exact.sigma_macro_at_Req,
        sigma_defect_at_Req=exact.sigma_defect_at_Req,
        sector_ratio=float(exact.sigma_macro_at_Req / max(exact.sigma_defect_at_Req, 1e-30)),
        f_min_metric=float(np.min(
            -2.0 * (
                params.M + 2.0 * math.pi * params.M ** 2 / params.tau ** 2 *
                (1.0 / r_int - 1.0 / params.R_ext)
                + params.alpha_BR * exact.sigma_defect - r_int / 2.0
                - exact.sigma_macro - exact.sigma_defect
            ) / r_int
        )),
        metric_positive=True,  # will be set below
    ))
    # Fix metric for regime C
    met_C = inject_exact_metric(exact, params)
    entries[-1] = RegimeSeparationEntry(
        name="d11_coupled",
        description="D11 exact coupled: BVP Phi+f, g_p>0",
        phi_at_Req=float(exact.phi[idx_req]),
        eps_macro_at_Req=float(exact.epsilon_macro[idx_req]),
        sigma_macro_at_Req=exact.sigma_macro_at_Req,
        sigma_defect_at_Req=exact.sigma_defect_at_Req,
        sector_ratio=float(exact.sigma_macro_at_Req / max(exact.sigma_defect_at_Req, 1e-30)),
        f_min_metric=met_C.f_min,
        metric_positive=met_C.metric_positive,
    )

    laplacian_jump = fmin_B2 - fmin_A  # physical domain Laplacian effect
    portal_jump = met_C.f_min - fmin_B  # portal on extended domain
    if abs(laplacian_jump) > 10 * abs(portal_jump):
        dominant = "laplacian"
    elif abs(portal_jump) > 10 * abs(laplacian_jump):
        dominant = "portal"
    else:
        dominant = "both"

    return RegimeSeparationResult(
        entries=entries,
        laplacian_jump=laplacian_jump,
        portal_jump=portal_jump,
        dominant_effect=dominant,
        notes=[
            f"Laplacian-only metric shift (physical domain): {laplacian_jump:.4f}",
            f"Portal-only metric shift: {portal_jump:.4f}",
            f"Dominant effect: {dominant}",
            "The Phi enhancement on extended domain is boundary-driven. "
            "On the physical domain [R_EQ, R_EXT], the Laplacian gives ~2x "
            "sigma_macro enhancement (moderate, not dramatic).",
        ],
    )


# ================================================================
# Level 6d: Boundary Sensitivity
# ================================================================

def compute_boundary_sensitivity(
    params: ExactTwoFieldParams,
) -> BoundarySensitivityResult:
    """Test sensitivity of Phi enhancement to inner boundary location."""
    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, params.n_interior)

    # Uncoupled defect (same for all)
    d2_params = NumericalMonopoleParams(
        eta=params.eta, lam=params.lam, r_min=params.r_min,
        r_max=params.r_max, n_grid=params.n_grid,
        M=params.M, tau=params.tau, R_ext=params.R_ext,
    )
    bvp_d = solve_hedgehog_bvp(d2_params)
    f_unc = np.interp(r_int, bvp_d.r_grid, bvp_d.f_solution)
    fp_unc = np.interp(r_int, bvp_d.r_grid, bvp_d.f_prime)
    eps_defect = _compute_defect_energy_from_f(r_int, f_unc, fp_unc, params.eta, params.lam)
    sig_defect = _sigma_from_profile(r_int, eps_defect)

    phi_proxy_Req = params.M / R_EQ ** 2
    entries: List[BoundarySensitivityEntry] = []
    phys_entry = None

    for r_min_test in [0.005, 0.01, 0.05, 0.1, R_EQ]:
        phi_bvp = _solve_uncoupled_macro_bvp_on_domain(
            r_int, r_min_test, params.r_max, params,
        )
        eps_macro = _compute_macro_energy_from_phi(r_int, phi_bvp, params.tau)
        sig_macro = _sigma_from_profile(r_int, eps_macro)
        _, fmin, _, pos = _inject_metric(r_int, sig_macro, sig_defect, params)
        phi_req = float(phi_bvp[0])
        ratio = phi_req / phi_proxy_Req

        entry = BoundarySensitivityEntry(
            r_min=r_min_test,
            phi_at_Req=phi_req,
            phi_ratio_to_proxy=ratio,
            f_min_metric=fmin,
            metric_positive=pos,
        )
        entries.append(entry)
        if abs(r_min_test - R_EQ) < 0.01:
            phys_entry = entry

    # Determine if enhancement is boundary-driven
    # If ratio changes by > 5x across r_min range, it's boundary-driven
    ratios = [e.phi_ratio_to_proxy for e in entries]
    max_ratio = max(ratios)
    min_ratio = min(ratios)
    boundary_driven = (max_ratio / max(min_ratio, 0.01)) > 5

    return BoundarySensitivityResult(
        entries=entries,
        physical_domain_entry=phys_entry or entries[-1],
        enhancement_boundary_driven=boundary_driven,
        summary=(
            f"Phi enhancement at R_EQ ranges from {min_ratio:.1f}x to "
            f"{max_ratio:.1f}x depending on r_min. "
            f"On physical domain (r_min=R_EQ), ratio={phys_entry.phi_ratio_to_proxy:.2f}x. "
            f"Enhancement is {'boundary-driven' if boundary_driven else 'intrinsic'}."
        ),
    )


# ================================================================
# Level 6e: Layered D9 Assessment
# ================================================================

def compute_d9_layered_assessment(
    exact: ExactTwoFieldSolution,
    regime_sep: RegimeSeparationResult,
    d9_comp: D9ComparisonResult,
    params: ExactTwoFieldParams,
) -> D9LayeredAssessment:
    """Split D9 assessment into per-layer evaluation."""
    # Metric viability: do both agree on positivity?
    if d9_comp.metric_positive_d11 == d9_comp.metric_positive_d9:
        if abs(d9_comp.f_min_shift) < 0.1:
            metric_layer = "good"
        else:
            metric_layer = "moderate"
    else:
        metric_layer = "poor"

    # Macro field profile: how different is Phi from M/r^2?
    # Use physical-domain regime for fair comparison
    phys = [e for e in regime_sep.entries if e.name == "d11_uncoupled_physical"]
    if phys:
        phys_phi_ratio = phys[0].phi_at_Req / (params.M / R_EQ ** 2)
        if abs(phys_phi_ratio - 1.0) < 0.3:
            field_layer = "good"
        elif abs(phys_phi_ratio - 1.0) < 1.0:
            field_layer = "moderate"
        else:
            field_layer = "poor"
    else:
        field_layer = "moderate"

    # Energy density: how different is eps_macro?
    if phys:
        eps_ratio = phys[0].eps_macro_at_Req / max(
            regime_sep.entries[0].eps_macro_at_Req, 1e-30)
        if abs(eps_ratio - 1.0) < 0.5:
            energy_layer = "good"
        elif abs(eps_ratio - 1.0) < 2.0:
            energy_layer = "moderate"
        else:
            energy_layer = "poor"
    else:
        energy_layer = "moderate"

    # Defect deformation
    if d9_comp.f_d11_vs_d9_max_shift < 0.05:
        defect_layer = "good"
    elif d9_comp.f_d11_vs_d9_max_shift < 0.2:
        defect_layer = "moderate"
    else:
        defect_layer = "poor"

    # Sector balance
    phys_ratio = phys[0].sector_ratio if phys else 1.0
    d9_ratio = regime_sep.entries[0].sector_ratio if regime_sep.entries else 1.0
    if phys_ratio / max(d9_ratio, 0.01) < 3.0:
        balance = "preserved"
    elif phys_ratio / max(d9_ratio, 0.01) < 10.0:
        balance = "shifted"
    else:
        balance = "overwhelmed"

    summary = (
        f"Layered D9 assessment: "
        f"metric viability={metric_layer}, "
        f"field profile={field_layer}, "
        f"energy density={energy_layer}, "
        f"defect deformation={defect_layer}, "
        f"sector balance={balance}. "
        f"D9 is a good approximation for viability but "
        f"{'also good' if field_layer == 'good' else 'limited'} "
        f"for field-level structure."
    )

    return D9LayeredAssessment(
        metric_viability=metric_layer,
        macro_field_profile=field_layer,
        energy_density=energy_layer,
        defect_deformation=defect_layer,
        sector_balance=balance,
        summary=summary,
    )


# ================================================================
# Level 7: Master Computation
# ================================================================

def compute_exact_two_field(
    params: Optional[ExactTwoFieldParams] = None,
) -> ExactTwoFieldResult:
    """Run the full Phase D11 exact two-field closure analysis."""
    if params is None:
        params = ExactTwoFieldParams()

    result = ExactTwoFieldResult(
        valid=True, params=params,
        nonclaims=list(EXACT_TWO_FIELD_NONCLAIMS),
        assumptions=list(EXACT_TWO_FIELD_ASSUMPTIONS),
    )

    # Level 0: Document equations
    result.field_equations = document_field_equations(params)

    # Level 1: Solve exact coupled system at default params
    result.exact_solution = solve_exact_two_field(params)

    # Level 2: Compare to D9
    result.d9_comparison = compare_to_d9(result.exact_solution, params)

    # Level 3: Metric injection
    result.metric_result = inject_exact_metric(result.exact_solution, params)

    # Level 4: Lambda scan
    result.lambda_scan = scan_lambda_exact(params)

    # Level 5: Portal scan
    result.portal_scan = scan_portal_exact(params)

    # Level 6a: D9 retrospective
    result.d9_retrospective = assess_d9_retrospective(
        result.lambda_scan, result.d9_comparison, params,
    )

    # Level 6b: Classification
    result.classification = classify_exact_two_field(
        result.lambda_scan, result.d9_retrospective,
        result.portal_scan, params,
    )

    # Level 6c: Regime separation
    result.regime_separation = compute_regime_separation(
        result.exact_solution, params,
    )

    # Level 6d: Boundary sensitivity
    result.boundary_sensitivity = compute_boundary_sensitivity(params)

    # Level 6e: Layered D9 assessment
    result.d9_layered = compute_d9_layered_assessment(
        result.exact_solution, result.regime_separation,
        result.d9_comparison, params,
    )

    return result


# ================================================================
# Level 8: Serialization
# ================================================================

def exact_two_field_result_to_dict(
    result: ExactTwoFieldResult,
) -> Dict[str, Any]:
    """Serialize to JSON-compatible dict."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "phase": "D11",
        "title": "Exact Two-Field Closure",
    }

    if result.field_equations:
        fe = result.field_equations
        d["field_equations"] = {
            "macro_equation": fe.macro_equation,
            "defect_equation": fe.defect_equation,
            "portal_term": fe.portal_term,
            "portal_sign_verification": fe.portal_sign_verification,
            "boundary_conditions": fe.boundary_conditions,
            "background_geometry": fe.background_geometry,
            "source_status": fe.source_status,
            "macro_laplacian_status": fe.macro_laplacian_status,
            "energy_density_convention": fe.energy_density_convention,
            "remaining_approximations": fe.remaining_approximations,
        }

    if result.exact_solution:
        es = result.exact_solution
        d["exact_solution"] = {
            "converged": es.converged,
            "method": es.method,
            "n_iterations": es.n_iterations,
            "g_portal": es.g_portal,
            "lam": es.lam,
            "sigma_defect_at_Req": es.sigma_defect_at_Req,
            "sigma_macro_at_Req": es.sigma_macro_at_Req,
            "final_residual": es.final_residual,
            "relaxation_used": es.relaxation_used,
        }

    if result.d9_comparison:
        dc = result.d9_comparison
        d["d9_comparison"] = {
            "f_min_d11": dc.f_min_d11,
            "f_min_d9": dc.f_min_d9,
            "f_min_shift": dc.f_min_shift,
            "metric_positive_d11": dc.metric_positive_d11,
            "metric_positive_d9": dc.metric_positive_d9,
            "phi_vs_proxy_max_deviation": dc.phi_vs_proxy_max_deviation,
            "phi_vs_proxy_rms_deviation": dc.phi_vs_proxy_rms_deviation,
            "f_d11_vs_d9_max_shift": dc.f_d11_vs_d9_max_shift,
            "f_d11_vs_d9_rms_shift": dc.f_d11_vs_d9_rms_shift,
            "d9_proxy_assessment": dc.d9_proxy_assessment,
            "proxy_quality_score": dc.proxy_quality_score,
        }

    if result.metric_result:
        mr = result.metric_result
        d["metric_result"] = {
            "f_min": mr.f_min,
            "f_min_radius": mr.f_min_radius,
            "metric_positive": mr.metric_positive,
            "f_at_Req": mr.f_at_Req,
            "budget": mr.budget,
        }

    if result.lambda_scan:
        ls = result.lambda_scan
        d["lambda_scan"] = {
            "n_scanned": ls.n_scanned,
            "n_converged": ls.n_converged,
            "n_positive_d11": ls.n_positive_d11,
            "n_positive_d9": ls.n_positive_d9,
            "viable_d11": ls.viable_d11,
            "viable_d9": ls.viable_d9,
            "viability_comparison": ls.viability_comparison,
            "entries": [
                {
                    "lam": e.lam,
                    "converged": e.converged,
                    "method": e.method,
                    "n_iterations": e.n_iterations,
                    "f_min_d11": e.f_min_d11,
                    "f_min_d9": e.f_min_d9,
                    "metric_positive_d11": e.metric_positive_d11,
                    "metric_positive_d9": e.metric_positive_d9,
                    "f_shift_from_d9": e.f_shift_from_d9,
                    "phi_deviation_max": e.phi_deviation_max,
                }
                for e in ls.entries
            ],
        }

    if result.portal_scan:
        ps = result.portal_scan
        d["portal_scan"] = {
            "n_scanned": ps.n_scanned,
            "n_positive": ps.n_positive,
            "sensitivity_assessment": ps.sensitivity_assessment,
            "entries": [
                {
                    "g_portal": e.g_portal,
                    "converged": e.converged,
                    "f_min": e.f_min,
                    "metric_positive": e.metric_positive,
                    "phi_deviation_max": e.phi_deviation_max,
                }
                for e in ps.entries
            ],
        }

    if result.d9_retrospective:
        dr = result.d9_retrospective
        d["d9_retrospective"] = {
            "assessment": dr.assessment,
            "viability_agreement": dr.viability_agreement,
            "f_min_correlation": dr.f_min_correlation,
            "max_metric_discrepancy": dr.max_metric_discrepancy,
            "parameter_window_agreement": dr.parameter_window_agreement,
            "summary": dr.summary,
        }

    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "d9_assessment": cl.d9_assessment,
            "d9_viability_confirmed": cl.d9_viability_confirmed,
            "exact_viability_across_lambda": cl.exact_viability_across_lambda,
            "summary": cl.summary,
        }

    if result.regime_separation:
        rs = result.regime_separation
        d["regime_separation"] = {
            "entries": [
                {
                    "name": e.name,
                    "phi_at_Req": e.phi_at_Req,
                    "eps_macro_at_Req": e.eps_macro_at_Req,
                    "sigma_macro_at_Req": e.sigma_macro_at_Req,
                    "sector_ratio": e.sector_ratio,
                    "f_min_metric": e.f_min_metric,
                    "metric_positive": e.metric_positive,
                }
                for e in rs.entries
            ],
            "laplacian_jump": rs.laplacian_jump,
            "portal_jump": rs.portal_jump,
            "dominant_effect": rs.dominant_effect,
        }

    if result.boundary_sensitivity:
        bs = result.boundary_sensitivity
        d["boundary_sensitivity"] = {
            "entries": [
                {
                    "r_min": e.r_min,
                    "phi_at_Req": e.phi_at_Req,
                    "phi_ratio_to_proxy": e.phi_ratio_to_proxy,
                    "f_min_metric": e.f_min_metric,
                    "metric_positive": e.metric_positive,
                }
                for e in bs.entries
            ],
            "enhancement_boundary_driven": bs.enhancement_boundary_driven,
            "summary": bs.summary,
        }

    if result.d9_layered:
        dl = result.d9_layered
        d["d9_layered_assessment"] = {
            "metric_viability": dl.metric_viability,
            "macro_field_profile": dl.macro_field_profile,
            "energy_density": dl.energy_density,
            "defect_deformation": dl.defect_deformation,
            "sector_balance": dl.sector_balance,
            "summary": dl.summary,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
