"""Tests for Phase D12 -- Canonical Source/Charge Derivation.

Verifies:
  - All candidate ontologies are evaluated
  - Requirement-matching logic is consistent
  - Classification outputs are deterministic
  - Final D12 classification is reproducible from explicit criteria
  - Ranking logic is inspectable and non-circular
  - Serialization round-trips correctly
"""

from __future__ import annotations

import math
import pytest
from typing import List

from grut.canonical_q_derivation import (
    # Constants
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    LAMBDA_DEFAULT,
    ETA_TARGET,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    ETA_SQUARED,
    WINDING_NUMBER_N1,
    Q_TOPO_N1,
    N_CANDIDATE_ONTOLOGIES,
    N_REQUIREMENT_SOURCES,
    CLASSIFICATION_OPTIONS,
    ONTOLOGY_RATING_OPTIONS,
    REQUIREMENT_STRENGTH_OPTIONS,
    D12_ASSUMPTIONS,
    D12_NONCLAIMS,
    # Dataclasses
    PhaseRequirement,
    RequirementSet,
    OntologyTest,
    OntologyCandidate,
    OntologyRanking,
    RequirementMatchEntry,
    RequirementMatchingTable,
    LogicalCircleClosure,
    D12Classification,
    D12Result,
    # Functions
    build_requirement_set,
    build_ontology_candidates,
    rank_ontology_candidates,
    build_matching_table,
    build_logical_circle_closure,
    classify_d12,
    compute_canonical_q_derivation,
    d12_result_to_dict,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def d12_result() -> D12Result:
    """Run the full D12 computation once for all tests."""
    return compute_canonical_q_derivation()


@pytest.fixture(scope="module")
def requirements() -> RequirementSet:
    return build_requirement_set()


@pytest.fixture(scope="module")
def candidates(requirements) -> List[OntologyCandidate]:
    return build_ontology_candidates(requirements)


@pytest.fixture(scope="module")
def ranking(candidates) -> OntologyRanking:
    return rank_ontology_candidates(candidates)


@pytest.fixture(scope="module")
def matching_table(candidates, requirements) -> RequirementMatchingTable:
    return build_matching_table(candidates, requirements)


@pytest.fixture(scope="module")
def logical_circle(ranking) -> LogicalCircleClosure:
    return build_logical_circle_closure(ranking)


# ================================================================
# 1. Constants and identities
# ================================================================

class TestConstants:
    """Verify canonical constants and derived identities."""

    def test_alpha_vac(self):
        assert ALPHA_VAC == pytest.approx(1.0 / 3.0)

    def test_r_eq(self):
        assert R_EQ == pytest.approx(R_S * ALPHA_VAC)

    def test_tau_canonical(self):
        assert TAU_CANONICAL == pytest.approx(math.sqrt(1.5))

    def test_a_crit(self):
        assert A_CRIT == pytest.approx(1.062)

    def test_eta_target(self):
        assert ETA_TARGET == pytest.approx(1.0 / math.sqrt(8.0 * math.pi))

    def test_comp_b_coeff(self):
        assert COMP_B_COEFF == pytest.approx(1.0 / (8.0 * math.pi))

    def test_eta_squared_equals_comp_b(self):
        """Critical identity: eta^2 = COMP_B_COEFF = 1/(8*pi)."""
        assert ETA_SQUARED == pytest.approx(COMP_B_COEFF, rel=1e-10)

    def test_eta_squared_definition(self):
        assert ETA_SQUARED == pytest.approx(ETA_TARGET ** 2, rel=1e-10)

    def test_q_topo_n1(self):
        assert Q_TOPO_N1 == pytest.approx(WINDING_NUMBER_N1 * ETA_TARGET)

    def test_winding_number_integer(self):
        assert isinstance(WINDING_NUMBER_N1, int)
        assert WINDING_NUMBER_N1 == 1

    def test_n_candidate_ontologies(self):
        assert N_CANDIDATE_ONTOLOGIES == 6

    def test_n_requirement_sources(self):
        assert N_REQUIREMENT_SOURCES == 5

    def test_rho_eq_coeff(self):
        expected = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
        assert RHO_EQ_COEFF == pytest.approx(expected)


# ================================================================
# 2. Classification option sets
# ================================================================

class TestClassificationOptions:
    """Verify option lists are complete and non-empty."""

    def test_classification_options_count(self):
        assert len(CLASSIFICATION_OPTIONS) == 5

    def test_classification_options_unique(self):
        assert len(set(CLASSIFICATION_OPTIONS)) == len(CLASSIFICATION_OPTIONS)

    def test_ontology_rating_options_count(self):
        assert len(ONTOLOGY_RATING_OPTIONS) == 5

    def test_ontology_rating_options_unique(self):
        assert len(set(ONTOLOGY_RATING_OPTIONS)) == len(ONTOLOGY_RATING_OPTIONS)

    def test_requirement_strength_options(self):
        assert set(REQUIREMENT_STRENGTH_OPTIONS) == {
            "strong", "partial", "weak", "none"
        }

    def test_classification_contains_expected(self):
        expected = [
            "canonically_derived",
            "principled_and_strongly_constrained",
            "defect_realized_but_not_uniquely_derived",
            "still_effective_only",
            "unresolved",
        ]
        for e in expected:
            assert e in CLASSIFICATION_OPTIONS

    def test_rating_contains_expected(self):
        expected = [
            "eliminated", "weakly_viable", "strongly_viable",
            "best_supported", "derived",
        ]
        for e in expected:
            assert e in ONTOLOGY_RATING_OPTIONS


# ================================================================
# 3. Assumptions and nonclaims
# ================================================================

class TestAssumptionsAndNonclaims:
    """Verify assumptions and nonclaims are documented."""

    def test_assumptions_count(self):
        assert len(D12_ASSUMPTIONS) == 10

    def test_nonclaims_count(self):
        assert len(D12_NONCLAIMS) == 10

    def test_assumptions_all_nonempty(self):
        for a in D12_ASSUMPTIONS:
            assert len(a) > 10

    def test_nonclaims_all_nonempty(self):
        for n in D12_NONCLAIMS:
            assert len(n) > 10

    def test_assumptions_numbered(self):
        for i, a in enumerate(D12_ASSUMPTIONS):
            assert a.startswith(f"{i + 1}.")

    def test_nonclaims_numbered(self):
        for i, n in enumerate(D12_NONCLAIMS):
            assert n.startswith(f"{i + 1}.")


# ================================================================
# 4. Requirement set
# ================================================================

class TestRequirementSet:
    """Verify the requirement reconstruction."""

    def test_requirement_count(self, requirements):
        assert requirements.n_requirements == N_REQUIREMENT_SOURCES

    def test_all_requirements_have_ids(self, requirements):
        for r in requirements.requirements:
            assert r.requirement_id != ""

    def test_requirement_ids_unique(self, requirements):
        ids = [r.requirement_id for r in requirements.requirements]
        assert len(set(ids)) == len(ids)

    def test_all_requirements_locked(self, requirements):
        for r in requirements.requirements:
            assert r.locked is True

    def test_requirement_ids_present(self, requirements):
        expected_ids = {
            "REQ_6C_SHAPE",
            "REQ_6C_COEFF",
            "REQ_ROUTEBC_CLOSURE",
            "REQ_D1_ADMISSIBILITY",
            "REQ_D11_VIABILITY",
        }
        actual_ids = {r.requirement_id for r in requirements.requirements}
        assert actual_ids == expected_ids

    def test_all_requirements_have_descriptions(self, requirements):
        for r in requirements.requirements:
            assert len(r.description) > 20

    def test_all_requirements_have_formal_conditions(self, requirements):
        for r in requirements.requirements:
            assert len(r.formal_condition) > 10

    def test_source_phases_nonempty(self, requirements):
        assert len(requirements.source_phases) > 0


# ================================================================
# 5. Ontology candidates
# ================================================================

class TestOntologyCandidates:
    """Verify all candidate ontologies are constructed and tested."""

    def test_candidate_count(self, candidates):
        assert len(candidates) == N_CANDIDATE_ONTOLOGIES

    def test_candidate_ids_unique(self, candidates):
        ids = [c.candidate_id for c in candidates]
        assert len(set(ids)) == len(ids)

    def test_expected_candidate_ids(self, candidates):
        expected = {
            "topological_winding_number",
            "noether_charge",
            "geometric_support_invariant",
            "curvature_triggered_source",
            "memory_sector_emergent",
            "effective_defect_charge",
        }
        actual = {c.candidate_id for c in candidates}
        assert actual == expected

    def test_all_candidates_have_names(self, candidates):
        for c in candidates:
            assert len(c.name) > 3

    def test_all_candidates_have_descriptions(self, candidates):
        for c in candidates:
            assert len(c.description) > 20

    def test_all_candidates_have_formulas(self, candidates):
        for c in candidates:
            assert len(c.formula) > 5

    def test_all_candidates_tested_against_all_requirements(
        self, candidates, requirements
    ):
        n_req = requirements.n_requirements
        for c in candidates:
            assert len(c.requirement_tests) == n_req
            total = (c.n_requirements_satisfied
                     + c.n_requirements_partial
                     + c.n_requirements_failed)
            assert total == n_req

    def test_requirement_test_strengths_valid(self, candidates):
        valid_strengths = set(REQUIREMENT_STRENGTH_OPTIONS)
        for c in candidates:
            for t in c.requirement_tests:
                assert t.strength in valid_strengths

    def test_all_candidates_have_ratings(self, ranking):
        valid_ratings = set(ONTOLOGY_RATING_OPTIONS)
        for c in ranking.candidates:
            assert c.rating in valid_ratings

    def test_topological_candidate_has_highest_strong_count(self, candidates):
        topo = next(c for c in candidates
                    if c.candidate_id == "topological_winding_number")
        for c in candidates:
            if c.candidate_id != "topological_winding_number":
                assert c.n_requirements_satisfied <= topo.n_requirements_satisfied


# ================================================================
# 6. Specific candidate properties
# ================================================================

class TestSpecificCandidates:
    """Verify key properties of individual candidates (post-ranking)."""

    def test_topological_is_best_supported(self, ranking):
        topo = next(c for c in ranking.candidates
                    if c.candidate_id == "topological_winding_number")
        assert topo.rating == "best_supported"

    def test_topological_not_grut_native(self, ranking):
        topo = next(c for c in ranking.candidates
                    if c.candidate_id == "topological_winding_number")
        assert topo.grut_native is False

    def test_topological_support_class_match(self, ranking):
        topo = next(c for c in ranking.candidates
                    if c.candidate_id == "topological_winding_number")
        assert topo.support_class_match is True
        assert topo.coefficient_match is True

    def test_noether_eliminated(self, ranking):
        noether = next(c for c in ranking.candidates
                       if c.candidate_id == "noether_charge")
        assert noether.rating == "eliminated"

    def test_memory_eliminated(self, ranking):
        mem = next(c for c in ranking.candidates
                   if c.candidate_id == "memory_sector_emergent")
        assert mem.rating == "eliminated"

    def test_memory_is_grut_native(self, ranking):
        """Memory-sector candidate is GRUT-native but mechanism-eliminated."""
        mem = next(c for c in ranking.candidates
                   if c.candidate_id == "memory_sector_emergent")
        assert mem.grut_native is True
        assert mem.support_class_match is False

    def test_geometric_eliminated(self, ranking):
        geom = next(c for c in ranking.candidates
                    if c.candidate_id == "geometric_support_invariant")
        assert geom.rating == "eliminated"

    def test_effective_weakly_viable(self, ranking):
        eff = next(c for c in ranking.candidates
                   if c.candidate_id == "effective_defect_charge")
        assert eff.rating == "weakly_viable"

    def test_curvature_weakly_viable(self, ranking):
        curv = next(c for c in ranking.candidates
                    if c.candidate_id == "curvature_triggered_source")
        assert curv.rating == "weakly_viable"

    def test_topological_has_quantization(self, ranking):
        topo = next(c for c in ranking.candidates
                    if c.candidate_id == "topological_winding_number")
        assert "quantized" in topo.conservation_quantization.lower()

    def test_topological_generalizes(self, ranking):
        topo = next(c for c in ranking.candidates
                    if c.candidate_id == "topological_winding_number")
        assert topo.generalizes_beyond_implementation is True


# ================================================================
# 7. Ranking
# ================================================================

class TestRanking:
    """Verify ranking logic and ordering."""

    def test_ranking_best_candidate(self, ranking):
        assert ranking.best_candidate_id == "topological_winding_number"

    def test_ranking_best_rating(self, ranking):
        assert ranking.best_rating == "best_supported"

    def test_ranking_order_length(self, ranking):
        assert len(ranking.ranking_order) == N_CANDIDATE_ONTOLOGIES

    def test_ranking_order_first(self, ranking):
        assert ranking.ranking_order[0] == "topological_winding_number"

    def test_ranking_order_last(self, ranking):
        """Memory-sector (all-failed) should be last."""
        assert ranking.ranking_order[-1] == "memory_sector_emergent"

    def test_ranking_method_documented(self, ranking):
        assert len(ranking.ranking_method) > 50

    def test_ranking_is_deterministic(self, requirements):
        """Running ranking twice produces the same order."""
        c1 = build_ontology_candidates(requirements)
        r1 = rank_ontology_candidates(c1)
        c2 = build_ontology_candidates(requirements)
        r2 = rank_ontology_candidates(c2)
        assert r1.ranking_order == r2.ranking_order
        assert r1.best_candidate_id == r2.best_candidate_id

    def test_no_derived_candidates(self, ranking):
        """No candidate should be 'derived' (none is GRUT-native + all-strong)."""
        for c in ranking.candidates:
            assert c.rating != "derived"

    def test_exactly_one_best_supported(self, ranking):
        best_count = sum(1 for c in ranking.candidates
                         if c.rating == "best_supported")
        assert best_count == 1


# ================================================================
# 8. Requirement-matching table
# ================================================================

class TestMatchingTable:
    """Verify the requirement x candidate matching table."""

    def test_entry_count(self, matching_table):
        expected = N_CANDIDATE_ONTOLOGIES * N_REQUIREMENT_SOURCES
        assert len(matching_table.entries) == expected

    def test_n_candidates(self, matching_table):
        assert matching_table.n_candidates == N_CANDIDATE_ONTOLOGIES

    def test_n_requirements(self, matching_table):
        assert matching_table.n_requirements == N_REQUIREMENT_SOURCES

    def test_all_entries_have_strength(self, matching_table):
        valid = set(REQUIREMENT_STRENGTH_OPTIONS)
        for e in matching_table.entries:
            assert e.strength in valid

    def test_all_entries_have_comments(self, matching_table):
        for e in matching_table.entries:
            assert len(e.comment) > 10

    def test_all_candidate_requirement_pairs_covered(self, matching_table):
        pairs = {(e.candidate_id, e.requirement_id)
                 for e in matching_table.entries}
        expected_candidates = {
            "topological_winding_number", "noether_charge",
            "geometric_support_invariant", "curvature_triggered_source",
            "memory_sector_emergent", "effective_defect_charge",
        }
        expected_reqs = {
            "REQ_6C_SHAPE", "REQ_6C_COEFF", "REQ_ROUTEBC_CLOSURE",
            "REQ_D1_ADMISSIBILITY", "REQ_D11_VIABILITY",
        }
        for cid in expected_candidates:
            for rid in expected_reqs:
                assert (cid, rid) in pairs


# ================================================================
# 9. Logical circle closure
# ================================================================

class TestLogicalCircle:
    """Verify the logical circle closure statement."""

    def test_circle_closed(self, logical_circle):
        assert logical_circle.circle_closed is True

    def test_phase_6c_link_nonempty(self, logical_circle):
        assert len(logical_circle.phase_6c_link) > 50

    def test_source_law_link_nonempty(self, logical_circle):
        assert len(logical_circle.source_law_link) > 50

    def test_family_4_link_nonempty(self, logical_circle):
        assert len(logical_circle.family_4_link) > 50

    def test_defect_realization_link_nonempty(self, logical_circle):
        assert len(logical_circle.defect_realization_link) > 50

    def test_d11_link_nonempty(self, logical_circle):
        assert len(logical_circle.d11_exact_closure_link) > 50

    def test_closure_paragraph_nonempty(self, logical_circle):
        assert len(logical_circle.closure_paragraph) > 100

    def test_closure_qualification_nonempty(self, logical_circle):
        assert len(logical_circle.closure_qualification) > 50

    def test_closure_paragraph_mentions_pi_2(self, logical_circle):
        assert "pi_2" in logical_circle.closure_paragraph

    def test_closure_paragraph_mentions_extension(self, logical_circle):
        assert "extension" in logical_circle.closure_paragraph.lower()


# ================================================================
# 10. Final D12 classification
# ================================================================

class TestD12Classification:
    """Verify the final classification output."""

    def test_classification_valid_option(self, d12_result):
        assert d12_result.classification.classification in CLASSIFICATION_OPTIONS

    def test_classification_is_principled(self, d12_result):
        assert d12_result.classification.classification == (
            "principled_and_strongly_constrained"
        )

    def test_best_ontology(self, d12_result):
        assert d12_result.classification.best_ontology == (
            "topological_winding_number"
        )

    def test_best_ontology_rating(self, d12_result):
        assert d12_result.classification.best_ontology_rating == "best_supported"

    def test_summary_nonempty(self, d12_result):
        assert len(d12_result.classification.summary) > 50

    def test_canon_statement_nonempty(self, d12_result):
        assert len(d12_result.classification.canon_statement) > 50

    def test_remaining_gap_nonempty(self, d12_result):
        assert len(d12_result.classification.remaining_gap) > 20

    def test_rating_counts_sum(self, d12_result):
        cls = d12_result.classification
        total = (cls.n_eliminated + cls.n_weakly_viable
                 + cls.n_strongly_viable + cls.n_best_supported
                 + cls.n_derived)
        assert total == N_CANDIDATE_ONTOLOGIES

    def test_no_derived(self, d12_result):
        assert d12_result.classification.n_derived == 0

    def test_one_best_supported(self, d12_result):
        assert d12_result.classification.n_best_supported == 1

    def test_canon_statement_mentions_eta(self, d12_result):
        assert "eta" in d12_result.classification.canon_statement

    def test_canon_statement_mentions_winding(self, d12_result):
        assert "winding" in d12_result.classification.canon_statement.lower()

    def test_remaining_gap_mentions_o3(self, d12_result):
        assert "O(3)" in d12_result.classification.remaining_gap


# ================================================================
# 11. Master result and serialization
# ================================================================

class TestMasterResultAndSerialization:
    """Verify the master result container and serialization."""

    def test_result_valid(self, d12_result):
        assert d12_result.valid is True

    def test_result_has_requirements(self, d12_result):
        assert d12_result.requirements is not None

    def test_result_has_candidates(self, d12_result):
        assert d12_result.candidates is not None
        assert len(d12_result.candidates) == N_CANDIDATE_ONTOLOGIES

    def test_result_has_ranking(self, d12_result):
        assert d12_result.ranking is not None

    def test_result_has_matching_table(self, d12_result):
        assert d12_result.matching_table is not None

    def test_result_has_logical_circle(self, d12_result):
        assert d12_result.logical_circle is not None

    def test_result_has_classification(self, d12_result):
        assert d12_result.classification is not None

    def test_serialization_valid(self, d12_result):
        d = d12_result_to_dict(d12_result)
        assert d["valid"] is True

    def test_serialization_has_all_keys(self, d12_result):
        d = d12_result_to_dict(d12_result)
        expected_keys = {
            "valid", "requirements", "candidates", "ranking",
            "matching_table", "logical_circle", "classification",
        }
        assert set(d.keys()) == expected_keys

    def test_serialization_candidates_count(self, d12_result):
        d = d12_result_to_dict(d12_result)
        assert len(d["candidates"]) == N_CANDIDATE_ONTOLOGIES

    def test_serialization_classification(self, d12_result):
        d = d12_result_to_dict(d12_result)
        assert d["classification"]["classification"] == (
            "principled_and_strongly_constrained"
        )

    def test_serialization_matching_table_entries(self, d12_result):
        d = d12_result_to_dict(d12_result)
        expected = N_CANDIDATE_ONTOLOGIES * N_REQUIREMENT_SOURCES
        assert len(d["matching_table"]["entries"]) == expected

    def test_serialization_ranking_order(self, d12_result):
        d = d12_result_to_dict(d12_result)
        assert d["ranking"]["ranking_order"][0] == "topological_winding_number"

    def test_serialization_logical_circle(self, d12_result):
        d = d12_result_to_dict(d12_result)
        assert d["logical_circle"]["circle_closed"] is True

    def test_deterministic_full_computation(self):
        """Full computation is deterministic across two runs."""
        r1 = compute_canonical_q_derivation()
        r2 = compute_canonical_q_derivation()
        assert r1.classification.classification == r2.classification.classification
        assert r1.classification.best_ontology == r2.classification.best_ontology
        assert r1.ranking.ranking_order == r2.ranking.ranking_order

    def test_invalid_result_serialization(self):
        r = D12Result(valid=False)
        d = d12_result_to_dict(r)
        assert d == {"valid": False}
