# Lift-selection verification: ABSTRACT mathematics on 1-3 modes (proof support); not a physics member.
"""V-3 proof support (abstract mathematics only).
Koopman composition U_T f(x) = f(Tx)  vs  Mehler/OU  P_T f(x) = E f(Tx + sqrt(I-TT^T) y), y~N(0,I).
Checks: (1) 1-mode x^2; (2) P_T = e^{-Lap/2} U_T e^{+Lap/2} on polynomials (2 modes, non-symmetric T);
(3) W x W^-1 = x - d/dx; (4) P_T not multiplicative; (5) OU generator of P_T has Q = K + K^T;
(6) ||U_T||_{L2(gamma)} = T^{-1/2} (1 mode) and |x|^s eigenfunctions in L2(gamma)."""
import sympy as sp, itertools

x, y, t = sp.symbols('x y t', real=True)
T = sp.symbols('T', positive=True)

def gauss_E(expr, var):  # E over var ~ N(0,1) for polynomial expr
    p = sp.Poly(sp.expand(expr), var)
    out = 0
    for (k,), c in p.terms():
        out += c * (0 if k % 2 else sp.factorial2(k - 1) if k > 0 else 1)
    return sp.expand(out)

# (1) one mode, f = x^2
f = x**2
U = f.subs(x, T*x)
P = gauss_E(f.subs(x, T*x + sp.sqrt(1 - T**2)*y), y)
print('(1) U_T x^2 =', U, ' | P_T x^2 =', P, ' | differ by', sp.simplify(P - U))
He2 = x**2 - 1
print('    P_T He2 - T^2 He2 =', sp.simplify(gauss_E((He2).subs(x, T*x+sp.sqrt(1-T**2)*y), y) - T**2*He2),
      '; U_T He2 - T^2 He2 =', sp.simplify(He2.subs(x, T*x) - T**2*He2))

# (2) two modes, non-symmetric contraction T (numeric rational), check P_T = W U_T W^-1, W = exp(-Lap/2)
x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2', real=True)
Tm = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 5)], [0, sp.Rational(3, 5)]])
M = sp.eye(2) - Tm*Tm.T
Lc = M.cholesky()
print('(2) ||T||<1 ?', max(abs(e) for e in (Tm.T*Tm).eigenvals()) < 1)
X = sp.Matrix([x1, x2]); Y = sp.Matrix([y1, y2])

def lap(g):
    return sp.diff(g, x1, 2) + sp.diff(g, x2, 2)

def heat(g, s, order=6):  # exp(s*Lap/2) g on polynomials (terminating series)
    out, term = 0, g
    for n in range(order):
        out += term
        term = sp.expand(s * lap(term) / 2 / (n + 1))
    return sp.expand(out)

def Uop(g):
    Z = Tm*X
    return sp.expand(g.subs({x1: Z[0], x2: Z[1]}, simultaneous=True))

def Pop(g):
    Z = Tm*X + Lc*Y
    h = sp.expand(g.subs({x1: Z[0], x2: Z[1]}, simultaneous=True))
    return gauss_E(gauss_E(h, y1), y2)

ok = True
for a, b in itertools.product(range(4), range(4)):
    if a + b > 4: continue
    g = x1**a * x2**b
    lhs = Pop(g)
    rhs = heat(Uop(heat(g, +1)), -1)
    if sp.simplify(lhs - rhs) != 0:
        ok = False; print('   mismatch', g)
print('    P_T == e^{-Lap/2} U_T e^{+Lap/2} on all monomials deg<=4:', ok)
# (4) P_T not multiplicative
print('(4) P_T(x1^2) - P_T(x1)^2 =', sp.simplify(Pop(x1**2) - Pop(x1)**2), '(=(I-TT^T)_11 =', M[0, 0], ')')
# (3) W x W^-1 = x - d/dx (1 mode)
g = sp.Function('g')
h = x**3 + 2*x
Wm = lambda e: sp.expand(sum(((-sp.Rational(1, 2))**n / sp.factorial(n)) * sp.diff(e, x, 2*n) for n in range(5)))
Wi = lambda e: sp.expand(sum(((sp.Rational(1, 2))**n / sp.factorial(n)) * sp.diff(e, x, 2*n) for n in range(5)))
print('(3) W M_x W^-1 h - (x h - h\') =', sp.simplify(Wm(x*Wi(h)) - (x*h - sp.diff(h, x))))
# (5) OU generator of Mehler: d/dt P_{e^{-Kt}} f at t=0 = -(Kx).grad f + 1/2 tr(Q Hess f), Q = K + K^T
K = sp.Matrix([[1, sp.Rational(2, 3)], [-sp.Rational(1, 3), 2]])  # accretive? check
print('(5) K_s eigen:', [sp.nsimplify(e) for e in ((K + K.T)/2).eigenvals()])
fpoly = x1**2*x2 + x2**3 + x1*x2
Tt = sp.exp(-K*t)
Mt = sp.eye(2) - Tt*Tt.T
# E f(Tx + z), z~N(0,Mt): compute by moment formula via derivative at t=0 of generator
Hs = sp.hessian(fpoly, (x1, x2)); gr = sp.Matrix([sp.diff(fpoly, v) for v in (x1, x2)])
gen_OU = sp.expand((-(K*X)).dot(gr) + sp.Rational(1, 2)*((K + K.T)*Hs).trace())
# direct: dMt/dt at 0 = K + K^T ; d(Tx)/dt at 0 = -Kx ; Gaussian smoothing to first order: 1/2 tr(dM Hess)
dM0 = sp.simplify(sp.diff(Mt, t).subs(t, 0))
print('    dM/dt|0 == K+K^T :', sp.simplify(dM0 - (K + K.T)) == sp.zeros(2))
# (6) L2(gamma) norm of U_T and |x|^s eigenfunctions
import numpy as np
from scipy.integrate import quad
Tv = 0.6
def n2(fun):
    return quad(lambda u: fun(u)**2*np.exp(-u*u/2)/np.sqrt(2*np.pi), -np.inf, np.inf, limit=400)[0]
for s in (-0.4, -0.2, 0.3):
    fun = lambda u, s=s: abs(u)**s
    print(f'(6) s={s}: |x|^s in L2(gamma) norm^2={n2(fun):.4f}; U_T|x|^s = T^s |x|^s, eigenvalue {Tv**s:.4f} (T^-1/2={Tv**-0.5:.4f})')
# norm ratio for narrow gaussian bumps approaching sup density ratio T^{-1}
for w in (0.3, 0.1, 0.03):
    fun = lambda u, w=w: np.exp(-u*u/(4*w*w))
    r = np.sqrt(n2(lambda u: fun(Tv*u))/n2(fun))
    print(f'    ||U_T f||/||f|| for bump width {w}: {r:.4f}  (-> T^-1/2 = {Tv**-0.5:.4f})')
