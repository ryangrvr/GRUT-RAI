# RELATIONAL-vs-MEDIUM DISCRIMINATOR — D-1 CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner
(`RELATIONAL_ONTOLOGY_OWNER_RULING_01.md` §4), question verbatim: *"Can two
theories with the same K(t,t′), same effective observables, and different
microscopic interpretations of that kernel be experimentally or
mathematically distinguished at all?"* — with the owner's own decision rule:
NO → the dispute is representational, both vocabularies discarded as
fundamental; YES → a genuine ontology-level discriminator exists.

**Scope (fixed):** the exactly solvable Gaussian class, where the question
is decidable — the Feynman–Vernon influence functional of a Gaussian bath is
determined by the kernel pair **(K, N)** (retarded/dissipation and
noise/fluctuation) and nothing else, so "same effective observables" can be
made precise and tested rather than assumed. Recorded anchor: the T2 chain's
facts that **G_R is state-independent while the noise kernel is
state-dependent** — "same K" does not exhaust observable content; (K, N) is
the natural equivalence-class label. Register untouched; ledger 0; fenced
routes untouched; no prediction campaign.

## 1. THE WORLDS (frozen; S = one site, ω_S = 1; M = 8 bath modes; ħ = 1)

- **W-A (star / "medium" representation):** S coupled directly to M
  independent bath modes, frequencies ω_μ spread over [0.4, 2.2], couplings
  c_μ (declared arrays in the instrument), bath in its ground state.
- **W-B (chain / relational-looking representation of the SAME theory):**
  the exact Lanczos tridiagonalization of W-A's bath started from the
  normalized coupling vector — an E-orthogonal transformation, so K and N
  are preserved identically and the two are **isomorphic** as abstract
  theories. Role: the *representational-choice exemplar*.
- **W-B′ (distinct micro-theory, same influence data):** W-B plus **two
  decoupled hidden modes** (different dimension, different full spectrum) —
  genuinely non-isomorphic to W-A, with identical (K, N). Role: the
  *underdetermination exemplar*.
- **W-D (same K, different state):** W-A's Hamiltonian with the bath in a
  **thermal state at T = 0.8** — K identical (state-independence), N
  different. Role: the *noise-channel discriminator exemplar*.
- **W-B″ (sensitivity control):** W-B with one Lanczos coefficient
  perturbed by 1% — K differs; the access-level metrics MUST detect it or
  the run HALTS (dull-metric guard).

## 2. ACCESS LEVELS AND METRICS (frozen)

Exact covariance evolution σ(t) of the full closed system from the product
initial state (S ground ⊗ declared bath state), reduced to the access set;
time grid t ∈ [0, 30], 300 points.

- **L1 — S-local access:** Δ₁(X, Y) = max_t ‖σ_SS^X(t) − σ_SS^Y(t)‖_F,
  normalized by max_t ‖σ_SS^A(t)‖_F.
- **L2 — enlarged non-E access:** attach a probe oscillator (ω_p = 0.7,
  spring 0.05 to S, ground state) to both worlds; Δ₂ = the same metric on
  the (S+probe) block.
- **L3 — full-theory invariants:** dimension; sorted spectrum of V (compared
  as multisets, tolerance 1e-9); K-kernel identity check
  Δ_K = max_t |K^X(t) − K^Y(t)| / max|K^A|.
- **Equality threshold** ε = 1e-8 (relative); **detection threshold**
  δ = 1e-3 (relative). Both frozen now.

## 3. PRE-REGISTERED CLASSIFICATION (mechanical)

- **E1 (underdetermination established):** Δ_K(A,B′) < ε AND Δ₁(A,B′) < ε
  AND Δ₂(A,B′) < ε while L3 invariants differ (dimension/spectrum) —
  same-(K,N) micro-distinct theories are S-indistinguishable at every
  tested access level.
- **E2 (noise channel discriminates):** Δ_K(A,D) < ε while Δ₁(A,D) > δ —
  kernel-equal theories with different fluctuation data ARE S-distinguishable.
- **E3 (sensitivity):** Δ₁(A,B″) > δ — the metrics detect a 1% influence-
  data difference (else HALT, metrics too dull to support any verdict).
- **E4 (representation check):** Δ_K, Δ₁, Δ₂ (A,B) < ε and L3 invariants
  IDENTICAL — the star/chain pair is one theory twice.

**Answer to the owner's question, assembled mechanically:**
- If E1–E4 all hold: **"NO at fixed influence data (K, N) and S-limited
  access; YES across influence-data classes."** Consequence, per the
  owner's own rule applied at this scope: the medium-vs-relational dispute
  is **representational at fixed (K, N)** — both vocabularies are discarded
  as fundamental *at that level* — and any genuine ontology-level
  discriminator must live in **what constrains the (K, N) pair** (e.g.,
  KMS/FDT-class relations between dissipation and fluctuation), not in the
  kernel alone.
- If E1 fails: same-(K,N) theories were distinguished — a genuine
  discriminator exists inside the tested class; report which observable.
- If E2 fails: even the noise channel does not discriminate — the
  equivalence class is larger than (K, N); report.

**Honesty riders (frozen):** the verdict is class-scoped (Gaussian, finite,
factorized initial state); the pointer from E2 to the gravitational sector
(the recorded state-dependence of N and the O(H²) FDT/KMS obstruction) is a
POINTER, not a computation — the noise-sector fork stays owner-held and no
GRUT-chain noise computation is run.

## 4. DELIVERABLES AND STOP

1. `calc/discriminator_d1.py` (pure stdlib, self-checking; emits
   `DISCRIMINATOR_D1_RESULT.json`, sha-hashed).
2. `DISCRIMINATOR_VERDICT_01.md` — the answer in the owner's YES/NO form
   with its scope, and what it does to the two vocabularies.
3. **HARD STOP at the verdict** (waiting decision: the owner rules on the
   vocabularies and orders P-2 or otherwise). Fenced routes untouched.
