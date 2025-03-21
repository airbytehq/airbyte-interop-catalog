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
    help="Directory containing mapping files.",
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


@main.command()
@click.argument("source_name", type=str)
@click.argument("project_name", type=str)
@click.option(
    "--output-file",
    help="Output file path (defaults to catalog/{source_name}/generated/airbyte-catalog.json)",
)
def create_airbyte_catalog(
    source_name: str,
    _project_name: str,
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
        console.print(f"Error: Config file {config_file} does not exist", style="bold red")
        return

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


    # Set default paths if not provided
    config_file = f"catalog/{source_name}/src/{project_name}/config.yml"
    if not output_dir:
        output_dir = f"catalog/{source_name}/src/{project_name}/transforms"
    
    # Set path for local target schema file
    requirements_dir = f"catalog/{source_name}/requirements/{project_name}"
    Path(requirements_dir).mkdir(parents=True, exist_ok=True)

    # Load config and target schema
    config, target_tables = _load_config(config_file)
    if not config or not target_tables:
        return
    
    target_schema = _get_target_schema(config, requirements_dir)
    if not target_schema:
        return

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Process each target table
    created_files = _generate_mapping_files(
        source_name, project_name, target_tables, target_schema, output_path,
    )

    _report_results(created_files)


def _load_config(config_file):
    """Load configuration file and extract target tables."""
    from pathlib import Path

    import yaml
    
    config_path = Path(config_file)
    if not config_path.exists():
        console.print(f"Error: Config file {config_file} does not exist", style="bold red")
        return None, None

    config = yaml.safe_load(config_path.read_text())
    target_tables = config.get("target_tables", [])
    if not target_tables:
        console.print(f"No target tables defined in {config_file}", style="bold yellow")
        return config, None
    
    return config, target_tables


def _get_target_schema(config, requirements_dir):
    """Download or load target schema file."""
    from pathlib import Path

    import requests
    import yaml
    
    # Get target schema URL
    target_schema_url = config.get("target_dbt_schema")
    if not target_schema_url:
        console.print("Error: target_dbt_schema not defined in config.yml", style="bold red")
        return None
    
    # Determine target schema file name from URL
    target_schema_filename = target_schema_url.split("/")[-1]
    local_schema_path = Path(requirements_dir) / target_schema_filename
    
    # Download target schema if not already downloaded
    if not local_schema_path.exists():
        console.print(f"Downloading target schema to {local_schema_path}...")
        try:
            response = requests.get(target_schema_url)
            response.raise_for_status()
            local_schema_path.write_text(response.text)
            console.print(f"Downloaded target schema to {local_schema_path}", style="green")
            return yaml.safe_load(response.text)
        except Exception as e:
            console.print(f"Error downloading target schema: {e}", style="bold red")
            return None
    else:
        console.print(f"Using existing target schema file: {local_schema_path}")
        return yaml.safe_load(local_schema_path.read_text())


def _find_table_schema(target_schema, table_name):
    """Find table schema in target schema."""
    for source in target_schema.get("sources", []):
        for table in source.get("tables", []):
            if table.get("name") == table_name:
                return table
    return None


def _create_mapping_structure(source_name, project_name, table_name, table_schema):
    """Create mapping structure for a table."""
    return {
        "domain": f"{source_name}.{project_name}",
        "transforms": [
            {
                "display_name": f"{table_schema.get('description', table_name)}",
                "id": table_name,
                "from": [
                    {f"{table_name}s": f"airbyte_raw_{source_name}.{table_name}s"},
                ],
                "fields": {},
            },
        ],
    }


def _add_fields_to_mapping(mapping, table_schema):
    """Add fields with MISSING expressions to mapping."""
    fields_dict = mapping["transforms"][0]["fields"]
    for column in table_schema.get("columns", []):
        field_name = column.get("name")
        description = column.get("description", "")
        
        # Skip missing field names
        if not field_name:
            continue
            
        fields_dict[field_name] = {
            "expression": "MISSING",
            "description": description,
        }
    return mapping


def _generate_mapping_files(source_name, project_name, target_tables, target_schema, output_path):
    """Generate mapping files for target tables."""

    import yaml
    
    created_files = []
    for table_name in target_tables:
        # Check if mapping file already exists
        mapping_file = output_path / f"{table_name}.yml"
        if mapping_file.exists():
            console.print(f"Skipping {table_name}: Mapping file already exists", style="blue")
            continue

        # Find table schema in target_schema
        table_schema = _find_table_schema(target_schema, table_name)
        if not table_schema:
            console.print(f"Warning: Schema not found for table {table_name}", style="yellow")
            continue

        # Create mapping structure
        mapping = _create_mapping_structure(source_name, project_name, table_name, table_schema)
        
        # Add fields with MISSING expressions
        mapping = _add_fields_to_mapping(mapping, table_schema)

        # Write mapping file
        with mapping_file.open("w") as f:
            yaml.dump(mapping, f, default_flow_style=False, sort_keys=False)
        
        created_files.append(str(mapping_file))
        console.print(f"Created mapping file for {table_name}", style="green")
    
    return created_files


def _report_results(created_files):
    """Report results of file generation."""
    if created_files:
        console.print(f"Generated {len(created_files)} mapping files:", style="bold green")
        for file in created_files:
            console.print(f"  - {file}")
    else:
        console.print("No new mapping files generated.", style="bold blue")


if __name__ == "__main__":
    main()
