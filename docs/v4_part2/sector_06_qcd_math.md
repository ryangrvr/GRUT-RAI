# Sector 6 — QCD / Strong Force: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Status |
|--------|---------|--------|
| g_s | Strong coupling constant | Free parameter |
| T^a_c (a=1..8) | SU(3) generators (Gell-Mann lambda^a / 2) | Implemented |
| f^{abc} | SU(3) structure constants | Implemented |
| A_mu^a | Gluon fields (a=1..8) | Scaffold |
| F_{mu nu}^a | Color field strength tensor | Scaffold |
| q = (q_r, q_g, q_b)^T | Quark color triplet | Documented |
| D_mu | SU(3) covariant derivative | Implemented |

## 1. Constitutive SU(3) specialization

From Sector 2, the gauge principle promotes the target functional gradient to a covariant derivative. For SU(3) color:

    D_mu q = d_mu q + i g_s T^a_c A_mu^a q

where q is a color triplet (3-component vector in color space) and T^a_c = lambda^a / 2 are the eight generators of SU(3).

The gauge-invariant constitutive target functional:

    F[q, A] = integral { q^dag q + c_2 (D_mu q)^dag (D^mu q) } d^4x

This is the SU(3) specialization of the same structure that gives U(1) and SU(2) in Sectors 2 and 5.

## 2. SU(3) Lie algebra

Generators: T^a = lambda^a / 2 (a = 1, ..., 8) where lambda^a are the Gell-Mann matrices.

Commutation relation:

    [T^a, T^b] = i f^{abc} T^c

Structure constants f^{abc} are totally antisymmetric. Nonzero values:
- f^{123} = 1
- f^{147} = f^{165} = f^{246} = f^{257} = f^{345} = f^{376} = 1/2
- f^{458} = f^{678} = sqrt(3)/2

Trace normalization: Tr(T^a T^b) = delta^{ab} / 2

## 3. Color field strength

    F_{mu nu}^a = d_mu A_nu^a - d_nu A_mu^a + g_s f^{abc} A_mu^b A_nu^c

In matrix form:

    F_{mu nu} = d_mu A_nu - d_nu A_mu + i g_s [A_mu, A_nu]

The self-interaction term [A_mu, A_nu] generates gluon-gluon interactions. This is the key non-abelian feature inherited from Sector 2's SU(2) treatment.

Yang-Mills action:

    S_YM = -(1/2) integral Tr(F_{mu nu} F^{mu nu}) d^4x

## 4. Color representations

| Representation | Dimension | Objects | Status |
|----------------|-----------|---------|--------|
| Fundamental (3) | 3 | Quarks q_i | Documented |
| Anti-fundamental (3-bar) | 3 | Antiquarks | Documented |
| Adjoint (8) | 8 | Gluons | Documented |
| Singlet (1) | 1 | Color-neutral hadrons | Target |

Quadratic Casimir:
- Fundamental: C_F = (N^2 - 1) / (2N) = 4/3 for N=3
- Adjoint: C_A = N = 3

## 5. Candidate observables

### 5a. Wilson loop (proxy)

The Wilson loop measures the phase accumulated by a color charge transported around a closed path:

    W(C) = (1/N) Tr P exp(i g_s oint_C A_mu dx^mu)

- **Area law:** W ~ exp(-sigma * Area) implies confinement (sigma = string tension)
- **Perimeter law:** W ~ exp(-mu * Perimeter) implies deconfinement

**Status:** A toy-level 2D lattice implementation is scaffolded. This is exploratory, not full lattice QCD.

### 5b. Flux-tube / string tension proxy

Between a static quark-antiquark pair at separation r, confinement predicts:

    V(r) = -alpha_s / r + sigma * r

The linear-in-r term (string tension sigma) is the confinement signature.

**Status:** Not yet computed. This is a target observable for future work.

### 5c. Running coupling

One-loop beta function for SU(3) with N_f quark flavors:

    beta(g_s) = -(11 - 2N_f/3) g_s^3 / (16 pi^2)

For N_f <= 16: beta < 0 (asymptotic freedom). For N_f = 6 (SM): coefficient = -7.

**Status:** The analytical formula is documented. Whether GRUT's constitutive structure modifies the running is an open question.

## 6. Missing ingredients (explicit)

| Ingredient | Status | Note |
|------------|--------|------|
| Confinement | **Open** | Wilson loop scaffolded; area law not demonstrated |
| Asymptotic freedom | **Open** | Beta function documented; GRUT modification unknown |
| Hadron spectrum | **Open** | Requires nonperturbative dynamics |
| Chiral symmetry breaking | **Open** | Not addressed |
| Lattice formulation | **Not attempted** | Would require substantial new work |
| Glueball spectrum | **Open** | Requires pure-gauge nonperturbative computation |
