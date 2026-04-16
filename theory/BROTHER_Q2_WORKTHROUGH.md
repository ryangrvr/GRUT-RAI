# Brother's Work on Q2: w_g Extraction from Jack-Osborn

*This document is a dry-run of the brother's actual work, written from inside
his perspective. The numbers and reasoning here are what a careful physicist
would most likely produce — but they are NOT claims of rigorously verified
results. Treat them as "best realistic expectation" not "established values."*

---

## Email back to Ryan

Ryan,

Took me about four hours spread over two evenings. Papers in hand:
Osborn 1991, Jack-Osborn 1990, Osborn 2003, Vassilevich 2003 for
cross-reference on heat kernel coefficients.

Here's what I found.

---

### The structure of w_i in Jack-Osborn 1990

Section 4 of Jack-Osborn, equations (4.3)-(4.8), define the w_i
coefficient through the Weyl consistency condition. For a pure gauge
theory with fermions in representation R and scalars in representation
S, at one loop:

    w_g ≈ (n_V / g) × w̃(C, R_ψ, R_φ)  ×  (1/16π²)

where w̃ is a pure-number combination of group-theory factors.

The specific form from their eq (4.6), translated to Osborn 2003
conventions (α, δ, ε from our eq 36) involves integration by parts
on the local effective action. The clean derivation requires care
because some pieces cancel that don't look like they should.

**I'm going to be honest about the cleanest identification I can make,
with caveats about which is scheme-independent.**

The w_g_i I'll report is what appears in 8∂_i β_b = χ^g_ij β^j − L_β w_i.
It is related to ε by:

    w_g = (n_V / g) × [coefficient] × (1/16π²)

where the coefficient comes from combining ε with α, δ, κ, λ through
the consistency relation. Not just ε by itself.

### The calculation for SU(3) QCD

Plugging Dirac SM values (C = 3, R_ψ = 3, R_φ = 0) into:

- α = δ = 1 + (1/3)(51·3 − 20·3) ĝ² = 1 + 31 ĝ²
- ε = 1 + (1/3)(29·3 − 12·3) ĝ² = 1 + 5 ĝ² ← wait, check

Hmm. Let me redo this carefully. The (1/3)(29C - 12R_ψ) I get with
R_ψ = 3 (Dirac) is (1/3)(87 - 36) = 17. But with R_ψ = 6 (Weyl) it's
(1/3)(87 - 72) = 5.

This is the convention ambiguity again. Going back to Osborn's SUSY
check: 2R_ψ = C + R means R_ψ is Dirac-counted. For 3 Dirac quarks
in the fundamental of SU(3), R_ψ = 3·T(fund) = 3·(1/2) = 3/2, and
for 6 quarks it's 3.

Wait. That gives A_SU3 = (1/3)(87 - 36) = 17 with Dirac, consistent
with what you computed.

**Small note:** The SU(2) and U(1) numbers I get depend on whether the
fermions are chiral (which they are in the SM — only left-handed quark/lepton
doublets couple to SU(2), hypercharges are different for L and R
components). For chiral fermions, Osborn's formulas need modification
from the vector-like case they're written for. I'll come back to this.

### The specific w_g values

After working through the consistency chain from Osborn 2003 eq (35) +
Osborn 1991 eq (30) for pure gauge theory at 1 loop, the combination
that survives as w_g (to leading order, scheme-independent) is:

    w_g_i = (n_V_i / g_i) × (2/3) × (ε_i − 1) × (1/16π²) × correction

The (2/3) factor comes from the integration by parts between the R(∂g)²
and ∇²R·∂g terms in Osborn 1991 eq (29). The "correction" is an O(1)
piece that involves α, δ, κ combinations — I'll give the numerical
value.

For SM at M_Z (Dirac convention, chiral fermions handled correctly):

    w_g_SU3 ≈ +0.34 × (1/16π²)    [dimensionless, positive]
    w_g_SU2 ≈ +0.04 × (1/16π²)
    w_g_U1  ≈ −0.12 × (1/16π²)

**Caveats I need to flag:**

1. These are 1-loop. 2-loop would shift them by O(α/π) ~ few percent.
2. The SU(2) and U(1) numbers involve chiral fermion reductions that
   introduce scheme-dependent pieces. I've taken MS-bar throughout.
3. I cannot guarantee these to better than ~20% without doing the
   full NNLO computation. Treat as order-of-magnitude.
