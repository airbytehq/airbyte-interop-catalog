"""
Utility functions for generating transform scaffold files.

This module provides functionality to generate blank mapping YAML files
for target tables that are not yet defined.
"""

from pathlib import Path
from typing import Any

import requests
import yaml
from rich.console import Console

from morph.ai import models
from morph.utils import resource_paths

console = Console()


def load_config(config_file: str) -> tuple[dict[str, Any] | None, list[str] | None]:
    """Load configuration file and extract target tables.

    Args:
        config_file: Path to the config file

    Returns:
        Tuple containing the config dictionary and list of target tables
    """
    config_path = Path(config_file)
    if not config_path.exists():
        raise ValueError(f"Error: Config file {config_file} does not exist")

    config = yaml.safe_load(config_path.read_text())
    target_tables = config.get("target_tables", [])
    if not target_tables:
        raise ValueError(f"No target tables defined in {config_file}")

    return config, target_tables


def download_target_schema(
    source_name: str,
    project_name: str,
    config: dict[str, Any],
    *,
    if_not_exists: bool = False,
) -> None:
    """Download or load target schema file.

    Returns:
        Target schema dictionary or None if not found
    """
    # Determine target schema file name
    local_schema_path = resource_paths.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not local_schema_path.exists() and if_not_exists:
        # Nothing to do
        console.print(f"Using existing target schema file: {local_schema_path}")
        return None

    # Get target schema URL
    target_schema_url = config.get("target_dbt_schema_url")
    if not target_schema_url:
        raise ValueError("Error: target_dbt_schema_url not defined in config.yml")

    # Download target schema
    console.print(f"Downloading target schema to {local_schema_path}...")
    try:
        response = requests.get(target_schema_url)
        response.raise_for_status()
        local_schema_path.write_text(response.text)
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


def generate_mapping_file(
    source_name: str,
    project_name: str,
    table_name: str,
    *,
    parent_folder: Path,
    if_not_exists: bool = False,
) -> Path | None:
    """Generate a scaffold mapping file for a table."""
    mapping_file = parent_folder / f"{table_name}.yml"
    if mapping_file.exists() and if_not_exists:
        console.print(f"Skipping {table_name}: Mapping file already exists", style="blue")
        return None

    dbt_source_file_path = resource_paths.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    # Find table schema in target_schema
    table_schema: models.DbtSourceFile = models.DbtSourceFile.from_file(
        dbt_source_file_path,
    ).get_table(table_name)

    # Create mapping structure
    mapping = create_mapping_structure(source_name, project_name, table_name, table_schema)

    # Write mapping file
    mapping_file.write_text(yaml.dump(mapping, default_flow_style=False, sort_keys=False))

    console.print(f"Created mapping file for {table_name}", style="green")
    return mapping_file


def generate_mapping_files(
    source_name: str,
    project_name: str,
    target_tables: list[str],
    target_schema: dict[str, Any],
    parent_folder: Path,
) -> list[str]:
    """Generate mapping files for target tables.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        target_tables: List of target table names
        target_schema: Target schema dictionary
        output_path: Path to output directory

    Returns:
        List of created file paths
    """
    created_files = []
    for table_name in target_tables:
        # Check if mapping file already exists
        mapping_file = generate_mapping_file(
            source_name,
            project_name,
            table_name,
            table_schema=find_table_schema(target_schema, table_name),
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
