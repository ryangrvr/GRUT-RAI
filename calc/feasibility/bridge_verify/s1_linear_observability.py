# Access-bridge verification: ABSTRACT mathematics (proof support); not a physics member; no simulation campaign.
"""S1: abstract linear-algebra checks on the committed K (read-only import of build_K).
(a) single-site Kalman observability of K_b = build_K(24,0)[1:,1:] and of build_K(24,0), per site
(b) (K - w^2)^{-1} vs (K + s)^{-1}: same rational matrix function under z = w^2 = -s
(c) Koopman on L2(Lebesgue): ||f o phi_t||^2 = e^{t tr K} ||f||^2 (Gaussian test function, closed form)
"""
import sys
import numpy as np
sys.path.insert(0, "/home/user/GRUT-RAI/calc")
from c1_seam import build_K

K = np.array(build_K(24, 0.0))
Kb = K[1:, 1:]
for name, M in (("K_full(24)", K), ("K_b(23)", Kb)):
    lam, V = np.linalg.eigh(M)
    n = len(M)
    gaps = np.min(np.diff(lam))
    ranks = []
    for i in range(n):
        O = np.array([np.linalg.matrix_power(M, j)[i] for j in range(n)])
        # PBH-equivalent test is better conditioned: min |V[i,k]|
        ranks.append(np.min(np.abs(V[i, :])))
    print(name, "min eig gap", gaps, "diag", np.diag(M)[:3], "...", np.diag(M)[-2:])
    print("  per-site min_k |v_k(i)| (0 => site i fails single-site observability):")
    print("  ", np.array2string(np.array(ranks), precision=2))

# (b) resolvent identity
w2 = 0.09
s = -w2
A = [0, 5, 11]
G1 = np.linalg.inv(Kb - w2 * np.eye(23))[np.ix_(A, A)]
G2 = np.linalg.inv(Kb + s * np.eye(23))[np.ix_(A, A)]
print("(b) max|G(w^2) - G(s=-w^2)| =", np.max(np.abs(G1 - G2)))

# (c) Koopman on L2(Leb): f(x)=exp(-|x|^2/2); ||f o phi_t||^2 = pi^{n/2}/sqrt(det(E^T E)), E=e^{-Kt}
from scipy.linalg import expm
M = Kb[:4, :4]
t = 0.7
E = expm(-M * t)
n = 4
lhs = np.pi ** (n / 2) / np.sqrt(np.linalg.det(E.T @ E))
rhs = np.exp(t * np.trace(M)) * np.pi ** (n / 2)
print("(c) ||U^t f||^2 / (e^{t trK}||f||^2) =", lhs / rhs)
