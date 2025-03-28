"""Command-line interface for Morph."""

import shutil
from pathlib import Path

import click
from rich.console import Console

from morph import models
from morph.ai import map
from morph.ai.eval import get_table_mapping_eval
from morph.constants import DEFAULT_PROJECT_NAME, HEADER_COMMENT
from morph.utils import resource_paths, text_utils
from morph.utils.airbyte_catalog import write_catalog_file
from morph.utils.dbt_source_files import (
    generate_dbt_sources_yml_from_airbyte_catalog,
)
from morph.utils.lock_file import generate_lock_file_for_project
from morph.utils.logic import if_none
from morph.utils.mapping_to_dbt_models import generate_dbt_package
from morph.utils.transform_scaffold import (
    download_target_schema,
    generate_transform_scaffold,
    load_config,
)

console = Console()


@click.group()
@click.version_option(package_name="morph", prog_name="morph")
def main() -> None:
    """Morph CLI."""
    pass


@main.command()
@click.argument(
    "catalog_file",
    type=click.Path(exists=True, path_type=Path),
)
@click.option("--source-name", type=str, help="Name of the source (e.g., 'hubspot')")
@click.option(
    "--output-file",
    help="Output file path",
    type=click.Path(path_type=Path),
)
@click.option("--database", type=str, help="Database name")
@click.option("--schema", type=str, help="Schema name")
def airbyte_catalog_to_dbt_sources_yml(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    *,
    catalog_file: Path | None = None,
    output_file: Path | None = None,
    database: str | None = None,
    schema: str | None = None,
) -> None:
    """Convert JSON schema files or Airbyte catalogs to a dbt sources.yml file.

    This command converts a JSON schema or Airbyte catalog to a dbt sources.yml file.
    The catalog file can be either a JSON schema or an Airbyte catalog.

    CATALOG_FILE: Path to the JSON schema or Airbyte catalog file
    """
    generate_dbt_sources_yml_from_airbyte_catalog(
        source_name=source_name,
        project_name=project_name,
        catalog_file=catalog_file,
        output_file=output_file,
        database=database,
        schema=schema,
    )


