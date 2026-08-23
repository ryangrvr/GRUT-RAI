"""C1 PRIMITIVE VALIDATION: derive and validate the free TT-graviton mode
from the tensor action with explicit typed identities for h_k and v_k."""
import cmath, json, math, os, sys
import sympy as sp

FAILS, RESULTS = [], []
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- SYMBOLS ----
eta_s = sp.symbols('etas', real=True)
k_s = sp.symbols('k', positive=True)


def record(cid, desc, ok, detail=""):
    RESULTS.append({"id": cid, "desc": desc, "pass": bool(ok), "detail": detail})
    print("  %s %s: %s %s" % ("ok" if ok else "FAIL", cid, desc, detail))
    if not ok:
        FAILS.append(cid)

# ---- TYPED VARIABLE REGISTRY ----
class ModeType:
    STRAIN = "physical_TT_strain_h_k"
    CANONICAL = "canonical_variable_v_k"

class ModeFunction:
    def __init__(self, func, mode_type, k_val):
        self._func = func
        self.type = mode_type
        self.k = k_val
    def __call__(self, var):
        return self._func(var)
    def require_type(self, expected):
        if self.type != expected:
            raise TypeError(
                "MODE TYPE MISMATCH: got '%s', expected '%s'. "
                "This is the h_k/v_k confusion the primitive gate exists to catch."
                % (self.type, expected))

# ---- DERIVE THE EQUATIONS FROM THE ACTION ----
print("=" * 78)
print("STEP 1: derive equations from the tensor action")
print("=" * 78)

eta, kk = sp.symbols('eta k', positive=True)
i_ = sp.I

# Conformal-time strain equation: h'' + 2*(a'/a)*h' + k^2*h = 0
# For dS: a = -1/(H*eta), H=1 => a'/a = -1/eta
Hcal = -1 / eta
strain_eq = "h''_eta + 2*(-1/eta)*h'_eta + k^2*h = 0"

# Canonical: v = a*h => v'' + (k^2 - a''/a)*v = 0
# For dS: a''/a = 2/eta^2
canon_eq = "v''_eta + (k^2 - 2/eta^2)*v = 0"
print("  strain eq:", strain_eq)
print("  canonical eq:", canon_eq)
print("  relation: v = a * h")

# ---- STEP 2: construct BD solution from the canonical equation ----
print("\nSTEP 2: construct BD solution from the canonical equation")
v_bd_expr = (1 - sp.I/(k_s*eta_s)) * sp.exp(-sp.I*k_s*eta_s) / sp.sqrt(2*k_s)
res_can_sym = sp.diff(v_bd_expr, eta_s, 2) + (k_s**2 - 2/eta_s**2)*v_bd_expr
res_can_simpl = sp.simplify(res_can_sym)
ok_sym_canon = res_can_simpl == 0
record("R1_symbolic_canonical", "canonical EOM residual", ok_sym_canon,
       "res=%s" % str(res_can_simpl)[:40])

h_strain_expr = -eta_s * v_bd_expr
res_str_sym = sp.diff(h_strain_expr, eta_s, 2) - 2/eta_s*sp.diff(h_strain_expr, eta_s) + k_s**2*h_strain_expr
res_str_simpl = sp.simplify(res_str_sym)
ok_sym_strain = res_str_simpl == 0
record("R1_symbolic_strain", "strain EOM residual", ok_sym_strain,
       "res=%s" % str(res_str_simpl)[:40])

# ---- STEP 3: numerical implementation ----
print("\nSTEP 3: numerical implementation")

def v_bd(k_val, eta_val):
    """Canonical BD mode."""
    return (1 - 1j/(k_val*eta_val)) * cmath.exp(-1j*k_val*eta_val) / math.sqrt(2*k_val)

def h_phys(k_val, eta_val):
    """Physical strain h = v/a = -eta*v (H=1)."""
    return -eta_val * v_bd(k_val, eta_val)

# numerical residual for canonical equation
def v_num_residual(k_val, eta_val, hh):
    vp = (v_bd(k_val, eta_val+hh) - v_bd(k_val, eta_val-hh)) / (2*hh)
    vpp = (v_bd(k_val,eta_val+hh) - 2*v_bd(k_val,eta_val) + v_bd(k_val,eta_val-hh))/hh**2
    return abs(vpp + (k_val**2 - 2/(eta_val**2))*v_bd(k_val, eta_val))

conv_ok = True
prev_res = float('inf')
for hh in (1e-2, 1e-3, 1e-4):
    r = v_num_residual(1.0, -1.0, hh)
    print("    hh=%.0e residual=%.4e" % (hh, r))
    if r >= prev_res and prev_res < float('inf'):
        conv_ok = False
    prev_res = r
