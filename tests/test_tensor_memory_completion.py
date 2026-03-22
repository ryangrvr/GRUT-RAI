"""
Tests for grut.tensor_memory_completion
========================================

Phase D14: Tensor Memory Completion and Defect-Sector Derivation Test

Verifies:
- All candidate completions are evaluated
- Mode decomposition outputs are present and valid
- Instability logic is deterministic
- Eta-analysis outputs are explicit
- Support-class tests are complete
- Final D14 classification is reproducible from explicit criteria
"""

import json
import os
import tempfile

import pytest

from grut.tensor_memory_completion import (
    ACTION_VERDICTS,
    D14_CLASSIFICATION_OPTIONS,
    ETA_OUTCOMES,
    INSTABILITY_LEVELS,
    NONCLAIMS,
    SUPPORT_CLASS_STRENGTHS,
    D14Classification,
    D14Result,
    EtaAnalysisEntry,
    ModeAnalysisEntry,
    SupportClassTest,
    TensorActionCandidate,
    analyze_eta_prediction,
    analyze_mode_decomposition,
    build_action_candidates,
    classify_d14,
    compute_tensor_memory_completion,
    d14_result_to_dict,
    export_d14_result_json,
    identify_remaining_gaps,
    test_support_class_continuity,
)


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="module")
def d14_result():
    return compute_tensor_memory_completion()


@pytest.fixture(scope="module")
def candidates(d14_result):
    return d14_result.action_candidates


@pytest.fixture(scope="module")
def modes(d14_result):
    return d14_result.mode_decomposition


@pytest.fixture(scope="module")
def support(d14_result):
    return d14_result.support_class_result


@pytest.fixture(scope="module")
def eta(d14_result):
    return d14_result.eta_analysis


@pytest.fixture(scope="module")
def classification(d14_result):
    return d14_result.classification


@pytest.fixture(scope="module")
def gaps(d14_result):
    return d14_result.remaining_gaps


# ===================================================================
# Class: TestVocabulary
# ===================================================================

class TestVocabulary:
    """Test vocabulary constants."""

    def test_classification_options(self):
        assert len(D14_CLASSIFICATION_OPTIONS) == 5

    def test_action_verdicts(self):
        assert len(ACTION_VERDICTS) == 5

    def test_instability_levels(self):
        assert len(INSTABILITY_LEVELS) == 4

    def test_support_class_strengths(self):
        assert len(SUPPORT_CLASS_STRENGTHS) == 4

    def test_eta_outcomes(self):
        assert len(ETA_OUTCOMES) == 5

    def test_nonclaims(self):
        assert len(NONCLAIMS) >= 5


# ===================================================================
# Class: TestActionCandidates
# ===================================================================

class TestActionCandidates:
    """Test tensor-memory action candidates."""

    def test_candidate_count(self, candidates):
        assert len(candidates) == 5

    def test_all_verdicts_valid(self, candidates):
        for c in candidates:
            assert c.verdict in ACTION_VERDICTS, (
                f"Candidate '{c.name}' has invalid verdict '{c.verdict}'"
            )

    def test_all_have_inherited_content(self, candidates):
        for c in candidates:
            assert len(c.inherited_content) >= 1

    def test_all_have_new_content(self, candidates):
        for c in candidates:
            assert len(c.new_completion_content) >= 1

    def test_all_have_reasoning(self, candidates):
        for c in candidates:
            assert len(c.reasoning) > 50

    def test_fierz_pauli_fails(self, candidates):
        fp = next(c for c in candidates if "Fierz-Pauli" in c.name and "Non" not in c.name)
        assert fp.verdict == "fails"

    def test_non_fp_fails(self, candidates):
        nfp = next(c for c in candidates if "Non-Fierz-Pauli" in c.name)
        assert nfp.verdict == "fails"

    def test_proca_partially_motivated(self, candidates):
        proca = next(c for c in candidates if "Proca" in c.name)
        assert proca.verdict == "partially_motivated"

    def test_constrained_fails(self, candidates):
        constrained = next(c for c in candidates if "Constrained" in c.name)
        assert constrained.verdict == "fails"

    def test_relaxation_fails(self, candidates):
        relax = next(c for c in candidates if "relaxation" in c.name.lower())
        assert relax.verdict == "fails"

    def test_no_candidate_derives(self, candidates):
        for c in candidates:
            assert c.verdict != "derived"

    def test_invalid_verdict_rejected(self):
        with pytest.raises(ValueError, match="Invalid verdict"):
            TensorActionCandidate(
                name="test", field_content="", symmetry_class="",
                kinetic_structure="", potential_structure="",
                curvature_coupling="", scalar_coupling="",
                inherited_content=[], new_completion_content=[],
                mode_structure="", new_parameters=[],
                verdict="INVALID", reasoning="test",
            )

    def test_deterministic(self):
        c1 = build_action_candidates()
        c2 = build_action_candidates()
        assert len(c1) == len(c2)
        for a, b in zip(c1, c2):
            assert a.name == b.name
            assert a.verdict == b.verdict


