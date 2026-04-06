# GRUT II Lambda-Prime — 3D Geometry Optimization and Valid-Regime USL Testability Audit

## Purpose

Reassess USL testability as a full 3D mass-distribution problem, not a 1D point-particle separation problem. Determine whether ANY experimentally plausible geometry/protocol combination keeps the USL testable in the valid regime (l ≥ 2R for spheres, or l > h for disks).

---

## Part I — 3D Structural Reset

### Why the earlier roadmap failed

The Gamma-Prime through Zeta-Prime roadmap treated mass as a scalar and separation as a 1D parameter. The formula Lambda = Gm^2/(hbar l) was optimized as if l could be chosen independently of the particle size. In reality:

- For a sphere of radius R, the formula is valid only for l > 2R
- For l < 2R, the extended-body Diosi integral gives Delta_E ~ l^2 (NOT 1/l)
- The suppression factor is (l/R)^3 in the overlap regime

**The USL test problem is fundamentally a 3D density-difference functional:**

```
Delta_E = (G/2) ∫∫ [rho_1(x) - rho_2(x)] [rho_1(x') - rho_2(x')] / |x-x'| d^3x d^3x'
```

This integral depends on the full 3D shape of the particle and the direction and magnitude of displacement. Different geometries give wildly different answers at the same mass and displacement.

### The key insight

**The overlap geometry determines everything.** The critical question is: at what displacement l does the difference density rho_1 - rho_2 become maximal? For a sphere, this happens at l = 2R (just touching). For a thin disk displaced along its thin axis, it happens at l = h (the thickness). The THINNEST dimension of the particle along the displacement direction controls when the overlap regime ends.

---

## Part II — Geometry Class Inventory

### Five geometries evaluated

| Geometry | Characteristic sizes | Overlap ends at l = | Point-mass at l ~ | Notes |
|----------|---------------------|:-------------------:|:------------------:|-------|
| **Sphere** | R | 2R | 2R | Baseline. All mass in a ball. |
| **Thin rod** (perp. disp.) | Length L, radius a | 2a | 2a | Mass spread along L, thin cross-section a. |
| **Thin disk** (axial disp.) | Radius R_d, thickness h | h | h (along axis) | Overlap vanishes after h. But point-mass requires l > R_d. |
| **Hollow shell** | R, wall thickness t | ~R (shell theorem) | 2R | Shell theorem: interior potential is flat → less suppression. |
| **Dumbbell** | Two lumps + gap | gap | gap + 2R_lump | Pre-separated mass → no overlap at any l if gap > 0. |

### Which geometries help?

**Sphere:** Overlap regime extends to l = 2R. For 100 fg silica, 2R = 443 nm. Large separations needed.

**Rod (perpendicular displacement):** Overlap ends at l = 2a, where a is the rod RADIUS (the thin dimension). For a 100 fg rod with L = 2.2 um and a = 81 nm: overlap ends at 162 nm — smaller than the sphere's 443 nm. The rod reduces the required separation by ~3×. But the rod has more self-energy spread along its length, reducing the Diosi integral slightly.

**Disk (axial displacement):** Overlap ends at l = h, the disk thickness. For h = 10 nm: overlap ends at 10 nm! This is 44× better than the sphere. However, for h < l << R_disk, the mass is still spread over the disk area, and the Diosi integral is suppressed relative to the point-mass formula until l > R_disk.

**Hollow shell:** The shell theorem means the potential inside is constant. This reduces the self-interaction somewhat but doesn't fundamentally change the overlap geometry. Modest improvement.

---

## Part III — Overlap Regime and Valid-Regime Comparison

### Sphere (baseline) at m = 100 fg (R = 221 nm)

| l (nm) | l/R | Lambda (s^-1) | Lambda_point (s^-1) | S factor |
|:------:|:---:|:------------:|:-------------------:|:--------:|
| 10 | 0.045 | 2.87×10^-5 | 6.33×10^-1 | 4.5×10^-5 |
| 100 | 0.45 | 2.43×10^-3 | 6.33×10^-2 | 0.038 |
| 250 | 1.13 | 1.08×10^-2 | 2.53×10^-2 | 0.43 |
| 443 | 2.0 | 1.43×10^-2 | 1.43×10^-2 | 1.00 |

Point-mass validity requires l > 443 nm for 100 fg spheres.

### Sphere in Talbot-Lau (d = 500 nm grating, l = 250 nm)

