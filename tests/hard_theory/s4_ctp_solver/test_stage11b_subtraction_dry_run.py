from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.partition_divergence_identifier import (
    identify_partition_divergences,
)
from grut.hard_theory.s4_ctp_solver.partition_counterterm_mapper import (
    map_partition_divergences_to_counterterms,
)
from grut.hard_theory.s4_ctp_solver.subtraction_dry_run_plan import (
    build_subtraction_dry_run_plan,
)
from grut.hard_theory.s4_ctp_solver.subtraction_dry_run_audit import (
    audit_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
    run_stage11a_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_divergences_identified():
    report = run_stage11b_subtraction_dry_run()
    assert report["divergences"]["status"] == "divergences_identified_structural"


def test_regulator_remains_active():
    report = run_stage11b_subtraction_dry_run()
    assert report["divergences"]["regulator_active"] is True


def test_counterterm_mapping_runs():
    report = run_stage11b_subtraction_dry_run()
    assert report["mapping"]["mapping_status"] in {"mapped_structural", "partial", "unmapped"}


def test_unmapped_divergences_tracked():
    report = run_stage11b_subtraction_dry_run()
    assert "unmapped_divergences" in report["mapping"]


def test_dry_run_plan_built():
    report = run_stage11b_subtraction_dry_run()
    assert report["plan"]["status"] == "dry_run_only"


def test_no_subtraction_performed():
    report = run_stage11b_subtraction_dry_run()
    assert report["plan"]["subtractions_performed"] is False


def test_no_regulator_removed():
    report = run_stage11b_subtraction_dry_run()
    assert report["plan"]["regulator_removed"] is False


def test_no_finite_part():
    report = run_stage11b_subtraction_dry_run()
    assert report["plan"]["finite_part_computed"] is False


def test_no_amplitude():
    report = run_stage11b_subtraction_dry_run()
    assert report["audit"]["can_extract"] is False


def test_audit_blocks_extraction_and_r():
    report = run_stage11b_subtraction_dry_run()
    assert report["audit"]["can_extract"] is False
    assert report["audit"]["can_compute_r"] is False


def test_injected_unmapped_divergence_prevents_advancement():
    stage11a = run_stage11a_single_partition_integration()
    divergences = identify_partition_divergences(stage11a)
    divergences["divergences_identified"].append("unmapped_extra")
    mapping = map_partition_divergences_to_counterterms(divergences)
    plan = build_subtraction_dry_run_plan(mapping)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_subtraction_dry_run(plan, mapping, guard)
    assert audit["can_advance_to_finite_part_benchmark"] is False


def test_no_claim_promotion():
    report = run_stage11b_subtraction_dry_run()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage11b_subtraction_dry_run()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
