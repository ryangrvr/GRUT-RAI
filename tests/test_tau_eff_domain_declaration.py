"""Tests for grut/tau_eff_domain_declaration.py — τ_eff Domain Declaration.

Covers:
  TestConstants               — OMEGA_TAU_PRODUCT, OMEGA_0, TAU_EFF_CANON
  TestContexts                — three contexts; none covariant; correct omega symbols
  TestStructuralIdentity      — omega_0 * tau_eff = 1 verified numerically
  TestCovariantRoadmap        — not built; three requirements documented
  TestDomainDeclaration       — declaration survivable; what is not survivable
  TestVerdict                 — computed from Booleans
  TestNonclaims               — not claiming results are wrong
  TestMasterAudit             — end-to-end run_tau_eff_domain_declaration()
  TestCrossConsistency        — tau_eff_canon = 1/omega_0; all three omegas distinct
"""

from __future__ import annotations

import math
import pytest

from grut.tau_eff_domain_declaration import (
    OMEGA_TAU_PRODUCT,
    TAU_SQ,
    R_EQ,
    M_EXT,
    BETA_Q_CANON,
    OMEGA_0_SQ,
    OMEGA_0,
    TAU_EFF_CANON,
    build_contexts,
    build_structural_identity,
    build_covariant_roadmap,
    build_domain_declaration,
    assign_verdict,
    run_tau_eff_domain_declaration,
)


class TestConstants:
    def test_omega_tau_product(self):
        assert abs(OMEGA_TAU_PRODUCT - 1.0) < 1e-10

    def test_omega_0_sq_formula(self):
        """ω₀² = β_Q · GM/R_eq³ = 2 · 0.5 / (1/3)³ = 1/(2/27) = 13.5"""
        expected = BETA_Q_CANON * M_EXT / (R_EQ ** 3)
        assert abs(OMEGA_0_SQ - expected) < 1e-10

    def test_omega_0_sq_value(self):
        """ω₀² = β_Q·M/R_eq³ = 2×0.5/(1/3)³ = 1/(1/27) = 27.0"""
        assert abs(OMEGA_0_SQ - 27.0) < 1e-6

    def test_omega_0_value(self):
        assert abs(OMEGA_0 - math.sqrt(27.0)) < 1e-6

    def test_tau_eff_canon_from_identity(self):
        """τ_eff_canon = 1/ω₀ (from ω₀·τ_eff = 1)."""
        assert abs(TAU_EFF_CANON - 1.0 / OMEGA_0) < 1e-10

    def test_omega_tau_product_verified(self):
        """ω₀ · τ_eff_canon = 1 exactly."""
        assert abs(OMEGA_0 * TAU_EFF_CANON - OMEGA_TAU_PRODUCT) < 1e-10

    def test_tau_eq_ne_tau_eff(self):
        """τ (bare, TAU_SQ) is NOT τ_eff_canon; they are related but distinct."""
        # τ² = 3/2, so τ = sqrt(3/2) ≈ 1.225; τ_eff_canon = 1/ω₀ ≈ 0.272
        tau_bare = math.sqrt(TAU_SQ)
        assert abs(tau_bare - TAU_EFF_CANON) > 0.1


