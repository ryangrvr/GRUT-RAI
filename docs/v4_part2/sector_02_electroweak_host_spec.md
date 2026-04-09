# Sector 2 — Electroweak / Standard Model Host Structure: Specification

## Sector name
Electroweak / Standard Model Host Structure

## Status
**Recovered host structure**

## Claim boundary

GRUT recovers the electroweak gauge structure of the Standard Model by promoting the target functional's gradient to a covariant derivative and organizing the directed-response field into SU(2) × U(1)_Y multiplets. The Higgs mechanism generates gauge boson and fermion masses through spontaneous symmetry breaking of the target functional.

**What is claimed:**
- U(1) gauge coupling enters structurally through D_mu = d_mu + ieA_mu in F[z,A]
- The Lorentz force and Aharonov-Bohm phase are recovered
- SU(2) × U(1)_Y multiplet structure reproduces charge quantization Q = T^3 + Y/2
- All three anomaly cancellation conditions are satisfied exactly (sum Y, sum Y^3, SU(2)^2 U(1)_Y)
- The Higgs VEV breaks SU(2) × U(1)_Y -> U(1)_EM
- W/Z masses, photon massless, rho = 1 at tree level
- Fermion masses M_f = y_f v / sqrt(2) from Yukawa couplings
- The free-parameter count matches the Standard Model (~20)

**What is NOT claimed:**
- No flavor closure (Yukawa couplings remain free)
- No species-mass prediction
- No beyond-SM phenomenology
- No parameter reduction relative to the SM
- The gauge group SU(2) × U(1)_Y is assumed, not derived

## Dependencies

- **Sector 1:** QM recovery (Schrodinger backbone, constitutive law, target functional)
- **A0:** CTP doubling (for open-system extension if needed)
- **A1:** Directed response (the constitutive equation)
- **A2:** Complex relaxation with tau_I = hbar/2

## Deliverables

| # | Deliverable | Path |
|---|-------------|------|
| 1 | Specification | `docs/v4_part2/sector_02_electroweak_host_spec.md` |
| 2 | Math scaffold | `docs/v4_part2/sector_02_electroweak_host_math.md` |
| 3 | Code modules (7) | `grut_solver/sectors/ew/` |
| 4 | Validation tests | `tests/sectors/ew/test_sector_02.py` |
| 5 | Notebook | `notebooks/sector_02_electroweak_host.py` |
| 6 | Paper summary | `docs/v4_part2/sector_02_electroweak_host_for_paper.md` |

## Closure condition

This sector is closed when:
1. U(1) gauge invariance of |z|^2 verified numerically
2. Lorentz force F = eE verified for multiple field strengths (< 2% error)
3. AB phase linearity in A verified
4. All 7 SM fermion charges reproduced exactly by Q = T^3 + Y/2
5. All 3 anomaly conditions = 0 exactly (to floating-point precision)
6. Q<H> = 0 exactly (photon massless)
7. rho = m_W^2 / (m_Z^2 cos^2 theta_W) = 1.000000
8. No new physics claimed beyond SM host recovery
