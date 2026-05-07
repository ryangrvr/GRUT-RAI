# GRUT v7 — Appendix I: Experimental Program

## The Tests That Determine GRUT's Fate

---

## I.0 — Purpose

This appendix specifies every experimentally testable prediction of GRUT,
ordered by feasibility and impact.

---

## I.1 — The Primary Test: Gravitational Decoherence Plateau

**What to measure:** The decoherence rate Lambda of a mesoscopic object
as a function of pressure P, mass m, geometry R, and superposition
separation l.

**The prediction:** Below P ~ 10^-10 Pa, Lambda saturates at
Lambda_grav = G m^2 S(l/R) / (hbar l). Standard QM predicts Lambda → 0.

**The six scaling laws (the real prediction):**

| Signature | Measurement | Expected |
|:---|:---|:---|
| F1: mass-squared | Lambda vs m at fixed l | Slope = 2 on log-log |
| F2: geometry | gold vs silica at same mass | Different Lambda |
| F3: pressure plateau | Lambda vs P scan | Flat below 10^-10 Pa |
| F4: l-scaling | Lambda vs l in far field | Slope = -1 |
| F5: entanglement | Bell vs separable pairs | Bell decoheres slower |
| F6: geometric kink | Fine scan near l = 2R | Slope change +2 → -1 |

**A single experiment measuring F1 + F2 + F6 would be decisive.** No tested
alternative reproduces all six simultaneously.

**Target groups:** Arndt (Vienna), Aspelmeyer (Vienna), Geraci (Northwestern),
Bateman (UCL).

**Benchmark:** Gold microsphere R = 1 um, l = 1 um: Lambda ~ 689 Hz, t_coh ~ 1.5 ms.

**Technology gap:** Current state-of-art reaches ~10^5 amu at ~10 nm separation.
The prediction requires ~10^10 amu at ~100 nm. The gap is ~5 orders in mass
and ~1 order in separation. Feasible within next-generation optomechanics.

---

## I.2 — The Cosmological Link

**If Lambda_grav is measured:** tau_0 is determined independently.
Then H_inf = (2-R)/(S tau_0) becomes a zero-parameter prediction of
the cosmological constant.

**The specific test:** Does the measured tau_0 give Omega_Lambda within
the Planck error bar (0.6889 ± 0.0056)?

**If yes:** GRUT connects a lab measurement to the expansion of the universe.
**If no:** The cosmological formula is falsified (the anomaly structure, S,
or the bridge parameter is wrong).

---

## I.2a — The Scaling Exponent Table

The decisive discriminator between GRUT and environmental decoherence is not any
single rate but the PATTERN of scaling exponents across four experimental axes:

| Channel | alpha (mass) | beta (separation) | gamma (pressure) | delta (temperature) |
|:---|:---|:---|:---|:---|
| **GRUT** | **+2.0** | **-1.0** | 0.0 | 0.0 |
| Gas scattering | +0.67 | +2.0 | +1.0 | +0.5 |
| Blackbody | +0.67 | +2.0 | 0.0 | +6.0 |
| EM noise | ~0 | ~0 | 0.0 | ~0 |
| Vibrational | ~0 | ~0 | 0.0 | ~0 |

**The smoking gun: beta.** GRUT has beta = -1 (decoherence DECREASES with separation).
ALL environmental sources have beta = +2 (decoherence INCREASES with separation).
Opposite signs. Varying l and measuring the slope gives an unambiguous YES/NO answer.

Precision needed: +/- 1% in the separation scaling exponent.

---

## I.2b — Three Experimental Protocols

**Protocol A (Mass Scaling):** Vary mass 100x at fixed l, P, T. Fit alpha.
- GRUT confirmation: alpha > 1.5
- GRUT falsification: alpha < 1.0
- Strength: Moderate (alpha = 2 vs alpha = 0.67 is large but mass is harder to vary cleanly)

**Protocol B (Separation Anti-Scaling) — STRONGEST:** Vary l by 20x at fixed m, P, T. Fit beta.
- GRUT confirmation: beta < -0.5
- GRUT falsification: beta > +1.5
- Strength: Decisive (opposite signs make this the cleanest test)

**Protocol C (Environmental Decoupling):** Vary P and T independently. Extract
the P-independent, T-independent residual floor.
- GRUT confirmation: Non-zero floor survives at all P and T
- GRUT falsification: Lambda -> 0 as P -> 0 and T -> 0
- Strength: Strong (tests the plateau prediction F3 directly)

---

## I.2c — Realistic Noise Budget

A complete noise budget identifies the dominant noise source at each operating point:

| Channel | Rate at (m=10^9 amu, l=100nm, P=10^-14 Pa, T=4K) | Notes |
|:---|:---|:---|
| GRUT gravitational | ~10^-5 Hz | Signal |
| Gas scattering | ~10^-5 Hz | Comparable to GRUT at this P |
| Blackbody radiation | ~10^-13 Hz | Negligible at 4K |
| Laser shot noise | ~10^14 Hz | MUST be subtracted (not decoherence) |
| Radiation pressure | ~10^-3 Hz | Significant |
| EM noise (good shielding) | ~10^-3 Hz | Often dominant |
| Vibrational (good isolation) | ~10^-12 Hz | Negligible |

