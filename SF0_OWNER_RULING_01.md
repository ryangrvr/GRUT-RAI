# SF-0 — OWNER RULING 01 (R-F; SF-0 terminal; SF-1 charter authorized, draft only)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5903310812`**, after review of
`123abaa` (SF-0 definitions), `8e6a105` (the SF-0 audit) and the CA-1 / RS-1 free-fermion
definitions. The comment is authoritative; this file records it.

## 1. R-F = (b)

> **Use the excitation law of the exact invariant particle-number sector.**

The ruling is not an owner preference added after seeing the candidate. It follows from the frozen
definitions:
- SF-0 §1 permits 𝓔-sector, i.e. L_eff = the generator restricted to an exact invariant sector,
  with its retained-observable response.
- For CA-1 F, particle number is exactly conserved. So the L_eff of a fixed-N sector is the
  many-body generator restricted to that charge sector, together with the fixed retained density
  response. It is **not** the one-particle hopping matrix viewed in isolation.
- §2 reads I-z from the lowest excitation branch of L_eff. Reading (a) throws away the very sector
  restriction the pre-registration says to inspect.

## 2. The three objections do not demote the candidate

| Objection (`SF0_PARENT_SECTOR_FORMATION_01.md` §4.1) | Owner disposition |
|---|---|
| **A.** z = 2 occurs only at the dilute edge | The frozen rule makes a z difference law-level. It does not require an open-measure region of state space. **The edge character is a scope qualification**; it must not be used to redefine z as a value after the fact. |
| **B.** Particle–hole symmetry | PH identifies ν with 1 − ν. It does **not** identify a generic finite density (for example half filling) with the dilute scaling sector. It maps the two edges ν→0 and ν→1 onto each other. |
| **C.** Every finite ring is gapped | True, but the project already classifies z for finite-ring classes by their controlled thermodynamic/low-momentum limit (RS-1 / CA-1). Finite-size spacing cannot erase z here without also invalidating those. **The SF-1 charter must freeze the thermodynamic scaling before evaluation.** |

Provisional structure stated by the owner, for the same ε(k) = −2 cos k:
- finite filling 0 < ν < 1 gives Δε ~ v_F δk, so z = 1;
- fixed N = O(1) as L → ∞ gives ε(k) + 2 ~ k², so z = 2.

These are **not** encoded as passed facts. SF-1 must derive them from the frozen parent.

## 3. SF-0 terminal

The proposed `REQUIRES-NEW-PARENT` is **NOT ADOPTED.** With R-F = (b), the frozen mechanical
outcome is:

> **SF-0 = FORMULABLE-IN-EXISTING-CLASS (CA-1 F conserved filling sectors), owner R-F = (b).**

The candidate is the existing CA-1 F free-fermion hopping parent, widened **only in its allowed
state/particle-number family**, not in its microscopic rules.

**Earned at SF-0:** a clean formation test can be posed on an existing parent without a new
microscopic law. The following are the same across sectors:
- site net;
- Fock space;
- hopping Hamiltonian and hopping amplitude;
- local density observable;
- statistics;
- generator.

Only the exactly conserved particle-number sector differs, and it is selected by state/boundary data.

**No claim is made that H-SF is demonstrated.**

## 4. SF-1 authorized: charter drafting only

Draft `SF1_FORMATION_CHARTER_01.md` and **do not run it.** It preserves SF-0 §§1–3 and freezes the
items below (the ruling's §4, summarized; the comment is verbatim-authoritative).

| Item | Requirement |
|---|---|
| 4.1 **Parent** | H_F = −Σ_j (c_j†c_{j+1} + h.c.) on the periodic ring and its declared thermodynamic sequence. It is the full Fock-space Hamiltonian. No chemical potential, no filling-dependent coupling, no sector-specific H. No change of lattice, statistics, boundary condition, hopping or readout. |
| 4.2 **Selector** | The exactly conserved N_F = Σ n_j, with [H_F, N_F] = 0. Wording to carry: **formation-by-conserved-sector / boundary data, not attractor selection.** |
| 4.3 **Families** | Dense D: N_L = ⌊νL⌋, with one fixed ν ∈ (0,1), preferably 1/2. Dilute E: N_L = N₀ fixed, N₀ ≥ 1. Neither may be tuned after results. |
| 4.4 **Reference state** | The lowest-energy state of H_F within each exact N sector. This is a state declaration. Generic unitary evolution does not relax to it; SF-1 tests the **sector-conditioned effective law, not thermalization.** |
| 4.5 **Readout** | The same n_j or ρ_q in every sector. No bosonized string observable; no sector-specific readout. |
| 4.6 **Invariants** | Primary I-z; secondary I-q. The expected identities are to be derived, not assumed. If density-response support is used, it must be defined once, before calculation. |
| 4.7 **Coarse-graining** | One IR procedure for both families, with a frozen order: finite-L spectrum → declared L → ∞ → q → 0 → z from the leading edge. It must not use a one-particle dispersion for one family and Lindhard response for the other. |
| 4.8 **Quotient** | SF-0 §3 unchanged. Rescaling cannot turn z = 1 into z = 2; PH copies are quotiented; different densities alone do not count. |
| 4.9 **Outcomes** | FORMATION-OF-LAW-CLASS / STATE-NOT-LAW / EDGE-ONLY-NONROBUST / SECTOR-SMUGGLED / UNFORMULABLE, frozen before any run. |
| 4.10 **Hostile controls** | (1) PH: ν and 1 − ν land in the same class. (2) Two finite fillings (e.g. 1/4, 1/2) land in the same class. (3) At least two N₀ land in the same dilute class. (4) Limit order: the result is not created by an illegitimate swap of L → ∞ and q → 0. (5) The same density-response definition is used throughout. |

## 5. Interpretation fence

Even a positive SF-1 establishes only:

> **one known microscopic parent can support more than one inequivalent low-energy effective-law
> class depending on a conserved boundary/state sector.**

It does **not** establish:
- multiple universes;
- cosmological domain formation;
- varying constants;
- cross-universe mixing;
- the origin of our universe's constants;
- that GRUT's substrate has this property;
- that S-5 is solved.

Only after such a result may one ask whether a GRUT-relevant parent realizes the same mechanism.

## 6. S-5 remains HELD

- **If SF-1 fails** under the common controls, the formation route loses its strongest
  existing-class candidate, and the case for S-5 or a new parent strengthens.
- **If SF-1 succeeds,** the next question is whether GRUT's own candidate substrate has a
  corresponding conserved/formation variable.

## 7. Governance

- Charter only. No SF-1 run, and therefore **no v4 exception is granted by this ruling.**
- A later execution authorization must explicitly grant the campaign-specific exception to the
  post-v4 in-house physics stop.
- Update the SF-0 record and CURRENT_STATE, then HARD STOP with the frozen SF-1 charter for review.
- No new parent, no S-5, no SF-2, no domain mixing, no empirical claim.

## Auditor note

The §4.1 reading (a) in `SF0_PARENT_SECTOR_FORMATION_01.md` was the auditor's. Per this ruling it is
overruled: the excitation law of the 𝓔-sector restriction is the frozen object.
