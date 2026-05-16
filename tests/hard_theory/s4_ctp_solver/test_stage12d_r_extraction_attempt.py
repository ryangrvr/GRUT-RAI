import types

import pytest

from grut.hard_theory.s4_ctp_solver.r_extraction_audit import audit_r_extraction
from grut.hard_theory.s4_ctp_solver.r_physical_validation import (
    validate_r_physical_properties,
)
from grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt import (
    run_stage12d_r_extraction_attempt,
)


def _build_pair(candidate_suffix: str, renorm_id: str = "scheme_v1:reg_v1") -> dict:
    cancellation_ready = {
        "divergence_cancellation": True,
        "regulator_cancellation": True,
        "scheme_cancellation": True,
    }
    numerator = {
        "candidate_key": f"numerator_{candidate_suffix}",
        "candidate_id": f"numerator_{candidate_suffix}",
        "renorm_structure_id": renorm_id,
        "regulator_dependence_class": "dim_reg",
        "cancellation_ready": cancellation_ready,
        "dimensionless": True,
    }
    denominator = {
        "candidate_key": f"denominator_{candidate_suffix}",
        "candidate_id": f"denominator_{candidate_suffix}",
        "renorm_structure_id": renorm_id,
        "regulator_dependence_class": "dim_reg",
        "cancellation_ready": cancellation_ready,
        "dimensionless": True,
    }
    return {
        "numerator": numerator,
        "denominator": denominator,
        "renorm_structure_shared": renorm_id,
    }


def _stage12c_payload(valid_pairs, r_legal: bool) -> dict:
    return {
        "r_legal": r_legal,
        "valid_pairs": valid_pairs,
    }


def test_single_legal_pair_selected_only(monkeypatch):
    pair_one = _build_pair("one")
    pair_two = _build_pair("two")
    stage12c = _stage12c_payload(
        [{"pair": pair_one}, {"pair": pair_two}],
        r_legal=True,
    )

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["pair"]["numerator"]["candidate_id"] == pair_one["numerator"]["candidate_id"]


def test_no_multiple_pair_extraction(monkeypatch):
    pair_one = _build_pair("one")
    pair_two = _build_pair("two")
    stage12c = _stage12c_payload(
        [{"pair": pair_one}, {"pair": pair_two}],
        r_legal=True,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["pair"]["numerator"]["candidate_id"] != pair_two["numerator"]["candidate_id"]


def test_symbolic_ratio_constructed(monkeypatch):
    pair = _build_pair("symbolic")
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["symbolic_r"]["symbolic_ratio"] == "R_symbolic"


def test_scheme_tags_preserved(monkeypatch):
    pair = _build_pair("scheme", renorm_id="scheme_tag_v1")
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["symbolic_r"]["numerator"]["scheme_tags"] == "scheme_tag_v1"
    assert report["symbolic_r"]["denominator"]["scheme_tags"] == "scheme_tag_v1"


def test_regulator_tags_preserved(monkeypatch):
    pair = _build_pair("reg")
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["symbolic_r"]["numerator"]["regulator"] == "dim_reg"
    assert report["symbolic_r"]["denominator"]["regulator"] == "dim_reg"


def test_cancellation_execution_runs(monkeypatch):
    pair = _build_pair("cancel")
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert "cancellation_valid" in report["cancellation"]


def test_finite_isolation_runs(monkeypatch):
    pair = _build_pair("finite")
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert "isolation_ok" in report["finite"]


def test_validation_rejects_missing_scheme_metadata():
    symbolic_r = {
        "scheme_tags": None,
        "numerator": {"scheme_tags": None, "dimensionless": True},
        "denominator": {"scheme_tags": None, "dimensionless": True},
    }
    cancellation = {
        "scheme_dependence_cancelled": True,
        "regulator_dependence_cancelled": True,
    }
    validation = validate_r_physical_properties(symbolic_r, cancellation)
    assert validation["valid"] is False
    assert validation["scheme_metadata_present"] is False


def test_validation_rejects_remaining_regulator_dependence():
    symbolic_r = {
        "scheme_tags": "scheme",
        "numerator": {"scheme_tags": "scheme", "dimensionless": True},
        "denominator": {"scheme_tags": "scheme", "dimensionless": True},
    }
    cancellation = {
        "scheme_dependence_cancelled": True,
        "regulator_dependence_cancelled": False,
    }
    validation = validate_r_physical_properties(symbolic_r, cancellation)
    assert validation["valid"] is False


def test_audit_rejects_manual_simplification():
    symbolic_r = {"manual_step": "simplify"}
    cancellation = {"cancellation_valid": True}
    validation = {"valid": True}
    audit = audit_r_extraction(symbolic_r, cancellation, validation)
    assert audit["status"] == "invalid"
    assert "manual_step" in audit["violations"]


def test_audit_rejects_hidden_parameter_insertion():
    symbolic_r = {"inserted_parameter": "hidden"}
    cancellation = {"cancellation_valid": True}
    validation = {"valid": True}
    audit = audit_r_extraction(symbolic_r, cancellation, validation)
    assert audit["status"] == "invalid"
    assert "inserted_parameter" in audit["violations"]


def test_audit_rejects_non_cancelled_dependence():
    symbolic_r = {}
    cancellation = {"cancellation_valid": False}
    validation = {"valid": True}
    audit = audit_r_extraction(symbolic_r, cancellation, validation)
    assert audit["status"] == "invalid"
    assert "cancellation_incomplete" in audit["violations"]


def test_r_value_none_unless_validation_and_audit_pass(monkeypatch):
    pair = _build_pair("fail")
    pair["numerator"]["cancellation_ready"]["regulator_cancellation"] = False
    stage12c = _stage12c_payload([{"pair": pair}], r_legal=True)
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt.run_stage12c_r_legality_gate",
        lambda: stage12c,
    )

    report = run_stage12d_r_extraction_attempt()
    assert report["valid"] is False
    assert report["r_value"] is None


def test_no_claim_promotion_and_no_c_final_cosmo():
    report = run_stage12d_r_extraction_attempt()
    assert report["promotes_claims"] is False
    assert report["r_value"] not in {"C_Final", "C_Cosmo"}


def test_recursive_guard_invoked():
    report = run_stage12d_r_extraction_attempt()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
