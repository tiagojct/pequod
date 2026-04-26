"""Matplotlib glue.

`matplotlib` is an optional dependency. Functions in this module
import it lazily and raise a clear ImportError if it isn't installed.
Install with::

    pip install pequod[plot]
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ._data import PALETTES
from ._palettes import palette

if TYPE_CHECKING:
    from matplotlib.colors import Colormap


_MPL_REQUIRED_MSG = (
    "matplotlib is required for this function. "
    "Install with `pip install pequod[plot]` "
    "or `pip install matplotlib`."
)


def to_cmap(
    name: str = "log",
    kind: str = "continuous",
    reverse: bool = False,
) -> "Colormap":
    """Build a matplotlib colormap from a Pequod palette.

    Parameters
    ----------
    name :
        Palette name. See :func:`palette`.
    kind :
        ``"continuous"`` returns a
        :class:`matplotlib.colors.LinearSegmentedColormap` interpolating
        across the palette stops. ``"discrete"`` returns a
        :class:`matplotlib.colors.ListedColormap` with the exact stops.
    reverse :
        If ``True``, reverse the colormap before returning.

    Returns
    -------
    matplotlib.colors.Colormap
    """
    try:
        from matplotlib.colors import (
            LinearSegmentedColormap,
            ListedColormap,
        )
    except ImportError as exc:  # pragma: no cover
        raise ImportError(_MPL_REQUIRED_MSG) from exc

    cols = palette(name, kind="discrete", reverse=reverse)
    cmap_name = f"pequod_{name.replace('-', '_')}"

    if kind == "discrete":
        return ListedColormap(cols, name=cmap_name + "_d")
    if kind == "continuous":
        return LinearSegmentedColormap.from_list(cmap_name, cols)
    raise ValueError(
        f"`kind` must be 'discrete' or 'continuous', got {kind!r}."
    )


def register_cmaps(prefix: str = "pequod_") -> list[str]:
    """Register every named Pequod palette with matplotlib.

    After calling this, the colormaps are addressable by name in
    matplotlib's usual ways::

        plt.imshow(data, cmap="pequod_log")
        sns.heatmap(df, cmap="pequod_log_cool")

    Returns
    -------
    list of str
        The names of the colormaps that were registered.
    """
    try:
        import matplotlib as mpl
    except ImportError as exc:  # pragma: no cover
        raise ImportError(_MPL_REQUIRED_MSG) from exc

    names: list[str] = []
    for pname in PALETTES:
        cmap = to_cmap(pname, kind="continuous")
        cmap_name = f"{prefix}{pname.replace('-', '_')}"
        cmap.name = cmap_name
        # matplotlib >= 3.5: prefer the `colormaps` registry.
        register = getattr(mpl, "colormaps", None)
        if register is not None and hasattr(register, "register"):
            try:
                register.register(cmap, name=cmap_name, force=True)
            except TypeError:  # very old matplotlib without `force`
                register.register(cmap, name=cmap_name)
        else:  # pragma: no cover — pre-3.5 fallback
            from matplotlib import cm
            cm.register_cmap(name=cmap_name, cmap=cmap)
        names.append(cmap_name)
    return names
