# Contributing Guide

This project uses modern Python tooling:

- `uv` for package management
- `ruff` for linting and formatting
- `pytest` for testing
- `basedpyright` for type checking
- `poethepoet` for task running

## Setup Development Environment

Most commands can be run with poe. To view the available commands, simply run `poe` on its own. If you need to install poe, you can do so with `pipx install poethepoet` or `uv tool install poethepoet`.

Use the list of `poe` tasks to get started; then you can invoke invidual tools by examining the definitions within `poe_tasks.toml`.

```bash
# Install Poe if not yet installed:
uv tool install poethepoet

# Install the project and dependencies in its dedicated `.venv` virtualenv:
poe install

# View other available poe tasks and their descriptions:
poe

...
```
