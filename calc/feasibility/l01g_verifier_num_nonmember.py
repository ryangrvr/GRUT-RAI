import numpy as np, scipy.linalg as sl
# toy N=3, NOT the record chain: diag 3.1,2.7,1.9 ; couplings -0.7,-0.5
K=np.array([[3.1,-0.7,0],[-0.7,2.7,-0.5],[0,-0.5,1.9]]); N=3
A=np.block([[np.zeros((N,N)),np.eye(N)],[-K,np.zeros((N,N))]])
def Sig0(Ts,Tb):
    S=np.zeros((2*N,2*N)); S[0,0]=Ts/K[0,0]; S[N,N]=Ts
    S[1:N,1:N]=Tb*np.linalg.inv(K[1:,1:]); S[N+1:,N+1:]=Tb*np.eye(N-1); return S
def St(S0,t): E=sl.expm(A*t); return E@S0@E.T
def EB(S): return 0.5*np.trace(S[N+1:,N+1:])+0.5*np.trace(K[1:,1:]@S[1:N,1:N])
def D(S,Tb,refq):
    s=np.array([[S[0,0],S[0,N]],[S[0,N],S[N,N]]]); R=np.diag([refq,Tb])
    return 0.5*(np.trace(np.linalg.solve(R,s))-2-np.log(np.linalg.det(s)/np.linalg.det(R)))
Gb=np.linalg.inv(K[1:,1:])[0,0]; G11=np.linalg.inv(K)[0,0]; g=0.7
for (Ts,Tb) in [(2,1),(0.5,1)]:
    S0=Sig0(Ts,Tb)
    for t in [0.02,0.05,0.1]:
        S=St(S0,t)
        print(Ts,Tb,t,'dEB=%.3e'%(EB(S)-EB(S0)),'pred EB~%.3e'%(Ts*g**2*t**2/(2*K[0,0])),
          'dD_loc=%.3e'%(D(S,Tb,Tb/K[0,0])-D(S0,Tb,Tb/K[0,0])),'dD_glob=%.3e'%(D(S,Tb,Tb*G11)-D(S0,Tb,Tb*G11)),
          'pred=%.3e'%(g**2*Gb/2*(1-Tb/Ts)*t**2))
# I-2/I-3 W check with deterministic response functions
for t in [0.05,0.1,0.2]:
    E=sl.expm(A*t)
    # state x=(q,p); columns 0 (q10) and N (p10)
    u=np.array([E[N,0],E[N,N]]); v=np.array([E[1,0],E[1,N]])
    W=u[0]*v[1]-u[1]*v[0]
    u3=np.array([E[0,0],E[0,N]]); v3=np.array([E[N+1,0],E[N+1,N]])
    W3=u3[0]*v3[1]-u3[1]*v3[0]
    print(t,'W_I2=%.4e'%W,'pred %.4e'%(-g*t**2/2),'W_I3=%.4e'%W3,'pred %.4e'%(-g*t**2/2))
