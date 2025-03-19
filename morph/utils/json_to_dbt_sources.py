"""Code to convert JSON schema files or Airbyte catalog to dbt sources.yml format."""

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

PREAMBLE = """# This file was auto-generated using the following command:
# {command}
# To regenerate this file, run the command above.
"""


def get_dbt_sources_yml(
    catalog_file: Path,
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
    preamble: str | None = None,
) -> str:
    """Return a string containing the sources.yml file with a header comment."""
    preamble = generate_header_comment() if preamble is None else preamble

    # Write to output file with header comment
    return preamble + yaml.dump(
        _generate_dbt_sources_yml_from_airbyte_catalog(
            catalog_file=catalog_file,
            source_name=source_name,
            database=database,
            schema=schema,
        ),
        default_flow_style=False,
        sort_keys=False,
    )


def _json_schema_to_dbt_column(
    property_name: str,
    property_schema: dict[str, Any],
) -> dict[str, Any]:
    """Convert a JSON schema property to a dbt column definition."""
    column = {"name": property_name}

    # Map JSON schema types to dbt types
    type_mapping = {
        "string": "varchar",
        "integer": "integer",
        "number": "float",
        "boolean": "boolean",
        "object": "variant",
        "array": "array",
    }

    if "type" in property_schema:
        json_type = property_schema["type"]
        if isinstance(json_type, list):
            # Handle multiple types (e.g., ["string", "null"])
            non_null_types = [t for t in json_type if t != "null"]
            if non_null_types:
                column["type"] = type_mapping.get(non_null_types[0], "varchar")
        else:
            column["type"] = type_mapping.get(json_type, "varchar")

    # Add description if available
    if "description" in property_schema:
        column["description"] = property_schema["description"]

    # Handle format for dates, timestamps, etc.
    if "format" in property_schema:
        format_mapping = {
            "date": "date",
            "date-time": "timestamp",
            "time": "time",
            "email": "varchar",
            "uri": "varchar",
        }
        column["type"] = format_mapping.get(
            property_schema["format"],
            column.get("type", "varchar"),
        )

    return column


def _json_schema_to_dbt_table(table_name: str, schema_data: dict[str, Any]) -> dict[str, Any]:
    """Convert a JSON schema to a dbt table definition."""
    table = {"name": table_name}

    # Add description if available
    if "description" in schema_data:
        table["description"] = schema_data["description"]

    # Extract columns from properties
    if "properties" in schema_data:
        columns: list[dict[str, Any]] = []
        for prop_name, prop_schema in schema_data["properties"].items():
            columns.append(_json_schema_to_dbt_column(prop_name, prop_schema))

        if columns:
            table["columns"] = columns  # type: ignore

    return table


def generate_header_comment(
    command_args: argparse.Namespace | None = None,
) -> str:
    """Generate a header comment for the output file with reproduction instructions."""
    # Reconstruct the command used to generate the file
    command_args = command_args or argparse.Namespace()
    command = "uv run morph json-to-dbt"

    if command_args.catalog_path:
        command += f" --catalog-path {command_args.catalog_path}"

    if command_args.source_name != "default_source":
        command += f" --source-name {command_args.source_name}"

    if command_args.database:
        command += f" --database {command_args.database}"

    if command_args.schema:
        command += f" --schema {command_args.schema}"

    if command_args.output != "sources.yml":
        command += f" --output {command_args.output}"

    return PREAMBLE.format(command=command)


def _create_dbt_source_yml_from_tables_list(
    tables: list[dict[str, Any]],
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Create a dbt source definition with tables."""
    # Sort tables alphabetically by name
    sorted_tables = sorted(tables, key=lambda x: x.get("name", ""))

    source = {"name": source_name, "tables": sorted_tables}

    if database:
        source["database"] = database

    if schema:
        source["schema"] = schema

    return {"version": 2, "sources": [source]}


def _generate_dbt_sources_yml_from_airbyte_catalog(
    catalog_file: Path,
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Generate a dbt sources.yml structure from an Airbyte catalog file."""
    try:
        catalog = json.loads(catalog_file.read_text())

        if "streams" not in catalog:
            raise ValueError(f"Invalid Airbyte catalog: 'streams' key not found in {catalog_file}")

        tables: list[dict[str, Any]] = []
        for stream in catalog["streams"]:
            if "name" not in stream or "json_schema" not in stream:
                print(f"Warning: Stream missing required fields in {catalog_file}, skipping")
                continue

            table_name = stream["name"]
            table: dict[str, Any] = _json_schema_to_dbt_table(
                table_name=table_name,
                schema_data=stream["json_schema"],
            )
            tables.append(table)

        return _create_dbt_source_yml_from_tables_list(
            tables=tables,
            source_name=source_name,
            database=database,
            schema=schema,
        )
    except Exception as e:
        print(f"Error processing Airbyte catalog {catalog_file}: {e}")
        return _create_dbt_source_yml_from_tables_list(
            tables=[],
            source_name=source_name,
            database=database,
            schema=schema,
        )


__all__ = ["get_dbt_sources_yml"]
