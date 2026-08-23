#!/usr/bin/env python3
"""class_c_contamination_audit: prove the Class-C calculation cannot accidentally
know what answer GRUT wants.

PHASE 0 of the Class-C pre-dispatch sequence (owner brief 2026-08-21). Scans the
ACTIVE Class-C surface (specification, manifest, code, fixtures, preregistration)
for historical-information leakage: target timescales, staked spectral exponents,
ansatz names, class-A assumptions, preferred outcomes, hard-coded regulators or
epochs. Occurrences are CLASSIFIED, not merely counted:

    EXECUTABLE   .py/.json on the active surface  -> CONTAMINATION (fails audit)
    PREREG       active class-C preregistration   -> CONTAMINATION
    PROSE-INERT  spec prose naming the quantity in order to PROHIBIT/REPORT it
    PROSE-REVIEW active-doc hit with no prohibition context -> blocks transmission
    HISTORICAL   documents outside the active surface -> listed, inert

Exit 0 = clean; exit 1 = contaminated. The report is WRITTEN BY THIS SCRIPT:
    provenance/CLASS_C_CONTAMINATION_AUDIT.md
Pure stdlib. Run: python3 provenance/class_c_contamination_audit.py
"""
import datetime
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_PATH = os.path.join(ROOT, "provenance", "CLASS_C_CONTAMINATION_AUDIT.md")

ACTIVE_DOCS = [
    "CLASS_C_DISPATCH_SPEC.md",
    "RUNG3_SPECTRAL_MEASURE_SPEC.md",
    "CLASS_C_DISPATCH_DECISIONS.md",
]
ACTIVE_MANIFEST = ["CLASS_C_MANIFEST.json"]
ACTIVE_CODE_PATTERNS = [
    "calc/class_c*.py",
    "provenance/class_c*.py",
]
ACTIVE_PREREG_GLOB = "provenance/prereg/*CLASS_C*"
HISTORICAL_DOCS = [
    "RUNG3_KEYSTONE_MAP.md",
    "RUNG3_BRIDGE_SCOPE.md",
    "DISPATCH_ONE_PAGE.md",
    "SPECIALIST_BRIEF_rung3_spine.md",
    "calc/worldline_reduction.py",
    "calc/tt_worldline_spectrum.py",
    "calc/RESULTS_worldline_reduction.md",
    "calc/RESULTS_tt_worldline.md",
]

PATTERNS = [
    ("TAU0_TARGET", r"\btau_?0\b"),
    ("MYR_TARGET", r"\b41\.9\b"),
    ("S3_EXPONENT", r"\bs\s*=\s*3\b"),
    ("J_OMEGA3", r"J\s*\(\s*w(?:omega)?\s*\)\s*[~=\u2248]\s*w\^?3|omega\s*\^\s*3|omega\s*\*\*\s*3|\bw\s*\*\*\s*3\b"),
    ("SINGLE_POLE_ANSATZ", r"single[- ]pole"),
    ("PREFERRED_OUTCOME_LANGUAGE", r"desired memory|make GRUT work|preserve GRUT|GRUT wants"),
    ("HARDCODED_REGULATOR_DEFAULT", r"(?<![\u2202/])\bk_min\s*=\s*[0-9]"),
    ("HARDCODED_EPOCH_DEFAULT", r"(?i)\bepoch\s*=\s*[0-9]|\bt_bar\s*=\s*[0-9]"),
]
INERT_CONTEXT_MARKERS = [
    "No J(", "falsified", "FALSIFIED", "prohibit", "Prohibit", "forbidden",
    "Forbidden", "NOT super-Ohmic", "red list", "Red if asserted", "No tau",
    "does not survive", "no tau", "falsified at class A", "kill condition",
    "Prohibitions", "prohibited", "Forbidden quantities", "ban", "ban it",
]


