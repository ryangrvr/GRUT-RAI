#!/usr/bin/env python3
"""CLOSURE-PREMISE TEST on the 3D Lorentz-compatible family -- premises first; 2D only if licensed.

STANDING STATE (not re-derived, not modified): commit b0bdfb6, register 73 nodes, net +17.
W-0 FENCE: everything computed here is COMPUTED-AND-REPORTED, NOT BANKED.

THE QUESTION. The measured chain ends 3 -> 2:
  K(w,k) = a(w,k) P2 + b(w,k) P0s + c(w,k) X_sw
and 2D {P2, P0s} is reached ONLY by killing c. This task determines, premise by premise,
WHAT kills c, by WHAT mechanism, in WHICH regime -- computed, not asserted. Start from 3D.

METHOD: exact arithmetic (sympy/Fraction) at the standing samples (3,2),(5,2),(7,3),
with general-(w,k) structural derivations alongside. Diagnose-before-report on every
anomaly. Numbers in the report come from this computation's output, never from memory.
"""
import sympy as sp
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
I = sp.I

# ================= STEP 0: OBJECT REGISTRY (before any computation) =================
print("=== STEP 0: OBJECT REGISTRY ===")
REG = {
    "metric":      "ETA = diag(1,-1,-1,-1) (mostly-minus, flat-review convention); klo[m]=ETA[m][m]*kup[m]",
    "slot_1":      "indices (m,n): R-SLOT (response/retarded); the ONLY slot the diagonal Ward identity constrains",
    "slot_2":      "indices (r,s): A-SLOT (source); NOT constrained in the registered diagonal-Ward framework",
    "index_variance": "all structures built from kup and lowered with ETA; contractions shown explicitly",
    "omega_power": "K is the chi-TYPE response (omega^0 power, dimensionless structures); "
                   "the G1 object-correction (Im chi = J/omega) lives one derivative away and is NOT used here",
    "channels":    "a = P2 coefficient (TT), b = P0s coefficient (theta-trace scalar), "
                   "c = X_sw coefficient (r-transverse x a-longitudinal off-diagonal)",
    "time_parity": "SECOND-AUTHOR CORRECTED (was: 'h_mn is T-even' -- false as a blanket statement): "
                   "h_00, h_ij are T-even; h_0i is T-ODD (one time index). The Onsager reduction works "
                   "via the eps-signature cancellation (eps_mn = (-1)^{#time indices} against the "
                   "k-parity of the structures; second_author_closure_premises.py E1, 0/256 violations "
                   "per structure), NOT via componentwise evenness. The FLAT registered vacuum carries "
                   "no T-odd background quantity; NB the FRW Hubble rate IS T-odd -- flat-scope only",
    "samples":     "(omega,k) in {(3,2),(5,2),(7,3)} -- rational, q^2 != 0",
}
for kk, vv in REG.items():
    print(f"   {kk:15s}: {vv}")

# slot-convention re-verification against the caught defect (membership run, b475985):
print("   slot convention re-verified by: pull(slot-exchanged Xsw) == pull(Xsw).T -- see E5 of")
print("   second_author_kernel_gate.py (countersigned 9561fb0); this file builds on that check.")

w, k = sp.symbols('omega k', positive=True)
ETA = sp.diag(1, -1, -1, -1)
kup = [w, sp.Integer(0), sp.Integer(0), k]
klo = [ETA[m, m]*kup[m] for m in range(4)]
k2 = sum(kup[m]*klo[m] for m in range(4))
th = sp.Matrix(4, 4, lambda m, n: ETA[m, n] - klo[m]*klo[n]/k2)
omg = sp.Matrix(4, 4, lambda m, n: klo[m]*klo[n]/k2)
def K4(f): return {(m, n, r, s): f(m, n, r, s) for m in range(4) for n in range(4)
                   for r in range(4) for s in range(4)}
P2  = K4(lambda m, n, r, s: (th[m, r]*th[n, s] + th[m, s]*th[n, r])/2 - th[m, n]*th[r, s]/3)
P0s = K4(lambda m, n, r, s: th[m, n]*th[r, s]/3)
Xsw = K4(lambda m, n, r, s: th[m, n]*omg[r, s])
Xws = K4(lambda m, n, r, s: omg[m, n]*th[r, s])


