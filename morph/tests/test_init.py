"""Tests for the package initialization."""

import morph


def test_version():
    """Test that the version is defined."""
    assert morph.__version__ is not None
    assert isinstance(morph.__version__, str)
