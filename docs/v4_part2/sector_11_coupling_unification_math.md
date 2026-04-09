# Sector 11 -- Coupling Unification: Mathematical Scaffold

## 1. One-Loop Renormalization Group Running

The Standard Model gauge couplings run with energy scale mu according to the one-loop RGE:

    1/alpha_i(mu) = 1/alpha_i(M_Z) - b_i/(2 pi) ln(mu/M_Z)

where i = 1, 2, 3 labels the U(1)_Y, SU(2)_L, SU(3)_c gauge groups respectively.

### One-loop beta-function coefficients (SM):

    b_1 = 41/10
    b_2 = -19/6
    b_3 = -7

These are fixed by the SM particle content: three generations of fermions, one Higgs doublet.

### Low-energy boundary values at M_Z = 91.1876 GeV:

    alpha_1(M_Z) ~ 1/59.0    (GUT-normalized: alpha_1 = (5/3) alpha_Y)
    alpha_2(M_Z) ~ 1/29.6
    alpha_3(M_Z) ~ 1/8.4

Equivalently:

    1/alpha_1(M_Z) ~ 59.0
    1/alpha_2(M_Z) ~ 29.6
    1/alpha_3(M_Z) ~ 8.4

## 2. SM Couplings Do NOT Unify

Evolving the three couplings to high energies using the one-loop SM beta functions:

At mu ~ 10^{13} GeV:
    1/alpha_1 ~ 42.5
    1/alpha_2 ~ 32.1
    1/alpha_3 ~ 17.0

At mu ~ 10^{15} GeV:
    1/alpha_1 ~ 39.5
    1/alpha_2 ~ 31.0
    1/alpha_3 ~ 13.5

At mu ~ 10^{16} GeV:
    1/alpha_1 ~ 38.5
    1/alpha_2 ~ 30.5
    1/alpha_3 ~ 12.0

The three inverse couplings do not meet at a single point. The closest approach occurs near mu ~ 10^{15} GeV, where the mismatch is approximately:

    Delta(10^{15} GeV) = max_i(1/alpha_i) - min_i(1/alpha_i) ~ 39.5 - 13.5 = 26.0

The pairs (alpha_1, alpha_2) and (alpha_2, alpha_3) cross at different scales, separated by roughly one order of magnitude in energy. This is the well-known failure of SM gauge coupling unification.

## 3. Convergence Metric

Define the convergence metric at scale mu:

    Delta(mu) = max_{i in {1,2,3}} [1/alpha_i(mu)] - min_{i in {1,2,3}} [1/alpha_i(mu)]

Perfect unification requires Delta(mu_GUT) = 0 at some scale mu_GUT.

In the SM:
    Delta_min ~ 3-5% relative mismatch (depending on two-loop corrections and threshold effects)

This non-zero Delta_min is the quantitative statement that SM couplings fail to unify.

For comparison, in the MSSM with superpartner masses near ~1 TeV:
    b_1^{MSSM} = 33/5, b_2^{MSSM} = 1, b_3^{MSSM} = -3

    Delta_min^{MSSM} ~ 0 at mu_GUT ~ 2 x 10^{16} GeV

(This is the classic MSSM unification success, shown for reference only -- GRUT is not supersymmetric.)

## 4. What GRUT Would Need to Provide

For GRUT to achieve gauge coupling unification, the constitutive structure would need to modify the beta-function coefficients. Specifically:

    b_i -> b_i + Delta b_i^{GRUT}

where the corrections Delta b_i^{GRUT} arise from new charged states in the GRUT constitutive spectrum.

Each new field with gauge quantum numbers contributes:

    Delta b_i = T(R_i) * d(R_other) * multiplicity / normalization

where T(R_i) is the Dynkin index of the representation under group i.

**OPEN QUESTION:** Does the GRUT constitutive field content include any states charged under the SM gauge groups beyond the known SM particles? If yes, their quantum numbers determine Delta b_i and potentially rescue unification. If no, GRUT adds nothing to the running and the SM non-unification persists.

## 5. Threshold Corrections

Even with modified running, precision unification requires threshold corrections at the unification scale:

    1/alpha_i(mu_GUT) = 1/alpha_GUT + lambda_i/(12 pi) sum_heavy ln(M_heavy/mu_GUT)

where the sum runs over heavy states near mu_GUT and lambda_i are group-theoretic factors.

These corrections are model-dependent and can shift the apparent unification scale by up to an order of magnitude.

**STATUS:** No heavy spectrum is predicted by GRUT, so no threshold corrections can be computed.

## 6. Summary of Missing Elements

| Element | Status |
|---|---|
| GRUT-charged states modifying beta functions | **OPEN QUESTION** |
| Modified beta-function coefficients Delta b_i | **MISSING** |
| Unification scale mu_GUT | **MISSING** |
| Unified coupling alpha_GUT | **MISSING** |
| Threshold corrections from GRUT spectrum | **MISSING** |
| Predictive relations among low-energy couplings | **MISSING** |
| Proton-decay predictions (if B violation present) | **MISSING** |

GRUT adds nothing to gauge coupling running unless the constitutive structure contains states charged under the SM gauge groups. Whether it does is an open question that the current formulation does not answer.
