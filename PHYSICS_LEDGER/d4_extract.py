import json, sympy as sp, time, gc
t0 = time.time()
def stamp(m): print("[%6.0fs] %s" % (time.time()-t0, m), flush=True)
T1 = json.loads(open("WALL_KR_TIER1_VERTEX_ARTIFACT.json").read())
V = sp.sympify(T1["ds_vertex_srepr"])
H = sp.Symbol("H"); u = sp.Symbol("u")
V = V.xreplace({sp.Symbol("H"): H, sp.Symbol("u"): u})
stamp("dS vertex loaded: %d terms" % len(sp.Add.make_args(V)))
w = sp.Symbol("omega", positive=True)
q = sp.Symbol("q", positive=True)
nu1, nu2 = sp.symbols("nu1 nu2")
X = sp.symbols("X0 X1 X2 X3")
t11, t12, t13, t22, t23, t33 = sp.symbols("t11 t12 t13 t22 t23 t33")
dd = sp.Symbol("d", positive=True)

def entries(tag, mat):
    sub = {}
    for m_ in range(4):
        for n_ in range(m_, 4):
            sub[sp.Symbol("e%s_%d%d" % (tag, m_, n_))] = mat[m_][n_]
    return sub

def run_case(name, nvec, e2_mat, e3_mat, e1_mat):
    sub = {}
    sub.update(entries("1", e1_mat))
    sub.update(entries("2", e2_mat))
    sub.update(entries("3", e3_mat))
    # momenta: p1=(w,0,0,0); p2=(nu1, q nvec); p3=(nu2, -q nvec)
    for c, val in (("p1", [w, 0, 0, 0]),
                   ("p2", [nu1] + [q * nv for nv in nvec]),
                   ("p3", [nu2] + [-q * nv for nv in nvec])):
        for m_ in range(4):
            sub[sp.Symbol("%s_%d" % (c, m_))] = val[m_]
    r = V.xreplace(sub)
    r = sp.expand(r)
    r = sp.simplify(sp.expand(r)) if len(sp.Add.make_args(r)) < 4000 \
        else sp.expand(r)
    return r

def tt_proj_mat(nvec, tsyms):
    # spatial TT projection of generic symmetric t about unit nvec,
    # trace removal with symbolic (d-1)
    tmat = [[0]*3 for _ in range(3)]
    tm = {(0,0):tsyms[0],(0,1):tsyms[1],(0,2):tsyms[2],
          (1,1):tsyms[3],(1,2):tsyms[4],(2,2):tsyms[5]}
    def t_(i,j): return tm[(min(i,j),max(i,j))]
    P = [[(1 if i==j else 0) - nvec[i]*nvec[j] for j in range(3)]
         for i in range(3)]
    Pt = [[sum(P[i][k_]*P[j][l_]*t_(k_,l_) for k_ in range(3)
               for l_ in range(3)) for j in range(3)] for i in range(3)]
    trPt = sum(P[k_][l_]*t_(k_,l_) for k_ in range(3) for l_ in range(3))
    M = [[0]*4 for _ in range(4)]
    for i in range(3):
        for j in range(3):
            M[i+1][j+1] = sp.expand(Pt[i][j] - P[i][j]*trPt/(dd-1))
    return M

def gauge_img_mat(kvec4, Xs):
    M = [[0]*4 for _ in range(4)]
    for m_ in range(4):
        for n_ in range(4):
            M[m_][n_] = sp.I*(kvec4[m_]*Xs[n_] + kvec4[n_]*Xs[m_])
    return M

def plus_z_mat():
    M = [[0]*4 for _ in range(4)]
    M[1][1] = 1; M[2][2] = -1
    return M

def trace_mat():
    M = [[0]*4 for _ in range(4)]
    for i in (1,2,3): M[i][i] = 1
    return M

OUT = {}
CASES = []
# direction z (symbolic-clean) and one skew rational direction
z = [0,0,1]
sk = [sp.Rational(2,7), sp.Rational(3,7), sp.Rational(6,7)]  # |sk|=1
for tag, nvec in (("z", z), ("skew", sk)):
    p2vec4 = [nu1] + [q*nv for nv in nvec]
    CASES += [
      ("MAIN_%s" % tag,      nvec, gauge_img_mat(p2vec4, X),
       tt_proj_mat(nvec, (t11,t12,t13,t22,t23,t33)), plus_z_mat()),
      ("CTRL_trace_%s" % tag, nvec, trace_mat(),
       tt_proj_mat(nvec, (t11,t12,t13,t22,t23,t33)), plus_z_mat()),
      ("CTRL_asym_%s" % tag, nvec,
       [[sp.I*p2vec4[m_]*X[n_] for n_ in range(4)] for m_ in range(4)],
       tt_proj_mat(nvec, (t11,t12,t13,t22,t23,t33)), plus_z_mat()),
    ]
for name, nvec, e2m, e3m, e1m in CASES:
    r = run_case(name, nvec, e2m, e3m, e1m)
    rH = {n_: sp.simplify(sp.expand(sp.expand(r).coeff(H, n_) if n_
          else sp.expand(r).subs(H, 0))) for n_ in (0,1,2)}
    OUT[name] = {("H%d" % n_): sp.srepr(rH[n_]) for n_ in (0,1,2)}
    OUT[name + "_zero"] = {("H%d" % n_): bool(rH[n_] == 0)
                           for n_ in (0,1,2)}
    stamp("%s: H0 %s | H1 %s | H2 %s" % (name,
          "ZERO" if rH[0]==0 else "NONZERO",
          "ZERO" if rH[1]==0 else "NONZERO",
          "ZERO" if rH[2]==0 else "NONZERO"))
    json.dump(OUT, open(".d4_vertex_gauge.json","w"))
    gc.collect()
stamp("DONE")
