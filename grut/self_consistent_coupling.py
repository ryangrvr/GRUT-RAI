"""Phase D9 — Self-Consistent Coupled Profile Integration.

Tests whether the D7 metric viability survives when the defect profile is
allowed to deform under coupling, rather than being held frozen on Schwarzschild.

SCOPE: D9 is a self-consistent profile iteration under a REDUCED CLOSURE.
The portal feedback uses a macro-amplitude proxy inferred from the D7/D8
effective Component A profile, rather than a separately solved macro field
variable Phi(r).  D9 therefore tests self-consistency under a field-amplitude
proxy closure, NOT the fully exact two-field Euler–Lagrange system.

MACRO-FIELD PROXY CLOSURE: The D8 portal term g_p Phi^2 |vec_Phi|^2 enters
the defect EL equation as +2 g_p Phi_bg^2 f, where Phi_bg is the macro
background.  In D9, Phi_bg^2 is approximated by the effective macro amplitude:
    V_proxy(r) = A_eff(r)^2 * RHO_EQ_COEFF / (eta^2 * r^4)
This is an amplitude proxy, not the exact field variable.

PORTAL SIGN (from D8): The portal term enters with POSITIVE sign in the
defect EL equation.  This is STABILIZING: the portal acts as an additional
effective mass for the defect, pushing f(r) toward vacuum (f→1) faster,
slightly tightening the core.

UNDER-RELAXATION: Picard iteration with f_next = (1-omega)*f_old + omega*f_new.
Default omega=0.5; fallback to 0.3 or 0.2 if oscillation detected.

LOCKED INHERITANCE:
  D6: companion_architecture_viable (additive, A=1 + defect, lambda >= 25)
  D7: fully_coupled_viable (two effective channels, viable all 6 lambda)
  D8: d7_channels_largely_action_derived (portal + GR)

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
# Constants
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

# D9-specific
MAX_ITERATIONS_DEFAULT = 20
CONVERGENCE_TOL_DEFAULT = 1e-4
RELAXATION_FACTOR_DEFAULT = 0.5
RELAXATION_FALLBACK = [0.3, 0.2]
G_PORTAL_DEFAULT = 1.0
G_PORTAL_SCAN_VALUES = [0.0, 0.1, 0.5, 1.0]
LAMBDA_SCAN_VALUES = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]

DEFORMATION_THRESHOLDS = {
    "negligible": 0.01,   # max |delta_f| < 1%
    "moderate": 0.05,     # max |delta_f| < 5%
    "significant": 0.10,  # max |delta_f| < 10%
}

CLASSIFICATION_OPTIONS = [
    "self_consistent_coupling_viable",
    "viability_window_shifted_but_survives",
    "partially_viable_under_self_consistency",
    "destroyed_by_self_consistency",
    "unresolved_solver_artifacts",
]


# ================================================================
# Assumptions
# ================================================================

SELF_CONSISTENT_ASSUMPTIONS = [
    "1. Macro-field proxy closure: portal feedback uses A_eff(r)^2 as proxy "
    "for Phi_bg^2, NOT a separately solved macro field variable.",

    "2. Portal sign is POSITIVE (stabilizing): from D8 action derivation, "
    "+2 g_p Phi^2 vec_Phi enters defect EL, tightening the core.",

    "3. Portal normalization: V_proxy(r) = A_eff(r)^2 * RHO_EQ_COEFF / "
    "(eta^2 * r^4), absorbing 2*g_p into g_portal.",

    "4. Under-relaxed Picard iteration: f_next = (1-omega)*f_old + omega*f_new, "
    "omega=0.5 default, fallback to 0.3/0.2 if oscillation detected.",

    "5. Convergence criterion: ||f_next - f_old||_inf < 1e-4.",

    "6. Frozen D7 profile used as initial guess and comparison baseline.",

    "7. Gravitational back-reaction (alpha_BR=1) and source amplification "
    "(beta_XR=1) inherited from D7 unit benchmark.",

    "8. Lambda scan inherited from D6/D7: [5, 10, 25, 50, 100, 200].",

    "9. Portal strength g_portal scanned at [0, 0.1, 0.5, 1.0] for sensitivity.",

    "10. D9 tests self-consistency under reduced closure, NOT the fully exact "
    "two-field Euler–Lagrange system.",
]

SELF_CONSISTENT_NONCLAIMS = [
    "1. This phase does NOT prove final theory closure.",

    "2. A surviving self-consistent solution strongly upgrades confidence but "
    "remains within the tested framework.",

    "3. A failure would downgrade D7 from structural viability to stress-test "
    "viability, not erase its value.",

    "4. The macro-field proxy closure is a significant approximation. The "
    "fully exact two-field solution is not computed.",

    "5. Portal coupling g_portal is scanned, not predicted from first principles.",

    "6. Under-relaxation is a numerical technique, not physical content.",

    "7. Convergence of the Picard iteration does not guarantee uniqueness.",

    "8. Profile deformation diagnostics are relative to the frozen baseline.",

    "9. This phase does NOT justify metaphysical or observer-based interpretation.",

    "10. Classification is within the D9 numerical framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class SelfConsistentParams:
    """Parameters for Phase D9."""
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
class CoupledSolverDefinition:
    """Level 0: Documents the self-consistent solver."""
    iteration_scheme: str
    d8_action_reference: str
    modified_ode: str
    convergence_criterion: str
    proxy_closure_statement: str
    sign_analysis: str
    under_relaxation_scheme: str
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledProfileSolution:
    """Level 1: Self-consistent coupled solution."""
    converged: bool
    n_iterations: int
    g_portal: float
    lam: float
    r_grid: np.ndarray
    # Defect profile (self-consistent)
    f_defect: np.ndarray
    f_defect_prime: np.ndarray
    epsilon_defect: np.ndarray
    sigma_defect: np.ndarray
    sigma_defect_at_Req: float
    # Coupled macro
    A_eff: np.ndarray
    A_eff_at_Req: float
    epsilon_macro: np.ndarray
    sigma_macro: np.ndarray
    sigma_macro_at_Req: float
    # Convergence
    convergence_history: List[float]
    final_residual: float
    relaxation_used: float
    notes: List[str] = field(default_factory=list)


@dataclass
class ProfileDeformationAssessment:
    """Level 2: Comparison of self-consistent vs frozen profiles."""
    f_shift_max: float
    f_shift_rms: float
    f_shift_at_Req: float
    crossover_radius_frozen: float
    crossover_radius_sc: float
    crossover_shift: float
    core_change: float    # f'(r_min) shift
    tail_change: float    # f(r_max) shift
    sigma_defect_shift: float  # relative shift at R_eq
    deformation_classification: str  # negligible, moderate, significant
    notes: List[str] = field(default_factory=list)


@dataclass
class SelfConsistentMetricResult:
    """Level 3: Metric injection with self-consistent profiles."""
    r_grid: np.ndarray
    f_coupled: np.ndarray
    f_min: float
    f_min_radius: float
    metric_positive: bool
    f_at_Req: float
    f_d7_at_Req: float
    metric_shift_from_d7: float
    budget: Dict[str, Dict[str, float]]
    notes: List[str] = field(default_factory=list)


@dataclass
class LambdaScanEntry:
    """One lambda in the self-consistent scan."""
    lam: float
    converged_frozen: bool
    converged_sc: bool
    n_iterations: int
    f_min_d7: float
    f_min_sc: float
    metric_positive_d7: bool
    metric_positive_sc: bool
    f_shift: float
    deformation_max: float
    notes: str = ""


@dataclass
class LambdaScanResult:
    """Level 4: Lambda scan comparing D7 frozen vs self-consistent."""
    entries: List[LambdaScanEntry]
    n_scanned: int
    n_converged: int
    n_positive_d7: int
    n_positive_sc: int
    viable_d7: List[float]
    viable_sc: List[float]
    threshold_shift: str
    rescue_preserved: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class PortalScanEntry:
    """One g_portal value in the sensitivity scan."""
    g_portal: float
    converged: bool
    n_iterations: int
    f_min: float
    metric_positive: bool
    deformation_max: float
    notes: str = ""


@dataclass
class PortalScanResult:
    """Level 5: Portal strength sensitivity scan."""
    entries: List[PortalScanEntry]
    n_scanned: int
    n_positive: int
    sensitivity_assessment: str
    notes: List[str] = field(default_factory=list)


@dataclass
class SelfConsistentClassification:
    """Level 6: Final D9 classification."""
    classification: str
    phase_status: str
    d7_viability_preserved: bool
    deformation_level: str
    proxy_closure_used: bool
    summary: str
    phase_lock_update: Dict[str, str]


@dataclass
class SelfConsistentResult:
    """Master result container for Phase D9."""
    valid: bool
    params: SelfConsistentParams
    solver_definition: Optional[CoupledSolverDefinition] = None
    profile_solution: Optional[CoupledProfileSolution] = None
    frozen_solution: Optional[CoupledProfileSolution] = None
    deformation: Optional[ProfileDeformationAssessment] = None
    metric_result: Optional[SelfConsistentMetricResult] = None
    lambda_scan: Optional[LambdaScanResult] = None
    portal_scan: Optional[PortalScanResult] = None
    classification: Optional[SelfConsistentClassification] = None
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


def _solve_frozen_baseline(
    params: SelfConsistentParams,
    lam_override: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, bool]:
    """Solve the standard (frozen) D2 BVP on the interior grid.

    Returns (r_int, f_defect, f_prime, epsilon_defect, converged).
    """
    lam = lam_override if lam_override is not None else params.lam

    d2_params = NumericalMonopoleParams(
        eta=params.eta, lam=lam, r_min=params.r_min, r_max=params.r_max,
        n_grid=params.n_grid, M=params.M, tau=params.tau, R_ext=params.R_ext,
    )
    bvp = solve_hedgehog_bvp(d2_params)
    energy = extract_defect_energy(bvp, d2_params)

    r_int = np.linspace(R_EQ + 1e-6, params.R_ext, params.n_interior)
    f_interp = np.interp(r_int, bvp.r_grid, bvp.f_solution)
    fp_interp = np.interp(r_int, bvp.r_grid, bvp.f_prime)
    eps_interp = np.interp(r_int, energy.r_grid, energy.total_epsilon)

    return r_int, f_interp, fp_interp, eps_interp, bvp.converged


def _compute_macro_coupled(
    r: np.ndarray,
    sigma_defect: np.ndarray,
    scalar_A: float,
    beta_XR: float,
    M: float,
    tau: float,
    R_ext: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute coupled macro: A_eff, epsilon_macro, sigma_macro."""
    rho_eq_coeff = M ** 2 / (2.0 * tau ** 2)
    m_eff = M + beta_XR * sigma_defect
    A_eff = scalar_A * m_eff / M
    eps_macro = A_eff ** 2 * rho_eq_coeff / r ** 4
    sig_macro = _sigma_from_profile(r, eps_macro)
    return A_eff, eps_macro, sig_macro


