#!/usr/bin/env python3
"""kernel_nonstationarity: how large is K(t,t') - K(t-t') on the stored exact FRW solutions?

CHARTER: NONSTATIONARITY_CHARTER_01.md (pre-registration frozen at commit eb3fc07 BEFORE this
instrument ran). Owner constraints: measurement only -- no new physical assumption, no
transport-law search, no discriminator evaluation, no register change. The integrator is the
transport instrument's validated Run class, reused unchanged (its controls ran at machine
precision under commit 05226bf).

OBJECT: the free TT commutator kernel at fixed comoving k on the declared Om = 0.315
background. Disclosed at pre-registration: at fixed comoving k even dS is not dt-only
(the comoving label redshifts), so three curves are reported on one grid -- FRW (the
measurement), dS(H0) (declared comparator convention), flat (exact zero control). The
D3a-stationary worldline object would need a smearing choice: NAMED, NOT TAKEN.

MEASURES (frozen): M1 same-lag drift (headline = max relative drift over reportable cells,
reporting floor 0.1 x grid max); M2 best-stationary residual R; M3 excess over dS.
GRID (frozen): anchors z_a in {0, 0.25, 0.5}; lags L*H0 in {0.1, 0.2, 0.4}; k in {0.5, 1, 2}.

Pure stdlib. Run: python3 calc/kernel_nonstationarity.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kernel_transport_rule import Run, ds_closed_K  # validated integrator, reused unchanged

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


Z_ANCH = [0.0, 0.25, 0.5]
LAGS = [0.1, 0.2, 0.4]
KS = [0.5, 1.0, 2.0]


def idx_at_t(r, t_target):
    best, bi = 1e99, 0
    for i, t in enumerate(r.t):
        d = abs(t - t_target)
        if d < best:
            best, bi = d, i
    return bi


def s1_controls():
    print("\n=== S1: CONTROLS (inherited integrator; flat exact-zero; dS comparator spot-check) ===")
    r = Run(1.0, bg="lcdm", n_steps=120000)
    wdrift = max(abs(r.wronskian(i) - 1.0) for i in range(0, len(r.t), 101))
    check(wdrift < 1e-6, f"Wronskian constancy on the production run (max drift {wdrift:.1e})")
    # flat exact-zero control: a == 1, t == eta; same-lag kernel independent of anchor
    # flat: a never grows, so the a_end guard would exit immediately -- run on the step-count
    # guard instead (a_end unreachable by construction; the 4n cap terminates the integration)
    rf = Run(1.0, bg="flat", n_steps=40000, a_start=1.0, a_end=2.0)
    n = len(rf.eta)
    L = 0.4
    ks = []
    for frac in (0.55, 0.7, 0.85):
        i = int(n * frac)
        j = idx_at_t(rf, rf.t[i] - L * rf.a[0])  # t = a*eta with constant a
        ks.append(rf.K(i, j) * rf.a[0] ** 2)  # constant-a normalization, uniform
    drift_flat = (max(ks) - min(ks)) / max(abs(v) for v in ks)
    check(drift_flat < 1e-6, f"flat exact-zero control: same-lag drift = {drift_flat:.1e}")
    # dS comparator spot-check: closed form vs numeric dS run at one (anchor, lag) pair
    rd = Run(1.0, bg="ds", H_star=1.0, n_steps=60000, a_start=0.3, a_end=0.99)
    i = len(rd.a) - 1
    j = idx_at_t(rd, rd.t[i] - 0.4)
    e1, e2 = -1.0 / rd.a[i], -1.0 / rd.a[j]
    got, want = rd.K(i, j), ds_closed_K(1.0, 1.0, e1, e2, rd.a[i], rd.a[j])
    rel = abs(abs(got) - abs(want)) / abs(want)
    check(rel < 1e-4, f"dS comparator spot-check: closed form vs numeric run (rel {rel:.1e})")
    return r


def s2_measure(runs):
    print("\n=== S2: THE MEASUREMENT (frozen grid; all cells reported) ===")
    t0 = runs[KS[0]].t[-1]
    grid_vals = {"frw": {}, "ds": {}}
    dropped = []
    for k in KS:
        r = runs[k]
        for L in LAGS:
            for z_a in Z_ANCH:
                a_a = 1.0 / (1.0 + z_a)
                ia = r.idx_at_a(a_a)
                t_a = r.t[ia]
                t_e = t_a - L
                if t_e <= r.t[0]:
                    dropped.append((k, L, z_a))
                    continue
                je = idx_at_t(r, t_e)
                grid_vals["frw"][(k, L, z_a)] = r.K(ia, je)
                # dS(H0) comparator: a_dS(t) = exp(t - t0), eta = -1/a (H = 1 = H0)
                a1, a2 = math.exp(t_a - t0), math.exp(t_e - t0)
                grid_vals["ds"][(k, L, z_a)] = ds_closed_K(k, 1.0, -1.0 / a1, -1.0 / a2, a1, a2)
    check(not dropped, f"grid feasibility: {len(dropped)} cells dropped "
                       f"({dropped if dropped else 'none'})", "note" if dropped else "ok")
    norm = {bg: max(abs(v) for v in grid_vals[bg].values()) for bg in ("frw", "ds")}

    # M1 same-lag drift per (k, L), both backgrounds
    cells = []
    print(f"\n   {'k':>4} {'L*H0':>5} | {'FRW n1':>8} {'FRW n2':>8} | {'dS n1':>8} {'dS n2':>8} | "
          f"{'excess(n2)':>10} | reportable")
    for k in KS:
        for L in LAGS:
            row = {"k": k, "L": L}
            for bg in ("frw", "ds"):
                vals = [grid_vals[bg][(k, L, z)] for z in Z_ANCH if (k, L, z) in grid_vals[bg]]
                spread = max(vals) - min(vals)
                meanabs = sum(abs(v) for v in vals) / len(vals)
                row[bg] = {"vals": vals, "n1": spread / norm[bg],
                           "n2": (spread / meanabs) if meanabs > 0 else float("inf"),
                           "meanabs": meanabs, "reportable": meanabs > 0.1 * norm[bg]}
            row["excess_n2"] = row["frw"]["n2"] - row["ds"]["n2"]
            cells.append(row)
            print(f"   {k:>4} {L:>5} | {row['frw']['n1']:>8.3f} {row['frw']['n2']:>8.3f} | "
                  f"{row['ds']['n1']:>8.3f} {row['ds']['n2']:>8.3f} | {row['excess_n2']:>10.3f} | "
                  f"{'yes' if row['frw']['reportable'] else 'below floor'}")

    reportable = [c for c in cells if c["frw"]["reportable"]]
    headline = max(c["frw"]["n2"] for c in reportable)
    headline_cell = max(reportable, key=lambda c: c["frw"]["n2"])
    excess_max = max(c["excess_n2"] for c in reportable)
    check(True, f"M1 HEADLINE: max relative same-lag drift (FRW, reportable cells) = "
                f"{headline:.3f} at (k = {headline_cell['k']}, L*H0 = {headline_cell['L']}); "
                f"{len(reportable)}/{len(cells)} cells above the frozen floor", "note")
    check(True, f"M3: max excess of FRW drift over the dS(H0) comparator = {excess_max:.3f} "
                "(the FRW-specific non-stationarity beyond the redshifting-label effect)", "note")

    # M2 best-stationary residual, FRW
    Rk = {}
    num_all, den_all = 0.0, 0.0
    for k in KS:
        num, den = 0.0, 0.0
        for L in LAGS:
            vals = [grid_vals["frw"][(k, L, z)] for z in Z_ANCH if (k, L, z) in grid_vals["frw"]]
            kbar = sum(vals) / len(vals)
            num += sum((v - kbar) ** 2 for v in vals)
            den += sum(v ** 2 for v in vals)
        Rk[k] = math.sqrt(num / den)
        num_all += num
        den_all += den
    R_pooled = math.sqrt(num_all / den_all)
    for k in KS:
        print(f"       M2: R(k = {k}) = {Rk[k]:.3f}")
    check(True, f"M2: pooled best-stationary residual R = {R_pooled:.3f} -- the fraction of the "
                "kernel's sampled variation that NO dt-only function can carry", "note")
    return grid_vals, cells, {"headline_n2": headline, "headline_cell":
                              {"k": headline_cell["k"], "L": headline_cell["L"]},
                              "excess_over_ds_max": excess_max, "R_per_k": Rk,
                              "R_pooled": R_pooled, "norm": norm}


def main():
    t_start = time.time()
    print("NON-STATIONARITY MEASUREMENT (charter: NONSTATIONARITY_CHARTER_01.md, frozen at eb3fc07)")
    r1 = s1_controls()
    if FAIL:
        print("\nHALT: controls failed; no measurement is reported.")
        sys.exit(1)
    runs = {1.0: r1}
    for k in (0.5, 2.0):
        runs[k] = Run(k, bg="lcdm", n_steps=120000)
    grid_vals, cells, summary = s2_measure(runs)

    out = {
        "instrument": "kernel_nonstationarity",
        "charter": "NONSTATIONARITY_CHARTER_01.md", "charter_commit": "eb3fc07",
        "date": "2026-09-25",
        "object": "free TT commutator kernel at fixed comoving k (measurement only; the "
                  "D3a-stationary worldline object needs a smearing choice -- named, not taken)",
        "grid": {"z_anchors": Z_ANCH, "lags_H0": LAGS, "k": KS},
        "cells": [{"k": c["k"], "L": c["L"],
                   "frw": {kk: c["frw"][kk] for kk in ("vals", "n1", "n2", "reportable")},
                   "ds": {kk: c["ds"][kk] for kk in ("vals", "n1", "n2")},
                   "excess_n2": c["excess_n2"]} for c in cells],
        "summary": summary,
        "checks": CHECKS, "failures": FAIL,
        "elapsed_s": round(time.time() - t_start, 2),
        "no_campaign_fence": "measurement only: no transport rule proposed, no discriminator "
                             "evaluated, no register change; fenced routes untouched",
        "hard_stop": "measurement recorded; owner reads the magnitude and decides what it "
                     "changes about the fenced queue",
    }
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "KERNEL_NONSTATIONARITY_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nNON-STATIONARITY MEASUREMENT: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print("HARD STOP: measurement recorded pending owner reading.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
