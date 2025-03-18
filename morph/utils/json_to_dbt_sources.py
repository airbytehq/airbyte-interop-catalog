"""
Code to convert JSON schema files or Airbyte catalog to dbt sources.yml format.

Usage:
    python json_to_dbt_sources.py <json_schema_file_or_directory> [--source-name SOURCE_NAME] [--output OUTPUT_FILE]
    python json_to_dbt_sources.py <airbyte_catalog_file> --catalog [--source-name SOURCE_NAME] [--output OUTPUT_FILE]

Example:
    python json_to_dbt_sources.py schemas/ --source-name my_source --output models/sources.yml
    python json_to_dbt_sources.py catalog.json --catalog --source-name my_source --output models/sources.yml
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def json_schema_to_dbt_column(
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


def json_schema_to_dbt_table(schema_name: str, schema_data: dict[str, Any]) -> dict[str, Any]:
    """Convert a JSON schema to a dbt table definition."""
    table = {"name": schema_name}

    # Add description if available
    if "description" in schema_data:
        table["description"] = schema_data["description"]

    # Extract columns from properties
    if "properties" in schema_data:
        columns = []
        for prop_name, prop_schema in schema_data["properties"].items():
            columns.append(json_schema_to_dbt_column(prop_name, prop_schema))

        if columns:
            table["columns"] = columns  # type: ignore

    return table


def generate_header_comment(command_args: argparse.Namespace) -> str:
    """Generate a header comment for the output file with reproduction instructions."""
    # Reconstruct the command used to generate the file
    script_name = Path(sys.argv[0]).name
    command = f"python {script_name} {command_args.schema_path}"

    if command_args.catalog:
        command += " --catalog"

    if command_args.source_name != "default_source":
        command += f" --source-name {command_args.source_name}"

    if command_args.database:
        command += f" --database {command_args.database}"

    if command_args.schema:
        command += f" --schema {command_args.schema}"

    if command_args.output != "sources.yml":
        command += f" --output {command_args.output}"

    # Create the header comment
    return (
        "# This file is auto-generated. DO NOT EDIT MANUALLY.\n"
        f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        "# To regenerate this file, run the following command:\n"
        f"# {command}\n"
    )


def create_dbt_source(
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


def process_schema_file(schema_file: str) -> tuple[str, dict[str, Any]]:
    """Process a single schema file and return table name and table definition."""
    schema_path = Path(schema_file)
    with schema_path.open() as f:
        schema_data = json.load(f)

    # Use filename without extension as table name
    table_name = schema_path.stem
    table = json_schema_to_dbt_table(table_name, schema_data)
    return table_name, table


def generate_dbt_sources_yml(
    schema_files: list[str],
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Generate a dbt sources.yml structure from JSON schema files."""
    tables = []

    for schema_file in schema_files:
        try:
            _, table = process_schema_file(schema_file)
            tables.append(table)
        except Exception as e:
            print(f"Error processing {schema_file}: {e}")

    return create_dbt_source(tables, source_name, database, schema)


def parse_airbyte_catalog(
    catalog_file: str,
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Generate a dbt sources.yml structure from an Airbyte catalog file."""
    try:
        catalog_path = Path(catalog_file)
        with catalog_path.open() as f:
            catalog = json.load(f)

        if "streams" not in catalog:
            raise ValueError(f"Invalid Airbyte catalog: 'streams' key not found in {catalog_file}")

        tables = []
        for stream in catalog["streams"]:
            if "name" not in stream or "json_schema" not in stream:
                print(f"Warning: Stream missing required fields in {catalog_file}, skipping")
                continue

            table_name = stream["name"]
            table = json_schema_to_dbt_table(table_name, stream["json_schema"])
            tables.append(table)

        return create_dbt_source(tables, source_name, database, schema)
    except Exception as e:
        print(f"Error processing Airbyte catalog {catalog_file}: {e}")
        return create_dbt_source([], source_name, database, schema)
