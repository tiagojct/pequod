# Examples

Four hero images that show what Pequod looks like in matplotlib —
two on the dark surface, two on light. Reproduce them with:

```bash
pip install "pequod[plot]" numpy
python examples/plots.py
```

The full source for every figure below is in
[`plots.py`](plots.py); fewer than 200 lines, no helpers beyond
`pequod.register_cmaps()` and a tiny `_theme()` function that
applies the palette's surface tokens to a matplotlib axes.

## 1 — Crew accents on dark (Log 950)

Eight sine series, each in a different crew dark variant, on a
Log 950 ink surface. The accents stay in their pigment register
without competing.

![Crew accents on dark](01_crew_dark.png)

## 2 — Log scale as a continuous colormap

Three Gaussian bumps rendered with `pequod_log` registered as a
matplotlib colormap. The warm-paper → deep-ink ramp does the
heavy lifting: the eye reads the scalar field instantly, with
no banding and no rainbow distortion.

![Log heatmap](02_log_heatmap.png)

## 3 — Five distributions on light (Log 50)

Overlapping Gaussian densities with crew light variants, semi-
transparent fills layered against Log 50 paper. None of the five
collapse to the same hue under standard vision.

![Distributions on light](03_distributions_light.png)

## 4 — Specimen-style swatch grid

The full Log scale (twelve steps) and the eight crew accents
(light + dark) in one figure. Auto-contrast labels — cream on
the dark cells, navy on the light ones.

![Swatch grid](04_swatches.png)

## What the script shows you

If you want to lift bits into your own plotting code, the
patterns worth borrowing are:

- **`pequod.register_cmaps()`** — call once per process, then
  use `cmap="pequod_log"` and friends like any built-in
  matplotlib colormap.
- **A small `_theme(ax, dark=True/False)` helper** — sets the
  axes facecolor to `pequod.LOG["Log 50"]` or `Log 950`,
  picks matching text and grid colours from the same scale,
  and turns off the top/right spines. This is enough to make
  every figure look "Pequod" without retouching by hand.
- **`pequod.CREW_DARK[name]`** for series colours on dark
  backgrounds and **`pequod.CREW_LIGHT[name]`** on paper. They
  are already tuned for those surfaces.

## Reproducing on your machine

The script uses Geist as its primary font (matching the rest of
the project) and falls back to Inter, Helvetica Neue, Arial, and
DejaVu Sans in that order. Install
[Geist](https://fonts.google.com/specimen/Geist) for the closest
match; everything else still renders, just with a different
typeface.
