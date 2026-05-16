"""Stage 3F external audit gate."""

from typing import Dict, List


def run_stage3f_external_audit() -> Dict[str, object]:
    stage4_scope: List[str] = [
        "controlled toy integrals",
        "known benchmark integrals",
        "diagram-subset exploratory attempts",
        "no GRUT claim promotion",
    ]
    return {
        "stage": "3F",
        "status": "external_audit_ready",
        "audit_manifest_complete": True,
        "capability_matrix_complete": True,
        "refusal_report_available": True,
        "reproducibility_bundle_available": True,
        "can_compute_3loop": False,
        "promotes_claims": False,
        "ready_for_stage4_attempts": True,
        "stage4_allowed_scope": stage4_scope,
    }
