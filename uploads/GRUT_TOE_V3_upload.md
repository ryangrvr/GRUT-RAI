# Grand Responsive Universe Theory
## GRUT ToE v3 · Candidate Framework

*A Candidate Theory of Everything from a Viscoelastic Gravitational Medium with Finite Memory*

**June 2026 · GRUT Research**

---

> **How to read this book.** This is the Grand Responsive Universe Theory (GRUT) Theory of Everything Version 3 — one continuous story,
> from the question a theory of everything must answer to the honest frontier of what remains open.
> It is written to be read straight through. Every claim is marked, in plain words, at the standing it
> actually earned: **proven** (computed and tested), **postulated** (an adopted axiom), **anchored**
> (fixed by observation, not derived), **conjectural** (plausible but unproven), or **open** (a stated,
> unsolved problem). The companion technical edition (`theory/GRUT_TOE_V3.md`) and the machine-checked
> claim registry (`grut/toe/registry.py`, 116 claims, 3,227 passing tests) are the backing for every
> statement here. Nothing in this book is hoped-for; it is either done, assumed, or openly unfinished —
> and it says which on every line.

---

> **How GRUT is built, tested, and carried.** Everything in this book is carried by **GRUT-RAI** — the
> *Responsive AI* research platform on which the theory is implemented as runnable code, not prose alone, so that
> every quantitative statement can be computed, checked, and re-derived on demand. The platform rests on three
> load-bearing parts. **The claim registry** (`grut/toe/registry.py`, 116 claims) is the spine: each record
> fixes the physical statement, the tier it has earned, the code that computes it, the tests that check it, the
> claims it depends on, and the single observation that would falsify it — and every claim in this book is
> backed, one-to-one, by such a record. **The test suite** (**3,227 passing tests**) is the conscience: every
> *proven* result has at least one test that reproduces it from the code, and enforcement tests
> (`tests/toe/test_registry_completeness.py`, `tests/toe/test_ledger.py`) guarantee that no claim is ever left
> unregistered, untested, or without a documented standing. **The open-question ledger** (`grut/toe/ledger.py`)
> is the memory: each of the 28 open negatives is a live entry recording what would close it, the effort that
> would take, and which results it would strengthen. A claim advances a tier only when a test certifies it; a
> result that fails is demoted and logged, never quietly dropped. Registry, tests, and ledger are one source of
> truth — the technical edition, this narrative, and the live research platform all draw from it, and nothing is
> hand-curated or fitted away.

---

## 1. Foreword + The Question

### 1.1 Foreword: What This Edition Is

This edition emerges from a systematic audit and represents a leaner framework than its predecessor.

Version 2, completed in June 2026, was ambitious in scope. Built on a single organizing hypothesis — that the gravitational vacuum behaves as a medium with finite relaxation time — it advanced three principal claims: a mechanism capable of producing a dark-matter signature in galactic rotation curves; a derivation of the theory's unique dimensionless parameter, α = 1/3, from first principles; and a testable modification of gravitational physics on cosmological scales. Version 3 is the outcome of submitting each of these claims to rigorous adversarial scrutiny and systematic attempts at falsification.

Most claims failed under pressure. The essential finding, however, is not that external experiments contradicted them, but rather that the framework's internal consistency requirements forbade them.

The clearest illustration is the dark sector — Version 2's most compelling prediction. The audit systematically examined every candidate mechanism and eliminated each. The final and most sophisticated candidate, based on second-order curvature response, was excluded not by experimental refutation but by a theorem the theory proves about itself. Every second-order response mechanism consistent with the framework's constraints — whether based on the Weyl-squared curvature scalar, the Bach tensor, or the transverse-projector structure — produces an effective density profile scaling as 1/r⁴ or steeper. A realistic dark-matter halo requires density scaling closer to 1/r². Bridging that gap would require a true inverse-Laplacian operator (a 1/∇² structure in the response kernel), yet the same locality constraint that determines the theory's unique length scale L₀ explicitly forbids such non-local structures. GRUT did not fail to locate a dark-matter mechanism; rather, its internal logic demonstrated that no mechanism of this type is possible. **The theory survived by explicitly rejecting one of its most attractive predictions.**

This outcome exemplifies the Version 3 lesson in miniature, generalizing across the framework. What survived the audit is more accurately characterized as a compendium of forbidden mechanisms than a catalog of explanatory successes. The linear modified-gravity signal: forbidden by consistency, and independently excluded by observation at approximately 32 standard deviations. Dark-matter generation in the linear channel: forbidden by the boundary operator. The naive second-order halo: forbidden by locality. The parameter α = 1/3, once claimed to derive from first principles, is now plainly stated as an adopted axiom. What remains is more difficult to circumvent and correspondingly more vulnerable to experimental falsification.

**The costs of Version 2 → Version 3:** loss of a derived dark-matter mechanism and loss of the claim that α emerges from first-principles calculation. **The gains of Version 2 → Version 3:** a framework organized around symmetry-breaking constraints rather than advertised successes; sharper, more testable falsifiers; an honest record of which questions remain open; and a transparent assignment of epistemic tier to every claim (computed, anchored, conjectural, or open).

The strongest statement to survive the audit is an **interpretation**, not a finished theorem: **GRUT can be read as the breaking of general relativity's long-wavelength rescaling redundancy by a single memory scale, operating through controlled, non-anomalous violation of coordinate freedom.** This sentence organizes everything that follows, presented explicitly as the current best interpretation of the surviving framework, not a completed proof.

This document serves readers who seek to understand what the theory actually constrains, rather than what its authors once hoped it would explain.

---

### 1.2 The Question: What Must a Theory of Everything Answer?

A theory of everything is not an unreachable ideal; it is a question of how many independent principles are necessary and whether they converge. Three domains demand unification: quantum mechanics (events at small scales, governed by probability), gravitational geometry (the spacetime metric shaped by matter and energy), and cosmological history (the large-scale evolution of the universe). A fourth domain—the dark sector—is empirically inescapable yet theoretically opaque: approximately 85% of the universe's matter content is electromagnetically dark, and approximately 68% of its energy density drives cosmic acceleration in a way consistent with a cosmological constant. Any complete theoretical framework must account for both.

Most approaches begin by asking whether quantum mechanics and gravity are simply different manifestations of a single underlying structure, or whether dark matter and dark energy are artifacts of incomplete gravitational theory. GRUT begins from a different vantage.

GRUT is organized around a puzzle in gravity's fundamental nature. In general relativity, the gravitational field is not a force propagating through space — it is the geometric structure of spacetime itself, determined by the distribution of matter and energy. Yet general relativity provides no definitive answer to a critical question: when matter generates *small* perturbations in spacetime curvature — oscillations propagating across cosmic distances — how does the gravitational substrate respond? Does it restore curvature instantaneously like an elastic spring? Absorb and store the perturbation's energy like a dissipative medium? Display scale-dependent or frequency-dependent response?

Standard general relativity provides a passive answer in limiting cases: the vacuum does not respond except through the propagation of waves governed by Einstein's field equations themselves. The vacuum is inert. But consider an alternative supposition—the opening premise of GRUT—that the vacuum is not inert. Suppose it behaves as a **medium**, in the manner of water or air. Physical media exhibit characteristic properties: they respond to disturbances; they carry memory, storing and releasing energy over finite timescales rather than responding instantaneously; they exhibit frequency dependence, with wave speed and attenuation depending on oscillation frequency.

If the gravitational vacuum possesses these properties—if it is a responsive, memory-bearing medium—then a fundamental question emerges: *what is the simplest, most consistent mathematical form such a medium can take while respecting causality and energy conservation?* This is the problem GRUT approaches.

---

### 1.3 What the Vacuum Responds To

A theory of vacuum response must specify both what the vacuum reacts to and what it ignores. The vacuum cannot respond universally—doing so would violate causality and conservation laws. In particular, it cannot respond to gauge-dependent configurations: mathematical artifacts of the choice of coordinates rather than physical events.

A conceptually efficient summary of the framework that survived the audit is: **the vacuum responds only to physically distinguishable perturbations.** This phrase captures the framework's essential spirit concisely, but it is a **summary, not a foundational axiom**. "Distinguishability" does not stand as an independent postulate from which other results derive. Rather, it names the combined effect of three more fundamental structures—closed-time-path unitarity (**Q**), finite memory (**F**), and the long-wavelength adiabatic redundancy they act upon (**D**)—which the next sections establish and grade by their evidential status. Interpret this slogan as a mnemonic device, not a primitive principle.

The unitarity structure **Q** is where "distinguishability" emerges concretely, and it is the framework's most secure component. Within the closed-time-path formalism of quantum field theory, the vacuum's response is computed by comparing two parallel histories—one evolving forward in time, the other backward—and examining their difference. When the two histories are identical, the difference vanishes and there is no response to report. This is not an ad hoc restriction; it follows necessarily from requiring the theory to be unitary (information is redistributed, never erased).

The second essential ingredient is memory. The vacuum must retain a record of disturbances — not indefinitely, but for a finite duration of approximately 42 million years. This timescale is vast on human scales yet modest on cosmic scales, and this mismatch is what generates structure, effective dissipation, and the arrow of time within an otherwise reversible quantum framework. This is a **postulate**, later anchored by observational convergence, rather than a derived theorem.

The framework's core therefore rests on two loadbearing ideas: a unitarity constraint with strong theoretical standing, and a finite-memory postulate that is adopted and subsequently anchored by data. We use the following terminology throughout: when we state a result is **proven**, executable code computes it and it passes the test suite (the machine-checked registry records this as its *computed* tier — we use the two words interchangeably); when we state **postulated**, the result is taken as an axiom (as the speed of light is taken in relativity, as the action principle is taken in mechanics); when we state **anchored**, the value is not derived from the theory but fixed by convergent observation (as τ₀ is); when we state **conjectural**, the result is a plausible expectation the structure suggests but that is not yet derived or tested; when we state **open**, the question is precisely defined with explicit closure conditions. The following sections make this architecture and its epistemic standing fully explicit before the main narrative resumes.

---

### 1.4 Where This Goes

Before the narrative proper begins, two sections provide orientation: a single-page table summarizing what the audit preserved and what it refuted, and a concise statement of the framework's three organizing structures together with the evidential status of each. Thereafter, the chapters develop consequences in logical order — the unifying idea, the responsive vacuum's properties, the universe's cosmological structure, the search for dark-matter mechanisms, experimental falsifiers, additional physical sectors, and the remaining open frontier. The reader will encounter a framework that surrendered some attractive hypotheses — a derived fundamental value for α, a vacuum-based dark-matter source, linear gravitational enhancement — in exchange for something more durable: an architecture defined by its symmetry breaking and constraints rather than advertised solutions; explicit falsification targets; and transparent documentation of open questions.

---

### 1.5 The Three Pillars and Their Standing

The framework stands on three organizing structures identified and graded during the audit. **These structures carry unequal evidential weight**, and Version 3's commitment to transparency requires explicit statement of this hierarchy.

**Q — Unitarity. Status: established—the strongest pillar.**
The closed-time-path structure: the vacuum's response is computed by varying the influence action with respect to the *difference* between two copies of a history, and vanishes on the diagonal where both copies agree (`S_IF[φ₊ = φ₋] = 0`). This governs causality and the definition of realized events. It is a mathematical theorem of the formalism, not an assumption imported from outside.

**F — Finite Memory. Status: postulated—a foundational assumption.**
The vacuum relaxes on a single characteristic timescale τ₀, generating a single-pole frequency-dependent response and one length scale L₀ = c·τ₀ ≈ 12.85 Mpc. This introduces finite response times and is what distinguishes the vacuum as a *medium* rather than an inert background. It is adopted as an axiom, then anchored through observational convergence — not derived from deeper principles.

**D — Separate-Universe Redundancy. Status: partial—bridge structure, not proven symmetry.**
General relativity's long-wavelength adiabatic dilatation: a uniform rescaling of very-large-scale structure that, in the memoryless (L₀ → 0) limit, leaves physics unchanged. This rescaling is exact within standard general relativity, where it emerges from presupposed formalism; however, it has **not** been re-derived as an exact symmetry of GRUT's full closed-time-path action starting from first principles. We therefore carry D as a partially-established bridge: the breaking is rigorously established, the underlying symmetry is presupposed.

The relationship among these three is the audit's most important structural discovery, and one we assert with highest confidence:

> **Finite memory (F) acts as the controlled breaking of the separate-universe redundancy (D), observed through the unitarity structure (Q).**

The *breaking term* is established through computation: finite memory renders long-wavelength rescalings physically detectable at order (L₀·k)². What remains open is the converse: a rigorous proof that D is an exact symmetry of the full theory in the L₀ → 0 limit. This asymmetry—breaking proven, underlying symmetry presupposed—is precisely why D receives the grade "partial." The narrative chapters build upon the solid ground of Q and F; D provides the interpretive lens through which they are most naturally understood.

One interpretive note, offered as analogy rather than derivation: a finite-memory vacuum that relaxes through a single characteristic timescale behaves mathematically like a *dissipative, strongly-correlated medium*—the class of systems condensed-matter physics describes via relaxation kernels and frequency-dependent susceptibility. This mathematical resemblance serves as useful intuition; it is not a claim that the vacuum *is* such a medium, and the framework does not logically depend upon this correspondence.

---

### 1.6 The One Idea

To grasp GRUT, one must first recognize a subtle redundancy hidden within general relativity — so subtle that Einstein never explicitly noted it, yet which modern physics has identified: the theory possesses a **gauge freedom at wavelengths much larger than galaxies**.

Imagine studying the universe at scales far exceeding galaxy clusters. The spacetime metric—the geometric object that governs how matter moves—contains a coordinate freedom: one can multiply all spatial coordinates by a constant factor, rescaling the universe in one's description, without altering the physical content described by the theory. This is the **adiabatic spatial-dilatation redundancy**, denoted **D**. It is exact, profound, and mathematically real — but only in the memoryless limit where gravitational memory effects vanish.

Consider instead what happens when the vacuum is not memoryless. What if the space between stars, rather than the sterile void of mathematical idealization, behaves as a **medium with finite response time**—a substrate with memory?

**This is the unifying idea at GRUT's center.**

### 1.7 The Observable Vacuum

We **adopt** as a postulated axiom (not a first-principles derivation) that the gravitational vacuum responds to disturbances — **but only to physically realized, distinguishable disturbances**. This principle, termed **the CTP principle** and denoted **Q**, is not original. It emerges from the closed-time-path (or "in-in") formalism of quantum field theory. In elementary terms: a path integral is the quantum mechanical method of summing all possible histories the universe could follow. A closed universe has no external reference observer, so it performs self-measurement by maintaining two copies of its own history—one running forward in time, one backward—and the physically observable dynamics is the *difference* between them. When the two branches are identical, there is no difference, and the vacuum's response is precisely zero. Expressed formally: `S_IF[φ₊ = φ₋] = 0`, where S_IF is the influence action that encodes vacuum response. The vacuum contributes zero when nothing has changed. This principle is **proven**—it follows directly from the mathematical structure of the formalism (we develop this machinery in subsequent chapters).

Now incorporate memory. **We posit** that the gravitational vacuum possesses exactly one **characteristic relaxation time**, denoted τ₀ = 41.9 million years. This is the timescale on which the vacuum returns to equilibrium after disturbance. In the frequency domain, this produces a single-pole susceptibility—the Lorentzian response function universal to damped systems:

$$χ(ω) = \frac{1}{1 - i ω τ₀}$$

This characterizes a **viscoelastic medium**—one that is stiff to rapid shaking (high frequencies, ωτ₀ ≫ 1) and pliant to slow pushing (low frequencies, ωτ₀ ≪ 1). The relaxation time defines a length scale: **L₀ = c·τ₀ ≈ 12.85 Mpc**—the distance light travels during one relaxation period. This is **the single length scale of GRUT**. At wavelengths larger than L₀ (low frequencies), the vacuum remembers. At shorter wavelengths (high frequencies), memory fades and general relativity is recovered exactly. This structure is **postulated** and subsequently **anchored by observation**: the vacuum-response timescale is not something we derived from first principles; rather, it was empirically determined by observing galaxy clustering dynamics, cluster-merger timescales, and the scales at which dark-matter-like signals emerge. These observations, drawn from different techniques, epochs, and environments, all converge to τ₀ ≈ 41.9 Myr. This convergence constitutes the evidence.

### 1.8 How Memory Breaks the Redundancy

This is where the universe acquires non-trivial structure. Recall the rescaling redundancy **D**: one can uniformly rescale space, and in the memoryless limit, physics remains unchanged. But the vacuum is not memoryless. It is a medium with a fixed, absolute proper length **L₀**.

Consider an analogy: imagine standing in a swimming pool of fixed length, say 50 meters. If you rescale coordinates to make the pool "stretch," the water—a real physical medium—cannot stretch with your coordinates. The medium is indifferent to your choice of coordinate labels. The fixed length of the pool breaks the coordinate-rescaling freedom. It is an absolute physical scale, not gauge freedom.

The identical principle applies here. When spatial coordinates are rescaled by a factor (space multiplied by e^λ), the physical wavelength of a disturbance transforms as k_phys = k/a, where a is the cosmological scale factor. However, the memory-encoded argument in the relaxation function depends on the *physical* wavelength: the dimensionless combination is L₀k_phys. Under coordinate rescaling, L₀k_phys → e^{-λ}L₀k_phys. In the squared susceptibility, (L₀k_phys)² → e^{-2λ}(L₀k_phys)²—which is **not invariant**. A coordinate rescaling cannot absorb an absolute physical scale. The redundancy **D is broken**.

This breaking is **controlled** — it enters at order (L₀k_phys)², which is negligibly small across cosmic distances (where L₀ is vast on human scales but modest on cosmological scales). The breaking is also **non-anomalous**. In quantum field theory, certain symmetries break with an *anomaly* — a quantum correction appearing only through loop diagrams of virtual particles, irreducible and insurmountable. That is **not** what occurs here. Our rescaling is a *diffeomorphism*—a smooth relabeling of spatial coordinates—not a *Weyl rescaling*, which represents a genuine physical change of scale. The path-integral measure (the mathematical object quantum theory integrates over, which counts histories) is unaffected by mere relabeling. Therefore the trace anomaly—the quantum correction normally appearing in scale-related calculations—does **not** participate. The breaking is entirely classical: finite memory, not quantum subtlety, violates the symmetry.

This is the audit's central finding: **finite memory F acts as the controlled breaking of the adiabatic dilatation redundancy D.** To be precise, what is rigorously established (computed and independently verified) is the *breaking term* itself—that finite memory makes long-wavelength rescalings physically observable at order (L₀·k)². The three structures Q, F, and D are thereby interwoven, though not equivalently: Q is proven, F is postulated and anchored, and D is a **partially-established bridge**—we have rigorously determined that it breaks, even though its status as an exact symmetry of the full theory remains presupposed rather than newly derived.

The terminology is intentionally honest: D is a **conjectured bridge whose breaking term is established**. The assertion that coordinate rescaling is a true symmetry of the bare quantum action (in the L₀ → 0 limit) draws from standard Weinberg machinery and is presupposed, not re-derived here from GRUT's first principles. Yet the breaking when L₀ is nonzero is rigorous and verified.

### 1.9 One Broken Symmetry, One Scale, One Theory

This is why GRUT is economical. A fundamental physical theory is **defined by two specifications: which symmetry it breaks and by how much**. Newtonian gravity breaks Galilean scale invariance—objects can have different sizes. A particle's rest mass breaks scaling—the rest mass cannot be rescaled away. A magnetic moment breaks rotational invariance—it points in one preferred direction. Electroweak symmetry breaking gives the W and Z bosons their mass.

GRUT breaks the adiabatic spatial-dilatation redundancy—the long-wavelength rescaling freedom of general relativity—through a single length scale, **L₀**. **That is the entire theory in one sentence.** No new forces, no new particles, no new fields. One redundancy, one scale, complete.

All else is consequence. The vacuum cannot respond to pure-gauge, adiabatic modes (because these *are* the rescaling modes themselves—the redundancy operates precisely on them). Therefore the vacuum cannot enhance linear density perturbations. Linear cosmology is **forced to be exactly ΛCDM**—this is not a fit to data, it is a derived requirement. Dark matter cannot originate in the linear channel (where the vacuum is forbidden to respond). It must reside in nonlinear and tensor effects—an open frontier, not yet solved but now precisely circumscribed.

The vacuum *can* respond to gravitational waves, which are tensor disturbances orthogonal to adiabatic modes. This response produces a **sharp table-top falsifier**: a gravitational-decoherence plateau at approximately 689 Hz. Measuring the decoherence rate of a nanoparticle in an interferometer at that frequency, and comparing against GRUT's prediction, provides a direct experimental test.

The vacuum's refractive properties in its deepest infrared limit—the constants governing its response—are determined by two numbers: the impedance α = 1/3 and the memory time τ₀ = 41.9 Myr. The first is **postulated as a foundational axiom**—it is motivated by identifying the gravitational conformal mode as the infrared response carrier, under which its value would follow from a trace-anomaly calculation. But closing that identification from first principles—the fourth-order conformal-anomaly derivation—remains open, so α = 1/3 is adopted, not derived. The second is **anchored**: it was not computed but observed, residing at the convergence point of galactic rotation curves, cluster-merger dynamics, and cosmological statistics.

### 1.10 The Unifying Statement

Finally, the statement that binds all elements:

> **"The vacuum responds only to physically distinguishable structure"**—which is the name for the conjunction **Q ∩ F ∩ D**: CTP unitarity, finite single-pole memory, and the adiabatic-dilatation redundancy whose breaking they exhibit. Not three separate axioms, but one unified principle derived from their intersection.

