#!/usr/bin/env python3
"""partition_selection_p1: can invariant criteria select a system/bath partition from
correlation structure alone?

CHARTER: RELATIONAL_ONTOLOGY_CHARTER_01.md (pre-registration frozen at commit 3bba895 BEFORE
this instrument ran; testbeds, partition family, criteria, thresholds and A/B/C signatures are
fixed there and implemented here mechanically).

SCOPE (fixed at charter): TOY-CLASS structural probe in the exactly solvable Gaussian world --
closed quadratic H = p^T p/2 + q^T V q/2, ground states, exact reduced dynamics. The verdict is
about the CRITERION CLASS (can it select subsystems at all, and in which A/B/C mode), never
about reality directly. hbar = m = 1 declared (hbar is an EMPIRICAL INPUT per the record).

NO-DEFAULT FENCE: nothing below knows which answer any prior GRUT architecture would prefer.
NO-CAMPAIGN FENCE: measures the criterion class; proposes no ontology; changes no register
field. Pure stdlib. Run: python3 calc/partition_selection_p1.py
"""
import hashlib
import itertools
import json
import math
import os
import random
import sys
import time

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note", "halt": "HALT"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


# ============================== tiny dense linear algebra ====================================
def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(m)) for j in range(p)] for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def sub(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def frob(A):
    return math.sqrt(sum(x * x for r in A for x in r))


def jacobi_eig(Ain, tol=1e-12, sweeps=100):
    """Cyclic Jacobi for symmetric matrices. Returns (eigenvalues, eigenvector-columns)."""
    n = len(Ain)
    A = [row[:] for row in Ain]
    Vv = eye(n)
    for _ in range(sweeps):
        off = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                theta = 0.5 * (A[q][q] - A[p][p]) / A[p][q]
                t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p] = c * akp - s * akq
                    A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k] = c * apk - s * aqk
                    A[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = Vv[k][p], Vv[k][q]
                    Vv[k][p] = c * vkp - s * vkq
                    Vv[k][q] = s * vkp + c * vkq
    return [A[i][i] for i in range(n)], Vv


def matfunc(A, f):
    """f(A) for symmetric A via eigendecomposition."""
    lam, U = jacobi_eig(A)
    n = len(A)
    D = [[f(lam[i]) if i == j else 0.0 for j in range(n)] for i in range(n)]
    return matmul(matmul(U, D), transpose(U))


# ============================== testbeds (charter 1.1) =======================================
N = 10
SEED = 20260925


def build_x1():
    """Homogeneous ring: uniform diagonal w0^2 + 2k, off-diagonal -k, periodic."""
    w0, k = 1.0, 0.5
    V = [[0.0] * N for _ in range(N)]
    for i in range(N):
        V[i][i] = w0 * w0 + 2 * k
        V[i][(i + 1) % N] -= k
        V[(i + 1) % N][i] -= k
    return V


def build_x2():
    """Open chain, uniform bulk; light impurity at site 0 weakly coupled to site 1."""
    w0, k, wimp2, g = 1.0, 0.5, 0.09, 0.1
    V = [[0.0] * N for _ in range(N)]
    for i in range(1, N):
        V[i][i] = w0 * w0
    for i in range(1, N - 1):
        V[i][i] += k
        V[i + 1][i + 1] += k
        V[i][i + 1] -= k
        V[i + 1][i] -= k
    V[0][0] = wimp2 + g
    V[1][1] += g
    V[0][1] -= g
    V[1][0] -= g
    return V


def build_x3():
    rng = random.Random(SEED)
    A = [[rng.gauss(0, 1) / math.sqrt(N) for _ in range(N)] for _ in range(N)]
    V = matmul(transpose(A), A)
    for i in range(N):
        V[i][i] += 0.1
    return V


# ============================== criteria (charter 1.3) =======================================
def crit_c1(V, S):
    """Memory-kernel participation rank per |S| (minimize)."""
    E = [i for i in range(N) if i not in S]
    VEE = sub(V, E, E)
    VSE = sub(V, list(S), E)
    lam, U = jacobi_eig(VEE)
    Ut = transpose(U)
    ws = []
    for mu in range(len(E)):
        omega2 = max(lam[mu], 1e-14)
        v = [sum(VSE[a][j] * Ut[mu][j] for j in range(len(E))) for a in range(len(S))]
        ws.append(sum(x * x for x in v) / math.sqrt(omega2))
    s1 = sum(ws)
    s2 = sum(w * w for w in ws)
    pr = (s1 * s1 / s2) if s2 > 0 else 0.0
    return pr / len(S)


def gs_blocks(V):
    Vh = matfunc(V, lambda x: math.sqrt(max(x, 1e-14)))
    Vmh = matfunc(V, lambda x: 1.0 / math.sqrt(max(x, 1e-14)))
    return Vmh, Vh  # sigma_qq = Vmh/2, sigma_pp = Vh/2


def vn_entropy(Vmh, Vh, S):
    A = [[Vmh[i][j] / 2.0 for j in S] for i in S]
    B = [[Vh[i][j] / 2.0 for j in S] for i in S]
    Ah = matfunc(A, lambda x: math.sqrt(max(x, 1e-14)))
    M = matmul(matmul(Ah, B), Ah)
    lam, _ = jacobi_eig(M)
    ent = 0.0
    for l in lam:
        nu = math.sqrt(max(l, 0.25))  # symplectic eigenvalue >= 1/2
        if nu > 0.5 + 1e-12:
            ent += (nu + 0.5) * math.log(nu + 0.5) - (nu - 0.5) * math.log(nu - 0.5)
    return ent


def crit_c2(V, S, cache):
    """Ground-state mutual information per |S| (minimize). Global pure: I = 2 S_vN(S)."""
    Vmh, Vh = cache
    return 2.0 * vn_entropy(Vmh, Vh, list(S)) / len(S)


def crit_c3(V, S, tstar=2.0):
    """Causal cohesion ||G_SS||/||G_SE|| at t* (maximize)."""
    G = matfunc(V, lambda x: math.sin(math.sqrt(max(x, 1e-14)) * tstar) / math.sqrt(max(x, 1e-14)))
    E = [i for i in range(N) if i not in S]
    num = frob(sub(G, list(S), list(S)))
    den = frob(sub(G, list(S), E))
    return num / max(den, 1e-30)


def probe_autocorr(V, p, tgrid):
    lam, U = jacobi_eig(V)
    out = []
    for t in tgrid:
        c = 0.0
        for k in range(len(lam)):
            w = math.sqrt(max(lam[k], 1e-14))
            c += (U[p][k] ** 2) * math.cos(w * t) / (2.0 * w)
        out.append(c)
    return out


def crit_c4(V, probe, tol=0.10):
    """Anchored minimal realization: smallest S containing probe whose ISOLATED dynamics
    reproduces the probe autocorrelation within tol; ties broken by C1. Returns (S or None)."""
    tgrid = [10.0 * i / 200 for i in range(201)]
    Cex = probe_autocorr(V, probe, tgrid)
    scale = max(abs(c) for c in Cex)
    best = None
    for size in (1, 2):
        cands = []
        for S in itertools.combinations(range(N), size):
            if probe not in S:
                continue
            VSS = sub(V, list(S), list(S))
            lam, U = jacobi_eig(VSS)
            pi = list(S).index(probe)
            err = 0.0
            for i, t in enumerate(tgrid):
                c = sum((U[pi][k] ** 2) * math.cos(math.sqrt(max(lam[k], 1e-14)) * t)
                        / (2.0 * math.sqrt(max(lam[k], 1e-14))) for k in range(size))
                err = max(err, abs(c - Cex[i]) / scale)
            if err <= tol:
                cands.append((crit_c1(V, S), S))
        if cands:
            best = min(cands)[1]
            break
    return best


# ============================== selection machinery (charter 1.4) ============================
def all_partitions():
    return [tuple([i]) for i in range(N)] + list(itertools.combinations(range(N), 2))


def orbit_key_ring(S):
    """Translation-orbit invariant on the ring: sorted gaps."""
    if len(S) == 1:
        return ("size1",)
    a, b = sorted(S)
    d = min(b - a, N - (b - a))
    return ("size2", d)


def run_criteria(V, label, ring=False):
    cache = gs_blocks(V)
    parts = all_partitions()
    scores = {"C1": {}, "C2": {}, "C3": {}}
    for S in parts:
        scores["C1"][S] = crit_c1(V, S)
        scores["C2"][S] = crit_c2(V, S, cache)
        scores["C3"][S] = -crit_c3(V, S)  # negate: uniform minimize convention
    result = {}
    for cname, sc in scores.items():
        ranked = sorted(sc.items(), key=lambda kv: kv[1])
        (Sw, vw), (Sr, vr) = ranked[0], ranked[1]
        gap = (vr - vw) / max(abs(vw), 1e-30)
        tie_orbit = None
        if ring:
            # tie within the winner's orbit?
            okey = orbit_key_ring(Sw)
            orb = [v for S2, v in sc.items() if orbit_key_ring(S2) == okey]
            spread = max(orb) - min(orb)
            if spread < 1e-6:
                tie_orbit = okey
                # gap to the best OTHER orbit
                others = [v for S2, v in sc.items() if orbit_key_ring(S2) != okey]
                gap = (min(others) - vw) / max(abs(vw), 1e-30)
        result[cname] = {"winner": list(Sw), "winner_score": vw, "runner_up": list(Sr),
                         "gap": gap, "tie_orbit": (list(tie_orbit) if tie_orbit else None)}
    return result, scores


def coarse_grain_V(V):
    """2:1 blocking: Q_b = (q_{2b}+q_{2b+1})/sqrt(2); V_blocked = P^T V P."""
    nb = N // 2
    P = [[0.0] * nb for _ in range(N)]
    for b in range(nb):
        P[2 * b][b] = 1.0 / math.sqrt(2.0)
        P[2 * b + 1][b] = 1.0 / math.sqrt(2.0)
    return matmul(matmul(transpose(P), V), P)


def cg_stable(V, S, cname):
    """Does the winner's image win (within its size class) in the blocked system?"""
    global N
    Vb = coarse_grain_V(V)
    img = tuple(sorted(set(i // 2 for i in S)))
    nb = N // 2
    cands = [tuple(c) for c in itertools.combinations(range(nb), len(img))]
    cacheb = gs_blocks(Vb)
    N_save = N
    N = nb
    try:
        vals = {}
        for c in cands:
            if cname == "C1":
                vals[c] = crit_c1(Vb, c)
            elif cname == "C2":
                vals[c] = crit_c2(Vb, c, cacheb)
            else:
                vals[c] = -crit_c3(Vb, c)
        winner = min(vals.items(), key=lambda kv: kv[1])[0]
        return winner == img
    finally:
        N = N_save


# ============================== controls (charter 1.5) =======================================
def s1_controls():
    print("\n=== S1: CONTROLS (halt on miss) ===")
    V = build_x1()
    lam, _ = jacobi_eig(V)
    lam.sort()
    exact = sorted(1.0 + 4 * 0.5 * math.sin(math.pi * k / N) ** 2 for k in range(N))
    worst = max(abs(a - b) for a, b in zip(lam, exact))
    check(worst < 1e-9, f"eigensolver control: ring spectrum matches analytic (worst {worst:.1e})")
    # GLE control: 2-oscillator exact kernel K(t) = g^2 sin(w_E t)/w_E via the general formula
    g, wE2 = 0.3, 2.0
    V2 = [[1.0, -g], [-g, wE2]]
    N_save = globals()["N"]
    globals()["N"] = 2
    try:
        pr = crit_c1(V2, (0,))
    finally:
        globals()["N"] = N_save
    check(abs(pr - 1.0) < 1e-9, f"GLE control: single bath mode gives participation rank {pr:.6f} (exact 1)")
    Vmh, Vh = gs_blocks(build_x3())
    sS = vn_entropy(Vmh, Vh, [0, 3, 7])
    sE = vn_entropy(Vmh, Vh, [i for i in range(N) if i not in (0, 3, 7)])
    check(abs(sS - sE) < 1e-7, f"Gaussian-MI control: global purity S(S) = S(E) (|diff| {abs(sS-sE):.1e})")


# ============================== main =========================================================
def main():
    t0 = time.time()
    print("PARTITION SELECTION P-1 (charter: RELATIONAL_ONTOLOGY_CHARTER_01.md, frozen at 3bba895)")
    s1_controls()
    if FAIL:
        print("\nHALT: controls failed; no signature is issued.")
        sys.exit(1)

    out = {"testbeds": {}}
    THR = 0.20
    for label, builder, ring, probe in (("X1", build_x1, True, 0),
                                        ("X2", build_x2, False, 0),
                                        ("X3", build_x3, False, None)):
        V = builder()
        if probe is None:
            probe = max(range(N), key=lambda i: V[i][i])
        res, scores = run_criteria(V, label, ring=ring)
        print(f"\n=== {label} ===")
        selections = {}
        for cname, r in res.items():
            if ring and r["tie_orbit"] is not None:
                verdict = f"TIE-ORBIT {r['tie_orbit']} (orbit gap to next {r['gap']:.3f})"
                selections[cname] = ("TIE-ORBIT", tuple(r["winner"]), r["gap"])
            else:
                sel = r["gap"] >= THR and cg_stable(V, tuple(r["winner"]), cname)
                verdict = (f"SELECTS {r['winner']} (gap {r['gap']:.3f}, cg-stable)" if sel
                           else f"no selection (winner {r['winner']}, gap {r['gap']:.3f}"
                                f"{', cg-unstable' if r['gap'] >= THR else ''})")
                selections[cname] = (("SELECTS" if sel else "NONE"), tuple(r["winner"]), r["gap"])
            print(f"  {cname}: {verdict}")
        # X1 rigging control: unique (non-orbit) intrinsic selection HALTS
        if ring:
            rigged = any(v[0] == "SELECTS" for v in selections.values())
            check(not rigged, "X1 rigging control: no intrinsic criterion selects a unique "
                              "partition on the symmetric ring", "ctrl" if not rigged else "halt")
            if rigged:
                print("\nHALT: a criterion broke translation symmetry; instrument invalid.")
                sys.exit(1)
        c4 = crit_c4(V, probe)
        print(f"  C4 (anchored, probe site {probe}): "
              f"{'selects ' + str(list(c4)) if c4 else 'NO-SELECTION at |S| <= 2'}")
        out["testbeds"][label] = {"criteria": res, "selections":
                                  {k: {"verdict": v[0], "winner": list(v[1]), "gap": v[2]}
                                   for k, v in selections.items()},
                                  "C4": {"probe": probe, "selected": (list(c4) if c4 else None)}}

    # ---- signature, mechanically (charter 1.4) ----
    print("\n=== SIGNATURE (charter 1.4, mechanical) ===")
    x2sel = out["testbeds"]["X2"]["selections"]
    x3sel = out["testbeds"]["X3"]["selections"]
    x1sel = out["testbeds"]["X1"]["selections"]
    x2_selecting = [(k, tuple(v["winner"])) for k, v in x2sel.items() if v["verdict"] == "SELECTS"]
    x1_all_tie = all(v["verdict"] == "TIE-ORBIT" for v in x1sel.values())
    agree_pairs = [(a, b) for i, (a, wa) in enumerate(x2_selecting)
                   for (b, wb) in x2_selecting[i + 1:] if wa == wb]
    a_sig = len(agree_pairs) >= 1 and x1_all_tie
    x2_winners = set(tuple(v["winner"]) for v in x2sel.values())
    x3_winners = set(tuple(v["winner"]) for v in x3sel.values())
    x3_selecting = [k for k, v in x3sel.items() if v["verdict"] == "SELECTS"]
    intrinsic_disagree = (len(x2_winners) > 1 and len(x2_selecting) <= 1) or \
                         (len(x3_winners) > 1 and len(x3_selecting) <= 1)
    c4_selects = all(out["testbeds"][t]["C4"]["selected"] is not None for t in ("X2", "X3"))
    if a_sig:
        signature = "A"
        detail = (f"intrinsic criteria {agree_pairs} agree on {x2_selecting[0][1]} in X2 with "
                  "cg-stability, and X1 returns tie-orbits only")
    elif intrinsic_disagree and c4_selects:
        signature = "C"
        detail = ("intrinsic criteria disagree or fail to select stably where structure is "
                  "present, while the anchored criterion always selects -- selection happens "
                  "only when an anchor is consumed")
    else:
        signature = "B"
        detail = "intrinsic criteria select only up to ties/families, coherently"
    check(True, f"SIGNATURE = {signature}: {detail}", "note")
    out["signature"] = {"value": signature, "detail": detail,
                        "x1_all_tie_orbit": x1_all_tie,
                        "x2_agreeing_selectors": agree_pairs,
                        "x2_winners": [list(w) for w in x2_winners],
                        "x3_winners": [list(w) for w in x3_winners]}

    # tolerance-flip test (charter 1.4, the philosophy exit)
    flips = []
    for thr in (0.10, 0.30):
        x2s = [(k, tuple(v["winner"])) for k, v in x2sel.items()
               if v["gap"] >= thr and v["verdict"] in ("SELECTS", "NONE")
               and cg_stable(build_x2(), tuple(v["winner"]), k)]
        ap = [(a, b) for i, (a, wa) in enumerate(x2s) for (b, wb) in x2s[i + 1:] if wa == wb]
        sig_thr = "A" if (len(ap) >= 1 and x1_all_tie) else ("C" if c4_selects else "B")
        if sig_thr != signature:
            flips.append({"threshold": thr, "signature": sig_thr})
    out["tolerance_flip"] = flips
    if flips:
        check(True, f"TOLERANCE-FLIP: the signature changes under threshold variation {flips} -- "
                    "per the charter, this triggers the NOT-SHARPER-THAN-PHILOSOPHY report", "note")
    else:
        check(True, "tolerance-flip test: signature stable under threshold 0.10-0.30", "note")

    out.update({"instrument": "partition_selection_p1", "charter_commit": "3bba895",
                "date": "2026-09-25", "N": N, "seed": SEED,
                "checks": CHECKS, "failures": FAIL,
                "elapsed_s": round(time.time() - t0, 2)})
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "PARTITION_SELECTION_P1_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nPARTITION SELECTION P-1: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print("HARD STOP: signature recorded pending the relational-ontology map.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
