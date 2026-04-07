# GRUT III Book A — Stage A3: Dephasing/Bath Closure Decision

---

## Question

Does gravity alone supply both the USL dephasing (Sector 3) AND the dissipation/noise (Sectors 1-2), or is a separate environmental bath required?

This is the sharpest open structural question in the GRUT-II inheritance. It determines whether the minimal variable set is truly (g, Phi) or whether an additional environmental sector must be added.

---

## Setup: What is at stake

The CTP action has three sectors:

| Sector | Physical content | What determines it |
|:------:|-----------------|-------------------|
| 1 | Dissipation: rate 1/tau | Bath spectral density J(omega) at low frequency |
| 2 | Noise: coefficient D = k_B T tau | Bath temperature T and spectral density |
| 3 | Dephasing: rate Gm^2/(hbar l) | Gravitational self-energy (tree-level) |

Sector 3 is unambiguously gravitational: it comes from integrating out the Newtonian potential at tree level. The question is about Sectors 1-2: what is the bath?

---

## Branch 1: Gravity-Only

### Assumptions

| # | Assumption | Tag |
|---|-----------|:---:|
| B1-A1 | The gravitational field g_a, integrated out at one-loop order, provides both the dissipation kernel eta and the noise kernel D. | **ASSUMED** |
| B1-A2 | The spectral density of gravitational fluctuations is Ohmic (or effectively Ohmic) at the frequencies relevant to the constitutive field. | **ASSUMED** |
| B1-A3 | The effective temperature in the gravitational FDT is a well-defined quantity (Hawking temperature near horizons, zero-point fluctuations in flat space, or some coarse-grained gravitational temperature). | **ASSUMED** |
| B1-A4 | No non-gravitational environmental sector is needed. The variable set (g_r, g_a, Phi_r, Phi_a) is complete. | **ASSUMED** (= claim S4 from Book A) |

### Strengths

1. **Minimality.** Only two fields (g, Phi) are needed. No additional content. The theory is maximally parsimonious.

2. **Structural unity.** Both the dephasing (tree-level) and the dissipation/noise (one-loop) come from the same gravitational sector. The constitutive relaxation time tau would be determined by the gravitational spectral density, not by an external parameter.

3. **Predictivity.** If tau is determined by gravity, the theory has one fewer free parameter. The entire constitutive + quantum sector is controlled by (G, hbar, m, geometry).

4. **Naturalness of the DP-type scaling.** The USL scaling Gm^2/(hbar l) is manifestly gravitational. If the bath is also gravitational, the entire decoherence-dissipation structure is a consequence of gravity's open-system dynamics.

### Failure modes

| # | Failure mode | Consequence |
|---|-------------|-------------|
| B1-F1 | One-loop gravitational D is too small. The gravitational vacuum fluctuations in flat space produce momentum diffusion D_grav ~ G^2 m^2 hbar omega^3 / c^5 (from graviton emission/absorption). For mesoscopic masses, this is catastrophically small (~10^-80 in SI units). | tau_grav ~ 1/D_grav would be ~10^80 s. The constitutive relaxation time would be cosmologically long — not the ~seconds-to-years range needed for physical relevance. **The gravity-only bath does not produce a physically relevant tau in flat space.** |
| B1-F2 | The Ohmic assumption (B1-A2) fails. Gravitational fluctuations in flat space have a spectral density ~ omega^3 (graviton density of states), which is super-Ohmic, not Ohmic. The Markovian/overdamped limit may not apply. | The constitutive law may not emerge in its simple first-order form from a gravitational bath. Memory effects dominate. |
| B1-F3 | The effective gravitational temperature (B1-A3) is zero in flat space (no thermal gravitons). | D = k_B T tau with T = 0 gives D = 0 (no noise). The FDT partner of any gravitational dissipation vanishes. The noise sector is empty unless near a horizon (T = T_H). |

### Regime limits

