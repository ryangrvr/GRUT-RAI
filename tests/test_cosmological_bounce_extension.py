"""Tests for grut.cosmological_bounce_extension (Appendix A).

Coverage:
- Vocabulary and constant validation
- Translation map construction and content
- Cosmological model specification
- Bounce / singularity-avoidance analysis
- Three-scenario comparison
- Classification logic
- Remaining gaps and nonclaims
- Export / serialization
- Determinism
"""

from __future__ import annotations

import json
import math

import pytest

from grut.cosmological_bounce_extension import (
    # Vocabularies
    APPENDIX_A_CLASSIFICATION_OPTIONS,
    TRANSLATION_QUALITY_LEVELS,
    SCENARIO_TYPES,
    BOUNCE_STATUSES,
    ASSUMPTION_ORIGINS,
    # Constants
    ALPHA_VAC,
    TAU_CANONICAL,
    LAMBDA_DEFAULT,
    ETA_TARGET,
    COMP_B_COEFF,
    # Dataclasses
    TranslationEntry,
    TranslationMap,
    CosmologicalAssumption,
    CosmologicalModel,
    BounceTest,
    BounceAnalysis,
    ScenarioResult,
    ComparisonResult,
    RemainingGap,
    AppendixAResult,
    # Builders
    build_translation_map,
    build_cosmological_model,
    analyze_bounce_criteria,
    build_comparison_scenarios,
    classify_cosmological_bounce,
    compute_cosmological_bounce_result,
)


# ===================================================================
# Vocabulary tests
# ===================================================================

class TestVocabulary:
    def test_classification_options(self):
        assert len(APPENDIX_A_CLASSIFICATION_OPTIONS) == 5
        assert "cosmological_bounce_derived_within_current_grut" in APPENDIX_A_CLASSIFICATION_OPTIONS
        assert "extension_attempt_failed" in APPENDIX_A_CLASSIFICATION_OPTIONS

    def test_translation_quality_levels(self):
        assert len(TRANSLATION_QUALITY_LEVELS) == 4
        assert "exact" in TRANSLATION_QUALITY_LEVELS
        assert "fails" in TRANSLATION_QUALITY_LEVELS

    def test_scenario_types(self):
        assert len(SCENARIO_TYPES) == 3
        assert "classical_baseline" in SCENARIO_TYPES

    def test_bounce_statuses(self):
        assert len(BOUNCE_STATUSES) == 4
        assert "full_bounce" in BOUNCE_STATUSES
        assert "singularity_persists" in BOUNCE_STATUSES

    def test_assumption_origins(self):
        assert len(ASSUMPTION_ORIGINS) == 3
        assert "current_canon" in ASSUMPTION_ORIGINS


class TestConstants:
    def test_alpha_vac(self):
        assert ALPHA_VAC == pytest.approx(1.0 / 3.0)

    def test_tau_canonical(self):
        assert TAU_CANONICAL == pytest.approx(math.sqrt(1.5))

    def test_lambda_default(self):
        assert LAMBDA_DEFAULT == pytest.approx(8.0 * math.pi)

    def test_eta_target(self):
        assert ETA_TARGET == pytest.approx(1.0 / math.sqrt(8.0 * math.pi))

    def test_comp_b_coeff(self):
        assert COMP_B_COEFF == pytest.approx(1.0 / (8.0 * math.pi))


# ===================================================================
# Translation map tests
# ===================================================================

class TestTranslationMap:
    @pytest.fixture
    def tmap(self):
        return build_translation_map()

    def test_entry_count(self, tmap):
        assert len(tmap.entries) == 6

    def test_all_qualities_valid(self, tmap):
        for e in tmap.entries:
            assert e.translation_quality in TRANSLATION_QUALITY_LEVELS

    def test_all_origins_valid(self, tmap):
        for e in tmap.entries:
            assert e.assumption_origin in ASSUMPTION_ORIGINS

    def test_overall_quality(self, tmap):
        assert tmap.overall_quality == "structurally_analogous_only"

    def test_component_b_fails(self, tmap):
        comp_b = [e for e in tmap.entries if "component_B" in e.strong_field_concept]
        assert len(comp_b) == 1
        assert comp_b[0].translation_quality == "fails"

    def test_memory_scalar_heuristic(self, tmap):
        mem = [e for e in tmap.entries if "component_A" in e.strong_field_concept]
        assert len(mem) == 1
        assert mem[0].translation_quality == "heuristic"

    def test_trigger_heuristic(self, tmap):
        trig = [e for e in tmap.entries if "trigger" in e.strong_field_concept]
        assert len(trig) == 1
        assert trig[0].translation_quality == "heuristic"

    def test_two_component_reduces(self, tmap):
        two = [e for e in tmap.entries if "two_component" in e.strong_field_concept]
        assert len(two) == 1
        assert two[0].translation_quality == "structurally_analogous_only"

    def test_summary_nonempty(self, tmap):
        assert len(tmap.summary) > 50

    def test_all_entries_have_reasoning(self, tmap):
        for e in tmap.entries:
            assert len(e.reasoning) > 20

    def test_invalid_quality_rejected(self):
        with pytest.raises(ValueError, match="Invalid translation quality"):
            TranslationEntry(
                strong_field_concept="test",
                cosmological_parallel="test",
                translation_quality="perfect",
                reasoning="test",
                assumption_origin="current_canon",
            )

    def test_invalid_origin_rejected(self):
        with pytest.raises(ValueError, match="Invalid assumption origin"):
            TranslationEntry(
                strong_field_concept="test",
                cosmological_parallel="test",
                translation_quality="exact",
                reasoning="test",
                assumption_origin="magic",
            )


