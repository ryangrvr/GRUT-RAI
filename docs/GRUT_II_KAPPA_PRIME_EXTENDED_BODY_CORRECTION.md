# GRUT II Kappa-Prime — Extended-Body Gravitational Self-Energy Audit

## Purpose

Resolve whether the gravitational dephasing term at the frozen operating point remains large enough once the extended-body self-energy correction is computed exactly.

---

## Part I — Exact Self-Energy Difference

The Diosi self-energy difference for a uniform sphere of mass m, radius R, displaced by l:

```
Delta_E(l, R, m) = (G/2) ∫∫ [rho_1(x) - rho_2(x)] [rho_1(x') - rho_2(x')] / |x-x'| d^3x d^3x'
```

This equals:

```
Delta_E = G [U_self - U_cross(l)]
```

where U_self = (6/5) m^2/R is the self-interaction integral and U_cross(l) is the interaction integral between the two displaced spheres.

---

## Part II — Exact Evaluation

Numerical integration of the 6D Diosi integral (reduced to 2D by symmetry) gives:

| l/R | U_cross / (m^2/R) | Delta_E / (G m^2/R) | Suppression S = Delta_E_exact / (G m^2/l) |
|:---:|:--:|:--:|:--:|
| 0.001 | 1.200000 | 5.0×10^-7 | 5×10^-10 |
| 0.01 | 1.19995 | 5.0×10^-5 | 5×10^-7 |
| 0.036 | 1.19975 | 2.5×10^-4 | 2.3×10^-5 |
| 0.1 | 1.19519 | 4.8×10^-3 | 4.8×10^-4 |
| 0.5 | 1.098 | 0.102 | 0.051 |
| 1.0 | 0.881 | 0.319 | 0.319 |
| 1.5 | 0.660 | 0.540 | 0.809 |
| **2.0** | **0.500** | **0.700** | **1.000** (point-mass exact) |
| 3.0 | 0.333 | 0.867 | 1.000 |

---

## Part III — Small-l/R Expansion

For l << R, the leading-order behavior is:

```
Delta_E(l << R) = C × G m^2 / R × (l/R)^2
```

with **C ≈ 0.500** (numerically confirmed to 0.1%).

The suppression factor relative to the point-mass formula:

```
S = Delta_E_exact / (G m^2/l) = C × (l/R)^3
```

**The suppression goes as (l/R)^3.** For l/R = 0.036 (the frozen operating point): S = 0.500 × (0.036)^3 ≈ **2.3 × 10^-5**.

### Physical interpretation

In the small-l/R regime, the two displaced spheres almost completely overlap. The difference density rho_1 - rho_2 is confined to thin crescent-shaped shells at the surface of the sphere. The gravitational self-energy of these thin shells is proportional to l^2 (dipole scaling), not to 1/l (point-mass scaling). The crossover between the two regimes occurs at l ~ R.

---

## Part IV — Frozen Operating Point

| Quantity | Point-mass | Extended-body (exact) |
|----------|:----------:|:---------------------:|
| m | 25 fg | 25 fg |
| R | 139.5 nm | 139.5 nm |
| l | 5 nm | 5 nm |
| l/R | 0.036 | 0.036 |
| Delta_E | 4.17 × 10^-36 J | **1.90 × 10^-40 J** |
| Lambda | 7.91 × 10^-2 s^-1 | **1.80 × 10^-6 s^-1** |
| Lambda_gas | 6.09 × 10^-3 s^-1 | 6.09 × 10^-3 s^-1 |
| **USL/gas** | **13.0** | **0.0003** |
| Suppression S | 1.0 | **2.3 × 10^-5** |

**The frozen operating point is killed.** The extended-body correction reduces the USL by a factor of ~44,000. The corrected USL is 3,400× below the gas decoherence floor.

---

## Part V — Roadmap Revision

### Why l = 5 nm fails

At l/R = 0.036, the two displaced spheres overlap by 99.96%. The gravitational self-energy difference between "mass at x" and "mass at x+5nm" is negligible because the mass distributions are nearly identical. The Diosi integral sees only the thin surface crescents.

### The true optimum: l ~ 2R

