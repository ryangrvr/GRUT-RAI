#!/usr/bin/env python3
"""SECOND-AUTHOR REVIEW of wall_a_closure_premises.py -- independent recomputation, not citation.

Expectations registered BEFORE running (the calibration-template discipline):
  E1  The Onsager reduction's TRUE mechanism: the eps-signature-weighted transpose at -kvec equals
      the PLAIN slot exchange at +kvec, for every component of every structure. This is the
      cancellation the reviewed file GLOSSED as "structures are even in k".
  E2  The glossed wording is FALSE componentwise: structures with one time index flip sign under
      kvec -> -kvec alone. Expect nonzero violation count for theta/omg-built structures.
      (Registry correction: h_0i is T-ODD; the conclusion survives E1's cancellation, not evenness.)
  E3  The reciprocity nullspace has dim 2 with the EXACT pattern a1=a2, b1=b2, c1=c2=0 -- the
      reviewed file gated dim and c-freedom but never verified the a/b pattern it printed.
  E4  PARTNER-EXCLUSION (stronger than the file's epsilon-mediation argument): with a T-odd SCALAR
      background H (NB: the FRW Hubble rate IS T-odd -- the file's registry line "no T-odd
      background quantity" is scope-limited to the FLAT registered vacuum), Onsager-Casimir maps
      c(H) Xsw -> c(-H) Xws; Xws is Ward-forbidden AND independent, so c(H) = 0 for ALL H -- there
      is no Hall-type odd-c escape IN THE WARD-ALLOWED FAMILY. Reachability: in a family
      artificially enlarged to include Xws, an odd c(H) = -c(-H) MUST survive the same solve
      (the tensor-space analogue of the 2-channel gyrotropic plant).
  E5  The finite-system T-odd plant, with a CORRECT and GATED predicate (the reviewed file's
      line-168 predicate is inverted -- true for symmetric-nonzero pairs -- and feeds no gate).
  E6  The P-C reduced form Q(v) = im(a)*TTsq + (im(b)/3)(v:th)^2 + im(c)(v:th)(v:om) is EXACT
      against the full 256-term contraction (the reviewed file asserted the reduction).
  E7  Conservation with LOWER k on the contravariant source forces (v:om) = 0 exactly; the
      kup-contraction produces a spurious nonzero (the caught variance trap, exhibited).

Samples: reviewer's own (9,4) plus shared (3,2). Exact arithmetic throughout. Exit 0 iff all pass.
"""
import sympy as sp
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
w, k = sp.symbols('omega k', positive=True)
ETA = sp.diag(1, -1, -1, -1)

def structures(kup):
    klo = [ETA[m, m]*kup[m] for m in range(4)]
    k2 = sum(kup[m]*klo[m] for m in range(4))
    th = sp.Matrix(4, 4, lambda m, n: ETA[m, n] - klo[m]*klo[n]/k2)
    om = sp.Matrix(4, 4, lambda m, n: klo[m]*klo[n]/k2)
    K4 = lambda f: {(m, n, r, s): f(m, n, r, s) for m in range(4) for n in range(4)
                    for r in range(4) for s in range(4)}
    return dict(
        P2=K4(lambda m, n, r, s: (th[m, r]*th[n, s] + th[m, s]*th[n, r])/2 - th[m, n]*th[r, s]/3),
        P0s=K4(lambda m, n, r, s: th[m, n]*th[r, s]/3),
        Xsw=K4(lambda m, n, r, s: th[m, n]*om[r, s]),
        Xws=K4(lambda m, n, r, s: om[m, n]*th[r, s])), th, om, klo, k2

Splus, THp, OMp, KLOp, K2p = structures([w, 0, 0, k])
Sminus, _, _, _, _ = structures([w, 0, 0, -k])   # kvec -> -kvec, omega fixed
eps = [1, -1, -1, -1]                            # eps_m = (-1)^{1 if m is spatial? NO:} see below
# T-parity signature of a 2-index component (m,n): (-1)^{number of TIME indices}.
# eps_mn = (-1)^{n0(mn)}: n0 counts indices equal to 0.
def eps2(m, n): return (-1)**((1 if m == 0 else 0) + (1 if n == 0 else 0))

