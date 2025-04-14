"""Utility functions for file operations."""

import hashlib
from pathlib import Path


def compute_file_hash(file_path: Path) -> str:
    """Compute the SHA-256 hash of a file.

    Args:
        file_path: Path to the file

    Returns:
        Hexadecimal hash string
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return ""

    sha256_hash = hashlib.sha256()
    # Read file in binary mode using pathlib
    content = file_path.read_bytes()
    sha256_hash.update(content)
    return sha256_hash.hexdigest()
