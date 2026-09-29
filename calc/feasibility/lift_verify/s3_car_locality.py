# Lift-selection verification: ABSTRACT mathematics on 1-3 modes (proof support); not a physics member.
"""V-6 / D-5 readiness proof support (abstract mathematics; 3 sites, Jordan-Wigner).
(a) odd generators at disjoint sites anticommute; even elements of site-set A commute with everything at disjoint B.
(b) real Clifford (Majorana) fields: symmetric quadratic forms sum P_ij g_i g_j are scalars (tr P).
(c) JW images: even local fermion operators on contiguous sets are local spin operators; odd ones carry strings."""
import numpy as np, itertools
I2 = np.eye(2); Z = np.diag([1., -1.]); X = np.array([[0., 1.], [1., 0.]]); Y = np.array([[0, -1j], [1j, 0]])
sm = np.array([[0., 1.], [0., 0.]])
def kron(*m):
    out = np.array([[1.]])
    for a in m: out = np.kron(out, a)
    return out
N = 3
a = [kron(*([Z]*i + [sm] + [I2]*(N-i-1))) for i in range(N)]
ad = [m.conj().T for m in a]
anti = lambda A, B: A@B + B@A; comm = lambda A, B: A@B - B@A
print('(a) {a0,a2}=0:', np.allclose(anti(a[0], a[2]), 0), ' {a0,a2^dag}=0:', np.allclose(anti(a[0], ad[2]), 0),
      ' [a0,a2]!=0:', not np.allclose(comm(a[0], a[2]), 0))
even0 = [ad[0]@a[0], a[0]+ad[0]@a[0]@a[0]]  # second is odd actually; filter by parity below
P = kron(*([Z]*N))
def parity(Op): return 'even' if np.allclose(P@Op@P, Op) else ('odd' if np.allclose(P@Op@P, -Op) else 'mixed')
A_ops = [ad[0]@a[0], ad[0]@a[1] + ad[1]@a[0], a[0]@a[1]]           # even, region {0,1}
B_ops = [a[2], ad[2], ad[2]@a[2]]                                  # odd/odd/even, region {2}
print('    parities A:', [parity(o) for o in A_ops], ' B:', [parity(o) for o in B_ops])
print('    even(A) commutes with all B:', all(np.allclose(comm(u, v), 0) for u in A_ops for v in B_ops))
g = []
for i in range(N):
    g += [a[i] + ad[i], -1j*(a[i] - ad[i])]  # 2N Majoranas; real Clifford over R^{2N}
print('(b) Majorana {g_i,g_j} = 2 delta:', all(np.allclose(anti(g[i], g[j]), 2*np.eye(2**N)*(i == j)) for i in range(2*N) for j in range(2*N)))
rng = np.random.default_rng(1); S = rng.normal(size=(2*N, 2*N)); S = S + S.T
Q = sum(S[i, j]*g[i]@g[j] for i in range(2*N) for j in range(2*N))
print('    symmetric form sum S_ij g_i g_j == tr(S)*1 :', np.allclose(Q, np.trace(S)*np.eye(2**N)))
# (c) JW: a0^dag a1 + h.c. (even, contiguous) is local: equals (X0 X1 + Y0 Y1)/2 up to sign; odd a2 carries Z0 Z1 string
hop = ad[0]@a[1] + ad[1]@a[0]
print('(c) even hop(0,1) == -(X0X1+Y0Y1)/2 or +:', np.allclose(hop, (kron(X, X, I2)+kron(Y, Y, I2))/2) or np.allclose(hop, -(kron(X, X, I2)+kron(Y, Y, I2))/2))
print('    odd a2 acts nontrivially on sites 0,1 (string):', not np.allclose(a[2], kron(I2, I2, sm)))
# (d) odd readout: in any parity-even state rho, <g_0> = 0
rho = np.diag(rng.random(2**N)); rho /= rho.trace()   # diagonal in occupation basis -> commutes with P
print('(d) even state, <Majorana g0> =', np.trace(rho@g[0]).real)
