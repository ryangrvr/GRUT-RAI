#!/usr/bin/env python3
"""build_figures: the document's three figures, generated — never drawn by hand.

THE RULE, inherited from the one-number rule: every register-derived quantity in a figure is
read from the register at build time, so a figure cannot go stale any more than a count can.
And the honesty constraints are structural, not editorial:

  FIGURE 1 (tier histogram): bars in the CANONICAL tier order (the front matter's vocabulary
  order), never sorted by height — a sorted histogram is an editorial ordering. The `derived`
  tier has no bar: it is marked by an EMPTY DASHED FRAME spanning the plot, labelled with its
  count, so the reader sees a tier present in the vocabulary and unpopulated in fact. The frame
  is a marker, not a bar — its extent is not a value, and the caption must not say it is
  (corrected 2026-08-17 after the figure lens read the caption against the drawing).
  Flat fills, no gradients, no smoothing.

  FIGURE 2 (postulate sort): the four bins with their members as NAMES — no counts anywhere,
  so nothing can go stale and no bin reads as "bigger" by a number. Membership is transcribed
  from POSTULATE_MAP.md's bins; a drift in membership is a documentation change, reviewed as
  one.

  FIGURE 3 (three spectral sketches): single pole / branch cut / gapped tower on IDENTICAL
  axes and scales, so no panel can be made to resemble another by scale choice. The tower
  panel's gap is annotated as the content ("no support below the gap") — the anti-near-miss
  constraint, mandated: the tower must not read as an almost-single-pole. The curves are
  schematic by declared intent (the caption says so); the *structure* (one pole at zero /
  continuum from zero / discrete poles away from zero) is the only claim.

Refused, permanently, per the outline: the mu(x) allowance window. A ceiling over a missing
floor reads as a prediction band regardless of caption.

Run:  python3 build_figures.py --write   write docs/fig1_tiers.svg, fig2_postulates.svg,
                                          fig3_spectra.svg
      python3 build_figures.py --check    re-render and diff against the written files
Pure stdlib. Deterministic output (no timestamps, no randomness) so --check is exact.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")

TIER_ORDER = ["shown", "derived", "derived-pending", "assumed", "to-derive"]
INK = "#1a1a1a"
BAR = "#7a8ba6"
EMPTY = "#c0392b"


def tier_counts():
    with open(os.path.join(HERE, "claims.json")) as f:
        cl = json.load(f)["claims"]
    grut = [c for c in cl if c.get("ledger_scope", "grut") == "grut"]
    counts = {t: 0 for t in TIER_ORDER}
    for c in grut:
        t = c.get("tier")
        if t in counts:
            counts[t] += 1
    return counts


def fig1():
    counts = tier_counts()
    W, H, ml, mb, mt = 640, 360, 60, 70, 40
    plot_h = H - mb - mt
    maxc = max(counts.values())
    bw, gap = 90, 26
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="Helvetica,Arial,sans-serif">',
             f'<text x="{W//2}" y="24" text-anchor="middle" font-size="15" fill="{INK}">'
             f'Register tiers, framework scope — generated from claims.json</text>']
    for i, t in enumerate(TIER_ORDER):
        n = counts[t]
        x = ml + i * (bw + gap)
        h = int(plot_h * n / maxc) if maxc else 0
        y = mt + plot_h - h
        if n == 0:
            parts.append(f'<rect x="{x}" y="{mt}" width="{bw}" height="{plot_h}" fill="none" '
                         f'stroke="{EMPTY}" stroke-dasharray="6 4" stroke-width="1.5"/>')
            parts.append(f'<text x="{x + bw//2}" y="{mt + plot_h//2 - 8}" text-anchor="middle" '
                         f'font-size="13" fill="{EMPTY}">empty</text>')
            parts.append(f'<text x="{x + bw//2}" y="{mt + plot_h//2 + 12}" text-anchor="middle" '
                         f'font-size="13" fill="{EMPTY}">({n})</text>')
        else:
            parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" fill="{BAR}"/>')
            parts.append(f'<text x="{x + bw//2}" y="{y - 6}" text-anchor="middle" '
                         f'font-size="13" fill="{INK}">{n}</text>')
        parts.append(f'<text x="{x + bw//2}" y="{mt + plot_h + 18}" text-anchor="middle" '
                     f'font-size="12" fill="{INK}">{t}</text>')
    parts.append(f'<line x1="{ml - 8}" y1="{mt + plot_h}" x2="{W - 20}" y2="{mt + plot_h}" '
                 f'stroke="{INK}" stroke-width="1"/>')
    parts.append(f'<text x="{W//2}" y="{H - 14}" text-anchor="middle" font-size="11" '
                 f'fill="{INK}">bars in the vocabulary\'s canonical order, never sorted; '
                 f'the empty tier is the result</text>')
    parts.append('</svg>')
    return "\n".join(parts)


# Each member is (label drawn in the figure, the phrase that must appear in POSTULATE_MAP.md).
# The anchors exist so test_figure_two_tracks_the_postulate_map can bind the figure to the map in
# BOTH directions: no invented member, and no map member silently dropped. The first version
# carried neither binding and had already lost three of Bin 4's members (re-screen, 2026-08-17).
BINS = [
    ("Bedrock: posits, not\nderivation targets", [
        ("medium ontology + split", "responsive-medium ontology + system/bath split"),
        ("low-entropy past boundary", "The Past Hypothesis"),
        ("Born measure", "The Born measure"),
    ]),
    ("Open layers: named\ndischarge paths", [
        ("bath memory shape", "The bath's pole structure / collisionality"),
        ("pure-TT choice", "The pure-TT projector"),
        ("covariant gauge-orbit\navailability", "The 4d-covariant gauge-orbit availability"),
    ]),
    ("Borrowings, loan\nrecorded", [
        ("GR (recovered with\nimports)", "GR / the Einstein–Hilbert action"),
        ("anomaly-to-amplitude\nbridge (settled negative)", "The α→TT bridge"),
    ]),
    ("Results — never\ninputs", [
        ("FDT lock (removed an\nassumption)", "`rung2_kms_gate`"),
        ("tidal Love/KK link", "`rung4_love_kk`"),
        ("α = a/c (shown,\nconditional theorem)", "`rung9a_value`"),
        ("the μ=4/3 modification\nexcluded — ΛCDM survives,\nit is not what is ruled out", "`mu_linear`"),
        ("no-crossing (to-derive,\nanchored)", "The no-crossing"),
        ("the arrow's existence\n(intrinsic)", "The arrow's existence"),
        ("the dissolved-screen\nnegatives", "The dissolved-screen negatives"),
    ]),
]


def _bin_height(title, members):
    """Height a bin needs for its own content. Boxes are sized to content and drawn uniform:
    trailing empty space inside a bin reads as 'more could go here' — an incompleteness the
    sort does not have (found by rendering, 2026-08-17)."""
    h = 20 + len(title.split("\n")) * 15 + 8
    for label, _anchor in members:
        h += len(label.split("\n")) * 14 + 8
    return h + 14


def fig2():
    bw, gap, ml, mt = 172, 14, 20, 46
    box_h = max(_bin_height(t, m) for t, m in BINS)
    W, H = ml * 2 + 4 * bw + 3 * gap, mt + box_h + 20
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="Helvetica,Arial,sans-serif">',
             f'<text x="{W//2}" y="24" text-anchor="middle" font-size="15" fill="{INK}">'
             f'The postulate sort — names, not counts (transcribed from POSTULATE_MAP.md)</text>']
    for i, (title, members) in enumerate(BINS):
        x = ml + i * (bw + gap)
        parts.append(f'<rect x="{x}" y="{mt}" width="{bw}" height="{box_h}" fill="none" '
                     f'stroke="{INK}" stroke-width="1.2"/>')
        ty = mt + 20
        for line in title.split("\n"):
            parts.append(f'<text x="{x + bw//2}" y="{ty}" text-anchor="middle" font-size="12" '
                         f'font-weight="bold" fill="{INK}">{line}</text>')
            ty += 15
        ty += 8
        for label, _anchor in members:
            for line in label.split("\n"):
                parts.append(f'<text x="{x + bw//2}" y="{ty}" text-anchor="middle" '
                             f'font-size="11" fill="{INK}">{line}</text>')
                ty += 14
            ty += 8
    parts.append('</svg>')
    return "\n".join(parts)


def _axes(x0, w, label, status):
    y_base, h = 300, 210
    s = [f'<line x1="{x0}" y1="{y_base}" x2="{x0 + w}" y2="{y_base}" stroke="{INK}"/>',
         f'<line x1="{x0 + w // 2}" y1="{y_base}" x2="{x0 + w // 2}" y2="{y_base - h}" '
         f'stroke="{INK}" stroke-dasharray="2 3"/>',
         f'<text x="{x0 + w // 2}" y="{y_base + 16}" text-anchor="middle" font-size="11" '
         f'fill="{INK}">ω = 0</text>',
         f'<text x="{x0 + w // 2}" y="{y_base + 34}" text-anchor="middle" font-size="12" '
         f'fill="{INK}">{label}</text>',
         ]
    for n, line in enumerate(status.split("|")):
        s.append(f'<text x="{x0 + w // 2}" y="{y_base + 50 + n * 13}" text-anchor="middle" '
                 f'font-size="10" fill="{INK}">{line}</text>')
    return s, y_base, h


def fig3():
    # ONE amplitude for all three panels. Different heights across panels would be an editorial
    # weight cue on three MUTUALLY EXCLUSIVE candidate answers to one undetermined question, and
    # there is no y-axis to normalize against (found by the mandated figure lens, 2026-08-17:
    # the first version drew the framework's assumed case ~47% taller than the known one).
    AMP = 0.62
    pw, pgap, left = 260, 60, 30
    W, H = left + 3 * pw + 2 * pgap + left, 400
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="Helvetica,Arial,sans-serif">',
             f'<text x="{W//2}" y="22" text-anchor="middle" font-size="15" fill="{INK}">'
             f'Three candidate low-frequency structures — identical axes and amplitudes, '
             f'schematic by declared intent</text>',
             f'<text x="{W//2}" y="40" text-anchor="middle" font-size="11" fill="{INK}">'
             f'the order is not a ranking; each panel carries its status in the register'
             f'</text>']
    # (a) single pole
    x0 = left
    ax, yb, h = _axes(x0, pw, "(a) single pole",
                      "the framework's conjecture — derived-pending,|lean recorded circular")
    parts += ax
    pts = []
    for i in sorted(set(list(range(0, pw + 1, 4)) + [pw // 2])):
        u = (i - pw / 2) / (pw / 14.0)
        y = yb - h * AMP / (1 + u * u)
        pts.append(f"{x0 + i},{y:.1f}")
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BAR}" '
                 f'stroke-width="2.2"/>')
    # (b) branch cut -- a SHELF, not a tent: an apex at omega = 0 would make the cut read as a
    # blunt version of (a). Its content is continuous support through zero with no isolated peak.
    x0 = left + pw + pgap
    ax, yb, h = _axes(x0, pw, "(b) branch cut", "the refuting outcome —|would retire the conjecture")
    parts += ax
    top = yb - h * AMP
    pts = [f"{x0 + 6},{yb}"]
    for i in range(0, pw - 11, 4):
        xx = x0 + 6 + i
        u = (xx - (x0 + pw / 2)) / (pw * 0.5)
        y = top + (h * AMP * 0.72) * (u ** 6)
        pts.append(f"{xx},{min(y, yb):.1f}")
    pts.append(f"{x0 + pw - 6},{yb}")
    parts.append(f'<polygon points="{" ".join(pts)}" fill="{BAR}" fill-opacity="0.35" '
                 f'stroke="{BAR}" stroke-width="1.5"/>')
    parts.append(f'<text x="{x0 + pw//2}" y="{top - 12:.0f}" text-anchor="middle" font-size="11" '
                 f'fill="{INK}">continuous through ω = 0 — no isolated peak</text>')
    # (c) gapped tower -- EQUAL HEIGHTS, deliberately: innermost-tallest gives the eye an envelope
    # peaking at omega = 0 with a notch cut out, i.e. an almost-single-pole, the exact impression
    # this panel must not create. The claim is structural: discrete support, none below the gap.
    x0 = left + 2 * (pw + pgap)
    ax, yb, h = _axes(x0, pw, "(c) gapped tower",
                      "the known free-field structure|in the well-posed substitute")
    parts += ax
    gap_px, lead, step = int(pw * 0.20), 12, 22
    assert gap_px + lead + 2 * step < pw // 2, "tower poles would run off the panel"
    ph = h * AMP
    for sgn in (-1, 1):
        for k in range(3):
            px = x0 + pw // 2 + sgn * (gap_px + lead + k * step)
            parts.append(f'<line x1="{px}" y1="{yb}" x2="{px}" y2="{yb - ph:.1f}" '
                         f'stroke="{BAR}" stroke-width="3"/>')
            parts.append(f'<circle cx="{px}" cy="{yb - ph:.1f}" r="3" fill="{BAR}"/>')
    # the gap box spans the ACTUAL empty interval between the innermost poles, edge to edge
    half = gap_px + lead
    parts.append(f'<rect x="{x0 + pw//2 - half}" y="{yb - ph - 6:.0f}" width="{2 * half}" '
                 f'height="{ph + 6:.0f}" fill="none" stroke="{INK}" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{x0 + pw//2}" y="{yb - ph - 34:.0f}" text-anchor="middle" '
                 f'font-size="11" fill="{INK}">no support below the gap</text>')
    parts.append(f'<text x="{x0 + pw//2}" y="{yb - ph - 18:.0f}" text-anchor="middle" '
                 f'font-size="11" fill="{INK}">— not a near-miss of (a)</text>')
    parts.append('</svg>')
    svg = "\n".join(parts)
    # CANVAS GUARD: the first version's panel (c) ran 30px past the viewBox and its outermost
    # pole never rendered -- five visible poles, asymmetric, the very cluster the panel exists to
    # avoid. The pole-inside-panel assert above passed throughout. Both are checked now.
    import re as _re
    xs = [float(v) for v in _re.findall(r'(?:x|x1|x2|cx)="(-?[0-9.]+)"', svg)]
    for pts in _re.findall(r'points="([^"]+)"', svg):
        xs += [float(p.split(",")[0]) for p in pts.split()]
    # TEXT counts too: a centred label wider than its panel clips at the viewport, and the first
    # version of this guard read only anchor coordinates -- so it certified a canvas whose panel
    # (a) status line ran to the left edge (re-screen, 2026-08-17). Advance width is estimated at
    # 0.55em, deliberately generous.
    for anchor_x, size, text in _re.findall(
            r'<text x="(-?[0-9.]+)"[^>]*font-size="([0-9.]+)"[^>]*>([^<]*)</text>', svg):
        half = 0.55 * float(size) * len(text) / 2
        xs += [float(anchor_x) - half, float(anchor_x) + half]
    assert max(xs) < W, f"figure 3 draws past its canvas: {max(xs):.1f} >= {W}"
    assert min(xs) >= 0, f"figure 3 draws off the left edge: {min(xs):.1f}"
    return svg


FIGS = {"fig1_tiers.svg": fig1, "fig2_postulates.svg": fig2, "fig3_spectra.svg": fig3}


def main():
    if "--check" in sys.argv:
        for name, fn in FIGS.items():
            path = os.path.join(DOCS, name)
            on_disk = open(path).read() if os.path.exists(path) else ""
            if on_disk != fn():
                print(f"DRIFT: {name} does not match a fresh render. Never hand-edit a "
                      f"generated figure; edit build_figures.py and rebuild.")
                return 1
        print("figures match their generators (and figure 1 matches the register).")
        return 0
    if "--write" in sys.argv:
        for name, fn in FIGS.items():
            open(os.path.join(DOCS, name), "w").write(fn())
            print(f"wrote docs/{name}")
        return 0
    print("usage: build_figures.py --write | --check")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
