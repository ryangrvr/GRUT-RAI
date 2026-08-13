# R1 — the answer calc: does the action assign the interior modulus a value?

*Code: `calc/anomaly_c0_map.py` (pure stdlib; every load-bearing quadratic form computed in exact rationals at four independent 4-momenta with fit + held-out verification, zero residual; **mutation-tested** — five mutants including "x := α²" and a corrupted C² row are all caught). Provenance: built to the spec of the 2026-08-03 four-route derivation reconnaissance, then **rebuilt after its own firewall went AMBER on eight blockers** (see the amendment record below). **Ledger delta 0; no tier field touched. Nothing applied to the register.***

---

## The verdict: **NO PIN** — `result_face = k-dependent form factor`

$$x_\text{anom}(k) = \frac{1}{3\alpha}\cdot\frac{k^2}{k^2 + M_\sigma^2}, \qquad M_\sigma^2 = \frac{M_P^2}{12\,c_R^\text{tot}}$$

**x_anom(k→0) = 0 exactly and scheme-immunely — *in flat space*.** The curved-background limit is **HALTED**, not claimed zero (two independent in-house power counts of the FRW correction disagree on its k-structure, so the honest output is the halt).

The 1/(3α) is explicit: the form factor equals x — and "saturates at exactly 1" — **only at α = 1/3**. That is the T-BRANS-DICKE numerical collision the calc names as a trap, not a confirmation of the endpoint; and the saturation regime sits at or above M_P, where the derivative expansion producing the R² has already broken down. On the calc's **own computed sign** (c_R^anom < 0 structurally, since N > 0), M_σ² is **tachyonic** and the form factor does not rise to 1 at all — it is negative for every sub-Planckian k.

## Magnitude — the two statements are not interchangeable

- **The anomaly's own contribution** over the cosmological band is **≥108 decades below every banked bound** (computed: |x| ≈ 10⁻¹²³ … 10⁻¹¹¹, i.e. ~111 decades below EDGE = 0.594 at the worst point).
- **The scheme piece is free and unbounded.** With c_R free the form factor *can* reach the window — x = EDGE needs c_R ≈ 7×10¹¹⁰, x = the TT-auto gate needs ≈1.7×10¹⁰⁹, x = α² needs ≈6.2×10¹⁰⁹ — i.e. ordinary f(R)-dark-energy Compton-wavelength territory, which DESI actually constrains. **That freedom *is* the no-pin finding.** "R1 cannot reach the window" would contradict the scheme scan and is **not** claimed.

## The computed structure table (every row now computed — this was the firewall's first blocker)

| quadratic form | exact decomposition (k-independent after dividing by k²/k⁴) | consequence |
|---|---|---|
| −h·G⁽¹⁾ (linearized EH) | k²[ **−½** P2, 0 P1, **1** P0s, 0, 0 ] | **GR lock** P0s/P2 = **−2** exactly — reproduces the banked (1/2)k²[P⁽²⁾−2P⁽⁰ˢ⁾] |
| (R⁽¹⁾)² (∫R²) | k⁴[ **0** P2, 0, **3** P0s, 0, 0 ] | pure spin-0 |
| Riem² | k⁴[ 1, 0, **1**, 0, 0 ] | reaches P0s — at k⁴ |
| Ric² | k⁴[ ¼, 0, **1**, 0, 0 ] | reaches P0s — at k⁴ |
| ∫E₄ (a-anomaly) | **identically zero in every structure** | genuine cancellation: P2: 1−4(¼)+0 = 0; P0s: 1−4(1)+3 = 0 (**topological in d=4**, not O(h) counting) |
| ∫C² (c-anomaly) | k⁴[ **½** P2, 0, **0** P0s, 0, 0 ] | **no spin-0 carrier** |
| (tr h)² (naive vertex) | [ 0, 0, **3** P0s, **1** P0w, **2** MIX ] | **Ward-violating** — not the induced kernel |

Ward holds throughout the diff-invariant rows (P1 = P0w = MIX = 0; the vanishing of the P0s↔P0w transfer term *is* the Ward statement). The σ vertex h = 2ση has P2 = P1 = 0 identically — the α→TT back-door is kinematically shut — though the calc now states that this guard alone is **weak** (blind to an index-raising bug; only the generic-h decomposition catches that).

## Scope split (the firewall's B4 — the conditional is now enforced, not merely listed)

- **(A) Local, ≤4-derivative, flat space — UNCONDITIONAL and carrier-agnostic.** The enumeration {∫√g, ∫R, ∫R², ∫E₄, ∫C²} is complete for local ≤4-derivative diff invariants and does not use rung9a's IF. **Every operator reaching P0s does so at k⁴** (Riem² and Ric² reach it too — "only ∫R² reaches P0s" would be false). ∫R *is* the EH k² term; ∫√g is tadpole-locked. No local ≤4-derivative operator supplies a k-independent dial.
- **(B) Nonlocal closure — CONDITIONAL on rung9a's IF** (the conformal mode is the IR carrier), since R1's object *is* the Riegert conformalon. The concrete gap is ∫R □⁻¹ R, whose quadratic form ~k² P0s is degenerate in k-scaling with EH — exactly the constant dial. It is closed **by dimensions**: that coefficient carries mass², which a dimensionless anomaly coefficient cannot supply.
- **(C) Curved background — HALTED** (KC-FRONTIER-TRESPASS). No in-house number is quoted; dispatch optionality routes to X_FLOOR_MAP's independent pre-registration ("D3 requires no dispatch"), not to an estimate of the halted sector.

