# Sector 2 — Electroweak / SM Host Structure: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Units / values |
|--------|---------|----------------|
| A_mu | U(1) gauge field (photon) | V s m^-1 |
| W_mu^a | SU(2) gauge fields (a=1,2,3) | — |
| B_mu | U(1)_Y gauge field | — |
| e | Electric charge coupling | 1.602e-19 C |
| g | SU(2) coupling | ~0.653 |
| g' | U(1)_Y coupling | ~0.350 |
| T^a | SU(2) generators = sigma^a/2 | — |
| Y | Hypercharge | integer or 1/3 multiples |
| Q | Electric charge operator = T^3 + Y/2 | — |
| theta_W | Weinberg angle | sin^2 ~ 0.231 |
| H | Higgs doublet (SU(2), Y=+1) | — |
| v | Higgs VEV | 246 GeV |
| mu^2, lambda | Higgs potential parameters | — |
| y_f | Yukawa couplings | species-dependent, FREE |

## 1. Constitutive route to gauge structure

From Sector 1, the target functional for a free particle is:

    F[z] = integral { |z|^2 + c_2 |nabla z|^2 }

F has a global U(1) symmetry: z -> e^{i theta} z.

**The gauge principle:** Promote global -> local symmetry. Introduce gauge field A_mu and covariant derivative:

    D_mu = d_mu + i e A_mu

The gauge-invariant target functional:

    F[z, A] = integral { |z|^2 + c_2 |D z|^2 }

This is the UNIQUE minimal modification preserving local U(1).

## 2. U(1) gauge coupling

The gauge-coupled Schrodinger equation (from Sector 1 + covariant derivative):

    i hbar d_t z = [(p - eA)^2 / (2m) + e Phi] z

Under local U(1) transformation z -> e^{i theta(x)} z, A_mu -> A_mu - (1/e) d_mu theta:
- D_mu z transforms covariantly: D_mu z -> e^{i theta} D_mu z
- |D_mu z|^2 is invariant
- Physical observables |z|^2 are gauge-invariant

## 3. Lorentz force and Aharonov-Bohm

**Lorentz force (Ehrenfest):** m d^2<x>/dt^2 = e<E> + e<v x B>

In 1D with uniform E, A=0: a = eE/m. Verified to 1.4%.

**AB phase:** A charged particle acquires phase delta_phi = e integral A.dl / hbar even where E = B = 0. This is the holonomy of the gauge connection.

## 4. SU(2) × U(1)_Y organization

Promote z to an SU(2) doublet Z = (z_1, z_2)^T. The covariant derivative:

    D_mu Z = d_mu Z + i g (sigma^a / 2) W_mu^a Z + i g' (Y/2) B_mu Z

SU(2) transformation: Z -> U Z, U = exp(i theta^a T^a).
- |Z|^2 invariant under SU(2)
- |D_mu Z|^2 invariant under SU(2) × U(1)_Y

Field strength tensor (non-abelian):

    F_mu_nu^a = d_mu W_nu^a - d_nu W_mu^a - g epsilon^{abc} W_mu^b W_nu^c

Self-interaction term [W_mu, W_nu] is the hallmark of non-abelian gauge theory.

## 5. Charge quantization

Electric charge operator: Q = T^3 + Y/2.

| Particle | SU(2) | T^3 | Y | Q = T^3 + Y/2 |
|----------|-------|-----|---|----------------|
| nu_eL | 2 | +1/2 | -1 | 0 |
| e_L | 2 | -1/2 | -1 | -1 |
| e_R | 1 | 0 | -2 | -1 |
| u_L | 2 | +1/2 | +1/3 | +2/3 |
| d_L | 2 | -1/2 | +1/3 | -1/3 |
| u_R | 1 | 0 | +4/3 | +2/3 |
| d_R | 1 | 0 | -2/3 | -1/3 |

All charges exact.

## 6. Anomaly cancellation

Three conditions, one complete generation:

**sum Y = 0** (gravitational):
(-1)×1 + (-1)×1 + (1/3)×3 + (1/3)×3 + (+2)×1 + (-4/3)×3 + (2/3)×3 = 0

**sum Y^3 = 0** (U(1)_Y^3):
(-1)^3 + (-1)^3 + 3(1/3)^3 + 3(1/3)^3 + 8 + 3(-4/3)^3 + 3(2/3)^3 = 0

**sum Y over doublets = 0** (SU(2)^2 × U(1)_Y):
2(-1) + 2(1/3)(3) = -2 + 2 = 0

All three exact zero. Requires N_c = 3 (color factor) and specific hypercharges.

## 7. Higgs mechanism

Higgs field H is an SU(2) doublet with Y = +1.

Target functional (Mexican hat):

    V(H) = -mu^2 |H|^2 + lambda |H|^4

Minimum at |H|^2 = v^2/2, v = mu / sqrt(lambda) = 246 GeV.

VEV: <H> = (0, v/sqrt(2))^T.

Symmetry breaking: SU(2) × U(1)_Y -> U(1)_EM.
- Q <H> = (T^3 + Y/2) <H> = 0: photon remains massless.
- T^1, T^2, (T^3 - Y/2) broken: 3 Goldstone bosons eaten by W+, W-, Z.
- 4 Higgs DOF = 3 Goldstones + 1 physical Higgs boson (m_H = sqrt(2) mu).

## 8. W/Z mass relations

From (D_mu <H>)^dag (D^mu <H>):

    m_W = g v / 2
    m_Z = sqrt(g^2 + g'^2) v / 2
    m_photon = 0

Weinberg mixing: sin^2(theta_W) = g'^2 / (g^2 + g'^2)

rho parameter: rho = m_W^2 / (m_Z^2 cos^2 theta_W) = 1 (tree level).

Fermion masses: M_f = y_f v / sqrt(2). Yukawa couplings y_f are FREE.

## 9. Exact claim boundary

This sector recovers the SM electroweak structure with the same parameter count. It does NOT:
- Derive the gauge group (assumed SU(2) × U(1)_Y)
- Derive the number of generations (3 is observed, not computed)
- Derive Yukawa couplings (free parameters, same as SM)
- Reduce the SM parameter count
- Predict any beyond-SM observable
