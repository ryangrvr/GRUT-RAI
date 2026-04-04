"""Tests for Appendix S-C --- Extension-Level and Emergent Symmetries."""
import pytest
from grut.sc_extension_emergent_symmetries_audit import (
    N_O3_CHECKS, N_SU2_CHECKS, N_GAUGE_CHECKS, N_SECTOR_PAIRS,
    N_LIMITATIONS, N_APPENDIX_P, N_SC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    SC_O3_VERDICT, SC_SU2_VERDICT, SC_LORENTZ_VERDICT,
    SC_GAUGE_VERDICT, SC_AUTH_VERDICT, SC_OVERALL_P,
    ALLOWED_O3, ALLOWED_SU2, ALLOWED_LORENTZ_EM, ALLOWED_GAUGE, ALLOWED_AUTH,
    SC_NONCLAIMS,
    run_sc_extension_emergent_symmetries_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_sc_extension_emergent_symmetries_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(SC_NONCLAIMS)==N_SC_NONCLAIMS
        for nc in SC_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert SC_O3_VERDICT=="o3_extension_sector_coherent_but_not_native"
        assert SC_SU2_VERDICT=="su2_like_observable_grammar_extension_level_only"
        assert SC_GAUGE_VERDICT=="no_native_or_effective_gauge_symmetry_identified"
        assert "lorentz" in SC_LORENTZ_VERDICT.lower()

class TestO3:
    def test_n_checks(self, result): assert result.track_b_o3.n_checks==N_O3_CHECKS
    def test_not_native(self, result): assert result.track_b_o3.o3_native is False
    def test_verdict(self, result): assert result.track_b_o3.o3_verdict==SC_O3_VERDICT

class TestSU2:
    def test_n_checks(self, result): assert result.track_c_su2.n_checks==N_SU2_CHECKS
    def test_verdict(self, result): assert result.track_c_su2.su2_verdict==SC_SU2_VERDICT

class TestExchange:
    def test_tau_caveat(self, result): assert result.track_d_exchange.tau_caveat_present is True
    def test_fermionic_blocked(self, result): assert result.track_d_exchange.fermionic_blocked is True

class TestLorentz:
    def test_verdict(self, result):
        assert result.track_e_lorentz.lorentz_emergence_verdict==SC_LORENTZ_VERDICT

class TestGauge:
    def test_none_found(self, result): assert result.track_f_gauge.any_gauge_found is False
    def test_verdict(self, result): assert result.track_f_gauge.gauge_verdict==SC_GAUGE_VERDICT

class TestSectors:
    def test_n_pairs(self, result): assert result.track_g_sectors.n_pairs==N_SECTOR_PAIRS

class TestLimitations:
    def test_n_items(self, result): assert result.track_h_limitations.n_items==N_LIMITATIONS

class TestAppendixP:
    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True

class TestHardGated:
    def test_all_exact(self, result):
        assert result.o3_verdict==SC_O3_VERDICT
        assert result.su2_like_verdict==SC_SU2_VERDICT
        assert result.lorentz_emergence_verdict==SC_LORENTZ_VERDICT
        assert result.gauge_verdict==SC_GAUGE_VERDICT
        assert result.authorization_verdict==SC_AUTH_VERDICT
    def test_all_in_allowed(self, result):
        assert result.o3_verdict in ALLOWED_O3
        assert result.su2_like_verdict in ALLOWED_SU2
        assert result.lorentz_emergence_verdict in ALLOWED_LORENTZ_EM
        assert result.gauge_verdict in ALLOWED_GAUGE
        assert result.authorization_verdict in ALLOWED_AUTH
    def test_all_distinct(self, result):
        v={result.o3_verdict,result.su2_like_verdict,
           result.lorentz_emergence_verdict,result.gauge_verdict,
           result.authorization_verdict}
        assert len(v)==5

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_diagnostics(self, result):
        assert result.diagnostics["o3_native"] is False
        assert result.diagnostics["any_gauge"] is False
    def test_idempotency(self):
        r1=run_sc_extension_emergent_symmetries_audit()
        r2=run_sc_extension_emergent_symmetries_audit()
        assert r1.o3_verdict==r2.o3_verdict
    def test_self_test(self): assert _self_test() is True
