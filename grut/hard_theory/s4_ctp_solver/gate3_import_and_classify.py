"""Gate 3 workflow: import Mathematica JSONs, land coefficients, classify quotient."""

from __future__ import annotations

import argparse
from typing import Any, Dict

from grut.hard_theory.s4_ctp_solver.gate3_coefficient_landing import (
    land_gate3_coefficients,
)
from grut.hard_theory.s4_ctp_solver.gate3_mathematica_import import (
    import_mathematica_coefficient,
)
from grut.hard_theory.s4_ctp_solver.gate3_r_quotient_classifier import (
    classify_gate3_r_quotient,
)


def run_gate3_import_and_classify(
    *,
    cosmo_json_path: str,
    final_json_path: str,
    replicated: bool = False,
) -> Dict[str, Any]:
    cosmo_import = import_mathematica_coefficient(cosmo_json_path)
    final_import = import_mathematica_coefficient(final_json_path)

    if not cosmo_import["accepted"] or not final_import["accepted"]:
        return {
            "coefficient_statuses": {
                "C_Euler_cosmo": cosmo_import["status"],
                "C_Euler_final": final_import["status"],
            },
            "imports": {
                "C_Euler_cosmo": cosmo_import,
                "C_Euler_final": final_import,
            },
            "landing": {
                "accepted": False,
                "status": "rejected",
                "reason": "import_rejected",
            },
            "classification": {
                "classification": "blocked",
                "R_3loop": None,
                "reason": "invalid_or_rejected_input_artifact",
                "promotes_claims": False,
            },
            "promotes_claims": False,
        }

    cosmo = cosmo_import["result"]
    final = final_import["result"]
    landing = land_gate3_coefficients(cosmo=cosmo, final=final)

    if not landing.get("accepted"):
        return {
            "coefficient_statuses": {
                "C_Euler_cosmo": cosmo.status,
                "C_Euler_final": final.status,
            },
            "imports": {
                "C_Euler_cosmo": cosmo_import,
                "C_Euler_final": final_import,
            },
            "landing": landing,
            "classification": {
                "classification": "blocked",
                "R_3loop": None,
                "reason": "landing_rejected",
                "promotes_claims": False,
            },
            "promotes_claims": False,
        }

    if landing.get("status") == "blocked":
        classification = {
            "classification": "blocked",
            "R_3loop": None,
            "reason": "coefficient_blocked",
            "promotes_claims": False,
        }
    else:
        classification = classify_gate3_r_quotient(
            cosmo=cosmo,
            final=final,
            replicated=replicated,
        )

    return {
        "coefficient_statuses": {
            "C_Euler_cosmo": cosmo.status,
            "C_Euler_final": final.status,
        },
        "imports": {
            "C_Euler_cosmo": cosmo_import,
            "C_Euler_final": final_import,
        },
        "landing": landing,
        "classification": classification,
        "promotes_claims": False,
    }


def print_gate3_import_and_classify(report: Dict[str, Any]) -> None:
    print("Gate3 import-and-classify report")
    print("Coefficient statuses:", report["coefficient_statuses"])
    print("Landing status:", report["landing"].get("status"), report["landing"].get("reason"))
    print("Quotient classification:", report["classification"].get("classification"))

    r_3loop = report["classification"].get("R_3loop")
    if r_3loop is not None and report["classification"].get("classification") == "computed_candidate":
        print("R_3loop:", r_3loop)
        comparison = report["classification"].get("comparison", {})
        print("Comparison sqrt(4/3):", comparison.get("sqrt_4_over_3"))
        print("Comparison 1.15428:", comparison.get("loop_target_1_15428"))
        print("Comparison Osborn/local RG:", comparison.get("osborn_local_rg"))


def _main() -> None:
    parser = argparse.ArgumentParser(description="Import Gate 3 Mathematica coefficients and classify quotient.")
    parser.add_argument("cosmo", nargs="?", help="Path to C_Euler_cosmo JSON")
    parser.add_argument("final", nargs="?", help="Path to C_Euler_final JSON")
    parser.add_argument("--cosmo", dest="cosmo_opt", help="Path to C_Euler_cosmo JSON")
    parser.add_argument("--final", dest="final_opt", help="Path to C_Euler_final JSON")
    parser.add_argument("--replicated", action="store_true", help="Mark as independently replicated")
    args = parser.parse_args()

    cosmo_path = args.cosmo_opt or args.cosmo
    final_path = args.final_opt or args.final
    if not cosmo_path or not final_path:
        parser.error("Provide cosmo and final JSON paths as positional args or with --cosmo/--final.")

    report = run_gate3_import_and_classify(
        cosmo_json_path=cosmo_path,
        final_json_path=final_path,
        replicated=args.replicated,
    )
    print_gate3_import_and_classify(report)


if __name__ == "__main__":
    _main()