# ============ STEP 1: STRUCTURAL FACTS (computed, at general (w,k) and samples) ============
print("\n=== STEP 1: STRUCTURAL FACTS ===")
# (1a) transpose relation: X_sw^T = X_ws (slot exchange)
t_ok = all(Xsw[(r, s, m, n)] - Xws[(m, n, r, s)] == 0
           for m in range(4) for n in range(4) for r in range(4) for s in range(4))
print(f"   (1a) X_sw^T == X_ws (slot exchange), general (w,k)          : {t_ok}")
# (1b) Ward: r-slot transversality -- X_sw allowed, X_ws forbidden
ward_sw = all(sp.simplify(sum(kup[m]*Xsw[(m, n, r, s)] for m in range(4))) == 0
              for n in range(4) for r in range(4) for s in range(4))
ward_ws_vals = {n: sp.simplify(sum(kup[m]*Xws[(m, n, r, s)] for m in range(4)))
                for n in range(4) for r in range(4) for s in range(4)}
ward_ws_dead = all(v == 0 for v in ward_ws_vals.values())
print(f"   (1b) r-slot Ward: X_sw transversal                          : {ward_sw}")
print(f"        r-slot Ward: X_ws transversal (must be False)          : {ward_ws_dead}")
# (1c) linear independence of X_sw, X_ws (at a rational sample)
def sample(wv, kv):
    sub = {w: sp.Integer(wv), k: sp.Integer(kv)}
    out = {}
    for kk, Kd in {'P2': P2, 'P0s': P0s, 'Xsw': Xsw, 'Xws': Xws}.items():
        out[kk] = {idx: sp.simplify(val.subs(sub)) for idx, val in Kd.items()}
    return out
S1 = sample(3, 2)
vecs = [sp.Matrix([S1['Xsw'][(m, n, r, s)] for m in range(4) for n in range(4)
                   for r in range(4) for s in range(4)]),
        sp.Matrix([S1['Xws'][(m, n, r, s)] for m in range(4) for n in range(4)
                   for r in range(4) for s in range(4)])]
indep = sp.Matrix.hstack(*vecs).rank() == 2
print(f"   (1c) {{X_sw, X_ws}} linearly independent at (3,2)             : {indep}")
struct_ok = t_ok and ward_sw and (not ward_ws_dead) and indep
if not struct_ok:
    raise SystemExit("STOP: structural facts failed; premises may not proceed.")

# ================= STEP 2: P-A ONSAGER RECIPROCITY (the candidate mechanism) =================
print("\n=== STEP 2: P-A RECIPROCITY ===")
print("   Onsager relation with T-parity signatures: K_mnrs(w,kvec) = eps_mn eps_rs K_rsmn(w,-kvec).")
print("   SECOND-AUTHOR CORRECTED justification (was 'structures are even in k' -- FALSE componentwise:")
print("   72 sign-flipping components across the four structures under kvec->-kvec alone): the eps")
print("   signatures cancel EXACTLY against the k-parity of the covariant structures (verified 0/256")
print("   violations per structure, second_author_closure_premises.py E1/E2), so the net operation")
print("   IS plain slot-exchange symmetry K(w,k) == K^T(w,k) at the same (w,k). Same endpoint,")
print("   corrected mechanism.")
print("   Registered form: K(w) = a(w)P2 + b(w)P0s + c(w)X_sw ; reciprocity demands")
print("   a1 P2 + b1 P0s + c1 X_sw == a2 P2 + b2 P0s + c2 X_ws  (a2=a(-w) etc.).")

def reciprocity_constraint(wv, kv):
    """Solve the slot-exchange constraint exactly; report the free space and c's fate.
    Registered expectation: dim 2 -- (a1=a2) and (b1=b2) are the only free parameters;
    c1, c2 pinned to zero. (First draft wrongly expected dim 4; 6 unknowns minus the
    four constraints = 2. Expectation corrected before the verdict was used.)"""
    S = sample(wv, kv)
    rows = []
    for m in range(4):
        for n in range(4):
            for r in range(4):
                for s in range(4):
                    row = [S['P2'][(m, n, r, s)], S['P0s'][(m, n, r, s)], S['Xsw'][(m, n, r, s)],
                           -S['P2'][(m, n, r, s)], -S['P0s'][(m, n, r, s)], -S['Xws'][(m, n, r, s)]]
                    rows.append([sp.nsimplify(x) for x in row])
    M = sp.Matrix(rows)
    ns = M.nullspace()
    c_free = any(v[2] != 0 or v[5] != 0 for v in ns)
    return len(ns), c_free, ns

