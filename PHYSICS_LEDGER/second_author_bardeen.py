#!/usr/bin/env python3
"""Second-author review of wall_a_bardeen_basis.py -- INDEPENDENT re-derivation.

Protocol (mirrors the countersigned second_author_review.py pattern):
  Stage 0  object/metadata declarations (standing convention rule)
  Stage 1  calibration of the gauge machinery against knowns BEFORE any use
  Stage 2  independent derivation of the FRW gauge orbit via a DIFFERENT code
           path than the primary: Christoffel symbols + symmetrised covariant
           derivative, (L_xi g)_{mu nu} = nabla_mu xi_nu + nabla_nu xi_mu,
           instead of the primary's direct xi^l d_l g_mn + g_ln d_m xi^l + ...
           form.  Same tensor identity, independent implementation.
  Stage 3  derived transformation rules checked against the textbook knowns;
           Bardeen invariance COMPUTED (never asserted); plants must FAIL
  Stage 4  jet-space null-space dimension count at a rational sample point;
           Psi/Phi span membership IS the pure-gauge plant, done exactly
  Stage 5  cross-check against the primary's REGISTERED counts
  Stage 6  verdict JSON

AUTHORSHIP: second-author instrument, built at the owner's direction.
Stage-5 expectations were fixed from the primary's printed output BEFORE this
script was run (blind-comparison discipline).
"""
import sympy as sp
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ============================ STAGE 0: DECLARATIONS ============================
print("=== STAGE 0: OBJECT DECLARATIONS (standing convention rule) ===")
DECL = {
    "g": "FRW background metric, COVARIANT 2-tensor, g = a(eta)^2 diag(-1,1,1,1), conformal coords",
    "xi": "gauge generator, CONTRAVARIANT vector xi^mu; z-hat plane-wave mode Y=exp(ikz)",
    "dG": "gauge variation delta g_{mu nu} = (L_xi g)_{mu nu} -- COVARIANT components; "
          "NOT the perturbation field h_{mu nu} with raised indices",
    "Hc": "conformal Hubble a'/a, substituted symbolically AFTER differentiation",
    "jets": "field jets (phi,B,psi,E,phi',B',psi',E',E'') are INDEPENDENT coordinates, "
            "not derivatives of one another",
    "counts": "'9/6/3' etc. are FIELD-COMBINATION counts; the kernel-structure table in the "
              "primary is a PRE-REGISTERED PREDICTION and is out of scope here",
}
for kk, vv in DECL.items():
    print(f"   {kk:8s}: {vv}")

# ============ STAGE 1+2: INDEPENDENT MACHINERY + CALIBRATION GATES ============
eta, x, y, z = sp.symbols('eta x y z')          # <-- the scoping fix: ALL coords declared
X = [eta, x, y, z]
k = sp.Symbol('k', positive=True)
I = sp.I
a  = sp.Function('a')(eta)
al = sp.Function('alpha')(eta)      # xi^0 scalar
be = sp.Function('beta')(eta)       # longitudinal scalar: xi^3 = i k beta Y
ta = sp.Function('tau')(eta)        # transverse vector: xi^1 = tau Y
Y  = sp.exp(I*k*z)

gl = sp.diag(-a**2, a**2, a**2, a**2)              # covariant background
gu = sp.diag(-1/a**2, 1/a**2, 1/a**2, 1/a**2)      # contravariant background

def Gamma(l, m, n):
    """Christoffel symbol Gamma^l_{mn} of gl -- computed, not recalled."""
    e = sp.Integer(0)
    for r in range(4):
        e += gu[l, r]*(sp.diff(gl[n, r], X[m]) + sp.diff(gl[m, r], X[n]) - sp.diff(gl[m, n], X[r]))
    return sp.simplify(e/2)

GAM = {(l, m, n): Gamma(l, m, n) for l in range(4) for m in range(4) for n in range(4)}

