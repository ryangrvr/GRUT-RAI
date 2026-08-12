# Frontier #3 — the L₀→0 redundancy (in-house attempt + verdict)

*The one genuinely open derivation of the four ToE frontiers, posed and attempted in-house. Scope, stated up front and held throughout: a **foundational theorem, not a ToE-completion** — even if proven it derives no new physics, predicts no observable, fixes no constant. Default-BROKEN: the win is the honest verdict, not a forced proof. Code: `calc/L0_redundancy.py`. Register: `l0_r1_redundancy_exists` (shown-generic), `l0_r2_exact_unique_breaker` / `l0_r3_payoff_mu_linear` (to-derive, default-BROKEN).*

---

## The claim

In the memoryless limit (L₀→0), the adiabatic spatial dilatation is an exact, unbroken redundancy of the full CTP (Schwinger–Keldysh) influence action S_IF; memory (L₀≠0) is the **unique** parameter that breaks it, and is therefore the **only** source of physical structure.

## Decomposition

- **R1 — the redundancy exists (generic).** The long-wavelength adiabatic dilatation is a residual large-gauge redundancy generating the adiabatic mode (Weinberg 2003; Maldacena consistency relation; Hinterbichler–Hui–Khoury Ward identities). **Standard physics — `shown`, flagged not-uniquely-GRUT** (it names neither S_IF nor L₀).
- **R2 — the crux (GRUT-specific).** From S_IF: (i) exact at L₀→0? (ii) L₀ the unique breaker? (iii) is the adiabatic mode **derived** from the action, or **presupposed**?
- **R3 — the payoff.** Does R2 graduate `mu_linear` (turn its presupposed adiabatic-dilatation bridge into a derived one) and make "memory = structure-creator" a clean theorem?

## The in-house attempt (R2)

`calc/L0_redundancy.py` works a checkable toy: one mode of a single-pole influence kernel,
K_R(ω; L₀) = −iω / (1 − iωL₀), with the **dilatation-breaking density** B(ω) = (ω d/dω − 1) K_R(ω). B ≡ 0 ⇔ the dilatation ω→sω (with the matching field weight) is an exact redundancy.

**(i) Exactness at L₀→0 — HOLDS (in the toy).** Analytically B = ω²L₀ / (1 − iωL₀)² = **O(L₀)**, confirmed numerically (|B|/L₀ → 1 as L₀→0; B ≡ 0 at L₀=0). The memoryless limit restores the redundancy **exactly**, broken at leading order O(L₀). This part is real.

**(ii) L₀ the unique breaker — FAILS as stated.** Set memory off (L₀ = 0 exactly) and turn on a trace/conformal anomaly — a **log-running coupling** K^anom ≈ −iω·b·log(ω/μ), standing in for `rung9a`'s α: its dilatation-breaking density is B^anom = (ω∂_ω−1)K^anom = **−i·b·ω ≠ 0** (the *logarithm* is the genuine breaker; a bare −ibω term would be degree-1 and give B=0). The anomaly breaks dilatation invariance **independently of memory**. So L₀ is *not* the unique breaker — it is unique only in the anomaly-free/classical sector. **"Memory is the *only* source of structure" directly contradicts GRUT's own `rung9a`** (the trace anomaly is a second, already-banked structure-source).

**(iii) Derived or presupposed — PRESUPPOSED.** The dilatation generator (ω d/dω) and the field weight are **inputs** to the calculation. Nothing derives the adiabatic mode or its weight *from* K_R; they are assumed — the Weinberg adiabatic-mode construction, inherited from the **assumed background diffeomorphism invariance**. This is the **relocation trap** (the arrow-of-time pattern; already flagged by the `mu_linear` pre-screen): a "proof" that assumes the mode has relocated the input, not derived the redundancy.

## Verdict (default-BROKEN, honest)

**R2 dissolves to: the redundancy is *exact* in the memoryless limit, but it rests on a *presupposed* input (the adiabatic mode) and L₀ is *not strictly unique* (the anomaly co-breaks).** That is itself a result — the honest one the discipline is built to produce: **the foundation rests on a named irreducible input** (the adiabatic mode / background diff-invariance), and memory is the **leading classical-IR structure-source, not the only one.**

**R3:** R2 does **not** cleanly graduate `mu_linear` — it *relocates* the adiabatic-dilatation bridge `mu_linear` needs rather than deriving it, so `mu_linear` stays a **no-go export**. "Memory = structure-creator" holds only in the weaker, conditional form, not as a clean theorem.

## Independent firewall (2026-06-29) — DISSOLVES, both directions clean

An independent both-directions screen (attempt-the-proof / refute / over-claim) **confirmed the verdict and sharpened it** — no manufactured proof, no over-dismissal:

- **Leg (i) strengthened from toy to a general theorem.** The attempt agent generalized: for *any* analytic causal kernel K_R = −iω·f(iωL₀) with f(0)=1, the dilatation-breaking density is **B = ω²L₀·f′(iωL₀) = O(L₀)** exactly — confirmed across single-pole, exponential, and cubic-pole memories. The single pole was not special; the exact-at-L₀→0 result is generic over analytic memories. *But* it coincides with R1's standard soft theorem and confers no GRUT-specific falsifiable content.
- **A legitimate steelman on (ii):** in the classical (b=0) sector, B≡0 for all ω ⟺ f′≡0 ⟺ no memory term — so L₀ *is* the unique **classical** breaker. This is consistent with the register (the anomaly is the separately-banked `rung9a`) but weakens "memory = the *only* structure-source" to "the only *classical* one."
- **The decisive (iii), honestly adjudicated:** a real pro-derivation point survives — among {translation, dilatation, special-conformal} acting on S_IF's *own* argument ω, only the dilatation D = ω d/dω gives a *constant* field weight, so S_IF genuinely singles out dilatation-of-its-own-argument and reads the weight off the kernel's homogeneity (not freely inserted). **But** K_R(ω) carries no information that frequency-dilatation ω→sω *is* the **spatial** adiabatic dilatation x→e^λx; that ω↔x identification is the imported separate-universe/Weinberg map. The assumption is **relocated** (from "the adiabatic mode" to "the ω↔x map"), not discharged.

**Ceiling, even with a specialist:** the most a full de Sitter calculation could reach is "unique-*classical*-breaker + derived-mode" — **never** the strong "L₀ is the unique breaker / memory is the only structure-source" claim, because `rung9a`'s anomaly stands. **Next step: FRONTIER-RESERVED (specialist), not in-house** — the frequency-space density B(ω) has exhausted what it can settle; (iii) requires the full S_IF dilatation variation on de Sitter *plus* a from-the-action derivation of the ω↔x map. Do not re-attempt in-house.

## Scope and honesty

- **Foundational theorem, not novel physics.** Even the part that holds (exact at L₀→0) predicts nothing and fixes no constant. Do not let it inflate into "reclaims the ToE."
- **Toy, not the full proof.** One mode, single pole, frequency space. A real proof would need the full S_IF dilatation variation on de Sitter *and* a from-the-action derivation of the mode — **frontier, specialist territory** if it is to be pushed past the in-house attempt.
- **Banked at honest tiers**, ledger 0 each: R1 `shown`-generic, R2/R3 `to-derive` default-BROKEN. The resident FLAGs all three at proposal time; `validate.py` GREEN at net **+12** (posing open questions adds no physics input). Relayed for the independent both-directions firewall before anything graduates above `to-derive`.

## Reproducibility
```
python3 calc/L0_redundancy.py     # the dilatation-breaking density B(ω) vs L₀ and the anomaly
```
Pure stdlib; runs in well under a second.
