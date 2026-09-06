"""Run the registered SECTOR-SELECTION FIREWALL (Phase 3) and write reports.

Scope: algorithmic-organization study ONLY. This is NOT a causal-emergence
test and does not touch the reducibility gate or any frozen artifact.

Outputs (committed together):
  rrt0/reports/SECTOR_SELECTION_FIREWALL.json
  rrt0/RRT0_SECTOR_SELECTION_FIREWALL.md
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rrt0.sector_firewall import (  # noqa: E402
    CONTROLS, K, NB, aggregate, registered_conditions, run_firewall, verdict,
)

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUTCOME_LABELS = {
    "STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE",
    "NO_STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE_DETECTED",
    "SECTOR_SELECTION_DIAGNOSTIC_FAILED",
    "SECTOR_SELECTION_UNRESOLVED",
}
CLAIM_FIREWALL = "IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE"


def sha256(path):
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    conds = registered_conditions()
    results, conds = run_firewall(conds)
    agg = aggregate(results)
    outcome = verdict(agg)
    assert outcome in OUTCOME_LABELS, outcome

    report = {
        "report": "SECTOR_SELECTION_FIREWALL",
        "phase": 3,
        "scope": ("algorithmic-organization study; NOT a causal-emergence "
                  "test; does not modify the reducibility gate or any frozen "
                  "artifact"),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "registered_constants": {
            "N_basis_operators": NB,
            "K_registered": K,
            "conditions": conds,
        },
        "controls": {name: {"threshold": thr, "mode": mode}
                     for name, mode, thr in CONTROLS},
        "per_condition": results,
        "aggregate": agg,
        "outcome": outcome,
        "claim_firewall": CLAIM_FIREWALL,
        "interpretation_limit": (
            "A favorable result means only that the frozen discovery "
            "procedure identified a reproducible pattern among candidate "
            "operator-response clusters that survived the registered split, "
            "seed, k, epsilon, basis, permutation, null, and held-out "
            "controls. It does NOT mean the model generated physical "
            "sectors, causal structure, observers, geometry, spacetime, or "
            "any new physical primitive."),
    }
    OUT_PATH = REPORTS / "SECTOR_SELECTION_FIREWALL.json"
    REPORTS.mkdir(exist_ok=True)
    OUT_PATH.write_text(json.dumps(report, indent=2) + "\n")

    md = render_md(report, OUT_PATH)
    (ROOT / "RRT0_SECTOR_SELECTION_FIREWALL.md").write_text(md)

    print(f"outcome: {outcome}")
    print(f"controls passed: {agg['n_pass']}/{agg['n_total']}")
    for k, v in agg.get("summary", {}).items():
        print(f"  {k}: worst={v['worst_case']:.4f} "
              f"thr={v['threshold']} pass={v['pass']}")
    print(f"claim firewall: {CLAIM_FIREWALL}")
    return 0


def render_md(report, json_path):
    agg = report["aggregate"]
    lines = [
        "# RRT0 — Sector-Selection Firewall (Phase 3)",
        "",
        "## Scope",
        "",
        "This is an **algorithmic-organization study**, not a causal-emergence "
        "test. It asks one narrow, pre-registered question:",
        "",
        "> Can a pre-registered clustering pipeline identify stable "
        "algorithmic organization in response data without "
        "discovery/evaluation leakage or representation-dependent "
        "self-validation?",
        "",
        "The established model-class ceiling stands unconditionally and is "
        "not modified, weakened, bypassed, or excepted by anything below:",
        "",
        "```",
        "IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE",
        "```",
        "",
        "## Registered pipeline",
        "",
        f"- Basis operators: NB = {NB}; registered partition k = K = {K}.",
        "- Discovery matrix: row a = perturbation sigma_a, entry b = "
        "|Tr[B_b · Delta]| with Delta from the canonical `e_alpha` "
        "intervention propagated by route-A `evolve_delta`.",
        "- Controls: discovery/evaluation split (B1), standardized-basis "
        "representation (B2), neighboring-k (B3), epsilon ladder (B4), "
        "seed/replicate (B5), label-permutation null (B6), held-out states "
        "(B7).",
        "",
        "## Registered conditions",
        "",
        "```json",
        json.dumps(report["registered_constants"]["conditions"], indent=2),
        "```",
        "",
        "## Results",
        "",
    ]
    if "summary" in agg:
        lines += ["| control | threshold | worst case | pass |",
                  "|---|---|---|---|"]
        for name, v in agg["summary"].items():
            lines.append(f"| {name} | {v['threshold']} | "
                         f"{v['worst_case']:.6f} | {v['pass']} |")
        lines.append("")
    lines += [
        f"**Outcome: `{report['outcome']}`** "
        f"(controls passed: {agg['n_pass']}/{agg['n_total']})",
        "",
        "## Interpretation limit",
        "",
        report["interpretation_limit"],
        "",
        "## Provenance",
        "",
        f"- Machine-readable report: `reports/"
        f"SECTOR_SELECTION_FIREWALL.json` (sha256 `{sha256(json_path)}`).",
        f"- Generated: {report['generated_utc']}",
        "- Frozen artifacts untouched: `RRT0_FREEZE.json`, "
        "`RRT0_INPUT_LEDGER.json`, `RRT0_E_ALPHA_SEMANTIC_DECISION.md`, "
        "`Phi_raw`, reducibility gate and its results.",
        "- No geometry reconstruction, continuum/IR, gravity, cosmology, QG, "
        "Standard Model, or ToE program was run.",
        "",
        "## Claim firewall (unconditional)",
        "",
        "```",
        CLAIM_FIREWALL,
        "```",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
