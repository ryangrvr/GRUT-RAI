"""Tests for Appendix R-A --- Matter Program Charter."""
import pytest
from grut.ra_matter_program_charter import (
    MATTER_PROGRAM_STAGES, N_STAGES,
    ALLOWED_SUCCESS_CRITERIA, ALLOWED_CHARTER_VERDICTS,
    APPENDIX_P_DISCIPLINE_RULE_IDS, N_APPENDIX_P_RULES,
    FORBIDDEN_FAILURE_MODE_IDS, FORBIDDEN_FAILURE_MODE_NAMES,
    N_FORBIDDEN_FAILURE_MODES, N_RA_NONCLAIMS, RA_NONCLAIMS,
    CHARTER_VERDICT, ALLOWED_APPENDIX_P_CLASSES,
    run_ra_matter_program_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ra_matter_program_charter()

class TestRAConstants:
    def test_n_stages(self):
        assert N_STAGES == 8
        assert len(MATTER_PROGRAM_STAGES) == N_STAGES
    def test_n_rules(self):
        assert N_APPENDIX_P_RULES == 8
    def test_n_ffms(self):
        assert N_FORBIDDEN_FAILURE_MODES == 8
    def test_n_nonclaims(self):
        assert len(RA_NONCLAIMS) == N_RA_NONCLAIMS
        for nc in RA_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdict(self):
        assert CHARTER_VERDICT == "matter_program_authorized_and_staged"
    def test_stages_start(self):
        assert "R0" in MATTER_PROGRAM_STAGES[0]
    def test_stages_end(self):
        assert "R-G" in MATTER_PROGRAM_STAGES[-1]

class TestObjective:
    def test_statement(self, result):
        assert len(result.objective.statement) > 50
    def test_not_in_scope(self, result):
        assert len(result.objective.what_is_not_in_scope) >= 5
    def test_preconditions_met(self, result):
        assert result.objective.preconditions_met is True
    def test_mentions_fermionic(self, result):
        text = " ".join(result.objective.what_is_not_in_scope).lower()
        assert "fermionic" in text

class TestStages:
    def test_count(self, result):
        assert len(result.stage_sequence) == N_STAGES
    def test_sequential(self, result):
        for i, s in enumerate(result.stage_sequence):
            assert s.stage_index == i
    def test_first_rb(self, result):
        assert "R-B" in result.stage_sequence[2].stage_id
    def test_last_rg(self, result):
        assert "R-G" in result.stage_sequence[-1].stage_id
    def test_re_fermionic(self, result):
        re = result.stage_sequence[5]
        assert "fermionic" in re.stage_name.lower()
    def test_all_have_question(self, result):
        for s in result.stage_sequence:
            assert len(s.primary_question) > 10
    def test_ids_unique(self, result):
        ids = [s.stage_id for s in result.stage_sequence]
        assert len(ids) == len(set(ids))

class TestRules:
    def test_count(self, result):
        assert len(result.appendix_p_rules) == N_APPENDIX_P_RULES
    def test_r8_classical(self, result):
        r8 = result.appendix_p_rules[7]
        assert "classical" in r8.rule_statement.lower() or "M/N/O" in r8.rule_statement
    def test_ids_unique(self, result):
        ids = [r.rule_id for r in result.appendix_p_rules]
        assert len(ids) == len(set(ids))

class TestFFMs:
    def test_count(self, result):
        assert len(result.forbidden_failure_modes) == N_FORBIDDEN_FAILURE_MODES
    def test_all_names(self, result):
        names = [f.name for f in result.forbidden_failure_modes]
        for expected in FORBIDDEN_FAILURE_MODE_NAMES:
            assert expected in names
    def test_ffm1_particle(self, result):
        assert result.forbidden_failure_modes[0].name == "particle_from_excitation_grammar"
    def test_ffm3_fermions(self, result):
        assert result.forbidden_failure_modes[2].name == "fermions_from_second_wave_quantum_by_default"
    def test_ffm4_born(self, result):
        assert result.forbidden_failure_modes[3].name == "born_rule_smuggled_into_matter"

class TestNonclaims:
    def test_count(self, result):
        assert result.entry_nonclaims.n_nonclaims == N_RA_NONCLAIMS
    def test_registered(self, result):
        assert result.entry_nonclaims.all_registered is True
    def test_mentions_fermionic(self, result):
        text = " ".join(result.entry_nonclaims.nonclaims).lower()
        assert "fermionic" in text

class TestVerdict:
    def test_verdict(self, result):
        assert result.charter_verdict == CHARTER_VERDICT
    def test_in_allowed(self, result):
        assert result.charter_verdict in ALLOWED_CHARTER_VERDICTS
    def test_r0_linked(self, result):
        assert result.r0_inventory_linked is True

class TestDiagnostics:
    def test_n_stages(self, result):
        assert result.diagnostics["n_stages"] == N_STAGES
    def test_first_substantive(self, result):
        assert result.diagnostics["first_substantive_stage"] == "R-B"
    def test_fermionic_stage(self, result):
        assert result.diagnostics["fermionic_boundary_stage"] == "R-E"

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_idempotency(self):
        r1 = run_ra_matter_program_charter()
        r2 = run_ra_matter_program_charter()
        assert r1.charter_verdict == r2.charter_verdict
    def test_self_test(self):
        assert _self_test() is True
