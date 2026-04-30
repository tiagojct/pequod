#!/usr/bin/env python3
"""
Design + verify a corrected Pequod palette.

Produces candidate hex codes for `log` (12-step sequential) and the
`crew` (8 qualitative) light + dark variants, then runs the same
Viénot-Brettel-Mollon CVD simulation as scripts/cvd_check.py against
the candidates so we can iterate to a CVD-safe set before propagating
to pequod.json.

Design constraints:
  log         monotonic decrease in CIELAB L*, even step sizes,
              warm-paper to deep-ink character preserved
  crew light  L* clustered near 48, hues spread across the wheel,
              every CVD pair ΔE >= 12
  crew dark   L* clustered near 72, same hues as light
  characters  red=Ahab, blue=Starbuck, indigo=Queequeg,
              yellow=Pip, grey=Ishmael, orange=Stubb,
              green=Tashtego, brown=Daggoo  (roles fixed)

Run:
    python3 scripts/design_palette.py
"""
from __future__ import annotations

import colorsys
import math
import sys
from itertools import combinations
from pathlib import Path

import numpy as np


# ── sRGB <-> linear / hex ──────────────────────────────────────────────

def hex_to_rgb(h: str) -> np.ndarray:
    h = h.lstrip("#")
    return np.array([int(h[i : i + 2], 16) for i in (0, 2, 4)], dtype=float)


def rgb_to_hex(rgb) -> str:
    rgb = np.clip(np.round(rgb), 0, 255).astype(int)
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c: np.ndarray) -> np.ndarray:
    c = np.clip(np.asarray(c, dtype=float), 0, 1)
    out = np.where(c <= 0.0031308, 12.92 * c, 1.055 * c ** (1 / 2.4) - 0.055)
    return np.clip(np.round(out * 255), 0, 255).astype(int)


# ── sRGB → CIELAB (D65) ────────────────────────────────────────────────

RGB2XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041],
])
WHITE_D65 = np.array([0.95047, 1.0, 1.08883])


def lab_from_hex(h: str) -> np.ndarray:
    rgb = hex_to_rgb(h)
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


def deltaE(h1: str, h2: str) -> float:
    return float(np.linalg.norm(lab_from_hex(h1) - lab_from_hex(h2)))


# ── CIELAB → sRGB (D65) ────────────────────────────────────────────────
# Inverse of the above, used by `lch_to_hex` to materialise designed stops.

XYZ2RGB = np.linalg.inv(RGB2XYZ)


def lab_to_xyz(L: float, a: float, b: float) -> np.ndarray:
    fy = (L + 16) / 116
    fx = a / 500 + fy
    fz = fy - b / 200
    delta = 6 / 29
    f_inv = lambda t: np.where(t > delta, t ** 3, 3 * delta ** 2 * (t - 4 / 29))
    xyz = WHITE_D65 * f_inv(np.array([fx, fy, fz]))
    return xyz


def lch_to_hex(L: float, C: float, h_deg: float) -> str:
    """LCH -> hex. Out-of-gamut values are clipped silently — we report
    those at the end so the designer can pull C down."""
    h_rad = math.radians(h_deg)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)
    xyz = lab_to_xyz(L, a, b)
    rgb_lin = XYZ2RGB @ xyz
    rgb = linear_to_srgb(rgb_lin)
    return rgb_to_hex(rgb)


def in_gamut(L: float, C: float, h_deg: float, tol: float = 0.01) -> bool:
    """True if the LCH triple round-trips cleanly through sRGB."""
    h_rad = math.radians(h_deg)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)
    xyz = lab_to_xyz(L, a, b)
    rgb_lin = XYZ2RGB @ xyz
    return bool(np.all(rgb_lin >= -tol) and np.all(rgb_lin <= 1 + tol))


# ── CVD simulation (Viénot-Brettel-Mollon, severity 1.0) ──────────────

