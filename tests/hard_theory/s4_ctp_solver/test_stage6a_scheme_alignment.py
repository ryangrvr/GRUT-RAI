from grut.hard_theory.s4_ctp_solver.scheme_definition import (
    define_reference_scheme,
)
from grut.hard_theory.s4_ctp_solver.scheme_alignment_engine import (
    align_to_scheme,
)
from grut.hard_theory.s4_ctp_solver.scheme_consistency_checks import (
    check_scheme_consistency,
)
from grut.hard_theory.s4_ctp_solver.scheme_alignment_report import (
    generate_scheme_alignment_report,
)
from grut.hard_theory.s4_ctp_solver.stage6a_scheme_alignment import (
    run_stage6a_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_scheme_definition_exists():
    scheme = define_reference_scheme()
    assert scheme["scheme_id"]
    assert scheme["regulator"]
    assert scheme["invariant_basis"]
    assert scheme["promotes_claims"] is False


def test_alignment_maps_structures_and_tags():
    scheme = define_reference_scheme()
    result = {"topology_id": "t1", "expression": "Euler_density + R_squared"}
    aligned = align_to_scheme(result, scheme)
    assert aligned["status"] == "aligned_structural"
    assert aligned["aligned_terms"]
    assert aligned["scheme_tags"]
    assert aligned["promotes_claims"] is False


def test_alignment_does_not_compute_coefficients():
    scheme = define_reference_scheme()
    aligned = align_to_scheme({"topology_id": "t1", "expression": "Euler_density"}, scheme)
    assert all("UNDEFINED" not in term["term"] for term in aligned["aligned_terms"])


def test_cross_topology_consistency_runs():
    aligned_results = [
        {
            "aligned_terms": [
                {"invariant": "Euler_density"},
                {"invariant": "R_squared"},
            ]
        },
        {"aligned_terms": [{"invariant": "Euler_density"}]},
    ]
    consistency = check_scheme_consistency(aligned_results)
    assert consistency["status"] in {"consistent", "partial", "inconsistent"}
    assert "Euler_density" in consistency["consistent_terms"]
    assert "R_squared" in consistency["fragile_terms"]


def test_report_generated():
    scheme = define_reference_scheme()
    aligned_results = [{"aligned_terms": [{"invariant": "Euler_density"}]}]
    consistency = check_scheme_consistency(aligned_results)
    report = generate_scheme_alignment_report(scheme, aligned_results, consistency)
    assert report["report_type"] == "scheme_alignment"
    assert report["promotes_claims"] is False


def test_stage6a_flags_and_guard():
    report = run_stage6a_scheme_alignment()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6a_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage5d_before = pipeline.run_stage5d_candidate_readiness()
    _ = pipeline.run_stage6a_scheme_alignment()
    stage5d_after = pipeline.run_stage5d_candidate_readiness()
    assert stage5d_before["status"] == stage5d_after["status"]


def test_no_full_three_loop_claims_in_stage6a():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6a_scheme_alignment()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
