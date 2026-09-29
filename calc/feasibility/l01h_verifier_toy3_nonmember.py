# NON-MEMBER toy (O-2 design verification). Not a charter instrument.
# Never evaluates n=23, a=1 (the declared family). Archived per preview discipline.
import numpy as np
from scipy.linalg import expm, eigh
def Kmat(n,a,d,g):
    Q=np.zeros((n,n))
    for i in range(n-1): Q[i+1,i]=1
    Q[0,n-1]=1
    E=np.zeros((n,n)); E[0,0]=1
    return d*np.eye(n)+a*E-g*Q
def wstar(n,a,g):
    r=np.roots([1,a]+[0]*(n-2)+[-g**n]); return max(r.real[abs(r.imag)<1e-7])
def dacc(n,a,g):
    K=Kmat(n,a,0,g); return -eigh((K+K.T)/2,eigvals_only=True)[0]
print("E-3: band [w*, d_acc] at fixed g; delta=g-d_acc vs pi^2 g/(2n^2) and weak-defect a/n - a^2/(6g); width vs g ln(1+a/g)/n (strong) and a^2(n-1)(n-2)/(6g n^2) (weak)")
for n in [3,5,7,11,13,25,51,101]:
  for a in [1.0,0.5,0.01]:
    if n==23 and a==1: continue
    g=1.0
    ws=wstar(n,a,g); da=dacc(n,a,g); delta=g-da
    print(f"n={n:3d} a={a:4}: w*={ws:.6f} d_acc={da:.6f} width={da-ws:.3e} nonempty={da>ws} | delta={delta:.3e} pi2/2n2={np.pi**2*g/(2*n*n):.3e} a/n={a/n:.3e} | strongW={g*np.log(1+a/g)/n - np.pi**2*g/(2*n*n):.3e} weakW={a*a*(n-1)*(n-2)/(6*g*n*n):.3e}")
print("E-2: max_t k(t) / Perron bound in band (non-accretive stable), and k<=exp(-(d-w*)t)")
worst=0
for n in [3,5,7,11,13,25]:
  for a in [1.0,0.5,3.0,10.0]:
    for g in [0.3,1.0,2.0]:
      ws=wstar(n,a,g); da=dacc(n,a,g)
      for d in np.linspace(ws+1e-4*(da-ws),da,5):
        K=Kmat(n,a,d,g); ev=np.linalg.eigvals(K); assert min(ev.real)>0
        mu=eigh((K+K.T)/2,eigvals_only=True)[0]
        ts=np.linspace(0,8*n/d,800); dt=ts[1]; P=expm(-K*dt); x=np.eye(n)[:,0]; mk=0; viol=0; norm=0
        for t in ts[1:]:
            x=P@x; mk=max(mk,x[0]); viol=max(viol,x[0]-np.exp(-(d-ws)*t)); 
        normmax=max(np.linalg.norm(expm(-K*t),2) for t in np.linspace(0,4*n/d,60))
        worst=max(worst,viol)
        if d==da or abs(d-da)<1e-12: print(f"n={n} a={a} g={g} d=d_acc(mu={mu:.1e}): max k(t>0)={mk:.4f} maxviol(Perron)={viol:.1e} max||e^-Kt||_2={normmax:.3f}")
print("worst Perron-bound violation",worst)
