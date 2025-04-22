"""
Utilities for generating DBML (Database Markup Language) files from DbtSourceFile objects.

DBML files can be used to visualize database schemas as Entity Relationship Diagrams (ERDs).
"""

from pathlib import Path

from pydbml import Database
from pydbml.classes import Column, Table
from pydbml.renderer.dbml.default import DefaultDBMLRenderer
from rich.console import Console

from morph import resources
from morph.models import DbtSourceFile
from morph.utils.dbml.dbml_visualizer import visualize_source_dbml, visualize_target_dbml

console = Console()


def generate_dbml_from_dbt_source_file(
    dbt_source_file: DbtSourceFile,
    output_file: Path,
) -> None:
    """Generate a DBML file from a DbtSourceFile.

    Args:
        dbt_source_file: DbtSourceFile object to convert to DBML
        output_file: Path where the DBML file should be written
    """
    database = Database()

    for source_table in dbt_source_file.source_tables:
        dbml_table = Table(source_table.name)

        for column in source_table.columns:
            column_obj = Column(
                name=column.name,
                type=column.data_type or "unknown",  # type: ignore # Leave None if not provided
                note=column.description if column.description else None,
            )

            dbml_table.add_column(column_obj)

        database.add(dbml_table)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    output_file.write_text(DefaultDBMLRenderer.render_db(database))

    console.print(f"Generated DBML file at {output_file}")


def generate_source_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
    output_file: Path | None = None,
    visualize: bool = True,
) -> None:
    """Generate a DBML file for the Airbyte source.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        output_file: Optional custom output path
        visualize: Whether to visualize the DBML file after generation
    """
    source_yml_path = resources.get_generated_source_yml_path(
        source_name=source_name,
        project_name=project_name,
    )

    if not source_yml_path.exists():
        console.print(
            f"Source file {source_yml_path} does not exist, skipping source DBML generation",
        )
        return

    dbt_source_file = DbtSourceFile.from_file(source_yml_path)

    if output_file is None:
        output_file = resources.get_source_dbml_path(
            source_name=source_name,
            project_name=project_name,
        )

    generate_dbml_from_dbt_source_file(
        dbt_source_file=dbt_source_file,
        output_file=output_file,
    )

    if visualize:
        try:
            visualize_source_dbml(source_name=source_name, project_name=project_name)
        except FileNotFoundError:
            console.print("DBML file not found, skipping visualization")
        except RuntimeError as e:
            console.print(f"Docker not available, skipping visualization: {e!s}")
        except Exception as e:
            console.print(f"Error visualizing DBML file: {e!s}")


def generate_target_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
    output_file: Path | None = None,
    visualize: bool = True,
) -> None:
    """Generate a DBML file for the target schema.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        output_file: Optional custom output path
        visualize: Whether to visualize the DBML file after generation
    """
    target_schema_path = resources.get_dbt_sources_requirements_path(
        source_name=source_name,
        project_name=project_name,
    )

    if not target_schema_path.exists():
        console.print(
            f"Target schema file {target_schema_path} does not exist, skipping target DBML generation",
        )
        return

    dbt_source_file = DbtSourceFile.from_file(target_schema_path)

    if output_file is None:
        output_file = resources.get_target_dbml_path(
            source_name=source_name,
            project_name=project_name,
        )

    generate_dbml_from_dbt_source_file(
        dbt_source_file=dbt_source_file,
        output_file=output_file,
    )

    if visualize:
        try:
            visualize_target_dbml(source_name=source_name, project_name=project_name)
        except FileNotFoundError:
            console.print("DBML file not found, skipping visualization")
        except RuntimeError as e:
            console.print(f"Docker not available, skipping visualization: {e!s}")
        except Exception as e:
            console.print(f"Error visualizing DBML file: {e!s}")
