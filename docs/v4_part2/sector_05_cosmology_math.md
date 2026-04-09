# Sector 5 — Cosmology: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Status |
|--------|---------|--------|
| H(z) | Hubble parameter at redshift z | Computed |
| E(z) | H(z)/H_0 (normalized) | Computed |
| Omega_m(z) | Matter density parameter | Computed |
| D(z) | Linear growth factor | Computed |
| f(z) | Growth rate d(ln D)/d(ln a) | Computed |
| fsigma8(z) | Growth observable | Computed |
| rho_eq | Constitutive equilibrium density | Derived (< 0: PROBLEM) |
| lambda_screen | Screening length | FREE PARAMETER |
| kappa, gamma | Lensing convergence, shear | Computed |

## 1. Homogeneous background (FRW embedding)

The GRUT constitutive field couples to the Friedmann equation through a modified Hubble rate. The operator stack (operators.py) evolves:

    H^2(z) = H_0^2 [Omega_m (1+z)^3 + Omega_Lambda + memory_correction(z)]

The memory correction comes from the constitutive field's relaxation dynamics on the expanding background. The canonical parameters (C_rho, C_k, w_EOS, sigma8_0) are defined in the JSON schema.

**Status:** Implemented and running. Produces E(z), H(z), Omega_m(z).

## 2. Growth factor and fsigma8

Linear perturbation growth:

    D''(a) + [3/a + H'(a)/H(a)] D'(a) - (3/2) Omega_m(a) / a^2 D(a) = 0

Growth rate: f = d(ln D)/d(ln a)
Observable: fsigma8(z) = f(z) sigma8(z)

**Status:** Implemented in operators.py op_growth(). Compared against LCDM reference.

## 3. LCDM reference baseline

    E_LCDM(z) = sqrt(Omega_m (1+z)^3 + Omega_Lambda + Omega_r (1+z)^4 + Omega_k (1+z)^2)

**Status:** Implemented in lcdm_reference.py. Used as comparison baseline.

## 4. Dark-energy analysis (FAILED)

The constitutive equilibrium density:

    rho_eq = -M^2 / (2 tau^2 r^4)

**PROBLEM:** rho_eq < 0. A negative energy density is ANTI-accelerating (w = -1 with wrong sign). The dark-energy replacement route (XII Alpha) is PERMANENTLY FAILED.

**Nonclaim:** GRUT does not provide a dark-energy solution.

## 5. Cosmological bounce (partial)

The constitutive field's memory kernel can soften the FRW singularity but does NOT produce a true bounce:

    Classification: singularity_softened_but_not_bounced

**Status:** Computed in cosmological_bounce_extension.py. Valid analysis with honest conclusion.

## 6. Screening length (naturalness problem)

The scalar field has a screening length lambda that determines where GRUT effects become relevant:

    lambda_screen = free parameter

No natural mechanism within GRUT sets lambda to a cosmological scale. This is documented as a NATURALNESS PROBLEM in the viability audit.

## 7. Lensing and rotation curves

**Lensing:** Full FFT-based calculator for convergence kappa, shear gamma_1/gamma_2, and magnification. Computed from matter distributions.

**Rotation curves:** Baryonic + GRUT prediction compared against galaxy observations.

**Status:** Both are computational tools. They do not constitute cosmological closure — they provide comparison infrastructure.

## 8. What is missing (explicit)

| Ingredient | Status | Note |
|------------|--------|------|
| Dark-energy mechanism | **PERMANENTLY FAILED** | rho_eq < 0 |
| Late-universe modification | **Failed** | No viable route |
| Precision CMB fit | **Not attempted** | No perturbation spectrum |
| BAO comparison | **Not attempted** | Infrastructure exists but not fitted |
| Natural screening length | **Open** | Naturalness problem documented |
| Full observational fit | **Not achieved** | Residual metrics exist but not a fit |
| Early-universe regulator | **Conditional** | Not validated |
