"""Command-line interface for Morph."""

from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from morph import models, resources
from morph.ai import map
from morph.ai.checks import check_openai_api_key
from morph.ai.eval import get_table_mapping_eval
from morph.constants import DEFAULT_PROJECT_NAME
from morph.utils import text_utils
from morph.utils.airbyte_sync import sync_source
from morph.utils.dbml.dbml_visualizer import render_dbml_to_svg
from morph.utils.dbt_build import build_dbt_project
from morph.utils.lock_file import update_lock_file
from morph.utils.logic import if_none
from morph.utils.transform_scaffold import (
    generate_transform_scaffold,
)

try:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=Path.cwd() / ".env")
except ImportError:
    pass  # python-dotenv not installed, skipping .env loading

console = Console()


@click.group()
@click.version_option(package_name="morph", prog_name="morph")
def main() -> None:
    """Morph CLI."""
    pass


@main.command()
@click.argument("source_name", type=str)
@click.argument(
    "project_name",
    type=str,
    default=DEFAULT_PROJECT_NAME,
)
@click.option(
    "--db-path",
    help="Path to DuckDB database (defaults to .data/{source_name}.duckdb)",
    type=click.Path(path_type=Path),
)
@click.option(
    "--no-catalog",
    is_flag=True,
    help="Skip catalog generation",
)
@click.option(
    "--no-creds",
    is_flag=True,
    help="Skip credentials",
)
@click.option(
    "--with-data",
    is_flag=True,
    default=None,
    help="Include data extraction",
)
def sync(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    db_path: Path | None = None,
    *,
    no_catalog: bool = False,
    no_creds: bool = False,
    with_data: bool | None = None,
) -> None:
    """Sync data from an Airbyte source to a local database.

    This command syncs data from an Airbyte source to a local DuckDB database.
    The streams to sync are specified in the config.yml file.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    console.print(
        f"Syncing '{source_name}' database...",
    )
    sync_source(
        source_name=source_name,
        project_name=project_name,
        streams="*",
        db_path=db_path,
        with_data=with_data,
        no_catalog=no_catalog,
        no_creds=no_creds,
    )
    console.print(f"Synced '{source_name}' database.")


@main.command()
@click.argument("source_name", type=str)
@click.argument("project_name", type=str, default=DEFAULT_PROJECT_NAME)
def lock(
    source_name: str,
    project_name: str,
) -> None:
    """Update the project's lock file.

    This command creates a morph-lock.toml file in the project's src directory
    that tracks unused source streams, unused source fields, unmapped target tables,
    and unmapped target table fields.

    SOURCE_NAME: Name of the source (e.g., 'facebook_marketing')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    # Call the existing update_lock_file function
    console.print(f"Generating lock file for {source_name}...")
    update_lock_file(source_name, project_name)
    console.print(f"Generated lock file for {source_name}")


@main.command()
@click.argument("dbml_file_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output-file-path",
    type=click.Path(path_type=Path),
    help="Path where the SVG file should be written",
)
def visualize_dbml(
    dbml_file_path: Path,
    output_file_path: Path | None = None,
) -> None:
    """Visualize a DBML file as an SVG image using Docker.

    This command renders a DBML file to an SVG image using a Docker-based solution.
    Docker must be installed and available on your system.

    DBML_FILE_PATH: Path to the DBML file to visualize
    """
    try:
        render_dbml_to_svg(
            dbml_file_path=dbml_file_path,
            output_file_path=output_file_path,
        )
    except Exception as e:
        console.print(f"Error visualizing DBML file: {e!s}")
        sys.exit(1)


