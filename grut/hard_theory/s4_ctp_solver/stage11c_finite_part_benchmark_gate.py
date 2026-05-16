"""Stage 11C finite-part benchmark gate."""

from typing import Dict, List

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


def run_stage11c_finite_part_benchmark_gate() -> Dict[str, object]:
    benchmarks = define_finite_part_benchmarks()
    results: List[Dict[str, object]] = []
    comparisons: List[Dict[str, object]] = []

    for benchmark in benchmarks:
        result = extract_finite_part_from_benchmark(benchmark)
        results.append(result)
        comparisons.append(compare_finite_part_to_known(result, benchmark))

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_finite_part_benchmark(results, comparisons, guard)

    all_pass = all(
        comparison.get("comparison_status") == "benchmark_pass" for comparison in comparisons
    )

    return {
        "stage": "11C",
        "status": "finite_part_benchmark_gate",
        "benchmarks_run": len(benchmarks),
        "all_benchmarks_pass": all_pass,
        "native_input_used": False,
        "can_advance_to_native_finite_part_attempt": audit.get(
            "can_advance_to_native_finite_part_attempt"
        ),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "benchmarks": benchmarks,
        "results": results,
        "comparisons": comparisons,
        "audit": audit,
        "guard": guard,
    }
