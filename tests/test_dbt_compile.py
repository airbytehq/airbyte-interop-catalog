"""Tests for dbt compile functionality."""

import os
import subprocess
import tempfile
from pathlib import Path

import pytest

from morph.utils.mapping_to_dbt_models import generate_dbt_package


def test_dbt_compile_generated_project():
    """Test that a generated dbt project can be compiled successfully."""
    # Skip test if dbt is not installed
    try:
        subprocess.run(["dbt", "--version"], check=True, capture_output=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        pytest.skip("dbt not installed, skipping test")
    
    # Create a temporary directory for the test
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set up test directories
        catalog_dir = Path(temp_dir) / "catalog"
        transforms_dir = catalog_dir / "transforms"
        transforms_dir.mkdir(parents=True)
        
        # Create a simple mapping file
        mapping_content = """
domain: test
transforms:
  - id: test_model
    display_name: Test Model
    from:
      source_table: test_source.test_table
    fields:
      id:
        expression: source_table.id
        description: Primary key
      name:
        expression: source_table.name
        description: Name field
"""
        mapping_file = transforms_dir / "test.yml"
        mapping_file.write_text(mapping_content)
        
        # Generate the dbt project
        output_dir = catalog_dir / "generated"
        generate_dbt_package(str(catalog_dir), str(output_dir), str(transforms_dir))
        
        # Verify the project was generated
        assert (output_dir / "dbt_project" / "dbt_project.yml").exists()
        assert (output_dir / "dbt_project" / "packages.yml").exists()
        assert (output_dir / "dbt_project" / "profiles").exists()
        assert (output_dir / "dbt_project" / "models" / "test_model.sql").exists()
        
        # Create sources.yml file
        models_dir = output_dir / "dbt_project" / "models"
        sources_content = """
version: 2

sources:
  - name: test_source
    tables:
      - name: test_table
"""
        sources_path = models_dir / "sources.yml"
        sources_path.write_text(sources_content)
        
        # Run dbt deps first to install dependencies
        os.chdir(output_dir)
        deps_result = subprocess.run(
            ["dbt", "deps", "--profiles-dir", "profiles"],
            capture_output=True,
            text=True,
        )
        assert deps_result.returncode == 0, f"dbt deps failed: {deps_result.stderr}"
        
        # Run dbt compile
        result = subprocess.run(
            ["dbt", "compile", "--profiles-dir", "profiles"],
            capture_output=True,
            text=True,
        )
        
        # Check that compilation succeeded
        assert result.returncode == 0, f"dbt compile failed: {result.stderr}"
        
        # Verify compiled SQL was generated
        assert (output_dir / "target" / "compiled").exists()
        assert any((output_dir / "target" / "compiled").glob("**/*.sql"))
