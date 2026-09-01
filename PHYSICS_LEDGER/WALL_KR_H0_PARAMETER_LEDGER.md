# H⁰ PARAMETER-COUNT / LEDGER UPDATE — AUDIT NOTE

**Date:** 2026-09-01 · **Stage:** governance / accounting only ·
**Instrument:** `wall_kr_h0_parameter_ledger.py` · **Machine-readable:**
`WALL_KR_H0_PARAMETER_LEDGER_RESULT.json` · **Battery: 19/19, zero
failures.** · **Register modified: NO** (`provenance/claims.json`
byte-identical; net `16` unchanged). · **W-0: unbanked. HARD STOP.**

## CONCLUSION

> **H⁰ contains exactly one independent unresolved renormalization
> constant, Λ_R. This is a reparameterization of the (μ, c4)
> representation, not the removal of a parameter. No numerical value has
> been selected.**
>
> **Axis-2 remains C / unchanged.**

## THE ACCOUNTING QUESTION — ANSWERED HONESTLY

The owner's instruction was explicit: *if μ and c4 were never counted as
independent frozen inputs, do not manufacture a numerical "reduction."*

**They were never counted.** Verified mechanically against the register:
it contains **no Λ_R entry and no c4 entry** — its single `c4` string
match is the substring of the prose token **"Sec4"**. The entire
contract-K_R campaign has been W-0 (computed-and-reported, not banked)
throughout.

**Therefore no reduction is claimed and the register net is unchanged.**
The correct statement is the representation one: *the apparent
two-parameter H⁰ representation is shown to contain exactly one
independent constant.*

## NAME COLLISION — FOUND, RECORDED, AND DISAMBIGUATED

The register already uses the symbol **μ** for a **different physical
quantity**: the linear-cosmology modification parameter μ = 1 + α
(μ = 1 GR-like; μ = 4/3 trace-only, ISW-excluded), in the nodes
`mu_linear` and `zeta_interior_family`. That is **not** the
renormalization scale of the contract H⁰ kernel.

This surfaced only in this stage, because `claims.json` is itself a
barred file that the μ-audit correctly did not read. It changes nothing
about μ-RULING-C — but it is an independent reason to carry the new
constant as **Λ_R** rather than as "μ", and it is recorded here so no
later reader conflates them.

## THE COUNT

| | |
|---|---|
| **Irreducible unresolved H⁰ local inputs** | **1** |
| **Identifier** | **Λ_R = μ·exp(c4/2A)** |
| Parameterization | (μ, c4) → Λ_R |
| Numerical value | **none** |
| H² locals (c0p, c2p) | **excluded — fork-gated** |

## ASSERTIONS, RECORDED SEPARATELY

- **A.** c0 = 0 exactly *(verified against the D5 artifact's own record)*
- **B.** c2 = 0 exactly *(same)*
- **C.** c4 is determined by the certified D5 finite calculation **only
  modulo the renormalization-scale representation**
- **D.** (μ, c4) contains exactly **one** independent H⁰ constant
- **E.** Λ_R is genuine: ∂ReΣ^(H0)/∂Λ_R ≠ 0
- **F.** No numerical value of Λ_R has been introduced *(verified against
  the frozen Owner Decision Record)*
- **G.** Axis-2 remains **C** *(same)*

**D is gated non-vacuously:** two *distinct* (μ, c4) points sharing one
Λ_R give the **identical** response — the family is degenerate along the
Λ_R orbit. **Negative control:** moving c4 *off* that orbit changes the
response, so the degeneracy is specific to Λ_R and the "two independent
constants" reading is violated by the certified collapse relation.

## FIREWALLS

**Register firewall:** no claim grade upgraded or downgraded, no node
added, no  altered; Axis-2, the single-pole stance, and all
K_R conclusions untouched. Verified by byte-identical hash.

**Cross-scope firewall:** the read-set intersected with the
barred/outcome set (Axis-2 output, benchmark artifact, J(ω) instrument,
plant, comparator) is **empty**; no spectral-outcome token appears in the
instrument's source, with runtime-assembled sentinels proving the scanner
has teeth. **Disclosed carve-out:**  is barred for
loop-computing instruments; this stage reads it for governance accounting
only — no loop quantity, no spectral object, no modification.

## PROVENANCE

D5 H⁰ c0/c2/c4 → `12ea453` / `04b8d6c`; μ-RULING-C → `eef50eb`; Owner
Decision Record → `fb3ce39`; the Λ_R reparameterization → `4a2e728`
(package §3) and `fb3ce39` (gated both ways). The uncertified pre-repair
Axis-2 runs are **not cited and not read**.

## HARD STOP

Next authorized stage: **the H² local fork** — not opened here.
