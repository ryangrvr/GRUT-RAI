#!/usr/bin/env python3
"""p5_access: attack the access structure itself.

CHARTER: P5_ACCESS_CHARTER_01.md (pre-registration frozen at commit 4013a32 BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5827176252). "Access structure" is
a CANDIDATE, not an axiom, tested across: representational choice vs dynamically
constrained structure vs genuinely additional physical structure. Binding tightening
carried from P-4 acceptance: "access is the last place a new principle could hide" is NOT
a theorem -- it is the remainder this instrument attacks.

Legs: L-E entangling-refactorization positive control (mere representation) | L-A
inequivalent declarations, bath-small vs bath-big + decoupled hidden sector | L-B/C
dynamically generated algebra closure of {I, H, B} (generic 16 / parity-commutant 8 /
abelian small; seed residual reported; bicommutant CITED -- NULL-REDUNDANT) | L-D the
counterattack: hidden-A vs hidden-B, identical in-access hierarchy, different
out-of-access <sz2(t)>, different post-quench coherence after the access-extension
B -> B + 0.4 sx2 at t* = 3.0.

Pure stdlib. Run: python3 calc/p5_access.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3_nc_lift import cmat, cmul, cdag

FAIL = []
CHECKS = []
HALT = []  # analytic-identity breaches: instrument bugs, never physics


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


def halt_check(ok, msg):
    """Frozen control rule: a breach of an analytic identity HALTS as an instrument bug."""
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---------------- operator construction (bit i = spin i; bit 0 -> up, bit 1 -> down) ---------
def pauli(nq, i, ax):
    d = 2 ** nq
    M = cmat(d)
    for n in range(d):
        up = (n >> i) & 1 == 0
        if ax == "z":
            M[n][n] = 1.0 + 0j if up else -1.0 + 0j
        elif ax == "x":
            M[n][n ^ (1 << i)] = 1.0 + 0j
        elif ax == "y":
            M[n][n ^ (1 << i)] = -1j if up else 1j
    return M


def madd(*terms):
    d = len(terms[0][1])
    M = cmat(d)
    for c, A in terms:
        for i in range(d):
            for j in range(d):
                M[i][j] += c * A[i][j]
    return M


def mnorm(A):
    return max(sum(abs(x) for x in row) for row in A)  # max row-sum norm


def mdiff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A)))


def expm(A):
    """exp(A) by exact scaling-and-squaring (power-of-two divisor) + Taylor."""
    d = len(A)
    s = 0
    while mnorm(A) / (2 ** s) > 0.5:
        s += 1
    B = [[A[i][j] / (2 ** s) for j in range(d)] for i in range(d)]
    E = [[(1.0 + 0j) if i == j else 0j for j in range(d)] for i in range(d)]
    T = [row[:] for row in E]
    for k in range(1, 40):
        T = cmul(T, B)
        T = [[T[i][j] / k for j in range(d)] for i in range(d)]
        for i in range(d):
            for j in range(d):
                E[i][j] += T[i][j]
        if mnorm(T) < 1e-24:
            break
    for _ in range(s):
        E = cmul(E, E)
    return E


def mvec(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(v))]


def vdot(u, v):
    return sum(u[k].conjugate() * v[k] for k in range(len(u)))


# ---------------- pure-dephasing evolution (lambda = 1, frozen) -------------------------------
DT = 0.05
NT = 200  # grid t_k = k*DT, k = 1..200 -> t in (0, 10]
TSTAR_STEP = 60  # t* = 3.0 (frozen quench time, exact grid multiple)


def coherence(H, B, psi0, quench_B=None):
    """C(t_k) = <psi0| U_-(t)^dag U_+(t) |psi0>, H_pm = H +/- B; optional B -> quench_B at t*.
    Exact stepping: U(k dt) = U(dt)^k. Returns (C list, psi_plus branch snapshots list)."""
    Up = expm([[-1j * DT * (H[i][j] + B[i][j]) for j in range(len(H))] for i in range(len(H))])
    Um = expm([[-1j * DT * (H[i][j] - B[i][j]) for j in range(len(H))] for i in range(len(H))])
    pp, pm = psi0[:], psi0[:]
    C, snaps = [], []
    for k in range(1, NT + 1):
        if quench_B is not None and k == TSTAR_STEP + 1:
            Up = expm([[-1j * DT * (H[i][j] + quench_B[i][j]) for j in range(len(H))]
                       for i in range(len(H))])
            Um = expm([[-1j * DT * (H[i][j] - quench_B[i][j]) for j in range(len(H))]
                       for i in range(len(H))])
        pp = mvec(Up, pp)
        pm = mvec(Um, pm)
        C.append(vdot(pm, pp))
        snaps.append((pp[:], pm[:]))
    return C, snaps


def cdiff(CA, CB, lo=0, hi=NT):
    return max(abs(CA[k] - CB[k]) for k in range(lo, hi))


# ---------------- L-E: positive control for MERE REPRESENTATION -------------------------------
def leg_E():
    print("\n=== L-E: ENTANGLING REFACTORIZATION (positive control for representation) ===")
    nq, d = 3, 8
    H = madd((0.5, pauli(3, 0, "z")), (0.5, pauli(3, 1, "z")), (0.5, pauli(3, 2, "z")))
    B = madd((0.5, pauli(3, 0, "x")), (0.4, pauli(3, 1, "x")), (0.3, pauli(3, 2, "x")))
    psi0 = [0j] * d
    psi0[d - 1] = 1.0 + 0j  # |ddd> ground state of H
    XZ = cmul(pauli(3, 1, "x"), pauli(3, 2, "z"))
    V = expm([[-1j * 0.7 * XZ[i][j] for j in range(d)] for i in range(d)])
    Vd = cdag(V)
    Hp = cmul(V, cmul(H, Vd))
    Bp = cmul(V, cmul(B, Vd))
    psi0p = mvec(V, psi0)
    check(mdiff(Hp, H) > 0.1 and mdiff(Bp, B) > 0.1,
          f"L-E refactorization is nontrivial: |H'-H| = {mdiff(Hp, H):.3f}, "
          f"|B'-B| = {mdiff(Bp, B):.3f} (genuinely noncommuting recombination)")
    C0, _ = coherence(H, B, psi0)
    C1, _ = coherence(Hp, Bp, psi0p)
    dmax = cdiff(C0, C1)
    halt_check(dmax < 1e-9,
               f"L-E GATE: coherence identical under entangling refactorization, "
               f"max diff = {dmax:.2e} < 1e-9 (analytic identity; breach would HALT)")
    check(True, "L-E verdict component: the factorization/embedding is REPRESENTATIONAL -- "
                "an entangling recombination of the declared subsystems changes nothing "
                "observable through the declared access", "note")
    return dmax


# ---------------- L-A: inequivalent declarations ----------------------------------------------
def leg_A():
    print("\n=== L-A: INEQUIVALENT DECLARATIONS (bath-small vs bath-big + hidden) ===")
    Hs = madd((0.5, pauli(1, 0, "z")))
    Bs = madd((0.5, pauli(1, 0, "x")))
    ps = [0j, 1.0 + 0j]  # |d>
    Cs, _ = coherence(Hs, Bs, ps)
    Hb = madd((0.5, pauli(3, 0, "z")),
              (0.8, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))), (0.3, pauli(3, 1, "z")))
    Bb = madd((0.5, pauli(3, 0, "x")))
    pb = [0j] * 8
    pb[7] = 1.0 + 0j  # |ddd>
    Cb, _ = coherence(Hb, Bb, pb)
    dmax = cdiff(Cs, Cb)
    halt_check(dmax < 1e-9,
               f"L-A GATE: in-access coherence identical across inequivalent declarations, "
               f"max diff = {dmax:.2e} < 1e-9 (analytic: decoupled commuting factor)")
    check(True, "L-A verdict component: the declared partition difference (different total "
                "algebras, identical coupling map) changes nothing coupled -- access as "
                "bookkeeping is REPRESENTATIONAL for uncoupled structure", "note")
    return dmax


# ---------------- L-B/C: dynamically generated algebra closure --------------------------------
def hs_flat(A):
    return [A[i][j] for i in range(len(A)) for j in range(len(A))]


def closure_dim(gens, d, max_sweeps=8):
    """Dimension of the algebra generated by gens under products: Hilbert-Schmidt
    Gram-Schmidt span, iterated product sweeps to stability. Returns (dim, stable)."""
    basis = []  # orthonormal flattened HS vectors
    mats = []

    def add(M):
        v = hs_flat(M)
        for b in basis:
            c = sum(x.conjugate() * y for x, y in zip(b, v))
            v = [y - c * x for x, y in zip(b, v)]
        nrm = math.sqrt(sum(abs(x) ** 2 for x in v))
        if nrm > 1e-8:
            basis.append([x / nrm for x in v])
            mats.append(M)
            return True
        return False

    for G in gens:
        add(G)
    for _ in range(max_sweeps):
        grew = False
        cur = list(mats)
        for A in cur:
            for Bm in cur:
                if add(cmul(A, Bm)):
                    grew = True
        if not grew:
            break
    dim = len(basis)
    extra = False  # stability control: one extra full sweep must not grow the span
    cur = list(mats)
    for A in cur:
        for Bm in cur:
            if add(cmul(A, Bm)):
                extra = True
    return dim, not extra


def leg_BC():
    print("\n=== L-B/C: DYNAMICALLY GENERATED ALGEBRA (closure of {I, H, B}) ===")
    d = 4
    I4 = [[(1.0 + 0j) if i == j else 0j for j in range(d)] for i in range(d)]
    z1, z2 = pauli(2, 0, "z"), pauli(2, 1, "z")
    x1, y2 = pauli(2, 0, "x"), pauli(2, 1, "y")
    xx = cmul(pauli(2, 0, "x"), pauli(2, 1, "x"))
    zz = cmul(z1, z2)

    Hg = madd((0.9, z1), (1.1, z2), (0.7, xx))
    Bg = madd((0.5, x1), (0.3, y2))
    dg, sg = closure_dim([I4, Hg, Bg], d)
    check(dg == 16 and sg, f"L-B/C case (i) generic seed + generic H: closure dim = {dg} "
                           f"(expected 16, full algebra), stable = {sg}")

    Hp = madd((0.9, z1), (1.1, z2), (0.7, xx))
    Bp = madd((0.5, xx), (0.3, z1))
    dp, sp = closure_dim([I4, Hp, Bp], d)
    check(dp == 8 and sp, f"L-B/C case (ii) parity-symmetric ([., z1z2] = 0): closure dim = {dp} "
                          f"(expected 8, the commutant block), stable = {sp}")

    Ha = madd((0.6, z1), (0.8, z2))
    Ba = madd((0.4, zz))
    da, sa = closure_dim([I4, Ha, Ba], d)
    check(da < 8 and sa, f"L-B/C case (iii) abelian seed, commuting H: closure dim = {da} "
                         f"(small, measured), stable = {sa}")

    dseed, _ = closure_dim([I4, Ba], d)
    check(True, f"SEED RESIDUAL (reported, not absorbed): same dynamics, seed {{I, B}} alone "
                f"closes at dim {dseed} vs dim {da} for {{I, H, B}} -- the closure is canonical "
                f"GIVEN a seed; the seed itself remains a declaration", "note")
    check(True, "ADJUDICATION (frozen): symmetry constrains the closure to the commutant -- "
                "bicommutant theory CITED as standard mathematics; as a candidate new "
                "principle this is NULL-REDUNDANT. Seedless minimality: no canonical "
                "selection generically (P-1 trichotomy carries) -- class UNDERDETERMINED",
          "note")
    return {"generic": dg, "parity": dp, "abelian": da, "seed_residual": dseed}


# ---------------- L-D: the counterattack ------------------------------------------------------
def build_D(hidden):
    H = madd((0.5, pauli(3, 0, "z")), *hidden)
    B = madd((0.5, pauli(3, 0, "x")))
    Bq = madd((0.5, pauli(3, 0, "x")), (0.4, pauli(3, 1, "x")))  # access extension at t*
    psi0 = [0j] * 8
    psi0[7] = 1.0 + 0j
    return H, B, Bq, psi0


def sz2_traj(snaps):
    Z2 = pauli(3, 1, "z")
    out = []
    for pp, pm in snaps:
        ep = vdot(pp, mvec(Z2, pp)).real
        em = vdot(pm, mvec(Z2, pm)).real
        out.append(0.5 * (ep + em))
    return out


def leg_D():
    print("\n=== L-D: THE COUNTERATTACK (hidden-A vs hidden-B) ===")
    hidA = [(0.8, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))), (0.3, pauli(3, 1, "z"))]
    hidB = [(-1.1, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))), (0.6, pauli(3, 2, "z"))]
    HA, BA, BqA, p0 = build_D(hidA)
    HB, BB, BqB, _ = build_D(hidB)

    CA, snapsA = coherence(HA, BA, p0)
    CB, snapsB = coherence(HB, BB, p0)
    d_in = cdiff(CA, CB)
    halt_check(d_in < 1e-9,
               f"L-D GATE (i) in-access: probe coherence identical on all of (0, 10], "
               f"max diff = {d_in:.2e} < 1e-9 (analytic: hidden sectors decoupled)")

    zA, zB = sz2_traj(snapsA), sz2_traj(snapsB)
    CA2, snapsA2 = coherence(HA, BA, p0)  # matched control: hidden-A rebuilt and rerun
    zA2 = sz2_traj(snapsA2)
    ctrl_z = max(abs(a - b) for a, b in zip(zA, zA2))
    d_out = max(abs(a - b) for a, b in zip(zA, zB))
    check(ctrl_z < 1e-12, f"L-D matched control (hidden-A vs hidden-A): out-of-access "
                          f"trajectory diff = {ctrl_z:.1e} < 1e-12", "ctrl")
    check(d_out > 0.05, f"L-D GATE (ii) out-of-access: max |<sz2(t)>_A - <sz2(t)>_B| = "
                        f"{d_out:.3f} > 0.05 -- the constructions differ physically")

    CqA, _ = coherence(HA, BA, p0, quench_B=BqA)
    CqB, _ = coherence(HB, BB, p0, quench_B=BqB)
    CqA2, _ = coherence(HA, BA, p0, quench_B=BqA)
    ctrl_q = cdiff(CqA, CqA2)
    d_pre = cdiff(CqA, CqB, 0, TSTAR_STEP)
    d_post = cdiff(CqA, CqB, TSTAR_STEP, NT)
    check(ctrl_q < 1e-12, f"L-D matched control (quench, hidden-A vs hidden-A): "
                          f"diff = {ctrl_q:.1e} < 1e-12", "ctrl")
    halt_check(d_pre < 1e-9, f"L-D GATE (iii-pre): pre-quench coherence identical, "
                             f"max diff = {d_pre:.2e} < 1e-9")
    check(d_post > 1e-3, f"L-D GATE (iii-post): post-quench (B -> B + 0.4 sx2 at t* = 3.0) "
                         f"coherence differs, max diff = {d_post:.4f} > 1e-3")

    check(True, "L-D verdict component (frozen consequence rule): (i)+(ii) => ACCESS-SPLIT -- "
                "the access boundary is underdetermining: in-access influence data cannot fix "
                "out-of-access physics; (iii) => the split is CONDITIONALLY PHYSICAL: "
                "invisible forever under fixed access, consequential exactly when access "
                "changes", "note")
    return {"in_access": d_in, "out_access": d_out, "pre_quench": d_pre, "post_quench": d_post,
            "ctrl_z": ctrl_z, "ctrl_q": ctrl_q}


# ---------------- main ------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("P-5: ATTACK THE ACCESS STRUCTURE (charter frozen at 4013a32)")
    dE = leg_E()
    dA = leg_A()
    dims = leg_BC()
    dD = leg_D()

    print("\n=== COMPOSITE (frozen taxonomy; components reported separately) ===")
    check(True, "REPRESENTATIONAL: factorization/embedding and partition bookkeeping "
                "(L-E, L-A gates)", "note")
    check(True, "DYNAMICALLY-CONSTRAINED: the generated algebra GIVEN a seed (L-B/C dims "
                "16/8/small as declared) -- with the seed reported as the residual "
                "declaration", "note")
    check(True, "NULL-REDUNDANT: the symmetry constraint (bicommutant = standard structure); "
                "no new principle", "note")
    check(True, "ACCESS-SPLIT, CONDITIONALLY PHYSICAL: L-D gates -- identical in-access "
                "hierarchy, different out-of-access physics, difference exposed exactly "
                "when access extends", "note")
    check(True, "UNDERDETERMINED: seedless minimality -- generically no canonical seed "
                "selection", "note")

    out = {"instrument": "p5_access", "charter_commit": "4013a32", "date": "2026-09-25",
           "grid": {"dt": DT, "nt": NT, "t_star": TSTAR_STEP * DT},
           "LE_maxdiff": dE, "LA_maxdiff": dA, "LBC_dims": dims, "LD": dD,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "P5_ACCESS_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nP-5 ACCESS ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}; "
          f"halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
