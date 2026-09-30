# SF-1 — FORMATION CHARTER 01 (CA-1 F conserved filling sectors)

**STATUS: FROZEN FOR EXECUTION (amended per `SF1_OWNER_RULING_01.md`, Issue #2 comment
`5903400225`).**

- **The frozen commit is the commit that introduces this revision.** CURRENT_STATE records its hash
  as the SF-1 frozen charter.
- **ONE execution is authorized.** A campaign-specific exception to the post-v4 in-house physics stop
  is granted for SF-1 only (ruling §6).
- **Draft history:** the draft was frozen at `f2177da`. The amendment log is §12.
- **Before this freeze:** no code was written, no member was computed, and no preview was run.
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
  - Boundary condition: **periodic**, c_L ≡ c_0 (OR-3, approved).
  - Hopping amplitude: 1.
  - Spinless fermions.
  - L is even.
  - Single-particle levels: ε(k) = −2 cos k at k = 2πj/L.
- **Not permitted:**
  - a chemical potential;
  - a filling-dependent or sector-specific coupling;
  - any other term;
  - a change of lattice, statistics, BC, hopping or readout.
- **One H builder:** a single function builds H_F, or its single-particle levels, for every sector
  (C-5).
- **Record identification:** this is the CA-1 F hopping h = −(S + S⁻¹) (`calc/ca1_carrier.py`
  `hop_op`, periodic), taken as a many-body parent.
- **RS-1's antiperiodic grid** (`calc/rs1_retained.py:59`) does not bind SF-1 and is not mixed in.

## §2 Sector selector and reference state (frozen)

- **Selector:** the exactly conserved N_F = Σ_j n_j, with [H_F, N_F] = 0. Initial/boundary data
  choose the sector. Nothing in the dynamics changes H_F.
- **Reference state |0_N⟩:** the lowest-energy eigenstate of H_F **within the sector N_F = N**.
  - This is a state declaration.
  - Generic unitary evolution does not relax to it, and no relaxation claim is made.
- **Odd-N convention (OR-3, approved):** every sector used has **N odd**, and there is no averaging
  over degenerate ground states.
- **Analytic odd-N control A-ODD (ruling §3), for every sector used:**
  - (i) The N lowest single-particle levels are exactly the symmetric set
    O_N = { k_j : j = −M … M }, with M = (N−1)/2. This is k = 0 plus the complete ±k pairs
    j = ±1 … ±M.
  - (ii) The level gap at the Fermi edge is strictly positive: ε(2π(M+1)/L) − ε(2πM/L) > 0. So no
    partially filled ±k pair remains.
  - (iii) **Odd-hole statement:** the complement (the holes) is symmetric about k = π and has odd
    size L − N. It is k = π plus complete pairs.
  - The run checks (i)–(iii) in exact integer/level arithmetic.
  - On the V-FOCK rings, the exact ground-state energy and uniqueness must agree with (i)–(ii).
  - **Any disagreement ⇒ RUN VOID.**

## §3 Sector families and L sequences (frozen; no tuning after results)

| Tag | Role | Sector rule | L sequence (frozen) |
|---|---|---|---|
| **D** | primary dense | N_L = L/2 (ν = 1/2) | L ∈ {258, 1026, 4098, 16386} (L ≡ 2 mod 4) |
| **E** | primary dilute | N_L = N₀ = 1 | L ∈ {256, 1024, 4096, 16384} |
| D-¼ | control C-2 | N_L = L/4 (ν = 1/4) | L ∈ {260, 1028, 4100, 16388} (L ≡ 4 mod 8) |
| D-¾ | control C-1 (PH of D-¼) | N_L = 3L/4 | same as D-¼ |
| E-3 | control C-3 | N_L = N₀ = 3 | same as E |
| Ē | control C-1 (PH of E) | N_L = L − 1 | same as E |
| **C-6** | **REPORT-ONLY crossover** | N_L = nearest odd(√L), ties to the lower odd | L = s² + 1, s ∈ {17, 33, 65, 129, 257}, i.e. L ∈ {290, 1090, 4226, 16642, 66050} |

