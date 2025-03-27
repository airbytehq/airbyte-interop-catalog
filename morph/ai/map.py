"""Mapping confidence evaluation using Marvin AI."""

from marvin import fn as ai_fn
from rich.console import Console
from rich.prompt import Prompt

from morph import constants
from morph.ai import models
from morph.utils import resource_paths, text_utils
from morph.utils.logic import if_none
from morph.utils.retries import with_retry
from morph.utils.transform_scaffold import generate_empty_mapping_file

console = Console()

MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE = 5


@ai_fn
def ai_fn_select_best_match_source_schema(
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
    pass


@with_retry(max_retries=3)
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


@ai_fn
def ai_fn_infer_best_match_source_stream_name_short_list(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> models.SourceTableMappingSuggestionShortList:
    """Get the name of the top 3-5 source tables based on the source and target table summaries.

    You are trying to find the source tables which are most similar to the target table in content,
    meaning, and structure.
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
                expression=constants.MISSING,
                description=field.description,
            )
            for field in transform_parsed.field_mappings
        ],
    )
    new_transform_file_content.write_to_transform_file(transform_file)


@with_retry(max_retries=3)
def infer_best_match_source_stream_name_short_list(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
) -> list[models.SourceTableMappingSuggestion]:
    """Get the name of the best match source table based on the source and target table summaries.

    Args:
        target_schema: The target schema to map to
        source_tables: A list of source tables to choose from

    Returns:
        A list of SourceTableMappingSuggestion objects.
    """
    # This function will be implemented by Marvin AI
    pass


@with_retry(max_retries=3)
def infer_best_match_source_stream_name(
    target_schema: models.SourceTableSummary,
    source_tables: list[models.SourceTableSummary],
    *,
    auto_confirm: bool | None = None,
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
    _ = auto_confirm  # TODO: Implement auto-confirm
    if not isinstance(target_schema, models.SourceTableSummary):
        raise ValueError(
            f"target_schema must be a SourceTableSummary, got: {type(target_schema)}",
        )

    if not isinstance(source_tables, list):
        raise ValueError(f"source_tables must be a list, got: {type(source_tables)}")

    if not all(isinstance(table, models.SourceTableSummary) for table in source_tables):
        raise ValueError("source_tables must be a list of SourceTableSummary objects")

    console.print(f"Inferring best match source stream name for {target_schema.name}...")
    console.print(f"Source tables ({len(source_tables)}): {[s.name for s in source_tables]}")
    console.print(f"Target schema: {target_schema}")

    if len(source_tables) > MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE:
        console.print(
            f"[yellow]Warning: There are {len(source_tables)} source tables, "
            f"which is more than the maximum of {MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE}. "
            "Only the top 5 will be considered for the mapping inference. ",
        )
        console.print(
            "The next step will be to create a short list of the top 5 source tables "
            "based on table name similarity.",
        )
        # console.input("Press 'Enter' to continue...")
        console.line()
        console.print("...", style="white")
        console.line()
        source_tables_without_columns = [
            models.SourceTableSummary(
                name=s.name,
                description=s.description,
                column_names=[],
            )
            for s in source_tables
        ]
        short_list: models.SourceTableMappingSuggestionShortList = (
            ai_fn_infer_best_match_source_stream_name_short_list(
                target_schema=target_schema,
                source_tables=source_tables_without_columns,
            )
        )
        short_list_names = [s.suggested_source_table_name for s in short_list.suggestions]
        if len(short_list.suggestions) > MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE:
            console.print(
                f"Too many suggestions were returned ({len(short_list_names)}): {short_list_names}",
                f"\nWe will only consider the top 5: {short_list_names[:MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE]}",
                style="yellow",
            )
            short_list_names = short_list_names[:MAX_SOURCE_TABLE_PER_MAPPING_INFERENCE]
        else:
            console.print(
                f"The following {len(short_list_names)} source tables were returned "
                f"as potential matches for the '{target_schema.name}' target table: "
                f"[green]{', '.join(short_list_names)}[/green]",
                "\nWe will now proceed with inferring the best match from these options.",
                style="yellow",
            )

        source_tables = [s for s in source_tables if s.name in short_list_names]

    # console.input("Press 'Enter' to continue...")
    console.line()
    return ai_fn_select_best_match_source_schema(target_schema, source_tables)


def populate_missing_mappings(
    source_name: str,
    project_name: str,
    transform_name: str,
) -> None:
    """Populate missing mappings for a single target table."""
    transform_file = resource_paths.get_transform_file(
        source_name=source_name,
        project_name=project_name,
        transform_name=transform_name,
    )
    transform_parsed = models.TableMapping.read_from_transform_file(transform_file)
    fields_to_populate = []

    source_table_info = models.SourceTableSummary.from_dbt_source_file(
        source_file=resource_paths.get_generated_source_yml_path(
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
        if field.expression == constants.MISSING:
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


def infer_table_mappings(  # noqa: PLR0912 (too many branches)
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

    # Extract fields from dbt transform format
    if not yaml_file.exists():
        current_mapping_source_stream_name = constants.MISSING
    else:
        current_mapping_source_stream_name = models.TableMapping.read_from_transform_file(
            yaml_file
        ).source_stream_name

    # Get all source schemas
    dbt_source_file_path = resource_paths.get_generated_source_yml_path(
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

        suggested_source_table: models.SourceTableMappingTopTwoSuggestions | None = (
            infer_best_match_source_stream_name(
                target_schema=target_table_schema,
                source_tables=source_tables,
            )
        )

        console.print("The best match found was:")
        console.print(suggested_source_table.best_match_suggestion.as_rich_table())
        source_table = suggested_source_table.best_match_suggestion.suggested_source_table_name

        if suggested_source_table.next_best_match_suggestion:
            console.print("The next best match was:")
            console.print(suggested_source_table.next_best_match_suggestion.as_rich_table())

        # Ask user to confirm mapping
        confirm_mapping = "Y"
        if suggested_source_table and not auto_confirm:
            if current_mapping_source_stream_name == "MISSING":
                summary_text = (
                    f"The table `{target_table_schema.name}` is currently not mapped. "
                    f"\nDo you want to apply the proposed mapping to use `{source_table}`? "
                )
            elif current_mapping_source_stream_name == source_table:
                summary_text = (
                    f"The table `{target_table_schema.name}` is already mapped to the best match source table `{source_table}`. "
                    f"\n[yellow]Do you want to rebuild the mappings? "
                    "\nAll existing mappings will be reset and a new set of mappings will be generated.[/yellow]\n"
                )
            else:
                summary_text = (
                    f"The table `{target_table_schema.name}` is currently mapped to `{current_mapping_source_stream_name}`. "
                    f"\n[yellow]Do you want to apply the proposed mapping to use `{source_table}` instead? "
                    "\nAll existing mappings will be reset and a new set of mappings will be generated.[/yellow]\n"
                )

            confirm_mapping = Prompt.ask(
                "\n\n"
                + summary_text
                + "\n"
                + "Press `Enter` to continue using the best match ('n' to skip, or 'a' to abort)...",
                choices=["Y", "n", "a"],
                default="Y",
                case_sensitive=False,
            )

        if confirm_mapping == "a":
            raise Exception("Aborting")

        if confirm_mapping == "n":
            console.print("Mapping rejected.", style="red")
            add_skipped_target_table(
                source_name=source_name,
                project_name=project_name,
                transform_name=transform_name,
            )
            return

        if suggested_source_table is not None:
            source_table = suggested_source_table.best_match_suggestion.suggested_source_table_name

    if source_table is None:
        return

    console.print("Mapping confirmed.", style="green")

    if not yaml_file.exists():
        console.print(
            summary_text + f"[yellow]No YAML file found for target table {transform_name}[/yellow]",
        )
        generate_empty_mapping_file(
            source_name=source_name,
            project_name=project_name,
            table_name=transform_name,
            parent_folder=resource_paths.get_transforms_dir(
                source_name=source_name,
                project_name=project_name,
            ),
        )

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


def get_skipped_target_tables(
    source_name: str,
    project_name: str,
) -> list[str]:
    """Get the list of skipped tables from the config file."""
    config_file = resource_paths.get_config_file_path(
        source_name=source_name,
        project_name=project_name,
    )
    config = text_utils.load_yaml_file(config_file)
    return config.get("target_tables_skipped", [])


def add_skipped_target_table(
    source_name: str,
    project_name: str,
    transform_name: str,
) -> None:
    """Add a skipped table to the config file."""
    config_file = resource_paths.get_config_file_path(
        source_name=source_name,
        project_name=project_name,
    )
    config = text_utils.load_yaml_file(config_file)
    skipped_tables = config.get("target_tables_skipped", [])
    if transform_name not in skipped_tables:
        skipped_tables.append(transform_name)
        config["target_tables_skipped"] = sorted(skipped_tables)
        text_utils.dump_yaml_file(config, config_file)