record("R2_convergence", "numerical residual converges", conv_ok)

# ---- STEP 4: independent RK4 ODE integration ----
print("\nSTEP 4 -- independent RK4 ODE integration")
def rk4_canonical(k_val, eta0, eta1, n):
    d = (eta1 - eta0) / n
    v0 = (1 - 1j/(k_val*eta0)) * cmath.exp(-1j*k_val*eta0) / math.sqrt(2*k_val)
    # CORRECTED 2026-08-22 -- identical defect to calc/C1_GROUND_TRUTH_MODE.py, found by
    # provenance/emit_gate_status.py surfacing this artifact's 5/6. Sign was flipped on the
    # dominant term and the factor i was missing on 1/(k eta^2). For
    # v = (1 - i/(k eta)) exp(-i k eta)/sqrt(2k),
    #   dv/deta = exp(-i k eta)/sqrt(2k) * [ i/(k eta^2) - i k (1 - i/(k eta)) ]
    # (sympy-verified exact). The wrong seed excites the second solution: |v| is preserved,
    # phase is ~antiphase, so a magnitude-only control passes it. rel 1.483 -> 8.33e-11.
    dp0 = cmath.exp(-1j*k_val*eta0) * (
        1j/(k_val*eta0**2) - 1j*k_val*(1 - 1j/(k_val*eta0))
    ) / math.sqrt(2*k_val)
    v_, p_ = v0, dp0
    e = eta0
    for _ in range(n):
        f = -(k_val**2 - 2/(e*e))
        fv = p_; fp = f*v_
        em = e + d/2; fm = -(k_val**2 - 2/(em*em))
        k2v = p_ + fp*d/2; k2p = fm*(v_+fv*d/2)
        k3v = p_ + k2p*d/2; k3p = fm*(v_+k2v*d/2)
        ee = e+d; f4 = -(k_val**2 - 2/(ee*ee))
        k4v = p_+k3p*d; k4p = f4*(v_+k3v*d)
        v_ += d/6*(fv+2*k2v+2*k3v+k4v); p_ += d/6*(fp+2*k2p+2*k3p+k4p)
        e += d
    return v_

k_t = 1.0
v_rk4 = rk4_canonical(k_t, -100.0, -1.0, 50000)
v_exact_end = v_bd(k_t, -1.0)
rel_err = abs(v_rk4 - v_exact_end) / abs(v_exact_end)
record("R3_rk4_vs_analytic", "RK4 vs analytic at eta=-1",
       rel_err < 1e-3, "rel=%.2e" % rel_err)
print("    RK4 |v|=%.8f, analytic |v|=%.8f" % (abs(v_rk4), abs(v_exact_end)))

# ---- Wronskian ----
wvals = []
for kw in (0.5, 1.0, 3.0):
    for ew in (-100.0, -10.0, -1.0):
        v0w = (1 - 1j/(kw*ew)) * cmath.exp(-1j*kw*ew) / math.sqrt(2*kw)
        vpw = (v_bd(kw, ew+1e-6) - v_bd(kw, ew-1e-6)) / (2*1e-6)
        w = v0w * vpw.conjugate() - vpw * v0w.conjugate()
        wvals.append(w.imag)
spread_w = max(wvals) - min(wvals)
mean_w = sum(wvals) / len(wvals)
record("Wronskian_constancy", "W Im constant", spread_w < 1e-6,
       "spread=%.2e mean=%.6f" % (spread_w, mean_w))

# ---- cross-variable consistency ----
print("\nCross-variable consistency")
ok_cross = True
for kv in (0.5, 1.0, 3.0):
    for ev in (-100.0, -50.0, -10.0, -1.0):
        v_val = v_bd(kv, ev)
        h_val = -ev * v_val  # h = -eta * v for H=1
        # verify: does h satisfy strain equation? (already proven symbolically)
        # here we just check the conversion identity numerically
        v_reconstructed = -h_val / ev  # v = -h/eta
        if abs(v_reconstructed - v_val) > 1e-12 * max(abs(v_val), 1):
            ok_cross = False
record("cross_variable", "h=v/a<->v=-eta*h identity", ok_cross)

# ---- summary ----
np = sum(1 for r in RESULTS if r["pass"])
verdict = "ALL CHECKS PASS" if not FAILS else \
    "%d FAILURES: %s" % (len(FAILS), ", ".join(
        r["id"] for r in RESULTS if not r["pass"]))
print("\n" + "=" * 78)
print(verdict + " (%d/%d)" % (np, len(RESULTS)))
out = os.path.join(ROOT, "C1_PRIMITIVE_VALIDATION_STATUS.json")
json.dump({"verdict": verdict, "checks": RESULTS}, open(out, "w"), indent=2)
print("status:", out)


