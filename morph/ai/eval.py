"""Mapping confidence evaluation using Marvin AI."""

from collections.abc import Callable
from functools import wraps
from time import sleep, time
from typing import Any, TypeVar

from marvin import ai_fn
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table

from morph.utils.rich_utils import rich_formatted_confidence

console = Console()

T = TypeVar("T")

MAX_RETRIES = 3


def with_retry(
    max_retries: int = MAX_RETRIES,
    backoff_factor: float = 0.0,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator that adds retry logic with exponential backoff to a function.

    Args:
        max_retries: Maximum number of retry attempts
        backoff_factor: Factor for exponential backoff (default: 2.0)

    Returns:
        Decorated function with retry logic
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            latest_exception = None
            start_time = time()
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    elapsed = time() - start_time
                    console.print(
                        f"[white]Success on attempt {attempt + 1} after {elapsed:.2f} seconds.[/white]",
                        style="italic",
                    )
                    return result
                except Exception as e:
                    console.print(f"[yellow]Failed on attempt {attempt + 1}: {e}[/yellow]")
                    latest_exception = e
                    if attempt == max_retries - 1:  # Last attempt
                        raise Exception(f"Failed after {max_retries} attempts") from e

                    sleep(backoff_factor**attempt)  # Exponential backoff

            raise latest_exception

        return wrapper

    return decorator


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    """The name of the field."""

    expression: str | bool | float | int
    """The expression to evaluate."""

    description: str | None = None
    """A description of the field."""

    tests: list[dict[str, str]] | None = None


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


class MappingConfidence(BaseModel):
    """Represents the confidence score and explanation for a mapping."""

    score: float
    """The overall confidence score (0.00 to 1.00)."""

    explanation: str
    """A detailed explanation of the overall score."""

    field_evals: list[FieldMappingEval]
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


def print_mapping_analysis(
    confidence: MappingConfidence,
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
    for field_eval in confidence.field_evals:
        field_data = next((f for f in fields if f.name == field_eval.name), {})
        print_mapping_eval(
            field_data,
            field_eval,
            table,
        )

    # Print results
    console.print(f"\nOverall Confidence Score: {rich_formatted_confidence(confidence.score)}")
    console.print("\nExplanation:")
    console.print(f"\n{confidence.explanation}", style="italic")
    console.print("\nField-by-Field Analysis:")
    console.print(table)


@ai_fn
def evaluate_mapping_confidence(
    mappings: list[FieldMapping],
) -> MappingConfidence:
    """Evaluate the confidence of a field mapping configuration.

    Args:
        fields: List of field mappings to evaluate

    Returns:
        MappingConfidence object containing:
        - score: Overall confidence score (0.00 to 1.00)
        - explanation: Detailed explanation of the score
        - field_evals: Individual confidence scores per field
    """
    # This function will be implemented by Marvin AI
    pass


@with_retry()
def get_mapping_confidence(
    mappings: list[FieldMapping],
) -> MappingConfidence:
    """Get confidence score for a mapping configuration.

    Args:
        fields: List of field mappings

    Returns:
        MappingConfidence object with confidence score and explanation

    Raises:
        Exception: If all retries fail
    """
    return evaluate_mapping_confidence(mappings)