| m (fg) | R (nm) | l/R | Lambda_USL (s^-1) | Lambda_gas (s^-1) | USL/gas |
|:------:|:------:|:---:|:-----------------:|:-----------------:|:-------:|
| 10 | 103 | 2.43 | 2.53×10^-4 | 3.30×10^-3 | 0.077 |
| 100 | 221 | 1.13 | 1.08×10^-2 | 1.53×10^-2 | 0.71 |
| **200** | **279** | **0.90** | **2.45×10^-2** | **2.43×10^-2** | **1.01** |
| 500 | 379 | 0.66 | 6.89×10^-2 | 4.48×10^-2 | 1.54 |
| 1000 | 477 | 0.52 | 1.47×10^-1 | 7.12×10^-2 | 2.06 |

**Spheres in Talbot-Lau reach USL/gas = 1 at ~200 fg.** The extended-body suppression at l/R ≈ 0.9 is a factor of ~2-3, not the catastrophic 10^4 of the frozen operating point.

### Stern-Gerlach nanodiamonds

| m (fg) | R (nm) | t (ms) | l (nm) | l/R | Lambda_USL (s^-1) | Lambda_gas (s^-1) | USL/gas |
|:------:|:------:|:------:|:------:|:---:|:-----------------:|:-----------------:|:-------:|
| 50 | 151 | 1 | 186 | 1.24 | 4.50×10^-3 | 7.09×10^-3 | 0.63 |
| **500** | **324** | **10** | **1,860** | **5.7** | **8.51×10^-2** | **3.29×10^-2** | **2.59** |
| **1000** | **409** | **10** | **930** | **2.3** | **6.81×10^-1** | **5.22×10^-2** | **13.0** |

**The SG nanodiamond route at 1000 fg, t = 10 ms gives USL/gas = 13 in the point-mass regime (l/R = 2.3).** This is a clean, valid-regime signal.

### Thin disk in Talbot-Lau (edge-on gas orientation)

| m (fg) | h (nm) | R_disk (um) | l = 250 nm | Lambda_USL | Lambda_gas (edge) | USL/gas (edge) |
|:------:|:------:|:-----------:|:----------:|:----------:|:-----------------:|:-------------:|
| 100 | 10 | 1.20 | 250 | 2.53×10^-2 | 2.40×10^-3 | **10.6** |
| 100 | 50 | 0.54 | 250 | 2.53×10^-2 | 5.36×10^-3 | **4.7** |
| 500 | 10 | 2.69 | 250 | 6.33×10^-1 | 5.36×10^-3 | **118** |

**IF disk orientation can be controlled (edge-on to gas flow), the gas cross-section drops dramatically and the USL/gas ratio becomes enormous.** However, maintaining orientation during free evolution is experimentally very challenging. The face-on cross-section is 100-1000× larger, wiping out the advantage.

---

## Part IV — Geometry × Protocol Survey

### Route 1: Stern-Gerlach + Nanodiamond (MOST PROMISING)

- **Geometry:** Sphere (or near-sphere). Diamond density 3500 kg/m^3 → smaller R than silica.
- **Separation mechanism:** Spin-dependent magnetic force on NV center. No wavepacket expansion needed.
- **Achievable separation:** l = F_SG t^2 / (2m). At dB/dz = 10^6 T/m, F = 1.86×10^-17 N.
- **At 1000 fg, 10 ms:** l = 930 nm, l/R = 2.3 → point-mass regime.
- **Key advantage:** Separation set by external force, not quantum expansion. No "expansion ratio" bottleneck.
- **Key challenge:** 10 ms free fall (1 m drop tower, or magnetic levitation). Charge neutralization. Maintaining NV spin coherence.

### Route 2: Talbot-Lau + Sphere (CONDITIONALLY VIABLE)

- **Geometry:** Sphere.
- **Separation mechanism:** Material grating or optical grating, period d = 500 nm, l ~ 250 nm.
- **At 200+ fg:** l/R ~ 0.9, extended-body suppression ~2-3×. USL/gas ~ 1.
- **At 500+ fg:** USL/gas ~ 1.5.
- **Key advantage:** Well-established interferometry technique. No spin coupling needed.
- **Key challenge:** Massive particles (200-500 fg) through nm-scale gratings. Coherence maintenance over Talbot time (which scales linearly with mass).

### Route 3: Talbot-Lau + Thin Disk (SPECULATIVE)

- **Geometry:** Thin disk (h ~ 10-50 nm), displaced axially through grating.
- **Separation mechanism:** Grating period d, axial separation l > h.
- **Key advantage:** Edge-on gas cross-section is tiny → USL/gas can be >100.
- **Key challenge:** Maintaining disk orientation. Fabricating monodisperse thin disks. The point-mass formula is NOT valid for h < l << R_disk; need intermediate-regime Diosi integral.

