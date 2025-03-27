"""Mapping confidence evaluation using Marvin AI."""

from marvin import fn as ai_fn
from rich.console import Console

from morph.ai import models
from morph.utils import resource_paths
from morph.utils.logic import if_none
from morph.utils.retries import with_retry
from morph.utils.transform_scaffold import generate_mapping_file

console = Console()


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


@with_retry(max_retries=3)
def get_best_match_source_stream_name(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMappingSuggestion:
    """Get the name of the best match source table based on the source and target table summaries.

    Args:
        target_schema: The target schema to map to
        source_tables: A list of source tables to choose from

    Returns:
        A SourceTableMappingSuggestion object.

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


def generate_table_mappings(
    source_name: str,
    project_name: str,
    *,
    transform_name: str,
    source_table: str | None = None,
    auto_confirm: bool | None = None,
) -> None:
    auto_confirm = if_none(auto_confirm, False)

    # Find the YAML file
    yaml_file = resource_paths.get_transform_file(
        source_name,
        project_name=project_name,
        transform_name=transform_name,
    )

    if not yaml_file.exists():
        console.print(f"[yellow]No YAML file found for target table {transform_name}[/yellow]")
        generate_mapping_file(
            source_name=source_name,
            project_name=project_name,
            table_name=transform_name,
            parent_folder=resource_paths.get_transforms_dir(
                source_name=source_name,
                project_name=project_name,
            ),
        )

    # Extract fields from dbt transform format
    current_mapping = models.TableMapping.read_from_transform_file(yaml_file)
    print(current_mapping)

    # Get all source schemas
    dbt_source_file_path = resource_paths.get_generated_sources_yml_path(
        source_name=source_name,
        project_name=project_name,
    )
    if not dbt_source_file_path.exists():
        models.generate_dbt_sources_yml_from_airbyte_catalog(
            source_name=source_name,
            project_name=project_name,
        )

    if not dbt_source_file_path.exists():
        console.print(
            f"[red]Error: Could not generate dbt sources.yml file at {dbt_source_file_path}[/red]",
        )
        return

    if not source_table:
        # We need the AI to suggest a source table

        target_table_schemas = models.SourceTableSummary.from_dbt_source_file(
            resource_paths.get_dbt_sources_requirements_path(
                source_name=source_name,
                project_name=project_name,
            ),
        )
        target_table_schema = next(
            (t for t in target_table_schemas if t.name == transform_name),
            None,
        )
        if not target_table_schema:
            console.print(f"[red]Error: Could not find target table {transform_name}[/red]")
            return

        source_tables: list[models.SourceTableSummary] = (
            models.SourceTableSummary.from_dbt_source_file(
                dbt_source_file_path,
            )
        )

        suggested_source_table = get_best_match_source_stream_name(
            target_schema=transform_name,
            source_tables=source_tables,
        )
        source_table = suggested_source_table.suggested_source_table_name

    # Ask user to confirm mapping
    confirm_mapping = "y"
    if not auto_confirm:
        confirm_mapping = input(
            f"The table is currently mapped to `{current_mapping.source_stream_name}`. "
            f"Do you want to apply the proposed mapping to use `{source_table}` instead? "
            "All existing mappings will be reset to `MISSING` and a new set of mappings will be generated. "
            "Continue? (y/n)",
        )

    if confirm_mapping == "y":
        print("Mapping confirmed.")
        # Apply mapping
        # Update transform file
        change_mapping_source_table(
            source_name=source_name,
            project_name=project_name,
            transform_name=transform_name,
            new_source_table=source_table,
        )
        populate_missing_mappings(
            source_name=source_name,
            project_name=project_name,
            transform_name=transform_name,
        )
        # Update lock file
        # Update dbt project
    else:
        print("Mapping rejected.")
