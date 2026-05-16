"""Tensor-heavy native attempt topology for Stage 5C."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TensorNativeAttemptTopology:
    topology_id: str
    loop_order: int
    background: str
    tensor_depth: str
    native_attempt: bool


def select_tensor_native_topology() -> TensorNativeAttemptTopology:
    return TensorNativeAttemptTopology(
        topology_id="s4_3loop_mixed_tensor_native_deep",
        loop_order=3,
        background="S4",
        tensor_depth="enhanced",
        native_attempt=True,
    )