# ===================================================================
# Cosmological model tests
# ===================================================================

class TestCosmologicalModel:
    @pytest.fixture
    def model(self):
        return build_cosmological_model()

    def test_background_geometry(self, model):
        assert "FRW" in model.background_geometry

    def test_dynamical_variables(self, model):
        assert len(model.dynamical_variables) == 3
        assert any("a(t)" in v for v in model.dynamical_variables)
        assert any("H(t)" in v for v in model.dynamical_variables)
        assert any("Phi(t)" in v for v in model.dynamical_variables)

    def test_curvature_scalars(self, model):
        assert len(model.curvature_scalars) >= 2

    def test_defect_absent(self, model):
        assert "ABSENT" in model.defect_sector_status.upper()

    def test_assumptions_nonempty(self, model):
        assert len(model.assumptions) >= 7

    def test_all_assumption_origins_valid(self, model):
        for a in model.assumptions:
            assert a.origin in ASSUMPTION_ORIGINS

    def test_inherited_nonempty(self, model):
        assert len(model.inherited_from_canon) >= 4

    def test_newly_introduced_nonempty(self, model):
        assert len(model.newly_introduced) >= 2

    def test_friedmann_equations(self, model):
        assert "H^2" in model.friedmann_equation_standard
        assert "rho_memory" in model.friedmann_equation_modified

    def test_memory_equation(self, model):
        assert "tau" in model.memory_equation
        assert "dPhi/dt" in model.memory_equation

    def test_effective_pressure(self, model):
        assert "SEC" in model.effective_pressure_contribution

    def test_summary_nonempty(self, model):
        assert len(model.summary) > 50

    def test_invalid_assumption_origin_rejected(self):
        with pytest.raises(ValueError, match="Invalid origin"):
            CosmologicalAssumption(
                assumption="test",
                origin="divine_revelation",
                notes="test",
            )


# ===================================================================
# Bounce analysis tests
# ===================================================================

class TestBounceAnalysis:
    @pytest.fixture
    def bounce(self):
        return analyze_bounce_criteria()

    def test_tests_nonempty(self, bounce):
        assert len(bounce.tests) >= 7

    def test_overall_status(self, bounce):
        assert bounce.overall_bounce_status == "singularity_softened"

    def test_sec_violation_possible(self, bounce):
        assert bounce.sec_violation_possible is True

    def test_sec_conditional_on_nonempty(self, bounce):
        assert len(bounce.sec_violation_conditional_on) >= 2

    def test_a_avoids_zero_conditional(self, bounce):
        assert bounce.a_avoids_zero == "conditional"

    def test_sign_structure_no(self, bounce):
        assert bounce.sign_structure_change == "no"

    def test_all_test_results_valid(self, bounce):
        valid_results = {"yes", "no", "conditional", "indeterminate"}
        for t in bounce.tests:
            assert t.result in valid_results, f"Invalid result: {t.result}"

    def test_relaxation_does_not_favor_bounce(self, bounce):
        relax = [t for t in bounce.tests if "relaxation" in t.test_name]
        assert len(relax) == 1
        assert relax[0].result == "no"

    def test_compact_object_comparison(self, bounce):
        comp = [t for t in bounce.tests if "compact_object" in t.test_name]
        assert len(comp) == 1
        assert comp[0].result == "no"

    def test_sign_structure_test(self, bounce):
        sign = [t for t in bounce.tests if "sign_structure" in t.test_name]
        assert len(sign) == 1
        assert sign[0].result == "no"

    def test_all_tests_have_reasoning(self, bounce):
        for t in bounce.tests:
            assert len(t.reasoning) > 30

    def test_summary_nonempty(self, bounce):
        assert len(bounce.summary) > 100

    def test_invalid_bounce_status_rejected(self):
        with pytest.raises(ValueError, match="Invalid bounce status"):
            BounceAnalysis(
                tests=[],
                sec_violation_possible=False,
                sec_violation_conditional_on=[],
                a_avoids_zero="no",
                H_remains_finite="no",
                curvature_remains_finite="no",
                effective_repulsion="no",
                sign_structure_change="no",
                overall_bounce_status="magic_bounce",
                summary="test",
            )


