# GRUT II Beta-Prime — Universal Scaling Law Experimental Constraint Audit

## Is the USL Already Excluded by Existing Quantum Experiments?

---

## Part I — Experimental Class Inventory

### Class 1: Large-Molecule Matter-Wave Interferometry

**Record (2025): Arndt group, Vienna — sodium nanoparticle clusters**
- Mass: ~170,000 amu = 2.8 × 10^-22 kg
- Particle size: ~8 nm diameter
- Delocalization: dozens of times particle diameter (~100+ nm)
- Interference: observed (high visibility)
- Source: Pedalino et al., Nature (2025)

**Previous record (2019): Fein et al., Vienna — functionalized oligoporphyrins**
- Mass: >25,000 amu = 4.2 × 10^-23 kg
- Grating period: 266 nm → effective branch separation l ~ 270 nm
- Coherence time: >7 ms
- Visibility: 25% ± 3%
- Source: Fein et al., Nature Physics 15, 1242 (2019)

### Class 2: Optomechanical / Ground-State Cooling

**LIGO mirrors (2021): Whittle et al.**
- Mass: 10 kg (effective)
- Achievement: ground state (10.8 phonons avg)
- BUT: NOT a spatial superposition experiment. No coherence/decoherence bound on gravitational decoherence.

**Bulk acoustic (2025):**
- Mass: 7.5 micrograms
- Achievement: ground state (<0.4 phonons)
- NOT a spatial superposition.

### Class 3: Levitated Nanoparticles

**Delic et al. (2020): Aspelmeyer group — silica nanoparticle**
- Mass: ~10^9 amu = few × 10^-18 kg
- Size: 143 nm diameter
- Achievement: ground state (0.43 phonons)
- Coherence time: 7.6 microseconds
- BUT: NO spatial superposition yet. Ground-state preparation only.
- Zero-point fluctuation: ~10^-12 m (sub-picometer)

**Proposals (2024): Romero-Isart et al.**
- Target: 100 nm silica particle, mass ~10^8 amu
- Target delocalization: several nm
- Target coherence: milliseconds
- Status: PROPOSED, not yet achieved

### Class 4: Atom Interferometers

**Stanford 10m tower (Kasevich group)**
- Atom: Rb (87 amu = 1.44 × 10^-25 kg)
- Path separation: up to 54 cm
- Interrogation time: up to 2 s

**Panda et al. (2024) — lattice atom interferometry**
- Atom: Sr (87 amu)
- Coherence time: up to 70 seconds
- Path separation: sub-micrometer (optical lattice spacing)

**MAGIS-100 (under construction, Fermilab)**
- 100-meter baseline
- Target: meter-scale separations for seconds

---

## Part II — USL Prediction Table

### The USL formula

```
Lambda_USL = G m^2 / (hbar l)

where:
  G = 6.674 × 10^-11 m^3 kg^-1 s^-2
  hbar = 1.055 × 10^-34 J s
  m = superposed mass (kg)
  l = branch separation (m)
```

### Predictions vs observations

| Experiment | m (kg) | l (m) | Lambda_USL (s^-1) | tau_USL (s) | Observed coherence | Status |
|-----------|--------|-------|-------------------|------------|-------------------|--------|
| **Fein 2019 (molecules)** | 4.2e-23 | 2.7e-7 | **4.4e-10** | 2.3e9 | >7 ms | **FAR BELOW sensitivity** |
| **Arndt 2025 (Na clusters)** | 2.8e-22 | 1e-7 | **5.0e-8** | 2.0e7 | Interference observed | **FAR BELOW sensitivity** |
| **Kasevich (Rb atoms, 54cm)** | 1.4e-25 | 0.54 | **1.6e-22** | 6.2e21 | 2 s coherent | **NEGLIGIBLE** |
| **Panda 2024 (Sr, 70s)** | 1.4e-25 | 1e-7 | **8.8e-16** | 1.1e15 | 70 s coherent | **NEGLIGIBLE** |
| **Delic 2020 (nanoparticle)** | 1e-18 | 1e-12 (ZPF) | **6.3e5** | 1.6e-6 | 7.6 us | **WOULD CONSTRAIN if superposed** |
| **MAQRO proposal** | 1e-17 | 1e-7 | **6.3e-2** | 16 | ~100 s target | **TESTABLE** |
| **Future nano (100nm, 10nm sep)** | 1e-18 | 1e-8 | **6.3e3** | 1.6e-4 | ms target | **TESTABLE** |

### Key findings from the table

**All existing matter-wave interferometry experiments are MANY orders of magnitude away from the USL prediction.** The Arndt 2025 record (Lambda_USL = 5 × 10^-8 s^-1) predicts decoherence on a timescale of ~200 days. The experiment observes interference over milliseconds. The USL prediction is 10^10 times weaker than needed to affect the experiment.

