import io
import re
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def dump_yaml_file(data: Any, file_path: Path, /) -> None:
    """Dump data to a YAML file."""
    yaml.dump(data, file_path)


def dump_yaml_str(data: Any, /) -> str:
    """Dump data to a YAML string."""
    buf = io.BytesIO()
    yaml.dump(data, buf)
    return buf.getvalue().decode("utf-8")


def load_yaml_file(file_path: Path, /) -> dict[str, Any]:
    """Load data from a YAML file."""
    return yaml.load(file_path)


def load_yaml_str(data: str, /) -> dict[str, Any]:
    """Load data from a YAML string."""
    return yaml.load(data)


def normalize_field_name(name: str) -> str:
    """Normalize a field name by replacing special characters with underscores.

    Args:
        name: The original field name to normalize.

    Returns:
        The normalized field name, with special characters replaced by underscores.
    """
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)
