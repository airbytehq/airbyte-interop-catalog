"""Morph: A Python library for data transformation."""

from importlib.metadata import version

try:
    __version__ = version("morph")
except Exception:
    __version__ = "unknown"
