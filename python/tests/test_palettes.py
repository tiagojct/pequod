"""Palette unit tests — no matplotlib required."""

from __future__ import annotations

import re

import pytest

import pequod
from pequod import (
    CREW,
    CREW_DARK,
    CREW_LIGHT,
    LOG,
    PALETTES,
    palette,
)


HEX_RE = re.compile(r"^#[0-9A-F]{6}$")


def test_log_has_twelve_steps():
    assert len(LOG) == 12
    assert list(LOG)[0] == "Log 50"
    assert list(LOG)[-1] == "Log 950"


def test_crew_palettes_have_eight_named_entries():
    assert len(CREW_LIGHT) == 8
    assert len(CREW_DARK) == 8
    assert set(CREW_LIGHT) == set(CREW_DARK)
    assert set(CREW_LIGHT) == {
        "Ahab", "Starbuck", "Queequeg", "Pip",
        "Ishmael", "Stubb", "Tashtego", "Daggoo",
    }


def test_crew_bundles_light_dark_roles():
    assert set(CREW) == {"light", "dark", "roles"}
    assert len(CREW["roles"]) == 8


def test_every_value_is_a_six_digit_hex():
    for v in LOG.values():
        assert HEX_RE.match(v), v
    for v in CREW_LIGHT.values():
        assert HEX_RE.match(v), v
    for v in CREW_DARK.values():
        assert HEX_RE.match(v), v


def test_named_palettes_resolve():
    expected = {"log", "log-warm", "log-cool", "crew", "crew-dark", "syntax"}
    assert set(PALETTES) == expected


def test_palette_returns_a_list_of_hex_strings():
    out = palette("log")
    assert isinstance(out, list)
    assert len(out) == 12
    assert all(HEX_RE.match(c) for c in out)


def test_palette_default_name_is_log():
    assert palette() == palette("log")


def test_palette_n_truncates_for_discrete():
    assert palette("crew", n=3) == ["#A83732", "#0082B1", "#253E82"]


def test_palette_continuous_interpolates():
    out = palette("log", n=100, kind="continuous")
    assert len(out) == 100
    assert all(HEX_RE.match(c) for c in out)
    assert out[0] == "#F7F3EE"     # endpoint preserved
    assert out[-1] == "#0B1720"    # endpoint preserved


def test_palette_reverse_flips_order():
    fwd = palette("log")
    rev = palette("log", reverse=True)
    assert fwd == list(reversed(rev))


def test_palette_unknown_name_errors():
    with pytest.raises(ValueError, match="Unknown palette"):
        palette("nonexistent")


def test_palette_too_many_discrete_colours_errors():
    with pytest.raises(ValueError, match="has only"):
        palette("crew", n=100)


def test_palette_zero_n_errors():
    with pytest.raises(ValueError, match="positive integer"):
        palette("crew", n=0)


def test_palette_invalid_kind_errors():
    with pytest.raises(ValueError, match="kind"):
        palette("log", kind="bogus")


def test_version_attribute():
    assert isinstance(pequod.__version__, str)
    assert pequod.__version__.count(".") >= 2