RGB2LMS = np.array([
    [17.8824, 43.5161, 4.11935],
    [3.45565, 27.1554, 3.86714],
    [0.0299566, 0.184309, 1.46709],
])
LMS2RGB = np.linalg.inv(RGB2LMS)

SIM_MATRICES = {
    "protan": np.array([[0.0, 2.02344, -2.52581], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]),
    "deutan": np.array([[1.0, 0.0, 0.0], [0.494207, 0.0, 1.24827], [0.0, 0.0, 1.0]]),
    "tritan": np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-0.395913, 0.801109, 0.0]]),
}


def simulate(h: str, matrix: np.ndarray) -> str:
    rgb = hex_to_rgb(h)
    lin = srgb_to_linear(rgb)
    lms = RGB2LMS @ lin
    lms_sim = matrix @ lms
    lin_sim = LMS2RGB @ lms_sim
    return rgb_to_hex(linear_to_srgb(lin_sim))


# ── Designed log ramp ──────────────────────────────────────────────────
# 12 stops at evenly-spaced L* from 96 -> 7. Hue rotates from a warm
# tan band (~75°) at the top to a cool ink band (~245°) at the bottom,
# with a gentle taper through the middle so the perceptual shift feels
# continuous instead of the abrupt step-8/9 jump in the v0.1 ramp.

LOG_DESIGN = [
    # (L*,  C,    h°,   stop name)
    (96.0,  3.0,   80.0, "50"),
    (90.0,  6.0,   78.0, "100"),
    (82.0, 12.0,   75.0, "150"),
    (73.0, 22.0,   70.0, "200"),
    (62.0, 30.0,   62.0, "300"),
    (51.0, 30.0,   55.0, "400"),
    (42.0, 22.0,   48.0, "500"),
    (33.0, 14.0,  240.0, "600"),
    (25.0, 18.0,  248.0, "700"),
    (18.0, 16.0,  252.0, "800"),
    (12.0, 12.0,  254.0, "900"),
    ( 7.0,  8.0,  256.0, "950"),
]


# ── Designed crew (LCH) ────────────────────────────────────────────────
# Light variants target L*=48 against a Log-100 paper; dark variants
# target L*=72 against Log-950 ink. Hues are chosen for max CVD-safe
# spread while keeping each character's brand role.

CREW_DESIGN = [
    # name      role     light(L,C,h)        dark(L,C,h)
    # L* deliberately laddered so confusable hue pairs (red/green,
    # orange/green, blue/indigo, yellow/orange) separate by lightness
    # under CVD even when hue collapses. Light L* span: 28 -> 82.
    # Dark L* span: 50 -> 92, mirroring the light ladder ~+22 L*.
    # Constraints:
    #   - Light L* in [22, 55] so every accent reads as syntax foreground
    #     on Log-100 paper (background L*=90).
    #   - Dark L* in [60, 92] so every accent reads on Log-950 ink (L*=8).
    #   - Every CVD pair under deutan + protan must clear ΔE >= 10.
    #   - Tritan accepts ΔE >= 7 for the yellow/orange pair (Pip ↔ Stubb)
    #     because two warm hues at similar L collapse under tritan and
    #     pushing them apart would break readability or hue identity.
    #     Tritan deficiency is rare (~0.01 %); the trade is documented.
    #
    # Hue tuning:
    #   ahab     vermillion (h=32) — better deutan separation from green
    #   tashtego cyan-green (h=165) — same reasoning, opposite side
    #   pip      shifted toward citrine (h=95) and pushed darker so it
    #            separates from stubb under deutan as well as in normal
    #            vision; gives up some "lemon" character to gain safety
    # Pip light is a darker mustard/ochre (L*=34, not bright lemon) so
    # it stays readable as syntax foreground on Log-100 paper AND gives
    # tritan separation from Stubb (orange) by lightness alone.
    # Pip dark stays light enough to read on Log-950 ink.
    ("daggoo",   "brown",  (22, 24,  32),  (52, 22,  32)),
    ("queequeg", "indigo", (28, 44, 290),  (60, 38, 290)),
    ("ahab",     "red",    (40, 54,  32),  (66, 40,  32)),
    ("tashtego", "green",  (46, 40, 160),  (74, 30, 160)),
    ("pip",      "yellow", (34, 50,  82),  (80, 42,  92)),
    ("ishmael",  "grey",   (48,  4,  80),  (76,  3,  80)),
    ("starbuck", "blue",   (50, 38, 245),  (86, 24, 245)),
    ("stubb",    "orange", (54, 58,  50),  (90, 24,  60)),
]


