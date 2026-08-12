#!/usr/bin/env python3
"""RUNG 7: evolving dark-energy w(z) from a finite-memory vacuum -- the second differentiator.

SIGN NOTE (SUPERSEDED 2026-06-29 by rung7_w2 / calc/wz_sign.py + calc/RESULTS_wz_sign.md): the
"w_a > 0, the WRONG sign for DESI" conclusion in this toy is RETRACTED. The w_a SIGN is
frontier-indeterminate -- the second law fixes the dissipative branch on the phantom SIDE (w<=-1,
which forbids a phantom-divide crossing) but NOT the w_a SLOPE sign (this toy's sign is a
zeta=const/Eckart artifact; other passive zeta(a) scalings give w_a>0 too). The robust, retained
content here is the NO-CROSSING / needs->=2-modes structure and the sourced w=-1 FLAT prediction;
read the sign claims below as the toy output they are, not as a banked result.


Goal: a PASS-candidate observable that does NOT depend on the rung-8 falsifier's magnitude,
to get GRUT off single-point-of-failure. A finite-memory vacuum has a frequency-dependent
response chi(omega); out of equilibrium its effective equation of state w(z) can deviate
from -1. A static-Lambda time-symmetric family cannot produce an evolving w(z) -- so IF
GRUT predicts (not fits) the shape, it differentiates.

This build surfaces a STRUCTURAL coupling to rung 3's confirmation boundary, which is the
main result and must be reported straight.

Heuristic relaxor model (illustrative of STRUCTURE; the exact form needs the full
Calzetta-Hu in-in stress tensor): the cosmological expansion forces the vacuum at frequency
~ H(z). A single relaxation time tau gives a storage response R(x)=x^2/(1+x^2), x=H(z)*tau,
so w(z) = -1 + eps * R(H(z) tau). Units: H in units of H0; eps is a staked amplitude.
"""
import math

OM = 0.31           # matter density; OL = 1-OM (flat)
OL = 1.0 - OM


def E(z):
    """Dimensionless Hubble H(z)/H0 (LCDM background)."""
    return math.sqrt(OM * (1 + z) ** 3 + OL)


def w_relaxor(z, Htau, eps):
    x = E(z) * Htau          # H(z)*tau in units where tau is measured in 1/H0
    return -1.0 + eps * (x * x) / (1.0 + x * x)


def cpl_fit(Htau, eps):
    """Return (w0, wa) of the CPL map w(z)=w0+wa z/(1+z) matching value+slope at z=0."""
    w0 = w_relaxor(0.0, Htau, eps)
    h = 1e-4
    dwdz0 = (w_relaxor(h, Htau, eps) - w_relaxor(0.0, Htau, eps)) / h
    wa = dwdz0          # since d/dz[z/(1+z)]|0 = 1
    return w0, wa


