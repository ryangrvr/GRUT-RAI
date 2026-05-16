from grut.hard_theory.s4_ctp_solver.candidate_structure_registry import (
    create_candidate_record,
)
from grut.hard_theory.s4_ctp_solver.candidate_structure_detection import (
    detect_candidate_structures,
)
from grut.hard_theory.s4_ctp_solver.candidate_scheme_assessment import (
    assess_candidate_scheme_safety,
)
from grut.hard_theory.s4_ctp_solver.candidate_extraction_blockers import (
    identify_extraction_blockers,
)
from grut.hard_theory.s4_ctp_solver.stage5d_candidate_readiness import (
    run_stage5d_candidate_readiness,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_candidate_registry_record_status():
    record = create_candidate_record(
        candidate_id="candidate_1",
        source_topologies=["t1"],
        symbolic_form="Euler_density",
        associated_invariant="Euler_density",
        scheme_sensitivity="unknown",
        occurrence_count=2,
    )
    assert record["status"] == "candidate_not_extracted"
    assert record["promotes_claims"] is False


def test_candidate_records_never_promote_claims():
    detection = detect_candidate_structures(
        [
            {"topology_id": "t1", "expression": "Euler_density"},
            {"topology_id": "t2", "expression": "Euler_density"},
        ]
    )
    assert detection["promotes_claims"] is False
    assert all(candidate["promotes_claims"] is False for candidate in detection["candidates"])


def test_detection_finds_repeated_structures():
    results = [
        {
            "topology_id": "t1",
            "expression": "Euler_density + R_squared",
            "divergence_structure": "1/epsilon^3",
        },
        {
            "topology_id": "t2",
            "expression": "Euler_density + R_squared",
            "divergence_structure": "1/epsilon^3",
        },
    ]
    detection = detect_candidate_structures(results)
    assert detection["status"] == "candidates_detected"
    assert detection["candidates"]


def test_detection_does_not_compute_coefficients():
    detection = detect_candidate_structures(
        [
            {"topology_id": "t1", "expression": "Euler_density"},
            {"topology_id": "t2", "expression": "Euler_density"},
        ]
    )
    candidate = detection["candidates"][0]
    assert candidate["status"] == "candidate_not_extracted"
    assert candidate["promotes_claims"] is False


def test_empty_detection_safe():
    detection = detect_candidate_structures([])
    assert detection["status"] == "no_candidates_detected"
    assert detection["candidates"] == []


def test_scheme_assessment_euler_density():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "Euler_density"}
    )
    assert assessment["scheme_sensitivity"] == "scheme_protected_candidate"


def test_scheme_assessment_weyl_squared():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "Weyl_squared"}
    )
    assert assessment["scheme_sensitivity"] == "scheme_protected_candidate"


def test_scheme_assessment_box_r():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "box_R"}
    )
    assert assessment["scheme_sensitivity"] == "total_derivative_scheme_dependent"


def test_scheme_assessment_r_squared():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "R_squared"}
    )
    assert assessment["scheme_sensitivity"] == "scheme_fragile"


def test_scheme_assessment_nonlocal():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "nonlocal_R_log_box_R"}
    )
    assert assessment["scheme_sensitivity"] == "scheme_protected_candidate"


def test_scheme_assessment_unknown():
    assessment = assess_candidate_scheme_safety(
        {"candidate_id": "c1", "associated_invariant": "unknown"}
    )
    assert assessment["scheme_sensitivity"] == "unknown"


def test_blockers_include_required():
    blockers = identify_extraction_blockers(
        {
            "candidate_id": "c1",
            "symbolic_form": "tensor_structure_placeholder",
            "source_topologies": ["tensor_topology"],
        }
    )
    assert "finite_part_not_computed" in blockers["blockers"]
    assert "convergence_not_established" in blockers["blockers"]
    assert "tensor_contractions_not_resolved" in blockers["blockers"]


def test_stage5d_audit_flags():
    report = run_stage5d_candidate_readiness()
    assert report["can_extract_any_candidate"] is False
    assert report["can_compute_r"] is False
    assert report["can_promote_r_route"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage5d_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage5a_before = pipeline.run_stage5a_native_attempt()
    stage5b_before = pipeline.run_stage5b_native_multi()
    stage5c_before = pipeline.run_stage5c_tensor_native()

    _ = pipeline.run_stage5d_candidate_readiness()

    stage5a_after = pipeline.run_stage5a_native_attempt()
    stage5b_after = pipeline.run_stage5b_native_multi()
    stage5c_after = pipeline.run_stage5c_tensor_native()

    assert stage5a_before["status"] == stage5a_after["status"]
    assert stage5b_before["status"] == stage5b_after["status"]
    assert stage5c_before["status"] == stage5c_after["status"]


def test_no_full_three_loop_claims_in_stage5d():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage5d_candidate_readiness()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