**Dominant noise at 300K:** Blackbody (10^6 Hz). **At 4K:** EM noise (10^-3 Hz).
**At 100 mK:** EM noise (10^-6 Hz with excellent shielding).

**The bottleneck:** EM shielding. Even at 100 mK with UHV (10^-14 Pa),
electromagnetic noise dominates unless shielding reaches 10^-6 Hz or better.
This requires multi-layer mu-metal + active compensation or superconducting shields.

---

## I.2d — The Isotope Decoherence Test

The cleanest geometry discriminator. Compare nanoparticles of different
isotopes of the SAME element:

**Why cleaner than material swap:** Si-28 vs Si-30 have identical chemistry,
crystal structure, surface charge, optical properties, and phonon spectrum.
The ONLY difference is nuclear mass -> density -> radius -> S(l/R) -> Lambda_grav.
Environmental decoherence sees identical surfaces and predicts ratio = 1.000.

| Pair | GRUT Ratio | Deviation | 5-sigma precision |
|:---|:---|:---|:---|
| **Ca-40 vs Ca-48** | **0.694** | **30.6%** | 6.1% |
| Ge-70 vs Ge-76 | 0.848 | 15.2% | 3.0% |
| Si-28 vs Si-30 | 0.871 | 12.9% | 2.6% |
| W-182 vs W-186 | 0.957 | 4.3% | 0.9% |

Recommended: Silicon (enriched isotopes commercially available from semiconductor
industry, 99.99% purity). Ca-48 gives stronger discrimination but is harder to source.

---

## I.2e — Material Swap Experiment

Take two spheres of IDENTICAL mass but different density. GRUT predicts
different rates; mass-only models predict identical rates.

**Best pair:** Osmium (22,590 kg/m^3) vs Aluminum (2,700 kg/m^3) at 10^8 amu:
**737% rate difference** at the optimal separation (near the geometric kink).

**Condition:** The experiment MUST operate at separations comparable to the
particle radius (l ~ R). In the far field (l >> R), all materials give
S = 1 and the ratio collapses to 1.000.

---

## I.2f — Geometry Kink Scan

The extended-body suppression S(l/R) = min(1, (l/R)^3/6) creates a sharp
slope change at l = 6^(1/3)R ≈ 1.817R on a log-log plot:

- Near field (l < R): Lambda proportional to l^2 (slope +2)
- Far field (l > R): Lambda proportional to l^-1 (slope -1)

The kink is UNIQUE to GRUT. Diosi-Penrose (point mass) has no kink.
CSL has no kink. Finding the kink at the predicted location l = 6^(1/3)R ≈ 1.817R
would be a geometry-specific confirmation.

At 10^9 amu gold: R = 27 nm. Kink predicted at l = 49 nm.

---

## I.2g — Entanglement Protection Test

GRUT predicts that Bell-entangled pairs decohere SLOWER than separable states.
CSL predicts the SAME rate (state-independent).

At 10^8 amu, l = 100 nm: Bell/separable ratio = 0.41 (59% protection).
CSL ratio = 1.000 (0% protection).

The protection is mass-independent (~65% at d = 50 nm, constant across
5 decades of mass). This is a YES/NO discriminator: does entanglement
affect the decoherence rate?

---

## I.3 — Secondary Tests

| Prediction | What to measure | Expected | Current status |
|:---|:---|:---|:---|
| Dark photon at ~387 MeV | Collider or beam dump searches | m_A ~ 387 MeV, g_dark ~ 0.917 | LHCb, Belle II searching |
| No axion | Axion detection experiments | Null result | ADMX, ABRACADABRA running |
| Baryon asymmetry | Precision eta_B from CMB | 6.56 × 10^-10 (Route 1) | Planck: 6.1 ± 0.04 × 10^-10 |
| Neural 40 Hz | Gamma-tubulin correlation across species | f ~ 40 Hz at N ~ 38,000 | Testable with comparative neuroscience |
| Koide K = 2/3 | Precision tau mass measurement | K within 0.005% of 2/3 | PDG: K = 0.666632 |

---

## I.4 — What Would Falsify GRUT

| Observation | What it kills |
|:---|:---|
| No decoherence plateau | The predictive core (Lambda_grav) |
| Axion detected | Strong CP hypothesis (theta = 0 from FP) |
| Proton decay observed | SM emergence argument (minimality) |
| Koide violated | Z_3 trace identity |
| 4th generation fermion found | N = 3 uniqueness |
| Lambda_grav measured but gives wrong Omega_Lambda | The bridge parameter |

---

## I.5 — What Would NOT Falsify GRUT

| Observation | Why it survives |
|:---|:---|
| No GW modification at LIGO | Predicted: effect is 10^-39 rad (dead) |
| No QNM modification | Predicted: effect is 10^-80 (dead) |
| Hierarchy problem unsolved | Acknowledged: honest negative |
| Fermion masses not derived | Acknowledged: M0 and theta open |

---

*D. Ryan Grover, April 2026.*