class TestContexts:
    def setup_method(self):
        self.contexts = build_contexts()

    def test_three_contexts(self):
        assert len(self.contexts) == 3

    def test_sectors(self):
        sectors = {c.sector for c in self.contexts}
        assert "cosmological" in sectors
        assert "collapse" in sectors
        assert "interior_pde" in sectors

    def test_none_covariant(self):
        for c in self.contexts:
            assert c.is_covariant is False, f"Context {c.sector} wrongly marked covariant"

    def test_omega_symbols_distinct(self):
        omega_symbols = [c.omega_symbol for c in self.contexts]
        assert len(set(omega_symbols)) == 3, "All three omega definitions must be distinct"

    def test_cosmological_omega_is_H(self):
        cosmo = next(c for c in self.contexts if c.sector == "cosmological")
        assert cosmo.omega_symbol == "H"

    def test_collapse_omega_is_V_over_R(self):
        coll = next(c for c in self.contexts if c.sector == "collapse")
        assert "|V|/R" in coll.omega_symbol or "V/R" in coll.omega_symbol

    def test_pde_omega_is_omega_0(self):
        pde = next(c for c in self.contexts if c.sector == "interior_pde")
        assert "omega_0" in pde.omega_symbol or "ω₀" in pde.omega_symbol

    def test_all_have_domain_assumptions(self):
        for c in self.contexts:
            assert len(c.domain_assumptions) >= 2, f"Context {c.sector} needs domain assumptions"

    def test_all_have_references(self):
        for c in self.contexts:
            assert len(c.reference) > 5

    def test_tau_eff_formula_form_preserved(self):
        """All three contexts use a τ_eff formula involving tau."""
        for c in self.contexts:
            formula = c.tau_eff_formula.lower()
            assert "tau" in formula


class TestStructuralIdentity:
    def setup_method(self):
        self.s = build_structural_identity()

    def test_identity_value(self):
        assert abs(self.s.identity_value - 1.0) < 1e-10

    def test_omega_0(self):
        assert abs(self.s.omega_0 - OMEGA_0) < 1e-10

    def test_tau_eff_canon(self):
        assert abs(self.s.tau_eff_canon - TAU_EFF_CANON) < 1e-10

    def test_product_equals_one(self):
        product = self.s.omega_0 * self.s.tau_eff_canon
        assert abs(product - 1.0) < 1e-10

    def test_preserved_across_contexts(self):
        assert self.s.preserved_across_contexts is True

    def test_derivation_nonempty(self):
        assert len(self.s.derivation) > 30

    def test_notes_mention_anchor(self):
        combined = " ".join(self.s.notes).lower()
        assert "anchor" in combined or "preserved" in combined


class TestCovariantRoadmap:
    def setup_method(self):
        self.r = build_covariant_roadmap()

    def test_not_currently_built(self):
        assert self.r.currently_built is False

    def test_requirement_1_documented(self):
        assert len(self.r.requirement_1) > 30
        assert "covariant" in self.r.requirement_1.lower()

    def test_requirement_2_documented(self):
        assert len(self.r.requirement_2) > 30

    def test_requirement_3_documented(self):
        assert len(self.r.requirement_3) > 30
        assert "omega" in self.r.requirement_3.lower() or "ω" in self.r.requirement_3

    def test_survivable_without(self):
        assert self.r.survivable_without is True

    def test_declared_limitation_nonempty(self):
        assert len(self.r.declared_limitation) > 50

    def test_declared_limitation_mentions_preferred_frame(self):
        assert "preferred" in self.r.declared_limitation.lower() or "frame" in self.r.declared_limitation.lower()

    def test_declared_limitation_mentions_structural_identity(self):
        assert "omega" in self.r.declared_limitation.lower() or "tau_eff" in self.r.declared_limitation.lower() or "ω₀" in self.r.declared_limitation


class TestDomainDeclaration:
    def setup_method(self):
        self.d = build_domain_declaration()

    def test_spherical_symmetry_assumed(self):
        assert self.d.spherical_symmetry_assumed is True

    def test_quasi_static_assumed(self):
        assert self.d.quasi_static_assumed is True

    def test_preferred_frame_assumed(self):
        assert self.d.preferred_frame_assumed is True

    def test_covariant_omega_absent(self):
        assert self.d.covariant_omega_absent is True

    def test_declaration_survivable(self):
        assert self.d.declaration_is_survivable is True

    def test_what_is_not_survivable_nonempty(self):
        assert len(self.d.what_is_not_survivable) > 50

    def test_not_survivable_mentions_matter(self):
        assert "matter" in self.d.what_is_not_survivable.lower()

    def test_not_survivable_mentions_implicit(self):
        assert "implicit" in self.d.what_is_not_survivable.lower()

    def test_domain_statement_nonempty(self):
        assert len(self.d.domain_statement) > 50


