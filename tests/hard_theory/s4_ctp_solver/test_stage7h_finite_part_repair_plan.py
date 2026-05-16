from grut.hard_theory.s4_ctp_solver.stage7h_finite_part_repair_plan import (
    run_stage7h_finite_part_repair_plan,
)
from grut.hard_theory.s4_ctp_solver.stage7g_finite_part_audit import (
    run_stage7g_finite_part_audit,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_registry import (
    build_finite_part_repair_registry,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_prioritizer import (
    prioritize_repairs,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_plan import (
    generate_repair_plan,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_audit import (
    audit_repair_plan,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_repair_registry_exists():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    assert registry["repairs"]


def test_all_blocker_categories_covered():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    blockers = {item["blocker"] for item in registry["repairs"]}
    required = set(registry["required_blockers"])
    assert required.issubset(blockers)


def test_repairs_not_started():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    assert all(item["status"] == "not_started" for item in registry["repairs"])


def test_repairs_have_completion_test():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    assert all(item["completion_test"] for item in registry["repairs"])


def test_prioritizer_returns_top_priority():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    assert prioritization["top_priority"]


def test_priority_queue_includes_all_repairs():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    queue = set(prioritization["priority_queue"])
    repairs = {item["repair_id"] for item in registry["repairs"]}
    assert repairs == queue


def test_plan_contains_ordered_steps():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    plan = generate_repair_plan(prioritization["priority_queue"], registry["repairs"])
    steps = plan["steps"]
    assert steps
    assert [step["step"] for step in steps] == list(range(1, len(steps) + 1))


def test_plan_disallows_finite_parts():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    plan = generate_repair_plan(prioritization["priority_queue"], registry["repairs"])
    assert plan["can_compute_finite_parts_after_plan"] is False


def test_audit_covers_all_blockers():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    plan = generate_repair_plan(prioritization["priority_queue"], registry["repairs"])
    audit = audit_repair_plan(plan)
    assert not audit["missing_blockers"]


def test_audit_disallows_finite_parts():
    stage7g = run_stage7g_finite_part_audit()
    registry = build_finite_part_repair_registry(stage7g["blockers"])
    prioritization = prioritize_repairs(registry["repairs"])
    plan = generate_repair_plan(prioritization["priority_queue"], registry["repairs"])
    audit = audit_repair_plan(plan)
    assert audit["can_compute_finite_parts"] is False


def test_stage7h_flags_and_guard():
    report = run_stage7h_finite_part_repair_plan()
    assert report["status"] == "finite_part_blocker_repair_plan"
    assert report["repairs_started"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7h_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7g_before = pipeline.run_stage7g_finite_part_audit()
    _ = pipeline.run_stage7h_finite_part_repair_plan()
    stage7g_after = pipeline.run_stage7g_finite_part_audit()
    assert stage7g_before["status"] == stage7g_after["status"]


def test_no_full_three_loop_claims_in_stage7h():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7h_finite_part_repair_plan()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
