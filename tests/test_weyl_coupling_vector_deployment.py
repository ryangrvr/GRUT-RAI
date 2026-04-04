"""
Tests for GRUT Phase D15 -- Non-Minimal Curvature Coupling and Weyl-Induced
Vector Deployment Test.

Verifies:
- All candidate actions are evaluated with valid structure
- Mode decomposition and effective mass analysis are present and valid
- Support-class continuity outputs are explicit
- Eta analysis outputs are explicit
- D14 vs D15 comparison is explicit
- Final D15 classification is reproducible from explicit criteria
- Nonclaims and remaining gaps are present
"""

from __future__ import annotations

import json
import pytest

from grut.weyl_coupling_vector_deployment import (
    # Vocabularies
    D15_CLASSIFICATION_OPTIONS,
    COUPLING_TYPES,
    ACTION_VERDICTS,
    INSTABILITY_LEVELS,
    GHOST_STATUSES,
    SUPPORT_CLASS_STRENGTHS,
    ETA_OUTCOMES,
    D14_VS_D15_UPGRADE_LEVELS,
    # Dataclasses
    NonMinimalActionCandidate,
    ModeEffectiveMassEntry,
    ModeDecompositionD15,
    SupportClassTest,
    SupportClassResult,
    EtaAnalysisEntry,
    EtaAnalysisResult,
    D14vsD15Entry,
    D14vsD15Comparison,
    FoundationalGap,
    D15Classification,
    D15Result,
    # Loophole statement
    D14_LOOPHOLE_STATEMENT,
    # Builders / analyzers
    build_nonminimal_candidates,
    analyze_mode_decomposition,
    analyze_curvature_deployment,
    analyze_support_class,
    analyze_eta,
    compare_d14_d15,
    classify_d15,
    identify_remaining_gaps,
    compute_weyl_coupling_result,
    # Serialization
    d15_result_to_dict,
    d15_result_to_json,
    # Nonclaims
    D15_NONCLAIMS,
)


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="module")
def d15_result() -> D15Result:
    """Compute D15 result once for all tests."""
    return compute_weyl_coupling_result()


# ===================================================================
# Vocabulary Tests
# ===================================================================

class TestVocabulary:
    def test_classification_options_nonempty(self):
        assert len(D15_CLASSIFICATION_OPTIONS) >= 3

    def test_coupling_types_nonempty(self):
        assert len(COUPLING_TYPES) >= 3

    def test_action_verdicts_nonempty(self):
        assert len(ACTION_VERDICTS) >= 3

    def test_instability_levels_nonempty(self):
        assert len(INSTABILITY_LEVELS) >= 3

    def test_ghost_statuses_nonempty(self):
        assert len(GHOST_STATUSES) >= 3

    def test_support_class_strengths_nonempty(self):
        assert len(SUPPORT_CLASS_STRENGTHS) >= 3

    def test_eta_outcomes_nonempty(self):
        assert len(ETA_OUTCOMES) >= 3

    def test_upgrade_levels_nonempty(self):
        assert len(D14_VS_D15_UPGRADE_LEVELS) >= 3

    def test_nonclaims_nonempty(self):
        assert len(D15_NONCLAIMS) >= 3


# ===================================================================
# Loophole Statement Tests
# ===================================================================

class TestLoophole:
    def test_loophole_statement_nonempty(self):
        assert len(D14_LOOPHOLE_STATEMENT.strip()) > 100

    def test_loophole_mentions_d14(self):
        assert "D14" in D14_LOOPHOLE_STATEMENT

    def test_loophole_mentions_weyl(self):
        assert "Weyl" in D14_LOOPHOLE_STATEMENT

    def test_loophole_mentions_mass_splitting(self):
        assert "mass" in D14_LOOPHOLE_STATEMENT.lower()


# ===================================================================
# Candidate Action Tests
# ===================================================================

