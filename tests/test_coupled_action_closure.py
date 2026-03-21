"""Tests — Phase D8: Coupled Action Closure.

60 tests across 11 classes.
"""

import json
import pytest

from grut.coupled_action_closure import (
    compute_coupled_action,
    coupled_action_result_to_dict,
    define_sector_actions,
    construct_interaction_candidates,
    assemble_action,
    derive_euler_lagrange,
    map_channel_recovery,
    inventory_closure,
    classify_coupled_action,
    CoupledActionParams,
    CoupledActionResult,
    N_SECTORS,
    N_D7_CHANNELS,
    N_INTERACTION_CANDIDATES,
    N_EL_FIELDS,
    RECOVERY_STATUSES,
    CLOSURE_STATUSES,
    CLASSIFICATION_OPTIONS,
    COUPLED_ACTION_ASSUMPTIONS,
    COUPLED_ACTION_NONCLAIMS,
)


@pytest.fixture(scope="module")
def params():
    return CoupledActionParams()


@pytest.fixture(scope="module")
def result(params):
    return compute_coupled_action(params)


# ================================================================
# TestConstants (5 tests)
# ================================================================

class TestConstants:
    def test_n_sectors(self):
        assert N_SECTORS == 4

    def test_n_d7_channels(self):
        assert N_D7_CHANNELS == 2

    def test_n_interaction_candidates(self):
        assert N_INTERACTION_CANDIDATES == 4

    def test_n_el_fields(self):
        assert N_EL_FIELDS == 3

    def test_recovery_statuses(self):
        assert len(RECOVERY_STATUSES) == 4
        assert "action_derived" in RECOVERY_STATUSES
        assert "derived_after_approximation" in RECOVERY_STATUSES


# ================================================================
# TestSectorActions (6 tests)
# ================================================================

class TestSectorActions:
    def test_sector_actions_exist(self, result):
        assert result.sector_actions is not None

    def test_four_sectors(self, result):
        assert len(result.sector_actions) == 4

    def test_gravity_sector(self, result):
        names = [s.name for s in result.sector_actions]
        assert "gravitational" in names

    def test_macro_sector(self, result):
        names = [s.name for s in result.sector_actions]
        assert "macro_scalar_memory" in names

    def test_defect_sector(self, result):
        names = [s.name for s in result.sector_actions]
        assert "defect_triplet" in names

    def test_each_has_lagrangian(self, result):
        for s in result.sector_actions:
            assert s.lagrangian_form != ""


# ================================================================
# TestInteractionCandidates (5 tests)
# ================================================================

class TestInteractionCandidates:
    def test_candidates_exist(self, result):
        assert result.interaction_candidates is not None

    def test_four_candidates(self, result):
        assert len(result.interaction_candidates) == 4

    def test_portal_present(self, result):
        names = [t.name for t in result.interaction_candidates]
        assert "scalar_triplet_portal" in names

    def test_grav_coupling_present(self, result):
        names = [t.name for t in result.interaction_candidates]
        assert "stress_energy_gravitational_coupling" in names

    def test_each_has_target_channel(self, result):
        for t in result.interaction_candidates:
            assert t.target_d7_channel != ""


# ================================================================
# TestActionAssembly (6 tests)
# ================================================================

class TestActionAssembly:
    def test_action_exists(self, result):
        assert result.action_candidate is not None

    def test_four_sectors(self, result):
        assert result.action_candidate.n_sectors == 4

    def test_four_interactions(self, result):
        assert result.action_candidate.n_interaction_terms == 4

    def test_six_free_params(self, result):
        assert result.action_candidate.n_free_parameters == 6

    def test_action_contains_grav(self, result):
        assert "S_grav" in result.action_candidate.full_action_symbolic

    def test_action_contains_portal(self, result):
        assert "S_portal" in result.action_candidate.full_action_symbolic


# ================================================================
# TestEulerLagrange (6 tests)
# ================================================================

class TestEulerLagrange:
    def test_el_exist(self, result):
        assert result.el_derivations is not None

    def test_three_equations(self, result):
        assert len(result.el_derivations) == 3

    def test_metric_el(self, result):
        fields = [el.field_name for el in result.el_derivations]
        assert "metric" in fields

    def test_macro_el(self, result):
        fields = [el.field_name for el in result.el_derivations]
        assert "macro_scalar" in fields

    def test_defect_el(self, result):
        fields = [el.field_name for el in result.el_derivations]
        assert "defect_triplet" in fields

    def test_metric_identifies_backreaction(self, result):
        metric_el = [el for el in result.el_derivations if el.field_name == "metric"][0]
        assert "back_reaction_gravitational_penalty" in metric_el.terms_identified


