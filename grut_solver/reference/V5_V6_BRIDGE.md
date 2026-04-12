# GRUT v5 → v6 Bridge Document (Updated)

## What v5 Achieved, Where It Stops, What Changed Since v5, and What v6 Must Solve

D. Ryan Grover, April 2026

---

## v5 Final Status

13 sectors. 183 tests. One equation. Every sector has at least a structural result. The predictive core (USL decoherence) has zero free parameters. The cosmological constant candidate gives 0.2% accuracy at H_0 = 70. The graviton propagator gives 3/5 QG closures. DM solitons exist and are stable but underdetermined.

70-75% of a ToE, honest about the rest.

---

## What Changed Since v5 Was Published

### Status Upgrades

| Item | v5 Status | Current Status | What Changed |
|------|-----------|---------------|--------------|
| QG closure conditions | 2/5 (minisuperspace) | **3/5** (tensor graviton) | Graviton propagator computed: massless, no ghost, UV 1/omega^3 |
| A2 (tau_I = hbar/2) | Axiom | **Definition** (normalization choice) | Cannot be derived from A0+A1; it selects the Keldysh normalization that gives QM |
| Unified z_target | "Specified per sector" | **Conceptually resolved** (S_CTP is the unified object) | Not yet formalized as explicit variational map |
| DM sigma/m | "Consistent with Bullet Cluster" | **Partially corrected** (viable for M > 10^9 GeV only) | Full sigma/m analysis showed M < 10^9 excluded for natural lambda |
| DM lambda | "Not fitted" | **Underdetermined** (one equation, two unknowns) | All routes to derive lambda exhaustively tested; none close uniquely |

### Status Downgrades (Honest Corrections)

| Item | v5 Claimed | Corrected | Reason |
|------|-----------|-----------|--------|
| Benchmark "10pg nanodiamond R=50nm" | Physically realizable | **Inconsistent** | No material has density 19,000 g/cm^3. Replaced with gold microsphere R=1um |
| "Decoherence is undefined" at fixed point | Broad claim | **Constitutive channel only** | Standard Lindblad decoherence still operates; only the constitutive driving term is zero |
| "One measurement decides all" | Global falsifiability | **Primary target; other sectors independently testable** | Failed plateau doesn't logically disprove Koide or QCD mapping |
| "10 steps, 0 gaps" | Complete derivation | **7 computed + 3 structural** | Structural steps constrain but don't constitute conventional derivation |
| "LOCKED / DEMONSTRATED" labels | Confident | **VERIFIED / COMPUTED** | Toned to match what's actually shown |
| Omega_Lambda "0.25% accuracy" | Single number | **H_0 dependent** (0.2% at 70, 8.1% at Planck) | Not an independent prediction of Omega_Lambda |
| DM "Bullet Cluster automatically satisfied" | Assertion | **Viable for M > 10^9 GeV only** | sigma/m exceeds bounds at M = 10^6 for all natural lambda |
| Heating constraints | "NOT in conflict" | **Order-of-magnitude consistent** | Full constraint analysis not performed |
| Sector 13 "Consciousness" | Label | **Neural Resonance** (recommended) | Reduces reputational risk without changing the mathematics |

---

## The Five Frontiers

### Frontier 1: Unified z_target (CONCEPTUALLY RESOLVED, NOT FORMALIZED)

**Resolution:** S_CTP (the CTP effective action) IS the unified object. Each sector's z_target is a different limit of S_CTP:

- Real part of S_CTP → z_target (coherent evolution, equations of motion)
- Imaginary part of S_CTP → noise kernel (decoherence rates)
- Stationary point of S_CTP → self-referential fixed point

**What's missing for v6:** The variational map from S_CTP to z_target must be written as an explicit formalism section showing:
1. S_CTP[fields, metric] in full generality
2. Variation delta S / delta z_a = 0 → constitutive equation in general form
3. NR limit → Sector 1 z_target
4. Gravitational noise limit → Sector 3 Lambda_grav
5. FRW minisuperspace limit → Sector 5 z_target
6. Yang-Mills limit → Sector 6 z_target

Until this is written as a single coherent derivation, it is bridge material.

### Frontier 2: Cosmology Precision (GENUINELY OPEN)

**What exists:** H_inf = (2-R)/(S tau_0) as a structural ansatz. Three steps constrained by symmetry and boundary conditions, not by explicit Lagrangian calculation. Discrete map with derived parameters producing qualitative three-phase behavior.

**What's missing:**
1. Explicit 3-loop CTP influence functional at de Sitter background
2. Proof that the finite part gives exactly (2-R)/(S tau_0) and not some other form
3. Continuous E(z) compared to Pantheon+/DESI/Planck at percent level
4. Independent prediction of H_0 (or an H_0-independent observable)

**Difficulty:** Research-level QFT in curved spacetime. Not desk-computable.

**Bridge status:** This frontier stays open until the explicit calculation exists. The structural ansatz is well-motivated but not derived.

### Frontier 3: Quantum Gravity Tensor Sector (3/5 CLOSURES MET)

