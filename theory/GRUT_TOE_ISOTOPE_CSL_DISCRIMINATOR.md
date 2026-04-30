# GRUT-vs-CSL Isotope-Pair Discriminator

*Auto-generated from `grut/derived/decoherence/csl_discriminator.py`.*

GRUT predicts decoherence rate Λ ∝ m² (quadratic in mass). CSL predicts Λ ∝ λN (or λm), linear in nucleon count or mass. Isotope substitution within the same element holds geometry and chemistry constant, isolating the mass-scaling difference as a clean, parameter-cancelling discriminator (λ drops out of the ratio).

## Predictions

| Pair | mass ratio | GRUT (m²) | CSL linear-N | Discriminator | Precision needed |
|:---|---:|---:|---:|---:|---:|
| 30Si/28Si | 1.0714 | 1.1478 | 1.0714 | +7.13% | 3.82% |
| 109Ag/107Ag | 1.0187 | 1.0378 | 1.0187 | +1.87% | 0.95% |
| 184W/182W | 1.0110 | 1.0221 | 1.0110 | +1.10% | 0.56% |

## Discriminator framing

GRUT is parameter-free at this scale. The prediction Λ_grav = Gm² S(l/R) / (ℏl) has every input known. Isotope substitution at fixed geometry gives ratio = (m_heavy/m_light)² with no free parameter.

CSL has localization parameter λ as a free input. Different published λ values (GRW λ ≈ 10⁻¹⁶ s⁻¹, Adler enhanced, Bassi-Pearle range) span orders of magnitude. The CSL-predicted ABSOLUTE rate is λ-dependent. But the CSL ratio between isotopes is λ-INDEPENDENT — λ cancels.

So the GRUT-vs-CSL discriminator is purely STRUCTURAL: quadratic vs linear scaling. The discriminator factor is approximately the mass ratio itself (1-7% across the isotope pairs above).

## Experimental program

Matter-wave interferometry programs (MAQRO, MAGIS-100, atom interferometers, optomechanical levitation) target decoherence-rate precisions in the ~1-10% range over the next decade. The Si pair is detectable at <5% precision; the Ag pair at <1%; the W pair at <0.5%. MAQRO's design sensitivity puts the Si and Ag discriminators within reach.

## Detailed entries

### 30Si/28Si

- **Element:** Si
- **Light isotope:** 28Si (m = 27.976927 amu)
- **Heavy isotope:** 30Si (m = 29.973770 amu)
- **Mass ratio (heavy/light):** 1.071375
- **GRUT predicted ratio (m²):** 1.147844
- **CSL predicted ratio (linear-N):** 1.071429
- **CSL predicted ratio (Adler mass-prop):** 1.071375
- **GRUT − CSL difference:** +7.132%
- **Discriminating precision required:** 3.821% (2σ-level)

### 109Ag/107Ag

- **Element:** Ag
- **Light isotope:** 107Ag (m = 106.905097 amu)
- **Heavy isotope:** 109Ag (m = 108.904752 amu)
- **Mass ratio (heavy/light):** 1.018705
- **GRUT predicted ratio (m²):** 1.037760
- **CSL predicted ratio (linear-N):** 1.018692
- **CSL predicted ratio (Adler mass-prop):** 1.018705
- **GRUT − CSL difference:** +1.872%
- **Discriminating precision required:** 0.953% (2σ-level)

### 184W/182W

- **Element:** W
- **Light isotope:** 182W (m = 181.948205 amu)
- **Heavy isotope:** 184W (m = 183.950932 amu)
- **Mass ratio (heavy/light):** 1.011007
- **GRUT predicted ratio (m²):** 1.022135
- **CSL predicted ratio (linear-N):** 1.010989
- **CSL predicted ratio (Adler mass-prop):** 1.011007
- **GRUT − CSL difference:** +1.103%
- **Discriminating precision required:** 0.557% (2σ-level)


Verify:
  [PASS] grut_predicts_larger_than_csl_for_heavy_isotope
  [PASS] si_discriminator_above_5_pct
  [PASS] ag_discriminator_around_2_pct
  [PASS] w_discriminator_around_1_pct
  [PASS] discriminator_matches_mass_ratio_minus_one
  [PASS] csl_variants_agree_to_0p1_pct