# ── Build + report ─────────────────────────────────────────────────────

def build_log() -> dict[str, str]:
    out = {}
    for L, C, h, name in LOG_DESIGN:
        if not in_gamut(L, C, h):
            print(f"  ! Log {name} out of gamut at L={L} C={C} h={h}", file=sys.stderr)
        out[f"Log {name}"] = lch_to_hex(L, C, h)
    return out


def build_crew() -> dict[str, dict[str, str]]:
    out = {}
    for name, role, light, dark in CREW_DESIGN:
        for variant, (L, C, h) in (("light", light), ("dark", dark)):
            if not in_gamut(L, C, h):
                print(f"  ! {name}.{variant} out of gamut at L={L} C={C} h={h}",
                      file=sys.stderr)
        out[name] = {
            "light": lch_to_hex(*light),
            "dark":  lch_to_hex(*dark),
            "role":  role,
        }
    return out


def report_log(log: dict[str, str]) -> None:
    print("\n=== log (sequential) ===")
    Ls = []
    for k, v in log.items():
        L = lab_from_hex(v)[0]
        Ls.append(L)
        print(f"  {k:8s} {v}  L*={L:5.1f}")
    diffs = np.diff(Ls)
    print(f"  ΔL* between stops: {' '.join(f'{d:+5.1f}' for d in diffs)}")
    print(f"  monotonic decrease: {all(d < 0 for d in diffs)}  "
          f"min step {min(abs(d) for d in diffs):.1f}  "
          f"max step {max(abs(d) for d in diffs):.1f}")


def report_crew(crew: dict[str, dict[str, str]], variant: str) -> None:
    print(f"\n=== crew · {variant} ===")
    pairs = [(n, c[variant]) for n, c in crew.items()]
    for n, c in pairs:
        L, a, b = lab_from_hex(c)
        h = (math.degrees(math.atan2(b, a)) + 360) % 360
        chroma = math.hypot(a, b)
        print(f"  {n:9s} {c}  L*={L:5.1f}  C={chroma:5.1f}  h={h:5.1f}°")

    # Pairwise normal + CVD ΔE — flag worst pair per condition.
    for cvd_name, matrix in [("normal", None)] + list(SIM_MATRICES.items()):
        sim = [
            (n, simulate(c, matrix) if matrix is not None else c)
            for n, c in pairs
        ]
        worst = min(
            (
                (n1, n2, deltaE(s1, s2))
                for (n1, s1), (n2, s2) in combinations(sim, 2)
            ),
            key=lambda x: x[2],
        )
        verdict = "OK" if worst[2] >= 10 else ("WARN" if worst[2] >= 6 else "FAIL")
        print(
            f"  {cvd_name:7s} worst {worst[0]:9s} ↔ {worst[1]:9s} "
            f"ΔE={worst[2]:5.1f}  [{verdict}]"
        )


def main() -> int:
    log = build_log()
    crew = build_crew()

    report_log(log)
    report_crew(crew, "light")
    report_crew(crew, "dark")

    print("\n--- proposed JSON fragments ---")
    print('"log": {')
    print(",\n".join(f'    "{k.split()[1]}": "{v}"' for k, v in log.items()))
    print("},")
    print('"accents": {')
    blocks = []
    for n, c in crew.items():
        blocks.append(
            f'    "{n}": {{ "light": "{c["light"]}", "dark": "{c["dark"]}", '
            f'"role": "{c["role"]}" }}'
        )
    print(",\n".join(blocks))
    print("}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