# ===================================================================
# Comparison scenario tests
# ===================================================================

class TestComparisonScenarios:
    @pytest.fixture
    def comparison(self):
        return build_comparison_scenarios()

    def test_three_scenarios(self, comparison):
        assert len(comparison.scenarios) == 3

    def test_scenario_types(self, comparison):
        types = {s.scenario_type for s in comparison.scenarios}
        assert types == set(SCENARIO_TYPES)

    def test_classical_singular(self, comparison):
        classical = [s for s in comparison.scenarios if s.scenario_type == "classical_baseline"]
        assert len(classical) == 1
        assert classical[0].singularity_outcome == "singularity_persists"
        assert classical[0].H_diverges is True
        assert classical[0].a_reaches_zero is True

    def test_memory_only_softened(self, comparison):
        mem = [s for s in comparison.scenarios if s.scenario_type == "grut_memory_only"]
        assert len(mem) == 1
        assert mem[0].singularity_outcome == "singularity_softened"

    def test_memory_trigger_softened(self, comparison):
        trig = [s for s in comparison.scenarios if s.scenario_type == "grut_memory_plus_trigger"]
        assert len(trig) == 1
        assert trig[0].singularity_outcome == "singularity_softened"

    def test_no_bounce_from_memory(self, comparison):
        assert comparison.bounce_depends_on_memory_alone is False

    def test_no_bounce_from_trigger(self, comparison):
        assert comparison.bounce_depends_on_trigger_extension is False

    def test_bounce_requires_extra(self, comparison):
        assert comparison.bounce_depends_on_extra_assumptions is True

    def test_no_scenario_bounces(self, comparison):
        for s in comparison.scenarios:
            assert s.singularity_outcome != "full_bounce"

    def test_no_sec_violation(self, comparison):
        for s in comparison.scenarios:
            assert s.sec_violated is False

    def test_classical_no_extra(self, comparison):
        classical = [s for s in comparison.scenarios if s.scenario_type == "classical_baseline"]
        assert classical[0].depends_on_extra_assumptions is False

    def test_all_outcomes_valid(self, comparison):
        for s in comparison.scenarios:
            assert s.singularity_outcome in BOUNCE_STATUSES

    def test_summary_nonempty(self, comparison):
        assert len(comparison.summary) > 100

    def test_invalid_scenario_rejected(self):
        with pytest.raises(ValueError, match="Invalid scenario type"):
            ScenarioResult(
                scenario_type="quantum_gravity",
                label="test",
                description="test",
                singularity_outcome="singularity_persists",
                H_diverges=True,
                a_reaches_zero=True,
                curvature_diverges=True,
                sec_violated=False,
                depends_on_extra_assumptions=False,
                extra_assumptions=[],
                summary="test",
            )


# ===================================================================
# Classification tests
# ===================================================================

