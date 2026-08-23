#!/usr/bin/env python3
"""class_c_benchmark_matrix: the golden-limit matrix, emitted not hand-typed.

PHASE 5-6 of the Class-C pre-dispatch sequence (owner brief 2026-08-21).
Benchmarks must be QUANTITATIVE with explicit tolerances; a green suite
establishes only that machinery reproduces what it should.

Provenance honesty (Phase 11 principle, applied here): running the existing
calcs is a SAME-CODE RERUN, not an independent confirmation. The one cell
computed by freshly written code (different quadrature scheme, written against
the closed form only) is labelled INDEPENDENT-CODE.

Emits: provenance/CLASS_C_BENCHMARK_MATRIX.md
Exit 0 iff every APPLICABLE cell passes within tolerance.
Pure stdlib. Run: python3 provenance/class_c_benchmark_matrix.py
"""
import datetime
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "provenance", "CLASS_C_BENCHMARK_MATRIX.md")
FAILS = []


def run_calc(rel, extra=()):
    r = subprocess.run([sys.executable, os.path.join(ROOT, rel), *extra],
                       capture_output=True, text=True, timeout=600)
    return r.returncode, r.stdout + r.stderr


# ---- INDEPENDENT-CODE benchmark: fresh Simpson implementation ---------------
def fold_independent(w, Lam, n=800):
    """int_w^Lam x(x-w)/(4 pi^2) dx by Simpson -- deliberately different
    scheme from calc/worldline_reduction.py's midpoint loop.
    SUPPORT: theta-function constraints restrict x to [w, Lam].
    (2026-08-22 screen catch: the first draft integrated [0, Lam], which
    includes the unphysical x < w region and disagreed with the closed form
    at 3.5e-04 -- the disagreement was the investigation trigger.)"""
    a, b = w, Lam
    h = (b - a) / n

    def f(x):
        return (x * (x - w)) / (4.0 * math.pi * math.pi)

    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3.0


def fold_closed(w, Lam):
    return (Lam ** 3 / 3.0 - Lam ** 2 * w / 2.0 + w ** 3 / 6.0) / (4.0 * math.pi ** 2)


ROWS = []
FAILS_LIST = []


def bench(limit, component, desc, measured, expect, status, prov):
    ROWS.append((limit, component, desc, measured, status, prov))
    if status != "PASS":
        FAILS_LIST.append(f"{component} / {limit}: {status}")