class TestCandidateActions:
    def test_candidate_count(self, d15_result):
        assert len(d15_result.action_candidates) == 6

    def test_all_coupling_types_valid(self, d15_result):
        for c in d15_result.action_candidates:
            assert c.coupling_type in COUPLING_TYPES, f"{c.name}: invalid coupling_type"

    def test_all_verdicts_valid(self, d15_result):
        for c in d15_result.action_candidates:
            assert c.verdict in ACTION_VERDICTS, f"{c.name}: invalid verdict"

    def test_all_ghost_statuses_valid(self, d15_result):
        for c in d15_result.action_candidates:
            assert c.ghost_status in GHOST_STATUSES, f"{c.name}: invalid ghost_status"

    def test_all_have_inherited_content(self, d15_result):
        for c in d15_result.action_candidates:
            assert len(c.inherited_content) > 0, f"{c.name}: no inherited content"

    def test_all_have_new_content(self, d15_result):
        for c in d15_result.action_candidates:
            assert len(c.new_completion_content) > 0, f"{c.name}: no new content"

    def test_all_have_reasoning(self, d15_result):
        for c in d15_result.action_candidates:
            assert len(c.reasoning) > 20, f"{c.name}: reasoning too short"

    def test_weyl_quadratic_fails(self, d15_result):
        b1 = d15_result.action_candidates[0]
        assert "Weyl" in b1.name
        assert b1.verdict == "fails"

    def test_ricci_fails(self, d15_result):
        b2 = d15_result.action_candidates[1]
        assert "Ricci" in b2.name
        assert b2.verdict == "fails"

    def test_kretschner_fails(self, d15_result):
        b3 = d15_result.action_candidates[2]
        assert "Kretschner" in b3.name
        assert b3.verdict == "fails"

    def test_tidal_electric_fails(self, d15_result):
        b4 = d15_result.action_candidates[3]
        assert b4.verdict == "fails"

    def test_combined_nonFP_weyl_fails(self, d15_result):
        b5 = d15_result.action_candidates[4]
        assert b5.ghost_status == "ghost_present"
        assert b5.verdict == "fails"

    def test_gauss_bonnet_fails(self, d15_result):
        b6 = d15_result.action_candidates[5]
        assert "Gauss" in b6.name or "gauss_bonnet" in b6.coupling_type
        assert b6.verdict == "fails"

    def test_no_candidate_succeeds(self, d15_result):
        for c in d15_result.action_candidates:
            assert c.verdict != "derived", f"{c.name} should not derive"

    def test_has_weyl_coupling_type(self, d15_result):
        weyl_candidates = [c for c in d15_result.action_candidates if c.coupling_type == "weyl_tensor"]
        assert len(weyl_candidates) >= 2

    def test_invalid_verdict_rejected(self):
        with pytest.raises(ValueError):
            NonMinimalActionCandidate(
                name="test", coupling_type="weyl_tensor",
                action_term="test", inherited_content=[], new_completion_content=[],
                coupling_parameters=[], ghost_status="ghost_free",
                mode_modification="test", vector_sector_effect="test",
                verdict="INVALID", reasoning="test",
            )

    def test_invalid_coupling_type_rejected(self):
        with pytest.raises(ValueError):
            NonMinimalActionCandidate(
                name="test", coupling_type="INVALID",
                action_term="test", inherited_content=[], new_completion_content=[],
                coupling_parameters=[], ghost_status="ghost_free",
                mode_modification="test", vector_sector_effect="test",
                verdict="fails", reasoning="test",
            )

    def test_invalid_ghost_status_rejected(self):
        with pytest.raises(ValueError):
            NonMinimalActionCandidate(
                name="test", coupling_type="weyl_tensor",
                action_term="test", inherited_content=[], new_completion_content=[],
                coupling_parameters=[], ghost_status="INVALID",
                mode_modification="test", vector_sector_effect="test",
                verdict="fails", reasoning="test",
            )

    def test_deterministic(self):
        c1 = build_nonminimal_candidates()
        c2 = build_nonminimal_candidates()
        assert len(c1) == len(c2)
        for a, b in zip(c1, c2):
            assert a.name == b.name
            assert a.verdict == b.verdict


# ===================================================================
# Mode Decomposition Tests
# ===================================================================

class TestModeDecomposition:
    def test_three_mode_sectors(self, d15_result):
        assert len(d15_result.mode_decomposition.entries) == 3

    def test_mode_sectors(self, d15_result):
        sectors = {e.mode_sector for e in d15_result.mode_decomposition.entries}
        assert "scalar_trace" in sectors
        assert "vector_spin1" in sectors
        assert "tensor_spin2" in sectors

    def test_vector_exists(self, d15_result):
        assert d15_result.mode_decomposition.vector_exists is True

    def test_vector_curvature_sensitive(self, d15_result):
        assert d15_result.mode_decomposition.vector_curvature_sensitive is True

    def test_vector_not_unstable(self, d15_result):
        assert d15_result.mode_decomposition.vector_instability not in (
            "weakly_unstable", "strongly_unstable", "derivationally_decisive"
        )

    def test_all_instability_statuses_valid(self, d15_result):
        for e in d15_result.mode_decomposition.entries:
            assert e.instability_status in INSTABILITY_LEVELS, (
                f"{e.mode_sector}: invalid instability_status"
            )

    def test_summary_nonempty(self, d15_result):
        assert len(d15_result.mode_decomposition.summary) > 50

    def test_invalid_instability_rejected(self):
        with pytest.raises(ValueError):
            ModeEffectiveMassEntry(
                mode_sector="test", exists=True, curvature_sensitive=True,
                effective_mass_shift="test", instability_status="INVALID",
                triplet_relevance="test", verdict="test", analysis="test",
            )


# ===================================================================
# Curvature Deployment Tests
# ===================================================================

