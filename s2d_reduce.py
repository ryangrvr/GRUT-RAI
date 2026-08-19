import sympy as sp
t,r=sp.symbols('t r'); H=sp.symbols('H',positive=True); l=sp.symbols('l',positive=True)
f=1-H**2*r**2
psi=sp.Function('psi')(t,r); h0=sp.Function('h0')(t,r)
LL=l*(l+1)
# substitution h1 = r*psi/f  , and  d_t h0 = f * d_r ( f*h1 )   [eq (I)]
h1 = r*psi/f
dth0 = sp.simplify(f*sp.diff(f*h1, r))
# eq (II):  d_t[ d_r h0 - (2/r) h0 ] - d_tt h1 - (L-2) f h1/r^2 = 0
eqII = sp.diff(dth0, r) - (2/r)*dth0 - sp.diff(h1,t,2) - (LL-2)*f*h1/r**2
eqII = sp.simplify(sp.expand(sp.simplify(eqII)))
print("eq(II) after substitution (should be  -(1/(f/r))*[master]):")
# multiply by f/r
M = sp.simplify(sp.expand(sp.simplify(eqII*f/r)))
M = sp.collect(sp.expand(M), [sp.Derivative(psi,(r,2)), sp.Derivative(psi,r), sp.Derivative(psi,(t,2)), psi])
print(); sp.pprint(M)
# now compare with  psi_{r*r*} - psi_tt - V psi   where d_r* = f d_r
V = sp.symbols('V')
target = f*sp.diff(f*sp.diff(psi,r),r) - sp.diff(psi,t,2) - V*psi
diff = sp.simplify(sp.expand(M - target))
Vsol = sp.solve(sp.Eq(diff,0), V)
print("\n=> V(r) =", sp.simplify(sp.factor(Vsol[0])))
print("   compare f*l(l+1)/r^2 :", sp.simplify(Vsol[0] - f*LL/r**2)==0)
# tortoise form
u=sp.symbols('u',positive=True)
Vu = sp.simplify(Vsol[0].subs(r, sp.tanh(u)/H))
print("\n   in tortoise u = H r_* with H r = tanh(u):  V =", sp.simplify(sp.expand_trig(sp.simplify(Vu))))
