"""Phase D1 — Defect-Sector Admissibility and Hedgehog ODE Derivation.

Formalizes the minimal symmetry-breaking defect sector that could generate
the missing Component B support with asymptotic scaling epsilon_B ~ 1/r^2.

This is a CANDIDATE EXTENSION program, not locked canon.

PRINCIPAL RESULTS:

  Result 1 — Field-Content Admissibility:
    A single real scalar has pi_2(R) = 0 and cannot support topological
    defects in 3D.  A complex scalar has pi_2(S^1) = 0.  An O(3) triplet
    has vacuum manifold S^2 with pi_2(S^2) = Z, supporting monopole/hedgehog
    configurations.  The O(3) triplet is the minimal admissible field content.

  Result 2 — Symmetry-Breaking Potential:
    V(Phi) = -(1/2) mu^2 |Phi|^2 + (1/4) lambda |Phi|^4
    Vacuum expectation scale: eta = mu / sqrt(lambda)
    eta is a symmetry-breaking amplitude scale, NOT a literal charge.

  Result 3 — Hedgehog Ansatz and Radial ODE:
    Phi_a(r) = eta * f(r) * x_hat_a
    ODE: f'' + (2/r) f' - (2/r^2) f - lambda*eta^2 * f(f^2 - 1) = 0
    BCs: f(0) = 0, f(infinity) = 1

  Result 4 — Energy-Density Decomposition:
    epsilon(r) = (1/2) eta^2 (f')^2     [radial kinetic / core]
              +  eta^2 f^2 / r^2         [angular gradient / topological]
              + (1/4) lambda eta^4 (f^2-1)^2  [potential]

  Result 5 — Asymptotic Component B Proof:
    As f -> 1, f' -> 0:
    epsilon(r) -> eta^2 / r^2
    The tail coefficient matches Component B if eta^2 = 1/(8*pi).
    This is a shape-and-normalization matching condition, not yet a
    derived physical identification.

  Result 6 — Classification:
    provisional_candidate_extension_formulated

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants — canonical GRUT parameters
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ_OVER_RS = ALPHA_VAC
R_EQ = R_S * R_EQ_OVER_RS           # = 1/3
C_COMPACTNESS = R_S / R_EQ          # = 3
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)  # ~ 1.2247

# Phase 6/6B/6C locked values
A_CRIT = 1.062
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
COMP_B_COEFF = 1.0 / (8.0 * math.pi)   # ~ 0.03979
PHI_GOLDEN = (1.0 + math.sqrt(5.0)) / 2.0  # ~ 1.618

# Defect-sector specific
N_FIELD_CANDIDATES = 3
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)  # ~ 0.1995
MU_DEFAULT = 1.0
LAMBDA_DEFAULT = MU_DEFAULT ** 2 / (ETA_TARGET ** 2)
# = 8 * pi ~ 25.13
COMPONENT_B_TARGET_EXPONENT = -2.0
DELTA_CORE = 1.0  # default core width for analytic profile


# ================================================================
# Assumptions — explicitly documented
# ================================================================

DEFECT_ASSUMPTIONS = [
    "1. The candidate extension seeks a topological defect sector whose "
    "energy-density tail scales as eta^2/r^2, matching the shape of "
    "Component B from the interior deficit program (Phase 6C).",

    "2. Topological admissibility requires non-trivial pi_2(M) where M "
    "is the vacuum manifold.  This is the standard homotopy criterion "
    "for monopole-type defects in 3 spatial dimensions.",

    "3. The O(3) triplet with Mexican-hat potential V = -(1/2)mu^2|Phi|^2 "
    "+ (1/4)lambda|Phi|^4 is the minimal field content satisfying this "
    "criterion, with vacuum manifold S^2 and pi_2(S^2) = Z.",

    "4. The symmetry-breaking scale eta = mu/sqrt(lambda) is an amplitude "
    "scale, NOT a literal electric or gauge charge.  No gauge field is "
    "introduced in this phase.",

    "5. The hedgehog ansatz Phi_a = eta * f(r) * x_hat_a is the standard "
    "spherically symmetric monopole configuration for an O(3) triplet.",

    "6. The energy-density decomposition into radial kinetic, angular "
    "gradient, and potential terms follows from the standard minimally "
    "coupled scalar Lagrangian (1/2)(partial Phi_a)^2 - V.",

    "7. The analytic interpolating profile f(r) = r/sqrt(r^2 + delta^2) "
    "is used as the primary D1 vehicle.  It has the correct core behavior "
    "f(0)=0 and asymptotic limit f(inf)=1.  Full shooting integration "
    "is deferred to Phase D2.",

    "8. The asymptotic tail eta^2/r^2 is exact in the f->1 limit and "
    "does not depend on the core solution or the ODE approximation.",

    "9. The background metric is held fixed (Schwarzschild or GRUT "
    "interior).  No back-reaction from the defect sector is computed.",

    "10. This phase formulates a candidate extension only.  Physical "
    "viability and GRUT compatibility remain open pending Phase D2.",
]


# ================================================================
# Nonclaims — what this phase does NOT prove
# ================================================================

DEFECT_NONCLAIMS = [
    "1. This phase does NOT prove the final particle sector of the theory.",

    "2. This phase does NOT derive the defect from the already-locked "
    "GRUT core.  The triplet is introduced as a candidate extension.",

    "3. This phase does NOT show that the defect restores the metric "
    "by itself.  It only proves shape compatibility of the tail.",

    "4. This phase does NOT identify eta with a literal electric charge "
    "or any gauge coupling constant.",

    "5. This phase does NOT justify metaphysical, observer-based, or "
    "consciousness-related interpretations.",

    "6. This phase only formulates a mathematically explicit candidate "
    "extension and proves its asymptotic shape compatibility with "
    "Component B.",

    "7. The coefficient-matching condition eta^2 = 1/(8*pi) is a "
    "normalization requirement, not a derived physical identification.",

    "8. The analytic interpolating profile is an approximation.  The "
    "true solution requires shooting integration (deferred to D2).",

    "9. The compatibility inventory is not exhaustive.  Additional "
    "questions may emerge during Phase D2 implementation.",

    "10. The classification 'provisional_candidate_extension_formulated' "
    "means the extension is mathematically formulated and shape-compatible, "
    "but NOT yet physically viable or GRUT-integrated.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class DefectAdmissibilityParams:
    """Module parameters."""
    mu: float = MU_DEFAULT
    lam: float = LAMBDA_DEFAULT  # 'lambda' is reserved in Python
    eta: float = ETA_TARGET
    delta_core: float = DELTA_CORE
    r_min: float = 0.01
    r_max: float = 50.0
    n_radial: int = 500
    component_B_target: float = COMP_B_COEFF


@dataclass
class FieldCandidate:
    """One field-content candidate."""
    name: str
    field_type: str
    n_components: int
    vacuum_manifold: str
    pi_2: str  # homotopy group pi_2(M)
    supports_monopole: bool
    notes: str


@dataclass
class FieldContentAssessment:
    """Assessment of minimal field content for monopole-type defect."""
    candidates: List[FieldCandidate]
    n_candidates: int
    selected_name: str
    selected_reason: str
    minimal_n_components: int


@dataclass
class SymmetryBreakingPotential:
    """Mexican-hat / SSB potential definition."""
    formula: str
    mu: float
    lam: float
    eta: float  # = mu / sqrt(lambda)
    eta_squared: float
    vacuum_manifold: str
    potential_at_minimum: float  # V(eta) = -mu^4 / (4*lambda)
    notes: List[str]


@dataclass
class HedgehogAnsatz:
    """Hedgehog configuration definition."""
    ansatz_formula: str
    gradient_radial: str  # (df/dr) * x_hat_a * x_hat_i component
    gradient_angular: str  # (f/r) * (delta_ai - x_hat_a * x_hat_i)
    gradient_squared: str  # (df/dr)^2 + 2*f^2/r^2
    n_components: int
    boundary_conditions: Dict[str, float]
    notes: List[str]


@dataclass
class HedgehogODE:
    """Hedgehog radial ODE: f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f(f^2-1) = 0."""
    ode_formula: str
    # Coefficients in standard form: f'' + A(r)*f' + B(r)*f + N(f,r) = 0
    coefficient_f_prime: str  # "2/r"
    coefficient_f: str        # "-2/r^2"
    nonlinear_term: str       # "-lam*eta^2*f*(f^2-1)"
    bc_origin: float  # f(0) = 0
    bc_infinity: float  # f(inf) = 1
    # Analytic interpolating profile
    analytic_profile_formula: str
    r_grid: np.ndarray
    f_analytic: np.ndarray
    f_prime_analytic: np.ndarray
    f_double_prime_analytic: np.ndarray
    ode_residual: np.ndarray  # how well the analytic profile satisfies the ODE
    max_residual: float
    notes: List[str]


@dataclass
class EnergyDecomposition:
    """Energy density decomposed into 3 terms."""
    r_grid: np.ndarray
    # Three terms
    radial_kinetic: np.ndarray   # (1/2) * eta^2 * (f')^2
    angular_gradient: np.ndarray  # eta^2 * f^2 / r^2
    potential_term: np.ndarray    # (1/4) * lam * eta^4 * (f^2 - 1)^2
    # Total
    total_epsilon: np.ndarray
    # Asymptotic behavior
    tail_exponent: float  # fitted exponent of total epsilon at large r
    angular_fraction_at_large_r: float  # fraction from angular term
    notes: List[str]


@dataclass
class AsymptoticTailProof:
    """Proof that the hedgehog tail gives eta^2/r^2."""
    # Asymptotic analysis
    f_limit: float  # f -> 1
    f_prime_limit: float  # f' -> 0
    surviving_term: str  # "eta^2 / r^2"
    surviving_coefficient: float  # eta^2
    target_coefficient: float  # 1/(8*pi)
    coefficient_match: bool  # eta^2 == 1/(8*pi)?
    # Numerical verification
    fitted_exponent: float  # from log-log fit at large r
    exponent_deviation: float  # |fitted - (-2.0)|
    # Ratio test: epsilon(r) * r^2 should -> eta^2
    ratio_at_large_r: float  # epsilon(r_max) * r_max^2
    ratio_target: float  # eta^2
    ratio_match: bool  # |ratio - eta^2| < tolerance
    shape_compatible: bool
    notes: List[str]


@dataclass
class CompatibilityQuestion:
    """One compatibility question for Phase D2."""
    question_id: int
    category: str
    question: str
    severity: str  # "high", "medium", "low"
    deferred_to: str  # "Phase D2"


@dataclass
class CompatibilityInventory:
    """Inventory of unresolved questions for Phase D2."""
    questions: List[CompatibilityQuestion]
    n_questions: int
    n_high_severity: int
    n_medium_severity: int


@dataclass
class DefectAdmissibilityClassification:
    """Final classification."""
    classification: str
    phase_status: str
    shape_compatible: bool
    coefficient_matching_eta_squared: float
    n_compatibility_questions: int
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class DefectAdmissibilityResult:
    """Master result container."""
    valid: bool
    params: DefectAdmissibilityParams
    field_content: Optional[FieldContentAssessment] = None
    potential: Optional[SymmetryBreakingPotential] = None
    ansatz: Optional[HedgehogAnsatz] = None
    ode: Optional[HedgehogODE] = None
    energy: Optional[EnergyDecomposition] = None
    tail_proof: Optional[AsymptoticTailProof] = None
    compatibility: Optional[CompatibilityInventory] = None
    classification: Optional[DefectAdmissibilityClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Helper functions
# ================================================================

def make_radial_grid(params: DefectAdmissibilityParams) -> np.ndarray:
    """Create logarithmically-spaced radial grid."""
    return np.logspace(
        np.log10(params.r_min), np.log10(params.r_max), params.n_radial
    )


def _fit_spatial_exponent(r: np.ndarray, y: np.ndarray) -> float:
    """Fit power-law exponent via log-log regression."""
    mask = (y > 0) & np.isfinite(y)
    if np.sum(mask) < 3:
        return float("nan")
    log_r = np.log(r[mask])
    log_y = np.log(y[mask])
    n = len(log_r)
    sx = np.sum(log_r)
    sy = np.sum(log_y)
    sxx = np.sum(log_r ** 2)
    sxy = np.sum(log_r * log_y)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return float("nan")
    b = (n * sxy - sx * sy) / denom
    return float(b)


def _analytic_f(r: np.ndarray, delta: float) -> np.ndarray:
    """Analytic interpolating profile: f(r) = r / sqrt(r^2 + delta^2)."""
    return r / np.sqrt(r ** 2 + delta ** 2)


def _analytic_f_prime(r: np.ndarray, delta: float) -> np.ndarray:
    """Derivative: f'(r) = delta^2 / (r^2 + delta^2)^{3/2}."""
    return delta ** 2 / (r ** 2 + delta ** 2) ** 1.5


