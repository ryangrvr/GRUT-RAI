#!/usr/bin/env python3
"""SECOND-AUTHOR REVIEW of wall_a_assembly1.py (ASSEMBLY-1) -- the checks that decide
whether ASSEMBLY-2 is authorised.

Expectations registered BEFORE running:
  E1  WICK/NORMALISATION, decided by an EXACT zero-dimensional QFT (no diagrams, no
      conventions -- a Gaussian integral): with S_int = (1/2) Gamma h phi^2 and
      <phi phi> = G, the O(h^2) 1PI coefficient is Sigma = (1/2) Gamma^2 G^2.
      The reviewed instrument's Step-3 formula Sigma_ab = eta_a eta_b
      (kappa^2 a1^2 a2^2 / 4) N (x) [G_ab]^2 with N = gamma (x) gamma equals
      Gamma1 Gamma2 [G]^2 -- NET FACTOR 1 -- which the toy refutes: expect HALF.
      (Equivalently: with the full unrestricted d^4l integral, l <-> K-l double-counts
      the pairing; the bubble's 1/2 must appear explicitly.)
  E2  CTP SIGN PIN, fully symbolic (theta as a symbol): with the SIGNED components
      Sigma_ab = eta_a eta_b S_ab, S_ab = (G_ab)^2, the retarded object is
        Sigma_R = Sigma_++ + Sigma_+-  =  S_++ - S_+-  = theta (F^2 - Ftilde^2).
      The instrument's numeric Gate 3 tested the UNSIGNED S row (correct object), but
      its LABEL "Sigma_R = Sigma++ - Sigma+-" applied to the signed components of its
      own Step 3 yields S_++ + S_+- which is NOT retarded (exhibit: 2 Ftilde^2 at
      t < 0). Also: the trace mix vanishes IDENTICALLY (largest-time identity) --
      confirming the instrument's disclosed computed fact symbolically.
  E3  THE k = 0 DEGENERACY: at K = (w, 0), the medium frame u is parallel to K, so
      every u-structure collapses into the {eta, K} span -- six-channel closure at
      k = 0 is kinematically guaranteed and carries NO placement information. At a
      k != 0 rational sample the {eta, K, u} symmetric-pair span STRICTLY EXCEEDS the
      six-channel span (rank grows) -- Q1's placement content lives at k != 0.

Exit 0 iff all three expectations are met (E1 'met' = the toy CONTRADICTS net factor 1).
"""
import sympy as sp
import json, os, sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

print("=== E1: THE WICK FACTOR, DECIDED EXACTLY (zero-dimensional QFT) ===")
h, G, Gam = sp.symbols('h G Gamma', positive=True)
phi = sp.Symbol('phi', real=True)
# Z(h) = int dphi exp(-phi^2/(2G) + (1/2) Gamma h phi^2): exact Gaussian
# log Z = -(1/2) log(1/G - Gamma h) + const = (1/2)[Gamma h G + (Gamma h G)^2/2 + ...]
logZ_series = sp.series(-sp.Rational(1, 2)*sp.log(1/G - Gam*h), h, 0, 3).removeO()
coeff_h2 = sp.expand(logZ_series).coeff(h, 2)
# 1PI two-point of h: effective action (1/2) Sigma h^2 => Sigma = 2 * coeff_h2
Sigma_exact = sp.simplify(2*coeff_h2)
expected_half = sp.Rational(1, 2)*Gam**2*G**2
claimed_net1 = Gam**2*G**2
e1a = sp.simplify(Sigma_exact - expected_half) == 0
e1b = sp.simplify(Sigma_exact - claimed_net1) != 0
print(f"   exact Gaussian: Sigma = {Sigma_exact}")
print(f"   equals (1/2) Gamma^2 G^2 (the bubble's symmetry factor)         : {e1a}")
print(f"   REFUTES the instrument's NET FACTOR 1 (Gamma^2 G^2)             : {e1b}")
print("   => the reviewed Step-3 formula Sigma_ab = eta_a eta_b (kappa^2 a1^2 a2^2/4)")
print("      N [G_ab]^2 with the FULL unrestricted d^4l integral OVERCOUNTS BY 2: the")
print("      l <-> K-l exchange maps the integrand to itself, so either the integral is")
print("      halved or an explicit 1/2 restores the bubble symmetry factor. This is a")
print("      NORMALISATION defect (does not touch support, placement, or s-class; DOES")
print("      touch the eventual J(omega) magnitude comparison). Must be fixed at")
print("      ASSEMBLY-2 entry.")
e1_ok = e1a and e1b

