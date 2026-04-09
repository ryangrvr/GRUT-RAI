# Sector 6 — QCD / Strong Force: Specification

## Sector name
QCD / Strong Force

## Status
**Open, with computational entry point**

This is the first genuinely open sector with new implementable structure. Sector 2 established non-abelian gauge machinery for SU(2) x U(1)_Y. Sector 6 specializes that machinery to SU(3) color, providing the algebraic and gauge-covariant entry point for QCD within the GRUT framework. No QCD physics closure (confinement, asymptotic freedom, hadron spectrum) is claimed.

## Claim boundary

**What is claimed:**
- The constitutive target functional admits SU(3) specialization via D_mu = d_mu + ig_s T^a_c A_mu^a
- The SU(3) Lie algebra (Gell-Mann matrices, structure constants) is implemented and validated
- Gauge covariance of the SU(3) covariant derivative is verified
- Color charge assignments for fundamental and adjoint representations are documented
- First exploratory observables (Wilson loop proxy, confinement probe) are scaffolded

**What is NOT claimed:**
- No confinement proof or demonstration
- No asymptotic freedom closure
- No hadron spectrum computation
- No chiral symmetry breaking
- No lattice QCD equivalence
- No claim that GRUT adds anything to QCD beyond hosting it

## Dependencies

- **Sector 2:** Non-abelian gauge host (SU(2) machinery, covariant derivatives, Lie algebra)
- **A1-A2:** Constitutive law and complex relaxation
- **Standard QCD:** The physics target (external, not derived)

## Deliverables

| # | Deliverable | Path |
|---|-------------|------|
| 1 | Specification | this file |
| 2 | Math scaffold | `docs/v4_part2/sector_06_qcd_math.md` |
| 3 | Code modules | `grut_solver/sectors/qcd/` |
| 4 | Validation tests | `tests/sectors/qcd/test_sector_06.py` |
| 5 | Notebook | `notebooks/sector_06_qcd.py` |
| 6 | Paper summary | `docs/v4_part2/sector_06_qcd_for_paper.md` |

## Closure condition

This sector is NOT closed. Closure would require:
1. Demonstration of confinement (area-law Wilson loop or equivalent)
2. Recovery of asymptotic freedom (running coupling beta function)
3. Hadron spectrum computation (at least pion, proton masses)
4. Chiral symmetry breaking

The entry point — SU(3) algebra, covariance, representations — is the foundation on which a QCD specialist could build these tests.
