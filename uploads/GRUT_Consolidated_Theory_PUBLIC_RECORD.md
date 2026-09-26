# GRUT — Grand Responsive Universe Theory
## Consolidated Theory, Formal Architecture, Results, Limits, and Completion Program

## Record information

| | |
|------------|----------------------------------------|
| **Author** | D. Ryan Grover (independent researcher) |
| **Document** | Consolidated Research Record 02 — public-record edition |
| **Date of this version** | 26 September 2026 |
| **Earlier version** | the 25 September 2026 draft, preserved as `uploads/GRUT_Consolidated_Theory_2026-09-25_DRAFT_as_received.md` |
| **DOI (this version)** | 10.5281/zenodo.22983638 |
| **Concept DOI (all versions of the theory record)** | 10.5281/zenodo.19803663 |
| **Software and provenance archive** | GRUT-RAI, all versions: 10.5281/zenodo.18993689 |
| **Repository** | `https://github.com/ryangrvr/GRUT-RAI`, branch `master-w25bu9` |
| **Source boundary** | commit `6abbf3164655c513b72dfc72f4a64013b061c489` (25 September 2026, 21:54 UTC−5; 26 September 2026, 02:54 UTC) |
| **Foundations record** | branch `adjudicator-track` @ `90218f5`, archived byte-exact in `archive/adjudicator-track_90218f5/` |
| **License** | CC BY 4.0 (text and deposit); source code also available under MIT |
| **External peer review** | none |
| **Experimental validation** | none |
| **Confirmed novel predictions** | none |

**Source boundary, stated fully.**
- *What it covers.* This manuscript consolidates the GRUT record on
  `master-w25bu9` through commit `6abbf316`. It also relies on the
  foundations record on `adjudicator-track` (tip `90218f5`), which this
  release archives byte-exact because the branch is not merged
  (Section 28).
- *The RRP line.* `master-w25bu9` forks from the repository's `master`
  branch at commit `a2dcb02` (24 September 2026), the RRP program
  synthesis. The RRP records are therefore in the source history. Their
  results enter this theory only through deliberate source inspection,
  scope classification, and owner adjudication.
- *Other branches.* The public repository has other branches (`main`,
  `physics-final`, `v4`, `v2`, `v1-retired`, `testingi-rrt`,
  `rrt0-phase2`). They are not sources for this record except where cited
  by commit.
- *This file's own commits.* The manuscript and its release tooling were
  committed after the source boundary. They add no computation and change
  no status.

**Epistemic boundary.** This is an in-house research record: computations,
formalizations, and owner rulings, each at its declared scope. No external
peer review is claimed, and no experimental validation is claimed. No
outside human reviewer has checked any GRUT-specific result.

---

## Notice: correction and supersession of an earlier deposit

This version is deposited under the same concept DOI (10.5281/zenodo.19803663)
as earlier GRUT work. Among those earlier versions is *Grand Responsive
Universe Theory GRUT ToE v4.0 — The Emergence of Everything — Candidate
Framework* (version DOI 10.5281/zenodo.20783057, deposited 21 June 2026).
**The claims of that deposit are withdrawn. It is substantially wrong, and
nothing in it should be cited as a result.** Its author's own supersession
notice gives the record:

- A later verification pass scored it 1 of 18 on its verifiable numbers,
  0 of 7 on its falsifiers, and 1 of 11 on its scorecard rows.
- Several of its lines did not survive:
  - its dark-matter substrate line;
  - its two-anchor hierarchy ledger;
  - its claimed unified no-go;
  - its entire "forbidden-by-theorem" tier.
- Two of its headline claims fail outright:
  - Its advertised 32σ exclusion recomputes to about 2.0σ, and the
    mechanism it rested on had the wrong sign.
  - Its "689 Hz, zero free parameters" falsifier does not exist as
    advertised.
- Its title carried the phrase "Theory of Everything". This record does
  not.

The later *Program Record* release of 7 September 2026 (Books I–X, working
edition) retired the theory-of-everything claim. The de Sitter
absorptive-response paper is the previous version of this record and
remains a standalone standard-QFT result (Section 24.1). Where any earlier
version in this lineage conflicts with the present record, the present
record's scoped statements govern. Section 29 gives the full release
history.

---

## What this is and what it found

GRUT began as a hypothesis about gravity. The hypothesis was that the
gravitational vacuum behaves like a responsive material with memory: empty
space responds to what happens in it with a delay, rather than instantly.
That idea gives the program its name.

Its strongest form, a vacuum memory with a single characteristic time, did
not survive: exact de Sitter free-field calculations produce memory with no
single time scale. In September 2026 the program's own adjudication found
that the framework, as then scoped, "fails to constitute a distinctive
physical theory", which is not a finding that its hypothesis is false. The
program was closed on 23 September and reopened on 25 September with a
narrower question.

This record answers that narrower question: **in explicit model systems,
what structure appears on its own, and what must be put in by hand?** The
models are mostly networks of coupled oscillators (masses and springs, or
their overdamped analogues) plus small quantum spin systems. Each is only
partly observed: some degrees of freedom are watched, and the rest act as
a hidden environment.

**Found, within the tested model classes only:**

- **Memory and irreversibility from local dynamics.** Hiding part of a
  local network gives the visible part an exact memory. As the network
  grows, its response becomes effectively irreversible, and the lattice
  dimension sets the long-time form of the memory. The direction of time
  is not derived.
- **Averages and noise are not the whole story.** Higher-order
  correlations can distinguish environments that agree on both the average
  response and the noise.
- **Access decides what can be learned.** With rich access to the hidden
  network, its dimension and distances can be reconstructed. From a single
  site, genuinely different networks look identical.
- **Changing networks need two-time memory.** When the network changes in
  steps, the memory depends on two times, not only on their difference,
  and no single-time description packages it. The smooth and infinite-size
  cases are open.

**Not found:**

- No experimentally confirmed prediction. The program's own ledger of
  GRUT-specific derived predictions stands at zero.
- Planck's constant, the Born rule, and quantum noncommutativity are
  inputs, not results.
- Gravity is not derived. A route toward a graviton-like response works
  only if several structural inputs are supplied by hand. Among them are a
  massless graviton-like field that reaches every sector, and a light cone
  shared between sectors. Several pre-registered tests along that route
  failed and remain on the record.

**How the work was done.** Much of the mathematics is standard
open-systems and spectral theory. The program's contribution is
pre-registered, in-house verification within these classes, and a precise
map of what depends on what. The computations were run largely by AI
agents under the author's direction, and the author ruled on each status.
No outside human has reviewed any GRUT-specific result.

This record is not a completed theory, and it is not a theory of
everything.

## Abstract

GRUT (Grand Responsive Universe Theory) is a research program. It asks
whether local microscopic models can generate continuum, influence,
geometric, and gravitationally relevant effective structures without taking
those structures as primitive. This record consolidates the program at a
deliberate pause. Its central result is a dependency-resolved hierarchy:

$$
\mathcal O_{\rm local}\longrightarrow\mathcal C_{\rm continuum}\longrightarrow\mathcal I\longrightarrow\mathfrak A\longrightarrow\mathcal G\longrightarrow\mathcal F_{\rm eff}\longrightarrow\mathcal G_{\rm grav}.
$$

The access structure $\mathfrak A$ is a cross-cutting condition, not a
single link. It fixes which subsystem is retained, which distinctions can
be reconstructed, and where boundary events make hidden differences
observable.

**The core.** In the tested classes, eliminating the hidden modes of a
finite local network gives the retained part an exact memory kernel. The
infinite-volume limit gives continuous spectra and effectively
irreversible response. Lattice dimension sets the late-time decay of the
memory. These limits are graded as family-level facts, not general
theorems. The direction of the arrow of time is supplied, not derived.

**Influence.** In the declared Gaussian class, realizable response and
noise spectra obey $J\ge0$ and $\nu\ge\hbar J/2$. This is standard
Caldeira–Leggett-class realizability, verified in class, with $\hbar$
located as the height of the fluctuation floor. The pair $(K,N)$ is not
the whole interface: higher connected cumulants separate environments with
identical two-point data. Positivity of the full influence hierarchy is
ordinary state positivity, a restatement rather than a new principle.

**Access and geometry.** A distinction is physical exactly as far as it
changes accessible influence data, and the access seed itself is supplied.
In the tested classes, rich access reconstructs the hidden network's
geometry, including the elimination of isospectral impostors. Restricted
access leaves distinct geometries indistinguishable. Geometry here is
access-relative, never absolute.

**Nonstationarity.** The core construction extends, in class, to finite
networks whose couplings change in steps. The reduction is exact to
$10^{-12}$ and continuous with the stationary case. A separately
pre-registered test certifies that no single spectral measure and no
function of the time difference alone packages the resulting two-time
memory. The first test's two packaging gates failed and remain
permanently red.

**Gravity.** A route toward a gravitational identification was attacked
one assumption at a time. Still supplied are the access seed and a
coincidence of access seeds (CARRIER), a massless gauge- and
Lorentz-redundant probe, universal reach, a co-stretch (unit-change)
declaration, and a cross-sector light cone. Given these inputs, the retained sector is constrained to a gapless,
$z=1$, locally accessible Goldstone-like class. A matter-side dissipation
exponent, $\omega^7$, is within-class occupancy evidence only. Its record
includes an analytic calculation sealed in advance, but also unimplemented
sealed gates and pre-registrations committed together with the result
(Section 17). The forcing ("Class-4") derivation of gravity is open.

**What is claimed.** No confirmed prediction is claimed. GRUT-specific
derived predictions stand at zero, the program's distinctive-theory
adjudication failed as scoped, and seventeen failed pre-registered gates
(ten red-register entries) are preserved. No outside human has reviewed the
work. The achievement is narrower and more exact. Repeated
counterexample-driven attacks have organized a diffuse set of assumptions
into an explicit inventory of eleven named primitive inputs, unresolved
seams, and preserved red gates. Completion is defined as seven typed
mathematical problems, and an input may legitimately remain primitive once
its status is certified.

---

## How to read this record

- **New to GRUT:** read "What this is and what it found", Section 0,
  Section 26, and the ledger of Section 31.
- **Critical specialist:** read Section 32, Sections 4–10, Sections 20–24
  and 31, Sections 12–19, Sections 26 and 29, then Section 28 and
  Appendices D and G.
- **Section 32** gives the strongest supported statement, and **Section 31**
  the full status ledger.
- **Sections 0–3** cover motivation, method, what GRUT claims, its
  relation to existing work, and the formal architecture. **Figure 1**
  (Section 3) is the map of the whole record.
- **Sections 4–11** present the generative core: continuum, stationarity,
  influence, access, geometry, units, and quantum structure.
- **Sections 12–19** cover the conditional gravitational branch.
- **Sections 20–25** give the formal statement, the input inventory, the
  seams, the red register, the completion program, and falsifiability.
- **Sections 26–29** give the non-claims, provenance, and history.
- **Appendix H** is a glossary of every program-specific term. **Appendix
  I** resolves symbols that carry more than one meaning. **Appendix G**
  indexes every campaign fork by commit.

Each result is graded by a fixed vocabulary (Section 1). Numbers are given
with their source, and the repository artifacts decide the status of any
individual claim.

**Two words used narrowly.** In this record, *prediction* means an
empirical prediction about nature; agreements between in-house analytic and
numerical computations are called checks. *Theory* means the program's
current formal construction (Sections 20–24); the program's own
distinctive-theory adjudication failed as scoped (Section 29), and nothing
since has been adjudicated to overturn that grading.

---

# 0. Origin, and why this record is narrower

**The founding hypothesis.** GRUT began as the hypothesis that the
gravitational vacuum is a responsive medium with finite memory. In an
open-system (in-in) description, its retarded response and noise kernels
would carry a single finite memory time $\tau_0$: a single-pole kernel.
The idea was that this would make gravity a universal, memory-bearing
environment to which all matter couples. The program's working identity
followed from it: the *gravitational identification*, the claim that the
persistent continuum generated by local dynamics is physically realized by
gravity. That identification is graded **hypothesis**, not derived
(Section 12).

**What happened to it.**
- The single-pole bet is negated in its strongest form: exact de Sitter
  free-field theory forces scale-free, power-law memory at the computed
  order.
- A distinctive-theory adjudication, run twice on 4–5 September 2026,
  found that the framework "fails to constitute a distinctive physical
  theory". The adjudication records that this is **not** "the
  responsive-vacuum hypothesis is false". GRUT was left unevaluated at its
  own claim point.
- On 23 September 2026 the program was formally closed. On 25 September
  2026 it was reopened by owner ruling as a theory-development effort,
  with a narrower object: *exhibit the mathematics of the theory — show
  how it works — before any external claim is made.*

**Reopening is not rehabilitation.** The reopening ruling states that
every earlier grading stands. That includes zero derived predictions, the
failed distinctive-theory adjudication, the negated founding bet, and the
no-go ledger.

**What this record does.** It reports the dependency campaign run after
the reopening:
- twenty-two chartered forks;
- a formalization;
- a completion attack on the stationarity seam (C1-a and C1-a2).

It asks what structure remains once every assumption the program could
not earn has been removed. It is published at a deliberate consolidation
pause. Later results enter only through a new dated record.

---

# 1. Scope, epistemic discipline, and status vocabulary

The record is maintained under a source-first rule: **computational checks
outrank narrative prose.** A later document describing a claim more
confidently does not make the claim stronger.

**The formal grading vocabulary** (Formalization 01 §0; binding):

- **[IDENTITY]:** an exact mathematical identity. It carries content only
  as a classification.
- **[DERIVED-IN-CLASS]:** established by a chartered instrument within a
  declared model class, at stated tolerances. The class is part of the
  statement.
- **[FAMILY-FACT]:** demonstrated across a tested family of models. It is
  stronger than an example but is not a general theorem.
- **[SUPPLIED]:** a primitive input the program does not derive (Section
  21).
- **[UNDEFINED]:** a composition or object the theory does not currently
  define. The seams live here.

**Other status labels used in the record:**

- **[CONSTRAINED]:** restricted by the evidence but not uniquely selected.
- **[DOMAIN DATUM]:** state, boundary, or regime information explicitly
  typed as data within the theory's domain. It is one of the three
  certified closure statuses (Section 24).
- **[UNRESOLVED]** / **OPEN:** not decided by present evidence.
- **[RED]:** a pre-registered gate failed. **The gate stays red
  permanently.** A separately chartered measurement may establish a new
  result on the same question, but it never turns the original gate green
  (Appendix C).
- **[NULL-AS-NEW-PRINCIPLE]:** a proposed foundational principle that
  reduced to an existing identity or positivity condition, under the
  program's redundancy rule.
- **Owner ruling:** a project-level adjudication by the author recording
  how a result is admitted, demoted, fenced, or incorporated. It is not a
  theorem, a peer-review finding, or an experimental confirmation.

> A failure is a result. It is never repaired by changing the interpretation after the run.

A conditional result stays conditional. A successful calculation does not
discharge the assumptions that made it possible. Program-specific terms
are defined in **Appendix H**, and the meaning of "pre-registered" in this
record is stated precisely in **Appendix D**.

---

# 2. What GRUT currently claims

> **Within the admitted model classes, local dynamics generate continuum spectral structure, memory, effective dissipation, and an influence hierarchy that is complete as an interface within the declared model and access class. Declared access determines which distinctions are recoverable. In the tested classes, sufficiently rich access reconstructs graph and substrate geometry from accessible influence data. The program has not established a unique microscopic ontology, nor shown that every physical sector must instantiate this construction.**

The campaign forced three demotions relative to earlier formulations:

1. **The constitutive kernel is not fundamental.** A memory kernel is
   downstream of subsystem selection, state information, and access (P-1,
   D-1). The influence hierarchy is also richer than the kernel pair
   $(K,N)$ (P-3).
2. **Stationarity is not fundamental.** Exact nonstationary constructions
   produce genuinely two-time kernels (Section 5). The stationary form
   $K(t-t')$ is a regime-specific representation.
3. **In the tested class, "medium" versus "relational" language is not
   physical.** In the exactly solvable Gaussian class, with a factorized
   initial state, genuinely different microscopic environments are
   observationally equivalent at fixed influence data and system-limited
   access (D-1). The run does not exclude access channels outside that
   class.

What remains is a **dependency-resolved theory of generative structure**,
not a guessed field equation.

## 2.1 Relation to existing work, and what is new

**What is new.** This section is a positioning map, not a literature
review: no systematic literature search has been performed for this
record. Most of the mathematics used in Layers I–IV is standard. The
program's own verdicts say so, grading the machinery "standard
mathematics" or NULL-REDUNDANT as a new principle. What the program adds
is in-house, pre-registered verification within declared classes, and the
dependency map: which structures the tested models generate, which they do
not, and where each supplied input enters. Program-specific in-class
findings have not been checked against the literature for priority.

| Record section | Standard ingredient it re-demonstrates or relates to | What the program says it added |
|------------|------------------------------|----------------------|
| §4 elimination and memory | Nakajima–Zwanzig and Mori projection [Nak58, Zwa60, Mor65]; Caldeira–Leggett baths [CL83]; Bernstein–Widder completely monotone class [†Ber29, †Wid41]; Kronecker/Hankel minimal realization (named in the instrument); infinite harmonic lattices [†FKM65] | an in-class finite-local demonstration of the chain from locality to memory, continuum, and effective irreversibility |
| §4.3 irreversibility | Feynman–Vernon factorization [FV63], Poincaré recurrence, Pusz–Woronowicz passivity [PW78], Nakajima–Zwanzig deletion | the organization of these ingredients, per the record's own statement |
| §6 influence cone | Caldeira–Leggett-class Gaussian realizability; Feynman–Vernon influence functional [FV63, CL83]; fluctuation–dissipation [CW51, Kub66] | "borrowed-standard" per the P-2 charter; the program adds verification, minimality probes, and the mapping onto the record |
| §6.4 hierarchy positivity | positivity of the state on the operator algebra generated by the coupling (GNS/Wightman-type positivity [†SW64]) | NULL-AS-NEW-PRINCIPLE; one Gram condition organizes the cone's two inequalities as low-order faces |
| §8 access | bicommutant and central-decomposition structure; Lanczos chains [†Lan50] | NULL-REDUNDANT as principles; the content is which distinctions each access level makes recoverable |
| §9 geometry | spectral geometry and "hearing the shape" [†Kac66]; effective resistance [†KR93]; star–mesh (Y–Δ) reduction; Lanczos/recursion [†Lan50, †HHK72] | the eliminations and non-eliminations each access level produces |
| §10 units | dimensional analysis | the operational discriminator separating a unit change from a physical deformation |
| §13–§14 probe, universality | Weinberg's soft-graviton and spin-2 universality arguments [†Wei64, †Wei65]; Gupta-type gauge arguments [†Gup54] | the exact boundary of what is derived given the supplied probe |
| §16 retained sector | Goldstone modes [†Gol61] | a class selection relative to tested candidates |
| §17 matter–graviton channel | golden-rule emission; the standard minimal coupling $-\tfrac{\kappa}{2}h_{ij}T^{ij}$ | within-class exponent evidence |
| §18 TT channel | transverse-traceless projection (textbook transversality) | a classification of channel existence by relative dispersion |
| nearest relatives | stochastic gravity [HV08]; Sakharov induced gravity [Sak67]; Jacobson's thermodynamic derivation [Jac95] | comparisons, not support |
| obstructions | Weinberg–Witten [WW80] | carried as a named-exit condition (Section 22) |

References marked † are supplied for this edition. Their bibliographic
data have not been verified against the program's source register (see
References).

