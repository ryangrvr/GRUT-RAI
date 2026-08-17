# Where the Responsive Vacuum Stops

*A negative-results report on a program that modelled the gravitational vacuum as a medium with memory, priced every assumption it took, and pushed until it stopped.*

D. Ryan Grover · {{WAVE_DATE}}

> **Correction record, {{CORRECTION_DATE}}.** Part I's first draft failed its mandatory hostile pre-screen (DO-NOT-SHIP): I.1 overstated two priority claims and contained a physics error in its gauge fence. The section was left standing under a do-not-cite banner rather than pulled, then corrected: I.1 is now one third its drafted length and claims nothing beyond the literature it cites; the register nodes that carried the same over-scoped clause were corrected **first**, with the source read (arXiv:2507.03103) that the register itself had flagged as owed. The full trail — draft, verdict, correction — is in the repository history.
>
> **Published in parts.** Complete as of {{WAVE_DATE}}: the front matter, the note on the
> prior deposit, **Part 0**, **Part I** (corrected; see the record above), **Part II**
> (its figure enters with the figures wave and is marked in place), and **Part III**.
> **Outstanding:** Parts IV through VII, the appendices, and all figures. The outline is fixed and lives in the
> repository; the sections not listed as complete **do not yet exist**. This line is updated
> at the close of every wave, and a document silent about its own completeness would be the
> last uncaught instance of the pattern this document is about.

---

## Abstract

**This is a negative-results report.** A framework treating the gravitational vacuum as an open medium with finite memory — one in-in (Schwinger–Keldysh) influence action, its response kernel decomposed on Barnes–Rivers spin projectors — was built, priced assumption by assumption, and pushed until it stopped. This document states where it stopped.

Three results outlive it, and two are about general relativity rather than about this framework. **First:** linearized Einstein–Hilbert is *not* transverse-traceless. Diffeomorphism invariance buys transversality but not tracelessness; the kernel is ½k²[P⁽²⁾ − 2P⁽⁰ˢ⁾], so the scalar sector survives the Ward identity at an exact ratio P⁽⁰ˢ⁾/P⁽²⁾ = −2 — which means the pure-TT ansatz this framework was built on is a **choice**, not a theorem, and it is priced as one. **Second:** the thermodynamic arrow decomposes — an open medium's arrow *exists* intrinsically, while its *direction* is imported from the bath's state, so the framework sharpens the Past Hypothesis rather than dissolving it. **Third:** the anomaly action that was supposed to fix the framework's one free parameter was computed and **fixes nothing** — it yields a scale, not a number.

The framework produced **no novel positive prediction**; the register's `derived` tier holds **{{tier_derived}}** entries. Its single decisive question — whether the assembled low-frequency spectral density ρ_TT(ω→0) = 2 Im G_R^TT of the *pure-graviton* de Sitter self-energy has a relaxation pole or a branch cut ([arXiv:2103.08547](https://arxiv.org/abs/2103.08547), [2107.13905](https://arxiv.org/abs/2107.13905), [2602.07908](https://arxiv.org/abs/2602.07908)) — was drafted as a one-page ask **and never sent**; later in-house work suggests it may be **ill-posed** in the formalism its intended readers use, since that corpus never reduces Σ(x;x′) to a time difference and so has no ω at all.

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

# Part 0 — Why anyone would model the vacuum this way

## 0.1 — The complaint against an inert vacuum

The quantum vacuum, as measured, is not inert. It polarizes: the effective electric charge runs with distance because the vacuum screens it, and the Lamb shift sits in the hydrogen spectrum — in the standard, ordering-dependent picture, because the vacuum's fluctuations move the electron. A force between uncharged plates — Casimir's — is measured to high precision, though whether it measures vacuum energy or the plates' mutual polarization is itself argued (Jaffe 2005) — a caution worth remembering every time this Part leans on an analogy. And an accelerated detector is predicted to find the vacuum thermal — the Unruh temperature, standard but unobserved. All of this is standard physics — the first items textbook QED, the Unruh prediction free-field theory for accelerated observers — and the measured effects are uncontested, whatever their interpretation: the vacuum, as measured, responds.

