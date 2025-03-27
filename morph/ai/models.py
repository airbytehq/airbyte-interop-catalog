"""Models for AI-related functionality."""

from pathlib import Path

import rich
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from typing_extensions import Self

from morph.utils import text_utils
from morph.utils.rich_utils import rich_formatted_confidence

console = Console()


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


class DbtSourceTable(BaseModel):
    """Represents a source table schema in a dbt project."""

    name: str
    """The name of the table."""

    description: str | None = None
    """A description of the table."""

    columns: list[DbtSourceColumn]
    """The columns in the table."""

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Create a DbtSourceTable from a dictionary."""
        return cls(
            name=data["name"],
            description=data.get("description", None),  # noqa: SIM910  # I disagree with this rule
            columns=[DbtSourceColumn(**column) for column in data["columns"]],
        )

    def to_dict(self) -> dict:
        """Convert the DbtSourceTable to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "columns": [column.model_dump() for column in self.columns],
        }


class DbtSourceFile(BaseModel):
    """Represents a dbt source file."""

    source_name: str
    """The name of the source."""

    source_tables: list[DbtSourceTable]
    """The sources in the file."""

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

    def get_table(self, table_name: str) -> DbtSourceTable:
        """Get a table from the source file."""
        table = next(
            (table for table in self.source_tables if table.name == table_name),
            None,
        )
        if not table:
            raise ValueError(f"Table {table_name} not found in source file")

        return table


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

    @classmethod
    def read_from_transform_file(cls, transform_file: Path) -> Self:
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

        fields: list[DbtSourceColumn] = []
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

    def write_to_transform_file(self, transform_file: Path) -> None:
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


class FieldMappingEval(BaseModel):
    """Represents the confidence score for a field mapping."""

    name: str
    """The name of the field."""

    score: float
    """The confidence score (0.00 to 1.00).

    Values defined as `MISSING` should receive a score of 0.00.
    """

    # Not used yet, so hiding to reduce cost:
    # explanation: str
    # """A short explanation of the score."""


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


def print_mapping_eval(
    mapping: FieldMapping,
    eval_result: FieldMappingEval,
    table: Table | None = None,
) -> None:
    """Print a mapping evaluation result.

    Args:
        mapping: The field mapping definition
        eval_result: The evaluation result
        table: Optional table to add the row to instead of printing directly
    """
    # Color code the confidence score based on thresholds
    confidence_str = rich_formatted_confidence(eval_result.score)

    if table:
        table.add_row(
            mapping.name,
            str(mapping.expression),
            mapping.description or "",
            confidence_str,
        )
    else:
        console.print(
            f"Field: [cyan]{mapping.name}[/cyan]"
            f" Expression: [yellow]{mapping.expression}[/yellow]"
            f" Description: [white]{mapping.description or ''}[/white]"
            f" Confidence: {confidence_str}",
        )


def print_table_mapping_analysis(
    table_mapping_eval: TableMappingEval,
    fields: list[FieldMapping],
    title: str = "Mapping Confidence Analysis",
) -> None:
    """Print a complete mapping confidence analysis.

    Args:
        confidence: The confidence evaluation results
        fields: List of field mappings
        title: Optional title for the analysis table
    """
    # Create results table
    table = Table(title=title)
    table.add_column("Field", style="cyan")
    table.add_column("Expression", style="yellow")
    table.add_column("Description", style="white")
    table.add_column("Confidence", justify="right")

    # Print each field evaluation
    for field_eval in table_mapping_eval.field_mapping_evals:
        field_data = next((f for f in fields if f.name == field_eval.name), {})
        print_mapping_eval(
            field_data,
            field_eval,
            table,
        )

    # Print results
    console.print(
        f"\nOverall Confidence Score: {rich_formatted_confidence(table_mapping_eval.score)}",
    )
    console.print("\nExplanation:")
    console.print(f"\n{table_mapping_eval.explanation}", style="italic")
    console.print("\nField-by-Field Analysis:")
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
        source_tables = text_utils.load_yaml_file(source_file)["sources"][0]["tables"]
        return [
            cls(
                name=table["name"],
                description=table.get("description", None),
                column_names=[column["name"] for column in table["columns"]],
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

    def as_rich_table(self) -> rich.table.Table:
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