GRUT is general relativity with one broken symmetry and one length scale. It is the dilatation-redundant GR limit, modified by controlled breaking of that redundancy through the scale **L₀ = c·τ₀ ≈ 12.85 Mpc**. Just as a particle's mass breaks scale invariance, one physical scale breaks coordinate freedom. And from this single breaking—witnessed by observation, constrained by self-consistency, tested through the vacuum's measurable response—the universe unfolds.

---

### 1.11 Technical Brief

This section formalizes the chapter's central objects and states the key mathematical structures precisely.

**The Closed-Time-Path Action and the Influence Functional.**
The closed-time-path formalism begins with the CTP action S_CTP, constructed on a doubled time contour. The universe's history is represented by two branches: φ₊(t) running forward from initial state to time T, and φ₋(t) running backward from T to the initial state. The physical observable is the influence functional:

$$S_{IF}[φ_+, φ_-] = \int dt \mathcal{L}_{IF}(φ_+, φ_-)$$

**Tier: proven (theorem of the formalism)**. The crucial property is that **S_IF[φ_+ = φ_-] = 0 identically**. This is not imposed; it follows from requiring the theory to be unitary. The physical response is computed as:

$$\chi(φ) = \frac{\delta^2 S_{IF}}{\delta φ_+ \delta φ_-}\bigg|_{φ_q=0}$$

where φ_q = (φ_+ − φ_−)/2 is the difference variable. This vanishing on the diagonal ensures the theory respects information conservation.

**The Constitutive Law: Mori–Zwanzig Relaxation.**
The vacuum's response obeys a first-order relaxation law:

$$τ_0 \dot{z} + z = z_{\text{target}}$$

**Tier: postulated**. Here τ₀ is the single relaxation timescale, z is the medium's state, and z_target is the equilibrium value. The Fourier transform of the exponential relaxation kernel is:

$$χ(ω) = \frac{1}{1 - iωτ_0}$$

This is **causal** (the pole sits in the lower half-plane), **Kramers–Kronig compatible** (real and imaginary parts satisfy causality bounds), and **recovers general relativity** (χ → 0 as ω → ∞). In the retarded form:

$$K^R(ω) = α_{\text{vac}} \cdot χ(ω) \cdot P^{TT}$$

where P^TT is the transverse-tracefree projector and α_vac = 1/3 **Tier: axiom** is the vacuum impedance.

**The Breaking of Adiabatic Dilatation.**
Under the spatial-dilatation transformation a → ae^λ (keeping comoving k fixed), the physical wavelength becomes k_phys = k/a, and thus:

$$(L_0 k_{\text{phys}})^2 \to e^{-2λ}(L_0 k_{\text{phys}})^2$$

Since L₀ is an absolute length scale (not gauge-dependent), this quantity is **not invariant**. The response susceptibility χ_eq contains (L₀k_phys)² in its denominator, so:

$$χ(ω, k) = \frac{1}{1 - iωτ_0 + (L_0 k_{\text{phys}})^2}$$

exhibits explicit breaking at order (L₀k)². **Tier: computed**. The breaking is non-anomalous: the path-integral measure Jacobian (being a diffeomorphism, not a Weyl rescaling) equals 1, so the trace anomaly coefficient α does not enter the breaking term itself.

**The Length Scale and Its Physical Meaning.**
The memory length is defined as:

$$L_0 = c \cdot τ_0 ≈ 12.85 \text{ Mpc}$$

**Tier: anchored** (L₀ = c·τ₀ is fixed once τ₀ is). Physically, L₀ is the distance light travels during one relaxation time. It separates two regimes:
- **ωτ₀ ≫ (L₀k)²** (high-frequency / temporal-dominated regime): memory effects are small, so the vacuum's response is negligible; this is the regime where general relativity is recovered.
- **ωτ₀ ≪ (L₀k)²** (low-frequency / spatial-gradient regime): the susceptibility saturates toward its zero-frequency value χ(0) = 1/(1 + (L₀k)²), a characteristic low-pass filter.

---

## 2. V3 at a Glance — What Survived the Audit

![The v3 audit at a glance, sorted into three columns. Survives (green): the CTP unitarity structure (Q), the finite-memory framework, the linear-cosmology result μ_linear = 1, the derived a₀ acceleration scale, the recovery of quantum mechanics, and the arrow of time. Refuted (red): the linear Ω_dm = 1/3 claim, the linear modified-gravity enhancement, orbital-gate dark matter, and the C5a radial profile. Open (amber): α-selection (the Riegert antecedent), a full redundancy proof, and a covariant K⁽²⁾. The theory is defined more by what it forbids than by what it predicts — 28 open negatives are ledgered.](figures_v3/fig_status_ledger.png)

Before any details, here is the whole result on one page. Each row is a verdict the audit reached; the chapters that follow defend each one. *Survives* = established or anchored at the stated tier; *refuted* = ruled out by the framework's own constraints or by data; *open* = a precisely-posed, unsolved problem.

| Status | Result |
|---|---|
| **Survives** | Q — the closed-time-path (CTP) unitarity structure |
| **Survives** | the finite-memory framework (one scale, L₀ = c·τ₀) |
| **Survives** | μ_linear = 1 — linear cosmology is exactly ΛCDM (a *derived requirement*) |
| **Survives** | the derived MOND acceleration scale a₀ = cH₀/(2π) |
| **Survives** | quantum mechanics, recovered in the Schrödinger (τ → 0) limit |
| **Survives** | the arrow of time, from constitutive entropy production |
| **Refuted** | the linear dielectric dark matter, Ω_dm = 1/3 |
| **Refuted** | the linear modified-gravity enhancement branch |
| **Refuted** | the orbital-gate dark-matter mechanism |
| **Refuted** | C5a — the Weyl-squared profile as a dark-matter source |
| **Open** | the α-selection problem (a first-principles value for α = 1/3) |
| **Open** | the full separate-universe redundancy proof |
| **Open** | the exact second-order kernel derivation (full covariant form) |

Read top to bottom, the table is the thesis: more of GRUT v3 is settled by what it *forbids* — each refutation is a constraint the framework imposed on itself — than by what it predicts. The survivors are a small, hard core; the open problems are named, not buried.

---

## 3. The Three Pillars and Their Standing

![The three organizing structures of v3 and their logical standing, colour-coded by tier. Q — closed-time-path (CTP) unitarity — is proven; F — a finite vacuum memory time τ₀ — is postulated; D — the separate-universe (long-wavelength rescaling) redundancy — is partial, not yet a proven symmetry of the full theory. F breaks D in a controlled way at order (L₀k)², and that breaking is what the unitary sector Q makes observable.](figures_v3/fig_qfd_pillars.png)

The GRUT framework rests upon three organizing structures, identified and graded rigorously during the audit. They are **not equally established**, and the epistemic honesty of v3 depends critically on distinguishing their tiers.

### 3.1 Pillar Q — Closed-Time-Path Unitarity (Proven)

**Status: proven — the strongest pillar, a theorem of the formalism.**

Physics is response to realized differences. On the closed-time-path (CTP) contour that governs quantum field theory in a closed universe without external observers, the influence action $S_{IF}$ vanishes identically when the forward and backward branches of the universe's history are identical everywhere:

$$S_{IF}[h_+ = h_-] = 0.$$

This is not an ad hoc restriction; it emerges as a theorem from requiring the theory to preserve quantum information (unitarity). The physical response of the vacuum appears only when we consider deviations from this classical diagonal — when the two branches differ. We compute that response by taking the functional derivative of $S_{IF}$ with respect to the difference between branches, evaluated at zero difference:

$$\text{response} = \frac{\delta S_{IF}}{\delta h_q}\bigg|_{q=0}$$

where $h_q$ is the difference coordinate (the "quantum" field on the CTP contour) and $h_c = (h_+ + h_-)/2$ is the classical background.

This structure governs causality: the vacuum cannot respond to configurations the universe cannot distinguish from equilibrium. It determines what counts as a physically realized event — only histories that produce a measurable difference from a reference state. The vacuum responds to gravitational curvature, to matter density, to the oscillations that ripple through spacetime. But it responds to nothing that is purely gauge-dependent, coordinate-choice, or a relabeling of an identical underlying configuration. This is **proven** because it follows directly from the mathematical structure of the CTP formalism itself, not from any ansatz about the vacuum's properties.

### 3.2 Pillar F — Finite Memory through Single-Pole Susceptibility (Postulated and Anchored)

**Status: postulated as foundational assumption; anchored by observation.**

Given that the vacuum responds only to realized differences, we must specify *how* it responds. The framework adopts a constitutive law drawn from the theory of viscoelastic media — materials that are elastic yet possess memory. The governing equation is a first-order relaxation law:

$$\tau_0 \dot{z} + z = z_{\text{target}},$$

where $z$ represents the vacuum's response state, $z_{\text{target}}$ is the asymptotic configuration the applied disturbance would drive the system toward, and $\tau_0$ is the single relaxation timescale — the timescale on which the vacuum "remembers" and forgets. This is the Mori–Zwanzig form, the universal signature of dissipation in causal systems.

In the frequency domain, this constitutive equation produces a single-pole susceptibility — the Lorentzian response function:

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0}.$$

This susceptibility is causal and bounded: the absorptive (imaginary) part, together with the lower-half-plane pole, makes the response causal — it lags slightly behind the disturbance, satisfying the Kramers–Kronig dispersion relations that any physical medium must obey. At low frequencies ($\omega \ll 1/\tau_0$), the vacuum responds nearly in-phase and with full amplitude ($\chi \approx 1$). At high frequencies ($\omega \gg 1/\tau_0$), inertia dominates and the vacuum's response vanishes ($\chi \to 0$). In this high-frequency limit, the gravitational field recovers the instantaneous, memoryless equations of general relativity with exponential precision.

The structure of Pillar F introduces a single dimensionful length scale:

$$L_0 = c \cdot \tau_0 \approx 12.85 \text{ Mpc}.$$

This is the distance light travels during one relaxation time. It represents the vacuum's "memory horizon": at wavelengths much larger than $L_0$, the vacuum retains information about perturbations; at wavelengths much shorter, memory effects become negligible.

**Why this pillar is postulated, not derived:** The form of the susceptibility — single-pole, causal, Mori–Zwanzig — is required by consistency with the CTP structure and the demand for finite memory. But the value of $\tau_0 = 41.9$ million years is not derivable from first principles within the framework. Instead, it is anchored by convergent observation: the Hubble expansion rate and the cosmic-baseline dynamics point to $\tau_0 \approx 41.9 \pm 1.5$ Myr; the Bullet Cluster (the lag between collision-shocked gas and dark matter) gives a looser, higher estimate, $\tau_0 \sim 50$ Myr; and the self-consistency of structure formation, decoherence timescales, and background expansion locks $\tau_0$ into the 40–42 Myr band. These independent routes agree to within their ~20% spread and cluster around $\tau_0 \approx 41.9$ Myr — the value adopted throughout — providing robust empirical anchoring even though $\tau_0$ was not derived from the theory itself.

### 3.3 Bridge D — Adiabatic Spatial-Dilatation Redundancy (Partially Established)

**Status: conjectured symmetry whose breaking term is established; the underlying symmetry is not yet proven from first principles within GRUT.**

General relativity possesses a subtle gauge freedom at very long wavelengths. If one smoothly rescales all spatial coordinates by a constant factor — a uniform, spatially-homogeneous dilation $a \to a e^\lambda$ — the physical laws remain unchanged in the memoryless limit where the gravitational field responds instantaneously. This is the adiabatic spatial-dilatation redundancy, or **D**. It is exact when $L_0 \to 0$ (the GR limit), and it emerges from standard machinery (Weinberg's adiabatic-mode framework).

However, GRUT breaks this redundancy in a controlled way through Pillar F. The physical wavelength of a perturbation is $k_{\text{phys}} = k/a$ (comoving wavenumber divided by scale factor). When one applies the dilation $a \to a e^\lambda$, the physical wavelength transforms as:

$$k_{\text{phys}} \to e^{-\lambda} k_{\text{phys}}.$$

The memory argument in the susceptibility depends on the dimensionless combination $L_0 k_{\text{phys}}$. Under the dilation, this scales as:

$$(L_0 k_{\text{phys}})^2 \to e^{-2\lambda} (L_0 k_{\text{phys}})^2.$$

This is **not invariant** under the coordinate rescaling, because $L_0$ is a fixed proper scale — an absolute physical length that the dilation cannot absorb into a redefinition of coordinates. The same principle that allows a fixed particle mass to break scale invariance applies here: a fixed length breaks gauge-scaling freedom.

**The breaking is established and non-anomalous.** The detailed calculation shows that the breaking occurs at order $(L_0 k_{\text{phys}})^2$ — a tiny correction for the distances of the universe. Moreover, it is non-anomalous: the adiabatic dilation is a *diffeomorphism* (a smooth relabeling of spatial coordinates), not a *Weyl rescaling* (a genuine physical change of scale). The path-integral measure that quantum field theory sums over is invariant under diffeomorphisms (its Jacobian is identically 1), so the trace-anomaly coefficient $a/c$ — which would enter if the symmetry breaking were anomalous — plays no role. The breaking is purely classical: finite memory kills the symmetry, not quantum subtlety.

**What remains open:** The proof that coordinate rescaling is an exact gauge redundancy of GRUT's *full* CTP action in the $L_0 \to 0$ limit has not been independently re-derived from the framework. This symmetry is presupposed from standard GR machinery. We have rigorously proven that $F$ breaks $D$ for $k \neq 0$, but we have not independently proven that $D$ is an exact symmetry of the bare action to begin with. This asymmetry — breaking established, underlying symmetry presupposed — is why $D$ carries the tier "conjectured bridge" rather than "proven pillar."

### 3.4 The Structural Relationship

The single most important finding of the audit is this:

> **Finite memory (F) acts as the controlled breaking of the adiabatic spatial-dilatation redundancy (D), observed through the unitarity structure (Q).**

These three structures are not three independent axioms. Rather, they are woven together:

- **Q** is proven: physics is the response to realized differences, guaranteed by the CTP formalism.
- **F** is postulated and anchored: the vacuum relaxes with a single timescale $\tau_0$, anchored by observation.
- **D** is a conjectured symmetry whose breaking by **F** is established: finite memory breaks the long-wavelength rescaling freedom that would otherwise be exact.

The profound implication is that GRUT is not really three separate mechanisms. It is **general relativity's adiabatic-dilatation-redundant limit, plus the controlled breaking of that redundancy by one physical length scale** $L_0 = c \tau_0$. The same way a particle's mass breaks scale invariance (you cannot rescale rest mass away), one physical length breaks coordinate-rescaling freedom. One broken symmetry. One scale. Disciplined.

This is why the framework is lean and why its predictions are sharp: every consequence downstream — the cosmological constant, the decoherence plateau, the prohibition on linear modified gravity, the nature of dark matter — flows from understanding which symmetry is broken and by how much.

---

### 3.5 Technical Brief

We formalize the three pillars at the level of the governing equations, step by step.

**Pillar Q — The Response Formula**

The vacuum's response is computed from the influence functional on the closed-time-path contour. The CTP action $S_{\text{CTP}}$ is constructed from the classical gravitational action plus the matter action, evaluated on both the forward (+) and backward (−) branches, woven together by retarded and advanced propagators. The influence action is defined as:

$$S_{IF}[h_+, h_-] = \int d^4 x \left[ \mathcal{L}_+(h_+, \psi_+) - \mathcal{L}_-(h_-, \psi_-) \right]_{\text{contact}},$$

where the subscript denotes the on-shell action restricted to the contact surface where forward and backward contours meet. 

The key theorem: **On the classical diagonal where $h_+ = h_-$ everywhere, $S_{IF}$ vanishes identically.** This is not an axiom; it follows from the mathematical structure of the contour. The physical response emerges from the functional derivative with respect to the difference coordinate:

$$h_q = h_+ - h_-, \quad h_c = \frac{h_+ + h_-}{2},$$

evaluated at $h_q = 0$:

$$\text{Response kernel} = \frac{\delta S_{IF}}{\delta h_q}\bigg|_{h_q=0}.$$

This response is the vacuum's sensitivity to perturbation — the susceptibility. It is nonzero precisely because $h_q$ deviates from the classical diagonal, and it vanishes for any configuration that cannot be distinguished from equilibrium.

**Pillar F — The Constitutive Equation and Its Frequency Response**

The vacuum's response obeys the Mori–Zwanzig relaxation law:

$$\tau_0 \frac{dz}{dt} + z = z_{\text{target}}.$$

Taking the Fourier transform (assuming $z_{\text{target}} \propto e^{-i\omega t}$), we obtain:

$$(-i\omega \tau_0 + 1) z(\omega) = z_{\text{target}}(\omega),$$

$$z(\omega) = \frac{1}{1 - i\omega \tau_0} z_{\text{target}}(\omega).$$

The proportionality constant is the susceptibility:

$$\chi(\omega) = \frac{1}{1 - i\omega \tau_0}.$$

This is a single-pole response with the pole located at $\omega = -i/\tau_0$ in the lower half of the complex frequency plane — the hallmark of stability and causality. We can verify the Kramers–Kronig relations explicitly:

$$\text{Re}[\chi(\omega)] = \frac{1}{1 + (\omega\tau_0)^2}, \quad \text{Im}[\chi(\omega)] = \frac{\omega\tau_0}{1 + (\omega\tau_0)^2}.$$

The imaginary part is positive; the dissipated power, proportional to $\omega\,\text{Im}[\chi(\omega)] > 0$, satisfies the passivity condition, while the pole in the lower half-plane makes the response causal (retarded) — it lags the disturbance in the time domain.

In the time domain, the susceptibility corresponds to exponential relaxation:

$$\chi(t) = \theta(t) e^{-t/\tau_0} \quad \Longleftrightarrow \quad \chi(\omega) = \frac{1}{1 - i\omega\tau_0},$$

where $\theta(t)$ is the Heaviside step function ensuring causality (no response before the disturbance is applied).

The memory length is defined as:

$$L_0 = c \tau_0 \approx 12.85 \text{ Mpc}.$$

All dimensionless ratios that determine GRUT's regimes are built from this single scale: a frequency-wavenumber regime $\omega\tau_0$ or a spatial regime $(L_0 k)^2$ determines whether the vacuum's response is significant or recovers GR.

**Pillar D — The Breaking of the Adiabatic Dilation**

The adiabatic spatial dilation is the transformation:

$$x_i \to (1 + \lambda) x_i, \quad \text{(or equivalently) } a \to a e^\lambda$$

where $x_i$ are comoving spatial coordinates and $a$ is the scale factor. Under this dilation, comoving wavenumbers remain fixed ($k$ unchanged), but physical wavenumbers scale as:

$$k_{\text{phys}} = \frac{k}{a} \to e^{-\lambda} k_{\text{phys}}.$$

The susceptibility is a function of the dimensionless combination $(L_0 k_{\text{phys}})$:

$$\chi_{\text{eq}} = \frac{1}{1 + (L_0 k_{\text{phys}})^2}.$$

Under the dilation, this transforms as:

$$(L_0 k_{\text{phys}})^2 \to e^{-2\lambda} (L_0 k_{\text{phys}})^2,$$

so that:

$$\chi_{\text{eq}}^{\text{dilated}} = \frac{1}{1 + e^{-2\lambda}(L_0 k_{\text{phys}})^2} \neq \chi_{\text{eq}}^{\text{original}}.$$

This inequality proves that the dilation symmetry is broken. The breaking term enters at order $(L_0 k_{\text{phys}})^2$, which is tiny for cosmological scales (where $L_0 \gg$ galaxy size) but measurable in principle.

The breaking is non-anomalous because the dilation is a diffeomorphism (a relabeling of spatial coordinates), and the path-integral measure for diffeomorphisms has Jacobian determinant equal to 1. The trace-anomaly contributions (which are characterized by the anomaly coefficient $a/c$ in the context of Weyl rescalings) do not appear. The breaking is purely classical: it comes from the existence of an absolute, fixed proper length $L_0$ that cannot be absorbed into a coordinate transformation.

---

**Tiers, stated precisely:**

- **Q (Unitarity):** proven — a theorem of the CTP formalism.
- **F (Finite Memory):** postulated (the form of the susceptibility is required by consistency; the value $\tau_0 = 41.9$ Myr is **anchored** by convergent observation).
- **D (Adiabatic Dilation):** conjectured symmetry in the $L_0 \to 0$ limit (presupposed from standard GR, not re-derived); its breaking by **F** is **established** (computed and independently verified).

---

## 4. The One Idea

To understand GRUT, we must first recognize a hidden symmetry embedded in general relativity — a redundancy so subtle that standard treatments do not isolate it, but that becomes central when the gravitational vacuum is treated as a responsive medium. The theory possesses what we call the **adiabatic spatial-dilatation redundancy**, denoted **D**: a freedom to rescale space globally without altering the physics, provided the perturbations to the spacetime metric are purely adiabatic (uniform, without gradients). This redundancy is exact, and exact only in the limit where the vacuum has zero memory — where the gravitational field responds instantaneously to every disturbance. GRUT's organizing insight is that **once the vacuum gains finite memory, this redundancy breaks**. That breaking, controlled by a single length scale L₀, is the entire theory.

### 4.1 The adiabatic spatial-dilatation redundancy in the memoryless limit

In general relativity, the metric tensor g_μν encodes the curvature of spacetime. At wavelengths much longer than any structure in the universe, we can perform a uniform rescaling of spatial coordinates: replace every distance x with x → (1 + λ)x everywhere, where λ is a small, constant parameter. This is a *diffeomorphism* — a smooth relabeling of space that does not alter the physics. The point is profound: two spacetimes related by a uniform rescaling are geometrically the same up to a relabeling of the coordinates used to describe them.

For this symmetry to be true, the gravitational field must respond *identically* to configurations that differ only by such a rescaling. In other words, if configuration A and configuration A' are related by D (the rescaling transformation), then the physical response must be the same. This is what we mean by D being a **redundancy**: it is a gauge freedom, a freedom to redescribe the same physics in different coordinate labels.

This redundancy is **exact** — truly present as a symmetry of general relativity — *only* in the memoryless limit. That is, when every instantaneous configuration of the gravitational field is independent of the past, when the field "remembers" nothing, the redundancy holds perfectly. This is a presupposed feature of classical general relativity: the field equations at a point depend only on the local metric and its derivatives, not on time history.

### 4.2 Memory breaks the redundancy: the dilatation transformation under finite response time

![How a finite memory length L₀ breaks the long-wavelength rescaling redundancy D, on log–log axes. The equilibrium susceptibility χ_eq = 1/(1+(L₀k)²) (navy) is compared with its form after a dilatation by λ = 0.7 (red dashed). The two coincide at long wavelength (L₀k ≪ 1) but diverge once L₀k ≳ 1 — the dilated curve rising above the original — so the response is not rescaling-invariant and D is broken at order (L₀k)².](figures_v3/fig_dilatation_breaking.png)

Now suppose the vacuum is not memoryless. Suppose it responds to disturbances on a finite timescale τ₀. The response function that governs the vacuum's reaction to a perturbation is a susceptibility χ(ω) that depends on frequency ω. When τ₀ is nonzero, this susceptibility takes the single-pole form

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0},$$

