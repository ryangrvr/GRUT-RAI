"""Define requirements for nonlocal anomaly-protected sources."""

from typing import Dict, List


_SOURCE_TYPES = [
    "R_log_box_R",
    "Weyl_log_box_Weyl",
    "Im_log_minus_box_i_epsilon",
    "CTP_Keldysh_causal_response_kernel",
    "anomaly_induced_nonlocal_finite_term",
]


_ACCEPTANCE_TESTS = [
    "nonlocal_kernel_present",
    "anomaly_channel_derivation_present",
    "regulator_cancellation_trace_present",
    "local_counterterm_nonmixing_verified",
    "ward_ctp_consistency_verified",
    "finite_coefficient_extractable",
    "independent_replication_target_defined",
]


def acceptance_tests() -> List[str]:
    return list(_ACCEPTANCE_TESTS)


def required_source_types() -> List[str]:
    return list(_SOURCE_TYPES)


def build_source_requirement(source_type: str) -> Dict[str, object]:
    return {
        "source_type": source_type,
        "required_derivation": "defined_in_nonlocal_anomaly_derivation_plan",
        "required_inputs": [
            "nonlocal_kernel_structure",
            "anomaly_channel_evidence",
            "ctp_causal_structure",
            "regulator_tracking",
            "ward_identity_validation",
        ],
        "acceptance_tests": acceptance_tests(),
        "scheme_protection_condition": "nonlocal_anomaly_channel_protected",
        "failure_modes": [
            "local_counterterm_mixing",
            "regulator_dependence",
            "ward_inconsistency",
            "ctp_causal_violation",
            "finite_part_unavailable",
        ],
        "status": "not_derived",
        "promotes_claims": False,
    }