- Every N_L in the table is odd.
- **For C-6:** √L = s + O(1/s) with s odd, so N_L = s, and no tie occurs.
- **The primary contrast is D vs E** (ν_L → 1/2 vs ν_L → 0).
- **Thermodynamic limit value k_F^∞ of the top occupied momentum k_F(L) = π(N_L − 1)/L:**
  - πν for D, D-¼ and D-¾;
  - 0 for E, E-3 and C-6;
  - π for Ē.

## §4 Retained observable and common operational object (frozen; one definition)

- **Readout** (identical in every sector): ρ_q = Σ_j e^{−iqj} n_j, with q = 2πm/L, m = 1 … L−1.
  - No string observable.
  - No sector-specific readout.
- **Common object:**

  S_{L,N}(q, ω) = (1/N) Σ_m |⟨m|ρ_q|0_N⟩|² δ(ω − (E_m − E_0))

  Invariants depend only on its **support**, so the normalization does not enter.
- **Finite-L support:**

  Σ_{L,N} = { (q, E_m − E_0) : weight > 10⁻¹² }

  The weight is summed over each degenerate eigenspace, which makes it basis-independent.
- **Finite-L lower edge:** ω⁻_{L,N}(q) = min { ω : (q, ω) ∈ Σ_{L,N} }.
- **Free-fermion identity I-FF (verified by V-FOCK, not assumed):**
  - Σ_{L,N} = { (q, ε(k+q) − ε(k)) : k ∈ occ, k+q ∉ occ }.
  - Each particle–hole state carries unit weight.
  - I-FF may be used at large L only after V-FOCK passes.

## §5 Common IR procedure and structural invariants (frozen; identical for every family)

**Prescription P (primary):**
1. Exact finite-L support.
2. L → ∞ along the declared sequence at fixed q ∈ (0, π]:
   ω⁻(q) := lim_L ω⁻_{L,N_L}(q_L), where q_L is the nearest grid momentum, with ties going to the
   lower m.
3. q → 0⁺.
4. z_P := lim_{q→0⁺} log ω⁻(q) / log q.

**Prescription P′ (C-4):**
- ω₁(L) := ω⁻_{L,N_L}(2π/L);
- z_{P′} := −lim_{L→∞} log ω₁(L) / log L.

**Invariants:**
- **I-z** (primary) := z_P.
- **I-q** (secondary) := n_soft = |Q_soft|, where

  Q_soft = { q* : lim_{q→q*} ω⁻(q) = 0 } **taken modulo q ~ −q ~ q + 2π** (ruling §4)

  - Each class is represented by its representative in [0, π].
  - q* = 0 is included via the one-sided limit.
  - C-1 verifies the quotient: the raw 2k_F-type representatives of D-¼ and D-¾ are reported
    alongside the folded sets.
- **Class of a family:** the pair **(I-z, I-q)**.

**Grade (SF-0 §2):**
- ω⁻(q), z_P, z_{P′} and Q_soft are obtained in **closed form**: symbolic limits of the I-FF support,
  with sympy allowed. Finite-L enumeration is a cross-check.
- **Numerical cross-check (frozen):**
  - At q ∈ {π/2, π/4, π/8, π/16, π/32}, for the largest L of each sequence:
    |ω⁻_{L,N_L}(q_L) − ω⁻(q)| ≤ 4·|k_F(L) − k_F^∞| + 20π/L.
  - ω₁(L) must match its closed form to 10⁻¹² (relative) at every L of every sequence.
  - **A mismatch in D, E, D-¼, D-¾, E-3 or Ē is an integrity failure ⇒ RUN VOID.**
  - For C-6 (report-only), a mismatch is reported and does not void the run.
- **Undefined limits:** a limit that does not exist in (0, ∞) makes that invariant **UNDEFINED.**
  Fitting is not allowed.

