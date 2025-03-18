"""Tests for the JSON to dbt sources conversion functionality."""

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any

import pytest
from click.testing import CliRunner

from morph.cli import main
from morph.utils.json_to_dbt_sources import (
    generate_dbt_sources_yml,
    generate_header_comment,
    json_schema_to_dbt_column,
)


def test_json_schema_to_dbt_column() -> None:
    """Test conversion of JSON schema properties to dbt column definitions."""
    # Test string type
    string_schema = {"type": "string", "description": "A text column"}
    result = json_schema_to_dbt_column("text_col", string_schema)
    assert result == {
        "name": "text_col",
        "description": "A text column",
        "type": "varchar",
    }

    # Test integer type
    integer_schema = {"type": "integer"}
    result = json_schema_to_dbt_column("int_col", integer_schema)
    assert result == {
        "name": "int_col",
        "type": "integer",
    }


@pytest.mark.parametrize(
    "args,expected_command",
    [
        (
            {
                "schema_path": "catalog.json",
                "catalog": True,
                "source_name": "hubspot",
                "database": "my_db",
                "schema": "public",
                "output": "src_hubspot.yml",
            },
            "uv run morph json-to-dbt --catalog --source-name hubspot --database my_db --schema public --output src_hubspot.yml catalog.json",
        ),
        (
            {
                "schema_path": "schemas/",
                "catalog": False,
                "source_name": "custom_source",
                "database": None,
                "schema": None,
                "output": "models/sources.yml",
            },
            "uv run morph json-to-dbt --source-name custom_source --output models/sources.yml schemas/",
        ),
    ],
)
def test_generate_header_comment(args: dict[str, Any], expected_command: str) -> None:
    """Test generation of header comments with various command arguments."""
    # Create a Namespace object from the args dictionary
    command_args = argparse.Namespace(**args)

    # Generate the header comment
    header = generate_header_comment(command_args)

    # Verify the command in the header matches the expected command
    assert expected_command in header
    assert "# This file was auto-generated using the following command:" in header
    assert "# To regenerate this file, run the command above." in header


def test_cli_json_to_dbt_command() -> None:
    """Test the json-to-dbt CLI command with a sample schema."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a sample JSON schema file
        schema_path = Path(tmpdir) / "test_schema.json"
        schema_content = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string", "description": "User's name"},
            },
        }
        with schema_path.open("w") as f:
            json.dump(schema_content, f)

        # Test the command
        result = runner.invoke(
            main,
            [
                "json-to-dbt",
                str(schema_path),
                "--source-name",
                "test_source",
                "--database",
                "test_db",
                "--schema",
                "test_schema",
            ],
        )

        assert result.exit_code == 0
        assert "Generated dbt sources.yml" in result.output

        # Verify the output file exists and contains expected content
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            output_path = Path(tmpfile.name)
        assert output_path.exists()

        # Clean up
        output_path.unlink()


def test_generate_dbt_sources_yml() -> None:
    """Test generation of dbt sources YAML from JSON schema files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test schema file
        schema_path = Path(tmpdir) / "test_table.json"
        schema_content = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
        }
        with schema_path.open("w") as f:
            json.dump(schema_content, f)

        # Generate sources.yml content
        result = generate_dbt_sources_yml(
            [str(schema_path)],
            source_name="test_source",
            database="test_db",
            schema="test_schema",
        )

        # Verify the structure
        assert "version" in result
        assert "sources" in result
        assert len(result["sources"]) == 1
        source = result["sources"][0]
        assert source["name"] == "test_source"
        assert source["database"] == "test_db"
        assert source["schema"] == "test_schema"
        assert len(source["tables"]) == 1
        assert source["tables"][0]["name"] == "test_table"


def test_cli_json_to_dbt_help() -> None:
    """Test the help output for json-to-dbt command."""
    runner = CliRunner()
    result = runner.invoke(main, ["json-to-dbt", "--help"])
    assert result.exit_code == 0
    assert "Convert JSON schema files" in result.output
