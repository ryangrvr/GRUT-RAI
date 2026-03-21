"""Tests — Phase D3: Scalar/Triplet Unification.

57 tests across 10 classes.
"""

import math
import json
import pytest

from grut.scalar_triplet_unification import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, LAMBDA_DEFAULT,
    N_RELATION_TYPES, N_TRIGGER_TYPES, N_MINIMAL_COUPLINGS,
    # Assumptions / nonclaims
    UNIFICATION_ASSUMPTIONS, UNIFICATION_NONCLAIMS,
    # Dataclasses
    ScalarTripletParams,
    # Functions
    define_relation_types,
    assess_relation_types,
    build_relation_taxonomy,
    define_trigger_types,
    assess_trigger_types,
    build_trigger_taxonomy,
    check_canon_preservation,
    define_minimal_couplings,
    rank_candidates,
    classify_unification,
    compute_scalar_triplet_unification,
    scalar_triplet_unification_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return ScalarTripletParams()


@pytest.fixture(scope="module")
def result():
    return compute_scalar_triplet_unification()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_n_relation_types(self):
        assert N_RELATION_TYPES == 4

    def test_n_trigger_types(self):
        assert N_TRIGGER_TYPES == 5

    def test_n_minimal_couplings(self):
        assert N_MINIMAL_COUPLINGS == 5

    def test_eta_target(self):
        assert abs(ETA_TARGET - 1.0 / math.sqrt(8.0 * math.pi)) < 1e-10

    def test_comp_b_coeff(self):
        assert abs(COMP_B_COEFF - 1.0 / (8.0 * math.pi)) < 1e-10


# ================================================================
# Section 2: Relation-Type Taxonomy (6 tests)
# ================================================================

class TestRelationTypeTaxonomy:
    def test_taxonomy_exists(self, result):
        assert result.relation_taxonomy is not None

    def test_four_types(self, result):
        assert result.relation_taxonomy.n_types == 4

    def test_embedding_present(self, result):
        names = [s.short_name for s in result.relation_taxonomy.specs]
        assert "embedding" in names

    def test_companion_present(self, result):
        names = [s.short_name for s in result.relation_taxonomy.specs]
        assert "companion" in names

    def test_emergent_present(self, result):
        names = [s.short_name for s in result.relation_taxonomy.specs]
        assert "emergent" in names

    def test_replacement_present(self, result):
        names = [s.short_name for s in result.relation_taxonomy.specs]
        assert "replacement" in names


# ================================================================
# Section 3: Relation-Type Assessments (6 tests)
# ================================================================

class TestRelationTypeAssessments:
    def test_scores_in_range(self, result):
        for a in result.relation_taxonomy.assessments:
            assert 0 <= a.overall_score <= 1

    def test_embedding_above_replacement(self, result):
        emb = [a for a in result.relation_taxonomy.assessments if a.type_id == 1][0]
        repl = [a for a in result.relation_taxonomy.assessments if a.type_id == 4][0]
        assert emb.overall_score > repl.overall_score

    def test_embedding_preserves_A(self, result):
        emb = [a for a in result.relation_taxonomy.assessments if a.type_id == 1][0]
        assert emb.preserves_comp_A

    def test_embedding_preserves_B(self, result):
        emb = [a for a in result.relation_taxonomy.assessments if a.type_id == 1][0]
        assert emb.preserves_comp_B

    def test_companion_preserves_A(self, result):
        comp = [a for a in result.relation_taxonomy.assessments if a.type_id == 2][0]
        assert comp.preserves_comp_A

    def test_all_have_verdict(self, result):
        for a in result.relation_taxonomy.assessments:
            assert len(a.verdict) > 0


# ================================================================
# Section 4: Trigger-Type Taxonomy (6 tests)
# ================================================================

class TestTriggerTypeTaxonomy:
    def test_taxonomy_exists(self, result):
        assert result.trigger_taxonomy is not None

    def test_five_types(self, result):
        assert result.trigger_taxonomy.n_types == 5

    def test_explicit_present(self, result):
        names = [s.short_name for s in result.trigger_taxonomy.specs]
        assert "explicit" in names

    def test_curvature_present(self, result):
        names = [s.short_name for s in result.trigger_taxonomy.specs]
        assert "curvature" in names

    def test_source_density_present(self, result):
        names = [s.short_name for s in result.trigger_taxonomy.specs]
        assert "source_density" in names

    def test_lag_processing_present(self, result):
        names = [s.short_name for s in result.trigger_taxonomy.specs]
        assert "lag_processing" in names


