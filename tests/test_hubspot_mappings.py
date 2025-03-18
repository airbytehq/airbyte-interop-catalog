"""Tests for the HubSpot mappings."""

import os
import pytest
import yaml
from pathlib import Path


def test_tickets_to_ticket_mapping():
    """Test that the tickets to ticket mapping covers all required fields."""
    # Paths to the relevant files
    base_dir = Path(os.path.dirname(os.path.dirname(__file__)))
    mapping_path = base_dir / "catalog" / "hubspot" / "transforms" / "tickets_to_ticket.yml"
    source_schema_path = base_dir / "catalog" / "hubspot" / "airbyte-source" / "schemas" / "tickets.json"
    target_schema_path = base_dir / "catalog" / "hubspot" / "target-schemas" / "fivetran" / "src_hubspot.yml"
    
    # Load the mapping file
    with open(mapping_path, "r") as f:
        mapping = yaml.safe_load(f)
    
    # Load the target schema
    with open(target_schema_path, "r") as f:
        target_schema = yaml.safe_load(f)
    
    # Load the source schema
    with open(source_schema_path, "r") as f:
        import json
        source_schema = json.load(f)
    
    # Find the ticket table in the target schema
    ticket_table = None
    for table in target_schema.get("sources", [])[0].get("tables", []):
        if table.get("name") == "ticket":
            ticket_table = table
            break
    
    assert ticket_table is not None, "Could not find ticket table in target schema"
    
    # Get all the fields from the mapping
    mapping_fields = mapping["transforms"][0]["fields"]
    
    # Get all the fields from the target schema
    target_fields = [column["name"] for column in ticket_table.get("columns", [])]
    
    # Check that all target fields are in the mapping
    for field in target_fields:
        assert field in mapping_fields, f"Field {field} from target schema is not in mapping"
    
    # Check that all mapping fields that aren't "MISSING" are valid source fields
    source_properties = source_schema.get("properties", {})
    for field, value in mapping_fields.items():
        if value != "MISSING" and isinstance(value, str) and value.startswith("tickets."):
            source_field = value.split(".", 1)[1]
            assert source_field in source_properties, f"Field {source_field} from mapping is not in source schema"
