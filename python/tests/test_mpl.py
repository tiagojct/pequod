"""Matplotlib integration tests. Skipped if matplotlib isn't installed."""

from __future__ import annotations

import pytest

mpl = pytest.importorskip("matplotlib")
from matplotlib.colors import (  # noqa: E402
    LinearSegmentedColormap,
    ListedColormap,
)

import pequod  # noqa: E402


def test_to_cmap_continuous_returns_linear_segmented():
    cmap = pequod.to_cmap("log", kind="continuous")
    assert isinstance(cmap, LinearSegmentedColormap)


def test_to_cmap_discrete_returns_listed():
    cmap = pequod.to_cmap("crew", kind="discrete")
    assert isinstance(cmap, ListedColormap)
    assert cmap.N == 8


def test_to_cmap_reverse():
    fwd = pequod.to_cmap("log", kind="discrete")
    rev = pequod.to_cmap("log", kind="discrete", reverse=True)
    assert list(fwd.colors) == list(reversed(rev.colors))


def test_to_cmap_unknown_palette_errors():
    with pytest.raises(ValueError):
        pequod.to_cmap("nonexistent")


def test_to_cmap_unknown_kind_errors():
    with pytest.raises(ValueError):
        pequod.to_cmap("log", kind="bogus")


def test_register_cmaps_registers_all_named_palettes():
    names = pequod.register_cmaps()
    expected = {
        "pequod_log", "pequod_log_warm", "pequod_log_cool",
        "pequod_crew", "pequod_crew_dark", "pequod_syntax",
    }
    assert set(names) == expected
    # Each name should now resolve via the matplotlib registry.
    for n in names:
        cmap = mpl.colormaps.get_cmap(n)
        assert cmap is not None


def test_register_cmaps_supports_custom_prefix():
    names = pequod.register_cmaps(prefix="myproj_")
    assert all(n.startswith("myproj_") for n in names)
    # Clean up: drop our test-only registrations to avoid polluting later
    # tests in the same session.
    for n in names:
        try:
            mpl.colormaps.unregister(n)
        except (KeyError, ValueError):
            pass
