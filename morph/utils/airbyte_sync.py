"""
Utilities for syncing data from Airbyte sources.
"""

from pathlib import Path
from typing import TYPE_CHECKING

from morph.utils.airbyte_catalog import get_source

if TYPE_CHECKING:
    import airbyte as ab


def get_duckdb_cache(db_path: str, source_name: str) -> "ab.DuckDBCache":
    """Get a DuckDB cache instance.

    Args:
        db_path: Path to the DuckDB database
        source_name: Name of the source

    Returns:
        A DuckDB cache instance
    """
    import airbyte as ab  # Problem with imports

    return ab.DuckDBCache(
        db_path=db_path,
        schema_name=f"{source_name}_raw",
    )


def sync_source(
    source_name: str,
    streams: list[str] | str = "*",
    db_path: Path | None = None,
) -> None:
    """Sync data from an Airbyte source to a local database.

    Args:
        source_name: Name of the source
        streams: List of streams to sync or "*" for all
        db_path: Optional path to the DuckDB database
    """
    if db_path is None:
        db_path = Path(f".data/{source_name}.duckdb")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Ensure the .data directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    cache = get_duckdb_cache(str(db_path), source_name)
    source = get_source(source_name, streams)
    source.check()
    source.read(cache=cache)
