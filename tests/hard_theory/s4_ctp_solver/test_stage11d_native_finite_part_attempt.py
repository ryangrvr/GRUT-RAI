from grut.hard_theory.s4_ctp_solver.stage11d_native_finite_part_attempt import (
    run_stage11d_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
    run_stage11a_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_selector import (
    select_native_partition_for_finite_part,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_extractor import (
    attempt_native_partition_finite_part,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_validation import (
    validate_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_audit import (
    audit_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_selector_requires_readiness():
    stage11a = run_stage11a_single_partition_integration()
    stage11b = run_stage11b_subtraction_dry_run()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    selection = select_native_partition_for_finite_part(stage11a, stage11b, stage11c)
    assert selection["selection_allowed"] is True
    assert selection["selected_count"] == 1


def test_exactly_one_partition_selected():
    report = run_stage11d_native_finite_part_attempt()
    assert report["partition_count"] == 1


def test_finite_part_attempt_runs():
    report = run_stage11d_native_finite_part_attempt()
    assert report["finite_part_attempted"] is True


def test_coefficient_scope_single_partition_only():
    report = run_stage11d_native_finite_part_attempt()
    assert report["coefficient_scope"] == "single_partition_only"


def test_coefficient_name_not_forbidden():
    report = run_stage11d_native_finite_part_attempt()
    assert report["result"]["coefficient_name"] not in {"C_Final", "C_Cosmo", "R"}


def test_no_amplitude():
    report = run_stage11d_native_finite_part_attempt()
    assert report["amplitude_computed"] is False


def test_validation_catches_illegal_coefficient_naming():
    stage11a = run_stage11a_single_partition_integration()
    stage11b = run_stage11b_subtraction_dry_run()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    selection = select_native_partition_for_finite_part(stage11a, stage11b, stage11c)
    result = attempt_native_partition_finite_part(selection)
    result["coefficient_name"] = "C_Final"
    validation = validate_native_finite_part_attempt(result)
    assert validation["status"] == "invalid"


def test_audit_blocks_coefficients():
    report = run_stage11d_native_finite_part_attempt()
    assert report["audit"]["can_compute_c_final"] is False
    assert report["audit"]["can_compute_c_cosmo"] is False
    assert report["audit"]["can_compute_r"] is False
    assert report["audit"]["can_extract"] is False


def test_no_claim_promotion():
    report = run_stage11d_native_finite_part_attempt()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage11d_native_finite_part_attempt()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_invalid_when_validation_fails():
    stage11a = run_stage11a_single_partition_integration()
    stage11b = run_stage11b_subtraction_dry_run()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    selection = select_native_partition_for_finite_part(stage11a, stage11b, stage11c)
    result = attempt_native_partition_finite_part(selection)
    result["coefficient_name"] = "C_Cosmo"
    validation = validate_native_finite_part_attempt(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_native_finite_part_attempt(result, validation, guard)
    assert audit["status"] == "invalid"
