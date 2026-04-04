"""
Tests for Appendix Q-II.A --- Second-Wave Quantum Charter
=========================================================
"""

import pytest

from grut.qiia_second_wave_quantum_charter import (
    SECOND_WAVE_STAGES, N_STAGES,
    ALLOWED_SUCCESS_CRITERIA, ALLOWED_CHARTER_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    APPENDIX_P_DISCIPLINE_RULE_IDS, N_APPENDIX_P_RULES,
    FORBIDDEN_FAILURE_MODE_IDS, FORBIDDEN_FAILURE_MODE_NAMES,
    N_FORBIDDEN_FAILURE_MODES,
    N_QIIA_NONCLAIMS, QIIA_NONCLAIMS,
    CHARTER_VERDICT,
    run_qiia_second_wave_charter, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiia_second_wave_charter()


# ===========================================================================
# TestQIIAConstants
# ===========================================================================

class TestQIIAConstants:
    def test_n_stages(self):
        assert N_STAGES == 8

    def test_stages_list_length(self):
        assert len(SECOND_WAVE_STAGES) == N_STAGES

    def test_n_appendix_p_rules(self):
        assert N_APPENDIX_P_RULES == 7

    def test_n_forbidden_failure_modes(self):
        assert N_FORBIDDEN_FAILURE_MODES == 8

    def test_n_nonclaims(self):
        assert N_QIIA_NONCLAIMS == 8

    def test_nonclaims_length(self):
        assert len(QIIA_NONCLAIMS) == N_QIIA_NONCLAIMS

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in QIIA_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_charter_verdict_string(self):
        assert CHARTER_VERDICT == "part_two_authorized_and_staged"

    def test_allowed_success_criteria_size(self):
        assert len(ALLOWED_SUCCESS_CRITERIA) == 4

    def test_allowed_charter_verdicts_size(self):
        assert len(ALLOWED_CHARTER_VERDICTS) == 2

    def test_ffm_ids_length(self):
        assert len(FORBIDDEN_FAILURE_MODE_IDS) == N_FORBIDDEN_FAILURE_MODES

    def test_ffm_names_length(self):
        assert len(FORBIDDEN_FAILURE_MODE_NAMES) == N_FORBIDDEN_FAILURE_MODES

    def test_rule_ids_length(self):
        assert len(APPENDIX_P_DISCIPLINE_RULE_IDS) == N_APPENDIX_P_RULES

    def test_stages_start_with_qii0(self):
        assert "Q-II.0" in SECOND_WAVE_STAGES[0]

    def test_stages_end_with_qiig(self):
        assert "Q-II.G" in SECOND_WAVE_STAGES[-1]


# ===========================================================================
# TestProgramObjective
# ===========================================================================

class TestProgramObjective:
    def test_statement_not_empty(self, result):
        assert len(result.objective.statement) > 50

    def test_scope_not_empty(self, result):
        assert len(result.objective.scope) > 30

    def test_not_in_scope_length(self, result):
        assert len(result.objective.what_is_not_in_scope) >= 5

    def test_not_in_scope_mentions_born_rule(self, result):
        text = " ".join(result.objective.what_is_not_in_scope).lower()
        assert "born" in text

    def test_not_in_scope_mentions_entanglement(self, result):
        text = " ".join(result.objective.what_is_not_in_scope).lower()
        assert "entanglement" in text

    def test_preconditions_length(self, result):
        assert len(result.objective.required_preconditions) >= 3

    def test_preconditions_met(self, result):
        assert result.objective.preconditions_met is True

    def test_preconditions_mention_qf(self, result):
        text = " ".join(result.objective.required_preconditions).lower()
        assert "q-f" in text or "first_wave" in text or "first wave" in text


# ===========================================================================
# TestStageSequence
# ===========================================================================

class TestStageSequence:
    def test_stage_count(self, result):
        assert len(result.stage_sequence) == N_STAGES

    def test_stage_indices_sequential(self, result):
        for i, stage in enumerate(result.stage_sequence):
            assert stage.stage_index == i

    def test_first_stage_is_qii0(self, result):
        assert "Q-II.0" in result.stage_sequence[0].stage_id

    def test_second_stage_is_qiia(self, result):
        assert "Q-II.A" in result.stage_sequence[1].stage_id

    def test_third_stage_is_qiib(self, result):
        assert "Q-II.B" in result.stage_sequence[2].stage_id

    def test_last_stage_is_qiig(self, result):
        assert "Q-II.G" in result.stage_sequence[-1].stage_id

    def test_all_stages_have_primary_question(self, result):
        for s in result.stage_sequence:
            assert len(s.primary_question) > 20

    def test_all_stages_have_success_criterion(self, result):
        for s in result.stage_sequence:
            assert s.success_criterion_type in ALLOWED_SUCCESS_CRITERIA

    def test_all_stages_have_appendix_p_expected(self, result):
        for s in result.stage_sequence:
            assert s.appendix_p_class_expected in ALLOWED_APPENDIX_P_CLASSES

    def test_qiib_depends_on_qiia(self, result):
        qiib = result.stage_sequence[2]
        assert any("Q-II.A" in d for d in qiib.depends_on)

    def test_qiic_depends_on_qiib(self, result):
        qiic = result.stage_sequence[3]
        assert any("Q-II.B" in d for d in qiic.depends_on)

    def test_qiig_depends_on_multiple(self, result):
        qiig = result.stage_sequence[-1]
        assert len(qiig.depends_on) >= 3

    def test_stage_ids_unique(self, result):
        ids = [s.stage_id for s in result.stage_sequence]
        assert len(ids) == len(set(ids))

    def test_no_native_canon_expected(self, result):
        for s in result.stage_sequence:
            assert s.appendix_p_class_expected != "native_canon"


# ===========================================================================
# TestSuccessCriteria
# ===========================================================================

class TestSuccessCriteria:
    def test_success_described(self, result):
        assert len(result.success_criteria.success_description) > 30

    def test_partial_described(self, result):
        assert len(result.success_criteria.partial_success_description) > 30

    def test_bounded_negative_described(self, result):
        assert len(result.success_criteria.bounded_negative_description) > 30

    def test_extension_level_described(self, result):
        assert len(result.success_criteria.extension_level_description) > 30

    def test_bounded_negative_is_valid_outcome(self, result):
        text = result.success_criteria.bounded_negative_description.lower()
        assert "valid" in text or "valuable" in text


# ===========================================================================
# TestAppendixPRules
# ===========================================================================

class TestAppendixPRules:
    def test_rule_count(self, result):
        assert len(result.appendix_p_rules) == N_APPENDIX_P_RULES

    def test_r1_classification_completeness(self, result):
        r1 = result.appendix_p_rules[0]
        assert r1.rule_id == "QII-R1"
        assert "explicit" in r1.rule_statement.lower()

    def test_r2_nativity_discipline(self, result):
        r2 = result.appendix_p_rules[1]
        assert r2.rule_id == "QII-R2"
        assert "native_canon" in r2.rule_statement.lower()

    def test_r3_dof_accounting(self, result):
        r3 = result.appendix_p_rules[2]
        assert r3.rule_id == "QII-R3"
        assert "MIP" in r3.rule_statement or "new field" in r3.rule_statement.lower()

    def test_r7_first_wave_immutability(self, result):
        r7 = result.appendix_p_rules[6]
        assert r7.rule_id == "QII-R7"
        assert "locked" in r7.rule_statement.lower() or "LOCKED" in r7.rule_statement

    def test_all_rules_have_violation(self, result):
        for r in result.appendix_p_rules:
            assert len(r.violation_would_be) > 5

    def test_all_rules_have_tests_for(self, result):
        for r in result.appendix_p_rules:
            assert len(r.tests_for) > 3

    def test_rule_ids_unique(self, result):
        ids = [r.rule_id for r in result.appendix_p_rules]
        assert len(ids) == len(set(ids))


# ===========================================================================
# TestForbiddenFailureModes
# ===========================================================================

class TestForbiddenFailureModes:
    def test_ffm_count(self, result):
        assert len(result.forbidden_failure_modes) == N_FORBIDDEN_FAILURE_MODES

    def test_ffm1_entanglement_from_decoherence(self, result):
        ffm1 = result.forbidden_failure_modes[0]
        assert ffm1.name == "entanglement_from_decoherence"

    def test_ffm2_tensor_from_notation(self, result):
        ffm2 = result.forbidden_failure_modes[1]
        assert ffm2.name == "tensor_product_from_notation"

    def test_ffm3_many_body_from_toys(self, result):
        ffm3 = result.forbidden_failure_modes[2]
        assert ffm3.name == "many_body_from_two_state_toys"

    def test_ffm4_born_from_pointer(self, result):
        ffm4 = result.forbidden_failure_modes[3]
        assert ffm4.name == "born_rule_from_pointer_basis"

    def test_ffm5_matter_from_interference(self, result):
        ffm5 = result.forbidden_failure_modes[4]
        assert ffm5.name == "matter_readiness_from_interference_only"

    def test_ffm6_algebra_from_single(self, result):
        ffm6 = result.forbidden_failure_modes[5]
        assert ffm6.name == "operator_algebra_from_single_observable_success"

    def test_ffm7_statistics_without_structure(self, result):
        ffm7 = result.forbidden_failure_modes[6]
        assert ffm7.name == "statistics_closure_without_new_structure"

    def test_ffm8_extension_as_native(self, result):
        ffm8 = result.forbidden_failure_modes[7]
        assert ffm8.name == "extension_level_success_as_native_quantum_canon"

    def test_all_ffms_have_why_forbidden(self, result):
        for ffm in result.forbidden_failure_modes:
            assert len(ffm.why_forbidden) > 20

    def test_all_ffms_have_related_appendix(self, result):
        for ffm in result.forbidden_failure_modes:
            assert len(ffm.related_appendix) > 5

    def test_ffm_names_match_expected(self, result):
        names = [ffm.name for ffm in result.forbidden_failure_modes]
        for expected in FORBIDDEN_FAILURE_MODE_NAMES:
            assert expected in names

    def test_ffm_ids_unique(self, result):
        ids = [ffm.mode_id for ffm in result.forbidden_failure_modes]
        assert len(ids) == len(set(ids))


# ===========================================================================
# TestEntryNonclaims
# ===========================================================================

class TestEntryNonclaims:
    def test_nonclaims_count(self, result):
        assert result.entry_nonclaims.n_nonclaims == N_QIIA_NONCLAIMS

    def test_nonclaims_list_length(self, result):
        assert len(result.entry_nonclaims.nonclaims) == N_QIIA_NONCLAIMS

    def test_all_registered(self, result):
        assert result.entry_nonclaims.all_registered is True

    def test_all_start_with_not_claiming(self, result):
        for nc in result.entry_nonclaims.nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_mentions_part_ii(self, result):
        text = " ".join(result.entry_nonclaims.nonclaims).lower()
        assert "part_ii" in text or "part ii" in text or "part_two" in text

    def test_mentions_born_rule(self, result):
        text = " ".join(result.entry_nonclaims.nonclaims).lower()
        assert "born" in text


# ===========================================================================
# TestCharterVerdict
# ===========================================================================

class TestCharterVerdict:
    def test_verdict(self, result):
        assert result.charter_verdict == CHARTER_VERDICT

    def test_verdict_in_allowed(self, result):
        assert result.charter_verdict in ALLOWED_CHARTER_VERDICTS

    def test_qii0_linked(self, result):
        assert result.qii0_inventory_linked is True


# ===========================================================================
# TestDiagnostics
# ===========================================================================

class TestDiagnostics:
    def test_n_stages(self, result):
        assert result.diagnostics["n_stages"] == N_STAGES

    def test_n_rules(self, result):
        assert result.diagnostics["n_appendix_p_rules"] == N_APPENDIX_P_RULES

    def test_n_ffms(self, result):
        assert result.diagnostics["n_forbidden_failure_modes"] == N_FORBIDDEN_FAILURE_MODES

    def test_n_nonclaims(self, result):
        assert result.diagnostics["n_nonclaims"] == N_QIIA_NONCLAIMS

    def test_preconditions_met(self, result):
        assert result.diagnostics["preconditions_met"] is True

    def test_first_substantive_stage(self, result):
        assert result.diagnostics["first_substantive_stage"] == "Q-II.B"


# ===========================================================================
# TestMasterAudit
# ===========================================================================

class TestMasterAudit:
    def test_valid_true(self, result):
        assert result.valid is True

    def test_idempotency(self):
        r1 = run_qiia_second_wave_charter()
        r2 = run_qiia_second_wave_charter()
        assert r1.valid == r2.valid
        assert r1.charter_verdict == r2.charter_verdict

    def test_self_test(self):
        assert _self_test() is True
