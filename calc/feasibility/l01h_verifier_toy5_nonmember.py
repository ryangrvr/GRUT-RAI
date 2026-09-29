# NON-MEMBER toy (O-2 design verification). Not a charter instrument.
# Never evaluates n=23, a=1 (the declared family). Archived per preview discipline.
import mpmath as mp, numpy as np
mp.mp.dps=50
# n=3, a=3, d=1: extend g range; also check break-set monotone in g for n=7,a=1 on a coarse grid
def brk(n,a,d,g,T=None):
    W=mp.polyroots([1,a]+[0]*(n-2)+[-mp.mpf(g)**n],maxsteps=300,extraprec=300)
    R=[w/(n*w+(n-1)*a) for w in W]
    return any(mp.re(sum(-r*(d-w)*mp.e**(-(d-w)*t) for r,w in zip(R,W)))>0 for t in np.linspace(0.02,(T or 8.0*n/d),600))
print([ (g,brk(3,3,1,g)) for g in [1.2,1.3,1.4,1.45,1.46]])
print([ (round(g,2),brk(7,1,1,g)) for g in np.linspace(0.3,1.06,12)])
