#!/usr/bin/env python3
"""build_figures: the document's three figures, generated — never drawn by hand.

THE RULE, inherited from the one-number rule: every register-derived quantity in a figure is
read from the register at build time, so a figure cannot go stale any more than a count can.
And the honesty constraints are structural, not editorial:

  FIGURE 1 (tier histogram): bars in the CANONICAL tier order (the front matter's vocabulary
  order), never sorted by height — a sorted histogram is an editorial ordering. The `derived`
  bar is drawn at its true height with its count labelled, so its emptiness is a datum, not a
  gap in the axis. Flat fills, no gradients, no smoothing.

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
                 f'the empty bar is the result</text>')
    parts.append('</svg>')
    return "\n".join(parts)


BINS = [
    ("Bedrock: posits, not\nderivation targets",
     ["medium ontology + split", "low-entropy past boundary", "Born measure"]),
    ("Open layers: named\ndischarge paths",
     ["bath memory shape", "pure-TT choice", "covariant gauge-orbit\navailability"]),
    ("Borrowings, loan\nrecorded",
     ["GR (recovered with\nimports)", "anomaly-to-amplitude\nbridge (settled negative)"]),
    ("Results — never\ninputs",
     ["FDT lock (removed an\nassumption)", "ΛCDM-shape exclusion", "no-crossing (to-derive,\nanchored)"]),
]


def _bin_height(title, members):
    """Height a bin needs for its own content. Boxes are sized to content and drawn uniform:
    trailing empty space inside a bin reads as 'more could go here' — an incompleteness the
    sort does not have (found by rendering, 2026-08-17)."""
    h = 20 + len(title.split("\n")) * 15 + 8
    for m in members:
        h += len(m.split("\n")) * 14 + 8
    return h + 14


def fig2():
    bw, gap, ml, mt = 160, 16, 20, 46
    box_h = max(_bin_height(t, m) for t, m in BINS)
    W, H = 720, mt + box_h + 20
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
        for m in members:
            for line in m.split("\n"):
                parts.append(f'<text x="{x + bw//2}" y="{ty}" text-anchor="middle" '
                             f'font-size="11" fill="{INK}">{line}</text>')
                ty += 14
            ty += 8
    parts.append('</svg>')
    return "\n".join(parts)


def _axes(x0, w, label):
    y_base, h = 300, 210
    s = [f'<line x1="{x0}" y1="{y_base}" x2="{x0 + w}" y2="{y_base}" stroke="{INK}"/>',
         f'<line x1="{x0 + w // 2}" y1="{y_base}" x2="{x0 + w // 2}" y2="{y_base - h}" '
         f'stroke="{INK}" stroke-dasharray="2 3"/>',
         f'<text x="{x0 + w // 2}" y="{y_base + 16}" text-anchor="middle" font-size="11" '
         f'fill="{INK}">ω = 0</text>',
         f'<text x="{x0 + w // 2}" y="330" text-anchor="middle" font-size="12" '
         f'fill="{INK}">{label}</text>']
    return s, y_base, h


def fig3():
    W, H, pw = 900, 350, 260
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="Helvetica,Arial,sans-serif">',
             f'<text x="{W//2}" y="22" text-anchor="middle" font-size="15" fill="{INK}">'
             f'Three low-frequency structures, identical axes — schematic by declared intent'
             f'</text>']
    # (a) single pole: Lorentzian centred at 0
    x0 = 30
    ax, yb, h = _axes(x0, pw, "(a) single pole")
    parts += ax
    pts = []
    for i in range(0, pw + 1, 4):
        u = (i - pw / 2) / (pw / 14.0)
        y = yb - h * 0.92 / (1 + u * u)
        pts.append(f"{x0 + i},{y:.1f}")
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BAR}" '
                 f'stroke-width="2.2"/>')
    # (b) branch cut: continuum from 0 (shaded wedge, no peak)
    x0 = 30 + pw + 60
    ax, yb, h = _axes(x0, pw, "(b) branch cut")
    parts += ax
    # A SHELF, NOT A TENT. An apex at omega = 0 would make the cut read as a blunt version of
    # panel (a) -- the same near-miss defect the tower panel is mandated to avoid, in the other
    # direction. The cut's content is CONTINUOUS SUPPORT THROUGH ZERO with no isolated peak, so
    # the top is flat across the origin and falls only at the outer edges.
    top = yb - h * 0.55
    pts = [f"{x0 + 6},{yb}"]
    for i in range(0, pw - 11, 4):
        xx = x0 + 6 + i
        u = (xx - (x0 + pw / 2)) / (pw * 0.5)
        y = top + (h * 0.42) * (u ** 6)          # flat through the origin, soft outer falloff
        pts.append(f"{xx},{min(y, yb):.1f}")
    pts.append(f"{x0 + pw - 6},{yb}")
    parts.append(f'<polygon points="{" ".join(pts)}" fill="{BAR}" fill-opacity="0.35" '
                 f'stroke="{BAR}" stroke-width="1.5"/>')
    parts.append(f'<text x="{x0 + pw//2}" y="{top - 12}" text-anchor="middle" font-size="11" '
                 f'fill="{INK}">continuous through ω = 0 — no isolated peak</text>')
    # (c) gapped tower: discrete poles, none inside the gap; the gap annotated as the content
    x0 = 30 + 2 * (pw + 60)
    ax, yb, h = _axes(x0, pw, "(c) gapped tower")
    parts += ax
    # EQUAL HEIGHTS, DELIBERATELY. A tower drawn with its innermost poles tallest gives the eye
    # an envelope peaking at omega = 0 with a notch cut out -- i.e. it reads as an almost-single
    # pole, the exact impression this panel is mandated not to create. The claim here is
    # structural only: DISCRETE support, NONE below the gap. Residue magnitudes are not the
    # content, so they are not drawn as if they were. (Defect found in this figure's first
    # render, 2026-08-17, before screening; recorded here so a later edit does not reinstate it.)
    # geometry pinned so all six poles sit INSIDE the panel and symmetric about the origin:
    # gap_px + lead + 2*step must stay under pw/2 (found by rendering, 2026-08-17 -- the first
    # spacing ran the outermost poles off the panel and read as an asymmetric cluster).
    gap_px, lead, step = int(pw * 0.20), 12, 22
    assert gap_px + lead + 2 * step < pw // 2, "tower poles would run off the panel"
    ph = h * 0.62
    for sgn in (-1, 1):
        for k in range(3):
            px = x0 + pw // 2 + sgn * (gap_px + lead + k * step)
            parts.append(f'<line x1="{px}" y1="{yb}" x2="{px}" y2="{yb - ph:.0f}" '
                         f'stroke="{BAR}" stroke-width="3"/>')
            parts.append(f'<circle cx="{px}" cy="{yb - ph:.0f}" r="3" fill="{BAR}"/>')
    # the gap box spans the EMPTY interval only, and stops short of the innermost poles
    parts.append(f'<rect x="{x0 + pw//2 - gap_px}" y="{yb - ph - 6:.0f}" width="{2 * gap_px}" '
                 f'height="{ph + 6:.0f}" fill="none" stroke="{EMPTY}" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{x0 + pw//2}" y="{yb - ph - 34:.0f}" text-anchor="middle" '
                 f'font-size="11" fill="{EMPTY}">no support below the gap</text>')
    parts.append(f'<text x="{x0 + pw//2}" y="{yb - ph - 18:.0f}" text-anchor="middle" '
                 f'font-size="11" fill="{EMPTY}">— not a near-miss of (a)</text>')
    parts.append('</svg>')
    return "\n".join(parts)


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
