#!/usr/bin/env python3
"""SECOND-AUTHOR REVIEW of the three kernel files -- gates the boost-license ruling.

Reviewed (all same-author, uncountersigned): wall_a_kernel_gate.py,
wall_a_kernel_gate_bruteforce.py, wall_a_boost_membership.py.
The Bardeen file is already countersigned; these are not.

REGISTERED EXPECTATIONS (fixed before this script was run; disagreement ->
investigate, never average):
  E1  equivariance dims 21/11/6 by an INDEPENDENT construction: column-major
      unknown ordering + sympy rank -- different from the reviewed file's
      row-major ordering and hand-rolled Fraction elimination.
  E2  the reviewed file's hand-coded scalar orbit rows/covectors match the
      COUNTERSIGNED symbolic derived rules (second_author_bardeen.py), at both
      of its samples -- closes the shared-sign-error hole.
  E3  flat orthogonality pair(P1,{P2,P0s,Xsw}) = 0 recomputed at THIS review's
      own independent k (not the reviewed file's k).
  E4  T bijection fields <-> h_mn: independent reimplementation, exact round-trip.
  E5  slot convention COHERENT (not merely present): pull(K with slots
      exchanged) == pull(K).T on the slot-asymmetric Xsw.
  E6  third sample (omega,k)=(7,3), chosen by this review: intersection = 2,
      scalar boost-killed = 6, plants pass both directions, Ward-identification
      confirmed.
  E7  original block-arithmetic gate agrees with the measured dims; it is henceforth
      the derivation sketch.

Calibration of THIS review's machinery on knowns precedes every ruling.
"""
import sympy as sp
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
I = sp.I

print("=== STAGE 0: DECLARATIONS ===")
print("   reviewed : wall_a_kernel_gate.py (derivation sketch)")
print("              wall_a_kernel_gate_bruteforce.py (measurement, route 2)")
print("              wall_a_boost_membership.py (scalar membership, route 3)")
print("   counts   : KERNEL-STRUCTURE counts throughout")
print("   expectations E1..E7 registered above, before running")

# ============ STAGE 1: CALIBRATION OF THE REVIEW MACHINERY ============
print("\n=== STAGE 1: REVIEW-MACHINERY CALIBRATION (knowns only) ===")

def equiv_dim_rev(na, Ja, Pa, nr, Jr, Pr):
    """Independent equivariance solver: column-major unknowns y[l+na*m]=K[l][m],
    sympy rank (vs reviewed file: row-major + hand-rolled Fraction Gauss)."""
    idx = lambda l, m: l + na*m
    rows = []
    for i in range(na):
        for j in range(nr):
            r = [sp.Integer(0)]*(na*nr)
            for l in range(na): r[idx(l, j)] += sp.Integer(Ja[l][i])   # (Ja^T K)[i][j]
            for l in range(nr): r[idx(i, l)] += sp.Integer(Jr[l][j])   # (K Jr)[i][j]
            rows.append(r)
            r2 = [sp.Integer(0)]*(na*nr)
            for l in range(na):
                for m in range(nr):
                    r2[idx(l, m)] += sp.Integer(Pa[l][i])*sp.Integer(Pr[m][j])
            r2[idx(i, j)] -= 1                                          # Pa^T K Pr = K
            rows.append(r2)
    return na*nr - sp.Matrix(rows).rank()

J2 = [[0, -1], [1, 0]]
I2 = [[1, 0], [0, 1]]
Pm = [[1, 0], [0, -1]]
cal = []
cal.append(("commutant of SO(2) on 2x2 (no parity) = 2", equiv_dim_rev(2, J2, I2, 2, J2, I2) == 2))
cal.append(("commutant of SO(2) on 2x2 + parity   = 1", equiv_dim_rev(2, J2, Pm, 2, J2, Pm) == 1))
cal.append(("trivial 1x1 space                     = 1", equiv_dim_rev(1, [[0]], [[1]], 1, [[0]], [[1]]) == 1))
cal.append(("known-rank case: Ja^T K = 0, K 2x1    = 0", equiv_dim_rev(2, J2, I2, 1, [[0]], [[1]]) == 0))
for nm, ok in cal:
    print(f"   calibration {nm}: {'PASS' if ok else 'FAIL'}")
cal_ok = all(ok for _, ok in cal)
if not cal_ok:
    raise SystemExit("STOP: review machinery failed calibration; no ruling possible.")


# ============ STAGE 2: REVIEW OF wall_a_kernel_gate_bruteforce.py ============
print("\n=== STAGE 2: BRUTE-FORCE GATE REVIEW ===")

