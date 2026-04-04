"""Tests for grut.dark_sector_extension (Appendix B).

Coverage:
- Vocabulary and constant validation
- Problem definition (DM/DE separation)
- Dark matter analysis and hard-gated classification
- Dark energy analysis and hard-gated classification
- Minimal mathematical models
- Comparison classes
- Overall classification
- Assumptions and remaining gaps
- Nonclaims
- Export / serialization
- Determinism
"""

from __future__ import annotations

import json
import math

import pytest

from grut.dark_sector_extension import (
    # Vocabularies
    DM_CLASSIFICATION_OPTIONS,
    DE_CLASSIFICATION_OPTIONS,
    APPENDIX_B_CLASSIFICATION_OPTIONS,
    INTERPRETATION_LEVELS,
    SCENARIO_TYPES,
    ASSUMPTION_STATUSES,
    PARAMETER_AUTHORITY_LEVELS,
    SECTOR_RELEVANCE_LEVELS,
    # Constants
    ALPHA_VAC,
    TAU_CANONICAL,
    LAMBDA_DEFAULT,
    ETA_TARGET,
    COMP_B_COEFF,
    # Dataclasses
    SectorRelevance,
    DarkSectorProblem,
    DarkMatterTest,
    DarkMatterResult,
    DarkEnergyTest,
    DarkEnergyResult,
    ParameterEntry,
    MinimalModel,
    ScenarioComparison,
    ComparisonResult,
    AssumptionEntry,
    FoundationalGap,
    AppendixBClassification,
    AppendixBResult,
    # Builders
    define_dark_sector_problems,
    analyze_dark_matter,
    analyze_dark_energy,
    build_minimal_models,
    build_comparisons,
    classify_appendix_b,
    build_assumptions,
    build_nonclaims,
    identify_remaining_gaps,
    compute_dark_sector_result,
    appendix_b_result_to_dict,
    appendix_b_result_to_json,
)


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="module")
def result() -> AppendixBResult:
    return compute_dark_sector_result()


# ===================================================================
# Vocabulary tests
# ===================================================================

class TestVocabulary:
    def test_dm_classification_options(self):
        assert len(DM_CLASSIFICATION_OPTIONS) == 5
        assert "dark_matter_interpretation_partial_mimic" in DM_CLASSIFICATION_OPTIONS
        assert "dark_matter_interpretation_failed" in DM_CLASSIFICATION_OPTIONS

    def test_de_classification_options(self):
        assert len(DE_CLASSIFICATION_OPTIONS) == 5
        assert "dark_energy_interpretation_reframes_but_does_not_solve" in DE_CLASSIFICATION_OPTIONS

    def test_overall_classification_options(self):
        assert len(APPENDIX_B_CLASSIFICATION_OPTIONS) == 5
        assert "mixed_and_partial" in APPENDIX_B_CLASSIFICATION_OPTIONS

    def test_interpretation_levels(self):
        assert len(INTERPRETATION_LEVELS) == 6
        assert "derived" in INTERPRETATION_LEVELS
        assert "failed" in INTERPRETATION_LEVELS

    def test_scenario_types(self):
        assert len(SCENARIO_TYPES) == 3
        assert "classical_baseline" in SCENARIO_TYPES

    def test_assumption_statuses(self):
        assert len(ASSUMPTION_STATUSES) == 4
        assert "inherited_from_canon" in ASSUMPTION_STATUSES

    def test_parameter_authority_levels(self):
        assert len(PARAMETER_AUTHORITY_LEVELS) == 5
        assert "inherited" in PARAMETER_AUTHORITY_LEVELS

    def test_sector_relevance_levels(self):
        assert len(SECTOR_RELEVANCE_LEVELS) == 5
        assert "directly_relevant" in SECTOR_RELEVANCE_LEVELS
        assert "absent" in SECTOR_RELEVANCE_LEVELS


# ===================================================================
# Problem definition tests
# ===================================================================

