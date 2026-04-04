"""Tests for X-C --- Outcome Selection, State-Update, Measurement."""
import pytest
from grut.xc_outcome_selection_state_update_audit import (
    N_CANDIDATES, N_XC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    XC_OUTCOME, XC_UPDATE, XC_INFLATION, XC_SCOPE, XC_AUTH, XC_OVERALL,
    OUTCOME_OPTIONS, UPDATE_OPTIONS, INFLATION_OPTIONS, SCOPE_OPTIONS, AUTH_OPTIONS,
    XC_NONCLAIMS, run_xc_outcome_selection_state_update_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_xc_outcome_selection_state_update_audit()

class TestHardGated:
    def test_all(self,result):
        assert result.outcome_postulate_status in OUTCOME_OPTIONS
        assert result.update_status in UPDATE_OPTIONS
        assert result.inflation_status in INFLATION_OPTIONS
        assert result.scope_status in SCOPE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.outcome_postulate_status,result.update_status,
           result.inflation_status,result.scope_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_axioms(self,result): assert result.diagnostics["total_axioms_xb_xc"]==3
    def test_dof(self,result): assert result.diagnostics["new_dof"]==0
    def test_no_collapse(self,result): assert result.diagnostics["collapse_ontology"] is False
    def test_no_resolved(self,result): assert result.diagnostics["measurement_problem_resolved"] is False
    def test_consistent(self,result): assert result.diagnostics["repeated_measurement_consistent"] is True
    def test_bell(self,result): assert result.diagnostics["bell_chsh_operational"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self):
        assert len(XC_NONCLAIMS)==N_XC_NONCLAIMS
        for nc in XC_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
