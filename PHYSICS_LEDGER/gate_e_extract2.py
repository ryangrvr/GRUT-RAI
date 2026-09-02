import json, sympy as sp, time, gc, random
t0 = time.time()
def stamp(m):
    print("[%6.0fs] %s" % (time.time()-t0, m), flush=True)
u, up, ub, D = sp.symbols("u u_p u_b Delta", real=True)
H = sp.Symbol("H", real=True); q = sp.Symbol("q", positive=True)
src = open("wall_kr_tier3_loop.py").read()
i0 = src.find("def _exp_arg_of_factors"); i1 = src.find("\nWIG =")
g = {"sp": sp, "D": D, "ub": ub, "q": q}
exec(src[i0:i1], g)
IC = json.loads(open(".tier3_integrand_cache.json").read())
stamp("cache loaded")
SG = sp.sympify(IC["sig_g"]); SL = sp.sympify(IC["sig_l"])
NK = sp.sympify(IC["nk_wigner"])
stamp("sympified")
# run-2 finding (mine): sig_g/sig_l are cached in (u, u') variables
# while nk_wigner is in Wigner variables (u_b, Delta) -- the run-2
# "identity failure" and the cone_split "unrecognized phase
# -2iqu + 2iqu'" were BOTH this frame mismatch, not physics.
# Transform to the common Wigner frame first: u = ub + D/2, u' = ub - D/2
WIGSUB = {u: ub + D/2, up: ub - D/2}
SG = sp.expand(SG.subs(WIGSUB)); SL = sp.expand(SL.subs(WIGSUB))
stamp("sig_g/sig_l transformed to the Wigner frame")
# identity nk == sg + sl: NUMERIC spot-check at 6 random points (the
# full symbolic expand caused the run-1 memory death; numeric at
# rational points is exact enough at 30+ digits, 6 points, all symbols)
syms = sorted((NK.free_symbols | SG.free_symbols | SL.free_symbols),
              key=str)
random.seed(7)
ok_id = True
for t in range(6):
    sub = {s: sp.Rational(random.randint(2, 60), random.randint(2, 60))
           for s in syms}
    r = complex((NK - SG - SL).evalf(30, subs=sub))
    ref = max(1e-30, abs(complex(NK.evalf(30, subs=sub))))
    if abs(r) / ref > 1e-22:
        ok_id = False
        stamp("identity FAILS at point %d: rel %.2e" % (t, abs(r)/ref))
stamp("identity nk == sg + sl (numeric, 6 pts): %s" % ok_id)
out = {"id_nk": bool(ok_id), "id_nk_method": "numeric 6-point exact-rational spot check at 30 digits, in the COMMON Wigner frame (run-2 frame-mismatch disclosed; run-1 symbolic expand exhausted memory)"}
del NK; gc.collect()
for name, X in (("sg", SG), ("sl", SL)):
    E = sp.expand(X)
    for n in (0, 1, 2):
        cn = E.coeff(H, n) if n else E.subs(H, 0)
        c = g["cone_split"](sp.expand(cn))
        cm = sp.cancel(sp.together(c["m"]))
        cp = sp.cancel(sp.together(c["p"]))
        out["%s_H%d_m" % (name, n)] = sp.srepr(cm)
        out["%s_H%d_p" % (name, n)] = sp.srepr(cp)
        out["%s_H%d_stray" % (name, n)] = str(c["stray"])
        stamp("%s H^%d: m %s | p %s | stray %s" % (
            name, n, "0" if cm == 0 else "NONZERO",
            "0" if cp == 0 else "NONZERO", c["stray"]))
        json.dump(out, open(".gate_e_cones.json", "w"))
        del cn, c, cm, cp; gc.collect()
    del E; gc.collect()
stamp("DONE")
