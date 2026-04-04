"""Tests for grut/g_minus_closure_audit.py — g_- Closure Status Audit.

Covers:
  TestClosureConditions       — three conditions; condition_2 unknown; all_met=False
  TestStaticSourceVanishes    — rho_eq field1==field2; difference==0; source_vanishes True
  TestGMinusZeroGuarantee     — guaranteed=False; under_projection=True; paths
  TestDynamicSubsumed         — a_crit closes; g_minus subleading; no new static path
  TestPhiMinusConfirmation    — radial_power=4; kinetic_sign=-1; no Component B
  TestVerdictComputed         — verdict from booleans; source_path_closed; homogeneous_open
  TestNonclaims               — universal_no_go=False; homogeneous open stated
  TestForbiddenClaims         — forbidden list populated; no forbidden claim in verdict
  TestMasterAudit             — end-to-end run_g_minus_closure_audit()
  TestCrossConsistency        — rho_eq matches metric_closure_program constants
"""

from __future__ import annotations

import math
import pytest

from grut.g_minus_closure_audit import (
    # Constants
    RHO_EQ_AT_R_EQ,
    VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN,
    VERDICT_FULLY_CLOSED,
    VERDICT_SOURCE_NONZERO,
    FORBIDDEN_CLAIMS,
    # Functions
    build_closure_conditions,
    run_static_source_test as _run_static_source_test,
    assess_dynamic_g_minus,
    assess_phi_minus,
    assign_closure_verdict,
    run_g_minus_closure_audit,
    # Data structures
    ClosureConditions, GMinusStaticSourceTest, GMinusDynamicAssessment,
    ScalarPhiMinusAssessment, GMinusClosureResult,
)
from grut.metric_closure_program import (
    M_EXT, R_EQ, TAU_SQ, A_CRIT,
)


# ================================================================
# TestClosureConditions
# ================================================================

class TestClosureConditions:
    """The three conditions required for source=0 => g_-=0."""

    def setup_method(self):
        self.cond = build_closure_conditions()

    def test_condition_1_is_true(self):
        """Condition 1 (static BCs): satisfied under GRUT equilibrium assumption."""
        assert self.cond.condition_1_static_bc is True

    def test_condition_1_status_satisfied(self):
        """Condition 1 status string is 'satisfied'."""
        assert self.cond.condition_1_status == "satisfied"

    def test_condition_2_is_false(self):
        """Condition 2 (no homogeneous modes): stored as False (unknown)."""
        assert self.cond.condition_2_no_homogeneous is False

    def test_condition_2_status_likely_false(self):
        """Condition 2 status is 'likely_false' — wrong-sign EH expected unstable."""
        assert self.cond.condition_2_status == "likely_false__wrong_sign_EH_expected_unstable"

    def test_condition_2_notes_mention_homogeneous(self):
        """Condition 2 notes document the homogeneous mode concern."""
        assert "homogeneous" in self.cond.condition_2_notes.lower()

    def test_condition_2_notes_mention_wrong_sign(self):
        """Condition 2 notes document wrong-sign EH instability."""
        assert "wrong" in self.cond.condition_2_notes.lower() or "unstable" in self.cond.condition_2_notes.lower()

    def test_condition_3_is_true(self):
        """Condition 3 (Galley projection): assumed True."""
        assert self.cond.condition_3_galley_projection is True

    def test_condition_3_status_assumed(self):
        """Condition 3 status is 'assumed' — projection is not derived."""
        assert self.cond.condition_3_status == "assumed"

    def test_all_conditions_met_is_false(self):
        """all_conditions_met = False because condition 2 is unknown."""
        assert self.cond.all_conditions_met is False

    def test_all_conditions_not_met_follows_from_condition_2(self):
        """all_conditions_met = condition_1 AND condition_2 AND condition_3 = False."""
        assert self.cond.all_conditions_met == (
            self.cond.condition_1_static_bc
            and self.cond.condition_2_no_homogeneous
            and self.cond.condition_3_galley_projection
        )

    def test_conditions_notes_nonempty(self):
        """Conditions notes list is populated."""
        assert len(self.cond.notes) > 0


