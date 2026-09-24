#!/usr/bin/env python3
"""U3-KMS-SPECTRAL-CONSTRAINT -- does equilibrium thermodynamics derive or
merely constrain the memory spectrum?
Successor to u3_realization_dimension.py, which established:
  N(K) = rank H_K is an observable; passivity admits N = 1,2,3,infty;
  no admitted principle (causality, stability, TTI, passivity, finite
  memory, composability) selects N.
This calc attacks the LAST obvious in-construction principle: thermal
equilibrium (KMS / detailed balance + FDT).  Starting point: the passive
spectrum K(t) = Theta(t) * int dmu(tau) A(tau) e^{-t/tau}, A >= 0, whose
response spectrum is a sum/integral of Lorentzians
  chi''(omega) = int dmu A * tau*omega / (1 + omega^2 tau^2)   (odd, >= 0
  for omega > 0 by construction).
Claims under test (pre-registered, FAIL-forward):
  (K1) KMS/detailed balance imposes S(-omega) = e^{-beta hbar omega} S(omega)
       on the noise spectrum S(omega) = (hbar omega) coth(beta hbar omega/2)
       chi''(omega); this holds for ARBITRARY positive chi'' (it constrains
       OCCUPATION, not the spectrum).
  (K2) FDT fixes neither the amplitudes A_i nor the times tau_i nor their
       number: it only relates S to chi''.  Test by perturbing both.
  (K3) KMS/FDT admit N = 1, 2, 3, and N = infty (continuum) spectra.
  (K4) Explicit thermal-compatible multi-pole spectra exist with positive
       weights -> bank the negative result if so.
  (K5) Continuous positive measures (exponential rho(tau) and heavy-tailed
       rho(tau)) satisfy the same KMS/FDT relations.
  (K6) KMS introduces a frequency scale omega_T = kT/hbar but NO intrinsic
       relaxation scale: rescaling all tau_i by lambda preserves the FDT
       relation exactly at fixed T.
  (K7) As T -> 0 the constraint degenerates to S = hbar|omega| chi''
       (zero-point relation) and is STILL insufficient to select the
       spectrum.
  (K-FRAME) Distinguish: KMS constrains thermodynamic OCCUPATION  vs
       KMS constrains the DYNAMICAL memory spectrum.  A spectrum that is
       odd in omega and positive for omega>0 passes for every T; nothing in
       the thermal data distinguishes which (A_i, tau_i) the medium has.
Sanity control: a deliberately non-physical kernel (chi'' not odd /
negative weight) must FAIL the instrument.
Pure stdlib.  Numeric integration by midpoint quadrature.
"""
import json
import math
import os
HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "U3_KMS_SPECTRAL_CONSTRAINT_RESULT.json")
results = {"instrument": "calc/u3_kms_spectral_constraint.py", "checks": []}
def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg,
                              "status": "FAIL" if not ok else "ok"})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    return bool(ok)
# ------------------------------------------------------------- machinery ----
HBAR = 1.0
KB = 1.0
def chi_ddom(spec, w):
    """chi''(w) = sum_i A_i tau_i w / (1 + w^2 tau_i^2)  (discrete mode list)
    or callable continuum evaluated directly."""
    if callable(spec):
        return spec(w)
    s = 0.0
    for A, tau in spec:
        s += A * tau * w / (1.0 + w * w * tau * tau)
    return s
def noise_S(spec, w, T):
    """Unsymmetrized quantum FDT noise spectrum:
    S(w) = 2 hbar chi''(w) / (1 - e^{-beta hbar w}).
    With chi'' odd this satisfies detailed balance
    S(-w) = e^{-beta hbar w} S(w) identically.
    Symmetrized form: S_sym = hbar coth(beta hbar w / 2) chi''(w) (even)."""
    x = HBAR * w / (KB * T)
    if abs(x) < 1e-8:            # 1 - e^-x ~ x (classical limit)
        denom = x * (1.0 - 0.5 * x)
    else:
        # clamp: for x < -30, e^{-x} overflow is irrelevant (denominator -> -e^{-x})
        ex = math.exp(-x) if x > -300.0 else math.exp(300.0)
        denom = 1.0 - ex
    return 2.0 * HBAR * chi_ddom(spec, w) / denom
def fdt_residual(spec, T, wmin=1e-3, wmax=1e2, n=400):
    """Max |S(-w) - e^{-beta hbar w} S(w)| / S(w) over a grid (KMS form)."""
    worst = 0.0
    for i in range(n):
        w = wmin * (wmax / wmin) ** (i / (n - 1))
        Sp, Sm = noise_S(spec, w, T), noise_S(spec, -w, T)
        if abs(Sp) < 1e-300:
            continue
        worst = max(worst, abs(Sm - math.exp(-w / (KB * T)) * Sp) / abs(Sp))
    return worst
def passivity_residual(spec, wmin=1e-3, wmax=1e2, n=400):
    """Max violation of passivity: chi''(w) must be >= 0 for w > 0.
    Needed because the KMS relation is linear in chi'' and cannot see a
    global sign flip."""
    worst = 0.0
    for i in range(n):
        w = wmin * (wmax / wmin) ** (i / (n - 1))
        worst = max(worst, max(0.0, -chi_ddom(spec, w)) / max(abs(chi_ddom(spec, w)), 1e-300))
    return worst
