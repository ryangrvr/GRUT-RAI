"""Tests for grut/phi_sector_bifurcation.py — Phi Sector Bifurcation Statement.

Covers:
  TestConstants               — X_EQ, M_DRIVE_EQ, PHI_FIELD_AT_REQ, PSI_PROXY
  TestTrajectoryRegime        — domain, ODE, equilibrium, energy_density
  TestFieldRegime             — domain, ODE, equilibrium, rho_eq profile
  TestFixedPointAgreement     — values agree at R_eq; is_coincidence; away from R_eq
  TestUnifiedEquation         — exists_currently=False; both options documented
  TestMatterLocalizationRisk  — different profiles; quarantine requirement
  TestBifurcationVerdict      — computed from Booleans
  TestNonclaims               — no false claims about consistency or impossibility
  TestMasterAudit             — end-to-end run_phi_sector_bifurcation()
  TestCrossConsistency        — Phi_field ≠ alpha_vac; PSI_PROXY = alpha_vac
"""

from __future__ import annotations

import math
import pytest

from grut.phi_sector_bifurcation import (
    M_EXT, R_EQ, TAU_SQ, ALPHA_VAC,
    X_EQ, M_DRIVE_EQ, PHI_FIELD_AT_REQ, PSI_PROXY,
    build_trajectory_regime,
    build_field_regime,
    build_fixed_point_agreement,
    build_unified_equation_requirement,
    build_matter_localization_risk,
    assign_bifurcation_verdict,
    run_phi_sector_bifurcation,
)


class TestConstants:
    def test_m_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_r_eq(self):
        assert abs(R_EQ - 1.0 / 3.0) < 1e-10

    def test_tau_sq(self):
        assert abs(TAU_SQ - 1.5) < 1e-10

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_x_eq_formula(self):
        """X_eq = M/R_eq^2 = 0.5 / (1/9) = 4.5"""
        expected = M_EXT / (R_EQ ** 2)
        assert abs(X_EQ - expected) < 1e-10

    def test_x_eq_value(self):
        assert abs(X_EQ - 4.5) < 1e-10

    def test_m_drive_eq_equals_x_eq(self):
        """Trajectory equilibrium = X_eq (same fixed point)."""
        assert abs(M_DRIVE_EQ - X_EQ) < 1e-10

    def test_phi_field_at_req_equals_x_eq(self):
        """Field equilibrium at R_eq = X_eq (same fixed point)."""
        assert abs(PHI_FIELD_AT_REQ - X_EQ) < 1e-10

    def test_psi_proxy_equals_alpha_vac(self):
        """PSI_PROXY = 1/(1+2) = 1/3 = alpha_vac (coincidence at beta_Q=2)."""
        expected = 1.0 / (1.0 + 2.0)
        assert abs(PSI_PROXY - expected) < 1e-10
        assert abs(PSI_PROXY - ALPHA_VAC) < 1e-10

    def test_psi_proxy_ne_phi_field(self):
        """PSI_PROXY = 1/3 but Phi_field(R_eq) = 4.5 — these are DIFFERENT objects."""
        assert abs(PSI_PROXY - PHI_FIELD_AT_REQ) > 1.0


class TestTrajectoryRegime:
    def setup_method(self):
        self.r = build_trajectory_regime()

    def test_name(self):
        assert self.r.name == "trajectory"

    def test_symbol(self):
        assert "M_drive" in self.r.symbol

    def test_ode_contains_tau_eff(self):
        assert "tau_eff" in self.r.ode.lower()

    def test_ode_contains_x(self):
        assert "X" in self.r.ode or "GM" in self.r.ode

    def test_domain_is_point_valued(self):
        assert "point" in self.r.domain.lower() or "0+1" in self.r.domain

    def test_equilibrium_value(self):
        assert abs(self.r.equilibrium_value - X_EQ) < 1e-10

    def test_not_rho_eq_profile(self):
        """Trajectory sector does not directly produce rho_eq = -M^2/(2tau^2 r^4)."""
        assert "implicit" in self.r.energy_density.lower() or "not directly" in self.r.energy_density.lower()

    def test_notes_mention_single_point(self):
        combined = " ".join(self.r.notes).lower()
        assert "scalar" in combined or "point" in combined or "single" in combined


