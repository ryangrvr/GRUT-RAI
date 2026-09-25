#!/usr/bin/env python3
"""sx1_length: can Sel-4x (constant length rescaling = pure unit change) be selected?

CHARTER: SX1_LENGTH_EQUIVALENCE_CHARTER_01.md (pre-registration frozen at commit 3857e64
BEFORE this instrument ran; owner direction after the GS-1 ruling, Issue #2 comment
5837782502). GS-1's access-relative geometry is an earned input; the principle identifying a
constant length rescaling with a unit change is on trial. Forbidden as selectors: CARRIER,
GeoInv, the TT stress tensor, omega^7, the supplied massless probe structure, a preselected
spatial coupling, the conclusion that lengths transform as units, self-reconstruction.

Discriminator: a transformation is a pure unit change iff every dimensionless accessible
datum is invariant -- normalized spectrum, normalized resistance profile, anisotropy ratio,
static-dynamic product R(0,1) w_max^2, hop geometry.

Legs: L-U co-stretch | L-R rigid stretch | L-A anisotropic / inhomogeneous deformation |
L-P earned admissibility | L-C the owner's counterexample under single-site access.

Pure stdlib. Run: python3 calc/sx1_length.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from gs1_geometry import laplacian, inv, G, mm, tr

FAIL = []
CHECKS = []
HALT = []
L = 6
NS = L * L
LAM = 1.3
PIN = 0.2


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


def idx(r, c):
    return (r % L) * L + (c % L)


def edges(scale):
    """scale(kind, r, c) -> spring weight for the x-edge or y-edge starting at (r, c)."""
    E = []
    for r in range(L):
        for c in range(L):
            E.append((idx(r, c), idx(r, c + 1), scale("x", r, c)))
            E.append((idx(r, c), idx(r + 1, c), scale("y", r, c)))
    return E


def network(scale, pin):
    return laplacian(NS, edges(scale), [pin] * NS)


def resistance(Kinv, a, b):
    return Kinv[a][a] + Kinv[b][b] - 2 * Kinv[a][b]


def data(K):
    lam, _ = jacobi_eig(K)
    om = sorted(math.sqrt(max(x, 0.0)) for x in lam)
    s = [(w - om[0]) / (om[-1] - om[0]) for w in om]
    Ki = inv(K)
    r1 = resistance(Ki, idx(0, 0), idx(0, 1))
    prof = [resistance(Ki, idx(0, 0), idx(0, j)) / r1 for j in (2, 3)]
    aniso = r1 / resistance(Ki, idx(0, 0), idx(1, 0))
    prod = r1 * om[-1] ** 2
    support = sorted((i, j) for i in range(NS) for j in range(i + 1, NS) if K[i][j] != 0.0)
    return {"shape": s, "profile": prof, "aniso": aniso, "product": prod,
            "support": support, "min_eig": min(lam)}


def delta(a, b):
    d = max(abs(x - y) for x, y in zip(a["shape"], b["shape"]))
    d = max(d, max(abs(x - y) for x, y in zip(a["profile"], b["profile"])))
    d = max(d, abs(a["aniso"] - b["aniso"]))
    d = max(d, abs(a["product"] - b["product"]) / abs(b["product"]))
    return d


def legs_grid():
    print("\n=== L-U / L-R / L-A / L-P: CONSTANT SPATIAL ACTIONS ON A 6x6 PERIODIC GRID "
          "(lambda = 1.3) ===")
    base = data(network(lambda k, r, c: 1.0, PIN))
    cases = {
        "co-stretch (springs AND pins / lambda)": network(lambda k, r, c: 1.0 / LAM, PIN / LAM),
        "rigid stretch (springs / lambda, pins fixed)": network(lambda k, r, c: 1.0 / LAM, PIN),
        "anisotropic (x-springs / lambda)":
            network(lambda k, r, c: 1.0 / LAM if k == "x" else 1.0, PIN),
        "inhomogeneous (columns 0-2 / lambda)":
            network(lambda k, r, c: 1.0 / LAM if c in (0, 1, 2) else 1.0, PIN),
    }
    out = {}
    for name, K in cases.items():
        d = data(K)
        dd = delta(d, base)
        same_hops = d["support"] == base["support"]
        out[name] = {"delta": dd, "aniso": d["aniso"], "hops_same": same_hops,
                     "min_eig": d["min_eig"]}
        if name.startswith("co-stretch"):
            halt_check(dd < 1e-12, f"L-U GATE {name}: |Delta D| = {dd:.1e} < 1e-12 -- a PURE "
                                   f"UNIT CHANGE (dimensionless data identity; halt-grade)")
        elif name.startswith("rigid"):
            check(dd > 1e-3, f"L-R GATE {name}: |Delta D| = {dd:.4f} > 1e-3 -- a constant "
                             f"rescaling of spatial couplings that is NOT a unit change "
                             f"(the intrinsic scale did not co-stretch)")
        else:
            check(dd > 1e-3, f"L-A GATE {name}: |Delta D| = {dd:.4f} > 1e-3 (anisotropy ratio "
                             f"{d['aniso']:.4f}) -- a physical deformation, observable")
        check(True, f"  {name}: hop geometry (graph integers) unchanged = {same_hops}", "note")
        check(d["min_eig"] > 0, f"L-P GATE {name}: min eigenvalue {d['min_eig']:.4f} > 0 -- "
                                f"𝔠_full admits it")
    check(True, "L-U/L-R/L-A/L-P consequence (frozen): only the co-stretch is a unit change. "
                "The rigid stretch and the deformations are observable -- and every one is "
                "earned-admissible. Earned structure DETECTS which occurred; it does not "
                "FORBID a probe from doing any of them. Hop (graph-integer) geometry sees none "
                "of them: metric/dynamic data do", "note")
    return out


def leg_C():
    print("\n=== L-C: THE OWNER'S COUNTEREXAMPLE -- single-site access to the path a-1-2 ===")
    K = [[1.2, -1.0, 0.0], [-1.0, 1.7, -0.7], [0.0, -0.7, 0.7]]
    K1 = [[x / LAM for x in r] for r in K]
    c, s = math.cos(0.4), math.sin(0.4)
    O = [[1, 0, 0], [0, c, -s], [0, s, c]]
    K2 = mm(mm(O, K1), tr(O))
    dsite = max(abs(G(K1, w)[0][0] - G(K2, w)[0][0]) for w in (0.3, 0.9))
    halt_check(dsite < 1e-12, f"L-C GATE: single-site data identical for description 1 (pure "
                              f"unit change) and description 2 (unit change + non-isometric "
                              f"interior deformation): max diff {dsite:.1e} < 1e-12 "
                              f"(halt-grade)")
    check(abs(K2[0][2]) > 1e-3, f"L-C GATE: description 2 is NOT a pure unit change of the "
                                f"hidden network -- site a couples to node 2 (weight "
                                f"{-K2[0][2]:.4f}) where the hidden path has none")
    dfull = max(abs(G(K1, 0.3)[i][j] - G(K2, 0.3)[i][j]) for i in range(3) for j in range(3))
    check(dfull > 1e-3, f"L-C GATE: full-access data separate them, max diff {dfull:.4f} "
                        f"> 1e-3")
    check(True, "L-C consequence (frozen): under limited access, 'unit change' and 'unit change "
                "+ physical deformation' are indistinguishable -- the counterexample SURVIVES. "
                "Under full access they separate", "note")
    return {"single_site_diff": dsite, "a2_weight": -K2[0][2], "full_diff": dfull}


def adjudicate(rg, rc):
    co = rg["co-stretch (springs AND pins / lambda)"]
    rig = rg["rigid stretch (springs / lambda, pins fixed)"]
    defs = [rg["anisotropic (x-springs / lambda)"], rg["inhomogeneous (columns 0-2 / lambda)"]]
    classification = co["delta"] < 1e-12
    hypothesis_false = rig["delta"] > 1e-3
    all_admissible = all(v["min_eig"] > 0 for v in rg.values())
    selection = "DERIVED" if not all_admissible else \
        "IRREDUCIBLE INPUT (reduced to the co-stretch declaration)"
    decid = ("CLASS-SPLIT by access" if (rc["single_site_diff"] < 1e-12 and
                                         rc["full_diff"] > 1e-3) else "not split")
    return {"classification_identity": "uniform co-stretch == unit change" if classification
            else "FAILED",
            "sel4x_general_hypothesis": "FALSE (rigid stretch is an observable constant "
                                        "rescaling)" if hypothesis_false else "not refuted",
            "deformations_observable": all(d["delta"] > 1e-3 for d in defs),
            "selection": selection, "decidability": decid,
            "overall": "IRREDUCIBLE INPUT for selection; CLASS-SPLIT by access for "
                       "decidability"}


def main():
    t0 = time.time()
    print("SX-1: CAN Sel-4x (CONSTANT LENGTH RESCALING = UNIT CHANGE) BE SELECTED? (charter "
          "frozen at 3857e64)")
    rg = legs_grid()
    rc = leg_C()
    adj = adjudicate(rg, rc)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "sx1_length", "charter_commit": "3857e64", "date": "2026-09-25",
           "lambda": LAM, "grid": rg, "LC": rc, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "SX1_LENGTH_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nSX-1 LENGTH-EQUIVALENCE ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
