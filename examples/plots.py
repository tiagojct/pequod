"""Pequod showcase plots.

Generates four hero images that use the palette in matplotlib.
Saves them next to this script as PNGs at 2x DPI for sharp display.

Run with:
    pip install "pequod[plot]" numpy
    python plots.py

Each figure is built deliberately to show off one aspect of the
palette — categorical contrast, sequential interpolation, light vs
dark surfaces, and what crew accents look like under saturation.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import pequod

OUT = Path(__file__).resolve().parent
DPI = 200
RNG = np.random.default_rng(11)

# Register the colormaps once for the whole script.
pequod.register_cmaps()

# Light and dark surface palettes — keep the body-text/surface tokens
# as named constants so all four plots stay coherent.
PAPER     = pequod.LOG["Log 50"]
INK       = pequod.LOG["Log 950"]
INK_TEXT  = pequod.LOG["Log 100"]
PAPER_TEXT = pequod.LOG["Log 800"]
MUTED_DARK  = pequod.LOG["Log 300"]    # warm taupe for muted text on dark
MUTED_LIGHT = pequod.LOG["Log 600"]    # log 600 for muted text on light
GRID_DARK   = pequod.LOG["Log 800"]
GRID_LIGHT  = pequod.LOG["Log 200"]


def _set_typography():
    """Approximate the website's Geist look with system fonts."""
    mpl.rcParams.update({
        "font.family": ["Geist", "Inter", "Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size":   10,
        "axes.titlesize": 13,
        "axes.titleweight": "semibold",
        "axes.labelsize":  10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi":     DPI,
        "savefig.dpi":    DPI,
        "savefig.bbox":   "tight",
    })


def _theme(ax, *, dark: bool):
    """Apply a Pequod surface to the given axes."""
    surface = INK   if dark else PAPER
    text    = INK_TEXT if dark else PAPER_TEXT
    muted   = MUTED_DARK if dark else MUTED_LIGHT
    grid    = GRID_DARK if dark else GRID_LIGHT

    ax.set_facecolor(surface)
    ax.figure.set_facecolor(surface)
    for spine in ax.spines.values():
        spine.set_color(grid)
    ax.tick_params(colors=muted, which="both")
    ax.xaxis.label.set_color(text)
    ax.yaxis.label.set_color(text)
    ax.title.set_color(text)
    ax.grid(True, color=grid, linewidth=0.6, alpha=0.5)
    ax.set_axisbelow(True)


# ── 1. Hero: time series with all eight crew accents (dark) ────────────

def hero_dark():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    t = np.linspace(0, 4 * np.pi, 600)
    crew_dark = pequod.CREW_DARK
    series = list(crew_dark.items())

    for i, (name, hex_col) in enumerate(series):
        # Slightly varied phase + envelope to make the lines distinct.
        amp   = 1.0 + 0.05 * i
        phase = i * 0.55
        decay = 1.0 - 0.04 * i
        y = amp * np.sin(t * decay + phase) * np.exp(-t / 18) + 0.06 * i
        ax.plot(t, y, color=hex_col, linewidth=2.0, label=name, alpha=0.95)

    ax.set_title("Pequod — eight crew accents on Log 950 ink", loc="left", pad=14)
    ax.set_xlabel("t")
    ax.set_ylabel("amplitude")
    ax.set_xlim(0, 4 * np.pi)

    leg = ax.legend(
        loc="upper right", ncols=2, frameon=True,
        facecolor=pequod.LOG["Log 900"], edgecolor=GRID_DARK,
        labelcolor=INK_TEXT, fontsize=9, framealpha=0.92,
    )

    fig.savefig(OUT / "01_crew_dark.png")
    plt.close(fig)


# ── 2. Sequential heatmap on the Log scale ─────────────────────────────

def heatmap_log():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=True)

    # Smooth 2D field — sum of three radial bumps + low-amplitude noise.
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

    ax.set_title("Pequod Log scale as a continuous colormap", loc="left", pad=14)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    cbar = fig.colorbar(im, ax=ax, pad=0.015, shrink=0.92)
    cbar.outline.set_edgecolor(GRID_DARK)
    cbar.ax.tick_params(colors=MUTED_DARK)
    cbar.set_label("density", color=INK_TEXT)

    fig.savefig(OUT / "02_log_heatmap.png")
    plt.close(fig)


