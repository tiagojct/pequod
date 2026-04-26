# pequod · Python package

The Pequod palette for Python: the full Log base scale, eight crew
accents (light and dark variants), and matplotlib helpers.

The narrative, design rationale, and full accessibility analysis live
in the [repository README](https://github.com/tiagojct/pequod/blob/main/README.md)
and on the [project website](https://tiagojct.eu/projects/pequod/).

## Install

From PyPI:

```bash
pip install pequod
```

With the matplotlib helpers:

```bash
pip install "pequod[plot]"
```

From source (the Python package lives in the `python/` subdirectory of
the main repository):

```bash
pip install "git+https://github.com/tiagojct/pequod.git#subdirectory=python"
```

## Quick start

```python
from pequod import LOG, CREW_LIGHT, CREW_DARK, palette

LOG                       # 12-step Log base scale, dict[str, str]
CREW_LIGHT                # 8 accents, light variants
CREW_DARK                 # 8 accents, dark variants

palette("log")            # full Log scale, list[str] of hex codes
palette("crew", n=5)      # first five crew accents
palette("log-cool", n=100, kind="continuous")    # interpolated to 100
```

Six named palettes:

| Name        | Length | Kind        | Suggested use                              |
|-------------|:-----:|-------------|--------------------------------------------|
| `log`       | 12    | sequential  | continuous gradients, heatmaps             |
| `log-warm`  | 6     | sequential  | warm side only (Log 50–400)                |
| `log-cool`  | 6     | sequential  | cool side only (Log 500–950)               |
| `crew`      | 8     | qualitative | categories, groups (light variants)        |
| `crew-dark` | 8     | qualitative | categories on a dark theme                 |
| `syntax`    | 8     | qualitative | crew in syntax-role order                  |

## Matplotlib

Two surfaces, depending on how much ceremony you want.

**Register all palettes once, then use by name:**

```python
import matplotlib.pyplot as plt
import numpy as np
import pequod

pequod.register_cmaps()    # adds pequod_log, pequod_crew, etc.

x = np.outer(np.linspace(0, 1, 200), np.ones(50))
plt.imshow(x, cmap="pequod_log")
plt.show()
```

**Build a colormap explicitly:**

```python
from pequod import to_cmap

cmap = to_cmap("log", kind="continuous")        # LinearSegmentedColormap
cmap = to_cmap("crew", kind="discrete")          # ListedColormap
cmap = to_cmap("log-cool", reverse=True)         # reversed
```

`to_cmap` and `register_cmaps` raise a clear `ImportError` if matplotlib
isn't installed; everything else in the package (the data dicts,
`palette()`) is pure Python with no dependencies.

## Keeping tokens in sync

The canonical palette lives at `../pequod.json` (one directory above
this package). The data shipped with the Python package is generated
from it:

```bash
cd python
python data-raw/generate_data.py
```

That rewrites `src/pequod/_data.py` so the Python values always match
the JSON tokens.

## Licence

MIT. The underlying palette tokens are also available under CC-BY-4.0
via `../pequod.json`; see `../LICENSE-CC-BY-4.0`.