---

# 3. The formal architecture

## 3.1 The seven principal objects

1. **$\mathcal O_{\rm local}$: local microscopic dynamics.** Finite local
   dynamical systems in the admitted classes (Section 3.3). No unique
   substrate ontology is selected.
2. **$\mathcal C_{\rm continuum}$: continuum structure.** Spectral and
   memory structure obtained by eliminating hidden modes and taking
   limits.
3. **$\mathcal I$: the influence hierarchy.** Response, noise, and higher
   connected correlations of the retained sector's environment.
4. **$\mathfrak A$: access.**
   - The *seed* is the set of system operators through which an observer
     or probe couples to the environment (for example, the coupling
     operator $B$ together with the identity).
   - Its *closure* is the operator algebra the seed generates under
     products and time evolution.
   - *Boundary events* are changes to the seed.
5. **$\mathcal G$: geometry.** Geometry reconstructed from influence and
   access data by spectral, resistance, metric-density, and walk-count
   functionals: geometry *as far as access reaches*.
6. **$\mathcal F_{\rm eff}$: effective sectors and probes.** Sector classes
   inside the influence cone, candidate retained sectors, and the probe
   structures that couple to them.
7. **$\mathcal G_{\rm grav}$: gravitational-side response.** The
   conditional gravitational influence point, the transverse-traceless
   (TT) response, channel conditions, and the exponent class.

## 3.2 The cross-cutting role of access

Access is consumed in three roles:
- **partition:** it determines which subsystem is retained;
- **reach:** it determines which distinctions can be reconstructed;
- **boundary events:** changing access turns hidden differences into
  observable ones.

In the tested class, the closure is canonical given a seed, but the seed
itself is not dynamically selected (P-5, P-6).

![**Figure 1.** The GRUT architecture as this record defines it. Green: the generative core (derived in class or family-fact). Orange: the conditional branch. Grey: supplied inputs I1–I11, shown where they enter. Blue: access, which acts on every layer. Red: the two seams.](figures/grut_architecture.png)

## 3.3 The admitted model classes

Every result in this record holds within a declared class. The classes
actually used are:

| Class | Dynamics | Used in |
|----------------|----------------------------|--------------------|
| (a) First-order relaxational networks | $\dot x=-\mathbf K x$, with $\mathbf K$ symmetric positive (semi)definite and local (overdamped springs plus on-site pins; RC-type) | persistence checks, minimal-ontology C1–C3, C1-a, C1-a2 |
| (b) Conservative harmonic lattices | $\ddot x=-\mathbf K x$ on nearest-neighbour lattices, or an oscillator coupled to $M$ harmonic modes | continuum origin, infinite-bath limit, irreversibility I1–I2 |
| (c) Gaussian (quadratic bosonic) baths | star baths with per-mode Gaussian states, classical or quantum | P-2, D-1, G-1, G-2, GS-1, SX-1, CA-1, RS-1 |
| (d) Finite spin systems | tensor products of qubits with local Hamiltonians | P-3, P-4, P-5, P-6, S4-1, and the quantum legs of G-2 |
| (e) Declared continuum sectors | dispersive fields $\omega(p)$ with tree-level (golden-rule) pair channels | CP-1, EQ-1, TT-1; the ω⁷ coupling instrument (a quantum harmonic chain coupled to TT gravitons) |

**Class matters for form.** Classes (a) and (b) give memory kernels of
different form, and the record keeps them apart:
- In class (a), memory kernels are *completely monotone*: sums of decaying
  exponentials.
- In class (b), kernels *oscillate*: sums of cosines, whose envelope
  decays only in the continuum limit.

The admitted principles for "derivable" are: strict locality; finite
microscopic content per site; first- or second-order autonomy; passivity;
time-translation invariance of the microscopic law (relaxed in Section 5);
and standard open-system reduction.

---

# 4. Layer I — local microscopic dynamics to continuum

*Primary sources.* The foundations record of the `adjudicator-track`
branch, archived byte-exact in `archive/adjudicator-track_90218f5/`:
- GRUT Skeleton v02.1 (`GRUT_SKELETON_01.md`, commit `90218f5`);
- the instruments `calc/u3_*.py` and their result files, first committed at
  `affdf52` (24 September 2026) and partly repaired at `5f5395e` the same
  day.

The foundations record predates the charter protocol of the later
campaign. Its checks are written into the instruments' code; no charter was
committed separately before these runs (Appendix D). Section 4.5 gives its
full scorecard, including its failed checks.

## 4.1 Exact finite reduction: where memory comes from

**Setting (class (a), Section 3.3).** Take a finite local network
$\dot x=-\mathbf K x$, with $\mathbf K$ symmetric positive definite. Split
the coordinates into one retained coordinate $q$ (site 0) and hidden
coordinates $y$. Write:
- $K_{SS}$ for the retained site's own stiffness;
- $v$ for the vector coupling the hidden sites to $q$;
- $\lambda_l>0$ and $e_l$ for the eigenvalues and eigenvectors of the
  hidden block $\mathbf K_{yy}$;
- $u_l=e_l\cdot v$ for the coupling of $q$ to hidden eigenmode $l$.

Eliminating $y$ exactly gives

$$
\dot q(t)=-K_{SS}\,q(t)+\int_0^t k(t-s)\,q(s)\,ds+\eta(t),\qquad
k(\tau)=\sum_l u_l^2\,e^{-\lambda_l\tau}=v^{\mathsf T}e^{-\mathbf K_{yy}\tau}v .
$$

Here $\eta(t)=\sum_l u_l e^{-\lambda_l t}m_l(0)$ carries the hidden modes'
initial data ($m_l=e_l\cdot y$); it vanishes when the hidden sites start
at rest. This is the form the program's instruments implement
(`calc/c1_seam.py`; C1-a charter, §1). The memory kernel $k$ is a positive
sum of decaying exponentials, so it is *completely monotone*.

*Notation note.* Earlier program documents write the same kernel as
$K_R(t)=\sum_k (v_{1k})^2e^{\lambda_k t}$ with $\operatorname{Re}\lambda_k<0$
(eigenvalues of the generator $-\mathbf K_{yy}$), and write the reduced
equation schematically as $\dot q=-\int K_R\,q+\text{drive}$. That is the
same kernel with the opposite sign convention for $\lambda$; the schematic
equation omits the instantaneous term and the sign of the memory term.
This record uses the decay-rate form above throughout (Appendix I).

> **Worked example: one hidden node.** Let
> $\mathbf K=\begin{pmatrix}K_{SS}&-g\\-g&\gamma\end{pmatrix}$, so the
> hidden node has total stiffness $\gamma$ and couples to $q$ with
> strength $g$. Then $v=g$, the hidden propagator is $e^{-\gamma\tau}$, and
> $$\dot q(t)=-K_{SS}\,q(t)+\int_0^t g^2e^{-\gamma(t-s)}\,q(s)\,ds .$$
> The retained coordinate now has memory with a single time scale
> $1/\gamma$. As $\gamma\to\infty$ the hidden node follows $q$ instantly and
> the memory disappears. This is what "memory exists if and only if there
> is persistent auxiliary state" means. The foundations record's check P3
> uses exactly this model and records the kernel
> $g^2e^{-at}\Theta(t)$.

**What the foundations record establishes, in class.**

- *Necessity.* Without persistent auxiliary state there is no memory
  (checks P1 and P2 of `u3_origin_persistence.py`). These are algebraic
  statements; P1 is asserted in the code rather than computed.
- *The constructive converse* (checks P3, P4, and E4a):
  - Eliminating hidden modes produces the kernel exactly. The repaired P3
    records direct kernel extraction to $1.8\times10^{-5}$ and trajectory
    equivalence to $1.4\times10^{-16}$. In that model the auxiliary
    variable realizes the eliminated node exactly, so the second figure is
    floating-point agreement between algebraically identical updates. The
    elimination identity is exact algebra; C1-a re-demonstrates it on a
    24-site network to $10^{-12}$ (Section 5.1).
  - The *realization dimension* (the minimal number of hidden modes that
    reproduces a kernel, i.e. its Hankel rank, by Kronecker's theorem)
    equals the number of **distinct** eliminated modes: $\{1{:}1,\ 2{:}2,\
    3{:}3,\ 5{:}5\}$, and a degenerate-pair control returns $M-1$. P4
    synthesizes its kernels directly as sums of exponentials rather than
    by eliminating a bath model, so it tests realization, not elimination.
  - A pure delay is the limit of an $n$-stage Erlang cascade. Convergence
    holds for the integrated kernel (the cumulative distribution), not
    pointwise: $L^1$ errors 0.486, 0.376, 0.277, 0.198 for
    $n=2,4,8,16$ (E4a).

**Repair history (disclosed).** P3, P4, and E4a first **failed**: P3 with
tail error 0.995 against a threshold of 0.05; P4 with Hankel rank 4 at
$M=5$; E4a with errors that *grew* (0.721 → 1.193) while its summary said
they decreased. The failures were diagnosed as instrument defects:
- P3 had recorded the closed-loop rate instead of the kernel;
- P4 had a variable-shadowing bug and near-degenerate random time
  constants;
- E4a compared a density against a step.

The instruments were repaired the same day under the owner's authorization
(repair set `5f5395e`), and the converse was re-banked by measurement. The
repair was not separately chartered, and the failing result files were
regenerated in place at the branch head; the originals remain in git at
`affdf52` and are quoted in `U3_RECORD_NOTE_02`. Appendix C.1 states how
this record distinguishes an instrument repair from a failed gate, and
Section 23.1 lists the failures.

## 4.2 Continuum emergence (class (b), conservative lattices)

The continuum-origin computation (`calc/u3_continuum_origin.py`) uses
class (b): nearest-neighbour periodic lattices with unit springs and unit
masses and **no damping anywhere**. The local memory kernel at the origin
site is

$$
K_0(t)=\sum_k w_k\cos(\omega_k t),\qquad w_k=\lvert v_{0k}\rvert^2,\quad \omega_k^2=\text{eigenvalues of the lattice Laplacian},
$$

and in the continuum limit $K_0(t)=\int\cos(\omega t)\,d\mu(\omega)$, with
$\mu$ the local density of states. These kernels oscillate. They are not
of the completely monotone class (a) form, whose continuum limit is
$\int e^{-t/\tau}\,d\rho(\tau)$ with $d\rho\ge0$ (Section 4.4).

The computation recorded six checks, all marked as passed, with the verdict
`continuum_emergent_from_local_finite_ontology`:

| Check | Content | Recorded measurement |
|-----|----------------------|------------------------------------|
| (i) | Finite chains converge to the continuum kernel on a fixed time window | Sup gap 0.515 at $L=16$; $2.8\times10^{-15}$ at $L=64$; $3.1\times10^{-15}$ at $L=1024$ |
| (ii) | Mode spacing scales as inverse volume at fixed lattice spacing | $\delta\omega\cdot L$ = 3.98, 4.33, 4.42, 4.44 at $L$ = 16, 64, 256, 1024 |
| (iii) | Dimension sets the late-time envelope | Envelope slopes −0.52 ($d=1$), −1.04 ($d=2$), −1.36 ($d=3$), against $t^{-d/2}$ targets −0.5, −1.0, −1.5. All three kernels change sign in the tail (25, 13, 11 sign changes) |
| (iv) | Every substrate is nearest-neighbour local | Maximum coupling range 1 (true by construction; asserted in the code) |
| (v) | The low-frequency class is universal across microscopic spectra | Density-of-states exponents 2.15 (uniform $32^3$ lattice) and 1.79 (weakly disordered lattice); Debye value $d-1=2$ |
| (vi) | Viability of gravity as the bath | **Order-of-magnitude count only** (asserted in the code): suppressing recurrences beyond the cosmic age needs $\gtrsim10^{18}$ modes; the gravitational field has $\sim10^{183}$ in a Hubble volume |

**How to read the table.**
- *Five computational checks and one count.* Check (vi) is recorded as a
  pass but is an estimate, not a derivation; gravity-as-bath remains a
  hypothesis (Section 12). Check (iv) is true by construction.
- *Check (i) reflects finite propagation speed.* On a fixed window, a long
  enough chain reproduces the infinite-chain kernel exactly (already at
  $L=64$) before boundary reflections return. Finite systems still recur,
  on a time scale that grows with $L$.
- *Check (iii).* The instrument labels $d=1$ "recurrent, oscillatory
  ($J_0$ class)" and $d\ge2$ "power law". The recorded slopes show the same
  $t^{-d/2}$ envelope law in all three dimensions, with dimension setting
  the exponent. The $d=1$ fit window is recorded as *not* above the
  finite-size floor, and the $d=3$ slope deviates from theory by 0.14.
- *Check (v).* The result data record the disordered lattice as $14^3$;
  the instrument's summary line says $12^3$.

**Scope.** Continuous spectra, $t^{-d/2}$ envelopes, and effective
irreversibility in infinite harmonic lattices are classical results
[†FKM65]. The computation re-demonstrates them from strictly local finite
models, with no damping inserted. It selects no universal spectral content:
the density $\mu$ (or $\rho$ in class (a)) is supplied. The formal grade of
the infinite-volume results is **[FAMILY-FACT]**: demonstrated across the
tested families, not a limit theorem.

*(Label note: checks (i)–(vi) are internal to this computation. They are
unrelated to the completion problems C1–C7 of Section 24.)*

## 4.3 Irreversibility

Two foundations instruments bear on irreversibility.

- **Infinite bath (4/4).** An oscillator coupled to $M$ Hamiltonian modes,
  with no damping inserted anywhere, acquires dissipative response as
  $M\to\infty$ (tested to $M=2048$). Verdict:
  `dissipation_emergent_in_thermodynamic_limit`.
- **Irreversibility origin (3/4).** This battery asks whether
  coarse-graining plus a boundary condition alone can generate
  irreversibility. Its answer is **no**:
  - a finite closed Hamiltonian system, even with a low-entropy initial
    condition, only dephases, and its kernel recurs;
  - the verdict is `B_irreducible_dissipation_or_infinite_bath`: effective
    irreversibility requires either the infinite-volume limit or
    irreducible microscopic dissipation. GRUT's claim uses the former.

The failed check tested whether the sign of the absorptive spectrum
$\chi''(\omega)$ distinguishes dephasing from dissipation. For the
resistive control it recorded a positive fraction of 0.0, while its summary
line asserts strict positivity. Preparing this edition found three further
problems that the foundations record does not itself disclose:
- the instrument's sign convention for $\chi''$ may produce the recorded
  0.0 (a code observation, unconfirmed because the instrument was not
  re-run);
- its first two cases run the same simulation;
- the second case's pass condition is partly vacuous.

**Status.**
- The **existence** of effective irreversibility is **[FAMILY-FACT]**, as a
  coarse-grained response in the infinite-volume limit. It is not a proof
  that microscopic dynamics stop being reversible.
- Its **direction**, the arrow of time, is **[SUPPLIED]** boundary data
  (inventory item I10).

## 4.4 Spectral form and uniqueness limits

In class (a) the generator is symmetric and positive definite. All poles
are then real and simple, and the stationary kernel has the completely
monotone representation

$$
k(\tau)=\int e^{-\tau/\theta}\,d\rho(\theta),\qquad d\rho\ge0
$$

(the Bernstein–Widder class [†Ber29, †Wid41]). Passivity in the broader
positive-real sense does not by itself exclude complex poles: the class (b)
kernels of Section 4.2 oscillate.

**Uniqueness has limits.** The measure $\rho$ is uniquely recoverable from
$k$ only for light tails (a Stieltjes moment-problem condition, named in the
instrument). The heavy-tailed kernels relevant to the gravitational
constructions lie outside that uniqueness class, although the support of
$\rho$ stays observable.

In summary:
- the **form** of the representation is derived in class;
- the **content** of $\rho$, including its support and any macroscopic
  scale such as $\tau_0$, is supplied (inventory item I11).

## 4.5 The foundations record as a whole

The Skeleton cites some foundations instruments and not others. The full
record on the branch is:

| Instrument | Battery | Notes |
|--------------------|------|----------------------------------------|
| persistence origin (P1–P7) | 7/7 | 5/7 before the same-day repair (Section 4.1) |
| spectrum (E-series) | 13/13 | 12/13 before repair (E4a) |
| realization dimension | 8/8 | |
| continuum origin | 6/6 | two checks true by construction (Section 4.2) |
| infinite bath | 4/4 | |
| irreversibility origin | **3/4** | failed check and further defects in Section 4.3 |
| minimal generative ontology | **5/6** | the failed check (a derivative coupling outside the positive class) contradicts its own summary; a second check passes although its measured exponent is −0.19 against an expected −0.5 |
| gravity-bath spectral match | **8/9** | discrete-box kernel correlation 0.43 / 0.29 against a threshold of 0.98; the committed result still reads $t^{-3}$ where the corrected script says $t^{-4}$ |
| coarse-graining universality | **2/7** | not cited by the Skeleton; several summaries contradict the recorded branch data |
| first coupling instrument | **5/9** | superseded by the rebuilt instrument (Section 17) |
| kernel minimality; KMS spectral constraint; scale origin; resistive scale; gravitational clock; geometry spectral selection | 5/5; 9/9; 7/7; 4/4; 4/4; 9/9 | |

During preparation of this edition, the six pure-standard-library
instruments were re-executed from a copy: spectrum, realization dimension,
geometry spectral selection, kernel minimality, KMS spectral constraint,
and scale origin. All six reproduced their committed scores. The
instruments that need `numpy` were not re-run.

---

# 5. The stationarity seam and its current resolution

**Why stationarity matters.** Section 4 assumed that the environment's
memory depends only on the lag $t-s$ (stationarity). For a free
graviton-like field on the standard expanding-universe background, a
calculation in the cosmological record shows that it does not.

**The measurement** (non-stationarity instrument, 7/7, `5ea380e`; governed
by owner Correction 01, `6fc5139`). The object is the exact retarded
(commutator) kernel of a free transverse-traceless (TT) tensor mode at
fixed comoving wavenumber $k$ on the declared ΛCDM background. It was
sampled at anchor redshifts $z_a\in\{0,\,0.25,\,0.5\}$, lags $0.1$, $0.2$,
$0.4/H_0$, and $k=0.5,1,2$. On that frozen grid:

- The best unconstrained $\Delta t$-only approximation leaves a pooled
  residual fraction $R=0.516$ of the kernel's sampled variation.
- The same-lag drift reaches 1.53: at fixed lag, the kernel changes by more
  than its own mean magnitude as the anchor moves. Part of this is a
  fixed-comoving-$k$ labelling effect, which a de Sitter comparator also
  shows (drift ≈ 0.99). The excess specific to the expanding background is
  0.17, 0.24, and 0.54 at lags 0.1, 0.2, and $0.4/H_0$.
- **Kernel transport** (11/11, `05226bf`). No tested local transport rule
  (the de Sitter kernel re-rated at the observation, midpoint, or emission
  rate) reproduces the exact kernel over the relevant interval. The local
  de Sitter transport matches to ≤ 0.3% at lags up to about $0.25/H_0$; the
  best member is about 3% off at $0.55/H_0$; all are off by 34–130% by
  $0.8/H_0$.

**Scope.** This is a measurement on the sampled domain, not a theorem. It
does not establish that a stationary reduction is impossible in another
representation (for example, the smeared worldline correlator), for
another observable, or in another regime.

The finding created **seam S1**: the continuum map $\epsilon$ of the core
was [UNDEFINED] off stationary backgrounds.

## 5.1 C1-a — the finite stepped nonstationary extension

C1-a (charter `fa6ac44`, verdict `55a708d`, battery 10/12) attacked S1 by
*generating* a two-time kernel from a declared nonstationary microscopic
law. The cosmological kernel was never used as the model.

> **The model (class (a)).** A chain of 24 sites with unit springs and
> pins 0.3 on every site; site 0 is retained and the other 23 are hidden.
> Time is split into epochs $[0,4)$, $[4,8)$, $[8,12]$. During the middle
> epoch the four hidden springs $(1,2),\dots,(4,5)$ are multiplied by
> $1+\epsilon_m$, with $\epsilon_m\in\{0,\ 0.01,\ 0.02,\ 0.5\}$. The
> coupling spring $(0,1)$ is never modulated, so all nonstationarity lives
> in the hidden network. The retained site starts excited and the hidden
> sites start at rest, so $\eta=0$.

**Why the kernel becomes two-time.** Within one epoch $e$ the hidden block
has eigenvalues $\Lambda_e=\{\lambda_{e,l}\}$, eigenvector matrix $V_e$,
and couplings $u_e=V_e^{\mathsf T}v$. Across a step at time $t_*$ (a sudden
quench),

$$
k(t,s)=u_B^{\mathsf T}\,e^{-\Lambda_B(t-t_*)}\;C\;e^{-\Lambda_A(t_*-s)}\,u_A,\qquad C=V_B^{\mathsf T}V_A,
$$

for $s$ before and $t$ after the step. The matrix $C$ is the overlap
between the old and new hidden eigenmodes. The kernel is not a function of
$t-s$ alone, and it reduces to $\sum_l u_l^2e^{-\lambda_l(t-s)}$ when
$\epsilon_m=0$ ($C=\mathbb 1$).

**The reduced solve.** The instrument solves the retained dynamics using
only retained-level ("S-level") data: the per-epoch spectra
$\{\lambda_e,u_e\}$, the mixing matrices $C$, and $K_{SS}$. Within an epoch,
$\dot m_l=-\lambda_l m_l+u_l q$ and $\dot q=-K_{SS}q+\sum_l u_l m_l$; at each
boundary, $m\mapsto Cm$. Integration is fourth-order Runge–Kutta with step
0.002.

| Component | Result |
|----------|--------------------------------------------------|
| **The map $\epsilon$** | **DERIVED EXTENSION, in class.** The S-level solve reproduces the exact full nonstationary dynamics to $1.0\times10^{-12}$. The step-halving error ratio is 17.85, a fourth-order signature, so the residual is integrator error. |
| **Continuity** | $k(t,s)\to k(t-s)$ **exactly** when time-translation invariance is restored ($7.8\times10^{-16}$). The deviation is linear in the modulation amplitude (ratio 1.9968 between $\epsilon_m=0.02$ and $0.01$). |
| **Earned structure** | **Preserved.** Passivity holds, and the multi-time Gram matrix stays positive semidefinite off the stationary domain (to $8.6\times10^{-14}$). A deliberately tampered Gram matrix is detected at −0.160. Hierarchy positivity is therefore stationarity-independent by measurement, not only by identity. |
| **Packaging** | Two frozen gates **RED** (Section 23): the same-lag drift measured 0.0498 against a threshold of 0.1, and the local-anchor family's midpoint member measured 0.0494 against 0.05. The labeled diagnostic found the thresholds miscalibrated against the frozen *peak* normalization: $k(0)=v^{\mathsf T}v$ does not depend on the modulation, so normalizing by the peak suppresses the effect being measured. |

The owner accepted the map, continuity, and structure components and
carried the packaging question to C1-a2. The formal domain extension is
recorded as Formalization 01 Amendment 02 (equivalently, Formalization 02
Amendment 01).

## 5.2 C1-a2 — the packaging boundary, certified

C1-a2 (charter `3b139ab`, verdict `4deda60`, battery 7/7) is a separately
chartered re-test. C1-a's record was declared immutable, and its two reds
stay red. "Packaging" means representing $k(t,s)$ by a single stationary
spectral measure or by a single function of $t-s$.

**Design.** C1-a's model, with two working points ($\epsilon_m=0.5$ and
$1.0$) and a stationary control. Anchors: three times in the first epoch
(1.5, 2.0, 2.5) and three in the modulated epoch (5.5, 6.0, 6.5). Lag
window $\tau\in[0.5,3.0]$. The statistics use the kernel's own local scale
at each lag instead of its peak.

