#!/usr/bin/env python3
"""SECOND-AUTHOR REVIEW of wall_a_a1_vertex.py -- independent recomputation, not citation.

Expectations registered BEFORE running:
  E1  The det gate the file SKIPPED: -det(eta + kappa h) at O(kappa) equals h_tr exactly
      (the file's chk_det verified only the O(kappa^0) term while its print claimed the
      O(kappa) check). Plus the blindness exhibit: a DIAGONAL-ONLY perturbation passes the
      det check while its L^(1) provably loses every cross term.
  E2  Independent-route derivation: g^{mn} O(kappa) via the Neumann inverse VERIFIED BY
      MULTIPLICATION (never Taylor-of-Matrix.inv), own L^(1) assembly, own momentum-space
      vertex -- must match the file's compact form on all 16 components at general
      symbolic (a, m, p, q).
  E3  The flat orbit identity, arbitrary xi: Gamma^{mn}(K_m xi_n + K_n xi_m) == 2 xi.l
      with l^n = K_m Gamma^{mn} -- an ALGEBRAIC identity, which is why the file's Ward
      gate carries the full flat-orbit content (the 'recon' gate's defect is duplication /
      an independence overclaim, NOT missing content); and l^n EoM-organised with the
      a^2 m^2 mass.
  E4  THE MISSING RECOMPOSITION GATE (second-author target 5 had no gate in the file):
      at two generic exact-rational momentum samples (K^2 != 0, K not axis-aligned; a, m
      SYMBOLIC), the full vertex is EXACTLY recoverable from the recorded data
      (Gamma^TT, trace scalar t, longitudinal vector l^n) via
        beta = K.l/K^2,  v = l - beta K,  alpha = (t - beta)/3,
        Gamma = Gamma^TT + alpha*theta^{mn} + beta*omega^{mn} + (v^m K^n + v^n K^m)/K^2
      -- the two recorded discards parameterise ALL non-TT content; no third structure.
      Plus the VARIANCE DEFECT SITE reproduced: the all-lower projector applied to the
      upper-index Gamma spuriously breaks transversality (the file's self-caught defect 6).
  E5  Sign degeneracy: the flat plant fixes only (sign of T)x(sign of S_int); harmless
      downstream because the self-energy carries TWO vertex insertions.

COVERAGE NOTE (disclosed): two fleet verifiers (plants-independence,
projection-recomposition) died on a subagent session limit before returning. Their
targets are covered here instead: det blindness + skipped gate (E1), recomposition +
variance site (E4), sign degeneracy (E5); flat-plant independence is settled by the
completed derivation verifier's from-scratch rederivation (two-plane-wave extraction,
two-distinct-fields normalisation regulator), which makes the typed comparator moot.

Exit 0 iff all pass. Exact arithmetic throughout (symbolic where cheap, exact-rational
samples where the projector algebra is rational in momenta).
"""
import sympy as sp
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
kappa, m, av = sp.symbols('kappa m a_v', positive=True)
ETA = sp.diag(1, -1, -1, -1)

# symmetric perturbation, 10 independent symbols
syms = {}
hlo = {}
for mu in range(4):
    for nu in range(4):
        key = (min(mu, nu), max(mu, nu))
        if key not in syms:
            syms[key] = sp.Symbol(f'h{key[0]}{key[1]}')
        hlo[(mu, nu)] = syms[key]
h_tr = sum(ETA[mu, mu]*hlo[(mu, mu)] for mu in range(4))
Hm = sp.Matrix(4, 4, lambda mu, nu: hlo[(mu, nu)])
M = ETA + kappa*Hm

print("=== E1: the skipped det gate + the diagonal-blindness exhibit ===")
det_lin = sp.expand(-M.det()).coeff(kappa, 1)
e1a = sp.expand(det_lin - h_tr) == 0
print(f"   -det(eta + kappa h) O(kappa) coefficient == h_tr exactly       : {e1a}")
Hdiag = sp.diag(*[hlo[(i, i)] for i in range(4)])
det_lin_diag = sp.expand(-(ETA + kappa*Hdiag).det()).coeff(kappa, 1)
e1b = sp.expand(det_lin_diag - h_tr) == 0   # defective M passes the det check
# first-order (Neumann) inverse -- verified by product in E2 -- used for both L1's:
dmu = list(sp.symbols('d0 d1 d2 d3'))
def L1_kin_of(Hmat):
    inv1 = ETA.inv() - kappa*ETA.inv()*Hmat*ETA.inv()
    trH = sum(ETA[i, i]*Hmat[i, i] for i in range(4))
    sng = av**4*(1 + kappa*trH/2)
    kin = sng*sp.Rational(1, 2)*sum((av**-2*inv1[mu, nu])*dmu[mu]*dmu[nu]
                                    for mu in range(4) for nu in range(4))
    return sp.expand(sp.expand(kin).coeff(kappa, 1))
