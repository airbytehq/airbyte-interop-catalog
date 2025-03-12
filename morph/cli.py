"""Command-line interface for Morph."""

import click
from rich.console import Console

from morph.transform import apply_transform, read_file, write_file

console = Console()


@click.group()
@click.version_option()
def main() -> None:
    """Morph: A Python library for data transformation."""
    pass


@main.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option(
    "--transform-type",
    "-t",
    type=click.Choice(["uppercase_keys", "lowercase_keys", "flatten"]),
    default="flatten",
    help="Type of transformation to apply",
)
def transform(
    input_file: str,
    output: str | None = None,
    transform_type: str = "flatten",
) -> None:
    """Transform data from INPUT_FILE.

    Examples:
        morph transform data.json --transform-type=uppercase_keys
        morph transform data.csv --output=transformed.json
    """
    console.print(
        f"Transforming data from [bold]{input_file}[/bold] using [green]{transform_type}[/green]",
    )

    try:
        # Read input data
        data = read_file(input_file)

        # Apply transformation
        transformed_data = apply_transform(data, transform_type)

        # Write output
        if output:
            console.print(f"Writing output to [bold]{output}[/bold]")
            write_file(transformed_data, output)
        else:
            console.print("[bold]Transformed data:[/bold]")
            write_file(transformed_data)

        console.print("[bold green]Transformation completed successfully![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e!s}")
        raise click.Abort() from e


if __name__ == "__main__":
    main()
