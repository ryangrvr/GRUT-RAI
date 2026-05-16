"""Cross-topology scheme consistency checks."""

from typing import Dict, List


_PROTECTED = {"Euler_density", "Weyl_squared", "nonlocal_R_log_box_R"}
_FRAGILE = {"R_squared", "box_R"}


def check_scheme_consistency(aligned_results: List[Dict[str, object]]) -> Dict[str, object]:
    per_topology = []
    for result in aligned_results:
        invariants = {
            term.get("invariant")
            for term in result.get("aligned_terms", [])
            if term.get("invariant")
        }
        per_topology.append(invariants)

    protected_seen = set().union(*per_topology) & _PROTECTED if per_topology else set()
    fragile_seen = set().union(*per_topology) & _FRAGILE if per_topology else set()

    inconsistent_terms = []
    consistent_terms = []
    reason = "no_data"
    status = "partial"

    if per_topology:
        reason = "partial_alignment"
        for invariant in protected_seen:
            if all(invariant in inv for inv in per_topology):
                consistent_terms.append(invariant)
            else:
                inconsistent_terms.append(invariant)
        status = "consistent" if not inconsistent_terms else "partial"

    return {
        "status": status,
        "consistent_terms": consistent_terms,
        "inconsistent_terms": inconsistent_terms,
        "fragile_terms": sorted(fragile_seen),
        "reason": reason,
        "promotes_claims": False,
    }
