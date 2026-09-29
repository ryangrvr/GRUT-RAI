# NON-MEMBER toy (O-2 design verification). Not a charter instrument.
# Never evaluates n=23, a=1 (the declared family). Archived per preview discipline.
import sys, mpmath as mp, numpy as np
from scipy.linalg import eigh
mp.mp.dps = 50
# NON-MEMBER toys only (n != 23 or a != 1)
def Kmat(n, a, d, g):
    Q = np.zeros((n, n))
    for i in range(n - 1): Q[i + 1, i] = 1
    Q[0, n - 1] = 1
    E = np.zeros((n, n)); E[0, 0] = 1
    return d * np.eye(n) + a * E - g * Q
def dacc(n, a, g):
    K = Kmat(n, a, 0, g); return -eigh((K + K.T) / 2, eigvals_only=True)[0]
def breaks(n, a, d, g):
    W = mp.polyroots([1, a] + [0] * (n - 2) + [-mp.mpf(g) ** n], maxsteps=300, extraprec=300)
    R = [w / (n * w + (n - 1) * a) for w in W]
    for t in np.linspace(0.02, 5.0 * n / d, 400):
        if mp.re(sum(-r * (d - w) * mp.e ** (-(d - w) * t) for r, w in zip(R, W))) > 0: return True
    return False
def gb(n, a, d):
    lo, hi = 0.0, 1.2 * d
    if not breaks(n, a, d, hi): return None
    for _ in range(14):
        m = (lo + hi) / 2
        if breaks(n, a, d, m): hi = m
        else: lo = m
    return hi
def gacc(n, a, d):
    lo, hi = 0.3 * d, 3 * d
    for _ in range(50):
        m = (lo + hi) / 2
        if dacc(n, a, m) < d: lo = m
        else: hi = m
    return lo
n = int(sys.argv[1]); d = 1.0
for a in [1.0, 0.5, 3.0]:
    if n == 23 and a == 1: continue
    b = gb(n, a, d); ga = gacc(n, a, d)
    print(f"n={n} a={a} d=1: g_break~{b}  g_acc={ga:.5f}  accretive&nonmonotone={b is not None and b < ga}  e^(-1-a/d)={np.exp(-1-a/d):.3f}", flush=True)