class TestProblemDefinition:
    def test_two_problems_defined(self, result):
        assert len(result.problem_definitions) == 2

    def test_dm_and_de_separated(self, result):
        names = [p.name for p in result.problem_definitions]
        assert "dark_matter" in names
        assert "dark_energy" in names

    def test_dm_sectors_mapped(self, result):
        dm = [p for p in result.problem_definitions if p.name == "dark_matter"][0]
        sectors = [s.sector for s in dm.relevant_grut_sectors]
        assert "macro_scalar_memory" in sectors
        assert "gravitational" in sectors

    def test_defect_absent_for_dm(self, result):
        dm = [p for p in result.problem_definitions if p.name == "dark_matter"][0]
        defect = [s for s in dm.relevant_grut_sectors if s.sector == "defect_triplet"][0]
        assert defect.relevance == "absent"

    def test_de_sectors_mapped(self, result):
        de = [p for p in result.problem_definitions if p.name == "dark_energy"][0]
        sectors = [s.sector for s in de.relevant_grut_sectors]
        assert "macro_scalar_memory" in sectors

    def test_shared_field_content(self, result):
        for p in result.problem_definitions:
            assert p.shared_field_content is True


# ===================================================================
# Dark matter analysis tests
# ===================================================================

class TestDarkMatterAnalysis:
    def test_dm_test_count(self, result):
        assert len(result.dark_matter_result.tests) >= 5

    def test_memory_gravitates(self, result):
        assert result.dark_matter_result.memory_gravitates_independently is True

    def test_memory_not_collisionless(self, result):
        assert result.dark_matter_result.memory_collisionless is False

    def test_memory_collision_not_demonstrated(self, result):
        assert result.dark_matter_result.memory_survives_cluster_collision is False

    def test_defect_not_relevant(self, result):
        assert result.dark_matter_result.defect_sector_relevant is False

    def test_scaling_does_not_match(self, result):
        assert result.dark_matter_result.scaling_matches_cdm is False

    def test_no_stable_phenomenology(self, result):
        assert result.dark_matter_result.has_stable_weak_field_phenomenology is False

    def test_dm_classification_valid(self, result):
        assert result.dark_matter_result.classification in DM_CLASSIFICATION_OPTIONS

    def test_dm_classification_value(self, result):
        assert result.dark_matter_result.classification == \
            "dark_matter_interpretation_partial_mimic"

    def test_dm_justification_nonempty(self, result):
        assert len(result.dark_matter_result.justification) > 50

    def test_all_interpretation_levels_valid(self, result):
        for t in result.dark_matter_result.tests:
            assert t.interpretation_level in INTERPRETATION_LEVELS

    def test_invalid_dm_interpretation_rejected(self):
        with pytest.raises(ValueError):
            DarkMatterTest(
                test_name="bad",
                question="bad",
                result="bad",
                viable=False,
                interpretation_level="INVALID",
                comment="bad",
            )


# ===================================================================
# Dark energy analysis tests
# ===================================================================

class TestDarkEnergyAnalysis:
    def test_de_test_count(self, result):
        assert len(result.dark_energy_result.tests) >= 4

    def test_produces_negative_pressure(self, result):
        assert result.dark_energy_result.produces_negative_pressure is True

    def test_w_minus_1_trivially(self, result):
        assert result.dark_energy_result.equation_of_state_w_minus_1 is True

    def test_vacuum_tension_not_derived(self, result):
        assert result.dark_energy_result.vacuum_tension_derived is False

    def test_cc_not_explained(self, result):
        assert result.dark_energy_result.cosmological_constant_explained is False

    def test_requires_extension(self, result):
        assert result.dark_energy_result.requires_cosmological_extension is True

    def test_de_classification_valid(self, result):
        assert result.dark_energy_result.classification in DE_CLASSIFICATION_OPTIONS

    def test_de_classification_value(self, result):
        assert result.dark_energy_result.classification == \
            "dark_energy_interpretation_reframes_but_does_not_solve"

    def test_de_justification_nonempty(self, result):
        assert len(result.dark_energy_result.justification) > 50

    def test_all_interpretation_levels_valid(self, result):
        for t in result.dark_energy_result.tests:
            assert t.interpretation_level in INTERPRETATION_LEVELS

    def test_invalid_de_interpretation_rejected(self):
        with pytest.raises(ValueError):
            DarkEnergyTest(
                test_name="bad",
                question="bad",
                result="bad",
                viable=False,
                interpretation_level="INVALID",
                comment="bad",
            )


# ===================================================================
# Minimal models tests
# ===================================================================

class TestMinimalModels:
    def test_two_models(self, result):
        assert len(result.minimal_models) == 2

    def test_dm_model_present(self, result):
        tracks = [m.track for m in result.minimal_models]
        assert "dark_matter" in tracks

    def test_de_model_present(self, result):
        tracks = [m.track for m in result.minimal_models]
        assert "dark_energy" in tracks

    def test_parameters_present(self, result):
        for m in result.minimal_models:
            assert len(m.parameters) >= 3

    def test_all_parameter_authorities_valid(self, result):
        for m in result.minimal_models:
            for p in m.parameters:
                assert p.authority in PARAMETER_AUTHORITY_LEVELS

    def test_interpretation_types(self, result):
        for m in result.minimal_models:
            assert m.interpretation_type in [
                "field_theoretic", "effective", "phenomenological"
            ]


