"""Utility functions for markdown formatting."""

from morph.utils.rich_utils import CONFIDENCE_HIGH, CONFIDENCE_LOW


def markdown_formatted_confidence(score: float) -> str:
    """Format a confidence score with markdown emphasis.

    Args:
        score: The confidence score to format

    Returns:
        A markdown formatted string representing the confidence score
    """
    if score > CONFIDENCE_HIGH:
        return f"🟢 _{score:.2f}_"  # Bold for high confidence

    if score < CONFIDENCE_LOW:
        return f"❌ _{score:.2f}_"  # Red for low confidence

    return f"⚠️ _{score:.2f}_"  # Normal for medium confidence


def create_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Create a markdown table from headers and rows.

    Args:
        headers: List of column headers
        rows: List of rows, where each row is a list of cell values

    Returns:
        A markdown formatted table as a string
    """
    if not headers or not rows:
        return ""

    # Create header row
    table = "| " + " | ".join(headers) + " |\n"

    # Create separator row
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Create data rows
    for row in rows:
        # Ensure row has same number of columns as headers
        while len(row) < len(headers):
            row.append("")
        table += (
            "| "
            + " | ".join([str(cell).replace("\n", " ").replace("|", "\\|") for cell in row])
            + " |\n"
        )

    return table


def create_markdown_section(title: str, content: str, level: int = 2) -> str:
    """Create a markdown section with a header and content.

    Args:
        title: The section title
        content: The section content
        level: The header level (1-6)

    Returns:
        A markdown formatted section as a string
    """
    header = "#" * level
    return f"{header} {title}\n\n{content}\n"
