import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_tensor_spectrum import (
    tensor_mode_records,
)
from grut.hard_theory.s4_ctp_solver.tt_projector import (
    tt_projector_record,
    check_projector_structural_identities,
)
from grut.hard_theory.s4_ctp_solver.graviton_decomposition import (
    decompose_metric_perturbation_record,
    graviton_sector_components,
)
from grut.hard_theory.s4_ctp_solver.ward_tensor_checks import (
    audit_tensor_ward_structure,
    audit_ctp_branch_consistency,
    audit_graviton_decomposition_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage3c_tensor_audit import (
    run_stage3c_tensor_audit,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_tensor_spectral_records_exist():
    a = sp.symbols("a", positive=True)
    scalar_rec, vec_rec, tt_rec = tensor_mode_records(2, a)
    assert scalar_rec.mode_type == "scalar"
    assert vec_rec.mode_type == "transverse_vector"
    assert tt_rec.mode_type == "transverse_traceless_tensor"


def test_scalar_status_benchmarked():
    a = sp.symbols("a", positive=True)
    scalar_rec, _, _ = tensor_mode_records(1, a)
    assert scalar_rec.status == "benchmarked_scalar"


def test_tensor_modes_not_evaluated():
    a = sp.symbols("a", positive=True)
    _, vec_rec, tt_rec = tensor_mode_records(1, a)
    assert vec_rec.status != "benchmarked_scalar"
    assert tt_rec.status != "benchmarked_scalar"


def test_tt_projector_record_and_checks():
    record = tt_projector_record()
    checks = check_projector_structural_identities(record)
    assert record.status == "structural_projector_not_explicit"
    assert checks["promotes_claims"] is False
    assert checks["idempotence"] == "not_evaluated"


def test_graviton_decomposition_sectors():
    record = decompose_metric_perturbation_record()
    components = graviton_sector_components()
    assert "TT" in components
    assert "vector" in components
    assert "scalar_longitudinal" in components
    assert "trace" in components
    assert components["trace"].sector == "conformal_sector"
    assert components["vector"].sector == "gauge_sector"
    assert record["status"] == "structural_decomposition"


def test_ward_tensor_checks_refuse_promotion():
    assert audit_tensor_ward_structure()["promotes_claims"] is False
    assert audit_ctp_branch_consistency()["promotes_claims"] is False
    assert audit_graviton_decomposition_consistency()["promotes_claims"] is False


def test_stage3c_audit_output():
    report = run_stage3c_tensor_audit()
    assert report["can_compute_3loop"] is False
    assert report["tensor_modes_explicitly_evaluated"] is False
    assert report["next_required_for_promotion"]


def test_pipeline_stage3c_status_and_prior_stages():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"


def test_no_full_three_loop_claims_in_stage3c():
    pipeline = S4CTPPipeline()
    stage3c = pipeline.run_stage3c_tensor_audit()
    assert "computed" not in str(stage3c).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