**The only regime where Lambda_USL becomes significant is the levitated-nanoparticle regime** (m ~ 10^-18 kg) with spatial superpositions (not yet achieved). The Delic 2020 experiment prepared the ground state but did not create a spatial superposition.

---

## Part III — Bound Interpretation

### Does current data constrain the USL?

**NO.** The USL rate is so small for all existing interferometry experiments that it is completely invisible. The gravitational decoherence predicted by the USL is:

- For the best molecule experiment: Lambda = 5 × 10^-8 s^-1. This predicts coherence loss of ~10^-10 over the 7 ms experiment duration. Completely undetectable.
- For the best atom interferometer: Lambda = 10^-22 s^-1. Negligible on any timescale.
- For any current optomechanical system: no spatial superposition exists to test.

### What about the Diosi-Penrose bounds?

The Donadi et al. (2021) Gran Sasso experiment **ruled out the parameter-free DP model** (R_0 at nuclear scale). The DP model predicts Lambda ~ Gm^2/(hbar R) where R is the object SIZE (not the superposition separation).

**The USL differs from DP:** Lambda_USL = Gm^2/(hbar l) where l is the SEPARATION. For the DP-relevant regime (compact objects, R ~ nuclear), the DP rate is enormous and was ruled out. But the USL rate depends on the SEPARATION l, which is typically much larger than R. For a molecule in a Talbot-Lau interferometer (l ~ 270 nm >> R ~ 1 nm), the USL gives a much SMALLER rate than DP.

**The DP exclusion does NOT exclude the USL.** They are different scalings applied to different length scales.

### Residual decoherence budget

For the Fein 2019 experiment:
- Measured visibility: 25% ± 3%
- Expected visibility (QM + known decoherence): ~25-30%
- Residual unexplained decoherence: consistent with zero (within ~10% uncertainty)
- Upper bound on extra decoherence rate: Lambda_extra < ~100 s^-1 (rough, from visibility decay)

The USL predicts Lambda = 4.4 × 10^-10 s^-1. This is 11 orders of magnitude below the experimental sensitivity to extra decoherence.

**The USL is FAR below the noise floor of all current experiments.**

---

## Part IV — Scaling Window

### Where does the USL become testable?

The USL rate Lambda = Gm^2/(hbar l) scales as m^2/l. To reach Lambda ~ 1 s^-1 (detectable with ~1 s coherence time):

```
Gm^2/(hbar l) = 1
m^2/l = hbar/G = 1.055e-34 / 6.674e-11 = 1.58e-24 kg^2/m
```

For l = 100 nm = 10^-7 m: m = sqrt(1.58e-24 × 10^-7) = sqrt(1.58e-31) = 1.26e-16 kg ~ 10^11 amu.

This corresponds to a **~100 nm silica particle** (mass ~10^-16 to 10^-17 kg) superposed over ~100 nm. This is EXACTLY the MAQRO-class experiment target.

### The experimental frontier

| Platform | Mass target | Separation target | Lambda_USL | Detectable? | Timeline |
|----------|-----------|-----------------|-----------|:----------:|---------|
| **MAQRO** (space) | 10^-17 kg | 100 nm | ~0.06 s^-1 | **YES** (if ~100 s coherence) | 2030s |
| **Levitated nano** (ground) | 10^-18 kg | 10 nm | ~6000 s^-1 | **YES** (if ms coherence) | 2025-2028 |
| **Levitated nano** (ground) | 10^-18 kg | 100 nm | ~600 s^-1 | **YES** (if ms coherence) | 2025-2028 |
| **Molecule interfero.** | 10^-22 kg | 270 nm | ~5e-8 s^-1 | **NO** (too weak) | — |
| **Atom interfero.** | 10^-25 kg | 1 m | ~10^-22 s^-1 | **NO** (negligible) | — |

**The MAQRO-class and levitated-nanoparticle platforms are the ONLY viable routes to testing the USL in the next decade.**

### The critical threshold

For a levitated nanoparticle (m ~ 10^-18 kg) superposed over l ~ 10 nm:
```
Lambda_USL = 6.3 × 10^3 s^-1
tau_USL = 0.16 ms
```

This predicts decoherence in ~0.16 ms. If such a superposition is created and coherence is observed for >1 ms, the USL is EXCLUDED at this mass/separation. If coherence is lost at ~0.1-1 ms (faster than environmental models predict), the USL is SUPPORTED.

---

## Part V — Structural Consequence

### If the USL is excluded

