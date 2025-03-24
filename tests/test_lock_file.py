"""
Tests for lock file generation.
"""

import tempfile
from pathlib import Path

import pytest
import yaml

from morph.utils.lock_file import (
    compute_file_hash,
    find_unmapped_target_fields,
    find_unmapped_target_tables,
    find_unused_source_streams,
    generate_lock_file_for_project,
    validate_field_mappings,
)


def test_compute_file_hash():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"test content")
        filename = f.name

    # Compute hash
    file_hash = compute_file_hash(filename)

    # Clean up
    Path(filename).unlink()

    # Hash should be consistent
    assert file_hash == "6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"


def test_find_unused_source_streams():
    # Test data
    config_streams = ["stream1", "stream2", "stream3"]
    mapping_files = [
        {"transforms": [{"from": [{"stream1": "table1"}]}]},
        {"transforms": [{"from": {"stream2": "table2"}}]},
    ]

    # Find unused streams
    unused_streams = find_unused_source_streams(config_streams, mapping_files)

    # Should find stream3 as unused
    assert unused_streams == ["stream3"]


def test_find_unmapped_target_tables():
    # Test data
    config_tables = ["table1", "table2", "table3"]
    mapping_files = [{"transforms": [{"id": "table1"}]}, {"transforms": [{"id": "table2"}]}]

    # Find unmapped tables
    unmapped_tables = find_unmapped_target_tables(config_tables, mapping_files)

    # Should find table3 as unmapped
    assert unmapped_tables == ["table3"]


def test_find_unmapped_target_fields():
    # Test data
    transform_id = "table1"
    target_schema = {
        "sources": [
            {
                "tables": [
                    {
                        "name": "table1",
                        "columns": [{"name": "field1"}, {"name": "field2"}, {"name": "field3"}],
                    },
                ],
            },
        ],
    }
    fields = {"field1": {"expression": "source.field1"}, "field2": {"expression": "source.field2"}}

    # Find unmapped fields
    unmapped_fields = find_unmapped_target_fields(transform_id, target_schema, fields)

    # Should find field3 as unmapped
    assert unmapped_fields == ["field3"]


def test_validate_field_mappings():
    # Valid mapping
    source_aliases = {"contacts"}
    fields = {"field1": {"expression": "contacts.field1"}, "field2": {"expression": "MISSING"}}

    # Should not raise an exception
    validate_field_mappings("transform_id", source_aliases, fields)

    # Invalid mapping (typo in table name)
    source_aliases = {"contacts"}
    fields = {"field1": {"expression": "contact.field1"}}

    # Should raise ValueError
    with pytest.raises(ValueError):
        validate_field_mappings("transform_id", source_aliases, fields)


def test_generate_lock_file():
    # Create test directory structure
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create config file
        config = {
            "source_name": "test",
            "source_streams": ["stream1", "stream2"],
            "target_tables": ["table1", "table2"],
            "target_dbt_schema": "https://example.com/schema.yml",
        }

        config_dir = Path(tmpdir) / "config"
        config_dir.mkdir()
        with (config_dir / "config.yml").open("w") as f:
            yaml.dump(config, f)

        # Create mapping file
        mapping = {
            "domain": "test.test",
            "transforms": [
                {
                    "id": "table1",
                    "from": [{"stream1": "source.stream1"}],
                    "fields": {
                        "field1": {"expression": "stream1.field1"},
                        "field2": {"expression": "MISSING"},
                    },
                    "annotations": {"unused_source_fields": {"stream1": ["unused1", "unused2"]}},
                },
            ],
        }

        mapping_dir = Path(tmpdir) / "transforms"
        mapping_dir.mkdir()
        with (mapping_dir / "table1.yml").open("w") as f:
            yaml.dump(mapping, f)

        # Create target schema
        target_schema = {
            "sources": [
                {
                    "tables": [
                        {
                            "name": "table1",
                            "columns": [{"name": "field1"}, {"name": "field2"}, {"name": "field3"}],
                        },
                        {"name": "table2", "columns": [{"name": "field1"}, {"name": "field2"}]},
                    ],
                },
            ],
        }

        # Call function
        lock_file = Path(tmpdir) / "morph-lock.toml"
        generate_lock_file_for_project(
            source_name="test",
            project_name="test",
            config=config,
            mapping_dir=mapping_dir,
            target_schema=target_schema,
            output_path=lock_file,
        )

        # Verify lock file was created
        assert lock_file.exists()