# ── 3. Light theme: distribution comparison (overlapping KDEs) ─────────

def distributions_light():
    _set_typography()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    _theme(ax, dark=False)

    crew_light = pequod.CREW_LIGHT
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
        col = crew_light[name]
        ax.fill_between(x, y, color=col, alpha=0.35, linewidth=0)
        ax.plot(x, y, color=col, linewidth=1.8, label=name)

    ax.set_title("Five overlapping distributions in the light palette", loc="left", pad=14)
    ax.set_xlabel("value")
    ax.set_ylabel("density")
    ax.set_xlim(-5, 6)

    leg = ax.legend(
        loc="upper right", frameon=True,
        facecolor=PAPER, edgecolor=GRID_LIGHT,
        labelcolor=PAPER_TEXT, fontsize=9, framealpha=0.95,
    )

    fig.savefig(OUT / "03_distributions_light.png")
    plt.close(fig)


# ── 4. Specimen-style swatch grid (light + dark in one figure) ─────────

def swatch_grid():
    _set_typography()
    fig, axes = plt.subplots(2, 1, figsize=(10, 5.4),
                             gridspec_kw={"height_ratios": [1.0, 1.0]})
    fig.set_facecolor(PAPER)

    # Top: Log scale, twelve swatches across.
    ax = axes[0]
    log_items = list(pequod.LOG.items())
    n_log = len(log_items)
    for i, (name, hex_col) in enumerate(log_items):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=hex_col, edgecolor="none"))
        # Auto-contrast label color
        r, g, b = int(hex_col[1:3], 16), int(hex_col[3:5], 16), int(hex_col[5:7], 16)
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        text_col = INK_TEXT if lum < 140 else PAPER_TEXT
        ax.text(i + 0.5, 0.66, name.replace("Log ", ""),
                ha="center", va="center", color=text_col,
                fontsize=11, fontweight="semibold")
        ax.text(i + 0.5, 0.32, hex_col,
                ha="center", va="center", color=text_col,
                fontsize=7.5, family="monospace")
    ax.set_xlim(0, n_log); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Log scale", loc="left", pad=10, color=PAPER_TEXT)

    # Bottom: crew light + dark, paired.
    ax = axes[1]
    crew_names = list(pequod.CREW_LIGHT.keys())
    n_crew = len(crew_names)
    for i, name in enumerate(crew_names):
        light = pequod.CREW_LIGHT[name]
        dark  = pequod.CREW_DARK[name]
        ax.add_patch(plt.Rectangle((i, 0.5), 1, 0.5, facecolor=light, edgecolor="none"))
        ax.add_patch(plt.Rectangle((i, 0.0), 1, 0.5, facecolor=dark,  edgecolor="none"))
        ax.text(i + 0.5, 1.08, name,
                ha="center", va="bottom", color=PAPER_TEXT,
                fontsize=10, fontweight="semibold")
        ax.text(i + 0.5, 0.75, light,
                ha="center", va="center", color=INK_TEXT,
                fontsize=7.2, family="monospace")
        ax.text(i + 0.5, 0.25, dark,
                ha="center", va="center", color=PAPER_TEXT,
                fontsize=7.2, family="monospace")
    ax.set_xlim(0, n_crew); ax.set_ylim(0, 1.18)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Crew accents — light (top) / dark (bottom)", loc="left",
                 pad=18, color=PAPER_TEXT)

    fig.suptitle("", y=0.0)  # silence default
    fig.tight_layout(h_pad=2.0)
    fig.savefig(OUT / "04_swatches.png")
    plt.close(fig)


def main():
    hero_dark()
    heatmap_log()
    distributions_light()
    swatch_grid()
    print("Wrote:")
    for p in sorted(OUT.glob("*.png")):
        size_kb = p.stat().st_size / 1024
        print(f"  {p.name:<28s} {size_kb:6.1f} KB")


if __name__ == "__main__":
    main()