class TestFieldRegime:
    def setup_method(self):
        self.r = build_field_regime()

    def test_name(self):
        assert self.r.name == "field"

    def test_symbol_contains_r_t(self):
        assert "r" in self.r.symbol and ("t" in self.r.symbol or "Phi" in self.r.symbol)

    def test_domain_is_distributed(self):
        assert "distributed" in self.r.domain.lower() or "1+1" in self.r.domain

    def test_equilibrium_value(self):
        assert abs(self.r.equilibrium_value - X_EQ) < 1e-10

    def test_equilibrium_formula_contains_r_dependence(self):
        """Phi_eq = M/r^2 for ALL r, not just R_eq."""
        assert "all r" in self.r.equilibrium_formula.lower() or "M/r" in self.r.equilibrium_formula

    def test_energy_density_negative(self):
        """rho_eq = -M^2/(2tau^2 r^4) < 0."""
        assert "-M^2" in self.r.energy_density or "-X^2" in self.r.energy_density

    def test_energy_density_radial_profile(self):
        """Energy density has 1/r^4 profile."""
        assert "r^4" in self.r.energy_density or "r4" in self.r.energy_density.lower()

    def test_notes_mention_source_degeneracy(self):
        combined = " ".join(self.r.notes).lower()
        assert "degeneracy" in combined or "underdetermined" in combined


class TestFixedPointAgreement:
    def setup_method(self):
        traj = build_trajectory_regime()
        fld = build_field_regime()
        self.a = build_fixed_point_agreement(traj, fld)

    def test_trajectory_value(self):
        assert abs(self.a.trajectory_value - X_EQ) < 1e-10

    def test_field_value(self):
        assert abs(self.a.field_value - X_EQ) < 1e-10

    def test_values_agree(self):
        """Both regimes have the same fixed point at R_eq."""
        assert self.a.values_agree is True

    def test_agreement_radius(self):
        assert abs(self.a.agreement_radius - R_EQ) < 1e-10

    def test_is_coincidence(self):
        """Agreement is a coincidence of fixed points, not object identity."""
        assert self.a.is_coincidence is True

    def test_mechanism_mentions_self_healing(self):
        assert "self-healing" in self.a.agreement_mechanism.lower() or "self_healing" in self.a.agreement_mechanism.lower()

    def test_notes_mention_away_from_R_eq(self):
        combined = " ".join(self.a.notes).lower()
        assert "away" in combined or "r != r_eq" in combined or "varies" in combined

    def test_psi_proxy_is_separate_object(self):
        """PSI_PROXY = 1/3 != X_eq = 4.5: the deceleration ratio is NOT M_drive or Phi_field."""
        # PSI_PROXY is neither trajectory_value nor field_value
        assert abs(PSI_PROXY - self.a.trajectory_value) > 1.0
        assert abs(PSI_PROXY - self.a.field_value) > 1.0


class TestUnifiedEquation:
    def setup_method(self):
        self.u = build_unified_equation_requirement()

    def test_does_not_exist_currently(self):
        assert self.u.exists_currently is False

    def test_option_a_documented(self):
        assert len(self.u.option_a) > 20
        assert "covariant" in self.u.option_a.lower() or "point-particle" in self.u.option_a.lower()

    def test_option_b_documented(self):
        assert len(self.u.option_b) > 20
        assert "projection" in self.u.option_b.lower() or "map" in self.u.option_b.lower()

    def test_blocking_gap_documented(self):
        assert len(self.u.blocking_gap) > 20
        assert "absent" in self.u.blocking_gap.lower() or "not" in self.u.blocking_gap.lower()

    def test_blocking_gap_mentions_tau_eff(self):
        assert "tau_eff" in self.u.blocking_gap.lower() or "tau" in self.u.blocking_gap.lower()


class TestMatterLocalizationRisk:
    def setup_method(self):
        self.r = build_matter_localization_risk()

    def test_field_matter_profile_is_1_over_r2(self):
        assert "1/r" in self.r.field_matter_profile or "r^2" in self.r.field_matter_profile.lower()

    def test_trajectory_matter_is_point(self):
        assert "point" in self.r.trajectory_matter_profile.lower()

    def test_agree_at_R_eq(self):
        assert self.r.agree_at_R_eq is True

    def test_disagree_away_from_R_eq(self):
        assert self.r.agree_away_from_R_eq is False

    def test_risk_statement_nonempty(self):
        assert len(self.r.risk_statement) > 50

    def test_quarantine_requirement_nonempty(self):
        assert len(self.r.quarantine_requirement) > 50

    def test_quarantine_mentions_which_phi(self):
        assert "which" in self.r.quarantine_requirement.lower() or "regime" in self.r.quarantine_requirement.lower()


class TestBifurcationVerdict:
    def setup_method(self):
        traj = build_trajectory_regime()
        fld = build_field_regime()
        agreement = build_fixed_point_agreement(traj, fld)
        unified = build_unified_equation_requirement()
        risk = build_matter_localization_risk()
        self.verdict = assign_bifurcation_verdict(agreement, unified, risk)

    def test_verdict_computed(self):
        assert len(self.verdict) > 20

    def test_verdict_not_unified(self):
        assert "unified_equation_exists" not in self.verdict

    def test_verdict_mentions_two_objects(self):
        assert "two" in self.verdict or "distinct" in self.verdict

    def test_verdict_mentions_coincidence(self):
        assert "coincidence" in self.verdict

    def test_verdict_mentions_matter_declaration(self):
        assert "matter" in self.verdict or "declare" in self.verdict