# ===================================================================
# Class: TestModeDecomposition
# ===================================================================

class TestModeDecomposition:
    """Test mode decomposition analysis."""

    def test_three_modes(self, modes):
        assert len(modes.entries) == 3

    def test_mode_sectors(self, modes):
        sectors = {e.mode_sector for e in modes.entries}
        assert sectors == {"scalar_trace", "vector_spin1", "tensor_spin2"}

    def test_spin1_exists(self, modes):
        assert modes.spin1_exists is True

    def test_spin1_not_unstable(self, modes):
        assert modes.spin1_instability == "absent"

    def test_all_instability_statuses_valid(self, modes):
        for e in modes.entries:
            assert e.instability_status in INSTABILITY_LEVELS

    def test_scalar_trace_exists(self, modes):
        scalar = next(e for e in modes.entries if e.mode_sector == "scalar_trace")
        assert scalar.exists is True
        assert scalar.dof_count == 1

    def test_spin2_exists(self, modes):
        tensor = next(e for e in modes.entries if e.mode_sector == "tensor_spin2")
        assert tensor.exists is True
        assert tensor.dof_count == 5

    def test_spin1_dof_count(self, modes):
        spin1 = next(e for e in modes.entries if e.mode_sector == "vector_spin1")
        assert spin1.dof_count == 3

    def test_summary_nonempty(self, modes):
        assert len(modes.summary) > 50

    def test_invalid_instability_rejected(self):
        with pytest.raises(ValueError, match="Invalid instability status"):
            ModeAnalysisEntry(
                mode_sector="test", exists=True, dof_count=1,
                curvature_sensitive=False, instability_status="INVALID",
                triplet_relevance="", verdict="", analysis="",
            )


# ===================================================================
# Class: TestSupportClass
# ===================================================================

class TestSupportClass:
    """Test support-class continuity."""

    def test_tests_nonempty(self, support):
        assert len(support.tests) >= 4

    def test_overall_fails(self, support):
        assert support.overall_continuity is False

    def test_all_strengths_valid(self, support):
        for t in support.tests:
            assert t.strength in SUPPORT_CLASS_STRENGTHS

    def test_summary_nonempty(self, support):
        assert len(support.summary) > 50

    def test_angular_gradient_addressed(self, support):
        texts = " ".join(t.result for t in support.tests).lower()
        assert "angular" in texts

    def test_invalid_strength_rejected(self):
        with pytest.raises(ValueError, match="Invalid strength"):
            SupportClassTest(
                test="test", result="test",
                strength="INVALID", comment="test",
            )


# ===================================================================
# Class: TestEtaAnalysis
# ===================================================================

class TestEtaAnalysis:
    """Test eta prediction analysis."""

    def test_entries_nonempty(self, eta):
        assert len(eta.entries) >= 5

    def test_best_outcome_valid(self, eta):
        assert eta.best_outcome in ETA_OUTCOMES

    def test_best_outcome_value(self, eta):
        assert eta.best_outcome == "related_to_parameters"

    def test_no_derivation(self, eta):
        for e in eta.entries:
            assert not e.eta_derived

    def test_all_outcomes_valid(self, eta):
        for e in eta.entries:
            assert e.outcome in ETA_OUTCOMES

    def test_summary_nonempty(self, eta):
        assert len(eta.summary) > 50

    def test_invalid_outcome_rejected(self):
        with pytest.raises(ValueError, match="Invalid eta outcome"):
            EtaAnalysisEntry(
                mechanism="test", eta_derived=False,
                eta_constrained=False, eta_matched_only=False,
                outcome="INVALID", comment="test",
            )


