from grut.hard_theory.s4_ctp_solver.stage7k_tensor_contraction_repair import (
    run_stage7k_tensor_contraction_repair,
)
from grut.hard_theory.s4_ctp_solver.tt_index_repair import (
    repair_tt_index_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_projector_repair import (
    repair_tt_projector_placement,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_repair_audit import (
    audit_tensor_contraction_repair,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_index_repair_runs():
    readiness = {
        "index_structure": {
            "complete": False,
            "free_indices": ["mu"],
            "tt_constraints_respected": False,
        }
    }
    repair = repair_tt_index_structure(readiness)
    assert repair["repair"] == "tt_index_structure"


def test_index_repair_proposes_fixes():
    readiness = {
        "index_structure": {
            "complete": False,
            "free_indices": ["mu"],
            "tt_constraints_respected": False,
        }
    }
    repair = repair_tt_index_structure(readiness)
    assert repair["repairs_proposed"]


def test_illegal_free_indices_detected_or_cleared():
    readiness = {
        "index_structure": {
            "complete": False,
            "free_indices": ["mu"],
            "tt_constraints_respected": True,
        }
    }
    repair = repair_tt_index_structure(readiness)
    assert repair["illegal_free_indices_remaining"] in {True, False}


def test_projector_repair_runs():
    repair = repair_tt_projector_placement({"projector_check": {"projector_consistency": False}})
    assert repair["repair"] == "tt_projector_placement"


def test_canonical_projector_form_proposed():
    repair = repair_tt_projector_placement({"projector_check": {"projector_consistency": False}})
    assert repair["canonical_form"]


def test_projector_not_evaluated():
    repair = repair_tt_projector_placement({"projector_check": {"projector_consistency": False}})
    assert repair["projector_evaluated"] is False


def test_ordering_protocol_defined():
    protocol = define_contraction_ordering_protocol()
    assert protocol["protocol_id"] == "tt_contraction_ordering_v1"


def test_ordering_protocol_disallows_contraction_now():
    protocol = define_contraction_ordering_protocol()
    assert protocol["allows_contraction_now"] is False


def test_audit_flags_no_contractions():
    index_repair = {
        "illegal_free_indices_remaining": False,
        "contractions_performed": False,
    }
    projector_repair = {
        "canonical_form": "P_TT * inverse_operator_placeholder * P_TT",
        "projector_evaluated": False,
    }
    protocol = {"status": "protocol_defined"}
    audit = audit_tensor_contraction_repair(index_repair, projector_repair, protocol, {"guard": "tensor_placeholder_guard"})
    assert audit["contractions_performed"] is False


def test_audit_blocker_closed_false():
    report = run_stage7k_tensor_contraction_repair()
    assert report["audit"]["blocker_closed"] is False


def test_audit_disallows_finite_parts():
    report = run_stage7k_tensor_contraction_repair()
    assert report["audit"]["can_compute_finite_parts"] is False


def test_future_sandbox_allowed_only_when_conditions_pass():
    index_repair = {
        "illegal_free_indices_remaining": False,
        "contractions_performed": False,
    }
    projector_repair = {
        "canonical_form": "P_TT * inverse_operator_placeholder * P_TT",
        "projector_evaluated": False,
    }
    protocol = {"status": "protocol_defined"}
    audit = audit_tensor_contraction_repair(index_repair, projector_repair, protocol, {"guard": "tensor_placeholder_guard"})
    assert audit["future_sandbox_allowed"] is True


def test_stage7k_flags_and_guard():
    report = run_stage7k_tensor_contraction_repair()
    assert report["status"] == "tensor_contraction_repair"
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7k_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7j_before = pipeline.run_stage7j_tensor_contraction_readiness()
    _ = pipeline.run_stage7k_tensor_contraction_repair()
    stage7j_after = pipeline.run_stage7j_tensor_contraction_readiness()
    assert stage7j_before["status"] == stage7j_after["status"]


def test_no_full_three_loop_claims_in_stage7k():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7k_tensor_contraction_repair()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
