from grut.hard_theory.s4_ctp_solver.nonlocal_form_extractor import (
    extract_nonlocal_markers,
)
from grut.hard_theory.s4_ctp_solver.im_log_kernel_constructor import (
    build_im_log_kernel_candidate,
)
from grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction import (
    run_stage_p3_nonlocal_form_construction,
)


def test_extractor_finds_im_log_marker():
    stageN2 = {
        "candidate_sources": [
            {"term": "Im log(-Box - i epsilon) nonlocal kernel", "scaffold_only": True}
        ]
    }
    report = extract_nonlocal_markers({}, stageN2, {}, {})
    assert report["marker_map"]["log_minus_box_i_epsilon_placeholder"] is True


def test_im_log_candidate_scaffold_only_gate():
    stageN2 = {
        "candidate_sources": [
            {"term": "Im log(-Box - i epsilon) nonlocal kernel", "scaffold_only": True}
        ]
    }
    report = extract_nonlocal_markers({}, stageN2, {}, {})
    result = build_im_log_kernel_candidate(report)
    assert result["status"] == "constructed"
    assert result["candidate"]["scaffold_only"] is False

    empty = extract_nonlocal_markers({}, {"candidate_sources": []}, {}, {})
    blocked = build_im_log_kernel_candidate(empty)
    assert blocked["status"] == "blocked"


def test_p3_candidate_symbolic_and_no_r(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage_p2_nonlocal_kernel_derivation",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage9c_regularized_integrand",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage11b_subtraction_dry_run",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "term": "Im log(-Box - i epsilon) nonlocal kernel",
                    "scaffold_only": True,
                }
            ]
        },
    )

    report = run_stage_p3_nonlocal_form_construction()
    assert report["protected_source_derived"] is False
    assert report["r_computation_allowed"] is False

    assert report["candidates_constructed"]
    candidate = report["candidates_constructed"][0]["candidate"]
    assert candidate["coefficient"] == "symbolic_uncomputed"


def test_missing_curvature_markers_blocked(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage_p2_nonlocal_kernel_derivation",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage9c_regularized_integrand",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage11b_subtraction_dry_run",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "term": "Im log(-Box - i epsilon) nonlocal kernel",
                    "scaffold_only": True,
                }
            ]
        },
    )

    report = run_stage_p3_nonlocal_form_construction()
    blocked_targets = {entry.get("target"): entry for entry in report["blocked_targets"]}
    assert blocked_targets["R_log_box_R"]["reason"] == "marker_missing"
    assert blocked_targets["Weyl_log_box_Weyl"]["reason"] == "marker_missing"


def test_no_claim_promotion(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage_p2_nonlocal_kernel_derivation",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage9c_regularized_integrand",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stage11b_subtraction_dry_run",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "term": "Im log(-Box - i epsilon) nonlocal kernel",
                    "scaffold_only": True,
                }
            ]
        },
    )

    report = run_stage_p3_nonlocal_form_construction()
    assert report["promotes_claims"] is False
    for entry in report["candidates_constructed"]:
        assert entry["promotes_claims"] is False
        assert entry["candidate"]["promotes_claims"] is False
    for entry in report["blocked_targets"]:
        assert entry["promotes_claims"] is False
