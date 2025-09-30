"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines."""
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
