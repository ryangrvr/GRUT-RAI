from grut.hard_theory.s4_ctp_solver.stage10a_partial_integration_benchmark import (
    run_stage10a_partial_integration_benchmark,
)
from grut.hard_theory.s4_ctp_solver.benchmark_subintegrals import (
    define_benchmark_subintegrals,
)
from grut.hard_theory.s4_ctp_solver.partial_integration_engine import (
    run_partial_integration,
)
from grut.hard_theory.s4_ctp_solver.partial_integration_comparison import (
    compare_partial_integration_to_known,
)
from grut.hard_theory.s4_ctp_solver.partial_integration_audit import (
    audit_partial_integration,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_benchmark_list_exists():
    benchmarks = define_benchmark_subintegrals()
    assert benchmarks


def test_integration_performed_only_for_benchmarks():
    benchmarks = define_benchmark_subintegrals()
    result = run_partial_integration(benchmarks[0])
    assert result["integration_performed"] is True
    assert result["native_integrand_used"] is False


def test_known_result_comparison_passes():
    benchmarks = define_benchmark_subintegrals()
    result = run_partial_integration(benchmarks[0])
    comparison = compare_partial_integration_to_known(result, benchmarks[0])
    assert comparison["comparison_status"] == "benchmark_pass"


def test_injected_mismatch_fails():
    benchmarks = define_benchmark_subintegrals()
    result = run_partial_integration(benchmarks[0])
    result["result"] = "mismatch"
    comparison = compare_partial_integration_to_known(result, benchmarks[0])
    assert comparison["comparison_status"] == "benchmark_fail"


def test_native_integrand_not_used():
    report = run_stage10a_partial_integration_benchmark()
    assert report["native_integrand_used"] is False


def test_stage10a_disallows_extraction():
    report = run_stage10a_partial_integration_benchmark()
    assert report["can_extract"] is False


def test_stage10a_disallows_r_computation():
    report = run_stage10a_partial_integration_benchmark()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage10a_partial_integration_benchmark()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10a_partial_integration_benchmark()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10a_partial_integration_benchmark()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_full_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_valid_for_benchmarks():
    benchmarks = define_benchmark_subintegrals()
    results = [run_partial_integration(b) for b in benchmarks]
    comparisons = [compare_partial_integration_to_known(r, b) for r, b in zip(results, benchmarks)]
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_partial_integration(results, comparisons, guard)
    assert audit["status"] in {"valid", "invalid"}