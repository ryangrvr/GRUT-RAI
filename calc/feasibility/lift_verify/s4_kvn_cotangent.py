# Lift-selection verification: ABSTRACT mathematics on 1-3 modes (proof support); not a physics member.
"""V-1/V-5 proof support (abstract mathematics, 1 degree of freedom, symbolic).
(a) KvN Liouvillian L = -i(f d/dx + f'/2) equals the symmetric (Weyl) quantization (1/2)(f P + P f), P = -i d/dx,
    of the cotangent-lift Hamiltonian H = p f(x); Heisenberg derivative of any multiplication operator g(x) is exactly f g'.
(b) Cotangent lift: xdot = f(x) (x-sector autonomous), pdot = -f'(x) p.
(c) Ordering ambiguity for a nonlinear readout under an eps-family: x^3 vs Wick :x^3: = x^3 - 3 eps x share eps->0 limit."""
import sympy as sp
x, k, b, eps = sp.symbols('x k beta epsilon', real=True)
psi = sp.Function('psi')(x); g = sp.Function('g')(x)
f = -k*x - 4*b*x**3
Pop = lambda u: -sp.I*sp.diff(u, x)
L = lambda u: -sp.I*(f*sp.diff(u, x) + sp.diff(f, x)*u/2)
weyl = lambda u: (f*Pop(u) + Pop(f*u))/2
print('(a) L == (fP+Pf)/2 :', sp.simplify(L(psi) - weyl(psi)) == 0)
heis = sp.simplify(sp.I*(L(g*psi) - g*L(psi)))   # i[L, g] psi
print('    i[L,g] psi == f g\' psi :', sp.simplify(heis - f*sp.diff(g, x)*psi) == 0)
p = sp.symbols('p', real=True); H = p*f
print('(b) xdot = dH/dp =', sp.diff(H, p), ';  pdot = -dH/dx =', sp.expand(-sp.diff(H, x)))
print('(c) :x^3: - x^3 =', -3*eps*x, ' -> vanishes as eps->0; two generators f_1 = -kx-4b x^3, f_2 = -kx-4b(x^3-3 eps x) differ at eps>0')
