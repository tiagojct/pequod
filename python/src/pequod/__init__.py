"""pequod — pigment-inspired colour palette for reading and code.

A Python port of the Pequod palette: the full Log base scale, eight
crew accents in light and dark variants, and matplotlib helpers.

Quick start
-----------
>>> from pequod import LOG, CREW_LIGHT, palette
>>> palette("log")[:3]
['#FBFAF5', '#F8F4EB', '#ECE5D3']
>>> palette("crew", n=3)
['#B5534A', '#527C98', '#4A4E8C']

Matplotlib
----------
>>> import pequod, matplotlib.pyplot as plt    # doctest: +SKIP
>>> pequod.register_cmaps()                    # doctest: +SKIP
>>> plt.imshow(data, cmap="pequod_log")        # doctest: +SKIP

The narrative, design rationale, and full accessibility analysis live
at https://tiagojct.eu/projects/pequod/. The canonical source is at
https://github.com/tiagojct/pequod.
"""

from __future__ import annotations

__version__ = "0.1.0"

from ._data import (
    LOG,
    CREW_LIGHT,
    CREW_DARK,
    CREW,
    CREW_ROLES,
    PALETTES,
)
from ._palettes import palette


# Lazy attribute access for the matplotlib helpers — keeps `import pequod`
# light if matplotlib isn't installed.
def __getattr__(name: str):
    if name in {"to_cmap", "register_cmaps"}:
        from . import _mpl
        return getattr(_mpl, name)
    raise AttributeError(f"module 'pequod' has no attribute {name!r}")


__all__ = [
    "__version__",
    "LOG",
    "CREW_LIGHT",
    "CREW_DARK",
    "CREW",
    "CREW_ROLES",
    "PALETTES",
    "palette",
    "to_cmap",
    "register_cmaps",
]
