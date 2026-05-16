"""Build the Stage 12E R result classification report."""

from typing import Dict


def build_r_result_report(
    classification: Dict[str, object],
    analysis: Dict[str, object],
) -> Dict[str, object]:
    return {
        "stage": "12E",
        "status": "r_result_classification",
        "classification": classification.get("classification"),
        "r_physical_result": False,
        "can_publish_r": False,
        "can_claim_r": False,
        "next_required_action": analysis.get("next_required_action"),
        "promotes_claims": False,
    }