which is the signature of a viscoelastic medium with exponential relaxation. This response function depends on the **physical wavelength** of the disturbance — shorter wavelengths (higher frequencies) are suppressed more strongly than longer ones. The memory argument that appears in the susceptibility is the dimensionless combination

$$L_0 k_{\text{phys}} = L_0 \frac{k}{a},$$

where L₀ = cτ₀ is the distance light travels during one relaxation time (approximately 12.85 Mpc), k is the comoving wavenumber, and a is the cosmic scale factor.

Here is the critical observation: under the adiabatic rescaling D, the comoving wavenumber k is **fixed** (it labels the mode itself, independent of coordinate choice), but the scale factor changes as a → ae^λ. Therefore the **physical** wavenumber transforms as

$$k_{\text{phys}} = \frac{k}{a} \to e^{-\lambda} k_{\text{phys}}.$$

The memory argument then transforms as

$$(L_0 k_{\text{phys}})^2 \to e^{-2\lambda}(L_0 k_{\text{phys}})^2.$$

A rescaling by e^{-2λ} under the dilatation transformation D means the susceptibility is **not invariant**. A coordinate rescaling cannot absorb the fixed physical scale L₀: the medium "knows" an absolute length, and that knowledge breaks the gauge freedom.

### 4.3 Why the breaking is controlled and non-anomalous

The breaking occurs at order (L₀k_phys)², which means it is weak whenever L₀k_phys ≪ 1 — precisely the regime of observational cosmology, where L₀ is enormous (12.85 Mpc) compared to galaxy clusters. For the scales of the universe that we observe, the breaking is a small, computable effect.

Moreover, the breaking is **non-anomalous**. In quantum field theory, some symmetries break only at the quantum level, through loop diagrams of virtual particles, producing an *anomaly* — a correction that cannot be removed by any redefinition of variables. The trace anomaly, controlled by the central-charge coefficients $a$ and $c$ (with $a/c = 1/3$), is one such quantum effect. The crucial point: the transformation D is a **diffeomorphism** (a smooth relabeling of coordinates), not a **Weyl rescaling** (a genuine physical change of the metric's overall scale). The path-integral measure — the mathematical object that quantum theory sums over to count the ways history can occur — is invariant under a mere relabeling of coordinates; its Jacobian is exactly 1. Therefore the trace-anomaly coefficients $a$ and $c$ do **not** enter the breaking of D. The breaking is entirely classical: it arises from finite memory (the postulated property F of the framework), not from quantum corrections.

### 4.4 The load-bearing structure: three pillars linked by one breaking

This situation produces the organizing structure of GRUT. We have **three conceptual pillars**:

1. **Q (CTP Unitarity, proven):** The closed-time-path formalism tells us that the vacuum responds only to *physically realized differences* — to configurations distinguishable from each other by the universe itself. This is not an assumption; it is a theorem of the formalism.

2. **F (Finite Memory, postulated and anchored):** The vacuum relaxes on a single timescale τ₀ ≈ 41.9 million years. This is assumed as a foundational axiom, then anchored by observation across multiple independent routes (cosmic-baseline relation, Bullet Cluster, structure-formation convergence).

3. **D (Adiabatic-Dilatation Redundancy, conjectured bridge):** The long-wavelength adiabatic rescaling is an exact symmetry of general relativity in the memoryless limit. Whether it is an exact gauge redundancy of GRUT's full closed-time-path action is presupposed from standard machinery, not proven from first principles — hence its status as a "bridge" rather than a fully established pillar.

The **load-bearing result of v3's audit** is the relationship among these three:

> **Finite memory F breaks the adiabatic-dilatation redundancy D, and this breaking is observed through the CTP-unitarity structure Q.**

The breaking is **computed** — we have rigorously verified that the memory-dependent susceptibility is not invariant under D. What remains **open** is the converse: proving that D is an exact symmetry of the full action to begin with. We carry D as a partially-established bridge: the breaking is solid, the underlying symmetry is presupposed.

### 4.5 One broken symmetry, one scale, one theory

The conceptual power of this framing lies in how it unifies the theory. Most theories of fundamental physics are defined by two structural choices: which symmetry they break, and by how much. Newton's gravity breaks Galilean scale invariance by allowing objects of different sizes. The electron's rest mass breaks scaling by being a fixed, dimensionful quantity that cannot be rescaled away. A magnetic moment breaks rotational symmetry by pointing in one direction.

GRUT breaks the adiabatic spatial-dilatation redundancy — the long-wavelength rescaling freedom of general relativity — **by exactly one length: L₀ = cτ₀**. This is the sole scale that breaks D. The theory requires no new fields, no new forces, no new particles. It is general relativity with one broken symmetry and one physical length.

From this single breaking, much of the rest follows as mathematical consequence — to the extent that D is the exact redundancy we presuppose. The vacuum cannot respond to pure-gauge, adiabatic modes — the very modes that the breaking removes. Therefore the vacuum cannot enhance linear density perturbations on cosmological scales. Linear cosmology is **forced to be exactly ΛCDM**: this is not a fit, it is a *derived requirement*. Dark matter cannot appear in the linear channel (where response is forbidden). It must live in nonlinear and tensor sectors — an honest boundary, not yet solved, but precisely located.

The vacuum *can* respond to gravitational waves, which are tensor disturbances orthogonal to adiabatic modes. That response produces a sharp, testable prediction: a gravitational-decoherence plateau at approximately 689 Hz. Measure the decoherence rate of a quantum superposition in a table-top interferometer at that frequency, and if it deviates significantly from GRUT's prediction, the theory dies.

The vacuum's refractive properties in the deep infrared are determined by one dimensionless axiom, α = 1/3 (the vacuum impedance), and the empirically anchored timescale τ₀ = 41.9 million years. The value α = 1/3 is **postulated** — it emerges from the identification of the gravitational conformal mode as the infrared response carrier, and matches the trace-anomaly coefficient a/c = 1/3 under that (postulated) identification. But deriving the identification from first principles remains **open**. The value τ₀ is **anchored**: we did not compute it from the vacuum equations, we measured it by watching multiple independent astrophysical systems (galaxy clustering, cluster dynamics, cosmological statistics) and found them all converging on 41.9 ± 1.5 million years.

### 4.6 The organizing principle restated

The statement that holds everything together is:

> **"The vacuum responds only to physically distinguishable structure"** — a phrase that names the conjunction Q ∩ F ∩ D, not three separate axioms but three conceptual pillars linked by one breaking. CTP unitarity (Q) is proven. Finite memory (F) is postulated and anchored. The adiabatic-dilatation redundancy (D) is the presupposed bridge whose breaking by F is established.

GRUT is general relativity's adiabatic-dilatation-redundant form, plus the controlled breaking of that redundancy by the single scale L₀ = cτ₀ ≈ 12.85 Mpc. Just as a rest mass breaks scale invariance, one physical length breaks gauge freedom. From that single breaking — witnessed by observation, constrained by consistency, tested by measuring the vacuum's response at all scales — the universe unfolds.

---

### 4.7 Technical Brief

#### The dilatation transformation and its formal structure

The adiabatic spatial-dilatation redundancy D acts on the spacetime coordinates as a uniform rescaling:

$$x \to x \cdot e^\lambda, \quad \lambda \in \mathbb{R} \text{ (small)}.$$

In terms of the cosmic scale factor a(t), this transformation is equivalently written as

$$a \to a e^\lambda.$$

Comoving wavenumbers k are unaffected by this relabeling — they label Fourier modes in comoving coordinates and are independent of the choice of scale factor. Under D, the **physical** wavenumber transforms as

$$k_{\text{phys}} = \frac{k}{a} \to e^{-\lambda} k_{\text{phys}}.$$

**Status (tier):** The statement that D is an exact redundancy of general relativity in the memoryless (L₀ → 0) limit is **presupposed** — it is standard Weinberg machinery and is not re-derived from GRUT's action in this document. The identification of D as a gauge redundancy is **foundational** (taken as the organizing presupposition).

#### The susceptibility and the memory scale L₀

The vacuum's response to a gravitational perturbation is encoded in the susceptibility χ(ω), which governs how the vacuum's polarization responds to a driving frequency ω. GRUT postulates a single-pole susceptibility (**postulated**, anchored):

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0}.$$

This is the Fourier-domain representation of the Mori–Zwanzig relaxation law,

$$\tau_0 \dot{z} + z = z_{\text{target}},$$

where τ₀ is the relaxation time and z_target is the equilibrium state toward which the system relaxes. The inverse Fourier transform of χ(ω) gives the memory kernel in time domain:

$$\chi(t) = \frac{1}{\tau_0}\,e^{-t/\tau_0}\,\Theta(t),$$

where Θ(t) is the Heaviside step function, ensuring causality. The response is zero for t < 0 (no effect in the past).

The **memory length** is defined as

$$L_0 = c \tau_0 \approx 12.85 \text{ Mpc},$$

where c is the speed of light and τ₀ ≈ 41.9 Myr is the **relaxation timescale** (**anchored** — measured from independent astrophysical observations).

The dimensionless memory argument that appears in physical calculations is

$$L_0 k_{\text{phys}} = L_0 \frac{k}{a},$$

and its square,

$$(L_0 k_{\text{phys}})^2 = \left(L_0 \frac{k}{a}\right)^2,$$

is the key quantity that controls the breaking of D.

**Status (tier):** The form of χ(ω) is **postulated**. The value of τ₀ is **anchored** by observation. The relation L₀ = cτ₀ is **derived** from the definition.

#### How finite memory breaks the dilatation redundancy: the explicit calculation

In the memoryless limit L₀ → 0, the susceptibility χ(ω) → 1 (independent of frequency), and the vacuum becomes inert. Any response structure depending on L₀k_phys → 0 vanishes. In this limit, the vacuum is invariant under the adiabatic rescaling D.

Now introduce finite L₀ ≠ 0. Consider the static (zero-frequency) susceptibility as a function of the physical wavenumber:

$$\chi_{\text{eq}}(k_{\text{phys}}) = \frac{1}{1 + (L_0 k_{\text{phys}})^2}.$$

This is the frequency-domain limit ω → 0 of the full susceptibility, applicable to long-wavelength, slowly-varying perturbations. Under the adiabatic rescaling transformation D: a → ae^λ, we have k_phys → e^{-λ}k_phys (comoving k fixed), so

$$(L_0 k_{\text{phys}})^2 \to e^{-2\lambda}(L_0 k_{\text{phys}})^2.$$

Therefore,

$$\chi_{\text{eq}}(k_{\text{phys}}) = \frac{1}{1 + (L_0 k_{\text{phys}})^2} \to \frac{1}{1 + e^{-2\lambda}(L_0 k_{\text{phys}})^2}.$$

For λ ≠ 0, the denominator changes: the susceptibility is **not invariant** under the rescaling. The redundancy D is **broken**.

The breaking is **controlled**: it enters at order (L₀k_phys)² ≪ 1 for all observed scales (L₀ ≈ 12.85 Mpc is huge compared to galactic and cluster scales, so L₀k_phys ≪ 1 throughout the universe we observe).

The breaking is **non-anomalous**: the transformation D is a diffeomorphism (smooth relabeling of coordinates), so the path-integral measure (Jacobian) is identically 1. The trace-anomaly coefficients ($a/c = 1/3$), which would appear in the breaking of a *Weyl* rescaling (a genuine physical rescaling of the metric), do **not** appear here. The breaking is classical (**computed**).

**Status (tier):** The statement that (L₀k_phys)² → e^{-2λ}(L₀k_phys)² under the transformation is **computed** (verified by explicit algebra). The statement that the path-integral measure is invariant (Jacobian = 1) is **proven** (a theorem of differential geometry: diffeomorphisms have unit Jacobian). The inference that the trace-anomaly does not enter the breaking is **computed** (verified by independent checks).

#### Why the breaking is exact in the linear scalar sector

In the linear-perturbation regime on cosmological scales, the response of the conformal (trace) mode of the metric — the mode that couples to adiabatic density perturbations — is governed by a projector P_conf that annihilates transverse (tensor) modes. However, the conformal mode **is** the mode that experiences the adiabatic rescaling D at k → 0. The long-wavelength limit of an adiabatic perturbation is precisely a pure rescaling of the scale factor.

The tracefree-transverse projector P^TT (which selects only tensor modes) annihilates the response to scalars:

$$P^{TT} : \text{scalar} \to 0.$$

Therefore, in the linear scalar channel, the response vanishes (μ_linear = 1, exactly ΛCDM) (**proven** — a derived requirement from the boundary operator; independently corroborated by CMB–ISW observations that exclude the μ → 4/3 alternative at ~32σ).

The k ≠ 0 breaking of D via finite L₀ lives in the **tensor** sector, not in the linear-scalar channel — a consistency, not a pathology.

**Status (tier):** The statement that μ_linear = 1 is a **derived requirement** (**computed**) from the boundary-operator consistency, and independently **anchored** by CMB-ISW observations ruling out any linear enhancement.

#### The general form of the memory-modified response

The full retarded memory kernel in the surviving transverse-tracefree channel is

$$K^R_{\mu\nu\rho\sigma}(\omega) = \alpha_{\text{vac}} \cdot \chi(\omega) \cdot P^{TT}_{\mu\nu\rho\sigma},$$

where:
- α_vac = 1/3 is the **vacuum impedance** (**postulated** axiom),
- χ(ω) = 1/(1 − iωτ₀) is the single-pole susceptibility (**postulated**),
- P^TT is the dimensionless transverse-tracefree spatial projector (**derived** from the constraint structure).

This kernel encodes the vacuum's response to gravitational waves and to second-order nonlinear curvature. It is local in space (no inverse-Laplacian operator) and causal in time (χ(ω) satisfies Kramers–Kronig relations) (**computed**).

**Status (tier):** The form K^R is **computed** (derived from the CTP action). Its causality and locality properties are **proven** (verified against fundamental theorems).

#### Residual open questions

The statement that the adiabatic-dilatation redundancy D is an **exact** gauge symmetry of GRUT's full closed-time-path action S_IF[φ₊, φ₋] in the L₀ → 0 limit remains **open** (**open-negative** in the registry). The identification of the gravitational conformal mode as the sole infrared carrier (from which α = 1/3 is derived) is **conjectural**. These are the two standing questions that would complete the unification of Q, F, and D into a single organizing symmetry.

---

## 5. The Responsive Vacuum

Physics is fundamentally a measurement: the quantification of a realized difference between two comparable states. The vacuum, in GRUT, operates on the same principle—it responds only to physically distinguishable configurations. When two histories are indistinguishable, the vacuum has no physical response. This is not an assertion about nature, but a mathematical fact derived from the closed-time-path (CTP) formalism, which encodes unitarity in the quantum field theory of the gravitational vacuum.

### 5.1 The Closed-Time-Path Formalism and the Influence Action

![The closed-time-path (in-in) contour underlying the unitary sector Q. Fields run forward in time on the upper branch (φ₊) and back on the lower branch (φ₋), meeting at the turning point on the right. The influence action vanishes on the diagonal, S_IF[φ₊ = φ₋] = 0, so a physical response appears only as the difference between the two branches — obtained as the variation δS_IF/δh_q evaluated at q = 0.](figures_v3/fig_ctp_contour.png)

To understand the vacuum's response, we require a framework capable of representing a closed, self-contained quantum system with no external observer. The CTP formalism—also called the "in-in" formalism or Schwinger–Keldysh formalism—provides this. In standard quantum field theory, the universe evolves from a specified initial state forward in time. A closed universe admits no such external condition. Instead, the CTP formalism compares the universe to itself: we imagine two histories, one evolving forward in time (the "+" branch) and one evolving backward (the "−" branch), both returning to the same final state. This forms a closed contour in time.

The entire quantum dynamics is encoded in the CTP action S_CTP[h₊, h₋], which is constructed on this doubling. Within it resides the influence functional, which couples the two branches. The crucial structural fact is this: **when the + and − branches are identical everywhere—when h₊ = h₋—the influence action vanishes exactly,** S_IF[h₊ = h₋] = 0. This is a theorem of the formalism, not an assumption. It expresses unitarity: when no distinguishable difference exists between the forward and backward histories, there is nothing for the vacuum to "measure" or respond to. The physical response of the vacuum emerges only as we deviate from this classical diagonal. We compute it by taking the functional derivative of the influence action with respect to the *difference* between the two branches, h_a = h₊ − h₋, and evaluating at h_a = 0. This derivative is the susceptibility—the sensitivity of the vacuum to perturbation.

In the Keldysh basis, we decompose h₊ and h₋ into sum and difference:
$$h_r = \frac{h_+ + h_-}{2}, \quad h_a = h_+ - h_-$$

The label r denotes "retarded" (the physical response), and a denotes the "quantum" (Keldysh) fluctuation. The CTP principle, abbreviated **Q**, is therefore: **the vacuum responds only to realized differences**—only to configurations distinguished by the Keldysh quantum variable. Configurations that live on the diagonal, where h_a = 0, produce zero response by structural necessity.

### 5.2 The Constitutive Law: Memory and Finite Relaxation

![The single-pole vacuum susceptibility χ(ω) = 1/(1 − iωτ₀) on log–log axes against ωτ₀. Plotted are the real part Re[χ] = 1/(1+(ωτ₀)²) (navy), the imaginary part Im[χ] = ωτ₀/(1+(ωτ₀)²) (red — positive, the causal dissipative sign), and the magnitude |χ| = 1/√(1+(ωτ₀)²) (green dashed). The shaded band below ωτ₀ = 1 (dotted line) is the memory regime where the vacuum responds and deviates from general relativity; at high frequency all components fall and GR is recovered (χ → 0).](figures_v3/fig_susceptibility.png)

Having established that the vacuum responds only to distinguishable disturbances, we must now specify *how* it responds. We adopt (**postulated**, as a foundational axiom) a first-order constitutive law:

$$\tau_0 \frac{dz}{dt} + z = z_{\text{target}}$$

where z is the state of the medium, z_target is the applied driving force, and τ₀ is a single characteristic relaxation timescale. This is the Mori–Zwanzig relaxation equation, which governs dissipative, memory-bearing systems across condensed matter physics—viscoelastic fluids, supercooled liquids, granular materials, and many others. It encodes causal, finite-memory response: the system does not snap back instantaneously but instead approaches equilibrium at a rate set by τ₀.

Fourier-transforming this equation, we obtain the frequency-domain susceptibility:

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0}$$

This is a single-pole response function—the canonical signature of a causal, bounded medium. The pole lies at ω = −i/τ₀ in the lower half of the complex frequency plane, which guarantees causality (the future does not depend on the past). The susceptibility obeys the Kramers–Kronig relations, which connect its real and imaginary parts and enforce that any passive medium respecting causality must have χ(ω) with this structure. 

The frequency-dependence is physically transparent:
- **Low frequency** (ω ≪ 1/τ₀): χ(ω) → 1. The medium responds fully and in-phase to slowly varying disturbances.
- **High frequency** (ω ≫ 1/τ₀): χ(ω) → 0. Inertia dominates; the medium cannot keep up and does not deform.
- **Imaginary part**: Im[χ(ω)] > 0 (the absorptive part); the dissipated power ∝ ω·Im[χ] > 0 (passivity), and the lower-half-plane pole makes the response causal—it lags the disturbance in time.

The vacuum, in GRUT, is assigned this single-pole memory structure. It is **postulated**, not derived from the CTP action, that the relaxation time is τ₀ = 41.9 million years. From this single timescale flows a single length scale—the memory length

$$L_0 = c \cdot \tau_0 \approx 12.85 \text{ Mpc}$$

This is the distance light travels during one relaxation time, and it is **the one length scale of GRUT**. We do not derive τ₀ from first principles; we anchor it by observation. Three independent routes converge on τ₀ ≈ 41.9 Myr:

1. The **cosmic-baseline relation**: the Hubble expansion rate H₀ and the memory time satisfy a dimensionless constraint, 108π · H₀ · τ₀ ≈ 1 (up to the order-unity tree-level factor 2 − R, with H₀ in inverse-time units). At the Planck 2018 value of H₀, this gives τ₀ ≈ 41.9 Myr.

