# Errata / Corrigendum: D7/D8 Source Amplification Sign Error

## Affecting: GRUT_STRONG_FIELD_CLOSURE_D10_MASTER (Zenodo)

**Date of Discovery:** April 2026 (Book XVI Alpha)
**Author:** D. Ryan Grover
**Severity:** CRITICAL — affects all conditional surplus claims in D7-D10

---

## 1. The Error

### Published Claim (D7, in D10 Master Document)

Phase D7 claimed that the defect energy integrated above radius r provides source amplification:

```
m_eff(r) = M + beta_XR * Sigma_defect(r)
```

where Sigma_defect(r) = integral from r to R_ext of 4*pi*r'^2 * eps_defect dr' is the integrated defect energy ABOVE radius r.

This was classified as "STRONGLY SUPPORTED" with "12.7× constructive source amplification."

### The Correction

By Birkhoff's theorem, the gravitational field at radius r in a spherically symmetric system depends ONLY on the mass ENCLOSED within r. The defect energy above r is NOT enclosed at r. The correct formula is:

```
m_enclosed(r) = M_ext - Sigma_defect(r) - Sigma_scalar(r)
```

The sign is REVERSED. Defect energy above r REDUCES the enclosed mass, not increases it.

### Quantitative Impact

| lambda | A_eff (Published) | A_eff (Corrected) | Overprediction Factor |
|--------|------------------|------------------|----------------------|
| 5 | ~1.42 | ~0.28 | 5× |
| 10 | ~1.60 | ~0.23 | 7× |
| 25 | ~1.94 | ~0.11 | 17× |
| 50 | ~2.22 | ~0.01 | 222× |
| 100 | ~2.44 | ~0.01 | 244× |

---

## 2. Impact on Published Claims

| Claim | Published Status | Corrected Status |
|-------|-----------------|-----------------|
| D7 source amplification | STRONGLY SUPPORTED | **RETRACTED** (sign error) |
| D7 "12.7× constructive" | Claimed | **RETRACTED** (actual: ~0.06× attenuation) |
| D8 action grounding | STRONGLY SUPPORTED | MATHEMATICALLY VALID; amplification channel retracted |
| D9 proxy self-consistency | PROXY-DEPENDENT | Requires reassessment (proxy assumed amplification) |
| Conditional surpluses (2-3) | Implied by D7 | **COLLAPSED to 0** |

---

## 3. What Remains Valid

The sign error affects ONLY the source amplification channel (D7 Channel 2). The following are UNAFFECTED:

- **D1-D5:** Independent of amplification
- **D6 additive companion:** Defect-only metric support WORKS at lambda >= 25 (f = +0.50)
- **D8 gravitational penalty channel:** Exact and action-derived
- **D8 portal coupling:** Mathematically valid (g_p Phi^2 |vec_Phi|^2)
- **D10 trigger analysis:** Valid within stated scope
- **D11-D14:** Valid as assessments
- **All Phase I-VII results:** Independent

---

## 4. How the Error Was Discovered

Book XVI Alpha (April 2026) performed a self-consistent A_eff bootstrap computation:

1. Start with D7/D8 proxy A_eff
2. Compute peak processing energy: eps = A^2 M^2/(2 tau^2 r^4)
3. Integrate mass from R_ext inward including ALL energy contributions
4. Extract actual enclosed mass at R_eq
5. Compute new A_eff from self-consistent mass

The self-consistent computation showed m_enclosed(R_eq) ~ 0.05 (not 0.95), giving A_eff ~ 0.11 (not 1.94). The discrepancy was traced to the Birkhoff sign error in the D7 formula.

Code: `grut/quasi_static_rate.py`
Documentation: `docs/BOOK_XVI_TARGET_ALPHA_QUASI_STATIC_RATE_ANALYSIS_AND_AEFF_BRIDGE_AUDIT.md`

---

## 5. Positive Consequence

The D6 defect-only result (no amplification needed) survives and is STRONGER than previously recognized:

At lambda = 25, the O(3) hedgehog defect's angular gradient energy (eta^2 f^2/r^2) alone provides Sigma/M = 0.83, giving f(R_eq) = +0.50 on a fixed Schwarzschild background. This is metric positivity WITHOUT any source amplification — a cleaner and more robust result than the D7-dependent claim.

---

*This corrigendum is part of the GRUT program's commitment to adversarial self-audit and honest correction. The discovery and correction of the D7/D8 sign error is documented as part of the program's scientific record.*