**Equivalence quotient:** SF-0 §3 unchanged.
- Exponents are invariant under constant rescalings.
- PH copies are quotiented.
- Densities alone do not count.

## §6 Controls (frozen)

| # | Control | Pass condition | Kind |
|---|---|---|---|
| **V-FOCK** | Build H_F **once** on the full 2^L Fock space (Jordan–Wigner signs, periodic bond included) for L ∈ {6, 10, 12}. Extract the sector blocks by N from that single matrix. Sectors: N ∈ {1, 3, L−3, L−1} for all L; N = L/2 for L ∈ {6, 10}; N ∈ {L/4, 3L/4} for L = 12. All q = 2πm/L. | Unique sector ground state (gap > 10⁻⁹). The grouped support set equals the I-FF enumeration (energies to 10⁻¹⁰, same membership). | integrity |
| **A-ODD** | §2 (i)–(iii) on every sector of every sequence, plus agreement with V-FOCK. | All hold; the analytic ground energy Σ_{O_N} ε equals the Fock E_0 to 10⁻¹⁰. | integrity |
| **C-1** | Particle–hole. (Fock) sector spectra and grouped ρ_q supports of N and L − N coincide on the V-FOCK rings. (Family) class(D-¼) = class(D-¾) and class(E) = class(Ē), after the I-q quotient. | All equal. | integrity |
| **C-2** | Two finite fillings. | class(D-¼) = class(D). | robustness |
| **C-3** | Two dilute N₀. | class(E-3) = class(E). | robustness |
| **C-4** | Limit order. | z_P = z_{P′} for each of D, E, D-¼, D-¾, E-3, Ē. | robustness |
| **C-5** | One H builder and one support/readout function serve every sector. Their source sha256 is recorded, and neither takes a family/sector tag argument. | Audit passes. | integrity |
| **C-6** | **REPORT-ONLY** crossover (ruling §2). Reports the exact k_F(L) = π(N_L−1)/L and its scaling; z_P; z_{P′}; and whether a unique one-parameter z exists. If none exists: **MULTISCALE / PATH-DEPENDENT IR.** | None. It **cannot assign or change the terminal** and is not a defect. | report |

## §7 Outcome classes and mechanical terminal (frozen)

**Physics terminals** (ruling §7):
- **FORMATION-OF-LAW-CLASS**, requiring all of:
  - same parent, generator, parameters and readout;
  - the sectors differ only through conserved data;
  - both families have well-defined persistent IR descriptions;
  - an SF-0 invariant differs after the quotient;
  - the difference survives the common prescription.
- **STATE-NOT-LAW.**
- **EDGE-ONLY-NONROBUST.**
- **SECTOR-SMUGGLED.**
- **UNFORMULABLE.**

**Procedural state:** **RUN VOID** (no physics terminal).

**Mechanical order** (the first matching step decides):

1. **RUN VOID** if any of these fails:
   - V-FOCK, A-ODD, C-1 or C-5;
   - a closed-form / numeric cross-check on a non-C-6 family.

   Then: preserve the artifact, identify the defect, no silent repair, no re-run without an owner
   ruling.
2. **SECTOR-SMUGGLED** if any step used a μ, a sector-specific H or readout, a changed BC or
   changed statistics.
3. **UNFORMULABLE** if any of:
   - class(D) or class(E) is undefined (I-z **and** I-q UNDEFINED);
   - under OR-1b narrowing, a class needed for C-2 or C-3 (D-¼, E-3) is undefined.
4. **STATE-NOT-LAW** if class(D) = class(E).
5. If class(D) ≠ class(E):
   - C-4 fails → **EDGE-ONLY-NONROBUST**;
   - otherwise C-2 or C-3 shows **well-defined but differing** classes → **EDGE-ONLY-NONROBUST**;
   - otherwise → **FORMATION-OF-LAW-CLASS**.

C-6 is read **after** the terminal and only shapes its wording (§11).

**Death conditions for FORMATION-OF-LAW-CLASS:**
- RUN VOID;
- class(D) = class(E);
- z_P ≠ z_{P′} in any non-C-6 family;
- D-¼ ≠ D;
- E-3 ≠ E;
- any parent or readout change.

