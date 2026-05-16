import pytest

from grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification import (
    run_stage12e_r_result_classification,
)


def _stage12c_payload(r_legal: bool) -> dict:
    return {"r_legal": r_legal}


def _stage12d_payload(
    r_value=None,
    validation_ok=True,
    audit_ok=True,
    cancellation_ok=True,
    isolation_ok=True,
    symbolic_exists=True,
) -> dict:
    return {
        "r_value": r_value,
        "validation": {"valid": validation_ok},
        "audit": {"status": "valid" if audit_ok else "invalid"},
        "cancellation": {"cancellation_valid": cancellation_ok},
        "finite": {
            "finite_structure": "R_finite_symbolic" if symbolic_exists else None,
            "isolation_ok": isolation_ok,
        },
        "symbolic_r": {"symbolic_ratio": "R_symbolic"} if symbolic_exists else None,
    }


def test_blocked_by_legality(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(False),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "blocked_by_legality"


def test_blocked_by_validation(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(validation_ok=False),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "blocked_by_validation"


def test_blocked_by_audit(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(audit_ok=False),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "blocked_by_audit"


def test_ambiguous_symbolic_result(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(cancellation_ok=False, isolation_ok=False),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "ambiguous_symbolic_result"


def test_valid_symbolic_candidate(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(r_value="R_finite_symbolic"),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "valid_symbolic_candidate"
    assert report["r_physical_result"] is False
    assert report["can_publish_r"] is False
    assert report["can_claim_r"] is False


def test_failed_extraction(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12c_r_legality_gate",
        lambda: _stage12c_payload(True),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification.run_stage12d_r_extraction_attempt",
        lambda: _stage12d_payload(
            r_value=None,
            symbolic_exists=False,
            cancellation_ok=True,
            isolation_ok=True,
        ),
    )

    report = run_stage12e_r_result_classification()
    assert report["classification"] == "failed_extraction"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
