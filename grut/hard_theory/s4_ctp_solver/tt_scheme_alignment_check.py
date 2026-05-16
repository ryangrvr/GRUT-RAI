"""Scheme alignment check for TT renormalization dry-run."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.counterterms import counterterm_registry
from grut.hard_theory.s4_ctp_solver.scheme_definition import define_reference_scheme


def check_tt_scheme_alignment(plan: Dict[str, object]) -> Dict[str, object]:
    scheme = define_reference_scheme()
    registry = counterterm_registry()
    required = set(plan.get("subtractions_required", []))

    scheme_protected_terms: List[str] = []
    scheme_fragile_terms: List[str] = []
    for key in required:
        record = registry.get(key)
        if record is None:
            continue
        if record.scheme_dependence.startswith("topological"):
            scheme_protected_terms.append(record.invariant)
        else:
            scheme_fragile_terms.append(record.invariant)

    basis = set(scheme.get("invariant_basis", []))
    required_invariants = set(scheme_protected_terms + scheme_fragile_terms)

    if basis and required_invariants == basis:
        alignment = "consistent"
    elif scheme_protected_terms or scheme_fragile_terms:
        alignment = "partial"
    else:
        alignment = "incomplete"

    return {
        "scheme_alignment": alignment,
        "scheme_fragile_terms": scheme_fragile_terms,
        "scheme_protected_terms": scheme_protected_terms,
        "can_extract": False,
        "promotes_claims": False,
    }
