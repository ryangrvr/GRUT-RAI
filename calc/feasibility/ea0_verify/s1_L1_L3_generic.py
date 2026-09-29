# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S1: L1 spectral formula == Krylov/cyclic projector; L3; and the owner's question:
for GENERIC H, do states with P_rho != I (any subset S of eigenvectors, incl. rank 1)
still have Gamma(rho) == Gamma?  Checked for (a) full Herm(4), Herm(8); (b) random
nearest-neighbour 2-local 3-qubit chains (a local family)."""
import itertools
import numpy as np
from common import *

rng = np.random.default_rng(1)

# --- L1: spectral form vs Krylov, with a degenerate H and a mixed rho of rank 2
n = 3; d = 8
H = rand_herm(d, rng)
w, U = np.linalg.eigh(H)
# force a 2-fold degeneracy to test the E_lambda formula properly
w[1] = w[0]; H = U @ np.diag(w) @ U.conj().T
V = rng.normal(size=(d, 2)) + 1j * rng.normal(size=(d, 2))   # supp rho (rank 2)
Pk, rk = krylov_projector(H, V)
# spectral form: sum over distinct eigenvalues of proj onto span(E_lam V)
Ps = np.zeros((d, d), complex)
for lam in np.unique(np.round(w, 12)):
    E = U[:, np.abs(w - lam) < 1e-9]; E = E @ E.conj().T
    M = E @ V
    Uq, s, _ = np.linalg.svd(M); r = int(np.sum(s > 1e-10)); Q = Uq[:, :r]
    Ps += Q @ Q.conj().T
print("L1 spectral-vs-Krylov diff:", np.linalg.norm(Pk - Ps), "rank", rk, " [P,H]=", np.linalg.norm(comm(Pk, H)))
# covariance
Wu = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))[0]
Pk2, _ = krylov_projector(Wu @ H @ Wu.conj().T, Wu @ V)
print("L1 covariance diff:", np.linalg.norm(Pk2 - Wu @ Pk @ Wu.conj().T))


def min_edge_over_subsets(H, n, x, y):
    d = 2 ** n
    w, U = np.linalg.eigh(H)
    worst = np.inf; worst_S = None
    for r in range(1, d):
        for S in itertools.combinations(range(d), r):
            Q = U[:, list(S)]; P = Q @ Q.conj().T
            e = edge_strength(H, P, x, y, n)
            if e < worst:
                worst, worst_S = e, S
    return worst, worst_S, edge_strength(H, np.eye(d), x, y, n)

# --- generic full Herm(4) (2 qubits) and Herm(8) (3 qubits, x=0,y=1)
for n in (2, 3):
    mins = []
    for trial in range(5 if n == 3 else 20):
        H = rand_herm(2 ** n, rng)
        m, S, full = min_edge_over_subsets(H, n, 0, 1)
        mins.append(m)
    print(f"full Herm({2**n}): min over trials & all eigen-subsets of edge strength = {min(mins):.3e}")

# --- local family: random nearest-neighbour 2-local chain 0-1-2; edges (0,1) present, (0,2) absent
def rand_nn_chain(n, rng):
    H = np.zeros((2 ** n, 2 ** n), complex)
    for s in range(n):
        for a in PAULI:
            H += rng.normal() * site_op(a, s, n)
    for s in range(n - 1):
        for a in PAULI:
            for b in PAULI:
                H += rng.normal() * site_op(a, s, n) @ site_op(b, s + 1, n)
    return H

mins = []
for trial in range(5):
    H = rand_nn_chain(3, rng)
    m, S, full = min_edge_over_subsets(H, 3, 0, 1)
    mins.append(m)
    e02 = edge_strength(H, np.eye(8), 0, 2, 3)
print(f"random NN 3-chain: min edge(0,1) over all eigen-subsets = {min(mins):.3e};  Gamma edge(0,2) = {e02:.1e}")
print("nondegeneracy check (min eigen gap, last NN chain):", np.min(np.diff(np.linalg.eigvalsh(H))))
