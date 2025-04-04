"""Models for AI-related functionality."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel
from rich.console import Console
from rich.markdown import Markdown
from typing_extensions import Self

from morph import constants, resources
from morph.utils import text_utils
from morph.utils.markdown_utils import (
    create_markdown_section,
    create_markdown_table,
    markdown_formatted_confidence,
)
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

    subcolumns: list[DbtSourceColumn] | None = None
    """Nested subcolumns for complex data types (variant/object columns)."""

    original_name: str | None = None
    """The original field name before normalization, if different from name."""

    @classmethod
    def from_json_schema(
        cls,
        property_name: str,
        property_schema: dict[str, Any],
        nesting_level: int = 0,
    ) -> DbtSourceColumn:
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

    _attached_evaluation: TableMappingEval | None = None
    """The evaluation of the table mapping."""

    def get_file_path(self) -> Path:
        """Get the file path for the transform file."""
        return resources.get_transform_file(
            source_name=self.source_name,
            project_name=self.project_name,
            transform_name=self.transform_name,
        )

    def attach_evaluation(self, evaluation: TableMappingEval) -> None:
        """Attach an evaluation to the table mapping."""
        self._attached_evaluation = evaluation

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

        table_mapping = cls(
            source_name=source_name,
            project_name=project_name,
            transform_name=transform_name,
            source_stream_name=source_stream_name,
            target_table_name=target_table_name,
            field_mappings=fields,
        )

        # Load attached evaluation if present
        if "annotations" in file_data and "evaluation" in file_data["annotations"]:
            eval_data = file_data["annotations"]["evaluation"]

            # Create field mapping evaluations
            field_mapping_evals: list[FieldMappingEval] = []
            for field_eval_data in eval_data.get("field_mapping_evals", []):
                field_mapping_evals.append(
                    FieldMappingEval(
                        name=field_eval_data["name"],
                        score=field_eval_data["score"],
                        explanation=field_eval_data["explanation"],
                    )
                )

            # Create and attach the evaluation
            evaluation = TableMappingEval(
                table_match_score=eval_data["table_match_score"],
                completion_score=eval_data["completion_score"],
                explanation=eval_data["explanation"],
                field_mapping_evals=field_mapping_evals,
            )
            table_mapping.attach_evaluation(evaluation)

        return table_mapping

    def to_file(self, transform_file: Path | None = None) -> None:
        """Write the TableMapping to a transform file."""
        transform_file = transform_file or resources.get_transform_file(
            source_name=self.source_name,
            project_name=self.project_name,
            transform_name=self.transform_name,
        )
        output_dict: dict[str, Any] = {
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
        if self._attached_evaluation:
            output_dict["annotations"] = {}
            if (
                self._attached_evaluation.table_match_score >= constants.MIN_APPROVAL_SCORE
                and len(self.get_missing_field_mappings()) <= constants.MAX_MISSING_FIELDS
            ):
                output_dict["annotations"]["approved"] = True
            else:
                output_dict["annotations"]["approved"] = False

            output_dict["annotations"]["missing_fields"] = self.get_missing_field_mappings()
            output_dict["annotations"]["evaluation"] = self._get_evaluation_as_dict()

        text_utils.dump_yaml_file(
            output_dict,
            transform_file,
        )

    def _get_evaluation_as_dict(
        self,
    ) -> dict[str, Any]:
        if not self._attached_evaluation:
            raise ValueError("No evaluation attached to the table mapping")

        def _to_dict(field_eval: FieldMappingEval) -> dict[str, Any]:
            """Add the expression to the field evaluation."""
            field_ref: FieldMapping | None = next(
                (f for f in self.field_mappings if f.name == field_eval.name),
                None,
            )
            result = field_eval.model_dump(exclude_none=True, exclude_unset=True)

            if field_ref:
                ordered_dict = {
                    "name": result.pop("name"),
                    "expression": str(field_ref.expression),
                    "score": result.pop("score", None),
                    "explanation": result.pop("explanation", None),
                }
                ordered_dict.update(result)
                result = ordered_dict

            return result

        return {
            "source_stream_name": self.source_stream_name,
            "target_table_name": self.target_table_name,
            "table_match_score": self._attached_evaluation.table_match_score,
            "completion_score": self._attached_evaluation.completion_score,
            "explanation": self._attached_evaluation.explanation,
            "field_mapping_evals": [
                _to_dict(field_eval) for field_eval in self._attached_evaluation.field_mapping_evals
            ],
        }

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

    def as_markdown(self) -> str:
        """Generate a markdown table for the mapping confidence analysis.

        Returns:
            A markdown formatted string containing the analysis
        """
        if not self._attached_evaluation:
            raise ValueError("No evaluation attached to the table mapping")

        # Create header section
        title = f"Table Mapping Eval: '{self.source_stream_name}->{self.target_table_name}'"

        # Overall confidence section
        table_match_confidence = f"Table Match Confidence Score: {markdown_formatted_confidence(self._attached_evaluation.table_match_score)}"
        table_completion_score = f"Table Completion Score: {markdown_formatted_confidence(self._attached_evaluation.completion_score)}"

        # Explanation section
        explanation = create_markdown_section(
            "Explanation",
            self._attached_evaluation.explanation,
            level=3,
        )

        # Field-by-field analysis section
        headers = ["Field", "Expression", "Description", "Confidence", "Evaluation"]
        rows: list[list[str]] = []

        for field_eval in self._attached_evaluation.field_mapping_evals:
            field_ref: FieldMapping = next(
                f for f in self.field_mappings if f.name == field_eval.name
            )
            rows.append(
                [
                    field_eval.name,
                    str(field_ref.expression),
                    field_ref.description or "",
                    markdown_formatted_confidence(field_eval.score),
                    field_eval.explanation,
                ],
            )

        field_analysis = create_markdown_section(
            "Field-by-Field Analysis",
            create_markdown_table(headers, rows),
            level=3,
        )

        # Combine all sections
        return create_markdown_section(
            title,
            table_match_confidence
            + "\n\n"
            + table_completion_score
            + "\n\n"
            + explanation
            + field_analysis,
            level=2,
        )

    def print_as_rich_table(self) -> None:
        """Print a complete mapping confidence analysis.

        This method is maintained for backward compatibility but now uses markdown.

        Args:
            confidence: The confidence evaluation results
            fields: List of field mappings
            title: Optional title for the analysis table
        """
        console.print(Markdown(self.as_markdown()))


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

    table_match_score: float
    """The confidence score for the name match between the source and target tables."""

    completion_score: float
    """The overall confidence score (0.00 to 1.00)."""

    explanation: str
    """A detailed explanation of the overall score."""

    field_mapping_evals: list[FieldMappingEval]
    """A dictionary of field names and their confidence scores."""


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

    def as_markdown_table(self) -> str:
        """Return a markdown representation of the object.

        Returns:
            A markdown formatted string
        """
        title = f"Table Matching Suggestion for '{self.target_table_name}'"

        # Create a simple two-column table
        headers = ["Property", "Value"]
        rows = [
            ["Suggested Source Table", self.suggested_source_table_name],
            ["Confidence Score", markdown_formatted_confidence(self.confidence_score)],
            ["Explanation", self.explanation],
        ]

        table = create_markdown_table(headers, rows)
        return create_markdown_section(title, table, level=3)

    def as_rich_table(self) -> Markdown:
        """Return a markdown representation of the object.

        This method is maintained for backward compatibility but now returns a markdown string.

        Returns:
            A markdown formatted string
        """
        return Markdown(self.as_markdown_table())


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


class TableMappingAudit(BaseModel):
    """Represents the audit results for a table mapping."""

    _table_mapping: TableMapping
    _source_dbt_file: DbtSourceFile
    _target_dbt_file: DbtSourceFile

    unused_source_table_columns: list[str]
    """The source table columns that are not used in the transform."""

    omitted_target_table_columns: list[str]
    """The target table columns that are not declared in the mapping."""

    missing_target_table_columns: list[str]
    """The source table columns that are declared "MISSING" in the transform."""

    erroneous_source_table_columns: list[str]
    """Any source table columns that are referenced but do not exist in the source.

    These are likely caused by hallucinations in the LLM, or else a column was removed that
    was previously present.
    """

    def get_errors(self) -> list[tuple[str, str]]:
        """Return a list of errors found in the audit.

        Each error is represented as a tuple of (error_type, instance_details).
        """
        return [
            ("Erroneous Source Column Reference", column)
            for column in self.erroneous_source_table_columns
        ] + [
            ("Omitted Target Column in Mapping", column)
            for column in self.omitted_target_table_columns
        ]

    @classmethod
    def new(
        cls,
        table_mapping: TableMapping,
        source_dbt_file: DbtSourceFile,
        target_dbt_file: DbtSourceFile,
    ) -> Self:
        """Create a TableMappingAudit from a TableMapping.

        Args:
            table_mapping: The table mapping to audit
            source_dbt_file: The source DBT file
            target_dbt_file: The target DBT file

        Returns:
            A TableMappingAudit instance
        """
        source_table = source_dbt_file.get_table(table_mapping.source_stream_name)
        target_table = target_dbt_file.get_table(table_mapping.target_table_name)

        return cls(
            unused_source_table_columns=cls._find_unused_source_columns(
                source_table=source_table,
                table_mapping=table_mapping,
            ),
            omitted_target_table_columns=cls._find_omitted_target_columns(
                target_table=target_table,
                table_mapping=table_mapping,
            ),
            missing_target_table_columns=cls._find_missing_target_columns(
                table_mapping=table_mapping,
            ),
            erroneous_source_table_columns=cls._find_erroneous_source_columns(
                source_table=source_table,
                table_mapping=table_mapping,
            ),
            _target_dbt_file=target_dbt_file,
            _source_dbt_file=source_dbt_file,
            _table_mapping=table_mapping,
        )

    def fix_errors(self) -> TableMapping:
        """Fix errors in the table mapping.

        Change erroneous mappings to "MISSING" and return the resulting mapping.
        """
        source_table_alias = self._table_mapping.source_stream_name
        for column in self.erroneous_source_table_columns:
            for field in self._table_mapping.field_mappings:
                if field.expression == source_table_alias + "." + column:
                    field.expression = "MISSING"

        # TODO: Declare anything missing.

        # Return the updated table mapping
        return self._table_mapping

    @staticmethod
    def _find_unused_source_columns(
        source_table: DbtSourceTable,
        table_mapping: TableMapping,
    ) -> list[str]:
        """Find source table columns that are not used in the transform.

        Args:
            source_table: The source table
            table_mapping: The table mapping

        Returns:
            List of unused source table columns
        """
        # Get all source column names
        source_column_names = {column.name for column in source_table.columns_and_subcolumns}

        # Get all source column names used in the mapping
        used_column_names: set[str] = set()
        for field in table_mapping.field_mappings:
            # Skip MISSING fields
            if field.expression == "MISSING":
                continue

            # Handle expressions that reference source columns
            expr = str(field.expression)
            if expr.startswith(f"{table_mapping.source_stream_name}."):
                # Extract the column name from the expression
                column_name = expr.split(".", 1)[1]
                used_column_names.add(column_name)

        # Find unused columns
        return sorted(source_column_names - used_column_names)

    @staticmethod
    def _find_omitted_target_columns(
        target_table: DbtSourceTable,
        table_mapping: TableMapping,
    ) -> list[str]:
        """Find target table columns that are not declared in the mapping.

        Args:
            target_table: The target table
            table_mapping: The table mapping

        Returns:
            List of target table columns that are omitted from the mapping
        """
        # Get all target column names
        target_column_names = {column.name for column in target_table.columns_and_subcolumns}

        # Get all mapped field names
        mapped_field_names = {field.name for field in table_mapping.field_mappings}

        # Find omitted columns
        return sorted(target_column_names - mapped_field_names)

    @staticmethod
    def _find_missing_target_columns(
        table_mapping: TableMapping,
    ) -> list[str]:
        """Find target table columns that are declared as 'MISSING' in the transform.

        Args:
            table_mapping: The table mapping

        Returns:
            List of target table columns that are declared as 'MISSING'
        """
        missing_columns = []

        for field in table_mapping.field_mappings:
            if field.expression == "MISSING":
                missing_columns.append(field.name)

        return sorted(missing_columns)

    @staticmethod
    def _find_erroneous_source_columns(
        source_table: DbtSourceTable,
        table_mapping: TableMapping,
    ) -> list[str]:
        """Find source table columns that are referenced but do not exist in the source.

        Args:
            source_table: The source table
            table_mapping: The table mapping

        Returns:
            List of erroneous source table columns
        """
        # Get all source column names
        source_column_names = {column.name for column in source_table.columns_and_subcolumns}

        # Find referenced source columns that don't exist
        erroneous_columns = []

        for field in table_mapping.field_mappings:
            # Skip MISSING fields
            if field.expression == "MISSING":
                continue

            # Handle expressions that reference source columns
            expr = str(field.expression)
            if expr.startswith(f"{table_mapping.source_stream_name}."):
                # Extract the column name from the expression
                column_name = expr.split(".", 1)[1]
                if column_name not in source_column_names:
                    erroneous_columns.append(column_name)

        return sorted(erroneous_columns)
