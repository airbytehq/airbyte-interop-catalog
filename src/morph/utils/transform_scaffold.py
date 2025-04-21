"""
Utility functions for generating transform scaffold files.

This module provides functionality to generate blank mapping YAML files
for target tables that are not yet defined.
"""

from pathlib import Path
from typing import Any

import requests
from rich.console import Console

from morph import models, resources
from morph.constants import HEADER_COMMENT
from morph.utils import text_utils

console = Console()


def download_target_schema(
    source_name: str,
    project_name: str,
    *,
    if_not_exists: bool = False,
) -> None:
    """Download or load target schema file.

    Returns:
        Target schema dictionary or None if not found
    """
    # Determine target schema file name
    local_schema_path: Path = resources.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    if local_schema_path.exists() and if_not_exists:
        # Nothing to do
        console.print(f"Using existing target schema file: {local_schema_path}")
        return

    # Get target schema URL
    target_schema_url: str = resources.get_source_config(
        source_name=source_name,
    )["target_dbt_schema_url"]
    if not target_schema_url:
        raise ValueError("Error: target_dbt_schema_url not defined in config.yml")

    # Download target schema
    console.print(f"Downloading target schema to {local_schema_path}...")
    try:
        response = requests.get(target_schema_url)
        response.raise_for_status()
        local_schema_path.parent.mkdir(parents=True, exist_ok=True)
        local_schema_path.write_text(HEADER_COMMENT + response.text)
        console.print(f"Downloaded target schema to {local_schema_path}", style="green")
        return

    except Exception as e:
        raise FileNotFoundError(f"Error downloading target schema: {e}") from e


def find_table_schema(target_schema: dict[str, Any], table_name: str) -> dict[str, Any] | None:
    """Find table schema in target schema.

    Args:
        target_schema: Target schema dictionary
        table_name: Name of the table to find

    Returns:
        Table schema dictionary or None if not found
    """
    for source in target_schema.get("sources", []):
        for table in source.get("tables", []):
            if table.get("name") == table_name:
                return table
    return None


def create_mapping_structure(
    source_name: str,
    project_name: str,
    table_name: str,
    table_schema: models.DbtSourceTable,
) -> dict[str, Any]:
    """Create mapping structure for a table.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        table_name: Name of the table
        table_schema: Schema dictionary for the table

    Returns:
        Mapping structure dictionary
    """
    result = {
        "domain": f"{source_name}.{project_name}",
        "transforms": [
            {
                "name": table_name,
                "display_name": f"{table_schema.description}",
                "from": [{"MISSING": "MISSING"}],
                "fields": {},
            },
        ],
    }
    return _add_fields_to_mapping(result, table_schema)


def _add_fields_to_mapping(
    mapping: dict[str, Any],
    table_schema: models.DbtSourceTable,
) -> dict[str, Any]:
    """Add fields with MISSING expressions to mapping.

    Args:
        mapping: Mapping dictionary
        table_schema: Schema dictionary for the table

    Returns:
        Updated mapping dictionary with fields added
    """
    fields_dict = mapping["transforms"][0]["fields"]
    for column in table_schema.columns:
        field_name = column.name
        description = column.description

        # Skip missing field names
        if not field_name:
            continue

        fields_dict[field_name] = {"expression": "MISSING", "description": description}
    return mapping


def generate_empty_mapping_file(
    source_name: str,
    project_name: str,
    transform_name: str,
    *,
    parent_folder: Path,
    if_not_exists: bool = False,
) -> Path | None:
    """Generate a scaffold mapping file for a table."""
    mapping_file = parent_folder / f"{transform_name}.yml"
    if mapping_file.exists() and if_not_exists:
        console.print(f"Skipping '{transform_name}': Mapping file already exists", style="blue")
        return None

    dbt_source_requirements_file = resources.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    # Find table schema in target_schema
    table_schema: models.DbtSourceTable = models.DbtSourceFile.from_file(
        dbt_source_requirements_file,
    ).get_table(transform_name)

    # Create mapping structure
    mapping = create_mapping_structure(source_name, project_name, transform_name, table_schema)

    # Write mapping file
    text_utils.dump_yaml_file(mapping, mapping_file)

    console.print(f"Created mapping file scaffold for `{transform_name}`", style="green")
    return mapping_file


def generate_mapping_files(
    source_name: str,
    project_name: str,
    target_tables: list[str],
    parent_folder: Path,
) -> list[str]:
    """Generate mapping files for target tables.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        target_tables: List of target table names

    Returns:
        List of created file paths
    """

    created_files = []
    for table_name in target_tables:
        # Check if mapping file already exists
        mapping_file = generate_empty_mapping_file(
            source_name=source_name,
            project_name=project_name,
            transform_name=table_name,
            parent_folder=parent_folder,
        )
        if mapping_file:
            created_files.append(mapping_file)

    return created_files


def report_results(created_files: list[str]) -> None:
    """Report results of file generation.

    Args:
        created_files: List of created file paths
    """
    if created_files:
        console.print(f"Generated {len(created_files)} mapping files:", style="bold green")
        for file in created_files:
            console.print(f"  - {file}")
    else:
        console.print("No new mapping files generated.", style="bold blue")


def generate_transform_scaffold(
    source_name: str,
    project_name: str,
    output_dir: Path | None = None,
) -> None:
    """Generate scaffold mapping YAML files for target tables.

    This command generates blank mapping YAML files for any target tables
    that are not yet defined. The generated files will include all fields
    from the target schema but with MISSING expressions.
    """

    # Set default paths if not provided
    if not output_dir:
        output_dir = resources.get_transforms_dir(
            source_name=source_name,
            project_name=project_name,
        )

    # Load config and target schema
    config = resources.get_source_config(source_name)
    if not config:
        return

    download_target_schema(
        source_name=source_name,
        project_name=project_name,
        if_not_exists=True,
    )
    target_schema = text_utils.load_yaml_file(
        resources.get_dbt_sources_requirements_path(
            source_name=source_name,
            project_name=project_name,
        ),
    )

    if not target_schema:
        return

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Process each target table
    created_files = generate_mapping_files(
        source_name=source_name,
        project_name=project_name,
        target_tables=target_schema.get("tables", []),
        parent_folder=output_path,
    )

    report_results(created_files)
