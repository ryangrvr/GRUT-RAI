# GRUT III Book A — Stage A4: Domain-of-Validity Finalization

---

## 1. Regime Matrix

Six axes. Three zones per axis. Every claim in the backbone is bounded by this matrix.

### Zone definitions

- **CONTROLLED:** The backbone has been verified in this regime by explicit calculation, structural argument, or standard-physics inheritance. Claims carry full declared confidence.
- **CAUTION:** The backbone is plausibly valid but has not been verified. Claims carry reduced confidence and must be flagged as extrapolations.
- **UNSAFE / EXCLUDED:** The backbone is known to fail, is untested with reason to suspect failure, or requires structural extensions not yet constructed. Claims are FORBIDDEN.

---

### Axis 1: Scale (spatial separation l relative to body size R)

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED | l > 2R | **Verified** | Point-mass USL: Lambda = Gm^2/(hbar l). Kappa-Prime. |
| CONTROLLED | l < 2R | **Verified** | Extended-body Diosi integral. Kappa-Prime. Suppression ~ (l/R)^3. |
| UNSAFE | l < R_body_min (UV cutoff, l approaching atomic scale) | **Excluded** | Diosi integral's 1/|x-x'| kernel requires regularization. Physical cutoff is body radius R. Sub-atomic separations are outside EFT scope. |

### Axis 2: Curvature (R_curvature / R_Schwarzschild or equivalently Phi_Newton / c^2)

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED | Phi_N/c^2 < 10^-6 (weak field: solar system, mesoscopic experiments) | **Verified** | Newtonian limit. All A1-A3 checks pass. |
| CAUTION | 10^-6 < Phi_N/c^2 < 0.1 (moderate: neutron star surfaces, white dwarfs) | **Unverified** | X(g_r) unspecified (A1-L6). Post-Newtonian corrections to USL not computed. Backreaction (A2-M1) potentially relevant. |
| UNSAFE | Phi_N/c^2 > 0.1 (strong: near BH horizons, mergers) | **Excluded** | Newtonian USL invalid. Covariant Diosi integral not constructed. X(g_r) critical and unknown. Backreaction mandatory. Overdamped limit untested. |

### Axis 3: Timescale (omega relative to 1/tau and omega_D)

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED | omega << 1/tau (low-frequency constitutive relaxation) AND omega << omega_D (Markovian) | **Verified** | First-order ODE: tau dPhi/dt + Phi = X. Iota-Prime. |
| CAUTION | omega ~ 1/tau (constitutive resonance) | **Unverified** | Non-exponential transients possible. Linear analysis still applies but approach to attractor may show non-monotonic behavior if underdamped corrections exist. |
| UNSAFE | omega > omega_D (non-Markovian, bath memory time resolved) | **Excluded** | Markovian truncation fails. Full retarded kernel K(t-s) required. Bath spectral density J(omega) unknown. |

### Axis 4: Coupling strength (Phi self-interaction and Phi-g coupling)

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED | Linear Phi (no self-interaction, no cubic saturation, no delay) | **Verified** | Linear CTP action produces exact constitutive law. A1-L2, A1-C4. |
| CAUTION | Weakly nonlinear Phi (cubic saturation h(v) = gamma v - delta v^3 from GRUT-II Nu) | **Unverified within CTP** | GRUT-II Nu demonstrated bistability at the ODE level. The CTP action for nonlinear Phi has not been written. Claim C4 (unique attractor) is voided in the nonlinear regime. |
| UNSAFE | Strong Phi-g coupling (Phi backreaction comparable to matter T_{mu nu}) | **Excluded** | Test-field approximation fails. Full coupled (g, Phi) dynamics required. A2-M1 unresolved. |

### Axis 5: UV/IR window

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED (IR) | l >> l_Planck, m >> m_Planck, energies << M_Pl c^2 | **Verified** | All mesoscopic and astrophysical applications. No UV sensitivity in the Diosi integral (regulated by R). |
| CAUTION | l ~ micron to mm scale (Casimir/short-range gravity experiments) | **Unverified** | Fifth-force constraints may bound Phi coupling. Not checked. |
| UNSAFE (UV) | l ~ l_Planck or energies ~ M_Pl c^2 | **Excluded** | EFT breaks down. Quantum gravity regime. No GRUT claim applies. |