def _compute_portal_potential(
    r: np.ndarray,
    A_eff: np.ndarray,
    eta: float,
    M: float,
    tau: float,
) -> np.ndarray:
    """Compute the macro-amplitude proxy portal potential.

    V_proxy(r) = A_eff(r)^2 * RHO_EQ_COEFF / (eta^2 * r^4)

    This is the MACRO-AMPLITUDE PROXY, not the exact Phi^2 field variable.
    The sign is POSITIVE (stabilizing) per D8 derivation.
    """
    rho_eq_coeff = M ** 2 / (2.0 * tau ** 2)
    return A_eff ** 2 * rho_eq_coeff / (eta ** 2 * r ** 4)


def _solve_modified_bvp(
    params: SelfConsistentParams,
    V_portal_on_bvp_grid: Optional[np.ndarray] = None,
    lam_override: Optional[float] = None,
) -> HedgehogBVPSolution:
    """Solve the portal-modified hedgehog BVP.

    Modified ODE:
      f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) + g_portal*V_proxy(r)*f = 0

    The portal term enters with POSITIVE sign (stabilizing, from D8).
    V_portal_on_bvp_grid must be interpolated onto the BVP grid.
    """
    eta = params.eta
    lam = lam_override if lam_override is not None else params.lam
    g_portal = params.g_portal
    r_min = params.r_min
    r_max = params.r_max
    n = params.n_grid

    r_grid = np.linspace(r_min, r_max, n)

    # Interpolate V_portal onto BVP grid if provided
    if V_portal_on_bvp_grid is not None:
        V_on_grid = V_portal_on_bvp_grid
    else:
        V_on_grid = np.zeros(n)

    def ode(r_pts, y):
        f_val = y[0]
        fp = y[1]
        # Interpolate V_portal at solver evaluation points
        V_at_r = np.interp(r_pts, r_grid, V_on_grid)
        # Standard hedgehog + portal feedback (positive sign = stabilizing)
        fpp = (-(2.0 / r_pts) * fp
               + (2.0 / r_pts ** 2) * f_val
               + lam * eta ** 2 * f_val * (f_val ** 2 - 1.0)
               + g_portal * V_at_r * f_val)
        return np.array([fp, fpp])

    def bc(ya, yb):
        return np.array([ya[0] - 0.0, yb[0] - 1.0])

    # Initial guess
    delta_core = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
    f_guess = r_grid / np.sqrt(r_grid ** 2 + delta_core ** 2)
    fp_guess = delta_core ** 2 / (r_grid ** 2 + delta_core ** 2) ** 1.5
    y_guess = np.array([f_guess, fp_guess])

    if not HAS_SCIPY_BVP:
        return HedgehogBVPSolution(
            converged=False, r_grid=r_grid, f_solution=f_guess,
            f_prime=fp_guess, c1_effective=float(fp_guess[0]),
            max_residual=float("nan"), f_at_rmax=float(f_guess[-1]),
            notes=["scipy.solve_bvp not available"],
        )

    try:
        sol = solve_bvp(ode, bc, r_grid, y_guess, tol=1e-6, max_nodes=5000)
        y_sol = sol.sol(r_grid)
        return HedgehogBVPSolution(
            converged=sol.success, r_grid=r_grid,
            f_solution=y_sol[0], f_prime=y_sol[1],
            c1_effective=float(y_sol[1][0]),
            max_residual=float(sol.rms_residuals.max()) if hasattr(sol, 'rms_residuals') else 0.0,
            f_at_rmax=float(y_sol[0][-1]),
            notes=[f"Modified BVP converged: {sol.success}, g_portal={g_portal}"],
        )
    except Exception as exc:
        return HedgehogBVPSolution(
            converged=False, r_grid=r_grid, f_solution=f_guess,
            f_prime=fp_guess, c1_effective=float(fp_guess[0]),
            max_residual=float("nan"), f_at_rmax=float(f_guess[-1]),
            notes=[f"Modified BVP failed: {exc}"],
        )


