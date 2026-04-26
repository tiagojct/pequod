#!/usr/bin/env python3
"""Regenerate src/pequod/_data.py from ../../pequod.json.

Run from the python package root:
    python data-raw/generate_data.py

Keeps the Python palette in sync with the canonical tokens — the
JSON is the only place the colour values should be edited.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PALETTE_PATH = REPO_ROOT / "pequod.json"
OUT_PATH = Path(__file__).resolve().parent.parent / "src" / "pequod" / "_data.py"


def fmt_dict(d: dict, indent: str = "    ") -> str:
    if not d:
        return "{}"
    width = max(len(repr(k)) for k in d) + 1
    lines = [f'{indent}{repr(k):<{width}}: {v!r},' for k, v in d.items()]
    return "{\n" + "\n".join(lines) + f"\n{indent[:-4] if len(indent) >= 4 else ''}}}"


def main() -> int:
    if not PALETTE_PATH.exists():
        raise SystemExit(f"pequod.json not found at {PALETTE_PATH}")

    tokens = json.loads(PALETTE_PATH.read_text())
    version = tokens["version"]

    log_scale = {f"Log {k}": v for k, v in tokens["log"].items()}
    accents = tokens["accents"]
    crew_light = {n.capitalize(): a["light"] for n, a in accents.items()}
    crew_dark = {n.capitalize(): a["dark"] for n, a in accents.items()}
    crew_roles = {n.capitalize(): a["role"] for n, a in accents.items()}

    body = f'''"""Palette data — generated from ../pequod.json (v{version}).

Re-generate with:
    python data-raw/generate_data.py
"""

from __future__ import annotations

#: Pequod Log base scale — the twelve-step warm-paper to deep-ink ladder.
LOG: dict[str, str] = {fmt_dict(log_scale)}

#: Crew accents tuned for a Log 100 paper surface (light-mode UIs).
CREW_LIGHT: dict[str, str] = {fmt_dict(crew_light)}

#: Crew accents tuned for a Log 950 ink surface (dark-mode UIs).
CREW_DARK: dict[str, str] = {fmt_dict(crew_dark)}

#: Suggested syntax role for each crew accent.
CREW_ROLES: dict[str, str] = {fmt_dict(crew_roles)}

#: Bundled crew metadata: light variants, dark variants, and roles.
CREW: dict[str, dict[str, str]] = {{
    "light": CREW_LIGHT,
    "dark":  CREW_DARK,
    "roles": CREW_ROLES,
}}

#: Master palette lookup. Use :func:`pequod.palette` to fetch any of these
#: by name; values are tuples so callers cannot mutate the constants.
_log_items = tuple(LOG.values())
_crew_l    = tuple(CREW_LIGHT.values())
_crew_d    = tuple(CREW_DARK.values())

PALETTES: dict[str, tuple[str, ...]] = {{
    "log":       _log_items,
    "log-warm":  _log_items[:6],
    "log-cool":  _log_items[6:],
    "crew":      _crew_l,
    "crew-dark": _crew_d,
    # Crew in syntax-role order: keyword, string, number, comment,
    # function, type, constant, variable.
    "syntax": (
        CREW_LIGHT["Ahab"],
        CREW_LIGHT["Tashtego"],
        CREW_LIGHT["Pip"],
        CREW_LIGHT["Ishmael"],
        CREW_LIGHT["Starbuck"],
        CREW_LIGHT["Queequeg"],
        CREW_LIGHT["Stubb"],
        CREW_LIGHT["Daggoo"],
    ),
}}
'''

    OUT_PATH.write_text(body)
    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)} from pequod.json v{version} "
          f"({len(log_scale)} log steps, {len(accents)} crew accents).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
