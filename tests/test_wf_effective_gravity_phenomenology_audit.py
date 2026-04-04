"""Tests for W-F --- Effective Gravitational Phenomenology."""
import pytest
from grut.wf_effective_gravity_phenomenology_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_WF_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WF_STATIC, WF_FORCE, WF_CONSIST, WF_GRAVITY, WF_AUTH, WF_OVERALL,
    STATIC_OPTIONS, FORCE_OPTIONS, GEOM_CONSIST_OPTIONS, GRAVITY_OPTIONS, AUTH_OPTIONS,
    WF_NONCLAIMS, run_wf_effective_gravity_phenomenology_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wf_effective_gravity_phenomenology_audit()

class TestConstants:
    def test_nc(self):
        assert len(WF_NONCLAIMS)==N_WF_NONCLAIMS
        for nc in WF_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestHardGated:
    def test_all(self,result):
        assert result.static_field_status in STATIC_OPTIONS
        assert result.force_law_status in FORCE_OPTIONS
        assert result.geometry_consistency_status in GEOM_CONSIST_OPTIONS
        assert result.gravity_analogy_status in GRAVITY_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.static_field_status,result.force_law_status,
           result.geometry_consistency_status,result.gravity_analogy_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_helmholtz(self,result): assert result.diagnostics["static_operator"]=="Helmholtz_screened"
    def test_yukawa(self,result): assert "Yukawa" in result.diagnostics["profile"]
    def test_no_einstein(self,result): assert result.diagnostics["einstein_equations"] is False
    def test_no_unscreened(self,result): assert result.diagnostics["unscreened_gravity"] is False
    def test_agree(self,result): assert result.diagnostics["force_metric_agree_static"] is True
    def test_test_probe(self,result): assert result.diagnostics["test_probe_only"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_self_test(self): assert _self_test() is True
