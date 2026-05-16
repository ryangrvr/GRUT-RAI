from grut.hard_theory.s4_ctp_solver.stage10c_multi_subintegrand_consistency import (
    run_stage10c_multi_subintegrand_consistency,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_set import (
    select_native_subintegrand_set,
)
from grut.hard_theory.s4_ctp_solver.multi_subintegrand_engine import (
    run_multi_subintegrand_attempt,
)
from grut.hard_theory.s4_ctp_solver.multi_subintegrand_consistency import (
    compare_subintegrand_behaviors,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)


def test_selects_two_or_three_subintegrands():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrands = select_native_subintegrand_set(integrand)
    assert 2 <= len(subintegrands) <= 3


def test_none_is_full_diagram():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    subintegrands = select_native_subintegrand_set(integrand)
    assert all(sub["full_diagram"] is False for sub in subintegrands)


def test_attempts_run_for_each():
    report = run_stage10c_multi_subintegrand_consistency()
    attempts = report["attempts"]["attempts"]
    assert len(attempts) == report["subintegrands_attempted"]


def test_regulator_remains_active_for_all():
    report = run_stage10c_multi_subintegrand_consistency()
    attempts = report["attempts"]["attempts"]
    assert all(attempt["regulator_present"] is True for attempt in attempts)


def test_no_finite_parts():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["finite_parts_computed"] is False


def test_no_amplitude():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["amplitude_computed"] is False


def test_comparison_runs():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["comparison"]["comparison"] == "multi_subintegrand_behavior"


def test_scheme_metadata_consistent():
    report = run_stage10c_multi_subintegrand_consistency()
    issues = report["comparison"]["issues"]
    assert "scheme_id_mismatch" not in issues
    assert "default_regulator_mismatch" not in issues


def test_invalid_unregulated_attempt_fails():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    scheme = run_stage9c_regularized_integrand().get("scheme", {})
    subintegrands = select_native_subintegrand_set(integrand)
    for sub in subintegrands:
        sub["scheme_id"] = scheme.get("scheme_id")
        sub["default_regulator"] = scheme.get("default_regulator")
    attempts = run_multi_subintegrand_attempt(subintegrands)
    attempts["attempts"][0]["regulator_present"] = False
    comparison = compare_subintegrand_behaviors(attempts)
    assert comparison["consistent"] is False


def test_can_extract_false():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["can_extract"] is False


def test_can_compute_r_false():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10c_multi_subintegrand_consistency()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
