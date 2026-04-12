# GRUT v5 → v6 Bridge Document

## What v5 Achieved, Where It Stops, and What v6 Must Solve

D. Ryan Grover, April 2026

---

## v5 Final Status (Locked)

13 sectors. 183 tests. One equation. Every sector has at least a structural result. Zero sectors fully open. The predictive core (USL decoherence) has zero free parameters and is experimentally testable.

But v5 is 70-75% of a ToE. The remaining 25-30% is specific and identified.

---

## Where v5 Stops: The Five Frontiers

### Frontier 1: Sector 9 — Dark Matter Closure

**What v5 has:** Stable topological solitons from the double-well fixed-point landscape. BPS exact. Survives noise. Mass range 10^6-10^13 GeV from anomaly splitting.

**Where it stops:** The toy model has two parameters (lambda, v) and one constraint (M from anomaly splitting). lambda is NOT uniquely determined. Every route to derive lambda from existing anomaly constants was exhausted:

| Route | lambda | Result |
|-------|--------|--------|
| C_FINAL | 1.1e-4 | Too small, sigma/m explodes |
| R-1 | 0.154 | Not uniquely motivated |
| 2-R | 0.846 | Best structural candidate but not derived |
| alpha_vac | 0.333 | No derivation linking to soliton coupling |
| c_2 = tau_I^2/M | Fixes M = 0.25 GeV | Wrong scale entirely |
| Thin-wall condition | Automatic (R_0/delta = 5847) | Doesn't constrain |
| BPS stability | Automatic | Doesn't constrain |

**sigma/m at benchmarks (geometric, upper bound):**

sigma/m [cm^2/g] = 1.96e24 / (lambda^2 M^3)

- M = 10^6 GeV: EXCLUDED for all natural lambda (needs lambda > 1400)
- M = 10^9 GeV: VIABLE for lambda > 0.04 (all O(1) candidates work)
- M = 10^13 GeV: EASILY VIABLE for any lambda > 0

**The structural reason closure fails:** One equation, two unknowns. The double-well toy model is genuinely underdetermined. This is a model limitation, not a computational one.

**What v6 needs:**

1. **Gauge the Z_2 symmetry** — promote z -> -z to a local gauge symmetry. lambda becomes the gauge self-coupling, fixed by the gauge group. This is the standard route from global to local symmetry.

2. **Or: embed in electroweak** — if the DM soliton field couples to the Higgs, lambda is related to the Higgs portal coupling. This connects Sectors 2 and 9.

3. **Or: add fermion content** — Yukawa coupling provides the second constraint. This connects Sectors 7 and 9 (flavor hierarchy determines DM coupling).

4. **Or: relic density** — computing the thermal or non-thermal production during early-universe threshold crossings (using the discrete era map from Sector 5) gives an independent constraint on (lambda, v).

Each route extends the model beyond v5's content. The most GRUT-native route is #4 (relic density from threshold crossings), because it uses existing Sector 5 machinery.

**Additionally needed for full scattering:**
- 3D object type must be unambiguous (thin-wall bubble chosen, but profile must be derived not assumed)
- Soliton-soliton interaction potential (computed from overlapping profiles or moduli-space approximation)
- Velocity-dependent cross-section for cluster environments

---

### Frontier 2: Sector 12 — Quantum Gravity Beyond Minisuperspace

**What v5 has:** 2/5 closure conditions met (UV completion + classical GR recovery) from minisuperspace fluctuation analysis. Jacobian J = Omega_Lambda. Stable fixed point.

**Where it stops:** Minisuperspace is one degree of freedom. The full gravitational sector has tensor modes (2 polarizations of the graviton), vector modes (gauge), and scalar modes (conformal factor). The 3 unmet conditions require the full tensor sector:

- Condition 1 (graviton): need transverse-traceless modes with m = 0 at low k
- Condition 3 (backreaction): need the full metric-matter loop to close self-consistently
- Condition 4 (BH info): need the full attractor basin, not just one eigenvalue

**What v6 needs:**

1. **Tensor perturbation analysis** — linearize the constitutive gravity equation (with transverse projector) around de Sitter for tensor modes h_ij^TT. Compute the dispersion relation. Show it gives omega^2 = k^2 c^2 at low k (massless graviton) with 1/omega^2 damping at high k.

2. **Graviton propagator** — compute the retarded propagator from the constitutive equation. This is: G_R(k, omega) = 1 / (omega^2 - k^2 c^2 + i omega / tau_grav). Show it has the correct pole structure.

