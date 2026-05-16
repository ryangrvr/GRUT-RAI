"""Run coefficient assembly dry-run."""

from typing import Dict, List


def run_coefficient_assembly_dry_run(
    registry: Dict[str, object],
    rules: Dict[str, object],
) -> Dict[str, object]:
    buckets = list(registry.get("candidate_buckets", {}).values())

    return {
        "assembly_status": "dry_run_only",
        "candidate_buckets": buckets,
        "c_final_computed": False,
        "c_cosmo_computed": False,
        "r_computed": False,
        "physical_coefficients_computed": False,
        "rules_id": rules.get("rules_id"),
        "promotes_claims": False,
    }
