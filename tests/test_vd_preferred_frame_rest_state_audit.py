"""Tests for V-D --- Preferred Frame and Rest-State Ontology."""
import pytest
from grut.vd_preferred_frame_rest_state_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_VD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VD_PF, VD_RS, VD_DRAG, VD_OBS, VD_AUTH, VD_OVERALL,
    PF_OPTIONS, RS_OPTIONS, DRAG_OPTIONS, OBS_OPTIONS, AUTH_OPTIONS,
    VD_NONCLAIMS, run_vd_preferred_frame_rest_state_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vd_preferred_frame_rest_state_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VD_NONCLAIMS)==N_VD_NONCLAIMS
        for nc in VD_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VD_PF=="constitutive_substrate_rest_frame_supported"
        assert VD_RS=="substrate_rest_state_supported_but_matter_rest_unlicensed"
        assert VD_DRAG=="no_vacuum_drag_claim_licensed"

class TestEvidence:
    def test_count(self,result): assert len(result.evidence_table)==N_CANDIDATES

class TestObstructions:
    def test_count(self,result): assert len(result.track_g_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.preferred_frame_status in PF_OPTIONS
        assert result.rest_state_status in RS_OPTIONS
        assert result.drag_status in DRAG_OPTIONS
        assert result.observability_status in OBS_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.preferred_frame_status,result.rest_state_status,
           result.drag_status,result.observability_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_substrate_frame(self,result): assert result.diagnostics["substrate_rest_frame"] is True
    def test_no_matter(self,result): assert result.diagnostics["matter_rest_frame"] is False
    def test_no_drag(self,result): assert result.diagnostics["vacuum_drag_licensed"] is False
    def test_no_back(self,result): assert result.diagnostics["back_reaction_present"] is False
    def test_conditional_obs(self,result): assert result.diagnostics["observability_conditional"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_idempotency(self):
        r1=run_vd_preferred_frame_rest_state_audit()
        r2=run_vd_preferred_frame_rest_state_audit()
        assert r1.drag_status==r2.drag_status
    def test_self_test(self): assert _self_test() is True
