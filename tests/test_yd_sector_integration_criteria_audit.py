"""Tests for Y-D --- Sector Integration Criteria."""
import pytest
from grut.yd_sector_integration_criteria_audit import (
    N_SECTORS, N_CRITERIA, N_INTERFACE_RULES, N_FUTURE_SECTORS,
    N_YD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    YD_INTEG, YD_IFACE, YD_READY, YD_BACK, YD_AUTH, YD_OVERALL,
    INTEG_OPTIONS, IFACE_OPTIONS, READY_OPTIONS, BACK_OPTIONS, AUTH_OPTIONS,
    YD_NONCLAIMS, run_yd_sector_integration_criteria_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_yd_sector_integration_criteria_audit()

class TestStructure:
    def test_crit(self,result): assert len(result.criteria)==N_CRITERIA
    def test_rules(self,result): assert len(result.interface_rules)==N_INTERFACE_RULES
    def test_sectors(self,result): assert len(result.sector_table)==N_SECTORS
    def test_ranking(self,result): assert len(result.future_ranking)==N_FUTURE_SECTORS

class TestHardGated:
    def test_all(self,result):
        assert result.integration_criteria_status in INTEG_OPTIONS
        assert result.interface_rule_status in IFACE_OPTIONS
        assert result.readiness_status in READY_OPTIONS
        assert result.backreaction_status in BACK_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.integration_criteria_status,result.interface_rule_status,
           result.readiness_status,result.backreaction_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_strong(self,result): assert result.diagnostics["strong_integration_achieved"] is False
    def test_nearest(self,result): assert result.diagnostics["nearest_future_sector"]=="apparatus"
    def test_most_distant(self,result): assert result.diagnostics["most_distant_sector"]=="chemistry"
    def test_no_back(self,result): assert result.diagnostics["backreaction_present"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self): assert len(YD_NONCLAIMS)==N_YD_NONCLAIMS
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_self_test(self): assert _self_test() is True
