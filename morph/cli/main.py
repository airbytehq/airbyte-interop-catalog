"""Command-line interface for Morph."""

import argparse
from pathlib import Path
from typing import Any

import click
import yaml
from rich.console import Console

from morph.utils.json_to_dbt_sources import (
    generate_dbt_sources_yml,
    generate_header_comment,
    parse_airbyte_catalog,
)
from morph.utils.mapping_to_dbt_models import generate_dbt_package

console = Console()


@click.group()
@click.version_option()
def main() -> None:
    """Morph: A Python library for data transformation."""
    pass


@main.command()
@click.argument("schema_path", type=click.Path(exists=True))
@click.option("--catalog", is_flag=True, help="Treat input as Airbyte catalog file")
@click.option("--source-name", default="default_source", help="Name for the dbt source")
@click.option("--database", help="Database name for the source")
@click.option("--schema", help="Schema name for the source")
@click.option("--output", default="sources.yml", help="Output file path")
def json_to_dbt(
    schema_path: str,
    catalog: bool,
    source_name: str,
    database: str | None,
    schema: str | None,
    output: str,
) -> None:
    """Convert JSON schema files or Airbyte catalog to dbt sources.yml format."""
    schema_path_obj = Path(schema_path)

    # Validate input path exists
    if not schema_path_obj.exists():
        raise ValueError(f"Error: {schema_path} does not exist")

    # Process based on input type
    if catalog:
        if not schema_path_obj.is_file() or not schema_path_obj.name.endswith(".json"):
            raise ValueError(f"Error: {schema_path} is not a valid JSON file")

        sources_yml = parse_airbyte_catalog(
            schema_path,
            source_name,
            database,
            schema,
        )
    else:
        schema_files: list[str] = []
        if schema_path_obj.is_dir():
            schema_files.extend(
                str(f) for f in schema_path_obj.iterdir() if f.name.endswith(".json")
            )
        elif schema_path_obj.is_file() and schema_path_obj.name.endswith(".json"):
            schema_files.append(schema_path)
        else:
            console.print(f"Error: {schema_path} is not a valid JSON file or directory")
            return

        if not schema_files:
            console.print("No JSON schema files found")
            return

        sources_yml = generate_dbt_sources_yml(
            schema_files,
            source_name,
            database,
            schema,
        )

    # Generate header comment
    args = argparse.Namespace(
        schema_path=schema_path,
        catalog=catalog,
        source_name=source_name,
        database=database,
        schema=schema,
        output=output,
    )
    header_comment = generate_header_comment(args)

    # Write to output file with header comment
    output_path = Path(output)
    with output_path.open("w") as f:
        f.write(header_comment)
        yaml.dump(sources_yml, f, default_flow_style=False, sort_keys=False)

    console.print(f"Generated dbt sources.yml at {output}")


@main.command()
@click.option(
    "--source-name",
    default=None,
    help="Name for the dbt source (defaults to catalog directory name)",
)
@click.option(
    "--project-name",
    default=None,
    help="Name for the dbt project (defaults to 'fivetran-interop')",
)
@click.argument("catalog_dir", type=click.Path(exists=True))
@click.argument("catalog_file", type=click.Path(exists=True))
@click.option(
    "--output-dir",
    help="Output directory for generated dbt project (defaults to {catalog_dir}/generated)",
)
@click.option(
    "--mapping-dir",
    help="Directory containing mapping files.",
)
def generate_dbt_project(
    source_name: str | None = None,
    project_name: str = "fivetran-interop",
    *,
    catalog_file: str | None = None,
    output_dir: str | None = None,
    mapping_dir: str | None = None,
) -> None:
    """Generate a dbt project from mapping files and catalog.json.

    This command generates a complete dbt project in the specified output directory,
    including models for each transform defined in the mapping files and a sources.yml
    file generated from the catalog.json file.

    CATALOG_DIR: Path to the catalog directory (e.g., 'catalog/hubspot')
    CATALOG_FILE: Path to the Airbyte catalog.json file
    """
    _ = project_name  # Not used currently

    catalog_dir = Path("catalog")
    catalog_file = catalog_file or catalog_dir / source_name / "generated" / "airbyte-catalog.json"

    # Validate input paths exist
    if not catalog_dir.exists():
        raise ValueError(f"Error: {catalog_dir} does not exist")

    if not Path(catalog_file).exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    output_dir = output_dir or catalog_dir / source_name / "generated"
    mapping_dir = mapping_dir or catalog_dir / source_name / "src" / project_name / "transforms"

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
        )

        # Write sources.yml to models directory
        models_dir = actual_output_dir / "dbt_project" / "models"
        models_dir.mkdir(parents=True, exist_ok=True)

        sources_path = models_dir / "sources.yml"
        sources_path.write_text(yaml.dump(sources_yml, default_flow_style=False, sort_keys=False))

        project_dir = actual_output_dir / "dbt_project"
        console.print(f"Generated dbt project at {project_dir}")
        console.print("To use the generated dbt project:")
        console.print(f"  1. cd {project_dir}")
        console.print("  2. dbt deps --profiles-dir profiles")
        console.print("  3. dbt compile --profiles-dir profiles")
    except Exception as e:
        raise ValueError(f"Error generating dbt project: {e}") from e


@main.command()
@click.argument("source_name", type=str)
@click.option(
    "--output-file",
    help="Output file path (defaults to catalog/{source_name}/generated/airbyte-catalog.json)",
)
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
@click.argument("project_name", type=str)
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

    import yaml

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


# Project Auto-Generation
@main.command()
@click.argument("source_name", type=str)
@click.option("--project-name", type=str, default="fivetran-interop")
@click.option("--no-airbyte-catalog", is_flag=True)
@click.option("--no-transforms", is_flag=True)
@click.option("--no-dbt-project", is_flag=True)
def generate_project(
    source_name: str,
    project_name: str,
    *,
    no_airbyte_catalog: bool | None = None,
    no_transforms: bool | None = None,
    no_dbt_project: bool | None = None,
) -> None:
    """Generate a project scaffold for a new connector, or update an existing one."""

    def _if_none(input: Any, default: bool | None, /) -> Any:
        return input if input is not None else default

    no_airbyte_catalog = _if_none(no_airbyte_catalog, False)
    no_transforms = _if_none(no_transforms, False)
    no_dbt_project = _if_none(no_dbt_project, False)

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
        generate_transform_scaffold.callback(source_name, project_name)
        console.print(f"Generated transforms for {source_name}")

    # Generate dbt project
    if not no_dbt_project:
        console.print(f"Generating dbt project for {source_name}...")
        generate_dbt_project.callback(source_name, project_name)
        console.print(f"Generated dbt project for {source_name}")


if __name__ == "__main__":
    main()
