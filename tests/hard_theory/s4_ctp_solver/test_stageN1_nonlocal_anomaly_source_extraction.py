from grut.hard_theory.s4_ctp_solver.stageN1_nonlocal_anomaly_source_extraction import (
    run_stageN1_nonlocal_anomaly_source_extraction,
)


def test_filters_local_terms(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN1_nonlocal_anomaly_source_extraction.run_stage6a_scheme_alignment",
        lambda: {
            "report": {
                "aligned_results": [
                    {
                        "topology_id": "t1",
                        "aligned_terms": [
                            {"invariant": "R_squared", "term": "R^2"},
                            {
                                "invariant": "nonlocal_R_log_box_R",
                                "term": "R log(box) R",
                            },
                        ],
                    }
                ]
            }
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN1_nonlocal_anomaly_source_extraction.run_stage5d_candidate_readiness",
        lambda: {"candidates": []},
    )

    report = run_stageN1_nonlocal_anomaly_source_extraction()
    assert report["protected_sources_found"] == 1
    assert report["candidate_sources"]


def test_no_r_or_claim_promotion(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN1_nonlocal_anomaly_source_extraction.run_stage6a_scheme_alignment",
        lambda: {"report": {"aligned_results": []}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stageN1_nonlocal_anomaly_source_extraction.run_stage5d_candidate_readiness",
        lambda: {"candidates": []},
    )

    report = run_stageN1_nonlocal_anomaly_source_extraction()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    assert report["can_build_second_protected_coefficient"] is False