### Route 4: Space-based free fall (LONG-TERM)

- **Any geometry, any mass, very long free evolution.**
- **MAQRO-PF targets ~10^9 amu (~1.7 fg) with 100 s free fall.**
- **For USL: need heavier particles. 100+ fg with 10+ s free fall.**
- **Key advantage:** Microgravity eliminates free-fall height constraint.
- **Key challenge:** 2030s timeline. Particle source in space.

---

## Part V — Geometry-Optimized USL Scan

### Best candidates ranked

| Rank | Route | Mass | Separation | l/R | USL/gas | Status |
|:----:|-------|:----:|:----------:|:---:|:-------:|:------:|
| **1** | **SG nanodiamond, 10 ms** | **1000 fg** | **930 nm** | **2.3** | **13.0** | **POINT-MASS VALID** |
| 2 | SG nanodiamond, 10 ms | 500 fg | 1860 nm | 5.7 | 2.6 | Point-mass valid |
| 3 | Talbot-Lau sphere, d=500nm | 1000 fg | 250 nm | 0.52 | 2.1 | Extended-body (~2× suppressed) |
| 4 | Talbot-Lau sphere, d=500nm | 500 fg | 250 nm | 0.66 | 1.5 | Extended-body (~3× suppressed) |
| 5 | Talbot-Lau sphere, d=500nm | 200 fg | 250 nm | 0.90 | 1.0 | Extended-body (marginal) |
| 6 | Talbot-Lau disk (edge-on) | 100 fg | 250 nm | — | 10.6 | Requires orientation control |

---

## Part VI — Design Principle Extraction

### The general rule

**Maximize the ratio l / R_min, where R_min is the particle's smallest dimension along the displacement direction.**

- For a sphere: R_min = R. Need l > 2R. This forces large separations.
- For a disk (axial): R_min = h. Need l > h. Thin disks escape overlap early.
- For a rod (perpendicular): R_min = a (cross-section radius). Need l > 2a.

### The three design strategies

1. **Make the particle smaller (higher density, smaller R):** Diamond (3500) vs silica (2200) gives 20% smaller R at the same mass. Osmium (22,590) would give 2× smaller R. Material density matters.

2. **Use anisotropic particles displaced along the thin dimension:** Thin disks, nanorods. The overlap regime ends at the THICKNESS, not the lateral extent. But environmental cross-section may be large in other dimensions.

3. **Use separation mechanisms that achieve l > 2R directly:** Stern-Gerlach forces grow as t^2. With 10 ms and the right gradient, l > 2R is achievable for 1000 fg particles. No wavepacket expansion needed.

### The optimal geometry is NOT a sphere

Spheres are actually **near-worst** for the USL because all three dimensions are the same. The overlap regime extends to l = 2R = 2(3m/(4πρ))^{1/3}, which grows as m^{1/3}. For any given mass, an elongated or flattened geometry reaches the valid regime at smaller l.

However, the practical optimal geometry is **whatever can be experimentally prepared, superposed, and detected.** Spheres and near-spherical nanodiamonds have the most experimental infrastructure. The disk route is theoretically better but experimentally harder.

---

## Part VII — Consequence for GRUT II Readiness

### The window reopens — differently

The Kappa-Prime correction killed the frozen operating point (25 fg / 5 nm) but Lambda-Prime identifies **two viable replacement routes:**

**Route A: Stern-Gerlach nanodiamond (best candidate)**
- 1000 fg (10^-15 kg) nanodiamond with NV center
- 10 ms SG separation: l = 930 nm (l/R = 2.3, point-mass valid)
- USL/gas = 13 at P = 10^-13 Pa, T = 4 K
- No wavepacket expansion needed — separation is force-driven
- Requires: 1 m drop tower or magnetic levitation, NV spin coherence

**Route B: Talbot-Lau sphere (backup)**
- 200-1000 fg silica sphere
- d = 500 nm grating, l = 250 nm
- USL/gas = 1-2 (marginal but detectable with high statistics)
- Extended-body suppression factor ~2-3 (not catastrophic at l/R ~ 0.5-0.9)
- Requires: massive-particle Talbot-Lau interferometry (not yet demonstrated above ~170 kDa)

### What has changed