The question this program asked is one step further. Elsewhere in physics, response comes tied to dispersion and — somewhere in its spectrum — to loss. The textbook dielectric polarizes instantly; every real dielectric has dispersion — its polarization lags the field, carries a memory of it, and dissipates. A viscoelastic solid is the mechanical version: it pushes back like a spring at short times and flows like a fluid at long times, and the connection between the two behaviours is a memory kernel. Instant, lossless response — response with *zero* memory — is an idealization no measured medium realizes exactly: response comes with dispersion, and dispersion — by Kramers–Kronig — with absorption somewhere in the spectrum. The complaint against an inert gravitational vacuum is simply that "inert" asserts the zero-memory limit exactly, for the one case where it is checked far less stringently than in any laboratory medium — binary-pulsar damping and GW170817 bound it; they do not probe it as a dielectric is probed.

What is that analogy worth? One thing only: a question precise enough to fail. An analogy between the vacuum and a viscoelastic medium licenses no conclusion about gravity — media are made of parts, and whether the vacuum is "made of" anything is exactly what nobody knows. The entire worth of the intuition is whether it can be turned into a definite mathematical object with a definite parameter space and definite exclusion rules, so that the world can say no to it. Part II writes that object down; Part III reports where it stopped.

The idea itself is not new, and that comes first. Sakharov (1967) proposed that gravity is not fundamental but *induced* — the metric's stiffness an effective elasticity of the vacuum, paid for by the matter content at high energy. Jacobson (1995) derived the Einstein equation as an *equation of state*, thermodynamic rather than fundamental, from horizon entropy and the Unruh temperature. The analogue-gravity program (Unruh's sonic horizons onward; Barceló–Liberati–Visser for the survey) exhibits laboratory media — flowing fluids, condensates — in which effective metrics and horizons demonstrably arise, and Hawking-like radiation is reported, its thermality still argued. (The lineage citations here carry the same verification scope as Part I's priority references: verified through secondary literature, not read in original.) A vacuum that behaves as a medium is a decades-old hypothesis; the lineage above is its record. What this program put on top of that lineage is not a new idea but a bookkeeping discipline — every assumption priced, one of them late, caught by the program's own screen; every derivation gated — and whether *that* was worth anything is Part VI's question, not this section's.

## 0.2 — What a memory would buy

If the gravitational vacuum relaxed with finite memory, three things would follow — and each is stated here as a hope, a direction of search, not a result.

A cosmological constant that is not constant: late-time acceleration as a medium still relaxing, its slow approach to equilibrium doing the work the bare constant does in the standard picture. A structural home for gravitational dissipation: an open medium's response and its noise are locked together by the fluctuation-dissipation relation everywhere in equilibrium physics, so gravitational-wave damping and gravitational noise would arrive as one package with a defined shape, wherever the medium is near equilibrium, rather than as free inventions. And a setting where the arrow of time's machinery becomes load-bearing: an open medium *has* an arrow, and a framework built on one must say precisely where that arrow comes from — an obligation Part I.2 reports in full.

That is the hope, in full. The parts that follow report what pursuing it produced: no novel positive prediction, several exclusions, and a small number of results that outlive the framework — most of them results *about the hope's own limits*.

## 0.3 — What it costs before anything is derived

The entry price — most of it paid up front, the last item priced late, after the program's own adversarial screen caught a theorem consuming it unpriced: the division of the world into a slow metric and a fast bath; the restriction of the bath's influence to Gaussian order; the background's causal structure, taken as given; and the covariant availability of the gauge-orbit identity that late-caught theorem leans on (the theorem is Part II.1's). Each is a named input booked under the founding ledger entry (`rung1_inin_action` in `provenance/claims.json`); none has a derivation exhibited from anything above it; the last carries an explicit condition for its own retirement. Everything claimed for the framework below is downstream of that purchase, and no framework result is stronger than it. Part I's two results are the deliberate exception — they hold whether or not the purchase was worth making.

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

