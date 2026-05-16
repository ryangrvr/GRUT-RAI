import sympy as sp

from grut.hard_theory.s4_ctp_solver.known_results_library import known_results_library
from grut.hard_theory.s4_ctp_solver.toy_integrals_flat import (
    compute_scalar_bubble_integral,
    compute_scalar_tadpole_integral,
)
from grut.hard_theory.s4_ctp_solver.toy_integrals_curved import (
    heat_kernel_trace_low_order,
    s4_scalar_mode_sum_truncation,
)
from grut.hard_theory.s4_ctp_solver.heat_kernel import scalar_heat_kernel_coefficients
from grut.hard_theory.s4_ctp_solver.evaluation_engine import (
    evaluate_with_benchmark_check,
)
from grut.hard_theory.s4_ctp_solver.stage4a_benchmark_evaluation import (
    run_stage4a_benchmark_evaluation,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_known_results_library_entries():
    library = known_results_library()
    required = {
        "scalar_1loop_bubble_flat",
        "scalar_tadpole_flat",
        "dim_reg_pole",
        "log_divergence",
        "heat_kernel_trace_low_order",
    }
    assert required.issubset(set(library.keys()))


def test_bubble_integral_pole_structure():
    m = sp.symbols("m", positive=True)
    result = compute_scalar_bubble_integral(4, m, "dim_reg")
    epsilon = sp.symbols("epsilon")
    assert result.expression.has(epsilon)


def test_tadpole_integral_behavior():
    m = sp.symbols("m", positive=True)
    result = compute_scalar_tadpole_integral(4, m, "dim_reg")
    assert result.expression.has(m)


def test_dim_reg_pole_structure_present():
    m = sp.symbols("m", positive=True)
    result = compute_scalar_bubble_integral(4, m, "dim_reg")
    epsilon = sp.symbols("epsilon")
    assert result.expression.has(epsilon)


def test_curved_heat_kernel_trace_matches_stage2():
    coeffs = scalar_heat_kernel_coefficients()
    expected = coeffs.a0 + coeffs.a1
    result = heat_kernel_trace_low_order().expression
    assert sp.simplify(result - expected) == 0


def test_s4_spectral_truncation_behavior():
    a = sp.symbols("a", positive=True)
    result = s4_scalar_mode_sum_truncation(2, a)
    assert result.status == "partial_benchmark"
    assert "l<=2" in result.truncation


def test_evaluation_engine_matches_and_flags():
    m = sp.symbols("m", positive=True)
    bubble = compute_scalar_bubble_integral(4, m, "dim_reg")
    ok = evaluate_with_benchmark_check(bubble, "scalar_1loop_bubble_flat")
    assert ok["matches_known_result"] is True
    assert ok["promotes_claims"] is False

    tadpole = compute_scalar_tadpole_integral(4, m, "dim_reg")
    bad = evaluate_with_benchmark_check(tadpole, "scalar_1loop_bubble_flat")
    assert bad["matches_known_result"] is False


def test_stage4a_audit_gate_and_pipeline():
    report = run_stage4a_benchmark_evaluation()
    assert report["can_compute_full_3loop"] is False
    assert report["can_attempt_partial_3loop"] is True

    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    stage3d = pipeline.run_stage3d_scheme_audit()
    stage3e = pipeline.run_stage3e_crosscheck_audit()
    stage3f = pipeline.run_stage3f_external_audit()
    stage4a = pipeline.run_stage4a_benchmark_evaluation()

    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"
    assert stage3e["status"] == "crosscheck_audit"
    assert stage3f["status"] == "external_audit_ready"
    assert stage4a["status"] == "benchmark_evaluation"


def test_no_full_three_loop_claims_in_stage4a():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage4a_benchmark_evaluation()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
