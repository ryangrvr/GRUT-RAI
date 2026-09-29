# NON-MEMBER check of review item D-1 (late-time band-edge sign alternation).
# pin = 0.45 (NOT the record's 0.3), N = 800, product Gaussian start, T_s=2, T_b=1.
# Uses exact modal formulas; looks ONLY at t in [150, 700] (late times, far before T_rec ~ 2*799/v_max).
import math
N, PIN, g, Ts, Tb = 800, 0.45, 1.0, 2.0, 1.0
d = 2 + PIN
th = [(2*k-1)*math.pi/(2*N+1) for k in range(1, N+1)]
lam = [d - 2*math.cos(x) for x in th]
om = [math.sqrt(l) for l in lam]
nrm = 2/math.sqrt(2*N+1)
v1 = [nrm*math.sin(x) for x in th]; v2 = [nrm*math.sin(2*x) for x in th]
u = v1; w = [u[k]/lam[k] for k in range(N)]; r = sum(u[k]*u[k]/lam[k] for k in range(N))
K11 = d
def moments(t):
    c = [math.cos(o*t) for o in om]; s = [math.sin(o*t)/o for o in om]
    # q_i(t) = sum_k v_k(i) [c_k Q_k0 + s_k P_k0];  p_i = sum_k v_k(i)[-lam_k s_k Q_k0 + c_k P_k0]
    aq1 = [v1[k]*c[k] for k in range(N)]; bq1 = [v1[k]*s[k] for k in range(N)]
    ap2 = [-v2[k]*lam[k]*s[k] for k in range(N)]; bp2 = [v2[k]*c[k] for k in range(N)]
    # Q0 cov (modal) = (Ts/K11) u u^T + Tb (diag(1/lam) - w w^T / r); P0 cov = Ts u u^T + Tb (I - u u^T)
    def quadQ(x, y):
        xu = sum(a*b for a, b in zip(x, u)); yu = sum(a*b for a, b in zip(y, u))
        xw = sum(a*b for a, b in zip(x, w)); yw = sum(a*b for a, b in zip(y, w))
        return (Ts/K11)*xu*yu + Tb*(sum(x[k]*y[k]/lam[k] for k in range(N)) - xw*yw/r)
    def quadP(x, y):
        xu = sum(a*b for a, b in zip(x, u)); yu = sum(a*b for a, b in zip(y, u))
        return Ts*xu*yu + Tb*(sum(a*b for a, b in zip(x, y)) - xu*yu)
    return g*(quadQ(ap2, aq1) + quadP(bp2, bq1))   # J = g <p2 q1>
ts = [150 + 0.25*i for i in range(2201)]
J = [moments(t) for t in ts]
neg = sum(1 for x in J if x < 0); sign_changes = sum(1 for a, b in zip(J, J[1:]) if (a < 0) != (b < 0))
print(f"NON-MEMBER pin={PIN} N={N}: t in [150,700]: fraction J<0 = {neg/len(J):.3f}, sign changes = {sign_changes}")
print("sample |J| scale at t~150, 400, 700:", [f"{abs(J[i]):.2e}" for i in (0, 1000, 2200)])
# Output (2026-09-29): NON-MEMBER pin=0.45 N=800: t in [150,700]: fraction J<0 = 0.496, sign changes = 739
# sample |J| scale at t~150, 400, 700: 1.10e-06, 8.26e-08, 2.49e-08
# Nothing was computed on the declared pin-0.3 chain.