# ===================================================================
# Comparison tests
# ===================================================================

class TestComparisons:
    def test_two_comparisons(self, result):
        assert len(result.comparisons) == 2

    def test_dm_comparison_present(self, result):
        tracks = [c.track for c in result.comparisons]
        assert "dark_matter" in tracks

    def test_de_comparison_present(self, result):
        tracks = [c.track for c in result.comparisons]
        assert "dark_energy" in tracks

    def test_three_scenarios_each(self, result):
        for c in result.comparisons:
            assert len(c.scenarios) == 3

    def test_all_scenario_types_valid(self, result):
        for c in result.comparisons:
            for s in c.scenarios:
                assert s.scenario in SCENARIO_TYPES

    def test_best_scenario_identified(self, result):
        for c in result.comparisons:
            assert len(c.best_scenario) > 0

    def test_extension_assessed(self, result):
        for c in result.comparisons:
            assert c.extra_extension_mild_or_substantial in ["mild", "substantial"]


# ===================================================================
# Classification tests
# ===================================================================

class TestClassification:
    def test_dm_valid(self, result):
        assert result.classification.dm_classification in DM_CLASSIFICATION_OPTIONS

    def test_de_valid(self, result):
        assert result.classification.de_classification in DE_CLASSIFICATION_OPTIONS

    def test_overall_valid(self, result):
        assert result.classification.overall_classification in APPENDIX_B_CLASSIFICATION_OPTIONS

    def test_dm_value(self, result):
        assert result.classification.dm_classification == \
            "dark_matter_interpretation_partial_mimic"

    def test_de_value(self, result):
        assert result.classification.de_classification == \
            "dark_energy_interpretation_reframes_but_does_not_solve"

    def test_overall_value(self, result):
        assert result.classification.overall_classification == "mixed_and_partial"

    def test_dm_justification_nonempty(self, result):
        assert len(result.classification.dm_justification) > 20

    def test_de_justification_nonempty(self, result):
        assert len(result.classification.de_justification) > 20

    def test_overall_justification_nonempty(self, result):
        assert len(result.classification.overall_justification) > 20

    def test_invalid_dm_classification_rejected(self):
        with pytest.raises(ValueError):
            AppendixBClassification(
                dm_classification="INVALID",
                de_classification=DE_CLASSIFICATION_OPTIONS[0],
                overall_classification=APPENDIX_B_CLASSIFICATION_OPTIONS[0],
                dm_justification="test",
                de_justification="test",
                overall_justification="test",
            )

    def test_invalid_de_classification_rejected(self):
        with pytest.raises(ValueError):
            AppendixBClassification(
                dm_classification=DM_CLASSIFICATION_OPTIONS[0],
                de_classification="INVALID",
                overall_classification=APPENDIX_B_CLASSIFICATION_OPTIONS[0],
                dm_justification="test",
                de_justification="test",
                overall_justification="test",
            )

    def test_deterministic(self, result):
        r2 = compute_dark_sector_result()
        assert r2.classification.dm_classification == \
            result.classification.dm_classification
        assert r2.classification.de_classification == \
            result.classification.de_classification
        assert r2.classification.overall_classification == \
            result.classification.overall_classification


# ===================================================================
# Assumptions tests
# ===================================================================

class TestAssumptions:
    def test_assumption_count(self, result):
        assert len(result.assumptions) >= 5

    def test_all_statuses_valid(self, result):
        for a in result.assumptions:
            assert a.status in ASSUMPTION_STATUSES

    def test_cosmological_extension_flagged(self, result):
        ext = [a for a in result.assumptions if a.status == "extension_assumption"]
        assert len(ext) >= 2

    def test_inherited_present(self, result):
        inh = [a for a in result.assumptions if a.status == "inherited_from_canon"]
        assert len(inh) >= 2


# ===================================================================
# Remaining gaps tests
# ===================================================================

class TestRemainingGaps:
    def test_gap_count(self, result):
        assert len(result.remaining_gaps) >= 3

    def test_has_critical(self, result):
        critical = [g for g in result.remaining_gaps if g.severity == "critical"]
        assert len(critical) >= 2

    def test_collisionless_gap_identified(self, result):
        texts = [g.gap.lower() for g in result.remaining_gaps]
        assert any("collisionless" in t for t in texts)

    def test_scaling_gap_identified(self, result):
        texts = [g.gap.lower() for g in result.remaining_gaps]
        assert any("a^-3" in t or "scaling" in t for t in texts)