# ================================================================
# TestStaticSourceVanishes
# ================================================================

class TestStaticSourceVanishes:
    """At static equilibrium, T^Phi_1 = T^Phi_2 => source = 0."""

    def setup_method(self):
        self.cond = build_closure_conditions()
        self.st = _run_static_source_test(self.cond)

    def test_rho_eq_field1_equals_field2(self):
        """Both fields have the same equilibrium energy density."""
        assert self.st.rho_eq_field1 == self.st.rho_eq_field2

    def test_rho_eq_formula(self):
        """rho_eq = -M^2 / (2 tau^2 R_eq^4)."""
        expected = -M_EXT ** 2 / (2.0 * TAU_SQ * R_EQ ** 4)
        assert abs(self.st.rho_eq_field1 - expected) < 1e-15

    def test_rho_eq_is_negative(self):
        """Equilibrium energy density is negative (phantom field)."""
        assert self.st.rho_eq_field1 < 0.0

    def test_source_difference_is_zero(self):
        """Source difference is exactly 0.0 (floating point)."""
        assert self.st.source_difference == 0.0

    def test_source_vanishes(self):
        """source_vanishes = True."""
        assert self.st.source_vanishes is True

    def test_rho_eq_constant_matches(self):
        """Module constant RHO_EQ_AT_R_EQ matches the computed value."""
        assert abs(RHO_EQ_AT_R_EQ - self.st.rho_eq_field1) < 1e-15


# ================================================================
# TestGMinusZeroGuarantee
# ================================================================

class TestGMinusZeroGuarantee:
    """Tests for the conditional g_-=0 implications."""

    def setup_method(self):
        self.cond = build_closure_conditions()
        self.st = _run_static_source_test(self.cond)

    def test_g_minus_zero_not_guaranteed(self):
        """g_- = 0 is NOT guaranteed: condition 2 unknown prevents it."""
        assert self.st.g_minus_zero_guaranteed is False

    def test_g_minus_zero_under_projection_is_true(self):
        """g_- = 0 under Galley projection (conditions 1+3 hold)."""
        assert self.st.g_minus_zero_under_projection is True

    def test_source_driven_component_b_false(self):
        """Source-driven path: Component B from g_- = False (source closed)."""
        assert self.st.source_driven_component_b is False

    def test_homogeneous_component_b_is_undetermined(self):
        """Homogeneous path: Component B status = 'undetermined'."""
        assert self.st.homogeneous_component_b == "undetermined"

    def test_g_minus_guaranteed_follows_all_conditions(self):
        """g_minus_zero_guaranteed == all_conditions_met."""
        assert self.st.g_minus_zero_guaranteed == self.cond.all_conditions_met

    def test_under_projection_requires_conditions_1_and_3(self):
        """g_minus_zero_under_projection requires conditions 1+3 and source_vanishes."""
        expected = (
            self.cond.condition_1_static_bc
            and self.cond.condition_3_galley_projection
            and self.st.source_vanishes
        )
        assert self.st.g_minus_zero_under_projection == expected

    def test_notes_mention_homogeneous_path(self):
        """Notes document the homogeneous path remaining open."""
        combined = " ".join(self.st.notes).lower()
        assert "homogeneous" in combined


# ================================================================
# TestDynamicSubsumed
# ================================================================

