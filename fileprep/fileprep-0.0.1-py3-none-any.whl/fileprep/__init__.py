__version__ = '0.1.0'

import os
from datetime import datetime
import pandas as pd
import xlrd


def get_dfiles(path_source):
    """Switches to the given path sources and returns a file list for a given directory."""
    os.chdir(path_source)
    return os.listdir()


def get_files(path_source, ext):
    """ Parses a given dirpath for dirnames and filenames, walks through the dirpath, appends any xls filepath in "xls_list" while every other file is beeing recorded in "other_list"."""

    xls_list = []
    other_list = []

    for dirpath, dirnames, filenames in os.walk(path_source):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if file.endswith(".{}".format(ext)):
                xls_list.append(file_path)
            else:
                other_list.append(file_path)
    return pd.Series(xls_list), pd.Series(other_list)


def column_prep(df):
    """Lowers every column title, trims, removes special formatting and places an underscore instead of space."""

    df.columns = (
        df.columns.str.lower()
        .str.replace(",", " ")
        .str.replace("-", " ")
        .str.replace("/", " ")
        .str.replace(".", " ")
        .str.replace(":", " ")
        .str.replace("(", " ")
        .str.replace(")", " ")
        .str.replace("\\s+", " ", regex=True)
        .str.strip()
        .str.replace(" ", "_")
    )
    return


def meta_data(file, df):
    """Writes file based meta data to each row of a dataframe (file_name, file_c_time, file_import_time)."""
    df["file_name"] = file
    df["file_c_time"] = datetime.fromtimestamp(os.stat(file).st_ctime)
    df["file_import_time"] = datetime.now()
    return


def get_empty_rows(file):
    """ Finds empty rows. Works for table with a 2 column wide header and regular table later on."""

    empty_row_list = []
    empty_cell = False

    with xlrd.open_workbook(file) as wb:
        cs = wb.sheet_by_index(0)
        num_cols = cs.ncols
        num_rows = cs.nrows

        for row_index in range(0, num_rows):
            count_empty = 0

            for col_index in range(0, num_cols):
                cell_val = cs.cell(row_index, col_index).value

                if cell_val == "":
                    empty_cell = True
                    count_empty += 1
                else:
                    empty_cell = False

            if count_empty == num_cols:
                empty_row_list.append(row_index)
                # print ('Row {} is empty'.format(row_index))

    header = empty_row_list[0]
    table = empty_row_list[-1]
    data = empty_row_list[-1] + 1

    return header, table, data


def create_header_table(file, header):
    """ Creates a dictionary bases on 2 header columns and transposes it into a regular table with titles and content."""
    head_dict = {}

    with xlrd.open_workbook(file) as wb:
        cs = wb.sheet_by_index(0)

        for i in range(header):
            head_dict[cs.cell(i, 0).value] = [cs.cell(i, 1).value]

    return pd.DataFrame.from_dict(head_dict)
