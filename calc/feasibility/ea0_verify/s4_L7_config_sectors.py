# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S4: exhaustive scan of 'classical-configuration' sectors (spans of computational basis states) on 3 qubits
(x=0, y=1, s=2).  For each subset S (|S|>=2), is there an H with [H,P_S]=0, h_xy != 0 (edge in Gamma),
and the x-y edge removed in Gamma(P_S)?  Tabulate against simple structural predicates:
  xfrozen: all configs in S share the same x-bit;  yfrozen: same y-bit.
Also verifies the dual NSC: edge removed <=> Tr_{not y}[H,[A,M]] = 0 for all A in A_x, M in P B(H) P."""
import itertools
import numpy as np
from common import *
from s3_L7_random_sector import solve_space, Ops, strings
jointmask = np.array([s[0] != 0 and s[1] != 0 for s in strings])

n, d, x, y = 3, 8, 0, 1
bits = [tuple((k >> (n - 1 - q)) & 1 for q in range(n)) for k in range(d)]

def ptrace_keep(Mop, keep):
    T = Mop.reshape([2] * (2 * n))
    # trace out all qubits except 'keep'
    idx_in = list(range(n)); idx_out = list(range(n, 2 * n))
    letters = 'abcdefghijklmnop'
    ins = [letters[i] for i in range(n)]; outs = [letters[n + i] for i in range(n)]
    for q in range(n):
        if q != keep:
            outs[q] = ins[q]
    expr = ''.join(ins) + ''.join(outs) + '->' + ins[keep] + outs[keep]
    return np.einsum(expr, T)

counts = {}
examples = []
dual_ok = True
for r in range(2, d):
    for S in itertools.combinations(range(d), r):
        P = np.zeros((d, d), complex)
        for k in S: P[k, k] = 1
        null = solve_space(P)
        J = null[:, jointmask] if len(null) else np.zeros((0, 1))
        removable = len(null) > 0 and np.linalg.norm(J) > 1e-8
        xf = len({bits[k][x] for k in S}) == 1
        yf = len({bits[k][y] for k in S}) == 1
        key = (xf, yf, removable)
        counts[key] = counts.get(key, 0) + 1
        if removable and not (xf or yf):
            examples.append(S)
        if removable and len(examples) < 3 and r == 4:
            # dual NSC check on the max-joint-content admissible H
            u, s, vt = np.linalg.svd(J.T); cH = null.T @ vt[0]
            H = sum(c * O for c, O in zip(cH, Ops))
            worst = 0
            for a in PAULI:
                A = site_op(a, x, n)
                for i in S:
                    for j in S:
                        Mop = np.zeros((d, d), complex); Mop[i, j] = 1
                        worst = max(worst, np.linalg.norm(ptrace_keep(comm(H, comm(A, Mop)), y)))
            dual_ok &= worst < 1e-9
print("(x frozen, y frozen, edge-removal possible with h_xy!=0): count")
for k in sorted(counts): print("  ", k, counts[k])
print("removable sectors with neither x nor y frozen:", [[bits[k] for k in S] for S in examples][:6], "... total", len(examples))
print("dual NSC consistent on sampled removable cases:", dual_ok)
