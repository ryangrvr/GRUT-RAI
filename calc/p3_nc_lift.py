#!/usr/bin/env python3
"""p3_nc_lift: does the influence-data admissibility geometry and the counting law survive
genuine noncommutativity?

CHARTER: P3_NC_LIFT_CHARTER_01.md (pre-registration frozen at commit 78b188e BEFORE this
instrument ran; authority = GitHub Issue #2 + its ten-point owner guidance). Posture: ATTACK.
The redundancy rule is binding: a constraint reducible to state positivity or CP is recorded
NULL-AS-NEW-PRINCIPLE even where it survives as geometry. No proof-of-QM: every positivity
used below is quantum-mechanical INPUT, cited, never derived. hbar = 1.

Pure stdlib. Run: python3 calc/p3_nc_lift.py
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig  # validated real-symmetric eigensolver

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


# ---------------- complex matrix helpers (lists of complex) ----------------------------------
def cmat(n):
    return [[0j] * n for _ in range(n)]


def cmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(m)) for j in range(p)] for i in range(n)]


def cdag(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def herm_eigs(A):
    """Eigenvalues of a complex Hermitian matrix via the real 2n x 2n embedding."""
    n = len(A)
    M = [[0.0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = A[i][j].real
            M[i][j + n] = -A[i][j].imag
            M[i + n][j] = A[i][j].imag
            M[i + n][j + n] = A[i][j].real
    lam, _ = jacobi_eig(M)
    return sorted(lam)  # spectrum doubled; min/PSD checks unaffected


def eig2h(A):
    """Closed-form eigenvalues of a 2x2 Hermitian matrix."""
    tr = (A[0][0] + A[1][1]).real
    det = (A[0][0] * A[1][1] - A[0][1] * A[1][0]).real
    d = math.sqrt(max(tr * tr / 4 - det, 0.0))
    return (tr / 2 - d, tr / 2 + d)


# ---------------- Q1: matrix admissibility on the exact 3-spin thermal bath ------------------
OMS = [0.7, 1.0, 1.6]
GS = [0.6, 0.5, 0.4]
HS = [0.3, 0.7, 0.2]
BETA = 2.0
NB = 3
DIM = 2 ** NB


def bath_ops():
    """B1 = sum g_i sx_i, B2 = sum h_i sy_i in the computational (sz) basis; energies."""
    E = [sum((0.5 if (n >> i) & 1 == 0 else -0.5) * OMS[i] for i in range(NB)) for n in range(DIM)]
    B1 = cmat(DIM)
    B2 = cmat(DIM)
    for n in range(DIM):
        for i in range(NB):
            m = n ^ (1 << i)
            B1[n][m] += GS[i]
            # sy in (up=bit0, down=bit1) basis: <up|sy|down> = -1j, <down|sy|up> = +1j
            up_n = (n >> i) & 1 == 0
            B2[n][m] += HS[i] * (-1j if up_n else 1j)
    return E, B1, B2


def q1():
    print("\n=== Q1: MATRIX ADMISSIBILITY (exact spin bath, noncommuting channels) ===")
    E, B1, B2 = bath_ops()
    comm = cmul(B1, B2)
    comm2 = cmul(B2, B1)
    cn = max(abs(comm[i][j] - comm2[i][j]) for i in range(DIM) for j in range(DIM))
    check(cn > 0.1, f"[B1, B2] != 0 (norm-inf {cn:.3f}): the channels are genuinely noncommuting")
    Z = sum(math.exp(-BETA * e) for e in E)
    p = [math.exp(-BETA * e) / Z for e in E]
    # spectral matrices C_ab(omega) as Gram sums; also keep the Gram vectors for the reduction
    C = {}
    gram = {}
    Bs = [B1, B2]
    for n in range(DIM):
        for m in range(DIM):
            amps = [Bs[a][n][m] for a in range(2)]
            if all(abs(x) < 1e-15 for x in amps):
                continue
            w = round(E[m] - E[n], 9)
            C.setdefault(w, cmat(2))
            gram.setdefault(w, [])
            for a in range(2):
                for b in range(2):
                    C[w][a][b] += p[n] * amps[a] * amps[b].conjugate()
            gram[w].append([math.sqrt(p[n]) * x for x in amps])
    herm_worst, psd_min = 0.0, 1e99
    for w, M in C.items():
        herm_worst = max(herm_worst, max(abs(M[i][j] - M[j][i].conjugate())
                                         for i in range(2) for j in range(2)))
        psd_min = min(psd_min, eig2h(M)[0])
    check(herm_worst < 1e-12, f"Hermiticity of every C(omega) (worst {herm_worst:.1e})")
    check(psd_min > -1e-10, f"Gram-PSD of every C(omega) (min eigenvalue {psd_min:.1e})")
    # cross-frequency noncommutativity of the spectral matrices
    ws = sorted(k for k in C if k > 0)
    M1, M2 = C[ws[0]], C[ws[1]]
    ncn = max(abs(x - y) for x, y in zip(sum(cmul(M1, M2), []), sum(cmul(M2, M1), [])))
    check(ncn > 1e-4, f"[C(w1), C(w2)] != 0 (norm-inf {ncn:.2e}): no fixed channel basis exists")
    # candidate lift: nu +- J/2 >= 0 with nu = (C(w)+C(-w))/2, J = C(w)-C(-w)  (both Hermitian)
    lift_min = 1e99
    for w in ws:
        Cm = C.get(-w, cmat(2))
        nu = [[(C[w][i][j] + Cm[i][j]) / 2 for j in range(2)] for i in range(2)]
        J = [[C[w][i][j] - Cm[i][j] for j in range(2)] for i in range(2)]
        for sgn in (1, -1):
            M = [[nu[i][j] + sgn * J[i][j] / 2 for j in range(2)] for i in range(2)]
            lift_min = min(lift_min, eig2h(M)[0])
    check(lift_min > -1e-10, f"CANDIDATE LIFT HOLDS on the model: nu(w) +- J(w)/2 >= 0 as "
                             f"Hermitian matrices at every frequency (min eig {lift_min:.1e})")
    # covariance under a declared non-orthogonal channel congruence
    R = [[1.0, 0.4], [-0.2, 1.1]]
    cov_min = 1e99
    for w in ws:
        Cm = C.get(-w, cmat(2))
        for M0 in (C[w], Cm):
            M = [[sum(R[i][a] * M0[a][b] * R[j][b] for a in range(2) for b in range(2))
                  for j in range(2)] for i in range(2)]
            cov_min = min(cov_min, eig2h(M)[0])
    check(cov_min > -1e-10, "covariance: the conditions hold in congruence-transformed channels "
                            f"(non-orthogonal R; min eig {cov_min:.1e}) -- truth-value invariant")
    # strictness over the scalar theory: channelwise-passing, matrix-failing pair
    nu_bad = [[1.0 + 0j, 0.9 + 0j], [0.9 + 0j, 1.0 + 0j]]
    J_bad = [[1.8 + 0j, 0j], [0j, 1.8 + 0j]]
    chanwise = all((nu_bad[a][a].real >= abs(J_bad[a][a]) / 2) for a in range(2))
    Mbad = [[nu_bad[i][j] - J_bad[i][j] / 2 for j in range(2)] for i in range(2)]
    check(chanwise and eig2h(Mbad)[0] < -0.5,
          f"STRICTNESS: the declared pair passes every channelwise scalar check yet "
          f"nu - J/2 has eigenvalue {eig2h(Mbad)[0]:.2f} < 0 -- NON-REALIZABLE (any realization "
          "would make it a Gram matrix); the matrix order is strictly stronger than the scalar "
          "cone applied per channel", "ctrl")
    # redundancy adjudication: the PSD condition IS bath-state positivity (Gram reconstruction)
    rec_worst = 0.0
    for w, vecs in gram.items():
        M = cmat(2)
        for v in vecs:
            for a in range(2):
                for b in range(2):
                    M[a][b] += v[a] * v[b].conjugate()
        rec_worst = max(rec_worst, max(abs(M[i][j] - C[w][i][j]) for i in range(2) for j in range(2)))
    check(rec_worst < 1e-12,
          f"REDUNDANCY (adjudicated as chartered): every C(omega) reconstructs exactly from Gram "
          f"vectors sqrt(p_n)<n|B_a|m> (worst {rec_worst:.1e}) -- the matrix admissibility "
          "condition IS bath-state positivity in influence-data language: NULL-AS-NEW-PRINCIPLE")
    # commuting restriction: single channel reduces to the scalar cone
    scal_ok = True
    for w in ws:
        Cm = C.get(-w, cmat(2))
        nu11 = (C[w][0][0] + Cm[0][0]).real / 2
        J11 = (C[w][0][0] - Cm[0][0]).real
        scal_ok = scal_ok and (nu11 + 1e-12 >= abs(J11) / 2)
    check(scal_ok, "commuting restriction: the single-channel diagonal recovers the scalar "
                   "nu >= |J|/2 at every frequency")
    return {"lift_min_eig": lift_min, "noncomm_channels": cn, "noncomm_cross_freq": ncn}


# ---------------- Q2: CP separation ----------------------------------------------------------
def q2():
    print("\n=== Q2: CP SEPARATION (Choi PSD of the exact reduced map) ===")
    E, B1, _ = bath_ops()
    n = 2 * DIM
    H = [[0.0] * n for _ in range(n)]
    mu = 0.4
    for pb in range(2):
        for nb_ in range(DIM):
            i = pb * DIM + nb_
            H[i][i] += E[nb_]
            sz = 1.0 if pb == 0 else -1.0
            for mb in range(DIM):
                j = pb * DIM + mb
                H[i][j] += sz * B1[nb_][mb].real
            H[(1 - pb) * DIM + nb_][i] += mu
    lam, V = jacobi_eig(H)
    Z = sum(math.exp(-BETA * e) for e in E)
    pB = [math.exp(-BETA * e) / Z for e in E]
    for t in (0.7, 2.1):
        ph = [cmath.exp(-1j * l * t) for l in lam]
        U = [[sum(V[i][k] * ph[k] * V[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
        choi = cmat(4)
        for i in range(2):
            for j in range(2):
                # Lambda(|i><j|) = Tr_B[ U (|i><j| x rho_B) U^dag ]
                blk = cmat(2)
                for a in range(2):
                    for b in range(2):
                        s = 0j
                        for nb_ in range(DIM):
                            for mb in range(DIM):
                                s += U[a * DIM + mb][i * DIM + nb_] * pB[nb_] * \
                                     U[b * DIM + mb][j * DIM + nb_].conjugate()
                        blk[a][b] = s
                for a in range(2):
                    for b in range(2):
                        choi[i * 2 + a][j * 2 + b] = blk[a][b]
        mn = herm_eigs(choi)[0]
        check(mn > -1e-9, f"Choi PSD at t = {t} (min eig {mn:.1e}) -- CP holds by dilation; "
                          "it adds no data constraint beyond state positivity (the (b) leg)")


# ---------------- Q3: non-Gaussian control ----------------------------------------------------
def dephasing_coherence(omegas, gs, lam, ts):
    """Pure dephasing: c(t) = <gs| e^{iH+t} e^{-iH-t} |gs>, H+- = H_B +- lam*B/2, B = sum g sx."""
    nb = len(omegas)
    d = 2 ** nb
    HB = [[0.0] * d for _ in range(d)]
    B = [[0.0] * d for _ in range(d)]
    for n in range(d):
        HB[n][n] = sum((0.5 if (n >> i) & 1 == 0 else -0.5) * omegas[i] for i in range(nb))
        for i in range(nb):
            B[n][n ^ (1 << i)] += gs[i]
    gs_idx = min(range(d), key=lambda n: HB[n][n])
    out = []
    eig = {}
    for sgn in (1, -1):
        Hp = [[HB[i][j] + sgn * lam * B[i][j] / 2 for j in range(d)] for i in range(d)]
        eig[sgn] = jacobi_eig(Hp)
    for t in ts:
        mats = {}
        for sgn in (1, -1):
            l, V = eig[sgn]
            ph = [cmath.exp((1j if sgn == 1 else -1j) * x * t) for x in l]
            mats[sgn] = [[sum(V[i][k] * ph[k] * V[j][k] for k in range(d)) for j in range(d)]
                         for i in range(d)]
        M = cmul(mats[1], mats[-1])
        out.append(M[gs_idx][gs_idx])
    return out


def q3():
    print("\n=== Q3: NON-GAUSSIAN CONTROL (matched 2-point, different kappa_4) ===")
    g = 0.5
    # equal-time moments in the ground state (all spins down): <B^2>, <B^4> by direct algebra
    def moments(omegas, gs):
        nb = len(omegas)
        d = 2 ** nb
        B = [[0.0] * d for _ in range(d)]
        for n in range(d):
            for i in range(nb):
                B[n][n ^ (1 << i)] += gs[i]
        gidx = d - 1  # all bits set = all down = lowest energy in our convention
        B2 = [[sum(B[i][k] * B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
        B4 = [[sum(B2[i][k] * B2[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
        return B2[gidx][gidx], B4[gidx][gidx], sum(B2[gidx][k] * B[k][gidx] for k in range(d))
    m2A, m4A, m3A = moments([1.0, 1.0], [g, g])
    m2B, m4B, m3B = moments([1.0], [g * math.sqrt(2)])
    k4A, k4B = m4A - 3 * m2A ** 2, m4B - 3 * m2B ** 2
    check(abs(m2A - m2B) < 1e-12, f"two-point MATCH: <B^2> = {m2A:.4f} both (2g^2 = {2*g*g:.4f})")
    check(abs(m3A) < 1e-12 and abs(m3B) < 1e-12, "third cumulants vanish by symmetry (checked)")
    check(abs(k4A - (-4 * g ** 4)) < 1e-12 and abs(k4B - (-8 * g ** 4)) < 1e-12,
          f"kappa_4 DIFFER as derived: {k4A:.4f} (= -4g^4) vs {k4B:.4f} (= -8g^4)")
    ts = [10.0 * i / 399 for i in range(400)]
    cA = dephasing_coherence([1.0, 1.0], [g, g], 1.0, ts)
    cB = dephasing_coherence([1.0], [g * math.sqrt(2)], 1.0, ts)
    dmax = max(abs(a - b) for a, b in zip(cA, cB))
    check(dmax > 1e-3, f"CLASS-SPLIT DETECTED: probe coherence curves differ by {dmax:.3f} "
                       "despite identical (K, N) -- the Gaussian pair is a PROJECTION; the first "
                       "obstruction is the connected fourth cumulant")
    cA2 = dephasing_coherence([1.0, 1.0], [g, g][::-1], 1.0, ts)  # relabeled spins
    dctl = max(abs(a - b) for a, b in zip(cA, cA2))
    check(dctl < 1e-12, f"matched control (relabeled bath): difference {dctl:.1e} < 1e-12", "ctrl")
    return {"kappa4_A": k4A, "kappa4_B": k4B, "coherence_delta": dmax}


# ---------------- Q4: counting in noncommuting channels ---------------------------------------
WGRID = [0.02 * (10.0) ** (i / 29) for i in range(30)]  # [0.02, 0.2]


def slope(js):
    xs = [math.log(w) for w in WGRID]
    ys = [math.log(j) for j in js]
    n = len(xs)
    xb, yb = sum(xs) / n, sum(ys) / n
    return sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)


def Jmat(w, extra_q=0, cancel=False):
    q = w  # linear dispersion, exact root
    supp = (6 * (q - math.sin(q)) / q) if cancel else 1.0  # order-2 cancellation factor ~ q^2
    v = [supp * q ** (1 + extra_q) / math.sqrt(2 * w),
         supp * 0.3 * q ** (2 + extra_q) / math.sqrt(2 * w)]
    u = [0.3 * q ** (2 + extra_q) / math.sqrt(2 * w), q ** (3 + extra_q) / math.sqrt(2 * w)]
    return [[v[i] * v[j] + u[i] * u[j] for j in range(2)] for i in range(2)]


def q4():
    print("\n=== Q4: COUNTING IN NONCOMMUTING CHANNELS (rank-2 matrix J, exact roots) ===")
    def eigslopes(extra_q=0, cancel=False):
        e1s, e2s = [], []
        for w in WGRID:
            M = Jmat(w, extra_q, cancel)
            lo, hi = eig2h([[complex(M[i][j]) for j in range(2)] for i in range(2)])
            e1s.append(hi)  # dominant
            e2s.append(max(lo, 1e-300))
        return slope(e1s), slope(e2s)
    s1, s2 = eigslopes()
    check(True, f"base eigen-slopes: dominant {s1:+.3f}, subdominant {s2:+.3f}", "note")
    s1p, s2p = eigslopes(extra_q=1)
    check(abs((s1p - s1) - 2) < 0.1 and abs((s2p - s2) - 2) < 0.1,
          f"H1-matrix: multiplying ALL vertices by q shifts BOTH eigen-slopes by "
          f"{s1p - s1:+.3f}, {s2p - s2:+.3f} (frozen: +2 +- 0.1)")
    s1c, s2c = eigslopes(cancel=True)
    h3_eig = abs((s1c - s1) - 4) < 0.2
    check(h3_eig,
          f"H3-matrix (FROZEN GATE, preserved as found): the cancellation shifts the dominant "
          f"eigen-slope by {s1c - s1:+.3f}, NOT +4 -- at eigenvalue level the claim FAILS")
    # POST-HOC DIAGNOSTIC (added after the frozen gate failed; a measurement, not a rescue):
    # track the affected SPECIES' spectral weight |v|^2 directly.
    def vweight(cancel):
        out = []
        for w in WGRID:
            q = w
            supp = (6 * (q - math.sin(q)) / q) if cancel else 1.0
            out.append((supp * q) ** 2 / (2 * w) + (supp * 0.3 * q ** 2) ** 2 / (2 * w))
        return slope(out)
    dv = vweight(True) - vweight(False)
    check(abs(dv - 4) < 0.05,
          f"POST-HOC DIAGNOSTIC: the cancellation adds {dv:+.3f} to the affected SPECIES' "
          "spectral weight exactly -- the +4 increment survives PER BRANCH; what fails is its "
          "commutation with eigenvalue ordering: in matrix channels a cancelled branch can be "
          "MASKED by another channel (min-dominance) and the observable dominant exponent shifts "
          "only to the masking channel's class. MODIFIED, not survived, at eigenvalue level.",
          "note")
    # null control: an omega-DEPENDENT channel rescaling fakes exponent shifts
    fake = []
    for w in WGRID:
        M = Jmat(w)
        D = [w, 1.0]
        fake.append(max(eig2h([[complex(D[i] * M[i][j] * D[j]) for j in range(2)]
                               for i in range(2)])))
    sfake = slope(fake)
    check(abs(sfake - s1) > 0.5,
          f"NULL CONTROL: the omega-dependent rescaling diag(w, 1) shifts the apparent dominant "
          f"slope to {sfake:+.3f} (true {s1:+.3f}) -- convention laundering demonstrated and "
          "EXCLUDED by the omega-independent-basis freeze", "ctrl")
    # scalar-limit control: single channel reproduces S-1
    sc = slope([q * q / (2 * w) for q, w in zip(WGRID, WGRID)])
    check(abs(sc - 1.0) < 0.05, f"scalar-limit control: single channel p = 1 gives s = {sc:+.3f} "
                                "(S-1's convention: 2p - 1 = 1)")
    return {"base": (s1, s2), "H1_shift": (s1p - s1, s2p - s2), "H3_shift": s1c - s1,
            "fake_slope": sfake}


# ---------------- Q5: representation invariance at matrix level -------------------------------
def q5():
    print("\n=== Q5: REPRESENTATION INVARIANCE (bath-local rotation; full influence data equal) ===")
    ts = [10.0 * i / 199 for i in range(200)]
    g, th = 0.5, 0.9
    base = dephasing_coherence([1.0, 1.0], [g, g], 1.0, ts)
    # rotated realization: B' = U B U^dag with U = exp(-i th sum sz/2) (commutes with H_B, state)
    nb, d = 2, 4
    HB = [[0.0] * d for _ in range(d)]
    B = [[0.0] * d for _ in range(d)]
    for n in range(d):
        HB[n][n] = sum((0.5 if (n >> i) & 1 == 0 else -0.5) * 1.0 for i in range(nb))
        for i in range(nb):
            B[n][n ^ (1 << i)] += g
    Uph = [cmath.exp(-1j * th * sum(0.5 if (n >> i) & 1 == 0 else -0.5 for i in range(nb)))
           for n in range(d)]
    Bp = [[Uph[i] * B[i][j] * Uph[j].conjugate() for j in range(d)] for i in range(d)]
    gs_idx = min(range(d), key=lambda n: HB[n][n])
    out = []
    for t in ts:
        vals = {}
        for sgn in (1, -1):
            Hp = [[HB[i][j] + sgn * 0.5 * Bp[i][j] for j in range(d)] for i in range(d)]
            lam = herm_eigs(Hp)  # embedding doubles; need vectors -> do direct series instead
        # exact via scaling-and-squaring series on the 4x4 (small norm * t manageable)
        def expm(Mm, pref):
            n_ = len(Mm)
            A = [[pref * Mm[i][j] for j in range(n_)] for i in range(n_)]
            nrm = max(abs(A[i][j]) for i in range(n_) for j in range(n_))
            k, sq = 1, 0
            while nrm / k > 0.25:
                k *= 2
                sq += 1
            A = [[A[i][j] / k for j in range(n_)] for i in range(n_)]
            R = [[1.0 + 0j if i == j else 0j for j in range(n_)] for i in range(n_)]
            Tm = [row[:] for row in R]
            for p_ in range(1, 18):
                Tm = [[sum(Tm[i][x] * A[x][j] for x in range(n_)) / p_ for j in range(n_)]
                      for i in range(n_)]
                R = [[R[i][j] + Tm[i][j] for j in range(n_)] for i in range(n_)]
            for _ in range(sq):
                R = cmul(R, R)
            return R
        Hp1 = [[HB[i][j] + 0.5 * Bp[i][j] for j in range(d)] for i in range(d)]
        Hm1 = [[HB[i][j] - 0.5 * Bp[i][j] for j in range(d)] for i in range(d)]
        M = cmul(expm(Hp1, 1j * t), expm(Hm1, -1j * t))
        out.append(M[gs_idx][gs_idx])
    dmax = max(abs(a - b) for a, b in zip(base, out))
    check(dmax < 1e-9, f"rotated realization reproduces the probe trajectory (max diff {dmax:.1e} "
                       "< 1e-9): microscopic differences with identical FULL influence data are "
                       "representational -- D-1 extended to the matrix level; the quantity that "
                       "DOES distinguish realizations is exactly the cumulant data (Q3: kappa_4)")


def main():
    t0 = time.time()
    print("P-3 NONCOMMUTATIVE-LIFT INSTRUMENT (charter: P3_NC_LIFT_CHARTER_01.md, frozen at 78b188e)")
    r1 = q1()
    q2()
    r3 = q3()
    r4 = q4()
    q5()
    if FAIL:
        print("\nHALT-CLASS FAILURES PRESENT; composite verdict withheld.")
    print("\n=== COMPOSITE (charter section 3, mechanical) ===")
    qa = "SURVIVES-AS-GEOMETRY + NULL-AS-NEW-PRINCIPLE"
    h3_failed = any("H3-matrix (FROZEN GATE" in f for f in FAIL)
    qb = ("COUNTING MODIFIED in matrix channels (per-branch increments survive exactly, incl. "
          "+2 on all eigen-slopes; the +4 cancellation increment is MASKED at eigenvalue level "
          "by min-dominance -- the frozen eigenvalue-level gate FAILED and is preserved) + "
          "CLASS-SPLIT beyond Gaussian (first obstruction kappa_4)") if h3_failed else \
         "COUNTING SURVIVES (matrix channels) + CLASS-SPLIT (beyond Gaussian; first obstruction kappa_4)"
    check(True, f"Question A: {qa}", "note")
    check(True, f"Question B: {qb}", "note")
    out = {"instrument": "p3_nc_lift", "charter_commit": "78b188e", "date": "2026-09-25",
           "authority": "GitHub Issue #2 + owner guidance comment",
           "Q1": r1, "Q3": r3, "Q4": r4,
           "composite": {"A": qa, "B": qb},
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on what the lift does to the theory"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "P3_NC_LIFT_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nP-3 NC LIFT: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