- **Near a BH horizon:** T = T_Hawking ≠ 0. The gravitational bath is thermal. Sector 2 noise is nonzero. tau could be finite. This is the ONE regime where gravity-only might work.
- **In flat space:** T_grav = 0 (or Unruh temperature, which is zero for inertial observers). D = 0. tau → infinity. Gravity-only FAILS to produce constitutive relaxation in flat space.
- **In cosmological settings:** T_grav ~ T_deSitter = H/(2 pi k_B). Very small. tau ~ 10^{60+} s.

### Summary for Branch 1

**Gravity-only works near horizons (finite T_H provides a thermal bath) but FAILS in flat space and weak-field regimes where T_grav → 0. The gravitational spectral density is super-Ohmic (omega^3), not Ohmic, complicating the Markovian limit.**

---

## Branch 2: Mixed Bath

### Assumptions

| # | Assumption | Tag |
|---|-----------|:---:|
| B2-A1 | Sector 3 (USL dephasing) is gravitational (tree-level Newtonian self-energy). | **DERIVED** (inherited from Iota-Prime) |
| B2-A2 | Sectors 1-2 (dissipation/noise) are sourced by a non-gravitational environmental bath: matter fields, thermal radiation, gas collisions, or some combination. | **ASSUMED** |
| B2-A3 | The bath spectral density J(omega) is Ohmic at the relevant frequencies. | **ASSUMED** (standard for matter/thermal baths) |
| B2-A4 | The temperature T is the environmental temperature (e.g., T = 4 K for the cryogenic nanoparticle experiment, or T ~ 10^7 K for stellar interiors). | **ASSUMED** |
| B2-A5 | tau is a parameter of the effective theory, determined by the matter-environment coupling, not by gravity. | **ASSUMED** |
| B2-A6 | The minimal variable set is (g_r, g_a, Phi_r, Phi_a) PLUS an environmental sector (traced out, leaving D and tau as effective parameters). | **ASSUMED** |

### Strengths

1. **Physical plausibility.** In every concrete GRUT calculation (Delta-Prime environmental budget, Mu-Prime hardware audit), the dominant decoherence/noise sources are environmental (gas collisions, blackbody radiation, magnetic noise). The gravitational noise is always negligible by many orders of magnitude. The mixed-bath picture matches the actual physics.

2. **Ohmic bath is natural.** Matter and thermal baths typically have Ohmic or near-Ohmic spectral densities at low frequencies. The Markovian/overdamped limit is standard and well-tested for these baths.

3. **Finite tau at all scales.** Environmental interactions produce finite dissipation rates at all relevant scales, not just near horizons. The constitutive relaxation can operate anywhere matter is present.

4. **Separation of scales.** The USL (gravitational, tree-level, G-dependent) and the constitutive relaxation (environmental, matter-dependent, tau as effective parameter) live at different scales and have different dependencies. This cleanly explains why the USL scales as Gm^2/(hbar l) while tau depends on local conditions (temperature, density, coupling).

5. **Consistency with GRUT-I.** The Level-1 formula 1/tau_local = 1/tau_0 + 1/t_dyn mixes a background rate (1/tau_0, possibly gravitational or cosmological) with a dynamical rate (1/t_dyn ~ sqrt(G rho)), which is a local matter density, not a pure gravitational vacuum effect. This is mixed-bath structure.

### Failure modes

| # | Failure mode | Consequence |
|---|-------------|-------------|
| B2-F1 | tau remains a free parameter. The theory cannot predict the constitutive relaxation time; it can only constrain it from observations. | Reduced predictivity compared to gravity-only (if gravity-only worked). |
| B2-F2 | The bath identity is not unique. Different environments give different tau, D, and even different spectral densities. The constitutive law is environment-dependent. | The theory is an EFT, not a fundamental theory. The constitutive law is universal in form but not in parameters. |
| B2-F3 | The separation of USL (gravitational) and tau (environmental) could break at strong coupling or near horizons, where gravitational and matter effects mix. | The clean two-source structure (gravity for Sector 3, environment for Sectors 1-2) is a weak-field/low-coupling approximation. |

### Regime limits

- **Flat space / weak field:** Works. Environmental bath provides finite tau and D. USL from gravity at tree level. Clean separation.
- **Near horizons:** Both gravitational and environmental baths contribute. The gravitational bath (Hawking temperature) adds to the environmental bath. The separation of sources softens but does not break.
- **Strong curvature:** The distinction between "gravitational" and "environmental" may blur (the environment IS gravitational near a BH). Branch 2 does not fail but loses its clean separation.