def _compute_d7_frozen_metric(
    r_int: np.ndarray,
    eps_defect: np.ndarray,
    params: SelfConsistentParams,
) -> float:
    """Compute D7-frozen f_min for comparison."""
    sig_defect = _sigma_from_profile(r_int, eps_defect)
    A_eff, eps_macro, sig_macro = _compute_macro_coupled(
        r_int, sig_defect, params.scalar_A, params.beta_XR,
        params.M, params.tau, params.R_ext,
    )
    sig_total = sig_macro + sig_defect
    mass_coeff = 2.0 * math.pi * params.M ** 2 / params.tau ** 2
    m_static = params.M + mass_coeff * (1.0 / r_int - 1.0 / params.R_ext)
    delta_coupled = m_static + params.alpha_BR * sig_defect - r_int / 2.0
    f_coupled = -2.0 * (delta_coupled - sig_total) / r_int
    return float(np.min(f_coupled))


def _find_crossover_radius(
    r: np.ndarray,
    sig_macro: np.ndarray,
    sig_defect: np.ndarray,
) -> float:
    """Find radius where defect Sigma overtakes macro Sigma."""
    diff = sig_defect - sig_macro
    # Find first crossing from negative to positive (or vice versa)
    for i in range(len(diff) - 1):
        if diff[i] * diff[i + 1] < 0:
            # Linear interpolation
            frac = -diff[i] / (diff[i + 1] - diff[i])
            return float(r[i] + frac * (r[i + 1] - r[i]))
    # No crossing found
    return float(r[-1])


# ================================================================
# Level 0: Coupled Solver Definition
# ================================================================

