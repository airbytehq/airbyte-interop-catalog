"""Mapping confidence evaluation using Marvin AI."""

from typing import TypeVar

from rich.console import Console
from rich.table import Table

from morph import models
from morph.ai import functions as ai_fn
from morph.utils import rich_utils
from morph.utils.retries import with_retry

console = Console()

T = TypeVar("T")

MAX_RETRIES = 3


@with_retry()
def get_table_mapping_eval(
    field_mappings: list[models.FieldMapping],
) -> models.TableMappingEval:
    """Get confidence score for a mapping configuration.

    Args:
        fields: List of field mappings

    Returns:
        TableMappingEval object with confidence score and explanation

    Raises:
        Exception: If all retries fail
    """
    latest_exception = None

    # TODO: We should enforce "strict" mode here, so that the LLM always generates valid JSON output.
    # For now, we retry blindly because the AI is not always reliable at generating the JSON output.
    max_retries = 5
    result = None
    for attempt in range(max_retries):
        try:
            result = ai_fn.evaluate_mapping_confidence(field_mappings)
            break
        except Exception as e:
            latest_exception = e
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(
                    f"Failed to evaluate mapping confidence after {max_retries} attempts",
                ) from e

    if not result:
        raise latest_exception

    return result


def print_mapping_eval(
    mapping: models.FieldMapping,
    eval_result: models.FieldMappingEval,
    table: Table | None = None,
) -> None:
    """Print a mapping evaluation result.

    Args:
        mapping: The field mapping definition
        eval_result: The evaluation result
        table: Optional table to add the row to instead of printing directly
    """
    # Color code the confidence score based on thresholds
    confidence_str = rich_utils.rich_formatted_confidence(eval_result.score)

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
    table_mapping_eval: models.TableMappingEval,
    fields: list[models.FieldMapping],
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
        f"\nOverall Confidence Score: {rich_utils.rich_formatted_confidence(table_mapping_eval.score)}",
    )
    console.print("\nExplanation:")
    console.print(f"\n{table_mapping_eval.explanation}", style="italic")
    console.print("\nField-by-Field Analysis:")
    console.print(table)
