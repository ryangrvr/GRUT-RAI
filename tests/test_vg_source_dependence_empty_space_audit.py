"""Tests for V-G --- Source Dependence and Empty-Space Limit."""
import pytest
from grut.vg_source_dependence_empty_space_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_VG_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VG_EMPTY, VG_SUPPORT, VG_MULTI, VG_SDEP, VG_AUTH, VG_OVERALL,
    EMPTY_OPTIONS, SUPPORT_OPTIONS, MULTI_OPTIONS, SDEP_OPTIONS, AUTH_OPTIONS,
    VG_NONCLAIMS, run_vg_source_dependence_empty_space_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vg_source_dependence_empty_space_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VG_NONCLAIMS)==N_VG_NONCLAIMS
        for nc in VG_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VG_EMPTY=="zero_response_on_persistent_substrate_supported"
        assert VG_SUPPORT=="support_is_source_profile_dependent_only"
        assert VG_SDEP=="manifestation_strongly_source_dependent_on_persistent_substrate"

class TestEvidence:
    def test_count(self,result): assert len(result.evidence_table)==N_CANDIDATES

class TestObstructions:
    def test_count(self,result): assert len(result.track_h_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.empty_region_status in EMPTY_OPTIONS
        assert result.source_support_status in SUPPORT_OPTIONS
        assert result.multisource_status in MULTI_OPTIONS
        assert result.source_dependence_status in SDEP_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.empty_region_status,result.source_support_status,
           result.multisource_status,result.source_dependence_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_persists(self,result): assert result.diagnostics["substrate_persists_at_zero"] is True
    def test_no_vanish(self,result): assert result.diagnostics["space_vanishes_at_zero"] is False
    def test_no_created(self,result): assert result.diagnostics["source_created_space"] is False
    def test_linear(self,result): assert result.diagnostics["linear_superposition"] is True
    def test_no_horizon(self,result): assert result.diagnostics["horizon_licensed"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_idempotency(self):
        r1=run_vg_source_dependence_empty_space_audit()
        r2=run_vg_source_dependence_empty_space_audit()
        assert r1.empty_region_status==r2.empty_region_status
    def test_self_test(self): assert _self_test() is True
