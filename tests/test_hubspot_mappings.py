"""Tests for the HubSpot mappings."""

from pathlib import Path

import pytest
import yaml


def _test_mapping(source_table, target_table, mapping_file):
    """Helper function to test that a mapping covers all required fields."""
    # Paths to the relevant files
    base_dir = Path(__file__).parent.parent
    mapping_path = base_dir / "catalog" / "hubspot" / "transforms" / "fivetran-compat" / mapping_file
    source_schema_path = base_dir / "catalog" / "hubspot" / "generated" / "src_airbyte_hubspot.yml"
    target_schema_path = (
        base_dir / "catalog" / "hubspot" / "target-schemas" / "fivetran" / "src_hubspot.yml"
    )

    # Load the mapping file
    mapping = yaml.safe_load(mapping_path.read_text())

    # Load the target schema
    target_schema = yaml.safe_load(target_schema_path.read_text())

    # Load the source schema
    source_schema = yaml.safe_load(source_schema_path.read_text())

    # Find the target table in the target schema
    target_table_def = None
    for table in target_schema.get("sources", [])[0].get("tables", []):
        if table.get("name") == target_table:
            target_table_def = table
            break

    assert target_table_def is not None, f"Could not find {target_table} table in target schema"
    
    # Find the source table in the source schema
    source_table_def = None
    for table in source_schema.get("sources", [])[0].get("tables", []):
        if table.get("name") == source_table:
            source_table_def = table
            break
    
    assert source_table_def is not None, f"Could not find {source_table} table in source schema"

    # Get all the fields from the mapping
    mapping_fields = mapping["transforms"][0]["fields"]

    # Get all the fields from the target schema
    target_fields = [column["name"] for column in target_table_def.get("columns", [])]

    # Check that all target fields are in the mapping
    for field in target_fields:
        assert field in mapping_fields, f"Field {field} from target schema is not in mapping"

    # Check that all mapping fields that aren't "MISSING" are valid source fields
    source_columns = {column["name"]: column for column in source_table_def.get("columns", [])}
    for _field, value in mapping_fields.items():
        if value != "MISSING" and isinstance(value, str) and value.startswith(f"{source_table}."):
            source_field = value.split(".", 1)[1]
            assert source_field in source_columns or source_field == "id", (
                f"Field {source_field} from mapping is not in source schema"
            )


def test_tickets_to_ticket_mapping():
    """Test that the tickets to ticket mapping covers all required fields."""
    _test_mapping("tickets", "ticket", "ticket.yml")


def test_companies_to_company_mapping():
    """Test that the companies to company mapping covers all required fields."""
    _test_mapping("companies", "company", "company.yml")
