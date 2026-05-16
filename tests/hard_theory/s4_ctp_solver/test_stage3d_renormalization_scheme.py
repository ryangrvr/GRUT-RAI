from grut.hard_theory.s4_ctp_solver.counterterms import counterterm_registry
from grut.hard_theory.s4_ctp_solver.divergence_structure import (
    create_divergence_record,
    associate_counterterms,
)
from grut.hard_theory.s4_ctp_solver.scheme_invariants import (
    classify_scheme_sensitivity,
)
from grut.hard_theory.s4_ctp_solver.renormalization_audit import (
    audit_counterterm_coverage,
    audit_divergence_has_counterterm,
    audit_scheme_metadata_consistency,
    audit_scheme_invariant_claim,
    audit_forbidden_promotion_after_renormalization,
)
from grut.hard_theory.s4_ctp_solver.stage3d_scheme_audit import (
    run_stage3d_scheme_audit,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_counterterm_registry_complete():
    registry = counterterm_registry()
    expected = {
        "cosmological_constant_counterterm",
        "einstein_hilbert_counterterm",
        "R_squared_counterterm",
        "Ricci_squared_counterterm",
        "Riemann_squared_counterterm",
        "Euler_density_counterterm",
        "Weyl_squared_counterterm",
        "box_R_counterterm",
    }
    assert expected.issubset(set(registry.keys()))
    assert all(r.status == "registered_not_evaluated" for r in registry.values())
    assert all(r.scheme_dependence for r in registry.values())


def test_divergence_record_structures():
    record = create_divergence_record(loop_order=2, regulator="dim_reg", scheme="ms_bar")
    assert record.status == "divergence_tracked_not_renormalized"
    assert record.regulator == "dim_reg"
    assert record.scheme == "ms_bar"

    record = record.__class__(
        loop_order=record.loop_order,
        pole_structure="1/epsilon",
        associated_counterterms=record.associated_counterterms,
        regulator=record.regulator,
        scheme=record.scheme,
        subtraction_status=record.subtraction_status,
        status=record.status,
    )
    assert record.pole_structure in {"1/epsilon", "1/epsilon^2", "log_cutoff", "finite", "unknown"}


def test_associate_counterterms():
    record = create_divergence_record(loop_order=1, regulator="dim_reg", scheme="ms_bar")
    updated = associate_counterterms(record, ["Euler_density_counterterm"])
    assert updated.associated_counterterms == ["Euler_density_counterterm"]


def test_scheme_classifications():
    assert classify_scheme_sensitivity("a")["classification"] == "scheme_protected_benchmarked"
    assert classify_scheme_sensitivity("c")["classification"] == "scheme_protected_benchmarked"
    assert classify_scheme_sensitivity("box_R")["classification"] == "scheme_dependent_total_derivative"
    assert classify_scheme_sensitivity("C_Cosmo")["classification"] == "scheme_fragile_local"
    assert classify_scheme_sensitivity("C_Final")["classification"] == "scheme_protected_candidate"
    assert classify_scheme_sensitivity("R_ratio")["classification"] == "depends_on_scheme_alignment"


def test_renormalization_audits_refuse_promotion():
    record = create_divergence_record(loop_order=1, regulator="dim_reg", scheme="ms_bar")
    audits = [
        audit_counterterm_coverage(record),
        audit_divergence_has_counterterm(record),
        audit_scheme_metadata_consistency([record]),
        audit_scheme_invariant_claim(classify_scheme_sensitivity("a")),
        audit_forbidden_promotion_after_renormalization([record]),
    ]
    assert all(audit["promotes_claims"] is False for audit in audits)


def test_stage3d_audit_gate():
    report = run_stage3d_scheme_audit()
    assert report["renormalized_coefficients_present"] is False
    assert report["can_compute_3loop"] is False
    assert report["promotes_claims"] is False


def test_pipeline_stage3d_status_and_prior_stages():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    stage3d = pipeline.run_stage3d_scheme_audit()
    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"


def test_no_full_three_loop_claims_in_stage3d():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage3d_scheme_audit()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