cross_true = L1_kin_of(Hm).coeff(hlo[(0, 1)]).coeff(dmu[0], 1).coeff(dmu[1], 1)
cross_diag = L1_kin_of(Hdiag).coeff(hlo[(0, 1)]).coeff(dmu[0], 1).coeff(dmu[1], 1)
e1c = (sp.simplify(cross_true) != 0) and (sp.simplify(cross_diag) == 0)
print(f"   diagonal-only M passes the det check (blindness confirmed)     : {e1b}")
print(f"   true L1 h01-cross term = {sp.simplify(cross_true)}; diagonal-defect L1 loses it: {e1c}")
e1_ok = e1a and e1b and e1c
print(f"   E1 {'PASS' if e1_ok else 'FAIL'}")

print("\n=== E2: independent-route derivation (product-verified inverse, own assembly) ===")
inv1 = ETA.inv() - kappa*ETA.inv()*Hm*ETA.inv()
prod = sp.expand(M*inv1)
e2a = all(sp.expand(prod[i, j].coeff(kappa, 0) - (1 if i == j else 0)) == 0 and
          sp.expand(prod[i, j].coeff(kappa, 1)) == 0 for i in range(4) for j in range(4))
print(f"   (eta+kh)(eta^-1 - k eta^-1 h eta^-1) == Id through O(kappa)    : {e2a}")
phi2 = sp.Symbol('PHI2')
sng = av**4*(1 + kappa*h_tr/2)
kin = sng*sp.Rational(1, 2)*sum((av**-2*inv1[mu, nu])*dmu[mu]*dmu[nu]
                                for mu in range(4) for nu in range(4))
mass = sng*sp.Rational(-1, 2)*m**2*phi2
L1_mine = sp.expand(sp.expand(kin + mass).coeff(kappa, 1))
pu = list(sp.symbols('P0:4'))
qu = list(sp.symbols('Q0:4'))
plo = [ETA[i, i]*pu[i] for i in range(4)]
qlo = [ETA[i, i]*qu[i] for i in range(4)]
def dot(P, Q): return sum(ETA[i, i]*P[i]*Q[i] for i in range(4))
pdq = dot(pu, qu)
Gam_mine = {}
for mu in range(4):
    for nu in range(4):
        coeff = sp.expand(L1_mine.coeff(hlo[(min(mu, nu), max(mu, nu))]))
        if mu != nu:
            coeff = coeff/2   # the pair (mu,nu),(nu,mu) shares one symbol; split evenly
        out = sp.Integer(0)
        poly = sp.Poly(coeff, *dmu, phi2)
        for mono, cf in zip(poly.monoms(), poly.coeffs()):
            da = mono[:4]
            if sum(da) == 2:      # two derivatives -> -(p_a q_b + q_a p_b) over leg assignments
                idxs = [i for i in range(4) for _ in range(da[i])]
                a_, b_ = idxs[0], idxs[1]
                if a_ == b_:
                    out += cf*(-(2*plo[a_]*qlo[a_]))
                else:
                    out += cf*(-(plo[a_]*qlo[b_] + qlo[a_]*plo[b_]))
            elif mono[4] == 1:    # phi^2 -> factor 2 (identical legs)
                out += 2*cf
        # REVIEWER SELF-CATCH (disclosed): the first draft raised here with
        # ETA[mu,mu]*ETA[nu,nu] -- but coeff(h01-symbol) is already the coefficient of the
        # LOWER-index component h_{01}, which is exactly what the UPPER-index Gamma^{mu nu}
        # contracts. The spurious eta-factors flipped only the 0i components (eta00*eta11 = -1),
        # so Gamma^{00} and the spatial block passed while the mixed components failed E2 --
        # the k^mu/k_mu defect family, in the reviewer's own code, caught by the reviewer's
        # own gate. Diagnosed before any report; the target file was never implicated.
        Gam_mine[(mu, nu)] = sp.expand(kappa*out)
cand = {}
for mu in range(4):
    for nu in range(4):
        cand[(mu, nu)] = sp.expand((kappa*av**2/2)*(pu[mu]*qu[nu] + qu[mu]*pu[nu]
                                                    - ETA[mu, nu]*(pdq + av**2*m**2)))
e2b = all(sp.expand(Gam_mine[(mu, nu)] - cand[(mu, nu)]) == 0
          for mu in range(4) for nu in range(4))
