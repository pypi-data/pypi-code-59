#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A custom object for MySQL, to operate the MySQL database."""
from typing import Any, Dict
import pymysql
import sys


class Util_MySQL:
    def __init__(self, host_info: Dict[str, Any]) -> None:
        """The format of host_info:\n
            host_info = {\n
                "host": "host", # required
                "port": 3306, # optional, default is 3306
                "user": "user", # required
                "password": "password", # required
                "database": "mysql", # optional
            }"""

        expr = True
        expr_list = ["host", "user", "password"]
        for _ in expr_list:
            if _ not in host_info:
                expr = False
        if "port" not in host_info:
            host_info["port"] = 3306
        # if "charset" not in host_info:
        #     host_info["charset"] = "UTF-8"
        if expr:
            self.host_info = host_info
        else:
            sys.exit("There is an error in the database connection information.")

    def _connect(self):
        self.db_conn = pymysql.connect(
            host=self.host_info["host"],
            port=self.host_info["port"],
            user=self.host_info["user"],
            password=self.host_info["password"],
            # charset=self.host_info["charset"]
        )
        if "database" in self.host_info:
            tmp_cur = self.db_conn.cursor()
            tmp_cur.execute(f'use {self.host_info["database"]};')
            return tmp_cur
        else:
            return self.db_conn.cursor()

    def Query(self, sql: str):
        """Query data from the database.

        :param sql(str): It's a sql statement."""

        cur = self._connect()
        try:
            cur.execute(sql)
            data = cur.fetchall()
        except Exception as e:
            print("sql statement is " + sql)
            sys.exit(e)
        cur.close()
        self.db_conn.close()
        return data

    def Change(self, sql: str):
        """Change the data in the database.

        :param sql(str): It's a sql statement."""

        cur = self._connect()
        try:
            cur.execute(sql)
            self.db_conn.commit()
        except Exception as e:
            self.db_conn.rollback()
            print("sql statement is " + sql)
            sys.exit(e)
        cur.close()
        self.db_conn.close()

    # def _check(self, params, method, options):
    #     for option in options:
    #         if option not in params:
    #             sys.exit(
    #                 f"The parameter {option} is required to execute the {method} method")

    # def Query(self, params: Dict[str, str]):
    #     """Query data from the database. Return the data which matched the params.

    #     :param params(Dict[str, str]): The parameter of query sql.\n
    #         It's like filling them in the sql statement.
    #         The format of params:
    #             params = {
    #                 "table": "name", # required
    #                 "col": "col", # optional, default is Asterisk(*)
    #                 "where": "where", #  optional
    #             }
    #         Example:
    #             table: "db.table" or "table" or "table as t", etc.
    #             col: "col" or "table.col" or "col as c", etc.
    #             where: "col='xxx'" or "col1='xxx' and col2='yyy'", etc."""

    #     required_option = ["table"]
    #     self._check(params, self.Query, required_option)
    #     cur = self._connect()
    #     sql_where = ''
    #     sql_col = '*'
    #     if "where" in params:
    #         sql_where = "WHERE " + params["where"]
    #     if "col" in params:
    #         sql_col = params["col"]
    #     sql = f"SELECT {sql_col} FROM {params['table']} {sql_where};"
    #     try:
    #         cur.execute(sql)
    #         data = cur.fetchall()
    #     except Exception as e:
    #         print("sql statement is " + sql)
    #         sys.exit(e)
    #     cur.close()
    #     self.db_conn.close()
    #     return data

    # def NoQuery(self, method: str, params: Dict[str, str]):
    #     """Change the data in the database.

    #     :param method(str): The method which where be executed.\n
    #     :param params(Dict[str, str]): The parameter of sql.\n
    #         It's like filling them in the sql statement.
    #         The format of params:
    #             params = {
    #                 "table": "name", # required
    #                 "where": "where", # required by delete method and update method. It is not safe to update a whole column of data, so there must be a where statement even if the method is update.
    #                 "info": "info", # required by update method.
    #                 "values": "values", # required by insert method. If no column name is specified, the data is added to the columns of the table in order until the data insertion is complete.
    #             }
    #         Example:
    #             table: "db.table" or "table" or "table as t", etc. where method is insert, "table(col1, col3...)" is also legal.
    #             where: "col='xxx'" or "col1='xxx' and col2='yyy'", etc.
    #             info: "col1='xxx'" or "col1='xxx', col2='yyy'", etc.
    #             values: "xxx" or "xxx, yyy", etc."""

    #     if method == "insert":
    #         required_option = ["table", "values"]
    #         self._check(params, self.Query, required_option)
    #         sql = f"INSERT INTO {params['table']} VALUES({params['values']})"
    #     elif method == "update":
    #         required_option = ["table", "where", "info"]
    #         self._check(params, self.Query, required_option)
    #         sql = f"UPDATE {params['table']} SET {params['info']} WHERE {params['where']};"
    #     elif method == "delete":
    #         required_option = ["table", "where"]
    #         self._check(params, self.Query, required_option)
    #         sql = f"DELETE FROM {params['table']} WHERE {params['where']};"
    #     else:
    #         sys.exit()

    #     cur = self._connect()
    #     try:
    #         cur.execute(sql)
    #         self.db_conn.commit()
    #     except Exception as e:
    #         self.db_conn.rollback()
    #         print("sql statement is " + sql)
    #         sys.exit(e)
    #     cur.close()
    #     self.db_conn.close()