# ===================================================================
# Class: TestClassification
# ===================================================================

class TestClassification:
    """Test D14 classification."""

    def test_classification_valid(self, classification):
        assert classification.classification in D14_CLASSIFICATION_OPTIONS

    def test_classification_value(self, classification):
        assert classification.classification == "tensor_memory_completion_fails_to_upgrade_D13"

    def test_no_upgrade(self, classification):
        assert classification.upgrade_over_d13 is False

    def test_spin1_not_achieved(self, classification):
        assert classification.spin1_instability_achieved is False

    def test_support_not_achieved(self, classification):
        assert classification.support_class_continuity is False

    def test_eta_no_progress(self, classification):
        assert classification.eta_progress is False

    def test_justification_nonempty(self, classification):
        assert len(classification.justification) > 50

    def test_deterministic(self):
        r1 = compute_tensor_memory_completion()
        r2 = compute_tensor_memory_completion()
        assert r1.classification.classification == r2.classification.classification
        assert r1.classification.upgrade_over_d13 == r2.classification.upgrade_over_d13

    def test_invalid_classification_rejected(self):
        with pytest.raises(ValueError, match="Invalid D14 classification"):
            D14Classification(
                classification="INVALID",
                justification="test",
                spin1_instability_achieved=False,
                support_class_continuity=False,
                eta_progress=False,
                upgrade_over_d13=False,
            )


# ===================================================================
# Class: TestRemainingGaps
# ===================================================================

class TestRemainingGaps:
    """Test remaining gaps."""

    def test_gaps_nonempty(self, gaps):
        assert len(gaps) >= 4

    def test_has_critical(self, gaps):
        critical = [g for g in gaps if g.severity == "critical"]
        assert len(critical) >= 2

    def test_ssb_obstruction_identified(self, gaps):
        texts = " ".join(g.gap + " " + g.notes for g in gaps).lower()
        assert "ssb" in texts or "variational" in texts

    def test_o3_still_extension(self, gaps):
        o3 = next(g for g in gaps if "O(3)" in g.gap or "principled" in g.gap)
        assert o3.severity == "critical"


# ===================================================================
# Class: TestExport
# ===================================================================

class TestExport:
    """Test export functionality."""

    def test_to_dict_valid(self, d14_result):
        d = d14_result_to_dict(d14_result)
        assert isinstance(d, dict)
        assert d["valid"] is True

    def test_to_dict_serializable(self, d14_result):
        d = d14_result_to_dict(d14_result)
        s = json.dumps(d, default=str)
        assert len(s) > 1000

    def test_export_json(self, d14_result):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            export_d14_result_json(d14_result, path)
            with open(path) as f:
                data = json.load(f)
            assert data["valid"] is True
            assert len(data["action_candidates"]) == 5
        finally:
            os.unlink(path)


# ===================================================================
# Class: TestD14Result
# ===================================================================

class TestD14Result:
    """Test top-level D14 result."""

    def test_valid(self, d14_result):
        assert d14_result.valid is True

    def test_all_components(self, d14_result):
        assert d14_result.action_candidates is not None
        assert d14_result.mode_decomposition is not None
        assert d14_result.support_class_result is not None
        assert d14_result.eta_analysis is not None
        assert d14_result.classification is not None
        assert d14_result.remaining_gaps is not None
        assert d14_result.nonclaims is not None

    def test_nonclaims_nonempty(self, d14_result):
        assert len(d14_result.nonclaims) >= 5

    def test_deterministic(self):
        r1 = compute_tensor_memory_completion()
        r2 = compute_tensor_memory_completion()
        assert r1.classification.classification == r2.classification.classification
