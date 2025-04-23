"""
Utility functions for generating morph-lock.toml files.

This module provides functionality to generate lock files that track unused streams,
unused stream fields, unmapped target tables, and unmapped target table fields.
"""

from pathlib import Path
from typing import Any

import tomli_w as toml_writer
from rich.console import Console

from morph import models, resources
from morph.models import DbtSourceFile, FieldMapping, TableMappingAudit
from morph.utils.airbyte_catalog import write_catalog_file
from morph.utils.airbyte_sync import sync_source
from morph.utils.file_utils import compute_file_hash
from morph.utils.transform_scaffold import download_target_schema

console = Console()


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


def update_lock_file(  # noqa: PLR0914
    source_name: str,
    project_name: str,
) -> None:
    """Generate a lock file for a project.

    Args:
        source_name: Name of the source
        project_name: Name of the project
    """
    # Download target schema if it doesn't exist
    download_target_schema(
        source_name=source_name,
        project_name=project_name,
        if_not_exists=True,
    )

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
            with_data=False,
            no_creds=airbyte_catalog_file.is_file(),  # Don't use creds if we already have a catalog
        )

    dbt_source_file: DbtSourceFile = DbtSourceFile.from_file(
        dbt_source_file_path,
    )

    transform_files: list[Path] = resources.get_transforms_files(
        source_name=source_name,
        project_name=project_name,
    )
    transforms: list[models.TransformFile] = [
        models.TransformFile.from_file(yaml_file) for yaml_file in transform_files
    ]
    used_source_streams: list[str] = sorted(
        {transform.source_stream_name for transform in transforms},
    )
    unused_source_streams = sorted(
        {t.name for t in dbt_source_file.source_tables} - set(used_source_streams),
    )

    lock_file_mapping_data: dict[str, Any] = {}  # What we will write to the lock file
    for transform_obj in transforms:
        # Process each transform (assume one per file for now)
        for transform in [transform_obj]:
            transform_id = transform.transform_name

            # Create a TableMappingAudit instance
            audit: TableMappingAudit = TableMappingAudit.new(
                table_mapping=transform,
                source_dbt_file=dbt_source_file,
                target_dbt_file=dbt_requirements_source_file,
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
                "unused_source_fields": audit.unused_source_table_columns,
                # Create a target DbtSourceFile from the requirements file
                "omitted_target_fields": audit.omitted_target_table_columns,
                "erroneous_source_table_columns": audit.erroneous_source_table_columns,
            }

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
    lock_file_path = resources.get_lock_file_path(
        source_name=source_name,
        project_name=project_name,
    )

    # Ensure parent directory exists
    lock_file_path.parent.mkdir(parents=True, exist_ok=True)
    # Convert lock data to TOML string and write to file
    toml_string = toml_writer.dumps(lock_data)
    lock_file_path.write_bytes(toml_string.encode("utf-8"))

    console.print(f"Generated lock file for {source_name}", style="green")
