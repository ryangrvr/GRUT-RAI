"""Tests for Y-E --- Final Quantum-Dynamical Ledger."""
import pytest
from grut.ye_final_quantum_dynamical_ledger import (
    N_LEDGER, N_GAPS, N_YE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN, ALLOWED_CLS,
    YE_QD, YE_IF, YE_COMP, YE_FUT, YE_AUTH, YE_OVERALL,
    QD_OPTIONS, IF_OPTIONS, COMP_OPTIONS, FUT_OPTIONS, AUTH_OPTIONS,
    YE_NONCLAIMS, run_ye_final_quantum_dynamical_ledger, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ye_final_quantum_dynamical_ledger()

class TestLedger:
    def test_count(self,result): assert len(result.ledger)==N_LEDGER
    def test_valid(self,result):
        for i in result.ledger: assert i.classification in ALLOWED_CLS
    def test_established(self,result):
        n=sum(1 for i in result.ledger if i.classification=="extension_established")
        assert n>=10

class TestGaps:
    def test_count(self,result): assert len(result.gaps)==N_GAPS
    def test_seq(self,result):
        for i,g in enumerate(result.gaps): assert g.rank==i+1

class TestHardGated:
    def test_all(self,result):
        assert result.quantum_dynamical_status in QD_OPTIONS
        assert result.interface_status in IF_OPTIONS
        assert result.completion_status in COMP_OPTIONS
        assert result.future_boundary_status in FUT_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.quantum_dynamical_status,result.interface_status,
           result.completion_status,result.future_boundary_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_ext(self,result): assert result.diagnostics["grand_total_extensions"]==7
    def test_params(self,result): assert result.diagnostics["grand_total_parameters"]==3
    def test_fields(self,result): assert result.diagnostics["grand_total_new_fields"]==0
    def test_y_axioms(self,result): assert result.diagnostics["y_new_axioms"]==0
    def test_qm(self,result): assert result.diagnostics["full_qm"] is False
    def test_integ(self,result): assert result.diagnostics["strong_integration"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self): assert len(YE_NONCLAIMS)==N_YE_NONCLAIMS
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
