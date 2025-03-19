# Usage:
#   uv script run scripts/create_hubspot_data.py
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "airbyte",  # PyAirbyte
# ]
# ///

import airbyte as ab
from airbyte.secrets import GoogleGSMSecretManager

AIRBYTE_INTERNAL_GCP_PROJECT = "dataline-integration-testing"

SOURCE_NAME = "hubspot"
PATH_TO_DUCKDB_DB = f".data/{SOURCE_NAME}.duckdb"
STREAMS = [
    "companies",
    "tickets",
]


def get_config(source_name="hubspot", secret_name: str | None = None) -> None:
    connector_name = f"source-{source_name}"
    secret_manager = GoogleGSMSecretManager(
        project=AIRBYTE_INTERNAL_GCP_PROJECT,
        credentials_json=ab.get_secret("GCP_GSM_CREDENTIALS"),
    )
    if secret_name:
        return secret_manager.get_secret(secret_name).parse_json()

    return next(iter(secret_manager.fetch_connector_secrets(connector_name)), None).parse_json()


def get_source(source_name: str) -> ab.Source:
    docker_image: bool | None = None
    if source_name == "hubspot":
        # Hubspot's CDK ref is not properly pinned in its pyproject.toml (needs airbyte-cdk==2.4.0)
        # AND it needs the old version of pendulum so it isn't compatible with Python 3.12
        docker_image = True
    else:
        raise ValueError(f"Source {source_name} not supported")

    return ab.get_source(
        f"source-{source_name}",
        config=get_config(source_name),
        docker_image=docker_image,
        streams=STREAMS,
    )


def get_duckdb_cache() -> ab.DuckDBCache:
    return ab.DuckDBCache(
        db_path=PATH_TO_DUCKDB_DB,
    )


def sync_source(source_name: str) -> None:
    cache = get_duckdb_cache()
    source = get_source(source_name)
    source.check()
    source.read(cache=cache)


def main() -> None:
    print("Hello from example.py!")
    sync_source("hubspot")


if __name__ == "__main__":
    main()
