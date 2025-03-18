"""Command-line interface for Morph."""

import argparse
import os
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
@click.option("--output-dir", help="Output directory for generated dbt project (defaults to {catalog_dir}/generated)")
@click.option("--mapping-dir", help="Directory containing mapping files (defaults to {catalog_dir}/transforms)")
def generate_dbt_project(
    catalog_dir: str,
    output_dir: str | None = None,
    mapping_dir: str | None = None,
) -> None:
    """Generate a dbt project from mapping files.
    
    This command generates a complete dbt project in the specified output directory,
    including models for each transform defined in the mapping files.
    
    CATALOG_DIR: Path to the catalog directory (e.g., 'catalog/hubspot')
    """
    catalog_path = Path(catalog_dir)
    
    # Validate input path exists
    if not catalog_path.exists():
        console.print(f"Error: {catalog_dir} does not exist")
        return
    
    # Generate dbt package
    try:
        generate_dbt_package(catalog_dir, output_dir, mapping_dir)
        
        # Determine the actual output directory
        actual_output_dir = output_dir if output_dir else str(catalog_path / "generated")
        
        # Create profiles.yml with duckdb and motherduck configurations
        profiles_dir = os.path.join(actual_output_dir, "profiles")
        os.makedirs(profiles_dir, exist_ok=True)
        
        profiles_content = """
default:
  target: duckdb
  outputs:
    duckdb:
      type: duckdb
      path: target/dbt.duckdb
      extensions:
        - httpfs
        - parquet
    motherduck:
      type: duckdb
      path: md:
      extensions:
        - httpfs
        - parquet
      settings:
        motherduck_token: ${MOTHERDUCK_TOKEN}
"""
        
        with open(os.path.join(profiles_dir, "profiles.yml"), "w") as f:
            f.write(profiles_content)
        
        console.print(f"Generated dbt project at {actual_output_dir}")
        console.print(f"To use the generated dbt project:")
        console.print(f"  1. cd {actual_output_dir}")
        console.print(f"  2. dbt deps")
        console.print(f"  3. dbt run")
    except Exception as e:
        console.print(f"Error generating dbt project: {e}", style="bold red")


if __name__ == "__main__":
    main()
