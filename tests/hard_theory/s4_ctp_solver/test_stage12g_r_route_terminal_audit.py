from grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit import (
    run_stage12g_r_route_terminal_audit,
)


def _stage12a_payload() -> dict:
    return {"registry": {"candidate_buckets": {"bucket": {"id": "b1"}}}}


def _stage12b_payload() -> dict:
    return {"audit": {"audit": "scheme_stability"}}


def _stage12c_payload() -> dict:
    return {"r_legal": False, "blocking_reason": "no_valid_pairs"}


def _stage12d_payload() -> dict:
    return {
        "r_attempted": True,
        "failure_reason": "no_legal_pairs",
        "validation": {"valid": False, "reason": "physical_checks_failed"},
        "audit": {"status": "invalid", "violations": ["validation_failed"]},
    }


def _stage12e_payload() -> dict:
    return {"classification": "blocked_by_legality"}


def _stage12f_payload() -> dict:
    return {
        "next_required_action": "resolve_stage12c_legality",
        "blocking_reason": "no_valid_pairs",
    }


def test_terminal_audit_package(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12a_coefficient_assembly_dry_run",
        lambda: _stage12a_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12b_scheme_stability_audit",
        lambda: _stage12b_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12e_r_result_classification",
        lambda: _stage12e_payload(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit.run_stage12f_r_status_report",
        lambda: _stage12f_payload(),
    )

    report = run_stage12g_r_route_terminal_audit()
    assert report["status"] == "r_route_terminal_audit"
    assert report["terminal_classification"] == "blocked_by_legality"
    assert report["blockers"]
    assert report["next_required_action"] == "resolve_stage12c_legality"

    package = report["terminal_package"]
    assert "candidate_buckets" in package
    assert "scheme_stability_audit" in package
    assert "r_legality_gate" in package
    assert "r_symbolic_attempt" in package
    assert "r_result_classification" in package
    assert "r_status_report" in package
    assert "blocker_ledger" in package


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
