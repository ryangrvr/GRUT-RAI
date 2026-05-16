"""Schema definition for coefficient candidate metadata."""

from typing import List


def required_candidate_metadata_fields() -> List[str]:
    return [
        "tensor_origin_class",
        "loop_order",
        "regulator_dependence_class",
        "renormalization_structure",
        "invariant_class",
        "locality_class",
        "scheme_class_source",
        "cancellation_inputs_available",
    ]
