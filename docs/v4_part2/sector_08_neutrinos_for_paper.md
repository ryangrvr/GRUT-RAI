# Sector 8 — Neutrinos

**Status: Open, with exploratory entry point**

## What GRUT already has
Neutrinos fit within the electroweak host. Dirac and Majorana/seesaw mass entry points are documented. PMNS mixing angles and oscillation observables are scaffolded as diagnostic utilities. No neutrino mass mechanism is derived from GRUT.

## Minimal sector equations
| # | Equation | Status |
|---|----------|--------|
| 1 | m_Dirac = y_nu v / sqrt(2) | Documented (y_nu ~ 10^-12) |
| 2 | m_seesaw ~ (y_nu v)^2 / (2 M_R) | Documented (M_R undetermined) |
| 3 | P(alpha->beta) = \|sum U_{ai}* U_{bi} exp(-i m_i^2 L/2E)\|^2 | Implemented |

## Derived observables
All values are MEASURED INPUTS, not GRUT predictions: theta_12 = 33.4 deg, theta_23 = 49 deg, theta_13 = 8.6 deg, dm^2_21 = 7.53e-5 eV^2, dm^2_32 = 2.45e-3 eV^2.

## Validation summary
| Test | Status |
|------|--------|
| Dirac mass formula | **PASS** |
| Seesaw formula | **PASS** |
| Mass-scale scan (4 entries) | **PASS** |
| PMNS row norms ~ 1 | **PASS** |
| Mixing angles documented as input | **PASS** |
| Oscillation probability (T2K-like) | **PASS** |
| Mass splittings documented | **PASS** |
| No overclaiming | **PASS** |

**8/8 pass.**

## What remains open
Neutrino mass mechanism, PMNS derivation, mass ordering, CP phase, Dirac vs Majorana, absolute mass scale — all open.

## Closure condition
Derive the neutrino mass mechanism, PMNS mixing angles, mass ordering, and CP phase from GRUT structure.