def dG(xi_vec, m, n):
    """(L_xi g)_{mn} = d_m xi_n + d_n xi_m - 2 Gamma^l_{mn} xi_l  (INDEPENDENT path).
    NOTE: the Christoffel term contracts the LOWERED xi_l, not xi^l."""
    xi_lo = [sum(gl[j, l]*xi_vec[j] for j in range(4)) for l in range(4)]
    e = sp.diff(xi_lo[n], X[m]) + sp.diff(xi_lo[m], X[n])
    for l in range(4):
        e -= 2*GAM[(l, m, n)]*xi_lo[l]
    return sp.expand(e)

print("\n=== STAGE 1: CALIBRATION GATES (machinery vs knowns, BEFORE use) ===")
g1 = True   # spatial translation must kill L_xi g (background is x-independent)
xi_tr = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0)]
for m in range(4):
    for n in range(4):
        if sp.simplify(dG(xi_tr, m, n)) != 0:
            g1 = False
print(f"   GATE 1  spatial translation kills L_xi g          : {'PASS' if g1 else 'FAIL'}")

g2 = True   # pure time translation must reproduce d/d(eta) g EXACTLY
xi_tt = [sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)]
for m in range(4):
    for n in range(4):
        if sp.simplify(dG(xi_tt, m, n) - sp.diff(gl[m, n], eta)) != 0:
            g2 = False
print(f"   GATE 2  time translation == d/d(eta) g componentwise: {'PASS' if g2 else 'FAIL'}")

g3 = True   # rotation about z must kill L_xi g (isotropy)
xi_rot = [sp.Integer(0), -y, x, sp.Integer(0)]
for m in range(4):
    for n in range(4):
        if sp.simplify(dG(xi_rot, m, n)) != 0:
            g3 = False
print(f"   GATE 3  z-rotation kills L_xi g                    : {'PASS' if g3 else 'FAIL'}")


# ================= STAGE 2: INDEPENDENT GAUGE-ORBIT DERIVATION =================
xi = [al*Y, ta*Y, sp.Integer(0), I*k*be*Y]         # upper-index xi^mu
print("\n=== STAGE 2: DERIVED GAUGE ORBIT (Christoffel path) ===")
dg = {(m, n): sp.simplify(dG(xi, m, n)) for m in range(4) for n in range(4)}

# read the perturbation deltas off the derived orbit (conventions as registered):
#   dg00=-2a^2 (dphi)Y ; dg03=a^2(ik dB)Y ; dg01=a^2(dS)Y ; dg11=-2a^2(dpsi)Y ;
#   dg33=a^2(-2dpsi-2k^2 dE)Y ; dg13=a^2(ik dF)Y ; dg12=a^2(dh)Y
dphi = sp.simplify(-dg[(0, 0)]/(2*a**2*Y))
dB   = sp.simplify( dg[(0, 3)]/(a**2*I*k*Y))
dS   = sp.simplify( dg[(0, 1)]/(a**2*Y))
dpsi = sp.simplify(-dg[(1, 1)]/(2*a**2*Y))
dE   = sp.simplify(-(dg[(3, 3)]/(a**2*Y) + 2*dpsi)/(2*k**2))
dF   = sp.simplify( dg[(1, 3)]/(a**2*I*k*Y))
dh   = sp.simplify( dg[(1, 2)]/(a**2*Y))
for nm, e in (("d_phi", dphi), ("d_B", dB), ("d_psi", dpsi), ("d_E", dE),
              ("d_S", dS), ("d_F", dF), ("d_h(TT)", dh)):
    print("   %-8s = %s" % (nm, sp.simplify(e)))

# ==================== STAGE 3: KNOWNS CHECK + BARDEEN + PLANTS ====================
Hc = sp.Symbol('Hc')
subH = {sp.Derivative(a, eta): Hc*a}
def H_(e):  # substitute H -> Hc for comparison with the knowns
    return sp.simplify(sp.expand(e).subs(subH))

