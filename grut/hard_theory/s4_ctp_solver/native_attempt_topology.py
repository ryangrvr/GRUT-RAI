"""Native attempt topology selection for Stage 5A."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NativeAttemptTopology:
    topology_id: str
    loop_order: int
    background: str
    topology_type: str
    native_attempt: bool


def select_native_attempt_topology() -> NativeAttemptTopology:
    return NativeAttemptTopology(
        topology_id="s4_3loop_scalar_triple_bubble_native_attempt",
        loop_order=3,
        background="S4",
        topology_type="factorizable_scalar",
        native_attempt=True,
    )
