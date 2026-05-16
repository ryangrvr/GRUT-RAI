from grut.hard_theory.s4_ctp_solver.audit_manifest import build_audit_manifest
from grut.hard_theory.s4_ctp_solver.capability_matrix import build_capability_matrix
from grut.hard_theory.s4_ctp_solver.refusal_report import generate_refusal_report
from grut.hard_theory.s4_ctp_solver.reproducibility_bundle import (
    build_reproducibility_bundle,
)
from grut.hard_theory.s4_ctp_solver.summary_report import build_summary_report
from grut.hard_theory.s4_ctp_solver.stage3f_external_audit import (
    run_stage3f_external_audit,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_audit_manifest_contains_all_stages():
    manifest = build_audit_manifest()
    for stage_id in ("Stage 1", "Stage 2", "Stage 3", "Stage 3B", "Stage 3C", "Stage 3D", "Stage 3E"):
        assert stage_id in manifest
    assert all(entry.allowed_claim_tier != "computed" for entry in manifest.values())
    assert all(entry.current_limitations for entry in manifest.values())


def test_capability_matrix_full_3loop_row():
    matrix = build_capability_matrix()
    row = next(item for item in matrix if item.capability == "compute full 3-loop S4 CTP action")
    assert row.status == "not_available"
    assert row.promotes_claims is False


def test_refusal_report_full_3loop():
    report = generate_refusal_report("compute_full_3loop_s4_ctp")
    assert report["can_do"] is False
    assert report["available_alternatives"]
    assert report["required_before_allowed"]


def test_reproducibility_bundle():
    bundle = build_reproducibility_bundle()
    assert "pytest tests/hard_theory/s4_ctp_solver -q" in bundle["test_commands"]
    assert "pytest -q" in bundle["test_commands"]
    assert bundle["can_compute_3loop"] is False


def test_summary_report_helper():
    report = build_summary_report()
    assert report["stage_statuses"]
    assert report["capability_snapshot"]
    assert report["reproducibility_commands"]
    assert report["can_compute_3loop"] is False


def test_stage3f_audit_and_pipeline_status():
    report = run_stage3f_external_audit()
    assert report["status"] == "external_audit_ready"
    assert report["ready_for_stage4_attempts"] is True
    assert any("no GRUT claim promotion" == item for item in report["stage4_allowed_scope"])

    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    stage3d = pipeline.run_stage3d_scheme_audit()
    stage3e = pipeline.run_stage3e_crosscheck_audit()
    stage3f = pipeline.run_stage3f_external_audit()

    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"
    assert stage3e["status"] == "crosscheck_audit"
    assert stage3f["status"] == "external_audit_ready"
    assert stage3f["summary_report"]["can_compute_3loop"] is False


def test_no_full_three_loop_claims_in_stage3f():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage3f_external_audit()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
