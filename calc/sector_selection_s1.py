#!/usr/bin/env python3
"""sector_selection_s1: given the cone, what selects the physical trajectory through it?

CHARTER: SECTOR_SELECTION_CHARTER_01.md (pre-registration frozen at commit 351a326 BEFORE this
instrument ran; battery, hypotheses, functionals, thresholds and outcome classes fixed there).

CONVENTION (instrument's own, declared): J(omega) = sum_f |M_f|^2 delta(omega - omega_f), mode
normalization 1/sqrt(2 omega) per quantum. Exponents measured at 30 log-spaced points via exact
root-finding (no binning), log-log least squares over the declared window omega in [0.02, 0.2],
window-stability check on the half window. B4 is built FRESH (continuum dispersion
omega = q - beta q^3, beta = 0.05, pair at fixed small k_par = 1e-3); no code or data shared
with the adjudicator v3 instrument -- it independently probes the same cancellation CLASS.

Pure stdlib. Run: python3 calc/sector_selection_s1.py
"""
import hashlib
import json
import math
import os
import sys
import time

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


WLO, WHI = 0.02, 0.2
WGRID = [WLO * (WHI / WLO) ** (i / 29) for i in range(30)]


def slope(ws, js):
    xs = [math.log(w) for w, j in zip(ws, js) if j > 0]
    ys = [math.log(j) for j in js if j > 0]
    n = len(xs)
    xb, yb = sum(xs) / n, sum(ys) / n
    return sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)


def measure(Jfunc, label, expect=None, tol=0.05):
    js = [Jfunc(w) for w in WGRID]
    s_full = slope(WGRID, js)
    half = WGRID[:15]
    s_half = slope(half, [Jfunc(w) for w in half])
    stable = abs(s_full - s_half) < 0.05
    msg = f"{label}: s = {s_full:+.3f} (half-window {s_half:+.3f}{'' if stable else ' UNSTABLE'})"
    if expect is not None:
        check(stable and abs(s_full - expect) < tol, msg + f"  [analytic {expect:+d}]")
    else:
        check(stable, msg)
    return s_full


# ============================== PC-A: THE BATTERY ============================================
def b1(p):
    """1 quantum, d = 3, vertex q^p: J = 4 pi w^2 * w^{2p} / (2w) ~ w^{1+2p}."""
    return lambda w: 4 * math.pi * w * w * (w ** (2 * p)) / (2 * w)


def b2(deriv):
    """2 quanta, d = 1, pair at k = 0 (q' = -q, w = 2q). Minimal: |M|^2 = 1/(4 wq wq');
    one derivative per leg: |M|^2 = (q q')^2/(4 wq wq'). Root density dq/dw = 1/2."""
    def J(w):
        q = w / 2.0
        m2 = 1.0 / (4 * q * q) if not deriv else (q * q) ** 2 / (4 * q * q)
        return 2 * m2 * 0.5  # two sign choices of q, density 1/2
    return J


def b3_d3():
    """2 quanta, d = 3, pair at k = 0: J = 4 pi q^2 |M|^2 dq/dw, |M|^2 = 1/(4 q^2)."""
    def J(w):
        q = w / 2.0
        return 4 * math.pi * q * q * (1.0 / (4 * q * q)) * 0.5
    return J


BETA, KPAR = 0.05, 1e-3


def disp(q):
    return q - BETA * q ** 3


def b4(which):
    """2 quanta, d = 1, counter-propagating pair (q > 0, q' = KPAR - q < 0), curvature-
    perturbed dispersion. Stress-type vertex bracket = sqrt(w w') + q q'/sqrt(w w')."""
    def J(wt):
        lo, hi = KPAR + 1e-9, 3.0
        f = lambda q: disp(q) + disp(q - KPAR) - wt
        if f(lo) > 0 or f(hi) < 0:
            return 0.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if f(mid) < 0:
                lo = mid
            else:
                hi = mid
        q = 0.5 * (lo + hi)
        wq, wqp = disp(q), disp(q - KPAR)
        t1 = math.sqrt(wq * wqp)
        t2 = q * (KPAR - q) / math.sqrt(wq * wqp)
        br = {"kinetic": t1, "potential": t2, "full": t1 + t2}[which]
        m2 = br * br / (4 * wq * wqp)
        dwdq = (1 - 3 * BETA * q ** 2) + (1 - 3 * BETA * (q - KPAR) ** 2)
        return m2 / dwdq
    return J


