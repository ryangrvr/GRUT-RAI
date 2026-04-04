"""Tests for W-E --- Effective Geometry and Metric Extension."""
import pytest
from grut.we_effective_geometry_metric_extension_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_WE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WE_METRIC, WE_GEODESIC, WE_COMMON, WE_REGIME, WE_AUTH, WE_OVERALL,
    METRIC_OPTIONS, GEODESIC_OPTIONS, COMMON_OPTIONS, REGIME_OPTIONS, AUTH_OPTIONS,
    WE_NONCLAIMS, run_we_effective_geometry_metric_extension_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_we_effective_geometry_metric_extension_audit()

class TestConstants:
    def test_nc(self):
        assert len(WE_NONCLAIMS)==N_WE_NONCLAIMS
        for nc in WE_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestHardGated:
    def test_all(self,result):
        assert result.metric_extension_status in METRIC_OPTIONS
        assert result.geodesic_status in GEODESIC_OPTIONS
        assert result.common_geometry_status in COMMON_OPTIONS
        assert result.regime_status in REGIME_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.metric_extension_status,result.geodesic_status,
           result.common_geometry_status,result.regime_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_conformal(self,result): assert result.diagnostics["conformal_metric_available"] is True
    def test_geodesic(self,result): assert result.diagnostics["geodesic_redescription"] is True
    def test_no_einstein(self,result): assert result.diagnostics["einstein_equations"] is False
    def test_no_dynamics(self,result): assert result.diagnostics["metric_dynamics"] is False
    def test_slave(self,result): assert result.diagnostics["metric_slave_to_phi"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