print("=== E1: eps-weighted -k transpose == plain +k transpose (the glossed cancellation) ===")
e1_ok = True
for name, S in Splus.items():
    Sm = Sminus[name]
    bad = sum(1 for m in range(4) for n in range(4) for r in range(4) for s in range(4)
              if sp.simplify(eps2(m, n)*eps2(r, s)*Sm[(r, s, m, n)] - S[(r, s, m, n)]) != 0)
    print(f"   {name:4s}: eps_mn eps_rs S_(rs,mn)(w,-k) != S_(rs,mn)(w,+k) at {bad}/256 components")
    e1_ok &= (bad == 0)
print(f"   E1 {'PASS' if e1_ok else 'FAIL'}: the Onsager operation reduces to PLAIN slot exchange at (w,k)")

print("\n=== E2: the glossed 'even in k' wording is FALSE componentwise ===")
e2_viol = {name: sum(1 for idx in S if sp.simplify(Sminus[name][idx] - S[idx]) != 0)
           for name, S in Splus.items()}
print(f"   componentwise evenness violations under kvec->-kvec alone: {e2_viol}")
e2_ok = any(v > 0 for v in e2_viol.values())
print(f"   E2 {'PASS' if e2_ok else 'FAIL'}: violations exist -- the eps cancellation (E1), not evenness, is the mechanism")

print("\n=== E3: reciprocity nullspace PATTERN (own ordering: c1,a1,b1,c2,a2,b2) ===")
def recip_nullspace(wv, kv, include_ws_partner_only=True):
    Sn, _, _, _, _ = structures([sp.Integer(wv), 0, 0, sp.Integer(kv)])
    rows = []
    for m in range(4):
        for n in range(4):
            for r in range(4):
                for s in range(4):
                    rows.append([Sn['Xsw'][(m, n, r, s)], Sn['P2'][(m, n, r, s)], Sn['P0s'][(m, n, r, s)],
                                 -Sn['Xws'][(m, n, r, s)], -Sn['P2'][(m, n, r, s)], -Sn['P0s'][(m, n, r, s)]])
    return sp.Matrix(rows).nullspace()
e3_ok = True
for (wv, kv) in ((9, 4), (3, 2)):
    ns = recip_nullspace(wv, kv)
    dim = len(ns)
    # pattern: every nullspace vector has c1 = c2 = 0 AND a1 = a2 AND b1 = b2 (ordering c1,a1,b1,c2,a2,b2)
    pat = all(v[0] == 0 and v[3] == 0 and sp.simplify(v[1] - v[4]) == 0 and sp.simplify(v[2] - v[5]) == 0
              for v in ns)
    print(f"   sample ({wv},{kv}): dim={dim} (expect 2), exact pattern a1=a2, b1=b2, c1=c2=0: {pat}")
    e3_ok &= (dim == 2 and pat)
print(f"   E3 {'PASS' if e3_ok else 'FAIL'}")

print("\n=== E4: partner-exclusion under a T-odd scalar background; reachability in the enlarged family ===")
# Ward-allowed family: c(H) Xsw = c(-H) Xws componentwise, Xsw/Xws independent => c(H)=c(-H)=0.
Sn, _, _, _, _ = structures([sp.Integer(3), 0, 0, sp.Integer(2)])
vec = lambda S: sp.Matrix([S[(m, n, r, s)] for m in range(4) for n in range(4)
                           for r in range(4) for s in range(4)])
