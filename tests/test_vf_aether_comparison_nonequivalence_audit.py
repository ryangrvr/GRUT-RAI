"""Tests for V-F --- Aether Comparison and Non-Equivalence."""
import pytest
from grut.vf_aether_comparison_nonequivalence_audit import (
    N_FEATURES, N_NOEQUIV, N_VF_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VF_AETHER, VF_WAVE, VF_DETECT, VF_MATERIAL, VF_AUTH, VF_OVERALL,
    AETHER_OPTIONS, WAVE_OPTIONS, DETECT_OPTIONS, MATERIAL_OPTIONS, AUTH_OPTIONS,
    VF_NONCLAIMS, run_vf_aether_comparison_nonequivalence_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vf_aether_comparison_nonequivalence_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VF_NONCLAIMS)==N_VF_NONCLAIMS
        for nc in VF_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VF_AETHER=="historical_aether_identity_not_supported"
        assert VF_WAVE=="no_luminiferous_role_licensed"
        assert VF_MATERIAL=="nonmaterial_constitutive_substrate_only"

class TestFeatures:
    def test_count(self,result): assert len(result.feature_comparison)==N_FEATURES
    def test_no_full_match(self,result):
        full=[f for f in result.feature_comparison if f.overlap=="present"]
        assert len(full)==0
    def test_one_partial(self,result):
        partial=[f for f in result.feature_comparison if "partial" in f.overlap]
        assert len(partial)==1

class TestEvidence:
    def test_count(self,result): assert len(result.evidence_table)==N_FEATURES

class TestNonEquivalence:
    def test_count(self,result): assert len(result.track_f_nonequivalence)==N_NOEQUIV
    def test_wave_first(self,result):
        assert "wave" in result.track_f_nonequivalence[0].name.lower()

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.aether_identity_status in AETHER_OPTIONS
        assert result.wave_medium_status in WAVE_OPTIONS
        assert result.detectability_status in DETECT_OPTIONS
        assert result.material_medium_status in MATERIAL_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.aether_identity_status,result.wave_medium_status,
           result.detectability_status,result.material_medium_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_no_aether(self,result): assert result.diagnostics["aether_identity"] is False
    def test_no_lum(self,result): assert result.diagnostics["luminiferous_role"] is False
    def test_no_drag(self,result): assert result.diagnostics["drag_licensed"] is False
    def test_zero_full(self,result): assert result.diagnostics["n_fully_present"]==0
    def test_five_absent(self,result): assert result.diagnostics["n_absent"]==5

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_vf_aether_comparison_nonequivalence_audit()
        r2=run_vf_aether_comparison_nonequivalence_audit()
        assert r1.aether_identity_status==r2.aether_identity_status
    def test_self_test(self): assert _self_test() is True
