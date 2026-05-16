from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_schemes import (
    define_regularization_schemes,
)
from grut.hard_theory.s4_ctp_solver.tt_regularized_inversion import (
    perform_regularized_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_comparison import (
    compare_regularization_results,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_audit import (
    audit_regularized_inversion,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_regularization_schemes_defined():
    schemes = define_regularization_schemes()
    assert "cutoff" in schemes["schemes"]
    assert "exponential_damping" in schemes["schemes"]
    assert "zeta_placeholder" in schemes["schemes"]


def test_regularization_modifies_sum():
    import sympy as sp

    epsilon = sp.symbols("epsilon", positive=True)
    cutoff = perform_regularized_tt_inversion(5, epsilon, "cutoff")
    damped = perform_regularized_tt_inversion(5, epsilon, "exponential_damping")
    assert cutoff["regularized_sum"] != damped["regularized_sum"]


def test_structure_preserved():
    import sympy as sp

    epsilon = sp.symbols("epsilon", positive=True)
    result = perform_regularized_tt_inversion(5, epsilon, "cutoff")
    assert result["structure_preserved"] is True


def test_comparison_reports_divergence_reduction():
    import sympy as sp

    epsilon = sp.symbols("epsilon", positive=True)
    results = [
        perform_regularized_tt_inversion(5, epsilon, "cutoff"),
        perform_regularized_tt_inversion(5, epsilon, "exponential_damping"),
    ]
    comparison = compare_regularization_results(results)
    assert comparison["stability_improved"] is True
    assert comparison["structure_preserved"] is True


def test_audit_valid():
    import sympy as sp

    epsilon = sp.symbols("epsilon", positive=True)
    results = [
        perform_regularized_tt_inversion(5, epsilon, "cutoff"),
        perform_regularized_tt_inversion(5, epsilon, "exponential_damping"),
    ]
    comparison = compare_regularization_results(results)
    audit = audit_regularized_inversion({"regularized": results, "comparison": comparison})
    assert audit["status"] == "valid"


def test_stage7e_flags_and_guard():
    report = run_stage7e_tt_regularization()
    assert report["status"] == "tt_regularized_inversion"
    assert report["regularization_applied"] is True
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7e_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7d_before = pipeline.run_stage7d_tt_diagnostics()
    _ = pipeline.run_stage7e_tt_regularization()
    stage7d_after = pipeline.run_stage7d_tt_diagnostics()
    assert stage7d_before["status"] == stage7d_after["status"]


def test_no_full_three_loop_claims_in_stage7e():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7e_tt_regularization()
    assert report["can_compute_full_3loop"] is False