class TestDynamicSubsumed:
    """Dynamic g_- does not open a new static closure path."""

    def setup_method(self):
        self.dyn = assess_dynamic_g_minus()

    def test_a_crit_scenario_closes(self):
        """A_crit kinetic scenario closes f=0 dynamically (Appendix J, locked)."""
        assert self.dyn.a_crit_scenario_closes is True

    def test_a_crit_value(self):
        """A_crit value matches locked value from interior_metric_closure.py."""
        assert abs(self.dyn.a_crit_value - A_CRIT) < 1e-10

    def test_g_minus_correction_order(self):
        """g_- correction is first-order in g_-."""
        assert self.dyn.g_minus_correction_order == "first_order_in_g_minus"

    def test_g_minus_subsumed(self):
        """Dynamic closure is already explained without g_-."""
        assert self.dyn.g_minus_subsumed is True

    def test_no_new_static_path(self):
        """Dynamic g_- does not open a new static closure path."""
        assert self.dyn.opens_new_static_path is False

    def test_notes_mention_subleading(self):
        """Notes document that g_- is subleading."""
        combined = " ".join(self.dyn.notes).lower()
        assert "subleading" in combined or "first order" in combined or "first_order" in combined


# ================================================================
# TestPhiMinusConfirmation
# ================================================================

class TestPhiMinusConfirmation:
    """Phi_- scalar sector confirmation (from route_b_component_b.py Result B)."""

    def setup_method(self):
        self.pm = assess_phi_minus()

    def test_kinetic_sign_is_minus_one(self):
        """Phi_- has wrong-sign kinetic energy: kinetic_sign = -1."""
        assert self.pm.kinetic_sign == -1

    def test_radial_power_is_4(self):
        """Phi_- energy density ~ 1/r^4 (Component A profile, not Component B)."""
        assert self.pm.radial_power == 4

    def test_provides_component_b_false(self):
        """Phi_- does NOT provide Component B (wrong profile: 1/r^4 not 1/r^2)."""
        assert self.pm.provides_component_b is False

    def test_energy_density_scaling(self):
        """Energy density scaling is '1_over_r4_ghost'."""
        assert "1_over_r4" in self.pm.energy_density_scaling

    def test_source_reference(self):
        """Source reference points to route_b_component_b.py."""
        assert "route_b_component_b" in self.pm.source_reference

    def test_notes_mention_ghost(self):
        """Notes document the ghost character."""
        combined = " ".join(self.pm.notes).lower()
        assert "ghost" in combined


# ================================================================
# TestVerdictComputed
# ================================================================

class TestVerdictComputed:
    """Verdict assigned from Boolean outcomes, not hardcoded."""

    def setup_method(self):
        self.cond = build_closure_conditions()
        self.st = _run_static_source_test(self.cond)
        self.verdict, self.source_closed, self.homogeneous_open = assign_closure_verdict(
            self.st, self.cond
        )

    def test_source_path_closed_is_true(self):
        """Source-driven path is closed."""
        assert self.source_closed is True

    def test_homogeneous_path_open_is_true(self):
        """Homogeneous path is open (condition 2 unknown)."""
        assert self.homogeneous_open is True

    def test_verdict_is_source_closed_homogeneous_open(self):
        """Verdict = SOURCE_CLOSED_HOMOGENEOUS_OPEN (not fully closed, not nonzero)."""
        assert self.verdict == VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN

    def test_verdict_not_fully_closed(self):
        """Verdict is not FULLY_CLOSED (would require condition 2 established)."""
        assert self.verdict != VERDICT_FULLY_CLOSED

    def test_verdict_not_source_nonzero(self):
        """Verdict is not SOURCE_NONZERO (source does vanish)."""
        assert self.verdict != VERDICT_SOURCE_NONZERO

    def test_verdict_contains_implausible_not_impossible(self):
        """Verdict string encodes conditional closure (implausible, not impossible)."""
        assert "implausible" in self.verdict
        assert "impossible" in self.verdict

    def test_verdict_contains_homogeneous(self):
        """Verdict string references homogeneous modes."""
        assert "homogeneous" in self.verdict

    def test_verdict_consistent_with_booleans(self):
        """Verdict string is consistent with source_closed and homogeneous_open."""
        if self.source_closed and not self.homogeneous_open:
            assert self.verdict == VERDICT_FULLY_CLOSED
        elif self.source_closed and self.homogeneous_open:
            assert self.verdict == VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN
        else:
            assert self.verdict == VERDICT_SOURCE_NONZERO


# ================================================================
# TestNonclaims
# ================================================================