print("\n=== E2: CTP SIGN PIN, SYMBOLIC (theta algebra; largest-time identity) ===")
F, Ft, th = sp.symbols('F Ftilde theta', positive=True)   # F = F_xy, Ftilde = F_yx
thb = 1 - th
Gpp, Gpm, Gmp, Gmm = th*F + thb*Ft, Ft, F, thb*F + th*Ft
S = {'++': Gpp**2, '+-': Gpm**2, '-+': Gmp**2, '--': Gmm**2}
# theta idempotence: theta^2 = theta (a step function). REVIEWER SELF-CATCH (disclosed):
# a naive subs(th**2, th) on a positive symbol ALSO rewrites bare th as sqrt(th) (sympy
# matches th = (th^2)^(1/2)) and silently corrupted the first run's E2 -- caught by the
# gate itself, diagnosed before reporting. Replace EXACT squares only:
idem = lambda e: sp.expand(e).replace(
    lambda x: x.is_Pow and x.base == th and x.exp == 2, lambda x: th)
row = idem(S['++'] - S['+-'])
e2a = sp.simplify(row - th*(F**2 - Ft**2)) == 0
trace = idem(S['++'] - S['+-'] - S['-+'] + S['--'])
e2b = sp.simplify(trace) == 0
# signed components: Sigma_ab = eta_a eta_b S_ab
Sig = {'++': S['++'], '+-': -S['+-'], '-+': -S['-+'], '--': S['--']}
signed_correct = idem(Sig['++'] + Sig['+-'])
e2c = sp.simplify(signed_correct - th*(F**2 - Ft**2)) == 0
signed_label = idem(Sig['++'] - Sig['+-'])
at_tneg = sp.simplify(signed_label.subs(th, 0))            # t < t': must be 0 if retarded
e2d = at_tneg != 0
print(f"   S_++ - S_+- == theta (F^2 - Ftilde^2)  [retarded support, exact] : {e2a}")
print(f"   trace mix c=(1,-1) == 0 IDENTICALLY (largest-time identity)      : {e2b}")
print(f"   SIGNED Sigma_++ + Sigma_+- == theta (F^2 - Ftilde^2)             : {e2c}")
print(f"   the LITERAL label 'Sigma_++ - Sigma_+-' on signed components at")
print(f"   t < t' equals {at_tneg} != 0 -- NOT retarded (the landmine, pinned): {e2d}")
print("   => the instrument's NUMERIC Gate 3 tested the correct (unsigned) object; its")
print("      LABEL is wrong for its own signed Step-3 components. ASSEMBLY-2 must")
print("      implement Sigma_R = Sigma_++ + Sigma_+- (signed) == S_++ - S_+- (unsigned).")
print("      The disclosed trace-annihilation is the largest-time identity -- confirmed.")
e2_ok = e2a and e2b and e2c and e2d

print("\n=== E3: k = 0 DEGENERACY vs k != 0 SPAN GROWTH (placement lives at k != 0) ===")
ETA = sp.diag(1, -1, -1, -1)
def channels_at(K):
    Kl = [ETA[i, i]*K[i] for i in range(4)]
    K2 = sum(K[i]*Kl[i] for i in range(4))
    th_ = sp.Matrix(4, 4, lambda i, j: ETA[i, j] - Kl[i]*Kl[j]/K2)
    om_ = sp.Matrix(4, 4, lambda i, j: Kl[i]*Kl[j]/K2)
    K4 = lambda f: {(m, n, r, s): f(m, n, r, s) for m in range(4) for n in range(4)
                    for r in range(4) for s in range(4)}
    return dict(
        P2=K4(lambda m, n, r, s: (th_[m, r]*th_[n, s] + th_[m, s]*th_[n, r])/2 - th_[m, n]*th_[r, s]/3),
        P1=K4(lambda m, n, r, s: (th_[m, r]*om_[n, s] + th_[m, s]*om_[n, r]
                                  + th_[n, r]*om_[m, s] + th_[n, s]*om_[m, r])/2),
        P0s=K4(lambda m, n, r, s: th_[m, n]*th_[r, s]/3),
        P0w=K4(lambda m, n, r, s: om_[m, n]*om_[r, s]),
        Xsw=K4(lambda m, n, r, s: th_[m, n]*om_[r, s]),
        Xws=K4(lambda m, n, r, s: om_[m, n]*th_[r, s]))
