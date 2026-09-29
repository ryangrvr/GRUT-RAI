# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S3: Is 'alignment with a local configuration' (L7 (4)) NECESSARY for edge removal?
For a RANDOM subspace P (rank r) of 3 qubits (x=0,y=1,s=2), solve the LINEAR problem
   {H Hermitian : [H,P]=0  and  P[A,[H,B]]P = 0  for all A in A_x, B in A_y}
and ask whether it contains H with h_xy != 0 (so the edge IS in Gamma but NOT in Gamma(P/r)).
Then test whether P is 'aligned' with local structure at x or y: dimension of the local commutant
{a traceless in A_x : [a,P]=0}, and the spectrum of the local reduced support."""
import itertools
import numpy as np
from common import *

n, d, x, y = 3, 8, 0, 1
basis1 = [I2, X, Y, Z]
strings = list(itertools.product(range(4), repeat=n))
Ops = [kron(*[basis1[i] for i in s]) for s in strings]  # 64 Hermitian Pauli strings


def solve_space(P):
    rows = []
    for O in Ops:
        cols = [comm(O, P).ravel()]
        for a in PAULI:
            A = site_op(a, x, n)
            for b in PAULI:
                B = site_op(b, y, n)
                cols.append((P @ comm(A, comm(O, B)) @ P).ravel())
        v = np.concatenate(cols)
        rows.append(np.concatenate([v.real, v.imag]))
    M = np.array(rows).T  # constraints x 64
    _, s, Vt = np.linalg.svd(M)
    null = Vt[np.sum(s > 1e-9):]
    return null  # each row = real Pauli coefficients of an admissible H


def local_commutant_dim(P, site):
    # traceless a at site with [a (x) 1, P] = 0
    M = np.array([comm(site_op(p, site, n), P).ravel() for p in PAULI]).T
    M = np.vstack([M.real, M.imag])
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-9))


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    jointmask = np.array([s[x] != 0 and s[y] != 0 for s in strings])
    for r in (1, 2, 3, 4, 5, 6):
        for trial in range(3):
            Q = np.linalg.qr(rng.normal(size=(d, r)) + 1j * rng.normal(size=(d, r)))[0]
            P = Q @ Q.conj().T
            null = solve_space(P)
            # best admissible H maximizing joint x-y content: take null-space basis restricted to joint coords
            if len(null) == 0:
                print(f"r={r}: empty"); continue
            J = null[:, jointmask]
            u, s, vt = np.linalg.svd(J.T)
            cH = null.T @ vt[0]  # combination with largest joint content
            H = sum(c * O for c, O in zip(cH, Ops))
            hxy = h_xy_part(H, x, y, n)
            print(f"r={r} trial={trial}: dim admissible space={len(null):2d}, max ||h_xy||/||H|| = {np.linalg.norm(hxy)/np.linalg.norm(H):.3f}, "
                  f"Gamma edge={edge_strength(H, np.eye(d), x, y, n):.3f}, Gamma(P) edge={edge_strength(H, P, x, y, n):.1e}, "
                  f"local commutant dims (x,y)=({local_commutant_dim(P, x)},{local_commutant_dim(P, y)}), "
                  f"||P h_xy P||={np.linalg.norm(P@hxy@P):.3f}")
            if r == 3 and trial == 0:
                np.save("s3_example_P.npy", P); np.save("s3_example_H.npy", H)
