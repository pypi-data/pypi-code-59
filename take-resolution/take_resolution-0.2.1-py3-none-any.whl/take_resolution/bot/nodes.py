# -*- coding: utf-8 -*-
__author__ = 'Gabriel Salgado'
__version__ = '0.1.0'

import pandas as pd
import pyspark as ps


DF = pd.DataFrame
SDF = ps.sql.DataFrame


def select_bot(df: SDF, bot_column: str, bot: str) -> SDF:
    """Select element on table by bot.

    :param df: Spark dataframe.
    :type df: ``pyspark.sql.DataFrame``
    :param bot_column: Column that indicates the bot.
    :type bot_column: ``str``
    :param bot: Bot name.
    :type bot: ``str``
    :return: Filtered spark dataframe by bot.
    :rtype: ``pyspark.sql.DataFrame``
    """
    return df.filter(df[bot_column] == bot)


def select_flux(df: SDF, column: str) -> SDF:
    """Select bot flux column on spark dataframe.

    :param df: Spark dataframe.
    :type df: ``pyspark.sql.DataFrame``
    :param column: Column that indicates the bot flux.
    :type column: ``str``
    :return: Spark dataframe with only bot flux.
    :rtype: ``pyspark.sql.DataFrame``
    """
    return df.select(column)


def query(df: SDF) -> DF:
    """Query spark dataframe getting pandas dataframe.

    :param df: Spark dataframe.
    :type df: ``pyspark.sql.DataFrame``
    :return: Pandas dataframe with the data.
    :rtype: ``pandas.DataFrame``
    """
    return df.toPandas()
