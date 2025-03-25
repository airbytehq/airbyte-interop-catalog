"""Utility functions for rich."""

CONFIDENCE_HIGH = 0.65
CONFIDENCE_LOW = 0.35


def rich_formatted_confidence(score: float) -> str:
    """Format a confidence score with color."""
    if score > CONFIDENCE_HIGH:
        return f"[green]{score:.2f}[/green]"

    if score < CONFIDENCE_LOW:
        return f"[red]{score:.2f}[/red]"

    return f"[yellow]{score:.2f}[/yellow]"
