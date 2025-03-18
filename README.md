# Morph

A Python library for data transformation.

## Installation

```bash
pip install morph
```

## Usage

See the [Usage Guide](USAGE.md) for detailed instructions on how to use Morph, including examples for generating dbt projects from mapping files.

```python
import morph

# Example usage will be added here
```

## Development

This project uses modern Python tooling:

- `uv` for package management
- `ruff` for linting and formatting
- `pytest` for testing
- `basedpyright` for type checking
- `poethepoet` for task running

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/airbytehq/morph.git
cd morph

# Install dependencies with uv
uv pip install -e ".[dev]"

# Run tests
poe test
```

## License

Elastic License 2.0 (ELv2)
