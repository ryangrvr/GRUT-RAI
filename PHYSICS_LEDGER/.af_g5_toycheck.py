#!/usr/bin/env python3
"""Standalone verification of the REPLACEMENT G5 gate (odd-structure functional
Hessian) before it is wired into wall_d2_phase11_af_basis.py.  Pure sympy; execs
only the fast prefix (engine + toy gates) of the main script -- no machinery."""
import os
import time

src = open('wall_d2_phase11_af_basis.py').read()
pre = src.split('print("\\n=== STEP M:')[0]
ns = {'__name__': '__main__', '__file__': os.path.abspath('wall_d2_phase11_af_basis.py')}
exec(compile(pre, 'prefix', 'exec'), ns)

sp = ns['sp']
uu = ns['uu']
H = ns['H']
om = ns['om']
master = ns['master']
old_kernel_of = ns['old_kernel_of']
Etr = ns['Etr']

t0 = time.time()
print('\n##### STANDALONE NEW-G5 VERIFICATION #####')

b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
Bp = b0 + H * b1 * uu + H ** 2 * b2 * uu ** 2
TAB_B = {(1, 0): Bp, (0, 1): Bp}

# ---- route 3: the generalised master kernel (both placements) ----
kP = sp.expand(master(TAB_B, 'P'))
kE = sp.expand(master(TAB_B, 'E'))
kold = sp.expand(old_kernel_of(TAB_B))
tgt = -sp.diff(Bp, uu).subs(uu, 0)
print('R3 master(P) =', kP)
print('R3 master(E) =', kE)
print('R3 old       =', kold)
print('R3 P==E:', sp.expand(kP - kE) == 0,
      '| P==-Bp(0):', sp.expand(kP - tgt) == 0,
      '| old==0:', kold == 0)


# ---- route 1: direct functional Hessian (Euler-Lagrange; no master formula) ----
def fh_el(Bfun):
    """K(u1,u2) = Sum_{m,n} (-d/du1)^m [ L_{hA_m hB_n}(u1) dd_n(u1-u2) ],
    the derivative acting on the product (product rule, computed term by term)."""
    hAs = [sp.Symbol('hA_%d' % i) for i in range(2)]
    hBs = [sp.Symbol('hB_%d' % i) for i in range(2)]
    L = Bfun * (hAs[1] * hBs[0] + hAs[0] * hBs[1])
    acc = {}
    for m in range(2):
        for n in range(2):
            c = sp.diff(sp.diff(L, hAs[m]), hBs[n])
            if c == 0:
                continue
            dist = {n: c}
            for _ in range(m):
                nd = {}
                for q_, cf in dist.items():
                    nd[q_] = sp.expand(nd.get(q_, 0) + sp.diff(cf, uu))
                    nd[q_ + 1] = sp.expand(nd.get(q_ + 1, 0) + cf)
                dist = dict((k_, v_) for k_, v_ in nd.items() if v_ != 0)
            for q_, cf in dist.items():
                acc[q_] = sp.expand(acc.get(q_, 0) + (-1) ** m * cf)
    return dict((k_, v_) for k_, v_ in acc.items() if v_ != 0)


el = fh_el(Bp)
print('R1 EL kernel slots {dd-order: coef(u)}:', el)
print('R1 == {0: -Bp\'(u)}:', el == {0: -sp.diff(Bp, uu)})

# R1 distributional validation: bilinear form == plain second variation
phi = sp.exp(-uu ** 2) * (1 + uu)
psi = sp.exp(-uu ** 2) * (2 - uu + uu ** 2)
var2 = sp.integrate(Bp * (sp.diff(phi, uu) * psi + phi * sp.diff(psi, uu)),
                    (uu, -sp.oo, sp.oo))
bil1 = sp.integrate(el[0] * phi * psi, (uu, -sp.oo, sp.oo))
phi2 = sp.exp(-uu ** 2) * uu
psi2 = sp.exp(-uu ** 2) * (1 + 3 * uu + uu ** 2)
var2b = sp.integrate(Bp * (sp.diff(phi2, uu) * psi2 + phi2 * sp.diff(psi2, uu)),
                     (uu, -sp.oo, sp.oo))
bil1b = sp.integrate(el[0] * phi2 * psi2, (uu, -sp.oo, sp.oo))
print('R1 bilinear == second variation (2 test pairs):',
      sp.simplify(var2 - bil1) == 0 and sp.simplify(var2b - bil1b) == 0)

# raw-kernel bilinear validation via sympy DiracDelta (K_raw = [B(u1)-B(u2)] dd'(u1-u2))
u1, u2 = sp.symbols('u1 u2', real=True)
try:
    inA = sp.integrate(phi.subs(uu, u1) * Bp.subs(uu, u1)
                       * sp.Derivative(sp.DiracDelta(u1 - u2), u1), (u1, -sp.oo, sp.oo))
    print('R2 raw inner-A probe:', inA)
except Exception as e:
    print('R2 raw inner-A probe EXC:', repr(e)[:120])

# ---- route 2: raw-kernel centre expansion + registered slot/E-transform ----
Dl, uc = sp.symbols('Delta uc', real=True)
diffB = sp.expand(Bp.subs(uu, uc + Dl / 2) - Bp.subs(uu, uc - Dl / 2))
print('R2 centre difference [B(u1)-B(u2)] (odd in Delta):', diffB)
k2 = sp.Integer(0)
for (j,), c in sp.Poly(diffB, Dl).terms():
    k2 = sp.expand(k2 + c * Etr(j, 1))
print('R2 slot-route kernel:', k2)
print("R2 == -B'(uc):", sp.expand(k2 + sp.diff(Bp, uu).subs(uu, uc)) == 0)

# sympy DiracDelta identity probes (for the wired distributional identities)
x = sp.Symbol('x', real=True)
f3 = 3 + 2 * x + x ** 2
print('probe  Int f*dd    :', sp.integrate(f3 * sp.DiracDelta(x), (x, -sp.oo, sp.oo)))
print('probe  Int f*ddp   :', sp.integrate(f3 * sp.Derivative(sp.DiracDelta(x), x), (x, -sp.oo, sp.oo)))
print('probe  Int x*ddp   :', sp.integrate(x * sp.Derivative(sp.DiracDelta(x), x), (x, -sp.oo, sp.oo)))
print('probe  Int x^2*ddp :', sp.integrate(x ** 2 * sp.Derivative(sp.DiracDelta(x), x), (x, -sp.oo, sp.oo)))

# ---- the H-grading statements ----
print('H1 part of corrected (uc=0):', sp.expand(kP.coeff(H, 1)),
      '== -b1*H:', sp.expand(kP.coeff(H, 1) + b1 * H) == 0)
print('H0 corrected==0:', sp.expand(kP.coeff(H, 0)) == 0,
      '| old H0==0:', sp.expand(kold.coeff(H, 0)) == 0,
      '| old H1==0:', sp.expand(kold.coeff(H, 1)) == 0)
TAB_C = {(1, 0): sp.Integer(7), (0, 1): sp.Integer(7)}
kc = sp.expand(master(TAB_C, 'P'))
print('B=const: corrected==0:', kc == 0, '| old==0:', sp.expand(old_kernel_of(TAB_C)) == 0)
kuc = sp.expand(master(TAB_B, 'P', uc=sp.Rational(1, 3)))
print("uc=1/3: K == -B'(1/3):",
      sp.expand(kuc + sp.diff(Bp, uu).subs(uu, sp.Rational(1, 3))) == 0)
print('elapsed %.1fs' % (time.time() - t0))
