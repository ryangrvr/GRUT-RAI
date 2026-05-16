from grut.hard_theory.s4_ctp_solver.s4_scalar_spectral_inversion import (
    perform_scalar_spectral_inversion,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_engine import (
    run_scalar_inversion_engine,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_comparison import (
    compare_to_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_audit import (
    audit_scalar_inversion,
)
from grut.hard_theory.s4_ctp_solver.s4_scalar_propagator_closed_form import (
    build_conformal_scalar_propagator_closed_form,
)
from grut.hard_theory.s4_ctp_solver.stage7a_scalar_inversion import (
    run_stage7a_scalar_inversion,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_scalar_inversion_runs_multiple_cutoffs():
    engine = run_scalar_inversion_engine([5, 10, 20, 50])
    l_values = [result["l_max"] for result in engine["results"]]
    assert l_values == [5, 10, 20, 50]


def test_partial_sum_computed():
    import sympy as sp

    radius = sp.symbols("a", positive=True)
    result = perform_scalar_spectral_inversion(5, radius)
    assert result["status"] == "partial_sum"
    assert result["expression"] is not None


def test_no_tt_usage():
    engine = run_scalar_inversion_engine([5])
    assert all(result["sector"] == "scalar" for result in engine["results"])


def test_closed_form_comparison_runs():
    engine = run_scalar_inversion_engine([5, 10])
    closed_form = build_conformal_scalar_propagator_closed_form()
    comparison = compare_to_closed_form(engine["results"], closed_form)
    assert comparison["comparison"] == "scalar_inversion_vs_closed"


def test_error_decreases_with_l_max():
    engine = run_scalar_inversion_engine([5, 10, 20, 50])
    closed_form = build_conformal_scalar_propagator_closed_form()
    comparison = compare_to_closed_form(engine["results"], closed_form)
    errors = comparison["error_trend"]
    assert all(earlier >= later for earlier, later in zip(errors, errors[1:]))


def test_convergence_observed_not_proven():
    engine = run_scalar_inversion_engine([5, 10])
    closed_form = build_conformal_scalar_propagator_closed_form()
    comparison = compare_to_closed_form(engine["results"], closed_form)
    assert comparison["convergence_observed"] is True
    assert comparison["convergence_proven"] is False


def test_inversion_audit_passes():
    engine = run_scalar_inversion_engine([5])
    audit = audit_scalar_inversion({**engine, "convergence_observed": True})
    assert audit["status"] == "valid_benchmark"


def test_stage7a_flags_and_guard():
    report = run_stage7a_scalar_inversion()
    assert report["inversion_performed"] is True
    assert report["tt_inversion_performed"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7a_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6g_before = pipeline.run_stage6g_spectral_strategy()
    _ = pipeline.run_stage7a_scalar_inversion()
    stage6g_after = pipeline.run_stage6g_spectral_strategy()
    assert stage6g_before["status"] == stage6g_after["status"]


def test_no_full_three_loop_claims_in_stage7a():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7a_scalar_inversion()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
