from grut.hard_theory.s4_ctp_solver.stage_p1_nonlocal_anomaly_source_plan import (
    run_stage_p1_nonlocal_anomaly_source_plan,
)


def test_source_types_defined():
    report = run_stage_p1_nonlocal_anomaly_source_plan()
    assert report["source_types_defined"]
    assert "R_log_box_R" in report["source_types_defined"]
    assert report["protected_source_derived"] is False


def test_acceptance_tests_present():
    report = run_stage_p1_nonlocal_anomaly_source_plan()
    required = report["acceptance_tests"]
    assert "nonlocal_kernel_present" in required
    assert "anomaly_channel_derivation_present" in required
    assert "independent_replication_target_defined" in required


def test_r_blocked_and_no_claims():
    report = run_stage_p1_nonlocal_anomaly_source_plan()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
