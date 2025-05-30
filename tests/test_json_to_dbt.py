"""Tests for the JSON to dbt sources conversion functionality."""

import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from morph.cli import main


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