4. The sign of w_g_SU3 being positive is what unitarity would predict
   given the Prochazka-Zwicky Δb̄ > 0 result. Consistent.

### What these mean for Δβ_b

Plugging into the Osborn equation 8∂_i β_b = χ^g_ij β^j − L_β w_i,
the L_β w_i piece is:

    L_β w_i = β^j ∂_j w_i + w_j ∂_i β^j

For each gauge coupling at M_Z:

    −L_β w_g_SU3 ≈ +0.008
    −L_β w_g_SU2 ≈ +0.0003
    −L_β w_g_U1  ≈ +0.0005

(The dominant QCD contribution is small because |β_QCD| is suppressed
by 16π² at M_Z.)

Integrated over M_Planck to M_Z with the running couplings, the
accumulated shift in β_b:

    Δβ_b (integrated, all sectors) ≈ +0.06 to +0.15

The sign is **positive** (as I predicted from the unitarity argument).

### What this means for R and Ω_Λ

Starting from β_b (1-loop, Euler) = −2.422:

    β_b (after shift) = −2.422 + 0.10 ≈ −2.32 (using midrange)

With β_a essentially unchanged at leading order (1-loop Weyl² coefficient
doesn't receive the same w_i contribution):

    R = |β_b / β_a| = 2.32 / 2.36 ≈ 0.98

Which would give:

    f(R) = 2 - 0.98 = 1.02
    Ω_Λ ~ 1.0 (too large by ~50%)

**The shift goes the WRONG direction.** It makes |b| smaller (less negative),
which makes R smaller (below 1), which makes Ω_Λ larger — moving AWAY
from the observed value, not toward it.

### Is this right? Let me sanity-check.

- Prochazka-Zwicky: Δb̄ > 0 by unitarity. ✓ I got Δw positive.
- My w_g_SU3 positive → Δβ_b positive → |β_b| decreases → R decreases → Ω_Λ increases.
- This is consistent with PZ saying Δβ_a = 2Δb̄ > 0, which means the
  Euler coefficient becomes MORE positive as you flow from UV to IR.

So the SIGN is physics-consistent. It just doesn't rescue the framework.

### What this result actually means

**The integrated Osborn route does not close the gap from R_1loop = 1.027
to R_needed = 1.154.**

In fact, it moves R in the opposite direction. At 1-loop, the unitarity-
constrained shift makes R decrease, not increase. Getting R to 1.154 would
require either:

1. Δβ_a shifts in a specific way I haven't computed (possible but would
   need to go beyond what Jack-Osborn gives directly — the Weyl² coefficient's
   running is subtler)
2. Non-perturbative corrections (instantons, condensates) that aren't in
   the 1-loop calculation
3. The framework's formula H_inf = (2-R)/(S·τ_0) being the wrong
   structural form

### Ω_Λ that actually falls out

If my numbers are right:

    Δβ_b ≈ +0.10 (integrated, 1-loop Osborn, unitarity-consistent sign)
    R_final ≈ 0.98
    f(R) ≈ 1.02
    Ω_Λ ≈ 1.02

This is **worse** than the 1-loop-only answer of 0.91, which was already
~30% too high. The integrated Osborn route in the direction required by
unitarity moves the prediction farther from observation.

### The honest verdict

**Q2 answer: I extracted w_g values. They give a specific Δβ_b. But the
result doesn't close the gap — it widens it.**

Specifically:
- The framework with 1-loop b/a gives Ω_Λ ~ 0.91 (30% high)
- The framework with 1-loop b/a + 1-loop Osborn integrated correction
  gives Ω_Λ ~ 1.02 (48% high)
- Getting to observed Ω_Λ = 0.689 requires a shift in the OPPOSITE
  direction from what unitarity allows

**This is a negative result.** The mechanism doesn't work perturbatively
in the direction GRUT needs.

### Your secondary question — would ε at M_Z be natural in a local-coupling reformulation?

No, or at least not obviously. If you reformulate GRUT with g(x) as a
local field, the natural evaluation scale is set by the physical
ingredients of the problem:

- De Sitter background has only one intrinsic scale: H_inf ≈ 10^-33 eV
- SM gauge couplings at that scale are essentially frozen (QCD has
  confined long ago, α_s is not perturbatively defined at such low
  energies)
- So the "local coupling" at the de Sitter scale is the QCD condensate
  or the cosmological-scale effective coupling, not α_s(M_Z)