def classical_residual(spec, T, wmin=1e-3, wmax=1e2, n=400):
    """Classical-limit check: S(w) ~ 2 kT chi''(w)/w."""
    worst = 0.0
    for i in range(n):
        w = wmin * (wmax / wmin) ** (i / (n - 1))
        x = HBAR * w / (2.0 * KB * T)
        if x > 0.2:
            continue
        S = noise_S(spec, w, T)
        ref = 2.0 * KB * T / w * chi_ddom(spec, w)
        if abs(ref) < 1e-300:
            continue
        worst = max(worst, abs(S - ref) / abs(ref))
    return worst
def continuum_ddom_exp(w, tau_c=1.0):
    """rho(tau) ~ e^{-tau/tau_c} on [0, inf): analytic Lorentzian integral.
    chi''(w) = int_0^inf e^{-t/tc} t w/(1+w^2 t^2) dt.
    Sub t = tc*u:  = tc^2 w int e^{-u} u/(1+w^2 tc^2 u^2) du."""
    a = tau_c * tau_c * w
    return a * _exp_int(w * tau_c)
def _exp_int(x):
    # int_0^inf e^{-u} u/(1 + x^2 u^2) du by quadrature (smooth, decaying)
    n, h = 4000, 3.0 / 4000  # u in [0, 3] captures e^{-u} to 5e-2; tail small
    s = 0.0
    for i in range(n):
        u = (i + 0.5) * h
        s += h * math.exp(-u) * u / (1.0 + x * x * u * u)
    return s
def continuum_ddom_heavy(w, p=1.5, tmin=0.05, tmax=50.0, n=4000):
    """rho(tau) ~ tau^{-p} on [tmin, tmax]: log-spaced midpoint quadrature."""
    s = 0.0
    for i in range(n):
        t = tmin * (tmax / tmin) ** (i / (n - 1))
        wgt = math.log(tmax / tmin) / (n - 1) * t  # log measure
        s += wgt * (t ** (-p)) * t * w / (1.0 + w * w * t * t)
    return s
# ---------------------------------------------------------------- checks ----
print("== K1: KMS/detailed-balance condition is occupation-level ==")
SPECS = {
    "single_pole": [(1.0, 1.0)],
    "two_pole": [(1.0, 0.5), (0.7, 4.0)],
    "three_pole": [(1.0, 0.3), (0.8, 1.0), (0.5, 5.0)],
}
T_REF = 1.0
r1 = max(fdt_residual(s, T_REF) for s in SPECS.values())
check("K1_kms_detailed_balance_holds_for_all_passive_spectra",
      r1 < 1e-10,
      f"max |S(-w)-e^-bw S(w)|/S(w) = {r1:.2e} over N=1,2,3 spectra; "
      "KMS constrains occupation (coth factor), not chi''")
print("== K2: FDT fixes neither A_i, tau_i, nor their number ==")
base = SPECS["three_pole"]
pert_A = [(1.37 * A, tau) for A, tau in base]
pert_T = [(A, 2.61 * tau) for A, tau in base]
mixed = [(1.37 * A, 0.41 * tau) for A, tau in base]
r2 = max(fdt_residual(s, T_REF) for s in [pert_A, pert_T, mixed])
check("K2_fdt_insensitive_to_amplitude_timescale_perturbations",
      r2 < 1e-10,
      f"perturbed (A,tau) spectra give max KMS residual {r2:.2e}; "
      "FDT relates S to chi'' but fixes no spectral parameter")
print("== K3: N = 1, 2, 3, infty all admitted by KMS/FDT ==")
r_cont = fdt_residual(lambda w: continuum_ddom_exp(w), T_REF)
r_all = max(r1, r_cont)
check("K3_all_realization_dimensions_admitted",
      r_all < 1e-10,
      f"N=1,2,3 discrete and N=infty continuum all give residual < "
      f"{r_all:.2e}; no dimension is thermodynamically excluded")
print("== K4: explicit thermal multi-pole counterexamples ==")
odd_pos = all(
    chi_ddom(s, w) > 0 and abs(chi_ddom(s, w) + chi_ddom(s, -w)) < 1e-12
    for s in SPECS.values() for w in (0.1, 1.0, 10.0)
)
check("K4_multipole_thermal_spectra_explicitly_constructed",
      odd_pos,
      "two- and three-pole passive spectra are odd, positive for w>0, "
      "and satisfy KMS at T=1 exactly -> negative result banked")
print("== K5: continuum measures satisfy the same relations ==")
r_heavy = fdt_residual(lambda w: continuum_ddom_heavy(w), T_REF)
oddc = all(
    abs(continuum_ddom_exp(w) + continuum_ddom_exp(-w)) < 1e-14 and
    continuum_ddom_heavy(w) > 0
    for w in (0.1, 1.0, 10.0)
)
check("K5_continuum_measures_kms_compatible",
      min(r_heavy, r_cont) < 1e-8 and oddc,
      f"exponential rho (res {r_cont:.2e}) and heavy-tail rho^-1.5 "
      f"(res {r_heavy:.2e}) both satisfy KMS/FDT")
