#!/usr/bin/env python3
"""c1a2_packaging: the packaging boundary re-tested with a defensible normalization.

CHARTER: C1A2_PACKAGING_CHARTER_01.md (pre-registration frozen at commit 3b139ab BEFORE
this instrument ran; owner ruling on C1-a, Issue #2). Separate from C1-a, whose record is
immutable and whose two L-B reds stay red regardless of this run. Calibration by C1-a's
labeled diagnostics is disclosed in the charter.

Defensible normalization: k(0) = v.v is modulation-independent, so peak-normalized
statistics structurally suppress the two-time effect; statistics here use the kernel's
own local scale at the same lag, window tau in [0.5, 3.0].

Gates: P-1 two-time magnitude (local scale, eps_m = 0.5) | P-2 amplitude scaling |
P-3 the local-anchor family fails, every member (eps_m = 1.0) | P-4 the whole Dt-only
class excluded (per-lag mean is the L2-optimal Dt-only fit; std/mean gate) |
P-5 stationary control (halt) | P-6 specificity control (halt): a stationary world with a
DIFFERENT kernel shows zero drift.

Pure stdlib; machinery reused from c1_seam unchanged. Run: python3 calc/c1a2_packaging.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import World, PIN, eigset, prop

FAIL = []
CHECKS = []
HALT = []
ANCH_A = [1.5, 2.0, 2.5]
ANCH_B = [5.5, 6.0, 6.5]
TAUS = [0.5 + 0.1 * i for i in range(26)]


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note", "diag": "diag"}[kind]
    print(f"  {tag if ok or kind in ('note', 'diag') else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind not in ("note", "diag"):
        FAIL.append(msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


def kernel_table(w, anchors):
    """k(a + tau, a) for every anchor and window tau."""
    return {a: [w.kernel(a + t, a) for t in TAUS] for a in anchors}


def drift_stat(tab):
    """max over cross-epoch anchor pairs and window taus of the local-scale drift."""
    worst = 0.0
    for a in ANCH_A:
        for b in ANCH_B:
            for ka, kb in zip(tab[a], tab[b]):
                worst = max(worst, abs(ka - kb) / max(abs(ka), abs(kb)))
    return worst


def spread_stat(tab):
    """max over window taus of std-across-anchors / mean |k| (per-lag mean = the
    L2-optimal Dt-only fit, so this gates the WHOLE Dt-only class)."""
    anchors = ANCH_A + ANCH_B
    worst = 0.0
    for i in range(len(TAUS)):
        vals = [tab[a][i] for a in anchors]
        mu = sum(vals) / len(vals)
        std = math.sqrt(sum((v - mu) ** 2 for v in vals) / len(vals))
        mabs = sum(abs(v) for v in vals) / len(vals)
        worst = max(worst, std / mabs)
    return worst


def anchor_family(w):
    pairs = [(s, t) for s in (2.6, 3.0, 3.4) for t in (4.4, 4.8, 5.4)] + \
            [(s, t) for s in (6.6, 7.0, 7.4) for t in (8.4, 8.8, 9.4)]
    pairs = [(s, t) for s, t in pairs if 0.5 <= t - s <= 3.0]

    def epoch_of(a):
        return 1 if 4.0 <= a < 8.0 else 0

    out = {}
    for name, anchor in (("emission (a=s)", lambda s, t: s),
                         ("observation (a=t)", lambda s, t: t),
                         ("midpoint", lambda s, t: 0.5 * (s + t))):
        out[name] = max(abs(w.frozen(epoch_of(anchor(s, t)), t - s) - w.kernel(t, s))
                        / abs(w.kernel(t, s)) for s, t in pairs)
    return out


class ScaledStationaryWorld:
    """All springs x scale, pins unchanged, CONSTANT IN TIME (both epochs identical):
    a stationary world with a genuinely different kernel (the P-6 specificity control)."""

    def __init__(self, N, scale):
        self.N = N
        K = [[0.0] * N for _ in range(N)]
        for i in range(N):
            K[i][i] = PIN
        for i in range(N - 1):
            w = scale
            K[i][i + 1] -= w
            K[i + 1][i] -= w
            K[i][i] += w
            K[i + 1][i + 1] += w
        bath = [row[1:] for row in K[1:]]
        es = eigset(bath)
        self.bath = [es, es]

    def kernel(self, t, s):
        v = [1.0] + [0.0] * (self.N - 2)
        v = prop(self.bath, s, t, v)
        return v[0]


def main():
    t0 = time.time()
    print("C1-a2: THE PACKAGING BOUNDARY, RE-TESTED (charter frozen at 3b139ab)")
    w05, w10, w00 = World(24, 0.5), World(24, 1.0), World(24, 0.0)
    tab05 = kernel_table(w05, ANCH_A + ANCH_B)
    tab10 = kernel_table(w10, ANCH_A + ANCH_B)
    tab00 = kernel_table(w00, ANCH_A + ANCH_B)

    print("\n=== P-1 / P-2: TWO-TIME MAGNITUDE IN THE KERNEL'S LOCAL SCALE ===")
    r05 = drift_stat(tab05)
    check(r05 > 0.05, f"P-1 GATE: max local-scale same-lag drift at eps_m = 0.5: "
                      f"r = {r05:.4f} > 0.05 over cross-epoch anchor pairs, tau in "
                      f"[0.5, 3] -- the generated kernel is two-time at order 10^-1 in "
                      f"its own scale")
    r10 = drift_stat(tab10)
    ratio = r10 / r05
    check(1.5 <= ratio <= 2.5, f"P-2 GATE: amplitude scaling r(1.0)/r(0.5) = {ratio:.4f} "
                               f"in [1.5, 2.5] (r(1.0) = {r10:.4f}) -- the effect scales "
                               f"with the TTI-breaking amplitude")

    print("\n=== P-3: THE LOCAL-ANCHOR FAMILY FAILS, EVERY MEMBER (eps_m = 1.0) ===")
    fam10 = anchor_family(w10)
    fam05 = anchor_family(w05)
    d10 = ", ".join(f"{k}: {v:.4f}" for k, v in fam10.items())
    d05 = ", ".join(f"{k}: {v:.4f}" for k, v in fam05.items())
    check(all(v > 0.05 for v in fam10.values()),
          f"P-3 GATE: every member's worst cross-boundary relative error > 0.05 at "
          f"eps_m = 1.0 ({d10}) -- no single frozen spectral measure reproduces the "
          f"crossing kernel")
    check(True, f"  eps_m = 0.5 family values (reported, not gated): {d05}", "note")

    print("\n=== P-4: THE WHOLE Dt-ONLY CLASS EXCLUDED (the certifying gate) ===")
    s10 = spread_stat(tab10)
    check(s10 > 0.05, f"P-4 GATE: max over window lags of std-across-anchors / mean|k| = "
                      f"{s10:.4f} > 0.05 at eps_m = 1.0 -- the per-lag mean is the "
                      f"L2-optimal Dt-only fit, so EVERY Dt-only kernel misses the "
                      f"generated K(t,s) by > 5% of its local scale at some lag")

    print("\n=== P-5 / P-6: CONTROLS (halt-grade) ===")
    r00, s00 = drift_stat(tab00), spread_stat(tab00)
    halt_check(r00 < 1e-10 and s00 < 1e-10,
               f"P-5 GATE: eps_m = 0 stationary control: drift {r00:.1e}, spread "
               f"{s00:.1e}, both < 1e-10 -- the statistics vanish exactly on the "
               f"stationary domain (halt-grade)")
    ws = ScaledStationaryWorld(24, 1.25)
    tabs = kernel_table(ws, ANCH_A + ANCH_B)
    rs = drift_stat(tabs)
    kdiff = max(abs(a - b) / max(abs(a), abs(b))
                for a, b in zip(tabs[ANCH_A[0]], tab00[ANCH_A[0]]))
    halt_check(rs < 1e-10, f"P-6 GATE: matched STATIONARY world (all springs x1.25, "
                           f"constant): drift statistic {rs:.1e} < 1e-10 -- zero drift "
                           f"(halt-grade)")
    check(kdiff > 0.05, f"P-6 GATE: yet its kernel differs from the base stationary "
                        f"kernel by {kdiff:.4f} > 0.05 relative -- the statistic detects "
                        f"NONSTATIONARITY, never mere kernel difference")

    certified = (r05 > 0.05 and 1.5 <= ratio <= 2.5
                 and all(v > 0.05 for v in fam10.values()) and s10 > 0.05
                 and r00 < 1e-10 and s00 < 1e-10 and rs < 1e-10 and kdiff > 0.05)
    adj = {
        "packaging_boundary": ("CERTIFIED: no single spectral measure and no Dt-only "
                               "kernel packages the generated K(t,s) at finite stepped "
                               "level in-class; the priced datum is the two-time "
                               "spectral datum C1-a exhibited ({lambda_e, u_e} + the "
                               "mixing matrices)" if certified else
                               "NOT CERTIFIED -- see red gates"),
        "relation_to_C1a": "C1-a's record unchanged; its two L-B reds remain red",
        "S1_partition": ("packaging certification CLOSED at finite stepped level; "
                         "C1-b (infinite volume) and C1-c (smooth modulation) remain "
                         "open, named not opened" if certified else
                         "packaging certification still open"),
        "fences": "no cosmological object consumed; no C2 content; omega^7/Class-4/"
                  "GR-1/closed forks untouched; no absolute exponent computed",
    }
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "c1a2_packaging", "charter_commit": "3b139ab",
           "date": "2026-09-25", "P1_r05": r05, "P2_r10": r10, "P2_ratio": ratio,
           "P3_family_eps1": fam10, "P3_family_eps05_reported": fam05, "P4_spread": s10,
           "P5_drift0": r00, "P5_spread0": s00, "P6_scaled_drift": rs,
           "P6_kernel_diff": kdiff, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "C1A2_PACKAGING_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    gated = [c for c in CHECKS if c["kind"] not in ("note", "diag")]
    n_ok = sum(1 for c in gated if c["ok"])
    print(f"\nC1-a2 PACKAGING RE-TEST: {n_ok}/{len(gated)} gated checks passed; "
          f"failures: {len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