class TestNonclaims:
    def setup_method(self):
        self.r = run_phi_sector_bifurcation()

    def test_nonclaims_nonempty(self):
        assert len(self.r.nonclaims) >= 3

    def test_not_claiming_inconsistency(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "not claiming" in combined and "inconsistent" in combined

    def test_not_claiming_impossible(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "impossible" in combined or "cannot exist" in combined

    def test_psi_proxy_separation_in_nonclaims(self):
        """Nonclaims must clarify that PSI_PROXY is NOT M_drive or Phi_field."""
        combined = " ".join(self.r.nonclaims).lower()
        assert "psi" in combined or "alpha_vac" in combined or "deceleration" in combined


class TestMasterAudit:
    def setup_method(self):
        self.r = run_phi_sector_bifurcation()

    def test_trajectory_regime_name(self):
        assert self.r.trajectory_regime.name == "trajectory"

    def test_field_regime_name(self):
        assert self.r.field_regime.name == "field"

    def test_fixed_point_agreement_values_agree(self):
        assert self.r.fixed_point_agreement.values_agree is True

    def test_fixed_point_is_coincidence(self):
        assert self.r.fixed_point_agreement.is_coincidence is True

    def test_unified_equation_absent(self):
        assert self.r.unified_equation.exists_currently is False

    def test_matter_risk_disagrees_away(self):
        assert self.r.matter_risk.agree_away_from_R_eq is False

    def test_verdict_nonempty(self):
        assert len(self.r.bifurcation_verdict) > 20

    def test_diagnostics_x_eq(self):
        assert abs(self.r.diagnostics["X_EQ"] - 4.5) < 1e-10

    def test_diagnostics_psi_proxy(self):
        assert abs(self.r.diagnostics["PSI_PROXY"] - 1.0 / 3.0) < 1e-10

    def test_diagnostics_unified_absent(self):
        assert self.r.diagnostics["unified_equation_exists"] is False

    def test_diagnostics_agree_away_false(self):
        assert self.r.diagnostics["agree_away_from_R_eq"] is False


class TestCrossConsistency:
    """Structural cross-checks across the two regimes."""

    def test_both_equilibrium_values_equal_x_eq(self):
        traj = build_trajectory_regime()
        fld = build_field_regime()
        assert abs(traj.equilibrium_value - fld.equilibrium_value) < 1e-10
        assert abs(traj.equilibrium_value - X_EQ) < 1e-10

    def test_x_eq_not_alpha_vac(self):
        """X_eq = 4.5 != alpha_vac = 1/3: the field value is NOT the vacuum fraction."""
        assert abs(X_EQ - ALPHA_VAC) > 1.0

    def test_psi_proxy_equals_alpha_vac_not_phi_field(self):
        """The alpha_vac coincidence is through PSI_PROXY, not through Phi_field."""
        assert abs(PSI_PROXY - ALPHA_VAC) < 1e-10
        assert abs(PHI_FIELD_AT_REQ - ALPHA_VAC) > 1.0

    def test_same_ode_form_both_regimes(self):
        """Both ODEs have the form tau_eff * dPhi/dt + Phi = X."""
        traj = build_trajectory_regime()
        fld = build_field_regime()
        # Both ODEs contain tau_eff and X
        assert "tau_eff" in traj.ode and "tau_eff" in fld.ode

    def test_trajectory_is_point_field_is_distributed(self):
        traj = build_trajectory_regime()
        fld = build_field_regime()
        assert "0+1" in traj.domain or "point" in traj.domain.lower()
        assert "1+1" in fld.domain or "distributed" in fld.domain.lower()

    def test_fixed_point_agreement_exact(self):
        traj = build_trajectory_regime()
        fld = build_field_regime()
        agreement = build_fixed_point_agreement(traj, fld)
        assert abs(agreement.trajectory_value - agreement.field_value) < 1e-15

    def test_rho_eq_only_in_field_regime(self):
        """rho_eq = -M^2/(2tau^2 r^4) is a property of the field sector, not trajectory."""
        fld = build_field_regime()
        traj = build_trajectory_regime()
        assert "rho" in fld.energy_density.lower() or "-M^2" in fld.energy_density or "-X^2" in fld.energy_density
        # Trajectory does NOT directly produce rho_eq
        assert "implicit" in traj.energy_density.lower() or "not directly" in traj.energy_density.lower()
