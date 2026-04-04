"""Tests for W-C --- Propagation Action and Closure."""
import pytest
from grut.wc_propagation_action_closure_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_WC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WC_ACTION, WC_RESPONSE, WC_DISS, WC_DOWNSTREAM, WC_AUTH, WC_OVERALL,
    ACTION_OPTIONS, RESPONSE_OPTIONS, DISS_OPTIONS, DOWNSTREAM_OPTIONS, AUTH_OPTIONS,
    WC_NONCLAIMS, run_wc_propagation_action_closure_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wc_propagation_action_closure_audit()

class TestConstants:
    def test_nc(self):
        assert len(WC_NONCLAIMS)==N_WC_NONCLAIMS
        for nc in WC_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert WC_ACTION=="action_for_undamped_core_only"
        assert WC_RESPONSE=="response_functional_or_doubled_field_packaging_preferred"
        assert WC_DISS=="damping_obstruction_partially_softened"
        assert WC_DOWNSTREAM=="propagation_platform_now_supports_later_probe_and_geometry_work"

class TestCandidates:
    def test_count(self,result): assert len(result.candidates)==N_CANDIDATES

class TestObstructions:
    def test_count(self,result): assert len(result.obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all(self,result):
        assert result.propagated_action_status in ACTION_OPTIONS
        assert result.response_functional_status in RESPONSE_OPTIONS
        assert result.dissipation_obstruction_status in DISS_OPTIONS
        assert result.downstream_extension_value in DOWNSTREAM_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.propagated_action_status,result.response_functional_status,
           result.dissipation_obstruction_status,result.downstream_extension_value,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_undamped(self,result): assert result.diagnostics["undamped_action_exists"] is True
    def test_damped(self,result): assert result.diagnostics["full_damped_action_exists"] is False
    def test_response(self,result): assert result.diagnostics["response_functional_available"] is True
    def test_softened(self,result): assert result.diagnostics["damping_obstruction_softened"] is True
    def test_not_resolved(self,result): assert result.diagnostics["damping_fully_resolved"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_self_test(self): assert _self_test() is True
