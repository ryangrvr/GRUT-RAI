# Sector 2 — Electroweak / Standard Model Host Structure

**Status: Recovered host structure**

## What GRUT already has

The electroweak gauge structure of the Standard Model is recovered by promoting the target functional's gradient to a covariant derivative and organizing the directed-response field into SU(2) × U(1)_Y multiplets. The Higgs mechanism generates gauge boson and fermion masses through spontaneous symmetry breaking. The free-parameter count matches the Standard Model. This sector establishes host consistency; it does not claim parameter reduction or beyond-SM phenomenology.

## Minimal sector equations

| # | Equation | Role |
|---|----------|------|
| 1 | D_mu = d_mu + ieA_mu | U(1) covariant derivative (gauge principle) |
| 2 | F[z,A] = integral {\|z\|^2 + c_2\|Dz\|^2} | Gauge-invariant target functional |
| 3 | iℏ d_t z = [(p-eA)^2/(2m) + ePhi] z | Gauge-coupled Schrodinger |
| 4 | D_mu Z = d_mu Z + ig T^a W_mu^a Z + ig'(Y/2) B_mu Z | Non-abelian covariant derivative |
| 5 | Q = T^3 + Y/2 | Electric charge operator |
| 6 | sum Y = sum Y^3 = sum Y(doublets) = 0 | Anomaly cancellation |
| 7 | V(H) = -mu^2\|H\|^2 + lambda\|H\|^4 | Mexican-hat Higgs potential |
| 8 | <H> = (0, v/sqrt(2))^T, Q<H> = 0 | SSB: SU(2)×U(1)_Y -> U(1)_EM |
| 9 | m_W = gv/2, m_Z = sqrt(g^2+g'^2)v/2, rho = 1 | Mass relations |
| 10 | M_f = y_f v / sqrt(2) | Fermion masses (y_f FREE) |

## Derived observables

| Observable | Value / relation | Status |
|------------|-----------------|--------|
| m_W | 80.3 GeV | Demonstrated |
| m_Z | 91.1 GeV | Demonstrated |
| m_photon | 0 (exact) | Demonstrated |
| rho | 1.000000 | Demonstrated |
| sin^2(theta_W) | 0.223 | Demonstrated |
| Q(nu_eL) | 0 | Exact |
| Q(e_L) | -1 | Exact |
| Q(u_L) | +2/3 | Exact |
| Q(d_L) | -1/3 | Exact |
| Yukawa hierarchy | y_top/y_electron = 338,552 | Documented (free) |

## GRUT-RAI / grut_solver implementation

| Module | Function | Status |
|--------|----------|--------|
| `gauge_u1.py` | Covariant Laplacian, gauge RHS, invariance check | Implemented |
| `lorentz_force.py` | Acceleration benchmark in E field | Implemented |
| `ab_phase.py` | Aharonov-Bohm phase benchmark | Implemented |
| `electroweak_su2_u1.py` | SU(2) structure, charges, covariance, Lie algebra | Implemented |
| `anomaly_cancellation.py` | Three exact-zero anomaly checks | Implemented |
| `higgs_sector.py` | VEV, symmetry breaking, Goldstone counting | Implemented |
| `mass_relations.py` | W/Z masses, rho, fermion masses, parameter count | Implemented |

Entry point: `notebooks/sector_02_electroweak_host.py`

## Validation summary

| Test | Quantity | Expected | Measured | Status |
|------|----------|----------|----------|--------|
| U(1) gauge invariance | max \|rho - rho'\| | < 10^-14 | 4.4 × 10^-16 | **PASS** |
| Lorentz force (E=0.5) | a_meas vs eE/m | < 2% | 1.3% | **PASS** |
| Lorentz force (3 values) | all < 2% | — | all pass | **PASS** |
| AB phase | gauge phase exact | density unchanged | < 10^-14 | **PASS** |
| Charge quantization | Q = T^3 + Y/2 | 7/7 exact | all match | **PASS** |
| SU(2) covariance | D'Z' = U(DZ) | < 10^-12 | 1.6 × 10^-17 | **PASS** |
| Lie algebra | [T^a,T^b] = i eps T^c | exact | 0 error | **PASS** |
| Anomaly (grav.) | sum Y = 0 | 0 | 0.0 | **PASS** |
| Anomaly (cubic) | sum Y^3 = 0 | 0 | 0.0 | **PASS** |
| Anomaly (mixed) | sum Y(dbl) = 0 | 0 | 0.0 | **PASS** |
| Higgs VEV | v > 0, V_min < 0 | — | v = 1.41, V = -0.50 | **PASS** |
| Symmetry breaking | Q<H> = 0, 3 broken | — | exact | **PASS** |
| W/Z masses | m_W ~ 80, m_Z ~ 91 | SM values | 80.3, 91.1 | **PASS** |
| rho parameter | rho = 1 | 1.000000 | 1.000000 | **PASS** |
| Parameter count | matches SM | ~20 | 19 free + 1 identified | **PASS** |
| Yukawas free | documented | — | hierarchy = 338,552x | **PASS** |

**13 / 13 tests pass.**

## What remains open

| Item | Status | Note |
|------|--------|------|
| Gauge group derivation | Open | SU(2) × U(1)_Y is assumed, not derived |
| Number of generations | Open | 3 is observed, not computed |
| Yukawa couplings | Free | Same as SM — not derived |
| Flavor mixing (CKM/PMNS) | Free | Same as SM — not derived |
| SU(3) color (QCD) | Not in this sector | Deferred to Sector 6 |
| Non-abelian dynamics (full YM) | Documented, not propagated | Self-interaction verified algebraically |

## Closure condition

Sector 2 is closed as a host-recovery sector. All structural benchmarks pass: gauge invariance, charge quantization, anomaly cancellation, symmetry breaking, mass relations, and parameter count. The electroweak structure of the Standard Model is recovered from the GRUT target functional with the gauge principle applied to the covariant derivative. No new physics is claimed in this sector. The free-parameter count is identical to the SM.
