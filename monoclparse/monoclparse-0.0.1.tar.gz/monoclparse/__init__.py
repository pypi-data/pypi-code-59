import os

from glob import glob
from pathlib import Path

import pandas as pd

from .util import format_column_name
from ._version import __version__


def read_report(path: Path) -> pd.DataFrame:
    """Read a Monocl Excel report into a Pandas dataframe."""
    df = pd.read_excel(io=path, header=[6, 7])
    df.columns = list(map(format_column_name, df.columns))
    df = df.drop([df.columns[-1], df.columns[0]], axis=1)
    return df


def monocl_report_to_tsv(input: Path, output: Path) -> None:
    """Convert a Monocl Excel report into a TSV file with a single header."""
    read_report(input).to_csv(output, sep='\t', index=False)
