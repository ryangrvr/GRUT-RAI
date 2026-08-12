#!/usr/bin/env python3
"""TWO-SCALE VACUUM: is the IR relaxation scale tau2 ~ 1/H forced by the de Sitter horizon,
or inserted by hand?

GRUT's evolving-w(z) story (rung 7) needs a second, slow relaxation scale tau2 ~ 1/H0 -- the
same 'second bath scale' that conditions single-pole (rung 3). We asserted it was
'horizon-motivated'. This tests that, using Starobinsky-Yokoyama stochastic inflation, where a
light scalar in de Sitter obeys a Langevin equation whose noise IS the horizon (Gibbons-Hawking)
scale:

    dphi/dt = -V'(phi)/(3H) + (H/2pi) eta(t),   <eta(t)eta(t')> = delta(t-t')

The diffusion constant is D = (1/2)(H/2pi)^2 = H^2/(8 pi^2): the fluctuation amplitude is set by
the horizon. So the EXISTENCE of a horizon-driven relaxation is intrinsic to de Sitter -- not
inserted. The question is the TIMESCALE.

For the first two moments the Langevin equation closes exactly (Ornstein-Uhlenbeck for V=m^2 phi^2/2):
    d<phi>/dt   = -(m^2/3H) <phi>
    d<phi^2>/dt = -2(m^2/3H) <phi^2> + 2D
=> mean relaxes at rate m^2/3H, so  tau_relax = 3H/m^2,  and  <phi^2>_eq = 2D/(2 m^2/3H) = 3H^4/(8 pi^2 m^2).
We integrate these moment ODEs deterministically (no randomness) and read off the relaxation time.

Units: H = 1.  tau is then in units of the Hubble time 1/H.  Pure stdlib.
"""
import math

H = 1.0
D = H ** 2 / (8.0 * math.pi ** 2)          # diffusion from the horizon noise (H/2pi)^2/2


def rk4_moments(m, phi0=1.0, var0=0.0, dt=0.002, tmax=200.0):
    """Integrate the OU moment ODEs; return (times, mean[], var[]) and the mean's 1/e time."""
    k = m * m / (3.0 * H)                    # OU relaxation rate
    mean, var, t = phi0, var0, 0.0
    one_over_e_time = None
    target = phi0 / math.e
    n = int(tmax / dt)
    for _ in range(n):
        # state y = (mean, var); dy/dt
        def deriv(mn, vr):
            return (-k * mn, -2.0 * k * vr + 2.0 * D)
        m1 = deriv(mean, var)
        m2 = deriv(mean + 0.5 * dt * m1[0], var + 0.5 * dt * m1[1])
        m3 = deriv(mean + 0.5 * dt * m2[0], var + 0.5 * dt * m2[1])
        m4 = deriv(mean + dt * m3[0], var + dt * m3[1])
        new_mean = mean + dt / 6 * (m1[0] + 2 * m2[0] + 2 * m3[0] + m4[0])
        new_var = var + dt / 6 * (m1[1] + 2 * m2[1] + 2 * m3[1] + m4[1])
        if one_over_e_time is None and new_mean <= target:
            one_over_e_time = t + dt
        mean, var, t = new_mean, new_var, t + dt
    return mean, var, one_over_e_time


