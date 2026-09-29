# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S8: L4 'exclusion, never inclusion' -- is it a property of the chosen definition only?
Alternative, equally seedless, covariant definition using the compressed operator systems themselves:
   x ~'_rho z  iff  exists A in A_x, B in A_z with  [P A P, [P H P, P B P]] != 0.
Chain x=0 - y=1 - z=2 with NO x-z coupling.  Scan all eigen-subsets P."""
import itertools
import numpy as np
from common import *

n, d = 3, 8
rng = np.random.default_rng(5)
H = (site_op(X, 0, n) @ site_op(X, 1, n) + 0.8 * site_op(Y, 1, n) @ site_op(Y, 2, n)
     + 0.37 * site_op(Z, 0, n) + 0.61 * site_op(Z, 1, n) + 0.23 * site_op(Z, 2, n) + 0.3 * site_op(X, 1, n))
print("Gamma edge x-z (uncompressed):", edge_strength(H, np.eye(d), 0, 2, n))
w, U = np.linalg.eigh(H)
best = (0, None)
for r in range(2, d):
    for S in itertools.combinations(range(d), r):
        Q = U[:, list(S)]; P = Q @ Q.conj().T
        m = 0
        for a in PAULI:
            PA = P @ site_op(a, 0, n) @ P
            for b in PAULI:
                PB = P @ site_op(b, 2, n) @ P
                m = max(m, np.linalg.norm(comm(PA, comm(P @ H @ P, PB))))
        if m > best[0]:
            best = (m, S)
print("max over sectors of compressed-definition x-z edge:", best)
# also: Gamma(rho) monotone in P, but NOT monotone under state change: find P1, P2 incomparable with edge in one only
P_frozen = kron((I2 + Z) / 2, I2, I2)
H2 = site_op(Z, 0, n) @ site_op(Z, 1, n) + 0.7 * site_op(X, 1, n)
Pk, _ = krylov_projector(H2, P_frozen @ rng.normal(size=(d, 4)))
Pflip = kron((I2 - Z) / 2, I2, I2)
Pmix = np.eye(d)
print("edge x-y: rho in Zx=+1 sector:", f"{edge_strength(H2, Pk, 0, 1, n):.1e}",
      "| after local rotation of x making rho faithful:", round(edge_strength(H2, Pmix, 0, 1, n), 3))