def define_coupled_solver(
    params: SelfConsistentParams,
) -> CoupledSolverDefinition:
    """Document the self-consistent solver configuration."""
    return CoupledSolverDefinition(
        iteration_scheme=(
            "Under-relaxed Picard iteration: solve defect BVP with portal "
            "feedback, update macro profiles, iterate until convergence. "
            "f_next = (1-omega)*f_old + omega*f_new."
        ),
        d8_action_reference=(
            "D8 portal term: S_portal = integral sqrt(-g) g_p Phi^2 |vec_Phi|^2. "
            "Enters defect EL as +2 g_p Phi_bg^2 f (positive = stabilizing)."
        ),
        modified_ode=(
            "f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) "
            "+ g_portal * V_proxy(r) * f = 0"
        ),
        convergence_criterion=f"||f_next - f_old||_inf < {params.convergence_tol}",
        proxy_closure_statement=(
            "MACRO-FIELD PROXY CLOSURE: Portal feedback uses A_eff(r)^2 as "
            "proxy for Phi_bg^2, NOT a separately solved macro field variable. "
            "D9 tests self-consistency under a reduced closure, not the fully "
            "exact two-field Euler–Lagrange system."
        ),
        sign_analysis=(
            "The portal term enters the defect EL with POSITIVE sign "
            "(stabilizing). From D8: +2 g_p Phi^2 vec_Phi acts as effective "
            "mass increase for the defect field, pushing f(r) toward vacuum "
            "(f→1) faster. g_portal > 0 gives constructive tightening of "
            "the defect core. The normalization absorbs 2*g_p into g_portal "
            "and uses the macro amplitude proxy for Phi_bg^2."
        ),
        under_relaxation_scheme=(
            f"omega = {params.relaxation_factor} (default). "
            f"Fallback: {RELAXATION_FALLBACK} if oscillation detected. "
            "Prevents false convergence failure from Picard stiffness."
        ),
        notes=[
            "D9 relaxes D7's defect-shape freezing approximation.",
            "Initial guess: frozen D7 profile (standard D2 BVP solution).",
            f"Max iterations: {params.max_iterations}.",
        ],
    )


# ================================================================
# Level 1: Self-Consistent Solver
# ================================================================

def solve_self_consistent(
    params: SelfConsistentParams,
    lam_override: Optional[float] = None,
) -> CoupledProfileSolution:
    """Solve the self-consistent coupled system via Picard iteration.

    1. Start with frozen D2 defect profile
    2. Compute coupled macro + portal potential
    3. Re-solve defect BVP with portal feedback
    4. Under-relax and check convergence
    5. Iterate
    """
    lam = lam_override if lam_override is not None else params.lam

    # Step 0: Solve frozen baseline
    r_int, f_frozen, fp_frozen, eps_frozen, conv_frozen = _solve_frozen_baseline(
        params, lam_override=lam,
    )
    sig_defect_frozen = _sigma_from_profile(r_int, eps_frozen)

    # If g_portal == 0: return frozen result directly (D7 recovery)
    if abs(params.g_portal) < 1e-12:
        A_eff, eps_macro, sig_macro = _compute_macro_coupled(
            r_int, sig_defect_frozen, params.scalar_A, params.beta_XR,
            params.M, params.tau, params.R_ext,
        )
        return CoupledProfileSolution(
            converged=conv_frozen, n_iterations=0, g_portal=0.0, lam=lam,
            r_grid=r_int, f_defect=f_frozen, f_defect_prime=fp_frozen,
            epsilon_defect=eps_frozen, sigma_defect=sig_defect_frozen,
            sigma_defect_at_Req=float(sig_defect_frozen[0]),
            A_eff=A_eff, A_eff_at_Req=float(A_eff[0]),
            epsilon_macro=eps_macro, sigma_macro=sig_macro,
            sigma_macro_at_Req=float(sig_macro[0]),
            convergence_history=[0.0], final_residual=0.0,
            relaxation_used=params.relaxation_factor,
            notes=["g_portal=0: D7 frozen result recovered exactly."],
        )

    # Iteration loop
    f_current = f_frozen.copy()
    fp_current = fp_frozen.copy()
    eps_current = eps_frozen.copy()
    omega = params.relaxation_factor
    history: List[float] = []
    converged = False
    n_iter = 0

    for iteration in range(params.max_iterations):
        n_iter = iteration + 1

        # Step 1: Compute macro from current defect
        sig_defect = _sigma_from_profile(r_int, eps_current)
        A_eff, eps_macro, sig_macro = _compute_macro_coupled(
            r_int, sig_defect, params.scalar_A, params.beta_XR,
            params.M, params.tau, params.R_ext,
        )

        # Step 2: Compute portal potential (macro-amplitude proxy)
        V_portal_int = _compute_portal_potential(
            r_int, A_eff, params.eta, params.M, params.tau,
        )

        # Step 3: Interpolate V_portal onto BVP grid and solve modified BVP
        bvp_r = np.linspace(params.r_min, params.r_max, params.n_grid)
        V_portal_bvp = np.interp(bvp_r, r_int, V_portal_int)
        # Extrapolate: set to zero outside interior grid
        V_portal_bvp[bvp_r < r_int[0]] = V_portal_int[0]
        V_portal_bvp[bvp_r > r_int[-1]] = 0.0

        bvp_result = _solve_modified_bvp(params, V_portal_bvp, lam_override=lam)

        if not bvp_result.converged:
            # Try with reduced relaxation
            if omega > RELAXATION_FALLBACK[-1]:
                omega = RELAXATION_FALLBACK[0] if omega > RELAXATION_FALLBACK[0] else RELAXATION_FALLBACK[-1]
                history.append(float("nan"))
                continue
            else:
                history.append(float("nan"))
                break

        # Interpolate BVP solution onto interior grid
        f_new = np.interp(r_int, bvp_result.r_grid, bvp_result.f_solution)
        fp_new = np.interp(r_int, bvp_result.r_grid, bvp_result.f_prime)

        # Step 4: Under-relax
        f_next = (1.0 - omega) * f_current + omega * f_new
        fp_next = (1.0 - omega) * fp_current + omega * fp_new

        # Check convergence
        residual = float(np.max(np.abs(f_next - f_current)))
        history.append(residual)

        # Detect oscillation: if residual increased twice in a row, reduce omega
        if len(history) >= 3 and history[-1] > history[-2] > history[-3]:
            if omega > RELAXATION_FALLBACK[-1]:
                omega = max(omega * 0.7, RELAXATION_FALLBACK[-1])

        f_current = f_next
        fp_current = fp_next

        # Recompute energy from current profile
        # 3-term energy: kinetic + angular + potential
        eps_kinetic = 0.5 * params.eta ** 2 * fp_current ** 2
        eps_angular = params.eta ** 2 * f_current ** 2 / r_int ** 2
        eps_potential = 0.25 * lam * params.eta ** 4 * (f_current ** 2 - 1.0) ** 2
        eps_current = eps_kinetic + eps_angular + eps_potential

        if residual < params.convergence_tol:
            converged = True
            break

    # Final profiles
    sig_defect_final = _sigma_from_profile(r_int, eps_current)
    A_eff_final, eps_macro_final, sig_macro_final = _compute_macro_coupled(
        r_int, sig_defect_final, params.scalar_A, params.beta_XR,
        params.M, params.tau, params.R_ext,
    )

    return CoupledProfileSolution(
        converged=converged, n_iterations=n_iter, g_portal=params.g_portal,
        lam=lam, r_grid=r_int,
        f_defect=f_current, f_defect_prime=fp_current,
        epsilon_defect=eps_current, sigma_defect=sig_defect_final,
        sigma_defect_at_Req=float(sig_defect_final[0]),
        A_eff=A_eff_final, A_eff_at_Req=float(A_eff_final[0]),
        epsilon_macro=eps_macro_final, sigma_macro=sig_macro_final,
        sigma_macro_at_Req=float(sig_macro_final[0]),
        convergence_history=history,
        final_residual=history[-1] if history else 0.0,
        relaxation_used=omega,
        notes=[
            f"Converged: {converged} in {n_iter} iterations",
            f"Final residual: {history[-1] if history else 0.0:.6e}",
            f"Relaxation used: {omega}",
            f"g_portal: {params.g_portal}",
        ],
    )


