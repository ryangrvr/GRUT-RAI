# Book XVI — Target Beta: Structural Claim Matrix

---

## Table 1 — Candidate Evaluation (5 Candidates x 3 Criteria)

| Candidate | C1: Not GR+matter | C2: Adversarial math | C3: No amplification | **Verdict** |
|-----------|--------------------|---------------------|---------------------|-------------|
| 1. Native time-reversal breaking | **PASS** (GR is T-reversible) | **PASS** (Lyapunov theorem) | **PASS** (equation itself) | **SURVIVES** |
| 2. Phase 4 T^Phi (rho_eq < 0) | **PASS** (GR has no scalar) | **PASS** (xAct; 3-step algebra) | **PASS** (exact equilibrium) | **SURVIVES** |
| 3. Constitutive decoherence | **PASS** (no universal tau_dec in QM) | **PARTIAL FAIL** (L postulated) | **PASS** | **FAILS (C2)** |
| 4. Biology scaffold | **PASS** (no biology in GR+SM) | **CONDITIONAL** (extension-level) | **PASS** | **PASSES AT EXTENSION LEVEL** |
| 5. Vacuum response | **PASS** (foundational) | **N/A** (postulate, not derivation) | **PASS** | **ARCHITECTURAL FOUNDATION** |

---

## Table 2 — Adversarial Vulnerability Scan

| Claim element | Attack vector | Defense | Severity |
|---------------|--------------|---------|----------|
| Forward semigroup S(t) = exp(-t/tau) | "Could be reversed" | Lyapunov V < 0 is algebraic theorem | **NONE** |
| rho_eq = -X^2/(2tau^2) | "Sign error?" | 3-step algebra: (1/2 - 1)/tau^2 = -1/(2tau^2) | **NONE** |
| w = -1 | "Depends on approximation?" | Exact at equilibrium with nabla Phi = 0 | **NONE** |
| Phi = X at equilibrium | "Why equilibrium?" | Definition of steady state: dPhi/dt = 0 implies Phi = X | **NONE** |
| X = M/r^2 | "Only Newtonian" | Leading-order GR: X ~ m(r)/r^2 with corrections | **LOW** |
| tau value | "Unknown parameter" | FREE — determines all magnitudes | **HIGH** |
| Minimal coupling | "Why not conformal?" | Standard choice; conformal gives different T^Phi | **MODERATE** |
| Decoherence L = (1/sqrt(tau))Phi | "Why this L?" | Postulated (MBU); not derived | **HIGH** |
| Biology bridges | "Just postulates" | Yes, but 26 zero-cost consequences | **MODERATE** |

---

## Table 3 — The Irreducible Claim: Derivation Chain

| Step | Content | Status | Source |
|------|---------|--------|--------|
| 0 | Postulate: tau dPhi/dt + Phi = X | **POSTULATE** | Book II native canon |
| 1 | Forward semigroup: Phi(t) = X + delta_0 exp(-t/tau) | **DERIVED** (exact solution of linear ODE) | Appendix TC |
| 2 | Lyapunov: V = (1/2)delta^2, dV/dt = -2V/tau < 0 | **DERIVED** (algebraic theorem) | Appendix TC |
| 3 | Scalar action: S = integral[(1/2)(nabla Phi)^2 + V(Phi) - Phi*J] | **STANDARD** (minimally coupled scalar) | Phase 1 |
| 4 | T^Phi: nabla_a Phi nabla_b Phi - g_ab[...] | **DERIVED** (variation of action) | Phase 4 xAct |
| 5 | Equilibrium: Phi = X, nabla Phi = 0 | **DERIVED** (steady state of Step 0) | Phase 4 |
| 6 | rho_eq = V - Phi*J = -X^2/(2tau^2) | **DERIVED** (3-step algebra) | Phase 4 |
| 7 | w = p/rho = -1 | **DERIVED** (from T^Phi components) | Phase 4 |

**Steps 1-7 are all derivations from Step 0. The entire chain depends on ONE postulate.**

---

## Table 4 — Predictions vs GR+Matter

| Regime | GR+matter prediction | GRUT prediction | Difference |
|--------|---------------------|-----------------|-----------|
| Vacuum exterior of star | rho = 0 | rho = -M^2/(2tau^2 r^4) | **Negative energy halo** |
| Compact-object interior | Schwarzschild (f < 0 inside horizon) | Worse: mass accumulates, f more negative | **WORSENED** (XIII Gamma) |
| Late-universe cosmology | Accelerating (with Lambda) | Anti-accelerating (rho_eq < 0) | **Opposite sign** |
| Early-universe cosmology | Standard Big Bang + inflation | Softened but not bounced + 3-regime H*tau | **Modified transition** |
| Arrow of time | Statistical / boundary conditions | Constitutive (Lyapunov at ODE level) | **Native irreversibility** |
| Decoherence | Model-dependent (environment) | tau_dec = tau/2 (if Lindblad postulated) | **Universal timescale** (conditional) |

