"""
Copyright (c) 2018 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: rameshchandra.d@teradata.com
Secondary Owner: sanath.vobilisetty@teradata.com

teradataml db utilities
----------
A teradataml database utility functions provide interface to Teradata Vantage common tasks such as drop_table, drop_view, create_table etc.
"""
import pandas as pd
from sqlalchemy.sql.functions import Function
import teradataml.context.context as tdmlctx
from teradataml.common.utils import UtilFuncs
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.constants import TeradataTableKindConstants
from teradataml.common.sqlbundle import SQLBundle
from teradataml.common.constants import SQLConstants
from teradataml.utils.validators import _Validators
from teradatasql import OperationalError
from teradatasqlalchemy.dialect import preparer, dialect as td_dialect

def db_drop_table(table_name, schema_name = None):
    """
    DESCRIPTION:
        Drops the table from the given schema.

    PARAMETERS:
        table_name:
            Required Argument
            Specifies the table name to be dropped.
            Types: str

        schema_name:
            Optional Argument
            Specifies schema of the table to be dropped. If schema is not specified, function drops table from the
            current database.
            Default Value: None
            Types: str

    RETURNS:
        True - if the operation is successful.

    RAISES:
        TeradataMlException - If the table doesn't exist.

    EXAMPLES:
        >>> load_example_data("dataframe", "admissions_train")

        # Drop table in current database
        >>> db_drop_table(table_name = 'admissions_train')

        # Drop table from the given schema
        >>> db_drop_table(table_name = 'admissions_train', schema_name = 'alice')
    """
    # Argument validations
    awu_matrix = []
    awu_matrix.append(["schema_name", schema_name, True, (str), True])
    awu_matrix.append(["table_name", table_name, False, (str), True])

    # Validate argument types
    _Validators._validate_function_arguments(awu_matrix)

    # Joining view and schema names in the format "schema_name"."view_name"
    table_name = _get_quoted_object_name(schema_name, table_name)

    try:
        return UtilFuncs._drop_table(table_name)
    except TeradataMlException:
        raise
    except OperationalError:
        raise
    except Exception as err:
        raise TeradataMlException(Messages.get_message(MessageCodes.DROP_FAILED, "table", table_name),
                                  MessageCodes.DROP_FAILED) from err

def db_drop_view(view_name, schema_name = None):
    """
    DESCRIPTION:
        Drops the view from the given schema.

    PARAMETERS:
        view_name:
            Required Argument
            Specifies view name to be dropped.
            Types: str

        schema_name:
            Optional Argument
            Specifies schema of the view to be dropped. If schema is not specified, function drops view from the current
            database.
            Default Value: None
            Types: str

    RETURNS:
        True - if the operation is successful.

    RAISES:
        TeradataMlException - If the view doesn't exist.

    EXAMPLES:
        # Create a view
        >>> connection_object.execute("create view temporary_view as (select 1 as dummy_col1, 2 as dummy_col2);")

        # Drop view in current schema
        >>> db_drop_view(view_name = 'temporary_view')

        # Drop view from the given schema
        >>> db_drop_view(view_name = 'temporary_view', schema_name = 'alice')
    """
    # Argument validations
    awu_matrix = []
    awu_matrix.append(["schema_name", schema_name, True, (str), True])
    awu_matrix.append(["view_name", view_name, False, (str), True])

    # Validate argument types
    _Validators._validate_function_arguments(awu_matrix)

    # Joining view and schema names in the format "schema_name"."view_name"
    view_name = _get_quoted_object_name(schema_name, view_name)

    try:
        return UtilFuncs._drop_view(view_name)
    except TeradataMlException:
        raise
    except OperationalError:
        raise
    except Exception as err:
        raise TeradataMlException(Messages.get_message(MessageCodes.DROP_FAILED, "view", view_name),
                                  MessageCodes.DROP_FAILED) from err

