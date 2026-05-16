from grut.hard_theory.s4_ctp_solver.stage10b_native_subintegrand_dry_run import (
    run_stage10b_native_subintegrand_dry_run,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_selector import (
    select_native_subintegrand,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_engine import (
    run_native_subintegrand_integration,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_comparison import (
    check_subintegrand_behavior,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_audit import (
    audit_native_subintegrand_run,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_subintegrand_selected():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrand = select_native_subintegrand(integrand)
    assert subintegrand["status"] == "subintegrand_selected"


def test_full_integrand_not_used():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["full_integrand_used"] is False


def test_integration_attempt_runs():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrand = select_native_subintegrand(integrand)
    result = run_native_subintegrand_integration(subintegrand)
    assert result["integration_attempted"] is True


def test_regulator_remains_present():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["result"]["regulator_present"] is True


def test_no_finite_part_computed():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["result"]["finite_part_computed"] is False


def test_no_amplitude_computed():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["result"]["amplitude_computed"] is False


def test_behavior_check_passes_for_valid_case():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["checks"]["behavior_ok"] is True


def test_injected_invalid_case_fails():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrand = select_native_subintegrand(integrand)
    result = run_native_subintegrand_integration(subintegrand)
    result["regulator_present"] = False
    checks = check_subintegrand_behavior(result)
    assert checks["behavior_ok"] is False


def test_audit_blocks_extraction():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["audit"]["can_extract"] is False


def test_stage_disallows_r_computation():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10b_native_subintegrand_dry_run()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage10a_before = pipeline.run_stage10a_partial_integration_benchmark()
    _ = pipeline.run_stage10b_native_subintegrand_dry_run()
    stage10a_after = pipeline.run_stage10a_partial_integration_benchmark()
    assert stage10a_before["status"] == stage10a_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_audit_blocks_when_unstable():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrand = select_native_subintegrand(integrand)
    result = run_native_subintegrand_integration(subintegrand)
    result["regulator_present"] = False
    checks = check_subintegrand_behavior(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_native_subintegrand_run(result, checks, guard)
    assert audit["status"] == "invalid"
