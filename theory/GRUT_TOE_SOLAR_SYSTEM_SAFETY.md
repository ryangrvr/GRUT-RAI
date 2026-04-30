# GRUT — Solar-System Safety Multi-Test Demonstration

*Auto-generated from `grut/derived/solar_system_safety.py`. Re-run to regenerate.*

Eight independent precision tests of GR span six orders of magnitude in frequency. For each test, GRUT's predicted constitutive correction α_eff(ω) = α/(1 + (ωτ_0)²) is compared to the observational measurement precision. The safety factor (obs precision / α_eff) is the margin by which GRUT's prediction sits below detection threshold.

## Aggregate

- Total tests: 8
- Tests with safety factor > 1 (GRUT below detection): 8/8
- Tests with safety factor > 100 (substantial margin): 8/8
- Smallest safety factor: 2.31e+05
- Largest safety factor: 1.45e+35
- Median safety factor: 1.07e+16

## Per-test breakdown

| ID | Test | Period | ωτ_0 | α_eff | Obs precision | Safety factor |
|:---|:---|:---|---:|---:|---:|---:|
| SS01 | Saturn orbit (Cassini ranging) | 30 yr | 8.78e+06 | 4.33e-15 | 1.0e-09 | 2.3e+05 |
| SS02 | Mercury perihelion advance | 88 days | 1.09e+09 | 2.79e-19 | 3.0e-03 | 1.1e+16 |
| SS03 | Lunar laser ranging | 27.3 days | 3.52e+09 | 2.69e-20 | 1.0e-13 | 3.7e+06 |
| SS04 | GPS orbital relativity | 12 hours | 1.92e+11 | 9.01e-24 | 1.0e-13 | 1.1e+10 |
| SS05 | Hulse-Taylor binary pulsar B1913+16 | 7.75 hours | 2.98e+11 | 3.76e-24 | 1.6e-03 | 4.3e+20 |
| SS06 | Cassini Shapiro delay | 500 s (≈ 1 AU/c) | 1.66e+13 | 1.21e-27 | 2.3e-05 | 1.9e+22 |
| SS07 | LIGO/Virgo GW propagation (GW170817) | ≈10 ms (100 Hz GW) | 8.31e+17 | 4.83e-37 | 7.0e-02 | 1.4e+35 |
| SS08 | Earth orbit (AU ranging) | 1 yr | 2.63e+08 | 4.81e-18 | 1.0e-09 | 2.1e+08 |

## Detailed entries

### SS01 — Saturn orbit (Cassini ranging)

- **Period:** 30 yr (9.47e+08 s)
- **Frequency basis:** orbital angular frequency
- **ω = 2π/period:** 6.64e-09 Hz
- **ωτ_0:** 8.78e+06
- **α_eff(ω):** 4.33e-15
- **Observational precision:** 1.0e-09 (Cassini ranging fractional precision on Saturn position)
- **Safety factor:** 2.31e+05 (safe)
- **Citation:** Folkner et al. 2014 (DE430 ephemeris)

### SS02 — Mercury perihelion advance

- **Period:** 88 days (7.60e+06 s)
- **Frequency basis:** orbital angular frequency
- **ω = 2π/period:** 8.26e-07 Hz
- **ωτ_0:** 1.09e+09
- **α_eff(ω):** 2.79e-19
- **Observational precision:** 3.0e-03 (fractional precision on the GR contribution (43 arcsec/century) from MESSENGER and INPOP ephemerides)
- **Safety factor:** 1.07e+16 (safe)
- **Citation:** Park et al. 2017 (AJ 153 121); Verma et al. 2014

### SS03 — Lunar laser ranging

- **Period:** 27.3 days (2.36e+06 s)
- **Frequency basis:** Earth-Moon orbital frequency
- **ω = 2π/period:** 2.66e-06 Hz
- **ωτ_0:** 3.52e+09
- **α_eff(ω):** 2.69e-20
- **Observational precision:** 1.0e-13 (G_dot/G constraint per year (Williams et al. 2004))
- **Safety factor:** 3.72e+06 (safe)
- **Citation:** Williams, Turyshev, Boggs 2004 (PRL 93 261101)

### SS04 — GPS orbital relativity

- **Period:** 12 hours (4.32e+04 s)
- **Frequency basis:** GPS satellite orbital frequency
- **ω = 2π/period:** 1.45e-04 Hz
- **ωτ_0:** 1.92e+11
- **α_eff(ω):** 9.01e-24
- **Observational precision:** 1.0e-13 (atomic clock fractional stability (~10⁻¹³/day))
- **Safety factor:** 1.11e+10 (safe)
- **Citation:** Ashby 2003 (Living Rev. Rel. 6, 1)

### SS05 — Hulse-Taylor binary pulsar B1913+16

- **Period:** 7.75 hours (2.79e+04 s)
- **Frequency basis:** orbital angular frequency
- **ω = 2π/period:** 2.25e-04 Hz
- **ωτ_0:** 2.98e+11
- **α_eff(ω):** 3.76e-24
- **Observational precision:** 1.6e-03 (ratio of observed to GR-predicted period decay rate (precision ~0.16%))
- **Safety factor:** 4.26e+20 (safe)
- **Citation:** Weisberg & Huang 2016 (ApJ 829 55)

### SS06 — Cassini Shapiro delay

- **Period:** 500 s (≈ 1 AU/c) (5.00e+02 s)
- **Frequency basis:** photon transit time across Sun's gravitational field
- **ω = 2π/period:** 1.26e-02 Hz
- **ωτ_0:** 1.66e+13
- **α_eff(ω):** 1.21e-27
- **Observational precision:** 2.3e-05 (post-Newtonian γ measurement (γ - 1 = (2.1 ± 2.3) × 10⁻⁵))
- **Safety factor:** 1.91e+22 (safe)
- **Citation:** Bertotti, Iess, Tortora 2003 (Nature 425 374)

### SS07 — LIGO/Virgo GW propagation (GW170817)

- **Period:** ≈10 ms (100 Hz GW) (1.00e-02 s)
- **Frequency basis:** gravitational-wave angular frequency
- **ω = 2π/period:** 6.28e+02 Hz
- **ωτ_0:** 8.31e+17
- **α_eff(ω):** 4.83e-37
- **Observational precision:** 7.0e-02 (constraint on GW group velocity vs. c at 7% level (GW170817 + GRB170817A coincidence))
- **Safety factor:** 1.45e+35 (safe)
- **Citation:** Abbott et al. (LIGO+Virgo) 2017 (ApJL 848 L13)

### SS08 — Earth orbit (AU ranging)

- **Period:** 1 yr (3.16e+07 s)
- **Frequency basis:** Earth orbital frequency
- **ω = 2π/period:** 1.99e-07 Hz
- **ωτ_0:** 2.63e+08
- **α_eff(ω):** 4.81e-18
- **Observational precision:** 1.0e-09 (AU determination precision from radar/pulsar timing)
- **Safety factor:** 2.08e+08 (safe)
- **Citation:** DE430 / IAU 2009 nominal AU value


Verify:
  [PASS] all_tests_safe
  [PASS] all_tests_substantial_margin
  [PASS] median_safety_above_1e6
  [PASS] min_safety_above_1e4
  [PASS] all_alpha_eff_under_1e_minus_10
  [PASS] tests_span_six_orders_of_magnitude_in_omega
