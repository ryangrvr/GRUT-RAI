"""GRUT Appendix E — Pass 2: Stability and Consistency Audit Module.

Implements the four narrow deterministic checks identified in Pass 1:

  CHECK 1 — τ_eff self-consistency ratio per sector
  CHECK 2 — Q from three independent routes
  CHECK 3 — Φ boundary condition at the equilibrium endpoint
  CHECK 4 — T_Q2 extraction vs thermodynamic candidates

STATUS: DETERMINISTIC AUDIT ONLY
  This module does NOT run simulations, solve ODEs, or introduce new physics.
  It uses only published canonical parameters and published formulas.
  All four checks are algebraic/arithmetic — no integration required.

PASS 2 DETERMINATION (encoded in run_pass2_audit):
  locally_consistent_globally_underdetermined — UNCHANGED from Pass 1.

LOCKED INHERITANCE:
  - Appendix C: all quantum blockers in force (not touched here)
  - Q1–Q4: bounded recovery/spectral phase (not touched here)
  - Appendix D: thermodynamic_sector_partially_consistent (not touched here)
  - Appendix E Pass 1: locally_consistent_globally_underdetermined

WHAT THIS MODULE DOES NOT CLAIM:
  - Does NOT claim the τ tension is resolved
  - Does NOT claim Q is independently triangulated
  - Does NOT claim Φ identity is established (only endpoint consistency)
  - Does NOT claim temperature is determined
  - Does NOT upgrade Appendix E to "appears_coherent_in_claimed_regimes"
  - Does NOT run any simulation or solve any ODE
  - Does NOT assess any claim outside the four checks

ASSUMPTIONS EXPOSED:
  - τ_local = τ₀·t_dyn/(t_dyn+τ₀) is the interior PDE τ (interior_pde.py)
  - τ_eff = τ₀/(1+(|V/R|·τ₀)²) is the collapse/cosmology τ (collapse.py, Q2)
  - At equilibrium: V=0, M_drive=a_grav, R=R_eq=r_s/3
  - ω₀ = sqrt(β_Q·GM/R_eq³) at R_eq
  - Φ_barrier = ε_Q·(r_s/R_eq)^β_Q at equilibrium
  - Φ_constitutive at equilibrium = 1 (normalized steady-state)
  - T_Q2 = ℏ·Ω/k_B (Ω=1/τ₀) is NOT the bath temperature — category error
  - 4 temperature candidates from thermodynamic_sector.py (not 6)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

# ================================================================
# Physical Constants (SI)
# ================================================================

G_SI = 6.674e-11            # m^3 kg^-1 s^-2
C_SI = 299_792_458.0        # m/s
HBAR_SI = 1.054571817e-34   # J·s
K_B = 1.380649e-23          # J/K

# ================================================================
# Canonical GRUT Parameters (locked)
# ================================================================

TAU_0_S = 1.3225e15         # s   — Phase I anchor (τ₀)
ALPHA_VAC = 1.0 / 3.0       # dimensionless — vacuum susceptibility
BETA_Q = 2.0                # dimensionless — barrier exponent (ASSUMED, not derived)
EPSILON_Q = ALPHA_VAC ** 2  # = 1/9 — barrier amplitude (derived from α_vac at β_Q=2)
R_EQ_OVER_RS = EPSILON_Q ** (1.0 / BETA_Q)  # = 1/3 — endpoint ratio

# Reference mass
M_SUN_KG = 1.989e30         # kg
M_REF_KG = 30.0 * M_SUN_KG # 30 solar masses

# Quality factor (canonical, derived below)
Q_CANONICAL = BETA_Q / ALPHA_VAC   # = 6.0

# Structural identity value
OMEGA_0_TAU_LOCAL_IDENTITY = 1.0   # ω₀ · τ_local = 1 at equilibrium

# Forbidden classification strings (guard against unsupported claims)
_FORBIDDEN_PASS2_CLASSIFICATIONS = {
    "appears_coherent_in_claimed_regimes",
    "fully_consistent",
    "globally_consistent",
    "cross_sector_coherent",
}


# ================================================================
# Data Structures
# ================================================================

@dataclass
class Check1Result:
    """Result of Check 1: τ_eff self-consistency ratio per sector."""

    # Sector τ values at equilibrium (V=0, R=R_eq)
    tau_0_s: float = TAU_0_S

    # Collapse sector: τ_eff = τ₀/(1+(|V/R|·τ₀)²) at V=0
    tau_collapse_at_equilibrium_s: float = 0.0
    tau_collapse_meaning: str = "tau_eff from collapse formula at V=0: tau_0/(1+0^2) = tau_0"

    # Interior PDE sector: τ_local = τ₀·t_dyn/(t_dyn+τ₀) at R_eq
    tau_local_pde_s: float = 0.0
    t_dyn_s: float = 0.0
    tau_local_meaning: str = "tau_local from tier-0 closure: tau0*t_dyn/(t_dyn+tau0) approx t_dyn"

    # Self-consistency ratio
    tau_ratio: float = 0.0        # tau_collapse / tau_pde at equilibrium
    omega_0_tau_0: float = 0.0    # ω₀·τ₀ (same as ratio, for reference)
    omega_0_rad_s: float = 0.0    # ω₀ at reference mass

    # Q2 resonance check
    omega_0_actual_rad_s: float = 0.0     # ω₀ (astrophysical)
    omega_bath_cutoff_rad_s: float = 0.0  # Ω = 1/τ₀ (cosmological)
    resonance_ratio: float = 0.0          # ω₀ / Ω = ω₀ · τ₀
    resonance_holds_numerically: bool = False

    # Structural identity verification
    omega_0_tau_local: float = 0.0        # should be ≈ 1
    structural_identity_holds: bool = False

    # What type of τ the structural identity uses
    structural_identity_uses_tau: str = "tau_local (gravitational scaling, NOT tau_eff from constitutive law)"

    # Classification
    classification: str = ""
    # "tau_eff_boundedly_translatable"
    # "tau_eff_tensioned_across_sectors"
    # "tau_eff_structurally_contradictory"
    # "tau_eff_underdefined"

    # Assumptions
    assumptions: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tau_0_s": self.tau_0_s,
            "tau_collapse_at_equilibrium_s": self.tau_collapse_at_equilibrium_s,
            "tau_local_pde_s": self.tau_local_pde_s,
            "t_dyn_s": self.t_dyn_s,
            "tau_ratio": self.tau_ratio,
            "omega_0_rad_s": self.omega_0_rad_s,
            "omega_0_tau_0": self.omega_0_tau_0,
            "omega_bath_cutoff_rad_s": self.omega_bath_cutoff_rad_s,
            "resonance_ratio": self.resonance_ratio,
            "resonance_holds_numerically": self.resonance_holds_numerically,
            "omega_0_tau_local": self.omega_0_tau_local,
            "structural_identity_holds": self.structural_identity_holds,
            "structural_identity_uses_tau": self.structural_identity_uses_tau,
            "classification": self.classification,
            "assumptions": self.assumptions,
            "nonclaims": self.nonclaims,
        }


@dataclass
class Check2Result:
    """Result of Check 2: Q from three routes."""

    # Route A: Q = β_Q / α_vac (formula)
    q_route_a: float = 0.0
    q_route_a_formula: str = "Q = beta_Q / alpha_vac"
    q_route_a_assumptions: List[str] = field(default_factory=list)

    # Route B: Q from interior PDE damping
    q_route_b: float = 0.0
    q_route_b_formula: str = "Q = beta_Q / (alpha_vac * omega_0 * tau_local)"
    q_route_b_assumptions: List[str] = field(default_factory=list)
    route_b_reduces_to_a: bool = False   # True if algebraically identical

    # Route C: Q from interior waves damping
    q_route_c: float = 0.0
    q_route_c_formula: str = "Q = 2 / (alpha_vac * omega_0 * tau_local)"
    q_route_c_assumptions: List[str] = field(default_factory=list)
    route_c_beta_q_independent: bool = False  # True — does not depend on beta_Q

    # Agreement assessment
    all_agree: bool = False
    max_deviation_from_mean: float = 0.0

    # Independence test: do routes B and C agree at non-canonical beta_Q?
    q_route_b_at_beta_q_15: float = 0.0   # β_Q = 1.5 (non-canonical)
    q_route_c_at_beta_q_15: float = 0.0   # β_Q = 1.5 (should still = 6.0)
    routes_b_c_agree_at_noncanonical_beta_q: bool = False

    # W4 test
    beta_q_is_assumed_not_derived: bool = True
    beta_q_controls_routes_a_and_b: bool = True
    beta_q_does_not_control_route_c: bool = True

    # Shared hidden assumptions across all routes
    shared_assumptions: List[str] = field(default_factory=list)

    # Classification
    classification: str = ""
    # "q_triangulated_across_routes"
    # "q_consistent_but_assumption_loaded"
    # "q_numerically_aligned_but_not_independent"
    # "q_incoherent"

    nonclaims: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "q_route_a": self.q_route_a,
            "q_route_b": self.q_route_b,
            "q_route_c": self.q_route_c,
            "route_b_reduces_to_a": self.route_b_reduces_to_a,
            "route_c_beta_q_independent": self.route_c_beta_q_independent,
            "all_agree": self.all_agree,
            "q_route_b_at_beta_q_15": self.q_route_b_at_beta_q_15,
            "q_route_c_at_beta_q_15": self.q_route_c_at_beta_q_15,
            "routes_b_c_agree_at_noncanonical_beta_q": self.routes_b_c_agree_at_noncanonical_beta_q,
            "beta_q_is_assumed_not_derived": self.beta_q_is_assumed_not_derived,
            "beta_q_controls_routes_a_and_b": self.beta_q_controls_routes_a_and_b,
            "beta_q_does_not_control_route_c": self.beta_q_does_not_control_route_c,
            "shared_assumptions": self.shared_assumptions,
            "classification": self.classification,
            "nonclaims": self.nonclaims,
        }


@dataclass
class Check3Result:
    """Result of Check 3: Φ boundary condition at endpoint."""

    # Reference mass used
    M_kg: float = M_REF_KG

    # Φ_barrier at R_eq
    phi_barrier_at_req: float = 0.0
    phi_barrier_formula: str = "Phi_barrier = epsilon_Q * (r_s/R_eq)^beta_Q"
    phi_barrier_expected: float = 1.0   # Should be 1 at R_eq by endpoint law

    # Φ_constitutive at R_eq (normalized steady-state)
    phi_constitutive_at_req: float = 0.0
    phi_constitutive_formula: str = "Phi_constitutive = M_drive/a_grav at steady state = 1"
    phi_constitutive_normalization: str = "M_drive/a_grav (dimensionless, steady-state = 1)"

    # Comparison
    phi_values_equal_at_req: bool = False
    phi_agreement_is_by_construction: bool = True  # Always True — see analysis

    # Off-equilibrium warning
    off_equilibrium_phi_barrier_formula: str = "epsilon_Q * (r_s/R)^beta_Q — function of R only"
    off_equilibrium_phi_constitutive_formula: str = "M_drive(t)/a_grav(t) — history-dependent ODE solution"
    off_equilibrium_tracking_is_same: bool = False   # They are genuinely different off-R_eq

    # Action-principle Φ
    action_phi_comparison: str = "underdetermined — covariant source X in tau*dPhi/dt + Phi = X not explicit"

    # Classification
    classification: str = ""
    # "phi_endpoint_relation_viable"
    # "phi_endpoint_relation_tensioned"
    # "phi_dual_use_notational_only"
    # "phi_dual_use_structural_conflict"
    # "phi_relation_underdetermined"

    classification_off_equilibrium: str = "phi_relation_underdetermined"

    nonclaims: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "M_kg": self.M_kg,
            "phi_barrier_at_req": self.phi_barrier_at_req,
            "phi_constitutive_at_req": self.phi_constitutive_at_req,
            "phi_values_equal_at_req": self.phi_values_equal_at_req,
            "phi_agreement_is_by_construction": self.phi_agreement_is_by_construction,
            "off_equilibrium_tracking_is_same": self.off_equilibrium_tracking_is_same,
            "action_phi_comparison": self.action_phi_comparison,
            "classification": self.classification,
            "classification_off_equilibrium": self.classification_off_equilibrium,
            "nonclaims": self.nonclaims,
        }


@dataclass
class TemperatureCandidateSummary:
    """Numeric summary of one Appendix D temperature candidate."""
    name: str
    formula: str
    T_kelvin: float
    grut_native: bool
    derivation_status: str


@dataclass
class Check4Result:
    """Result of Check 4: T_Q2 vs thermodynamic candidates."""

    # Q2 bath cutoff
    omega_cutoff_rad_s: float = 0.0    # Ω = 1/τ₀
    tau_0_s: float = TAU_0_S

    # The (incorrect) T_Q2 formula from Pass 1
    t_q2_category_error_formula: str = "T_Q2 = hbar * Omega / k_B = hbar / (k_B * tau_0)"
    t_q2_category_error_kelvin: float = 0.0
    t_q2_is_category_error: bool = True  # Always True
    t_q2_error_explanation: str = (
        "In the Drude bath model J(omega)=eta*omega*Omega^2/(omega^2+Omega^2), "
        "the temperature T is an INDEPENDENT parameter that enters the FDT as "
        "S(omega) = 2*k_B*T * Im[chi(omega)] / omega. "
        "hbar*Omega/k_B is the cutoff energy, not the bath temperature. "
        "T_Q2 as defined in Pass 1 conflates these two distinct quantities."
    )

    # What Q2 actually constrains
    q2_constrains_bath_shape: bool = True
    q2_constrains_bath_cutoff: bool = True
    q2_constrains_bath_temperature: bool = False   # This is the key finding

    # Reference mass for temperature comparison
    M_kg: float = M_REF_KG

    # Four temperature candidates (from thermodynamic_sector.py)
    candidates: List[TemperatureCandidateSummary] = field(default_factory=list)
    n_candidates: int = 4  # Not 6 — Pass 1 overestimated

    # Comparison
    t_q2_matches_any_candidate_within_factor_2: bool = False
    t_q2_orders_of_magnitude_below_lowest_candidate: float = 0.0
    lowest_candidate_T_kelvin: float = 0.0

    # Resonance check (from Check 1 finding)
    q2_resonance_condition_holds_numerically: bool = False
    q2_resonance_note: str = (
        "Q2 claims omega_0 = Omega = 1/tau_0 (resonance condition). "
        "Numerically: omega_0 ~ 1.76e4 rad/s, Omega = 1/tau_0 ~ 7.56e-16 rad/s. "
        "These differ by ~2.3e19. Resonance does NOT hold numerically. "
        "It holds only between omega_0 and 1/tau_local (not 1/tau_0)."
    )

    # Q4 status after this check
    q4_temperature_deficit_unchanged: bool = True

    # Classification
    classification: str = ""
    # "q2_temperature_supports_one_candidate"
    # "q2_temperature_narrows_but_does_not_resolve"
    # "q2_temperature_noninformative"
    # "q2_temperature_conflicts_with_appendix_d"

    nonclaims: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "omega_cutoff_rad_s": self.omega_cutoff_rad_s,
            "t_q2_category_error_kelvin": self.t_q2_category_error_kelvin,
            "t_q2_is_category_error": self.t_q2_is_category_error,
            "t_q2_error_explanation": self.t_q2_error_explanation,
            "q2_constrains_bath_shape": self.q2_constrains_bath_shape,
            "q2_constrains_bath_cutoff": self.q2_constrains_bath_cutoff,
            "q2_constrains_bath_temperature": self.q2_constrains_bath_temperature,
            "n_candidates": self.n_candidates,
            "candidates": [
                {"name": c.name, "T_kelvin": c.T_kelvin,
                 "grut_native": c.grut_native, "formula": c.formula}
                for c in self.candidates
            ],
            "t_q2_matches_any_candidate_within_factor_2": self.t_q2_matches_any_candidate_within_factor_2,
            "t_q2_orders_of_magnitude_below_lowest_candidate": self.t_q2_orders_of_magnitude_below_lowest_candidate,
            "q2_resonance_condition_holds_numerically": self.q2_resonance_condition_holds_numerically,
            "q4_temperature_deficit_unchanged": self.q4_temperature_deficit_unchanged,
            "classification": self.classification,
            "nonclaims": self.nonclaims,
        }


@dataclass
class Pass2AuditResult:
    """Master result from Appendix E Pass 2."""
    check1: Check1Result = field(default_factory=Check1Result)
    check2: Check2Result = field(default_factory=Check2Result)
    check3: Check3Result = field(default_factory=Check3Result)
    check4: Check4Result = field(default_factory=Check4Result)

    # Integrated assessment
    most_reduced_root_failure: str = ""
    strongest_remaining_blocker: str = ""
    pass2_overall_determination: str = ""
    classification_unchanged: bool = True

    # Guard: this must never appear in the determination
    _forbidden_classifications: List[str] = field(
        default_factory=lambda: list(_FORBIDDEN_PASS2_CLASSIFICATIONS)
    )

    valid: bool = False

    def assert_no_unsupported_claims(self) -> None:
        """Raise AssertionError if any result claims full consistency."""
        for forbidden in self._forbidden_classifications:
            if forbidden in self.pass2_overall_determination:
                raise AssertionError(
                    f"FORBIDDEN CLAIM in pass2_overall_determination: '{forbidden}'. "
                    f"This classification is not supported by the four checks."
                )
            if forbidden in self.check1.classification:
                raise AssertionError(f"FORBIDDEN CLAIM in check1: '{forbidden}'")
            if forbidden in self.check2.classification:
                raise AssertionError(f"FORBIDDEN CLAIM in check2: '{forbidden}'")
            if forbidden in self.check3.classification:
                raise AssertionError(f"FORBIDDEN CLAIM in check3: '{forbidden}'")
            if forbidden in self.check4.classification:
                raise AssertionError(f"FORBIDDEN CLAIM in check4: '{forbidden}'")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "check1": self.check1.to_dict(),
            "check2": self.check2.to_dict(),
            "check3": self.check3.to_dict(),
            "check4": self.check4.to_dict(),
            "most_reduced_root_failure": self.most_reduced_root_failure,
            "strongest_remaining_blocker": self.strongest_remaining_blocker,
            "pass2_overall_determination": self.pass2_overall_determination,
            "classification_unchanged": self.classification_unchanged,
            "valid": self.valid,
        }


# ================================================================
# Check Implementations
# ================================================================

def run_check1(M_kg: float = M_REF_KG) -> Check1Result:
    """Check 1: τ_eff self-consistency ratio per sector.

    Computes τ at equilibrium from both the dynamic formula (collapse sector)
    and the tier-0 local closure (interior PDE sector), and reports the ratio.

    Parameters
    ----------
    M_kg : float
        Reference mass in kg.

    Returns
    -------
    Check1Result
    """
    result = Check1Result()
    result.tau_0_s = TAU_0_S

    # Derived equilibrium quantities
    r_s = 2.0 * G_SI * M_kg / C_SI**2
    R_eq = R_EQ_OVER_RS * r_s   # = r_s/3

    # Local dynamical time at R_eq
    t_dyn = math.sqrt(R_eq**3 / (2.0 * G_SI * M_kg))
    result.t_dyn_s = t_dyn

    # ── Collapse sector τ at equilibrium (V=0) ──────────────────
    # tau_eff = tau_0 / (1 + (|V/R| * tau_0)^2)
    # At V=0: tau_eff = tau_0
    tau_collapse = TAU_0_S
    result.tau_collapse_at_equilibrium_s = tau_collapse

    # ── Interior PDE τ (tier-0 local closure) ───────────────────
    # tau_local = tau_0 * t_dyn / (t_dyn + tau_0)
    tau_local = TAU_0_S * t_dyn / (t_dyn + TAU_0_S)
    result.tau_local_pde_s = tau_local

    # ── Self-consistency ratio ───────────────────────────────────
    ratio = tau_collapse / tau_local if tau_local > 0 else float("inf")
    result.tau_ratio = ratio

    # ── ω₀ at R_eq ───────────────────────────────────────────────
    omega_g_sq = G_SI * M_kg / R_eq**3
    omega_0 = math.sqrt(BETA_Q * omega_g_sq)
    result.omega_0_rad_s = omega_0
    result.omega_0_actual_rad_s = omega_0

    # ── ω₀ · τ₀ ratio ────────────────────────────────────────────
    result.omega_0_tau_0 = omega_0 * TAU_0_S

    # ── Bath cutoff frequency ─────────────────────────────────────
    omega_bath = 1.0 / TAU_0_S   # Ω = 1/τ₀
    result.omega_bath_cutoff_rad_s = omega_bath

    # ── Resonance check ──────────────────────────────────────────
    # Q2 claims ω₀ = Ω = 1/τ₀. Is this numerically true?
    resonance_ratio = omega_0 / omega_bath if omega_bath > 0 else float("inf")
    result.resonance_ratio = resonance_ratio
    # Resonance holds if ratio ≈ 1 (within 10%)
    result.resonance_holds_numerically = abs(resonance_ratio - 1.0) < 0.1

    # ── Structural identity ──────────────────────────────────────
    # ω₀ · τ_local should be ≈ 1 (gravitational scaling)
    omega_0_tau_local = omega_0 * tau_local
    result.omega_0_tau_local = omega_0_tau_local
    result.structural_identity_holds = abs(omega_0_tau_local - 1.0) < 0.05  # 5% tolerance

    # ── Classification ───────────────────────────────────────────
    # The two τ formulas give values differing by ~10^19 at equilibrium.
    # This is not a translation (H ~ |V/R| ~ ω are all well-defined substitutions),
    # but the τ objects refer to different physical closures:
    # - τ_collapse at V=0 = τ₀ (constitutive law evaluated at static limit)
    # - τ_local (interior PDE) = t_dyn (gravitational scaling, tier-0 closure)
    # These are different formulas, not the same formula with different ω.
    result.classification = "tau_eff_tensioned_across_sectors"

    result.assumptions = [
        "tau_collapse at V=0: tau_eff = tau_0 / (1 + (|V/R|*tau_0)^2) evaluated at V=0 gives tau_0",
        "tau_local in interior PDE: tau_local = tau_0*t_dyn/(t_dyn+tau_0) (tier-0 closure)",
        "t_dyn = sqrt(R_eq^3 / (2GM)) at equilibrium",
        "omega_0 = sqrt(beta_Q * GM / R_eq^3)",
        "Structural identity: omega_0 * tau_local = 1 (gravitational scaling, not constitutive property)",
    ]

    result.nonclaims = [
        "Does NOT claim tau tension is resolved by covariant formulation",
        "Does NOT claim the two tau formulas are limit cases of the same formula",
        "Does NOT claim the structural identity omega_0*tau=1 holds for tau_0 (it does not)",
        "Does NOT assess the cosmological sector tau separately (H-scale; same formula as collapse)",
    ]

    return result


def run_check2(M_kg: float = M_REF_KG) -> Check2Result:
    """Check 2: Q from three independent routes.

    Computes Q via three algebraic routes and tests their independence.

    Parameters
    ----------
    M_kg : float
        Reference mass in kg.

    Returns
    -------
    Check2Result
    """
    result = Check2Result()

    # Shared quantities needed for Routes B and C
    r_s = 2.0 * G_SI * M_kg / C_SI**2
    R_eq = R_EQ_OVER_RS * r_s
    t_dyn = math.sqrt(R_eq**3 / (2.0 * G_SI * M_kg))
    tau_local = TAU_0_S * t_dyn / (t_dyn + TAU_0_S)
    omega_g_sq = G_SI * M_kg / R_eq**3
    omega_0 = math.sqrt(BETA_Q * omega_g_sq)
    omega_0_tau_local = omega_0 * tau_local   # ≈ 1

    # ── Route A: Q = β_Q / α_vac (formula route) ────────────────
    q_a = BETA_Q / ALPHA_VAC
    result.q_route_a = q_a
    result.q_route_a_assumptions = [
        "beta_Q = 2 (ASSUMED, not derived)",
        "alpha_vac = 1/3 (locked)",
    ]

    # ── Route B: PDE damping route ────────────────────────────────
    # gamma_PDE = alpha_vac * omega_g^2 * tau_local / (1 + (omega_0*tau_local)^2)
    # At omega_0*tau_local = 1: gamma_PDE = alpha_vac * (omega_0^2/beta_Q) * tau_local / 2
    # Q_B = omega_0 / (2 * gamma_PDE) = beta_Q / (alpha_vac * omega_0 * tau_local)
    gamma_pde = ALPHA_VAC * omega_g_sq * tau_local / (1.0 + omega_0_tau_local**2)
    q_b = omega_0 / (2.0 * gamma_pde) if gamma_pde > 0 else float("inf")
    result.q_route_b = q_b
    result.q_route_b_assumptions = [
        "gamma_PDE = alpha_vac * omega_g^2 * tau_local / (1 + (omega_0*tau_local)^2)",
        "tau_local (interior PDE tier-0 closure)",
        "omega_0 * tau_local ≈ 1 (structural identity)",
        "beta_Q = 2 (via omega_g^2 = omega_0^2/beta_Q)",
        "alpha_vac = 1/3",
    ]
    # Routes A and B are algebraically identical at omega_0*tau_local = 1:
    # Q_B = beta_Q / (alpha_vac * 1) = Q_A
    result.route_b_reduces_to_a = abs(q_b - q_a) < 1e-6 * q_a

    # ── Route C: Interior waves damping ──────────────────────────
    # gamma_mem = alpha_vac * omega_0^2 * tau_local / (2 * (1 + (omega_0*tau_local)^2))
    # Q_C = omega_0 / (2 * gamma_mem) = 2 / (alpha_vac * omega_0 * tau_local)
    gamma_mem = ALPHA_VAC * omega_0**2 * tau_local / (2.0 * (1.0 + omega_0_tau_local**2))
    q_c = omega_0 / (2.0 * gamma_mem) if gamma_mem > 0 else float("inf")
    result.q_route_c = q_c
    result.q_route_c_assumptions = [
        "gamma_mem = alpha_vac * omega_0^2 * tau_local / (2*(1+(omega_0*tau_local)^2))",
        "tau_local (interior PDE tier-0 closure)",
        "omega_0 * tau_local ≈ 1 (structural identity)",
        "alpha_vac = 1/3",
        "Does NOT depend on beta_Q explicitly",
    ]
    # Route C: Q_C = 2 / alpha_vac (independent of beta_Q)
    result.route_c_beta_q_independent = True   # By construction — see formula

    # ── Agreement check ──────────────────────────────────────────
    qs = [q_a, q_b, q_c]
    q_mean = sum(qs) / len(qs)
    result.all_agree = max(abs(q - q_mean) / q_mean for q in qs) < 0.01
    result.max_deviation_from_mean = max(abs(q - q_mean) / q_mean for q in qs)

    # ── β_Q independence test at β_Q = 1.5 ──────────────────────
    beta_q_test = 1.5
    omega_0_test = math.sqrt(beta_q_test * omega_g_sq)
    omega_0_tau_test = omega_0_test * tau_local

    # Route B at β_Q = 1.5:
    gamma_pde_test = ALPHA_VAC * omega_g_sq * tau_local / (1.0 + omega_0_tau_test**2)
    q_b_test = omega_0_test / (2.0 * gamma_pde_test) if gamma_pde_test > 0 else float("inf")
    result.q_route_b_at_beta_q_15 = q_b_test
    # Algebraically: Q_B = beta_Q / (alpha_vac * omega_0_test * tau_local)
    # omega_0_test * tau_local ≈ sqrt(beta_q_test) / sqrt(BETA_Q) (from scaling)
    # So Q_B_test = beta_q_test / (alpha_vac * sqrt(beta_q_test)/sqrt(BETA_Q))
    #             = sqrt(beta_q_test) * sqrt(BETA_Q) / alpha_vac
    # At beta_q_test = 1.5, BETA_Q = 2: Q_B_test = sqrt(3) / alpha_vac = sqrt(3) * 3 ≈ 5.196

    # Route C at β_Q = 1.5 (does NOT depend on beta_Q):
    gamma_mem_test = ALPHA_VAC * omega_0_test**2 * tau_local / (2.0 * (1.0 + omega_0_tau_test**2))
    q_c_test = omega_0_test / (2.0 * gamma_mem_test) if gamma_mem_test > 0 else float("inf")
    result.q_route_c_at_beta_q_15 = q_c_test
    # Route C always gives Q = 2/alpha_vac = 6 if omega_0*tau = 1.
    # But at beta_q = 1.5, omega_0*tau ≠ 1, so the actual value will drift.

    result.routes_b_c_agree_at_noncanonical_beta_q = abs(q_b_test - q_c_test) < 0.01

    # ── Shared assumptions ───────────────────────────────────────
    result.shared_assumptions = [
        "alpha_vac = 1/3 (all three routes)",
        "omega_0 * tau_local = 1 (structural identity — gravitational scaling, all three routes)",
        "tau_local from tier-0 closure (Routes B and C share this)",
        "beta_Q = 2 (Routes A and B explicitly; Route C at canonical beta_Q implicitly via tau_local scaling)",
    ]

    # ── Classification ───────────────────────────────────────────
    # Routes A and B are algebraically degenerate (same formula).
    # All three share omega_0*tau_local = 1 as a hidden assumption.
    # Agreement is a consequence of shared assumptions, not independent measurement.
    result.classification = "q_numerically_aligned_but_not_independent"

    result.nonclaims = [
        "Does NOT claim Q = 6 is independently verified by three measurements",
        "Does NOT claim Q is cross-sector triangulated",
        "Does NOT claim beta_Q = 2 is confirmed by route agreement",
        "Does NOT assess Q from thermodynamic sector (imports Q_canonical = 6 hardcoded)",
    ]

    return result


def run_check3(M_kg: float = M_REF_KG) -> Check3Result:
    """Check 3: Φ boundary condition at equilibrium endpoint.

    Computes Φ_barrier and Φ_constitutive at R_eq and compares.

    Parameters
    ----------
    M_kg : float
        Reference mass in kg.

    Returns
    -------
    Check3Result
    """
    result = Check3Result(M_kg=M_kg)

    # ── Φ_barrier at R_eq ────────────────────────────────────────
    # Phi_barrier(R) = epsilon_Q * (r_s/R)^beta_Q
    # At R = R_eq = r_s/3: epsilon_Q * (r_s/(r_s/3))^beta_Q = epsilon_Q * 3^beta_Q
    phi_barrier = EPSILON_Q * (3.0 ** BETA_Q)
    result.phi_barrier_at_req = phi_barrier
    # Verify: (1/9) * 3^2 = (1/9) * 9 = 1.0

    # ── Φ_constitutive at R_eq (normalized) ─────────────────────
    # Steady-state of tau dM_drive/dt + M_drive = a_grav:
    # M_drive_steady = a_grav  →  M_drive/a_grav = 1
    phi_constitutive = 1.0
    result.phi_constitutive_at_req = phi_constitutive

    # ── Comparison ───────────────────────────────────────────────
    result.phi_values_equal_at_req = abs(phi_barrier - phi_constitutive) < 1e-10

    # This equality is by construction: R_eq is defined as the point where
    # a_Q = a_inward → Phi_barrier = 1. And the constitutive steady-state = 1.
    result.phi_agreement_is_by_construction = True

    # ── Off-equilibrium assessment ────────────────────────────────
    # Phi_barrier(R) = epsilon_Q * (r_s/R)^beta_Q — instantaneous function of R
    # Phi_constitutive(t) = M_drive(t)/a_grav(t) — history-dependent ODE
    # These track R differently and cannot be equated off-equilibrium.
    result.off_equilibrium_tracking_is_same = False

    # ── Classification ───────────────────────────────────────────
    result.classification = "phi_endpoint_relation_viable"
    result.classification_off_equilibrium = "phi_relation_underdetermined"

    result.nonclaims = [
        "Does NOT claim Phi_barrier and Phi_constitutive are the same physical field",
        "Does NOT claim the endpoint agreement persists off-equilibrium",
        "Does NOT resolve the action-principle Phi comparison (source X is not explicit)",
        "Does NOT claim the endpoint check provides a derivation of the endpoint law",
        "Agreement at R_eq is a consequence of the endpoint law construction, not independent",
    ]

    return result


def run_check4(M_kg: float = M_REF_KG) -> Check4Result:
    """Check 4: T_Q2 extraction vs thermodynamic candidates.

    Identifies T_Q2 as a category error and reports the four
    Appendix D temperature candidates numerically.

    Parameters
    ----------
    M_kg : float
        Reference mass in kg.

    Returns
    -------
    Check4Result
    """
    result = Check4Result(M_kg=M_kg)

    # ── Bath cutoff ───────────────────────────────────────────────
    omega_cutoff = 1.0 / TAU_0_S   # Ω = 1/τ₀
    result.omega_cutoff_rad_s = omega_cutoff

    # ── T_Q2 (the category error) ─────────────────────────────────
    # This is NOT the bath temperature. It is the energy of the bath cutoff.
    t_q2_wrong = HBAR_SI * omega_cutoff / K_B
    result.t_q2_category_error_kelvin = t_q2_wrong
    result.t_q2_is_category_error = True
    result.q2_constrains_bath_temperature = False

    # ── Derived quantities at reference mass ─────────────────────
    r_s = 2.0 * G_SI * M_kg / C_SI**2
    R_eq = R_EQ_OVER_RS * r_s
    omega_g_sq = G_SI * M_kg / R_eq**3
    omega_0 = math.sqrt(BETA_Q * omega_g_sq)
    # tau_local = 1/omega_0 at equilibrium (structural identity)
    tau_local = 1.0 / omega_0

    # Effective "surface gravity" proxy: kappa_eff = omega_0^2 * R_eq
    kappa_eff = omega_0**2 * R_eq

    # Standard Hawking temperature
    T_hawking = HBAR_SI * C_SI**3 / (8.0 * math.pi * G_SI * M_kg * K_B)

    # T1: Surface-gravity analog
    T_sg = HBAR_SI * kappa_eff / (2.0 * math.pi * K_B)

    # T2: Dissipation temperature T = hbar*omega_0 / (Q*k_B)
    T_diss = HBAR_SI * omega_0 / (Q_CANONICAL * K_B)

    # T3: Structural-identity temperature T = hbar*omega_0 / k_B
    T_struct = HBAR_SI * omega_0 / K_B

    # T4: Standard Hawking (imported)
    T_hawk = T_hawking

    result.candidates = [
        TemperatureCandidateSummary(
            name="T_surface_gravity",
            formula="hbar * kappa_eff / (2*pi*k_B)",
            T_kelvin=T_sg,
            grut_native=False,
            derivation_status="analog_of_standard",
        ),
        TemperatureCandidateSummary(
            name="T_dissipation",
            formula="hbar * omega_0 / (Q * k_B)",
            T_kelvin=T_diss,
            grut_native=True,
            derivation_status="derived_from_grut",
        ),
        TemperatureCandidateSummary(
            name="T_structural",
            formula="hbar * omega_0 / k_B",
            T_kelvin=T_struct,
            grut_native=True,
            derivation_status="derived_from_grut",
        ),
        TemperatureCandidateSummary(
            name="T_hawking",
            formula="hbar * c^3 / (8*pi*G*M*k_B)",
            T_kelvin=T_hawk,
            grut_native=False,
            derivation_status="imported",
        ),
    ]
    result.n_candidates = 4

    # ── Comparison ────────────────────────────────────────────────
    all_T = [c.T_kelvin for c in result.candidates if c.T_kelvin > 0]
    lowest_T = min(all_T) if all_T else 0.0
    result.lowest_candidate_T_kelvin = lowest_T

    if lowest_T > 0 and t_q2_wrong > 0:
        ratio = lowest_T / t_q2_wrong
        result.t_q2_orders_of_magnitude_below_lowest_candidate = math.log10(ratio)
        result.t_q2_matches_any_candidate_within_factor_2 = (
            ratio < 2.0 and ratio > 0.5
        )
    else:
        result.t_q2_matches_any_candidate_within_factor_2 = False

    # ── Resonance check ───────────────────────────────────────────
    # ω₀ vs Ω = 1/τ₀
    resonance_ratio = omega_0 / omega_cutoff if omega_cutoff > 0 else float("inf")
    result.q2_resonance_condition_holds_numerically = abs(resonance_ratio - 1.0) < 0.1

    # ── Classification ────────────────────────────────────────────
    # Q2 bath identification specifies the bath spectral shape and cutoff.
    # Temperature T is a separate free parameter in the FDT.
    # T_Q2 = hbar*Omega/k_B is a category error (cutoff energy ≠ bath temperature).
    # No comparison to Appendix D candidates is possible from Q2 alone.
    result.classification = "q2_temperature_noninformative"
    result.q4_temperature_deficit_unchanged = True

    result.nonclaims = [
        "Does NOT claim T_Q2 = hbar/(k_B*tau_0) is the bath temperature",
        "Does NOT claim Q2 constrains the bath temperature",
        "Does NOT claim the Drude bath resonance condition holds numerically (it does not)",
        "Does NOT narrow the Appendix D temperature candidates",
        "Does NOT resolve Q4 (temperature as missing ingredient)",
        "Does NOT upgrade thermodynamic_sector from partially_consistent",
    ]

    return result


# ================================================================
# Master Entry Point
# ================================================================

def run_pass2_audit(M_kg: float = M_REF_KG) -> Pass2AuditResult:
    """Run all four Pass 2 checks and return integrated result.

    Parameters
    ----------
    M_kg : float
        Reference mass in kg (default: 30 M_sun).

    Returns
    -------
    Pass2AuditResult
        Full audit result with all four checks and integrated assessment.

    Notes
    -----
    This function does NOT run simulations. All computations are algebraic.
    The overall determination is LOCKED to locally_consistent_globally_underdetermined.
    No check result can upgrade to a full consistency classification.
    """
    result = Pass2AuditResult()

    result.check1 = run_check1(M_kg)
    result.check2 = run_check2(M_kg)
    result.check3 = run_check3(M_kg)
    result.check4 = run_check4(M_kg)

    # ── Integrated assessment ─────────────────────────────────────
    result.most_reduced_root_failure = (
        "root_failure_2_phi_dual_use: endpoint consistency established (viable). "
        "Both Phi objects equal 1 at R_eq by construction of the endpoint law. "
        "Off-equilibrium identity remains underdetermined."
    )

    result.strongest_remaining_blocker = (
        "root_failure_1_tau_eff_non_covariance: The structural identity omega_0*tau=1 "
        "uses tau_local (gravitational scaling), not tau_eff from the constitutive law. "
        f"At equilibrium: tau_collapse = tau_0 ~ {TAU_0_S:.2e} s, "
        f"tau_local ≈ t_dyn (astrophysical scale). "
        "The Q2 resonance condition omega_0 = Omega = 1/tau_0 is numerically false "
        "by a factor of omega_0*tau_0 ~ 10^19 for astrophysical masses."
    )

    # LOCKED classification — cannot be upgraded by the four checks
    result.pass2_overall_determination = "locally_consistent_globally_underdetermined"
    result.classification_unchanged = True

    # ── Guard ─────────────────────────────────────────────────────
    result.assert_no_unsupported_claims()

    result.valid = True
    return result
