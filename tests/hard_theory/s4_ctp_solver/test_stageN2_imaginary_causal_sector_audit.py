from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)


def test_detects_imaginary_log(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage6a_scheme_alignment",
        lambda: {
            "report": {
                "aligned_results": [
                    {
                        "topology_id": "t1",
                        "aligned_terms": [
                            {"invariant": "unknown", "term": "log(-Box - i eps) R"}
                        ],
                    }
                ]
            }
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage5d_candidate_readiness",
        lambda: {"candidates": []},
    )

    report = run_stageN2_imaginary_causal_sector_audit()
    assert report["protected_sources_found"] == 1
    assert report["candidate_sources"]


def test_rejects_local_counterterms(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage6a_scheme_alignment",
        lambda: {
            "report": {
                "aligned_results": [
                    {
                        "topology_id": "t1",
                        "aligned_terms": [
                            {"invariant": "R_squared", "term": "R^2"},
                            {"invariant": "box_R", "term": "box R"},
                        ],
                    }
                ]
            }
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage5d_candidate_readiness",
        lambda: {"candidates": []},
    )

    report = run_stageN2_imaginary_causal_sector_audit()
    assert report["protected_sources_found"] == 0
    assert report["candidate_sources"] == []


def test_no_r_or_claim_promotion(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage6a_scheme_alignment",
        lambda: {"report": {"aligned_results": []}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit.run_stage5d_candidate_readiness",
        lambda: {"candidates": []},
    )

    report = run_stageN2_imaginary_causal_sector_audit()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
