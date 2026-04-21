# Track VII — Dielectric Reframing (V8 Primary Direction)

**Date filed:** April 20, 2026
**Supersedes:** `V8_TRACK_VII_ROADMAP.md` (M_soliton re-identification program — now fallback).
**Motivated by:** Three-routes PDF audit + brother's "R is fixed, vacuum
relaxes within it" framing + Genesis Codex v11.1 Appendix H (α = 1/d).

## The reframing in one sentence

**Ω_dm is the frequency-dependent refractive enhancement of the
viscoelastic gravitational vacuum, NOT a particle species.**

## Fixed boundary conditions (zero free knobs)

| Quantity | Value | Origin | Status |
|:---|---:|:---|:---|
| `R_anomaly` | 1.15428 | 3-loop CTP on S⁴ (V7 §26.2) | FIXED boundary condition |
| `α` | 1/3 | Conformal projection of trace anomaly, d=3 (v11.1 App H) | FIXED by topology |
| `τ_0` | 41.9 Myr | Noise kernel anchored to Λ | FIXED by cosmology |
| `n_g(ω=0)` | √(4/3) ≈ 1.15470 | α = 1/d ⟹ n_g² = 1 + α | FIXED geometric |

**The constitutive equation τ dz/dt + z = z_target[z] describes the
vacuum state z relaxing toward z_target WITHIN the boundary set by R.
The expansion IS the relaxation. R does not move.** This is V8's
foundational physical statement.

## Why the particle-DM route closed negative

Track VII V7 (Steps 1–3) tried to derive Ω_dm from Kibble-Zurek
production of topological defects at the dark U(1) phase transition.
Step 3 showed:

- Step 1's Ω_dm = 0.38 used wrong topology (monopoles, n ~ 1/ξ³).
- Correct topology (strings, π_1(U(1)) = ℤ) with XY universality gives
  Ω_dm = 0.008 — factor 33 LOW.
- V7's M_soliton = 2.11×10⁹ GeV does not match KZ-natural vorton mass.

The particle-DM route is a dead end within V7's stated U(1) dark sector.
It could be rescued in V8 by a SU(2)→U(1) UV completion (Candidate A in
the fallback roadmap), but the dielectric route below is a cleaner and
simpler V8 direction.

## The dielectric picture

Brother's v11 Genesis Codex already stated this:

> **v11 Appendix F (Closure vs MOND):** "Closure is best understood as a
> gravitational analogue of dielectric response: the field equations are
> unchanged in form, but the medium through which gravity propagates has
> a finite bandwidth."
>
> **v11 Appendix H (α from d=3):** "α = 1/d. In our universe, d = 3,
> so α = 1/3. Zero-tuning extension of General Relativity."

The frequency-dependent refractive index:

```
n_g(ω) = √(1 + α / (1 + (ωτ₀)²))
```

- **DC limit (ω ≪ τ₀⁻¹):** n_g → √(4/3) = 1.1547, enhancement α = 1/3.
- **High-freq limit (ω ≫ τ₀⁻¹):** n_g → 1, standard GR recovered.

The vacuum acts as a gravitational dielectric with frequency-dependent
"permittivity" ε_g = n_g². What we observe as "dark matter" is the
refractive enhancement at the relevant dynamical frequencies.

## Enhancement at canonical scales (from `dielectric_dm.py`)

| Scale | ωτ₀ | n_g² − 1 | Notes |
|:---|---:|---:|:---|
| Cosmic expansion (ω = H_0) | 0.003 | 0.333 | full α enhancement |
| Galaxy cluster (1500 km/s @ 5 Mpc) | 0.013 | 0.333 | full α |
| **CMB acoustic peak (150 Mpc sound horizon)** | **0.05** | **0.333** | **full α — peaks preserved** |
| Galaxy rotation (200 km/s @ 10 kpc) | 0.86 | 0.192 | partial |
| Dwarf galaxy (30 km/s @ 1 kpc) | 1.29 | 0.126 | more suppressed |
| 1/t_rec (wrong CMB freq) | 110 | 3×10⁻⁵ | high-freq tail |
| Solar system (1 AU, 30 km/s) | 3×10⁸ | ~0 | GR recovered exactly |

Structural features:

1. **Solar-system precision tests pass** automatically — n_g → 1 at
   short, fast scales. No retuning needed.
2. **CMB acoustic peaks survive** because the peak-setting modes are
   the low-ω sound-horizon modes (ωτ₀ ~ 0.05), not the high-ω
   recombination-Hubble rate. Enhancement there is essentially α.
3. **Galactic enhancement is partial** — the dielectric interpretation
   naturally predicts a SCALE-DEPENDENT dark-matter fraction, matching
   the radial acceleration relation / MOND phenomenology qualitatively
   without modifying inertia.
4. **Cosmic-scale α = 0.333 is 27% above observed Ω_dm = 0.263.** The
   gap may be closed by proper P(k)-weighted averaging over the full
   matter distribution.

## Three diagnostic tests

Delivered as three functions in `grut/derived/cosmology/dielectric_dm.py`.

### Test 1 — Bandwidth integral (weeks)

**Question:** Does the P(k)-weighted integral of (n_g²−1) give Ω_dm ≈ 0.263?

