# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S9: L5 checks.  (i) {e^{-bH}}' = {H}' for DEGENERATE H too (exp injective);
(ii) C-5 table claim '{rho}' cap A_x = C1 for entangled faithful rho' -- counterexample
rho = rho_{xs} (entangled, full rank) (x) 1_y/2 : faithful, entangled, commutes with all of A_y."""
import numpy as np
from scipy.linalg import expm
from common import *

rng = np.random.default_rng(2)
d = 8
w, U = np.linalg.eigh(rand_herm(d, rng)); w[2] = w[1]; w[5] = w[4] = w[3]
H = U @ np.diag(w) @ U.conj().T

def commutant_dim(M):
    # dim of {A : [A,M]=0} over C
    L = np.kron(M, np.eye(d)) - np.kron(np.eye(d), M.T)
    return int(np.sum(np.linalg.svd(L, compute_uv=False) < 1e-9))

G = expm(-0.9 * H)
L1 = np.kron(H, np.eye(d)) - np.kron(np.eye(d), H.T)
L2 = np.kron(G, np.eye(d)) - np.kron(np.eye(d), G.T)
_, _, V1 = np.linalg.svd(L1); _, _, V2 = np.linalg.svd(L2)
k = commutant_dim(H)
N1 = V1[-k:]; N2 = V2[-commutant_dim(G):]
same = np.linalg.matrix_rank(np.vstack([N1, N2]), tol=1e-8) == k
print("degenerate H: dim{H}'=", k, " dim{e^-bH}'=", commutant_dim(G), " same space:", same)

# (ii)
phi = np.array([1, 0, 0, 1]) / np.sqrt(2)
rxs = 0.8 * np.outer(phi, phi) + 0.2 * np.eye(4) / 4   # entangled (fidelity 0.85>1/2), full rank
# order qubits (x, y, s): build rho = rho_xs (x) 1_y/2 with y in the middle
rho = np.einsum('ab,cd->acbd', rxs.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4), np.eye(2) / 2)
rho = np.kron(rxs, np.eye(2) / 2).reshape([2] * 6)  # (x s y) ordering
rho = rho.transpose(0, 2, 1, 3, 5, 4).reshape(8, 8)  # -> (x y s)
print("min eig rho:", np.linalg.eigvalsh(rho).min(), " ||[rho, sigma_y^a]||:",
      [round(np.linalg.norm(comm(rho, site_op(p, 1, 3))), 12) for p in PAULI])
# partial transpose negativity on x|s to confirm entanglement of rho_xs
pt = rxs.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
print("rho_xs PT min eig (negative => entangled):", np.linalg.eigvalsh(pt).min())