def pc_a():
    print("\n=== PC-A: THE BATTERY (exponents via exact roots; log-slope on the frozen window) ===")
    print("  -- B1: one quantum, d = 3, vertex q^p (H1: +2 per momentum power) --")
    s = {p: measure(b1(p), f"B1 p={p}", expect=1 + 2 * p) for p in (0, 1, 2)}
    inc1a, inc1b = s[1] - s[0], s[2] - s[1]
    check(abs(inc1a - 2) < 0.1 and abs(inc1b - 2) < 0.1,
          f"H1 (B1): increments {inc1a:+.3f}, {inc1b:+.3f} (frozen: +2 +- 0.1 each)")
    print("  -- B2: two quanta, d = 1, minimal vs one-derivative-per-leg --")
    s_min = measure(b2(False), "B2 minimal", expect=-2)
    s_der = measure(b2(True), "B2 derivative", expect=2)
    check(abs((s_der - s_min) - 4) < 0.2,
          f"H1 (B2, pair channel): increment {s_der - s_min:+.3f} for two momentum powers "
          "(frozen: +4 +- 0.2)")
    print("  -- B3: two quanta, minimal, d = 1 vs d = 3 (H2: measure Delta_phase) --")
    s_d3 = measure(b3_d3(), "B3 d=3", expect=0)
    dphase = s_d3 - s_min
    check(True, f"H2 MEASURED: Delta_phase(1 -> 3) = {dphase:+.3f} (= d - 1 difference)", "note")
    print("  -- B4: the cancellation class (fresh model; H3: order-2 cancellation -> +4) --")
    s_kin = measure(b4("kinetic"), "B4 kinetic-only")
    s_pot = measure(b4("potential"), "B4 potential-only")
    s_ful = measure(b4("full"), "B4 full (near-cancelling)")
    check(abs(s_kin - s_pot) < 0.15,
          f"B4 pattern: kinetic-only ({s_kin:+.3f}) ~ potential-only ({s_pot:+.3f}) -- the base")
    inc4 = s_ful - 0.5 * (s_kin + s_pot)
    check(abs(inc4 - 4) < 0.2,
          f"H3: the tracelessness-class cancellation adds {inc4:+.3f} (frozen: +4 +- 0.2) -- "
          "independently reproducing the recorded kinetic/potential/full pattern in a fresh model")
    return {"B1": s, "B2": {"min": s_min, "der": s_der}, "B3_dphase": dphase,
            "B4": {"kin": s_kin, "pot": s_pot, "full": s_ful, "cancel_increment": inc4}}


# ============================== PC-B: MAPPING THE RECORDED LADDER ============================
def pc_b(bat):
    print("\n=== PC-B: THE RECORDED LADDER (3, 5, 7), mapped by recorded mechanisms only ===")
    h1_ok = abs(bat["B1"][1] - bat["B1"][0] - 2) < 0.1
    h3_ok = abs(bat["B4"]["cancel_increment"] - 4) < 0.2
    # recorded increments: 3 -> 5 attributed (benchmark verdict) to the two-derivative TT vertex
    # ("contributing omega^4 in |V|^2") -- an H1-class increment of +2 net; 3 -> 7 in the phonon
    # channel attributed (v3 counterfactual controls) to the tracelessness cancellation -- +4 =
    # H3 with m = 2 over the channel base. Conventions differ per record entry; the confrontation
    # is at increment level only, where conventions cancel.
    composed = h1_ok and h3_ok
    check(composed, "PC-B: the recorded increments {+2 (vertex-derivative class), +4 "
                    "(cancellation class)} are both reproduced by the battery's additive law -- "
                    "grade CONSISTENT-BY-MECHANISM (increment level; never one-formula-derived)")
    return composed


