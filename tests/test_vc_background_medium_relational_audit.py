"""Tests for V-C --- Background vs Medium vs Relational."""
import pytest
from grut.vc_background_medium_relational_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_VC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VC_BG, VC_MED, VC_REL, VC_LABEL, VC_AUTH, VC_OVERALL,
    BG_OPTIONS, MED_OPTIONS, REL_OPTIONS, LABEL_OPTIONS, AUTH_OPTIONS,
    VC_NONCLAIMS, run_vc_background_medium_relational_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vc_background_medium_relational_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VC_NONCLAIMS)==N_VC_NONCLAIMS
        for nc in VC_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VC_BG=="constitutive_substrate_without_full_background_identity"
        assert VC_MED=="rest_frame_substrate_supported_without_material_medium"
        assert VC_REL=="weak_relational_manifestation_on_persistent_substrate"
        assert VC_LABEL=="distinct_scalar_dissipative_substrate_category_supported"

class TestEvidence:
    def test_count(self,result): assert len(result.evidence_table)==N_CANDIDATES

class TestObstructions:
    def test_count(self,result): assert len(result.track_h_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.background_status in BG_OPTIONS
        assert result.medium_status in MED_OPTIONS
        assert result.relational_status in REL_OPTIONS
        assert result.ontology_label_status in LABEL_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.background_status,result.medium_status,
           result.relational_status,result.ontology_label_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_persistent(self,result): assert result.diagnostics["persistent_substrate"] is True
    def test_no_aether(self,result): assert result.diagnostics["aether_identity"] is False
    def test_no_material(self,result): assert result.diagnostics["material_medium"] is False
    def test_no_mach(self,result): assert result.diagnostics["strict_relational"] is False
    def test_distinct(self,result): assert result.diagnostics["distinct_category"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_idempotency(self):
        r1=run_vc_background_medium_relational_audit()
        r2=run_vc_background_medium_relational_audit()
        assert r1.ontology_label_status==r2.ontology_label_status
    def test_self_test(self): assert _self_test() is True
