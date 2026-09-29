# L0-1h — O-2 EXACT APPENDIX 01: result and clause-level verdict

**Scope:** the frozen list of `L0_1H_THEOREM_01.md` §4 (frozen at
`165a5f6`, per owner ruling 02). The instrument is
`calc/l01h_appendix.py` (`a247780`), committed before the run and tested
on non-members only (enclosure, and negative and positive controls). It
was **run once** on the members (n = 23, a = 1, the declared g-grid).

**Result:** `L0_1H_APPENDIX_RESULT.json`, sha256
`c9d8b8fb6fc40c76c565d7afda9b773d27a9c824511c0d36dc42135f9890cabd`.

## §1 Per-g table (exact brackets are in the JSON; floats here are for reading only)

| g | w\* (A-1) | d_acc (A-2) | band non-empty | t\* | A-3 | certified ratio g·Lₙ / ((u+a)·U₁) | d_mono est. (float, never promoted) |
|---|---|---|---|---|---|---|---|
| 1/20 | 0.0435502608 | 0.0495383021 | yes | 335/8 | **SEPARATED** | 1.438 | 0.5096 |
| 1/10 | 0.0897117794 | 0.0990845106 | yes | 253/8 | **SEPARATED** | 1.525 | 0.6760 |
| 1/4 | 0.2325127447 | 0.2477690550 | yes | 161/8 | **SEPARATED** | 1.660 | 1.0715 |
| 1/2 | 0.4759936555 | 0.4957209114 | yes | 105/8 | **SEPARATED** | 1.767 | 1.6435 |
| 1 | 0.9696580306 | 0.9921048476 | yes | 8 | **SEPARATED** | 1.864 | 2.7133 |
| 2 | 1.9645386658 | 1.9863973718 | yes | 37/8 | **SEPARATED** | 1.934 | 4.7764 |
| 4 | 3.9610416218 | 3.9789079368 | yes | 5/2 | **SEPARATED** | 1.982 | 8.8681 |
| 10 | 9.9584824621 | 9.9690704795 | yes | 1 | **SEPARATED** | 1.977 | 20.6818 |

- **Brackets:** each w\* and d_acc bracket has width ≤ 10⁻¹². The d_acc
  brackets come from exact LDLᵀ pivots.
- **A-2 consistency:** the band is non-empty at every g, as P-2
  requires.
- **A-3:** at every g, the member **K(u, g)**, where u is the upper
  d_acc bracket, is **strictly accretive** (all exact pivots > 0). It
  has **k′(t\*) > 0, certified**, since g·Lₙ > (u+a)·U₁ with rigorous
  enclosures. The smallest certified margin is 1.44.
- **A-4:** not triggered. No g returned NOT CERTIFIED.
- **A-5 (P-1 cross-check, not a gate):** at every witness member,
  max_t k(t) stays below the Perron bound e^{−(u−w\*)t}. The largest
  value of k minus the bound was about −0.011, so there were no
  violations.

## §2 Clause-level verdict (by the confirmed mapping; owner ruling 02 §1)

| Clause | Result | Grade |
|---|---|---|
| **H2-m** (growth is the mechanism) | **FALSIFIED** | Theorem P-1, for every member. No appendix input. |
| **H2-s** (accretive ⇒ monotone) | **FALSIFIED** at all 8 declared g | Exact certified counterexamples: K(u, g) is strictly accretive and has k′(t\*) > 0. |
| **H2-n** (stable, non-accretive ⇒ non-monotone) | **HOLDS** at all 8 declared g, over the whole band (w\*, d_acc) at each | J-6 plus the certified d_mono > d_acc. Recorded independently; **it rescues neither H2-m nor H2-s.** |

**O-2 = FALSIFIED** (terminal once the owner rules). H2-m fails by
theorem, and H2-s fails by exact counterexample. Either alone would
suffice under the confirmed mapping.

## §3 What is certified, at its scope

At each of the eight declared g (n = 23, a = 1, the retained-site
kernel):

> **w\* < d_acc < d_mono** (the first by bracket; the second by exact
> witness), so **stable ⊋ accretive ⊋ monotone** as classes in d.

At the tested boundaries, then, *spectral stability ⇏ accretivity ⇏
retained-site monotone decrease*. Each implication fails at its own
boundary, and each failure is exact.

**Limits, stated so the result is not over-read:**
- The certification covers **only the eight declared g**. Nothing is
  claimed between grid points, for other n or a, or for any site other
  than the retained one.
- **d_mono itself is not certified.** Only d_mono > u is certified. The
  float estimates in §1 are for reading and are never promoted.
- **The width of the separation** (d_mono is several times d_acc at
  small g) **is a float observation, not a result.**
- **The mechanism** the design attributed to the lap (transport round
  the cycle) is consistent with the witness times t\*. Those fall near
  the first-lap transit, scaling roughly as n/(g + a). But the appendix
  does not test that attribution, and it is **not** claimed.
- **Affinity and CM (J-4)** stay on their separate line, outside this
  verdict.

## §4 Standing

- No property → ingredient edge is created.
- The floor, pending the owner's ruling on O-2: O-1 CLASS-SPLIT, O-2
  FALSIFIED (proposed), O-3 DISCHARGED, O-4 CLASS-SPLIT, O-5
  DISCHARGED, O-6 FALSIFIED.
- **If the owner rules O-2 terminal, T5 is met,** and O-7 can move from
  provisional to adjudication (O-2 result → O-7, never the reverse).

**HARD STOP** pending the owner's ruling.
