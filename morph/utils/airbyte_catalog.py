"""
Utilities for generating Airbyte catalog files.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import airbyte as ab
from airbyte.secrets import GoogleGSMSecretManager

from morph import resources
from morph.utils.dbt.dbt_source_files import update_generated_dbt_sources_yml_from_airbyte_catalog

AIRBYTE_INTERNAL_GCP_PROJECT = "dataline-integration-testing"
USE_DOCKER_IMAGE = True


def get_connector_id(
    source_name: str,
) -> str:
    """Get the connector ID for an Airbyte source.

    Args:
        source_name: Name of the source. (e.g. "hubspot" or "facebook_marketing")

    Returns:
        The connector ID (e.g. "source-hubspot" or "source-facebook-marketing")
    """
    if source_name.startswith("source-"):
        return source_name

    return f"source-{source_name.replace('_', '-')}"


def get_config(
    source_name: str,
    secret_name: str | None = None,
) -> dict[str, Any]:
    """Get the config for an Airbyte source.

    Args:
        source_name: Name of the source
        secret_name: Optional name of the specific secret to use

    Returns:
        The source configuration as a dictionary
    """

    connector_name = get_connector_id(source_name)
    secret_manager = GoogleGSMSecretManager(
        project=AIRBYTE_INTERNAL_GCP_PROJECT,
        credentials_json=ab.get_secret("GCP_GSM_CREDENTIALS"),
    )
    if secret_name:
        return secret_manager.get_secret(
            secret_name=secret_name,
        ).parse_json()

    secret = next(
        iter(
            secret_manager.fetch_connector_secrets(
                connector_name,
            ),
        ),
        None,
    )
    if secret is None:
        raise ValueError(f"No secrets found for {connector_name}")
    return secret.parse_json()


def get_source(
    source_name: str,
    streams: list[str] | str = "*",
) -> ab.Source:
    """Get an Airbyte source instance.

    Args:
        source_name: Name of the source
        streams: List of streams to include or "*" for all

    Returns:
        An Airbyte source instance
    """

    # Hubspot's CDK ref is not properly pinned in its pyproject.toml (needs airbyte-cdk==2.4.0)
    # AND it needs the old version of pendulum so it isn't compatible with Python 3.12
    return ab.get_source(
        get_connector_id(source_name),
        config=get_config(source_name),
        docker_image=USE_DOCKER_IMAGE,
        streams=streams,
    )


def write_catalog_file(
    source_name: str,
    output_file_path: Path | None = None,
) -> Path:
    """Write the Airbyte catalog to a file.

    The default file path will be used unless a custom location is specified.

    Args:
        source_name: Name of the source
        output_file_path: Path to the output file
    """
    output_file_path = output_file_path or resources.get_generated_catalog_path(
        source_name=source_name,
    )
    connector_name = get_connector_id(source_name)
    source = get_source(connector_name, streams="*")
    source.check()
    catalog = source.discovered_catalog

    # Ensure parent directories exist
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_file_path.write_text(catalog.model_dump_json(indent=2))

    update_generated_dbt_sources_yml_from_airbyte_catalog(
        source_name=source_name,
    )

    return output_file_path
