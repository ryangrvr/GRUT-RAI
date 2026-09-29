# Lift-selection verification: ABSTRACT mathematics on 1-3 modes (proof support); not a physics member.
"""V-2 proof support (abstract mathematics only; 2-3 modes).
(a) Koopman generator on polynomials of degree 2 vs boson Sym^2 vs fermion Lambda^2 spectra; resonance counterexamples.
(b) Wick: <n1 n2> for gauge-invariant quasi-free (Gaussian) states: boson = C11C22+|C12|^2 (permanent), fermion = det."""
import numpy as np, itertools, sympy as sp

def sums(lam, n, fermi):
    idx = itertools.combinations(range(len(lam)), n) if fermi else itertools.combinations_with_replacement(range(len(lam)), n)
    return sorted(sum(lam[i] for i in c) for c in idx)

# Koopman generator on degree-2 polynomials, symbolic, K upper-triangular non-symmetric with eigenvalues 1,2,3
x = sp.symbols('x1:4')
K = sp.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 3]])
f = -K*sp.Matrix(x)
mons = [x[i]*x[j] for i in range(3) for j in range(i, 3)]
L = sp.zeros(len(mons))
for c, m in enumerate(mons):
    Lm = sp.expand(sum(f[k]*sp.diff(m, x[k]) for k in range(3)))
    P = sp.Poly(Lm, *x)
    for r, m2 in enumerate(mons):
        L[r, c] = P.coeff_monomial(m2)
print('Koopman generator on deg-2 polys, eigenvalues:', sorted(L.eigenvals(multiple=True)))
lam = [1, 2, 3]
print('boson Sym^2 sums  :', sums(lam, 2, False))
print('fermion Lam^2 sums:', sums(lam, 2, True))
print('2*lam_2 = 4 in fermion two-particle sector?', 4 in sums(lam, 2, True), ' (resonance 2l2 = l1+l3)')
print('2*lam_1 = 2 in fermion sectors of any n?', [2 in sums(lam, n, True) for n in range(4)], ' (resonance 2l1 = l2, single-particle)')
lamd = [1, 1, 3]
print('degenerate spectrum (1,1,3): fermion Lam^2 sums', sums(lamd, 2, True), '-> value 2 = 2*lam_1 present with n_k<=1')
print('dims: Sym^2 =', len(sums(lam, 2, False)), ' Lam^2 =', len(sums(lam, 2, True)))

# Wick check: 2 modes, Gaussian gauge-invariant state rho ~ exp(-a^dag H a); boson truncated Fock, fermion exact (JW)
rng = np.random.default_rng(0)
A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); H = A @ A.conj().T + 0.8*np.eye(2)
def boson_ops(d):
    a = np.diag(np.sqrt(np.arange(1, d)), 1); I = np.eye(d)
    return [np.kron(a, I), np.kron(I, a)]
def fermion_ops():
    a = np.array([[0, 1], [0, 0]]); Z = np.diag([1, -1]); I = np.eye(2)
    return [np.kron(a, I), np.kron(Z, a)]
from scipy.linalg import expm
for name, ops in (('boson', boson_ops(40)), ('fermion', fermion_ops())):
    Hop = sum(H[i, j]*ops[i].conj().T @ ops[j] for i in range(2) for j in range(2))
    rho = expm(-Hop); rho /= np.trace(rho)
    C = np.array([[np.trace(rho @ ops[i].conj().T @ ops[j]) for j in range(2)] for i in range(2)])
    n = [o.conj().T @ o for o in ops]
    n1n2 = np.trace(rho @ n[0] @ n[1]).real
    perm = (C[0, 0]*C[1, 1] + C[0, 1]*C[1, 0]).real; det = (C[0, 0]*C[1, 1] - C[0, 1]*C[1, 0]).real
    print(f'{name}: <n1n2>={n1n2:.10f}  perm(C)={perm:.10f}  det(C)={det:.10f}')
