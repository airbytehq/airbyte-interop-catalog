"""Tests for the JSON to dbt sources conversion functionality."""

from click.testing import CliRunner

from morph.cli import cli
from morph.utils.json_to_dbt_sources import (
    _json_schema_to_dbt_column,  # type: ignore[reportPrivateUsage]
)


def test_json_schema_to_dbt_column() -> None:
    """Test conversion of JSON schema properties to dbt column definitions."""
    # Test string type
    string_schema = {"type": "string", "description": "A text column"}
    result = _json_schema_to_dbt_column("text_col", string_schema)
    assert result == {
        "name": "text_col",
        "description": "A text column",
        "type": "varchar",
    }

    # Test integer type
    integer_schema = {"type": "integer"}
    result = _json_schema_to_dbt_column("int_col", integer_schema)
    assert result == {
        "name": "int_col",
        "type": "integer",
    }


def test_cli_json_to_dbt_help() -> None:
    """Test the help output for json-to-dbt command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["json-to-dbt", "--help"])
    assert result.exit_code == 0, result.output
    assert "Convert JSON schema files" in result.output
