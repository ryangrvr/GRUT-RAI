# GRUT: THE SKELETON — claims, status, and kill conditions

**Version 02, 2026-09-24.** GRUT — *Grand Responsive Universe Theory*, a name retained
by program convention (§11) — is presented here for a physicist outside the program:
what it claims, what has actually been derived, what is measured rather than derived,
what remains conjectural, and what would kill it. Version 02 incorporates an
adversarial verification round run on version 01 itself; the defects that round found
in this document are disclosed in §10, because they instantiate the exact failure mode
the program polices.

**Status tags.** **DERIVED** = a calculation on the program record establishes it, at
stated scope, *at the level of passing pre-registered checks* (not verdict prose — see
§10). **ANCHOR** = shown (not assumed) to require empirical input within the admitted
principles of §3.0. **HYPOTHESIS** = proposed and testable, not derived. **OPEN** =
under construction or unresolved. Nothing here is called proven; survival of a test is
never treated as truth. The calculations are FAIL-forward instruments: each check is a
pre-registered prediction, failures are recorded rather than repaired post hoc, and a
verdict is only as good as its checks.

## 1. The claim, in one paragraph

GRUT proposes that irreversible, memory-bearing response originates in a **finite,
strictly local microscopic substrate** whose infinite-volume limit generates a
**continuum of persistent degrees of freedom**; that the fundamental constitutive
objects are the **retarded response kernel K_R(t)** and its **spectral measure ρ(τ)**;
and — the central hypothesis — that **gravity is the physical realization of this
persistent continuum**: the universal dissipative environment to which all matter
couples. Everything below that identification is a claim about generic resistive
media; the identification itself is what gives the program empirical content, and it
is the clause exposed to the kill test of §6.

## 2. The ladder

Tags apply at the stated scope — generic local resistive media below the
identification arrow; everything read *as a claim about gravity* is HYPOTHESIS until
§6 reports. The arrows deliberately do not all have the same status.

```
finite local microscopic substrate
        │  DERIVED (necessity): memory REQUIRES persistent auxiliary state —
        │    a slaved variable yields only instantaneous response (checks P1, P2)
        │  OPEN (constructive converse): "every finite-memory kernel is
        │    realizable by persistent modes, with N = M" failed its defining
        │    checks on the record (P3, P4, E4a — disclosed in §10)
        ▼
persistent degrees of freedom
        │  DERIVED: dissipation and continuous spectra emerge in the
        │  thermodynamic/infinite-volume limit; no damping inserted by hand
        ▼
thermodynamic continuum of memory modes
        │  DERIVED (form): spectral measure positive (completely monotone /
        │    Bernstein–Widder class); passivity excludes repeated (Jordan) poles
        │  ANCHOR (content): the support of ρ and the scale τ₀ are supplied
        ▼
positive spectral measure ρ(τ)
        │  DERIVED (conditional): ρ is uniquely recoverable from K_R when all
        │  spectral moments are finite (light tails). Power-law/heavy tails sit
        │  OUTSIDE the deterministic uniqueness class — and the gravitational
        │  kernels of §6 are that class. Whether nature is light-tailed is an
        │  empirical input. The support structure (atomic vs continuous) remains
        │  an observable of K_R unconditionally (check E2a).
        ▼
retarded constitutive response K_R(t)
        │  DERIVED: existence of irreversible response; positivity; passivity
        │  ANCHOR: the direction of the arrow of time is imported
        ▼
dissipation + passivity + arrow
        │  HYPOTHESIS: gravity as the realization of the memory continuum —
        │  spectrally consistent at 8/9 checks (measured graviton DOS exponent
        │  1.972 vs theoretical 2.000; negative control passed); NOT derived
        ▼
candidate gravitational realization
        │  OPEN: the matter–graviton coupling. First derivation attempt
        │  adjudicated: ATTEMPT RECORDED, INSTRUMENT REPAIR REQUIRED, GATE
        │  UNTOUCHED (§5). The instrument is being rebuilt as the on-shell
        │  golden-rule object; analytic predictions are to be sealed by both
        │  parties BEFORE the rebuilt instrument reports (§6 protocol).
        ▼
matter–gravity coupling
        │  KILL TEST (an event, not a status): the T3 confrontation (§6);
        │  external channels in §7
        ▼
observable response
```

## 3. What has actually been derived

### 3.0 The admitted principles (what "derivable" is relative to)