# ================================================================
# TestChannelRecovery (6 tests)
# ================================================================

class TestChannelRecovery:
    def test_recovery_exists(self, result):
        assert result.channel_recovery is not None

    def test_two_channels(self, result):
        assert result.channel_recovery.n_channels == 2

    def test_one_action_derived(self, result):
        assert result.channel_recovery.n_action_derived == 1

    def test_one_approximate(self, result):
        assert result.channel_recovery.n_derived_after_approximation == 1

    def test_zero_effective(self, result):
        assert result.channel_recovery.n_effective_closure == 0

    def test_recovery_fraction(self, result):
        assert abs(result.channel_recovery.d7_recovery_fraction - 0.75) < 0.01


# ================================================================
# TestClosureInventory (6 tests)
# ================================================================

class TestClosureInventory:
    def test_inventory_exists(self, result):
        assert result.closure_inventory is not None

    def test_ten_items(self, result):
        assert result.closure_inventory.n_total == 10

    def test_four_derived(self, result):
        assert result.closure_inventory.n_action_derived == 4

    def test_three_effective(self, result):
        assert result.closure_inventory.n_effective == 3

    def test_three_open(self, result):
        assert result.closure_inventory.n_open == 3

    def test_all_statuses_valid(self, result):
        for e in result.closure_inventory.entries:
            assert e.status in CLOSURE_STATUSES


# ================================================================
# TestClassification (6 tests)
# ================================================================

class TestClassification:
    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_classification_valid(self, result):
        assert result.classification.classification in CLASSIFICATION_OPTIONS

    def test_phase_lock_has_d8(self, result):
        assert "coupled_action_D8" in result.classification.phase_lock_update

    def test_phase_lock_has_d7(self, result):
        assert "cross_coupling_D7" in result.classification.phase_lock_update

    def test_recovery_fraction_matches(self, result):
        assert abs(result.classification.d7_recovery_fraction - 0.75) < 0.01

    def test_channels_count(self, result):
        cl = result.classification
        assert cl.n_channels_derived + cl.n_channels_approximate + cl.n_channels_effective == 2


# ================================================================
# TestD7Consistency (5 tests)
# ================================================================

class TestD7Consistency:
    def test_grav_penalty_action_derived(self, result):
        entry = [e for e in result.channel_recovery.entries
                 if e.d7_channel_name == "gravitational_penalty"][0]
        assert entry.recovery_status == "action_derived"

    def test_source_amp_after_approximation(self, result):
        entry = [e for e in result.channel_recovery.entries
                 if e.d7_channel_name == "source_amplification"][0]
        assert entry.recovery_status == "derived_after_approximation"

    def test_grav_quality_exact(self, result):
        entry = [e for e in result.channel_recovery.entries
                 if e.d7_channel_name == "gravitational_penalty"][0]
        assert entry.recovery_quality == "exact"

    def test_source_quality_structural(self, result):
        entry = [e for e in result.channel_recovery.entries
                 if e.d7_channel_name == "source_amplification"][0]
        assert entry.recovery_quality == "structural"

    def test_source_has_approximations(self, result):
        entry = [e for e in result.channel_recovery.entries
                 if e.d7_channel_name == "source_amplification"][0]
        assert len(entry.approximations_required) >= 2


# ================================================================
# TestNonclaimsSerialization (4 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = coupled_action_result_to_dict(result)
        s = json.dumps(d)
        assert s is not None

    def test_serialization_has_classification(self, result):
        d = coupled_action_result_to_dict(result)
        assert "classification" in d


# ================================================================
# TestStructuralConsistency (5 tests)
# ================================================================

class TestStructuralConsistency:
    def test_portal_targets_amplification(self, result):
        portal = [t for t in result.interaction_candidates
                  if t.name == "scalar_triplet_portal"][0]
        assert "source_amplification" in portal.target_d7_channel

    def test_grav_targets_penalty(self, result):
        grav = [t for t in result.interaction_candidates
                if t.name == "stress_energy_gravitational_coupling"][0]
        assert "gravitational_penalty" in grav.target_d7_channel

    def test_portal_constructive(self, result):
        portal = [t for t in result.interaction_candidates
                  if t.name == "scalar_triplet_portal"][0]
        assert portal.sign_effect == "constructive"

    def test_grav_destructive(self, result):
        grav = [t for t in result.interaction_candidates
                if t.name == "stress_energy_gravitational_coupling"][0]
        assert grav.sign_effect == "destructive"

    def test_macro_el_has_amplification(self, result):
        macro_el = [el for el in result.el_derivations
                    if el.field_name == "macro_scalar"][0]
        assert "source_amplification_pathway" in macro_el.terms_identified