def _analytic_f_double_prime(r: np.ndarray, delta: float) -> np.ndarray:
    """Second derivative: f''(r) = -3 * r * delta^2 / (r^2 + delta^2)^{5/2}."""
    return -3.0 * r * delta ** 2 / (r ** 2 + delta ** 2) ** 2.5


# ================================================================
# Level 1: Field-Content Admissibility
# ================================================================

def assess_field_content() -> FieldContentAssessment:
    """Assess minimal field content for monopole-type defect.

    Criterion: pi_2(M) must be non-trivial for the vacuum manifold M
    to support point-like topological defects (monopoles) in 3D.

    Candidates:
      1. Single real scalar: vacuum manifold = {+eta, -eta} (discrete)
         -> pi_2 = 0.  No monopole.
      2. Complex scalar: vacuum manifold = S^1
         -> pi_2(S^1) = 0.  No monopole.  (Supports vortices via pi_1.)
      3. Real O(3) triplet: vacuum manifold = S^2
         -> pi_2(S^2) = Z.  SUPPORTS monopole/hedgehog.
    """
    candidates = [
        FieldCandidate(
            name="real_scalar",
            field_type="single real scalar",
            n_components=1,
            vacuum_manifold="{+eta, -eta} (discrete Z_2)",
            pi_2="pi_2 = 0 (trivial, discrete manifold)",
            supports_monopole=False,
            notes=(
                "A single real scalar with SSB has a discrete vacuum "
                "manifold.  It supports domain walls (pi_0 non-trivial) "
                "but NOT monopoles."
            ),
        ),
        FieldCandidate(
            name="complex_scalar",
            field_type="complex scalar (2 real components)",
            n_components=2,
            vacuum_manifold="S^1 (circle of degenerate vacua)",
            pi_2="pi_2(S^1) = 0",
            supports_monopole=False,
            notes=(
                "A complex scalar with SSB has vacuum manifold S^1.  "
                "It supports vortices/strings via pi_1(S^1) = Z, "
                "but NOT monopoles (pi_2 = 0)."
            ),
        ),
        FieldCandidate(
            name="O3_triplet",
            field_type="real O(3) triplet (3 real components)",
            n_components=3,
            vacuum_manifold="S^2 (2-sphere of degenerate vacua)",
            pi_2="pi_2(S^2) = Z",
            supports_monopole=True,
            notes=(
                "An O(3) triplet with SSB has vacuum manifold S^2.  "
                "pi_2(S^2) = Z supports monopole/hedgehog configurations "
                "classified by integer winding number.  This is the "
                "minimal field content for the desired defect class."
            ),
        ),
    ]

    return FieldContentAssessment(
        candidates=candidates,
        n_candidates=N_FIELD_CANDIDATES,
        selected_name="O3_triplet",
        selected_reason=(
            "O(3) triplet is the minimal field content with non-trivial "
            "pi_2, required for monopole-type defects in 3 spatial "
            "dimensions.  Vacuum manifold S^2 with pi_2(S^2) = Z."
        ),
        minimal_n_components=3,
    )


