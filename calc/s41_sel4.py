#!/usr/bin/env python3
"""s41_sel4: can Sel-4 be selected without defining gravity as Sel-4?

CHARTER: S41_SEL4_CHARTER_01.md (pre-registration frozen at commit e83b6f0 BEFORE this
instrument ran; authority: owner ruling recorded in EQ1_S41_OWNER_RULING_01.md). Sel-4 is
split into temporal (4t), universality (4U) and spatial (4x, carried from EQ-1). Every
"derived" component is conditional on the inherited constraint C_cons (the probe's constant
limit couples to a conserved local charge). Discriminators are unit-invariant but dynamically
sensitive: normalized spectrum shape, and a cross-sector correlation with the best common
time rescaling optimized away.

Legs: L-T single-sector commutants (MFIM generic / TFIM integrable / XX free) | L-D extra
conserved charge changes the intrinsic spectral shape | L-N non-conserved coupling: what
excludes it | L-U universality: ladder commutants + clock-comparison dynamics.

Pure stdlib. Run: python3 calc/s41_sel4.py
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from p3_nc_lift import herm_eigs

FAIL = []
CHECKS = []
HALT = []
HX, HZ = 0.9045, 0.8090
HPROBE = 0.05


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


# ---------------- exact Pauli-string algebra (I=0, X=1, Y=2, Z=3) ------------------------------
MUL = [[(1, 0), (1, 1), (1, 2), (1, 3)],
       [(1, 1), (1, 0), (1j, 3), (-1j, 2)],
       [(1, 2), (-1j, 3), (1, 0), (1j, 1)],
       [(1, 3), (1j, 2), (-1j, 1), (1, 0)]]


def smul(s, t):
    ph = 1
    out = []
    for a, b in zip(s, t):
        p, c = MUL[a][b]
        ph *= p
        out.append(c)
    return ph, tuple(out)


def anticommute(s, t):
    return sum(1 for a, b in zip(s, t) if a and b and a != b) % 2 == 1


def op_add(A, B, cb=1.0):
    out = dict(A)
    for s, c in B.items():
        out[s] = out.get(s, 0) + cb * c
    return {s: c for s, c in out.items() if abs(c) > 1e-15}


def comm(A, B):
    out = {}
    for sa, ca in A.items():
        for sb, cb in B.items():
            if anticommute(sa, sb):
                ph, r = smul(sa, sb)
                out[r] = out.get(r, 0) + 2 * ph * ca * cb
    return {s: c for s, c in out.items() if abs(c) > 1e-14}


def placed(N, assign):
    s = [0] * N
    for site, p in assign:
        s[site] = p
    return tuple(s)


def ring_sum(N, pattern, sites=None):
    """Translation-invariant sum of a Pauli pattern along a ring of the given sites."""
    sites = list(range(N)) if sites is None else sites
    L = len(sites)
    op = {}
    for i in range(L):
        s = placed(N, [(sites[(i + k) % L], p) for k, p in enumerate(pattern) if p])
        op[s] = op.get(s, 0) + 1.0
    return op


def patterns(rmax):
    out = [(p,) for p in (1, 2, 3)]
    if rmax >= 2:
        out += [(a, b) for a in (1, 2, 3) for b in (1, 2, 3)]
    if rmax >= 3:
        out += [(a, m, b) for a in (1, 2, 3) for m in (0, 1, 2, 3) for b in (1, 2, 3)]
    return out


def chain_H(N, J, hx, hz, kind="ising"):
    if kind == "xx":
        return op_add(ring_sum(N, (1, 1)), ring_sum(N, (2, 2)))
    H = {s: J * c for s, c in ring_sum(N, (3, 3)).items()}
    H = op_add(H, ring_sum(N, (1,)), hx)
    if hz:
        H = op_add(H, ring_sum(N, (3,)), hz)
    return H


def commutant(basis, H):
    cols = []
    keys = {}
    for O in basis:
        C = comm(O, H)
        v = {}
        for s, c in C.items():
            v[s] = (c / 1j).real  # Hermitian strings -> purely imaginary commutator
            if s not in keys:
                keys[s] = len(keys)
        cols.append(v)
    n = len(basis)
    G = [[sum(cols[i].get(s, 0.0) * cols[j].get(s, 0.0) for s in cols[i])
          for j in range(n)] for i in range(n)]
    lam, V = jacobi_eig(G)
    mx = max(abs(x) for x in lam) or 1.0
    null = [[V[i][k] for i in range(n)] for k in range(n) if abs(lam[k]) < 1e-10 * mx]
    return null


def combo(basis, coef):
    out = {}
    for O, c in zip(basis, coef):
        if abs(c) > 1e-14:
            out = op_add(out, O, c)
    return out


# ---------------- dense matrices (for ED) -------------------------------------------------------
def dense(op, N):
    d = 2 ** N
    M = [[0j] * d for _ in range(d)]
    for s, c in op.items():
        for b in range(d):
            nb, ph = b, 1 + 0j
            for j, p in enumerate(s):
                if not p:
                    continue
                bit = (b >> j) & 1
                if p == 1:
                    nb ^= (1 << j)
                elif p == 2:
                    nb ^= (1 << j)
                    ph *= (1j if bit == 0 else -1j)
                else:
                    ph *= (1 if bit == 0 else -1)
            M[nb][b] += c * ph
    return M


def is_real(M):
    return max(abs(x.imag) for row in M for x in row) < 1e-14


def spectrum(M):
    if is_real(M):
        lam, _ = jacobi_eig([[x.real for x in row] for row in M])
        return sorted(lam)
    return sorted(herm_eigs(M))[::2]


def shape(E):
    e0, e1 = E[0], E[-1]
    return [(e - e0) / (e1 - e0) for e in E]


def edges(op):
    out = set()
    for s in op:
        sup = [i for i, p in enumerate(s) if p]
        for a in range(len(sup)):
            for b in range(a + 1, len(sup)):
                out.add((sup[a], sup[b]))
    return out


def mat_comm_norm(A, B):
    d = len(A)
    AB = [[sum(A[i][k] * B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    BA = [[sum(B[i][k] * A[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    return max(abs(AB[i][j] - BA[i][j]) for i in range(d) for j in range(d))


# ---------------- L-T: single-sector commutants ------------------------------------------------
def leg_T():
    print("\n=== L-T: Sel-4t ON A SINGLE SECTOR (does locality + C_cons force O ~ H?) ===")
    N = 8
    basis = [ring_sum(N, p) for p in patterns(3)]
    res = {}
    for name, H, pred in (("MFIM (generic)", chain_H(N, 1.0, HX, HZ), "==1"),
                          ("TFIM (integrable)", chain_H(N, 1.0, HX, 0.0), ">=2"),
                          ("XX (free)", chain_H(N, 1.0, 0, 0, "xx"), ">=2")):
        if name.startswith("MFIM"):
            halt_check(len(comm(H, H)) == 0, "L-T control: [H, H] = 0 exactly in the "
                                             "symbolic Pauli algebra (halt-grade)")
        null = commutant(basis, H)
        dim = len(null)
        ok = dim == 1 if pred == "==1" else dim >= 2
        res[name] = dim
        check(ok, f"L-T GATE {name}: commutant of H in the {len(basis)}-operator range-<=3 "
                  f"local basis (L = {N}) has dim {dim} (predicted {pred})")
    check(True, "L-T consequence (frozen): for the generic sector, locality + C_cons leave "
                "only O ~ H -- the constant clock-probe coupling IS a time-unit change: "
                "temporal Sel-4 DERIVED-IN-CLASS, conditional on C_cons. Integrable and free "
                "sectors carry extra local conserved charges: temporal Sel-4 NOT forced "
                "there (CONSTRAINED-NONUNIQUE). The phonon-type retained sector is free", "note")
    return res


# ---------------- L-D: an extra conserved charge is a genuine alternative ----------------------
def leg_D():
    print("\n=== L-D: DISCRIMINATOR FOR ALTERNATIVE (i) -- EXTRA CONSERVED CHARGE (TFIM, L = 6) "
          "===")
    N = 6
    pats = patterns(3)
    basis = [ring_sum(N, p) for p in pats]
    H = chain_H(N, 1.0, HX, 0.0)
    hvec = [0.0] * len(pats)
    hvec[pats.index((3, 3))] = 1.0
    hvec[pats.index((1,))] = HX
    hn = math.sqrt(sum(x * x for x in hvec))
    hu = [x / hn for x in hvec]
    null = commutant(basis, H)

    def resid(v):
        c = sum(a * b for a, b in zip(v, hu))
        r = [a - c * b for a, b in zip(v, hu)]
        return math.sqrt(sum(x * x for x in r)) / math.sqrt(sum(x * x for x in v)), r

    best = max(null, key=lambda v: resid(v)[0])
    rel, o2 = resid(best)
    check(rel > 0.1, f"L-D GATE: extracted extra conserved charge O2 has relative residual "
                     f"{rel:.3f} > 0.1 against H (commutant dim at L = 6: {len(null)})")
    O2 = combo(basis, o2)
    Hm, O2m = dense(H, N), dense(O2, N)
    cn = mat_comm_norm(O2m, Hm)
    halt_check(cn < 1e-10, f"L-D control: dense ||[O2, H]|| = {cn:.1e} < 1e-10 (ED agrees "
                           f"with the symbolic commutant; halt-grade)")
    nO = max(abs(x) for row in O2m for x in row)
    nH = max(abs(x) for row in Hm for x in row)
    O2s = [[x * nH / nO for x in row] for row in O2m]  # match operator scale to H
    E0 = spectrum(Hm)
    Eu = spectrum([[Hm[i][j] * (1 + HPROBE) for j in range(len(Hm))] for i in range(len(Hm))])
    Ea = spectrum([[Hm[i][j] + HPROBE * O2s[i][j] for j in range(len(Hm))]
                   for i in range(len(Hm))])
    s0 = shape(E0)
    du = max(abs(a - b) for a, b in zip(shape(Eu), s0))
    da = max(abs(a - b) for a, b in zip(shape(Ea), s0))
    check(du < 1e-10, f"L-D GATE: unit-change probe O = H leaves the normalized spectrum "
                      f"shape unchanged, max|ds| = {du:.1e} < 1e-10")
    check(da > 1e-4, f"L-D GATE: extra-charge probe O = O2 changes the normalized spectrum "
                     f"shape, max|ds| = {da:.3e} > 1e-4 -- a genuinely distinct, conserved, "
                     f"local alternative that is intrinsically visible")
    return {"O2_residual": rel, "commutant_dim_L6": len(null), "dense_comm": cn,
            "shape_unit": du, "shape_O2": da}


# ---------------- L-N: the non-conserved alternative ------------------------------------------
def gram_psd(Hm_real, Om_real, ts=(0.0, 1.0, 2.5)):
    lam, V = jacobi_eig(Hm_real)
    d = len(lam)
    g = min(range(d), key=lambda k: lam[k])
    Ot = [[sum(V[i][a] * Om_real[i][j] * V[j][b] for i in range(d) for j in range(d)
               if Om_real[i][j] != 0.0) for b in range(d)] for a in (g,)]
    amps = [Ot[0][m] ** 2 for m in range(d)]
    G = [[sum(amps[m] * cmath.exp(-1j * (lam[m] - lam[g]) * (ta - tb)) for m in range(d))
          for tb in ts] for ta in ts]
    scale = max(abs(G[i][i]) for i in range(3))
    return min(herm_eigs(G)) / scale


def leg_N():
    print("\n=== L-N: ALTERNATIVE (iii) -- NON-CONSERVED COUPLING O = sum X_i (MFIM, L = 6) ===")
    N = 6
    H = chain_H(N, 1.0, HX, HZ)
    O = ring_sum(N, (1,))
    C = comm(O, H)
    cn = math.sqrt(sum(abs(c) ** 2 for c in C.values()))
    check(cn > 0, f"L-N GATE: ||[O, H]|| (Pauli norm) = {cn:.3f} > 0 -- O is not conserved; "
                  f"C_cons excludes it")
    Hm = dense(H, N)
    Om = dense(O, N)
    Hr = [[x.real for x in row] for row in Hm]
    Or = [[x.real for x in row] for row in Om]
    E0 = spectrum(Hm)
    Ea = spectrum([[Hm[i][j] + HPROBE * Om[i][j] for j in range(len(Hm))]
                   for i in range(len(Hm))])
    da = max(abs(a - b) for a, b in zip(shape(Ea), shape(E0)))
    check(da > 1e-4, f"L-N GATE: the constant probe changes the normalized spectrum shape, "
                     f"max|ds| = {da:.3e} > 1e-4 (intrinsically visible)")
    mn = gram_psd(Hr, Or)
    check(mn >= -1e-12, f"L-N GATE: ground-state two-time Gram of O PSD, min eig / scale = "
                        f"{mn:.2e} -- 𝔠_full admits it")
    same = edges(op_add(H, O, HPROBE)) == edges(H)
    check(same, "L-N GATE: interaction graph of H + hO equals that of H -- G-2's hop "
                "geometry cannot see this alternative")
    check(True, "L-N consequence (frozen): the non-conserved alternative is admitted by "
                "𝔠_full and invisible to G-2 geometry; it is excluded by C_cons and by "
                "nothing else earned. Without C_cons, Sel-4t cannot be selected", "note")
    return {"comm_norm": cn, "shape_change": da, "gram_min": mn, "graph_same": same}


# ---------------- L-U: universality ---------------------------------------------------------------
def ladder_H(L, g, with_legs=True):
    N = 2 * L
    A = list(range(L))
    B = list(range(L, 2 * L))
    HA = {s: 1.0 * c for s, c in ring_sum(N, (3, 3), A).items()}
    HA = op_add(HA, ring_sum(N, (1,), A), HX)
    HA = op_add(HA, ring_sum(N, (3,), A), HZ)
    HB = {s: 1.3 * c for s, c in ring_sum(N, (3, 3), B).items()}
    HB = op_add(HB, ring_sum(N, (1,), B), 0.7)
    HB = op_add(HB, ring_sum(N, (3,), B), 0.5)
    V = {}
    for i in range(L):
        s = placed(N, [(A[i], 3), (B[i], 3)])
        V[s] = V.get(s, 0) + g
    return HA, HB, V


def ladder_basis(L):
    N = 2 * L
    A = list(range(L))
    B = list(range(L, 2 * L))
    basis = [ring_sum(N, p, A) for p in patterns(2)]
    basis += [ring_sum(N, p, B) for p in patterns(2)]
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            op = {}
            for i in range(L):
                s = placed(N, [(A[i], a), (B[i], b)])
                op[s] = op.get(s, 0) + 1.0
            basis.append(op)
    return basis


def evo_setup(Hr, psi_index, obs_diag):
    lam, V = jacobi_eig(Hr)
    d = len(lam)
    c = [V[psi_index][m] for m in range(d)]
    Ot = [[sum(V[k][m] * obs_diag[k] * V[k][n] for k in range(d)) for n in range(d)]
          for m in range(d)]
    terms = [(c[m] * c[n] * Ot[m][n], lam[m] - lam[n]) for m in range(d) for n in range(d)
             if abs(c[m] * c[n] * Ot[m][n]) > 1e-15]
    return terms


def C_of(terms, t):
    return sum(w * math.cos(f * t) for w, f in terms)


def discriminator(base_terms, probe_terms, ts):
    target = [C_of(probe_terms, t) for t in ts]

    def D(c):
        return max(abs(target[i] - C_of(base_terms, c * ts[i])) for i in range(len(ts)))

    best_c, best = 1.0, float("inf")
    for k in range(201):
        c = 0.9 + 0.001 * k
        v = D(c)
        if v < best:
            best, best_c = v, c
    lo, hi = best_c - 0.001, best_c + 0.001
    gr = (math.sqrt(5) - 1) / 2
    x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
    f1, f2 = D(x1), D(x2)
    while hi - lo > 1e-12:
        if f1 < f2:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - gr * (hi - lo)
            f1 = D(x1)
        else:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + gr * (hi - lo)
            f2 = D(x2)
    return min(best, f1, f2), 0.5 * (lo + hi)


def leg_U():
    print("\n=== L-U: Sel-4U UNIVERSALITY (ladder commutants + clock-comparison dynamics) ===")
    out = {}
    L = 6
    basis = ladder_basis(L)
    for g, pred in ((0.0, 2), (0.3, 1)):
        HA, HB, V = ladder_H(L, g)
        H = op_add(op_add(HA, HB), V)
        dim = len(commutant(basis, H))
        out[f"commutant_g{g}"] = dim
        check(dim == pred, f"L-U GATE commutant (legs L = {L}, {len(basis)}-operator basis), "
                           f"rung g = {g}: dim {dim} (predicted {pred})")
    Ls = 3
    N = 2 * Ls
    ts = [10.0 * i / 40 for i in range(41)]
    psi = (1 << 3) | (1 << 4) | (1 << 5)
    obs = [(1 if (b & 1) == 0 else -1) * (1 if ((b >> 3) & 1) == 0 else -1)
           for b in range(2 ** N)]
    for g in (0.3, 0.0):
        HA, HB, V = ladder_H(Ls, g)
        H = op_add(op_add(HA, HB), V)
        Hr = [[x.real for x in row] for row in dense(H, N)]
        HAr = [[x.real for x in row] for row in dense(HA, N)]
        base = evo_setup(Hr, psi, obs)
        uni = evo_setup([[x * (1 + HPROBE) for x in row] for row in Hr], psi, obs)
        non = evo_setup([[Hr[i][j] + HPROBE * HAr[i][j] for j in range(2 ** N)]
                         for i in range(2 ** N)], psi, obs)
        du, cu = discriminator(base, uni, ts)
        dn, cnb = discriminator(base, non, ts)
        tag = "coupled" if g else "decoupled"
        halt_check(du < 1e-10, f"L-U GATE {tag} (g = {g}): universal probe Delta = {du:.1e} "
                               f"< 1e-10 at best common rescale c = {cu:.6f} (exact time "
                               f"rescaling; halt-grade)")
        check(dn > 1e-3, f"L-U GATE {tag} (g = {g}): non-universal probe Delta = {dn:.3e} "
                         f"> 1e-3 even at the best common rescale c = {cnb:.6f} -- relative "
                         f"clock rates are visible in the full accessible dynamics")
        out[f"Delta_universal_{tag}"] = du
        out[f"Delta_nonuniversal_{tag}"] = dn
        if g:
            same = edges(op_add(H, HA, HPROBE)) == edges(H)
            check(same, "L-U GATE: non-universal probe preserves the interaction graph -- "
                        "G-2 hop geometry blind to it")
            mn = gram_psd(Hr, HAr)
            check(mn >= -1e-12, f"L-U GATE: ground-state two-time Gram of the non-universal "
                                f"coupling O = H_A PSD, min eig / scale = {mn:.2e} -- 𝔠_full "
                                f"admits it")
            out["graph_same"], out["gram_min"] = same, mn
    check(True, "L-U consequence (frozen): with ANY rung coupling, C_cons leaves only "
                "H_total -- clock universality DERIVED-IN-CLASS for interacting sectors. "
                "Decoupled sectors: each clock is separately conserved, so conservation "
                "allows epsilon_A != epsilon_B -- yet the relative rate is observable by "
                "joint access. Universality is IRREDUCIBLE for non-interacting sectors", "note")
    return out


# ---------------- adjudication ------------------------------------------------------------------
def adjudicate(rT, rD, rN, rU):
    t_generic = rT["MFIM (generic)"] == 1
    t_integ = (rT["TFIM (integrable)"] >= 2 and rT["XX (free)"] >= 2
               and rD["shape_O2"] > 1e-4)
    u_inter = rU["commutant_g0.3"] == 1 and rU["Delta_nonuniversal_coupled"] > 1e-3
    u_free = rU["commutant_g0.0"] == 2 and rU["Delta_nonuniversal_decoupled"] > 1e-3
    nulls = rN["gram_min"] >= -1e-12 and rN["graph_same"] and rU["graph_same"] \
        and rU["gram_min"] >= -1e-12
    parts = {
        "Sel-4t": ("CLASS-SPLIT: DERIVED-IN-CLASS (generic, | C_cons) / "
                   "CONSTRAINED-NONUNIQUE (integrable, free)") if (t_generic and t_integ)
        else ("DERIVED-IN-CLASS (| C_cons)" if t_generic else "NOT DERIVED"),
        "Sel-4U": ("CLASS-SPLIT: DERIVED-IN-CLASS (interacting, | C_cons) / "
                   "IRREDUCIBLE (non-interacting)") if (u_inter and u_free)
        else ("DERIVED-IN-CLASS (| C_cons)" if u_inter else "NOT DERIVED"),
        "Sel-4x": "IRREDUCIBLE (carried from EQ-1, not re-tested)",
        "𝔠_full & G-2 geometry": "NULL as selectors" if nulls else "not NULL",
    }
    derived_all = False
    return {"parts": parts, "overall": "CLASS-SPLIT per part; Sel-4 as a whole NOT derived",
            "derived_all": derived_all, "conditional_on": "C_cons"}


def main():
    t0 = time.time()
    print("S4-1: CAN Sel-4 BE SELECTED WITHOUT DEFINING GRAVITY AS Sel-4? (charter frozen "
          "at e83b6f0)")
    rT = leg_T()
    rD = leg_D()
    rN = leg_N()
    rU = leg_U()
    adj = adjudicate(rT, rD, rN, rU)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj["parts"].items():
        check(True, f"{k}: {v}", "note")
    check(True, f"OVERALL: {adj['overall']}. Every derived part is conditional on C_cons "
                f"(zero-momentum conservation inherited from CP-1/EQ-1) -- the owner rules "
                f"on that inheritance. Class-4 stays OPEN", "note")
    out = {"instrument": "s41_sel4", "charter_commit": "e83b6f0", "date": "2026-09-25",
           "LT": rT, "LD": rD, "LN": rN, "LU": rU, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "S41_SEL4_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nS4-1 Sel-4 ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}; "
          f"halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