def db_list_tables(schema_name=None, object_name=None, object_type='all'):
    """
    DESCRIPTION:
        Lists the Vantage objects(table/view) names for the specified schema name.

    PARAMETERS:
        schema_name:
            Optional Argument.
            Specifies the name of schema in the database. If schema is not specified, function lists tables/views from
            the current database.
            Default Value: None
            Types: str

        object_name:
            Optional Argument.
            Specifies a table/view name or pattern to be used for filtering them from the database.
            Pattern may contain '%' or '_' as pattern matching characters.
            A '%' represents any string of zero or more arbitrary characters. Any string of characters is acceptable as
            a replacement for the percent.
            A '_' represents exactly one arbitrary character. Any single character is acceptable in the position in
            which the underscore character appears.
            Default Value: None
            Types: str
            Example:
                1. '%abc' will return all table/view object names starting with any character and ending with abc.
                2. 'a_c' will return all table/view object names starting with 'a', ending with 'c' and has length of 3.

        object_type:
            Optional Argument.
            Specifies object type to apply the filter. Valid values for this argument are 'all','table','view',
            'volatile','temp'.
                * all - List all the object types.
                * table - List only tables.
                * view - List only views.
                * volatile - List only volatile tables.
                * temp - List all teradataml temporary objects created in the specified database.
            Default Value: 'all'
            Types: str

    RETURNS:
        Pandas DataFrame

    RAISES:
        TeradataMlException - If the object_type argument is provided with invalid values.
        OperationalError    - If any errors are raised from Vantage.

    EXAMPLES:
        # Example 1 - List all object types in the default schema
        >>> load_example_data("dataframe", "admissions_train")
        >>> db_list_tables()

        # Example 2 - List all the views in the default schema
        >>> connection_object.execute("create view temporary_view as (select 1 as dummy_col1, 2 as dummy_col2);")
        >>> db_list_tables(None , None, 'view')

        # Example 3 - List all the object types in the the default schema whose names begin with 'abc' followed by one
        # arbitrary character and any number of characters in the end.
        >>> connection_object.execute("create view abcd123 as (select 1 as dummy_col1, 2 as dummy_col2);")
        >>> db_list_tables(None, 'abc_%', None)

        # Example 4 - List all the tables in the default schema whose names begin with 'adm_%' followed by one
        # arbitrary character and any number of characters in the end.
        >>> load_example_data("dataframe", "admissions_train")
        >>> db_list_tables(None, 'adm_%', 'table')

        # Example 5 - List all the views in the default schema whose names begin with any character but ends with 'abc'
        >>> connection_object.execute("create view view_abc as (select 1 as dummy_col1, 2 as dummy_col2);")
        >>> db_list_tables(None, '%abc', 'view')

        # Example 6 - List all the volatile tables in the default schema whose names begin with 'abc' and ends with any
        # arbitrary character and has a length of 4
        >>> connection_object.execute("CREATE volatile TABLE abcd(col0 int, col1 float) NO PRIMARY INDEX;")
        >>> db_list_tables(None, 'abc_', 'volatile')

        # Example 7 - List all the temporary objects created by teradataml in the default schema whose names begins and
        # ends with any number of arbitrary characters but contains 'filter' in between.
        >>> db_list_tables(None, '%filter%', 'temp')
    """

    if tdmlctx.get_connection() is None:
        raise TeradataMlException(Messages.get_message(MessageCodes.INVALID_CONTEXT_CONNECTION),
                                  MessageCodes.INVALID_CONTEXT_CONNECTION)

    # Argument validations
    awu_matrix = []
    awu_matrix.append(["schema_name", schema_name, True, (str), True])
    awu_matrix.append(["object_name", object_name, True, (str), True])
    permitted_object_types = [TeradataTableKindConstants.ALL.value, TeradataTableKindConstants.TABLE.value,
                             TeradataTableKindConstants.VIEW.value, TeradataTableKindConstants.VOLATILE.value,
                             TeradataTableKindConstants.TEMP.value]
    awu_matrix.append(["object_type", object_type, True, (str), True, permitted_object_types])

    # Validate argument types
    _Validators._validate_function_arguments(awu_matrix)

    try:
        return _get_select_table_kind(schema_name, object_name, object_type)
    except TeradataMlException:
        raise
    except OperationalError:
        raise
    except Exception as err:
        raise TeradataMlException(Messages.get_message(MessageCodes.LIST_DB_TABLES_FAILED),
                                  MessageCodes.LIST_DB_TABLES_FAILED) from err

