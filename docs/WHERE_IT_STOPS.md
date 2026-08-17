# Where the Responsive Vacuum Stops

*A negative-results report on a program that modelled the gravitational vacuum as a medium with memory, priced every assumption it took, and pushed until it stopped.*

D. Ryan Grover · 2026-08-12

> **Correction record, 2026-08-12.** Part I's first draft failed its mandatory hostile pre-screen (DO-NOT-SHIP): I.1 overstated two priority claims and contained a physics error in its gauge fence. The section was left standing under a do-not-cite banner rather than pulled, then corrected: I.1 is now one third its drafted length and claims nothing beyond the literature it cites; the register nodes that carried the same over-scoped clause were corrected **first**, with the source read (arXiv:2507.03103) that the register itself had flagged as owed. The full trail — draft, verdict, correction — is in the repository history.
>
> **Published in parts.** Complete as of 2026-08-12: the front matter, the note on the
> prior deposit, and **Part I** (corrected; see the record above). **Outstanding:** Parts 0 and
> II through VII, and the appendices. The outline is fixed
> and lives in the repository; the sections below this front matter **do not yet exist**. This
> line is updated at the close of every wave, and a document silent about its own
> completeness would be the last uncaught instance of the pattern this document is about.

---

## Abstract

**This is a negative-results report.** A framework treating the gravitational vacuum as an open medium with finite memory — one in-in (Schwinger–Keldysh) influence action, its response kernel decomposed on Barnes–Rivers spin projectors — was built, priced assumption by assumption, and pushed until it stopped. This document states where it stopped.

Three results outlive it, and two are about general relativity rather than about this framework. **First:** linearized Einstein–Hilbert is *not* transverse-traceless. Diffeomorphism invariance buys transversality but not tracelessness; the kernel is ½k²[P⁽²⁾ − 2P⁽⁰ˢ⁾], so the scalar sector survives the Ward identity at an exact ratio P⁽⁰ˢ⁾/P⁽²⁾ = −2 — which means the pure-TT ansatz this framework was built on is a **choice**, not a theorem, and it is priced as one. **Second:** the thermodynamic arrow decomposes — an open medium's arrow *exists* intrinsically, while its *direction* is imported from the bath's state, so the framework sharpens the Past Hypothesis rather than dissolving it. **Third:** the anomaly action that was supposed to fix the framework's one free parameter was computed and **fixes nothing** — it yields a scale, not a number.

The framework produced **no novel positive prediction**; the register's `derived` tier holds **0** entries. Its single decisive question — whether the assembled low-frequency spectral density ρ_TT(ω→0) = 2 Im G_R^TT of the *pure-graviton* de Sitter self-energy has a relaxation pole or a branch cut ([arXiv:2103.08547](https://arxiv.org/abs/2103.08547), [2107.13905](https://arxiv.org/abs/2107.13905), [2602.07908](https://arxiv.org/abs/2602.07908)) — was drafted as a one-page ask **and never sent**; later in-house work suggests it may be **ill-posed** in the formalism its intended readers use, since that corpus never reduces Σ(x;x′) to a time difference and so has no ω at all.

Two inflations are refused. The physics is not presented as a theory. The method — a claim register that prices assumptions and blocks derivations that quietly acquire them — is the more transferable output and is **unvalidated by anyone but its author**. A prior book by the same author, with a live DOI, describes a **different** framework and is substantially wrong; the note below says what and why the correction is owed rather than done.

**Every link in this program's verification chain except one human being is an AI.** That is stated in the front matter, at full volume, because a program whose audit chain is AI is more trustworthy for saying so than for letting the word "verified" do quiet work.

**Where to check any of this.** Repository: `github.com/ryangrvr/GRUT-RAI`, commit `f4ff2dfe16cb`, MIT licence — that commit holds every artifact this document describes, and the document naming it is necessarily a descendant of it, since a file cannot contain its own hash; the rebuild described here is the `rebuild/` subtree, and the prior lineage discussed below is retained in the same repository as historical record. The commands below reproduce everything numeric in this document, from a clean checkout, with no dependencies beyond the Python 3 standard library:

```bash
cd rebuild
python3 provenance/validate.py                     # the register gate
python3 provenance/emit_public_numbers.py --check   # every count above, regenerated
python3 provenance/build_public_doc.py --check      # this document, re-rendered from source
cd provenance && python3 -m pytest -q               # the full suite
```

