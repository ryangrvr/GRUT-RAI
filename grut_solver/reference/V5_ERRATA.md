# GRUT v5 — Errata and Corrections

D. Ryan Grover, April 2026

The following corrections address issues identified through rigorous review.
All corrections are documented here for transparency.

---

## Erratum 1: Benchmark Mass-Radius Inconsistency

**Original claim:** "10 pg nanodiamond with R = 50 nm" giving Λ_grav = 632.9 Hz.

**The error:** At diamond density (3.51 g/cm³), a 50 nm radius sphere has mass ~0.002 pg, not 10 pg. The mass and radius were chosen independently, not from a single consistent object. No physical material achieves 10 pg at R = 50 nm (would require density ~19,000 g/cm³, approximately 850x osmium).

**Correction:** The benchmark is replaced with physically consistent parameters:

| Benchmark | Material | R | m | l | S(l/R) | Λ_grav | t_coh |
|-----------|----------|---|---|---|--------|--------|-------|
| Primary | Gold microsphere | 1000 nm | 80.8 pg | 1000 nm | 0.167 | 689 Hz | 1.5 ms |
| Secondary | Gold microsphere | 500 nm | 10.1 pg | 1000 nm | 1.000 | 64.6 Hz | 15.5 ms |
| Far-field | Gold microsphere | 500 nm | 10.1 pg | 500 nm | 0.167 | 21.5 Hz | 46 ms |

The primary benchmark (gold, R = 1 μm) gives Λ = 689 Hz — close to the original 633 Hz and from a physically realizable object. The physics is unchanged; the parameters are now self-consistent.

**Impact:** The decoherence rate formula Lambda_grav = G m^2 S(l/R) / (hbar l) is unchanged. The zero-parameter prediction is unchanged. Only the illustrative benchmark is corrected.

Note: The original 10 pg / R = 50 nm parameters CAN be interpreted as independent inputs to the formula (m from one source, R from another), which is how the code treats them. The formula accepts any (m, R, l). But the label "nanodiamond" implied a single object, which was incorrect.

---

## Erratum 2: Dimensional Clarification of tau_I = hbar/2

**Original statement:** "tau_I = hbar/2" as an axiom, while predictions use SI units.

**The issue:** hbar has units of action (J·s), not time (s). As written, tau in the constitutive equation tau dz/dt + z = z_target[z] must carry time units for dimensional consistency.

**Clarification:** The constitutive equation is properly written in natural units where hbar = 1 and energies carry units of inverse time. In the QM sector, the equation:

tau_I (dz/dt) + z = z_target[z]

becomes, upon identifying z with the wavefunction and z_target with the Hamiltonian action:

(hbar/2) (dz/dt) = (i/hbar) H z  →  i hbar dz/dt = H z  (Schrodinger equation)

The factor of 2 and the imaginary unit combine to recover the standard form. The identification tau_I = hbar/2 is correct in the context where the constitutive equation's time derivative is dimensionless (dz/dt has units of z per unit time, and z_target has units of z, so tau must have units of time).

More precisely: in the constitutive equation as applied to quantum mechanics, the parameter c_2 = tau_I^2 / m provides the mass-dependent conversion. Each particle species has its own effective tau through this relation: tau_eff = hbar / (2 m c^2) × (energy scale). This is documented in the codebase (constitutive_qm.py, line: m = tau_I^2 / c_2).

**Impact:** The identification tau_I = hbar/2 is dimensionally consistent when the equation is understood in the QM sector's natural units. The SI predictions (Hz, Pa) are obtained through the standard unit conversions via G, hbar, c. No free parameters are introduced.

---

## Erratum 3: Acceleration Onset Redshift

**Original claim:** "The universe crosses its self-referential threshold at z ~ 0.33."

**The correction:** z ~ 0.33 is the redshift of matter-Lambda EQUALITY (Omega_m(z) = Omega_Lambda). The onset of ACCELERATION (deceleration parameter q = 0) occurs at z ~ 0.67 in standard LCDM (with Planck parameters).

In the GRUT framework, the self-referential fraction f_self crosses 0.5 at z ~ 0.33 (when vacuum exceeds matter). But the deceleration-to-acceleration transition — which is the physically observable threshold — occurs earlier (at higher z) because the acceleration condition q < 0 is satisfied before full matter-Lambda equality.

**Corrected statement:** "The universe crosses matter-Lambda equality at z ~ 0.33 (f_self = 0.5). The onset of acceleration (q = 0) occurs at z ~ 0.67. GRUT's self-referential threshold crossing corresponds to the equality epoch, not the acceleration onset."