# ================================================================
# Level 2: Symmetry-Breaking Potential
# ================================================================

def define_ssb_potential(
    params: DefectAdmissibilityParams,
) -> SymmetryBreakingPotential:
    """Define the Mexican-hat SSB potential.

    V(Phi) = -(1/2) mu^2 |Phi|^2 + (1/4) lambda |Phi|^4

    Vacuum expectation scale: eta = mu / sqrt(lambda)
    This is a symmetry-breaking amplitude, NOT a literal charge.
    """
    mu = params.mu
    lam = params.lam
    eta = mu / math.sqrt(lam)  # should match params.eta
    V_min = -mu ** 4 / (4.0 * lam)

    notes = [
        f"mu = {mu:.6f}",
        f"lambda = {lam:.6f}",
        f"eta = mu/sqrt(lambda) = {eta:.6f}",
        f"eta^2 = {eta**2:.6f}",
        f"V(eta) = -mu^4/(4*lambda) = {V_min:.6f}",
        "eta is a symmetry-breaking amplitude scale, NOT a charge",
        f"Component B matching requires eta^2 = 1/(8*pi) = {COMP_B_COEFF:.6f}",
    ]

    return SymmetryBreakingPotential(
        formula="V(Phi) = -(1/2) mu^2 |Phi|^2 + (1/4) lambda |Phi|^4",
        mu=mu,
        lam=lam,
        eta=eta,
        eta_squared=eta ** 2,
        vacuum_manifold="S^2 (|Phi| = eta, direction free)",
        potential_at_minimum=V_min,
        notes=notes,
    )


