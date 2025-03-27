"""Simple utility functions."""

from typing import Any


def if_none(input: Any, default: bool | None, /) -> Any:
    """Helper function to return input if it is not None, otherwise return default."""
    return input if input is not None else default