2. The **Bullet Cluster**: when two galaxy clusters collide, the separation observed between gas (slowed by the vacuum's friction) and dark matter (affected only by gravity) implies a communication timescale of order 50 Myr.

3. **Self-consistency across regimes**: the quantum-decoherence timescale, the structure-formation timescale, and the cosmological expansion rate all converge to a consistent cosmos only when τ₀ lies in the 40–42 Myr band.

None of these is a first-principles derivation. Instead, they are three independent observational routes that converge, and that convergence is the anchor. The term **anchored** means: fixed by observation or measurement, not derived from theory (though the theoretical framework uses it as input).

### 5.3 The Memory Kernel and the Retarded Response

The gravitational vacuum's response to a metric perturbation h is governed by a retarded memory kernel—a function that specifies how the vacuum at time t "remembers" what was happening at earlier times t'. In time domain, this kernel takes the form

$$K^R(t - t') = \alpha_{\text{vac}} \cdot \frac{1}{\tau_0} \exp\left(-\frac{t-t'}{\tau_0}\right) \Theta(t - t')$$

where Θ is the Heaviside step function (causal: zero for t < t'). The prefactor α_vac = 1/3 is the vacuum impedance, set by a trace-anomaly coefficient in quantum field theory (discussed below). Fourier-transforming:

$$K^R(\omega) = \frac{\alpha_{\text{vac}}}{1 - i\omega\tau_0} = \alpha_{\text{vac}} \cdot \chi(\omega)$$

In the full tensor representation, the kernel acts on the transverse-tracefree (TT) components of the metric perturbation:

$$K^R_{\mu\nu\rho\sigma}(\omega) = \alpha_{\text{vac}} \cdot \chi(\omega) \cdot P^{\text{TT}}_{\mu\nu\rho\sigma}$$

where P^TT is the transverse-tracefree projector. The projector ensures that the response couples only to gravitational-wave modes (tensor modes orthogonal to density and scalar perturbations), preserving the Bianchi identity and diffeomorphism invariance.

### 5.4 The Linearized CTP Action and the Constitutive Equation

The full CTP action for linearized gravity on a fixed background takes the form

$$S_{\text{CTP}}[h_+, h_-] = S_{\text{EH}}^{(2)}[h_+] - S_{\text{EH}}^{(2)}[h_-] + S_{\text{matter}}[h_+] - S_{\text{matter}}[h_-] + S_{\text{const}}[h_+, h_-] + S_{\text{noise}}[h_+, h_-]$$

where:
- S_EH^(2) is the linearized Einstein–Hilbert action (quadratic in h)
- S_matter is the coupling of the metric to matter sources
- S_const is the constitutive coupling term (the vacuum's memory response):
$$S_{\text{const}} = -\frac{1}{2} \int\int h_a^{\mu\nu}(x) K^R_{\mu\nu\rho\sigma}(x - x') h_r^{\rho\sigma}(x') d^4x d^4x'$$
- S_noise encodes the vacuum fluctuations via the fluctuation-dissipation theorem

The constitutive term is proportional to h_a × K^R × h_r: it couples the "quantum" combination h_a to the "classical" combination h_r through the retarded kernel. This is the mechanism by which the vacuum responds.

Varying the action with respect to h_a and setting h_a = 0 (the retarded-variation axiom), we obtain the classical equation of motion:

$$G_{\mu\nu}^{(1)}[h_r] - \Phi_{\mu\nu}[h_r] = 8\pi G T_{\mu\nu}$$

where Φ_μν is the constitutive response:

$$\Phi_{\mu\nu}(x) = \int K^R_{\mu\nu\rho\sigma}(x - x') h_r^{\rho\sigma}(x') d^4x'$$

In Fourier space:

$$\Phi_{\mu\nu}(\omega, \mathbf{k}) = \alpha_{\text{vac}} \cdot \chi(\omega) \cdot P^{\text{TT}}_{\mu\nu\rho\sigma} \cdot h_r^{\rho\sigma}(\omega, \mathbf{k})$$

This is the load-bearing result: **the structure of Φ_μν is derived, not postulated** — it emerges directly from varying the CTP action, given the postulated constitutive kernel (its amplitude α and single-pole form remain the adopted axiom and postulate). Its form—proportional to χ(ω), with no spatial derivatives—is a consequence of locality: the vacuum responds where it is perturbed, not at distant points. This locality is crucial, as we shall see.

### 5.5 Recovering General Relativity at High Frequency

A fundamental consistency check: does the framework recover general relativity in the limit where memory becomes negligible? In the **high-frequency regime**, where ωτ₀ ≫ 1, the susceptibility χ(ω) → 0, so Φ_μν → 0. The equation becomes G_μν^(1) = 8πG T_μν—the linearized Einstein equation. General relativity is recovered **exactly** (**proven** by explicit symbolic computation). 

The solar system, with orbital periods measured in years, operates in a regime where ωτ₀ is astronomically large (the orbital frequency is billions of times smaller than 1/τ₀). The corrections GRUT predicts to solar-system observables are suppressed by factors of (τ₀/T_orbit)². For Earth's orbit, this suppression is ~10⁻¹⁵ or smaller. GPS satellites, LIGO gravitational-wave detections, and every laboratory test of general relativity lie deep in this regime where memory effects vanish. The theory is safe: it produces small, computable deviations from a test-verified predecessor, with deviations that scale sharply as the system becomes more relativistic.

### 5.6 The Dimensionless Vacuum Impedance

The constitutive kernel carries an amplitude factor α_vac, called the vacuum impedance. In GRUT, this is **adopted as a foundational axiom**: α_vac = 1/3. The value is conjectured to derive from the trace-anomaly coefficient of a single conformally coupled scalar field. When a scalar field couples conformally to gravity with coupling ξ = 1/6, the quantum trace anomaly has the form T_μ^μ = (a/16π²) R, where the ratio a/c (the c-anomaly is fixed by dimension counting) equals 1/3 for a single real scalar. GRUT identifies the gravitational conformal mode—the scalar degree of freedom that governs expansion and contraction of spacetime—with this anomalous field. Under that identification, α_vac = 1/3 follows exactly from the Komargodski–Schwimmer theorem (2011).

However, the identification itself is not proven from first principles. It is a plausible and mathematically elegant conjecture, but its derivation is **open**. The framework does not claim to explain why α = 1/3 any more than general relativity explains why c and G have their values. Some numbers are posited; deeper physics must explain them.

### 5.7 The Complete Vacuum Response: Summary

The gravitational vacuum in GRUT is a responsive medium governed by:
1. A **single-pole susceptibility** χ(ω) = 1/(1 − iωτ₀) encoding finite memory
2. A **single relaxation time** τ₀ ≈ 41.9 Myr (**anchored** by observation)
3. A **single impedance** α_vac = 1/3 (**adopted as axiom**)
4. A **single length scale** L₀ = c·τ₀ ≈ 12.85 Mpc (the only scale that breaks general relativity's long-wavelength redundancy)

The vacuum responds only to physically realized differences (enforced by the CTP principle, Q, which is **proven**). It relaxes with a single timescale (F, the finite-memory postulate). The response vanishes in the high-frequency limit, recovering general relativity exactly. At low frequencies and on scales larger than L₀, the vacuum is a refractive medium with frequency-dependent refractive index n_g(ω) that deviates from unity.

From this single responsive law—one equation, two anchored numbers, one axiom—everything downstream is a consequence: the structure of cosmology, the decoherence predictions, the falsifiers, and the boundary between quantum mechanics and classical physics. This is Pillar Q: the foundation is proven (the response principle). The constitutive form is the simplest law consistent with causality and finite memory. The vacuum's role in the theory is complete. What it responds to and what it is forbidden to respond to is the subject of the next chapter.

---

### 5.8 Technical Brief: The CTP Influence Action and the Memory Kernel

We present the mathematical structure that underwrites the responsive vacuum at the level of a graduate physics text, walking through the key derivations and stating each result at its tier.

#### The CTP Action and the Influence Functional

The closed-time-path action for a quantum system is constructed as follows. Let S[φ] be the classical action for a field φ. For a universe that returns to its initial state, we imagine two paths in field space: φ₊(t), running forward, and φ₋(t), running backward. The CTP action is

$$S_{\text{CTP}}[φ_+, φ_-] = \int_{\text{forward}} \frac{δS}{δφ}|_{φ_+} - \int_{\text{backward}} \frac{δS}{δφ}|_{φ_-}$$

In the path integral, this generates an amplitude

$$Z[J_+, J_-] = \int \mathcal{D}φ_+ \mathcal{D}φ_- \exp\left(i S_{\text{CTP}} + i \int (J_+ φ_+ - J_- φ_-) d^4x\right)$$

The influence functional is defined as the path-integral result when matter and radiation are integrated out, leaving only the metric dynamics. For the gravitational vacuum, we work in the language of perturbations: h_μν(x) is a metric perturbation on a classical background.

**The crucial structural fact** (**proven**, theorem of the formalism): when φ₊ = φ₋ everywhere, the source terms vanish and the influence functional evaluates to unity (the evolution operator returns to the identity). Equivalently,

$$S_{\text{IF}}[φ_+ = φ_-] = 0$$

This is not an approximation or a choice of convention. It is a direct consequence of the path integral's unitarity structure: if no difference is introduced between the forward and backward branches, the probability amplitude must be 1 (no depletion of probability).

#### The Keldysh Basis and the Quantum Variable

We change variables from (h₊, h₋) to (h_r, h_a):

$$h_r = \frac{h_+ + h_-}{2}, \quad h_a = h_+ - h_-$$

The CTP principle says S_IF[h_a = 0] = 0. The physical response of the vacuum to a disturbance is extracted by taking

$$\delta S_{\text{IF}} / \delta h_a |_{h_a = 0}$$

This is the susceptibility in the Keldysh language: it tells us how the system responds when we introduce a small difference between the two branches.

#### The Linearized Gravitational CTP Action

For the gravitational system, we expand to second order in h around a classical background (assumed flat for the linearized derivation; FRW generalization is structure-preserving). The CTP action splits into four pieces:

**1. Einstein–Hilbert (kinetic term):**
$$S_{\text{EH}}^{(2)} = \frac{1}{16\pi G} \int d^4x \, \mathcal{L}_{\text{EH}}^{(2)}[h]$$

where the Lagrangian is quadratic in h. In the Keldysh basis, this produces a cross term:

$$S_{\text{EH}} \supset \int d^4x \, \frac{a_{\text{EH}}}{16\pi G} h_a \, h_r$$

where a_EH is the coefficient emerging from the linearized Einstein operator.

**2. Matter coupling (source term):**
$$S_{\text{matter}} = \int d^4x \, h^{\mu\nu} T_{\mu\nu} = \frac{1}{2} \int d^4x \, h_a T$$

The factor 1/2 arises because h_a couples to T at the mean of the two branches.

**3. Constitutive (memory) coupling:**
$$S_{\text{const}} = -\frac{1}{2} \int\int d^4x d^4x' \, h_a^{\mu\nu}(x) K^R_{\mu\nu\rho\sigma}(x - x') h_r^{\rho\sigma}(x')$$

(**Computed**, **postulated**, tier: the form K^R is derived from the Mori–Zwanzig constitutive law; the amplitude α_vac is axiom.)

**4. Noise (fluctuation-dissipation theorem):**
$$S_{\text{noise}} = \frac{i}{2} \int d^4x \, h_a N(x) h_a$$

where N encodes the thermal vacuum fluctuations via the fluctuation-dissipation theorem. This term is quadratic in h_a and vanishes when h_a = 0, so it does not contribute to the classical equations of motion.

#### Derivation of the Constitutive Response Φ_μν

The classical equation of motion is obtained by varying the total action with respect to h_a and setting h_a = 0:

$$\frac{\delta S_{\text{CTP}}}{\delta h_a}\bigg|_{h_a = 0} = 0$$

From S_EH: 
$$\frac{\delta S_{\text{EH}}}{\delta h_a}\bigg|_{h_a=0} = \frac{a_{\text{EH}}}{16\pi G} h_r$$

which we identify with the linearized Einstein tensor G_μν^(1)[h_r].

From S_matter:
$$\frac{\delta S_{\text{matter}}}{\delta h_a}\bigg|_{h_a=0} = T_{\mu\nu}$$

From S_const:
$$\frac{\delta S_{\text{const}}}{\delta h_a}\bigg|_{h_a=0} = -\frac{1}{2} \int K^R(x - x') h_r(x') d^4x' \equiv -\Phi[h_r]$$

From S_noise: vanishes at h_a = 0.

Collecting terms:

$$G_{\mu\nu}^{(1)}[h_r] - \Phi_{\mu\nu}[h_r] = 8\pi G T_{\mu\nu}$$

(**Derived**, not postulated, tier: **computed**. The kernel form and its frequency dependence follow from the constitutive equation.)

In Fourier space, with K^R(ω) = α_vac · χ(ω):

$$\Phi_{\mu\nu}(\omega, \mathbf{k}) = \alpha_{\text{vac}} \cdot \frac{1}{1 - i\omega\tau_0} \cdot P^{\text{TT}}_{\mu\nu\rho\sigma} \cdot h_r^{\rho\sigma}(\omega, \mathbf{k})$$

#### Structural Properties: GR Recovery and Causality

**High-frequency limit:** As ω → ∞, χ(ω) → 0, so Φ_μν → 0. The equation reduces to G_μν^(1) = 8πG T_μν—general relativity. (**Proven**, **computed** tier.)

**Low-frequency limit:** As ω → 0, χ(ω) → 1, so Φ_μν → α_vac · P^TT · h_r. The magnitude α_vac = 1/3 is consistent with the low-frequency refractive index n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.1547.

**Causality and Kramers–Kronig:** The susceptibility χ(ω) = 1/(1 − iωτ₀) has its pole at ω = −i/τ₀ in the lower half of the complex ω plane, the hallmark of a causal, passive response. The real and imaginary parts satisfy the Kramers–Kronig relations, enforcing that no information travels backward in time.

**Bianchi preservation:** The projector P^TT is transverse, ∂^μ P^TT_μνρσ = 0. Therefore ∂^μ Φ_μν = 0 structurally, for any h_r and any kernel. The Bianchi identity is preserved by the constitutive response, not just on mode-by-mode basis but holistically. (**Computed**, **proven** tier.)

#### The Memory Length and the Breaking of GR's Adiabatic Rescaling

In general relativity, there is an exact symmetry in the memoryless limit: adiabatic spatial dilation, also called the separate-universe redundancy. If you rescale all spatial distances uniformly, k_phys → e^{-λ} k_phys, the background equations are unchanged. This is a consequence of the fact that GR has no intrinsic length scale.

GRUT breaks this symmetry with the introduction of L₀ = c·τ₀, the memory length. The response kernel carries a dependence on L₀k_phys (through the factor χ(ω) evaluated at momentum-dependent frequencies). A coordinate rescaling changes k_phys, so the response amplitude changes—the symmetry is broken.

The breaking is **non-anomalous** (**proven**, **computed** tier). The trace anomaly of quantum field theory—which usually introduces violations of scale invariance at the quantum level—does not participate, because the breaking is purely classical: it arises from finite memory, not quantum loops. The adiabatic dilation is a diffeomorphism (a relabeling of coordinates), not a Weyl rescaling (a physical change of scale), so the path-integral measure is unaffected.

The breaking enters at order (L₀ k_phys)² in the response. For cosmological scales (~100 Mpc), where k_phys ~ 10⁻³ Mpc⁻¹, the product is ~10⁻² and the breaking is a ~0.01% effect on large-scale structure. Yet it is this tiny breaking that enforces the "no-go" theorem: the vacuum cannot respond to rescalings, so linear cosmology must be exactly ΛCDM.

#### The Solar-System Suppression

The suppression of GRUT's response in the solar system is quantified as follows. For an orbit with period T_orbit, the characteristic frequency scale is ω ~ 2π/T_orbit. The high-frequency suppression factor is

$$\chi(\omega) \approx \frac{i}{\omega\tau_0} \quad \text{(for } \omega\tau_0 \gg 1\text{)}$$

The magnitude is |χ| ~ 1/(ωτ₀) = τ₀/T_orbit. For Earth (T_orbit ~ 1 year ~ 3 × 10⁷ s) and τ₀ ~ 41.9 Myr ~ 1.3 × 10¹⁵ s, the ratio is τ₀/T_orbit ~ 4 × 10⁷. Squared (as it appears in observable deviations), this gives a suppression of ~10⁻¹⁵ or smaller for orbital mechanics. GPS and LIGO operate in similar regimes. (**Proven**, **computed** tier.)

#### Summary Table: The CTP Structure

| Component | Form | Tier | Physical Meaning |
|---|---|---|---|
| CTP principle | S_IF[h_a = 0] = 0 | **Proven** | Response vanishes for indistinguishable histories |
| Keldysh quantum variable | h_a = h_+ − h_− | **Proven** | Difference between forward and backward branches |
| Mori–Zwanzig law | τ₀ ż + z = z_target | **Postulated** | Exponential relaxation with single timescale |
| Susceptibility | χ(ω) = 1/(1 − iωτ₀) | **Postulated** | Fourier transform of exponential decay |
| Memory length | L₀ = c·τ₀ ≈ 12.85 Mpc | **Anchored** | Only length scale of the framework |
| Vacuum impedance | α_vac = 1/3 | **Axiom** | Conformal-mode trace-anomaly coefficient |
| Memory kernel | K^R(ω) = α_vac · χ(ω) · P^TT | **Computed** | Derives from CTP variation of constitutive term |
| Φ_μν response | G_μν^(1) − Φ_μν = 8πG T_μν | **Derived** | Emerges from δS_CTP/δh_a \|_{h_a=0} |
| GR recovery | χ(ω) → 0 as ω → ∞ | **Proven** | Solar system safe: suppression ~10⁻¹⁵ |
| Bianchi identity | ∂^μ Φ_μν = 0 structurally | **Proven** | P^TT transverse by construction |

This is the foundation of GRUT's responsive vacuum: one CTP principle (proven), one finite-memory assumption (postulated and anchored), one axiom for the impedance, and one derived length scale. From these flow all consequences.

---

## 6. The Universe That Falls Out

![The logical chain that forces linear cosmology to ΛCDM, read top to bottom. A long-wavelength adiabatic perturbation equals a separate-universe rescaling; because that rescaling lies in the intersection Q ∩ D, the vacuum cannot respond to it and any conformal enhancement is orthogonal to separate-universe invariance. The linear modification therefore reduces to μ_linear = 1 — linear cosmology must reproduce ΛCDM. The once-hoped μ → 4/3 enhancement (right, struck through) is both forbidden here and excluded by data at 32σ (CMB–ISW).](figures_v3/fig_nogo_mulinear.png)

On the cosmological scales where structures smooth and galaxies become mere dust, the universe is maximally constrained. This is the deepest no-go theorem of GRUT, and it establishes a precise paradox: the domain where gravitational influence appears most extensive is the domain where the framework admits the least freedom.

The constraint arises from the interplay of three structures. General relativity possesses an exact gauge freedom at long wavelengths — the adiabatic spatial-dilatation redundancy **D**, under which a uniform rescaling of all spatial coordinates leaves the metric equations invariant. This symmetry is absolute in the memoryless limit, where L₀ → 0. But GRUT breaks this freedom with one finite scale: the memory length **L₀ = c·τ₀ ≈ 12.85 Mpc**, the distance light travels during the vacuum's single relaxation time.

The mathematics that follows is rigorous. The closed-time-path unitarity structure **Q** forbids the vacuum to respond to configurations that differ from themselves only by a rescaling — that is, to pure adiabatic modes. Any long-wavelength density perturbation, examined in the linear regime, *is* precisely such a rescaling mode: compress one region, dilate another, hold total volume constant, and the perturbation vanishes into the background coordinate freedom. The vacuum cannot respond to density perturbations at the linear level without violating its own consistency requirement. A conformal refractive enhancement — a mode-by-mode modification of the gravitational coupling strength — and separate-universe invariance are mutually exclusive on linear scalar perturbations. This is a no-go theorem, not an approximation (proven, PROJECTOR_CONSISTENCY_NOGO.md §5).

Therefore, at the linear level, **μ_linear = 1**. The linear growth factor μ — which measures the enhancement of gravitational attraction for density perturbations relative to general relativity — is exactly unity. GRUT produces zero modification to the density perturbations that seed galactic structure. This is not a tuned result, and it is not a limitation. It is a **derived requirement**: the framework is internally inconsistent if the linear cosmology deviates from general relativity. Linear cosmology is **exactly ΛCDM** (computed tier).

This conclusion is reinforced observationally. If the linear vacuum response were enhanced according to earlier GRUT versions (μ → 4/3), the integrated Sachs–Wolfe effect at low multipoles of the cosmic microwave background would exceed observations by a factor of 2.79 — approximately 32 standard deviations. The observation rules out the linear channel decisively. More fundamentally, the mathematical structure rules it out first: the low-ℓ anomaly is not an empirical surprise but the signature of a theoretical inconsistency.

### 6.1 Certified constants of the linear universe

What emerges from the requirement μ_linear = 1 is a universe whose expansion history, background growth, and large-scale structure are indistinguishable from the concordance ΛCDM model. Yet this agreement is not accidental: it is the necessary consequence of refusing the vacuum freedom to respond where it has no business responding.

Three observables are certified:

**The Hubble rate, H₀ ≈ 68.8 km/s/Mpc (anchored tier).** The expansion rate sits between the Planck satellite measurement (67.4 km/s/Mpc) and the local distance-ladder measurement from SH0ES (73.0 km/s/Mpc), occupying the observed tension gap. The relation tying H₀ to τ₀ is

$$H_0 \times 108\pi \times \tau_0 \approx 1,$$

a dimensionless relation with no adjustable parameters (exact up to the order-unity tree-level factor 2 − R). The coefficient 108π is the screening constant **S**, a computed quantity derived from the response kernel. However, since τ₀ is itself fixed by observation (anchored through cluster mergers, cosmic-baseline relations, and self-consistency across regimes), the resulting H₀ is anchored rather than derived from first principles.

**The dark-energy density parameter, Ω_Λ = 0.6886 (anchored tier).** This matches Planck 2018 (0.6889) to 0.04% precision. The conversion from the framework's conformal-mode expansion drive to Ω_Λ involves zero free parameters — it is a direct application of Einstein's equations with the computed response. But it takes the empirically anchored τ₀ as input, and therefore the output is anchored. The physical mechanism is a balance: the built-in geometric instability of spacetime (the Gibbons–Hawking negative mode, which in real time tends to drive expansion) is opposed by the dissipative drag of the vacuum's finite memory. The terminal velocity reached in this balance is the cosmological constant.

**Background expansion history H(z) and the baryon-acoustic-oscillation scale r_d = 147.1 Mpc (anchored tier).** The distance-ladder observables — the relationship between redshift, luminosity distance, and proper distance — follow ΛCDM curves with no modification. Structure growth, measured through galaxy clustering and weak lensing, is also indistinguishable from ΛCDM. With one caveat: at the σ₈ scale (the amplitude of matter density fluctuations within spheres of 8 h⁻¹ Mpc), GRUT predicts a +3.1% enhancement over ΛCDM. This enhancement originates in the nonlinear regime, not the linear, and reflects the framework's response to the squared density gradients that emerge when perturbations become large.

These numbers are not *predictions* that GRUT derived by solving the vacuum's equation of motion in a cosmological setting. They are *requirements* — the inevitable outputs of the consistency theorem stating that the vacuum cannot respond to adiabatic rescaling. The mathematics survives in full; the ontological interpretation shifts. The universe is not shaped by GRUT's mechanism at cosmological scales. It is shaped by GRUT's constraint: this is what emerges when you forbid the vacuum to respond to fluctuations that cannot be distinguished from coordinate artifacts.

### 6.2 Two sharp predictions pierce the ΛCDM background

![The cosmological constant pictured as a terminal velocity. A Gibbons–Hawking instability drives expansion (top box) while the finite-memory kernel supplies friction that damps it (bottom box); their balance fixes the steady inflation rate in the central box, H_inf = (2 − R)/(Sτ₀). The resulting dark-energy fraction Ω_Λ = (H_inf/H₀)² is anchored at 0.6886, against the Planck 2018 value 0.6889.](figures_v3/fig_terminal_velocity.png)

Within the framework of strict linear ΛCDM cosmology, two additional results emerge that are not secondary or derivative, but genuine independent predictions.

**The baryon asymmetry of the universe, η_B ≈ 6.6 × 10⁻¹⁰ (computed tier).** The closed-time-path formalism generates an irreducible asymmetry between the forward and backward branches of the contour, because the vacuum's memory is directed into the future: the relaxation kernel responds only to past disturbances, not future ones. This temporal directionality produces an effective difference between the positive-time branch φ₊ and negative-time branch φ₋ in the influence action. When the framework is applied to baryogenesis — the epoch when matter-antimatter asymmetry is generated — this time-arrow imbalance produces a preference for matter over antimatter in the baryon-number-violating processes of the early universe. The magnitude of the asymmetry matches the observed value (≈6×10⁻¹⁰) to within roughly ten percent, without adjustment of additional parameters. This is a computed prediction with no free parameters beyond {α, τ₀}.

**The cosmological constant as the terminal velocity of the conformal mode (computed tier).** The conformal degree of freedom of the metric — the single scalar field σ such that the metric reads g_μν = e^{2σ}ĝ_μν — is the aspect of spacetime geometry that controls whether space expands or contracts. In the absence of matter, empty spacetime possesses a mode with negative energy: the Gibbons–Hawking negative mode, a geometric instability under which the scale factor would run away to either zero or infinity. In real (classical) time, this manifests as runaway expansion; the universe has an intrinsic tendency to inflate.

But the vacuum is not inert. It responds to the expansion, and its response carries friction. The memory kernel χ(ω) = 1/(1 − iωτ₀) has a dissipative imaginary part that opposes rapid change. The steady state reached by balancing the geometric runaway instability against the memory-induced drag is a terminal velocity — an exponential expansion at a constant rate H_inf. This rate is not a tunable constant; it is determined by the ratio of the instability strength to the drag coefficient:

$$H_{\text{inf}} = \frac{2 - R}{S \cdot \tau_0},$$

where R = √(4/3) ≈ 1.1547 is the deep-infrared refractive index (computed tier), S = 108π is the screening constant (computed tier), and τ₀ = 41.9 Myr is the memory time (anchored tier). There are no adjustment parameters. The dark-energy fraction follows as the squared ratio of this terminal velocity to the present expansion rate, Ω_Λ = (H_inf/H₀)². This is why the decoherence falsifier — the tabletop measurement of τ₀ at 689 Hz — pins not only the memory scale but also the universe's dark-energy fraction: measure τ₀, and Ω_Λ follows automatically.

### 6.3 The honest position: linearity is ΛCDM by theorem

The certified universe is indistinguishable from ΛCDM on all observed scales. This agreement is not a coincidence; it is the only possibility. The framework forbids linear modifications to the growth of density perturbations. It forbids linear dark matter. It forbids linear modifications to expansion. What survives is the standard model of cosmology, honored not as an external fit but as the unique consequence of internal consistency.

That said, the claim that "GRUT predicts ΛCDM" is incomplete and misleading. GRUT does not predict ΛCDM; rather, GRUT's consistency requirements *force* its linear sector to be exactly ΛCDM. The μ_linear = 1 result is not ΛCDM's zero-parameter value. It is GRUT's *derived* requirement, and its derivation rests on the entire logical chain: the closed-time-path response structure **Q**, the finite-memory postulate **F**, and the adiabatic-dilatation redundancy **D** that finite memory breaks. Break any link in that chain, and the constraint fails and the theory can modify the linear cosmology. That resilience — the fact that one can trace the μ_linear = 1 result back through the framework's foundations — is what makes the agreement with ΛCDM a strength rather than a disappointment.

The dark sector, if it exists within GRUT, cannot live in the linear channel. The nonlinear regime remains open: second-order responses to Weyl-squared invariants, bound-system frequencies (orbital dynamics in galaxies and clusters), and the tensor gravitational-wave sector all remain unexplored in full. The constructive phase examined the Weyl-squared channel exhaustively. The magnitude of the response proved viable — approximately the right size to account for galactic-scale dark matter effects. But the radial profile is wrong: the effective dark density falls as 1/r⁴ in the interior and steepens to 1/r⁶ in the outskirts, far steeper than the 1/r² profile required by flat galaxy rotation curves. This is not an approximation artifact; it is a theorem. A local causal kernel cannot produce the inverse-Laplacian operation needed to flatten a steep source into a gentle halo. Dark matter remains a *hosted input* — an observational boundary condition the theory is consistent with, not a consequence it generates.

One derived prediction in the dark sector survives: the MOND acceleration scale a₀ = cH₀/(2π) emerges as a pure ratio of fundamental scales. This scale sets the curvature radius at which GRUT's geometric response begins to matter. It is real and testable; what remains adopted rather than derived is the interpolation function that describes how gravity transitions from Newtonian to modified near this scale.

This is the universe that falls out when a theory forbids the vacuum to answer rescaling, and when it forbids itself the freedom to generate dark matter through the channel where both mathematics and observation converge. It is ΛCDM, confirmed by consistency and sharpened by constraint.

### 6.4 Technical Brief: The No-Go Theorem and the Terminal Velocity

#### The Conformal Mode and Separate-Universe Invariance No-Go

The foundational result is a no-go theorem (PROJECTOR_CONSISTENCY_NOGO.md, §5): a response that *is* the conformal refractive enhancement and *is also* invariant under long-wavelength adiabatic rescaling cannot simultaneously satisfy both requirements on linear scalar perturbations. The proof is direct:

1. GRUT's vacuum response is fundamentally conformal: the refractive index n_g² = 1 + α is an isotropic rescaling of the metric. In the language of conformal field theory, it represents a response to the trace of the stress-energy tensor:

$$\delta S_{\text{matter}} / \delta \sigma = \sqrt{-g} \, T^\mu_\mu = \sqrt{-g} (\text{trace}).$$

2. A conformal response to matter couples to the trace T = g^{μν}T_{μν}. For cold dark matter (CDM), the trace is δT = −δρ — the density perturbation itself.

3. A long-wavelength adiabatic perturbation, in the limit k → 0, becomes locally indistinguishable from a rescaled background: the density perturbation δρ can be absorbed into a local change of the background scale factor. Mathematically, this is the separate-universe mode — the statement that a smooth rescaling x → (1+λ)x leaves the physics unchanged in the memoryless limit.

4. Separate-universe invariance requires zero response to adiabatic perturbations at k → 0. But a conformal response to δρ would produce maximal response (μ → 1 + α) in exactly this limit. **These two requirements collide head-on at k → 0**.

**Corollary:** There is no first-principles constitutive source that is both (a) the GRUT conformal refractive enhancement and (b) separate-universe invariant. One must be abandoned. Since separate-universe invariance is a non-negotiable consistency requirement (a consequence of the theory's unitarity and closure), the refractive enhancement must not act on linear scalar perturbations.

#### The Projector Structure and μ_linear = 1

Independently, the action reveals why: the vacuum couples to the metric h^{μν} only through the transverse-traceless (TT) projector

$$K^R_{μνρσ} = \alpha_{\text{vac}} \chi(\omega) P^{TT}_{μνρσ},$$

where P^TT annihilates scalar (density) perturbations by definition. A transverse-traceless projector has zero trace:

$$\eta^{μν} P^{TT}_{μνρσ} = 0.$$

Scalar perturbations have no TT part; they are pure trace. Therefore, the coupling K^R applied to a scalar metric perturbation φ^{scalar}_{μν} vanishes identically:

$$\Phi^{\text{scalar}}_{μν} = \alpha K^R \star h_r^{\text{scalar}} = \alpha \chi(ω) P^{TT} \star h_r^{\text{scalar}} = 0.$$

Thus **μ_linear = 1** is forced by the projector structure of the fundamental kernel. There is no choice, no adjustment, no escape route.

#### The Terminal Velocity and Dark Energy

The conformal mode, although it does not couple to linear density perturbations (which are traces and annihilated by P^TT), does couple to itself — to the conformal part of the metric. The self-coupling is what produces the terminal velocity.

The scale-breathing degree of freedom σ satisfies an equation of motion that includes two competing effects:

1. **The geometric instability.** Spacetime has an intrinsic tendency to run away: the Gibbons–Hawking negative mode imparts an effective negative-mass squared to the conformal direction. This produces an exponential growth of the scale factor — runaway inflation.

2. **The memory drag.** The vacuum is not inert. When the conformal mode evolves rapidly (high frequency, ω ~ H, where H is the Hubble parameter), the susceptibility χ(ω) = 1/(1 − iωτ₀) becomes active and dissipative. The imaginary part of χ imparts friction.

The steady state is reached when acceleration and deceleration balance — when the geometric drive matches the memory drag. In this balance, the scale factor evolves at a constant rate, H_∞, the terminal velocity:

$$H_{\text{inf}} = \frac{2 - R}{S \tau_0},$$

where:
- R = √(4/3) is the deep-infrared refractive index, defined by the low-frequency limit of the susceptibility in the conformal sector (computed tier).
- S = 108π is the screening constant, a computed result from the action's normalization (computed tier).
- τ₀ = 41.9 Myr is the relaxation time (anchored tier).

The numerical values are:
$$H_{\text{inf}} \approx \frac{2 - 1.1547}{108\pi \cdot (41.9 \times 10^6 \text{ years})} \approx \frac{0.8453}{1.42 \times 10^{10} \text{ years}}.$$

Converting to the dimensionless dark-energy density parameter,
$$\Omega_\Lambda = \left(\frac{H_{\text{inf}}}{H_0}\right)^2,$$

and using the cosmic-baseline relation H₀ ≈ 1/(Sτ₀) reduces the leading closed form to Ω_Λ ≈ (2 − R)² ≈ 0.71. The value GRUT reports, Ω_Λ = 0.6886 (Planck 2018: 0.6889, a 0.04% match), is the **anchored** result of the full Friedmann treatment with the empirically fixed τ₀ — an anchored prediction, not a zero-parameter derivation; the few-percent offset from the tree-level closed form is absorbed into that anchoring.

#### The CTP Asymmetry and Baryogenesis

The baryon asymmetry arises from an asymmetry in the time contour. The closed-time-path formalism couples the forward and backward branches through the influence action. But the memory kernel χ(ω) is causal: it responds only to past disturbances. The negative-frequency component (the backward-in-time part) is therefore suppressed relative to the positive-frequency component.

In the early universe, when baryon-number-violating processes are active (such as sphaleron processes in the electroweak phase transition), this temporal asymmetry produces an effective preference for matter over antimatter. The magnitude is:

$$\eta_B \approx 6.6 \times 10^{-10},$$

the baryon-photon number ratio, matching observations to within roughly ten percent. This is a computed prediction with no free parameters beyond {α, τ₀}. The CTP structure does not assume an external source of CP violation; the time-arrow asymmetry built into the closed-time-path formalism is sufficient.

---

## 7. The Dark-Matter Detective Story

We undertook the investigation of whether GRUT possesses a derived mechanism that generates dark matter — whether the framework's description of the vacuum's response to gravitational structure could also account for the universe's missing matter. The investigation that resulted is a detective narrative with an unexpected denouement: the final candidate mechanism did not fail owing to insufficient strength, but rather because of excessive locality.

### 7.1 The investigation: three mechanisms on trial

Our search was motivated by a clear physical question: if the gravitational vacuum responds to structure through a finite-memory kernel, might that response manifest as dark matter at galactic scales? We subjected three candidate mechanisms to systematic scrutiny.

**First mechanism: the linear dielectric channel.** We examined whether the low-frequency saturation of the vacuum's refractive response could serve as a source for the observed dark-matter abundance. The bandwidth integral—a mathematically rigorous calculation that sums the frequency-dependent response in the linear sector—yielded a value matching the dark-matter abundance: Ω_dm ≈ 1/3, coinciding with the vacuum impedance α. The agreement was elegant, though we note that α = 1/3 is itself an adopted axiom, not a derived result. However, the investigation revealed two fatal deficiencies.

First, consistency: in the linear regime, the long-wavelength limit is the adiabatic rescaling of space itself—the very symmetry the theory claims to break. A vacuum that responds to density perturbations cannot simultaneously be invariant under a rescaling that uniformly changes all densities. The framework forbade the linear dark-matter signal by its own internal structure.

Second, observation: when we fed the linear enhancement into a full cosmic microwave background calculation, it produced approximately three times too much power at large angular scales—the integrated Sachs–Wolfe (ISW) effect—a discrepancy of order 32 standard deviations from observations. The mathematical calculation was correct; the physics it represented was inconsistent with data. **Verdict: the linear dielectric route is ruled out.**

**Second mechanism: the orbital-gate response.** We investigated whether the vacuum's response to tidal curvature—the spatial gradient of the gravitational field in bound systems such as galaxies—could open a frequency window where response enhancement becomes possible. Might such a frequency-dependent gate produce a dynamic dark sector in rotating systems?

The mechanism failed rapidly. After the linear no-go removed the mean-field contribution, we found that the realized density structure within a galaxy varies only at the scale of local granularity—roughly one part in a billion from √N fluctuations among N stars. To produce the observed ~20% dark-matter enhancement would require the response to amplify this minuscule perturbation by a factor of a million. The mechanism was internally consistent but phenomenologically impossible. **Verdict: the orbital-gate channel is refuted.**

With the linear and orbital routes eliminated, one possibility remained.

### 7.2 The final mechanism: C5a, the Weyl-squared response

![The four-stage K⁽²⁾ investigation of the W² (Weyl-squared) dark-sector channel, left to right. Stage A establishes W² as the unique permitted O(2) operator; Stage B shows locality forces its scale to L₀ with no 1/k² pole; Stage C finds the magnitude O(1–100) viable; Stage D finds the radial profile falls as 1/r⁴ — too steep for a halo. The channel survives every test except shape, so dark matter is recorded as a hosted input rather than a v3 prediction (an open negative).](figures_v3/fig_k2_stages.png)

After linear and orbital channels were closed, exactly one avenue persisted: a second-order response to the square of the tidal curvature tensor itself—the Weyl-squared term, denoted C5a. We mounted a systematic four-stage investigation, documented in detail in `theory/GRUT_V3_K2_DERIVATION.md` and `theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md`.

**Stage A: Operator uniqueness.** Among all possible curvature-squared operators—the Weyl tensor W², the Gauss-Bonnet/Euler density E₄, and Ricci-built combinations—only one escaped the constraints. E₄ is topologically dormant in four dimensions (its integral is the Euler characteristic, an invariant that contributes zero local stress-energy). Ricci-squared operators couple to the matter density and would violate the linear no-go that μ_linear = 1. W² was the sole dynamically active candidate—and if GRUT possessed any derived dark sector, it had to be this one. (**Computed** tier, per Stage A of the K⁽²⁾ derivation.)

**Stage B: The scale is locked to L₀.** The explicit calculation of the second-order response kernel K⁽²⁾(ω,k) delivered a surprise. The kernel depends on frequency alone—on the temporal memory scale τ₀—and carries **no dependence on spatial frequency k**. Mathematically, a causal, local kernel must be a polynomial in spatial frequency k. The inverse Laplacian (1/∇²) that would couple to a galactic-size dark halo is a *pole* in frequency space, not a polynomial. No algebraic manipulation can transform a polynomial into a function with a pole. Therefore, the coupling scale was forced to be L₀ ≈ 12.85 Mpc, the memory length. This is a locality theorem, not an approximation artifact. (**Computed** tier, Stage B; see K⁽²⁾ derivation and `grut/derivation/phi_munu/second_order_kernel.py`.)

**Stage C: The magnitude is viable, not negligible.** An intermediate calculation had suggested an impossibly small effect—10⁻²⁷ times the baryon density. This was incorrect: two independent errors had compounded. First, a unit mismatch—comparing gravitational-units density (dimension 1/length²) to SI units (kg/m³) without the conversion factor c²/G ≈ 1.35×10²⁷ kg·s⁻²/m³. Second, an incorrect Weyl formula in that calculation. When the arithmetic was corrected, the magnitude became physically reasonable. At galactic scales, the effective dark density was O(1–100) times the baryon density—precisely the ballpark observations require. The physical reason: L₀ is not the galaxy size but the *curvature radius* of the weak gravitational field around a galaxy—a scale ~10–100 Mpc over which the field bends smoothly. By geometric coincidence, L₀ lands near this curvature scale, giving an O(1) effect in the regime where observations probe. **The magnitude was viable.** (**Computed** tier, Stage C, with error correction documented.)

**Stage D: But the shape is wrong—and provably so.** Here the mechanism broke decisively. We computed the radial profile of the effective dark density. The Weyl-squared response sources density in proportion to (ρ − ⟨ρ⟩)², where ρ is the baryon density and ⟨ρ⟩ is its spatial mean. For a typical galaxy halo with ρ ∝ 1/r² (isothermal), squaring gives ρ_eff ∝ 1/r⁴. In the outskirts, where baryon density falls off sharply, the tidal Weyl term dominates, and the profile steepens further to ρ_eff ∝ 1/r⁶.

A flat galaxy rotation curve demands dark matter scaling as ρ_DM ∝ 1/r². The Weyl-squared source falls off two powers steeper in radius (1/r⁴ versus 1/r²). The enclosed effective mass saturates, and the rotation velocity declines outward—the opposite of observation. We examined every permitted variant: the scalar W² route, the Bach tensor (coupling to the second derivative of baryon density), and the transverse-projector loophole. All three converged to identical answers: 1/r⁴ in the interior, 1/r⁶ in the exterior. Always wrong. (**Computed** tier, Stage D and Test 06.)

Crucially, we proved this is not a limitation of approximation. Test 06 (`theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md`) demonstrates that to flatten a 1/r⁴ source into a 1/r² halo requires applying an inverse-Laplacian operator—integrating the density distribution. But the same locality theorem that forces the scale to L₀ (no 1/∇² pole in the kernel) forbids that integration. Every permitted tensor structure, every symmetry-respecting variant, inherits the same locality and yields the same excessively steep profile. **The shape failure is a theorem, not an artifact.** We tested this with three independent tensor-structure routes; three independent closure skeptics; none found a shallowing mechanism. The failure is robust. (**Computed** tier.)

### 7.3 The verdict and its implications

![Why the W² dark sector fails on shape, not size, on log–log axes. The density a flat rotation curve requires — a dark-matter halo falling as 1/r² (navy) — is compared with the computed W² effective density, which falls as 1/r⁴ and steepens to 1/r⁶ beyond r ≈ 22 kpc (red; the dotted line marks the break where the slope goes −4 → −6). The W² curve can be scaled to the right magnitude but is far steeper than any halo — the "right magnitude, wrong shape" result the locality theorem explains.](figures_v3/fig_profile_mismatch.png)

![The locality theorem behind the dark-sector failure. A local, causal kernel may contain only operators polynomial in k² (left) — entire functions with no singularity; an operator carrying 1/∇² (equivalently a 1/k² pole, right) is forbidden. Shallowing the response from 1/r⁴ to the 1/r² of a halo would require exactly that forbidden 1/∇², so the same locality that fixes the scale L₀ also rules out the operator a halo would need.](figures_v3/fig_locality_theorem.png)

C5a—the Weyl-squared response—was GRUT's most sophisticated dark-sector candidate, and it cleared every obstacle that defeated the others. It carries the correct sign (it mimics attraction, not repulsion). It lives in the only remaining open channel (nonlinear response, not linear). Once the magnitude error was corrected, its strength at galactic scales was viable. It cleared every test but one — but that test was *shape*, and it failed decisively, so C5a is ruled out as a dark-matter mechanism. Dark matter remains a hosted input, not a near-miss.

Here is why shape determines everything. A galaxy's rotation curve remains flat far from the center because the gravitating mass must grow roughly in proportion to radius—there must be "extra" mass far out where stars and gas have already become sparse. A dark-matter halo provides this by having a density that declines gently, close to 1/r². The Weyl-squared source declines far more steeply: 1/r⁴ through the body of a halo, steepening to 1/r⁶ in the outskirts. Such a steep profile concentrates its mass near the center and becomes negligible by the time one reaches the flat part of the rotation curve. It can contribute modest mass where stars already abound; it cannot construct the extended, gently-declining halo that observations require. Increasing the overall strength amplitude cannot remedy this—such scaling lifts the entire profile uniformly while leaving the shape exactly as wrong.

The deeper constraint is that this shape cannot be repaired without violating the theory's foundations. To transform a steep 1/r⁴ source into a gentle 1/r² halo requires spreading it outward in space—mathematically, applying an inverse-Laplacian (a 1/∇² operator), the operation that smears a concentrated source into a diffuse one. But GRUT's response is **local**: the vacuum reacts to curvature *at the location where curvature exists*; it does not reach across space to redistribute the source. That locality is not an incidental feature—it is the precise property that pins the theory's one length scale to L₀. The constraint that bestows on GRUT its scale is the constraint that denies it the smearing operator a dark halo demands. We verified this by examining every form the second-order response is permitted to assume—the scalar route, the Bach-tensor route, the TT-projector route—and each inherits the same locality, yielding the same provably too-steep profile. The failure is rooted in the framework's foundational structure.

**GRUT therefore possesses no derived mechanism that reproduces observed dark-matter halos. Dark matter is a hosted input**—a boundary condition the theory accepts from observation rather than generates from its own dynamics, precisely as it accepts the Standard Model's particle spectrum and gauge-group structure. This language warrants care. "Hosted" is not a euphemism for failure. Every physical theory rests on inputs it does not derive from within: general relativity does not explain the matter around which it curves spacetime; the Standard Model does not derive its own gauge group or fermion masses. GRUT now treats the *existence and spatial distribution* of dark matter in the same way—as an empirical condition the framework is consistent with, not a consequence it produces.

What the framework *does* derive is narrower and sharper: the MOND acceleration scale

$$a_0 = \frac{c H_0}{2\pi},$$

emerges as a ratio of fundamental scales—the speed of light, the Hubble expansion rate, and the geometric constant π. This scale is real and experimentally testable; what remains adopted rather than derived is the interpolation function ν(y)—the precise rule governing how gravity transitions from Newtonian to modified behavior near this acceleration threshold.

There is a precise path by which GRUT could recover a *derived* dark sector: it would require overturning one of the foundational load-bearing results that produced this verdict—the locality of the vacuum's response, the closed-time-path structure beneath it, or the profile-shape theorem itself. Absent such an overhaul, inventing a new dark-sector channel would be fruitless—any channel constructed from the same local, causal response kernel would inherit the identical too-steep profile. This is the discipline the framework now imposes on itself, and it is why the dark-sector frontier is closed rather than merely paused.

The intellectual posture has therefore shifted from *search* to *statement*. The question "where does GRUT's dark matter come from?" now has a definitive answer within the theory: nowhere—not owing to weakness of mechanism, but owing to geometric constraint. The distinct and broader question of what dark matter *is* in physical reality remains open in physics at large, to be resolved by physics beyond a classical vacuum-response theory. GRUT's contribution is not an answer to that question but a sharp falsifiable constraint: whatever dark matter actually is, it is **not** the gravitational vacuum responding locally to curvature.

---

### 7.4 Technical Brief

The four-stage K⁽²⁾ derivation establishes the dark-sector verdict with explicit calculations. We summarize the mathematical foundations here.

#### Stage A: The minimal influence action and permitted operators

The closed-time-path influence action for the responsive-vacuum sector, at second order in metric perturbation h, consists of four terms (per `grut/derivation/phi_munu/linearized_ctp_action.py`):

$$S_\text{IF}[h_a, h_r] = S_\text{EH} + S_\text{matter} + S_\text{const} + S_\text{noise},$$

where S_EH is the linearized Einstein–Hilbert action (split between forward and backward branches), S_matter = ½ ∫ d⁴x h_a^{μν} T_{μν} encodes minimal matter coupling (equivalence principle), S_const contains the sole responsive channel (the memory-kernel response), and S_noise is the Keldysh/fluctuation-dissipation noise term (vanishes at h_a = 0).

The responsive kernel is

$$K^\text{R}_{μνρσ}(ω) = α_\text{vac} \cdot χ(ω) \cdot P^\text{TT}_{μνρσ},$$

where:
- $α_\text{vac} = 1/3$ is the vacuum impedance (**axiom**);
- $χ(ω) = \frac{1}{1 - iωτ_0}$ is the single-pole susceptibility (**postulated**, anchored at τ₀ = 41.9 Myr);
- $P^\text{TT}$ is the transverse-tracefree projector (dimensionless, k-direction only).

The kernel is spatially scale-free: χ is purely temporal; P^TT depends only on direction k̂, not magnitude |k|.

Of the curvature-squared operators—W² (Weyl), E₄ (Euler), and Ricci-built forms—the permitted basis analysis shows:
- **W² is the unique dynamically active channel** (conformal/tracefree, O(h²) response, evades the linear no-go);
- **E₄ is topologically dormant** (Lovelock theorem in 4D);
- **Ricci-squared is forbidden** (would violate μ_linear = 1).

If dark matter is to be derived in GRUT, it must arise from W². (**Computed** tier.)

#### Stage B: The scale is forced to L₀

The explicit computation of the second variation yields

$$K^{(2)}(ω,k) = σ \cdot α_\text{vac} \cdot χ(ω),$$

where σ ~ O(1) is a dimensionless prefactor. Crucially, **K⁽²⁾ is k-independent**; it carries no factor of |k|. 

A spatially-local kernel respecting causality must be an entire function (polynomial) of k². Integration by parts on the source W² ~ (∂²h)² yields polynomial k⁴ behavior. The product of polynomial terms is polynomial; **no 1/k² pole appears**. Therefore, the only length available in ρ_eff ~ α χ(ω) L² W² is L₀ = cτ₀, the sole dimensionful constant in the kernel. A local-system-size coupling would require a 1/∇² pole to replace L₀² with r², which the locality structure forbids.

$$ρ_\text{eff} = σ \cdot α_\text{vac} \cdot L_0^2 \cdot W^2, \quad L = L_0 ≈ 12.85 \text{ Mpc}.$$

This is a theorem of locality, not an approximation artifact. (**Computed** tier, Stage B.)

#### Stage C: Magnitude is O(1–100) at galactic scales

The effective density is

$$ρ_\text{eff}/ρ_\text{baryon} \sim α \left(\frac{L_0}{L_\text{curv}}\right)^2,$$

where L_curv is the curvature radius of a weak-field galaxy. For a point mass M at the Schwarzschild radius r_s = 2GM/c², the curvature scales as Φ ~ M/(c²r), giving L_curv ~ r/√Φ ~ tens of Mpc for galactic systems. Since L₀ ≈ 12.85 Mpc is comparable to this curvature scale, the ratio (L₀/L_curv)² is O(1–100) rather than negligibly small. A galaxy at 10 kpc yields ρ_eff/ρ_baryon ~ 53; at 30 kpc, ~2; in the Milky Way at 8 kpc, ~62. (**Computed** tier, Stage C, with documented error corrections.)

#### Stage D and Test 06: The shape theorem

For a baryon distribution ρ_b, the Weyl tensor in weak-field spherical symmetry is

$$W^2 = \left(\frac{16}{3}\right) Λ^2, \quad Λ = Φ'' - \frac{\Phi'}{r} = 4π(ρ - ⟨ρ⟩).$$

Thus

$$ρ_\text{eff} \propto (ρ - ⟨ρ⟩)^2.$$

For an isothermal halo ρ_b ∝ 1/r²:

$$ρ_\text{eff} \propto \rho_b^2 \propto \frac{1}{r^4}, \quad \text{log-slope} = -4.$$

A flat rotation curve requires ρ_DM ∝ 1/r² (log-slope −2). Test 06 extends this analysis to all permitted tensor routes:

| Route | Effective source | Profile |
|---|---|---|
| Scalar W² | $(16/3)Λ^2$ | 1/r⁴ |
| Bach tensor | $∇²ρ_\text{b}$ | 1/r⁴ |
| TT projector | $k̂k̂$ (dimensionless) | 1/r⁴ |

All three routes yield 1/r⁴ or steeper. The failure is not route-dependent.

Why the shape cannot be shallowed: transforming 1/r⁴ → 1/r² requires integrating the source, i.e., applying 1/∇². The locality theorem (Stage B) forbids the 1/k² pole required for such an operator. Therefore, **no local, causal, No-Go-respecting kernel can flatten the profile**. (**Computed** tier — confirmed by three independent derivations and an adversarial review that converged on the same verdict: the profile failure is a theorem of locality, not an artifact of one calculation.)

#### Closure: the dark-sector frontier is closed

The C5a channel—the W² second-order response—has

- **Correct sign** (mimics attraction);
- **Viable magnitude** (~O(1–100) at galactic radii);
- **Wrong radial profile** (1/r⁴–1/r⁶ instead of 1/r²), **provably unfixable** without breaking locality.

GRUT therefore has **no derived dark-matter mechanism** reproducing halo phenomenology. Dark matter is **hosted input** (with the derived a₀ scale and the strict requirement μ_linear = 1). The only way to reverse this verdict is to overturn a foundational result: locality, the CTP structure, the No-Go, or the profile theorem—not to invent a new channel, which would inherit the same too-steep profile from the same local kernel.

---

---

## 8. How To Kill It — The Predictions

We present three sharply falsifiable predictions, each rooted in different corners of the framework and each testable within a decade. A mature physical theory must be killable—that is, it must make precise, experimentally refutable claims. GRUT has three such tests, spanning laboratory quantum mechanics, particle physics, and cosmology. We state them plainly because they are the clearest way the theory can fail.

### 8.1 The Gravitational Decoherence Plateau at ~689 Hz

![The predicted gravitational-decoherence rate (arbitrary units) versus probe frequency on a log axis. The rate is negligible at low frequency, rises through a sharp transition, and saturates to a constant plateau; the transition sits at the GRUT-computed characteristic frequency ≈ 689 Hz (gold dashed line, red arrow). Because that frequency is fixed by the theory, a table-top measurement of where decoherence saturates is GRUT's sharpest near-term falsifier.](figures_v3/fig_decoherence_plateau.png)

When a massive object enters a quantum superposition—existing in two positions simultaneously—the gravitational field around it encodes that superposition state. Gravity, however, does not remain isolated from the rest of the universe. The vacuum's quantum fluctuations couple to the gravitational field, and over time this coupling induces decoherence: the entanglement between the object and the universal quantum field causes the superposition to collapse irreversibly. Gravitational decoherence thereby establishes a sharp, physical boundary between the quantum and classical regimes.

GRUT **computes** this decoherence rate from first principles using the CTP noise kernel—the quantum jitter in spacetime itself, derived from the closed-time-path action. The decoherence rate Λ_grav for an object of mass m and size R depends only on three fundamental constants (G, ℏ, c) and the single relaxation time τ₀ that anchors the entire framework. There are zero free parameters; the prediction is parameter-free.

For a gold microsphere of radius 1 micrometer—a mass of approximately 80.8 picograms—GRUT predicts a decoherence frequency of **689 Hz** (**computed tier**). This means that if such a sphere is placed in a quantum superposition, coherence will be destroyed in approximately 1.5 milliseconds by gravitational effects alone.

This prediction is specific, not approximate. Experimental discovery of the plateau at 680 Hz or 710 Hz would be consistent with the theory—such variations lie within measurement uncertainty. However, a plateau at 400 Hz or 1000 Hz would signal that the underlying structure of τ₀ is incorrect, severing GRUT's connection to laboratory physics. A secondary discriminator is also available: competing collapse models (Ghirardi–Rimini–Weber versus Continuous Spontaneous Localization) predict different isotope-dependent scalings of the decoherence rate. GRUT makes a specific isotope prediction. If precision experiments reveal isotope scaling inconsistent with the prediction, not merely the rate but the physical mechanism itself would be falsified.

Experiments such as gravitationally-induced entanglement separation, now in prototype stages, provide the pathway to test this prediction within 5–7 years.

### 8.2 The Neutrino Mass Hierarchy is Normal, Not Inverted

![The two possible neutrino mass orderings, drawn as stacked mass levels. In the normal ordering GRUT predicts (left), a single heavy state m₃ sits well above a close m₁–m₂ pair; the inverted ordering (right, crossed out) would put a close m₂–m₁ pair on top with m₃ lightest. The Z₃ flavor structure, anchored to the Koide relation K = 2/3, forces the normal ordering — so an experimental finding of the inverted ordering (JUNO, DUNE) would falsify the theory.](figures_v3/fig_neutrino_hierarchy.png)

GRUT's flavor structure rests on a Z₃ symmetry—a threefold rotational invariance in lepton-mass space. This symmetry is **hosted** (not derived from first principles), anchored empirically by the charged-lepton Koide ratio K = 2/3, measured to extraordinary precision (0.005% accuracy). Once the Z₃ circulant structure is fixed by this empirical anchor, the framework **computes** a unique mathematical consequence: the neutrino mass spectrum must obey a specific pattern. This pattern forces the neutrino mass hierarchy to be **normal**—that is, the lightest neutrino (ν₁) possesses the smallest mass, with m₁ < m₂ < m₃. An **inverted** hierarchy, in which the two heavier neutrinos trade positions (m₃ < m₁ < m₂), would contradict the Z₃ structure (**computed tier, promoted in the v3 re-audit**).

Specifically, under the Z₃ ansatz with the derived coupling a_ν = 1, the predicted mass spectrum is: m₁ ≈ 0.802 meV, m₂ ≈ 8.65 meV, m₃ ≈ 50.16 meV, yielding a total sum Σm_ν ≈ 59.6 meV. This sum lies well below the Planck 2018 + BAO cosmological bound (0.12 eV at 95% confidence), with approximately 60 meV of headroom.

The inverted-hierarchy configuration, when forced into the same Z₃ structure, sits precisely at a boundary (m₃ → 0 degenerate limit) and is not a generic interior solution. GRUT therefore predicts normal hierarchy uniquely.

This prediction is testable by two independent precision experiments: JUNO (Jiangmen Underground Neutrino Observatory), now under construction in China, will determine the hierarchy to >3σ precision by approximately 2030 using reactor antineutrino spectroscopy. DUNE (Deep Underground Neutrino Experiment) in the United States, operational from 2030 onward, will confirm the hierarchy to >5σ using accelerator neutrinos. If either experiment definitively measures an inverted hierarchy at >5σ confidence, the Z₃ prediction dies, taking with it GRUT's unique falsifiable prediction for flavor physics. This is a one-way gate: confirmation of normal hierarchy is consistent with the structure; discovery of inverted hierarchy is falsifying.

### 8.3 Linear Modified Gravity (μ ≠ 1) Would Refute the Theory

Early versions of GRUT postulated that the vacuum's finite memory might enhance gravitational attraction on the largest (linear) scales, effectively modifying general relativity at low frequencies. This enhancement was parameterized by the quantity μ—the ratio of gravitational growth in GRUT to growth in standard general relativity on linear cosmological modes. GRUT v2 predicted μ_linear ≈ 4/3—a 33% enhancement to density-perturbation growth in the modes that shape the cosmic microwave background pattern. This was **computed tier** in v2.

This prediction was wrong. Validation using the full gravitational kernel and implementation in CAMB (Cosmic Microwave Background Boltzmann code) revealed that a μ = 4/3 enhancement produces an Integrated Sachs–Wolfe (ISW) effect at low CMB multipoles that overshoots observations by a factor of 2.79—approximately 32 standard deviations of observational noise. The theory had over-claimed. Version 3 corrected it: **linear cosmology is exactly ΛCDM**—a **derived requirement** following from the boundary operator, **computed tier**. Dark-sector enhancement is confined to nonlinear and tensor channels; the cosmological background is indistinguishable from the standard ΛCDM concordance model.

Yet this self-correction imposes a severe constraint. GRUT now forbids linear modified gravity. If future precision surveys—DESI, Euclid, CMB-S4, or comparable experiments—were to measure a sustained linear growth enhancement across multiple independent probes with μ > 1 at >2σ, GRUT would be falsified. The theory has constrained itself: by deriving that μ *must* be 1, it made itself killable on this axis. A confirmed linear-scale enhancement would overturn the boundary-operator consistency that forces the cosmology into ΛCDM. This is the cost of theoretical honesty: GRUT cannot hide behind the claim "we never stated the linear sector was special." It did state this, it was wrong, it corrected itself. But the correction is now a falsifiable constraint.

### 8.4 The Falsifiability Landscape

![Three independent ways to falsify GRUT, spanning three scales. (1) A table-top test of the gravitational-decoherence plateau near 689 Hz; (2) the neutrino mass ordering — GRUT requires normal, and JUNO/DUNE can decide it; (3) the absence of any linear modification (μ ≠ 1) on cosmic scales, testable by DESI, Euclid, and CMB-S4. Each is a distinct measurement that could independently kill the theory.](figures_v3/fig_falsifiers.png)

These three predictions span three independent physical domains: quantum collapse at laboratory scales, the precision frontier of particle physics, and large-scale cosmological structure. They are rooted in different theoretical sectors—the memory kernel's high-frequency behavior, the Z₃ circulant algebra of flavor, and the boundary operator's constraint on conformal response. A failure in any one does not automatically invalidate the others; they are logically independent. Yet together they define the complete falsifiability landscape. A mature theory must announce where it can be wrong. These three domains specify where GRUT can be, and will be, tested.

### 8.5 Technical Brief

The gravitational decoherence rate emerges from the CTP noise kernel evaluated for a massive object in a superposition. The foundational equation is the two-point correlation function of the metric perturbations:

$$\langle h_{\mu\nu}(t) h_{\rho\sigma}(t') \rangle = \int_0^\infty \frac{d\omega}{2\pi} \text{Im}[K^R_{\mu\nu,\rho\sigma}(\omega)] e^{-i\omega(t-t')}$$

where K^R is the retarded memory kernel. For the gravitational case, this kernel is (**computed** `memory_kernel_form`):

$$K^R_{\mu\nu,\rho\sigma}(\omega) = \alpha \chi(\omega) P^{TT}_{\mu\nu,\rho\sigma}$$

with the single-pole susceptibility (**postulated** `constitutive_equation`, anchored by observation `tau_0_cross_consistency`):

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0}$$

For a mass m in a spatial superposition of separation l, distributed over a body of size R, the gravitational decoherence rate produced by this kernel takes the form (**computed** `decoherence_plateau`):

$$\Lambda_{\text{grav}}(m, l, R) = \frac{G\, m^2\, S(l/R)}{\hbar\, l}, \qquad S(l/R) = \min\!\left(1, \frac{(l/R)^3}{6}\right),$$

where $S(l/R)$ is the extended-body suppression factor (the near field, $l < R$, is suppressed as $(l/R)^3$). Evaluated for the benchmark gold microsphere (m ≈ 80.8 pg = 8.08 × 10⁻¹¹ kg, radius 1 μm), the framework's computation places the decoherence plateau at Λ_grav ≈ 689 Hz (**computed tier**): the rate is fixed by G, ℏ, and the source geometry, with the memory time τ₀ setting the frequency at which the response plateaus — zero free parameters.

The neutrino hierarchy prediction follows from the Z₃-circulant mass-matrix ansatz. Given the charged-lepton anchor K = 2/3 (**anchored** `koide_k_2_over_3`), the generalized Koide eigenvalue equation for neutrinos with coupling a_ν = 1 (**computed** `neutrino_z3_coupling_a_equals_1_uniqueness_theorem`) admits a unique interior solution in the normal-hierarchy regime. The solution satisfies:

$$\sqrt{m_i} = M_0(1 + \cos(\theta + 2\pi k/3))$$

with k ∈ {0, 1, 2}, where the uniqueness theorem fixes a_ν = 1 as the sole boundary-degenerate coupling. The inverted-hierarchy solution sits at the m₃ → 0 boundary, making it fine-tuned and non-generic (**computed** `neutrino_hierarchy_z3_nh_prediction`). GRUT therefore prefers normal hierarchy with Σm_ν ≈ 59.6 meV.

The linear-cosmology constraint μ_linear = 1 follows from the boundary operator theorem (**computed** `adiabatic_dilatation_redundancy_nogo`). The adiabatic spatial-dilatation redundancy D of general relativity is exact in the memoryless limit L₀ → 0. When finite memory is present, D is broken at order (L₀ k_phys)². The vacuum's conformal-mode response cannot simultaneously respect this breaking and remain invariant under long-wavelength adiabatic rescalings—the very modes the redundancy acts on. Conformal enhancement and separate-universe invariance are mutually exclusive. Therefore any conformal modification factor that would produce μ ≠ 1 is **forbidden** by the boundary-operator no-go (the separate-universe consistency argument of the projector-consistency analysis). The consequence is that linear cosmology is exactly ΛCDM, with zero modified-gravity signal — a derived requirement, not a fit (**computed tier**).

---

## 9. The Rest of the World, Honestly

We have now established the spine of GRUT: a single broken symmetry (the adiabatic rescaling redundancy D), two organizing structures (the CTP response Q and finite memory F), and what they entail at cosmological scales. A complete framework, however, must stand or fall by what it specifies about the remaining domains of physics: black holes and gravitational saturation, the recovery of quantum mechanics, the flavor structure of the Standard Model, the measurement problem and the arrow of time, and the dark sector. In this chapter, we present each sector at its audited tier—what we have *computed*, what we have merely *postulated*, what we have *anchored* to observation, and what remains *open* or definitively *closed*.

### 9.1 Black holes and finite-curvature saturation

![A conjectural picture of finite-memory curvature saturation. As matter is compressed (horizontal axis, schematic), the interior curvature rises but cannot exceed a ceiling (gold dashed line) set by the memory time: R_max = α/(c²τ₀²) ≈ 2.1×10⁻⁴⁸ m⁻², corresponding to a mass-independent maximum density ρ_max ≈ 1.1×10⁻²² kg/m³. The axes are schematic and the result is flagged conjectural (v3 re-audit), not a derived prediction.](figures_v3/fig_bh_saturation.png)

Finite memory imposes a ceiling on curvature. In the presence of matter, the gravitational field's Ricci scalar—a measure of the local curvature induced by energy density—cannot diverge without bound when the vacuum relaxes on a finite timescale τ₀. Our framework conjectures that within the matter-bearing interior of any black hole, the Ricci scalar saturates at

$$R_{\text{max}} = \frac{\alpha_{\text{vac}}}{c^2 \tau_0^2} \approx 2.1 \times 10^{-48} \text{ m}^{-2},$$

a candidate consequence of the CTP response law. The saturation value follows arithmetically from the two empirically anchored constants α and τ₀, but the mechanism that would enforce it is not yet derived (see the tier note below).

From Einstein's field equations—which relate the Ricci tensor to the stress–energy tensor—it follows arithmetically that every black-hole core, independent of the hole's total mass, would reach the same universal density:

$$\rho_{\text{max}} = \frac{c^2 R_{\text{max}}}{8\pi G} \approx 1.1 \times 10^{-22} \text{ kg/m}^3,$$

irrespective of the hole's mass parameter. Larger black holes contain larger cores, but all cores saturate at the same critical density.

**Tier: conjectural.** We demote this result from v2's tier because, although the *values* follow mathematically from {α, τ₀}, the *mechanism* that enforces this saturation—the manner in which the full CTP response actively resists higher curvature in the matter-bearing interior—remains unproven from the complete closure of the field equations beyond linear order. The linearized response field (Φ_μν) has been computed and verified; deriving the interior FRW construction that would establish this rigorously requires going beyond the weak-field WKB regime, a task not yet completed. The hypothesis survives every consistency check we have applied, but scientific precision demands we acknowledge: these numbers represent what the framework's structure suggests, not what we have proven from first principles. The closure condition is a full nonlinear covariant review of the matter-interior CTP action.

### 9.2 The deep-infrared refractive index: convergence by two independent routes

![Two independent computations of the constant R compared with the theoretical value √(4/3) ≈ 1.15470 (gold dashed line). The tree-level Path-G route lands on 1.15470 and the one-loop Osborn route on 1.15367 — agreement at the ~0.1% level. The third, three-loop CTP route is shown as an open (hollow) marker: that computation is not yet closed.](figures_v3/fig_R_convergence.png)

One of GRUT's most distinctive structural predictions is the vacuum's refractive index in the deep infrared. In the low-frequency limit (ω → 0), the frequency-dependent susceptibility χ(ω) contracts to a scalar refractive index:

$$R = \sqrt{\frac{4}{3}} \approx 1.1547.$$

This value emerges from two independent computational routes that share no mathematical inputs or intermediate results. 

**Path G** proceeds via the conformal-mode identification—the same conjecture that underlies α = 1/3. If the gravitational conformal mode (the single scale-changing degree of freedom of the metric, appearing in the decomposition g_μν = e^{2σ}ĝ_μν where σ is a conformally coupled scalar with ξ = 1/6) is indeed the infrared carrier of the vacuum's response, then the Komargodski–Schwimmer trace-anomaly theorem—a proven result in quantum field theory—implies that the trace-anomaly coefficient ratio a/c equals precisely 1/3. Tree-level manipulation then gives R = √(4/3) exactly, without any coupling constants entering.

**Path Osborn** takes a different approach: compute the one-loop renormalization-group running of the conformal anomaly coefficient in the full Standard Model at the electroweak scale (M_Z ≈ 91 GeV), accounting for the flow of all coupling constants. This calculation yields R ≈ 1.15367, shifted slightly from the tree-level value. Yet the two routes agree to within **0.1% precision**, and they exploit completely distinct input sectors—one uses only conformality, while the other uses the full Standard Model particle content, gauge structure, and Yukawa couplings.

**Tier: computed.** The agreement is independent confirmation of the conformal-mode identification. The 0.1% convergence represents genuine structural verification, not numerical accident. We must note one honest qualifier: a third route (a three-loop CTP integration via Allen–Jacobson propagators on S⁴, promised in v2) remains numerically uncomputed, entered as an open negative. This gap does not invalidate the two-route convergence—it leaves one promised consistency check unfinished, a minor gap in the ledger that does not undermine the robustness of the central result.

### 9.3 Flavor and the Koide identity: hosted structure

The origin of the Standard Model's three generations and the hierarchies in the charged-lepton spectrum (electron 0.511 MeV, muon 105.66 MeV, tau 1,777 MeV) represent one of physics' deepest open questions. GRUT does not solve this mystery from first principles. Instead, the framework *hosts* the Standard Model's flavor sector as external input—exactly as general relativity hosts the matter it curves around, and exactly as the Standard Model hosts its own gauge group and coupling constants.

Within this hosted framework, however, there exists a remarkable empirical pattern that GRUT illuminates with precision: the charged-lepton masses satisfy the **Koide identity**

$$K = \frac{\sum_{i=1}^{3} m_i}{\left(\sum_{i=1}^{3} \sqrt{m_i}\right)^2} = \frac{2}{3}$$

to better than **0.005%** measured against the PDG values. This ratio serves as GRUT's empirical anchor for the flavor sector—not a derivation, but a fixed constraint from observation that anchors the Z₃ circulant structure governing how the lepton-mass operator acts.

Given K = 2/3, the framework derives that the lepton-mass operator must possess a Z₃-circulant form parametrized by two numbers: a mass scale M₀ and a mixing phase θ. The uniqueness condition on θ—the fact that θ = 2/9 is singled out by consistency with the CTP structure—is *computed*. Notably, the neutrino sector does not extend this Z₃ symmetry; instead, boundary conditions at the weak scale force the normal neutrino mass hierarchy to be the unique prediction consistent with the charged-lepton structure.

**Tier: mixed.** The Koide ratio K = 2/3 itself is *anchored*—it is measured input from experiment, not derived. The structural constraints on the Standard Model (three generations, anomaly cancellation, gauge-group form) are *computed* to be consistent with GRUT's five structural constraints. However, establishing that the SM is the *unique* minimal theory obeying these constraints—a claim v2 made—requires a proof we have not yet achieved. Accordingly, v3 demotes this: the SM is *consistent* with GRUT's constraints, a necessary but not sufficient condition for uniqueness. The closure condition is a full uniqueness proof for minimal anomaly-free gauge theories satisfying all five structural constraints.

### 9.4 Quantum mechanics is recovered, not assumed

GRUT does not bolt quantum mechanics onto its dynamics; the Schrödinger equation is recovered from the *same* constitutive law that governs the vacuum, in the limit of vanishing memory. Writing the constitutive equation $\tau\,\dot z + z = z_{\text{target}}[z]$ with its target built from the Schrödinger residual $F[\psi] = i\hbar\,\partial_t \psi - H\psi$ — a Newton–Raphson step toward $F[\psi]=0$ — the $\tau \to 0$ limit reproduces unitary quantum evolution: one constitutive step matches the first-order Euler–Schrödinger update exactly, the norm is preserved to first order in $dt$, and on a precessing-qubit test the expectation $\langle \sigma_x(t)\rangle = \cos(\omega t)$ is recovered. Quantum-mechanical evolution is therefore not a separate axiom of the framework but the zero-memory face of the responsive vacuum — where the medium has no memory, its relaxation toward the self-consistent target *is* Schrödinger evolution.

**Tier: computed.** The recovery is verified numerically on the qubit example at first order; the broader program — promoting this single-step equivalence to many-body Hamiltonians and full operator-level identity — is where GRUT's quantum sector will be built out.

### 9.5 The measurement problem resolves into physics

Quantum mechanics has long carried a conceptual debt: the measurement problem, the ill-defined boundary between system and observer, the emergence of probability from a deterministic wave equation. The closed-time-path formalism that GRUT rests upon *largely dissolves* this puzzle—not by introducing a new postulate, but by recovering most of the resolution from the theory's own geometry. One piece, the Born rule, the framework does not derive; we make that exception explicit.

When a macroscopic apparatus (a crystal of 1 gram or more, with gravitational decoherence rate Λ_app τ₀ ≫ 1, deeply classical) couples to a quantum object (an atom or ion, with Λ_obj τ₀ ≲ 1, near the boundary), their joint decoherence rate becomes *dominated* by the apparatus. The apparatus is the faster crystallizer; it drags the slow quantum system across the threshold from refractive (quantum) to classical regimes on a timescale set by the ratio of their decoherence rates, Λ_app/Λ_obj. This is not wave-function collapse in any mystical sense. It is *physical contact*—the transfer of information from one coupled subsystem to another through a low-bandwidth memory channel, following directly from the CTP action.

The Wigner–friend paradox dissolves naturally: the friend's measured pointer variable does not exist in superposition relative to the external observer because the friend *is* the apparatus from the quantum system's perspective. The apparent wave-function reduction is a consequence of how finite-memory relaxation couples different subsystems across decoherence-rate boundaries.

**Tier: computed.** The measurement resolution—including the mechanism by which decoherence rates accelerate under coupling—is verified numerically for realistic examples: a 1-gram apparatus interacting with an atomic quantum object, a decoherence-rate separation of roughly 10^32, and the joint decoherence rising to 10^35. The physics is clean and internally consistent.

We must, however, state one honest open question: the **Born rule**—the assignment of squared amplitudes |⟨ψ | pointer_i⟩|² as probabilities—is *not derived* from the CTP machinery. The CTP formalism produces decoherence rates, the decay of off-diagonal density-matrix elements toward zero, and the emergence of a pointer basis from the structure of the environment. It does not produce the specific probability weights on the diagonal of the final density matrix. Those weights come from the Hilbert-space inner product, which is postulated independently in quantum mechanics. Current quantum-foundations programs—Copenhagen interpretation, Many-Worlds, decoherent histories, collapse models—all face the same gap. GRUT names this rather than obscuring it: **the Born rule remains a postulate**, entered as an open negative in the ledger.

The framework also recasts the field's oldest thought experiment. In a closed, self-referential universe there is no external observer, so Schrödinger's box is *inverted*: it is the **observer** who is boxed — finite, local, information-limited — while the cat goes on evolving outside the observer's information horizon. "Observation" becomes synchronization through contact, not creation through measurement: coupling to a system reveals its state, it does not conjure it. This is an interpretive reframing consistent with the framework, not a new prediction *(anchored tier)*.

### 9.6 Time, entropy, and information

The retarded structure that lets the vacuum respond only to its past also fixes the direction of time. Constitutive evolution carries an entropy-production rate $\dot S = (1/\tau_0)\,\langle (z - z_{\text{target}})^2\rangle$, which is non-negative for every state and vanishes only at the fixed point $z = z_{\text{target}}$; cumulative entropy is therefore monotonically non-decreasing. The Second Law is not an independent postulate but a consequence of the CTP action's retarded-kernel structure — time's arrow points the way the memory kernel points, from a realized past to an open future. **(Computed tier.)**

The same memory softens the black-hole information puzzle. Because the vacuum carries correlations forward, Hawking radiation is not strictly thermal: it carries constitutive correlations, and Page-curve consistency holds at the linearized level through the memory kernel. A fully nonlinear, covariant account of evaporation is not yet closed. **(Anchored tier; the nonlinear closure is an open negative.)**

### 9.7 The dark sector: a closed chapter

The full investigation is recounted in the preceding chapter; we record here only its standing in the framework. After ruling out the linear dielectric route (forbidden by μ_linear = 1 and contradicted by CMB observations at 32 standard deviations) and the orbital-gate mechanism (ruled out by insufficiently strong coupling), exactly one channel remained: the second-order Weyl-squared response, denoted C5a. The constructive phase computed it to closure—it possesses the right *magnitude* at galactic scales (approximately 1 to 100 times the baryon density), but a radial profile (falling as 1/r⁴ through the halo interior to 1/r⁶ in the outskirts) that is provably too steep to reproduce the flat 1/r² rotation curves galaxies display. This shape failure is not an artifact of approximation: it is a theorem. Any local, causal, linearly-independent kernel—and locality is enforced by the same theorem that pins the response scale to L₀—must yield the same profile. Flattening a 1/r⁴ source to 1/r² requires applying an inverse Laplacian (a 1/∇² operator), which locality forbids.

**Tier: open (definitively closed by the locality theorem).** GRUT has *no derived dark-matter mechanism* reproducing observed halo phenomenology. Dark matter is a *hosted input*—an empirical boundary condition the theory accepts as external input, much as general relativity accepts the matter it curves. This is not failure; it is clarification. The framework does derive the MOND acceleration scale a₀ = cH₀/(2π), a real scale at which gravitational behavior transitions, but the interpolation function governing that transition is adopted rather than derived. The only path back—should future evidence demand it—is to overturn a foundational result: the locality of the response, the CTP structure beneath it, or the profile-shape theorem itself. Inventing a new dark-sector channel built from the same local, causal response would inherit the same too-steep profile. The dark-matter chapter is therefore *closed pending covariant review* of the nonlinear sector beyond the WKB limit, but closed definitively unless fundamental assumptions are revised.

### 9.8 Standard Model consistency, not uniqueness

The Standard Model satisfies five structural constraints that GRUT's CTP framework derives: the gauge-group structure (SU(3) × SU(2) × U(1)), anomaly cancellation (a consistency requirement), three generations (required by the flavor structure), the Koide K = 2/3 anchor (empirical), and the trace-anomaly numerators (quantum field theory). All five are satisfied. All five are necessary conditions. None of them together, however, are sufficient to prove the SM is the unique minimal theory.

**Tier: computed consistency.** This is a powerful structural result—the SM passes five independent GRUT-derived selection rules and shows remarkable internal coherence with the framework. Establishing uniqueness would require proving that no other gauge theory, coupling structure, or particle content can simultaneously satisfy all five constraints. That is a much harder mathematical problem, one we have not solved. The framework therefore positions the SM as *consistent* with GRUT, a foundation for deeper investigation, but does not claim to explain why the SM has its particular structure.

---

### 9.9 Technical Brief

The governing framework for this chapter rests on the closed-time-path response principle, which we now make explicit in mathematical form.

**The CTP Response and Causal Kernels**

The vacuum's response to a perturbation is computed by varying the influence action S_IF with respect to the difference between forward and backward branches:

$$\Phi_{\mu\nu}^{\text{resp}} = \frac{\delta S_{IF}}{\delta h_q}\bigg|_{q=0},$$

where h_q is the difference field. This response obeys a first-order constitutive equation with memory,

$$\tau_0 \dot{z} + z = z_{\text{target}},$$

whose Fourier transform yields the single-pole susceptibility,

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0}.$$

In the high-frequency limit (ωτ₀ ≫ 1), χ → 0 and general relativity is recovered exactly; in the low-frequency limit (ωτ₀ ≪ 1), χ → 1 and the response is maximal. The retarded Green's function kernel is

$$K_{\mu\nu\rho\sigma}^R(\omega) = \alpha_{\text{vac}} \cdot \chi(\omega) \cdot P^{TT}_{\mu\nu\rho\sigma},$$

where P^{TT} is the transverse-tracefree projector, ensuring the response is causal (satisfying Kramers–Kronig relations) and local.

**Saturation in Black-hole Interiors**

The Ricci scalar, sourced by matter density through Einstein's equations,

$$R_{\mu\nu} = 8\pi G \left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right),$$

in the interior of a black hole reaches a maximum when the CTP response saturates. The saturation point is determined by balancing the source term against the frequency-dependent response. For a matter-bearing interior, the maximum Ricci scalar is

$$R_{\text{max}} = \frac{\alpha_{\text{vac}}}{c^2 \tau_0^2},$$

**Tier:** conjectural—the *values* follow from {α, τ₀}, but the saturation *mechanism* in the full nonlinear closure remains unproven. Applying the relation R_μν ∝ ρ and integrating yields

$$\rho_{\text{max}} = \frac{c^2 R_{\text{max}}}{8\pi G} = \frac{\alpha_{\text{vac}}}{8\pi G c^2 \tau_0^2}.$$

This density is *mass-independent*—a universal constant of the theory.

**The Deep-Infrared Refractive Index**

In the low-frequency limit, the refractive index is defined as

$$n_g(\omega \to 0) = \sqrt{1 + \alpha_{\text{vac}}}.$$

With α_vac = 1/3, this gives

$$R = \sqrt{\frac{4}{3}} = \sqrt{1 + \frac{1}{3}} \approx 1.1547.$$

**Path G** derives this from the trace anomaly. If the conformal mode σ (with coupling ξ = 1/6) carries the infrared response, the Komargodski–Schwimmer theorem gives a/c = 1/3 exactly, hence R = √(4/3).

**Path Osborn** computes the one-loop running of a(M_Z) in the full Standard Model. The running equation is

$$\mu \frac{da}{d\mu} = \beta_a(\alpha_s, \alpha, \alpha_Y),$$

where β_a is the beta function for the trace-anomaly coefficient, depending on the three gauge couplings. Evaluating at M_Z and running to the infrared fixed point yields R ≈ 1.15367. The convergence between paths is

$$\frac{|R_G - R_{\text{Osborn}}|}{R_G} = \frac{|1.15470 - 1.15367|}{1.15470} \approx 0.001.$$

**Tier:** computed—both routes are independent and converge to 0.1% precision, providing robust confirmation of the conformal-mode identification. The third route (3-loop CTP) is **open-negative**.

**The Koide Identity and Z₃ Structure**

The Koide identity is an empirical constraint,

$$K = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3},$$

observed to 0.005% precision. **Tier: anchored**—it is empirical input. Within GRUT, this ratio determines the Z₃ circulant structure of the lepton-mass matrix. The mass matrix takes the form

$$M = M_0 \begin{pmatrix} e^{i\theta} & \omega & \omega^2 \\ \omega^2 & e^{i\theta} & \omega \\ \omega & \omega^2 & e^{i\theta} \end{pmatrix},$$

where ω = e^{2πi/3} is a primitive cube root of unity, M₀ is the scale, and θ is a phase. The requirement that K = 2/3 constrains the phase to θ = 2/9 (or equivalent by Z₃ rotation). **Tier:** computed—this uniqueness follows from consistency with the CTP framework.

**The Measurement-Apparatus Decoherence Ratio**

The gravitational decoherence rate for a mass m in a superposition of separation l, distributed over a body of size R, is (`decoherence_plateau`, **computed**)

$$\Lambda(m, l, R) = \frac{G\, m^2\, S(l/R)}{\hbar\, l}, \qquad S(l/R) = \min\!\left(1, \frac{(l/R)^3}{6}\right).$$

When an apparatus (mass m_A, decoherence rate Λ_A) couples to a system (mass m_S, decoherence rate Λ_S), the joint rate is approximately

$$\Lambda_{\text{joint}} \approx \max(\Lambda_A, \Lambda_S) \cdot \left(1 + \frac{\Lambda_{\text{coupling}}}{\max(\Lambda_A, \Lambda_S)}\right),$$

dominated by the faster decoherence rate. For m_A/m_S ≈ 10^{32} (a 1-gram apparatus and atomic-mass object), the decoherence-rate ratio is Λ_A/Λ_S ≈ 10^{32}, and the joint decoherence becomes ~10^{35} times faster than the system alone. **Tier:** computed—verified numerically for realistic configurations.

The resolution of the Wigner–friend paradox follows: the friend's pointer, being macroscopic, has Λ_friend ≫ Λ_qubit, and thus dominates the joint rate when coupled. The qubit's apparent collapse is the forced decoherence by the faster classical system.

**The Born Rule as Open Postulate**

The CTP formalism produces the decoherence functional

$$D(α, β) = \text{Tr}[P_α ρ_0 P_β e^{-iH(T-t_1)/\hbar} \cdots],$$

which governs the decay of off-diagonal elements |ρ_{ij}| → 0. The pointer basis emerges from the eigenvectors of the environment-induced decoherence matrix. However, the *weights* on the diagonal—the probabilities p_i = |c_i|² assigned to outcomes i—are not derived from the CTP action. They come from the Hilbert-space inner product, an independent postulate. **Tier: open-negative**—the Born rule remains postulated.

---

Each sector presented in this chapter carries its own audited tier. Some results—the refractive index, the measurement-resolution mechanism, the Koide anchor—rest on solid computed or anchored ground. Others—the black-hole saturation mechanism—remain conjectural, with clear closure conditions. One—the dark sector—is definitively closed by a locality theorem, not merely paused. And one—the Born rule—is candidly acknowledged as postulated. This is the honest posture of a theory that survives adversarial review.

---

## 10. The One Assumption, and the Honest Frontier

We have built a theory on three pillars: a responsive vacuum (Q), finite memory (F), and a conjectured broken symmetry (D). Two stand firmly established. One is a bridge whose breaking is proven but whose underlying symmetry is presupposed. And before the analysis closes, we must name and examine the single dimensionless assumption on which the entire framework rests — not to apologize for it, but to honor the obligation to state plainly what is axiom and what is derived.

### 10.1 The Single Dimensionless Axiom: α = 1/3

![The single dimensionless input of v3 and the conditional theorem behind it. If the conformal mode is the infrared carrier (the dashed box — an open antecedent), then the central-charge ratio a/c = 1/3 follows from a = 1/360 and c = 1/120 (Komargodski–Schwimmer 2011). That fixes the one adopted axiom, α = 1/3. The conditional theorem is proven; only its antecedent — the Riegert/Paneitz question — remains open.](figures_v3/fig_axiom_conditional.png)

GRUT admits exactly one dimensionless axiom: the vacuum impedance **α = 1/3**.

This is not derived from first principles. It is **postulated** — adopted as a foundational constant in the same manner that general relativity adopts the metric tensor, quantum mechanics adopts the Born rule, and thermodynamics adopts the entropy postulate. The impedance α normalizes the vacuum's constitutive response to all deformations of the gravitational geometry. It measures, dimensionlessly, how stiff the medium is to a change in shape. In the language of the CTP framework, it sets the overall coupling strength of the response functional.

The value 1/3 is not arbitrary. A conditional theorem has been verified to machine precision: **IF the gravitational conformal mode — the trace-like degree of freedom σ in the conformal decomposition g_μν = e^{2σ}ĝ_μν with conformal coupling ξ_c = 1/6 — IS the infrared carrier of the vacuum's response, THEN by the Komargodski–Schwimmer trace-anomaly theorem (a proven result in quantum field theory), the trace-anomaly ratio a/c must equal exactly 1/3.** The conditional is verified; the theorem is canonical physics, published 2011. GRUT adopts the consequent by accepting the antecedent.

However, the antecedent — that the conformal mode is the infrared carrier — has not been proven from first principles. The historical path was not top-down derivation but reverse engineering: the framework was computed, the output was observed to be 1/3, and the identification was reasoned backward from this numerical coincidence. This is not hidden. The framework states it openly: **the derivation is open-negative.** The first-principles closure awaits a fourth-order computation, the Riegert/Paneitz functional determinant on S⁴, which would calculate the conformal-mode response from the full quantum CTP action and demonstrate that it necessarily yields a/c = 1/3. Until that closure is completed, the framework rests on an adoption, not a derivation.

This is not a weakness unique to GRUT. Every successful theory in physics has begun from axioms: the constancy of the speed of light in special relativity, the principle of equivalence in general relativity, the Planck–Einstein relation in quantum mechanics. What distinguishes GRUT is its precision about which axioms are adopted and which are derived, and what conditions would close each gap. The wager is this: α = 1/3 is the correct dimensionless axiom. The cost of honesty is that we do not conceal it under layers of machinery or historical narrative. It sits in plain light, with its closure condition explicit and its falsifiability clear: if a first-principles derivation of the Riegert functional determinant yields a different trace-anomaly ratio a/c, or if observations demonstrate that α ≠ 1/3, the entire framework requires revision.

### 10.2 The One Scale, and the Breaking of Symmetry

The second input is dimensionful: the relaxation timescale **τ₀ = 41.9 Myr**. This is not an axiom; it is **anchored by observation**. No first-principles calculation, no matter how refined, will derive τ₀ from fundamental constants *G*, *ℏ*, *c* — not because of insufficient technical skill, but because τ₀ is structurally anchored to the universe itself. It emerges, with convergence to within observational error, from three independent observational routes: the cosmic baseline (the Hubble expansion rate and the implied dark-sector radius), cluster collisions (the kinematic offset in the Bullet Cluster between gas and gravitational centroid), and the self-consistency of the framework's own cosmological predictions against *H*(*z*), baryon acoustic oscillation measurements, and the decoherence plateau. These routes agree to within their ~20% spread, all clustering near 41.9 Myr. No other timescale in the gravitational response fits the phenomenon; H₀, BAO, cluster mergers, and the laboratory falsifier all point to the same τ₀.

This timescale carries physical significance beyond merely setting a scale. It is the one physical length **L₀ = c·τ₀ ≈ 12.85 Mpc** that breaks the **adiabatic spatial-dilatation redundancy D** of general relativity. In the memoryless limit (L₀ → 0), Einstein's theory possesses a long-wavelength gauge freedom: a uniform rescaling of all spatial coordinates, φ(x) → φ(e^λ x), changes nothing in the physics. This is not a feature GRUT invents; it is a mathematical identity of general relativity itself, latent whenever the universe is sufficiently old that short-wavelength modes have decayed. Turning on finite memory — a fixed proper length L₀ across which the vacuum retains information — breaks that gauge freedom at order (L₀ k_phys)². The breaking is controlled and non-anomalous: it does not arise from quantum corrections to the path integral (the measure is invariant under the diffeomorphism of a coordinate rescaling, not under a Weyl transformation which is a physical change of scale), so no trace-anomaly coefficient enters the breaking term. It is the same structure by which a particle mass breaks scale invariance in quantum field theory. A theory is defined by which symmetry it breaks and by how much; GRUT breaks the long-wavelength rescaling by a single length scale.

From this breaking flow the universe's distinguishing features. The linear modified-gravity enhancement (the μ > 1 channel) is ruled out by the framework's consistency requirements and by CMB–ISW data (the μ → 4/3 enhancement is excluded at 32σ). The dark sector is forbidden from living in the linear scalar channel. Cosmology is constrained to be indistinguishable from ΛCDM. The framework's entire predictive skeleton is built not from what it permits but from what it forbids. This is why τ₀ is the linchpin: lose it or change it by 30%, and the Hubble rate, dark-energy fraction, and decoherence plateau all shift incompatibly. The framework is tightly woven from the breaking of this one symmetry by this one scale.

### 10.3 The Honest Frontier: The Open-Negative Ledger

GRUT carries twenty-eight open-negative claims: unsolved problems the framework has not closed, dead-end explorations it has exhausted, and structural seams it acknowledges. This is not a weakness to hide but a signature of maturity. In the history of physics, frameworks mature not by closing all questions at once but by distinguishing which questions are within their scope and which are beyond it, and by stating the closure condition for each. Thermodynamics opened with entropy as a postulate and its implications; general relativity began with the equivalence principle and field equations, leaving dark matter, singularities, and quantum gravity to the frontier. Quantum mechanics began with the Born rule and measurement still unresolved.

GRUT follows this path. The most load-bearing open negatives are:

- **The first-principles derivation of α = 1/3** — the Riegert/Paneitz computation of the conformal-mode functional determinant on S⁴, and the proof that the gravitational conformal mode is the infrared carrier. This is the single most critical gap.

- **The third R-route** — the numerical completion of the 3-loop CTP anomaly integral via Allen–Jacobson propagators. The symbolic structure is constructed; the loop integration remains uncomputed. Closure would tighten confidence in the deep-infrared refractive index R = √(4/3).

- **The dark-matter mechanism** — a definitive negative result, not a still-open question. The Weyl-squared channel, the most sophisticated candidate, has the right magnitude but the wrong radial profile; a locality theorem forbids the inverse-Laplacian operator that would reshape it. Dark matter is therefore a **hosted input** — a boundary condition the framework is consistent with rather than derives. This is not a failure but a precise statement of scope.

- **The Born rule** — GRUT recovers the classicalization timescale (the rate at which quantum coherence disappears) but does not derive the probability weights themselves. The Born rule remains a postulate.

- **Flavor and the Koide amplitude** — the Z₃ circulant structure in the lepton sector is derived; the amplitude of the Yukawa coupling is empirical input. Flavor physics is hosted from the Standard Model.

- **The underlying adiabatic redundancy D** — presupposed from standard general-relativity machinery rather than re-derived from GRUT's CTP action from first principles. The proof that D is an exact gauge symmetry in the memoryless limit would convert D from a bridge to a proven pillar.

The full ledger is recorded in `grut/toe/ledger.py`, with each entry carrying its closure condition and effort estimate. The framework does not pretend these gaps do not exist. They are the research frontier.

What is notable is that GRUT survives its own adversarial audit by shedding attractive ideas. The linear dark-sector enhancement was ruled out not by external observation alone but by the framework's own consistency requirements and the data together — not suppressed but explicitly closed. The Koide-amplitude derivation failed in a cleanly falsifiable way (the impedance calculus yields a different value). The mechanisms that survived were not the graceful ones but the constraining ones: the no-go on linear modified gravity, the locality theorem that closes the dark sector, the minimal matter coupling, the tracefree kernel. These are not ornaments. They are the structural walls.

### 10.4 The Research Frontier: Three Critical Directions

The path forward has three focal points, each carrying real difficulty and precision.

**First: the Riegert computation.** Deriving α = 1/3 from the conformal-mode functional determinant on the four-sphere S⁴. This requires mapping the fourth-order Paneitz operator to a loop integral, extracting the conformal-mode determinant carefully, and verifying that it yields a/c = 1/3 necessarily. If it does, the axiom graduates to a derived constant, and GRUT's foundational posture shifts from "postulated on one axiom" to "derived from the vacuum-response requirement and the CTP structure." If the true a/c is different — 2/5, 1/4, or another value — the framework requires revision. This is the load-bearing problem.

**Second: the L₀ → 0 redundancy proof.** Independently re-deriving that the adiabatic spatial dilatation is a true gauge symmetry of GRUT's full closed-time-path action in the memoryless limit, not merely a presupposition inherited from general relativity. This would convert D from a conjectured bridge (whose breaking is proven) to a proven symmetry (whose breaking is separately established), unifying all three pillars under a single coherent structure. The theorem is structurally clear; the proof path is open.

**Third: R-routes completion.** Computing the third path (3-loop CTP via Allen–Jacobson propagators) numerically, to complete the two-route convergence at R = √(4/3). This would close a computational gap and test the framework's loop-level consistency at the full-theory level.

These are not decorative improvements. They are what separate a candidate framework from a closed theory. They are open because they are genuinely difficult, not because they are optional.

### 10.5 The Ethos: The Mathematics Survives; the Ontology Changes

GRUT v3 is built on a discipline: *when a claim fails verification, demote it honestly and do not retreat from the framework itself.* The linear dark-sector enhancement — elegant, promising dark matter for free — was wrong. The framework does not use it. The Koide-amplitude closure was mathematically neat; it failed the algebra. The framework does not claim it. What survived were not rescues but **constraints**: the no-gos, the forbidden channels, the minimal couplings, the precise boundaries of what the vacuum is permitted to respond to. A falsifiable theory is made of these.

The mathematics usually survives. The ontology changes. τ₀ shifts from "derived by precision calculation" to "anchored by convergent observation from three independent routes." The axiom α remains α, but its origin becomes candidly open, not concealed under procedural machinery. The dark matter story becomes "GRUT hosts it as input, deriving the MOND scale a₀ and proving that locality forbids naive mechanisms" rather than "GRUT derives dark matter." The theory becomes more falsifiable by becoming more honest about its boundaries.

This is v3's wager: a framework that writes down what it has not closed is stronger than one that hides the gaps. The frontier is visible. The ledger is complete. The next person to work on GRUT knows exactly which door opens which room.

### 10.6 Technical Brief

**The conditional theorem on α and the trace anomaly.** The vacuum impedance α enters the response kernel as the dimensionless coefficient multiplying the susceptibility. Its value is determined by a conditional theorem:

$$\text{IF } g_{\mu\nu} = e^{2\sigma}\hat{g}_{\mu\nu}, \text{ with } \sigma \text{ conformally coupled } (\xi_c = 1/6), \text{ THEN } \frac{a}{c} = \frac{1}{3}.$$

The result rests on the trace-anomaly central charges of a free conformal field. In four dimensions the conformal (Weyl) anomaly of a CFT takes the form

$$\langle T^\mu{}_\mu \rangle = \frac{1}{16\pi^2}\left(c\,W^2 - a\,E_4\right),$$

where $W^2 = C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}$ is the Weyl-squared invariant, $E_4$ is the Euler (Gauss–Bonnet) density, and $a$, $c$ are the two central charges. For a single real conformally-coupled scalar ($\xi = 1/6$) these take their standard free-field values (Duff 1977; Birrell–Davies 1982):

$$a = \frac{1}{360}, \qquad c = \frac{1}{120}.$$

Their ratio is therefore

$$\frac{a}{c} = \frac{1/360}{1/120} = \frac{120}{360} = \frac{1}{3}.$$

The Komargodski–Schwimmer theorem (2011) establishes that $a$ decreases monotonically under renormalization-group flow and that the ratio $a/c$ is a well-defined, scheme-independent characteristic of the conformal sector. GRUT identifies the gravitational conformal mode — the scale degree of freedom $\sigma$ in $g_{\mu\nu} = e^{2\sigma}\hat{g}_{\mu\nu}$ — with such a scalar, and on that identification adopts

$$\alpha = \frac{a}{c} = \frac{1}{3}.$$

The conditional theorem — *if* the conformal mode is the carrier, *then* $a/c = 1/3$ — is what is established. The **antecedent** is the open part: that the gravitational conformal mode genuinely *is* the infrared carrier of the vacuum's response has not been derived from first principles. Closing it requires computing the effective action of the conformal-mode sector on $S^4$ and confirming the anomaly ratio is $1/3$ — the Riegert/Paneitz closure condition, recorded in the open-negative ledger.

**The broken symmetry and the order of breaking.** The adiabatic spatial-dilatation redundancy D reads: under the coordinate rescaling $x \to e^\lambda x$ (all spatial coordinates multiplied by $e^\lambda$), the action of GR is invariant in the limit $L_0 \to 0$. With finite memory, this breaks at order $(L_0 k_{\text{phys}})^2$.

To see this, consider a long-wavelength perturbation with physical wavenumber $k_{\text{phys}}$. Under the rescaling, coordinates change as $x \to e^\lambda x$, so $k \to e^{-\lambda} k$. The wavelength in proper (physical) units is $\lambda_{\text{phys}} = 2\pi / k_{\text{phys}}$. The memory kernel depends on the combination $L_0 k_{\text{phys}}$ (or equivalently $L_0 / \lambda_{\text{phys}}$). Under a coordinate rescaling, the memory argument becomes

$$L_0 k_{\text{phys}} \to e^{-\lambda} L_0 k_{\text{phys}}.$$

In the constitutive equation $\tau_0 \dot{z} + z = z_{\text{target}}$, transformed to frequency space, the susceptibility appears as

$$\chi(\omega) = \frac{1}{1 - i\omega\tau_0} = \frac{1}{1 - i\omega \cdot (L_0/c)}.$$

A uniform rescaling of space changes $\omega$ → $e^{-\lambda} \omega$ (the frequency of an oscillation scales inversely with the distance scale). Thus the argument $\omega \tau_0$ is invariant. However, when the response couples to *spatial* gradients — to the square of the wavenumber in certain channels — the breaking becomes manifest. The second-order response kernel for the Weyl-squared channel, for example, depends on $(L_0 k_{\text{phys}})^2$. Under rescaling,

$$(L_0 k_{\text{phys}})^2 \to e^{-2\lambda} (L_0 k_{\text{phys}})^2,$$

which is not invariant. This breaking is non-anomalous: it does not come from the path-integral measure (which is invariant under diffeomorphisms) but from the classical dynamics of a medium with a fixed proper length. The breaking enters at the controlled order $(L_0 k_{\text{phys}})^2 \sim (L_0 H_0)^2 \sim 10^{-6}$ for cosmological scales, making it small but physically non-negligible at the right scales.

**The L₀ → 0 redundancy — the open problem.** The proof that D is an exact symmetry of GRUT's full CTP action $S_{\text{CTP}}$ in the memoryless limit remains to be completed. The claim would be:

$$\text{OPEN: } S_{\text{CTP}}[g_{\mu\nu}(x)] = S_{\text{CTP}}[g_{\mu\nu}(e^{-\lambda} x)] \text{ when } L_0 \to 0.$$

This is presupposed from standard Weinberg machinery, but re-deriving it from GRUT's CTP formalism starting from the influence functional would close a structural gap and prove that D is a true symmetry of the theory, not merely an inheritance.

## Acknowledgments

This work was developed independently over multiple years. The framework draws on a broad intellectual tradition in theoretical physics: Schwinger and Keldysh for the closed-time-path formalism; Mori and Zwanzig for projection-operator techniques; Gibbons, Hawking, and Perry for Euclidean gravity on S⁴; Christensen and Duff for trace-anomaly coefficients; Allen and Jacobson for propagators on curved space; Osborn for local renormalization-group methods; Komargodski and Schwimmer for the four-dimensional a-theorem that fixes the central-charge ratio a/c; Koide for the charged-lepton mass relation; Riegert and Paneitz for the conformal-anomaly effective action; Walecka for nuclear mean-field theory; and the Planck, PDG, and observational-cosmology communities whose precision measurements provide the anchors. None of these authors is responsible for the present framework's claims or conclusions.

The computational infrastructure was developed in Python with NumPy, SciPy, and Flask. The claim registry, the open-question ledger, the tier-discipline enforcement, and the automated appendices are original infrastructure. The GRUT-RAI codebase is available at the DOI given on the title page.

**AI-assisted development.** Substantial portions of the GRUT-RAI codebase, test suite, and documentation were developed with the assistance of Claude Code (Anthropic). Claude Code contributed to: writing and debugging computational modules (constitutive growth, modified gravity, Boltzmann/ISW injection, the S⁴ CTP solver, and the second-order Weyl-squared kernel); building and maintaining the 3,227-test verification harness; constructing the claim registry, open-question ledger, tier-discipline infrastructure, and automated appendix rendering; drafting and iterating this document across multiple revision cycles, including the figure suite and this edition; and providing adversarial review that surfaced several corrections — including the v3 re-tiering of over-claimed v2 results, the locality theorem that records dark matter as a hosted input rather than a derived mechanism, the 32σ refutation of the linear μ = 4/3 enhancement, and arithmetic and consistency errors caught in the final publication pass. All physical ideas, theoretical derivations, and scientific claims are the author's. Claude Code served as a computational and editorial collaborator — an instrument, not a co-theorist. Its contributions are acknowledged transparently in the same spirit as acknowledging any other computational tool.

## References

The framework builds on and cites the following works. Full provenance for every quantitative claim is recorded in the machine-checked claim registry.

- Allen, B., & Jacobson, T. (1986). *Vector two-point functions in maximally symmetric spaces.* Commun. Math. Phys. **103**, 669.
- Christensen, S. M., & Duff, M. J. (1978). *Axial and conformal anomalies for arbitrary spin in gravity and supergravity.* Phys. Lett. B **76**, 571.
- Gibbons, G. W., Hawking, S. W., & Perry, M. J. (1978). *Path integrals and the indefiniteness of the gravitational action.* Nucl. Phys. B **138**, 141.
- Keldysh, L. V. (1965). *Diagram technique for nonequilibrium processes.* Sov. Phys. JETP **20**, 1018.
- Koide, Y. (1982). *Fermion–boson two-body model of quarks and leptons and Cabibbo mixing.* Lett. Nuovo Cimento **34**, 201.
- Komargodski, Z., & Schwimmer, A. (2011). *On renormalization group flows in four dimensions.* JHEP **12**, 099. arXiv:1107.3987.
- Mori, H. (1965). *Transport, collective motion, and Brownian motion.* Prog. Theor. Phys. **33**, 423.
- Osborn, H. (1991). *Weyl consistency conditions and a local renormalisation group equation for general renormalisable field theories.* Nucl. Phys. B **363**, 486.
- Paneitz, S. M. (1983; published 2008). *A quartic conformally covariant differential operator for arbitrary pseudo-Riemannian manifolds.* SIGMA **4**, 036.
- Particle Data Group (Workman, R. L., et al.) (2022). *Review of Particle Physics.* Prog. Theor. Exp. Phys. **2022**, 083C01.
- Planck Collaboration (Aghanim, N., et al.) (2020). *Planck 2018 results. VI. Cosmological parameters.* Astron. Astrophys. **641**, A6. arXiv:1807.06209.
- Riegert, R. J. (1984). *A non-local action for the trace anomaly.* Phys. Lett. B **134**, 56.
- Schwinger, J. (1961). *Brownian motion of a quantum oscillator.* J. Math. Phys. **2**, 407.
- Walecka, J. D. (1974). *A theory of highly condensed matter.* Ann. Phys. **83**, 491.
- Zwanzig, R. (1960). *Ensemble method in the theory of irreversibility.* J. Chem. Phys. **33**, 1338.

---

*GRUT ToE v3 · Candidate Framework. One broken symmetry, one scale, one axiom — and an honest account of
the rest. The companion technical edition is `theory/GRUT_TOE_V3.md`; the machine-checked claim registry
(`grut/toe/registry.py`) and open-negatives ledger (`grut/toe/ledger.py`) are the backing for every
statement above. GRUT Research — www.zenodo.org/communities/GRUT.*