A negative result is valid: **multiple sectors, one effective-law class.**

## §8 Expected identities (not assumed)

The owner's provisional expectations are:
- D: z = 1, two Fermi points;
- E: z = 2, band bottom.

No gate confirms them, and the procedure is fixed independently of them.

## §9 Artifacts

- `calc/sf1_formation.py`, one script, one run. It records the sha256 of its own source and of this
  charter.
- `SF1_FORMATION_RESULT.json`.
- `SF1_FORMATION_VERDICT_01.md`.
- Then **HARD STOP.**

## §10 Owner rulings on the former open items (`SF1_OWNER_RULING_01.md`)

- **OR-1: approved.**
  - Integrity failure = RUN VOID.
  - C-2/C-3 well-defined-but-different ⇒ EDGE-ONLY-NONROBUST; undefined ⇒ UNFORMULABLE.
- **OR-2: C-6 adopted, REPORT-ONLY.** A path-dependence is labelled MULTISCALE / PATH-DEPENDENT IR
  and cannot change the terminal.
- **OR-3: approved.** Periodic BC and the odd-N convention, plus the A-ODD analytic control.
- **I-q quotient:** q ~ −q ~ q + 2π, verified by C-1.

## §11 Interpretation fence (ruling §7, carried)

**Strongest allowed positive statement:**

> Within one fixed free-fermion microscopic parent, different exact conserved particle-number
> scaling sectors support inequivalent IR effective-law classes under the preregistered
> density-response coarse-graining.

If C-6 is path-dependent, append:

> The result concerns distinct asymptotic sector scalings; intermediate sub-extensive particle-number
> scalings form a crossover/multiscale regime rather than a third preregistered terminal class.

**Not claimed:**
- spontaneous universe formation or dynamical selection;
- domain formation;
- varying constants;
- a GRUT-substrate property;
- S-5 solved.

The sector is supplied by conserved boundary/state data. S-5 stays HELD. No SF-2.

## §12 Amendment log (draft `f2177da` → frozen revision)

| # | Change | Source |
|---|---|---|
| AM-1 | RUN VOID for integrity failure; C-2/C-3 narrowing (well-defined-but-different vs undefined) | ruling §1 |
| AM-2 | C-6 added as REPORT-ONLY. Family N_L = nearest odd(√L); L sequence frozen with s odd so no ties occur | ruling §2 |
| AM-3 | Periodic BC and odd-N frozen; RS-1 grid not mixed in | ruling §3 |
| AM-4 | A-ODD analytic control (symmetric fill; odd-hole statement; agreement with Fock or VOID) | ruling §3 |
| AM-5 | I-q quotient q ~ −q ~ q + 2π, verified by C-1 | ruling §4 |
| AM-6 | §10 open items replaced by the rulings | ruling §5 |
| AM-7 | **Auditor pre-freeze correction (disclosed):** numeric cross-check tolerance changed from 8π/L to 4·\|k_F(L) − k_F^∞\| + 20π/L. See the derivation below. | pre-freeze; no data |
| AM-8 | **Auditor pre-freeze specification (disclosed):** concrete L sequences frozen for every family. The draft said only "the declared sequence". Closed-form/numeric mismatch folded into RUN VOID, consistent with AM-1. Degenerate-eigenspace weight grouping specified for basis independence. | pre-freeze; no data |

**AM-7 derivation.** The draft bound 8π/L ignored the Lipschitz constants of
ω = ε(k+q) − ε(k): |∂_k ω| ≤ 4 and |∂_q ω| ≤ 2.
- Finite L displaces the allowed-k endpoint by at most |k_F(L) − k_F^∞| plus a grid offset of 3π/L.
- Finite L displaces q by at most π/L.
- Hence the bound 4|k_F(L) − k_F^∞| + 12π/L + 2π/L, rounded up to the frozen 20π/L term.

The tolerance was set from this bound alone, before any computation.
