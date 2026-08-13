# Where the Responsive Vacuum Stops

*A negative-results report on a program that modelled the gravitational vacuum as a medium with memory, priced every assumption it took, and pushed until it stopped.*

D. Ryan Grover · {{STAMP_DATE}}

---

## Abstract

**This is a negative-results report.** A framework treating the gravitational vacuum as an open medium with finite memory — one in-in (Schwinger–Keldysh) influence action, its response kernel decomposed on Barnes–Rivers spin projectors — was built, priced assumption by assumption, and pushed until it stopped. This document states where it stopped.

Three results outlive it, and two are about general relativity rather than about this framework. **First:** linearized Einstein–Hilbert is *not* transverse-traceless. Diffeomorphism invariance buys transversality but not tracelessness; the kernel is ½k²[P⁽²⁾ − 2P⁽⁰ˢ⁾], so the scalar sector survives the Ward identity at an exact ratio P⁽⁰ˢ⁾/P⁽²⁾ = −2 — which means the pure-TT ansatz this framework was built on is a **choice**, not a theorem, and it is priced as one. **Second:** the thermodynamic arrow decomposes — an open medium's arrow *exists* intrinsically, while its *direction* is imported from the bath's state, so the framework sharpens the Past Hypothesis rather than dissolving it. **Third:** the anomaly action that was supposed to fix the framework's one free parameter was computed and **fixes nothing** — it yields a scale, not a number.

The framework produced **no novel positive prediction**; the register's `derived` tier holds **{{tier_derived}}** entries. Its single decisive question — whether the assembled low-frequency spectral density ρ_TT(ω→0) = 2 Im G_R^TT of the *pure-graviton* de Sitter self-energy has a relaxation pole or a branch cut ([arXiv:2103.08547](https://arxiv.org/abs/2103.08547), [2107.13905](https://arxiv.org/abs/2107.13905), [2602.07908](https://arxiv.org/abs/2602.07908)) — was drafted as a one-page ask **and never sent**; later in-house work suggests it may be **ill-posed** in the formalism its intended readers use, since that corpus never reduces Σ(x;x′) to a time difference and so has no ω at all.

Two inflations are refused. The physics is not presented as a theory. The method — a claim register that prices assumptions and blocks derivations that quietly acquire them — is the more transferable output and is **unvalidated by anyone but its author**. A prior book by the same author, with a live DOI, describes a **different** framework and is substantially wrong; the note below says what and why the correction is owed rather than done.

**Every link in this program's verification chain except one human being is an AI.** That is stated in the front matter, at full volume, because a program whose audit chain is AI is more trustworthy for saying so than for letting the word "verified" do quiet work.

**Where to check any of this.** Repository: `github.com/ryangrvr/GRUT-RAI`, commit `f4ff2dfe16cb`, MIT licence; the rebuild described here is the `rebuild/` subtree, and the prior lineage discussed below is retained in the same repository as historical record. The commands below reproduce everything numeric in this document, from a clean checkout, with no dependencies beyond the Python 3 standard library:

```bash
cd rebuild
python3 provenance/validate.py                     # the register gate
python3 provenance/emit_public_numbers.py --check   # every count above, regenerated
python3 provenance/build_public_doc.py --check      # this document, re-rendered from source
cd provenance && python3 -m pytest -q               # the full suite
```

`rebuild/HOW_TO_VERIFY.md` gives the rest, including what a green run does and does not mean. The eleven commits this document's argument points at — the regression that turned *commit* into *accept*, the audit that undercounted by eight, the {{n_pressure_removals}} occasions adversarial pressure removed a claim I wanted — are in that history, dated. **This work has not been deposited under its own DOI; when it is, this line will name it.** Independent researcher, no institutional affiliation; contact ryngrvr@gmail.com.

---

## If you read nothing else

1. **No novel positive prediction.** The `derived` tier is empty and a test fails if that changes without this sentence changing.
2. **Three results outlive the framework**, and two are facts about GR: the linearized-EH kernel is not transverse-traceless (exact ratio −2, constrained sector); the arrow decomposes into intrinsic existence and imported direction; and the anomaly action meant to fix the framework's one free parameter was computed and **fixes nothing** — it yields a scale, not a number.
3. Its one decisive question — **pole or cut in ρ_TT(ω→0)** — was **drafted, held, never sent**, and may be ill-posed as posed.
4. **No outside physicist has answered any physics question put by this program.** Fixed point 2 states this checkably rather than as a denial.
5. **Every verifier in the chain but one human is an AI** — including the role the register calls "overseer," in 214 places.
6. A previous book by this author, live under its own DOI, is **not this framework** and is substantially wrong. The correction is **owed, not done**.

---

## Six fixed points

**1 — Zero novel positive predictions; the `derived` tier is empty.** Of {{n_grut}} claims in the framework's scope, the tier reserved for "follows from the foundation, derivation exhibited and checked" holds **{{tier_derived}}**. Populated: `shown` ({{tier_shown}}, standard physics verified against primary sources by the author), `derived-pending` ({{tier_derived_pending}}, derived modulo a *named* open input), `assumed` ({{tier_assumed}}), `to-derive` ({{tier_to_derive}}). The tiers are assigned by the author, alone.

**2 — No outside physicist has answered any physics question put by this program.** Stated specifically, because the general denial is unfalsifiable-sounding:

The register contains **{{spec_B}} records phrased as an external pass having run** — among them **{{n_spec_2026_06_25_occurrences}}, across {{n_spec_2026_06_25_nodes}} nodes**, written as *SPECIALIST CONFIRMED* and *SPECIALIST-CORRECTED* and dated 2026-06-25. **No transmission to any outside human is logged at any date** — that half is checkable against the register in minutes, and an adversarial search of every file, log, git object and archived snapshot found none. That those passes were AI sessions run by the author is **not** established by the register, which never records modality; **it is the author's own statement, made 2026-08-12**, and the reader should treat the two halves differently: one is auditable, the other is testimony.