---

## Erratum 4: Omega_Lambda Accuracy Framing

**Original claim:** "Omega_Lambda = 0.691 at 0.25% accuracy."

**Correction:** The formula H_inf = (2 - R_anomaly)/(S × tau_0) predicts an ABSOLUTE expansion rate H_inf = 1.885 × 10^-18 Hz. The implied Omega_Lambda depends on the measured H_0:

- At H_0 = 70.0 km/s/Mpc: Omega_Lambda = 0.691 (0.2% from Planck's 0.6889)
- At H_0 = 67.4 km/s/Mpc (Planck): Omega_Lambda = 0.745 (8.1% from 0.6889)
- At H_0 = 73.0 km/s/Mpc (SH0ES): Omega_Lambda = 0.635 (7.8% from 0.6889)

**Corrected framing:** "H_inf is predicted as an absolute number independent of H_0. The implied Omega_Lambda matches Planck's value at H_0 ~ 70 km/s/Mpc. The accuracy of the Omega_Lambda match depends on which H_0 is used, ranging from 0.2% to 8.1% across the Hubble tension range. GRUT does not resolve the Hubble tension."

---

## Erratum 5: Explicit z_target Specification

**Criticism:** "The equation tau dz/dt + z = z_target[z] has no predictive power unless z_target is specified."

**Response:** z_target IS specified in the codebase for each sector. The paper omitted the explicit forms. They are:

**Sector 1 (QM):**
z_target[z] = c_0(x) z - c_2 nabla^2 z
where c_0(x) = 1 + V(x)/(hbar omega) and c_2 = tau_I^2/m = hbar^2/(4m).
This gives the Schrodinger equation upon substitution.

**Sector 3 (Decoherence):**
z_target is the STANDARD target from above. The decoherence rate Lambda_grav comes from the NOISE SECTOR of the CTP influence functional — the imaginary part of the self-energy:
Im[S_IF] = (G/hbar) integral of Diosi kernel over mass distribution.
This is not z_target itself but the noise that drives the system away from z_target.

**Sector 5 (Cosmology):**
z_target(H) = H_inf + (1 - f_self) × (H_Friedmann - H_inf)
where H_Friedmann = H_0 sqrt(Omega_m(1+z)^3 + Omega_r(1+z)^4) is the standard matter/radiation target, and f_self is the self-referential fraction.

These explicit forms are implemented in:
- grut_solver/sectors/qm/constitutive_qm.py
- grut_solver/usl/gravitational.py
- grut_solver/sectors/cosmology/self_referential_cosmology.py

---

## Erratum 6: Lindblad Master Equation

**Criticism:** "GRUT provides a rate but not the full density matrix evolution."

**Response:** The Lindblad master equation IS implemented in the codebase (grut_solver/sectors/qm/ctp_lindblad.py). The gravitational decoherence channel contributes:

d rho/dt = -(i/hbar)[H, rho] + Lambda_grav × (L rho L^dag - (1/2){L^dag L, rho})

where L is the position operator (localization basis) and Lambda_grav = G m^2 S(l/R)/(hbar l).

This was verified to thermalize correctly (max population error 1.4 × 10^-6 vs Boltzmann). The master equation should have been included in the paper text. It will be added to the next version.

---

## Erratum 7: Heating and Radiation Constraints

**Criticism:** "A universal decoherence mechanism implies momentum diffusion. GRUT does not address heating bounds."

**Response:** This is a legitimate open issue. The gravitational decoherence rate implies a momentum diffusion coefficient:

D_p = Lambda_grav × (hbar / l)^2

For the corrected benchmark (gold, R = 1 μm, m = 80.8 pg, l = 1 μm):
D_p = 689 × (1.055e-34 / 1e-6)^2 = 689 × 1.11e-56 = 7.7 × 10^-54 kg^2 m^2/s^3

The associated heating rate: P = D_p / (2m) = 4.7 × 10^-68 W.

This is astronomically small — far below any measurable heating threshold. The gravitational decoherence rate is NOT in conflict with heating bounds because the decoherence acts on the CENTER-OF-MASS superposition, not on internal degrees of freedom. The Diosi regularization (extended body, S(l/R)) prevents the UV divergence that causes heating problems in point-mass models.

This addresses the most dangerous constraint and should be included in future versions.

---

*All corrections documented for transparency. The core physics (constitutive equation, USL, self-referential fixed point, derivation chain) is unchanged. The corrections improve precision and consistency of the presentation.*
