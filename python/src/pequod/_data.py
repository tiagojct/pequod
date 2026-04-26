"""Palette data — generated from ../pequod.json (v0.1.0-alpha).

Re-generate with:
    python data-raw/generate_data.py
"""

from __future__ import annotations

#: Pequod Log base scale — the twelve-step warm-paper to deep-ink ladder.
LOG: dict[str, str] = {
    "Log 50":  "#FBFAF5",
    "Log 100": "#F8F4EB",
    "Log 150": "#ECE5D3",
    "Log 200": "#DFD3B8",
    "Log 300": "#C4A57B",
    "Log 400": "#A8865E",
    "Log 500": "#8B7B6B",
    "Log 600": "#6E5F52",
    "Log 700": "#527275",
    "Log 800": "#2C3E50",
    "Log 900": "#1C2936",
    "Log 950": "#13181F",
}

#: Crew accents tuned for a Log 100 paper surface (light-mode UIs).
CREW_LIGHT: dict[str, str] = {
    "Ahab":     "#B5534A",
    "Starbuck": "#527C98",
    "Queequeg": "#4A4E8C",
    "Pip":      "#A8812B",
    "Ishmael":  "#6E6E6B",
    "Stubb":    "#B5683A",
    "Tashtego": "#507352",
    "Daggoo":   "#7A5440",
}

#: Crew accents tuned for a Log 950 ink surface (dark-mode UIs).
CREW_DARK: dict[str, str] = {
    "Ahab":     "#E07A72",
    "Starbuck": "#7FA8C3",
    "Queequeg": "#8A8ECE",
    "Pip":      "#D9B461",
    "Ishmael":  "#A5A5A0",
    "Stubb":    "#E29B6E",
    "Tashtego": "#8AB08C",
    "Daggoo":   "#AF8870",
}

#: Suggested syntax role for each crew accent.
CREW_ROLES: dict[str, str] = {
    "Ahab":     "red",
    "Starbuck": "blue",
    "Queequeg": "indigo",
    "Pip":      "yellow",
    "Ishmael":  "grey",
    "Stubb":    "orange",
    "Tashtego": "green",
    "Daggoo":   "brown",
}

#: Bundled crew metadata: light variants, dark variants, and roles.
CREW: dict[str, dict[str, str]] = {
    "light": CREW_LIGHT,
    "dark":  CREW_DARK,
    "roles": CREW_ROLES,
}

#: Master palette lookup. Use :func:`pequod.palette` to fetch any of these
#: by name; values are tuples so callers cannot mutate the constants.
_log_items = tuple(LOG.values())
_crew_l    = tuple(CREW_LIGHT.values())
_crew_d    = tuple(CREW_DARK.values())

PALETTES: dict[str, tuple[str, ...]] = {
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
}
