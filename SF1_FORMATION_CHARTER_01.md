# SF-1 — FORMATION CHARTER 01 (CA-1 F conserved filling sectors)

**STATUS: DRAFT, FROZEN AT THIS COMMIT FOR OWNER REVIEW. NOT RUN. NOT EXECUTABLE.**
- **Authority:** `SF0_OWNER_RULING_01.md` §4 (Issue #2 comment `5903310812`): "Draft the SF-1
  charter only. No SF-1 physics run yet."
- **Execution needs a later owner authorization** that **explicitly grants the campaign-specific
  exception to the post-v4 in-house physics stop.** No such exception exists yet.
- **Before this draft:** no code was written, no member was computed, and no preview was run.
- **Carries SF-0 §§1–3 unchanged** (`SF0_PARENT_SECTOR_FORMATION_01.md`, `123abaa`).
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

> **Wording carried throughout:** SF-1 tests **formation-by-conserved-sector / boundary data, not
> attractor selection.** It tests a **sector-conditioned effective law, not dynamical
> thermalization.**

## §0 Question

For one fixed microscopic fermion parent, do two frozen families of exact particle-number sectors
carry inequivalent IR effective-law classes under one common IR procedure? The two families are the
dense family (ν > 0) and the dilute family (N fixed as L → ∞).

## §1 Parent (frozen)

- **One Hamiltonian:**

  H_F = − Σ_{j=0}^{L−1} ( c_j† c_{j+1} + c_{j+1}† c_j )

  - It acts on the **full fermionic Fock space** of the ring ℤ_L.
  - Boundary condition: **periodic**, c_L ≡ c_0.
  - Hopping amplitude: 1.
  - Spinless fermions.
- **Thermodynamic sequence:** the rings ℤ_L with **L even**, along the per-family sequences in §3.
- **Not permitted anywhere in SF-1:**
  - a chemical potential;
  - a filling-dependent or sector-specific coupling;
  - any other term;
  - a change of lattice, statistics, boundary condition, hopping or readout.
- **One H builder:** a single function constructs H_F (or its single-particle matrix) and is used
  for every sector. See control C-5.
- **Record identification:** this is the CA-1 F hopping h = −(S + S⁻¹) (`CA1_CARRIER_CHARTER_01.md`
  §1; `calc/ca1_carrier.py` `hop_op`, periodic), taken as a many-body parent.
- **Discrepancy disclosed:** RS-1's Lindhard computation used antiperiodic momenta k = 2π(j+½)/N
  (`calc/rs1_retained.py:59`). SF-1 follows the owner's "periodic ring" and does **not** inherit
  that choice. See OR-3.

## §2 Sector selector and reference state (frozen)

- **Selector:** the exactly conserved N_F = Σ_j n_j, with [H_F, N_F] = 0. Initial/boundary data
  choose the sector. Nothing in the dynamics changes H_F.
- **Reference state |0_N⟩:** the lowest-energy eigenstate of H_F **within the sector N_F = N**.
  - This is a state declaration.
  - Generic unitary evolution does not relax to it, and no relaxation claim is made.
- **Uniqueness convention (frozen; see OR-3):**
  - Every sector used has **N odd** (with L even).
  - Reason: under periodic BC, even N gives a degenerate sector ground state.
  - With N odd, the occupied single-particle momenta are k_j = 2πj/L, j = −(N−1)/2 … (N−1)/2.
    This set is nondegenerate because −2 cos k strictly increases in |k| on [0, π].
  - V-FOCK (§6) must confirm the uniqueness numerically. It is not assumed.

## §3 Sector families (frozen; no tuning after results)

| Tag | Role | Sector rule | L sequence | N parity |
|---|---|---|---|---|
| **D** | primary dense | N_L = L/2 (ν = 1/2) | L ≡ 2 (mod 4) | odd |
| **E** | primary dilute | N_L = N₀ = 1 | L even, L ≥ 8 | odd |
| D-¼ | control C-2 | N_L = L/4 (ν = 1/4) | L ≡ 4 (mod 8) | odd |
| D-¾ | control C-1 (PH of D-¼) | N_L = 3L/4 | L ≡ 4 (mod 8) | odd |
| E-3 | control C-3 | N_L = N₀ = 3 | L even, L ≥ 8 | odd |
| Ē | control C-1 (PH of E) | N_L = L − 1 | L even, L ≥ 8 | odd |

- **The primary contrast is D vs E:** ν_L → 1/2 versus ν_L → 0.
- ν = 1/2 is the value the record already uses (CA-1 F / RS-1).
- N₀ = 1 and N₀ = 3 are the two smallest odd values, chosen before any computation.

## §4 Retained observable and common operational object (frozen; one definition)

- **Readout** (identical in every sector): ρ_q = Σ_j e^{−iqj} n_j, with q = 2πm/L, m = 1 … L−1.
  - No bosonized or string observable.
  - No sector-specific readout.
- **Common object:** the per-particle dynamic structure factor of the reference state:

  S_{L,N}(q, ω) = (1/N) Σ_m |⟨m| ρ_q |0_N⟩|² δ(ω − (E_m − E_0)).

  - Every quantity below depends only on the **support** of S_{L,N}, so the 1/N normalization does
    not enter any invariant.
  - The normalization is fixed only so that the object is O(1) in both families.
- **Finite-L support:**

  Σ_{L,N} = { (q, E_m − E_0) : |⟨m|ρ_q|0_N⟩|² > 10⁻¹² }

  E_m ranges over all eigenstates of H_F in the same sector. ρ_q conserves N.
- **Finite-L lower edge:** ω⁻_{L,N}(q) = min { ω : (q, ω) ∈ Σ_{L,N} }.
- **Free-fermion identity I-FF (to be verified, not assumed):**
  - ρ_q|0_N⟩ = Σ_{k occ, k+q unocc} c†_{k+q} c_k |0_N⟩.
  - Each term is a single particle–hole state with |matrix element|² = 1 and energy
    ε(k+q) − ε(k), where ε(k) = −2 cos k.
  - So Σ_{L,N} = {(q, ε(k+q) − ε(k)) : k ∈ occ, k+q ∉ occ}.
  - The run may use I-FF at large L **only after** V-FOCK confirms it on the full Fock space.

## §5 Common IR procedure and structural invariants (frozen order; identical for every family)

**Prescription P (primary):**
1. Take the exact finite-L support Σ_{L,N} (§4).
2. Take the declared thermodynamic limit along the family's L sequence (§3), at fixed q ∈ (0, π]:
   ω⁻(q) := lim_{L→∞} ω⁻_{L,N_L}(q_L). Here q_L is the grid momentum 2πm/L nearest q (ties to the
   lower m).
3. Then take q → 0⁺.
4. z_P := lim_{q→0⁺} log ω⁻(q) / log q, the exponent of the leading nonzero behaviour of the lower
   support edge.

**Prescription P′ (limit-order control C-4):** joint scaling q = 2π/L:
- ω₁(L) := ω⁻_{L,N_L}(2π/L);
- z_{P′} := − lim_{L→∞} log ω₁(L) / log L along the same sequence.

**Invariants:**
- **I-z** (primary) := z_P.
- **I-q** (secondary) := n_soft, the number of distinct soft momenta
  Q_soft = { q* ∈ [0, π] : lim_{q→q*} ω⁻(q) = 0 }.
  - The limit at q* = 0 is one-sided, from q > 0.
  - This operationalizes "branch / low-energy excitation content" through the one common object.
- **Class of a family:** the pair **(I-z, I-q)**.

**Grade (SF-0 §2):**
- ω⁻(q), z_P, z_{P′} and Q_soft must be obtained in **closed form**: symbolic limits of the I-FF
  support, with sympy allowed.
- Finite-L enumeration is a **numerical cross-check only**. It passes if
  |ω⁻_{L,N_L}(q_L) − ω⁻(q)| ≤ 8π/L at q ∈ {π/2, π/4, π/8, π/16, π/32}, for the largest L of each
  sequence, with L ≥ 2¹².
- **A closed-form / numeric mismatch halts the run** and returns it to the owner.
- A limit that does not exist in (0, ∞) leaves that family's I-z **UNDEFINED.** Fitting is not
  allowed.

**Equivalence quotient:** SF-0 §3 unchanged.
- Constant rescalings of q, ω or units cannot change z_P, since exponents are rescaling-invariant.
- PH copies are quotiented (C-1).
- Basis changes do not count.
- Different densities alone do not count; only a change in (I-z, I-q) counts.

## §6 Controls (frozen)

| # | Control | Pass condition | Kind |
|---|---|---|---|
| **V-FOCK** | Full-Fock-space verification. Build H_F **once** on the 2^L Fock space for L ∈ {6, 10, 12}. Extract the sector blocks by N projection **from that single matrix**. Compute \|0_N⟩, uniqueness, E_m and ⟨m\|ρ_q\|0_N⟩. Sectors: N ∈ {1, 3, L−3, L−1} for all three L; N = L/2 for L ∈ {6, 10}; N ∈ {L/4, 3L/4} for L = 12. | Sector ground state nondegenerate (gap > 10⁻⁹). The support set equals the I-FF enumeration exactly (energies to 10⁻¹⁰, same membership). | integrity |
| **C-1** | Particle–hole. c_j → (−1)^j c_j† maps H_F → H_F (L even) and N → L − N; for q ≠ 0, ρ_q → −ρ_q. | D-¼ and D-¾ have the same class. E and Ē have the same class. | integrity (exact symmetry) |
| **C-2** | Two finite fillings. | D-¼ has the same class as D. | robustness |
| **C-3** | Dilute-family stability. | E-3 has the same class as E. | robustness |
| **C-4** | Limit order. | z_P = z_{P′} in each of D, E, D-¼, D-¾, E-3, Ē. | robustness |
| **C-5** | Common readout and parent. One H builder and one S/support function serve every sector. The run records the source hash of both and asserts that no sector-dependent branch exists in either. | Code audit passes. | integrity |

## §7 Outcome classes and mechanical terminal (frozen)

**Outcome classes (owner ruling §4.9):**
- **FORMATION-OF-LAW-CLASS**, requiring all of:
  - (1) the same parent, generator, parameters and readout;
  - (2) the sectors differ only through conserved state/boundary data;
  - (3) both families have well-defined persistent IR effective descriptions;
  - (4) at least one SF-0 invariant differs after the quotient;
  - (5) the difference survives the common thermodynamic/IR prescription.
- **STATE-NOT-LAW:** the fillings differ, but every invariant agrees.
- **EDGE-ONLY-NONROBUST:** a nominal z distinction appears only through incompatible limit orders or
  a singular zero-density prescription, and it disappears under the common scaling.
- **SECTOR-SMUGGLED:** the result needs a μ, a filling-dependent H, a different readout, different
  statistics or another microscopic change.
- **UNFORMULABLE:** no common retained-observable effective law can be defined across the families.

**Mechanical order** (the first matching step decides):

1. **Integrity.** If V-FOCK, C-1 or C-5 fails, the **RUN IS VOID**. No terminal is assigned; the run
   returns to the owner, and there is no re-run without a ruling. (OR-1: this procedural status is a
   charter addition for owner approval.)
2. **SECTOR-SMUGGLED** if the C-5 audit or the record shows that any step used a μ, a
   sector-specific H or readout, a changed BC or a changed statistics.
3. **UNFORMULABLE** if I-z **and** I-q are UNDEFINED for D or for E.
4. **STATE-NOT-LAW** if class(D) = class(E).
5. If class(D) ≠ class(E):
   - C-4 fails → **EDGE-ONLY-NONROBUST**;
   - otherwise C-2 or C-3 fails → **EDGE-ONLY-NONROBUST** (OR-1: mapping proposed for owner
     confirmation);
   - otherwise → **FORMATION-OF-LAW-CLASS**.

**Death conditions** (any one kills FORMATION-OF-LAW-CLASS):
- a void run;
- a closed-form / numeric mismatch not resolved by owner ruling;
- class(D) = class(E);
- z_P ≠ z_{P′} in any family;
- D-¼ ≠ D;
- E-3 ≠ E;
- any parent/readout change.

A negative result is valid: **multiple sectors, one effective-law class.**

## §8 Expected identities (not assumed)

The owner's ruling states the provisional expectations:
- D: two Fermi points, linear density excitations, z = 1.
- E: band-bottom quadratic excitations, z = 2.

These are **not** encoded as passed facts, and no gate is written to confirm them. The procedure in
§§4–7 is fixed independently of them.

## §9 Artifacts at execution (not created now)

- `calc/sf1_formation.py`, one script. It freezes its constants by sha before the run.
- `SF1_FORMATION_RESULT.json`.
- `SF1_FORMATION_VERDICT_01.md`.
- One run, then the verdict, then HARD STOP.

## §10 Open items for owner review (before freezing for execution)

- **OR-1. Procedural mappings.** Two items are not in the ruling:
  - the "RUN VOID" status on an integrity failure;
  - the mapping of a C-2/C-3 failure to EDGE-ONLY-NONROBUST. (Its alternative is UNFORMULABLE for
    a family whose class is not stable.)
- **OR-2. Optional hostile control C-6: sub-extensive families,** N_L ≈ L^α with 0 < α < 1 (for
  example α = 1/2, rounded to the nearest odd N).
  - D and E do not sample the crossover region between them, where ν_L → 0 while N_L → ∞.
  - C-6 would test whether the D/E contrast is a robust two-class statement or depends on N staying
    finite.
  - **Auditor's unverified analytic expectation, disclosed rather than hidden: P and P′ may disagree
    on such families.** That is why it is offered.
  - If adopted, the owner must freeze its effect before the run. Options:
    - report-only scope data that cannot change the terminal;
    - a P/P′ divergence there triggers EDGE-ONLY-NONROBUST.
- **OR-3. Boundary condition and parity convention:**
  - periodic BC (per the ruling) instead of RS-1's antiperiodic momenta;
  - odd-N sectors only, for a unique reference state. The alternative for even N is an average
    over the degenerate ground manifold.

## §11 Interpretation fence (ruling §5, carried)

A FORMATION-OF-LAW-CLASS result would establish only:

> one known microscopic parent supports more than one inequivalent low-energy effective-law class
> depending on a conserved boundary/state sector.

It would not establish any of the following:
- multiple universes;
- domain formation;
- varying constants;
- cross-universe mixing;
- the origin of constants;
- that GRUT's substrate has this property;
- a solution of S-5.

S-5 stays HELD. No SF-2, domain mixing or empirical claim.
