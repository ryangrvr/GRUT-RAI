#!/usr/bin/env python3
"""discriminator_d1: can two theories with the same K(t,t'), same effective observables, and
different microscopic interpretations be distinguished at all?

CHARTER: DISCRIMINATOR_CHARTER_01.md (pre-registration frozen at commit 53ab11f BEFORE this
instrument ran; worlds, access levels, thresholds and the E1-E4 classification are fixed there).

SCOPE: the exactly solvable Gaussian class, where the Feynman-Vernon influence functional of a
linearly coupled Gaussian bath is determined by the pair (K, N) and "same effective
observables" is decidable. Worlds: W-A star ("medium" representation, ground bath); W-B its
exact Lanczos chain (one theory twice, E-orthogonal); W-B' chain + two DECOUPLED hidden modes
(distinct micro-theory, identical (K,N)); W-D same Hamiltonian as A, THERMAL bath T = 0.8
(same K, different N); W-B'' 1%-perturbed chain (sensitivity control -- HALT if undetected).
Pure stdlib. Run: python3 calc/discriminator_d1.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig, matmul, transpose, matfunc, frob  # validated

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


M = 8
OMEGA_S2 = 1.0
T_THERMAL = 0.8
TGRID = [30.0 * i / 299 for i in range(300)]
EPS, DELTA = 1e-8, 1e-3

# declared star data (charter section 1)
W_MU = [0.4 + 1.8 * (mu + 0.5) / M for mu in range(M)]          # bath frequencies
C_MU = [0.15 * (1.0 + 0.5 * math.sin(2.3 * mu)) for mu in range(M)]  # couplings


class World:
    """A quadratic world: V (n x n, S at index 0) + bath initial state spec."""

    def __init__(self, name, V, bath_state):
        self.name, self.V, self.bath_state = name, V, bath_state
        self.n = len(V)
        lam, U = jacobi_eig(V)
        self.lam = [max(l, 1e-14) for l in lam]
        self.U = U

    def kernel_K(self):
        """GLE kernel K(t) = V_SE Omega_E^-1 sin(Omega_E t) V_ES (scalar, S = {0})."""
        E = list(range(1, self.n))
        VEE = [[self.V[i][j] for j in E] for i in E]
        vse = [self.V[0][j] for j in E]
        lam, U = jacobi_eig(VEE)
        Ut = transpose(U)
        w = []
        for mu in range(len(E)):
            om = math.sqrt(max(lam[mu], 1e-14))
            c = sum(vse[j] * Ut[mu][j] for j in range(len(E)))
            w.append((c * c, om))
        return [sum(c2 * math.sin(om * t) / om for c2, om in w) for t in TGRID]

    def kernel_N(self, T=0.0):
        """Noise kernel N(t) = sum c^2/(2 om) coth(om/2T) cos(om t) (T=0: coth=1)."""
        E = list(range(1, self.n))
        VEE = [[self.V[i][j] for j in E] for i in E]
        vse = [self.V[0][j] for j in E]
        lam, U = jacobi_eig(VEE)
        Ut = transpose(U)
        out = [0.0] * len(TGRID)
        for mu in range(len(E)):
            om = math.sqrt(max(lam[mu], 1e-14))
            c2 = sum(vse[j] * Ut[mu][j] for j in range(len(E))) ** 2
            coth = 1.0 if T <= 0 else 1.0 / math.tanh(om / (2.0 * T))
            for i, t in enumerate(TGRID):
                out[i] += c2 / (2.0 * om) * coth * math.cos(om * t)
        return out

    def initial_sigma(self):
        """Product state: S ground of isolated V[0][0]; bath in declared state of V_EE.
        Returns (sqq, sqp, spp) as n x n blocks (sqp = <qp+pq>/2 = 0 here)."""
        n = self.n
        E = list(range(1, n))
        VEE = [[self.V[i][j] for j in E] for i in E]
        if self.bath_state == "ground":
            f_q = lambda x: 1.0 / (2.0 * math.sqrt(max(x, 1e-14)))
            f_p = lambda x: math.sqrt(max(x, 1e-14)) / 2.0
        else:  # thermal
            f_q = lambda x: (1.0 / math.tanh(math.sqrt(max(x, 1e-14)) / (2 * T_THERMAL))) \
                / (2.0 * math.sqrt(max(x, 1e-14)))
            f_p = lambda x: (1.0 / math.tanh(math.sqrt(max(x, 1e-14)) / (2 * T_THERMAL))) \
                * math.sqrt(max(x, 1e-14)) / 2.0
        Bq = matfunc(VEE, f_q)
        Bp = matfunc(VEE, f_p)
        ws = math.sqrt(self.V[0][0])
        sqq = [[0.0] * n for _ in range(n)]
        spp = [[0.0] * n for _ in range(n)]
        sqq[0][0] = 1.0 / (2.0 * ws)
        spp[0][0] = ws / 2.0
        for a, i in enumerate(E):
            for b, j in enumerate(E):
                sqq[i][j] = Bq[a][b]
                spp[i][j] = Bp[a][b]
        return sqq, spp

    def sigma_S_traj(self, block):
        """Exact reduced covariance trajectory on the site-set `block`:
        returns list over t of the 2|B| x 2|B| covariance (qq, qp; pq, pp) entries."""
        sqq0, spp0 = self.initial_sigma()
        U, lam = self.U, self.lam
        Ut = transpose(U)
        traj = []
        for t in TGRID:
            cosd = [math.cos(math.sqrt(l) * t) for l in lam]
            sind = [math.sin(math.sqrt(l) * t) for l in lam]
            A = matmul(matmul(U, [[cosd[i] if i == j else 0.0 for j in range(self.n)]
                                  for i in range(self.n)]), Ut)
            B = matmul(matmul(U, [[sind[i] / math.sqrt(lam[i]) if i == j else 0.0
                                   for j in range(self.n)] for i in range(self.n)]), Ut)
            C = matmul(matmul(U, [[-sind[i] * math.sqrt(lam[i]) if i == j else 0.0
                                   for j in range(self.n)] for i in range(self.n)]), Ut)
            # sigma_qq(t) = A sqq0 A^T + B spp0 B^T ; sigma_pp(t) = C sqq0 C^T + A spp0 A^T
            # sigma_qp(t) = A sqq0 C^T + B spp0 A^T
            qq = matmul(matmul(A, sqq0), transpose(A))
            qq2 = matmul(matmul(B, spp0), transpose(B))
            pp = matmul(matmul(C, sqq0), transpose(C))
            pp2 = matmul(matmul(A, spp0), transpose(A))
            qp = matmul(matmul(A, sqq0), transpose(C))
            qp2 = matmul(matmul(B, spp0), transpose(A))
            m = []
            for i in block:
                row = []
                for j in block:
                    row.append(qq[i][j] + qq2[i][j])
                for j in block:
                    row.append(qp[i][j] + qp2[i][j])
                m.append(row)
            for i in block:
                row = []
                for j in block:
                    row.append(qp[j][i] + qp2[j][i])
                for j in block:
                    row.append(pp[i][j] + pp2[i][j])
                m.append(row)
            traj.append(m)
        return traj


# ------------------------------- world builders ---------------------------------------------
def build_A():
    n = 1 + M
    V = [[0.0] * n for _ in range(n)]
    V[0][0] = OMEGA_S2
    for mu in range(M):
        V[1 + mu][1 + mu] = W_MU[mu] ** 2
        V[0][1 + mu] = -C_MU[mu]
        V[1 + mu][0] = -C_MU[mu]
    return World("W-A(star,ground)", V, "ground")


def lanczos_chain(perturb=0.0):
    """Tridiagonalize diag(w_mu^2) from start vector c/||c||; full reorthogonalization."""
    d = [w * w for w in W_MU]
    nrm = math.sqrt(sum(c * c for c in C_MU))
    v = [c / nrm for c in C_MU]
    Vs, alphas, betas = [v[:]], [], []
    for k in range(M):
        w = [d[i] * Vs[k][i] for i in range(M)]
        a = sum(w[i] * Vs[k][i] for i in range(M))
        alphas.append(a)
        for vv in Vs:  # full reorthogonalization
            proj = sum(w[i] * vv[i] for i in range(M))
            w = [w[i] - proj * vv[i] for i in range(M)]
        b = math.sqrt(sum(x * x for x in w))
        if k < M - 1:
            betas.append(b)
            Vs.append([x / max(b, 1e-300) for x in w])
    if perturb:
        betas[2] *= (1.0 + perturb)
    T = [[0.0] * M for _ in range(M)]
    for k in range(M):
        T[k][k] = alphas[k]
        if k < M - 1:
            T[k][k + 1] = betas[k]
            T[k + 1][k] = betas[k]
    return T, nrm


def build_chain(name, extra_modes=(), perturb=0.0):
    T, nrm = lanczos_chain(perturb)
    Me = M + len(extra_modes)
    n = 1 + Me
    V = [[0.0] * n for _ in range(n)]
    V[0][0] = OMEGA_S2
    for i in range(M):
        for j in range(M):
            V[1 + i][1 + j] = T[i][j]
    V[0][1] = -nrm
    V[1][0] = -nrm
    for a, w2 in enumerate(extra_modes):
        V[1 + M + a][1 + M + a] = w2
    return World(name, V, "ground")


def build_D():
    w = build_A()
    return World("W-D(star,thermal T=0.8)", w.V, "thermal")


# ------------------------------- metrics -----------------------------------------------------
def rel_max(xs, ys, scale):
    return max(abs(a - b) for a, b in zip(xs, ys)) / scale


def traj_delta(t1, t2, scale):
    return max(frob([[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(m1, m2)])
               for m1, m2 in zip(t1, t2)) / scale


def with_probe(w):
    """Attach a probe oscillator to S only (charter L2)."""
    n = w.n + 1
    V = [[0.0] * n for _ in range(n)]
    for i in range(w.n):
        for j in range(w.n):
            V[i][j] = w.V[i][j]
    g, wp2 = 0.05, 0.49
    V[0][0] += g
    V[n - 1][n - 1] = wp2 + g
    V[0][n - 1] = -g
    V[n - 1][0] = -g
    return World(w.name + "+probe", V, w.bath_state)


def main():
    t0 = time.time()
    print("DISCRIMINATOR D-1 (charter: DISCRIMINATOR_CHARTER_01.md, frozen at 53ab11f)")
    A = build_A()
    B = build_chain("W-B(chain,ground)")
    Bp = build_chain("W-B'(chain+2 hidden,ground)", extra_modes=(2.89, 0.36))
    Bpp = build_chain("W-B''(chain,1% perturbed)", perturb=0.01)
    D = build_D()

    print("\n=== KERNEL IDENTITIES (L3 partial) ===")
    KA = A.kernel_K()
    scaleK = max(abs(x) for x in KA)
    dK = {w.name: rel_max(KA, w.kernel_K(), scaleK) for w in (B, Bp, Bpp, D)}
    for nm, v in dK.items():
        print(f"  Delta_K(A, {nm}) = {v:.2e}")
    check(dK[B.name] < EPS and dK[Bp.name] < EPS, "K identical for A/B/B' (Lanczos exactness)")
    check(dK[D.name] < EPS, "K identical for A/D (state-independence of the kernel)")
    check(dK[Bpp.name] > DELTA, f"sensitivity: 1% perturbation shifts K by {dK[Bpp.name]:.1e} > 1e-3", "ctrl")
    NA = A.kernel_N(0.0)
    ND = D.kernel_N(T_THERMAL)
    NBp = Bp.kernel_N(0.0)
    scaleN = max(abs(x) for x in NA)
    check(rel_max(NA, NBp, scaleN) < EPS, "N identical for A/B' (same influence data)")
    check(rel_max(NA, ND, scaleN) > DELTA,
          f"N differs for A/D by {rel_max(NA, ND, scaleN):.2f} (same K, different fluctuations)")

    print("\n=== L1: S-LOCAL ACCESS (exact covariance trajectories) ===")
    trA = A.sigma_S_traj([0])
    scale1 = max(frob(m) for m in trA)
    d1 = {}
    for w in (B, Bp, Bpp, D):
        d1[w.name] = traj_delta(trA, w.sigma_S_traj([0]), scale1)
        print(f"  Delta_1(A, {w.name}) = {d1[w.name]:.2e}")

    print("\n=== L2: ENLARGED NON-E ACCESS (S + probe) ===")
    trAp = with_probe(A).sigma_S_traj([0, A.n])  # probe is last site of the probed world
    scale2 = max(frob(m) for m in trAp)
    d2 = {}
    for w in (B, Bp):
        wp = with_probe(w)
        d2[w.name] = traj_delta(trAp, wp.sigma_S_traj([0, w.n]), scale2)
        print(f"  Delta_2(A, {w.name}) = {d2[w.name]:.2e}")

    print("\n=== L3: FULL-THEORY INVARIANTS ===")
    specA = sorted(A.lam)
    specB = sorted(B.lam)
    specBp = sorted(Bp.lam)
    same_AB = A.n == B.n and max(abs(a - b) for a, b in zip(specA, specB)) < 1e-9
    diff_ABp = (A.n != Bp.n)
    print(f"  dim(A) = {A.n}, dim(B) = {B.n}, dim(B') = {Bp.n}")
    check(same_AB, "A and B: same dimension, same full spectrum (one theory, two representations)")
    check(diff_ABp, "A and B': different dimension (genuinely non-isomorphic micro-theories)")

    print("\n=== CLASSIFICATION (charter section 3, mechanical) ===")
    E3 = d1[Bpp.name] > DELTA
    check(E3, f"E3 sensitivity: Delta_1(A,B'') = {d1[Bpp.name]:.1e} > 1e-3 -- metrics detect a 1% "
              "influence-data difference", "ctrl")
    if not E3:
        print("\nHALT: metrics too dull; no verdict.")
        sys.exit(1)
    E1 = dK[Bp.name] < EPS and d1[Bp.name] < EPS and d2[Bp.name] < EPS and diff_ABp
    E2 = dK[D.name] < EPS and d1[D.name] > DELTA
    E4 = dK[B.name] < EPS and d1[B.name] < EPS and d2[B.name] < EPS and same_AB
    check(E1, "E1 UNDERDETERMINATION: same-(K,N) micro-distinct theories are S-indistinguishable "
              f"at every tested access level (Delta_1 = {d1[Bp.name]:.1e}, Delta_2 = {d2[Bp.name]:.1e}) "
              "while full-theory invariants differ")
    check(E2, f"E2 NOISE CHANNEL: kernel-equal, state-different theories ARE S-distinguishable "
              f"(Delta_1(A,D) = {d1[D.name]:.2f})")
    check(E4, "E4 REPRESENTATION: the star/chain pair is one theory twice (all levels equal, "
              "invariants identical)")
    if E1 and E2 and E4:
        answer = ("NO at fixed influence data (K, N) and S-limited access; "
                  "YES across influence-data classes")
        conseq = ("the medium-vs-relational dispute is REPRESENTATIONAL at fixed (K, N); any "
                  "genuine ontology-level discriminator must live in what CONSTRAINS the (K, N) "
                  "pair, not in the kernel alone")
    elif not E1:
        answer = "YES inside the tested class -- same-(K,N) theories were distinguished"
        conseq = "report the distinguishing observable; the equivalence theorem is violated"
    else:
        answer = "the equivalence class is larger than (K, N)"
        conseq = "the noise channel failed to discriminate; report"
    check(True, f"ANSWER: {answer}", "note")
    check(True, f"CONSEQUENCE: {conseq}", "note")

    out = {"instrument": "discriminator_d1", "charter_commit": "53ab11f", "date": "2026-09-25",
           "worlds": {w.name: {"dim": w.n} for w in (A, B, Bp, Bpp, D)},
           "delta_K": dK, "delta_L1": d1, "delta_L2": d2,
           "noise_delta_AD": rel_max(NA, ND, scaleN),
           "L3": {"same_A_B": same_AB, "nonisomorphic_A_Bprime": diff_ABp},
           "E": {"E1": E1, "E2": E2, "E3": E3, "E4": E4},
           "answer": answer, "consequence": conseq,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "scope": "Gaussian class, factorized initial state; the gravitational-sector pointer "
                    "(state-dependent noise; the O(H^2) FDT/KMS obstruction) is a pointer, not a "
                    "computation; noise fork stays owner-held",
           "hard_stop": "verdict recorded; owner rules on the vocabularies and orders P-2 or otherwise"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "DISCRIMINATOR_D1_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nDISCRIMINATOR D-1: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print("HARD STOP: verdict recorded pending owner ruling on the vocabularies.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
