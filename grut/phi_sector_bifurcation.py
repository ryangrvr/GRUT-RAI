"""Phi (Φ) Sector Bifurcation Statement.

GRUT uses a single symbol Φ across two structurally distinct regimes:

  Φ_trajectory  — the collapse sector memory field M_drive(t), evaluated at
                  the moving shell position R(t).  A single degree of freedom.

  Φ_field       — the constitutive sector relaxation field Φ(r, t), a
                  spatially distributed object with equilibrium profile M/r².

Both satisfy the same governing ODE:

    τ_eff · dΦ/dt + Φ = X

but with different domains:
  - Trajectory regime: X = GM/R², evaluated at the shell, point-valued.
  - Field regime:      X = M/r², evaluated at all r, spatially distributed.

At static equilibrium both regimes satisfy X - Φ = 0 (self-healing condition):
  - Trajectory:  M_drive → GM/R_eq²   (single value)
  - Field:       Φ(r) → M/r²          (spatial profile)

These fixed points AGREE at r = R_eq, i.e.:
  M_drive(R_eq) = GM/R_eq² = Φ_field(R_eq)

This is the ONLY point of guaranteed agreement.  Outside R_eq, or away from
static equilibrium, the two regimes diverge structurally.

PRINCIPAL RESULTS
-----------------
  A. The two regimes are governed by the same ODE form, but differ in
     mathematical type: trajectory (0+1D, point-valued) vs. field (1+1D, r-distributed).

  B. Their identification at the equilibrium endpoint is a coincidence of
     fixed points, not a derivation of unity.  The assertion "Φ_collapse = α_vac
     ↔ Φ_constitutive saturated at X_eq" holds numerically at one radius but
     does not imply the two objects are the same.

  C. Matter localization built on Φ silently inherits either the field (spatial
     profile) or the trajectory (point value), depending on which sector is used.
     These give structurally different matter objects even though they agree at R_eq.

  D. A unified governing equation does not exist in the current architecture.
     It would require either: (1) a covariant field equation that reduces to the
     trajectory ODE in the point-particle limit, or (2) a formal projection map
     from Φ(r,t) to M_drive(t) that is self-consistent across the ODE.

BIFURCATION VERDICT
-------------------
  "two_distinct_objects__same_ode_form__different_domains__
   common_fixed_point_at_R_eq__identification_is_coincidence_not_derivation__
   matter_localization_must_declare_which_Phi"

NONCLAIMS
---------
  1. This module does NOT claim the two regimes are inconsistent — they agree
     at equilibrium by the self-healing condition.
  2. This module does NOT close the question of whether a unified equation exists.
  3. The fixed-point agreement (M_drive = Φ_field at R_eq) is real and useful;
     what it does NOT do is make the two objects identical away from that point.

References
----------
  collapse.py              — trajectory ODE dM_drive/dt = (a_grav - M_drive)/τ_eff
  action_principle.py      — constitutive ODE τ_eff·u^a∇_aΦ + Φ = X
  tov_interior.py          — static equilibrium: Φ(R_eq) = M/R_eq² (field sector)
  nonlocal_strong_field.py — self-healing condition: X - Φ = 0 at equilibrium
  barrier_action_sector.py — Equilibrium Source Degeneracy Theorem
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Locked constants (canonical GRUT equilibrium, β_Q = 2)
# ---------------------------------------------------------------------------
M_EXT: float = 0.5           # M = r_s/2 (geometric units)
R_EQ: float = 1.0 / 3.0     # R_eq = α_vac r_s = r_s/3
TAU_SQ: float = 1.5          # τ² = 3/2  (from equilibrium condition)
ALPHA_VAC: float = 1.0 / 3.0  # α_vac = 1/3

# Source term at equilibrium: X_eq = M/R_eq²
X_EQ: float = M_EXT / (R_EQ ** 2)  # = 0.5 / (1/9) = 4.5

# Trajectory value at equilibrium: M_drive → X_eq (numerically equal)
M_DRIVE_EQ: float = X_EQ  # = 4.5  (M/R_eq² in geometric units — same fixed point)

# Field profile at R_eq: Φ_field(R_eq) = M/R_eq² = X_eq
PHI_FIELD_AT_REQ: float = X_EQ  # = 4.5  (field sector, same fixed point)

# α_vac coincidence: Ψ_proxy = 1/(1+β_Q) = 1/3 = α_vac at β_Q = 2
# This is a SEPARATE numerical identity from Φ_field or M_drive.
PSI_PROXY: float = ALPHA_VAC  # = 1/3; NOT the same as M_drive or Φ_field


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class PhiRegime:
    """Description of one Φ sector regime."""
    name: str                     # "trajectory" or "field"
    symbol: str                   # "M_drive" or "Phi(r,t)"
    ode: str                      # governing ODE in symbolic form
    domain: str                   # "0+1D point-valued" or "1+1D r-distributed"
    source_X: str                 # how X is evaluated
    equilibrium_value: float      # Φ value at static equilibrium at R_eq
    equilibrium_formula: str      # symbolic expression for equilibrium value
    energy_density: str           # what energy density it produces (symbolic)
    bounds: str                   # "bounded [0, X_eq]" or "X_eq as attractor"
    units: str
    notes: List[str] = field(default_factory=list)


@dataclass
class FixedPointAgreement:
    """The single point of guaranteed agreement between the two regimes.

    Both regimes satisfy X - Phi = 0 at static equilibrium, evaluated at R_eq.
    This agreement is real, useful, and exact — but restricted to one radius.
    """
    trajectory_value: float      # M_drive at R_eq = M/R_eq² = 4.5
    field_value: float           # Phi_field(R_eq) = M/R_eq² = 4.5
    values_agree: bool           # True: both equal X_eq = 4.5
    agreement_radius: float      # R_eq = 1/3 (only guaranteed at this point)
    agreement_condition: str     # "static equilibrium, X - Phi = 0"
    agreement_mechanism: str     # "self-healing condition (nonlocal_strong_field.py)"
    is_coincidence: bool         # True: coincidence of fixed points, not unification
    notes: List[str] = field(default_factory=list)


@dataclass
class UnifiedEquationRequirement:
    """What would be needed to produce a genuine unified governing equation."""
    exists_currently: bool       # False
    option_a: str                # covariant field eq. reducing to trajectory in point limit
    option_b: str                # formal projection map Phi(r,t) → M_drive(t)
    blocking_gap: str            # what prevents each option currently
    notes: List[str] = field(default_factory=list)


@dataclass
class MatterLocalizationRisk:
    """Structural risk for matter built on Phi.

    If matter is localized using Phi, the spatial structure depends on
    WHICH regime is inherited:
      - Field regime → matter has spatial extent (profile 1/r²)
      - Trajectory regime → matter is a point object (one value at R)
    These are structurally different even though they agree at R_eq.
    """
    field_matter_profile: str    # "1/r² spatial distribution"
    trajectory_matter_profile: str  # "point value at R, no spatial extent"
    agree_at_R_eq: bool          # True: numerically identical at R_eq
    agree_away_from_R_eq: bool   # False: structurally different at all other r
    risk_statement: str
    quarantine_requirement: str  # what must be declared before matter claims


@dataclass
class PhiBifurcationResult:
    """Master result of the Phi sector bifurcation statement."""
    trajectory_regime: PhiRegime
    field_regime: PhiRegime
    fixed_point_agreement: FixedPointAgreement
    unified_equation: UnifiedEquationRequirement
    matter_risk: MatterLocalizationRisk
    bifurcation_verdict: str     # computed
    nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def build_trajectory_regime() -> PhiRegime:
    """Describe the collapse-sector Φ (M_drive) regime.

    M_drive is the memory state of gravitational acceleration at the shell.
    ODE: dM_drive/dt = (a_grav - M_drive) / τ_eff
    Equivalently: τ_eff · dM_drive/dt + M_drive = X = GM/R²
    Domain: single moving shell position R(t) — 0+1D, point-valued.
    """
    return PhiRegime(
        name="trajectory",
        symbol="M_drive(t)",
        ode="tau_eff * dM_drive/dt + M_drive = X   where X = GM/R^2 at shell R(t)",
        domain="0+1D point-valued — evaluated only at the moving shell R(t)",
        source_X="X = GM/R^2 (gravitational acceleration at shell position)",
        equilibrium_value=M_DRIVE_EQ,
        equilibrium_formula="M_drive → GM/R_eq^2 = M/R_eq^2 = X_eq",
        energy_density="implicit in collapse dynamics; not directly rho_eq = -M^2/(2tau^2 r^4)",
        bounds="bounded by force balance; M_drive in [0, GM/R^2] during infall",
        units="m/s^2 (gravitational acceleration units in SI; geometric: M/r^2)",
        notes=[
            "Collapse sector: collapse.py, ODE at lines ~209",
            "M_drive tracks instantaneous gravitational drive with memory lag",
            "At equilibrium R_eq: M_drive → a_grav(R_eq) = GM/R_eq^2 = X_eq",
            "The deceleration ratio a_out/a_in = 1/(1+beta_Q) = alpha_vac is a SEPARATE",
            "  derived quantity (effective_lapse.py), NOT M_drive itself",
            "M_drive is a scalar at a point, not a field profile",
        ],
    )


def build_field_regime() -> PhiRegime:
    """Describe the constitutive-sector Φ(r,t) field regime.

    Phi(r,t) is the distributed memory relaxation field satisfying the
    covariant constitutive ODE at each spatial point r.
    Domain: all r (or r in [R_eq, R_ext]) — 1+1D, spatially distributed.
    """
    return PhiRegime(
        name="field",
        symbol="Phi(r,t)",
        ode="tau_eff * dPhi/dt + Phi = X   where X = M/r^2 (source profile at each r)",
        domain="1+1D r-distributed — field defined at each r in [R_eq, R_ext]",
        source_X="X = M/r^2 (spatial profile; r-dependent source at each point)",
        equilibrium_value=PHI_FIELD_AT_REQ,
        equilibrium_formula="Phi_eq(r) = M/r^2 for all r  (static limit tau*dPhi/dt -> 0)",
        energy_density="rho_eq = -M^2 / (2 tau^2 r^4)  (negative; drives metric deficit)",
        bounds="attractor at X(r) = M/r^2; no hard upper bound",
        units="M/r^2 units (same dimension as X; geometric: M/r^2 where M is mass)",
        notes=[
            "Constitutive sector: action_principle.py, tov_interior.py",
            "Full equilibrium profile: Phi_eq(r) = M/r^2 for all r",
            "At r = R_eq: Phi_eq(R_eq) = M/R_eq^2 = X_eq (agrees with trajectory sector)",
            "Away from R_eq: Phi_field(r) = M/r^2 != M/R_eq^2 (spatial profile)",
            "rho_eq = -X^2/(2tau^2) = -M^2/(2tau^2 r^4) — negative energy density",
            "The Equilibrium Source Degeneracy Theorem (barrier_action_sector.py):",
            "  T^Phi_munu is UNDERDETERMINED from equilibrium constitutive primitives alone",
        ],
    )


def build_fixed_point_agreement(
    traj: PhiRegime, fld: PhiRegime
) -> FixedPointAgreement:
    """Verify and characterise the fixed-point agreement at R_eq.

    Both regimes satisfy tau * dPhi/dt + Phi = X with the same fixed point
    X(R_eq) = M/R_eq^2 = 4.5 at static equilibrium.  This agreement is real
    and exact at r = R_eq, but does NOT imply the two objects are the same.
    """
    tol = 1e-10
    agree = abs(traj.equilibrium_value - fld.equilibrium_value) < tol

    return FixedPointAgreement(
        trajectory_value=traj.equilibrium_value,
        field_value=fld.equilibrium_value,
        values_agree=agree,
        agreement_radius=R_EQ,
        agreement_condition="static equilibrium: tau * dPhi/dt = 0, so Phi = X",
        agreement_mechanism=(
            "self-healing condition (nonlocal_strong_field.py): X - Phi = 0 at equilibrium; "
            "same ODE form => same fixed point X(R_eq) for both regimes"
        ),
        is_coincidence=True,
        notes=[
            f"trajectory equilibrium value:  M_drive = X_eq = {traj.equilibrium_value:.4f}",
            f"field equilibrium value:       Phi(R_eq) = X_eq = {fld.equilibrium_value:.4f}",
            f"agreement at R_eq = {R_EQ:.4f}:  {agree}",
            "Agreement is EXACT at R_eq by the self-healing condition.",
            "Agreement is STRUCTURAL (both are fixed points of the same ODE form).",
            "Agreement does NOT hold for r != R_eq:",
            "  field: Phi_field(r) = M/r^2 varies with r",
            "  trajectory: M_drive is a single number at R, not a function of r",
            "is_coincidence = True: fixed-point agreement != object identity",
            "The assertion 'Phi_collapse = alpha_vac' refers to a RATIO (effective_lapse.py),",
            "  not to M_drive or Phi_field directly. See PSI_PROXY in this module.",
        ],
    )


def build_unified_equation_requirement() -> UnifiedEquationRequirement:
    """State what would be needed for a genuine unified Phi governing equation."""
    return UnifiedEquationRequirement(
        exists_currently=False,
        option_a=(
            "A covariant field equation tau_eff * u^a nabla_a Phi + Phi = X[g, T] "
            "that reduces to the trajectory ODE dM_drive/dt = (X - M_drive)/tau_eff "
            "in the point-particle limit (shell mass concentrated at R).  "
            "This requires: (1) a covariant source term X[g, T] that is well-defined "
            "both as a distributed field and at a point; (2) a covariant tau_eff that "
            "is not sector-dependent (see tau_eff_domain_declaration.py)."
        ),
        option_b=(
            "A formal projection map pi: Phi(r,t) -> M_drive(t) such that M_drive(t) = "
            "int Phi(r,t) * weight(r, R(t)) dr for some weight function, and such that "
            "M_drive satisfies the trajectory ODE if Phi satisfies the field equation.  "
            "This requires: verifying that the projection commutes with the ODE operator."
        ),
        blocking_gap=(
            "Currently absent: (1) no covariant X[g,T] defined across all regimes; "
            "(2) no explicit projection map from field to trajectory; "
            "(3) tau_eff is sector-fragmented (see tau_eff_domain_declaration.py), "
            "which prevents a single covariant ODE from reducing to all three contexts."
        ),
        notes=[
            "Unified equation does NOT currently exist in the architecture.",
            "The two regimes are formally consistent (same ODE, same fixed point).",
            "Formal consistency is weaker than mathematical identity of the objects.",
            "Option A and Option B are not equivalent — they would produce different",
            "  matter structures if both were implemented.",
        ],
    )


def build_matter_localization_risk() -> MatterLocalizationRisk:
    """Characterise the structural risk for matter built on Phi."""
    return MatterLocalizationRisk(
        field_matter_profile="1/r^2 spatial distribution (from Phi_eq(r) = M/r^2)",
        trajectory_matter_profile="point value at R — no spatial extent in r",
        agree_at_R_eq=True,
        agree_away_from_R_eq=False,
        risk_statement=(
            "Any matter claim that uses 'Phi' for localization, knotting, defect structure, "
            "or response-lock language implicitly inherits one of the two regimes.  "
            "The field regime gives matter with spatial profile 1/r^2; the trajectory regime "
            "gives matter as a structureless point.  These are different matter objects even "
            "though they agree at the single point r = R_eq.  Claims about matter shape, "
            "spatial extent, or radial response depend critically on which Phi is meant."
        ),
        quarantine_requirement=(
            "Before any matter-sector claim involving Phi, the following must be declared: "
            "(1) Which Phi regime is being used (field or trajectory). "
            "(2) Whether spatial profile (field: 1/r^2) or point value (trajectory: M/R^2) "
            "    is the relevant object for the matter claim. "
            "(3) Any result derived from Phi_field that is then applied to matter as a "
            "    localized object must explicitly justify why the field profile, not the "
            "    trajectory value, is the appropriate regime."
        ),
    )


def assign_bifurcation_verdict(
    agreement: FixedPointAgreement,
    unified: UnifiedEquationRequirement,
    risk: MatterLocalizationRisk,
) -> str:
    """Compute the bifurcation verdict from Boolean outcomes."""
    if not agreement.values_agree:
        return "numerical_disagreement_at_R_eq__fundamental_inconsistency"
    elif not unified.exists_currently and agreement.is_coincidence:
        return (
            "two_distinct_objects__same_ode_form__different_domains__"
            "common_fixed_point_at_R_eq__identification_is_coincidence_not_derivation__"
            "matter_localization_must_declare_which_Phi"
        )
    elif unified.exists_currently:
        return "unified_equation_exists__single_Phi_object"
    else:
        return "undetermined"


def run_phi_sector_bifurcation() -> PhiBifurcationResult:
    """Run the Phi sector bifurcation analysis.

    Returns a complete PhiBifurcationResult documenting the two regimes,
    their fixed-point agreement, the unified equation gap, and the
    matter localization risk.
    """
    traj = build_trajectory_regime()
    fld = build_field_regime()
    agreement = build_fixed_point_agreement(traj, fld)
    unified = build_unified_equation_requirement()
    risk = build_matter_localization_risk()
    verdict = assign_bifurcation_verdict(agreement, unified, risk)

    nonclaims = [
        "NOT claiming the two regimes are inconsistent — they agree at R_eq by the "
        "self-healing condition.",
        "NOT claiming a unified equation cannot exist — it is absent, not impossible.",
        "NOT claiming fixed-point agreement is meaningless — it is exact and structurally "
        "grounded; the nonclaim is only that fixed-point agreement != object identity.",
        "NOT claiming matter claims are invalid — they are suspended pending declaration "
        "of which Phi regime is intended.",
        "The deceleration ratio alpha_vac = 1/(1+beta_Q) = 1/3 is NOT M_drive or Phi_field; "
        "it is a separate kinematic object (effective_lapse.py Psi_proxy).",
    ]

    diagnostics: Dict[str, Any] = {
        "M_EXT": M_EXT,
        "R_EQ": R_EQ,
        "TAU_SQ": TAU_SQ,
        "ALPHA_VAC": ALPHA_VAC,
        "X_EQ": X_EQ,
        "M_DRIVE_EQ": M_DRIVE_EQ,
        "PHI_FIELD_AT_REQ": PHI_FIELD_AT_REQ,
        "PSI_PROXY": PSI_PROXY,
        "values_agree_at_R_eq": agreement.values_agree,
        "is_coincidence": agreement.is_coincidence,
        "unified_equation_exists": unified.exists_currently,
        "field_matter_profile": risk.field_matter_profile,
        "agree_away_from_R_eq": risk.agree_away_from_R_eq,
        "verdict": verdict,
    }

    return PhiBifurcationResult(
        trajectory_regime=traj,
        field_regime=fld,
        fixed_point_agreement=agreement,
        unified_equation=unified,
        matter_risk=risk,
        bifurcation_verdict=verdict,
        nonclaims=nonclaims,
        diagnostics=diagnostics,
    )