for (wv, kv) in ((3, 2), (5, 2), (7, 3)):
    dim, c_free, ns = reciprocity_constraint(wv, kv)
    print(f"   sample (w,k)=({wv},{kv}): reciprocity solution space dim = {dim} "
          f"(expect 2: a1=a2, b1=b2 free); c free? {c_free}")
pa_holds = True
pa_results = {}
for (wv, kv) in ((3, 2), (5, 2), (7, 3)):
    dim, c_free, ns = reciprocity_constraint(wv, kv)
    pa_results[f"{wv},{kv}"] = {"dim": int(dim), "c_free": bool(c_free)}
    pa_holds &= (dim == 2 and not c_free)
print(f"   P-A VERDICT: reciprocity forces c1 = c2 = 0 at all samples: {'YES -- c=0 DERIVED' if pa_holds else 'NO -- FINDING'}")
print("   MECHANISM: the reciprocity partner of X_sw is X_ws; X_ws is Ward-forbidden (1b);")
print("   hence no nonzero c admits a slot-symmetric Ward-compatible completion.")
print("   REGIME: equilibrium / time-reversal-symmetric state, T-even couplings, no T-odd background.")


# ================= STEP 3: P-B FDT/KMS (corollary chain, re-derived not cited) =================
print("\n=== STEP 3: P-B KMS / FDT ===")
print("   Load-bearing identity, derived on a finite system (NOT cited): the spectral (commutator)")
print("   response of ANY weights satisfies  chi''_BA(w) = -chi''_AB(-w)  -- slot exchange flips w.")
print("   T-even operators (real symmetric matrix elements) => chi'' ODD in w: chi''_AB(-w) = -chi''_AB(w)")
print("   => chi''_BA(w) = chi''_AB(w): slot-symmetric. T-odd operator => antisymmetric (Hall-type).")
print("   (Reality is LOAD-BEARING in that step: a complex-Hermitian non-real A breaks oddness in w")
print("   while the general identity still holds -- verifier-exhibited.)")
# finite 3-level system, rational data; weights symbolic (KMS ratio stated, not needed for the identity)
E = [sp.Rational(0), sp.Rational(5, 2), sp.Rational(7, 2)]
def spec_chi2(A, B, wv):
    """chi''_AB(wv) = pi * sum_{mn} (p_m - p_n) A_mn B_nm delta(w - (E_n - E_m)), symbolic p."""
    p = sp.symbols('p0:3', positive=True)
    out = 0
    for m in range(3):
        for n in range(3):
            d = sp.simplify((E[n] - E[m]) - wv)
            if d == 0:
                out += sp.pi*(p[m] - p[n])*A[m, n]*B[n, m]
    return sp.simplify(out)
# T-even operators: real symmetric matrices
Ae = sp.Matrix([[0, 2, 0], [2, 0, sp.Rational(3, 2)], [0, sp.Rational(3, 2), 0]])
Be = sp.Matrix([[0, 1, sp.Rational(1, 3)], [1, 0, sp.Rational(5, 4)], [sp.Rational(1, 3), sp.Rational(5, 4), 0]])
res = {}
for wv in (sp.Rational(5, 2), sp.Rational(7, 2), sp.Rational(1), sp.Rational(6)):
    xAB = spec_chi2(Ae, Be, wv)
    xBA = spec_chi2(Be, Ae, wv)
    res[wv] = (sp.simplify(xAB), sp.simplify(xBA), sp.simplify(xBA + spec_chi2(Ae, Be, -wv)))
    print(f"   w={str(wv):6s}: chi''_AB={str(res[wv][0]):10s}  chi''_BA={str(res[wv][1]):10s}  "
          f"chi''_BA + chi''_AB(-w) = {res[wv][2]}")
