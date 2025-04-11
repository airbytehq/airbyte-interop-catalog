"""
Utilities for visualizing DBML files using Docker-based dbml-renderer.

This module provides functionality to render DBML files to SVG images
using the dbml-renderer tool in a Docker container.
"""

import shutil
import subprocess
from pathlib import Path
from typing import Optional

from rich.console import Console

from morph import resources

console = Console()


def check_docker_availability() -> bool:
    """Check if Docker CLI is available.

    Returns:
        bool: True if Docker is available, False otherwise.
    """
    return shutil.which("docker") is not None


def render_dbml_to_svg(
    dbml_file_path: Path,
    output_file_path: Optional[Path] = None,
) -> bool:
    """Render a DBML file to SVG using Docker-based dbml-renderer.

    Args:
        dbml_file_path: Path to the DBML file to render
        output_file_path: Path where the SVG file should be written.
            If not provided, will use the same path as the DBML file with .svg extension.

    Returns:
        bool: True if rendering was successful, False otherwise.

    Raises:
        RuntimeError: If Docker is not available.
    """
    if not check_docker_availability():
        raise RuntimeError(
            "Docker is not available. Please install Docker to use DBML visualization."
        )

    if not dbml_file_path.exists():
        console.print(f"DBML file {dbml_file_path} does not exist, skipping visualization")
        return False

    if output_file_path is None:
        output_file_path = dbml_file_path.with_suffix(".svg")

    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    abs_dbml_path = dbml_file_path.absolute()
    abs_output_path = output_file_path.absolute()
    
    mount_dir = abs_dbml_path.parent
    
    rel_dbml_file = abs_dbml_path.name
    rel_output_file = abs_output_path.name if abs_output_path.parent == mount_dir else abs_output_path

    try:
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{mount_dir}:/data",
            "node:20-alpine", "sh", "-c",
            f"npm install -g @softwaretechnik/dbml-renderer && dbml-renderer -i /data/{rel_dbml_file} -o /data/{rel_output_file}"
        ]
        
        console.print(f"Rendering DBML file {dbml_file_path} to {output_file_path}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode != 0:
            console.print(f"Error rendering DBML file: {result.stderr}")
            return False
            
        console.print(f"Successfully rendered DBML file to {output_file_path}")
        return True
    except Exception as e:
        console.print(f"Error rendering DBML file: {str(e)}")
        return False


def visualize_source_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
) -> bool:
    """Visualize the source DBML file for a source.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Returns:
        bool: True if visualization was successful, False otherwise.
    """
    dbml_path = resources.get_source_dbml_path(
        source_name=source_name,
        project_name=project_name,
    )
    
    return render_dbml_to_svg(dbml_path)


def visualize_target_dbml(
    source_name: str,
    project_name: str = resources.DEFAULT_PROJECT_NAME,
) -> bool:
    """Visualize the target DBML file for a source.

    Args:
        source_name: Name of the source
        project_name: Name of the project

    Returns:
        bool: True if visualization was successful, False otherwise.
    """
    dbml_path = resources.get_target_dbml_path(
        source_name=source_name,
        project_name=project_name,
    )
    
    return render_dbml_to_svg(dbml_path)