# ================================================================
# Level 2: Profile Deformation Assessment
# ================================================================

def assess_profile_deformation(
    sc: CoupledProfileSolution,
    frozen: CoupledProfileSolution,
    params: SelfConsistentParams,
) -> ProfileDeformationAssessment:
    """Compare self-consistent vs frozen defect profiles."""
    r = sc.r_grid
    f_shift = sc.f_defect - frozen.f_defect
    f_shift_max = float(np.max(np.abs(f_shift)))
    f_shift_rms = float(np.sqrt(np.mean(f_shift ** 2)))
    f_shift_Req = float(f_shift[0])

    # Core change: f'(r_min) shift
    core_change = float(sc.f_defect_prime[0] - frozen.f_defect_prime[0])

    # Tail change: f(r_max) shift
    tail_change = float(sc.f_defect[-1] - frozen.f_defect[-1])

    # Crossover radius
    cross_frozen = _find_crossover_radius(r, frozen.sigma_macro, frozen.sigma_defect)
    cross_sc = _find_crossover_radius(r, sc.sigma_macro, sc.sigma_defect)
    cross_shift = cross_sc - cross_frozen

    # Sigma shift
    sig_shift = (sc.sigma_defect_at_Req - frozen.sigma_defect_at_Req) / (
        frozen.sigma_defect_at_Req if frozen.sigma_defect_at_Req > 1e-12 else 1.0
    )

    # Classify deformation
    if f_shift_max < DEFORMATION_THRESHOLDS["negligible"]:
        deform_cls = "negligible"
    elif f_shift_max < DEFORMATION_THRESHOLDS["moderate"]:
        deform_cls = "moderate"
    elif f_shift_max < DEFORMATION_THRESHOLDS["significant"]:
        deform_cls = "significant"
    else:
        deform_cls = "large"

    return ProfileDeformationAssessment(
        f_shift_max=f_shift_max, f_shift_rms=f_shift_rms,
        f_shift_at_Req=f_shift_Req,
        crossover_radius_frozen=cross_frozen,
        crossover_radius_sc=cross_sc,
        crossover_shift=cross_shift,
        core_change=core_change, tail_change=tail_change,
        sigma_defect_shift=sig_shift,
        deformation_classification=deform_cls,
        notes=[
            f"Max |delta_f|: {f_shift_max:.6f}",
            f"RMS delta_f: {f_shift_rms:.6f}",
            f"Crossover shift: {cross_shift:.4f}",
            f"Core f' change: {core_change:.6f}",
            f"Deformation: {deform_cls}",
        ],
    )


# ================================================================
# Level 3: Metric Injection
# ================================================================

