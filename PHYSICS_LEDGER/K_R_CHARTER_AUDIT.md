# K_R CHARTER AUDIT — what K_R is, what depends on it, and the minimum valid construction

**Date:** 2026-08-30 · Document/charter work ONLY. **No K_R computation
occurred.** No frozen artifact modified. Baseline: Wall-A closure `c1c3f51`;
frozen kernel `dd77b1943e2068c6…888c4ae1`; register `a70a2ad1…` (read-only;
the +1 remains a completed ruling and is not reopened here).
**Companion:** `K_R_DEPENDENCY_MAP.json`.

---

## 1. What K_R is — from the frozen record, verbatim

**Definition (register, `rung1_inin_formalism`, tier *shown*):** the vacuum
response is described by *"a single Schwinger–Keldysh influence action S_IF
with retarded dissipation kernel **K_R** and noise kernel N (doubled x_r/x_a
fields)."* K_R is the **retarded dissipation kernel of the influence action**
— an open-systems object acting on the probe's doubled variables, paired with
N and constrained by KMS (`rung2_kms_gate`: *"admissible kernels must satisfy
KMS detailed balance"*).

**Structural form (register, `p_tt_ansatz`):** *"K^R = α·χ(ω)·P^TT, with the
projector P^TT **chosen** (not derived)"* — K_R is a frequency kernel times a
tensor structure, and the register's own interrogation ruled the P^TT
restriction CHOSEN. (Our Q1^TT = INSIDE result bears on that choice at the
Σ-level but is a *different node's* business; not conflated here.)

**Pipeline position (benchmark, verbatim):**
`Σ(x,x′) → G_R^TT(x,x′) → K_R → J(ω)` — K_R sits **after** the `G_R^TT`
dressing and **before** the spectral read-off `J(ω)`.

**What G_R^TT and "dressing" mean (register, `rung3_single_pole` frontier
note, verbatim):** *"the TRANSPORT SELF-ENERGY Σ controlling
**G_R = 1/(G0⁻¹ − Σ)**"* — the dressing is the Dyson resummation of the
frozen self-energy into the retarded TT graviton propagator.

**Conventions (frozen):** *"Im chi = J/omega (friction)"* (the G1 plant's
registered friction convention); the closure registry: *"K is the chi-TYPE
response (omega^0 power)… the G1 object-correction (Im chi = J/omega) lives
one derivative away."* Retarded/−i0 structure: inherited from the frozen
kernel (Wall-C/TTW premise noted by the benchmark as touching *"the in-out vs
retarded structure"*).

**What K_R construction requires (the frozen unblock list,
`BARDEEN_FRW_COMPLETION_STATUS.md`, verbatim):** *"The staged
`gw_tensor_friction.py` work — building the smallest defensible
graviton-probe assembly from the frozen Class-C contract. That is
research-grade work requiring: the dS TT-TT-TT vertex (hundreds of terms,
Tsamis–Woodard class); renormalization under the frozen D5 contract;
dual-gauge verification per D4. Each of those is a multi-session component.
They are not approximable, not substitutable, and not bypassable."*

**Answers to the charter's §2 questions:**

| question | answer from the frozen record |
|---|---|
| What is K_R? | the retarded dissipation kernel of S_IF (probe-level, doubled fields) |
| Variables | ω (χ-type, ω⁰); tensor slot P^TT per the ansatz; the frozen record does **not** pin the probe's k-configuration (see UNDERDEFINED) |
| Inputs | the frozen Σ_R^finite; G0 (free TT propagator); the graviton-probe coupling (the influence-functional piece) |
| Σ → K_R map | Dyson dressing G_R = 1/(G0⁻¹ − Σ), then reduction of the graviton-probe influence functional to the probe's quadratic kernel |
| Influence-action kernel? | YES, explicitly (`rung1_inin_formalism`) |
| G_R^TT | the Σ-dressed retarded TT propagator |
| "Dressing" | the Dyson step above, quoted verbatim |
| Pipeline stage | between Σ and J(ω): `Σ → G_R^TT → K_R → J(ω)` |
| Benchmark conclusions defined ON K_R | the two-axis ledger-consequence cell at contract scope; the `rung3_single_pole` pole-vs-branch-cut anchor question; rung7's consumption of the relaxational result |

**UNDERDEFINED (stated, not filled from memory):** the frozen texts pin the
pipeline order, the friction convention, and the dressing identity — but do
**not** pin (i) the probe's kinematic configuration (which k defines the
benchmark's ω-only K_R: a k→0 TT mode? a mode integral?); (ii) the truncation
order of the Dyson step (first-order insertion vs geometric resummation — a
physically consequential choice for pole-vs-cut structure); (iii) the precise
probe-graviton coupling normalization. **These three require an owner
declaration BEFORE any K_R construction** — pre-registration discipline: fix
them before the answer exists.

## 2. Dependency graph

```
                frozen Σ_R^finite (dd77b194…, IMMUTABLE)
                          │
             [Dyson: G_R = 1/(G0⁻¹ − Σ)]          ← truncation order UNDERDEFINED
                          │
                       G_R^TT
                          │
             [graviton-probe influence functional] ← frozen unblock list:
                          │                          TT-TT-TT vertex + D5 renorm
                          │                          + D4 dual-gauge
                        K_R
                          │
           ┌──────────────┼───────────────────┐
   benchmark consequence  │            rung3 pole-vs-cut
   cell (contract scope)  │            anchor question
                    rung7 consumption
```

**Depends on K_R:** the benchmark's ledger-consequence cell at contract
scope; `rung3_single_pole`'s anchor question; rung7's microscopic
consumption. **Does NOT depend on K_R:** Q1/Q4/Q5/Q3 (Declaration-4 Σ-level
objects, closed); the J5 record; PV; A4; **and the +1 discharge — CONFIRMED:
the frozen map admits only Q1^TT ∧ Q5^TT, and the discharge is a completed
owner ruling. K_R cannot reopen it and is not needed by it.**

## 3. Minimal-construction specification (future stage; NOT implemented)

- **Immutable inputs:** kernel `dd77b194…` (+ its TT view); A3-1 masters;
  the G0 TT propagator in the engine's conventions; registry `faa977d4…`
  with the guard LIVE (G0 wiring: the registered J(ω) may not re-enter).
- **Transformations:** (T1) Dyson dressing at an owner-declared order;
  (T2) influence-functional reduction to the probe's quadratic retarded
  kernel, per the frozen three-component unblock list — **any claim that a
  component of that list can be skipped requires an owner ruling first; the
  frozen text says "not bypassable"**; (T3) the owner-declared probe
  kinematics closing UNDERDEFINED item (i).
- **Object:** K_R(ω)·(tensor slot), retarded (−i0 inherited), H-orders as
  declared (flat first; the H-grading convention carried from the freeze);
  flat limit = the H⁰ sector, structurally.
- **Normalization:** the friction convention Im χ = J/ω, anchored the way PV
  anchored phase space — by a derived theorem gate, never a fit.
- **Independent validation route:** dispersive reconstruction of G_R^TT from
  Im Σ (the PV machinery, already validated to 3.5e-6) vs the direct Dyson
  algebra; per-stage negative controls (wrong dressing sign must break KMS/
  passivity gates; probe-coupling corruption must be detected).
- **Acceptance criterion:** K_R produced from pinned inputs with gates green
  and controls behaving — and only THEN, as a separate step, the benchmark
  cell evaluated against it.
- **New-physics vs bookkeeping, stated in advance:** if K_R's analytic
  structure (gap/cut/pole content) **differs** from χ_Σ's under the declared
  dressing — e.g. the Dyson denominator generates a pole from the cut — that
  is a genuine new physical result bearing directly on `rung3_single_pole`.
  If K_R reproduces χ_Σ's analytic content up to normalization (the
  `α·χ·P^TT` form at leading order), the stage is a
  bookkeeping/transformation result — still required for the benchmark cell,
  but not new physics. **The pole-vs-cut question is exactly what the
  truncation-order declaration (UNDERDEFINED ii) decides the meaning of, which
  is why it must be declared before computing.**

## 4. Massive/massless bridge: **SEPARATE OPEN QUESTION**

K_R construction from the frozen Σ does **not** require the bridge: the
pipeline is defined on the assembly as built (massive matter loop). The
bridge matters for *interpreting* K_R against the massless-mode-derived s=3
family — the same scope note the J-adjudication recorded. Not started.

## 5. Ward Class-B relation: **BYPASSES at TT scope; does NOT resolve**

No frozen text says K_R resolves the vector residual. The executed A4/W5
gates prove the residual has zero TT projection, and K_R consumes the
**TT-projected** dressed propagator — so at TT scope K_R is insulated from
the residual by proof, not by neglect. The residual's named discharge path
remains the Bardeen completion (a different charter). The three records stay
separate: TT robust · Ward Class B unresolved · K_R open.

## 6. Statement of non-computation

No K_R quantity was computed, estimated, or prototyped in this stage. The
only artifacts created are this audit and its JSON companion.

**The decision now before the owner:** declare the three UNDERDEFINED items
(probe kinematics, Dyson truncation order, coupling normalization) and rule
on the frozen three-component unblock list — or decline the K_R charter and
declare the current scope complete.
