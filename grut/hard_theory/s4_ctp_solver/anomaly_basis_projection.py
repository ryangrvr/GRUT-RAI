"""Project nonlocal kernels onto S4 anomaly basis channels."""

from typing import Dict


def project_kernel_to_anomaly_basis(
    source_type: str,
    s4_identities: Dict[str, object],
    off_shell_continuation: bool = False,
) -> Dict[str, object]:
    s4_weyl_zero = s4_identities.get("s4_weyl_zero") is True

    projects_to_euler = False
    projects_to_weyl = False
    survives_on_s4 = True
    blocked_reason = None

    if source_type == "R_log_box_R":
        projects_to_euler = True
        survives_on_s4 = True
    elif source_type == "Weyl_log_box_Weyl":
        projects_to_weyl = True
        survives_on_s4 = False
        if s4_weyl_zero and not off_shell_continuation:
            blocked_reason = "weyl_zero_on_s4"
    elif source_type == "Im_log_minus_box_i_epsilon":
        survives_on_s4 = True
        blocked_reason = "causal_ctp_kernel"
    else:
        survives_on_s4 = False
        blocked_reason = "unknown_kernel_source"

    return {
        "source_type": source_type,
        "projects_to_euler_channel": projects_to_euler,
        "projects_to_weyl_channel": projects_to_weyl,
        "survives_on_s4": survives_on_s4,
        "blocked_reason": blocked_reason,
        "promotes_claims": False,
    }
