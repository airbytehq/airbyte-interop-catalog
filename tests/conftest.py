"""Pytest configuration for Morph tests."""

import pytest


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return {
        "id": "sample-1",
        "name": "Sample Data",
        "values": [1, 2, 3, 4, 5],
    }
