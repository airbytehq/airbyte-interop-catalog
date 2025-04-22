"""
Utilities for working with Docker.

This module provides functionality for checking Docker availability
and running Docker commands.
"""

import shutil
import subprocess
from pathlib import Path

from rich.console import Console

console = Console()


def check_docker_availability() -> bool:
    """Check if Docker CLI is available.

    Returns:
        bool: True if Docker is available, False otherwise.
    """
    return shutil.which("docker") is not None


def run_docker_command(
    image: str,
    command: str,
    mount_dir: Path,
    environment_vars: dict[str, str] | None = None,
) -> None:
    """Run a command in a Docker container.

    Args:
        image: Docker image to use
        command: Command to run in the container
        mount_dir: Directory to mount in the container
        environment_vars: Environment variables to pass to the container

    Raises:
        RuntimeError: If Docker is not available
        subprocess.CalledProcessError: If the Docker command fails
    """
    if not check_docker_availability():
        raise RuntimeError("Docker is not available. Please install Docker to use this feature.")

    cmd = ["docker", "run", "--rm", "-v", f"{mount_dir.absolute()}:/data"]

    if environment_vars:
        for key, value in environment_vars.items():
            cmd.extend(["-e", f"{key}={value}"])

    cmd.extend([image, "sh", "-c", command])

    console.print(f"Running Docker command with image {image}")
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    console.print("Docker command completed successfully")
