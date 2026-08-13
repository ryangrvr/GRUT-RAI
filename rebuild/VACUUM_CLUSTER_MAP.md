# The vacuum cluster — a map, not a solution

*The first application of this register's discipline to physics at large rather than to the framework that built it. **Scope fence, hard: this is a MAP.** The question is not "what solves the cosmological-constant problem" — it is **how many independent underived inputs is this cluster, and do any share a root.** Any line that starts proposing a resolution has drifted.*

**Status: BANKED under its own scope (2026-08-04).** 13 nodes at `ledger_scope: vacuum-cluster`, audited by `provenance/validate_scoped.py` under the ruled physics vocabulary (six tiers, four mandatory riders). **GRUT's ledger is untouched at +13** and the cluster's own ledger is 0 — the two vocabularies cannot bleed (verified by execution: a `measured` node passes its own gate and is *rejected* by GRUT's). GRUT was excluded as a lens throughout (KC5); its relation is a single node drawn **last**, marked **decorative**, carrying **zero credit** in the inventory.

**Provenance:** a six-agent mapping wave + adjudicator (pre-registered kill-conditions, default-broken toward INDEPENDENT), then a three-lens adversarial firewall + adjudicator that re-ran every load-bearing computation in sympy. **The firewall came back AMBER and broke two of the three legs of the main proof.** What follows is the post-firewall state, which is weaker and more useful than what preceded it.

---

## Ruling 1 — Independence: **independent under the repaired criterion, with one merge candidate seen and refused**

> **The top line, stated so a reader who stops here gets the claim the analysis supports.** Throughout this document, **"independent" means exactly one thing: *no merge reduces the underived-input count*.** That is a ledger fact, not a claim about problem-identity, and the two are not the same statement.
>
> Under the repaired criterion (`provenance/merge_criterion.py` **v2**, frozen 2026-08-04 with hashes recorded *externally* in `FROZEN_MERGE.txt`; six merge classes, n-sided, **vector verdict**): **no reduction is available.** The strongest candidate — Banks-type cosmological SUSY breaking — scores **TRADE: −1 real parameter, +1 posit.** It is **not refuted**: it buys the weak scale's independence at the price of a relation nobody derives. So the honest claim is *independence under the reading that declines that trade* — weaker than "proven", and weaker than v1's "seen and refused".

**L (the vacuum-energy input) and H (the electroweak-hierarchy input) are independent.** Three attack lenses tried to construct the merge and none broke the conclusion. But two of the three supporting arguments failed and are withdrawn — and, more seriously, the *criterion itself* was found defective and has since been repaired (below).

**The spine, and it is the one thing that survived every attack — D0(ii):** in flat-space QFT, ℒ → ℒ + c is an **exact symmetry of the action**; an additive constant appears in no S-matrix element and no correlator of local operators, and only *differences* are measurable (Casimir, phase transitions). **Gravity breaks that symmetry** by coupling c to g_μν. So L carries a load-bearing premise — *the field-independent constant gravitates* — that H does not carry at all. Four independent attack routes (trace anomaly, thermodynamic free energy, Casimir/finite-volume, fixed external background) all failed against it. This is a theorem of ordinary QFT, predating every framework in the discussion.

**Withdrawn — P1(i), "the hierarchy problem exists with no gravity."** Overclaimed. The construction *inserts* a heavy singlet rather than deriving one. What is genuinely metric-free is the **conditional**: *if* a threshold at M exists, *then* δm_H² ~ κM²/16π². The antecedent needs a witness, and every non-gravitational candidate is model-inferred (seesaw assumes Majorana neutrinos; Dirac neutrinos give no threshold at all; GUT and PQ scales are inferences). **Restated as an asymmetry of ROLE, not of existence:** for H, gravity at most supplies an instance of a metric-free conditional's antecedent; for L, gravity supplies *the observable itself*.

**Withdrawn — R1, "degenerate discharge."** Its algebra is right (I confirm: with exact SUSY the MSSM potential has no stationary point off the origin, so F = 0 predicts v = 0 *and* ρ_vac = 0). Its **inference is unsound**, and the reductio lands: rejecting a symmetry because its *exact* point predicts the wrong value would equally refuse 't Hooft's chiral protection of the electron mass, which no physicist does. (The photon is the wrong control — there the symmetry is exact *and* the observed value is zero.) The accepted criterion is radiative stability in the *softly-broken neighbourhood* with the symmetry restored in the limit. Under it, **SUSY does explain H** — which is the orthodox case for SUSY, and which this analysis elsewhere concedes.

**Downgraded — P2, the empty-intersection argument.** D_L = {M_S = ρ_obs^¼} is not read off the world; it is derived from the unstated map ρ_vac ≃ M_S⁴. That map is **not universal**: in no-scale supergravity (K = −3M_P² ln(T+T̄), W = W₀) the potential is **identically zero** at tree level with m_3/2 nonzero and undetermined — verified symbolically. At tree level D_L then contains *every* M_S and the 14.6-order disjointness evaporates. **P2 is framework-relative evidence, not proof** — and by our own KC3, quoting "14.6 orders" without that map was a violation.

**Surviving refutation — R3.** Gauging SUSY — the only regime in which a cosmological constant is physical — destroys the positivity: V = e^{K/M_P²}[K^{ij̄}D_iW D_j̄W̄ − 3|W|²/M_P²] is not positive semi-definite. The firewall **strengthened** this: the no-scale counterexample that broke P2 is only possible *because* the −3|W|²/M_P² term cancels the F-term — i.e. the strongest attack on P2 is an instance of R3's own mechanism.

**The criterion defect — found, and now REPAIRED.** The original criterion asked whether the sets of parameter values discharging each problem *at its observed value* intersect. That is an **identity test**, structurally blind to merges where the parameters are not identical but one *determines* the other — and it therefore **systematically over-reports independence**. The exemplar it could not see: Banks-type cosmological SUSY breaking, M_S = √(ρ_obs^¼ M_Pl) → **2.3–5.2 TeV, inside the hierarchy window**, where the intersection is literally nonempty under that relation.

**The repair** (`provenance/merge_criterion.py` + `merge_test.py`, pre-registered, frozen by hash before application, mutation-tested): four merge classes — identity, **functional relation**, common cause, definitional — with a **ledger-native** test. *A merge holds only if the merged accounting has strictly fewer underived inputs than the separate accounting, with the relation's own cost included: a derived relation is free, a posited one is itself an input.* Without that cost clause any two problems merge by fiat — you trade two inputs for one input plus an unexplained relation and gain nothing but a sentence.

**The repair was itself reviewed, and v1 had four defects** — each with a constructed, scored counterexample. The unifying one (**D4**) is the error already ruled against one layer up: *v1 netted a posited relation against a saved number*, collapsing two incommensurable types to one scalar. Proven consequence over 1712 configurations: **a posited binary relation could never merge, by arithmetic alone** — so the very class the repair existed for was unreachable, and v1's "seen and refused" was *arithmetically forced, not physics-adjudicated*. The other three: **D3** the bundle theorem (counting labels, not real-parameter dimension, lets *anything* merge on demand — θ̄ and y_e included); **D2** a one-directional tally leak in the modal case, untested by all nine of v1's controls; **D1** all four classes were total-collapse (n→1), so **shared-constraint** was unrepresentable — and its counterexample is the Friedmann sum rule, where every *pair* correctly scores nothing while the *triple* costs two inputs, not three.

**v2** reports a **vector, never a net**; counts **real-parameter dimension** over a pre-registered atomic vocabulary; tallies the accounts independently and **flags enumeration-sensitivity** rather than silently resolving it; and is **n-sided** with **shared-constraint** and **dissolution** added.

**Banks under v2:** separate {ρ_Λ, M_Pl, v} = 3 → merged {ρ_Λ, M_Pl} = 2, relation **posited**. Vector: **numeric −1, posit +1 → TRADE.** In words: *it buys one real parameter at the price of one underived relation.* Whether that trade is worth taking is a human judgement the tool refuses to make. **Banks is not refuted** — and saying it was is a claim v1's arithmetic manufactured.

## Ruling 2 — The number: **"120 orders" is not load-bearing, but for a different reason than we first said**

**STRUCK — the w = +1/3 argument.** Our sharpest-looking disqualification was that a hard 3-momentum cutoff gives ρ = Λ⁴/16π², p = Λ⁴/48π², hence **w = +1/3 exactly** — "a radiation fluid, not a cosmological constant." The arithmetic is exact (sympy-confirmed). **The inference is wrong.** It diagnoses a *Lorentz-violating regulator*, not the object: an O(4)-invariant Euclidean cutoff gives a field-independent constant in V, hence **p = −ρ exactly, w = −1**, and the magnitude goes **up** (10^122.09 vs 10^120.75). One line of regulator change restores everything the argument claimed to destroy.

**What replaces it, and it is stronger.** The covariant repair does **not** deliver a clean scheme-free magnitude either: sweeping μ from 1 GeV to Λ takes the coefficient from +0.138 to −0.0008 — **a sign flip** — with |V|/ρ_obs running 10^122.09 → 10^119.84. So the covariant magnitude carries its own ~2.3-order band *and an undetermined sign*, stacked on the ≥5.00-order convention span (reduced vs non-reduced M_Pl = 2.80 orders; the 1/16π² loop factor = 2.20; 118/120/121/122/123 all in circulation as the same calculation). **The force transfers from the stress-tensor argument to the convention argument.**

**The real load-bearer** is that in dimensional regularization power divergences are scaleless and vanish identically; the one-loop vacuum energy is quartic in the **mass**, logarithmic in the scale (pole coefficient −m⁴/64π², confirmed). **And the scheme-independent core is untouched:** established thresholds alone — electron ~10^31, QCD condensates ~10^43–10^44.5, electroweak vacuum depth **10^54.675** (verified) × ρ_obs — need no regulator and no cutoff. **The problem does not evaporate. Its famous number does.**

## Ruling 3 — The count: **do not bank a scalar**

**N = 10 is not recoverable as a determinate output of our own criterion**, and this is the wave's most important self-correction. The membership test's clause (ii) is **disjunctive** ("changes whether a problem-statement exists **or what it is**"), and we applied the loose disjunct to what we wanted in and the tight disjunct to what we wanted out. Read tightly (existence only), ρ_obs's *value* and v both drop out — a cluster problem survives ρ = 10⁻⁴⁰ GeV⁴ — giving **~6–8**. Read loosely, every parameter entering any threshold qualifies: **>15**. With the corrections below, our own loose reading gives **12–13**. *The one value the criterion does not determine is 10.*

**Three failures of our own kill-conditions, found by the firewall:**

- **KC4 failed in the omission direction.** We policed assumptions being *imported* and never ran the test against assumptions being *omitted*. **Lorentz invariance of the vacuum is uncounted** — and Ruling 2 *proves* it load-bearing, since a Lorentz-violating regulator yields w = +1/3 and hence no explanandum at all. That is an internal contradiction between our own rulings.
- **KC1 self-violation, and it is systematic.** Two of the ten are **compounds**: "EFT naturalness applies" fuses EFT *validity* (structural) with EFT *naturalness* (methodological) — the landscape stance accepts the first and rejects the second; and "vacuum energy gravitates" fuses *Lorentz invariance forcing T_μν ∝ g_μν* with *minimal sourcing of the metric* — unimodular denies only the second. We enforced the kill-conditions on Ruling 1 and relaxed them on Ruling 3.
- **KC5 is asymmetric with respect to our own default.** Merges characteristically arrive framework-borne (SUSY, no-scale, landscape, Banks); separations can usually be stated framework-free. A rule excluding frameworks as lenses therefore **filters merge evidence out** — on top of a default already broken toward independent, that is a double thumb on the scale. And we used a framework as a lens at the decisive point anyway (ρ_vac ≃ M_S⁴ generating D_L).

**Accepted additions:** *B3 — heavy thresholds exist above v* (a proposition about the world, underived in SM+GR; drop it and the hierarchy problem-statement dissolves — Bardeen's position; distinct from the naturalness *criterion*), and *Lorentz invariance of the vacuum*.

**The deliverable is a TYPED INVENTORY, not an integer** (overseer-ruled 2026-08-04: *if the integer is a type-mixed sum, don't ship an integer* — an integer invites exactly the cross-cluster comparison its own disclaimer forbids). Live in the register under `ledger_scope: vacuum-cluster`, audited by `provenance/validate_scoped.py`:

### CORRECTED 2026-08-04 by the compound-split re-audit

The inventory below **grew**, which is the anti-flattering direction and where an honest re-audit of one's own work should land. It grew for **two different reasons that are never summed**:

| type | count | members |
|---|---|---|
| **measured** (data; carries *no* implication about explanatory obligation) | **3** | ρ_Λ, v, M_Pl |
| **postulate** (propositions about the world; each with a CONTESTED/STANDARD subtype) | **11** | *contested (4):* minimal sourcing · heavy thresholds exist · EFT vacuum operator · gravitational UV ceiling<br>*standard (7):* Lorentz-invariant vacuum · IR gravity is GR · **state + expectation functional** · mean-field sourcing · EFT decoupling · **universal metric coupling** · flatness in the reduction |
| **heuristic** (criteria; no truth-value) | **2** | normative naturalness · typicality/measure |
| **open** | **2** | w = −1 (an *edge*, see below) · GRUT's relation (decorative, zero-credit) |
| *retired, **not counted*** | *2* | *semiclassical sourcing → split; EFT validity → split* |

**Droppable — an alternative formulation denies or omits it: 14.** *The types do not commute; there is no total, by ruling.*

**The two tallies, kept apart:**
- **2 COMPOUNDS** (one node carrying two dischargeable things → **split** it): *semiclassical sourcing* → a state-and-expectation-functional + mean-field sourcing; *EFT validity* → decoupling + the vacuum operator. The second was **pre-registered as atomic** and was not — the sharpest miss of that audit. Cohen–Kaplan–Nelson, UV/IR mixing and holographic bounds all accept ordinary decoupling and deny the naive bookkeeping for the dimension-zero operator, so one node had been feeding **both sides of the Λ/hierarchy division Ruling 1 turns on**.
- **3 OMISSIONS** (a presupposition booked nowhere → **add** a node): *universal metric coupling / the equivalence principle*, presupposed by minimal sourcing, mean-field sourcing **and** IR-gravity-is-GR and booked by none; *the gravitational UV ceiling*, which was housed only inside heavy-thresholds' parenthetical; *spatial flatness in the reduction*, an uncounted premise of a **measured** node whose `depends_on` was empty while its own scheme tag read "FLAT".

**Why the distinction is the wave's real output:** compoundness and omission *present identically* — both feel like "this node carries more than one thing" — and an analyst holding only the split tool fixes an omission by cutting the nearest node, mislocating a cluster-wide presupposition into that node's dependency structure. Two of five pre-registered candidates were exactly that error. See `provenance/OMISSION_STANDARD.txt` and CHARTER §4.

**Two ruled corrections carried in the same wave:** heavy-thresholds' *"equivalently: the EFT has a genuine cutoff below M_Pl"* was **struck as false** — the existence of coupled heavy states *implies* a cutoff and is not implied by it, since a cutoff can be non-particle — found independently by two analysts under opposite mandates. And **w = −1 is an EDGE booked as a vertex**: it duplicates undecided pair 5 below and appears a third time inside ρ_Λ's overturning clause. It costs nothing only because this map refuses a total. **If anyone ever ships an integer, it must not be summed.**

<details><summary>The pre-correction inventory, as first banked (kept for the diff)</summary>

measured **3** · postulate **6** (minimal sourcing · Lorentz-invariant vacuum · semiclassical sourcing · heavy thresholds · EFT validity · IR gravity is GR) · heuristic **2** · open **1**; droppable 8 of 12. Two of those twelve were already compound nodes split under KC1, and two were added by the firewall — so this node set had *already* been corrected once in each direction before the re-audit corrected it again.
</details>

## The five undecided pairs, with their deciding questions

1. **(vacuum energy gravitates, IR gravity is GR)** — dissociable *classically* (verified algebraically); does the dissociation survive quantization? The literature is genuinely split. *Deciding question: is unimodular gravity's decoupling of vacuum energy stable under quantum corrections, or is it gauge-fixed GR with identical predictions?*
2. **(normative naturalness, typicality/measure)** — one input in two hats, or two? *Deciding question: can the normative obligation be stated without an implicit ensemble?*
3. **(M_Pl, heavy thresholds exist)** — decides whether M_Pl is a cluster member or merely the unit-setter, and whether the charitable reading of "120 orders" is available at all. *Deciding question: at what scale does the gravitational derivative expansion actually break down?*
4. **(ρ_Λ, typicality)** — the only route by which ρ_Λ stops being bedrock. *Deciding question: is there an ensemble with a computable, non-question-begging measure under which the observed value is typical, independently established rather than postulated to license the inference it supports?*
5. **(ρ_Λ-as-a-value, w = −1)** — one input or two (an amplitude plus a constancy)? Empirically in motion: DESI DR2 reports 2.8–4.2σ for w₀wₐCDM depending on the supernova compilation, always inside the two-parameter CPL family. *Deciding question: does a non-parametric reconstruction of w(z) prefer evolution?*


## The merge criterion — the arc, closed

**What it is, correctly labelled:** a **declaration schema plus a structural validator — never an adjudicator.** Three of its four judgements are declared non-mechanizable and the fourth needs an authored table, so *every* input to its arithmetic is an analyst judgement. Its cardinal invariant now sits at the top of the file in the harness's own idiom: **passing the merge tool never banks a reduction — it produces a candidate for adjudication.** Structural refusals (`REFUSED-INCOMPLETE`) are verdicts it may reach; **REDUCTION / TRADE / NO-REDUCTION are declared readings**, and eleven tests pin the distinction so no future wave can quietly re-promote it.

**Why that reframe rather than a fourth hardening round:** v1 → 4 defects, v2 → 8 blockers, v3 → the registry broke its own pre-registration. Each fix *relocated* where the judgement enters — analyst labels, then analyst integers, then an authored registry — rather than removing it. That is a fixed point of relocation, not convergence. **If a tool cannot be certified, do not let it certify.**

**The registry is derived, not authored.** `registry_mapping.py` states one domain-free rule (dim = 1 per named input; kind from the claim's own tier through a frozen table; a claim whose cost is booked elsewhere gets no entry) and `registry_derive` applies it mechanically. Applied to six blocked ids it **overruled the author on two and caught a third omission**: α was refused (its anchor credit is suspended — not an input), `mu_linear` was refused (its own note says it adds no input directly), and rung6 turned out to carry *two* inputs where one had been listed. **The exception list — one entry — is the audit surface.**

> **Registry caveat, kept prominent: audit the registry before the arithmetic.** The arithmetic is no longer where the judgement lives.

**Banks is TRADE, not refuted** — −1 real parameter, +1 posit. It buys the weak scale's independence at the price of a relation nobody derives, and whether that trade is worth taking is a judgement the tool declines to make.

## What this wave actually demonstrated about the method

The discipline transferred. Off its home turf, on its first outing, it: caught the field's most-quoted number as convention-dependent by ~5 orders with an undetermined sign; caught two normally-uncounted background assumptions; **caught its own strongest argument (w = +1/3) as a regulator artifact**; **caught its own kill-conditions failing in three distinct ways** — omission-blindness, compound nodes, and a default-protecting asymmetry; and **refused its own headline integer**. It also found a live category error in this program's own CHARTER (Λ listed under *assumed*, alongside the Born rule, when it is a datum every candidate theory must reproduce).

It did not solve anything, and it was not supposed to.

**And it found a defect in its own instrument — twice.** The merge criterion that produced the independence verdict was an identity test, blind to an entire merge class. That defect would not have produced one blind spot across many clusters — it would have replicated the *same* blind spot in every cluster and corrupted exactly the cross-cluster double-count analysis that is the reason to map more than one. It was repaired before scaling — and then the *repair* was independently reviewed and found to have four defects of its own, all fixed in v2 before anything scaled.

**Re-run against this program's own ledger under v2:** all four of GRUT's recorded double-count checks now score **TRADE (−1 numeric, +1 posit)**, not "refused". **The ledger does not move** — a trade is not a reduction, and taking one would swap a booked input for an unbooked relation, which is the laundering the ledger exists to prevent. **NET +13 stands.** But the *warrant* is corrected: it is *"no relation is derived, so no input can be removed without booking a new one"* — **not** *"these are demonstrably different things"*, which is stronger than anything shown.

**A new owed item, surfaced by the repair:** no **shared-constraint** check has ever been run on GRUT's ledger. That class is not localizable to any pair, so the four pairwise checks *cannot* have found it — the Friedmann blindness, at home. An n-sided sweep of the +13 is now named and owed.

**Marked precisely on `method_novelty`, which asks for *different team, different problem, catches a real error*:** this is **same team, different problem, real errors caught** — two of three. Banked as **partial movement, explicitly not a discharge** (the first movement on that node in the program's history). The missing third is the load-bearing one: it is still self-evidence, and by the node's own rule self-evidence does not settle the external-validation debt.