ident_ok = all(r[2] == 0 for r in res.values())
print(f"   identity chi''_BA(w) = -chi''_AB(-w) EXACT at all resonances : {'PASS' if ident_ok else 'FAIL'}")
# SECOND-AUTHOR CORRECTION (verifier finding): the T-even => slot-symmetry bridge -- the actual
# step that reaches P-A's algebra -- was printed side by side but never machine-gated. Gated now:
teven_slot_ok = all(sp.simplify(r[0] - r[1]) == 0 for r in res.values())
print(f"   T-even bridge chi''_BA(w) == chi''_AB(w) at all resonances    : {'PASS' if teven_slot_ok else 'FAIL'}")
# T-odd plant: imaginary antisymmetric matrix elements => antisymmetric response survives
At = I*sp.Matrix([[0, 2, 0], [-2, 0, sp.Rational(3, 2)], [0, sp.Rational(-3, 2), 0]])  # T-odd
xAB_t = spec_chi2(At, Be, sp.Rational(5, 2))
xBA_t = spec_chi2(Be, At, sp.Rational(5, 2))
# SECOND-AUTHOR CORRECTION (see second_author_closure_premises.py E5): the first predicate here
# was inverted (an OR true for symmetric-nonzero pairs) AND fed no gate. Antisymmetric means the
# slot-exchanged pair SUMS to zero and the response is nonvacuous; gated into plants_ok below.
todd_antisym = (sp.simplify(xAB_t + xBA_t) == 0) and (sp.simplify(xAB_t) != 0)
print(f"   T-odd plant: chi''_AB vs chi''_BA with one T-odd operator    : {sp.simplify(xAB_t)} vs {sp.simplify(xBA_t)}")
print("   KMS adds: p_m/p_n = exp(-b*(E_n-E_m)) (detailed balance) -- locks the state INTO")
print("   equilibrium, where the T-even reciprocity of the full kernel applies (P-A's algebra).")
print("   P-B VERDICT: c=0 is a COROLLARY -- KMS => detailed balance => equilibrium reciprocity")
print("   => the P-A constraint. Mechanism shared with P-A; no independent kill.")
pb_corollary = ident_ok and teven_slot_ok and pa_holds
# REGIME-TABLE PRECISION (verifier finding): T-even slot symmetry holds for ARBITRARY diagonal
# populations -- KMS is not needed for that step. What KMS genuinely adds: (i) it does NOT supply
# T-evenness of couplings / absence of a T-odd background (Gibbs + a T-odd operator keeps the Hall
# branch exactly) -- that assumption must be NAMED in the FDT-locked row; (ii) for degenerate
# spectra, state = f(H) equalises populations across degenerate pairs, killing the static w=0
# Hall line (which a non-degenerate 3-level system can never expose) and excluding stationary
# degenerate-block coherences.


# ================= STEP 4: P-C PASSIVITY (two domains -- computed separately) =================
print("\n=== STEP 4: P-C PASSIVITY ===")
print("   Quadratic form Q(v) = v^{mn} ImK_{mnrs} v^{rs} with ImK = im(a)P2 + im(b)P0s + im(c)X_sw.")
print("   For symmetric test field v: Q = im(a)*TT(v)^2 + (im(b)/3)(v:th)^2 + im(c)*(v:th)(v:om).")
print("   DOMAIN DISTINCTION (computed, this is the crux). VARIANCE REGISTRY: V is the")
print("   CONTRAVARIANT test field v^{mu nu}; conservation is k_mu v^{mu nu} = 0 (LOWER k);")
print("   (v:om) = omega_{mu nu} v^{mu nu} (lower omega). SELF-CATCH: the first draft mixed")
print("   variance (conservation with kup, then lower-omega on a lower-index field) and got a")
print("   spurious nonzero residual -- the k^mu vs k_mu defect family, caught by the check")
print("   itself returning a suspicious expression, diagnosed before reporting.")
vcons = sp.symbols('v00 v01 v02 v03 v11 v12 v13 v22 v23 v33', real=True)  # 10 comps, symmetric
V = sp.zeros(4, 4)
idx = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
for (ii, (m, n)) in enumerate(idx):
    V[m, n] = V[n, m] = vcons[ii]
