from grut.hard_theory.s4_ctp_solver.stage8c_controlled_fragment_contractions import (
    run_stage8c_controlled_fragment_contractions,
)
from grut.hard_theory.s4_ctp_solver.tt_controlled_fragment import (
    define_controlled_tensor_fragment,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_engine import (
    run_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_validation import (
    validate_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_audit import (
    audit_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_controlled_fragment_defined():
    fragment = define_controlled_tensor_fragment()
    assert fragment["fragment_id"] == "controlled_tt_fragment_v1"


def test_controlled_fragment_scope():
    fragment = define_controlled_tensor_fragment()
    assert fragment["scope"] == "controlled_fragment_only"


def test_controlled_fragment_contains_multiple_local_fragments():
    fragment = define_controlled_tensor_fragment()
    assert len(fragment["local_fragments"]) > 1


def test_controlled_fragment_requires_no_propagator():
    fragment = define_controlled_tensor_fragment()
    assert fragment["requires_propagator"] is False


def test_controlled_fragment_requires_no_full_diagram():
    fragment = define_controlled_tensor_fragment()
    assert fragment["requires_full_diagram"] is False


def test_controlled_fragment_contraction_runs():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["status"] == "controlled_fragment_partial"


def test_ordering_protocol_followed():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    ordering = define_contraction_ordering_protocol()
    assert result["ordering_protocol_id"] == ordering["protocol_id"]
    assert result["ordering_protocol_followed"] is True


def test_projector_preserved():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["projector_preserved"] is True


def test_tt_constraints_preserved():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["tt_constraints_preserved"] is True


def test_no_propagator_evaluated():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["propagator_evaluated"] is False


def test_no_full_diagram_contracted():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["full_diagram_contracted"] is False


def test_no_finite_part_computed():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    assert result["finite_part_computed"] is False


def test_validation_passes_for_valid_fragment():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    validation = validate_controlled_fragment_contraction(result)
    assert validation["status"] == "valid_fragment"


def test_validation_fails_if_ordering_violation_injected():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    result["ordering_protocol_followed"] = False
    validation = validate_controlled_fragment_contraction(result)
    assert validation["status"] == "invalid_fragment"


def test_audit_returns_no_full_contractions():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_controlled_fragment_contraction(result)
    audit = audit_controlled_fragment_contraction({**result, "guard": guard}, validation)
    assert audit["full_contractions_performed"] is False


def test_audit_returns_no_finite_parts():
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_controlled_fragment_contraction(result)
    audit = audit_controlled_fragment_contraction({**result, "guard": guard}, validation)
    assert audit["can_compute_finite_parts"] is False


def test_stage8c_disallows_extraction():
    report = run_stage8c_controlled_fragment_contractions()
    assert report["can_extract"] is False


def test_stage8c_disallows_r_computation():
    report = run_stage8c_controlled_fragment_contractions()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage8c_controlled_fragment_contractions()
    assert report["result"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage8c_controlled_fragment_contractions()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage8c_controlled_fragment_contractions()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage8b_before = pipeline.run_stage8b_local_contractions()
    _ = pipeline.run_stage8c_controlled_fragment_contractions()
    stage8b_after = pipeline.run_stage8b_local_contractions()
    assert stage8b_before["status"] == stage8b_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