KNOWN = {
    "dphi": al.diff(eta) + Hc*al,
    "dB":   be.diff(eta) - al,
    "dpsi": -Hc*al,
    "dE":   be,
    "dS":   ta.diff(eta),
    "dF":   ta,
    "dh":   sp.Integer(0),
}
derived = {"dphi": dphi, "dB": dB, "dpsi": dpsi, "dE": dE, "dS": dS, "dF": dF, "dh": dh}
print("\n=== STAGE 3a: DERIVED RULES vs TEXTBOOK KNOWNS ===")
rules_ok = {}
for nm in derived:
    ok = sp.simplify(H_(derived[nm]) - KNOWN[nm]) == 0
    rules_ok[nm] = bool(ok)
    print(f"   {nm:6s} matches known form: {'PASS' if ok else 'FAIL'}")

# Bardeen invariance -- COMPUTED through the derived rules (no printed claims):
dEp  = sp.diff(dE, eta)                # delta(E')   from the DERIVED delta(E)
dBp  = sp.diff(dB, eta)                # delta(B')
dEpp = sp.diff(dE, (eta, 2))           # delta(E'')
dPsi = H_(dpsi - Hc*(dB - dEp))                       # Psi  = psi  - H(B-E')
dPhi = H_(dphi + Hc*(dB - dEp) + (dBp - dEpp))        # Phi  = phi + H(B-E') + (B'-E'')
print("\n=== STAGE 3b: BARDEEN INVARIANCE (computed) ===")
print(f"   delta[Psi_Bardeen] = {dPsi}   -> {'INVARIANT' if dPsi == 0 else 'NOT INVARIANT'}")
print(f"   delta[Phi_Bardeen] = {dPhi}   -> {'INVARIANT' if dPhi == 0 else 'NOT INVARIANT'}")
psi_inv = bool(dPsi == 0)
phi_inv = bool(dPhi == 0)

print("\n=== STAGE 3c: PLANTS (must FAIL invariance) ===")
plant_psi = H_(dpsi) != 0     # bare psi
plant_E   = H_(dE)   != 0     # bare E  (P0s-analogue)
plant_B   = H_(dB)   != 0     # bare B
print(f"   bare psi delta = {H_(dpsi)}   -> correctly NOT invariant: {'PASS' if plant_psi else 'FAIL'}")
print(f"   bare E   delta = {H_(dE)}     -> correctly NOT invariant: {'PASS' if plant_E else 'FAIL'}")
print(f"   bare B   delta = {H_(dB)}     -> correctly NOT invariant: {'PASS' if plant_B else 'FAIL'}")

if not (g1 and g2 and g3):
    raise SystemExit("STOP: calibration gates failed; derivation may not proceed.")

# =================== STAGE 4: JET-SPACE NULL-SPACE COUNT ===================
print("\n=== STAGE 4: NULL-SPACE DIMENSION COUNT (rational sample point) ===")
jets = {sp.Derivative(al, (eta, 2)): sp.Symbol('A2'), sp.Derivative(al, eta): sp.Symbol('A1'), al: sp.Symbol('A0'),
        sp.Derivative(be, (eta, 2)): sp.Symbol('B2'), sp.Derivative(be, eta): sp.Symbol('B1'), be: sp.Symbol('B0'),
        sp.Derivative(ta, (eta, 2)): sp.Symbol('T2'), sp.Derivative(ta, eta): sp.Symbol('T1'), ta: sp.Symbol('T0')}
def J(e): return sp.expand(e.subs(jets))

dsJ = {'phi': J(dphi), 'B': J(dB), 'psi': J(dpsi), 'E': J(dE),
       'phi_p': J(sp.diff(dphi, eta)), 'B_p': J(sp.diff(dB, eta)),
       'psi_p': J(sp.diff(dpsi, eta)), 'E_p': J(sp.diff(dE, eta)), 'E_pp': J(sp.diff(dE, (eta, 2)))}
