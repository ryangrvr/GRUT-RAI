#!/usr/bin/env python3
"""EH six-channel projection -- the A2 phase-1 hard stop, resolved from first principles.

METHOD (recall-proof): build the linearized Ricci operator R^(1)[h] in momentum space,
PROVE the recalled formula correct by verifying gauge invariance R^(1)[k_(mu xi_nu)] = 0
exactly (linearized diffeo invariance -- if the formula were mis-recalled, this fails),
form the Einstein kernel E = R - (1/2) eta tr R, then decompose E in the countersigned
six-channel basis by trace pairing.

TARGET (register-banked, three verifiers, exact rationals): EH = (1/2) k^2 [P2 - 2 P0s].
The RATIO coeff(P0s)/coeff(P2) = -2 is the physical content; overall sign/normalization
is action convention. Gauge invariance => transversality => all gauge/transfer channels
must vanish EXACTLY, not 'modulo gauge'.

AUTHORSHIP: checker-implemented; calibrated by the gauge-invariance identity and the
banked ratio, not by any prior G_coord implementation. W-0: reported, not banked.
"""
from fractions import Fraction as F
from itertools import product as prod
import sys

ETA=[[F(1 if i==j==0 else (-1 if i==j else 0)) for j in range(4)] for i in range(4)]
IDX=list(prod(range(4),repeat=4))

