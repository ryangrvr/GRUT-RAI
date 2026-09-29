# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S5: inspect an edge-removing H for the correlated (non-frozen) sector span{|000>,|110>} (x=0,y=1,s=2):
x's configuration is NOT fixed in the sector; is P h_xy P non-scalar (coupling acting non-trivially)?"""
import itertools
import numpy as np
from common import *
from s3_L7_random_sector import solve_space, Ops, strings

n, d = 3, 8
names = 'IXYZ'
jointmask = np.array([s[0] != 0 and s[1] != 0 for s in strings])
P = np.zeros((d, d), complex); P[0, 0] = 1; P[6, 6] = 1   # |000>, |110>
null = solve_space(P)
print("admissible dim:", len(null))
# print a basis of admissible H restricted to joint x-y Pauli content
J = null[:, jointmask]
u, s, vt = np.linalg.svd(J.T)
print("singular values of joint-content map:", np.round(s, 3))
for k in range(int(np.sum(s > 1e-8))):
    c = null.T @ vt[k]
    terms = [(''.join(names[i] for i in strings[m]), round(c[m], 3)) for m in range(64) if abs(c[m]) > 1e-6]
    H = sum(cc * O for cc, O in zip(c, Ops))
    hxy = h_xy_part(H, 0, 1, n)
    PhP = P @ hxy @ P
    print(f"H_{k}: {terms}")
    print(f"   ||[H,P]||={np.linalg.norm(comm(H,P)):.1e}  Gamma edge={edge_strength(H, np.eye(d), 0, 1, n):.3f} "
          f" Gamma(P) edge={edge_strength(H, P, 0, 1, n):.1e}  P h_xy P restricted = \n{np.round(PhP[np.ix_([0,6],[0,6])],3)}")
# hand example: H = XxXy (+ fields) on sector span{000,110}
for lab, H in [("XxXy", site_op(X,0,n)@site_op(X,1,n)),
               ("XxXy + YxYy", site_op(X,0,n)@site_op(X,1,n)+site_op(Y,0,n)@site_op(Y,1,n)),
               ("XxXy - YxYy", site_op(X,0,n)@site_op(X,1,n)-site_op(Y,0,n)@site_op(Y,1,n))]:
    print(lab, " [H,P]=", round(np.linalg.norm(comm(H,P)),3), " Gamma(P) edge=", round(edge_strength(H,P,0,1,n),3))
