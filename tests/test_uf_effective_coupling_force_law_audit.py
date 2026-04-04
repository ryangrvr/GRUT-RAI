"""Tests for U-F --- Effective Coupling and Force-Law."""
import pytest
from grut.uf_effective_coupling_force_law_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_UF_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UF_PROBE, UF_FORCE, UF_RANGE, UF_DERIV, UF_AUTH, UF_OVERALL,
    PROBE_OPTIONS, FORCE_OPTIONS, RANGE_OPTIONS, DERIV_OPTIONS,
    AUTH_OPTIONS, UF_NONCLAIMS,
    run_uf_effective_coupling_force_law_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_uf_effective_coupling_force_law_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UF_NONCLAIMS)==N_UF_NONCLAIMS
        for nc in UF_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UF_PROBE=="constitutive_probe_response_conditionally_supported"
        assert UF_FORCE=="gradient_or_medium_response_only"
        assert UF_RANGE=="falloff_is_source_profile_dependent_only"
        assert UF_DERIV=="constitutive_or_phenomenological_only"

class TestTrackA:
    def test_postulate_needed(self, result):
        text=" ".join(result.track_a_precondition.findings).lower()
        assert "postulat" in text

class TestTrackB:
    def test_gradient_only(self, result):
        text=" ".join(result.track_b_force_candidates.findings).lower()
        assert "gradient" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_CANDIDATES
    def test_no_probe_native(self, result):
        assert "No" in result.evidence_table[0].probe_response

class TestObstructions:
    def test_count(self, result): assert len(result.track_g_obstructions)==N_OBSTRUCTIONS
    def test_first(self, result):
        assert "spatial" in result.track_g_obstructions[0].name.lower()

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.probe_coupling_status in PROBE_OPTIONS
        assert result.force_law_status in FORCE_OPTIONS
        assert result.range_status in RANGE_OPTIONS
        assert result.derivation_status in DERIV_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.probe_coupling_status,result.force_law_status,
           result.range_status,result.derivation_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_no_force(self, result): assert result.diagnostics["force_law_derived"] is False
    def test_no_probe(self, result): assert result.diagnostics["probe_coupling_native"] is False
    def test_no_inv_sq(self, result): assert result.diagnostics["inverse_square_licensed"] is False
    def test_no_gauge(self, result): assert result.diagnostics["gauge_mediation_available"] is False

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_uf_effective_coupling_force_law_audit()
        r2=run_uf_effective_coupling_force_law_audit()
        assert r1.force_law_status==r2.force_law_status
    def test_self_test(self): assert _self_test() is True
