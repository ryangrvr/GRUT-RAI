# Feasibility benchmark ONLY, on a NON-member matrix (pin 0.7, arbitrary temps).
import time
from fractions import Fraction as F
N = 23
K = [[F(0)]*N for _ in range(N)]
for i in range(N):
    K[i][i] = F(27,10) if i < N-1 else F(17,10)   # pin 0.7: NOT a charter member
for i in range(N-1):
    K[i][i+1] = K[i+1][i] = F(-1)
T = [F(3 + (i*7) % 5, 2) for i in range(N)]       # arbitrary non-member temps
idx = {}
for i in range(N):
    for j in range(i, N):
        idx[(i, j)] = len(idx)
n = len(idx)
def key(a, b): return idx[(a, b)] if a <= b else idx[(b, a)]
rows, rhs = [], []
for i in range(N):
    for j in range(i, N):
        r = {}
        for m in range(N):
            if K[i][m]: r[key(m, j)] = r.get(key(m, j), 0) + K[i][m]
            if K[m][j]: r[key(i, m)] = r.get(key(i, m), 0) + K[m][j]
        rows.append(r); rhs.append(2*T[i] if i == j else F(0))
t0 = time.time()
A = [[F(0)]*n + [rhs[k]] for k in range(n)]
for k, r in enumerate(rows):
    for c, v in r.items(): A[k][c] = F(v)
for c in range(n):
    p = next(r for r in range(c, n) if A[r][c] != 0)
    A[c], A[p] = A[p], A[c]
    pv = A[c][c]
    rowc = A[c]
    nz = [j for j in range(c, n+1) if rowc[j] != 0]
    for r in range(c+1, n):
        f = A[r][c]
        if f != 0:
            f = f / pv
            Ar = A[r]
            for j in nz: Ar[j] -= f * rowc[j]
x = [F(0)]*n
for c in range(n-1, -1, -1):
    s = A[c][n] - sum(A[c][j]*x[j] for j in range(c+1, n) if A[c][j] != 0)
    x[c] = s / A[c][c]
el = time.time() - t0
# residual check
Sig = [[x[key(i,j)] for j in range(N)] for i in range(N)]
res = max(abs(sum(K[i][m]*Sig[m][j] + Sig[i][m]*K[m][j] for m in range(N)) - (2*T[i] if i==j else 0)) for i in range(N) for j in range(N))
dig = max(len(str(v.numerator)) + len(str(v.denominator)) for v in x)
print(f"unknowns={n} elimination {el:.1f}s  exact residual={res}  max digits={dig}")
# Output of the single timing run (2026-09-29), before the L0-1e first draft:
# unknowns=276 elimination 1.0s  exact residual=0  max digits=730
# Only wall-time, residual and digit count were printed; no weight, CM status, or kernel.
