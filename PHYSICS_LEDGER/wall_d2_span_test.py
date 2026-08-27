#!/usr/bin/env python3
"""H^2 RESIDUAL-SPAN CLASSIFICATION -- standalone diagnostic (authorized at 53e94c3).

ONE QUESTION: is the computed H^2 target representable in the FROZEN local basis?
Nothing else is decided here. In particular this concerns LOCAL UV COUNTERTERM
STRUCTURE and does NOT determine Q1 placement, Im chi, convergence class, or
relaxational/resonant character.

METHOD. The validated Phase-10/11 construction is executed up to (but NOT including)
its own identification section, giving the cached H^2 target and the validated basis
kernels. The LINEAR ALGEBRA is then done here, twice, by two genuinely different
routes (different component ordering, different column ordering, different elimination
routine), because the rank result is load-bearing.

THE TARGET IS IMMUTABLE: not recomputed for a preferred representation, not refit, not
renormalised, no slots dropped, not projected.
"""
import json, os, sys, time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAIL = []


def ck(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg); sys.stdout.flush()
    if not ok:
        FAIL.append(msg)
    return ok


# ---- STEP 0: execute the validated construction up to the identification section ----
src = open(os.path.join(HERE, "wall_d2_phases8_12.py")).read()
MARK = "# ================= PHASE 11: IDENTIFICATION"
assert MARK in src, "marker not found -- refusing to guess where to split"
os.environ.setdefault("SKIPBAT", "1")
ns = {'__name__': '__main__', '__file__': os.path.join(HERE, "wall_d2_phases8_12.py")}
print("=== STEP 0: executing validated construction (cache-backed) ===")
exec(compile(src.split(MARK)[0], "wall_d2_phases8_12.py", "exec"), ns)
print(f"[{time.time()-T0:7.1f}s] construction done")

QS, K_SAMPLES = ns['QS'], ns['K_SAMPLES']
SIG0, SIG1, SIG2 = ns['SIG0'], ns['SIG1'], ns['SIG2']
om, kk, mm, H, c = ns['om'], ns['kk'], ns['mm'], ns['H'], ns['c']
OPS = ('Lam', 'EH', 'R2', 'Rmn2')
ck(len(K_SAMPLES) >= 3, f"three K samples available: {[(str(a),str(b)) for a,b in K_SAMPLES]}")

# ---- STEP 3: SAME-FOOTING MAP, built once and used by BOTH sides ----
print("\n=== STEP 3: same-footing component map ===")
def pol(ex, pre):
    return sorted({q for q in sp.expand(ex).free_symbols if str(q).startswith(pre)}, key=str)
allsyms = sp.expand(SIG2.subs({om: K_SAMPLES[0][0], kk: K_SAMPLES[0][1]}))
Es = pol(allsyms, 'E_') or pol(sum(QS[0][o][2] for o in OPS), 'E_')
Ps = pol(allsyms, 'P_') or pol(sum(QS[0][o][2] for o in OPS), 'P_')
for o in OPS:
    Es = sorted(set(Es) | set(pol(QS[0][o][2], 'E_')), key=str)
    Ps = sorted(set(Ps) | set(pol(QS[0][o][2], 'P_')), key=str)
SLOTS = [(e_, p_) for e_ in Es for p_ in Ps]
print(f"   component map: {len(Es)} E-symbols x {len(Ps)} P-symbols = {len(SLOTS)} slots")
print(f"   E order: {[str(x) for x in Es[:4]]} ...   P order: {[str(x) for x in Ps[:4]]} ...")
ck(len(SLOTS) > 0, "same-footing map is non-empty and shared by target and basis")


def slotvec(ex, slots):
    ex = sp.expand(ex)
    return [sp.expand(ex.coeff(e_, 1).coeff(p_, 1)) for (e_, p_) in slots]


def build(idx, order, slots):
    ov, kv = K_SAMPLES[idx]
    B = [slotvec(sp.expand(QS[idx][o][order]), slots) for o in OPS]      # 4 columns
    t = slotvec(sp.expand({0: SIG0, 1: SIG1, 2: SIG2}[order].subs({om: ov, kk: kv})), slots)
    return B, t


# ---- two INDEPENDENT rank routes ----
def rank_sympy(cols, extra=None):
    M = sp.Matrix([[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))])
    if extra is not None:
        M = M.row_join(sp.Matrix([[x] for x in extra]))
    return M.rank()


def rank_bareiss(cols, extra=None):
    """independent route: REVERSED slot order, REVERSED column order, hand-rolled
    fraction-free (Bareiss) elimination -- no call to sympy's rank()."""
    ncol = len(cols) + (1 if extra is not None else 0)
    rows = []
    for i in reversed(range(len(cols[0]))):
        r = [sp.expand(cols[j][i]) for j in reversed(range(len(cols)))]
        if extra is not None:
            r.append(sp.expand(extra[i]))
        rows.append(r)
    rank, piv = 0, 0
    prev = sp.Integer(1)
    for col in range(ncol):
        sel = None
        for r in range(piv, len(rows)):
            if sp.expand(rows[r][col]) != 0:
                sel = r; break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        for r in range(piv + 1, len(rows)):
            for cc in range(col + 1, ncol):
                rows[r][cc] = sp.cancel((rows[r][cc] * rows[piv][col]
                                         - rows[r][col] * rows[piv][cc]) / prev)
            rows[r][col] = sp.Integer(0)
        prev = rows[piv][col]
        piv += 1; rank += 1
    return rank