# Part II — The framework, written down

## II.1 — The premise as mathematics

> **In one sentence, for readers who skip this section:** the framework is a single quadratic influence action for the metric perturbation on a doubled time contour — a dissipation kernel and a noise kernel, each carried on the spin-2 and scalar tensor structures, a restriction that is a family-conditional theorem resting on one priced input, not a gift of the symmetries — and that action *orients* (a sign floor, x_diss(ω) ≥ 0 pointwise — never a value) its one free scalar ratio, x, without ever fixing it.

The system is the metric perturbation h_μν on a declared background, doubled in the in-in (Schwinger–Keldysh) way that open-system physics requires: one copy for each branch of the time contour, or equivalently an average field and a difference field. The bath — the vacuum's fast degrees of freedom, the metric's own fast modes included — is **integrated out and deliberately not specified**. It is the framework's priced frontier: the bath's one structural property that matters (the shape of its memory) is exactly the question the program drafted for outside help and never sent (Part IV).

The symmetries imposed are declared as an inventory, and nothing beyond the inventory is available: retarded causality; truncation at quadratic order; the system/bath division itself; the equilibrium (KMS) condition with matrix passivity — whose fluctuation-dissipation lock, noise tied to dissipation channel by channel, is that condition's *consequence*, the ledger's assumption-removing event, not a separate imposition; diffeomorphism invariance **with its corrected, narrower scope** — dissipation necessarily breaks the doubled diffeomorphism symmetry down to its diagonal (Salcedo–Colás–Dufner–Pajer), so the surviving identity buys transversality on one slot of the response kernel only, not the exhaustiveness an earlier version of this framework's documentation claimed; background homogeneity and isotropy with their inherited parity-evenness; and the Onsager pair symmetry. Linearized Weyl invariance is *not* on the list and not available — the framework imports the trace anomaly, which is the statement that Weyl invariance is broken.

At quadratic order, at fixed frequency and wavenumber, the action is then

    S_IF[h_r, h_a] = ∫ h_a · K_R · h_r + (i/2) h_a · N · h_a