An audit of the word *specialist* found **{{spec_total}} occurrences across {{spec_nodes}} of {{total}} claims** ({{spec_raw_incl_annotations}} if you count the 2026 annotation blocks that document them), classified: **{{spec_B}}** phrased as a pass having run, **{{spec_A}}** reserving a *future* expert, **{{spec_C}}** generic or collective, **{{spec_D}}** filenames. That word is not the only one that reads as outside authority — the register also uses *referee*, *reviewer*, *externally reviewed*, and *overseer-verified*, where "overseer" is the author. Appendix D classifies all of them. The first version of this audit used one word and one letter-case; both narrowings are why the term list is now pre-registered before the audit runs.

**3 — A prior book with a live DOI describes a different theory.** Concept DOI `10.5281/zenodo.19803663`; latest version `10.5281/zenodo.20783057`. See the note below.

**4 — Every count here is generated, not typed.** See the next section.

**5 — This is not the program's final deposit.** A signed termination condition schedules a closing document *after* a stop condition fires. **No stop condition has fired.** This document corrects a wrong live DOI — a different obligation — and changes nothing about what fires or when.

**6 — The name contains "Theory of Everything."** It does, on the prior deposit's title page. What that reaches for is addressed at the end, in the author's own voice, last.

---

## The one-number rule

No count in this document was typed by hand. Every figure derived from the claim register is a named placeholder in the source file, substituted by `provenance/build_public_doc.py` from `provenance/emit_public_numbers.py`; a test fails if the rendered text disagrees with a fresh run, **and a second test fails if any register-derived figure appears typed in the source** — as a digit, a spelled-out numeral, or a hyphenated ratio. The rule exists because this program has published wrong counts twice: once through an audit pattern that silently dropped every capitalized instance of the word it counted, and once in the prior book, at scale.

**Three exceptions, each marked where it occurs.** Numbers **quoted from the prior deposit** are that record's claims about itself. Numbers **cited from published literature** carry their source. And numbers from **the verification pass over the prior deposit** are that pass's findings, attributed to it — they are not this register's counts and no script here can emit them.

---

## A note on the prior deposit

A book by this author is live on Zenodo: *Grand Responsive Universe Theory GRUT ToE v4.0 — The Emergence of Everything — Candidate Framework*, deposited 2026-06-21, resource type **preprint**, latest of several versions under concept DOI `10.5281/zenodo.19803663`. **It is not the framework described here, and it is substantially wrong.**

It was not sloppy, and that is the point. Its own public description reads:

> *"Fully machine-checked. 121 registered claims across six tiers, over 3,000 gating tests, falsifiers attached — every reader-facing claim mapped to a registry tier, no HOSTED or OPEN result dressed as DERIVED."*

*(Those figures are quoted from that deposit; they are its claims about itself.)* That is this document's pitch, made first, by the same author, about a body of work a later verification pass scored **1-of-18 on its verifiable numbers, 0-of-7 on its falsifiers, and 1-of-11 on its scorecard rows** *(that pass's findings, attributed to it)*. A reader who notices I am promising machine-checked rigor twice is right to notice, and is owed the mechanism rather than an assurance.

**Here is the mechanism.** The tests tested the code. The register graded itself. Nothing in the loop was charged with trying to break a result before it was banked. Three thousand tests can pass against a register written by the same process that wrote the claims; a tier label is worth only the adversarial pressure applied before it is assigned, and there was none. The test count measured coverage of machinery, not scrutiny of physics.

**And here is what is different now, stated with its limits rather than as a credential.** A substantive result is surfaced by `provenance/bankgate.py` and then attacked by a separate AI session — run by me, from a clean context, instructed to default to *broken* — before I accept it. **That pass is not independent in the sense fixed point 2 requires:** same operator, same model family, no human in the loop but me. **And the gate reports rather than blocks** — it exits zero on a flag; it surfaces work for a firewall, it does not withhold anything by itself. Its only claim to bite is that it is charged against the result and its verdicts are recorded whether or not I liked them. {{n_pressure_removals}} times in this document's own construction that pressure removed a claim I wanted; the occasions are listed in `provenance/construction_pressure.json`, so the number is emitted and the instances are inspectable. The register carries those verdicts as free text, not as a structured field — a gap, and the reason this is asserted here and only partly demonstrated.

What died with the book: an entire dark-matter substrate line; a two-anchor hierarchy ledger; a claimed unified no-go; and the whole `FORBIDDEN-BY-THEOREM` tier, which asserted impossibility results the framework had not established.

Two errors can be quoted from the book against itself. Its key-points list advertises a **32σ** exclusion *(quoted)*; this register's own recomputation of that quantity returned **{{isw_sigma}}σ** ({{isw_central}} central), and found the mechanism it rested on had the wrong sign. The same list advertises a falsifier at **"689 Hz, zero free parameters"** *(quoted)*; that observable was later found to be energy-basis rather than position-basis — not a free-parameter question at all, so the falsifier as advertised does not exist.

**The remedy, stated as owed.** A version DOI is permanent by design: `10.5281/zenodo.20783057` will retrieve that text forever. What *can* be done is to deposit a superseding note as a new version under the concept DOI, so every citation of `10.5281/zenodo.19803663` resolves to the correction and points onward here. **That has not been done.** It is owed, it is mine to do, and until it is, the prior record stands uncorrected where most readers will meet it.

---
