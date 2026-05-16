from grut.hard_theory.s4_ctp_solver.stage8b_local_contractions import (
    run_stage8b_local_contractions,
)
from grut.hard_theory.s4_ctp_solver.tt_local_contraction_fragments import (
    define_local_contraction_fragments,
)
from grut.hard_theory.s4_ctp_solver.tt_local_contraction_engine import (
    run_local_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_local_contraction_validation import (
    validate_local_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_local_contraction_audit import (
    audit_local_contractions,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_local_fragments_defined():
    fragments = define_local_contraction_fragments()
    assert fragments


def test_each_fragment_scope_local_only():
    fragments = define_local_contraction_fragments()
    assert all(fragment["scope"] == "local_only" for fragment in fragments)


def test_each_fragment_requires_no_propagator():
    fragments = define_local_contraction_fragments()
    assert all(fragment["requires_propagator"] is False for fragment in fragments)


def test_each_fragment_requires_no_full_diagram():
    fragments = define_local_contraction_fragments()
    assert all(fragment["requires_full_diagram"] is False for fragment in fragments)


def test_local_contraction_engine_runs():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    assert result["status"] == "local_contraction_partial"


def test_local_contraction_scope_remains_local():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    assert result["contraction_scope"] == "local_only"


def test_no_propagator_evaluated():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    assert result["propagator_evaluated"] is False


def test_no_full_diagram_contraction():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    assert result["full_diagram_contracted"] is False


def test_no_finite_part_computed():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    assert result["finite_part_computed"] is False


def test_validation_passes_for_allowed_fragment():
    fragment = define_local_contraction_fragments()[0]
    result = run_local_contraction(fragment)
    validation = validate_local_contraction(result)
    assert validation["status"] == "valid_local"


def test_validation_fails_for_forbidden_fragment():
    fragment = define_local_contraction_fragments()[0]
    fragment["allowed_by_sandbox"] = False
    result = run_local_contraction(fragment)
    validation = validate_local_contraction(result)
    assert validation["status"] == "invalid_local"


def test_audit_returns_no_full_contractions():
    fragments = define_local_contraction_fragments()
    results = [run_local_contraction(fragment) for fragment in fragments]
    validations = [validate_local_contraction(result) for result in results]
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_local_contractions(results, validations, guard)
    assert audit["full_contractions_performed"] is False


def test_audit_returns_no_finite_parts():
    fragments = define_local_contraction_fragments()
    results = [run_local_contraction(fragment) for fragment in fragments]
    validations = [validate_local_contraction(result) for result in results]
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_local_contractions(results, validations, guard)
    assert audit["can_compute_finite_parts"] is False


def test_stage8b_disallows_extraction():
    report = run_stage8b_local_contractions()
    assert report["can_extract"] is False


def test_stage8b_disallows_r_computation():
    report = run_stage8b_local_contractions()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage8b_local_contractions()
    assert all(result["r_extracted"] is False for result in report["results"])


def test_no_claim_promotion():
    report = run_stage8b_local_contractions()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage8b_local_contractions()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage8a_before = pipeline.run_stage8a_tensor_contraction_sandbox()
    _ = pipeline.run_stage8b_local_contractions()
    stage8a_after = pipeline.run_stage8a_tensor_contraction_sandbox()
    assert stage8a_before["status"] == stage8a_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
