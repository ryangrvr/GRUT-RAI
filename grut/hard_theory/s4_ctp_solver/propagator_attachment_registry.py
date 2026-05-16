"""Propagator attachment registry for symbolic skeleton attachments."""

from typing import Dict, List


def build_propagator_attachment_registry() -> List[Dict[str, object]]:
    return [
        {
            "propagator_id": "scalar_conformal_s4",
            "field_type": "scalar",
            "source_stage": "6C",
            "evaluation_status": "symbolic_only",
            "allowed_attachment": True,
            "promotes_claims": False,
        },
        {
            "propagator_id": "ghost_s4_structural",
            "field_type": "ghost",
            "source_stage": "6D",
            "evaluation_status": "symbolic_only",
            "allowed_attachment": True,
            "promotes_claims": False,
        },
        {
            "propagator_id": "tt_s4_scaffold",
            "field_type": "tt_graviton",
            "source_stage": "6F",
            "evaluation_status": "scaffold_not_evaluated",
            "allowed_attachment": True,
            "promotes_claims": False,
        },
    ]