# ================================================================
# Section 5: Trigger-Type Assessments (6 tests)
# ================================================================

class TestTriggerTypeAssessments:
    def test_all_coherent(self, result):
        for a in result.trigger_taxonomy.assessments:
            assert a.coherent

    def test_curvature_grut_native(self, result):
        curv = [a for a in result.trigger_taxonomy.assessments if a.trigger_id == 2][0]
        assert curv.grut_native

    def test_explicit_not_grut_native(self, result):
        expl = [a for a in result.trigger_taxonomy.assessments if a.trigger_id == 1][0]
        assert not expl.grut_native

    def test_lag_grut_native(self, result):
        lag = [a for a in result.trigger_taxonomy.assessments if a.trigger_id == 4][0]
        assert lag.grut_native

    def test_curvature_above_explicit(self, result):
        curv = [a for a in result.trigger_taxonomy.assessments if a.trigger_id == 2][0]
        expl = [a for a in result.trigger_taxonomy.assessments if a.trigger_id == 1][0]
        assert curv.score > expl.score

    def test_all_preserve_canon(self, result):
        for a in result.trigger_taxonomy.assessments:
            assert a.preserves_canon


# ================================================================
# Section 6: Canon Preservation (6 tests)
# ================================================================

class TestCanonPreservation:
    def test_checks_exist(self, result):
        assert result.canon_checks is not None

    def test_four_checks(self, result):
        assert len(result.canon_checks) == 4

    def test_embedding_passes(self, result):
        emb = [c for c in result.canon_checks if c.relation_type_id == 1][0]
        assert emb.all_pass

    def test_companion_passes(self, result):
        comp = [c for c in result.canon_checks if c.relation_type_id == 2][0]
        assert comp.all_pass

    def test_emergent_fails(self, result):
        emerg = [c for c in result.canon_checks if c.relation_type_id == 3][0]
        assert not emerg.all_pass

    def test_replacement_fails(self, result):
        repl = [c for c in result.canon_checks if c.relation_type_id == 4][0]
        assert not repl.all_pass


# ================================================================
# Section 7: Minimal Couplings (5 tests)
# ================================================================

class TestMinimalCouplings:
    def test_couplings_exist(self, result):
        assert result.minimal_couplings is not None

    def test_five_couplings(self, result):
        assert len(result.minimal_couplings) == 5

    def test_span_multiple_relations(self, result):
        rel_ids = set(c.relation_type_id for c in result.minimal_couplings)
        assert len(rel_ids) >= 2

    def test_embedding_id_zero_params(self, result):
        assert result.minimal_couplings[0].n_new_params == 0

    def test_all_have_descriptions(self, result):
        for c in result.minimal_couplings:
            assert len(c.description) > 10


# ================================================================
# Section 8: Candidate Ranking (6 tests)
# ================================================================

class TestCandidateRanking:
    def test_ranking_exists(self, result):
        assert result.ranking is not None

    def test_at_least_five(self, result):
        assert result.ranking.n_candidates >= 5

    def test_sorted_descending(self, result):
        scores = [r.combined_score for r in result.ranking.ranked]
        assert all(scores[i] >= scores[i + 1]
                   for i in range(len(scores) - 1))

    def test_top_passes_canon(self, result):
        assert result.ranking.ranked[0].canon_passes

    def test_scores_in_range(self, result):
        for r in result.ranking.ranked:
            assert 0 <= r.combined_score <= 1

    def test_top_score_above_half(self, result):
        assert result.ranking.top_score > 0.5


# ================================================================
# Section 9: Classification (6 tests)
# ================================================================

class TestClassification:
    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_classification_nonempty(self, result):
        assert len(result.classification.classification) > 0

    def test_phase_status_nonempty(self, result):
        assert len(result.classification.phase_status) > 0

    def test_summary_nonempty(self, result):
        assert len(result.classification.summary) > 10

    def test_phase_lock_has_d3(self, result):
        assert "unification_D3" in result.classification.phase_lock_update

    def test_result_valid(self, result):
        assert result.valid


# ================================================================
# Section 10: Nonclaims & Serialization (5 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = scalar_triplet_unification_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100

    def test_serialization_classification(self, result):
        d = scalar_triplet_unification_result_to_dict(result)
        assert len(d["classification"]["classification"]) > 0

    def test_serialization_ranking(self, result):
        d = scalar_triplet_unification_result_to_dict(result)
        assert d["ranking"]["n_candidates"] >= 5
