"""Tests for the subcolumns functionality in dbt source files."""

from morph.models import DbtSourceColumn, DbtSourceTable
from morph.utils.dbt_source_files import json_schema_to_dbt_table

EXPECTED_TOP_LEVEL_SUBCOLUMNS = 3
EXPECTED_NESTED_SUBCOLUMNS = 2
EXPECTED_ADDRESS_SUBCOLUMNS = 3


def test_dbt_source_column_from_json_schema_with_subcolumns() -> None:
    """Test conversion of nested JSON schema properties to dbt column definitions with subcolumns."""
    object_schema = {
        "type": "object",
        "description": "A variant column with nested fields",
        "properties": {
            "id": {"type": "string", "description": "User ID extracted from the variant"},
            "name": {"type": "string", "description": "User name extracted from the variant"},
            "nested_again": {
                "type": "object",
                "description": "Further nested data",
                "properties": {
                    "child_id": {"type": "integer", "description": "Child ID"},
                    "child_name": {"type": "string", "description": "Child name"},
                },
            },
        },
    }

    result = DbtSourceColumn.from_json_schema("user", object_schema)

    assert result.name == "user"
    assert result.description == "A variant column with nested fields"
    assert result.data_type == "json"

    assert result.subcolumns is not None
    assert len(result.subcolumns) == EXPECTED_TOP_LEVEL_SUBCOLUMNS

    subcolumn_names = [col.name for col in result.subcolumns]
    assert "id" in subcolumn_names
    assert "name" in subcolumn_names
    assert "nested_again" in subcolumn_names

    nested_again = next(col for col in result.subcolumns if col.name == "nested_again")
    assert nested_again.description == "Further nested data"
    assert nested_again.subcolumns is not None
    assert len(nested_again.subcolumns) == EXPECTED_NESTED_SUBCOLUMNS

    nested_subcolumn_names = [col.name for col in nested_again.subcolumns]
    assert "child_id" in nested_subcolumn_names
    assert "child_name" in nested_subcolumn_names


def test_dbt_source_table_serialization_with_subcolumns() -> None:
    """Test serialization of DbtSourceTable with subcolumns."""
    nested_subcolumns = [
        DbtSourceColumn(
            name="child_id",
            description="Child ID",
            data_type="integer",
        ),
        DbtSourceColumn(
            name="child_name",
            description="Child name",
            data_type="varchar",
        ),
    ]

    nested_column = DbtSourceColumn(
        name="nested_again",
        description="Further nested data",
        data_type="json",
        subcolumns=nested_subcolumns,
    )

    subcolumns = [
        DbtSourceColumn(
            name="id",
            description="User ID extracted from the variant",
            data_type="varchar",
        ),
        DbtSourceColumn(
            name="name",
            description="User name extracted from the variant",
            data_type="varchar",
        ),
        nested_column,
    ]

    column = DbtSourceColumn(
        name="user",
        description="A variant column with nested fields",
        data_type="json",
        subcolumns=subcolumns,
    )

    table = DbtSourceTable(
        name="test_table",
        description="Test table",
        columns=[column],
    )

    serialized = table.to_dict()

    assert "columns" in serialized
    assert isinstance(serialized["columns"], list)
    assert len(serialized["columns"]) > 0

    column_dict = serialized["columns"][0]
    assert isinstance(column_dict, dict)
    assert "meta" in column_dict
    assert isinstance(column_dict["meta"], dict)
    assert "subcolumns" in column_dict["meta"]
    assert isinstance(column_dict["meta"]["subcolumns"], list)
    assert len(column_dict["meta"]["subcolumns"]) == EXPECTED_TOP_LEVEL_SUBCOLUMNS

    nested_again_dict = None
    for col in column_dict["meta"]["subcolumns"]:
        if col["name"] == "nested_again":
            nested_again_dict = col
            break

    assert nested_again_dict is not None
    assert "subcolumns" in nested_again_dict
    assert isinstance(nested_again_dict["subcolumns"], list)
    assert len(nested_again_dict["subcolumns"]) == EXPECTED_NESTED_SUBCOLUMNS


def test_json_schema_to_dbt_table_with_subcolumns() -> None:
    """Test that json_schema_to_dbt_table correctly handles nested properties."""
    schema_data = {
        "type": "object",
        "description": "A test table",
        "properties": {
            "id": {"type": "integer", "description": "Primary key"},
            "name": {"type": "string", "description": "User name"},
            "user_data": {
                "type": "object",
                "description": "User data as a variant",
                "properties": {
                    "email": {"type": "string", "description": "User email"},
                    "address": {
                        "type": "object",
                        "description": "User address",
                        "properties": {
                            "street": {"type": "string", "description": "Street address"},
                            "city": {"type": "string", "description": "City"},
                            "zip": {"type": "string", "description": "ZIP code"},
                        },
                    },
                },
            },
        },
    }

    table = json_schema_to_dbt_table("test_table", schema_data)

    assert table["name"] == "test_table"
    assert table["description"] == "A test table"
    assert "columns" in table

    assert "columns" in table
    assert isinstance(table["columns"], list)

    columns = {}
    for col in table["columns"]:
        assert isinstance(col, dict)
        assert "name" in col
        columns[col["name"]] = col

    assert "user_data" in columns
    user_data = columns["user_data"]

    assert "meta" in user_data
    assert isinstance(user_data["meta"], dict)
    assert "subcolumns" in user_data["meta"]
    assert isinstance(user_data["meta"]["subcolumns"], list)
    assert len(user_data["meta"]["subcolumns"]) == EXPECTED_NESTED_SUBCOLUMNS

    address = None
    for col in user_data["meta"]["subcolumns"]:
        if col["name"] == "address":
            address = col
            break

    assert address is not None
    assert "subcolumns" in address
    assert isinstance(address["subcolumns"], list)
    assert len(address["subcolumns"]) == EXPECTED_ADDRESS_SUBCOLUMNS


def test_dbt_source_table_deserialization_with_subcolumns() -> None:
    """Test deserialization of DbtSourceTable with subcolumns."""
    serialized_table = {
        "name": "test_table",
        "description": "Test table",
        "columns": [
            {
                "name": "user",
                "description": "A variant column with nested fields",
                "type": "json",
                "meta": {
                    "subcolumns": [
                        {
                            "name": "id",
                            "description": "User ID extracted from the variant",
                            "type": "varchar",
                        },
                        {
                            "name": "name",
                            "description": "User name extracted from the variant",
                            "type": "varchar",
                        },
                        {
                            "name": "nested_again",
                            "description": "Further nested data",
                            "type": "json",
                            "subcolumns": [
                                {
                                    "name": "child_id",
                                    "description": "Child ID",
                                    "type": "integer",
                                },
                                {
                                    "name": "child_name",
                                    "description": "Child name",
                                    "type": "varchar",
                                },
                            ],
                        },
                    ],
                },
            },
        ],
    }

    table = DbtSourceTable.from_dict(serialized_table)

    assert table.name == "test_table"
    assert table.description == "Test table"
    assert len(table.columns) == 1

    column = table.columns[0]
    assert column.name == "user"
    assert column.description == "A variant column with nested fields"
    assert column.data_type == "json"

    assert column.subcolumns is not None
    assert len(column.subcolumns) == EXPECTED_TOP_LEVEL_SUBCOLUMNS

    nested_again = next(col for col in column.subcolumns if col.name == "nested_again")
    assert nested_again.subcolumns is not None
    assert len(nested_again.subcolumns) == EXPECTED_NESTED_SUBCOLUMNS
