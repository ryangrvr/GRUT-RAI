# GRUT v7 — Appendix E: Information and Coarse-Graining

## Classical Reality as Decoherence-Created Information — Quantitative Results

---

## E.0 — Purpose

This appendix COMPUTES the rate of classical information creation from
gravitational decoherence, the channel capacity of the gravitational
decoherence channel, and the total classical information content of the
observable universe.

---

## E.1 — Decoherence Creates Classical Information

A quantum system in superposition |L> + |R> carries NO classical information
about position — it occupies both locations. After gravitational decoherence,
the density matrix becomes rho ~ p_L|L><L| + p_R|R><R| — now it carries
ONE BIT of classical information (which position was realized).

**Rate of classical information creation:**

    dI/dt = Lambda_grav × ln(2)    [nats/s per channel]                   (E.1)

Each decoherence event converts one quantum superposition into one
classical fact. The rate is Lambda_grav — the same quantity that sets
the decoherence timescale.

---

## E.2 — Information Timescale Across the Hierarchy

The time to create one bit of classical information from a quantum superposition:

    t_bit = 1 / Lambda_grav = hbar l / (G m^2 S(l/R))                    (E.2)

| System | m | Lambda_grav [Hz] | t_bit | Regime |
|:---|:---|:---|:---|:---|
| Electron | 9.1 × 10^-31 kg | 5.3 × 10^-27 | 6 × 10^12 Myr | Deep quantum |
| C60 fullerene | 1.2 × 10^-24 kg | 9.1 × 10^-17 | 350 Myr | Quantum |
| Protein (500 amu) | 8.3 × 10^-25 kg | 4.4 × 10^-16 | 73 Myr | Boundary |
| Gold 1 um sphere | 80.8 pg | 4.1 × 10^3 | 0.2 ms | Classical |
| Bacterium | 1 pg | 0.63 | 1.6 s | Marginally classical |
| Cat (5 kg) | 5 kg | 1.6 × 10^27 | 6 × 10^-28 s | Ultra-classical |
| Human (70 kg) | 70 kg | 3.1 × 10^28 | 3 × 10^-29 s | Ultra-classical |

**The pattern:** Quantum systems take cosmological times to produce one bit
of classical information (electrons: 10^12 Myr). Classical systems produce
bits at incomprehensibly fast rates (humans: 10^28 bits/s). The boundary
is at the protein/bacterium scale — exactly where biology operates.

**A protein takes 73 Myr to produce one bit.** This is comparable to tau_0
(41.9 Myr) — the same constitutive timescale that enters the cosmological
formula. The protein scale IS the decoherence crossover scale.

---

## E.3 — Channel Capacity of Gravitational Decoherence

The gravitational decoherence channel transmits classical position information
from the quantum system to the gravitational field. Its Holevo capacity:

    C = Lambda_grav × log_2(N_states)    [bits/s]                         (E.3)

where N_states = L/l is the number of distinguishable position states
(region size L, superposition separation l).

| System | Lambda [Hz] | N_states | C [bits/s] |
|:---|:---|:---|:---|
| Protein | 4.4 × 10^-16 | 1,000 | 4.4 × 10^-15 |
| Gold 1 um | 4.1 × 10^3 | 1,000 | 4.1 × 10^4 |
| Bacterium | 0.63 | 100 | 4.2 |
| Sand grain | 1.1 × 10^5 | 10,000 | 1.4 × 10^6 |
| Baseball | 4.7 × 10^21 | 100 | 3.1 × 10^22 |

**The Holevo capacity is the MAXIMUM rate** at which any measurement can
extract classical position information from the system. No experiment can
learn the system's position faster than the gravitational decoherence
channel provides it.

---

## E.4 — Mutual Information: System ↔ Gravitational Field

Before decoherence, the system and its gravitational field are uncorrelated:

    I(system : gravity) = 0

After decoherence, they are classically correlated (the gravitational field
"knows" where the mass is):

    I(system : gravity) = S_decoherence = Lambda_grav × t × ln(2)        (E.4)

This mutual information is CREATED by the decoherence process. It is the
physical content of the quantum-to-classical transition: the system's
position becomes correlated with the gravitational field, creating a
classical record that any observer can read.

---

## E.5 — The Quantum-Classical Information Boundary

The control parameter Xi = Lambda_grav × t_obs determines the information regime:

    Xi << 1:  Quantum information (no classical record, requires tomography)
    Xi = 1:   Boundary (one bit of classical information per observation)
    Xi >> 1:  Classical information (definite, recordable, shareable)

**At t_obs = 1 second, l = 1 um:** The boundary mass is ~10^12 amu
(~10^-15 kg, the mass of a large virus). Objects heavier produce ≥ 1 bit/s
of classical information through gravitational decoherence.

**The measurement problem in GRUT:** A measurement device must be in the
Xi >> 1 regime to function — it must produce classical information fast
enough to record an outcome. This is automatic for any macroscopic device
(Xi ~ 10^20+ for lab equipment). The "collapse" is the gravitational
decoherence of the measurement apparatus, not a separate postulate.

---

## E.6 — Total Classical Information in the Observable Universe

The total classical information created by gravitational decoherence over
the age of the universe:

    I_total = sum over all objects: Lambda_grav(m, l) × age × ln(2)

The dominant contribution comes from galaxy clusters (~10^15 M_sun each,
~10^6 in the observable universe):

| Quantity | Value |
|:---|:---|
| Lambda per cluster | 2.5 × 10^92 Hz |
| Bits per cluster over 13.8 Gyr | 1.1 × 10^110 |
| Total clusters | ~10^6 |
| **Total classical bits** | **~10^116** |
| Holographic bound (10^122 bits) | 10^122 |
| **Fraction of holographic bound** | **10^-6** |

**The GRUT interpretation:** Gravitational decoherence has converted
approximately ONE MILLIONTH of the universe's holographic information
capacity into classical reality. The remaining 99.9999% is still quantum
— inaccessible to classical observation.

The classical universe we observe is the thin surface layer of a vastly
larger quantum information structure. We see 10^116 bits of classical
reality embedded in 10^122 bits of total capacity. The rest is hidden
behind the decoherence boundary — not destroyed, but quantum.

---

## E.7 — Limitations

- The channel capacity (E.3) assumes independent decoherence channels
  (no entanglement between position states)
- The total information estimate uses crude cluster-scale approximation;
  a proper computation would integrate over the mass function
- The Holevo bound is an upper limit; actual information extraction
  may be lower
- The "measurement problem" interpretation (E.5) is structural, not
  a derivation of the Born rule (which comes from Z = 1 in the CTP)
- No quantum error correction or information recovery is computed
  (except for BH information in main document)

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix E: Information and Coarse-Graining.*