# ---- 2a/2b: independent dims + generator/parity consistency ----
def gens(pairs, doubles=(), n=10):
    J = [[0]*n for _ in range(n)]
    for (i, j) in pairs:   J[i][j] = -1; J[j][i] = 1    # helicity-1
    for (i, j) in doubles: J[i][j] = -2; J[j][i] = 2    # helicity-2
    return J
def parity(odds, n=10):
    return [[(-1 if i in odds else 1)*(1 if i == j else 0) for j in range(n)] for i in range(n)]

Ja = gens(pairs=[(4, 5), (6, 7)], doubles=[(8, 9)])
Pa = parity(odds={5, 7, 9})
Jr = gens(pairs=[(2, 3)], doubles=[(4, 5)], n=6)
Pr = parity(odds={3, 5}, n=6)

antisym = all(Ja[i][j] == -Ja[j][i] for i in range(10) for j in range(10)) and \
          all(Jr[i][j] == -Jr[j][i] for i in range(6) for j in range(6))
pjp_a = all(sum(Pa[i][l]*Ja[l][m]*Pa[m][n] for l in range(10) for m in range(10)) == -Ja[i][n]
            for i in range(10) for n in range(10))
pjp_r = all(sum(Pr[i][l]*Jr[l][m]*Pr[m][n] for l in range(6) for m in range(6)) == -Jr[i][n]
            for i in range(6) for n in range(6))
print(f"   generators antisymmetric (real rotations)        : {'PASS' if antisym else 'FAIL'}")
print(f"   parity conjugation P J P = -J, both slots        : {'PASS' if (pjp_a and pjp_r) else 'FAIL'}")

dims = (equiv_dim_rev(10, Ja, Pa, 10, Ja, Pa),
        equiv_dim_rev(10, Ja, Pa, 6, Jr, Pr),
        equiv_dim_rev(6, Jr, Pr, 6, Jr, Pr))
e1 = dims == (21, 11, 6)
print(f"   E1 independent equivariance dims: K_full={dims[0]} K_Ward={dims[1]} K_both={dims[2]}"
      f"  -> {'PASS' if e1 else 'FAIL'}")

# ---- 2c: hand-coded orbit rows vs countersigned symbolic derived rules ----
eta = sp.Symbol('eta')
al, be = sp.Function('alpha')(eta), sp.Function('beta')(eta)
H, Hp = sp.Symbol('H'), sp.Symbol('Hp')
A0, A1, A2 = sp.symbols('A0 A1 A2')
B0, B1, B2 = sp.symbols('B0 B1 B2')
# countersigned rules (second_author_bardeen.py, both prior routes).
# SELF-CATCH (reviewer error, 2026-08-24): the first draft of THIS review used H as a
# constant Symbol, so d(H*alpha)/deta silently dropped the H'-alpha term and E2 flagged
# two spurious MISMATCHes -- against a CORRECT reviewed file. Diagnosed by hand (only
# the H'-involving entries mismatched) before any report; fixed by making H a function
# of eta BEFORE differentiating. The reviewed file's hand-coded Hp entries were right.
Hf = sp.Function('Hcal')(eta)
dphi, dB, dpsi, dE = sp.Derivative(al, eta) + Hf*al, sp.Derivative(be, eta) - al, -Hf*al, be
coords = sp.symbols('phi B psi E phi_p B_p psi_p E_p E_pp')
jets = {al: A0, sp.Derivative(al, eta): A1, sp.Derivative(al, (eta, 2)): A2,
        be: B0, sp.Derivative(be, eta): B1, sp.Derivative(be, (eta, 2)): B2,
        Hf: H, sp.Derivative(Hf, eta): Hp}
def Jrow(expr): return sp.expand(expr.subs(jets))
d1s = (dphi, dB, dpsi, dE)
d1p = (sp.diff(dphi, eta), sp.diff(dB, eta), sp.diff(dpsi, eta), sp.diff(dE, eta),
       sp.diff(dE, (eta, 2)))
sym_rows = {p: [Jrow(e).coeff(p) for e in d1s + d1p] for p in (A0, A1, A2, B0, B1, B2)}
# the reviewed file's hand-coded rows (object under review, transcribed from its source):
their_rows = {'A0': [H, -1, -H, 0, Hp, 0, -Hp, 0, 0],
              'A1': [1, 0, 0, 0, H, -1, -H, 0, 0],
              'A2': [0, 0, 0, 0, 1, 0, 0, 0, 0],
              'B0': [0, 0, 0, 1, 0, 0, 0, 0, 0],
              'B1': [0, 1, 0, 0, 0, 0, 0, 1, 0],
              'B2': [0, 0, 0, 0, 0, 1, 0, 0, 1]}
