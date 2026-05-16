import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_scalar_propagator_closed_form import (
    build_conformal_scalar_propagator_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_validation import (
    validate_conformal_scalar_propagator,
    compare_spectral_to_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_convergence import (
    diagnose_scalar_spectral_convergence,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_blocker_update import (
    update_full_s4_propagator_blocker_scalar_only,
)
from grut.hard_theory.s4_ctp_solver.stage6c_scalar_propagator import (
    run_stage6c_scalar_propagator,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_closed_form_scalar_propagator_record():
    record = build_conformal_scalar_propagator_closed_form()
    assert record["propagator_id"] == "s4_conformal_scalar_closed_form"
    assert record["field"] == "scalar"
    assert record["coupling"] == "conformal"
    assert record["background"] == "S4"
    assert record["status"] == "closed_form_benchmarked_scalar_only"
    assert "coincident_point_Z_to_1" in record["singularities"]
    assert record["zero_mode_issue"] is False


def test_validation_checks_scalar_only():
    record = build_conformal_scalar_propagator_closed_form()
    validation = validate_conformal_scalar_propagator(record)
    assert validation["status"] == "benchmarked_scalar_only"
    assert validation["checks"]["scales_as_1_over_a2"] is True
    assert validation["checks"]["conformal_denominator"] is True


def test_spectral_comparison_runs():
    radius = sp.symbols("a", positive=True)
    comparison = compare_spectral_to_closed_form([2, 4], radius)
    assert comparison["comparison"] == "spectral_vs_closed_form"
    assert comparison["convergence_proven"] is False


def test_convergence_diagnostic():
    diagnostic = diagnose_scalar_spectral_convergence([2, 4])
    assert diagnostic["status"] == "diagnostic_only"
    assert diagnostic["convergence_proven"] is False


def test_blocker_update_partial_closure():
    update = update_full_s4_propagator_blocker_scalar_only()
    assert update["scalar_conformal_subproblem"] == "partially_closed"
    assert update["tt_graviton_propagator"] == "open"
    assert update["overall_blocker_closed"] is False


def test_stage6c_flags_and_guard():
    report = run_stage6c_scalar_propagator()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6c_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6b_before = pipeline.run_stage6b_multi_blocker_harness()
    _ = pipeline.run_stage6c_scalar_propagator()
    stage6b_after = pipeline.run_stage6b_multi_blocker_harness()
    assert stage6b_before["status"] == stage6b_after["status"]


def test_no_full_three_loop_claims_in_stage6c():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6c_scalar_propagator()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