class TestCurvatureDeployment:
    def test_deployment_dict_keys(self, d15_result):
        candidates = d15_result.action_candidates
        mode_decomp = d15_result.mode_decomposition
        deployment = analyze_curvature_deployment(mode_decomp, candidates)
        assert "trigger_quantity" in deployment
        assert "sign_structure" in deployment
        assert "threshold_analysis" in deployment
        assert "vector_classification" in deployment
        assert "vector_deployed" in deployment
        assert "summary" in deployment

    def test_vector_not_deployed(self, d15_result):
        candidates = d15_result.action_candidates
        mode_decomp = d15_result.mode_decomposition
        deployment = analyze_curvature_deployment(mode_decomp, candidates)
        assert deployment["vector_deployed"] is False

    def test_trigger_mentions_weyl(self, d15_result):
        candidates = d15_result.action_candidates
        mode_decomp = d15_result.mode_decomposition
        deployment = analyze_curvature_deployment(mode_decomp, candidates)
        assert "Weyl" in deployment["trigger_quantity"] or "tidal" in deployment["trigger_quantity"]


# ===================================================================
# Support-Class Tests
# ===================================================================

class TestSupportClass:
    def test_tests_nonempty(self, d15_result):
        assert len(d15_result.support_class_result.tests) >= 3

    def test_overall_fails(self, d15_result):
        assert d15_result.support_class_result.overall_continuity is False

    def test_all_strengths_valid(self, d15_result):
        for t in d15_result.support_class_result.tests:
            assert t.strength in SUPPORT_CLASS_STRENGTHS, (
                f"{t.test}: invalid strength"
            )

    def test_summary_nonempty(self, d15_result):
        assert len(d15_result.support_class_result.summary) > 50

    def test_hedgehog_addressed(self, d15_result):
        hedgehog_tests = [
            t for t in d15_result.support_class_result.tests
            if "hedgehog" in t.test.lower() or "angular" in t.test.lower()
        ]
        assert len(hedgehog_tests) >= 1

    def test_invalid_strength_rejected(self):
        with pytest.raises(ValueError):
            SupportClassTest(
                test="test", result="test", strength="INVALID", comment="test",
            )


# ===================================================================
# Eta Analysis Tests
# ===================================================================

class TestEtaAnalysis:
    def test_entries_nonempty(self, d15_result):
        assert len(d15_result.eta_analysis.entries) >= 2

    def test_best_outcome_valid(self, d15_result):
        assert d15_result.eta_analysis.best_outcome in ETA_OUTCOMES

    def test_no_derivation(self, d15_result):
        for e in d15_result.eta_analysis.entries:
            assert e.eta_derived is False

    def test_all_outcomes_valid(self, d15_result):
        for e in d15_result.eta_analysis.entries:
            assert e.outcome in ETA_OUTCOMES, f"{e.mechanism}: invalid outcome"

    def test_summary_nonempty(self, d15_result):
        assert len(d15_result.eta_analysis.summary) > 30

    def test_invalid_outcome_rejected(self):
        with pytest.raises(ValueError):
            EtaAnalysisEntry(
                mechanism="test", eta_derived=False, eta_constrained=False,
                eta_matched_only=True, outcome="INVALID", comment="test",
            )


# ===================================================================
# D14 vs D15 Comparison Tests
# ===================================================================

class TestD14Comparison:
    def test_entries_nonempty(self, d15_result):
        assert len(d15_result.d14_comparison.entries) >= 4

    def test_overall_upgrade_valid(self, d15_result):
        assert d15_result.d14_comparison.overall_upgrade in D14_VS_D15_UPGRADE_LEVELS

    def test_overall_upgrade_value(self, d15_result):
        # D15 provides at most a conceptual upgrade
        assert d15_result.d14_comparison.overall_upgrade in (
            "no_upgrade", "conceptual_only"
        )

    def test_vector_criterion_present(self, d15_result):
        criteria = [e.criterion.lower() for e in d15_result.d14_comparison.entries]
        assert any("vector" in c for c in criteria)

    def test_ghost_criterion_present(self, d15_result):
        criteria = [e.criterion.lower() for e in d15_result.d14_comparison.entries]
        assert any("ghost" in c for c in criteria)

    def test_summary_nonempty(self, d15_result):
        assert len(d15_result.d14_comparison.summary) > 50

    def test_structural_understanding_upgraded(self, d15_result):
        struct = [
            e for e in d15_result.d14_comparison.entries
            if "structural" in e.criterion.lower()
        ]
        assert len(struct) >= 1
        assert struct[0].upgrade is True


# ===================================================================
# Classification Tests
# ===================================================================

