# C1 in-house assembly attempt — how far the pole-vs-cut question can be pushed without the specialist

> ## ERRATUM (2026-08-10b) — four source-verified corrections; the body below is retained unedited
> 1. **T² is a coefficient function, not a structure function** (p.23: "the only one of the
>    coefficient functions Tⁱ(x;x′) that contributes is T²(x;x′)"). The nine structure functions
>    are T¹², T¹⁶, T¹⁸, T¹⁹, S², S⁴, S⁷, S⁸, S¹⁰ (p.14, Epilogue); eq. (81) makes T² a composite
>    of six of them. Step 1's "one of the nine structure functions" is wrong at the category.
> 2. **The tabulated T² is the in-out (Feynman) object, not retarded** — Step 1's "T² *is* the
>    (gauge-fixed) retarded TT self-energy kernel" is wrong at the definition. In 48 pages:
>    `retarded` 0, `causal` 0, `Schwinger` 0, `Keldysh` 0, `in-in` 0; T*-ordered VEVs at
>    eqs. (116), (133); Feynman iε at eq. (9). The SK conversion is arXiv:2107.13905 §2.2.3
>    (T²_SK; eqs. (52)–(55) create the causal support and branch structure).
> 3. **"exact one-loop coincidence-limit tables" is inverted on both words** — §4.2: "The actual
>    computation [22] was made in D=4 dimensions before it was understood how to employ
>    dimensional regularization, so it can only be used away from coincidence." Not dim-reg'd,
>    not renormalized, missing local terms.
> 4. **A position-space ln(H²∆x²) is not time-domain secularity** — that needs the x′ integration
>    of eq. (109), which the paper explicitly has not done (Epilogue). "Demonstrably nonzero and
>    secular" overstates: NONZERO is established; "secular" awaits the integration.


*Node: `rung3_single_pole` / channel `C1` (`PREREG_TERMINATION_V4_2026-08-10.txt`). Status: **NOT a resolution of C1** — R2 ("nodes decide") and R4 ("quotes decide") govern C1's actual channel line, logged separately in `provenance/prereg/RESULT_TERMINATION_events.txt`. This file is an in-house computation attempt using only published, cited results — the thing DISPATCH_ONE_PAGE.md was sent out precisely because this attempt cannot finish it. Read as: how far can the existing literature legitimately carry the assembly before hitting a named, uncompleted piece of machinery — not as a specialist-grade derivation.*

*Sources (full technical extraction in `c1_assembly_technical_inputs.md`, not copied into this repo — cite directly): Tan, Tsamis, Woodard, [arXiv:2103.08547](https://arxiv.org/abs/2103.08547) (CQG 38 (2021) 145024); Glavan, Miao, Prokopec, Woodard, [arXiv:2602.07908](https://arxiv.org/abs/2602.07908) (JHEP 04 (2026) 159); Mora, Tsamis, Woodard, [arXiv:1307.1422](https://arxiv.org/abs/1307.1422) (JCAP 10 (2013) 018); Tan, Tsamis, Woodard, [arXiv:2107.13905](https://arxiv.org/abs/2107.13905) (Phil. Trans. R. Soc. A 380 (2021) 0187); Miao, Tsamis, Woodard, [arXiv:2409.12003](https://arxiv.org/abs/2409.12003) ("Leading Logarithm Quantum Gravity").

---

## Step 1 — identify the exact object

Tan-Tsamis-Woodard give this unambiguously: for a TT plane-wave graviton, **only one of the nine structure functions, \(T^2(x;x')\), survives the projection** ([arXiv:2103.08547](https://arxiv.org/pdf/2103.08547) §3.3.1, eq. 108). The quantum-corrected mode-function equation is

\[
-\tfrac12 a^2\big(\partial_0^2 + 2aH\partial_0 + k^2\big)u(\eta,k) = \int d^4x'\; iT^2(x;x')\,u(\eta',k)\,e^{-i\vec k\cdot\Delta\vec x}. \tag{eq. 109}
\]

This is exactly \(G_R^{TT}\)'s defining equation before assembly: \(T^2\) *is* the (gauge-fixed) retarded TT self-energy kernel your dispatch calls \(K_R\)/\(\Sigma_R^{TT}\). So the object in DISPATCH_ONE_PAGE.md and the object Tan-Tsamis-Woodard parameterize are the same object, modulo the assembly step. **Correction to log: this closes a gap the dispatch itself flagged ("has the pure-graviton TT observable even been computed") — it has, at the gauge-fixed level, and it has a name: \(T^2\).**

## Step 2 — is the gauge-fixed \(T^2\) secular, for a graviton-loop source?

Table 8 of 2103.08547 gives \(T^2_L\neq0\) explicitly (a rational function of \(\Delta\eta,\Delta x\), prefactor \(-\kappa^2/64\pi^4\)), i.e. the graviton-loop contribution to \(T^2\) **does** carry a \(\ln(H^2\Delta x^2)\) factor. The paper's own epilogue contrasts this against the *scalar-loop* contribution to the same \(T^2\), which is secular-free ("there are no changes in the graviton mode function" for an MMC-scalar loop, §5). Companion papers confirm this is not a fluke of the coincidence-limit tables: Mora-Tsamis-Woodard's Hartree treatment finds the mode function correction goes like \(GH^2\ln(a)/a^2\) ([1307.1422](https://arxiv.org/abs/1307.1422) abstract), and Tan-Tsamis-Woodard's exact (non-Hartree) treatment reports growth "enhanced by the square of the number of inflationary e-foldings" ([2107.13905](https://arxiv.org/abs/2107.13905) abstract) — a search-indexed excerpt gives the asymptotic form \(u_1\to \frac{\kappa^2H^2}{4\pi^2}u_0(0,k)\cdot\frac43\ln^2(a)\) (medium confidence — not independently re-verified against the full derivation in this session).

**Correction to log, higher-confidence part:** the "TT-frozen" possibility your STATE.md keeps open ("a frozen mode is equally consistent with trivial/no-response") **is not available for graviton-self-loop sources** — \(T^2\) is demonstrably nonzero and secular there, both in the exact one-loop coincidence-limit tables and in two independent companion-paper mode-function calculations. Freezing is only established for *scalar/matter-loop* sources, a different diagram class entirely. This resolves one binary the in-house probe had left open, in the direction *against* triviality (there is something here to resum), which is the less flattering direction per your own directional-optimism guard — reported as such.

## Step 3 — does this secular \(T^2\) survive gauge-invariant assembly?

This is where the attempt stops, and it stops for a *named, specific* reason, not a vague "it's hard."

Glavan-Miao-Prokopec-Woodard's 2026 result is exactly the precedent your dispatch cites: for a **scalar probe** (\(\Psi\) playing both source and observer), the one-graviton-loop self-mass is gauge-*dependent* under a Δα gauge variation until diagram classes 6, 7, and the external-mode-function correction \(\delta u = \delta u_I+\delta u_{II}\) are added — none of which existed in the pre-2026 literature ([2602.07908](https://arxiv.org/abs/2602.07908) §4, §8; Table 2's six-column cancellation, eq. 8.1). Their own words: *"unlike in flat space, additional diagrams and contributions are necessary, including the one-loop corrections to the external mode functions... In curved space, secular corrections to mode functions are possible; they combine with one-loop corrections to the amputated four-point function to yield a gauge-independent result."* That sentence is the load-bearing one: it says secular content **can be physical** post-assembly in de Sitter — assembly does not generically kill logs, it can also legitimate them. It also says the authors themselves do not yet know whether *their own* scalar-probe logs survive: *"Only once this is done will we have a definitive answer as to whether the large quantum-gravitational logarithms persist."*

Two things follow directly, and both are hard stops for an in-house attempt:

**(A) The source/observer/external-mode-function assembly has never been formulated for a graviton probe.** 2602.07908's whole construction is built around the massive scalar \(\Psi\) sitting at both ends of the exchange diagram; there is no graviton-probe analogue in this paper or (per the technical extraction) anywhere else located. Building one means re-deriving Table 2's six-column cancellation — classes 0–7 plus \(\delta u_{I,II}\) — with a graviton probe replacing \(\Psi\), which changes vertex Feynman rules, the reduction identities (§3, Donoghue identities), and very likely the diagram count (a graviton probe carries its own gauge freedom the scalar probe didn't). This is new technical work, not a reading exercise.

**(B) Even granting (A), \(T^2\)'s specific gauge-dependence under Δα/δβ has not been computed.** 2602.07908 proves cancellation for the *scalar self-mass*, not for \(T^2\). Nothing in the located literature shows whether \(T^2\)'s secular piece (Table 8) is itself gauge-artifact or gauge-invariant content. Kill-condition check (borrowing your own p_tt-interrogation discipline): claiming "the graviton-loop log in \(T^2\) survives assembly" *without doing (A) and re-running the Δα/δβ check on \(T^2\) specifically* would be exactly the kind of Ward-identity-over-reach / relocation-without-discharge your framework already forbids elsewhere (`NO_GO_LEDGER.md` entry 6; the p_tt interrogation's kill-condition 2). I am not making that claim.

## Step 4 — even granting assembly, is the resummation a pole or something else?

Also blocked, and also for a named reason. Miao-Tsamis-Woodard's 2024 paper ([2409.12003](https://arxiv.org/abs/2409.12003)) is the graviton-sector generalization of the Starobinsky-stochastic + dynamical-RG technique that would do this resummation — but the paper **derives the Langevin equation (the stochastic input) and explicitly stops there**: *"We must postpone the variant of the renormalization group analysis for pure gravity... implementing them is a considerable undertaking which we defer to a later work."* No resummed graviton two-point function or self-energy exists yet, by the authors' own statement. So even if (A) and (B) above were both discharged, the tool that would turn a confirmed secular \(T^2\) into an analytic-structure verdict (pole vs. cut) is itself unfinished machinery, not a solved problem being looked up.

## A third possibility your dispatch's binary doesn't name (flag only, not a finding)

The medium-confidence asymptotic form \(u_1\propto \ln^2(a)\) at *one* loop order (rather than the single \(\ln(a)\) per loop order that the standard Starobinsky-Yokoyama secular counting produces, e.g. in \(\lambda\phi^4\)) would, if confirmed, be structurally a *double*-logarithm at leading order — the same shape as a Sudakov form factor. Geometric resummation of single logs per order gives an exponential in cosmic time \(e^{-\gamma Ht}\) → a simple pole. Resummation of a genuine double-log-per-order tower instead points toward a Gaussian/super-exponential decay \(\sim e^{-c(Ht)^2}\), whose Fourier transform is an **entire function** — analytic everywhere, with neither a simple pole nor the kind of non-analytic branch cut "free-streaming" usually names. If this holds up under a real re-derivation, C1's pole-vs-cut framing would need a third box, not just a resolution one way or the other. Flagged here explicitly as unverified (the equation was recovered from a search-indexed snippet, not confirmed against the full derivation) — **not banked, not a claim**, just named so it isn't lost.

## Kill-condition checklist (run against this attempt itself)

1. **Circularity** — clean. \(T^2\)'s secular content is read directly off Tan-Tsamis-Woodard's own Table 8 and two companion mode-function results, not presupposed.
2. **Ward-identity over-reach** — clean. No claim here that diffeomorphism invariance alone decides pole vs. cut; the opposite point is made explicitly (gaps A/B/resummation are dynamical, not symmetry, questions).
3. **Adiabatic-mode relocation** — clean. The mode-function equation used (eq. 109) is the paper's own, not hand-inserted.
4. **Passivity misuse** — not invoked; no claim is derived from passivity alone.
5. **Consistency-of-consequences** — the one live risk is over-trusting the \(\ln^2(a)\) figure; it is explicitly held at flag-only, unbanked status for exactly this reason.

## Verdict

**C1 does not resolve.** What changes is the *quality* of "still open": before this attempt, the blocker was "the assembly doesn't exist, generically." After it, the blocker is two named, specific, uncompleted pieces of technical machinery —

- **(A)** a graviton-probe version of the Glavan-Miao-Prokopec-Woodard source/observer/external-mode-function assembly (2602.07908's method, never built for a graviton probe), and
- **(B)** completion of the Miao-Tsamis-Woodard graviton Langevin/DRG resummation ([2409.12003](https://arxiv.org/abs/2409.12003)'s own stated deferral) —

plus one correction with immediate value regardless of how C1 resolves: **the TT sector is not frozen for graviton-self-loop sources** (only for scalar-loop sources), so the "trivial/no-response" escape route your STATE.md kept open for the TT channel is closed. There is a real secular effect sitting in \(T^2\) waiting on (A) and (B), not nothing.

## Spec for a completion (unchanged in kind from the no-go ledger's style)

A completion needs, in order: (A) build the graviton-probe analogue of 2602.07908 Table 2's assembly and re-run its Δα/δβ cancellation check *on \(T^2\) specifically*, not on the scalar self-mass; (B) finish Miao-Tsamis-Woodard's deferred RG/Fokker-Planck step for the assembled kernel; then read the resummed kernel's ω→0 analytic structure. This is the actual content of the specialist dispatch — this attempt sharpens what is being asked for, it does not substitute for it.
