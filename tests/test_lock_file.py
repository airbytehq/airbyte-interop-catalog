"""
Tests for lock file generation.
"""

import tempfile
from pathlib import Path

import pytest

from morph.utils import text_utils
from morph.utils.lock_file import (
    compute_file_hash,
    find_mapped_target_fields,
    find_missing_target_fields,
    find_omitted_target_fields,
    find_unmapped_target_tables,
    find_unused_source_streams,
    generate_lock_file_for_project,
    validate_field_mappings,
)


def test_compute_file_hash():
    # Create a temporary file with known content
    temp_file = Path(tempfile.mktemp())
    temp_file.write_bytes(b"test content")

    # Compute hash
    file_hash = compute_file_hash(str(temp_file))

    # Clean up
    temp_file.unlink()

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
    mapping_files = [{"transforms": [{"name": "table1"}]}, {"transforms": [{"name": "table2"}]}]

    # Find unmapped tables
    unmapped_tables = find_unmapped_target_tables(config_tables, mapping_files)

    # Should find table3 as unmapped
    assert unmapped_tables == ["table3"]


def test_find_omitted_target_fields():
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

    # Find omitted fields
    omitted_fields = find_omitted_target_fields(transform_id, target_schema, fields)

    # Should find field3 as omitted
    assert omitted_fields == ["field3"]


def test_find_missing_target_fields():
    # Test data
    fields = {
        "field1": {"expression": "source.field1"},
        "field2": {"expression": "MISSING"},
        "field3": {"expression": "source.field3"},
        "field4": {"expression": "MISSING"},
    }

    # Find missing fields
    missing_fields = find_missing_target_fields(fields)

    # Should find field2 and field4 as missing
    assert missing_fields == ["field2", "field4"]


def test_find_mapped_target_fields():
    # Test data
    fields = {
        "field1": {"expression": "source.field1"},
        "field2": {"expression": "MISSING"},
        "field3": {"expression": "source.field3"},
        "field4": {"expression": "MISSING"},
        "field5": {"expression": "concat(source.field5, ' suffix')"},
    }

    # Find mapped fields
    mapped_fields = find_mapped_target_fields(fields)

    # Should find field1, field3, and field5 with their expressions
    assert mapped_fields == {
        "field1": "source.field1",
        "field3": "source.field3",
        "field5": "concat(source.field5, ' suffix')",
    }


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
        config_file = config_dir / "config.yml"
        text_utils.dump_yaml_file(config, config_file)

        # Create mapping file
        mapping = {
            "domain": "test.test",
            "transforms": [
                {
                    "name": "table1",
                    "from": [{"stream1": "source.stream1"}],
                    "fields": {
                        "field1": {"expression": "stream1.field1"},
                        "field2": {"expression": "MISSING"},
                        "field4": {"expression": "MISSING"},
                    },
                    "annotations": {"unused_source_fields": {"stream1": ["unused1", "unused2"]}},
                },
            ],
        }

        mapping_dir = Path(tmpdir) / "transforms"
        mapping_dir.mkdir()
        mapping_file = mapping_dir / "table1.yml"
        text_utils.dump_yaml_file(mapping, mapping_file)

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

        # Create source schema directory and file
        source_schema_dir = Path(tmpdir) / "catalog" / "test" / "generated"
        source_schema_dir.mkdir(parents=True)
        source_schema_file = source_schema_dir / "src_airbyte_hubspot.yml"
        source_schema = {
            "sources": [
                {
                    "name": "test",
                    "tables": [
                        {"name": "stream1"},
                        {"name": "stream2"},
                    ],
                },
            ],
        }
        text_utils.dump_yaml_file(source_schema, source_schema_file)

        # Create requirements directory and file
        requirements_dir = Path(tmpdir) / "catalog" / "test" / "requirements" / "test"
        requirements_dir.mkdir(parents=True)
        requirements_file = requirements_dir / "src_hubspot.yml"
        requirements = {
            "sources": [
                {
                    "name": "test",
                    "tables": [
                        {"name": "table1"},
                        {"name": "table2"},
                    ],
                },
            ],
        }
        text_utils.dump_yaml_file(requirements, requirements_file)

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

        # For testing, we'll just verify specific content exists in the file
        # since tomli_w is write-only and we can't easily parse the TOML
        lock_data_str = lock_file.read_text()

        # Verify the mapping data exists
        assert "mappings.table1" in lock_data_str

        # Verify omitted_target_fields
        assert "omitted_target_fields" in lock_data_str
        assert "field3" in lock_data_str

        # Verify unmapped_target_fields (MISSING fields)
        assert "unmapped_target_fields" in lock_data_str
        assert "field2" in lock_data_str
        assert "field4" in lock_data_str

        # Verify mapped_target_fields
        assert "mapped_target_fields" in lock_data_str
        assert "stream1.field1" in lock_data_str