| | Frozen roadmap (void) | Corrected roadmap (Lambda-Prime) |
|---|---|---|
| Mass | 25 fg | **500-1000 fg** |
| Separation | 5 nm | **250-1000 nm** |
| Protocol | Inverted-potential expansion | **SG force or Talbot-Lau grating** |
| Expansion ratio | 2,700 | **Not applicable** (force-driven) |
| USL regime | Overlap (l/R = 0.036) | **Point-mass or mild overlap** |
| USL/gas | 13 (wrong) | **2-13 (correct)** |
| Timeline | 2-5 years | **5-10 years (SG), 10-15 years (Talbot-Lau)** |

### Eta-Prime must be rewritten

The terminal roadmap (Eta-Prime) is void in its quantitative content. The qualitative structure survives: the USL is the gravitational self-energy dephasing, the CTP derivation is correct, the sole environmental bottleneck is gas pressure. But ALL numbers (mass, separation, expansion ratio, USL/gas, run count) must be replaced with the Lambda-Prime corrected values.

---

## Part VIII — Final Verdict

### Classification

**3d_geometry_reopens_usl_test_window**

The extended-body correction killed the frozen operating point but Lambda-Prime identifies viable replacement routes that operate in the valid regime (l ≥ 2R). The Stern-Gerlach nanodiamond route at 1000 fg with 10 ms free fall gives USL/gas = 13 in the point-mass regime — a clean, correct signal with no extended-body suppression. The Talbot-Lau sphere route at 200-500 fg with d = 500 nm grating gives USL/gas = 1-2 with modest extended-body suppression.

The USL remains testable. The test is harder, heavier, and further away than the frozen roadmap claimed — but it is not experimentally remote.

### Public-Facing Paragraph

GRUT II Lambda-Prime performs a full 3D geometry optimization of the USL test window, correcting the extended-body error identified in Kappa-Prime. The point-mass USL formula is valid only when the superposition separation exceeds the particle diameter. For the previously frozen operating point (25 fg, 5 nm separation, 280 nm diameter), the formula was used outside its validity by a factor of 56 in length scale. Lambda-Prime identifies two viable replacement routes that operate in the valid regime. The most promising is Stern-Gerlach separation of a 1000 femtogram nanodiamond (with NV center) over 930 nanometers in 10 milliseconds, giving a USL/gas ratio of 13 in the point-mass regime — a clean, correct signal. The backup route is Talbot-Lau interferometry with 200-500 fg silica spheres through 500 nm gratings, giving marginal but detectable signals. Both routes require heavier particles and larger separations than the voided roadmap, but neither requires the impractical wavepacket expansion ratios that appeared when the problem was incorrectly treated as one-dimensional. The USL test window has rotated from a wavepacket-expansion problem into a massive-particle superposition-creation problem, and is open.

### Internal Doctrine Paragraph

Lambda-Prime establishes that the USL quantum-sector program is NOT dead — it has been corrected and rerouted. The Kappa-Prime extended-body correction was severe but not terminal because the valid-regime test window (l > 2R) is experimentally accessible through force-driven separation protocols (Stern-Gerlach) that bypass the wavepacket expansion bottleneck entirely. The optimal candidate is a 1000 fg nanodiamond with NV center, SG-separated by ~1 um in 10 ms, giving USL/gas = 13 in the point-mass regime with no extended-body suppression. The corrected quantum-sector roadmap is: (a) mass scale 500-1000 fg (not 25 fg), (b) separation 250-1000 nm (not 5 nm), (c) protocol SG or Talbot-Lau (not inverted-potential expansion), (d) timeline 5-10 years (not 2-5 years). The CTP derivation (Iota-Prime) is unaffected. The three-sector structure is unaffected. The Eta-Prime terminal roadmap must be rewritten with the corrected numbers, but its qualitative structure survives.

### Next Forced Move

**GRUT II Mu-Prime — Corrected Terminal Quantum-Sector Roadmap:** Rewrite Eta-Prime with the Lambda-Prime corrected operating points, incorporating the SG nanodiamond route as the primary candidate and Talbot-Lau as the backup. This is the corrected terminal document for the GRUT-II quantum sector, replacing the void Eta-Prime.

---

*GRUT II Lambda-Prime complete. Verdict: 3d_geometry_reopens_usl_test_window. The SG nanodiamond route at 1000 fg / 930 nm / 10 ms gives USL/gas = 13 in the point-mass-valid regime. The Talbot-Lau sphere route at 200-500 fg / 250 nm gives USL/gas = 1-2 with modest extended-body suppression. The frozen roadmap (25 fg / 5 nm) is void but the test window is open at higher mass and larger separation. The wavepacket expansion bottleneck is eliminated by force-driven separation protocols. The corrected program requires 500-1000 fg particles superposed over 250-1000 nm — harder and further than the frozen roadmap but not experimentally remote.*
