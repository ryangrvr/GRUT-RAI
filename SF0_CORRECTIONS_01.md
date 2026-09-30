# SF-0 — CORRECTIONS 01 (additive; auditor-initiated after SF-1)

- **Date:** 2026-09-30.
- **Trigger:** the accepted SF-1 result (`SF1_OWNER_RULING_02.md`) is a counterexample to a blanket
  argument in `SF0_PARENT_SECTOR_FORMATION_01.md` §4.
- **Handling:** historical text is not rewritten. The SF-0 record carries a pointer here.
- **Standing:** this is **proposed by the auditor.** The owner may accept, amend or strike it.

## SC-1. The "Linear/Gaussian ⇒ STATE-NOT-LAW by construction" argument is withdrawn as stated

**What SF-0 §4 said (lines 166–168):**

> Linear/Gaussian classes (𝒞₁, 𝒞₃, 𝒦_N, P-1, FS-1, CA-1 P/T/D): the equations of motion do not
> depend on the state. So every §2 invariant of L_eff is state-independent, and any sector
> multiplicity is STATE-NOT-LAW by construction.

The same reasoning appears in the §4 table rows:
- FS-1 fixed-H: "quadratic ⇒ state-blind law";
- O-6: "same A on every torus".

**Why it fails:**
- The free-fermion parent of SF-1 is quadratic (Gaussian). Its equations of motion are
  state-independent.
- Yet under R-F = (b), with the density readout, its sector-conditioned IR class differs. This was
  accepted.
- The argument used reading (a) (the single-particle/linear law) for the invariants. It is
  therefore overruled by R-F = (b) for every class to which it was applied.

**What survives (identity grade):** for quadratic dynamics, the retarded response of **linear**
observables (x_j, c_j, …) is a state-independent c-number commutator. So the blanket statement holds
**only for linear retained observables.**

**What does not survive:** for **quadratic** retained observables (densities n_j, energy densities,
quadratic charges), the support of the response/structure factor about a sector state depends on
that state's occupations:
- Pauli blocking for fermions;
- occupation weights for bosons;
- mode amplitudes for classical conservative flows.

The structural invariants read from that support can therefore be sector-dependent. SF-1 is the
explicit instance.

## SC-2. Labels affected

| SF-0 §4 row | Old label | Status after SC-1 |
|---|---|---|
| 𝒞₁ (Hurwitz-linear), 𝒞₂ (strictly convex) | STATE-NOT-LAW / single sector | **Stands.** The reason is a unique persistent state (a single attractor), not linearity. |
| 𝒞₃ (OU) | STATE-NOT-LAW | **Stands.** The reason is a unique stationary law, not linearity. |
| FS-1 fixed-H charge sectors | STATE-NOT-LAW ("state-blind") | **RE-OPENED**, for SFG-0 under reading (b) with a quadratic readout |
| O-6 𝒦_N tori | STATE-NOT-LAW ("same A") | **RE-OPENED**, for SFG-0 under reading (b) with a quadratic readout |
| CA-1 P/T/D, P-1 | SECTOR-SMUGGLED (different generators or V) | **Stands.** The labels rest on generator changes, not on linearity. |
| P-6 L-C (finite spin blocks) | STATE-NOT-LAW | **Stands, with a qualifier:** P-6 declares no thermodynamic sequence, so no IR exponent is defined. The finite-gap argument is replaced by this one, per SF-0 ruling §2C. |

- **The SF-0 terminal is unaffected.** It was already FORMULABLE-IN-EXISTING-CLASS per R-F, and the
  re-opened rows can only add candidates.
- **The §5.1 M-1…M-4 list** ("what the other classes lack") is qualified. For quadratic readouts,
  linear/conservative classes with persistent occupation or action sectors are **not** excluded by
  construction.
