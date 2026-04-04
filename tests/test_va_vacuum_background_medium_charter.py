"""Tests for V-A --- Vacuum, Background, and Medium Charter."""
import pytest
from grut.va_vacuum_background_medium_charter import (
    STAGES, N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS,
    FFM_NAMES, N_VA_NONCLAIMS, VA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_va_vacuum_background_medium_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_va_vacuum_background_medium_charter()

class TestConstants:
    def test_stages(self): assert N_STAGES==9
    def test_distinctions(self): assert N_DISTINCTIONS==12
    def test_nonclaims(self):
        assert len(VA_NONCLAIMS)==N_VA_NONCLAIMS
        for nc in VA_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestDistinctions:
    def test_count(self,result): assert len(result.distinctions)==N_DISTINCTIONS
    def test_d1_vacuum_medium(self,result):
        assert result.distinctions[0].left=="vacuum"
        assert result.distinctions[0].right=="medium"

class TestStages:
    def test_count(self,result): assert len(result.stage_sequence)==N_STAGES
    def test_sequential(self,result):
        for i,s in enumerate(result.stage_sequence): assert s.stage_index==i
    def test_vb(self,result): assert "V-B" in result.stage_sequence[2].stage_id
    def test_vh(self,result): assert "V-H" in result.stage_sequence[-1].stage_id

class TestFFMs:
    def test_count(self,result): assert len(result.ffms)==N_FFMS
    def test_all_names(self,result):
        names=[f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestVBLicensed:
    def test_count(self,result): assert len(result.vb_licensed.licensed_tests)>=3

class TestVerdicts:
    def test_charter(self,result): assert result.charter_verdict==CHARTER_VERDICT
    def test_auth(self,result): assert result.authorization_verdict==AUTH_VERDICT
    def test_overall(self,result): assert result.overall_appendix_p==OVERALL_P

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_idempotency(self):
        r1=run_va_vacuum_background_medium_charter()
        r2=run_va_vacuum_background_medium_charter()
        assert r1.charter_verdict==r2.charter_verdict
    def test_self_test(self): assert _self_test() is True
