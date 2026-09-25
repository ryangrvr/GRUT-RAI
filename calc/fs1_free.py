#!/usr/bin/env python3
"""fs1_free: can the unit-change result be selected for a genuinely free gapless sector?

CHARTER: FS1_FREE_SECTOR_CHARTER_01.md (pre-registration frozen at commit 19fd85f BEFORE this
instrument ran; authority: owner ruling recorded in S41_FS1_OWNER_RULING_01.md). C_cons is an
unresolved import; FS-1 works inside the owner-specified conserved-coupling family, so every
result is conditional on it. DISTINGUISH (can the data tell O = H from an independent
conserved charge?) is kept separate from SELECT (does anything earned forbid it?).

Sector: harmonic ring N = 20, periodic, unpinned (gapless). Quadratic operators
Q = 1/2 z^T M z, z = (u, p); conservation A J M_H - M_H J A = 0; dynamics zdot = J M z.

Legs: L-T conserved-tower dimension vs range | L-P 𝔠_full admissibility | L-I dynamic vs
static multi-temperature influence data | L-G G-2 hop geometry of the probe-modified sector |
L-S the candidate GeoInv selector.

Pure stdlib. Run: python3 calc/fs1_free.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig

FAIL = []
CHECKS = []
HALT = []
N = 20
D2 = 2 * N
HPROBE = 0.05
T3 = (0.02, 0.04, 0.08)


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


# ---------------- quadratic algebra --------------------------------------------------------------
def zeros(n=D2):
    return [[0.0] * n for _ in range(n)]


def shift(r):
    S = [[0.0] * N for _ in range(N)]
    for i in range(N):
        S[i][(i + r) % N] += 1.0
    return S


def madd(A, B, cb=1.0):
    return [[A[i][j] + cb * B[i][j] for j in range(len(A))] for i in range(len(A))]


def mscale(A, c):
    return [[c * x for x in row] for row in A]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(m)) for j in range(p)] for i in range(n)]


def mvec(A, v):
    return [sum(a * b for a, b in zip(row, v)) for row in A]


def blocks(uu=None, pp=None, up=None):
    M = zeros()
    for i in range(N):
        for j in range(N):
            if uu:
                M[i][j] += uu[i][j]
            if pp:
                M[N + i][N + j] += pp[i][j]
            if up:
                M[i][N + j] += up[i][j]
                M[N + j][i] += up[i][j]
    return M


def sym_shift(r):
    return mscale(madd(shift(r), shift(-r)), 0.5)


J = zeros()
for _i in range(N):
    J[_i][N + _i] = 1.0
    J[N + _i][_i] = -1.0

K = madd(mscale(sym_shift(0), 2.0), mscale(sym_shift(1), -2.0))
MH = blocks(uu=K, pp=sym_shift(0))
JMH = mmul(J, MH)


def cons_map(A):
    AJ = mmul(A, J)
    return madd(mmul(AJ, MH), mmul(mmul(MH, J), A), -1.0)


def fnorm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def basis(R):
    out = []
    for r in range(R + 1):
        out.append(("pp", r, blocks(pp=sym_shift(r))))
    for r in range(R + 1):
        out.append(("uu", r, blocks(uu=sym_shift(r))))
    for r in range(-R, R + 1):
        out.append(("up", r, blocks(up=shift(r))))
    return out


def null_space_cols(cols):
    n = len(cols)
    G = [[sum(a * b for a, b in zip(cols[i], cols[j])) for j in range(n)] for i in range(n)]
    lam, V = jacobi_eig(G)
    mx = max(abs(x) for x in lam) or 1.0
    return [[V[i][k] for i in range(n)] for k in range(n) if abs(lam[k]) < 1e-10 * mx]


def flat(A):
    return [x for row in A for x in row]


def combo(bas, coef):
    M = zeros()
    for (_, _, B), c in zip(bas, coef):
        if abs(c) > 1e-15:
            M = madd(M, B, c)
    return M


MQ2 = blocks(uu=mmul(sym_shift(2), K), pp=sym_shift(2))
MP1 = blocks(up=madd(shift(1), shift(-1), -1.0))


# ---------------- L-T: the conserved tower ------------------------------------------------------
def leg_T():
    print("\n=== L-T: IS THE FREE EXCEPTION STRUCTURAL? (conserved tower vs range, N = 20) ===")
    h0 = max(abs(x) for x in flat(cons_map(MH)))
    halt_check(h0 < 1e-12, f"L-T control: [H, H] residual max|AJM_H - M_HJA| = {h0:.1e} "
                           f"< 1e-12 (halt-grade)")
    dims = {}
    tower = None
    for R in (1, 2, 3, 4):
        bas = basis(R)
        null = null_space_cols([flat(cons_map(B)) for _, _, B in bas])
        dims[R] = len(null)
        check(len(null) == 2 * R, f"L-T GATE R = {R}: conserved subspace of the "
                                  f"{len(bas)}-element range-<={R} basis has dim {len(null)} "
                                  f"(predicted 2R = {2 * R})")
        if R == 3:
            tower = (bas, null)
    rq = max(abs(x) for x in flat(cons_map(MQ2)))
    rp = max(abs(x) for x in flat(cons_map(MP1)))
    check(rq < 1e-10 and rp < 1e-10, f"L-T GATE: explicit Q2 (residual {rq:.1e}) and P1 "
                                     f"(residual {rp:.1e}) are conserved, both < 1e-10")
    check(True, "L-T consequence (frozen): the free phonon sector carries a tower of local "
                "conserved quadratic charges that grows linearly with range -- the S4-1 "
                "free-sector exception is STRUCTURAL, not a spin-model artifact", "note")
    return dims, tower


# ---------------- L-P: 𝔠_full ------------------------------------------------------------------
def leg_P(tower):
    print("\n=== L-P: 𝔠_full AS A SELECTOR (probe-modified Hamiltonians bounded below) ===")
    out = {}
    nH = fnorm(MH)
    cases = [("H", MH), ("Q2", MQ2), ("P1", MP1)]
    bas, null = tower
    for k, v in enumerate(null):
        cases.append((f"tower#{k}", combo(bas, v)))
    for name, MO in cases:
        MOs = mscale(MO, nH / fnorm(MO))
        lam, _ = jacobi_eig(madd(MH, MOs, HPROBE))
        mn = min(lam)
        out[name] = mn
        check(mn >= -1e-10, f"L-P GATE {name}: H + hO (h = {HPROBE}, O scaled to ||H||) has "
                            f"min eigenvalue {mn:.2e} >= -1e-10 -- 𝔠_full admits it")
    check(True, "L-P consequence (frozen): every member of the conserved tower is "
                "𝔠_full-admissible -- NULL as a selector", "note")
    return out


# ---------------- L-I: influence data ------------------------------------------------------------
def leg_I():
    print("\n=== L-I: DISTINGUISH VIA INFLUENCE DATA (mode space, k != 0) ===")
    ks = [2 * math.pi * j / N for j in range(1, N)]
    om = [2 * abs(math.sin(k / 2)) for k in ks]
    weights = {"H": om, "Q1": [math.cos(k) * w for k, w in zip(ks, om)],
               "P1": [2 * math.sin(k) for k in ks]}

    def var(w, T):
        tot = 0.0
        for wk, o in zip(w, om):
            nb = 0.0 if T == 0 else 1.0 / math.expm1(o / T)
            tot += wk * wk * nb * (nb + 1)
        return tot

    vac = {k: var(w, 0) for k, w in weights.items()}
    halt_check(all(v == 0.0 for v in vac.values()),
               f"L-I GATE (a): vacuum connected correlator of every conserved coupling is "
               f"exactly zero ({vac}) -- a conserved charge annihilates the vacuum's "
               f"fluctuations (halt-grade identity)")
    check(True, "L-I (a) consequence (frozen): for any conserved O the probe's connected "
                "two-time correlator is time-independent, so J(omega != 0) = 0 identically. "
                "Dynamic influence data CANNOT distinguish O = H from any conserved charge "
                "(UNDERDETERMINED), and conserved clock couplings contribute nothing to "
                "GR-1's zero-momentum pair channel", "note")
    R = {k: var(w, 0.5) / var(w, 2.0) for k, w in weights.items()}
    dq = abs(R["Q1"] / R["H"] - 1)
    dp = abs(R["P1"] / R["H"] - 1)
    check(dq > 1e-2 and dp > 1e-2, f"L-I GATE (b): static multi-temperature ratio "
                                   f"Var(T=0.5)/Var(T=2): H {R['H']:.5f}, Q1 {R['Q1']:.5f}, "
                                   f"P1 {R['P1']:.5f}; |R_Q1/R_H - 1| = {dq:.3f}, "
                                   f"|R_P1/R_H - 1| = {dp:.3f} (both > 1e-2): "
                                   f"distinguishable")
    lam = 3.7
    Rs = var([lam * x for x in weights["Q1"]], 0.5) / var([lam * x for x in weights["Q1"]], 2.0)
    di = abs(Rs - R["Q1"]) / R["Q1"]
    halt_check(di < 1e-14, f"L-I control: amplitude invariance R(3.7 O) = R(O) to {di:.1e} "
                           f"(the discriminator is amplitude-free; halt-grade)")
    return {"vacuum": vac, "ratios": R, "dQ1": dq, "dP1": dp, "amp_inv": di}


# ---------------- L-G: G-2 hop geometry of the probe-modified sector -----------------------------
def response_u(M, j, i, t, mmax=40):
    JM = mmul(J, M)
    v = [0.0] * D2
    v[N + j] = 1.0
    tot = 0.0
    fact = 1.0
    for m in range(1, mmax + 1):
        v = mvec(JM, v)
        fact *= m
        tot += v[i] * t ** m / fact
    return tot


def hop_hat(M, j, i):
    R = [abs(response_u(M, j, i, t)) for t in T3]
    s1 = math.log(R[1] / R[0]) / math.log(2)
    s2 = math.log(R[2] / R[1]) / math.log(2)
    return (2 * s1 - s2 - 1) / 2


def resistance(M, a, b):
    L = [[M[i][j] + 1.0 / N for j in range(N)] for i in range(N)]
    rhs = [0.0] * N
    rhs[a], rhs[b] = 1.0, -1.0
    n = N
    A = [row[:] + [rhs[i]] for i, row in enumerate(L)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            for kk in range(c, n + 1):
                A[r][kk] -= f * A[c][kk]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (A[r][n] - sum(A[r][kk] * x[kk] for kk in range(r + 1, n))) / A[r][r]
    return x[a] - x[b]


def leg_G():
    print("\n=== L-G: DISTINGUISH VIA G-2 SPECTRAL GEOMETRY (hop estimator on the retarded "
          "response) ===")
    nH = fnorm(MH)
    Mh = madd(MH, MH, HPROBE)
    Mq = madd(MH, mscale(MQ2, nH / fnorm(MQ2)), HPROBE)
    Mp = madd(MH, mscale(MP1, nH / fnorm(MP1)), HPROBE)
    dh = [hop_hat(Mh, 0, d) for d in (1, 2, 3, 4)]
    ok = all(abs(dh[d - 1] - d) < 0.3 for d in (1, 2, 3, 4))
    check(ok, f"L-G GATE O = H: hop estimates d_hat(0,d) = "
              f"{', '.join(f'{x:.3f}' for x in dh)} for d = 1..4 (each within 0.3 of d): "
              f"the unit change preserves the recovered geometry")
    dq = hop_hat(Mq, 0, 2)
    check(dq < 0.5, f"L-G GATE O = Q2: d_hat(0,2) = {dq:.3f} < 0.5 -- the constant probe "
                    f"REWIRES the recovered geometry (distance-2 sites become adjacent)")
    dp = hop_hat(Mp, 0, 1)
    check(dp < 0.8, f"L-G GATE O = P1: d_hat(0,1) = {dp:.3f} < 0.8 -- recovered geometry "
                    f"altered")
    uu = lambda M: [[M[i][j] for j in range(N)] for i in range(N)]
    r0 = resistance(uu(MH), 0, 8)
    rr = {nm: resistance(uu(M), 0, 8) / r0 for nm, M in (("H", Mh), ("Q2", Mq), ("P1", Mp))}
    check(True, f"L-G reported only: static resistance R(0,8) relative to unperturbed -- "
                f"H {rr['H']:.5f}, Q2 {rr['Q2']:.5f}, P1 {rr['P1']:.5f}", "note")
    return {"hop_H": dh, "hop_Q2_d2": dq, "hop_P1_d1": dp, "resistance_ratio": rr}


# ---------------- L-S: the candidate GeoInv selector ---------------------------------------------
def leg_S(tower):
    print("\n=== L-S: SELECT -- the candidate GeoInv ('a constant probe preserves the G-2 hop "
          "geometry') on the R = 3 tower ===")
    bas, null = tower
    e = [0.0] * D2
    e[N + 0] = 1.0
    powers = [e]
    for m in range(1, 9):
        powers.append(mvec(JMH, powers[-1]))

    def JMH_pow_apply(k, v):
        for _ in range(k):
            v = mvec(JMH, v)
        return v

    cols = []
    for v in null:
        MO = combo(bas, v)
        JMO = mmul(J, MO)
        col = []
        for d in (1, 2, 3, 4):
            for m in range(1, 2 * d + 1):
                deriv = [0.0] * D2
                for k in range(m):
                    w = JMH_pow_apply(m - 1 - k, mvec(JMO, powers[k]))
                    deriv = [a + b for a, b in zip(deriv, w)]
                col.append(deriv[d % N])
                col.append(deriv[(-d) % N])
        cols.append(col)
    sel = null_space_cols(cols)
    check(len(sel) == 1, f"L-S GATE: GeoInv leaves a null space of dim {len(sel)} in the "
                         f"{len(null)}-dim conserved tower (predicted 1)")
    res = None
    if sel:
        coef = [sum(sel[0][c] * null[c][b] for c in range(len(null))) for b in range(len(bas))]
        Ms = combo(bas, coef)
        a, b = fnorm(Ms), fnorm(MH)
        res = min(fnorm(madd(mscale(Ms, 1 / a), mscale(MH, 1 / b), -1.0)),
                  fnorm(madd(mscale(Ms, 1 / a), mscale(MH, 1 / b), 1.0)))
        check(res < 1e-8, f"L-S GATE: the GeoInv survivor is H itself, residual {res:.1e} "
                          f"< 1e-8")
    check(True, "L-S consequence (frozen): among the free sector's local conserved charges, "
                "'the constant probe preserves the recovered hop geometry' selects O ~ H "
                "exactly. GeoInv is NOT earned -- it is chartered as a candidate", "note")
    return {"dim": len(sel), "H_residual": res}


def adjudicate(dims, rP, rI, rG, rS, tower_dim):
    structural = all(dims[R] == 2 * R for R in dims)
    earned_dim = tower_dim if all(v >= -1e-10 for v in rP.values()) else None
    if earned_dim == 1:
        sel = "DERIVED"
    elif earned_dim is not None and earned_dim < tower_dim:
        sel = "CONSTRAINED-NONUNIQUE"
    else:
        sel = "IRREDUCIBLE INPUT" + (" (reduced to GeoInv)" if rS["dim"] == 1 else "")
    return {"structural": structural,
            "distinguish": {"dynamic_influence": "NO (UNDERDETERMINED)",
                            "static_multiT_influence": "YES" if rI["dQ1"] > 1e-2 else "NO",
                            "G2_hop_geometry": "YES" if (rG["hop_Q2_d2"] < 0.5 and
                                                         rG["hop_P1_d1"] < 0.8) else "NO"},
            "select": sel, "earned_dim": earned_dim, "tower_dim": tower_dim,
            "conditional_on": "C_cons (unresolved import)"}


def main():
    t0 = time.time()
    print("FS-1: CAN UNIT-CHANGE BE SELECTED FOR A GENUINELY FREE GAPLESS SECTOR? (charter "
          "frozen at 19fd85f)")
    dims, tower = leg_T()
    rP = leg_P(tower)
    rI = leg_I()
    rG = leg_G()
    rS = leg_S(tower)
    adj = adjudicate(dims, rP, rI, rG, rS, len(tower[1]))
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    check(True, f"STRUCTURAL free-sector exception: {adj['structural']}", "note")
    check(True, f"DISTINGUISH: {adj['distinguish']}", "note")
    check(True, f"SELECT: {adj['select']} (earned constraints leave {adj['earned_dim']} of "
                f"{adj['tower_dim']} tower dimensions); conditional on "
                f"{adj['conditional_on']}", "note")
    out = {"instrument": "fs1_free", "charter_commit": "19fd85f", "date": "2026-09-25",
           "LT": dims, "LP": rP, "LI": rI, "LG": rG, "LS": rS, "adjudication": adj,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "FS1_FREE_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nFS-1 FREE-SECTOR ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
