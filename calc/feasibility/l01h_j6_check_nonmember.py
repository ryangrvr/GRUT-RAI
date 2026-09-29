# NON-MEMBER check of identity J-6 (L0_1H_THEOREM_01.md). Never evaluates n=23, a=1.
# NON-MEMBER check of identity J-6: k'(t)>0 <=> g*y_n(t) > (d+a)*y_1(t), y=exp(P t)e1, P=gQ+a(I-E11) >= 0 (d-free)
import numpy as np
from scipy.linalg import expm, eigh
def mats(n,a,g):
    Q=np.zeros((n,n)); 
    for i in range(n-1): Q[i+1,i]=1
    Q[0,n-1]=1; E=np.zeros((n,n)); E[0,0]=1
    return Q,E
for (n,a,g,d) in [(5,1,0.9,1.0),(7,1,0.5,0.95),(11,0.5,0.6,0.8),(13,3,0.2,1.0)]:
    assert not (n==23 and a==1)
    Q,E=mats(n,a,g); K=d*np.eye(n)+a*E-g*Q; P=g*Q+a*(np.eye(n)-E)
    worst=0
    for t in np.linspace(0.05,60,400):
        kp=-(K@expm(-K*t))[0,0]; y=expm(P*t)[:,0]
        crit=(g*y[-1]-(d+a)*y[0])*np.exp(-(d+a)*t)
        worst=max(worst,abs(kp-crit)/(abs(kp)+1e-300))
    ts=np.linspace(0.01,200,20000); R=max(g*expm(P*t)[-1,0]/expm(P*t)[0,0] for t in ts[::20])
    Ks=lambda dd:(dd*np.eye(n)+a*E-g*(Q+Q.T)/2)
    dacc=-eigh(a*E-g*(Q+Q.T)/2,eigvals_only=True)[0]
    r=np.roots([1,a]+[0]*(n-2)+[-g**n]); ws=max(r.real[abs(r.imag)<1e-9])
    print(f"n={n} a={a} g={g}: J6 rel.err={worst:.1e}  w*={ws:.4f} d_acc={dacc:.4f} d_mono~R-a={R-a:.4f}")
