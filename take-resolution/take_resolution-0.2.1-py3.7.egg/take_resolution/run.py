# -*- coding: utf-8 -*-
__author__ = 'Gabriel Salgado'
__version__ = '0.1.0'

import typing as tp
import pathlib as pl
from kedro.framework.context import KedroContext
from kedro.framework.context import load_package_context
from kedro.pipeline import Pipeline
from take_resolution.pipeline import create_pipelines


class ProjectContext(KedroContext):
    """Context class for this package.

    Example:
    ::
    >>> from take_resolution.run import ProjectContext
    >>> context = ProjectContext('project_path')
    >>> context.run()

    Or with file ``.kedro.yml`` specifying template context as project context
    ::
        context_path: template.run.ProjectContext

    Example:
    ::
    >>> from kedro.context import load_context
    >>> context = load_context('project_path')
    """

    project_name = 'ResolutionAnalysis'
    project_version = '0.16.3'
    package_name = 'take_resolution'


    def _get_pipelines(self) -> tp.Dict[str, Pipeline]:
        return create_pipelines()


def run_package():
    """Run method to run default pipeline."""
    project_path = pl.Path.cwd()
    package_name = pl.Path(__file__).resolve().parent.name
    project_context = load_package_context(project_path=project_path, package_name=package_name)
    project_context.run()


if __name__ == "__main__":
    run_package()
