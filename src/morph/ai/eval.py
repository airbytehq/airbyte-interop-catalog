"""Mapping confidence evaluation using Marvin AI."""

from typing import TypeVar

from rich.console import Console

from morph import models
from morph.ai import functions as ai_fn
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
    return ai_fn.evaluate_mapping_confidence(field_mappings)
