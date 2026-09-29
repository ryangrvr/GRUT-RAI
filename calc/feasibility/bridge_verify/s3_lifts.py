# Access-bridge verification: ABSTRACT mathematics (proof support); not a physics member; no simulation campaign.
"""S3: abstract checks for the lift table.
(a) Koopman-von Neumann (half-density) generator L = f.grad + (1/2) div f on test functions:
    - anti-self-adjointness is standard; here only the commutator structure:
      [M_a,[L,M_b]] = 0 for multiplication ops (first-order generator),
      [lam_i,[L, M_{x_j}]] = -i d_i f_j  (lam_i = -i d/dx_i): the K / J(x) support, no hbar.
(b) Quasi-free Lindblad loss with generator matrix K (PSD), N = 2 modes:
    boson (Fock cutoff 3/mode, 2-particle initial state; loss never raises number, so exact)
    vs fermion (exact 4-dim). One-particle correlation C_ij = <a_i^dag a_j> follows
    e^{-Kt} C e^{-Kt} for BOTH; a two-particle observable differs.
(c) Mehler / Segal: Gamma(T) on L2(gamma) maps He_n -> T^n He_n (N = 1), i.e. the
    real-space bosonic second quantization is a commutative (classical OU) object.
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

# ---------- (a)
x1, x2, b = sp.symbols("x1 x2 b")
X = [x1, x2]
psi = sp.Function("psi")(x1, x2)
f = [-2 * x1 + x2 - 4 * b * x1 ** 3, x1 - 2 * x2 - 4 * b * x2 ** 3]
div = sum(sp.diff(fi, xi) for fi, xi in zip(f, X))


def L(u):
    return sum(fi * sp.diff(u, xi) for fi, xi in zip(f, X)) + sp.Rational(1, 2) * div * u


def M(a):
    return lambda u: a * u


def lam(i):
    return lambda u: -sp.I * sp.diff(u, X[i])


def comm(A, B):
    return lambda u: sp.expand(A(B(u)) - B(A(u)))


a_fun, b_fun = sp.Function("a")(x1), sp.Function("bb")(x2)
dc = sp.simplify(comm(M(a_fun), comm(L, M(b_fun)))(psi))
print("(a) [M_a(x1),[L,M_b(x2)]] psi =", dc)
for i in range(2):
    for j in range(2):
        r = sp.simplify(comm(lam(i), comm(L, M(X[j])))(psi) / psi)
        print(f"(a) [lam_{i+1},[L,x_{j+1}]] = {r}   (-i d_{i+1} f_{j+1} = "
              f"{sp.simplify(-sp.I*sp.diff(f[j], X[i]))})")

# ---------- (b)
K = np.array([[1.3, -0.6], [-0.6, 0.9]])
kap, V = np.linalg.eigh(K)


def lindblad_evolve(a_ops, rho0, t, steps=4000):
    jumps = [np.sqrt(2 * kap[k]) * (V[0, k] * a_ops[0] + V[1, k] * a_ops[1]) for k in range(2)]
    d = rho0.shape[0]
    I = np.eye(d)
    Lsup = np.zeros((d * d, d * d), complex)
    for Lk in jumps:
        LdL = Lk.conj().T @ Lk
        Lsup += np.kron(Lk, Lk.conj()) - 0.5 * np.kron(LdL, I) - 0.5 * np.kron(I, LdL.T)
    vec = expm(Lsup * t) @ rho0.reshape(-1)
    return vec.reshape(d, d)


def corr(rho, a_ops):
    return np.array([[np.trace(rho @ a_ops[i].conj().T @ a_ops[j]) for j in range(2)]
                     for i in range(2)])


# boson
c = 4
a1 = np.diag(np.sqrt(np.arange(1, c)), 1)
Ib = np.eye(c)
A_b = [np.kron(a1, Ib), np.kron(Ib, a1)]
# fermion (Jordan-Wigner)
sm = np.array([[0, 1], [0, 0]])
Z = np.diag([1, -1])
A_f = [np.kron(sm, np.eye(2)), np.kron(Z, sm)]


def state_11(a_ops):
    d = a_ops[0].shape[0]
    vac = np.zeros(d); vac[0] = 1
    v = a_ops[0].conj().T @ a_ops[1].conj().T @ vac
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


t = 0.8
E = expm(-K * t)
for name, A in (("boson", A_b), ("fermion", A_f)):
    rho0 = state_11(A)
    C0 = corr(rho0, A)
    rho = lindblad_evolve(A, rho0, t)
    Ct = corr(rho, A)
    pred = E @ C0.T @ E  # <a_i^dag a_j> transposed convention: C^T evolves as E C^T E
    n1n2 = np.trace(rho @ A[0].conj().T @ A[0] @ A[1].conj().T @ A[1]).real
    print(f"(b) {name}: max|C(t) - E C0 E| = {np.max(np.abs(Ct.T - pred)):.2e}; "
          f"<n1 n2>(t) = {n1n2:.6f}; tr rho = {np.trace(rho).real:.12f}")

# ---------- (c) Mehler
xs, ys, T = sp.symbols("x y T", real=True)
for n in (2, 3, 4):
    He = sp.hermite_prob(n, xs)
    integrand = He.subs(xs, T * xs + sp.sqrt(1 - T ** 2) * ys) * sp.exp(-ys ** 2 / 2) / sp.sqrt(2 * sp.pi)
    val = sp.integrate(sp.expand(integrand), (ys, -sp.oo, sp.oo))
    print(f"(c) Mehler He_{n}: residual =", sp.simplify(val - T ** n * He))
