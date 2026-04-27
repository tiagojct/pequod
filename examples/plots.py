"""Pequod showcase plots.

Generates eight hero images that use the palette in matplotlib —
four on dark surfaces, four on light. Saves each one next to this
script as a 200-DPI PNG.

Run with:
    pip install "pequod[plot]" numpy
    python plots.py

Designed to mirror the website typography: titles set in Atkinson
Hyperlegible Next SemiBold, body text in Atkinson Hyperlegible Next,
monospace ticks/labels in JetBrains Mono. matplotlib falls back
through Inter / Helvetica Neue / DejaVu Sans if Atkinson Hyperlegible
Next is not installed.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

import pequod

OUT = Path(__file__).resolve().parent
DPI = 200
RNG = np.random.default_rng(11)

# matplotlib's font scanner skips filenames containing '[' (the
# variable-axis convention used by Google Fonts), so a user-installed
# `AtkinsonHyperlegibleNext[wght].ttf` won't be discovered automatically.
# Register any matching variable font explicitly.
def _register_user_variable_fonts(*name_fragments: str) -> None:
    user_font_dirs = (Path.home() / "Library" / "Fonts", Path.home() / ".local" / "share" / "fonts")
    for d in user_font_dirs:
        if not d.is_dir():
            continue
        for path in d.glob("*.ttf"):
            if any(frag.lower() in path.name.lower() for frag in name_fragments):
                fm.fontManager.addfont(str(path))

_register_user_variable_fonts("AtkinsonHyperlegibleNext", "JetBrainsMono")

# Register the colormaps once for the whole script.
pequod.register_cmaps()

# Surface tokens — keep these constants aligned with the website.
PAPER       = pequod.LOG["Log 50"]
INK         = pequod.LOG["Log 950"]
INK_TEXT    = pequod.LOG["Log 100"]
PAPER_TEXT  = pequod.LOG["Log 800"]
HEAD_DARK   = pequod.LOG["Log 150"]    # parchment for dark-mode titles
HEAD_LIGHT  = pequod.LOG["Log 800"]    # navy for light-mode titles
MUTED_DARK  = pequod.LOG["Log 300"]
MUTED_LIGHT = pequod.LOG["Log 600"]
GRID_DARK   = pequod.LOG["Log 800"]
GRID_LIGHT  = pequod.LOG["Log 200"]


def _set_typography():
    """Match the website typography: Atkinson Hyperlegible Next for prose, JetBrains Mono for code/ticks."""
    mpl.rcParams.update({
        "font.family":      ["Atkinson Hyperlegible Next", "Inter", "Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size":        11,
        "axes.titlesize":   16,
        "axes.titleweight": 600,
        "axes.titlepad":    18,
        "axes.titlelocation": "left",
        "axes.labelsize":   11,
        "axes.labelweight": 500,
        "axes.labelpad":    8,
        "xtick.labelsize":  9.5,
        "ytick.labelsize":  9.5,
        "legend.fontsize":  9.5,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi":  DPI,
        "savefig.dpi": DPI,
        "savefig.bbox": "tight",
        # Tick labels in JetBrains Mono so digits line up.
        "xtick.color": MUTED_DARK,
        "ytick.color": MUTED_DARK,
    })


def _theme(ax, *, dark: bool, mono_ticks: bool = True):
    """Paint axes with the appropriate Pequod surface.

    Note: this does NOT set the title colour. matplotlib's
    ``set_title`` always overrides title colour from rcParams, which
    means anything set here gets clobbered when the plot calls
    ``ax.set_title(...)`` later. Use the :func:`_title` helper after
    plotting to set both the text and a contrasting colour.
    """
    surface = INK if dark else PAPER
    body    = INK_TEXT if dark else PAPER_TEXT
    muted   = MUTED_DARK if dark else MUTED_LIGHT
    grid    = GRID_DARK if dark else GRID_LIGHT

    ax.set_facecolor(surface)
    ax.figure.set_facecolor(surface)
    for spine in ax.spines.values():
        spine.set_color(grid)
        spine.set_linewidth(0.8)
    ax.tick_params(colors=muted, which="both", length=4, width=0.7)
    if mono_ticks:
        for lab in ax.get_xticklabels() + ax.get_yticklabels():
            lab.set_fontfamily(["JetBrains Mono", "SF Mono", "DejaVu Sans Mono"])
            lab.set_color(muted)
    ax.xaxis.label.set_color(body)
    ax.yaxis.label.set_color(body)
    ax.grid(True, color=grid, linewidth=0.6, alpha=0.55)
    ax.set_axisbelow(True)


def _title(ax, text, *, dark: bool, **kwargs):
    """Set a left-aligned title in Atkinson Hyperlegible Next SemiBold with the right contrast."""
    color = HEAD_DARK if dark else HEAD_LIGHT
    ax.set_title(text, color=color, fontweight=600, fontsize=16,
                 loc="left", pad=18, **kwargs)


def _legend(ax, *, dark: bool, **kwargs):
    bg   = pequod.LOG["Log 900"] if dark else PAPER
    edge = GRID_DARK if dark else GRID_LIGHT
    text = INK_TEXT if dark else PAPER_TEXT
    leg = ax.legend(
        frameon=True, facecolor=bg, edgecolor=edge,
        labelcolor=text, framealpha=0.92, **kwargs,
    )
    return leg


# ── 1. Hero: time series with all eight crew accents (dark) ────────────

def hero_dark():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    t = np.linspace(0, 4 * np.pi, 600)
    crew = pequod.CREW_DARK
    for i, (name, hex_col) in enumerate(crew.items()):
        amp   = 1.0 + 0.05 * i
        phase = i * 0.55
        decay = 1.0 - 0.04 * i
        y = amp * np.sin(t * decay + phase) * np.exp(-t / 18) + 0.06 * i
        ax.plot(t, y, color=hex_col, linewidth=2.0, label=name, alpha=0.95)

    _title(ax, "Eight crew accents on Log 950 ink", dark=True)
    ax.set_xlabel("t")
    ax.set_ylabel("amplitude")
    ax.set_xlim(0, 4 * np.pi)
    _legend(ax, dark=True, loc="upper right", ncols=2)

    fig.savefig(OUT / "01_crew_dark.png")
    plt.close(fig)


# ── 2. Sequential heatmap on the Log scale ─────────────────────────────

def heatmap_log():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    n = 280
    x = np.linspace(-3, 3, n)
    y = np.linspace(-2, 2, int(n * 0.6))
    X, Y = np.meshgrid(x, y)

    Z = (
        np.exp(-((X + 1.2) ** 2 + (Y + 0.5) ** 2) / 1.4)
        + 0.85 * np.exp(-((X - 1.0) ** 2 + (Y - 0.7) ** 2) / 0.9)
        + 0.55 * np.exp(-((X - 0.4) ** 2 + (Y + 0.9) ** 2) / 0.4)
    )
    Z += 0.03 * RNG.standard_normal(Z.shape)

    im = ax.imshow(
        Z, cmap="pequod_log", aspect="auto", origin="lower",
        extent=[x.min(), x.max(), y.min(), y.max()],
        interpolation="bilinear",
    )

    _title(ax, "Log scale as a continuous colormap", dark=True)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    cbar = fig.colorbar(im, ax=ax, pad=0.015, shrink=0.92)
    cbar.outline.set_edgecolor(GRID_DARK)
    cbar.ax.tick_params(colors=MUTED_DARK)
    cbar.set_label("density", color=INK_TEXT)
    for lab in cbar.ax.get_yticklabels():
        lab.set_fontfamily(["JetBrains Mono", "SF Mono", "DejaVu Sans Mono"])

    fig.savefig(OUT / "02_log_heatmap.png")
    plt.close(fig)


# ── 3. Light theme: distribution comparison (overlapping KDEs) ─────────

def distributions_light():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=False)

    crew = pequod.CREW_LIGHT
    pairs = [
        ("Tashtego", -0.3, 0.95),
        ("Starbuck",  0.6, 1.15),
        ("Pip",       1.7, 0.80),
        ("Daggoo",    2.5, 1.25),
        ("Queequeg", -1.4, 1.05),
    ]
    x = np.linspace(-5, 6, 800)
    for name, mu, sigma in pairs:
        y = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
        col = crew[name]
        ax.fill_between(x, y, color=col, alpha=0.32, linewidth=0)
        ax.plot(x, y, color=col, linewidth=1.8, label=name)

    _title(ax, "Five overlapping distributions on Log 50 paper", dark=False)
    ax.set_xlabel("value"); ax.set_ylabel("density")
    ax.set_xlim(-5, 6)
    _legend(ax, dark=False, loc="upper right")

    fig.savefig(OUT / "03_distributions_light.png")
    plt.close(fig)


# ── 4. Specimen-style swatch grid ──────────────────────────────────────

def swatch_grid():
    _set_typography()
    fig, axes = plt.subplots(2, 1, figsize=(10, 5.4),
                             gridspec_kw={"height_ratios": [1.0, 1.0]})
    fig.set_facecolor(PAPER)

    ax = axes[0]
    items = list(pequod.LOG.items())
    n = len(items)
    for i, (name, hex_col) in enumerate(items):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=hex_col, edgecolor="none"))
        r, g, b = int(hex_col[1:3], 16), int(hex_col[3:5], 16), int(hex_col[5:7], 16)
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        text_col = INK_TEXT if lum < 140 else PAPER_TEXT
        ax.text(i + 0.5, 0.66, name.replace("Log ", ""),
                ha="center", va="center", color=text_col,
                fontsize=12, fontweight=600)
        ax.text(i + 0.5, 0.32, hex_col,
                ha="center", va="center", color=text_col,
                fontsize=8, family="JetBrains Mono")
    ax.set_xlim(0, n); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Log scale", color=PAPER_TEXT)

    ax = axes[1]
    crew_names = list(pequod.CREW_LIGHT.keys())
    n = len(crew_names)
    for i, name in enumerate(crew_names):
        light = pequod.CREW_LIGHT[name]
        dark  = pequod.CREW_DARK[name]
        ax.add_patch(plt.Rectangle((i, 0.5), 1, 0.5, facecolor=light, edgecolor="none"))
        ax.add_patch(plt.Rectangle((i, 0.0), 1, 0.5, facecolor=dark,  edgecolor="none"))
        ax.text(i + 0.5, 1.08, name, ha="center", va="bottom",
                color=PAPER_TEXT, fontsize=11, fontweight=600)
        ax.text(i + 0.5, 0.75, light, ha="center", va="center",
                color=INK_TEXT, fontsize=7.5, family="JetBrains Mono")
        ax.text(i + 0.5, 0.25, dark, ha="center", va="center",
                color=PAPER_TEXT, fontsize=7.5, family="JetBrains Mono")
    ax.set_xlim(0, n); ax.set_ylim(0, 1.18)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Crew accents — light (top) / dark (bottom)", color=PAPER_TEXT)

    fig.tight_layout(h_pad=2.0)
    fig.savefig(OUT / "04_swatches.png")
    plt.close(fig)


# ── 5. Scatter — categorical clusters with crew light ──────────────────

def scatter_light():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=False)

    crew = pequod.CREW_LIGHT
    centres = {
        "Ahab":     ( 1.6,  2.3),
        "Starbuck": (-2.0,  0.4),
        "Tashtego": ( 0.2, -1.6),
        "Pip":      ( 2.6, -0.6),
        "Queequeg": (-1.2,  2.2),
    }
    for name, (mx, my) in centres.items():
        n = 90
        x = RNG.normal(mx, 0.55, n)
        y = RNG.normal(my, 0.55, n)
        ax.scatter(x, y, s=42, color=crew[name],
                   edgecolor=PAPER, linewidth=0.6, alpha=0.85, label=name)

    _title(ax, "Five clusters in crew light variants", dark=False)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_xlim(-4, 4.5); ax.set_ylim(-3, 4)
    _legend(ax, dark=False, loc="lower left")

    fig.savefig(OUT / "05_scatter_light.png")
    plt.close(fig)


# ── 6. Bar chart — grouped, on dark ────────────────────────────────────

def bars_dark():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    categories = ["Q1", "Q2", "Q3", "Q4"]
    series = [
        ("Ahab",     [4.2, 5.1, 4.8, 6.0]),
        ("Starbuck", [3.5, 4.0, 5.2, 5.7]),
        ("Tashtego", [2.8, 3.9, 4.6, 5.4]),
        ("Pip",      [3.1, 3.4, 3.0, 3.9]),
    ]
    crew = pequod.CREW_DARK
    n_groups = len(categories)
    n_series = len(series)
    width = 0.8 / n_series
    x = np.arange(n_groups)

    for i, (name, vals) in enumerate(series):
        offset = (i - (n_series - 1) / 2) * width
        ax.bar(x + offset, vals, width=width * 0.92,
               color=crew[name], label=name, edgecolor="none")

    _title(ax, "Quarterly throughput by team", dark=True)
    ax.set_xlabel("quarter"); ax.set_ylabel("throughput  (a.u.)")
    ax.set_xticks(x); ax.set_xticklabels(categories)
    for lab in ax.get_xticklabels():
        lab.set_fontfamily(["JetBrains Mono", "SF Mono", "DejaVu Sans Mono"])
        lab.set_color(MUTED_DARK)
    _legend(ax, dark=True, loc="upper left", ncols=2)

    fig.savefig(OUT / "06_bars_dark.png")
    plt.close(fig)


# ── 7. Horizontal bars (columns) — sorted, light ───────────────────────

def hbars_light():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=False)

    crew = pequod.CREW_LIGHT
    items = [
        ("Ahab",     7.4),
        ("Starbuck", 6.1),
        ("Queequeg", 5.7),
        ("Daggoo",   4.9),
        ("Tashtego", 4.3),
        ("Pip",      3.6),
        ("Stubb",    3.2),
        ("Ishmael",  2.8),
    ]
    items.sort(key=lambda kv: kv[1])
    names = [name for name, _ in items]
    vals  = [v for _, v in items]
    cols  = [crew[name] for name in names]

    y = np.arange(len(names))
    ax.barh(y, vals, color=cols, edgecolor="none", height=0.72)

    # Value annotations at each bar's tip.
    for yi, v in zip(y, vals):
        ax.text(v + 0.12, yi, f"{v:.1f}",
                va="center", ha="left",
                color=PAPER_TEXT, fontsize=9.5,
                fontfamily=["JetBrains Mono", "SF Mono", "DejaVu Sans Mono"])

    ax.set_yticks(y); ax.set_yticklabels(names)
    for lab in ax.get_yticklabels():
        lab.set_fontfamily(["Atkinson Hyperlegible Next", "Inter", "DejaVu Sans"])
        lab.set_color(PAPER_TEXT)
    _title(ax, "Crew rank by mentions in the corpus", dark=False)
    ax.set_xlabel("mentions  ×  10³")
    ax.set_xlim(0, max(vals) * 1.16)
    ax.spines["left"].set_visible(False)

    fig.savefig(OUT / "07_hbars_light.png")
    plt.close(fig)


# ── 8. Box plot — distributions per crew member, dark ──────────────────

def boxplot_dark():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    crew = pequod.CREW_DARK
    names = list(crew.keys())
    # Eight skewed distributions with different spread per crew.
    data = []
    for i, name in enumerate(names):
        n = 180
        loc   = -0.6 + 0.18 * i + 0.18 * np.sin(i * 1.7)
        scale = 0.7 + 0.05 * (i % 4)
        sample = RNG.normal(loc, scale, n)
        # Gentle skew on a few series.
        if i % 3 == 0:
            sample = sample + 0.6 * RNG.gamma(1.5, 0.4, n)
        data.append(sample)

    box = ax.boxplot(
        data, vert=True, patch_artist=True, widths=0.55,
        medianprops=dict(color=INK_TEXT, linewidth=1.6),
        whiskerprops=dict(color=MUTED_DARK, linewidth=1.0),
        capprops=dict(color=MUTED_DARK, linewidth=1.0),
        flierprops=dict(marker="o", markersize=3.5,
                        markerfacecolor=MUTED_DARK,
                        markeredgecolor="none", alpha=0.55),
    )
    for patch, name in zip(box["boxes"], names):
        patch.set_facecolor(crew[name])
        patch.set_alpha(0.85)
        patch.set_edgecolor("none")

    ax.set_xticks(np.arange(1, len(names) + 1))
    ax.set_xticklabels(names)
    for lab in ax.get_xticklabels():
        lab.set_fontfamily(["Atkinson Hyperlegible Next", "Inter", "DejaVu Sans"])
        lab.set_color(INK_TEXT)
    _title(ax, "Per-crew distribution — eight box plots", dark=True)
    ax.set_ylabel("value")

    fig.savefig(OUT / "08_boxplot_dark.png")
    plt.close(fig)


def main():
    hero_dark()
    heatmap_log()
    distributions_light()
    swatch_grid()
    scatter_light()
    bars_dark()
    hbars_light()
    boxplot_dark()
    print("Wrote:")
    for p in sorted(OUT.glob("*.png")):
        size_kb = p.stat().st_size / 1024
        print(f"  {p.name:<32s} {size_kb:6.1f} KB")


if __name__ == "__main__":
    main()
