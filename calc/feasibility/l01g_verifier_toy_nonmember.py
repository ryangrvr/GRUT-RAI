import sympy as sp
t=sp.symbols('t')
a1,a2,a3,a4,g,h,m,Ts,Tb=sp.symbols('a1 a2 a3 a4 g h m T_s T_b',positive=True)
N=4
K=sp.Matrix([[a1,-g,0,0],[-g,a2,-h,0],[0,-h,a3,-m],[0,0,-m,a4]])
Z=sp.zeros(N);I=sp.eye(N)
A=sp.BlockMatrix([[Z,I],[-K,Z]]).as_explicit()
KB=K[1:,1:]
S0=sp.zeros(2*N)
S0[0,0]=Ts/a1; S0[N,N]=Ts
S0[1:N,1:N]=Tb*KB.inv()
for i in range(1,N): S0[N+i,N+i]=Tb
# Taylor of Sigma
order=7
terms=[S0]; cur=S0
for n in range(1,order+1):
    cur=(A*cur+cur*A.T); terms.append(cur)
Sig=sum((terms[n]*t**n/sp.factorial(n) for n in range(order+1)),sp.zeros(2*N))
# dE_B/dt = g * <p2 q1>  (general coupling -g)
cur_heat=sp.expand(g*Sig[N+1,0])
print('dEB/dt =', sp.collect(sp.simplify(cur_heat),t))
# reduced covariance site1
q2=sp.expand(Sig[0,0]); p2=sp.expand(Sig[N,N]); qp=sp.expand(Sig[0,N])
print('<q1^2>-T_s/a1 =', sp.factor(sp.series(q2,t,0,7).removeO()-Ts/a1))
print('<p1^2>-T_s =', sp.factor(sp.series(p2,t,0,7).removeO()-Ts))
print('<q1p1> =', sp.factor(sp.series(qp,t,0,6).removeO()))
print('----')
ser=sp.series(sp.simplify(cur_heat),t,0,6).removeO()
for k in range(0,6):
    c=sp.factor(sp.simplify(ser.coeff(t,k)))
    if c!=0: print('t^%d:'%k,c)
# local-Gibbs relative entropy of Gaussian 1-dof: D = 1/2[tr(S0^-1 S) - 2 - ln det(S)/det(S0)]
Sq=sp.series(q2,t,0,7).removeO(); Sp=sp.series(p2,t,0,7).removeO(); Sx=sp.series(qp,t,0,7).removeO()
def D(refq,refp):
    return sp.Rational(1,2)*(Sq/refq+Sp/refp-2-sp.log((Sq*Sp-Sx**2)/(refq*refp)))
Dl=sp.series(D(Tb/a1,Tb),t,0,7).removeO()
for k in range(0,7):
    c=sp.factor(sp.simplify(Dl.coeff(t,k)))
    if c!=0 and k>0: print('D_local t^%d:'%k,c)
