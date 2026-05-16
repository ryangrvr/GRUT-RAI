"""Controlled diagram fragment definition for Stage 8C."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.tt_local_contraction_fragments import (
    define_local_contraction_fragments,
)


def define_controlled_tensor_fragment() -> Dict[str, object]:
    local_fragments = define_local_contraction_fragments()

    return {
        "fragment_id": "controlled_tt_fragment_v1",
        "scope": "controlled_fragment_only",
        "local_fragments": local_fragments,
        "requires_propagator": False,
        "requires_full_diagram": False,
        "allowed_by_stage8b": True,
        "status": "controlled_fragment_defined",
        "promotes_claims": False,
    }
