"""Define allowed Euler-channel coefficient roles."""

from typing import Dict, List


def build_euler_coefficient_roles() -> List[Dict[str, object]]:
    return [
        {
            "role_id": "euler_numerator",
            "allowed_kernel": "R_log_box_R",
            "coefficient_symbol": "C_Euler_num",
            "coefficient_value": None,
            "source": "round_s4_euler_anomaly_channel",
        },
        {
            "role_id": "euler_denominator",
            "allowed_kernel": "R_log_box_R",
            "coefficient_symbol": "C_Euler_den",
            "coefficient_value": None,
            "source": "round_s4_euler_anomaly_channel",
        },
    ]
