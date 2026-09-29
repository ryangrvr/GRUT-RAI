# Rank-drop theorem proof support: ABSTRACT symbolic check (arbitrary on-site nonlinearity); not a physics member.
# Abstract check (mathematics, not a physics member): end-site output on a path with
# ARBITRARY on-site nonlinearities g_k and arbitrary diagonal d_k, couplings w_k.
import sympy as sp
for N in (3, 4, 5):
    x = sp.symbols(f'x1:{N+1}'); w = sp.symbols(f'w1:{N}'); d = sp.symbols(f'd1:{N+1}')
    g = [sp.Function(f'g{k+1}') for k in range(N)]
    f = []
    for k in range(N):
        e = -d[k]*x[k] - g[k](x[k])
        if k > 0: e += w[k-1]*x[k-1]
        if k < N-1: e += w[k]*x[k+1]
        f.append(e)
    phi = [x[0]]
    for j in range(1, N):
        prev = phi[-1]
        phi.append(sp.expand(sum(sp.diff(prev, x[k])*f[k] for k in range(N))))
    J = sp.Matrix([[sp.diff(p, xi) for xi in x] for p in phi])
    upper_zero = all(sp.simplify(J[i, j]) == 0 for i in range(N) for j in range(i+1, N))
    diag = [sp.simplify(J[i, i]) for i in range(N)]
    print(N, "lower-triangular:", upper_zero, "diag:", diag, "det:", sp.factor(sp.prod(diag)))