def vec(S4):
    return sp.Matrix([S4[(m, n, r, s)] for m in range(4) for n in range(4)
                      for r in range(4) for s in range(4)])
u = [sp.Integer(1), 0, 0, 0]                       # medium/bath rest frame
ul = [ETA[i, i]*u[i] for i in range(4)]
def u_structs():
    uu = {(m, n): ul[m]*ul[n] for m in range(4) for n in range(4)}
    K4 = lambda f: {(m, n, r, s): f(m, n, r, s) for m in range(4) for n in range(4)
                    for r in range(4) for s in range(4)}
    return [K4(lambda m, n, r, s: uu[(m, n)]*uu[(r, s)]),
            K4(lambda m, n, r, s: uu[(m, n)]*ETA[r, s]),
            K4(lambda m, n, r, s: ETA[m, n]*uu[(r, s)])]
for (Kv, label) in ([(sp.Integer(5), 0, 0, 0)], 'k = 0')  if False else \
                   [([sp.Integer(5), 0, 0, sp.Integer(0)], 'k = 0'),
                    ([sp.Integer(5), 0, 0, sp.Integer(2)], 'k = 2')]:
    CH = channels_at(Kv)
    base = sp.Matrix.hstack(*[vec(S4) for S4 in CH.values()])
    r0 = base.rank()
    withu = sp.Matrix.hstack(base, *[vec(S4) for S4 in u_structs()])
    r1 = withu.rank()
    print(f"   K = {Kv} ({label}): rank(six channels) = {r0}; rank(+ u-structures) = {r1}")
    if label == 'k = 0':
        e3a = (r1 == r0)
    else:
        e3b = (r1 > r0)
print(f"   at k = 0 the u-structures ADD NOTHING (u parallel K: closure guaranteed)   : {e3a}")
print(f"   at k != 0 the span STRICTLY GROWS (placement is a real question only there): {e3b}")
print("   => ASSEMBLY-1's six-channel closure at the rest-frame configuration is")
print("      kinematics, not physics; it must never be cited as Q1 placement evidence.")
print("      Q1 runs at k != 0, where medium-frame (u) structures can genuinely appear")
print("      -- their appearance IS the 'outside the 3D family' outcome the blind allows.")
e3_ok = e3a and e3b

ALL = {"E1_wick_half_refutes_net1": bool(e1_ok),
       "E2_ctp_sign_pin_and_largest_time": bool(e2_ok),
       "E3_k0_degeneracy_kneq0_growth": bool(e3_ok)}
ok = all(ALL.values())
print(f"\nSECOND-AUTHOR VERDICT: {'ALL EXPECTATIONS MET' if ok else 'BREAK -- see gates'}")
print(json.dumps(ALL, indent=1))
json.dump({"instrument": "second_author_assembly1.py", "reviews": "wall_a_assembly1.py",
           "expectations": ALL, "all_pass": bool(ok),
           "findings": [
               "F-A1-1 (NORMALISATION, load-bearing for magnitudes): the Step-3 net factor is "
               "1/2, not 1 -- exact zero-dimensional Gaussian gives Sigma = (1/2) Gamma^2 G^2; "
               "with the full d^4l integral the l <-> K-l exchange double-counts. Fix at "
               "ASSEMBLY-2 entry; support/placement/s-class untouched.",
               "F-A1-2 (SIGN PIN, load-bearing for causality downstream): numeric Gate 3 tested "
               "the correct UNSIGNED row S_++ - S_+-; the label is wrong for the signed Step-3 "
               "components: Sigma_R = Sigma_++ + Sigma_+- (signed). Implementing the literal "
               "label on signed components yields a NON-retarded object (2 Ftilde^2 at t<t'). "
               "Trace-mix annihilation confirmed as the largest-time identity.",
               "F-A1-3 (SCOPE, blind-hygiene): six-channel closure at k = 0 is kinematically "
               "guaranteed (u parallel K); Q1 placement content exists only at k != 0 (span "
               "growth exhibited: rank +3 with u-structures). The rest-frame closure must not "
               "be cited as placement evidence.",
           ]},
          open(os.path.join(HERE, "SECOND_AUTHOR_ASSEMBLY1_VERDICT.json"), "w"), indent=2)
print("verdict written: SECOND_AUTHOR_ASSEMBLY1_VERDICT.json")
sys.exit(0 if ok else 1)