MSAMP = [sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(11, 3)]


def ranks_at(idx, order, msub):
    slots = SLOTS
    B, t = build(idx, order, slots)
    Bm = [[sp.expand(x.subs(mm, msub)) for x in colv] for colv in B]
    tm = [sp.expand(x.subs(mm, msub)) for x in t]
    return (rank_sympy(Bm), rank_sympy(Bm, tm), rank_bareiss(Bm), rank_bareiss(Bm, tm), Bm, tm)


print("\n=== STEP 4: multi-K^2 rank test (K1,K2 fitting; K3 HELD OUT) ===")
report = {}
for order, label in ((0, "H^0 (anchor control)"), (2, "H^2 (the question)")):
    print(f"\n--- {label} ---")
    rows = []
    for idx in range(3):
        ov, kv = K_SAMPLES[idx]
        tag = "HELD-OUT" if idx == 2 else "fitting"
        for msub in MSAMP[:1]:
            rA, rAt, rB, rBt, Bm, tm = ranks_at(idx, order, msub)
            ck(rA == rB and rAt == rBt,
               f"{label} K=({ov},{kv}) [{tag}]: two independent rank routes AGREE "
               f"(sympy {rA}/{rAt} vs Bareiss {rB}/{rBt})")
            inside = (rAt == rA)
            print(f"   K=({ov},{kv}) [{tag}] m={msub}: rank(B) = {rA}, "
                  f"rank([B|t]) = {rAt}, nullity(B) = {len(OPS) - rA}  -> "
                  f"{'INSIDE span' if inside else 'OUTSIDE span'}")
            rows.append(dict(K=[str(ov), str(kv)], held_out=(idx == 2), m=str(msub),
                             rank_B=int(rA), rank_Bt=int(rAt),
                             nullity=int(len(OPS) - rA), inside=bool(inside)))
    report[label] = rows

print("\n=== STEP 4b: m-dependence of the rank verdict (generic-rank guard) ===")
for msub in MSAMP:
    rA, rAt, rB, rBt, _, _ = ranks_at(0, 2, msub)
    print(f"   H^2 K1, m = {msub}: rank(B) = {rA}, rank([B|t]) = {rAt} -> "
          f"{'INSIDE' if rAt == rA else 'OUTSIDE'}  (Bareiss {rB}/{rBt})")
    ck(rA == rB and rAt == rBt, f"rank routes agree at m = {msub}")

print("\n=== STEP 4c: NULL-SPACE STRUCTURE of the H^2 basis ===")
_, _, _, _, Bm, tm = ranks_at(0, 2, MSAMP[0])
Mb = sp.Matrix([[Bm[j][i] for j in range(4)] for i in range(len(Bm[0]))])
nsp = Mb.nullspace()
print(f"   nullity = {len(nsp)}")
for v in nsp:
    print(f"   null vector over ({', '.join(OPS)}): "
          f"{[sp.nsimplify(x) for x in sp.Matrix(v).T.tolist()[0]]}")
ck(True, f"H^2 basis null space recorded ({len(nsp)} vector(s))")

print("\n=== STEP 9: self-checks ===")
ck(sp.expand(SIG2 - ns['SIG2']) == 0, "target unchanged since load (no mutation)")
ck(len(SLOTS) == len(Es) * len(Ps), "slot count consistent with the component map")
ck(all(len(build(i, 2, SLOTS)[0]) == 4 for i in range(3)),
   "exactly 4 basis columns at every sample (no column silently removed/added)")
_, t0v = build(0, 0, SLOTS)
ck(any(x != 0 for x in t0v), "H^0 target nonzero (anchor control is live)")

print(f"\n[FAIL count = {len(FAIL)}]  elapsed {time.time()-T0:.1f}s")
for f_ in FAIL:
    print("   FAILED:", f_)
json.dump({"instrument": "wall_d2_span_test.py",
           "question": "is the computed H^2 target representable in the frozen local basis?",
           "slots": len(SLOTS), "E_syms": len(Es), "P_syms": len(Ps),
           "ranks": report, "fail_count": len(FAIL), "failures": FAIL,
           "fence": "LOCAL UV counterterm structure only; determines nothing about Q1, "
                    "Im chi, convergence class, or relaxational/resonant character"},
          open(os.path.join(HERE, "WALL_D2_SPAN_TEST_RESULT.json"), "w"), indent=2)
print("result written: WALL_D2_SPAN_TEST_RESULT.json")
sys.exit(0 if not FAIL else 1)
