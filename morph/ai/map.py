"""Mapping confidence evaluation using Marvin AI."""

from marvin import fn as ai_fn

from morph.ai import models


@ai_fn
def select_best_match_source_schema(
    target_schema: models.DbtSourceTable,
    source_schemas: list[models.DbtSourceTable],
) -> str | models.NoConfidenceChoice:
    """Select the name of the source schema that is most similar to the target schema.

    Args:
        target_schema: The target schema to map to
        source_schemas: A list of source schemas to choose from

    Returns:
        The name of the source schema that is most similar to the target schema
        or a NoConfidenceChoice if the AI does not have any good options to choose from.
    """
    # This function will be implemented by Marvin AI
    pass


@ai_fn
def generate_mapping(
    target_schema: models.DbtSourceTable,
    source_schemas: list[models.DbtSourceTable],
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


def get_best_match_source_schema(
    target_schema: models.DbtSourceTable,
    source_schemas: list[models.DbtSourceTable],
) -> str | models.NoConfidenceChoice:
    """Get the name of the best match source schema.

    Args:
        target_schema: The target schema to map to
        source_schemas: A list of source schemas to choose from

    Returns:
        The name of the source schema that is most similar to the target schema
        or a NoConfidenceChoice if the AI does not have any good options to choose from.

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
            result = select_best_match_source_schema(target_schema, source_schemas)
            break
        except Exception as e:
            latest_exception = e
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(
                    f"Failed to evaluate mapping confidence after {max_retries} attempts.",
                ) from e

    if not result:
        raise latest_exception

    return result


def create_mappings_from_source_schema(
    target_schema: models.DbtSourceTable,
    source_schema: models.DbtSourceTable,
) -> list[models.FieldMapping]:
    """Create a list of field mappings from a source schema."""
