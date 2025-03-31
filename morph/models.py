"""Models for AI-related functionality."""

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from typing_extensions import Self

from morph import resources
from morph.utils import text_utils
from morph.utils.rich_utils import rich_formatted_confidence
from morph.utils.text_utils import normalize_field_name

console = Console()

COMPLEX_DATA_TYPE = "json"  # Type for complex objects with subcolumns


class NoConfidenceChoice(BaseModel):
    """Represents a choice to not make a selection.

    This is used instead of choosing a specific source schema, because the AI
    does not have any good options to choose from.
    """

    reason: str
    """Explanation of why the AI did not make a selection."""

    bad_choice_if_forced: str | None = None
    """The next-best path to take if the user forces a selection."""


class DbtSourceColumn(BaseModel):
    """Represents a column in a source table schema."""

    name: str
    """The name of the column."""

    description: str | None = None
    """A description of the column."""

    data_type: str | None = None
    """The data type of the column."""

    subcolumns: list["DbtSourceColumn"] | None = None
    """Nested subcolumns for complex data types (variant/object columns)."""

    original_name: str | None = None
    """The original field name before normalization, if different from name."""

    @classmethod
    def from_json_schema(
        cls,
        property_name: str,
        property_schema: dict[str, Any],
        nesting_level: int = 0,
    ) -> "DbtSourceColumn":
        """Convert a JSON schema property to a DbtSourceColumn.

        Args:
            property_name: The name of the property.
            property_schema: The JSON schema for the property.
            nesting_level: The current nesting level (0 for top-level properties).

        Returns:
            A DbtSourceColumn instance representing the column.
        """

        type_mapping = {
            "string": "varchar",
            "integer": "integer",
            "number": "float",
            "boolean": "boolean",
            "object": COMPLEX_DATA_TYPE,
            "array": "array",
        }

        data_type = "varchar"  # Default
        if "type" in property_schema:
            json_type = property_schema["type"]
            if isinstance(json_type, list):
                non_null_types = [t for t in json_type if t != "null"]
                if non_null_types:
                    data_type = type_mapping.get(non_null_types[0], "varchar")
            else:
                data_type = type_mapping.get(json_type, "varchar")

        if "format" in property_schema:
            format_mapping = {
                "date": "date",
                "date-time": "timestamp",
                "time": "time",
                "email": "varchar",
                "uri": "varchar",
            }
            data_type = format_mapping.get(
                property_schema["format"],
                data_type,
            )

        description = property_schema.get("description")

        subcolumns = None
        if json_type := property_schema.get("type"):
            is_object = json_type == "object" or (
                isinstance(json_type, list) and "object" in json_type
            )
            if is_object and "properties" in property_schema:
                nested_columns = []
                for prop_name, prop_schema in property_schema["properties"].items():
                    nested_column = cls.from_json_schema(
                        prop_name,
                        prop_schema,
                        nesting_level + 1,
                    )
                    nested_columns.append(nested_column)

                if nested_columns:
                    subcolumns = nested_columns

        name = property_name
        original_name = None
        if nesting_level == 0:
            normalized_name = normalize_field_name(property_name)
            if normalized_name != property_name:
                name = normalized_name
                original_name = property_name

        return cls(
            name=name,
            description=description,
            data_type=data_type,
            subcolumns=subcolumns,
            original_name=original_name,
        )


