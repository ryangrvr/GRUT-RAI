from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.finite_part_benchmark_library import (
    define_finite_part_benchmarks,
)
from grut.hard_theory.s4_ctp_solver.finite_part_extractor_benchmark import (
    extract_finite_part_from_benchmark,
)
from grut.hard_theory.s4_ctp_solver.finite_part_benchmark_comparison import (
    compare_finite_part_to_known,
)
from grut.hard_theory.s4_ctp_solver.finite_part_benchmark_audit import (
    audit_finite_part_benchmark,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_benchmark_library_exists():
    benchmarks = define_finite_part_benchmarks()
    assert benchmarks


def test_known_pole_and_finite_parts_present():
    benchmarks = define_finite_part_benchmarks()
    assert all("known_pole" in bench for bench in benchmarks)
    assert all("known_finite_part" in bench for bench in benchmarks)


def test_extraction_works_for_benchmarks():
    benchmarks = define_finite_part_benchmarks()
    result = extract_finite_part_from_benchmark(benchmarks[0])
    assert result["finite_part_extracted"] is True


def test_comparison_passes_for_correct_finite_part():
    benchmarks = define_finite_part_benchmarks()
    result = extract_finite_part_from_benchmark(benchmarks[0])
    comparison = compare_finite_part_to_known(result, benchmarks[0])
    assert comparison["comparison_status"] == "benchmark_pass"


def test_injected_wrong_finite_part_fails():
    benchmarks = define_finite_part_benchmarks()
    result = extract_finite_part_from_benchmark(benchmarks[0])
    result["finite_part"] = "wrong"
    comparison = compare_finite_part_to_known(result, benchmarks[0])
    assert comparison["comparison_status"] == "benchmark_fail"


def test_native_input_used_false():
    report = run_stage11c_finite_part_benchmark_gate()
    assert report["native_input_used"] is False


def test_can_extract_false():
    report = run_stage11c_finite_part_benchmark_gate()
    assert report["can_extract"] is False


def test_can_compute_r_false():
    report = run_stage11c_finite_part_benchmark_gate()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage11c_finite_part_benchmark_gate()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage11c_finite_part_benchmark_gate()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_blocks_without_benchmark_pass():
    benchmarks = define_finite_part_benchmarks()
    results = [extract_finite_part_from_benchmark(benchmarks[0])]
    comparisons = [
        {"comparison_status": "benchmark_fail", "matches_known_finite_part": False}
    ]
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_finite_part_benchmark(results, comparisons, guard)
    assert audit["can_advance_to_native_finite_part_attempt"] is False
