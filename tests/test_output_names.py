# tests/test_output_names.py
from __future__ import annotations

from chardet.output_names import (
    _COMPAT_NAMES,
    apply_legacy_rename,
    apply_preferred_superset,
)


def test_apply_preferred_superset_ascii():
    d = {"encoding": "ascii", "confidence": 1.0, "language": None}
    apply_preferred_superset(d)
    assert d["encoding"] == "cp1252"


def test_apply_preferred_superset_no_match():
    d = {"encoding": "utf-8", "confidence": 1.0, "language": None}
    apply_preferred_superset(d)
    assert d["encoding"] == "utf-8"


def test_apply_preferred_superset_none():
    d = {"encoding": None, "confidence": 0.0, "language": None}
    apply_preferred_superset(d)
    assert d["encoding"] is None


def test_apply_legacy_rename_is_alias_of_apply_preferred_superset():
    """``apply_legacy_rename`` is the deprecated alias for the same function."""
    assert apply_legacy_rename is apply_preferred_superset


def test_compat_names_maps_codec_to_display() -> None:
    """_COMPAT_NAMES maps codec names to 5.x/6.x display names."""
    # 5.x compat entries
    assert _COMPAT_NAMES["big5hkscs"] == "Big5"
    assert _COMPAT_NAMES["cp855"] == "IBM855"
    assert _COMPAT_NAMES["euc_jis_2004"] == "EUC-JP"
    assert _COMPAT_NAMES["iso2022_jp_2"] == "ISO-2022-JP"
    assert _COMPAT_NAMES["shift_jis_2004"] == "SHIFT_JIS"
    # Windows codepage entries
    assert _COMPAT_NAMES["cp1252"] == "Windows-1252"
    assert _COMPAT_NAMES["cp1251"] == "Windows-1251"
    # ISO entries
    assert _COMPAT_NAMES["iso8859-1"] == "ISO-8859-1"
    # Codec names that match 5.x output have no entry
    assert "ascii" not in _COMPAT_NAMES
    assert "utf-8" not in _COMPAT_NAMES
