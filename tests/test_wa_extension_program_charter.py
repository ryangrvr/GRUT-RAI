"""Tests for W-A --- Extension Program Charter."""
import pytest
from grut.wa_extension_program_charter import (
    STAGES, N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS,
    FFM_NAMES, N_WA_NONCLAIMS, WA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_wa_extension_program_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wa_extension_program_charter()

class TestConstants:
    def test_stages(self): assert N_STAGES==9
    def test_nc(self):
        assert len(WA_NONCLAIMS)==N_WA_NONCLAIMS
        for nc in WA_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestDistinctions:
    def test_count(self,result): assert len(result.distinctions)==N_DISTINCTIONS

class TestStages:
    def test_count(self,result): assert len(result.stage_sequence)==N_STAGES
    def test_sequential(self,result):
        for i,s in enumerate(result.stage_sequence): assert s.stage_index==i
    def test_wb(self,result): assert "W-B" in result.stage_sequence[2].stage_id

class TestFFMs:
    def test_count(self,result): assert len(result.ffms)==N_FFMS
    def test_names(self,result):
        names=[f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestVerdicts:
    def test_charter(self,result): assert result.charter_verdict==CHARTER_VERDICT
    def test_auth(self,result): assert result.authorization_verdict==AUTH_VERDICT
    def test_overall(self,result): assert result.overall_appendix_p==OVERALL_P

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_self_test(self): assert _self_test() is True
