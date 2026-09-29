# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""Abstract toy-operator helpers for EA-0 lemma checks (qubits only; no physics members)."""
import numpy as np
from functools import reduce

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [X, Y, Z]


def kron(*ops):
    return reduce(np.kron, ops)


def site_op(op, site, n):
    return kron(*[op if k == site else I2 for k in range(n)])


def comm(a, b):
    return a @ b - b @ a


def edge_strength(H, P, x, y, n):
    """max over Pauli A at x, B at y of ||P [A,[H,B]] P||  (Pauli basis spans traceless part; identity gives 0)."""
    best = 0.0
    for a in PAULI:
        A = site_op(a, x, n)
        for b in PAULI:
            B = site_op(b, y, n)
            C = comm(A, comm(H, B))
            best = max(best, np.linalg.norm(P @ C @ P))
    return best


def krylov_projector(H, V, tol=1e-10):
    """Projector onto span{H^k v : v in columns of V}."""
    n = H.shape[0]
    vecs = [V]
    cur = V
    for _ in range(n):
        cur = H @ cur
        vecs.append(cur)
    M = np.hstack(vecs)
    U, s, _ = np.linalg.svd(M)
    r = int(np.sum(s > tol * max(1.0, s[0])))
    Q = U[:, :r]
    return Q @ Q.conj().T, r


def rand_herm(n, rng):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (A + A.conj().T) / 2


def h_xy_part(H, x, y, n):
    """Component of H with non-trivial support on BOTH x and y (Pauli expansion)."""
    import itertools
    basis = [I2, X, Y, Z]
    out = np.zeros_like(H)
    d = 2 ** n
    for idx in itertools.product(range(4), repeat=n):
        if idx[x] == 0 or idx[y] == 0:
            continue
        O = kron(*[basis[i] for i in idx])
        c = np.trace(O.conj().T @ H) / d
        out += c * O
    return out