`rebuild/HOW_TO_VERIFY.md` gives the rest, including what a green run does and does not mean. The eleven commits this document's argument points at — the regression that turned *commit* into *accept*, the audit that undercounted by eight, the 4 occasions adversarial pressure removed a claim I wanted — are in that history, dated. **This work has not been deposited under its own DOI; when it is, this line will name it.** Independent researcher, no institutional affiliation; contact ryngrvr@gmail.com.

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

**1 — Zero novel positive predictions; the `derived` tier is empty.** Of 49 claims in the framework's scope, the tier reserved for "follows from the foundation, derivation exhibited and checked" holds **0**. Populated: `shown` (10, standard physics verified against primary sources by the author), `derived-pending` (4, derived modulo a *named* open input), `assumed` (15), `to-derive` (20). The tiers are assigned by the author, alone.

**2 — No outside physicist has answered any physics question put by this program.** Stated specifically, because the general denial is unfalsifiable-sounding:

The register contains **28 records phrased as an external pass having run** — among them **6, across 5 nodes**, written as *SPECIALIST CONFIRMED* and *SPECIALIST-CORRECTED* and dated 2026-06-25. **No transmission to any outside human is logged at any date** — that half is checkable against the register in minutes, and an adversarial search of every file, log, git object and archived snapshot found none. That those passes were AI sessions run by the author is **not** established by the register, which never records modality; **it is the author's own statement, made 2026-08-12**, and the reader should treat the two halves differently: one is auditable, the other is testimony.

An audit of the word *specialist* found **49 occurrences across 18 of 70 claims** (58 if you count the 2026 annotation blocks that document them), classified: **28** phrased as a pass having run, **17** reserving a *future* expert, **2** generic or collective, **2** filenames. That word is not the only one that reads as outside authority — the register also uses *referee*, *reviewer*, *externally reviewed*, and *overseer-verified*, where "overseer" is the author. Appendix D classifies all of them. The first version of this audit used one word and one letter-case; both narrowings are why the term list is now pre-registered before the audit runs.

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

**And here is what is different now, stated with its limits rather than as a credential.** A substantive result is surfaced by `provenance/bankgate.py` and then attacked by a separate AI session — run by me, from a clean context, instructed to default to *broken* — before I accept it. **That pass is not independent in the sense fixed point 2 requires:** same operator, same model family, no human in the loop but me. **And the gate reports rather than blocks** — it exits zero on a flag; it surfaces work for a firewall, it does not withhold anything by itself. Its only claim to bite is that it is charged against the result and its verdicts are recorded whether or not I liked them. 4 times in this document's own construction that pressure removed a claim I wanted; the occasions are listed in `provenance/construction_pressure.json`, so the number is emitted and the instances are inspectable. The register carries those verdicts as free text, not as a structured field — a gap, and the reason this is asserted here and only partly demonstrated.

What died with the book: an entire dark-matter substrate line; a two-anchor hierarchy ledger; a claimed unified no-go; and the whole `FORBIDDEN-BY-THEOREM` tier, which asserted impossibility results the framework had not established.

Two errors can be quoted from the book against itself. Its key-points list advertises a **32σ** exclusion *(quoted)*; this register's own recomputation of that quantity returned **2.0σ** (1.97 central), and found the mechanism it rested on had the wrong sign. The same list advertises a falsifier at **"689 Hz, zero free parameters"** *(quoted)*; that observable was later found to be energy-basis rather than position-basis — not a free-parameter question at all, so the falsifier as advertised does not exist.

**The remedy, stated as owed.** A version DOI is permanent by design: `10.5281/zenodo.20783057` will retrieve that text forever. What *can* be done is to deposit a superseding note as a new version under the concept DOI, so every citation of `10.5281/zenodo.19803663` resolves to the correction and points onward here. **That has not been done.** It is owed, it is mine to do, and until it is, the prior record stands uncorrected where most readers will meet it.

---

# Part I — Two results that outlive the framework

Most of what follows this Part is about a framework that stopped. This Part is not. The two results here are about general relativity and about open-system irreversibility, and they hold whether or not the responsive-vacuum framing is worth anything. They are also, both of them, **careful restatements of standard material** rather than new physics — that claim is made explicitly in I.3, and the reader should hold me to it while reading I.1 and I.2.