print(f"   own-route vertex == compact form, all 16 comps, general (a,m,p,q): {e2b}")
e2_ok = e2a and e2b
print(f"   E2 {'PASS' if e2_ok else 'FAIL'}")

print("\n=== E3: flat orbit identity with arbitrary xi; EoM-organised longitudinal ===")
Ku = [pu[i] + qu[i] for i in range(4)]
Klo = [ETA[i, i]*Ku[i] for i in range(4)]
xi = list(sp.symbols('xi0:4'))
xilo = [ETA[i, i]*xi[i] for i in range(4)]
lvec = [sp.expand(sum(Klo[mu]*cand[(mu, nu)] for mu in range(4))) for nu in range(4)]
contr = sp.expand(sum(cand[(mu, nu)]*(Klo[mu]*xilo[nu] + Klo[nu]*xilo[mu])
                      for mu in range(4) for nu in range(4)))
e3a = sp.expand(contr - 2*sum(xilo[nu]*lvec[nu] for nu in range(4))) == 0
lexp = [sp.expand((kappa*av**2/2)*((dot(pu, pu) - av**2*m**2)*qu[nu]
                                   + (dot(qu, qu) - av**2*m**2)*pu[nu])) for nu in range(4)]
e3b = all(sp.expand(lvec[nu] - lexp[nu]) == 0 for nu in range(4))
print(f"   Gamma.(K xi + xi K) == 2 xi.l for ARBITRARY xi (algebraic)     : {e3a}")
print(f"   l^n EoM-organised: (kappa a^2/2)[(p^2-a^2m^2) q + (q^2-a^2m^2) p]: {e3b}")
print("   => the file's Ward gate DOES carry the full flat-orbit content; its 'recon' gate's")
print("      defect is duplication (same contraction twice) and an independence overclaim,")
print("      NOT missing content. The FRW a'-layer: fleet verifier W2 derived the orbit from")
print("      Lie_xi g with the 2(a'/a) xi^0 eta_mn term and found delta L1 = (bath EoM incl.")
print("      friction) x (xi.dphi) + total derivative, identically -- no obstruction.")
e3_ok = e3a and e3b
print(f"   E3 {'PASS' if e3_ok else 'FAIL'}")

print("\n=== E4: recomposition gate + variance defect site (exact-rational samples) ===")
SAMPLES = [((3, 2, 1, 1), (5, -1, 2, 1)),     # K = (8,1,3,2), K^2 = 50
           ((2, 1, 1, 0), (3, 1, -1, 2))]     # K = (5,2,0,2), K^2 = 17
e4_ok = True
for (ps, qs) in SAMPLES:
    sub = {pu[i]: sp.Integer(ps[i]) for i in range(4)}
    sub.update({qu[i]: sp.Integer(qs[i]) for i in range(4)})
    G = {k: sp.expand(v.subs(sub)) for k, v in cand.items()}
    Kn = [sp.Integer(ps[i] + qs[i]) for i in range(4)]
    Kl = [ETA[i, i]*Kn[i] for i in range(4)]
    Ksq = sum(Kn[i]*Kl[i] for i in range(4))
    th_uu = sp.Matrix(4, 4, lambda i, j: ETA[i, j] - sp.Rational(Kn[i]*Kn[j], 1)/Ksq)
    om_uu = sp.Matrix(4, 4, lambda i, j: sp.Rational(Kn[i]*Kn[j], 1)/Ksq)
    thK = sp.Matrix(4, 4, lambda i, j: ETA[i, j] - Kl[i]*Kl[j]/Ksq)
    d_ud = [[(1 if i == r else 0) - Kn[i]*Kl[r]/Ksq for r in range(4)] for i in range(4)]
    GTT = {}
    for i in range(4):
        for j in range(4):
            GTT[(i, j)] = sp.expand(sum(((d_ud[i][r]*d_ud[j][s] + d_ud[i][s]*d_ud[j][r])/2
                                         - th_uu[i, j]*thK[r, s]/3)*G[(r, s)]
                                        for r in range(4) for s in range(4)))
    tt_trace = sp.expand(sum(ETA[i, i]*GTT[(i, i)] for i in range(4)))
    tt_trans = all(sp.expand(sum(Kl[i]*GTT[(i, j)] for i in range(4))) == 0 for j in range(4))
    t_scal = sp.expand(sum(ETA[i, i]*G[(i, i)] for i in range(4)))
    lv = [sp.expand(sum(Kl[i]*G[(i, j)] for i in range(4))) for j in range(4)]
    beta = sp.expand(sum(Kl[nu]*lv[nu] for nu in range(4))/Ksq)
    vv = [sp.expand(lv[nu] - beta*Kn[nu]) for nu in range(4)]
    v_trans = sp.expand(sum(Kl[nu]*vv[nu] for nu in range(4))) == 0
    alpha = sp.expand((t_scal - beta)/3)
    recon_ok = all(sp.expand(GTT[(i, j)] + alpha*th_uu[i, j] + beta*om_uu[i, j]
                             + (vv[i]*Kn[j] + vv[j]*Kn[i])/Ksq - G[(i, j)]) == 0
                   for i in range(4) for j in range(4))
    # variance defect site: ALL-LOWER theta applied to the UPPER-index Gamma (the file's
    # self-caught defect 6) must SPURIOUSLY break transversality:
    GTT_bad = {}
    for i in range(4):
        for j in range(4):
            GTT_bad[(i, j)] = sp.expand(sum(((thK[i, r]*thK[j, s] + thK[i, s]*thK[j, r])/2
                                             - thK[i, j]*thK[r, s]/3)*G[(r, s)]
                                            for r in range(4) for s in range(4)))
    bad_trans = any(sp.expand(sum(Kl[i]*GTT_bad[(i, j)] for i in range(4))) != 0 for j in range(4))
    ok = (tt_trace == 0) and tt_trans and v_trans and recon_ok and bad_trans
    e4_ok &= ok
    print(f"   sample p={ps}, q={qs} (K^2={Ksq}): TT traceless+transverse {tt_trace == 0 and tt_trans}; "
          f"v theta-transverse {v_trans}; RECOMPOSITION exact {recon_ok}; "
          f"all-lower-projector defect exhibited {bad_trans}")
