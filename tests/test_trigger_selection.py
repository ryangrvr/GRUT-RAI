"""
Phase D10 — Trigger Selection Closure: Tests (60 tests).

Validates trigger candidate definitions, regime tests, action compatibility,
self-consistency compatibility, scoring, ranking, classification,
nonclaims, serialization, and physics consistency.
"""

import json
import math

import pytest

from grut.trigger_selection import (
    # Constants
    N_TRIGGER_CANDIDATES,
    SCORE_CRITERIA,
    CONTRAST_THRESHOLD,
    TRIGGER_CLASSIFICATION_OPTIONS,
    TRIGGER_SELECTION_ASSUMPTIONS,
    TRIGGER_SELECTION_NONCLAIMS,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    R_EXT,
    KRETSCHNER_COEFF,
    COMPATIBILITY_LEVELS,
    ITERATION_EFFECTS,
    SCORE_CRITERION_NAMES,
    # Dataclasses
    TriggerSelectionParams,
    TriggerSelectionResult,
    # Functions
    define_trigger_candidates,
    test_regime_correctness as _test_regime_correctness,
    assess_action_compatibility,
    assess_self_consistency_compatibility,
    assemble_trigger_assessments,
    rank_triggers,
    classify_trigger_selection,
    compute_trigger_selection,
    trigger_selection_result_to_dict,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return TriggerSelectionParams()


@pytest.fixture(scope="module")
def result(params):
    return compute_trigger_selection(params)


@pytest.fixture(scope="module")
def candidates(result):
    return result.candidates


@pytest.fixture(scope="module")
def regime_tests(result):
    return {r.candidate_name: r for r in result.regime_tests}


@pytest.fixture(scope="module")
def action_compat(result):
    return {a.candidate_name: a for a in result.action_compatibility}


@pytest.fixture(scope="module")
def sc_compat(result):
    return {s.candidate_name: s for s in result.sc_compatibility}


@pytest.fixture(scope="module")
def assessments(result):
    return {a.candidate.name: a for a in result.assessments}


# ================================================================
# 1. TestConstants (5 tests)
# ================================================================

class TestConstants:
    def test_n_trigger_candidates(self):
        assert N_TRIGGER_CANDIDATES == 4

    def test_score_criteria(self):
        assert SCORE_CRITERIA == 5

    def test_contrast_threshold(self):
        assert CONTRAST_THRESHOLD == 100.0

    def test_classification_options_count(self):
        assert len(TRIGGER_CLASSIFICATION_OPTIONS) == 5

    def test_score_criterion_names_count(self):
        assert len(SCORE_CRITERION_NAMES) == 5


# ================================================================
# 2. TestTriggerCandidates (5 tests)
# ================================================================

class TestTriggerCandidates:
    def test_candidate_count(self, candidates):
        assert len(candidates) == N_TRIGGER_CANDIDATES

    def test_ricci_scalar_not_vacuum(self, candidates):
        c = next(c for c in candidates if c.name == "ricci_scalar")
        assert c.nonzero_in_vacuum is False

    def test_kretschmann_vacuum(self, candidates):
        c = next(c for c in candidates if c.name == "kretschmann_sqrt")
        assert c.nonzero_in_vacuum is True

    def test_weyl_vacuum(self, candidates):
        c = next(c for c in candidates if c.name == "weyl_sqrt")
        assert c.nonzero_in_vacuum is True

    def test_invariant_types(self, candidates):
        types = {c.invariant_type for c in candidates}
        assert types == {"ricci_family", "tidal_family"}


# ================================================================
# 3. TestVacuumStrongField (6 tests)
# ================================================================

class TestVacuumStrongField:
    def test_ricci_scalar_zero(self, regime_tests):
        assert regime_tests["ricci_scalar"].value_at_Req == 0.0

    def test_kretschmann_nonzero(self, regime_tests):
        assert regime_tests["kretschmann_sqrt"].value_at_Req > 0

    def test_kretschmann_value(self, regime_tests):
        expected = math.sqrt(48.0) * M_EXT / (R_EQ**3)
        assert abs(regime_tests["kretschmann_sqrt"].value_at_Req - expected) < 1e-6

    def test_weyl_equals_kretschmann(self, regime_tests):
        assert abs(
            regime_tests["weyl_sqrt"].value_at_Req
            - regime_tests["kretschmann_sqrt"].value_at_Req
        ) < 1e-10

    def test_ricci_squared_zero(self, regime_tests):
        assert regime_tests["ricci_squared_sqrt"].value_at_Req == 0.0

    def test_vacuum_active_count(self, regime_tests):
        active = sum(1 for r in regime_tests.values() if r.vacuum_active)
        assert active == 2  # kretschmann + weyl


# ================================================================
# 4. TestWeakFieldSuppression (6 tests)
# ================================================================

class TestWeakFieldSuppression:
    def test_kretschmann_suppressed(self, regime_tests):
        assert regime_tests["kretschmann_sqrt"].weak_field_suppressed is True

    def test_weyl_suppressed(self, regime_tests):
        assert regime_tests["weyl_sqrt"].weak_field_suppressed is True

    def test_kretschmann_regime_correct(self, regime_tests):
        assert regime_tests["kretschmann_sqrt"].regime_correct is True

    def test_weyl_regime_correct(self, regime_tests):
        assert regime_tests["weyl_sqrt"].regime_correct is True

    def test_ricci_regime_incorrect(self, regime_tests):
        assert regime_tests["ricci_scalar"].regime_correct is False

    def test_contrast_ratio_value(self, regime_tests):
        # (R_ext/R_eq)^3 = (2.0 / (1/3))^3 = 6^3 = 216
        assert abs(regime_tests["kretschmann_sqrt"].contrast_ratio - 216.0) < 1e-6


# ================================================================
# 5. TestActionCompatibility (6 tests)
# ================================================================

class TestActionCompatibility:
    def test_kretschmann_natural(self, action_compat):
        assert action_compat["kretschmann_sqrt"].compatibility_level == "naturally_compatible"

    def test_weyl_natural(self, action_compat):
        assert action_compat["weyl_sqrt"].compatibility_level == "naturally_compatible"

    def test_ricci_scalar_natural(self, action_compat):
        # Conformal coupling is natural even though R=0 in vacuum
        assert action_compat["ricci_scalar"].compatibility_level == "naturally_compatible"

    def test_ricci_squared_assumptions(self, action_compat):
        assert action_compat["ricci_squared_sqrt"].compatibility_level == "compatible_with_assumptions"

    def test_ricci_squared_not_natural(self, action_compat):
        assert action_compat["ricci_squared_sqrt"].natural_in_action is False

    def test_all_have_coupling_form(self, action_compat):
        assert all(a.coupling_form for a in action_compat.values())


# ================================================================
# 6. TestSCCompatibility (5 tests)
# ================================================================

class TestSCCompatibility:
    def test_kretschmann_stabilizing(self, sc_compat):
        assert sc_compat["kretschmann_sqrt"].effect_on_iteration == "stabilizing"

    def test_weyl_stabilizing(self, sc_compat):
        assert sc_compat["weyl_sqrt"].effect_on_iteration == "stabilizing"

    def test_ricci_neutral(self, sc_compat):
        assert sc_compat["ricci_scalar"].effect_on_iteration == "neutral"

    def test_all_d9_compatible(self, sc_compat):
        assert all(s.d9_compatible for s in sc_compat.values())

    def test_all_have_assessment(self, sc_compat):
        assert all(s.compatibility_assessment for s in sc_compat.values())


# ================================================================
# 7. TestAssessments (6 tests)
# ================================================================

class TestAssessments:
    def test_assessment_count(self, result):
        assert len(result.assessments) == N_TRIGGER_CANDIDATES

    def test_kretschmann_score_5(self, assessments):
        assert assessments["kretschmann_sqrt"].total_score == 5

    def test_weyl_score_5(self, assessments):
        assert assessments["weyl_sqrt"].total_score == 5

    def test_ricci_scalar_score_2(self, assessments):
        assert assessments["ricci_scalar"].total_score == 2

    def test_ricci_squared_score_1(self, assessments):
        assert assessments["ricci_squared_sqrt"].total_score == 1

    def test_breakdown_has_all_criteria(self, assessments):
        for a in assessments.values():
            assert set(a.score_breakdown.keys()) == set(SCORE_CRITERION_NAMES)


# ================================================================
# 8. TestRanking (6 tests)
# ================================================================

class TestRanking:
    def test_top_score(self, result):
        assert result.ranking.top_score == 5

    def test_family_size(self, result):
        assert len(result.ranking.family_members) == 2

    def test_kretschmann_in_family(self, result):
        assert "kretschmann_sqrt" in result.ranking.family_members

    def test_weyl_in_family(self, result):
        assert "weyl_sqrt" in result.ranking.family_members

    def test_degeneracy_note_mentions_distinct(self, result):
        assert "distinct" in result.ranking.vacuum_degeneracy_note.lower()

    def test_separation(self, result):
        assert result.ranking.separation == 4  # 5 - 1


# ================================================================
# 9. TestClassification (6 tests)
# ================================================================

class TestClassification:
    def test_classification_value(self, result):
        assert result.classification.classification == (
            "kretschmann_family_trigger_best_supported_within_tested_framework"
        )

    def test_classification_in_options(self, result):
        assert result.classification.classification in TRIGGER_CLASSIFICATION_OPTIONS

    def test_phase_status(self, result):
        assert result.classification.phase_status == "ASSESSED"

    def test_trigger_family_count(self, result):
        assert len(result.classification.trigger_family) == 2

    def test_proxy_caveat_conditional(self, result):
        assert result.classification.proxy_caveat.trigger_closure_conditional is True

    def test_phase_lock_update(self, result):
        assert "D10" in result.classification.phase_lock_update


# ================================================================
# 10. TestNonclaimsSerialization (4 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_nonclaims_count(self, result):
        assert len(result.nonclaims) == 10

    def test_assumptions_count(self, result):
        assert len(result.assumptions) == 10

    def test_serializable_to_dict(self, result):
        d = trigger_selection_result_to_dict(result)
        assert isinstance(d, dict)

    def test_json_serializable(self, result):
        d = trigger_selection_result_to_dict(result)
        json_str = json.dumps(d)
        assert len(json_str) > 0


# ================================================================
# 11. TestPhysicsConsistency (5 tests)
# ================================================================

class TestPhysicsConsistency:
    def test_kretschmann_weyl_vacuum_equal(self, regime_tests):
        """Kretschmann and Weyl must give identical values in vacuum."""
        assert abs(
            regime_tests["kretschmann_sqrt"].value_at_Req
            - regime_tests["weyl_sqrt"].value_at_Req
        ) < 1e-10

    def test_ricci_family_all_fail_vacuum(self, result):
        """All Ricci-family candidates must fail vacuum strong-field test."""
        ricci = [a for a in result.assessments
                 if a.candidate.invariant_type == "ricci_family"]
        assert all(not a.regime_test.vacuum_active for a in ricci)

    def test_tidal_family_all_pass_vacuum(self, result):
        """All tidal-family candidates must pass vacuum strong-field test."""
        tidal = [a for a in result.assessments
                 if a.candidate.invariant_type == "tidal_family"]
        assert all(a.regime_test.vacuum_active for a in tidal)

    def test_d4_score_ordering(self, assessments):
        """D4 score ordering: K > R_ab^2 > R."""
        k = assessments["kretschmann_sqrt"].candidate.d4_score
        r2 = assessments["ricci_squared_sqrt"].candidate.d4_score
        r = assessments["ricci_scalar"].candidate.d4_score
        assert k > r2 > r

    def test_sourced_interior_active_for_ricci(self, regime_tests):
        """Ricci candidates should be active in sourced regions."""
        assert regime_tests["ricci_scalar"].sourced_interior_active is True
        assert regime_tests["ricci_squared_sqrt"].sourced_interior_active is True
