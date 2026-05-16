"""Build the terminal audit report for the R route."""

from typing import Dict


def build_r_route_terminal_report(
    stage12e: Dict[str, object],
    stage12f: Dict[str, object],
    ledger: Dict[str, object],
) -> Dict[str, object]:
    return {
        "stage": "12G",
        "status": "r_route_terminal_audit",
        "r_physical_result": False,
        "r_publishable": False,
        "r_claim_allowed": False,
        "terminal_classification": stage12e.get("classification"),
        "blockers": ledger.get("blockers", []),
        "next_required_action": stage12f.get("next_required_action"),
        "promotes_claims": False,
    }
