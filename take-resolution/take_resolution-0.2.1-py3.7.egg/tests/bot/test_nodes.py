# -*- coding: utf-8 -*-
__author__ = 'Gabriel Salgado'
__version__ = '0.1.0'

import logging as lg
import typing as tp
import pytest
import pandas as pd
import pyspark as ps
import findspark
from take_resolution.bot.nodes import select_flux
from take_resolution.bot.nodes import select_bot
from take_resolution.bot.nodes import query


DF = pd.DataFrame
SDF = ps.sql.DataFrame
Session = ps.sql.SparkSession

session = None


def setup_module(module):
    findspark.init()
    lg.getLogger('py4j').setLevel(lg.WARN)
    module.session = ps.sql.SparkSession.builder \
        .master('local').appName('resolution').enableHiveSupport().getOrCreate()


def teardown_module(module):
    module.session.stop()


@pytest.fixture
def spark_session() -> Session:
    return session


@pytest.fixture
def df_spark(spark_session: Session) -> SDF:
    return spark_session.createDataFrame([
        ('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)
    ], ['first', 'second'])


@pytest.fixture
def df_pandas() -> DF:
    return pd.DataFrame([
        ('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)
    ], columns=['first', 'second'])


@pytest.mark.parametrize('column_value', [
    ('first', 'A'),
    ('first', 'B'),
    ('first', 'C'),
    ('first', 'D'),
    ('first', 'E'),
    ('second', 1),
    ('second', 2),
    ('second', 3),
    ('second', 4),
    ('second', 5)
])
def test__select_bot(df_spark: SDF, column_value: tp.Tuple[str, tp.Any]):
    column, value = column_value
    df = select_bot(df_spark, column, value)
    assert isinstance(df, ps.sql.DataFrame)
    assert len(df.columns) == len(df_spark.columns)
    assert len(df.toPandas()) == 1


@pytest.mark.parametrize('column', ['first', 'second'])
def test__select_flux(df_spark: SDF, column: str):
    df = select_flux(df_spark, column)
    assert isinstance(df, ps.sql.DataFrame)
    assert len(df.columns) == 1
    assert df.columns[0] == column


def test__query(df_spark: SDF, df_pandas: DF):
    df = query(df_spark)
    assert isinstance(df, pd.DataFrame)
    pd.testing.assert_frame_equal(df, df_pandas)
