"""Benchmark subintegrals for controlled partial integration."""

from typing import Dict, List


def define_benchmark_subintegrals() -> List[Dict[str, object]]:
    return [
        {
            "benchmark_id": "gaussian_integral",
            "known_result": "gaussian_integral_result",
            "regulator": "dim_reg_placeholder",
            "scheme": "ms_bar_placeholder",
            "status": "known_benchmark",
        },
        {
            "benchmark_id": "dim_reg_scalar_tadpole",
            "known_result": "tadpole_pole_structure",
            "regulator": "dim_reg_placeholder",
            "scheme": "ms_bar_placeholder",
            "status": "known_benchmark",
        },
        {
            "benchmark_id": "one_loop_bubble_pole",
            "known_result": "bubble_pole_structure",
            "regulator": "dim_reg_placeholder",
            "scheme": "ms_bar_placeholder",
            "status": "known_benchmark",
        },
    ]
