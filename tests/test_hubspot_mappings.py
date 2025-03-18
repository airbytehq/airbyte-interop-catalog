"""Tests for the HubSpot mappings."""

from pathlib import Path

import yaml


def test_tickets_to_ticket_mapping():
    """Test that the tickets to ticket mapping covers all required fields."""
    # Paths to the relevant files
    base_dir = Path(__file__).parent.parent
    mapping_path = base_dir / "catalog" / "hubspot" / "transforms" / "tickets_to_ticket.yml"
    source_schema_path = base_dir / "catalog" / "hubspot" / "generated" / "src_airbyte_hubspot.yml"
    target_schema_path = (
        base_dir / "catalog" / "hubspot" / "target-schemas" / "fivetran" / "src_hubspot.yml"
    )

    # Load the mapping file
    with mapping_path.open("r") as f:
        mapping = yaml.safe_load(f)

    # Load the target schema
    with target_schema_path.open("r") as f:
        target_schema = yaml.safe_load(f)

    # Load the source schema
    with source_schema_path.open("r") as f:
        source_schema = yaml.safe_load(f)

    # Find the ticket table in the target schema
    ticket_table = None
    for table in target_schema.get("sources", [])[0].get("tables", []):
        if table.get("name") == "ticket":
            ticket_table = table
            break

    assert ticket_table is not None, "Could not find ticket table in target schema"
    
    # Find the tickets table in the source schema
    tickets_table = None
    for table in source_schema.get("sources", [])[0].get("tables", []):
        if table.get("name") == "tickets":
            tickets_table = table
            break
    
    assert tickets_table is not None, "Could not find tickets table in source schema"

    # Get all the fields from the mapping
    mapping_fields = mapping["transforms"][0]["fields"]

    # Get all the fields from the target schema
    target_fields = [column["name"] for column in ticket_table.get("columns", [])]

    # Check that all target fields are in the mapping
    for field in target_fields:
        assert field in mapping_fields, f"Field {field} from target schema is not in mapping"

    # Check that all mapping fields that aren't "MISSING" are valid source fields
    source_columns = {column["name"]: column for column in tickets_table.get("columns", [])}
    for _field, value in mapping_fields.items():
        if value != "MISSING" and isinstance(value, str) and value.startswith("tickets."):
            source_field = value.split(".", 1)[1]
            assert source_field in source_columns or source_field == "id", (
                f"Field {source_field} from mapping is not in source schema"
            )