---

## I.1 — General relativity's own response kernel is not transverse-traceless

> **In one paragraph.** When you write down how spacetime responds to being disturbed, the response splits into pieces labelled by spin. It is tempting, in model-building, to keep only the spin-2 piece — gravitational waves have two polarizations, so a "purely gravitational" response ought to be purely spin-2. That reasoning is wrong, and general relativity is the counterexample: linearized Einstein–Hilbert's own kernel carries a scalar piece alongside its spin-2 one. A model that keeps only spin-2 has made a **choice**.

**Everything in this section is standard material, and this time that sentence is the section.** The spin-projector decomposition is Barnes (1963) and Rivers (1964), applied to linearized gravitation by van Nieuwenhuizen (1973), routine since Stelle (1977). The kernel of linearized Einstein–Hilbert in that basis is the standard form ½k²[P⁽²⁾ − (d−2)P⁽⁰ˢ⁾] with P⁽⁰ˢ⁾ = θθ/(d−1) — in four dimensions, a scalar-to-spin-2 ratio of **−2** — and its scalar coefficient is precisely what produces the textbook conserved-source exchange T·T − ½T², so it is observationally load-bearing: it fixes the Newtonian normalization and the light-bending ratio, while **carrying no radiative degrees of freedom** — the physical spectrum is exactly two helicities. The scalar-channel-on-or-off question is likewise old ground: Stelle's R² coefficient switches the spin-0 channel on independently; Weyl-squared gravity is the standard case where it is zero *with a symmetry argument supplied*; ghost-free non-local gravity treats the spin-0 form factor as an independent function. This program's own computations of the −2 are **transcription checks against that literature, twice, in exact rational arithmetic** — not the source of the number.

*(Attestation: the priority references above were verified for existence, authorship, journal and year through secondary literature; I did not read the originals. An earlier draft of this section claimed two narrow novelties on top of the textbook material. A hostile pre-screen — run under this program's own mandatory rules — found both overstated and found a physics error in the section's gauge fence; the corrected account is in the repository, and the register's own nodes now carry the correction. The details are Part VI's material: the short version is that a symmetry restriction this framework's documentation attributed to the Ward identity turns out, per Salcedo–Colás–Dufner–Pajer's open-gravity construction, to be partly a choice — which makes the sentence below stronger, not weaker.)*

**The one thing this section is for:** the framework this document describes was built on a purely transverse-traceless response kernel. Nothing above forces that — general relativity's own kernel is the counterexample, and the open-gravity operator space is wider still. So the register prices the TT ansatz as what it is: **a declared assumption, costing one entry in the ledger, inherited as a conditionality by every result that leans on it.** The interrogation that established this was commissioned by this program against its own framework, and the answer — *chosen, not forced* — made the framework weaker and the register more honest.

## I.2 — Where the arrow of time is imported

For an open quantum system reduced from time-symmetric microscopic dynamics via the closed-time-path influence functional, the thermodynamic arrow splits into two logically separable parts.

**Existence is intrinsic.** The influence functional of a Gaussian bath yields a retarded dissipation kernel and a noise kernel with: a retarded, analytic self-energy (causal, analytic in the upper half plane); a positive Källén–Lehmann spectral measure; and a positive-semidefinite noise kernel. These hold operator-identically — they need no assumption about the *system's* initial state. So *that* dissipation occurs, and its *magnitude*, are genuine outputs of the formalism. This is the strongest defensible version of the "intrinsic arrow" claim, and it is real but narrow.

**Direction is imported.** None of that fixes the *sign* of relaxation. The direction is set by low-entropy data on the **past boundary**, in three interchangeable guises that reduce to one initial-condition assumption:

1. **the past-endpoint contour convention** — where on the closed time contour the density matrix is specified;
2. **passivity of the bath state.** By Pusz–Woronowicz (1978), a thermal (KMS) state with positive inverse temperature *is* passivity *is* "no work extractable" *is* the second law as a property of the state. The sign of that inverse temperature alone decides damping versus anti-damping; a legal population-inverted state **reverses the arrow**. Spectral positivity never fixes this sign;
3. **factorization of the initial system-bath state** — the quantum *Stosszahlansatz*. In the Nakajima–Zwanzig construction the closed dissipative master equation is literally a deletion of the initial correlations; irreversibility is generated by that choice.

