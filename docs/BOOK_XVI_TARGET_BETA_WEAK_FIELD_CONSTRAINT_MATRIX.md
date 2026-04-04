# BOOK XVI TARGET BETA — WEAK-FIELD CONSTRAINT MATRIX

**Companion matrix for:** Book XVI Beta — Irreducible Constitutive Gravity and Tau-Constraint Audit
**Program:** GRUT Omni-ToE
**Phase:** G (Portal-UI Anamnesis)
**Date:** 2026-04-04
**Classification:** Formal Audit Companion — 9 Reference Tables

---

## TABLE 1 — Irreducible Claim Table

| Field | Value |
|---|---|
| **Claim formula** | `rho_eq = -X^2 / (2 tau^2)` |
| **Equation of state** | `w = -1` (NEC-saturated) |
| **Derivation chain** | 3 steps from constitutive equation |
| Step 1 | Constitutive relation `T^Phi_{mu nu}` at equilibrium `Phi = X` |
| Step 2 | Extract `rho_eq` from `T^Phi_{00}` component |
| Step 3 | Verify `p_eq = -rho_eq` yields `w = -1` identically |
| **Verification method** | xAct (Mathematica tensor algebra) |
| **Postulate count** | 1 |
| **Free parameter count** | 1 (`tau`) |

---

## TABLE 2 — Reduction / Comparison Table

| Comparison | Matches | Differs | Irreducible? |
|---|---|---|---|
| vs GR + massive scalar | Same action form, same `T_{mu nu}`, same equilibrium energy | Dynamics only (1st order vs 2nd order) | **REDUCIBLE** at equilibrium |
| vs R^2 correction | — | Different scaling (`1/r^4` vs `1/r^6`), different origin (scalar matter vs modified gravity) | **NOT EQUIVALENT** |
| vs Semiclassical vacuum | — | Different origin (classical vs quantum), different scaling, different suppression (`tau` vs `hbar`) | **NOT EQUIVALENT** |

---

## TABLE 3 — Weak-Field Derivation Table

| Step | Expression | Note |
|---|---|---|
| 1 | `X(r) = M / r^2` | Newtonian source identification |
| 2 | `rho_eq(r) = -M^2 / (2 tau^2 r^4)` | Substitution into claim formula |
| 3 | `dm/dr = 4 pi r^2 rho_eq = -2 pi M^2 / (tau^2 r^2)` | Mass-shell equation |
| 4 | `delta_m(r) = 2 pi M^2 / (tau^2 r)` | Integration from `r` to infinity |
| 5 | `delta_f(r) = -4 pi M^2 / (tau^2 r^2)` | Force correction |
| 6 | `delta_beta_effective = 4 pi / tau^2` | PPN deviation (geometric units) |

**Critical note:** Source identification is **AMBIGUOUS**. `X = 0` if Ricci-sourced, because `R = 0` in Schwarzschild vacuum exterior.

---

## TABLE 4 — Observable / PPN Table

| Location | tau (s) | \|delta_f\| | \|delta_beta\| | Detectable? |
|---|---|---|---|---|
| Mercury perihelion | 1 | 1.4e-25 | 1.4e-10 | **NO** |
| Earth orbit | 1 | 1.4e-26 | 1.4e-10 | **NO** |
| Mercury perihelion | 6e5 (t_dyn) | 3.9e-37 | 3.8e-22 | **NO** |
| Earth orbit | 3.5e6 (t_dyn) | 1.1e-39 | 1.1e-23 | **NO** |
| Solar surface | 1126 (t_dyn) | 5.0e-28 | 1.1e-16 | **NO** |

**Current detection threshold (Cassini):** `|delta_beta| > 2.3e-5`

---

## TABLE 5 — Tau-Constraint Table

| Observation | Bound on \|delta_beta\| | tau_min (km) | tau_min (s) |
|---|---|---|---|
| Cassini (gamma) | 2.3e-5 | 739 | 2.5e-3 |
| Nordtvedt / LLR (beta) | 1e-4 | 355 | 1.2e-3 |
| Mercury precession | 1e-3 | 112 | 3.7e-4 |

**To reach Cassini sensitivity:** `tau < 739 km = 2.5 ms`.
**Physical tau values:** `t_dyn >> 2.5 ms` always. No physical tau threatens detection.

---

## TABLE 6 — Hard-Criteria Pass/Fail Matrix

| # | Criterion | Verdict |
|---|---|---|
| 1 | Mathematical sharpness | **YES** — 3-step derivation, explicit closed-form formula |
| 2 | Irreducibility vs GR + matter | **NO** — reducible to GR + massive scalar at equilibrium |
| 3 | Clarity of weak-field derivation | **YES** — explicit, bounded, step-by-step |
| 4 | Genuine precision-gravity consequence | **NO** — corrections ~10^-16 at physical tau |
| 5 | Strength of tau constraints | **FORMAL ONLY** — tau > 2.5 ms; physical tau >> this bound |
| 6 | Observational distinctness | **NO** — silent at all physical tau |
| 7 | Frontier survives | **NO** — weakens sharply |

---

## TABLE 7 — Limitation / Failure Table

| Failure | Severity | Detail |
|---|---|---|
| Reducible at equilibrium | **CRITICAL** | `T^Phi` identical to GR + massive scalar at `Phi = X` |
| Source identification ambiguous | **HIGH** | `X = 0` if Ricci-sourced (`R = 0` in Schwarzschild exterior) |
| Correction structurally suppressed | **HIGH** | `delta_beta = 4 pi / (tau_s * c)^2`; `c^2` factor kills observable magnitude |
| No physical tau reaches detection | **HIGH** | All `t_dyn >> 2.5 ms` |
| Dynamics not tested by static metric | **MODERATE** | GRUT novelty is dynamics; equilibrium is testable but reducible |

---

## TABLE 8 — Frontier Consequence Table

| Aspect | Before XVI Beta | After XVI Beta |
|---|---|---|
| Gravity frontier | Active frontier with demonstrated surplus | Equilibrium claim reducible + silent |
| Equilibrium `T^Phi` | Irreducible structural claim | Reducible to GR + massive scalar |
| Weak-field | Sharpest testable prediction | Observationally silent at physical tau |
| Tau constraint | Controlling free parameter | Formally bounded but not physically threatened |
| Program identity | Constitutive gravity modifies Einstein | Constitutive dynamics (not equilibrium) is the novelty |
| GRUT novelty | Negative energy halo | Native dissipation, Lyapunov, time-reversal (dynamics only) |

---

## TABLE 9 — Final Classification

| Aspect | Status |
|---|---|
| **Global verdict** | **A** — weak-field claim reducible + observationally silent |
| Irreducibility | FAILS at equilibrium; survives in dynamics only |
| Weak-field correction | Derived (`delta_f = -4 pi M^2 / (tau^2 r^2)`) but undetectable |
| Tau bound | `tau > 2.5 ms` (formal); physical `tau >> bound` |
| Observational window | NONE — corrections ~10^-16 at physical tau |
| Gravity frontier | WEAKENS SHARPLY |
| Structural novelty | DYNAMICS ONLY (dissipation, Lyapunov, time-reversal breaking) |
| Next step | Accept weak-field silence; pivot to dynamical predictions if any exist |

---

*End of Book XVI Target Beta — Weak-Field Constraint Matrix.*