def _get_select_table_kind(schema_name, table_name, table_kind):
    """
    Get the list of the table names from the specified schema name.

    PARAMETERS:
        schema_name - The Name of schema in the database. The default value is the current database name.
        table_name -  The pattern to be used to filtering the table names from the database.
                      The table name argument can contain '%' as pattern matching charecter.For example '%abc'
                      will return all table names starting with any charecters and ending with abc.
        table_kind -  The table kind to apply the filter. The valid values are 'all','table','view','volatile','temp'.
                      all - list the all the table kinds.
                      table - list only tables.
                      view - list only views.
                      volatile - list only volatile temp.
                      temp - list all teradata ml temporary objects created in the specified database.
    RETURNS:
        Panda's DataFrame - if the operation is successful.

    RAISES:
        Database error if an error occurred while executing query.

    EXAMPLES:
        _get_select_table_kind("schema_name", "table_name", "all")
    """
    object_name_str = None
    if table_name is not None:
        object_name_str = "'{0}'".format(table_name)
    object_table_kind = None

    # Check the schema name.
    if schema_name is None:
        schema_name = tdmlctx._get_current_databasename()

    # Check the table kind.
    if (table_kind == TeradataTableKindConstants.VOLATILE.value):
        query = SQLBundle._build_help_volatile_table()
    else:
        # Tablekind:
        # 'O' - stands for Table with no primary index and no partitioning
        # 'Q' - stands for Queue table
        # 'T' - stands for a Table with a primary index or primary AMP index, partitioning, or both.
        #       Or a partitioned table with NoPI
        # 'V' - stands for View
        if (table_kind == TeradataTableKindConstants.TABLE.value):
            object_table_kind = "'{0}','{1}','{2}'".format('O', 'Q', 'T')
        elif (table_kind == TeradataTableKindConstants.VIEW.value):
            object_table_kind = "'{0}'".format('V')
        elif (table_kind == TeradataTableKindConstants.TEMP.value):
            if table_name is None:
                object_name_str = "'{0}'".format(TeradataTableKindConstants.ML_PATTERN.value)
            else:
                object_name_str = "'{0}','{1}'".format(table_name,TeradataTableKindConstants.ML_PATTERN.value)
        else:
            object_table_kind = "'{0}','{1}','{2}','{3}'".format('O', 'Q', 'T', 'V')
        query = SQLBundle._build_select_table_kind(schema_name, object_name_str, object_table_kind)

    try:
        pddf = pd.read_sql(query, tdmlctx.td_connection.connection)
        # Check if all table kind is requested and add also volatile tables to the pdf.
        if (table_kind == TeradataTableKindConstants.ALL.value):
            try:
                #add volatile tables to all dataframe.
                vtquery = SQLBundle._build_help_volatile_table()
                vtdf = pd.read_sql(vtquery, tdmlctx.td_connection.connection)
                if not vtdf.empty:
                    vtdf.rename(columns={TeradataTableKindConstants.VOLATILE_TABLE_NAME.value: TeradataTableKindConstants.REGULAR_TABLE_NAME.value}, inplace=True)
                    frames = [pddf, vtdf[[TeradataTableKindConstants.REGULAR_TABLE_NAME.value]]]
                    pddf = pd.concat(frames)
                    pddf.reset_index(drop=True, inplace=True)
            except Exception as err:
                pass #no volatle tables exist.
        if (table_kind == TeradataTableKindConstants.VOLATILE.value):
            pddf.rename(columns={TeradataTableKindConstants.VOLATILE_TABLE_NAME.value: TeradataTableKindConstants.REGULAR_TABLE_NAME.value}, inplace=True)
            return pddf[[TeradataTableKindConstants.REGULAR_TABLE_NAME.value]]
        else:
            return pddf
    except Exception as err:
        return pd.DataFrame()


def _execute_transaction(queries):
    """
    Internal function to execute the query or list of queries passed, as one transaction.

    PARAMETERS:
        queries:
            Required argument.
            Specifies a query or a list of queries to be executed as a single transaction.
            Types: str or list of str

    RAISES:
        Exception

    RETURNS:
        None.

    EXAMPLES:
        >>> _execute_transaction([query1, query2])
    """
    auto_commit_off = "{fn teradata_nativesql}{fn teradata_autocommit_off}"
    auto_commit_on = "{fn teradata_nativesql}{fn teradata_autocommit_on}"
    con = None
    cur = None

    if queries is not None:
        if isinstance(queries, str):
            queries = [queries]

        # Check if we have any queries to execute
        if len(queries) == 0:
            return

        try:
            con = tdmlctx.td_connection
            if con is None:
                raise TeradataMlException(Messages.get_message(MessageCodes.CONNECTION_FAILURE),
                                          MessageCodes.CONNECTION_FAILURE)
            con = con.connection
            cur = con.cursor()
            # Set auto_commit to OFF
            cur.execute(auto_commit_off)
            for query in queries:
                cur.execute(query)

            # Try committing the the transaction
            con.commit()
        except Exception:
            # Let's first rollback
            con.rollback()
            # Now, let's raise the error as is
            raise
        finally:
            # Finally, we must set auto_commit to ON
            cur.execute(auto_commit_on)

