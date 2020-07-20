import pandas as pd


def default_table_style(df):
    """ Apply a default clean table style to pandas df.to_html() for use in email strings.

    :param df: Dataframe to apply the style to.
    :type df: Pandas Dataframe
    :return: HTML string for insertion in email.
    :rtype: string
    """
    df = '''
            <head>
                <style>
                    table.dataframe {
                        border-collapse: collapse;
                    }
                    table.dataframe th{
                        border: 1px solid black;
                        padding: 10px;
                        font-size:14px;
                        text-align: center;
                    }
                    table.dataframe td {
                        border: 1px solid black;
                        padding: 10px;
                        font-size:12px;
                        text-align: center;
                    }
                }
                </style>
            </head>
            ''' + df.to_html(index=False)
    return df
