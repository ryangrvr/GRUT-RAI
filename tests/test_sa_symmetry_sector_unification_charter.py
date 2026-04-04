"""Tests for Appendix S-A --- Symmetry and Sector-Unification Charter."""
import pytest
from grut.sa_symmetry_sector_unification_charter import (
    STAGES, N_STAGES, N_RULES, FFM_NAMES, N_FFMS,
    N_SA_NONCLAIMS, SA_NONCLAIMS, CHARTER_VERDICT,
    ALLOWED_CHARTER_VERDICTS,
    run_sa_symmetry_sector_unification_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_sa_symmetry_sector_unification_charter()

class TestConstants:
    def test_stages(self): assert N_STAGES==6; assert len(STAGES)==6
    def test_rules(self): assert N_RULES==7
    def test_ffms(self): assert N_FFMS==8; assert len(FFM_NAMES)==8
    def test_nonclaims(self):
        assert len(SA_NONCLAIMS)==N_SA_NONCLAIMS
        for nc in SA_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdict(self): assert CHARTER_VERDICT=="symmetry_program_authorized_and_staged"

class TestObjective:
    def test_statement(self, result): assert len(result.objective.statement)>50
    def test_not_in_scope(self, result): assert len(result.objective.not_in_scope)>=5
    def test_preconditions(self, result): assert result.objective.preconditions_met is True

class TestStages:
    def test_count(self, result): assert len(result.stage_sequence)==N_STAGES
    def test_sequential(self, result):
        for i,s in enumerate(result.stage_sequence): assert s.stage_index==i
    def test_sb_first_substantive(self, result):
        assert "S-B" in result.stage_sequence[2].stage_id
    def test_se_last(self, result):
        assert "S-E" in result.stage_sequence[-1].stage_id

class TestRules:
    def test_count(self, result): assert len(result.rules)==N_RULES
    def test_s_r7_extension(self, result):
        r7=result.rules[6]; assert "extension" in r7.statement.lower()

class TestFFMs:
    def test_count(self, result): assert len(result.ffms)==N_FFMS
    def test_all_names(self, result):
        names=[f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names
    def test_ffm1(self, result):
        assert result.ffms[0].name=="extension_sector_as_native_symmetry"

class TestVerdict:
    def test_verdict(self, result): assert result.charter_verdict==CHARTER_VERDICT
    def test_in_allowed(self, result): assert result.charter_verdict in ALLOWED_CHARTER_VERDICTS
    def test_s0_linked(self, result): assert result.s0_linked is True

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_idempotency(self):
        r1=run_sa_symmetry_sector_unification_charter()
        r2=run_sa_symmetry_sector_unification_charter()
        assert r1.charter_verdict==r2.charter_verdict
    def test_self_test(self): assert _self_test() is True
