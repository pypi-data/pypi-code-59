from collections import defaultdict

class RownumMaker(object):

    cols = defaultdict(int)
    col = None
    rownum = 0

    @classmethod
    def increment(cls, col):
        cls.cols[col] += 1
        return cls.cols[col]

    @classmethod
    def increment_turbo(cls, col):
        if cls.col == col:
            cls.rownum += 1
        else:
            cls.col = col
            cls.rownum = 1

        return cls.rownum

class TypeConverter(object) :

    @staticmethod
    def dt_to_str(df) :
        dt_cols = [i for i, d in zip(df.dtypes.index, df.dtypes) if d == 'datetime64[ns]']
        for col in dt_cols :
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
        return df

    @staticmethod
    def change_type(df, db_dtypes):
        # print(df.to_json())
        correct_pairs = [
            ("object", "VARCHAR"),
            ("int64", "INTEGER"),
            ("int64", "BIGINT"),
            ("int64", "TINYINT"),
            ("object", "TIMESTAMP"),
            ("object", "DATETIME"),
            ("float64", "DECIMAL"),
            ("float64", "DOUBLE"),
            ("object", "TEXT"),
            ("object", "TINYTEXT"),
        ]
        dtypes_df = df.dtypes.reset_index()
        dtypes_df.columns = ['col_nm', 'df_type']
        dtypes_df['db_type'] = dtypes_df.col_nm.apply(lambda x: db_dtypes.get(x, None))
        dtypes_df.df_type = dtypes_df.df_type.astype(str)
        for col in dtypes_df.values:
            if col[1] in ['int64', 'float64']:
                df[col[0]] = df[col[0]].fillna(0)
            elif col[1] in ['object']:
                df[col[0]] = df[col[0]].fillna('')
            else:
                pass
            if tuple(col[1:]) not in correct_pairs:
                if col[-1] in ['VARCHAR', 'TEXT'] :
                    if col[1] == 'int64' :
                        df[col[0]] = df[col[0]].astype(str)
                    elif col[1] == 'float64' :
                        df[col[0]] = df[col[0]].astype(int).astype(str)
                    else :
                        raise Exception('Cannot convert {} to {} ( {} )1 : '.format(col[1], col[-1], col[0]))
                elif col[-1] in ['INTEGER', 'BIGINT', 'TINYINT'] :
                    if col[1] == 'float64' :
                        df[col[0]] = df[col[0]].astype(int)
                    elif col[1] == 'object' :
                        df[col[0]] = df[col[0]].apply(lambda x : 0 if not x else x).astype(int)
                    else :
                        raise Exception('Cannot convert {} to {} ( {} )2'.format(col[1], col[-1], col[0]))
                elif col[-1] in ['DECIMAL', 'DOUBLE']:
                    if col[1] == 'int64' :
                        df[col[0]] = df[col[0]].astype(float).astype(str)
                    elif col[1] == 'object' :
                        try :
                            if col[0] in ['partial_can_rtn_flag'] :
                                df[col[0]] = df[col[0]].apply(lambda x: 0 if not x else x).astype(float)
                            else :
                                df[col[0]] = df[col[0]].apply(lambda x : 0 if not x else x).astype(float).astype(str)
                        except :
                            raise Exception('Cannot convert {} to {} ( {} )3'.format(col[1], col[-1], col[0]))
                    else :
                        raise Exception('Cannot convert {} to {} ( {} )4'.format(col[1], col[-1], col[0]))​
                        elif col[-1] in ['TIMESTAMP', 'DATETIME']:
                            if col[1] == 'datetime64[ns]':
                        df[col[0]] = df[col[0]].dt.strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        raise Exception('Cannot convert {} to {} ( {} )5'.format(col[1], col[-1], col[0]))
                elif col[-1] in ['TEXT', 'TINYTEXT'] :
                    print("-"*30)

                else:
                    raise Exception('Cannot convert {} to {} ( {} )'.format(col[1], col[-1], col[0]))

        return df