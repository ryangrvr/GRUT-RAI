# Sector 09 -- Dark Matter: Mathematical Scaffold

## 1. Structural Criteria for a GRUT Dark-Matter Candidate

Any dark-matter candidate arising from the GRUT constitutive framework must satisfy four simultaneous requirements:

| Criterion | Formal Requirement | Observational Constraint |
|---|---|---|
| **Stability** | Lifetime tau >> t_0 (age of universe) | tau > 10^{26} yr (indirect-detection bounds) |
| **Electrical neutrality** | Q_em = T_3 + Y/2 = 0 | No electromagnetic coupling at tree level |
| **Weak coupling** | Interaction cross-section sigma below direct-detection bounds | sigma < ~10^{-46} cm^2 (current WIMP-nucleon limits) |
| **Relic compatibility** | Thermal or non-thermal production yields correct abundance | Omega_DM h^2 = 0.1200 +/- 0.0012 (Planck 2018) |

All four conditions must hold simultaneously. Satisfying any three while violating the fourth excludes the candidate.

## 2. Candidate Types Within GRUT Architecture

Three classes of candidate are structurally available within the GRUT constitutive hierarchy:

### 2a. Hidden-Sector Response Field

A constitutive response field phi_D that couples to the Standard Model only through gravitational or portal-type interactions:

    L_portal = lambda_HP |H|^2 |phi_D|^2

where H is the SM Higgs doublet and lambda_HP is the portal coupling. Direct-detection cross-section scales as:

    sigma_SI ~ lambda_HP^2 f_N^2 m_N^2 / (4 pi m_h^4)

where f_N ~ 0.3 is the nucleon form factor and m_h = 125 GeV.

### 2b. Topological Soliton

A stable, localized field configuration stabilized by a conserved topological charge Q_top:

    Q_top = (1/2pi) integral d^2x epsilon^{ij} partial_i n_hat . partial_j n_hat

Topological stability guarantees tau = infinity (no perturbative decay channel).

### 2c. Weakly-Coupled Constitutive Excitation

A massive excitation of the constitutive field spectrum with mass m_chi and annihilation cross-section:

    <sigma v> ~ g_chi^4 / (16 pi m_chi^2)

where g_chi is the constitutive coupling strength.

## 3. Stability Requirement

The candidate must satisfy:

    tau_DM >> t_0 ~ 4.35 x 10^{17} s

This requires all kinematically allowed decay channels to be suppressed. For a particle of mass m_chi, partial widths must satisfy:

    Gamma_total = sum_f Gamma(chi -> f) < 1/tau_min ~ 10^{-26} yr^{-1}

Suppression mechanisms available in GRUT:
- Discrete symmetry (e.g., Z_2 parity on the constitutive sector)
- Topological protection (winding number conservation)
- Kinematic closure (no lighter states carrying the same quantum numbers)

**STATUS:** No specific symmetry has been identified in the GRUT constitutive action that guarantees DM stability. This is OPEN.

## 4. Direct-Detection Coupling Bound

The spin-independent WIMP-nucleon cross-section is bounded by:

    sigma_SI < ~10^{-46} cm^2   (for m_chi ~ 30 GeV, LZ/XENONnT)

For a contact interaction with mediator mass M and coupling g:

    sigma_SI ~ g^4 m_N^2 / (pi M^4)

Setting sigma_SI < 10^{-46} cm^2 with M ~ 100 GeV requires g < ~10^{-3}.

## 5. Relic Abundance

The observed dark-matter density:

    Omega_DM h^2 = 0.1200 +/- 0.0012

For a thermal relic with s-wave annihilation, the standard freezeout calculation gives:

    Omega_chi h^2 ~ (3 x 10^{-26} cm^3/s) / <sigma v>

so the canonical thermal cross-section is:

    <sigma v>_thermal ~ 3 x 10^{-26} cm^3/s

The Boltzmann equation governing freezeout:

    dY/dx = - (s <sigma v>) / (H x) (Y^2 - Y_eq^2)

where Y = n/s, x = m_chi/T, s is entropy density, H is Hubble rate.

**STATUS:** No freezeout calculation has been performed for any GRUT candidate. The abundance is not predicted.

## 6. Summary of Missing Elements

| Element | Status |
|---|---|
| Concrete DM candidate from GRUT spectrum | **MISSING** |
| Stability mechanism (symmetry identification) | **MISSING** |
| Relic abundance calculation | **MISSING** |
| Direct-detection cross-section prediction | **MISSING** |
| Indirect-detection signal prediction | **MISSING** |
| Consistency with collider bounds | **MISSING** |

This sector is a scaffold: it specifies what a GRUT dark-matter theory must deliver, but does not yet deliver it.
