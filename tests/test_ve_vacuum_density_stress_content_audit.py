"""Tests for V-E --- Vacuum Density, Stress, Substrate Content."""
import pytest
from grut.ve_vacuum_density_stress_content_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_VE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    VE_DENS, VE_STRESS, VE_CONTENT, VE_FLUID, VE_AUTH, VE_OVERALL,
    DENS_OPTIONS, STRESS_OPTIONS, CONTENT_OPTIONS, FLUID_OPTIONS, AUTH_OPTIONS,
    VE_NONCLAIMS, run_ve_vacuum_density_stress_content_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ve_vacuum_density_stress_content_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(VE_NONCLAIMS)==N_VE_NONCLAIMS
        for nc in VE_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VE_DENS=="constitutive_density_like_descriptor_conditionally_supported"
        assert VE_STRESS=="no_stress_language_licensed"
        assert VE_CONTENT=="dissipation_does_not_upgrade_to_content_ontology"
        assert VE_FLUID=="no_fluid_or_equation_of_state_language_licensed"

class TestEvidence:
    def test_count(self,result): assert len(result.evidence_table)==N_CANDIDATES

class TestObstructions:
    def test_count(self,result): assert len(result.track_g_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.density_status in DENS_OPTIONS
        assert result.stress_status in STRESS_OPTIONS
        assert result.content_upgrade_status in CONTENT_OPTIONS
        assert result.fluid_status in FLUID_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.density_status,result.stress_status,
           result.content_upgrade_status,result.fluid_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_density_like(self,result): assert result.diagnostics["density_like_available"] is True
    def test_no_energy(self,result): assert result.diagnostics["true_energy_density"] is False
    def test_no_stress(self,result): assert result.diagnostics["stress_licensed"] is False
    def test_no_fluid(self,result): assert result.diagnostics["fluid_licensed"] is False
    def test_no_content_at_rest(self,result): assert result.diagnostics["content_at_rest"] is False
    def test_response_dependent(self,result): assert result.diagnostics["content_response_dependent"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_idempotency(self):
        r1=run_ve_vacuum_density_stress_content_audit()
        r2=run_ve_vacuum_density_stress_content_audit()
        assert r1.density_status==r2.density_status
    def test_self_test(self): assert _self_test() is True