Strict locality; finite microscopic content; autonomous first-order dynamics;
passivity (no internal free-energy source); time-translation invariance; standard
open-system reduction (elimination of unobserved variables; in-in response). Priced
imports beyond these are ledgered per result. Every "cannot be derived" claim in §4
means: not derivable from *these* principles — a narrower and more checkable statement
than absolute impossibility.

### 3.1 The derived items (with certificates and, where they exist, failures)

The central defining relation, for orientation — schematic; exact definitions live in
the cited records:

    K_R(t) = ∫ e^(−t/τ) dρ(τ)   (completely monotone class),
    retained-sector dynamics:  q̇(t) = −∫₀ᵗ K_R(t−s) q(s) ds + drive,

obtained by eliminating persistent local variables from a finite network with
first-order passive dynamics.

1. **Memory requires persistent auxiliary structure** (necessity direction). A
   no-memory theory stays memoryless; persistence appears iff an auxiliary variable
   carries independent state. *(persistence-origin checks P1, P2, passing.)* The
   converse package — elimination constructively produces the kernel; every
   non-instantaneous kernel is representable; realization dimension N equals the
   number of eliminated modes M — is asserted in several record verdicts but its
   defining checks failed (P3: tail error 0.995; P4: N=M broken at M=5; E4a:
   claimed convergence with increasing errors). Status: OPEN at check level. See §10.
2. **Continuum and dissipation from the thermodynamic limit.** A strictly local,
   finite, non-dissipative substrate generates continuous spectra and irreversible
   response in the infinite-volume limit; late-time kernel class t^(−d/2) (d = spatial
   dimension of the substrate), with the small-k cusp term argued subleading (stated
   stationary-phase rationale corroborated by the measured envelope). *(continuum-origin
   6/6; infinite-bath 4/4; irreversibility-origin 3/4.)*
3. **Form constraints on the spectrum.** Positivity (Bernstein–Widder); exclusion of
   repeated poles by passivity *(realization-dimension check E5b, passing)*;
   conditional uniqueness of ρ from K_R (light-tailed case; check E2b) with the
   heavy-tailed exception disclosed in the ladder; support structure observable from
   K_R alone *(check E2a)*.
4. **A minimal generative ontology.** Local first-order dynamics plus resistive
   couplings suffice to generate the structure above — the "resistive persistent
   sector," conditional on §3.0. *(minimal-generative-ontology, 5/6.)*
5. **Two selection rules in the gravitational construction, mutually reinforcing.**
   The transversality rule (the TT polarization component along the matter axis
   vanishes for aligned propagation) emerges from geometry unimposed *(coupling calc
   V8)*; independently, the aligned emission channel closes kinematically — a
   lightlike graviton at aligned incidence has no interior on-shell two-phonon
   solution, a Cherenkov-type mismatch (subsonic phonons, lightlike graviton).
   Reported by the builder during the instrument rebuild; confirmed analytically by
   the adjudicator; pending re-confirmation on the rebuilt instrument.

### 3.2 A certified external anchor (NOT a GRUT derivation)

The program's one published-grade result is standard QFT, independent of the GRUT
interpretation: the absorptive part of the graviton self-energy on a de Sitter
background through order H⁶ — branch-cut class, ω⁴ flat-space limit, dissipative sign,
validity window ω ≳ 3.4H (= √(104/9) H). Referred to throughout as **the T3
certificate**. Availability: public repository release (GRUT-RAI, branch
`physics-final`, package v1.0, commit 310101f); archival (Zenodo) upload pending. It
is listed here as the fixed wall the §6 confrontation runs into, not as evidence for
GRUT.

## 4. What is measured, not derived

- **The spectral content of ρ(τ)** — support/dimension and the macroscopic scale τ₀:
  six dedicated no-go calculations (scale-origin, resistive-scale,
  gravitational-clock, geometry-selection, KMS-constraint, dimension-selection) agree
  that no mechanism inside §3.0 generates them. Anchors, analogous in role to G and Λ
  in general relativity — with the caveat that ρ's support is a functional input,
  a larger supply than two constants.
- **The direction of the arrow of time**: existence of irreversibility is derived
  (item 2); orientation is imported boundary data *(irreversibility-origin,
  infinite-bath records)*.
