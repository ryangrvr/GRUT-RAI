from grut.hard_theory.s4_ctp_solver.extraction_criteria import (
    define_extraction_criteria,
)
from grut.hard_theory.s4_ctp_solver.extraction_requirement_mapper import (
    map_blockers_to_requirements,
)
from grut.hard_theory.s4_ctp_solver.extraction_dry_run import (
    perform_extraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.extraction_readiness_audit import (
    audit_extraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage5e_extraction_dry_run import (
    run_stage5e_extraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_extraction_criteria_list():
    criteria = define_extraction_criteria()
    items = criteria["criteria"]
    assert "finite_part_computed" in items
    assert "spectral_convergence_established" in items
    assert "tensor_contractions_resolved" in items
    assert "scheme_alignment_fixed" in items
    assert "ward_identity_verified" in items
    assert "cross_topology_consistency_confirmed" in items
    assert "independent_replication_available" in items
    assert criteria["promotes_claims"] is False


def test_criteria_not_marked_satisfied_by_default():
    criteria = define_extraction_criteria()
    audit = audit_extraction_readiness({"candidate_id": "c1"}, criteria)
    assert audit["criteria_satisfied"] == []
    assert audit["extraction_allowed"] is False


def test_blockers_map_to_requirements():
    mapping = map_blockers_to_requirements(
        {
            "candidate_id": "c1",
            "blockers": [
                "finite_part_not_computed",
                "tensor_contractions_not_resolved",
            ],
        }
    )
    assert mapping["can_satisfy_now"] is False
    assert mapping["requirements"]
    assert mapping["requirements"][0]["required_action"]


def test_dry_run_does_not_compute_coefficients():
    report = perform_extraction_dry_run({"candidate_id": "c1"})
    assert report["status"] == "extraction_not_permitted_dry_run"
    assert report["simulated_output"]["coefficient"] == "UNDEFINED"
    assert report["promotes_claims"] is False


def test_dry_run_missing_inputs_non_empty():
    report = perform_extraction_dry_run({"candidate_id": "c1"})
    assert report["missing_inputs"]


def test_readiness_audit_blocks_extraction():
    criteria = define_extraction_criteria()
    audit = audit_extraction_readiness({"candidate_id": "c1"}, criteria)
    assert audit["extraction_allowed"] is False
    assert audit["promotes_claims"] is False


def test_stage5e_flags_and_guard():
    report = run_stage5e_extraction_dry_run()
    assert report["any_extraction_allowed"] is False
    assert report["all_blocked"] is True
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage5e_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage5d_before = pipeline.run_stage5d_candidate_readiness()
    _ = pipeline.run_stage5e_extraction_dry_run()
    stage5d_after = pipeline.run_stage5d_candidate_readiness()
    assert stage5d_before["status"] == stage5d_after["status"]


def test_no_full_three_loop_claims_in_stage5e():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage5e_extraction_dry_run()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
