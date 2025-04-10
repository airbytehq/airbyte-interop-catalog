"""Utility functions for getting resource paths.

This module provides utility functions for getting resource paths.

Most functions take a `source_name` and optional `project_name` argument, which are used to
construct the path to the resource. If `project_name` is not provided, it defaults to
`fivetran-interop`.
"""

from pathlib import Path
from typing import Any, overload

from morph.constants import DEFAULT_PROJECT_NAME
from morph.utils import text_utils


def get_catalog_root_dir() -> Path:
    """Assume we are running from the root of the morph repo."""
    return Path("catalog")


def get_generated_dir_root(
    source_name: str,
) -> Path:
    """Assume we are running from the root of the morph repo."""
    return get_catalog_root_dir() / source_name / Path("generated")


def get_lock_file_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the lock file."""
    return get_catalog_root_dir() / source_name / f"{project_name}.morph-lock.toml"


def get_generated_catalog_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the generated Airbyte catalog file."""
    _ = project_name  # Unused for now
    return (
        get_generated_dir_root(
            source_name=source_name,
        )
        / "airbyte-catalog.json"
    )


def get_generated_dbt_project_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the generated dbt project.yml file."""
    _ = project_name  # Unused for now
    return get_generated_dir_root(source_name=source_name) / "dbt_project"


def get_generated_dbt_project_models_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the generated dbt project models directory."""
    _ = project_name  # Unused for now
    return get_generated_dbt_project_dir(source_name, project_name) / "models"


def get_generated_source_yml_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the generated dbt sources.yml file."""
    _ = project_name  # Unused for now
    return (
        get_generated_dir_root(
            source_name=source_name,
        )
        / f"src_airbyte_{source_name}.yml"
    )


def get_erd_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the ERD directory for a source."""
    _ = project_name  # Unused for now
    return (
        get_generated_dir_root(
            source_name=source_name,
        )
        / "erd"
    )


def get_source_dbml_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the source DBML file for a source."""
    return get_erd_dir(source_name=source_name, project_name=project_name) / "source.dbml"


def get_target_dbml_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    """Get the path to the target DBML file for a source."""
    return get_erd_dir(source_name=source_name, project_name=project_name) / "target.dbml"


def get_requirements_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    return get_catalog_root_dir() / source_name / "requirements" / project_name


def get_dbt_sources_requirements_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    return get_requirements_dir(source_name, project_name) / "src_dbt_requirements.yml"


def get_src_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    return get_catalog_root_dir() / source_name / "src" / project_name


def get_config_file_path(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    return get_src_dir(source_name, project_name) / "config.yml"


def get_transforms_dir(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> Path:
    return get_src_dir(source_name, project_name) / "transforms"


def get_transforms_files(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> list[Path]:
    """Get the path to the transform files."""
    transforms_dir = get_transforms_dir(source_name, project_name)
    return list(transforms_dir.glob("*.yml"))


def get_transform_file(
    source_name: str,
    *,
    project_name: str = DEFAULT_PROJECT_NAME,
    transform_name: str,
) -> Path:
    return get_transforms_dir(source_name, project_name) / f"{transform_name}.yml"


@overload
def get_source_config(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
) -> dict[str, Any]: ...
@overload
def get_source_config(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    key: str | None = None,
    default: Any = None,
) -> Any: ...


def get_source_config(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    key: str | None = None,
    default: Any = None,
) -> dict[str, Any] | Any:
    """Load configuration file and extract target tables.

    Args:
        source_name: Name of the source
        project_name: Name of the project
        key: Key to extract from the config

    Returns:
        Config dictionary.
    """
    config_file: Path = get_config_file_path(
        source_name=source_name,
        project_name=project_name,
    )

    if not config_file.is_file():
        raise ValueError(f"Error: Config file {config_file} does not exist")

    config = text_utils.load_yaml_file(config_file)

    if not key:
        return config

    return config.get(key, default)