# Project Auto-Generation
@main.command()
@click.argument("source_name", type=str)
@click.option("--project-name", type=str, default=DEFAULT_PROJECT_NAME)
@click.option("--no-airbyte-catalog", is_flag=True)
@click.option("--no-creds", is_flag=True)
@click.option("--no-transforms", is_flag=True)
@click.option("--no-dbt-project", is_flag=True)
@click.option("--no-lock-file", is_flag=True)
def build(
    source_name: str,
    project_name: str,
    *,
    no_airbyte_catalog: bool | None = None,
    no_creds: bool | None = None,
    no_transforms: bool | None = None,
    no_dbt_project: bool | None = None,
    no_lock_file: bool | None = None,
) -> None:
    """Build auto-generated source and project artifacts."""
    no_airbyte_catalog = if_none(no_airbyte_catalog, False)
    no_transforms = if_none(no_transforms, False)
    no_dbt_project = if_none(no_dbt_project, False)
    no_lock_file = if_none(no_lock_file, False)

    # Validate input arguments
    if not source_name or not project_name:
        console.print("Error: --source-name and --project-name are required", style="bold red")
        return

    # Generate Airbyte catalog and schema artifacts
    if not any([no_airbyte_catalog, no_creds]):
        console.print(f"Generating Airbyte catalog for {source_name}...")
        sync_source(
            source_name,
            no_catalog=no_airbyte_catalog,
            no_creds=no_creds,
            with_data=False,
        )
        console.print("Generated Airbyte catalog.")

    # Generate transforms
    if not no_transforms:
        console.print(f"Generating transforms for {source_name}...")
        generate_transform_scaffold(source_name, project_name)
        console.print(f"Generated transforms for {source_name}")

    # Generate lock file
    if not no_lock_file:
        console.print(f"Generating lock file for {source_name}...")
        update_lock_file(source_name, project_name)
        console.print(f"Generated lock file for {source_name}")

    # Generate dbt project
    if not no_dbt_project:
        console.print(f"Generating dbt project for {source_name}...")
        build_dbt_project(source_name, project_name)
        console.print(f"Generated dbt project for {source_name}")


@main.command()
@click.argument("source_name")
@click.argument("project_name", default=DEFAULT_PROJECT_NAME)
@click.option(
    "--no-build",
    is_flag=True,
    help="Skip building the dbt project after evaluation",
    type=bool,
    default=False,
)
def eval(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    *,
    do_source_annotations: bool = True,
    no_build: bool = False,
) -> None:
    """Use AI to evaluated the quality of transform logic.

    SOURCE_NAME is the name of the source (e.g., hubspot, shopify)
    PROJECT_NAME is the name of the project (defaults to fivetran-interop)
    """
    check_openai_api_key()
    # Construct the path to the transforms directory
    transforms_dir = resources.get_transforms_dir(
        source_name=source_name,
        project_name=project_name,
    )

    if not transforms_dir.exists():
        console.print(f"[red]Error: Transforms directory not found at {transforms_dir}[/red]")
        return

    # Find all YAML files
    yaml_files = list(transforms_dir.glob("**/*.yml")) + list(transforms_dir.glob("**/*.yaml"))

    if not yaml_files:
        console.print(f"[yellow]No YAML files found in {transforms_dir}[/yellow]")
        return

    # Process each YAML file
    for yaml_file in sorted(yaml_files):
        console.print(f"\n[bold]Evaluating {yaml_file}[/bold]\n")
        transform_obj = models.TransformFile.from_file(yaml_file)

        # Get confidence score
        table_mapping_eval: models.TableMappingEval = get_table_mapping_eval(
            transform_obj.field_mappings,
        )

        # Print analysis
        transform_obj.attach_evaluation(table_mapping_eval)
        transform_obj.print_as_rich_table()

        if do_source_annotations:
            transform_obj.to_file()

    update_lock_file(
        source_name=source_name,
        project_name=project_name,
    )

    if not no_build:
        console.print("\n" + ("-" * 80) + "\n")
        console.print("Rebuilding dbt project...", style="bold green")
        build_dbt_project(source_name, project_name)
        console.print("Build step completed successfully.", style="bold green")


