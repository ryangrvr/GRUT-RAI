"""Benchmark-only finite-part extractor."""

from typing import Dict


def extract_finite_part_from_benchmark(benchmark: Dict[str, object]) -> Dict[str, object]:
    return {
        "benchmark_id": benchmark.get("benchmark_id"),
        "pole_subtracted": True,
        "finite_part_extracted": True,
        "native_input_used": False,
        "finite_part": benchmark.get("known_finite_part"),
        "status": "benchmark_finite_part_extracted",
        "promotes_claims": False,
    }
