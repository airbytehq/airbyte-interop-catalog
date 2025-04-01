"""AI functions for Morph."""

import marvin

from morph import models
from morph.utils.retries import with_retry

VERBOSE_MODE = False

if not VERBOSE_MODE:
    marvin.settings.enable_default_print_handler = False


CONFIDENCE_INSTRUCTIONS = """
When evaluating confidence:
  - Consider "MISSING" to be a 0.0 confidence score.
  - Highest confidence score is 1.0, meaning the mapping is perfect.
  - Never give a score above 0.7 if the two columns could likely be referring to different things.
  - If you cannot find a good match for a specific column, set its expression to "MISSING".
  - Don't suggest mappings for fields that are not 0.6 or higher.
  - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
"""

FIELD_MAPPING_INSTRUCTIONS = """
When generating mappings:
    - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
    - If you cannot find a good match for a specific column, set its expression to "MISSING".
    - Don't suggest mappings for fields that are not 0.6 or higher.
    - If you have identical options at top-level or nested level, you should return the top one.
      For instance, between `property_company_id` and `property.company.id`, you should choose
      `property_company_id`.
    - Do not penalize confidence scores for differences in casing, such as camel case vs snake case.
"""

TABLE_MAPPING_INSTRUCTIONS = """
When evaluating the mapping configuration:
    - Consider "MISSING" to be a 0.0 confidence score.
    - Highest confidence score is 1.0, meaning the mapping is perfect.
    - Never give a score above 0.7 if the two tables could likely be referring to different things.
    - Do not penalize confidence scores for differences in singular vs plural of the same terms.
    - Do not penalize confidence scores for differences in casing, such as camel case vs snake case.
"""


@with_retry(max_retries=2)
@marvin.fn(
    instructions=CONFIDENCE_INSTRUCTIONS,
)  # pyright: ignore [reportUntypedFunctionDecorator]
def evaluate_mapping_confidence(
    mappings: list[models.FieldMapping],
) -> models.TableMappingEval:
    """Evaluate the confidence of a field mapping configuration.

    Args:
        mappings: List of field mappings to evaluate

    Returns:
        TableMappingEval object containing:
        - score: Overall confidence score (0.00 to 1.00)
        - explanation: Detailed explanation of the score
        - field_mapping_evals: Individual confidence scores per field
    """
    # This function will be implemented by Marvin AI
    ...


@marvin.fn
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
@marvin.fn(instructions=FIELD_MAPPING_INSTRUCTIONS)  # pyright: ignore [reportUntypedFunctionDecorator]
def generate_mappings(
    fields_to_populate: list[models.FieldMapping],
    source_schema: models.DbtSourceTable,
) -> list[models.FieldMappingSuggestion]:
    """Generate mappings for a list of fields.

    Keep in mind this guidance:
    - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
    - If you cannot find a good match for a specific column, set it's expression to exactly
      "MISSING" with no table prefix.

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


@marvin.fn(instructions=TABLE_MAPPING_INSTRUCTIONS)  # pyright: ignore [reportUntypedFunctionDecorator]
def infer_best_match_source_stream_name_short_list(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMatchingSuggestionShortList:
    """Get the name of the top 3-5 source tables based on the source and target table summaries.

    You are trying to find the source tables which are most similar to the target table in content,
    meaning, and structure.
    """
    # This function will be implemented by Marvin AI
    ...