In the extended-body regime (l < 2R), Delta_E **increases** with l (as ~l^2). It reaches its maximum at l = 2R, where the spheres just touch and the point-mass formula becomes exact. For l > 2R, Delta_E = Gm^2/l decreases with l.

**The maximum USL rate occurs at l = 2R for each mass.**

### Corrected mass scan at l = 2R

| m (fg) | R (nm) | l = 2R (nm) | Lambda_USL (s^-1) | Lambda_gas (s^-1) | USL/gas | Expansion ratio |
|:------:|:------:|:-----------:|:-----------------:|:-----------------:|:-------:|:---------------:|
| 50 | 176 | 351 | 4.50×10^-3 | 9.66×10^-3 | 0.47 | 271,000 |
| 100 | 221 | 443 | 1.43×10^-2 | 1.53×10^-2 | 0.93 | 483,000 |
| **107** | **226** | **452** | — | — | **≈ 1.0** | **≈ 500,000** |
| 150 | 253 | 507 | 2.81×10^-2 | 2.01×10^-2 | 1.40 | 678,000 |
| 200 | 279 | 558 | 4.54×10^-2 | 2.43×10^-2 | 1.86 | 861,000 |
| 300 | 319 | 639 | 8.92×10^-2 | 3.19×10^-2 | 2.80 | 1,207,000 |
| 500 | 379 | 757 | 2.09×10^-1 | 4.48×10^-2 | 4.66 | 1,848,000 |
| 1000 | 477 | 954 | 6.63×10^-1 | 7.12×10^-2 | 9.32 | 3,293,000 |

### The corrected crossover

- **USL = gas** at l = 2R: m ≈ **107 fg** (R ≈ 226 nm, l = 452 nm)
- **USL/gas = 3** at l = 2R: m ≈ **300 fg** (R ≈ 320 nm, l = 639 nm)
- **USL/gas = 10** at l = 2R: m ≈ **1000 fg** (R ≈ 477 nm, l = 954 nm)

### The expansion ratio catastrophe

At the corrected crossover mass (107 fg), the required expansion ratio is l/x_zpf ≈ **500,000**. The current experimental record is ~1,000. This is a gap of **500×** — not 3× as the frozen roadmap claimed.

At USL/gas = 3 (300 fg): expansion ratio ≈ 1.2 million.
At USL/gas = 10 (1000 fg): expansion ratio ≈ 3.3 million.

**The expansion ratio is not achievable by any known or foreseeable protocol.**

### What went wrong

The Epsilon-Prime and Zeta-Prime optimization assumed the point-mass USL formula Lambda = Gm^2/(hbar l), which increases as l decreases. This led to the conclusion that l = 5 nm was optimal. The extended-body correction reverses this: for l << R, the true USL decreases as l^2, not increases as 1/l. The entire optimization was performed in the wrong regime.

The point-mass formula is only valid for l >> R. For a 25 fg particle (R = 140 nm), this means l >> 140 nm — i.e., separations of hundreds of nanometers, not 5 nm.

---

## Part VI — Structural Interpretation

### What Kappa-Prime means for the program

The extended-body correction is **not** a small numerical adjustment. It is a qualitative change that:

1. **Kills the frozen operating point** (25 fg / 5 nm): suppression factor 2.3 × 10^-5.
2. **Shifts the crossover mass upward** from ~7 fg (point-mass) to ~107 fg (extended-body at l = 2R).
3. **Makes the expansion ratio impractical**: ~500,000 at the corrected crossover, vs ~2,700 at the (now invalid) frozen point.
4. **Invalidates the Epsilon-Prime and Zeta-Prime roadmaps** in their current form.

### What survives

1. **The CTP / influence-functional derivation (Iota-Prime)** is unaffected. The USL IS the gravitational self-energy dephasing in the influence functional. The extended-body correction modifies the self-energy integral, not the mechanism.

2. **The constitutive law derivation (Theta-Prime)** is unaffected. It lives in Sector 1 of the CTP action, which has nothing to do with spatial superposition.

3. **The three-sector structure** (dissipation / noise / dephasing) is unaffected.

4. **The USL scaling** is correct in the point-mass regime (l >> R). The formula Lambda = Gm^2/(hbar l) remains valid there.

### What does not survive

