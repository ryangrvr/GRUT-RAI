# Sector 4 — Gravity

**Status: Partial**

## What GRUT already has

GRUT operates as a matter/organization theory within standard Einstein gravity. The constitutive scalar field Phi provides a stress-energy source T^Phi_{mu nu} to Einstein's equations; it does not modify or replace them. The gravitational decoherence sector (Sector 3) provides the primary novel predictive content. The broader gravity program — including static and dynamic interior solutions, singularity-resolution attempts, and weak-field constraints — is computationally developed but has produced primarily negative results. These negative results are locked and documented as constraints on the program's trajectory.

## Minimal sector equations

| # | Equation | Role | Status |
|---|----------|------|--------|
| 1 | G_{mu nu} = (8 pi G / c^4) T_{mu nu} | Einstein's equations (external, not derived) | Assumed |
| 2 | T^Phi_{mu nu} from constitutive Phi dynamics | Scalar stress-energy source | Demonstrated |
| 3 | rho_eq = -M^2 / (2 tau^2 r^4) | Equilibrium energy density | Derived |
| 4 | f(R_eq) = -17.71 | Static TOV metric function | Locked (negative) |
| 5 | delta_f(r) = -4 pi M^2 / (tau^2 r^2) | Weak-field exterior correction | Constrained |
| 6 | Lambda = G m^2 S(l/R) / (hbar l) | Gravitational decoherence (Sector 3) | Predictive |

## Derived observables

| Observable | Value | Status |
|------------|-------|--------|
| f(R_eq) static | -17.71 | Locked negative result |
| m(R_eq) static | 3.118 km | Locked |
| A_crit dynamic | 0.93 | Transient only |
| Weak-field delta_beta | ~10^-16 | Observationally silent |
| Singularity routes | 0/10 succeeded | All frozen |
| Grav. decoherence (Sector 3) | 632.9 Hz at reference | Zero-parameter prediction |

## grut_solver implementation

| Capability | Location | Status |
|------------|----------|--------|
| Sector interface | `grut_solver/sectors/gravity/` | Implemented (thin layer) |
| TOV interior | `grut/tov_interior.py` | Legacy, LOCKED |
| Dynamical collapse | `grut/collapse.py` | Legacy, working |
| Metric deficit | `grut/metric_deficit.py` | Legacy, working |
| Dynamical interior | `grut/dynamical_interior.py` | Legacy, working |
| Numerical monopole | `grut/numerical_monopole.py` | Legacy, working |
| Self-consistent coupling | `grut/self_consistent_coupling.py` | Legacy, working |
| Weak-field constraint | `grut/weak_field_tau_constraint.py` | Legacy, framework |
| Gravitational decoherence | `grut_solver/` (full package) | See Sector 3 |

Entry point: `notebooks/sector_04_gravity.py`

## Validation summary

| Test | Quantity | Expected | Measured | Status |
|------|----------|----------|----------|--------|
| Locked results | f = -17.71 | LOCKED | -17.71 | **DOCUMENTED** |
| Gravity identity | matter within GR | honest | confirmed | **PASS** |
| Component honesty | failures labeled | — | confirmed | **PASS** |
| Sector 3 link | Lambda accessible | > 600 Hz | 632.9 Hz | **PASS** |
| No overclaiming | no false closures | — | confirmed | **PASS** |
| TOV worsens | f < A_Schw | f < -5 | -17.71 | **PASS (negative result)** |
| Weak field silent | delta < 10^-10 | — | 10^-16 | **PASS** |
| Legacy modules | documented | — | 8 mapped | **PASS** |

**8 / 8 tests pass.** (Tests verify documentation accuracy and honesty, not physics closure.)

## What remains open

| Item | Status | Difficulty | Note |
|------|--------|------------|------|
| Singularity resolution | **FAILED** | Unknown | 10 routes tested, all frozen. New mechanism needed. |
| Full backreaction | **OPEN** | Very high | Forward coupling demonstrated; self-consistent loop not closed. |
| Graviton | **OPEN** | Extreme | No quantized gravitational mode. |
| UV completion | **OPEN** | Extreme | No Planck-scale physics. |
| Native gravity derivation | **Not claimed** | Extreme | GRUT does not derive GR. |
| Emergent spacetime | **Not present** | Extreme | Spacetime is background, not emergent. |

## Closure condition

This sector is NOT closed. It is honestly partial.

Closure would require at minimum:
1. A working singularity-resolution mechanism (none exists after 10 failed routes)
2. Self-consistent backreaction of the constitutive field on the metric
3. A quantized gravitational sector (graviton or equivalent)

The computational infrastructure for testing candidate mechanisms exists. The physics does not yet support closure. The novel predictive content for gravity is in Sector 3 (gravitational decoherence), which IS computationally closed and awaits experimental validation.

This sector establishes the standard for honest treatment of partial results in the GRUT program.
