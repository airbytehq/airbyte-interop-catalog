"""AI functions for Morph."""

import marvin

from morph import models

VERBOSE_MODE = False

if not VERBOSE_MODE:
    marvin.settings.enable_default_print_handler = False


agent = marvin.Agent(
    name="morph-ai",
    description="AI agent for Morph.",
    model="gpt-4",
    verbose=VERBOSE_MODE,
)


PROJECT_CONTEXT = """
Project Context: You are fulfilling the role of a data engineer creating logic for mapping source
data from Airbyte into a target schema that should be interoperable with a similar schema from
Fivetran.

Many of the upstream source APIs are shared across these two implementations, and the schemas are
similar, but not identical. Your task is to create a mapping configuration that will allow for
transforming data from the source schema to the target schema, while maintaining the integrity and
meaning of the data.

It is acceptable to make fuzzy matches, but you should not pair any clearly different fields or
tables together based on text similarities alone. For example, "tax_line_items" is not the same as
"orders" or "transactions", and a reasonable person would not equate them - whereas in "accounts"
"customer_accounts" are very likely to be the same thing, if there's no closer match available.

Similarly, "customer_id" and "user_id" are not the same thing, but "customer_id" and
"customer_account_id" are likely the same thing. You should not penalize for casing differences,
but you should penalize for differences in meaning. For example, "customer_id" and "customerId"
are likely the same thing, but "customer_id" and "customer_address_id" are not.
"""

GENERAL_CONFIDENCE_INSTRUCTIONS = """
When evaluating table and field mappings generally:
  - If you cannot find a good match for a specific table or column, set its expression to "MISSING".
  - Consider "MISSING" to be a 0.00 confidence score.
  - The highest confidence score is 1.00, meaning the mapping is perfect.
  - Don't suggest mappings for fields or tables that are not likely, for instance 0.50 or higher.
  - Never give a score above 0.70 if the tables or columns could likely be referring to different
    things.
    - E.g. "region", "sales_region", and "customer_region" may or may not refer to the same thing,
      so at best, a score between 0.50 and 0.70 would be appropriate.
    - A score over 0.70 when the mapping is uncertain would require strong contextual evidence that
      the two things are the same.
  - Never penalize confidence scores for casing or for differences in singular vs plural of the
    same terms.
    - E.g. consider "user" and "users" to be the same, as well as "Address" and "address".
"""

FIELD_MAPPING_INSTRUCTIONS = """
When generating field-level mappings:
    - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
      - This mapping always gets a score of 1.00, but otherwise, there is no reward or penalty for
        this, since it is a standard mapping for all tables.
    - Don't suggest mappings for fields that are not 0.6 or higher.
    - If you cannot find a good match for a specific column, set its expression to "MISSING".
    - If you have identical options at top-level or nested level, you should return the top one.
      - For instance, between `property_company_id` and `property.company.id`, you should choose
        `property_company_id`.
    - Do not penalize confidence scores for differences in casing, such as camel case vs snake case.
    - When explaining 'MISSING' mappings, you can keep it simple and say exactly "No good match
      found.".

When evaluating field-level mappings:
  - You should always map `_fivetran_synced` to a source stream's `_airbyte_extracted_at` column.
"""

TABLE_MAPPING_INSTRUCTIONS = """
When evaluating table matching:

You will grade the table mapping based on the following criteria:
  - Table Match Score: The **quality** of the table matching itself. The relative confidence
    that the source and target tables are describing the same subject matter.
  - Completion Score: The completion rating for population of field mappings.
A scenario where table match score can be high, while the completion score is still low,
would be when both source and target endpoints are generated from the same API, but the source
implementation does not serialize all of the fields that the target implementation does.
"""


@marvin.fn(
    agent=agent,
    instructions="\n\n".join(
        [
            PROJECT_CONTEXT,
            GENERAL_CONFIDENCE_INSTRUCTIONS,
            TABLE_MAPPING_INSTRUCTIONS,
            FIELD_MAPPING_INSTRUCTIONS,
        ],
    ),
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


@marvin.fn(
    agent=agent,
    instructions="\n\n".join(
        [
            PROJECT_CONTEXT,
            GENERAL_CONFIDENCE_INSTRUCTIONS,
            TABLE_MAPPING_INSTRUCTIONS,
        ],
    ),
)  # pyright: ignore [reportUntypedFunctionDecorator]
def select_best_match_source_schema(
    target_table_schema: models.SourceTableSummary,
    source_table_schemas: list[models.SourceTableSummary],
) -> models.SourceTableMappingTopTwoSuggestions:
    """Select the name of the source stream that is most similar to the target table schema.

    You should consider the name of the source stream, the name of the target table, and the
    degree of overlap in the column definitions of the source and target.

    Args:
        target_table_schema: The target schema to map to
        source_table_schemas: A list of source schemas to choose from

    Returns:
        A SourceTableMappingTopTwoSuggestions object.
    """
    # This function will be implemented by Marvin AI
    ...


@marvin.fn(
    agent=agent,
    instructions="\n\n".join(
        [
            PROJECT_CONTEXT,
            GENERAL_CONFIDENCE_INSTRUCTIONS,
            TABLE_MAPPING_INSTRUCTIONS,
            FIELD_MAPPING_INSTRUCTIONS,
        ],
    ),
)  # pyright: ignore [reportUntypedFunctionDecorator]
def generate_mappings(
    fields_to_populate: list[models.FieldMapping],
    source_schema: models.DbtSourceTable | models.SourceTableSummary,
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


@marvin.fn(
    agent=agent,
    instructions="\n\n".join(
        [
            PROJECT_CONTEXT,
            GENERAL_CONFIDENCE_INSTRUCTIONS,
            TABLE_MAPPING_INSTRUCTIONS,
        ],
    ),
)  # pyright: ignore [reportUntypedFunctionDecorator]
def infer_best_match_source_stream_name_short_list(
    target_table_description: models.SourceTableSummary,
    available_source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMappingSuggestionShortList:
    """Get the name of the top 3-5 source tables based on the source and target table summaries.

    You are trying to find the source tables which are most similar to the target table in content,
    meaning, and structure.
    """
    # This function will be implemented by Marvin AI
    ...