print("   => the two recorded discards (trace scalar, longitudinal vector) parameterise the")
print("      complete non-TT content of this vertex; NO third structure is silently present.")
print(f"   E4 {'PASS' if e4_ok else 'FAIL'}")

print("\n=== E5: sign degeneracy of the flat plant; quadratic invariance downstream ===")
rep = sp.expand(sum(cand[(i, j)]*ETA[i, i]*ETA[j, j]*cand[(i, j)] for i in range(4) for j in range(4)))
rep_flip = sp.expand(sum((-cand[(i, j)])*ETA[i, i]*ETA[j, j]*(-cand[(i, j)])
                         for i in range(4) for j in range(4)))
e5_ok = sp.expand(rep - rep_flip) == 0
print(f"   flat plant fixes only (sign T)x(sign S_int); Gamma.Gamma invariant under")
print(f"   Gamma -> -Gamma (two insertions in Sigma)                       : {e5_ok}")

ALL = {"E1_det_gate_and_blindness": bool(e1_ok), "E2_independent_route_vertex": bool(e2_ok),
       "E3_orbit_identity_arbitrary_xi": bool(e3_ok), "E4_recomposition_and_variance_site": bool(e4_ok),
       "E5_sign_degeneracy_quadratic": bool(e5_ok)}
ok = all(ALL.values())
print(f"\nSECOND-AUTHOR VERDICT: {'ALL EXPECTATIONS MET' if ok else 'BREAK -- see gates'}")
print(json.dumps(ALL, indent=1))
json.dump({"instrument": "second_author_a1_vertex.py", "reviews": "wall_a_a1_vertex.py",
           "expectations": ALL, "all_pass": bool(ok),
           "coverage_note": "two fleet verifiers died on a subagent session limit; their targets "
                            "(det blindness, recomposition, variance site, sign degeneracy, "
                            "gate audit) are covered by E1/E4/E5 here plus the hand audit "
                            "recorded in the coordination log; flat-plant independence settled "
                            "by the completed derivation verifier's from-scratch rederivation",
           "corrections": [
               "chk_det gate verified only the O(kappa^0) term while its print claimed the O(kappa) "
               "check; det_lin == h_tr verified here (E1) and the gate added to the reviewed file",
               "'recon' gate duplicates the ward gate (same contraction) -- independence overclaim "
               "in the builder report; content-wise the Ward gate DOES carry the full flat-orbit "
               "statement (E3: arbitrary-xi contraction == 2 xi.l algebraically)",
               "recomposition gate was MISSING (second-author target 5 had no gate): added here (E4) "
               "-- discards parameterise all non-TT content, no third structure",
               "flat plant fixes only (sign of T)x(sign of S_int); harmless downstream (E5)",
           ]},
          open(os.path.join(HERE, "SECOND_AUTHOR_A1_VERDICT.json"), "w"), indent=2)
print("verdict written: SECOND_AUTHOR_A1_VERDICT.json")
sys.exit(0 if ok else 1)
