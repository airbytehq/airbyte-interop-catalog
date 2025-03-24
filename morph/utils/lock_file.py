"""
Utility functions for generating morph-lock.toml files.

This module provides functionality to generate lock files that track unused streams,
unused stream fields, unmapped target tables, and unmapped target table fields.
"""

import hashlib
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

try:
    import tomli_w as toml_writer
except ImportError:
    import tomli_w as toml_writer

from rich.console import Console

console = Console()


def compute_file_hash(file_path: str) -> str:
    """Compute the SHA-256 hash of a file.

    Args:
        file_path: Path to the file

    Returns:
        Hexadecimal hash string
    """
    if not Path(file_path).exists():
        return ""

    sha256_hash = hashlib.sha256()
    with Path(file_path).open("rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def find_unused_source_streams(
    config_streams: list[str], mapping_files: list[dict[str, Any]],
) -> list[str]:
    """Find source streams that are not used in any mapping file.

    Args:
        config_streams: List of source streams from config.yml
        mapping_files: List of loaded mapping files

    Returns:
        List of unused source streams
    """
    used_streams = set()

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
    config_tables: list[str], mapping_files: list[dict[str, Any]],
) -> list[str]:
    """Find target tables that are not mapped in any transform.

    Args:
        config_tables: List of target tables from config.yml
        mapping_files: List of loaded mapping files

    Returns:
        List of unmapped target tables
    """
    mapped_tables = set()

    # Extract all transform IDs
    for mapping in mapping_files:
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("id")
            if transform_id:
                mapped_tables.add(transform_id)

    # Find unmapped tables
    return sorted(set(config_tables) - mapped_tables)


def find_unmapped_target_fields(
    transform_id: str, target_schema: dict[str, Any], fields: dict[str, Any],
) -> list[str]:
    """Find target table fields that are not mapped in a transform.

    Args:
        transform_id: ID of the transform
        target_schema: Target schema dictionary
        fields: Dictionary of fields in the transform

    Returns:
        List of unmapped target fields
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
    target_fields = set()
    for column in table_schema.get("columns", []):
        field_name = column.get("name")
        if field_name:
            target_fields.add(field_name)

    # Get all mapped field names
    mapped_fields = set(fields.keys())

    # Find unmapped fields
    return sorted(target_fields - mapped_fields)


def validate_field_mappings(
    transform_id: str, source_aliases: set[str], fields: dict[str, Any],
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
            for potential_alias in [source_alias, f"{source_alias}s"]:
                # Look for the most common case: table.field notation
                if "." in expression and potential_alias not in expression:
                    parts = expression.split(".")
                    if (
                        parts[0]
                        and parts[0] != potential_alias
                        and parts[0].startswith(potential_alias[:-1])
                    ):
                        raise ValueError(
                            f"Fatal error in transform '{transform_id}': "
                            f"Field '{field_name}' references '{parts[0]}' but source alias is '{potential_alias}'",
                        )


def generate_lock_file(
    source_name: str,
    project_name: str,
    config: dict[str, Any],
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
    # Get source streams and target tables from config
    source_streams = config.get("source_streams", [])
    target_tables = config.get("target_tables", [])

    # Load all mapping files
    mapping_files = []
    mapping_data = {}

    for yaml_file in list(mapping_dir.glob("**/*.yml")) + list(mapping_dir.glob("**/*.yaml")):
        with Path(yaml_file).open() as f:
            try:
                mapping = yaml.safe_load(f)
                mapping_files.append(mapping)

                # Process each transform
                for transform in mapping.get("transforms", []):
                    transform_id = transform.get("id")
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
                        transform_id, source_aliases, transform.get("fields", {}),
                    )

                    # Find unmapped target fields
                    unmapped_fields = find_unmapped_target_fields(
                        transform_id, target_schema, transform.get("fields", {}),
                    )

                    # Extract unused source fields from annotations
                    unused_fields = {}
                    annotations = transform.get("annotations", {})
                    if "unused_source_fields" in annotations:
                        unused_fields = annotations["unused_source_fields"]

                    # Add to mapping data
                    rel_path = Path(yaml_file).relative_to(mapping_dir)
                    mapping_data[transform_id] = {
                        "source_file": str(rel_path),
                        "source_file_hash": compute_file_hash(str(yaml_file)),
                        "unused_source_fields": unused_fields,
                        "unmapped_target_fields": unmapped_fields,
                    }
            except Exception as e:
                console.print(f"Error loading mapping file {yaml_file}: {e}", style="bold red")

    # Find unused source streams
    unused_streams = find_unused_source_streams(source_streams, mapping_files)

    # Find unmapped target tables
    unmapped_tables = find_unmapped_target_tables(target_tables, mapping_files)

    # Get paths to requirements file and Airbyte source file
    requirements_file = f"requirements/{project_name}/src_hubspot.yml"
    requirements_path = Path(f"catalog/{source_name}/{requirements_file}")

    airbyte_source_file = "generated/airbyte-catalog.json"
    airbyte_source_path = Path(f"catalog/{source_name}/{airbyte_source_file}")

    # Create lock file structure
    lock_data = {
        "project": {
            "source_name": source_name,
            "project_name": project_name,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "requirements_file": requirements_file,
            "requirements_file_hash": compute_file_hash(str(requirements_path)),
            "airbyte_source_file": airbyte_source_file,
            "airbyte_source_file_hash": compute_file_hash(str(airbyte_source_path)),
        },
        "coverage": {
            "unused_source_streams": unused_streams,
            "unmapped_target_tables": unmapped_tables,
        },
        "mappings": mapping_data,
    }

    # Write lock file
    with Path(output_path).open("wb") as f:
        toml_writer.dump(lock_data, f)

    console.print(f"Generated lock file at {output_path}", style="green")
