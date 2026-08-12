# One question about the pure-graviton de Sitter self-energy

> ## STATUS: HELD — DO NOT SEND AS WRITTEN (2026-08-10)
> **The ask's ω is pinned to cosmic time, and the audience-of-record corpus never uses that
> object.** Across ~200 pages of the relevant corpus (arXiv:2103.08547, 2107.13905, 2409.12003,
> 2507.04308, 2508.17787, 2601.12887, 2601.09309, 2501.05077) the terms `frequency`, `ω`,
> `Fourier`, `spectral`, `retarded`, `pole`, `branch cut`, `damping` all score **zero**. Three
> structural reasons, not oversight: (i) Σ(x;x′) is never reduced to a function of a time
> difference — no stationarity, no ω; (ii) the leading-logarithm truncation trades the two-time
> kernel for a local ODE in T = Ht; (iii) the stochastic field's band [H, Ha(t)] moves with
> absolute time. As posed, the question may be **ill-posed in this formalism**; a well-posed
> static-patch substitute (ω as the boost eigenvalue; QNM tower) is recorded as an open route in
> `provenance/prereg/RESULT_TERMINATION_events.txt` (2026-08-10 research note). HELD pending a
> re-pose; the C1 clock has not started.

*One page. The full technical brief (conventions, kill-conditions, riders) is attached as `SPECIALIST_BRIEF_rung3_spine.md` for anyone who wants it; nothing in it changes the question below.*

## The object

The **gauge-invariantly assembled, low-ω tensor (TT) spectral density of the pure-graviton one-loop de Sitter self-energy**:

ρ_TT(ω → 0) = 2 Im G_R^TT(ω),  equivalently  η = lim_{ω→0} Im G_R^TT(ω)/ω

— where G_R^TT is the retarded TT response obtained **after** (i) gauge-invariant assembly of source vertex + observer vertex + external-leg corrections, (ii) IR resummation, and (iii) analytic continuation to ω → 0. Throughout, ω is conjugate to **cosmic time** t (the comoving observer's proper time; ln a = Ht, exact on this computation's de Sitter background — the clock in which our secular-envelope dictionary and the KMS temperature T = H/2π are stated); if your assembly's natural clock differs, quote the verdict with its clock named.

## The specific open computation

**Does ρ_TT(ω→0) for the pure-graviton case have a single-pole (Markovian/Debye) structure, or a branch cut?** Concretely: after assembly and resummation, is the low-ω TT response analytic at ω = 0 with a finite η (pole class), or non-analytic (cut class — e.g. a secular-log structure that survives assembly)?

The three-step extraction above, in a universally accepted form, **does not yet exist for the pure-graviton case**. A secular ln(a) in the time domain is *not* an answer — steps (ii)–(iii) are exactly what separate a genuine spectral cut from a gauge/IR artifact, and the pure-graviton assembly has not been pushed through them.

## Where the computation stands (sharpened 2026-08-10, after an in-house assembly attempt — write-up available on request)

**The gauge-fixed kernel exists and has a name: T²(x;x′)** — Tan–Tsamis–Woodard show it is the single **coefficient function** contributing after TT projection (PDF p.23 = printed folio 22 — this register cites PDF pages for 2103.08547; the folio runs one behind: "the only one of the coefficient functions Tⁱ(x;x′) that contributes is T²(x;x′)"; the nine *structure* functions are T¹², T¹⁶, T¹⁸, T¹⁹, S², S⁴, S⁷, S⁸, S¹⁰, and eq. (81) makes T² a composite of six of them), with eq. (109) of arXiv:2103.08547 the quantum-corrected mode-function equation. **Caveat carried on the face (correction 2026-08-10b): the tabulated T² is the in-out (Feynman) object, not retarded** — the Schwinger–Keldysh conversion lives in arXiv:2107.13905 §2.2.3 (a different symbol, T²_SK; its eqs. (52)–(55) create the causal support and branch structure) — **and a position-space ln(H²∆x²) is not yet time-domain secularity** (that needs the x′ integration of eq. (109), which the paper's epilogue lists as not done). Its **graviton-loop contribution is nonzero and carries ln(H²∆x²)** (Table 8, all of whose entries carry that factor), while the analogous scalar-loop contributions (Table 6) are log-free — the same paper's "no changes in the graviton mode function" statement is explicitly scoped to the **scalar-loop** case (epilogue, citing Park–Woodard 2011). So there is secular content in the gauge-fixed TT kernel awaiting assembly and resummation — the question is not whether the kernel exists but what its content survives as.

**The two specific missing pieces** (named, not generic): **(A)** the gauge-invariant assembly of JHEP 04 (2026) 159 (arXiv:2602.07908) — source + observer + external-mode-function corrections — is constructed for a **scalar probe**; no graviton-probe version exists, and building one changes the vertex rules, the reduction identities, and plausibly the diagram count. **(B)** the resummation tool — **half-discharged (corrected 2026-08-10b)**: the 2409.12003 deferral was two-part, and the h_μ0 untangling half was **completed in arXiv:2507.04308** (Leading Logarithm Quantum Gravity II); the **RG half was not** — `renormalization group` occurs zero times in its 24 pages, its prerequisite is re-deferred, and the authors "enjoin caution." The bare de Donder self-energy is gauge-dependent in the relevant sector (how the gauge parameters affect the logarithm terms is stated as unknown in 2103.08547 §4.3), so the verdict cannot be read off the gauge-fixed object. To our knowledge, **nobody has posed the pole-vs-cut question in this assembled, low-ω form.**

**A third-outcome flag raised 2026-08-10 is RETIRED (2026-08-10b), reason on its face:** the flag inferred a possible Sudakov/entire-function endpoint from 2107.13905's "square of the number of e-foldings," read as a double log at one loop. Source verification kills the premise twice: arXiv:2601.12887 §4.1 eq. (44) gives u(t,k) = u₀(t,k){1 + (9/8)λ²T² + …} with λ ≡ κ²H²/3π² and T ≡ Ht (its eq. 23) — **λ² is two loops carrying two logs, i.e. one log per loop**, matching arXiv:2601.09309's stated counting rule for quantum gravity; and **the sign is positive — growth, not decay**. The inference chain fails at the counting step and at the sign step. Retired, not deleted, so no future pass re-raises it from the same misread.

## What a yes or a no does

We maintain a small research program (an open-system, finite-memory framing of the gravitational vacuum, audited claim-by-claim with every assumption priced). Its single load-bearing structural conjecture is that the vacuum's TT response is **single-pole** (finite memory). This is the one question the program cannot decide in-house — it is a genuine one-loop QFT-in-dS computation, not a modeling choice.

- **Pole class (finite η):** the program's core structural assumption is *earned* at one loop, and its remaining free scale becomes computable in principle.
- **Cut class:** the core assumption is **refuted** as stated — we retire it and say so; the program's ledger is built to take exactly this outcome.
- **A third clean outcome is also decisive:** if the spin-0 sector of the same assembled kernel is locked to the GR ratio (P⁰ˢ/P² = −2) by a Ward/constraint identity, that is a protecting-symmetry result we equally want to know (detail in the attached brief, Rider A).

Either way the answer is publishable stand-alone dS physics; our use of it is downstream and attributed.

**Contact:** Ryan Graver — ryngrvr@gmail.com. We will send the full brief, our conventions file, and our own partial computations (with their recorded dead-ends) on request.