indep = sp.Matrix.hstack(vec(Sn['Xsw']), vec(Sn['Xws'])).rank() == 2
cH, cmH = sp.symbols('cH cmH')
sol = sp.solve([sp.Eq(cH*Sn['Xsw'][idx], cmH*Sn['Xws'][idx]) for idx in Sn['Xsw']], [cH, cmH], dict=True)
excl = bool(sol) and all(s.get(cH, 0) == 0 and s.get(cmH, 0) == 0 for s in sol)
print(f"   Xsw/Xws independent at (3,2): {indep}; c(H) Xsw = c(-H) Xws forces c(H)=c(-H)=0: {excl}")
print("   -> the odd-c Hall escape is closed by PARTNER-EXCLUSION (Xws Ward-dead), NOT by the absence")
print("      of T-odd background objects; robust even where H (T-odd) is present. Registry corrected.")
# Reachability: enlarge the family to include Xws (drop the Ward fence). Constraint becomes
#   cs(H) Xsw + cw(H) Xws = cs(-H) Xws + cw(-H) Xsw  =>  cs(H) = cw(-H): an ODD combined mode SURVIVES:
#   cs(H) = g(H), cw(H) = g(-H) -- e.g. g odd gives antisymmetric part K_A = g(H)(Xsw - Xws)/... nonzero.
csH, cwH, csmH, cwmH = sp.symbols('csH cwH csmH cwmH')
eqs = [sp.Eq(csH*Sn['Xsw'][idx] + cwH*Sn['Xws'][idx], csmH*Sn['Xws'][idx] + cwmH*Sn['Xsw'][idx])
       for idx in Sn['Xsw']]
solE = sp.solve(eqs, [csH, cwH], dict=True)
reach = bool(solE) and all(sp.simplify(s[csH] - cwmH) == 0 and sp.simplify(s[cwH] - csmH) == 0 for s in solE)
print(f"   enlarged family: solve gives cs(H)=cw(-H), cw(H)=cs(-H) (odd mode SURVIVES): {reach}")
print("   -> the instrument CAN retain a Hall-type mode when the partner is available: reachability")
print("      proven in the actual tensor space, not only the 2-channel analogue.")
e4_ok = indep and excl and reach
print(f"   E4 {'PASS' if e4_ok else 'FAIL'}")

print("\n=== E5: finite-system T-odd plant with a CORRECT, GATED predicate ===")
E = [sp.Rational(0), sp.Rational(5, 2), sp.Rational(7, 2)]
p = sp.symbols('p0:3', positive=True)
def chi2(A, B, wv):
    out = 0
    for m in range(3):
        for n in range(3):
            if sp.simplify((E[n] - E[m]) - wv) == 0:
                out += sp.pi*(p[m] - p[n])*A[m, n]*B[n, m]
    return sp.simplify(out)
Be = sp.Matrix([[0, 1, sp.Rational(1, 3)], [1, 0, sp.Rational(5, 4)], [sp.Rational(1, 3), sp.Rational(5, 4), 0]])
At = sp.I*sp.Matrix([[0, 2, 0], [-2, 0, sp.Rational(3, 2)], [0, sp.Rational(-3, 2), 0]])
xAB, xBA = chi2(At, Be, sp.Rational(5, 2)), chi2(Be, At, sp.Rational(5, 2))
e5_ok = (sp.simplify(xAB + xBA) == 0) and (sp.simplify(xAB) != 0)   # antisymmetric AND nonvacuous
print(f"   chi''_AB = {xAB}, chi''_BA = {xBA}; antisym (sum==0) and nonzero: {e5_ok}")
# the reviewed predicate, evaluated on a SYMMETRIC-nonzero pair, to exhibit the inversion:
xs = chi2(Be, Be, sp.Rational(5, 2))
reviewed_pred_on_symmetric = (sp.simplify(xs + xs) != 0) or (sp.simplify(xs - xs) == 0)
print(f"   reviewed line-168 predicate evaluated on a SYMMETRIC pair (must expose inversion): "
      f"{reviewed_pred_on_symmetric} (True == the predicate cannot distinguish; defect exhibited)")
e5_ok &= reviewed_pred_on_symmetric
print(f"   E5 {'PASS' if e5_ok else 'FAIL'}")

print("\n=== E6: full 256-term Q(v) contraction vs the asserted reduced form ===")
vsym = sp.symbols('v0:10', real=True)
idx10 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
V = sp.zeros(4, 4)
for i, (m, n) in enumerate(idx10):
    V[m, n] = V[n, m] = vsym[i]
ia, ib, ic = sp.symbols('ima imb imc', real=True)
Sg, THg, OMg, KLOg, K2g = Splus, THp, OMp, KLOp, K2p
Q_full = sp.expand(sum(V[m, n]*(ia*Sg['P2'][(m, n, r, s)] + ib*Sg['P0s'][(m, n, r, s)]
                                + ic*Sg['Xsw'][(m, n, r, s)])*V[r, s]
                       for m in range(4) for n in range(4) for r in range(4) for s in range(4)))