class TestNonclaims:
    """The module must explicitly document what it does NOT claim."""

    def setup_method(self):
        self.result = run_g_minus_closure_audit()

    def test_universal_no_go_is_false(self):
        """universal_no_go = False: this is NOT a universal no-go theorem."""
        assert self.result.universal_no_go is False

    def test_universal_no_go_in_diagnostics(self):
        """Diagnostics confirm universal_no_go = False."""
        assert self.result.diagnostics["universal_no_go"] is False

    def test_homogeneous_path_open_in_result(self):
        """Result states the homogeneous path is open."""
        assert self.result.homogeneous_path_open is True

    def test_nonclaims_list_nonempty(self):
        """Nonclaims list is populated."""
        assert len(self.result.nonclaims) > 0

    def test_nonclaims_mention_not_computed(self):
        """Nonclaims state that g_- energy density is not computed here."""
        combined = " ".join(self.result.nonclaims).lower()
        assert "not compute" in combined or "does not compute" in combined

    def test_nonclaims_mention_homogeneous(self):
        """Nonclaims acknowledge homogeneous path not ruled out."""
        combined = " ".join(self.result.nonclaims).lower()
        assert "homogeneous" in combined

    def test_nonclaims_mention_non_galley(self):
        """Nonclaims acknowledge non-Galley formalisms not covered."""
        combined = " ".join(self.result.nonclaims).lower()
        assert "galley" in combined or "ctp" in combined


# ================================================================
# TestForbiddenClaims
# ================================================================

class TestForbiddenClaims:
    """Forbidden claims are listed and not present in the verdict."""

    def test_forbidden_list_nonempty(self):
        """FORBIDDEN_CLAIMS list is populated."""
        assert len(FORBIDDEN_CLAIMS) > 0

    def test_universal_no_go_is_forbidden(self):
        """Asserting a universal no-go for g_- is a forbidden claim."""
        assert "universal_no_go_for_g_minus" in FORBIDDEN_CLAIMS

    def test_g_minus_computed_is_forbidden(self):
        """Claiming g_- energy density is computed is forbidden."""
        assert "g_minus_energy_density_computed" in FORBIDDEN_CLAIMS

    def test_component_b_impossible_is_forbidden(self):
        """Claiming Component B is impossible from g_- is forbidden."""
        assert "component_b_impossible_from_g_minus" in FORBIDDEN_CLAIMS

    def test_search_exhaustively_closed_is_forbidden(self):
        """Claiming the search is exhaustively closed is forbidden."""
        assert "search_exhaustively_closed" in FORBIDDEN_CLAIMS

    def test_result_includes_forbidden_list(self):
        """run_g_minus_closure_audit() result includes the forbidden claims list."""
        result = run_g_minus_closure_audit()
        for claim in FORBIDDEN_CLAIMS:
            assert claim in result.forbidden_claims

    def test_verdict_does_not_contain_forbidden_keywords(self):
        """Verdict string does not contain forbidden claim keywords."""
        result = run_g_minus_closure_audit()
        for fc in FORBIDDEN_CLAIMS:
            assert fc not in result.verdict, f"Forbidden claim '{fc}' in verdict"


# ================================================================
# TestMasterAudit
# ================================================================

