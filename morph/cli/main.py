"""Command-line interface for Morph."""

from pathlib import Path
from typing import Any

import click
import yaml
from rich.console import Console
from rich.table import Table

from morph.ai.eval import get_mapping_confidence
from morph.utils.json_to_dbt_sources import (
    parse_airbyte_catalog,
)
from morph.utils.lock_file import generate_lock_file_for_project
from morph.utils.mapping_to_dbt_models import generate_dbt_package

console = Console()


@click.group()
@click.version_option(package_name="morph", prog_name="morph")
def main() -> None:
    """Morph CLI."""
    pass


@main.command()
@click.argument("catalog_file", type=str)
@click.option("--source-name", type=str, help="Name of the source (e.g., 'hubspot')")
@click.option("--output-file", type=str, help="Output file path")
@click.option("--database", type=str, help="Database name")
@click.option("--schema", type=str, help="Schema name")
def json_to_dbt(
    catalog_file: str,
    source_name: str | None = None,
    output_file: str | None = None,
    database: str | None = None,
    schema: str | None = None,
) -> None:
    """Convert JSON schema files or Airbyte catalogs to a dbt sources.yml file.

    This command converts a JSON schema or Airbyte catalog to a dbt sources.yml file.
    The catalog file can be either a JSON schema or an Airbyte catalog.

    CATALOG_FILE: Path to the JSON schema or Airbyte catalog file
    """
    # Validate input file exists
    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    # Generate sources.yml from catalog.json
    if source_name is None:
        source_name = Path(catalog_file).stem

    sources_yml = parse_airbyte_catalog(
        catalog_file,
        source_name,
        database,
        schema,
    )

    # Write sources.yml to output file
    output_path = Path(output_file) if output_file else Path(f"sources_{source_name}.yml")

    # Create a simple header comment
    header = f"""# This file was auto-generated using the following command:
# uv run morph json-to-dbt {catalog_file} --source-name {source_name}
# To regenerate this file, run the command above.
"""
    sources_yml_with_header = f"{header}\n{yaml.dump(sources_yml, default_flow_style=False, sort_keys=False)}"

    # Write to file
    output_path.write_text(sources_yml_with_header)
    console.print(f"Generated sources.yml at {output_path}")


@main.command()
@click.argument("source_name", type=str)
@click.argument(
    "project_name",
    type=str,
    default="fivetran-interop",
)
@click.option(
    "--catalog-file",
    help="Path to Airbyte catalog JSON file (defaults to catalog/{source_name}/generated/airbyte-catalog.json)",
)
@click.option(
    "--output-dir",
    help="Output directory for generated dbt project (defaults to catalog/{source_name}/generated)",
)
@click.option(
    "--mapping-dir",
    help="Directory containing mapping YAML files (defaults to catalog/{source_name}/src/{project_name}/transforms)",
)
def generate_dbt_project(
    source_name: str,
    project_name: str,
    catalog_file: str | None = None,
    output_dir: str | None = None,
    mapping_dir: str | None = None,
) -> None:
    """Generate a dbt project from mapping files.

    This command generates a dbt project from mapping files. The mapping files
    should be in YAML format and located in the mapping directory.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    _ = project_name  # Not used currently

    catalog_dir = Path("catalog")
    if source_name is not None:
        catalog_file = catalog_file or str(
            catalog_dir / source_name / "generated" / "airbyte-catalog.json",
        )

    # Validate input paths exist
    if not catalog_dir.exists():
        raise ValueError(f"Error: {catalog_dir} does not exist")

    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    if source_name is not None:
        output_dir = output_dir or str(catalog_dir / source_name / "generated")
        mapping_dir = mapping_dir or str(
            catalog_dir / source_name / "src" / project_name / "transforms",
        )

    # Generate dbt package
    try:
        # Generate dbt models from mapping files
        generate_dbt_package(
            source_name=source_name,
            output_dir=output_dir,
            mapping_dir=mapping_dir,
        )

        # Determine the actual output directory
        actual_output_dir = (
            Path(output_dir) if output_dir else catalog_dir / source_name / "generated"
        )

        # Generate sources.yml from catalog.json
        sources_yml = parse_airbyte_catalog(
            catalog_file,
            source_name,
            None,  # database
            None,  # schema
        )

        # Write sources.yml to models directory
        sources_path = actual_output_dir / "models" / "src_airbyte_raw.yml"
        # Ensure parent directory exists
        sources_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert dict to YAML string before writing
        sources_path.write_text(yaml.dump(sources_yml, default_flow_style=False, sort_keys=False))

        console.print(f"Generated dbt project at {actual_output_dir}")
    except Exception as e:
        console.print(f"Error generating dbt project: {e}", style="bold red")


@main.command()
def create_airbyte_catalog(
    source_name: str,
    output_file: str | None = None,
) -> None:
    """Generate an Airbyte catalog JSON file for a source.

    This command generates an Airbyte catalog JSON file for the specified source.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    from pathlib import Path

    from morph.utils.airbyte_catalog import write_catalog_file

    # Set default output file path if not provided
    if not output_file:
        # We could use project_name in the future if needed
        output_file = f"catalog/{source_name}/generated/airbyte-catalog.json"

    console.print(f"Generating Airbyte catalog for {source_name}...")
    write_catalog_file(source_name, Path(output_file))
    console.print(f"Generated Airbyte catalog at {output_file}")