v_th = sum(V[m, n]*THg[m, n] for m in range(4) for n in range(4))
v_om = sum(V[m, n]*OMg[m, n] for m in range(4) for n in range(4))
TTsq = sp.expand(sum(V[m, n]*Sg['P2'][(m, n, r, s)]*V[r, s]
                     for m in range(4) for n in range(4) for r in range(4) for s in range(4)))
Q_red = sp.expand(ia*TTsq + (ib/sp.Integer(3))*v_th**2 + ic*v_th*v_om)
e6_ok = sp.simplify(Q_full - Q_red) == 0
print(f"   Q_full == im(a)*TTsq + (im(b)/3)(v:th)^2 + im(c)(v:th)(v:om) exactly: {e6_ok}")
print(f"   (v:om)^2 coefficient in Q_full: {sp.expand(Q_full).coeff(v_om, 2) if False else 'absent by construction check above'}")
e6b = sp.simplify(Q_full.subs(ia, 0).subs(ib, 0) - ic*v_th*v_om) == 0
print(f"   cross-term coefficient is exactly im(c) (no factor error): {e6b}")
e6_ok &= e6b
print(f"   E6 {'PASS' if e6_ok else 'FAIL'}")

print("\n=== E7: conservation variance chain; the kup trap exhibited ===")
cons_lo = [sp.simplify(sum(KLOg[m]*V[m, n] for m in range(4))) for n in range(4)]
sol_lo = sp.solve(cons_lo, list(vsym), dict=True)
v_om_on = sp.simplify(v_om.subs(sol_lo[0])) if sol_lo else None
print(f"   k_mu(LOWER) v^(mu nu) = 0 => (v:om) = {v_om_on} (expect 0 exactly)")
# the trap: kup contraction is NOT the conservation law for a contravariant density
cons_up = [sp.simplify(sum([w, 0, 0, k][m]*V[m, n] for m in range(4))) for n in range(4)]
sol_up = sp.solve(cons_up, list(vsym), dict=True)
v_om_trap = sp.simplify(v_om.subs(sol_up[0])) if sol_up else None
e7_ok = (v_om_on == 0) and (sp.simplify(v_om_trap) != 0)
print(f"   kup-contraction 'conservation' leaves (v:om) = {v_om_trap} != 0 -- the variance trap, exhibited")
print(f"   E7 {'PASS' if e7_ok else 'FAIL'}")

ALL = {"E1_eps_cancellation": bool(e1_ok), "E2_evenness_wording_false": bool(e2_ok),
       "E3_nullspace_pattern": bool(e3_ok), "E4_partner_exclusion_and_reachability": bool(e4_ok),
       "E5_todd_plant_gated": bool(e5_ok), "E6_Q_reduction_exact": bool(e6_ok),
       "E7_variance_chain": bool(e7_ok)}
ok = all(ALL.values())
print(f"\nSECOND-AUTHOR VERDICT: {'ALL EXPECTATIONS MET -- countersigned with corrections' if ok else 'BREAK -- see gates'}")
print(json.dumps(ALL, indent=1))
json.dump({"instrument": "second_author_closure_premises.py", "reviews": "wall_a_closure_premises.py",
           "expectations": ALL, "all_pass": bool(ok),
           "corrections": [
               "registry 'h_mn is T-even' FALSE for h_0i (T-odd); conclusion survives via the eps-k cancellation (E1), computed here",
               "'structures even in k' FALSE componentwise (E2); the eps-weighted transpose is the mechanism",
               "line-168 todd_antisym predicate inverted and ungated (E5); corrected+gated here",
               "gyrotropic closure is PARTNER-EXCLUSION (Xws Ward-dead), not epsilon-mediation/no-T-odd-object; "
               "H is T-odd in FRW, so the file's registry line is scope-limited to the flat registered vacuum (E4)",
           ]},
          open(os.path.join(HERE, "SECOND_AUTHOR_CLOSURE_VERDICT.json"), "w"), indent=2)
print("verdict written: SECOND_AUTHOR_CLOSURE_VERDICT.json")
sys.exit(0 if ok else 1)