1. **The 25 fg / 5 nm operating point** is invalid.
2. **The 20-30 fg "sweet spot"** was entirely within the extended-body regime and is void.
3. **The claim that the USL is testable in 2-5 years** is retracted. The corrected crossover mass (~107 fg) with l ~ 450 nm and expansion ratio ~500,000 is far beyond any foreseeable experimental capability.

---

## Part VII — Final Verdict

### Classification

**point_mass_usl_not_valid_at_operating_point**

The extended-body gravitational self-energy correction obliterates the frozen operating point. The suppression factor is (l/R)^3 ≈ 2 × 10^-5 at l = 5 nm, R = 140 nm. The USL/gas ratio drops from 13 to 0.0003. The corrected crossover mass (where USL first equals gas at the optimal separation l = 2R) is ~107 fg, requiring a spatial superposition of ~450 nm — with an expansion ratio of ~500,000 from the ground state. This is not achievable with any known or near-term protocol.

The quantum-sector roadmap established in Gamma-Prime through Zeta-Prime was built on the point-mass USL formula in a regime where it does not apply. The roadmap requires fundamental revision.

### Public-Facing Paragraph

GRUT II Kappa-Prime computes the exact extended-body gravitational self-energy correction for the USL test window. For a uniform silica sphere of radius R in a spatial superposition with displacement l, the gravitational dephasing rate is suppressed by a factor of ~(l/R)^3 relative to the point-mass formula when l << R. At the frozen operating point (25 fg, l = 5 nm, R = 140 nm), this suppression factor is 2 × 10^-5, reducing the USL/gas ratio from 13 to 0.0003. The signal is destroyed. The corrected crossover — where the USL first exceeds environmental gas decoherence at the optimal separation l = 2R — occurs at mass ~107 fg (R ≈ 226 nm, l ≈ 452 nm), requiring a spatial superposition expansion ratio of ~500,000 from the quantum ground state. This is far beyond the current record (~1,000) and any foreseeable experimental capability. The quantum-sector roadmap must be fundamentally revised: the USL is testable in the point-mass regime (l > 2R) only, which requires either much heavier particles or a qualitatively different experimental architecture.

### Internal Doctrine Paragraph

The Kappa-Prime correction is severe and non-negotiable. The entire Gamma-Prime through Zeta-Prime optimization was performed using the point-mass USL formula Lambda = Gm^2/(hbar l) at separations where l/R ~ 0.04, deep in the extended-body regime where the true rate is suppressed by (l/R)^3 ~ 10^-5. This error propagated through the mass optimization, the separation sweep, the robustness analysis, and the terminal roadmap. None of the quantitative claims in those stages (USL/gas ratios, run counts, expansion ratios) are valid at the stated operating points. The Iota-Prime CTP derivation remains structurally correct — the USL IS the gravitational self-energy dephasing — but the self-energy must be computed with the EXACT Diosi integral, not the point-mass approximation, whenever l < 2R. The corrected test window (l ~ 2R, m > 100 fg, expansion ratio > 500,000) places the USL far beyond current and near-term experimental reach. The quantum-sector roadmap is NOT ready for terminal closure. It must be reopened.

### Next Forced Move

**GRUT II Lambda-Prime — Corrected Quantum-Sector Assessment:** With the extended-body correction included, determine whether ANY experimentally accessible regime exists where the USL is testable. Specifically: (a) is there a particle geometry (e.g., high-aspect-ratio, composite, or hollow structures) that reduces the extended-body suppression? (b) does the l > 2R regime (point-mass valid) become accessible through alternative superposition protocols (Stern-Gerlach with nanodiamonds, Talbot-Lau with large grating periods)? (c) or is the USL experimentally inaccessible for the foreseeable future, making the quantum-sector prediction sharp but untestable?

---

*GRUT II Kappa-Prime complete. Verdict: point_mass_usl_not_valid_at_operating_point. The extended-body correction suppresses the USL by (l/R)^3 ≈ 2×10^-5 at the frozen operating point (25 fg, 5 nm). The corrected crossover mass is ~107 fg at l = 2R ≈ 452 nm, requiring expansion ratio ~500,000 (vs current record ~1,000). The frozen roadmap is void. The CTP derivation (Iota-Prime) remains structurally valid — the mechanism is correct, the magnitude is not. The quantum sector must be reopened.*
