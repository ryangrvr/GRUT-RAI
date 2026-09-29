# Access-bridge verification: ABSTRACT mathematics (proof support); not a physics member; no simulation campaign.
"""S2: symbolic Hermann-Krener / accessibility structure for the L0-1c *class*
(tridiagonal cooperative chain, on-site quartic), small N, symbolic couplings.
f_i = -d_i x_i + w_{i-1} x_{i-1} + w_i x_{i+1} - 4 b x_i^3.
(a) end-site output h = x_1: Jacobian of Phi = (L_f^j h)_{j<N} is lower-triangular with
    constant diagonal prod(w) -> det constant (no rank drop anywhere).
(b) interior-site output h = x_2 (N=3): det of the observability Jacobian; is it
    x-dependent / can it vanish?
(c) nonlinear OUTPUT MAP on the LINEAR flow: h = x_1^2 -> codistribution rank at x=0 is 0.
(d) accessibility with added input g = e_1: rank of {g, ad_f g, ..., ad_f^{N-1} g}.
"""
import sympy as sp


def chain(N):
    x = sp.symbols(f"x1:{N+1}")
    d = sp.symbols(f"d1:{N+1}", positive=True)
    w = sp.symbols(f"w1:{N}", positive=True)
    b = sp.Symbol("b", positive=True)
    f = []
    for i in range(N):
        fi = -d[i] * x[i] - 4 * b * x[i] ** 3
        if i > 0:
            fi += w[i - 1] * x[i - 1]
        if i < N - 1:
            fi += w[i] * x[i + 1]
        f.append(fi)
    return sp.Matrix(x), sp.Matrix(f), w, b, d


def lie(h, f, x):
    return sum(sp.diff(h, xi) * fi for xi, fi in zip(x, f))


def obs_jac(h, f, x, N):
    L = [h]
    for _ in range(N - 1):
        L.append(sp.expand(lie(L[-1], f, x)))
    return sp.Matrix([[sp.diff(Lj, xi) for xi in x] for Lj in L])


for N in (2, 3, 4, 5, 6):
    x, f, w, b, d = chain(N)
    J = obs_jac(x[0], f, x, N)
    upper_zero = all(J[i, j] == 0 for i in range(N) for j in range(i + 1, N))
    diag = [sp.factor(J[i, i]) for i in range(N)]
    det = sp.factor(J.det()) if N <= 4 else sp.prod(diag)
    print(f"(a) N={N}: lower-triangular={upper_zero}; diag={diag}; det={det}")

# (b) interior output, N=3
x, f, w, b, d = chain(3)
J = obs_jac(x[1], f, x, 3)
det = sp.factor(J.det())
print("(b) N=3 interior output x2: det =", det)

# (c) nonlinear output on linear flow (b=0), h = x1^2
x, f, w, b, d = chain(3)
fl = f.subs(b, 0)
J2 = obs_jac(x[0] ** 2, fl, x, 3)
print("(c) h=x1^2 on linear flow: rank at x=0:", J2.subs({xi: 0 for xi in x}).rank(),
      "; generic rank:", J2.subs({x[0]: 1, x[1]: 2, x[2]: 3, w[0]: 1, w[1]: 1,
                                    d[0]: 2, d[1]: 2, d[2]: 1}).rank())

# (d) accessibility with constant input field g = e_1 (the priced probe)
for N in (3, 4, 5):
    x, f, w, b, d = chain(N)
    g = sp.Matrix([1] + [0] * (N - 1))
    cols = [g]
    Df = f.jacobian(x)
    for _ in range(N - 1):
        v = cols[-1]
        br = v.jacobian(x) * f - Df * v        # [f, v] convention
        cols.append(sp.expand(br))
    M = sp.Matrix.hstack(*cols)
    upper = all(M[i, j] == 0 for j in range(N) for i in range(j + 1, N))
    print(f"(d) N={N}: ad_f^j e1 matrix upper-triangular={upper}; diag=",
          [sp.factor(M[i, i]) for i in range(N)])
