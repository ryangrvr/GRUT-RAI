# L0-1 FLOOR — SUCCESSOR LIST (T4: preserved, not executed under floor authority)

> **CURRENT STATUS POINTER:** Current successor statuses are maintained in `GRUT_SUCCESSOR_STATUS_01.md`. The
> historical successor questions below are preserved unchanged.

The floor's obligation list is closed (T4 of the adopted termination
condition). Questions the floor raises are recorded here. They are
**preserved, not executed** under floor authority. Anything here moves
into active work only by a new owner authorization outside the floor,
or by an explicit T4 scope-change ruling.

| # | Question | Raised by | What is attached |
|---|---|---|---|
| S-1 | **Is noise primitive or derived?** | L0-1e review (B); owner ruling `5888965691` | **The linear-Gaussian observational-equivalence theorem.** For linear drift with additive Gaussian noise, the stationary correlation e₁ᵀe^{−Kτ}Σe₁ is reproduced exactly by (i) a deterministic linear flow from a Gaussian initial ensemble N(0, Σ), and (ii) a deterministic Hamiltonian dilation (a Ford–Kac–Mazur-type bath with thermal initial data at per-site temperatures). So no second-order battery in this class can separate primitive from derived stochasticity. A test needs a class where they separate, e.g. nonlinear drift or multiplicative noise, where noise-induced drift moves the mean. |
| S-2 | **The hard D-DET:** multiplicative, colored, non-Gaussian, and nonlinear stochastic classes | design §3 (deferred); L0-1e charter §3.9 | F-5 fails there (the mean response depends on the noise), so determinism can bear on P^resp. |
| S-3 | **The crossed cell:** does generator-side cycle affinity break *correlation* complete monotonicity, with the noise held FDT-like? | reversal diagnostic §2.3 | Needed to separate "response ↔ correlation" from "generator ↔ noise" in the D-HERM/D-DET contrast. The other crossed cell (noise → response) is empty by F-5. |

| S-4 | **Re-reading the two-property hypothesis.** Should "dissipation → derivable order" read "strict-Lyapunov structure / off the chain-recurrent set", and should "detailed balance" be attached to "stationary lag distinguishability"? | L0-1f (O-5) revision 1, withdrawn per review DORD-5 | D-3 (sufficient), D-4 (necessary; α∩ω obstruction), Conley's chain-recurrence theorem (cited), D-5. The frozen H-ORD wording ("*exactly* in the dissipative classes") fails for stable limit cycles, which are outside the record's classes. Re-wording the frozen hypothesis needs an owner ruling (T4). |
| S-5 | **Can the generator itself be derived rather than presupposed?** Every O-5 formulation takes the generator (f, K, or (V, g)) as substrate data. Its magnitude sets the derived clock and its sign carries the orientation. | L0-1f (O-5) §0, §6 | The design's §0 lists "a generator" as a primitive-looking floor assumption. O-5's T1 scope does not include deriving it. |

| S-6 | **Does a coarse-grained arrow survive band-edge memory?** Candidate measures: the worst drawdown of ⟨E_B⟩ against its net rise, and the backflow fraction ∫J⁻/∫\|J\|. | O-6 ruling (`5895858851`): FALSIFIED for the strict form only. | `L0_1G_PREFREEZE_REVIEW_01.md` §3(a) lists the magnitude maps. A test needs a principled coarse-graining criterion, fixed before evaluation. |

| S-7 | **What sets the monotone boundary d_mono?** This covers the untested lap/transport interpretation, dependence on n, a and the retained site, and whether the threshold ordering can reverse in other classes. | O-2 (`L0_1H_OWNER_RULING_03.md`); accepted by O-7 ruling (`L0_1_FLOOR_O7_OWNER_RULING_01.md`) | Only d_mono > d_acc is certified (8 g, n = 23, a = 1). The appendix was one-sided and cannot certify the reverse ordering. J-6 gives the exact criterion k′ > 0 ⟺ g·yₙ/y₁ > d + a. |
| S-8 | **The affinity/complete-monotonicity line**, pre-registered independently | O-2 design and theorem (J-4); accepted by O-7 ruling | The one-way ring breaks CM at every g > 0 (J-4, theorem). This must **never** be folded into O-2 or into the passivity question. |

**Priority (owner, O-7 ruling):** S-7 and S-8 are legitimate local
follow-ups, **not** the priority successor research front.

**Held elsewhere, not on this list:** the pin-free locality fork
(L0-1b's Outcome A; outside the floor per T8); the reversal diagnostic
(a pre-registered Level-0 synthesis diagnostic, owner ruling
`5888965691`).
