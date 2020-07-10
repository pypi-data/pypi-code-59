import logging
import sys
import warnings
import json
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

warnings.filterwarnings("ignore")

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s  %(name)s  %(levelname)s: %(message)s",
)
logging.basicConfig(
    stream=sys.stderr,
    level=logging.ERROR,
    format="%(asctime)s  %(name)s  %(levelname)s: %(message)s",
)
logging.captureWarnings(True)

types_converter_dict = {
    "mysql:pg": {
        "type": {
            "char": "character",
            "varchar": "character varying",
            "tinytext": "text",
            "mediumtext": "text",
            "text": "text",
            "longtext": "text",
            "tinyblob": "bytea",
            "mediumblob": "bytea",
            "longblob": "bytea",
            "binary": "bytea",
            "varbinary": "bytea",
            "bit": "bit varying",
            "tinyint": "smallint",
            "tinyint unsigned": "smallint",
            "smallint": "smallint",
            "smallint unsigned": "integer",
            "mediumint": "integer",
            "mediumint unsigned": "integer",
            "int": "integer",
            "int unsigned": "bigint",
            "bigint": "bigint",
            "bigint unsigned": "numeric",
            "float": "real",
            "float unsigned": "real",
            "double": "double precision",
            "double unsigned": "double precision",
            "decimal": "numeric",
            "decimal unsigned": "numeric",
            "numeric": "numeric",
            "numeric unsigned": "numeric",
            "date": "date",
            "datetime": "timestamp without time zone",
            "time": "time without time zone",
            "timestamp": "timestamp without time zone",
            "year": "smallint",
            "enum": "character varying",
            "set": "ARRAY[]::text[]",
        },
        "default": {"current_timestamp": "now()"},
    },
    "mysql:vertica": {
        "type": {
            "text": "long varchar(65000)",
            "json": "long varchar(65000)",
            "enum": "long varchar",
            "double": "double precision",
        },
        "default": {"current_timestamp": "now()"},
    },
    "mysql:exasol": {
        "type": {
            "text": "varchar",
            "json": "varchar",
            "enum": "varchar",
            "blob": "varchar",
            "set": "varchar",
            "tinytext": "varchar",
            "datetime": "timestamp",
        },
        "default": {},
    },
    "ch:vertica": {
        "type": {
            "string": "long varchar(65000)",
            "uuid": "long varchar(65000)",
            "double": "double precision",
            "uint8": "integer",
            "uint16": "integer",
            "uint32": "integer",
            "uint64": "integer",
            "int64": "integer",
            "int8": "integer",
            "int16": "integer",
            "int32": "integer",
        },
        "default": {},
    },
    "pg:vertica": {
        "type": {
            "_text": "long varchar(65000)",
            "text": "long varchar(65000)",
            "jsonb": "long varchar(65000)",
            "json": "long varchar(65000)",
            "int2": "bigint",
            "int4": "bigint",
            "int8": "bigint",
            "float4": "double precision",
            "float8": "double precision",
            "numeric": "numeric precision",
        },
        "default": {},
    },
}

dialect_dict = {
    "ch": "clickhouse+native",
    "pg": "postgresql",
    "mysql": "mysql+pymysql",
    "vertica": "vertica+vertica_python",
    "exasol": "exa+pyodbc",
}

quotes_dict = {
    "ch": "`",
    "pg": '"',
    "mysql": '"',
    "vertica": '"',
    "exasol": '"',
}

max_length_mult = {
    "ch": 1,
    "pg": 1,
    "mysql": 1,
    "vertica": 1.8,
    "exasol": 1,
}

# types update to insert then
update_types_dict = {
    "ch": {"int32": "int", "int8": "bool", "str": "str", "float": "float"},
    "pg": {
        "double precision": "float",
        "integer": "int",
        "json": "json",
        "boolean": "bool",
    },
    "mysql": {
        "double precision": "float",
        "int": "int",
        "json": "json",
        "boolean": "bool",
    },
    "vertica": {
        "double precision": "float",
        "integer": "int",
        "json": "json",
        "boolean": "bool",
    },
    "exasol": {
        "double precision": "float",
        "integer": "int",
        "json": "json",
        "boolean": "bool",
    },
}