**Calibration disclosure.** The charter states that its thresholds were set
with roughly a 2× margin below C1-a's labeled diagnostic values:
"calibration by prior measurement, disclosed — not blind prediction". Its
recorded strength is "freshly frozen, mechanically evaluated".

The gates below are renamed A2-1 to A2-6; the charter calls them P-1 to
P-6, labels unrelated to the forks P-1 to P-6 of Sections 6–8.

| Gate (charter label) | Statistic | Result | Threshold |
|---------|------------------------------|-------------|--------|
| A2-1 (P-1) | Largest local-scale difference between the kernel at the same lag from anchors in different epochs, $\epsilon_m=0.5$ | 0.1182 | > 0.05 |
| A2-2 (P-2) | Ratio of that statistic at $\epsilon_m=1.0$ to $\epsilon_m=0.5$ | 1.6769 | 1.5–2.5 |
| A2-3 (P-3) | Worst error of each frozen local-anchor rule (anchor at emission, observation, midpoint), $\epsilon_m=1.0$ | 0.1095 / 0.1484 / 0.0968 | each > 0.05 |
| A2-4 (P-4) | Largest per-lag spread of $k(a+\tau,a)$ over the six anchors, divided by its mean | 0.1100 | > 0.05 |
| A2-5 (P-5) | Stationary control, both statistics | $4.4\times10^{-15}$, $1.8\times10^{-15}$ | < $10^{-10}$ |
| A2-6 (P-6) | Stationary world with all springs ×1.25: drift statistic | $3.8\times10^{-15}$ | < $10^{-10}$ |
| A2-6 (P-6) | The same world: kernel difference from the base world | 0.2737 | > 0.05 |

**A2-4 excludes the whole class.** At each lag, the per-anchor mean is the
$L^2$-optimal $\Delta t$-only fit. A2-4 therefore excludes every
$\Delta t$-only kernel at the certified scope, not just three
prescriptions.

**A2-6 fixes the statistic's meaning.** A stationary world whose kernel
differs by 0.2737 gives zero nonstationarity signal. The statistic detects
nonstationarity, not kernel difference.

**Certified at finite stepped level, in class:** no single spectral measure
and no single $\Delta t$-kernel packages the generated $k(t,s)$ over the
sampled anchors and window. The exclusion is not a theorem over all
nonstationary laws. The replacement datum is exhibited constructively:

