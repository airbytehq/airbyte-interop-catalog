"""Tests for the mapping_to_dbt_models module."""

import pytest

from morph.utils.dbt.mapping_to_dbt_models import _format_json_path


def test_format_json_path_no_dots():
    """Test that expressions without dots are returned unchanged."""
    expression = "users.id"
    result = _format_json_path(expression)
    assert result == expression


def test_format_json_path_bracket_notation():
    """Test bracket notation formatting."""
    expression = "users.contact.email"
    result = _format_json_path(expression, "duckdb", "dot_notation")
    assert result == "users.contact.email"


def test_format_json_path_portable():
    """Test portable (dbt macro) formatting."""
    expression = "users.address.street"
    result = _format_json_path(expression, "duckdb", "portable")
    assert result == "{{ json_extract(users.address, ['street']) }}"


def test_format_json_path_default():
    """Test default formatting uses bracket notation."""
    expression = "users.preferences.theme"
    result = _format_json_path(expression, "duckdb", "default")
    assert result == "users.preferences.theme"


def test_format_json_path_unimplemented_traversal():
    """Test that unimplemented traversal methods raise NotImplementedError."""
    expression = "users.contact.phone"
    unimplemented_methods = ["json_path", "colon_notation", "arrow_notation"]

    for method in unimplemented_methods:
        with pytest.raises(NotImplementedError) as excinfo:
            _format_json_path(expression, "duckdb", method)
        assert "not implemented yet" in str(excinfo.value)


def test_format_json_path_invalid_traversal():
    """Test that invalid traversal method raises ValueError."""
    expression = "users.address.city"
    with pytest.raises(ValueError) as excinfo:
        _format_json_path(expression, "postgres", "bracket_notation")
    assert "not valid for SQL dialect" in str(excinfo.value)


def test_format_json_path_table_column():
    """Test that table.column expressions are returned unchanged."""
    expression = "users.id"
    result = _format_json_path(expression, "duckdb", "bracket_notation")
    assert result == expression
    result = _format_json_path(expression, "duckdb", "portable")
    assert result == expression
