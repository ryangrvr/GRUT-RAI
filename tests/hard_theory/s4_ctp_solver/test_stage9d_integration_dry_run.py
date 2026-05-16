from grut.hard_theory.s4_ctp_solver.stage9d_integration_dry_run import (
    run_stage9d_integration_dry_run,
)
from grut.hard_theory.s4_ctp_solver.integration_variable_definition import (
    define_integration_variables,
)
from grut.hard_theory.s4_ctp_solver.integration_domain_specification import (
    define_integration_domain,
)
from grut.hard_theory.s4_ctp_solver.integration_ordering_plan import (
    define_integration_ordering,
)
from grut.hard_theory.s4_ctp_solver.regulator_handling_strategy import (
    define_regulator_handling,
)
from grut.hard_theory.s4_ctp_solver.integration_dry_run_audit import (
    audit_integration_dry_run,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_integration_variables_defined():
    variables = define_integration_variables()
    assert variables["variables"]


def test_domain_defined():
    domain = define_integration_domain()
    assert domain["status"] == "domain_defined_symbolic"


def test_ordering_defined():
    ordering = define_integration_ordering()
    assert ordering["status"] == "ordering_defined"


def test_regulator_strategy_defined():
    regulator = define_regulator_handling()
    assert regulator["status"] == "regulator_strategy_defined"


def test_no_integration_performed():
    report = run_stage9d_integration_dry_run()
    assert report["plan"]["integration_performed"] is False


def test_no_amplitudes_computed():
    report = run_stage9d_integration_dry_run()
    assert report["plan"]["amplitude_computed"] is False


def test_no_finite_parts_computed():
    report = run_stage9d_integration_dry_run()
    assert report["plan"]["finite_part_computed"] is False


def test_plan_summary_present():
    report = run_stage9d_integration_dry_run()
    summary = report["plan_summary"]
    assert summary["variable_count"] >= 0
    assert summary["domain_type"]
    assert summary["regularization_dependent"] in {True, False}
    assert summary["default_regulator"]
    assert summary["integration_performed"] is False
    assert summary["status"] == "dry_run_summary"


def test_audit_passes_for_valid_plan():
    variables = define_integration_variables()
    domain = define_integration_domain()
    ordering = define_integration_ordering()
    regulator = define_regulator_handling()
    plan = {
        "variables": variables,
        "domain": domain,
        "ordering": ordering,
        "regulator_handling": regulator,
        "integration_performed": False,
        "amplitude_computed": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
    }
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_integration_dry_run({**plan, "guard": guard})
    assert audit["status"] == "valid"


def test_audit_fails_if_component_missing():
    variables = define_integration_variables()
    ordering = define_integration_ordering()
    regulator = define_regulator_handling()
    plan = {
        "variables": variables,
        "domain": None,
        "ordering": ordering,
        "regulator_handling": regulator,
        "integration_performed": False,
        "amplitude_computed": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
    }
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_integration_dry_run({**plan, "guard": guard})
    assert audit["status"] == "invalid"


def test_stage9d_disallows_finite_parts():
    report = run_stage9d_integration_dry_run()
    assert report["audit"]["can_compute_finite_parts"] is False


def test_stage9d_disallows_extraction():
    report = run_stage9d_integration_dry_run()
    assert report["can_extract"] is False


def test_stage9d_disallows_r_computation():
    report = run_stage9d_integration_dry_run()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage9d_integration_dry_run()
    assert report["plan"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage9d_integration_dry_run()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage9d_integration_dry_run()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage9c_before = pipeline.run_stage9c_regularized_integrand()
    _ = pipeline.run_stage9d_integration_dry_run()
    stage9c_after = pipeline.run_stage9c_regularized_integrand()
    assert stage9c_before["status"] == stage9c_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
