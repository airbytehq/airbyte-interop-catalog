"""Mapping confidence evaluation using Pydantic AI."""

from pydantic import BaseModel
from pydantic_ai import ai_model


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    expression: str | bool | float | int
    description: str | None = None
    tests: list[dict[str, str]] | None = None


class MappingConfidence(BaseModel):
    """Represents the confidence score and explanation for a mapping."""

    score: float
    explanation: str
    field_scores: dict[str, float]


@ai_model
class MappingConfidenceEvaluator:
    """Evaluates the confidence of field mapping configurations."""

    def evaluate_mapping_confidence(
        self,
        mappings: list[FieldMapping],
    ) -> MappingConfidence:
        """Evaluate the confidence of a field mapping configuration.

        Args:
            mappings: List of field mappings to evaluate

        Returns:
            MappingConfidence object containing:
            - score: Overall confidence score (0.00 to 1.00)
            - explanation: Detailed explanation of the score
            - field_scores: Individual confidence scores per field
        """
        # This function will be implemented by Pydantic AI
        # Using mappings parameter to avoid linting warning
        _ = mappings
        # Return a placeholder to satisfy the type checker
        return MappingConfidence(
            score=0.0,
            explanation="Placeholder - will be replaced by AI implementation",
            field_scores={},
        )


def get_mapping_confidence(
    mappings: list[dict],
) -> MappingConfidence:
    """Get confidence score for a mapping configuration.

    Args:
        mappings: List of field mappings

    Returns:
        MappingConfidence object with confidence score and explanation

    Raises:
        Exception: If all retries fail
    """
    field_mappings = [FieldMapping(**mapping) for mapping in mappings]
    latest_exception = None

    # TODO: We should enforce "strict" mode here, so that the LLM always generates valid JSON output.
    # For now, we retry blindly because the AI is not always reliable at generating the JSON output.
    max_retries = 5
    result = None
    evaluator = MappingConfidenceEvaluator()
    for attempt in range(max_retries):
        try:
            result = evaluator.evaluate_mapping_confidence(field_mappings)
            break
        except Exception as e:
            latest_exception = e
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(
                    f"Failed to evaluate mapping confidence after {max_retries} attempts",
                ) from e

    if not result:
        if latest_exception:
            raise Exception("Failed to evaluate mapping confidence") from latest_exception
        raise Exception("Failed to evaluate mapping confidence - unknown error")

    return result
