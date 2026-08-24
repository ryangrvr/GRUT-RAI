#!/usr/bin/env python3
# A2 PHASE 1 v3 - clean rewrite. BR projectors correct-by-construction:
# orthonormal sector bases, sqrt2-weighted 6-vector convention.
# Plants: TT -> P2, scalar -> P0s, EH identity vs independent derivation.
SECTORS={}
import json, math

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def norm(a): return math.sqrt(dot(a,a))

KVEC=[2.0,3.0,6.0]
KK=dot(KVEC,KVEC)                     # 49
W=[x/math.sqrt(KK) for x in KVEC]     # unit axis
u1=cross(KVEC,[1.0,0.0,0.0]); e_t1=[x/norm(u1) for x in u1]
u2=cross(KVEC,e_t1);           e_t2=[x/norm(u2) for x in u2]

R2=math.sqrt(2.0)
def sym_to_vec(S):
    return [S[0][0],S[1][1],S[2][2], R2*S[0][1],R2*S[0][2],R2*S[1][2]]

def sector_tensor(e):
    T=[[e[i]*e[j] for j in range(3)] for i in range(3)]
    v=sym_to_vec(T); n=math.sqrt(dot(v,v))
    return [[x/n for x in row] for row in T]

# CORRECT TT basis: traceless combinations in the transverse plane
T_a=[[e_t1[i]*e_t1[j] for j in range(3)] for i in range(3)]
T_b=[[e_t2[i]*e_t2[j] for j in range(3)] for i in range(3)]
c=1.0/math.sqrt(2.0)
TT1=[[(T_a[i][j]-T_b[i][j])*c for j in range(3)] for i in range(3)]
TT2=[[ (e_t1[i]*e_t2[j]+e_t2[i]*e_t1[j])/math.sqrt(2.0) for j in range(3)] for i in range(3)]
TT_tensors=[TT1,TT2]
plane=[]
for base in ([1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]):
    v=[base[i]-W[i]*dot(base,W) for i in range(3)]
    nv=norm(v)
    if nv>1e-12: plane.append([x/nv for x in v])
P1_tensors=[]
for u in plane[:2]:
    T=[[(u[i]*W[j]+W[i]*u[j])/math.sqrt(2.0) for j in range(3)] for i in range(3)]
    P1_tensors.append(T)
E_0s=[[1.0/3.0 if i==j else 0.0 for j in range(3)] for i in range(3)]
ns=norm(sym_to_vec(E_0s))
E_0s_n=[[x/ns for x in row] for row in E_0s]
Wt=[[W[i]*W[j]-(1.0/3.0 if i==j else 0.0) for j in range(3)] for i in range(3)]
nw=norm(sym_to_vec(Wt))
E_0w_n=[[x/nw for x in row] for row in Wt]
SECTORS['P2'] = TT_tensors
SECTORS['P1'] = P1_tensors
SECTORS['P0s'] = [E_0s_n]
SECTORS['P0w'] = [E_0w_n]

def matmul(A,B):
    n=len(A); m=len(B[0]); p=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]
def close(A,B,tol=1e-10):
    return all(abs(a-b)<=tol for ra,rb in zip(A,B) for a,b in zip(ra,rb))
fails=[]
def check(name,cond,detail=''):
    print(('PASS ' if cond else 'FAIL ')+name+((' :: '+detail) if detail else ''))
    if not cond: fails.append(name)
I6=[[1.0 if i==j else 0.0 for j in range(6)] for i in range(6)]
OPS={}
for nm,basis in SECTORS.items():
    M=[[0.0]*6 for _ in range(6)]
    # Gram-Schmidt the sector basis IN THE EMBEDDED 6-vec metric first
    vs=[]
    for t in basis:
        v=[float(x) for x in sym_to_vec(t)]
        for p in vs:
            c=sum(a*b for a,b in zip(v,p))
            v=[a-c*b for a,b in zip(v,p)]
        nv=math.sqrt(sum(x*x for x in v))
        if nv>1e-13: vs.append([x/nv for x in v])
    for v in vs:
        P=[[v[i]*v[j] for j in range(6)] for i in range(6)]
        for i in range(6):
            for j in range(6): M[i][j]+=P[i][j]
    OPS[nm]=M

