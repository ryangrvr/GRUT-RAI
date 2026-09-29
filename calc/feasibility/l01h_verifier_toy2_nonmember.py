# NON-MEMBER toy (O-2 design verification). Not a charter instrument.
# Never evaluates n=23, a=1 (the declared family). Archived per preview discipline.
import mpmath as mp, numpy as np
from toy import Kmat, dacc
mp.mp.dps=80
def roots(n,a,g):
    c=[1,a]+[0]*(n-2)+[-mp.mpf(g)**n]
    return mp.polyroots(c,maxsteps=500,extraprec=400)
def kfun(n,a,d,g):
    W=roots(n,a,g); R=[w**(n-1)/(n*w**(n-1)+(n-1)*a*w**(n-2)) for w in W]
    k=lambda t: mp.re(sum(r*mp.e**(-(d-w)*t) for r,w in zip(R,W)))
    kp=lambda t: mp.re(sum(-r*(d-w)*mp.e**(-(d-w)*t) for r,w in zip(R,W)))
    ws=max(mp.re(w) for w in W if abs(mp.im(w))<1e-30)
    return k,kp,ws
def breaks(n,a,d,g,T=None):
    k,kp,ws=kfun(n,a,d,g)
    T=T or 6.0*n/d
    ts=np.linspace(0.01,T,1500)
    return max(float(kp(t)/abs(k(t))) for t in ts)>0
def gb(n,a,d):
    lo,hi=0.01,1.5*d
    if not breaks(n,a,d,hi): return None
    for _ in range(25):
        m=(lo+hi)/2
        if breaks(n,a,d,m): hi=m
        else: lo=m
    return hi
def gacc(n,a,d):
    lo,hi=0.5*d,3*d
    for _ in range(50):
        m=(lo+hi)/2
        if dacc(n,a,m)<d: lo=m
        else: hi=m
    return lo
if __name__=="__main__":
    d=1.0
    for n in [3,5,7,9,11,13,17,25,31]:
        for a in [1.0,0.5,3.0]:
            if n==23 and a==1: continue
            b=gb(n,a,d); ga=gacc(n,a,d)
            asym=d*np.exp(-1-a/d)
            print(f"n={n} a={a} d=1: g_break={b}  g_acc={ga:.5f}  accretive-nonmonotone band exists={b is not None and b<ga}  asym e^(-1-a/d)={asym:.3f}")