def update_value_type(fields, item, key, db="ch"):
    """
    :param db: db to update
    :param fields: dict - key  type
    :param item: - to upldate item
    :param key: key to updatee
    :return:
    """
    if db not in dialect_dict:
        raise ModuleNotFoundError(
            "Dialect for {} type of database was'nt found, should be in list {}".format(
                db, list(dialect_dict.keys())
            )
        )
    if item is None:
        return item
    if item[key] is None:
        return item
    type = "str"
    for type_old in update_types_dict[db]:
        if fields[key].lower().find(type_old) > -1:
            type = update_types_dict[db][type_old]

    if type == "int":
        item[key] = int(item[key])
    elif type == "float":
        item[key] = float(item[key])
    elif type == "json":
        item[key] = json.dumps(item[key])
    elif type == "bool":
        item[key] = bool(item[key])
    else:
        item[key] = str(item[key])
    return item


excluded_fields = ["password"]


def update_column_type(column, from_db, to_db):
    """convert types between source and destination"""
    key = "{}:{}".format(from_db, to_db)
    if key not in types_converter_dict:
        raise NotImplementedError(
            "table converter from {} to {} is not implemented".format(from_db, to_db)
        )

    type_from = column["data_type"]
    types_conv = types_converter_dict[key]["type"]
    if type_from in types_conv:
        type_to = types_conv[type_from]
    else:
        type_to = type_from

    if column["character_maximum_length"] is not None and type_to not in "text":
        type_to += "({character_maximum_length})".format(
            character_maximum_length=int(
                column["character_maximum_length"] * max_length_mult[to_db]
            )
        )
        return type_to
    if column["column_default"] is not None:
        default_from = column["column_default"].lower()
        if default_from in types_converter_dict[key]["default"]:
            default_to = types_converter_dict[key]["default"][default_from]
        else:
            default_to = default_from
        type_to += " default {column_default}".format(column_default=default_to)

    return type_to


def generate_sort_part_vertica(sort_part, date_field="date"):
    part = (
        "PARTITION BY EXTRACT(year FROM {date_field}) * 10000 + EXTRACT(MONTH FROM {date_field}) * 100 + EXTRACT("
        "day FROM {date_field})".format(date_field=date_field)
    )
    sort_field = sort_part[0]["SORTING_KEY"]
    if sort_field != "":
        sort = "ORDER BY {sort_field}".format(sort_field=sort_field)
    else:
        sort = ""
    return sort + " " + part


def get_type_sql_alchemy(type):
    try:
        return str(type.nested_type.__visit_name__).lower()
    except BaseException:
        return str(type.__visit_name__).lower()


def get_length_type_sql_alchemy(type):
    try:
        return type.length
    except BaseException:
        None


def get_default_arg_sql_alchemy(column):
    if column.default is not None:
        return column.default.arg
    elif column.server_default is not None:
        return str(column.server_default.arg)


def get_table_schema(table_name, meta):
    columns_name = [
        "column_name",
        "data_type",
        "character_maximum_length",
        "column_default",
    ]
    table_sql = Table(table_name, meta)
    columns = [c.name for c in table_sql.columns]
    types = [get_type_sql_alchemy(c.type) for c in table_sql.columns]
    length = [get_length_type_sql_alchemy(c.type) for c in table_sql.columns]
    default = [get_default_arg_sql_alchemy(c) for c in table_sql.columns]
    fields = list(zip(columns, types, length, default))
    fields = [dict(zip(columns_name, f)) for f in fields]
    return fields


