"""Tests for X-E --- Final Probability Ledger."""
import pytest
from grut.xe_final_probability_ledger import (
    N_LEDGER, N_GAPS, N_XE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN, ALLOWED_CLS,
    XE_PROB, XE_COMP, XE_UNIT, XE_FUT, XE_AUTH, XE_OVERALL,
    PROB_OPTIONS, COMP_OPTIONS, UNIT_OPTIONS, FUT_OPTIONS, AUTH_OPTIONS,
    XE_NONCLAIMS, run_xe_final_probability_ledger, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_xe_final_probability_ledger()

class TestLedger:
    def test_count(self,result): assert len(result.ledger)==N_LEDGER
    def test_valid(self,result):
        for i in result.ledger: assert i.classification in ALLOWED_CLS
    def test_established(self,result):
        n=sum(1 for i in result.ledger if i.classification=="extension_established")
        assert n>=3

class TestGaps:
    def test_count(self,result): assert len(result.gaps)==N_GAPS
    def test_seq(self,result):
        for i,g in enumerate(result.gaps): assert g.rank==i+1

class TestHardGated:
    def test_all(self,result):
        assert result.probability_layer_status in PROB_OPTIONS
        assert result.completion_status in COMP_OPTIONS
        assert result.unitarity_boundary_status in UNIT_OPTIONS
        assert result.future_boundary_status in FUT_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.probability_layer_status,result.completion_status,
           result.unitarity_boundary_status,result.future_boundary_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_axioms(self,result): assert result.diagnostics["total_axioms"]==3
    def test_dof(self,result): assert result.diagnostics["total_new_dof"]==0
    def test_op(self,result): assert result.diagnostics["operationally_sufficient"] is True
    def test_qm(self,result): assert result.diagnostics["full_qm"] is False
    def test_unit(self,result): assert result.diagnostics["unitarity_present"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self):
        assert len(XE_NONCLAIMS)==N_XE_NONCLAIMS
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