# ================================================================
# Level 3: Hedgehog Ansatz
# ================================================================

def define_hedgehog_ansatz(
    params: DefectAdmissibilityParams,
) -> HedgehogAnsatz:
    """Define the hedgehog configuration.

    Phi_a(r) = eta * f(r) * x_hat_a

    where x_hat_a = x_a / r is the unit radial vector.

    Gradient decomposition:
        partial_i Phi_a = eta * [f'(r) * x_hat_i * x_hat_a
                                + (f(r)/r) * (delta_{ia} - x_hat_i * x_hat_a)]

    (partial Phi)^2 = eta^2 * [(f')^2 + 2*f^2/r^2]

    The first term is radial kinetic; the second is angular gradient
    (the topological contribution).
    """
    return HedgehogAnsatz(
        ansatz_formula="Phi_a(r) = eta * f(r) * x_hat_a",
        gradient_radial="eta * f'(r) * x_hat_i * x_hat_a",
        gradient_angular="eta * (f/r) * (delta_{ia} - x_hat_i * x_hat_a)",
        gradient_squared="eta^2 * [(f')^2 + 2 * f^2 / r^2]",
        n_components=3,
        boundary_conditions={"f(0)": 0.0, "f(infinity)": 1.0},
        notes=[
            "x_hat_a = x_a / r is the unit radial vector",
            "The radial part f'(r) carries core / kinetic energy",
            "The angular part f/r carries topological / gradient energy",
            "At large r, f -> 1 and the angular term -> eta^2/r^2",
        ],
    )


# ================================================================
# Level 4: Hedgehog ODE (with analytic profile)
# ================================================================

