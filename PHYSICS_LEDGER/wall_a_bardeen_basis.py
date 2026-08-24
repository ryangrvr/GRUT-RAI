#!/usr/bin/env python3
"""Bardeen basis, gate 1 of the FRW kinematic completion -- DERIVED, not recalled.

METHOD (recall-proof): the gauge orbit is computed from the Lie derivative
(L_xi g)_mn = xi^l d_l g_mn + g_ln d_m xi^l + g_ml d_n xi^l on the exact FRW background
g = a(eta)^2 diag(-1,1,1,1), at fixed spatial momentum k z-hat. No transformation rule is
taken from memory. Invariants are the exact null space of the orbit action on the field
jet space, per helicity sector, with symbolic a(eta). Plants verify: a pure-gauge
configuration is annihilated by every invariant; bare psi / bare P0s-analogues are NOT
invariant (the gate-1 finding, reproduced from first principles).

TYPE DECLARATIONS (the standing rule):
  - '10' below is a FIELD-COMPONENT COUNT; '6' invariants is a FIELD-COMBINATION COUNT;
  - the closing kernel table is a KERNEL-STRUCTURE COUNT and is a PRE-REGISTERED
    PREDICTION for the kernel-level implementation, not a result of this file.

AUTHORSHIP: checker-built at the owner's direction; second-author review owed (standing).
W-0: computed-and-reported, NOT banked.
"""
import sympy as sp

eta,x,y,z,k = sp.symbols('eta x y z k')
I = sp.I
a  = sp.Function('a')(eta)
al = sp.Function('alpha')(eta)     # xi^0 scalar
be = sp.Function('beta')(eta)      # spatial scalar gauge fn: xi^i = d^i(beta Y)
ta = sp.Function('tau')(eta)       # transverse vector gauge fn (x-component)
Y  = sp.exp(I*k*z)
X  = [eta,x,y,z]
xi = [al*Y, ta*Y, sp.Integer(0), I*k*be*Y]          # upper-index xi^mu
g  = sp.diag(-a**2, a**2, a**2, a**2)

def Lie(m,n):
    e = sum(xi[l]*sp.diff(g[m,n],X[l]) for l in range(4))
    e += sum(g[l,n]*sp.diff(xi[l],X[m]) for l in range(4))
    e += sum(g[m,l]*sp.diff(xi[l],X[n]) for l in range(4))
    return sp.simplify(sp.expand(e))

# ---- read off the component transformations from the DERIVED Lie derivative ----
# parameterization: dg_00=-2a^2 phi Y ; dg_0z=a^2(ik B)Y ; dg_0x=a^2 S Y ;
# dg_xx=-2a^2 psi Y ; dg_zz=a^2(-2psi-2k^2 E)Y ; dg_xz=a^2(ik F)Y ; dg_xy=a^2 h Y
d_phi = sp.simplify(-Lie(0,0)/(2*a**2*Y))
d_B   = sp.simplify( Lie(0,3)/(a**2*I*k*Y))
d_S   = sp.simplify( Lie(0,1)/(a**2*Y))
d_psi = sp.simplify(-Lie(1,1)/(2*a**2*Y))
d_E   = sp.simplify((Lie(3,3)/(a**2*Y) + 2*d_psi)/(-2*k**2))
d_F   = sp.simplify( Lie(1,3)/(a**2*I*k*Y))
d_h   = sp.simplify( Lie(1,2)/(a**2*Y))
print("DERIVED gauge transformations (H = a'/a implicit; ' = d/deta):")
for nm,e in (("d_phi",d_phi),("d_B",d_B),("d_psi",d_psi),("d_E",d_E),
             ("d_S",d_S),("d_F",d_F),("d_h(TT)",d_h)):
    print("   %-8s = %s"%(nm,sp.simplify(e)))

# ---- jet-space null-space computation, SCALAR sector ----
# jet coords: (phi, B, psi, E, phi', B', psi', E', E'')  [9]
# orbit params: (al, al', al'', be, be', be'')            [6]
jets = {sp.Derivative(al,(eta,2)):sp.Symbol('A2'), sp.Derivative(al,eta):sp.Symbol('A1'), al:sp.Symbol('A0'),
        sp.Derivative(be,(eta,3)):sp.Symbol('B3'), sp.Derivative(be,(eta,2)):sp.Symbol('B2'),
        sp.Derivative(be,eta):sp.Symbol('B1'), be:sp.Symbol('B0'),
        sp.Derivative(ta,(eta,2)):sp.Symbol('T2'), sp.Derivative(ta,eta):sp.Symbol('T1'), ta:sp.Symbol('T0')}