## The α-power audit — both halves now rest on computed rows

b′ (a-anomaly) enters only through the □R vertex → R² → P0s; b (c-anomaly) enters through ∫C² → **P2 only** (P0s = 0, computed). Scoped: this is the statement about the *local* C² counterterm (and the nonlocal C ln□ C sharing its P2 structure); the WZ vertex bσC² is O(σh²) — cubic, contributing nothing to the tree-level two-point kernel. Therefore **α = a/c is the coefficient of nothing** here: net dynamical α-power = 0, an *output*. **x = α² is structurally unreachable** on this topology, and the calc's directional guard asserts x_anom never lands near α or α² anywhere in the physical band.

## Two proposed register edits (both flagged, neither applied)

1. **To `rung9b_bridge` (settled-negative, FROZEN) — the heavier one.** Its PRIMARY obstruction is projector orthogonality ("trace = spin-0, TT = spin-2"). The computed a/c sector-split **refines rather than refutes** it: the anomaly has *both* carriers — b′ → P0s and b → P2, both at k⁴ — so the coarse form is too blunt; what actually blocks the bridge is that **the ratio a/c is the coefficient of neither**. This is a *strengthening* of rung9b, now computed. Overseer's call.
2. **To `eft_operator_basis` finding (iv).** Its second clause, "the anomaly leaves TT unaffected", is **false at two-point level** (∫C² is pure P2). The **one-point clause stands** (⟨T^μ_μ⟩ is spin-0). Correct reason it transports nothing into c₂ (the earlier reason was a non sequitur): what reaches P2 is **b alone, never the ratio a/c**, so the rung9b bridge object is untouched — and the C² structure is k⁴, not the k² of the response kernel.

**The R1/rung3 boundary (argued-grade, deliberately weakened):** no non-analytic DC spin-0 structure arises in this local/flat sector; a scheme-immune normalization would need one, and the dimensional argument says it needs a **mass²** — which massive matter supplies and a dimensionless anomaly coefficient cannot. That points at rung3's Π₀. The calc does **not** adjudicate its own bankability, and the earlier "provably not the anomaly" is withdrawn: the anomaly *does* carry non-analytic structure (C² ln□ C²) — in the P2 channel, which is why it cannot help here.

**A new blocker on the u5 deliverable:** X_FLOOR_MAP homed the x ≥ 0 orientation lemma's fence on R1's sign. R1's sign is degenerate with the free counterterm (the flip is now straddled explicitly in the scan), so **R1 declines to supply it** — and the stronger finding for the overseer is that the fence appears to have been **mis-homed**: R1's sign is the sign of a quantity ~10⁻¹¹⁴, which could not orient the family's physical dial even had it come out definite. Re-home or unbank.

**Channel fence (cross-channel comparison, flagged):** quasi-static f(R) gives **Σ = 1 identically** and η = (1+2κ)/(1+4κ), while the family postulates η = 1/μ and Σ = 1 + xα/2. The anomaly-induced R² is therefore a **Σ-null modification — not a member of the banked interior family** but a different point in (μ,η,Σ) space. Since EDGE is a DESI Σ₀ *lensing* bound, that bound has zero grip on this modification. Immaterial to the verdict (≥108 decades survives any O(1) mismatch), but the magnitude comparison is cross-channel and is now guarded in code.

## Amendment record — what the firewall caught, and what changed

The first build passed its own selftest while its two most load-bearing facts (∫C², ∫E₄) lived in **print statements**, and a mutation test showed the selftest would still pass with the answer replaced by **x = α²** — the single outcome the pre-registered directional guard declares must be an error. The physics survived a fourth independent implementation; the *artifact* did not. Fixed: **B1/B2** — linearized Riemann/Ricci added; C², E₄, Riem², Ric², (tr h)² all computed and routed through the same `decompose()`; **B3** — `x_anom(k, c_R)` now exists as a function, the DC zero is computed across the whole scheme scan, and the selftest catches all five mutants (sign-flip+inflate, constant-x-at-α², corrupted C² row, dropped k²-scaling, corrupted E₄ row); the old "two independent derivations agree" tautology is replaced by a **real** kernel-ratio-vs-f(R) cross-check at four (k, c_R) points spanning both signs — which immediately caught an algebra error of mine in the f(R) growth form; **B4** — the scope split above; **B5** — the scheme scan's sign/magnitude bug fixed and the sign flip now straddled; **B6** — the window claim re-scoped; **B7** — the channel guard added; **B8** — the rung9b proposal foregrounded and correctly worded. Tightenings T1–T21 applied (flat-space qualifier, 1/(3α) explicit, tachyonic-branch statement, E₄'s correct topological reason, the k⁴ phrasing, the corrected naive-vertex arithmetic 3 P0s (not 2), rider quoted in full rather than "verbatim"-paraphrased, partial-predicate-match stated, numeric self-consistency, halt not crossed, guards armed on physical bands, momentum-coverage fence, dead code removed).

## Routing and banking status

Fires X_FLOOR_MAP's partial-pin rider (**partial predicate match**, stated as such: the rider was pre-registered for "x_anom = 0 scheme-immune"; the actual return is a form factor with a scheme-immune DC zero but scheme-dependent amplitude and sign — both route to the same weaker consequence, **no tier change**). Both **D3** predicates fired. **Explicit non-claims:** does not establish Π₀ = 0; does not fire D1; no claim that x = 0 is forced or that p_tt is vindicated.

**HELD at FLAG** pending overseer verification. Nothing propagates to `claims.json`.