### Axis 6: Quantum/classical regime

| Zone | Condition | Status | Governing structure |
|:----:|-----------|:------:|---------------------|
| CONTROLLED (Classical) | Phi_a → 0 (saddle-point / mean-field limit) | **Verified** | Constitutive law is the classical EOM. Langevin equation for stochastic extension. |
| CONTROLLED (Quantum, superposition) | Phi_a not small, but matter in spatial superposition on fixed Phi background | **Verified** | USL applies to matter superpositions. Phi_r is classical; the quantum content is in the matter branches of the CTP path integral, not in Phi itself. |
| CAUTION | Phi itself in superposition (quantum Phi_a dynamics beyond saddle point) | **Unverified** | Full quantum CTP path integral for Phi not performed. Quantum corrections to the constitutive law unknown. |
| UNSAFE | Phi and g simultaneously in superposition (quantum gravity for the constitutive sector) | **Excluded** | Requires quantum gravity. Outside EFT scope. |

---

## 2. Claim-to-Regime Map

Every surviving (non-retracted) claim from the A1 ledger, mapped to its valid regime.

| Claim | Statement (abbreviated) | Valid regime | Boundary |
|:-----:|------------------------|-------------|----------|
| S1 | Local action cannot produce dissipation (Bauer) | All | None — theorem |
| S2 | CTP is necessary and sufficient for constitutive sector | All dissipative regimes | Structural |
| S3 | Minimal explicit variables: (g_r, g_a, Phi_r, Phi_a) | Weak curvature, Markovian, overdamped, linear Phi | Breaks at strong curvature (X unknown), non-Markovian (memory), underdamped (inertial Phi), nonlinear Phi |
| ~~S4~~ | ~~No extra bath needed~~ | ~~—~~ | **RETRACTED in flat space** (A3). Survives only near horizons as OPEN. |
| C1 | CTP variation → tau dPhi/dt + Phi = X | Markovian, overdamped, linear, slowly-varying background | Fails if non-Markovian, underdamped, or nonlinear |
| C2 | iD Phi_a^2 → Gaussian white noise | Markovian, overdamped, thermal equilibrium, Ohmic bath | Fails if non-Ohmic, non-Markovian, or T → 0 (quantum noise regime) |
| C3 | D = k_B T tau (FDT) | Ohmic, high-T (k_B T >> hbar/tau) | Fails at low T (quantum FDT: D → hbar eta / 2 at T = 0) |
| C4 | Unique attractor Phi* = X | Linear Phi only | Voided if nonlinear (bistability from GRUT-II Nu) |
| C5 | Markovian law = leading truncation | omega_D >> 1/tau | Fails if omega_D ~ 1/tau (non-Markovian corrections enter) |
| C6 | tau is not determined by minimal action | All | Structural: always true. tau is an EFT parameter (A3 confirms). |
| Q1 | Integrating out Newtonian g → Diosi Delta_E | Newtonian (v << c), weak field, instantaneous potential | Fails at post-Newtonian order or near horizons |
| Q2 | Lambda = Gm^2/(hbar l) | l > 2R, Newtonian | Fails for l < 2R (use Diosi integral) or strong field |
| Q3 | Extended-body suppression ~ (l/R)^3 | l < 2R, uniform sphere | Fails for non-spherical bodies (different suppression); exact result requires body-specific Diosi integral |
| Q4 | USL is dephasing (1/l), not diffusion (l^2) | All Newtonian | Structural distinction; regime-independent within Newtonian limit |
| Q5 | USL has no FDT partner | Tree-level, Newtonian | At loop level, gravitational noise partner expected (unknown magnitude) |
| Q6 | USL and Level-1 are separate predictions | Within three-sector CTP structure | Could soften at loop level if gravitational noise contributes to Sectors 1-2 |
| L11 | Environmental bath provides tau, D, T (A3 result) | Flat space and weak field | Near horizons, gravitational bath (T_H) may contribute alongside environment |

---

## 3. Unsafe Extrapolation Blacklist

The following claims are EXPLICITLY FORBIDDEN. Any document, calculation, or communication that makes these claims is in violation of the Book A domain freeze.

