"""Tests for W-B --- Spatial Propagation Extension."""
import pytest
from grut.wb_spatial_propagation_extension_audit import (
    N_CANDIDATES, N_WB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    WB_PROP, WB_PREF, WB_SPEED, WB_LORENTZ, WB_AUTH, WB_OVERALL,
    PROP_OPTIONS, PREF_OPTIONS, SPEED_OPTIONS, LORENTZ_OPTIONS, AUTH_OPTIONS,
    WB_NONCLAIMS, run_wb_spatial_propagation_extension_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wb_spatial_propagation_extension_audit()

class TestConstants:
    def test_nc(self):
        assert len(WB_NONCLAIMS)==N_WB_NONCLAIMS
        for nc in WB_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert WB_PREF=="damped_hyperbolic_extension_preferred"
        assert WB_SPEED=="finite_characteristic_speed_conditionally_supported"
        assert WB_LORENTZ=="restricted_effective_lorentz_appearance_supported"

class TestCandidates:
    def test_count(self,result): assert result.n_candidates==N_CANDIDATES
    def test_c2_preferred(self,result):
        c2=[c for c in result.candidates if c.class_id=="C2"][0]
        assert c2.finite_speed is True
        assert c2.preserves_dissipation is True
    def test_c1_no_speed(self,result):
        c1=[c for c in result.candidates if c.class_id=="C1"][0]
        assert c1.finite_speed is False
    def test_recommended(self,result):
        assert "C2" in result.recommended

class TestHardGated:
    def test_all_in(self,result):
        assert result.propagation_extension_status in PROP_OPTIONS
        assert result.preferred_extension_class in PREF_OPTIONS
        assert result.speed_status in SPEED_OPTIONS
        assert result.lorentz_appearance_status in LORENTZ_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.propagation_extension_status,result.preferred_extension_class,
           result.speed_status,result.lorentz_appearance_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_speed(self,result): assert result.diagnostics["finite_speed"] is True
    def test_native(self,result): assert result.diagnostics["preserves_native_core"] is True
    def test_params(self,result): assert result.diagnostics["new_parameters"]==2
    def test_fields(self,result): assert result.diagnostics["new_fields"]==0

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
