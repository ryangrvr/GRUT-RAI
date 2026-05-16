"""Finite-part benchmark library (non-native)."""

from typing import Dict, List


def define_finite_part_benchmarks() -> List[Dict[str, object]]:
    return [
        {
            "benchmark_id": "scalar_tadpole_finite_v1",
            "input_expression": "tadpole_finite_structure",
            "known_pole": "A/epsilon",
            "known_finite_part": "B_tadpole",
            "scheme": "dimensional_regularization_placeholder",
            "status": "known_finite_part_benchmark",
            "promotes_claims": False,
        },
        {
            "benchmark_id": "log_integral_finite_v1",
            "input_expression": "log_integral_finite_structure",
            "known_pole": "A/epsilon",
            "known_finite_part": "B_log",
            "scheme": "dimensional_regularization_placeholder",
            "status": "known_finite_part_benchmark",
            "promotes_claims": False,
        },
        {
            "benchmark_id": "pole_plus_finite_v1",
            "input_expression": "A/epsilon + B",
            "known_pole": "A/epsilon",
            "known_finite_part": "B",
            "scheme": "dimensional_regularization_placeholder",
            "status": "known_finite_part_benchmark",
            "promotes_claims": False,
        },
    ]
