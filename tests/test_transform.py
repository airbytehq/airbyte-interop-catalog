"""Tests for the transform module."""

import tempfile
from pathlib import Path

import pytest

from morph.transform import apply_transform, read_file, write_file


def test_apply_transform_uppercase_keys():
    """Test uppercase_keys transformation."""
    data = {"name": "test", "value": 123}
    result = apply_transform(data, "uppercase_keys")
    assert result == {"NAME": "test", "VALUE": 123}


def test_apply_transform_lowercase_keys():
    """Test lowercase_keys transformation."""
    data = {"NAME": "test", "Value": 123}
    result = apply_transform(data, "lowercase_keys")
    assert result == {"name": "test", "value": 123}


def test_apply_transform_flatten():
    """Test flatten transformation."""
    data = {
        "person": {"name": "John", "address": {"city": "New York", "zip": "10001"}},
        "active": True,
    }
    result = apply_transform(data, "flatten")
    assert result == {
        "person.name": "John",
        "person.address.city": "New York",
        "person.address.zip": "10001",
        "active": True,
    }


def test_apply_transform_invalid():
    """Test invalid transformation type."""
    data = {"name": "test"}
    with pytest.raises(ValueError):
        apply_transform(data, "invalid_transform")


def test_read_write_json_file():
    """Test reading and writing JSON files."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as temp:
        temp_path = Path(temp.name)

    try:
        # Write test data
        test_data = {"name": "test", "values": [1, 2, 3]}
        write_file(test_data, temp_path)

        # Read it back
        read_data = read_file(temp_path)

        assert read_data == test_data
    finally:
        # Clean up
        if temp_path.exists():
            temp_path.unlink()


def test_read_write_csv_file():
    """Test reading and writing CSV files."""
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp:
        temp_path = Path(temp.name)

    try:
        # Write test data
        test_data = {"data": [{"id": "1", "name": "Alice"}, {"id": "2", "name": "Bob"}]}
        write_file(test_data, temp_path)

        # Read it back
        read_data = read_file(temp_path)

        assert read_data["data"] == test_data["data"]
    finally:
        # Clean up
        if temp_path.exists():
            temp_path.unlink()
