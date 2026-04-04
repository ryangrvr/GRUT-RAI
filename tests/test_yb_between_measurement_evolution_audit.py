"""Tests for Y-B --- Between-Measurement Evolution Postulate."""
import pytest
from grut.yb_between_measurement_evolution_audit import (
    N_CANDIDATES, N_YB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    YB_EVOL, YB_PREF, YB_INFLATION, YB_SCOPE, YB_AUTH, YB_OVERALL,
    EVOL_OPTIONS, PREF_OPTIONS, INFLATION_OPTIONS, SCOPE_OPTIONS, AUTH_OPTIONS,
    YB_NONCLAIMS, run_yb_between_measurement_evolution_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_yb_between_measurement_evolution_audit()

class TestHardGated:
    def test_all(self,result):
        assert result.evolution_postulate_status in EVOL_OPTIONS
        assert result.preferred_evolution_class in PREF_OPTIONS
        assert result.inflation_status in INFLATION_OPTIONS
        assert result.scope_status in SCOPE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.evolution_postulate_status,result.preferred_evolution_class,
           result.inflation_status,result.scope_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_axioms(self,result): assert result.diagnostics["new_axioms"]==0
    def test_dof(self,result): assert result.diagnostics["new_dof"]==0
    def test_prob(self,result): assert result.diagnostics["prob_compatible"] is True
    def test_grut(self,result): assert result.diagnostics["grut_compatible"] is True
    def test_no_unit(self,result): assert result.diagnostics["unitarity_bought"] is False
    def test_no_decoh(self,result): assert result.diagnostics["decoherence_bought"] is False
    def test_trace(self,result): assert result.diagnostics["preserves_trace"] is True
    def test_cp(self,result): assert result.diagnostics["cp_divisible"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self): assert len(YB_NONCLAIMS)==N_YB_NONCLAIMS
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
