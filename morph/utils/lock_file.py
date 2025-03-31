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

from morph import models, resources
from morph.models import DbtSourceFile, FieldMapping
from morph.utils import text_utils
from morph.utils.airbyte_catalog import write_catalog_file
from morph.utils.airbyte_sync import sync_source
from morph.utils.file_utils import compute_file_hash
from morph.utils.transform_scaffold import download_target_schema

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


def find_omitted_target_fields(
    transform_id: str,
    target_schema: dict[str, Any],
    fields: list[FieldMapping],
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
    mapped_fields: set[str] = {f.name for f in fields}

    # Find omitted fields
    return sorted(target_fields - mapped_fields)


def validate_field_mappings(
    transform_id: str,
    source_aliases: set[str],
    fields: list[FieldMapping],
) -> None:
    """Validate field mappings for fatal errors.

    Args:
        transform_id: ID of the transform
        source_aliases: Set of source table aliases
        fields: List of field mappings in the transform

    Raises:
        ValueError: If a fatal validation error is found
    """
    for field in fields:
        expression = str(field.expression)
        field_name = field.name

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
) -> None:
    """Generate a lock file for a project.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Raises:
        ValueError: If a fatal validation error is found
    """
    # Load all mapping files
    lock_file_mapping_data: dict[str, Any] = {}  # What we will write to the lock file

    # Extract source streams and target tables from schema files instead of config
    dbt_requirements_source_file_path: Path = resources.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    dbt_requirements_source_file: DbtSourceFile = DbtSourceFile.from_file(
        dbt_requirements_source_file_path,
    )

    airbyte_catalog_file = resources.get_generated_catalog_path(
        source_name=source_name,
        project_name=project_name,
    )
    dbt_source_file_path: Path = resources.get_generated_source_yml_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not dbt_source_file_path.is_file():
        write_catalog_file(
            source_name=source_name,
        )
        sync_source(
            source_name=source_name,
            streams="*",
            no_data=True,
            no_creds=airbyte_catalog_file.is_file(),  # Don't use creds if we already have a catalog
        )

    dbt_source_file: DbtSourceFile = DbtSourceFile.from_file(
        dbt_source_file_path,
    )

    transform_files: list[Path] = list(
        resources.get_transforms_dir(
            source_name=source_name,
        ).glob("**/*.yml"),
    )
    transforms: list[models.TableMapping] = [
        models.TableMapping.from_file(yaml_file) for yaml_file in transform_files
    ]
    used_source_streams: list[str] = sorted(
        {transform.source_stream_name for transform in transforms},
    )
    unused_source_streams = sorted(
        {t.name for t in dbt_source_file.source_tables} - set(used_source_streams),
    )

    for transform_obj in transforms:
        # Process each transform (assume one per file for now)
        for transform in [transform_obj]:
            transform_id = transform.transform_name

            dbt_source_table: models.DbtSourceTable = dbt_source_file.get_source_table(
                transform.source_stream_name,
            )

            # Extract source aliases from "from" section
            # For now, we assume only one source table per transform
            source_aliases: set[str] = {transform.source_stream_name}

            # Validate field mappings
            validate_field_mappings(
                transform_id=transform_id,
                source_aliases=source_aliases,
                fields=transform.field_mappings,
            )
            # Add to mapping data
            lock_file_mapping_data[transform_id] = {
                "source_file": str(transform.get_file_path()),
                "source_file_hash": compute_file_hash(transform.get_file_path()),
                "mapped_target_fields": {
                    f.name: f.expression for f in transform_obj.get_mapped_fields()
                },
                "unmapped_target_fields": transform_obj.get_missing_field_mappings(),
                "omitted_target_fields": find_omitted_target_fields(
                    transform_id=transform_id,
                    target_schema=text_utils.load_yaml_file(
                        resources.get_dbt_sources_requirements_path(
                            source_name=source_name,
                            project_name=project_name,
                        ),
                    ),
                    fields=transform.field_mappings,
                ),
            }
            for source_alias in source_aliases:
                dbt_source_table = dbt_source_file.get_source_table(source_alias)
                if "unused_source_fields" not in lock_file_mapping_data[transform_id]:
                    lock_file_mapping_data[transform_id]["unused_source_fields"] = {}

                lock_file_mapping_data[transform_id]["unused_source_fields"][source_alias] = sorted(
                    [
                        c.name
                        for c in dbt_source_table.columns_and_subcolumns
                        if not any(
                            (
                                f"{source_alias}.{c.name}"
                                in str(f.expression)  # Contains table.field
                                or c.name == str(f.expression)  # Exact match on field name
                            )
                            for f in transform_obj.get_mapped_fields(
                                source_alias=source_alias,
                            )
                        )
                    ],
                )

    # Sort mapping data by transform ID
    lock_file_mapping_data = dict(sorted(lock_file_mapping_data.items()))

    # Find unmapped target tables
    unmapped_tables: set[str] = {t.name for t in dbt_requirements_source_file.source_tables} - {
        t.stem for t in transform_files
    }

    # Create lock file structure
    lock_data = {
        "project": {
            "source_name": source_name,
            "project_name": project_name,
            # "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),  # Temporarily removed due to noisy diffs
            "requirements_file": str(dbt_requirements_source_file_path),
            "requirements_file_hash": compute_file_hash(dbt_requirements_source_file_path),
            "airbyte_source_file": str(dbt_source_file_path),
            "airbyte_source_file_hash": compute_file_hash(dbt_source_file_path),
        },
        "coverage": {
            "unused_source_streams": sorted(unused_source_streams),
            "unmapped_target_tables": sorted(unmapped_tables),
        },
        "mappings": lock_file_mapping_data,
    }

    # Write lock file
    # Convert lock data to TOML string and write to file
    toml_string = toml_writer.dumps(lock_data)
    resources.get_lock_file_path(
        source_name=source_name,
    ).write_bytes(toml_string.encode("utf-8"))

    console.print(f"Generated lock file for {source_name}", style="green")


def generate_lock_file(
    source_name: str,
    project_name: str,
) -> None:
    """Generate a lock file for a project.

    Args:
        source_name: Name of the source
        project_name: Name of the project
    """
    # Set paths
    lock_file = resources.get_lock_file_path(
        source_name=source_name,
        project_name=project_name,
    )

    # Ensure parent directory exists
    lock_file.parent.mkdir(parents=True, exist_ok=True)

    # Set path for local target schema file
    requirements_dir = f"catalog/{source_name}/requirements/{project_name}"
    Path(requirements_dir).mkdir(parents=True, exist_ok=True)

    download_target_schema(
        source_name=source_name,
        project_name=project_name,
        if_not_exists=True,
    )

    # Generate lock file
    try:
        generate_lock_file_for_project(
            source_name=source_name,
            project_name=project_name,
        )
    except ValueError as e:
        console.print(f"Error generating lock file: {e}", style="bold red")