def inject_self_consistent_metric(
    sc: CoupledProfileSolution,
    params: SelfConsistentParams,
) -> SelfConsistentMetricResult:
    """Inject self-consistent profiles into the metric."""
    r = sc.r_grid
    mass_coeff = 2.0 * math.pi * params.M ** 2 / params.tau ** 2

    m_static = params.M + mass_coeff * (1.0 / r - 1.0 / params.R_ext)
    delta_coupled = m_static + params.alpha_BR * sc.sigma_defect - r / 2.0
    sig_total = sc.sigma_macro + sc.sigma_defect
    f_coupled = -2.0 * (delta_coupled - sig_total) / r

    f_min = float(np.min(f_coupled))
    f_min_idx = int(np.argmin(f_coupled))
    f_min_r = float(r[f_min_idx])
    metric_pos = bool(f_min > 0)
    f_at_Req = float(f_coupled[0])

    # D7 frozen reference
    f_d7 = _compute_d7_frozen_metric(
        r, np.interp(r, sc.r_grid, sc.epsilon_defect) * 0 + sc.epsilon_defect,
        params,
    )
    # Actually recompute D7 frozen properly
    _, _, _, eps_frozen, _ = _solve_frozen_baseline(params, lam_override=sc.lam)
    f_d7 = _compute_d7_frozen_metric(
        np.linspace(R_EQ + 1e-6, params.R_ext, params.n_interior),
        eps_frozen, params,
    )

    metric_shift = f_min - f_d7

    # Budget at key radii
    budget: Dict[str, Dict[str, float]] = {}
    for r_key in [R_EQ, 0.5, 0.75, 1.0]:
        if R_EQ <= r_key <= params.R_ext:
            idx = int(np.argmin(np.abs(r - r_key)))
            budget[f"r={r_key:.4f}"] = {
                "delta_coupled": float(delta_coupled[idx]),
                "sigma_macro": float(sc.sigma_macro[idx]),
                "sigma_defect": float(sc.sigma_defect[idx]),
                "sigma_total": float(sig_total[idx]),
                "f_coupled": float(f_coupled[idx]),
            }

    return SelfConsistentMetricResult(
        r_grid=r, f_coupled=f_coupled, f_min=f_min, f_min_radius=f_min_r,
        metric_positive=metric_pos, f_at_Req=f_at_Req,
        f_d7_at_Req=f_d7, metric_shift_from_d7=metric_shift,
        budget=budget,
        notes=[
            f"f_min = {f_min:.6f} at r = {f_min_r:.4f}",
            f"Metric positive: {metric_pos}",
            f"Shift from D7 frozen: {metric_shift:.6f}",
        ],
    )


# ================================================================
# Level 4: Lambda Scan
# ================================================================

def scan_lambda_self_consistent(
    params: SelfConsistentParams,
) -> LambdaScanResult:
    """Scan lambda: D7 frozen vs self-consistent at unit benchmark."""
    entries: List[LambdaScanEntry] = []

    for lam_val in params.lambda_scan:
        # Frozen baseline (g_portal=0)
        p_frozen = SelfConsistentParams(
            eta=params.eta, lam=lam_val, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=params.alpha_BR, beta_XR=params.beta_XR,
            g_portal=0.0,
        )
        frozen_sol = solve_self_consistent(p_frozen, lam_override=lam_val)
        f_d7 = _compute_d7_frozen_metric(
            frozen_sol.r_grid, frozen_sol.epsilon_defect, p_frozen,
        )
        met_pos_d7 = bool(f_d7 > 0)

        # Self-consistent
        p_sc = SelfConsistentParams(
            eta=params.eta, lam=lam_val, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=params.alpha_BR, beta_XR=params.beta_XR,
            g_portal=params.g_portal,
            max_iterations=params.max_iterations,
            convergence_tol=params.convergence_tol,
            relaxation_factor=params.relaxation_factor,
        )
        sc_sol = solve_self_consistent(p_sc, lam_override=lam_val)
        met_sc = inject_self_consistent_metric(sc_sol, p_sc)

        # Deformation
        deform = assess_profile_deformation(sc_sol, frozen_sol, params)

        entries.append(LambdaScanEntry(
            lam=lam_val,
            converged_frozen=frozen_sol.converged,
            converged_sc=sc_sol.converged,
            n_iterations=sc_sol.n_iterations,
            f_min_d7=f_d7,
            f_min_sc=met_sc.f_min,
            metric_positive_d7=met_pos_d7,
            metric_positive_sc=met_sc.metric_positive,
            f_shift=met_sc.f_min - f_d7,
            deformation_max=deform.f_shift_max,
            notes=f"lam={lam_val}",
        ))

    n_scanned = len(entries)
    n_conv = sum(1 for e in entries if e.converged_sc)
    n_pos_d7 = sum(1 for e in entries if e.metric_positive_d7)
    n_pos_sc = sum(1 for e in entries if e.metric_positive_sc)

    viable_d7 = [e.lam for e in entries if e.metric_positive_d7]
    viable_sc = [e.lam for e in entries if e.metric_positive_sc]

    if viable_sc == viable_d7:
        shift = "unchanged"
    elif len(viable_sc) > len(viable_d7):
        shift = "lower"
    elif len(viable_sc) < len(viable_d7):
        shift = "higher"
    elif len(viable_sc) == 0:
        shift = "destroyed"
    else:
        shift = "shifted"

    d7_25plus = [e.lam for e in entries if e.metric_positive_d7 and e.lam >= 25]
    sc_25plus = [e.lam for e in entries if e.metric_positive_sc and e.lam >= 25]
    rescue = len(sc_25plus) >= len(d7_25plus) and len(d7_25plus) > 0

    return LambdaScanResult(
        entries=entries, n_scanned=n_scanned, n_converged=n_conv,
        n_positive_d7=n_pos_d7, n_positive_sc=n_pos_sc,
        viable_d7=viable_d7, viable_sc=viable_sc,
        threshold_shift=shift, rescue_preserved=rescue,
        notes=[
            f"Scanned {n_scanned} lambda values, {n_conv} converged.",
            f"Viable D7: {viable_d7}",
            f"Viable SC: {viable_sc}",
            f"Threshold shift: {shift}",
        ],
    )