def derive_hedgehog_ode(
    params: DefectAdmissibilityParams,
) -> HedgehogODE:
    """Derive and evaluate the hedgehog radial ODE.

    Derivation from Euler-Lagrange equations:

    The energy functional is:
        E = 4*pi * integral dr r^2 [
            (1/2)*eta^2*(f')^2 + eta^2*f^2/r^2 + V(f)
        ]

    where V(f) = (1/4)*lam*eta^4*(f^2 - 1)^2.

    The integrand (including the r^2 measure) is:
        L = (1/2)*eta^2*r^2*(f')^2 + eta^2*f^2 + (1/4)*lam*eta^4*r^2*(f^2-1)^2

    Euler-Lagrange: d/dr[dL/df'] - dL/df = 0

        dL/df' = eta^2 * r^2 * f'
        d/dr[...] = eta^2 * [2*r*f' + r^2*f''] = eta^2 * r^2 * [f'' + (2/r)*f']

        dL/df = 2*eta^2*f + lam*eta^4*r^2*f*(f^2-1)
                (using d/df[(f^2-1)^2] = 4*f*(f^2-1), times 1/4 gives f*(f^2-1))

    Setting d/dr[dL/df'] = dL/df:
        eta^2*r^2*[f'' + (2/r)*f'] = 2*eta^2*f + lam*eta^4*r^2*f*(f^2-1)

    Dividing by eta^2 * r^2:
        f'' + (2/r)*f' - (2/r^2)*f - lam*eta^2*f*(f^2-1) = 0

    This is the hedgehog radial ODE.
    """
    r = make_radial_grid(params)
    delta = params.delta_core
    eta = params.eta
    lam = params.lam

    # Analytic interpolating profile
    f = _analytic_f(r, delta)
    fp = _analytic_f_prime(r, delta)
    fpp = _analytic_f_double_prime(r, delta)

    # ODE residual: f'' + (2/r)*f' - (2/r^2)*f - lam*eta^2*f*(f^2-1)
    residual = fpp + (2.0 / r) * fp - (2.0 / r ** 2) * f - lam * eta ** 2 * f * (f ** 2 - 1.0)
    max_res = float(np.max(np.abs(residual)))

    notes = [
        "ODE derived from Euler-Lagrange of hedgehog energy functional",
        f"Analytic profile: f(r) = r/sqrt(r^2 + delta^2), delta = {delta}",
        f"Max ODE residual: {max_res:.6e}",
        "Full shooting integration deferred to Phase D2",
        "Boundary conditions: f(0) = 0, f(inf) = 1",
        f"f(r_min={params.r_min:.2f}) = {f[0]:.6f}",
        f"f(r_max={params.r_max:.1f}) = {f[-1]:.6f}",
    ]

    return HedgehogODE(
        ode_formula="f'' + (2/r)*f' - (2/r^2)*f - lam*eta^2*f*(f^2-1) = 0",
        coefficient_f_prime="2/r",
        coefficient_f="-2/r^2",
        nonlinear_term="-lam*eta^2*f*(f^2-1)",
        bc_origin=0.0,
        bc_infinity=1.0,
        analytic_profile_formula="f(r) = r / sqrt(r^2 + delta^2)",
        r_grid=r,
        f_analytic=f,
        f_prime_analytic=fp,
        f_double_prime_analytic=fpp,
        ode_residual=residual,
        max_residual=max_res,
        notes=notes,
    )


# ================================================================
# Level 5: Energy Decomposition
# ================================================================

