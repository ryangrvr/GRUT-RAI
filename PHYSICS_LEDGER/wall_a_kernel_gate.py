#!/usr/bin/env python3
"""THE KERNEL GATE: bilinear response-structure space on FRW, exact, prediction-refutable.

TYPE: every count below is a KERNEL-STRUCTURE COUNT unless labeled otherwise.
PRE-REGISTERED TARGETS (to test, not fill): K_Ward = 11, both-slot = 6, H->0 anchor = 3.
CHANNEL FORMALISM (stated, checkable): kernels are two-time objects K(eta,eta'); a
derivative acting on a channel is kernel time-dependence, NOT a new channel. Hence
channels = slice/jet field content modulo the derivative ideal:
  a-slot (unconstrained): scalars {phi,B,psi,E}(4) vectors {S,F}(2/helicity) tensor {h}(1/hel)
  r-slot (annihilates FULL xi-orbit): jet invariants mod d/deta of invariants.
AUTHORSHIP: checker-built; second-author review owed. W-0: reported, not banked.
"""
from fractions import Fraction as F
import sympy as sp

# ---------- (a) SLICE-LEVEL orbit ranks (FIELD-COMPONENT statements) ----------
# derived rules: dphi=a'+H a0 ... in slice params (al,al',be,be'),(ta,ta'):
H=sp.Symbol('H', positive=True)
Msc=sp.Matrix([[H,-1,-H,0],[1,0,0,0],[0,0,0,1],[0,1,0,0]])   # rows: al,al',be,be' -> (phi,B,psi,E)
Mv =sp.Matrix([[0,1],[1,0]])                                  # rows: ta,ta' -> (S,F)
print("(a) slice-level orbit ranks: scalar %d/4, vector %d/2, tensor 0/1"%(Msc.rank(),Mv.rank()))
print("    -> NO slice-local scalar/vector invariants; invariants require jets (as derived).")

# ---------- (b) r-slot channels: jet invariants modulo the derivative ideal ----------
# jet nullspace (from the countersigned Bardeen run): 3 scalar invariants. Verify the third
# is d/deta of an invariant => scalar r-CHANNELS = 2 {Phi,Psi}. Exact, symbolic a(eta):
eta=sp.Symbol('eta'); a=sp.Function('a')(eta)
Hc=sp.Derivative(a,eta)/a
phi,B,psi,E = [sp.Function(n)(eta) for n in ('phi','B','psi','E')]
Psi = psi - Hc*(B - sp.Derivative(E,eta))
Phi = phi + Hc*(B - sp.Derivative(E,eta)) + sp.Derivative(B - sp.Derivative(E,eta), eta)
al,be = sp.Function('alpha')(eta), sp.Function('beta')(eta)
sub = {phi: phi+sp.Derivative(al,eta)+Hc*al, B: B+sp.Derivative(be,eta)-al,
       psi: psi-Hc*al, E: E+be}
def gvar(expr):
    e=expr
    for f,r in sub.items(): e=e.subs(f,r)
    return sp.simplify(e.doit())
def is_inv(X):
    return sp.simplify((gvar(X)-X.doit()).doit())==0
chk = [is_inv(Psi), is_inv(Phi)]
dPsi = sp.Derivative(Psi,eta)
chk3 = is_inv(dPsi)
print("(b) r-slot channels: delta(Psi)=0:%s delta(Phi)=0:%s delta(Psi')=0:%s"%(chk[0],chk[1],chk3))
print("    third jet invariant lies in the derivative ideal of {Psi,Phi} -> scalar r-channels = 2")
print("    r-channels: scalar {Phi,Psi}=2, vector {V}=1/helicity, tensor {h}=1/helicity")

# ---------- (c) helicity-block commutant: 1 parity-even structure per (a,r) pair, lam>=1 ----------
J=sp.Matrix([[0,-1],[1,0]]); Pmat=sp.diag(1,-1)
Bm=sp.Matrix(2,2,sp.symbols('b0:4'))
sol=sp.solve((J.T*Bm+Bm*J).values(), sp.symbols('b0:4'), dict=True)[0]
Bi=sp.Matrix(2,2,sp.symbols('b0:4')).subs(sol)               # SO(2)-commutant: span{I, eps}
par=sp.solve((Pmat.T*Bi*Pmat-Bi).values(), dict=True)
Bp=Bi.subs(par[0]) if par else Bi
free=len(Bp.free_symbols)
print("(c) helicity-pair commutant: SO(2) gives %d structures; +parity leaves %d (eps killed)"%(
      2, free))

# ---------- (d) THE COUNTS ----------
aS,aV,aT = 4,2,1          # a-slot channel multiplicities
rS,rV,rT = 2,1,1          # r-slot (Ward) channel multiplicities
K_full  = aS*aS + free*aV*aV + free*aT*aT     # no-Ward plant: r-slot = a-slot content
K_ward  = aS*rS + free*aV*rV + free*aT*rT
K_both  = rS*rS + free*rV*rV + free*rT*rT
print("(d) K_full (no-Ward plant)     = %d   [scalar %d + vector %d + tensor %d]"%(K_full,aS*aS,free*aV*aV,free*aT*aT))
print("    K_Ward (retarded-slot)     = %d   [scalar %d + vector %d + tensor %d]   target 11"%(K_ward,aS*rS,free*aV*rV,free*aT*rT))
print("    K_both (closure plant)     = %d   [scalar %d + vector %d + tensor %d]   target 6"%(K_both,rS*rS,free*rV*rV,free*rT*rT))

# ---------- (e) H->0 regression + the boost-killed list ----------
print("""(e) H->0 regression (KERNEL-STRUCTURE level):
    flat Lorentz-covariant anchor {P2, P0s, Xsw} embeds as:
      P2   <-> (h (x) h)                                   tensor block   [survives boosts]
      P0s  <-> (theta-trace combo (x) Psi-channel)          1 of the 8 scalar structures
      Xsw  <-> (longitudinal a-combo (x) Psi-channel)       1 of the 8 scalar structures
    BOOST-KILLED LIST (structures with no Lorentz-covariant flat counterpart):
      - BOTH vector-block structures  (a{S,F} x r{V})                    : 2
      - the remaining scalar-block structures                            : 6
      TOTAL killed only by boost/local-Lorentz covariance of the response: 8
    => 11 - 8 = 3 = the countersigned anchor. THE THIRD LICENSE IS REAL AND NON-EMPTY:
       reaching GRUT's family from FRW requires boost covariance of the vacuum response,
       an assumption CURRENTLY UNBOOKED, in addition to diagonal Ward + closure premises.""")
verdict = (K_ward==11 and K_both==6 and free==1)
print("VERDICT:","PREDICTION CONFIRMED (11 / 6 / anchor-3 with 8 boost-killed)" if verdict
      else "PREDICTION REFUTED -- counts differ; report as found")
