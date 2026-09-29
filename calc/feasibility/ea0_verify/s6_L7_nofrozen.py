# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S6: among configuration sectors (3 qubits, x=0,y=1,s=2) admitting an edge-removing H with h_xy != 0,
tabulate rank vs 'some site frozen'; inspect the GHZ-pair sector span{|000>,|111>} and verify
P h_xy P for a random admissible H (random combination of the admissible space)."""
import itertools
import numpy as np
from common import *
from s3_L7_random_sector import solve_space, Ops, strings

n, d = 3, 8
names = 'IXYZ'
jointmask = np.array([s[0] != 0 and s[1] != 0 for s in strings])
bits = [tuple((k >> (n - 1 - q)) & 1 for q in range(n)) for k in range(d)]
tab = {}
for r in range(2, d):
    for S in itertools.combinations(range(d), r):
        P = np.diag([1.0 + 0j if k in S else 0 for k in range(d)])
        null = solve_space(P)
        if len(null) == 0 or np.linalg.norm(null[:, jointmask]) < 1e-8:
            continue
        frozen = any(len({bits[k][q] for k in S}) == 1 for q in range(n))
        tab[(r, frozen)] = tab.get((r, frozen), 0) + 1
print("(rank, some site frozen): #removable sectors", dict(sorted(tab.items())))

rng = np.random.default_rng(3)
P = np.diag([1.0 + 0j if k in (0, 7) else 0 for k in range(d)])
null = solve_space(P)
c = null.T @ rng.normal(size=len(null))
H = sum(cc * O for cc, O in zip(c, Ops))
hxy = h_xy_part(H, 0, 1, n)
print("GHZ-pair sector: admissible dim", len(null), " ||h_xy||=", round(np.linalg.norm(hxy), 3),
      " Gamma edge=", round(edge_strength(H, np.eye(d), 0, 1, n), 3), " Gamma(P) edge=", f"{edge_strength(H, P, 0, 1, n):.1e}")
print("  P h_xy P on sector:\n", np.round(P[np.ix_([0, 7], [0, 7])] @ hxy[np.ix_([0, 7], [0, 7])], 3))
print("  P H P on sector:\n", np.round(H[np.ix_([0, 7], [0, 7])], 3))