@main.command()
@click.argument("source_name", type=str)
@click.argument(
    "project_name",
    type=str,
    default=DEFAULT_PROJECT_NAME,
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
        generated_sources_path = resource_paths.get_generated_source_yml_path(
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
        new_sources_path = (
            resource_paths.get_generated_dbt_project_models_dir(
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
    default=DEFAULT_PROJECT_NAME,
)
@click.option(
    "--config-file",
    type=click.Path(path_type=Path),
    help="Path to config.yml (defaults to catalog/{source_name}/src/{project_name}/config.yml)",
)
@click.option(
    "--db-path",
    help="Path to DuckDB database (defaults to .data/{source_name}.duckdb)",
    type=click.Path(path_type=Path),
)
def create_airbyte_data(
    source_name: str,
    project_name: str,
    config_file: Path | None = None,
    db_path: Path | None = None,
) -> None:
    """Sync data from an Airbyte source to a local database.

    This command syncs data from an Airbyte source to a local DuckDB database.
    The streams to sync are specified in the config.yml file.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    from morph.utils.airbyte_sync import sync_source

    # Set default paths if not provided
    if not config_file:
        config_file = Path(f"catalog/{source_name}/src/{project_name}/config.yml")
    if not db_path:
        db_path = Path(f".data/{source_name}.duckdb")

    # Load streams from config.yml
    config_path = Path(config_file)
    if not config_path.exists():
        raise ValueError(f"Error: Config file {config_file} does not exist")

    config = text_utils.load_yaml_file(config_path)
    source_streams = config.get("source_streams", [])
    # target_tables will be used in future implementations
    _ = config.get("target_tables", [])

    console.print(f"Syncing {source_name} data for streams: {', '.join(source_streams)}...")
    sync_source(source_name, source_streams, db_path)
    console.print(f"Synced {source_name} data to {db_path}")


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
    config = load_config(config_file)
    if not config:
        console.print(f"Error: Could not load config from {config_file}", style="bold red")
        return

    download_target_schema(
        source_name=source_name,
        project_name=project_name,
        config=config,
        if_not_exists=True,
    )
    target_schema = text_utils.load_yaml_file(
        resource_paths.get_dbt_sources_requirements_path(
            source_name=source_name,
            project_name=project_name,
        ),
    )

    if not target_schema:
        console.print("Error: Could not load target schema", style="bold red")
        return

    # Generate lock file
    try:
        generate_lock_file_for_project(
            source_name=source_name,
            project_name=project_name,
            mapping_dir=mapping_dir,
            target_schema=target_schema,
            output_path=lock_file,
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
@click.option(
    "--no-airbyte-catalog",
    is_flag=True,
    default=True,  # TODO: Revert to False once we resolve the serpyco-rs issue
)
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
    no_airbyte_catalog = if_none(no_airbyte_catalog, False)
    no_transforms = if_none(no_transforms, False)
    no_dbt_project = if_none(no_dbt_project, False)
    no_lock_file = if_none(no_lock_file, False)

    # Validate input arguments
    if not source_name or not project_name:
        console.print("Error: --source-name and --project-name are required", style="bold red")
        return

    # Generate Airbyte catalog
    if not no_airbyte_catalog:
        console.print(f"Generating Airbyte catalog for {source_name}...")
        create_airbyte_catalog.callback(source_name)
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
        generate_dbt_project.callback(source_name, project_name)
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
        mapping_data = text_utils.load_yaml_file(yaml_file)

        # Extract fields from dbt transform format
        fields: list[models.FieldMapping] = []
        for transform in mapping_data.get("transforms", []):
            for field_name, field_data in transform.get("fields", {}).items():
                fields.append(
                    models.FieldMapping(
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
        models.print_table_mapping_analysis(
            table_mapping_eval=table_mapping_eval,
            fields=fields,
            title=f"Mapping Confidence Analysis - {yaml_file.name}",
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
    requirements_dbt_source_file = resource_paths.get_dbt_sources_requirements_path(
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
        resource_paths.get_config_file_path(
            source_name=source_name,
            project_name=project_name,
        ),
    )
    target_tables: list[str] = []
    skipped_tables: list[str] = config_file_content.get("target_tables_skipped", [])
    for target_table in dbt_requirements_file.source_tables:
        console.print(f"Evaluating '{target_table.name}'...")
        include_table = True
        transform_file = resource_paths.get_transform_file(
            source_name=source_name,
            project_name=project_name,
            transform_name=target_table.name,
        )
        if transform_file.exists():
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


@main.command()
@click.argument("catalog_path", type=click.Path(exists=True))
@click.option("--source-name", default="default_source", help="Name for the dbt source")
@click.option("--database", help="Database name for the source")
@click.option("--schema", help="Schema name for the source")
@click.option("--output", default="sources.yml", help="Output file path")
def airbyte_catalog_to_dbt(
    catalog_path: str,
    source_name: str,
    database: str | None,
    schema: str | None,
    output: str,
) -> None:
    """Convert JSON schema files or Airbyte catalog to dbt sources.yml format."""
    catalog_path_obj = Path(catalog_path)

    # Validate input path exists
    if not catalog_path_obj.exists():
        raise ValueError(f"Error: {catalog_path} does not exist")

    if not catalog_path_obj.is_file() or not catalog_path_obj.name.endswith(".json"):
        raise ValueError(f"Error: {catalog_path} is not a valid JSON file")

    from morph.models import DbtSourceFile

    dbt_file = DbtSourceFile.from_airbyte_catalog_json(
        catalog_file=catalog_path,
        source_name=source_name,
    )

    sources_yml = dbt_file.to_dict()

    if (database or schema) and sources_yml.get("sources"):
        if database:
            sources_yml["sources"][0]["database"] = database
        if schema:
            sources_yml["sources"][0]["schema"] = schema

    # Write to output file with header comment
    output_path = Path(output)
    output_path.write_text(HEADER_COMMENT + text_utils.dump_yaml_str(sources_yml))

    console.print(f"Generated dbt sources.yml at {output}")


if __name__ == "__main__":
    main()
