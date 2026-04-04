"""Tests for W-D --- Probe Coupling and Response."""
import pytest
from grut.wd_probe_coupling_response_audit import (
    N_CANDIDATES, N_WD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WD_PROBE, WD_COUPLING, WD_RESPONSE, WD_BACK, WD_AUTH, WD_OVERALL,
    PROBE_OPTIONS, COUPLING_OPTIONS, RESPONSE_OPTIONS, BACK_OPTIONS, AUTH_OPTIONS,
    WD_NONCLAIMS, run_wd_probe_coupling_response_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wd_probe_coupling_response_audit()

class TestConstants:
    def test_nc(self):
        assert len(WD_NONCLAIMS)==N_WD_NONCLAIMS
        for nc in WD_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestCandidates:
    def test_count(self,result): assert result.n_candidates==N_CANDIDATES
    def test_preferred(self,result): assert "gradient" in result.recommended.lower()

class TestHardGated:
    def test_all(self,result):
        assert result.probe_identity_status in PROBE_OPTIONS
        assert result.coupling_class_status in COUPLING_OPTIONS
        assert result.response_status in RESPONSE_OPTIONS
        assert result.backreaction_status in BACK_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.probe_identity_status,result.coupling_class_status,
           result.response_status,result.backreaction_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_postulates(self,result): assert result.diagnostics["new_postulates"]==1
    def test_fields(self,result): assert result.diagnostics["new_fields"]==0
    def test_back(self,result): assert result.diagnostics["backreaction"] is False
    def test_eom(self,result): assert result.diagnostics["probe_has_eom"] is True
    def test_geom(self,result): assert result.diagnostics["geometry_leverage"]=="high"

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_self_test(self): assert _self_test() is True
