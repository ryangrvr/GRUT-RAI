from grut.hard_theory.s4_ctp_solver.candidate_metadata_r3_validation import (
    validate_candidate_metadata_r3,
)
from grut.hard_theory.s4_ctp_solver.candidate_regulator_dependence_resolver import (
    apply_regulator_dependence_metadata,
)
from grut.hard_theory.s4_ctp_solver.candidate_tensor_origin_resolver import (
    apply_tensor_origin_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata import (
    run_stage12c_r3_complete_missing_metadata,
)


def _registry() -> dict:
    return {
        "candidate_buckets": {
            "c_final_candidate": {},
            "c_cosmo_candidate": {},
            "scheme_fragile_candidate": {},
            "nonlocal_scheme_protected_candidate": {},
        }
    }


def test_tensor_origin_class_assigned_for_all_candidates():
    registry = apply_tensor_origin_metadata(_registry())
    for candidate in registry["candidate_buckets"].values():
        assert candidate.get("tensor_origin_class")


def test_regulator_dependence_class_assigned_for_all_candidates():
    registry = apply_regulator_dependence_metadata(
        _registry(),
        {"regularization_attached": True},
        {"plan_summary": {"default_regulator": "dimensional_regularization_placeholder"}},
    )
    for candidate in registry["candidate_buckets"].values():
        assert candidate.get("regulator_dependence_class") == "symbolic_regulator_preserved"


def test_invalid_regulator_removed_fails_validation():
    registry = apply_regulator_dependence_metadata(
        _registry(),
        {"regularization_attached": False},
        {"plan_summary": {"default_regulator": "dimensional_regularization_placeholder"}},
    )
    registry = apply_tensor_origin_metadata(registry)
    validation = validate_candidate_metadata_r3(registry)
    assert validation["valid"] is False
    assert validation["invalid_regulator_removed"] is True


def test_remaining_missing_fields_empty_only_when_complete(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage9c_regularized_integrand",
        lambda: {"regularization_attached": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage9d_integration_dry_run",
        lambda: {"plan_summary": {"default_regulator": "dimensional_regularization_placeholder"}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage12c_r2_metadata_completion",
        lambda: {"registry": _registry()},
    )

    report = run_stage12c_r3_complete_missing_metadata()
    assert report["remaining_missing_fields"] == []
    assert report["metadata_completed"] is True


def test_rerun_12b_12c_recommended_true_only_when_complete(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage9c_regularized_integrand",
        lambda: {"regularization_attached": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage9d_integration_dry_run",
        lambda: {"plan_summary": {"default_regulator": "dimensional_regularization_placeholder"}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata.run_stage12c_r2_metadata_completion",
        lambda: {"registry": _registry()},
    )

    report = run_stage12c_r3_complete_missing_metadata()
    assert report["metadata_completed"] is True
    assert report["rerun_12b_12c_recommended"] is True


def test_no_r_computation():
    report = run_stage12c_r3_complete_missing_metadata()
    assert report["r_computation_allowed"] is False


def test_no_claim_promotion():
    report = run_stage12c_r3_complete_missing_metadata()
    assert report["promotes_claims"] is False