coordsS = ['phi', 'B', 'psi', 'E', 'phi_p', 'B_p', 'psi_p', 'E_p', 'E_pp']
paramsS = [sp.Symbol(s) for s in ('A0', 'A1', 'A2', 'B0', 'B1', 'B2')]

leftover = [sp.expand(dsJ[c] - sum(dsJ[c].coeff(p)*p for p in paramsS)) for c in coordsS]
lin_ok = all(l == 0 for l in leftover)
print(f"   orbit linear in the 6 declared jet params: {'PASS' if lin_ok else 'FAIL: '+str(leftover)}")
assert lin_ok, "orbit not linear in declared jet params"

# rational sample point (generic): a=13/10, a'=2/5, a''=9/10, k=2
R = sp.Rational
def sample(e):
    return sp.nsimplify(sp.cancel(
        e.subs(sp.Derivative(a, (eta, 2)), R(9, 10))
         .subs(sp.Derivative(a, eta), R(2, 5))
         .subs(a, R(13, 10)).subs(k, 2)))
M = sp.Matrix([[sample(dsJ[c]).coeff(p) for c in coordsS] for p in paramsS])
rkS = M.rank()
nullS = M.nullspace()
print(f"   SCALAR: jet coords 9, orbit params 6, rank = {rkS} -> invariants = {9 - rkS}")
scalar_count_ok = bool(rkS == 6 and len(nullS) == 3)

# Psi/Phi span membership == the exact pure-gauge plant:
#   a covector w annihilates every orbit direction  <=>  the combination w.c is
#   gauge-invariant  <=>  every pure-gauge configuration is killed by it.
Hn = R(2, 5)/R(13, 10)   # Hc at the sample point = 4/13
covPsi = sp.Matrix([0, -Hn, 1, 0, 0, 0, 0,  Hn,  0])
covPhi = sp.Matrix([1,  Hn, 0, 0, 0, 1, 0, -Hn, -1])
N = sp.Matrix.vstack(*[v.T for v in nullS])
psi_in_span = bool(sp.Matrix.vstack(N, covPsi.T).rank() == N.rank())
phi_in_span = bool(sp.Matrix.vstack(N, covPhi.T).rank() == N.rank())
print(f"   Psi_Bardeen covector in null space (pure-gauge plant, exact): {'PASS' if psi_in_span else 'FAIL'}")
print(f"   Phi_Bardeen covector in null space (pure-gauge plant, exact): {'PASS' if phi_in_span else 'FAIL'}")

fieldsyms = sp.symbols('phi B psi E phi_p B_p psi_p E_p E_pp')
print("   scalar invariants (sample-point forms):")
for v in nullS:
    print("     ", sp.simplify(sum(sp.nsimplify(v[i])*fieldsyms[i] for i in range(9))))

# vector sector
dsV = {'S': J(dS), 'F': J(dF), 'S_p': J(sp.diff(dS, eta)), 'F_p': J(sp.diff(dF, eta))}
coordsV = ['S', 'F', 'S_p', 'F_p']
paramsV = [sp.Symbol(s) for s in ('T0', 'T1', 'T2')]
MV = sp.Matrix([[sample(dsV[c]).coeff(p) for c in coordsV] for p in paramsV])
rkV = MV.rank()
print(f"   VECTOR: jet coords 4, orbit params 3, rank = {rkV} -> invariants = {4 - rkV}")
vector_count_ok = bool(rkV == 3)
S_, F_, S_p, F_p = sp.symbols('S F S_p F_p')
vec_forms = [sp.simplify(sum(sp.nsimplify(v[i])*[S_, F_, S_p, F_p][i] for i in range(4)))
             for v in MV.nullspace()]
for f in vec_forms:
    print("     vector invariant:", f)
vector_form_ok = bool(len(vec_forms) == 1 and sp.simplify(vec_forms[0] - (F_p - S_)) == 0)
print(f"   vector invariant is F' - S: {'PASS' if vector_form_ok else 'FAIL'}")

