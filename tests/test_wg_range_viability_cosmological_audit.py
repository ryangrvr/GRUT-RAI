"""Tests for W-G --- Range Viability and Cosmological Relevance."""
import pytest
from grut.wg_range_viability_cosmological_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_WG_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WG_SCREEN, WG_RANGE, WG_NATURAL, WG_COSMO, WG_AUTH, WG_OVERALL,
    SCREEN_OPTIONS, RANGE_OPTIONS, NATURAL_OPTIONS, COSMO_OPTIONS, AUTH_OPTIONS,
    WG_NONCLAIMS, run_wg_range_viability_cosmological_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wg_range_viability_cosmological_audit()

class TestConstants:
    def test_nc(self):
        assert len(WG_NONCLAIMS)==N_WG_NONCLAIMS
        for nc in WG_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestHardGated:
    def test_all(self,result):
        assert result.screening_scale_status in SCREEN_OPTIONS
        assert result.range_viability_status in RANGE_OPTIONS
        assert result.naturalness_status in NATURAL_OPTIONS
        assert result.cosmology_status in COSMO_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.screening_scale_status,result.range_viability_status,
           result.naturalness_status,result.cosmology_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_free(self,result): assert result.diagnostics["lambda_is_free"] is True
    def test_no_cosmo(self,result): assert result.diagnostics["cosmological_dynamics"] is False
    def test_short_robust(self,result): assert result.diagnostics["short_range_robust"] is True
    def test_no_tuning(self,result): assert result.diagnostics["tuning_crisis"] is False
    def test_no_natural(self,result): assert result.diagnostics["lambda_naturally_selected"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
