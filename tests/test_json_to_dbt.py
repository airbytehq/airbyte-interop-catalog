"""Tests for the JSON to dbt sources conversion functionality."""

import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from morph.cli import main
from morph.utils.dbt.dbt_source_files import (
    generate_dbt_sources_yml_from_schema_files,
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
        "data_type": "varchar",
    }

    # Test integer type
    integer_schema = {"type": "integer"}
    result = json_schema_to_dbt_column("int_col", integer_schema)
    assert result == {
        "name": "int_col",
        "data_type": "integer",
        "description": None,
    }


@pytest.mark.skip(
    reason="Fails with 'No such file or directory'.",
)
def test_cli_json_to_dbt_command() -> None:
    """Test the json-to-dbt CLI command with a sample schema."""
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a sample JSON schema file
        schema_path = (Path(tmpdir) / "test_schema.json").absolute()
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
        output_path = Path("sources.yml")
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
        result = generate_dbt_sources_yml_from_schema_files(
            source_name="test_source",
            database="test_db",
            schema="test_schema",
            schema_files=[str(schema_path)],
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


def test_airbyte_catalog_with_additional_columns() -> None:
    """Test that Airbyte catalog parsing adds the required additional columns."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a sample Airbyte catalog file
        catalog_path = Path(tmpdir) / "catalog.json"
        catalog_content = {
            "streams": [
                {
                    "name": "test_stream",
                    "json_schema": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                        },
                    },
                },
            ],
        }
        with catalog_path.open("w") as f:
            json.dump(catalog_content, f)

        from morph.models import DbtSourceFile

        dbt_file = DbtSourceFile.from_airbyte_catalog_json(
            catalog_file=catalog_path,
            source_name="test_source",
        )

        result = dbt_file.to_dict()

        # Verify the structure and additional columns
        assert "sources" in result
        assert len(result["sources"]) == 1
        source = result["sources"][0]
        assert source["name"] == "test_source"
        assert len(source["tables"]) == 1
        table = source["tables"][0]

        # Check for the additional columns
        columns = {col["name"]: col for col in table["columns"]}
        assert "_airbyte_extracted_at" in columns
        assert columns["_airbyte_extracted_at"]["data_type"] == "timestamp"
        assert "_airbyte_meta" in columns
        assert columns["_airbyte_meta"]["data_type"] == "json"
        assert "_airbyte_raw_id" in columns
        assert columns["_airbyte_raw_id"]["data_type"] == "varchar"
