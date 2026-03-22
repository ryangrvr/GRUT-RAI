"""
Tests for grut.geometric_induction_o3
======================================

Phase D13: Geometric Induction of the O(3) Sector

Verifies:
- All candidate constructions are evaluated
- All pathways are assessed
- Requirement-matching logic is consistent
- Derivation criteria are assessed for all pathways
- Classification is deterministic and reproducible
- No hidden scoring or ad hoc weights
- Exported result structure is complete
"""

import json
import os
import tempfile

import pytest

from grut.geometric_induction_o3 import (
    CONSTRUCTION_VERDICTS,
    D13_CLASSIFICATION_OPTIONS,
    DERIVATION_CRITERIA,
    NONCLAIMS,
    PATHWAY_VERDICTS,
    PRIOR_REQUIREMENTS,
    REQUIREMENT_MATCH_LEVELS,
    CandidateConstruction,
    D13Classification,
    D13Result,
    DerivationCriterionResult,
    DerivationTarget,
    FoundationalGap,
    PathwayAssessment,
    RequirementMatchEntry,
    RequirementMatchingTable,
    assess_derivation_criteria,
    assess_pathways,
    build_candidate_constructions,
    build_requirement_matching,
    classify_geometric_induction,
    compute_geometric_induction,
    d13_result_to_dict,
    define_derivation_target,
    export_d13_result_json,
    identify_remaining_gaps,
)


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="module")
def d13_result():
    return compute_geometric_induction()


@pytest.fixture(scope="module")
def constructions(d13_result):
    return d13_result.constructions


@pytest.fixture(scope="module")
def pathways(d13_result):
    return d13_result.pathway_assessments


@pytest.fixture(scope="module")
def req_matching(d13_result):
    return d13_result.requirement_matching


@pytest.fixture(scope="module")
def criteria_results(d13_result):
    return d13_result.derivation_criteria_results


@pytest.fixture(scope="module")
def classification(d13_result):
    return d13_result.classification


@pytest.fixture(scope="module")
def gaps(d13_result):
    return d13_result.remaining_gaps


# ===================================================================
# Class: TestVocabulary
# ===================================================================

class TestVocabulary:
    """Test vocabulary constants."""

    def test_classification_options(self):
        assert len(D13_CLASSIFICATION_OPTIONS) == 5

    def test_construction_verdicts(self):
        assert len(CONSTRUCTION_VERDICTS) == 5

    def test_pathway_verdicts(self):
        assert len(PATHWAY_VERDICTS) == 6

    def test_requirement_match_levels(self):
        assert len(REQUIREMENT_MATCH_LEVELS) == 5

    def test_prior_requirements(self):
        assert len(PRIOR_REQUIREMENTS) == 6

    def test_derivation_criteria(self):
        assert len(DERIVATION_CRITERIA) == 6

    def test_nonclaims(self):
        assert len(NONCLAIMS) >= 5


# ===================================================================
# Class: TestDerivationTarget
# ===================================================================

class TestDerivationTarget:
    """Test derivation target definition."""

    def test_target_has_all_criteria(self):
        target = define_derivation_target()
        assert len(target.criteria) == 6
        assert set(target.criteria) == set(DERIVATION_CRITERIA)

    def test_target_description_nonempty(self):
        target = define_derivation_target()
        assert len(target.description) > 100


# ===================================================================
# Class: TestCandidateConstructions
# ===================================================================

class TestCandidateConstructions:
    """Test candidate construction evaluation."""

    def test_construction_count(self, constructions):
        assert len(constructions) == 10

    def test_all_verdicts_valid(self, constructions):
        for c in constructions:
            assert c.verdict in CONSTRUCTION_VERDICTS, (
                f"Construction '{c.name}' has invalid verdict '{c.verdict}'"
            )

    def test_three_pathways_covered(self, constructions):
        pathways = {c.pathway for c in constructions}
        assert pathways == {"tetrad_geometric", "memory_tensorization", "uv_completion"}

    def test_tetrad_constructions_count(self, constructions):
        tetrad = [c for c in constructions if c.pathway == "tetrad_geometric"]
        assert len(tetrad) == 5

    def test_memory_constructions_count(self, constructions):
        memory = [c for c in constructions if c.pathway == "memory_tensorization"]
        assert len(memory) == 3

    def test_uv_constructions_count(self, constructions):
        uv = [c for c in constructions if c.pathway == "uv_completion"]
        assert len(uv) == 2

    def test_all_have_ingredients(self, constructions):
        for c in constructions:
            assert len(c.ingredients) >= 2, (
                f"Construction '{c.name}' has fewer than 2 ingredients"
            )

    def test_all_have_reasoning(self, constructions):
        for c in constructions:
            assert len(c.reasoning) > 30, (
                f"Construction '{c.name}' has insufficient reasoning"
            )

    def test_grut_native_flag_set(self, constructions):
        for c in constructions:
            assert isinstance(c.grut_native, bool)

    def test_uv_constructions_not_grut_native(self, constructions):
        uv = [c for c in constructions if c.pathway == "uv_completion"]
        for c in uv:
            assert c.grut_native is False

    def test_tetrad_memory_are_grut_native(self, constructions):
        native = [c for c in constructions
                   if c.pathway in ("tetrad_geometric", "memory_tensorization")]
        for c in native:
            assert c.grut_native is True

    def test_no_construction_claims_derivation(self, constructions):
        for c in constructions:
            assert c.verdict != "derived", (
                f"Construction '{c.name}' claims derivation -- "
                f"this should not happen without extraordinary evidence"
            )

    def test_invalid_verdict_rejected(self):
        with pytest.raises(ValueError, match="Invalid verdict"):
            CandidateConstruction(
                name="test", pathway="test",
                ingredients=["a", "b"],
                construction_description="test",
                symmetry_status="test",
                grut_native=True,
                support_class_outcome="test",
                coefficient_outcome="test",
                strong_field_activation="test",
                hedgehog_emergence="test",
                verdict="INVALID",
                reasoning="test",
            )


