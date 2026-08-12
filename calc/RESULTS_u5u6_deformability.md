# u5 & u6 — the deformability computation (one calc, both claims)

*The single in-house computation the u5↔u6 convergence pointed at: does the reversible-bracket partition of the surviving sector survive (sharp → real order parameter + phase structure) or collapse (deformable → rigid + info_i2-adjacent)? Code: `calc/u5u6_deformability.py`. Register: `u5_constitutive_phases` and `u6_constitutive_order` (both `to-derive`, ledger 0 — UNCHANGED). Scope: **TOY/SCALING** — symmetry + naive scaling, **not** the rigorous fixed-point RG. Default-BROKEN: the win is the honest factorization, not a resolved horn.*

---

## The claim (default-BROKEN)

The u5 surviving sector (relativistic, passive, KMS, causal viscoelastic transport) is labeled by the reversible mode-coupling / Poisson-bracket structure (u6's candidate order parameter). Whether that partition is **sharp** (distinct fixed points → real order parameter + phase structure) or **deformable** (couplings RG-irrelevant → collapse → one rigid class + info_i2-adjacent) is the deformability question — and settling it fixes the *scaling-level structure* of both u5 (count) and u6 (real order parameter iff sharp) together, graduating neither.

## The result — the question factors into two knobs

**KNOB 1 — deformability (RG-relevance at the relativistic z=1 fixed point).** *Undecided at scaling level.* Symmetry-protection is **decidable**: the Model-H bracket (OP advected by conserved momentum T^{0i}) is **symmetry-forced-present** by T_μν-conservation + Lorentz — it cannot be tuned to zero. But **presence is not relevance**: whether the present coupling *distinguishes* a fixed point (sharp) or *flows away* (deformable) is set by the anomalous dimension at the interacting fixed point. **z=1 is guaranteed only *if* the critical dynamics flows to a Lorentz-invariant fixed point** — in a thermal/KMS medium boosts are broken (a thermal state picks a rest frame), so z=1 here is a *fixed-point assumption*, not a symmetry theorem. Under z=1 the non-relativistic Hohenberg–Halperin upper-critical-dimension logic (which works by letting the mode coupling drive z off its van Hove value) does **not** transfer. KNOB 1 is a fixed-point (loop / ε-expansion) computation — **this toy does not resolve it**; it fixes only that the H-bracket is present (a necessary, not sufficient, condition for a sharp H-class).

**KNOB 2 — availability (conserved-charge content).** *Decidable — the clean core.* A reversible bracket {φ, Q} exists only if Q is a conserved charge of the vacuum. **T_μν is universal** (⇒ the H-bracket is always available *and* symmetry-forced; "universal" in the flat-space/fixed-background EFT sense the HH dictionary assumes, where T^{0i} generates translations). Every **other** bracket needs an **extra** conserved charge the pure gravitational vacuum *may or may not* carry: Model J a non-abelian internal charge, Model E/F a U(1), Model G internal + staggered. (E and F share one U(1) bracket per HH convention, so the four bracket entries cover the five labels E/F/G/H/J.) So, **given sharp**, the u5 class count = number of available brackets:

| vacuum charge content | available brackets | count (sharp) | count (deformable) |
|---|---|---|---|
| pure gravity (only T_μν) | {H} | **1** | 1 |
| + U(1) | {H, E/F} | 2 | 1 |
| + non-abelian SU(2) | {H, J} | 2 | 1 |
| + U(1)+SU(2)+staggered | {H, J, E/F, G} | 4 | 1 |

## The reduction (the scaling-level finding)

The deformability question **factors as KNOB1 × KNOB2**, and the u5 count reduces to a sharp physical question: **how many conserved charges beyond T_μν does the responsive vacuum carry?** u5 and u6 then settle **together**:
- **sharp + extra charges** → u6 order parameter **real** + u5 **phase structure** (a family);
- **deformable** → u6 **collapses** + u5 **rigid** (one class, info_i2-adjacent);
- **sharp + only-T_μν** → u6 order parameter real but **single-valued** + u5 **rigid** (count 1).

Note: for pure gravity **both horns give count 1** — the sharp/deformable split there is only whether the single class carries a real (single-valued) order parameter or a collapsed one.

## Verdict (default-BROKEN, honest; TOY/SCALING; graduates neither u5 nor u6)

**DERIVED (scaling level) — the FACTORIZATION only (graduates neither u5 nor u6; horn UNDECIDED):** the deformability question factors into KNOB 1 (RG-relevance — *undecided* at scaling, fixed-point calc; H-bracket symmetry-forced-present) × KNOB 2 (charge content — *decidable*, count a monotone function of charge content, schematically ~1 per unlocked bracket — some classes need combined structure and one charge can seed several). The whole thing reduces to the conserved-charge count. The scaling-level *structure* of u5 and u6 is fixed together; neither is graduated.

**Fences (both directions):**
- **TOY/SCALING** — symmetry + naive scaling, **not** the fixed-point (anomalous-dimension) RG that decides KNOB 1. Points the direction; does not resolve.
- **The conserved-charge content is a fenced modeling input** (rung3-channel-shaped): whether GRUT's vacuum carries a charge beyond T_μν (a conformalon current? an anomaly current?) is **not** settled here. This is a **second** rung3-shaped fenced input, **distinct** from u6's already-held coarse-graining/slow-variable conditional (the independent-definition guard's conditional pass), which remains **live and un-discharged** — the bracket enumeration here presupposes the slow variables are already chosen.
- **Both horns first-class.** Sharp ⇒ order parameter + phase structure; deformable ⇒ collapse + rigid.
- **"only T_μν ⇒ rigid" is a lean**, conditioned on the modeling input *and* on "sharp" — **not** a banked result. (The builder's lean, held loosely — the same one the survey caught on u5.)
- **u5 and u6 stay `to-derive`, ledger 0.** This derives the scaling-level *factorization*, not the horn.

## Independent firewall (2026-07-04) — both directions, amber→green after fixes

A three-lens firewall (over-claim / physics-math / consistency) ran *before* banking. Outcome: **no blockers; resolves no horn (KNOB 1 stays undecided everywhere); the "only T_μν ⇒ rigid" statement is a fenced lean not a result; the physics is sound at scaling level (the HH bracket→model→charge dictionary verified from first principles; the code faithfully gives SU(2)-alone → {H,J}); consistent with the banked u5/u6 openings; both stay to-derive/ledger 0.** Required fixes, all applied:
- **Fence under-named a condition** — the top-level "only T_μν ⇒ rigid" fence named only the charge-content input and dropped the second, more insidious one ("sharp"). Now names **both**.
- **Verb attached to u5/u6, not the factorization** — "settles both u5 and u6" reworded so the object is the *scaling-level factorization* (graduates neither); "in one stroke" dropped.
- **Standalone "DERIVED (scaling level):" header** bound inline to "the FACTORIZATION only (graduates neither; horn undecided)".
- **Re-carried u6's live coarse-graining conditional** — the new charge-content input is flagged as a *second*, distinct rung3-shaped fenced input; u6's original independent-definition conditional-pass (on the slow-variable choice) remains live and un-discharged.

Physics precision fixes (both improve honesty): **z=1 is a *fixed-point assumption*, not a symmetry theorem** in a thermal/KMS medium (boosts broken by the rest frame); and the count is a **monotone function of charge content (~1 per unlocked bracket)**, not a literal bijection — Model G needs combined structure and one SU(2) can seed both J and G (the code and table already handle this correctly; only the prose slogan was tightened). Plus: `info_i2`→`info_i2-adjacent`, burden-neutral charge wording, the E/F-as-one-pair note, and the flat-space T_μν scope note.

Independently confirmed by the physics lens: the H = T_μν-advection (symmetry-forced), J = self-precession/SU(2), E/F = U(1), G = staggered+internal dictionary is correct; pure gravity's only guaranteed conserved current is T_μν; and the both-horn logic (including pure-gravity count 1 in *both* horns, differing only in real-single-valued vs collapsed order parameter) is sound. Self-test passes.