def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # ---- 1. same-code rerun: worldline_reduction ---------------------------
    rc, out = run_calc("calc/worldline_reduction.py")
    errs = [float(x) for x in re.findall(r"rel\.err\s+([0-9.e+-]+)", out)]
    ok1 = rc == 0 and errs and max(errs) < 2e-3
    bench("exactly-solvable special case", "worldline_reduction (fold identity)",
          "closed form vs quadrature, max over w grid",
          f"max rel.err {max(errs):.1e}" if errs else "none parsed",
          "< 2e-3", "PASS" if ok1 else "FAIL", "SAME-CODE RERUN")

    # ---- 2. same-code rerun: tt_worldline_spectrum -------------------------
    rc2, out2 = run_calc("calc/tt_worldline_spectrum.py")
    m = re.search(r"reproduces Q = \(w/2pi\)e\^\{-eps w\}: (.*)", out2)
    worst = 0.0
    if m:
        for pair in m.group(1).split(","):
            a, b = [float(x) for x in pair.strip().split("/")]
            worst = max(worst, abs(a - b) / b)
    ok2 = rc2 == 0 and worst < 3e-2
    bench("H->0 / flat-vacuum limit (pipeline)",
          "tt_worldline_spectrum (half-line transform)",
          "numeric vs exact (w/2pi)e^{-eps w}, worst over w grid",
          f"worst rel.err {worst:.1e}", "< 3e-2",
          "PASS" if ok2 else "FAIL", "SAME-CODE RERUN")

    # ---- 3. INDEPENDENT-CODE benchmark of the fold identity ----------------
    w, Lam = 1.7, 20.0
    ind = fold_independent(w, Lam)
    clo = fold_closed(w, Lam)
    rel = abs(ind - clo) / abs(clo)
    bench("exactly-solvable special case (INDEPENDENT CODE)",
          "fold identity, fresh Simpson implementation", f"w={w}, Lam={Lam}",
          f"rel.err {rel:.1e}", "< 1e-6",
          "PASS" if rel < 1e-6 else "FAIL", "INDEPENDENT-CODE")

    # ---- 4-7. contract benchmarks ------------------------------------------
    rc3, out3 = run_calc("provenance/class_c_manifest_gate.py")
    n_refuse = out3.count("refuses:")
    bench("fail-closed contract", "class_c_manifest_gate",
          "require() refuses UNDECIDED sections",
          f"{n_refuse} refusals observed", ">= 3",
          "PASS" if rc3 == 0 and n_refuse >= 3 else "FAIL", "SAME-CODE RERUN")

    rc4, out4 = run_calc("calc/class_c_solver.py", ("--selftest",))
    bench("fail-closed contract", "class_c_solver",
          "refuses while prerequisites undecided (--selftest)",
          f"exit {rc4}, REFUSED={'REFUSED' in out4}", "exit 0 + REFUSED",
          "PASS" if rc4 == 0 and "REFUSED" in out4 else "FAIL", "SAME-CODE RERUN")

    rc5, out5 = run_calc("provenance/class_c_dependency_closure.py")
    bench("parameter-leakage closure", "class_c_dependency_closure",
          "8 bypass mutants caught + clean source passes + live surface closed",
          f"exit {rc5}, SURVIVED={out5.count('SURVIVED')}", "exit 0, 0 survived",
          "PASS" if rc5 == 0 else "FAIL", "SAME-CODE RERUN")

    rc6, out6 = run_calc("provenance/class_c_contamination_audit.py")
    clean6 = out6.strip().splitlines()[0] if out6 else ""
    bench("contamination", "class_c_contamination_audit",
          "active-surface verdict", clean6[:60], "CLEAN, exit 0",
          "PASS" if rc6 == 0 and "CLEAN" in out6 else "FAIL", "SAME-CODE RERUN")

    # ---- not-yet-applicable limits (declared, so absence is visible) --------
    na_rows = [
        ("H->0 limit of assembled G_R^TT", "NOT YET APPLICABLE -- class C uncomputed"),
        ("KMS/thermal limit of assembled response", "NOT YET APPLICABLE"),
        ("gauge-equivalent formulation agreement", "NOT YET APPLICABLE -- gauge UNDECIDED-DISPATCH"),
        ("weak-coupling limit of interacting Sigma", "NOT YET APPLICABLE"),
    ]

    verdict = "ALL APPLICABLE CELLS PASS" if not FAILS_LIST else \
        "FAILURES: " + "; ".join(FAILS_LIST)
    lines = [
        "# CLASS_C_BENCHMARK_MATRIX — emitted, never hand-typed",
        "",
        f"*Generated {ts} by `provenance/class_c_benchmark_matrix.py` "
        f"(Phases 5-6). Verdict: **{verdict}**.*",
        "",
        "*Provenance: rows marked SAME-CODE RERUN execute existing implementations*"
        "*-- regression checks, NOT independent confirmations. The row marked*"
        "*INDEPENDENT-CODE is computed by a fresh implementation written against*"
        "*the closed form only.*",
        "",
        "| limit | component | benchmark | measured | tolerance | status | provenance |",
        "|---|---|---|---|---|---|---|",
    ]
    for limit, comp, desc, meas, st, prov in ROWS:
        lines.append(f"| {limit} | {comp} | {desc} | {meas} | — | {st} ({prov}) |")
    lines += ["", "## Not-yet-applicable limits (declared, so absence is visible)", ""]
    for a, b in na_rows:
        lines.append(f"- **{a}**: {b}.")
    lines += [
        "",
        "## What this matrix does and does not establish",
        "",
        "Green cells establish that the machinery reproduces its known limits.",
        "They do NOT establish any class-C physics result; walls A-C stand.",
        "",
    ]
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"class_c_benchmark_matrix: {verdict}")
    print(f"report: {os.path.relpath(OUT, ROOT)}")
    return 1 if FAILS_LIST else 0


if __name__ == "__main__":
    sys.exit(main())