class TestClassification:
    @pytest.fixture
    def result(self):
        return compute_cosmological_bounce_result()

    def test_classification_valid(self, result):
        assert result.classification in APPENDIX_A_CLASSIFICATION_OPTIONS

    def test_classification_value(self, result):
        assert result.classification == "singularity_softened_but_not_bounced"

    def test_justification_nonempty(self, result):
        assert len(result.justification) > 50

    def test_no_bounce_claimed(self, result):
        assert "derived_within" not in result.classification
        assert "strongly_suggested" not in result.classification

    def test_not_failed(self, result):
        assert result.classification != "extension_attempt_failed"

    def test_deterministic(self, result):
        r2 = compute_cosmological_bounce_result()
        assert result.classification == r2.classification
        assert result.justification == r2.justification

    def test_invalid_classification_rejected(self):
        with pytest.raises(ValueError, match="Invalid classification"):
            AppendixAResult(
                translation_map=build_translation_map(),
                cosmological_model=build_cosmological_model(),
                bounce_analysis=analyze_bounce_criteria(),
                comparison=build_comparison_scenarios(),
                classification="singularity_cured_by_magic",
                justification="test",
                remaining_gaps=[],
                nonclaims=[],
                upgrade_paths=[],
            )

    def test_classify_bounce_derived_if_bounce_present(self):
        """Verify that if a scenario achieves full bounce, classification upgrades."""
        translation = build_translation_map()
        bounce = analyze_bounce_criteria()
        comparison = build_comparison_scenarios()
        # Manually patch a scenario to have full_bounce
        comparison.scenarios[1] = ScenarioResult(
            scenario_type="grut_memory_only",
            label="test",
            description="test",
            singularity_outcome="full_bounce",
            H_diverges=False,
            a_reaches_zero=False,
            curvature_diverges=False,
            sec_violated=True,
            depends_on_extra_assumptions=False,
            extra_assumptions=[],
            summary="test",
        )
        cls, _ = classify_cosmological_bounce(translation, bounce, comparison)
        assert cls == "cosmological_bounce_derived_within_current_grut"

    def test_classify_suggested_if_bounce_with_extras(self):
        """If bounce achieved but with extra assumptions, classify as suggested."""
        translation = build_translation_map()
        bounce = analyze_bounce_criteria()
        comparison = build_comparison_scenarios()
        comparison.scenarios[2] = ScenarioResult(
            scenario_type="grut_memory_plus_trigger",
            label="test",
            description="test",
            singularity_outcome="full_bounce",
            H_diverges=False,
            a_reaches_zero=False,
            curvature_diverges=False,
            sec_violated=True,
            depends_on_extra_assumptions=True,
            extra_assumptions=["assumed V_eff"],
            summary="test",
        )
        cls, _ = classify_cosmological_bounce(translation, bounce, comparison)
        assert cls == "cosmological_bounce_strongly_suggested_by_extension"


# ===================================================================
# Remaining gaps and nonclaims tests
# ===================================================================

class TestGapsAndNonclaims:
    @pytest.fixture
    def result(self):
        return compute_cosmological_bounce_result()

    def test_gaps_nonempty(self, result):
        assert len(result.remaining_gaps) >= 4

    def test_has_critical_gaps(self, result):
        critical = [g for g in result.remaining_gaps if g.severity == "critical"]
        assert len(critical) >= 2

    def test_sec_gap_identified(self, result):
        sec_gaps = [g for g in result.remaining_gaps if "SEC" in g.gap]
        assert len(sec_gaps) >= 1

    def test_component_b_gap_identified(self, result):
        b_gaps = [g for g in result.remaining_gaps if "Component B" in g.gap]
        assert len(b_gaps) >= 1

    def test_nonclaims_nonempty(self, result):
        assert len(result.nonclaims) >= 6

    def test_nonclaims_not_claim_bounce(self, result):
        for nc in result.nonclaims:
            assert "NOT" in nc.upper() or "not" in nc

    def test_upgrade_paths_nonempty(self, result):
        assert len(result.upgrade_paths) >= 4


# ===================================================================
# Export / serialization tests
# ===================================================================

class TestExport:
    @pytest.fixture
    def result(self):
        return compute_cosmological_bounce_result()

    def test_to_dict_valid(self, result):
        d = result.to_dict()
        assert isinstance(d, dict)
        assert "classification" in d
        assert "translation_map" in d
        assert "bounce_analysis" in d
        assert "comparison" in d

    def test_to_dict_serializable(self, result):
        d = result.to_dict()
        s = json.dumps(d)
        assert len(s) > 100

    def test_export_json(self, result):
        j = result.to_json()
        parsed = json.loads(j)
        assert parsed["classification"] == "singularity_softened_but_not_bounced"

    def test_roundtrip(self, result):
        j = result.to_json()
        d = json.loads(j)
        assert d["bounce_analysis"]["overall_bounce_status"] == "singularity_softened"
        assert d["comparison"]["bounce_depends_on_memory_alone"] is False


# ===================================================================
# Full result tests
# ===================================================================

class TestFullResult:
    @pytest.fixture
    def result(self):
        return compute_cosmological_bounce_result()

    def test_all_components_present(self, result):
        assert result.translation_map is not None
        assert result.cosmological_model is not None
        assert result.bounce_analysis is not None
        assert result.comparison is not None
        assert result.classification is not None
        assert result.justification is not None

    def test_translation_quality(self, result):
        assert result.translation_map.overall_quality == "structurally_analogous_only"

    def test_bounce_status(self, result):
        assert result.bounce_analysis.overall_bounce_status == "singularity_softened"

    def test_no_scenario_bounces(self, result):
        for s in result.comparison.scenarios:
            assert s.singularity_outcome != "full_bounce"

    def test_classification_conservative(self, result):
        assert result.classification == "singularity_softened_but_not_bounced"

    def test_deterministic(self, result):
        r2 = compute_cosmological_bounce_result()
        assert result.to_json() == r2.to_json()