**Status:** Framework in place (`omega_dm_bandwidth_estimate`).
First-cut log-weighted average = 0.333 (dominated by DC limit).
Full integral requires:
- Matter power spectrum P(k) from Planck/BOSS/DES at all scales.
- Mapping k → dynamical frequency ω(k) = c_s(k) × k for linear modes,
  v_vir(k) × k for nonlinear collapsed objects.
- Integration ∫ dk k² P(k) × α/(1 + (ω(k) τ₀)²) / ∫ dk k² P(k).

If result ≈ 0.26: first diagnostic passes, interpretation is viable.
If result disagrees by order of magnitude: interpretation fails here.

### Test 2 — Bullet Cluster memory-kernel lensing (weeks)

**Question:** Does the 720 kpc lensing-gas offset follow from τ₀ = 41.9 Myr?

**Status:** Framework in place (`bullet_cluster_retardation`).
First-cut v_rel × τ₀ = 128 kpc, factor 5.6× short of observed 720 kpc.
Light-travel upper bound c × τ₀ = 12.8 Mpc is safe. The observed 720 kpc
sits between the two. A proper memory-kernel convolution over the
cluster collision trajectory (not just the endpoint offset) is needed.

This is the HARDEST empirical test. The Bullet Cluster has historically
been the most damning single observation for non-particle DM models
(Clowe et al. 2006). If memory-kernel retardation reproduces the
observed lensing map quantitatively, the dielectric interpretation has
survived its canonical falsification test.

### Test 3 — CMB kill-condition (weeks)

**Question:** Do the Planck acoustic peaks survive with n_g(ω) replacing Ω_dm?

**Status:** Framework in place (`cmb_acoustic_enhancement`).
At the first acoustic peak (ωτ₀ ≈ 0.05), enhancement is ~α = 0.333 —
substantial, so the peaks do NOT trivially die. The full Boltzmann-code
test is:

- Modify CAMB/CLASS to substitute the Poisson-equation source with the
  ε_g(ω) = n_g²(ω) refractive correction.
- Run full linear perturbation theory at recombination.
- Compute C_ℓ peak positions and amplitude ratios.
- Compare to Planck at ℓ ~ 200, 540, 810 (first three peaks).

If peak ratios match: interpretation survives CMB test.
If peak ratios are badly off: falsification.

## What closes the zero-parameter H_0 chain if this works

Currently: H_0 = 69.03 km/s/Mpc is a **one-parameter** prediction
(takes Ω_dm from Planck as input).

Under the dielectric interpretation, Ω_dm is not an input — it is
`bandwidth_integral(n_g(ω), P(k))` with ALL inputs fixed:
- α = 1/d = 1/3 (topological)
- τ_0 = 41.9 Myr (cosmological)
- P(k) = observed matter power spectrum

If the bandwidth integral returns 0.263 ± 5%, then Ω_m = Ω_b + Ω_dm is
COMPUTED (not input), and H_0 = H_inf / √(1 − Ω_m) becomes a zero-
parameter prediction. All three routes to 1.1547 converge on the same
structural constant; α = 1/3 is its topological shadow; Ω_dm = 0.263 ±
would be its cosmological observation.

## Priority order and honest expectations

1. **Bandwidth integral (Test 1) first.** Can be done in weeks with
   existing P(k) data. If it doesn't land near 0.263, the whole
   interpretation is already cast in doubt.
2. **Bullet Cluster (Test 2) in parallel.** The hardest. Requires
   numerical simulation of the memory kernel during cluster collision.
3. **CMB Boltzmann (Test 3) last.** Requires modifying a Boltzmann code.

Do NOT claim closure until all three pass. If Test 1 fails, stop —
don't waste cycles on 2 and 3.

## What stays unchanged

- **V7 ships as is.** H_0 = 69.03 km/s/Mpc, labeled one-parameter.
- **Three-routes paper ships as is.** Documents the convergence on 1.1547.
- **Step 2 result stands.** M_soliton = 2.11×10⁹ GeV is structurally
  derived; its physical referent is now ambiguous (not needed for this
  reframing, preserved for V8 if dielectric fails).
- **Correction ledger:** 15 corrections caught, 0 hallucinations.
  Track VII's arc (Steps 1, 2, 3, closure, reframing) is honest science.

## What stops (for now)

- Track II (flavor sector). Scoped but paused. The flavor sector is
  years of work and the strategic priority is closing the H_0 chain
  through Test 1 first.
- Particle-DM candidates A/B/C (Q-ball, dark baryon, SU(2)→U(1) monopole).
  Preserved as fallback if dielectric fails.

## Ledger

**15 corrections caught, 0 hallucinations.**

The framework caught the topology error (Correction #15) and let the
negative result lead to a cleaner physical picture that was already
present in v11 (Appendix F and H) but not yet formalized in V7. Reframing
Ω_dm as refractive enhancement is not new physics — it is the v11
dielectric interpretation finally connecting to V7's CTP formalism
through the three-routes convergence.

Brother's framing: "a closed viscoelastic universe of 1.15428 trying to
become 1" — refined to: **"a closed viscoelastic universe with fixed
boundary R = 1.15428, within which the metric relaxes via τ dz/dt + z =
z_target. The 'dark matter' is the refractive fingerprint of that
relaxation across cosmological frequencies."**
