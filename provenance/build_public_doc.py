#!/usr/bin/env python3
"""build_public_doc: render the public document from its source, substituting every count.

THE ONE-NUMBER RULE, MADE MECHANICAL. The source (`docs/WHERE_IT_STOPS.src.md`) contains named
placeholders, never digits, for every register-derived count. This script substitutes them from
emit_public_numbers.numbers() and writes the rendered document. A test re-renders and diffs, so a
hand-edited number in the rendered file is a build failure rather than a reading error.

Why a renderer rather than "be careful": the rule is a prohibition on the BODY. Counts typed into
prose are exactly what the prior deposit got wrong at scale, and "no count is ever typed" is not a
property a person can maintain across 26,000 words -- it is a property a build step can.

Run:  python3 build_public_doc.py           print the rendered document
      python3 build_public_doc.py --write   write ../docs/WHERE_IT_STOPS.md
      python3 build_public_doc.py --check    re-render and diff against the written file
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.src.md")
OUT = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.md")

sys.path.insert(0, HERE)
import emit_public_numbers as E  # noqa: E402

TOKEN = re.compile(r"\{\{([A-Za-z_0-9]+)\}\}")


def values():
    n = E.numbers()
    v = {
        "STAMP_DATE": E.STAMP_DATE,
        "CORRECTION_DATE": E.CORRECTION_DATE,
        "WAVE_DATE": E.WAVE_DATE,
        "total": n["total"], "n_grut": n["n_grut"], "n_cluster": n["n_cluster"],
        "net_grut": f"+{n['net_grut']}", "net_cluster": f"+{n['net_cluster']}",
        "waived_total": f"+{n['waived_total']}", "n_waivers": len(n["waivers"]),
        "n_sources": n["n_sources"], "n_calcs": n["n_calcs"],
        "n_test_files": n["n_test_files"], "n_tests": n["n_tests"],
        "spec_total": n["spec_total"], "spec_nodes": n["spec_nodes"],
        "spec_A": n["spec_A"], "spec_B": n["spec_B"],
        "spec_C": n["spec_C"], "spec_D": n["spec_D"],
        "n_spec_2026_06_25_nodes": n["n_spec_2026_06_25_nodes"],
        "n_spec_2026_06_25_occurrences": n["n_spec_2026_06_25_occurrences"],
        "isw_sigma": n["isw_sigma"], "isw_central": n["isw_central"],
        "x_upper": n["x_upper"], "mu_allowance": n["mu_allowance"],
        "desi_sigma0": n["desi_sigma0"], "x_gate": n["x_gate"],
        "spec_raw_incl_annotations": n["spec_raw_incl_annotations"],
        "n_pressure_removals": n["n_pressure_removals"],
    }
    for tier in ("shown", "derived", "derived-pending", "assumed", "to-derive"):
        v["tier_" + tier.replace("-", "_")] = n["tiers"].get(tier, 0)
    return v


def render():
    with open(SRC) as f:
        src = f.read()
    vals = values()
    missing = sorted({m.group(1) for m in TOKEN.finditer(src)} - set(vals))
    if missing:
        raise SystemExit(f"source uses undefined placeholders: {missing}")
    return TOKEN.sub(lambda m: str(vals[m.group(1)]), src)


def main():
    doc = render()
    if "--check" in sys.argv:
        on_disk = open(OUT).read() if os.path.exists(OUT) else ""
        if on_disk != doc:
            print("DRIFT: WHERE_IT_STOPS.md does not match a fresh render of its source. "
                  "Never hand-edit the rendered file; edit the .src.md and rebuild.")
            return 1
        print("rendered document matches its source and the register.")
        return 0
    if "--write" in sys.argv:
        open(OUT, "w").write(doc)
        print(f"wrote {OUT}")
        return 0
    print(doc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
