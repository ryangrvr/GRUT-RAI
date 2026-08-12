# The arrow of time — attacked: result

**Date:** 2026-06-25 · **Code:** `calc/arrow_origin.py` (exactly-solvable demonstration) +
7-agent adversarial workflow (steelman-intrinsic, 3 source-traces, primary-source verifier,
synthesis, anti-laundering critic). Register claim: `arrow_of_time`.
**Verdict: imported — initial-condition. Confidence high (on the decisive leg).**

## The decisive cut: EXISTENCE vs DIRECTION
The steelman built the strongest intrinsic case, then broke it on exactly this seam:

- **EXISTENCE / magnitude of dissipation is intrinsic.** The in-in/CTP influence functional gives
  a retarded analytic self-energy, a positive Källén-Lehmann spectral measure, and a positive
  noise kernel — operator-identically, with **no low-entropy *system* initial state needed.**
  That is the genuine, narrow win.
- **DIRECTION is imported.** None of the above fix the *sign* of relaxation — they fix |Im Σ_R|,
  not which way it runs. The direction comes from low-entropy data on the **past boundary**, in
  three interchangeable guises that reduce to **one** initial-condition assumption:
  1. the **past-endpoint contour** convention (where ρ is specified);
  2. **decisive — passivity / KMS β>0 of the bath state.** Pusz-Woronowicz (1978): KMS β>0 ≡
     passivity ≡ "no work extractable" ≡ the second law as a *state property*. sign(β) in
     coth(βω/2) alone decides damp vs anti-damp; a legal β<0 (population-inverted) KMS state
     **reverses the arrow.** Positivity never fixes this.
  3. **factorization** ρ_S⊗ρ_B — the quantum Stosszahlansatz (Nakajima-Zwanzig: the closed
     dissipative master equation is the Qρ(0)=0 *deletion*, an artifact of that choice).

## The toy demonstration (independent-boson dephasing, exactly solvable)
- Γ(t) = Γ(−t) **exactly** → the dynamics carry no preferred direction.
- |L(t)| decays to ~0.03 and **returns to exactly 1.0000** at t_rec → reversible.
- t_rec ∝ N → monotone decay exists only in the continuum limit (an assumption).
- Decay set by coth(ω/2T) — i.e. by the **assumed bath state** (β>0). (This is the passivity
  input, made concrete: my T>0 bath *is* the β>0 passive state the synthesis pins the direction to.)

## Primary-source verification (all confirmed)
- Feynman-Vernon (1963) assumes a factorized initial state (Aurell et al., J. Phys. A 2020).
- Finite baths recur (Poincaré); irreversibility needs the continuum limit (Caldeira-Leggett 1983;
  Ponomarev et al. 2012).
- The uncorrelated initial state = Boltzmann's Stosszahlansatz: **the arrow reverses for entangled
  initial states** (Partovi, PRE 77 021110, 2008); the δρ(0)=0 step is the irreversibility-generator
  in Mori-Zwanzig (te Vrugt 2022, citing Zeh).
- **No derivation escapes** a low-entropy/typicality input — Bogoliubov weakening-of-correlations
  and ETH/typicality merely **relocate** it (REFUTED that any escapes).

## Anti-laundering audit (passed, with one tightening)
The verdict is structurally anti-laundering: it never lets "factorization is the natural
preparation" or "the passive bath is physically reasonable" count as *derived* — naturalness is
downstream of the Past Hypothesis (Zeh; Price's double-standard critique). The critic's one
sharpening makes the import **more** total, not less: even the "intrinsic" positivity is proven
relative to a passive/stable reference state, so the passive-state assumption co-supplies part of
what looked dynamics-intrinsic.

## What GRUT actually is (the floor — and it is honorable)
GRUT does **not** derive the arrow. Its genuine, defensible contribution is **methodological**:
the existence-vs-direction decomposition, and the triangulation showing the three guises are one
initial-condition assumption that no known derivation escapes. That is a real, clarifying
contribution to the Albert/Price/Carroll problem — *here is exactly where, and in what form, the
arrow is assumed* — not "GRUT solves the arrow." Ledger **+1**: the passive low-entropy
past-boundary state (the Past Hypothesis), named, not laundered.

## Ceiling-check — ANSWERED by the specialist (2026-06-25), and it closes the arrow
**Question:** Holding dynamics, contour, and positivity fixed, is there any non-passive (not
KMS-β>0) bath state giving monotone forward relaxation — or does direction provably track sign(β)
alone?

**Answer: NO, sign(β) alone does not generally fix the direction — and the loop over-reached in
claiming it did.** The honest scope:
- **Within the equilibrium KMS class** (which *is* GRUT's assumed vacuum, via the rung-2 KMS/FDT
  gate): yes, detailed-balance direction is fixed by sign(β); the β>0 reading is sound for GRUT.
- **Outside KMS** (squeezed, driven-Floquet, active, nonthermal-Gaussian baths — and GRUT's own
  FDT-broken out-of-equilibrium regime at rung 7): there is **no single β**. N(ω) and Im[χ]
  decouple; the reduced dynamics still relax — but to a **nonequilibrium steady state**, with the
  direction set by the **full Liouvillian / stationary state / frequency-dependent rate
  asymmetry**, not a temperature scalar.

**Either way, the direction is imported from the assumed bath state, never from the time-symmetric
dynamics.** So the intrinsic-arrow **ceiling is closed**: there is no dynamics-only or
single-scalar route to a direction. The over-general "sign(β) alone" is demoted to its KMS scope;
the verdict (existence intrinsic, direction imported) stands and is reinforced. The in-in formalism
is the right *tool* — it cleanly separates intrinsic existence from imported direction and handles
both KMS and NESS baths — but it does **not solve** the arrow. The firewall caught a genuine
over-generalization on the very last question; the floor is the final answer.
