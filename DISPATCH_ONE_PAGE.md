# One question about the pure-graviton de Sitter self-energy

*One page. The full technical brief (conventions, kill-conditions, riders) is attached as `SPECIALIST_BRIEF_rung3_spine.md` for anyone who wants it; nothing in it changes the question below.*

## The object

The **gauge-invariantly assembled, low-ω tensor (TT) spectral density of the pure-graviton one-loop de Sitter self-energy**:

ρ_TT(ω → 0) = 2 Im G_R^TT(ω),  equivalently  η = lim_{ω→0} Im G_R^TT(ω)/ω

— where G_R^TT is the retarded TT response obtained **after** (i) gauge-invariant assembly of source vertex + observer vertex + external-leg corrections, (ii) IR resummation, and (iii) analytic continuation to ω → 0. Throughout, ω is conjugate to **cosmic time** t (the comoving observer's proper time; ln a = Ht, exact on this computation's de Sitter background — the clock in which our secular-envelope dictionary and the KMS temperature T = H/2π are stated); if your assembly's natural clock differs, quote the verdict with its clock named.

## The specific open computation

**Does ρ_TT(ω→0) for the pure-graviton case have a single-pole (Markovian/Debye) structure, or a branch cut?** Concretely: after assembly and resummation, is the low-ω TT response analytic at ω = 0 with a finite η (pole class), or non-analytic (cut class — e.g. a secular-log structure that survives assembly)?

The three-step extraction above, in a universally accepted form, **does not yet exist for the pure-graviton case**. A secular ln(a) in the time domain is *not* an answer — steps (ii)–(iii) are exactly what separate a genuine spectral cut from a gauge/IR artifact, and the pure-graviton assembly has not been pushed through them.

## Where the computation stands (sharpened 2026-08-10, after an in-house assembly attempt — write-up available on request)

**The gauge-fixed kernel exists and has a name: T²(x;x′)** — Tan–Tsamis–Woodard show it is the single structure function surviving TT projection, with eq. (109) of arXiv:2103.08547 the quantum-corrected mode-function equation. Its **graviton-loop contribution is nonzero and carries ln(H²∆x²)** (Table 8, all of whose entries carry that factor), while the analogous scalar-loop contributions (Table 6) are log-free — the same paper's "no changes in the graviton mode function" statement is explicitly scoped to the **scalar-loop** case (epilogue, citing Park–Woodard 2011). So there is secular content in the gauge-fixed TT kernel awaiting assembly and resummation — the question is not whether the kernel exists but what its content survives as.

**The two specific missing pieces** (named, not generic): **(A)** the gauge-invariant assembly of JHEP 04 (2026) 159 (arXiv:2602.07908) — source + observer + external-mode-function corrections — is constructed for a **scalar probe**; no graviton-probe version exists, and building one changes the vertex rules, the reduction identities, and plausibly the diagram count. **(B)** the resummation tool: arXiv:2409.12003 derives the graviton-sector **Langevin input**; the RG completion that would convert a confirmed secular kernel into an ω→0 analytic-structure verdict is not in the record we could locate. The bare de Donder self-energy is gauge-dependent in the relevant sector (how the gauge parameters affect the logarithm terms is stated as unknown in 2103.08547 §4.3), so the verdict cannot be read off the gauge-fixed object. To our knowledge, **nobody has posed the pole-vs-cut question in this assembled, low-ω form.**

**One flag on the binary itself, offered with its confidence stated:** arXiv:2107.13905's own abstract reports one-loop corrections to gravitational-radiation propagation "enhanced by the **square** of the number of inflationary e-foldings" — a double logarithm at one loop. We have not verified the coefficient against the derivation, nor whether it survives assembly; but if a genuine double-log-per-order tower is what resums, the natural endpoint is Sudakov-type Gaussian decay in cosmic time — an **entire function** at ω = 0, neither pole nor cut. If you know this either way, one line in your reply saves the question from a false binary.

## What a yes or a no does

We maintain a small research program (an open-system, finite-memory framing of the gravitational vacuum, audited claim-by-claim with every assumption priced). Its single load-bearing structural conjecture is that the vacuum's TT response is **single-pole** (finite memory). This is the one question the program cannot decide in-house — it is a genuine one-loop QFT-in-dS computation, not a modeling choice.

- **Pole class (finite η):** the program's core structural assumption is *earned* at one loop, and its remaining free scale becomes computable in principle.
- **Cut class:** the core assumption is **refuted** as stated — we retire it and say so; the program's ledger is built to take exactly this outcome.
- **A third clean outcome is also decisive:** if the spin-0 sector of the same assembled kernel is locked to the GR ratio (P⁰ˢ/P² = −2) by a Ward/constraint identity, that is a protecting-symmetry result we equally want to know (detail in the attached brief, Rider A).

Either way the answer is publishable stand-alone dS physics; our use of it is downstream and attributed.

**Contact:** Ryan Graver — ryngrvr@gmail.com. We will send the full brief, our conventions file, and our own partial computations (with their recorded dead-ends) on request.
