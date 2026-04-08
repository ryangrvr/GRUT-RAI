# Program M — Stage M1: RG and Scheme Invariance Test

---

## Step 1: Explicit μ-Dependence

**R(μ) = 1.154283417871962**

**dR/d(ln μ) = 0 exactly.**

Both C_Final and C_Cosmo as given in the paper are PURE NUMBERS — built from {π, ζ(3), ln(2), integers}. No μ, no scale, no running. They are the final finite parts after MS-bar pole subtraction.

The μ-dependence in the full effective action (through the ln(q²/μ²) nonlocality) splits into: C_Final × q² ln(q²) (nonlocal, μ-independent coefficient) minus C_Final × q² ln(μ²) (local R² counterterm, absorbed by the R² coupling's running). C_Final itself does not run.

**Result: R is μ-independent by construction within MS-bar.**

---

## Step 2: Regularization Scheme Sensitivity

### Transcendental decomposition

```
C_Final = [297 + 6π² + 1728 ln(2)ζ(3)] / (16384 π⁶)
           ↑rational  ↑transcendental   ↑transcendental

C_Cosmo = [−108000 + π⁴ + 1536π⁴ln(2) + 540ζ(3)] / (276480 π⁴)
           ↑rational   ↑trans  ↑trans        ↑trans
```

### The critical finding

The ratio from RATIONAL parts alone: R_rational = 212.7
The ratio from TRANSCENDENTAL parts alone: R_trans = 40.8
The full ratio: R = 1.154

**R is NOT simply a ratio of transcendental structures.** It emerges from the specific CANCELLATION between the large rational and transcendental contributions in both numerator and denominator. R = 1.154 results from:

```
C_Cosmo = −108000 + 97 + 103709 + 649 = −3545  (heavy cancellation: 104455 − 108000)
C_Final_num = 297 + 59 + 1440 = 1796            (moderate cancellation)
```

The C_Cosmo numerator involves a cancellation of ~97% between −108000 and +104455. This is a FINE CANCELLATION. Whether it is structurally protected depends on whether the rational coefficient (−108000) and the transcendental contributions (104455) transform TOGETHER under scheme changes.

### Scheme-change analysis

Under a scheme change (MS-bar → momentum subtraction):
- Scheme changes affect RATIONAL prefactors of transcendental terms
- They can also add finite RATIONAL constants

If C_Cosmo = −108000 + f(π, ζ(3), ln(2)), and a scheme change shifts −108000 → −108000 + δ, then:

```
C_Cosmo → −108000 + δ + f(...) = C_Cosmo + δ
R → |C_Cosmo + δ| / |C_Final + δ'|
```

For R to be unchanged: δ/C_Cosmo = δ'/C_Final. This is NOT guaranteed by any simple structural argument — it requires that the scheme-dependent shifts to BOTH coefficients are in the same proportion.

### The paper's argument

The paper claims: "Scheme-dependent local counterterms shift C_Final and C_Cosmo independently, but identical logarithmic dependence in the trace sector ensures exact cancellation in the ratio R."

This argument rests on the claim that BOTH coefficients inherit their scheme dependence from the SAME trace-anomaly functional, so that:

```
C_Final(scheme) = c_F × A_anomaly(scheme)
C_Cosmo(scheme) = c_C × A_anomaly(scheme)
```

where c_F, c_C are scheme-independent kinematic factors and A_anomaly is the scheme-dependent anomaly coefficient. In this case R = |c_C/c_F| is trivially scheme-independent.

**But the explicit formulas do NOT factor this way.** C_Final and C_Cosmo involve DIFFERENT transcendental combinations (C_Final has ln(2)ζ(3); C_Cosmo has π⁴ln(2) and ζ(3) separately). They cannot be written as (constant × same function).

### Verdict

**R is μ-independent (exact). R is CONDITIONALLY scheme-independent:**
- Plausible (UV-anomaly-controlled, shared diagram topologies)
- NOT proven (the explicit formulas do not factor into [kinematic × common anomaly])
- The heavy cancellation in C_Cosmo (97%) makes R potentially sensitive to rational shifts of order ~3% of the total

---

## Step 3: Field Content Sensitivity

**Decoupling (heavy fields, M >> SM):** R is STABLE. Appelquist-Carazzone ensures heavy fields decouple. C_Final and C_Cosmo reflect only light-spectrum anomaly coefficients. PASS.

**Light field addition:** R shifts. The integer coefficients (99, 108000, 576, 1536, 540) encode SM-specific field multiplicities. Adding a light scalar changes these integers → changes R. Estimated shift: ~1-2% per new scalar DOF. This is PHYSICAL and expected: R encodes the matter content.

**Verdict: DECOUPLING-CONSISTENT. R is SM-specific, not universal across all QFTs.**

---

## Step 4: IR vs UV Origin

| Component | UV or IR | Evidence |
|:---------:|:--------:|---------|
| C_Final | UV-determined | Coefficient of nonlocal R ln(□)R operator, fixed by 3-loop anomaly |
| C_Cosmo | UV-determined | Finite vacuum counterterm from 3-loop subtraction |
| R | UV-anomaly-controlled | Both components are UV-determined; ratio inherits UV protection |
| 1/k⁴ noise | IR-manifesting | Fourier transform of the ln(q²) nonlocality, dominates at k → 0 |

**R is UV-anomaly-controlled and IR-manifesting.** Its value is set by the UV structure (field content, loop diagrams) but its physical consequences appear in the IR (decoherence, cosmological constant). This is the most favorable structure for scheme independence — anomaly-determined quantities are typically protected by matching conditions.

However: the SPECIFIC COMBINATION of rational and transcendental terms that produces R = 1.154 involves a heavy cancellation that is not obviously anomaly-protected. The protection may be more fragile than the UV-anomaly classification suggests.

---

## M1 Final Output

```
1. R(μ) = 1.154283417871962
   dR/d(ln μ) = 0  (exact, no μ in expression)

2. Scheme-sensitive terms:
   C_Cosmo involves 97% cancellation between rational (−108000)
   and transcendental (+104455) parts.
   R emerges from this cancellation, not from a simple ratio
   of transcendental structures.

   Scheme changes affecting the rational part by O(1000) could
   shift R by O(1) unless structurally protected.

3. Decoupling:
   Heavy fields: STABLE (Appelquist-Carazzone). PASS.
   Light fields: R shifts ~1-2% per new DOF. PHYSICAL.

4. Origin:
   UV-anomaly-controlled, IR-manifesting.
   Most favorable structure for invariance, but the heavy
   cancellation in C_Cosmo introduces fragility.
```

### Token: **r_conditionally_scheme_independent**

R is μ-independent (exact). R is scheme-independent IF the 97% cancellation in C_Cosmo is protected by anomaly matching. This requires either:
1. A second-scheme computation yielding the same R, or
2. A structural proof that the rational coefficient (−108000) and the transcendental contributions are BOTH anomaly-determined and shift in proportion

Neither is provided. The invariance is plausible (UV-anomaly origin) but conditional (heavy cancellation not obviously protected).

---

*Program M Stage M1 complete. dR/d(ln μ) = 0 exact. Scheme independence: CONDITIONAL. Key fragility: C_Cosmo involves 97% cancellation between rational and transcendental parts. R emerges from this cancellation. Scheme changes affecting the rational coefficient could destabilize R unless anomaly-protected. Decoupling: PASS. UV origin: YES. Token: r_conditionally_scheme_independent.*
