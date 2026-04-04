"""Tests for V-B --- Vacuum Existence, Ground-State, Source-Free Limit."""
import pytest
from grut.vb_vacuum_existence_ground_state_audit import (
    TAU, GAMMA, N_REGIMES, N_OBSTRUCTIONS, N_VB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VB_SF, VB_GS, VB_SP, VB_MACH, VB_AUTH, VB_OVERALL,
    SF_OPTIONS, GS_OPTIONS, SP_OPTIONS, MACH_OPTIONS, AUTH_OPTIONS,
    VB_NONCLAIMS,
    run_vb_vacuum_existence_ground_state_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vb_vacuum_existence_ground_state_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VB_NONCLAIMS)==N_VB_NONCLAIMS
        for nc in VB_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VB_SF=="asymptotic_decay_to_zero_supported"
        assert VB_GS=="zero_state_is_constitutive_but_ontologically_ambiguous"
        assert VB_SP=="substrate_persists_with_zero_response_conditionally_supported"
        assert VB_MACH=="weak_source_dependence_only"

class TestTrackA:
    def test_decay(self, result):
        text=" ".join(result.track_a_source_free.findings).lower()
        assert "exp(-t/tau)" in text or "exponential" in text
    def test_zero_attractor(self, result):
        text=" ".join(result.track_a_source_free.findings).lower()
        assert "attractor" in text

class TestTrackB:
    def test_not_eigenstate(self, result):
        text=" ".join(result.track_b_ground_state.findings).lower()
        assert "eigenstate" in text or "hamiltonian" in text

class TestTrackD:
    def test_weak_only(self, result):
        text=" ".join(result.track_d_machian.findings).lower()
        assert "weak" in text

class TestTrackE:
    def test_stable(self, result):
        text=" ".join(result.track_e_stability.findings).lower()
        assert "stable" in text
    def test_no_ssb(self, result):
        text=" ".join(result.track_e_stability.findings).lower()
        assert "no" in text and ("ssb" in text or "symmetry breaking" in text or "mexican" in text)

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_REGIMES

class TestObstructions:
    def test_count(self, result): assert len(result.track_g_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.source_free_state_status in SF_OPTIONS
        assert result.ground_state_status in GS_OPTIONS
        assert result.substrate_persistence_status in SP_OPTIONS
        assert result.machian_status in MACH_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.source_free_state_status,result.ground_state_status,
           result.substrate_persistence_status,result.machian_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_stable(self, result): assert result.diagnostics["globally_stable"] is True
    def test_no_ssb(self, result): assert result.diagnostics["ssb_possible"] is False
    def test_no_vev(self, result): assert result.diagnostics["vev_licensed"] is False
    def test_no_mach(self, result): assert result.diagnostics["strict_machian_supported"] is False
    def test_no_nonzero(self, result): assert result.diagnostics["nonzero_stationary_exists"] is False
    def test_decay_rate(self, result): assert abs(result.diagnostics["decay_rate"]-GAMMA)<1e-15

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=5
    def test_idempotency(self):
        r1=run_vb_vacuum_existence_ground_state_audit()
        r2=run_vb_vacuum_existence_ground_state_audit()
        assert r1.source_free_state_status==r2.source_free_state_status
    def test_self_test(self): assert _self_test() is True