def main():
    print("=" * 78)
    print("TWO-SCALE VACUUM  --  is tau2 ~ 1/H forced by the de Sitter horizon?")
    print("Starobinsky-Yokoyama stochastic inflation; noise = H/2pi (Gibbons-Hawking).  H=1.")
    print("=" * 78)

    print("""
HORIZON-FORCED part (intrinsic to de Sitter, NOT inserted):
  The Langevin noise amplitude is H/2pi -- the Gibbons-Hawking fluctuation. So a light field in
  de Sitter is DRIVEN by the horizon and relaxes toward the Starobinsky-Yokoyama equilibrium.
  The existence of a horizon-scale stochastic relaxation is a property of de Sitter, not a patch.
  diffusion D = (H/2pi)^2/2 = %.5f  (in units H=1)
""" % D)

    # ---- free field: timescale needs a mass ------------------------------------------
    print("-" * 78)
    print("FREE FIELD V=m^2 phi^2/2:  tau_relax = 3H/m^2.  (numerics check the moment ODEs)")
    print("-" * 78)
    print("    m/H     tau_relax*H (=3/(m/H)^2)   1/e time (numeric)   <phi^2>_eq (num / 3/(8pi^2 m^2))")
    for moh in (0.3, 1.0, math.sqrt(3.0), 3.0):
        m = moh * H
        mean_f, var_f, t1e = rk4_moments(m)
        tau_pred = 3.0 / moh ** 2
        var_eq_pred = 3.0 / (8 * math.pi ** 2 * moh ** 2)
        t1e_s = f"{t1e:.2f}" if t1e else ">tmax"
        print(f"   {moh:5.2f}    {tau_pred:14.3f}          {t1e_s:>10}        {var_f:.4f} / {var_eq_pred:.4f}")
    print("""    => tau_relax ~ 1/H requires m ~ sqrt(3) H ~ 1.7 H. A LIGHT field (m << H) relaxes in
       MANY Hubble times (tau >> 1/H); a free field tuned to tau ~ 1/H0 NOW needs m ~ H0 ~ 1e-33
       eV -- the standard quintessence coincidence. So for a FREE mode, tau2 ~ 1/H is INSERTED.""")

    # ---- self-interacting field: dynamical mass tracks H -----------------------------
    print("\n" + "-" * 78)
    print("SELF-INTERACTING FIELD lambda phi^4/4:  de Sitter IR generates m^2_eff ~ sqrt(lambda) H^2")
    print("  (Starobinsky-Yokoyama dynamical mass -- literature value, workflow-verifying)")
    print("-" * 78)
    print("    lambda    m_eff/H = (lambda)^(1/4)   tau_relax*H = 3/sqrt(lambda)")
    for lam in (1.0, 0.1, 0.01):
        meff_over_h = lam ** 0.25
        tau = 3.0 / math.sqrt(lam)
        print(f"   {lam:6.2f}    {meff_over_h:18.3f}        {tau:10.2f}")
    print("""    => m_eff ~ sqrt(lambda) H, so tau_relax ~ 3/(sqrt(lambda) H). For lambda ~ O(1),
       tau ~ few x (1/H). CRUCIALLY m_eff ~ H TRACKS the Hubble scale at EVERY epoch, so
       tau ~ 1/H always -- 'evolving now' is generic, NOT a one-time coincidence. For such a mode
       tau2 ~ 1/H is FORCED by the horizon (up to the O(1) coupling).""")

    print("\n" + "=" * 78)
    print("VERDICT  (lead; the human de Sitter / stochastic-inflation specialist is the firewall)")
    print("=" * 78)
    print("""\
  CONDITIONAL. Decompose, as with the arrow (existence vs scale):
   * The horizon FORCES the NOISE (H/2pi) and the EXISTENCE of a stochastic relaxation toward the
     Starobinsky-Yokoyama equilibrium. That part is intrinsic to de Sitter -- not a patch.
   * The relaxation TIMESCALE tau2:
       - FREE IR mode: tau ~ 3H/m^2; tau ~ 1/H0 today needs m ~ H0 -- the standard quintessence
         coincidence/tuning. INSERTED.
       - SELF-INTERACTING O(1) IR mode: de Sitter IR generates m_eff ~ sqrt(lambda) H, which
         TRACKS H, so tau ~ 1/H at all epochs. FORCED by the horizon (no 'why now' coincidence).
  So tau2 ~ 1/H is horizon-FORCED *iff* GRUT's IR vacuum mode is a light, O(1)-self-coupled scalar
  (dynamical-mass tracking), and INSERTED/tuned if it is a free field.

  WHAT THE 'NATURAL' ROUTE STILL ASSUMES (mark, do not launder):
   (i)  the existence of a light scalar IR mode in the vacuum;
   (ii) an O(1) self-coupling lambda for it.
  These are real inputs. The horizon supplies the noise and the tracking; it does not supply the
  mode or its coupling for free.

  CANDIDATE INTERNAL CONNECTION (hypothesis, not established): the conformalon -- the contested
  dynamical conformal mode of the trace-anomaly / rung-9 alpha leg -- is exactly a self-interacting
  conformal scalar that could be this IR mode, tying rung 9 (alpha de-anchor) to rung 7 (w(z)
  two-scale). If so, the same mode that threatens the alpha anchor would SUPPLY the cosmological
  relaxation. To be checked, not claimed.

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'For a light O(1)-self-coupled scalar in de Sitter, does the dynamically generated mass
     m_eff ~ sqrt(lambda) H track H closely enough across the matter->dark-energy transition that
     the relaxation time stays ~ 1/H (making evolving w(z) generic), or does the tracking fail
     once H is not constant (restoring a coincidence)?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
