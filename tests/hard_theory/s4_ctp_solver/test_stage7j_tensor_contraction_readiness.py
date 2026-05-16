from grut.hard_theory.s4_ctp_solver.stage7j_tensor_contraction_readiness import (
    run_stage7j_tensor_contraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.tt_index_structure import (
    analyze_tt_index_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_rules import (
    define_tt_contraction_rules,
)
from grut.hard_theory.s4_ctp_solver.tt_projector_consistency import (
    check_tt_projector_consistency,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_readiness import (
    evaluate_contraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_index_structure_analysis_runs():
    result = analyze_tt_index_structure([
        {"structure": "tensor_preserved"},
    ])
    assert result["index_structure_id"] == "tt_indices"


def test_indices_detected_and_categorized():
    result = analyze_tt_index_structure([
        {"structure": "tensor_preserved"},
    ])
    assert result["indices_detected"]
    assert result["paired_indices"]


def test_free_indices_detected_if_present():
    result = analyze_tt_index_structure([])
    assert result["complete"] is False


def test_contraction_rules_defined():
    rules = define_tt_contraction_rules()
    assert rules["rules_id"] == "tt_contraction_rules"


def test_forbidden_contractions_exist():
    rules = define_tt_contraction_rules()
    assert rules["forbidden"]


def test_projector_consistency_check_runs():
    check = check_tt_projector_consistency(
        [{"projector": {"projector_id": "tt_projector_extended"}}]
    )
    assert check["projector_required"] is True


def test_readiness_true_only_if_structure_complete():
    index_structure = {
        "complete": True,
        "free_indices": [],
        "tt_constraints_respected": True,
    }
    rules = define_tt_contraction_rules()
    projector_check = {"projector_consistency": True}
    readiness = evaluate_contraction_readiness(index_structure, rules, projector_check)
    assert readiness["readiness"] == "ready"


def test_readiness_false_if_missing_element():
    index_structure = {
        "complete": False,
        "free_indices": ["mu"],
        "tt_constraints_respected": False,
    }
    rules = define_tt_contraction_rules()
    projector_check = {"projector_consistency": False}
    readiness = evaluate_contraction_readiness(index_structure, rules, projector_check)
    assert readiness["readiness"] == "not_ready"


def test_no_contractions_performed():
    report = run_stage7j_tensor_contraction_readiness()
    assert report["audit"]["contractions_performed"] is False


def test_flags_disallow_finite_parts_and_extraction():
    report = run_stage7j_tensor_contraction_readiness()
    assert report["can_compute_finite_parts"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage7j_tensor_contraction_readiness()
    assert report["promotes_claims"] is False


def test_guard_invoked():
    report = run_stage7j_tensor_contraction_readiness()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7j_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7i_before = pipeline.run_stage7i_convergence_repair()
    _ = pipeline.run_stage7j_tensor_contraction_readiness()
    stage7i_after = pipeline.run_stage7i_convergence_repair()
    assert stage7i_before["status"] == stage7i_after["status"]


def test_no_full_three_loop_claims_in_stage7j():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7j_tensor_contraction_readiness()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
