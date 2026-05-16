"""Acceptance tests required for protected nonlocal sources."""

from typing import List


def protected_source_acceptance_tests() -> List[str]:
    return [
        "nonlocal_kernel_present",
        "anomaly_channel_derivation_present",
        "regulator_cancellation_trace_present",
        "local_counterterm_nonmixing_verified",
        "ward_ctp_consistency_verified",
        "finite_coefficient_extractable",
        "independent_replication_target_defined",
    ]
