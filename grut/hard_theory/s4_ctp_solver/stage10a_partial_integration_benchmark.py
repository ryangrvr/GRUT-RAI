"""Stage 10A controlled partial integration benchmark."""

from typing import Dict, List

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
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10a_partial_integration_benchmark() -> Dict[str, object]:
    benchmarks = define_benchmark_subintegrals()
    results: List[Dict[str, object]] = [run_partial_integration(b) for b in benchmarks]
    comparisons = [
        compare_partial_integration_to_known(result, benchmark)
        for result, benchmark in zip(results, benchmarks)
    ]
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_partial_integration(results, comparisons, guard)

    all_benchmarks_pass = all(
        comparison.get("comparison_status") == "benchmark_pass" for comparison in comparisons
    )

    return {
        "stage": "10A",
        "status": "controlled_partial_integration_benchmark",
        "benchmarks_run": len(benchmarks),
        "all_benchmarks_pass": all_benchmarks_pass,
        "native_integrand_used": False,
        "can_advance_to_native_subintegral_dry_run": audit.get(
            "can_advance_to_native_subintegral_dry_run"
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