def _execute_stored_procedure(function_call, fetchWarnings=True, expect_none_result=False):
    """
    DESCRIPTION:
       Executes the specified function call of the stored procedure which contains
       function name and parameters used by the function.

    PARAMETERS:
        function_call:
            Required argument.
            Specifies Function object for the stored procedure to be executed.
            This function object contains stored procedure name along with its arguments.
            Types: sqlalchemy.sql.functions.Function

        fetchWarnings:
            Optional Argument.
            Specifies a flag that decides whether to raise warnings thrown from Vantage or not.
            This will be the ideal behaviour for most of the stored procedures to fetch the warnings.
            Default Values: True
            Types: bool

        expect_none_result:
            Optional Argument.
            When set to True, warnings will be ignored, and only result set is returned.
            Returns None if query does not produce a result set.
            This option is ignored when fetchWarnings is set to True.
            Default Values: False
            Types: bool

    RETURNS:
           Results received from Vantage after the execution.

    RAISES:
           Exception thrown by the Vantage.

    EXAMPLES:
        # No parameter needed by stored procedure.
        functioncall = func.SYSUIF.list_base_environments()
        _execute_stored_procedure(functioncall)

        # Parameters are passed to the stored procedure in a list.
        functioncall = func.SYSUIF.install_file('myfile','mapper.py','cz!/documents/mapper.py')
        _execute_stored_procedure("SYSUIF.install_file(functioncall)", fetchWarnings=True)
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["function_call", function_call, False, (Function)])
    __arg_info_matrix.append(["fetchWarnings", fetchWarnings, True, (bool)])
    __arg_info_matrix.append(["expect_none_result", expect_none_result, True, (bool)])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    sqlbundle = SQLBundle()

    # Get the query for running stored procedure.
    exec_sp_stmt = sqlbundle._get_sql_query(SQLConstants.SQL_EXEC_STORED_PROCEDURE)

    return UtilFuncs._execute_query(exec_sp_stmt.format(_get_function_call_as_string(function_call)), fetchWarnings, expect_none_result)


def _get_function_call_as_string(sqlcFuncObj):
    """
    DESCRIPTION:
        This function returns string representation for the sqlalchemy.sql.functions.Function object
        which will be used to create a query to be used to execute the function.

    PARAMETERS:
        sqlcFuncObj:
            Required Argument.
            Specifies function object representing the SQL function call to be executed.

        RAISES:
            None

        RETURNS:
            String representation of the input Function.

        EXAMPLES:
            functioncall = func.SYSUIF.install_file("tdml_testfile", "test_script", "/root/test_script.py")
            _get_function_call_as_string(functioncall)

        Output:
            "SYSUIF.install_file('tdml_testfile', 'test_script', '/root/test_script.py')"
    """
    # This is done by _exec_stored_procedure
    from teradatasqlalchemy.dialect import dialect as td_dialect
    kw = dict({'dialect': td_dialect(),
               'compile_kwargs':
                   {
                       'include_table': False,
                       'literal_binds': True
                   }
               })

    return str(sqlcFuncObj.compile(**kw))

def _get_quoted_object_name(schema_name, object_name):
    """
    DESCRIPTION:
        This function quotes and joins schema name to the object name which can either be table or a view.

    PARAMETERS:
        schema_name
            Required Argument.
            Specifies the schema name.
            Types: str

        object_name
            Required Argument.
            Specifies the object name either table or view.
            Types: str

    RAISES:
        None

    RETURNS:
        Quoted and joined string of schema and object name.

    EXAMPLES:
        _get_quoted_object_name(schema_name = "alice", object_name = "admissions_train")

    OUTPUT:
        '"alice"."admissions_train"'
    """
    tdp = preparer(td_dialect)
    schema_name = tdp.quote(schema_name) if schema_name is not None else tdp.quote(tdmlctx._get_current_databasename())
    quoted_object_name = "{0}.{1}".format(schema_name, tdp.quote(object_name))
    return quoted_object_name