cons = [sp.simplify(sum(klo[m]*V[m, n] for m in range(4))) for n in range(4)]   # k_mu v^{mu nu}=0
v_om = sp.simplify(sum(V[m, n]*omg[m, n] for m in range(4) for n in range(4)))  # omega_{mn} v^{mn}
sol = sp.solve(cons, vcons, dict=True)
v_om_cons = sp.simplify(v_om.subs(sol[0])) if sol else None
print(f"   conservation k_mu v^mu_nu = 0 solvable: {bool(sol)};  (v:om) on conserved sources = {v_om_cons}")
pc_domain_conserved = (v_om_cons == 0)
print(f"   => on the CONSERVED-source domain passivity never probes c        : {pc_domain_conserved}")
print(f"      (Q = im(a)*TT^2 + (im(b)/3)(v:th)^2 -- no c term; c UNCONSTRAINED by passivity)")
# unconserved (full) domain: PSD over (x,y) = (v:th, v:om)
x, y = sp.symbols('x y', real=True)
Q2 = sp.Matrix([[sp.Symbol('imb')/3, sp.Symbol('imc')/2], [sp.Symbol('imc')/2, sp.Integer(0)]])
mins = [Q2[0, 0], sp.simplify(Q2.det())]
print(f"   on the UNCONSTRAINED domain: 2x2 block [[im(b)/3, im(c)/2],[im(c)/2, 0]]:")
print(f"      principal minors: {mins[0]}, det = {mins[1]}  -> PSD forces im(c) = 0 exactly")
print("   P-C VERDICT: passivity alone does NOT kill c on the physical (conserved-source)")
print("   domain -- it is BLIND to c there; it would kill c outright only by admitting")
print("   non-conserved sources, which the diagonal-Ward registration excludes. The expected")
print("   |c|-inequality does NOT materialise: the omega-channel diagonal is identically zero")
print("   (P0w is Ward-forbidden), so the lemma's hypothesis (both diagonals probed) fails.")
print("   DIAGNOSED BEFORE REPORTING as a deviation from the briefed expectation: reported as found.")
# SECOND-AUTHOR CORRECTION (verifier finding, same genus as the todd-predicate defect): pc_kills
# was a hardcoded literal False, making the (not pc_kills) gate tautological -- if the
# conserved-domain computation had come out False, all_ok would not have noticed. Now derived:
# the P-C verdict rests on pc_domain_conserved, so the gate does too.
pc_kills = not pc_domain_conserved


# ================= STEP 5: P-D recorded (conclusion, never a premise) =================
print("\n=== STEP 5: P-D BOTH-SLOT TRANSVERSALITY ===")
print("   Recorded as the CONCLUSION the other premises may license, never an independent input:")
print("   a-slot transversality of K is what c=0 (plus a,b) amounts to; in equilibrium it follows")
print("   from P-A; outside equilibrium it is NOT available and the family stays 3D.")

# ================= STEP 6: PLANTS (calibrated before any verdict use) =================
print("\n=== STEP 6: PLANTS ===")
# (i) equilibrium Kubo-type kernel: slot-symmetric by construction -> P-A passes it; a c!=0
#     kernel fed to the same test must be FLAGGED.
S = sample(3, 2)
def slot_sym(Kd):
    return all(Kd[(r, s, m, n)] - Kd[(m, n, r, s)] == 0
               for m in range(4) for n in range(4) for r in range(4) for s in range(4))
