from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.integrand_regularization_scheme import (
    define_integrand_regularization_scheme,
)
from grut.hard_theory.s4_ctp_solver.integrand_regularization_attachment import (
    attach_regularization_to_integrand,
)
from grut.hard_theory.s4_ctp_solver.regularized_integrand_validation import (
    validate_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.regularized_integrand_audit import (
    audit_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_assembly import (
    assemble_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_components import (
    build_loop_integrand_components,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_regularization_scheme_defined():
    scheme = define_integrand_regularization_scheme()
    assert scheme["scheme_id"] == "integrand_regularization_v1"


def test_scheme_includes_required_regulators():
    scheme = define_integrand_regularization_scheme()
    assert "dimensional_regularization_placeholder" in scheme["regulators"]
    assert "spectral_cutoff_placeholder" in scheme["regulators"]
    assert "exponential_damping_placeholder" in scheme["regulators"]
    assert "zeta_placeholder" in scheme["regulators"]


def test_default_regulator_exists():
    scheme = define_integrand_regularization_scheme()
    assert scheme["default_regulator"]


def test_regularization_attaches_to_integrand():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    assert result["regularization_attached"] is True


def test_regulator_factor_symbolic():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    assert result["regulator_factor"]


def test_divergence_tags_exist():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    assert result["divergence_tags"]


def test_no_integration_performed():
    report = run_stage9c_regularized_integrand()
    assert report["result"]["integration_performed"] is False


def test_no_amplitude_computed():
    report = run_stage9c_regularized_integrand()
    assert report["result"]["amplitude_computed"] is False


def test_no_finite_part_computed():
    report = run_stage9c_regularized_integrand()
    assert report["result"]["finite_part_computed"] is False


def test_validation_passes_for_valid_scaffold():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    validation = validate_regularized_integrand(result)
    assert validation["status"] == "valid_regularized_scaffold"


def test_validation_fails_if_regulator_metadata_missing():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    result["scheme"] = None
    validation = validate_regularized_integrand(result)
    assert validation["status"] == "invalid_regularized_scaffold"


def test_audit_returns_no_finite_parts():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_regularized_integrand(result)
    audit = audit_regularized_integrand({**result, "guard": guard}, validation)
    assert audit["can_compute_finite_parts"] is False


def test_stage9c_disallows_extraction():
    report = run_stage9c_regularized_integrand()
    assert report["can_extract"] is False


def test_stage9c_disallows_r_computation():
    report = run_stage9c_regularized_integrand()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage9c_regularized_integrand()
    assert report["result"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage9c_regularized_integrand()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage9c_regularized_integrand()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage9b_before = pipeline.run_stage9b_loop_integrand_scaffold()
    _ = pipeline.run_stage9c_regularized_integrand()
    stage9b_after = pipeline.run_stage9b_loop_integrand_scaffold()
    assert stage9b_before["status"] == stage9b_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