— a retarded dissipation kernel and a noise kernel, each decomposed on the spin-2 projector P⁽²⁾ and the transverse scalar projector P⁽⁰ˢ⁾. Each channel's coefficient obeys: upper-half-plane analyticity (causality); the KMS lock in equilibrium, noise tied to dissipation channel by channel; and passivity — no channel may amplify at any frequency, with no cross-channel rescue. The restriction of *both* kernels to those two structures has a history: after the correction recorded in Part I it stood as a **declared restriction**, not a consequence; it has since been shown in-house to be a **theorem on the framework's own admissible family, conditional on one priced input** — the covariant availability of the gauge-orbit identity, the ledger's newest entry — with positivity doing the closing work the broken symmetry could not. The same positivity closes the spin-2 dissipation channel at spacelike momenta on the same family — the closure rides the same priced input, and tensor-sector spacelike support would require the medium frame the framework's covariant family excludes. Outside that family — noise decoupled from dissipation, non-thermal occupations — a strictly larger operator space exists (Salcedo–Colás–Dufner–Pajer's open-gravity construction) and is fenced at its point of entry. One structural conjecture remains deliberately open and labelled: that the memory is *finite* — a single relaxation pole rather than a branch cut. That is the framework's load-bearing conjecture, it is external, and Part IV is about it.

One anchor sets the scale: general relativity's own kernel, ½k²[P⁽²⁾ − 2P⁽⁰ˢ⁾] — its scalar component, twice the spin-2 one in magnitude, is Part I's first result made structural, and GR itself refuses the pure-spin-2 idealization. And the scalar modulus is given a name: x, the scalar channel's coefficient normalized to the trace-only endpoint — the configuration whose scalar channel couples to the trace alone (x = 1) — **declared a function of frequency and wavenumber rather than a constant**, because nothing in the program's corpus forces it constant and pretending otherwise would smuggle a dial.

The landing: **the action does not fix x.** What it forbids is real — anti-passive response in either channel at any frequency; noise detached from dissipation in equilibrium; acausal kernels. Two further exclusions have homes outside the action and are recorded at their own strength: the trace-only endpoint x = 1 at constant x, excluded by a partly empirical export (the register's `mu_linear` no-go), not by the action's conditions; and — held at to-derive by the register's own ruling, conditional on the single-pole conjecture this paragraph just declared open, and generic where it holds (Vikman 2005) — the statement that a single passive channel cannot cross the phantom divide. What the action itself does not forbid is recorded with equal weight: any amplitude of either modulus, any nonnegative value of x, any frequency- or wavenumber-structure compatible with the conditions above. The action carries a *family*. "Responsiveness" means exactly this list — a doubled rank-2 field, this inventory of symmetries, two kernel channels with these analyticity, balance, and positivity conditions, one adopted dimensionless axiom (α, the anomaly normalization, conditional-theorem grade), one open conjecture (the single-pole memory, external), one hand-chosen point (x = 0 constant — the pure-TT choice, priced in the ledger), and one unfixed function. Anything attributed to "responsiveness" that does not follow from that list is an insertion, and the register books it as one.

## II.2 — What it bets

The postulate map sorts every input by kind, and the sort answers "what is this framework actually betting?" *(The figure for this section — the postulate sort drawn as a map — enters with the figures wave; the completeness line above tracks it.)*

**Bedrock: posits that are not even candidates for derivation.** The medium ontology itself, with its division into slow metric and fast bath — the bet, and a framework must bet something. The low-entropy past boundary — Part I.2 is the demonstration that, in every case surveyed, the arrow's *direction* is imported rather than dynamical — so the framework imports it, priced. And the Born measure: decoherence machinery selects a pointer *basis*; it does not by itself supply the outcome *probability*; the probability rule is inherited. The discipline's claim about these is not "unsolved" but "un-derivable in every case surveyed" (Part I.2's scope): surveyed derivation claims relocate the input; they do not remove it — and counting a relocation as a removal is the laundering the register books (laundering — deriving with an input the derivation does not declare).

**Open layers: assumed today, each with a named path to discharge.** The bath's memory shape — pole or cut, the framework's one decisive external question. The pure-spin-2 choice — the symmetry route to forcing it is *closed* (Part I.1); a dynamical route through the bath survives, at the recorded cost that it would relocate the assumption rather than remove it. The general action carries x free; the framework's cosmology exports were computed at the hand-chosen point x = 0 — the pure-TT choice — and that point, not the family, is what this open layer names. And the covariant gauge-orbit availability — the entry booked while this document was in preparation, which is booked to retire into the operator basis's reserved covariant completion — the register's named placeholder for that work — if and when it lands, in-house or in the literature.

**Borrowings, with the loan recorded: things the framework does not host.** General relativity itself is *recovered with imports*, never derived — the memory-to-zero limit collapses the kernel to a local form, and the recovery leans on horizon area and the Unruh temperature, both priced. Each program surveyed pays somewhere: Jacobson pays with horizon thermodynamics, Sakharov with the high-energy matter content. And the anomaly-to-amplitude bridge — the hope that the trace anomaly would normalize the spin-2 response — is settled negative on sector orthogonality: the two anomaly coefficients live in different channels (the a-anomaly reaches the spin-0 channel only, the c-anomaly the spin-2 channel only), their ratio is the coefficient of neither, and no metric-built object carries it across.

**Results, never inputs.** The fluctuation-dissipation lock — an entry that *removed* an assumption (the register's negative ledger event, `rung2_kms_gate`). Linear cosmology in the ΛCDM shape — held not by derivation but by a partly empirical exclusion the framework exports against its own naive modification; derived-pending, leaning on the pure-TT point and carrying that conditionality. The no-crossing statement — a single passive channel cannot cross the phantom divide (the second law fixes the side, not the slope) — held at to-derive, gated on the single-pole question, generic where it holds (Vikman 2005). The map's reading rule: a bedrock item claimed as derived is laundering; an open layer that graduates is a real ledger event; a borrowing sold as hosted is an over-claim; a result counted as an input is the category error the register's gate exists to catch.

One sentence for the whole bet: **a medium taken at Gaussian order on a given causal background, a boundary condition, and a measure — everything else is either open with a named discharge, borrowed with the loan recorded, or output.**

## II.3 — The whole story, with the holes marked

The register's story is authored where it must be and generated where it matters: the stage-to-claims mapping is the construction — authored — and every link's status is computed from the claims, not narrated over them. The chain, from origin to observers, at a glance — the status marks exactly as generated:

> origin → medium → persistence → arrow ∥ thermality → gravity → quantum → classicality ∥ structure → dark energy → matter (SILENT) → observers (UNPOSED)

The marks are the content. Two pairs of links are *concurrent* (∥) because forcing them into sequence would be a readability lie: the arrow and thermality are one fact doing two jobs, and decoherence of cosmological perturbations happens *during* structure formation — the two do not cleanly separate. One link is **SILENT**: no node in the framework's scope books the Standard Model's spectrum or couplings as a claim — the chain's matter link (persistence's far neighbour) is empty, and the chain says so in capitals rather than tidying the hole away. One link is **UNPOSED**: how observers arise has never even been asked in the register, and the chain ends by admitting it.

What the generated statuses show, read as a whole: the original content clusters in the middle. The memory kernel, the fluctuation-dissipation lock, the arrow decomposition — the links where the open-system toolkit actually grips — carry the program's own contributions. Both ends are borrowed or empty: the origin link is pure import (the past boundary), and the far end is silence. The framework is a **middle-of-the-story framework**, strongest exactly where dissipation, memory, and detailed balance do work, empty where they have nothing to hold.

And one structural fact the chain surfaced: the story's strongest joint — the node shared between the arrow and thermality links — is the same node as the ledger's assumption-*removing* entry (`rung2_kms_gate`). The place where the narrative is most load-bearing and the place where the accounting ran negative coincide. The shared node is the authored mapping's; its negative ledger entry is the register's — both halves are checkable.

The chain also keeps its own books: every claim in the framework's scope (the GRUT nodes) is either placed in a link or listed off-chain with a reason, and the generator errors if one goes missing. The full artifact, statuses and all, is `EMERGENCE_CHAIN.md` in the repository, regenerated on every register change; this section is a reading of it, and where the two disagree, the generated artifact wins.

---

# Part III — Where it stops

**Every entry in this Part is a statement about the framework as written, not about nature.** That sentence governs everything below and is promoted here, to the chapter head, so no boundary can be read as a discovery about the world.

## III.0 — How to read a boundary

A boundary on your own model is a debugging note. It says: *this construction, with these declared inputs, cannot reach that place* — and nothing about whether the place exists. Debugging notes are what a biting gate produces — though whether *this* gate bit is not assertible from here: the earned strengths on each entry below, and the pressure record in III.3, are the checkable evidence either way. That is why this Part sits inside the physics rather than in an appendix of caveats: the boundaries *are* the output.

They come at distinct earned strengths, and the strengths are not interchangeable. The strongest label the ledger defines — **FORBIDDEN**, a structural impossibility within the framework's axioms — **is banked by nothing in this register.** Say it in the legend, because the absence is load-bearing: the strongest exports here are *settled-negative* (no known route, a strong obstruction, a named rescue left open), *excluded* (killed by data plus structure, not impossibility), *invisible-by-suppression* (real but unobservably small), and *borrowed* (not derivable from this machinery; imported and marked). One further label appears below — *not earned*, an economy claim unavailable at the framework's current strength, classed with settled-negative and carrying a named rescue. Over-grading a no-go — promoting an obstruction to an impossibility — is the exact failure mode this program polices, and the prior deposit committed it with an entire tier.

## III.1 — The containment results, entry by entry

Each entry below is transcribed from the no-go ledger (`NO_GO_LEDGER.md`) at its earned strength, names its register home and tier, and ends with what it imposes on any completion. The tiers matter as much as the strengths: several boundaries are themselves held open by the register — a boundary can be no better established than the claims it stands on.

**The anomaly-to-amplitude bridge — SETTLED-NEGATIVE, not forbidden.** The hope that the conformal-anomaly ratio normalizes the spin-2 response amplitude is settled negative on a primary obstruction of sector orthogonality — computed, exact: the a-anomaly reaches the spin-0 channel only and the c-anomaly the spin-2 channel only, so the ratio α = a/c is a ratio of coefficients living in *different* channels and the coefficient of neither, and no metric-built scalar-to-spin-2 intertwiner exists to carry it across — with independent Ward-identity and RG-protection obstructions behind it. The fluctuation-dissipation lock fails to rescue it (the would-be normalization cancels out of the lock), but that is a failure to rescue, not a fourth obstruction. The α *value* is untouched: a/c = 1/3 is standard physics as a conditional theorem — *if* the conformal mode is the response's infrared carrier, then α = 1/3 (`rung9a_value`, tier shown); what the framework adopts, axiom-grade, is applying that identification as its normalization. Only α's *role* as the kernel normalization is settled negative (`rung9b_bridge`, tier assumed, sub-status settled-negative). Impossibility in every extension is *not* claimed. **Spec for a completion:** supply a new operator identity — a legitimate scalar-to-spin-2 intertwiner — or accept the amplitude as an external input.

**The naive growth modification — EXCLUDED, a hybrid grade: structural plus joint empirical at the ~4σ-class weight attributed by the no-go ledger.** The super-horizon growth modification the framework's own conformal coefficient naively suggests is dead twice over: a separate-universe consistency argument (conditional on adiabaticity and a named dilatation bridge), and a joint empirical disfavoring — the recomputed cross-correlation tension at {{isw_sigma}}σ ({{isw_central}} central; the prior deposit's advertised figure in this channel is retired as impossible there) together with an independent lensing-amplitude tension at {{desi_sigma0}}σ. The register home is `mu_linear`, tier **derived-pending** with an armed trigger: if the bath's trace (spin-0) correlator is established nonvanishing — closing the last route to deriving the scalar sector's vanishing — the tier demotes by its own recorded rule. The endpoint exclusion itself is p_tt-independent: it survives even if that trigger fires. What leans on the pure-TT point is the *surviving* statement — "linear cosmology in the ΛCDM shape," which holds given the chosen scalar coupling and is empirically *selected*, not derived. **Spec:** derive the scalar sector's vanishing from the action (the symmetry route is closed — Part I.1; only the bath route survives, at a recorded relocation cost) or accept the choice as an input.

**An economical evolving dark energy — NOT EARNED.** A single-parameter evolving equation of state matching DESI's evolving-w evidence is not available to a single passive relaxation channel: one passive mode stays on one side of the phantom divide — the line w = −1 that the data's preferred history crosses — (generic where it holds — Vikman 2005 — and conditional on the open single-pole conjecture; the register holds the no-crossing at tier **to-derive** across its homes `rung7_wz`, `rung7_w2_wa_sign`, `rung7_w3_nocrossing_export`, by its own ruling that a no-go cannot outrank its anchor). An earlier "wrong sign" reading of the evolution slope was retracted — the slope's sign is indeterminate at the current frontier, fixed by nothing yet banked; the second law fixes the *side*, never the slope. The framework's sourced statement is a flat equation of state at the divide; matching an actual crossing would cost a genuine second slow mode and the parameter that comes with it — which is the economy the claim was trying to keep. **Spec:** supply that second, cosmologically slow, sign-changing mode, and pay for it.

**The tabletop decoherence falsifier — INVISIBLE-BY-SUPPRESSION, quiet or faint.** The framework's qualitative wedge against collapse models — energy-basis rather than position-basis decoherence — is real as a distinction and fails as an observable: the dominant coupling commutes with the system Hamiltonian and samples the noise spectrum at zero frequency, where the framework's assumed bath spectrum vanishes (quiet); the wedge-carrying couplings survive, suppressed by seven to tens of orders of magnitude below current sensitivity (`calc/q1_energy_basis_magnitude.py`) (faint). Register: `rung8_falsifier`, tier **to-derive**. Observability would require staking the noise amplitude roughly ~10⁷× above its natural value at the current matter-wave bound — a tuned number. **Spec:** a leading off-diagonal energy coupling at order unity, or a bath resonance that lifts the magnitude; otherwise this falsifier cannot carry the program.

**Gravitational-wave dissipation as a signature — INVISIBLE-BY-SUPPRESSION.** The dissipative dephasing of gravitational waves is real — absent in lossless GR — and sits tens of orders of magnitude below any detectability threshold; the GW170817 speed bound is satisfied with room to spare. The suppression is the same Planck suppression that makes the framework solar-system-safe: a feature of the construction, not a tuning, and also the reason it cannot be seen. Register: `rung4_love_kk`, tier **shown** (the kernel structure), with the magnitudes in `calc/gw_dissipation_bounds.py`. **Spec:** a bath resonance or collective infrared mode lifting the response into the live window — nothing in the corpus supplies one.

**Deriving general relativity — BORROWED.** The in-in machinery does not select the Einstein–Hilbert action; the diffeomorphism identity constrains conservation, not the action, and whole families of actions satisfy it. The recovery in the zero-memory limit leans on horizon area and the Unruh temperature, both imported and priced (`rung5_gr_limit`, tier **assumed**). On current footing the gravitational sector is a member of the emergent-gravity family, not a from-scratch derivation. **Spec:** the microscopic input that fixes the coupling and the derivative expansion without importing the area law — an open, hard program.

**Deriving the Born rule — BORROWED.** Integrating out the bath reproduces the Schrödinger core and selects a pointer basis; a preferred basis is not outcome selection, and the probability measure is inherited (`rung6_qm_limit`, tier **assumed**). The decoherence *rate* is a genuine output; the *rule* is a postulate the framework carries like everyone else. **Spec:** the outcome measure itself — decoherence is necessary, not sufficient.

That is the full list — nothing at FORBIDDEN, and saying so is part of the list.

## III.2 — The one empirical surface: a ceiling with no floor

Exactly one place in this framework is *actively bounded* by current data — a live parameter constrained from above, as distinct from an endpoint killed or a signature suppressed below any contact — and its shape invites misreading in both directions, so it is stated here with its qualifiers.

The pure-TT choice closed the naive scalar channel; the interior it foreclosed is now an explicitly parameterized family — the scalar modulus x of Part II, running from the pure-TT point to the excluded trace-only endpoint. The computed record on that family: the lensing bound admits the interior below a ceiling of roughly {{x_upper}} in x — computed at central input values and read at the loose (conservative, upper) edge of the register's declared uncertainty fence — corresponding to a growth-modification allowance (μ−1) of up to roughly {{mu_allowance}} at the edge. An owed calculation (the low-multipole temperature auto-correlation channel, estimate-grade today) is expected to tighten it, and it is the register's standing gate for any interior-viability claim above roughly {{x_gate}} in x — compatibility above that mark is provisional on it. And the family has **no floor**: nothing in the framework, the register, or the data pushes x away from zero. The strongest attempt to draw one — the computed anomaly action, the abstract's third headline result — yields a scale, not a number (`calc/anomaly_c0_map.py`), so the floor stayed undrawn. The family *allows*; it does not predict.

That asymmetry is the central content of this surface, and both directions of misreading are live. Read as a prediction band, the allowance is a fabrication — there is no lower edge, so there is no band, and the corresponding figure is refused on exactly those grounds (a drawn ceiling over an undrawn floor reads as a band no matter the caption). Read as a null result, it is also wrong — the framework is *not* excluded on this surface; the tension the data does show (the lensing-amplitude tension at {{desi_sigma0}}σ, independent of the retired channel) bounds the family from above and says nothing below. The honest sentence is unexciting: the interior family is compatible with current linear cosmology anywhere under its ceiling (provisionally, above the standing-gate mark, until the owed calculation lands), and the lensing-amplitude tension the ceiling comes from may itself be fully compatible with the framework — the register cannot yet say otherwise.

Two corrections sharpen this surface, both against the framework's convenience. First, x is not a number. The action declares it a function of frequency and wavenumber, and nothing in the corpus forces it constant; every "one free parameter" description — this document's own abstract included — therefore *understates* the freedom, and the constant-x window above is a one-dimensional cut through a function space — every number quoted on it carries that cut-conditionality, recorded in the register. Second, the boundary's flagship version was demoted by the program's own audit: the sharper bound once derived in the low-multipole temperature auto-correlation channel is family-conditional and contaminated by the very insertion it tested, so the loose reading above is what survives. The ceiling is real; everything sharper is conditional.

## III.3 — The times the machinery fired against the author

The boundary list above is only as credible as the pressure that shaped it. This section is that pressure's record, inside the physics Part on purpose: these occasions are the reasons to believe III.1 says what the register says rather than what its author wanted. The occasions are data (`provenance/construction_pressure.json`) — the front matter's count of them is emitted from that file, and each is checkable. All are from this document's own construction. They are told in one tone, in order.

**The independence claim.** The author wrote that the program's adversarial passes are "independent." The hostile pre-screen removed it: the passes are the same operator, the same model family, no human in the loop but the author — precisely the credential the front matter spends a paragraph refusing. The document now says so instead.

**The blocking claim.** The author wrote that results are attacked "before they may be banked." The pre-screen, checking the claim against the gate's own code, removed it: the gate exits cleanly on a flag — it surfaces work, it does not withhold anything. The phrasing implied a lock that does not exist, and the mechanism section now states what the gate actually does.

**The no-typed-counts claim.** The author wrote "no count in this document was typed by hand" — and the claim was falsified inside its own paragraph, where spelled-out numerals and hyphenated ratios had walked past a guard that checked bare integers only. The guard was rebuilt to see word-forms and ratios, and the rule's statement now names its enforcement and its exceptions.

**The attribution claim.** The author wrote that the register's authority-flavored records "all trace to sessions the author ran himself." The adversarial search removed the claim as stated: the register proves the *absence of a logged transmission* and never records who or what ran a session — so the second half is the author's testimony, and the document now labels it as testimony rather than as a checkable fact.

**The priority claims.** The author wrote a first draft of Part I.1 carrying two novelty claims and a gauge argument. The mandated pre-screen returned do-not-ship: one novelty was inverted by published work the register itself had flagged as owed reading, the other was refuted by the cited literature's own organization of the material, and the gauge argument transcribed a fact from one setting into another where it is false. The register was corrected first; the section shrunk to a third of its drafted length and now claims nothing beyond the literature it cites; the trail is in the correction record at the head of this document.

One caution about reading the pattern: the file's own admission rule guarantees the direction — an occasion enters only when a pass removed a claim the author wanted — so the consistency is the selection criterion, not a finding. What the record evidences is existence, number, and checkability: the machinery fired, repeatedly, on this one document's construction, and each firing is inspectable. A gate that only ever confirms is decoration; the record, not the assurance, is the evidence that this one does not.

---