| # | Forbidden claim | Why forbidden | Source of prohibition |
|---|----------------|---------------|---------------------|
| **X1** | "The GRUT CTP action is fully covariant." | It is not. The action is constructed in the Newtonian limit. No covariant form has been written. The X(g_r) functional is unspecified. | A1-L6, A1-L7, A2 Section 3.3 |
| **X2** | "The USL formula Lambda = Gm^2/(hbar l) applies at all separations." | It does not. Valid ONLY for l > 2R. For l < 2R, suppressed by (l/R)^3. The Gamma-Prime through Zeta-Prime roadmap was voided by this error. | Kappa-Prime, A1-L10 |
| **X3** | "The constitutive relaxation time tau is derived from the CTP action." | It is not. tau is an EFT parameter. The bath spectral density that determines it is not specified. | A1-C6, A3 |
| **X4** | "Gravity alone provides the dissipative bath for the constitutive field." | It does not in flat space. Three independent arguments against: D_grav → 0, super-Ohmic, second-law violation. | A3, Branch 1 failure modes |
| **X5** | "The GRUT EFT is valid near black hole horizons." | Not verified. X(g_r) is unspecified. Overdamped limit is untested. Newtonian USL is invalid. Backreaction is uncomputed. | A2 Section 3.3 |
| **X6** | "The constitutive field Phi has a unique attractor in the nonlinear regime." | It does not. GRUT-II Nu demonstrated bistability under cubic saturation + delay. C4 is restricted to the linear regime. | A1-C4, GRUT-II Nu |
| **X7** | "The CTP formalism has been demonstrated to be ghost-free for the GRUT coupling." | Ghost-freedom is argued by standard CTP reasoning but no GRUT-specific linearized stability analysis has been performed. | A2 Section 2.5 |
| **X8** | "The noise coefficient D is determined within the theory." | It is not. D = k_B T tau depends on the environmental temperature T and the relaxation time tau, both of which are EFT inputs. | A1-L3, A3 |
| **X9** | "The GRUT quantum prediction has been tested or is testable on a near-term timescale." | It has not and is not. The hardware gaps (T2, mass scale, hold time) are 5-15 years from closure. The voided Eta-Prime "2-5 years" claim is retracted. | Mu-Prime, Nu-Prime, A1-V3 |
| **X10** | "GRUT is a Theory of Everything." | Book A does not establish ToE status. It establishes a minimal irreversible EFT in a bounded domain. ToE claims require full covariance, UV completion, and quantitative predictions in all regimes — none of which are achieved. | Book A mandate |

---

## 4. Book A Closure Memo

### What Book A establishes

1. **The minimal CTP backbone is internally consistent within its declared regime.** Three CTP unitarity conditions pass. FDT is satisfied. No contradictions found under weak-curvature, Markovian, overdamped, linear, Ohmic conditions. (A1, A2)

2. **The backbone consists of five irreducible explicit elements** {L1 (CTP doubling), L2 (dissipation), L3 (noise), L4 (USL dephasing), L6 (source coupling X)} **plus one implicit element** {L11 (environmental bath providing tau, D, T)}. (A1, A3)

3. **The USL is derived as gravitational self-energy dephasing** at tree level in the Newtonian limit, with the extended-body Diosi integral providing the exact correction for l < 2R. (Inherited from Iota-Prime and Kappa-Prime; verified in A1-A2)

4. **The constitutive law is derived exactly** from the CTP action within the Markovian/overdamped regime. (Inherited from Iota-Prime; verified in A1)

5. **The dissipative bath is environmental, not gravitational,** in flat space and weak-field regimes. Gravity-only fails by three independent arguments. The theory is an EFT with environment-dependent parameters (tau, D, T). (A3)

6. **The domain of validity is explicitly bounded** along six axes (scale, curvature, timescale, coupling, UV/IR, quantum/classical) with controlled, caution, and unsafe zones for each. (A4)

7. **Ten unsafe extrapolations are explicitly blacklisted.** (A4)

8. **Four retracted claims from GRUT-II** (V1-V4) remain retracted and are not reinstated. (A1)

9. **Six closure conditions remain open** (MC1-MC6 from Book A). These are handed to subsequent stages. (A2)

