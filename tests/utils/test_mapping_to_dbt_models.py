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


def test_format_json_path_json_path():
    """Test JSON_EXTRACT formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "bigquery", "json_path")
    assert result == "JSON_EXTRACT(user, '$.profile.name')"


def test_format_json_path_colon_notation():
    """Test colon notation formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "snowflake", "colon_notation")
    assert result == "user:profile:name"


def test_format_json_path_arrow_notation():
    """Test arrow notation formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "postgres", "arrow_notation")
    assert result == "user->'profile'->>'name'"


def test_format_json_path_dot_notation():
    """Test dot notation formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "bigquery", "dot_notation")
    assert result == "user.profile.name"


def test_format_json_path_portable():
    """Test portable (dbt macro) formatting."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "duckdb", "portable")
    assert result == "{{ json_extract(user, ['profile', 'name']) }}"


def test_format_json_path_default():
    """Test default formatting uses dialect default."""
    expression = "user.profile.name"
    result = _format_json_path(expression, "duckdb", "default")
    assert result == "user['profile']['name']"
    
    result = _format_json_path(expression, "bigquery", "default")
    assert result == "JSON_EXTRACT(user, '$.profile.name')"


def test_format_json_path_invalid_traversal():
    """Test that invalid traversal method raises ValueError."""
    expression = "user.profile.name"
    with pytest.raises(ValueError) as excinfo:
        _format_json_path(expression, "postgres", "dot_notation")
    assert "not valid for SQL dialect" in str(excinfo.value)
