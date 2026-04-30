"""Palette data — generated from ../pequod.json (v0.2.0-alpha).

Re-generate with:
    python data-raw/generate_data.py
"""

from __future__ import annotations

#: Pequod Log base scale — the twelve-step warm-paper to deep-ink ladder.
LOG: dict[str, str] = {
    'Log 50'  : '#F7F3EE',
    'Log 100' : '#EAE1D7',
    'Log 150' : '#DBC9B6',
    'Log 200' : '#CFAD8E',
    'Log 300' : '#BD8C68',
    'Log 400' : '#A16E50',
    'Log 500' : '#835A49',
    'Log 600' : '#335260',
    'Log 700' : '#163F54',
    'Log 800' : '#0D2F42',
    'Log 900' : '#0C222F',
    'Log 950' : '#0B1720',
}

#: Crew accents tuned for a Log 100 paper surface (light-mode UIs).
CREW_LIGHT: dict[str, str] = {
    'Ahab'     : '#A83732',
    'Starbuck' : '#0082B1',
    'Queequeg' : '#253E82',
    'Pip'      : '#6A4A00',
    'Ishmael'  : '#76716B',
    'Stubb'    : '#CA6435',
    'Tashtego' : '#177C55',
    'Daggoo'   : '#552823',
}

#: Crew accents tuned for a Log 950 ink surface (dark-mode UIs).
CREW_DARK: dict[str, str] = {
    'Ahab'     : '#E3877C',
    'Starbuck' : '#A6DFFF',
    'Queequeg' : '#838CCF',
    'Pip'      : '#DEC577',
    'Ishmael'  : '#BFBBB6',
    'Stubb'    : '#FFD9BB',
    'Tashtego' : '#82C4A2',
    'Daggoo'   : '#A17069',
}

#: Suggested syntax role for each crew accent.
CREW_ROLES: dict[str, str] = {
    'Ahab'     : 'red',
    'Starbuck' : 'blue',
    'Queequeg' : 'indigo',
    'Pip'      : 'yellow',
    'Ishmael'  : 'grey',
    'Stubb'    : 'orange',
    'Tashtego' : 'green',
    'Daggoo'   : 'brown',
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
