# S2 — OWNER RULING 03 (S2-1 terminal accepted; S2-HB boundary audit opened)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5909019588`**, after review of
`64d9cc9` (corrective provenance), `de6eb46` (corrective result and verdict), `227dd09` (charter) and
`32645cc` (derivation). The comment is authoritative; this file records it.

## 1. Terminal: ACCEPTED

- **S2-1 = FULL-DISCRIMINATOR-CONFIRMED**, at the frozen S2-1 scope.
- The first execution stays **permanently RUN VOID** and contributes no physics terminal.
- **The corrective execution is the adjudicating artifact.**

## 2. Corrective provenance: accepted

- **Preserved history:** `e92cf29`, `81b4f8f`, `227dd09` and `32645cc`.
- **The patch at `64d9cc9`:** three exact-rational `nsimplify` uses were replaced by literal exact
  arithmetic, and the output filename was redirected.
- The redirect is **provenance-only** and consistent with preserving the RUN VOID artifact.
- **No physics object, member, predicate, coefficient, terminal rule or theorem-bearing expression
  changed.**

## 3. Execution controls: PASS

- **I-1 … I-5 all pass together in one artifact:** E-3, E-1, every member, E-2/I-5,
  `all_checks_pass = true`, `defects = []`, exact rationals throughout.
- **No third execution is needed or authorized.**

## 4. Coefficient theorem: ACCEPTED

- Δc₂ = −24βT₁a, so m₁^𝒮 − m₁^𝒟 = −12βT₁a·t² + O(t³).
- Δc₃ = 24βT₁a(44βa² + 5K₁₁).
- **The leading discriminator is local to the retained noise amplitude T₁.**

## 5. HT-B: ACCEPTED; T-HT CLOSED

The hypothesis covers every preparation-independent hidden law on the same state space with O-1
defined.
- **Step A** forces ξ₁ = 0 a.s. without higher moments.
- **Step B:** hidden uncertainty changes the ± pair difference only by o(t²), whereas forcing
  supplies −24βT₁a·t².

Conclusion: **no such ν reproduces the frozen C-B map when β > 0 and T₁ > 0. HT-B closes T-HT, and
there is no HT-C counterexample at this scope.**

## 6. The accepted scientific statement

> **Within the declared nonlinear C-B class, ongoing stochastic forcing is observationally
> distinguishable in the retained mean-response map from uncertainty confined to the initial
> condition on the same deterministic state space.**

- **In short:** ongoing forcing ≠ initial uncertainty only, for the frozen C-B comparison.
- **Mechanism:** noise-generated spread + drift curvature → mean-response structure.
- **This is the first accepted break of the S-1 equivalence in the hard stochastic class.**

## 7. Report-only order-4 findings: ACCEPTED AS DIAGNOSTICS

- **G(∞)** (T₁ = 0): Δc₂ = Δc₃ = 0, and **Δc₄ = −(48/11)aβ**. Remote noise first reaches the retained
  mean at fourth order.
- **F vs GR(∞):** they agree through Δc₃ and first differ at Δc₄.
- **Reading:**

  > **The earliest response correction is controlled by local retained-site noise, while remote
  > profile structure enters later through deterministic propagation.**

- **Not a finite-time dominance theorem.** No remainder bound was chartered.

## 8. What S2-1 changes: a class split

- The S-1 linear statement stays valid at its scope: a linear drift gives mean closure and
  initial-ensemble equivalence on the tested objects.
- **That equivalence is not structurally stable under nonlinear drift.**
- **The dividing mechanism:** noise reaches nonlinear curvature, which opens the moment hierarchy and
  changes the retained mean. It is not Gaussian vs non-Gaussian noise, not Itô vs Stratonovich, and
  not "noise itself".

| Drift | Effect of ongoing noise |
|---|---|
| **Linear canonical** | Ongoing martingale noise is invisible to the frozen mean-response object. |
| **Nonlinear curved** | Ongoing additive noise can become visible already in the retained mean response. |

## 9. Not established

- noise is ontologically fundamental, or GRUT requires primitive randomness;
- deterministic physics cannot reproduce the stochastic process;
- a larger hidden environment cannot reproduce the reduced law;
- quantum outcomes, Born probabilities or collapse;
- the L0-1c drift is derived.

**The excluded alternative is exactly:** the same deterministic state space plus a random initial
condition only. **The enlarged deterministic environment remains open.**

