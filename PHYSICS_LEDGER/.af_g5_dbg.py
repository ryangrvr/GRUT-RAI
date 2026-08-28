#!/usr/bin/env python3
"""Debug the G5 route-2 bilinear check: which of the two DiracDelta dd' shift
integrals sympy gets wrong (or fails to simplify)."""
import time

import sympy as sp

t0 = time.time()
uu = sp.Symbol('u', real=True)
u1, u2 = sp.symbols('u1 u2', real=True)
H = sp.Symbol('H', positive=True)
b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
Bmod = b0 + H * b1 * uu + H ** 2 * b2 * uu ** 2
phi = sp.exp(-uu ** 2) * (1 + uu)
psi = sp.exp(-uu ** 2) * (2 - uu + uu ** 2)

var2 = sp.integrate(Bmod * (sp.diff(phi, uu) * psi + phi * sp.diff(psi, uu)),
                    (uu, -sp.oo, sp.oo))
print('[%.1fs] var2 done' % (time.time() - t0))

inA = sp.integrate(phi.subs(uu, u1) * Bmod.subs(uu, u1)
                   * sp.Derivative(sp.DiracDelta(u1 - u2), u1), (u1, -sp.oo, sp.oo))
print('[%.1fs] inA done' % (time.time() - t0))
inB = sp.integrate(Bmod.subs(uu, u2) * psi.subs(uu, u2)
                   * sp.Derivative(sp.DiracDelta(u2 - u1), u2), (u2, -sp.oo, sp.oo))
print('[%.1fs] inB done' % (time.time() - t0))
print('inA =', inA)
print('inB =', inB)
expA = -sp.diff(phi.subs(uu, u2) * Bmod.subs(uu, u2), u2)
expB = -sp.diff(Bmod.subs(uu, u1) * psi.subs(uu, u1), u1)
print('inA == -[phi*B]\'(u2):', sp.simplify(sp.expand(inA - expA)) == 0)
print('inB == -[B*psi]\'(u1):', sp.simplify(sp.expand(inB - expB)) == 0)
print('inA - expA =', sp.simplify(sp.expand(inA - expA)))
print('inB - expB =', sp.simplify(sp.expand(inB - expB)))

tA = sp.integrate(sp.expand(inA * psi.subs(uu, u2)), (u2, -sp.oo, sp.oo))
print('[%.1fs] tA done' % (time.time() - t0))
tB = sp.integrate(sp.expand(inB * phi.subs(uu, u1)), (u1, -sp.oo, sp.oo))
print('[%.1fs] tB done' % (time.time() - t0))
d = sp.expand(tA + tB - var2)
print('tA+tB-var2 (expanded) == 0:', d == 0)
if d != 0:
    print('  diff:', sp.simplify(d))
    print('  numeric check at (b0,b1,b2,H)=(1,2,3,5):',
          float(d.subs({b0: 1, b1: 2, b2: 3, H: 5}).evalf()))
print('elapsed %.1fs' % (time.time() - t0))
