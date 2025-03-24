"""Mapping confidence evaluation using Marvin AI."""

from marvin import ai_fn
from pydantic import BaseModel


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    expression: str
    description: str | None = None
    tests: list[dict[str, str]] | None = None


class MappingConfidence(BaseModel):
    """Represents the confidence score and explanation for a mapping."""

    score: float
    explanation: str
    field_scores: dict[str, float]


@ai_fn
def evaluate_mapping_confidence(
    source_type: str,
    target_type: str,
    fields: list[FieldMapping],
) -> MappingConfidence:
    """Evaluate the confidence of a field mapping configuration.

    Args:
        source_type: The source data type (e.g., "JSON", "CSV")
        target_type: The target data type (e.g., "dbt model")
        fields: List of field mappings to evaluate

    Returns:
        MappingConfidence object containing:
        - score: Overall confidence score (0.00 to 1.00)
        - explanation: Detailed explanation of the score
        - field_scores: Individual confidence scores per field
    """
    # This function will be implemented by Marvin AI
    pass


def get_mapping_confidence(
    source_type: str,
    target_type: str,
    fields: list[dict],
) -> MappingConfidence:
    """Get confidence score for a mapping configuration.

    Args:
        source_type: The source data type
        target_type: The target data type
        fields: List of field mappings

    Returns:
        MappingConfidence object with confidence score and explanation
    """
    field_mappings = [FieldMapping(**field) for field in fields]
    return evaluate_mapping_confidence(source_type, target_type, field_mappings)
