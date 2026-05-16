"""Stage 3 audit gate for controlled partials."""

from typing import Dict, Iterable, List

from grut.hard_theory.s4_ctp_solver.three_loop_partials import ThreeLoopPartial


def run_stage3_partial_audit(partials: Iterable[ThreeLoopPartial]) -> Dict[str, object]:
    partial_list = list(partials)
    all_have_omitted_terms = all(bool(p.omitted_terms) for p in partial_list)
    all_refuse_promotion = all(p.status != "computed" for p in partial_list)
    all_have_scheme_metadata = all(
        bool(p.scheme_label) and bool(p.regulator_label) for p in partial_list
    )

    next_required: List[str] = [
        "explicit S4 propagators",
        "full tensor contraction",
        "renormalization/scheme matching",
        "Ward identity verification",
        "independent replication",
    ]

    return {
        "stage": 3,
        "status": "speculative_internal",
        "partials_count": len(partial_list),
        "all_have_omitted_terms": all_have_omitted_terms,
        "all_refuse_promotion": all_refuse_promotion,
        "all_have_scheme_metadata": all_have_scheme_metadata,
        "can_promote": False,
        "next_required_for_promotion": next_required,
    }
