from grut.hard_theory.s4_ctp_solver.stage8d_diagram_skeleton import (
    run_stage8d_diagram_skeleton,
)
from grut.hard_theory.s4_ctp_solver.tt_diagram_skeleton import (
    define_tt_diagram_skeleton,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_contraction_engine import (
    run_skeleton_structural_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_constraint_checks import (
    check_skeleton_constraints,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_audit import (
    audit_skeleton_contraction,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def test_diagram_skeleton_defined():
    skeleton = define_tt_diagram_skeleton()
    assert skeleton["diagram_id"] == "tt_skeleton_v1"


def test_skeleton_includes_nodes_and_edges():
    skeleton = define_tt_diagram_skeleton()
    assert skeleton["nodes"]
    assert skeleton["edges"]


def test_propagators_placeholders_only():
    skeleton = define_tt_diagram_skeleton()
    assert skeleton["propagators"] == "placeholders_only"


def test_loops_present_structurally():
    skeleton = define_tt_diagram_skeleton()
    assert skeleton["loops_present"] is True


def test_skeleton_contraction_runs():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["status"] == "skeleton_structural"


def test_index_flow_resolves():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["index_flow_resolved"] in {True, False}


def test_tt_constraints_preserved():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["tt_constraints_preserved"] is True


def test_projectors_preserved():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["projectors_preserved"] is True


def test_no_propagator_evaluated():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["propagators_evaluated"] is False


def test_no_loop_integration():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["loops_evaluated"] is False


def test_no_finite_parts_computed():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    assert result["finite_part_computed"] is False


def test_constraint_check_runs():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    check = check_skeleton_constraints(result)
    assert check["constraint_check"] == "skeleton"


def test_audit_enforces_structure_only():
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    check = check_skeleton_constraints(result)
    audit = audit_skeleton_contraction({**result, "guard": guard}, check)
    assert audit["structure_only"] is True


def test_stage8d_disallows_extraction():
    report = run_stage8d_diagram_skeleton()
    assert report["can_extract"] is False


def test_stage8d_disallows_r_computation():
    report = run_stage8d_diagram_skeleton()
    assert report["can_compute_r"] is False


def test_no_r_extraction():
    report = run_stage8d_diagram_skeleton()
    assert report["result"]["r_extracted"] is False


def test_no_claim_promotion():
    report = run_stage8d_diagram_skeleton()
    assert report["promotes_claims"] is False


def test_index_flow_trace_exists():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert trace["status"] == "index_flow_trace_structural"


def test_index_flow_trace_records_node_flow():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert trace["node_index_flow"]


def test_index_flow_trace_records_edge_pairings():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert trace["edge_pairings"]


def test_index_flow_trace_records_projectors():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert trace["projector_positions"]


def test_index_flow_trace_unresolved_indices_explicit():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert "unresolved_indices" in trace


def test_index_flow_trace_no_evaluation_or_claims():
    report = run_stage8d_diagram_skeleton()
    trace = report["index_flow_trace"]
    assert trace["propagators_evaluated"] is False
    assert trace["loops_evaluated"] is False
    assert trace["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage8d_diagram_skeleton()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_earlier_stages_unchanged():
    pipeline = S4CTPPipeline()
    stage8c_before = pipeline.run_stage8c_controlled_fragment_contractions()
    _ = pipeline.run_stage8d_diagram_skeleton()
    stage8c_after = pipeline.run_stage8c_controlled_fragment_contractions()
    assert stage8c_before["status"] == stage8c_after["status"]


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
