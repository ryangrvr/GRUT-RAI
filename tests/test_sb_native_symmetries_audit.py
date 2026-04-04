"""Tests for Appendix S-B --- Native Symmetries and Exact Invariants."""
import pytest
from grut.sb_native_symmetries_audit import (
    N_CONTINUOUS, N_DISCRETE, N_LORENTZ, N_TIME_REV, N_CONSERVATION,
    N_SCALE, N_INVARIANTS, N_BOUNDARY, N_APPENDIX_P, N_SB_NONCLAIMS,
    N_ALLOWED, N_FORBIDDEN,
    SB_LORENTZ_VERDICT, SB_DISCRETE_VERDICT, SB_TIME_REVERSAL_VERDICT,
    SB_CONSERVATION_VERDICT, SB_AUTHORIZATION_VERDICT, SB_OVERALL_P_CLASS,
    ALLOWED_LORENTZ, ALLOWED_DISCRETE, ALLOWED_TIME_REV,
    ALLOWED_CONSERVATION, ALLOWED_AUTH, SB_NONCLAIMS,
    run_sb_native_symmetries_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_sb_native_symmetries_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(SB_NONCLAIMS)==N_SB_NONCLAIMS
        for nc in SB_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert SB_LORENTZ_VERDICT=="lorentz_invariance_natively_broken"
        assert SB_TIME_REVERSAL_VERDICT=="time_reversal_natively_broken_by_tau_dissipation"
        assert SB_CONSERVATION_VERDICT=="dissipative_balance_laws_only_no_standard_exact_conservation"
        assert SB_DISCRETE_VERDICT=="z2_reflection_native_and_exact"
    def test_overall_native_canon(self):
        assert SB_OVERALL_P_CLASS=="native_canon"

class TestContinuous:
    def test_count(self, result): assert result.track_a_continuous.n_items==N_CONTINUOUS
    def test_spatial_native(self, result):
        cs2=result.track_a_continuous.items[1]; assert cs2.status=="native"
        cs3=result.track_a_continuous.items[2]; assert cs3.status=="native"
    def test_boost_broken(self, result):
        cs4=result.track_a_continuous.items[3]; assert cs4.status=="broken"

class TestDiscrete:
    def test_count(self, result): assert result.track_b_discrete.n_items==N_DISCRETE
    def test_z2_exact(self, result):
        ds1=result.track_b_discrete.items[0]; assert ds1.status=="native_exact"
    def test_t_broken(self, result):
        ds4=result.track_b_discrete.items[3]; assert ds4.status=="broken"
    def test_verdict(self, result):
        assert result.track_b_discrete.discrete_verdict==SB_DISCRETE_VERDICT

class TestLorentz:
    def test_preferred_frame(self, result):
        assert result.track_c_lorentz.preferred_frame is True
    def test_verdict(self, result):
        assert result.track_c_lorentz.lorentz_verdict==SB_LORENTZ_VERDICT

class TestTimeReversal:
    def test_arrow(self, result):
        assert result.track_d_time_reversal.dissipative_arrow is True
    def test_verdict(self, result):
        assert result.track_d_time_reversal.time_reversal_verdict==SB_TIME_REVERSAL_VERDICT

class TestConservation:
    def test_no_noether(self, result):
        assert result.track_e_conservation.standard_noether is False
    def test_verdict(self, result):
        assert result.track_e_conservation.conservation_verdict==SB_CONSERVATION_VERDICT

class TestScale:
    def test_broken(self, result):
        assert result.track_f_scale.scale_broken is True

class TestInvariants:
    def test_n_exact(self, result):
        assert result.track_g_invariants.n_exact==5
    def test_ni1_exact(self, result):
        assert result.track_g_invariants.items[0].exact is True

class TestBoundary:
    def test_all_fenced(self, result):
        assert result.track_h_boundary.n_fenced==N_BOUNDARY
    def test_none_native(self, result):
        for i in result.track_h_boundary.items:
            assert i.native is False

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.lorentz_verdict==SB_LORENTZ_VERDICT
        assert result.discrete_symmetry_verdict==SB_DISCRETE_VERDICT
        assert result.time_reversal_verdict==SB_TIME_REVERSAL_VERDICT
        assert result.conservation_verdict==SB_CONSERVATION_VERDICT
        assert result.authorization_verdict==SB_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.lorentz_verdict in ALLOWED_LORENTZ
        assert result.discrete_symmetry_verdict in ALLOWED_DISCRETE
        assert result.time_reversal_verdict in ALLOWED_TIME_REV
        assert result.conservation_verdict in ALLOWED_CONSERVATION
        assert result.authorization_verdict in ALLOWED_AUTH
    def test_all_distinct(self, result):
        v={result.lorentz_verdict,result.discrete_symmetry_verdict,
           result.time_reversal_verdict,result.conservation_verdict,
           result.authorization_verdict}
        assert len(v)==5

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_diagnostics(self, result):
        d=result.diagnostics
        assert d["lorentz_broken"] is True
        assert d["t_reversal_broken"] is True
        assert d["standard_noether"] is False
        assert d["n_native_invariants"]==5
    def test_idempotency(self):
        r1=run_sb_native_symmetries_audit()
        r2=run_sb_native_symmetries_audit()
        assert r1.lorentz_verdict==r2.lorentz_verdict
    def test_self_test(self): assert _self_test() is True
