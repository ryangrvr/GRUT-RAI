from grut.hard_theory.s4_ctp_solver.r_candidate_selector import (
    identify_r_candidate_pairs,
)
from grut.hard_theory.s4_ctp_solver.r_structure_compatibility import (
    check_r_structure_compatibility,
)
from grut.hard_theory.s4_ctp_solver.r_cancellation_check import check_r_cancellation
from grut.hard_theory.s4_ctp_solver.r_legality_audit import audit_r_legality_inputs
from grut.hard_theory.s4_ctp_solver.r_legality_decision import decide_r_legality


def _base_registry() -> dict:
    return {
        "candidate_buckets": {
            "nonlocal_scheme_protected_candidate": {
                "candidate_id": "nonlocal_scheme_protected_candidate_v1",
                "renorm_structure_id": "renorm_v1",
                "tensor_origin_class": "tt",
                "loop_order": 3,
                "regulator_dependence_class": "dim_reg",
                "counterterm_contamination": False,
                "protection_class": "nonlocal",
                "cancellation_ready": {
                    "divergence_cancellation": True,
                    "regulator_cancellation": True,
                    "scheme_cancellation": True,
                },
            },
            "c_cosmo_candidate": {
                "candidate_id": "c_cosmo_candidate_v1",
                "renorm_structure_id": "renorm_v1",
                "tensor_origin_class": "tt",
                "loop_order": 3,
                "regulator_dependence_class": "dim_reg",
                "counterterm_contamination": False,
                "protection_class": "anomaly_protected",
                "cancellation_ready": {
                    "divergence_cancellation": True,
                    "regulator_cancellation": True,
                    "scheme_cancellation": True,
                },
            },
        }
    }


def _base_classifications() -> dict:
    return {
        "classifications": [
            {
                "candidate_key": "nonlocal_scheme_protected_candidate",
                "classification": "scheme_protected",
            },
            {
                "candidate_key": "c_cosmo_candidate",
                "classification": "scheme_protected",
            },
        ]
    }


def test_valid_pair_case():
    pairs = identify_r_candidate_pairs(_base_classifications(), _base_registry(), {})
    eligible = [
        pair for pair in pairs["candidate_pairs"] if pair["selection_status"] == "eligible"
    ]
    assert eligible

    pair = eligible[0]
    structural = check_r_structure_compatibility(pair)
    cancellation = check_r_cancellation(pair)
    audit = audit_r_legality_inputs(pair, structural, cancellation)
    decision = decide_r_legality(pair, structural, cancellation, audit)
    assert decision["r_legal"] is True


def test_scheme_mismatch_rejection():
    registry = _base_registry()
    registry["candidate_buckets"]["c_cosmo_candidate"]["renorm_structure_id"] = "renorm_v2"
    pairs = identify_r_candidate_pairs(_base_classifications(), registry, {})
    assert all(pair["selection_status"] == "rejected" for pair in pairs["candidate_pairs"])


def test_cancellation_failure_rejection():
    registry = _base_registry()
    registry["candidate_buckets"]["c_cosmo_candidate"]["cancellation_ready"][
        "regulator_cancellation"
    ] = False
    pairs = identify_r_candidate_pairs(_base_classifications(), registry, {})
    eligible = [
        pair for pair in pairs["candidate_pairs"] if pair["selection_status"] == "eligible"
    ]
    assert eligible

    pair = eligible[0]
    cancellation = check_r_cancellation(pair)
    assert cancellation["cancellation_valid"] is False


def test_mixed_local_nonlocal_rejection():
    registry = _base_registry()
    registry["candidate_buckets"]["c_cosmo_candidate"]["protection_class"] = "local"
    pairs = identify_r_candidate_pairs(_base_classifications(), registry, {})
    assert all(pair["selection_status"] == "rejected" for pair in pairs["candidate_pairs"])