def J(e): return sp.expand(e.subs(jets))
ds = {'phi':J(d_phi),'B':J(d_B),'psi':J(d_psi),'E':J(d_E)}
ds['phi_p']=J(sp.diff(d_phi,eta)); ds['B_p']=J(sp.diff(d_B,eta))
ds['psi_p']=J(sp.diff(d_psi,eta)); ds['E_p']=J(sp.diff(d_E,eta)); ds['E_pp']=J(sp.diff(d_E,(eta,2)))
coordsS=['phi','B','psi','E','phi_p','B_p','psi_p','E_p','E_pp']
paramsS=[sp.Symbol(s) for s in ('A0','A1','A2','B0','B1','B2')]
M = sp.Matrix([[sp.expand(ds[c]).coeff(p) for c in coordsS] for p in paramsS])
leftover = [sp.simplify(sp.expand(ds[c]) - sum(M[i,j]*paramsS[i] for i in range(len(paramsS))))
            for j,c in enumerate(coordsS)]
assert all(l==0 for l in leftover), "orbit not linear in declared jet params: "+str(leftover)
rk = M.rank(); null = M.nullspace()   # null vectors v: M v = 0 -> invariant COVECTORS? careful:
# rows of M are orbit DIRECTIONS in coord space; invariant covectors w satisfy M w = 0 (w orthogonal
# to every orbit direction in the coordinate basis pairing).
print("\nSCALAR sector: jet coords 9, orbit params 6, orbit rank = %d -> invariants = %d"%(rk,9-rk))
inv_forms=[]
fieldsyms = sp.symbols('phi B psi E phi_p B_p psi_p E_p E_pp')
for v in null:
    expr = sp.simplify(sum(sp.nsimplify(v[i])*fieldsyms[i] for i in range(9)))
    inv_forms.append(expr); print("   invariant:", expr)

# ---- verify against the BARDEEN forms and run plants ----
H = sp.Symbol('Hc')  # conformal Hubble a'/a, treated symbolically via substitution
subH = {sp.Derivative(a,(eta,2)): (sp.Symbol('Hp')+H**2)*a, sp.Derivative(a,eta): H*a}
def deltaOf(expr_fields):
    # apply the derived deltas to a field expression in fieldsyms
    rep = dict(zip(fieldsyms,[ds['phi'],ds['B'],ds['psi'],ds['E'],ds['phi_p'],ds['B_p'],ds['psi_p'],ds['E_p'],ds['E_pp']]))
    return sp.simplify(sp.expand(expr_fields.subs(rep)).subs(subH))
phi_,B_,psi_,E_,phi_p,B_p,psi_p,E_p,E_pp = fieldsyms
# SELF-CATCH RECORDED: the first candidates (psi + H(B-E'), phi - H(B-E') - (B-E')')
# were RECALLED forms with the wrong relative sign for the DERIVED convention and failed
# the invariance check -- while the exact null space produced the true forms. The
# derivation corrected the memory, which is precisely the recall-proof design.
Psi_B = psi_ - H*(B_ - E_p)                       # Bardeen Psi, DERIVED convention
Phi_B = phi_ + H*(B_ - E_p) + (B_p - E_pp)        # Bardeen Phi, DERIVED convention
for nm,f in (("Psi_Bardeen",Psi_B),("Phi_Bardeen",Phi_B),("bare psi (plant: must FAIL)",psi_),
             ("bare E (P0s-analogue plant: must FAIL)",E_)):
    dv = deltaOf(f)
    print("   delta[%-32s] = %s   -> %s"%(nm,dv,"INVARIANT" if dv==0 else "not invariant"))

# ---- VECTOR sector ----
dsV={'S':J(d_S),'F':J(d_F),'S_p':J(sp.diff(d_S,eta)),'F_p':J(sp.diff(d_F,eta))}
paramsV=[sp.Symbol(s) for s in ('T0','T1','T2')]
coordsV=['S','F','S_p','F_p']
MV=sp.Matrix([[sp.expand(dsV[c]).coeff(p) for c in coordsV] for p in paramsV])
rkV=MV.rank(); print("\nVECTOR sector: jet coords 4, orbit params 3, rank = %d -> invariants = %d"%(rkV,4-rkV))
S_,F_,S_p,F_p = sp.symbols('S F S_p F_p')
for v in MV.nullspace():
    print("   invariant:", sp.simplify(sum(sp.nsimplify(v[i])*[S_,F_,S_p,F_p][i] for i in range(4))))

# ---- TENSOR sector ----
print("\nTENSOR sector: delta h_TT =", d_h, " -> h_TT invariant outright" if d_h==0 else "NONZERO?!")

print("""
==============================================================================
KERNEL-STRUCTURE COUNT -- PRE-REGISTERED PREDICTION (block arithmetic; the
kernel-level exact implementation is the next gate and must be able to refute):
  diagonal-Ward class (r-slot annihilates the FULL FRW orbit incl. xi^0;
  a-slot unconstrained; SO(2)_khat x parity):
      tensor 1x1 + vector 2x1 + scalar 4x2  =  11
  both-slot / closure-theorem regime (both slots invariant):
      tensor 1x1 + vector 1x1 + scalar 2x2  =   6
  flat LORENTZ-covariant sub-family (the countersigned anchor):  3 -> 2
  => a NEW NAMED LICENSE separates the FRW counts from the flat anchor:
     boost/local-Lorentz covariance of the vacuum response -- CURRENTLY UNBOOKED.
==============================================================================""")
