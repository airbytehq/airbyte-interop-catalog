"""Mapping confidence evaluation using Marvin AI."""

from marvin import ai_fn

from morph.ai import models


@ai_fn
def evaluate_mapping_confidence(
    mappings: list[models.FieldMapping],
) -> models.MappingConfidence:
    """Evaluate the confidence of a field mapping configuration.

    Args:
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
    mappings: list[dict],
) -> models.MappingConfidence:
    """Get confidence score for a mapping configuration.

    Args:
        fields: List of field mappings

    Returns:
        MappingConfidence object with confidence score and explanation

    Raises:
        Exception: If all retries fail
    """
    field_mappings = [models.FieldMapping(**mapping) for mapping in mappings]
    latest_exception = None

    # TODO: We should enforce "strict" mode here, so that the LLM always generates valid JSON output.
    # For now, we retry blindly because the AI is not always reliable at generating the JSON output.
    max_retries = 5
    result = None
    for attempt in range(max_retries):
        try:
            result = evaluate_mapping_confidence(field_mappings)
            break
        except Exception as e:
            latest_exception = e
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(
                    f"Failed to evaluate mapping confidence after {max_retries} attempts"
                ) from e

    if not result:
        raise latest_exception

    return result