# ================================================================
# Level 5: Portal Strength Scan
# ================================================================

def scan_portal_strength(
    params: SelfConsistentParams,
) -> PortalScanResult:
    """Scan portal strength for sensitivity at default lambda."""
    entries: List[PortalScanEntry] = []

    for g_val in params.g_portal_scan:
        p = SelfConsistentParams(
            eta=params.eta, lam=params.lam, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=params.alpha_BR, beta_XR=params.beta_XR,
            g_portal=g_val,
            max_iterations=params.max_iterations,
            convergence_tol=params.convergence_tol,
            relaxation_factor=params.relaxation_factor,
        )
        sc_sol = solve_self_consistent(p)
        met = inject_self_consistent_metric(sc_sol, p)

        # Deformation vs frozen
        p0 = SelfConsistentParams(
            eta=params.eta, lam=params.lam, xi=params.xi,
            r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
            n_interior=params.n_interior, M=params.M, tau=params.tau,
            R_ext=params.R_ext, scalar_A=params.scalar_A,
            alpha_BR=params.alpha_BR, beta_XR=params.beta_XR,
            g_portal=0.0,
        )
        frozen_sol = solve_self_consistent(p0)
        deform = assess_profile_deformation(sc_sol, frozen_sol, params)

        entries.append(PortalScanEntry(
            g_portal=g_val, converged=sc_sol.converged,
            n_iterations=sc_sol.n_iterations,
            f_min=met.f_min, metric_positive=met.metric_positive,
            deformation_max=deform.f_shift_max,
            notes=f"g_portal={g_val}",
        ))

    n_pos = sum(1 for e in entries if e.metric_positive)
    all_pos = n_pos == len(entries)
    max_deform = max(e.deformation_max for e in entries) if entries else 0.0

    if all_pos and max_deform < DEFORMATION_THRESHOLDS["moderate"]:
        sensitivity = "insensitive"
    elif all_pos:
        sensitivity = "mild_sensitivity"
    elif n_pos > 0:
        sensitivity = "moderate_sensitivity"
    else:
        sensitivity = "high_sensitivity"

    return PortalScanResult(
        entries=entries, n_scanned=len(entries), n_positive=n_pos,
        sensitivity_assessment=sensitivity,
        notes=[
            f"Scanned {len(entries)} g_portal values.",
            f"{n_pos}/{len(entries)} positive.",
            f"Max deformation: {max_deform:.6f}",
            f"Sensitivity: {sensitivity}",
        ],
    )


# ================================================================
# Level 6: Classification
# ================================================================

def classify_self_consistent(
    lambda_scan: LambdaScanResult,
    deformation: ProfileDeformationAssessment,
    portal_scan: PortalScanResult,
    params: SelfConsistentParams,
) -> SelfConsistentClassification:
    """Classify the D9 self-consistent coupling result."""
    viable_d7 = lambda_scan.viable_d7
    viable_sc = lambda_scan.viable_sc
    rescue = lambda_scan.rescue_preserved
    deform_level = deformation.deformation_classification
    all_converged = lambda_scan.n_converged == lambda_scan.n_scanned

    if not all_converged and lambda_scan.n_converged < 3:
        classification = "unresolved_solver_artifacts"
        d7_preserved = False
        summary = (
            f"Only {lambda_scan.n_converged}/{lambda_scan.n_scanned} lambda "
            "values converged. Solver artifacts prevent classification."
        )
    elif rescue and len(viable_sc) >= len(viable_d7):
        if viable_sc == viable_d7 or len(viable_sc) > len(viable_d7):
            classification = "self_consistent_coupling_viable"
            d7_preserved = True
            summary = (
                f"D7 viability preserved under self-consistency. "
                f"Viable window: {viable_sc} (D7: {viable_d7}). "
                f"Profile deformation: {deform_level}. "
                f"Proxy closure used."
            )
        else:
            classification = "viability_window_shifted_but_survives"
            d7_preserved = True
            summary = (
                f"Viable window shifted under self-consistency. "
                f"Viable: {viable_sc} (D7: {viable_d7}). "
                f"Deformation: {deform_level}."
            )
    elif len(viable_sc) > 0:
        if len(viable_sc) < len(viable_d7):
            classification = "viability_window_shifted_but_survives"
            d7_preserved = True
            summary = (
                f"Viable window narrowed. Viable: {viable_sc} (D7: {viable_d7}). "
                f"Deformation: {deform_level}."
            )
        else:
            classification = "partially_viable_under_self_consistency"
            d7_preserved = False
            summary = (
                f"Partial viability. Viable: {viable_sc} (D7: {viable_d7})."
            )
    elif len(viable_sc) == 0 and len(viable_d7) > 0:
        classification = "destroyed_by_self_consistency"
        d7_preserved = False
        summary = "Self-consistency eliminates metric positivity at all lambda."
    else:
        classification = "unresolved_solver_artifacts"
        d7_preserved = False
        summary = "Unresolved."

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
        "cross_coupling_D7": "LOCKED (fully_coupled_viable)",
        "coupled_action_D8": "LOCKED (d7_channels_largely_action_derived)",
        "self_consistent_D9": phase_status,
    }

    return SelfConsistentClassification(
        classification=classification,
        phase_status=phase_status,
        d7_viability_preserved=d7_preserved,
        deformation_level=deform_level,
        proxy_closure_used=True,
        summary=summary,
        phase_lock_update=phase_lock,
    )


# ================================================================
# Level 7: Master Computation
# ================================================================

