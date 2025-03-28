"""AI functions for Morph."""

from marvin import ai_fn  # type: ignore

from morph import models
from morph.utils.retries import with_retry


@ai_fn
def evaluate_mapping_confidence(
    mappings: list[models.FieldMapping],
) -> models.TableMappingEval:
    """Evaluate the confidence of a field mapping configuration.

    Args:
        mappings: List of field mappings to evaluate

    When evaluating confidence:
      - Consider "MISSING" to be a 0.0 confidence score.
      - Highest confidence score is 1.0, meaning the mapping is perfect.
      - Never give a score above 0.7 if the two columns could likely be referring to different things.

    Returns:
        TableMappingEval object containing:
        - score: Overall confidence score (0.00 to 1.00)
        - explanation: Detailed explanation of the score
        - field_mapping_evals: Individual confidence scores per field
    """
    # This function will be implemented by Marvin AI
    ...


@ai_fn
def select_best_match_source_schema(
    target_schema: models.DbtSourceTable,
    source_schemas: list[models.DbtSourceTable],
) -> models.SourceTableMappingTopTwoSuggestions:
    """Select the name of the source stream that is most similar to the target table schema.

    You should consider the name of the source stream, the name of the target table, and the
    degree of overlap in the column definitions of the source and target.

    Args:
        target_schema: The target schema to map to
        source_schemas: A list of source schemas to choose from

    Returns:
        A SourceTableMappingTopTwoSuggestions object.
    """
    # This function will be implemented by Marvin AI
    ...


@with_retry(max_retries=3)
@ai_fn
def generate_mappings(
    fields_to_populate: list[models.FieldMapping],
    source_schema: models.DbtSourceTable,
) -> list[models.FieldMappingSuggestion]:
    """Generate mappings for a list of fields.

    Keep in mind this guidance:
    - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
    - If you cannot find a good match for a specific column, set it's expression to exactly
      "MISSING" with no table prefix.

    When evaluating confidence:
      - Consider "MISSING" to be a 0.0 confidence score.
      - Never give a score above 0.7 if the two columns could be referring to different things.
      - Don't suggest mappings for fields that are not 0.6 or higher.

    Args:
        fields_to_populate: A list of fields to populate.
        source_schema: The source schema to populate the fields from.

    Returns:
        A list of FieldMapping objects containing:
        - name: The name of the field.
        - expression: The expression to populate the field with.
        - description: The description of the field.
        - field_mapping_confidence_scores: The confidence scores for the mapping of fields from the
          source stream to the target table.
    """
    # This function will be implemented by Marvin AI
    ...


@ai_fn
def infer_best_match_source_stream_name_short_list(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMappingSuggestionShortList:
    """Get the name of the top 3-5 source tables based on the source and target table summaries.

    You are trying to find the source tables which are most similar to the target table in content,
    meaning, and structure.
    """
    # This function will be implemented by Marvin AI
    ...
