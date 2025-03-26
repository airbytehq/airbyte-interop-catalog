"""Command-line interface for Morph."""

from pathlib import Path

import click
import yaml
from rich.console import Console

from morph.utils.dbt_source_files import (
    generate_dbt_sources_yml_from_airbyte_catalog,
    generate_header_comment,
    parse_airbyte_catalog_to_dbt_sources_format,
)

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

        sources_yml = parse_airbyte_catalog_to_dbt_sources_format(
            schema_path,
            source_name,
            database,
            schema,
        )
    else:
        schema_files = []
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

        sources_yml = generate_dbt_sources_yml_from_airbyte_catalog(
            schema_files,
            source_name,
            database,
            schema,
        )

    # Generate header comment
    args = type(
        "Args",
        (),
        {
            "schema_path": schema_path,
            "catalog": catalog,
            "source_name": source_name,
            "database": database,
            "schema": schema,
            "output": output,
        },
    )()
    header_comment = generate_header_comment(args)

    # Write to output file with header comment
    output_path = Path(output)
    content = header_comment + yaml.dump(sources_yml, default_flow_style=False, sort_keys=False)
    output_path.write_text(content)

    console.print(f"Generated dbt sources.yml at {output}")


if __name__ == "__main__":
    main()