---

## Table 5 — Program Scope Map

| Sector | GRUT coverage | Level | Depends on |
|--------|--------------|-------|-----------|
| Vacuum structure | tau dPhi/dt + Phi = X | **NATIVE** | Postulate |
| Forward semigroup / arrow of time | Lyapunov guaranteed | **DERIVED** | Step 0 |
| Equilibrium energy-momentum | rho_eq = -X^2/(2tau^2) | **DERIVED** | Step 0 + Phase 4 |
| Gravity | Einstein gravity (GR) as framework | **INSTALLED** | Step 0 + GR (not derived) |
| Compact-object physics | T^Phi on GR backgrounds | **DERIVED** (adverse) | Steps 0-7 |
| Cosmology | 3-regime H*tau regulator | **DERIVED** (partial) | Steps 0-7 + FRW |
| Soliton matter | O(3) topological solitons | **EXTENSION** (Bridge 1) | 4P + 2p |
| Gauge forces | Yang-Mills | **EXTENSION** (Bridge 2) | 2P + 1p + 1F + 6DOF |
| Biology (homeostasis-boundary) | 26 zero-cost targets | **EXTENSION CONSEQUENCE** | Bridges 1-5 |
| Quantum (operational) | Lindblad + decoherence | **CONDITIONAL** (postulated L) | Steps 0 + Lindblad postulate |
| Fermions | BLOCKED | **ABSENT** | 3-layer obstruction |

---

## Table 6 — Cost Accounting

| Category | Current (XVI Alpha) | Change from XVI Beta | Final |
|----------|--------------------|--------------------|-------|
| Committed postulates | 16 | 0 | **16** |
| Committed parameters | 11 | 0 | **11** |
| Committed fields | 1 | 0 | **1** |
| Committed DOF | 6 | 0 | **6** |
| Free parameters (controlling) | 1 (tau) | Identified as priority | **1** |
| Irreducible structural claims | 0 identified | **1 identified** | **1** |
| Surviving candidates | — | 2 (= 1 inseparable claim) | **1 claim** |
| Failed candidates | — | 3 (decoherence, biology, vacuum-as-claim) | **3 failed/conditional** |

---

## Table 7 — Next-Stage Priority (from the Irreducible Claim)

| Priority | Task | Reason | Difficulty |
|----------|------|--------|-----------|
| **1** | Constrain tau from observation | Controls ALL prediction magnitudes; one free parameter | HIGH (needs astro data) |
| **2** | Compute rho_eq effect on binary-pulsar timing | The sharpest precision test; Hulse-Taylor P-dot at 0.2% | HIGH (GR + scalar correction) |
| **3** | Compute 3-regime H*tau cosmological signature | Observable in CMB / expansion history | MODERATE |
| **4** | Compute equilibrium scalar effect on gravitational lensing | Additional mass from rho_eq modifies lensing | MODERATE |
| **5** | Build second-wave quantum (Q-II) | Extend conditional decoherence to composite states | MODERATE |
| **6** | Resolve fermion obstruction | Opens chemistry, real matter | HIGH (structural barrier) |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| **Irreducible structural claim** | rho_eq = -X^2/(2tau^2) on GR backgrounds (from constitutive dissipation) |
| **Derivation status** | THEOREM (3-step algebra from one postulate; xAct verified) |
| **Adversarial robustness** | PASS (no hidden assumptions, no proxies, no amplification) |
| **Cannot reduce to GR+matter** | PASS (GR has no constitutive scalar with this specific T^Phi) |
| **Controlling vulnerability** | tau (one free parameter; determines all magnitudes) |
| **Adverse consequences** | REAL: anti-accelerating, worsens interiors, no bounce |
| **Biology scaffold** | INTACT at extension level (26 zero-cost targets survive) |
| **Quantum program** | CONDITIONAL (postulated Lindblad; decoherence derived within that) |
| **Compact-object frontier** | COLLAPSED (XVI Alpha; sign error) |
| **Next priority** | Constrain tau; compute precision-test predictions |

---

*Structural Claim Matrix complete. Eight tables. One irreducible claim identified: rho_eq = -X^2/(2tau^2). Controlling parameter: tau. Adverse consequences are the predictions.*