@main.command()
@click.argument("source_name", type=str)
@click.argument(
    "project_name",
    type=str,
    default="fivetran-interop",
)
@click.option(
    "--config-file",
    help="Path to config.yml (defaults to catalog/{source_name}/src/{project_name}/config.yml)",
)
@click.option(
    "--db-path",
    help="Path to DuckDB database (defaults to .data/{source_name}.duckdb)",
)
def create_airbyte_data(
    source_name: str,
    project_name: str,
    config_file: str | None = None,
    db_path: str | None = None,
) -> None:
    """Sync data from an Airbyte source to a local database.

    This command syncs data from an Airbyte source to a local DuckDB database.
    The streams to sync are specified in the config.yml file.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    from pathlib import Path

    from morph.utils.airbyte_sync import sync_source

    # Set default paths if not provided
    if not config_file:
        config_file = f"catalog/{source_name}/src/{project_name}/config.yml"
    if not db_path:
        db_path = f".data/{source_name}.duckdb"

    # Load streams from config.yml
    config_path = Path(config_file)
    if not config_path.exists():
        raise ValueError(f"Error: Config file {config_file} does not exist")

    config = yaml.safe_load(config_path.read_text())
    source_streams = config.get("source_streams", [])
    # target_tables will be used in future implementations
    _ = config.get("target_tables", [])

    console.print(f"Syncing {source_name} data for streams: {', '.join(source_streams)}...")
    sync_source(source_name, source_streams, db_path)
    console.print(f"Synced {source_name} data to {db_path}")


@main.command()
@click.argument("source_name", type=str)
@click.argument("project_name", type=str)
@click.option(
    "--output-dir",
    help="Output directory for generated transform files (defaults to catalog/{source_name}/src/{project_name}/transforms)",
)
def generate_transform_scaffold(
    source_name: str,
    project_name: str,
    output_dir: str | None = None,
) -> None:
    """Generate scaffold mapping YAML files for target tables.

    This command generates blank mapping YAML files for any target tables
    that are not yet defined. The generated files will include all fields
    from the target schema but with MISSING expressions.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    from pathlib import Path

    from morph.utils.transform_scaffold import (
        generate_mapping_files,
        get_target_schema,
        load_config,
        report_results,
    )

    # Set default paths if not provided
    config_file = f"catalog/{source_name}/src/{project_name}/config.yml"
    if not output_dir:
        output_dir = f"catalog/{source_name}/src/{project_name}/transforms"

    # Set path for local target schema file
    requirements_dir = f"catalog/{source_name}/requirements/{project_name}"
    Path(requirements_dir).mkdir(parents=True, exist_ok=True)

    # Load config and target schema
    config, target_tables = load_config(config_file)
    if not config or not target_tables:
        return

    target_schema = get_target_schema(config, requirements_dir)
    if not target_schema:
        return

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Process each target table
    created_files = generate_mapping_files(
        source_name,
        project_name,
        target_tables,
        target_schema,
        output_path,
    )

    report_results(created_files)