### Summary for Branch 2

**Mixed bath works at all scales. tau is a free parameter. The separation of gravitational dephasing (Sector 3) from environmental dissipation/noise (Sectors 1-2) is clean in weak field and softens near horizons. The theory is an EFT with environment-dependent parameters.**

---

## Side-by-Side Branch Table

| Property | Branch 1: Gravity-Only | Branch 2: Mixed Bath |
|----------|:----------------------:|:--------------------:|
| **Variable set** | (g_r, g_a, Phi_r, Phi_a) only | (g_r, g_a, Phi_r, Phi_a) + traced-out environment |
| **Sector 3 (USL)** | Gravitational tree-level | Gravitational tree-level |
| **Sector 1-2 source** | Gravitational one-loop | Environmental (matter/thermal) |
| **tau determined by** | Gravitational spectral density J_grav(omega) | Environmental coupling (free parameter) |
| **D determined by** | FDT with T_grav | FDT with T_env |
| **T in flat space** | 0 (no thermal gravitons) | T_env (finite, measurable) |
| **Ohmic spectral density?** | No (J_grav ~ omega^3, super-Ohmic) | Yes (standard for matter baths) |
| **Markovian limit?** | Questionable (super-Ohmic) | Standard (Ohmic) |
| **tau in flat space** | → infinity (T = 0, D = 0) | Finite (environment provides) |
| **tau near horizon** | Finite (T = T_H, D ≠ 0) | Finite (T_env + T_H) |
| **Free parameters** | Fewer (tau derived from G, m, geometry) | More (tau is EFT parameter) |
| **Flat-space viability** | **FAILS** (no dissipation without thermal gravitons) | **WORKS** |
| **Consistency with experimental roadmap** | Inconsistent (gas/thermal noise dominates, not gravity) | **Consistent** |
| **Consistency with GRUT-I Level-1** | Partial (1/t_dyn involves matter density, not pure gravity) | **Consistent** |
| **Predictivity** | Higher if it worked; but it doesn't in flat space | Lower but physically viable |

---

## Discriminators

What would empirically or theoretically separate the branches?

| # | Discriminator | What it tests | How it could be measured/computed | Status |
|---|--------------|---------------|----------------------------------|:------:|
| **D1** | Compute one-loop gravitational D_grav in flat space. | If D_grav produces a physically relevant tau (tau < age of universe), Branch 1 is viable. If D_grav → 0, Branch 1 fails in flat space. | One-loop graviton self-energy of Phi on flat CTP contour. | **NOT COMPUTED** |
| **D2** | Measure tau experimentally. | If tau matches the gravitational prediction (Branch 1) or the environmental prediction (Branch 2), one branch is selected. | Requires detecting the constitutive relaxation of Phi, which has not been observed. | **NOT MEASURABLE** (Phi not directly observed) |
| **D3** | Check spectral density of gravitational fluctuations. | If J_grav(omega) is Ohmic at low omega, Branch 1's Markovian limit is viable. If super-Ohmic (omega^3), it fails. | Standard QFT calculation for graviton spectral density. Known: J_grav ~ omega^3 in flat space (graviton density of states). | **COMPUTED (in literature): super-Ohmic.** Branch 1 Markovian limit fails. |
| **D4** | Check whether D = 0 is consistent with CTP positivity. | CTP requires Im S_eff ≥ 0 (U3). If D = 0, then Im S_eff = 0, which satisfies U3 but gives a delta-function density matrix (no fluctuations, pure state). Is this self-consistent for a dissipative theory? | Structural: a dissipative system with no noise violates the second law (entropy decreases). | **RESOLVED: D = 0 is inconsistent with dissipation.** If there is dissipation (tau finite), there MUST be noise (D > 0), or the second law is violated. |

### Discriminator D4 is decisive

**If the constitutive field dissipates (tau is finite), the second law requires a noise source (D > 0).** In flat space, the gravitational bath provides D_grav → 0 (zero temperature, super-Ohmic). Therefore:

