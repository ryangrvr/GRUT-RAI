from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt import (
    run_stage_p2_nonlocal_anomaly_kernel_attempt,
)


def test_scaffold_only_sources_do_not_close_kernel(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt.run_stage_p1_nonlocal_anomaly_source_plan",
        lambda: {"acceptance_tests": ["nonlocal_kernel_present"]},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "scaffold_only": True,
                    "indicators": {"nonlocal_kernel": True},
                }
            ]
        },
    )

    report = run_stage_p2_nonlocal_anomaly_kernel_attempt()
    assert report["kernel_found"] is False
    assert "only_scaffold_sources" in report["missing_reasons"]


def test_non_scaffold_candidate_recorded(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt.run_stage_p1_nonlocal_anomaly_source_plan",
        lambda: {"acceptance_tests": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "scaffold_only": False,
                    "indicators": {"imaginary_log": True},
                }
            ]
        },
    )

    report = run_stage_p2_nonlocal_anomaly_kernel_attempt()
    assert report["kernel_found"] is True
    assert report["kernel_candidates"]
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
