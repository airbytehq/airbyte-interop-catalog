"""Utilities for retries."""

from functools import wraps
from time import sleep, time
from typing import Any, Callable, TypeVar

from rich.console import Console

console = Console()

T = TypeVar("T")
MAX_RETRIES = 3


def with_retry(
    max_retries: int = MAX_RETRIES,
    backoff_factor: float = 0.0,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator that adds retry logic with exponential backoff to a function.

    Args:
        max_retries: Maximum number of retry attempts
        backoff_factor: Factor for exponential backoff (default: 2.0)

    Returns:
        Decorated function with retry logic
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            latest_exception = None
            start_time = time()
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    elapsed = time() - start_time
                    console.print(
                        f"[white]Success on attempt {attempt + 1} after {elapsed:.2f} seconds.[/white]",
                        style="italic",
                    )
                    return result
                except Exception as e:
                    console.print(f"[yellow]Failed on attempt {attempt + 1}: {e}[/yellow]")
                    latest_exception = e
                    if attempt == max_retries - 1:  # Last attempt
                        raise Exception(f"Failed after {max_retries} attempts") from e

                    sleep(backoff_factor**attempt)  # Exponential backoff

            raise latest_exception

        return wrapper

    return decorator