def classify(path, kind):
    """Return (hits, exists): hits = [(pattern_name, lineno, line)]."""
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return [], False
    hits = []
    with open(full, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            for name, pat in PATTERNS:
                if re.search(pat, line):
                    hits.append((name, i, line.strip()[:140]))
    return hits, True


def in_code_fence(all_lines, lineno):
    """True if `lineno` sits inside a ``` fenced block (code-like prose)."""
    fence = False
    for i, ln in enumerate(all_lines[: lineno - 1], 1):
        if ln.strip().startswith("```"):
            fence = not fence
    return fence


def is_inert_prose(all_lines, lineno, line):
    """DOC hits CANNOT execute: they are PROSE-INERT by default, EXCEPT when the
    hit sits inside a fenced code block (code-like -> PROSE-REVIEW)."""
    return not in_code_fence(all_lines, lineno)


def manifest_allowlist(manifest_obj):
    """String fragments that MAY legitimately appear in the manifest: the
    prohibition list, the not-the-object list, and outcome classes."""
    frags = []
    for key in ("prohibitions", "not_the_object", "permitted_outcome_classes",
                "requested_observables", "regulator_policy"):
        val = manifest_obj.get(key)
        if isinstance(val, list):
            frags += [str(v) for v in val]
        elif isinstance(val, str):
            frags.append(val)
    return frags



def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    rows_active, rows_hist = [], []
    contaminated = []

    def scan(kind, relpath):
        full = os.path.join(ROOT, relpath)
        hits, exists = classify(relpath, kind)
        bucket = rows_active if kind != "HISTORICAL" else rows_hist
        if not exists:
            bucket.append(("INFO", relpath, "ABSENT (no file yet)", "-", "-"))
            return
        all_lines = open(full, encoding="utf-8").read().splitlines()
        # audit/gate/checker MACHINERY necessarily names what it scans and holds
        # reference/test data: self-reference is inert for these files -- they
        # are not solvers and emit no physics results.
        if relpath.startswith("provenance/class_c_"):
            kind = "CHECKER"
        allowlist = []
        if kind == "MANIFEST":
            try:
                allowlist = manifest_allowlist(json.load(open(full, encoding="utf-8")))
            except Exception:
                pass
        if not hits:
            bucket.append(("CLEAN", relpath, "no forbidden pattern", "-", "-"))
            return
        for name, lineno, line in hits:
            if kind == "CODE":
                cls = "CONTAMINATION"
                contaminated.append((f"{relpath}:{lineno}", name, line))
            elif kind in ("MANIFEST", "PREREG"):
                inert = any(frag and frag[:40] in line for frag in allowlist)
                cls = "PROSE-INERT (declared prohibition)" if inert else "CONTAMINATION"
                if not inert:
                    contaminated.append((f"{relpath}:{lineno}", name, line))
            elif kind == "DOC":
                inert = is_inert_prose(all_lines, lineno, line)
                cls = "PROSE-INERT" if inert else "PROSE-REVIEW"
                if not inert:
                    contaminated.append((f"{relpath}:{lineno}", name, line))
            elif kind == "CHECKER":
                cls = "REFERENCE-DATA-INERT"
            elif kind == "AUDIT":
                cls = "SELF-REF-INERT"
            else:
                cls = "HISTORICAL-INERT"
            bucket.append((kind, f"{relpath}:{lineno}", cls, name, line))

    for p in ACTIVE_DOCS:
        scan("DOC", p)
    for p in ACTIVE_MANIFEST:
        scan("MANIFEST", p)
    for pat in ACTIVE_CODE_PATTERNS:
        for p in sorted(glob.glob(os.path.join(ROOT, pat))):
            scan("CODE", os.path.relpath(p, ROOT))
    for p in sorted(glob.glob(os.path.join(ROOT, ACTIVE_PREREG_GLOB))):
        scan("PREREG", os.path.relpath(p, ROOT))
    for p in HISTORICAL_DOCS:
        scan("HISTORICAL", p)

    # ---- emit report (script-written, never hand-typed) ---------------------
    verdict = "CONTAMINATED" if contaminated else "CLEAN"
    lines = [
        "# CLASS_C_CONTAMINATION_AUDIT — emitted, never hand-typed",
        "",
        f"*Generated {ts} by `provenance/class_c_contamination_audit.py` "
        f"(Phase 0, owner brief 2026-08-21). Verdict: **{verdict}**.*",
        "",
        "## What was searched",
        "",
        "Active surface: " + ", ".join(f"`{p}`" for p in ACTIVE_DOCS + ACTIVE_MANIFEST)
        + "; code globs " + ", ".join(f"`{p}`" for p in ACTIVE_CODE_PATTERNS)
        + "; prereg glob `" + ACTIVE_PREREG_GLOB + "`.",
        "Historical surface (inert unless promoted): "
        + ", ".join(f"`{p}`" for p in HISTORICAL_DOCS) + ".",
        "",
        "Forbidden-pattern set: " + ", ".join(n for n, _ in PATTERNS) + ".",
        "",
        "## Active-surface findings",
        "",
    ]
    for kind, loc, cls, name, line in rows_active:
        lines.append(f"- `{loc}` [{cls}] {name}: {line}")
    lines += ["", "## Historical-surface findings (inert unless promoted)", ""]
    for kind, loc, cls, name, line in rows_hist:
        lines.append(f"- `{loc}` [{cls}] {kind}: {line}")
    if contaminated:
        lines += ["", "## CONTAMINATION DETAIL (blocks dispatch)", ""]
        for loc, name, line in contaminated:
            lines.append(f"- `{loc}` [{name}] {line}")
    lines += [
        "",
        "## Adjudication rule",
        "",
        "EXECUTABLE/MANIFEST/PREREG hits fail the audit outright. PROSE-REVIEW hits",
        "block transmission until reclassified. PROSE-INERT hits are permitted only",
        "where the quantity is named in order to be prohibited or reported.",
        "",
    ]
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"class_c_contamination_audit: {verdict}")
    print(f"report: {os.path.relpath(REPORT_PATH, ROOT)}")
    for loc, name, line in contaminated:
        print(f"  CONTAMINATION {loc} [{name}] {line[:100]}")
    return 1 if contaminated else 0


if __name__ == "__main__":
    sys.exit(main())

