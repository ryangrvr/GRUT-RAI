from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_selector import (
    select_cross_partition_finite_partitions,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_engine import (
    run_cross_partition_finite_attempts,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_consistency import (
    check_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_audit import (
    audit_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.stage11d_native_finite_part_attempt import (
    run_stage11d_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_selects_two_or_three_partitions():
    stage10f = run_stage10f_partition_consistency_audit()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    stage11d = run_stage11d_native_finite_part_attempt()
    selection = select_cross_partition_finite_partitions(stage10f, stage11c, stage11d)
    assert selection["selected_count"] in {2, 3}


def test_no_amplitudes():
    report = run_stage11e_cross_partition_finite_consistency()
    assert report["amplitude_computed"] is False


def test_no_c_final_c_cosmo_r():
    report = run_stage11e_cross_partition_finite_consistency()
    results = report["attempts"]["results"]
    assert all(result["c_final_computed"] is False for result in results)
    assert all(result["c_cosmo_computed"] is False for result in results)
    assert all(result["r_extraction_attempted"] is False for result in results)


def test_rejects_illegal_coefficient_naming():
    stage10f = run_stage10f_partition_consistency_audit()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    stage11d = run_stage11d_native_finite_part_attempt()
    selection = select_cross_partition_finite_partitions(stage10f, stage11c, stage11d)
    attempts = run_cross_partition_finite_attempts(selection["selected_partitions"])
    attempts["results"][0]["coefficient_name"] = "C_Final"
    consistency = check_cross_partition_finite_consistency(attempts["results"])
    assert consistency["consistent"] is False


def test_consistency_check_runs():
    report = run_stage11e_cross_partition_finite_consistency()
    assert "consistent" in report["consistency"]


def test_audit_blocks_extraction():
    report = run_stage11e_cross_partition_finite_consistency()
    assert report["audit"]["can_extract"] is False


def test_recursive_guard_invoked():
    report = run_stage11e_cross_partition_finite_consistency()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_invalid_when_illegal_name():
    stage10f = run_stage10f_partition_consistency_audit()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    stage11d = run_stage11d_native_finite_part_attempt()
    selection = select_cross_partition_finite_partitions(stage10f, stage11c, stage11d)
    attempts = run_cross_partition_finite_attempts(selection["selected_partitions"])
    attempts["results"][0]["coefficient_name"] = "C_Cosmo"
    consistency = check_cross_partition_finite_consistency(attempts["results"])
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_cross_partition_finite_consistency(attempts["results"], consistency, guard)
    assert audit["status"] == "invalid"