def run(kup):
    klo=[sum(ETA[m][n]*kup[n] for n in range(4)) for m in range(4)]
    k2=sum(kup[m]*klo[m] for m in range(4))
    th=[[ETA[m][n]-klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    om=[[klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    T4=lambda f:{x:f(*x) for x in IDX}
    P={'P2':T4(lambda m,n,r,s:F(1,2)*(th[m][r]*th[n][s]+th[m][s]*th[n][r])-F(1,3)*th[m][n]*th[r][s]),
       'P1':T4(lambda m,n,r,s:F(1,2)*(th[m][r]*om[n][s]+th[m][s]*om[n][r]+th[n][r]*om[m][s]+th[n][s]*om[m][r])),
       'P0s':T4(lambda m,n,r,s:F(1,3)*th[m][n]*th[r][s]),
       'P0w':T4(lambda m,n,r,s:om[m][n]*om[r][s]),
       'Xsw':T4(lambda m,n,r,s:th[m][n]*om[r][s]),
       'Xws':T4(lambda m,n,r,s:om[m][n]*th[r][s])}
    # ---- linearized Ricci as a kernel on h (momentum space, all indices explicit) ----
    # R_mn[h] = 1/2( -k_m k^l h_ln - k_n k^l h_lm + k^2 h_mn + k_m k_n h ),  h = eta^rs h_rs
    # As a 4-index kernel acting on h_rs (symmetrized in r,s):
    def sym(d):
        return {(m,n,r,s):F(1,2)*(d[(m,n,r,s)]+d[(m,n,s,r)]) for m,n,r,s in IDX}
    def delta(a,b): return F(1 if a==b else 0)
    # Kernel stored all-lower; application raises (r,s) with eta. So every free lower index
    # on h in the formula becomes a METRIC factor, and every contracted k^l becomes klo:
    #   -1/2 k_m k^l h_{ln}  ->  -1/2 klo[m] klo[r] ETA[n][s]
    #   +1/2 k^2 h_{mn}      ->  +1/2 k2 ETA[m][r] ETA[n][s]
    #   +1/2 k_m k_n h       ->  +1/2 klo[m] klo[n] ETA[r][s]
    # (INDEX-VARIANCE RULE applied after the gauge check caught the kup/delta mis-encoding.)
    Ric={}
    for m,n,r,s in IDX:
        t = F(0)
        t += -F(1,2)*klo[m]*klo[r]*ETA[n][s]
        t += -F(1,2)*klo[n]*klo[r]*ETA[m][s]
        t += F(1,2)*k2*ETA[m][r]*ETA[n][s]
        Ric[(m,n,r,s)]=t
    # trace term: +1/2 k_m k_n h,  h = eta^{rs} h_rs -> kernel += 1/2 klo[m] klo[n] * etaINV[r][s]
    for m,n,r,s in IDX:
        Ric[(m,n,r,s)] += F(1,2)*klo[m]*klo[n]*ETA[r][s]   # eta inverse = eta (diag +-1)
    Ric=sym(Ric)
    # ---- GAUGE-INVARIANCE PROOF of the recalled formula ----
    import random
    random.seed(7)
    ok_gauge=True
    for trial in range(3):
        xi=[F(random.randint(-5,5)) for _ in range(4)]
        hg={ (r,s): klo[r]*xi[s]+klo[s]*xi[r] for r,s in prod(range(4),repeat=2)}
        out=[sum(Ric[(m,n,r,s)]*ETA[r][r]*ETA[s][s]*hg[(r,s)] for r,s in prod(range(4),repeat=2))
             for m,n in prod(range(4),repeat=2)]
        if any(x!=0 for x in out): ok_gauge=False
    print("  gauge invariance R^(1)[k_(mu xi_nu)] = 0 (3 random xi):","PROVED" if ok_gauge else "FAIL")
    if not ok_gauge: return False
    # ---- Einstein kernel E = Ric - 1/2 eta_mn (eta^ab Ric_ab) ----
    E={}
    for m,n,r,s in IDX:
        tr = sum(ETA[a][b]*Ric[(a,b,r,s)] for a,b in prod(range(4),repeat=2))
        E[(m,n,r,s)] = Ric[(m,n,r,s)] - F(1,2)*ETA[m][n]*tr
    # ---- six-channel decomposition by trace pairing ----
    def pair(A,B): return sum(A[(m,n,r,s)]*ETA[m][m]*ETA[n][n]*ETA[r][r]*ETA[s][s]*B[(m,n,r,s)]
                              for m,n,r,s in IDX)
    coeff={}
    coeff['P2'] = pair(P['P2'],E)/pair(P['P2'],P['P2'])
    coeff['P0s']= pair(P['P0s'],E)/pair(P['P0s'],P['P0s'])
    coeff['P1'] = pair(P['P1'],E)/pair(P['P1'],P['P1'])
    coeff['P0w']= pair(P['P0w'],E)/pair(P['P0w'],P['P0w'])
    # under the full component pairing the six structures are MUTUALLY ORTHOGONAL and the
    # transfer structures pair with THEMSELVES: pair(Xsw,Xsw)=(th.th)(om.om)=3, while
    # pair(Xws,Xsw)=(th.om)^2=0. (Corrects the earlier 'conjugate pairing' note.)
    coeff['Xsw']= pair(P['Xsw'],E)/pair(P['Xsw'],P['Xsw'])
    coeff['Xws']= pair(P['Xws'],E)/pair(P['Xws'],P['Xws'])
    print("  channel coefficients (in units where k^2=%s):"%k2)
    for nm in ('P2','P0s','P1','P0w','Xsw','Xws'):
        print("    %-4s : %s"%(nm,coeff[nm]))
    # residual: E minus its P2/P0s parts must vanish IDENTICALLY (not modulo gauge)
    R={x:E[x]-coeff['P2']*P['P2'][x]-coeff['P0s']*P['P0s'][x] for x in IDX}
    maxres=max(abs(v) for v in R.values())
    print("  residual E - c2 P2 - c0 P0s : max |.| = %s  %s"%(maxres,"(IDENTICALLY ZERO)" if maxres==0 else "NONZERO"))
    ratio=coeff['P0s']/coeff['P2']
    print("  RATIO coeff(P0s)/coeff(P2) = %s   (banked target: -2)"%ratio)
    return maxres==0 and ratio==F(-2) and all(coeff[nm]==0 for nm in ('P1','P0w','Xsw','Xws'))

allok=True
for kup in ([F(5),F(4),F(2),F(1)],[F(2),F(1),F(1),F(1)]):
    print("k^mu =",[str(x) for x in kup])
    allok &= run(kup); print()
print("VERDICT:","EH = c * k^2 [P2 - 2 P0s] EXACTLY -- gauge/transfer channels identically zero;"
      " the banked identity is reproduced from first principles" if allok else "FAILURES ABOVE")
sys.exit(0 if allok else 1)