def main():
    print("=" * 78)
    print("RUNG 7  evolving w(z) from a finite-memory vacuum")
    print("w(z) = -1 + eps * (H(z)tau)^2/(1+(H(z)tau)^2)   [relaxor, illustrative]")
    print("=" * 78)

    # ---- (A) the scale that matters: tau_c (UV) vs tau_2 ~ 1/H0 (IR) -------------------
    print("\n(A) WHICH relaxation time? w(z) only evolves if the vacuum has response power")
    print("    at omega ~ H(z). Compare the confirmed UV-cutoff memory vs an IR scale.")
    omega_c_over_H0 = 1e40       # microscopic cutoff vs Hubble: ~40+ orders of magnitude
    Htau_uv = 1.0 / omega_c_over_H0
    print(f"    UV cutoff:  tau_c ~ 1/omega_c,  H0*tau_c ~ {Htau_uv:.0e}")
    print(f"    IR horizon: tau_2 ~ 1/H0,       H0*tau_2 = 1")
    print("      z      w(z) [tau=tau_c, UV]      w(z) [tau=1/H0, IR]   (eps=0.4)")
    for z in [0.0, 0.5, 1.0, 2.0, 3.0]:
        wuv = w_relaxor(z, Htau_uv, 0.4)
        wir = w_relaxor(z, 1.0, 0.4)
        print(f"   {z:5.2f}      {wuv:18.12f}     {wir:12.5f}")
    print("    => UV-cutoff memory: w = -1 to ~80 decimals, FLAT. No evolution, no")
    print("       differentiation -- a single-pole short-memory vacuum reproduces Lambda.")
    print("       Observable w(z) evolution REQUIRES a slow scale tau_2 ~ 1/H0.")

    # ---- (B) the coupling to rung 3's boundary ----------------------------------------
    print("\n" + "-" * 78)
    print("(B) THE COUPLING TO RUNG 3  (the main structural result)")
    print("-" * 78)
    print("""
    The expert's confirmation of single-pole came with ONE boundary: it holds PROVIDED the
    vacuum bath has no second internal dynamical scale. Rung 7 just showed that an evolving
    w(z) REQUIRES exactly such a second scale, tau_2 ~ 1/H0. So the two are coupled:

       single-pole (tabletop)  wants  ONE scale (the UV cutoff)
       evolving w(z) (cosmology) wants a SECOND, slow scale tau_2 ~ 1/H0

    RESOLUTION -- they coexist BY SCALE SEPARATION, not by contradiction:
      * tau_2/tau_c ~ omega_c/H0 ~ 1e40. The IR pole is ~40 orders of magnitude slower.
      * At tabletop frequencies (omega >> H0) the IR pole is invisibly slow -> the kernel is
        still single-pole/cutoff-dominated. The expert's 'no second scale' is satisfied
        WHERE THE TABLETOP LIVES, even though a second scale exists in the deep IR.
      * At cosmological frequencies (omega ~ H) the IR pole is active -> w(z) evolves.
    So GRUT can have BOTH, but only by committing to a TWO-SCALE vacuum:
        UV cutoff omega_c  (tabletop single-pole)  +  IR horizon scale ~H  (w(z) evolution).
    That is a concrete, named, falsifiable structural commitment -- not a free patch.
    Note the IR scale ~H is horizon-motivated (de Sitter/Gibbons-Hawking), the SAME scale
    where kill-shot #1 found cosmology sits at the crossover. It may be natural rather than
    a tuned coincidence -- but 'why tau_2 ~ 1/H now' must be addressed (cosmic coincidence).
""")

    # ---- (C) the falsifiable prediction: a one-parameter (w0,wa) locus ----------------
    print("-" * 78)
    print("(C) THE PARAMETER-ECONOMY TEST  (vs CPL's two free params w0, wa)")
    print("-" * 78)
    print("    With tau_2 = 1/H0 FIXED by the horizon, the relaxor is a ONE-parameter family")
    print("    (eps). So w0 and wa are CORRELATED -- a pre-registerable locus, not a free fit.")
    print("      eps     w0=w(0)      wa(eff)      w(z=1)     w(z=3)")
    for eps in [0.1, 0.2, 0.4, 0.6]:
        w0, wa = cpl_fit(1.0, eps)
        print(f"     {eps:4.2f}   {w0:8.4f}    {wa:8.4f}    {w_relaxor(1,1.0,eps):8.4f}   {w_relaxor(3,1.0,eps):8.4f}")
    w0a, waa = cpl_fit(1.0, 0.4)
    print(f"\n    Predicted locus: w0 = -1 + eps/2,  wa = +{waa/0.4:.3f}*eps  (both rise with eps)")
    print("    => GRUT predicts wa > 0 with w0 > -1 for eps>0 (w LESS negative in the past).")

    # ---- (D) honest test against DESI, reported straight ------------------------------
    print("\n" + "-" * 78)
    print("(D) MATCH TO DESI 2024-25  --  the embarrassing-direction check")
    print("-" * 78)
    print("""
    DESI's hint is w0 ~ -0.8 (> -1) WITH wa ~ -0.6 (< 0): w MORE negative in the PAST,
    crossing -1 ('quintom'). This toy gives wa > 0 [SIGN RETRACTED 2026-06-29 -- see header +
    rung7_w2: the wa sign is a zeta-scaling ARTIFACT (zeta=const->wa<0, zeta~1/H^2->wa>0), so it
    is genuinely OPEN, NOT 'wrong'; the robust content is the NO-CROSSING, since a single passive
    channel cannot cross -1]. So the SIMPLEST one-parameter relaxor does NOT match DESI's specific
    (w0>-1, wa<0) pattern -- report this straight, do not fit around it. Options, honestly tiered:
      * the storage/loss split or the sign of the relaxor response may differ in the full
        in-in stress-tensor computation (the toy R(x) is heuristic) -> to-derive;
      * a quintom crossing needs more than a single passive relaxor (e.g. a sign-changing
        response or two modes) -> would ADD a parameter, eroding the economy win;
      * if the full computation still gives wa>0, rung 7 FAILS to match DESI and is NOT the
        second differentiator -> then diversify elsewhere (GW dissipation from Im[chi]).
""")

    print("=" * 78)
    print("VERDICT  (lead; for the specialist)")
    print("=" * 78)
    print("""\
  * STRUCTURE (robust): a single-pole short-memory vacuum (UV-cutoff memory) gives w=-1 flat,
    FAILS-DIFFERENTIATION (reproduces Lambda, inherits the CC problem). Evolving w(z) REQUIRES
    a second, cosmologically slow scale tau_2 ~ 1/H0.
  * COUPLING (the main result): that second scale is exactly the 'second bath scale' boundary
    on rung 3's single-pole confirmation. They coexist ONLY by ~40-orders scale separation
    (UV cutoff for the tabletop, IR horizon for cosmology). GRUT must commit to this TWO-SCALE
    vacuum explicitly -- it is a named, falsifiable structural input, and it ties rung 3,
    rung 7, and the de Sitter crossover from kill-shot #1 into one picture.
  * ECONOMY (candidate win): with tau_2=1/H0 fixed by the horizon, w(z) is a ONE-parameter
    family -> a correlated (w0,wa) locus, fewer params than CPL -> pre-registerable.
  * DESI (honest fail-so-far): this toy gives wa>0 [SIGN RETRACTED 2026-06-29 -- a zeta=const
    artifact; the wa sign is OPEN, see header + rung7_w2]. The robust, retained content is the
    NO-CROSSING (a single passive channel cannot cross -1) + sourced w=-1 FLAT; matching DESI's
    crossing needs an inserted >=2-mode structure -- a flagged mismatch, not a fit.

  STATUS: rung 7 stays to-derive. It is a STRUCTURAL second differentiator (w(z) evolution is
  impossible for the static-Lambda family) but its DESI-matching shape is not yet earned and
  the simplest version mismatches. Ledger +1 (eps) and the two-scale commitment is a new
  named input (the IR scale tau_2 ~ 1/H0).

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'Does the in-in (Calzetta-Hu) effective stress tensor of a relaxing vacuum with an IR
     horizon-scale relaxation give w(z) with wa<0 (quintom, DESI-like) or wa>0, for a single
     passive relaxor -- i.e. can one slow pole cross w=-1, or does crossing require two modes?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
