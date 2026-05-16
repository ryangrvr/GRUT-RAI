"""Formal OR4 definition record for the protected R domain."""

from typing import Dict, List


def build_formal_r_definition() -> Dict[str, object]:
    domain_requirements: List[str] = [
        "round_euclidean_s4",
        "conformally_flat",
        "weyl_squared_zero",
        "euler_density_survives",
    ]

    definition_statements: List[str] = [
        "r_defined_as_protected_euler_channel_anomaly_quotient",
        "r_not_defined_as_c_cosmo_over_c_final_without_euler_mapping",
        "r_not_defined_as_im_log_over_curvature_log_without_ctp_to_euler",
    ]

    allowed_routes = [
        {
            "source_type": "R_log_box_R",
            "role": "euler_channel_anomaly_quotient",
            "notes": "Protected Euler-channel kernel candidate on round S4.",
        }
    ]

    blocked_routes = [
        {
            "source_type": "Weyl_log_box_Weyl",
            "role": "weyl_channel_blocked_on_s4",
            "reason": "weyl_zero_on_s4",
        },
        {
            "source_type": "Im_log_minus_box_i_epsilon",
            "role": "ctp_causal_kernel_blocked",
            "reason": "ctp_to_euler_bridge_missing",
        },
    ]

    return {
        "definition_id": "or4_formal_r_definition",
        "definition_domain": "round_s4_euler_anomaly_channel",
        "domain_requirements": domain_requirements,
        "definition_statements": definition_statements,
        "allowed_routes": allowed_routes,
        "blocked_routes": blocked_routes,
        "source_refs": [
            "theory/hard_theory/R_DEFINITION.md",
            "theory/ZENODO_EPSILON_IDENTIFICATION.md",
            "grut/foundation/anomaly.py",
        ],
        "promotes_claims": False,
    }
