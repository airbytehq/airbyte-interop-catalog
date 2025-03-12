"""Core transformation functionality for Morph."""

import csv
import json
from pathlib import Path
from typing import Any

from rich.console import Console

console = Console()


def read_file(file_path: str | Path) -> dict[str, Any]:
    """
    Read data from a file based on its extension.

    Args:
        file_path: Path to the file to read

    Returns:
        Dict containing the parsed data
    """
    path = Path(file_path)

    if path.suffix.lower() == ".json":
        with path.open() as f:
            return json.load(f)
    elif path.suffix.lower() == ".csv":
        data = []
        with path.open(newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))
        return {"data": data}
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def write_file(data: dict[str, Any], file_path: str | Path | None = None) -> None:
    """
    Write data to a file or stdout.

    Args:
        data: Data to write
        file_path: Path to write to, or None for stdout
    """
    if file_path is None:
        console.print_json(data=data)
        return

    path = Path(file_path)

    if path.suffix.lower() == ".json":
        with path.open("w") as f:
            json.dump(data, f, indent=2)
    elif path.suffix.lower() == ".csv":
        if not isinstance(data.get("data"), list):
            raise ValueError("Data must contain a 'data' key with a list of records for CSV output")

        records = data["data"]
        if not records:
            raise ValueError("No records to write")

        fieldnames = records[0].keys()
        with path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def apply_transform(data: dict[str, Any], transform_type: str) -> dict[str, Any]:
    """
    Apply a transformation to the data.

    Args:
        data: Data to transform
        transform_type: Type of transformation to apply

    Returns:
        Transformed data
    """
    if transform_type == "uppercase_keys":
        return {k.upper(): v for k, v in data.items()}
    if transform_type == "lowercase_keys":
        return {k.lower(): v for k, v in data.items()}
    if transform_type == "flatten":
        result = {}

        def _flatten(d, prefix=""):
            for k, v in d.items():
                key = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    _flatten(v, key)
                else:
                    result[key] = v

        _flatten(data)
        return result
    raise ValueError(f"Unsupported transform type: {transform_type}")