def compute_self_consistent(
    params: Optional[SelfConsistentParams] = None,
) -> SelfConsistentResult:
    """Run the full Phase D9 self-consistent coupling analysis."""
    if params is None:
        params = SelfConsistentParams()

    result = SelfConsistentResult(
        valid=True, params=params,
        nonclaims=list(SELF_CONSISTENT_NONCLAIMS),
        assumptions=list(SELF_CONSISTENT_ASSUMPTIONS),
    )

    # Level 0: Solver definition
    result.solver_definition = define_coupled_solver(params)

    # Level 1: Solve frozen baseline (g_portal=0)
    p_frozen = SelfConsistentParams(
        eta=params.eta, lam=params.lam, xi=params.xi,
        r_min=params.r_min, r_max=params.r_max, n_grid=params.n_grid,
        n_interior=params.n_interior, M=params.M, tau=params.tau,
        R_ext=params.R_ext, scalar_A=params.scalar_A,
        alpha_BR=params.alpha_BR, beta_XR=params.beta_XR,
        g_portal=0.0,
    )
    result.frozen_solution = solve_self_consistent(p_frozen)

    # Level 1: Solve self-consistent
    result.profile_solution = solve_self_consistent(params)

    # Level 2: Profile deformation
    result.deformation = assess_profile_deformation(
        result.profile_solution, result.frozen_solution, params,
    )

    # Level 3: Metric injection
    result.metric_result = inject_self_consistent_metric(
        result.profile_solution, params,
    )

    # Level 4: Lambda scan
    result.lambda_scan = scan_lambda_self_consistent(params)

    # Level 5: Portal scan
    result.portal_scan = scan_portal_strength(params)

    # Level 6: Classification
    result.classification = classify_self_consistent(
        result.lambda_scan, result.deformation,
        result.portal_scan, params,
    )

    return result


# ================================================================
# Level 8: Serialization
# ================================================================

def self_consistent_result_to_dict(
    result: SelfConsistentResult,
) -> Dict[str, Any]:
    """Serialize to JSON-compatible dict."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "phase": "D9",
        "title": "Self-Consistent Coupled Profile Integration",
    }

    if result.solver_definition:
        sd = result.solver_definition
        d["solver_definition"] = {
            "iteration_scheme": sd.iteration_scheme,
            "modified_ode": sd.modified_ode,
            "proxy_closure_statement": sd.proxy_closure_statement,
            "sign_analysis": sd.sign_analysis,
            "under_relaxation_scheme": sd.under_relaxation_scheme,
        }

    if result.profile_solution:
        ps = result.profile_solution
        d["profile_solution"] = {
            "converged": ps.converged,
            "n_iterations": ps.n_iterations,
            "g_portal": ps.g_portal,
            "sigma_defect_at_Req": ps.sigma_defect_at_Req,
            "A_eff_at_Req": ps.A_eff_at_Req,
            "sigma_macro_at_Req": ps.sigma_macro_at_Req,
            "final_residual": ps.final_residual,
            "relaxation_used": ps.relaxation_used,
        }

    if result.deformation:
        df = result.deformation
        d["deformation"] = {
            "f_shift_max": df.f_shift_max,
            "f_shift_rms": df.f_shift_rms,
            "crossover_radius_frozen": df.crossover_radius_frozen,
            "crossover_radius_sc": df.crossover_radius_sc,
            "crossover_shift": df.crossover_shift,
            "core_change": df.core_change,
            "tail_change": df.tail_change,
            "sigma_defect_shift": df.sigma_defect_shift,
            "deformation_classification": df.deformation_classification,
        }

    if result.metric_result:
        mr = result.metric_result
        d["metric_result"] = {
            "f_min": mr.f_min,
            "f_min_radius": mr.f_min_radius,
            "metric_positive": mr.metric_positive,
            "f_at_Req": mr.f_at_Req,
            "f_d7_at_Req": mr.f_d7_at_Req,
            "metric_shift_from_d7": mr.metric_shift_from_d7,
            "budget": mr.budget,
        }

    if result.lambda_scan:
        ls = result.lambda_scan
        d["lambda_scan"] = {
            "n_scanned": ls.n_scanned,
            "n_converged": ls.n_converged,
            "n_positive_d7": ls.n_positive_d7,
            "n_positive_sc": ls.n_positive_sc,
            "viable_d7": ls.viable_d7,
            "viable_sc": ls.viable_sc,
            "threshold_shift": ls.threshold_shift,
            "rescue_preserved": ls.rescue_preserved,
            "entries": [
                {
                    "lam": e.lam,
                    "converged_sc": e.converged_sc,
                    "n_iterations": e.n_iterations,
                    "f_min_d7": e.f_min_d7,
                    "f_min_sc": e.f_min_sc,
                    "metric_positive_d7": e.metric_positive_d7,
                    "metric_positive_sc": e.metric_positive_sc,
                    "f_shift": e.f_shift,
                    "deformation_max": e.deformation_max,
                }
                for e in ls.entries
            ],
        }

    if result.portal_scan:
        ps2 = result.portal_scan
        d["portal_scan"] = {
            "n_scanned": ps2.n_scanned,
            "n_positive": ps2.n_positive,
            "sensitivity_assessment": ps2.sensitivity_assessment,
            "entries": [
                {
                    "g_portal": e.g_portal,
                    "converged": e.converged,
                    "f_min": e.f_min,
                    "metric_positive": e.metric_positive,
                    "deformation_max": e.deformation_max,
                }
                for e in ps2.entries
            ],
        }

    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "d7_viability_preserved": cl.d7_viability_preserved,
            "deformation_level": cl.deformation_level,
            "proxy_closure_used": cl.proxy_closure_used,
            "summary": cl.summary,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
