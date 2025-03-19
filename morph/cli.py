"""Command-line interface for Morph."""

from pathlib import Path

import click
import yaml
from rich.console import Console

from morph.utils.json_to_dbt_sources import (
    generate_header_comment,
    get_dbt_sources_yml,
)
from morph.utils.mapping_to_dbt_models import generate_dbt_package

console = Console()


@click.group()
@click.version_option()
def cli() -> None:
    """Morph: A Python library for data transformation."""
    pass


@cli.command("json-to-dbt")
@click.option("--catalog_path", type=click.Path(exists=True))
@click.option("--source-name", default="default_source", help="Name for the dbt source")
@click.option("--database", help="Database name for the source")
@click.option("--schema", help="Schema name for the source")
@click.option(
    "--output",
    default="sources.yml",
    help="Output file path",
    type=click.Path(exists=False),
)
def json_to_dbt(
    catalog_path: Path,
    *,
    source_name: str,
    database: str | None = None,
    schema: str | None = None,
    output: Path,
) -> None:
    """Convert JSON schema files or Airbyte catalog to dbt sources.yml format."""
    # Validate input path exists
    if not catalog_path.exists():
        console.print(f"Error: {catalog_path} does not exist")
        return

    # Process based on input type
    if not catalog_path.is_file() or not catalog_path.name.endswith(".json"):
        console.print(f"Error: {catalog_path} is not a valid JSON file")
        return

    header_comment: str = generate_header_comment()
    sources_yml_str: str = get_dbt_sources_yml(
        catalog_file=catalog_path,
        source_name=source_name,
        database=database,
        schema=schema,
        preamble=header_comment,
    )

    output_path = Path(output)
    output_path.write_text(yaml.dump(sources_yml_str, default_flow_style=False, sort_keys=False))
    console.print(f"Generated dbt sources.yml at {output}")


@cli.command()
@click.argument("catalog_file", type=click.Path(exists=True))
@click.option(
    "--output-dir",
    help="Output directory for generated dbt project (defaults to {catalog_dir}/generated)",
)
@click.option("--source-name", default="default_source", help="Name for the dbt source")
@click.option("--database", help="Database name for the source")
@click.option("--schema", help="Schema name for the source")
@click.option(
    "--output",
    default="sources.yml",
    help="Output file path",
    type=click.Path(exists=False),
)
def catalog_json_to_dbt_sources(
    catalog_file: Path,
    *,
    source_name: str,
    database: str | None,
    schema: str | None,
    output: Path,
) -> None:
    """Convert JSON schema files or Airbyte catalog to dbt sources.yml format."""

    # Validate input path exists
    if not catalog_file.exists():
        console.print(f"Error: {catalog_file} does not exist")
        return

    if not catalog_file.is_file() or not catalog_file.name.endswith(".json"):
        console.print(f"Error: {catalog_file} is not a valid JSON file")
        return

    sources_yml: str = get_dbt_sources_yml(
        catalog_file=catalog_file,
        source_name=source_name,
        database=database,
        schema=schema,
    )

    output.write_text(sources_yml)
    console.print(f"Generated dbt sources.yml at {output}")


@cli.command()
@click.argument("catalog_dir", type=click.Path(exists=True))
@click.argument("catalog_file", type=click.Path(exists=True))
@click.option(
    "--output-dir",
    help="Output directory for generated dbt project (defaults to {catalog_dir}/generated)",
    type=click.Path(exists=False),
)
@click.option(
    "--mapping-dir",
    help="Directory containing mapping files (defaults to {catalog_dir}/transforms)",
    type=click.Path(exists=True),
)
@click.option(
    "--source-name",
    default=None,
    help="Name for the dbt source (defaults to catalog directory name)",
)
def generate_dbt_project(
    catalog_dir: Path,
    catalog_file: Path,
    output_dir: Path | None = None,
    mapping_dir: Path | None = None,
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
        generate_dbt_package(
            catalog_dir=catalog_dir,
            output_dir=output_dir,
            mapping_dir=mapping_dir,
        )

        # Determine the actual output directory
        actual_output_dir = Path(output_dir) if output_dir else catalog_path / "generated"

        # Generate sources.yml from catalog.json
        sources_yml: str = get_dbt_sources_yml(
            catalog_file=catalog_file,
            source_name=source_name,
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
    cli()
