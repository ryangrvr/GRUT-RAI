"""Assemble the R route terminal audit package."""

from typing import Dict


def build_r_route_terminal_audit(
    stage12a: Dict[str, object],
    stage12b: Dict[str, object],
    stage12c: Dict[str, object],
    stage12d: Dict[str, object],
    stage12e: Dict[str, object],
    stage12f: Dict[str, object],
    ledger: Dict[str, object],
) -> Dict[str, object]:
    return {
        "candidate_buckets": stage12a.get("registry", {}).get("candidate_buckets", {}),
        "scheme_stability_audit": stage12b.get("audit", {}),
        "r_legality_gate": stage12c,
        "r_symbolic_attempt": stage12d,
        "r_result_classification": stage12e,
        "r_status_report": stage12f,
        "blocker_ledger": ledger,
        "next_required_action": stage12f.get("next_required_action"),
        "promotes_claims": False,
    }
