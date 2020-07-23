# -*- coding: utf-8 -*-
__author__ = 'Gabriel Salgado'
__version__ = '0.11.1'

import typing as tp
import operator as op
import functools as ft
import pathlib as pl
from kedro.config import ConfigLoader
from kedro.pipeline import Pipeline
from kedro.framework.context import load_package_context
from take_resolution.utils import build_pipeline


def load_pipelines(loader: ConfigLoader, filename: str, variable: str = '') -> tp.Dict[str, Pipeline]:
    """Load pipelines from config.

    :param loader: Config loader.
    :type loader: ``kedro.config.config.ConfigLoader``
    :param filename: Filename to load config.
    :type filename: ``str``
    :param variable: Variable name.
    :type variable: ``str``
    :return: Pipeline in dict.
    :rtype: ``dict`` from ``str`` to ``kedro.pipeline.Pipeline``
    """
    pipelines = dict()
    dct_pipeline_setting = loader.get(filename)
    for key, pipeline_setting in dct_pipeline_setting.items():
        if variable:
            key = key.replace('VARIABLE', variable)
        pipelines[key] = build_pipeline(pipeline_setting, variable)
    return pipelines


def create_pipelines(**_) -> tp.Dict[str, Pipeline]:
    """Create all pipelines in the project.

    :return: All pipelines in a dict.
    :rtype: ``dict`` from ``str`` to ``kedro.pipeline.Pipeline``
    """
    pipelines = dict()
    package_name = pl.Path(__file__).resolve().parent.name
    context = load_package_context(pl.Path.cwd(), package_name)
    loader = context.config_loader
    filename = 'pipelines.yml'
    pipelines.update(load_pipelines(loader, filename))
    pipelines['__default__'] = ft.reduce(op.add, pipelines.values())
    return pipelines