3. **Full backreaction loop** — solve the constitutive gravity equation coupled to quantum matter self-consistently. The fixed-point condition z = z_target[z] for the coupled system should give the de Sitter vacuum with quantum corrections.

---

### Frontier 3: The tau_I Dimensional Question

**What v5 has:** tau_I = hbar/2 identified by matching to the Schrodinger equation. The paper acknowledges that tau's physical meaning shifts between sectors.

**Where it stops:** A hostile reviewer can still ask: is tau a relaxation time or not? If it changes meaning in each sector, is "one equation" a genuine unification or just notation?

**What v6 needs:** Either:

1. **Derive tau_I from A0-A1 alone** — show that the CTP doubling + directed response UNIQUELY fix tau_I = hbar/2 without importing the Schrodinger equation. This would make A2 a theorem, not an axiom.

2. **Or: explicitly define the sector-specific tau** — provide a clear map: tau(sector) = f(sector-specific constants). Show that all sector-specific taus reduce to the same constitutive equation via dimensional scaling.

---

### Frontier 4: Cosmology Precision

**What v5 has:** H_inf = (2-R)/(S tau_0) as a structural ansatz. Three structural steps in the derivation chain. Discrete map with derived parameters producing three-phase expansion.

**Where it stops:** The structural steps are constrained (linearity from single insertion, boundaries from CTP doubling) but not derived from a Lagrangian. The discrete map produces qualitative three-phase behavior but not precision E(z).

**What v6 needs:**

1. **Non-perturbative CTP calculation** — evaluate the 3-loop influence functional at the de Sitter fixed point explicitly. Show it produces the (2-R) factor.

2. **Continuous cosmological evolution** — replace the discrete era map with a continuous integrator that solves the constitutive Friedmann equation with the full retarded memory kernel. Compare E(z) to Pantheon+, DESI, and Planck data at percent level.

3. **Independent Omega_Lambda prediction** — derive H_0 as well as H_inf, or show that GRUT predicts a specific (H_0, Omega_Lambda) pair rather than a one-parameter family.

---

### Frontier 5: Explicit z_target Derivation

**What v5 has:** z_target specified for QM (c_0 z - c_2 nabla^2 z), cosmology (blended Friedmann + vacuum), and decoherence (noise from CTP influence functional).

**Where it stops:** The z_target forms are STATED, not DERIVED from the CTP action in one unified calculation. Each sector has its own z_target obtained by different methods.

**What v6 needs:** A single derivation that starts from the CTP effective action S_CTP[z+, z-] and produces z_target[z] for ALL sectors as different limits of one functional. This is the "holy grail" computation — it would make the "one equation" claim rigorous.

---

## Priority Ranking for v6

| Priority | Frontier | Difficulty | Impact if solved |
|----------|----------|------------|-----------------|
| 1 | z_target derivation (F5) | Very high | Makes "one equation" rigorous |
| 2 | Cosmology precision (F4) | High | Makes Omega_Lambda a prediction |
| 3 | QG tensor sector (F2) | High | Closes 3 more conditions |
| 4 | DM closure (F1) | Medium | Makes Sector 9 definite |
| 5 | tau_I derivation (F3) | Medium | Makes A2 a theorem |

---

## What v6 Would Look Like If All Frontiers Are Closed

- One CTP action -> one z_target[z] -> ALL sectors as limits
- Omega_Lambda derived independently (not conditional on H_0)
- Graviton from tensor perturbations (5/5 QG closures)
- DM mass and sigma/m uniquely predicted (one candidate, not a family)
- tau_I derived from A0-A1 (two axioms, not three)
- Precision E(z) matching CMB+BAO+SNe jointly

That would be ~95% of a ToE. The remaining 5% would be exact fermion masses, baryon asymmetry value, and neutrino mass splittings — all requiring the multi-generation z_target.

---

## The Experimental Arm (Independent of v6 Theory)

While the theory develops, the experimental program can proceed:

1. **USL decoherence plateau** — the primary test. Gold microsphere, R ~ 0.5-1 um, ultra-high vacuum. 2027-2030 timeline with levitated optomechanics.

2. **Cross-species gamma-tubulin correlation** — neuroscience test of the 40 Hz coincidence. Comparatively inexpensive. Can be done now.

3. **R_anomaly precision** — better determination of the 3-loop anomaly coefficients would tighten the H_inf prediction and constrain the DM parameter space.

The theory and experiment can develop in parallel. Neither needs to wait for the other.

---

*D. Ryan Grover, April 2026. Bridge document for GRUT v5 -> v6.*