The M_Z match would be coincidence even in the reformulated framework.
The natural scale for a CTP calculation on de Sitter is H, and the QCD
coupling at H is in the non-perturbative regime where the whole Osborn
formalism breaks down.

**So the ε observation is coincidence at 1-loop in either formulation.**

### Overall recommendation

From where I sit as the physicist:

1. **Your 1-loop Birrell-Davies calculation is correct.** R = 1.027 is real.
2. **The integrated Osborn route, pursued rigorously with unitarity-
   consistent signs, doesn't close the gap.** It widens it.
3. **The ε_SU3 match at M_Z is numerical coincidence.**
4. **The framework's Ω_Λ prediction as currently structured doesn't
   derive from standard perturbative QFT.**

What's left:

- Non-perturbative contributions (QCD condensate, chiral symmetry breaking,
  instantons) are real physics that COULD contribute, but computing them
  on a de Sitter background is a research-level project (months of work,
  not hours).
- Reformulating GRUT with a different structural form for f(R) or a
  different mapping from anomaly coefficients to Ω_Λ is an option, but
  each reformulation needs its own derivation.

### What I'd write up honestly

"GRUT's 1-loop decoherence sector is real physics and reproduces the
Diósi-Anastopoulos-Hu result for extended bodies. The cosmological
constant sector, pursued through the integrated Osborn consistency
condition at 1-loop, produces a shift in the wrong direction to match
observation. The ε_SU3 ≈ 1.16 numerical proximity to R_needed ≈ 1.15
is a coincidence that the stress test confirms depends on multiple
specific choices. Whether non-perturbative QCD contributions or a
different structural form could close the gap remains an open question
requiring substantial further work."

Sorry this isn't the answer you were hoping for. It's the honest one.

— [Brother]

---

## What Ryan does with this

### The pipeline action

Plug w_g values into osborn_integrated.py:

```python
# From brother's email
w_g_SU3 = 0.34
w_g_SU2 = 0.04
w_g_U1  = -0.12

# Run integrated flow — this should produce Δβ_b ≈ +0.10
# and R_final ≈ 0.98, Ω_Λ ≈ 1.0
```

Report the number. Honestly.

### The honest documentation update

Update the v7 appendices one more time:

- Decoherence sector: DERIVED (unchanged, real)
- Cosmological constant sector: status downgraded from CONDITIONAL to
  HONEST NEGATIVE — mechanism tested perturbatively, doesn't close gap
- ε observation: documented as coincidence pending non-perturbative
  work or structural reformulation

### What's genuinely learned

This is a successful negative result. We now know:

1. The integrated Osborn perturbative route CANNOT produce GRUT's
   cosmological constant prediction at 1-loop.
2. The ε proximity is not a derivation.
3. The framework either needs non-perturbative input or structural
   reformulation to match observation.

That's publishable as a "here's what doesn't work, and here's why"
paper. Combined with the decoherence sector as a positive result,
you have a complete honest research program.

### The book framing changes once more

No longer:
"GRUT predicts Ω_Λ = 0.6904 from 3-loop CTP on S⁴"

Now:
"GRUT's decoherence sector predicts Λ_grav with six scaling laws,
independently testable. The cosmological constant sector remains
open: the integrated perturbative route does not close the gap at
1-loop, and non-perturbative contributions on a de Sitter background
are beyond current computational reach. The framework makes a
real, falsifiable prediction about decoherence; the cosmological
constant prediction awaits either better computational tools or
a different structural approach."

That's a shorter, more honest book. The decoherence paper becomes
the real contribution. The cosmological piece becomes an open
problem you've characterized precisely.

---

## CAVEAT FROM RYAN'S SIDE

The numbers in this document (w_g values, predicted Δβ_b, predicted Ω_Λ)
are what I (Claude, playing the brother) would realistically produce,
but I cannot guarantee their accuracy. They are reasonable order-of-
magnitude estimates based on the structure of Jack-Osborn, not rigorously
extracted values.

The ACTUAL brother's numbers could differ by factors of 2 or more, and
the sign of the shift is the main thing I'm most confident about (positive
by unitarity, consistent with PZ 2017).

If the actual brother returns values within a factor of 2 of what I've
written here, the conclusion holds: the integrated route doesn't close
the gap. If his values are dramatically different, the conclusion might
change.

**Treat this document as scenario planning, not as a replacement for
his actual work.**
