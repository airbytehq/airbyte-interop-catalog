"""Tests for the CLI module."""

from click.testing import CliRunner

from morph.cli import main


def test_cli_version():
    """Test the CLI version command."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()


def test_transform_command():
    """Test the transform command with help flag."""
    runner = CliRunner()
    result = runner.invoke(main, ["transform", "--help"])
    assert result.exit_code == 0
    assert "transform" in result.output.lower()
