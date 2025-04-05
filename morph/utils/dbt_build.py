"""DBT build module.

This module contains functions to generate a dbt project from mapping files.
"""

from __future__ import annotations

import shutil
import subprocess

from rich.console import Console

from morph import resources
from morph.utils.dbt.dbt_source_files import (
    generate_dbt_sources_yml_from_airbyte_catalog,
)
from morph.utils.dbt.mapping_to_dbt_models import generate_dbt_package

console = Console()


def build_dbt_project(
    source_name: str,
    project_name: str,
    *,
    run_tests: bool = True,
) -> None:
    """Generate a dbt project from mapping files.

    This command generates a dbt project from mapping files. The mapping files
    should be in YAML format and located in the mapping directory.

    SOURCE_NAME: Name of the source (e.g., 'hubspot')
    PROJECT_NAME: Name of the project (e.g., 'fivetran-interop')
    """
    _ = project_name  # Not used currently

    catalog_dir = resources.get_catalog_root_dir()
    if source_name is None:
        raise ValueError("Error: --source-name is required")

    catalog_file = resources.get_generated_catalog_path(
        source_name,
        project_name,
    )

    # Validate input paths exist
    if not catalog_dir.exists():
        raise ValueError(f"Error: {catalog_dir} does not exist")

    if not catalog_file.exists():
        raise ValueError(f"Error: {catalog_file} does not exist")

    dbt_project_dir = resources.get_generated_dbt_project_dir(
        source_name=source_name,
        project_name=project_name,
    )
    # Generate dbt package
    try:
        # Generate dbt models from mapping files
        generate_dbt_package(
            source_name=source_name,
            project_name=project_name,
        )

        # Get sources.yml path from generated directory
        generated_sources_path = resources.get_generated_source_yml_path(
            source_name=source_name,
            project_name=project_name,
        )
        if not generated_sources_path.exists():
            # Only generate sources.yml if it doesn't exist.
            # Otherwise, we'll copy the existing sources.yml into the generated directory.
            generate_dbt_sources_yml_from_airbyte_catalog(
                source_name=source_name,
                project_name=project_name,
                catalog_file=catalog_file,
                output_file=generated_sources_path,
            )

        # Get sources.yml path in dbt project models directory
        new_sources_path = (
            resources.get_generated_dbt_project_models_dir(
                source_name,
                project_name,
            )
            / "src_airbyte_raw.yml"
        )

        # Ensure parent directory exists
        new_sources_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert dict to YAML string before writing
        #
        # new_sources_path.write_text(yaml.dump(sources_yml, default_flow_style=False, sort_keys=False))

        # Copy sources.yml into the generated directory
        shutil.copy(generated_sources_path, new_sources_path)

        console.print(f"Generated dbt project at {dbt_project_dir}")
    except Exception as e:
        console.print(f"Error generating dbt project: {e}", style="bold red")

    if run_tests:
        console.print("Running dbt tests...")
        result = subprocess.run(
            ["uv", "run", "dbt", "deps"],
            cwd=dbt_project_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Error running dbt deps: {result.stderr}",
            )

        result = subprocess.run(
            ["uv", "run", "dbt", "run", "--profiles-dir", "profiles"],
            cwd=dbt_project_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode == 0:
            print(result.stdout.replace("\\n", "\n"))
            console.print("DBT tests completed.")
        else:
            print(f"Error running dbt tests: {result.stderr}")
            print(f"Command output: {result.stdout}")

        console.print("DBT tests completed.")