def decompose_energy(
    ode: HedgehogODE,
    params: DefectAdmissibilityParams,
) -> EnergyDecomposition:
    """Decompose energy density into 3 terms.

    epsilon(r) = (1/2)*eta^2*(f')^2          [radial kinetic / core]
              +  eta^2*f^2/r^2               [angular gradient / topological]
              + (1/4)*lam*eta^4*(f^2-1)^2    [potential]
    """
    r = ode.r_grid
    f = ode.f_analytic
    fp = ode.f_prime_analytic
    eta = params.eta
    lam = params.lam

    # Three terms
    radial_kinetic = 0.5 * eta ** 2 * fp ** 2
    angular_gradient = eta ** 2 * f ** 2 / r ** 2
    potential = 0.25 * lam * eta ** 4 * (f ** 2 - 1.0) ** 2

    total = radial_kinetic + angular_gradient + potential

    # Fit exponent at large r (outer half of grid)
    n = len(r)
    outer_r = r[3 * n // 4:]
    outer_eps = total[3 * n // 4:]
    tail_exp = _fit_spatial_exponent(outer_r, outer_eps)

    # Angular fraction at large r
    ang_outer = angular_gradient[3 * n // 4:]
    total_outer = total[3 * n // 4:]
    ang_frac = float(np.mean(ang_outer / total_outer))

    notes = [
        "Radial kinetic: (1/2)*eta^2*(f')^2 — concentrated at core",
        "Angular gradient: eta^2*f^2/r^2 — topological tail",
        "Potential: (1/4)*lam*eta^4*(f^2-1)^2 — concentrated at core",
        f"Tail exponent (outer quarter): {tail_exp:.4f}",
        f"Angular fraction at large r: {ang_frac:.4f}",
        "At large r, angular gradient dominates -> eta^2/r^2",
    ]

    return EnergyDecomposition(
        r_grid=r,
        radial_kinetic=radial_kinetic,
        angular_gradient=angular_gradient,
        potential_term=potential,
        total_epsilon=total,
        tail_exponent=tail_exp,
        angular_fraction_at_large_r=ang_frac,
        notes=notes,
    )


# ================================================================
# Level 6: Asymptotic Tail Proof
# ================================================================

def prove_asymptotic_tail(
    energy: EnergyDecomposition,
    params: DefectAdmissibilityParams,
) -> AsymptoticTailProof:
    """Prove that the hedgehog tail gives eta^2/r^2.

    Asymptotic analysis (f -> 1, f' -> 0):
      - radial kinetic: (1/2)*eta^2*(f')^2 -> 0
      - angular gradient: eta^2*f^2/r^2 -> eta^2/r^2
      - potential: (1/4)*lam*eta^4*(f^2-1)^2 -> 0

    Surviving term: eta^2 / r^2

    Coefficient-matching condition:
      eta^2 = 1/(8*pi) matches Component B = 1/(8*pi*r^2)
    """
    r = energy.r_grid
    eta = params.eta
    total = energy.total_epsilon

    # Fit exponent at large r
    n = len(r)
    outer_r = r[3 * n // 4:]
    outer_eps = total[3 * n // 4:]
    fitted_exp = _fit_spatial_exponent(outer_r, outer_eps)
    exp_dev = abs(fitted_exp - COMPONENT_B_TARGET_EXPONENT)

    # Ratio test: epsilon(r) * r^2 should approach eta^2 at large r
    ratio = total[-1] * r[-1] ** 2
    ratio_target = eta ** 2
    ratio_ok = abs(ratio - ratio_target) / ratio_target < 0.01

    # Coefficient match
    coeff_match = abs(eta ** 2 - COMP_B_COEFF) / COMP_B_COEFF < 0.01

    # Shape compatible if exponent is close to -2.0
    shape_ok = exp_dev < 0.05

    notes = [
        f"f -> 1 at large r: f(r_max) = {_analytic_f(np.array([params.r_max]), params.delta_core)[0]:.8f}",
        f"f' -> 0 at large r: f'(r_max) = {_analytic_f_prime(np.array([params.r_max]), params.delta_core)[0]:.2e}",
        f"Surviving term: eta^2/r^2 = {eta**2:.6f}/r^2",
        f"Fitted tail exponent: {fitted_exp:.6f} (target: -2.0)",
        f"Exponent deviation: {exp_dev:.6e}",
        f"Ratio test: epsilon*r^2 at r_max = {ratio:.6f} (target: eta^2 = {ratio_target:.6f})",
        f"Coefficient match (eta^2 = 1/(8*pi)): {coeff_match}",
        "This is a shape-and-normalization matching condition, "
        "not yet a derived physical identification.",
    ]

    return AsymptoticTailProof(
        f_limit=1.0,
        f_prime_limit=0.0,
        surviving_term="eta^2 / r^2",
        surviving_coefficient=eta ** 2,
        target_coefficient=COMP_B_COEFF,
        coefficient_match=coeff_match,
        fitted_exponent=fitted_exp,
        exponent_deviation=exp_dev,
        ratio_at_large_r=ratio,
        ratio_target=ratio_target,
        ratio_match=ratio_ok,
        shape_compatible=shape_ok,
        notes=notes,
    )


# ================================================================
# Level 7: Compatibility Inventory
# ================================================================

def build_compatibility_inventory() -> CompatibilityInventory:
    """Build inventory of unresolved questions for Phase D2."""
    questions = [
        CompatibilityQuestion(
            question_id=1,
            category="core_regularity",
            question=(
                "Does the monopole core energy remain integrable and "
                "numerically manageable near r = 0?  Is the core "
                "compatible with the TOV-style integrator used in the "
                "GRUT interior program?"
            ),
            severity="high",
            deferred_to="Phase D2",
        ),
        CompatibilityQuestion(
            question_id=2,
            category="grut_coupling",
            question=(
                "How does the triplet defect sector couple to the "
                "existing GRUT source law and Einstein equations?  "
                "Is the coupling additive (T^total = T^memory + T^defect), "
                "replacement (T^total = T^defect), or hybrid?"
            ),
            severity="high",
            deferred_to="Phase D2",
        ),
        CompatibilityQuestion(
            question_id=3,
            category="locked_results",
            question=(
                "Does this extension leave Component A (1/r^4 from "
                "scalar memory) intact?  Does it destabilize previously "
                "locked classical structures (Phase 6, 6B, 6C)?"
            ),
            severity="high",
            deferred_to="Phase D2",
        ),
        CompatibilityQuestion(
            question_id=4,
            category="scalar_memory_relation",
            question=(
                "What is the relation between the O(3) triplet defect "
                "field and the original GRUT scalar-memory field Phi?  "
                "Is the triplet: (a) a replacement of the scalar, "
                "(b) an embedding (scalar as one component), "
                "(c) a companion sector coupled to the scalar, or "
                "(d) a next-sector extension with independent dynamics?  "
                "This is the major conceptual hinge for GRUT integration."
            ),
            severity="high",
            deferred_to="Phase D2",
        ),
        CompatibilityQuestion(
            question_id=5,
            category="physical_viability",
            question=(
                "Is the candidate merely shape-compatible, or is it "
                "dynamically viable?  What must be solved numerically "
                "in Phase D2 to decide?  Specifically: (a) full shooting "
                "solution of the hedgehog ODE, (b) integrated energy "
                "and mass profile, (c) self-consistent Einstein-defect "
                "system."
            ),
            severity="medium",
            deferred_to="Phase D2",
        ),
        CompatibilityQuestion(
            question_id=6,
            category="interpretation",
            question=(
                "What physical interpretation does the symmetry-breaking "
                "scale eta carry?  Is it a fundamental constant, a "
                "derived scale from GRUT parameters, or a new free "
                "parameter?  Can eta be related to existing GRUT "
                "constants (tau, M, alpha_vac) through a consistency "
                "condition?"
            ),
            severity="medium",
            deferred_to="Phase D2",
        ),
    ]

    n_high = sum(1 for q in questions if q.severity == "high")
    n_med = sum(1 for q in questions if q.severity == "medium")

    return CompatibilityInventory(
        questions=questions,
        n_questions=len(questions),
        n_high_severity=n_high,
        n_medium_severity=n_med,
    )


# ================================================================
# Level 8: Classification
# ================================================================

def classify_defect_admissibility(
    tail: AsymptoticTailProof,
    inventory: CompatibilityInventory,
) -> DefectAdmissibilityClassification:
    """Classify the defect-sector admissibility result."""
    classification = "provisional_candidate_extension_formulated"
    phase_status = "formulated"

    phase_lock = {
        "phase_6_f_at_req": "LOCKED (-17.71)",
        "phase_6b_A_crit": "LOCKED (1.062)",
        "phase_6c_deficit": "LOCKED (Component A + Component B)",
        "route_c_markov": "LOCKED (insufficient, 1/r^4)",
        "route_b_all_channels": "LOCKED (closed within Galley CTP)",
        "route_c_nonmarkov": "LOCKED (source profile locking, 1/r^4)",
        "source_law_program": "LOCKED (partially viable, no GRUT-native mechanism)",
        "defect_sector_D1": f"FORMULATED ({classification})",
    }

    summary = (
        f"Phase D1 complete.  The O(3) triplet with SSB potential and "
        f"hedgehog ansatz produces an energy-density tail eta^2/r^2 "
        f"that is shape-compatible with Component B.  "
        f"Coefficient-matching requires eta^2 = 1/(8*pi).  "
        f"{inventory.n_questions} compatibility questions deferred to D2 "
        f"({inventory.n_high_severity} high severity).  "
        f"Classification: {classification}."
    )

    return DefectAdmissibilityClassification(
        classification=classification,
        phase_status=phase_status,
        shape_compatible=tail.shape_compatible,
        coefficient_matching_eta_squared=tail.surviving_coefficient,
        n_compatibility_questions=inventory.n_questions,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 9: Master Function
# ================================================================

def compute_defect_admissibility(
    params: Optional[DefectAdmissibilityParams] = None,
) -> DefectAdmissibilityResult:
    """Master function: run the complete Phase D1 assessment.

    Steps:
        1. Assess field-content admissibility (homotopy scan)
        2. Define SSB potential and eta
        3. Define hedgehog ansatz
        4. Derive hedgehog ODE (with analytic profile)
        5. Decompose energy density into 3 terms
        6. Prove asymptotic 1/r^2 tail
        7. Build compatibility inventory for Phase D2
        8. Classify
    """
    if params is None:
        params = DefectAdmissibilityParams()

    result = DefectAdmissibilityResult(valid=False, params=params)

    try:
        # Step 1
        result.field_content = assess_field_content()

        # Step 2
        result.potential = define_ssb_potential(params)

        # Step 3
        result.ansatz = define_hedgehog_ansatz(params)

        # Step 4
        result.ode = derive_hedgehog_ode(params)

        # Step 5
        result.energy = decompose_energy(result.ode, params)

        # Step 6
        result.tail_proof = prove_asymptotic_tail(result.energy, params)

        # Step 7
        result.compatibility = build_compatibility_inventory()

        # Step 8
        result.classification = classify_defect_admissibility(
            result.tail_proof, result.compatibility,
        )

        # Metadata
        result.nonclaims = list(DEFECT_NONCLAIMS)
        result.assumptions = list(DEFECT_ASSUMPTIONS)
        result.diagnostics = {
            "selected_field": result.field_content.selected_name,
            "eta": params.eta,
            "eta_squared": params.eta ** 2,
            "comp_B_coeff": COMP_B_COEFF,
            "tail_exponent": result.tail_proof.fitted_exponent,
            "shape_compatible": result.tail_proof.shape_compatible,
            "coefficient_match": result.tail_proof.coefficient_match,
            "max_ode_residual": result.ode.max_residual,
            "n_compatibility_questions": result.compatibility.n_questions,
            "classification": result.classification.classification,
        }
        result.valid = True

    except Exception as exc:
        result.diagnostics["error"] = str(exc)

    return result


# ================================================================
# Level 10: Serialization
# ================================================================

def defect_admissibility_result_to_dict(
    result: DefectAdmissibilityResult,
) -> Dict[str, Any]:
    """Serialize DefectAdmissibilityResult to JSON-safe dictionary."""
    out: Dict[str, Any] = {"valid": result.valid}

    # Params
    out["params"] = {
        "mu": result.params.mu,
        "lam": result.params.lam,
        "eta": result.params.eta,
        "delta_core": result.params.delta_core,
        "r_min": result.params.r_min,
        "r_max": result.params.r_max,
        "n_radial": result.params.n_radial,
    }

    # Field content
    if result.field_content is not None:
        fc = result.field_content
        out["field_content"] = {
            "n_candidates": fc.n_candidates,
            "selected_name": fc.selected_name,
            "selected_reason": fc.selected_reason,
            "minimal_n_components": fc.minimal_n_components,
            "candidates": [
                {
                    "name": c.name,
                    "field_type": c.field_type,
                    "n_components": c.n_components,
                    "vacuum_manifold": c.vacuum_manifold,
                    "pi_2": c.pi_2,
                    "supports_monopole": c.supports_monopole,
                }
                for c in fc.candidates
            ],
        }

    # Potential
    if result.potential is not None:
        p = result.potential
        out["potential"] = {
            "formula": p.formula,
            "mu": p.mu,
            "lam": p.lam,
            "eta": p.eta,
            "eta_squared": p.eta_squared,
            "vacuum_manifold": p.vacuum_manifold,
            "potential_at_minimum": p.potential_at_minimum,
            "notes": p.notes,
        }

    # Ansatz
    if result.ansatz is not None:
        a = result.ansatz
        out["ansatz"] = {
            "ansatz_formula": a.ansatz_formula,
            "gradient_squared": a.gradient_squared,
            "n_components": a.n_components,
            "boundary_conditions": a.boundary_conditions,
        }

    # ODE
    if result.ode is not None:
        o = result.ode
        out["ode"] = {
            "ode_formula": o.ode_formula,
            "coefficient_f_prime": o.coefficient_f_prime,
            "coefficient_f": o.coefficient_f,
            "nonlinear_term": o.nonlinear_term,
            "bc_origin": o.bc_origin,
            "bc_infinity": o.bc_infinity,
            "analytic_profile_formula": o.analytic_profile_formula,
            "max_residual": o.max_residual,
            "f_at_rmin": float(o.f_analytic[0]),
            "f_at_rmax": float(o.f_analytic[-1]),
            "notes": o.notes,
        }

    # Energy decomposition
    if result.energy is not None:
        e = result.energy
        out["energy"] = {
            "tail_exponent": e.tail_exponent,
            "angular_fraction_at_large_r": e.angular_fraction_at_large_r,
            "notes": e.notes,
        }

    # Tail proof
    if result.tail_proof is not None:
        t = result.tail_proof
        out["tail_proof"] = {
            "surviving_term": t.surviving_term,
            "surviving_coefficient": t.surviving_coefficient,
            "target_coefficient": t.target_coefficient,
            "coefficient_match": t.coefficient_match,
            "fitted_exponent": t.fitted_exponent,
            "exponent_deviation": t.exponent_deviation,
            "ratio_at_large_r": t.ratio_at_large_r,
            "ratio_target": t.ratio_target,
            "ratio_match": t.ratio_match,
            "shape_compatible": t.shape_compatible,
            "notes": t.notes,
        }

    # Compatibility inventory
    if result.compatibility is not None:
        ci = result.compatibility
        out["compatibility"] = {
            "n_questions": ci.n_questions,
            "n_high_severity": ci.n_high_severity,
            "n_medium_severity": ci.n_medium_severity,
            "questions": [
                {
                    "id": q.question_id,
                    "category": q.category,
                    "question": q.question,
                    "severity": q.severity,
                    "deferred_to": q.deferred_to,
                }
                for q in ci.questions
            ],
        }

    # Classification
    if result.classification is not None:
        cl = result.classification
        out["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "shape_compatible": cl.shape_compatible,
            "coefficient_matching_eta_squared": cl.coefficient_matching_eta_squared,
            "n_compatibility_questions": cl.n_compatibility_questions,
            "phase_lock_update": cl.phase_lock_update,
            "summary": cl.summary,
        }

    out["nonclaims"] = result.nonclaims
    out["assumptions"] = result.assumptions
    out["diagnostics"] = result.diagnostics

    return out