class FieldsConverterOneWay:
    """
    class to upload just one way
    """

    def __init__(self, sql_credentials, db, debug=True, tables=None):
        """

        :param sql_credentials:
        :param db:
        :param debug: show debug text
        :param tables:  converter only for list of tables. Will process more rapid
        """
        self.tables = tables or []
        self.db = db
        self.debug = debug
        self.sql_credentials = sql_credentials
        cred = self.sql_credentials[self.db]

        if self.db not in dialect_dict:
            raise ModuleNotFoundError(
                "Dialect for {} type of database was'nt found, should be in list {}".format(
                    self.db, list(dialect_dict.keys())
                )
            )
        else:
            dialect_from = dialect_dict[self.db]
        uri_sql_alchemy = "{0}://{1}:{2}@{3}:{4}/{5}".format(
            dialect_from,
            cred["user"],
            cred["password"],
            cred["host"],
            cred["port"],
            cred["database"],
        )

        if "connect_args" in self.sql_credentials[self.db]:
            connect_args = self.sql_credentials[self.db]["connect_args"]
        else:
            connect_args = {}
        engine = create_engine(uri_sql_alchemy, connect_args=connect_args)
        self.conn = engine.connect()
        self.log("connecting to {} successfull".format(self.db))
        if "schema" in cred:
            self.schema = cred["schema"]
            self.meta = MetaData(bind=engine, schema=self.schema)
        else:
            self.meta = MetaData(bind=engine)

        if len(self.tables) > 0:
            self.meta.reflect(only=self.tables)
        else:
            self.meta.reflect()

    def log(self, text):
        if self.debug:
            logging.info(self.__str__ + ": " + text)

    def check_if_table_availible(self, table):
        if len(self.tables) > 0 and table not in self.tables:
            raise ModuleNotFoundError(
                "Table_name to convert {} should be in list{} or set tables param to defult".format(
                    table, self.tables
                )
            )

    @property
    def __str__(self):
        return "FieldsConverterOneWay_{}".format(self.db)

    @property
    def __repr__(self):
        return "FieldsConverterOneWay_{}".format(self.db)

    def __del__(self):
        self.conn.close()

    def update_value_type(self, table_name, items):
        """
        :param items: list of dicts to update
        :param table_name: table_name to insert
        :return:
        """
        fields = self.get_columns(table_name=table_name)
        keys = fields.keys()
        for item in items:
            for key in keys:
                item = update_value_type(fields, item, key, db=self.db)
        return items

    def get_columns(self, table_name):
        """get column:type dict"""
        self.check_if_table_availible(table_name)
        fields = get_table_schema(table_name, self.meta)
        columns = [
            f["column_name"] for f in fields if f["column_name"] not in excluded_fields
        ]
        types = [
            f["data_type"] for f in fields if f["column_name"] not in excluded_fields
        ]
        return dict(zip(columns, types))


