"""Phase D2 — Numerical Monopole Integration and Interior Metric Viability.

Numerically solves the hedgehog ODE via boundary-value problem, extracts the
full defect energy-density profile, and injects it into the established
interior metric framework to test whether metric positivity can be restored.

PRINCIPAL RESULTS:

  Result 1 — BVP Solver:
    The hedgehog ODE f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0
    is solved as a two-point BVP with f(r_min)~0, f(r_max)=1.
    The free parameter c_1 (slope at origin) is determined by the solver.

  Result 2 — Core Regularity:
    The near-origin expansion f(r) ~ c_1*r*(1 - lam*eta^2*r^2/10) is
    regular.  Core energy density is finite and integrable.

  Result 3 — Two Coupling Modes:
    Case A (additive): scalar at A_crit + defect.  Tests stacked rescue.
    Case B (hybrid):   scalar at A=1 + defect.  Tests whether defect
                       supplies Component B independently.

  Result 4 — Metric Injection:
    f_corrected(r) = -2*(delta(r) - Sigma_total(r))/r
    where Sigma_total = Sigma_scalar + Sigma_defect.

  Result 5 — Classification:
    (determined by numerical outcome)

SELF-CONTAINED: Depends only on math, numpy, scipy.  No grut/ cross-imports.
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
A_CRIT_SQUARED = A_CRIT ** 2  # ~ 1.128

COMP_B_COEFF = 1.0 / (8.0 * math.pi)
ETA_MATCH = 1.0 / math.sqrt(8.0 * math.pi)
ETA_MATCH_SQUARED = ETA_MATCH ** 2  # = COMP_B_COEFF

MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
R_EXT = 2.0 * R_S  # exterior boundary (matches Phase 6 DeficitParams)

LAMBDA_SCAN_VALUES = [5.0, 10.0, 25.0, 50.0, 100.0, 200.0]
PHASE6_F_AT_REQ = -17.71

# Key radii for Sigma accounting
KEY_RADII = [R_EQ, 0.5, 0.75, 1.0]


# ================================================================
# Assumptions
# ================================================================

MONOPOLE_ASSUMPTIONS = [
    "1. The hedgehog ODE is solved as a two-point BVP with scipy.solve_bvp. "
    "The free parameter c_1 (slope at origin) is determined by the solver.",

    "2. The near-origin expansion f(r) ~ c_1*r - c_1*lam*eta^2*r^3/10 "
    "is used to initialize the BVP guess near r_min > 0.",

    "3. The coefficient-matching condition eta^2 = 1/(8*pi) is held fixed. "
    "Lambda is scanned to vary core size at fixed eta.",

    "4. Two coupling modes are tested: Case A (scalar at A_crit + defect) "
    "and Case B (scalar at A=1 + defect).  Case B is the interpretively "
    "cleaner test of whether the defect supplies Component B.",

    "5. The metric injection uses the established formula: "
    "f(r) = -2*(delta(r) - Sigma(r))/r where delta = m - r/2 and "
    "Sigma = integral_r^R_ext 4*pi*r'^2 * epsilon dr'.",

    "6. The static mass profile m(r) = M + MASS_COEFF*(1/r - 1/R_ext) "
    "is inherited from the Phase 6 locked result.",

    "7. Sigma_scalar = A^2 * MASS_COEFF * (1/r - 1/R_ext) is the "
    "analytic scalar-memory contribution to the source integral.",

    "8. Sigma_defect is computed by numerical integration of the full "
    "BVP-derived defect energy density profile.",

    "9. The lambda scan is bounded and disciplined, not an exhaustive "
    "parameter search.  It tests core-size dependence at fixed eta.",

    "10. The background metric is held fixed.  No iterative self-consistent "
    "back-reaction loop is implemented in D2.",
]

MONOPOLE_NONCLAIMS = [
    "1. This phase does NOT prove the final particle sector.",

    "2. This phase does NOT prove the defect sector is GRUT canon.",

    "3. This phase does NOT identify eta as a literal electric charge.",

    "4. A successful metric rescue establishes numerical viability, not "
    "full physical derivation.",

    "5. A failed metric rescue does NOT invalidate D1 admissibility. "
    "It shows this candidate extension is insufficient or unstable "
    "in the tested coupling setup.",

    "6. The additive coupling (Case A) may overstack support terms. "
    "Case B is the cleaner test.",

    "7. The BVP solver uses finite-domain approximation (r_min > 0, "
    "r_max < infinity).  Domain effects are monitored but not "
    "fully eliminated.",

    "8. The static mass profile is inherited, not re-derived with "
    "the defect sector included self-consistently.",

    "9. The lambda scan explores a bounded range.  Extreme values "
    "of lambda may produce different behavior.",

    "10. The classification is within the tested numerical framework "
    "only.  Alternative coupling architectures might yield "
    "different results.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class NumericalMonopoleParams:
    """Parameters for Phase D2."""
    eta: float = ETA_MATCH
    lam: float = 25.0  # default lambda (moderate core)
    r_min: float = 0.01
    r_max: float = 5.0
    n_grid: int = 300
    lambda_scan: List[float] = field(
        default_factory=lambda: list(LAMBDA_SCAN_VALUES)
    )
    # Metric parameters
    M: float = M_EXT
    tau: float = TAU_CANONICAL
    R_ext: float = R_EXT


@dataclass
class CoreSeriesExpansion:
    """Near-origin series f(r) ~ c1*r + c3*r^3."""
    c1_estimate: float  # estimated slope at origin
    c3_formula: str     # c3 = -lam*eta^2*c1/10
    c3_value: float
    series_at_rmin: float  # f(r_min) from series
    notes: List[str] = field(default_factory=list)


@dataclass
class HedgehogBVPSolution:
    """Numerical BVP solution."""
    converged: bool
    r_grid: np.ndarray
    f_solution: np.ndarray
    f_prime: np.ndarray
    c1_effective: float  # f'(r_min) ≈ c1 from solution
    max_residual: float
    f_at_rmax: float
    notes: List[str] = field(default_factory=list)


@dataclass
class DefectEnergyProfile:
    """Energy density profile from BVP solution."""
    r_grid: np.ndarray
    radial_kinetic: np.ndarray
    angular_gradient: np.ndarray
    potential_term: np.ndarray
    total_epsilon: np.ndarray
    core_peak: float
    integrated_mass: float  # 4pi * integral r^2 * epsilon dr
    tail_exponent: float
    tail_coefficient: float  # epsilon*r^2 at large r
    notes: List[str] = field(default_factory=list)


@dataclass
class MetricInjectionResult:
    """Result of injecting defect into interior metric."""
    coupling_mode: str  # "case_A" or "case_B"
    scalar_amplitude: float  # A used for scalar sector
    r_grid: np.ndarray
    delta: np.ndarray        # m(r) - r/2
    sigma_scalar: np.ndarray
    sigma_defect: np.ndarray
    sigma_total: np.ndarray
    f_corrected: np.ndarray
    f_min: float
    f_min_radius: float
    metric_positive: bool
    # Sigma accounting: defect fraction at key radii
    defect_fraction: Dict[str, float]  # {r_value: fraction}
    notes: List[str] = field(default_factory=list)


@dataclass
class LambdaScanEntry:
    """One entry in the lambda scan."""
    lam: float
    bvp_converged: bool
    core_peak: float
    tail_exponent: float
    f_min_case_A: float
    f_min_case_B: float
    metric_positive_A: bool
    metric_positive_B: bool
    defect_sigma_fraction_at_Req: float
    notes: str = ""


@dataclass
class LambdaScanResult:
    """Full lambda scan result."""
    entries: List[LambdaScanEntry]
    n_scanned: int
    n_converged: int
    n_positive_A: int
    n_positive_B: int
    best_lambda_A: Optional[float]
    best_lambda_B: Optional[float]
    best_fmin_A: float
    best_fmin_B: float
    notes: List[str] = field(default_factory=list)


@dataclass
class CompatibilityCheck:
    """Compatibility with prior locked results."""
    component_A_intact: bool
    coupling_is_additive: bool
    locked_results_preserved: bool
    defect_provides_component_B_shape: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class NumericalMonopoleClassification:
    """Final D2 classification."""
    classification: str
    phase_status: str
    metric_positive_case_A: bool
    metric_positive_case_B: bool
    best_fmin_A: float
    best_fmin_B: float
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class NumericalMonopoleResult:
    """Master result container."""
    valid: bool
    params: NumericalMonopoleParams
    core_series: Optional[CoreSeriesExpansion] = None
    bvp_solution: Optional[HedgehogBVPSolution] = None
    energy_profile: Optional[DefectEnergyProfile] = None
    injection_A: Optional[MetricInjectionResult] = None
    injection_B: Optional[MetricInjectionResult] = None
    lambda_scan: Optional[LambdaScanResult] = None
    compatibility: Optional[CompatibilityCheck] = None
    classification: Optional[NumericalMonopoleClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Helpers
# ================================================================

def _make_grid(r_min: float, r_max: float, n: int) -> np.ndarray:
    return np.linspace(r_min, r_max, n)


def _fit_exponent(r: np.ndarray, y: np.ndarray) -> float:
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


def _sigma_from_profile(r: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """Compute Sigma(r) = integral_r^r_max 4*pi*r'^2 * epsilon(r') dr'.

    Uses cumulative trapezoid from the right.
    """
    integrand = 4.0 * math.pi * r ** 2 * epsilon
    # Integrate from right: Sigma(r) = integral_r^r_max
    # We compute the cumulative integral from right to left
    sigma = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = r[i + 1] - r[i]
        sigma[i] = sigma[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * dr
    return sigma


# ================================================================
# Level 1: Core Series
# ================================================================

def compute_core_series(params: NumericalMonopoleParams) -> CoreSeriesExpansion:
    """Near-origin expansion: f(r) ~ c1*r - (lam*eta^2*c1/10)*r^3.

    c1 is the free parameter.  For the initial BVP guess, we estimate
    c1 ~ 1/delta where delta = 1/sqrt(lam*eta^2) is the core size.
    """
    eta = params.eta
    lam = params.lam
    delta_core = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
    c1_est = 1.0 / delta_core  # rough estimate
    c3 = -lam * eta ** 2 * c1_est / 10.0
    f_rmin = c1_est * params.r_min + c3 * params.r_min ** 3

    return CoreSeriesExpansion(
        c1_estimate=c1_est,
        c3_formula="c3 = -lam * eta^2 * c1 / 10",
        c3_value=c3,
        series_at_rmin=f_rmin,
        notes=[
            f"delta_core = 1/sqrt(lam*eta^2) = {delta_core:.4f}",
            f"c1 estimate = {c1_est:.4f}",
            f"c3 = {c3:.6f}",
            f"f(r_min={params.r_min}) ~ {f_rmin:.6f}",
        ],
    )


# ================================================================
# Level 2: BVP Solver
# ================================================================

def solve_hedgehog_bvp(
    params: NumericalMonopoleParams,
) -> HedgehogBVPSolution:
    """Solve the hedgehog ODE as a two-point BVP.

    f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0
    f(r_min) ~ 0, f(r_max) = 1

    c1 (the slope at the origin) is the free matching parameter,
    solved by the BVP system adjusting the interior profile.
    """
    eta = params.eta
    lam = params.lam
    r_min = params.r_min
    r_max = params.r_max
    n = params.n_grid

    r_grid = _make_grid(r_min, r_max, n)

    # ODE system: y[0] = f, y[1] = f'
    def ode(r, y):
        f_val = y[0]
        fp = y[1]
        fpp = -(2.0 / r) * fp + (2.0 / r ** 2) * f_val + lam * eta ** 2 * f_val * (f_val ** 2 - 1.0)
        return np.array([fp, fpp])

    # Boundary conditions: f(r_min) ~ small, f(r_max) = 1
    def bc(ya, yb):
        # ya at r_min: f should be small (~c1*r_min)
        # yb at r_max: f = 1
        return np.array([ya[0] - 0.0, yb[0] - 1.0])
        # Setting ya[0] = 0 at r_min (close to origin)

    # Initial guess: D1 analytic profile
    delta_core = 1.0 / math.sqrt(lam * eta ** 2) if lam * eta ** 2 > 0 else 1.0
    f_guess = r_grid / np.sqrt(r_grid ** 2 + delta_core ** 2)
    fp_guess = delta_core ** 2 / (r_grid ** 2 + delta_core ** 2) ** 1.5
    y_guess = np.array([f_guess, fp_guess])

    if not HAS_SCIPY_BVP:
        # Fallback: use analytic profile
        return HedgehogBVPSolution(
            converged=False,
            r_grid=r_grid,
            f_solution=f_guess,
            f_prime=fp_guess,
            c1_effective=fp_guess[0],
            max_residual=float("nan"),
            f_at_rmax=f_guess[-1],
            notes=["scipy.solve_bvp not available; using analytic fallback"],
        )

    try:
        sol = solve_bvp(ode, bc, r_grid, y_guess, tol=1e-6, max_nodes=5000)
        converged = sol.success

        # Evaluate on original grid
        y_sol = sol.sol(r_grid)
        f_sol = y_sol[0]
        fp_sol = y_sol[1]

        # Compute residual
        rhs = ode(r_grid, y_sol)
        # Residual from the RHS vs actual derivatives
        max_res = float(sol.rms_residuals.max()) if hasattr(sol, 'rms_residuals') else 0.0

        c1_eff = float(fp_sol[0])

        return HedgehogBVPSolution(
            converged=converged,
            r_grid=r_grid,
            f_solution=f_sol,
            f_prime=fp_sol,
            c1_effective=c1_eff,
            max_residual=max_res,
            f_at_rmax=float(f_sol[-1]),
            notes=[
                f"BVP converged: {converged}",
                f"c1_effective (f' at r_min): {c1_eff:.6f}",
                f"f(r_max) = {f_sol[-1]:.8f}",
                f"Max RMS residual: {max_res:.2e}",
            ],
        )
    except Exception as exc:
        # Fallback to analytic
        return HedgehogBVPSolution(
            converged=False,
            r_grid=r_grid,
            f_solution=f_guess,
            f_prime=fp_guess,
            c1_effective=float(fp_guess[0]),
            max_residual=float("nan"),
            f_at_rmax=float(f_guess[-1]),
            notes=[f"BVP solver failed: {exc}; using analytic fallback"],
        )


# ================================================================
# Level 3: Energy Profile
# ================================================================

def extract_defect_energy(
    bvp: HedgehogBVPSolution,
    params: NumericalMonopoleParams,
) -> DefectEnergyProfile:
    """Extract the 3-term energy density from the BVP solution."""
    r = bvp.r_grid
    f = bvp.f_solution
    fp = bvp.f_prime
    eta = params.eta
    lam = params.lam

    radial_kinetic = 0.5 * eta ** 2 * fp ** 2
    angular_gradient = eta ** 2 * f ** 2 / r ** 2
    potential = 0.25 * lam * eta ** 4 * (f ** 2 - 1.0) ** 2
    total = radial_kinetic + angular_gradient + potential

    core_peak = float(np.max(total))
    # Integrated mass: 4*pi * integral r^2 * epsilon dr
    integrand = 4.0 * math.pi * r ** 2 * total
    _trapz = getattr(np, "trapezoid", np.trapz)
    int_mass = float(_trapz(integrand, r))

    # Tail analysis (outer quarter)
    n = len(r)
    outer = slice(3 * n // 4, n)
    tail_exp = _fit_exponent(r[outer], total[outer])
    tail_coeff = float(total[-1] * r[-1] ** 2)

    return DefectEnergyProfile(
        r_grid=r,
        radial_kinetic=radial_kinetic,
        angular_gradient=angular_gradient,
        potential_term=potential,
        total_epsilon=total,
        core_peak=core_peak,
        integrated_mass=int_mass,
        tail_exponent=tail_exp,
        tail_coefficient=tail_coeff,
        notes=[
            f"Core peak epsilon: {core_peak:.6f}",
            f"Integrated defect mass: {int_mass:.6f}",
            f"Tail exponent: {tail_exp:.4f}",
            f"Tail coefficient (epsilon*r^2): {tail_coeff:.6f} (target: {ETA_MATCH_SQUARED:.6f})",
        ],
    )


# ================================================================
# Level 4: Metric Injection
# ================================================================

def inject_into_metric(
    energy: DefectEnergyProfile,
    params: NumericalMonopoleParams,
    scalar_A: float,
) -> MetricInjectionResult:
    """Inject defect energy into the interior metric.

    Coupling mode determined by scalar_A:
      Case A: scalar_A = A_CRIT (additive diagnostic)
      Case B: scalar_A = 1.0   (reduced-scalar / hybrid)

    IMPORTANT: The metric formulas are valid only in the interior domain
    [R_EQ, R_ext].  The BVP domain [r_min, r_max] is larger (to allow
    the hedgehog to reach f -> 1).  We:
      1. Build an interior grid within [R_EQ, R_ext]
      2. Interpolate the BVP-derived epsilon_defect onto it
      3. Compute Sigma_defect = integral_r^R_ext 4*pi*r'^2 * epsilon dr'
         with upper limit R_ext (not r_max)
      4. Evaluate f_corrected only on the interior grid

    delta(r) = m(r) - r/2
    m(r) = M + MASS_COEFF * (1/r - 1/R_ext)
    Sigma_scalar = A^2 * MASS_COEFF * (1/r - 1/R_ext)
    f_corrected = -2*(delta - Sigma_total)/r
    """
    M = params.M
    tau = params.tau
    R_ext = params.R_ext

    mass_coeff = 2.0 * math.pi * M ** 2 / tau ** 2

    # ---- Build interior grid [R_EQ, R_ext] ----
    n_interior = 400
    r_int = np.linspace(R_EQ + 1e-6, R_ext, n_interior)

    # ---- Interpolate defect epsilon onto interior grid ----
    eps_interp = np.interp(r_int, energy.r_grid, energy.total_epsilon)

    # ---- Static mass profile (inherited from Phase 6) ----
    m_r = M + mass_coeff * (1.0 / r_int - 1.0 / R_ext)
    delta = m_r - r_int / 2.0

    # ---- Sigma from scalar memory (analytic) ----
    sigma_scalar = scalar_A ** 2 * mass_coeff * (1.0 / r_int - 1.0 / R_ext)

    # ---- Sigma from defect: integral_r^R_ext 4*pi*r'^2 * epsilon dr' ----
    sigma_defect = _sigma_from_profile(r_int, eps_interp)

    sigma_total = sigma_scalar + sigma_defect

    # ---- Corrected metric coefficient ----
    f_corrected = -2.0 * (delta - sigma_total) / r_int

    f_min = float(np.min(f_corrected))
    f_min_idx = int(np.argmin(f_corrected))
    f_min_r = float(r_int[f_min_idx])
    metric_pos = bool(f_min > 0)

    # Mode label
    if abs(scalar_A - A_CRIT) < 0.01:
        mode = "case_A"
    elif abs(scalar_A - 1.0) < 0.01:
        mode = "case_B"
    else:
        mode = f"custom_A={scalar_A:.3f}"

    # Sigma accounting at key radii
    defect_frac: Dict[str, float] = {}
    for r_key in KEY_RADII:
        if R_EQ <= r_key <= R_ext:
            idx = int(np.argmin(np.abs(r_int - r_key)))
            st = sigma_total[idx]
            sd = sigma_defect[idx]
            frac = sd / st if st > 1e-30 else 0.0
            defect_frac[f"r={r_key:.4f}"] = float(frac)

    notes = [
        f"Coupling mode: {mode} (scalar A = {scalar_A:.3f})",
        f"Interior grid: [{R_EQ:.4f}, {R_ext:.4f}] ({n_interior} points)",
        f"f_min = {f_min:.6f} at r = {f_min_r:.4f}",
        f"Metric globally positive: {metric_pos}",
    ]
    for k, v in defect_frac.items():
        notes.append(f"Defect Sigma fraction at {k}: {v:.4f}")

    return MetricInjectionResult(
        coupling_mode=mode,
        scalar_amplitude=scalar_A,
        r_grid=r_int,
        delta=delta,
        sigma_scalar=sigma_scalar,
        sigma_defect=sigma_defect,
        sigma_total=sigma_total,
        f_corrected=f_corrected,
        f_min=f_min,
        f_min_radius=f_min_r,
        metric_positive=metric_pos,
        defect_fraction=defect_frac,
        notes=notes,
    )


def run_both_coupling_cases(
    energy: DefectEnergyProfile,
    params: NumericalMonopoleParams,
) -> Tuple[MetricInjectionResult, MetricInjectionResult]:
    """Run metric injection for both Case A and Case B."""
    case_A = inject_into_metric(energy, params, scalar_A=A_CRIT)
    case_B = inject_into_metric(energy, params, scalar_A=1.0)
    return case_A, case_B


# ================================================================
# Level 5: Lambda Scan
# ================================================================

def scan_lambda(
    params: NumericalMonopoleParams,
) -> LambdaScanResult:
    """Scan over lambda values at fixed eta^2 = 1/(8*pi)."""
    entries: List[LambdaScanEntry] = []

    for lam_val in params.lambda_scan:
        p = NumericalMonopoleParams(
            eta=params.eta,
            lam=lam_val,
            r_min=params.r_min,
            r_max=params.r_max,
            n_grid=params.n_grid,
            M=params.M,
            tau=params.tau,
            R_ext=params.R_ext,
        )

        bvp = solve_hedgehog_bvp(p)
        energy = extract_defect_energy(bvp, p)
        case_A, case_B = run_both_coupling_cases(energy, p)

        # Defect fraction at R_eq
        frac_key = f"r={R_EQ:.4f}"
        frac_Req = case_B.defect_fraction.get(frac_key, 0.0)

        entries.append(LambdaScanEntry(
            lam=lam_val,
            bvp_converged=bvp.converged,
            core_peak=energy.core_peak,
            tail_exponent=energy.tail_exponent,
            f_min_case_A=case_A.f_min,
            f_min_case_B=case_B.f_min,
            metric_positive_A=case_A.metric_positive,
            metric_positive_B=case_B.metric_positive,
            defect_sigma_fraction_at_Req=frac_Req,
            notes=f"lam={lam_val:.1f}, core_peak={energy.core_peak:.4f}",
        ))

    n_conv = sum(1 for e in entries if e.bvp_converged)
    n_pos_A = sum(1 for e in entries if e.metric_positive_A)
    n_pos_B = sum(1 for e in entries if e.metric_positive_B)

    # Best lambda for each case (highest f_min)
    best_A = max(entries, key=lambda e: e.f_min_case_A)
    best_B = max(entries, key=lambda e: e.f_min_case_B)

    return LambdaScanResult(
        entries=entries,
        n_scanned=len(entries),
        n_converged=n_conv,
        n_positive_A=n_pos_A,
        n_positive_B=n_pos_B,
        best_lambda_A=best_A.lam if best_A.f_min_case_A > 0 else None,
        best_lambda_B=best_B.lam if best_B.f_min_case_B > 0 else None,
        best_fmin_A=best_A.f_min_case_A,
        best_fmin_B=best_B.f_min_case_B,
        notes=[
            f"Scanned {len(entries)} lambda values",
            f"Converged: {n_conv}/{len(entries)}",
            f"Metric positive Case A: {n_pos_A}/{len(entries)}",
            f"Metric positive Case B: {n_pos_B}/{len(entries)}",
            f"Best f_min Case A: {best_A.f_min_case_A:.6f} at lambda={best_A.lam}",
            f"Best f_min Case B: {best_B.f_min_case_B:.6f} at lambda={best_B.lam}",
        ],
    )


# ================================================================
# Level 6: Compatibility Check
# ================================================================

def check_compatibility(
    injection_A: MetricInjectionResult,
    injection_B: MetricInjectionResult,
    energy: DefectEnergyProfile,
    params: NumericalMonopoleParams,
) -> CompatibilityCheck:
    """Check compatibility with prior locked results."""
    notes: List[str] = []

    # Component A intact?
    # The scalar memory at A=1 provides exactly |rho_eq| = M^2/(2*tau^2*r^4)
    # At A_crit, it provides A_crit^2 * |rho_eq|
    # The defect does NOT replace Component A — it adds Component B
    comp_A_intact = True
    notes.append("Component A: scalar memory sector unchanged by defect addition")

    # Additive coupling
    coupling_additive = True
    notes.append("Coupling: T_total = T_scalar + T_defect (additive)")

    # Locked results: Phase 6 f(R_eq) = -17.71 was without defect
    # Adding defect changes f(r) — that's the whole point
    locked_ok = True
    notes.append(
        "Prior locked results: Phase 6 metric was computed WITHOUT defect. "
        "Defect is a candidate extension, not a contradiction."
    )

    # Defect provides Component B shape
    tail_ok = abs(energy.tail_exponent - (-2.0)) < 0.1
    notes.append(f"Defect tail exponent: {energy.tail_exponent:.4f} "
                 f"(target: -2.0, match: {tail_ok})")

    return CompatibilityCheck(
        component_A_intact=comp_A_intact,
        coupling_is_additive=coupling_additive,
        locked_results_preserved=locked_ok,
        defect_provides_component_B_shape=tail_ok,
        notes=notes,
    )


# ================================================================
# Level 7: Classification
# ================================================================

def classify_numerical_monopole(
    injection_A: MetricInjectionResult,
    injection_B: MetricInjectionResult,
    scan: LambdaScanResult,
    compat: CompatibilityCheck,
) -> NumericalMonopoleClassification:
    """Classify the D2 result."""
    pos_A = injection_A.metric_positive
    pos_B = injection_B.metric_positive
    any_scan_A = scan.n_positive_A > 0
    any_scan_B = scan.n_positive_B > 0

    if any_scan_B and any_scan_A:
        classification = "defect_candidate_numerically_viable"
        status = "viable"
    elif any_scan_A and not any_scan_B:
        classification = "defect_candidate_partially_viable_but_metric_not_fully_restored"
        status = "partially_viable"
    elif pos_A or pos_B:
        classification = "defect_candidate_partially_viable_but_metric_not_fully_restored"
        status = "partially_viable"
    elif scan.best_fmin_A > -1.0 or scan.best_fmin_B > -1.0:
        classification = "defect_candidate_shape_correct_but_metric_insufficient"
        status = "insufficient"
    else:
        classification = "defect_candidate_unresolved_but_bounded"
        status = "unresolved"

    phase_lock = {
        "phase_6_f_at_req": "LOCKED (-17.71)",
        "phase_6b_A_crit": "LOCKED (1.062)",
        "phase_6c_deficit": "LOCKED (Component A + Component B)",
        "route_c_all": "LOCKED (insufficient)",
        "route_b_all": "LOCKED (closed within Galley CTP)",
        "source_law_program": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "LOCKED (provisional candidate formulated)",
        "defect_D2": f"TESTED ({classification})",
    }

    summary = (
        f"Phase D2: {classification}.  "
        f"Case A (scalar A_crit + defect): f_min = {scan.best_fmin_A:.4f}, "
        f"positive in {scan.n_positive_A}/{scan.n_scanned} lambda values.  "
        f"Case B (scalar A=1 + defect): f_min = {scan.best_fmin_B:.4f}, "
        f"positive in {scan.n_positive_B}/{scan.n_scanned} lambda values."
    )

    return NumericalMonopoleClassification(
        classification=classification,
        phase_status=status,
        metric_positive_case_A=any_scan_A,
        metric_positive_case_B=any_scan_B,
        best_fmin_A=scan.best_fmin_A,
        best_fmin_B=scan.best_fmin_B,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 8: Master Function
# ================================================================

def compute_numerical_monopole(
    params: Optional[NumericalMonopoleParams] = None,
) -> NumericalMonopoleResult:
    """Master function: run the complete Phase D2 assessment."""
    if params is None:
        params = NumericalMonopoleParams()

    result = NumericalMonopoleResult(valid=False, params=params)

    try:
        # 1. Core series
        result.core_series = compute_core_series(params)

        # 2. BVP solution
        result.bvp_solution = solve_hedgehog_bvp(params)

        # 3. Energy profile
        result.energy_profile = extract_defect_energy(
            result.bvp_solution, params,
        )

        # 4. Metric injection (both cases)
        result.injection_A, result.injection_B = run_both_coupling_cases(
            result.energy_profile, params,
        )

        # 5. Lambda scan
        result.lambda_scan = scan_lambda(params)

        # 6. Compatibility
        result.compatibility = check_compatibility(
            result.injection_A, result.injection_B,
            result.energy_profile, params,
        )

        # 7. Classification
        result.classification = classify_numerical_monopole(
            result.injection_A, result.injection_B,
            result.lambda_scan, result.compatibility,
        )

        result.nonclaims = list(MONOPOLE_NONCLAIMS)
        result.assumptions = list(MONOPOLE_ASSUMPTIONS)
        result.diagnostics = {
            "bvp_converged": result.bvp_solution.converged,
            "tail_exponent": result.energy_profile.tail_exponent,
            "core_peak": result.energy_profile.core_peak,
            "f_min_case_A": result.injection_A.f_min,
            "f_min_case_B": result.injection_B.f_min,
            "n_lambda_positive_A": result.lambda_scan.n_positive_A,
            "n_lambda_positive_B": result.lambda_scan.n_positive_B,
            "classification": result.classification.classification,
        }
        result.valid = True

    except Exception as exc:
        result.diagnostics["error"] = str(exc)
        import traceback
        result.diagnostics["traceback"] = traceback.format_exc()

    return result


# ================================================================
# Level 9: Serialization
# ================================================================

def numerical_monopole_result_to_dict(
    result: NumericalMonopoleResult,
) -> Dict[str, Any]:
    """Serialize to JSON-safe dictionary."""
    out: Dict[str, Any] = {"valid": result.valid}

    out["params"] = {
        "eta": result.params.eta,
        "lam": result.params.lam,
        "r_min": result.params.r_min,
        "r_max": result.params.r_max,
        "n_grid": result.params.n_grid,
    }

    if result.core_series is not None:
        cs = result.core_series
        out["core_series"] = {
            "c1_estimate": cs.c1_estimate,
            "c3_value": cs.c3_value,
            "series_at_rmin": cs.series_at_rmin,
            "notes": cs.notes,
        }

    if result.bvp_solution is not None:
        bvp = result.bvp_solution
        out["bvp"] = {
            "converged": bvp.converged,
            "c1_effective": bvp.c1_effective,
            "max_residual": bvp.max_residual,
            "f_at_rmax": bvp.f_at_rmax,
            "notes": bvp.notes,
        }

    if result.energy_profile is not None:
        ep = result.energy_profile
        out["energy"] = {
            "core_peak": ep.core_peak,
            "integrated_mass": ep.integrated_mass,
            "tail_exponent": ep.tail_exponent,
            "tail_coefficient": ep.tail_coefficient,
            "notes": ep.notes,
        }

    for label, inj in [("injection_A", result.injection_A),
                        ("injection_B", result.injection_B)]:
        if inj is not None:
            out[label] = {
                "coupling_mode": inj.coupling_mode,
                "scalar_amplitude": inj.scalar_amplitude,
                "f_min": inj.f_min,
                "f_min_radius": inj.f_min_radius,
                "metric_positive": inj.metric_positive,
                "defect_fraction": inj.defect_fraction,
                "notes": inj.notes,
            }

    if result.lambda_scan is not None:
        ls = result.lambda_scan
        out["lambda_scan"] = {
            "n_scanned": ls.n_scanned,
            "n_converged": ls.n_converged,
            "n_positive_A": ls.n_positive_A,
            "n_positive_B": ls.n_positive_B,
            "best_lambda_A": ls.best_lambda_A,
            "best_lambda_B": ls.best_lambda_B,
            "best_fmin_A": ls.best_fmin_A,
            "best_fmin_B": ls.best_fmin_B,
            "entries": [
                {
                    "lam": e.lam,
                    "converged": e.bvp_converged,
                    "core_peak": e.core_peak,
                    "tail_exponent": e.tail_exponent,
                    "f_min_A": e.f_min_case_A,
                    "f_min_B": e.f_min_case_B,
                    "positive_A": e.metric_positive_A,
                    "positive_B": e.metric_positive_B,
                    "defect_fraction_Req": e.defect_sigma_fraction_at_Req,
                }
                for e in ls.entries
            ],
            "notes": ls.notes,
        }

    if result.compatibility is not None:
        out["compatibility"] = {
            "component_A_intact": result.compatibility.component_A_intact,
            "coupling_additive": result.compatibility.coupling_is_additive,
            "locked_ok": result.compatibility.locked_results_preserved,
            "defect_B_shape": result.compatibility.defect_provides_component_B_shape,
            "notes": result.compatibility.notes,
        }

    if result.classification is not None:
        cl = result.classification
        out["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "positive_A": cl.metric_positive_case_A,
            "positive_B": cl.metric_positive_case_B,
            "best_fmin_A": cl.best_fmin_A,
            "best_fmin_B": cl.best_fmin_B,
            "phase_lock_update": cl.phase_lock_update,
            "summary": cl.summary,
        }

    out["nonclaims"] = result.nonclaims
    out["assumptions"] = result.assumptions
    out["diagnostics"] = result.diagnostics

    return out
