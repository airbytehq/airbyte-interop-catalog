"""
Tests for lock file generation.
"""

import tempfile
from pathlib import Path

from morph.utils.lock_file import (
    compute_file_hash,
)


def test_compute_file_hash():
    # Create a temporary file with known content
    temp_file = Path(tempfile.mktemp())
    temp_file.write_bytes(b"test content")

    # Compute hash
    file_hash = compute_file_hash(temp_file)

    # Clean up
    temp_file.unlink()

    # Hash should be consistent
    assert file_hash == "6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"