# ===================================================================
# Class: TestPathwayAssessments
# ===================================================================

class TestPathwayAssessments:
    """Test pathway assessments."""

    def test_three_pathways(self, pathways):
        assert len(pathways) == 3

    def test_pathway_names(self, pathways):
        names = {p.pathway for p in pathways}
        assert names == {"tetrad_geometric", "memory_tensorization", "uv_completion"}

    def test_all_verdicts_valid(self, pathways):
        for p in pathways:
            assert p.verdict in PATHWAY_VERDICTS

    def test_memory_has_support_class_success(self, pathways):
        memory = next(p for p in pathways if p.pathway == "memory_tensorization")
        assert memory.support_class_success is True

    def test_memory_has_ontology_continuity(self, pathways):
        memory = next(p for p in pathways if p.pathway == "memory_tensorization")
        assert memory.ontology_continuity is True

    def test_uv_not_native(self, pathways):
        uv = next(p for p in pathways if p.pathway == "uv_completion")
        assert uv.native_to_grut is False

    def test_tetrad_and_memory_native(self, pathways):
        for p in pathways:
            if p.pathway in ("tetrad_geometric", "memory_tensorization"):
                assert p.native_to_grut is True

    def test_all_have_summary(self, pathways):
        for p in pathways:
            assert len(p.summary) > 50

    def test_each_pathway_has_constructions(self, pathways):
        for p in pathways:
            assert len(p.constructions) >= 2

    def test_invalid_pathway_verdict_rejected(self):
        with pytest.raises(ValueError, match="Invalid pathway verdict"):
            PathwayAssessment(
                pathway="test",
                native_to_grut=True,
                mathematical_discipline="heuristic",
                support_class_success=False,
                coefficient_constraint=False,
                ontology_continuity=False,
                strong_field_necessity=False,
                constructions=[],
                verdict="INVALID",
                summary="test",
            )

    def test_deterministic(self):
        c1 = build_candidate_constructions()
        c2 = build_candidate_constructions()
        p1 = assess_pathways(c1)
        p2 = assess_pathways(c2)
        for a, b in zip(p1, p2):
            assert a.pathway == b.pathway
            assert a.verdict == b.verdict


# ===================================================================
# Class: TestRequirementMatching
# ===================================================================

class TestRequirementMatching:
    """Test requirement-matching table."""

    def test_six_requirements(self, req_matching):
        assert len(req_matching.entries) == 6

    def test_all_match_levels_valid(self, req_matching):
        for entry in req_matching.entries:
            for val in [entry.tetrad_induction, entry.tensorized_memory, entry.uv_completion]:
                assert val in REQUIREMENT_MATCH_LEVELS, (
                    f"Requirement '{entry.requirement}' has invalid match level '{val}'"
                )

    def test_all_have_comments(self, req_matching):
        for entry in req_matching.entries:
            assert len(entry.comments) > 10

    def test_homotopy_strong_across_viable_pathways(self, req_matching):
        homotopy = next(
            e for e in req_matching.entries if "HOMOTOPY" in e.requirement
        )
        assert homotopy.tetrad_induction == "strong"
        assert homotopy.tensorized_memory == "strong"

    def test_coefficient_none_everywhere(self, req_matching):
        coeff = next(
            e for e in req_matching.entries if "COEFF" in e.requirement
        )
        assert coeff.tetrad_induction == "none"
        assert coeff.tensorized_memory == "none"
        assert coeff.uv_completion == "none"

    def test_invalid_match_level_rejected(self):
        with pytest.raises(ValueError, match="Invalid match level"):
            RequirementMatchEntry(
                requirement="test",
                tetrad_induction="INVALID",
                tensorized_memory="strong",
                uv_completion="none",
                comments="test",
            )


# ===================================================================
# Class: TestDerivationCriteria
# ===================================================================

