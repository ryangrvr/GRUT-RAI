import sympy as sp

from grut.hard_theory.s4_ctp_solver.diagram_topologies import stage3_topologies
from grut.hard_theory.s4_ctp_solver.asymptotic_expansions import (
    large_radius_expansion,
    small_curvature_expansion,
    heat_kernel_truncated_expansion,
    flat_limit_projection,
)
from grut.hard_theory.s4_ctp_solver.stage3_audit import run_stage3_partial_audit
from grut.hard_theory.s4_ctp_solver.ward_audit import audit_scheme_consistency
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def _partials():
    topologies = stage3_topologies()
    return [large_radius_expansion(t, order=2) for t in topologies]


def test_topology_count_and_loop_order():
    topologies = stage3_topologies()
    assert len(topologies) >= 6
    assert all(t.loop_order == 3 for t in topologies)


def test_topology_status():
    topologies = stage3_topologies()
    assert all(t.status == "represented_not_evaluated" for t in topologies)


def test_partials_status_and_omissions():
    partials = _partials()
    assert all(p.status == "speculative_internal" for p in partials)
    assert all(p.omitted_terms for p in partials)


def test_partials_scheme_and_regulator_metadata():
    partials = _partials()
    assert all(p.scheme_label for p in partials)
    assert all(p.regulator_label for p in partials)


def test_expansion_functions_return_speculative():
    topology = stage3_topologies()[0]
    assert large_radius_expansion(topology, order=2).status == "speculative_internal"
    assert small_curvature_expansion(topology, order=2).status == "speculative_internal"
    assert heat_kernel_truncated_expansion(topology, max_a_n=2).status == "speculative_internal"
    assert flat_limit_projection(topology).status == "speculative_internal"


def test_ward_audits_never_promote():
    partial = _partials()[0]
    report = audit_scheme_consistency(partial)
    assert report["promotes_claim"] is False


def test_stage3_audit_gate():
    partials = _partials()
    report = run_stage3_partial_audit(partials)
    assert report["can_promote"] is False
    assert report["status"] == "speculative_internal"


def test_pipeline_stage3_status_and_stage2_unchanged():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"


def test_no_full_three_loop_claims():
    pipeline = S4CTPPipeline()
    stage3 = pipeline.run_stage3_partials()
    assert "computed" not in str(stage3).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
