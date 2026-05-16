from grut.hard_theory.s4_ctp_solver.stage12f_r_status_report import (
    run_stage12f_r_status_report,
)


def _stage12c_payload(r_legal: bool, blocking_reason: str = "no_valid_pairs") -> dict:
    return {"r_legal": r_legal, "blocking_reason": blocking_reason}


def _stage12d_payload(r_attempted: bool = True, failure_reason: str = "no_legal_pairs") -> dict:
    return {"r_attempted": r_attempted, "failure_reason": failure_reason}


def _stage12e_payload(classification: str, next_required_action: str) -> dict:
    return {
        "classification": classification,
        "next_required_action": next_required_action,
    }


def test_report_blocked_by_legality(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(False, "scheme_inputs_unstable"),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12e_r_result_classification",
        lambda: _stage12e_payload("blocked_by_legality", "resolve_stage12c_legality"),
    )

    report = run_stage12f_r_status_report()
    assert report["r_legal"] is False
    assert report["classification"] == "blocked_by_legality"
    assert report["blocking_reason"] == "scheme_inputs_unstable"


def test_report_valid_symbolic_candidate(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12e_r_result_classification",
        lambda: _stage12e_payload("valid_symbolic_candidate", "retain_symbolic_candidate_only"),
    )

    report = run_stage12f_r_status_report()
    assert report["classification"] == "valid_symbolic_candidate"
    assert report["can_publish_r"] is False
    assert report["can_claim_r"] is False
    assert report["blocking_reason"] == "symbolic_candidate_not_physical"


def test_report_includes_attempt_and_next_action(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(r_attempted=True, failure_reason="no_legal_pairs"),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12f_r_status_report.run_stage12e_r_result_classification",
        lambda: _stage12e_payload("failed_extraction", "recheck_symbolic_pipeline_inputs"),
    )

    report = run_stage12f_r_status_report()
    assert report["r_attempted"] is True
    assert report["next_required_action"] == "recheck_symbolic_pipeline_inputs"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
