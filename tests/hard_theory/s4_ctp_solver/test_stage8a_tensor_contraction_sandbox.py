from grut.hard_theory.s4_ctp_solver.stage8a_tensor_contraction_sandbox import (
    run_stage8a_tensor_contraction_sandbox,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_rules import (
    define_sandbox_contraction_rules,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_contractions import (
    run_minimal_sandbox_contractions,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_results import (
    validate_sandbox_results,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_audit import (
    audit_tensor_contraction_sandbox,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_sandbox_rules_defined():
    rules = define_sandbox_contraction_rules()
    assert rules["rules_id"] == "tt_sandbox_contraction_rules_v1"


def test_sandbox_rules_include_allowed_and_forbidden():
    rules = define_sandbox_contraction_rules()
    assert rules["allowed"]
    assert rules["forbidden"]


def test_sandbox_rules_disallow_full_contractions():
    rules = define_sandbox_contraction_rules()
    assert rules["allows_full_contractions"] is False


def test_minimal_sandbox_contractions_run():
    results = run_minimal_sandbox_contractions()
    assert results["status"] == "sandbox_symbolic"


def test_trace_condition_contraction_present():
    results = run_minimal_sandbox_contractions()
    expressions = [entry["expression"] for entry in results["contractions_run"]]
    assert "g^{mu nu} h_TT_{mu nu} -> 0" in expressions


def test_transverse_condition_placeholder_present():
    results = run_minimal_sandbox_contractions()
    expressions = [entry["expression"] for entry in results["contractions_run"]]
    assert "nabla^mu h_TT_{mu nu} -> 0" in expressions


def test_projector_idempotence_placeholder_present():
    results = run_minimal_sandbox_contractions()
    expressions = [entry["expression"] for entry in results["contractions_run"]]
    assert "P_TT * P_TT -> P_TT" in expressions


def test_no_propagators_evaluated():
    results = run_minimal_sandbox_contractions()
    assert results["propagators_evaluated"] is False


def test_no_full_contractions_performed():
    results = run_minimal_sandbox_contractions()
    assert results["full_contractions_performed"] is False


def test_validation_passes_for_allowed_sandbox():
    results = run_minimal_sandbox_contractions()
    validation = validate_sandbox_results(results)
    assert validation["status"] == "valid_sandbox"


def test_validation_fails_if_forbidden_contraction_injected():
    results = run_minimal_sandbox_contractions()
    results["contractions_run"].append(
        {
            "rule": "full_diagram_contraction",
            "expression": "full_diagram_contraction",
        }
    )
    validation = validate_sandbox_results(results)
    assert validation["status"] == "invalid_sandbox"


def test_audit_returns_no_finite_parts():
    results = run_minimal_sandbox_contractions()
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_sandbox_results(results)
    audit = audit_tensor_contraction_sandbox({**results, "guard": guard}, validation)
    assert audit["can_compute_finite_parts"] is False


def test_stage8a_disallows_extraction():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["can_extract"] is False


def test_stage8a_disallows_r_computation():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["can_compute_r"] is False


def test_no_finite_parts_computed():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["results"]["finite_parts_computed"] is False


def test_no_r_extraction():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["results"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage8a_tensor_contraction_sandbox()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage7k_before = pipeline.run_stage7k_tensor_contraction_repair()
    _ = pipeline.run_stage8a_tensor_contraction_sandbox()
    stage7k_after = pipeline.run_stage7k_tensor_contraction_repair()
    assert stage7k_before["status"] == stage7k_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
