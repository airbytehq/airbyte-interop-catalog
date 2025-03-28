"""
Code to convert JSON schema files or Airbyte catalog to dbt sources.yml format.

Usage:
    python dbt_source_files.py <json_schema_file_or_directory> [--source-name SOURCE_NAME] [--output OUTPUT_FILE]
    python dbt_source_files.py <airbyte_catalog_file> --catalog [--source-name SOURCE_NAME] [--output OUTPUT_FILE]

Example:
    python dbt_source_files.py schemas/ --source-name my_source --output models/sources.yml
    python dbt_source_files.py catalog.json --catalog --source-name my_source --output models/sources.yml
"""

import json
from pathlib import Path
from typing import Any

from rich.console import Console

from morph.constants import DEFAULT_PROJECT_NAME, HEADER_COMMENT
from morph.utils import resource_paths, text_utils

console = Console()


def json_schema_to_dbt_column(
    property_name: str,
    property_schema: dict[str, Any],
) -> dict[str, Any]:
    """Convert a JSON schema property to a dbt column definition.
    
    This function is maintained for backward compatibility.
    New code should use DbtSourceColumn.from_json_schema() instead.
    """
    from morph.models import DbtSourceColumn
    
    dbt_column = DbtSourceColumn.from_json_schema(property_name, property_schema)
    return dbt_column.model_dump(exclude={"subcolumns": True})


def json_schema_to_dbt_table(schema_name: str, schema_data: dict[str, Any]) -> dict[str, Any]:
    """Convert a JSON schema to a dbt table definition."""
    from morph.models import DbtSourceColumn, DbtSourceTable
    
    table = {"name": schema_name}

    # Add description if available
    if "description" in schema_data:
        table["description"] = schema_data["description"]

    # Extract columns from properties
    if "properties" in schema_data:
        columns = []
        for prop_name, prop_schema in schema_data["properties"].items():
            dbt_column = DbtSourceColumn.from_json_schema(prop_name, prop_schema)
            columns.append(dbt_column)

        if columns:
            dbt_table = DbtSourceTable(
                name=schema_name,
                description=table.get("description"),
                columns=columns
            )
            return dbt_table.to_dict()

    return table


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
    schema_data = json.loads(schema_path.read_text())

    # Use filename without extension as table name
    table_name = schema_path.stem
    table = json_schema_to_dbt_table(table_name, schema_data)
    return table_name, table


def generate_dbt_sources_yml_from_schema_files(
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


def generate_dbt_sources_yml_from_airbyte_catalog(
    source_name: str,
    *,
    project_name: str = DEFAULT_PROJECT_NAME,
    catalog_file: Path | None = None,
    output_file: Path | None = None,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Generate a dbt sources.yml structure from an Airbyte catalog file."""
    if not catalog_file:
        catalog_file = resource_paths.get_generated_catalog_path(source_name, project_name)

    # Validate input file exists
    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    # Calculate output path
    output_path = (
        Path(output_file)
        if output_file
        else resource_paths.get_generated_source_yml_path(
            source_name=source_name,
            project_name=project_name,
        )
    )

    sources_yml = parse_airbyte_catalog_to_dbt_sources_format(
        catalog_file,
        source_name,
        database,
        schema,
    )

    sources_yml_with_header = f"{HEADER_COMMENT}\n{text_utils.dump_yaml_str(sources_yml)}"

    # Write to file
    output_path.write_text(sources_yml_with_header)
    console.print(f"Generated sources.yml at {output_path}")
    
    return sources_yml


def parse_airbyte_catalog_to_dbt_sources_format(
    catalog_file: str | Path,
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
) -> dict[str, Any]:
    """Generate a dbt sources.yml structure from an Airbyte catalog file."""
    try:
        catalog_path = Path(catalog_file)
        catalog = json.loads(catalog_path.read_text())

        if "streams" not in catalog:
            raise ValueError(f"Invalid Airbyte catalog: 'streams' key not found in {catalog_file}")

        tables = []
        for stream in catalog["streams"]:
            if "name" not in stream or "json_schema" not in stream:
                print(f"Warning: Stream missing required fields in {catalog_file}, skipping")
                continue

            table_name = stream["name"]
            table = json_schema_to_dbt_table(table_name, stream["json_schema"])

            # Add the three additional Airbyte columns to all streams
            airbyte_columns = [
                {
                    "name": "_airbyte_extracted_at",
                    "type": "timestamp",
                    "description": "Timestamp when the record was extracted from the source",
                },
                {
                    "name": "_airbyte_meta",
                    "type": "variant",
                    "description": "Metadata about the record",
                },
                {
                    "name": "_airbyte_raw_id",
                    "type": "varchar",
                    "description": "Unique identifier for the raw record",
                },
            ]

            # Add columns to the table if they don't already exist
            if "columns" not in table:
                table["columns"] = []

            table["columns"].extend(airbyte_columns)

            tables.append(table)

        return create_dbt_source(tables, source_name, database, schema)
    except Exception as e:
        print(f"Error processing Airbyte catalog {catalog_file}: {e}")
        return create_dbt_source([], source_name, database, schema)


def get_dbt_sources_requirements(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> dict[str, Any]:
    """Get the parsed dbt sources.yml requirements file content."""
    catalog_file = resource_paths.get_generated_catalog_path(source_name, project_name)
    return parse_airbyte_catalog_to_dbt_sources_format(catalog_file, source_name)
