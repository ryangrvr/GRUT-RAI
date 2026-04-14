"""Tests for SM emergence from CTP fixed-point structure."""

def test_anomaly_cancellation():
    from grut_solver.sectors.ew.sm_emergence import anomaly_cancellation_constraint
    r = anomaly_cancellation_constraint()
    assert r["all_cancel"]
    assert abs(r["gravitational"]) < 1e-10
    assert abs(r["cubic"]) < 1e-10
    assert abs(r["mixed_su2"]) < 1e-10

def test_asymptotic_freedom():
    from grut_solver.sectors.ew.sm_emergence import asymptotic_freedom_constraint
    r = asymptotic_freedom_constraint()
    assert r["asymptotically_free"]
    assert r["b_0"] > 0
    assert r["N_f"] < r["N_f_max"]

def test_ssb_stability():
    from grut_solver.sectors.ew.sm_emergence import ssb_constraint
    r = ssb_constraint()
    assert r["broken_stable"]
    assert r["symmetric_unstable"]

def test_cp_violation():
    from grut_solver.sectors.ew.sm_emergence import cp_violation_constraint
    r = cp_violation_constraint()
    assert not r["R_equals_1"]
    assert r["N_gen_minimum"] == 3

def test_sm_satisfies_all():
    from grut_solver.sectors.ew.sm_emergence import sm_uniqueness_from_ctp
    r = sm_uniqueness_from_ctp()
    assert r["all_satisfied"]

def test_2gen_fails_cp():
    from grut_solver.sectors.ew.sm_emergence import sm_uniqueness_from_ctp
    r = sm_uniqueness_from_ctp()
    assert "FAILS" in r["alternatives"]["SM with 2 generations"]["conclusion"]

def test_no_color_fails():
    from grut_solver.sectors.ew.sm_emergence import sm_uniqueness_from_ctp
    r = sm_uniqueness_from_ctp()
    assert "FAILS" in r["alternatives"]["SU(2)×U(1) only (no color)"]["conclusion"]

def test_full_analysis_runs():
    from grut_solver.sectors.ew.sm_emergence import full_sm_emergence_analysis
    r = full_sm_emergence_analysis()
    assert "COMPUTED" in r["status"]
    assert len(r["honest_negatives"]) >= 4
