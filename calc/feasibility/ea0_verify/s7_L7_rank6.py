# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S7: inspect the rank-5/6 configuration sectors (no site frozen) that admit edge removal.
Question: can the admissible H move configurations INSIDE the sector (off-diagonal P H P), and is
P h_xy P then non-scalar / non-zero?  Also: does edge removal persist for a generic admissible H?"""
import itertools
import numpy as np
from common import *
from s3_L7_random_sector import solve_space, Ops, strings

n, d = 3, 8
jointmask = np.array([s[0] != 0 and s[1] != 0 for s in strings])
bits = [tuple((k >> (n - 1 - q)) & 1 for q in range(n)) for k in range(d)]
rng = np.random.default_rng(11)
shown = 0
for r in (6, 5, 4):
    for S in itertools.combinations(range(d), r):
        if any(len({bits[k][q] for k in S}) == 1 for q in range(n)):
            continue
        P = np.diag([1.0 + 0j if k in S else 0 for k in range(d)])
        null = solve_space(P)
        if len(null) == 0 or np.linalg.norm(null[:, jointmask]) < 1e-8:
            continue
        c = null.T @ rng.normal(size=len(null))
        H = sum(cc * O for cc, O in zip(c, Ops))
        hxy = h_xy_part(H, 0, 1, n)
        idx = list(S)
        HP = H[np.ix_(idx, idx)]
        off = np.linalg.norm(HP - np.diag(np.diag(HP)))
        K = hxy[np.ix_(idx, idx)]
        scal = np.linalg.norm(K - np.trace(K) / r * np.eye(r))
        # is P H P irreducible? (connectivity graph of off-diagonal entries)
        A = (np.abs(HP) > 1e-9).astype(int); R = np.linalg.matrix_power(A + np.eye(r, dtype=int), r)
        conn = bool(np.all(R > 0))
        print(f"r={r} S={[bits[k] for k in S]}\n   admissible dim={len(null)}, ||off-diag PHP||={off:.3f} (connected={conn}), "
              f"||P h_xy P - scalar||={scal:.3f}, ||P h_xy P||={np.linalg.norm(K):.3f}, "
              f"Gamma edge={edge_strength(H, np.eye(d), 0, 1, n):.2f}, Gamma(P) edge={edge_strength(H, P, 0, 1, n):.1e}")
        shown += 1
        if shown % 2 == 0:
            break