class TestDerivationCriteria:
    """Test derivation criteria assessment."""

    def test_six_criteria(self, criteria_results):
        assert len(criteria_results) == 6

    def test_all_criteria_covered(self, criteria_results):
        criteria_names = {r.criterion for r in criteria_results}
        assert criteria_names == set(DERIVATION_CRITERIA)

    def test_all_have_best_pathway(self, criteria_results):
        for r in criteria_results:
            assert len(r.best_pathway) > 0

    def test_coefficient_has_no_best(self, criteria_results):
        coeff = next(r for r in criteria_results if r.criterion == "coefficient_constraint")
        assert coeff.best_pathway == "none"

    def test_support_class_best_is_memory(self, criteria_results):
        support = next(r for r in criteria_results if r.criterion == "support_class_1_over_r2")
        assert support.best_pathway == "memory_tensorization"

    def test_all_have_notes(self, criteria_results):
        for r in criteria_results:
            assert len(r.notes) > 10


# ===================================================================
# Class: TestClassification
# ===================================================================

class TestClassification:
    """Test D13 classification."""

    def test_classification_valid(self, classification):
        assert classification.classification in D13_CLASSIFICATION_OPTIONS

    def test_classification_value(self, classification):
        assert classification.classification == "partially_motivated_not_derived"

    def test_best_pathway_is_memory(self, classification):
        assert classification.best_pathway == "memory_tensorization"

    def test_justification_nonempty(self, classification):
        assert len(classification.justification) > 50

    def test_criteria_total(self, classification):
        assert classification.derivation_criteria_total == 6

    def test_requirements_total(self, classification):
        assert classification.requirements_total == 6

    def test_not_canonically_derived(self, classification):
        assert classification.classification != "canonically_derived_from_geometry"

    def test_not_effectively_induced(self, classification):
        assert classification.classification != "effectively_induced_but_not_fundamental"

    def test_deterministic(self):
        r1 = compute_geometric_induction()
        r2 = compute_geometric_induction()
        assert r1.classification.classification == r2.classification.classification
        assert r1.classification.best_pathway == r2.classification.best_pathway

    def test_invalid_classification_rejected(self):
        with pytest.raises(ValueError, match="Invalid D13 classification"):
            D13Classification(
                classification="INVALID",
                best_pathway="test",
                justification="test",
                derivation_criteria_met=0,
                derivation_criteria_total=6,
                requirements_strong=0,
                requirements_total=6,
            )


# ===================================================================
# Class: TestRemainingGaps
# ===================================================================

class TestRemainingGaps:
    """Test remaining foundational gaps."""

    def test_gaps_nonempty(self, gaps):
        assert len(gaps) >= 4

    def test_has_critical_gaps(self, gaps):
        critical = [g for g in gaps if g.severity == "critical"]
        assert len(critical) >= 2

    def test_gap_severities_valid(self, gaps):
        valid = {"critical", "significant", "minor"}
        for g in gaps:
            assert g.severity in valid

    def test_tensor_potential_gap(self, gaps):
        pot = next(g for g in gaps if "potential" in g.gap.lower())
        assert pot.severity == "critical"

    def test_stability_gap(self, gaps):
        stab = next(g for g in gaps if "stability" in g.gap.lower())
        assert stab.severity == "critical"

    def test_coefficient_gap(self, gaps):
        coeff = next(g for g in gaps if "eta" in g.gap.lower() or "coefficient" in g.gap.lower())
        assert coeff.severity == "significant"


# ===================================================================
# Class: TestExport
# ===================================================================

class TestExport:
    """Test export functionality."""

    def test_to_dict_valid(self, d13_result):
        d = d13_result_to_dict(d13_result)
        assert isinstance(d, dict)
        assert d["valid"] is True
        assert "constructions" in d
        assert "pathway_assessments" in d
        assert "classification" in d

    def test_to_dict_serializable(self, d13_result):
        d = d13_result_to_dict(d13_result)
        s = json.dumps(d, default=str)
        assert len(s) > 1000

    def test_export_json(self, d13_result):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            export_d13_result_json(d13_result, path)
            with open(path) as f:
                data = json.load(f)
            assert data["valid"] is True
            assert len(data["constructions"]) == 10
        finally:
            os.unlink(path)

    def test_constructions_in_export(self, d13_result):
        d = d13_result_to_dict(d13_result)
        names = {c["name"] for c in d["constructions"]}
        assert any("memory tensor" in n.lower() or "Memory tensor" in n for n in names)

    def test_nonclaims_in_export(self, d13_result):
        d = d13_result_to_dict(d13_result)
        assert len(d["nonclaims"]) >= 5


# ===================================================================
# Class: TestD13Result
# ===================================================================

class TestD13Result:
    """Test top-level D13 result."""

    def test_valid(self, d13_result):
        assert d13_result.valid is True

    def test_all_components_present(self, d13_result):
        assert d13_result.derivation_target is not None
        assert d13_result.constructions is not None
        assert d13_result.pathway_assessments is not None
        assert d13_result.requirement_matching is not None
        assert d13_result.derivation_criteria_results is not None
        assert d13_result.classification is not None
        assert d13_result.remaining_gaps is not None
        assert d13_result.nonclaims is not None

    def test_deterministic(self):
        r1 = compute_geometric_induction()
        r2 = compute_geometric_induction()
        assert r1.classification.classification == r2.classification.classification
        assert len(r1.constructions) == len(r2.constructions)