class TestMasterAudit:
    """End-to-end tests for run_g_minus_closure_audit()."""

    def setup_method(self):
        self.result = run_g_minus_closure_audit()

    def test_result_is_valid(self):
        assert self.result.valid is True

    def test_conditions_present(self):
        assert self.result.conditions is not None

    def test_static_test_present(self):
        assert self.result.static_test is not None

    def test_dynamic_present(self):
        assert self.result.dynamic_assessment is not None

    def test_phi_minus_present(self):
        assert self.result.phi_minus_assessment is not None

    def test_verdict_nonempty(self):
        assert len(self.result.verdict) > 0

    def test_verdict_is_correct(self):
        """Master verdict = SOURCE_CLOSED_HOMOGENEOUS_OPEN."""
        assert self.result.verdict == VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN

    def test_source_path_closed(self):
        assert self.result.source_path_closed is True

    def test_homogeneous_path_open(self):
        assert self.result.homogeneous_path_open is True

    def test_universal_no_go_false(self):
        assert self.result.universal_no_go is False

    def test_diagnostics_populated(self):
        diag = self.result.diagnostics
        for key in [
            "rho_eq_at_R_eq", "source_difference", "condition_1_static_bc",
            "condition_2_status", "condition_3_galley_projection",
            "all_conditions_met", "source_vanishes", "g_minus_zero_guaranteed",
            "g_minus_zero_under_projection", "source_path_closed",
            "homogeneous_path_open", "universal_no_go",
        ]:
            assert key in diag, f"Missing diagnostic key: {key}"

    def test_diagnostics_condition_2_likely_false(self):
        assert self.result.diagnostics["condition_2_status"] == "likely_false__wrong_sign_EH_expected_unstable"

    def test_diagnostics_source_vanishes(self):
        assert self.result.diagnostics["source_vanishes"] is True

    def test_diagnostics_g_minus_not_guaranteed(self):
        assert self.result.diagnostics["g_minus_zero_guaranteed"] is False

    def test_diagnostics_under_projection_true(self):
        assert self.result.diagnostics["g_minus_zero_under_projection"] is True

    def test_nonclaims_present(self):
        assert len(self.result.nonclaims) > 0

    def test_forbidden_claims_present(self):
        assert len(self.result.forbidden_claims) > 0


# ================================================================
# TestCrossConsistency
# ================================================================

class TestCrossConsistency:
    """Cross-consistency with upstream locked values."""

    def test_rho_eq_constant_formula(self):
        """RHO_EQ_AT_R_EQ = -M^2/(2*tau^2*R_eq^4)."""
        expected = -M_EXT ** 2 / (2.0 * TAU_SQ * R_EQ ** 4)
        assert abs(RHO_EQ_AT_R_EQ - expected) < 1e-15

    def test_rho_eq_matches_metric_closure_constants(self):
        """rho_eq uses the same M_EXT, TAU_SQ, R_EQ as metric_closure_program.py."""
        computed = -M_EXT ** 2 / (2.0 * TAU_SQ * R_EQ ** 4)
        assert abs(RHO_EQ_AT_R_EQ - computed) < 1e-15

    def test_a_crit_in_dynamic_matches_locked(self):
        """Dynamic assessment A_crit matches locked value from Appendix J."""
        dyn = assess_dynamic_g_minus()
        assert abs(dyn.a_crit_value - A_CRIT) < 1e-10

    def test_phi_minus_radial_power_consistent_with_catalog(self):
        """Phi_- radial power = 4, consistent with metric_closure_program kinetic_A1."""
        pm = assess_phi_minus()
        assert pm.radial_power == 4  # same as kinetic_A1 in catalog

    def test_source_path_closure_stronger_than_unresolved(self):
        """This audit upgrades from 'unresolved' to 'source_path_closed'."""
        result = run_g_minus_closure_audit()
        # Previous status was "unresolved" — now source path is closed
        assert result.source_path_closed is True
        # But not fully closed — homogeneous path remains
        assert result.homogeneous_path_open is True

    def test_verdict_encodes_partial_closure(self):
        """Verdict is stronger than 'unresolved' but weaker than 'fully_closed'."""
        result = run_g_minus_closure_audit()
        assert result.verdict != "unresolved"
        assert result.verdict != VERDICT_FULLY_CLOSED
        assert result.verdict == VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN

    def test_condition_2_explains_why_not_fully_closed(self):
        """The reason the audit is not fully closed is condition 2 being likely_false."""
        cond = build_closure_conditions()
        # If condition 2 were True, all conditions would be met
        # and the source path would fully close
        assert cond.condition_2_no_homogeneous is False
        assert cond.condition_2_status == "likely_false__wrong_sign_EH_expected_unstable"
        assert cond.all_conditions_met is False
