# NON-MEMBER toy (O-2 design verification). Not a charter instrument.
# Never evaluates n=23, a=1 (the declared family). Archived per preview discipline.
import numpy as np, mpmath as mp
from scipy.linalg import expm, eigh
from math import factorial, lgamma, exp, log
def Kmat(n,a,d,g):
    Q=np.zeros((n,n))
    for i in range(n-1): Q[i+1,i]=1
    Q[0,n-1]=1
    E=np.zeros((n,n)); E[0,0]=1
    return d*np.eye(n)+a*E-g*Q, Q
def wstar(n,a,g):
    r=np.roots([1,a]+[0]*(n-2)+[-g**n]); return max(r.real[abs(r.imag)<1e-9])
def dacc(n,a,g):
    K,Q=Kmat(n,a,0,g); Ks=(K+K.T)/2; return -eigh(Ks,eigvals_only=True)[0]
assert not False
# J-1 and eigen check
for (n,a,d,g) in [(5,1,1,0.9),(7,0.5,0.8,1.1),(11,1,1,0.7),(13,0.5,1,1.02)]:
    K,Q=Kmat(n,a,d,g); s=0.3+0.7j; w=d+s
    G=np.linalg.inv(K+s*np.eye(n))[0,0]; Gf=w**(n-1)/(w**(n-1)*(w+a)-g**n)
    ev=np.sort_complex(np.linalg.eigvals(K)); rt=np.sort_complex(d-np.roots([1,a]+[0]*(n-2)+[-g**n]))
    # series vs expm
    errs=[]
    for t in [0.5,3,10,25]:
        kex=expm(-K*t)[0,0]
        mp.mp.dps=30
        # h_j via exact: inverse Laplace numeric of each term: use sum with convolution by quadrature
        tot=mp.e**(-(d+a)*t)
        for j in range(1,12):
            m=(n-1)*j
            f=lambda u: (t-u)**(m-1)/mp.factorial(m-1)*u**j*mp.e**(-a*u)/mp.factorial(j)
            tot+=g**(n*j)*mp.e**(-d*t)*mp.quad(f,[0,t])
        errs.append(abs(float(tot)-kex))
    print("J1",n,a,d,g,abs(G-Gf),np.max(abs(ev-rt)),"J2 errs",max(errs))
