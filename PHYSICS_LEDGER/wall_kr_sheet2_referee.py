"""Sheet-II referee: radius-VERIFIED stepwise Taylor continuation (every step
< 0.6 x distance to the branch point z = 4), two distinct paths as the
error certificate, then secant from BOTH candidate neighbourhoods."""
import json, sys
import mpmath as mp
import sympy as sp
sys.path.insert(0, "/Users/mpg/Desktop/GRUT ResponsiveAI/PHYSICS_LEDGER")
mp.mp.dps = 30
HERE = "/Users/mpg/Desktop/GRUT ResponsiveAI/PHYSICS_LEDGER"
class Gfun(sp.Function): nargs = 5
class Rfun(sp.Function): nargs = 5
FRZ = json.load(open(HERE + "/Sigma_R_finite_full.json"))
S0 = sp.sympify(FRZ["sectors"]["0"]["srepr"], locals={"Gfun": Gfun, "Rfun": Rfun})
om, kk, mm, muS = sp.symbols("omega k m mu", positive=True)
kap = sp.Symbol("kappa")
def Es(i,j): return sp.Symbol("E_%d%d" % (min(i,j),max(i,j)))
def Ps(i,j): return sp.Symbol("P_%d%d" % (min(i,j),max(i,j)))
sub0 = {}
for a in range(4):
    for b in range(a,4):
        sub0[Es(a,b)] = 0; sub0[Ps(a,b)] = 0
sub0[Es(1,1)] = 1; sub0[Es(2,2)] = -1; sub0[Ps(1,1)] = 1; sub0[Ps(2,2)] = -1
chi0_sym = sp.expand((sp.expand(S0.xreplace(sub0))/2).subs(kk, 0))
KAPN = sp.Float(mp.nstr(mp.log(4*mp.pi)-mp.euler, 25), 25)
def quad_atom(fam,n_,np_,e_,K2):
    K2 = mp.mpc(K2); D = lambda y: 1-y*(1-y)*K2; w = lambda y: y**n_*(1-y)**np_
    bps = [0, mp.mpf(1)/2, 1]
    if K2.imag != 0 and K2.real > 4:
        r = mp.re(mp.sqrt(1-4/K2)); bps = sorted({0,(1-r)/2,mp.mpf(1)/2,(1+r)/2,1})
    if fam == "G":
        return mp.quad(lambda y: w(y)*D(y)**e_*(-mp.log(D(y))), bps)
    return mp.quad(lambda y: w(y)*D(y)**e_, bps)
def chiI(z):
    wv = mp.sqrt(mp.mpc(z))
    s2 = {om: sp.Float(mp.nstr(mp.re(wv),22),22)+sp.Float(mp.nstr(mp.im(wv),22),22)*sp.I,
          mm: 1, muS: 1, kap: KAPN}
    e2 = chi0_sym.subs(s2); rep = {}
    for A in e2.atoms(Gfun, Rfun):
        v = quad_atom(type(A).__name__[0], int(A.args[0]), int(A.args[1]), int(A.args[2]), mp.mpc(z))
        rep[A] = sp.Float(mp.nstr(mp.re(v),25),25)+sp.Float(mp.nstr(mp.im(v),25),25)*sp.I
    return mp.mpc(complex(sp.N(e2.subs(rep), 25)))
def tcoef(f, a, r, N=18, nodes=64):
    vals = [f(a + r*mp.expjpi(2*mp.mpf(j)/nodes)) for j in range(nodes)]
    return [sum(vals[j]*mp.expjpi(-2*mp.mpf(j)*n/nodes) for j in range(nodes))/nodes/r**n
            for n in range(N)]
def pshift(cs, a, b, N=18):
    return [sum(cs[n]*mp.binomial(n,k)*(b-a)**(n-k) for n in range(k, len(cs)))
            for k in range(N)]
def peval(cs, a, z):
    return sum(c*(z-a)**n for n, c in enumerate(cs))
def continue_path(anchors):
    """verified-radius continuation; returns (final coeffs, final anchor)."""
    a0 = anchors[0]
    d0 = abs(a0 - 4)
    cs = tcoef(chiI, a0, mp.mpf("0.5")*d0)
    aa = a0
    for b in anchors[1:]:
        step = abs(b - aa); dist = abs(aa - 4)
        assert step < mp.mpf("0.62")*dist, "RADIUS VIOLATION %s -> %s (%.2f vs %.2f)" % (aa, b, step, dist)
        cs = pshift(cs, aa, b); aa = b
    return cs, aa
P1 = [mp.mpc(6, 1.2), mp.mpc(6, "0.35"), mp.mpc(6, "-0.5"), mp.mpc("5.3", "-0.85"),
      mp.mpc("4.7", "-1.25"), mp.mpc("4.0", "-1.55"), mp.mpc("3.2", "-1.6"),
      mp.mpc("2.4", "-1.4"), mp.mpc("1.7", "-1.15"), mp.mpc("1.2", "-1.0")]
P2 = [mp.mpc(6, 1.2), mp.mpc(6, "0.3"), mp.mpc("6.1", "-0.6"), mp.mpc("5.4", "-1.1"),
      mp.mpc("4.6", "-1.5"), mp.mpc("3.8", "-1.7"), mp.mpc("2.9", "-1.6"),
      mp.mpc("2.1", "-1.3"), mp.mpc("1.4", "-1.05"), mp.mpc("1.0", "-0.9")]
csA, aA = continue_path(P1)
csB, aB = continue_path(P2)
for zt in (mp.mpc("1.1", "-0.9"), mp.mpc("0.9", "-1.0")):
    va, vb = peval(csA, aA, zt), peval(csB, aB, zt)
    print("two-path certificate at %s: A=%s B=%s rel=%s"
          % (mp.nstr(zt,4), mp.nstr(va,8), mp.nstr(vb,8), mp.nstr(abs(va-vb)/abs(va),3)))
def chiII(z): return peval(csA, aA, mp.mpc(z))
for gs, seeds in (("-1", [mp.mpc("0.116","-0.945"), mp.mpc("1.08","-0.11"), mp.mpc("1.0","-0.8")]),
                  ("-2", [mp.mpc("0.711","-1.296"), mp.mpc("1.45","-0.02"), mp.mpc("1.2","-1.0")])):
    g = mp.mpf(gs)
    D = lambda z: z - g*chiII(z)
    found = []
    for s in seeds:
        z0, z1 = s + mp.mpc("0.1","0.05"), s - mp.mpc("0.08","0.06")
        try:
            for _ in range(40):
                f0, f1 = D(z0), D(z1)
                if abs(f1-f0) < mp.mpf("1e-32"): break
                z2 = z1 - f1*(z1-z0)/(f1-f0)
                z0, z1 = z1, z2
                if abs(D(z1)) < mp.mpf("1e-14"): break
            if abs(D(z1)) < mp.mpf("1e-10") and abs(mp.im(z1)) > 1e-8:
                if not any(abs(z1-f) < mp.mpf("0.02") for f in found):
                    found.append(z1)
        except Exception as e:
            print("  seed %s failed: %s" % (mp.nstr(s,3), e))
    print("g=%s: verified-radius sheet-II zeros in the searched region: %s"
          % (gs, [mp.nstr(z,6) for z in found] or "NONE"))
    print("    |D| at production candidate: %s ; at audit candidate: %s"
          % (mp.nstr(abs(D(seeds[0])),4), mp.nstr(abs(D(seeds[1])),4)))