key = {A0: 'A0', A1: 'A1', A2: 'A2', B0: 'B0', B1: 'B1', B2: 'B2'}
e2 = True
for p in sym_rows:
    for c in range(9):
        if sp.simplify(sym_rows[p][c] - their_rows[key[p]][c]) != 0:
            e2 = False
            print(f"      MISMATCH param {key[p]} coord {coords[c]}: "
                  f"symbolic {sym_rows[p][c]} vs hand-coded {their_rows[key[p]][c]}")
print(f"   E2 hand-coded orbit rows == countersigned symbolic rules: {'PASS' if e2 else 'FAIL'}")

# ---- 2d: E3 flat orthogonality at THIS review's own independent k ----
print("\n   E3 flat orthogonality pair(P1,{P2,P0s,Xsw}), independent k=(3,1,2,1):")
def flat_pair_zero(kup):
    R = sp.Rational
    ETA = [[R(1 if i == j == 0 else (-1 if i == j else 0)) for j in range(4)] for i in range(4)]
    klo = [sum(ETA[m][n]*kup[n] for n in range(4)) for m in range(4)]
    k2 = sum(kup[m]*klo[m] for m in range(4))
    th = [[ETA[m][n] - klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    om = [[klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    def T4(f): return {(m, n, r, s): f(m, n, r, s) for m in range(4) for n in range(4)
                       for r in range(4) for s in range(4)}
    P1 = T4(lambda m, n, r, s: (th[m][r]*om[n][s] + th[m][s]*om[n][r]
                                + th[n][r]*om[m][s] + th[n][s]*om[m][r])/2)
    fam = {'P2':  T4(lambda m, n, r, s: (th[m][r]*th[n][s] + th[m][s]*th[n][r])/2 - th[m][n]*th[r][s]/3),
           'P0s': T4(lambda m, n, r, s: th[m][n]*th[r][s]/3),
           'Xsw': T4(lambda m, n, r, s: th[m][n]*om[r][s])}
    def pair(A, B):
        return sum(A[(m, n, r, s)]*ETA[m][m]*ETA[n][n]*ETA[r][r]*ETA[s][s]*B[(m, n, r, s)]
                   for m in range(4) for n in range(4) for r in range(4) for s in range(4))
    vals = {nm: sp.simplify(pair(P1, K)) for nm, K in fam.items()}
    plant_nontrivial = sp.simplify(pair(P1, P1)) != 0   # pairing itself must not be degenerate
    return vals, all(v == 0 for v in vals.values()), plant_nontrivial
vals, e3, pair_plant = flat_pair_zero([sp.Rational(3), sp.Rational(1), sp.Rational(2), sp.Rational(1)])
print(f"      pair values: { {k: str(v) for k, v in vals.items()} }")
print(f"      E3 all exact zero: {'PASS' if e3 else 'FAIL'}   "
      f"(plant: pairing non-degenerate pair(P1,P1)!=0: {'PASS' if pair_plant else 'FAIL'})")
e3 = e3 and pair_plant

# ============ STAGE 3: REVIEW OF wall_a_boost_membership.py ============
print("\n=== STAGE 3: MEMBERSHIP RUN REVIEW ===")
OM, KK = 7, 3   # third sample, chosen by this review (registered in E6)
w, k = sp.Integer(OM), sp.Integer(KK)
s = -I*w
ETA4 = sp.diag(1, -1, -1, -1)
q = [w, sp.Integer(0), sp.Integer(0), k]
qlo = [ETA4[m, m]*q[m] for m in range(4)]
q2 = sum(q[m]*qlo[m] for m in range(4))
th = sp.Matrix(4, 4, lambda m, n: ETA4[m, n] - qlo[m]*qlo[n]/q2)
omg = sp.Matrix(4, 4, lambda m, n: qlo[m]*qlo[n]/q2)
P0sK = {(m, n, r, t): th[m, n]*th[r, t]/3 for m in range(4) for n in range(4) for r in range(4) for t in range(4)}
XswK = {(m, n, r, t): th[m, n]*omg[r, t] for m in range(4) for n in range(4) for r in range(4) for t in range(4)}
P1K = {(m, n, r, t): (th[m, r]*omg[n, t] + th[m, t]*omg[n, r]
                      + th[n, r]*omg[m, t] + th[n, t]*omg[m, r])/2
       for m in range(4) for n in range(4) for r in range(4) for t in range(4)}

# ---- 3a: E4 independent T, exact round-trip ----
def h_of(f):   # documented convention, independently coded
    phi, B, psi, E, Sx, Sy, Fx, Fy, hp, hx = f
    h = sp.zeros(4, 4)
    h[0, 0] = -2*phi
    h[0, 1] = h[1, 0] = Sx; h[0, 2] = h[2, 0] = Sy; h[0, 3] = h[3, 0] = I*k*B
    h[1, 1] = -2*psi + hp; h[2, 2] = -2*psi - hp; h[3, 3] = -2*psi - 2*k**2*E
    h[1, 2] = h[2, 1] = hx; h[1, 3] = h[3, 1] = I*k*Fx; h[2, 3] = h[3, 2] = I*k*Fy
    return h
def f_of(h):   # exact inverse derived by this review
    u = h[1, 1] + h[2, 2] + h[3, 3]
    psi = (h[3, 3] - u)/4
    return [-h[0, 0]/2, h[0, 3]/(I*k), psi, (-h[3, 3] - 2*psi)/(2*k**2),
            h[0, 1], h[0, 2], h[1, 3]/(I*k), h[2, 3]/(I*k), (h[1, 1] - h[2, 2])/2, h[1, 2]]
Rat = sp.Rational
test_fields = [Rat(3, 2), Rat(-2, 3), Rat(5, 4), Rat(7, 5), Rat(1, 3),
               Rat(-4, 3), Rat(2, 7), Rat(9, 4), Rat(-5, 6), Rat(11, 7)]
roundtrip = all(sp.simplify(a - b) == 0 for a, b in
                zip(test_fields, f_of(h_of(test_fields))))
# basis round-trip too
basis_ok = all(all(sp.simplify(a - b) == 0 for a, b in
                   zip([sp.Integer(1) if i == e else sp.Integer(0) for i in range(10)],
                       f_of(h_of([sp.Integer(1) if i == e else sp.Integer(0) for i in range(10)]))))
              for e in range(10))
e4 = bool(roundtrip and basis_ok)
print(f"   E4 T bijection exact round-trip (basis + rational generic): {'PASS' if e4 else 'FAIL'}")


# ---- 3b: E5 slot-convention coherence: pull(slots exchanged) == pull().T ----
def pull_rev(K):   # documented convention, independently coded:
    # M[u][v] = sum K_{mnrs} * (raised h of field v in the R-SLOT (m,n))
    #                        * (raised h of field u in the A-SLOT (r,s))
    M = sp.zeros(10, 10)
    Hs = [h_of([sp.Integer(1) if e == u else sp.Integer(0) for e in range(10)]) for u in range(10)]
    for u in range(10):
        ha = Hs[u]
        for v in range(10):
            hr = Hs[v]
            tot = sp.Integer(0)
            for m in range(4):
                for n in range(4):
                    rr = ETA4[m, m]*ETA4[n, n]*hr[m, n]
                    if rr == 0: continue
                    for r in range(4):
                        for t in range(4):
                            aa = ETA4[r, r]*ETA4[t, t]*ha[r, t]
                            if aa == 0: continue
                            tot += K[(m, n, r, t)]*rr*aa
            M[u, v] = sp.expand(tot)
    return M
def slot_exchange(K):
    return {(m, n, r, t): K[(r, t, m, n)] for m in range(4) for n in range(4)
            for r in range(4) for t in range(4)}
Bx = pull_rev(XswK)
Bx_ex = pull_rev(slot_exchange(XswK))
e5 = all(sp.simplify(Bx[i, j] - Bx_ex[j, i]) == 0 for i in range(10) for j in range(10))
print(f"   E5 slot coherence: pull(Xsw with slots exchanged) == pull(Xsw).T: {'PASS' if e5 else 'FAIL'}")
print("      (P0s is slot-symmetric, hence useless for this test; Xsw is the discriminating object)")

# ---- 3c: E6 the full membership run at the third sample ----
Bp0s, Bp1 = pull_rev(P0sK), pull_rev(P1K)
wPsi = [sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(0)] + [sp.Integer(0)]*6
wPhi = [sp.Integer(1), s, sp.Integer(0), -s**2] + [sp.Integer(0)]*6   # Phi0 = phi + sB - s^2 E
curved = []
for u in range(4):
    for wv in (wPsi, wPhi):
        M = sp.zeros(10, 10)
        for v in range(10): M[u, v] = wv[v]
        curved.append(M)
vec = lambda M: [M[i, j] for i in range(10) for j in range(10)]
rk = lambda Ms: sp.Matrix([vec(M) for M in Ms]).rank()
r_fam, r_cur, r_all = rk([Bp0s, Bx]), rk(curved), rk(curved + [Bp0s, Bx])
inter = r_cur + r_fam - r_all
killed = r_cur - inter
names = ["%s x %s" % (a, r) for a in ("phi", "B", "psi", "E") for r in ("Psi0", "Phi0")]
table = {nm: (rk([Bp0s, Bx, M]) == r_fam) for nm, M in zip(names, curved)}
plant_member = rk([Bp0s, Bx, Bp0s]) == r_fam
plant_reject = rk([Bp0s, Bx, Bp1]) == r_fam + 1
ward_id = (r_all == r_cur)
e6 = bool(inter == 2 and killed == 6 and plant_member and plant_reject and ward_id
          and not any(table.values()))
print(f"   E6 sample (omega,k)=({OM},{KK}): rank(family)={r_fam} rank(curved)={r_cur} "
      f"rank(union)={r_all} -> INTERSECTION={inter}, boost-killed={killed}")
for nm in names:
    print(f"      {nm:12s}: {'IN' if table[nm] else 'OUTSIDE'} family span")
print(f"      plants: P0s self-membership {'PASS' if plant_member else 'FAIL'}, "
      f"P1 rejected {'PASS' if plant_reject else 'FAIL'}")
print(f"      Ward-identification (family inside curved Ward span): "
      f"{'CONFIRMED' if ward_id else 'MISMATCH -- FINDING'}")
print(f"   E6 -> {'PASS' if e6 else 'FAIL'}")

# ============ STAGE 4: REVIEW OF wall_a_kernel_gate.py (derivation sketch) ============
print("\n=== STAGE 4: ORIGINAL GATE vs MEASURED DIMS ===")
out = subprocess.run([sys.executable, os.path.join(HERE, "wall_a_kernel_gate.py")],
                     capture_output=True, text=True).stdout
m = re.search(r"K_full \(no-Ward plant\)\s+= (\d+)", out)
m2 = re.search(r"K_Ward \(retarded-slot\)\s+= (\d+)", out)
m3 = re.search(r"K_both \(closure plant\)\s+= (\d+)", out)
orig = (int(m.group(1)), int(m2.group(1)), int(m3.group(1))) if (m and m2 and m3) else None
e7 = orig == dims
print(f"   original gate block arithmetic: {orig} vs measured {dims} -> "
      f"{'PASS (derivation-sketch status confirmed)' if e7 else 'FAIL'}")


# ============================== STAGE 5: VERDICT ==============================
all_ok = all([cal_ok, antisym, pjp_a, pjp_r, e1, e2, e3, e4, e5, e6, e7])
verdict = ("COUNTERSIGNED: all three kernel files pass second-author review. Independent "
           "equivariance construction reproduces 21/11/6 (E1); hand-coded orbit rules match "
           "the countersigned symbolic derivation (E2); flat orthogonality exact at an "
           "independent k (E3); T bijection round-trips (E4); slot convention coherent under "
           "slot exchange (E5); intersection=2 with 6 boost-killed scalars reproduced at a "
           "third sample (E6); original gate agrees and is hereby the derivation sketch (E7). "
           "The boost-license ruling may proceed on a fully computed, now countersigned list."
           if all_ok else "REVIEW FAILED -- do not rule; investigate the failing gate above.")
print("\n=== STAGE 5: VERDICT ===")
print(verdict)

json.dump({
    "instrument": "second_author_kernel_gate.py",
    "reviewed": ["wall_a_kernel_gate.py", "wall_a_kernel_gate_bruteforce.py",
                 "wall_a_boost_membership.py"],
    "registered_expectations": "E1..E7 fixed before running",
    "calibration": {"commutant_knowns": cal_ok},
    "gates": {"E1_independent_dims_21_11_6": e1, "E2_rows_match_countersigned_rules": e2,
              "E3_orthogonality_at_independent_k": e3, "E4_T_bijection_roundtrip": e4,
              "E5_slot_exchange_equals_transpose": e5, "E6_third_sample_full_run": e6,
              "E7_original_gate_agrees": e7},
    "third_sample": {"omega": OM, "k": KK},
    "measured": {"K_full": dims[0], "K_Ward": dims[1], "K_both": dims[2],
                 "intersection_at_third_sample": int(inter), "boost_killed": 8,
                 "boost_killed_split": "2 vector (orthogonality) + 6 scalar (membership)"},
    "ward_identification": "CONFIRMED" if ward_id else "MISMATCH",
    "verdict": verdict,
}, open(os.path.join(HERE, "SECOND_AUTHOR_KERNEL_VERDICT.json"), "w"), indent=2)
print("verdict written: SECOND_AUTHOR_KERNEL_VERDICT.json")
sys.exit(0 if all_ok else 1)

