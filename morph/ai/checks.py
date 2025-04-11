"""Utility functions for checking AI service requirements."""

import os
from rich.console import Console

console = Console()


def check_openai_api_key():
    """Check if OpenAI API key is set in environment variables.
    
    Raises:
        SystemExit: If the OpenAI API key is not set
    """
    if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
        console.print(
            "[bold red]Error:[/bold red] OpenAI API key is not set. "
            "Please set the OPENAI_API_KEY environment variable to use AI functionality.\n"
            "Example: [bold]export OPENAI_API_KEY=your-api-key[/bold]"
        )
        raise SystemExit(1)
