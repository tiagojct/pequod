"""pequod — pigment-inspired colour palette for reading and code.

A Python port of the Pequod palette: the full Log base scale, eight
crew accents in light and dark variants, and matplotlib helpers.

Quick start
-----------
>>> from pequod import LOG, CREW_LIGHT, palette
>>> palette("log")[:3]
['#F7F3EE', '#EAE1D7', '#DBC9B6']
>>> palette("crew", n=3)
['#931432', '#006A98', '#253E82']

Matplotlib
----------
>>> import pequod, matplotlib.pyplot as plt    # doctest: +SKIP
>>> pequod.register_cmaps()                    # doctest: +SKIP
>>> plt.imshow(data, cmap="pequod_log")        # doctest: +SKIP

The narrative, design rationale, and full accessibility analysis live
at https://ensigns.tiagojacinto.eu/pequod/. This package is built from
https://github.com/tiagojct/pequod. Pequod continues in Ensigns
(https://github.com/tiagojct/ensigns); 0.3.0 is the last release of this
package.
"""

from __future__ import annotations

__version__ = "0.3.0"

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
