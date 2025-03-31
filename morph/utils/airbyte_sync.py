"""
Utilities for syncing data from Airbyte sources.
"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import airbyte as ab
from airbyte_cdk.models.airbyte_protocol import (
    AirbyteStream,
    ConfiguredAirbyteCatalog,
    ConfiguredAirbyteStream,
    DestinationSyncMode,
    SyncMode,
)
from airbyte_protocol.models import (
    AirbyteCatalog,
)
from rich.console import Console

from morph import resources
from morph.constants import DEFAULT_PROJECT_NAME
from morph.utils import text_utils
from morph.utils.airbyte_catalog import get_source, write_catalog_file
from morph.utils.dbt_source_files import generate_dbt_sources_yml_from_airbyte_catalog
from morph.utils.logic import if_none

console = Console()


def get_duckdb_cache(db_path: str, source_name: str) -> ab.DuckDBCache:
    """Get a DuckDB cache instance.

    Args:
        db_path: Path to the DuckDB database
        source_name: Name of the source

    Returns:
        A DuckDB cache instance
    """
    return ab.DuckDBCache(
        db_path=db_path,
        schema_name=f"{source_name}_raw",
    )


def sync_source(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    streams: list[str] | str = "*",
    db_path: Path | None = None,
    *,
    no_catalog: bool = False,
    no_creds: bool = False,
    with_data: bool | None = None,
) -> None:
    """Sync data from an Airbyte source to a local database.

    Args:
        source_name: Name of the source
        streams: List of streams to sync or "*" for all
        db_path: Optional path to the DuckDB database
        no_data: If True, only create empty tables without syncing data
        no_creds: If True, do not use credentials for the source
    """
    if not no_catalog:
        console.print(f"Generating Airbyte catalog for '{source_name}'...")
        write_catalog_file(
            source_name=source_name,
        )
        console.print(f"Generating dbt source file for '{source_name}'.")
        generate_dbt_sources_yml_from_airbyte_catalog(
            source_name=source_name,
            project_name=project_name,
        )
        console.print(f"Generated Airbyte catalog and dbt source file for {source_name}.")

    with_data = if_none(with_data, False)
    if db_path is None:
        db_path = Path(f".data/{source_name}.duckdb")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Ensure the .data directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    if no_creds:
        # Get the catalog file path
        catalog_file = resources.get_generated_catalog_path(
            source_name=source_name,
        )
        # Load the catalog from the file
        discovered_catalog = AirbyteCatalog.model_validate(
            text_utils.load_yaml_file(catalog_file),
        )

        # Create a fake source using the catalog
        class FakeSource:
            name = source_name

            def get_selected_streams(self) -> list[str]:
                return [stream.name for stream in discovered_catalog.streams]

            def get_configured_catalog(
                self,
                streams: list[str] | str | None = None,
            ) -> ConfiguredAirbyteCatalog:
                _ = streams
                return ConfiguredAirbyteCatalog(
                    streams=[
                        ConfiguredAirbyteStream(
                            stream=AirbyteStream(
                                name=stream.name,
                                json_schema=stream.json_schema,
                                source_defined_cursor=stream.source_defined_cursor,
                                supported_sync_modes=[SyncMode.full_refresh],
                            ),
                            sync_mode=SyncMode.full_refresh,
                            destination_sync_mode=DestinationSyncMode.append,
                        )
                        for stream in discovered_catalog.streams
                    ],
                )

        source = cast(ab.Source, FakeSource())  # Fake that this is a real source

    else:
        source = get_source(
            source_name=source_name,
            streams=streams,
        )
        source.check()

    console.print(f"Creating empty tables for '{source_name}'...")
    cache = get_duckdb_cache(
        db_path=str(db_path),
        source_name=source_name,
    )
    # Create tables in the database
    cache.create_source_tables(source)
    console.print("Completed creating empty tables.")

    if with_data and not no_creds:
        console.print(f"Syncing '{source_name}' raw data...")
        source.read(cache=cache, streams="*")
