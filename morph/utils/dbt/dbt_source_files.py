"""
Code to convert JSON schema files or Airbyte catalog to dbt sources.yml format.

Usage:
    python dbt_source_files.py <json_schema_file_or_directory> [--source-name SOURCE_NAME] [--output OUTPUT_FILE]
    python dbt_source_files.py <airbyte_catalog_file> --catalog [--source-name SOURCE_NAME] [--output OUTPUT_FILE]

Example:
    python dbt_source_files.py schemas/ --source-name my_source --output models/sources.yml
    python dbt_source_files.py catalog.json --catalog --source-name my_source --output models/sources.yml
"""

from pathlib import Path

from rich.console import Console

from morph import resources
from morph.constants import DEFAULT_PROJECT_NAME, HEADER_COMMENT
from morph.models import DbtSourceFile
from morph.utils import text_utils

console = Console()


def update_generated_dbt_sources_yml_from_airbyte_catalog(
    source_name: str,
    *,
    project_name: str = DEFAULT_PROJECT_NAME,
    catalog_file: Path | None = None,
    output_file: Path | None = None,
) -> None:
    """Generate a dbt sources.yml structure from an Airbyte catalog file.

    Save it to disk in the default location, or in a custom location if specified.
    """
    if not catalog_file:
        catalog_file = resources.get_generated_catalog_path(
            source_name=source_name,
            project_name=project_name,
        )

    # Validate input path exists
    if not catalog_file.exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    if not catalog_file.name.endswith(".json"):
        raise ValueError(f"Error: {catalog_file} is not a valid JSON file")

    dbt_file: DbtSourceFile = DbtSourceFile.from_airbyte_catalog_json(
        catalog_file=catalog_file,
        source_name=source_name,
    )

    # Calculate output path
    output_path = output_file or resources.get_generated_source_yml_path(
        source_name=source_name,
        project_name=project_name,
    )

    # Write to file
    output_path.write_text(f"{HEADER_COMMENT}\n{text_utils.dump_yaml_str(dbt_file.to_dict())}")
    console.print(f"Generated sources.yml at {output_path}")
