"""
Utilities for visualizing DBML files using Docker-based dbml-renderer.

This module provides functionality to render DBML files to SVG images
using the dbml-renderer tool in a Docker container.
"""

from pathlib import Path

from rich.console import Console

from morph import resources
from morph.utils.docker_utils import run_docker_command

console = Console()


def render_dbml_to_svg(
    dbml_file_path: Path,
    output_file_path: Path | None = None,
) -> None:
    """Render a DBML file to SVG using Docker-based dbml-renderer.

    Args:
        dbml_file_path: Path to the DBML file to render
        output_file_path: Path where the SVG file should be written.
            If not provided, will use the same path as the DBML file with .svg extension.

    Raises:
        RuntimeError: If Docker is not available.
        FileNotFoundError: If the DBML file does not exist.
        subprocess.CalledProcessError: If the Docker command fails.
        Exception: For any other errors during rendering.
    """
    if not dbml_file_path.exists():
        raise FileNotFoundError(f"DBML file {dbml_file_path} does not exist")

    if output_file_path is None:
        output_file_path = dbml_file_path.with_name(f"{dbml_file_path.stem}.svg")

    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    abs_dbml_path = dbml_file_path.absolute()
    abs_output_path = output_file_path.absolute()

    mount_dir = abs_dbml_path.parent

    rel_dbml_file = abs_dbml_path.name
    rel_output_file = (
        abs_output_path.name if abs_output_path.parent == mount_dir else abs_output_path
    )

    try:
        console.print(f"Rendering DBML file {dbml_file_path} to {output_file_path}")

        command = f"npm install -g @softwaretechnik/dbml-renderer && dbml-renderer -i /data/{rel_dbml_file} -o /data/{rel_output_file}"
        run_docker_command(
            image="node:20-alpine",
            command=command,
            mount_dir=mount_dir,
        )

        console.print(f"Successfully rendered DBML file to {output_file_path}")
    except Exception as e:
        console.print(f"Error rendering DBML file: {e!s}")
        raise


def visualize_source_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
) -> None:
    """Visualize the source DBML file for a source.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Raises:
        FileNotFoundError: If the DBML file does not exist.
        RuntimeError: If Docker is not available.
        subprocess.CalledProcessError: If the Docker command fails.
        Exception: For any other errors during rendering.
    """
    dbml_path = resources.get_source_dbml_path(
        source_name=source_name,
        project_name=project_name,
    )

    render_dbml_to_svg(dbml_path)


def visualize_target_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
) -> None:
    """Visualize the target DBML file for a source.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Raises:
        FileNotFoundError: If the DBML file does not exist.
        RuntimeError: If Docker is not available.
        subprocess.CalledProcessError: If the Docker command fails.
        Exception: For any other errors during rendering.
    """
    dbml_path = resources.get_target_dbml_path(
        source_name=source_name,
        project_name=project_name,
    )

    render_dbml_to_svg(dbml_path)
