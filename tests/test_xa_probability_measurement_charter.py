"""Tests for X-A --- Probability/Measurement Charter."""
import pytest
from grut.xa_probability_measurement_charter import (
    N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS, FFM_NAMES,
    N_XA_NONCLAIMS, XA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_xa_probability_measurement_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_xa_probability_measurement_charter()

class TestConstants:
    def test_nc(self):
        assert len(XA_NONCLAIMS)==N_XA_NONCLAIMS
        for nc in XA_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestStructure:
    def test_dist(self,result): assert len(result.distinctions)==N_DISTINCTIONS
    def test_stages(self,result): assert len(result.stage_sequence)==N_STAGES
    def test_seq(self,result):
        for i,s in enumerate(result.stage_sequence): assert s.stage_index==i
    def test_ffms(self,result):
        names=[f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestVerdicts:
    def test_charter(self,result): assert result.charter_verdict==CHARTER_VERDICT
    def test_auth(self,result): assert result.authorization_verdict==AUTH_VERDICT
    def test_overall(self,result): assert result.overall_appendix_p==OVERALL_P

class TestDiag:
    def test_born(self,result): assert result.diagnostics["born_present"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_self_test(self): assert _self_test() is True
