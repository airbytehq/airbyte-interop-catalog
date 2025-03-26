"""Mapping confidence evaluation using Marvin AI."""

from marvin import fn as ai_fn

from morph.ai import models
from morph.utils import resource_paths
from morph.utils.retries import with_retry


@ai_fn
def select_best_match_source_schema(
    target_schema: models.DbtSourceTable,
    source_schemas: list[models.DbtSourceTable],
) -> models.SourceTableMappingSuggestion:
    """Select the name of the source stream that is most similar to the target table schema.

    You should consider the name of the source stream, the name of the target table, and the
    degree of overlap in the column definitions of the source and target.

    Args:
        target_schema: The target schema to map to
        source_schemas: A list of source schemas to choose from

    Returns:
        A SourceTableMappingSuggestion object containing:
        - target_table_name: The name of the target table.
        - suggested_source_table_name: The name of the source table suggested by the AI.
        - confidence_score: The confidence score for the mapping of the source table to the target table.
        - explanation: A detailed explanation of the confidence score.
        - next_best_source_table_name: The next-best match for the source table.
        - next_best_source_table_confidence_score: The confidence score for the next-best match for the source table.
    """
    # This function will be implemented by Marvin AI
    pass


@ai_fn
def generate_mappings(
    fields_to_populate: list[models.FieldMapping],
    source_schema: models.DbtSourceTable,
) -> list[models.FieldMappingSuggestion]:
    """Generate mappings for a list of fields.

    Args:
        fields_to_populate: A list of fields to populate.
        source_schema: The source schema to populate the fields from.

    Returns:
        A list of FieldMapping objects containing:
        - name: The name of the field.
        - expression: The expression to populate the field with.
        - description: The description of the field.
        - field_mapping_confidence_scores: The confidence scores for the mapping of fields from the source stream to the target table.
    """
    # This function will be implemented by Marvin AI
    pass


def change_mapping_source_table(
    source_name: str,
    project_name: str,
    transform_name: str,
    new_source_table: str,
) -> None:
    """Change the source table for a given transform.

    This will also reset the field mappings to the default `MISSING`.
    """
    transform_file = resource_paths.get_transform_file(
        source_name=source_name,
        project_name=project_name,
        transform_name=transform_name,
    )
    transform_parsed = models.TableMapping.read_from_transform_file(transform_file)
    transform_parsed.source_stream_name = new_source_table
    new_transform_file_content = models.TableMapping(
        source_name=source_name,
        project_name=project_name,
        transform_name=transform_name,
        source_stream_name=new_source_table,
        target_table_name=transform_name,
        field_mappings=[
            models.FieldMapping(
                name=field.name,
                expression="MISSING",
                description=field.description,
            )
            for field in transform_parsed.field_mappings
        ],
    )
    new_transform_file_content.write_to_transform_file(transform_file)


@with_retry(max_retries=2)
def get_best_match_source_stream_name(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMappingSuggestion:
    """Get the name of the best match source table based on the source and target table summaries.

    Args:
        target_schema: The target schema to map to
        source_tables: A list of source tables to choose from

    Returns:
        A SourceTableMappingSuggestion object containing:
        - target_table_name: The name of the target table.
        - suggested_source_table_name: The name of the source table suggested by the AI.
        - confidence_score: The confidence score for the mapping of the source table to the target table.
        - explanation: A detailed explanation of the confidence score.
        - next_best_source_table_name: The next-best match for the source table.
        - next_best_source_table_confidence_score: The confidence score for the next-best match for the source table.

    Raises:
        Exception: If all retries fail
    """
    return select_best_match_source_schema(target_schema, source_tables)


def create_mappings_from_source_schema(
    target_schema: models.DbtSourceTable,
    source_schema: models.DbtSourceTable,
) -> list[models.FieldMapping]:
    """Create a list of field mappings from a source schema."""


def populate_missing_mappings(
    source_name: str,
    project_name: str,
    transform_name: str,
) -> None:
    """Populate missing mappings from a source schema."""
    transform_file = resource_paths.get_transform_file(
        source_name=source_name,
        project_name=project_name,
        transform_name=transform_name,
    )
    transform_parsed = models.TableMapping.read_from_transform_file(transform_file)
    fields_to_populate = []

    source_table_info = models.SourceTableSummary.from_dbt_source_file(
        source_file=resource_paths.get_generated_sources_yml_path(
            source_name=source_name,
            project_name=project_name,
        ),
    )
    source_schema: models.SourceTableSummary = next(
        (table for table in source_table_info if table.name == transform_parsed.source_stream_name),
        None,
    )
    if source_schema is None:
        raise ValueError(f"Source schema not found for {transform_parsed.source_stream_name}")

    # Populate missing mappings
    for field in transform_parsed.field_mappings:
        if field.expression == "MISSING":
            fields_to_populate.append(field)

    # Generate new mappings
    new_mapping_suggestions: list[models.FieldMappingSuggestion] = generate_mappings(
        fields_to_populate=fields_to_populate,
        source_schema=source_schema,
    )
    for suggested_field in new_mapping_suggestions:
        for existing_field in transform_parsed.field_mappings:
            if existing_field.name == suggested_field.target_field_name:
                existing_field.expression = (
                    f"{source_schema.name}.{suggested_field.source_field_name}"
                )

    transform_parsed.write_to_transform_file(transform_file)