def generate_lock_file(
    source_name: str,
    project_name: str,
) -> None:
    """Generate a lock file for a project.

    Args:
        source_name: Name of the source
        project_name: Name of the project
    """
    from pathlib import Path

    from morph.utils.transform_scaffold import get_target_schema, load_config

    # Set paths
    config_file = f"catalog/{source_name}/src/{project_name}/config.yml"
    mapping_dir = Path(f"catalog/{source_name}/src/{project_name}/transforms")
    lock_file = Path(f"catalog/{source_name}/src/morph-lock.toml")

    # Ensure parent directory exists
    lock_file.parent.mkdir(parents=True, exist_ok=True)

    # Set path for local target schema file
    requirements_dir = f"catalog/{source_name}/requirements/{project_name}"
    Path(requirements_dir).mkdir(parents=True, exist_ok=True)

    # Load config and target schema
    config, target_tables = load_config(config_file)
    if not config or not target_tables:
        console.print(f"Error: Could not load config from {config_file}", style="bold red")
        return

    target_schema = get_target_schema(config, requirements_dir)
    if not target_schema:
        console.print("Error: Could not load target schema", style="bold red")
        return

    # Generate lock file
    try:
        generate_lock_file_for_project(
            source_name=source_name,
            project_name=project_name,
            config=config,
            mapping_dir=mapping_dir,
            target_schema=target_schema,
            output_path=lock_file,
        )
    except ValueError as e:
        console.print(f"Error generating lock file: {e}", style="bold red")


# Project Auto-Generation
@main.command()
@click.argument("source_name", type=str)
@click.option("--project-name", type=str, default="fivetran-interop")
@click.option("--no-airbyte-catalog", is_flag=True)
@click.option("--no-transforms", is_flag=True)
@click.option("--no-dbt-project", is_flag=True)
@click.option("--no-lock-file", is_flag=True)
def generate_project(
    source_name: str,
    project_name: str,
    *,
    no_airbyte_catalog: bool | None = None,
    no_transforms: bool | None = None,
    no_dbt_project: bool | None = None,
    no_lock_file: bool | None = None,
) -> None:
    """Generate a project scaffold for a new connector, or update an existing one."""

    def _if_none(input: Any, default: bool | None, /) -> Any:
        return input if input is not None else default

    no_airbyte_catalog = _if_none(no_airbyte_catalog, False)
    no_transforms = _if_none(no_transforms, False)
    no_dbt_project = _if_none(no_dbt_project, False)
    no_lock_file = _if_none(no_lock_file, False)

    # Validate input arguments
    if not source_name or not project_name:
        console.print("Error: --source-name and --project-name are required", style="bold red")
        return

    # Generate Airbyte catalog
    if not no_airbyte_catalog:
        console.print(f"Generating Airbyte catalog for {source_name}...")
        create_airbyte_catalog(source_name)
        console.print("Generated Airbyte catalog.")

    # Generate transforms
    if not no_transforms:
        console.print(f"Generating transforms for {source_name}...")
        generate_transform_scaffold(source_name, project_name)
        console.print(f"Generated transforms for {source_name}")

    # Generate lock file
    if not no_lock_file:
        console.print(f"Generating lock file for {source_name}...")
        generate_lock_file(source_name, project_name)
        console.print(f"Generated lock file for {source_name}")

    # Generate dbt project
    if not no_dbt_project:
        console.print(f"Generating dbt project for {source_name}...")
        generate_dbt_project(source_name, project_name)
        console.print(f"Generated dbt project for {source_name}")


@main.command()
@click.argument(
    "mapping_file",
    type=click.Path(exists=True, path_type=Path),
)
def eval_mapping_confidence(
    mapping_file: Path,
) -> None:
    """Evaluate confidence of a mapping configuration.

    MAPPING_FILE should be a YAML file containing field mappings.
    """
    # Read mapping file
    mapping_data = yaml.safe_load(mapping_file.read_text())

    # Extract fields from dbt transform format
    fields = []
    for transform in mapping_data.get("transforms", []):
        for field_name, field_data in transform.get("fields", {}).items():
            fields.append(
                {
                    "name": field_name,
                    "expression": field_data.get("expression", ""),
                    "description": field_data.get("description", ""),
                    "tests": [],  # TODO: Extract tests if present
                }
            )

    if not fields:
        console.print("[red]No fields found in the mapping file.[/red]")
        return

    # Get confidence score
    confidence = get_mapping_confidence(fields)

    # Create results table
    table = Table(title="Mapping Confidence Analysis")
    table.add_column("Field", style="cyan")
    table.add_column("Confidence", style="green", justify="right")
    table.add_column("Expression", style="yellow")
    table.add_column("Description", style="white")

    for field, score in confidence.field_scores.items():
        field_data = next((f for f in fields if f["name"] == field), {})
        table.add_row(
            field,
            f"{score:.2f}",
            field_data.get("expression", ""),
            field_data.get("description", ""),
        )

    # Print results
    console.print(f"\nOverall Confidence Score: [green]{confidence.score:.2f}[/green]")
    console.print(f"\nExplanation: {confidence.explanation}")
    console.print("\nField-by-Field Analysis:")
    console.print(table)


if __name__ == "__main__":
    main()
