from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.coefficient_candidate_registry import (
    build_coefficient_candidate_registry,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_rules import (
    define_coefficient_assembly_rules,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_dry_run import (
    run_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_audit import (
    audit_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_candidate_registry_built():
    stage11e = run_stage11e_cross_partition_finite_consistency()
    registry = build_coefficient_candidate_registry(stage11e.get("attempts", {}).get("results", []))
    assert "candidate_buckets" in registry


def test_candidate_buckets_exist():
    report = run_stage12a_coefficient_assembly_dry_run()
    buckets = report["registry"]["candidate_buckets"]
    assert "c_final_candidate" in buckets
    assert "c_cosmo_candidate" in buckets
    assert "scheme_fragile_candidate" in buckets
    assert "nonlocal_scheme_protected_candidate" in buckets


def test_assembly_rules_block_physical_coefficients():
    rules = define_coefficient_assembly_rules()
    assert rules["physical_coefficients_allowed"] is False


def test_dry_run_emits_no_computed_coefficients():
    report = run_stage12a_coefficient_assembly_dry_run()
    assembly = report["assembly"]
    assert assembly["c_final_computed"] is False
    assert assembly["c_cosmo_computed"] is False
    assert assembly["r_computed"] is False


def test_audit_blocks_extraction():
    report = run_stage12a_coefficient_assembly_dry_run()
    assert report["audit"]["can_extract"] is False


def test_recursive_guard_invoked():
    report = run_stage12a_coefficient_assembly_dry_run()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_illegal_computed_coefficient_injection_fails():
    stage11e = run_stage11e_cross_partition_finite_consistency()
    registry = build_coefficient_candidate_registry(stage11e.get("attempts", {}).get("results", []))
    rules = define_coefficient_assembly_rules()
    assembly = run_coefficient_assembly_dry_run(registry, rules)
    assembly["c_final_computed"] = True
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_coefficient_assembly_dry_run(assembly, guard)
    assert audit["status"] == "invalid"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
