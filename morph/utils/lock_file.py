"""
Utility functions for generating morph-lock.toml files.

This module provides functionality to generate lock files that track unused streams,
unused stream fields, unmapped target tables, and unmapped target table fields.
"""

from datetime import datetime
from pathlib import Path
from typing import Any

import tomli_w as toml_writer
from rich.console import Console

from morph.models import DbtSourceFile
from morph.utils import resource_paths, text_utils
from morph.utils.file_utils import compute_file_hash

console = Console()


def find_unused_source_streams(
    config_streams: list[str],
    mapping_files: list[dict[str, Any]],
) -> list[str]:
    """Find source streams that are not used in any mapping file.

    Args:
        config_streams: List of source streams from config.yml
        mapping_files: List of loaded mapping files

    Returns:
        List of unused source streams
    """
    used_streams: set[str] = set()

    # Extract all stream names from "from" sections
    for mapping in mapping_files:
        for transform in mapping.get("transforms", []):
            from_data = transform.get("from", {})

            # Handle both list and dict formats for 'from' field
            if isinstance(from_data, list):
                for source_item in from_data:
                    used_streams.update(source_item.keys())
            else:
                used_streams.update(from_data.keys())

    # Find unused streams
    return sorted(set(config_streams) - used_streams)


def find_unmapped_target_tables(
    config_tables: list[str],
    mapping_files: list[dict[str, Any]],
) -> list[str]:
    """Find target tables that are not mapped in any transform.

    Args:
        config_tables: List of target tables from config.yml
        mapping_files: List of loaded mapping files

    Returns:
        List of unmapped target tables
    """
    mapped_tables: set[str] = set()

    # Extract all transform IDs
    for mapping in mapping_files:
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("name")
            if transform_id:
                mapped_tables.add(transform_id)

    # Find unmapped tables
    return sorted(set(config_tables) - mapped_tables)


def find_omitted_target_fields(
    transform_id: str,
    target_schema: dict[str, Any],
    fields: dict[str, Any],
) -> list[str]:
    """Find target table fields that are not mapped in a transform.

    Args:
        transform_id: ID of the transform
        target_schema: Target schema dictionary
        fields: Dictionary of fields in the transform

    Returns:
        List of target fields that are omitted from the mapping
    """
    # Find table schema in target schema
    table_schema = None
    for source in target_schema.get("sources", []):
        for table in source.get("tables", []):
            if table.get("name") == transform_id:
                table_schema = table
                break
        if table_schema:
            break

    if not table_schema:
        return []

    # Get all field names from the target schema
    target_fields: set[str] = set()
    for column in table_schema.get("columns", []):
        field_name = column.get("name")
        if field_name:
            target_fields.add(field_name)

    # Get all mapped field names
    mapped_fields: set[str] = set(fields.keys())

    # Find omitted fields
    return sorted(target_fields - mapped_fields)


def find_missing_target_fields(
    fields: dict[str, Any],
) -> list[str]:
    """Find target fields marked as MISSING in a transform.

    Args:
        fields: Dictionary of fields in the transform

    Returns:
        List of fields marked as MISSING
    """
    missing_fields: list[str] = []

    for field_name, field_config in fields.items():
        expression = field_config.get("expression")

        # Check if expression is "MISSING"
        if expression == "MISSING":
            missing_fields.append(field_name)

    return sorted(missing_fields)


def find_mapped_target_fields(
    fields: dict[str, Any],
) -> dict[str, str]:
    """Find target fields and their expressions in a transform.

    Args:
        fields: Dictionary of fields in the transform

    Returns:
        Dictionary of field names to their expressions, excluding MISSING expressions
    """
    mapped_fields = {}

    for field_name, field_config in fields.items():
        expression = field_config.get("expression")

        # Skip if expression is "MISSING"
        if expression == "MISSING":
            continue

        # Add to mapped fields
        mapped_fields[field_name] = expression

    return mapped_fields


def extract_source_streams(source_name: str) -> list[str]:
    """Extract source streams from the Airbyte dbt source file.

    Args:
        source_name: Name of the source

    Returns:
        List of source stream names
    """
    source_schema_path = Path(f"catalog/{source_name}/generated/src_airbyte_{source_name}.yml")
    if not source_schema_path.exists():
        console.print(
            f"Warning: Generated source schema file not found at {source_schema_path}",
            style="yellow",
        )
        return []

    try:
        source_file = DbtSourceFile.from_file(source_schema_path)
        return [table.name for table in source_file.source_tables]
    except Exception as e:
        console.print(f"Error loading source schema: {e}", style="bold red")
        return []


def extract_target_tables(source_name: str, project_name: str) -> list[str]:
    """Extract target tables from the requirements file.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Returns:
        List of target table names
    """
    requirements_path = resource_paths.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not requirements_path.exists():
        console.print(
            f"Warning: Requirements file not found at {requirements_path}",
            style="yellow",
        )
        return []

    try:
        source_file = DbtSourceFile.from_file(requirements_path)
        return [table.name for table in source_file.source_tables]
    except Exception as e:
        console.print(f"Error loading requirements: {e}", style="bold red")
        return []


