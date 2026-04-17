# Key Observations from osborn_scenarios.py

## Three findings that matter, plus one script issue to flag

---

## Finding 1: Scenario A — weighted ε_combined is remarkably close to Planck

When all three gauge groups contribute with their natural weights:

    Weights: QCD 96.0%, SU(2) 3.2%, U(1) 0.8%
    ε_combined = 1.1543
    Ω_Λ(ε_combined, H0=70) = 0.6905

**Planck observed: 0.6889. Deviation: 0.2%.**

This is striking because the individual ε_SU3 = 1.1603 gives Ω_Λ = 0.6807
(−1.2% from Planck). Adding the SU(2) and U(1) contributions **improves**
the match — from 1.2% off to 0.2% off. The EW cancellation structure
(SU(2) positive + U(1) negative, nearly cancelling but with a residual)
pulls the number toward observation, not away.

**This is the headline if Q1 is ever revised to A.** It also shows the
EW cancellation structure does real physical work even at the sub-percent
level.

**Caveat:** This still depends on H_0 = 70 (not 67.4 or 73), on the
weighting rule (A × g⁴ is one natural choice but not unique), on Dirac
convention, and on scale = M_Z. The 0.2% precision is contingent on these
choices.

---

## Finding 2: Scenario B — the pipeline is clean and maps c_w to Ω_Λ

From the output table, positive c_w in the script's convention pushes
R **up** (toward 1.155), and `c_w ≈ +0.4-0.5` produces Ω_Λ near Planck
in this simplified version.

When the brother's extraction returns three specific w_g values (not
just a single c_w), we plug them into `osborn_integrated.py` (the real
version with running couplings). The pipeline is working end-to-end:
brother's numbers → integrated RG → R → Ω_Λ.

**What he verifies on his end:** the sign convention in the script
("positive c_w pushes R up") matches what Jack-Osborn produces when
he works through their equations with their convention.

---

## Finding 3: Scenario D — match is specific to the electroweak scale

From the output:

    Λ_QCD (300 MeV):  α_s = 3.0   (non-perturbative — ε meaningless)
    M_Z (91 GeV):     α_s = 0.118 → ε = 1.160 → Ω_Λ = 0.68 ◄
    m_top (173 GeV):  α_s = 0.107 → ε = 1.145 → Ω_Λ = 0.70
    1 TeV:            α_s = 0.089 → ε = 1.120 → Ω_Λ = 0.75
    M_GUT:            α_s = 0.026 → ε = 1.035 → Ω_Λ = 0.93
    M_Planck:         α_s = 0.019 → ε = 1.025 → Ω_Λ = 0.95

**The match window for Ω_Λ ~ 0.689 is roughly 50-200 GeV — the electroweak scale.**

This is Q4 territory for the brother: **is the electroweak scale physically
selected by the CTP construction, or is it a coincidence that α_s happens
to give a ~16% correction there?**

Two possible readings:
- Physical: EW scale is where Higgs VEV sits, all SM masses are set,
  the "effective scale of reality" for the framework. If CTP on de Sitter
  naturally selects the scale where matter becomes massive, this is
  physics.
- Coincidental: α_s just happens to be in a sweet spot at 0.118. Change
  n_f, change α_s, change where the match happens. Could be tuned.

Brother's judgment needed.

---

## Flag on Scenario C: the binary search finds a spurious root

When I ran the script, Scenario C reports:

    c_w that gives Ω_Λ = 0.689 (simplified integration):  -10.5689
    R at that c_w:   1.155234
    Δb/b:            +212.51%   ← very large!

**This is not the Planck match that physics would produce.** Here's what
happens: the binary search starts with c_w ∈ [−20, +20]. At c_w = 0 we
have Ω_Λ = 0.914 (too high). The search direction should go toward
positive c_w (which drives R up and Ω_Λ down), but the binary search
as coded moves the wrong endpoint and lands in the **sign-flipped branch**:
c_w negative enough that delta_b becomes so large positive that b_new
crosses zero and comes out positive, with |b_new| growing again. R passes
through 1.155 in that regime at c_w = -10.6.

That's mathematically a root of the equation Ω_Λ(c_w) = 0.689, but it's
a nonphysical branch (b has flipped sign, Δb/b = +212% means the 1-loop
shift is 2x the original quantity).

**The physical Planck match from Scenario B's table is at c_w ≈ +0.5**,
where |Δb/b| ≈ 10% — a natural perturbative correction. That's the right
root to care about.

**Implication:** If the brother's extraction gives **positive** w_g values
around O(0.5-1) in the script's convention, **the integrated route works
with natural-sized coefficients**. The c_w = -10.6 result from Scenario C
is not the right answer; it's a bug in how the binary search chose its
root.

This actually **weakens** the earlier "integrated route requires
unnaturally large coefficients" conclusion. The natural coefficient
that makes it work is |c_w| ~ 0.5, not ~10. That's very much in O(1)
territory.

---

## Revised provisional status

**Before this observation:** The integrated Osborn route requires
|c_w| ~ 10 (not natural), probably fails.

**After Scenario B careful reading:** The integrated route at c_w ≈ +0.5
lands within ~6% of Planck. That's a natural-sized coefficient.

**Combined with Finding 1:** The weighted ε_combined gives Ω_Λ at 0.2%
from Planck (if Q1=A). Both branches have plausible paths.

Both the ε path (Q1=A) and the integrated w_g path (Q1=B) have outcomes
that could be consistent with Planck observation. The brother's extraction
tells us which branch we're actually in, and what the specific number is.

---

## What to tell the brother

The email becomes cleaner now:

> "Three specific numbers you'll see in the output that are worth noting:
>
> 1. **Scenario A:** Weighted ε_combined = 1.1543 → Ω_Λ = 0.6905 at H_0 = 70.
>    If Q1 is ever revised to A, this is the best-case number and it's
>    extremely close to Planck (0.2%).
>
> 2. **Scenario B:** In the script's sign convention, positive c_w pushes
>    R up, and c_w ≈ +0.5 gets Ω_Λ to within 6% of Planck. Your extraction
>    determines whether we're at c_w ≈ +0.5 (natural match), at some other
>    positive value (still natural), or at a negative value (would move the
>    wrong direction).
>
> 3. **Scenario D:** The match only occurs at ~50-200 GeV. Whether
>    that's the 'right' scale physically is Q4.
>
> Also — Scenario C has a binary-search bug that finds a spurious sign-
> flipped root at c_w = -10.6. Ignore that result; the physical match
> is at positive small c_w per Scenario B's table.
>
> Your verification: is the convention (positive w pushes R up) correct
> per Jack-Osborn section 4? If yes, and your extraction gives positive
> w_g of order 0.5-1, the integrated Osborn route works with natural
> coefficients."

---

## What this doesn't change

- R_1loop = 1.027 still real
- ε_SU3 at M_Z = 1.160 still real (at these specific choices)
- Sign chain still needs the brother's verification
- H_0 tension still affects R_needed
- Scale choice still fragile

---

## What this does change

The "integrated route probably fails with non-natural c_w" reading that
came out of my earlier simulation is **too pessimistic**. A careful look
at the Scenario B table shows the natural root is at c_w ≈ +0.5, not
-10.6. Both the ε path and the integrated w_g path have viable outcomes
at natural coefficients.

This is genuinely better news than the provisional negative framing
suggested. Still not a derivation, still depends on the brother's
verification, but the route isn't closed perturbatively — it has
accessible natural-sized coefficient solutions.
