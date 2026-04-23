#!/usr/bin/env python3
"""
Viénot–Brettel–Mollon CVD simulation + pairwise ΔE report for Pequod accents.

Reads the accent list from pequod.json (sibling of the `scripts/` folder),
simulates each accent at 100 % severity for protanopia, deuteranopia,
and tritanopia, and reports pairwise CIE76 ΔE*ab distances between the
simulated accents in each condition.

ΔE interpretation:
  ~ 1      just-noticeable difference
  ~ 5      perceptible but similar
  ~ 10     the rough boundary at which two colours stop reading as distinct
  >= 15    clearly separable

Dependency: NumPy.

Usage:
    python3 scripts/cvd_check.py

Reference:
    Viénot F, Brettel H, Mollon JD. Digital video colourmaps for checking
    the legibility of displays by dichromats. Color Res Appl. 1999;24(4):
    243–252. doi:10.1002/(SICI)1520-6378(199908)24:4<243::AID-COL5>3.0.CO;2-0
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np


# ── sRGB <-> linear light ───────────────────────────────────────────────

def srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c: np.ndarray) -> np.ndarray:
    c = np.clip(np.asarray(c, dtype=float), 0, 1)
    out = np.where(c <= 0.0031308, 12.92 * c, 1.055 * c ** (1 / 2.4) - 0.055)
    return np.clip(np.round(out * 255), 0, 255).astype(int)


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


# ── Viénot–Brettel–Mollon matrices (LMS space, severity 1.0) ────────────

RGB2LMS = np.array(
    [
        [17.8824, 43.5161, 4.11935],
        [3.45565, 27.1554, 3.86714],
        [0.0299566, 0.184309, 1.46709],
    ]
)
LMS2RGB = np.linalg.inv(RGB2LMS)

SIM_MATRICES = {
    "protanopia": np.array(
        [
            [0.0, 2.02344, -2.52581],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    ),
    "deuteranopia": np.array(
        [
            [1.0, 0.0, 0.0],
            [0.494207, 0.0, 1.24827],
            [0.0, 0.0, 1.0],
        ]
    ),
    "tritanopia": np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [-0.395913, 0.801109, 0.0],
        ]
    ),
}


def simulate(hex_in: str, sim_matrix: np.ndarray) -> str:
    rgb = np.array(hex_to_rgb(hex_in))
    lin = srgb_to_linear(rgb)
    lms = RGB2LMS @ lin
    lms_sim = sim_matrix @ lms
    lin_sim = LMS2RGB @ lms_sim
    return rgb_to_hex(linear_to_srgb(lin_sim))


# ── sRGB → CIELAB (D65) for ΔE ─────────────────────────────────────────

RGB2XYZ = np.array(
    [
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041],
    ]
)
WHITE_D65 = np.array([0.95047, 1.0, 1.08883])


def lab(hex_in: str) -> np.ndarray:
    rgb = np.array(hex_to_rgb(hex_in))
    lin = srgb_to_linear(rgb)
    xyz = RGB2XYZ @ lin
    xyzn = xyz / WHITE_D65
    delta = 6 / 29
    f = lambda t: np.where(t > delta ** 3, t ** (1 / 3), t / (3 * delta ** 2) + 4 / 29)
    fx, fy, fz = f(xyzn)
    L = 116 * fy - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)
    return np.array([L, a, b])


def delta_e(h1: str, h2: str) -> float:
    return float(np.linalg.norm(lab(h1) - lab(h2)))


# ── Report ─────────────────────────────────────────────────────────────


def analyse(label: str, colours: list[tuple[str, str]], matrix: np.ndarray) -> None:
    sim = [(name, simulate(hex_val, matrix)) for name, hex_val in colours]

    print(f"\n── {label} ─────────────────")
    for (name, hex_val), (_, hex_sim) in zip(colours, sim):
        print(f"  {name:10s} {hex_val} → {hex_sim}")

    distances: list[tuple[str, str, float]] = []
    for i in range(len(sim)):
        for j in range(i + 1, len(sim)):
            n1, c1 = sim[i]
            n2, c2 = sim[j]
            distances.append((n1, n2, delta_e(c1, c2)))

    distances.sort(key=lambda x: x[2])
    n1, n2, d = distances[0]
    print(f"  closest pair: {n1} ↔ {n2}  ΔE = {d:.1f}")

    flagged = [(n1, n2, d) for n1, n2, d in distances if d < 15]
    if flagged:
        print("  potentially confusable (ΔE < 15):")
        for n1, n2, d in flagged:
            verdict = "✗ confusable" if d < 10 else "⚠ close"
            print(f"    {n1:10s} ↔ {n2:10s}  ΔE = {d:5.1f}  {verdict}")
    else:
        print("  ✓ all pairs ΔE ≥ 15 — clearly separable")


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    palette_path = repo_root / "pequod.json"

    if not palette_path.exists():
        print(f"error: {palette_path} not found", file=sys.stderr)
        return 2

    with palette_path.open() as f:
        palette = json.load(f)

    accents = palette.get("accents", {})
    if not accents:
        print("error: no accents defined in pequod.json", file=sys.stderr)
        return 2

    crew_light = [(name.capitalize(), spec["light"]) for name, spec in accents.items()]
    crew_dark = [(name.capitalize(), spec["dark"]) for name, spec in accents.items()]

    print("═══════════════ LIGHT VARIANTS ═══════════════")
    for cvd_name, matrix in SIM_MATRICES.items():
        analyse(f"light · {cvd_name}", crew_light, matrix)

    print("\n═══════════════ DARK VARIANTS ═══════════════")
    for cvd_name, matrix in SIM_MATRICES.items():
        analyse(f"dark · {cvd_name}", crew_dark, matrix)

    return 0


if __name__ == "__main__":
    sys.exit(main())
