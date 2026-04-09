# Sector 10 -- Baryogenesis: Mathematical Scaffold

## 1. Sakharov Conditions

Any mechanism producing the observed baryon asymmetry of the universe must satisfy the three Sakharov conditions simultaneously:

| Condition | Physical Requirement | GRUT Status |
|---|---|---|
| **(1) Baryon-number violation** | Processes exist with Delta B != 0 | NOT IDENTIFIED in constitutive action |
| **(2) C and CP violation** | Charge conjugation and combined CP symmetry are both broken | NOT IDENTIFIED in constitutive action |
| **(3) Departure from thermal equilibrium** | Interactions occur out of equilibrium | STRUCTURALLY PRESENT via CTP formalism (A0) |

All three conditions are necessary. Satisfying only condition (3) -- which GRUT does provide -- is insufficient.

## 2. CTP Relevance: Nonequilibrium Structure

The Closed-Time-Path (CTP) formalism (GRUT Axiom A0) is inherently a nonequilibrium framework. The CTP generating functional:

    Z_CTP = integral D[phi_+] D[phi_-] exp{i S[phi_+] - i S[phi_-]}

with the doubling of field degrees of freedom (phi_+, phi_-) on the forward and backward time branches encodes:

- Real-time evolution (not Euclidean)
- Dissipation and decoherence
- Memory effects via non-Markovian kernels
- Departure from thermal equilibrium as a natural feature, not an add-on

This means Sakharov condition (3) is **built into the formalism**. The CTP structure does not require a phase transition or out-of-equilibrium decay to be grafted on -- it naturally describes systems away from equilibrium.

However: the CTP structure alone does not generate baryon-number violation or CP violation. Those must come from the field content and couplings.

## 3. Toy Asymmetry Evolution

A minimal model for baryon asymmetry generation takes the form:

    dN_B/dt = epsilon * Gamma * f(T)

where:
- **epsilon** = CP asymmetry parameter (dimensionless, |epsilon| << 1)
- **Gamma** = rate of the B-violating interaction [s^{-1}]
- **f(T)** = departure-from-equilibrium factor (dimensionless)

The departure-from-equilibrium factor:

    f(T) = 1 - n_eq(T)/n_actual(T)

vanishes in thermal equilibrium (f -> 0) and approaches unity when the interaction freezes out (f -> 1).

The integrated baryon asymmetry:

    N_B(t_final) = epsilon * integral_0^{t_final} dt Gamma(t) f(T(t))

In a radiation-dominated universe with T ~ t^{-1/2}:

    N_B ~ epsilon * (Gamma / H)|_{T_D} * f(T_D)

where T_D is the temperature at which the B-violating interaction decouples (Gamma ~ H).

## 4. Observational Target

The baryon-to-photon ratio:

    eta_B = (n_B - n_Bbar) / n_gamma = (6.143 +/- 0.019) x 10^{-10}

(Planck 2018, from CMB + BBN concordance)

This is equivalently expressed as:

    Omega_B h^2 = 0.02242 +/- 0.00014

Any baryogenesis mechanism must produce eta_B to this precision, starting from a symmetric initial state (eta_B = 0 at T >> T_D).

The smallness of eta_B (~10^{-10}) means the CP asymmetry parameter epsilon need not be large, provided the departure from equilibrium is sufficient.

## 5. Standard Mechanisms (for Reference)

| Mechanism | B violation | CP source | Nonequilibrium |
|---|---|---|---|
| GUT baryogenesis | Heavy boson decay (Delta B != 0) | Complex Yukawa couplings | Out-of-equilibrium decay |
| Electroweak baryogenesis | Sphaleron transitions | CKM + BSM CP phases | First-order EW phase transition |
| Leptogenesis | Lepton-number violation (heavy nu_R decay) + sphalerons | Complex neutrino Yukawas | Out-of-equilibrium decay |
| Affleck-Dine | Flat-direction condensate carries B | A-terms in SUSY potential | Coherent field oscillation |

GRUT does not currently implement any of these mechanisms. The CTP structure is compatible with all of them but does not select one.

## 6. Summary of Missing Elements

| Element | Status |
|---|---|
| Baryon-number-violating operator in GRUT action | **MISSING** |
| CP-violating phase in constitutive couplings | **MISSING** |
| Concrete freezeout/decoupling calculation | **MISSING** |
| Sphaleron dynamics within GRUT framework | **MISSING** |
| Prediction of eta_B from first principles | **MISSING** |
| Connection to leptogenesis via Sector 8 (neutrinos) | **OPEN** |

The CTP formalism provides the nonequilibrium backbone (Sakharov condition 3). The remaining two Sakharov conditions require new physics content that has not been specified.