- If tau is finite in flat space, the noise CANNOT come from gravity alone. An environmental bath is required.
- Branch 1 (gravity-only) is self-consistent ONLY if tau → infinity in flat space (no dissipation, no noise needed).
- But GRUT-I postulates tau as a finite, universal constitutive parameter. This is incompatible with Branch 1 in flat space.

---

## Provisional Verdict

### Status: **BOUNDED-OPEN, with strong directional evidence favoring Branch 2.**

### Reasoning

1. **Branch 1 (gravity-only) fails in flat space** by three independent arguments:
   - D_grav → 0 (no thermal gravitons, T = 0) → no noise → violates second law if tau is finite (D4)
   - J_grav ~ omega^3 (super-Ohmic, not Ohmic) → Markovian limit fails (D3)
   - tau_grav ~ 1/D_grav → infinity → no constitutive relaxation (B1-F1)

2. **Branch 1 survives near horizons** (T = T_H ≠ 0, providing a thermal gravitational bath), but this is a restricted regime, not the general case.

3. **Branch 2 (mixed bath) works at all scales.** It is consistent with:
   - All experimental roadmap calculations (gas/thermal noise dominates)
   - The GRUT-I Level-1 formula (tau depends on local matter dynamics)
   - The second law (environmental bath provides D > 0 for finite tau)
   - Standard Ohmic/Markovian physics

4. **Neither branch can be declared superior without D1** (the one-loop gravitational D calculation), because:
   - Branch 2 is strongly favored by physical arguments, but the gravity-only loop computation has not been done within GRUT
   - A conceivable escape for Branch 1: if the constitutive field has a non-standard coupling to gravity that produces Ohmic dissipation (e.g., through X-dependent interactions that mimic an Ohmic bath), the simple graviton-density-of-states argument may not apply. This is speculative but not excluded.

### Minimum missing discriminator to resolve

**D1: Compute the one-loop gravitational contribution to D (and hence tau) in flat space within the GRUT CTP action.**

If D_grav is negligible compared to environmental D at relevant scales: **Branch 2 is mandatory.** The theory is an EFT with an environmental bath. S4 ("no extra bath needed") is RETRACTED.

If D_grav is somehow non-negligible (requiring non-standard Phi-g coupling): **Branch 1 remains alive** but needs the explicit mechanism identified.

---

## Structural Consequence for the Backbone

### If Branch 2 is confirmed (most likely)

The minimal backbone {L1, L2, L3, L4, L6} acquires an additional structural element:

**L11: Environmental bath sector** — An implicit environmental sector, traced out, that provides the spectral density J(omega) and temperature T determining D and tau. The variables (g_r, g_a, Phi_r, Phi_a) remain the explicit DOF; the bath is encoded in the effective parameters (tau, D, T).

The theory structure becomes:

```
CTP backbone (explicit):  (g_r, g_a, Phi_r, Phi_a)
Environmental bath (implicit, traced out):  provides tau, D, T
Gravitational dephasing (explicit, tree-level):  provides Lambda_USL
```

Claim S4 ("no additional bath beyond g, Phi needed in principle") is downgraded:
- Old status: INFERRED
- New status: **RETRACTED in flat space; OPEN near horizons**

### If Branch 1 survives (unlikely in flat space)

The backbone is unchanged, but the Phi-g coupling must be non-standard (not minimal coupling) to produce an Ohmic spectral density from gravitational fluctuations alone. This would be a major theoretical claim requiring explicit construction.

---

*GRUT III Book A Stage A3 complete. Verdict: BOUNDED-OPEN, Branch 2 (mixed bath) strongly favored. Branch 1 (gravity-only) fails in flat space by three independent arguments: D_grav → 0, super-Ohmic spectral density, second-law violation. Branch 1 survives only near horizons. Branch 2 is consistent with all experimental and theoretical evidence. Minimum missing discriminator: one-loop gravitational D computation (D1). If D_grav negligible: S4 retracted, environmental bath mandatory, tau is an EFT parameter. The backbone acquires an implicit environmental sector (L11).*