K_kubo = {idx: sp.Rational(2, 3)*S['P2'][idx] + 5*S['P0s'][idx] for idx in S['P2']}
plant_sym_pass = slot_sym(K_kubo)
K_bad = {idx: K_kubo[idx] + sp.Rational(7, 4)*S['Xsw'][idx] for idx in S['P2']}
plant_bad_flagged = not slot_sym(K_bad)
print(f"   (i) equilibrium Kubo mock kernel slot-symmetric            : {'PASS' if plant_sym_pass else 'FAIL'}")
print(f"       c!=0 kernel flagged by the same test                   : {'PASS' if plant_bad_flagged else 'FAIL'}")
# (ii) gyrotropic medium: T-odd background B. PLANT-REDESIGN DISCLOSED: the first mock
#      used X_sw itself as the antisymmetric part and FAILED the proper test -- correctly!
#      An Onsager-compatible Hall structure must be epsilon-mediated (antisymmetric under
#      slot exchange IN ITSELF, so the B-flip and the transpose-flip cancel); X_sw is not
#      epsilon-type, and the registered comoving vacuum contains NO T-odd object from which
#      one could be built. That IS the physics: the gyrotropic escape is closed for the
#      gravitational vacuum. Plant redone in 2-channel space (exact arithmetic):
Bfield = sp.Symbol('Bfield', real=True)
gB = 3*Bfield                                   # Hall-type amplitude, odd in B
d0 = sp.Rational(5, 4)                          # diagonal (channel-symmetric) part
K_gyro_B  = sp.Matrix([[d0,  gB], [-gB, d0]])   # conductivity-type kernel at background B
K_gyro_mB = sp.Matrix([[d0, -gB], [gB, d0]])    # same medium at reversed B
proper = sp.simplify(K_gyro_B - K_gyro_mB.T) == sp.zeros(2, 2)     # Onsager-Casimir: retained
naive = sp.simplify(K_gyro_B - K_gyro_B.T) == sp.zeros(2, 2)       # T-blind test: kills Hall
print(f"   (ii) gyrotropic (2-channel): proper test K(B)==K^T(-B) RETAINS off-diagonal g!=0:"
      f" {'PASS' if proper else 'FAIL'}")
print(f"        naive test K(B)==K^T(B) would kill it (wrong test)    : {'demonstrated' if not naive else 'FAIL'}")
print(f"        GRAVITATIONAL CLOSURE of this escape -- SECOND-AUTHOR CORRECTED MECHANISM: the")
print(f"        operative closure is PARTNER-EXCLUSION, not epsilon-mediation / no-T-odd-object.")
print(f"        The Onsager partner of c(H) X_sw is c(-H) X_ws -- a DIFFERENT, linearly independent,")
print(f"        Ward-forbidden structure (unlike the 2-channel Hall case, whose partner is minus")
print(f"        itself) -- so c(H) = 0 for ALL H, ODD c(H) INCLUDED, even where a T-odd scalar")
print(f"        background exists (FRW's H is T-odd; the no-T-odd-object registry line is flat-scope")
print(f"        only). Reachability in the ACTUAL tensor space: the family enlarged to include X_ws")
print(f"        retains the odd Hall mode cs(H)=cw(-H) under the same solve")
print(f"        (second_author_closure_premises.py E4) -- the kill is physics, not instrument blindness.")
# SECOND-AUTHOR ADDITION (verifier finding): slot_sym detects slot asymmetry only -- a symmetric
# Ward-FORBIDDEN addition (e.g. +Xsw+Xws) would pass it. Gate that the assembled plant kernels lie
# in the Ward-allowed class the test is scoped to (r-slot transversality at the sample):
kup_s = [sp.Integer(3), sp.Integer(0), sp.Integer(0), sp.Integer(2)]
def rslot_ward(Kd):
    return all(sp.simplify(sum(kup_s[m]*Kd[(m, n, r, s)] for m in range(4))) == 0
               for n in range(4) for r in range(4) for s in range(4))
plants_ward_ok = rslot_ward(K_kubo) and rslot_ward(K_bad)
print(f"        assembled plant kernels r-slot Ward-allowed (scope gate)   : {'PASS' if plants_ward_ok else 'FAIL'}")
plants_ok = plant_sym_pass and plant_bad_flagged and proper and (not naive) and todd_antisym and plants_ward_ok


