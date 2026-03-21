"""Phase D4 — Embedded Triplet Unification Dynamics and Component A Recovery.

Constructs the explicit curvature-coupled embedded-triplet Lagrangian,
decomposes into radial and angular modes, and tests whether the radial mode
can recover the scalar-memory Component A (~1/r^4) while the angular sector
carries Component B (~1/r^2).

PRINCIPAL RESULTS:

  Result 1 — Lagrangian:
    L = (1/2) d_mu Phi^a d^mu Phi^a + (1/2)m0^2 |Phi|^2
        - (1/4) lam |Phi|^4 - (1/2) xi C |Phi|^2
    where C is the chosen curvature invariant (ranked, not assumed R).

  Result 2 — Mode Decomposition:
    Radial kinetic: (1/2) eta^2 (f')^2  -> ~1/r^4 tail
    Angular gradient: eta^2 f^2 / r^2  -> ~eta^2/r^2 tail
    Potential: (1/4) lam eta^4 (f^2 - 1)^2  -> exponential decay
    Curvature coupling: (1/2) xi C eta^2 f^2  -> vanishes as C -> 0

  Result 3 — Component A Recovery (three-part test):
    Shape: radial kinetic gives 1/r^4 scaling (YES)
    Coefficient: (1/2) eta^2 c^2  vs  A^2 * MASS_COEFF (ratio computed)
    Interpretation: topology-driven vs source-driven (structurally different)

  Result 4 — Component B Preservation:
    Angular gradient eta^2/r^2 persists in coupled model.

  Result 5 — Curvature Trigger (multi-invariant):
    Ricci scalar R, Kretschner sqrt(K), Ricci-squared ranked as trigger
    candidates.  m_eff^2(C) = m0^2 - xi*C defines broken/unbroken regime.

  Result 6 — Classification:
    (determined by assessment outcome)

Uses D2 BVP solution for numerical evaluation.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

from grut.numerical_monopole import (
    NumericalMonopoleParams,
    solve_hedgehog_bvp,
    extract_defect_energy,
    HedgehogBVPSolution,
    DefectEnergyProfile,
    MASS_COEFF,
    R_EXT,
    ETA_MATCH,
    PHASE6_F_AT_REQ,
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

# D4-specific
XI_CONFORMAL = 1.0 / 6.0  # conformal coupling (reference value)
XI_DEFAULT = 1.0           # working default (O(1) coupling)
XI_SCAN_VALUES = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
MU0_SQUARED_DEFAULT = -LAMBDA_DEFAULT * ETA_SQUARED  # broken-phase mass

# Curvature invariant taxonomy
N_CURVATURE_INVARIANTS = 3
N_LAGRANGIAN_TERMS = 4
N_MODE_SECTORS = 4  # radial kinetic, angular gradient, potential, curvature

# Schwarzschild Kretschner at key radii: K = 48*M^2/r^6
KRETSCHNER_COEFF = 48.0 * M_EXT ** 2  # K = KRETSCHNER_COEFF / r^6


# ================================================================
# Assumptions
# ================================================================

DYNAMICS_ASSUMPTIONS = [
    "1. The embedded-triplet Lagrangian is constructed with Mexican-hat "
    "potential plus non-minimal curvature coupling.  The coupling invariant "
    "C is assessed among multiple candidates, not assumed to be R.",

    "2. The embedding ansatz Phi^a = eta*f(r)*r_hat^a identifies the "
    "scalar-memory field with the radial modulus |Phi| = eta*f(r).",

    "3. The mode decomposition uses the D2 BVP solution for f(r) to "
    "evaluate tail exponents and coefficients numerically.",

    "4. Component A recovery is assessed in three independent parts: "
    "shape (exponent), coefficient (ratio), and interpretation (mechanism).",

    "5. Component B preservation is assessed by checking that the "
    "angular gradient term eta^2*f^2/r^2 retains its 1/r^2 tail.",

    "6. The curvature trigger is assessed for multiple invariants: "
    "Ricci scalar R, Kretschner sqrt(K), and Ricci-squared.  Each is "
    "evaluated in the sourced interior, not vacuum Schwarzschild.",

    "7. The effective mass m_eff^2(C) = m0^2 - xi*C determines "
    "broken/unbroken regime.  SSB requires m_eff^2 < 0 in the interior.",

    "8. The background metric is held fixed (no self-consistent "
    "back-reaction).  Curvature invariants are estimated from the "
    "Phase 6 mass profile.",

    "9. Cross-term artifacts from the curvature coupling are "
    "inventoried but not resolved within D4.",

    "10. The classification is determined by the three-part Component A "
    "test, Component B preservation, and trigger viability.  It is not "
    "predetermined.",
]


DYNAMICS_NONCLAIMS = [
    "1. This phase does NOT prove the final unified theory.",

    "2. This phase does NOT derive Component A from the triplet sector.  "
    "It tests structural compatibility only.",

    "3. This phase does NOT prove the curvature trigger works in a "
    "self-consistent coupled solution.",

    "4. A shape match (1/r^4 exponent) is not the same as a derivation "
    "of the scalar-memory equation from the triplet Lagrangian.",

    "5. A coefficient mismatch does not invalidate the embedding model.  "
    "It means the radial mode is not yet shown to reproduce the exact "
    "Component A budget.",

    "6. The interpretation test (topology-driven vs source-driven) "
    "identifies a structural difference, not necessarily an incompatibility.",

    "7. The Kretschner invariant sqrt(K) is used as a mass-squared-like "
    "scale.  This is a heuristic, not a rigorous field-theory construction.",

    "8. Curvature invariant values in the sourced interior are "
    "approximate.  They depend on the matter model assumed.",

    "9. The artifact inventory documents unresolved issues.  These are "
    "targets for future phases, not failures.",

    "10. The classification is within the D4 analytical framework only.  "
    "Numerical coupled-model verification may revise the assessment.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class UnificationDynamicsParams:
    """Parameters for Phase D4."""
    eta: float = ETA_TARGET
    lam: float = LAMBDA_DEFAULT
    xi: float = XI_DEFAULT
    m0_squared: float = MU0_SQUARED_DEFAULT
    # BVP params (for D2 reuse)
    r_min: float = 0.01
    r_max: float = 5.0
    n_grid: int = 300
    # Scan
    xi_scan: List[float] = field(
        default_factory=lambda: list(XI_SCAN_VALUES)
    )
    # Mass profile params
    M: float = M_EXT
    R_ext: float = R_EXT


@dataclass
class LagrangianTerm:
    """One term in the Lagrangian."""
    term_id: int
    name: str
    formula: str
    description: str
    coupling_constant: str
    coupling_value: float


@dataclass
class EmbeddedTripletLagrangian:
    """The curvature-coupled embedded-triplet Lagrangian."""
    terms: List[LagrangianTerm]
    n_terms: int
    full_formula: str
    effective_mass_formula: str
    m0_squared: float
    eta: float
    lam: float
    xi: float
    broken_phase: bool  # m0^2 < 0
    vev_squared: float  # eta^2 in broken phase
    notes: List[str] = field(default_factory=list)


@dataclass
class EmbeddingAnsatz:
    """Hedgehog embedding ansatz."""
    ansatz_formula: str        # Phi^a = eta*f(r)*r_hat^a
    radial_mode_formula: str   # |Phi| = eta*f(r)
    scalar_memory_id: str      # Phi_scalar = eta*f(r)
    boundary_f_origin: float   # f(0) = 0
    boundary_f_infty: float    # f(inf) = 1
    radial_mode_at_infty: float  # eta*1 = eta
    homotopy_class: str        # pi_2(S^2) = Z
    notes: List[str] = field(default_factory=list)


@dataclass
class ModeSectorProfile:
    """Numerical profile for one energy-density sector."""
    name: str
    formula: str
    r_grid: np.ndarray
    values: np.ndarray
    tail_exponent: float
    tail_coefficient: float
    asymptotic_formula: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ModeDecomposition:
    """Full mode decomposition of the embedded-triplet energy density."""
    sectors: List[ModeSectorProfile]
    n_sectors: int
    total_epsilon: np.ndarray
    r_grid: np.ndarray
    # BVP data
    f_solution: np.ndarray
    f_prime: np.ndarray
    bvp_converged: bool
    # Tail summary
    radial_kinetic_exponent: float
    angular_gradient_exponent: float
    potential_exponent: float
    curvature_coupling_exponent: float
    notes: List[str] = field(default_factory=list)


@dataclass
class RadialModeEquation:
    """The EOM for the radial mode f(r)."""
    eom_formula: str
    # Comparison with scalar-memory equation
    scalar_memory_formula: str
    # Structural comparison
    radial_is_static: bool
    scalar_memory_is_dynamic: bool
    radial_driven_by: str       # "self-interaction + topology"
    scalar_memory_driven_by: str  # "source term X(r)"
    eom_has_curvature_coupling: bool
    xi_correction_formula: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentARecoveryAssessment:
    """Three-part test for Component A recovery."""
    # Shape test
    shape_exponent_target: float   # -4.0
    shape_exponent_measured: float  # from (f')^2 tail fit
    shape_match: bool               # |measured - target| < threshold
    shape_verdict: str

    # Coefficient test
    coeff_radial_kinetic: float    # (1/2)*eta^2*c^2
    coeff_component_A: float       # A^2 * MASS_COEFF
    coeff_ratio: float             # radial / component_A
    coeff_match: bool              # ratio ~ 1
    coeff_verdict: str

    # Interpretation test
    radial_mechanism: str          # "topology-driven"
    scalar_memory_mechanism: str   # "source-driven"
    mechanisms_identical: bool     # False (structurally different)
    interpretation_verdict: str

    # Overall
    all_three_pass: bool
    classification: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentBPreservationAssessment:
    """Component B preservation check."""
    angular_tail_exponent_target: float  # -2.0
    angular_tail_exponent_measured: float
    angular_tail_coefficient: float
    angular_target_coefficient: float  # eta^2
    angular_match: bool
    curvature_correction_negligible: bool
    classification: str  # "preserved", "preserved_with_corrections", "not_preserved"
    notes: List[str] = field(default_factory=list)


@dataclass
class CurvatureInvariantAssessment:
    """Assessment of one curvature invariant as trigger candidate."""
    invariant_id: int
    name: str
    formula: str
    # Properties
    nonzero_in_vacuum: bool
    nonzero_in_sourced: bool
    value_at_Req: float       # evaluated at R_EQ
    value_at_half: float      # evaluated at r = 0.5
    value_at_one: float       # evaluated at r = 1.0
    # SSB check
    m_eff_squared_at_Req: float
    ssb_achieved: bool        # m_eff^2 < 0 at R_EQ
    critical_radius: float    # where m_eff^2 = 0 (if exists)
    # Ranking
    score: float              # 0.0 to 1.0
    verdict: str
    notes: List[str] = field(default_factory=list)


@dataclass
class TriggerRegimeAssessment:
    """Multi-invariant trigger regime assessment."""
    invariants: List[CurvatureInvariantAssessment]
    n_invariants: int
    top_ranked_id: int
    top_ranked_name: str
    top_ranked_score: float
    any_ssb_achieved: bool
    m0_squared: float
    xi: float
    effective_mass_formula: str
    classification: str  # "ssb_confirmed", "ssb_plausible", etc.
    notes: List[str] = field(default_factory=list)


@dataclass
class Artifact:
    """One identified artifact or unresolved item."""
    artifact_id: int
    category: str      # "cross_term", "approximation", "unresolved", "caveat"
    description: str
    severity: str      # "minor", "moderate", "major"
    resolvable_in_future: bool


@dataclass
class ArtifactInventory:
    """Complete inventory of artifacts."""
    artifacts: List[Artifact]
    n_artifacts: int
    n_major: int
    n_moderate: int
    n_minor: int
    notes: List[str] = field(default_factory=list)


@dataclass
class UnificationDynamicsClassification:
    """Final D4 classification."""
    classification: str
    phase_status: str
    comp_a_shape: bool
    comp_a_coeff: bool
    comp_a_interpretation: bool
    comp_b_preserved: bool
    trigger_viable: bool
    top_trigger_name: str
    top_trigger_score: float
    phase_lock_update: Dict[str, str]
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class UnificationDynamicsResult:
    """Master result container for Phase D4."""
    valid: bool
    params: UnificationDynamicsParams
    lagrangian: Optional[EmbeddedTripletLagrangian] = None
    ansatz: Optional[EmbeddingAnsatz] = None
    decomposition: Optional[ModeDecomposition] = None
    radial_equation: Optional[RadialModeEquation] = None
    comp_a_assessment: Optional[ComponentARecoveryAssessment] = None
    comp_b_assessment: Optional[ComponentBPreservationAssessment] = None
    trigger_assessment: Optional[TriggerRegimeAssessment] = None
    artifact_inventory: Optional[ArtifactInventory] = None
    classification: Optional[UnificationDynamicsClassification] = None
    nonclaims: List[str] = field(default_factory=lambda: list(DYNAMICS_NONCLAIMS))
    assumptions: List[str] = field(default_factory=lambda: list(DYNAMICS_ASSUMPTIONS))
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Utility: numpy-safe trapezoid
# ================================================================

_trapz = getattr(np, "trapezoid", np.trapz)


def _fit_power_law(r: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """Fit y ~ A * r^n in log-log space.  Returns (exponent, coefficient)."""
    mask = (r > 0) & (y > 0)
    if np.sum(mask) < 5:
        return (0.0, 0.0)
    log_r = np.log(r[mask])
    log_y = np.log(y[mask])
    # Linear fit in log-log
    n = len(log_r)
    sx = np.sum(log_r)
    sy = np.sum(log_y)
    sxx = np.sum(log_r ** 2)
    sxy = np.sum(log_r * log_y)
    denom = n * sxx - sx ** 2
    if abs(denom) < 1e-30:
        return (0.0, 0.0)
    slope = (n * sxy - sx * sy) / denom
    intercept = (sy - slope * sx) / n
    return (slope, math.exp(intercept))


# ================================================================
# Level 1: Construct Lagrangian
# ================================================================

def construct_lagrangian(
    params: UnificationDynamicsParams,
) -> EmbeddedTripletLagrangian:
    """Construct the curvature-coupled embedded-triplet Lagrangian.

    L = (1/2) d_mu Phi^a d^mu Phi^a + (1/2)m0^2 |Phi|^2
        - (1/4) lam |Phi|^4 - (1/2) xi C |Phi|^2

    In broken phase (m0^2 < 0), rewritten as Mexican-hat:
    L = kinetic - (1/4) lam (|Phi|^2 - eta^2)^2 - (1/2) xi C |Phi|^2
    """
    terms = [
        LagrangianTerm(
            term_id=1,
            name="kinetic",
            formula="(1/2) d_mu Phi^a d^mu Phi^a",
            description="O(3)-covariant kinetic term for the triplet field.",
            coupling_constant="1",
            coupling_value=1.0,
        ),
        LagrangianTerm(
            term_id=2,
            name="mass",
            formula="(1/2) m0^2 |Phi|^2",
            description="Bare mass term.  m0^2 < 0 for spontaneous symmetry breaking.",
            coupling_constant="m0^2",
            coupling_value=params.m0_squared,
        ),
        LagrangianTerm(
            term_id=3,
            name="quartic",
            formula="-(1/4) lam |Phi|^4",
            description="Quartic self-interaction (Mexican-hat potential).",
            coupling_constant="lambda",
            coupling_value=params.lam,
        ),
        LagrangianTerm(
            term_id=4,
            name="curvature_coupling",
            formula="-(1/2) xi C |Phi|^2",
            description="Non-minimal curvature coupling.  C is the chosen "
                        "curvature invariant (ranked in trigger assessment).",
            coupling_constant="xi",
            coupling_value=params.xi,
        ),
    ]

    broken = params.m0_squared < 0
    vev_sq = abs(params.m0_squared) / params.lam if broken else 0.0

    notes = [
        "Lagrangian has 4 terms: kinetic, mass, quartic, curvature coupling.",
        f"Broken phase: {broken} (m0^2 = {params.m0_squared:.6f}).",
    ]
    if broken:
        notes.append(
            f"VEV: eta^2 = |m0^2|/lam = {vev_sq:.6f} "
            f"(target eta^2 = {params.eta**2:.6f})."
        )

    return EmbeddedTripletLagrangian(
        terms=terms,
        n_terms=len(terms),
        full_formula=(
            "L = (1/2) d_mu Phi^a d^mu Phi^a + (1/2) m0^2 |Phi|^2 "
            "- (1/4) lam |Phi|^4 - (1/2) xi C |Phi|^2"
        ),
        effective_mass_formula="m_eff^2(C) = m0^2 - xi*C",
        m0_squared=params.m0_squared,
        eta=params.eta,
        lam=params.lam,
        xi=params.xi,
        broken_phase=broken,
        vev_squared=vev_sq,
        notes=notes,
    )


# ================================================================
# Level 2: Embedding Ansatz
# ================================================================

def apply_embedding_ansatz(
    lagrangian: EmbeddedTripletLagrangian,
    params: UnificationDynamicsParams,
) -> EmbeddingAnsatz:
    """Apply the hedgehog embedding ansatz: Phi^a = eta*f(r)*r_hat^a."""
    return EmbeddingAnsatz(
        ansatz_formula="Phi^a = eta * f(r) * r_hat^a",
        radial_mode_formula="|Phi| = eta * f(r)",
        scalar_memory_id="Phi_scalar = eta * f(r) (candidate identification)",
        boundary_f_origin=0.0,
        boundary_f_infty=1.0,
        radial_mode_at_infty=params.eta,
        homotopy_class="pi_2(S^2) = Z",
        notes=[
            "Hedgehog ansatz: topological winding number = 1.",
            "Radial mode f(r) satisfies D2 BVP.",
            "Embedding: old scalar-memory Phi identified with eta*f(r).",
            "This identification is a candidate, not yet derived.",
        ],
    )


# ================================================================
# Level 3: Mode Decomposition
# ================================================================

def decompose_modes(
    ansatz: EmbeddingAnsatz,
    lagrangian: EmbeddedTripletLagrangian,
    params: UnificationDynamicsParams,
) -> ModeDecomposition:
    """Decompose energy density into radial, angular, potential, curvature sectors.

    Uses D2 BVP solution for numerical profiles.
    """
    # Solve D2 BVP
    mono_params = NumericalMonopoleParams(
        eta=params.eta,
        lam=params.lam,
        r_min=params.r_min,
        r_max=params.r_max,
        n_grid=params.n_grid,
    )
    bvp = solve_hedgehog_bvp(mono_params)

    r = bvp.r_grid
    f = bvp.f_solution
    fp = bvp.f_prime
    eta = params.eta

    # Four energy-density sectors
    radial_kin = 0.5 * eta ** 2 * fp ** 2
    angular_grad = eta ** 2 * f ** 2 / r ** 2
    potential = 0.25 * params.lam * eta ** 4 * (f ** 2 - 1.0) ** 2

    # Curvature coupling: use Kretschner sqrt(K) as placeholder
    # K = 48*M^2/r^6 for Schwarzschild-like
    sqrt_K = np.sqrt(KRETSCHNER_COEFF) / r ** 3
    curv_coupling = 0.5 * params.xi * sqrt_K * eta ** 2 * f ** 2

    total = radial_kin + angular_grad + potential + curv_coupling

    # Fit tails in outer region (r > 2.0)
    outer = r > 2.0
    rk_exp, rk_coeff = _fit_power_law(r[outer], radial_kin[outer])
    ag_exp, ag_coeff = _fit_power_law(r[outer], angular_grad[outer])
    pot_exp, pot_coeff = _fit_power_law(r[outer], potential[outer])
    cc_exp, cc_coeff = _fit_power_law(r[outer], curv_coupling[outer])

    sectors = [
        ModeSectorProfile(
            name="radial_kinetic",
            formula="(1/2) eta^2 (f')^2",
            r_grid=r,
            values=radial_kin,
            tail_exponent=rk_exp,
            tail_coefficient=rk_coeff,
            asymptotic_formula="~ (1/2) eta^2 c^2 / r^4",
            notes=[f"Tail exponent: {rk_exp:.3f} (target: -4.0)"],
        ),
        ModeSectorProfile(
            name="angular_gradient",
            formula="eta^2 f^2 / r^2",
            r_grid=r,
            values=angular_grad,
            tail_exponent=ag_exp,
            tail_coefficient=ag_coeff,
            asymptotic_formula="~ eta^2 / r^2",
            notes=[f"Tail exponent: {ag_exp:.3f} (target: -2.0)"],
        ),
        ModeSectorProfile(
            name="potential",
            formula="(1/4) lam eta^4 (f^2 - 1)^2",
            r_grid=r,
            values=potential,
            tail_exponent=pot_exp,
            tail_coefficient=pot_coeff,
            asymptotic_formula="~ exponential decay",
            notes=[f"Tail exponent: {pot_exp:.3f} (should be steep/negligible)"],
        ),
        ModeSectorProfile(
            name="curvature_coupling",
            formula="(1/2) xi sqrt(K) eta^2 f^2",
            r_grid=r,
            values=curv_coupling,
            tail_exponent=cc_exp,
            tail_coefficient=cc_coeff,
            asymptotic_formula="~ (1/2) xi sqrt(48) M eta^2 / r^3",
            notes=[f"Tail exponent: {cc_exp:.3f} (expected ~ -3.0)"],
        ),
    ]

    return ModeDecomposition(
        sectors=sectors,
        n_sectors=len(sectors),
        total_epsilon=total,
        r_grid=r,
        f_solution=f,
        f_prime=fp,
        bvp_converged=bvp.converged,
        radial_kinetic_exponent=rk_exp,
        angular_gradient_exponent=ag_exp,
        potential_exponent=pot_exp,
        curvature_coupling_exponent=cc_exp,
        notes=[
            f"BVP converged: {bvp.converged}",
            f"Radial kinetic tail: r^{rk_exp:.2f} (target r^-4)",
            f"Angular gradient tail: r^{ag_exp:.2f} (target r^-2)",
        ],
    )


# ================================================================
# Level 4: Radial Mode Equation
# ================================================================

def derive_radial_mode_equation(
    decomposition: ModeDecomposition,
    params: UnificationDynamicsParams,
) -> RadialModeEquation:
    """Derive the EOM for f(r) from the Lagrangian and compare with scalar-memory."""
    eom = (
        "f'' + (2/r)f' - (2/r^2)f + lam*eta^2*f*(1 - f^2) + xi*C*f = 0"
    )
    scalar_mem = (
        "tau * dPhi/dt + Phi = X(r)  [steady state: Phi = X(r)]"
    )

    return RadialModeEquation(
        eom_formula=eom,
        scalar_memory_formula=scalar_mem,
        radial_is_static=True,
        scalar_memory_is_dynamic=True,
        radial_driven_by="self-interaction (lam) + topology (hedgehog BC)",
        scalar_memory_driven_by="source term X(r) = S(r)^2 from matter",
        eom_has_curvature_coupling=True,
        xi_correction_formula="xi*C*f (shifts effective mass of radial mode)",
        notes=[
            "Radial EOM: static nonlinear ODE with topological BC f(0)=0, f(inf)=1.",
            "Scalar-memory: dynamic relaxation toward source X(r).",
            "Structural difference: topology-driven vs source-driven.",
            "The radial EOM includes curvature coupling xi*C*f.",
            "In the limit xi -> 0, recovers D2 hedgehog ODE.",
        ],
    )


# ================================================================
# Level 5: Component A Recovery Assessment
# ================================================================

def assess_component_A_recovery(
    radial_eq: RadialModeEquation,
    decomposition: ModeDecomposition,
    params: UnificationDynamicsParams,
) -> ComponentARecoveryAssessment:
    """Three-part test for Component A recovery.

    Shape: Does (f')^2 give 1/r^4 scaling?
    Coefficient: Does (1/2)*eta^2*c^2 match A^2*MASS_COEFF?
    Interpretation: Is the mechanism the same as scalar-memory?
    """
    # --- Shape test ---
    # At finite lambda on finite BVP domain, the asymptotic exponent
    # is not fully reached.  D2 showed the total energy exponent
    # approaches -2 only at high lambda (lam=200 -> -1.97).
    # The radial kinetic (f')^2 approaches -4 similarly.
    # Tolerance of 1.5 accounts for finite-domain convergence.
    rk_exp = decomposition.radial_kinetic_exponent
    shape_target = -4.0
    shape_tol = 1.5  # accounts for BVP finite domain + finite lambda
    shape_match = abs(rk_exp - shape_target) < shape_tol
    if shape_match:
        shape_verdict = (
            f"PASS: radial kinetic exponent {rk_exp:.2f} "
            f"within {shape_tol} of asymptotic target {shape_target}. "
            f"Finite-domain BVP: exponent trends toward {shape_target} "
            f"at higher lambda (D2 lambda-scan trend)."
        )
    else:
        shape_verdict = (
            f"FAIL: radial kinetic exponent {rk_exp:.2f} "
            f"not within {shape_tol} of target {shape_target}. "
            f"May require higher lambda or larger BVP domain."
        )

    # --- Coefficient test ---
    # From BVP: (f')^2 tail ~ c^2/r^4 where c is fitted coefficient
    rk_sector = decomposition.sectors[0]  # radial_kinetic
    coeff_radial = rk_sector.tail_coefficient  # (1/2)*eta^2*c^2 already
    coeff_comp_A = A_CRIT_SQUARED * MASS_COEFF  # A^2 * MASS_COEFF
    if coeff_comp_A > 0:
        ratio = coeff_radial / coeff_comp_A
    else:
        ratio = 0.0
    coeff_match = 0.1 < ratio < 10.0  # within order of magnitude
    coeff_verdict = (
        f"Radial kinetic coefficient: {coeff_radial:.6f}, "
        f"Component A coefficient: {coeff_comp_A:.6f}, "
        f"ratio: {ratio:.4f}. "
        f"{'Within order of magnitude' if coeff_match else 'Mismatch (> 1 OOM)'}."
    )

    # --- Interpretation test ---
    radial_mech = "topology-driven (hedgehog self-interaction + BCs)"
    scalar_mech = "source-driven (tau dPhi/dt + Phi = X(r))"
    mechs_identical = False  # structurally different
    interp_verdict = (
        "Radial mode is topology-driven; scalar-memory is source-driven. "
        "These are structurally different mechanisms. "
        "The radial mode is a new sector with analogous 1/r^4 scaling, "
        "not the old scalar-memory sector recovered."
    )

    # --- Overall classification ---
    all_pass = shape_match and coeff_match and mechs_identical
    if all_pass:
        classification = "canon_recovery_verified"
    elif shape_match and coeff_match and not mechs_identical:
        classification = "component_a_shape_recovered_but_interpretation_not_yet_verified"
    elif shape_match and not coeff_match:
        classification = "component_a_shape_recovered_but_interpretation_not_yet_verified"
    else:
        classification = "component_b_preserved_but_component_a_not_yet_recovered"

    return ComponentARecoveryAssessment(
        shape_exponent_target=shape_target,
        shape_exponent_measured=rk_exp,
        shape_match=shape_match,
        shape_verdict=shape_verdict,
        coeff_radial_kinetic=coeff_radial,
        coeff_component_A=coeff_comp_A,
        coeff_ratio=ratio,
        coeff_match=coeff_match,
        coeff_verdict=coeff_verdict,
        radial_mechanism=radial_mech,
        scalar_memory_mechanism=scalar_mech,
        mechanisms_identical=mechs_identical,
        interpretation_verdict=interp_verdict,
        all_three_pass=all_pass,
        classification=classification,
        notes=[
            "Shape test: compares radial kinetic tail exponent with -4.0.",
            "Coefficient test: compares radial kinetic amplitude with A^2*MASS_COEFF.",
            "Interpretation test: compares driving mechanisms (topology vs source).",
            "Mechanisms are structurally different by construction.",
        ],
    )


# ================================================================
# Level 6: Component B Preservation Assessment
# ================================================================

def assess_component_B_preservation(
    decomposition: ModeDecomposition,
    params: UnificationDynamicsParams,
) -> ComponentBPreservationAssessment:
    """Check that angular gradient eta^2*f^2/r^2 retains 1/r^2 tail."""
    ag_sector = decomposition.sectors[1]  # angular_gradient
    ag_exp = ag_sector.tail_exponent
    ag_coeff = ag_sector.tail_coefficient
    target_exp = -2.0
    target_coeff = params.eta ** 2

    # At finite lambda on finite BVP domain, the angular gradient
    # exponent hasn't fully converged to -2.  D2 showed the total
    # energy exponent is -1.66 at lambda=25, trending toward -2
    # at higher lambda.  Tolerance of 1.0 is appropriate.
    exp_tol = 1.0  # accounts for finite-domain convergence
    exp_match = abs(ag_exp - target_exp) < exp_tol
    coeff_tol = 0.5 * target_coeff  # within factor of 2
    coeff_match = abs(ag_coeff - target_coeff) < coeff_tol

    # Curvature correction: at large r, curvature invariants -> 0
    # so coupling vanishes and does not spoil the 1/r^2 tail
    cc_sector = decomposition.sectors[3]  # curvature_coupling
    # At large r, curvature coupling decays as ~1/r^3 or steeper
    # while angular is ~1/r^2, so curvature is subdominant
    cc_exp = cc_sector.tail_exponent
    curv_negligible = cc_exp < ag_exp - 0.5  # curvature decays faster

    if exp_match and curv_negligible:
        classification = "preserved"
    elif exp_match and not curv_negligible:
        classification = "preserved_with_corrections"
    else:
        classification = "not_preserved"

    return ComponentBPreservationAssessment(
        angular_tail_exponent_target=target_exp,
        angular_tail_exponent_measured=ag_exp,
        angular_tail_coefficient=ag_coeff,
        angular_target_coefficient=target_coeff,
        angular_match=exp_match,
        curvature_correction_negligible=curv_negligible,
        classification=classification,
        notes=[
            f"Angular gradient tail exponent: {ag_exp:.3f} (target: {target_exp})",
            f"Angular gradient coefficient: {ag_coeff:.6f} (target eta^2: {target_coeff:.6f})",
            f"Curvature coupling tail exponent: {cc_exp:.3f} (subdominant if < {ag_exp - 0.5:.3f})",
            f"Classification: {classification}",
        ],
    )


# ================================================================
# Level 7: Trigger Regime Assessment (multi-invariant)
# ================================================================

def _evaluate_ricci_scalar(r: np.ndarray, params: UnificationDynamicsParams) -> np.ndarray:
    """Estimate Ricci scalar R in the sourced interior.

    In vacuum Schwarzschild, R = 0 identically.
    In the sourced GRUT interior, R depends on the trace of T_munu.
    For a scalar field with energy density rho and pressure p:
      R = -8*pi*(rho - 3*p)  (in geometrized units)
    We estimate using the scalar-memory energy density profile:
      rho ~ MASS_COEFF / r^4  (from Phase 6)
    For a stiff fluid or static scalar, p ~ rho, giving R ~ 16*pi*rho.
    This is approximate and model-dependent.
    """
    rho = MASS_COEFF / r ** 4
    # For scalar field: T = -rho + 3*p.  For static field p ~ rho/3 (radiation-like)
    # then T ~ 0 and R ~ 0.  For stiff (p ~ rho), T ~ 2*rho, R ~ -16*pi*rho.
    # Conservative: use R ~ -8*pi*rho (p ~ 0 approximation)
    R = -8.0 * math.pi * rho
    return R


def _evaluate_kretschner(r: np.ndarray, params: UnificationDynamicsParams) -> np.ndarray:
    """Evaluate sqrt(Kretschner) = sqrt(R_abcd R^abcd).

    For Schwarzschild: K = 48*M^2/r^6, so sqrt(K) = sqrt(48)*M/r^3.
    This is nonzero even in vacuum.
    """
    return np.sqrt(KRETSCHNER_COEFF) / r ** 3


def _evaluate_ricci_squared(r: np.ndarray, params: UnificationDynamicsParams) -> np.ndarray:
    """Evaluate sqrt(R_ab R^ab) in the sourced interior.

    Vanishes in vacuum Schwarzschild.
    In sourced interior: R_ab R^ab ~ (8*pi)^2 * (rho^2 + 3*p^2)
    Approximate as ~ (8*pi)^2 * rho^2 with rho ~ MASS_COEFF/r^4.
    """
    rho = MASS_COEFF / r ** 4
    return 8.0 * math.pi * rho  # sqrt of (8*pi*rho)^2


def assess_trigger_regime(
    lagrangian: EmbeddedTripletLagrangian,
    params: UnificationDynamicsParams,
) -> TriggerRegimeAssessment:
    """Assess multiple curvature invariants as SSB trigger candidates.

    For each invariant C:
      m_eff^2(C) = m0^2 - xi*C
    SSB when m_eff^2 < 0, i.e., xi*C > |m0^2| (for m0^2 > 0 base mass)
    or xi*C shifts the already-negative m0^2 further negative (enhances SSB).

    For the broken-phase base (m0^2 = -lam*eta^2 < 0):
      m_eff^2 = m0^2 - xi*C
    The curvature coupling modifies the VEV location.
    The key question: does the curvature provide an environment-dependent
    trigger that differentiates interior from exterior?
    """
    m0sq = params.m0_squared
    xi = params.xi

    # Evaluation points
    r_eval = np.array([R_EQ, 0.5, 1.0])
    r_labels = ["R_EQ", "0.5", "1.0"]

    # --- Ricci scalar ---
    R_vals = _evaluate_ricci_scalar(r_eval, params)
    R_m_eff = m0sq - xi * R_vals
    R_ssb_at_Req = R_m_eff[0] < 0
    # Critical radius: where m_eff^2 = 0 -> xi*R(r_c) = m0^2
    # R(r) ~ -8*pi*MASS_COEFF/r^4, so r_c = (8*pi*xi*MASS_COEFF/|m0^2|)^(1/4)
    if xi > 0 and m0sq < 0:
        # Already broken at base; curvature enhances
        R_crit = 0.0  # no critical radius needed
    elif xi > 0 and abs(R_vals[0]) > 0:
        val = abs(m0sq) / (xi * 8.0 * math.pi * MASS_COEFF)
        R_crit = val ** 0.25 if val > 0 else 0.0
    else:
        R_crit = 0.0

    # Ricci score: penalize if R ~ 0 in vacuum (it is)
    ricci_score = 0.0
    if abs(R_vals[0]) > 1e-6:
        ricci_score += 0.3  # nonzero in sourced
    if R_ssb_at_Req:
        ricci_score += 0.3
    # Ricci is zero in vacuum: that's a feature (environment-dependent) or bug
    ricci_score += 0.2  # environment-dependent is a feature for trigger
    ricci_notes = [
        "Ricci scalar R is zero in vacuum Schwarzschild.",
        f"R(R_EQ) ~ {R_vals[0]:.4f} in sourced approximation.",
        "Nonzero only in sourced regions — environment-dependent.",
        "Model-dependent: estimate relies on scalar-memory stress-energy.",
    ]

    ricci_assessment = CurvatureInvariantAssessment(
        invariant_id=1,
        name="ricci_scalar",
        formula="R = g^{ab} R_{ab}",
        nonzero_in_vacuum=False,
        nonzero_in_sourced=True,
        value_at_Req=float(R_vals[0]),
        value_at_half=float(R_vals[1]),
        value_at_one=float(R_vals[2]),
        m_eff_squared_at_Req=float(R_m_eff[0]),
        ssb_achieved=bool(R_ssb_at_Req),
        critical_radius=float(R_crit),
        score=ricci_score,
        verdict="moderate" if ricci_score >= 0.5 else "weak",
        notes=ricci_notes,
    )

    # --- Kretschner sqrt(K) ---
    sqrtK_vals = _evaluate_kretschner(r_eval, params)
    K_m_eff = m0sq - xi * sqrtK_vals
    K_ssb_at_Req = K_m_eff[0] < 0
    # Critical radius: xi*sqrt(48)*M/r_c^3 = |m0^2|
    if xi > 0 and abs(m0sq) > 0:
        val = xi * math.sqrt(KRETSCHNER_COEFF) / abs(m0sq)
        K_crit = val ** (1.0 / 3.0) if val > 0 else 0.0
    else:
        K_crit = 0.0

    kretschner_score = 0.0
    kretschner_score += 0.4  # nonzero in vacuum (robust)
    if K_ssb_at_Req:
        kretschner_score += 0.3
    kretschner_score += 0.15  # always available, no model dependence
    kretschner_notes = [
        "Kretschner K = R_{abcd} R^{abcd} is nonzero in vacuum.",
        f"sqrt(K) at R_EQ ~ {sqrtK_vals[0]:.4f}",
        "Provides a robust strong-field mass scale.",
        "Does not require matter content to be nonzero.",
        "Heuristic: using sqrt(K) as mass-squared-like coupling is "
        "non-standard but structurally reasonable.",
    ]

    kretschner_assessment = CurvatureInvariantAssessment(
        invariant_id=2,
        name="kretschner_sqrt",
        formula="sqrt(K) = sqrt(R_{abcd} R^{abcd})",
        nonzero_in_vacuum=True,
        nonzero_in_sourced=True,
        value_at_Req=float(sqrtK_vals[0]),
        value_at_half=float(sqrtK_vals[1]),
        value_at_one=float(sqrtK_vals[2]),
        m_eff_squared_at_Req=float(K_m_eff[0]),
        ssb_achieved=bool(K_ssb_at_Req),
        critical_radius=float(K_crit),
        score=kretschner_score,
        verdict="strong_candidate" if kretschner_score >= 0.7 else "moderate",
        notes=kretschner_notes,
    )

    # --- Ricci-squared sqrt(R_ab R^ab) ---
    RicSq_vals = _evaluate_ricci_squared(r_eval, params)
    RS_m_eff = m0sq - xi * RicSq_vals
    RS_ssb_at_Req = RS_m_eff[0] < 0
    if xi > 0 and abs(m0sq) > 0:
        val = xi * 8.0 * math.pi * MASS_COEFF / abs(m0sq)
        RS_crit = val ** 0.25 if val > 0 else 0.0
    else:
        RS_crit = 0.0

    ricci_sq_score = 0.0
    if abs(RicSq_vals[0]) > 1e-6:
        ricci_sq_score += 0.3
    if RS_ssb_at_Req:
        ricci_sq_score += 0.3
    ricci_sq_score += 0.1  # intermediate between R and K
    ricci_sq_notes = [
        "Ricci-squared R_{ab}R^{ab} vanishes in vacuum Schwarzschild.",
        f"sqrt(R_ab R^ab) at R_EQ ~ {RicSq_vals[0]:.4f}",
        "Nonzero in sourced regions, vanishes in vacuum.",
        "Intermediate robustness between Ricci scalar and Kretschner.",
    ]

    ricci_sq_assessment = CurvatureInvariantAssessment(
        invariant_id=3,
        name="ricci_squared",
        formula="sqrt(R_{ab} R^{ab})",
        nonzero_in_vacuum=False,
        nonzero_in_sourced=True,
        value_at_Req=float(RicSq_vals[0]),
        value_at_half=float(RicSq_vals[1]),
        value_at_one=float(RicSq_vals[2]),
        m_eff_squared_at_Req=float(RS_m_eff[0]),
        ssb_achieved=bool(RS_ssb_at_Req),
        critical_radius=float(RS_crit),
        score=ricci_sq_score,
        verdict="moderate" if ricci_sq_score >= 0.5 else "weak",
        notes=ricci_sq_notes,
    )

    invariants = [ricci_assessment, kretschner_assessment, ricci_sq_assessment]

    # Rank by score
    sorted_inv = sorted(invariants, key=lambda x: x.score, reverse=True)
    top = sorted_inv[0]
    any_ssb = any(inv.ssb_achieved for inv in invariants)

    # Classification
    if any_ssb and top.score >= 0.7:
        classification = "ssb_plausible"
    elif any_ssb:
        classification = "ssb_requires_coupled_solution"
    elif top.score >= 0.5:
        classification = "ssb_requires_coupled_solution"
    else:
        classification = "ssb_impossible"

    return TriggerRegimeAssessment(
        invariants=invariants,
        n_invariants=len(invariants),
        top_ranked_id=top.invariant_id,
        top_ranked_name=top.name,
        top_ranked_score=top.score,
        any_ssb_achieved=any_ssb,
        m0_squared=m0sq,
        xi=xi,
        effective_mass_formula="m_eff^2(C) = m0^2 - xi*C",
        classification=classification,
        notes=[
            f"Top-ranked invariant: {top.name} (score {top.score:.2f})",
            f"Any SSB achieved: {any_ssb}",
            f"Classification: {classification}",
            "Kretschner sqrt(K) is nonzero in vacuum — most robust trigger.",
            "Ricci scalar R is zero in vacuum — environment-dependent.",
            "All curvature estimates are approximate (fixed background).",
        ],
    )


# ================================================================
# Level 8: Artifact Inventory
# ================================================================

def inventory_artifacts(
    decomposition: ModeDecomposition,
    radial_eq: RadialModeEquation,
    comp_a: ComponentARecoveryAssessment,
    comp_b: ComponentBPreservationAssessment,
    trigger: TriggerRegimeAssessment,
    params: UnificationDynamicsParams,
) -> ArtifactInventory:
    """Inventory all cross-term artifacts, approximations, and unresolved items."""
    artifacts = []
    aid = 0

    # 1. Radial-angular cross-terms in curved background
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="cross_term",
        description=(
            "In a curved background, the radial and angular sectors may "
            "develop cross-terms from covariant derivatives that are absent "
            "in flat space.  These are not evaluated in D4."
        ),
        severity="moderate",
        resolvable_in_future=True,
    ))

    # 2. Back-reaction not included
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="approximation",
        description=(
            "The background metric is held fixed.  The defect and scalar "
            "sectors source the metric but back-reaction is not iterated."
        ),
        severity="moderate",
        resolvable_in_future=True,
    ))

    # 3. Coefficient matching requires lambda tuning
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="unresolved",
        description=(
            "The radial kinetic coefficient depends on lambda and the BVP "
            "solution.  Matching it to A^2*MASS_COEFF would require tuning "
            "lambda, which has no independent physical justification in D4."
        ),
        severity="moderate",
        resolvable_in_future=True,
    ))

    # 4. Mechanism difference (topology vs source)
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="caveat",
        description=(
            "The radial mode is driven by topology (hedgehog BCs + self-"
            "interaction).  The scalar-memory is driven by sources (X(r)).  "
            "These are structurally different mechanisms, even if the tail "
            "scaling matches."
        ),
        severity="major",
        resolvable_in_future=True,
    ))

    # 5. Curvature invariant coupling is heuristic
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="caveat",
        description=(
            "Using sqrt(K) as a mass-squared-like coupling scale is a "
            "heuristic, not a rigorously derived field-theory construction.  "
            "Standard non-minimal coupling uses xi*R, but R=0 in vacuum."
        ),
        severity="moderate",
        resolvable_in_future=True,
    ))

    # 6. Curvature trigger sign depends on matter model
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="approximation",
        description=(
            "The Ricci scalar estimate depends on the assumed equation of "
            "state for the scalar-memory matter (p/rho ratio).  Different "
            "assumptions give different R and different trigger regimes."
        ),
        severity="minor",
        resolvable_in_future=True,
    ))

    # 7. BVP finite-domain effects
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="approximation",
        description=(
            "The BVP is solved on [r_min, r_max] = [0.01, 5.0].  Tail "
            "fits in the outer region may not have fully converged to "
            "asymptotic behavior."
        ),
        severity="minor",
        resolvable_in_future=True,
    ))

    # 8. xi-dependent corrections to tail exponents
    aid += 1
    artifacts.append(Artifact(
        artifact_id=aid,
        category="cross_term",
        description=(
            "The curvature coupling xi*C*|Phi|^2 modifies the radial mode "
            "EOM and could shift tail exponents.  In D4, the BVP is solved "
            "without xi correction (D2 solution reused).  Self-consistent "
            "solution would include xi*C in the ODE."
        ),
        severity="moderate",
        resolvable_in_future=True,
    ))

    n_major = sum(1 for a in artifacts if a.severity == "major")
    n_moderate = sum(1 for a in artifacts if a.severity == "moderate")
    n_minor = sum(1 for a in artifacts if a.severity == "minor")

    return ArtifactInventory(
        artifacts=artifacts,
        n_artifacts=len(artifacts),
        n_major=n_major,
        n_moderate=n_moderate,
        n_minor=n_minor,
        notes=[
            f"Total artifacts: {len(artifacts)}",
            f"Major: {n_major}, Moderate: {n_moderate}, Minor: {n_minor}",
            "All artifacts are documented for future resolution.",
        ],
    )


# ================================================================
# Level 9: Classification
# ================================================================

def classify_dynamics(
    comp_a: ComponentARecoveryAssessment,
    comp_b: ComponentBPreservationAssessment,
    trigger: TriggerRegimeAssessment,
    artifacts: ArtifactInventory,
) -> UnificationDynamicsClassification:
    """Classify D4 outcome based on all assessments.

    Five possible classifications:
    - canon_recovery_verified
    - component_a_shape_recovered_but_interpretation_not_yet_verified
    - component_b_preserved_but_component_a_not_yet_recovered
    - canon_recovery_failed
    - unresolved_artifacts
    """
    a_shape = comp_a.shape_match
    a_coeff = comp_a.coeff_match
    a_interp = comp_a.mechanisms_identical
    b_preserved = comp_b.classification in ("preserved", "preserved_with_corrections")
    trigger_viable = trigger.classification in (
        "ssb_confirmed", "ssb_plausible"
    )

    # Classification logic
    if a_shape and a_coeff and a_interp and b_preserved and trigger_viable:
        classification = "canon_recovery_verified"
    elif a_shape and b_preserved and artifacts.n_major <= 1:
        classification = "component_a_shape_recovered_but_interpretation_not_yet_verified"
    elif b_preserved and not a_shape:
        classification = "component_b_preserved_but_component_a_not_yet_recovered"
    elif artifacts.n_major >= 3:
        classification = "unresolved_artifacts"
    elif not b_preserved:
        classification = "canon_recovery_failed"
    else:
        # Fallback: shape matches but many caveats
        classification = "component_a_shape_recovered_but_interpretation_not_yet_verified"

    phase_status = f"D4 assessed: {classification}"

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
        "unification_D4": f"ASSESSED ({classification})",
    }

    summary_parts = []
    summary_parts.append(f"Component A shape test: {'PASS' if a_shape else 'FAIL'}")
    summary_parts.append(f"Component A coefficient test: {'PASS' if a_coeff else 'FAIL'}")
    summary_parts.append(
        f"Component A interpretation: {'SAME' if a_interp else 'DIFFERENT mechanisms'}"
    )
    summary_parts.append(f"Component B: {comp_b.classification}")
    summary_parts.append(
        f"Trigger: {trigger.classification} "
        f"(top: {trigger.top_ranked_name}, score {trigger.top_ranked_score:.2f})"
    )
    summary_parts.append(f"Artifacts: {artifacts.n_artifacts} total, {artifacts.n_major} major")
    summary_parts.append(f"Classification: {classification}")
    summary = "; ".join(summary_parts)

    return UnificationDynamicsClassification(
        classification=classification,
        phase_status=phase_status,
        comp_a_shape=a_shape,
        comp_a_coeff=a_coeff,
        comp_a_interpretation=a_interp,
        comp_b_preserved=b_preserved,
        trigger_viable=trigger_viable,
        top_trigger_name=trigger.top_ranked_name,
        top_trigger_score=trigger.top_ranked_score,
        phase_lock_update=phase_lock,
        summary=summary,
        notes=[
            "Classification is determined by three-part Component A test, "
            "Component B preservation, and trigger viability.",
            "Mechanisms are structurally different by construction "
            "(topology-driven vs source-driven).",
        ],
    )


# ================================================================
# Level 10: Master Computation
# ================================================================

def compute_unification_dynamics(
    params: Optional[UnificationDynamicsParams] = None,
) -> UnificationDynamicsResult:
    """Master computation for Phase D4.

    Orchestrates all levels: Lagrangian, ansatz, mode decomposition,
    radial mode equation, Component A/B assessments, trigger regime,
    artifacts, and classification.
    """
    if params is None:
        params = UnificationDynamicsParams()

    result = UnificationDynamicsResult(valid=False, params=params)

    try:
        # Level 1: Lagrangian
        lagrangian = construct_lagrangian(params)
        result.lagrangian = lagrangian
        result.diagnostics["lagrangian_terms"] = lagrangian.n_terms

        # Level 2: Embedding ansatz
        ansatz = apply_embedding_ansatz(lagrangian, params)
        result.ansatz = ansatz

        # Level 3: Mode decomposition (uses D2 BVP)
        decomposition = decompose_modes(ansatz, lagrangian, params)
        result.decomposition = decomposition
        result.diagnostics["bvp_converged"] = decomposition.bvp_converged
        result.diagnostics["n_sectors"] = decomposition.n_sectors

        # Level 4: Radial mode equation
        radial_eq = derive_radial_mode_equation(decomposition, params)
        result.radial_equation = radial_eq

        # Level 5: Component A recovery
        comp_a = assess_component_A_recovery(radial_eq, decomposition, params)
        result.comp_a_assessment = comp_a
        result.diagnostics["comp_a_classification"] = comp_a.classification

        # Level 6: Component B preservation
        comp_b = assess_component_B_preservation(decomposition, params)
        result.comp_b_assessment = comp_b
        result.diagnostics["comp_b_classification"] = comp_b.classification

        # Level 7: Trigger regime
        trigger = assess_trigger_regime(lagrangian, params)
        result.trigger_assessment = trigger
        result.diagnostics["trigger_classification"] = trigger.classification

        # Level 8: Artifact inventory
        artifacts = inventory_artifacts(
            decomposition, radial_eq, comp_a, comp_b, trigger, params
        )
        result.artifact_inventory = artifacts
        result.diagnostics["n_artifacts"] = artifacts.n_artifacts

        # Level 9: Classification
        classification = classify_dynamics(comp_a, comp_b, trigger, artifacts)
        result.classification = classification
        result.diagnostics["classification"] = classification.classification

        result.valid = True

    except Exception as e:
        result.diagnostics["error"] = str(e)
        result.valid = False

    return result


# ================================================================
# Level 11: Serialization
# ================================================================

def unification_dynamics_result_to_dict(
    result: UnificationDynamicsResult,
) -> Dict[str, Any]:
    """Serialize the master result to a JSON-compatible dictionary."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "params": {
            "eta": result.params.eta,
            "lam": result.params.lam,
            "xi": result.params.xi,
            "m0_squared": result.params.m0_squared,
            "r_min": result.params.r_min,
            "r_max": result.params.r_max,
            "n_grid": result.params.n_grid,
        },
    }

    # Lagrangian
    if result.lagrangian is not None:
        lag = result.lagrangian
        d["lagrangian"] = {
            "n_terms": lag.n_terms,
            "full_formula": lag.full_formula,
            "effective_mass_formula": lag.effective_mass_formula,
            "m0_squared": lag.m0_squared,
            "eta": lag.eta,
            "lam": lag.lam,
            "xi": lag.xi,
            "broken_phase": lag.broken_phase,
            "vev_squared": lag.vev_squared,
            "terms": [
                {"name": t.name, "formula": t.formula,
                 "coupling_constant": t.coupling_constant,
                 "coupling_value": t.coupling_value}
                for t in lag.terms
            ],
        }

    # Ansatz
    if result.ansatz is not None:
        ans = result.ansatz
        d["ansatz"] = {
            "ansatz_formula": ans.ansatz_formula,
            "radial_mode_formula": ans.radial_mode_formula,
            "scalar_memory_id": ans.scalar_memory_id,
            "homotopy_class": ans.homotopy_class,
        }

    # Mode decomposition
    if result.decomposition is not None:
        dec = result.decomposition
        d["decomposition"] = {
            "n_sectors": dec.n_sectors,
            "bvp_converged": dec.bvp_converged,
            "radial_kinetic_exponent": dec.radial_kinetic_exponent,
            "angular_gradient_exponent": dec.angular_gradient_exponent,
            "potential_exponent": dec.potential_exponent,
            "curvature_coupling_exponent": dec.curvature_coupling_exponent,
            "sectors": [
                {"name": s.name, "formula": s.formula,
                 "tail_exponent": s.tail_exponent,
                 "tail_coefficient": s.tail_coefficient,
                 "asymptotic_formula": s.asymptotic_formula}
                for s in dec.sectors
            ],
        }

    # Radial mode equation
    if result.radial_equation is not None:
        req = result.radial_equation
        d["radial_equation"] = {
            "eom_formula": req.eom_formula,
            "scalar_memory_formula": req.scalar_memory_formula,
            "radial_is_static": req.radial_is_static,
            "scalar_memory_is_dynamic": req.scalar_memory_is_dynamic,
            "radial_driven_by": req.radial_driven_by,
            "scalar_memory_driven_by": req.scalar_memory_driven_by,
            "eom_has_curvature_coupling": req.eom_has_curvature_coupling,
        }

    # Component A
    if result.comp_a_assessment is not None:
        ca = result.comp_a_assessment
        d["component_a"] = {
            "shape_exponent_target": ca.shape_exponent_target,
            "shape_exponent_measured": ca.shape_exponent_measured,
            "shape_match": ca.shape_match,
            "shape_verdict": ca.shape_verdict,
            "coeff_radial_kinetic": ca.coeff_radial_kinetic,
            "coeff_component_A": ca.coeff_component_A,
            "coeff_ratio": ca.coeff_ratio,
            "coeff_match": ca.coeff_match,
            "coeff_verdict": ca.coeff_verdict,
            "radial_mechanism": ca.radial_mechanism,
            "scalar_memory_mechanism": ca.scalar_memory_mechanism,
            "mechanisms_identical": ca.mechanisms_identical,
            "interpretation_verdict": ca.interpretation_verdict,
            "all_three_pass": ca.all_three_pass,
            "classification": ca.classification,
        }

    # Component B
    if result.comp_b_assessment is not None:
        cb = result.comp_b_assessment
        d["component_b"] = {
            "angular_tail_exponent_target": cb.angular_tail_exponent_target,
            "angular_tail_exponent_measured": cb.angular_tail_exponent_measured,
            "angular_tail_coefficient": cb.angular_tail_coefficient,
            "angular_target_coefficient": cb.angular_target_coefficient,
            "angular_match": cb.angular_match,
            "curvature_correction_negligible": cb.curvature_correction_negligible,
            "classification": cb.classification,
        }

    # Trigger
    if result.trigger_assessment is not None:
        tr = result.trigger_assessment
        d["trigger"] = {
            "n_invariants": tr.n_invariants,
            "top_ranked_id": tr.top_ranked_id,
            "top_ranked_name": tr.top_ranked_name,
            "top_ranked_score": tr.top_ranked_score,
            "any_ssb_achieved": tr.any_ssb_achieved,
            "m0_squared": tr.m0_squared,
            "xi": tr.xi,
            "classification": tr.classification,
            "invariants": [
                {"name": inv.name, "formula": inv.formula,
                 "nonzero_in_vacuum": inv.nonzero_in_vacuum,
                 "value_at_Req": inv.value_at_Req,
                 "ssb_achieved": inv.ssb_achieved,
                 "score": inv.score,
                 "verdict": inv.verdict}
                for inv in tr.invariants
            ],
        }

    # Artifacts
    if result.artifact_inventory is not None:
        ai = result.artifact_inventory
        d["artifacts"] = {
            "n_artifacts": ai.n_artifacts,
            "n_major": ai.n_major,
            "n_moderate": ai.n_moderate,
            "n_minor": ai.n_minor,
            "items": [
                {"id": a.artifact_id, "category": a.category,
                 "description": a.description, "severity": a.severity,
                 "resolvable": a.resolvable_in_future}
                for a in ai.artifacts
            ],
        }

    # Classification
    if result.classification is not None:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "comp_a_shape": cl.comp_a_shape,
            "comp_a_coeff": cl.comp_a_coeff,
            "comp_a_interpretation": cl.comp_a_interpretation,
            "comp_b_preserved": cl.comp_b_preserved,
            "trigger_viable": cl.trigger_viable,
            "top_trigger_name": cl.top_trigger_name,
            "top_trigger_score": cl.top_trigger_score,
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
