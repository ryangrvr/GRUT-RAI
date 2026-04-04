"""Tests for X-D --- Quantum Probability Closure Boundary."""
import pytest
from grut.xd_quantum_probability_closure_boundary_audit import (
    N_CAPABILITIES, N_GAPS, N_XD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    XD_OP, XD_UNIT, XD_APP, XD_LABEL, XD_AUTH, XD_OVERALL,
    OP_OPTIONS, UNIT_OPTIONS, APP_OPTIONS, LABEL_OPTIONS, AUTH_OPTIONS,
    XD_NONCLAIMS, run_xd_quantum_probability_closure_boundary_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_xd_quantum_probability_closure_boundary_audit()

class TestHardGated:
    def test_all(self,result):
        assert result.operational_status in OP_OPTIONS
        assert result.unitarity_gap_status in UNIT_OPTIONS
        assert result.apparatus_gap_status in APP_OPTIONS
        assert result.closure_label_status in LABEL_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.operational_status,result.unitarity_gap_status,
           result.apparatus_gap_status,result.closure_label_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_op(self,result): assert result.diagnostics["operationally_sufficient"] is True
    def test_qm(self,result): assert result.diagnostics["full_qm"] is False
    def test_op_gaps(self,result): assert result.diagnostics["n_gaps_block_operation"]==0
    def test_comp_gaps(self,result): assert result.diagnostics["n_gaps_block_completion"]==6
    def test_caps(self,result): assert result.diagnostics["n_capabilities_supported"]==5

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self):
        assert len(XD_NONCLAIMS)==N_XD_NONCLAIMS
        for nc in XD_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_self_test(self): assert _self_test() is True
