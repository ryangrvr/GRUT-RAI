# Q3: Literature Search for an ε-to-b/a Identity

## The question
Is there a published identity, theorem, or known relation between:
- **ε**: coefficient of R·∂_μg·∂^μg in the local-coupling 1-loop effective action (Osborn 2003 eq 36)
- **b/a**: ratio of Euler to Weyl² coefficients in the constant-coupling trace anomaly (Birrell-Davies)

## Search scope

Papers searched / consulted:
- Osborn 2003 (hep-th/0302119) — original ε formulas
- Osborn 1991 (NPB 363) — consistency conditions
- Jack-Osborn 1990 (NPB 343) — original w_i framework
- Jack-Osborn 2014 (arXiv:1312.0428) — gradient flow for β-functions
- Komargodski-Schwimmer 2011 (arXiv:1107.3987) — a-theorem
- Prochazka-Zwicky 2017 (arXiv:1703.01239) — Δb̄ flow
- Cordova-Freed-Lam-Seiberg 2019 (arXiv:1905.09315, 1905.13361) — anomalies in coupling space
- Functional and Local RG review (arXiv:1502.02439)

## What the literature DOES establish

1. **The a-theorem (Komargodski-Schwimmer 2011).** The Euler coefficient
   (our b) decreases monotonically from UV to IR: β^i ∂_i a ≤ 0.
   This is about b, not about the ratio b/a.

2. **ε is part of the Zamolodchikov-Osborn metric χ_ij** (Osborn 1991).
   It enters the consistency conditions as one of several anomaly
   coefficients (χ^e_i, χ^f_ij, w_i, Y_i, etc.), not as a direct
   map to b/a.

3. **At a CFT fixed point (β=0), all these quantities become constants**
   specific to the CFT. a and b (central charges) are fixed, ε takes
   some value, but there's no universal relation ε = f(a,b) across all
   CFTs.

4. **In large-N or SUSY limits**, various coefficients collapse.
   Osborn 2003 itself shows this explicitly for N=1 and N=2 SUSY
   (eqs 37-38) — but these produce relations within the (α,δ,ε,κ,λ)
   set, not between ε and b/a.

5. **Prochazka-Zwicky 2017** gives Δb̄ (BoxR coefficient change) and
   claims Δβ_a = 2Δb̄ at CBZ-FP to sixth order in κ. This is a
   relation between b-flow and b̄-flow, not between ε and b/a.

## What the literature DOES NOT establish (as far as my search shows)

- **No direct identity ε = f(a, b)** in general.
- **No reduction of ε to b/a** in any specific limit that's clearly documented.
- **No theorem connecting the local-coupling and constant-coupling sectors**
  in the specific way that would justify "R = ε_SU3" for the cosmological formula.

## Caveats about my search

1. I searched English-language published literature accessible through web
   fetch. There could be:
   - Results in specialized Russian-school references (e.g., Vilkovisky
     school beyond what I accessed)
   - Review chapters in quantum gravity books I don't have
   - Recent papers I didn't find in my keyword searches
2. The question might be folklore rather than explicitly published.
   A practitioner like the brother might know the answer from experience
   without a paper reference.

## My best answer to Q3

**Q3 = C** (no clear known identity, at the level of my search).

This means: if ε = R is going to work, it's either:

- A **new result** (Q3 = B: derivable but not published, worth co-authoring)
- Or **structurally specific to the CTP formulation** (Q3 = B via CTP
  argument rather than general QFT identity)
- Or a **0.46% coincidence** (Q3 = C, pending further work)

## Implication for the decision tree

The brother's answer on Q3 is likely to be:

- **Most probable:** C (no known general identity)
- **Possible:** A (if he knows a specific result I missed)
- **Best outcome:** B (if the CTP structure provides a derivation that
  hasn't been published because nobody's looked at this specific question)

**If Q3 = B in the CTP direction**, then Q1 (does CTP select ε over b/a)
is the key question, and the answer comes from the CTP formalism, not
from general QFT identities.

The literature search doesn't settle the question, but it does narrow it:
**any ε = R justification will have to come from CTP-specific arguments,
not from a general Weyl-anomaly theorem.** That's a useful narrowing.

## What this means practically

If the brother returns Q3 = C, the 0.46% proximity is either:
1. A coincidence we document as such
2. A clue pointing at CTP-specific structure we haven't formalized
3. A new result waiting to be derived

None of these require us to abandon or embrace the proximity. We just
label it accurately: promising, not derived, pending specific further work.

## References

- Osborn 2003: https://arxiv.org/abs/hep-th/0302119
- Osborn 1991: https://www.damtp.cam.ac.uk/user/ho10/loc.pdf
- Jack-Osborn 2014: https://arxiv.org/abs/1312.0428
- Komargodski-Schwimmer 2011: https://arxiv.org/abs/1107.3987
- Prochazka-Zwicky 2017: https://arxiv.org/abs/1703.01239
- Cordova et al 2019: https://arxiv.org/abs/1905.09315
- Functional and Local RG: https://arxiv.org/abs/1502.02439