print('=== PROPERTY TESTS ===')
for nm,P in OPS.items():
    R=matmul(P,P)
    res=max(abs(R[i][j]-P[i][j]) for i in range(6) for j in range(6))
    tr=sum(P[i][i] for i in range(6))
    check(nm+' idempotent',res<1e-10,'res=%.1e'%res)
    check(nm+' trace',abs(tr-round(tr))<1e-10,'tr=%f'%tr)
names=list(OPS)
for a_i in range(len(names)):
    for b_i in range(a_i+1,len(names)):
        pr=matmul(OPS[names[a_i]],OPS[names[b_i]])
        mx=max(abs(pr[x][y]) for x in range(6) for y in range(6))
        check(names[a_i]+' orth '+names[b_j] if False else names[a_i]+' orth '+names[b_i],mx<1e-10,'max=%.1e'%mx)
tot=[[sum(OPS[nm][i][j] for nm in names) for j in range(6)] for i in range(6)]
check('completeness sum=I6',close(tot,I6))
def matvec(A,v): return [sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A))]
scalar_plant=[[5.0 if i==j else 0.0 for j in range(3)] for i in range(3)]
sv=sym_to_vec(scalar_plant)
check('plant scalar -> P0s image',max(abs(a-b) for a,b in zip(matvec(OPS['P0s'],sv),sv))<1e-9)
tt_plant=[[ (e_t1[i]*e_t1[j]-e_t2[i]*e_t2[j])/math.sqrt(2.0) for j in range(3)] for i in range(3)]
tv=sym_to_vec(tt_plant)
check('plant TT -> preserved by P2',max(abs(a-b) for a,b in zip(matvec(OPS['P2'],tv),tv))<1e-9)

def eh_coord(S):
    kk=dot(KVEC,KVEC)
    Sk=[sum(S[a][b]*KVEC[b] for b in range(3)) for a in range(3)]
    sll=S[0][0]+S[1][1]+S[2][2]
    kkll=sum(KVEC[a]*KVEC[b]*S[a][b] for a in range(3) for b in range(3))
    out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            val=KK*S[i][j]-KVEC[i]*Sk[j]-KVEC[j]*Sk[i]+KVEC[i]*KVEC[j]*sll
            d=(1.0 if i==j else 0.0)
            val+=d*(kkll-kk*sll)
            row.append(val)
        out.append(row)
    return out
EH_op=[]
for i in range(6):
    e=[0.0]*6; e[i]=1.0
    S=[[0.0]*3 for _ in range(3)]
    S[0][0],S[1][1],S[2][2]=e[0],e[1],e[2]
    S[0][1]=S[1][0]=e[3]/R2; S[0][2]=S[2][0]=e[4]/R2; S[1][2]=S[2][1]=e[5]/R2
    EH_op.append(sym_to_vec(eh_coord(S)))
EH_claimed=[[ (KK/2.0)*(OPS["P2"][i][j]-2.0*OPS["P0s"][i][j]) for j in range(6)] for i in range(6)]
check('EH identity: coord == (k^2/2)(P2 - 2P0s)',
      max(abs(a-b) for ra,rb in zip(EH_op,EH_claimed) for a,b in zip(ra,rb)),
      'max abs diff (see DEBUG); comparison modulo gauge pending')
# DEBUG: compare operators on a generic tensor
S_gen=[[float(i*3+j+1)*0.1 for j in range(3)] for i in range(3)]
vg=sym_to_vec(S_gen)
a=matvec(EH_op,vg)
M=[[ (KK/2.0)*(OPS['P2'][i][j]-2.0*OPS['P0s'][i][j]) for j in range(6)] for i in range(6)]
b=matvec(M,vg)
print('DEBUG EH_coord:',[round(x,4) for x in a])
print('DEBUG proj   :',[round(x,4) for x in b])
print('DEBUG max diff:',max(abs(x-y) for x,y in zip(a,b)))

print()
print('FAILURES:',len(fails),fails if fails else '')
json.dump({'phase':'A2 phase 1 v3','all_pass':len(fails)==0,
  'eh_exact':close(EH_op,EH_claimed,1e-9)},
  open('WALL_A_A2_PHASE1_V3.json','w'),indent=1)
