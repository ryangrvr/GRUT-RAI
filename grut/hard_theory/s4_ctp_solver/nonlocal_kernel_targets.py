"""Define targets for nonlocal anomaly kernel derivation."""

from typing import Dict, List


_TARGETS = [
    {
        "source_type": "Im_log_minus_box_i_epsilon",
        "required_inputs": [
            "ctp_imaginary_markers",
            "nonlocal_kernel_structure",
            "regulator_tracking",
        ],
        "expected_nonlocal_form": "Im log(-Box - i epsilon)",
        "causal_structure_required": True,
    },
    {
        "source_type": "R_log_box_R",
        "required_inputs": [
            "nonlocal_kernel_structure",
            "anomaly_channel_evidence",
            "regulator_tracking",
        ],
        "expected_nonlocal_form": "R log(Box) R",
        "causal_structure_required": False,
    },
    {
        "source_type": "Weyl_log_box_Weyl",
        "required_inputs": [
            "nonlocal_kernel_structure",
            "anomaly_channel_evidence",
            "regulator_tracking",
        ],
        "expected_nonlocal_form": "Weyl log(Box) Weyl",
        "causal_structure_required": False,
    },
    {
        "source_type": "CTP_Keldysh_causal_response_kernel",
        "required_inputs": [
            "ctp_imaginary_markers",
            "causal_response_structure",
            "regulator_tracking",
        ],
        "expected_nonlocal_form": "CTP/Keldysh causal response kernel",
        "causal_structure_required": True,
    },
]


def define_nonlocal_kernel_targets() -> List[Dict[str, object]]:
    targets: List[Dict[str, object]] = []
    for target in _TARGETS:
        targets.append({**target, "status": "target_defined", "promotes_claims": False})
    return targets