$$
\bigl[\{\lambda_e,u_e\}_e,\ \{C_{e'e}\}_{e,e'}\bigr],\qquad C_{e'e}=V_{e'}^{\mathsf T}V_e ,
$$

or equivalently the family of hidden-network propagators. **Minimality is
not proved.** The owner accepted C1-a2 as Formalization 02 Amendment 02
(`6abbf316`), the source boundary of this record.

**Remaining parts of S1:**
- **C1-b**: the infinite-volume nonstationary limit (open);
- **C1-c**: smooth modulation (open).

---

# 6. Layer II — influence data

## 6.1 Definitions, and the Gaussian influence cone (P-2; 16/16)

> **Definitions (the P-2 class).** A system couples linearly, through an
> operator $B$, to a Gaussian bath of harmonic modes $\mu$ with frequencies
> $\omega_\mu>0$ and couplings $c_\mu$. The bath's entire effect on the
> system (its Feynman–Vernon influence functional [FV63]) is then fixed by
> two kernels:
> $$K(t)=\sum_\mu J_\mu\,\frac{\sin\omega_\mu t}{\omega_\mu}\quad\text{(dissipation, or response)},\qquad N(t)=\sum_\mu J_\mu s_\mu\,\frac{\cos\omega_\mu t}{\omega_\mu}\quad\text{(noise)} .$$
> Here $J_\mu=c_\mu^2$ is the spectral weight of mode $\mu$, and $s_\mu$ is
> its symmetric occupation: $s=\tfrac12$ in the vacuum and
> $s=\tfrac12\coth(\hbar\omega/2k_BT)$ at temperature $T$. The spectral
> forms are the **dissipation spectrum** $J(\omega)$ and the **noise
> spectrum** $\nu(\omega)=\hbar\,s(\omega)J(\omega)$. The P-2 instrument
> works in units $\hbar=k_B=1$; the factor $\hbar$ here is restored by
> declaration, so that the vacuum sits on the floor below.

Within this class, the realizable pairs form the cone

$$
\mathfrak C_{\rm Gauss}=\left\{(J,\nu):\ J(\omega)\ge0,\quad \nu(\omega)\ge\tfrac{\hbar}{2}J(\omega)\right\}.
$$

- $J\ge0$ is the passivity half. It is automatic for real couplings
  ($J_\mu=c_\mu^2$).
- $\nu\ge\hbar J/2$ is the quantum half. It says $s\ge\tfrac12$: the mode
  occupation above the zero point is non-negative.

**Worked example: a thermal bath.** At $T=0.7$ (units $\hbar=k_B=1$) the
instrument's frequency grid runs from $\omega\approx0.51$ to $2.09$, and
$s(\omega)=\tfrac12\coth(\omega/1.4)$ runs from 1.43 down to 0.553. Every
value exceeds $\tfrac12$, so the thermal state lies strictly inside the cone.
As $T\to0$, $s\to\tfrac12$ and the state reaches the floor: the vacuum
saturates it exactly (reconstruction to $2.3\times10^{-16}$ in $K$ and
$1.5\times10^{-16}$ in $N$).

**Minimality was probed constructively:**
- the vacuum saturates the floor exactly;
- the interior is filled, including a genuinely non-thermal (non-KMS)
  occupation profile;
- three proposed additional constraints were each defeated by an explicit
  realizer.

KMS, the fluctuation–dissipation theorem (FDT), stationarity, and
single-pole memory are **states inside the cone, not constraints on it**.
None of them selects the memory spectrum.

**Class boundary.** The cone holds for the declared class: harmonic modes
of positive frequency in Gaussian states, one scalar channel. Outside it,
for example in gain media or with effective negative-frequency
oscillators, $J<0$ occurs; the general quantum bound is the standard
$\nu\ge\frac{\hbar}{2}\lvert J\rvert$.

**Provenance.** The P-2 charter declares the cone "borrowed-standard
Gaussian open-system mathematics (Caldeira–Leggett-class realizability)"
[CL83, CW51, Kub66]. P-2's contribution is instrument-grade verification,
the minimality probes, and the mapping onto this record. It is not a GRUT
derivation.

## 6.2 What the cone explains, and what it does not

The floor $\nu\ge\frac{\hbar}{2}J$ locates ℏ geometrically, as the height of
the fluctuation floor. It does not derive the value:

$$
\boxed{\hbar\ \text{is located, not generated.}}
$$

Classical physics is the same cone with the floor removed. This does not
explain why the physical world is on the quantum branch.

## 6.3 Why $(K,N)$ is insufficient (P-3; 24/25)

P-3 built two genuinely different spin baths with exactly matched two-point
data: both have two-point function $C(t)=2g^2e^{-i\omega_0t}$, where $g$ is
the bath's coupling strength, and both have vanishing third cumulants. Their
connected fourth cumulants differ: $\kappa_4=-4g^4$ against $-8g^4$. A probe
qubit's coherence (maximum 1) evolves differently in the two baths, by up
to **0.338**; a matched control reads 0.0.

So $(K,N)$ is a projection of the influence structure, not all of it. The
first physical obstruction appears at the first unmatched cumulant, and
P-4 constructs pairs that first differ at orders 4, 6, and 8. **Matching to
finite order never certifies equivalence.**

**The matrix lift.** For several coupling operators $B_a$, define the
matrix spectrum $C_{ab}(\omega)$ of the bath correlations, and
$\nu\equiv\frac12\bigl(C(\omega)+\bar C^{\mathsf T}(-\omega)\bigr)$,
$J\equiv C(\omega)-\bar C^{\mathsf T}(-\omega)$. The candidate lift of the
cone, $\nu\pm J/2\succeq0$, is then literally $C(\omega)\succeq0$ and
$\bar C^{\mathsf T}(-\omega)\succeq0$: positivity of the bath state
(units $\hbar=1$). P-3 graded it **NULL-AS-NEW-PRINCIPLE**. For one
commuting channel it reduces to $\nu\ge\lvert J\rvert/2$.

## 6.4 The full influence hierarchy (P-4; 21/22)

The **influence hierarchy** is the set of all multi-time correlators
$\langle B(t_1)\cdots B(t_n)\rangle$ of the bath coupling operators.

- *Complete as an interface, in class.* In the tested class, two
  environments with the same hierarchy produce identical dynamics for every
  observable accessible through $B$; P-4 constructed no counterexample.
  Bounded-moment determinacy is cited as standard mathematics and claimed
  in class only.
- *Its positivity is state positivity.* The hierarchy is admissible exactly
  when every Gram matrix of monomials in $\{B(t)\}$ is positive
  semidefinite, which is positivity of the bath state on the algebra those
  operators generate:

$$
\boxed{\text{influence-hierarchy positivity}\equiv\text{state positivity}}\qquad[\text{IDENTITY; NULL-AS-NEW-PRINCIPLE}]
$$

One Gram condition contains the cone's two inequalities as its low-order
faces. This is a structural reformulation of quantum admissibility, not a
derivation of quantum mechanics. One frozen gate failed (the order-8
window; Section 23).

---

# 7. Sector counting and influence exponents (S-1; 18/18)

**The exponents.** Write $J(\omega)\propto\omega^s$ at low frequency. The
record carries three exponent classes, the "3/5/7 ladder":
- $s=3$: the matter (acoustic) channel of the earlier record;
- $s=5$: the flat-space graviton-loop kernel;
- $s=7$: the two-phonon graviton channel (Section 17).

These values come from different records in different conventions, so they
are compared only through their increments.

**Counting rules measured in S-1:**
- each extra power of momentum in the vertex adds +2.000;
- phase space adds $d-1$;
- an order-2 symmetry cancellation (tracelessness) adds +3.999.

The ladder is **consistent by mechanism** at the increment level, where
conventions cancel. No single formula derives its absolute values.

**The counting law, as updated by the P-3/P-4 ruling (provisional).** In
the tested families, locality and symmetry select **branch** exponent
classes. At matrix level the observable exponent then follows spectral
competition among branches:

$$
\text{locality}+\text{symmetry}\ \rightarrow\ \text{branch classes}\ \rightarrow\ \text{spectral/matrix selection}\ \rightarrow\ \text{effective sector}.
$$

Two further results bound the law:

- **No tested extremum selects the exponent.** None of the three declared
  extremization functionals (memory duration, low-frequency fraction,
  zero-point load) selects any recorded exponent. The one band-robust
  interior extremum found ($s=1.25$) lands on nothing physical. Amplitudes
  stay free.
- **Matrix masking.** With several channels, the lowest exponent dominates
  at low frequency ("min-dominance"), so a cancelled branch can be hidden by
  another. The frozen eigenvalue-level gate for S-1's hypothesis H3 remains
  **RED** (+2.216 against a predicted +4). The labeled post-hoc diagnostic
  shows the +4 increment surviving at branch level: +3.999 exactly on the
  cancelled branch's spectral weight.

> Locality and symmetry constrain the scaling class of a sector's influence data. They do not select its amplitude, state, or microscopic realization.

The spectral-density classification $J\propto\omega^s$ itself is standard
[Leg87]; S-1 grades its own law "a compatibility principle, not a new law".

---

# 8. Layer III — access as a physical interface

The campaign adopts, and its results repeatedly illustrate, the following
working principle. It is a definition, not a derived result, in the spirit
of operational approaches to the foundations of quantum theory:

> **A distinction is physically meaningful to an observer exactly to the extent that it changes the influence data accessible to that observer.**

## 8.1 Subsystem selection (P-1; 6/6)

In the tested class (the exactly solvable Gaussian toy class, one 10-site
testbed per regime), P-1 found three regimes:

- **Structured worlds:** the dynamics can distinguish a subsystem without
  help. One intrinsic criterion, causal cohesion, selected the impurity
  with gap 0.678, and the selection was stable under coarse-graining. No
  second criterion agreed, so the selection is partial and
  criterion-relative; the pre-registered signature was not reached.
- **Symmetric worlds:** descriptions are representationally equivalent;
  the intrinsic criteria return only tie-orbits.
- **Generic worlds:** no partition is selected by the tested criteria.

The natural criteria (bath rank, minimal entanglement, causal cohesion)
disagree with one another; no universal subsystem selector was found. The
instrument's mechanical signature printed "B", and the pre-registered
three-way taxonomy proved incomplete. The trichotomy is the verdict's
reading of the per-testbed data, and the owner ruling accepted it on that
basis.

## 8.2 Seed versus closure (P-5, 22/22; P-6, 38/39)

The **seed** is the set of operators through which a probe couples; its
**closure** is everything generated from the seed and the Hamiltonian
under products and commutators (Section 3.1).

- **Given a seed, its closure is canonical.** The seed itself matters: the
  same dynamics with seed $\{\mathbb 1,B\}$ alone closes at dimension 2, not
  4.
- **The map from seeds to closures is not injective (P-6).** On a 3-spin
  chain, the two end seeds $\sigma_z^1$ and $\sigma_z^3$ share the causal
  graph and the conservation law, and each generates exactly the same
  32-dimensional parity-commuting algebra. Yet a probe coupled through one
  or the other sees coherence curves differing by **0.287**.
- **Minimal sufficient seeds depend on the elimination path.**

That seeds are organized by the algebra's central decomposition is standard
structure (NULL-REDUNDANT as a principle). **The access seed is a supplied
input** (I1). One frozen P-6 gate failed (Section 23).

## 8.3 Boundary events (P-5)

A probe qubit couples to spin 1 of a three-spin network through
$B=0.5\,\sigma_x^1$ (pure dephasing). Two hidden environments, A and B,
agree on every multi-time correlator of $B$:
- the probe coherence is identical to $1.3\times10^{-14}$ over $0<t\le10$;
- yet the environments differ outside access by 1.547 in
  $\langle\sigma_z^2(t)\rangle$ (maximum possible 2).

At $t_*=3.0$ the coupling is extended to $B+0.4\,\sigma_x^2$, a change of
access. Before the change the probe coherences agree to
$7.8\times10^{-16}$; after it they split by **0.38**. The difference is
invisible forever under fixed access and consequential exactly when access
changes. Access therefore has a concrete physical role, not only a
bookkeeping one.

## 8.4 Medium versus relational descriptions (D-1; 13/13)

Take two non-isomorphic environments: a 9-dimensional star bath, and an
11-dimensional chain bath with two hidden decoupled modes. Their influence
data are identical. Every observable of the system alone agrees to
$4.5\times10^{-15}$, and observables routed through a probe coupled only via
the system agree to $6.3\times10^{-15}$.

Conversely, two theories with the same kernel $K$ but different noise $N$
split observably: the same bath in a thermal rather than a ground state
changes the noise kernel by 1.09, and the system's trajectories split by
0.91.

**Scope.** The tested class is exactly solvable Gaussian baths, factorized
initial state, one system degree of freedom, finite baths, and access
levels as declared. There, at fixed accessible influence data, the question
"medium or relational?" is representational. The run does not exclude an
access channel outside that class.

**Relation to standard results.** For linear coupling to a Gaussian bath,
that reduced dynamics depend on the bath only through $(K,N)$ is the
Feynman–Vernon result [FV63], and the star and chain forms are related by
Lanczos tridiagonalization [†Lan50]. D-1's contribution is operational: it
fixes the criterion "same influence data implies same physics at this
access" on which the rest of the record relies.

---

# 9. Layer IV — geometry as reconstructed structure

## 9.1 G-1 — the arrival-time route (26/34; eight gates RED)

In the tested class and at the tested scales, arrival-time functionals of
interface data are not metric on finite dispersive substrates. The located
obstructions are dispersive precursor tails, boundary reflections, and
impedance mismatch; G-1's held-out distance checks erred by 37%. All eight
failed gates remain red (on gated checks alone the battery is 9/17). G-2
later read the failure as one of the arrival-time instrument, not of
geometric information.

## 9.2 G-2 — spectral geometry (35/35)

Spectral functionals of the influence data recovered:

- **dimension** 1.000, 2.000, 2.942, and 1.000 for 1D, 2D, and 3D lattices
  and a quantum XX chain (true values 1, 2, 3, 1). The frozen estimator is
  $\hat d=1+\log_2[S(6)/S(3)]$, where $S(r)$ counts sites at hop distance
  $r$; on the cubic lattice its exact value is $1+\log_2(146/38)=2.942$, so
  that figure is the estimator's, not a numerical error;
- **hop distances** within 0.004;
- exact additive integer distance triples (for example $36=15+21$);
- **metric density** tracked to $10^{-9}$, with a held-out check at
  $2\times10^{-12}$.

All reconstructions survive representation scrambles. The recorded grade is
GEOMETRY-PARTIAL-SPECTRAL, with a structural GEOMETRY-UNDERDETERMINED
component. The machinery (heat kernels, effective resistance [†KR93],
Lanczos recursion, multidimensional scaling) is standard. The content is
which invariants a declared access makes recoverable. This establishes an
in-class reconstruction route, not access-independent geometry.

## 9.3 Access-relative geometry

**Single-site degeneracy.** Under single-site access, a 2D grid and a 1D
Lanczos chain have identical resolvent data (to $2.2\times10^{-16}$) and
heat-kernel data (to $4.4\times10^{-16}$). This is a structural degeneracy
of the interface, a consequence of the recursion method: any single-site
spectral measure is reproduced exactly by a semi-infinite chain [†Lan50,
†HHK72].

**Topology horizon.** Rings of circumference 40 and 80 have closed-walk
counts that agree as exact integers through order 38 and first differ at
order 40. The first distinguishing order equals the circumference.

## 9.4 GS-1 — selection by access richness (19/19)

| Access | Geometric selection |
|-----------|--------------------------------------------------|
| Full, site-resolved | **Selected in class, up to relabeling.** Reconstruction at full access is immediate by inversion. The finding is that even an isospectral candidate (a rotated stiffness matrix whose trace moments match to $2\times10^{-16}$) is eliminated: local data differ by 1.59. |
| Boundary, dynamic | **Dynamic data eliminate the Δ network.** Static data are blind: Y and Δ are static-identical to $2\times10^{-16}$. The first separating term is the $\omega^2$ coefficient, 0.1975, matching the analytic value. The dynamic data select the interior dimension (Y over Δ); the interior geometry itself remains **CONSTRAINED**, not uniquely selected. |
| Boundary, static only | Blind |
| Single site | Underdetermined: a non-isometric family survives every earned test |

**Terms.** Y is a three-terminal star with one interior node; Δ is its
star–mesh (Y–Δ) equivalent, with edge weights $w_iw_j/\sum w$. They have
identical static response. The first dynamic difference is the $\omega^2$
coefficient $K_{AI}K_{II}^{-2}K_{IA}$, the inertia of the hidden node; the
figure 0.1975 is its largest matrix entry ($16/81$).

**Scope.** Small quadratic (Gaussian) networks, where the two-point data are
the full hierarchy (P-4); the full-access test object is a $3\times3$ grid.
Non-Gaussian sectors could carry more.

The resulting hierarchy is

$$
\boxed{\text{influence data}\rightarrow\text{access}\rightarrow\text{spectral structure}\rightarrow\text{geometry}}
$$

and not "geometry → everything". Absolute geometry is not currently an
object of GRUT.

**A correction on the record.** A candidate passivity selector, LocPos
(every edge weight and on-site pin non-negative), had appeared to select a
unique geometry at single-site access. A labeled post-hoc diagnostic showed
that with interior pins of 0.1 it admits 96 members, 94 of them
non-isometric. LocPos narrows the family; it does not select a member. The
original line stays on the record beside the correction.

---

# 10. Spatial scaling and units (SX-1; 23/23)

**The physical picture.** A lattice field with nearest-neighbour springs
$k$ and on-site pins $p$ (mass-like terms) has two intrinsic lengths: the
lattice step and the correlation length $\ell_c=\sqrt{k/p}$, the lattice
analogue of a Compton wavelength. A **pure unit change** is a
transformation that leaves every dimensionless accessible datum invariant.
$\lvert\Delta\mathcal D\rvert$ is the largest change in a declared set of
dimensionless accessible data.

- **Co-stretch.** All couplings, pins included, rescale together.
  Dimensionless data stay invariant to $2.4\times10^{-15}$. This is a unit
  change [IDENTITY].
- **Rigid stretch.** Springs rescale while the pins stay fixed, so
  $\ell_c$ changes in lattice units. This is observable
  ($\lvert\Delta\mathcal D\rvert=0.013$). Anisotropic and inhomogeneous
  deformations are also observable (0.094 and 0.180).

All of these deformations are admitted by the earned structure: it
*detects* which one a probe performed but *forbids* none. The statement
"spatial rescaling is always a change of units" is therefore false in the
tested class, for sectors with two or more intrinsic scales; for
single-scale sectors the distinction is vacuous. Which operation a
gravitational probe performs is the supplied **co-stretch declaration**
(Sel-4x; inventory item I5), the ruler counterpart of "a uniform static
field rescales all rods equally".

**Decidability splits by access.** A pure unit change and a unit change
plus an interior deformation give identical single-site data (to
$1.3\times10^{-14}$) but separate under full access (6.05). SX-1 grades its
classification leg "dimensional analysis made operational".

---

# 11. Quantum structure: what is and is not recovered

**Recovered, in class:**
- the *form* of the quantum fluctuation floor (its height, ℏ, is supplied);
- matrix positivity constraints, stronger than channelwise positivity;
- discrimination by higher cumulants;
- the admissible influence hierarchy;
- the classical limit, as the same cone with the floor removed.

**Not derived:**
- **ℏ.** Located, not derived. The earlier record's ℏ-emergence attempt
  failed; its primary computation is not committed in this record's
  sources.
- **The Born rule.** The routes tested in the program's earlier record
  returned negative results. Decoherence selects a pointer basis; it does
  not select an outcome. This is not an evaluation of Gleason-type,
  envariance, or decision-theoretic derivations in the literature.
- **Noncommutativity.** Supplied. The routes tested from a commutative
  substrate produced no quantum structure. Published programs of that kind
  were not evaluated.

---

# 12. The gravity program

The gravity branch is conditional and downstream of the core. Success in it
would constrain a gravitational identification; failure in it would not
invalidate Sections 4–11.

**The gravitational identification** is the program's central physical
hypothesis: that the persistent, memory-bearing continuum of Layer I is
physically realized by gravity, so that gravity is the universal
dissipative environment to which all matter couples. It is graded
**HYPOTHESIS**, not derived. The foundations record found a gravity-like
spectral bath viable at 8 of 9 spectral checks (Section 4.5), which is
consistency, not derivation. Completion problem C7 (Section 24) is the test
that could kill it.

$$
(\mathcal I,\mathfrak A,\mathcal G)\rightarrow\mathcal F_{\rm eff}\rightarrow\mathcal G_{\rm grav}
$$

**The probe.** Throughout, the gravitational probe is the metric
perturbation $h_{ij}$. It couples to a matter sector through its stress
tensor, $L_{\rm int}=-\tfrac{\kappa}{2}h_{ij}T^{ij}$, the minimal universal
coupling, with $\kappa\sim1/M_{\rm Pl}$. The forks model it in three ways:
- as a uniform strain (CP-1, EQ-1, SX-1);
- as a constant clock field (S4-1, FS-1, U-1);
- as a massless spin-2 field (CC-1, TT-1, and the ω⁷ instrument).

**In plain terms.** Suppose one supplies a massless spin-2 probe that
couples universally to a conserved stress tensor, with a common light cone
and a declared unit convention (inputs I3–I6, Section 21). Then, within the
tested lattice models, the matter-side sector that can absorb or emit it
must be gapless, linearly dispersing, and Goldstone-like, and in the tested
coupling class its emission spectrum scales as $\omega^7$ in the program's
convention. Nothing in the branch derives the probe or its coupling. This
is what the record means by "general relativity is recovered with imports,
not derived" (Section 29).

**The reduction chain.** Each assumption in the chain was attacked in
sequence. Each attack reduced the assumption to a named, more specific
supplied premise, derived part of it within a stated class, or split it by
class:

| Fork | Assumption attacked | In standard terms | Outcome |
|-------|-----------|------------|----------------------------------------|
| **CP-1** (39/39) | Minimal-stress coupling | Which local stress coupling the probe uses | The couplings that give the exponent's +4 increment form a plane, so the exponent does not identify the coupling. Conservation leaves an improvement freedom ξ; adding infrared Weyl symmetry selects the canonical tensor in $D=2$ and the improved tensor in $D=4$. **Reduced to** geometric (proper-distance) coupling at $\xi=0$. |
| **EQ-1** (45/46) | Geometric-only coupling | The weak equivalence principle | Earned selectors leave geometric and non-geometric couplings side by side. **Reduced to Sel-4**: a constant probe acts on each sector as a pure change of units, invisible in the sector's own dimensionless data. |
| **S4-1** (28/28) | Sel-4 as a whole | Gravitational redshift and its universality | **Splits by part and by class.** The temporal part (Sel-4t: the probe couples to the sector's energy, $O\propto H$) is derived in class for generic sectors, given C_cons. The universality part (Sel-4U) is derived for interacting sectors and irreducible for non-interacting ones. |
| **FS-1** (31/31) | The free-sector exception | — | The exception is structural (Section 14). |
| **CC-1** (29/29) | C_cons | Current conservation | **Irreducible.** Reduced to a supplied massless gauge probe. |
| **U-1** (23/23) | Clock universality | Universality of coupling across sectors | **Class split.** Derived in class under exchange, conditional on the supplied massless gauge probe; irreducible for decoupled sectors. |
| **RS-1** (27/28) | Retained-sector choice | Which matter sector the probe couples to | A class is selected, conditional on CARRIER and the probe. |
| **CA-1** (23/23) | CARRIER | — | **Irreducible.** Reduced to an access-seed coincidence. |
| **SX-1** (23/23) | Sel-4x | Uniform rescaling of rods | **Irreducible.** Reduced to the co-stretch declaration. |
| **TT-1** (9/10) | The physical TT channel | Graviton emission by pairs of matter quanta | ξ has no effect on the physical channel; the tensor structure is forced; existence splits by class. |

---

# 13. Probe structure and universality

## 13.1 Conserved-current coupling (CC-1)

**C_cons** is the requirement that, at zero frequency and zero momentum,
the probe couples to a conserved local charge: its operator $O$ commutes
with the Hamiltonian, $[O,H]=0$.

A non-conserved coupling, the phonon mass modulation
$O_M=\tfrac12\sum_i p_i^2$, passes every earned selector at the
constant-probe level:
- the influence cone;
- hop and resistance geometry;
- static regularity.

It is spectrally a unit change. The criterion "stationary under driving"
turns out to be C_cons restated: requiring that a driven probe produce no
spectral weight at nonzero frequency is exactly $[O,H]=0$, an identity, so
it adds no independent support. Imposing C_cons wholesale would also
delete GR-1's own $T_{xx}$ pair channel, which does not commute with $H$;
C_cons can apply only to the probe's constant (clock) component.

**The positivity route separates the cases.** Exchange positivity was
tested in $D=4$ with 200 random sources per case (normalization arbitrary;
only the sign carries content):
- **Massless probes:** vector and spin-2 exchange become negative for
  non-conserved sources (minimum residues −10.6 and −17.8).
- **Massive probes:** exchange stays positive.

$$
\boxed{\begin{array}{c}\text{In the tested cases, } C_{\rm cons}\ \text{follows from the cone for a supplied massless}\\ \text{gauge probe, and not for massive probes.}\end{array}}
$$

This parallels Weinberg's low-energy derivation of charge conservation and
universal graviton coupling from massless spin-1 and spin-2 exchange
[†Wei64, †Wei65]; CC-1 grades itself "the Weinberg/Gupta–Bleuler-type
argument", NULL-REDUNDANT as a new principle. Its contribution is the
dependency map. *(The non-uniqueness of the exponent locus, often quoted
beside this result, is CP-1's finding; see Section 12.)*

## 13.2 Universal reach (U-1)

Given the supplied massless gauge/Lorentz probe structure, exchange-coupled
sectors are forced to universal clocks (derived in class). The soft-emission
gauge variation in $D=4$, over 100 random configurations per class, is at
least 0.13 for unequal clock couplings and at most $9\times10^{-16}$ for
equal ones. The forcing comes from the supplied structure, not from anything
earned; U-1 grades it "Weinberg's soft-emission argument: standard".

For genuinely decoupled sectors that variation vanishes exactly.
Non-universal clocks there are observable by joint access (cross-sector
discriminator 0.049, against $1.8\times10^{-14}$ for universal coupling), yet
nothing earned forbids them.

A dynamical probe that couples only through clocks mediates no exchange:
the bath energy $\langle H_B\rangle(t)$ stays constant to
$7.5\times10^{-15}$. Universal reach is therefore not self-generating: **it
is supplied** (I4).

---

# 14. Clock coupling and the free-sector loophole (S4-1, FS-1)

Let $O$ be the operator that the probe's constant (clock) component couples
to. In general relativity a uniform potential couples to the total energy,
$O=H$, which only rescales the sector's clock rate (gravitational
redshift).

- **Generic interacting sectors.** Such a sector has no local conserved
  charge other than $H$, so C_cons forces $O\propto H$ (derived in class,
  S4-1; the finite-system analogue of Weinberg's universality argument).
- **Free and integrable sectors.** An exact phonon ring carries exactly
  $2R$ independent local conserved quadratic charges within range $R$, so
  $H$ is not singled out.

This opens **loophole L1**:

> The gravity-side retained sector lies in the exception class of the clock-coupling ($O\propto H$) argument used to motivate its own coupling chain.

The candidate **GeoInv** ("a constant probe must not rewire the sector's
recovered hop geometry") would, together with C_cons, select $O=H$ in the
free sector. It is an **unpromoted candidate**, not an axiom. GR-1's pair
channel is *insensitive* to this ambiguity, because conserved clock
couplings contribute nothing to it; FS-1 records that insensitivity is not
the same as resolution.

---

# 15. Carrier selection (CA-1)

**CARRIER** is a bridging premise introduced in RS-1: *the matter sector
the gravitational probe couples to is the same sector whose static response
carries the geometry recovered in Section 9.* "Carries the geometry" means
that its effective resistance $R(0,r)$ is additive in the separation $r$.

CA-1 tested whether CARRIER can be derived:

- **The recovered geometry cannot pick the carrier.** Four genuinely
  different sectors built on the same substrate operator (a phonon, a $z=2$
  Schrödinger boson, a rescaled twin, and a classical relaxational field)
  recover the same normalized resistance geometry, to $4\times10^{-14}$.
  CA-1 notes that this leg is close to an identity: sectors built on the
  same stiffness operator share its geometry by construction.
- **The cone makes one earned cut.** It eliminates the classical carrier,
  because at $T=0$ its noise vanishes and $\nu-J/2=-0.192$ (units
  $\hbar=1$). Three quantum carriers survive. CA-1 records that this cut has
  an escape: a quantum-completed dissipative field would sit on the floor
  and survive.
- **A non-carrier bath survives everything earned.** Free fermions pass
  every earned test.

**CARRIER is therefore not derived.** It reduces to an access-seed
coincidence: *the sector the gravitational probe couples to is the sector
the geometry was recovered from*, i.e. the probe's access seed coincides
with the geometry-recovery seed. Since seeds are supplied (Section 8.2), so
is this coincidence (I2).

---

# 16. The retained gravitational-side sector (RS-1)

RS-1 tested five candidate sectors against two selectors.

- **The earned selector, given CARRIER:** the additivity ratio
  $A=R(0,16)/R(0,8)$ of the static effective resistance. A sector that
  carries an additive one-dimensional metric gives $A\approx2$; the frozen
  window is $[1.8,2.2]$.
- **The supplied selector, from the probe:** infrared boost compatibility,
  the ratio $v_gv_p/v^2$ of group and phase velocities, which tends to 1 for
  linear dispersion ($z=1$, $\omega\propto k$) and fails for $z=2$.

| Candidate | $A=R(0,16)/R(0,8)$ | $v_gv_p/v^2$ | Status |
|-----------|---------------|--------|--------------------|
| Phonon | 1.936 (additive) | 0.999 | **survives both** |
| Magnon ($z=2$) | 1.936 (additive) | 3.993 | eliminated by the supplied layer |
| Free fermions | 1.020 (local density saturates) | 0.995 | eliminated by the earned layer (local access) |
| Flexural chain ($z=2$) | 3.744 (size-dependent) | 3.993 | eliminated by both |
| Gapped control | 1.019 (screened) | 0.999 | eliminated by the earned layer |

What survives is a class, relative to the tested candidates and in the
infrared only:

$$
\boxed{\text{gapless},\ z=1,\ \text{locally accessible Goldstone-like}.}
$$

"Goldstone-like" means gapless, with static response $\propto1/q^2$,
reached through a local field [†Gol61]. This is a class, not a unique
ontology, and the final (magnon) cut is made by the supplied probe
structure. The gauge structure permits full-stress coupling but does not
force it.

**One frozen gate remains RED.** The flexural gate predicted cubic growth,
$A>4$, and measured 3.744. The labeled diagnostic shows
$R\sim N r^2$ (quadratic and size-dependent) rather than cubic behaviour.
The flexural sector is eliminated either way by the frozen window. The
exact member of the class and its dispersion curvature belong to inventory
item I11.

---

# 17. Matter–graviton coupling and the $\omega^7$ result

This section gives the full record of the program's most-cited
gravitational number, including the parts that weaken it.

## 17.1 The setup and the mechanism

**The instrument** (coupling instrument v3, `adjudicator-track`, repair set
`5f5395e`; battery 20/20). A quantum harmonic chain of 256 sites, with
lattice dispersion $\omega_q=\sqrt{\Omega^2+4\sin^2(q/2)}$ (acoustic
$\Omega=0$; gapped control $\Omega=1$), couples to weak-field TT gravitons
in a periodic box (14,938 modes, two polarizations, $\omega=\lvert k\rvert$)
only through its stress tensor, $L_{\rm int}=-\tfrac{\kappa}{2}h_{ij}T^{ij}$.
$J(\omega)$ is the golden-rule spectral density for a graviton of frequency
$\omega$ to convert into a pair of phonons $(q,q')$, with energy and
momentum conserved, at zero temperature and order $\kappa^2$. The chain is
the retained system and the gravitons are the bath.

**The mechanism** (GR-1, 30/31, `d827a32`). GR-1 built a fresh
one-dimensional pair instrument sharing no code or data with v3, and wrote
its predictions into its charter before any number existed. Every
prediction landed:
- the kinetic-only and potential-only stress vertices each give a base
  exponent $b$ (measured 4.002 and 4.004 in GR-1's convention);
- a non-minimal admixture destroys the cancellation below (4.011);
- the full minimal-stress vertex gives $b+4.004$: the order-2
  tracelessness cancellation removes the leading term and leaves a
  curvature residual $-2\alpha q^4$;
- exactly linear dispersion makes the full vertex vanish identically
  ($<10^{-14}$);
- all slopes are exactly invariant under rescaling the coupling by 16;
- the same-sign channel is kinematically closed at zero net momentum, and
  the gapped counterfactual is exactly empty below $2\Omega$.

In the v3 convention the base exponent is 3, so the channel's exponent is
$3+4=7$, and its memory kernel decays as $t^{-8}$. GR-1 grades the absolute
value "consistent by mechanism at increment level, never one-formula
derived".

## 17.2 The measured values and the sealed ledger

**Measured by v3:**
- continuum exponent 7.0077 (fit window $\omega\in[0.05,0.35]$);
- box exponent 7.018 (window $[0.15,1.2]$);
- coefficient ratio 1.0005 at $\omega=0.06$;
- kinetic-only 3.003, potential-only 3.006, exactly linear dispersion
  $\sim10^{-34}$;
- the instrument's own tidal control, +2.031 (predicted +2).

**The sealed ledger.** An analytic ledger
(`T2_THEOREM_GATE_AND_PREREGISTRATION_01.md`) was committed at `d2da3a5`
on 24 September 2026 at 18:37 (UTC−5). It was written by a separate AI
session (the "adjudicator") without access to the rebuilt instrument's
output. Its exponent gate G5 is a local log-slope of $8.00\pm0.05$ over
$\omega\in[0.02,0.32]$, which is $7.00\pm0.05$ in the propagator convention.

**What the comparison supports, and what it does not:**

- *The exponent class matches.* 7.008 lies within the ledger's
  $7.00\pm0.05$, although on a different fit window. The frequently quoted
  "$7\pm0.15$" is the instrument's own tolerance, not the ledger's.
- *The instrument's pre-registration was committed with its result.* Its
  window, tolerance, and coefficient check are written in its docstring,
  which was first committed together with its result at `5f5395e`. No
  earlier commit holds them.
- *The coefficient ratio is measured against the instrument's own
  asymptotic formula*, not against the ledger's sealed constants. The
  instrument labels this check "sealed G6", but the mapping onto the
  ledger's G6 constants is not implemented.
- *Several sealed gates have no implementation in v3:* the ledger's
  synthetic pipeline test and normalization map (G1), its own fit window
  (G5), a parity fit (G7), the gapped-step coefficient (G8), a broadening
  stability check (G9), and its +4 tidal control. Only the instrument's own
  +2 tidal variant was run.
- *Blindness is limited.* Two-sided blindness is attested only for the
  first rebuilt run (18:49 local time, timestamp-attested, not
  commit-sealed), which measured $\omega^{5.03}$ in its own convention. An
  adjudication committed after that run (`ebb3a42`) mapped the ledger's
  exponent onto that convention as $8-2-1=5$. The v3 instrument was then
  built in the adjudicator's tree, with pre-registrations mapped from the
  ledger, so v3 was not blind to it.
- *Both sides were AI-operated roles under the owner's direction*, run as
  separate processes in separate trees. "Independent" here means separate
  processes and sealed commits, not external review. Matching one exponent
  class from a small discrete set is weak evidence.

**The "Cherenkov no-go" episode.** A rebuilt run at 19:13 reported
$\omega^{2.38}$ and the verdict that the acoustic two-phonon channel is
closed ("Cherenkov no-go"). An adjudication committed the same evening
(`1e09d30`) refuted it: the no-go inequality holds only for same-sign pairs,
16 of 16 exact interior on-shell roots exist, and the run lacked the
golden-rule $1/d\omega$ normalization; a removed kinetic term in the vertex
was found later. The acoustic channel is **open**. The 18:49 and 19:13 run
outputs were never committed.

## 17.3 What the result is

$$
\boxed{\omega^7\ \text{is within-class occupancy evidence, not a universal GRUT prediction.}}
$$

"Occupancy evidence" means that the $\omega^7$ exponent class is inhabited
by at least one explicitly constructed, consistently coupled microscopic
sector. It is evidence that the class exists, not evidence that gravity's
actual dissipative response lies in it. Absolute exponents are never
compared across conventions; GR-1's own large-time slope, −8.975, is
reported only, because the sealed $t^{-8}$ class lives in the v3
convention. GR-1 also shows the discretized $\omega^7$ bath inside the
cone, with its vacuum exactly on the floor: gravity inherits ℏ as located;
it does not generate it.

**The Class-4 gate.** The program's criterion for a *forcing* derivation is
that a claimed derivation of a supplied input counts only if it strictly
reduces the total supplied content, without relocating, retyping, or
restricting scope. For the exponent, GR-1 froze the rule: the gate passes
only if no input beyond locality and symmetry is load-bearing. Measured:
- $\kappa\sim1/M_{\rm Pl}$ is **discharged** as amplitude-only: the slope is
  exactly invariant under rescaling it. This is not a derivation of
  Newton's constant.
- the minimal-stress coupling is **load-bearing**: the non-minimal
  counterfactual loses the +4;
- the retained-sector structure is **load-bearing**: a gapless sector is a
  precondition for any low-frequency response.

**The Class-4 gate remains open.** Its residual obstruction is exact: the
exponent is selected by counting *given* the coupling class, and the
coupling class is supplied (I1–I6). Class-4 has never been passed.

---

# 18. The TT graviton-response sector (TT-1; 9/10)

**Definitions and scope.** The stress tensor admits an improvement term
$\xi(\eta^{ij}k^2-k^ik^j)f$, where $\xi$ is its coefficient ($\xi=0$ is the
minimal coupling) and $f$ runs over a tower of higher terms. The
transverse-traceless projector about the graviton direction $\hat k$ is
$\Lambda(X)=PXP-\tfrac12P\operatorname{tr}(PX)$, with $P=\mathbb 1-\hat k\hat k$.
TT-1 treats tree-level emission of one on-shell graviton
($\Omega=\omega_1+\omega_2=\lvert k\rvert$, $c=1$) by a pair of
retained-sector quanta with momenta $p_1,p_2$, one isotropic dispersion per
sector, no loops, and computes no rate exponent.

## 18.1 ξ is irrelevant on the physical TT channel

Every improvement structure has a TT image at most $2\times10^{-15}$ of the
canonical vertex. The reason is structural [IDENTITY]:
- $\Lambda(kk)=0$;
- $\Lambda(\mathbb 1)=0$;
- $k^2=0$ on shell.

This is textbook transversality; its value here is classification. ξ remains
visible off shell and in the trace, so CP-1's finding for strain probes
stands.

## 18.2 Tensor structure

The TT tensor structure is forced within the tested class (rank 1 at every
point, $\lambda_2/\lambda_1\sim1.8\times10^{-16}$). So is the leading
infrared coupling: the higher-derivative form factor is suppressed as
$p^2$, exactly ×4.000 when $p$ doubles. Higher form factors are constrained
but not unique.

## 18.3 The rank-count red gate

The frozen prediction was rank 4; the measured rank is 3. An exact on-shell
identity in the linear sector explains the difference. With
$a=\lvert p_1\rvert$, $b=\lvert p_2\rvert$, $\omega_i=v\lvert p_i\rvert$, and
$(\omega_1+\omega_2)^2=\lvert p_1+p_2\rvert^2$,

$$
p_1\!\cdot p_2=\tfrac{v^2-1}{2}(a^2+b^2)+\omega_1\omega_2 .
$$

Curved dispersion restores rank 4. The frozen gate nevertheless **remains
RED**. A plausible explanation does not reclassify a failed gate.

## 18.4 Channel existence

| Retained-sector dispersion | Channel |
|--------------------|----------------------------------------|
| Exactly $v=c$, linear | **Dead**: the kinematics are collinear and the vertex vanishes identically |
| $v<c$, linear | **Open** (minimum vertex 0.032) |
| $v=c$ with subluminal curvature | **Open**, in proportion to the curvature (ratio 1.9975) |
| Superluminal curvature | **Closed**: no on-shell solution |

With per-sector $v=c$ units, the channel exists only through dispersion
curvature. That curvature is microscopic content the program has not
earned (I11), and the comparison of the sector's light cone with the
probe's is supplied (I6).

---

# 19. The 3D gravity red gate (GR-1)

GR-1 checked that the dimension entering the gravitational pair counting
equals the dimension recovered spectrally in Section 9. The log-slope of the
pair count should equal $2d$.

- In one dimension the gate passed: 2.222, inside $2\pm0.4$, on the chain
  where G-2 recovered $\hat d=1.000$.
- In three dimensions the frozen gate **failed and remains RED**: 5.362
  against $6\pm0.6$, a miss of 0.04 below the window.

A labeled diagnostic with the same frozen window on $13^3$, $21^3$, and
$31^3$ lattices gives $5.362\rightarrow5.493\rightarrow5.662$, rising
monotonically toward 6; on $13^3$ the lowest mode sits at 24% of the window
edge. This suggests a refinement for a future instrument whose rule must be
frozen in advance. It is not a repaired result: dimension consistency is
certified in 1D and indicated, not gate-certified, in 3D.

---

# 20. The formal theory datum (Formalizations 01 and 02)

A GRUT datum is

$$
\mathfrak D=(M,\mathfrak a,\varrho,\iota),
$$

where:
- $M$ is the microscopic model in an admitted class;
- $\mathfrak a$ is the access assignment (seed, closure, boundary events);
- $\varrho$ is a **state** on $M$'s algebra (the formalizations write it
  $\rho$; this record writes $\varrho$ to keep $\rho$ for the spectral
  measure);
- $\iota$ is the assignment of the conditional inventory (Section 21).

The **core datum** is $(M,\mathfrak a,\varrho)$. Two core data are
**representation-equivalent**, $\sim_{\rm rep}$, when an isomorphism of the
underlying algebras intertwines dynamics, state, and seed. The record's
controls verify that every core functional is constant on these classes
(Givens scrambles, exact Lanczos re-representation, congruence checks). The
core object is

$$
\mathrm{Core}:\ \mathbb D_{\rm core}/\!\sim_{\rm rep}\ \rightarrow\ (\mathcal C,\ \mathcal I,\ \mathcal I|_{\mathfrak a},\ \mathcal G).
$$

It satisfies seven compatibility relations:

| Relation | Content | Grade |
|--------------|----------------------------------|-------------|
| R1 kernel downstream | the kernel depends on model and access; exact spectral form; realization dimension = number of distinct eliminated modes | [DERIVED-IN-CLASS] |
| R2 admissibility | hierarchy positivity ⟺ state positivity; Gaussian face in the cone, vacuum on the floor | [IDENTITY] + [DERIVED-IN-CLASS] |
| R3 interface completeness | for declared access, in class, the accessible hierarchy tracks every physical difference | [DERIVED-IN-CLASS] |
| R4 counting | sector ↦ exponent class by locality and symmetry; per branch, masked at eigenvalue level (gate red) | [DERIVED-IN-CLASS] |
| R5 geometry from data | geometry is a function of accessible influence data; selection graded by access class | [DERIVED-IN-CLASS] |
| R6 unit-change coherence | dimensionless accessible data discriminate unit changes; co-stretch ≡ unit change | [IDENTITY] |
| R7 cross-fork datum sharing | the same data pushed through several maps give consistent outputs | checked property of the record |

**One theory on the core.** The statement that GRUT is one theory on the
core is a **checked property of the assembled record, not a theorem** about
all admitted models. Upgrading it would mean proving R1–R6 as class-level
theorems.

**Domain extension.** Following C1-a (Formalization 01 Amendment 02;
equivalently Formalization 02 Amendment 01), $\mathbb D_{\rm core}$ now
covers finite stepped nonstationary models, in class, as well as stationary
ones:

$$
\mathbb D_{\rm core}^{\rm stationary}\ \longrightarrow\ \mathbb D_{\rm core}^{\rm stationary}\cup\mathbb D_{\rm core}^{\rm stepped\ nonstationary}.
$$

This is the program's first actual domain extension.

**The conditional branch as an indexed family.** The inventory space is
$\mathbb I=\prod_{k=1}^{11}\mathbb I_k$. For each assignment $\iota$, the
fiber $\mathfrak T_\iota$ is the core object extended by the conditional
maps (conservation, universality, sector selection, unit change, gravity)
evaluated at $\iota$. The formalizations call the resulting family a
fibration,

$$
\pi:\mathfrak T\rightarrow\mathbb I_{\rm adm},\qquad \pi^{-1}(\iota)=\mathfrak T_\iota ;
$$

the word is used only for this indexed family, and no topological structure
is claimed. The campaign did two things to it, each demonstrated in class
by a chartered fork:

1. **It carved the base.** Six earned constraints carve the admissible
   region. Some remove assignments; the rest partition what survives:
   - a massless probe forces conservation (non-conserved couplings
     removed);
   - the cone cuts the classical carrier;
   - the sector class is reduced;
   - channel existence is partitioned by class;
   - universality is carved under exchange (non-universal clocks removed;
     decoupled assignments remain admissible);
   - the co-stretch dichotomy is real (both branches remain admissible;
     earned structure detects the difference but forbids neither).
2. **It refuted candidate sections.** A *section* over a coordinate is an
   earned map that would supply that coordinate from the core datum. Every
   attempted section family failed (P-6, CA-1, CC-1, U-1, SX-1, TT-1, P-2,
   and the prior Born-rule record).

> The fibers were not shown to collapse. The program mapped where they remain.

The termination points of the typed maps, where a map stops at a supplied
input or a seam, are part of the theory's content, not omissions from it.

---

# 21. The current primitive-input inventory

For most structural assumptions above the influence layer, the campaign
collapsed them into two stems: access, and probe structure. The quantum and
boundary-data inputs are priced separately.

**Stem A — access**
- **I1. Access seed.** A subalgebra of operators (Section 8.2). Not
  derived; physical at boundary changes.
- **I2. CARRIER.** The identification "geometry-recovery seed = probe access
  seed". Reduced to an access-seed coincidence (Section 15).

**Stem B — probe structure**
- **I3. The probe.** A massless, gauge- and Lorentz-redundant field with
  its coupling class. Supplied.
- **I4. Universal reach.** All sectors lie in one exchange-coupled
  component. **Supplied**: a probe coupled only through clocks mediates no
  exchange (U-1). Given I4, clock universality is derived in class; for
  sectors outside it, universality is irreducible.
- **I5. The co-stretch declaration (Sel-4x).** A rule for how constant
  probes act on intrinsic scales. Supplied.
- **I6. The cross-sector light cone.** A relation between sectors' light
  cones. Supplied; this is seam S2.

**Separately priced**
- **I7. ℏ.** Located as the height of the fluctuation floor; not derived.
- **I8. Born measure and outcomes.** Not derived; the tested routes were
  negative.
- **I9. Noncommutativity.** Supplied.
- **I10. States and boundary data.** Amplitudes, states, the direction of
  the arrow of time, the low-entropy past, and (on an expanding background)
  a state choice, a temperature structure, and a stationary reduction.
- **I11. Microscopic sector content.** The support of $\rho$, $\tau_0$, the
  exact retained sector, its dispersion, and its curvature.

The inventory states the boundary of what the program has derived.

**Certificate status** (Formalization 02 §3.2). No coordinate yet holds a
declared certificate.
- **I1 and I5** hold the *demonstration half* of an irreducibility
  certificate at stated scope: in-class exhibits of distinct values with
  identical accessible data.
- **I10** is the natural candidate for a domain datum.
- **I11** is the one coordinate with no certificate in either direction.

---

# 22. Seams, loopholes, and named obstructions

- **S1 — stationarity.** The finite stepped stratum is fully classified:
  the map and structure extend, and the packaging boundary is certified.
  Still open: C1-b (infinite volume) and C1-c (smooth modulation).
- **S2 — causal structure.** Spatial geometry is reconstructed in class,
  but no earned construction produces a common causal cone across sectors.
  Spatial and causal structure have not yet been derived from the same
  deeper data.
- **L1 — the free-sector loophole.** The retained free-phonon sector lies in
  the exception class of the clock-coupling ($O\propto H$) argument. This
  must be resolved before a self-consistent gravitational identification
  can be claimed.

**Named obstructions** (carried from Skeleton v02.1 §8 and Theory Paper
Working Draft 02 §7):
- **Weinberg–Witten** [WW80] constrains massless spin-2 particles in
  theories with a Lorentz-covariant conserved stress tensor. It is carried
  as a **named-exit condition**: any eventual completion must state which
  hypothesis it relinquishes. Keeping the probe supplied (I3) is how this
  record currently stands relative to it.
- **Soft-graviton universality** [†Wei64, †Wei65]. Universal stress
  coupling is *imported* here as the minimal-stress postulate. That import
  is where the no-go pressure on emergent gravity concentrates.
- **Lorentz recovery** is open: a retarded kernel selects a frame, and the
  constructions here are non-relativistic lattices.
- **Energy bookkeeping** (the Bianchi identity) is open.

---

# 23. The preserved red register

**Scope.** This table lists the frozen gates that failed in the chartered
forks on `master-w25bu9` (Appendix G). Its ten entries contain seventeen
failed gates, because G-1 alone contributes eight. Section 23.1 lists the
failed checks of the foundations record.

| Fork / gate | Status | What failed |
|------------------|-------|----------------------------------------|
| G-1 arrival-time geometry (eight gates) | **RED** | The arrival-time metric route fails in class: arrival-time functionals are not metric on the tested finite dispersive substrates at the tested scales |
| GR-1 3D dimension gate | **RED** | Measured 5.362 against a frozen $6\pm0.6$ |
| P-6 degenerate-companion gate | **RED** | Measured exactly 0.0. Diagnostic: the companion operator annihilates the reachable even-parity block |
| P-3 H3 eigenvalue gate | **RED** | Measured +2.216 against a predicted +4. Diagnostic: eigenvalue masking; +3.999 on the cancelled branch |
| P-4 order-8 window gate | **RED** | Measured 67.8 with non-asymptotic couplings. Diagnostic: 325 → 320 → 276, converging toward $2^8=256$ |
| EQ-1 static discriminator | **RED**; claim withdrawn | The "material mimic" was the geometric coupling in disguise (measured $2.7\times10^{-10}$ against > $10^{-3}$). The claim that static access separates what pair access cannot was withdrawn |
| RS-1 flexural gate | **RED** | Measured 3.744 against a predicted value above 4. Diagnostic: $R\sim Nr^2$ |
| TT-1 rank count | **RED** | Measured rank 3 against a predicted 4. Diagnostic: an on-shell identity |
| C1-a same-lag drift | **RED** | Measured 0.0498 against a threshold of 0.1. Diagnostic: the peak normalization is modulation-independent |
| C1-a local-anchor family | **RED** | The midpoint anchor measured 0.0494 against a threshold of 0.05 for every member |

**Relation to C1-a2.** The two C1-a reds are permanent. C1-a2 established a
new result on the same question under a new pre-registration; it did **not**
turn these reds green.

A red gate is not evidence against the whole theory. It is evidence against
the specific claim or instrument that the gate represents.

## 23.1 Failed checks in the foundations record

The foundations record (`adjudicator-track`, Section 4) predates the
charter protocol, and its failures are recorded here for completeness:

| Instrument | Failed | What failed |
|------------------|------|------------------------------------|
| irreversibility origin | 1 of 4 | the absorptive-spectrum sign check (Section 4.3) |
| minimal generative ontology | 1 of 6 | a derivative coupling outside the positive class; the check's summary contradicts its data |
| gravity-bath spectral match | 1 of 9 | discrete-box kernel correlation 0.43 / 0.29 against 0.98 |
| coarse-graining universality | 5 of 7 | five checks; several summaries contradict the recorded data |
| first coupling instrument | 4 of 9 | three exponent checks and the tidal control; the instrument was demoted and rebuilt (Section 17) |
| persistence origin P3, P4; spectrum E4a | 3 checks | failed before the same-day instrument repair (Section 4.1; Appendix C.1) |

---

# 24. The completion program

Completion means closing a finite set of typed problems. Each inventory
coordinate must reach one of three certified statuses (Formalization 02,
Definition 6):

1. **Derived section:** an earned derivation, certified by a chartered fork.
2. **Irreducible primitive:** an underdetermination demonstration at stated
   scope, followed by a declared axiom that carries the measured content.
3. **Domain datum:** explicit typing as boundary or state data within the
   theory's domain, plus a check that the theory's outputs are well
   defined given that datum.

GRUT is **closed as one theory** when the domain is enlarged across seams
S1 and S2 (or each seam is proved a permanent boundary, with its new
priced input named), and every coordinate carries one of the three
statuses with its certificate. The goal is not to make every primitive
disappear: "one theory" must not quietly mean "theory from nothing". What is
ruled out is an *uncertified* supplied input.

| Problem | Success | Irreducibility route | Current status |
|-------------|----------------------|----------------------|----------------|
| **C1** Stationarity seam | A nonstationary two-time kernel that reduces to the stationary one | Name the new priced structure the extension requires | **Finite stepped stratum classified** (C1-a, C1-a2). C1-b and C1-c open |
| **C2** Causal structure | A common cone from influence and access data under exchange | Show that relative cone data are not extractable at declared access | Open (seam S2) |
| **C3** Access seed | A selector that survives the P-6 battery | A full-scope underdetermination result plus a declared axiom | Strong partial evidence; not closed |
| **C4** Probe structure | Derive I3–I5 from declared alternatives | Classify the probe as an independent axis | Supplied |
| **C5** Quantum scale and outcomes | A generative account of the floor; a Born derivation that survives an adversarial battery | A classification-grade negative result | Open |
| **C6** Red gates | Separately frozen refinements, never reinterpretation | — | Open |
| **C7** External QFT confrontation | Map the retained-sector class onto the T3 anchor | — | Protocol adopted; not executed |

Listing a problem here does not imply that the program has a route to
closing it.

**Scope of C7.** C7 tests the conditional branch, not the core. It compares
the exponent class of the dissipative spectral density implied by the
conditional branch with the T3 anchor's, inside the anchor's validity
window. A mismatch there kills the gravitational identification, and the
core survives as generic open-system results. A class match would be weak
evidence, since matching one exponent class from a small discrete set is
not unlikely by chance. A pass discharges no stem and no seam. How the
matter-pair channel of Section 17 corresponds to the anchor's pure-graviton
loop is itself an open premise of C7. By a standing rider, any such
comparison must state the stationarity regime it assumes (Section 5).
Because C7's premises depend on the retained-sector selection, loophole L1
must be addressed in them.

## 24.1 The T3 anchor

The anchor is a standard-QFT computation: the Wigner-time-resolved
absorptive part of the one-loop pure-graviton self-energy on de Sitter
space, through order $H^6$, in the branch-cut class, with an $\omega^4$
flat-space limit, a dissipative sign, and a validity window
$\omega\gtrsim3.4H$ (here $H$ is the de Sitter Hubble rate). It is reported
in *Wigner-time structure of one-loop graviton dissipation in de Sitter
space* (D. Ryan Grover, version 1.0, 21 September 2026; frozen on branch
`physics-final` at `310101f`; present in the repository as
`GRUT_de_Sitter_Absorptive_Response_v1.0/`). It is the previous version of
this record under the same concept DOI.

- The object belongs to an established literature [TW96, TTW21]. What that
  paper certifies is its specific coefficient structure, not the object's
  existence.
- Its verification is in-house; it has not been externally reviewed.
- It is **not** a GRUT claim, and it is not evidence for GRUT. Its
  $\omega^4$ flat limit (in the self-energy convention) and the $\omega^7$ of
  Section 17 (in the v3 convention) cannot be compared without the
  convention map that C7 must supply.

---

# 25. Falsifiability

GRUT currently has no GRUT-specific derived prediction (Section 29). The
items below say how the declared layers or identifications could fail. The
spectral-form and cone layers coincide with standard open-system physics,
so a violation there would challenge that physics, not a GRUT-specific
hypothesis.

- **Spectral form.** The positive-measure form is a theorem for the declared
  passive class. It is falsified empirically only in a system that
  independent evidence places in that class; elsewhere a violation shows
  that the class does not apply. The record does not yet name any physical
  system as a claimed member of the class (a recorded gap, Skeleton v02.1
  §7).
- **Influence cone.** A realizable state in the declared Gaussian class
  outside $J\ge0$, $\nu\ge\hbar J/2$ would falsify the admissibility layer.
  Because the cone is state positivity (Section 6.4), such an observation
  would contradict the standard quantum mechanics of Gaussian open systems.
  Outside the class the cone does not apply.
- **Stationarity and packaging.** C1-a2 has a stated scope. Broader
  nonstationary classes can challenge whether the two-time datum is
  sufficient.
- **Gravity.** A mismatch in C7 would falsify the gravitational
  identification. It would not erase the continuum and influence results.
- **Cosmology.** The program's one cosmological channel concerns the
  dark-energy equation of state $w(z)$.
  - *The statement.* A single passive relaxation mode cannot carry $w$
    across $-1$ (a generic result [Vik05]). The earlier Program Record
    release (7 September 2026) stated that every purely relaxational kernel
    in GRUT's class stays on one side of $w=-1$, so an observed crossing
    would falsify the whole family, GRUT included.
  - *Its grade.* The program's own ledgers hold this "no-crossing"
    statement at to-derive grade: whether GRUT's vacuum-memory sector is
    such a mode depends on an unresolved link of its derivation chain, and
    the exclusion is shared by the whole passive class, not GRUT-specific.
  - *The sealed threshold.* A falsification threshold for DESI Data Release
    3 was pre-registered and sealed on 18 August 2026
    (`provenance/prereg/PREREG_DESI_DR3_2026-08-18_v3.txt`): a
    model-independent detection of $w(z)<-1$ at any redshift, at ≥ 5σ,
    robust across the release's headline data combinations, and published.
    The same file records that sustained non-crossing would confer no
    credit, and that the threshold is "this program's commitment about its
    own model, not a test the cosmology literature would recognize as
    addressed to it".
  - *Present data.* Published DESI analyses prefer evolving dark energy;
    the record cites about 3.1σ for DESI Data Release 2 with CMB data
    [DESI25]. The program's own assessment is that the framework is not
    falsified by present data.

---

# 26. What GRUT does not claim

GRUT does **not** currently claim any of the following:

- a completed theory of everything;
- a derivation of the Standard Model (the matter link is silent);
- a derivation of ℏ, of the Born rule, or of noncommutativity;
- absolute geometry, or a unique microscopic ontology;
- a universal single-pole or stationary memory kernel;
- an absolute $\omega^7$ prediction independent of sector and coupling
  assumptions;
- a completed gravitational identification, causal-cone derivation, or
  Class-4 result;
- resolution of every red gate;
- any confirmed novel quantitative prediction.

The claim this record supports is:

> Within the tested model classes, GRUT has constructed and stress-tested a bottom-up hierarchy in which local microscopic dynamics generate continuum spectra, memory, irreversibility, influence structure, and access-relative geometry. It has also identified, systematically, where quantum, causal, access, probe, and gravitational structure cease to be derived and must currently be supplied or tested further.

---

# 27. Relation to GRUT-RAI

GRUT-RAI is not the physical theory. It is the computational and provenance
infrastructure used to construct, test, audit, and preserve the theory. Its
roles include:
- implementing models;
- running pre-registered gates;
- committing charters before runs;
- storing SHA-256-hashed results;
- running counterfactual batteries;
- detecting instrument defects (halts);
- preventing narrative status inflation;
- maintaining the dependency ledger.

Its intended workflow is deliberately adversarial. A cycle runs:
1. hypothesis;
2. counterexample;
3. charter, committed to git;
4. instrument and run;
5. verdict;
6. owner ruling;
7. dependency update.

Appendix D states what the git record does and does not establish about
this ordering. RAI is a research instrument and a provenance system. It is
not an authority that can make a physical claim true.

---

# 28. Research provenance and publication-source rule

**Sources.** The authoritative snapshot is `master-w25bu9` at
`6abbf3164655c513b72dfc72f4a64013b061c489` (the source boundary),
together with the foundations record on `adjudicator-track` at
`90218f5`. The latter branch is not merged; its 51 files that are absent
from the publication branch are archived byte-exact, with SHA-256 sums, in
`archive/adjudicator-track_90218f5/`, so the deposit contains every source
this record cites.

Branch chronology does not revise the theory. Claims from the RRP line
(the Reality Requirements Program, recorded on `master` through `a2dcb02`,
the fork point of `master-w25bu9`) enter only through source inspection,
scope classification, and owner adjudication.

**The consolidated record draws on:**
- the foundations record (Section 4; Section 17's coupling instrument,
  sealed ledger, and adjudications);
- the non-stationarity, kernel-transport, and clock-mismatch instruments;
- the chartered forks P-1 to P-6, D-1, S-1; G-1, G-2, GS-1; GR-1, CP-1,
  EQ-1, S4-1, FS-1, CC-1, U-1, RS-1, CA-1, SX-1, TT-1; C1-a and C1-a2;
- GRUT Working Theory 01; Theory Paper Working Drafts 01 and 02;
  Formalizations 01 and 02, with their dated amendments;
- the de Sitter absorptive-response paper, as the T3 anchor
  (`GRUT_de_Sitter_Absorptive_Response_v1.0/`).

Appendix G gives commits, dates, and battery scores. Owner rulings are
recorded as files in the repository and on GitHub Issue #2; the issue
thread itself is not part of a repository snapshot.

> **How to verify a result.**
> ```
> git clone https://github.com/ryangrvr/GRUT-RAI
> cd GRUT-RAI && git checkout master-w25bu9
> cp -r calc /tmp/grut_calc && cd /tmp/grut_calc
> python3 c1a2_packaging.py
> ```
> - The campaign instruments are pure Python 3 standard library and
>   deterministic or fixed-seed. Each prints its battery (the command above
>   prints "7/7 gated checks passed") and writes its result file into the
>   parent directory, so run them from a copy, as shown, to avoid
>   overwriting the committed results.
> - Each result embeds its wall-clock run time, so a re-run's SHA-256 will
>   differ from the one quoted in the verdict, while every recorded number
>   should agree. For all 24 forks, the SHA-256 prefix quoted in the verdict
>   matches the committed result file.
> - The foundations instruments are in `archive/adjudicator-track_90218f5/calc/`.
>   Six are pure standard library; the others need `numpy` (and two need
>   `scipy`), with Python 3.12 recorded as the tested environment.

This manuscript and its release tooling were committed after the source
boundary. They add no computation and change no status.

---

# 29. History, standing gradings, governance, and record integrity

Several earlier GRUT formulations were materially stronger than the present
record supports. They are kept as history, not as claims.

## 29.1 Release history

| Date | Release | Status now |
|----------|--------------------------------------|----------------------|
| Dec 2025 – May 2026 | Closure Framework v1–v11; Phase I–III protocol deposits (e.g. 10.5281/zenodo.18008060); canonical builds (branch `v1-retired`); early GRUT-RAI software versions | Superseded |
| Apr – Jun 2026 | GitHub releases v2.1.0 to v10.0, including "zero free parameters in the predictive core", "R ≈ 1.154 with 0.28% precision", and "candidate Theory of Everything" | Superseded. Nothing from these lineages is carried unless re-derived under the current discipline |
| 18–19 Jun 2026 | GRUT ToE v3.0.0, "The Corrected Physical Picture" (a 32σ CMB–ISW exclusion; a 689 Hz decoherence plateau) | Superseded; the 32σ figure recomputes to about 2.0σ |
| 21 Jun 2026 | *GRUT ToE v4.0 — The Emergence of Everything — Candidate Framework* (10.5281/zenodo.20783057, under concept DOI 10.5281/zenodo.19803663) | **Withdrawn** by its author (see the Notice at the front of this record) |
| 7 Sep 2026 | GRUT v5.0 *Program Record*: Books I–X working edition and the RAI audit infrastructure (under the same concept DOI) | Retired the theory-of-everything claim; superseded where it conflicts with this record |
| 21 Sep 2026 | *Wigner-time structure of one-loop graviton dissipation in de Sitter space*, v1.0 (the previous version of this record) | Stands as a standalone standard-QFT result and the C7 anchor (Section 24.1) |
| 25 Sep 2026 | The owner's draft of this record (`uploads/GRUT_Consolidated_Theory_2026-09-25_DRAFT_as_received.md`) | Superseded by this edition |
| 26 Sep 2026 | This record (10.5281/zenodo.22983638) | Current |

Version DOIs that the repository does not record are not given here; the
Zenodo concept record lists every version.

## 29.2 Closure and reopening

- **Closure (23 September 2026).** The owner formally closed the program
  (`GRUT_PROGRAM_CLOSURE_01.md`). The closure recorded that the
  distinctive-theory claim failed, the theory-of-everything claim was
  retired, and no GRUT-specific prediction survived. It graded the founding
  hypothesis "unevaluated at its own claim point — neither proven nor
  disproven". An owner amendment the same evening added that the closure
  "closes the construction, not the question that motivated it".
- **Reopening (25 September 2026).** The owner reopened the program as a
  theory-development effort (`GRUT_PROGRAM_REOPEN_01.md`), with the object
  "exhibit the mathematics of the theory — show how it works — before any
  external claim is made". The closure document is not retracted: it stands
  as the accurate record of the 23 September boundary. **Reopening is not
  rehabilitation**: every standing grading below carries over.

## 29.3 Standing gradings

- **Predictions.** The GRUT-specific prediction ledger stands at **zero
  derived predictions**. The signature audit found no admissible,
  parameter-free observable that distinguishes GRUT from standard physics
  (verdict EMPTY).
- **The distinctive-theory adjudication**, run twice on 4 and 5 September
  2026 (a structural theory search with a blind hostile pass, and a
  resurrection audit), **failed** both times as scoped: the framework "fails
  to constitute a distinctive physical theory". That is not the same as
  "the responsive-vacuum hypothesis is false".
- **The founding bet**, a finite single-pole vacuum memory kernel, is
  **negated in its strongest form**: exact de Sitter free-field theory
  forces scale-free (power-law) memory at the computed order. The current
  theory builds on the computed structure; it does not re-argue the
  original ansatz.
- **The withdrawn June 2026 deposit** (10.5281/zenodo.20783057) stays
  withdrawn. Nothing in it is cited as a result.
- **Earlier no-go results stand at their recorded strengths** (see
  `NO_GO_LEDGER.md`):
  - *The α-bridge is settled-negative.* The hoped-for derivation of the
    tensor-response amplitude from the conformal-anomaly ratio $a/c=1/3$
    fails: the two anomalies live in different spin channels.
  - *μ = 4/3 is excluded.* The super-horizon enhancement of structure growth
    that GRUT's conformal coefficient naively suggests fails a
    separate-universe consistency argument and is disfavoured empirically
    at a joint ~4σ class (ISW cross-correlation ~2.0σ; DESI lensing
    ~3.5σ).
  - *General relativity is recovered with imports, not derived* (Section
    12).
  - *The Born rule is borrowed.*

**Demotions forced by the campaign:**
- the single-pole kernel is not selected;
- $\tau_0$ is not generated;
- the kernel sits downstream of partition, state, and access;
- $(K,N)$ is not the whole interface;
- geometry is access-relative;
- stationarity is a regime;
- the gravity coupling is conditional on the supplied probe;
- $\omega^7$ holds within its class;
- ℏ is located, not derived;
- Born outcomes are unresolved.

## 29.4 Governance at publication

- **External review is deferred by owner direction.** Direction D-1 of the
  reopening ruling (25 September 2026) reads: "No dispatches, no
  solicitation of outside review, until the owner rules the mathematics
  stands." It requires every artifact to carry the standing disclosure that
  no outside human has reviewed any of the work; this record does so. D-1
  is not recorded as lifted. Publishing this record is an owner act, and it
  does not solicit review.
- **Reviewer vocabulary in the repository.** Where repository files speak of
  "external", "specialist", "referee", "hostile", "blind", or "independent"
  reviewers, these were AI sessions run by the owner. No transmission to any
  outside human is logged at any date (`docs/WHERE_IT_STOPS.md`); older
  wording to the contrary (for example in `STATE.md`) is superseded by that
  finding.
- **The signed termination condition.** A termination condition for
  in-house GRUT physics (version 4) was signed on 10 August 2026 and is in
  force. In-house calculation stops at the earliest of 31 December 2026 or
  its other stated conditions, after which a deposit reports each of five
  named channels in one line. No stop condition has fired, and this record
  is not that deposit. The reopening ruling states that it cannot discharge
  or amend the signed condition; the owner's reconciliation of the two is
  owed.
- **The sealed DESI DR3 threshold** (Section 25) is in force. Whether it is
  the frozen crossing threshold that the termination condition's
  cosmological channel requires has not been adjudicated.

## 29.5 Record integrity

- **Five narrative-versus-run mismatches** are documented in Skeleton v02.1
  §10, cases in which a verdict's prose asserted what its checks had not
  shown:
  1. a kernel-exponent mismatch, $t^{-d}$ against $t^{-d/2}$
     (continuum origin; repaired);
  2. a $t^{-3}$ against $t^{-4}$ inconsistency (spectral match; corrected in
     the script, while the committed result still carries $t^{-3}$);
  3. a coupling verdict describing a run that did not happen (found by
     adjudication);
  4. persistence and representation prose asserting a theorem whose checks
     had failed (P3, P4, E4a; found by two AI record-verifiers);
  5. a kernel tail computed from a refuted pre-registration (repaired).

  The systemic fix is that the coupling instrument now assembles every
  verdict string from measured variables.
- **The asymmetric error budget.** An audit of 4 September 2026 found that
  negative results had faced none of the checks applied to positive ones
  (`RAI_GRUT_RESURRECTION.md`). The codified response is the N1–N10
  negative-control standard, including displaced-gate mutation testing. It
  is graded only partially repaired, "a detector, not a certifier", and only
  N4 and N5 have committed definitions. The red-gate discipline complements
  it by keeping failed gates from being softened by prose. The "Cherenkov
  no-go" of Section 17, accepted and refuted the same evening, is an
  example of the asymmetry.
- **The foundations repair.** The same-day repair of 24 September 2026
  regenerated the failing results in place at the branch head. That departs
  from the program's earlier rule that a contaminated instrument is not
  patched; the originals survive in git history (Appendix C.1).
- **Found in preparing this edition** and disclosed in Sections 4 and 17:
  checks asserted in code rather than computed, a possible sign-convention
  defect, summaries that contradict their data, and sealed gates without
  implementation.

These are part of the record.

---

# 30. The best current conceptual picture

The program's working picture is a heuristic, not a result. It reads, in
the tested classes:

$$
\boxed{\text{locality}\rightarrow\text{hidden modes}\rightarrow\text{continuum spectrum}\rightarrow\text{memory}\rightarrow\text{influence hierarchy}}
$$

$$
\boxed{\text{influence hierarchy}+\text{access}\rightarrow\text{recoverable spectral structure}\rightarrow\text{geometry}}
$$

and, conditionally,

$$
\boxed{\text{influence}+\text{access}+\text{geometry}+\text{probe structure}\rightarrow\text{effective sector}\rightarrow\text{gravitational-side response}}
$$

> **Observable physical structure can be understood as a hierarchy of constraints generated by local dynamics and revealed through access, with memory, dissipation, spectral structure, and geometry emerging at successive coarse-grained levels.**

The arrows differ in status. The first line is derived in class or
family-fact; the second is derived in class and access-relative; the third
is conditional on the supplied inputs I1–I6. The gravitational
interpretation is a further identification, graded hypothesis. It is not
the definition of the core.

## 30.1 Claim hygiene for citation and reuse

- **A constructive mechanism is not ontological uniqueness.**
- **An in-class derivation is not Class-4 forcing.** Fixed sector,
  coupling, probe, access, or state assumptions remain dependencies of the
  result.
- **Interface completeness is scoped** to the declared model and access
  class.
- **Geometry recovery is access-relative.**
- **The gravity branch is conditional.** Its classes and exponents are not
  universal predictions.
- **Red means red.** An explanation does not change a status.
- **Standard mathematics stays standard.** Where Section 2.1 or Section 31
  marks an ingredient as standard, the record claims its in-class
  verification and its place in the map, not its discovery.
- **Provenance machinery is not physical evidence.**

---

# 31. Theory ledger at this source boundary

"Kind" separates what the program re-demonstrated from what it found: **S**
= a standard ingredient, re-demonstrated in class; **P** = a
program-specific in-class finding, not checked against the literature for
priority; **—** = a supplied, open, or failed item.

| Layer | Present status | Kind |
|---------------|--------------------------------------|----|
| Local microscopic dynamics | Constructive classes (Section 3.3); no unique ontology | — |
| Exact finite reduction (memory) | **DERIVED-IN-CLASS** | S |
| Continuum emergence | **FAMILY-FACT** (tested infinite-volume families; the finite reduction is DERIVED-IN-CLASS) | S |
| Irreversibility (existence) | **FAMILY-FACT**, as effective coarse-grained response; its direction is **SUPPLIED** | S |
| Positive spectral measure (class (a)) | **DERIVED-IN-CLASS** | S |
| Recovery of $\rho$ from the kernel | **CONSTRAINED**; unique only for light tails | S |
| Spectral content of $\rho$ (support, $\tau_0$) | **SUPPLIED** (I11) | — |
| Nonstationary extension of the core map | **DERIVED-IN-CLASS** (finite, stepped) | P |
| Stationary packaging off stationarity | **Certified not to package** (finite, stepped, at the stated scope) | P |
| Two-time packaging datum | **Exhibited constructively**; minimality open | P |
| Gaussian influence cone | **DERIVED-IN-CLASS**; borrowed-standard mathematics | S |
| ℏ | **SUPPLIED** (located) | — |
| Full influence hierarchy | Complete interface **in class**; its positivity is an [IDENTITY] | S |
| Born rule | **SUPPLIED / UNRESOLVED** | — |
| Noncommutativity | **SUPPLIED** | — |
| Access relativity | **DERIVED-IN-CLASS** | P |
| Access seed | **SUPPLIED**; seed-to-closure map non-injective | P |
| Medium versus relational | Representational at fixed influence data, **in class** | S |
| Geometry reconstruction | **DERIVED-IN-CLASS**, access-relative (partial spectral geometry) | S, P |
| Absolute geometry | **UNRESOLVED** | — |
| Unit change | Co-stretch ≡ unit change [IDENTITY]; rigid stretch observable | S |
| CARRIER | **SUPPLIED**; reduced to an access-seed coincidence | P |
| Probe structure | **SUPPLIED** | — |
| Universal reach | **SUPPLIED** | — |
| Clock universality | **DERIVED-IN-CLASS** under exchange, given reach and the supplied probe; irreducible for decoupled sectors | S |
| Retained sector | Class **DERIVED-IN-CLASS**, conditional on CARRIER and the supplied probe, relative to the tested candidates; flexural gate **RED**; member **SUPPLIED / UNDEFINED** (I11) | P |
| $\omega^7$ | Within-class occupancy evidence; not absolute | P |
| TT tensor structure and leading IR coupling | **DERIVED-IN-CLASS** | S |
| TT higher form factors | **CONSTRAINED**; rank-count gate **RED** | — |
| 3D gravity consistency | **RED** | — |
| Gravity as the memory bath | **HYPOTHESIS**; spectrally viable (8/9); not derived | — |
| Causal / light-cone structure | **SUPPLIED** (S2) | — |
| Class-4 gravity | **OPEN**; never passed | — |
| External QFT confrontation (C7) | **OPEN** | — |
| Confirmed novel predictions | **None** | — |

---

# 32. Present status in one statement

As of 26 September 2026, at the source boundary defined at the beginning
of this document:

> **GRUT has earned a generative open-system core. In it, within the admitted model classes, strictly local microscopic dynamics produce continuum spectral structure, persistent memory, effective irreversible response, and an influence hierarchy that is complete as an interface within the declared model and access class. Sufficiently rich access reconstructs tested graph and substrate geometry from accessible influence functionals. The core construction extends constructively to finite stepped nonstationary dynamics, where a pre-registered certification at the stated scope (with its calibration disclosed) finds that no single stationary spectral measure or $\Delta t$-only kernel packages the response. A conditional chain from influence, access, and geometry to a gravitational-side response has been organized, within the tested scope, into an explicit inventory of named primitive inputs and unresolved seams. The theory remains incomplete in the full nonstationary limit, causal structure, access-seed selection, probe derivation, quantum scale and outcomes, the gravity red gates, and external gravitational confrontation. It has no confirmed novel quantitative prediction, and no outside human has reviewed it.**

This is the strongest statement the recorded evidence supports at this
source boundary.

---

# Appendix A — Core mathematical statements

| | Statement | Scope and grade | Kind |
|---|------------------------|------------------------|---|
| A.1 | $\dot q=-K_{SS}q+\int_0^t k(t-s)q(s)\,ds+\eta$, with $k(\tau)=\sum_l u_l^2e^{-\lambda_l\tau}$, $\lambda_l>0$ | Class (a); exact; [DERIVED-IN-CLASS] | S |
| A.2 | $k(\tau)=\int e^{-\tau/\theta}\,d\rho(\theta)$, $d\rho\ge0$ | Class (a), stationary; [DERIVED-IN-CLASS] (form) | S |
| A.2′ | $K_0(t)=\int\cos(\omega t)\,d\mu(\omega)$ | Class (b), infinite-volume limit; [FAMILY-FACT] | S |
| A.3 | $J(\omega)\ge0,\ \nu(\omega)\ge\frac{\hbar}{2}J(\omega)$ | Declared Gaussian class; [DERIVED-IN-CLASS], borrowed-standard | S |
| A.4 | $k(t,s)=k(t-s)$ | Only on stationary backgrounds; recovered exactly when time-translation invariance is restored | P |
| A.5 | $k(t,s)$ is two-time, packaged by $[\{\lambda_e,u_e\},\{C_{e'e}\}]$ | Finite stepped class; packaging boundary certified at stated scope; minimality open | P |
| A.6 | Influence-hierarchy positivity ≡ state positivity | [IDENTITY]; holds off stationarity by measurement | S |
| A.7 | $\mathfrak D=(M,\mathfrak a,\varrho,\iota)$, with $\varrho$ a state | Definition | — |
| A.8 | $\pi:\mathfrak T\rightarrow\mathbb I_{\rm adm}$ | Definition; the base is carved in class | — |

# Appendix B — Major counterexamples that shaped the theory

1. **Single-pole non-uniqueness.** Many passive finite-memory kernels
   satisfy the same generic principles, and de Sitter forces scale-free
   memory at the computed order.
2. **KMS non-selection.** KMS and FDT states are points inside the cone.
3. **Medium/relational degeneracy.** Non-isomorphic baths share the same
   influence data (D-1).
4. **Higher-cumulant obstruction.** Identical $(K,N)$ can give different
   probe physics (P-3).
5. **Access-seed non-uniqueness.** Identical closures can hide physically
   different seeds (P-6).
6. **Single-site geometry collapse.** A 2D grid and a 1D chain are
   identical from one site (G-2).
7. **The topology horizon.** Rings are indistinguishable below
   circumference order (G-2).
8. **Arrival-time failure.** Time of flight is not metric on the tested
   dispersive substrates (G-1).
9. **Exponent-locus non-uniqueness.** A plane of couplings gives the same
   exponent (CP-1).
10. **A surviving non-conserved coupling.** The phonon mass modulation
    passes every earned constant-level selector (CC-1).
11. **The free-sector conservation tower.** A free ring has $2R$ local
    conserved charges within range $R$ (FS-1).
12. **Carrier non-uniqueness.** Four sectors carry identical geometry
    (CA-1).
13. **Exact-light-cone death of the TT channel** (TT-1). For an exactly
    light-cone-matched linear sector ($v=c$), the on-shell locus is
    collinear and the TT vertex vanishes identically.
14. **C1-a's normalization defect.** Peak normalization suppresses
    nonstationarity.
15. **C1-a2's stationary specificity control.** A different stationary
    kernel leaves the nonstationarity statistic at numerical zero.
16. **The refuted "Cherenkov no-go."** A same-evening adjudication found
    the acoustic channel open (Section 17).

These counterexamples are part of the theory's evidentiary structure.

# Appendix C — The red-register rule

> **No red gate changes status through prose, reinterpretation, denominator changes, or retrospective threshold adjustment.**

A failed gate stays red permanently. Its question can be re-tested only by
a separately chartered refinement or an independent experiment whose scope,
threshold, and adjudication rule are frozen before evaluation; such a
re-test establishes a new result, and the original gate stays red. C1-a
and C1-a2 are the worked example: C1-a's two reds are permanent, and
C1-a2's certification is a new result under a new pre-registration, with
its calibration disclosure on the face of its charter.

## C.1 Instrument repair versus gate failure

- **Halts.** In the chartered campaign, an instrument that breaches an
  analytic identity halts: "instrument bug, never physics", and no verdict
  may be issued from that run. A halt is not a red, and the repaired run is
  a new run.
- **Gate failures.** A frozen gate that fails stays red. A labeled post-hoc
  diagnostic may be recorded beside it, but no gate is repaired and no
  re-run is tuned.
- **The foundations exception.** The one place in this record where failed
  checks were re-banked after repair is the foundations record's same-day
  repair set of 24 September 2026 (`5f5395e`). P3 had recorded the
  closed-loop rate instead of the kernel; P4 had a variable-shadowing bug
  and degeneracy-prone sampling; E4a compared a density with a step; and
  the coupling instrument had three defects (Section 17). The repairs were
  authorized by the owner and were not separately chartered. The failing
  results were regenerated in place; the originals remain in git at
  `affdf52`. The failures are listed in Section 23.1, and readers should
  weigh results re-banked after same-day repair accordingly.

# Appendix D — Methods: the research protocol and the role of AI agents

## D.1 The intended cycle

1. State the claim.
2. Identify the minimal assumptions.
3. Enumerate counterexamples.
4. Commit a charter (question, thresholds, decision rule) to git.
5. Implement the instrument.
6. Execute, without post-hoc tuning.
7. Preserve the failures.
8. Classify the result.
9. Obtain the owner ruling.
10. Update the dependency graph, and only then the theory ledger.

## D.2 What "pre-registered" means here, and what it does not establish

- For each of the 24 chartered forks of Appendix G, a charter file was
  committed alone, and the instrument, result, and verdict were then
  committed together in the next commit. Each verdict commit's parent is
  its charter commit.
- The gap between the two commits ranged from 76 s (SX-1) to 676 s (G-1),
  with a median of about 3 minutes.
- Because each instrument is first committed together with its result, the
  git record shows that each charter preceded its recorded result. It does
  not by itself show that no instrument was drafted or trial-run before its
  charter was committed; that rests on the operator's process. Git
  timestamps are set by the committer, and no third-party timestamping was
  used. No run logs are committed.
- All 24 forks were chartered, run, and adjudicated on 25 September 2026,
  between 03:42 and 22:37 UTC. The foundations record was produced on
  24 September 2026 without separately committed charters.
- **Calibration disclosures.** C1-a2's thresholds were set from C1-a's
  labeled diagnostics, as its charter states. No general record states who
  set the numerical thresholds of the other charters.

## D.3 The role of AI agents

- Charters, thresholds, instruments, verdicts, the formalizations, and this
  manuscript were drafted by AI agents under the owner's direction; the
  campaign's commits are authored `Claude`.
- Owner rulings were given by the owner and recorded by the agent "from the
  owner's own words", with any misstatement to be corrected by owner edit.
- On the foundations branch, "builder" and "adjudicator" are AI-operated
  roles under the owner's direction, working in separated trees.
  "Independent" there means separate processes and sealed commits, not
  external review.
- AI agents supplied computation, code, analysis, counterexample
  construction, document synthesis, and audit. They supply no authority.
  The physical status of a claim comes from the recorded construction, the
  committed instrument and result, and the explicit scope.

## D.4 Battery counting

A battery score is checks passed out of the total, as recorded in each
fork's verdict. Through SX-1 the total counts every battery line, including
frozen readings and labeled diagnostics; TT-1, C1-a, and C1-a2 count gated
checks only. On gated checks alone, for example, G-1 is 9/17, P-6 is 23/24,
and P-1 is 4/4. Failure counts do not depend on the convention. No record
explains the change of convention.

## D.5 Author, funding, and competing interests

The author is D. Ryan Grover, an independent researcher, the program's
owner and sole human participant. No funding and no competing interests are
declared in the record.

# Appendix E — The current research frontier

**Foundational:**
- C1-b and C1-c (the remainder of S1);
- C2 (causal cone, S2);
- C3 (access seed);
- C4 (probe structure);
- C5 (ℏ, Born outcomes, noncommutativity).

**Integrity:** the ten red-register entries of Section 23 (seventeen failed
gates in all, eight of them G-1), plus the foundations-record failures of
Section 23.1. The two C1-a reds are permanent; their question is answered by
C1-a2.

**Identification:**
- L1 (the free-sector loophole);
- the Class-4 gravitational coupling;
- C7 (the external QFT confrontation).

These answer different questions, and none may be silently substituted for
another.

# Appendix F — Publication note and citation

This document is the Zenodo-facing statement of the current GRUT theory. It
should be cited together with the GRUT-RAI repository snapshot, and with
the committed artifacts whenever a claim needs numerical provenance.

**Recommended citation:**
Grover, D. Ryan (2026). *GRUT — Grand Responsive Universe Theory:
Consolidated Theory, Formal Architecture, Results, Limits, and Completion
Program.* Consolidated Research Record 02 (public-record edition),
26 September 2026. Zenodo. <https://doi.org/10.5281/zenodo.22983638> (this
version). All versions: <https://doi.org/10.5281/zenodo.19803663>.

**Software and provenance archive:** Grover, D. Ryan (2026). *GRUT-RAI:
research and provenance infrastructure for the GRUT program.* Zenodo. All
versions: <https://doi.org/10.5281/zenodo.18993689>. The release
corresponding to this record carries its own version DOI, minted on
deposit.

**Repository:** `https://github.com/ryangrvr/GRUT-RAI`, branch
`master-w25bu9` (source boundary `6abbf316`), with the foundations record
of branch `adjudicator-track` (`90218f5`) archived in
`archive/adjudicator-track_90218f5/`.

**Version label.** "Consolidated Research Record 02" is the owner's label.
No document titled Consolidated Research Record 01 is deposited or held in
the repository; the earlier in-repository consolidations are GRUT Working
Theory 01 and Theory Paper Working Drafts 01 and 02.

**License and copyright.** © 2026 D. Ryan Grover. This document and its
Zenodo deposit are released under the Creative Commons Attribution 4.0
International license (CC BY 4.0). The source code in the repository is
also available under the MIT License (`LICENSE`).

The Zenodo record should preserve the repository snapshot that corresponds
to this publication. This consolidation does not replace the detailed
computational artifacts.

# Appendix G — Campaign index (for archival verification)

## G.1 The chartered forks

All forks are on `master-w25bu9`. "Battery" is the score recorded in each
fork's verdict (Appendix D.4). "Gap" is the time from the charter commit to
the verdict commit. All verdicts are dated 25 September 2026 (UTC).

| Fork | Question | Verdict (recorded strength) | Battery | Charter → verdict | Gap (min) | Verdict (UTC) |
|-----|----------------|----------------------|-----|---------------|----|-----|
| P-1 | Can a subsystem be derived from correlations? | Regime trichotomy (structured / symmetric / generic), in class | 6/6 | `3bba895` → `aa569ce` | 4.4 | 03:47 |
| D-1 | Medium or relational, at fixed $(K,N)$? | Distinguishable mathematically; representational at system-limited access, in class | 13/13 | `53ab11f` → `baa64dc` | 4.2 | 04:03 |
| P-2 | What minimally constrains realizable $(K,N)$? | Cone confirmed: exactly two inequalities, in class; borrowed-standard | 16/16 | `291c23a` → `80982c1` | 2.3 | 04:38 |
| S-1 | What selects a sector? | Selection by class (counting); no tested extremum | 18/18 | `351a326` → `cd3f7e3` | 2.8 | 04:46 |
| P-3 | Does the cone survive noncommutativity? | Survives; null as a new principle; $(K,N)$ is a projection | 24/25 | `78b188e` → `b05c99f` | 5.3 | 05:01 |
| P-4 | Is the hierarchy characterized? | Characterized and reducible; ladder established | 21/22 | `d0fc014` → `d24b1bb` | 4.3 | 05:12 |
| P-5 | Does a principle hide in access? | No; the seed is irreducible | 22/22 | `4013a32` → `eedd0ca` | 4.4 | 05:22 |
| P-6 | Is the seed dynamically selectable? | No: non-derived input | 38/39 | `179c108` → `ee21a45` | 5.6 | 05:45 |
| G-1 | Arrival-time geometry | Partial; eight reds | 26/34 | `f9b043b` → `aba55f1` | 11.3 | 06:12 |
| G-2 | Spectral geometry | Partial spectral geometry; single-site underdetermined | 35/35 | `c83e9d7` → `d612e2c` | 5.9 | 06:26 |
| GR-1 | The gravitational influence point and Class-4 | Admissible; selected by structure in class; Class-4 open | 30/31 | `ece56e7` → `d827a32` | 6.5 | 07:02 |
| CP-1 | Minimal-stress coupling | Splits by dimension; reduced to geometric coupling | 39/39 | `d78f9a4` → `5f5bd77` | 2.6 | 11:06 |
| EQ-1 | Geometric-only coupling | Reduced to Sel-4 | 45/46 | `708a31b` → `6e66e28` | 3.2 | 15:15 |
| S4-1 | Sel-4 | Splits by part and class | 28/28 | `e83b6f0` → `b2a2892` | 2.8 | 15:27 |
| FS-1 | The free-sector exception | Structural; $O=H$ not selected | 31/31 | `19fd85f` → `c0099da` | 2.4 | 15:51 |
| CC-1 | C_cons | Irreducible; reduced to the massless probe | 29/29 | `86a839f` → `17c4395` | 2.8 | 16:23 |
| U-1 | Clock universality | Class split: derived in class under exchange, given the supplied probe | 23/23 | `f31ab7d` → `8e3232b` | 2.0 | 16:39 |
| RS-1 | Retained sector | A class selected in class, conditionally | 27/28 | `1f18205` → `a83421f` | 1.8 | 18:31 |
| CA-1 | CARRIER | Irreducible; an access-seed coincidence | 23/23 | `e67b1d5` → `a1ad8f9` | 1.3 | 18:37 |
| GS-1 | Geometry selection | Splits by access | 19/19 | `7837fb2` → `8698f05` | 1.9 | 18:45 |
| SX-1 | Sel-4x (length equivalence) | Irreducible; the co-stretch declaration | 23/23 | `3857e64` → `42e94cc` | 1.3 | 19:01 |
| TT-1 | The physical TT channel and ξ | ξ irrelevant; tensor forced; existence splits by class | 9/10 | `b4a2f33` → `ff3266d` | 4.0 | 19:14 |
| C1-a | The stationarity seam: the map ε | ε extends; continuity and structure hold; packaging not certified | 10/12 | `fa6ac44` → `55a708d` | 6.7 | 22:02 |
| C1-a2 | The packaging boundary | **Certified** (finite stepped, in class) | 7/7 | `3b139ab` → `4deda60` | 1.9 | 22:37 |

The owner's acceptance of C1-a2 (Formalization 02 Amendment 02) is commit
`6abbf316`, 26 September 2026, 02:54 UTC: the source boundary.

## G.2 Other instruments and records cited

| Instrument or record | Branch | Result | Battery | Commit(s) |
|----------------|----------|------------------------|-----|-----------------|
| Non-stationarity measurement | `master-w25bu9` | Two-time at order unity on the sampled grid ($R=0.516$; drift 1.53) | 7/7 | charter `eb3fc07`; result `5ea380e`; Correction 01 `6fc5139` |
| Kernel transport | `master-w25bu9` | No tested local rule transports beyond ~$0.25/H_0$ | 11/11 | charter `c30f18e`; verdict `05226bf` |
| Clock mismatch | `master-w25bu9` | Comparison underdetermined | 23/23 | charter `b25d79f`; verdict `65774e4` |
| Foundations instruments (Section 4.5) | `adjudicator-track` | See Section 4.5 | various | first committed `affdf52`; repairs `5f5395e` |
| Coupling instrument v3 | `adjudicator-track` | `derived_within_class_onshell_omega7_channel_open` | 20/20 | `5f5395e` |
| Sealed analytic ledger (T2 theorem gate) | `adjudicator-track` | Exponent gate G5: $7.00\pm0.05$ (propagator convention) | — | `d2da3a5` |
| Coupling adjudications 01–03 | `adjudicator-track` | 03 refutes the "Cherenkov no-go" | — | `36caf65`, `ebb3a42`, `1e09d30` |
| GRUT Skeleton v02.1 | `adjudicator-track` | Foundations synthesis | — | `90218f5` |
| T3 anchor (de Sitter paper v1.0) | `physics-final` | Standard-QFT result | — | `310101f` |

# Appendix H — Glossary

- **Access (𝔄).** Which operators an observer or probe couples to (the
  *seed*), everything they generate under products and time evolution (the
  *closure*), and changes of the seed (*boundary events*). Section 3.1.
- **Adjudicator, builder.** AI-operated roles under the owner's direction
  on the foundations branch: one builds instruments, the other derives
  analytic expectations and audits (Appendix D.3).
- **Battery.** The full set of checks run by one instrument (Appendix D.4).
- **Branch (exponent).** One channel of a matrix-valued influence, with its
  own exponent class (Section 7).
- **CARRIER.** The premise that the sector the gravitational probe couples
  to is the sector whose static response carries the recovered geometry
  (Section 15; I2).
- **C_cons.** The requirement that the probe's constant limit couples to a
  conserved local charge, $[O,H]=0$ (Section 13.1).
- **Charter.** The pre-registration committed before a run: question,
  thresholds, and decision rule (Appendix D.2).
- **Class-4 gate.** The criterion for a forcing derivation: it counts only
  if it strictly reduces total supplied content; for the exponent, only if
  nothing beyond locality and symmetry is load-bearing. Never passed
  (Section 17.3).
- **Co-stretch.** A rescaling of every coupling, intrinsic scales included:
  a pure unit change (Section 10).
- **Completely monotone.** A kernel that is a positive mixture of decaying
  exponentials (Section 4.4).
- **Continuum map ε.** The core's map from microscopic model to continuum
  structure (Sections 5, 20).
- **Domain datum.** A coordinate typed as boundary or state data, with a
  well-definedness check; one of the three closure statuses (Section 24).
- **Earned.** Established by the program's own committed instruments at
  [DERIVED-IN-CLASS] strength or better; the opposite of supplied.
- **Fork.** One chartered investigation (for example P-2 or CA-1).
- **Gate.** A single pre-registered pass/fail test within a battery.
- **GeoInv.** An unpromoted candidate: a constant probe must not rewire a
  sector's recovered hop geometry (Section 14).
- **Halt.** An instrument stop on an analytic-identity breach: "instrument
  bug, never physics". "Halt-grade" identities are checks whose failure
  would halt the run (Appendix C.1).
- **In class.** Established only within a declared model class (Section
  3.3); the class is part of the statement.
- **Influence data, influence hierarchy.** The response, noise, and higher
  multi-time correlations through which an environment acts on the
  retained system (Section 6).
- **Inventory (I1–I11).** The explicitly supplied inputs (Section 21).
- **Irreducible (fork verdict).** Within the tested battery, no earned
  structure selects the input. This is not the formal "irreducible
  primitive" status of Section 24, which needs a declared certificate.
- **Labeled diagnostic.** A post-hoc measurement, labeled as such, recorded
  beside a failed gate; it never repairs the gate.
- **LocPos.** A candidate criterion: every edge weight and pin is
  non-negative (Section 9.4).
- **Matched control.** A replay of the same data under a relabeling, or a
  recomputation of a prior result, used to show the instrument reads zero
  where it should.
- **Min-dominance.** At low frequency the lowest exponent among channels
  dominates (Section 7).
- **NULL-REDUNDANT; NULL-AS-NEW-PRINCIPLE.** A candidate principle that
  reduced to standard structure or to an existing identity (Section 1).
- **Occupancy evidence.** Evidence that an exponent class is inhabited by
  at least one consistently coupled microscopic sector (Section 17.3).
- **Owner ruling.** The author's adjudication of how a result is admitted
  (Section 1).
- **Packaging.** Representing a two-time kernel by a single stationary
  spectral measure or a single function of $t-s$ (Section 5.2).
- **Prediction.** In this record, an empirical prediction about nature.
  Agreements between in-house analytic and numerical computations are
  called checks.
- **Probe.** The gravitational test field $h_{ij}$, modelled as a strain, a
  clock field, or a massless spin-2 field (Section 12); elsewhere a probe
  qubit used to read out coherence.
- **Realization dimension.** The minimal number of hidden modes that
  reproduces a kernel (its Hankel rank).
- **Red.** A failed pre-registered gate; permanent (Appendix C).
- **Retained sector.** The degrees of freedom kept after eliminating the
  environment; on the gravity side, the matter sector coupled to the probe.
- **RRP.** The Reality Requirements Program, a separate line on the
  `master` branch (Section 28).
- **S-level, S-local.** Using only data of the retained system S (Section
  5.1); observables of S alone (Section 8.4).
- **Seam.** A place where the theory's objects are not yet defined: S1
  (stationarity), S2 (causal structure).
- **Section.** An earned map that would supply an inventory coordinate from
  the core datum (Section 20).
- **Sel-4, Sel-4t, Sel-4U, Sel-4x.** A constant probe acts on each sector as
  a pure change of units (the operational weak equivalence principle); its
  temporal part, universality part, and length part (Sections 12, 14, 10).
- **Stem.** A group of inventory inputs: A (access, I1–I2) and B (probe,
  I3–I6).
- **T3 anchor.** The standard-QFT de Sitter graviton self-energy
  calculation used by C7 (Section 24.1).
- **TT.** Transverse-traceless: the physical polarizations of a graviton.
- **Universal reach.** All sectors lie in one exchange-coupled component
  (I4).
- **$z$.** The dynamical exponent, $\omega\propto k^z$; $z=1$ is linear
  (sound-like) dispersion.

# Appendix I — Notation and symbols with more than one meaning

| Symbol | Meaning in this record | Other meanings in the program's files |
|-----------|------------------------|--------------------------|
| $k(\tau)$, $k(t,s)$ | Memory kernel of Sections 4–5, decay-rate form, $\lambda_l>0$ | Written $K_R(t)=\sum(v_{1k})^2e^{\lambda_kt}$, $\operatorname{Re}\lambda_k<0$, in earlier documents |
| $K(t)$, $N(t)$ | Feynman–Vernon dissipation and noise kernels (Section 6) | $N$ is also a system size, and a realization dimension in the foundations files |
| $\mathbf K$, $K_{SS}$, $\mathbf K_{yy}$, $K_{AI}$ | Stiffness matrix and its blocks | — |
| $K_0(t)$ | Local kernel of a conservative lattice (Section 4.2) | — |
| $J(\omega)$, $\nu(\omega)$ | Dissipation and noise spectra; matrix-valued in Section 6.3 | $J_0$ is a Bessel function (Section 4.2); $J$ is a drive or a symplectic matrix in some instruments |
| $\rho(\theta)$, $\mu(\omega)$ | Spectral measure (class (a)); local density of states (class (b)) | — |
| $\varrho$ | A state (Section 20) | The formalizations write it $\rho$ |
| $s$ | Symmetric occupation (Section 6.1) | Low-frequency exponent, $J\propto\omega^s$ (Section 7) |
| $\xi$ | Improvement coefficient (Sections 12, 18) | SX-1 writes the correlation length as $\xi^2=k/p$; this record writes $\ell_c$ |
| $H$ | Hamiltonian | $H_0$: present Hubble rate (Section 5); $H$: de Sitter Hubble rate (Section 24.1); H3: an S-1 hypothesis label |
| $R$ | Residual fraction (Section 5) | $R(0,r)$: effective resistance (Sections 15–16); R1–R7: relations (Section 20); $R$: charge range (Section 14) |
| $\kappa$ | Gravitational coupling, $\sim1/M_{\rm Pl}$ | $\kappa_4$: fourth cumulant (Section 6.3) |
| $C$ | Mixing matrix $V_{\rm new}^{\mathsf T}V_{\rm old}$ (Section 5) | $C_{ab}(\omega)$: bath correlation spectrum; C_cons; C1–C7; $\mathcal C$: continuum object |
| P-1 … P-6 | Forks (Sections 6–8) | C1-a2's charter gates (renamed A2-1 … A2-6 here); the foundations checks P1–P7 |
| S-1; S1, S2 | A fork; the two seams | S-level, S-local (Glossary) |
| D-1 | A fork (Section 8.4) | Owner direction D-1, deferring external review (Section 29.4) |
| T3 | The de Sitter anchor | A target label in the P-2 instrument |

**Units and conventions.**
- $\hbar=k_B=1$ in the P-2, P-3, CA-1, and GR-1 instruments; Section 6.1
  restores ℏ by declaration.
- CA-1's classical noise, $\nu=(2T/\omega)J$, is twice the high-temperature
  limit of P-2's thermal curve; this affects only CA-1's finite-temperature
  statements, not the $T=0$ value quoted in Section 15.
- Exponent conventions are never mixed: the v3 propagator convention
  ($\omega^7$, $t^{-8}$), the sealed ledger's task-literal convention
  ($\omega^8$), GR-1's own convention (base ≈ 4), and the T3 self-energy
  convention ($\omega^4$ flat limit) are compared only through increments
  or through an explicit convention map.

---

# References

Citation keys without a dagger are held in the program's own source
register. The register records a verification tier for each entry: most
here were checked at metadata or abstract level (via Crossref, arXiv, or
the publisher) on 23 September 2026, and some are noted as known only
through secondary literature. **References marked † are supplied for this
edition. Their bibliographic data have not been verified against the
program's source register.** No systematic literature search has been
performed for this record.

**In the program's source register**

- [CL83] A. O. Caldeira and A. J. Leggett, "Path integral approach to
  quantum Brownian motion", *Physica A* **121**, 587 (1983).
- [CW51] H. B. Callen and T. A. Welton, *Phys. Rev.* **83**, 34 (1951).
- [DESI25] DESI Collaboration, DR2 cosmological constraints (2025),
  arXiv:2503.14738.
- [FV63] R. P. Feynman and F. L. Vernon, *Ann. Phys.* **24**, 118 (1963).
- [HV08] B. L. Hu and E. Verdaguer, "Stochastic gravity: theory and
  applications", *Living Rev. Relativity* **11**, 3 (2008).
- [Jac95] T. Jacobson, "Thermodynamics of spacetime", *Phys. Rev. Lett.*
  **75**, 1260 (1995).
- [Kub66] R. Kubo, "The fluctuation-dissipation theorem", *Rep. Prog. Phys.*
  **29**, 255 (1966).
- [Leg87] A. J. Leggett *et al.*, *Rev. Mod. Phys.* **59**, 1 (1987).
- [Mor65] H. Mori, "Transport, collective motion, and Brownian motion",
  *Prog. Theor. Phys.* **33**, 423 (1965).
- [Nak58] S. Nakajima, *Prog. Theor. Phys.* **20**, 948 (1958).
- [PW78] W. Pusz and S. L. Woronowicz, *Commun. Math. Phys.* **58**, 273
  (1978).
- [Sak67] A. D. Sakharov, "Vacuum quantum fluctuations in curved space and
  the theory of gravitation", *Dokl. Akad. Nauk SSSR* **177**, 70 (1967)
  [*Sov. Phys. Dokl.* **12**, 1040 (1968)]. (Register note: known through
  secondary literature.)
- [TTW21] L. Tan, N. C. Tsamis, and R. P. Woodard, "Graviton self-energy from
  gravitons in cosmology", *Class. Quantum Grav.* **38**, 145024 (2021);
  arXiv:2103.08547.
- [TW96] N. C. Tsamis and R. P. Woodard, "One loop graviton self-energy in a
  locally de Sitter background", *Phys. Rev. D* **54**, 2621 (1996);
  hep-ph/9602317.
- [Vik05] A. Vikman, "Can dark energy evolve to the phantom?", *Phys. Rev. D*
  **71**, 023515 (2005); astro-ph/0407107.
- [WW80] S. Weinberg and E. Witten, "Limits on massless particles", *Phys.
  Lett. B* **96**, 59 (1980).
- [Zwa60] R. Zwanzig, *J. Chem. Phys.* **33**, 1338 (1960).

**Supplied for this edition (†)**

- [†Ber29] S. Bernstein, "Sur les fonctions absolument monotones", *Acta
  Math.* **52**, 1 (1929).
- [†FKM65] G. W. Ford, M. Kac, and P. Mazur, "Statistical mechanics of
  assemblies of coupled oscillators", *J. Math. Phys.* **6**, 504 (1965).
- [†Gol61] J. Goldstone, "Field theories with 'superconductor' solutions",
  *Nuovo Cimento* **19**, 154 (1961).
- [†Gup54] S. N. Gupta, "Gravitation and electromagnetism", *Phys. Rev.*
  **96**, 1683 (1954).
- [†HHK72] R. Haydock, V. Heine, and M. J. Kelly, "Electronic structure based
  on the local atomic environment for tight-binding bands", *J. Phys. C*
  **5**, 2845 (1972).
- [†Kac66] M. Kac, "Can one hear the shape of a drum?", *Amer. Math.
  Monthly* **73**(4), 1 (1966).
- [†KR93] D. J. Klein and M. Randić, "Resistance distance", *J. Math. Chem.*
  **12**, 81 (1993).
- [†Lan50] C. Lanczos, "An iteration method for the solution of the
  eigenvalue problem of linear differential and integral operators",
  *J. Res. Natl. Bur. Stand.* **45**, 255 (1950).
- [†SW64] R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and
  All That* (W. A. Benjamin, New York, 1964).
- [†Wei64] S. Weinberg, "Photons and gravitons in S-matrix theory:
  derivation of charge conservation and equality of gravitational and
  inertial mass", *Phys. Rev.* **135**, B1049 (1964).
- [†Wei65] S. Weinberg, "Infrared photons and gravitons", *Phys. Rev.*
  **140**, B516 (1965).
- [†Wid41] D. V. Widder, *The Laplace Transform* (Princeton University Press,
  1941).

---

## External review and validation status

**No external peer review is claimed. No experimental validation is
claimed. No outside human reviewer has checked any GRUT-specific result.**
External review has been deliberately deferred by owner direction
(Section 29.4). This record reports an in-house research program, and its
computational and formal artifacts, at the stated source boundary.

## Publication integrity statement

This document is intentionally conservative. It states what the GRUT
program has constructed, constrained, supplied, or left open at the stated
source boundary. It is not independent experimental validation, a proof of
a unique microscopic ontology, or a completed theory of everything. The
strongest claims are those whose scope is stated immediately beside them.

If a future result changes a status, the change enters through a new dated
source boundary and a new consolidated record. This snapshot is never
silently rewritten.

# End of consolidated theory record