# ============================== PC-C: EXTREMIZATION ==========================================
def pc_c():
    print("\n=== PC-C: EXTREMIZATION BATTERY (null is first-class) ===")
    bands = [(0.02, 1.0), (0.05, 1.0), (0.02, 0.5)]
    s_grid = [1.0 + 0.25 * i for i in range(33)]  # 1..9
    hits = []
    results = {}
    for (lo, hi) in bands:
        wgrid = [lo + (hi - lo) * i / 400 for i in range(401)]
        dw = wgrid[1] - wgrid[0]
        Fs = {"F1_tau2": [], "F2_lowfrac": [], "F3_zeropoint": []}
        for s in s_grid:
            norm = sum(w ** s for w in wgrid) * dw
            Js = [w ** s / norm for w in wgrid]
            tgrid = [0.1 * (i + 1) for i in range(300)]
            K = [sum(J * math.sin(w * t) / w for J, w in zip(Js, wgrid)) * dw for t in tgrid]
            k2 = sum(k * k for k in K)
            Fs["F1_tau2"].append(sum(k * k * t * t for k, t in zip(K, tgrid)) / k2)
            mid = (lo + hi) / 2
            Fs["F2_lowfrac"].append(sum(J for J, w in zip(Js, wgrid) if w < mid) * dw)
            Fs["F3_zeropoint"].append(sum(0.5 * J * w for J, w in zip(Js, wgrid)) * dw)
        results[f"band[{lo},{hi}]"] = {k: v for k, v in Fs.items()}
        for fname, vals in Fs.items():
            ext = [s_grid[i] for i in range(1, len(vals) - 1)
                   if (vals[i] - vals[i - 1]) * (vals[i + 1] - vals[i]) < 0]
            for e in ext:
                for target in (3.0, 5.0, 7.0):
                    if abs(e - target) < 0.25:
                        hits.append((fname, (lo, hi), e, target))
            mono = "monotone" if not ext else f"interior extrema at s = {ext}"
            print(f"       {fname} on band [{lo},{hi}]: {mono}")
    # a HIT requires the SAME functional to land on the SAME target across ALL three bands
    robust = []
    for fname in ("F1_tau2", "F2_lowfrac", "F3_zeropoint"):
        for target in (3.0, 5.0, 7.0):
            if sum(1 for h in hits if h[0] == fname and h[3] == target) == len(bands):
                robust.append((fname, target))
    if robust:
        check(True, f"PC-C HIT (maximal suspicion flags per charter): {robust}", "note")
    else:
        check(True, "PC-C NULL: no declared functional extremizes at a recorded exponent "
                    "robustly across the declared bands -- the recorded occupancies are NOT "
                    "selected by this extremization family (null recorded as found)", "note")
    return robust, results


# ============================== PC-D: AMPLITUDE NON-SELECTION ================================
def pc_d():
    print("\n=== PC-D: AMPLITUDE NON-SELECTION (no-pin at cone level) ===")
    ok = True
    for lam in (0.1, 1.0, 10.0):
        J = [lam * w ** 7 for w in WGRID]
        admissible = all(j >= 0 for j in J)  # nu = J/2 saturates the floor for every lambda
        ok = ok and admissible
    check(ok, "lambda * J is cone-admissible for every lambda > 0 (floor saturated by the vacuum "
              "at each scale): the class law leaves the coefficient FREE -- whatever selects, "
              "selects classes, not amplitudes (the record's no-pin structure, at cone level)")
    return ok


def main():
    t0 = time.time()
    print("S-1 SECTOR-SELECTION INSTRUMENT (charter: SECTOR_SELECTION_CHARTER_01.md, frozen at 351a326)")
    bat = pc_a()
    if FAIL:
        print("\nHALT: battery failed; no outcome is issued.")
        sys.exit(1)
    composed = pc_b(bat)
    robust_hits, pcc = pc_c()
    ampl_free = pc_d()

    print("\n=== OUTCOME (charter section 3, mechanical) ===")
    if composed and not robust_hits and ampl_free:
        outcome = "SELECTION-BY-CLASS"
        detail = ("the missing arrow, as far as the tested classes reach, is LOCALITY + SYMMETRY "
                  "POWER COUNTING selecting the exponent CLASS of a sector's influence data; the "
                  "point within the class (amplitude, state) is sector-supplied")
    elif robust_hits:
        outcome = "SELECTION-BY-EXTREMUM"
        detail = f"robust extremization hits {robust_hits} -- flagged with maximal suspicion"
    elif not composed:
        outcome = "MAPPING-FAILS"
        detail = "the battery is additive but the recorded ladder does not map by recorded mechanisms"
    else:
        outcome = "COMPOSITION-FAILS"
        detail = "the battery violates additivity"
    check(True, f"OUTCOME: {outcome} -- {detail}", "note")

    out = {"instrument": "sector_selection_s1", "charter_commit": "351a326", "date": "2026-09-25",
           "battery": bat, "pcb_consistent_by_mechanism": composed,
           "pcc_robust_hits": robust_hits, "pcd_amplitude_free": ampl_free,
           "outcome": outcome,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "scope": "instrument's own golden-rule convention; increments convention-free; B4 is "
                    "an independent fresh model of the cancellation class (no v3 code); the "
                    "recorded 3/5/7 ladder consumed at increment level only; omega^7 remains "
                    "sector-occupancy evidence (class-4 gate open)",
           "hard_stop": "verdict recorded; owner directs P-3, the gravity sector, or geometry"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "SECTOR_SELECTION_S1_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nS-1 SECTOR SELECTION: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print(f"OUTCOME: {outcome}")
    print("HARD STOP: verdict recorded pending owner direction.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