### The exactly-solvable demonstration

`calc/arrow_origin.py` makes this concrete on the independent-boson (pure-dephasing) model with a super-Ohmic finite-memory bath, where the decoherence function is closed-form. It exhibits, exactly:

- **Time symmetry of the dynamics** — the decoherence function is even in time, identically. The equations of motion pick no direction.
- **Reversibility** — with finitely many modes the coherence decays toward zero and **returns to exactly one** at the Poincaré recurrence time.
- **The continuum limit as an assumption** — the recurrence time grows with mode number; a monotone, irreversible decay exists *only* in the many-mode limit.
- **Initial-state dependence** — the decay rate is set entirely by the assumed bath state.

So on a model where every step is visible, the arrow lives in the factorized low-entropy initial state and in the continuum limit — both assumptions, neither a consequence of the dynamics.

### Scope, and the ceiling that closed

Asked whether the direction tracks the sign of the inverse temperature *alone*, the honest answer is **no**, and the over-general version must be demoted:

- **Within the equilibrium class:** yes — the detailed-balance direction is fixed by that sign, and its positivity is the imported low-entropy input.
- **Outside it** (squeezed, driven, active, non-thermal baths): there is no single temperature; noise and dissipation decouple, and the system relaxes to a non-equilibrium steady state whose direction is set by the full generator.

Either way the direction is set by the assumed reservoir state, never by the time-symmetric dynamics. The ceiling is closed **within the cases surveyed** — a scoped result, not a universal no-go. One tightening runs against the result and belongs with it: even the "intrinsic" positivity above is established relative to a passive reference state, so the passive-state assumption co-supplies part of what looks dynamics-intrinsic. **The import is more total, not less.**

### What this is not

**It is not a solution to the arrow of time.** It is a decomposition plus a triangulation: three apparently different choices — contour, passivity, factorization — are one initial-condition assumption, and no surveyed derivation escapes it. Bogoliubov's weakening-of-correlations and eigenstate-thermalization/typicality arguments **relocate** the input; they do not remove it. The contribution is to say precisely what must be assumed and where, and to refuse to let it enter disguised as something dynamical.

### The framework corollary, last

In the responsive-vacuum program the equilibrium constraint is enforced as a hard admission gate that every candidate response kernel must pass. That gate — built as a *discipline* mechanism, to stop unphysical kernels — is *exactly* the object where the direction enters. The program does not bury the Past Hypothesis; the discipline machinery and the imported assumption turn out to be the same gate. That is a tidy fact about the construction and nothing more; sections above it do not depend on it.

---

## I.3 — Why these two are different in kind, and what neither of them is

The two results differ in what they are about. I.1 is a fact about **general relativity** — an exact statement about the structure of a kernel that exists whether or not anyone builds an open-system model on top of it. I.2 is a fact about **a formalism** — the in-in reduction of a bath — and applies to any open quantum system, gravitational or not. Neither is a fact about the responsive vacuum. That is precisely why they are in this Part: they are what remains if the framework is wrong.

**And now the demotion, before a referee supplies it: both are careful restatements of standard material.**

I.2 says so about itself in its own source document, and has from the beginning: *"This is not a solution to the arrow of time."* Every ingredient — Feynman–Vernon factorization, Poincaré recurrence, Pusz–Woronowicz passivity, the Nakajima–Zwanzig deletion — is established work by other people. What is offered is the *organization*: the claim that three assumptions are one, and the refusal to let it hide.

I.1 is demoted further than I.2, because its pre-screen demanded it: the section now claims **nothing** beyond the literature it cites. Its first draft claimed two narrow novelties; the mandated hostile pass found both overstated — one refuted by Stelle's own organization of the scalar channel, the other inverted by Salcedo–Colás–Dufner–Pajer's result that dissipation necessarily breaks the doubled diffeomorphism symmetry — and found a physics error besides. The pre-commitment in the first draft read: *if someone shows me that consequence stated in the literature, the honest response is to cite them and reduce this section to a pointer.* Someone did — the program's own pre-screen — and this is the pointer.

So the correct grade for this Part is: **two clarifications, carefully made, of things the literature already contains** — one of which cost the framework a load-bearing assumption when it landed. Not discoveries. Useful anyway, and useful independently of everything that follows.

---
