"""Models for AI-related functionality."""

from pydantic import BaseModel
from rich.console import Console
from rich.table import Table

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

    data_type: str
    """The data type of the column."""


class DbtSourceTable(BaseModel):
    """Represents a source table schema in a dbt project."""

    name: str
    """The name of the table."""

    description: str | None = None
    """A description of the table."""

    columns: list[DbtSourceColumn]
    """The columns in the table."""


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


class TableMapping(BaseModel):
    """Represents a table mapping with its properties."""

    source_stream_name: str
    """The name of the source table."""

    target_table_name: str
    """The name of the target table."""

    field_mappings: list[FieldMapping]
    """The field mappings for the table."""


class FieldMappingEval(BaseModel):
    """Represents the confidence score for a field mapping."""

    name: str
    """The name of the field."""

    score: float
    """The confidence score (0.00 to 1.00).

    Values defined as `MISSING` should receive a score of 0.00.
    """

    # Not used yet, so hiding to reduce cost:
    # explanation: str  # noqa: ERA001
    # """A short explanation of the score."""


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
        f"\nOverall Confidence Score: {rich_formatted_confidence(table_mapping_eval.score)}"
    )
    console.print("\nExplanation:")
    console.print(f"\n{table_mapping_eval.explanation}", style="italic")
    console.print("\nField-by-Field Analysis:")
    console.print(table)
