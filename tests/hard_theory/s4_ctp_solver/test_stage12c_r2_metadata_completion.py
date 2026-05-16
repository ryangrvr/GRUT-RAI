from grut.hard_theory.s4_ctp_solver.candidate_metadata_completion import (
    complete_candidate_metadata,
)
from grut.hard_theory.s4_ctp_solver.candidate_metadata_validation import (
    validate_candidate_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r2_metadata_completion import (
    run_stage12c_r2_metadata_completion,
)


def _registry() -> dict:
    return {
        "candidate_buckets": {
            "c_final_candidate": {"candidate_id": "c_final_candidate_v1"},
            "c_cosmo_candidate": {"candidate_id": "c_cosmo_candidate_v1"},
            "scheme_fragile_candidate": {"candidate_id": "scheme_fragile_candidate_v1"},
            "nonlocal_scheme_protected_candidate": {
                "candidate_id": "nonlocal_scheme_protected_candidate_v1"
            },
        }
    }


def test_every_candidate_gets_metadata_fields():
    registry = _registry()
    completion = complete_candidate_metadata(registry, {"attempts": {"results": []}}, {})
    buckets = completion["registry"]["candidate_buckets"]
    for candidate in buckets.values():
        assert "tensor_origin_class" in candidate
        assert "loop_order" in candidate
        assert "regulator_dependence_class" in candidate
        assert "renormalization_structure" in candidate
        assert "invariant_class" in candidate
        assert "locality_class" in candidate
        assert "scheme_class_source" in candidate
        assert "cancellation_inputs_available" in candidate


def test_missing_tensor_origin_class_fails_validation():
    registry = _registry()
    completion = complete_candidate_metadata(registry, {"attempts": {"results": []}}, {})
    buckets = completion["registry"]["candidate_buckets"]
    buckets["c_final_candidate"]["tensor_origin_class"] = None
    validation = validate_candidate_metadata(completion["registry"])
    assert validation["valid"] is False
    assert "tensor_origin_class" in validation["missing_fields"]


def test_missing_cancellation_inputs_available_fails_validation():
    registry = _registry()
    completion = complete_candidate_metadata(registry, {"attempts": {"results": []}}, {})
    buckets = completion["registry"]["candidate_buckets"]
    buckets["c_final_candidate"]["cancellation_inputs_available"] = None
    validation = validate_candidate_metadata(completion["registry"])
    assert validation["valid"] is False
    assert "cancellation_inputs_available" in validation["missing_fields"]


def test_c_cosmo_remains_fragile_by_default():
    registry = _registry()
    completion = complete_candidate_metadata(registry, {"attempts": {"results": []}}, {})
    candidate = completion["registry"]["candidate_buckets"]["c_cosmo_candidate"]
    assert candidate["invariant_class"] == "scheme_fragile"
    assert candidate["locality_class"] == "local"


def test_no_r_computation():
    report = run_stage12c_r2_metadata_completion()
    assert report["r_computation_allowed"] is False


def test_no_claim_promotion():
    report = run_stage12c_r2_metadata_completion()
    assert report["promotes_claims"] is False
