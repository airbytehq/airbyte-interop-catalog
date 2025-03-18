"""Command-line interface for Morph."""

import argparse
from pathlib import Path

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
        console.print(f"Error: {schema_path} does not exist")
        return

    # Process based on input type
    if catalog:
        if not schema_path_obj.is_file() or not schema_path_obj.name.endswith(".json"):
            console.print(f"Error: {schema_path} is not a valid JSON file")
            return

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
@click.argument("catalog_dir", type=click.Path(exists=True))
@click.argument("catalog_file", type=click.Path(exists=True))
@click.option(
    "--output-dir",
    help="Output directory for generated dbt project (defaults to {catalog_dir}/generated)",
)
@click.option(
    "--mapping-dir",
    help="Directory containing mapping files (defaults to {catalog_dir}/transforms)",
)
@click.option(
    "--source-name",
    default=None,
    help="Name for the dbt source (defaults to catalog directory name)",
)
def generate_dbt_project(
    catalog_dir: str,
    catalog_file: str,
    output_dir: str | None = None,
    mapping_dir: str | None = None,
    source_name: str | None = None,
) -> None:
    """Generate a dbt project from mapping files and catalog.json.

    This command generates a complete dbt project in the specified output directory,
    including models for each transform defined in the mapping files and a sources.yml
    file generated from the catalog.json file.

    CATALOG_DIR: Path to the catalog directory (e.g., 'catalog/hubspot')
    CATALOG_FILE: Path to the Airbyte catalog.json file
    """
    catalog_path = Path(catalog_dir)

    # Validate input paths exist
    if not catalog_path.exists():
        console.print(f"Error: {catalog_dir} does not exist")
        return

    if not Path(catalog_file).exists():
        console.print(f"Error: {catalog_file} does not exist")
        return

    # Set default source name if not provided
    if not source_name:
        source_name = catalog_path.name

    # Generate dbt package
    try:
        # Generate dbt models from mapping files
        generate_dbt_package(catalog_dir, output_dir, mapping_dir)

        # Determine the actual output directory
        actual_output_dir = Path(output_dir) if output_dir else catalog_path / "generated"

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
        console.print(f"Error generating dbt project: {e}", style="bold red")


if __name__ == "__main__":
    main()