# ===================================================================
# Nonclaims tests
# ===================================================================

class TestNonclaims:
    def test_nonclaim_count(self, result):
        assert len(result.nonclaims) >= 6

    def test_dm_not_is_dm(self, result):
        joined = " ".join(result.nonclaims).lower()
        assert "does not claim" in joined
        assert "dark matter" in joined

    def test_cc_not_solved(self, result):
        joined = " ".join(result.nonclaims).lower()
        assert "cosmological constant" in joined

    def test_bullet_cluster_not_reproduced(self, result):
        joined = " ".join(result.nonclaims).lower()
        assert "bullet cluster" in joined
        assert "reproduce" in joined or "reproduced" in joined


# ===================================================================
# Export tests
# ===================================================================

class TestExport:
    def test_to_dict_valid(self, result):
        d = appendix_b_result_to_dict(result)
        assert isinstance(d, dict)
        assert d["valid"] is True

    def test_to_dict_serializable(self, result):
        d = appendix_b_result_to_dict(result)
        s = json.dumps(d)
        assert len(s) > 100

    def test_json_roundtrip(self, result):
        s = appendix_b_result_to_json(result)
        d = json.loads(s)
        assert d["classification"]["dm_classification"] == \
            "dark_matter_interpretation_partial_mimic"
        assert d["classification"]["overall_classification"] == "mixed_and_partial"

    def test_all_sections_present(self, result):
        d = appendix_b_result_to_dict(result)
        assert "problem_definitions" in d
        assert "dark_matter_result" in d
        assert "dark_energy_result" in d
        assert "minimal_models" in d
        assert "comparisons" in d
        assert "classification" in d
        assert "assumptions" in d
        assert "remaining_gaps" in d
        assert "nonclaims" in d


# ===================================================================
# Top-level result tests
# ===================================================================

class TestAppendixBResult:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_components_present(self, result):
        assert result.problem_definitions is not None
        assert result.dark_matter_result is not None
        assert result.dark_energy_result is not None
        assert result.minimal_models is not None
        assert result.comparisons is not None
        assert result.classification is not None
        assert result.assumptions is not None
        assert result.remaining_gaps is not None
        assert result.nonclaims is not None

    def test_nonclaims_sufficient(self, result):
        assert len(result.nonclaims) >= 6

    def test_deterministic(self, result):
        r2 = compute_dark_sector_result()
        assert r2.valid == result.valid
        assert len(r2.nonclaims) == len(result.nonclaims)
        assert r2.classification.overall_classification == \
            result.classification.overall_classification


# ===================================================================
# Validation edge-case tests
# ===================================================================

class TestValidation:
    def test_invalid_sector_relevance(self):
        with pytest.raises(ValueError):
            SectorRelevance(sector="test", relevance="INVALID", reasoning="test")

    def test_invalid_assumption_status(self):
        with pytest.raises(ValueError):
            AssumptionEntry(
                assumption="test",
                status="INVALID",
                source="test",
                comment="test",
            )

    def test_invalid_parameter_authority(self):
        with pytest.raises(ValueError):
            ParameterEntry(
                name="test",
                value_or_form="test",
                authority="INVALID",
                source="test",
            )

    def test_invalid_scenario_type(self):
        with pytest.raises(ValueError):
            ScenarioComparison(
                scenario="INVALID",
                outcome="test",
                assumptions_needed=[],
                comment="test",
            )

    def test_invalid_dm_result_classification(self):
        with pytest.raises(ValueError):
            DarkMatterResult(
                tests=[],
                memory_gravitates_independently=True,
                memory_collisionless=False,
                memory_survives_cluster_collision=False,
                defect_sector_relevant=False,
                scaling_matches_cdm=False,
                has_stable_weak_field_phenomenology=False,
                classification="INVALID",
                justification="test",
                summary="test",
            )

    def test_invalid_de_result_classification(self):
        with pytest.raises(ValueError):
            DarkEnergyResult(
                tests=[],
                produces_negative_pressure=True,
                equation_of_state_w_minus_1=True,
                vacuum_tension_derived=False,
                cosmological_constant_explained=False,
                requires_cosmological_extension=True,
                classification="INVALID",
                justification="test",
                summary="test",
            )