# tensor sector
tensor_ok = bool(sp.simplify(dh) == 0)
print(f"   TENSOR: delta h_TT = {sp.simplify(dh)}  -> h_TT invariant outright: {'PASS' if tensor_ok else 'FAIL'}")

# ============ STAGE 5: CROSS-CHECK vs PRIMARY'S REGISTERED OUTPUT ============
print("\n=== STAGE 5: CROSS-CHECK vs wall_a_bardeen_basis.py (registered before run) ===")
# Registered from the primary's printed output prior to running THIS script:
PRIMARY = {"scalar_invariants": 3, "vector_invariants": 1, "tensor_invariant": True}
x_scalar = bool((9 - rkS) == PRIMARY["scalar_invariants"])
x_vector = bool((4 - rkV) == PRIMARY["vector_invariants"])
x_tensor = bool(tensor_ok == PRIMARY["tensor_invariant"])
x_rules  = bool(all(rules_ok.values()) and psi_inv and phi_inv
                and plant_psi and plant_E and plant_B)
print(f"   scalar count 3 == 3 : {'PASS' if x_scalar else 'FAIL'}")
print(f"   vector count 1 == 1 : {'PASS' if x_vector else 'FAIL'}")
print(f"   tensor invariant    : {'PASS' if x_tensor else 'FAIL'}")
print(f"   rules + Bardeen + plants all consistent: {'PASS' if x_rules else 'FAIL'}")

# ============================== STAGE 6: VERDICT ==============================
all_ok = all([g1, g2, g3, *rules_ok.values(), psi_inv, phi_inv,
              plant_psi, plant_E, plant_B, lin_ok, scalar_count_ok,
              psi_in_span, phi_in_span, vector_count_ok, vector_form_ok,
              tensor_ok, x_scalar, x_vector, x_tensor, x_rules])
verdict = ("Bardeen basis CONFIRMED by independent reviewer: gauge orbit re-derived via "
           "Christoffel path; rules match knowns; delta[Psi]=delta[Phi]=0 computed; plants "
           "fail as required; null-space counts 3/1/1 reproduce the primary; Psi and Phi "
           "span-membership exact at a rational sample point."
           if all_ok else "SECOND-AUTHOR REVIEW FAILED -- see gate output above.")
print("\n=== STAGE 6: VERDICT ===")
print(verdict)

json.dump({
    "instrument": "second_author_bardeen.py",
    "reviewed": "wall_a_bardeen_basis.py",
    "independent_path": "Christoffel + nabla-symmetrised generator (vs primary's direct Lie form)",
    "calibration": {"gate1_translation_kills": g1, "gate2_timetranslation_is_dg": g2,
                    "gate3_rotation_kills": g3},
    "derived_rules_match_knowns": rules_ok,
    "bardeen": {"delta_Psi_zero": psi_inv, "delta_Phi_zero": phi_inv,
                "plants_bare_psi_nonzero": plant_psi, "plants_bare_E_nonzero": plant_E,
                "plants_bare_B_nonzero": plant_B},
    "nullspace": {"scalar_coords": 9, "scalar_params": 6, "scalar_rank": int(rkS),
                  "scalar_invariants": 9 - int(rkS), "Psi_in_span": psi_in_span,
                  "Phi_in_span": phi_in_span,
                  "vector_invariants": 4 - int(rkV), "vector_invariant": "F_p - S",
                  "tensor_dh_zero": tensor_ok},
    "cross_check_vs_primary": {"scalar_count": x_scalar, "vector_count": x_vector,
                               "tensor_invariant": x_tensor, "rules_and_plants": x_rules},
    "sample_point": {"a": "13/10", "ap": "2/5", "app": "9/10", "k": 2},
    "verdict": verdict,
}, open(os.path.join(HERE, "SECOND_AUTHOR_BARDEEN_VERDICT.json"), "w"), indent=2)
print("verdict written: SECOND_AUTHOR_BARDEEN_VERDICT.json")

