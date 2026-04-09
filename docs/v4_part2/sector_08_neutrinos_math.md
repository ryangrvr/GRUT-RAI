# Sector 8 — Neutrinos: Mathematical Scaffold

## 1. Neutrino mass as distinct from generic flavor

Neutrinos are massless in the minimal SM (no right-handed neutrino). Observed oscillations require at least two nonzero masses. The mass mechanism is unknown.

## 2. Dirac mass entry point

If right-handed neutrinos nu_R exist:

    M_nu^Dirac = y_nu v / sqrt(2)

Same mechanism as charged fermions. Requires y_nu ~ 10^{-12} (unnaturally small).

## 3. Majorana / seesaw entry point

If nu_R has a Majorana mass M_R >> v:

    m_nu ~ (y_nu v)^2 / (2 M_R)     (Type-I seesaw)

This explains smallness naturally: m_nu is suppressed by the heavy scale M_R.

**Status in GRUT:** Neither Dirac nor Majorana is derived. Both are documented as exploratory entry points.

## 4. PMNS mixing matrix

The PMNS matrix U_PMNS relates neutrino flavor and mass eigenstates:

    nu_alpha = sum_i U_{alpha i} nu_i     (alpha = e, mu, tau; i = 1, 2, 3)

Parameterized by 3 mixing angles + 1 Dirac CP phase (+ 2 Majorana phases if applicable):

    theta_12 ~ 33.4 deg (solar)
    theta_23 ~ 49 deg (atmospheric)
    theta_13 ~ 8.6 deg (reactor)
    delta_CP ~ 195 deg (hint, not precise)

Unitarity: U^dag U = I (exact).

## 5. Oscillation observables

    P(nu_alpha -> nu_beta) = |sum_i U_{alpha i}* U_{beta i} exp(-i m_i^2 L / (2E))|^2

Key measured quantities:
- Delta m^2_21 = 7.53e-5 eV^2 (solar)
- |Delta m^2_32| = 2.453e-3 eV^2 (atmospheric)
- Mass ordering: normal (m_1 < m_2 < m_3) or inverted — OPEN

## 6. Missing ingredients

| Ingredient | Status |
|------------|--------|
| Neutrino mass mechanism | **Open** |
| PMNS derivation | **Open** |
| Mass ordering | **Open** |
| CP phase | **Open** |
| Dirac vs Majorana | **Open** |
| Absolute mass scale | **Open** |
