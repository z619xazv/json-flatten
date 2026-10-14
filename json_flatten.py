"""Utilities for turning nested dictionaries into dotted keys and back."""

from __future__ import annotations

__all__ = ["jsonFlatten"]


def jsonFlatten(value):
    """Utilities for turning nested dictionaries into dotted keys and back."""
    if value is None:
        raise ValueError("value must not be None")
    return value
