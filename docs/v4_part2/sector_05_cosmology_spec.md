# Sector 5 — Cosmology: Specification

## Sector name
Cosmology

## Status
**Partial / Conditional**

## Claim boundary

The cosmology sector has significant computational infrastructure — including H(z) evolution, LCDM reference comparisons, lensing and rotation-curve calculators, Hubble-tension metrics, and bounce/dark-sector analysis modules. However, key physics claims have FAILED:

**What is implemented and working:**
- Homogeneous background evolution with constitutive memory coupling (H(z), Omega_m, growth)
- LCDM reference baseline for comparison
- Hubble-tension residual metrics (E(z), fsigma8)
- Lensing calculator (convergence, shear, magnification)
- Rotation-curve analyzer
- Cosmological bounce analysis (singularity softening, not a full bounce)
- Dark-sector dual-track analysis (DM/DE interpretation framework)
- Cosmological viability audit (screening-length analysis)

**What has FAILED and is WITHDRAWN:**
- **Dark-energy replacement** (XII Alpha): rho_eq < 0 is anti-accelerating; w = -1 has wrong sign. PERMANENTLY FAILED. This is a nonclaim.
- **Late-universe cosmological modification**: no viable route found.

**What is conditional / frontier:**
- Dynamical cosmological regulator (three-regime H*tau transition) — conditional on XII Alpha revision
- Early-universe modification at T ~ 10^12 K — conditional, not validated

**What is NOT claimed:**
- No dark-energy solution
- No cosmological closure
- No late-universe modification
- No precision perturbation spectrum
- No CMB/BAO fit
- Screening length lambda is a FREE PARAMETER (naturalness problem)

## Dependencies

- **Sector 1:** QM backbone
- **Sector 4:** Gravity identity (matter within GR)
- **A0-A2:** Foundational axioms
- **GR + FRW:** Standard cosmological background (external)

## Deliverables

| # | Deliverable | Path |
|---|-------------|------|
| 1 | Specification | this file |
| 2 | Math scaffold | `docs/v4_part2/sector_05_cosmology_math.md` |
| 3 | Code interface | `grut_solver/sectors/cosmology/` |
| 4 | Validation tests | `tests/sectors/cosmology/test_sector_05.py` |
| 5 | Notebook | `notebooks/sector_05_cosmology.py` |
| 6 | Paper summary | `docs/v4_part2/sector_05_cosmology_for_paper.md` |

## Closure condition

This sector is NOT closed. Closure would require:
1. A working dark-energy mechanism (current one failed permanently)
2. Precision perturbation spectrum matching CMB/BAO
3. Natural determination of the screening length (currently free)
4. Full observational fit (H(z), fsigma8, CMB, BAO, SNIa)

The computational infrastructure for testing candidate mechanisms exists. The current physics falls short of cosmological closure.