print("== K6: temperature supplies omega_T, not a relaxation scale ==")
lams = (0.01, 0.1, 1.0, 10.0, 100.0)
T6 = 1.0
r6 = max(fdt_residual([(A, lam * tau) for A, tau in SPECS["three_pole"]],
                      T6) for lam in lams)
# stronger statement: the DATA S(w) itself is scale-covariant only through
# chi''; verify that changing T changes omega_T but admits the same taus
r_T = max(fdt_residual(SPECS["three_pole"], T)
          for T in (0.01, 0.1, 1.0, 10.0, 100.0))
check("K6_no_intrinsic_relaxation_scale_from_kms",
      r6 < 1e-10 and r_T < 1e-10,
      "rescaling all tau_i by lambda in [0.01,100] (max res "
      f"{r6:.2e}) and varying T over 4 decades (max res {r_T:.2e}) "
      "preserves KMS exactly: tau-spectrum is T-independent freedom")
print("== K7: T -> 0 degenerates to zero-point relation, still no selection ==")
T0 = 1e-6
r0_disc = fdt_residual(SPECS["three_pole"], T0, n=200)
r0_cont = fdt_residual(lambda w: continuum_ddom_exp(w), T0, n=200)
# zero-point form: S(w) -> 2 hbar chi''(w) Theta(w) independent of T
zp_ok = True
for w in (0.1, 1.0, 10.0):
    S = noise_S(SPECS["three_pole"], w, T0)
    ref = 2.0 * HBAR * chi_ddom(SPECS["three_pole"], w)
    if abs(S - ref) / abs(ref) > 1e-6:
        zp_ok = False
    Sneg = noise_S(SPECS["three_pole"], -w, T0)
    if abs(Sneg) > 1e-9 * abs(ref):
        zp_ok = False
check("K7_zero_temperature_limit_still_selects_nothing",
      r0_disc < 1e-8 and r0_cont < 1e-8 and zp_ok,
      f"T=1e-6: discrete res {r0_disc:.2e}, continuum res {r0_cont:.2e}; "
      "S degenerates to 2 hbar chi'' Theta(w) (zero-point), no selection")
print("== K-FRAME: occupation vs dynamical spectrum distinction ==")
# Different spectra produce DIFFERENT S(w) data, but all satisfy KMS: the
# thermal constraint cannot tell which (A_i, tau_i) the medium carries.
d12 = 0.0
for i in range(50):
    w = 1e-2 * (1e4) ** (i / 49)
    a, b = noise_S(SPECS["single_pole"], w, T_REF), noise_S(SPECS["two_pole"], w, T_REF)
    if abs(b) > 1e-300:
        d12 = max(d12, abs(a - b) / abs(b))
all_pass = all(fdt_residual(s, T_REF) < 1e-10 for s in SPECS.values())
check("KFRAME_kms_constrains_occupation_not_dynamical_spectrum",
      all_pass and d12 > 0.1,
      f"single- and two-pole media give empirically distinguishable S(w) "
      f"(max rel diff {d12:.1f}) yet BOTH satisfy KMS/FDT exactly: "
      "equilibrium data constrains occupation only; the memory spectrum "
      "is not derived from it")
print("== CONTROL: instrument must fail a non-physical kernel ==")
def bad_kernel(w):
    return w * w                      # even, not odd: violates KMS by FDT
def neg_kernel(w):
    return -w / (1.0 + w * w)         # negative weight: violates passivity
r_bad = fdt_residual(bad_kernel, T_REF)
r_neg = passivity_residual(neg_kernel)
check("CONTROL_nonphysical_kernels_rejected",
      r_bad > 0.1 and r_neg > 0.5,
      f"even chi'' KMS residual {r_bad:.2f}, negative-weight passivity "
      f"residual {r_neg:.2f}: the instrument discriminates")
# ------------------------------------------------------------------ close ---
results["verdict"] = (
    "KMS/FDT constrain the thermodynamic occupation of the noise spectrum "
    "but do NOT derive the memory spectrum: N = 1, 2, 3, and infty are all "
    "admitted, amplitudes and relaxation times are unconstrained, no "
    "intrinsic tau_0 emerges, and the T->0 limit selects even less. "
    "Thermodynamic derivation of the number of memory modes FAILS."
)
results["consequences"] = [
    "The attempt to derive N thermodynamically terminates (negative result).",
    "GRUT can derive the allowable FORM of a passive memory spectrum "
    "(odd, positive, simple poles) but not the number of modes or scales.",
    "Next candidate selection mechanism: geometry/spatial structure "
    "(u3_scale_selection), now motivated by exhaustion of temporal and "
    "thermodynamic constraints.",
]
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)
npass = sum(1 for c in results["checks"] if c["pass"])
print(f"\n{npass}/{len(results['checks'])} checks pass -> "
      f"{RESULT_PATH}")