### What Book A does NOT establish

1. **Full covariance.** The backbone is Newtonian. No covariant CTP action has been written.

2. **The functional form of X(g_r).** The source coupling is structurally required but functionally unspecified. This is the highest-priority open issue for Book B.

3. **The value of tau.** It is an EFT parameter, not a prediction.

4. **Strong-field validity.** The backbone is untested at R/R_S ~ 1. No claim of validity or invalidity is made.

5. **Loop-level completeness.** The one-loop gravitational noise kernel is not computed. The tree-level structure is complete; the loop-level structure is open.

6. **Nonlinear constitutive dynamics.** The CTP action covers the linear regime only. The GRUT-II bistability (cubic saturation + delay) has not been embedded in the CTP formalism.

7. **ToE status.** Book A does not claim or approach ToE closure.

### What Book B may assume from Book A

Book B (or any subsequent GRUT-III stage) may take the following as given without re-derivation:

| # | Assumption from Book A | Conditions |
|---|----------------------|------------|
| **BA1** | The CTP backbone {L1, L2, L3, L4, L6, L11} is internally consistent. | Within the controlled domain only. |
| **BA2** | The constitutive law tau dPhi/dt + Phi = X is the exact classical EOM of the CTP action. | Markovian, overdamped, linear, slowly-varying background. |
| **BA3** | The USL is Lambda = Gm^2/(hbar l) for l > 2R, with extended-body Diosi correction for l < 2R. | Newtonian, tree-level. |
| **BA4** | tau, D, T are EFT parameters provided by an environmental bath. | Flat space and weak field. Near horizons, a gravitational bath may contribute. |
| **BA5** | FDT holds: D = k_B T tau / 2 (CTP convention). | Ohmic, high-T, thermal equilibrium. |
| **BA6** | The unsafe extrapolation blacklist (X1-X10) is binding. | Always. |
| **BA7** | Claims V1-V4 are retracted. | Always. |

Book B may NOT assume:
- Any specific form of X(g_r)
- Any value of tau
- Any validity of the backbone at moderate or strong curvature
- Ghost-freedom of the GRUT-specific coupling (only of the general CTP framework)
- Completeness of the loop-level structure

---

## Gates

### A4-G1: All surviving claims are regime-bounded

**Status: PASS.**

Every claim in the A1 ledger is mapped to its valid regime in Section 2 above. No claim survives without explicit regime tags. The retracted claims (V1-V4) and the retracted flat-space S4 are marked accordingly.

### A4-G2: Unsafe extrapolations explicitly frozen

**Status: PASS.**

Ten forbidden claims (X1-X10) are listed in Section 3. Each carries the source of prohibition and the reason. The blacklist is binding on all subsequent stages.

### A4-G3: Book B dependency contract is clear

**Status: PASS.**

Seven assumptions (BA1-BA7) that Book B may inherit are listed in Section 4, each with conditions. Five things Book B may NOT assume are listed. The contract is explicit and bounded.

---

## Book A Final Status

| Stage | Gates | Status |
|:-----:|:-----:|:------:|
| A1: Backbone Freeze | G1 PASS, G2 PASS, G3 PASS | **CLOSED** |
| A2: Coupling Consistency | G1 PASS, G2 PASS, G3 PASS | **CLOSED** |
| A3: Bath Closure | Bounded-open (Branch 2 favored) | **CLOSED** (provisional: Branch 2 adopted pending D1 computation) |
| A4: Domain Freeze | G1 PASS, G2 PASS, G3 PASS | **CLOSED** |

**Book A: CLOSED.**

The minimal irreversible EFT is established, regime-bounded, and handed off. Six open closure conditions (MC1-MC6) are inherited by subsequent stages. The highest-priority next action is MC1: specify X[g_{mu nu}].

---

*GRUT III Book A Stage A4 complete. All gates pass. Regime matrix: 6 axes × 3 zones. Claim-to-regime map: 16 surviving claims bounded. Unsafe blacklist: 10 forbidden extrapolations. Book B contract: 7 inheritable assumptions, 5 non-inheritable items. Book A is CLOSED. The minimal CTP backbone is frozen, regime-bounded, and ready for handoff.*