@main.command()
@click.argument("source_name")
@click.argument("project_name", default=DEFAULT_PROJECT_NAME)
@click.option("--auto-confirm", is_flag=True, help="Automatically confirm mappings")
@click.option(
    "--include-skipped-tables",
    is_flag=True,
    help="Include skipped tables in the generation",
    type=bool,
    default=False,
)
@click.option(
    "--no-build",
    is_flag=True,
    help="Skip building the dbt project after generation",
    type=bool,
    default=False,
)
@click.option(
    "--regenerate-all",
    is_flag=True,
    help="Regenerate all mappings, even if they are already present",
    type=bool,
    default=False,
)
def generate(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    *,
    auto_confirm: bool | None = None,
    regenerate_all: bool = False,
    include_skipped_tables: bool = False,
    no_build: bool = False,
) -> None:
    """Use AI to generate new transform code for a project."""
    check_openai_api_key()
    requirements_dbt_source_file = resources.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not requirements_dbt_source_file.exists():
        console.print(f"Error: {requirements_dbt_source_file} does not exist", style="bold red")
        return

    console.print(
        f"Reading target tables list from '{requirements_dbt_source_file}' dbt source file...",
        style="green",
    )
    dbt_requirements_file: models.DbtSourceFile = models.DbtSourceFile.from_file(
        requirements_dbt_source_file,
    )
    config_file_content = text_utils.load_yaml_file(
        resources.get_config_file_path(
            source_name=source_name,
            project_name=project_name,
        ),
    )
    target_tables: list[str] = []
    skipped_tables: list[str] = config_file_content.get("target_tables_skipped", [])
    for target_table in dbt_requirements_file.source_tables:
        console.print(f"Evaluating '{target_table.name}'...")
        include_table = True
        transform_file = resources.get_transform_file(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table.name,
        )
        if regenerate_all:
            console.print(
                f"Regenerating '{target_table.name}' target table...",
                style="green",
            )
            target_tables.append(target_table.name)
            continue

        if transform_file.exists():
            transform_def = models.TransformFile.from_file(transform_file)
            if transform_def.get_mapped_fields():  # Skip if at least some fields are mapped
                include_table = False
                console.print(
                    f"Skipping '{target_table.name}' because it already has mappings.",
                    style="yellow",
                )

        if include_table and transform_file in skipped_tables:
            include_table = False
            console.print(
                f"Skipping '{target_table.name}' because it was found in the skipped tables list.",
                style="yellow",
            )

        if include_table:
            console.print(
                f"Found '{target_table.name}' target table with missing mappings ...",
                style="green",
            )
            target_tables.append(target_table.name)

    if not target_tables:
        console.print("All tables are up to date. Exiting.", style="bold green")
        return

    delim = "'\n - '"
    table = Table(
        title="Mapping Tables",
        show_lines=True,
    )
    table.add_column(
        "Source Tables",
    )
    table.add_column(
        "Target Tables",
    )
    table.add_row(
        f" - '{delim.join([s.name for s in dbt_requirements_file.source_tables])}'",
        f" - '{delim.join(target_tables)}'",
    )
    console.print(table)
    for target_table in target_tables:
        if (
            not regenerate_all
            and not include_skipped_tables
            and (
                target_table
                in map.get_skipped_target_tables(
                    source_name,
                    project_name,
                )
            )
        ):
            console.print(
                f"Skipping '{target_table}' because it was found in the skipped tables list.",
            )
            continue

        console.print(
            f"Generating missing mappings for '{target_table}'...",
            style="bold white on blue",
        )
        map.infer_table_mappings(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table,
            auto_confirm=auto_confirm,
            regenerate_all=regenerate_all,
        )

    console.print("Generation complete. Updating lock file...", style="bold green")
    update_lock_file(source_name, project_name)

    # Run the build step after generation is complete
    if not no_build:
        console.print("\n" + ("-" * 80) + "\n")
        console.print("Rebuilding dbt project...", style="bold green")
        build_dbt_project(source_name, project_name)
        console.print("Build step completed successfully.", style="bold green")


if __name__ == "__main__":
    main()
