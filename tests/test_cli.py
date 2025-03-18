"""Tests for the CLI module."""

from click.testing import CliRunner

from morph.cli import main


def test_cli_version():
    """Test the CLI version command."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()