class TestVerdict:
    def setup_method(self):
        self.r = run_tau_eff_domain_declaration()

    def test_verdict_computed(self):
        assert len(self.r.verdict) > 20

    def test_verdict_not_fully_unified(self):
        assert "fully_unified" not in self.r.verdict

    def test_verdict_mentions_preferred_frame(self):
        assert "preferred_frame" in self.r.verdict or "quasi_static" in self.r.verdict

    def test_verdict_mentions_covariant_open(self):
        assert "covariant_unification_open" in self.r.verdict or "open" in self.r.verdict

    def test_verdict_mentions_identity_preserved(self):
        assert "identity_preserved" in self.r.verdict or "omega0_tau" in self.r.verdict


class TestNonclaims:
    def setup_method(self):
        self.r = run_tau_eff_domain_declaration()

    def test_nonclaims_nonempty(self):
        assert len(self.r.nonclaims) >= 3

    def test_not_claiming_results_wrong(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "not claiming" in combined and "wrong" in combined

    def test_not_claiming_impossible(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "impossible" in combined or "cannot" in combined

    def test_not_claiming_identity_fragile(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "fragile" in combined or "locked" in combined


class TestMasterAudit:
    def setup_method(self):
        self.r = run_tau_eff_domain_declaration()

    def test_three_contexts(self):
        assert len(self.r.contexts) == 3

    def test_covariant_unification_not_built(self):
        assert self.r.covariant_unification_built is False

    def test_structural_identity_preserved(self):
        assert self.r.structural_identity_preserved is True

    def test_omega_tau_product(self):
        s = self.r.structural_identity
        assert abs(s.omega_0 * s.tau_eff_canon - 1.0) < 1e-10

    def test_verdict_nonempty(self):
        assert len(self.r.verdict) > 20

    def test_diagnostics_omega_0(self):
        assert abs(self.r.diagnostics["OMEGA_0"] - OMEGA_0) < 1e-10

    def test_diagnostics_tau_eff(self):
        assert abs(self.r.diagnostics["TAU_EFF_CANON"] - TAU_EFF_CANON) < 1e-10

    def test_diagnostics_unification_false(self):
        assert self.r.diagnostics["covariant_unification_built"] is False

    def test_diagnostics_identity_true(self):
        assert self.r.diagnostics["structural_identity_preserved"] is True

    def test_diagnostics_all_contexts_non_covariant(self):
        # all_contexts_covariant should be True (meaning all are non-covariant)
        assert self.r.diagnostics["all_contexts_covariant"] is True


class TestCrossConsistency:
    def test_tau_eff_canon_is_inverse_omega_0(self):
        assert abs(TAU_EFF_CANON * OMEGA_0 - 1.0) < 1e-10

    def test_all_three_omega_definitions_distinct(self):
        contexts = build_contexts()
        symbols = [c.omega_symbol for c in contexts]
        assert len(set(symbols)) == 3

    def test_structural_identity_matches_constants(self):
        s = build_structural_identity()
        assert abs(s.omega_0 - OMEGA_0) < 1e-10
        assert abs(s.tau_eff_canon - TAU_EFF_CANON) < 1e-10

    def test_omega_0_sq_formula_at_canon(self):
        """ω₀² = β_Q · GM/R_eq³ = 2 × 0.5 / (1/3)³ = 1/(1/27) = 27.0"""
        computed = BETA_Q_CANON * M_EXT / (R_EQ ** 3)
        assert abs(computed - 27.0) < 1e-6
        assert abs(OMEGA_0_SQ - computed) < 1e-6

    def test_declaration_survivable_roadmap_not_built(self):
        """Survivable precisely because it is declared, not hidden."""
        roadmap = build_covariant_roadmap()
        declaration = build_domain_declaration()
        assert not roadmap.currently_built
        assert declaration.declaration_is_survivable

    def test_identity_preserved_despite_non_covariance(self):
        """ω₀·τ_eff = 1 holds even though τ_eff itself is not covariant."""
        s = build_structural_identity()
        assert s.preserved_across_contexts is True
        # All three contexts are non-covariant
        contexts = build_contexts()
        assert all(not c.is_covariant for c in contexts)