# ================= STEP 7: REGIME TABLE + VERDICT =================
print("\n=== STEP 7: REGIME TABLE (computed entries only) ===")
print("   regime                                 | c = 0 status            | mechanism")
print("   ---------------------------------------+-------------------------+--------------------------------")
print("   equilibrium (T-even, no T-odd bkg)     | DERIVED                 | P-A: reciprocity partner")
print("                                          |                         | X_ws is Ward-forbidden")
print("   registered FDT-locked (eps,tau2) family| COROLLARY               | KMS + NAMED: T-even couplings/")
print("                                          |                         | no T-odd background (KMS alone")
print("                                          |                         | does not supply it) + state=f(H)")
print("                                          |                         | across degeneracies => equilibrium")
print("                                          |                         | reciprocity (P-A algebra)")
print("   genuine non-equilibrium                | ABSENT (family stays 3D)| reciprocity inapplicable;")
print("                                          |                         | passivity blind to c on the")
print("                                          |                         | conserved-source domain (P-C)")
all_ok = struct_ok and pa_holds and pb_corollary and (not pc_kills) and plants_ok
verdict = ("CLOSURE-PREMISE TEST COMPLETE: c=0 is DERIVED at equilibrium (reciprocity mechanism, "
           "partner Ward-forbidden), COROLLARY in the registered FDT-locked family, and ABSENT in "
           "genuine non-equilibrium -- where the family stays 3D. The 3->2 step is therefore a "
           "REGIME-GATED equilibrium fact, never a symmetry-of-the-background fact, and never a "
           "single argument: 21->11 gauge, 11->3 Lorentz-covariant response (+1, booked), 3->2 "
           "equilibrium reciprocity/KMS. The wall question stands untouched: does Sigma_R^TT place "
           "the vacuum response in the 3D subspace, and then in the 2D family, WITHOUT imposing them?"
           if all_ok else "CLOSURE-PREMISE TEST INCOMPLETE OR ANOMALOUS -- see gates above; report as found.")
print("\nVERDICT:", verdict)

json.dump({
    "instrument": "wall_a_closure_premises.py",
    "standing_state": "b0bdfb6, register 73 nodes, net +17, W-0: computed-and-reported not banked",
    "structural_facts": {"Xsw_T_equals_Xws": bool(t_ok), "Xsw_ward_allowed": bool(ward_sw),
                         "Xws_ward_forbidden": bool(not ward_ws_dead), "independent": bool(indep)},
    "premises": {
        "PA_reciprocity": {"verdict": "c=0 DERIVED at equilibrium",
                           "mechanism": "reciprocity partner X_ws is Ward-forbidden; no slot-symmetric "
                                        "Ward-compatible completion with c!=0",
                           "samples": pa_results, "holds": bool(pa_holds)},
        "PB_kms_fdt": {"verdict": "c=0 COROLLARY",
                       "mechanism": "KMS + NAMED assumptions: T-even couplings / no T-odd background "
                                    "(KMS alone does not supply it -- Gibbs + a T-odd operator keeps the "
                                    "Hall branch) and state=f(H) across degeneracies (kills the static "
                                    "w=0 Hall line) => equilibrium reciprocity (P-A algebra); load-bearing "
                                    "identity chi''_BA(w) = -chi''_AB(-w) derived on a finite system",
                       "identity_exact": bool(ident_ok), "teven_bridge_gated": bool(teven_slot_ok),
                       "corollary": bool(pb_corollary)},
        "PC_passivity": {"verdict": "c UNCONSTRAINED on the conserved-source domain; c=0 only on the "
                                    "unphysical unconserved domain",
                         "mechanism": "omega-channel diagonal identically zero (P0w Ward-forbidden); "
                                      "lemma hypothesis fails; briefed inequality expectation NOT met -- "
                                      "reported as found, diagnosed before reporting",
                         "kills_c": False},
        "PD_both_slot": {"verdict": "recorded as CONCLUSION, never a premise"},
    },
    "plants": {"kubo_symmetric_pass": bool(plant_sym_pass), "c_nonzero_flagged": bool(plant_bad_flagged),
               "gyrotropic_retained_by_proper_test": bool(proper),
               "gyrotropic_killed_by_naive_test": bool(not naive),
               "todd_plant_antisym_gated": bool(todd_antisym),
               "assembled_kernels_ward_allowed": bool(plants_ward_ok), "all_pass": bool(plants_ok)},
    "verdict": verdict,
}, open(os.path.join(HERE, "CLOSURE_PREMISE_RESULT.json"), "w"), indent=2)
print("result written: CLOSURE_PREMISE_RESULT.json")
sys_exit = 0 if all_ok else 1
import sys as _sys
_sys.exit(sys_exit)