## 10. The S-2 architecture

1. **S-1 (linear class):** initial-uncertainty equivalence.
2. **S2-0:** CLASS-SPLIT.
3. **S2-1:** FULL-DISCRIMINATOR-CONFIRMED.

> **Initial uncertainty alone cannot replace ongoing noise once the declared nonlinear drift couples
> noise-generated spread into the retained mean.** This is an accepted result.

## 11. Next: S2-HB, the enlarged deterministic / Hamiltonian-bath boundary (audit/formulation only)

- **Do not declare noise primitive yet.**
- **Question:**

  > **Can the C-B reduced stochastic response be reproduced by deterministic evolution on a larger
  > state space whose hidden environmental degrees of freedom are randomized only at the initial
  > time?**

- **File:** `S2_HAMILTONIAN_BATH_BOUNDARY_01.md`. No physics run and no v4 exception.

**11.1 The critical distinction:**
- **HB-U, unrestricted deterministic enlargement.** An entire driving history or path is placed in
  the hidden state and evolved deterministically. This is a mathematical realization theorem, not a
  physical bath derivation. Audit whether the record already contains an equivalent dilation or
  path-space statement.
- **HB-P, a physically constrained deterministic parent.**

  > Can a **local, autonomous, physically declared conservative/Hamiltonian parent**, with
  > randomness only in its initial environmental state, reproduce the C-B retained response law
  > without inserting a stochastic path as hidden initial data?

  This is the branch that can bear on GRUT. **A trivial path-space encoding must not count as HB-P.**

**11.2 Audit targets:**
- the S-1 Hamiltonian-bath / Gaussian realization;
- O-6;
- S5-1;
- the Sz.-Nagy / conservative dilations;
- the Koopman / KvN realizations;
- L0-1e;
- any CTP / influence-functional records;
- the declared FDT / KMS structures.

**Nine questions per candidate:**
1. Is the evolution deterministic?
2. Is it autonomous?
3. Is it Hamiltonian/symplectic, or only measure-preserving / a path shift?
4. Is the randomness confined to the initial hidden state?
5. Is it independent of the preparation a?
6. Does it reproduce second-order statistics only, or the **full C-B retained mean-response map**?
7. Does it need infinitely many hidden degrees of freedom?
8. Does it encode the future noise history in the initial state?
9. Is it already declared, merely possible by a general theorem, or absent?

**11.3 No-triviality rule.** A hidden variable equal to the whole Wiener trajectory, evolved by the
path-space shift, is classified as **UNRESTRICTED-REALIZATION**, not as a physical derivation of
noise.

**11.4 Frozen outcomes (pre-register before inspection):**

| Outcome | Condition |
|---|---|
| **PHYSICAL-BATH-ALREADY-REALIZES** | a declared Hamiltonian/conservative parent reproduces the C-B map at the required scope |
| **FORMULABLE-PHYSICAL-BATH-TEST** | no proof exists, but a declared physical parent supplies a clean executable test |
| **UNRESTRICTED-REALIZATION-ONLY** | enlargement exists only via a path-space or dilation representation |
| **SECOND-ORDER-ONLY** | declared baths reproduce the linear/Gaussian second-order class, but nothing reaches the nonlinear C-B discriminator |
| **NO-PHYSICAL-BATH-CANDIDATE** | no declared conservative/Hamiltonian parent can even formulate the test without new structure |
| **UNFORMULABLE** | |

**No new bath may be invented.**

## 12. Why S2-HB is next

- **Eliminated:** same-state-space initial randomness. **Not eliminated:** hidden deterministic
  environmental degrees of freedom.
- The logic is now:
  - same-state-space uncertainty: **NO**;
  - enlarged deterministic physical bath: **?**
- Only after this boundary is resolved would "primitive noise" language make sense.

## 13. Actions / HARD STOP

**Create:**
- this ruling;
- the verdict-02 banner;
- `S2_NOISE_ORIGIN_DEPOSIT_01.md`;
- the CURRENT_STATE update;
- the S2-HB pre-registration;
- the read-only audit.

Then **HARD STOP.**

**Not authorized:**
- an S2-HB physics run;
- S-3, the reversal diagnostic, S-6;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

> **Summary:** GRUT has now shown that ongoing noise cannot be replaced by initial uncertainty on the
> same nonlinear state space. The remaining noise-origin question is whether a larger deterministic
> physical environment can reproduce the same reduced dynamics.
