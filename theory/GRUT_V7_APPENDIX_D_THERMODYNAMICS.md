# GRUT v7 — Appendix D: Thermodynamics and the Arrow of Time

## Entropy Production from CTP Structure — Quantitative Results

---

## D.0 — Purpose

This appendix COMPUTES the entropy production rate from the constitutive
equation and shows that the arrow of time, the second law, and the
entropy budget of the universe all follow from S_CTP.

---

## D.1 — The Constitutive Entropy Production Rate

For the constitutive equation tau dz/dt + z = z_target[z] + xi(t), the
entropy production rate (Schnakenberg 1976, Seifert 2012) is:

    dS/dt = (1/tau) × <(z - z_target)^2> / sigma_eq^2                    (D.1)

where sigma_eq^2 = k_B T is the thermal equilibrium fluctuation.

From the FDT: at steady state, <(z - z_target)^2> = N tau / 2 = k_B T,
giving the MAXIMUM entropy production rate:

    dS/dt |_max = 1/tau = gamma     (the dissipation rate)                (D.2)

At the fixed point z = z_target[z]: dS/dt → 0 (equilibrium, no production).
During relaxation: dS/dt > 0 (the second law).

---

## D.2 — Gravitational Decoherence IS Entropy Production

The gravitational decoherence rate Lambda_grav is an entropy production rate:
it measures how fast the von Neumann entropy of the reduced density matrix
increases. Each decoherence event produces ln(2) nats of entropy (one bit
of classical information created from one destroyed superposition).

    dS_vN/dt = Lambda_grav × ln(2)    [nats/s per channel]               (D.3)

**Computed entropy production rates across the hierarchy of structure:**

| System | m [kg] | l [m] | Lambda_grav [Hz] | dS/dt [bits/s] |
|:---|:---|:---|:---|:---|
| Electron | 9.1 × 10^-31 | 10^-10 | 5.3 × 10^-27 | 5.3 × 10^-27 |
| C60 fullerene | 1.2 × 10^-24 | 10^-8 | 9.1 × 10^-17 | 9.1 × 10^-17 |
| Protein (500 amu) | 8.3 × 10^-25 | 10^-9 | 9.1 × 10^-18 | 9.1 × 10^-18 |
| Gold 1 um sphere | 80.8 × 10^-15 | 10^-6 | 4.1 × 10^3 | 4.1 × 10^3 |
| Bacterium | 10^-15 | 10^-6 | 0.63 | 0.63 |
| Grain of sand | 10^-9 | 10^-6 | 1.1 × 10^5 | 1.1 × 10^5 |
| Baseball | 0.15 | 10^-2 | 4.7 × 10^21 | 4.7 × 10^21 |
| Earth | 6 × 10^24 | 10^7 | 2.3 × 10^66 | 2.3 × 10^66 |

**The pattern:** Entropy production from gravitational decoherence scales
as m^2 × S(l/R) / l. Macroscopic objects produce enormous amounts of
entropy per second — this is WHY they are classical. The classical world
is the high-entropy-production regime of the constitutive dynamics.

**The quantum-classical boundary:** At Lambda_grav ~ 1 Hz (the bacterium
scale), gravitational entropy production becomes macroscopically relevant.
Below: quantum coherence (negligible entropy production). Above: classical
definiteness (overwhelming entropy production). The boundary is continuous,
not sharp.

---

## D.3 — The Second Law from CTP

**Theorem:** For the constitutive equation with FDT-consistent noise,
the entropy S(t) = -Tr(rho ln rho) is monotonically non-decreasing.

**Proof:**
1. The Lindblad form of the master equation (from S_CTP) generates a
   completely positive trace-preserving (CPTP) map
2. The von Neumann entropy is non-decreasing under CPTP maps
   (Lindblad 1975, Wehrl 1978)
3. The CTP noise kernel generates a CPTP map at each time step
4. Therefore S(t + dt) >= S(t) for all dt > 0

This is standard in open quantum systems. What GRUT adds: the noise kernel
is not environmental — it comes from S_CTP itself. The second law is
INTRINSIC to the dynamics, not imported from a heat bath.

---

## D.4 — The Arrow of Time

Axiom A1 (retarded variation) selects the causal, forward-in-time dynamics:

    delta S_CTP / delta z_a = 0  →  retarded Green's function

This is the foundational asymmetry. The constitutive equation inherits it:

    tau dz/dt + z = z_target[z]

relaxes TOWARD z_target (forward in time), not AWAY from it. The information
about the initial condition decays as exp(-t/tau) — irreversible by construction.

**The arrow of time is not derived from entropy or initial conditions.
It IS Axiom A1.** The retarded choice is the defining asymmetry of the
CTP formalism. Entropy increase is a CONSEQUENCE, not a cause.

**The cosmological arrow:** The constitutive cosmology (Appendix B) inherits
this arrow. H(t) relaxes toward H_inf through the era map. The eras progress
forward (0 → 329), never backward. The expansion history is irreversible
because the constitutive equation is dissipative.

---

## D.5 — Three Entropy Sources from One Action

The CTP effective action produces three distinct entropy sources:

| Source | Rate | Origin in S_CTP | Physical effect |
|:---|:---|:---|:---|
| Gravitational decoherence | Lambda_grav [Hz] | Im(S_IF) = noise kernel | Quantum → classical |
| Cosmological relaxation | (H - H_inf)^2 / (tau H_inf^2) | Constitutive dynamics | Expansion → de Sitter |
| Thermal equilibration | 1/tau_KMS = 2pi k_B T / hbar | FDT / KMS condition | Temperature equalization |

All three come from ONE object: the CTP effective action S_CTP. The noise
kernel gives Lambda_grav. The constitutive equation gives the cosmological
relaxation. The FDT gives the thermal rate. One action, three entropy sources.

---

## D.6 — Black Hole Entropy as Constitutive Information Transfer

The Bekenstein-Hawking entropy S_BH = 4 pi G M^2 / (hbar c) is the maximum
entropy of a region of mass M. The constitutive memory kernel provides the
mechanism for transferring this entropy to Hawking radiation:

    I_dot(M) = eta(M) × c^3 / (1920 G M ln 2)    [bits/s]

In the tau_0 branch (eta ~ 1): the information transfer rate equals the
Hawking emission rate. The BH entropy is transferred, not destroyed.
The Page curve turns over at the halfway point (unitarity preserved).

**The constitutive interpretation:** BH evaporation is the REVERSE of entropy
production — the constitutive memory kernel "un-decoheres" the information
that was locked behind the horizon, transferring it to outgoing radiation.

---

## D.7 — Limitations

- The entropy production formula (D.1) uses the classical FDT; quantum
  corrections (coth factor) modify the rate at low T
- The cosmological entropy production is not integrated to give a total entropy
- The BH recovery fraction (99.94%) comes from the full coupled simulation
  (main document Section 25), not from the simplified formula here
- The second-law proof applies to the Lindblad channel; whether it extends
  to the full constitutive gravity sector is not proven
- The arrow of time is POSTULATED (A1), not derived — this is a limitation
  shared with all causal dynamical theories

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix D: Thermodynamics and the Arrow of Time.*
