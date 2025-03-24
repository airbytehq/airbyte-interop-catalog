"""Tests for the CLI module."""

from click.testing import CliRunner

from morph.cli import main


def test_cli_version():
    """Test the CLI version command."""
    runner = CliRunner()
    # Use catch_exceptions=True to catch the RuntimeError
    result = runner.invoke(main, ["--version"], catch_exceptions=True)
    # In test environments, the package might not be installed, which is fine
    # We just want to make sure the command doesn't crash with an unexpected error
    if isinstance(result.exception, RuntimeError):
        assert "'morph' is not installed" in str(result.exception)
    else:
        assert result.exit_code == 0
        assert "version" in result.output.lower()
