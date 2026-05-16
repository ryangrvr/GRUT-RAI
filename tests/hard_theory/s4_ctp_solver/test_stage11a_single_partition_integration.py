from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
    run_stage11a_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.single_partition_selector import (
    select_single_approved_partition,
)
from grut.hard_theory.s4_ctp_solver.single_partition_integration_engine import (
    run_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.single_partition_behavior_check import (
    check_single_partition_behavior,
)
from grut.hard_theory.s4_ctp_solver.single_partition_audit import (
    audit_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_exactly_one_partition_selected():
    stage10f = run_stage10f_partition_consistency_audit()
    selection = select_single_approved_partition(stage10f)
    assert selection["selected_count"] == 1


def test_selected_partition_approved_by_10f():
    report = run_stage11a_single_partition_integration()
    assert report["selection"]["approval_source"] == "10F"
    collected = report["stage10f"]["collected"]["collected_attempts"]
    collected_ids = {
        attempt.get("partition_id") or attempt.get("subintegrand_id")
        for attempt in collected
    }
    assert report["selection"]["partition_id"] in collected_ids


def test_full_integrand_not_used():
    report = run_stage11a_single_partition_integration()
    assert report["selection"]["full_integrand"] is False


def test_integration_attempted():
    report = run_stage11a_single_partition_integration()
    assert report["integration_attempted"] is True


def test_regulator_active():
    report = run_stage11a_single_partition_integration()
    assert report["regulator_active"] is True


def test_no_divergence_subtraction():
    report = run_stage11a_single_partition_integration()
    assert report["result"]["divergences_subtracted"] is False


def test_no_finite_part():
    report = run_stage11a_single_partition_integration()
    assert report["result"]["finite_part_computed"] is False


def test_no_amplitude():
    report = run_stage11a_single_partition_integration()
    assert report["result"]["amplitude_computed"] is False


def test_behavior_check_runs():
    report = run_stage11a_single_partition_integration()
    assert report["behavior"]["behavior_ok"] is True


def test_invalid_regulator_removed_case_fails():
    stage10f = run_stage10f_partition_consistency_audit()
    selection = select_single_approved_partition(stage10f)
    result = run_single_partition_integration(selection)
    result["regulator_active"] = False
    behavior = check_single_partition_behavior(result)
    assert behavior["behavior_ok"] is False


def test_can_extract_false():
    report = run_stage11a_single_partition_integration()
    assert report["can_extract"] is False


def test_can_compute_r_false():
    report = run_stage11a_single_partition_integration()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage11a_single_partition_integration()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage11a_single_partition_integration()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage11a_single_partition_integration()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_invalid_when_multiple_selected():
    stage10f = run_stage10f_partition_consistency_audit()
    selection = select_single_approved_partition(stage10f)
    selection["selected_count"] = 2
    result = run_single_partition_integration(selection)
    behavior = check_single_partition_behavior(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_single_partition_integration(selection, result, behavior, guard)
    assert audit["status"] == "invalid"