class TestClassification:
    def test_classification_valid(self, d15_result):
        assert d15_result.classification.classification in D15_CLASSIFICATION_OPTIONS

    def test_classification_value(self, d15_result):
        assert d15_result.classification.classification == "nonminimal_curvature_route_fails"

    def test_vector_not_opened(self, d15_result):
        assert d15_result.classification.vector_channel_opened is False

    def test_instability_not_achieved(self, d15_result):
        assert d15_result.classification.instability_achieved is False

    def test_support_not_achieved(self, d15_result):
        assert d15_result.classification.support_class_continuity is False

    def test_eta_no_progress(self, d15_result):
        assert d15_result.classification.eta_progress is False

    def test_upgrade_over_d14(self, d15_result):
        assert d15_result.classification.upgrade_over_d14 in D14_VS_D15_UPGRADE_LEVELS

    def test_justification_nonempty(self, d15_result):
        assert len(d15_result.classification.justification) > 50

    def test_invalid_classification_rejected(self):
        with pytest.raises(ValueError):
            D15Classification(
                classification="INVALID",
                justification="test",
                vector_channel_opened=False,
                instability_achieved=False,
                support_class_continuity=False,
                eta_progress=False,
                upgrade_over_d14="no_upgrade",
            )

    def test_invalid_upgrade_rejected(self):
        with pytest.raises(ValueError):
            D15Classification(
                classification="nonminimal_curvature_route_fails",
                justification="test",
                vector_channel_opened=False,
                instability_achieved=False,
                support_class_continuity=False,
                eta_progress=False,
                upgrade_over_d14="INVALID",
            )

    def test_deterministic(self):
        r1 = compute_weyl_coupling_result()
        r2 = compute_weyl_coupling_result()
        assert r1.classification.classification == r2.classification.classification
        assert r1.classification.vector_channel_opened == r2.classification.vector_channel_opened
        assert r1.classification.instability_achieved == r2.classification.instability_achieved
        assert r1.classification.support_class_continuity == r2.classification.support_class_continuity
        assert r1.classification.eta_progress == r2.classification.eta_progress


# ===================================================================
# Remaining Gaps Tests
# ===================================================================

class TestRemainingGaps:
    def test_gaps_nonempty(self, d15_result):
        assert len(d15_result.remaining_gaps) >= 3

    def test_has_critical(self, d15_result):
        severities = [g.severity for g in d15_result.remaining_gaps]
        assert "critical" in severities

    def test_o3_still_extension(self, d15_result):
        o3_gaps = [g for g in d15_result.remaining_gaps if "O(3)" in g.gap]
        assert len(o3_gaps) >= 1

    def test_tensor_routes_exhausted(self, d15_result):
        tensor_gaps = [g for g in d15_result.remaining_gaps if "tensor" in g.gap.lower()]
        assert len(tensor_gaps) >= 1

    def test_eta_gap_present(self, d15_result):
        eta_gaps = [g for g in d15_result.remaining_gaps if "eta" in g.gap.lower()]
        assert len(eta_gaps) >= 1


# ===================================================================
# Export / Serialization Tests
# ===================================================================

class TestExport:
    def test_to_dict_valid(self, d15_result):
        d = d15_result_to_dict(d15_result)
        assert isinstance(d, dict)
        assert d["valid"] is True

    def test_to_dict_serializable(self, d15_result):
        d = d15_result_to_dict(d15_result)
        s = json.dumps(d)
        assert len(s) > 100

    def test_export_json(self, d15_result):
        s = d15_result_to_json(d15_result)
        parsed = json.loads(s)
        assert parsed["valid"] is True
        assert parsed["classification"]["classification"] == "nonminimal_curvature_route_fails"

    def test_all_sections_present(self, d15_result):
        d = d15_result_to_dict(d15_result)
        assert "action_candidates" in d
        assert "mode_decomposition" in d
        assert "support_class_result" in d
        assert "eta_analysis" in d
        assert "d14_comparison" in d
        assert "classification" in d
        assert "remaining_gaps" in d
        assert "nonclaims" in d


# ===================================================================
# D15Result Integrity Tests
# ===================================================================

class TestD15Result:
    def test_valid(self, d15_result):
        assert d15_result.valid is True

    def test_all_components_present(self, d15_result):
        assert d15_result.action_candidates is not None
        assert d15_result.mode_decomposition is not None
        assert d15_result.support_class_result is not None
        assert d15_result.eta_analysis is not None
        assert d15_result.d14_comparison is not None
        assert d15_result.classification is not None
        assert d15_result.remaining_gaps is not None
        assert d15_result.nonclaims is not None

    def test_nonclaims_nonempty(self, d15_result):
        assert len(d15_result.nonclaims) >= 5

    def test_deterministic(self):
        r1 = compute_weyl_coupling_result()
        r2 = compute_weyl_coupling_result()
        assert r1.valid == r2.valid
        assert len(r1.action_candidates) == len(r2.action_candidates)
        assert r1.classification.classification == r2.classification.classification