A definitive exclusion (coherence observed at Lambda > Lambda_USL) would mean:
- The anomaly-motivated decoherence scaling fails
- The E_grav ~ hbar Lambda identification is wrong
- The Phase II EQ-QUANTUM-001 (m^{-2/3} law for mass-dependent decoherence) loses its foundation
- GRUT II's quantum-gravitational thread is severed

**This would be a MAJOR structural loss.** The USL is the deepest connection between the IR anomaly and quantum mechanics in the GRUT program.

### If the USL is far below bounds

The USL remains VIABLE but untested. This is the current status. The program continues as before: the USL is a prediction that has not yet been reached by experiment.

### If the USL is near current bounds

This is the most interesting scenario: the levitated-nanoparticle experiments expected in the next 2-5 years will probe EXACTLY the USL range for m ~ 10^-18 kg. The USL prediction (Lambda ~ 10^3-10^4 s^-1 at this mass) is in the sensitive window of these experiments.

**The USL is entering its first real experimental test window in the next 2-5 years.**

---

## Part VI — Final Verdict

### usl_far_below_current_sensitivity + usl_near_future_test_window_identified.

The USL prediction Lambda = Gm^2/(hbar l) is:

1. **Consistent with ALL existing data.** No current experiment is sensitive enough to detect or exclude it. The predicted rates are 8-22 orders of magnitude below experimental sensitivity for molecule and atom interferometry.

2. **Not yet tested.** The levitated-nanoparticle experiments that could test it (spatial superposition of ~10^-18 kg objects) have not yet been performed. Ground-state cooling has been achieved but spatial superposition has not.

3. **Entering the test window.** The next generation of levitated-nanoparticle experiments (2025-2028) and space-based proposals (MAQRO, 2030s) target EXACTLY the mass and separation range where Lambda_USL becomes detectable. For m ~ 10^-18 kg and l ~ 10-100 nm, the predicted decoherence time is 0.1-10 ms — directly accessible.

4. **Distinguishable from DP.** The USL scaling (Lambda ~ m^2/l) differs from Diosi-Penrose (Lambda ~ m^2/R). The DP parameter-free version is already excluded (Donadi 2021). The USL is NOT excluded because it uses the SEPARATION l rather than the SIZE R.

### Public-Facing Paragraph

GRUT II Beta-Prime establishes that the universal scaling law Lambda = Gm^2/(hbar l) for gravitational decoherence is consistent with all existing experimental data. No current quantum experiment is sensitive enough to test it: the predicted decoherence rates are many orders of magnitude below the sensitivity of molecule and atom interferometry. However, the next generation of levitated-nanoparticle experiments (targeting spatial superposition of ~10^-18 kg objects over ~10-100 nm separations) will probe exactly the regime where the USL predicts measurable decoherence (Lambda ~ 10^3-10^4 s^-1, corresponding to coherence times of ~0.1-1 ms). The USL is distinguishable from the already-excluded parameter-free Diosi-Penrose model because it depends on the superposition SEPARATION rather than the object SIZE. The first direct test of the USL is expected within the next 2-5 years from ground-based levitated-nanoparticle experiments, with space-based tests (MAQRO) possible in the 2030s.

### Internal Doctrine

A serious empirical win would be: a levitated-nanoparticle experiment observing excess decoherence at a rate CONSISTENT with Lambda = Gm^2/(hbar l) and INCONSISTENT with known environmental decoherence sources. This would be the first experimental evidence for the anomaly-motivated gravitational decoherence scaling. A serious empirical loss would be: the same experiment observing coherence BEYOND the USL prediction (tau_observed >> tau_USL), which would exclude the scaling. The current status is: UNTESTED. The USL prediction for the most promising experimental regime (m ~ 10^-18 kg, l ~ 10 nm) gives Lambda ~ 6000 s^-1, predicting decoherence in ~0.16 ms. If coherence is maintained for >1 ms at these parameters, the USL is excluded. If decoherence occurs at ~0.1 ms with no environmental explanation, the USL is supported.

### Next Forced Move

Compute the EXACT USL prediction for the specific parameters of the most advanced levitated-nanoparticle experiment (Delic/Aspelmeyer group or equivalent). This means: take the actual particle mass, the planned superposition protocol, the expected environmental decoherence budget, and determine whether the USL signal is above or below the environmental noise floor. If above: the experiment will test the USL. If below: a larger mass or longer coherence time is needed.

---

*GRUT II Beta-Prime complete. USL: consistent with all current data (far below sensitivity). Near-future test window: levitated nanoparticles (m ~ 10^-18 kg, l ~ 10-100 nm, Lambda_USL ~ 10^3-10^4 s^-1). First direct test expected in 2-5 years. DP exclusion does not affect USL. Verdict: usl_far_below_current_sensitivity + usl_near_future_test_window_identified.*
