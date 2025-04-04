"""
Tests for TableMappingAudit functionality.
"""

import pytest

from morph.models import (
    DbtSourceColumn,
    DbtSourceFile,
    DbtSourceTable,
    FieldMapping,
    TableMapping,
    TableMappingAudit,
)


class TestTableMappingAudit:
    """Tests for TableMappingAudit class."""

    @pytest.fixture
    def source_table(self) -> DbtSourceTable:
        """Create a source table fixture."""
        return DbtSourceTable(
            name="source_table",
            description="A source table",
            columns=[
                DbtSourceColumn(name="id", data_type="integer", description="Primary key"),
                DbtSourceColumn(name="name", data_type="varchar", description="User name"),
                DbtSourceColumn(name="email", data_type="varchar", description="User email"),
                DbtSourceColumn(
                    name="created_at",
                    data_type="timestamp",
                    description="Creation timestamp",
                ),
                DbtSourceColumn(
                    name="updated_at",
                    data_type="timestamp",
                    description="Update timestamp",
                ),
                DbtSourceColumn(
                    name="metadata",
                    data_type="json",
                    description="User metadata",
                    subcolumns=[
                        DbtSourceColumn(name="age", data_type="integer", description="User age"),
                        DbtSourceColumn(
                            name="country",
                            data_type="varchar",
                            description="User country",
                        ),
                    ],
                ),
            ],
        )

    @pytest.fixture
    def target_table(self) -> DbtSourceTable:
        """Create a target table fixture."""
        return DbtSourceTable(
            name="target_table",
            description="A target table",
            columns=[
                DbtSourceColumn(name="id", data_type="integer", description="Primary key"),
                DbtSourceColumn(
                    name="full_name",
                    data_type="varchar",
                    description="User full name",
                ),
                DbtSourceColumn(
                    name="email_address",
                    data_type="varchar",
                    description="User email address",
                ),
                DbtSourceColumn(
                    name="created_date",
                    data_type="timestamp",
                    description="Creation date",
                ),
                DbtSourceColumn(name="age", data_type="integer", description="User age"),
                DbtSourceColumn(name="country", data_type="varchar", description="User country"),
            ],
        )

    @pytest.fixture
    def source_dbt_file(self, source_table: DbtSourceTable) -> DbtSourceFile:
        """Create a source DBT file fixture."""
        return DbtSourceFile(
            source_name="test_source",
            source_tables=[source_table],
        )

    @pytest.fixture
    def target_dbt_file(self, target_table: DbtSourceTable) -> DbtSourceFile:
        """Create a target DBT file fixture."""
        return DbtSourceFile(
            source_name="test_target",
            source_tables=[target_table],
        )

    @pytest.fixture
    def table_mapping(self) -> TableMapping:
        """Create a table mapping fixture."""
        return TableMapping(
            source_name="test_source",
            project_name="test_project",
            transform_name="target_table",
            source_stream_name="source_table",
            target_table_name="target_table",
            field_mappings=[
                FieldMapping(
                    name="id",
                    expression="source_table.id",
                    description="Primary key",
                ),
                FieldMapping(
                    name="full_name",
                    expression="source_table.name",
                    description="User full name",
                ),
                FieldMapping(
                    name="email_address",
                    expression="source_table.email",
                    description="User email address",
                ),
                # Missing field
                FieldMapping(
                    name="created_date",
                    expression="MISSING",
                    description="Creation date",
                ),
                # Field with erroneous source column
                FieldMapping(
                    name="age",
                    expression="source_table.age",
                    description="User age",
                ),
                # Omitted target field (country is not mapped)
            ],
        )

    def test_find_unused_source_columns(
        self,
        source_table: DbtSourceTable,
        table_mapping: TableMapping,
    ):
        """Test _find_unused_source_columns method."""
        unused_columns = TableMappingAudit._find_unused_source_columns(
            source_table=source_table,
            table_mapping=table_mapping,
        )

        # These columns from source_table are not used in the mapping
        assert set(unused_columns) == {
            "created_at",
            "updated_at",
            "metadata",
            "metadata.age",
            "metadata.country",
        }

    def test_find_omitted_target_columns(
        self,
        target_table: DbtSourceTable,
        table_mapping: TableMapping,
    ):
        """Test _find_omitted_target_columns method."""
        omitted_columns = TableMappingAudit._find_omitted_target_columns(
            target_table=target_table,
            table_mapping=table_mapping,
        )

        # The 'country' column from target_table is not declared in the mapping
        assert omitted_columns == ["country"]

    def test_find_missing_target_columns(self, table_mapping: TableMapping):
        """Test _find_missing_target_columns method."""
        missing_columns = TableMappingAudit._find_missing_target_columns(
            table_mapping=table_mapping,
        )

        # The 'created_date' field is marked as "MISSING" in the mapping
        assert missing_columns == ["created_date"]

    def test_find_erroneous_source_columns(
        self,
        source_table: DbtSourceTable,
        table_mapping: TableMapping,
    ):
        """Test _find_erroneous_source_columns method."""
        erroneous_columns = TableMappingAudit._find_erroneous_source_columns(
            source_table=source_table,
            table_mapping=table_mapping,
        )

        # The 'age' column is referenced in the mapping but doesn't exist in the source table
        # (it exists as a subcolumn of metadata, but not as a top-level column)
        assert erroneous_columns == ["age"]

    def test_new_method(
        self,
        source_dbt_file: DbtSourceFile,
        target_dbt_file: DbtSourceFile,
        table_mapping: TableMapping,
    ):
        """Test new method."""
        audit = TableMappingAudit.new(
            table_mapping=table_mapping,
            source_dbt_file=source_dbt_file,
            target_dbt_file=target_dbt_file,
        )

        # Verify all fields are populated correctly
        assert set(audit.unused_source_table_columns) == {
            "created_at",
            "updated_at",
            "metadata",
            "metadata.age",
            "metadata.country",
        }
        assert audit.omitted_target_table_columns == ["country"]
        assert audit.missing_target_table_columns == ["created_date"]
        assert audit.erroneous_source_table_columns == ["age"]
