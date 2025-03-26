"""Command-line interface for Morph."""

import shutil
from pathlib import Path
from typing import Any

import click
import yaml
from rich.console import Console

from morph.ai import models
from morph.ai.eval import get_table_mapping_eval
from morph.ai.map import (
    change_mapping_source_table,
    get_best_match_source_stream_name,
    populate_missing_mappings,
)
from morph.ai.models import (
    FieldMapping,
    TableMapping,
    print_table_mapping_analysis,
)
from morph.utils import resource_paths
from morph.utils.airbyte_catalog import write_catalog_file
from morph.utils.dbt_source_files import (
    generate_dbt_sources_yml_from_airbyte_catalog,
)
from morph.utils.lock_file import generate_lock_file_for_project
from morph.utils.mapping_to_dbt_models import generate_dbt_package
from morph.utils.transform_scaffold import (
    generate_mapping_files,
    get_target_schema,
    load_config,
    report_results,
)

console = Console()


def _if_none(input: Any, default: bool | None, /) -> Any:
    """Helper function to return input if it is not None, otherwise return default."""
    return input if input is not None else default


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
def airbyte_catalog_to_dbt_sources_yml(
    source_name: str,
    project_name: str = "fivetran-interop",
    *,
    catalog_file: str | None = None,
    output_file: str | None = None,
    database: str | None = None,
    schema: str | None = None,
) -> None:
    """Convert JSON schema files or Airbyte catalogs to a dbt sources.yml file.

    This command converts a JSON schema or Airbyte catalog to a dbt sources.yml file.
    The catalog file can be either a JSON schema or an Airbyte catalog.

    CATALOG_FILE: Path to the JSON schema or Airbyte catalog file
    """
    generate_dbt_sources_yml_from_airbyte_catalog(
        source_name,
        project_name,
        catalog_file,
        output_file,
        database,
        schema,
    )


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
) -> None:
    """Generate a dbt project from mapping files.

    This command generates a dbt project from mapping files. The mapping files
    should be in YAML format and located in the mapping directory.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    _ = project_name  # Not used currently

    catalog_dir = resource_paths.get_catalog_root_dir()
    if source_name is None:
        raise ValueError("Error: --source-name is required")

    catalog_file = resource_paths.get_generated_catalog_path(
        source_name,
        project_name,
    )

    # Validate input paths exist
    if not catalog_dir.exists():
        raise ValueError(f"Error: {catalog_dir} does not exist")

    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    output_dir = resource_paths.get_generated_dir_root(source_name)

    # Generate dbt package
    try:
        # Generate dbt models from mapping files
        generate_dbt_package(
            source_name=source_name,
            project_name=project_name,
        )

        # Determine the actual output directory
        actual_output_dir = output_dir or resource_paths.get_generated_dir_root(source_name)

        # Get sources.yml path from generated directory
        generated_sources_path = resource_paths.get_generated_sources_yml_path(
            source_name,
            project_name,
        )
        if not generated_sources_path.exists():
            # Only generate sources.yml if it doesn't exist.
            # Otherwise, we'll copy the existing sources.yml into the generated directory.
            generate_dbt_sources_yml_from_airbyte_catalog(
                source_name=source_name,
                project_name=project_name,
                catalog_file=catalog_file,
                output_file=generated_sources_path,
                database=None,  # database
                schema=None,  # schema
            )

        # Get sources.yml path in dbt project models directory
        new_sources_path = actual_output_dir / "models" / "src_airbyte_raw.yml"
        # Ensure parent directory exists
        new_sources_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert dict to YAML string before writing
        #
        # new_sources_path.write_text(yaml.dump(sources_yml, default_flow_style=False, sort_keys=False)) # noqa: ERA001

        # Copy sources.yml into the generated directory
        shutil.copy(generated_sources_path, new_sources_path)

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

    target_schema = get_target_schema(
        source_name=source_name,
        project_name=project_name,
        config=config,
        requirements_dir=requirements_dir,
    )
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
    # Set paths
    config_file = f"catalog/{source_name}/src/{project_name}/config.yml"
    mapping_dir = Path(f"catalog/{source_name}/src/{project_name}/transforms")
    lock_file = resource_paths.get_lock_file_path(
        source_name=source_name,
        project_name=project_name,
    )

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

    target_schema = get_target_schema(
        source_name=source_name,
        project_name=project_name,
        config=config,
        requirements_dir=requirements_dir,
    )
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


@main.command()
@click.argument("source_name", type=str)
@click.argument("project_name", type=str, default="fivetran-interop")
def lock(
    source_name: str,
    project_name: str,
) -> None:
    """Generate a lock file tracking unused streams and fields for a project.

    This command creates a morph-lock.toml file in the project's src directory
    that tracks unused source streams, unused source fields, unmapped target tables,
    and unmapped target table fields.

    SOURCE_NAME: Name of the source (e.g., 'facebook_marketing')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    # Call the existing generate_lock_file function
    console.print(f"Generating lock file for {source_name}...")
    generate_lock_file(source_name, project_name)
    console.print(f"Generated lock file for {source_name}")


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
@click.argument("source_name")
@click.argument("project_name", default="fivetran-interop")
def eval_project_mappings(
    source_name: str,
    project_name: str = "fivetran-interop",
) -> None:
    """Evaluate confidence of all mapping files in a project.

    SOURCE_NAME is the name of the source (e.g., hubspot, shopify)
    PROJECT_NAME is the name of the project (defaults to fivetran-interop)
    """
    # Construct the path to the transforms directory
    transforms_dir = Path("catalog") / source_name / "src" / project_name / "transforms"

    if not transforms_dir.exists():
        console.print(f"[red]Error: Transforms directory not found at {transforms_dir}[/red]")
        return

    # Find all YAML files
    yaml_files = list(transforms_dir.glob("**/*.yml")) + list(transforms_dir.glob("**/*.yaml"))

    if not yaml_files:
        console.print(f"[yellow]No YAML files found in {transforms_dir}[/yellow]")
        return

    # Process each YAML file
    for yaml_file in yaml_files:
        console.print(f"\n[bold]Evaluating {yaml_file}[/bold]\n")

        # Read mapping file
        mapping_data = yaml.safe_load(yaml_file.read_text())

        # Extract fields from dbt transform format
        fields: list[FieldMapping] = []
        for transform in mapping_data.get("transforms", []):
            for field_name, field_data in transform.get("fields", {}).items():
                fields.append(
                    FieldMapping(
                        name=field_name,
                        expression=field_data.get("expression", ""),
                        description=field_data.get("description", ""),
                    ),
                )

        if not fields:
            console.print("[yellow]No fields found in the mapping file.[/yellow]")
            continue

        # Get confidence score
        table_mapping_eval = get_table_mapping_eval(fields)

        # Print analysis
        print_table_mapping_analysis(
            table_mapping_eval=table_mapping_eval,
            fields=fields,
            title=f"Mapping Confidence Analysis - {yaml_file.name}",
        )


