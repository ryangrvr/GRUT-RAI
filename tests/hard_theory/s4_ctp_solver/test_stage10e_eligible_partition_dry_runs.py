from grut.hard_theory.s4_ctp_solver.stage10e_eligible_partition_dry_runs import (
    run_stage10e_eligible_partition_dry_runs,
)
from grut.hard_theory.s4_ctp_solver.stage10d_integrand_partition_map import (
    run_stage10d_integrand_partition_map,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_selector import (
    select_eligible_partitions,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_engine import (
    run_eligible_partition_dry_runs,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_consistency import (
    check_eligible_partition_consistency,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_audit import (
    audit_eligible_partition_dry_runs,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_selects_only_eligible_future_partitions():
    stage10d = run_stage10d_integrand_partition_map()
    selection = select_eligible_partitions(stage10d)
    assert all(
        partition["partition_type"] == "eligible_future"
        for partition in selection["selected_partitions"]
    )


def test_blocked_and_forbidden_skipped():
    stage10d = run_stage10d_integrand_partition_map()
    selection = select_eligible_partitions(stage10d)
    assert selection["blocked_skipped"] is True
    assert selection["forbidden_skipped"] is True


def test_dry_runs_executed_for_eligible_partitions():
    report = run_stage10e_eligible_partition_dry_runs()
    attempts = report["attempts"]["attempts"]
    assert report["eligible_attempted"] == len(attempts)


def test_regulator_preserved():
    report = run_stage10e_eligible_partition_dry_runs()
    attempts = report["attempts"]["attempts"]
    assert all(attempt["regulator_present"] is True for attempt in attempts)


def test_no_amplitude():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["amplitude_computed"] is False


def test_no_finite_parts():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["finite_parts_computed"] is False


def test_invalid_blocked_attempt_fails():
    stage10d = run_stage10d_integrand_partition_map()
    selection = select_eligible_partitions(stage10d)
    blocked = [
        partition
        for partition in stage10d.get("partitions", [])
        if partition.get("partition_type") == "blocked"
    ]
    if blocked:
        selection["selected_partitions"].append(blocked[0])
    attempts = run_eligible_partition_dry_runs(selection["selected_partitions"])
    consistency = check_eligible_partition_consistency(attempts)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_eligible_partition_dry_runs(selection, attempts, consistency, guard)
    assert audit["status"] == "invalid"


def test_can_extract_false():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["can_extract"] is False


def test_can_compute_r_false():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10e_eligible_partition_dry_runs()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_scheme_metadata_consistent():
    report = run_stage10e_eligible_partition_dry_runs()
    issues = report["consistency"]["issues"]
    assert "scheme_id_mismatch" not in issues
    assert "default_regulator_mismatch" not in issues