def validate_field_mappings(
    transform_id: str,
    source_aliases: set[str],
    fields: dict[str, Any],
) -> None:
    """Validate field mappings for fatal errors.

    Args:
        transform_id: ID of the transform
        source_aliases: Set of source table aliases
        fields: Dictionary of fields in the transform

    Raises:
        ValueError: If a fatal validation error is found
    """
    for field_name, field_config in fields.items():
        expression = field_config.get("expression")

        # Skip MISSING expressions
        if expression == "MISSING":
            continue

        # Check for mismatched field names (e.g., issu.my_field when alias is 'issue')
        for source_alias in source_aliases:
            # Look for the most common case: table.field notation
            if "." in str(expression):
                parts = expression.split(".")
                table_ref = parts[0]

                # Skip if the table reference matches the source alias
                if table_ref == source_alias:
                    continue

                # Check for potential typos (e.g., 'contact' instead of 'contacts')
                valid_refs = {source_alias, f"{source_alias}s"}
                if (
                    table_ref
                    and table_ref not in valid_refs
                    and table_ref.startswith(source_alias[:-1])
                ):
                    raise ValueError(
                        f"Fatal error in transform '{transform_id}': "
                        f"Field '{field_name}' references '{table_ref}' but source alias is '{source_alias}'",
                    )


def generate_lock_file_for_project(
    source_name: str,
    project_name: str,
    mapping_dir: Path,
    target_schema: dict[str, Any],
    output_path: Path,
) -> None:
    """Generate a lock file for a project.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        config: Configuration dictionary
        mapping_dir: Directory containing mapping files
        target_schema: Target schema dictionary
        output_path: Path to output the lock file

    Raises:
        ValueError: If a fatal validation error is found
    """
    # Extract source streams and target tables from schema files instead of config
    source_streams = extract_source_streams(source_name)
    target_tables = extract_target_tables(source_name, project_name)

    # Fallback to config if extraction failed
    # if not source_streams:
    #     console.print("Warning: Falling back to config file for source streams", style="yellow")
    #     source_streams = config.get("source_streams", [])

    # if not target_tables:
    #     console.print("Warning: Falling back to config file for target tables", style="yellow")
    #     target_tables = config.get("target_tables", [])

    # Load all mapping files
    mapping_files = []
    mapping_data = {}

    for yaml_file in list(mapping_dir.glob("**/*.yml")) + list(mapping_dir.glob("**/*.yaml")):
        # Use pathlib to read file content
        mapping = text_utils.load_yaml_file(yaml_file)
        mapping_files.append(mapping)

        # Process each transform
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("name")
            if not transform_id:
                continue

            # Extract source aliases from "from" section
            source_aliases = set()
            from_data = transform.get("from", {})

            if isinstance(from_data, list):
                for source_item in from_data:
                    source_aliases.update(source_item.keys())
            else:
                source_aliases.update(from_data.keys())

            # Validate field mappings
            validate_field_mappings(
                transform_id,
                source_aliases,
                transform.get("fields", {}),
            )

            # Find omitted target fields
            omitted_fields = find_omitted_target_fields(
                transform_id,
                target_schema,
                transform.get("fields", {}),
            )

            # Extract unused source fields from annotations
            unused_fields = {}
            annotations = transform.get("annotations", {})
            if "unused_source_fields" in annotations:
                unused_fields = annotations["unused_source_fields"]

            # Find missing target fields (marked as MISSING)
            missing_fields = find_missing_target_fields(
                transform.get("fields", {}),
            )

            # Find mapped target fields (excluding MISSING expressions)
            mapped_fields = find_mapped_target_fields(
                transform.get("fields", {}),
            )

            # Add to mapping data
            rel_path = Path(yaml_file).relative_to(mapping_dir)
            mapping_data[transform_id] = {
                "source_file": str(rel_path),
                "source_file_hash": compute_file_hash(str(yaml_file)),
                "mapped_target_fields": mapped_fields,
                "unmapped_target_fields": missing_fields,
                "omitted_target_fields": omitted_fields,
                "unused_source_fields": unused_fields,
            }

    # Sort mapping data by transform ID
    mapping_data = dict(sorted(mapping_data.items()))

    # Find unused source streams
    unused_streams = find_unused_source_streams(source_streams, mapping_files)

    # Find unmapped target tables
    unmapped_tables = find_unmapped_target_tables(target_tables, mapping_files)

    # Get paths to requirements file and Airbyte source file
    requirements_file = resource_paths.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )

    airbyte_source_file = resource_paths.get_generated_source_yml_path(
        source_name=source_name,
        project_name=project_name,
    )

    # Create lock file structure
    lock_data = {
        "project": {
            "source_name": source_name,
            "project_name": project_name,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "requirements_file": str(requirements_file),
            "requirements_file_hash": compute_file_hash(requirements_file),
            "airbyte_source_file": str(airbyte_source_file),
            "airbyte_source_file_hash": compute_file_hash(airbyte_source_file),
        },
        "coverage": {
            "unused_source_streams": unused_streams,
            "unmapped_target_tables": unmapped_tables,
        },
        "mappings": mapping_data,
    }

    # Write lock file
    # Convert lock data to TOML string and write to file
    toml_string = toml_writer.dumps(lock_data)
    Path(output_path).write_bytes(toml_string.encode("utf-8"))

    console.print(f"Generated lock file at {output_path}", style="green")
