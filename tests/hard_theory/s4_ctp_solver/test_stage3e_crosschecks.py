from grut.hard_theory.s4_ctp_solver.crosscheck_registry import crosscheck_registry
from grut.hard_theory.s4_ctp_solver.crosscheck_routes import (
    compute_via_heat_kernel,
    compute_via_spectral_sum,
    compute_via_flat_limit,
    compute_via_ward_identity,
)
from grut.hard_theory.s4_ctp_solver.consistency_metrics import (
    compare_symbolic_forms,
    compare_limit_behavior,
    compare_scheme_metadata,
)
from grut.hard_theory.s4_ctp_solver.crosscheck_audit import run_crosscheck
from grut.hard_theory.s4_ctp_solver.stage3e_crosscheck_audit import (
    run_stage3e_crosscheck_audit,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_registry_contains_quantities():
    registry = crosscheck_registry()
    assert len(registry) >= 2
    assert all(len(entry.available_routes) >= 2 for entry in registry.values())


def test_route_results_metadata_and_status():
    quantity_id = "scalar_1loop_effective_action"
    heat = compute_via_heat_kernel(quantity_id, {})
    spectral = compute_via_spectral_sum(quantity_id, {})
    flat = compute_via_flat_limit(quantity_id, {})
    ward = compute_via_ward_identity(quantity_id, {})

    for result in (heat, spectral, flat, ward):
        assert result.can_promote is False
        assert result.scheme
        assert result.regulator

    assert heat.status in {"benchmark", "partial"}
    assert spectral.status == "partial"
    assert flat.status in {"structural_only", "benchmark"}
    assert ward.status == "structural_only"


def test_consistency_metrics_behavior():
    quantity_id = "scalar_1loop_effective_action"
    heat = compute_via_heat_kernel(quantity_id, {})
    spectral = compute_via_spectral_sum(quantity_id, {})
    flat = compute_via_flat_limit(quantity_id, {})

    sym = compare_symbolic_forms(heat, spectral)
    limit = compare_limit_behavior(heat, flat)
    scheme = compare_scheme_metadata(heat, flat)

    assert sym["status"] in {"consistent", "inconclusive"}
    assert limit["status"] in {"consistent", "inconclusive"}
    assert scheme["status"] in {"consistent", "inconsistent"}


def test_crosscheck_audit_refuses_promotion():
    report = run_crosscheck("scalar_1loop_effective_action")
    assert report["promotes_claims"] is False
    assert report["overall_status"] != "computed"


def test_stage3e_audit_gate():
    report = run_stage3e_crosscheck_audit()
    assert report["can_compute_3loop"] is False
    assert report["promotes_claims"] is False


def test_pipeline_stage3e_status_and_prior_stages():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    stage3d = pipeline.run_stage3d_scheme_audit()
    stage3e = pipeline.run_stage3e_crosscheck_audit()

    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"
    assert stage3e["status"] == "crosscheck_audit"


def test_no_full_three_loop_claims_in_stage3e():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage3e_crosscheck_audit()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
