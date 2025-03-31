"""Command-line interface for Morph."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import click
from rich.console import Console

from morph import models, resources
from morph.ai import map
from morph.ai.eval import get_table_mapping_eval
from morph.constants import DEFAULT_PROJECT_NAME
from morph.utils import text_utils
from morph.utils.airbyte_catalog import write_catalog_file
from morph.utils.airbyte_sync import sync_source
from morph.utils.dbt_source_files import (
    generate_dbt_sources_yml_from_airbyte_catalog,
)
from morph.utils.lock_file import generate_lock_file_for_project
from morph.utils.logic import if_none
from morph.utils.mapping_to_dbt_models import generate_dbt_package
from morph.utils.transform_scaffold import (
    download_target_schema,
    generate_transform_scaffold,
)

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
    "--run-tests",
    is_flag=True,
    help="Run tests after generating the dbt project",
    default=True,
)
def generate_dbt_project(
    source_name: str,
    project_name: str,
    *,
    run_tests: bool = True,
) -> None:
    """Generate a dbt project from mapping files.

    This command generates a dbt project from mapping files. The mapping files
    should be in YAML format and located in the mapping directory.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    _ = project_name  # Not used currently

    catalog_dir = resources.get_catalog_root_dir()
    if source_name is None:
        raise ValueError("Error: --source-name is required")

    catalog_file = resources.get_generated_catalog_path(
        source_name,
        project_name,
    )

    # Validate input paths exist
    if not catalog_dir.exists():
        raise ValueError(f"Error: {catalog_dir} does not exist")

    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    dbt_project_dir = resources.get_generated_dbt_project_dir(
        source_name=source_name,
        project_name=project_name,
    )
    # Generate dbt package
    try:
        # Generate dbt models from mapping files
        generate_dbt_package(
            source_name=source_name,
            project_name=project_name,
        )

        # Get sources.yml path from generated directory
        generated_sources_path = resources.get_generated_source_yml_path(
            source_name=source_name,
            project_name=project_name,
        )
        if not generated_sources_path.exists():
            # Only generate sources.yml if it doesn't exist.
            # Otherwise, we'll copy the existing sources.yml into the generated directory.
            generate_dbt_sources_yml_from_airbyte_catalog(
                source_name=source_name,
                project_name=project_name,
                catalog_file=catalog_file,
                output_file=generated_sources_path,
            )

        # Get sources.yml path in dbt project models directory
        new_sources_path = (
            resources.get_generated_dbt_project_models_dir(
                source_name,
                project_name,
            )
            / "src_airbyte_raw.yml"
        )

        # Ensure parent directory exists
        new_sources_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert dict to YAML string before writing
        #
        # new_sources_path.write_text(yaml.dump(sources_yml, default_flow_style=False, sort_keys=False))

        # Copy sources.yml into the generated directory
        shutil.copy(generated_sources_path, new_sources_path)

        console.print(f"Generated dbt project at {dbt_project_dir}")
    except Exception as e:
        console.print(f"Error generating dbt project: {e}", style="bold red")

    if run_tests:
        console.print("Running dbt tests...")
        result = subprocess.run(
            ["uv", "run", "dbt", "run", "--profiles-dir", "profiles"],
            cwd=dbt_project_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode == 0:
            print(result.stdout.replace("\\n", "\n"))
            console.print("DBT tests completed.")
        else:
            print(f"Error running dbt tests: {result.stderr}")
            print(f"Command output: {result.stdout}")

        console.print("DBT tests completed.")


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
    "--no-data",
    is_flag=True,
    help="Skip data extraction",
)
@click.option(
    "--no-creds",
    is_flag=True,
    help="Skip credentials",
)
def create_airbyte_db(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    db_path: Path | None = None,
    *,
    no_catalog: bool = False,
    no_data: bool = False,
    no_creds: bool = False,
) -> None:
    """Sync data from an Airbyte source to a local database.

    This command syncs data from an Airbyte source to a local DuckDB database.
    The streams to sync are specified in the config.yml file.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    if not no_catalog:
        console.print(f"Generating Airbyte catalog for '{source_name}'...")
        write_catalog_file(
            source_name=source_name,
        )
        console.print(f"Generating dbt source file for '{source_name}'.")
        generate_dbt_sources_yml_from_airbyte_catalog(
            source_name=source_name,
            project_name=project_name,
        )
        console.print(f"Generated Airbyte catalog and dbt source file for {source_name}.")

    console.print(
        f"Syncing '{source_name}' database...",
    )
    sync_source(
        source_name=source_name,
        streams="*",
        db_path=db_path,
        no_data=no_data,
        no_creds=no_creds,
    )
    console.print(f"Synced '{source_name}' database: {db_path}")


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


@main.command()
@click.argument("source_name", type=str)
@click.argument("project_name", type=str, default=DEFAULT_PROJECT_NAME)
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
@click.option("--project-name", type=str, default=DEFAULT_PROJECT_NAME)
@click.option("--no-airbyte-catalog", is_flag=True)
@click.option("--no-data", is_flag=True)
@click.option("--no-creds", is_flag=True)
@click.option("--no-transforms", is_flag=True)
@click.option("--no-dbt-project", is_flag=True)
@click.option("--no-lock-file", is_flag=True)
def generate_project(
    source_name: str,
    project_name: str,
    *,
    no_airbyte_catalog: bool | None = None,
    no_data: bool | None = None,
    no_creds: bool | None = None,
    no_transforms: bool | None = None,
    no_dbt_project: bool | None = None,
    no_lock_file: bool | None = None,
) -> None:
    """Generate a project scaffold for a new connector, or update an existing one."""
    no_airbyte_catalog = if_none(no_airbyte_catalog, False)
    no_transforms = if_none(no_transforms, False)
    no_dbt_project = if_none(no_dbt_project, False)
    no_lock_file = if_none(no_lock_file, False)

    # Validate input arguments
    if not source_name or not project_name:
        console.print("Error: --source-name and --project-name are required", style="bold red")
        return

    # Generate Airbyte catalog
    if not any([no_airbyte_catalog, no_data, no_creds]):
        console.print(f"Generating Airbyte catalog for {source_name}...")
        create_airbyte_db.callback(
            source_name,
            no_catalog=no_airbyte_catalog,
            no_data=no_data,
            no_creds=no_creds,
        )  # type: ignore  (mypy doesn't recognize the callback signature)
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
        generate_dbt_project.callback(source_name, project_name)  # type: ignore  (mypy doesn't recognize the callback signature)
        console.print(f"Generated dbt project for {source_name}")


@main.command()
@click.argument("source_name")
@click.argument("project_name", default=DEFAULT_PROJECT_NAME)
def eval_project_mappings(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> None:
    """Evaluate confidence of all mapping files in a project.

    SOURCE_NAME is the name of the source (e.g., hubspot, shopify)
    PROJECT_NAME is the name of the project (defaults to fivetran-interop)
    """
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
    for yaml_file in yaml_files:
        console.print(f"\n[bold]Evaluating {yaml_file}[/bold]\n")
        transform_obj = models.TableMapping.from_file(yaml_file)

        # Get confidence score
        table_mapping_eval: models.TableMappingEval = get_table_mapping_eval(
            transform_obj.field_mappings,
        )

        # Print analysis
        table_mapping_eval.print_as_rich_table(
            from_transform=transform_obj,
        )


@main.command()
@click.argument("source_name")
@click.argument("project_name", default=DEFAULT_PROJECT_NAME)
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
    project_name: str = DEFAULT_PROJECT_NAME,
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
    map.infer_table_mappings(
        source_name,
        project_name,
        transform_name=target_table,
        source_table=source_table,
        auto_confirm=auto_confirm,
    )


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
def generate_missing_mappings(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    *,
    auto_confirm: bool | None = None,
    include_skipped_tables: bool = False,
) -> None:
    """Generate missing mappings for a project."""
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
        if transform_file.exists():
            transform_def = models.TableMapping.from_file(transform_file)
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

    console.print(
        f"Generating missing mappings for {len(target_tables)} tables: {', '.join(target_tables)}...",
    )

    for target_table in target_tables:
        if not include_skipped_tables and (
            target_table
            in map.get_skipped_target_tables(
                source_name,
                project_name,
            )
        ):
            console.print(
                f"Skipping '{target_table}' because it was found in the skipped tables list.",
            )
            continue

        console.print(f"Generating missing mappings for '{target_table}'...")
        map.infer_table_mappings(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table,
            auto_confirm=auto_confirm,
        )


if __name__ == "__main__":
    main()
