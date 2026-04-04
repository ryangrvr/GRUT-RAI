"""Tests for U-E --- Emergent Geometry and Metric-Like Structure."""
import pytest
from grut.ue_emergent_geometry_metric_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_UE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UE_METRIC, UE_GEOMETRY, UE_CURVATURE, UE_PROBE, UE_AUTH, UE_OVERALL,
    METRIC_OPTIONS, GEOMETRY_OPTIONS, CURVATURE_OPTIONS, PROBE_OPTIONS,
    AUTH_OPTIONS, UE_NONCLAIMS,
    run_ue_emergent_geometry_metric_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ue_emergent_geometry_metric_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UE_NONCLAIMS)==N_UE_NONCLAIMS
        for nc in UE_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UE_METRIC=="constitutive_metric_like_descriptor_conditionally_supported"
        assert UE_GEOMETRY=="refractive_or_conformal_analogy_only"
        assert UE_CURVATURE=="gradient_based_medium_language_only"
        assert UE_PROBE=="constitutive_response_or_refraction_only"

class TestTrackA:
    def test_constitutive(self, result):
        text=" ".join(result.track_a_metric.findings).lower()
        assert "constitutive" in text

class TestTrackC:
    def test_no_riemann(self, result):
        text=" ".join(result.track_c_curvature.findings).lower()
        assert "not curvature" in text or "not riemannian" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_CANDIDATES

class TestObstructions:
    def test_count(self, result): assert len(result.track_f_obstructions)==N_OBSTRUCTIONS
    def test_first(self, result):
        assert "spatial" in result.track_f_obstructions[0].name.lower()

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.metric_like_status in METRIC_OPTIONS
        assert result.geometry_status in GEOMETRY_OPTIONS
        assert result.curvature_status in CURVATURE_OPTIONS
        assert result.probe_trajectory_status in PROBE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.metric_like_status,result.geometry_status,
           result.curvature_status,result.probe_trajectory_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_metric_like_yes(self, result):
        assert result.diagnostics["metric_like_available"] is True
    def test_dynamics_no(self, result):
        assert result.diagnostics["metric_dynamics_available"] is False
    def test_curvature_no(self, result):
        assert result.diagnostics["curvature_available"] is False
    def test_geodesic_no(self, result):
        assert result.diagnostics["geodesic_available"] is False

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_ue_emergent_geometry_metric_audit()
        r2=run_ue_emergent_geometry_metric_audit()
        assert r1.metric_like_status==r2.metric_like_status
    def test_self_test(self): assert _self_test() is True
