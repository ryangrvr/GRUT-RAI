"""Tests for T-D --- Temperature, Equilibrium, Steady-State."""
import pytest
from grut.td_temperature_equilibrium_audit import (
    TAU, GAMMA, N_REGIMES, N_OBSTRUCTIONS, N_TD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    TD_EQUIL_VERDICT, TD_TEMP_VERDICT, TD_DRIVEN_VERDICT,
    TD_FLUCT_VERDICT, TD_AUTH_VERDICT, TD_OVERALL_P,
    EQUIL_OPTIONS, TEMP_OPTIONS, DRIVEN_OPTIONS, FLUCT_OPTIONS,
    AUTH_OPTIONS, TD_NONCLAIMS,
    run_td_temperature_equilibrium_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_td_temperature_equilibrium_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(TD_NONCLAIMS) == N_TD_NONCLAIMS
        for nc in TD_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert TD_EQUIL_VERDICT == "dynamical_fixed_points_without_thermodynamic_equilibrium"
        assert TD_TEMP_VERDICT == "no_temperature_interpretation_licensed"
        assert TD_DRIVEN_VERDICT == "stable_tracking_or_steady_states_supported"
        assert TD_FLUCT_VERDICT == "deterministic_perturbation_decay_only"

class TestTrackA:
    def test_not_equilibrium(self, result):
        text = " ".join(result.track_a_equilibrium.findings).lower()
        assert "not" in text and "equilibrium" in text

class TestTrackC:
    def test_no_temperature(self, result):
        text = " ".join(result.track_c_temperature.findings).lower()
        assert "no temperature" in text or "not temperature" in text or "not licensed" in text

class TestTrackE:
    def test_no_fluctuations(self, result):
        text = " ".join(result.track_e_fluctuation.findings).lower()
        assert "deterministic" in text

class TestObstructions:
    def test_count(self, result): assert len(result.track_f_obstructions) == N_OBSTRUCTIONS
    def test_probability_first(self, result):
        assert "probability" in result.track_f_obstructions[0].name.lower()

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table) == N_REGIMES
    def test_no_equilibrium_anywhere(self, result):
        for row in result.evidence_table:
            assert row.equilibrium_licensed == "No"

class TestLicensed:
    def test_fixed_point(self, result):
        assert any("fixed_point" in t for t in result.licensed_language.licensed)
    def test_steady_state(self, result):
        assert any("steady_state" in t for t in result.licensed_language.licensed)

class TestNonlicensed:
    def test_equilibrium(self, result):
        assert any("equilibrium" in t for t in result.nonlicensed_language.nonlicensed)
    def test_temperature(self, result):
        assert any("temperature" in t for t in result.nonlicensed_language.nonlicensed)

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.equilibrium_status in EQUIL_OPTIONS
        assert result.temperature_status in TEMP_OPTIONS
        assert result.driven_state_status in DRIVEN_OPTIONS
        assert result.fluctuation_status in FLUCT_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v = {result.equilibrium_status, result.temperature_status,
             result.driven_state_status, result.fluctuation_status,
             result.authorization}
        assert len(v) == 5

class TestDiagnostics:
    def test_temp_false(self, result): assert result.diagnostics["temperature_licensed"] is False
    def test_equil_false(self, result): assert result.diagnostics["equilibrium_licensed"] is False
    def test_fluct_false(self, result): assert result.diagnostics["fluctuation_licensed"] is False
    def test_steady_true(self, result): assert result.diagnostics["steady_state_supported"] is True

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings) >= 5
    def test_idempotency(self):
        r1 = run_td_temperature_equilibrium_audit()
        r2 = run_td_temperature_equilibrium_audit()
        assert r1.temperature_status == r2.temperature_status
    def test_self_test(self): assert _self_test() is True
