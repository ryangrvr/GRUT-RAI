#!/usr/bin/env python3
"""THE SCALAR MEMBERSHIP RUN: the six boost-killed scalar structures, COMPUTED not subtracted.

For each curved scalar kernel structure (a-field x r-channel), its H->0 limit is built as an
explicit field-space bilinear and rank-tested for membership in the flat Lorentz-covariant
Ward family span{P0s, Xsw}, pulled back through the exact bijection T: fields <-> h_mn at
fixed k. The invariant statement is the INTERSECTION DIMENSION of the two spans; the
per-structure table is reported alongside. Plants: P0s itself must be a member; a
P1-pullback must be rejected. Two rational (omega,k) samples.
This run also settles the Ward-identification soft spot: the flat family's r-covectors
(theta-trace) must lie in the span of the curved r-channels' flat limits {psi, phi+sB-s^2E}.
TYPE: KERNEL-STRUCTURE statements. AUTHORSHIP: checker; review owed. W-0 binding.
"""
import sympy as sp

I=sp.I
def run(om,kk):
    w,k=sp.Integer(om),sp.Integer(kk); s=-I*w          # d/deta -> s = -i*omega
    ETA=sp.diag(1,-1,-1,-1)
    q=[w,0,0,k]; qlo=[ETA[m,m]*q[m] for m in range(4)]
    q2=sum(q[m]*qlo[m] for m in range(4))
    th=sp.Matrix(4,4,lambda m,n: ETA[m,n]-qlo[m]*qlo[n]/q2)
    omg=sp.Matrix(4,4,lambda m,n: qlo[m]*qlo[n]/q2)
    def K4(f): return {(m,n,r,ss):f(m,n,r,ss) for m in range(4) for n in range(4)
                       for r in range(4) for ss in range(4)}
    P0s=K4(lambda m,n,r,ss: th[m,n]*th[r,ss]/3)
    Xsw=K4(lambda m,n,r,ss: th[m,n]*omg[r,ss])
    P1 =K4(lambda m,n,r,ss: (th[m,r]*omg[n,ss]+th[m,ss]*omg[n,r]
                             +th[n,r]*omg[m,ss]+th[n,ss]*omg[m,r])/2)
    # exact bijection T: fields (phi,B,psi,E,Sx,Sy,Fx,Fy,hp,hx) -> h_mn at a=1
    def hOf(e):
        f=[sp.Integer(0)]*10; f[e]=sp.Integer(1)
        phi,B,psi,E,Sx,Sy,Fx,Fy,hp,hx=f
        h=sp.zeros(4,4)
        h[0,0]=-2*phi
        h[0,1]=h[1,0]=Sx; h[0,2]=h[2,0]=Sy; h[0,3]=h[3,0]=I*k*B
        h[1,1]=-2*psi+hp; h[2,2]=-2*psi-hp; h[3,3]=-2*psi-2*k**2*E
        h[1,2]=h[2,1]=hx; h[1,3]=h[3,1]=I*k*Fx; h[2,3]=h[3,2]=I*k*Fy
        return h
    H=[hOf(u) for u in range(10)]
    def pull(K):   # field-space bilinear: SLOT 1 IS THE r-SLOT (Ward-constrained), so it
        # contracts h_r; slot 2 contracts h_a.  M[u][v] = B(f_a=e_u, f_r=e_v).
        # SLOT-SWAP DEFECT CAUGHT 2026-08-24: the first version contracted h_a with slot 1,
        # comparing the family with its slots exchanged -- Xsw then failed membership as an
        # artifact. Same index/slot error family as kup/klo; caught by diagnosing the
        # 'MISMATCH' finding against the flat r-covector by hand before reporting it.
        M=sp.zeros(10,10)
        for u in range(10):
            ha=H[u]
            for v in range(10):
                hr=H[v]; tot=sp.Integer(0)
                for m in range(4):
                    for n in range(4):
                        rr=ETA[m,m]*ETA[n,n]*hr[m,n]
                        if rr==0: continue
                        for r in range(4):
                            for ss in range(4):
                                aa=ETA[r,r]*ETA[ss,ss]*ha[r,ss]
                                if aa==0: continue
                                tot+=K[(m,n,r,ss)]*rr*aa
                M[u,v]=sp.expand(tot)
        return M
    Bp0s,Bxsw,Bp1=pull(P0s),pull(Xsw),pull(P1)
    # curved scalar structures at H->0: a in {phi,B,psi,E}(idx 0..3) x r in {Psi0, Phi0}
    wPsi=[0,0,1,0,0,0,0,0,0,0]
    wPhi=[1,s,0,-s**2,0,0,0,0,0,0]
    def S(u,wv):
        M=sp.zeros(10,10)
        for v in range(10): M[u,v]=wv[v]
        return M
    curved=[S(u,wv) for u in range(4) for wv in (wPsi,wPhi)]
    vec=lambda M:[M[i,j] for i in range(10) for j in range(10)]
    def rk(Ms): return sp.Matrix([vec(M) for M in Ms]).rank()
    r_fam=rk([Bp0s,Bxsw]); r_cur=rk(curved); r_all=rk(curved+[Bp0s,Bxsw])
    inter=r_cur+r_fam-r_all
    print(" (omega,k)=(%s,%s): rank(family)=%d rank(8 curved)=%d rank(union)=%d -> INTERSECTION=%d"
          %(om,kk,r_fam,r_cur,r_all,inter))
    print("   => scalar boost-killed = %d COMPUTED (8 - intersection)"%(r_cur-inter))
    # per-structure membership table
    names=["%s (x) %s"%(a,r) for a in ("phi","B","psi","E") for r in ("Psi0","Phi0")]
    for nm,M in zip(names,curved):
        m=rk([Bp0s,Bxsw,M])
        print("   %-14s : %s"%(nm,"IN family span" if m==r_fam else "OUTSIDE (boost-killed)"))
    # plants
    print("   plant P0s self-membership : %s"%("PASS" if rk([Bp0s,Bxsw,Bp0s])==r_fam else "FAIL"))
    print("   plant P1 rejected          : %s"%("PASS" if rk([Bp0s,Bxsw,Bp1])==r_fam+1 else "FAIL"))
    # Ward-identification: family r-covectors within curved channel span?
    r_chan=sp.Matrix([wPsi,wPhi]).rank()
    fam_in_curved = (r_all==r_cur)
    print("   Ward-identification (family inside curved Ward span): %s"%("CONFIRMED" if fam_in_curved else "MISMATCH -- FINDING"))
    return inter, r_cur-inter, fam_in_curved

print("SCALAR MEMBERSHIP RUN -- computed boost-killed list")
res=[run(3,2),run(5,2)]
ok=all(i==2 and b==6 and w for i,b,w in res)
print("\nVERDICT:","INTERSECTION = 2 AND SCALAR BOOST-KILLED = 6, COMPUTED AT BOTH SAMPLES;"
      " Ward-identification CONFIRMED -- full boost list now 8 = 2 vector + 6 scalar, ALL COMPUTED"
      if ok else "UNEXPECTED RESULT -- report as found: %s"%str(res))
