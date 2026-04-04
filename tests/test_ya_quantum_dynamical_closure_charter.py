"""Tests for Y-A --- Quantum-Dynamical Closure Charter."""
import pytest
from grut.ya_quantum_dynamical_closure_charter import (
    N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS, FFM_NAMES,
    N_YA_NONCLAIMS, YA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_ya_quantum_dynamical_closure_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ya_quantum_dynamical_closure_charter()

class TestStructure:
    def test_dist(self,result): assert len(result.distinctions)==N_DISTINCTIONS
    def test_stages(self,result): assert len(result.stage_sequence)==N_STAGES
    def test_ffms(self,result):
        names=[f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestVerdicts:
    def test_charter(self,result): assert result.charter_verdict==CHARTER_VERDICT
    def test_auth(self,result): assert result.authorization_verdict==AUTH_VERDICT
    def test_overall(self,result): assert result.overall_appendix_p==OVERALL_P

class TestDiag:
    def test_unit(self,result): assert result.diagnostics["unitarity_present"] is False
    def test_evol(self,result): assert result.diagnostics["evolution_law_present"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self): assert len(YA_NONCLAIMS)==N_YA_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
