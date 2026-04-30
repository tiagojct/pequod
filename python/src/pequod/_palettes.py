"""Palette helpers — return lists of hex strings for any context."""

from __future__ import annotations

from typing import Optional

from ._data import PALETTES


def palette(
    name: str = "log",
    n: Optional[int] = None,
    kind: str = "discrete",
    reverse: bool = False,
) -> list[str]:
    """Return a list of hex colour strings from a Pequod palette.

    Parameters
    ----------
    name :
        Palette name. One of ``"log"``, ``"log-warm"``, ``"log-cool"``,
        ``"crew"`` (light variants), ``"crew-dark"``, ``"syntax"``.
    n :
        Number of colours. Defaults to the full palette length.
    kind :
        Either ``"discrete"`` (returns the first ``n`` colours; raises if
        ``n`` exceeds the palette length) or ``"continuous"`` (linearly
        interpolates ``n`` colours across the palette in RGB space).
    reverse :
        If ``True``, reverse the returned list.

    Returns
    -------
    list of str
        Hex colour codes, uppercase, leading ``#``.

    Examples
    --------
    >>> palette("log")[:3]
    ['#F7F3EE', '#EAE1D7', '#DBC9B6']
    >>> palette("crew", n=3)
    ['#A83732', '#0082B1', '#253E82']
    >>> len(palette("log-cool", n=100, kind="continuous"))
    100
    """
    if name not in PALETTES:
        raise ValueError(
            f"Unknown palette {name!r}. "
            f"Available: {', '.join(PALETTES)}."
        )
    cols = list(PALETTES[name])
    if n is None:
        n = len(cols)
    if n < 1:
        raise ValueError("`n` must be a positive integer.")

    if kind == "discrete":
        if n > len(cols):
            raise ValueError(
                f"Requested {n} colours from palette {name!r} which has only "
                f"{len(cols)}. Use kind='continuous' to interpolate."
            )
        out = cols[:n]
    elif kind == "continuous":
        out = _interpolate(cols, n)
    else:
        raise ValueError(
            f"`kind` must be 'discrete' or 'continuous', got {kind!r}."
        )

    if reverse:
        out = list(reversed(out))
    return out


def _interpolate(stops: list[str], n: int) -> list[str]:
    """Linear-RGB interpolation across the given stops."""
    if n == 1:
        return [stops[len(stops) // 2]]

    rgb = [_hex_to_rgb(c) for c in stops]
    m = len(stops)

    out: list[str] = []
    for i in range(n):
        pos = i * (m - 1) / (n - 1)
        lo = int(pos)
        hi = min(lo + 1, m - 1)
        t = pos - lo
        r = (1 - t) * rgb[lo][0] + t * rgb[hi][0]
        g = (1 - t) * rgb[lo][1] + t * rgb[hi][1]
        b = (1 - t) * rgb[lo][2] + t * rgb[hi][2]
        out.append(_rgb_to_hex((r, g, b)))
    return out


def _hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
    h = hex_code.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    return "#{:02X}{:02X}{:02X}".format(
        round(rgb[0]), round(rgb[1]), round(rgb[2])
    )
