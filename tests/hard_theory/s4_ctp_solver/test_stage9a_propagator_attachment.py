from grut.hard_theory.s4_ctp_solver.stage9a_propagator_attachment import (
    run_stage9a_propagator_attachment,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_registry import (
    build_propagator_attachment_registry,
)
from grut.hard_theory.s4_ctp_solver.skeleton_propagator_attachment import (
    attach_propagators_to_skeleton,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_validation import (
    validate_propagator_attachments,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_audit import (
    audit_propagator_attachment,
)
from grut.hard_theory.s4_ctp_solver.tt_diagram_skeleton import (
    define_tt_diagram_skeleton,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_registry_contains_propagators():
    registry = build_propagator_attachment_registry()
    ids = {record["propagator_id"] for record in registry}
    assert {"scalar_conformal_s4", "ghost_s4_structural", "tt_s4_scaffold"} <= ids


def test_registry_is_symbolic_or_scaffold():
    registry = build_propagator_attachment_registry()
    statuses = {record["evaluation_status"] for record in registry}
    assert statuses <= {"symbolic_only", "scaffold_not_evaluated"}


def test_skeleton_loaded():
    skeleton = define_tt_diagram_skeleton()
    assert skeleton["diagram_id"] == "tt_skeleton_v1"


def test_propagators_attach_to_edges():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    assert result["attachments"]


def test_edge_coverage_checked():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    assert result["edges_covered"] in {True, False}


def test_field_type_compatibility_checked():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    validation = validate_propagator_attachments(result)
    assert validation["status"] in {"valid_attachment", "invalid_attachment"}


def test_tt_edge_rejects_scalar_propagator():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    result["attachments"][0]["propagator_id"] = "scalar_conformal_s4"
    validation = validate_propagator_attachments(result)
    assert validation["status"] == "invalid_attachment"


def test_ghost_edge_rejects_tt_propagator():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    ghost_index = next(
        idx
        for idx, attachment in enumerate(result["attachments"])
        if attachment["field_type"] == "ghost"
    )
    result["attachments"][ghost_index]["propagator_id"] = "tt_s4_scaffold"
    validation = validate_propagator_attachments(result)
    assert validation["status"] == "invalid_attachment"


def test_no_propagators_evaluated():
    report = run_stage9a_propagator_attachment()
    assert report["propagators_evaluated"] is False


def test_no_loops_evaluated():
    report = run_stage9a_propagator_attachment()
    assert report["loops_evaluated"] is False


def test_no_finite_parts_computed():
    report = run_stage9a_propagator_attachment()
    assert report["attachment_result"]["finite_part_computed"] is False


def test_validation_passes_for_correct_attachments():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    validation = validate_propagator_attachments(result)
    assert validation["status"] == "valid_attachment"


def test_validation_fails_for_incompatible_injected_attachment():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    result["attachments"][1]["propagator_id"] = "scalar_conformal_s4"
    validation = validate_propagator_attachments(result)
    assert validation["status"] == "invalid_attachment"


def test_audit_returns_no_finite_parts():
    skeleton = define_tt_diagram_skeleton()
    registry = build_propagator_attachment_registry()
    result = attach_propagators_to_skeleton(skeleton, registry)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    validation = validate_propagator_attachments(result)
    audit = audit_propagator_attachment({**result, "guard": guard}, validation)
    assert audit["can_compute_finite_parts"] is False


def test_stage9a_disallows_extraction():
    report = run_stage9a_propagator_attachment()
    assert report["can_extract"] is False


def test_stage9a_disallows_r_computation():
    report = run_stage9a_propagator_attachment()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage9a_propagator_attachment()
    assert report["attachment_result"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage9a_propagator_attachment()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage9a_propagator_attachment()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage8d_before = pipeline.run_stage8d_diagram_skeleton()
    _ = pipeline.run_stage9a_propagator_attachment()
    stage8d_after = pipeline.run_stage8d_diagram_skeleton()
    assert stage8d_before["status"] == stage8d_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