class FieldsConverter:
    def __init__(self, sql_credentials, from_db, to_db, debug=True, tables=None):
        """

        :param sql_credentials:
        :param from_db:
        :param to_db:
        :param debug: show debug text
        :param tables: converter only for list of tables. Will process more rapidly
        """
        self.tables = tables or []
        self.from_db = from_db
        self.to_db = to_db
        self.debug = debug
        self.sql_credentials = sql_credentials

        cred_from = self.sql_credentials[self.from_db]

        if self.from_db not in dialect_dict:
            raise ModuleNotFoundError(
                "Dialect for {} type of database was'nt found, should be in list {}".format(
                    self.from_db, list(dialect_dict.keys())
                )
            )
        else:
            dialect_from = dialect_dict[self.from_db]

        uri_sql_alchemy_from = "{0}://{1}:{2}@{3}:{4}/{5}".format(
            dialect_from,
            cred_from["user"],
            cred_from["password"],
            cred_from["host"],
            cred_from["port"],
            cred_from["database"],
        )
        cred_to = self.sql_credentials[self.to_db]
        if self.to_db not in dialect_dict:
            raise ModuleNotFoundError(
                "Dialect for {} type of database was'nt found, should be in list {}".format(
                    self.to_db, list(dialect_dict.keys())
                )
            )
        else:
            dialect_to = dialect_dict[self.to_db]

        uri_sql_alchemy_to = "{0}://{1}:{2}@{3}:{4}/{5}".format(
            dialect_to,
            cred_to["user"],
            cred_to["password"],
            cred_to["host"],
            cred_to["port"],
            cred_to["database"],
        )
        self.quote_char = quotes_dict[self.to_db]
        if "connect_args" in self.sql_credentials[self.from_db]:
            connect_args = self.sql_credentials[self.from_db]["connect_args"]
        else:
            connect_args = {}
        engine_from = create_engine(uri_sql_alchemy_from, connect_args=connect_args)
        self.conn_from = engine_from.connect()
        self.log("connecting to {} successfull".format(self.from_db))

        if "connect_args" in self.sql_credentials[self.to_db]:
            connect_args = self.sql_credentials[self.to_db]["connect_args"]
        else:
            connect_args = {}
        engine_to = create_engine(uri_sql_alchemy_to, connect_args=connect_args)
        self.conn_to = engine_to.connect()
        self.log("connecting to {} successfull".format(self.to_db))
        if "schema" in cred_from:
            self.schema_from = cred_from["schema"]
            self.meta_from = MetaData(bind=engine_from, schema=self.schema_from)
        else:
            self.meta_from = MetaData(bind=engine_from)

        if "schema" in cred_to:
            self.schema_to = cred_to["schema"]
            self.meta_to = MetaData(bind=engine_to, schema=self.schema_to)
        else:
            self.meta_to = MetaData(bind=engine_to)

        if len(self.tables) > 0:
            self.meta_from.reflect(only=self.tables)
            self.meta_to.reflect(only=self.tables)
        else:
            self.meta_from.reflect()
            self.meta_to.reflect()

    def log(self, text):
        if self.debug:
            logging.info(self.__str__ + ": " + text)

    def check_if_table_availible(self, table):
        if len(self.tables) > 0 and table not in self.tables:
            raise ModuleNotFoundError(
                "Table_name to convert {} should be in list{} or set tables param to defult".format(
                    table, self.tables
                )
            )

    @property
    def __str__(self):
        return "FieldsConverter_{}_{}".format(self.from_db, self.to_db)

    @property
    def __repr__(self):
        return "FieldsConverter_{}_{}".format(self.from_db, self.to_db)

    def __del__(self):
        self.conn_from.close()
        self.conn_to.close()

    def update_value_type(self, table_name, items):
        """
        :param items: list of dicts to update
        :param table_name: table_name to insert
        :return:
        """
        fields = self.get_columns(table_name=table_name, table_from=False)
        keys = fields.keys()
        for item in items:
            for key in keys:
                item = update_value_type(fields, item, key, db=self.to_db)
        return items

    def generate_create(self, fields, table_name, sort_part=None):
        add_part = ""
        if self.schema_to:
            cur_schema = self.schema_to
        else:
            cur_schema = ""
        if self.to_db == "vertica":
            if "date" in [f.lower() for f in fields.keys()]:
                date_field = "date"
            else:
                date_field = ""
            if sort_part is not None:
                add_part = generate_sort_part_vertica(sort_part, date_field=date_field)
                if (
                    date_field != ""
                    and fields[date_field].lower().find("not null") == -1
                ):
                    fields[date_field] += " not null"
        elif self.to_db == "exasol":
            cur_schema = self.exasol_schema
        txt = "CREATE TABLE IF NOT EXISTS {schema}.{table} (".format(
            schema=cur_schema, table=table_name
        )

        txt += ",".join(
            [
                self.quote_char + field + self.quote_char + " " + str(fields[field])
                for field in fields
                if field not in excluded_fields
            ]
        )
        txt += ")"

        return txt + " " + add_part

    def get_partition_and_sort_keys_ch(self, table_name):
        columns = ["PARTITION_KEY", "SORTING_KEY", "ENGINE"]
        sql = """SELECT partition_key, 
                        sorting_key,
                        engine
                        FROM system.tables
                        WHERE name = '{table_name}'
                              AND database = '{database}'
              """.format(
            table_name=table_name, database=self.ch_database
        )
        rows = self.conn_from.execute(sql)
        if rows[0][2] == "MaterializedView":
            return self.get_partition_and_sort_keys_ch(".inner." + table_name)
        else:
            return [dict(zip(columns, r)) for r in rows]

    def get_columns(self, table_name, table_from=True):
        """get column:type dict"""
        self.check_if_table_availible(table_name)
        if table_from:
            fields = get_table_schema(table_name, self.meta_from)
        else:
            fields = get_table_schema(table_name, self.meta_to)
        columns = [
            f["column_name"] for f in fields if f["column_name"] not in excluded_fields
        ]
        types = [
            f["data_type"] for f in fields if f["column_name"] not in excluded_fields
        ]
        return dict(zip(columns, types))

    def create_ddl(self, table_name):
        sort_part = None
        self.check_if_table_availible(table_name)
        fields = get_table_schema(table_name, self.meta_from)
        fields_new = {}
        for f in fields:
            fields_new[f["column_name"]] = update_column_type(
                f, self.from_db, self.to_db
            )
        return self.generate_create(
            fields_new, table_name.replace("_data", ""), sort_part
        )

    def drop_list_of_tables(self, tables):
        """drop every fkn table in list"""
        for table in tables:
            sql = "drop table {schema}.{table} cascade ".format(
                schema=self.schema_to, table=table
            )
            self.conn_to.execute(sql)

    def create_list_of_tables(self, tables, to_create=True, dir=None):
        result_list = []
        for table in tables:
            sql = self.create_ddl(table_name=table)
            result_list.append(sql)
            if to_create:
                self.conn_to.execute(sql)
                logging.info("creating table {} is successfull".format(table))
            if dir is not None:
                f = open(
                    dir
                    + "/"
                    + self.schema_to
                    + "_"
                    + table.replace("_date", "")
                    + ".sql",
                    "w",
                )
                f.write(sql)
                f.close()
        return result_list
