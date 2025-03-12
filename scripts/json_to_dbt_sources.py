#!/usr/bin/env python3
"""
A script to convert JSON schema files to dbt sources.yml format.

Usage:
    python json_to_dbt_sources.py <json_schema_file_or_directory> [--source-name SOURCE_NAME] [--output OUTPUT_FILE]

Example:
    python json_to_dbt_sources.py schemas/ --source-name my_source --output models/sources.yml
"""

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


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
    import sys
    from datetime import datetime

    # Reconstruct the command used to generate the file
    script_name = Path(sys.argv[0]).name
    command = f"python {script_name} {command_args.schema_path}"

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
            schema_path = Path(schema_file)
            with schema_path.open() as f:
                schema_data = json.load(f)

            # Use filename without extension as table name
            table_name = schema_path.stem
            table = json_schema_to_dbt_table(table_name, schema_data)
            tables.append(table)
        except Exception as e:
            print(f"Error processing {schema_file}: {e}")

    source = {"name": source_name, "tables": tables}

    if database:
        source["database"] = database

    if schema:
        source["schema"] = schema

    return {"version": 2, "sources": [source]}


def main():
    parser = argparse.ArgumentParser(description="Convert JSON schema files to dbt sources.yml")
    parser.add_argument("schema_path", help="Path to JSON schema file or directory")
    parser.add_argument("--source-name", default="default_source", help="Name for the dbt source")
    parser.add_argument("--database", help="Database name for the source")
    parser.add_argument("--schema", help="Schema name for the source")
    parser.add_argument("--output", default="sources.yml", help="Output file path")

    args = parser.parse_args()

    # Collect schema files
    schema_files = []
    schema_path = Path(args.schema_path)
    if schema_path.is_dir():
        for file in schema_path.iterdir():
            if file.name.endswith(".json"):
                schema_files.append(str(file))
    elif schema_path.is_file() and schema_path.name.endswith(".json"):
        schema_files.append(args.schema_path)
    else:
        print(f"Error: {args.schema_path} is not a valid JSON file or directory")
        return

    if not schema_files:
        print("No JSON schema files found")
        return

    # Generate sources.yml content
    sources_yml = generate_dbt_sources_yml(
        schema_files,
        args.source_name,
        args.database,
        args.schema,
    )

    # Generate header comment
    header_comment = generate_header_comment(args)

    # Write to output file with header comment
    output_path = Path(args.output)
    with output_path.open("w") as f:
        f.write(header_comment)
        yaml.dump(sources_yml, f, default_flow_style=False, sort_keys=False)

    print(f"Generated dbt sources.yml at {args.output}")


if __name__ == "__main__":
    main()
