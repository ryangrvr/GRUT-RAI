"""Native attempt topology set for Stage 5B."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class NativeAttemptTopologyEntry:
    topology_id: str
    loop_order: int
    background: str
    topology_type: str
    native_attempt: bool


def get_native_attempt_topology_set() -> List[NativeAttemptTopologyEntry]:
    return [
        NativeAttemptTopologyEntry(
            topology_id="s4_3loop_scalar_triple_bubble_native_attempt",
            loop_order=3,
            background="S4",
            topology_type="scalar_factorizable",
            native_attempt=True,
        ),
        NativeAttemptTopologyEntry(
            topology_id="s4_scalar_bubble_bubble_curvature_insertion",
            loop_order=3,
            background="S4",
            topology_type="scalar_curvature",
            native_attempt=True,
        ),
        NativeAttemptTopologyEntry(
            topology_id="s4_scalar_tensor_structural_native_attempt",
            loop_order=3,
            background="S4",
            topology_type="mixed_structural",
            native_attempt=True,
        ),
    ]
