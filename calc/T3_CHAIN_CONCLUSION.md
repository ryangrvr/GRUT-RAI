# T3 CHAIN CONCLUSION — the banked result of the Tier-3 H-sector line

**Status: BANKED by owner ruling 2026-09-21** (*"preserve everything you've got,
finish the small certificate follow-up, bank the T3-05/T3-07 chain, and then make
the Σ_R → G_R^TT question the final major physics calculation"*). Wording below is
the owner's corrected formulation; the interpretive qualification sits at the top,
per the owner's instruction, not the bottom.

## The result (owner's formulation, governing)

> **The one-loop graviton self-energy on de Sitter space contains a fully
> certified, irreducibly nonstationary absorptive response through H⁶ within the
> declared Tier-3 construction. Its Wigner-time dependence cannot be represented
> by the tested class of stationary amplitude/frequency dressings. This provides
> a concrete characterization of graviton-loop dissipation on an expanding
> background, but does not by itself distinguish GRUT from standard QFT on de
> Sitter.**

The calculation establishes an **absorptive graviton-loop response** on dS.
"Responsive medium" is a GRUT interpretation consistent with it — an expanding
background can carry memory/nonstationary response structure that cannot be
absorbed into a local stationary clock — and is not itself established by the
calculation, which is standard QFT on dS.

## The object

Im Σ_R(ω>0) = (ω⁴/1280π) · P(x, y),  x = H·u_b,  y = H/ω, under the declared
Tier-3 contract (pure-graviton loop, TT bath, Option-B adiabatic modes, k_ext→0
probe, d = 3; validity ω ≳ 3.4H per the record's own derived refusal ε_H):

| order | contribution to P | status | source |
|---|---|---|---|
| H⁰ | −3 | complete (two routes + quadrature) | `WALL_KR_TIER3_FLAT_RESULT.json` |
| H¹ | 0 | complete — vanishes exactly | `T3_07_H6_EXTRACTION_RESULT.json` |
| H² | −(104/3)·y² | complete, u_b-free | `WALL_KR_CONTRACT_RETARDED_VERDICT.md` |
| H³ | +24·x³ − (472/3)·x·y² | **complete — first u_b-odd term** | `T3_07_H6_EXTRACTION_RESULT.json` |
| H⁴ | −18·x⁴ + 220·x²·y² − 127·y⁴ | complete (custody: K2 → L → G) | `T3_05_H4_SECTOR_RESULT.json` |
| H⁵ | (416/3)·x³·y² − 496·x·y⁴ | **δ-class only** — PV leak at n = 4; NOT overclaimed; excluded from binding | `T3_07_H6_EXTRACTION_RESULT.json` |
| H⁶ | −48·x⁶ + (3448/3)·x⁴·y² − 3312·x²·y⁴ − (1280/3)·y⁶ | complete — first negative ω power | `T3_07_H6_EXTRACTION_RESULT.json` |

H⁷/H⁸ exist in the theory (object degree 8) and were removed by the builder's
`_HKILL` before caching; extraction would require a new assemble run. **Owner
ruling: lower priority — not to be run unless attached to a new physics
question.**

## The adjudication chain (what was eliminated, in order)

1. **Partition artifact — eliminated.** `T3_05K2_NAMESPACE_RECONCILIATION_RESULT.json`:
   cone_split and branch_map are the same partition under the source-verified
   namespace map (m ↔ (−2,0), p ↔ (+2,0)); T3-05K's DIFFER_BY_STRAY was a
   key-namespace instrument artifact (K2/K3 preserved as the defect record).
2. **Extraction artifact — tested.** `T3_05L_P_BRANCH_ABSORPTIVE_RESULT.json`:
   the p/(+2) cone is kinematically null for Im(ω>0) (delta support q = −ω/2
   outside the measure domain, per Δ-degree, termwise — not a cancellation), and
   the two cones carry independent content (odd-derivative conjugation-breaking,
   machine-verified) — any future Re Σ assembly must compute the p-cone PV
   content explicitly. The termwise extraction machinery reproduces the recorded
   A2 exactly (gate, run 6).
3. **Stationary dressed-clock representation — REFUTED at H⁶.**
   `T3_07B_SLOT_CERTIFICATE_RESULT.json`: for any Im Σ = F(x)·(ω̃⁴/1280π)·T(H/ω̃),
   ω̃ = ω·g(x) (contains C1 amplitude-only, C2 redshift-only, C3 combined), the
   pure-y slots fix t = (−3, −104/3, −127, −1280/3); the measured H¹/H³ data pin
   f₁ = 118/13, g₁ = −59/26; slots (2,0)/(2,2) fix f₂ = 1336/169, g₂ = 14733/1352;
   the x²y⁴ slot is then parameter-free: **model requires −169672/169 ≈ −1003.98;
   complete H⁶ data says −3312; residual 390056/169 ≠ 0.** Single-witness,
   parameter-free refutation on complete data only (H⁵ excluded).
   `T3_06A_STRUCTURE_ADJUDICATION_RESULT.json`'s C1/C2 refutation certificates
   (even-slot-only) stand; its C3 ADMITS_FIT verdict and its treatment of
   order-3 slots as zero are **superseded** by the measured H³ content and by
   T3-07B.

Supporting: `T3_06B_KEYSTONE_STATUS_RESULT.json` — sign-definiteness (exact max
of the ≤H⁴ object = −599127/270400 < 0 on the self-consistent window; grid-
sampled P < 0 at every tested point when the H³/H⁶ terms are included, both
signs of u_b, with the inner window hierarchical and the refusal-corner
qualitative); the secular radius x* = 6^(−1/4) at y = 0; the structural domain
gap to the declared ω→0 endpoint, which remains frontier-reserved per
`BUILD_BANKING_PROMPT.md`.

## What has NOT been established (owner's list, binding)

No new fundamental vacuum ontology; no new measurable GRUT-specific effect; no
Born-rule derivation; no emergence of ħ; no completed quantum-gravity theory; no
experimentally distinguishable prediction. **H stays empty.**

## Next steps (owner rulings, 2026-09-21)

1. **PV machinery** — eventually; NOT a prerequisite for this result (H⁵ is
   correctly quarantined; the H⁶ certificate does not depend on it). Becomes
   important for the full H⁵ and for Re Σ_R.
2. **H⁷/H⁸** — lower priority; only with a specific physical question attached.
3. **Σ_R → G_R^TT keystone — THE next physics step**, with the binding
   constraint: *do not force the bridge into a stationary one-frequency
   response* — the H⁶ certificate has shown the tested stationary reduction is
   inadequate; the response object may have to retain genuine two-time structure
   G_R(t, t′; k) rather than assuming G_R(ω, k). Charter drafted for
   ratification: `T3_08_GRTT_KEYSTONE_CHARTER.md`. No computation authorized by
   this document.
4. **Final synthesis** — after the keystone decision, not before. The project
   stops expanding sideways.

## Instrument-defect disclosures carried with the chain

T3-05L v1 conjugate-mirror premise (refuted by data; mechanism located);
T3-07 v1 exactness premise (assumptions bug, caught by its own gates; filed
NOT_H_EXACT); T3-07 runs 4–6 in-instrument sp.series/sp.solve infeasibility
(externalized to the T3-07B truncated-polynomial certificate); the run-3
i-convention port bug (fixed; prior file preserved). All logs retained
(`t3_05l_run*.log`, `t3_07_run1..6.log`, `t3_07b_run1.log`).