**What's computed:**
- Graviton propagator: G(k,w) = -16piG / [(w^2-k^2c^2)(1-iw tau)]
- Massless graviton (pole at w=kc, same as GR)
- No ghost (imaginary pole at w = -i/tau is dissipative)
- UV improved (|G| ~ 1/omega^3 vs 1/omega^2 in GR)
- Classical GR at LIGO (modification < 10^-10 for T_Planck)
- Spectral function positive (sign convention verified)

**Closure scorecard:**

| # | Condition | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Graviton or equivalent | **DEMONSTRATED** | Massless pole, no ghost, TT modes |
| 2 | UV completion | **CONFIRMED** | 1/omega^3 falloff, Planck suppression |
| 3 | Backreaction | STRUCTURAL | Constitutive eq couples metric to T_mn |
| 4 | BH information | **OPEN** | Requires nonlinear attractor analysis |
| 5 | Classical GR | **CONFIRMED** | LIGO modification < 10^-10 |

**What's missing for full closure:**
- Condition 3: Self-consistent backreaction loop (metric affects matter affects metric) must be solved explicitly, not assumed from the fixed-point definition
- Condition 4: Black hole information requires the full nonlinear attractor basin, including the approach from BH initial conditions. The minisuperspace attractor is necessary but not sufficient.

### Frontier 4: Dark Matter Closure (UNDERDETERMINED)

**What's computed:**
- Stable topological solitons from double-well potential (BPS exact)
- sigma/m = 1/(4 sigma_wall) = 1.96e24 / (lambda^2 M^3) cm^2/g
- Viable mass window: M > 10^9 GeV at natural lambda (0.1-1)
- Lower end M ~ 10^6 GeV: EXCLUDED for all natural lambda

**The structural problem:** Two parameters (lambda, v), one constraint (M from anomaly splitting). Lambda is NOT uniquely determined. All routes exhausted:

- lambda = C_FINAL: too small
- lambda = 2-R: structural candidate but not derived
- lambda from self-consistent c_2: gives fixed mass (wrong)
- Thin-wall condition: automatic, doesn't constrain
- BPS stability: automatic, doesn't constrain

**What v6 needs (any ONE of):**
1. Gauge the Z_2 symmetry → lambda from gauge coupling
2. Higgs portal → lambda from electroweak sector
3. Relic density from threshold crossings → independent (lambda, v) constraint
4. Fermion content (Yukawa) → second equation

**Additionally needed for full scattering:**
- Unambiguous 3D object type (thin-wall bubble chosen but profile must be derived)
- Soliton-soliton interaction potential
- Velocity-dependent cross-section

**Bridge status:** Sector 9 is a parametric existence proof with a viability map, not a closed DM model. This stays bridge-side until lambda is fixed by extension.

### Frontier 5: tau_I Derivation (RESOLVED — NEGATIVE)

**Finding:** tau_I = hbar/2 cannot be derived from A0 (CTP doubling) + A1 (directed response) alone. It depends on the normalization of the Keldysh variables, which is a convention.

**The identification tau_I = hbar/2 selects the normalization that makes the constitutive equation reduce to the Schrodinger equation.** This is the content of A2.

**Recommendation for v6:**
- Reframe A2 from "axiom" to "definition" or "normalization choice"
- State: "We define the constitutive variable z such that the imaginary relaxation parameter tau_I = hbar/2. This connects the CTP formalism to quantum mechanics. It is a normalization, not a physical axiom."
- This reduces the axiom count from three to two (A0 + A1), with A2 as a definition.

---

## Priority for v6 Development

| Priority | Frontier | What to do | Difficulty |
|----------|----------|-----------|------------|
| 1 | F1 (z_target formalism) | Write the explicit variational map from S_CTP to each sector | Medium (writing, not computing) |
| 2 | F3 (QG conditions 3+4) | Solve backreaction loop; analyze BH attractor | High |
| 3 | F4 (DM closure) | Extend model: gauge symmetry, portal, or relic density | Medium |
| 4 | F2 (cosmology) | 3-loop S_CTP at de Sitter | Very high (research frontier) |
| 5 | F5 (tau reframe) | Rewrite A2 as definition | Easy (writing only) |

---

## What v6 Would Look Like

- **Two axioms** (A0: CTP doubling, A1: directed response) + one definition (tau_I normalization)
- **One explicit CTP action** → z_target derived for each sector as a limit (formalized, not conceptual)
- **4/5 or 5/5 QG closures** (backreaction + BH info)
- **DM with unique lambda** (from gauge extension or relic density)
- **Precision cosmology** (if 3-loop calculation done; otherwise stays structural)
- **~85-95% of a ToE** (up from 70-75%)

---

## The Experimental Program (Independent of v6 Theory)

1. **USL decoherence plateau** — primary falsification test. Gold microsphere, R ~ 0.5-1 um, ultra-high vacuum. Timeline: 2027-2030 with levitated optomechanics.
2. **Cross-species gamma-tubulin correlation** — neuroscience test of the 40 Hz coincidence. Can be done now.
3. **R_anomaly precision** — tightens H_inf prediction and DM parameter space.
4. **Heating/radiation bounds** — full constraint analysis against underground experiments and precision oscillators.

Theory and experiment develop in parallel. The plateau measurement is the single most important external input.

---

*D. Ryan Grover, April 2026. Bridge document for GRUT v5 → v6.*