class DbtSourceTable(BaseModel):
    """Represents a source table schema in a dbt project."""

    name: str
    """The name of the table."""

    description: str | None = None
    """A description of the table."""

    columns: list[DbtSourceColumn]
    """The columns in the table."""

    @property
    def columns_and_subcolumns(self) -> list[DbtSourceColumn]:
        """Get all columns and subcolumns in the table."""

        def get_columns_and_subcolumns(
            column: DbtSourceColumn,
            parent_str: str = "",
        ) -> list[DbtSourceColumn]:
            """Recursively get all columns and subcolumns."""
            columns: list[DbtSourceColumn] = [
                column.model_copy(update={"name": parent_str + column.name}),
            ]
            for subcolumn in column.subcolumns or []:
                columns.extend(
                    get_columns_and_subcolumns(
                        column=subcolumn,
                        parent_str=parent_str + column.name + ".",
                    ),
                )
            return columns

        result: list[DbtSourceColumn] = []
        for column in self.columns:
            result.extend(
                get_columns_and_subcolumns(column),
            )

        return result

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """Create a DbtSourceTable from a dictionary."""
        columns = []
        for column_data in data["columns"]:
            column = column_data.copy()

            if "type" in column and column.get("data_type") is None:
                column["data_type"] = column.pop("type")

            if column.get("meta") and "subcolumns" in column["meta"]:
                column["subcolumns"] = column["meta"].pop("subcolumns")
                if not column["meta"]:  # Clean up empty meta dict
                    column.pop("meta")

            columns.append(DbtSourceColumn(**column))

        return cls(
            name=data["name"],
            description=data.get("description", None),  # noqa: SIM910  # I disagree with this rule
            columns=columns,
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert the DbtSourceTable to a dictionary."""
        columns = []
        for column in self.columns:
            col_dict = column.model_dump(exclude_none=True, exclude_unset=True)

            if "description" in col_dict and not col_dict["description"]:
                col_dict.pop("description")

            if "original_name" in col_dict:
                if "meta" not in col_dict:
                    col_dict["meta"] = {}
                col_dict["meta"]["original_name"] = col_dict.pop("original_name")

            if col_dict.get("subcolumns"):
                if "meta" not in col_dict:
                    col_dict["meta"] = {}
                col_dict["meta"]["subcolumns"] = col_dict.pop("subcolumns")

            if not col_dict.get("meta"):
                col_dict.pop("meta", None)

            columns.append(col_dict)

        result = {"name": self.name, "columns": columns}

        if self.description:
            result["description"] = self.description

        return result


class DbtSourceFile(BaseModel):
    """Represents a dbt source file."""

    source_name: str
    """The name of the source."""

    source_tables: list[DbtSourceTable]
    """The sources in the file."""

    def get_source_table(self, table_name: str) -> DbtSourceTable:
        """Get a source table by name."""
        matches = [table for table in self.source_tables if table.name == table_name]
        if not matches:
            raise ValueError(f"Table '{table_name}' not found in source file.")

        return matches[0]

    @classmethod
    def from_file(cls, file_path: Path) -> Self:
        """Create a DbtSourceFile from a file."""
        file_data = text_utils.load_yaml_file(file_path)
        sources = file_data["sources"]
        if len(sources) != 1:
            raise ValueError("Expected exactly one source in the file")

        source = sources[0]
        return cls(
            source_name=source["name"],
            source_tables=[DbtSourceTable.from_dict(table) for table in source["tables"]],
        )

    @classmethod
    def from_airbyte_catalog_json(
        cls,
        catalog_file: Path | str,
        source_name: str,
        database: str | None = None,  # noqa: ARG003
        schema: str | None = None,  # noqa: ARG003
    ) -> Self:
        """Create a DbtSourceFile from an Airbyte catalog JSON file.

        Args:
            catalog_file: Path to the Airbyte catalog JSON file
            source_name: Name of the source
            database: Optional database name
            schema: Optional schema name

        Returns:
            A DbtSourceFile instance
        """
        catalog_path = Path(catalog_file)
        catalog = json.loads(catalog_path.read_text())

        if "streams" not in catalog:
            raise ValueError(f"Invalid Airbyte catalog: 'streams' key not found in {catalog_file}")

        tables = []
        for stream in catalog["streams"]:
            if "name" not in stream or "json_schema" not in stream:
                continue

            table_name = stream["name"]

            columns = []
            if "properties" in stream["json_schema"]:
                for prop_name, prop_schema in stream["json_schema"]["properties"].items():
                    dbt_column = DbtSourceColumn.from_json_schema(prop_name, prop_schema)
                    columns.append(dbt_column)

            airbyte_columns = [
                DbtSourceColumn(
                    name="_airbyte_extracted_at",
                    data_type="timestamp",
                    description="Timestamp when the record was extracted from the source",
                ),
                DbtSourceColumn(
                    name="_airbyte_meta",
                    data_type=COMPLEX_DATA_TYPE,
                    description="Metadata about the record",
                ),
                DbtSourceColumn(
                    name="_airbyte_raw_id",
                    data_type="varchar",
                    description="Unique identifier for the raw record",
                ),
            ]

            columns.extend(airbyte_columns)

            table = DbtSourceTable(
                name=table_name,
                description=stream["json_schema"].get("description"),
                columns=columns,
            )
            tables.append(table)

        sorted_tables = sorted(tables, key=lambda x: x.name)

        return cls(
            source_name=source_name,
            source_tables=sorted_tables,
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert the DbtSourceFile to a dictionary.

        Returns:
            A dictionary representation of the DbtSourceFile
        """
        source = {
            "name": self.source_name,
            "schema": "{{ "
            + f"var('airbyte_{self.source_name}_schema', default='{self.source_name}_raw')"
            + " }}",
            "database": "{{ "
            + f"var('airbyte_{self.source_name}_database', default='{self.source_name}')"
            + " }}",
            "tables": [table.to_dict() for table in self.source_tables],
        }

        return {"version": 2, "sources": [source]}

    def get_table(self, table_name: str) -> DbtSourceTable:
        """Get a table from the source file."""
        table = next(
            (table for table in self.source_tables if table.name == table_name),
            None,
        )
        if not table:
            table_names = [table.name for table in self.source_tables]
            raise ValueError(f"Table '{table_name}' not found in source file. Found: {table_names}")

        return table

    def get_table_names(self) -> list[str]:
        """Get the names of all tables in the source file."""
        return [table.name for table in self.source_tables]


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    """The name of the field."""

    expression: str | bool | float | int
    """The expression used to generate the field.

    The text `MISSING` is used to indicate that the field is not mapped to any field in the source.
    """

    description: str | None = None
    """A description of the field."""


class FieldMappingSuggestion(BaseModel):
    """A suggestion for a field mapping."""

    target_field_name: str
    """The name of the target field."""

    source_field_name: str
    """The name of the source field or the text'MISSING' if the field cannot be mapped."""

    confidence_score: float
    """The confidence score for the field mapping, or 0.00 if the field cannot be mapped."""

    next_best_source_field_name: str | None = None
    """The next-best source field name, or 'MISSING' if the field cannot be mapped."""

    next_best_source_field_confidence_score: float | None = None
    """The confidence score for the next-best source field, or None if the field cannot be mapped."""


class TableMapping(BaseModel):
    """Represents a table mapping with its properties."""

    source_name: str
    """The name of the source."""

    project_name: str
    """The name of the project."""

    transform_name: str
    """The name of the transform."""

    source_stream_name: str
    """The name of the source table."""

    target_table_name: str
    """The name of the target table."""

    field_mappings: list[FieldMapping]
    """The field mappings for the table."""

    def get_file_path(self) -> Path:
        """Get the file path for the transform file."""
        return resources.get_transform_file(
            source_name=self.source_name,
            project_name=self.project_name,
            transform_name=self.transform_name,
        )

    @classmethod
    def from_file(cls, transform_file: Path) -> Self:
        """Create a TableMapping from a transform file."""
        file_data = text_utils.load_yaml_file(transform_file)
        source_name = file_data.get("domain", ".").split(".")[0]
        project_name = file_data.get("domain", ".").split(".")[1]
        transform_name = transform_file.stem

        mapping_data = file_data["transforms"][0]

        target_table_name = transform_file.stem

        source_stream_expression: dict[str, str] = mapping_data["from"][0]
        # Will be like:
        # {"source_stream_alias": "domain.source_stream_name"}
        source_stream_alias = next(iter(source_stream_expression.keys()))
        _ = source_stream_alias  # Unused for now
        source_stream_name = next(iter(source_stream_expression.values())).split(".")[-1]

        if not target_table_name:
            raise ValueError("target_table_name is required")

        fields: list[FieldMapping] = []
        for field_name, field_data in mapping_data.get("fields", {}).items():
            fields.append(
                FieldMapping(
                    name=field_name,
                    expression=field_data.get("expression", ""),
                    description=field_data.get("description", ""),
                ),
            )

        return cls(
            source_name=source_name,
            project_name=project_name,
            transform_name=transform_name,
            source_stream_name=source_stream_name,
            target_table_name=target_table_name,
            field_mappings=fields,
        )

    def to_file(self, transform_file: Path) -> None:
        """Write the TableMapping to a transform file."""
        output_dict = {
            "domain": f"{self.source_name}.{self.project_name}",
            "transforms": [
                {
                    "name": self.transform_name,
                    "from": [
                        {self.source_stream_name: f"{self.source_name}.{self.source_stream_name}"},
                    ],
                    "fields": {
                        field.name: {
                            "expression": field.expression,
                            "description": field.description,
                        }
                        for field in self.field_mappings
                    },
                },
            ],
        }
        text_utils.dump_yaml_file(
            output_dict,
            transform_file,
        )

    def get_missing_field_mappings(
        self,
    ) -> list[str]:
        """Find names of target fields marked as 'MISSING' in a transform.

        Returns:
            List of fields marked as 'MISSING'.
        """
        missing_fields: list[str] = []

        for field in self.field_mappings:
            expression = field.expression

            # Check if expression is "MISSING"
            if expression == "MISSING":
                missing_fields.append(field.name)

        return sorted(missing_fields)

    def get_mapped_fields(
        self,
        *,
        source_alias: str | None = None,
    ) -> list[FieldMapping]:
        """Find mapped fields, optionally filtered by source alias.

        Fields that are marked as 'MISSING' are always excluded.

        Args:
            source_alias: Optional source alias to filter field mappings

        Returns:
            List of mapped field mappings, excluding MISSING expressions
        """
        if source_alias:
            return [
                f
                for f in self.field_mappings
                if str(f.expression) != "MISSING"
                and str(f.expression).startswith(f"{source_alias}.")
            ]

        return [f for f in self.field_mappings if str(f.expression) != "MISSING"]


class FieldMappingEval(BaseModel):
    """Represents the confidence score for a field mapping."""

    name: str
    """The name of the field."""

    score: float
    """The confidence score (0.00 to 1.00).

    Values defined as `MISSING` should receive a score of 0.00.
    """

    explanation: str
    """A short explanation of the score."""


class TableMappingSuggestion(BaseModel):
    """A suggestion for a table mapping."""

    source_stream_name: str
    """The name of the source stream."""

    target_table_name: str
    """The name of the target table."""

    name_match_confidence_score: float
    """The confidence score for the mapping of source stream name to target table name."""

    field_mapping_confidence_scores: list[float] | None = None
    """The confidence scores for the mapping of fields from the source stream to the target table.

    If the field mappings are not available, this will be `None`.
    """


class TableMappingEval(BaseModel):
    """Represents the confidence score and explanation for a table mapping."""

    score: float
    """The overall confidence score (0.00 to 1.00)."""

    name_match_score: float
    """The confidence score for the name match between the source and target tables."""

    explanation: str
    """A detailed explanation of the overall score."""

    field_mapping_evals: list[FieldMappingEval]
    """A dictionary of field names and their confidence scores."""

    def print_as_rich_table(
        self,
        from_transform: TableMapping,
    ) -> None:
        """Print a complete mapping confidence analysis.

        Args:
            confidence: The confidence evaluation results
            fields: List of field mappings
            title: Optional title for the analysis table
        """
        # Create results table
        table = Table(title="Table Mapping Eval")
        table.add_column("Field", style="cyan")
        table.add_column("Expression", style="yellow")
        table.add_column("Description")
        table.add_column("Confidence", justify="right")
        table.add_column("Evaluation", style="italic")
        # Print results
        console.print(
            f"\nOverall Confidence Score: {rich_formatted_confidence(self.score)}",
        )
        console.print("\nExplanation:")
        console.print(f"\n{self.explanation}", style="italic")
        console.print("\nField-by-Field Analysis:")

        # Print each field evaluation
        for field_eval in self.field_mapping_evals:
            field_ref: FieldMapping = next(
                f for f in from_transform.field_mappings if f.name == field_eval.name
            )
            table.add_row(
                field_eval.name,
                str(field_ref.expression),
                field_ref.description or "",
                rich_formatted_confidence(field_eval.score),
                field_eval.explanation,
            )

        console.print(table)


class SourceTableSummary(BaseModel):
    """A summary of a source table."""

    name: str
    description: str | None = None
    column_names: list[str]

    @classmethod
    def from_dbt_source_file(
        cls,
        source_file: Path,
    ) -> list[Self]:
        """Create a SourceStreamSummary from a DbtSourceTable."""
        dbt_source_file: DbtSourceFile = DbtSourceFile.from_file(file_path=source_file)
        source_tables: list[DbtSourceTable] = dbt_source_file.source_tables
        return [
            cls(
                name=table.name,
                description=table.description,
                column_names=[column.name for column in table.columns_and_subcolumns],
            )
            for table in source_tables
        ]


class SourceTableMappingSuggestion(BaseModel):
    """A suggestion for a source table mapping.

    Optionally, the next-best match for the source table can also be provided.
    """

    target_table_name: str
    """The name of the target table."""

    suggested_source_table_name: str
    """The name of the source table suggested by the AI."""

    confidence_score: float
    """The confidence score for the mapping of the source table to the target table."""

    explanation: str
    """A detailed explanation of the confidence score."""

    def as_rich_table(self) -> Table:
        """Return a rich representation of the object as a Rich Table."""
        table = Table(
            title="Source Table Mapping Suggestion",
            show_header=False,
        )
        table.add_row("Target Table", self.target_table_name)
        table.add_row("Suggested Source Table", self.suggested_source_table_name)
        table.add_row("Confidence Score", rich_formatted_confidence(self.confidence_score))
        table.add_row("Explanation", self.explanation)
        return table


class SourceTableMappingSuggestionShortList(BaseModel):
    """A short list of source table mapping suggestions."""

    suggestions: list[SourceTableMappingSuggestion]
    """The suggestions for the source table mapping.

    The list should be sorted by confidence score, with the highest confidence score first.
    No more than 5 suggestions and no fewer than 3 should be provided.
    """


class SourceTableMappingTopTwoSuggestions(BaseModel):
    """A suggestion for a source table mapping.

    Optionally, the next-best match for the source table can also be provided.
    """

    best_match_suggestion: SourceTableMappingSuggestion
    """The best match for the source table."""

    next_best_match_suggestion: SourceTableMappingSuggestion | None = None
    """The next-best match for the source table."""