- **The quantum sector**: quantum mechanics is imported; Born weights are anchors —
  and not merely by policy: the program's tested derivation routes returned negative
  results (Experiment-P record). GRUT claims nothing about deriving them.
- **Ledgered imports of the coupling construction**: κ = 1/M_Pl (dimensionful), the
  retained-sector microscopic structure, and the minimal-stress-coupling postulate —
  the postulate is where the known no-go pressure on emergent gravity sits (§8).

A parallel audit program (RRP-00→03) found the same derived-structure/supplied-point
architecture in every audited formulation of established physics and concluded — at
audited scope: the audited frameworks, map class, and null models, not a universal
theorem — that the pattern is a property of formal description. Context, not upgrade:
it makes GRUT's anchor list expected structure, and proves nothing about GRUT.

## 5. What is conjectural

- **The gravitational identification** (central hypothesis): gravity has the right
  spectral class to be the universal memory bath (8/9 spectral checks; DOS exponent
  match above) and both selection rules come out correctly, but no calculation derives
  gravity as the bath.
- **The coupling.** The first derivation attempt ran 5 PASS / 4 FAIL; its own verdict
  string was "derived-within-class with imports ledgered," but the adjudication found
  the instrument computed an off-shell object rather than the physical dissipative
  spectral density, demoted the attempt to **ATTEMPT RECORDED, INSTRUMENT REPAIR
  REQUIRED, GATE UNTOUCHED**, and found the calc's verdict_detail describing a run
  that did not happen (instance #3 of §10's pattern). The rebuilt on-shell instrument
  and its theorem-gated pre-registration are the current work front.
- **Everything above the coupling arrow**, read as physics of gravity.

## 6. The in-house kill test: the T3 confrontation

Two objects produced by independent routes must agree or the identification dies:
the **T3 certificate** (§3.2 — loop QFT, fixed, certified) and the **gravitational
memory-kernel class predicted by the GRUT mechanism** once the rebuilt on-shell
coupling instrument reports. The comparison is by exponent class of the dissipative
response in the certificate's validity window (ω ≳ 3.4H), with the exact common
observable and the mapping between the two objects fixed in the pre-registration
*before* any numbers are compared.

Protocol (adopted 2026-09-24, before any rebuilt-instrument numbers exist):

- **Theorem gate, not exponent assertion.** The soft-limit exponent of the on-shell
  matter–graviton amplitude is *derived* — conservation-law cancellations and the TT
  projection tracked explicitly — never encoded as an expected answer (e.g., the
  quadrupole ω⁵ folklore) to be "confirmed." If soft suppression emerges, the exact
  cancellation responsible must be identified; if not, the specific assumption of the
  radiation analogy that fails for a response kernel must be identified.
- **Dual pre-registration.** Builder and adjudicator (§9) seal independent analytic
  predictions, by commit, before the rebuilt instrument reports. Their agreement or
  disagreement is itself recorded. Status: protocol adopted; instrument rebuild in
  progress; pre-registrations not yet sealed.
- **One leg already agrees:** the sign. The mechanism derives strict passivity; the
  certificate records the dissipative sign in-window. Necessary, far from sufficient.
- **Pre-registered outcomes.** Class match = the first discriminator-grade internal
  support the program has had (with the honest caveat that matching one exponent
  class from a small discrete set is weak Bayesian evidence — the match probability
  under the null is not small enough to retire skepticism). Mismatch = the
  identification is dead at a certified wall. Both outcomes are answers.

## 7. External kill channels

- **DESI w(z).** The program's record contains a named cosmological export — a
  within-branch prohibition on dark-energy phantom-divide crossing, tied to the
  second-law side of the mechanism — currently held at to-derive grade and gated on
  an unresolved rung of the derivation chain. Honestly: this channel is *armed but
  not sealed*; no committed sign prediction is published yet, so an outside reader
  cannot execute this test today. Sealing it (or discharging it as underivable) is on
  the program's books.
- **Any measured K_R in a system the theory claims** (candidate systems not yet
  named — a recorded gap): the kernel constrains ρ(τ) by inversion in the light-tailed
  case, the support structure unconditionally (E2a); a kernel requiring a non-positive
  measure or repeated poles falsifies the derived form constraints themselves — a
  deeper failure than the gravitational identification.

## 8. Obstructions this program must face (and where they currently sit)

Named because a referee will ask, and because their locations in the skeleton are
informative. **Weinberg–Witten (1980):** constrains massless spin-2 in theories with a
covariant conserved stress tensor; the program's requirement audit carries it as a
named-exit condition — any eventual GRUT completion must state which hypothesis it
relinquishes. **Soft-graviton universality (Weinberg):** universal stress coupling is
*imported* here as the minimal-stress-coupling postulate — the import is where the
emergent-gravity no-go pressure concentrates, and §6's theorem gate is the first place
it gets tested rather than assumed. **Lorentz invariance:** a retarded kernel selects
a frame; the present construction is non-relativistic (a lab-frame chain), and
recovery of covariance is OPEN — no claim is made. **Energy bookkeeping / Bianchi
consistency** of a dissipative gravitational sector: OPEN, unaddressed. **GR
recovery:** recorded as recovered-with-imports (the imports ledgered), not derived.
**Nearest relatives** a reader should compare: Caldeira–Leggett open-system baths
(the formal ancestor of the kernel machinery), stochastic gravity's Einstein–Langevin
equation (Hu–Verdaguer — gravity *with* noise/dissipation kernels, where GRUT's
identification instead makes gravity *the* kernel's realization), induced gravity
(Sakharov), and thermodynamic derivations of the field equations (Jacobson 1995).
GRUT's differentiator, if it survives §6, is the direction of the identification;
none of the above is currently cited as support.

## 9. Who "builder" and "adjudicator" are

AI-operated build and audit roles under the direction of the program owner, working
in separated trees with blinded protocols (the audit side derives predictions without
seeing the build side's numbers, and vice versa). "Independent" in this document means
separate processes and sealed commits, not external review. **No external validation
of any GRUT-specific claim exists yet.** The T3 certificate (§3.2) is the only item
positioned for outside checking today.

## 10. Record-integrity disclosure

This program's recurring documented failure mode is **narrative-vs-run mismatch**: a
verdict or summary asserting what its own checks refuted. Four instances are on
record: (1) a kernel exponent t^(−d) vs t^(−d/2) narrative/body mismatch
(continuum-origin, since repaired); (2) a t^(−3) vs t^(−4) inconsistency
(spectral-match, correction pending); (3) a coupling verdict_detail describing a run
that did not happen (§5); and (4) — found by the adversarial verification of *this
document's version 01* — persistence/representation prose asserting a theorem whose
defining checks failed (P3 tail error 0.995 vs threshold 0.05; P4 Hankel rank 4 at
M=5 breaking the claimed N=M law; E4a claiming errors "decrease" over the recorded
increasing sequence 0.721 → 1.193). Version 01 of this skeleton propagated instance
#4 into its base-rung DERIVED tag; version 02 demotes that tag (§2, §3.1 item 1). The
operating rule, applied to this document itself: **checks outrank prose, and every
status tag must trace to a check outcome.** Repairs of the underlying record entries
are owed by the build side and tracked.

## 11. What GRUT does not claim, and the name

No observable predictions beyond the kill channels above. No Standard Model content
(any completion must satisfy the standard anomaly-freedom conditions; the substrate
work has not touched matter content). No derivation of quantum mechanics or Born
statistics. No derivation of ρ's content or τ₀ (§4's no-gos forbid it within §3.0).
The historical GRUT claim set (pre-2026-09-23) is closed; the program convention is
that "GRUT is the name given to whatever coherent physical account survives the
investigation." To preempt the natural objection that this makes GRUT unkillable: the
*name* is a program label, and what is killable is stated exactly — the gravitational
identification dies at §6 or §7, and the derived lower half (items in §3.1) would
survive such a death only as generic open-system results, explicitly stripped of the
gravitational reading. A §6 mismatch would be recorded as the central hypothesis of
this skeleton failing, in those words.

## 12. Where things stand, honestly

A skeleton exists. Its lower half is derived at stated scope — with one base-rung tag
demoted by the program's own verification round (§10) — and its central objects are
measurable in principle, conditionally in practice. Its upper half is one
identification plus one construction under theorem-gated rebuild. "Working theory"
status requires at minimum: the §6 confrontation passed, ρ(τ) constrained by at least
one measured kernel, and the cosmological export sealed and surviving DESI. None of
these has happened. If the skeleton fails at §6, the program revises the central
mechanism early rather than building sectors on top of it; if it survives, later
sectors — quantum statistics, matter content, cosmology, classical spacetime — attach
one at a time, each with its own kill condition.
