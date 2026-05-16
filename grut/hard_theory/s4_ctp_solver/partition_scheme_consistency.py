"""Scheme consistency checks across partition attempts."""

from typing import Dict, List


def check_partition_scheme_consistency(attempts: List[Dict[str, object]]) -> Dict[str, object]:
    mismatches: List[str] = []
    scheme_ids = [attempt.get("scheme_id") for attempt in attempts]
    default_regs = [attempt.get("default_regulator") for attempt in attempts]

    if any(scheme_id is None for scheme_id in scheme_ids):
        mismatches.append("missing_scheme_id")
    if any(default_regulator is None for default_regulator in default_regs):
        mismatches.append("missing_default_regulator")

    scheme_id_set = {scheme_id for scheme_id in scheme_ids if scheme_id is not None}
    if len(scheme_id_set) > 1:
        mismatches.append("scheme_id_mismatch")

    default_reg_set = {reg for reg in default_regs if reg is not None}
    if len(default_reg_set) > 1:
        mismatches.append("default_regulator_mismatch")

    return {
        "scheme_consistent": not mismatches,
        "mismatches": mismatches,
        "promotes_claims": False,
    }
