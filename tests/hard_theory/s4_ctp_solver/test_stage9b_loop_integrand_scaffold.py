from grut.hard_theory.s4_ctp_solver.stage9b_loop_integrand_scaffold import (
    run_stage9b_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_components import (
    build_loop_integrand_components,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_assembly import (
    assemble_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_validation import (
    validate_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_audit import (
    audit_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_components_built():
    components = build_loop_integrand_components()
    assert components["components_id"] == "loop_integrand_components_v1"


def test_components_include_propagators():
    components = build_loop_integrand_components()
    assert components["propagators"]


def test_components_include_vertices():
    components = build_loop_integrand_components()
    assert components["vertices"]


def test_components_include_index_flow():
    components = build_loop_integrand_components()
    assert components["index_flow"]


def test_components_include_symmetry_factor():
    components = build_loop_integrand_components()
    assert components["symmetry_factor"]


def test_components_include_regulator_and_scheme():
    components = build_loop_integrand_components()
    assert components["regulator"]
    assert components["scheme"]


def test_loop_variables_present():
    components = build_loop_integrand_components()
    assert components["loop_variables"]


def test_integrand_scaffold_assembled():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    assert integrand["status"] == "integrand_scaffold"


def test_integrand_summary_present():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    summary = integrand["integrand_summary"]
    assert summary["propagator_count"] >= 0
    assert summary["vertex_count"] >= 0
    assert summary["loop_variable_count"] >= 0
    assert summary["scheme"]
    assert summary["regulator"]
    assert summary["evaluation_status"] == "symbolic_only"


def test_no_integration_performed():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    assert integrand["integration_performed"] is False


def test_no_propagator_evaluation():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    assert integrand["propagators_evaluated"] is False


def test_no_amplitude_computed():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    assert integrand["amplitude_computed"] is False


def test_no_finite_part_computed():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    assert integrand["finite_part_computed"] is False


def test_validation_passes_for_valid_scaffold():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    validation = validate_loop_integrand_scaffold(integrand)
    assert validation["status"] == "valid_integrand_scaffold"


def test_validation_fails_if_scheme_regulator_missing():
    components = build_loop_integrand_components()
    components["scheme"] = None
    components["regulator"] = None
    integrand = assemble_loop_integrand_scaffold(components)
    validation = validate_loop_integrand_scaffold(integrand)
    assert validation["status"] == "invalid_integrand_scaffold"


def test_audit_returns_no_finite_parts():
    components = build_loop_integrand_components()
    integrand = assemble_loop_integrand_scaffold(components)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_loop_integrand_scaffold(integrand)
    audit = audit_loop_integrand_scaffold({**integrand, "guard": guard}, validation)
    assert audit["can_compute_finite_parts"] is False


def test_stage9b_disallows_extraction():
    report = run_stage9b_loop_integrand_scaffold()
    assert report["can_extract"] is False


def test_stage9b_disallows_r_computation():
    report = run_stage9b_loop_integrand_scaffold()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage9b_loop_integrand_scaffold()
    assert report["integrand"]["finite_part_computed"] is False


def test_no_claim_promotion():
    report = run_stage9b_loop_integrand_scaffold()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage9b_loop_integrand_scaffold()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage9a_before = pipeline.run_stage9a_propagator_attachment()
    _ = pipeline.run_stage9b_loop_integrand_scaffold()
    stage9a_after = pipeline.run_stage9a_propagator_attachment()
    assert stage9a_before["status"] == stage9a_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
