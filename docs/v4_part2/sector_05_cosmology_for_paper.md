# Sector 5 — Cosmology

**Status: Partial / Conditional**

## What GRUT already has

The cosmology sector has significant computational infrastructure: homogeneous background evolution (H(z), growth factor, fsigma8), an LCDM reference baseline, Hubble-tension residual metrics, an FFT-based lensing calculator, a rotation-curve analyzer, a cosmological bounce analysis, and a dark-sector dual-track framework. However, the key physics claim — that the constitutive field provides a dark-energy mechanism — has permanently failed (rho_eq < 0 is anti-accelerating). The sector provides comparison and analysis tools, not a cosmological solution.

## Minimal sector equations

| # | Equation | Role | Status |
|---|----------|------|--------|
| 1 | H^2 = H_0^2 [Omega_m(1+z)^3 + Omega_Lambda + correction] | Modified Friedmann | Implemented |
| 2 | E(z) = H(z)/H_0 | Normalized Hubble | Implemented |
| 3 | D'' + [...] D' - (3/2) Omega_m / a^2 D = 0 | Growth equation | Implemented |
| 4 | rho_eq = -M^2 / (2 tau^2 r^4) | Equilibrium density | **NEGATIVE (FAILED)** |
| 5 | Classification: softened, not bounced | Bounce analysis | Partial |

## Derived observables

| Observable | Status | Note |
|------------|--------|------|
| E(z) at z = 0, 0.5, 1, 2 | Implemented | Matches LCDM to code precision |
| Omega_m(z) | Implemented | From operator stack |
| fsigma8(z) | Implemented | Compared to observational data |
| Hubble-tension residuals | Implemented | RMS and point-by-point |
| Lensing (kappa, gamma) | Implemented | FFT-based |
| Rotation curves v(r) | Implemented | Baryonic + GRUT prediction |
| Dark-energy mechanism | **PERMANENTLY FAILED** | rho_eq < 0 |

## grut_solver implementation

| Capability | Location | Status |
|------------|----------|--------|
| Sector interface | `grut_solver/sectors/cosmology/` | Implemented (status layer) |
| LCDM reference | `grut/lcdm_reference.py` | Legacy, working |
| Hubble tension metrics | `grut/hubble_tension_metrics.py` | Legacy, working |
| Bounce extension | `grut/cosmological_bounce_extension.py` | Legacy, working |
| Dark-sector analysis | `grut/dark_sector_extension.py` | Legacy, DE route FAILED |
| Lensing | `grut/lensing.py` | Legacy, working |
| Rotation curves | `grut/rotation_curves.py` | Legacy, working |
| Operators (H(z), growth) | `grut/operators.py` | Legacy, working |
| Cosmology sweep | `tools/sweep_cosmology.py` | Working |
| Hubble packet builder | `tools/build_hubble_tension_packet.py` | Working |

Entry point: `notebooks/sector_05_cosmology.py`

## Validation summary

| Test | Quantity | Expected | Measured | Status |
|------|----------|----------|----------|--------|
| DE failure documented | rho_eq < 0 | PERMANENTLY_FAILED | confirmed | **PASS** |
| Nonclaims explicit | 5 nonclaims | — | 5 documented | **PASS** |
| LCDM E(z=0) | 1.0 | 1.0 | 1.0000 | **PASS** |
| LCDM E(z=1) | 1.761 | 1.761 | 1.7607 | **PASS** |
| Component honesty | failures labeled | — | confirmed | **PASS** |
| No overclaiming | status = Partial | — | confirmed | **PASS** |
| Modules documented | >= 7 | — | 9 modules + 4 tools | **PASS** |
| Bounce = softening | not full bounce | — | confirmed | **PASS** |
| Screening length | FREE | — | documented | **PASS** |

**8 / 8 tests pass.** (Tests verify documentation accuracy and failure honesty.)

## What remains open

| Item | Status | Difficulty | Note |
|------|--------|------------|------|
| Dark-energy mechanism | **PERMANENTLY FAILED** | — | rho_eq < 0 |
| Late-universe modification | **Failed** | — | No viable route |
| Perturbation spectrum | **Not implemented** | High | Needed for CMB/BAO |
| CMB/BAO fit | **Not attempted** | Very high | Requires perturbation closure |
| Natural screening length | **Open** | High | Naturalness problem |
| Full observational fit | **Not achieved** | Very high | Infrastructure exists, physics missing |
| Early-universe regulator | **Conditional** | Medium | Not validated |

## Closure condition

This sector is NOT closed. Closure would require:
1. A viable dark-energy or late-universe acceleration mechanism (current one permanently failed)
2. A precision perturbation spectrum matching CMB and BAO observations
3. A natural determination of the screening length
4. Full observational fit across multiple datasets (H(z), fsigma8, CMB TT/EE, BAO, SNIa)

The computational infrastructure for testing candidate mechanisms exists and is extensive. The physics does not yet support cosmological closure. The dark-energy failure is permanent within the current constitutive framework (rho_eq < 0).
