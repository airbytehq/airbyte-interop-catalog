"""
Utilities for generating Airbyte catalog files.
"""

from pathlib import Path

import airbyte as ab
from airbyte.secrets import GoogleGSMSecretManager

AIRBYTE_INTERNAL_GCP_PROJECT = "dataline-integration-testing"


def get_config(source_name: str, secret_name: str | None = None) -> dict:
    """Get the config for an Airbyte source.

    Args:
        source_name: Name of the source
        secret_name: Optional name of the specific secret to use

    Returns:
        The source configuration as a dictionary
    """
    connector_name = f"source-{source_name}"
    secret_manager = GoogleGSMSecretManager(
        project=AIRBYTE_INTERNAL_GCP_PROJECT,
        credentials_json=ab.get_secret("GCP_GSM_CREDENTIALS"),
    )
    if secret_name:
        return secret_manager.get_secret(secret_name).parse_json()

    secret = next(iter(secret_manager.fetch_connector_secrets(connector_name)), None)
    if secret is None:
        raise ValueError(f"No secrets found for {connector_name}")
    return secret.parse_json()


def get_source(source_name: str, streams: list[str] | str = "*") -> ab.Source:
    """Get an Airbyte source instance.

    Args:
        source_name: Name of the source
        streams: List of streams to include or "*" for all

    Returns:
        An Airbyte source instance
    """
    # Hubspot's CDK ref is not properly pinned in its pyproject.toml (needs airbyte-cdk==2.4.0)
    # AND it needs the old version of pendulum so it isn't compatible with Python 3.12
    docker_image = True if source_name == "hubspot" else None

    return ab.get_source(
        f"source-{source_name}",
        config=get_config(source_name),
        docker_image=docker_image,
        streams=streams,
    )


def write_catalog_file(source_name: str, output_file_path: Path) -> None:
    """Write the Airbyte catalog to a file.

    Args:
        source_name: Name of the source
        output_file_path: Path to the output file
    """
    source = get_source(source_name, streams="*")
    source.check()
    catalog = source.discovered_catalog
    
    # Ensure parent directories exist
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_file_path.write_text(catalog.model_dump_json(indent=2))