@main.command()
@click.argument("source_name")
@click.argument("project_name", default="fivetran-interop")
@click.option("--target-table", type=str, help="Name of the target table to suggest mappings for")
@click.option(
    "--source-table",
    type=str,
    help="Optional name of the source table to suggest mappings for."
    "If not provided, the AI will suggest a source table.",
)
@click.option("--auto-confirm", is_flag=True, help="Automatically confirm mappings")
def suggest_table_mappings(
    source_name: str,
    project_name: str = "fivetran-interop",
    *,
    target_table: str,
    source_table: str | None = None,
    auto_confirm: bool | None = None,
) -> None:
    """Suggest table mappings for a project.

    SOURCE_NAME is the name of the source (e.g., hubspot, shopify)
    PROJECT_NAME is the name of the project (defaults to fivetran-interop)
    TARGET_TABLE is the name of the target table to suggest mappings for
    """
    auto_confirm = _if_none(auto_confirm, False)

    if not target_table:
        console.print("Error: --target-table is required", style="bold red")
        return

    # Find the YAML file
    yaml_file = resource_paths.get_transform_file(
        source_name,
        project_name=project_name,
        transform_name=target_table,
    )

    if not yaml_file.exists():
        console.print(f"[yellow]No YAML file found for target table {target_table}[/yellow]")
        return

    # Extract fields from dbt transform format
    current_mapping = TableMapping.read_from_transform_file(yaml_file)
    print(current_mapping)

    # Get all source schemas
    dbt_source_file_path = resource_paths.get_generated_sources_yml_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not dbt_source_file_path.exists():
        generate_dbt_sources_yml_from_airbyte_catalog(
            source_name=source_name,
            project_name=project_name,
        )

    if not dbt_source_file_path.exists():
        console.print(
            f"[red]Error: Could not generate dbt sources.yml file at {dbt_source_file_path}[/red]"
        )
        return

    if not source_table:
        # We need the AI to suggest a source table

        target_table_schemas = models.SourceTableSummary.from_dbt_source_file(
            resource_paths.get_requirements_dir(
                source_name=source_name,
                project_name=project_name,
            )
            / "src_facebook_ads.yml",  # TODO: Make this dynamic
        )
        target_table_schema = next(
            (t for t in target_table_schemas if t.name == target_table), None
        )
        if not target_table_schema:
            console.print(f"[red]Error: Could not find target table {target_table}[/red]")
            return

        source_tables: list[models.SourceTableSummary] = (
            models.SourceTableSummary.from_dbt_source_file(
                dbt_source_file_path,
            )
        )

        suggested_source_table = get_best_match_source_stream_name(
            target_schema=target_table,
            source_tables=source_tables,
        )
        source_table = suggested_source_table.suggested_source_table_name

    # Ask user to confirm mapping
    confirm_mapping = "y"
    if not auto_confirm:
        confirm_mapping = input(
            f"The table is currently mapped to `{current_mapping.source_stream_name}`. "
            f"Do you want to apply the proposed mapping to use `{source_table}` instead? "
            "All existing mappings will be reset to `MISSING` and a new set of mappings will be generated. "
            "Continue? (y/n)"
        )

    if confirm_mapping == "y":
        print("Mapping confirmed.")
        # Apply mapping
        # Update transform file
        change_mapping_source_table(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table,
            new_source_table=source_table,
        )
        populate_missing_mappings(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table,
        )
        # Update lock file
        # Update dbt project
    else:
        print("Mapping rejected.")


if __name__ == "__main__":
    main()
