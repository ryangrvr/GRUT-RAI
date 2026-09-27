# CORRECTION 01 to the GR-1 L-D labeled diagnostic (prose only)

**Date:** 2026-09-27 · **Authority:** the GR-2 campaign directive's
provenance rule ("If the attack exposes a flaw in an earlier result,
create a correction artifact rather than silently changing the old
result") · **Source of the correction:** GR2-L6
(`GR2_L6_VERDICT_01.md`; charter frozen `29ee4d7`; artifact sha
`64d20c89…`, 15/15).

**What is corrected.** Two prose statements inside the GR-1 L-D
*labeled post-hoc diagnostic* — a note, never a gate — recorded in
`calc/gr1_gravity.py` / `GR1_GRAVITY_RESULT.json` / GR-1's verdict:

1. **"converging monotonically toward 2d = 6."** The measured limit of
   the frozen-window sequence is $S_\infty = 6.2142$, not 6. The
   sequence $5.362\to5.493\to5.662$ continues $5.794\to5.893\to5.984\to
   6.038\to6.050$ at $s=45,63,91,121,131$: it **passes through 6** near
   $s\approx100$ and converges to $6.2142 = 6 + 0.2142$, where the
   $+0.2142$ is a lattice-dispersion curvature offset belonging to the
   window $[0.9,1.8]$, not to the dimension. The *dimensional* content of
   the diagnostic (that the deficit is finite-size, not a dimension
   inconsistency) stands, now with the mechanism derived: an
   open-boundary surface-mode surplus of order $1/s$ with analytic
   coefficient $b_1=22.571$.
2. **"the lowest mode sits at 24% of the window edge."** The figure 0.24
   is the absolute value $\omega_{\min}(13)=2\sin(\pi/26)=0.241$, not a
   percentage: it is 27% of the 0.9 edge and 13% of the 1.8 edge.

**What is not touched.** The GR-1 3D gate (5.362 against a frozen
$6\pm0.6$) is **RED and remains RED**. `calc/gr1_gravity.py`,
`GR1_GRAVITY_RESULT.json`, and `GR1_GRAVITY_VERDICT_01.md` are not
modified; this artifact stands beside them, per the red-register rule
(public record, Appendix C) and the directive. Any refined re-test of the
3D question is a separately chartered C6 act under the refinement rule
frozen in `GR2_L6_FINITE_SIZE_CHARTER_01.md` §5.

**Status effect:** none. No grading moves; the public record of
26 September 2026 is unchanged and is superseded only by a future dated
record.
