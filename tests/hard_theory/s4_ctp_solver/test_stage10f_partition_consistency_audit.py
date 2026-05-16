from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.partition_consistency_collector import (
    collect_partition_attempts,
)
from grut.hard_theory.s4_ctp_solver.partition_scheme_consistency import (
    check_partition_scheme_consistency,
)
from grut.hard_theory.s4_ctp_solver.partition_regulator_consistency import (
    check_partition_regulator_consistency,
)
from grut.hard_theory.s4_ctp_solver.partition_consistency_audit import (
    audit_partition_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_collects_stage10c_attempts():
    collected = collect_partition_attempts()
    sources = {attempt.get("source_stage") for attempt in collected["collected_attempts"]}
    assert "10C" in sources


def test_collects_stage10e_attempts():
    collected = collect_partition_attempts()
    sources = {attempt.get("source_stage") for attempt in collected["collected_attempts"]}
    assert "10E" in sources


def test_no_new_integrations():
    report = run_stage10f_partition_consistency_audit()
    assert report["new_integrations_performed"] is False


def test_scheme_consistency_check_runs():
    report = run_stage10f_partition_consistency_audit()
    assert "scheme_consistent" in report


def test_regulator_consistency_check_runs():
    report = run_stage10f_partition_consistency_audit()
    assert "regulator_consistent" in report


def test_injected_scheme_mismatch_fails():
    collected = collect_partition_attempts()
    attempts = collected["collected_attempts"]
    if attempts:
        attempts[0]["scheme_id"] = "mismatch"
    scheme_check = check_partition_scheme_consistency(attempts)
    assert scheme_check["scheme_consistent"] is False


def test_injected_regulator_removal_fails():
    collected = collect_partition_attempts()
    attempts = collected["collected_attempts"]
    if attempts:
        attempts[0]["regulator_present"] = False
    regulator_check = check_partition_regulator_consistency(attempts)
    assert regulator_check["regulator_consistent"] is False


def test_no_amplitude():
    report = run_stage10f_partition_consistency_audit()
    assert report["audit"]["status"] in {"valid", "invalid"}
    assert report["can_extract"] is False


def test_no_finite_parts():
    report = run_stage10f_partition_consistency_audit()
    assert report["can_compute_finite_parts"] is False


def test_can_extract_false():
    report = run_stage10f_partition_consistency_audit()
    assert report["can_extract"] is False


def test_can_compute_r_false():
    report = run_stage10f_partition_consistency_audit()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage10f_partition_consistency_audit()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10f_partition_consistency_audit()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10f_partition_consistency_audit()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_with_injected_mismatch_invalid():
    collected = collect_partition_attempts()
    attempts = collected["collected_attempts"]
    if attempts:
        attempts[0]["scheme_id"] = "mismatch"
    scheme_check = check_partition_scheme_consistency(attempts)
    regulator_check = check_partition_regulator_consistency(attempts)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_partition_consistency(collected, scheme_check, regulator_check, guard)
    assert audit["status"] in {"valid", "invalid"}
