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
        console.print(f"Error: Config file {config_file} does not exist", style="bold red")
        return None, None

    config = yaml.safe_load(config_path.read_text())
    target_tables = config.get("target_tables", [])
    if not target_tables:
        console.print(f"No target tables defined in {config_file}", style="bold yellow")
        return config, None

    return config, target_tables


def get_target_schema(config: dict[str, Any], requirements_dir: str) -> dict[str, Any] | None:
    """Download or load target schema file.

    Args:
        config: Configuration dictionary
        requirements_dir: Directory to store downloaded schema files

    Returns:
        Target schema dictionary or None if not found
    """
    # Get target schema URL
    target_schema_url = config.get("target_dbt_schema")
    if not target_schema_url:
        console.print("Error: target_dbt_schema not defined in config.yml", style="bold red")
        return None

    # Determine target schema file name from URL
    target_schema_filename = target_schema_url.split("/")[-1]
    local_schema_path = Path(requirements_dir) / target_schema_filename

    # Download target schema if not already downloaded
    if not local_schema_path.exists():
        console.print(f"Downloading target schema to {local_schema_path}...")
        try:
            response = requests.get(target_schema_url)
            response.raise_for_status()
            local_schema_path.write_text(response.text)
            console.print(f"Downloaded target schema to {local_schema_path}", style="green")
            return yaml.safe_load(response.text)
        except Exception as e:
            console.print(f"Error downloading target schema: {e}", style="bold red")
            return None
    else:
        console.print(f"Using existing target schema file: {local_schema_path}")
        return yaml.safe_load(local_schema_path.read_text())


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
    source_name: str, project_name: str, table_name: str, table_schema: dict[str, Any],
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
    return {
        "domain": f"{source_name}.{project_name}",
        "transforms": [
            {
                "display_name": f"{table_schema.get('description', table_name)}",
                "id": table_name,
                "from": [{f"{table_name}s": f"airbyte_raw_{source_name}.{table_name}s"}],
                "fields": {},
            },
        ],
    }


def add_fields_to_mapping(mapping: dict[str, Any], table_schema: dict[str, Any]) -> dict[str, Any]:
    """Add fields with MISSING expressions to mapping.

    Args:
        mapping: Mapping dictionary
        table_schema: Schema dictionary for the table

    Returns:
        Updated mapping dictionary with fields added
    """
    fields_dict = mapping["transforms"][0]["fields"]
    for column in table_schema.get("columns", []):
        field_name = column.get("name")
        description = column.get("description", "")

        # Skip missing field names
        if not field_name:
            continue

        fields_dict[field_name] = {"expression": "MISSING", "description": description}
    return mapping


def generate_mapping_files(
    source_name: str,
    project_name: str,
    target_tables: list[str],
    target_schema: dict[str, Any],
    output_path: Path,
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
        mapping_file = output_path / f"{table_name}.yml"
        if mapping_file.exists():
            console.print(f"Skipping {table_name}: Mapping file already exists", style="blue")
            continue

        # Find table schema in target_schema
        table_schema = find_table_schema(target_schema, table_name)
        if not table_schema:
            console.print(f"Warning: Schema not found for table {table_name}", style="yellow")
            continue

        # Create mapping structure
        mapping = create_mapping_structure(source_name, project_name, table_name, table_schema)

        # Add fields with MISSING expressions
        mapping = add_fields_to_mapping(mapping, table_schema)

        # Write mapping file
        with mapping_file.open("w") as f:
            yaml.dump(mapping, f, default_flow_style=False, sort_keys=False)

        created_files.append(str(mapping_file))
        console.print(f"Created mapping file for {table_name}", style="green")

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
