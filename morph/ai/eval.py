"""Mapping confidence evaluation using Marvin AI."""

from typing import TypeVar, cast

from rich.console import Console

from morph import models, resources
from morph.ai import functions as ai_fn
from morph.constants import DEFAULT_PROJECT_NAME

console = Console()

T = TypeVar("T")

MAX_RETRIES = 3


def evaluate_transforms(
    source_name: str,
    project_name: str = DEFAULT_PROJECT_NAME,
    *,
    do_source_annotations: bool = True,
) -> None:
    # Construct the path to the transforms directory
    transforms_dir = resources.get_transforms_dir(
        source_name=source_name,
        project_name=project_name,
    )

    if not transforms_dir.exists():
        console.print(f"[red]Error: Transforms directory not found at {transforms_dir}[/red]")
        return

    # Find all YAML files
    yaml_files = list(transforms_dir.glob("**/*.yml")) + list(transforms_dir.glob("**/*.yaml"))

    if not yaml_files:
        console.print(f"[yellow]No YAML files found in {transforms_dir}[/yellow]")
        return

    # Process each YAML file
    for yaml_file in sorted(yaml_files):
        console.print(f"\n[bold]Evaluating {yaml_file}[/bold]\n")
        transform_obj = models.TransformDefinition.from_file(yaml_file)

        # Get confidence score
        table_mapping_eval = cast(
            models.TableMappingEval,
            ai_fn.evaluate_mapping_confidence(
                transform_obj.field_mappings,
            ),
        )

        # Print analysis
        transform_obj.attach_evaluation(table_mapping_eval)
        transform_obj.print_as_rich_table()

        if do_source_annotations:
            transform_obj.to_file()
