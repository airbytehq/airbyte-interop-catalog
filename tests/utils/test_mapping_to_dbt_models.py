"""Tests for the mapping_to_dbt_models module."""

import pytest

from morph.utils.mapping_to_dbt_models import _format_json_path


def test_format_json_path_no_dots():
    """Test that expressions without dots are returned unchanged."""
    expression = "column_name"
    result = _format_json_path(expression)
    assert result == expression


def test_format_json_path_bracket_notation():
    """Test bracket notation formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "duckdb", "bracket_notation")
    assert result == "user['profile']['name']"


def test_format_json_path_portable():
    """Test portable (dbt macro) formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "duckdb", "portable")
    assert result == "{{ json_extract(user, ['profile', 'name']) }}"


def test_format_json_path_default():
    """Test default formatting uses bracket notation."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "duckdb", "default")
    assert result == "user['profile']['name']"


def test_format_json_path_unimplemented_traversal():
    """Test that unimplemented traversal methods raise NotImplementedError."""
    expression = "user.profile.name"
    unimplemented_methods = ["json_path", "colon_notation", "arrow_notation", "dot_notation"]

    for method in unimplemented_methods:
        with pytest.raises(NotImplementedError) as excinfo:
            _format_json_path(expression, "duckdb", method)
        assert "not implemented yet" in str(excinfo.value)


def test_format_json_path_invalid_traversal():
    """Test that invalid traversal method raises ValueError."""
    expression = "user.profile.name"
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
